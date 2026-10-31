#!/usr/bin/env python3
"""zil2py: translate the Zork I ZIL source into a Python module.

    python3 python/tools/zil2py.py  [--src DIR] [--out FILE]

The ZIL program is translated routine-by-routine into Python functions.
Game data (objects, vocabulary, syntax tables, TABLEs) is emitted as
declarative calls into zork1.runtime, which lays it out in an emulated
Z-machine memory image.  That keeps the original parser - which does
pointer arithmetic over its lexical buffers, vocabulary entries and
syntax tables - running unmodified.
"""

import argparse
import keyword
import textwrap
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from zilreader import (Atom, Char, Eval, Form, GVal, Hash, List, LVal, Quote,  # noqa: E402
                       Vector, read_file)


class CompileError(Exception):
    pass


def A(name):
    return Atom(name)


T = A("T")
ELSE = A("ELSE")


def is_atom(x, name=None):
    return isinstance(x, Atom) and (name is None or x.name == name)


def head(x):
    if isinstance(x, Form) and x and isinstance(x[0], Atom):
        return x[0].name
    return None


# ---------------------------------------------------------------------------
# name mangling

PY_RESERVED = set(keyword.kwlist) | {
    "z", "int", "str", "len", "print", "range", "list", "dict", "set", "min",
    "max", "abs", "type", "id", "object", "input", "open", "next", "iter",
    "sum", "all", "any", "bool", "map", "filter", "format", "hash", "vars",
    "locals", "globals", "exec", "eval", "compile", "chr", "ord", "repr",
    "round", "sorted", "super", "tuple", "zip", "bytes", "file",
}


def mangle(name):
    out = []
    for ch in name:
        if ch.isalnum() or ch == "_":
            out.append(ch)
        elif ch == "-":
            out.append("_")
        elif ch == "?":
            out.append("_P")
        elif ch == "$":
            out.append("S_")
        elif ch == "#":
            out.append("H_")
        else:
            out.append("_")
    s = "".join(out)
    while "__" in s:
        s = s.replace("__", "_")
    if s and s[0].isdigit():
        s = "N" + s
    return s


PREFIXES = ("V?", "ACT?", "PR?", "P?", "PS?", "P1?", "W?", "A?")


def upper_name(name):
    for p in PREFIXES:
        if name.startswith(p):
            return p[:-1] + "_" + mangle(name[len(p):]).strip("_")
    return mangle(name).upper()


def lower_name(name):
    s = mangle(name).lower()
    if s in PY_RESERVED:
        s += "_"
    return s


# ---------------------------------------------------------------------------
# compile-time (MDL) evaluation, for %<COND ...> and top-level COND

class CTEnv:
    def __init__(self):
        self.gvals = {"ZORK-NUMBER": 1}

    def eval(self, x):
        if isinstance(x, (int, str)):
            return x
        if isinstance(x, Quote):
            return x.obj
        if isinstance(x, GVal):
            n = x.atom.name
            if n not in self.gvals:
                raise CompileError(f"compile-time GVAL of unknown {n}")
            return self.gvals[n]
        if isinstance(x, Atom):
            return x
        if isinstance(x, Form):
            h = head(x)
            if not x:
                return False
            if h == "COND":
                for clause in x[1:]:
                    v = self.eval(clause[0])
                    if self.truthy(v):
                        for e in clause[1:]:
                            v = self.eval(e)
                        return v
                return False
            if h in ("==?", "=?"):
                return self.eval(x[1]) == self.eval(x[2])
            if h == "N==?":
                return self.eval(x[1]) != self.eval(x[2])
            if h == "GASSIGNED?":
                return x[1].name in self.gvals
            if h == "NOT":
                return not self.truthy(self.eval(x[1]))
            if h == "OR":
                for e in x[1:]:
                    v = self.eval(e)
                    if self.truthy(v):
                        return v
                return False
            if h == "AND":
                v = True
                for e in x[1:]:
                    v = self.eval(e)
                    if not self.truthy(v):
                        return False
                return v
        raise CompileError(f"can't evaluate at compile time: {x!r}")

    @staticmethod
    def truthy(v):
        return not (v is False or v == Form())


def expand_evals(x, env):
    """Replace every %<...> with its compile-time value (recursively)."""
    if isinstance(x, Eval):
        v = env.eval(x.obj)
        if v is True:
            v = T
        elif v is False:
            v = Form()
        return expand_evals(v, env)
    if isinstance(x, (Form, List, Vector)):
        return type(x)(expand_evals(e, env) for e in x)
    if isinstance(x, GVal):
        return GVal(expand_evals(x.atom, env))
    if isinstance(x, LVal):
        return LVal(expand_evals(x.atom, env))
    if isinstance(x, Quote):
        return Quote(expand_evals(x.obj, env))
    if isinstance(x, Hash):
        return Hash(x.type, expand_evals(x.obj, env))
    return x


# ---------------------------------------------------------------------------
# Strings: ZIL line breaks become spaces, '|' is a newline.

def zstr(s):
    s = s.replace("\r", "")
    s = s.replace("|\n", "|")
    s = s.replace("\n", " ")
    # ZILCH folded the two spaces after a full stop into one
    while ".  " in s:
        s = s.replace(".  ", ". ")
    return s.replace("|", "\n")


# ---------------------------------------------------------------------------
# Vocabulary

PS_BITS = {"OBJECT": 128, "VERB": 64, "ADJECTIVE": 32, "DIRECTION": 16,
           "PREPOSITION": 8, "BUZZ-WORD": 4}
P1_CODES = {"OBJECT": 0, "VERB": 1, "ADJECTIVE": 2, "DIRECTION": 3, "PREPOSITION": 0}
SPECIAL_WORDS = {"PERIOD": ".", "COMMA": ",", "QUOTE": '"'}


class Word:
    def __init__(self, text):
        self.text = text
        self.pos = []      # ordered list of parts of speech (first defined first)
        self.values = {}   # part of speech -> value

    def add(self, pos, value=None):
        if pos not in self.values:
            self.pos.append(pos)
            self.values[pos] = value


# ---------------------------------------------------------------------------

LOC_BITS = {"HELD": 128, "CARRIED": 64, "IN-ROOM": 32, "ON-GROUND": 16,
            "TAKE": 8, "MANY": 4, "HAVE": 2}

SYNTAX_GLOBALS = {"VERBS", "ACTIONS", "PREACTIONS", "PREPOSITIONS"}
BUILTIN_PROPS = {"SYNONYM", "ADJECTIVE", "GLOBAL", "PSEUDO"}


class Program:
    def __init__(self):
        self.env = CTEnv()
        self.constants = {}        # name -> value node  (source order)
        self.ct_constants = {}     # compile-time SETGs used as constants
        self.globals = {}          # name -> init node (source order)
        self.objects = []          # (name, kind, props list)
        self.object_index = {}
        self.routines = {}         # name -> Form
        self.routine_order = []
        self.flags = []
        self.props = []            # non-direction props, in first-use order
        self.directions = []
        self.propdefs = {}
        self.words = {}            # text -> Word
        self.word_order = []
        self.synonyms = []         # (head, [syns])
        self.buzz_counter = 255
        self.prep_counter = 255
        self.adj_counter = 255
        self.preps = {}            # canonical prep atom name -> number
        self.prep_canon = {}       # any prep word -> canonical word
        self.syntaxes = []         # dicts
        self.actions = {}          # action name -> (number, routine, preaction)
        self.action_order = []
        self.source_files = []

    # ---------------- reading
    def load(self, srcdir, main="zork1.zil"):
        items = read_file(os.path.join(srcdir, main))
        self.process_toplevel(items, srcdir)
        # constant the ZIL compiler defines itself
        self.constants["LOW-DIRECTION"] = 32 - len(self.directions)

    def process_toplevel(self, items, srcdir):
        for x in items:
            x = expand_evals(x, self.env)
            self.toplevel(x, srcdir)

    def toplevel(self, x, srcdir):
        if not isinstance(x, Form) or not x:
            return
        h = head(x)
        if h == "INSERT-FILE":
            fname = x[1].lower() + ".zil"
            self.source_files.append(fname)
            items = read_file(os.path.join(srcdir, fname))
            self.process_toplevel(items, srcdir)
        elif h in ("VERSION", "SET", "OR", "PRINC", "FREQUENT-WORDS?", "GDECL", "DEFMAC"):
            pass  # compile-time directives with no run-time effect
        elif h == "SETG":
            name = x[1].name
            val = self.env.eval(x[2]) if not isinstance(x[2], str) else x[2]
            self.env.gvals[name] = val
            self.ct_constants[name] = x[2]
        elif h == "DEFINE":
            name = x[1].name
            if name in ("MULTIFROB", "MULTIBITS"):
                return
            # a DEFINE in ZIL code position is treated as a routine
            self.add_routine(Form([A("ROUTINE")] + x[1:]))
        elif h == "ROUTINE":
            self.add_routine(x)
        elif h == "CONSTANT":
            self.constants[x[1].name] = x[2]
            self.env.gvals[x[1].name] = x[2] if isinstance(x[2], (int, str)) else x[2]
        elif h == "GLOBAL":
            self.globals[x[1].name] = x[2] if len(x) > 2 else Form()
        elif h in ("OBJECT", "ROOM"):
            self.add_object(x)
        elif h == "PROPDEF":
            self.propdefs[x[1].name] = x[2]
            self.prop(x[1].name)
        elif h == "DIRECTIONS":
            for d in x[1:]:
                self.directions.append(d.name)
                self.word(d.name).add("DIRECTION", d.name)
        elif h == "BUZZ":
            for w in x[1:]:
                wd = self.word(self.word_text(w))
                if "BUZZ-WORD" not in wd.values:
                    wd.add("BUZZ-WORD", self.buzz_counter)
                    self.buzz_counter -= 1
        elif h == "SYNONYM":
            self.synonyms.append((self.word_text(x[1]), [self.word_text(w) for w in x[2:]]))
            for w in x[1:]:
                self.word(self.word_text(w))
        elif h == "SYNTAX":
            self.add_syntax(x)
        elif h == "COND":
            for clause in x[1:]:
                if CTEnv.truthy(self.env.eval(clause[0])):
                    for e in clause[1:]:
                        self.toplevel(e, srcdir)
                    break
        elif h == "PROG":
            for e in x[2:]:
                self.toplevel(e, srcdir)
        else:
            raise CompileError(f"unknown top-level form {h}")

    @staticmethod
    def word_text(w):
        if isinstance(w, Atom):
            return w.name.lower()
        if isinstance(w, str):
            return w.lower()
        if isinstance(w, Char):
            return w.ch
        raise CompileError(f"bad word {w!r}")

    def word(self, text):
        text = text.lower()
        if text not in self.words:
            self.words[text] = Word(text)
            self.word_order.append(text)
        return self.words[text]

    def flag(self, name):
        if name not in self.flags:
            self.flags.append(name)
        return name

    def prop(self, name):
        if name not in self.props and name not in self.directions:
            self.props.append(name)
        return name

    def add_routine(self, x):
        name = x[1].name
        if name in self.routines:
            self.routine_order.remove(name)
        self.routines[name] = x
        self.routine_order.append(name)

    def add_object(self, x):
        name = x[1].name
        if name in self.object_index:
            raise CompileError(f"duplicate object {name}")
        self.object_index[name] = len(self.objects)
        self.objects.append((name, head(x), list(x[2:])))
        for p in x[2:]:
            pname = p[0].name
            if pname == "FLAGS":
                for f in p[1:]:
                    self.flag(f.name)
            elif pname == "SYNONYM":
                self.prop(pname)
                for w in p[1:]:
                    self.word(self.word_text(w)).add("OBJECT", 1)
            elif pname == "ADJECTIVE":
                self.prop(pname)
                for w in p[1:]:
                    wd = self.word(self.word_text(w))
                    if "ADJECTIVE" not in wd.values:
                        wd.add("ADJECTIVE", self.adj_counter)
                        self.adj_counter -= 1
            elif pname == "PSEUDO":
                self.prop(pname)
                for w in p[1::2]:
                    self.word(self.word_text(w)).add("OBJECT", 1)
            elif pname in ("IN", "LOC", "DESC", "FLAGS"):
                pass
            elif pname in self.directions:
                pass
            else:
                self.prop(pname)

    def add_syntax(self, x):
        parts = x[1:]
        eq = parts.index(A("="))
        pattern, rhs = parts[:eq], parts[eq + 1:]
        verb = self.word_text(pattern[0])
        syn = {"verb": verb, "nobj": 0, "prep1": 0, "prep2": 0, "find1": None,
               "find2": None, "loc1": 0, "loc2": 0}
        i = 1
        pending_prep = None
        while i < len(pattern):
            p = pattern[i]
            if is_atom(p, "OBJECT"):
                syn["nobj"] += 1
                n = syn["nobj"]
                if pending_prep:
                    syn[f"prep{n}"] = pending_prep
                    pending_prep = None
                i += 1
                while i < len(pattern) and isinstance(pattern[i], List):
                    lst = pattern[i]
                    if is_atom(lst[0], "FIND"):
                        syn[f"find{n}"] = self.flag(lst[1].name)
                    else:
                        bits = 0
                        for b in lst:
                            bits |= LOC_BITS[b.name]
                        syn[f"loc{n}"] = bits
                    i += 1
            else:
                pending_prep = self.prep_word(self.word_text(p))
                i += 1
        if pending_prep:
            # trailing preposition with no object, e.g. <SYNTAX GET UP = ...>
            syn[f"prep{syn['nobj'] + 1}"] = pending_prep
        action_rtn = rhs[0].name
        pre = rhs[1].name if len(rhs) > 1 else None
        act_name = action_rtn[2:] if action_rtn.startswith("V-") else action_rtn
        if len(rhs) > 2:
            act_name = rhs[2].name
        if act_name not in self.actions:
            self.actions[act_name] = [len(self.action_order) + 1, action_rtn, pre]
            self.action_order.append(act_name)
        else:
            a = self.actions[act_name]
            if pre and not a[2]:
                a[2] = pre
        syn["action"] = act_name
        self.syntaxes.append(syn)
        self.word(verb)

    def prep_word(self, text):
        canon = text
        for hd, syns in self.synonyms:
            if text in syns:
                canon = hd
        if canon not in self.preps:
            self.preps[canon] = self.prep_counter
            self.prep_counter -= 1
        self.word(canon).add("PREPOSITION", self.preps[canon])
        return canon

    # ---------------- vocabulary finalisation
    def finish_vocab(self):
        # verbs get their part of speech last (as ZILCH did)
        verbs = []
        for s in self.syntaxes:
            if s["verb"] not in verbs:
                verbs.append(s["verb"])
        canon_verbs = []
        for v in verbs:
            c = v
            for hd, syns in self.synonyms:
                if v in syns:
                    c = hd
            if c not in canon_verbs:
                canon_verbs.append(c)
        self.verb_numbers = {}
        n = 255
        for v in canon_verbs:
            self.verb_numbers[v] = n
            self.word(v).add("VERB", n)
            n -= 1
        # synonyms copy the parts of speech of their head word
        for hd, syns in self.synonyms:
            h = self.word(hd)
            for s in syns:
                w = self.word(s)
                for pos in h.pos:
                    w.add(pos, h.values[pos])
        for w in self.words.values():
            if "DIRECTION" in w.values and isinstance(w.values["DIRECTION"], str):
                w.values["DIRECTION"] = self.prop_number(w.values["DIRECTION"])

    def word_record(self, w):
        ps = 0
        for pos in w.pos:
            ps |= PS_BITS[pos]
        valued = [p for p in w.pos if p in P1_CODES]
        v1 = v2 = 0
        if valued:
            ps |= P1_CODES[valued[0]]
            v1 = w.values[valued[0]]
            if len(valued) > 1:
                v2 = w.values[valued[1]]
            if len(valued) > 2:
                print(f"warning: word {w.text!r} has >2 valued parts of speech",
                      file=sys.stderr)
        elif "BUZZ-WORD" in w.values:
            v1 = w.values["BUZZ-WORD"]
        return ps, v1, v2

    def prop_number(self, name):
        if name in self.directions:
            return 31 - self.directions.index(name)
        return 31 - len(self.directions) - self.props.index(name)

    def flag_number(self, name):
        return self.flags.index(name) + 1


# ---------------------------------------------------------------------------
# Code generation helpers

class Ctx:
    DISCARD = "discard"
    RETURN = "return"


class Assign:
    def __init__(self, var):
        self.var = var


def strip_parens(e):
    """Remove one pair of redundant outer parentheses from an expression."""
    if not (e.startswith("(") and e.endswith(")")):
        return e
    depth = 0
    for i, ch in enumerate(e):
        if ch == "(":
            depth += 1
        elif ch == ")":
            depth -= 1
            if depth == 0 and i != len(e) - 1:
                return e
    inner = e[1:-1]
    if ":=" in inner and inner.count("(") == e.count("(") - 1:
        # keep parentheses around a top-level walrus
        top = 0
        for i, ch in enumerate(inner):
            if ch == "(":
                top += 1
            elif ch == ")":
                top -= 1
            elif ch == ":" and top == 0 and inner[i:i + 2] == ":=":
                return e
    return inner


class Emitter:
    def __init__(self):
        self.lines = []
        self.depth = 0

    def emit(self, text):
        for kw in ("if ", "elif ", "while "):
            if text.startswith(kw) and text.endswith(":"):
                text = kw + strip_parens(text[len(kw):-1]) + ":"
        if text.startswith("return "):
            text = "return " + strip_parens(text[7:])
        self.lines.append((self.depth, text))


class FnCompiler:
    def __init__(self, gen, name, form):
        self.gen = gen
        self.prog = gen.prog
        self.zname = name
        self.form = form
        self.out = Emitter()
        self.locals = {}       # ZIL local name -> python name
        self.global_writes = set()
        self.temp_n = 0
        self.loops = []        # stack of dicts {kind, ctx}
        self.noarg_params = set()

    # ---------- utilities
    def emit(self, s):
        self.out.emit(s)

    def indent(self):
        self.out.depth += 1

    def dedent(self):
        self.out.depth -= 1

    def temp(self):
        self.temp_n += 1
        return f"_t{self.temp_n}"

    def capture(self):
        return _Capture(self)

    def error(self, msg):
        raise CompileError(f"in routine {self.zname}: {msg}")

    def local(self, atom):
        n = atom.name
        if n not in self.locals:
            self.error(f"unknown local {n}")
        return self.locals[n]

    def new_local(self, name):
        py = lower_name(name)
        taken = set(self.locals.values())
        while py in taken or py in self.gen.routine_py_names or py in PY_RESERVED:
            py += "_"
        self.locals[name] = py
        return py

    # ---------- routine
    def compile(self):
        f = self.form
        args = f[2]
        body = f[3:]
        if isinstance(args, Atom):  # activation name - unsupported
            self.error("activations not supported")
        params = []
        aux = []
        mode = "REQ"
        for a in args:
            if isinstance(a, str):
                mode = a
                continue
            if isinstance(a, List):
                var, init = a[0].name, a[1]
            else:
                var, init = a.name, None
            if mode in ("REQ", "OPTIONAL", "OPT"):
                params.append((var, init, mode))
            elif mode == "AUX" or mode == "EXTRA":
                aux.append((var, init))
            else:
                self.error(f"unknown arg mode {mode}")
        uses_assigned = self.find_assigned(body)
        sig = []
        pre = []
        for var, init, mode in params:
            py = self.new_local(var)
            if var in uses_assigned:
                sig.append(f"{py}=z.NOARG")
                self.noarg_params.add(var)
                if init is not None:
                    self.error("ASSIGNED? with default")
            elif init is None or isinstance(init, int) or init == Form() or init == T:
                sig.append(f"{py}={self.const_expr(init)}")
            else:
                sig.append(f"{py}=z.NOARG")
                pre.append((py, init))
        for var, init in aux:
            self.new_local(var)
        self.sig = sig
        # body
        for py, init in pre:
            self.emit(f"if {py} is z.NOARG:")
            self.indent()
            self.compile_stmt(init, Assign(py))
            self.dedent()
        for var, init in aux:
            py = self.locals[var]
            if init is None:
                self.emit(f"{py} = 0")
            else:
                self.compile_stmt(init, Assign(py))
        body = [b for b in body if not (isinstance(b, Hash) and b.type == "DECL")]
        body = [b for b in body if not isinstance(b, str)]
        if self.contains_again(body):
            # <AGAIN> at routine level restarts the routine body
            self.stmt_prog(Form([A("PROG"), List()] + body), Ctx.RETURN)
        else:
            self.compile_body(body, Ctx.RETURN)
        if not self.out.lines or not self.out.lines[-1][1].startswith("return") \
                or self.out.lines[-1][0] != 0:
            self.emit("return False")
        return self.render()

    def find_assigned(self, body):
        found = set()

        def walk(x):
            if isinstance(x, Form):
                if head(x) == "ASSIGNED?":
                    found.add(x[1].name)
                for e in x:
                    walk(e)
            elif isinstance(x, (List, Vector)):
                for e in x:
                    walk(e)
        for b in body:
            walk(b)
        return found

    def render(self):
        pyname = self.gen.routine_py[self.zname]
        lines = [f"def {pyname}({', '.join(self.sig)}):"]
        if self.global_writes:
            gl = sorted(self.global_writes)
            chunk = []
            for g in gl:
                chunk.append(g)
                if len(", ".join(chunk)) > 60:
                    lines.append("    global " + ", ".join(chunk))
                    chunk = []
            if chunk:
                lines.append("    global " + ", ".join(chunk))
        for depth, text in self.out.lines:
            lines.append("    " * (depth + 1) + text)
        return "\n".join(lines)

    def const_expr(self, x):
        if x is None or x == Form():
            return "False" if x is not None else "0"
        if x == T:
            return "True"
        if isinstance(x, int):
            return str(x)
        self.error(f"bad default {x!r}")

    # ---------- statements
    def compile_body(self, body, ctx):
        if not body:
            self.finish(ctx, "False")
            return
        for i, stmt in enumerate(body):
            last = i == len(body) - 1
            self.compile_stmt(stmt, ctx if last else Ctx.DISCARD)

    def finish(self, ctx, expr, pure=None):
        if ctx == Ctx.DISCARD:
            if pure is None:
                pure = self.is_pure(expr)
            if not pure:
                self.emit(expr)
        elif ctx == Ctx.RETURN:
            self.emit(f"return {expr}")
        else:
            if expr != ctx.var:
                self.emit(f"{ctx.var} = {strip_parens(expr)}")

    @staticmethod
    def is_pure(expr):
        if "(" not in expr:
            return True
        return False

    def compile_stmt(self, x, ctx):
        h = head(x)
        if h == "COND":
            return self.stmt_cond(x, ctx)
        if h == "REPEAT":
            return self.stmt_repeat(x, ctx)
        if h == "PROG":
            return self.stmt_prog(x, ctx)
        if h == "RETURN":
            return self.stmt_return(x)
        if h == "RTRUE":
            self.emit("return True")
            return
        if h == "RFALSE":
            self.emit("return False")
            return
        if h == "RFATAL":
            self.emit("return 2")
            return
        if h == "AGAIN":
            if not self.loops:
                self.error("AGAIN outside a loop")
            self.emit("continue")
            return
        if h in ("SET", "SETG") and ctx == Ctx.DISCARD:
            var = self.var_target(x[1], h)
            self.compile_stmt(x[2], Assign(var))
            return
        if h == "TELL" and ctx == Ctx.DISCARD:
            return self.stmt_tell(x[1:])
        if h in ("AND", "OR") and ctx == Ctx.DISCARD:
            return self.stmt_andor_discard(x)
        if h in ("SET", "SETG") and ctx == Ctx.RETURN:
            var = self.var_target(x[1], h)
            self.compile_stmt(x[2], Assign(var))
            self.emit(f"return {var}")
            return
        if h in ("SET", "SETG") and isinstance(ctx, Assign):
            var = self.var_target(x[1], h)
            self.compile_stmt(x[2], Assign(var))
            self.finish(ctx, var)
            return
        e = self.compile_expr(x)
        self.finish(ctx, e)

    def var_target(self, atom, h):
        if isinstance(atom, LVal):
            atom = atom.atom
        n = atom.name
        if h == "SET" and n in self.locals:
            return self.locals[n]
        if h == "SET":
            self.error(f"SET of non-local {n}")
        py = self.gen.gname(n)
        if n not in self.prog.globals:
            self.error(f"SETG of non-global {n}")
        self.global_writes.add(py)
        return py

    def stmt_andor_discard(self, x):
        # <AND a b c> as a statement == if a: if b: c
        h = head(x)
        args = x[1:]
        if not args:
            return
        depth0 = self.out.depth
        for i, a in enumerate(args):
            if i == len(args) - 1:
                self.compile_stmt(a, Ctx.DISCARD)
                break
            c = self.compile_expr(a)
            self.emit(f"if {c}:" if h == "AND" else f"if not ({c}):")
            self.indent()
        self.out.depth = depth0

    def stmt_cond(self, x, ctx):
        clauses = x[1:]
        # drop clauses whose test is a known-false compile-time constant
        live = []
        for c in clauses:
            if not isinstance(c, List):
                self.error(f"bad COND clause {c!r}")
            t = c[0]
            if isinstance(t, GVal) and t.atom.name in self.prog.ct_constants \
                    and t.atom.name not in self.prog.globals:
                v = self.prog.env.gvals[t.atom.name]
                if not CTEnv.truthy(v):
                    continue
                c = List([T] + c[1:])
            live.append(c)
        depth0 = self.out.depth
        first = True
        has_else = False
        for c in live:
            test, body = c[0], list(c[1:])
            if test == T or test == ELSE:
                if not body:
                    body = [T]   # (T) alone has the value T
                if first:
                    self.compile_body(body, ctx)
                else:
                    self.emit("else:")
                    self.indent()
                    mark = len(self.out.lines)
                    self.compile_body(body, ctx)
                    if len(self.out.lines) == mark:
                        self.emit("pass")
                    self.dedent()
                has_else = True
                break
            if not body and ctx != Ctx.DISCARD:
                # value of the clause is the value of the test
                with self.capture() as cap:
                    tv = self.compile_expr(test)
                t = self.temp() if not isinstance(ctx, Assign) else ctx.var
                if first:
                    cap.flush()
                    self.emit(f"{t} = {tv}" if t != tv else "pass")
                    self.emit(f"if {t}:")
                else:
                    self.emit("else:")
                    self.indent()
                    cap.flush()
                    self.emit(f"{t} = {tv}")
                    self.emit(f"if {t}:")
                self.indent()
                self.finish(ctx, t)
                self.dedent()
                first = False
                continue
            with self.capture() as cap:
                tv = self.compile_expr(test)
            if first:
                cap.flush()
                self.emit(f"if {tv}:")
            elif cap.empty():
                self.emit(f"elif {tv}:")
            else:
                self.emit("else:")
                self.indent()
                cap.flush()
                self.emit(f"if {tv}:")
            self.indent()
            mark = len(self.out.lines)
            if body:
                self.compile_body(body, ctx)
            if len(self.out.lines) == mark:
                self.emit("pass")
            self.dedent()
            first = False
        if not has_else and isinstance(ctx, Assign) and not first:
            self.emit("else:")
            self.indent()
            self.emit(f"{ctx.var} = False")
            self.dedent()
        elif first and not has_else:
            self.finish(ctx, "False")
        self.out.depth = depth0

    def stmt_repeat(self, x, ctx):
        bindings = x[1]
        if not isinstance(bindings, List):
            self.error("REPEAT without binding list")
        for b in bindings:
            if isinstance(b, List):
                py = self.new_local(b[0].name) if b[0].name not in self.locals else self.locals[b[0].name]
                self.compile_stmt(b[1], Assign(py))
            else:
                py = self.new_local(b.name) if b.name not in self.locals else self.locals[b.name]
                self.emit(f"{py} = 0")
        self.emit("while True:")
        self.indent()
        self.loops.append({"kind": "repeat", "ctx": ctx})
        body = x[2:]
        if not body:
            self.emit("pass")
        for stmt in body:
            self.compile_stmt(stmt, Ctx.DISCARD)
        self.loops.pop()
        self.dedent()

    def stmt_prog(self, x, ctx):
        bindings = x[1]
        for b in bindings:
            if isinstance(b, List):
                py = self.new_local(b[0].name)
                self.compile_stmt(b[1], Assign(py))
            else:
                py = self.new_local(b.name)
                self.emit(f"{py} = 0")
        body = x[2:]
        if self.contains_again(body):
            self.emit("while True:")
            self.indent()
            self.loops.append({"kind": "prog", "ctx": ctx})
            self.compile_body(body, ctx)
            self.loops.pop()
            if not self.out.lines[-1][1].startswith("return"):
                self.emit("break")
            self.dedent()
        else:
            self.compile_body(body, ctx)

    def contains_again(self, body):
        def walk(x):
            if isinstance(x, Form):
                h = head(x)
                if h == "AGAIN":
                    return True
                if h in ("REPEAT", "PROG"):
                    return False
                return any(walk(e) for e in x)
            if isinstance(x, List):
                return any(walk(e) for e in x)
            return False
        return any(walk(b) for b in body)

    def stmt_return(self, x):
        val = x[1] if len(x) > 1 else None
        if val is not None:
            # Infocom's ZILCH compiled <RETURN value> as a return from the
            # whole routine, even inside a REPEAT ("funny return"); only a
            # bare <RETURN> leaves the innermost loop.
            self.compile_stmt(val, Ctx.RETURN)
            return
        target = None
        crossing_prog = False
        for lp in reversed(self.loops):
            if lp["kind"] == "repeat":
                target = lp
                break
            crossing_prog = True
        if target is None:
            if val is None:
                self.emit("return True")
            else:
                self.compile_stmt(val, Ctx.RETURN)
            return
        ctx = target["ctx"]
        if crossing_prog and ctx != Ctx.RETURN:
            self.error("RETURN across PROG loop")
        if ctx == Ctx.RETURN:
            if val is None:
                self.emit("return True")
            else:
                self.compile_stmt(val, Ctx.RETURN)
            return
        if isinstance(ctx, Assign):
            if val is None:
                self.emit(f"{ctx.var} = True")
            else:
                self.compile_stmt(val, Assign(ctx.var))
        elif val is not None:
            self.compile_stmt(val, Ctx.DISCARD)
        self.emit("break")

    # ---------- TELL
    def tell_parts(self, args):
        """Return a list of parts; each is ('lit', str) or ('expr', pyexpr, pure)."""
        parts = []
        i = 0
        while i < len(args):
            a = args[i]
            if isinstance(a, str):
                parts.append(("lit", zstr(a)))
                i += 1
                continue
            if isinstance(a, Atom):
                n = a.name
                if n in ("CR", "CRLF"):
                    parts.append(("lit", "\n"))
                    i += 1
                    continue
                if i + 1 >= len(args):
                    self.error("TELL indicator at end")
                o = args[i + 1]
                i += 2
                if n in ("D", "DESC", "O", "OBJ"):
                    parts.append(("call", "z.D", o))
                elif n in ("A", "AN"):
                    parts.append(("call", "z.A", o))
                elif n in ("N", "NUM"):
                    parts.append(("call", "z.N", o))
                elif n in ("C", "CHR", "CHAR"):
                    parts.append(("call", "z.C", o))
                else:
                    parts.append(("prop", n, o))
                continue
            parts.append(("call", "z.S", a))
            i += 1
        return parts

    def stmt_tell(self, args):
        parts = self.tell_parts(args)
        pending = []

        def flush():
            if pending:
                merged = []
                for p in pending:
                    if merged and p[0] == "lit" and merged[-1][0] == "lit":
                        merged[-1] = ("lit", merged[-1][1] + p[1])
                    else:
                        merged.append(p)
                strs = [repr(p[1]) if p[0] == "lit" else p[1] for p in merged]
                self.emit(f"z.tell({', '.join(strs)})")
                pending.clear()

        for p in parts:
            if p[0] == "lit":
                pending.append(p)
                continue
            if p[0] == "prop":
                o = self.compile_expr(p[2])
                expr = f"z.S(z.getp({o}, {self.gen.gname('P?' + p[1])}))"
            else:
                mark = len(self.out.lines)
                o = self.compile_expr(p[2])
                if len(self.out.lines) > mark:
                    new = self.out.lines[mark:]
                    del self.out.lines[mark:]
                    flush()
                    self.out.lines.extend(new)
                expr = f"{p[1]}({o})"
            calls_routine = self.has_routine_call(p[2])
            if calls_routine:
                flush()
                t = self.temp()
                self.emit(f"{t} = {expr}")
                pending.append(("expr", t))
            else:
                pending.append(("expr", expr))
        flush()

    def has_routine_call(self, x):
        if isinstance(x, Form):
            h = head(x)
            if h in self.prog.routines:
                return True
            return any(self.has_routine_call(e) for e in x[1:])
        return False

    # ---------- expressions
    def compile_args(self, nodes):
        exprs = []
        for n in nodes:
            mark = len(self.out.lines)
            e = self.compile_expr(n)
            if len(self.out.lines) > mark and exprs:
                new = self.out.lines[mark:]
                del self.out.lines[mark:]
                for i, pe in enumerate(exprs):
                    if not self.is_trivial(pe):
                        t = self.temp()
                        self.emit(f"{t} = {pe}")
                        exprs[i] = t
                self.out.lines.extend(new)
            exprs.append(e)
        return exprs

    @staticmethod
    def is_trivial(e):
        return e.replace("_", "a").replace(".", "a").isalnum() or e.lstrip("-").isdigit() \
            or e.startswith("'") or e.startswith('"')

    def compile_expr(self, x):
        if isinstance(x, bool):
            return "True" if x else "False"
        if isinstance(x, int):
            return str(x)
        if isinstance(x, str):
            return repr(zstr(x))
        if isinstance(x, LVal):
            n = x.atom.name
            if n not in self.locals:
                self.error(f"unknown local .{n}")
            return self.locals[n]
        if isinstance(x, GVal):
            return self.gval(x.atom.name)
        if isinstance(x, Atom):
            n = x.name
            if n == "T":
                return "True"
            if n in self.prog.routines:
                return f"z.rtn({self.gen.routine_py[n]})"
            if n in self.locals:
                return self.locals[n]
            return self.gval(n)
        if isinstance(x, Quote):
            return self.compile_expr(x.obj)
        if isinstance(x, Form):
            if not x:
                return "False"
            return self.compile_form(x)
        self.error(f"can't compile {x!r}")

    def gval(self, n):
        p = self.prog
        if n in p.ct_constants and n not in p.globals and n not in p.constants:
            v = p.env.gvals[n]
            if v is False or v == Form():
                return "False"
            if v is True or v == T:
                return "True"
            if isinstance(v, int):
                return str(v)
        if n in p.routines:
            return f"z.rtn({self.gen.routine_py[n]})"
        if n in p.constants or n in p.globals or n in p.object_index or n in p.flags \
                or n.startswith(PREFIXES) or n in p.ct_constants or n in SYNTAX_GLOBALS:
            return self.gen.gname(n)
        self.error(f"unknown global ,{n}")

    def compile_form(self, x):
        h = head(x)
        if h is None:
            self.error(f"form with non-atom head {x!r}")
        args = x[1:]
        meth = BUILTINS.get(h)
        if meth:
            return meth(self, args)
        if h in self.prog.routines:
            py = self.gen.routine_py[h]
            nparams = self.gen.routine_nparams[h]
            if len(args) > nparams:
                self.error(f"too many args to {h}")
            es = self.compile_args(args)
            return f"{py}({', '.join(es)})"
        self.error(f"unknown routine or builtin <{h}>")

    # -- helpers used by builtins
    def binop(self, op, args, unary=None):
        es = self.compile_args(args)
        if len(es) == 1 and unary:
            return f"({unary}{es[0]})"
        return "(" + f" {op} ".join(es) + ")"

    def short_circuit(self, kind, args):
        if not args:
            return "True" if kind == "AND" else "False"
        bufs = []
        for a in args:
            with self.capture() as cap:
                e = self.compile_expr(a)
            bufs.append((cap, e))
        if all(c.empty() for c, _ in bufs[1:]):
            bufs[0][0].flush()
            if len(bufs) == 1:
                return bufs[0][1]
            joiner = " and " if kind == "AND" else " or "
            return "(" + joiner.join(e for _, e in bufs) + ")"
        # needs statement lowering
        t = self.temp()
        depth0 = self.out.depth
        for i, (cap, e) in enumerate(bufs):
            cap.flush()
            self.emit(f"{t} = {e}")
            if i < len(bufs) - 1:
                self.emit(f"if {t}:" if kind == "AND" else f"if not {t}:")
                self.indent()
        self.out.depth = depth0
        return t

    def via_temp(self, x):
        t = self.temp()
        self.compile_stmt(x, Assign(t))
        return t


class _Capture:
    def __init__(self, fc):
        self.fc = fc

    def __enter__(self):
        self.saved = self.fc.out.lines
        self.saved_depth = self.fc.out.depth
        self.fc.out.lines = []
        self.fc.out.depth = 0
        return self

    def __exit__(self, *exc):
        self.lines = self.fc.out.lines
        self.fc.out.lines = self.saved
        self.fc.out.depth = self.saved_depth
        return False

    def empty(self):
        return not self.lines

    def flush(self):
        d = self.fc.out.depth
        for depth, text in self.lines:
            self.fc.out.lines.append((depth + d, text))
        self.lines = []


# ---------------------------------------------------------------------------
# builtins:  name -> fn(compiler, args) -> python expression

BUILTINS = {}


def builtin(*names):
    def deco(f):
        for n in names:
            BUILTINS[n] = f
        return f
    return deco


def _call(fn, n=None):
    def f(c, args):
        if n is not None and len(args) != n:
            c.error(f"{fn} expects {n} args, got {len(args)}")
        es = c.compile_args(args)
        return f"{fn}({', '.join(es)})"
    return f


for _zil, _py, _n in [
    ("FSET?", "z.fset_p", 2), ("FSET", "z.fset", 2), ("FCLEAR", "z.fclear", 2),
    ("MOVE", "z.move", 2), ("REMOVE", "z.remove", 1), ("LOC", "z.loc", 1),
    ("IN?", "z.in_p", 2), ("FIRST?", "z.first_p", 1), ("NEXT?", "z.next_p", 1),
    ("GETP", "z.getp", 2), ("PUTP", "z.putp", 3), ("GETPT", "z.getpt", 2),
    ("PTSIZE", "z.ptsize", 1), ("NEXTP", "z.nextp", 2),
    ("GET", "z.get", 2), ("PUT", "z.put", 3), ("GETB", "z.getb", 2),
    ("PUTB", "z.putb", 3), ("RANDOM", "z.random", 1),
    ("PRINTD", "z.printd", 1), ("PRINTN", "z.printn", 1), ("PRINTC", "z.printc", 1),
    ("PRINTB", "z.printb", 1), ("PRINT", "z.print_", 1), ("PRINTI", "z.print_", 1),
    ("CRLF", "z.crlf", 0), ("READ", "z.read", 2), ("SAVE", "z.save", 0),
    ("RESTORE", "z.restore", 0), ("RESTART", "z.restart", 0), ("QUIT", "z.quit", 0),
    ("VERIFY", "z.verify", 0), ("DIROUT", "z.dirout", None), ("DIRIN", "z.dirin", None),
    ("USL", "z.usl", 0), ("NTH", "z.get", 2), ("MIN", "min", None), ("MAX", "max", None), ("MOD", "z.mod", 2), ("BCOM", "z.bcom", 1),
]:
    BUILTINS[_zil] = _call(_py, _n)


@builtin("APPLY")
def _apply(c, args):
    es = c.compile_args(args)
    return f"z.apply({', '.join(es)})"


@builtin("VALUE")
def _value(c, args):
    a = args[0]
    if isinstance(a, Atom):
        if a.name in c.locals:
            return c.locals[a.name]
        return c.gval(a.name)
    return f"z.value({c.compile_expr(a)})"


@builtin("+")
def _add(c, args):
    return c.binop("+", args)


@builtin("-")
def _sub(c, args):
    return c.binop("-", args, unary="-")


@builtin("*")
def _mul(c, args):
    return c.binop("*", args)


@builtin("/")
def _div(c, args):
    es = c.compile_args(args)
    return f"z.div({es[0]}, {es[1]})"


@builtin("BAND")
def _band(c, args):
    return c.binop("&", args)


@builtin("BOR")
def _bor(c, args):
    return c.binop("|", args)


@builtin("BTST")
def _btst(c, args):
    a, b = c.compile_args(args)
    return f"z.btst({a}, {b})"


def _cmp(op):
    def f(c, args):
        a, b = c.compile_args(args)
        return f"({a} {op} {b})"
    return f


for _n, _op in [("G?", ">"), ("GRTR?", ">"), ("L?", "<"), ("LESS?", "<"),
                ("G=?", ">="), ("L=?", "<="), ("N==?", "!="), ("N=?", "!=")]:
    BUILTINS[_n] = _cmp(_op)


@builtin("EQUAL?", "==?", "=?")
def _equal(c, args):
    es = c.compile_args(args)
    if len(es) == 2:
        return f"({es[0]} == {es[1]})"
    return f"({es[0]} in ({', '.join(es[1:])}))"


@builtin("ZERO?", "0?")
def _zero(c, args):
    (a,) = c.compile_args(args)
    return f"({a} == 0)"


@builtin("1?")
def _one(c, args):
    (a,) = c.compile_args(args)
    return f"({a} == 1)"


@builtin("NOT")
def _not(c, args):
    a = args[0]
    if head(a) in ("==?", "=?", "EQUAL?") and len(a) == 3:
        x, y = c.compile_args(a[1:])
        return f"({x} != {y})"
    (e,) = c.compile_args(args)
    return f"(not {e})"


@builtin("AND")
def _and(c, args):
    return c.short_circuit("AND", args)


@builtin("OR")
def _or(c, args):
    return c.short_circuit("OR", args)


def _ctl_form(name):
    def f(c, args):
        return c.via_temp(Form([A(name)] + list(args)))
    return f


for _n in ("COND", "REPEAT", "PROG"):
    BUILTINS[_n] = _ctl_form(_n)


def _ctl_stmt(name):
    def f(c, args):
        c.compile_stmt(Form([A(name)] + list(args)), Ctx.DISCARD)
        return "True" if name == "TELL" else "False"
    return f


for _n in ("RTRUE", "RFALSE", "RFATAL", "AGAIN", "RETURN", "TELL"):
    BUILTINS[_n] = _ctl_stmt(_n)


def _set_expr(h):
    def f(c, args):
        var = c.var_target(args[0], h)
        if isinstance(args[1], Form) and head(args[1]) in ("COND", "REPEAT", "PROG"):
            c.compile_stmt(args[1], Assign(var))
            return var
        (e,) = c.compile_args([args[1]])
        return f"({var} := {e})"
    return f


BUILTINS["SET"] = _set_expr("SET")
BUILTINS["SETG"] = _set_expr("SETG")


def _incdec(op, cmp):
    def f(c, args):
        var = c.var_target(args[0], "SET" if args[0].name in c.locals else "SETG")
        (n,) = c.compile_args([args[1]])
        return f"(({var} := {var} {op} 1) {cmp} {n})"
    return f


BUILTINS["IGRTR?"] = _incdec("+", ">")
BUILTINS["DLESS?"] = _incdec("-", "<")


@builtin("INC")
def _inc(c, args):
    var = c.var_target(args[0], "SET" if args[0].name in c.locals else "SETG")
    return f"({var} := {var} + 1)"


@builtin("DEC")
def _dec(c, args):
    var = c.var_target(args[0], "SET" if args[0].name in c.locals else "SETG")
    return f"({var} := {var} - 1)"


@builtin("REST")
def _rest(c, args):
    es = c.compile_args(args)
    return f"({es[0]} + {es[1] if len(es) > 1 else 1})"


@builtin("BACK")
def _back(c, args):
    es = c.compile_args(args)
    return f"({es[0]} - {es[1] if len(es) > 1 else 1})"


@builtin("ASSIGNED?")
def _assigned(c, args):
    return f"({c.local(args[0])} is not z.NOARG)"


def _multi(var):
    def f(c, args):
        if var == "PRSA":
            vals = [c.gen.gname("V?" + a.name) for a in args]
        else:
            vals = [c.compile_expr(a if not isinstance(a, Atom) else GVal(a)) for a in args]
        g = c.gen.gname(var)
        if len(vals) == 1:
            return f"({g} == {vals[0]})"
        return f"({g} in ({', '.join(vals)}))"
    return f


BUILTINS["VERB?"] = _multi("PRSA")
BUILTINS["PRSO?"] = _multi("PRSO")
BUILTINS["PRSI?"] = _multi("PRSI")
BUILTINS["ROOM?"] = _multi("HERE")


@builtin("ENABLE")
def _enable(c, args):
    (e,) = c.compile_args(args)
    return f"z.put({e}, {c.gen.gname('C-ENABLED?')}, 1)"


@builtin("DISABLE")
def _disable(c, args):
    (e,) = c.compile_args(args)
    return f"z.put({e}, {c.gen.gname('C-ENABLED?')}, 0)"


@builtin("PROB")
def _prob(c, args):
    if len(args) == 2:
        (e,) = c.compile_args(args[:1])
        return f"{c.gen.routine_py['ZPROB']}({e})"
    (e,) = c.compile_args(args)
    return f"({e} > z.random(100))"


@builtin("FLAMING?")
def _flaming(c, args):
    (e,) = c.compile_args(args)
    return f"(z.fset_p({e}, FLAMEBIT) and z.fset_p({e}, ONBIT))"


@builtin("OPENABLE?")
def _openable(c, args):
    (e,) = c.compile_args(args)
    return f"(z.fset_p({e}, DOORBIT) or z.fset_p({e}, CONTBIT))"


@builtin("ABS")
def _abs(c, args):
    (e,) = c.compile_args(args)
    return f"abs({e})"


def _bits(fn, joiner):
    def f(c, args):
        es = c.compile_args(args)
        o, bits = es[0], es[1:]
        return "(" + joiner.join(f"{fn}({o}, {b})" for b in bits) + ")"
    return f


BUILTINS["BSET"] = _bits("z.fset", ", ")
BUILTINS["BCLEAR"] = _bits("z.fclear", ", ")
BUILTINS["BSET?"] = _bits("z.fset_p", " or ")


@builtin("PUSH")
def _push(c, args):
    c.error("PUSH not supported")


def _code_table(kind):
    def f(c, args):
        return c.gen.code_table(Form([A(kind)] + list(args)), c.zname)
    return f


for _n in ("TABLE", "LTABLE", "ITABLE", "PTABLE", "PLTABLE"):
    BUILTINS[_n] = _code_table(_n)


# ---------------------------------------------------------------------------
# module generator

class Generator:
    def __init__(self, prog):
        self.prog = prog
        self.pynames = {}            # python upper name -> zil name
        self.gname_cache = {}
        self.code_tables = []        # (pyname, table form, routine)
        self.routine_py = {}
        self.routine_py_names = set()
        self.routine_nparams = {}
        for name in prog.routine_order:
            py = lower_name(name)
            while py in self.routine_py_names:
                py += "_"
            self.routine_py[name] = py
            self.routine_py_names.add(py)
            args = prog.routines[name][2]
            n = 0
            mode = "REQ"
            for a in args:
                if isinstance(a, str):
                    mode = a
                elif mode in ("REQ", "OPTIONAL", "OPT"):
                    n += 1
            self.routine_nparams[name] = n

    def gname(self, zil):
        if zil in self.gname_cache:
            return self.gname_cache[zil]
        py = upper_name(zil)
        while py in self.pynames and self.pynames[py] != zil or py in PY_RESERVED:
            py += "_"
        self.pynames[py] = zil
        self.gname_cache[zil] = py
        return py

    # ---- tables
    def table_expr(self, x, ctx_routine=None):
        h = head(x)
        args = list(x[1:])
        flags = set()
        if args and isinstance(args[0], List):
            flags = {a.name for a in args[0]}
            args = args[1:]
        if h == "ITABLE":
            spec = args[0]
            if isinstance(spec, Atom):  # <ITABLE NONE 180> / <ITABLE BYTE 60>
                kind = spec.name
                count = args[1]
                defaults = args[2:]
                if kind == "BYTE":
                    flags.add("BYTE")
                elif kind == "WORD":
                    pass
                elif kind != "NONE":
                    raise CompileError(f"ITABLE {kind}")
            else:
                count = spec
                if len(args) > 1 and isinstance(args[1], List):
                    flags |= {a.name for a in args[1]}
                    defaults = args[2:]
                else:
                    defaults = args[1:]
            elems = ", ".join(self.table_elem(e, ctx_routine) for e in defaults) or "0"
            kw = self.table_flags(flags)
            return f"z.itable({count}, [{elems}]{kw})"
        if h in ("LTABLE", "PLTABLE"):
            flags.add("LENGTH")
        elems = ", ".join(self.table_elem(e, ctx_routine) for e in args)
        return f"z.table([{elems}]{self.table_flags(flags)})"

    @staticmethod
    def table_flags(flags):
        kw = ""
        if "BYTE" in flags:
            kw += ", byte=True"
        if "LENGTH" in flags:
            kw += ", length=True"
        if "LEXV" in flags:
            kw += ", lexv=True"
        return kw

    def table_elem(self, e, ctx_routine):
        p = self.prog
        if isinstance(e, Hash) and e.type == "BYTE":
            return f"z.BYTE({self.table_elem(e.obj, ctx_routine)})"
        if isinstance(e, int):
            return str(e)
        if isinstance(e, str):
            return repr(zstr(e))
        if e == Form():
            return "0"
        if isinstance(e, Form) and head(e) in ("TABLE", "LTABLE", "ITABLE", "PTABLE", "PLTABLE"):
            return self.table_expr(e, ctx_routine)
        if isinstance(e, GVal):
            e = e.atom
        if isinstance(e, Atom):
            n = e.name
            if n == "T":
                return "1"
            if n in p.routines:
                return f"z.rtn({self.routine_py[n]})"
            if n in p.object_index or n in p.constants or n in p.globals \
                    or n.startswith(PREFIXES) or n in p.flags:
                return self.gname(n)
        raise CompileError(f"bad table element {e!r}")

    def code_table(self, x, routine):
        py = f"_TBL_{self.routine_py[routine].upper().strip('_')}_{sum(1 for t in self.code_tables if t[2] == routine) + 1}"
        self.code_tables.append((py, x, routine))
        return py

    # ---- objects
    def obj_prop_expr(self, pname, vals):
        p = self.prog
        if pname in p.directions:
            # exits
            if len(vals) == 1 and isinstance(vals[0], str):
                return f"z.nexit({zstr(vals[0])!r})"
            kw = vals[0].name if isinstance(vals[0], Atom) else None
            if kw == "TO":
                room = self.gname(vals[1].name)
                if len(vals) == 2:
                    return f"z.uexit({room})"
                if not is_atom(vals[2], "IF"):
                    raise CompileError(f"bad exit {vals!r}")
                cond = vals[3].name
                rest = vals[4:]
                if rest and is_atom(rest[0], "IS"):
                    # door: IF door IS OPEN [ELSE str]
                    msg = rest[3] if len(rest) > 3 else None
                    m = repr(zstr(msg)) if msg else "0"
                    return f"z.dexit({room}, {self.gname(cond)}, {m})"
                msg = rest[1] if rest else None
                m = repr(zstr(msg)) if msg else "0"
                return f"z.cexit({room}, {self.gname(cond)!r}, {m})"
            if kw == "PER":
                return f"z.fexit(z.rtn({self.routine_py[vals[1].name]}))"
            if kw == "SORRY":
                return f"z.nexit({zstr(vals[1])!r})"
            raise CompileError(f"bad exit {vals!r}")
        if pname == "SYNONYM":
            ws = ", ".join(self.word_ref(p.word_text(w)) for w in vals)
            return f"z.words({ws})"
        if pname == "ADJECTIVE":
            ws = ", ".join(self.adj_ref(p.word_text(w)) for w in vals)
            return f"z.bytes_({ws})"
        if pname == "GLOBAL":
            return f"z.bytes_({', '.join(self.gname(v.name) for v in vals)})"
        if pname == "PSEUDO":
            items = []
            for w, r in zip(vals[::2], vals[1::2]):
                items.append(self.word_ref(p.word_text(w)))
                items.append(f"z.rtn({self.routine_py[r.name]})")
            return f"z.words({', '.join(items)})"
        items = [self.table_elem(v, None) for v in vals]
        return f"z.words({', '.join(items)})"

    def word_ref(self, text):
        return f"_W[{text!r}]"

    def adj_ref(self, text):
        return f"_A[{text!r}]"

    # ---- the whole module
    def generate(self):
        p = self.prog
        p.finish_vocab()
        out = []
        w = out.append
        w('"""Zork I: The Great Underground Empire -- Python translation.')
        w("")
        w("GENERATED FILE - do not edit by hand.  Produced by python/tools/zil2py.py")
        w("from the original Infocom ZIL source:")
        w("")
        w("    " + "\n    ".join(textwrap.wrap(", ".join(["zork1.zil"] + p.source_files), 70)))
        w("")
        w("Routine, variable and object names follow the ZIL source so the two can")
        w('be read side by side.')
        w('"""')
        w("")
        w("from . import runtime as z")
        w("")
        w("# fmt: off")
        w("# flake8: noqa")
        w("")
        # numeric symbols ---------------------------------------------------
        w("# ---------------------------------------------------------------- flags")
        for f in p.flags:
            w(f"{self.gname(f)} = {p.flag_number(f)}")
        w("")
        w("# ----------------------------------------------------------- properties")
        for d in p.directions:
            w(f"{self.gname('P?' + d)} = {p.prop_number(d)}")
        for pr in p.props:
            w(f"{self.gname('P?' + pr)} = {p.prop_number(pr)}")
        w("")
        w("# --------------------------------------------------------------- objects")
        for i, (name, kind, props) in enumerate(p.objects):
            w(f"{self.gname(name)} = {i + 1}")
        w("")
        w("# ------------------------------------------------- actions and verbs")
        for a in p.action_order:
            w(f"{self.gname('V?' + a)} = {p.actions[a][0]}")
        for v, n in p.verb_numbers.items():
            w(f"{self.gname('ACT?' + v.upper())} = {n}")
        for pr, n in p.preps.items():
            w(f"{self.gname('PR?' + pr.upper())} = {n}")
        w("")
        w("# ------------------------------------------------- parts of speech")
        for pos, bit in PS_BITS.items():
            w(f"{self.gname('PS?' + pos)} = {bit}")
        for pos, code in P1_CODES.items():
            if pos != "PREPOSITION":
                w(f"{self.gname('P1?' + pos)} = {code}")
        w("")
        w("# ----------------------------------------------- compile-time settings")
        for name, node in p.ct_constants.items():
            if name in p.constants or name in p.globals:
                continue
            v = p.env.gvals[name]
            if isinstance(v, int) and not isinstance(v, bool):
                w(f"{self.gname(name)} = {v}")
            elif v is False or v == Form():
                w(f"{self.gname(name)} = False")
        w("")
        w("# ------------------------------------------------- numeric constants")
        deferred_constants = []
        for name, node in p.constants.items():
            if isinstance(node, int):
                w(f"{self.gname(name)} = {node}")
            elif node == Form():
                w(f"{self.gname(name)} = False")
            else:
                deferred_constants.append(name)
        w("")
        # routines -------------------------------------------------------------
        compiled = []
        for name in p.routine_order:
            fc = FnCompiler(self, name, p.routines[name])
            compiled.append((name, fc.compile()))
        w("# ===================================================================")
        w("# Routines")
        w("# ===================================================================")
        w("")
        for name, code in compiled:
            w(code)
            w("")
            w("")
        # data -----------------------------------------------------------------
        w("# ===================================================================")
        w("# Data: vocabulary, objects, tables and globals")
        w("# ===================================================================")
        w("")
        w("z.begin_build(globals())")
        w("")
        w("# Vocabulary: (word, parts-of-speech byte, value 1, value 2)")
        w("_W = z.vocabulary([")
        for text in sorted(p.words, key=lambda t: t):
            ps, v1, v2 = p.word_record(p.words[text])
            w(f"    ({text!r}, {ps:#04x}, {v1}, {v2}),")
        w("])")
        adjs = {t: wd.values["ADJECTIVE"] for t, wd in p.words.items() if "ADJECTIVE" in wd.values}
        w("_A = {" + ", ".join(f"{t!r}: {v}" for t, v in sorted(adjs.items())) + "}")
        w("")
        w("# Words referred to by the code (W?...)")
        self.used_words = sorted(self.collect_word_refs())
        for zname in self.used_words:
            text = SPECIAL_WORDS.get(zname, zname.lower())
            if text not in p.words:
                raise CompileError(f"W?{zname} is not in the vocabulary")
            w(f"{self.gname('W?' + zname)} = _W[{text!r}]")
        w("")
        w("# Global variables, numbered from 16 as in the Z-machine")
        names = [n for n in p.globals]
        w("z.declare_globals([")
        for n in names:
            w(f"    {self.gname(n)!r},")
        w("])")
        w("")
        w("# Objects, in definition order.  Children are linked in reverse")
        w("# definition order, as the original compiler did.")
        defaults = []
        for pname, node in p.propdefs.items():
            defaults.append(f"{self.gname('P?' + pname)}: {self.table_elem(node, None)}")
        w("z.property_defaults({" + ", ".join(defaults) + "})")
        w("")
        for name, kind, props in p.objects:
            desc = ""
            parent = "0"
            flags = []
            plist = []
            for pr in props:
                pname = pr[0].name
                vals = list(pr[1:])
                if pname == "LOC" or (pname == "IN" and len(vals) == 1
                                         and isinstance(vals[0], Atom)):
                    parent = self.gname(vals[0].name)
                elif pname == "DESC":
                    desc = zstr(vals[0])
                elif pname == "FLAGS":
                    flags = [self.gname(f.name) for f in vals]
                else:
                    plist.append((p.prop_number(pname), self.gname("P?" + pname),
                                  self.obj_prop_expr(pname, vals)))
            plist.sort(key=lambda t: -t[0])
            w(f"z.define_object({self.gname(name)}, {desc!r}, parent={parent},")
            w(f"    flags=[{', '.join(flags)}],")
            if plist:
                w("    props=[")
                for _, pn, pe in plist:
                    w(f"        ({pn}, {pe}),")
                w("    ])")
            else:
                w("    props=[])")
        w("z.link_objects()")
        w("")
        w("# Globals and table constants, in source order")
        for name in deferred_constants:
            w(f"{self.gname(name)} = {self.global_init(p.constants[name])}")
        for name, node in p.globals.items():
            w(f"{self.gname(name)} = {self.global_init(node)}")
        w("")
        w("# Tables that appear inside routine bodies")
        for py, form, routine in self.code_tables:
            w(f"{py} = {self.table_expr(form, routine)}")
        w("")
        w("# Syntax tables used by the parser")
        self.emit_syntax(w)
        w("")
        w("z.end_build()")
        w("")
        return "\n".join(out)

    def global_init(self, node):
        if isinstance(node, Form) and head(node) in ("TABLE", "LTABLE", "ITABLE", "PTABLE", "PLTABLE"):
            return self.table_expr(node)
        return self.table_elem(node, None)

    def collect_word_refs(self):
        found = set()

        def walk(x):
            if isinstance(x, GVal) and isinstance(x.atom, Atom) and x.atom.name.startswith("W?"):
                found.add(x.atom.name[2:])
            elif isinstance(x, (Form, List, Vector)):
                for e in x:
                    walk(e)
        for r in self.prog.routines.values():
            walk(r)
        for g in self.prog.globals.values():
            walk(g)
        return found

    def emit_syntax(self, w):
        p = self.prog
        by_verb = {}
        for s in p.syntaxes:
            v = s["verb"]
            for hd, syns in p.synonyms:
                if v in syns:
                    v = hd
            by_verb.setdefault(v, []).append(s)
        w("_SYNTAX = {}")
        w("# Each entry: (objects, prep1, prep2, find1, find2, loc1, loc2, action)")
        for v, syns in by_verb.items():
            w(f"_SYNTAX[{self.gname('ACT?' + v.upper())}] = [")
            for s in reversed(syns):  # stored in reverse definition order
                def pr(k):
                    return self.gname("PR?" + s[k].upper()) if s[k] else "0"

                def fd(k):
                    return self.gname(s[k]) if s[k] else "0"
                w(f"    ({s['nobj']}, {pr('prep1')}, {pr('prep2')}, {fd('find1')}, {fd('find2')}, "
                  f"{s['loc1']}, {s['loc2']}, {self.gname('V?' + s['action'])}),")
            w("]")
        w("VERBS = z.verbs_table(_SYNTAX)")
        w("ACTIONS = z.action_table({")
        for a in p.action_order:
            w(f"    {self.gname('V?' + a)}: z.rtn({self.routine_py[p.actions[a][1]]}),")
        w(f"}}, size={len(p.action_order) + 1})")
        w("PREACTIONS = z.action_table({")
        for a in p.action_order:
            pre = p.actions[a][2]
            if pre:
                w(f"    {self.gname('V?' + a)}: z.rtn({self.routine_py[pre]}),")
        w(f"}}, size={len(p.action_order) + 1})")
        canon = sorted(p.preps.items(), key=lambda kv: kv[1])
        w("PREPOSITIONS = z.prepositions_table([" +
          ", ".join(f"(_W[{t!r}], {self.gname('PR?' + t.upper())})" for t, n in canon) + "])")


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--src", default=os.path.join(here, "..", ".."))
    ap.add_argument("--out", default=os.path.join(here, "..", "zork1", "game.py"))
    args = ap.parse_args()
    prog = Program()
    prog.load(args.src)
    gen = Generator(prog)
    code = gen.generate()
    with open(args.out, "w") as f:
        f.write(code)
    print(f"wrote {args.out}: {len(prog.routines)} routines, {len(prog.objects)} objects, "
          f"{len(prog.words)} words, {len(prog.globals)} globals", file=sys.stderr)


if __name__ == "__main__":
    main()
