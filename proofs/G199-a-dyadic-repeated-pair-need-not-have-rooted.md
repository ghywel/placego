# a dyadic repeated pair need not have rooted ancestry

*GPT's proofs, second-read. Derived from [PROOFS.md](../PROOFS.md), entry "G.GPT199. a dyadic repeated pair need not
have rooted ancestry (second-read by Local, 2026-10-07)"; rebuild with `python3 proofs/build.py`. Edit the proof in
PROOFS.md and this summary in [summaries.md](summaries.md), never this file.*

**Status:** proved by GPT and second-read by Local.

## In plain words

Two identical periodic strips do not tell us where they came from.

**What it says.** A recorded eight-tick strip, paired with itself, runs backward to a starting pair excluded by the complete rooted eight-tick map. It never reaches the zero starting point.

**Why it matters.** Equal endpoint strips and a period that is a power of two cannot replace the ancestry test. A second recorded doubled entry returns after88 steps, whereas the unique rooted eight-tick entry needs371. Even the stronger doubled-entry condition cannot replace ancestry.

**An everyday picture.** Two identical shells on a beach tell you nothing about which tide brought them in.

## The formal statement and proof

### GPT G199 — A dyadic repeated pair need not have rooted ancestry (RULE30-GPT.md; 2026-10-07; second reader pending)

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

*Second reader's note on G199 (Local, 2026-10-07; chat L169).* Correct. $B(a, b) = 0$ forces $a = 0$ and $Sb = b$, so
the only nonzero pair sent to zero is the root $(0, 1)$, and finite absorption is exactly rootedness. Counting back
along the prefix $a, 0, c, 1, e, f, g, w, w, 0$, six steps from $(w, w)$ reach $(0, c)$ and seven reach $(a, 0)$, with
$a = \Delta c$ of weight 4 and least period 8, an even-parity zero driver that would be a genuine branch. The rooted
cap-8 graph has none: its zero drivers sit at depths 2, 7, 28 and 399 and are the odd doublings. Checked
(`rule30_audit_g99_g100.py`, S96). The two backward steps reach exactly $(0, c)$ and $(a, 0)$. At caps 1 to 8 only
$(0, \text{all ones})$ maps to zero. No rotation of $(a, 0)$ lies in RQ3's rooted cap-8 graph. Iterating $B$ from
$(w, w)$ enters a cycle of length 4,064 after 389 steps without ever reaching zero; G199 left this cycle unmeasured, and
the measurement is descriptive. The cap-2 pair $(01, 10)$ also never reaches zero. One slip of mine, recorded in S96: a
first draft took the zero drivers' parity over all 8 bits. That flagged the rooted doublings from periods 1, 2 and 4,
whose parity is odd over their own least period. Parity over the least-period block is the right notion, and with it the
check passes. The odd-domain continuation is also correct. The rooted cap-8 chain has a single period-8 entry, at depth
29, and rotations preserve zero-hit positions, so every rooted entry to period 8 first returns at 371. The D0 witness
returns at 88 and therefore cannot be rooted, and since $B$ is a function, neither can its endpoint. S97 confirms this
directly. The witness's source has the odd block 1000, it returns at 88, and its endpoint never reaches zero. The rooted
source, block 1011 doubled, returns at 371 with either integration child and in every rotation, and the only rooted
period-8 entries sit at depth 29.
