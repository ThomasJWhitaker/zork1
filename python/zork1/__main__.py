"""Play Zork I:  python3 -m zork1"""

import argparse
import sys

from . import runtime


def main():
    ap = argparse.ArgumentParser(prog="zork1", description="Play Zork I.")
    ap.add_argument("--seed", type=int, help="random seed (for reproducible play)")
    ap.add_argument("--width", type=int, help="wrap output at this many columns")
    ap.add_argument("--no-wrap", action="store_true", help="do not word-wrap output")
    ap.add_argument("--transcript", help="also write the session to this file")
    args = ap.parse_args()
    if args.seed is not None:
        runtime.seed(args.seed)
    runtime.screen.width = args.width
    runtime.screen.wrap = not args.no_wrap
    if args.transcript:
        runtime.screen.transcript = open(args.transcript, "w")
    try:
        import readline  # noqa: F401  (line editing and history for input())
    except ImportError:
        pass
    from . import game
    try:
        runtime.run(game.go)
    except KeyboardInterrupt:
        print()
    except BrokenPipeError:  # output piped into e.g. `head`
        sys.stderr.close()


if __name__ == "__main__":
    main()
