# three clock beats kill later odd column1 gates

*GPT's proofs, second-read. Derived from [PROOFS.md](../PROOFS.md), entry "G.GPT230. three clock beats kill later
odd column1 gates (second-read by Local, 2026-10-08)"; rebuild with `python3 proofs/build.py`. Edit the proof in
PROOFS.md and this summary in [summaries.md](summaries.md), never this file.*

**Status:** proved by GPT and second-read by Local.

## In plain words

A third clock beat shuts every later odd-time gate in the first column.

**What it says.** Under the alternating wall, an even-time black bit in column2 requires its neighbouring bit in column1 to be black. The next white wall beat therefore makes column1 white. Earlier results handle the initial exceptions for the empty-left family.

**Why it matters.** Candidate gate times from weaker local checks never actually activate later. This removes column3 from the selected source sum, while farther columns remain unresolved.

**An everyday picture.** A gate can be open at one stage, but the next interlock always closes it before the scheduled departure. Checking the whole short sequence removes possibilities that one stage alone allowed.

## The formal statement and proof

**Where:** RULE30-GPT.md GC456 atddd1e71; Local L268 in8f56dfd verifies the general odd-bit cutoff, all initial exceptions and the column-source composition. Source statement and proof copied verbatim below. G228 supplies the individual-bit implication; G226,G229 and G26 supply the source/time boundaries.

**Proof of the odd-bit cutoff.** Set S=x_(2n+2)(1) and B=x_(2n+2)(2). G228 proves B=1 implies S=1 from the wall values0,1 at times2n,2n+1; this implication holds for every compatible left row. At the next white wall beat, Rule210 gives

`x_(2n+3)(1)=(1-S)*B=0`.

If B=0 the expression is0, and if B=1 then S=1. Thus every odd column1 bit from time3 onward is0, independently of the effective stream or farther right bits. Only the three imposed wall values0,1,0 were used. The first odd bit at time1 has no preceding two-step obligation and is not covered by this argument.

**Column3 consequence.** G226's contrapositive gives V_t(3)=1 at t>=2 only if x_(t-2)(1)=1. At odd t>=5 this predecessor is an odd column1 bit at least3, now forbidden. For the empty initial left row, G26 gives x_0(1)=1, so x_1(1)=(1-x_0(1))*x_0(2)=0; this also removes the source at t=3. G229 proves V_1(3)=0 in every empty-left full0101 orbit. Therefore every odd-time column3 source is0 in that family. Even-time column3 sources are invisible at odd centre targets by G215's parity condition. Its complete contribution to every odd centre sample is0. G227's proposed late terms remain a true timetable, but actual three-beat predecessor obligations remove them all.

Combining this with G216,G226,G228, at target T=2^K+1 with K>=3 every selected source site i<=4 contributes0 for the empty-left full0101 family. If the initial global row is finite with support[-R,R] and 2^K>R+1, the homogeneous term is0 and an odd number of selected active sources must lie at i>=5. This now applies to odd as well as even K. The cone still grows and these farther sources are uncontrolled; no finite-witness exclusion follows.

**Duplicate guard for G230:** actual nearest G228,G227,G226 read in full. G228 supplies B=1 implies S=1 but does not compose the next white beat; G227 retains potential late column3 gates; G226 supplies their predecessor condition. This entry proves those later odd gates never fire and removes the remaining column3 sources with the stated initial hypotheses.

**Scope:** the odd-bit cutoff applies to every full0101 orbit from time3 onward. Empty-left hypotheses are needed for removing the initial column3 exceptions. The required source boundary i>=5 still grows into an uncontrolled cone; no full-right uniqueness or finite-seed exclusion follows.
