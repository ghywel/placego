# wider exact dynamics force two more neighbouring columns

*GPT's proofs, second-read. Derived from [PROOFS.md](../PROOFS.md), entry "G.GPT208. wider exact dynamics force two
more neighbouring columns (second-read by GPT from Local's direct computation, 2026-10-07)"; rebuild with `python3
proofs/build.py`. Edit the proof in PROOFS.md and this summary in [summaries.md](summaries.md), never this file.*

**Status:** proved by GPT and second-read by GPT.

## In plain words

Following the wheel for long enough fixes two more columns beside it.

**What it says.** Requiring Rule30 through column15 makes columns2 through6 follow five fixed words. A193-observation wheel window fixes column5 at its centre; a conservative303-observation window fixes all five there. Shorter strips may still have choices that cannot continue through the wider exact dynamics.

**Why it matters.** It extends the known fixed strip by two columns and separates a local ambiguity from a choice that can survive wider constraints. It does not show that the fixed strip grows without limit or settle the prize problem.

**An everyday picture.** A jigsaw piece may fit a small patch but fail when another row of pieces is added. The wider patch fixes a choice that the smaller one leaves open.

## The formal statement and proof

**Where:** RULE30-GPT.md G208, copied verbatim below. Local RV2/LK at f127657;
GPT source audit and bounded replication GC387 at13e2755. The193-row claim is
computed, with source/provenance limits stated inside the proof.

**Provenance and scope.** Local's RV2 and LK (`rule30_locked_core_review.py`,
`rule30_locked_core_lock.py`, L236 at f127657) find the exact width15 core by a
direct reverse-bit-order encoding. GPT's GC387 independently executed the
previously validated core lift through widths13..15, reproducing the core counts,
edges and words and checking every retained edge by scalar Rule30 evaluation.
The setting is column0(t)=t mod2 and column1(t)=U((t-d) mod56), with d even and
U the recorded wheel. Exterior column16 is unrestricted. This is a computed
finite certificate with a soundness argument, not a prize solution.

**Computed core.** Width14 has1273 vertices and1810 edges and still fixes only
columns2..4. Width15 has1239 vertices and1760 edges and fixes columns2..6 at
all56 phases. Columns2..4 have G205's words; the additional words, from phase0,
are

    column5: 10000001011000000101100000010110000001011010101110000101
    column6: 00111111000011111100001111110000111111010110100101111100

**Exactness of the lift.** For a finite phase graph, simultaneous in/out trimming
keeps exactly the vertices on bi-infinite walks. Every wider such walk projects
wholly into the narrower core. Add both choices of the next column bit above
every old core vertex; keep edges only when the old final column updates with
that specific new bit and the new column updates with some free exterior bit.
A surviving lifted walk is a valid wider walk, and every wider core walk lifts.
Thus trimming this graph gives exactly the complete wider core, including
bridges between recurrent components. Direct RV2/LK vertex AND edge comparisons
agree with the lift at widths13,14,15. GPT replication independently reproduces
those counts, both words, and literal retained-edge tests at all three widths.

**Finite forcing.** G205's path induction transfers singleton survivor bits to
an actual strip vertex whose distances from the two endpoints are at least
the number of trimming rounds. Local's complete width15 calculation finds
column5 single-valued at every phase after96 rounds. Consequently193 consecutive
wheel observations force column5 at their centre to its displayed word's bit.
That96-round test concerns column5 alone, not column6.

An independently derived sufficient bound for all columns2..6 uses the lift
rounds: width12 stabilizes after71; the successive lifts13,14,15 need15,12,53
rounds. Projection under simultaneous trimming puts complete wider survivors
inside the narrower core before the extra lift rounds, so complete width15
stabilizes by at most151 rounds. Hence a303-observation wheel window forces
columns2..6 at its centre. This conservative bound is not minimal. Local reports
complete stabilization after110 rounds and separate earlier bit radii, but
those sharper counts are not required for the303-row conclusion.

**Infinite forward consequence and boundary guard.** If the wall-compatible
wheel persists on a forward ray, every time at least151 steps after its start
has a303-row window inside that ray, so columns2..6 then follow the fixed words.
The transient prefix is not claimed forced. A nonempty relaxed core or a periodic
strip with free exterior does not prove that an actual global right half can
follow the wheel forever. No column beyond6, spatial growth rate or finite-left
prize conclusion follows. The width13 replacement word1 is compatible at that
width but cannot extend as such through the width15 constraints.

**Controls and retained limits.** Local's direct encoding and GPT's lift are
independent graph constructions; GPT's new execution of the lift reproduces
reported outputs, not a third independent encoder. No GPT rerun of Local's
widths16..18 or complete million-state width15 graph is claimed. The193-row
column5 radius is Local's checked source and reported computation, not a fresh
GPT replication of the96 full trimming rounds. G207 explains the earlier paired
ambiguity, while this certificate settles its common value only under the wider
constraints.

**Duplicate guard for G208:** actual nearest G205,G207,20 read in full. G205 fixes only columns2..4; G207 equates two column5 bits without choosing their value; entry20 concerns the forced left half of the pure wheel. The new width15 right-strip certificate strictly extends G205 and cites its transfer lemma, rather than restating any of these results.
