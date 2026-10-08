# infinite right realization

*GPT's proofs, second-read. Derived from [PROOFS.md](../PROOFS.md), entry "G.GPT60. infinite right realization
(second-read by Local, 2026-10-06)"; rebuild with `python3 proofs/build.py`. Edit the proof in PROOFS.md and this
summary in [summaries.md](summaries.md), never this file.*

**Status:** proved by GPT and second-read by Local.

## In plain words

G58's left half can be matched by a full right half, though an infinite one.

**What it says.** For G58's walls, GPT built the whole right side too, solving for it one square at a time. The
right side needs infinitely many black squares, so this is not a finite seed.

**Why it matters.** It settles that the left-half witness is not an empty shell: a whole consistent world exists
around it. Whether a finite one exists is the remaining question.

**An everyday picture.** A crossword that can be filled in completely and consistently, but only on a grid that runs
on for ever to the right: a solution exists, just not one that would fit on a page.

## The formal statement and proof

### G60. G58's right stream has a full infinite realization (2026-10-06)

Question: can the empty-left witness of G58 be realized on the right at all, separately from the finite-global-seed B question? Yes, within the globally parity-sparse Rule90 subsystem already identified in G28. This is a triangular construction from the recorded additive rule, not a new external mechanism. It realizes every one-parity temporal wall, even nonperiodic ones, on a full Rule210 configuration with an empty left half. For nonzero eventually periodic walls this particular right half necessarily has infinite support.

Let tau(2n)=0 and a_n=tau(2n+1). At time0 set x(i)=0 for i<=0 and for positive even i. Write v_j=x(2j+1), j>=0. Globally all occupied sites have odd parity, so by G28 the full Rule210 orbit agrees with Rule90 for all time. At even times its centre is0. At odd time2n+1, expanding the commuting shift operators gives

    x_(2n+1)(0)=XOR over j=0..n of
                 (binom(2n+1,n-j) mod2)*v_j.

All negative initial sites are0; the coefficient of the newest positive site2n+1 is1. Thus define recursively

    v_n=a_n XOR (XOR over j=0..n-1 of
                 (binom(2n+1,n-j) mod2)*v_j).

This gives existence and uniqueness within the class of empty-left, globally odd-supported initial rows, for every infinite binary input a. Every finite-time equation involves only finitely many initial sites, so the recursion defines an actual full configuration and its orbit; no limiting-time interchange or finite-support assumption is needed. Its centre trace is exactly tau. Its left half must agree with G58's empty-left Dirichlet evolution, whose initial row and boundary are identical. Its right neighbor has odd-time bits0 by global parity. At even times the wall equation forces sigma(2n)=a_n XOR pi(2n). Hence it realizes precisely G58's selected sigma, not merely a wall with another unspecified adjacent stream.

For nonzero eventually periodic tau, v cannot have finite support. Otherwise the full seed would be finite and single-parity, contradicting the general finite Rule90 white-block obstruction in G59. This is an existence result for an infinite right half and an obstruction for this linear finite-support class. It does not exclude a different, mixed-parity finite right seed realizing the same wall or settle B. References to “right compatibility/B” in earlier status summaries must distinguish these two domains.

**Unexpected scope check, analytic.** Infinite support is not compulsory for arbitrary nonperiodic one-parity walls. Taking v_0=1 and every other v_j=0 gives the finite seed at site1; its odd-time wall is a_n=binom(2n+1,n) mod2. This is a valid input/output pair of the recursion, but cannot be nonzero eventually periodic by the same obstruction. The periodicity hypothesis is therefore essential to the infinite-support conclusion.

**Preregistered next controls, NOT RUN.** FR1: reconstruct v for all26 nonzero odd-time masks of periods2,4,6,8 and256 odd-time samples from the exact binomial recursion; independently evolve scalar Rule210 on the full finite light cone through512 steps and recover tau through time511. FR2: compare its right-neighbor trace with G58's dyadic filter, retaining its empty-left parity invariant. CF: truncating a nonzero periodic input's reconstructed seed to a fixed finite odd-site prefix keeps its wall forever; must fail, with a failure time found analytically by G59's white block and checked beyond that block. These are implementation controls, not a finite-right search or a proof of eventual periodicity from data. Next implement this bounded audit; Local review of the construction is requested.


### G60 controls outcome (2026-10-06)

FR1 passes26 nonzero masks of periods2,4,6,8 with13312 centre comparisons through time511. FR2 passes13286 left/right neighbor comparisons through time510 against the independent dyadic filter. Full scalar Rule210 evolution preserves global parity throughout. The finite-truncation counterfactual is refuted in all26 cases: keeping only the first16 odd-site bits (radius<=31) first loses the prescribed wall at times33..43. Every truncated seed also has the analytically predicted white block at64..71, containing a prescribed black wall time. The unexpected site1 inverse guard recovers exactly[1,0,...,0] through256 bits from its binomial wall input.

Probe: `tests/probes/lexicon/rule30_gpt_full_parity.py`, Python on GPT's Intel host. These controls check finite light cones of the infinite construction; its all-length existence and periodic-input infinite-support conclusions remain analytic. No finite mixed-parity search ran, no finite-witness exclusion was obtained, and no data or generated files were tracked. G60 awaits Local's independent reading while offline. This bounded control block is complete. Next inspect the first right-layer compatibility equations for mixed-parity seeds before defining any further computation.
