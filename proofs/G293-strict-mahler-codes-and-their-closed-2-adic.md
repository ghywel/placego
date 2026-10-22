# Strict Mahler codes and their closed 2-adic closure have dimension log2(3/2)

*GPT's proofs, second-read. Derived from [PROOFS.md](../PROOFS.md), entry "G.GPT293. Strict Mahler codes and their
closed 2-adic closure have dimension log2(3/2) (second-read by Local, 2026-10-14)"; rebuild with `python3
proofs/build.py`. Edit the proof in PROOFS.md and this summary in [summaries.md](summaries.md), never this file.*

**Status:** proved by GPT and second-read by Local.

## In plain words

The strictly admissible Mahler parity records form a nonclosed set of 2-adic starts. Its closure adds boundary records but has the same finite-prefix language. Both sets have Hausdorff dimension log2(3/2): prefix counts give the upper bound, and the real beta map supplies the lower bound through cylinder masses. Local checked the carrying steps in L710.

**Why it matters.** This repairs the compactness wording while keeping the integer-realization question separate. It does not exclude positive ordinary integer starts.

## The formal statement and proof

**PROVED, Local L710 at9692476e.** Source: RULE30-GPT.md GC1221, section 2; finite-prefix clarification GC1222. Local read the triangular isometry, strict extension of each valid prefix and the cylinder mass bound. This is a structural lemma about the admissible code set, not Mahler nonexistence or a claim of new prior art. Filing check: proof_dupes --near G293 found G132, G147 and G143; all three were read. They concern rotation-code exclusions, phase countability and a repeat-filter counterexample, respectively; this lemma restates none of them. The carrying text below is copied verbatim from GC1221.

**2. Strict admissibility is not closed in the 2-adics.** Let S_strict contain the 2-adic starts whose parity code b has every tail u_j=sum_(k>=0) b_(j+k) 2^k/3^(k+1) strictly below 1/2. Let K contain starts whose every finite G51 window is nonempty. Each finite predicate depends on a finite residue, so K is closed. G51's prefix bijection makes the map b -> -sum b_k*2^k/3^(k+1) a homeomorphism from binary codes to Z_2, preserving common-prefix distances. Every finite valid prefix extends to a strict greedy code, hence K is the closure of S_strict.

Two boundary controls show these sets differ. The greedy critical code d(1) at normalized beta input 1 has u_0=1/2, so it is not strict; every finite prefix occurs for inputs below 1, so its 2-adic start lies in K. The critical remainder never vanishes (its dyadic numerator stays odd), which keeps each such prefix interval nonempty. Likewise the code 0 d(1) has u_0=1/3 and u_1=1/2; inputs approaching 1/3 from below give strict codes approaching it. This second control locates the excluded boundary after time 0 rather than only at the initial endpoint.

The uncountability and Hausdorff dimension log_2(3/2) do hold for both sets in the usual 2-adic metric. For the upper bound, GC663 gives fewer than 3 beta^T admissible prefixes, covering either set with balls of diameter 2^(-T). For the lower bound, push normalized Lebesgue measure on beta inputs [0,1) through their greedy code and then the 2-adic prefix map. A length-T code cylinder has Lebesgue measure at most beta^(-T), since its branch slope is beta^T. Thus every radius-2^(-T) ball has mass at most (2^(-T))^s, s=log_2(beta); the elementary mass-distribution covering argument gives dimension at least s. This also proves uncountability. No new language count or statistical fit is used.
