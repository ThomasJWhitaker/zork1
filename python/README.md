# Zork I in Python

A complete, playable Python translation of the Zork I ZIL source in this
repository.  Every routine, object, room, vocabulary word and syntax rule
comes from the original `.zil` files.  The game behaves exactly like the
original compiled story file: on scripted and randomly generated play, the
Python version produces the same transcript as `COMPILED/zork1.z3`
character for character.

## Playing

Requires Python 3.8 or later.  There are no dependencies.

```sh
cd python
python3 -m zork1
```

Options:

| option | meaning |
| --- | --- |
| `--seed N` | fixed random seed (reproducible combat, thief, etc.) |
| `--width N` | wrap text at N columns (default: terminal width) |
| `--no-wrap` | don't word-wrap output |
| `--transcript FILE` | also write the session to FILE |

`SAVE` and `RESTORE` ask for a file name (default `zork1.sav`).  `RESTART`,
`QUIT`, `SCORE`, `VERSION` and the other meta-commands work as in the
original.

## Layout

```
python/
  zork1/
    game.py       the translated game (generated, ~12k lines)
    runtime.py    Z-machine services: memory, objects, text, I/O, save/restore
    __main__.py   command-line entry point
  tools/
    zil2py.py     the ZIL -> Python translator
    zilreader.py  reader for ZIL/MDL source syntax
    zmachine.py   small Z-machine v3 interpreter, used as a test oracle
    difftest.py   compare the original and the translation on a command script
    fuzz.py       random-command differential fuzzer
  tests/          command scripts and the transcript test suite
```

`game.py` is generated.  To regenerate it after changing the translator or
the ZIL source:

```sh
python3 python/tools/zil2py.py
```

## How the translation works

The ZIL code is translated routine by routine into Python functions with
the same names (`V-WALK` becomes `v_walk`, `ACCESSIBLE?` becomes
`accessible_p`).  ZIL globals, constants, objects and flags become
module-level names (`HERE`, `P_ITBL`, `WEST_OF_HOUSE`, `TAKEBIT`).  Control
flow (`COND`, `REPEAT`, `RETURN`, `AGAIN`) maps onto `if`/`while`/`return`.
Where ZIL uses a statement as an expression, the translator introduces a
temporary.

The parser and many game routines do pointer arithmetic on tables.  They
walk the lexical buffer, read vocabulary entries byte by byte, and patch
property tables.  So the data stays in the Z-machine format:
`runtime.py` builds a byte-addressed memory image containing the
vocabulary, the object property tables and every `TABLE`/`LTABLE`/`ITABLE`,
laid out the way the Z-machine expects.  The translated code uses
`z.get`/`z.put`/`z.getb`/`z.putb` on it just as the ZIL did.  That lets the
original parser run unmodified.

A few details of Infocom's own compiler (ZILCH) had to be reproduced to
match the original game's behaviour:

* `<RETURN value>` inside a `REPEAT` returns from the whole routine.  Only
  a bare `<RETURN>` leaves the loop.  This matters in the combat code.
* A COND clause with no body, such as `(T)`, has the value of its test.
* In strings, line breaks become spaces, `|` is a newline, and two spaces
  after a full stop are folded into one.
* Children of an object are linked in reverse definition order.  Syntax
  entries for a verb are stored in reverse order, and verbs get the last
  part-of-speech slot in a vocabulary entry.  Unspecified syntax search
  bits are 0, and noun words carry the value 1.
* On some odd input the parser reads header word 0 as a vocabulary
  pointer.  Tables therefore start at address `0x400`, so that read finds
  zeros, as it does in the original.

## Testing

The test oracle is `tools/zmachine.py`, a small Z-machine interpreter that
runs the original `COMPILED/zork1.z3`.  Both programs get the same commands
and the same random-number stream, and their transcripts must match
exactly:

```sh
python3 python/tests/test_transcripts.py          # or: pytest python/tests
python3 python/tools/difftest.py python/tests/fullgame.txt
python3 python/tools/fuzz.py --runs 100 --length 300 --seed 7
```

The fuzzer builds commands from the game's real vocabulary: movement,
verbs with objects and prepositions, `ALL`/`BUT`, `AGAIN`, `OOPS`, `IT`,
answers to "What do you want to ...?" questions, numbers, quoted text and
nonsense.  It starts each run from a random point along a walkthrough, so
play reaches the dungeon, combat, the thief, and so on.

Known differences from the original story file:

* `SWIM` (also `BATHE`, `WADE`) with no object prints the name of object 0.
  In the original that is garbage memory (`"   xufpIt's pds"`); here it
  is empty.
* `PLAY` with an actor (`play troll`) kills you with an empty message.
  In the original, the compiler gave that empty string the address of the
  next string in the story file, so it prints " has no effect.".
* `SAVE`/`RESTORE` ask for a file name and use their own file format, not
  Quetzal.
* There is no status line.
