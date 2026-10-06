# two further forced odd bits at a = 21

*GPT's proofs, second-read by Local. Derived from [PROOFS.md](../PROOFS.md), entry "G.GPT85. two further forced odd
bits at a = 21 (second-read by Local, 2026-10-06)"; rebuild with `python3 proofs/build.py`. Edit the proof in
PROOFS.md and this summary in [summaries.md](summaries.md), never this file.*

**Status:** proved by GPT and second-read by Local.

## In plain words

The two candidates of G84 must also take the same next two steps: both odd.

**What it says.** After their third step the two numbers are both odd or both even. The smaller one needs an odd
fourth step and an odd fifth step to keep its growth factor up, so the larger one takes them too. Their first five
steps must be odd-odd-even-odd-odd and five odds, so they leave remainders 27 and 31 when divided by 32.

**Why it matters.** Each forced step cuts the places a meeting could hide by half, by proof rather than search.

**An everyday picture.** Two dancers keeping time to the same music: when one must step forward, so must the other.

## The formal statement and proof

### G85. Admission forces two further shared odd bits in a = 21 candidates (2026-10-06)

Continue G84's necessary a = 21 collision orientation. Let the smaller start n have prefix110 and the other start n+4 prefix111. After three steps their values are

    u=(9*n+5)/8, u'=(27*n+127)/8=3*u+14.

Thus these values have the same parity. Admission of the110 branch at step 4 requires its next bit1: retaining only two odd bits would leave9<16. Both values therefore take an odd step, giving v' =3*v+20 where v=(3*u+1)/2. These values again have the same parity. Admission of the lower branch at step 5 requires another odd bit, since27<32. Both take that odd step. Every a = 21 collision candidate must consequently have first five bits11011 and11111, respectively. By the parity bijection the lower start is27 modulo 32 and the upper31 modulo 32. After five steps their values satisfy w'=3*w+29, so they have opposite parity next; no further common-bit extension is asserted.

This is a conditional constraint on any collision, not its existence or an a = 21 exclusion. The global span bound still allows the positive intercept orientation, and these prefixes still attain its opposing extrema; this refinement does not by itself improve the cutoff20.

**Unexpected admission guard.** Starts3 and7 differ by 4 and begin110/111, but the lower branch fails coefficient admission at step 4. Its first five bits are11000, while the upper has11101. Thus displacement4 and the three-bit orientation alone do not imply the five-bit prefixes. The counterfactual omitting admission must fail on this pair.

**Next controls, preregistered NOT RUN.** FP1: direct exact trajectories for n=8*k+3 with0<=k<256 and n+4; whenever the lower start is coefficient-admitted through 5, require both five-bit prefixes, the three affine relations above, residues27/31 modulo 32 and opposite next parity. Do not require a terminal collision or infer one. FP2: separately check3/7 and the residue representatives27/31, retain failed admission in the guard. These are small algebra controls, not a new collision search or a Local computational job. Review requested; elementary recorded identities, no novelty claim.

### G85-G86 prefix and slack controls outcome (2026-10-06)

FP1-FP2 pass all 256 displacement-four pairs: 64 lower prefixes satisfy admission through five steps and have the required five-bit words, residues and affine relations; the 192 excluded prefixes are retained. SR1 confirms full and shifted admission of the 33-step word, fresh suffix deficit at step 26, and six-step states 107/121 with odd counts 5/5 for starts 27/31. Both counterfactuals are refuted. No control failed and no meeting pair was sought or asserted. Probe: `tests/probes/prizes/collatz_gpt_prefix_slack.py`; predictions at 2a8df48, published via aab6d7d, GPT Intel Python, under one second. Independent proof review remains pending.
