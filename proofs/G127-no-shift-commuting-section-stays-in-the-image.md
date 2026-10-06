# no shift-commuting section stays in the image; strict loss at one more layer

*GPT's proofs, second-read by Local. Derived from [PROOFS.md](../PROOFS.md), entry "G.GPT127. no shift-commuting
section stays in the image; strict loss at one more layer (second-read by Local, 2026-10-06)"; rebuild with `python3
proofs/build.py`. Edit the proof in PROOFS.md and this summary in [summaries.md](summaries.md), never this file.*

**Status:** proved by GPT and second-read by Local.

## In plain words

A predecessor inside the image may require a longer repeating pattern.

**What it says.** A period-two target has a period-four predecessor inside the image, but no period-two predecessor there. Therefore no predecessor choice that commutes with shifting can stay inside the image for every target.

**Why it matters.** Failure of a local inverse is not failure of every predecessor. A separate certificate shows genuine loss at the next layer: an allowed target forces a forbidden word in every predecessor. This establishes one strict image inclusion, not a rule for all deeper layers.

**An everyday picture.** A repeating request may need a response with a longer loop, even when a short local response exists outside the allowed set.

## The formal statement and proof

### G127. No shift-commuting predecessor section stays in the ternary image (2026-10-06)

**Status:** symbolic section obstruction and strict deeper-image loss; NS0/NS2 pass and NS1 prediction held. Uses G126's image theorem; independent review pending. The preregistered distinction between a section failure and strict loss is resolved by the separate certificate below. Further image layers remain open.

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

**NS0-NS2 outcome (2026-10-06 22:20 BST).** Executed after81fb4fd published the proof,predictions and instrument. NS0 PASS on all27 triple cases;NS2 PASS on the period-two section obstruction and period-four lift. NS1 HELD at n=6,so the blind witness-by7 prediction held. The search checked9,828 full-shift precursor blocks across n=1..6. The first missing periodic target prefix is022000. All six full-shift precursor blocks are

    22100000, 22100001, 22100002,
    22100022, 22100220, 22100221.

Each contains100. The independently decoded de Bruijn path count is also6. No floating arithmetic or sampling. Minimality is asserted only within the preregistered search of cyclically admissible target words through length6,not all possible global target classes.

**All-sequence obstruction,independently derived from binary constraints.** In any target starting02200d with d in{0,1}, C begins011000 and D begins00100 (the sixth D need not be used). The predecessor constraints force A(0)=1 because D(0)=0,C(1)=1. Compatibility at site0 forces A(1)=1,and compatibility at site1 then forces A(2)=0. The target equations at sites3 and4 force A(3)=A(4)=0. Encoding(C,A) forces precursor prefix22100,which contains100. This eliminates every global ternary predecessor lying in Y,periodic or not,without relying on enumerated boundary choices. Thus T(Y) forbids022000 and022001 in addition to Y's old exclusions.

The cyclic target(022000)^infinity belongs to Y: it consists of zero runs of length4 and two runs of length2,with no ones and no0202. Hence it has a full-shift predecessor by G126,but no predecessor from Y. Therefore T(Y) is a proper subset of Y,or equivalently T^2(full ternary shift) is strictly smaller than T(full ternary shift). G126's explicit predecessor section cannot establish stabilization,and now stabilization at this layer is refuted by a complete finite obstruction. This proves strict loss at one further layer,not strict loss at every depth or zero entropy of the limit set. Further iterated images and any wall-specific consequence remain open. Independent review pending.
