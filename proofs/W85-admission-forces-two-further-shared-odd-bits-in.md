# Admission forces two further shared odd bits in a = 21 candidates

*The waiting room (not yet verified). Derived from [PROOFS.md](../PROOFS.md), entry "G85. Admission forces two
further shared odd bits in a = 21 candidates (2026-10-06)"; rebuild with `python3 proofs/build.py`. Edit the proof
in PROOFS.md and this summary in [summaries.md](summaries.md), never this file.*

**Status:** in the waiting room: stated with a proof, not yet checked by a second reader.

## In plain words

The same possible pair must follow two more common odd steps.

**What it says.** Continue W84's smaller and larger starts. After their differing third step, their values have the same parity. The smaller start needs an odd fourth step to satisfy the growth-factor condition, forcing the larger to take one too. The same argument forces an odd fifth step for both. Their first five step patterns must be 11011 and 11111, where 1 means odd. Their starts leave remainders 27 and 31 on division by 32.

**Why it matters.** It makes the necessary candidate shape more precise. It neither finds a meeting nor excludes every possible pair. The next step has opposite parities, so the common odd-step extension stops here. Independent review and preregistered controls remain pending.

**An everyday picture.** Two routes must share two extra turns after their first fork; that still does not show that they reach the same destination.

## The formal statement and proof

Continue G84's necessary a = 21 collision orientation. Let the smaller start n have prefix110 and the other start n+4 prefix111. After three steps their values are

    u=(9*n+5)/8, u'=(27*n+127)/8=3*u+14.

Thus these values have the same parity. Admission of the110 branch at step 4 requires its next bit1: retaining only two odd bits would leave9<16. Both values therefore take an odd step, giving v' =3*v+20 where v=(3*u+1)/2. These values again have the same parity. Admission of the lower branch at step 5 requires another odd bit, since27<32. Both take that odd step. Every a = 21 collision candidate must consequently have first five bits11011 and11111, respectively. By the parity bijection the lower start is27 modulo 32 and the upper31 modulo 32. After five steps their values satisfy w'=3*w+29, so they have opposite parity next; no further common-bit extension is asserted.

This is a conditional constraint on any collision, not its existence or an a = 21 exclusion. The global span bound still allows the positive intercept orientation, and these prefixes still attain its opposing extrema; this refinement does not by itself improve the cutoff20.

**Unexpected admission guard.** Starts3 and7 differ by 4 and begin110/111, but the lower branch fails coefficient admission at step 4. Its first five bits are11000, while the upper has11101. Thus displacement4 and the three-bit orientation alone do not imply the five-bit prefixes. The counterfactual omitting admission must fail on this pair.

**Next controls, preregistered NOT RUN.** FP1: direct exact trajectories for n=8*k+3 with0<=k<256 and n+4; whenever the lower start is coefficient-admitted through 5, require both five-bit prefixes, the three affine relations above, residues27/31 modulo 32 and opposite next parity. Do not require a terminal collision or infer one. FP2: separately check3/7 and the residue representatives27/31, retain failed admission in the guard. These are small algebra controls, not a new collision search or a Local computational job. Review requested; elementary recorded identities, no novelty claim.
