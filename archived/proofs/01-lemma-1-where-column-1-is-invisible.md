# Lemma 1 (where column 1 is invisible)

*The wall form. Derived from [PROOFS.md](../PROOFS.md), entry "1. Lemma 1 (where column 1 is invisible)"; rebuild
with `python3 proofs/build.py`. Edit the proof in PROOFS.md and this summary in [summaries.md](summaries.md), never
this file.*

**Status:** proved.

## In plain words

When the middle square is black, the right side cannot be heard on the left at all.

**What it says.** Each step, the left half reads the middle column and column 1. But whenever the middle square is
black, the rule's "or" is already satisfied, so whatever column 1 says is ignored. Column 1 only gets a word in at
the white beats.

**Why it matters.** It halves the channel. With the wall blinking black and white, the right side can influence the
left only every other tick. Every later count of "how much information gets through" starts here.

**An everyday picture.** A door with a buzzer: when the door is already open (black), pressing the buzzer changes
nothing. The buzzer has no memory: at the next white beat, column 1 is heard again. The version with a memory is
proof 03's latch.

## The formal statement and proof

*Where:* RULE30-PRIZE.md, "7. Rung 2, first progress: left-side rigidity (2026-10-04)". *Bears on:* the wall form: column 1 is visible only at white times; every statement about injection rates rests on it. *Status:* proved.

**Lemma 1 (where column 1 is invisible).** With column 0's trace $\tau$ fixed, the forced left half depends on column
1 only at the times $t$ with $\tau(t) = 0$.

*Proof.* The only place column 1 enters is
$x_t(-1) = \tau(t+1) + \big(\tau(t) \vee x_t(1)\big) \bmod 2$. Where $\tau(t) = 1$, the "or" is 1 whatever $x_t(1)$
is. Every further left column is built from columns $-1$ and $0$ and those to their left. $\square$
