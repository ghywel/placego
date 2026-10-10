# Lemma B2 (the clock never stops)

*Windows, zero runs and the left band. Derived from [PROOFS.md](../PROOFS.md), entry "9. Lemma B2 (the clock never
stops)"; rebuild with `python3 proofs/build.py`. Edit the proof in PROOFS.md and this summary in
[summaries.md](summaries.md), never this file.*

**Status:** proved.

## In plain words

The diagonals near the edge each keep a steady beat, and going deeper the beats keep dropping by octaves, for ever.

**What it says.** Near the edge, each diagonal eventually settles into a steady repeating pattern. But the repeats
get longer as you go deeper, doubling again and again without end, so no single period fits them all. There are
infinitely many diagonals that go white for ever and infinitely many that go black for ever.

**Why it matters.** It proves a mechanism Rowland observed: the edge keeps producing fresh structure. Several
exclusions below need a black diagonal deeper than any given depth, and this supplies it. A doubling is itself a
regular pattern (the owner's point); what the lemma rules out is one common period. No finite run could confirm it
either: a period of 2^k ticks needs at least that long to show itself, so a measurement hears only the first few
octaves, and the proof carries the rest.

**An everyday picture.** Notes dropping an octave at a time, each one steady and each an octave below the last. A
scale that keeps going down soon leaves human hearing behind (about ten octaves cover all of it), but it never stops
being a scale (the owner's reading).

**Checked by machine.** A proof assistant (Lean) has checked it: the periods never stop growing, and there are infinitely many stripes that end white and infinitely many that end black.

## The formal statement and proof

*Where:* RULE30-PRIZE.md, "8.59 The window principle meets the band of stripes: a repeat is a white run, and the left side is never white for long (2026-10-05)". *Bears on:* the left band: the diagonal periods double without end (Rowland's mechanism, proved). *Status:* proved.

**Lemma B2 (the clock never stops).** The eventual periods of the diagonals are unbounded. So there are infinitely
many eventually white diagonals, and infinitely many eventually black ones.

*Proof.* Suppose every diagonal had eventual period dividing $P$. Write $V_k \in \{0,1\}^{\mathbb{Z}/P}$ for the
periodic regime of diagonal $k$, indexed by time modulo $P$, so that $V_k(s+1) = V_{k-2}(s) \oplus (V_{k-1}(s) \lor V_k(s))$
for every $k \ge 0$, with $V_{-1} = V_{-2} = 0$. The pairs $(V_{k-1}, V_k)$ take finitely many values, so
$(V_{k_1 - 1}, V_{k_1}) = (V_{k_2 - 1}, V_{k_2})$ for some $k_1 < k_2$. The recurrence can be read backwards,
$V_{k-2}(s) = V_k(s+1) \oplus (V_{k-1}(s) \lor V_k(s))$, so $V_{k_1 - j} = V_{k_2 - j}$ for every $j \ge 0$, and the
backward reading continues into the negative indices, where everything is 0. With $q = k_2 - k_1$ this gives
$V_0 = V_{-q} = 0$, against $V_0 \equiv 1$. So the periods are unbounded. A diagonal's period exceeds the periods
of the two before it only when the one before it is eventually white: otherwise a time with $D_{k-1}(t) = 1$ resets
$D_k(t+1) = \lnot D_{k-2}(t)$, after which $D_k$ follows its inputs' period. Infinitely many doublings need infinitely
many eventually white diagonals, and Lemma B1 turns each into an eventually black one. $\square$

*Machine-checked (Local, 2026-10-10 05:28 BST, L545).* tests/probes/lean/LemmaB2.lean, `lemma_B2`: no P >= 1 is an eventual
period of every diagonal. It covers the first sentence, that the periods are unbounded; the white/black corollary is
not formalised in that file; JenPow2.lean (L548) adds it: `infinitely_many_white` (for every N some diagonal k >= N
is eventually white) and `infinitely_many_black`, by `reset` (a black D_(k-1) makes D_k inherit its inputs' period)
and B1's white_then_black.
- The proof avoids the vectors over Z/P. Take one time after which diagonals 0 .. 4^P + 1 all have period P.
  Pigeonhole the windows (D_k, D_(k+1)) on [T, T + P); `ext_window` extends equal windows by periodicity.
- `D_back` reads the recurrence backwards, down to a negative diagonal against D_0.
- The axioms are propext, Classical.choice and Quot.sound. With JenPow2.lean the periods are powers of 2 without bound.
