# Independent and non-mainstream work on Rule 30 since the 2019 prizes

Scope and method. Searched 2026-10-09: arXiv (API phrase search `abs:"rule 30"`, every entry since 2019), GitHub
(repository search, code search for Lean files), Wolfram Community, the Wolfram Data Repository, OEIS A051023, and
Stack Exchange (MathOverflow, Math SE and CS SE through the API; cstheory was rate-limited). Each item was checked
against PRIOR-ART.md by grepping the author or repository name. **Already listed** means it is in PRIOR-ART.md, and it
is repeated here only when something new was found. "Read" means the page or file was opened. "(search summary)" means
only a search engine's summary was seen. None of the third-party code below was run. The one computation run for these
notes is the ring count under Key Question 5, and its code is given there.

Already in PRIOR-ART.md and not repeated unless new: Condrey (arXiv:2609.09431), Nersissian (arXiv:2609.25077,
2609.25078), Kopra (TCS 2023; arXiv:2202.13809), Kari and Kopra (arXiv:1710.05737), Rowland (2006), Jen, Powley's
thesis, Das (arXiv:2207.13237), Chan-López and Martín-Ruiz (arXiv:2604.00165), woahwhattheheck/commons issue 15314 and
PR 15318, Patto1155/rule30-foundry PR 47, fabianxvogt/rule30, TheJustinSunPrize/awards issue 774, OEIS A334496/A334497,
openai/math, Spencer, Meier–Staffelbach, Mariot et al., Yolcu–Aaronson–Heule (Collatz), and "Brunnbauer 2019"
(PRIOR-ART names it only as a search term).

## Q1. Which arXiv preprints from 2019 to 2026 make partial, checkable progress on the three prize problems?

### Takeaway
Since 2019 arXiv has very few Rule 30 preprints, and almost all of them are already in the record. The one new item
is Natal and Al-saadi (2024). It proves an O(n²/log n) bound for simulating any 1-D automaton to generation n and
measures it on Rule 30. This touches Problem 3 only loosely and says nothing about period 2. The full-solution claims
found (one arXiv paper, one Zenodo-backed repository, forum posts) give no checkable proof and are listed separately
below.

### Cited Findings
- **Coverage.** The arXiv API's exact-phrase search for "rule 30" in abstracts returns 15 entries in all. From 2019 on
  they are Kopra 2202.13809, Das 2207.13237, Fukś 2312.11377, Natal and Al-saadi 2409.07065, Sfairopoulos et al.
  2503.19572, Chan-López and Martín-Ruiz 2604.00165 (now at v3), Condrey 2609.09431 and Nersissian 2609.25077 and
  2609.25078, plus four unrelated ML or crypto papers that mention Rule 30 in passing —
  [arXiv API
  query](https://export.arxiv.org/api/query?search_query=abs:%22rule%2030%22&max_results=200&sortBy=submittedDate&sortOrder=descending).
- **NEW: Natal, J. and Al-saadi, O., "Fast Simulation of Cellular Automata by Self-Composition"**, arXiv:2409.07065,
  cs.CC (v1 2024-09-11, v2 2025-06-22). Type: proof plus computation.
  - Claim: k-fold self-composition gives a radius-kr rule whose rule table costs O(k²·2^(2kr)) to build. With
    k ~ log n (by the Lambert W function), the configuration at generation n costs O(n²/log n) time and O(n²/(log n)³)
    space (Theorem 8, Corollary 9). The result is for the whole row, not a single centre cell.
  - Experiments on Rule 30: the code's N = 10,000,000, run on a Xeon Gold 6230. The authors state that Wolfram's
    bitwise methods are "several times faster" at practical sizes. They also state that the bound assumes the
    unit-cost RAM model and that the n²/k step is a "simple geometric argument".
  - Verification: C++17 source is printed in Appendix 6.1, with no repository. Not run here.
  - Red flags: none of substance. It is a generic time–memory trade-off (a Four-Russians-style speedup), not evidence
    about irreducibility —
    [arXiv abs](https://arxiv.org/abs/2409.07065); [HTML v2](https://arxiv.org/html/2409.07065v2).
  - Use for period 2: none directly. For Problem 3 it fixes the baseline that any "O(n)" claim must beat:
    full simulation is already o(n²).
- **NEW, but its author is already listed: Nersissian, T., "Rule 30 Exact Binomial–Lucas Lifting: From Boolean Logic
  to Integer Coefficients, Stirling Transfer, and Support-Set Algebra"**, Wolfram Community / Wolfram Cloud document
  (2026-03-02, Staff Picks). Type: algebraic framework, partly proved.
  - Claims: the abstract says the framework proves that the 2-D spatial rows "expand infinitely and are strictly
    non-periodic" (Theorems 6.4 and 6.5). It treats the centre column's periodicity and density as open.
  - Verification: Proposition 2.1, Lemma 3.1, Corollary 4.1 and Theorem 4.3 have short proofs that can be checked.
    In the copy read, sections 6.2 to 9 are headings only, so the row theorems cannot be checked.
  - Red flags: it cites "arXiv:submit/7289701", a submission placeholder rather than an arXiv ID. Two references share
    a DOI, and one links to an unrelated title —
    [Wolfram Cloud document](https://www.wolframcloud.com/obj/b04b6551-fecf-465d-b02d-63d95abd751c).
  - In a Community post of 2026-02-12 the same author says his support sets S_m allow any cell to be queried in
    O(log n) time *once S_m is computed*, and asks whether the recursion for S_m can be shortcut —
    [Wolfram Community thread](https://community.wolfram.com/groups/-/m/t/1802242).
- **Already listed: Chan-López and Martín-Ruiz, arXiv:2604.00165**, now at v3 (2026). New detail, from a search
  summary only: it reports block entropies of a 4,096-step single-seed centre column and says the symmetric reference
  rule 22 admits O(log m) evaluation, leaving Rule 30 open —
  [arXiv HTML](https://arxiv.org/html/2604.00165v1) (search summary).
- **Peripheral, not read beyond the listing:** Sfairopoulos, K., Causer, L., Mair, J. F. et al., "Spin models from
  nonlinear cellular automata", arXiv:2503.19572 (2025), from an academic statistical-physics group; Fukś, H., "Four
  state deterministic cellular automaton rule emulating random diffusion", arXiv:2312.11377 (2023) —
  [arXiv API
  query](https://export.arxiv.org/api/query?search_query=abs:%22rule%2030%22&max_results=200&sortBy=submittedDate&sortOrder=descending).

#### Unverified full-solution claims (listed separately, with reasons)
- **Das, M., "Rule 30: Solving the Chaos"**, arXiv:2207.13237 (2022-07-27). Already listed. It claims an analytical
  solution to Problem 1. A search summary describes the argument as a heuristic "randomness count", which does not
  establish aperiodicity. The prize is still listed as open —
  [arXiv](https://arxiv.org/abs/2207.13237).
- **Brauer, L. B. A. (GitHub lba-brauer), "Statistical Randomness in the Central Column of Rule 30"**, repository
  lba-brauer/rule30-symbolic-fsm (created 2025-08-01), with Zenodo DOI 10.5281/zenodo.16730084. It claims to
  "address all three questions of the Rule 30 Prize": Q1 "Non-periodicity ✅", Q2 "Bit balance ✅", Q3 "Computational
  complexity ✅". Reason it is unverified: its methods are "Gaussian statistics and Bernoulli analysis" of finite
  simulations, and the page holds no proof. Licence CC BY-NC-ND 4.0; 0 stars —
  [repository](https://github.com/lba-brauer/rule30-symbolic-fsm).
- **graham medland, Wolfram Community** (2019-12-11 and 12). Claims "an algebraic equation for Rule 30" that runs on a
  four-function calculator. The thread gives no formula, only a figure and a LinkedIn link —
  [thread](https://community.wolfram.com/groups/-/m/t/1802242).
- **Tigran Nersissian, prize submission.** Says he sent a "solution paper" through the prize form around 2026-01-17
  and received no confirmation. His public arXiv papers are partial results (already in the record) —
  [thread](https://community.wolfram.com/groups/-/m/t/1802242).
- **David Gallimore, Wolfram Community** (2024-10-23, 2026-02-04). Says he has worked on a solution for about a year.
  No mathematical content is public —
  [thread](https://community.wolfram.com/groups/-/m/t/1802242).
- **James K. Wiles, "Conditional Patterns in Rule 30 and Their Implications on Computational Reducibility"** (blog,
  2023-08-27). Claims "O(1) computational complexity" for cells inside predictable white triangles. Reason it is not a
  Problem 3 result: such cells are fixed by a local window, which says nothing about the cost of cell n. It has no
  proof and no released code, and its later sections speculate about consciousness —
  [blog
  post](https://jameswiles.com/blog/Conditional-Patterns-in-Rule-30-and-Their-Implications-on-Computational-Reducibility.html).
- **qizwiz/rule30-ski-research, `prize3_from_sensitivity`.** Its conclusion `n + 1 ≤ 2*n + 1` is closed by `omega`
  and never uses its hypothesis, so it proves no lower bound. See Q2 —
  [ConeStructure.lean](https://raw.githubusercontent.com/qizwiz/rule30-ski-research/master/lean_proofs/ConeStructure.lean).

### Inferences
- Since 2019 the arXiv record on the prize problems is thin and already covered by PRIOR-ART.md. The diamonds, if any,
  are in GitHub repositories and forum posts (Q2, Q4, Q5), not in preprints.
- The Problem 3 items found (Natal–Al-saadi, Nersissian's O(log n) query, Wiles) all either speed up full simulation
  or move the cost into precomputation. None bears on period 2.

### Gaps
- The arXiv search used the exact phrase "rule 30" in abstracts. Papers that write "ECA 30", "rule-30" or "elementary
  rule 30" only in the body would be missed. Category listings (nlin.CG, math.DS) were not browsed by hand.
- The full text of Sfairopoulos et al. (2503.19572) was not read.
- Whether Nersissian's Binomial–Lucas row theorems have proofs elsewhere (perhaps in his arXiv companion paper)
  was not checked.

## Q2. Are there formal proofs (Lean, Coq, Isabelle, Agda) of Rule 30 or column results besides Condrey's?

### Takeaway
There is a canonical Lean 4 *statement* of Problems 1 and 2 in Google DeepMind's formal-conjectures (a big group, but
directly usable), and several small independent Lean projects. None formalises a period-2 or column-periodicity
lemma. The independent ones are a harness (Dibujaron), a small scoped development (wryan2986), and one file with a
`sorry` and a vacuous "prize" theorem (qizwiz). No Coq, Isabelle or Agda Rule 30 work was found.

### Cited Findings
- **NEW: google-deepmind/formal-conjectures, `FormalConjectures/Other/Rule30.lean`** (Apache-2.0, 2026). Type:
  formal statements.
  - It defines `step row i = xor (row (i-1)) (row i || row (i+1))` and `state` from a single black cell at 0, and
    `centerColumn t = state t 0`.
  - A sanity theorem `centerColumn_prefix` checks the first 8 values `[true, true, false, true, true, true, false,
    false]` by `decide`.
  - Problem 1 is stated as `answer(sorry) ↔ ¬ ∃ p > 0, ∃ N, ∀ t ≥ N, centerColumn (t+p) = centerColumn t`, and
    Problem 2 as `answer(sorry) ↔ {t | centerColumn t}.HasDensity (1/2)`. Problem 3 is omitted as "model-relative".
  - Verification: statements only, both `sorry` —
    [file](https://raw.githubusercontent.com/google-deepmind/formal-conjectures/main/FormalConjectures/Other/Rule30.lean).
  - Use for period 2: any Lean lemma the project writes, for example "no eventual period 2", could target these exact
    definitions, so that it slots into the community's canonical statement.
- **NEW: Dibujaron/rule30** (GitHub; design documents dated 2026-09-05; about 900 commits; 0 stars). Type:
  formalisation harness.
  - "Formalizing Wolfram's Rule 30 cellular automaton in Lean 4, with a harness that lets Claude agents do the
    proving". The harness, written in Gleam, dispatches one worker per blueprint node and checks the result with
    `lake build` plus an axiom check.
  - The README says proving the prize questions "is not expected". No proved centre-column lemma is visible on the
    README. Its explorer uses `next = (x << 1n) ^ (x | (x >> 1n))`, stated to reproduce A051023.
  - Build status and number of `sorry`s were not determined —
    [repository](https://github.com/Dibujaron/rule30).
- **NEW: wryan2986/rule30-lab** (GitHub, MIT, created 2026-07-22, 138 commits). Type: computation plus a small Lean 4
  development.
  - The one result labelled `partial-proof` is an "explicitly scoped all-one-tail exclusion". Its external width-two
    theorem (Jen/Kopra) "is reviewed informally but is not formalized in Lean".
  - A quality-gate script runs the Lean checks with the C++, CUDA and Rust tests. The theorem names were not visible
    on the page —
    [repository](https://github.com/wryan2986/rule30-lab).
- **NEW: qizwiz/rule30-ski-research, `lean_proofs/ConeStructure.lean`** (82 commits). Type: partial formalisation
  with red flags.
  - Proved without `sorry`: `rule30Local_flip_first` (left-permutivity at one cell), the head-flip lemmas, and
    `left_boundary_full_sensitive` (flipping the leftmost cone cell flips the cone's output, for all n).
  - `all_cells_essential` is `sorry` and labelled "KEY OPEN PROBLEM". There are 24 `native_decide` calls for n ≤ 4.
  - `prize3_from_sensitivity` is vacuous (see Q1). Red flag: input sensitivity of a cone cannot give a Problem 3
    bound, because the single-seed input is just n.
  - [file](https://raw.githubusercontent.com/qizwiz/rule30-ski-research/master/lean_proofs/ConeStructure.lean);
    [repository](https://github.com/qizwiz/rule30-ski-research).
- **NEW: The Last Math Competition, conjecture 00000001243.** The conjecture reads "This sequence [the Rule 30 centre
  column] is not eventually periodic, and among its factors of length < 2^k none contains a square". It was
  disproved in Lean by submitter lidangzzz (2026-09-12) as `tlm1243_false`: the prefix 1,1,0,1 contains the square
  "11".
  - The proof uses `decide`, with no `sorry`, no `native_decide` and no declared axioms (Lean/Mathlib v4.31.0).
  - The competition's acceptance rule is "no `sorry`, no `native_decide`, no extra axioms" plus a semantic review.
  - Value: none for period 2. The conjecture was malformed, and its first clause is Problem 1 itself, untouched —
    [conjecture](https://raw.githubusercontent.com/The-Last-Math-Competition/The-Last-Math-Competition/main/conjectures/00000001243.md);
    [submission](https://raw.githubusercontent.com/The-Last-Math-Competition/The-Last-Math-Competition/main/solutions/00000001243/lidangzzz_submission_20260912/Rule30.lean);
    [competition](https://github.com/The-Last-Math-Competition/The-Last-Math-Competition).
- **Found by code search but not read:**
  - paulklemstine/Lean: `Catalog/Novelty/ECARule30Chaos.lean` and
    `Catalog/Computation/CellularAutomata/FixedPointCounts.lean` (the raw fetch returned 404).
  - the-omega-institute/trureturing: `D5/S0/Automata/RuleThirtyTwentyTwoMersenneSignRefutation.lean`.
  - a second submission to conjecture 1243, by orionsheep.
  - competemath/emissary-archangel holds an export of the DeepMind file —
    [GitHub code search, `"rule 30" theorem
    extension:lean`](https://github.com/search?q=%22rule+30%22+theorem+extension%3Alean&type=code).
- **Condrey's repository, dcondrey/rule30**, still returns HTTP 404 to a plain fetch (as it did on 2026-10-07 in
  PRIOR-ART). A search engine describes it as "Proof-oriented, reproducible research on the Wolfram Rule 30 Prize
  Problems: partial theorems, exact certificates, and audited experiments". A search summary adds that it holds
  "proof-level classifications of the constant-zero and constant-one trace fibers" and only bounded evidence for
  Problems 2 and 3 —
  [repository URL](https://github.com/dcondrey/rule30) (not readable).
- **No Isabelle, Coq or Agda formalisation of Rule 30, or of a column result for any elementary automaton, was found**
  by web search —
  [search results included Dibujaron only](https://github.com/Dibujaron/rule30).

### Inferences
- The most useful formal asset is the DeepMind statement file. It is a fixed, community-maintained target, so a
  project lemma stated against `Rule30.state` and `centerColumn` would be directly comparable. Its `step` puts the
  left neighbour at `i-1`, the same orientation as Rule 30's left-permutivity, so a forced-left-half lemma can be
  stated without mirroring.
- Of the independent Lean work, only one lemma family overlaps the project's machinery: qizwiz's
  `left_boundary_full_sensitive`, a cone-level form of left-permutivity, the basis of Condrey's triangular uniqueness
  and of the project's forced left half. It is small but proved without `sorry`, and could be reused or rewritten.
- For workers: `decide` evaluation of Rule 30 prefixes is kernel-checkable in current Lean/Mathlib (the TLMC
  submission and the DeepMind sanity test both do it). Finite certificates of the project's period-2 searches could
  therefore be checked in Lean without `native_decide` when they are small.

### Gaps
- No Lean file was compiled here. The `sorry` count of Dibujaron/rule30 and wryan2986/rule30-lab is unknown.
- Condrey's repository could not be read: 404 to a plain fetch, and the session's GitHub access does not include it.
- The paulklemstine and omega-institute files are unread.

## Q3. Who has computed the centre column furthest, how was it verified, and what statistics were published?

### Takeaway
The public record is still Wolfram's billion steps (2019). The packed data is in the Wolfram Data Repository, credited
to Xiangdong Wen. No public computation past 10^9 steps was found. Independent groups have computed 10^7 bits on a
GPU (rule30-foundry, already listed) and published density, discrepancy and linear-complexity tables up to 10^5 to
10^6 bits. All are consistent with a random-looking column and none bears on period 2 beyond excluding short periods
with early onsets.

### Cited Findings
- **Wolfram, "Announcing the Rule 30 Prizes"** (2019): "just by running rule 30, we know the sequence doesn't become
  periodic in the first billion steps". Wolfram notes a trillion-step transient is possible —
  [announcement](https://writings.stephenwolfram.com/2019/10/announcing-the-rule-30-prizes/).
- **NEW: Wen, X., "A Billion Bits of the Center Column of the Rule 30 Cellular Automaton"**, Wolfram Data Repository
  (September 2019). Byte-packed, 8 values per byte with the earliest value in the high bit, about 8 GB when unpacked.
  A companion "A Million Bits ..." resource (Wolfram, 2017) matches NKS page 871. Both are linked from OEIS A051023.
  Verification method not stated in what was seen —
  [billion
  bits](https://datarepository.wolframcloud.com/resources/A-Billion-Bits-of-the-Center-Column-of-the-Rule-30-Cellular-Automaton);
  [million
  bits](https://datarepository.wolframcloud.com/resources/A-Million-Bits-of-the-Center-Column-of-the-Rule-30-Cellular-Automaton);
  [OEIS A051023](https://oeis.org/A051023).
- **NEW: OEIS A051023.**
  - The b-file runs n = 0..100000 (Antti Karttunen; terms 0..10000 from Reinhard Zumkeller).
  - Comments: A092539 gives the prefix as a binary number (Zumkeller, 2013), and the sequence is also the middle
    column of rule 86 (Karttunen, 2019).
  - Nothing on periodicity, density or proofs. Links include Jen (1986) and Pedro Hecht, "PQC: R-Propping a Chaotic
    Cellular Automata" (Univ. Buenos Aires, 2021; post-quantum cryptography, not prize-relevant) —
    [OEIS A051023](https://oeis.org/A051023).
- **Already listed, new numbers: Patto1155/rule30-foundry** (created 2026-03-27). A 10M-bit centre column on a
  GTX 1060 regenerates byte-identically, and an independent CPU implementation reproduces it. Tape width
  21,000,000, 10,000,000 steps, about 6 minutes. "No period p ≤ 5,000,000 in the first 10M bits", and no linear or
  Markov shortcut found —
  [repository](https://github.com/Patto1155/rule30-foundry) (search summary).
- **NEW: cochon123/rule30-prize** (created 2026-09-10; README: "No prize claim").
  - Ones in prefixes: 52 of 100, 481 of 1,000, 5,032 of 10,000, 50,098 of 100,000 (signed discrepancy 4, −38, 64,
    196).
  - For every period 1..4096 the smallest last-mismatch time is 95,902, so those periods are excluded only for onsets
    at or before 95,902.
  - Linear complexity from Berlekamp–Massey-type fits: 48 at 100 bits, 500 at 1,000, 5,001 at 10,000, 10,000 at
    20,000.
  - "Adaptive circuit lower bounds C(128) ≥ 6438, C(256) ≥ 27139", with no definition of C on the page seen —
    [REPORT.md](https://raw.githubusercontent.com/cochon123/rule30-prize/main/REPORT.md);
    [research/LOG.md](https://raw.githubusercontent.com/cochon123/rule30-prize/main/research/LOG.md).
- **NEW: wryan2986/rule30-lab.**
  - Reproduces the million-bit data independently, with balance checkpoints from 100 to 1,000,000 bits.
  - Linear complexity on 5,000 bits, automaticity searches at levels 1 to 9, and Python, C++ (AVX2), Rust and CUDA
    paths matched against shared vectors (10,000 trusted centre bytes; full rows to step 255).
  - Compute Sanitizer is excluded from the success claim because it failed under WSL —
    [repository](https://github.com/wryan2986/rule30-lab).
- **NEW: beedbyte/rule30-research** (created 2026-10-08, 2 commits).
  - Cell-by-cell and integer-bitset evolvers in Python. Tests compare 512 centre bits between the two and 1,024
    against a third, moving-frame recurrence.
  - "No finite computation proves a statement about all future times"; "not a Rule 30 prize submission" —
    [repository](https://github.com/beedbyte/rule30-research).
- **Already listed: fabianxvogt/rule30.** No eventual period up to 2,048 in the first million bits (PRIOR-ART). A
  search summary also mentions "saturation at ~4.6M steps for h=22", meaning unclear —
  [repository](https://github.com/fabianxvogt/rule30) (search summary).
- **Not opened:** Wolfram Notebook Archive, "Analysis of Black and White Cells in the Center Column of Rule 30"
  (2019-09) —
  [notebook](https://www.notebookarchive.org/analysis-of-black-and-white-cells-in-the-center-column-of-rule-30--2019-09-dtysya8/).

### Inferences
- The published linear-complexity profile (about N/2 at N = 100 to 20,000) is what a random sequence gives. An
  eventually periodic column would show bounded linear complexity past its onset, so these tables are an
  independent check of "no period up to about 10^4 with early onset", nothing more.
- For period 2 the finite searches add nothing beyond the project's own ladder. A 10^7- or 10^9-bit prefix already
  rules out period 2 with onset below that length. The open case is a late onset, which no prefix computation reaches.
- Discrepancy 196 at 10^5 (about 0.6·√N) is unremarkable for Problem 2. Wolfram's own Problem 2 table in the
  announcement remains the long-range source.

### Gaps
- No computation past 10^9 bits was found. Nobody was found to have independently re-verified the billion-bit data
  (for example by hash comparison).
- OEIS A070950 (the triangle) was not fetched, so its comments and references are unchecked.
- The meaning of cochon123's circuit measure C(n) was not determined.

## Q4. Are there SAT/SMT or exhaustive-search projects on Rule 30 columns or periodic configurations, with certificates?

### Takeaway
No SAT work on Rule 30 columns by Heule or another academic group was found. The closest is an independent,
agent-run repository (cochon123/rule30-prize). It reports SAT- and enumeration-based kills of period-2 onsets up to
width 28, a certificate excluding isolated-zero eventual periods 0 1^q for q = 7 and every q ≥ 9, and a conditional
16-state tail machine. If its scope holds, the 0 1^q family is the most concrete new period-exclusion claim in this
survey, and it deserves an audit. Its scope (strip models or the single seed) is not stated clearly.

### Cited Findings
- **NEW: cochon123/rule30-prize** (created 2026-09-10; it says its work was done by agents, with a coordinating
  agent checking arguments). Type: exhaustive search, SAT and finite certificates. Not checked by anyone outside, as
  far as could be found.
  - *Constant tails (proved, elementary).* "Infinitely many 0s and 1s in the centre are proved" via Jen's two-column
    theorem.
    - Eventually 1: the left neighbour is forced eventually 0.
    - Eventually 0: the left and right neighbours are equal, and the right column satisfies a non-decreasing
      recurrence, so it is eventually constant.
    - Their write-up scopes it to the single seed —
      [REPORT.md](https://raw.githubusercontent.com/cochon123/rule30-prize/main/REPORT.md);
      [nonperiodicity.md](https://raw.githubusercontent.com/cochon123/rule30-prize/main/nonperiodicity.md).
  - *Period 2, local relations.* With centre 0 at even and 1 at odd times: l_t = 1 at odd t, r_t = ¬l_t at even t,
    and l_(t+1) = r_t ∨ e_t, where e is column 2. For q_n = l_(T+2n), q_n = 0 forces q_(n−1) = q_(n+1) = 1. "Period 2
    therefore remains open under this local analysis" —
    [nonperiodicity.md](https://raw.githubusercontent.com/cochon123/rule30-prize/main/nonperiodicity.md).
  - *Period 2, onset widths.* "On-demand SAT gives finite L_0 lifetime for every 1<=T<=16" (Cycle B). A "sound onset
    enumeration ... kills every onset width T=1..28", longest extra R = 16 at T = 20 (Cycle C). "No uniform-in-T
    bound". Scripts: period2_vacuum.py, with notes period2_neighbor.md and period2_left_edge.md —
    [research/LOG.md](https://raw.githubusercontent.com/cochon123/rule30-prize/main/research/LOG.md).
  - *Conditional tail machine.* For an "eventually-zero Fibonacci u", F_k becomes "eventually equal to k mod 2" via a
    "16-state tail machine, absorb in at most 9 columns", so L_0 is impossible for those u. This is conditional on an
    eventually zero right neighbour —
    [research/LOG.md](https://raw.githubusercontent.com/cochon123/rule30-prize/main/research/LOG.md);
    [REPORT.md](https://raw.githubusercontent.com/cochon123/rule30-prize/main/REPORT.md).
  - *Isolated-zero periods.* "for q=7 and every q>=9, the radius-6 strip has a unique recurrent component whose left
    neighbor is periodic, so Jen/Kopra exclude that eventual center".
    - q ≥ 17 is handled by a finite gadget ("14-state cruise plus wrap-through-zero"), and 9 ≤ q ≤ 16 by finite
      graphs.
    - "Period 9 (q=8) is a genuine exception". Open: q ∈ {1,…,6, 8}, that is eventual periods 2 to 7 and 9 of this
      form.
    - Certificate: isolated_zero_uniform.py, "checked through q=40"; proof in isolated_zero_uniform.md.
    - The log warns elsewhere that strip survivors are not claimed to extend to the single-seed space-time —
      [research/LOG.md](https://raw.githubusercontent.com/cochon123/rule30-prize/main/research/LOG.md);
      [README](https://github.com/cochon123/rule30-prize).
  - Red flags: the scope of each certificate is unclear. The code was not run here. The GitHub listing shows over
    700 pull requests that were not inspected.
- **NEW: wryan2986/rule30-lab.** "Sideways reconstruction" tests eventually periodic centre traces in a finite search
  (horizon 500, maximum period 10). "No depth-independent state bound has been proved" —
  [repository](https://github.com/wryan2986/rule30-lab).
- **Already listed: woahwhattheheck/commons issue 15314 and PR 15318.** NEW sibling: issue 15523, "Research: Rule 30
  center-column equal-frequency prize (10,000 US dollars advertised)". A search summary says its status fields record that "no
  prize theorem or award has been established". The page returned 404 to a direct fetch —
  [issue 15523](https://github.com/woahwhattheheck/commons/issues/15523) (search summary only).
- **No Heule, SAT or SMT project on Rule 30 columns was found.** A search for SAT with elementary automata, periodic
  orbits, Rule 30, Heule or Sutner surfaced only a CA *control* problem cast as SAT, and the papers already in the
  record —
  [search hit: Natal–Al-saadi](https://arxiv.org/pdf/2409.07065); [Condrey](https://arxiv.org/pdf/2609.09431).
- **Low-value, search summary only:** GitHub issues in deepseek-launch-community/XuanJi-ISA (#153, #156) are "Draft
  v1.0 — workshop paper" texts fitting Rule 30's maximum preimage growth at c_30 = 1.56 or 1.563. The two drafts
  disagree with each other on rule 45 —
  [issue 153](https://github.com/deepseek-launch-community/XuanJi-ISA/issues/153);
  [issue 156](https://github.com/deepseek-launch-community/XuanJi-ISA/issues/156).

### Inferences
- **The cochon123 constant-tail argument shortens the period-1 proof.** Checked by hand here. Rule 30 reads
  x_(t+1)(i) = x_t(i−1) ⊕ (x_t(i) ∨ x_t(i+1)).
  - Centre eventually 1: then x_t(−1) = 0 eventually.
  - Centre eventually 0: then x_t(−1) = x_t(1) and x_(t+1)(1) = x_t(1) ∨ x_t(2) ≥ x_t(1), so column 1 is monotone,
    hence eventually constant.
  - Either way two adjacent columns are eventually constant. That contradicts Kopra's Corollary 3.7 for *every*
    configuration whose left half is eventually zero, not only the single seed (scope as recorded in PRIOR-ART.md).
  - So Condrey's period-1 theorem, and more, follows in a few lines from Kopra (2023). The monotone step appears to be
    in the record already: RULE30-PRIZE.md proposes to extend Condrey's "monotonicity (next to a constant wall,
    column 1 can only turn black once)". Workers should confirm that the two-line proof via Kopra is written down, as a
    check on
    how much of period 1 is cheap.
- **The isolated-zero result is the item most worth a second reader.** The project's period-2 trace is 0101... =
  (0 1^1)^∞, the q = 1 case, which cochon123 leaves open. A valid exclusion for q = 7 and every q ≥ 9 would be a new
  infinite family of excluded eventual periods: the words 0 1^q, periods 8, 10, 11, ....
  - It works through the same mechanism as the project: force column −1 to be periodic, then apply Jen/Kopra.
  - Why q ≤ 6 and q = 8 resist a radius-6 strip may say something about why period 2 resists.
  - Before any use: confirm that isolated_zero_uniform.py's strip model covers all finite configurations (or at least
    the single seed), and rerun it.
- The period-2 onset kills (T ≤ 28, "no uniform bound") match Condrey's H(2,w) ≥ w and the project's own finding that
  no constant bound governs period 2. They are independent confirmation, not a new lever.

### Gaps
- isolated_zero_uniform.md/.py, period2_vacuum.py and the "Fibonacci u" definition were not read or run. The scope of
  the certificates is unconfirmed.
- No academic SAT or exhaustive-search paper on Rule 30 column periodicity was found. If one exists under other
  terms, such as "trace subshift" or "column factor", these searches missed it.

## Q5. Are there useful answers on MathOverflow, Math StackExchange or Wolfram Community that prove lemmas about Rule 30
columns, diagonals or permutive rules?

### Takeaway
Two forum items have checkable content. The first is Johan Kopra's MathOverflow answer: by a published table, Rule 30
has no configuration of minimal temporal period 2 on the whole line. A ring count here confirms the table for periods
1 to 4. The second is a pair of Math SE questions measuring how a single cell spreads into a 0101... background,
exactly the project's period-2 wall. That pair has a numerical constant near 1.624 and no explanation. The Wolfram
Community thread's one lemma (Brunnbauer's, on right diagonals) restates Jen and Rowland.

### Cited Findings
- **NEW: MathOverflow 429509, "'Rule 30' in the infinite setting"** (Dominic van der Zypen, 2022-08-31). For which n
  is there x ∈ {0,1}^ℤ with F^n(x) = x and F^k(x) ≠ x for 0 < k < n?
  - Accepted answer by Johan Kopra (2022-09-01): "Table A.1 of https://core.ac.uk/download/pdf/236376428.pdf lists
    the number of preperiodic points with minimal preperiod q and minimal period p".
  - For Rule 30 with q = 0 and p = 1..6 the counts are "3,0,12,28,45,84 and in particular there does not exist a
    configuration with minimal period 2" —
    [Stack Exchange API record of the question and
    answer](https://api.stackexchange.com/2.3/questions/429509/answers?site=mathoverflow&filter=withbody).
  - The cited PDF returned 403 and its title and author were not identified.
- **Check run for these notes (prediction: if the table is right, rings give 3, 0, 12, 28 for p = 1..4).** Each
  configuration of minimal spatial period n ≤ 24 was counted once, with F^p x = x and p minimal.
  - Result: p = 1: 3 (spatial periods 1 and 2), p = 2: 0, p = 3: 12 (spatial period 12), p = 4: 28 (spatial period
    7), p = 5: 20 so far (5 at spatial period 5, 15 at 15), p = 6: 0 so far.
  - So the table is confirmed for p = 1..4, including the absence of period 2, among spatial periods up to 24. The
    remaining 25 points of period 5 and 84 of period 6 must have spatial periods above 24. That is consistent with
    the table, not a contradiction.
  - Counterfactual: a nonzero p = 2 count would have contradicted the answer. The code (C, written for these notes)
    follows. Source of the table values: the
    [API record](https://api.stackexchange.com/2.3/questions/429509/answers?site=mathoverflow&filter=withbody).
    ```c
    // Count Rule 30 points of Z with minimal spatial period n (each counted once) and minimal temporal
    // period p <= 6. Bit i = cell i; new(i) = old(i-1) ^ (old(i) | old(i+1)). Run: ./ringper 24
    #include <stdio.h>
    #include <stdint.h>
    #include <stdlib.h>
    int n; uint64_t M;
    static uint64_t rotl(uint64_t v,int k){k%=n; if(!k) return v; return ((v<<k)|(v>>(n-k)))&M;}
    static uint64_t F(uint64_t v){return rotl(v,1)^(v|rotl(v,n-1));}
    int main(int c,char**a){int NMAX=atoi(a[1]); long tot[7]={0};
     for(n=1;n<=NMAX;n++){M=(1ULL<<n)-1; long row[7]={0};
      for(uint64_t x=0;x<=M;x++){int prim=1;
       for(int d=1;d<n;d++) if(n%d==0 && rotl(x,d)==x){prim=0;break;}
       if(!prim) continue; uint64_t y=x;
       for(int p=1;p<=6;p++){y=F(y); if(y==x){row[p]++;tot[p]++;break;}}}
      printf("%d:",n); for(int p=1;p<=6;p++) printf(" %ld",row[p]); printf("\n");}
     printf("total p=1..6:"); for(int p=1;p<=6;p++) printf(" %ld",tot[p]); printf("\n");}
    ```
    Output totals for n ≤ 24: `3 0 12 28 20 0`. The three fixed points are 0^∞ and the two phases of (01)^∞. The
    alternating background is itself a fixed point of Rule 30.
- **MathOverflow 164486, "Is rule 30 Turing complete? Is there a proof that it isn't?"** (N. Virgo, 2014). Accepted
  answer by Algernon: no proof either way. It points to Sutner (MCU 2004), Ollinger (JAC 2008),
  Delvenne–Kůrka–Blondel (2006) and Di Lena–Margara (2008) on defining universality —
  [API record](https://api.stackexchange.com/2.3/questions/164486/answers?site=mathoverflow&filter=withbody).
- **NEW: Math SE 4497595, "Golden Ratio appears in this Rule 30 variation?"** (Trevor, 2022-07-21, score 25). Start a
  single 1 on a background of repeating 01. The pattern "only expands to fill a portion of its right side", and the
  ratio of the structured part of each row to the alternating cells before it appeared to approach φ ≈ 1.618, plotted
  through 600k rows.
  - Follow-up **Math SE 4832480, "Rule 30 Variation, revisited: Where does the constant come from?"** (mell_o_tron,
    2023-12-23). The earlier answer found the ratio instead heading for a larger value: "The 999000th computed value
    was 1.62414531", and the mean of the last 30 reported values is 1.6240807783333333. The asker wants an
    explanation, and the API listed no answer —
    [API record of both
    questions](https://api.stackexchange.com/2.3/questions/4497595;4832480?site=math&filter=withbody).
- **NEW: Math SE 4141181, "Periodic columns in asymmetrical 1D cellular automata?"** (Trevor, 2021-05-16). It asks
  for a two-colour rule that is not symmetric, with an aperiodic initial configuration and at least one, but finitely
  many, eventually periodic columns. It is motivated by Rule 30. One answer exists; it was not read (API rate limit;
  the site blocks direct fetches) —
  [API record](https://api.stackexchange.com/2.3/questions/4141181?site=math&filter=withbody).
- **Math SE 3969403, "Can information transmission be proven in a Rule 30 ECA?"** (Trevor, 2021-01-01). It proposes
  a light-cone argument against a transient-then-periodic centre and has no answers. **Math SE 3635888** (2020) asks
  about a thesis's "basic transition automaton" for ECA 30 (one answer, unread). **Math SE 3468724** (2019) asks to
  prove B2 = MOD(A1 + B1 + (1+B1)·C1, 2), which is Rule 30's algebraic normal form —
  [API search](https://api.stackexchange.com/2.3/search/advanced?order=desc&sort=relevance&q=%22rule%2030%22&site=math).
- **Wolfram Community, "Wolfram's Rule 30 contest"** (opened by Todd Rowland, 2019-10-05).
  - Michael Brunnbauer (2019-12-11, 16) claims "The necessary and sufficient condition for period doubling of
    diagonals from the right is established", and that right-diagonal periods never decrease, because each right
    diagonal is the previous diagonal XOR the OR of two earlier ones. He doubts it is new.
  - Todd Rowland replies it "sounds familiar from a talk by Eric Rowland" —
    [thread](https://community.wolfram.com/groups/-/m/t/1802242).
  - PRIOR-ART.md lists "Brunnbauer 2019 (diagonals only)" as a search term without content. The content is now
    known and is subsumed by Jen's 2^α right-diagonal periods and Rowland §5.
- **Wolfram Community, pronic-position formula** (2019, search summary only). A post proposes a centre-column formula
  of XOR and OR evaluated at pronic positions k(k+1), checked in Python against the first 256 rows, and asks whether
  it helps the prizes. It shows no answer. It was not found in the fetched copy of thread 1802242 and may be on the
  newer forum URL —
  [community.wolfram.com/t/wolframs-rule-30-contest/14814](https://community.wolfram.com/t/wolframs-rule-30-contest/14814)
  (search summary).

### Inferences
- **Kopra's table gives a cheap global fact for the period-2 write-up.** No bi-infinite Rule 30 space-time has
  temporal period 2. So an eventually period-2 centre can never sit in a configuration that is itself eventually
  temporally 2-periodic. Jen/Kopra already implies the neighbouring columns are not eventually periodic, so this is a
  consistency anchor, not a lever.
- **The 0101-background spread constant (about 1.624) is a free measurement of the project's own wall.** A single
  defect in the 0101... domain (a fixed point of Rule 30, by the ring count above) advances into it at a rate that
  two Math SE users measured through about 10^6 rows. The project
  has its own front-speed numbers next to a clamped 0101 column (PRIOR-ART: 0.21 cells per step leftwards).
  - Tentative: the two set-ups differ, since the forum's background is not clamped and the ratio's definition was not
    read in full. Matching the definitions, and asking whether 1.624 is algebraic (for example a root tied to the
    17/56 wheel), is a small, well-posed side question for CONSTELLATION.md, not the main line.
- Trevor's 4141181 is Kopra's page-7 barrier asked as a question: is there an asymmetric rule with a lone periodic
  column? Its unread answer may hold a concrete example, which would be useful as a non-Rule-30 test case for the
  project's templates.

### Gaps
- The answers on Math SE 4141181, 4497595, 3635888, 3634600 and 1727825 were not read. The Stack Exchange API
  rate-limited this IP for about 4.4 hours, and direct page fetches are blocked here.
- cstheory.stackexchange was not searched (rate limit).
- The core.ac.uk thesis behind Kopra's Table A.1 is unidentified (HTTP 403). The p = 5 and p = 6 counts (45, 84) were
  confirmed only partly (20 and 0 among spatial periods ≤ 24).
- Wolfram Community was not searched exhaustively. Other threads, such as the "Submit a Solution" discussions and
  the newer forum's Rule 30 tags, may hold more.
