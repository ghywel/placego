# No shift-commuting predecessor section stays in the ternary image

*The waiting room (not yet verified). Derived from [PROOFS.md](../PROOFS.md), entry "G127. No shift-commuting
predecessor section stays in the ternary image (2026-10-06)"; rebuild with `python3 proofs/build.py`. Edit the proof
in PROOFS.md and this summary in [summaries.md](summaries.md), never this file.*

**Status:** in the waiting room: stated with a proof, not yet checked by a second reader.

## In plain words

A predecessor inside the image may require a longer repeating pattern.

**What it says.** A period-two target has a period-four predecessor inside the image, but no period-two predecessor there. Therefore no predecessor choice that commutes with shifting can stay inside the image for every target.

**Why it matters.** Failure of a local inverse is not failure of every predecessor. A separate bounded search will seek a finite obstruction to having any image-constrained predecessor, while keeping that distinction explicit.

**An everyday picture.** A repeating request may need a response with a longer loop, even when a short local response exists outside the allowed set.

## The formal statement and proof

**Status:** symbolic section obstruction; NS0-NS2 preregistered NOT RUN. Uses G126's proposed exact image Y. A section failure does not prove T(Y) is smaller than Y; deeper-image stabilization remains open.

For the ternary sideways map T, let Y be the sequences avoiding100,101,112,0210,0211,0202. The period-two points of Y are exactly the repeating words00,11,12,21,22. Literal evaluation of G22's rule gives

    00 -> 00,
    11 -> 22,
    22 -> 11,
    12 -> 22,
    21 -> 22.

Thus the target(12)^infinity belongs to Y but has no period-two predecessor in Y. Any shift-commuting section Q:Y->Y of T would preserve being fixed by the two-step shift. Its value at this target would be such a predecessor, a contradiction. There is no shift-commuting section into Y, regardless of continuity; in particular there is no local one. G126's section into the full ternary shift is unaffected.

**Unexpected guard: a deeper predecessor nevertheless exists.** The repeating word0102 lies in Y and T(0102)=1212. It is a period-four predecessor of the period-two target. G126's canonical section instead returns(01)^infinity, outside Y. Hence failure of the canonical choice, and even failure of every period-preserving section, cannot establish absence of all image-constrained predecessors. These statements separate a constructive local inverse from mere onto-ness.

**NS0-NS2 preregistration.** A bounded search will address a different implication:does some target in Y have a finite prefix with no possible predecessor from Y? NS0 compares all27 radius-two ternary cases with an independent binary-pair decoding. NS2 checks the five period-two targets, the period-four lift0102, and the canonical-section failure;this is the identified unexpected check.

NS1 considers prefix lengths n=1..7, in increasing order. Enumerate all3^(n+2) full-shift precursor blocks, compute their length-n outputs, and retain as possible Y precursors every block avoiding the six forbidden words internally. This is a superset of globally admissible precursor blocks, so a missing output certifies impossibility for nonperiodic predecessors too. Restrict target witnesses to words w whose cyclic repetition lies in Y, to certify target extendability. Stop at the first length and lexicographically first missing target prefix. Blind prediction:a witness occurs by length7. If none occurs, record that prediction as refuted;do not infer stabilization.

For a witness, retain the complete set of its full-shift precursor blocks in memory and the spectrum of forbidden factors excluding them. Independently count every full-shift precursor via a de Bruijn-pair dynamic program using the binary-decoded rule, and require exact agreement with the enumerated count. No sampling or floating arithmetic. A full blocked-prefix certificate would prove T(Y) is a proper subset of Y;the absence of a short certificate would be finite evidence only. Counterfactual:the period-two failure alone proves strict deeper-image loss;NS2 must refute it. Publish the predictions and instrument before execution. This small structural certificate search duplicates no ring census or Local computational job.
