"""A reader for ZIL / MDL source text.

Produces a small tree of Python objects:

  Atom(name)            an MDL atom
  str                   a string literal (escapes already processed)
  int                   a number
  Form([...])           <...>
  List([...])           (...)
  Vector([...])         [...]
  GVal(x)  LVal(x)      ,X  .X
  Quote(x)              'X
  Segment(x)            !X
  Hash(type, x)         #TYPE x   (e.g. #BYTE 0, #DECL (...))
  Char(c)               !\\c  or \\c used as a character
  Eval(x)               %X   (compile-time evaluation)

Comments (``;`` followed by any object) are dropped.
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class Atom:
    name: str

    def __repr__(self):
        return self.name


class Form(list):
    def __repr__(self):
        return "<" + " ".join(map(repr, self)) + ">"


class List(list):
    def __repr__(self):
        return "(" + " ".join(map(repr, self)) + ")"


class Vector(list):
    def __repr__(self):
        return "[" + " ".join(map(repr, self)) + "]"


@dataclass
class GVal:
    atom: object

    def __repr__(self):
        return "," + repr(self.atom)


@dataclass
class LVal:
    atom: object

    def __repr__(self):
        return "." + repr(self.atom)


@dataclass
class Quote:
    obj: object

    def __repr__(self):
        return "'" + repr(self.obj)


@dataclass
class Segment:
    obj: object


@dataclass
class Hash:
    type: str
    obj: object


@dataclass
class Char:
    ch: str


@dataclass
class Eval:
    obj: object


class ReadError(Exception):
    pass


_DELIMS = set(" \t\r\n\f<>()[]{}\";,.'!%#")
# '.' and ',' are only delimiters at the *start* of an object; inside an atom
# name they are ordinary characters in MDL, but ZIL code never relies on that,
# so we treat them as ordinary inside atoms (e.g. "V?WALK" has none anyway).
_ATOM_STOP = set(" \t\r\n\f<>()[]{}\";,")


class Reader:
    def __init__(self, text, filename="?"):
        self.text = text
        self.pos = 0
        self.filename = filename

    def error(self, msg):
        line = self.text.count("\n", 0, self.pos) + 1
        raise ReadError(f"{self.filename}:{line}: {msg}")

    def skip_ws(self):
        t = self.text
        while self.pos < len(t) and t[self.pos] in " \t\r\n\f\x0c":
            self.pos += 1

    def read_all(self):
        out = []
        while True:
            obj = self.read()
            if obj is _EOF:
                return out
            out.append(obj)

    def read(self, closer=None):
        """Read one object. Returns _EOF at end, or _CLOSE if `closer` is hit."""
        while True:
            self.skip_ws()
            if self.pos >= len(self.text):
                if closer:
                    self.error(f"EOF while looking for {closer!r}")
                return _EOF
            c = self.text[self.pos]
            if c == ";":
                self.pos += 1
                obj = self.read(closer)
                if obj is _CLOSE:
                    self.error("comment before close bracket")
                continue  # drop comment
            break
        if closer and c == closer:
            self.pos += 1
            return _CLOSE
        if c in ">)]":
            self.error(f"unexpected {c!r}")
        if c == "<":
            self.pos += 1
            # "<>" is the empty form (false)
            return Form(self.read_seq(">"))
        if c == "(":
            self.pos += 1
            return List(self.read_seq(")"))
        if c == "[":
            self.pos += 1
            return Vector(self.read_seq("]"))
        if c == '"':
            return self.read_string()
        if c == ",":
            self.pos += 1
            return GVal(self.read_obj())
        if c == ".":
            self.pos += 1
            return LVal(self.read_obj())
        if c == "'":
            self.pos += 1
            return Quote(self.read_obj())
        if c == "%":
            self.pos += 1
            if self.text[self.pos] == "%":
                self.pos += 1
                self.read_obj()  # %% : evaluate and discard
                return self.read(closer)
            return Eval(self.read_obj())
        if c == "!":
            self.pos += 1
            if self.text[self.pos] == "\\":
                self.pos += 1
                ch = self.text[self.pos]
                self.pos += 1
                return Char(ch)
            return Segment(self.read_obj())
        if c == "#":
            self.pos += 1
            typ = self.read_atom_text()
            return Hash(typ, self.read_obj())
        return self.read_atom_or_number()

    def read_obj(self):
        obj = self.read()
        if obj is _EOF or obj is _CLOSE:
            self.error("expected an object")
        return obj

    def read_seq(self, closer):
        out = []
        while True:
            obj = self.read(closer)
            if obj is _CLOSE:
                return out
            out.append(obj)

    def read_string(self):
        t = self.text
        self.pos += 1
        buf = []
        while True:
            if self.pos >= len(t):
                self.error("unterminated string")
            c = t[self.pos]
            if c == "\\":
                buf.append(t[self.pos + 1])
                self.pos += 2
                continue
            if c == '"':
                self.pos += 1
                return "".join(buf)
            buf.append(c)
            self.pos += 1

    def read_atom_text(self):
        t = self.text
        buf = []
        while self.pos < len(t):
            c = t[self.pos]
            if c == "\\":
                buf.append(t[self.pos + 1])
                self.pos += 2
                continue
            if c in _ATOM_STOP:
                break
            buf.append(c)
            self.pos += 1
        if not buf:
            self.error("empty atom")
        return "".join(buf)

    def read_atom_or_number(self):
        start = self.pos
        text = self.read_atom_text()
        raw = self.text[start:self.pos]
        if "\\" not in raw:
            if text.lstrip("-").isdigit():
                return int(text)
            if len(text) > 2 and text[0] == "*" and text[-1] == "*" and text[1:-1].isdigit():
                return int(text[1:-1], 8)
        return Atom(text)


class _Sentinel:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return self.name


_EOF = _Sentinel("EOF")
_CLOSE = _Sentinel("CLOSE")


def read_file(path):
    with open(path, encoding="latin-1") as f:
        text = f.read()
    return Reader(text, path).read_all()
