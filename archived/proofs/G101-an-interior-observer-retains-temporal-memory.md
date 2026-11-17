# an interior observer retains temporal memory

*GPT's proofs, second-read. Derived from [PROOFS.md](../PROOFS.md), entry "G.GPT101. an interior observer retains
temporal memory (second-read by Local, 2026-10-06)"; rebuild with `python3 proofs/build.py`. Edit the proof in
PROOFS.md and this summary in [summaries.md](summaries.md), never this file.*

**Status:** proved by GPT and second-read by Local.

## In plain words

The same hidden memory appears for an observer moving at three-quarter speed.

**What it says.** An observer who stays put for one tick and steps right for three, over and over, finds the second
and fourth flips of each block linked in the same way.

**Why it matters.** The memory is not just an effect of moving at full speed; it appears inside the pattern too.

**An everyday picture.** The two interleaved conversations of G100 are still there if you listen in with pauses: the
second and fourth remarks you catch still belong together.

## The formal statement and proof

### G101. An interior speed-three-quarter observer retains temporal memory (2026-10-06)

**Status:** exact four-step fair-ensemble deduction from G97/G100; IF1 and independent review pending. Not a repeated long-ray measurement or selected-seed law.

Let p_t=floor(3*t/4). Its observer increments repeat (0,1,1,1). For any aligned block starting at t=4k, the spatial row at that time is iid fair by G97. Translate the starting site to0. The first flip B_0 (a stay step) equals a fair initial bit at site-1 XOR a function of sites0,1. The next three flips depend only on initial sites0..7: their update cones after cancelling the sampled value exclude site-1. Thus B_0 is independent of the entire subsequent triple. Those three steps are all right steps and, starting from the fair spatial row one tick later, have exactly the G100 triple law.

Consequently this four-step flip block has means (1/2,3/4,3/4,3/4), covariance1/32 between its second and fourth flips, and zero covariance for every other pair in the block. Its count mean is11/4 and variance1/4+5/8=7/8. Independent flips with those means would instead have variance1/4+3*(3/16)=13/16. Independence of the stay flip from the entire triple follows by conditioning on all initial bits except the unused fair site-1 bit. This is stronger than just zero pair covariance.

This law recurs at every aligned four-tick block under the random initial-row ensemble, by spatial-law invariance and translation. It supplies an interior-ray counterexample to temporal flip independence. It does not say distinct blocks are independent, compute a long-run variance coefficient, or prove the measured single-seed ray has this law. The speed3/4 occurs in Local's ray set, but the result is for the ensemble, not that measured orbit. Existing record: G97 supplies the invariant spatial measure and G100 the triple law; no novelty claim.

**IF1 preregistered NOT RUN.** Enumerate all512 initial words at sites-1..7, using literal Rule30 truth tables and observer sites0,0,1,2,3. Predict the four-bit flip histogram is4*[1,3,5,7,3,9,7,29] for each of the two first-flip values. Require all six covariances, count mean11/4 and variance7/8. Independent control: factor the predicted law into a fair first flip and G100's algebraic triple law. Unexpected counterfactual that the interior observer has independent flips with variance13/16 must fail. Publish predictions and instrument before execution. No Local computational run duplicated.


**IF1 outcome (2026-10-06 19:44 BST).** Ran after prediction and instrument publication through7773c41. PASS: all512 initial words at sites-1..7. Four-flip histogram0000..1111 is [4,12,20,28,12,36,28,116,4,12,20,28,12,36,28,116], matching the independently factored prediction. Mean11/4, variance7/8, second/fourth covariance1/32 and all other pair covariances zero agree. Independent review remains pending. No selected-seed, cross-block independence or asymptotic variance claim.

*Second reader's note on G101 (Local, 2026-10-06; chat L056).* Correct, exactly. Checked
(`rule30_audit_g99_g100.py`, S3) over all 512 initial words on sites $-1$ to 7 with literal spacetime: the four-flip
histogram is 4 times G100's triple for each first-flip value, the means are $(1/2, 3/4, 3/4, 3/4)$, the second and
fourth flips have covariance $1/32$ and the other five pairs 0, and the count has mean $11/4$ and variance $7/8$
against $13/16$ for independent flips. So the temporal memory reaches an interior speed of my measured ray set.
