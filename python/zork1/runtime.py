"""Runtime support for the Python translation of Zork I.

The translated game (game.py) keeps the data model of the original
Z-machine program: tables, vocabulary entries, property tables and the
parser's lexical buffers live in a byte-addressed memory image, and the
routines manipulate them with GET/PUT/GETB/PUTB just as the ZIL code did.
This module provides that memory, the object tree, text encoding,
input/output, randomness and save/restore.

Value conventions (all values are Python ints, as in the Z-machine):

  * memory addresses        0x0000 - 0x4FFF
  * string references       0x5000 - 0x6FFF  (strings stored in tables)
  * routine references      0x7000 - 0x7FFF  (routines stored in tables)
  * objects                 1 - 255

String literals used directly in code stay ordinary Python strings.
"""

import os
import pickle
import random as _random
import shutil
import sys
import textwrap

# ---------------------------------------------------------------------------
# sentinels / exceptions

NOARG = object()          # "optional argument not supplied"


class Quit(Exception):
    pass


class Restart(Exception):
    pass


class _Byte:
    __slots__ = ("v",)

    def __init__(self, v):
        self.v = v


def BYTE(v):
    """Marks a table element that occupies a single byte (#BYTE in ZIL)."""
    return _Byte(v)


# ---------------------------------------------------------------------------
# state

MEM_SIZE = 0x5000
STRING_BASE = 0x5000
ROUTINE_BASE = 0x7000

mem = bytearray(MEM_SIZE)
_alloc = 64                     # first 64 bytes are the story-file header
G = None                        # the game module's globals()

parent = [0] * 256
sibling = [0] * 256
child = [0] * 256
attrs = [0] * 256
prop_table = [0] * 256          # address of each object's property table
prop_defaults = {}
_pending_objects = []

strings = []                    # id - STRING_BASE -> text
_string_ids = {}
routines = []                   # id - ROUTINE_BASE -> function
_routine_ids = {}
_routine_nargs = []

global_names = []               # global number - 16 -> name in G

dictionary = {}                 # encoded word bytes -> address
_initial_state = None


def _sign(v):
    return v - 0x10000 if v & 0x8000 else v


def _word(v):
    """Convert any table value to a 16-bit unsigned integer."""
    if isinstance(v, bool):
        return int(v)
    if isinstance(v, str):
        return intern(v)
    if callable(v):
        return rtn(v)
    return int(v) & 0xFFFF


def intern(s):
    i = _string_ids.get(s)
    if i is None:
        i = STRING_BASE + len(strings)
        if i >= ROUTINE_BASE:
            raise RuntimeError("too many strings")
        strings.append(s)
        _string_ids[s] = i
    return i


def rtn(fn):
    """Return the integer reference for a routine."""
    i = _routine_ids.get(fn)
    if i is None:
        i = ROUTINE_BASE + len(routines)
        routines.append(fn)
        code = fn.__code__
        _routine_nargs.append(code.co_argcount)
        _routine_ids[fn] = i
    return i


# ---------------------------------------------------------------------------
# memory

def alloc(n):
    global _alloc
    a = _alloc
    _alloc += n
    if _alloc > MEM_SIZE:
        raise RuntimeError("out of table memory")
    return a


def get(t, i):
    a = (t + 2 * i) & 0xFFFF
    return _sign((mem[a] << 8) | mem[a + 1])


def put(t, i, v):
    a = (t + 2 * i) & 0xFFFF
    v = _word(v)
    mem[a] = v >> 8
    mem[a + 1] = v & 0xFF
    return True


def getb(t, i):
    return mem[(t + i) & 0xFFFF]


def putb(t, i, v):
    mem[(t + i) & 0xFFFF] = _word(v) & 0xFF
    return True


def _put_word_at(a, v):
    v = _word(v)
    mem[a] = v >> 8
    mem[a + 1] = v & 0xFF


# ---------------------------------------------------------------------------
# arithmetic helpers (Z-machine semantics)

def div(a, b):
    q = abs(a) // abs(b)
    return q if (a < 0) == (b < 0) else -q


def mod(a, b):
    r = abs(a) % abs(b)
    return -r if a < 0 else r


def btst(a, b):
    return (a & b) == b


def bcom(a):
    return ~a


# ---------------------------------------------------------------------------
# text encoding (version 3 Z-characters, no abbreviations)

A0 = "abcdefghijklmnopqrstuvwxyz"
A1 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
A2 = " \n0123456789.,!?_#'\"/\\-:()"


def zencode(text, limit=None):
    zs = []
    for ch in text:
        if ch == " ":
            zs.append(0)
        elif ch in A0:
            zs.append(A0.index(ch) + 6)
        elif ch in A1:
            zs += [4, A1.index(ch) + 6]
        elif ch in A2 and ch != " ":
            zs += [5, A2.index(ch) + 6]
        else:
            o = ord(ch)
            zs += [5, 6, o >> 5, o & 31]
    if limit is not None:
        zs = (zs + [5] * limit)[:limit]
    else:
        while len(zs) % 3:
            zs.append(5)
        if not zs:
            zs = [5, 5, 5]
    out = bytearray()
    for i in range(0, len(zs), 3):
        w = (zs[i] << 10) | (zs[i + 1] << 5) | zs[i + 2]
        if i + 3 >= len(zs):
            w |= 0x8000
        out += bytes([w >> 8, w & 255])
    return bytes(out)


def zdecode(a):
    zchars = []
    while True:
        w = (mem[a] << 8) | mem[a + 1]
        a += 2
        zchars += [(w >> 10) & 31, (w >> 5) & 31, w & 31]
        if w & 0x8000:
            break
    out = []
    alpha = 0
    i = 0
    while i < len(zchars):
        c = zchars[i]
        if c == 0:
            out.append(" ")
        elif c == 4:
            alpha = 1
            i += 1
            continue
        elif c == 5:
            alpha = 2
            i += 1
            continue
        elif c >= 6:
            if alpha == 2 and c == 6:
                if i + 2 < len(zchars):
                    out.append(chr((zchars[i + 1] << 5) | zchars[i + 2]))
                i += 3
                alpha = 0
                continue
            out.append((A0, A1, A2)[alpha][c - 6])
        alpha = 0
        i += 1
    return "".join(out)


# ---------------------------------------------------------------------------
# building the memory image (called from game.py at import time)

def begin_build(game_globals):
    global G, _alloc
    G = game_globals
    # Tables start at 0x400.  The parser occasionally treats header word 0
    # (0x0300) as a vocabulary entry when given odd input (e.g. a lone
    # quoted string answering a question); in the original that address
    # holds no noun/adjective bits, so keep the area zero to match.
    _alloc = 0x400
    mem[:] = bytes(MEM_SIZE)
    mem[0] = 3                     # version
    put(0, 1, 119)                 # release number
    for i, ch in enumerate(b"880429"):  # serial number
        mem[0x12 + i] = ch


def vocabulary(entries):
    """entries: (text, ps_byte, value1, value2).  Returns text -> address."""
    rows = sorted(entries, key=lambda e: zencode(e[0], 6))
    base = alloc(7 * len(rows))
    result = {}
    for i, (text, ps, v1, v2) in enumerate(rows):
        a = base + 7 * i
        enc = zencode(text, 6)
        mem[a:a + 4] = enc
        mem[a + 4] = ps
        mem[a + 5] = v1 & 0xFF
        mem[a + 6] = v2 & 0xFF
        dictionary[enc] = a
        result[text] = a
    return result


def property_defaults(d):
    prop_defaults.update(d)


def words(*vals):
    """Property data made of 16-bit words."""
    out = bytearray()
    for v in vals:
        v = _word(v)
        out += bytes([v >> 8, v & 255])
    return bytes(out)


def bytes_(*vals):
    """Property data made of bytes."""
    return bytes(_word(v) & 0xFF for v in vals)


def uexit(room):
    return bytes_(room)


def nexit(msg):
    return words(msg)


def fexit(routine):
    return words(routine) + b"\0"


def cexit(room, flag_global, msg):
    return bytes_(room, global_number(flag_global)) + words(msg)


def dexit(room, door, msg):
    return bytes_(room, door) + words(msg) + b"\0"


def define_object(num, desc, parent=0, flags=(), props=()):
    _pending_objects.append((num, desc, parent, flags, props))


def link_objects():
    for num, desc, par, flags, props in _pending_objects:
        bits = 0
        for f in flags:
            bits |= 1 << f
        attrs[num] = bits
        name = zencode(desc) if desc else b""
        size = 1 + len(name) + sum(1 + len(d) for _, d in props) + 1
        a = alloc(size)
        prop_table[num] = a
        mem[a] = len(name) // 2
        p = a + 1
        mem[p:p + len(name)] = name
        p += len(name)
        for pnum, data in props:
            if not 1 <= len(data) <= 8:
                raise RuntimeError(f"property {pnum} of object {num} has size {len(data)}")
            mem[p] = ((len(data) - 1) << 5) | pnum
            mem[p + 1:p + 1 + len(data)] = data
            p += 1 + len(data)
        mem[p] = 0
    # each object becomes the first child of its parent, so children end
    # up in reverse definition order
    for num, desc, par, flags, props in _pending_objects:
        if par:
            move(num, par)
    _pending_objects.clear()


def declare_globals(names):
    global_names[:] = names


def global_number(name):
    return global_names.index(name) + 16


def value(n):
    return G[global_names[n - 16]]


def table(items, byte=False, length=False):
    data = bytearray()
    if length:
        n = len(items)
        data += bytes([n]) if byte else bytes([n >> 8, n & 255])
    for it in items:
        if isinstance(it, _Byte) or byte:
            v = it.v if isinstance(it, _Byte) else it
            data.append(_word(v) & 0xFF)
        else:
            v = _word(it)
            data += bytes([v >> 8, v & 255])
    a = alloc(len(data))
    mem[a:a + len(data)] = data
    return a


def itable(count, defaults, byte=False, length=False, lexv=False):
    """<ITABLE count (flags) defaults...>: `defaults` repeated `count` times."""
    items = list(defaults) * count
    if lexv:
        prefix = [BYTE(count), BYTE(0)]
    elif length:
        prefix = [BYTE(count)] if byte else [count]
    else:
        prefix = []
    return table(prefix + items, byte=byte)


def verbs_table(syntax):
    """syntax: ACT number -> list of 8-tuples.  Returns the VERBS table."""
    lowest = min(syntax)
    vt = table([0] * (256 - lowest))
    for act, entries in syntax.items():
        data = [BYTE(len(entries))]
        for e in entries:
            data += [BYTE(x) for x in e]
        put(vt, 255 - act, table(data))
    return vt


def action_table(d, size):
    """A word table indexed by action number."""
    return table([d.get(i, 0) for i in range(size)])


def prepositions_table(pairs):
    items = [len(pairs)]
    for w, n in pairs:
        items += [w, n]
    return table(items)


def end_build():
    global _initial_state
    # give every routine a fixed reference number, so saved games stay valid
    for v in list(G.values()):
        if callable(v) and getattr(v, "__module__", None) == G["__name__"]:
            rtn(v)
    _initial_state = _snapshot()


# ---------------------------------------------------------------------------
# objects

def loc(o):
    return parent[o] if o else 0


def first_p(o):
    return child[o] if o else 0


def next_p(o):
    return sibling[o] if o else 0


def in_p(o, p):
    return bool(o) and parent[o] == p


def _unlink(o):
    p = parent[o]
    if not p:
        return
    if child[p] == o:
        child[p] = sibling[o]
    else:
        c = child[p]
        while c:
            if sibling[c] == o:
                sibling[c] = sibling[o]
                break
            c = sibling[c]
    parent[o] = 0
    sibling[o] = 0


def move(o, p):
    _unlink(o)
    sibling[o] = child[p]
    parent[o] = p
    child[p] = o
    return True


def remove(o):
    _unlink(o)
    return True


def fset(o, f):
    attrs[o] |= 1 << f
    return True


def fclear(o, f):
    attrs[o] &= ~(1 << f)
    return True


def fset_p(o, f):
    return bool(o) and bool(attrs[o] & (1 << f))


def _first_prop(o):
    a = prop_table[o]
    return a + 1 + mem[a] * 2


def getpt(o, p):
    if not o:
        return 0
    a = _first_prop(o)
    while mem[a]:
        b = mem[a]
        num, size = b & 31, (b >> 5) + 1
        if num == p:
            return a + 1
        if num < p:
            return 0
        a += 1 + size
    return 0


def ptsize(a):
    if not a:
        return 0
    return (mem[a - 1] >> 5) + 1


def getp(o, p):
    a = getpt(o, p)
    if not a:
        return prop_defaults.get(p, 0)
    if ptsize(a) == 1:
        return mem[a]
    return _sign((mem[a] << 8) | mem[a + 1])


def putp(o, p, v):
    a = getpt(o, p)
    if not a:
        raise RuntimeError(f"PUTP: object {o} has no property {p}")
    if ptsize(a) == 1:
        mem[a] = _word(v) & 0xFF
    else:
        _put_word_at(a, v)
    return True


def nextp(o, p):
    if p == 0:
        a = _first_prop(o)
    else:
        a = getpt(o, p)
        if not a:
            raise RuntimeError(f"NEXTP: object {o} has no property {p}")
        a += ptsize(a)
    return mem[a] & 31


def object_name(o):
    if not o:
        return ""
    a = prop_table[o]
    if mem[a] == 0:
        return ""
    return zdecode(a + 1)


# ---------------------------------------------------------------------------
# routines

def apply(f, *args):
    if not f:
        return False
    if not isinstance(f, int):
        f = rtn(f)
    i = f - ROUTINE_BASE
    fn = routines[i]
    n = _routine_nargs[i]
    r = fn(*args[:n])
    return False if r is None else r


# ---------------------------------------------------------------------------
# output

class Screen:
    """Collects output and word-wraps it to the terminal width."""

    def __init__(self, stream=None, width=None, wrap=True):
        self.stream = stream or sys.stdout
        self.width = width
        self.wrap = wrap
        self.line = ""
        self.transcript = None

    def get_width(self):
        if self.width:
            return self.width
        return max(20, min(shutil.get_terminal_size((80, 24)).columns, 100) - 1)

    def write(self, s):
        if self.transcript:
            self.transcript.write(s)
        if not self.wrap:
            self.stream.write(s)
            return
        parts = s.split("\n")
        for i, part in enumerate(parts):
            self.line += part
            if i < len(parts) - 1:
                self._emit_line(self.line)
                self.stream.write("\n")
                self.line = ""
        w = self.get_width()
        while len(self.line) > w:
            cut = self.line.rfind(" ", 0, w + 1)
            if cut <= 0:
                cut = w
            self.stream.write(self.line[:cut] + "\n")
            self.line = self.line[cut:].lstrip(" ")

    def _emit_line(self, line):
        w = self.get_width()
        if len(line) <= w:
            self.stream.write(line)
            return
        wrapped = textwrap.wrap(line, w, drop_whitespace=True, break_long_words=True,
                                replace_whitespace=False)
        self.stream.write("\n".join(wrapped))

    def flush(self):
        # print the partial line (a prompt) without ending it
        self.stream.write(self.line)
        self.line = ""
        self.stream.flush()


screen = Screen()
input_fn = None          # callable returning a line, or None at end of input


def _default_input():
    try:
        return input()
    except EOFError:
        return None


def output(s):
    screen.write(s)


def S(x):
    """The text of a string value (Python str or a string reference)."""
    if isinstance(x, str):
        return x
    if not x:
        return ""
    i = x - STRING_BASE
    if 0 <= i < len(strings):
        return strings[i]
    raise RuntimeError(f"not a string reference: {x}")


def D(o):
    return object_name(o)


def A(o):
    name = object_name(o)
    return ("an " if name[:1].lower() in "aeiou" else "a ") + name


def N(n):
    return str(int(n))


def C(c):
    return chr(c)


def tell(*parts):
    output("".join(parts))
    return True


def print_(x):
    output(S(x))
    return True


def printd(o):
    output(object_name(o))
    return True


def printn(n):
    output(str(int(n)))
    return True


def printc(c):
    output(chr(c))
    return True


def printb(w):
    if w:
        output(zdecode(w))
    return True


def crlf():
    output("\n")
    return True


def usl():
    return True


# ---------------------------------------------------------------------------
# input

SEPARATORS = ".,\""


def read(inbuf, lexv):
    screen.flush()
    line = (input_fn or _default_input)()
    if line is None:
        raise Quit()
    if screen.transcript:
        screen.transcript.write(line + "\n")
    maxlen = mem[inbuf]
    line = line.lower()[:maxlen - 1]
    for i, ch in enumerate(line):
        mem[inbuf + 1 + i] = ord(ch) & 0xFF
    mem[inbuf + 1 + len(line)] = 0
    tokenize(line, lexv)
    return True


def tokenize(line, lexv):
    toks = []
    i = 0
    while i < len(line):
        ch = line[i]
        if ch == " ":
            i += 1
            continue
        if ch in SEPARATORS:
            toks.append((ch, i))
            i += 1
            continue
        j = i
        while j < len(line) and line[j] != " " and line[j] not in SEPARATORS:
            j += 1
        toks.append((line[i:j], i))
        i = j
    toks = toks[:mem[lexv]]
    mem[lexv + 1] = len(toks)
    for k, (wd, pos) in enumerate(toks):
        a = lexv + 2 + 4 * k
        _put_word_at(a, dictionary.get(zencode(wd, 6), 0))
        mem[a + 2] = len(wd)
        mem[a + 3] = pos + 1


# ---------------------------------------------------------------------------
# randomness

_rng = _random.Random()


def _default_random(n):
    return _rng.randint(1, n)


random_fn = _default_random


def random(n):
    if n > 0:
        return random_fn(n)
    if n < 0:
        _rng.seed(-n)
    else:
        _rng.seed()
    return 0


def seed(s):
    _rng.seed(s)


# ---------------------------------------------------------------------------
# save / restore / restart

def _snapshot():
    return {
        "mem": bytes(mem),
        "parent": list(parent), "sibling": list(sibling), "child": list(child),
        "attrs": list(attrs),
        "globals": {n: G[n] for n in global_names},
        "strings": list(strings),
        "routines": [fn.__name__ for fn in routines],
    }


def _load(state):
    mem[:] = state["mem"]
    parent[:] = state["parent"]
    sibling[:] = state["sibling"]
    child[:] = state["child"]
    attrs[:] = state["attrs"]
    for n, v in state["globals"].items():
        G[n] = v
    strings[:] = state["strings"]
    _string_ids.clear()
    for i, s in enumerate(strings):
        _string_ids.setdefault(s, STRING_BASE + i)
    names = state["routines"]
    fns = [G[n] for n in names]
    routines[:] = fns
    _routine_nargs[:] = [fn.__code__.co_argcount for fn in fns]
    _routine_ids.clear()
    for i, fn in enumerate(fns):
        _routine_ids[fn] = ROUTINE_BASE + i


def _ask_filename(default):
    output(f"Enter a file name (default is \"{default}\"): ")
    screen.flush()
    line = (input_fn or _default_input)()
    if line is None:
        return None
    line = line.strip()
    return line or default


SAVE_DEFAULT = "zork1.sav"


def save():
    name = _ask_filename(SAVE_DEFAULT)
    if not name:
        return False
    try:
        with open(name, "wb") as f:
            pickle.dump({"format": "zork1-py-1", "state": _snapshot()}, f)
        return True
    except OSError:
        return False


def restore():
    name = _ask_filename(SAVE_DEFAULT)
    if not name or not os.path.exists(name):
        return False
    try:
        with open(name, "rb") as f:
            data = pickle.load(f)
        if data.get("format") != "zork1-py-1":
            return False
        _load(data["state"])
        return True
    except (OSError, pickle.UnpicklingError, KeyError, EOFError):
        return False


def restart():
    raise Restart()


def quit():
    raise Quit()


def verify():
    return True


def dirout(n, *args):
    # output streams: 2 = transcript, others are not needed here
    return True


def dirin(n):
    return True


# ---------------------------------------------------------------------------
# entry point

def run(go, inp=None):
    """Run the game: `go` is the translated GO routine."""
    global input_fn
    if inp is not None:
        input_fn = inp
    while True:
        try:
            go()
            return
        except Restart:
            screen.write("")
            _load(_initial_state)
            continue
        except Quit:
            screen.flush()
            return
