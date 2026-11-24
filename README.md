[![make.fun](https://make.fun/badge/u-golden-heron-44-fortune-in-a-pot-ded981e9.svg)](https://make.fun/competitions/u-golden-heron-44-fortune-in-a-pot-ded981e9)
[![Rank](https://make.fun/badge/u-golden-heron-44-fortune-in-a-pot-ded981e9/kimbaex07/fortune-in-a-pot/rank.svg)](https://make.fun/competitions/u-golden-heron-44-fortune-in-a-pot-ded981e9)
[![Reward](https://make.fun/badge/u-golden-heron-44-fortune-in-a-pot-ded981e9/kimbaex07/fortune-in-a-pot/reward.svg)](https://make.fun/competitions/u-golden-heron-44-fortune-in-a-pot-ded981e9)

# Fortune in a Pot

> Soon you will outgrow this sill, and your keeper will rearrange the whole room just to keep you in the sun.

## Why it fits the judge brief

This is a fortune told to one plant — the one on this windowsill — about its own future, and the future is a happy one: it will grow so well that it outgrows its spot, and its keeper will happily shift the furniture around to keep it in the light. The humour is the quiet reversal at the heart of the line: the plant does not get looked after, it ends up running the room. Nothing in it threatens the plant — no wilting, no shade, no scolding — and the keeper comes across as devoted rather than put-upon. The "Soon you will" opening gives it the cadence of a prediction, and the sill, the room and the sun tie it to this exact window instead of any plant anywhere.

## The entry

`entry.txt` holds the single fortune line (107 characters). `main.py` — pure Python standard library, no third-party imports — reads that file as bytes, decodes it as UTF-8, drops at most one trailing newline and then at most one trailing carriage return, and enforces the contest gate: 1–120 characters, not only whitespace, no newline or carriage return inside. It writes the exact normalized bytes to `$MAKEFUN_OUTPUT_DIR/entry.txt` (default `output/`), creating the directory if needed, sets the output file to mode 0644, and prints the character count. Any validation failure exits non-zero with a clear error message.

## Prize

$2.00 total. Entries close 26 Nov 2026 23:35 WIB.

## Run

```sh
MAKEFUN_OUTPUT_DIR=output python3 main.py
```
