#!/usr/bin/env python3
"""Differential test: run the same commands through the original story file
(on the reference interpreter in zmachine.py) and through the Python
translation, with an identical random-number stream, and compare the
transcripts.

    python3 python/tools/difftest.py commands.txt [--seed N] [--show]

Exit status is 0 when the transcripts are identical.
"""

import argparse
import difflib
import io
import os
import random
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.normpath(os.path.join(HERE, "..", ".."))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(ROOT, "python"))

STORY = os.path.join(ROOT, "COMPILED", "zork1.z3")


def make_input(commands, out):
    it = iter(commands)

    def inp():
        c = next(it, None)
        if c is not None:
            out.write(c + "\n")
        return c
    return inp


def make_random(seed):
    rng = random.Random(seed)

    def rnd(n):
        return rng.randint(1, n)
    return rnd


def run_original(commands, seed):
    from zmachine import ZMachine
    out = io.StringIO()
    rnd = make_random(seed)

    def zr(n):
        if n <= 0:
            return 0
        return rnd(n)
    vm = ZMachine(open(STORY, "rb").read(), make_input(commands, out), out.write, zr)
    vm.run()
    # Known bug in the original: SWIM with no object prints the "name" of
    # object 0, i.e. whatever bytes precede the object table.  The Python
    # version prints an empty name there instead.
    #
    # Known compiler artifact: ZILCH gave the empty string in <JIGS-UP "">
    # (V-PLAY, "play <actor>") the address of the next string in the string
    # table, so the original prints " has no effect." as the death message.
    # The Python version prints the intended empty message.
    text = out.getvalue().replace(OBJECT0_NAME, "")
    return text.replace("might have done!\n has no effect.\n", "might have done!\n\n")


def _object0_name():
    from zmachine import ZMachine
    vm = ZMachine(open(STORY, "rb").read(), None, None, None)
    return vm.decode(vm.w(vm.obj(0) + 7) + 1)[0]


OBJECT0_NAME = _object0_name()


def run_python(commands, seed):
    import importlib
    from zork1 import runtime
    out = io.StringIO()
    runtime.screen.stream = out
    runtime.screen.wrap = False
    runtime.random_fn = make_random(seed)
    if "zork1.game" in sys.modules:
        game = sys.modules["zork1.game"]
        runtime._load(runtime._initial_state)
    else:
        game = importlib.import_module("zork1.game")
    try:
        runtime.run(game.go, make_input(commands, out))
    except Exception:
        import traceback
        out.write("\n*** PYTHON EXCEPTION ***\n" + traceback.format_exc())
    return out.getvalue()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("commands")
    ap.add_argument("--seed", type=int, default=1)
    ap.add_argument("--show", action="store_true", help="print the Python transcript")
    args = ap.parse_args()
    commands = open(args.commands).read().splitlines()
    a = run_original(commands, args.seed)
    b = run_python(commands, args.seed)
    if args.show:
        print(b)
    if a == b:
        print(f"OK: transcripts identical ({len(commands)} commands, {len(a)} chars)")
        return 0
    diff = difflib.unified_diff(a.splitlines(), b.splitlines(), "original", "python",
                                lineterm="", n=2)
    for i, line in enumerate(diff):
        if i > 80:
            print("...")
            break
        print(line)
    return 1


if __name__ == "__main__":
    sys.exit(main())
