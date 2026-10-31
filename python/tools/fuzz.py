#!/usr/bin/env python3
"""Random-command differential fuzzer.

Builds random (mostly plausible) commands from the game's own vocabulary,
optionally after a prefix of tests/fullgame.txt so play reaches deep into
the dungeon, and checks that the original story file and the Python
translation produce identical transcripts.

    python3 python/tools/fuzz.py [--runs N] [--length L] [--seed S]
"""

import argparse
import difflib
import os
import random
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import difftest  # noqa: E402
from zmachine import ZMachine  # noqa: E402


def vocabulary():
    vm = ZMachine(open(difftest.STORY, "rb").read(), None, None, None)
    m = vm.mem
    cats = {"noun": [], "verb": [], "adj": [], "dir": [], "prep": [], "buzz": []}
    for i in range(vm.dict_count):
        a = vm.dict_start + i * vm.entry_len
        w = vm.decode(a)[0]
        ps = m[a + 4]
        if ps & 0x80:
            cats["noun"].append(w)
        if ps & 0x40:
            cats["verb"].append(w)
        if ps & 0x20:
            cats["adj"].append(w)
        if ps & 0x10:
            cats["dir"].append(w)
        if ps & 0x08:
            cats["prep"].append(w)
        if ps & 0x04:
            cats["buzz"].append(w)
    return cats


COMMON_NOUNS = ["lamp", "sword", "egg", "sack", "bottle", "window", "door", "rug",
                "troll", "thief", "case", "leaflet", "mailbox", "knife", "rope",
                "torch", "coffin", "boat", "pump", "bell", "book", "candles",
                "matches", "all", "it", "me", "house", "tree", "water", "garlic"]
COMMON_VERBS = ["take", "drop", "open", "close", "examine", "read", "put", "give",
                "attack", "throw", "turn on", "turn off", "move", "climb", "eat",
                "look at", "search", "push", "pull", "tie", "unlock", "light",
                "wave", "listen", "smell", "inventory", "look", "wait", "score",
                "diagnose", "pray", "jump", "enter", "exit", "go", "walk"]


def random_command(rng, v):
    r = rng.random()

    def noun():
        n = rng.choice(COMMON_NOUNS if rng.random() < 0.6 else v["noun"])
        if rng.random() < 0.15 and v["adj"]:
            n = rng.choice(v["adj"]) + " " + n
        return n

    if r < 0.22:
        return rng.choice(v["dir"])
    if r < 0.30:
        return rng.choice(COMMON_VERBS)
    if r < 0.62:
        verb = rng.choice(COMMON_VERBS if rng.random() < 0.7 else v["verb"])
        return f"{verb} {noun()}"
    if r < 0.75:
        verb = rng.choice(COMMON_VERBS if rng.random() < 0.7 else v["verb"])
        prep = rng.choice(["in", "on", "with", "to", "at", "from", "under"] if rng.random() < 0.7
                          else v["prep"])
        return f"{verb} {noun()} {prep} {noun()}"
    if r < 0.80:
        return rng.choice(["take all", "drop all", "take all but lamp", "put all in sack",
                           "take lamp and sword", "drop sword, lamp", "again", "g",
                           "oops lamp", "take lamp. drop it", "look. inventory",
                           "take it", "examine it"])
    if r < 0.85:
        return noun()  # answers orphaned questions
    if r < 0.90:
        return " ".join(rng.choice(v["noun"] + v["verb"] + v["buzz"])
                        for _ in range(rng.randint(1, 5)))
    if r < 0.93:
        return rng.choice(["frobnicate the widget", "xyzzy", "plugh", "hello",
                           "say hello", "zork", "", "   ", "\"hello\"", "troll, give me axe",
                           "echo", "ulysses", "odysseus", "temple", "treasure"])
    if r < 0.96:
        return f"{rng.choice(['set', 'turn', 'say', 'wait'])} {rng.randint(0, 2000)}"
    return rng.choice(v["verb"])


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--runs", type=int, default=20)
    ap.add_argument("--length", type=int, default=200)
    ap.add_argument("--seed", type=int, default=0)
    args = ap.parse_args()
    v = vocabulary()
    full = open(os.path.join(HERE, "..", "tests", "fullgame.txt")).read().splitlines()
    full = [c for c in full if c not in ("quit", "y")]
    failures = 0
    for run in range(args.runs):
        rng = random.Random(args.seed * 100003 + run)
        prefix = full[:rng.randint(0, len(full))]
        cmds = prefix + [random_command(rng, v) for _ in range(args.length)]
        # save/restore are interactive in the Python version (the reference
        # interpreter just fails them), so leave them out
        cmds = [c for c in cmds if not any(w.startswith(("save", "restor"))
                                           for w in c.split())]
        game_seed = rng.randint(1, 10 ** 6)
        a = difftest.run_original(cmds, game_seed)
        b = difftest.run_python(cmds, game_seed)
        if a == b:
            print(f"run {run}: OK ({len(cmds)} commands)")
            continue
        failures += 1
        print(f"run {run}: MISMATCH (game seed {game_seed})")
        faildir = os.path.join(HERE, "..", "fuzz-failures")
        os.makedirs(faildir, exist_ok=True)
        path = os.path.join(faildir, f"fail_{args.seed}_{run}_{game_seed}.txt")
        with open(path, "w") as f:
            f.write("\n".join(cmds) + "\n")
        diff = list(difflib.unified_diff(a.splitlines(), b.splitlines(), "original",
                                         "python", lineterm="", n=3))
        print("\n".join(diff[:40]))
        print(f"  commands saved to {path}")
    print(f"{args.runs - failures}/{args.runs} runs identical")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
