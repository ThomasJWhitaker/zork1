"""A minimal Z-machine version 3 interpreter.

Used as a reference oracle: it runs the original compiled story file
(COMPILED/zork1.z3) so the Python port's output can be compared against
it transcript-for-transcript.  Randomness is delegated to a callable so
both implementations can share an identical random stream.

Usage: python3 zmachine.py story.z3 [commands.txt]
"""

import sys

A0 = "abcdefghijklmnopqrstuvwxyz"
A1 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
A2 = " \n0123456789.,!?_#'\"/\\-:()"


class Quit(Exception):
    pass


class ZMachine:
    def __init__(self, story, input_fn, output_fn, random_fn):
        self.mem = bytearray(story)
        self.orig = bytes(story)
        self.input_fn = input_fn
        self.out = output_fn
        self.random_fn = random_fn
        self.restart()

    def restart(self):
        self.mem[:] = self.orig
        m = self.mem
        self.pc = self.w(6)
        self.dict_addr = self.w(8)
        self.obj_addr = self.w(10)
        self.glob_addr = self.w(12)
        self.abbr_addr = self.w(0x18)
        self.stack = []
        self.frames = []  # (return pc, locals, stack depth, store var)
        self.locals = []
        n = m[self.dict_addr]
        self.separators = [chr(c) for c in m[self.dict_addr + 1:self.dict_addr + 1 + n]]
        p = self.dict_addr + 1 + n
        self.entry_len = m[p]
        self.dict_count = self.w(p + 1)
        self.dict_start = p + 3
        self.dict = {}
        for i in range(self.dict_count):
            a = self.dict_start + i * self.entry_len
            self.dict[bytes(m[a:a + 4])] = a

    # ---- memory helpers
    def w(self, a):
        return (self.mem[a] << 8) | self.mem[a + 1]

    def setw(self, a, v):
        v &= 0xFFFF
        self.mem[a] = v >> 8
        self.mem[a + 1] = v & 0xFF

    # ---- text
    def decode(self, a, abbrev=True):
        zchars = []
        while True:
            word = self.w(a)
            a += 2
            zchars += [(word >> 10) & 31, (word >> 5) & 31, word & 31]
            if word & 0x8000:
                break
        return self.zchars_to_str(zchars, abbrev), a

    def zchars_to_str(self, zchars, abbrev=True):
        out = []
        alpha = 0
        i = 0
        while i < len(zchars):
            c = zchars[i]
            if c == 0:
                out.append(" ")
            elif c in (1, 2, 3):
                if i + 1 < len(zchars):
                    idx = 32 * (c - 1) + zchars[i + 1]
                    addr = self.w(self.abbr_addr + idx * 2) * 2
                    out.append(self.decode(addr, False)[0])
                i += 1
            elif c == 4:
                alpha = 1
                i += 1
                continue
            elif c == 5:
                alpha = 2
                i += 1
                continue
            else:
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

    def encode(self, word):
        zs = []
        for ch in word[:6]:
            if ch in A0:
                zs.append(A0.index(ch) + 6)
            elif ch in A2 and ch not in " \n":
                zs += [5, A2.index(ch) + 6]
            else:
                o = ord(ch)
                zs += [5, 6, o >> 5, o & 31]
        zs = (zs + [5] * 6)[:6]
        w1 = (zs[0] << 10) | (zs[1] << 5) | zs[2]
        w2 = (zs[3] << 10) | (zs[4] << 5) | zs[5] | 0x8000
        return bytes([w1 >> 8, w1 & 255, w2 >> 8, w2 & 255])

    # ---- objects
    def obj(self, n):
        return self.obj_addr + 62 + (n - 1) * 9

    def parent(self, n):
        return self.mem[self.obj(n) + 4]

    def sibling(self, n):
        return self.mem[self.obj(n) + 5]

    def child(self, n):
        return self.mem[self.obj(n) + 6]

    def props(self, n):
        return self.w(self.obj(n) + 7)

    def obj_name(self, n):
        p = self.props(n)
        if self.mem[p] == 0:
            return ""
        return self.decode(p + 1)[0]

    def first_prop(self, n):
        p = self.props(n)
        return p + 1 + self.mem[p] * 2

    def find_prop(self, n, prop):
        p = self.first_prop(n)
        while self.mem[p]:
            b = self.mem[p]
            num, size = b & 31, (b >> 5) + 1
            if num == prop:
                return p + 1, size
            if num < prop:
                break
            p += 1 + size
        return 0, 0

    def unlink(self, n):
        o = self.obj(n)
        par = self.mem[o + 4]
        if not par:
            return
        po = self.obj(par)
        if self.mem[po + 6] == n:
            self.mem[po + 6] = self.mem[o + 5]
        else:
            c = self.mem[po + 6]
            while c:
                co = self.obj(c)
                if self.mem[co + 5] == n:
                    self.mem[co + 5] = self.mem[o + 5]
                    break
                c = self.mem[co + 5]
        self.mem[o + 4] = 0
        self.mem[o + 5] = 0

    # ---- variables
    def read_var(self, v):
        if v == 0:
            return self.stack.pop()
        if v < 16:
            return self.locals[v - 1]
        return self.w(self.glob_addr + (v - 16) * 2)

    def write_var(self, v, val):
        val &= 0xFFFF
        if v == 0:
            self.stack.append(val)
        elif v < 16:
            self.locals[v - 1] = val
        else:
            self.setw(self.glob_addr + (v - 16) * 2, val)

    def fetch(self):
        b = self.mem[self.pc]
        self.pc += 1
        return b

    def fetchw(self):
        v = self.w(self.pc)
        self.pc += 2
        return v

    def store(self, val):
        self.write_var(self.fetch(), val)

    def branch(self, cond):
        b = self.fetch()
        on_true = bool(b & 0x80)
        if b & 0x40:
            off = b & 0x3F
        else:
            off = ((b & 0x3F) << 8) | self.fetch()
            if off & 0x2000:
                off -= 0x4000
        if cond == on_true:
            if off == 0:
                self.ret(0)
            elif off == 1:
                self.ret(1)
            else:
                self.pc += off - 2

    def call(self, addr, args, store_var):
        if addr == 0:
            self.write_var(store_var, 0)
            return
        a = addr * 2
        nloc = self.mem[a]
        a += 1
        locs = []
        for i in range(nloc):
            locs.append(self.w(a))
            a += 2
        for i, v in enumerate(args[:nloc]):
            locs[i] = v
        self.frames.append((self.pc, self.locals, len(self.stack), store_var))
        self.locals = locs
        self.pc = a

    def ret(self, val):
        pc, locs, depth, sv = self.frames.pop()
        del self.stack[depth:]
        self.pc = pc
        self.locals = locs
        self.write_var(sv, val)

    @staticmethod
    def s(v):
        return v - 0x10000 if v & 0x8000 else v

    def print_(self, s):
        self.out(s)

    # ---- main loop
    def run(self):
        try:
            while True:
                self.step()
        except Quit:
            pass

    def step(self):
        op = self.fetch()
        if op < 0x80:  # long 2OP
            t1 = 2 if op & 0x40 else 1
            t2 = 2 if op & 0x20 else 1
            ops = [self.operand(t1), self.operand(t2)]
            self.op2(op & 31, ops)
        elif op < 0xB0:  # short 1OP
            t = (op >> 4) & 3
            ops = [self.operand(t)]
            self.op1(op & 15, ops[0], t)
        elif op < 0xC0:
            self.op0(op & 15)
        else:
            types = self.fetch()
            ops = []
            for sh in (6, 4, 2, 0):
                t = (types >> sh) & 3
                if t == 3:
                    break
                ops.append(self.operand(t))
            if op < 0xE0:
                self.op2(op & 31, ops)
            else:
                self.opvar(op & 31, ops)

    def operand(self, t):
        if t == 0:
            return self.fetchw()
        if t == 1:
            return self.fetch()
        return self.read_var(self.fetch())

    def op2(self, n, o):
        s = self.s
        if n == 1:
            self.branch(any(o[0] == x for x in o[1:]))
        elif n == 2:
            self.branch(s(o[0]) < s(o[1]))
        elif n == 3:
            self.branch(s(o[0]) > s(o[1]))
        elif n == 4:
            v = o[0]
            nv = (s(self.peek_var(v)) - 1) & 0xFFFF
            self.poke_var(v, nv)
            self.branch(s(nv) < s(o[1]))
        elif n == 5:
            v = o[0]
            nv = (s(self.peek_var(v)) + 1) & 0xFFFF
            self.poke_var(v, nv)
            self.branch(s(nv) > s(o[1]))
        elif n == 6:
            self.branch(self.parent(o[0]) == o[1])
        elif n == 7:
            self.branch((o[0] & o[1]) == o[1])
        elif n == 8:
            self.store(o[0] | o[1])
        elif n == 9:
            self.store(o[0] & o[1])
        elif n == 10:
            a = self.obj(o[0]) + o[1] // 8
            self.branch(bool(self.mem[a] & (0x80 >> (o[1] % 8))))
        elif n == 11:
            a = self.obj(o[0]) + o[1] // 8
            self.mem[a] |= 0x80 >> (o[1] % 8)
        elif n == 12:
            a = self.obj(o[0]) + o[1] // 8
            self.mem[a] &= ~(0x80 >> (o[1] % 8)) & 0xFF
        elif n == 13:
            self.poke_var(o[0], o[1])
        elif n == 14:
            obj, dest = o
            self.unlink(obj)
            oo = self.obj(obj)
            do = self.obj(dest)
            self.mem[oo + 5] = self.mem[do + 6]
            self.mem[oo + 4] = dest
            self.mem[do + 6] = obj
        elif n == 15:
            self.store(self.w((o[0] + 2 * s(o[1])) & 0xFFFF))
        elif n == 16:
            self.store(self.mem[(o[0] + s(o[1])) & 0xFFFF])
        elif n == 17:
            a, size = self.find_prop(o[0], o[1])
            if a:
                self.store(self.mem[a] if size == 1 else self.w(a))
            else:
                self.store(self.w(self.obj_addr + (o[1] - 1) * 2))
        elif n == 18:
            a, size = self.find_prop(o[0], o[1])
            self.store(a)
        elif n == 19:
            if o[1] == 0:
                p = self.first_prop(o[0])
            else:
                a, size = self.find_prop(o[0], o[1])
                p = a + size
            self.store(self.mem[p] & 31)
        elif n == 20:
            self.store(s(o[0]) + s(o[1]))
        elif n == 21:
            self.store(s(o[0]) - s(o[1]))
        elif n == 22:
            self.store(s(o[0]) * s(o[1]))
        elif n == 23:
            a, b = s(o[0]), s(o[1])
            q = abs(a) // abs(b)
            self.store(q if (a < 0) == (b < 0) else -q)
        elif n == 24:
            a, b = s(o[0]), s(o[1])
            r = abs(a) % abs(b)
            self.store(-r if a < 0 else r)
        else:
            raise RuntimeError(f"bad 2OP {n} at {self.pc:x}")

    def peek_var(self, v):
        if v == 0:
            return self.stack[-1]
        return self.read_var(v)

    def poke_var(self, v, val):
        if v == 0:
            self.stack[-1] = val & 0xFFFF
        else:
            self.write_var(v, val)

    def op1(self, n, a, t):
        s = self.s
        if n == 0:
            self.branch(a == 0)
        elif n == 1:
            v = self.sibling(a)
            self.store(v)
            self.branch(v != 0)
        elif n == 2:
            v = self.child(a)
            self.store(v)
            self.branch(v != 0)
        elif n == 3:
            self.store(self.parent(a))
        elif n == 4:
            self.store((self.mem[a - 1] >> 5) + 1 if a else 0)
        elif n == 5:
            self.poke_var(a, s(self.peek_var(a)) + 1)
        elif n == 6:
            self.poke_var(a, s(self.peek_var(a)) - 1)
        elif n == 7:
            self.print_(self.decode(a)[0])
        elif n == 9:
            self.unlink(a)
        elif n == 10:
            self.print_(self.obj_name(a))
        elif n == 11:
            self.ret(a)
        elif n == 12:
            self.pc += s(a) - 2
        elif n == 13:
            self.print_(self.decode(a * 2)[0])
        elif n == 14:
            self.store(self.peek_var(a))
        elif n == 15:
            self.store(~a)
        else:
            raise RuntimeError(f"bad 1OP {n}")

    def op0(self, n):
        if n == 0:
            self.ret(1)
        elif n == 1:
            self.ret(0)
        elif n == 2:
            s, self.pc = self.decode(self.pc)
            self.print_(s)
        elif n == 3:
            s, self.pc = self.decode(self.pc)
            self.print_(s + "\n")
            self.ret(1)
        elif n == 4:
            pass
        elif n == 5:  # save
            self.branch(False)
        elif n == 6:  # restore
            self.branch(False)
        elif n == 7:
            self.restart()
        elif n == 8:
            self.ret(self.stack.pop())
        elif n == 9:
            self.stack.pop()
        elif n == 10:
            raise Quit()
        elif n == 11:
            self.print_("\n")
        elif n == 12:
            pass  # show_status
        elif n == 13:
            self.branch(True)
        else:
            raise RuntimeError(f"bad 0OP {n}")

    def opvar(self, n, o):
        if n == 0:
            self.call(o[0], o[1:], self.fetch())
        elif n == 1:
            self.setw((o[0] + 2 * self.s(o[1])) & 0xFFFF, o[2])
        elif n == 2:
            self.mem[(o[0] + self.s(o[1])) & 0xFFFF] = o[2] & 255
        elif n == 3:
            a, size = self.find_prop(o[0], o[1])
            if size == 1:
                self.mem[a] = o[2] & 255
            else:
                self.setw(a, o[2])
        elif n == 4:
            self.sread(o[0], o[1])
        elif n == 5:
            self.print_(chr(o[0]))
        elif n == 6:
            self.print_(str(self.s(o[0])))
        elif n == 7:
            self.store(self.random_fn(self.s(o[0])))
        elif n == 8:
            self.stack.append(o[0])
        elif n == 9:
            self.poke_var(o[0], self.stack.pop())
        elif n in (10, 11, 19, 20, 21):
            pass  # split/set window, output/input stream, sound
        else:
            raise RuntimeError(f"bad VAR {n}")

    def sread(self, tbuf, pbuf):
        line = self.input_fn()
        if line is None:
            raise Quit()
        maxlen = self.mem[tbuf]
        line = line.lower()[:maxlen - 1]
        for i, ch in enumerate(line):
            self.mem[tbuf + 1 + i] = ord(ch)
        self.mem[tbuf + 1 + len(line)] = 0
        tokenize(self, line, pbuf)


def tokenize(vm, line, pbuf):
    """Shared by the oracle: split `line` into words, store parse entries."""
    words = []
    i = 0
    while i < len(line):
        ch = line[i]
        if ch == " ":
            i += 1
            continue
        if ch in vm.separators:
            words.append((ch, i))
            i += 1
            continue
        j = i
        while j < len(line) and line[j] != " " and line[j] not in vm.separators:
            j += 1
        words.append((line[i:j], i))
        i = j
    maxw = vm.mem[pbuf]
    words = words[:maxw]
    vm.mem[pbuf + 1] = len(words)
    for k, (wd, pos) in enumerate(words):
        a = pbuf + 2 + 4 * k
        vm.setw(a, vm.dict.get(vm.encode(wd), 0))
        vm.mem[a + 2] = len(wd)
        vm.mem[a + 3] = pos + 1


def main():
    story = open(sys.argv[1], "rb").read()
    import random

    rng = random.Random(int(sys.argv[3]) if len(sys.argv) > 3 else 0)
    if len(sys.argv) > 2:
        cmds = iter(open(sys.argv[2]).read().splitlines())

        def inp():
            c = next(cmds, None)
            if c is not None:
                sys.stdout.write(c + "\n")
            return c
    else:
        def inp():
            try:
                return input()
            except EOFError:
                return None

    def rnd(n):
        if n <= 0:
            return 0
        return rng.randint(1, n)

    vm = ZMachine(story, inp, lambda s: sys.stdout.write(s), rnd)
    vm.run()


if __name__ == "__main__":
    main()
