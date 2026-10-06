# A clean dependency cone gives a law-free disagreement bound

*The waiting room (not yet verified). Derived from [PROOFS.md](../PROOFS.md), entry "G103. A clean dependency cone
gives a law-free disagreement bound (2026-10-06)"; rebuild with `python3 proofs/build.py`. Edit the proof in
PROOFS.md and this summary in [summaries.md](summaries.md), never this file.*

**Status:** in the waiting room: stated with a proof, not yet checked by a second reader.

## In plain words

A race-free dependency cone guarantees the cell follows the ideal history.

**What it says.** With independent race flags, a target cell's disagreement probability is at most1-(1-eps)^(t²). With only marginal flag bounds, it is at most eps*t². A fixed mean disagreement threshold therefore cannot arrive on a scale smaller than order eps^(-1/2).

**Why it matters.** It gives a rigorous constraint without fair-state or effective damage-speed assumptions. It supplies no matching upper bound, exact survival constant or realised hitting-time guarantee. Snapshot reads at unflagged nodes are required. Controls pass on 77440 histories and192 exact weighted site bounds; colleague review remains pending.

**An everyday picture.** If every ingredient in a recipe's dependency chain is unchanged, the final dish is unchanged too.

## The formal statement and proof

**Status:** coupling/union-bound proof; CP1 and independent review pending. Follow-up to Local L054 and G102. Existing-record search found the effective-cone fit but no clean-dependency-cone bound. This uses elementary deterministic dependencies and Bernoulli/union bounds, not a new concentration theorem.

Couple an ideal radius-one synchronous history and a raced history from the same arbitrary initial row. Assume every unflagged update reads its three parents from the raced history's previous logical row and applies the original rule; flagged updates may read already-computed neighbours as in races.c. For target(i,t), take all ancestor update nodes (j,s), 1<=s<=t, |j-i|<=t-s. There are t² distinct nodes on the line. On a W-cell ring, deduplication gives M=sum over s1..t of min(W,2*(t-s)+1)<=t².

**Clean-cone lemma.** If no ancestor node is flagged, target(i,t) equals the ideal value, regardless of flags outside the cone. Proof: induction from the common initial row through the cone's generations. Each cone update is unflagged and its three parents lie in the preceding cone layer. All those parents therefore agree, and applying the same deterministic rule preserves equality. New-value propagation outside the cone cannot enter via an unflagged node. Snapshot reads at unflagged nodes are an explicit assumption, not a claim about arbitrary in-place updating.

With independent Bernoulli(eps) flags, the clean event has probability(1-eps)^M. Consequently

    P(target differs)<=1-(1-eps)^M<=1-(1-eps)^(t²).

Without independence, if every flag has marginal probability at most eps, the union bound still gives P(target differs)<=min(1,eps*t²). Neither bound assumes fair states, injected-error independence, a measured speed0.246, damage irreversibility or a half-differing interior. Averaging cell indicators gives the same bound for the expected disagreement fraction D_t on a finite ring; spatial independence is unnecessary. Markov's bound also gives P(D_t>=delta)<=min(1,[1-(1-eps)^(t²)]/delta).

For 0<eps,delta<1, mean disagreement at least delta requires

    t>=sqrt(log(1-delta)/log(1-eps))

under independent flags, and t>=sqrt(delta/eps) under the marginal-only bound. Thus the necessary timescale is at least order eps^(-1/2) as eps tends to0, for any fixed mean threshold. This is a lower constraint on the onset of mean decoherence, not a matching upper estimate, exact survival law, realised hitting-time bound or exponent fit. It does not turn Local's measured coefficient0.623 into a theorem. Local's fractions concern finite realised runs.

**Unexpected final-tick guard.** On a five-cell ring started from a black cell at2, allow a right race only at site0 on step1, then no races on step2. Site1 on step2 differs from the ideal history despite its own final update being unflagged. Its ancestor at(step1,site0) was flagged. Checking just the final target is insufficient.

**CP1 preregistered NOT RUN.** For W3..5,T1..2, enumerate all initial rows and flag histories in both sequential race directions with races.c's boundary convention. Require agreement at every site with a clean cone. Use exact weights at eps0,1/4,1/2,1 and require every site disagreement probability to obey both bounds. Independently construct ancestor sets, and retain the final-tick guard. This is77440 short row/flag cases, no stochastic simulation or eps-scaling rerun. Publish predictions and instrument before execution.


**CP1 outcome (2026-10-06 19:56 BST).** Ran after prediction and instrument publication through43095bf. PASS: 77440 initial-row/flag histories and192 exact weighted site bounds. Every clean-cone site agrees, both independent-flag and marginal-only bounds hold, and the final-unflagged/earlier-ancestor guard differs as predicted. These finite controls support the coupling proof; they provide no matching rate, effective cone or realised hitting-time claim. Independent colleague review remains pending.
