# G18.3. Uniform protected-band theorem, even without a white prefix

*Theorems proved by GPT. Derived from [PROOFS.md](../PROOFS.md), entry "E.5. G18.3. Uniform protected-band theorem,
even without a white prefix"; rebuild with `python3 proofs/build.py`. Edit the proof in PROOFS.md and this summary
in [summaries.md](summaries.md), never this file.*

**Status:** proved by GPT (statement in PROOFS.md; the proof is copied below from RULE30-GPT.md).

## In plain words

A long enough black stretch wipes the slate: the left half becomes a known checkerboard whatever came before.

**What it says.** If the wall is black for b ticks, after any a ticks before, and b is at least 3a + 1, then the
left half at the start is a checkerboard from depth 4a to depth a + b − 1, whatever column 1 does before, during or
after.

**Why it matters.** It gives a protected band where the right side cannot reach, with no assumptions about the right
side at all.

**An everyday picture.** Fresh snow covering every track: after a long enough fall, you cannot tell who walked there
before.

## The formal statement and proof

*Where:* RULE30-GPT.md, "G18.3. Uniform protected-band theorem, even without a white prefix". *Status:* proved by GPT (proof there); its finite controls replicated by Local from the committed `rule30_gpt_slow_switch.py`, 2026-10-06 at edce038.

**Theorem.** Suppose a black wall run occupies times a..a+b-1, preceded by any a
wall bits and followed by anything. If a>=1 and b>=3a+1, row0 is checkerboard
on depths4a..a+b-1: even depths are1 and odd depths0. The right column before,
during and after the run is arbitrary. In particular this holds for slow walls,
without needing the monotone latch hypothesis.

## The proof, copied from RULE30-GPT.md

*Verbatim from [RULE30-GPT.md](../RULE30-GPT.md), the section named above; the master PROOFS.md holds the statement only.*

**Theorem.** Suppose a black wall run occupies times a..a+b-1, preceded by any a
wall bits and followed by anything. If a>=1 and b>=3a+1, row0 is checkerboard
on depths4a..a+b-1: even depths are1 and odd depths0. The right column before,
during and after the run is arbitrary. In particular this holds for slow walls,
without needing the monotone latch hypothesis.

**Proof.** At time a the checkerboard is known on depths1..b-1. One backwards
step reads its driver010 at depths1,2,3. For any preceding inverse-pair state,
these three drivers force x4=1; since x4=1 masks x3 in the next OR, every later
known driver determines the next cell independently of x3. Thus the earlier row
has the checkerboard on depths4..b. This needs b>=4.

Inductively after s>=1 steps backwards the known band is
[4s,b-1+s], with the same even-black phase. For one more step use the driver010
at4s+1..4s+3. It forces x(4s+4)=1 independently of all earlier inverse state;
subsequent alternating drivers propagate the phase through depth b+s.
The reset fits when b-1+s>=4s+3, equivalently b>=3(s+1)+1.
For all s<a this follows from b>=3a+1. The final band is [4a,a+b-1].
The inverse update within the row does not depend on the earlier wall bit once
its starting pair is given; the reset handles every pair. That proves the
nonperiodic-prefix version too. The band loses three cells of length per backwards
step, the same protected-window accounting as G13.5.

**Finite-support consequence.** At a slow wall's first white phase, b>=3a+1
forces a black cell at depth2*floor((a+b-1)/2). Hence a finite seed realizing
that trace cannot have a smaller left support radius. This extends G11's a=1
bound. It remains a finite-support exclusion for a specified window; it does not
exclude arbitrary radii or every repeated slow wall.
