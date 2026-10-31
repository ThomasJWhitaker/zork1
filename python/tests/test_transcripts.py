"""Transcript tests: the Python translation must produce exactly the same
output as the original story file (COMPILED/zork1.z3) run on the reference
interpreter, for scripted and randomly generated command sequences.

Run with pytest, or directly:  python3 python/tests/test_transcripts.py
"""

import glob
import os
import random
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "tools"))

import difftest  # noqa: E402
import fuzz  # noqa: E402

SCRIPTS = sorted(glob.glob(os.path.join(HERE, "*.txt")))


def check(commands, seed):
    a = difftest.run_original(commands, seed)
    b = difftest.run_python(commands, seed)
    assert a == b, "transcripts differ"


def test_scripts():
    for path in SCRIPTS:
        commands = open(path).read().splitlines()
        for seed in (1, 2, 3):
            check(commands, seed)


def test_fuzz():
    vocab = fuzz.vocabulary()
    full = open(os.path.join(HERE, "fullgame.txt")).read().splitlines()
    full = [c for c in full if c not in ("quit", "y")]
    for run in range(10):
        rng = random.Random(run)
        cmds = full[:rng.randint(0, len(full))]
        cmds += [fuzz.random_command(rng, vocab) for _ in range(150)]
        cmds = [c for c in cmds if not any(w.startswith(("save", "restor")) for w in c.split())]
        check(cmds, rng.randint(1, 10 ** 6))


if __name__ == "__main__":
    test_scripts()
    print(f"scripts: OK ({len(SCRIPTS)} files x 3 seeds)")
    test_fuzz()
    print("fuzz: OK (10 runs)")
