# mirror extension and quantifiers

*GPT's proofs, second-read by Local. Derived from [PROOFS.md](../PROOFS.md), entry "G.GPT65. mirror extension and
quantifiers (second-read by Local, 2026-10-06)"; rebuild with `python3 proofs/build.py`. Edit the proof in PROOFS.md
and this summary in [summaries.md](summaries.md), never this file.*

**Status:** proved by GPT and second-read by Local.

## In plain words

Any finite left half for Rule 210 can be matched by mirroring it on the right, and then column 1's freedom jumps.

**What it says.** Copy any finite left half, reflected, onto the right side. The two copies' effects cancel at the
wall, so the wall still blinks. Allowing every finite left half, column 1 can show any pattern at its even ticks:
half a bit of new information per tick.

**Why it matters.** It shows G64's "almost no information" depends on fixing the left half; vary it, and freedom
returns. It clarifies what the earlier statements do and do not cover.

**An everyday picture.** Two people pushing a swing from opposite sides at the same moment: their pushes cancel, and
the swing keeps its rhythm.

## The formal statement and proof

### G65. Mirror extension and the varying-left-row quantifier (2026-10-06)

Scope audit following G041, using G27's finite-prefix continuation and G60's triangular full realization. Fix tau=0101. Let h_j be G60's initial right bit at site2j+1 for the empty-left system. Prescribe any finite initial left row supported on odd depths, with e_j at site-(2j+1), and define the initial right row by

    v_j=h_j XOR e_j,

with every positive even site and the centre0. This gives a full Rule210 realization of the same clock and the prescribed left row. Its right support is infinite, since h has infinite support and e is finite. It is not a finite global witness.

Proof. The entire initial configuration has odd spatial support, so its Rule210 orbit agrees with Rule90. Relative to G60, the added configuration has the same bit e_j at the reflected sites plus/minus(2j+1). In the Rule90 expansion at the centre, those two sites have equal binomial coefficients at every time (the two coefficients are symmetric), so their contributions cancel over GF(2). Thus the wall stays0101 for all time. Equivalently the odd-time triangular equation depends on v_j XOR e_j; setting this to h_j preserves every equation. No linearity claim is made outside the global parity-sparse subsystem. The full left evolution is the unique Dirichlet evolution with that row and wall, hence matches G27's compatible left construction. This proves full infinite-right extension for every finite odd-supported left row, not only for the empty row.

**Exact language count after varying the row.** Restrict to these globally parity-sparse full realizations while allowing every finite odd-supported initial left row. In column1 every odd-time bit is0. By G27's continuation corollary, every length-n even-time word occurs: choose its finite left row (support at most2n-1) and apply the mirror extension above. Thus length-N temporal factors, across all realizations and all start times, are exactly the binary words with zeros on one of their two alternating position classes. Either class is realized by choosing a sufficiently long even-time prefix and a start of parity0 or1. Their intersection contains only the all-zero word. Therefore

    P(N)=2^ceil(N/2)+2^floor(N/2)-1,
    lim as N->infinity of log2(P(N))/N=1/2.

This is entropy of the union's temporal language. It does not assert that any one orbit has entropy1/2, or that every fixed nonempty initial left row has zero entropy. G64 proved zero for one fixed empty-left family, including its potentially nonlinear right realizations. Removing the fixed-row hypothesis already gives entropy at least1/2 in the broader family, because the parity-sparse subfamily above realizes these factors. No exact entropy is asserted for the broader mixed-parity family.

**Unexpected domain guard.** Reflected additions do not automatically cancel in Rule210 outside the parity subsystem. From the finite initial seed{1}, the centre at time2 is0. Adding the reflected even sites{-2,2} gives seed{-2,1,2}, whose centre at time1 is1, left neighbor1 and right neighbor0; Rule210 then gives centre1 at time2. Thus the centre changes, despite the mirrored addition. This is an analytic truth-table counterexample to importing Rule90 superposition into mixed-parity Rule210. It is not a clock witness or an experiment.

This synthesizes already recorded G27/G60 with the elementary binomial symmetry; no novelty claim or new prior-art theorem. The finite-right B problem remains open, and no Rule30 consequence is asserted. New details await Local's independent reading.

**Next controls, preregistered NOT RUN.** MX1:32 odd-depth left masks through depth9, reflected onto G60's reconstructed right seed, scalar Rule210 through256 steps; clock, prescribed initial left row and global parity must hold. MX2: all256 odd-depth left masks through depth15, same full extension, first8 column1 even bits must cover all256 words. Compare the two-phase temporal factor count for lengths1..8 against the exact formula above using those finite prefixes. CF: adding any reflected finite seed preserves a Rule210 centre trace; refute with{1} versus{-2,1,2} at time2. These are bounded controls for full infinite-right light cones and the language map, not finite-global witness searches.


### G65 controls outcome (2026-10-06)

MX1 passes32 left masks/8224 clock and parity time checks through256 steps. MX2 realizes all256 distinct eight-bit even-time column1 prefixes; temporal factor counts for lengths1..8 are2,3,5,7,11,15,23,31, matching the exact formula. The mixed-parity reflected-addition counterfactual is refuted at time2 (centre0 versus1). Probe: `tests/probes/lexicon/rule30_gpt_mirror.py`, Python on GPT's Intel host, under1 s. These finite checks do not estimate entropy or construct finite global witnesses. No control failed. The extension/count block is complete; G66 addresses bounded support uniformly.
