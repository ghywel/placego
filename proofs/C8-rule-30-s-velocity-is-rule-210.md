# Rule 30's velocity is Rule 210

*Short proofs restated from the running text. Derived from [PROOFS.md](../PROOFS.md), entry "C.8 Rule 30's velocity
is Rule 210 (RULE30-PRIZE.md §8.70; 2026-10-06)"; rebuild with `python3 proofs/build.py`. Edit the proof in
PROOFS.md and this summary in [summaries.md](summaries.md), never this file.*

**Status:** proved.

## In plain words

Rule 30's change from one tick to the next follows Rule 210, its closest sibling.

**What it says.** Look not at each square but at whether it changed colour between two ticks. That pattern of
changes obeys Rule 210 exactly: Rule 30 equals "keep the old colour, then flip it wherever Rule 210 says so". The
proof is two lines of algebra.

**Why it matters.** It explains why Rule 210 keeps turning up as Rule 30's nearest relative in the record, and it
lets the prize be written as a difference equation in the arithmetic of bits, where 1 + 1 = 0.

**An everyday picture.** Video compression: instead of storing every frame whole, a video file mostly stores what
changed since the frame before, and here those changes follow a simpler rule than the pictures themselves.

## The formal statement and proof

*Where:* §8.70 (the owner's question about velocity and acceleration). *Bears on:* why Rule 210 is Rule 30's closest
sibling; the prize as a difference equation over GF(2). *Status:* proved.

**Proposition.** $x_{t+1}(i) \oplus x_t(i) = x_t(i-1) \oplus (\lnot x_t(i) \wedge x_t(i+1))$ for Rule 30, i.e. Rule 30 $= c \oplus$ Rule 210.

*Proof.* $l \oplus (c \vee r) = l \oplus c \oplus r \oplus cr$, and $l \oplus r \oplus cr = l \oplus (\lnot c \wedge r)$. $\square$
