# Four consecutive zeros recover the missing depth-thirteen anchor

*The waiting room (not yet verified). Derived from [PROOFS.md](../PROOFS.md), entry "G242. Four consecutive zeros
recover the missing depth-thirteen anchor (GPT, 2026-10-08; waiting room, GC549.35)"; rebuild with `python3
proofs/build.py`. Edit the proof in PROOFS.md and this summary in [summaries.md](summaries.md), never this file.*

**Status:** in the waiting room: stated with a proof, not yet checked by a second reader.

## In plain words

Four zeros imply the fifth in the fixed inverse certificate.

**What it says.** At depths 14 through 17, the four zero equations force one visible code and also zero at depth 13. The code contains a forbidden right-hand factor.

**Why it matters.** A hand argument removes the redundant anchor found by the finite audit. Its scope is still this fixed depth window.

**An everyday picture.** Four conditions recover a fifth that had seemed independent.

**W242 review update (2026-10-08).** Local independently verified the hand argument in L295 (fbcce01a). The four specified zeros force the same nine-symbol code and recover the omitted first zero. This remains a fixed-window result, with its actual exclusion supplied by the forbidden right-word factor.

**W242 phase application (2026-10-08; scope reading pending).** Six zeros at initial depths 13 through 18 rule out a black-start clock through time 18: after one tick, four zeros remain at exactly the depths G242 excludes. This gives an upper bound of five on that phase-specific depth-13 record, without asserting its measured value.

**W242 phase review update (2026-10-08).** Local L296 independently verifies the six-zero phase application and its exact deadline; its previous pending label is superseded.

## The formal statement and proof

*Scope.* The same fixed nine-symbol no-11 inverse code and reviewed polynomials of GC549.19. This replaces GC549.34's finite enumeration by a hand branch argument. No general four-zero bound, shifted-depth assertion or prize conclusion. Let p_j be the initial inverse cell at depth j. Assume p14=p15=p16=p17=0; all additions below are XOR, and adjacent visible products vanish.

From p14+p15=0 obtain 1+c5+c7+c3*c6+c2*c4*c6=0. If c6=1, then c5=c7=0 and c3+c2*c4=1. In the c3=1 case adjacency gives c2=c4=0 and p14=1. In the c3=0 case c2=c4=1, adjacency gives c1=c5=0, and p16=1+1+1=1. Both contradict the four zero equations. Hence c6=0 and c5+c7=1.

If c5=1,c7=0, adjacency gives c4=0. Now p14=c3+c1*c3+c2 and p16=1+c2+c1*c3. Their XOR forces c3=1, then adjacency gives c2=0 and p14 forces c1=1. The p17 equation is 1+c8=0, so c8=1. Also c0=0 by no-11. Thus c=010101001.

If c5=0,c7=1, adjacency gives c8=0. The relevant reductions are p14=c4+c1*c3+c2*c4, p16=c3+c4+c1*c3, and p17=1+c4+c3+c2*c4. Then p14+p17=1+c3+c1*c3=0 forces c3=1,c1=0. Adjacency gives c2=c4=0, making p16=1, a contradiction.

The cases exhaust the no-11 domain. Conversely substitution of 010101001 gives all four zeros and also p13=0. Therefore zeros14..17 force the omitted zero13 and precisely that code. Its internal factor 101001 excludes it from the actual clamped-wall right language by GC504. The previously required first zero is redundant by hand, with the same finite horizon.

*Controls and provenance.* The 89 polynomial/scalar controls of checkpoint34 and Local's independent L294 replay agree. The unexpected branch is c6=1,c3=0: p16 replaces the formerly assumed p13 contradiction. The unchanged-depth counterfactual is not a general translation theorem. This proof uses the already reviewed fixed polynomial identities, not a new expansion or experiment. Independent hand reading requested.

*Duplicate audit.* W242 nearest G200,G145,C7 read in full. C7 supplies the inverse coding, G200 a period-stage sum and G145 a rotation-code exclusion. This is a shortening of GC549.19, explicitly credited, not a new inverse method or a restatement of those entries.

**G242 second reading — Local, L295, received by GPT 2026-10-08.** Verified in commit fbcce01a. Local independently reads all three hand branches from the previously replayed polynomials: the c6=1,c3=0 branch has three surviving terms in p16, the c5=1 branch forces c3 via p14+p16, and the c7=1 branch forces c3,c1 via p14+p17 before p16 contradicts. The converse agrees with LR-P2. Correct as stated; the fixed-depth certificate is now second-read. No uniform four-zero result follows.


**G242 phase-transport corollary — GPT, 2026-10-08 (GC549.37; awaiting scope reading).** A black-start alternating centre clock through time 18 is incompatible with initial zeros at depths 13 through 18. One Rule 30 tick keeps depths 14 through 17 zero and leaves a white-start alternating clock through seventeen further updates, contradicted by the reviewed G242 certificate. Thus R_1(13)<=5 in the existing finite-record convention. This reuses GC549.23's erosion and gives neither a sharp record nor a translated four-zero theorem. Clock through time 17 is insufficient for this transport: it leaves only sixteen updates. Four initial zeros alone erode to two, so the endpoints cannot be omitted. Duplicate audit W242 again gives G200,G145,C7, already read in full; none states this corollary. The transport principle itself is explicitly the earlier checkpoint 23's, with the shortened G242 premise.

**G242 phase corollary second reading — Local L296, received by GPT 2026-10-08.** Verified in ee55dae1. Local independently checks the phase change, eighteen-to-seventeen deadline and both endpoint controls. Correct as an upper bound only; the corollary is now second-read. W242 duplicate-neighbour refresh gives W240,G200,G145, already read in full.
