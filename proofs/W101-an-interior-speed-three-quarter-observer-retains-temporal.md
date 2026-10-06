# An interior speed-three-quarter observer retains temporal memory

*The waiting room (not yet verified). Derived from [PROOFS.md](../PROOFS.md), entry "G101. An interior
speed-three-quarter observer retains temporal memory (2026-10-06)"; rebuild with `python3 proofs/build.py`. Edit the
proof in PROOFS.md and this summary in [summaries.md](summaries.md), never this file.*

**Status:** in the waiting room: stated with a proof, not yet checked by a second reader.

## In plain words

Temporal memory also appears in an interior moving frame.

**What it says.** A speed-three-quarter observer repeats stay/right/right/right. Under a fair random initial row, the second and fourth flips in each aligned block have covariance1/32. The four-flip count variance is7/8 rather than the independent prediction13/16.

**Why it matters.** It extends the exact right-edge guard to an interior ray without rerunning long measurements. Distinct blocks need not be independent, and the selected seed or long-run variance remains unproved. Small controls and independent review remain pending.

**An everyday picture.** A slower route can still contain short stretches that carry the same memory as a fast route.

## The formal statement and proof

**Status:** exact four-step fair-ensemble deduction from G97/G100; IF1 and independent review pending. Not a repeated long-ray measurement or selected-seed law.

Let p_t=floor(3*t/4). Its observer increments repeat (0,1,1,1). For any aligned block starting at t=4k, the spatial row at that time is iid fair by G97. Translate the starting site to0. The first flip B_0 (a stay step) equals a fair initial bit at site-1 XOR a function of sites0,1. The next three flips depend only on initial sites0..7: their update cones after cancelling the sampled value exclude site-1. Thus B_0 is independent of the entire subsequent triple. Those three steps are all right steps and, starting from the fair spatial row one tick later, have exactly the G100 triple law.

Consequently this four-step flip block has means (1/2,3/4,3/4,3/4), covariance1/32 between its second and fourth flips, and zero covariance for every other pair in the block. Its count mean is11/4 and variance1/4+5/8=7/8. Independent flips with those means would instead have variance1/4+3*(3/16)=13/16. Independence of the stay flip from the entire triple follows by conditioning on all initial bits except the unused fair site-1 bit. This is stronger than just zero pair covariance.

This law recurs at every aligned four-tick block under the random initial-row ensemble, by spatial-law invariance and translation. It supplies an interior-ray counterexample to temporal flip independence. It does not say distinct blocks are independent, compute a long-run variance coefficient, or prove the measured single-seed ray has this law. The speed3/4 occurs in Local's ray set, but the result is for the ensemble, not that measured orbit. Existing record: G97 supplies the invariant spatial measure and G100 the triple law; no novelty claim.

**IF1 preregistered NOT RUN.** Enumerate all512 initial words at sites-1..7, using literal Rule30 truth tables and observer sites0,0,1,2,3. Predict the four-bit flip histogram is4*[1,3,5,7,3,9,7,29] for each of the two first-flip values. Require all six covariances, count mean11/4 and variance7/8. Independent control: factor the predicted law into a fair first flip and G100's algebraic triple law. Unexpected counterfactual that the interior observer has independent flips with variance13/16 must fail. Publish predictions and instrument before execution. No Local computational run duplicated.
