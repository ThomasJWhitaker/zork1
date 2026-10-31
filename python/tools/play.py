#!/usr/bin/env python3
"""Run a command script through the Python translation and print the transcript.

    python3 python/tools/play.py commands.txt [--seed N] [--tail K]
"""
import argparse
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import difftest  # noqa: E402

ap = argparse.ArgumentParser()
ap.add_argument("commands")
ap.add_argument("--seed", type=int, default=1)
ap.add_argument("--tail", type=int, default=0, help="only show the last K commands")
a = ap.parse_args()
cmds = [c for c in open(a.commands).read().splitlines() if not c.startswith("#")]
out = difftest.run_python(cmds, a.seed)
if a.tail:
    parts = out.split("\n>")
    out = "\n>".join(parts[-a.tail - 1:])
print(out)
