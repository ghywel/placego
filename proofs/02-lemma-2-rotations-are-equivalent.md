# Lemma 2 (rotations are equivalent)

*The wall form. Derived from [PROOFS.md](../PROOFS.md), entry "2. Lemma 2 (rotations are equivalent)"; rebuild with
`python3 proofs/build.py`. Edit the proof in PROOFS.md and this summary in [summaries.md](summaries.md), never this
file.*

**Status:** proved.

## In plain words

Starting the rhythm one beat later is the same problem, so only one starting beat needs checking.

**What it says.** If a finite seed made the middle column blink black-white from the start, then one tick later it
is still finite and blinks white-black. So every shifted version of a repeating word stands or falls together.

**Why it matters.** It removes duplicate work: to rule out a rhythm, rule out one of its rotations.

**An everyday picture.** A song is the same song whether you start listening at the first bar or the second.

## The formal statement and proof

*Where:* RULE30-PRIZE.md, "7. Rung 2, first progress: left-side rigidity (2026-10-04)". *Bears on:* the wall form: one rotation of a periodic word per class suffices. *Status:* proved.

**Lemma 2 (rotations are equivalent).** A finite configuration whose column is exactly periodic from $t = 0$, with
word $w$, is still finite one step later, and its column is then periodic with $w$ rotated by one place. So a finite
configuration exists for one rotation of a cyclic word exactly when it exists for all of them, and ruling out one
rotation per class is enough. $\square$
