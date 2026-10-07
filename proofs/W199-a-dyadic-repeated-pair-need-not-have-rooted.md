# A dyadic repeated pair need not have rooted ancestry

*The waiting room (not yet verified). Derived from [PROOFS.md](../PROOFS.md), entry "GPT G199 — A dyadic repeated
pair need not have rooted ancestry (RULE30-GPT.md; 2026-10-07; second reader pending)"; rebuild with `python3
proofs/build.py`. Edit the proof in PROOFS.md and this summary in [summaries.md](summaries.md), never this file.*

**Status:** in the waiting room: stated with a proof, not yet checked by a second reader.

## In plain words

Two identical periodic strips do not tell us where they came from.

**What it says.** A recorded eight-tick strip, paired with itself, runs backward to a starting pair excluded by the complete rooted eight-tick map. It never reaches the zero starting point.

**Why it matters.** Equal endpoint strips and a period that is a power of two cannot replace the ancestry test. A second recorded doubled entry returns after88 steps, whereas the unique rooted eight-tick entry needs371. Even the stronger doubled-entry condition cannot replace ancestry.

**An everyday picture.** Two copies of the same photograph can show where a journey ended without telling us where it began.

## The formal statement and proof

**Question, control and counterfactual.** A possible way to simplify the rooted distance problem was to treat every dyadic repeated pair(w,w) as lying in the backward zero basin. That would erase the ancestry test at a return endpoint. Check it against G189's already verified balanced cap8 return, rather than launch a basin census. The counterfactual is that dyadic period plus equal endpoint profiles suffices for rootedness. It fails; the inference below uses the completed rooted cap8 certificate, not a new run.

Recall B(a,b)=(S b XOR(a OR b),a). For any nonzero pair whose iterates first reach(0,0), its last nonzero predecessor must be(0,1): B(a,b)=0 forces a=0 and S b=b, so b is constant; the nonzero choice is1. Thus finite absorption is equivalent to membership in the rooted tree. This observation does not assert absorption for arbitrary pairs.

Use temporal words w=10100100, c=10010011 and a=10110100 from the verified G189/S83 prefix

    a, 0, c, 1, e, f, g, w, w, 0.

All displayed profiles are cap8 words. Counting the seven backward pair steps in that prefix gives B^6(w,w)=(0,c) and B^7(w,w)=(a,0). Directly Delta c=a. The word a has four black bits and least period8: its halves1011 and0100 differ. Hence(a,0) would be a genuine even-parity zero-driver branch node of least period8 if it were rooted. The complete cap8 rooted certificate, recorded under Local L115 and G161, excludes every such node. It follows that(a,0) and consequently(w,w) never reach zero under B. A finite eventual nonzero cycle follows from the finite cap8 state space, but no cycle length or trajectory was computed here.

**Identified unexpected scope check.** The previous cap2 nonabsorbing example(01,10) had unequal coordinates, so it did not refute this repeated-pair shortcut. This cap8 example has equal coordinates AND primitive dyadic period. It is still not a period-doubling return: its integration source has even parity and full period8, as G189 already records. Therefore it blocks erasing rooted ancestry but does not refute G190's odd-doubling reconstruction or establish a nonrooted witness inside that stronger domain.

**Failure retained and next obligation.** Dyadic repeated endpoints alone cannot recover the missing rooted predecessor history. No new growth estimate or status-board change. Local: check the six/seven-step indexing and the transfer from the existing all-cap8 no-genuine-branch certificate; no basin computation requested. The next rooted distance argument must retain actual ancestry, not silently infer it from the endpoint's period or equality.


**G199 continuation: ancestry is also missing inside the odd-doubling domain (2026-10-07; second reader pending).** The fixed S84/D0 witness has source with four-bit block1000 (odd parity), target period8, word w=00111101, and first return88. Thus it satisfies G190's stronger odd-doubling condition, unlike the balance control above. It still cannot be rooted.

By the complete cap8 certificate and G158, the rooted temporal-rotation quotient has no genuine branch and is a single chain. Its sole period8 entry orbit occurs at depth29; the preceding zero is at28 and its next zero at399, so its first-return distance is371. The complementary integration choices are shifts through4, and all temporal rotations preserve zero-hit positions and therefore this first-return distance. There is no later odd-doubling entry from period4 on a rooted history: periods do not decrease, and the unique cap4 quotient chain ends at that doubling. Consequently every rooted odd-doubling entry to period8 has first return371. The verified first return88 is incompatible with that rooted orbit. Its source(a,0), entry(0,c), and repeated endpoint(w,w) are outside the backward zero basin. If the endpoint were absorbing, its uniquely reconstructed preceding source would be absorbing and hence rooted, giving the contradiction just established.

This uses the completed finite root certificate, the reviewed rotation-quotient classification and D0's exact first-return witness. No unpreregistered minimum or new trajectory run is used. It specifically refutes replacing rooted ancestry by odd source parity plus complementary halves. It does not classify other return-88 components or bound large-period rooted return lengths. Local: include the unique-entry and rotation-invariant first-return argument in the same G199 second reading; no computation requested.
