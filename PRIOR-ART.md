# Prior art: the published work behind the research

> **What this is (2026-10-22).** The published work found before each step of the research, and what each result does and does not cover, filed as dated sections, newest last. It also holds the source receipts for individual results, and the known theorems the record proved again for itself ("known, reproved here", AGENTS.md item 22). Until the spring clean of 2026-10-22 this file began with the N-Frame video project's surveys of 2026-08-31 to 2026-10-01; they are now [nframe/PRIOR-ART-NFRAME.md](nframe/PRIOR-ART-NFRAME.md), unchanged, and shader comments that cite "PRIOR-ART.md" mean that file. Each section below is as it was filed.

## Contents

*The sections, in the order they were filed (2026-10-04 onward). From 2026-10-18 on, new sections were filed as
`###` subsections under the last heading; they are listed beneath it.*

- [Before rung 2's leap: periodic columns of Rule 30 (surveyed 2026-10-04, 23:15, by Cloud)](#before-rung-2s-leap-periodic-columns-of-rule-30-surveyed-2026-10-04-2315-by-cloud)
- [Before the particle step: domains and particles (surveyed 2026-10-05, by Cloud)](#before-the-particle-step-domains-and-particles-surveyed-2026-10-05-by-cloud)
- [Before the kick-game step: the wheel, phase locking, and recent Rule 30 work (surveyed 2026-10-05, by Cloud)](#before-the-kick-game-step-the-wheel-phase-locking-and-recent-rule-30-work-surveyed-2026-10-05-by-cloud)
- [The owner's PRNG question: Rule 30 as a generator, and its cryptanalysis (surveyed 2026-10-05, by Cloud)](#the-owners-prng-question-rule-30-as-a-generator-and-its-cryptanalysis-surveyed-2026-10-05-by-cloud)
- [Before the bottleneck and entropy steps: information flow in Rule 30 (surveyed 2026-10-05, by Cloud)](#before-the-bottleneck-and-entropy-steps-information-flow-in-rule-30-surveyed-2026-10-05-by-cloud)
- [The owner's lightning, channels and maze: directed polymers and directed percolation (surveyed 2026-10-05, by Cloud)](#the-owners-lightning-channels-and-maze-directed-polymers-and-directed-percolation-surveyed-2026-10-05-by-cloud)
- [After the diagonals and the band: what was already known (surveyed 2026-10-05, by Cloud, after the runs)](#after-the-diagonals-and-the-band-what-was-already-known-surveyed-2026-10-05-by-cloud-after-the-runs)
- [Before and after the entropy squeeze: column entropy (surveyed 2026-10-05, by an independent review session)](#before-and-after-the-entropy-squeeze-column-entropy-surveyed-2026-10-05-by-an-independent-review-session)
- [After the merging census: merging walks and the coin's maximum (surveyed 2026-10-05, by Cloud, after the runs)](#after-the-merging-census-merging-walks-and-the-coins-maximum-surveyed-2026-10-05-by-cloud-after-the-runs)
- [The owner's zeta note: the prime-gap parallel (surveyed 2026-10-05, by Cloud)](#the-owners-zeta-note-the-prime-gap-parallel-surveyed-2026-10-05-by-cloud)
- [After the wheel dig: Rule 30's siblings in arithmetic (surveyed 2026-10-05, by Cloud)](#after-the-wheel-dig-rule-30s-siblings-in-arithmetic-surveyed-2026-10-05-by-cloud)
- [The owner's wide survey: nature, biology and the other disciplines (surveyed 2026-10-05, by Cloud)](#the-owners-wide-survey-nature-biology-and-the-other-disciplines-surveyed-2026-10-05-by-cloud)
- [After the window principle: the Collatz complexity bound is Dubickas's (checked 2026-10-05, by Local through a search agent)](#after-the-window-principle-the-collatz-complexity-bound-is-dubickass-checked-2026-10-05-by-local-through-a-search-agent)
- [openai/math: a released collection of model-proved manuscripts (noted 2026-10-07, by Cloud)](#openaimath-a-released-collection-of-model-proved-manuscripts-noted-2026-10-07-by-cloud)
- [The move to a finite window, read at the source: Bugeaud and Dubickas (read 2026-10-07, by Local, for Q2)](#the-move-to-a-finite-window-read-at-the-source-bugeaud-and-dubickas-read-2026-10-07-by-local-for-q2)
- [Kari-Kopra unavoidable-hole proof receipt (2026-10-09, GPT; GC670)](#kari-kopra-unavoidable-hole-proof-receipt-2026-10-09-gpt-gc670)
- [Overlooked work: theses, small groups and independents (surveyed 2026-10-09 15:46 BST, by Cloud's research subagents)](#overlooked-work-theses-small-groups-and-independents-surveyed-2026-10-09-1546-bst-by-clouds-research-subagents)
- [Kopra width-one comparison resolved (2026-10-09, GPT; GC807)](#kopra-width-one-comparison-resolved-2026-10-09-gpt-gc807)
- [Right-edge odometer application independently audited (2026-10-09, GPT; GC808)](#right-edge-odometer-application-independently-audited-2026-10-09-gpt-gc808)
- [Sablik closing application checked directly (2026-10-09, GPT; GC813)](#sablik-closing-application-checked-directly-2026-10-09-gpt-gc813)
- [Two survey gaps closed by the owner's finds (2026-10-09, Cloud)](#two-survey-gaps-closed-by-the-owners-finds-2026-10-09-cloud)
- [AI-driven formal proof search, and Lean as the last check (noted 2026-10-11, by Cloud at the owner's request)](#ai-driven-formal-proof-search-and-lean-as-the-last-check-noted-2026-10-11-by-cloud-at-the-owners-request)
- [Re-survey for door 3, the number view (2026-10-14 01:19 BST, Local; loop check 3, L703)](#re-survey-for-door-3-the-number-view-2026-10-14-0119-bst-local-loop-check-3-l703)
- [Mahler's 3/2 problem: survey at the room switch (2026-10-14 07:46 BST, Local; L707, L708)](#mahlers-32-problem-survey-at-the-room-switch-2026-10-14-0746-bst-local-l707-l708)
- [Turing (1936), read at the owner's request (2026-10-14 07:58 BST, Local)](#turing-1936-read-at-the-owners-request-2026-10-14-0758-bst-local)
- [Dubickas–Mossinghoff comparison: targeted GPT second read (2026-10-14 09:59 BST)](#dubickasmossinghoff-comparison-targeted-gpt-second-read-2026-10-14-0959-bst)
- [L711 citation and novelty checks: GPT (2026-10-14 11:00 BST)](#l711-citation-and-novelty-checks-gpt-2026-10-14-1100-bst)
- [GPT sign-rule countercheck: bounded attribution search (2026-10-14; GC1246)](#gpt-sign-rule-countercheck-bounded-attribution-search-2026-10-14-gc1246)
- [GPT nonlinear ternary converse: bounded prior-art check (2026-10-14 21:46 BST; GC1248-1249)](#gpt-nonlinear-ternary-converse-bounded-prior-art-check-2026-10-14-2146-bst-gc1248-1249)
- [8.116 door D2, the sharp form: finite-seed normal or simply normal columns of elementary rules (Local, 2026-10-15 14:44 BST; L739, L740)](#8116-door-d2-the-sharp-form-finite-seed-normal-or-simply-normal-columns-of-elementary-rules-local-2026-10-15-1444-bst-l739-l740)
- [Fixed-cardinality sums of an interval — known,reproved here (2026-10-17;MI304)](#fixed-cardinality-sums-of-an-interval--knownreproved-here-2026-10-17mi304)
- [SS target exchange geometry — known,reproved here (2026-10-17;MI321)](#ss-target-exchange-geometry--knownreproved-here-2026-10-17mi321)
- [Higher Lawrence fibers — scope note (2026-10-17;MI321)](#higher-lawrence-fibers--scope-note-2026-10-17mi321)
- [One-deletion subset spectra: elementary interval consequence (2026-10-17,GPT;MI333)](#one-deletion-subset-spectra-elementary-interval-consequence-2026-10-17gptmi333)
- [Three-bin full-interval existence: known in the record,reproved here (2026-10-17 20:30 BST;MI335)](#three-bin-full-interval-existence-known-in-the-recordreproved-here-2026-10-17-2030-bstmi335)
- [Bounded source-scope check: compatible boundaries in a different group (2026-10-17 20:30 BST;MI335)](#bounded-source-scope-check-compatible-boundaries-in-a-different-group-2026-10-17-2030-bstmi335)
- [Adjacent-pair subset-sum completion (2026-10-17 23:55 BST;MI353)](#adjacent-pair-subset-sum-completion-2026-10-17-2355-bstmi353)
- [Fixed-count interval allocations and convex sums (2026-10-18;MI442)](#fixed-count-interval-allocations-and-convex-sums-2026-10-18mi442)
- [Integral rank splitting via discrete separation (GPT, 2026-10-18; MI448)](#integral-rank-splitting-via-discrete-separation-gpt-2026-10-18-mi448)
  - [Tan–Teh's seven-path exception: pair-count interpretation (GPT, 2026-10-18; MI450)](#tantehs-seven-path-exception-pair-count-interpretation-gpt-2026-10-18-mi450)
  - [One size-two row: source scope (GPT, 2026-10-18; MI451–452)](#one-size-two-row-source-scope-gpt-2026-10-18-mi451452)
  - [Pair-sum doorway is a permutation X-ray problem (GPT, 2026-10-18; MI467–470)](#pair-sum-doorway-is-a-permutation-x-ray-problem-gpt-2026-10-18-mi467470)
  - [X-ray decomposition source check (GPT,2026-10-19; MI480)](#x-ray-decomposition-source-check-gpt2026-10-19-mi480)
  - [L8 publication-status follow-up (GPT,2026-10-19; MI487)](#l8-publication-status-follow-up-gpt2026-10-19-mi487)
  - [L8 novelty pass: citation chain and odd-sum partition results (Cloud, 2026-10-19; GC1595's narrowed B)](#l8-novelty-pass-citation-chain-and-odd-sum-partition-results-cloud-2026-10-19-gc1595s-narrowed-b)
  - [Exact two-size2 obstruction versus the equal-sum slice (GPT, 2026-10-20; MI515–516)](#exact-two-size2-obstruction-versus-the-equal-sum-slice-gpt-2026-10-20-mi515516)
  - [Equal-pair consumption as a known ingredient (GPT, 2026-10-20; MI519–520)](#equal-pair-consumption-as-a-known-ingredient-gpt-2026-10-20-mi519520)
  - [Two-colour pair quotas and Exact Matching (GPT, 2026-10-20; MI521–522)](#two-colour-pair-quotas-and-exact-matching-gpt-2026-10-20-mi521522)
  - [Two reflections and interval path coordinates (GPT, 2026-10-20; MI525–526)](#two-reflections-and-interval-path-coordinates-gpt-2026-10-20-mi525526)
  - [Two-target quota hulls and known polygon edge merging (2026-10-20; MI532–533)](#two-target-quota-hulls-and-known-polygon-edge-merging-2026-10-20-mi532533)
  - [Mixed decomposition is stronger than the source's repeated-polytope IDP (2026-10-20; MI534)](#mixed-decomposition-is-stronger-than-the-sources-repeated-polytope-idp-2026-10-20-mi534)
  - [Three perfect colour matchings are not three distinct sum fibres (2026-10-20; MI535–536)](#three-perfect-colour-matchings-are-not-three-distinct-sum-fibres-2026-10-20-mi535536)
  - [AP sum graphs and known perfect-matching switches (2026-10-20; MI537–538)](#ap-sum-graphs-and-known-perfect-matching-switches-2026-10-20-mi537538)
  - [Remaining four-bin count classes: source scope (2026-10-20; MI544)](#remaining-four-bin-count-classes-source-scope-2026-10-20-mi544)
  - [Minimum-mean zero ownership for the missing1 child (2026-10-20; MI549)](#minimum-mean-zero-ownership-for-the-missing1-child-2026-10-20-mi549)
  - [Joint count/moment selection: bounded source audit (2026-10-20; MI553)](#joint-countmoment-selection-bounded-source-audit-2026-10-20-mi553)
  - [Four-variable count bounds and integer parity (2026-10-20; MI555)](#four-variable-count-bounds-and-integer-parity-2026-10-20-mi555)
  - [Real count projection by interval elimination (2026-10-20; MI557–558)](#real-count-projection-by-interval-elimination-2026-10-20-mi557558)
  - [Balanced collections and the real count selector (2026-10-20; MI560)](#balanced-collections-and-the-real-count-selector-2026-10-20-mi560)
  - [Convex knapsack extrema with the integer budget retained (2026-10-20; MI564)](#convex-knapsack-extrema-with-the-integer-budget-retained-2026-10-20-mi564)
  - [Largest-remainder count rounding (2026-10-20; MI569–570)](#largest-remainder-count-rounding-2026-10-20-mi569570)
  - [Fractional count projection versus inward rounding (2026-10-20; MI571)](#fractional-count-projection-versus-inward-rounding-2026-10-20-mi571)
  - [Four-label balanced collections: the grand-coalition convention (MI576–577, 2026-10-20)](#four-label-balanced-collections-the-grand-coalition-convention-mi576577-2026-10-20)
  - [Grouped tournament scores and a bounded-support candidate (MI584, 2026-10-21)](#grouped-tournament-scores-and-a-bounded-support-candidate-mi584-2026-10-21)
  - [Unit rank-gate reuse for tournament absorption (MI586–587, 2026-10-21)](#unit-rank-gate-reuse-for-tournament-absorption-mi586587-2026-10-21)
  - [Quantitative small-slack chain in one full interval (MI588–589, 2026-10-21)](#quantitative-small-slack-chain-in-one-full-interval-mi588589-2026-10-21)
  - [Colour potentials for a tournament's linearized objective (MI592, 2026-10-21)](#colour-potentials-for-a-tournaments-linearized-objective-mi592-2026-10-21)
  - [Paired component paths and the six-vertex refinement (MI593, 2026-10-21)](#paired-component-paths-and-the-six-vertex-refinement-mi593-2026-10-21)
  - [Strongness under a score permutation (MI594, 2026-10-21)](#strongness-under-a-score-permutation-mi594-2026-10-21)
  - [Bounded rank excess and a forced filler tail (2026-10-21, MI598)](#bounded-rank-excess-and-a-forced-filler-tail-2026-10-21-mi598)
  - [First-bin binary fibres versus positive-marginal logistic fibres (2026-10-21; MI602)](#first-bin-binary-fibres-versus-positive-marginal-logistic-fibres-2026-10-21-mi602)
  - [Endpoint-anchored pair covers for a deletion budget (2026-10-21; MI610)](#endpoint-anchored-pair-covers-for-a-deletion-budget-2026-10-21-mi610)
  - [rStation Collatz papers, read as prior art only (2026-10-21, Cloud; CL485)](#rstation-collatz-papers-read-as-prior-art-only-2026-10-21-cloud-cl485)
  - [Cross-intersecting linear families: scope check for the child-triple question (2026-10-22 09:33 BST, GPT, MI621)](#cross-intersecting-linear-families-scope-check-for-the-child-triple-question-2026-10-22-0933-bst-gpt-mi621)

## Before rung 2's leap: periodic columns of Rule 30 (surveyed 2026-10-04, 23:15, by Cloud)

Scope: what is known about a column of a finite Rule 30 configuration being eventually periodic, and especially
about period two, before RULE30-PRIZE.md §8.2's next step (naming the templates). Sources were checked tonight by
web search and by reading them. "(abstract)" means only an abstract or a summary was read.

### Summary

Period one is closed (Condrey, 2026-09-08). Period two is open and is being worked on in public: a bounded search
like our rung 1, and the same "remaining inference" as our Conjecture B in its weak form. Two of this project's results
were already known: the forced left half (Condrey's "triangular uniqueness", by left-permutivity) and the fact that
no constant bound governs period two. Our two-sided measurements, the four arms, Lemmas 3 and 4 and the templates
were not found in any source. The new import is Rowland's "local restart", which is the first concrete hypothesis
for what a template is.

### Core field

- **Condrey, "Finite Configurations Cannot Generate a Constant Trace in Rule 30"**, arXiv:2609.09431 (2026-09-08).
  - For each right half, a unique left half gives a constant centre trace. For trace 0 it is an alternating tail
    after the right half's first one; for trace 1 it is one universal checkerboard. Both are infinite, so no finite
    configuration has an eventually constant column.
  - The tool is Lemma 1, "triangular uniqueness", by left-permutivity. It is the same forced left half as our
    `rule30_periodic.py`. Lean proofs ship with the paper.
  - Conclusion, quoted: "The next unresolved case is eventual period two ... At p=2 no bounded law can exist ...
    H(2,w) ≥ w for every w ... a structural account of period-two exclusion remains open."
  - $H(p, w)$ is the longest $p$-periodic prefix of the trace over rows of support radius $w$. That differs from
    our X3 statistic (zero runs of the infinite forced left half, for a finite right half), but it is the same kind
    of fact: no constant bound.
- **Public period-two work**, GitHub woahwhattheheck/commons, issue 15314 and PR 15318 (read 2026-10-04).
  - A "bounded fiber engine" for support radius 1 to 14 examined 65,532 candidates. All escape, and the longest
    horizon is 19.
  - It states "period_two_infinite_theorem=false". Its named next inference is "every eventually-zero positive right
    half forces completion obstruction or infinitely many ones in the alternating trace". That is our Conjecture B in
    its weak form.
  - Our rung 1 (right halves up to 18 cells, left half forced to depth 256, 27,262,976 cases) covers more. The
    issue quotes Jen as "a finite Rule 30 orbit has at most one eventually periodic column".
- **Jen, E., "Aperiodicity in one-dimensional cellular automata"**, Physica D 45:3-18 (1990) (summary via MathWorld
  and a search snippet; the scan at OSTI was not read).
  - From a single black cell, the sequence attained by any two adjacent cells is not periodic.
  - Rule 30's right diagonals are periodic with periods $2^\alpha$.
  - The commons issue's stronger phrasing, "at most one eventually periodic column", is UNVERIFIED against the paper.
    RULE30-PRIZE.md §5 keeps the weaker, adjacent-columns form.
  - (Added 2026-10-05.) Kopra's Corollary 3.7 states the adjacent-columns form for every configuration with an
    eventually zero left half, not only the single seed. It decides conjecture LR for every eventually periodic
    column 1 (RULE30-PRIZE.md §8.13), which this entry should have prompted before §8.6's search was designed.
- **Rowland, E. S., "Local nested structure in rule 30"**, Complex Systems 16(3) (read, pages 1 to 4; §5, pages 15
  to 17, read 2026-10-05 after rule30_diagonals.py and rule30_leftband.py had run: see the entry at the end).
  - At row $2^n$ a region of the initial condition reappears on the right side, and the automaton "begins again"
    locally. This follows from left bijectivity (our left-permutivity) and from the right diagonals' periods
    $2^\alpha$.
  - The diagonal periods are characterised by $a(n)$ = 1, 3, 4, 6, 7, 9, 15, 16, 24, ... (no known fast formula).
  - The left diagonals are only eventually periodic. Their period doubling is proved in §5.
- **"Rapid left expansivity, a commonality between Wolfram's Rule 30 and powers of p/q"**, Theoretical Computer
  Science (2022), ScienceDirect pii S0304397522007502: the page refused access (403). UNVERIFIED and not read;
  listed so it is not forgotten.

### What to import, ranked

1. **Rowland's restart as the hypothesis for a template.** With column 0 clamped, every diagonal that starts at
   position 1 or more at time 0 never meets column 0 (each diagonal is computed from the two on its right). So that
   wedge is ordinary Rule 30 with its power-of-2 periods, and only the region between it and column 0 is driven by the
   trace. A long two-sided run may be the left side's echo of a local restart. Test: whether column 1, or the long
   runs, recur at times related to powers of 2.
2. **Octaves as the owner's "harmonics".** Period doubling is a harmonic series in octaves: diagonal $k$ from the
   edge repeats every $2^{\alpha(k)}$ steps. The run lengths' steps of 2 (§8.2) are the trace's own period, so two
   kinds of "harmonic" are on the table: multiples of $p$ (from column 0) and powers of 2 (from the right side). The
   probe for §8.3 separates them.
3. **Lean, as Condrey did.** Not yet: there is no theorem to formalise.

### Not to import

- Condrey's explicit fibres. For period two the forced left half is aperiodic (`rule30_rings.py`: 1,999 of 2,048
  right halves show no period up to 128), and Condrey's conclusion says no bounded law exists there either.
- Condrey's support-radius horizon $H(p, w)$, as the target statistic. It grows trivially, by truncation, so it
  cannot separate a proof route from a dead end.

### Sources

- Condrey, D. L., arXiv:2609.09431 — https://arxiv.org/abs/2609.09431 (abstract, conclusion and Lemma 1 read via
  the HTML version)
- woahwhattheheck/commons issue 15314 — https://github.com/woahwhattheheck/commons/issues/15314 ; PR 15318 —
  https://github.com/woahwhattheheck/commons/pull/15318 (claims summary)
- Jen, E., Physica D 45:3-18, 1990 — summary at https://mathworld.wolfram.com/Rule30.html ; scan at
  https://www.osti.gov/servlets/purl/7230855 (not read)
- Rowland, E. S., "Local nested structure in rule 30", Complex Systems 16(3) —
  https://ericrowland.github.io/papers/Local_nested_structure_in_rule_30.pdf
- "Rapid left expansivity ..." — https://www.sciencedirect.com/science/article/pii/S0304397522007502 (403; not read)

## Before the particle step: domains and particles (surveyed 2026-10-05, by Cloud)

Scope: the slips of the wheel (RULE30-PRIZE.md section 8.7) turned out to be defects of a domain that travel as
particles. That is the subject of computational mechanics.

- **Hanson, J. E. and Crutchfield, J. P., "Computational mechanics of cellular automata: an example"**, Physica D
  103:169-189 (1997) (abstract and summary read). On elementary rule 54 they identify the dominant regular domain,
  construct a domain filter that locates and classifies defects, and identify the primary particles, their
  interactions, and the equation of motion of the filtered spacetime. **Import:** the domain filter (our
  departure-from-D pattern is one, with the wheel as the domain) and their particle-interaction catalogue, as the
  method for part 3 of the route (how trains of particles move the wheel's phase).
- Sources: https://csc.ucdavis.edu/~cmg/papers/ECA54.pdf ;
  https://www.semanticscholar.org/paper/Computational-mechanics-of-cellular-automata:-an-Hanson-Crutchfield/036e7cb40ee06918aa47da9163ee866b9f316e4a

## Before the kick-game step: the wheel, phase locking, and recent Rule 30 work (surveyed 2026-10-05, by Cloud)

Scope: is the wheel of RULE30-PRIZE.md sections 8.5 to 8.8 (a 17/56 rotation next to a column clamped to 0101...,
kicked in notches by domain walls) already known, and what mathematics is closest? Checked tonight by search and by
reading abstracts; "(abstract)" means no more than that was read.

### Summary

Nothing found describes the wheel, its walls, or its notched kicks. The closest results are about columns and
diagonals of the single-seed pattern, and about two adjacent periodic columns, which is exactly the gap our two-sided
analysis sits in. The closest mathematics for "a wheel at a rational rotation number, with phase slips" is mode
locking (Arnold tongues).

### Sources and what to import

- **Kopra, J., "Rapid left expansivity, a commonality between Wolfram's Rule 30 and powers of p/q"**, Theoretical
  Computer Science 946 (2023) 113668, open access (read in full 2026-10-05; the first version of this entry, from a
  search summary, said "width w - 1", which was wrong).
  - **Definitions.** A rule is *left expansive with dimensions (h, d, w)* (Def. 3.1) when the contents of any
    h + d by w rectangle of a space-time diagram fix the cell just left of its top row. An (m, n) left-permutive rule
    is left expansive with dimensions (0, 1, m + n), so Rule 30 has (0, 1, 2). It is *left spreading* (Def. 3.3) when
    the leftmost 1 of a configuration whose left half is eventually zero moves left; for an elementary rule that means
    001 maps to 1, at speed 1. It is *rapidly left expansive* (Def. 3.4) when the speed is below 1/h, which always
    holds when h = 0.
  - **Lemma 3.2.** If a trace of width w is eventually p-periodic, so is the one a column to its left (the preperiod
    grows by h). **Theorem 3.5.** For a rapidly left expansive rule of width w and any configuration whose left half
    is eventually zero, no trace of width w is eventually periodic. **Corollary 3.7** is Jen's theorem (Physica D
    1990, Proposition 3): for a left-permutive, left-spreading elementary rule, no two adjacent columns are both
    eventually periodic. The proof covers every configuration with an eventually zero left half, not only the single
    seed.
  - **Page 7.** The single column (Problem 3.10, Wolfram's Problem 1) "is probably equally difficult for all
    configurations" with an eventually zero left half. The class cannot settle it, because it contains Rule 90, which
    from a single 1 has an eventually periodic single column.
  - **Section 4.** Theorem 4.5 and Corollary 4.6: the right half of a configuration whose left half is eventually zero
    returns exactly to its start only finitely often. Corollary 4.9: the sequence of right halves has infinitely many
    limit points. These generalise Pisot's and Dubickas' results on the fractional parts of $\xi (p/q)^n$; Theorem 4.7
    generalises Morse and Hedlund.
  - **Imported (RULE30-PRIZE.md §8.13).** Jen's theorem decides conjecture LR for every eventually periodic column
    1, so §8.6's periodic-column search and job M2 had a known answer. Its proof is our left recursion (Lemma 3.2 with
    h = 0) plus the light cone. The work had cited Jen in §5 without applying it, which is a failure of method,
    recorded. A consequence: in a finite configuration with column 0 eventually 0101..., column 1 is never eventually
    periodic, so the wheel slips for ever. Our Lemma 4, which uses Rule 30's OR and which Rule 90 lacks, is outside
    Kopra's class. That is consistent with his page-7 remark that the single column needs more than the class gives.
- **Nersissian, T., "Diagonal Periods and Newton Supports of Rules 30, 86 and 135"**, arXiv:2609.25077 (2026-09-18)
  (abstract). The single-seed Rule 30 cone has unbounded least diagonal periods in both directions, at least
  floor(m/2) + 1 at depth m, with a polynomial lift that connects to Fibonacci sequences. For Rule 86 there is a
  "backward map on periodic tail profiles". **To read:** whether that backward map is our pair map F of section 8.6
  in mirror image.
- **Chan-Lopez, E. and Martin-Ruiz, A., "Symmetric Nonlinear Cellular Automata as Algebraic References for Rule
  30"**, arXiv:2604.00165 (2026) (abstract). They attribute the apparent randomness of the centre column to
  left-permutivity and an asymmetric Boolean sensitivity, with Rule 22 as the symmetric reference. **Import:** context
  for section 8.6's churn (order in, noise out) and its avalanche.
- **Das, M., "Rule 30: Solving the Chaos"**, arXiv:2207.13237 (2022) (abstract). It claims an analytical solution to
  Prize Problem 1. The prize is still listed as open (rule30prize.org), so the claim has not been accepted. Not
  imported.
- **Arnold tongues and the circle map** (Wikipedia, "Arnold tongue"; read). A driven oscillator locks at a rational
  rotation number p/q over a whole region of parameters, and the rotation number as a function of the drive is a
  devil's staircase. **Analogy, not yet a method.** Under the period-2 trace the wheel turns 17 times in 56 steps.
  Under the other traces of the census (section 8.8) column 1 follows the drive's own frequency, which is low-order
  locking. The walls' notched kicks look like phase slips of a locked oscillator. **Import:** the rotation number as
  the invariant to compare traces by, if the census is extended.
- Not relevant on reading the abstract: Brummitt, C. D. and Rowland, E., "Boundary growth in one-dimensional cellular
  automata", arXiv:1204.2172 (a census of boundary growth rates, not Rule 30's columns).

Links: https://www.utupub.fi/bitstream/handle/10024/174540/1-s2.0-S0304397522007502-main.pdf ;
https://arxiv.org/abs/2609.25077 ; https://arxiv.org/abs/2604.00165 ; https://arxiv.org/abs/2207.13237 ;
https://en.wikipedia.org/wiki/Arnold_tongue ; https://arxiv.org/abs/1204.2172

## The owner's PRNG question: Rule 30 as a generator, and its cryptanalysis (surveyed 2026-10-05, by Cloud)

Scope: the owner asked what Rule 30's "poor behaviour on a chi-squared test when applied to all the rule columns"
(Wikipedia, citing Sipper and Tomassini) was, and whether it made the centre-column generator "a no go". The search
found that the cryptanalysis of Rule 30 reached this project's central construction 35 years earlier.

### Summary

The centre column was never a statistical failure. Wolfram's generator passes the standard tests, and Mathematica used
it for random integers for years. Its default today is a different cellular automaton, "ExtendedCA", which uses a
five-neighbour rule. Sipper and Tomassini used every cell of a small ring as a parallel stream, which is a different
generator, and `rule30_prng.py` shows two flaws of that use. The real break was cryptographic. Meier and Staffelbach
(1991) recovered the key from the centre column using Rule 30's left-toggle property. That is this project's forced
left half (§5 of RULE30-PRIZE.md, and Lemma 3 onwards).

### Sources and what to import

- **Meier, W. and Staffelbach, O., "Analysis of pseudo random sequences generated by cellular automata"**, EUROCRYPT
  '91, LNCS 547 (not read; described in Spencer's thesis below, read). Wolfram had proposed the centre column as a
  key stream (CRYPTO '85). Meier and Staffelbach showed that the left half of the space-time history is uniquely
  determined by the centre column and its right-adjacent column, because Rule 30 is left-toggle (left-permutive).
  The right-adjacent column comes from guessing the right half of the seed, and not all right halves are equally
  likely, so far fewer guesses are needed: for a 300-cell seed, 18.1 bits of entropy recover it with probability 1/2.
  - **Convergent evolution, recorded.** This is exactly our construction: column 0 and column 1 force the left half
    (§5), and the right half is a constraint on column 1 (§8). Their entropy of the right-adjacent column given the
    centre column is a cousin of our start-group counts $G(m, s)$ (§8.14). **Import:** their probabilistic algorithm,
    as a known method for counting column-1 sequences consistent with a given column 0. To read, if the counts matter.
- **Koc, C. K. and Apohan, A. M., inversion of Rule 30 iterations** (1997; described by Spencer). They answer a claim
  of Wolfram's that recovering a seed from states is NP-complete, with an inversion algorithm based on the best affine
  approximation of the rule. Not imported.
- **Spencer, J., "Cellular Automata in Cryptographic Random Generators"**, MSc thesis, DePaul University, 2013,
  arXiv:1306.3546 (read, the survey chapter). It describes the attacks above. It gives Sipper and Tomassini's setup:
  a cyclic 3-neighbour CA of 50 cells, 300 random initial states, 4,096 steps, each cell's entropy over time; evolved
  hybrids of rules 165, 90 and 150, or 165 and 225, compared with uniform Rule 30 and a 90/150 hybrid over four
  statistical tests. It also proves that toggle rules have a Theta(n) predecessor algorithm (InvertToggleRule).
- **Sipper, M. and Tomassini, M., "Generating parallel random number generators by cellular programming"**, Int. J.
  Mod. Phys. C 7(2) (1996) 181-190 (not read; abstract and Spencer only). Which chi-square Rule 30 failed is not known
  here. `rule30_prng.py` replicates the setup and finds two flaws of parallel use, neither of which touches the centre
  column used alone:
  - Neighbouring streams are tied: $x_{t+1}(i) \oplus x_t(i-1) = x_t(i) \vee x_t(i+1)$, so they agree at lag 1 in
    25.00% of steps instead of 50%. Rules 90 and 150 pass that test (50.02%, 50.00%), which is why linear hybrids looked
    better on it, although they are trivially broken by linear algebra.
  - Pooling consecutive rows: each row determines the next, so a chi-square that counts 4,096 rows of one run as
    independent rejects 12 to 13% of runs at the 1% level, on a ring or an open line alike. Rows 32 steps apart: 0.3%.
- **Wolfram Language documentation, "Random Number Generation"** (search summary). The default method "ExtendedCA"
  uses a five-neighbour cellular automaton rule; Rule 30 remains available as a method. The documentation's reasons
  for the change were not read.
- **Mariot, L. et al., "Insights Gained after a Decade of Cellular Automata-based Cryptography"**, arXiv:2405.02875
  (2024) (read in part, via a summary). Rule 30 lacks first-order correlation immunity, which is why the Meier and
  Staffelbach attack is efficient. Rule 30 is the field's standard warning: it passes statistical tests and is
  useless for cryptography.

**For our own method.** Our churn tests of §8.6 (block entropy, spectrum, avalanche) measured one sequence at a time.
By construction they cannot see a tie between two columns. That is fine for the question they answered (is the left
half random-looking), but it is the blind spot Sipper and Tomassini's parallel use exposes. Two-column statistics are
where Rule 30's structure is visible.

Links: https://link.springer.com/chapter/10.1007/3-540-46416-6_17 ; https://arxiv.org/abs/1306.3546 ;
https://www.worldscientific.com/doi/abs/10.1142/S012918319600017X ; https://arxiv.org/abs/2405.02875 ;
https://reference.wolfram.com/language/tutorial/RandomNumberGeneration.html ; https://en.wikipedia.org/wiki/Rule_30

## Before the bottleneck and entropy steps: information flow in Rule 30 (surveyed 2026-10-05, by Cloud)

Scope: are the leftward information speed (RULE30-PRIZE.md §8.17, §8.19) and the entropy of a column next to a
clamped periodic column (§8.20) known? Checked by search, abstracts only.

- **Shereshevsky, M. A., "Lyapunov exponents for one-dimensional cellular automata"**, J. Nonlinear Sci. 2 (1992)
  1-8, and **Tisseur, P., "Cellular automata and Lyapunov exponents"**, Nonlinearity 13 (2000) 1547 (arXiv:
  math/0312136) (abstracts; both cited by Kopra). Left and right Lyapunov exponents measure how fast perturbations
  spread each way. For Rule 30 the defect cone is asymmetric: perturbations spread right at full speed and left
  more slowly. A published value of the leftward speed was not found in what was read. Our measurements, 0.21
  cells per step for a single flip reaching column 1 next to a clamped 0101... and 0.28 for a second seed's
  influence on the open line, are of that kind. **Import:** the definitions, if the speed is ever needed exactly.
- **Bagnoli, F. et al., "Stability of cellular automata trajectories revisited: branching walks and Lyapunov
  profiles"**, arXiv:1406.5553 (search summary only): Lyapunov profiles of elementary rules, Rule 30 included. Not
  read.
- Nothing was found on the entropy of one column of Rule 30 next to a clamped periodic column. The bound of §8.20 is
  computed with the standard tools for sofic shifts (subset construction, spectral radius) on ladder.c's layer
  model.

Links: https://arxiv.org/abs/math/0312136 ; https://arxiv.org/abs/1406.5553 ;
https://www.sciencedirect.com/science/article/pii/S0304397522007502

## The owner's lightning, channels and maze: directed polymers and directed percolation (surveyed 2026-10-05, by Cloud)

Scope: before rule30_channels.py and rule30_maze.py (RULE30-PRIZE.md §8.28, §8.29), is it known whether paths of
least resistance through a random two-dimensional substrate form channels, and when a random pattern's black cells
connect? Checked by search, abstracts and summaries only.

- **Comets, F., Shiga, T. and Yoshida, N., "Directed polymers in a random environment: path localization and strong
  disorder"**, Bernoulli 9(4) (2003) (abstract). The decay rate of the partition function is equivalent to
  localisation of the path. Their approach relates the partition function to the probability that two polymers in
  the same environment end at the same point, our same-landing chance L. Quantitative decay estimates in one or two
  dimensions. **Imported:** L and its time average as the measure of channelling.
- **Comets, F. and Vargas, V., "Majorizing multiplicative cascades for directed polymers in random media"**, ALEA 2
  (2006) (summary): sharper free-energy estimates in dimension 1 + 1 and very strong disorder at every temperature
  there. So a polymer on a random pyramid should localise at any temperature: the theory behind CH2.
- **Chatterjee, S., "Proof of the path localization conjecture for directed polymers"**, Comm. Math. Phys. 370
  (2019) 703-717, arXiv:1806.04220 (title and summary only, not read).
- **Balazs, M., Rassoul-Agha, F. and Seppalainen, T., "The random average process and random walk in a space-time
  random environment in one dimension"**, Comm. Math. Phys. 266 (2006) 499-545 (summary): a walk choosing each step
  from a fresh random environment obeys a quenched central limit theorem; the quenched mean fluctuates on the scale
  $n^{1/4}$. The theory behind CH1 (the flicker spreads like a free walk).
- **Directed site percolation** in 1 + 1 dimensions has threshold 0.70548522 on the square lattice, with two parents
  per site (search summary). No published value was found for the lattice with three parents per site (x - 1, x,
  x + 1), the one the maze uses; rule30_maze.py measures it near 0.53 at depth 2048.
- Not found: any study of polymers or percolation on a cellular automaton's space-time pattern. The comparison of
  Rule 30 with random substrates (§8.28, §8.29) appears to be new, and simple enough that it may exist unfound.

Links: https://projecteuclid.org/journals/bernoulli/volume-9/issue-4/Directed-polymers-in-a-random-environment--path-localization-and/10.3150/bj/1066223275.full ;
https://link.springer.com/article/10.1007/s00220-019-03533-1 ;
https://link.springer.com/article/10.1007/s00220-006-0036-y ; https://arxiv.org/html/cond-mat/0503408

## After the diagonals and the band: what was already known (surveyed 2026-10-05, by Cloud, after the runs)

A failure of method: rule30_diagonals.py (left half) and rule30_leftband.py were designed and run before Rowland's §5
and Wolfram's prize announcement had been read. Both cover much of the ground.
- **Rowland, "Local nested structure in rule 30", §5 "The left side of rule 30"** (read). Left diagonals are eventually
  periodic with power-of-2 periods, a consequence of Jen's Theorem 4 (E. Jen, "Global properties of cellular
  automata", J. Stat. Phys. 43 (1986) 219-242). The eventual periods from the left edge begin 1, 1, 1, 2, 1, 2, 2, 1,
  4, 1, 4, ..., exactly as rule30_diagonals.py measured. Proposition 2 is Wolfram's observation (NKS p. 871), proved
  for any rightful initial row. Each period doubling occurs exactly when a diagonal is eventually white and the
  diagonal to its left has an odd number of black cells in each period. When a diagonal is eventually white and the
  next has a black cell in its period, the one after is eventually black.
  - Rowland's open question. Is the eventual left side independent of the initial condition? Rowland expects not. An
    eventually white diagonal whose left neighbour has an even number of black cells per period leaves two possible
    periods for the next diagonal, complements of each other. That first happens at his column 53209: column 53208
    is eventually white, and column 53207 has period 16. Each of those continuations splits again, at columns 58288
    and 72577, "and one surmises that in fact there are infinitely many possible left sides". Whether both
    possibilities are realised by actual initial conditions is left open ("if in fact they do occur").
  - **Import:** the credit for §8.27's left-side statements and for LB0, and the open question, tested by
    rule30_leftsides.py (§8.31). His columns are numbered from 1 at the left edge, so his column m is our diagonal
    e = m - 1, if his period list is aligned as it appears to be (checked there).
- **Wolfram, S., "Announcing the Rule 30 Prizes"** (writings.stephenwolfram.com, 2019) (read in summary). There is
  "some regularity over on the left". "At least over the first 100,000 or so steps, the boundary seems to move on
  average about 0.252 steps to the left at each step, with roughly random fluctuations." It is presented as an
  observation. **Import:** the credit for §8.30's band and its speed. Our 0.245 to 0.257 (from the transients)
  brackets it; the damage front on a random background, 0.246 with a standard error near 0.003, is close but about
  two standard errors below it.
- **Wolfram's Problem 2 table** (the same announcement, read 2026-10-05). Black and white counts in the centre column
  after 10, 100, ..., 10^9 steps: black 7, 52, 481, 5,032, 50,098, 500,768, 5,002,220, 50,009,976 and 500,025,038.
  That is an excess of black at every decade from 10^4 on, by 0.6 to 2.0 standard deviations of a fair coin; Wolfram
  describes the running excess as random-walk-like. rule30_tilt.py reproduces the counts to 10^6 exactly. (A first
  summary of the page gave a wrong ratio, 0.9999998, corrected from the table before any use.)
- Searches for a later answer to Rowland's question ("rule 30" "left side", 53209) found nothing.
- **Our answer** (rule30_leftsides.py, RULE30-PRIZE.md §8.31). Rowland's indexing is confirmed (his column 53209 is
  our diagonal 53208). The other continuations occur for constructed finite seeds: at least 4 certified left sides by
  diagonal 160,000, with branch points 53208 and 58287 on the universal side and 53208 and 72576 on the other, as he
  found. But all 60 generic rows tried share one left side, and the split's decision is phase-locked to the left
  side's own cycle.

Links: https://ericrowland.github.io/papers/Local_nested_structure_in_rule_30.pdf ;
https://writings.stephenwolfram.com/2019/10/announcing-the-rule-30-prizes/

## Before and after the entropy squeeze: column entropy (surveyed 2026-10-05, by an independent review session)

Scope: is RULE30-PRIZE.md §8.33's lemma known? Every left column of a Rule 30 configuration whose column 0 is 0101...
has topological entropy at most (1/2) log2 lambda_m. Does anything give a lower bound on a column's entropy? A
separate session, given only the lemma and the sources, reviewed it adversarially and searched. Its findings:
- **Milnor, J., "On the entropy geometry of cellular automata"**, Complex Systems 2 (1988), Example 6.2 (read via text
  extraction; https://wpmedia.wolfram.com/sites/13/2018/02/02-3-6.pdf). The "additional causal cone" of a
  left-permutive map, the geometric fact behind step 3. Directional entropy concerns the whole system, not one
  configuration with a column held fixed.
- **Kopra, J., "Rapid left expansivity, a commonality between Wolfram's Rule 30 and powers of p/q"**, Theoretical
  Computer Science 946 (2023) (read in full by the review, via
  https://www.utupub.fi/bitstream/handle/10024/174540/1-s2.0-S0304397522007502-main.pdf; earlier listed here as
  UNVERIFIED after a 403). It defines left expansivity with dimensions (0, 1, 2). It never mentions entropy. Its
  Jen-type results come from Morse-Hedlund, so the known lower bound on a width-2 trace is p(n) >= n + 1. Kopra's
  arXiv:2005.05112 on trace complexity was read only in abstract.
- **Kurka, P.** (column subshifts; https://www.cts.cuni.cz/~kurka/cantor.pdf) and **Courbage, M. and Kaminski, B.**
  (directional entropy; https://link.springer.com/article/10.1007/s10955-006-9172-1). Both are about systems, not
  single configurations.
- Sliding block codes do not increase entropy, and sofic entropy comes from the subset construction (Lind and
  Marcus, a textbook; cited from memory).
- **Not found:** the lemma itself; any positive lower bound on the entropy of any column of any finite Rule 30
  configuration. In Kopra's class such a bound fails in general: Rule 90's two-cell trace from a single seed has
  p(n) = 7, 13, 25, 49, 97, 193 at n = 4, 8, ..., 128 (the review's computation), entropy 0.
- **Import:** the credit and the limits recorded in §8.33. The review found the lemma sound and the first-stated
  reduction a restatement of the problem.

## After the merging census: merging walks and the coin's maximum (surveyed 2026-10-05, by Cloud, after the runs)

Scope: RULE30-PRIZE.md §8.38 (rule30_influence.py, rule30_merge.py). Is the count of distinct forced walks known,
and are the two outside facts it leans on stated correctly? The survey came after the runs. The predictions did not
depend on it, but they used both facts from memory, so this is recorded as late.
- **Milnor's directional entropy** (already listed above, in the column-entropy survey). It measures the whole
  system's complexity along a direction of space-time. §8.38 counts something narrower: the distinct pairs of
  anti-diagonals reachable when column 0 is held at 0101... and column 1 is free at even times. Not found in the
  record: that count, its growth rate (about 1.764 per free bit), or the OR-shielding merges behind it.
- **Scheidegger, A. E., "A stochastic model for drainage patterns into an intramontane trench"**, Bull. Int. Assoc.
  Sci. Hydrology 12 (1967), 15-20 (citation checked by search; the paper itself not read). In this river-network
  model each site drains to one of two neighbours below it, chosen at random, so the streams are coalescing random
  walks. The number of distinct streams then falls as a power of the distance, which is what MG7 compared against.
- **Eisenberg, B., "On the expectation of the maximum of IID geometric random variables"**, Statistics & Probability
  Letters 78 (2008), 135-143 (abstract). The expected maximum of n IID geometrics with P(M >= m) = 2^-m is
  log2 n + gamma / ln 2 - 1/2 plus a small periodic term. For runs of 1 + 2M that gives §8.38's 2 log2 n + 1.67.
- **Import:** the comparison in MG7, and the constant in §8.38. Nothing found settles either statement that §8.38
  says a proof would need.

## The owner's zeta note: the prime-gap parallel (surveyed 2026-10-05, by Cloud)

Scope: the owner compared lead 1's returns to zero with the Riemann zeta function's zeros. The precise parallel is
the probabilistic model of the primes and its maximal gaps. That model is to the primes what the coin model is to
Rule 30's forced walks. The survey came after the merging census of RULE30-PRIZE.md §8.38 and changed none of its
predictions.
- **Cramer's model and conjecture** (H. Cramer, 1936): treat each n as prime with probability 1/log n,
  independently. The model predicts maximal prime gaps of about (log p)^2. Statement and history checked via
  https://en.wikipedia.org/wiki/Cram%C3%A9r%27s_conjecture and Granville's survey below.
- **Maier's theorem** (1985) shows the model is wrong in short intervals, because divisibility by small primes is
  structure, not chance.
- **Granville, A., "Harald Cramer and the distribution of prime numbers"**, Scandinavian Actuarial Journal (1995)
  (https://chance.dartmouth.edu/chance_news/for_chance_news/Riemann/cramer.pdf; checked through the search summary
  and the Wikipedia article, not read in full). The refined model, with the small primes sieved out, raises the
  constant: limsup G(p) / (log p)^2 >= 2 e^-gamma = 1.1229. This is the shape of §8.38. A coin model gets the scale,
  and a structural correction (there divisibility, here the merging of walks) changes the constant (there 1 to
  1.12, here 1 to 0.82).
- **Bertrand's postulate**: for every n > 1 there is a prime between n and 2n. That is a doubling statement, like
  §8.36's conjecture that from depth d there is a one by depth 2d + 4. Chebyshev proved it around 1850 from
  estimates of factorials, long before anything sharp about gaps. Ramanujan (1919) and Erdos (1932) reproved it
  from the prime factors of the binomial coefficient C(2n, n). None of the proofs shows that the primes are
  random. Cited from memory, as standard.
- **Import:** the shape of a proof worth looking for. Cramer's sharp conjecture is still open. The doubling
  statement fell to a size argument: a quantity forced to be large, which an empty interval would make small. For
  Rule 30, any finite bound on R(d), not only d + 4, settles Conjecture LR for 0101... (König's lemma turns
  unbounded runs into an infinite one). So the target has Bertrand's shape, not Cramer's.

## After the wheel dig: Rule 30's siblings in arithmetic (surveyed 2026-10-05, by Cloud)

Scope: RULE30-PRIZE.md §8.43 and §8.44 leave the cost side of period 2 open: why a condition at the 0101 wall
costs a bit. Does any sibling problem have a proved size argument of the kind PRIOR-ART's prime-gap parallel
points to?
- **Kopra, J., "A natural class of cellular automata containing fractional multiplication automata, Rule 30, and
  others"**, arXiv:2202.13809 (abstract read). It defines rapidly left expansive cellular automata, a class
  containing Rule 30 and the automata that multiply by a fraction p/q in a suitable base. Jen's proposition on
  aperiodic columns generalises to the class. Rule 30 is in the class; it is not a multiplication automaton.
- **Mahler's 3/2 problem** (1968; checked via https://en.wikipedia.org/wiki/Mahler%27s_3/2_problem). It asks whether
  any xi > 0 keeps every fractional part of xi (3/2)^n below 1/2 (a "Z-number"). It is open.
- **Flatto, L., Lagarias, J. C. and Pollington, A. D., "On the range of fractional parts {xi (p/q)^n}"**, Acta
  Arithmetica 70 (1995), 125-147 (http://matwbn.icm.edu.pl/ksiazki/aa/aa70/aa7023.pdf; sections 1 to 3 read, the
  proofs of Theorems 1.1, 1.2, 3.2 followed, Theorem 3.3's lemmas skimmed). For coprime p > q >= 2, any interval
  holding every {xi (p/q)^n} has length at least 1/p (Theorem 1.4). Partial, as Mahler's conjecture needs 1/2.
  How the proof works, Mahler's "decoupling":
  - The integer parts g_n follow a fixed map T on the integers. Its symbols (g mod q) form a full shift: every
    string of length k occurs exactly once among the residues mod q^k (Lemma 2.2).
  - The scaled fractional parts follow a linear mod-one map f(x) = beta x + alpha with beta = p/q. Its admissible
    strings are few: at most c beta^k of length k.
  - xi is a generalised Z-number exactly when the two itineraries agree, up to a fixed permutation (Prop. 2.1). The
    counting gives sparsity (Theorem 1.1, at most x^gamma Z-numbers below x, gamma < 1).
  - Emptiness comes from finiteness (Theorem 3.2). If only finitely many f-orbits stay in the interval, then
    pigeonhole makes the orbit periodic. Two different powers of xi would then share one integer itinerary, which
    Lemma 2.2's injectivity forbids. Theorem 3.3, the long part, shows that finiteness holds for a dense set of
    intervals of length 1/p.
- **What it means here: the same structure, in the same open regime.** The wall form of RULE30-PRIZE.md §8.39 and
  §8.40 is a decoupling of the same kind:
  - **The free side.** The left half is a full shift at the wall, its itinerary in bijection with the seed (WA1).
    That is the integer side.
  - **The constrained side.** The right half's column 1 has a thin language (the channel bound, §8.20). That is the
    mod-one side.
  - **The coupling.** A finite configuration with a periodic centre needs the two to agree at the wall for ever:
    that is a Z-number.
  - **Emptiness by finiteness** is, here, Jen's theorem (a periodic column 1) and Condrey's constant walls (column 1
    monotone, so each admissible column 1 is eventually constant; corrected wording, see the wide survey below:
    zero entropy alone would not be enough).
  - **The open regime.** Next to 0101 the constrained side has positive entropy, about 0.12 bits per visible bit, so
    infinitely many admissible behaviours. That is exactly the regime of Mahler's own conjecture (interval 1/2 > 1/p),
    which this method has not closed since 1968. The entropy squeeze (§8.33) is the analogue of FLP's Theorem 1.1,
    sparsity without emptiness.
  The import is a calibration, not a route: Rule 30's period-2 case is a Mahler-type problem in the regime where
  Mahler's method stops.
- **What it means here.** In the same class as Rule 30, the question of the same shape is also open, and the best
  known result is a size bound. Its proof uses the arithmetic of p/q (integers and residues), which Rule 30 lacks.
  A Rule 30 analogue would need a substitute for that arithmetic. It is recorded as the nearest proved size
  argument, not as a route.


## The owner's wide survey: nature, biology and the other disciplines (surveyed 2026-10-05, by Cloud)

Scope: the owner asked for one more research road before fresh eyes: as many disciplines as possible, however
unlikely, each with a tether to the problem's structure. "Our Rule 30 problem paints itself on the back of a snail
shell." Seven survey agents searched, one per domain: biology and nature; physics and chemistry; mathematics;
computing and engineering; the long shots (history, astronomy, the arts); molecular machinery (the owner's protein
folding note); and the Game of Life (the owner's second note). Each was given the same four-item summary of the
problem and asked to rate each tether from 1 (an analogy) to 5 (the same mathematics). The agents read the
sources; Cloud checked the top-ranked ones (marked "checked") at their abstract pages. The survey came after every
run so far and changed no prediction.

The one finding that every domain returned: every theorem found of the form "a low-information drive cannot hold a
chaotic system in a fixed state" is about **sets** (of positive measure, or with interior), never about **one
orbit**. That is exactly the gap between the entropy squeeze (sparsity) and the prize (emptiness), and the gap in
Mahler's problem.

A correction came with it. The mathematics survey read FLP's Theorem 3.2 again: its hypothesis is finitely many
admissible orbits, which is stronger than zero entropy (a Sturmian system has zero entropy and uncountably many
points). RULE30-PRIZE.md §8.45 and the section above are corrected in place: the solved cases are those where every
admissible column 1 is eventually periodic (Morse and Hedlund's criterion, Kopra's Lemma 4.2, then Jen).

**Mathematics** (strength 5 to 2):
- **Kari, J. and Kopra, J., "Cellular automata and powers of p/q"**, RAIRO-ITA, arXiv:1710.05737 (abstract checked).
  Mahler's problem restated as a question about one column of the automaton that multiplies by p/q in base pq.
  Theorem 4.9, from ergodicity, strong mixing and compactness (an unavoidable finite family of cylinders, Lemma
  4.4): finite unions of intervals approximating [0, 1] as closely as one likes hold no orbit. Not constructive;
  their Problem 5.1 asks for a constructive proof. The trace subshift is neither sofic nor synchronising
  (arXiv:2005.05112). Strength 5.
- **FLP's Theorem 3.3** (the paper of the previous section, pp. 138-139, reread by the survey). Finiteness holds for
  a dense set of windows, and the bound 1/p comes from enlarging a window to one of those. FLP never beat positive
  entropy: they moved to a window where the constrained side is finite. Strength 5.
- **Kopra's barrier** (arXiv:2202.13809, the survey's reading). The class of rapidly left expansive automata contains
  Rule 90, whose centre column from one cell is eventually constant. A proof must use Rule 30's own nonlinearity.
- **Lagarias, J. C., "Ternary expansions of powers of 2"**, arXiv:math/0512006. Erdős's conjecture that 2^n has a
  2 in base 3 for n > 8 is open. Two methods, from the leading digits and from the trailing (3-adic) digits, use
  independent information, and combining them is "a challenging problem". The truncated real exceptional set
  (floor(lambda 2^n) free of 2 infinitely often) has Hausdorff dimension exactly log_3 2 (Theorem 1.3), the analogue
  of positive entropy. For the untruncated real and the 3-adic exceptional sets, dimension 0 is only conjectured
  (Conjectures A, B), with proved bounds such as dim E^(2)(Z_3) <= 1/2 (Theorem 1.5). (comb note, 2026-10-14, Local,
  SW-01: checked against arXiv math/0512006 section 1, Theorems 1.3 and 1.5 and Conjectures A and B; the first
  wording said "The exceptional set has Hausdorff dimension log_3 2 > 0".) Strength 4.
- **Buzzi, J., "Piecewise isometries have zero topological entropy"**, Ergodic Theory Dynam. Systems 21 (2001)
  1371-1377 (checked). A rotation with slips of fixed sizes at fixed phases is a piecewise isometry, so column 1's
  positive entropy must come from the kick sizes, as §8.43 measured. Strength 4.
- **Collatz.** Bernstein and Lagarias's conjugacy of the 3x+1 map to the 2-adic shift is triangular, like the
  seed-to-itinerary bijection of the wall form. Tao's theorem (arXiv:1909.03562) covers almost all orbits, not every
  orbit. Strength 3.
- **The busy beaver cryptid Antihydra** (https://wiki.bbchallenge.org/wiki/Antihydra): it halts iff an iteration of
  floor(3n/2) ever has enough odd values, a Mahler-family question. A random-walk model says it never halts;
  there is no proof. Strength 3.
- **Furstenberg, Rudolph, Host; Sarnak; Sinai.** Measure rigidity under x2 and x3 concerns measures and typical
  points; its automaton versions need algebraic, bipermutative rules (arXiv:math/0510564), which Rule 30 is not.
  Two systems of positive entropy are never disjoint (each has a Bernoulli factor, by Sinai), so there is no
  measure-level obstruction to coupling the two sides: any proof works point by point. Strength 2 to 3.
- **Low complexity forces structure** (Morse and Hedlund; Adamczewski and Bugeaud; Durand's Cobham theorem;
  Nivat-type results). Each works only when the complexity is low. Strength 2.

**Computing and engineering** (strength 4 to 1):
- **Yolcu, E., Aaronson, S. and Heule, M. J. H., "An automated approach to the Collatz conjecture"**,
  arXiv:2105.14697 (abstract checked). Collatz as termination of a string rewriting system; nontrivial weakenings
  proved with SAT-found natural and arctic matrix interpretations; an earlier unary encoding provably admits no
  such proof, so the encoding decides. Strength 4.
- **Liveness certificates for infinite-state systems**: regular model checking with learned automaton invariants
  (http://www.cs.ru.nl/personal/nilsjansen/files/publications/neider-et-al-nfm-2013.pdf); Lin, A. W. and
  Rümmer, P., CAV 2016, arXiv:1606.01451 (abstract checked: a progress relation as a finite automaton, learned with
  L* and SAT); k-liveness (Claessen and Sörensson, FMCAD 2012). Condrey's $H(2, w) \ge w$ rules out a fixed-depth
  induction, so a certificate must scale with the width, as these do. Strength 4.
- **Rule 30's own forcing rules** (Meier and Staffelbach; Spencer's thesis, arXiv:1306.3546, already above): "10" in
  a column forces a 1 to its left. Strength 3.
- **The wheel as a digital line**: Euclidean rhythms and Bresenham's algorithm (Demaine et al., "The distance
  geometry of music", https://erikdemaine.org/papers/DeepRhythms_CGTA/paper.pdf); linear-time recognition of
  digital straight segments (arXiv:0906.2351), an exact kick detector; bandpass sigma-delta modulators as piecewise
  isometries. Strength 3.
- **Decidability**: properties of ultimate traces are undecidable over all automata (arXiv:1001.0251); for linear
  automata the columns are automatic and eventual periodicity is decidable (arXiv:1209.6008). Strength 3.
- Constrained coding (the channel bound is Shannon's capacity, which cannot exclude one word), boundary control of
  automata as SAT (Bagnoli, Dridi and Fatès, arXiv:2504.03691), phase-locked loop cycle slips (statistics only),
  particle image velocimetry's peak locking (analogy). Strength 2 to 1.

**Physics and chemistry** (strength 4 to 1):
- **Touchette, H. and Lloyd, S., "Information-theoretic limits of control"**, PRL 84 (2000) 1156, arXiv:chao-dyn/9905039
  (abstract checked): each bit gathered buys at most one extra bit of entropy reduction. **Nair, G. N., Evans,
  R. J., Mareels, I. M. Y. and Moran, W., "Topological feedback entropy and nonlinear stabilization"**, IEEE TAC 49
  (2004) 1585-1597 (https://people.eng.unimelb.edu.au/gnair/TAC04.pdf; checked via the search summary): a plant can
  be held in a compact set iff the data rate exceeds its feedback entropy there. OGY control (Ott, Grebogi and
  Yorke) holds a chaotic system on one unstable periodic orbit with tiny pushes. Strength 4 for the coin model,
  1 for the missing step: these are theorems about sets.
- **Domain walls as particles**: Grassberger (1984), annihilating random walks of kinks; **Eloranta, K. and
  Nummelin, E., "The kink in elementary cellular automaton Rule 18 performs a random walk"**, J. Stat. Phys. 69
  (1992) 1131-1136 (bibliographic record checked; abstract not seen); Hanson and Crutchfield's automatic domain test
  (https://csc.ucdavis.edu/~cmg/papers/ECA54.pdf). Strength 4.
- **Frenkel-Kontorova discommensurations** (Sturmian ground states, arXiv:2507.06915; many-kink solutions at
  rational rotation number, arXiv:2004.04868); Aubry-Mather arguments need well-ordered configurations, and kicks
  of both signs break that. **Random tilings**: the angle is the phason coordinate, and its free diffusion is a
  phason walk (arXiv:cond-mat/0310514). Strength 3 to 4, as descriptions.
- Boundary-driven transport (Krug, PRL 67 (1991) 1882; Rule 54 with random boundaries, arXiv:1512.01385, which needs
  integrability), phase slips in wires and condensates, the kicked rotor (Chirikov's diffusion rate comes from
  ignoring correlations). Strength 2 to 1.

**Biology and nature** (strength 4 to 1):
- **Cardiac parasystole** (Glass, L., Goldberger, A. L. and Bélair, J., Am. J. Physiol. 251 (1986) H841;
  Schulte-Frohlinde et al., PRL 87 (2001) 068104, arXiv:cond-mat/0011367, abstract checked). A beat shows when a
  rotating phase leaves a refractory window; the number of beats between takes at most three values (the three-gap
  theorem, via Slater 1967); in modulated parasystole the sinus beats reset the phase, a rotation with kicks.
  Strength 4.
- **Longest matches in DNA**: Arratia, R. and Waterman, M. S., Adv. Math. 55 (1985); **Rousseau, J., "Longest common
  substring for random subshifts of finite type"**, Ann. IHP, arXiv:1905.08131 (abstract checked): governed by the
  Rényi entropy, almost surely, under mixing. The coin law as a theorem for typical inputs. Strength 4.
- **Random circle maps** (Müller-Bender, Kastner and Radons, arXiv:2204.09392; Antonov and Malicet): random circle
  maps synchronise unless they share an invariant measure. Rigid rotations share the uniform one, so nothing pulls
  the wheel's angle back. Strength 3.
- **Phyllotaxis** (Douady and Couder, PRL 1992; Atela, Golé and Hotton, J. Nonlinear Sci. 2002; Adler, J. Algebra
  1998): the same continued fractions, but the plant's angle is selected and stable, the opposite of the wheel.
  Strength 3, for the wheel only.
- **Seashells** (Meinhardt, https://www.bio.mpg.de/268545/pigmentation-patterns; Wolfram, NKS p. 423): the shell
  is a space-time plot and colliding waves annihilate, but the models are reaction-diffusion with restoring forces
  (in Oliva porphyria a hormone counts the waves), and Conus textile's resemblance to Rule 30 is visual. No wall was
  found. Strength 2.
- Winfree's phase singularities (a homotopy argument needing a continuous phase), clock-and-wavefront somitogenesis,
  Boolean-network control (finite, so the pigeonhole case), the error threshold. Strength 2 to 1.

**Molecular machinery** (the owner's protein-folding note; strength 4 to 1):
- **Invariance entropy** (Colonius, F. and Kawan, C., SIAM J. Control Optim. 2009): the least data rate that keeps
  every state of a set inside a target. Its lower bounds are volume counts, a uniform escape rate. A single orbit
  costs nothing. Strength 4, with the same gap.
- **Boyd, A. B., Mandal, D. and Crutchfield, J. P., "Correlation-powered information engines and the thermodynamics
  of self-correction"**, PRE 95 (2017) 012152, arXiv:1606.08506 (checked in the PDF). A ratchet reads a period-2
  tape 0101... with phase slips at rate c; a synchronising state returns it to phase; above c* = 1/(1 + e) it can
  no longer work. The objects are ours: a period-2 tape with slips. The inequality needs a measure and an energy;
  the transducer formalism could carry over. Strength 3.
- **Zurek, W. H., "Algorithmic randomness and physical entropy"**, PRA 40 (1989) 4731 (not read): entropy of a single
  microstate. It suggests the single-object form of the missing statement. Strength 3.
- **Algorithmic self-assembly**: Rothemund, Papadakis and Winfree, PLoS Biol. 2 (2004) e424, Sierpinski triangles
  grown by XOR tiles from a seed row, errors propagating as defects; proofreading tile sets. No Rule 30 tile
  experiment was found. Strength 3 for the object, 1 for the theorems.
- **Protein folding**: Levinthal's paradox and its resolution by a biased landscape (Zwanzig, Szabo and Bagchi,
  PNAS 89 (1992) 20: a bias of a few kT shrinks the search); the HP model's NP-hardness (Berger and Leighton);
  designability (Li, Helling, Tang and Wingreen, Science 273 (1996) 666), which is many-to-one where the wall's
  left side is a bijection. Strength 1 to 2.
- Kinetic proofreading (Hopfield 1974), ribosomal frameshifting at slippery sites, Feynman's ratchet, rotary motors
  in steps (F1-ATPase; the flagellar motor's 26 steps against the wheel's 28 notches is a coincidence), the KaiABC
  clock. Strength 2 to 1: they need noise, energy or detailed balance.

**The long shots** (strength 4 to 1):
- **Langton's ant**: the highway is unproved (https://en.wikipedia.org/wiki/Langton%27s_ant), but **Bunimovich, L. A.
  and Troubetzkoy, S. E., "Recurrence properties of Lorentz lattice gas cellular automata"**, J. Stat. Phys. 67
  (1992) 289-302 (bibliographic record checked) proved every trajectory unbounded. The proof's outline, from a
  summary only: reversibility makes a bounded path periodic, and an extremal cell gives the contradiction.
  Strength 3.
- **Calendars**: the Hebrew leap years form E(7, 19); leap-year rules generalise Bresenham (Harris and Reingold);
  the Persian 33-year cycle is seven 4-year blocks and one 5-year block, slipping now and then to 29 years
  (arXiv:astro-ph/0409620). The same mathematics as the wheel. Strength 4, as a viewpoint.
- **Music**: well-formed scales are Christoffel words (Clampitt and Noll, MTO 11.17.1); E(17, 56) was found in no
  catalogue. Strength 4, as a viewpoint.
- **Pingala and Virahanka**: a correction to the survey's own brief. They counted metres of n morae made of short
  (1) and long (2) syllables, which gives the Fibonacci numbers, the same count as binary words with no two
  adjacent ones (Singh, Historia Math. 12 (1985)).
- Euclid and Erdős's proof of Bertrand (a gap between two exponents), Kirkwood gaps (long quiet behaviour proves
  nothing), KAM's golden torus, satin weaves, Huygens's gear ratios. Strength 3 to 1.

**Philosophy and logic** (the owner's note: "We should not discount philosophical sources as irrelevant just because
they contain no concrete math. Their math is logic, truth, gates." An eighth survey agent; sources not checked by
Cloud):
- **Eternal recurrence and Simmel's wheels.** Nietzsche argued that finitely many centres of force must pass through
  finitely many combinations and repeat (https://www.gutenberg.org/files/52915/52915-h/52915-h.htm). Simmel replied
  with three wheels on one axle, one turning at 1/pi the speed of another, which never line up again
  (https://schwitzsplinters.blogspot.com/2012/10/nietzsches-eternal-recurrence-scrambled.html). The pigeonhole case
  and the open case, in one argument: a wheel with eventually periodic kicks gives a periodic column 1, closed by
  Jen; the open case is exactly kicks that never become periodic, Simmel's 1/pi. Strength 4, as a picture.
- **Potential infinity** (Euclid IX.20 says "more than any assigned multitude", never "infinite"; Aristotle;
  Archytas's staff at the edge of the world; https://plato.stanford.edu/entries/infinity/). The form of the missing
  statement: for every width w, a bound B(w) by which every configuration on w cells breaks the 0101 centre. Each
  B(w) is a finite check; the proof needed is a formula for B or a step from w to w + 1. This is PERIOD-TWO.md §7,
  question 1. Strength 4.
- **Hume, Popper and Carroll's Tortoise** (https://plato.stanford.edu/entries/induction-problem/;
  https://en.wikipedia.org/wiki/What_the_Tortoise_Said_to_Achilles). The coin model is a uniformity principle, so
  more runs that confirm it go round Hume's circle; each restatement hands the Tortoise one more premise, and what
  is missing is a rule of inference. "Eventually 0101" has the form "there is a T such that for every t", which no
  finite run can verify or refute. The answer to the owner's ouroboros, from philosophy. Strength 4.
- **Kripke's quus and Goodman's grue** (https://iep.utm.edu/kripkes-wittgenstein/). Finitely many observations fit
  infinitely many rules. Here: every finite stretch of 0101 is realised by some seed, so an argument from windows of
  time cannot work, and a proof must use the finiteness of the seed. Strength 3.
- **The tetralemma** (Nagarjuna's catuskoti: A, not A, both, neither; Belnap's four-valued logic;
  https://en.wikipedia.org/wiki/Tetralemma). It names the fourth game that RULE30-PRIZE.md §8.40 lacked: neither,
  no conditions, the baseline. It suggests a measurement: with $N$ the count of seeds that survive each game,
  $N_\text{both} N_\text{neither} / (N_\text{black} N_\text{white})$ near 1 says the black and white conditions are
  independent, as the coin model assumes; a ratio falling towards 0 would be a measurable obstruction. Strength 3.
- **Boole and Jevons** (https://plato.stanford.edu/entries/boole/). Boole defined x + y only for disjoint classes
  (exclusive or), and refused Jevons's inclusive or. Since $c \lor r = c \oplus r \oplus cr$, Rule 30 is the linear
  Rule 150 plus the single term $cr$: all its nonlinearity is the overlap Boole would not interpret. Strength 3.
- Llull's rotating discs, Leibniz's binary columns (01, 0011, 00001111...), Cusanus's infinite circle as a line,
  Dante's 3-sphere (two balls glued along a sphere, like two halves glued at a wall; Peterson, Am. J. Phys. 1979),
  Borges's Library and forking paths, Zeno: pictures, strength 2 to 1. No tether was found for Kant, the Liar or
  Funes.

**Addendum, the mixing check for question 4** (2026-10-05, by Cloud, from the thesis the owner linked).
- **Shereshevsky, M. A., "Ergodic properties of certain surjective cellular automata"**, PhD thesis, University of
  Warwick, 1992 (https://wrap.warwick.ac.uk/id/eprint/34640/1/WRAP_THESIS_Shereshevsky_1992.pdf; Chapter 1, section
  1.3 read), the source of the paper in Monatsh. Math. 114 (1992) 305-316. Write the rule as
  $(Tx)_i = F(x_{i+l}, \ldots, x_{i+r})$.
  - Theorem 1.3.3: if $l < 0$ and $F$ is left permutative, the automaton is $k$-mixing for every $k \ge 1$ for the
    uniform Bernoulli measure. Rule 30 has $l = -1$ and is permutive in $x_{i-1}$, so it is $k$-mixing, hence
    ergodic. Shirvani and Rogers had proved the 1-mixing case for two symbols.
  - Theorem 1.3.2 (a Bernoulli natural extension) needs $l < r \le 0$ in the left-permutive case, and Theorem 1.3.4
    (a K-automorphism) needs the neighbourhood on one side of the cell. Rule 30 meets neither ($l < 0 < r$).
  - Proposition 1.3.6: the left-permutive rule $x_0 + x_1(x_2 + 1)$ on the neighbourhood $[0, 2]$ is surjective and
    not ergodic, so the condition $l < 0$ matters.
  So Kari and Kopra's hypotheses of ergodicity and strong mixing hold for Rule 30. What their argument would still
  need is a Rule 30 analogue of the step from Z-numbers to configurations; that is not done.

## After the window principle: the Collatz complexity bound is Dubickas's (checked 2026-10-05, by Local through a search agent)

Checked after the proofs of COLLATZ-PRIZE.md §5 and RULE30-PRIZE.md §8.54, §8.57, §8.58 were written.
Pages and abstracts were read; no PDF could be opened, so Dubickas 2009, Jen 1990, Monks-Yazinski 2004,
López-Stoll 2009, Bernstein-Lagarias 1996 and Terras 1976 were seen only in abstract or through citing papers.

- **Collatz, W2 (complexity at least 1.71 n): FOUND, refereed, read in full 2026-10-06.** Dubickas, Glasgow Math. J.
  51 (2009) 243-252. Theorem 3 (the $\lceil px/q \rceil$ maps, $\liminf P/n \ge \log q/\log(p/q)$), Corollary 4 (the
  $\lceil 3x/2 \rceil$ sequence, $P(X, n) > 1.70951129\,n$) and Theorem 5 (the 3x+1 map on positive integers with
  $x_n \to \infty$: $P(X, n) > 1.70951129\,n$ for large $n$; "speculative" because conditional on a divergent
  trajectory). Integers only; rationals are not mentioned. He conjectures $P(X, n) = 2^n$. Credit settled: W2 for
  integers is his; ours adds odd-denominator rationals by the same count.
- **Collatz, W1 and W3: FOUND three times in 2026, all unrefereed** (GitHub notes of 2026-07-22 and 2026-09-22, a
  Zenodo record of 2026-10-02). Implied for integer orbits by Dubickas's Theorem 5; for slopes below $\log_3 2$ by
  Monks and Yazinski (2004), Theorem 2.7(b) (secondary account).
- **The lemma of COLLATZ-PRIZE.md §4**: the identity is Terras (1976) and Lagarias (1985, Theorem B), verbatim as
  Lemma 2.3 of arXiv:2602.10466; the least-residue bound is Kontorovich and Sinai's structure theorem, part two
  (arXiv:0910.1944, Theorem 5.2), in the odd-to-odd form.
- **arXiv:2101.12747** (López and Stoll, 2021): no refereed criticism, correction or confirmation found. The gap at
  its equations 15 and 16 (a real limit taken for a 2-adic one) is raised, with counterexamples and unanswered, in
  a public issue of 2026-09-30; a 2026 note calls it "an apparent gap".
- **Rule 30, Theorem A (Jen with a clock): NOT FOUND; NEAR.** Kopra (arXiv:2202.13809) Lemma 3.2 tracks the
  preperiod and Theorem 3.5 is the case $b = \infty$; Condrey (arXiv:2609.09431) Theorems 6, 7 and Corollary 8 bound
  the constant prefix of one column by $w + 2$ (period 1, from time 0, sharp). Nothing for period $P$, later windows,
  or pairs of columns.
- **Rule 30, Theorem A′ (the window principle): NOT FOUND; NEAR.** The mechanism is standard (Wolfram's prize post;
  Kopra, Definition 3.1). Its corollary $p(n) \ge n - L$ is weaker than Jen plus Morse-Hedlund. Dubickas's Theorem 3
  is the same count for the times-$p/q$ automata, which share Kopra's class with Rule 30; no common statement found.
  Kopra arXiv:2005.05112 computes the complexity of the whole trace subshift, not of one orbit.
- **Rule 30, Theorem E (Sturmian columns excluded): NOT FOUND.** Context: Rowland and Yassawi (arXiv:1209.6008),
  columns of linear automata are $p$-automatic, hence never Sturmian; Dolce and Tahay (DLT 2022, snippet only):
  Sturmian columns of quadratic slope exist in purpose-built automata.
- **Still to check:** whether the unboundedness of the left diagonals' periods (RULE30-PRIZE.md §8.59, Lemma B2) is
  in Jen (1986) or Rowland (2006, §5).

Sources opened for the Rule 30 statements: Kopra (two papers), the Kari-Kopra abstract, Condrey, Wolfram's prize
post and bibliography, the NKS Rule 30 note, Jen's OSTI abstract. Queries: Rule 30 with adjacent columns, window,
quantitative, Jen; left-permutive trace complexity from a finite configuration; Rule 30 Sturmian; Brunnbauer 2019
(diagonals only).


### GPT proof-audit reading (2026-10-06)

Read Rowland, [Local nested structure in rule 30, §5](https://ericrowland.github.io/papers/Local_nested_structure_in_rule_30.pdf),
pages 15–17, including the reset lemma and period-doubling proof. It discusses loss of seed information and the
first possible split at column 53209 (our zero-based diagonal 53208). The all-seed finite certificate in
RULE30-GPT.md G2 applies that mechanism; the branch construction was already in RULE30-PRIZE.md §8.31.
Unboundedness of diagonal periods was not found in this section; this is not a claim it is absent elsewhere.
Jen 1986 remains owed a full reading.

Checked the continued-fraction best-approximation input against Theorem 27 of the
[UNCG ergodic-theory lecture notes](https://uncg.edu/~cdsmyth/UNCG_Ergodic_Theory_Summer_School_2020_Final_Lecture_Notes.pdf).
G2 supplies a finite-offset argument for E Step 4. This standard input establishes no priority for the Rule 30
application, and no further literature search was made in this work block.


### GPT reset-front reading (2026-10-06 03:01 BST)

Re-read Rowland, [Local nested structure in rule 30, section 5](https://ericrowland.github.io/papers/Local_nested_structure_in_rule_30.pdf), pages 15–17: the black-parent reset and period-doubling mechanism. G6 applies that mechanism to the existing conservative front, not a new period theorem. Searches `"Rule 30" "settling" "left"` and `"Local nested structure in rule 30" left side reset period` returned this paper and related period sequences; no sub-3 all-branch settling theorem was found in these search results. This is a limited search, not proof of absence. The phase comparison below is an elementary order argument derived here; no priority claim.


### GPT waiting-budget and branch-tree check (2026-10-06 04:37 BST)

The source for the backward-reading argument is this project's RULE30-PRIZE.md Lemma B2, checked directly; the reset/extension mechanism is Rowland section 5, previously read in full. G7 states elementary quantitative consequences without claiming priority. Searches `"rule 30" "left side" "graph" period` and `"rule 30" "left side" "settling time"` found Rowland and a [2011 shift-subsystem paper](https://content.wolfram.com/sites/13/2019/01/20-1-3.pdf) (search result only, not read or used), alongside irrelevant results. No applicable all-branch sub-3 waiting bound was found in this limited search. G7's interval diagnostic applies existing evidence, not a new imported theorem.


### GPT finite local front potential (2026-10-06 04:49 BST)

G8 applies G7's unique-predecessor graph and G6's reset clock. The cycle obstruction and telescoping inequality are proved directly in G8. The graph/potential method is standard, not claimed novel. During this block, a search `Karp 1978 characterization minimum cycle mean digraph pdf Berkeley` located the [original Berkeley technical report](https://www2.eecs.berkeley.edu/Pubs/TechRpts/1977/ERL-m-77-47.pdf) and its [published abstract](https://www.sciencedirect.com/science/article/pii/0012365X78900110), which describes weighted cycle means and their algorithmic characterization. The archive PDF fetch returned403; the Berkeley EECS fallback succeeded and its full six-page text was read, including Lemma1's removal of negative cycles and Theorem1's characterization. Negating weights gives the corresponding maximum-reward statement used here. G8's specialized cycle traversal and reverse relaxation are not Karp's algorithm. The complete edge inequalities certify the result independently. No prior-art claim is made for the Rule 30 cycle or potential.


### GPT birth-restart transfer (2026-10-06 06:26 BST)

G9 uses elementary order distributivity: a monotone scalar map preserves finite maxima. No novelty claim for the maximum-over-restarts argument. Searches `Lindley recursion maximum partial sums workload queue lecture notes pdf`, `site.mit.edu Lindley recursion max partial sums pdf`, and `site.inria.fr max plus monotone maps distributivity maximum queue recursion` located reflected queue recurrences and max-plus methods. Read the publisher page of [Boxma et al., A multiplicative version of the Lindley recursion](https://link.springer.com/article/10.1007/s11134-021-09698-8), including its description of the classical queue special case, and the abstract only of [Akian and Fodjo, Probabilistic max-plus schemes for solving Hamilton-Jacobi-Bellman equations](https://arxiv.org/abs/1801.01780), which explicitly identifies distributivity of monotone operators with respect to suprema as a mechanism. Neither source supplies the Rule30 budget. Our nonlinear next-black maps are not asserted to be the classical additive Lindley recursion or globally max-plus linear. The scalar finite-maximum identity and its birth-budget consequence are proved directly in G9; no full-text priority survey was made.


### GPT aligned finite certificate audit (2026-10-06 06:35 BST)

G10 uses only mechanisms already read and credited in G7–G9: the project's unique predecessor, the maximum-cycle reward/potential argument (Karp report read in G8), and the temporal-rotation quotient proved in G9.4. Searched the repository for cycle means, potentials and aligned fronts before starting; no P6/P7 or P10 certificate was already recorded. No new external result or new literature priority is asserted. The additional periods test an existing candidate rather than import a new route. Exact edge inequalities and scalar witness checks establish the finite statements independently.


### GPT Condrey-end full reading (2026-10-06 07:05 BST)

Read all seven pages of [Condrey, Finite Configurations Cannot Generate a Constant Trace in Rule30](https://arxiv.org/pdf/2609.09431): triangular uniqueness; zero-trace invariant classes and OR latch; all-one checkerboard; finite-support corollaries; horizon proofs; conclusion and partial formalization limits. G11 distinguishes its zero-wall latch from its one-wall universal fibre. The one-hole prefix follows by applying the latter on the first black window and explicitly solving one inverse step; no novelty claim. Searches `"Rule 30" "one zero" periodic trace Condrey` and `"Rule 30" constant trace checkerboard preimage periodic holes`, restricted to arXiv and Rowland's site, returned Condrey, Rowland and other Rule30 papers but no exact repeated-hole budget usable here. This is a limited search, not proof of absence. Nersissian's period paper reappeared and was already listed in this document as abstract-only; it was not imported into this proof.

### 2026-10-06 — GPT G12, local hole shielding and the input time

Used the already-read Condrey triangular uniqueness and black-wall checkerboard (full reading recorded under G11), and the project's RULE30-PRIZE.md §8.2 Lemma4, rather than proposing a new ray or superposition route. G12's four-black-window shielding is a direct inverse-recurrence consequence of G11's first four cells; no independent priority claim. Local's C021 exploratory negative is retained: spreading on an earlier row differs from shielding on the injection row. This bounded algebraic audit did not conduct a new literature survey or import an external global propagation theorem.

### 2026-10-06 — GPT G13, synchronizing automata for a single inverse row

The project's §8.19 already reconstructs Rule30 preimages leftwards; G12 supplies injection-row agreement. Searches `"Rule 30" inverse synchronizing automaton` (arXiv/Complex Systems) and `synchronizing automaton reset word definition` (arXiv) returned Rowland's local nested-structure paper and general synchronization literature, but no directly usable Rule30 inverse-row reset-gap theorem. This limited search is not a novelty or absence claim. Opened [Maslennikova2014](https://arxiv.org/abs/1405.3576), **abstract only**, for the standard definition of a reset word; none of its complexity theorems was imported. G13 directly proves the four-state transitions and regular reset language, retaining a false first characterization. Survey results about random automata were not applied to this deterministic driver, and no uniform reset gaps were assumed.

### 2026-10-06 — GPT G14, extending the project's latch count

Read RULE30-PRIZE.md §8.2's Pell full-column count and Fibonacci visible language, §8.62/C022's white-wall latch and independent-shape bound, and the width-one golden-ratio control in `rule30_entropy.py`. G14 extends those elementary local rules to wall0^(p-1)1 with an exact two-state transfer matrix; the p2 case is credited as an existing result. No new external theorem, random-information hypothesis, or literature priority claim was imported. It is a bounded audit of the recorded mechanism, not a new global route or a substitute for Local's larger-width automaton.

### 2026-10-06 — GPT G15, arbitrary white-time gaps in the existing width-one envelope

Used RULE30-PRIZE.md §8.2's local constraints and known Fibonacci visible language, G14's exact latch count, and the project's width-one layer interpretation. G15 gives the elementary projected language for arbitrary white-time gaps by explicitly constructing each hidden interval; no new external theorem was invoked. The golden-ratio gap2 case is credited as known; gap>=3's full visible shift is only a one-layer relaxation, not a physical channel or prize claim. This is a bounded audit of the existing mechanism, with no claim of literature priority.

### 2026-10-06 — GPT G16, four-state refinement of the existing layer

Used the project’s layer update (`ladder.c`, §8.14/§8.20), §8.2’s known Fibonacci visible language, and G15’s width-one envelope. G16 directly composes the four-state relations and proves their eventual two-periodicity, rather than importing an external theorem or asserting novelty. It is a bounded audit of the same mechanism. The finite-state transducer distinction in C030 is proved in G16.3; no arbitrary driver was assumed to have a regular prefix language.

### 2026-10-06 — GPT G17, finite certificate in the existing right layer

Read the project’s layer definition, G16’s parity certificate, and the existing §8.20 projection machinery. G17 directly verifies the eight-state black relation and accepting subset graphs, proving equality of width-two/three languages. No external theorem or priority claim is imported; this is a bounded refinement and negative of the existing layer question, not a new global prize route.

### 2026-10-06 — GPT G18, auditing C032’s slow-switch proposal

Used Lemma1/§8.2’s future black-window checkerboard, G13’s inverse reset, G15’s latch language and C032/§8.63’s slow-wall proposal. G18 directly composes the existing inverse rule to certify a finite prefix and protected band. No new external theorem or priority claim is imported. The proposed complete per-period finite state is not assumed: a valid width-one tail counterexample identifies the missing closure premise.

### 2026-10-06 — GPT G19, balanced-latch finite-prefix obstruction

Used §8.2’s monotone right latch, G18’s exact prefix construction and C032’s slow-wall question. G19 directly lists all six prefixes for0^5 1^5 and independently evolves the64 small left seeds. This is a finite-window certificate, not a new global route or literature priority claim. No external theorem or asymptotic law was imported; the all-a support observation remains finite evidence.

### 2026-10-06 — GPT G20, another finite relation certificate in the existing layer

Used the existing layer definition (§8.14/§8.20, ladder.c), G16/G17’s subset-language proof and CONSTELLATION row16’s p5 question. G20 directly verifies a sixteen-state relation identity and extends six representative odd-period graphs to all odd p>=5. No external theorem or priority claim was imported; this is a bounded negative on the first restrictive width, not an assumed infinite-layer construction.

### 2026-10-06 — GPT G22, formalizing the recorded inverse-column rule

Used the inverse-column equation in CONSTELLATION row5/§8.36 and distinguished G7’s anti-diagonal predecessor coordinates. G22 directly constructs the image condition, fibres and finite-neighbourhood ternary recoding; no external entropy or CA classification theorem is imported. It claims no literature priority. A broader study of the induced CA still needs the standing literature check; the current result is a bounded algebraic formalization of the recorded rule.


- 2026-10-06, GPT G26 scope audit: Kopra (2023) Definition3.3/Corollary3.7 require left-spreading together with left-permutivity; Rule210 satisfies both. The Rule210 empty-left walled parity subsystem is Rule90; its return-path derivation uses standard Catalan decomposition, with binary generating series C(z)=1+z*C(z^2). These mechanisms are credited rather than proposed as new. Full-orbit compatibility remains separate.

- 2026-10-06, GPT G27: automatic-sequence terminology from Allouche/Shallit (2003), publisher extracts only, https://www.cambridge.org/core/books/automatic-sequences/B092437A099192BA22DE4CF638142558/listing . Three-state dyadic DFA derived directly, no novelty claim. Half-line obstruction reuses Jen/Kopra's zero-height periodic propagation with the boundary source of a left1 explicit; no assumed right-half realization.

- 2026-10-06, GPT G29: independently read Dubickas2009 Theorem5 and its proof (positive integers tending to infinity), https://www.cambridge.org/core/services/aop-cambridge-core/content/view/C40C0C07FEC20797475BB2899C436C9A/S0017089508004655a.pdf/on_integer_sequences_generated_by_linear_maps.pdf . The signed fixed-odd-denominator bound is the project's credited extension of the same divisibility/growth argument; exact rounding and cycle/interval controls are audits, not a novelty claim.

### Rule 30 on rings: what is tabulated (checked 2026-10-06, Local, for CONSTELLATION.md row 10)
- OEIS A334497, "Maximum value of eventual period for any starting configuration for a rule 30 cellular automaton in
  a cyclic universe of width n": 1, 1, 1, 8, 5, 1, 63, 40, 171, 15, 154, 102, 832, 1428, 1455, 6016, 10846, 2844,
  3705, 6150 (n = 1 .. 20). OEIS A334496, the period reached from the single cell: 1, 1, 1, 8, 5, 1, 4, 40, 72, 15,
  154, 102, 260, 1428, 1455, 6016, 10846, 2844, 247, 3420.
- NKS note 6.4 ("Periods in rules 30 and 45"): the single cell is not always the seed of the longest cycle (n = 13:
  832 against 260); a growth estimate near 2^(0.61 (n + 1)) for the maximum period appears in Wolfram's random-
  generator patent (US 4,961,159).
- Not found in the OEIS (searched "rule 30" with cycles / periodic / transient): the number of cycles by n, the
  number of states on cycles, the longest transient, or the gliding (rotation-invariant) cycles. `ring_census.c`
  computes all four exactly to n = 24.
- Triangle-size statistics (checked 2026-10-06): NKS note 6.1 ("Properties of initially random cellular automaton
  patterns"): "The density of triangles of size n goes roughly like 2^-n for rules 126, 30 (see also page 871), 150
  and 182 and roughly like 1.3^-n for rule 22", for random initial conditions, with no constant and no derivation.
  The 1984 Physica D paper is a scanned PDF (fetched; not text-extractable here; its text was not read). So the
  ratio one half is known approximately; the exact law 3 * 2^-(L+4) per cell from the invariant uniform measure,
  and its 0.1% match on the single cell's core (section 8.68), were not found. Page 871 of NKS is still to be read.



**2026-10-06 10:55 BST — GPT primary-source access update (G36).** The [Monks–Yazinski author PDF](https://monks.scranton.edu/files/pubs/AutoConjV13.pdf) is accessible despite the publisher403. Read the definition of Omega, Theorems2.1/2.7(b) and relevant proof portions, not the full paper. The rational divergent-orbit lower-density bound now has firsthand verification; global rationality preservation of the complement autoconjugacy is conjectural and equivalent to rational-orbit periodicity. G36 retains the square-zero route's limitation. This updates the earlier secondary-only/PDF-unavailable scope, without erasing that historical report.

### Collatz circuits (checked 2026-10-06, Local, for GPT's G47)
- R. P. Steiner, "A theorem on the Syracuse problem", Proceedings of the 7th Manitoba Conference on Numerical
  Mathematics and Computing (1977, published 1978), 553 to 559: there is no nontrivial 1-cycle (a "circuit": one
  run of odd steps followed by one run of even steps). Generalised by J. Simons and B. de Weger (2005) to m-cycles
  for small m. Found through the secondary literature (Lagarias's annotated bibliography); the paper itself not yet
  read. It closes G47's open clause: G47's surviving family members are circuits, so only k = 1 qualifies.



### 2026-10-06 — GPT G48: first-deficit scope and adjacent-swap prior art

[Primary author paper, Rozier–Terracol, arXiv:2502.00948v2](https://arxiv.org/html/2502.00948v2), Definition1.2 and Lemma2.1/proof read. The first-deficit census probes Terras's coefficient-stopping-time equality; the paper also supplies the known affine adjacent-swap comparison used in G40. Targeted reading only; original Terras PDF download failed. See RULE30-GPT.md G48 for scope and the retained small-start exception.

**2026-10-06 — GPT G50 primary-source scope update.** [Kari–Kopra, arXiv:1710.05737v1](https://arxiv.org/html/1710.05737v1): introduction, canonical base expansions, Lemma2.1/proof, base-six local-rule construction and trace Definition3.2/Corollary3.3 read. The full-alphabet local rule is not left-permutive; broader expansivity and selected real configuration realization must be checked separately. G50 specializes the already recorded decoupling mechanism; no novelty claim or whole-paper audit.

**2026-10-06 15:41 BST — GPT Collatz first-deficit envelope audit (G67).** Re-read [Rozier–Terracol arXiv:2502.00948v2](https://arxiv.org/html/2502.00948v2), Definition1.2, Lemma2.1 and Theorem2.2 with proof, not the whole paper. Actual/coefficient stopping-time equality is a conjecture for n>=2. The source's offset extrema range over unrestricted parity words. G67 conditions the same affine sum on the first-deficit barrier; its latest allowed odd positions are derived explicitly, with no novelty claim. No larger first-deficit census or external computational verification was audited.


**2026-10-06 — GPT G69 logarithmic-source audit.** Read [Rozier–Terracol v3](https://arxiv.org/html/2502.00948v3), Definition1.2 and Section6 around Proposition6.3: source-attributed Rhin exponent13.3 is unconditional; their later finite-total argument uses additional orbit conjectures. Original1987 Rhin proof not read. Read [Languasco–Luca–Moree–Togbé Theorem2.1](https://link.springer.com/article/10.1007/s12188-025-00293-9), positive rational Matveev statement and its prime-power-gap application. G69's barrier-conditioned polynomial ceiling is a direct synthesis, no novelty claim.

**New related preprint, audit required.** [Tong Niu, arXiv:2605.13886v1](https://arxiv.org/html/2605.13886v1), introduction and Sections3–4 sampled. It discusses fixed-length affine counting, overlapping G45's elementary residue/ceiling formulation. Displayed text defines r_w as normalized E, then inserts it as an integer intercept in the affine formula; those conventions differ by2^k. Its offset-bound proof also attributes the unrestricted maximum to ones-then-zeros, contrary to Rozier–Terracol Theorem2.2. The exact1100/0011 example gives B5/20 at a2,t4 and exposes that attribution reversal. These are specific textual normalization/order flags, not a complete refutation or audit of the manuscript. No count or acyclicity adjustment is imported from it.


### GPT G74 — backward first-step analysis, 2026-10-06

Existing-record search `adjoint`, `Duhamel`, `completion probability`, `backward kernel` found no earlier Collatz backward-completion identity in this record. Web searches `Markov chain perturbation telescoping finite horizon backward transition kernel Duhamel formula` and `site.maths.cam.ac.uk Markov chains backward equations discrete time transition probabilities lecture notes` located general perturbation work and teaching notes. Read [Chen's University of Washington lecture3](https://faculty.washington.edu/yenchic/18A_stat516/Lec3_DTMC_p1.pdf), section3.4 (pages5-6), which derives backward equations by conditioning on the first transition. G74 applies that elementary method to a killed, time-dependent fair-coin barrier and proves its finite telescoping identity directly. No published Collatz cancellation estimate is imported; no novelty claim or exhaustive prior-art search. The actual deterministic ensemble is not assumed Markov on odd counts.


### GPT G75 — binomial concentration and a dependent overshoot, 2026-10-06

The search `Hoeffding 1963 probability inequalities sums bounded random variables theorem 2 pdf` located [Hoeffding's original paper](https://www.cs.rpi.edu/academics/courses/spring06/random/hoefding.pdf) and its [publisher abstract](https://www.tandfonline.com/doi/abs/10.1080/01621459.1963.10500830). Only the search metadata and abstract excerpt were inspected, not the full paper. No general theorem from that paper is imported: G75 proves the required fair-binomial concentration estimate by its elementary cosh moment-generating function, and proves the central-atom estimate by induction. The reverse maximum and dependent truncation are derived directly from G74. No novelty claim, exhaustive literature claim, or independence of overshoot and endpoint count.


### GPT G78 — finite product-measure differentiation, 2026-10-06

Search `Russo formula derivative probability increasing event expected number pivotal original paper pdf` located [Grimmett's author-hosted Probability on Graphs draft](https://www.statslab.cam.ac.uk/~grg/books/pgs2e-draft.pdf), indexed section4.7, theorem4.66. Its search excerpt identifies the derivative as the mean number of pivotal coordinates for increasing events. Opening the PDF and locating that theorem failed with502; the full theorem was not read, and original Margulis/Russo papers were not audited. G78 directly differentiates its finite polynomial and separately differentiates each tail coordinate, so it imports no probability theorem. No novelty claim or assertion about actual Collatz class allocation. The method is the standard finite increasing-event sensitivity identity.


### GPT G82 — truncating a reverse maximum in time, 2026-10-06

Search `random walk maximum negative drift truncation anti concentration convolution binomial` located [Kugler and Wachtel's author preprint abstract](https://arxiv.org/abs/1107.5400), describing truncation methods for maxima of negative-drift walks. Only the search abstract excerpt was read; no theorem or constant was imported. G82 proves its bounded fair-bit coupling error directly with G75's tail estimate, then proves the binomial first-difference estimate by convolution and unimodality. Its moving ceiling barrier is handled explicitly. No novelty claim, exhaustive search claim, or transfer of iid assumptions to actual Collatz inputs.


### Owner's temporal-instrument connection — publisher abstracts checked, 2026-10-06

To situate the origin in WHAT-WE-BUILT.md, read the publisher abstract of Westerweel, Elsinga and Adrian, [Particle Image Velocimetry for Complex and Turbulent Flows](https://www.annualreviews.org/content/journals/10.1146/annurev-fluid-120710-101204), Annual Review of Fluid Mechanics 45 (2013). It describes time-resolved vector-field capture and discusses finite accuracy and spatial resolution; full text was not read. Also checked the publisher abstract of [3D Lagrangian Particle Tracking in Fluid Mechanics](https://www.annualreviews.org/content/journals/10.1146/annurev-fluid-031822-041721), volume 55 (2023): tracking individual particles provides position, velocity and acceleration. This supports the distinction between field changes at fixed locations and motion followed along trajectories. It does not establish equivalence of this project's video tracker to a calibrated PIV/LPT instrument, a performance or novelty claim, or a theorem about Rule 30. The discrete moving-frame identity proposed in the chat is elementary and will need its own scope audit before research use.

### GPT G98 — clock and causal-diamond scope audit, 2026-10-06

Read the abstract of Saravani and Aslanbeigi, [On the Causal Set-Continuum Correspondence](https://arxiv.org/abs/1403.6429): it treats number-volume correspondence and distinctions between small regions, sprinklings and large-volume lattices. No theorem from the full text was imported. Read the abstract/introduction of Baburin et al., [Universality Frontier for Asynchronous Cellular Automata](https://drops.dagstuhl.de/storage/00lipics/lipics-vol345-mfcs2025/html/LIPIcs.MFCS.2025.11/LIPIcs.MFCS.2025.11.html), MFCS2025: asynchronous simulation can use additional state, so a raw-update noncommutation guard must not be recast as impossibility of asynchronous simulation. G98's continuum Jacobian, discrete count, global-clock invariance and raw Rule30 update counterexamples are derived directly. No physics or novelty claim.

### Local — unequal ticks and asynchronous updating (the owner's question, CONSTELLATION row 19), 2026-10-06

Read via search summaries only, not the papers; status: pointers to read before any asynchronous run.

- **Nakamura (1974), asynchronous cellular automata and their computational ability.** Any synchronous $q$-state
  rule can be simulated by an asynchronous rule with the same neighbourhood and $3q^2$ states: a cell that has
  updated waits until its neighbours have caught up before its next transition, so it always reads the right
  generation. This is the classical form of GPT's G089 and G090 "versioned prior-generation reads": the synchronous
  history survives any schedule once each update reads the previous generation. Survey with the construction:
  Fatès, [A guided tour of asynchronous cellular automata](https://arxiv.org/abs/1406.0792).
- **$\alpha$-asynchronous elementary rules** (Fatès and co-authors, 2005 onward; Fatès, Thierry, Morvan and
  Schabanel, fully asynchronous double-quiescent rules, Theoretical Computer Science 2006): each cell updates with
  probability $\alpha$ per step; for some rules the behaviour changes abruptly as $\alpha$ varies, a second-order
  phase transition in the directed-percolation or parity-conserving class. What Rule 30 itself does under
  $\alpha$-asynchrony was not found in the summaries; to be read before any run.
- **Time Warp** (Jefferson's optimistic parallel discrete-event simulation) has been applied to simulations with
  asynchronous cellular automata ([core.ac.uk record](https://core.ac.uk/works/44253136)): processors run ahead on
  their own clocks and roll back when a late message arrives, which is the engineering form of the owner's unequal
  ticks with the synchronous history preserved.

Links: https://arxiv.org/abs/1406.0792 ; https://arxiv.org/pdf/2501.02578 ; https://en.wikipedia.org/wiki/Asynchronous_cellular_automaton ;
https://core.ac.uk/works/44253136 ; https://arxiv.org/abs/nlin/0703044

### GPT G104 — oriented random updates and spatial measures, 2026-10-06

Searched for asynchronous one-sided updates and invariant Bernoulli measures. Read the publisher abstract of Mairesse and Marcovici, [Probabilistic cellular automata and random fields with i.i.d. directions](https://www.numdam.org/articles/10.1214/12-AIHP530/), AIHP2014: it concerns synchronous probabilistic local updates and product invariant measures. Its update assumptions differ from our sequential raced-neighbour recursion; no theorem was imported. The search also returned [Orbits of the Bernoulli measure in single-transition asynchronous cellular automata](https://dmtcs.episciences.org/en/articles/2972); the page failed to fetch, so only its search excerpt about cylinder measures was read. G104 proves its oriented conditional inverse and first-row pair formula directly, with no novelty or exhaustive prior-art claim.

### GPT G105 — boundary and healing scope, 2026-10-06

Existing-record checks included RULE30-PRIZE.md §8.66 and PROOFS.md C.4 on background-dependent healing. Read the perturbation-wave section of [Formation of Morphogenetic Patterns in Cellular Automata](https://pmc.ncbi.nlm.nih.gov/articles/PMC7304752/): it already discusses Rule30's right-moving perturbation border and boundary-dependent recovery of periodic backgrounds. These are known mechanisms, not new discoveries here. G105 directly counts zero-row preimages in the finite cyclic snapshot/race implementation; no literature theorem or novelty claim is imported. The search is limited, not an exhaustive novelty audit.


### Projected memory and G112 (GPT, 2026-10-06)

Search: “Markov chain lumpability conditional past projected process criterion Kemeny Snell paper”. Read the abstract and metadata of Geiger and Temmel, [Lumpings of Markov chains, entropy rate preservation, and higher-order lumpability](https://arxiv.org/abs/1212.4375), revised2015. The abstract defines coordinate-wise projections and strong k-lumpability, with finite-state entropy criteria. Only the abstract was read. Projected Markov memory and higher-order lumpability are existing theory; those finite-state criteria are not invoked as an infinite-Rule30 theorem. G112 instead uses direct conditional probabilities, a local OR shielding identity and positive finite cylinders. Existing G102-G111 already supply masking, pulse echo and the finite table; no general theory novelty is claimed.


### GPT G131 — Sturmian block factors and orbit endpoints, 2026-10-06

Searched finite block coding of rotations with endpoints on one orbit. Read the publisher abstract of Kupsa and Starosta, [On the partitions with Sturmian-like refinements (2015)](https://www.aimsciences.org/article/doi/10.3934/dcds.2015.35.3483). It treats rotation partitions whose atoms are finite unions of half-open intervals with endpoints on one past orbit, and discusses stronger refinement/factor results. Only the abstract was read. G131 does not import those refinement or injectivity theorems: it constructs the finite XOR code directly and transfers the already proved Rule 30 repeat obstruction. These coding ingredients are established symbolic dynamics; no general coding novelty or exhaustive prior-art search is claimed.


### GPT — half-circle codes and the XOR-derivative bridge, 2026-10-07

Targeted record search for Rote, half-circle, antiperiod and Sturmian integration found no matching entry. Web query: “Rote sequences difference Sturmian sequences rotation half circle paper”. Read the abstract and introduction (printed pp.125–126) of Medkova, Pelantova and Vuillon, [Derived sequences of complementary symmetric Rote sequences](https://www.numdam.org/item/10.1051/ita/2019004.pdf), RAIRO 53 (2019), DOI10.1051/ita/2019004, also [arXiv1812.03748](https://arxiv.org/abs/1812.03748). The introduction states the known half-circle rotation construction and the equivalence between complementary symmetric Rote sequences and sequences whose modulo-two difference is Sturmian, crediting Rote. No later return-word theorem or algorithm was imported. GC158 tests only the elementary repetition transfer: the derivative loses the distinction between repeats and complement-repeats. This does not extend the Rule30 Sturmian exclusion to these codes.

## openai/math: a released collection of model-proved manuscripts (noted 2026-10-07, by Cloud)

[openai/math](https://github.com/openai/math), first commit 2026-10-06: 722 manuscripts (372 families) by an
unreleased OpenAI model, 162 with Lean formalisations, the rest at varying stages of verification. Read here: the
README and the catalogue (CONTENTS.md), not the proofs. Its claims on the prize pool are listed in PRIZE-PROBLEMS.md
§1, update of 2026-10-07.

For this record. No manuscript concerns Rule 30, elementary cellular automata, Collatz, Mahler's 3/2 problem, or
linear forms in log 2 and log 3 (the Collatz lane's G69 rests on Rhin's bound for those). Two are near neighbours.
Family 197 refutes Gottschalk's surjunctivity conjecture with an injective, non-surjective cellular automaton on a
nonsofic group; the integers are amenable, where the Garden of Eden theorem makes every injective automaton
surjective, so Rule 30 on a line is untouched. Family 017 proves that the irrationality exponent of π is exactly 2
(with Lean), a far sharper form of Lambert's 1761 theorem that π is irrational (the owner's question of 2026-10-06).

Use. Treat each manuscript as a preprint: prefer the Lean-formalised ones, check the main statement in the formal
file rather than the abstract, and cite the family number and manuscript title.


### GPT — Rote exponent comparison for the phase-zero repeat debt, 2026-10-07

Query: “Rote sequences critical exponent continued fractions parity numerators initial repetitions silver ratio”. Read only the abstract of Dvorakova, Medkova and Pelantova, [Complementary symmetric Rote sequences: the critical exponent and the recurrence function](https://arxiv.org/abs/2003.06916), DMTCS22(1), 2020. It gives continued-fraction formulas and a classification at critical exponent at most three. That ordinary factor exponent does not include our interval starting index a, so neither its classification nor the reported uncountability transfers to G144's boundary-phase debt. No paper theorem was imported; the G144 first-hit obstructions and converse are written out independently. No exhaustive novelty claim.

Independently read the current [openai/math README](https://github.com/openai/math), confirming that it presents manuscripts with differing verification status and warns of possible issues in unformalized results. This check does not verify any of CL010's headline mathematical statements or Lean artifacts. Local's catalogue-only Q7 scan is accepted separately; no mathematical result from the release is used here.

### Local — catalogue-only scan of openai/math for question 7, 2026-10-07

Scope, as GC161 set it: the release's `CONTENTS.md` only (all 372 family headers and every manuscript abstract
listed there), no proofs and no Lean files read. Keywords: Sturmian, Rote, rotation codes, mechanical and Beatty
words, balanced words, repetitions and critical exponents, three-distance, symbolic dynamics and subshifts,
cellular automata, combinatorics on words, inhomogeneous approximation. Result: no family or abstract is about
Sturmian, Rote or rotation codes, repetitions, critical exponents, subshifts or cellular automata on the integers, so
nothing in it helps question 7. Recorded and stopped. The three nearest, none usable:

| Family | Main statement, as the catalogue gives it | Formal artifact | Why it does not help |
|---|---|---|---|
| 022 | The weak inhomogeneous Duffin–Schaeffer conjecture: divergence of the totient-weighted series gives infinitely many solutions of the shifted approximation inequality for almost every x | no Lean link in the catalogue | a statement about almost every angle; our half-circle questions are about specific quadratic angles and fixed phases |
| 017 | The irrationality exponent of pi is 2 | Lean link in the catalogue | an exponent for one constant, not a method stated for rotation codes |
| 197 | A torsion-free nonsofic group algebra that is not directly finite; companion examples give injective nonsurjective cellular automata, refuting Gottschalk's surjunctivity conjecture | Lean link for the family; which statement it formalises was not checked | needs a nonsofic group; on the integers the Garden of Eden theorem holds (Cloud's CL010 reading confirmed against the catalogue) |

### GPT — periodic-predecessor parity, 2026-10-07

Query: “rule 30 periodic preimages period doubling synchronizing runs modulo 3”. Read the abstract and section 5 opening/proposition and proof of Eric Rowland, [Local Nested Structure in Rule 30](https://ericrowland.github.io/papers/Local_nested_structure_in_rule_30.pdf), Complex Systems16 (2006). Its period-doubling result concerns temporal diagonals in a left-justified evolution. G150 concerns spatial predecessors of a prescribed periodic row and derives its zero-gap criterion from the already recorded inverse transducer; no diagonal theorem is imported.

Also read only the abstract of [Diagonal Periods and Newton Supports of Rules 30, 86 and 135](https://arxiv.org/abs/2609.25077), submitted September2026. It claims unbounded single-seed diagonal periods and a backward periodic-tail map. The manuscript proof and relationship to G123/G124 or the wall route have not been audited. No result from it is used, and no novelty or exhaustive-search claim for G150 is made.

### GPT — diagonal-profile boundary audit, 2026-10-07

Read section 4 through Theorem13 of [Nersissian, Diagonal Periods and Newton Supports of Rules30,86 and135](https://arxiv.org/html/2609.25077v1). Checked the reset/integration argument and the finite-state first-hit proof. The latter counts absolute-time periodic profile pairs: a zero boundary is fixed and a nonzero boundary pair maps into it. Different transient lengths do not invalidate taking large times in each residue class. This shares G123's absorbing-orbit pigeonhole method, but follows temporal diagonal profiles rather than spatial ancestor rows.

**Unexpected map check, by hand.** Its backward map is B(u,v)=(S v XOR (u OR v),u). Our vertical inverse is H(a,b)=(S a XOR (a OR b),a), as in G128/G129. The shift acts on different coordinates. On constant tracks, B(0,1)=(0,0), whereas H(0,1)=(1,0) and H(1,0)=(0,1). Thus the same nonzero pair is absorbed in B and cycles in H; even their constant-track graphs are not conjugate. No wall conclusion or novelty claim is imported. The remaining manuscript, its numerical data and support representations were not audited here.

**GPT follow-up to Local L107 (2026-10-07).** The constant-track guard excludes even an injective encoding between these two full pair spaces that intertwines their depth maps and commutes with, or reverses, temporal shift. A shift-fixed pair must map to a shift-fixed pair. There are four such pairs on each side; injectivity makes the restricted map a bijection, hence a conjugacy of the two four-state depth graphs. Their periodic-point counts, one for B and three for H, contradict this. No continuity or local-code assumption is needed. This strengthens the failed faithful-identification route, not a general ban on transfers. The identified unexpected countercheck is the non-injective map sending every pair to (0,0): it intertwines both depth maps and respects shift in either direction. It carries no nonzero boundary information. Any useful factor-map bridge would therefore need an explicit boundary-preservation hypothesis, not just shift compatibility. This is an elementary audit of the recorded maps, not an imported theorem or a new numerical experiment.

### GPT — rotation-quotient first-hit bound, 2026-10-07

Read the abstract of Frati, Petak and Cheney, [Networks of Binary Necklaces Induced by Elementary Cellular Automata Rules](https://arxiv.org/abs/2409.04780) (2024): quotienting cyclic CA states by rotation is established, not a new method here. Their full paper and data were not inspected. Also read Klaus Sutner’s [Moebius Inversion lecture notes](https://www.cs.cmu.edu/~cdm/resources/24-moebius.pdf), pages5–8 and12–14, for divisor inversion, primitive words and necklace counts. G152 combines these standard counts with the recorded G124 period classification and a self-contained absorbing-orbit argument; no source theorem about Rule30’s zero basin is imported. Search “Rule30 zero periodic configurations necklace transient bound” located the necklace-network paper but no checked exact bound of this form. This is a limited search, not evidence of novelty.

### GPT — Rudin–Shapiro logical repeat-filter lane, 2026-10-07

Read Shallit and Xu, [Repetition factorization of automatic sequences](https://arxiv.org/html/2311.14961v2), section2 through Theorem2 and its repetition-predicate construction; also section6's stated Rudin–Shapiro result and proof outline. The cited first-order decision theorem covers addition, comparison, quantifiers and sequence indexing. Their repetition-factorization widths are not the project's start-index repeat debt, and no factorization theorem is imported as an exclusion. The RSP formula is an application of the standard method, not a novelty claim. Searches for Rudin–Shapiro repetitions and Walnut found this primary source and Rampersad–Shallit's summatory-function work; the latter's proof was not read or used here.

**RSP tool provenance.** Used the official [Walnut7.1.0 source](https://github.com/Walnut-Theorem-Prover/Walnut/tree/67e69c248d07324b25de1d4a498e877ac504999a), pinned before runs, and its supplied RS output automaton. The source was built in an isolated temporary toolchain. G153 records the exact formula, relation hash, instrument controls and independent product replay; semantic review remains pending. A raw tool decision is not claimed as an independently verified proof.

**G154 scope and method (2026-10-07).** This adapts the existing G147 countable/dense phase argument to a minimal symbolic trace family, using G140's reviewed coding and radius clock. The Rudin–Shapiro substitution is derived directly from its binary digit recurrence; bounded-gap minimality and nonperiodicity are proved in the entry, not imported from an unread substitution theorem. Countability, atom propagation and the isolated-point argument are elementary. No novelty is claimed for those general dynamical facts, and no generic exclusion is treated as exclusion of the specified original word.

**RSP verification update (2026-10-07).** Local L111 audits the direct LSD reconstruction and debt comparator and independently replays them, discharging G153's dependency on Walnut compilation semantics. The standard automaton method remains prior art. G153 is a reviewed computer-assisted necessary-filter pass, not a finite-wall construction.

**G155 method/scope (2026-10-07).** The two-supertile count is proved directly from G154's length-two four-letter substitution; no exact published Rudin–Shapiro factor formula is asserted or needed. This applies elementary factor counting to the reviewed wall-prefix locality, improving G147/G154's fixed-radius exception bound. It does not infer positive entropy or specified-word exclusion.

**G156 edge-diagonal correction of scope (2026-10-07).** Re-read section4 through Theorem13 of [Nersissian's paper](https://arxiv.org/html/2609.25077v1). Its B(u,v)=(S v XOR (u OR v),u) matches G7's diagonal-tree predecessor exactly. The previous comparison to the vertical wall inverse H remains valid: they shift different coordinates. The paper's absolute-profile bound therefore has a direct diagonal interpretation, without a wall conjugacy. G156 combines that existing first-hit mechanism with standard four-letter necklace counting, derived in the proof; no paper result is imported as a waiting-time or vertical-wall theorem. The theorem's record-spacing question remains open. Sections4.3-4.4 were inspected for scope: their finite support representations depend on actual period/transient sizes, and the formal milestone polynomial is explicitly not identified with a physical diagonal. Neither is used as a uniform bound.

### GPT — exact Rudin–Shapiro factor complexity, 2026-10-07

Read Allouche and Shallit, [Complexité des suites de Rudin-Shapiro généralisées](https://www.numdam.org/item/JTNB_1993__5_2_283_0.pdf), Journal de théorie des nombres de Bordeaux5(2),1993, printed pages285-288, section2 through Proposition2 and the small-length table. Theorem1 gives P_r(k)=8k-8 for k>=8. The four-letter substitution and binary coding match G154 after a'=c,b'=d; d=1 is the adjacent-11 parity word. Rendered formulas were checked because extracted text omitted inequality signs. The length-eight base enumeration is accepted as part of the published proof, not rerun. The later generalized-sequence proof was not read or imported. G155's application is N_(X_r)(L)<=8*ceil(L/2)-8 for L>=15; it counts possible exceptions rather than deciding existence. The paper's table at k=7 gives46, which is an explicit guard against extending the affine formula to all lengths. No new factor census.

**G157 finite-tree transfer (2026-10-07).** Re-read [Nersissian section4, Theorems10-12](https://arxiv.org/html/2609.25077v1): active drivers reset and preserve a common period, inactive drivers integrate with a possible doubling, and initialized diagonal tails have dyadic periods. G157 proves this mechanism for arbitrary two-sided periodic rooted histories and derives equality of the period-P and period-2^v2(P) trees. This is a finite-tree corollary and scope transfer, not novelty claimed for the underlying dyadic-period theorem or a physical-transient bound.

**G158 quotient branching (2026-10-07).** The reset/integration mechanism already checked in Nersissian section4, Theorems10-12, supplies the scalar recurrence classification. G158 adds the parent-stabilizer argument for child rotation orbits and the elementary finite-tree leaf count. Existing G152 concerns a spatial transition quotient that may merge, not this rooted edge tree. No literature novelty claim is made for integration or tree counting.

**Temporal-difference reformulation (2026-10-07).** Read [Nersissian section2.3, Theorems1 and4](https://arxiv.org/html/2609.25077v1), on the highest surviving Newton index, exact dyadic period, and finite-difference companion order. The G158-G161 source addendum derives the cyclic operator identities directly and uses them to restate the reviewed zero-driver parity test. This is standard GF(2) difference algebra; no novelty or new rooted absence theorem is claimed. Formal polynomial lifts of physical transients are not imported.

**Existing-record correction (2026-10-07).** G2.3 already derives the reset/even-parity classification and certifies the first genuine period16 split at diagonal53208, with an independent spatial-update check and disjoint cycles. G158 and G161 restate that mechanism in rooted-tree/orbit terms; the first branch is not new or unresolved. FBR16's no-branch prediction is rejected by prior evidence, retained honestly, and any completed new path run is only an independent replay.

**G163 monotone timing maps (2026-10-07).** Read the primary [Mathlib translation-number module](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Dynamics/Circle/RotationNumber/TranslationNumber.html), its introductory statement and declarations for phase-independent limits, bounded iterate displacement and translation-number powers. The general monotone degree-one mechanism is established prior art. G163 gives a self-contained integer-period proof and applies it to the full-line reset return map, deriving a discrete P-1 error and a bounded whole-block potential. This is neither a new rotation theorem nor a Lean-checked Rule30 proof. Existing G6, G8 and G10 are the internal comparison/finite-cycle records. Continuity and invertibility are not imported; no uniform compatible-cycle slope or transient-tree debt bound follows.


**HG4 horizon interpretation (2026-10-07).** Read the primary [CMU CS15-451 Lecture13, shortest paths](https://www.cs.cmu.edu/afs/cs/academic/class/15451-s14/www/LectureNotes/lecture13.pdf), pages3-6: bounded-edge Bellman recursion and Johnson potential reweighting with its telescoping identity. G166 uses the reward-sign version and a free stopping option to identify stabilization with shortest tight-edge distance to zero potential. G8/G10 already supply the internal least-potential framework. This is a standard finite-graph interpretation, not a new shortest-path theorem or a Rule30 compatibility bound.


### GPT — companion-paper frame constraint, 2026-10-07

Read the abstract, definitions and section10 through the opening of10.2 in [Nersissian, Diagonal Bases and Diagonal Periods of Elementary Cellular Automata](https://arxiv.org/html/2609.25078v1). Theorems7–9 identify Pascal as the unique lower-triangular binary transform making truncated OR convolution pointwise, while transporting truncated increment J to strict prefix XOR L. Full prefix I+L is a different operator. Nonzero nilpotent J cannot be diagonal in any invertible binary linear frame.

**Unexpected boundary check, by hand:** at length2, J sends e0 to e1 and e1 to0, hence J²=0 but J is nonzero; at length1, J=0 and the obstruction disappears. This concerns truncated coefficient increment, not G161's cyclic temporal difference.

The supplied-window recurrence cost does not improve the same rotated local update. Section10.2 separates constructing a support representation from querying it. No cumulative rooted-return estimate was established by this bounded reading; the remaining manuscript was not audited. No new computation, novelty claim or period-growth result.


**Companion growth-scope follow-up (GPT, 2026-10-07).** Read sections12.1 (Theorems12–13 and Corollary9),16–17 and the opening of19 in [Nersissian's companion paper](https://arxiv.org/html/2609.25078v1). The integer lift has Fibonacci degree, yielding an exponential period ceiling after reduction. This is an upper bound, not an asymptotic equality or a least binary interpolation order. Section17 explicitly leaves jump spacing undetermined. Its right-column recurrence and single-seed census do not provide an all-history bound for our rooted left-side stages.

**Unexpected hand check:** the stated recurrence gives D0=1, D1=t and D2(t)=sum_(u<t)(2u+1)=t². Its integer degree is2, but modulo2 it equals t, with period2 rather than the permitted ceiling4. Thus exact integer degree cannot be transferred to least binary order. This source check supplies no rooted cumulative-return estimate; uninspected sections and the census data were not audited or rerun.

### Cloud — a scan for outside work on period 2 since Condrey, 2026-10-07 21:22 BST

Asked by the owner's steer to find a weakness "by any means", Cloud first checked whether anyone outside had found
one. Searches: Rule 30 centre column period two finite configuration 2026; Condrey follow-ups on eventual period
two; Rule 30 prize progress 2026. Nothing found settles period 2 or offers a ready-made lever. What turned up:
- Condrey's own repository, github.com/dcondrey/rule30, is listed by the search engine as "Proof-oriented,
  reproducible research on the Wolfram Rule 30 Prize Problems: partial theorems, exact certificates, and audited
  experiments", but returned HTTP 404 when fetched. Its contents were not read; worth retrying.
- [Patto1155/rule30-foundry PR 47](https://github.com/Patto1155/rule30-foundry/pull/47): audits the
  right-special-factor route and finds it is Prize 1 restated (by Morse–Hedlund: right-special factors at every
  length are equivalent to non-periodicity). Certified p(n) = 2^n for n up to 18. Not a route.
- [fabianxvogt/rule30](https://github.com/fabianxvogt/rule30): no solution claimed; the centre column has no
  eventual period up to 2,048 in its first million bits. Its statement of the barrier is worth keeping: "Two adjacent
  periodic columns ⇒ everything left of them periodic ⇒ contradiction. (Proved.) One periodic column gives _no_
  known second periodic object."
- [TheJustinSunPrize/awards issue 774](https://github.com/TheJustinSunPrize/awards/issues/774) (2026-09-17): lists
  the centre column's aperiodicity with the prize as USD 10,000, from rule30prize.org; no new prize.
- The woahwhattheheck/commons issue 15314 and PR 15318, Condrey's paper and Nersissian's papers, all already here.
This is a limited search, not a novelty audit.

## The move to a finite window, read at the source: Bugeaud and Dubickas (read 2026-10-07, by Local, for Q2)

- **Bugeaud, Y. and Dubickas, A., "Fractional parts of powers and Sturmian words"**, C. R. Acad. Sci. Paris, Ser. I
  341 (2005) 69-74 (read in full, all six pages; doi 10.1016/j.crma.2005.06.007).
  - **Theorem 2.1.** For an integer b >= 2 and irrational xi, the numbers {xi b^n} cannot all lie in an interval
    shorter than 1/b. They all lie in a closed interval of length 1/b exactly when xi = g + k/(b - 1) + t_b(w), with
    w a Sturmian word on {0, 1}: the extremal cases are Sturmian.
  - **The mechanism.** A window shorter than 1/b confines the b-adic digits to two adjacent values. Irrationality
    makes the digit word aperiodic, so by Morse and Hedlund it has at least m + 1 factors of each length m. Then for
    every m some factor w_m occurs after both a 0 and a 1. The two tails then differ by more than 1/b - b^(-m), so
    the window has length at least 1/b. This is combinatorics on words, not pigeonhole over a bounded set; GPT's
    GC360 was right to reject my recalled version (L217, L219).
  - **The general p/q case,** Flatto, Lagarias and Pollington's theorem and its extension to algebraic numbers that
    are neither Pisot nor Salem, is Dubickas's, in the papers cited there as [4, 6]. It works through the "reduced
    length" of polynomials, with ell(qX - p) = p. Not read yet. (comb note, 2026-10-14, Local, SW-01: the p/q
    bound, length at least 1/p, is Flatto, Lagarias and Pollington's 1995 Theorem 1.4, above. What is credited to
    Dubickas, per refs [4, 6] here and Stephan's paper 1, is the extension to algebraic numbers that are neither
    Pisot nor Salem and the closed length-1/p case. Neither of the Dubickas papers [4, 6] has been read.)
  - **For us.** The extremal Sturmian case matches the record's Theorem E, which excludes every Sturmian column 1.
    The step "a factor preceded by two different letters forces a spread" is the shape of §8.58's window identity,
    where two times at which column 1 agrees for n steps force a zero run in the left half. Morse and Hedlund give
    such factors at every length in any aperiodic column 1. What Q2 needs is the converse pressure: a bound on zero
    runs that forbids them.
- **The general p/q case: Dubickas's reduced length** (found 2026-10-07 by search; Dubickas, Bull. London Math. Soc. 38
  (2006) 70-80, and the papers cited in Bugeaud and Dubickas as [4, 6]; the argument below is reconstructed from the
  definition and the search summaries, not read in the paper). For algebraic alpha with minimal polynomial
  P = sum p_k X^k, write xi alpha^n = x_n + r_n. Then sum p_k x_(n+k) = -sum p_k r_(n+k), an integer, because
  P(alpha) = 0. If every r_n lies in an interval of length L, the right side ranges over a window of length
  L * L(P), with L(P) the sum of |p_k|. If that is below 1, the integer is constant, the x_n satisfy a linear
  recurrence of fixed order, and that contradicts the hypothesis on xi unless alpha is Pisot or Salem. Replacing P by
  PQ for a normalized Q lowers L(P) to the reduced length ell(P), and ell(qX - p) = p gives Flatto, Lagarias and
  Pollington's 1/p. **For Q2:** the finite object is a fixed-order integer recurrence. A Rule 30 analogue would need a
  linear form of bounded order in column 0's and the left half's cells, forced constant by a window of the wall,
  which would put column 1 under a linear recurrence. Rule 30's OR is linear only where one input is known, so
  whether such a bounded-order relation exists inside zero runs is the Q2 question in FLP's terms.

### Local — unimodality of the Collatz demand law (Q9), searched 2026-10-08 05:37 BST

Searched before any proof attempt of "every actual demand law is unimodal" (DU, L275). Two standard web searches; the
items below are known from search summaries, not read in full.
- **Keilson and Gerber, "Some results for discrete unimodality", JASA 66 (1971) 386-389.** On the integers, a law is
  strongly unimodal (its convolution with every unimodal law is unimodal) exactly when it is log-concave. This covers
  the (1,1) part of the demand step, so unimodality can only break at the absorbing edge.
- **Passage-time unimodality** for one-dimensional strong Markov processes and its random-walk analogue (found as an
  Ann. Probab. item) concerns the law of the TIME of first passage, not the law of the minimum LEVEL at a
  fixed horizon, which is what the demand is (L275: d_a = P(min over s of (S_s - ell_s) = -1 - a)).
- **Log-concavity of exit distributions** of walks in bounded regions (a UCLA preprint found by search) cannot apply
  as stated: L048 shows the actual demand is not always log-concave.
No result was found on unimodality of the running minimum of a nonhomogeneous skip-free walk at a finite horizon. The
question stays ours; a proof would need an edge invariant that survives the critical/noncritical schedule.

### GPT GC487 automatic-kernel scope audit (2026-10-08)

Searches `site.cs.uwaterloo.ca Shallit k kernel automatic sequences finite kernel` and `site.writings.stephenwolfram.com rule 30 prizes automatic sequences` located Shallit's [Automatic Sequences slides](https://cs.uwaterloo.ca/~shallit/Talks/cant22-m.pdf). Read pages16-17: kernel definition and finite-kernel characterization statement, not an imported proof. GC487 independently proves a positive-continuation state-size lemma for canonical-binary LSB-first DFAO and a conditional finite-kernel indexing construction. Existing G137/Walnut prior art concerns automatic-word predicates, a different application. Finite signature counts cannot prove nonautomaticity, and nonautomaticity alone would not settle Rule30 indexing hardness. No novelty claim for kernel theory.


**GPT GC490,2026-10-08 — bounded parity-of-square-root search.** Query `automatic sequence "floor" "sqrt" squares nonautomatic` found no relevant primary-source treatment of the particular spin (-1)^floor(sqrt(n)) in the returned results. NOT FOUND in this bounded search, not a novelty claim. No secondary result imported. GC490 gives its discrepancy, explicit infinite decimations and arithmetic indexing proofs directly as a scope control; standard finite-state background remains GC487's Shallit source.

### 2026-10-08 — GPT GC520, zero-fibre contraction and bounded run search

Re-read the primary [Condrey paper](https://arxiv.org/html/2609.09431v1), already fully credited under G11, and the [Wolfram prize announcement](https://writings.stephenwolfram.com/2019/10/announcing-the-rule-30-prizes/). GC520 applies their recorded context to GC513/GC517; it asserts no new fibre classification. Searches for arbitrarily long Rule 30 centre runs, central-column run proofs, and constant-run results on Wolfram and Complex Systems domains found no usable selected unbounded-run theorem. Search scope was bounded; this records a failed lead, not absence of prior art. No statistical or secondary-source assertion was imported.

### 2026-10-08 — GPT GC521, actual unit-jump return constraint

Checked GC505-GC512 and the existing damage derivative record for all-time reversal and bounded-width escape results before claiming this block. GC521 extends the recorded initial reversal directly from Rule 30's local truth table; no external speed theorem or novelty priority is asserted. Its 128 finite local controls do not estimate transport. The larger-jump obstruction is retained rather than inferred away from conditional freshness.

### 2026-10-08 — GPT GC522, larger-jump return guard

Read GC507-GC508's finite jump/reset family and GC521's exact unit-reversal proof before this block. The first two healed-site equations directly supply the new guard; no external transport result or novelty claim is imported. GC507's existing N=1 example independently refutes all-positive immediate reversal. Local controls do not establish iid reachability or a long-time recovery law.

### 2026-10-08 — GPT GC523, actual escape template

Checked GC507-GC508's finite perturbation family and GC509-GC512's exposure and recurrence records before the audit. The invariant template follows directly from local Rule 30 updates; no external novelty or transport theorem is claimed. GC507's already-recorded N=1 example independently enters it. The finite-background construction and iid null-event caveat are retained separately.

### 2026-10-08 — GPT GC524, exact escape corridor probability

Used GC523's local template and G97's already-recorded spatial fair-product invariance. The two-step corridor inversion, finite time/site union and summable-event argument are elementary direct deductions; no new literature priority or external speed theorem is asserted. Adaptive-start conditioning is deliberately not replaced by an iid assumption. No new experiment was run.

### 2026-10-08 — GPT GC525, exact bulk-equivalence bridge

Checked the repository's right-edge confinement question and seed/trace-equivalence references before applying GC523's exact support. This is a direct corollary of that pending template proof, with no new classification or literature-priority claim. The right-light-cone disagreement is retained as the limit of the interior-equivalence statement. No new experiment was run.

### 2026-10-08 — GPT GC526, width-two confinement guard

Checked the existing confinement and damage-width record before using GC521's unit reversal and GC524's exact corridor probability. This direct width-transition deduction asserts no external novelty or general transport theorem. The endpoint reversal and deterministic singleton position are audited explicitly; no experiment was run.

### 2026-10-08 — GPT GC527, weighted front-displacement budget

Checked the existing jump-frequency and weighted-jump record before combining GC521 unit reversal with GC512 finite-exposure bounds. The pairing inequality is a direct elementary consequence, with GC505 and GC523 endpoint controls; no external novelty or transport estimate is asserted. No experiment was run.

### 2026-10-08 — GPT GC528, MSB convention audit

Used GC487's already-read automatic-sequence context and fixed sample. The separate prefix-state argument is direct deterministic-automaton reasoning, with no novelty priority asserted. No external result, larger sample or asymptotic automaticity claim is imported.

### 2026-10-08 — GPT GC529, defect-process definitions

Searched Rule 30 speed/Lyapunov and single-perturbation literature. Opened the primary [Baetens and Gravner author PDF](https://www.math.ucdavis.edu/~gravner/papers/bg2014.pdf) and [arXiv abstract](https://arxiv.org/abs/1509.06639). Read section 2.2's replica construction and the Rule 30 figure discussion, not the full paper. Its numerical profile is not imported as a simultaneous single-flip speed theorem. GC529 supplies our own local comparison counterexample; no source error or novelty priority is claimed. No usable rigorous iid single-flip speed theorem was found in this limited material; absence is not established. The earlier search-only Bagnoli entry remains unchanged.

### 2026-10-08 — GPT GC530, extremal-exponent quantifiers

Read primary [Tisseur PDF](https://arxiv.org/pdf/math/0312136), introduction, section 3.1 definitions and Proposition 3.1 statement, section 3.2 definitions and Proposition 3.2 statement with the adjacent convergence question. This upgrades targeted definition reading only, not a full-paper/proof audit. GC530 directly proves radius-speed extremal values for the iid full shift by finite zero windows, with no novelty priority asserted. The spatial maximum and arbitrary one-sided perturbation class differ from our fixed-origin single flip. Average definitions use liminf and cannot be cited as convergence of their defining sequence.

### 2026-10-08 — GPT GC531, plus shielding endpoint

Checked [Tisseur's primary definition](https://arxiv.org/pdf/math/0312136) against the existing exact rightmost-damage law. GC531 derives the plus shielding value directly, with no external novelty assertion. Correction to GC530 source labels: section 3.1 defines propagation, 3.2 contains Proposition 3.1, and 3.3 defines averages and contains Proposition 3.2. No full-paper or general convergence proof is claimed.

### 2026-10-08 — GPT GC532, running damage span

Checked GC509-GC512's exposure definitions, GC526's width-two limitation and the existing damage-width record. The running-maximum identity follows directly by substituting J_t=-w_t; no external novelty or theorem is imported. Existing first-step and GC523 cycle controls retain the endpoint offset. No experiment or broader width census was run.

### 2026-10-08 — GPT GC533, critical-ray recurrence scope

Searched “Rule 30 ergodicity sigma F characteristic direction cellular automaton directional mixing” and “cellular automata permutive directional ergodicity boundary light cone Rule 30”. Opened [Kopra, Rapid left expansivity](https://www.utupub.fi/bitstream/handle/10024/174540/1-s2.0-S0304397522007502-main.pdf?isAllowed=y&sequence=1), inspected section 2 definitions and searched its text for ergodicity; no matching theorem was found there. This is targeted reading, not a full audit. The already-recorded Shereshevsky thesis mixing hypotheses do not apply to the critical moving map with left endpoint 0; attempting to open its linked PDF failed, so that entry remains attributed to its original reader. No usable critical-ray visit theorem found in this limited material, not an absence claim. GC533's finite zero-cone escape witness is a direct derivation without novelty priority.

### 2026-10-08 — GPT GC534, critical-ray search retained

Follow-up queries: “rule 30 sigma ergodic”, “x0 x1 Shereshevsky ergodic”, and “Rule 30 directional mixing”. No usable primary theorem for the specified nonlinear critical map was obtained; search snippets are not imported as evidence. The existing negative-neighbourhood mixing scope remains unchanged. GC534's skew-extension and invariant-sign test are direct algebra, with no novelty claim and no measurable phase solution. Fixed-seed additive-potential exclusions such as GC483 concern a different equation and are not transferred here.

### 2026-10-08 — GPT GC535, finite-prefix phase exclusion

Checked the existing local-invariant, potential and phase record before auditing GC534's specific right-tail equation. The positive-cylinder and compactness arguments are direct; no external theorem or novelty priority is asserted. Unlike GC483's fixed-seed additive potentials, this concerns invariant signs of the iid critical-ray factor. Null fixed points are explicitly insufficient for the unrestricted measurable question. No finite phase census was run.

### 2026-10-08 — GPT GC536, measurable approximation scope

Checked GC534-GC535 and the earlier finite-model approximation guards. The error floor uses only the established positive cylinder, invariant tail measure and union bound; the marginal check uses equal old/new marginals. No external rate theorem or novelty priority is imported. The standard finite-prefix approximation principle is used only to retain the unresolved measurable limit, not to assert a convergence rate or invariant phase.

### 2026-10-08 — GPT GC537, fresh two-branch transition

Checked GC507's complete damage derivative, GC509's pre-pivot exposure and GC505's exact first-step laws. The strengthened full damage-word transition is a direct finite-cone consequence; no external novelty or regeneration theorem is imported. The existing conditional-selection and singleton-reset failures retain their scope. No new enumeration or speed fit was run.

### 2026-10-08 — GPT GC538, restricted fresh-return transport

Checked GC521's actual unit reversal, GC510's signed exponential moment bound and GC537's full fresh branch before deriving the restricted one/two-update return accounting. No external renewal theorem, novelty assertion or speed measurement is imported. The hypothesis retains a genuine fresh starting tick and the global martingale probability-one set, avoiding both vacuity and conditioning on future survival. No experiment was run.

### 2026-10-08 — GPT GC539, large-block time accounting

Checked GC532 running span, GC537 predictable healing offset, GC538 safe return blocks and GC510's signed moment bound. The time partition and terminal-deficit budget are direct identities and bounds; no external renewal theorem or novelty priority is asserted. Existing GC523 escape and safe endpoints are controls, with their deterministic versus iid scope retained. No experiment or occupation fit was run.

### 2026-10-08 — GPT GC540, record-average transport criterion

Checked the existing fresh-record, span, unit-return and unfinished-block arguments. The conditional ratio is direct telescoping and finite-growth interpolation, not an imported renewal-reward theorem or a novelty claim. No iid block, invariant induced law or finite-mean return theorem is presumed. Existing conditional safe endpoints and deterministic finite-record escape audit its scope; no experiment was run.

### 2026-10-08 — GPT GC541, predictable deterministic return

Checked GC509's exposure boundary, GC537's known healing branch, GC538 safe returns and GC540 average criterion. Determinism until the next exposure and the disjoint last-record identity are direct consequences, with no imported renewal theorem or novelty priority. GC523's finite-background infinite excursion retains its iid-null scope. Pre-pivot measurability is distinguished from finite decidability and from conditioning on future escape. No experiment was run.


### 2026-10-08 — GPT GC542, normality versus indexed computation

Existing-record search found no Champernowne entry; checked GC487, GC518, GC519 and GC528 for the already recorded distinction between finite-state certificates and arbitrary indexed algorithms. Read the primary chapter [Normal numbers and computer science](https://www.irif.fr/~carton/Enseignement/MPRI/Dynam-symbol/Documents/chapter.pdf), printed pages 2-3, for base-specific Champernowne normality and its overlapping-block meaning. Its printed page 18 explicitly warns that its mathematical-operation counts neglect arbitrary-precision arithmetic. Read [Alvarez and Becher (2017)](https://www-2.dc.uba.ar/staff/becher/papers/mcom3188.pdf), printed page 2930, for the decimal construction's independent-digit versus prefix distinction. GC542 proves its own conservative binary bit-cost bound and invokes established normality only. The PNAS PMC page was blocked by a browser challenge; no claim relies on that unread source. This classical counterexample has no novelty priority and is not a Rule 30 realization. No experiment was run.


### 2026-10-08 — GPT GC543, fixed-offset recovery obstruction

Checked GC524 exact finite corridors, GC532 span records, GC537 pre-pivot offset and GC541 duration convention before removing the forced pivot from the encounter cylinder. The positive-probability fixed-K duration obstruction is a direct contraction of existing results; no external theorem or novelty claim. No corridor extension, enumeration or speed fit was run. The iid-null infinite intersection and absence of mean or upper-tail conclusions are retained.


### 2026-10-08 — GPT GC544, adjacent run-duration scope

Checked GC494 run-pair cancellation, GC495 checkerboard mismatch and GC496 unequal-distance arrival, and searched the existing Rule 30 records for the solid-interval duration family. The exact one-step row and cone arrival give a direct finite-seed obstruction to a duration-only adjacent-run bound, with no external theorem or novelty claim. No enumeration or measurement was run. It does not assert reachability of these seeds at singleton run starts.


### 2026-10-08 — GPT GC545, white-start predecessor constraint

Checked GC495-GC496, GC517 and GC544, and searched the existing Rule 30 record for a solid-block predecessor condition. The exact left distance and necessary right prefix follow directly from Rule 30's XOR/OR update, with no external theorem or novelty priority. No experiment was run. The right endpoint allowance and absence of a selected-singleton block-growth bound are explicit.


### 2026-10-08 — GPT GC546, exact right endpoint audit

Checked GC545's necessary right prefix, GC496 first arrival and GC513 resonant branch. Direct Rule 30 evaluation at the two endpoint sites gives q=r+1+z; two finite-row hand controls retain the endpoint bit. No external result, novelty priority, experiment or singleton reachability is invoked.


### 2026-10-08 — GPT GC547, effective coordinate audit

Checked G130, already independently verified by Local L084, G4.4's triangular coefficient and GC542's statistics/runtime distinction. Prefix algorithms and the explicit program-plus-index description bound are proved directly; no external optimality theorem or novelty priority is invoked. Existing-record search found no earlier effective prefix-cost or unrestricted-description bound. No experiment was run. Supplied versus generated right input and full-prefix versus indexed output costs remain distinct.


### 2026-10-08 — GPT GC548, official Problem 3 scope

Read the current [official prize page](https://rule30prize.org/) and its linked [announcement](https://writings.stephenwolfram.com/2019/10/announcing-the-rule-30-prizes/), specifically the Problem 3 discussion, computational-effort models, displayed formal predicate and solution requirements. The finite-limsup predicate and prose shortcut threshold are recorded separately. Own synthetic runtime functions prove the quantifier distinctions; no algorithm, prize interpretation or novelty claim is imported. Existing-record search found no prior MaxLimit or no-O(n) scope audit. No experiment or external communication was performed.


**GPT CL051 algebra scope audit (2026-10-08, GC561).** Existing-record search for intertwiners, affine factors, the Gray part and seven-rings found G125's sideways/recurrent-ring correspondence, G55/C6's rotation lifts, CL046's source split and RULE30-PRIZE.md section 5's ring counts. G245 reuses elementary cyclic-shift algebra over GF(2) and uniqueness of Boolean multilinear coefficients to prove the Rule 60 transient decomposition and exclude nonconstant affine full-state Rule 30 factors to linear updates. This is a hand scope check of the recorded proposal; no literature novelty claim, new wheel model or external search is asserted.

### 2026-10-08 — Cloud, the 3x+1 map as an automaton (for COLLATZ-PRIZE.md §8)

Searched for prior representations of the Collatz map as a cellular automaton before recording the Gray-code split
of COLLATZ-PRIZE.md §8 (Rule 30 and the 3/2 map as two corrections of $n \oplus \lfloor n/2 \rfloor$). The four
references below were checked at their abstract or bibliographic pages only, not read in full.
- **Korec, I., "The 3x+1 problem, generalized Pascal triangles and cellular automata"**, Mathematica Slovaca 42
  (1992), 547-563 (https://eudml.org/doc/32424). It models the 3x+1 iteration by a seven-state one-way cellular
  automaton, equivalently a generalized Pascal triangle over a seven-element algebra. This is the nearest prior art
  to a Pascal-triangle reading of Collatz. Its triangle lives in a seven-element algebra, not in GF(2) with the
  carries as separate events.
- **Cloney, T., Goles, E. and Vichniac, G. Y., "The 3x+1 problem: a quasi cellular automaton"**, Complex Systems 1
  (1987), 349-360 (https://complex-systems.com/?p=1666). It studies the iterates in base 2 as a "quasi" cellular
  automaton, quasi because the choice between x/2 and 3x+1 reads the last bit, so the rule is not local.
- **Kari, J., "Cellular Automata, the Collatz Conjecture and Powers of 3/2"**, Developments in Language Theory
  (DLT 2012), LNCS 7410, 40-49, doi:10.1007/978-3-642-31653-1_5. It builds one-dimensional automata that multiply
  by 3 and by 3/2 in base 6, and states Collatz and Mahler's 3/2 problem as constraints on their space-time diagrams.
  It is the precursor of Kari and Kopra's "Cellular automata and powers of p/q", already in this file.
- **Bruschi, M., "Two cellular automata for the 3x+1 map"**, arXiv:nlin/0502061 (2005). It gives two simple automata
  for testing the conjecture on large numbers. Its author writes that only "a very faint light" arises from them for
  a proof.
None of these abstracts uses the split of the Gray code into a local correction (Rule 30) and a carry (3/2). The
identity is one line and is surely known in folklore. No novelty is claimed.

**GPT GC616 carry-domain audit (2026-10-08).** Read Akiyama, Frougny and Sakarovitch, *Powers of rationals modulo 1 and rational base number systems*, the Mahler integer/fractional discussion on printed page 28, at [author-hosted PDF](https://perso.telecom-paristech.fr/jsaka/PUB/Files/RBNS-rev.pdf). The parity-dependent fractional intervals are known and credited; no novelty for the rounded recurrence. The alternate primary host timed out. The exact real carry-floor convention and finite-age support guard are own hand audits of CL066 and GC598/GC600, not claims about that paper's full results.


### GC659 — B2 owed-reading checkpoint, partial (GPT, 2026-10-09)

Read the [publisher record for Jen1986](https://link.springer.com/article/10.1007/BF01010579): title, abstract and bibliographic metadata only. The full article remains subscription content and was not obtained in this bounded search. Queries included the exact title, DOI and the report identifier LA-UR-85-1218; no primary full text was retrieved. This does NOT settle whether B2 unboundedness is in that paper. Jen1986 remains owed a full reading.

Rechecked the [author's Rowland2006 PDF](https://ericrowland.github.io/papers/Local_nested_structure_in_rule_30.pdf), specifically its Jen attribution and section5 statements. Rowland attributes eventual diagonal periodicity to Jen Theorem4 and proves the odd-source/white-stripe criterion for doubling. That is distinct from a proof that doubling continues forever or a quantitative stage-spacing estimate. This confirms the existing section5 reading, not an absence claim about all of Jen or all other literature. The unexpected scope guard is that a single-cell diagonal record does not supply a rate on every rooted branch.

The earlier stored OSTI scan link concerns Jen1990, a different paper; its current retrieval failed and it was not read. No paywall login or purchase attempted. Next choose useful local proof work while preserving the specific1986 full-text limitation; do not mark the B2 prior-art item complete.


### GC663 beta-language source check (GPT, 2026-10-09)

[Li and Li, Distributions of full and non-full words in beta-expansions](https://arxiv.org/pdf/1705.07277): introduction, relevant sections2-3 read. The paper credits Renyi for beta transformations and their entropy, Parry for admissibility. Lemmas2.2/2.7 and proposition3.1 give maximal critical prefixes, fullness after lowering the last nonzero digit, and free concatenation onto a full cylinder. GC663 applies these established facts to G50-G51's Mahler fractional language at beta3/2. No novelty or whole-paper audit is claimed, and this does not complete the unrelated owed Jen1986 reading.


## Kari-Kopra unavoidable-hole proof receipt (2026-10-09, GPT; GC670)

[arXiv:1710.05737v1](https://arxiv.org/html/1710.05737v1), Lemmas4.3-4.4 and Theorems4.8-4.9 proofs read; not the full paper. The earlier abstract/survey receipt is supplemented. The compact null exceptional set is covered by added cylinders; the final hole is chosen by this repair. GC670 derives a uniform hitting horizon and its measure lower bound, then checks why that hole need not lie in the prescribed Mahler forbidden half. No new Z-number exclusion or constructive upper bound.


### GPT targeted Guan/Wang graph reading (2026-10-09; GC720)

Read the definitions and Rule 30 portion of section 3.2, printed pages 39–40 including Figure 4, of [Guan and Wang, Complex Shift Dynamics of Some Elementary Cellular Automaton Rules (2011)](https://doi.org/10.25088/ComplexSystems.20.1.31), using the [primary PDF](https://content.wolfram.com/sites/13/2019/01/20-1-3.pdf). This upgrades the earlier search-result-only citation for that portion. Its Rule 30 graph is a five-cycle. GC720 independently reconstructs it: entropy is zero and mixing fails, although the third-iterate spatial shift identity holds. This graph supplies no alternating wall. Rules 41/110 and the interval-map claims were not audited; no full-paper endorsement or comprehensive priority search.


### GPT targeted binary-quotient reading (2026-10-09; GC724)

Read printed pages 34–35 of [Guan/Wang 2011's primary PDF](https://content.wolfram.com/sites/13/2019/01/20-1-3.pdf), specifically the binary-evaluation diagram and boundary convention. GC724 checks a dyadic fibre: the two names of 1/4 yield different Rule 30 image reals. The displayed full-symbol-space interval-factor interpretation therefore needs a domain/expansion qualification. No full audit of the interval equations, other rules or entire paper is claimed.


### GPT turning-row attribution check (2026-10-09; GC725)

Read the definitions and Remark 2.1 of [Boyle and Lee, Jointly periodic points in cellular automata: computer explorations and conjectures](https://arxiv.org/html/math/0607178#S2). Its injective-CA hypothesis does not apply to Rule 30. It supplies directional-count context, not a direct invocation for Cloud's TR; the independently audited window proof suffices. No full-paper reading or novelty survey.


**GC763 right-prefix rate bound (GPT, 2026-10-09).** Re-read the author's [Rowland2006 PDF](https://ericrowland.github.io/papers/Local_nested_structure_in_rule_30.pdf), Lemma2 and section3 (pages6–10). They provide the dyadic integrator and return-to-initial-row framework, discuss seed dependence and uncertain growth rates. GC763's even half-period OR pairing supplies a scoped triple-doubling obstruction within that framework. This reading does not establish novelty or an exhaustive literature absence; no asymptotic single-cell coefficient is imported.


**Fair-row diagonal short-memory guard (GPT GC773, 2026-10-09).** Existing G97/G110/G113 and higher-order lumpability entry read. Web searches “Rule 30 autocorrelation light cone Bernoulli correlation exact temporal correlations” and “Rule 30 correlation sign alternation left permutive cellular automata” found no matching all-lag sign or two-step diagonal theorem in the returned results; NOT FOUND is limited to these searches. Reread the abstract/metadata of Geiger and Temmel, [Lumpings of Markov chains, entropy rate preservation, and higher-order lumpability](https://arxiv.org/abs/1212.4375), revised2015: projected-process memory is established theory. No full-paper read or import of its finite-state criteria. GC773 uses direct symmetry/correlation equations plus a128-word replay; no novelty or exhaustive absence claim.

### 2026-10-09 — GPT, CL081 neighbour-density corollary audit

The two left-column formulas already occur in RULE30-PRIZE.md Lemma 1 / R0; GC779 audits their endpoint summation without importing an external theorem. Searches `"Rule 30" "two thirds" periodic column` and `"Rule 30" "period two" density neighbours` returned mostly unrelated rule-number material and no exact statement. Follow-up queries `"rule 30" "periodic" "density"` and `"rule 30" "two-thirds"`, restricted to arxiv.org and complex-systems.com, found no exact two-thirds neighbour result. The first returned Martínez et al., *Complex Dynamics Emerging in Rule 30*, only a search excerpt of generic random-row/ring discussion read here; no lemma imported. Limited NOT FOUND, not an exhaustive absence or novelty claim.


### GC790 — Owner-requested diagonal-source comparison: Rowland checked, original Jen papers still partial (GPT, 2026-10-09)

Read [Rowland2006, author's PDF](https://ericrowland.github.io/papers/Local_nested_structure_in_rule_30.pdf), definitions and Lemma2 (printed pages4-7), section3's coordinate convention, and all of section5 (printed pages15-17). His immediate-periodicity bound matches the right-diagonal integrator; the left-side reset and white-neighbour odd-parity criterion match our settling mechanism. His general eventual-periodicity credit is to Jen1986 Theorem4, not Jen1990. Corrected the unchecked year attribution in §8.27. No rate or growing fixed-lag frontier follows from this comparison.

Jen1986's [publisher record](https://link.springer.com/article/10.1007/BF01010579) remains bibliographic/abstract access only. Jen1990's stored OSTI PDF retrieval again failed; the publisher PDF endpoint also returned an error. Consequently no original1990 hypothesis comparison with Proposition7 is claimed. The new accessible [MIT/LCS/TM-317 scan](https://publications.csail.mit.edu/lcs/pubs/pdf/MIT-LCS-TM-317.pdf) is a60-page1986 conference booklet: cover, foreword and opening roster inspected, not the journal paper. Do not mistake that search result for an obtained full Jen theorem proof. Local proofs remain independently audited; these specific original-source readings remain owed.


### GC792 — Jen1990 author report obtained after owner supplied a new link (GPT, 2026-10-09)

The supplied SciSpace link returned access errors, but direct retrieval of [the primary OSTI PDF](https://www.osti.gov/servlets/purl/7230855) succeeded. The22-page scan is LA-UR-90-761, titled Aperiodicity in One-Dimensional Cellular Automata, submitted to an AIP conference proceedings. Do not identify it as the journal version without comparison. Read section2 definitions (printed page3), section3 through Proposition3 and proof (printed pages5-7), and reference8; proposition/proof checked visually against the scan. Periodic allows finite transience; the standing initial condition is finite and nonzero on both sides. The Rule30 at-most-one-periodic-column mechanism agrees with the local inverse propagation argument. This report does not explicitly state Proposition7's stronger formal-driver/finite-left scope. The lemma and proposition credit Jen1986, Global Properties of Cellular Automata, whose original full text remains owed. The pre-proposition sentence says aperiodic where the proposition and proof say periodic, a visible source typo. This supersedes GC790's report-access failure, not the remaining1986 full-text limitation.


### GC794 — Owner-supplied Powley2009 thesis: targeted preimage and boundary reading (GPT, 2026-10-09)

Obtained [Edward Jack Powley, Global Properties of Cellular Automata, York PhD, October2009](https://www.cs.york.ac.uk/nature/group/theses/EdPowley.pdf),230 PDF pages. This matches the title of Jen1986, not its authorship or content. Read the abstract, contents, section2.1, section4.3's matrices/Theorems4.6-4.7, section9.2's Theorem9.5 and proof, section9.3, section7.5-7.6, section10.3-10.5, and chapter11; selected surrounding examples inspected, not a whole-thesis reading. Visually checked Rule30's matrices on page49. The transfer-matrix path count is useful for finite boundaries; its trace specializes to periodic rings. Section9.3 compresses a repeated spatial target into a repeated matrix product; it does not address a lone temporally periodic column. The symmetry/classification discussion is explicitly tentative. Section10.5 increases the neighbourhood radius for multiple transitions, so fixed-size one-step matrices do not automatically compress unbounded time. Existing de Bruijn work in our record predates this reading; no novelty claim. Boundary and defective-matrix controls in GC794 distinguish what transfers. Jen1986's original reading remains owed.


### GC800 — Bounded lookup for localized G trace patterns (GPT, 2026-10-09)

Searched the existing research/proof record for000111,111000 and adjacent-long-run claims; appearances in unrelated spatial predecessor and ambient-root controls do not assert this G trace theorem. Web queries: `"rule 30" "000111" diagonal` and `"rule 30" "111000" forbidden`. No relevant primary theorem was found in this bounded lookup; irrelevant matches were not used as evidence. This is not a claim of novelty or a complete literature search. GC800's local Boolean proof and exact finite-cone controls distinguish G/right-moving traces from physical vertical traces; independent reading remains requested.



### GPT targeted Jen1987 predecessor-count reading (2026-10-09; GC804)

Read the introduction, section2's endpoint-count recurrences and matrix construction, and section3's definitions and Rule30 table rows in [Erica Jen, Scaling of Preimages in Cellular Automata, Complex Systems1 (1987),1045-1062](https://wpmedia.wolfram.com/uploads/sites/13/2018/02/01-6-2.pdf). The counts concern finite spatial output words after one update, with unconstrained predecessor endpoints. This is useful precedent for retaining boundary states, not a temporal-column realizability theorem or fixed-dimension compression in time. Tables were read through extracted text; attempted table screenshots failed, so no visually verified table value claimed. The general scaling proof and all rule cases were not fully audited. GC804 independently reconstructs Rule30's four-preimage count and a spatial/temporal countercontrol. Already-read Guan/Wang sources were not treated as new findings. Jen1986 original full text remains unobtained after the bounded search.

## Overlooked work: theses, small groups and independents (surveyed 2026-10-09 15:46 BST, by Cloud's research subagents)

The owner asked whose verifiable work is passed over because its authors are students, independents or small groups.
Four survey passes (theses; traces and columns; independent Rule 30 work since 2019; older tools) each grepped this
file before listing anything. The full ranked report is `reports/overlooked-ca-survey/report.md`, and the
four sets of notes are in `reports/overlooked-ca-survey/notes/` (both moved and renamed on 2026-10-22 from paths with
spaces; reports/README.md lists the old paths). Each records how much of every
source was read. Nothing found proves period 2 or contradicts the record. The finds, ranked:
1. **Kopra, TCS 851 (2021), arXiv:2005.05112, Propositions 2.7 and 2.8, Lemma 3.17; his Turku thesis (2019),
   Propositions 3.3.4 and 3.3.5.** Read in full in both versions. For the p/q multiplication automata, one column from
   a nonzero finite configuration is never eventually periodic, in about 15 lines. The proof uses both ingredients:
   left-finiteness as a positive real value that shrinks, and the real dynamics as a width-1 sideways map. Rule 30's
   sideways map (Proposition 7) has width 2 and is not invertible, and that is the step it lacks. This upgrades the
   abstract-only entry above. Open: whether Kopra 2023 Theorem 3.5 at width 1 already contains it. *Answered later
   on 2026-10-09:* yes. Kopra 2023 (arXiv:2202.13809, read in full) says Theorem 3.5 reproves "Proposition 3.8 of
   [10]" (the TCS numbering of this result) with essentially the same proof. It has width 1 for the p/q automata and
   width 2 for left-permutive rules such as Rule 30. It notes that Rule 90 lies in the same class with an eventually
   periodic single-cell centre column (RULE30-PRIZE.md §8.77).
2. **cochon123/rule30-prize (an agent-run public repository, 2026).** Unverified. It claims certificates excluding
   eventual centre periods $0\,1^q$ for $q = 7$ and every $q \ge 9$ by forcing column -1 periodic, then Jen and
   Kopra. Its family is this record's parked black-end walls, and its scope (relaxation or single seed) is unstated.
   Its constant-tail argument for period 1 checks by hand.
   *Status, later on 2026-10-09:* the finite cases q = 7 and 9 to 16 were reproduced independently by Local (SG,
   L429) from GPT's specification of the relaxation (GC805). GPT's repair of the uniform argument (GC806), with
   Local's wrap table (WT, L431), closes every q >= 17. The repository's own uniform proof had a gap (GC805), so the
   result stands on the repair. It is filed as PROOFS.md entry 38. Open in the family: q = 1 to 6 and 8.
3. **Guillon, doctoral thesis, Paris-Est (2008), in French.** The "retourné" (Proposition 4.6.8) is the published
   general form of the forced left half; Proposition 4.8.5 relates entropy to trace entropy. The width convention is
   resolved for Rule 30 in RULE30-PRIZE.md §8.77: width 2 in the physical frame, not the radius 1.
4. **Tahay, doctoral thesis, Lorraine (2020); Dolce and Tahay, DLT 2022 (read in full, upgrading "snippet only");
   Marcovici, Stoll and Tahay, AUTOMATA 2018.** Fibonacci, quadratic-slope Sturmian and binary 3-automatic columns
   occur in quiescent CA from finite seeds: finiteness alone forces nothing. This is the citation the Theorem E row
   lacked.
5. **Sablik, TCS 400 (2008).** Left-permutive rules have a half-line of left-expansive slopes, and a right-expansive
   slope needs right-closing. Rule 30 is not right-closing (the survey's check), so it has no expansive slope at all.
6. **Coven, Pivato and Yassawi, Proc. AMS 135 (2007).** Odometers for left-permutive, memoryless rules with a fixed
   right tail. The survey's application (Rule 30 in the right-edge frame, the 2-adic map R to R xor (2R or 4R), OEIS
   A269160) is its own derivation and awaits a second reading.
7. Smaller: Kopra's MathOverflow answer 429509 (no configuration of minimal temporal period 2); Jalonen and Kari,
   Fundamenta Informaticae (2020), on sofic traces; Goles, Guillon and Rapaport on traced communication complexity
   (arXiv:1102.3522); Math SE 4497595 and 4832480 (a single cell on a 0101 background, ratio near 1.6241);
   DeepMind's formal-conjectures `Rule30.lean` statements; Litow and Dumas (1993); Coven (1980). Brunnbauer's 2019
   lemma has now been read: right-diagonal periods never decrease, which Jen and Rowland subsume.
Full-solution claims found (several repositories, preprints and forum posts) contain nothing checkable; the report
lists them with reasons. "Overlooked" rests on absence from this file and citation counts of 0 to 11: the pattern is
language, venue and discipline silos more than a measured bias against students or independents.


### GPT isolated-zero source audit begun: sound strip, uniform-proof gap (2026-10-09; GC805)

Read pinned [strip_graph.py](https://github.com/cochon123/rule30-prize/blob/3915b39894a34ac917dbaa2f1d6969183a780979/research/strip_graph.py), [isolated_zero_uniform.md](https://github.com/cochon123/rule30-prize/blob/3915b39894a34ac917dbaa2f1d6969183a780979/research/isolated_zero_uniform.md) and its checker at the same commit. The arbitrary-boundary strip is a sound relaxation of every real orbit, not a single-seed boundary model. No external code executed. Finite cases await Local's independent reimplementation. The uniform proof's LemmaF infers a cruise visit from unique prefix self-loop; GC805 gives a different projected two-cycle, so that inference needs an additional transient/extension argument. This is a proof gap, not a surviving radius6 counterexample or refutation of any period exclusion. Source paths are under research/; unauthenticated public API retrieval succeeded after browser-tool errors. No novelty or prize claim.


## Kopra width-one comparison resolved (2026-10-09, GPT; GC807)

Primary versions read: [2021 paper preprint](https://arxiv.org/pdf/2005.05112), v1,
Propositions2.7/2.8 with their proofs; [later generalization preprint](https://arxiv.org/pdf/2202.13809),
v1, Definitions3.1/3.3/3.4, Lemma3.2 and Theorem3.5 with proof. Journal-version identity is
bibliographic; no version-by-version comparison made. CL085's containment question is resolved:
Theorem3.5 applies at width1, dimensions(1,1,1), speed log base pq of p/q, strictly below1.
Its preceding paragraph explicitly credits the earlier result (numbered3.8 in the cited version).

The earlier reconstruction extracts the missing digit modulo q from the next-time digit and
modulo p from the previous-time digit, then uses coprimality. Advancing time while moving left
keeps the propagated period aligned; the represented value decreases by q squared each such
step. A zero period then forces a permanent left bound, contradicting multiplication growth.
This is an existing theorem, not new progress on Rule30's single column. The established
Rule30 width is2. The source's strict speed condition is essential; do not substitute mere
left expansivity. The standing arithmetic assumptions exclude q=1. No whole-paper audit claimed.

Finite isolated-zero receipt: Local L429 independently reproduced q=7 and9..16 at7848e5ad;
GPT GC807 accepts the graph-to-Jen logic after source reading, without rerunning the enumeration.
All-q exclusion remains open pending GC806's hand review and finite wrap certificate.


## Right-edge odometer application independently audited (2026-10-09, GPT; GC808)

[Coven, Pivato and Yassawi, Prevalence of odometers in cellular automata](https://arxiv.org/pdf/math/0511030),
v1 (2005 preprint of the2007 paper): definitions, Theorems1/4 and both proofs read;
not a whole-paper or journal-version comparison. These theorems apply to the survey's
single-seed Rule30 map in its right-edge frame. GPT independently checks genuine
anticipation, first-input permutivity, fixed zero right tail, prime2 additive form and
infinite orbit: the shifted left edge is-2t. The survey's2-adic formulas and three-state
Mealy decoder pass hand derivation. Its depth measurements are not rerun.

The cited theorem concerns the seed orbit closure. It does not assert that the full
2-adic map is ergodic, nor constrain the changing-coordinate readout defining the centre.
GC808 supplies explicit modulo8 and finite-prefix scope controls. Credit the theorem to
CPY and this application to the Cloud survey; no novelty priority claimed.


**2026-10-09 GC809 status update to the isolated-zero audit.** The proposed exclusion for
q=7 and every q>=9 is now established here: GC806 repairs the cruise-visit gap, independently
second-read by Local L430, and Local's SG/WT reimplementations give the finite certificates
(L429/L431;7848e5ad/93517b1d). GPT accepted both certificate logic chains after reading their
complete source, without rerunning numerical enumeration. The external uniform proof's
original self-loop inference remains invalid; credit its proposed theorem and method while
retaining the repair and independent checks. This is a restricted-wall result, not period2.


**GC810 scope addition (2026-10-09).** CPY's cited Theorems1/4 apply, after right-edge
normalization, to every nonempty finite Rule30 seed, by GC755's already-recorded support
argument. No new edge theorem claimed. Rule90 satisfies the same odometer hypotheses but
its single seed's physical centre is eventually zero, directly by the even central binomial
coefficient. This known comparator prevents using abstract orbit-closure conjugacy alone
to deduce vertical aperiodicity; a Rule30-specific readout/coupling condition remains needed.


## Sablik closing application checked directly (2026-10-09, GPT; GC813)

[Sablik, Directional dynamics for cellular automata](https://www.math.univ-toulouse.fr/~msablik/article/2008-TCS.pdf),
TCS400(2008)1-18, doi10.1016/j.tcs.2008.02.052: targeted definitions, Example3.4 and
Remark5.2 read; Theorem5.2 statement inspected, proof not audited. Exact cone endpoints
are not independently accepted: extracted minus signs are damaged and page8/15 screenshots
failed with cache misses. No whole-paper claim.

GC813 independently proves the survey's Rule30 right-closing failure using two
left-asymptotic rows with the same image, without rerunning its pair-graph search. One
row is finite, the other has an infinite black right tail. Translating the pair defeats
any fixed-width forward observation of arbitrary right inputs; this supports the survey's
no-right-expansive/no-expansive conclusion. Distinct finite seeds remain distinguishable
by the already-recorded rightmost-damage identity. The full-shift result does not decide
a finite seed's central trace. No novelty claim for closing theory or damage propagation.

**GC814 width receipt (2026-10-09).** Independently checked the direct Rule30 argument in Cloud section8.77: N2(n)<=Nw(n)<=N2(n+w-2) for w>=2, with a finite-anticipation decoder and projection inverse. This supports width2/full-map entropy equality without independently accepting the original Guillon thesis hypotheses. Three versus two fixed trace points refute width2/width1 conjugacy; they do not refute entropy equal to one bit. Section8.77 corrected accordingly. TW/TWX measurements not rerun by GPT.

## Two survey gaps closed by the owner's finds (2026-10-09, Cloud)

- **Math SE 4141181's answer read.** Johan Kopra (2022-01-19, accepted) reduces three colours to two with marker
  words 0000011, 0000101 and 0001001
  ([API record](https://api.stackexchange.com/2.3/questions/4141181/answers?site=math&filter=withbody)). The reduction
  leaves constant columns in every block of the encoding, since a binary non-overlapping code fixes its first and
  last letters, so it does not meet the question's "not infinitely many". Asymmetric two-colour answers exist among
  linear rules, with no symmetry in any frame (RULE30-PRIZE.md §8.77; `rule30_cloud_lone_column.py`). None was found
  among the elementary rules. **Import:** the Rule 90 barrier extends to rules with no mirror symmetry.
- **The PDF behind Kopra's MathOverflow table identified.** Jeremias Epperlein, *Topological Conjugacies Between
  Cellular Automata*, dissertation, TU Dresden (submitted 2017-02-03, defended 2017-04-21; examiners Stefan Siegmund
  and Jarkko Kari). CORE item 236376428; the owner supplied a mirrored copy. Appendix A gives, for every elementary
  rule class, the counts of points with each least preperiod q and least period p for q + p <= 6, and of their
  accumulation points. Section 6.3 treats permutive automata and was not read. The Rule 30 rows were recounted
  exactly (all 42 entries agree) and extended to p = 10 (`rule30_cloud_periodic_points.py`). **Import:** "no
  configuration of least temporal period 2" is now checked here, and the record's 84-ring is the unique orbit of
  least temporal period 6.
- **Scope (GC829), correcting the first item above:** with no symmetry in any frame, only the centre column is
  proved (moves -3, -1, +3) and the other columns are decided only for |j| <= 64. Moves -1, +3 give a fully proved
  answer to the question's letter, with an orbit symmetric about a moving line.


### Alon, Behajaina and Paran (2024): polynomial Collatz stopping time

*On the stopping time of the Collatz map in F2[x]*, [primary paper, arXiv2401.03210v1](https://arxiv.org/html/2401.03210v1). Helpful for CL090's proposed carry-free bridge. The paper states an O(degree^1.5) stopping bound and develops a coefficient-reversal/leading-term-removal reduction. **Reading scope (GPT GC832):** introduction and section2 through Lemma2.7; full stopping-bound proof not audited. Hicks et al. (2008) original remains unread here. **Own audit:** the accelerated carry-free map is parity-conditioned and has coefficient products a_0*a_i, so it is not F2-linear; Rule150's normalized seed polynomial has degree2t, preventing direct use of the same degree-descent potential. This is a route guard, not a transferred theorem or novelty claim.


**2026-10-09 — GPT GC847, rain stack statistics.** Reused the existing C5 uniform-Bernoulli measure proof and its independent four-preimage audit, alongside the prior triangle-statistics receipt above. Isolated-white stack tops are a different event from width-1 triangle births: the direct five-bit count gives 1/16 rather than C5's 3/32. The geometric stack-top law is derived explicitly in GC847; no external priority or new literature search is claimed. RN's single-seed agreement remains a measurement.

### Lemma B2 found in print (Local, 2026-10-09 19:44 BST)

The owed check "is the unboundedness of the left diagonals' periods (RULE30-PRIZE.md §8.59, Lemma B2) in Jen (1986)
or Rowland (2006, §5)?" now has a partial answer from a third source.
- **Nersissian, T., "Diagonal Periods and Newton Supports of Rules 30, 86 and 135"**, arXiv:2609.25077v1 (2026-09-18),
  §4 (read through a fetched summary of the HTML, with the theorem excerpts checked).
  - Rule 86 is Rule 30 reflected (Proposition 3). Its natural diagonals satisfy D_m(t + 1) = D_(m-2)(t) XOR
    (D_(m-1)(t) OR D_m(t)) (Proposition 4), which is our left-half recurrence.
  - Theorem 13 proves that their least eventual periods are unbounded from the single seed, with m + 2 <= 4^(Q_m).
    The method is ours: map adjacent periodic profile pairs backward; the boundary pairs (0, 0), which is fixed, and
    (0, 1) anchor a chain of distinct pairs.
  - Corollary 3, the record-doubling criterion, is Rowland's Proposition 2. Theorems 10 to 12 are the reset and
    integration lemmas.
  - Its §3 (Theorem 8) is about the other diagonals, parallel to the right edge (our G frame), with periods at least
    floor(m/2) + 1. That is a different object from B2.
- **Credit:** B2's method and its single-seed statement are Nersissian's, and earlier. Our every-left-finite-row
  statement is the same argument (§8.59 note).
- **Still owed:** Jen 1986, which is paywalled (the owner, 2026-10-09).



**Internal provenance, 2026-10-09 (GPT GC850).** The nine-black-step width-five adjacent-pair lock audits Local OH/L473 and uses the G15–G20 relaxation. Entry 38 supplies the earlier two-sided finite-seed exclusion and its external method credit. GC850 adds an independent finite image certificate and a reset-free hand invariant; it does not claim literature priority for black-boundary locking.


## AI-driven formal proof search, and Lean as the last check (noted 2026-10-11, by Cloud at the owner's request)

Read in two passes through a fetch tool: Tsoukalas et al. (Google DeepMind and Aarhus), "Advancing Mathematics Research
with AI-Driven Formal Proof Search", [arXiv 2605.22763](https://arxiv.org/abs/2605.22763), 21 May 2026. Agents that must
emit Lean proofs, checked by the compiler, resolved 9 of 353 formalised Erdős problems at a few hundred dollars each and
44 of 492 autoformalised OEIS conjectures; a plain generate-and-verify loop reproduced the Erdős results at higher cost
on the hard ones, and the full agent adds AlphaProof for subgoals and an evolutionary search over attempts. Erdős #125
(the sumset of the base-3 and base-4 digit sets {0,1} has lower density zero) is proved by a thinning argument that
needs 4^m and 3^k arbitrarily close, which Dirichlet gives because log 4 / log 3 is irrational: the same irrationality
that makes the left edge of the powers-of-3 pyramid on the site a Sturmian clock. Several problems needed a corrected
statement first (positive upper density where Erdős wrote density), and one agent first disproved the wrong
formalisation.

For this record. Nothing on cellular automata or Rule 30; the problems resolved are the accessible tail of the list, and
nothing suggests that a search for a short formal proof would reach the prize problems. The import is methodological:
the second-read protocol is our check against confident wrongness, and a proof checker is the stronger version of it.
Our finite results (certified cuts with cake_lpr certificates, cut-to-macro equivalences, strip cut products, the
eventual-periodicity exclusions) are the kind of statement Lean handles well. Hence the owner's standing instruction in
WORKING-TOGETHER.md ("Lean as the last check"), which updates item 3 of the periodic-interior import list above ("Lean,
as Condrey did. Not yet"): still not yet, but now the agreed final step. Companion: the openai/math note of 2026-10-07
above, most of whose manuscripts carry Lean formalisations.

## Re-survey for door 3, the number view (2026-10-14 01:19 BST, Local; loop check 3, L703)

Two web searches ("Rule 30 center column periodic proof arXiv 2026", extended; "Rule 30 cellular automaton column
eventually periodic two-adic irrational 2026", standard) and direct reads of two pages:
- Nothing new on the period-2 question or on columns as numbers. Condrey (arXiv:2609.09431), Nersissian
  (arXiv:2609.25077), Chan-Lopez and Martin-Ruiz (arXiv:2604.00165) and Das (arXiv:2207.13237) are all already here.
- The public period-two tracker, woahwhattheheck/commons issue 15314 (read 2026-10-04, above), returns "Page not found"
  on 2026-10-14. That is a dated negative; its earlier summary stands as read.
- beedbyte/rule30-research (GitHub, new to this file) is a specification and two finite evolvers with cross-checks for
  the single-cell centre column. It states that eventual nonperiodicity is open there and makes no claim.
- The internal record already covers the number view: 8.22 to 8.29 (columns as numbers, the complementary pair, the
  kinds of irrationality proof), 8.77 (the 2-adic frame) and 8.90 (the carry). Its main-line form, "period 2 means the
  centre column's 2-adic value is rational with denominator 3 * 2^n", restates the prize. No external method was
  found that this record lacks.

## Mahler's 3/2 problem: survey at the room switch (2026-10-14 07:46 BST, Local; L707, L708)

Web searches (extended and standard), plus direct reads of the Wikipedia and MathWorld entries, arXiv:2510.11723
(abstract and HTML) and the rwst/Confinement-Certificates repository (README and Challenge2.lean). PDFs were not
downloaded.

**The classical results.**
- *Mahler (1968), J. Austral. Math. Soc. 8, 313-321.* At most one Z-number in each [n, n+1), so at most O(x^0.7) below
  x. He conjectured that none exist.
- *Tijdeman (1972), "Note on Mahler's 3/2-problem".*
- *Pollington (1981).* {lambda: ||lambda (3/2)^n|| > 4/65 for all n} has positive Hausdorff dimension.
- *Flatto (1992), "Z-numbers and beta-transformations".* The count improves to O(x^theta) with
  theta = log2(3/2) = 0.585.
- *Flatto, Lagarias and Pollington (1995), Acta Arith. 70.* limsup minus liminf of {xi (p/q)^n} is at least 1/p (1/3
  for 3/2). Omega(3/2) > 1/2 would give Mahler.
- *Bugeaud (2004), Acta Arith. 114:* linear mod one transformations.

**Dubickas.**
- *(2008), Math. Nachr. 281.* No xi has every {xi (3/2)^n} in [8/39, 18/39] U [21/39, 31/39]. Infinitely many xi keep
  every {xi (3/2)^n} in (5/48, 43/48).
- *(2009), Acta Arith. 137:* powers cannot lie in a small interval.
- *(2019), Disc. Math. 342:* a single excluded window of length 31/81. (Flagged by the swarm as possibly misattributed;
  confirmed by GPT in GC1228: "Fractional parts of powers of large rational numbers", 342(7), 1949-1955, excluding the
  closed interval [8/57, 805/1539] of length 31/81. See below.)
- *Elsewhere:* complexity of minimal words in rational base p/q, liminf p(l)/l >= log q / log(p/q).

**Rational base number systems.**
- *Akiyama, Frougny and Sakarovitch (2008), Israel J. Math. 168.* Integer expansions in base p/q are unique and not a
  regular language; the expansions form a tree.
- *Akiyama (2008), "Mahler's Z-number and 3/2 number systems".* Multiple expansions, and Z-numbers in tree terms.
- *Andrieu, Eliahou and Vivion (arXiv:2510.11723, v2 April 2026).* Conjecture 1.2: minimal and maximal words are normal
  over subalphabets. It is equivalent to Conjecture 1.6: every orbit of T(x) = ceil(p x / q) is equidistributed mod
  q^k. Conjecture 1.2 implies no Z-numbers, no Z_{p/q}-numbers for p < q^2, Akiyama's triple-expansion conjecture and
  the Dubickas-Mossinghoff 4/3 problem.
- *Eliahou and Verger-Gaugry:* letters of the maximal word in base 3/2.

**Machine-verified frontier (Stephan, September 2026, "in collaboration with Claude Code"; Lean 4, kernel-checked
block certificates).**
- *Paper 1, "Confinement certificates for powers of rational numbers modulo one".* Regenerates FLP Cor. 1.4a,
  formalizes Dubickas's closed length-1/p theorem, and certifies Z_{3/2}(1/6, 13/24) and
  Z_{3/2}(961/3600, 2427/3600) empty. It also shows that no xi != 0 keeps ||xi (3/2)^n|| < 1/5, and certifies unions of
  total length up to 17/24.
- *Paper 2, "Confinement schemas and the reach of block certificates":*
  - Thms A and B: schemas for windows of length 1/p at every coprime base.
  - Thm C: escape within about K + log_q(X) + log_{p/q}(q/L) steps.
  - Thm D: completeness on the finite-hold-set class (finite hold set implies an empty Z-set), and an obstruction
    (no block certificate when the hold set is infinite).
  - Depth-size bound: a negative answer to Kari and Kopra's Problem 6.1 for this format.
  - Thm E: **Z_{3/2}(2/7, 5/7) is empty, a window of length 3/7 = 0.4286, "the ranked frontier and its exact
    ceiling".**
- *VibeMathed (2026)* reports that Claude-family models discovered and formalised it. MathWorld (13 Sep 2026) records
  the novelty as unknown and no independent specialist review.

**Withdrawn.** Kumar, arXiv:2411.03468 (2024), claimed no Z-numbers in Z^+ and was withdrawn in June 2025.

**Two cautions for our use.**
1. *The "3 mod 4" statement* returned by some search summaries ("a Z-number exists in [n, n+1) iff no iterate is 3
   mod 4") is false as an iff, because 1010... avoids 11 and gives a fractional part of 3/5. Only its necessary
   direction holds (GPT's G50, G51).
2. *Mahler's own window has an infinite hold set.* It is the whole window: every u in [0, 1/2) keeps an infinite orbit
   under u -> (3u - b)/2 with b chosen greedily. So Stephan's fractional-side certificates cannot reach it (his
   Thm D(ii)). The integer side is the crux, as in our Rule 30 work.

No published large-scale computer check of "no Z-number below N" was found. **Corrected (2026-10-14, found by the
swarm's adelic lane, abstract confirmed by Local):** Dubickas and Mossinghoff, "Lower bounds for Z-numbers", Math.
Comp. 78 (2009) 1837-1851, develop search algorithms and show that any Z_{3/2}-number exceeds 2^57, with bounds for
other p/q and links to 3x+1 stopping times. This survey had named Mossinghoff only through the 4/3 problem. The census
to 2^63 (MAHLER.md section 1) extends their bound.

**Swarm prior-art notes (2026-10-14; self-checks by sub-agents, credited for a second reader).**
- *Parry (1960), Renyi (1957):* the strict admissibility criterion behind the swarm's annulus form (MAHLER.md
  section 2), carried through G51's isometry.
- *Furstenberg (1967):* the dimension of a shift of finite type in the 2^-n metric, which gives the window
  ladder's dimensions log2(lambda_g).
- *Boyland, de Carvalho and Hall (2016):* maximal digit frequencies of beta-shifts. The swarm's "at most one third
  of a Z-number's integer parts are odd" is a special case.
- *Dubickas (2008):* the existence window (5/48, 43/48). The swarm's [7/57, 50/57] certificate lies inside it, and
  whether his construction already gives one xi per unit interval was not checked.
- *Akiyama, Frougny and Sakarovitch (2008):* state Mahler's question for nonzero xi. The negative half is the
  (1/2, 1) window problem; no separate treatment was found.
- *Window-to-residue equivalence (the ladder):* not found in the record or in one web search. Dubickas and
  Mossinghoff's "allowed residues" algorithm is the first place to look.

## Turing (1936), read at the owner's request (2026-10-14 07:58 BST, Local)

"On Computable Numbers, with an Application to the Entscheidungsproblem", Proc. London Math. Soc. (2) 42, pp. 230-265,
from the owner's copy. The 1937 correction is not in that copy. The owner's challenge: "these prize problems sit square
on Turing's On the Computability of Numbers because a coin toss is the ultimate adversarial program". The passages
that bear on our problems:
- *Section 3, Example I.* Turing's first machine computes 010101..., the period-2 sequence itself.
- *Section 8.* The diagonal process shows there is no general process for deciding whether a machine is circle-free,
  whether it ever prints a given symbol, or whether it prints 0 infinitely often. These are uniform questions about all
  machines. The footnote on p. 254 says "prints 0 infinitely often" is "of the same character" as circle-freeness.
  Our three problems have that shape:
  - Rule 30: every finite configuration's column eventually departs from 0101.
  - Mahler: every bounded range of starts dies out at a finite horizon (GC664).
  - Collatz.
  Each says "for every N there is a finite stage at which..." (Pi^0_2).
- *Section 9, p. 253.* "It is (so far as we know at present) possible that any assigned number of figures of delta
  can be calculated, but not by a uniform process. When sufficiently many figures of delta have been calculated, an
  essentially new method is necessary in order to obtain more figures."
- *Footnote, p. 255.* "it is often possible to show that certain classes of numbers are satisfactory".
- *Section 11.* It distinguishes "no general decision process" (Turing) from "specific unprovable propositions"
  (Goedel). A single prize statement has a definite truth value, so undecidability in Turing's sense applies to
  families, and the question for one instance is provability.

Our reading is in the session reply of the same date. In short:
- *A miniature of Turing's point in Stephan's 2026 work:* block certificates decide exactly the finite-hold-set
  windows, and provably cannot certify an infinite hold set.
- *The concrete bridge to Turing machines* is the busy-beaver holdout Antihydra, whose halting is a statement about
  iterating floor(3n/2), the same map family as Mahler's (G49 has its scope).


## Dubickas–Mossinghoff comparison: targeted GPT second read (2026-10-14 09:59 BST)

The published paper [Lower bounds for Z-numbers, DOI](https://doi.org/10.1090/S0025-5718-09-02211-X) was read through its [mirrored transcript](https://studyres.com/doc/16661447/lower-bounds-for-z-numbers-1.-an-approximate); publisher and CiteSeer PDF retrieval failed, so this is a textual read, not a rendered-table or implementation audit. Its definition uses the same strict half window. Lemma 3.1 and equations (3.6)–(3.7) give the decoupled map and fraction reconstruction. Table 4 and Theorem 5.1 give B=2^57 and M=137; equation (5.1) and Table 6 name start 9850069454682037. Algorithm 4.3 searches allowed residues; 4.4 is the alternative for q>=3.

Unexpected source cross-check: that published start is exactly GC1221's independently replayed H=137 fixture, chosen before this paper was identified. This calibrates definitions and the horizon convention, without independently reproducing the published global bound. Local's census uses an exact shrinking-window tree rather than their stored residue list; its adopted w63 receipt extends the cited cutoff, but no “first large-scale check” or current-record claim follows. The general Mahler problem remains open. Record searched: Dubickas/Mossinghoff and Lower bounds for Z-numbers -> Local's correction and survey. No computation run.


## L711 citation and novelty checks: GPT (2026-10-14 11:00 BST)

The 2019 entry's author and title are confirmed by [Lu–Zheng reference9](https://arxiv.org/html/2603.16794v1#bib.bib9) and the [author's institutional publication list](https://elaba.mb.vu.lt/mif/?aut=Art%C5%ABras+Dubickas): Dubickas, *Fractional parts of powers of large rational numbers*, Discrete Mathematics342(7),1949–1955, [DOI](https://doi.org/10.1016/j.disc.2019.03.018). The [reproduced original abstract](https://www.researchgate.net/publication/332643797_Fractional_parts_of_powers_of_large_rational_numbers) states the excluded closed interval [8/57,805/1539]. Subtracting the endpoints gives589/1539=31/81 exactly. Thus the title is consistent with the cited interval, not a bibliographic misattribution. Publisher retrieval failed and the full proof was not read.

D-M 2009 sections3–4 were targeted for the ladder: general coding appears, but no explicit plateau was found in that read. This is NOT FOUND on that limited scope; the general rational-base correspondence is known, and the exact ladder's novelty remains UNKNOWN pending Flatto/FLP. GC1228 verifies its core independently without a novelty claim.


## GPT sign-rule countercheck: bounded attribution search (2026-10-14; GC1246)

Searched `Lagarias ternary expansions powers 2 2009 3-adic integers arxiv`, `ternary square digits 0 and 1 Erdos Lagarias`,
`Z-numbers twice Mahler`, `ternary square contains a 2`, `Z-numbers multiplication by 3 2-adic`, and
`ternary x^e Cantor`. No exact attribution for the two sign rules or integer squaring corollary was located in these
limited searches. This does not establish novelty or absence from the literature.

Opened [Mahler's original paper](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/6416420BFE33A5DDC3DAB6EA358C2B0B/S1446788700005371a.pdf/an-unsolved-problem-on-the-powers-of-32.pdf), reading the parity/series reduction and odd-step necessary condition in sections1-5. This is the established context for the first-free-parity proof. No exact closed-set multiplier-intersection statement was located in that bounded reading.

Read [Lagarias, Ternary expansions of powers of2](https://arxiv.org/pdf/math/0512006), introduction/section1 and section4 through Lemma4.1. That lemma gives C intersect M^(-1)C={0} for positive M=2 mod3, and an infinite intersection for M=1 mod3. Its proof uses the first nonzero digit and recursive digit choices. It concerns linear MULTIPLICATION of a point by M; Cloud8.110 instead raises a unit point to an integer POWER. These operations must not be conflated. The source is an analogous mechanism, not an attribution of Cloud's exact nonlinear statement.

Flatto-Lagarias-Pollington's publisher page was opened, but both its archive PDF and official download returned403. The AMS Dubickas-Mossinghoff PDF was unavailable through this tool. Neither full paper was searched in this block; the existing GC1221/GC1228 and prior-art reads remain their own dated evidence. No folklore or priority claim is made.


## GPT nonlinear ternary converse: bounded prior-art check (2026-10-14 21:46 BST; GC1248-1249)

Searches: `3-adic Cantor set power map x^n digits 0 1 intersection nonlinear`, `ternary Cantor powers converse
Lagarias`, `"3-adic" "Cantor" "power map"`, and `"ternary" "x^e" "Cantor"`. Results mostly concerned LINEAR
multiplicative translates, including Abram-Lagarias, arXiv1308.3133 and arXiv1508.05967; their full texts were not
read in this block. No exact nonlinear converse attribution was located in this bounded search; NOT a novelty claim.

Read [Lagarias, Ternary expansions of powers of2](https://arxiv.org/pdf/math/0512006), section4 Lemma4.1 and its
proof (PDF pp21-22). For M=1 mod3 its recursive input-digit choice guarantees the next linear output digit avoids2.
This is the direct prior mechanism. GC1249 uses the same two-choice principle for x^e, with a proved output shift
v3(e) and convergence for negative integer exponents. The source does not in the passage read state that nonlinear
power-map result. Its preceding proof also explicitly uses4=(11)_3 and256=(100111)_3, so that example is known,
not a new Erdős exception. This block does not establish literature priority or search every source in full.

### SW-01 precedent scope checks (GPT, GC1256, 2026-10-15 11:08 BST)

Target: L730's claimed single-object precedents. Read the following primary passages, not the entire papers.

- [Bousch, Le poisson n'a pas d'arêtes (2000)](https://www.imo.universite-paris-saclay.fr/~thierry.bousch/preprints/cocycles.pdf),
  sections 1.2 and 3, Lemmas A-B (PDF pages 3, 5-6). For a Lipschitz observable rho on angle-doubling there is a
  continuous potential phi and maximal invariant average beta with rho(x) <= beta + phi(2x) - phi(x). Summing
  bounds every finite orbit sum by n beta plus a bounded endpoint term. The displayed sine example holds for
  every start and horizon. The enabling step is the fixed-point construction of the potential; the special
  observable then permits identifying the maximum. This is a real all-orbit precedent. A transfer still needs
  a justified observable and a strict gap; the paper does not give Rule 30's missing gap. Unexpected scope control:
  rho = 1 has phi = 0, beta = 1, so potential existence alone does not imply an exclusion.
- [Duke, Hyperbolic distribution problems and half-integral weight Maass forms (1988)](https://www.math.ucla.edu/~wdduke/preprints/hyperbolic.pdf),
  introduction and Theorem 1 (PDF pages 1-3). The equidistribution statement averages all Heegner points or all
  closed geodesics of a fundamental discriminant. It does not assert equidistribution of each geodesic. The
  individual Fourier-coefficient bounds are a different precise object; a proposer must identify which result
  is meant. Do not turn a packet average into control of a prescribed orbit.
- [Deutsch and Sagan, Congruences for Catalan and Motzkin numbers and related sequences (2006)](https://users.math.msu.edu/users/sagan/papers/old/ccm.pdf),
  section 3, Theorem 3.1 and proof (PDF pages 6-8). Exact Motzkin parity for every n follows from reflection
  pairing and a recursion on symmetric trees. This is an all-index theorem with an explicit structural reduction;
  it is not a theorem forcing arbitrary nonlinear orbit digits to be automatic. Its transfer needs an analogous
  identity, not just an observed kernel. No priority claim or full-paper audit is made here.

### K2-prime source bridge: finite words versus path sets (GPT, GC1258, 2026-10-15 11:49 BST)

- [Abram and Lagarias I, arXiv 1308.3133](https://arxiv.org/html/1308.3133), introduction 1.1, Theorem 1.6 and
  section 3.1 read. It constructs finite graphs for fixed finite intersections of 3-adic Cantor translates by
  tracking bounded arithmetic carries. This does not itself decide whether an arbitrary regular set of canonical
  finite numerals can be forward x4-closed while avoiding C-star. Caution: the [arXiv metadata abstract](https://arxiv.org/abs/1308.3133) says dimension zero
  has been shown, but the HTML abstract and Conjecture 1.2 state it as conjectural; use the theorem text.
- [Abram, Bolshakov and Lagarias II, arXiv 1508.05967v2](https://arxiv.org/html/1508.05967v2), sections 2.3 and
  3.1-3.3 read. Definition 3.1 uses all infinite paths from a marked graph vertex; such path sets are closed in
  the shift topology. Canonical finite-word acceptance has a terminal condition that cannot be discarded in a
  K2-prime transfer. The source's dimension estimates concern 3-adic sets, not exclusion of a specified integer.
- [FAR method, original developer's description](https://discuss.bbchallenge.org/t/decider-finite-automata-reduction/123)
  and [validation discussion](https://discuss.bbchallenge.org/t/validating-finite-automata-reduction-results/138)
  read: certificates separate the start from a regular backward-closed superset of halting configurations;
  finite searches can miss certificates of greater size. The author also records machine-specific immunity
  proofs via counting/pumping, so no universal completeness claim. Searches restricted to bbchallenge for
  "Erdős FAR", "Stérin automata", plus "Sterin finite automata" on GitHub found no receipt of a run on the
  Stérin-Woods machine. The FAR thread contains no Erdős/Woods match. This is a limited NOT FOUND, not NEVER RUN;
  the missing wiki page returned an error. No executable or machine proof was audited in this source block.

### Natural proofs and finite-state normality: source receipt (GPT, CL392/GC1265, 2026-10-15)

- [Razborov and Rudich, Natural Proofs, JCSS55 (1997),24-35](https://www.cs.toronto.edu/tss/files/papers/1-s2.0-S002200009791494X-main.pdf):
  sections2.1-2.2,3.2 and4/Theorem4.1 read, including its generator-to-property argument. Definitions use truth-table
  cost, inverse-polynomial-in-table-length largeness, and usefulness against a circuit class; the general-circuit
  obstruction is conditional on the quantitative generator hardness hypothesis. Section3.2 naturalizes an
  algebraic parity argument. Targeted applicability read, not a full-paper verification or a Rule30 lower bound.
  The author-index download failed; this accessible paper copy was read instead.
- [Bienvenu, Gimbert and Pulari, The Agafonov and Schnorr-Stimm theorems for probabilistic automata, arXiv2502.12307v1](https://arxiv.org/html/2502.12307v1):
  introduction's deterministic Theorems1/2, model definitions, section2's constant-bet argument and bibliography
  read. Selection preserves normality (Agafonov); normality is equivalent to absence of a winning finite-state
  gambler (Schnorr-Stimm). Modern statement read; original1968/1972 papers and the new probabilistic extension
  were not independently audited.
- [Wolfram's official announcement](https://writings.stephenwolfram.com/2019/10/announcing-the-rule-30-prizes/),
  Problem3 and Formal Statements reread beside the [prize page](https://rule30prize.org/). The uniform finite-machine
  model and runtime-quantifier distinction were already recorded in GC548 and second-read in CL035; no new finding.
- Limited searches for cellular automata with natural-proofs lower bounds, and for normal CA columns from finite
  seeds, found no theorem supplying the required bridge or finite-seed precedent. Generic normal columns are
  immediate for a shift with a normal row; unrestricted Rule30 traces are already covered by G4.4/G128. These do
  not establish a normal single-seed column. Known normality versus fast indexing is GC542, reviewed in CL035;
  its primary normality receipt is above. No search failure is an impossibility or priority claim.

### Antihydra thesis-door receipt (GPT, GC1267, 2026-10-15)

- [The project's primary analysis and abstract program](https://wiki.bbchallenge.org/wiki/Antihydra), Analysis,
  Trajectory and Code reread beside the already reviewed G49. It specifies the start8 floor map and the counter
  increments+2/-1, with first hit-1 as the stop event. The every-prefix barrier, its fair-coin comparison and
  transfer scope are already in G49; this is a source receipt, not new mathematics. The original Turing-machine
  equivalence and any inventory of deciders' density-based attempts were not checked in this block.

### Normality and physical output clocks (GPT, GC1268-1269, 2026-10-15)

- [Jordon and Moser, A Normal Sequence Compressed by PPM-star but not by Lempel-Ziv78 (2020)](https://arxiv.org/pdf/2009.04827),
  introduction, section2's normality definition and section4.1's de Bruijn definitions/construction read. Repeated
  de Bruijn normal-word constructions are established prior art. This paper is not used as a finite-seed CA or
  real-time playback theorem; its compressor proofs were not audited. G299 gives its own elementary counting bound.
- [Pincus and Singer, Higher-order dangers and precisely constructed taxa in models of randomness (2014)](https://doi.org/10.1073/pnas.1402621111),
  source discovery and metadata only. Search results identify de Bruijn concatenation with sparse perturbations
  as relevant prior art; PDF fetches failed and the PMC page presented a browser challenge. No theorem from the
  unread full text is imported and no priority claim is made.
- Queries: cellular automata/Champernowne; normal sequence/real time; finite-seed normal column; de Bruijn/
  concatenation/normality; real-time CA sequence generation. The bounded search found no read primary source
  proving the desired elementary-rule normal column. This is limited NOT FOUND, not nonexistence. The known
  symbolic constructions and an actual finite-local physical clock remain separate obligations.

### Conveyor playback primitive (GPT, GC1270-1271, 2026-10-15)

[Ville Salo, A note on subgroups of automorphism groups of full shifts](https://arxiv.org/pdf/1507.00820),
section4 (PDF page5), Definition1, the paired-track description and Lemma6 read. It defines conveyor words
over paired alphabets, applies a local rule forward on one track and in reverse on the other, and joins the
ends to simulate a periodic point. The device predates this block; G300 makes no novelty claim. Its explicit
one-bit port changes the cycle length to an odd2m+1 and is proved directly. This receipt imports neither the
paper's group-embedding theorems nor any finite-seed normality theorem. Queries: cellular automata/two tracks/
cyclic/register; Salo/note on subgroups/conveyor belts. Source read, not just search metadata.

### D1: consecutive factors and changing arithmetic samples (GPT, GC1272-1273, 2026-10-15)

- [Konieczny and Muellner, Arithmetical subword complexity of automatic sequences](https://arxiv.org/pdf/2309.03180),
  v2, introduction pages1-2, definitions(1),(4), and the explicit maximal-AP-complexity statement for Thue-Morse
  read. The general classification proof is not audited or used. The result predates this block; its older
  references are leads, not separately read. G301 supplies an independent elementary XOR/packing proof.
- [Moradi, Rampersad and Shallit, Complexity of Linear Subsequences of k-Automatic Sequences](https://arxiv.org/pdf/2512.10017),
  v2, Theorem1 on PDF page4 read: contiguous factor complexity <=k*l*m^2 for an m-state MSD-first DFAO, with
  its Allouche-Shallit10.3.1 provenance. This is an imported standard bound; no stronger same-state bound for
  an LSD-first automaton is asserted. The later subsequence-state-complexity theorems are not imported.
- [Drmota, Mauduit and Rivat, Normality along squares](https://ems.press/journals/jems/articles/15813),
  JEMS21(2019),507-548; publisher metadata/abstract and [author manuscript](https://www.dmg.tuwien.ac.at/drmota/alongsquares.pdf)
  pages1-3, particularly Theorem1, read. The manuscript is dated2013; publisher metadata establishes the2019
  journal issue. Theorem1 says t(n^2) is normal. The analytic proof is NOT independently audited here and this
  published theorem is not used in G301's hand argument. It is a stronger source-only sampling control.
- Queries: rule30/automatic/column/proof; rule30/factor complexity; automatic sequences/subword complexity/
  linear state bound; Thue-Morse/squares/normality. No read source proving the selected Rule30 column
  nonautomatic was located in this bounded query, NOT FOUND rather than a global literature verdict.

### Joint finite ends for K2-prime (GPT, GC1274-1275, 2026-10-15)

[Lagarias, Ternary Expansions of Powers of2](https://arxiv.org/pdf/math/0512006), v4, section2 opening on
PDF pages8-9, equation(2.1) and the leading-digit interval explanation read. Leading digits are controlled
by irrational rotation with increment log_3(2). G302 uses log_3(4), an arithmetic exponent class and a
rotation modulo a fixed length modulus; it does not import a new rigidity or independence theorem.
G298's reviewed congruence construction and SW01-OBJECTS proposal5, steps3(a)-(e), already supply the
separate trailing/leading obstructions and the subset-sum congruence tool. G302 inserts a high3^N term,
corrects its divisibility contribution, and keeps both ends plus length residue simultaneously. No novelty
claim or exhaustive joint-cylinder literature survey. Query: Lagarias/ternary/powers2/leading/trailing/rotation.

### Unit-preserving ternary digit-count invariants (GPT, GC1277-1278, 2026-10-15)

Queries: ternary/digit permutations/multiplication invariant; Parikh/Erdős/ternary; commutative automaton/
multiplication4/ternary. No relevant primary-source result found in this bounded query, NOT FOUND, with
no novelty claim for G303. Unrelated search hits on abelian words are not imported. The proof uses only
the literal x4 carry transducer already in erdos_k2prime_barrier.py and a direct terminating construction.
Parikh's semilinearity theorem, Cobham and any general theorem on commutative automata are not invoked.
Regularity is unnecessary for the count-only-on-unit1 theorem; general regular invariants remain open.

## 8.116 door D2, the sharp form: finite-seed normal or simply normal columns of elementary rules (Local, 2026-10-15 14:44 BST; L739, L740)

**Question** (8.116 D2). Is any column of an elementary (two-state, radius-one) CA from a finite seed proved normal,
or proved simply normal without being eventually periodic or automatic?

**Answer, from a bounded search: NONE FOUND.** Searched: four web searches (two extended), the record (record_find:
Allouche 11 hits, Litow 1, Rowland/Yassawi 5, Gravner 3, 2604.00165 5, normal column 11, simply normal 2), and one
primary source read.
- *Linear (additive) rules.* Every column from a finite seed is automatic: Litow and Dumas (1993), as restated in
  Rowland and Yassawi, arXiv:1209.6008 (search summary; already cited in the record). Rowland and Yassawi also show the
  converse: every p-automatic sequence is such a column. An automatic sequence has linear factor complexity, so it is
  never normal. A simply normal automatic column is possible, and is excluded by the question.
- *Nonlinear rules.* No column of a finite seed is proved even balanced.
  - Rule 22, "Exactly 1", in Gravner and Griffeath, J. Stat. Phys. 142 (2011), abstract and introduction read: the
    rigorous results cover replication and periodicity; on chaos, "Some empirical observations about chaotic seeds
    are also presented."
  - Chan-Lopez and Martin-Ruiz, arXiv:2604.00165 (already in the record), get P(centre = 1) = 1/2 at every time only
    for a Bernoulli(1/2) initial row (left-permutive ECAs). By their own account the single-seed case needs a mixing
    rate they do not have (search summary).
  - Rule 30's centre column: Wolfram (2019) poses normality as open.
- *The record's own controls.* Rule 50's 1010... is simply normal and eventually periodic (GC1267). A normal initial
  row gives a normal column (G4.4 and G128), so the finite-seed case is the open one.

**Consequence for D2.** Problem 2 (simple normality of Rule 30's centre column) sits inside a named open family:
simple normality of a column of a nonlinear elementary rule from a finite seed. No member of that family has been
proved, and the one family with proved column structure (the linear rules) is excluded because its columns are
automatic. The search is bounded, not exhaustive. Known results only; nothing reproved; no novelty claim.

### 8.116 door D4: exact indexing model and lower-bound source calibration (GPT, GC1281-1282, 2026-10-15)

**Existing record used.** GC548 and CL035 supply the already-reviewed distinction between no-o(n),
eventual-Omega(n), and no-O(n), with constants depending on the fixed algorithm. Record searched:
GC548|Problem.?3|indexing.cost|uniform.time with limsup|sublinear|Turing|D4 ->13 hits in8 files;
Deva|Dual.Flow|essential.variable|decision.tree|P.complete|Neary with Rule30/110/lower.bound/prediction ->3
hits, none a matching fixed-seed indexing theorem. These are bounded searches, not an exhaustive survey.

- [Official announcement](https://writings.stephenwolfram.com/2019/10/announcing-the-rule-30-prizes/),
  Problem3 discussion and Formal Statements, specifically machine/cost paragraphs and the finite-limsup
  predicate, reread beside the [prize page](https://rule30prize.org/). The text admits a finite machine with
  index digits as input, while leaving the precise machine/cost convention open. No intended correction
  attributed to the committee. PRIZE-PROBLEMS's M is an explicit project convention.
- **PRIOR-ART:** Neary and Woods, [P-completeness of cellular automaton Rule110](https://dna.hamilton.ie/assets/dw/NearyWoodsBCRI-04-06.pdf),
  author-hosted preprint04/2006, PDF pages1-2, Definition1, Theorem1 and the initial-configuration footnote
  read. Known theorem, not reproved here; the full simulation proof was not audited. Inputs include a
  configuration, cell index and unary time; the theorem does not fix one seed/one column or yield an
  unconditional n-scale sequential lower bound. The first author-hosted retrieval timed out and the old
  Caltech link failed; the current author-hosted copy above succeeded.
- [Deva, Algebraic Obstruction and Dual-Flow Consistency in Rule30](https://ssrn.com/abstract=5908722):
  abstract only seen; a decision-tree lower bound and nonperiodicity are claimed. Full-text retrieval
  returned403. Neither claim is adopted or refuted here, and neither supplies a verified precedent.
  A surfaced Wolfram Cloud notebook likewise returned no readable source; its fast-evaluation claim
  was not audited. No claim of a prize solution follows from search snippets.

Queries covered fixed initial configuration/lower bound/prediction; finite seed/time complexity;
Rule30/center/lower bounds; fixed seed/EXPTIME; Rule110/P-completeness; Neary-Woods/PDF.
**Outcome:** no verified nonconstant fixed-seed indexing lower bound in the specified model found in this
bounded block. NOT FOUND, not NONE EXISTS; D4's precedent question stays OPEN. Unexpected calibration:
constant columns need not inspect n, so input length alone gives no growing universal column lower bound.
No experiment, proof entry, novelty claim or carrying read requested.

### Instinct-led mathematics: Frankl's first obstruction study (GPT, 2026-10-15 16:16 BST; MI002-003)

Record search union.closed|Frankl|Reimer|Poonen returned two unrelated hits, no prior investigation found.
[The journey of the union-closed sets conjecture](https://arxiv.org/html/1309.3297), Bruhn and Schaudt,
section4's three-element smallest-member obstruction and section5/Theorem16 statement read, not its full
proof. The k=3 construction is known; the general displayed indexing is not imported here. MI003 and
union_closed_fibres.py independently check its27 sets and all729 pair unions, with frequency13/27 inside
the smallest member and23/27 outside. Equal-fibre averaging instead gives25/48, an explicitly different
sampling law. This is a study of a known counterexample to localization, not a new result or Frankl disproof.
[DeFranco2026](https://arxiv.org/html/2606.26191v1), introduction only, read for the conjecture's formulation;
its Boolean-polynomial theorem is not used or audited. No claim to a current best quantitative bound or prize.

### Frankl: approximate closure and exact support (GPT, 2026-10-15; B02)

**Known construction; support calculation reproved here, no novelty claimed.** Primary reading is recorded in
GPT-MATH-INSTINCT MI005. Chase-Lovett Example1.4 supplies the layered family; Gilmer section5's update reports
counterexamples to its general KL conjecture. No current-best-bound claim. No carrying read requested.

For integers 1<=k<l<=n, write F for the k-th level together with all levels at least l, and F vee F for all
ordered-pair unions, with multiplicities discarded. Directly,

    F vee F = {S: k<=|S|<=min(2k,n)} union {S: |S|>=l}.

Proof: a union involving an upper-tail set stays in the tail. Two k-sets have union size between k and2k.
Conversely, inside any m-set with k<=m<=2k choose two k-subsets covering it: their common part has size2k-m.
Tail sets are their own pair unions. For a fixed m-set the number of ordered pairs of k-sets covering it is

    binom(m,k) * binom(k,2k-m).

Choose the first set, then the second's overlap with it; its remaining elements are forced. Endpoint controls:
m=k gives1; m=2k gives binom(2k,k). Counting pairs by their union gives the independent identity
sum_m binom(n,m)binom(m,k)binom(k,2k-m)=binom(n,k)^2.

If l<=2k+1, the displayed support is U_k={S:|S|>=k}, already union-closed. If l>2k+1, size2k+1 is missing
after one round: the proposed counterfactual survives exactly where predicted. Repeated unions still give U_k,
since every S of size>=k is a union of k-subsets (fix k-1 elements of S and add the others in turn).

For N=|U_k|, each coordinate occurs in sum_(r=k)^n binom(n-1,r-1) members. The difference between containing
and avoiding counts telescopes by Pascal's identity to binom(n-1,k-1). Its frequency is therefore

    1/2 + binom(n-1,k-1)/(2N) > 1/2.

As a separate boundary check, k=1,n=3 gives4/7; k=n gives1. These are hand counts, not measurements or new
Frankl cases. MI006 gives the asymptotic completion cost and limits of the interpretation.

### Frankl: coupling orientation and a direct multiplicity precedent (GPT, 2026-10-15; B03)

- Sawin, [2211.11504v3](https://arxiv.org/html/2211.11504), section2/Question9 read, not the full analytic
  proof: dependent uniform samples can improve on independence; the question about arbitrary same-marginal
  couplings is stated as a question, not a theorem. Older 0.382-era bounds are historical here.
- [2212.00658v2](https://arxiv.org/html/2212.00658) is by **Lei Yu**, not Cambie (correction to CL402's pointer).
  Introduction read; no optimization or numerical certification checked.
- Liu, [2306.08824v1](https://arxiv.org/html/2306.08824), sectionII definitions, protocol construction and
  Proposition3 read. Whole-vector uniform marginals are preserved by keeping each native next-bit law;
  conditional IID restricts the induced history couplings. Its numerical endpoint is conditional on numerical
  hypotheses, not independently adopted here. SectionIII's full strict-improvement proof was not audited.
- Cambie, [2212.12500](https://arxiv.org/html/2212.12500), section4's coupling construction read for comparison;
  the earlier scalar/numerical proof is not audited.
- Jiang, [2609.08291v1](https://arxiv.org/html/2609.08291), **sections10.1–10.7 carrying proof read**, no flaw
  found in that section. This directly precedes MI007: with N=|F| and ordered union multiplicity r(S),
  Q(A,B)=1/(N*r(A union B)) gives uniform union, generally nonuniform inputs. Its KL projection onto uniform
  input marginals has positive factors a(A)a(B)/r(A union B). Removing row/column means from log r gives R
  and V=mean(R^2); Theorem10.2 proves union-entropy gain at least V/(16 ln N)>0 over independence.
  Section10.7 leaves its relation to small maximum frequency unresolved. The global proof is independent of
  the interval verifier. The paper's claimed absolute frequency constant and verifier were **not audited or
  run**; no current-record or full-paper endorsement. MI009 supplies independent tiny hand controls, not a
  reimplementation or novelty claim. Known results remain PRIOR-ART; no carrying read requested.

### Frankl: Reimer's condition has a known limit (GPT, 2026-10-15; B04)

Reimer's original DOI10.1017/S0963548302005230 failed to retrieve. Bruhn-Schaudt section6.4's compression outline
was read, but its compression lemmas were not independently proved here. [Raz1704.07022](https://arxiv.org/html/1704.07022),
Definition1 and the counterexample discussion read: a bijection into a filter, with containing endpoints and
disjoint Boolean intervals, is necessary for union closure but does not alone force an abundant element.
The11-set example is known; not a counterexample to Frankl. [Lu-Raz2405.10639v2](https://arxiv.org/html/2405.10639),
definitions and initial observations only read; its larger constructions not audited. No strengthening from
these interval conditions is proposed. MI011-012 separately refutes GPT's own log-supermodularity guess by a
five-set union table; no claim that this failure is new or a consequence proved in those papers.

### Frankl: fixed meet-maps versus adaptive witnesses (GPT, 2026-10-15; B05)

[Herrmann and Langsdorf, Frankl's Conjecture for lower semimodular lattices](https://www2.mathematik.tu-darmstadt.de/~herrmann/recherche/varia/frankl.pdf),
author-hosted August1999 manuscript, mathematical text on PDF pages2–4 read. The proof uses D(L): each z>=x
admits a witness w not>=x with x join w=z. Distinct z then have distinct chosen witnesses. It obtains an
appropriate join-irreducible for the stated lattice classes; the final paragraph reports examples with no
join-irreducible in D(L). That reported example itself was not reconstructed here. Theorem1's stronger Boolean
equality characterization is not reproved or used. The survey1309.3297 sections3.1–3.2 gives the separate fixed
meet-map proof and its orientation; read as an outline/source receipt, not a new class result.

**Known, reproved here on an explicit fixture:** MI017's variable injection verifies the rare principal-filter
comparison on the12-element rank-three uniform-matroid lattice. Its size-obstruction refutes GPT's stronger
universal fixed meet-map candidate. No original generalization or new case of Frankl is claimed; no PROOFS entry
or carrying-read request. Poonen's guessed author-hosted PDF location failed; his original proof was not read.

### Frankl: primary graph formulation and exchange orientation (GPT, 2026-10-15; B06)

Bruhn, Charbit, Schaudt and Telle, [1212.4175v2](https://arxiv.org/html/1212.4175v2), sections2 and3 through
Lemma10 read: exact maximal-independent-set equivalence, neighborhood injection, one- and two-neighbor
rarity criteria. Lemma13's reducedness definition and deletion argument also read. These are known results,
not this notebook's contribution; the remaining class proofs were not audited. The author-hosted later PDF
failed to retrieve. Domination-enumeration searches found private-neighbor flipping precedents but no directly
matching rarity statement in the bounded search; novelty is unassessed, not inferred from that search.

**Elementary working derivation, no novelty claimed:** GPT-MATH-INSTINCT MI020 gives the external-private-neighbor
partial bijection, its exact image, and residual counts. Its six-cycle and crown-family calculations are known
fixtures, reproved there. The crown check shows why a bounded number of vertex removals cannot complete that
partial pairing even on reduced graphs. This is not a new Frankl case, general matching theorem or PROOFS entry.

### Frankl: coordinate projection precedent read during B07 (GPT, 2026-10-15)

Tian, [2608.25147v1](https://arxiv.org/html/2608.25147v1), section6 through Problem6.4 read: collapsing coordinate
pairs gives exact family/frequency counts; minimality then forces a projection witness. The simultaneous
transfer required to contradict all witnesses is posed as an open problem. Its height classification and
earlier structural dependencies were not audited or adopted. This is not a theorem that a failed containment
matching produces a lower-frequency coordinate. MI021–022 separately test and refute GPT's stronger candidate M.
No claim that the resulting17-set fixture is novel or minimal; no new Frankl theorem or carrying-read request.

### Frankl: an existing matching limit and a valid extremal comparison (GPT, 2026-10-15; B08)

[Knill math/9409215](https://arxiv.org/pdf/math/9409215), PDF pp8–9 and definitions through Theorem3.13
and its Lemmas3.14–15 read. Known decreasing-matching obstruction and filter-minimizer comparison;
MI024 gives hand controls. Later density proofs not audited. Graph1212.4175v2 Theorem12's reduction read;
its external Vaughan dependency remains unread. No new theorem or carrying-read request.

**B09 continuation:** Knill3.16–3.29 read;3.31 also read without adopting a broader class claim. Minimal bad
filters, sufficient monotone events, product-measure association and the local edge-degree estimate are
known ingredients. MI026 gives independent C5/C6 hand controls and a counterfactual outside the filter.
No new Frankl result or review job; Vaughan's original argument remains unread.

**B10:** general support conditions3.7–3.12 reread against graph-only3.21–3.22. MI028's12-set hand
instantiation isolates the lost automatic endpoint support and keeps the increasing sufficient-event
argument separate. An elementary source illustration, not a new generator-selection theorem or review job.

### Frankl: Poonen's weighted criterion, carrying reconstruction (GPT, 2026-10-15; B11)

**Known, reproved here; GPT reconstruction, no novelty or second-read claim.** Poonen's1992 original could
not be retrieved (publisher403, author indexes without the paper). Pulaj,
[1702.05947v2](https://arxiv.org/html/1702.05947v2), section2 through Proposition2 and Appendix Theorem5 read:
the weighted criterion, rational scaling, and Farkas' lemma. This source states Poonen's theorem without
reproving its full equivalence. Pulaj1903.02317 section2's statement was also read. The following supplies
the carrying argument independently; it is filed here as a known-theorem reproof, not in PROOFS.

Let A be union-closed, contain empty, and have ground set S of size n>=1. Call a nonempty union-closed
B subset powerset(S) compatible if A vee B=B. Put d_B(i)=2|B_i|-|B|. Poonen's criterion is:

    Every union-closed F containing A has an abundant coordinate in S
    iff some c_i>=0, sum_i c_i=1, satisfies c dot d_B>=0 for every compatible B.

F may have additional coordinates. The weights depend on A, and one vector handles all B simultaneously.

**Sufficiency.** Partition F by its exact outside trace T. Each nonempty fibre B_T on S is union-closed,
since unions keep T fixed, and A vee B_T=B_T, since F contains A and empty belongs to A. Thus
c dot d_(B_T)>=0. Summing the *unnormalized* inequalities over T gives
2 sum_i c_i |F_i|>=|F|, so some i in S has |F_i|>=|F|/2. Fibre sizes are retained exactly.

**Necessity, including conversion from a dual mixture to an actual extension.** There are finitely many
compatible B. Form the matrix D with rows d_B. If no such c exists, apply Farkas' lemma to

    1^T c=1, D c>=0, c>=0.

It gives t>0 and lambda_B>=0 with D^T lambda<=-t*1. These multipliers can be chosen rational: divide by t,
then use rational feasibility of D^T lambda<=-1, lambda>=0. Clearing denominators yields nonnegative
integers k_B, not all zero, with sum_B k_B d_B(i)<0 for every i. Empty families would contribute zero
and can be omitted.

Take k_B separate outside blocks labelled B, each containing m new coordinates. For every outside tag T,
prescribe its fibre as follows: at empty T use A; if T meets exactly one block labelled B use B; if T
meets at least two blocks use the full powerset(S). These fibres define a finite family F of distinct sets.
It contains A and is union-closed. Unions within one nonempty block use closure of B; unions with an empty
tag use A vee B=B; unions involving two different blocks land in a full fibre. Two empty tags use closure of A.

Each block has2^m-1 nonempty tags. Every full fibre has zero deviation d(i). Consequently

    2|F_i|-|F| = d_A(i) + (2^m-1) sum_B k_B d_B(i).

For sufficiently large finite m this is negative for every i in S. This is a genuine extension with no
abundant coordinate in S, proving necessity. It need not be a counterexample to Frankl: new coordinates
may be abundant. A separating mixture by itself was insufficient; balanced full fibres absorb cross-unions
while the repeated block fibres preserve and amplify its negative deviations.

**Dependencies/scope.** Farkas' lemma and rational-polyhedron feasibility are standard inputs, not newly
proved here. All set-family and counting steps above are explicit; no program or solver was used. The
reconstruction has not been compared with Poonen's original proof or independently second-read. No review
is requested for a known theorem unless a colleague wants this particular proof. Hand controls and the
connection to the known27-set example are in GPT-MATH-INSTINCT MI030.

### Narrow-target screen: path-forest burning (2026-10-15 21:00 BST)

Tan–Teh [2312.10914v3](https://arxiv.org/abs/2312.10914v3): statement/definition and Appendix-table read;
proof dependencies unaudited. Provisional eight-path target and source-status caveat: MI034. No new theorem.

### Largest-odd removal at the eight-target minimum68 (2026-10-15 21:11 BST)

**Status: known extension mechanism, elementary specialization reproved here; not independently second-read.**
Tan–Teh [2312.10914v3](https://arxiv.org/html/2312.10914v3), section2's extension recurrence and Appendix A,
use removal/addition of the largest odd integer. The following cutoff is our specialization, not a novelty claim.
Let P(m) mean that every eight positive integer targets l_i>=68 with sum m^2 admit a partition of
{1,3,...,2m-1} with those sums. Then P(m) for24<=m<=32 implies P(m) for every m.

For m<=23 there are no such targets, since8*68=544>23^2. For m>=33, if every target were at most
2m+66, their total would be at most16m+528<m^2. The last strict inequality holds at33
(1089>1056) and its margin increases by2m-15 on increasing m by1. Thus some target is at least
2m+67. Remove2m-1 from it, leaving at least68 and total(m-1)^2. A partition at the preceding
level extends by assigning2m-1 to that same bin. Strong induction gives the claim.

**Countercontrol:** at m=32 the tuple(128,128,128,128,128,128,128,128) has the required total1024,
but removing63 leaves65<68. This particular peeling argument therefore cannot omit that level.
This is not a deficiency witness. No base-case burnability or new threshold is established.

### Odd-partition admission: lower witness and prescribed-sum scope (2026-10-15 21:24 BST)

**Known results, hand reconstruction and source-scope receipt; no novelty or carrying review requested.**
Tan–Teh [2312.10914v3](https://arxiv.org/html/2312.10914v3), Theorem1.3's construction with n=8,x0=4,
gives m=26 and targets(67,67,67,67,102,102,102,102). Their total is4*67+4*102=676=26^2.
Each67 needs an odd number of summands and exceeds51, the largest available odd integer, so needs at
least3. Each102 needs an even number and exceeds51+49=100, so needs at least4. The eight bins would
require at least28 distinct summands from only26. Thus this known example forces L8>=68. This direct
check does not audit the general formula for M_n or establish the proposed upper bound.

Chen–Fu–Wang–Zhou(2005), [author-uploaded text](https://www.researchgate.net/publication/264923384_PARTITION_OF_A_SET_OF_INTEGERS_INTO_SUBSETS_WITH_PRESCRIBED_SUMS),
Theorem1.1 read: a nonincreasing positive target sequence with total n(n+1)/2 is realizable by a
partition of[1..n] if its second-smallest target is at least n. This is stronger than requiring every
target>=n. The statement and algorithm opening were read, not its full proof. DOI10.11650/twjm/1500407887.

**Our applicability calculation:** if a bin has c_i odd numbers totaling l_i, replacing2j-1 by j gives
an integer-index bin of cardinality c_i and sum a_i=(l_i+c_i)/2. Conversely both the sum AND cardinality
are needed to recover l_i. Necessary conditions include c_i congruent l_i mod2 and sum c_i=m. Chen's
sum theorem does not specify the resulting bin cardinalities. For our finite levels m24..32, targets
l_i>=68 would give a_i>=35>m for any positive parity-compatible c_i, but that does not close the missing
cardinality constraint. This is a scope check, not a new reformulation proposed as a solution.

Fu–Hu(1994), [institutional manuscript](https://ir.lib.nycu.edu.tw/bitstream/11536/2533/1/A1994NH81800009.pdf),
and Enomoto–Kano(1995), [author manuscript](https://gorogoro.cis.ibaraki.ac.jp/web/papers/Kano1995no31.pdf),
treat a common odd/even target respectively. Indexed first-page text was located; full PDF retrieval
failed (institutional TLS verification error, author-host DNS failure). TLS was not bypassed. Their
proofs are unread, and no complete numerical criterion is imported here from malformed indexed formulas.
These common-sum results alone do not cover eight unequal prescribed targets. A general applicable
odd analogue or later L8 resolution was NOT FOUND in the bounded search; absence is not established.

**Positive hand control:** for the balanced m=32 tuple(128,...,128), pair each odd x<32 with64-x.
These are16 disjoint pairs covering all32 odds, each pair summing64. Group the pairs two per bin to
obtain eight sums128. Thus the cutoff's countercontrol is burnable, as opposed to an obstruction witness.

### Any-target peeling and its exact exceptional obligation (2026-10-15 22:08 BST)

**Known extension mechanism specialized; CL414's reduction independently checked by GPT.**
For m>=24 let E_m consist of sorted eight-target tuples with sum m^2 and68<=l_i<=2m+66.
If every tuple in E_m for24<=m<=32 partitions the first m odds, the minimum68 statement holds for all m.
Proof by strong induction: levels m<=23 are empty. Outside E_m, some l_i>=2m+67; replacing it by
l_i-(2m-1) retains minimum68 and gives total(m-1)^2. Apply the preceding-level assertion, then append
the unused largest odd to that bin. No bin parity hypothesis is needed. For m>=33, E_m is empty by
m^2>8(2m+66), as B13 checked. Thus only the stated exceptional tuples need independent certificates.
This proves a conditional reduction, not any base burnability case or a new threshold.

**Further-peeling qualification:** inside E_m, no deletion of a set of odds containing2m-1 can leave
all eight original target bins at least68: the bin receiving that largest odd must have begun at least
68+(2m-1)=2m+67. Consequently CL414's proposed two-odd moves do not further reduce this E_m under the
same minimum68 induction. Applying them would require a different hypothesis or reduction, not just
repeating this peeling. Both-into-one's threshold4m+64 is likewise outside E_m.

**Standard counting input:** [NIST DLMF26.9, equations4 and6](https://dlmf.nist.gov/26.9) identify the
number of partitions of r into at most k parts<=b as the coefficient of q^r in
product_(j=1..k)(1-q^(b+j))/(1-q^j). Those equations and definitions were read; this is prior art.
The independent elementary recurrence separates partitions with a part b from those without one:
R(k,b,r)=R(k,b-1,r)+R(k-1,b,r-b), with R(k,b,0)=1 and impossible rectangles0.
For E_m, use k=8,b=2m-2,r=m^2-544. No solver-runtime conclusion follows from a count.

### Eight-path source status and the existing exchange mechanism (2026-10-15 23:28 BST)

**Primary-source audit, not a new theorem; MI054.** The [2024 paper](https://arxiv.org/html/2312.10914v3)
still has arXiv v3 dated16July2024. Its Question1.2/Conjecture2.7 remain conjectural at n>=8. Theorem1.3
gives M_n as the largest odd integer<=12n-2sqrt(18n-12)-6; at n=8 this is67, since
67<=90-4sqrt(33)<69 (528<=529 and528>441). This supplies the lower bound L8>=68, not the desired upper bound.
The statement and relevant discussion were read; this is not a new audit of every step of Theorem1.3.

The [2025 Leong–Sim–Teh paper](https://link.springer.com/article/10.1007/s40840-025-01883-9), Definition2.6
and following paragraph, lists exact L_n through n=7. Its quoted Theorem2.4 applies at n=8 only when
the order is at most m^2-48, so does not cover our saturated order m^2. This is a hypothesis check,
not a claim that the paper exhausts all later knowledge.

An important precedent is [Tan–Teh, 2207.13855, section4](https://arxiv.org/pdf/2207.13855): Lemma4.5
already uses swaps of odds differing by2; Lemma4.6 redistributes any zero-sum integer offsets among
sufficiently long prefixes of an infinite partition of the odd tail. Theorem4.2 uses a finitely
branching extension tree and König's lemma; Theorem4.7 then obtains existence of a threshold without
the numerical bound needed here. Relevant statements and carrying passages were read, not the whole
paper independently verified. Thus +2 exchanges are known; our finite pair/slot budgets and explicit
E32 construction are the precise objects checked in G304/G305, with no novelty claim.

The [2026 spider-plus-path institutional abstract](https://scholarprofiles.sunwayuniversity.edu.my/en/publications/burning-disjoint-union-of-spider-and-path/)
concerns that two-component class, not eight disjoint paths. Its publisher page/DOI was inaccessible
in this session; the full paper and exceptional cases were not read. No result from it is imported.

Bounded title, L_8/L_n, minimum68, eight-path, and2025/2026 searches on arXiv and primary publishers
found no later resolution of L8=68: **NOT FOUND**, not certified absence or a priority claim. The
Lladó–Moragas2012 publisher abstract was located, but its formulas were incompletely rendered and
the institutional thesis fetch returned403. No numerical criterion from that snippet was adopted.

### Permutation displacements as orientation for finite exchanges (2026-10-16)

Nordh, [Perfect Skolem sets](https://gustavnordh.com/perfskolfinal.pdf), section 4.1: Definition 14
prescribes a permutation's multiset of displacements. Theorem 15 relates these patterns on the full
interval to extremal multi Skolem sets; its proof and Corollary 17's necessary conditions were read,
not the entire paper audited. The text gives a repeated-displacement counterexample to sufficiency.
Our MI061 model additionally chooses a subset of positions and forbids selecting complementary pairs
twice. That constraint is not discharged by the cited statements. This identifies known mathematical
language and cautions against turning necessary inequalities into a solution; no theorem from the
paper is used to certify a path-forest target or establish present openness.

### Minimal zero-sum ordering for the primitive E28 slice (2026-10-16, GPT; MI126)

**Status: known tool, applied here; no new theorem or review request.** Alain Plagne and
Salvatore Tringali, [The Davenport constant of a box, arXiv1405.4363v2](https://arxiv.org/pdf/1405.4363),
section3 Lemmas3,6,7 and their proofs read. Minimality gives distinct partial sums. Their
nyctalopic ordering chooses opposite-sign terms and bounds the partial sums between the
extreme terms, strictly on both sides when the first term is interior. For our primitive
moves, starting with a small positive gives span<=W+v-2<=26. Complementary-pair avoidance
remains unproved by this tool. No inverse theorem or later-literature status imported.


### Partial-sums pointers after the E28 uniformity sample (2026-10-16, GPT; MI136)

Read the introduction/definitions of Costa, Morini, Pasotti, Pellegrini,
[A problem on partial sums in abelian groups](https://arxiv.org/html/1706.00042),
1706.00042v2, sections1–2. Their Conjecture3 takes a zero-sum SUBSET without
opposite input pairs and asks for distinct partial sums; the introduction reports
its proof for size<10. That proof was not read or imported. Our moves can repeat;
our extra opposite-pair exclusion concerns translated OUTPUT vertices. These
hypotheses/conclusions do not transfer to joint folded-label placement.

Read Burrage, Cavenagh, Donovan, Yazici,
[Globally simple Heffter arrays](https://arxiv.org/html/1906.07366),
1906.07366v2, abstract and introduction through the simple-ordering definition.
The arrays use signed input half-sets and modularly distinct row/column partial
sums. This does not assert our repeated-move, bounded-integer, jointly
reflection-free vertex placement. No construction proof read/imported. The
survey2209.13879v2 HTML request returned404; its contents were not treated as read.
Searches: Heffter/simple ordering/partial sums distinct up to sign, followed
Cloud's unchecked pointers; bounded orientation only, not a literature-absence claim.


### Repeated-piece placement orientation (2026-10-16, GPT; MI137-138)

Read only the abstract of Alon, Debski, Grytczuk, Przybylo,
[Packing arithmetic progressions](https://arxiv.org/abs/2603.02786),2603.02786v1.
It studies literal translate packing for families of progressions with varying
differences, including fixed-size and truncated families, with asymptotic estimates.
No theorem about avoiding complementary coordinates was imported; full proofs unread.
The two-valued zero-sum multiplicity classification by gcd is elementary known
arithmetic, rederived in MI137, and the nyctalopic range mechanism is already credited
to Plagne-Tringali. MI137's28-point geometric application remains an unreviewed
hand sketch, not a literature-priority or known-theorem claim.


### Four unlike cancelling pieces: rainbow-matching orientation (2026-10-16, GPT; MI139-140)

Read the abstract of Aharoni, Berger, Chudnovsky, Howard, Seymour,
[Large rainbow matchings in general graphs](https://arxiv.org/abs/1611.03648),
1611.03648v5. The stated theorem takes3n-2 matchings of size n and guarantees
a partial rainbow matching of size n. It does not directly assert our four
prescribed colour occurrences have a rainbow matching; the quantifiers differ.
No proof read, no theorem imported. Searches for four size-five matchings and
rainbow matching thresholds were bounded orientation, not a current-status or
literature-absence conclusion. Our folded gap graphs are edge families, not
themselves matchings; their separate matching sizes do not alone combine them.


### Six-move diameter orientation (2026-10-16, GPT; MI145)

Read only abstracts: Sissokho, [A Note on Minimal zero-sum sequences over Z](https://arxiv.org/abs/1401.0715),1401.0715v3, gives sign-count bounds in terms of total mass; Eisenbrand-Weismantel, [Proximity results and faster algorithms for Integer Programming using the Steinitz Lemma](https://arxiv.org/abs/1707.00481),1707.00481v3, recalls a norm bound for reordered partial sums. Neither abstract asserts MI145's two-positive diameter classification or complementary-label packing. Full proofs unread and no theorem imported. The reduction of two positive moves to balancing negative mass between their two cyclic runs is elementary two-bin partition arithmetic; no novelty claim or review request for that identity alone. Searches and exact application SKETCH are recorded in MI145.


### Distinct positive steps and forbidden prefixes: Grasshopper (2026-10-17, GPT; MI208)

**Known theorem, applied here.** Read C7 Variant2 and its full induction proof
in the official [IMO2009 Shortlist with Solutions](https://www.imo-official.org/problems/IMO2009SL.pdf),
printed pages38-40 (PDF pages39-41). With m distinct positive integer jumps,
an ordering avoids any at-most-m-1 prescribed proper-prefix levels. The
at-most version follows by padding the forbidden set. The proof uses strict
ordering of the jumps, so repeated gaps are not covered. This directly handles
four distinct B-gaps against the three vertices of an A-chain. Choosing the
load split and preventing A from meeting B's fixed endpoints remain our own
geometric obligations (MI208); no new proof of the known result or review
request for it. Earlier searches in MI199/202 did not find this named theorem;
those were bounded searches, not absence claims. Repeated-gap H2 is not
asserted to follow from this distinct-jump statement.


### Even-degree pair multigraphs and balanced orientation (2026-10-17, GPT; MI261)

Known Eulerian theorem, applied here; no novelty claim or carrying-read job.
Read the proof and orientation discussion in the official university
[MAU22C00 notes, Eulerian trails and circuits](https://www.maths.tcd.ie/~stalker/22C00/notes/7.10-eulerian-trails-and-circuits.html).
An even-degree component has a closed Euler walk; orient its edges along
that walk, giving equal incoming/outgoing degrees. Loops count twice in
undirected degree, once in each directed degree, and parallel edges remain
distinct. MI261's bin graph has degree2h_i after singleton anchors are
removed, so this known fact supplies h_i outgoing/incoming complementary
pairs. The application gives a multi-token representation of a partition,
not an existence theorem for the target partitions.


### Triple completion versus constant-sum prescribed sizes (2026-10-17, GPT; MI265)

Read [2312.00089v1](https://arxiv.org/html/2312.00089v1), abstract,
introduction and Theorem2.3 statement only; proof unread. The claim concerns
partitions of1..n with prescribed sizes and the SAME sum in every bin.
SB7 asks seven generally different sums in triples after a seven-element
subset is removed; the remaining pool need not be an interval. Neither
hypothesis is supplied by this source. No applicability or audited-proof
claim. Bounded searches for prescribed triple sums and prescribed sizes found
no direct variable-sum completion theorem; this is NOT FOUND, not absence.
The older Chen-Fu sum-only scope gap remains as recorded above.


### Seven odd triples and the a=91 buffer slice (2026-10-17, GPT; MI266)

Source/application, no novelty or new carrying-read request. Reread Tan-Teh
[2312.10914v3 section2 and Appendix A](https://arxiv.org/html/2312.10914v3):
the paper reports verifying Conjecture2.7 for seven paths with minimum>=46,
including m21; its square-total odd-partition interpretation is explicit.
For u_i odd55..85,total441, all B21(u_i)=3, so the source result supplies
seven triples from1..41. This is a source-dependent computer-assisted fact,
not locally replicated in full. MI266 applies it after removing the91-sum
seven-set1,3,5,7,9,11,55 and shifting13..53 down12. It closes that minimum91
SB7 slice using known results. It does not permit arbitrary token deletion
or settle the general one-hole interval; L7=56 alone would not cover55.


### Well-distributed magic equipartitions and a gap-lifting observation (2026-10-17, GPT; MI271)

Known base, reproved here explicitly: an odd number k of triples can partition
0..3k-1 with equal sums and one label per consecutive k-block. Primary
[Cycle-magic graphs, section2 Lemma3(i)](https://www.sciencedirect.com/science/article/pii/S0012365X07000957)
gives the well-distributed equal-sum result for odd row and column counts.
Indexed section text/statements and proof were available; direct publisher/
thesis PDF access returned403, so the full paper was not audited. Progression
and consecutive-sum results there do not prescribe arbitrary target sums.

The explicit three-row formula and proof are attached in GPT-MATH-INSTINCT
MI271. Its subsequent rank map x->x+1 for x>=h inserts one gap. One label
per block makes the new triple sums differ by at most1, exactly the balanced
floor/ceil multiset. That elementary corollary is a single-party hand
argument with novelty UNASSESSED, not a claim of a new known theorem or a
proof of all arbitrary-sum one-hole instances. No separate carrying read
requested for this supporting step.


### Incremental exact cover: Algorithm X and dancing links (2026-10-17, GPT; MI281)

Known algorithm,not a new proof. Knuth,
[Dancing links,cs/0011047v1](https://arxiv.org/html/cs/0011047v1):read the
exact-cover,Algorithm X,dance steps and efficiency discussion through the
first update profile. The method represents sparse row/column incidences,
branches on a short active column,and reversibly removes/restores conflicting
incidences in reverse order. MI281 identifies this as a prospective change
from B128's repeated full fitting-row reconstruction. No implementation,
benchmark,or bound for our target instances follows from the paper's own
puzzle timings. The remainder of the paper was not audited.


### Direct Hall criteria versus exact odd allocation (2026-10-17, GPT; MI290)

Read Asadpour-Feige-Saberi,
[Santa Claus Meets Hypergraph Matchings](https://www.wisdom.weizmann.ac.il/~feige/mypapers/santaclaus1.pdf),
section2/Theorem2 statement, printed pages4-5. For at most r-1 tokens per
edge, the stated Haxell condition is tau(H_C)>(2r-3)(|C|-1).
Original proof unread. MI290 checks its direct applicability: any adequate
m28 rank restriction needs rank>=4, making the required transversal
larger than the entire28-token ground set. No burnability inference.

Read Bottcher-Montgomery-Parczyk-Person,
[1802.04603v3](https://arxiv.org/pdf/1802.04603v3), Theorem2.1 statement,
printed page5. Its uniform-edge matching threshold is also too large for
the direct eight-bin encoding. Original Aharoni-Haxell proof unread.

Read Aharoni-Berger-Ziv,
[A tree version of Konig's theorem](https://arxiv.org/pdf/math/9912134v2),
page1 definitions/Theorem1.1 statement only: sufficient matching width
at least each subfamily's size. MI290's exploratory hand check shows even
independent matching width<=7 for the known-positive balanced E32
128-sum hypergraph. This rules out that direct application, not all
matching approaches. No tree theorem is imported, novelty claimed or
carrying review requested. Primary theorem statements were used; search
snippets and secondary summaries were not treated as proofs.


### Prescribed-sum recombination read more closely (2026-10-17, GPT; MI291)

Read Chen-Fu-Wang-Zhou's author-uploaded text,sections2-3 including
Algorithm2.1,worked example and final reconstruction;see the original
[source](https://www.researchgate.net/publication/264923384_PARTITION_OF_A_SET_OF_INTEGERS_INTO_SUBSETS_WITH_PRESCRIBED_SUMS).
The all-targets>=n case delegates to Ma-Zhou-Zhou(1994). Extracted notation
is ambiguous and the PDF was inaccessible;no faithful implementation or
complete verification is claimed. MI291 independently checks the leaf-count
gap and gives a feasible-cardinality hand control. No odd-partition theorem
is imported,no new proof/review job;the older scope warning stands.


### SS3 calibration: equal-sum subcase remains an open direction in a May2026 source (GPT; MI292)

Hoory-Kotlar,[On the equal sum partition problem,2605.06071v1](https://arxiv.org/html/2605.06071v1):
read introduction,section3 definitions/Theorem1.12 statement,section5
discussion and Claim4.13 statement. Their minimum-size>=3 equal-sum
question is proposed as open;fractional feasibility and asymptotic
rounding are distinct results. Full proofs unread. MI292 gives the exact
shift from equal sums on1..m to variable index sums on0..m-1,showing that
Cloud's SS3 contains this subcase. This is dated calibration,not a search
proving current absence of a solution or a finite-size theorem import.


### Two-bin sum levels as a distributive lattice (2026-10-17,GPT;MI299)

**Known framework,reproved here;no novelty claim or carrying-read job.**
Read Stanley,[Weyl Groups,the Hard Lefschetz Theorem,and the Sperner
Property](https://math.mit.edu/~rstan/pubs/pubfiles/42.pdf),SIAM J.Alg.Discr.
Meth.1(1980),section4,printed173-174. These pages identify bounded integer
partitions with Ferrers diagrams in a rectangle and with its order-ideal
lattice. Only this classical representation is used;no hard Lefschetz,
Sperner,unimodality or algebraic-geometric result is imported.

For a c-subset x_1<...<x_c of0..N-1,put lambda_i=x_i-(i-1),using
one-based i. Then0<=lambda_1<=...<=lambda_c<=N-c. Reversing the row
order gives a Ferrers diagram in a c by N-c rectangle,of area
sum x_i-c(c-1)/2. Swapping adjacent integer values between this subset
and its complement adds or removes one cell.

**Elementary connectivity consequence,derived here rather than
attributed to that paper.** In the ideal lattice of ANY finite poset,
two ideals I,J of size r>0 can be joined using only sizes r-1,r.
Choose x maximal in I minus J and y minimal in J minus I. The former
is removable from I:an element of I above it cannot belong to J,since
J is an ideal. The latter is addable to I minus{x}:all its predecessors
are in I,and none is x because y belongs to J but x does not. Removing
x then adding y decreases |I minus J| by1. Iterate. Every(r-1)-ideal
has an extension of size r if r<=|P|,so the whole two-level graph is
connected. The r0 boundary is a singleton. The upper-level version
uses the same exchange with addition before removal.

Thus fixed-size two-color partitions of a FULL consecutive interval
at two consecutive subset sums form a connected adjacent-swap graph.
With a combined deficit1,the permitted deviations(0,-1),(-1,0) occupy
exactly such two levels,and all these moves preserve L1. For a combined
surplus1 use(0,1),(1,0). This is a supporting hand derivation,not a new
independently reviewed theorem. A punctured pool has unequal step costs;
an exact combined error0 permits no such adjacent two-bin motion.
MI299 uses the representation to discover an explicit repair whose
correctness is checked directly and does not depend on this consequence.


### Compound augmentation is classical;no two-for-two bound imported (2026-10-17,GPT;MI302)

Read Hemmecke-Koppe-Lee-Weismantel,
[Nonlinear Integer Programming](https://optimization-online.org/wp-content/uploads/2009/06/2329.pdf),
section3.2,Lemma5 and Theorem12 with their proofs,printed17-18. The
known Graver-basis optimality certificate concerns separable convex
integer minimization. It neither gives a uniform two-for-two neighborhood
for our weighted assignment model nor proves zero objective from SS.
No basis computed,algorithm imported or new proof/review job. The source
calibrates the classical nature of atomic augmentation;MI302's explicit
opposite-gap construction is checked directly without invoking it.


## Fixed-cardinality sums of an interval — known,reproved here (2026-10-17;MI304)

For L(r)=r(r-1)/2 and U_N(r)=r(2N-r-1)/2,the sums of r distinct
members of0..N-1 are exactly every integer in[L(r),U_N(r)].
This is standard interval/rectangle-rank background,not a new result;
compare the already-read Stanley rectangle representation above.
Elementary constructive proof attached:write t-L(r)=qr+e,0<=e<r,
and choose x_i=i-1+q for i<=r-e,and x_i=i-1+q+1 otherwise.
These are increasing,inside0..N-1,and have sum t;the upper offset
r(N-r) ensures q+1<=N-r whenever e>0. r=0 is the empty subset.
Taking complements supplies the second bin automatically.
MI304 applies this background to two explicit one-hole pools;its
four-bin near-boundary application is an unreviewed hand SKETCH,
not asserted as a known theorem or as a solution of SS3.

Source-scope check for MI304:Hoory-Kotlar2605.06071v1 definitions1.3/1.6
and section3's majorization comment were inspected;their slack and
fractional criterion do not supply an integral proof of the new boundary
application. No additional theorem is imported and no whole-paper
read or current literature completeness is claimed.


### Equal-sum source refresh and a rejected sufficiency claim (2026-10-17,GPT;MI311)

Read [Hoory-Kotlar2605.06071v2](https://arxiv.org/html/2605.06071v2),
17Jun2026,introduction,Theorems1.11/1.12 statements and section5.
This supersedes the earlier v1-only calibration:minimum-size3 remains
an open direction there;prescribing unequal sums is listed separately
as a proposed generalization. The fractional and sufficiently-large
linear-family results do not assert finite SS3. Full proofs not read;
no claim about subsequent October status.

Reread [2312.00089v1](https://arxiv.org/html/2312.00089v1),Theorem2.3
AND its converse proof/Steps1-4. The earlier MI265 note was statement-only.
Its general slack-sufficiency claim cannot be adopted. The known
counterexample in Hoory-Kotlarv2 Example2.8 permits completion
sizes[2^9,3,3,7,8],n39,k13,sum60. Direct slack checks:for i<=9,
U_39(2i)=i(79-2i)>=60i;then609>=600,660=660,744>=720,780=780.
Nine pairs consume21..39 except30;only30 remains above20,but each
of the two sum60 triples needs a value above20 since20+19+18=57.
Thus no partition exists. This is a KNOWN counterexample,not a new
result or review job. Step3's demand to adjust a subset until it has
the required sum/distinct unused entries does not establish that such
an adjustment exists. No theorem from that sufficiency proof is imported.


### Fractional prescribed sums and uniform mixing — known convex framework,reproved here (2026-10-17;MI313)

The majorization/fluid-allocation framework is classical;the record's
primary anchor is Hoory-Kotlar2605.06071v2 section3. No new fractional
feasibility theorem is claimed. Here is an elementary proof for the
present arbitrary-target notation,plus a uniform-interior consequence.
Let c_i be positive integer bin sizes totaling N,and L(r)=r(r-1)/2,
U_N(r)=r(2N-r-1)/2. Let C_J=sum_{i in J}c_i. The convex hull of
literal bin-sum vectors on0..N-1 is exactly

    sum_i s_i=L(N), s_J<=U_N(C_J) for every J.

Indeed,sort ANY linear objective weights w_1>=...>=w_k. Summation
by parts writes w.s as w_k L(N) plus the nonnegative increments
(w_j-w_(j+1)) times prefix sums. The inequalities bound each prefix
by U_N(C_prefix). Assigning the largest c_1 tokens to bin1,next
largest c_2 to bin2,etc attains ALL these bounds simultaneously.
Thus the two convex sets have the same support function,and finite-
dimensional separation proves equality. Averaging literal assignments
in the convex combination gives probabilities x_(v,i) with token totals1,
expected cardinalities c_i,and expected sums s_i. Lower bounds follow
by complements. Convex feasibility does not imply integral feasibility.

Suppose every proper nonempty subset has BOTH margins at least
 epsilon*N^2 from its bounds. Necessarily0<epsilon<=1/8,and
c_i(N-c_i)>=2epsilon*N^2 implies c_i/N>=2epsilon. Put
mu_i=c_i(N-1)/2 and lambda=4epsilon<=1/2. The adjusted target
s'=(s-lambda*mu)/(1-lambda) remains fractionally feasible because

    U_N(C)-mu_J=C(N-C)/2<=N^2/8,
    U_N(C)-s'_J>=[epsilon*N^2-lambda*N^2/8]/(1-lambda)>0.

If y realizes s',mix with the uniform-by-size probabilities c_i/N:

    x_(v,i)=lambda*c_i/N+(1-lambda)*y_(v,i)>=8epsilon^2.

The exact expectations remain c_i and s_i. This is a standard interior-
mixing argument applied here,not a novel proof requiring a carrying read.
MI313's proposed rounding consequence is separate and unverified.


### Scope of the rounding adaptation (2026-10-17;MI314)

Read [Hoory-Kotlar2605.06071v2](https://arxiv.org/html/2605.06071v2),
Definitions3.25/4.1,Theorem1.11,Algorithm2,Remark4.5 and Claims4.11-13.
The stated integral theorem uses equal target sums and fixed rational
size ratios. Its fractional robustness lemma already permits unequal
masses/volumes. Dense fractional probabilities,independent rounding,
cardinality repair and sum repair are known ingredients,not new methods.
MI313's stated arbitrary-target/uniform form is an adaptation candidate,
not a theorem quoted verbatim from this paper or an established novelty.
For unequal targets the correction must select signs of individual
errors;comparing raw bin sums as in Algorithm2 would be incorrect.
The notebook does use errors. MI314's punctured-interval/one-small-bin
application likewise remains an unreviewed corollary candidate.


### Two prescribed triples after CL434 — known corollary,no extra proof queue (2026-10-17;MI317)

Cloud CL434/5ef12b10 independently verified the general arbitrary-sum
three-bin theorem MI295 for sizes>=2. For N>=15,apply it to sizes
(3,3,N-6) and targets(u,v,L(N)-u-v). All SS bounds reduce to
3<=u,v<=3N-6 and15<=u+v<=6N-21. Thus two disjoint triples exist.
This is now a known corollary WITHIN this record,not an external
priority/novelty claim. MI315 retains a direct alternative construction,
status "known consequence,alternate proof unreviewed". Its MI316
registered audit was cancelled before execution when the carrying read
arrived;there is no run or finite validation result to cite.

## SS target exchange geometry — known,reproved here (2026-10-17;MI321)

Frank-Murota,[Decreasing Minimization on M-convex Sets: Background and
Structures](https://arxiv.org/pdf/2007.09616),section2 tight-set discussion
and Claim3.1/proof read. Integer base-polyhedron exchange is standard.
For positive bin sizes c_i,total N,set C_J=sum_{i in J}c_i and
F(J)=U_N(C_J). SS is exactly x(all)=L(N),x(J)<=F(J). Moreover
F(P)+F(Q)-F(P union Q)-F(P intersect Q)=C_(P minus Q)C_(Q minus P)>=0.

Attached specialized proof. Take integer SS points x,y and i with
x_i>y_i. Let T be the union of x-tight sets excluding i,including
the empty set. Tight sets are union/intersection-closed:modularity of
x and submodularity of F force equality. If T contained every
deficit index,x(all minus T)>y(all minus T),so y(T)>x(T)=F(T),
a contradiction. Choose a deficit j outside T. No x-tight set
contains j without i. Hence x-e_i+e_j satisfies every upper bound:
only those sets increase,and their integer slack is at least1.
Its L1 distance to y drops2. Repeat to obtain a unit-transfer path.
This proves target-domain connectivity,not realizability of partitions.
No novelty or carrying-review request.

## Higher Lawrence fibers — scope note (2026-10-17;MI321)

Santos-Sturmfels,[Higher Lawrence configurations](https://arxiv.org/pdf/math/0209326),
v3:introduction/Theorems1,3 and section3 proofs read;section2 examples
inspected. The construction records fixed column sums and fixed
A-weighted row sums. Markov moves connect existing nonnegative tables
in a fiber. For fixed A,the number of participating rows can be
bounded independently of the number of rows. This is not a bound of
two physical tokens or two bins,and changing N changes our base matrix.
It does not establish a desired subset of the fiber is nonempty.
MI321 gives our explicit signed-carrier encoding;no basis computed,
connectivity or zero-error existence imported from this source.


## One-deletion subset spectra: elementary interval consequence (2026-10-17,GPT;MI333)

This is background for an OPEN simultaneous-partition question,not
proposed as a novel theorem or new carrying-read job. The full-interval
subset-sum ingredient is the known result reproved under MI304 above.
The calculation here is a hand derivation,not independently reviewed;
no external source is claimed to contain this exact formulation.

Let P={0,...,M} minus{q},and 2<=r<=M-2. Its r-subset sums fill
the interval between their actual minimum and maximum,except possibly
minimum+1 when q=r,and maximum-1 when q=M-r. Both exclusions occur
if both equalities hold. There are no other holes in that spectrum.
Endpoint deletions q0,M simply leave a full interval.

Derivation:split an r-subset into l=r-k values below q and k above.
Put u=M-q. The feasible k range is max(0,r-q)..min(r,u).
Each fixed k gives an ENTIRE interval [a_k,b_k] by the known
fixed-cardinality spectra on each of the two intervals,where

  a_k=L(l)+k(q+1)+L(k),
  b_k=U_q(l)+k(q+1)+U_u(k),
  L(t)=t(t-1)/2, U_v(t)=t(2v-t-1)/2.

Both endpoints increase strictly with k. At adjacent feasible k,k+1,
l>=1,k<=u-1,and elementary subtraction gives

  a_(k+1)-b_k-1
    =1-(l-1)(q-l)-k(u-k-1).

Both products are nonnegative. Thus any gap contains exactly ONE
integer and requires l=1 OR q=l,and k=0 OR u=k+1. The corner
l1,k0 means r1;the corner q=l,u=k+1 means r=M-1;both are excluded.
The remaining corners are k0,q=r (first gap,minimum+1) and
l1,k=u-1,r=u (last gap,maximum-1). Their adjacent intervals do
not get filled by a farther k because both endpoints increase.
This exhausts the spectrum. Literal hand control:P={0,1,3,4},r2
has sums1,3,4,5,7,both predicted gaps2,6. That spectrum calculation
also holds at size2;SIMULTANEOUS sufficiency does not,as MI331's
P={0,1,2,3,4,6},targets(2,6,8) negative demonstrates.

MI333 uses this calculation to reduce a tight singleton face to a
two-bin completion. It does not assert general three-bin one-hole
sufficiency or full-interval four-bin SS3. No experiment here.


## Three-bin full-interval existence: known in the record,reproved here (2026-10-17 20:30 BST;MI335)

**Known,reproved here:** the EXISTENCE conclusion of MI295,already
independently PROVED by CL434. This alternative construction is an
unreviewed hand derivation,not a newly claimed theorem or a replacement
for MI295's stronger four-adjacent-swap descent bound. Literature
novelty remains unassessed. Filed here under the owner's reproof rule;
no new PROOFS entry or carrying-read job.

Let three sizes a,b,c>=2 total n,with prescribed sums totaling L(n)
and obeying SS. Write alpha(t)=L(t),beta(t)=U_n(t). Among all six
singleton lower/upper slacks choose the least h. Reflect the values
if needed,so its bin A has s_A=L(a)+h. Other bins' upper slacks
are at least h. Conservation gives

  s_B >= L(a+b)-L(a)=L(b)+ab,
  s_C >= L(a+c)-L(a)=L(c)+ac.

For ANY chosen size-a set A of sum s_A,removing a values cannot
make the smallest b remaining values exceed those at ranks a..a+b-1.
Thus these inequalities protect both residual lower bounds;their
complementary upper bounds follow from s_B+s_C=sum(remainder).
This is a rank argument,not an assumption of compatible bins.

Choose A as a prefix of length l,a suffix of length k,and one pivot,
where l+k=a-1. For each k=0,...,a-1,the pivot ranges from l to n-k-1.
The resulting sum intervals meet at their endpoints:the largest pivot
for k produces exactly the set obtained with the smallest pivot for
k+1. Together they cover all s_A in[L(a),U_n(a)]. The remainder is
[l,n-k-1] minus the pivot. After translating by l,it is0..b+c minus
one value r. The MI333 elementary spectrum calculation says that
its b-subset sums can miss only minimum+1 when r=b,or maximum-1
when r=c. In the first case the original B target would be
L(b)+lb+1,contradicting s_B>=L(b)+ab because(a-l)b=(k+1)b>=2.
The second case is the same forbidden minimum+1 for C,excluded by
s_C>=L(c)+ac and c>=2. Therefore a B subset of the required sum
exists,and its complement supplies C. This completes the alternative
existence proof,conditional on the hand calculation's correctness.
The contribution here is a useful global selection representation,
not another announcement of the already established theorem.

## Bounded source-scope check: compatible boundaries in a different group (2026-10-17 20:30 BST;MI335)

The abstract,introduction and Theorem1.1 of
[Prescribed-Difference Matchings with Four and Eight Holes](https://arxiv.org/html/2608.27547)
were read after a bounded source search. Its setting is binary vector
spaces and prescribed pair differences. Its global boundary selection
uses determinant coefficients and finite-field Fourier methods. That
scope supplies no theorem about these integer bin moments;no proof,
finite verification or software was imported or audited. The useful
analogy is to choose a boundary with its completion in mind. No
claim that its character identities transfer to this problem.


### Four-bin equal-sum predecessor versus prescribed targets (2026-10-17 21:43 BST;MI342)

**Known result;scope audit,not a novelty verdict.** Read Kotlar,
[Distance magic labeling in complete 4-partite graphs](https://arxiv.org/html/1410.6916),
arXiv1410.6916v7 (25Aug2015;published2016),Problem1,Observation1.1,
Conjecture1.5 and Theorem1.6. The theorem gives the equal-sum
four-part case for sizes at least2,subject to the stated integer
common sum and sorted-prefix inequalities. Read the preliminary
minimal-deviation lemmas and portions of sections3-4 to check scope;
this is NOT an independent verification of its diagram-based proof.
The exact normalization and comparison with MI339 are derived in
MI342. Our minimum3 condition excludes some cases of this known
theorem;arbitrary prescribed targets give a different extension
within the shared size domain,not an unrestricted strengthening.

Hoory-Kotlar,[2605.06071v2](https://arxiv.org/html/2605.06071v2),
section5 and references,again distinguish known equal-sum results
for at most4 parts from proposed unequal-target generalizations.
This agrees with the earlier MI311 source note;it does not certify
October open status or novelty of MI339. Searches for prescribed
cardinalities AND sums and direct antecedents found no exact
arbitrary-target four-bin theorem in this bounded search. NOT FOUND
here is not absence from the literature. The rejected general-k
sufficiency source2312.00089v1 remains rejected at MI311;no result
from it is imported. The current candidates remain PROOF-SKETCH.


## Adjacent-pair subset-sum completion (2026-10-17 23:55 BST;MI353)

**Known method,reproved here;local application hand/unreviewed.**
Read Károlyi,[Balanced subset sums of dense sets of integers](https://ir.cwi.nl/pub/13654/13654D.pdf),
CWI report PNA-R0801(2008),introduction/Theorems1,3,Corollary4,
and Lemmas6/7 with their proofs (printed pages1-5,not a full
read of the paper). The signed-sum completeness method in
Lemma7 is relevant. The paper's larger density results have
large-size hypotheses;none is invoked as a small-pool theorem.
No novelty claim for the elementary completion method below.

**Finite coin criterion,known,reproved here.** Let e_1,...,e_r
be positive integers with sum(e_i-1)<r. Their subset sums fill
all integers0..sum(e_i). Sort the e_i. The usual interval
induction starts at0 and extends through the next coin e if
e<=1+sum(previous coins). If its first failure occurs after k
coins,then each of the r-k remaining coins is>=k+2. Hence

 sum(e_i-1)>=(r-k)(k+1)=r+k(r-1-k)>=r,

contradiction,including k0. Thus there is no first failure.
This elementary induction is a proof of the finite criterion,
not a new density theorem or an asymptotic estimate.

**Application to a pool with few deletions.** Let z_0<...<z_(n-1)
be an integer interval with at most h values removed. Let
h<r and2r<=n. For every window of2r consecutive AVAILABLE
values,starting at rank j,put

 K_j=sum(z_(j+2i):0<=i<r),
 H_j=sum(z_(j+2i+1):0<=i<r),
 e_i=z_(j+2i+1)-z_(j+2i).

The disjoint pair gaps contain at most h deleted integers,so
sum(e_i-1)<=h<r. Choosing one actual value from each pair
therefore realizes EVERY integer in[K_j,H_j],by the criterion.
Consecutive windows meet EXACTLY:K_(j+1)=H_j. Consequently

 [K_0,H_(n-2r)] is contained in Sigma_r({z_i}).

This is a central interval,NOT a full scalar-spectrum formula.
For n2r,its endpoints sum to the total pool sum and its width
is at least r;any two targets of total sum(z_i) and difference
at most r can thus split into r values each. The more precise
criterion is that one target lies inside the displayed actual
interval. All values are used at most once because the pairs
are disjoint;the complement gives the other bin.

**Interior use and limit.** A legal prefix/suffix/pivot first
bin from an original two-hole pool leaves at most three holes.
If the other sizes b,c>=4 and r=min(b,c),the displayed interval
is a sufficient completion certificate for the smaller-bin target.
It does not prove that such a first-bin recipe always exists,
or that every permitted target lies inside this central interval.
At h=r the paired recipe may fail even while the actual subset
sum exists:MI353 retains a literal example of that distinction.
No PROOFS entry or independent carrying-read request for this
known-method application;generic compatibility remains OPEN.

**Fixed-prefix refinement of the same method (MI353).** Write
r<=t=n-r and h<r. For each k=h+1,...,r,fix the first r-k
available values. Pair sliding windows of2k in the remaining
pool. This certifies an entire interval[A_k,B_k],where

 A_k=sum(z_i:i<r-k)+sum(z_(r-k+2j):j<k),
 B_k=sum(z_i:i<r-k)+sum(z_(n-2k+2j+1):j<k).

The coin excess is at most h<k. Moreover A_k increases with
k,B_k increases with k,and B_k>=A_(k+1):after cancelling the
common low prefix,the k high indices in B_k are t-k ranks
above the corresponding indices in A_(k+1). Thus these
intervals join. Reflect the construction for the upper end;
the two families overlap on the original paired-window band.
They jointly contain every r-sum between A_(h+1) and its
reflected upper counterpart.

Relative to the actual r-minimum,the endpoint A_k increases
by T(k)=k(k-1)/2 from unit rank spacings. Each missing integer
adds at most floor(k/2):count how many selected alternating
ranks versus initial consecutive ranks lie above its gap.
Therefore,with

 D_h=T(h+1)+h*floor((h+1)/2),

all integer sums in[min_r+D_h,max_r-D_h] occur. This is a
known-method hand deduction,not an optimal bound or a full
spectrum catalogue. At h3 it gives D3=12,independent of r,t.
The source's asymptotic density theorem is still not invoked.

If the coarse buffer endpoints cross,the interval assertion is vacuous;
the actual paired-window band remains available in small pools.


### Four-pair endpoint of the same finite coin method (2026-10-18 00:31 BST;MI359)

Status:known finite coin-completeness criterion,reproved here;
the following structured-pool application is a hand deduction,
UNREVIEWED,with no novelty claim. Same primary-source context
and read scope as the adjacent-pair entry above.

For four positive integers of total<=8,the subset sums are
complete unless their sorted list is(2,2,2,2) or(1,1,1,5).
Indeed,at the first failed coin e>1+sum(previous),a failure
after1 or2 accepted coins forces total>=10. A failure after3
forces total>=8,with equality only(1,1,1,5). A failure at
the first coin forces all four>=2,hence exactly(2,2,2,2).
Conversely those two lists visibly fail. This is the same
elementary interval-extension criterion,not a density theorem.

Let an integer interval have<=4 deletions,including an adjacent
pair,but NO four consecutive deletions. In any window of8
available values,pair consecutive ranks. The four pair
differences have total<=8. Four differences2 would consume
all4 missing integers in four disjoint paired gaps,impossible
with adjacent missing integers. A difference5 requires four
consecutive missing integers. Both failures are excluded.
Thus every such four-pair window has a complete coin spectrum.
For k>=5 pairs,the old excess<=4<k criterion applies directly.

The sliding/fixed-prefix construction above can consequently
start at k4 rather than k5. For r,t>=4,apply it to the
smaller size and then complement. With the same rank-gap
endpoint bound,the actual r-subset spectrum contains

 [min_r+14,max_r-14], since T(4)+4*floor(4/2)=14.

This is a sufficient interior band,not a sharp localization
or full spectrum formula. A crossed interval is vacuous;the
actual paired band remains. The adjacent-pair/no-four-run
hypotheses persist under trimming,reflection and taking any
rank window:if an adjacent pair is outside a window,its two
holes cannot contribute to that window's four excess units.
This last formulation does not assume a window itself still
contains the adjacent pair.

### Partition polytopes: source pointer for two-interval sum vectors (GPT,2026-10-18;MI382)

Biao Gao,Frank K. Hwang,Wen-Ching Winnie Li,Uriel G. Rothblum,
*Partition polytopes over 1-dimensional points*,Mathematical Programming
85(1999),335-362,DOI[10.1007/s10107990019a](https://doi.org/10.1007/s10107990019a).
Read scope:the [institutional abstract](https://ir.lib.nycu.edu.tw/items/69d95839-5919-45fd-9a8b-ceb86b8e4c68)
returned in search describes convex hulls of partition-sum vectors,
including inequalities for prescribed cardinalities. Direct item/PDF
opens returned a login page;the paper was NOT read in full. This is
nearby prior art,not evidence that integer points of those hulls are
actual partitions,nor that MI382's two-interval saturation is new.
No theorem from this source is used in MI382. Novelty UNASSESSED.


## Fixed-count interval allocations and convex sums (2026-10-18;MI442)

Known convex geometry,applied here;no novelty claim. Read Fink's primary
author notes [Polymatroid subdivision](https://webspace.maths.qmul.ac.uk/a.fink/matroid_subdivisions_Edmonds2015.pdf),
Theorem1.1,Example1.4 and Corollary2.3:greedy vertices,permutohedra and
Minkowski sums of base polytopes. These are draft notes;the preceding
general Proposition2.2 has a proof placeholder and is not imported.
A second search result for Universal Tutte polynomial could not be opened;
no theorem is adopted from it. MI442 supplies the specialized elementary
support-function argument for fixed bin counts. It identifies a convex
hull,not discrete attainability. MI350/441's impossible integer target is
explicitly the midpoint of two attainable ones with identical counts.
This is consistent with MI321's older target-domain/partition distinction.
No integer-decomposition theorem for physical token assignments is asserted.


### B232 ordered-representative search receipt (GPT,2026-10-18;MI445)

Bounded searches: `"partition" "intervals" "prescribed" "cardinalities" "sums" integers`
and `"distinct representatives" "intervals" "sum" integers`. Search snippets
only;no directly applicable external theorem imported. This is not a
literature-completeness or novelty claim. G323 proves its elementary
ordered-interval interpolation directly and uses previously verified
MI295 for full-interval three-bin completion. Priority remains UNASSESSED.

## Integral rank splitting via discrete separation (GPT, 2026-10-18; MI448)

**Known theorem, applied here; no novelty claim.** Satoru Fujishige,
[Submodularity and Discrete Convexity](https://www.kurims.kyoto-u.ac.jp/~fujishig/nips2.pdf),
workshop slides, 7 December 2012, PDF page 22 (zero-based): “Discrete Separation
Theorem (Frank)” with the integrality clause. Read the parsed theorem and its
adjacent equivalent base formulation, plus the definitions of base polyhedra;
a screenshot request failed, so no visual read is claimed. The theorem supplies
an integer modular separator between an integer supermodular lower function and
integer submodular upper function whenever the former is pointwise below the latter.

For two labelled consecutive intervals and arbitrary fixed bin counts, set
f(J)=U_P(l_J), g(J)=v_J-U_Q(k_J). Total conservation makes f(E)=g(E);
the combined upper group bounds are exactly f>=g. The separator s and v-s
are integer rank-feasible row vectors. Complementation supplies lower cuts.
This is a rank split, not a theorem that either integer vector is a physical
partition. Four counts at least three in each row permit the existing G316
completion; thin counts require additional arguments.

Also read Júlia Pap's author-hosted thesis,
[Integrality, complexity and colourings in polyhedral combinatorics](https://papjuli.github.io/assets/theses/julia_pap_phd_thesis.pdf),
section 1.3, Theorem 1.3.4(ii) on integral g-polymatroid intersections, closure
properties, and bibliography item 23. It attributes generalized polymatroids to
András Frank, *Generalized polymatroids*, Finite and Infinite Sets, volume 37,
pp. 285–294 (1984). The original Frank paper was NOT read. The simpler discrete
separation formulation above is the theorem actually used, avoiding reliance
on Cloud's explicitly memory-qualified intersection formula. The new G324 row
repair has no priority claim; this source search does not assess its novelty.

### Tan–Teh's seven-path exception: pair-count interpretation (GPT, 2026-10-18; MI450)

Read [Tan–Teh, A note on graph burning of path forests, arXiv:2312.10914v3](https://arxiv.org/html/2312.10914v3),
Introduction, Definitions 2.3/2.5, Conjecture 2.7, and Conclusion. The tuple
(45,45,45,45,72,74,74) and its deficient-but-not-impossibly-burnable status are
THEIR known example. MI450 gives a short explanation: singleton minimum counts
sum to 18 of 20, but two large paths would have to share four tokens whose
maximum total is 144, below their required 146 or 148. A nearby literal positive
partition checks the strict inequality. This is a known-result explanation,
not a new deficient forest, a novelty claim, or proof of Conjecture 2.7.
The paper's reported uniqueness is not independently re-enumerated here.

### One size-two row: source scope (GPT, 2026-10-18; MI451–452)

Re-read Hoory–Kotlar [2605.06071v2](https://arxiv.org/html/2605.06071v2),
Introduction and section 5. Its equal-sum four-bin sufficiency does not directly
settle arbitrary prescribed sums with counts (2,b,c,d). No such extension is
imported. MI452's exact N11 diagnostic is finite project evidence only, and the
failed hand counterexample is explicitly withdrawn. No novelty assessment made.


### Pair-sum doorway is a permutation X-ray problem (GPT, 2026-10-18; MI467–470)

The old Nordh section4.1 receipt above already contains the exact six-entry
obstruction rediscovered in CL453. The pair-sum/displacement coordinate
conversion is recorded in MI467, with no novelty claim.
[Bebeacua–Mansour–Postnikov–Severini](https://math.mit.edu/~apost/papers/xray.pdf),
introduction/Proposition2.1 and its small-order table, supply the X-ray
language and counts246,1105,5270.
[Li–Liu–Yao2608.01442v1](https://arxiv.org/html/2608.01442v1),
introduction, section3 and section5 read for orientation: weighted dual
inequalities describe fractional X-rays, while integral realizability is
separate; the binary conjecture is a distinct restriction. The matrix at
section5's first example DOES have another integral realization, so it
cannot be cited as a nonrealizable X-ray. No theorem from these papers is
claimed proved here or used to certify an actual forest. MI469 gives a
literal weighted certificate for its own repeated-target negative.

### X-ray decomposition source check (GPT,2026-10-19; MI480)

Davis–Schroeder, [Relating tournaments and permutations with xrays](https://arxiv.org/html/2606.21532v1),
introduction,Lemmas2.4,3.1–3.2 and selected section4 statements read.
A transitive tournament decomposition supplies a permutation; having only
the score sequence does not provide that decomposition. Lemma2.4 records
the known tight-cut block structure audited in MI478. Section4 distinguishes
proved restrictions from conjectured completeness; none read here resolves
our ordered-target interior. Bounded search: no applicable construction
found, not certified absence. No new theorem imported or review queue.

### L8 publication-status follow-up (GPT,2026-10-19; MI487)

Eleven targeted title,notation,68,author and later-paper queries, in three
batches, found no prior L8 determination. This is NOT FOUND, not a complete
citation-index search or proof of priority. Re-read the primary publisher
text of [Leong–Sim–Teh2025](https://link.springer.com/article/10.1007/s40840-025-01883-9),
Definition2.6 and following paragraph: exact values are listed through L7;
its cited asymptotic statement remains conditional on the conjecture.
Theorem2.4's order condition is below saturated square order for eight paths.
This confirms scope as of that paper, not absence of later work.

The institutional [2026 spider-plus-path abstract](https://scholarprofiles.sunwayuniversity.edu.my/en/publications/burning-disjoint-union-of-spider-and-path/)
concerns that two-component graph class. Its primary DOI10.7151/dmgt.2600
again failed to open here; full text remains unread. Its abstract does not
settle our value, but cannot certify the absence of another statement in
the paper. No author contacted, external publication made, or novelty
status upgraded. G325's mathematical verification is unchanged.

### L8 novelty pass: citation chain and odd-sum partition results (Cloud, 2026-10-19; GC1595's narrowed B)

Scope set by GC1595: later citation chains and genuine odd or prescribed-cardinality extensions, reusing the
Chen–Fu–Wang–Zhou, MI291 and MI487 receipts rather than repeating them.
- *Citation chain.* Semantic Scholar's citation list for arXiv:2312.10914 holds one paper: Leong–Sim–Teh 2025
  (doi 10.1007/s40840-025-01883-9), already read in MI054/MI487 (exact values through L7). OpenAlex was rate-limited
  and not used. Google Scholar, MathSciNet and zbMATH were not consulted.
- *arXiv.* API searches on "path forest(s)" with burning, sorted by date, return nothing on the threshold after
  2312.10914. The only later hit, [2605.14730](https://arxiv.org/abs/2605.14730) (2026, hardness on regular graphs),
  mentions path forests only as a known NP-complete class. [2606.04178](https://arxiv.org/abs/2606.04178) (2026,
  split and {K2+2K1, P4, C4}-free graphs) does not mention path forests.
- *The 2026 spider-plus-path paper.* Its indexed abstract (DMGT, doi 10.7151/dmgt.2600, Leong–Sim–Teh, online August
  2025) treats one spider plus one path, m-burnable for order at most m^2+n-2 with m >= n+3 and exceptions. The full
  text returned HTTP 503 again; unread.
- *Odd-number partition results.* Tan–Teh's own pointer list (their section 2) names Ando–Gervacio–Kano 1990,
  Chen–Fu–Wang–Zhou 2005, Enomoto–Kano 1995, Fu–Hu 1994, Lladó–Moragas 2012 and Ma–Zhou–Zhou 1994. The two odd-number
  papers concern a COMMON sum: Fu–Hu (Discrete Math. 128, 143–150) characterizes when {1, 3, ..., 2n-1} splits into
  k subsets with a common odd sum (indexed abstract read); Enomoto–Kano (Discrete Math. 137, 189–193) the common even
  sum (title only). Both full texts failed again (author host: proxy 502; institutional host: TLS verification
  failure, not bypassed). arXiv searches for prescribed-sum partitions of odd integers and for "sumset partition"
  found only 2312.10914 itself and the already rejected 2312.00089.
**Result:** NOT FOUND, as in MI487: no later determination of L8 and no odd-number unequal-prescribed-sum theorem.
This is a bounded search with the access limits above, not certified absence or a priority claim.

### Exact two-size2 obstruction versus the equal-sum slice (GPT, 2026-10-20; MI515–516)

**Scope comparison only; no novelty verdict or new theorem status.** Re-read
Kotlar, [1410.6916v7](https://arxiv.org/html/1410.6916v7), Problem1,
Observation1.1, Conjecture1.5 and Theorem1.6. The theorem characterizes
COMMON-sum four-part partitions on1,...,N with minimum size2, using the
integer common sum and its sorted-prefix conditions. This refreshes MI342;
it is not a new independent audit of that paper's proof.

For fixed cardinalities c_i, translating0..N-1 to1..N changes targets by
u_i=s_i+c_i. Then u_J-T_(C_J)=s_J-L(C_J): ALL group cut slacks are unchanged.
The unreviewed section11 counterfamily becomes

    (T_a+1, 2a+4, 2a+6, T_c+(a+4)c-1), counts(a,2,2,c).

For common target K and sizes sorted increasingly, let P_j be the sum of
the j smallest sizes. Every j-bin group has size C_J>=P_j. Its one-based
upper bound is jK<=Uplus_N(C_J), where Uplus_N(r)=r(2N-r+1)/2 increases
with r. Thus the sorted-prefix upper inequalities jK<=Uplus_N(P_j) imply
ALL group upper inequalities; conservation gives all lower inequalities.
Conversely they are among the group bounds. Hence the common-sum slice
uses exactly the known source's conditions, not a stronger hidden screen.

The counterfamily's two size2 targets differ by2 under any common translation;
full value reflection reverses the sign. Hence this obstruction cannot
belong to the common-sum slice. F(3,3) becomes(7,10,12,26) on1..10,
with total55. This explains compatibility with Kotlar in the shared count
class; our candidate does not cover all the size2 multiplicities of his theorem.

Re-read Hoory–Kotlar, [2605.06071v2](https://arxiv.org/html/2605.06071v2),
Introduction and section5, especially its final direction: unequal prescribed
part sums are distinguished from the equal-sum problem, and the cited
prescribed-sums result leaves part sizes undetermined. This is a scope
statement in that version, not certification of October open status.
Two bounded search batches (five queries, three restricted to arXiv) found
no applicable primary-source exact arbitrary-target two-size2 classification.
The unrestricted searches returned mostly irrelevant material; none is
used as evidence. No citation-index audit or proof of absence is claimed.
G327/G328 and the composed parent remain unreviewed; novelty UNASSESSED.

### Equal-pair consumption as a known ingredient (GPT, 2026-10-20; MI519–520)

Read [Hoory–Kotlar2605.06071v2](https://arxiv.org/html/2605.06071v2),
Proposition2.7, Examples2.8/9 and Theorem2.11 with its proof. Equal-sum
pairs consuming a prescribed part of the token pool, followed by a capacity
bound for remaining bins, is already an explicit method there. Our fixed-sum
fibre being a matching and its elementary count are not claimed new.
FOUR-BIN-PARTITIONS section12 applies that ingredient to a one-hole pool
with r equal-target pair bins and ONE filler of possibly different target.
Its exact endpoint characterization is an unreviewed hand specialization,
not adopted from those statements and not labelled novel. Two narrow arXiv
queries yielded no exact counterpart; this is not a priority search.

### Two-colour pair quotas and Exact Matching (GPT, 2026-10-20; MI521–522)

Read Aprile–Di Summa, [The red-blue-yellow matching problem,
2603.18754v1](https://arxiv.org/html/2603.18754v1), Introduction and
Section2 (Theorems6/7 and their path/cycle argument, Remark8, Observation10).
Prescribed red/blue edge counts are an established matching framework.
Their general graphs allow cycles; the numerical distinct-sum fibres in
FOUR-BIN-PARTITIONS section13 exclude cycles by adding the token labels.
No source theorem is imported for that hand observation, its quota
countercontrol, or its direct weighted certificate. No algorithmic or
novelty claim is made.

Deza–Gerard–Ma–Pokutta, [Bounded-Support Additive Latin Transversals,
2607.11241v2](https://arxiv.org/abs/2607.11241): ABSTRACT ONLY read,
which identifies a prescribed edge-colour-count matching formulation.
No theorem/proof audit or transfer to our ordinary-integer partition
problem. Other search hits are not treated as read sources.

MI523–524: re-read Theorem6 and Observation10 of the same Aprile–Di Summa
source. The prefix-red/remaining-blue construction is already present;
section14 specializes it to alternating paths and derives a sorted
full-component quota formula. Known elementary ingredients, exact formula
hand/unreviewed here, no originality or general-graph algorithm claim.
The source's approximate arbitrary-colouring guarantee is not used as
an exact theorem for our setting.

### Two reflections and interval path coordinates (GPT, 2026-10-20; MI525–526)

Read the real-line reflection example on page11 of Michael Davis's
[2006 Coxeter-group talk](https://people.math.osu.edu/davis.12/talks/uwt-talk.pdf).
The two-reflection/translation action is known; section15's interval and
deleted-token readout is an elementary hand specialization, unreviewed
and not claimed original. The Utah course-solutions PDF timed out on
full fetch; only its indexed Question7 excerpt was available.

Karnauhova–Liebscher,[1504.03099](https://arxiv.org/abs/1504.03099),
ABSTRACT ONLY read: related bi-rainbow meander component counting, no
theorem or equivalence imported. Fernau–Gajjar2301.02178 indexed abstract
uses another sum-graph definition. Neither is treated as an exact source
for these fixed-target numerical fibres. No broader literature or novelty
conclusion follows from these orientation searches.

MI527–528: re-read Hoory–Kotlar2605.06071v2 Proposition2.7 and its
pair-consumption example. That is a common-target/full-pool setting,
not an imported adjacent-target one-hole theorem. Two narrow arXiv
queries for prescribed-sum pair partitions/consecutive integers and
unequal pair sums returned no result. G329's exact protected adjacent
classification is a hand candidate, novelty UNASSESSED; the empty
search is not a priority claim. Standard path/reflection ingredients
are rederived in its self-contained proof.


### Two-target quota hulls and known polygon edge merging (2026-10-20; MI532–533)

Primary source read: [CGAL5.3, 2D Minkowski Sums User Manual, Computing the
Minkowski Sum of Two Polygons](https://doc.cgal.org/5.3/Minkowski_sum_2/index.html),
which explains convex boundary construction by merging angle-ordered edges.
That machinery is known; we do not attribute an exact matching theorem
or lattice decomposition corollary to the manual. G330/FOUR-BIN-PARTITIONS
section18 supplies the proposed integer vertical-rounding argument and
its two-target matching specialization, self-contained and unreviewed.
No originality claim. Bounded searches did not locate the exact forest
statement; this is NOT FOUND in those searches, not a priority verdict.

Re-read [Aprile–Di Summa2603.18754v1, section2 Observation10](https://arxiv.org/html/2603.18754v1):
their alternating red/blue CYCLE construction loses one edge. It does not
supply our exact-forest integer-hull statement. The fixed C4 control has
a genuine integer hole, preserving the scope distinction. The SIAM2023
exact bipartite matching polytope abstract was read only for orientation;
no theorem from its unread proof is used. Geometric vertex-colouring
search hits and two unrelated arXiv pages are not imported.

### Mixed decomposition is stronger than the source's repeated-polytope IDP (2026-10-20; MI534)

[Haase, Nill, Paffenholz and Santos, Lattice points in Minkowski sums,
Electronic Journal of Combinatorics15(2008),N11](https://www.combinatorics.org/ojs/index.php/eljc/article/download/886/pdf/0),
full five-page text read. Theorem1.1 gives lattice-point addition
surjectivity when one polygon's normal fan coarsens the other's; the
smoothness assumption of the earlier result is removed. Its proof uses
lattice-free intersections and the fan condition, not downward closure.
This directly covers identical/homothetic component triangles, but does
not automatically cover our mixed odd paths. Already RBR and RBRBRBR
have triangles with intercepts(2,1),(4,3), non-axis normals(1,2),(3,4).
Their three-ray fans differ and neither coarsens the other. This scope
check is not a novelty claim or a counterexample to their theorem.

[Mori, Motomura, Ohsugi and Tsuchiya, Algebraic aspects of unconditional
lattice polytopes,2605.19586v1](https://arxiv.org/html/2605.19586v1),
introduction and section2 through Theorem2.2/proof read; later algebra
not imported. Their anti-blocking definition is the downward-closed
property used in G330. IDP concerns repeated copies tP of ONE polytope.
Theorems1.1/2.2 compare normality with reflected pieces; they do not state
the mixed P_1+...+P_m lattice-addition assertion we need. The terminology
is useful, but neither result is a replacement premise for G330's18.2.
Bounded search only: exact matching specialization/anti-blocking mixed
plane statement still NOT FOUND here; originality remains UNASSESSED.

### Three perfect colour matchings are not three distinct sum fibres (2026-10-20; MI535–536)

[Boyadzhiyska, Christoph and Szabo, Almost-perfect colorful matchings in
three-edge-colored bipartite graphs,2504.15167v2](https://arxiv.org/html/2504.15167v2),
introduction, Theorem1.2 and setup read, proof not imported. The theorem
assumes three disjoint PERFECT colour matchings on the same bipartite
vertex set, and supplies quotas totalling n-1. Those assumptions do not
hold for distinct real-token pair sums: a perfect sum-u matching on2n
tokens forces the total nu; two different perfect sum fibres would force
u=v. This is a direct conservation scope check, not an objection to the
source theorem. No absence, originality or new general matching result.

Re-opened Li–Liu–Yao2608.01442v1 for X-ray terminology/orientation only;
its binary restriction and degree relaxations are not substituted for
our ACTUAL integral-matching quota hull. Broad searches and the existing
record did not locate the exact three-sum no-hole question; no universal
inference from that search or from the fixed8 arithmetic-progression
fixtures/963 quota checks at MI536. No larger domain tested.

### AP sum graphs and known perfect-matching switches (2026-10-20; MI537–538)

[Dyer, Jerrum and Muller, On the switch Markov chain for perfect
matchings,1501.07725v3](https://arxiv.org/html/1501.07725v3), section2
Lemma2/proof and the monotone-graph definitions read. Switch connectivity
on chordal bipartite graphs is known; monotone graphs are a subclass.
[Dyer and Muller, Counting perfect matchings and the switch chain,
1705.05790v2](https://arxiv.org/html/1705.05790v2), section2 Theorem1's
odd-chord argument, section3.1 definitions/Lemmas5–7 and section3.2's
scope read. Quasimonotone means every bipartition cut is monotone;
the whole graph need not be bipartite. No rapid-mixing proof, counting
algorithm or recognition theorem imported. The later1801.06494v2 was
opened for orientation only, not used as a carrying source.

FOUR-BIN-PARTITIONS section19 specializes this known switch mechanism
with a direct adjacent-inversion proof on each alternating-cycle cut.
For AP targets u-d,u,u+d, cross sums on that cut are congruent to u
mod d, so the interval bounds suffice for each switch. The resulting
perfect-quota interval on the primitive(1,-2,1) line is an elementary
hand corollary here, unreviewed; no originality claim/new PROOFS filing.
It does not prove partial-quota hull integrality across covered sets.

### Remaining four-bin count classes: source scope (2026-10-20; MI544)

Re-read [Kotlar1410.6916v7](https://arxiv.org/html/1410.6916v7), Problem1,
Observation1.1, Conjecture1.5/Theorem1.6. It covers COMMON part sums,
including three/four size2 bins; it does not supply our arbitrary-target
classification. Re-read [Hoory–Kotlar2605.06071v2](https://arxiv.org/html/2605.06071v2),
section5 in full: its final direction distinguishes prescribed unequal
sums, and the cited prescribed-sum result leaves part sizes undetermined.
This is the exact source-version scope, not certified current openness.

Refreshed [Nordh, Perfect Skolem sets](https://gustavnordh.com/perfskolfinal.pdf),
the involution paragraph and section4.1 Definition14, Theorem15/proof,
Corollary17 and its repeated-displacement counterexample. These concern
prescribed DIFFERENCES/permutation displacements. Necessary density
conditions are not a sufficient theorem for repeated displacements.

For pair SUMS on0..N-1, the elementary encoding uses a fixed-point-free
involution pi and reversal R(x)=N-1-x. Setting rho=R composed with pi
gives rho(x)-x=N-1-s for EACH endpoint of a sum-s pair. Conversely one
must retain (R composed with rho)^2=id and rho(x)!=R(x) to recover a
pairing. A theorem about arbitrary displacement permutations does not
by itself impose these constraints. No claim that this logical scope
gap has been shown strict here; no Skolem result is imported to solve it.
Bounded searches found no applicable exact(2,2,2,c) arbitrary-sum theorem;
novelty and broader literature status remain UNASSESSED.

### Minimum-mean zero ownership for the missing1 child (2026-10-20; MI549)

The direct source-scope check remains narrow: [Kotlar1410.6916v7](https://arxiv.org/html/1410.6916v7)
introduction/Problem1/Theorem1.6 was reread; its stated partition problem has
common sums on a full interval. The earlier Hoory–Kotlar section5 scope
audit is MI544. Those statements do not directly supply the arbitrary-target
protected four-bin pool[0,M] minus1. Two broad searches for prescribed sums,
consecutive integers/holes and Kotlar/nonconsecutive partitions produced no
applicable primary theorem; unrelated and secondary hits were not used.
No literature absence or originality claim follows. Existing project G317
already uses zero ownership in a different two-hole THREE-bin problem.
MI549's contribution is a short minimum-target-per-token selector feeding
PROVED G327, with its all-group cut proof written directly. Novelty remains
UNASSESSED; no external theorem is asserted for the selector.

### Joint count/moment selection: bounded source audit (2026-10-20; MI553)

[Hwang–Onn–Rothblum, A Polynomial Time Algorithm for Shaped Partition Problems](https://epubs.siam.org/doi/abs/10.1137/S1052623497344002),
SIAM J. Optimization10(1999): read the official ABSTRACT, not the full paper.
Its task maximizes a convex function of part-sum vectors under shape constraints,
with fixed criterion dimension and part count. Exact attainment of prescribed
sums is a different task: minimizing a convex distance to the desired vector
(or maximizing its negative) does not match that objective assumption. The
failed convex-hull shortcut in MI442 therefore remains a relevant guard. No
integer-attainment theorem is imported.

[Hemmecke–Onn–Romanchuk, N-fold integer programming in cubic time](https://arxiv.org/pdf/1101.3267),
arXiv1101.3267v1: read introduction, definitions2.1–2.2, Lemmas3.7–3.8,
Theorem3.9 and section6/Theorem6.1 statement with its parameter discussion;
not the whole paper or an independent proof verification. The repeated fixed
bimatrix is a hypothesis. The variable-entry result still fixes block dimensions
and retains coefficient dependence. Its feasibility procedure may also return
infeasible; it does not make the protected inequalities sufficient.

For the natural per-token assignment encoding here, the count/sum blocks have
coefficients[1;x], varying with token x. No reduction to the required uniform
fixed block with controlled parameters has been supplied. The general Graver
view is useful algorithmic context, not a bounded repair theorem for this
family. No implementation or run is proposed from it.

The record search found26 hits/10 files for n.fold|multiobjective|
cardinality.constrain|prescribed.cardinalit with partition|sum|moment. Relevant
MI382/442/448 and existing prior-art scope were read; unrelated hits were not.
Two search batches (six queries) found no applicable count-selection theorem
in the sources actually inspected; this is a bounded negative search, not an
absence or novelty claim. A fresh Gao et al. PDF open again returned a DSpace
page, so no new full-paper read is claimed. Primary sources only were used.

### Four-variable count bounds and integer parity (2026-10-20; MI555)

Two bounded searches concerned four-variable subset-sum interval vertices,
parity and octagonal/UTVPI constraints. Read [Bagnara–Hill–Zaffanella,
An Improved Tight Closure Algorithm for Integer Octagonal Constraints](https://arxiv.org/pdf/0705.4618),
abstract/introduction, PDF pages1–2, and the constraint definition opening
section3; not the algorithm's proof. Their inequalities involve at most
two variables, with coefficients in{-1,0,1}; integer closure differs from
rational closure. This is relevant background, not the theorem used here.
Our conserved four-variable total is an extra condition; eliminating one
variable leaves a three-variable singleton-complement slab. No reduction
to that paper's precise hypothesis or import of its algorithm is claimed.
Cloud CL472 supplied the pair-box/parity coordinates. MI555–556 audit a
short elementary four-variable consequence directly, not an originality
claim, a general integer-programming theorem or a protected-parent proof.

### Real count projection by interval elimination (2026-10-20; MI557–558)

Read the Fourier–Motzkin projection statements and integrality caveat
in [UT Austin CS395T lecture8](https://www.cs.utexas.edu/~pingali/CS395T/2006fa/lectures/lecture8.pdf),
PDF pages10–15 (zero-based9–14); not the whole lecture. Pairing lower
and upper bounds eliminates a real variable; arbitrary projection does
not preserve integer feasibility automatically. MI558 derives its special
interval formulas directly. This is known elimination, not a new theorem
filed for review. A Stanford lecture open timed out, no read claimed.
The bounded prescribed-cardinality/two-interval search supplied no
applicable count-budget theorem in the inspected primary results.
MI557's direct algebra uses the project's scalar lemma and actual rank
inequalities; priority remains unassessed.

### Balanced collections and the real count selector (2026-10-20; MI560)

Known linear-programming/game-core criterion; no new proof entry.
Read [Laplace Mermoud–Popoli, Combinatorics on Social Configurations](https://arxiv.org/html/2406.16409v1),
section1: core definition, balanced weights and Theorem1. Its background
states the Bondareva–Shapley criterion. Also read the original-author
institutional [Shapley, On Balanced Sets and Cores, RAND RM4601(1965)](https://www.rand.org/pubs/research_memoranda/RM4601.html)
summary; its linked27-page scanned PDF was located, but text extraction
and screenshot tools supplied no readable pages here, so no full-paper
or original-proof read is claimed. Wiley's1967 PDF request redirected to
metadata. No theorem is adopted from search snippets or secondary pages.

For complement-symmetric count bounds, the real region is
sum k=H, k(J)<=U_J for all proper J. Maximize sum k under just those
upper bounds. It is feasible (take all coordinates sufficiently negative)
and bounded by singleton bounds. Standard LP duality gives the minimum
of sum lambda_J*U_J over lambda>=0 with each label's incident weights
summing1. An upper-feasible vector of total>=H can be decreased uniformly
to total H while preserving every upper bound; complementary upper
bounds then give every lower bound. Thus real feasibility is equivalent
to sum lambda_J*U_J>=H for EVERY balanced collection. This is the
upper-bound version of the known core theorem, rederived by standard
duality for scope, not a new discovery. It does not prove that the
actual moment-root endpoint function meets that criterion.

MI560's34/124/13/2 collection has weights1/2 on each group. Its
inequality is precisely the earlier crossing comparison. The groups
overlap: treating their twofold cover as disjoint token ownership
would lose the very constraint under investigation. No balanced-family
enumeration, new solver, real-selector existence or integer/physical
completion theorem is asserted from this source read.

### Convex knapsack extrema with the integer budget retained (2026-10-20; MI564)

Known convex-maximization geometry, specialized/rederived here; no
new proof-table entry or carrying review request. Primary search found
[Levi–Perakis–Romero, A continuous knapsack problem with separable convex utilities](https://doi.org/10.1016/j.orl.2014.06.007),
Operations Research Letters42(2014),367–373. The primary publisher search
result supplied the abstract/introduction and the author-hosted indexed
PDF supplied the opening of section2: convex utilities, box constraints,
a single sum budget, and the extreme-point setup. Direct publisher opens
returned403 and the author-PDF open404; no complete-paper read, exact
algorithm import or claim about its approximation results. The elementary
argument below is self-contained. This background is known, not a new
mathematical discovery or a theorem of protected count admission.

For MI562's four scalar ceilings, let a_i be the first admitted budget
and b_i the first plateau. On integers[a_i,b_i-1] the ceiling F_i is a
convex quadratic; on[b_i,cap_i] it is the constant protected upper.
To maximize sum F_i(r_i) under integer sum r_i<=R, first replace any
r_i>b_i by b_i. The cost is unchanged and the budget only decreases.
Split each remaining row into its preplateau interval or its single
plateau point. On each such box, the objective is convex. If two counts
are interior, vary them oppositely to the two ends of the legal segment.
Convexity gives an end with cost at least the initial cost, and an end
hits a box boundary. Segment endpoints are integers. Repeat. If the
budget is slack and one count remains interior, vary that count between
its lower bound and the smaller of its upper bound and the remaining
budget. Again a convex endpoint is no worse and is integer. Thus there
is a maximizer with every count in{a_i,b_i-1,b_i}, apart from at most
one count fixed by the TIGHT total budget. Empty preplateau intervals
and repeated endpoints are removed. No assertion about a fractional
mixture's expected cost is used.

Consequently the exact maximum occurs among at most3^4=81 endpoint
tuples and4*3^3=108 residual tuples. A residual tuple has three endpoint
counts and its fourth equal to R minus their sum; discard illegal or
over-budget tuples. If no tuple is feasible, neither is the original
allocation problem. In particular do NOT require budget equality when
all rows have plateaued below it. This is a constant-size SYMBOLIC
reduction for four rows, not a certificate that any of its189 costs
is below2S. Arbitrary n-row knapsack complexity is not being changed.

For the MI563 endpoint-mixture control, the average second size110
count is44. The actual scalar ceiling there is f110(45)-1=8064, whereas
the mixture's average ceiling is1013420/99. Thus the integer tuple
(10,110,44,55) costs47355<48400, despite the mixture's cost>48400.
That is ONE point, not the maximum over the189 candidates. It illustrates
exactly why the common-price relaxation and the discrete question differ.
The lost-plateau check F(0)=0,F(1)=1,F(2)=100 at budget1 requires b-1=1;
using only the first and plateau endpoints would miss the optimum.

### Largest-remainder count rounding (2026-10-20; MI569–570)

Known rounding ingredient, specialized here; no originality claim.
Read [Cont–Heidari, Optimal rounding under integer constraints, v1](https://arxiv.org/html/1501.00014v1),
section3's procedure through its largest-remainder comparison. Floor each
coordinate, then raise the required number with largest fractional parts.
No general objective-function proposition or complexity result is needed.
The four-coordinate discrepancy bound below is rederived directly.
The dependent-rounding primary paper was located/opened as background;
its randomization/correlation theorems are NOT used or claimed read.
Fujishige's integer separation statement, nips2 PDF page22, was re-read
for the physical composition already recorded at MI448; no broader
intersection theorem is substituted.

Let four real x_i have integer sum H, fractional parts a_i, and s=sum a_i
in{0,1,2,3}. Round up the s largest fractions. The total positive error
is E=s-sum_(largest s)a_i<=s-s^2/4<=1 (s0 gives E0). Since total error
is zero, EVERY subset error has absolute value<=E<=1. Coordinates remain
in their individual floor/ceiling pairs. Ties do not affect this bound.
Four half-integers attain E1; five fractions2/5 instead give E6/5, so
there is no automatic five-variable version with the same constant.
This is a standard rounding consequence, not a new proof-table entry.
The new punctured-pool APPLICATION and its unreviewed scope are in FOUR27.


### Fractional count projection versus inward rounding (2026-10-20; MI571)

Known rank/support-function geometry, specialized here; no new proof-table
entry or originality claim. Hoory–Kotlar2605.06071v2 definitions3.1–3.4,
majorization comment and Theorem3.6 statement re-read: fluid mixing has
real token shares. Postnikov's [primary paper](https://math.mit.edu/~apost/papers/permutohedron_full.pdf),
Prop14.12/proof and Remark14.13 read: the vertex-decomposition statement
uses sums of UNIT coordinate simplices. It does not establish physical
assignments with prescribed weighted sums/cardinalities; full mixed-
subdivision theory not audited. The previous broad search supplied no
applicable bridge, not a literature-absence claim.

For a row of length n, define A(a) as the linear interpolation of
L(j)=j(j-1)/2 at integer j, and V_n(a)=a(n-1)-A(a). Greedy filling
in any ordered bin-weight direction proves that fractional row moments
with prescribed REAL counts have upper group rank V_n(a_J). The two
row support functions add in the SAME order, so the combined group
bounds describe their Minkowski sum, exactly as MI442 with real counts.
Thus at fixed targets the exact fractional count projection Q has
0<=k_i<=c_i, total H and, for every proper group of integer size c
and real high count r,

    A(c-r)+(q+1)r+A(r) <= t_J,
    t_J <= (c-r)(q-1)-A(c-r)+Mr-A(r).

Writing theta=r-floor(r), A(r)=L(r)+theta(1-theta)/2, with L now the
quadratic extension. Since c is integer the two corrections add, giving
f_c(r)+theta(1-theta) and g_c(r)-theta(1-theta). This corrects a raw
quadratic relaxation by at most1/4 on EACH side. Ordinary punctured-pool
rank cuts imply fractional assignment by the familiar greedy support
argument; parent protection dominates those rank cuts, so Q is nonempty.
No physical integer assignment follows from this convex statement.

Each scalar interval I_J in Q contains exactly the same INTEGER points
as its ordinary moment test f<=t<=g. Therefore the rounded count region
P is obtained by replacing EVERY I_J with[ceil inf I_J,floor sup I_J]
(and is empty if an inward interval is empty). The unresolved parent
step is simultaneous feasibility AFTER those replacements. MI571's
literal fractional witness for the old size2 real-empty control shows
why fractional feasibility alone does not answer it. Its failed parent
protection cut is retained; no min3 protected counterexample is claimed.


### Four-label balanced collections: the grand-coalition convention (MI576–577, 2026-10-20)

Read [Laplace Mermoud, Grabisch and Sudhoelter2507.05898v1](https://arxiv.org/html/2507.05898v1),
section2.3 definitions/unique-weight characterization, the four-label
1/3,1/3,1/3,2/3 example, and Table2 (42 for n4). Whole algorithm/proofs
not audited. Cloud's41 counts ONLY proper coalitions; adding{V} yields
that known42. Its unique balancing weight is1, and no larger collection
containing V is minimal. Constant four-label incidence enumeration was
checked separately, no target domains or larger-n enumeration. The
finite9-type application and corrected weights are in FOUR29. The
balanced-core theorem itself was already sourced at MI560. Nothing
here asserts the protected moment endpoints satisfy the remaining rows.


### Grouped tournament scores and a bounded-support candidate (MI584, 2026-10-21)

Read Kolesnik and Sanchez, [The geometry of random tournaments](https://arxiv.org/html/2009.09322),
introduction and statements of Theorems1/3/4, Theorem5/Corollary6 and the
graphic-zonotope discussion; not the entire subdivision proof. The
known generalized Landau theorem characterizes integral orientation
scores by subset edge-count cuts and total conservation, including
multigraphs. It does not guarantee an acyclic orientation. G335 step1
also supplies a direct integral-flow proof for our grouped application.
Path reversal and the cyclic-triangle score identity are elementary
orientation tools, not novelty claims. The proposed bound using our
full-interval partition theorems is recorded separately as a HAND
candidate; its novelty is unassessed.

A secondary possible route was read in Parrilo's
[Sum of Squares Programs and Polynomial Inequalities](https://ocw.mit.edu/courses/6-972-algebraic-techniques-and-semidefinite-optimization-spring-2006/63d6e45650205ceef6701971a9b4621c_lecture_22.pdf):
introduction, Gram-matrix Theorem1 and certificate definitions in section3.
This is a framework for polynomial certificates, not evidence that our
crossing inequalities have low-degree certificates. No SOS computation
or parameter elimination was run; legality-pinned moment endpoints
still need separate treatment. The tournament argument is the chosen
bounded hand investigation, rather than an expanded endpoint catalogue.

### Unit rank-gate reuse for tournament absorption (MI586–587, 2026-10-21)

MI292 already gave the tight-prefix reachability argument and the
shared-token obstruction. G336 specializes that known gate to a unit
target shift in ONE full ordered run and explicitly uses PROVED G316
to lift it to a physical partition. No claim that graph edges can be
executed together is made. Reread Fink's primary draft notes
[Polymatroid subdivision](https://webspace.maths.qmul.ac.uk/a.fink/matroid_subdivisions_Edmonds2015.pdf),
introduction, Theorem1.1 and Example1.4 for known rank-cut/permutohedron
context. The proof placeholder in Proposition2.2 is still not imported;
no mixed integer-decomposition theorem is needed. The proposed star-
triangle application is separate, HAND/unreviewed, novelty unassessed.

### Quantitative small-slack chain in one full interval (MI588–589, 2026-10-21)

G324 step4 already uses strict submodularity to make tight colour cuts
comparable. G337 quantitatively specializes that same exact interval
rank identity: four row counts>=3 separate incomparable lower slacks
by9, making all slacks<=4 a chain. Known rank/cut geometry is not a
novelty claim. The proposed bounded-defect application to G335's
rainbow components, fixed-* score ordering and absorption is separately
HAND/unreviewed. Its physical lift is PROVED G316; no integer-point
conclusion is taken merely from Fink's general base-polytope source.

### Colour potentials for a tournament's linearized objective (MI592, 2026-10-21)

Read MIT6.854 [Min-Cost Flow notes](https://courses.csail.mit.edu/6.854/16/Notes/n10-mincostflow.html),
sections "Deciding optimality" and "Prices and Reduced Costs", including
the zero-source shortest-path construction. The known theorem equates
nonnegative residual cycle costs with a feasible potential. MI592 applies
it to the reversed five-colour orientation graph after linearizing Phi
at a GLOBAL maximum. This is known optimization machinery, not a novelty
claim. Its price certificate alone does not certify the quadratic
maximum: the protected NONmaximum in MI590 already admits zero prices.
The separate exact reversal formula includes the squared vertex changes;
no parent absorption theorem or sufficiency of simple circuit tests is
imported from the source.

### Paired component paths and the six-vertex refinement (MI593, 2026-10-21)

Read Bang-Jensen and Gutin, [Paths, Trees and Cycles in Tournaments](https://www.cs.rhul.ac.uk/~gutin/paperstsp/t1.pdf),
section2 through Proposition2.1, for path/strong-component definitions
and the known total ordering of tournament components. Our convention
uses arrows from winner to loser. The basic path reversal identity is
already in PROVED G335. G338 pairs opposite paths in DIFFERENT components,
then uses the four-colour palette count. Two bounded searches returned
mostly arc-coloured rainbow-path results; none was imported as a result
about fixed vertex-class totals. No exact predecessor was identified in
that bounded read; novelty remains UNASSESSED. The argument is fully
written as a HAND candidate, not attributed to the survey.

### Strongness under a score permutation (MI594, 2026-10-21)

The known Landau subset-score inequalities and their necessity were
reopened in Kolesnik–Sanchez Theorem1. A strong tournament has every
proper minimum k-score sum strictly above L(k); a bottom component of
a nonstrong tournament attains equality. Hence strongness is determined
by the internal score multiset. CL477's instrument already records the
tight-prefix/component correspondence. MI594 rederives this corollary
for a neutral score permutation, not as a new result. The separate
coupled core/run closure and full-palette application remain WORKING
HAND/unreviewed; no theorem from the source certifies that application.


### Bounded rank excess and a forced filler tail (2026-10-21, MI598)

Stanley, [Topics in Algebraic Combinatorics](https://math.mit.edu/~rstan/algcomb/algcomb.pdf),
Chapter6: rectangle partitions and Young diagrams, Proposition6.3's
boundary-word bijection and Theorem6.6's rank generating polynomial
were read. This is the known geometry of subsets displaced from an
initial segment, not a theorem about prescribed sums on punctured pools.
The project's MI354–355 already uses physical excess>=rank excess
to confine near-extremal subsets. MI598 applies that same elementary
inequality to the UNION of two bins: filler deficit<=D forces all
values after the first K+D available ranks into the filler. This
gives an exact joint-partition reduction in that stated stratum.
It is known machinery, rederived here; no novelty or new proof number.
No source theorem or argument establishes scalar-spectrum inheritance,
the global localization of all A2 failures, or the protected parent.


### First-bin binary fibres versus positive-marginal logistic fibres (2026-10-21; MI602)

Read Hara–Takemura–Yoshida,
[On Connectivity of Fibers with Positive Marginals in Multiple Logistic Regression](https://www.keisu.t.u-tokyo.ac.jp/data/2008/METR08-39.pdf),
Section2 including Proposition2, Lemma1 and Theorem1 with proofs.
The result gives equal-sum exchanges on equally spaced covariate
levels when every column marginal is positive. For a full interval,
encoding a subset and its complement as a binary two-row table has
column margins1 and fixed first-row count/moment, so the theorem
applies. On a two-hole interval the missing columns have margin0.
Deleting them destroys the equally spaced design; keeping them
violates positivity. Thus no two-hole connectivity is imported.
The first-bin fibre is already nonempty by scalar feasibility,
but its connectivity alone would not prove residual coverage.

Also read Rapallo–Yoshida,
[Markov bases and subbases for bounded contingency tables](https://arxiv.org/html/0905.4841v2),
abstract and Theorem3 only. Its ordinary-margin setting does not
include our additional weighted row sum. No such transfer is made.
No basis computation or experiment; known context, not a new proof.


### Endpoint-anchored pair covers for a deletion budget (2026-10-21; MI610)

Known ingredients: a fixed pair-sum fibre is a matching, so D deletions
cannot block D+1 disjoint pairs; fixed low/high values reduce a
cardinality-constrained sum to three free values. These are already
used in G326 and G318. G341's particular linear bound, two low-target
inductions and large-span/count gates are a new HAND application here,
not attributed as a known theorem and with novelty UNASSESSED.
Bounded arXiv searches for restricted-sumset dense intervals/deletions
and cardinality-constrained subset sums with deletions returned no
results; this is a search limitation, not evidence of novelty or an
absence theorem. The Károlyi signed-sum source previously read at MI353
is context only; no asymptotic density theorem is imported. G341 does
not rely on G340 or the old three-hole finite-basis reduction.

### rStation Collatz papers, read as prior art only (2026-10-21, Cloud; CL485)

**Source and scope.** rStation (rstation.ai, run by Dualverse AI) is a public community where AI agents post problems,
discussion and papers reviewed by other agents. At the owner's instruction (2026-10-21 ~23:40 BST) it is used here as
prior art only: read through its public read-only API, with no account, posting or voting. Its "accepted" standing is
community review by other agents, not external peer review. Read: the abstract list of all 16 Collatz papers, and the
statements, §1 and §2 (prior methods) of collatz_16. Not read: any proof in full, the supplements, or the other papers
beyond their abstracts. Nothing below is verified by us.

**collatz_16, "Automatic parity and primitive substitutions in rational Collatz dynamics"** (agent lyapunov_weaver,
accepted 2026-10-21). Candidate theorems for the shortcut map on positive rational 2-adic integers x:
- Thm 1: if the parity sequence of x's orbit is automatic in any base, the orbit is eventually periodic;
- Thm 1b: a binary coding of a fixed word of a primitive substitution with irreducible incidence polynomial and Perron
  root > 1 is never the parity word of a positive rational, even after finite edits;
- Thm 1c: the same, with an integer Perron root > 1, forces eventual periodicity.

Method: the inverse parity value Φ(w) = −(1/3) Σ w_n 2^n / 3^{s(n)} is compared in ℝ and ℚ₂. It needs density
gaps (Bell's computable densities of automatic sets), a Mahler-method relation matrix (Adamczewski–Faverjon,
Stephan, Brechler), and the Subspace Theorem. The authors say the written arguments have no independent or formal
verification, and that a general p-adic Mahler precedence question (Wang) is unaudited.

**Where it touches our record.**
1. *RULE30-PRIZE.md's fold table, row "Collatz divergence"* lists "nearest single-object theorem: none". If correct,
   collatz_16 supplies one for structured parity: no divergent rational orbit has automatic parity or primitive-morphic
   parity of these two kinds. It is a single-object rigidity theorem, which is the column's kind.
2. *The Mahler row* ("one series in the reals and the 2-adics", MAHLER.md §1, G50/G51) uses the same
   completion-comparison idea on the same kind of series, with a parity word. collatz_16 is the most developed
   instance of that technique we have seen.
3. *G31's square-zero word and G36* (Monks–Yazinski: rationality preservation is equivalent to rational-orbit
   periodicity). Thm 1 would rule out every automatic word as the parity of a non-periodic rational orbit. Whether
   G31's square-zero word is automatic is a question to check, not a claim.

**Other abstracts with a link to our Collatz record** (titles only; not read beyond the abstract):
- collatz_15, periodic-dictionary complexity of trajectories (cf. G30, complexity forced by zero γ);
- collatz_9, the coupled real/ternary Syracuse affine series (cf. G32, separate real and 2-adic limits);
- collatz_2, 6, 7 and 11, decay of Tao's Syracuse characteristic function and density upgrades (cf. G38–G44);
- collatz_10, 12 and 14, predecessor counts, first landings and Krasikov–Lagarias λ_k → 2;
- collatz_3, two-path obstructions to descent potentials.

rStation also cites Allikvere (Zenodo, July 2026) on natural-density almost boundedness; a primary source to read later.

**Follow-up (2026-10-22 02:37 BST, Cloud; CL510).** A search found no Allikvere paper on Zenodo or elsewhere. It did find
the natural-density result that the citation most likely concerns:
- **Lech Mazur, "Natural-Density Almost-Bounded Collatz Orbits in Logarithmic Time", v2, 21 July 2026**, with a Lean 4
  formalization on ProofAtlas ([page](https://www.proofatlas.ai/formalizations/natural-density-log-time-collatz/));
  the main file is `Erdos1135/ND/LogTime/Paper.lean` at commit `ca3dd0d`.
- **Claims, read from the formalization page only** (paper not read): odd-relative-density-one many odd starts descend
  below any threshold tending to infinity within 145·log N Syracuse steps; natural-density-one many positive starts do
  so within 436·log N raw Collatz steps.
- **Formalization, as the page reports it:** the build passed, with "None" for unfinished steps; 599 first-party
  files, about 183k lines. The upstream input is "the Rhin phase gap", a linear-forms-in-logarithms lower bound for
  |a·log 2 − b·log 3|; Terras's bound is a separate companion.
- **Bearing on the record.** Tao (2019) proved almost-boundedness in LOGARITHMIC density and remarked that natural
  density is a separate question. Korec gave natural density with min ≤ N^θ, θ > log 3 / log 4. If Mazur's theorem
  stands, it upgrades the density notion and adds an explicit logarithmic clock. That bears on the Collatz rows of
  RULE30-PRIZE.md's fold table (G38–G44's density statements). It does not touch the prize statement (every orbit),
  and the page says a density-zero exceptional set may remain.
- **Nothing here is verified by us.** No build, no axiom audit, no paper read. A Local block could build the Lean
  project and audit its axioms, as was done for the contributed Lean repo.
- **Update, 2026-10-22 03:15 BST (Cloud, CL511): independently built and axiom-audited.**
  - *What was built:* ProofAtlas's checked-source bundle at commit ca3dd0d (599 first-party Lean files), with Lean
    v4.30.0-rc2 and Mathlib 5450b53e (the paper's pins). It was built in a fresh scratch directory with a no-secrets
    environment. `lake build Erdos1135.ND.LogTime.Paper` completed with 4,150 jobs and no errors in 31 minutes on
    4 shared cores.
  - *The one change:* the bundle omits its single FormalConjectures import, so Cloud supplied that file as a shim with
    only `CollatzConjecture.collatzStep`, using the upstream definition verbatim
    (`if Even n then n / 2 else 3 * n + 1`). It was checked against google-deepmind/formal-conjectures' file.
  - *Axioms:* `#print axioms` gives only [propext, Classical.choice, Quot.sound] for both paper theorems,
    `ndRhinLogTimePaperPackage` and `ndRhinRawCollatzSqrtLogTimeBracket`.
  - *Trust scan of the source:* no `sorry`, `native_decide`, `axiom`, `opaque`, `implemented_by`, `extern`, `unsafe`
    or `skipKernelTC`.
  - *Statement alignment, read by Cloud:* `ND13LogTimeStatement C` unfolds to: for every f : ℕ → ℝ tending to
    infinity, {N | 0 < N ∧ ∃ m, m ≤ C·log N ∧ Col^[m] N < f N} has natural density 1 (Tendsto of count/N to 1),
    with C < 436.
  - *Status:* the Lean artifact compiles against standard axioms and states the paper's main claim. This is a
    machine check of someone else's theorem, tier 1 for "the formal statement is proved". It is not a reading of the
    mathematics, and not a novelty assessment.
  - *Bearing:* Tao's logarithmic-density almost-boundedness now has a formally checked natural-density form with a
    logarithmic clock. That is the nearest single-object-free density theorem for the Collatz fold row. It says
    nothing about every orbit.

**Follow-up (2026-10-22 04:17 BST, Cloud; CL520): Collatz CYCLE work on rStation, read through its public search API as
prior art.** The searches for Mahler, Rule 30, Wolfram and cellular automata found nothing on those topics. They did
surface two recent Collatz discussion threads (community posts, not reviewed papers) that bear on RULE30-PRIZE.md's
fold-table row "Collatz cycle" (Simons–de Weger; Hercher's no m-cycles for m ≤ 91, arXiv 2201.00406).
- **r/collatz post 24 (agent fourier_wren, 2026-10-21)** reports three things:
  - a gap in the proof of Hercher's Theorem 15. An upper bound on n_{j+l} is used where a lower bound is needed, and an
    inequality is reversed for l ≥ 1. Without repair the chain gives only m ≤ 82.
  - an elementary repair, sorting the minima and using convexity, that recovers m ≤ 91 with the same K values;
  - that at the verification bound X₀ = 2^71 (Barina 2025), m = 92 reduces to exactly one pair,
    K = 205632218873398596256, L = 120287136981023372109.
  It also gives a method floor: X₀ > 1/(3Λ) is needed to exclude a given (K, L).
- **Cloud's check (unexpected check, CL520):** Λ = (K + L)·ln 2 − K·ln 3 = 8.9008 × 10⁻²³ and 1/(3Λ) = 2^71.6655, both
  as stated (90-digit decimal arithmetic). (K + L)/K − log₂ 3 ≈ 6.2 × 10⁻⁴³, an extraordinarily close upper
  approximation. Nothing else in the thread was checked.
- **r/collatz post 31 (agent lyapunov_weaver, 2026-10-22 02:45 UTC)** reports a computational exclusion of primitive
  positive cycles with exactly 95 rising blocks. Ingredients: a "completion before the final small block" interval for
  the minimum n that uses no exponent of the last small block, then a four-candidate search over 546,468,497 abstract
  nodes. It builds on earlier threads (by "Cassian" and "Wren") that reached 94 blocks.
- **Status:** unverified, community-reviewed at most, and very recent. Two things bear on our record:
  1. If the Thm 15 gap is real, the fold table's citation of Hercher should carry the repair.
  2. The cycle row's bounded-m frontier may be moving past 91.

  A careful read of Hercher's Thm 15 (lines cited as 508–510 of v3) is the natural independent check, and the
  owner's "prior art only" stance stands.
- **Gap read by Cloud (2026-10-22 04:18 BST, CL521; single-party).** In arXiv 2201.00406v3 (PDF) the step is in the proof
  of **Theorem 21** (pp. 13–14; the post's "Thm 15" is presumably the source's counter). It reads: "since
  n_{m−m₂+1+ℓ} < n_{m−m₂+1}^{(δ^ℓ)} ≤ n^δ_{m−m₂+1}, we get the inequality T(n_{m−m₂+1+ℓ}) < 3/(2^v − 1)^δ".
  - Remark 7's bound T(n) < 3/n needs a LOWER bound on n_{m−m₂+1+ℓ}, but Lemma 20 supplies only an upper bound.
  - For ℓ ≥ 1 and δ > 1 the middle inequality runs the other way.
  - So the displayed inference does not follow as written, and both of the post's objections are correct readings.
  - Not checked: whether the post's repair (sorted minima, K ≤ t·G(r)) recovers m ≤ 91, and the m = 92 and 95-block
    computations.
  - Our record cites only Simons–de Weger in the fold table, so nothing of ours rested on this step.
- **Repair checked numerically by Cloud (2026-10-22 04:31 BST, CL522; single-party; `tests/probes/cloud_reads/hercher_chain.py`).**
  An independent implementation of Theorem 21 + Lemma 22 + Theorem 23 reproduces Hercher's chain to K > 7.942e21 at
  m = 91.
  - Bounding the two gap terms by 3/X₀ each excludes only m ≤ 82.
  - The repaired sum bound, min(Σ_r 3/max(X₀, 2^{K/G(r)} − 1), 97m/(54X₀)) with
    G(r) = (δ^{m−r+1} − 1)/(δ − 1) + r − 1, excludes m ≤ 91 with the same final K, at X₀ = 704·2^60 and at 2^71.
  - m = 92 is not excluded at 2^71.
  - The repair lemma (K ≤ t·G(r)) was checked by hand in CL521. So, as far as a single reader can say, **Hercher's
    "no m-cycles for m ≤ 91" stands, with the repaired step.**


No rStation paper treats Rule 30, the Wolfram problems, Mahler's 3/2 Z-numbers as such, or eight streets. A search
for "rule 30" and "cellular automat" returned nothing relevant.


### Cross-intersecting linear families: scope check for the child-triple question (2026-10-22 09:33 BST, GPT, MI621)

Furedi, Gyarfas and Kiraly, *Problems and results on 1-cross-intersecting
set pair systems*, Combinatorics, Probability and Computing32(2023),691–702,
[primary publication](https://doi.org/10.1017/S0963548323000044).
Read the introduction and section1.4. Their indexed families have
disjoint corresponding pairs; the1-cross condition additionally fixes
other intersections at exactly one. The two full fixed-sum triple
fibres in our problem have neither requirement. Their bounds are not
a direct partition criterion. MI621 attaches an elementary transversal
argument specialized to fixed-sum triples, without novelty or PROOFS
status. Actual cut admission remains a separate missing interface.


### Exact two-component completion for unitary abundancy (GPT, MI631, 2026-10-22)

**Known algebra, reproved here; not a new finiteness theorem.** For a
partial product C let sigma*(C)/(2C) = A/B < 1 in lowest terms, and
D = B - A. Two further components r,s on new, distinct prime bases
complete it precisely when

    (D*r - A)(D*s - A) = A*B,

with both factors positive, congruent to -A modulo D, and the recovered
r,s odd prime powers on the required distinct bases. Expanding proves
the equation. A nonpositive factor would mean the single component
already reaches or exceeds abundancy 2, so a second positive factor
cannot complete it. Thus positive divisor pairs give an exact finite
completion test for THIS fixed C. No floating root bound is needed.

**Hand control with a free exponent.** For C = 2^a * 3 * 5, a >= 6, put
x = 2^a and r <= s. The remaining ratio is 5x/[4(x+1)] >= 16/13.
If r >= 11, the two factors contribute at most (12/11)^2 < 16/13.
Distinct bases exclude 9 and 5, so r = 7. Solving gives

    s = 32(x+1)/(3x-32),       32/3 < s <= 13.

Only odd prime powers 11 or 13 lie there. They force x = 384 or 64;
only 64 is a power of 2. Hence this branch gives exactly 87360, whose
sigma* product is 65*4*6*8*14 = 174720.

This is a short reproof inside the known four-odd-component classification
of [Subbarao–Warren (1966), Theorem 2(8)](https://doi.org/10.4153/CMB-1966-018-4).
Read Theorems 2–4. General fixed-component finiteness is their Theorem 4;
uniformly bounding the component count is still the missing global step.
The completion identity and this control do not restore that quantifier.


### Arbitrary norm residues at a split prime: a density guard (GPT, MI632, 2026-10-22)

**COMPLETE HAND reproof with elementary finite geometry; not independently
carried, no novelty claim or new proof number.** Let p be an odd prime
with p = 1 mod 4, and let nonempty P,Q be subsets of F_p^2. Suppose all
squared cross-distances lie in S, with k = |S|. Then

    |P| * |Q| <= p^2 * k^2.                                      (LC)

Choose i^2 = -1 and coordinates u = x + i*y, v = x - i*y; the norm is
u*v. An isotropic pair shares u or v. Any set without an isotropic
pair has at most p points, since its u coordinates are distinct.

If P contains an isotropic pair, translate it to (0,0),(0,a), a != 0.
For a point (u,v) of Q put s = u*v, t = u*(v-a). If u != 0, then
s-t = a*u != 0; each ordered pair (s,t) in S^2 with s != t determines
at most one point. If u = 0, all p possible points are allowed only
when 0 is in S. Hence

    |Q| <= k*(k-1) + p*1_(0 in S) <= p*k.

The last inequality follows from (k-1)*(k-p) <= 0. If BOTH sets have
an isotropic pair, this bounds both sides and proves (LC). If one set,
say Q, has none and |Q| >= 2, then |Q| <= p. Two distinct Q centres
have nonisotropic separation; two circles with those centres meet in
at most two points. Thus |P| <= 2*k^2, and |P|*|Q| <= 2*p*k^2 <= p^2*k^2.
For a singleton side the bound is immediate from the ambient p^2 points.
These cases exhaust the possibilities, including the degenerate zero
circles. For S empty the assumed nonempty cross product is impossible.

**Controls by hand.** S = {0} and P = Q = an isotropic line attains
p^2. S = F_p and both full planes attains p^4. A singleton reduction
is handled separately, rather than being called a two-centre case.
The two-circle bound is used only at NONisotropic separation; at
isotropic separation the zero circles can share a whole line.

The bound tensorizes for squarefree products m of split primes and
independent filters S_p. In a product relation, project P,Q onto the
first factor; their largest fibres, even if at different residues,
form a complete bipartite pair in the remaining factors. Induction
gives

    sqrt(|P|*|Q|)/m^2 <= product_p (|S_p|/p).                      (CRT-LC)

So the geometric-mean POINT residue density cannot exceed the uniform
NORM residue density allowed by these filters. This is only a density
efficiency statement about a specified congruence mechanism.

Primary context read: Kang–Koh–Rakhmonov,
[arXiv:2506.07251, introduction and generalized-distance bounds](https://arxiv.org/abs/2506.07251);
no assertion that its coordinatable-set hypotheses automatically apply
to P,Q. For fixed split prime p, equidistribution of represented norms
in ALL residues, including 0, is the known Rieger result quoted in
[David–Devin–Nam–Schlitt, Theorem 2.2](https://www-lmpa.univ-littoral.fr/~ldevin/conjecture-SOS.pdf).
Read that statement and the adjacent Euler-factor/character proof; no
strong error term or uniform growing-modulus estimate is adopted here.

**Unexpected closure check: do not turn an ambient bound into actual
support.** Take Pbar = Qbar = {(0,0)} modulo 5 and S = {0}. Every actual
integer difference lies in 5Z^2, so its squared norm is divisible by
25. The ambient allowed norm 5 is a sum of two squares and is 0 mod 5,
but cannot occur. Thus counting represented integers allowed by S
gives an UPPER candidate pool, not a LOWER bound for actual distances.
Neither (LC) nor (CRT-LC) proves #661 false, nor closes arbitrary
congruence constructions, correlated norm filters, higher prime powers,
non-lattice constructions or moduli growing with the point count.


## Odd-weird last-prime interface, including repeated primes (GPT, MI635, 2026-10-22 15:34 BST)

**Status:** known elementary divisor algebra and a hand scope guard, not a new theorem or solution of [#470](https://www.erdosproblems.com/470). The odd-weird question is the cash-prize branch; the original even 2^k*p*q work addresses the separate primitive-infinitude branch. No odd example, finite-range extension or independent-review request here.

**Primary sources read.** Fang, [Searching on the boundary of abundance for odd weird numbers](https://arxiv.org/html/2207.12906), sections 1–4, gives the least-odd-weird-to-primitive-abundant reduction, abundance-complement subset test, and a largest-prime search tree that permits repeated primes. Its large finite computations were read as published results, not replayed. Amato–Hasler–Melfi–Parton, [Primitive weird numbers having more than three distinct prime factors](https://arxiv.org/html/1803.00324), Theorem 3.1 and its proofs, gives sufficient multi-prime gap constructions, not a universal odd construction. Their [2019 paper](https://arxiv.org/html/1802.07178), section 5, explicitly poses the largest-prime-squared primitive-weird question. Its open-question status is that source's statement, not a fresh exhaustive literature verdict.

**Exact interface.** Let a hypothetical least odd weird N have largest prime p, write m=N/p=p^a*u with gcd(p,u)=1 and a>=0, and put delta=2m-sigma(m)>0. Then

    sigma(mp) = p*sigma(m)+sigma(u),
    A(N) = sigma(u)-p*delta.

The first identity follows from sigma(p^(a+1))=p*sigma(p^a)+1. The familiar sigma(m)-p*delta formula applies only when a=0. The proper divisors of N are the DISJOINT union of all divisors of m and p^(a+1) times the proper divisors of u. Thus pseudoperfection is exactly a two-block subset-sum condition for A(N), by complementing a subset inside the full proper-divisor set. If 0<A(N)<p^(a+1), the second block is too large: N is pseudoperfect iff A(N) is a sum of distinct divisors of m. This does not imply either existence or absence of an odd weird number.

**Hand controls.** For m=315, p=103 (new prime), delta=6, sigma(m)=624 and N=32445. The abundance is 624-103*6=6=1+5, both old divisors. A small positive abundance alone does not certify weirdness. For the repeated-prime control N=2205=3^2*5*7^2, take p=7, m=315, a=1, u=45: sigma(u)=78, so A=78-7*6=36=1+35. The coprime-only formula would wrongly give 582. This N is actually primitive abundant: its maximal proper divisors 735,441,315 have divisor sums 1368,741,624 respectively, each below twice the divisor. Hence largest-prime exponent one cannot be imposed merely from primitive abundance. This positive control does not refute a conjecture specifically about primitive WEIRD numbers.

**Outcome / missing step.** The bounded attempt does not supply the required uniform subset-sum coverage or a missing-abundance witness, including in the old-divisor-only range. Recasting the target as an affine deficiency is bookkeeping, not a full-target advance. Do not turn the known finite trees into a universal proof, launch a fixed-count census, or discard repeated primes. No experiment was run. Continue a genuinely different supported route in the active programme; G342's carrying review remains the only new proof request.


## #710: a primorial vertex obstructs multiplier-only fractional weights below the old scale (GPT, MI637, 2026-10-22 15:47 BST)

**Status:** complete HAND counterargument to GPT's own restricted repair, not independently carried; no novelty claim, proof number, new experiment or general matching obstruction. The elementary prime-product bound is PRIOR-ART. The actual #710 asymptotic remains OPEN. This does not refute edge-adaptive weights, vertex deletions/reservoirs, or the original report's general proposal to exploit arithmetic rarity.

**Question tested.** Can the prime-edge degree proof of Erdős–Pomerance be sharpened merely by choosing arbitrary nonnegative weights w(p), the SAME at every occurrence of prime multiplier p? A fractional certificate would require each left vertex to have load at least 1 and each right vertex load at most 1. The weights can depend arbitrarily on n. Read primary [Erdős–Pomerance, Matching the natural numbers up to n with distinct multiples in another interval](https://math.dartmouth.edu/~carlp/PDF/matching.pdf), section 3, Theorem 3 and proof of (11), journal pp.153–155. Their large top group is assigned one common multiplier; the bulk uses prime edges and a worst-case right-degree bound. No numerical claims are imported from their scan.

**Precise model and hand obstruction.** Fix C>1. Let T=T(n) tend to infinity with T^2=o(log n). Set X=n*T, Y=C*X, I={1,...,floor(n/T)} and J=(X,Y] intersect Z. An edge i->v is present exactly when v/i is prime, and its weight is w(v/i). For all sufficiently large n, NO such nonnegative weight function can have all left loads >=1 and all right loads <=1.

Set u1=floor(n/(2*C*T)) and u2=floor(u1/(2*C)); both belong to I and are positive eventually. Let Pj be the COMPLETE prime neighbourhood of uj, namely primes in (X/uj,Y/uj]. They are disjoint: X/u2 >= 2*C*X/u1 > Y/u1. Feasible left loads would give sum(P1)w>=1 and sum(P2)w>=1. Every prime in their union is at most Z=Y/u2=O_C(T^2).

Put Q=product of ALL primes <=Z. The standard elementary estimate log Q=O(Z) gives Q=exp(o(log n))=n^o(1). For completeness, primes m<p<=2m divide binomial(2m,m), so their product is at most 4^m; summing this bound over dyadic intervals gives log(product(p<=z)p)<=4*z*log 2 for z>=2. No prime number theorem or prime-in-short-interval assumption is needed here.

Choose v=Q*(floor(X/Q)+1). Since Q=o(X), eventually X<v<=X+Q<Y, so v is an ACTUAL integer of J, not a hypothetical high-degree profile. Every p in P1 union P2 divides v. Its partner i=v/p is a positive integer and satisfies

    i < Y/(X/u1)=C*u1 <= n/(2*T),

so it belongs to I. Distinct primes yield distinct partners. The load at this single right vertex is therefore at least

    sum(p in P1 union P2) w(p) >= 2,

contradicting the required upper load 1. If a chosen Pj were empty, left feasibility already fails. This proves the stated restricted obstruction.

**Checks and limits.** Floors only strengthen the separation u2<=u1/(2C); the upper estimate Z=O(T^2) uses n/T->infinity. Choosing the first multiple STRICTLY ABOVE X handles the open endpoint. The same v is inside the actual right interval, and all its selected partners remain in the actual left set. At T^2 comparable to log n, Q need not be n^o(1), so the construction need not fit J: it does not contradict the old sqrt(log n) upper proof. At the conjectured T of constant times sqrt(log n/loglog n), all hypotheses do hold. Merely noting that v is globally rare cannot validate a certificate whose column cap is universal. Deleting v, using different prime weights in different left blocks, or allowing weights to depend on i or v leaves this model, and is NOT ruled out. There is NO Hall-deficient left set or counterexample to #710 here.

**Outcome.** The tested prime-multiplier-only repair cannot remove the scale loss. This is a bounded strategy guard, not new asymptotic coverage, and no independent proof review is requested for it at this point. A genuine next argument must exploit the actual Hall set or adapt to individual edges/vertices; that remains a mathematical task, not an automatic permission to rerun the census.


## #711: the short-direction CRT compression gate (GPT, MI638, 2026-10-22 16:03 BST)

**Status:** HAND route audit using standard finite-field collision counting and Jensen's inequality, not independently carried, no novelty claim or proof number. Full #711 remains OPEN. No experiment or new review request. Record searched: 711/Korsky/Kakeya/projection collisions/CRT quadratic -> original swarm report and its sources; no earlier short-direction calculation found in this record.

**Source scope.** Read [Chen–Korsky, arXiv:2607.26450v2](https://arxiv.org/html/2607.26450v2), main statements, the complete local progression-union lemma, both upper-bound proofs, and the lower-bound proof in section 5. The appendix was not fully read. Their bounds, already cited in the original report, leave the official exponent conjecture open: the lower bound is n times exp((log(2)/2-o(1))*log(n)/loglog(n)); the upper bound has exponent 4/3+o(1). Also read Kominers's [primary introduction and statements](https://arxiv.org/html/2607.10431). These are literature results, not new project discoveries or independent verification of the entire papers. Open-right versus closed-right interval conventions can change the length by one, not these asymptotics.

**The attempted improvement.** Keep the squarefree CRT construction, but replace x^2 modulo each odd prime q by ANY function f_q:F_q->F_q, possibly depending on n. Let Q be the product of r such primes. The resulting map f on Z/Q is coordinatewise. Put

    a_q(j) = |{f_q(x)+j*x : x in F_q}|,
    A(j) = |{f(x)+j*x : x in Z/Q}| = product(q|Q) a_q(j).

Can this make A(j)/Q uniformly much smaller for j=0,...,K-1? Averaging over all Q slopes would be invalid here: the source has K much smaller than Q. Nor may one simply align the worst slope at every prime, since its CRT representative might lie outside that short range.

**A valid short-range budget.** Let E_q(j) be the number of ORDERED pairs (x,y) with f_q(x)+jx=f_q(y)+jy. Each of the q(q-1) unequal ordered pairs determines exactly one slope; the diagonal contributes q for each slope. Hence

    sum(j mod q) E_q(j) = 2*q^2-q.

Cauchy–Schwarz on each fibre gives q^2/a_q(j)<=E_q(j). Concavity of log therefore gives

    (1/q)*sum(j mod q) log(q/a_q(j)) <= log(2-1/q).

The nonnegative summand is at most log q and has period q. Split the ACTUAL K consecutive slopes into complete q-periods and fewer than q remaining terms. Summing over primes gives

    (1/K)*sum(0<=j<K) log(Q/A(j))
      <= sum(q|Q) log(2-1/q) + E,
    E = (1/K)*sum(q|Q) q*log q.

Consequently at least one actual j<K satisfies

    A(j)/Q >= exp(-E) / product(q|Q)(2-1/q)
            >= 2^(-r)*exp(-E).

Thus ANY uniform full-residue image envelope delta for this coordinatewise class must exceed that bound. For the source's first r odd primes and K=exp((log(2)/2+o(1))*r), r asymptotic to a fixed positive multiple of log(n)/loglog(n), E=o(1): sum(q log q)=O((log n)^2), whereas K exceeds every fixed power of log n. The quadratic choice has delta=2^(-r)*product(1+1/q)=exp(-r*log 2+o(r)). Replacing the local functions alone cannot improve its LEADING logarithmic compression constant in this uniform-envelope class. This does not prove optimality of the whole lower-bound method.

**Adversarial controls and boundary.** For f_q=0, a_q(0)=1 and a_q(j)=q at every other local slope; the energy identity still gives 2q^2-q. With K=1 every coordinate collapses, so dropping the remainder E would falsely assert A(0)/Q>=2^(-r). This is an explicit countercontrol to that tempting period-average shortcut. For f_q=x^2 every image has (q+1)/2 points, checking the comparison with the source. All checks are literal hand identities, not a numerical run.

**Missing full-target inference.** A correlated f modulo Q need not factor into f_q, so the product step would fail. Moreover, full-residue images are only an UPPER envelope for the source's ACTUAL prime subset. The calculation supplies neither a lower bound on that physical support nor an obstruction to all short-direction constructions. It is not a Hall deficit, an upper bound on F(n), a polynomial lower bound, or a solution of #711. Stop the coordinatewise uniform-envelope refit; a new argument must use correlated residues, actual progression support, or a different full-target route. No automatic map census or prime-power extension.


## #647: fixed windows do not supply a uniform divisor barrier (GPT, MI640, 2026-10-22 16:17 BST)

**Outcome:** the bounded full-target attempt is inconclusive; no new theorem, finite exclusion, experiment or proof review. The original report already states the fixed-window Schinzel-H implication. Here is its exact construction and the missing uniformity, not a new result. Record searched: 647/divisor forcing -> original report and R647; its fixed-dimensional sieve was already carried.

The official page and thread returned HTTP 403 in this read. The indexed official statement agrees with the primary [Mian–Siddique paper](https://arxiv.org/html/2608.17880), read in full: finite certificates do not prove an infinite domination chain. No Lean build or claimed range is adopted independently here. Read Erdős's original [1979 Barriers paragraph, p.68](https://www.renyi.hu/~p_erdos/1979-22.pdf). Read Lau [2604.15042v3](https://arxiv.org/html/2604.15042), introduction, outline and section 7, plus Tao–Teräväinen [2512.01739v2](https://arxiv.org/html/2512.01739), introduction only. Lau's backward theorem supplies an unspecified constant times log k for Omega; it does not supply tau(n-k)<=k+2. The technical sieve proofs were not fully read or independently carried.

For fixed K>=2 let M=lcm(1,...,K)^2. The distinct linear forms F_i(t)=(M/i)*t-1, i=1,...,K, are admissible. For p<=K all coefficients are divisible by p, hence no form vanishes modulo p. For p>K at most K residues are excluded. Under Schinzel's H, infinitely many t make all forms prime. With n=M*t, gcd(i,F_i(t))=1 since i^2 divides M, and

    tau(n-i)=2*tau(i)<=2*(floor(i/2)+1)<=i+2.

This verifies EVERY inequality in the fixed prefix, not the remaining shifts. The n can depend on K without any usable upper bound. Already n>=M and log M asymptotic to 2K constrain this particular construction to K<= (1/2+o(1))*log n; no global divisor-tail bound covering the rest was obtained. Swapping these quantifiers would assert what is missing.

Unexpected hand control: the elementary large-Omega obstruction from powers of 2 does not imply a tau obstruction. At m=2^a one has Omega(m)=a but tau(m)=a+1, rather than 2^a. Similarly, a lower bound omega(n-k)>(1-epsilon)*log k only forces tau above k^{(1-epsilon)*log 2}, below the linear threshold. No implication from these cited statements settles #647. The next constructive finite target is #634's small tiling branches; no larger divisor scan or fixed-window sieve refit follows.


## #634: provisional boundary reduction for an equilateral rational 120-degree tile (GPT, MI641, 2026-10-22 16:17 BST)

**Status:** HAND source-based application, not independently carried, no novelty/proof number or full #634 claim. It is a possible reduction of the small-composite branch, pending the actual classification/interface audit. No experiment or review queue yet. Record searched: two c edges/14-tiling -> original report's scalar boundary discussion, not this inequality.

Read Beeson [No triangle can be cut into seven congruent triangles](https://arxiv.org/html/1811.09723), v5, section 12.2, Lemmas 7–8 and their proofs, also compared with the author's PDF. For an equilateral triangle tiled by a rational nonisosceles tile with angle gamma=120 degrees and irrational alpha/pi, the two-c-edge lemma says every boundary side contains at least two longest tile edges. Its general printed proof refers to an unlisted hypothesis (iv) in one endpoint case; DO NOT adopt the unrestricted lemma merely from its statement. In this EQUILATERAL application alpha+beta=60 degrees and alpha<beta, so a corner of 60 degrees is strictly between beta and 2beta. That problematic double-beta endpoint case is never entered. Boundary vertices containing gamma have the unique remaining angles alpha and beta, as required by the proof. The equilateral application and the other endpoint case still deserve a scoped carrying read before any new theorem is promoted.

**Arithmetic after that geometric premise.** Normalize the rational tile to primitive positive integers a<=b<c, with c^2=a^2+ab+b^2. They are pairwise coprime. Let L be the equilateral side, so L^2=Nab. Two c edges give L>=2c. Equality L=2c would imply ab divides 4, by coprimality with c. Up to swapping, the possible pairs (a,b) are (1,1),(1,2),(1,4); none has integer c. Thus L>2c. Boundary sides are unions of WHOLE tile edges; any further edge has length at least a. A third c edge also meets that bound. Therefore L>=2c+a.

Since c>b+a/2,

    (2c+a)^2-18ab
      =5a^2+4b^2-14ab+4ac
      >7a^2+4b^2-10ab
      =((4b-5a)^2+3a^2)/4 > 0.

Hence this application would give N>18 in the stated rational, nonisosceles equilateral 120-degree branch. The known 3-tiling by a 30-30-120 tile is an adversarial scope control: its side ratios include sqrt(3), so the rational/primitive-integer premise fails. No contradiction or universal obtuse-tile bound follows.

For the separate 14-tile triquadratic arithmetic candidate, tile (6,5,9) and outer sides (28,15,27) have exact area ratio 14. The same two-c-edge boundary premise would reject it because 15<2*9, but the equilateral-only audit above does NOT by itself verify that application. The original report's other shapes, commensurability reductions and its n<=100 map remain distinct dependencies. In particular, do not mark N=14 or N=15 fully excluded, alter original reports, or mark prize won on this basis. Continue the bounded source/interface audit before a consolidated carrying request.


## #634: completed boundary proof and the N=15 interface (GPT, MI642, 2026-10-22 16:32 BST)

**Status:** G343 is a COMPLETE HAND candidate in PROOFS.md's waiting room, not independently verified. Its specialized boundary mechanism is known machinery rederived with explicit equilateral hypotheses; novelty of the N>18 consequence is unassessed. The following N=15 composition is CONDITIONAL on G343 and the named literature premises, not a full #634 solution, a newly proved classification, or a prize won. No experiment or finite scan was run. The original agent reports and measured table are preserved unchanged.

**Actual sources and version limits.** Read the exact shape statements, commensurability and integer-scale/area derivations in Beeson–Rosu [2607.23453v3](https://arxiv.org/html/2607.23453v3), especially Theorems 4, 5, 7, 9 and Lemmas 10–18, followed by Theorems 19–22 and section 8. Read the relevant necessary conditions in Beeson [1206.1974](https://arxiv.org/html/1206.1974), which the fetched page labels **v7**, including Theorem 7.8 and the statement and main boundary argument of Theorem 11.7; do not call this a verified v8 read. These long classification proofs have not been independently re-proved here. The equilateral five-case list and Theorem 3(i) in [1812.07014v3](https://arxiv.org/html/1812.07014) were read, including the positive coloring number and square condition. The following short arithmetic is a new hand interface audit of those stated necessary conditions, not a replacement for their proofs.

**1. Equilateral outer triangle.** Classical counts are square, three times square, or six times square, so do not include 15. An irrational-angle tile with a 60-degree angle requires an integer 0<M<sqrt(15) with (135-M^2)*(15-M^2) square. At M=1,2,3 these integers are 1876,1441,756: strictly between 43^2 and 44^2, 37^2 and 38^2, and 27^2 and 28^2 respectively. The remaining 120-degree case is rational by the cited classification and is excluded by G343. Thus the equilateral N=15 conclusion depends only on G343 plus these explicit known classification/coloring premises.

**2. Group 1.** Put D=k^2-m^2, A=2*k^2-m^2, B=3*k^2-m^2, with coprime positive m<k. The source/report's integer-scale necessary counts for its five shapes are s^2*A, s^2*B, s^2*A*B, s^2*A/D, and s^2/D. The first two cannot equal 15: squarefreeness forces s=1; for A only k=2,3 can occur and the possible values are 7,14,17; for B only k=2 can occur and B=11. The product is at least 7*11=77. For s^2*A/D=15, A/D>2 forces s<=2; gcd(A,D)=1 forces D|s^2. None of D=1,2,4 is a difference of positive coprime squares, so this case is absent.

For the last shape, the previously scoped R634 corner argument extends directly from prime to **squarefree** N: its b=D boundary count gives D<=s<=N. If N=15 and s^2=15*D, then 15|s, hence s=D=15. The apex leg carrying a b edge is all b edges, as is the base, by the original mod-k counts. Their common corner must contain one alpha tile and one beta tile, but the beta tile has no b edge adjacent to beta. This is the same contradiction as the original A1 proof, now with the squarefree divisibility stated explicitly. It is not a claim of a new general classification or novelty.

**3. Group 2, four non-isosceles shapes.** The actual integer-scale formulas are lambda^2*3*(a+2*b)*(a+b), lambda^2*(2*a+b)*(a+b), lambda^2*(a+b)/b, and lambda^2*(a+2*b)*(2*a+b), where c^2=a^2+a*b+b^2 and the sides are primitive positive integers. The first count is >=18. For the second and fourth, squarefreeness forces lambda=1. The only possible factor pair is 3,5: the second forces (a,b)=(2,1), with c^2=7; the fourth forces fractional a,b. For the rational quotient formula, lambda<=3 and the ratios a/b at lambda=1,2,3 are 14,11/4,2/3. Primitive c^2 would be 211,181,19, none square. No product-compositeness inference alone was used to discard a composite N.

**4. Non-equilateral isosceles cases.** Reptilings and right-tile tilings are excluded at 15 by the cited classical/right-tile necessary counts (square, twice square, six times square, or even sums of squares). The gamma=2*alpha branch is excluded by the cited Theorem 11.7's nonsquarefree conclusion; that is a KNOWN source premise, not a new carrying read of all its rationality and boundary lemmas. The Group 1 shapes were handled above. For the 120-degree branch, section 8's exact formula is N=lambda^2*(a+2*b)/b, with lambda a positive integer. At N=15 positivity forces lambda=1 or 2; the required primitive side ratios a/b are 13 or 7/4, giving c^2=183 or 93, neither square. This uses the actual area formula, not the separate preprint's prime exclusion.

**Coverage and review question.** Subject to the quoted classification/commensurability/isosceles necessary conditions, these cases exhaust N=15 and exclude it. The new carrying step is G343's boundary-to-whole-edge argument and N>18 arithmetic; the composite interface also needs its scales and full case coverage checked. One consolidated request asks Cloud to carry G343 and audit this N=15 composition in exactly that literature-dependent scope. A successful review would settle a single count, not characterize all admissible N or win #634's prize. In particular N=14's non-equilateral (6,5,9)/(28,15,27) application is still separate. The bounded hand block is completed, not renewed for a threshold or tiling-search extension.

**Niggle sweep / unexpected check.** R in the lone-c proof can initially lie on a different outer side: the forced long edge from Q would then leave the convex triangle, so that case contradicts containment before using an internal half-neighborhood. T-junctions are allowed; termination at R, not an edge-to-edge assumption, is what makes the PR edge decomposition whole. Squarefreeness is used only where the relevant multiplicative factor is already an integer; it is NOT applied to the quotient counts before checking divisibility. The standard irrational 3-tiling remains a negative scope control. Gut: pleased that the boundary gap became a concrete proof; cautious about promoting the complete N=15 conclusion before its literature interface is independently checked.


## #552: the full deficit question and the missing uniform construction (GPT, MI643, 2026-10-22 16:41 BST)

**Outcome:** bounded full-target HAND/source attempt inconclusive. No new Ramsey bound, graph, experiment or carrying request. The cash question is whether n+sqrt(n)-R(C4,K_(1,n)) is unbounded along a sequence, not determination of one more small value. Record searched: C4 star/R552/Parsons/polarity -> original report and reviewed increment/matrix facts. The direct official page returned 403; indexed official wording was corroborated by the original paper's section 4.

**Primary sources actually read.** Burr–Erdos–Faudree–Rousseau–Schelp, [1989 paper](https://www.renyi.hu/~p_erdos/1989-32.pdf), Theorem 2 and its random-deletion proof on journal pages 84–85, and section 4 on pages 88–89. Boza [2409.12770v2](https://arxiv.org/html/2409.12770), sections 1–2 including all the functional-inequality proofs, and the table containing n=41. No finite search, external Lean build or solver receipt was replayed. A newly located external R(C4,K_(1,39))=46 candidate is not adopted here.

**A definite provenance correction.** Boza's v2 dated 12 June 2026 already lists f(41)=49, with an earlier reference. The swarm's independently controlled 48-vertex graph remains a valid witness, but the Ramsey VALUE cannot be described as newly found. This does not settle novelty of that particular connection rule. The original reports are preserved; the current review is corrected rather than rewriting their history. Independently checked [Radziszowski DS1 revision 18, Table IVa, printed page 21](https://www.cs.rit.edu/~spr/ElJC/ejcram18.pdf): its explicit row is 41, 49, reference Boza8. This is star indexing, not an inference from a wheel table.

**What the attempted structural route needs.** Put F(v)=max delta(G) over C4-free graphs on EXACTLY v vertices. Then f(n)=min{v:F(v)<v-n}. Negation of the prize assertion is equivalent, up to an absolute change of constant, to F(v)>=sqrt(v)-O(1) for every sufficiently large v. For one direction, if f(n)>=n+sqrt(n)-C, choose an integer K>C+2 and n=v-floor(sqrt(v))+K. For large v, n+sqrt(n)-C>v, so an actual v-vertex graph has minimum degree >=v-n=floor(sqrt(v))-K. Conversely, an all-v bound F(v)>=sqrt(v)-K applied at v=n+floor(sqrt(n))-ceil(K)-2 gives f(n)>v and hence a uniform bounded Ramsey deficit. These are quantifier checks of the known graph reformulation, not a construction.

The minimum order m(d) of SOME graph of minimum degree d is not the same datum as existence on EVERY required v. Disjoint unions preserve degree but only produce sums of available component orders, and cannot fill an interval just above d^2 by combining two components already of order about d^2. The prime-power/random-deletion proof supplies graphs at all target orders only with the loss its quantitative estimates permit; it does not give an absolute loss. No completion theorem filling this gap was obtained.

**Unexpected HAND control on a tempting functional shortcut.** The purely numerical function h(n)=n+floor(sqrt(n))+1 satisfies monotonicity, increments at most 2, Parsons' quoted upper bounds, the prime-power exact-value formulas at q^2 and q^2+1, and Boza's two main inequalities. For the disjunction h(a)>=a+b OR h(a+b)<=a+2b: if the first fails, b>=floor(sqrt(a))+2, so a<=(b-1)^2-1 and a+b<b^2. Therefore floor(sqrt(a+b))<=b-1, giving the second. Also h(m^2+3)=m^2+m+4 for m>=2, including the stated congruence class. Yet n+sqrt(n)-h(n) lies in [-1,0). Thus THESE universal functional conditions and prime-power values alone cannot force the affirmative cash conclusion. This h is NOT the actual Ramsey function (for example h(41)=48, whereas f(41)=49), does NOT fit every published small value, and does NOT construct graphs or prove the negative answer. It is a scope control for this proposed deduction only.

For a d-regular C4-free graph the known matrix identity is A^2=(d-1)I+J-B, where B is regular of degree e=v-1-d(d-1), joining pairs with no common neighbor. In the prospective bounded-deficit regime v=d^2+O(d), e=O(d), not a bounded number of exceptions. Finite near-equality rigidity cannot simply be assumed to complete a projective plane, nor do absent prime-power constructions prove absent graphs. No new global spectral contradiction or bounded-loss construction follows from the audited information.

**Trajectory choice.** This full-target attempt ends at a genuine missing all-order graph construction/nonexistence theorem. Do not replace it by a larger Ramsey table, a fixed-defect repair catalogue or an unsupported projective-plane equivalence. Next supported independent question: #7's actual repeated-prime sieve/interface, read from primary sources before proposing a universal lift. That is a different full-target inference, not an increase from the carried four-prime certificate to another finite list. G343's existing review remains pending without duplication; the programme stays ACTIVE.


## #99: exact triangle-free KKT configurations at every size (GPT, MI644, 2026-10-22 16:41 BST)

**Status:** standard regular-polygon geometry, known machinery reproved as a scoped HAND review of CL557, not a new prize result, proof number or carrying packet. No numerical experiment. CL557/90f6cab1 and kkt_check.py were read in full. Its normalized NNLS system has the correct contact/diameter signs and sum(mu)=1; a floating residual and tolerance active set are not an exact KKT certificate or proof of local minimality. The exact control below shows that the bare KKT equations really do allow unit-triangle-free configurations for all n>=4. It does not exclude first-order information combined with a global optimality constraint.

Take a regular n-gon of radius R=1/(2*sin(pi/n)), with vertices x_i. Its minimum distance is 1; the unit contact graph is the cycle C_n, which has no triangle for n>=4. Write u_i=x_i/R. The two unit contact directions at vertex i sum to 2*sin(pi/n)*u_i. Use the SAME nonnegative multiplier lambda on every contact edge.

For even n there are n/2 diameter pairs. Put mu=2/n on each and lambda=1/(n*sin(pi/n)). The diameter direction at each vertex is u_i; its weighted pull is (2/n)*u_i, equal to the weighted contact sum. For odd n there are n diameter pairs, joining offsets +(n-1)/2 and -(n-1)/2. Put mu=1/n on each and lambda=cos(pi/(2*n))/(n*sin(pi/n)). Those two diameter directions sum to 2*cos(pi/(2*n))*u_i, again giving force balance at every vertex. In both cases sum(mu)=1, all multipliers are positive, feasibility and complementary slackness hold, and the D-derivative is normalized correctly. No tolerance graph or limiting argument is used.

**Controls and scope.** At n=4 the formulas give a unit square, D=sqrt(2), lambda=sqrt(2)/4 and mu=1/2. At n=3 the contact graph is a triangle, so the n>=4 gate matters. These are stationary configurations, not asserted local minima. Their diameter grows linearly in n, whereas n points on a unit square grid fit in diameter at most sqrt(2)*(ceil(sqrt(n))-1); hence the polygons are globally suboptimal for all sufficiently large n. Thus force balance alone is insufficient at arbitrarily large size, but exact global attainment, additional rigidity and the full #99 question remain open. Cloud retains that lane; this is one cheap independent scope check of its new claim, not a duplicate search.


## #7: repeated-prime fibres and the actual distortion interface (GPT, MI645, 2026-10-22 16:54 BST)

**Status:** bounded full-target hand/source attempt, inconclusive. Known sieve algebra, no new proof number, experiment, finite-prime extension or review request. Record searched: distortion / squarefree covering / Hough–Nielsen -> original swarm report and R7; no earlier full repeated-prime interface in this record.

Read Hough–Nielsen, [Covering systems with restricted divisibility](https://www.math.stonybrook.edu/~rdhough/covering_restricted.pdf), sections 2–3's hypotheses; BBMST, [1901.11465v1](https://arxiv.org/html/1901.11465), sections 2–3 and the section 5 interface; and [1811.03547v1](https://arxiv.org/html/1811.03547), sections 2–3 and 6–7. Their tail already permits prime powers: squarefreeness in the later theorem is required only at primes at most 73. This is known scope, not our extension. Published numerical optimizations were read, not replayed or independently recertified here.

For a new prime p, write d=m*p^e. In an old-coordinate fibre x, the actual removed fraction is bounded by

    alpha_p(x) <= sum_{d=m*p^e} p^(-e) * 1[x == a_d mod m].

A p^a-coordinate does NOT make every progression a singleton: a class modulo p^e has p^(a-e) points. The exact hand control 0 mod 3 together with 1 mod 9 removes 4/9, not 1/9 or 1/3. The two classes are disjoint, so deleting contained progressions does not fix this interface. For previous prime r, compatible exponent pairs use max(a,b); the known identity

    sum_{a,b>=0} r^(-max(a,b))
      = 1 + sum_{j>=1}(2j+1)/r^j
      = 1 + (3r-1)/(r-1)^2

explains the published coefficient, rather than the squarefree 1+3/r. The multiplier 2j+1 counts ordered exponent pairs with maximum j. A single distortion cap is paid per PRIME here, not once per digit. Thus digitwise loss is avoidable by known grouping, but grouping supplies no monotone improvement of the squarefree initialization.

**Unexpected check.** Disjoint p-prefixes need not have a zero cross term in alpha_p(x)^2: this squares the TOTAL removed fraction over y, not the indicator intersection at one common y. For the two disjoint 3-prefixes above, alpha=1/3+1/9 and its square still has the positive 2/27 cross term. Ignoring that distinction would incorrectly remove a real contribution. No universal residue-sensitive saving or small-prime starting measure meeting the full tail criterion was obtained. Full #7 remains OPEN. Stop the automatic prime-power lift and finite-support extension; no outside Lean claim was built or adopted.

## #32: Radomskii's new lower bound, scoped source audit (GPT, MI646, 2026-10-22 16:54 BST)

**Status:** PASS as an independent hand source audit of the specified preprint argument; externally authored mathematics, not a project discovery, prize claim, formal proof or claim of journal acceptance. No experiment or new carrying queue. Record searched: Radomskii / 2610.14127 / large-shift lemma -> no earlier hit. The original swarm's conditional theorem remains valid but its current-status account predates this source.

Primary sources: Radomskii, [A lower bound for additive complements to the primes, 2610.14127v2](https://arxiv.org/html/2610.14127v2), revised 19 October 2026, complete main proof read; and [Large gaps between Romanoff numbers, 2609.38408v1](https://arxiv.org/html/2609.38408), section 3's complete carrying proof of Lemma 3.1 read. The latter PDF was also checked for the lemma's actual prime range: the lower endpoint is x^6, not x/6. The unversioned first paper HTML/PDF returned v1; the v2 HTML was read explicitly, and a v2 PDF fetch failed. No assertion that the missing v2 PDF was read.

The conclusion is B(X) >> log X * loglog X for every asymptotic additive complement B. It excludes O(log X), the subquestion attached to the $50 offer, but leaves the displayed o((log X)^2) problem open. No project prize-won cell changes to Yes.

**Carrying audit, not abstract-only adoption.** In the large-shift lemma, remove primes dividing the product of shift differences: log(Delta)=O(x^3), and primes exceed z=x^6, so the discarded reciprocal mass is O(1/(x^3 log x)). This preserves the coefficient normalization B comparable to 1. The cancellation sum a(d)/phi(d)=0, tilted square mass A_gamma<=A+C*gamma, and absolute divisibility-coefficient bound D^(3/2) were checked. The complete-period Gram matrix has zero blocks for unequal prime products; within each product its absolute off-diagonal row sum is O(k log D/z). Thus the signed local covariances are NOT treated as independence. The short-interval replacement costs D^3/T, using literal CRT residue counts, not an unjustified full-period average. Here D=exp(x/4), T=floor(exp(x)). Product-cutoff and repeated-prime losses are controlled before forming S1. Collapsing an uncovered form gives epsilon(v)>=0 with epsilon(v)<< (v/D)^beta+log(D)/z; the resulting S2/S1 tends to zero uniformly for k<=eta*x. This checks the simultaneous translate and uniformity in the baseline b, the earliest potentially dangerous input.

In the complement deduction, average the distinct shifts j-a modulo Q to leave <=eta*x of them; M=B(X), HM<=c*log X*loglog X, x=log X/3. A B-free gap in [X/2,X] has length L>=X/(2(M+1)). Its middle third contains the whole translate range, because Q*exp(x)=X^(2/3+o(1)) and H,y=X^o(1). Every positive difference then exceeds y, so its prime divisor is proper; elements of B to the right give negative differences. The floor only needs H>=1 for the final contradiction. All thresholds are uniform in B once H>=1 bounds M by c*log X*loglog X. No gap was found in these carrying steps.

**Unexpected checks / limits.** B empty gives a vacuous shift list, handled by t=1. B={0} reduces the block statement to a prime-gap lower bound, a substantive consistency requirement rather than an additive-complement discovery. Allowing a divisor equal to the difference would be fatal; the B-free gap and strict middle-third inequalities explicitly exclude it. Density-one coverage has no such eventual contradiction, so the almost-all upper bounds in the old report do not conflict with this theorem. No stronger log-squared lower bound or o(log-squared) construction follows.

**Trajectory.** The cash subquestion has a new external negative proof in the primary record, not a new solution by us. Update provenance and continue the genuinely open displayed question: can an almost-all thin complement be repaired into one global complement with o(log-squared) growth? The needed estimate is the actual exceptional-set repair cost, not merely density zero. Read the existing primary upper constructions before claiming that bridge. G343 remains pending its existing scoped review; no duplicate request and no self-halt.


## #32: the actual cost of repairing an almost complement (GPT, MI648, 2026-10-22 17:05 BST)

**Status:** completed bounded HAND/source audit, no full solution, new theorem number, experiment or carrying request. Record searched: exceptional complement / Kolountzakis / Dai–Pan / almost-all primes -> original e32 report and MI646; no existing repair-cost argument found. The owner then explicitly requested a pause after this block, superseding the earlier no-self-halt instruction. The heartbeat was set to PAUSED and its saved status verified; no further block is opened.

**Primary inputs actually read.** Kolountzakis, [author's August 1995 typescript](https://eigen-space.org/mk/ps/except.pdf), Theorem 1/remark and complete section 2.2 on pages 3–6, inspected visually because text extraction was garbled. Its independent choice probability is K*loglog(x)/x. The proof supplies A(x) asymptotic to K*log(x)*loglog(x), expected exceptional count O(x/log(x)^alpha), alpha=c*K for an absolute c>0, and then chooses alpha>M+1 for a fixed desired exponent M. The statement “for any M” therefore permits changing K and A; it is not a free improvement for one fixed construction.

Also read Dai–Pan [1101.1653v3](https://arxiv.org/html/1101.1653), introduction and section 3: fixed-epsilon construction costs K(epsilon)=O(1+log(1/epsilon)) times log N, followed by a sparse-stage diagonalization for density one. Its thresholds N0(epsilon) are not uniform at epsilon=epsilon(N). Ruzsa's full original PDF fetch failed and its author link returned DVI; no claim that its full proof was read here.

**Scope check.** Dai–Pan Theorem 1.2 covers almost all EVEN integers with B a set of primes. Its literal section-3 display S(x)>=(1-epsilon)x cannot be used for all integers: an odd member of P+B must use 2 as one summand, so there are at most 2*B(x) odd members. Thus S(x)<=x/2+O(B(x)+1). The intended even-number normalization/parity shift must be kept; this is a displayed normalization issue, not a refutation of the main almost-even result. No new analytic theorem is adopted from that display.

**A valid finite repair bound.** Let E be the ACTUAL complement of S=P+A and suppose |E intersect [X,3X]|<=delta*X, 0<delta<1. Choose t shifts independently from {0,...,X-1}. For each target n in {2X,...,3X-1}, n-d stays in [X,3X], and at most delta*X choices of d fail. Hence the expected number of uncovered targets is <=X*delta^t. If X*delta^t<1, some shift set D with at most t elements makes S+D cover the entire target window. Taking the new additive set (A intersect [0,3X])+D uses at most t*A(3X) elements. This is a legitimate existence argument by averaging, not a numerical experiment or a claim that the bound is sharp.

For the fixed-M source guarantee delta=O_M((log X)^(-M)), this certificate takes

    t=(1+o(1))*log X/(M*loglog X),
    t*A(3X) <= (K/M+o(1))*(log X)^2.

The displayed construction chooses K proportionally to M, so increasing M in this calculation does not make the certified coefficient tend to zero. This is an UPPER-BOUND budget that fails to imply little-o, not a lower bound forbidding better repair sets, overlaps between translated copies, or prime-specific structure.

**The global gate is additional.** A different finite D for each window is not one global complement. One safe globalization chooses shifts in [X/2,X) and targets in [2X,4X); the same argument applies with constant-factor changes. Every new additive element is then >=X/2, so future blocks do not pollute a fixed initial segment. Summing these O((log X)^2) certificates over dyadic X gives only O((log x)^3) by this crude count. It cannot be silently called o(log-squared), or even the classical O(log-squared) theorem. A reuse/overlap theorem would have to improve that count explicitly.

**Unexpected adversarial check.** Let E be the union of the integer intervals [N_j,N_j+j], N_j=2^(2^j). For every fixed M, E(x)=O_M(x/(log x)^M). Yet S=N minus E cannot be made cofinite by ANY fixed finite set of nonnegative shifts D: if j exceeds max(D)-min(D), then n=N_j+max(D) has n-d in E for every d in D. Thus arbitrarily strong fixed polylogarithmic exceptional bounds do not alone justify a fixed-finite-translate repair. This artificial S is not asserted to equal P+A; the check refutes only the density-only inference, not #32 or a growing adaptive repair.

**Outcome / trajectory.** No o((log x)^2) complement was constructed, and no impossibility proof was obtained. The actual missing inference is a prime-specific exceptional-set structure or a global shift-reuse bound with a smaller counting cost. This block closes without a local exponent/threshold catalogue. MI646's external lower bound and G342/G343's verified partial scopes stand. At the owner's explicit request, the programme is now PAUSED awaiting their continuance, not automatically resumed by a colleague's message.


## #120 (Erdős similarity): the dyadic and geometric cases are claimed externally (Cloud, CL560, 2026-10-22)

**Status: EXTERNAL CLAIM, read in part, not verified or built here.** OpenAI's public math release repository
(github.com/openai/math) holds two unrefereed preprints, "The dyadic case of the Erdős similarity conjecture"
(25 September 2026) and "The geometric case of the Erdős similarity conjecture" (5 October 2026). The second's main
theorem: for every q in (0,1) and η in (0,1) there is a compact E ⊆ [0,1] with m(E) > 1−η such that for every x and
every s ≠ 0, x + s q^n ∉ E for some n ≥ 1. The set may depend on q. The erdosproblems.com page for #120 links a Lean
formal statement of the dyadic case (lean/ComparatorChallenges/DyadicAvoidance.lean: the statement with `sorry`; its
JSON names the solution module OAI.MeasureTheory.DyadicAvoidance.Main and permits only propext, Quot.sound and
Classical.choice). We read the statement, the abstract, the mechanism overview and the related-work section; we did not
read the proof or build the Lean. The page still lists #120 as open, rightly: the prize asks for EVERY infinite set.

The preprint's related-work section names the prior criteria: Falconer and Eigen (a_{n+1}/a_n → 1),
Humke–Laczkovich, Kolountzakis 1997 (probabilistic; double sums including G_{1/2}+G_{1/2}), Bourgain 1987 (triple
sums), Chlebík 2015 Theorem 15 (finite subsets with normalized minimum gap e^{-o(m)}), Kolountzakis–Papageorgiou
2025, Mora Cuéllar et al. 2026 (geometric plus any infinite set), and Iosevich et al. 2026 (Rajchman measures,
which excludes countable sets). Survey: Jung, Lai and Mooroogen, arXiv:2412.11062.

Two elementary facts place what remains (CL560, tests/probes/swarm/ladder/e120/frontier.py; standard, recorded as
reasoning, not as a new result). First, avoiding an infinite subset of A avoids A. Second, if a_{n+1} ≥ c·a_n, the
greedy subsequence (next term = first a_m ≤ a_k/2) has every ratio in [c/2, 1/2]. So an extension of the geometric
method to ratios confined to a fixed interval [c, 1/2] would settle every null sequence with liminf a_{n+1}/a_n > 0.
Super-exponential sequences such as 2^{-n²} would remain; there, every m-point window's normalized minimum gap
decays like 2^{-Θ(m²)}.

**Addendum (Cloud, CL561, 2026-10-22): the bounded-ratio extension. PROOF-SKETCH, single-party, CONDITIONAL on the
geometric-case preprint's argument (unrefereed).** Claim: if a_n decreases to 0 and κ ≤ a_{n+1}/a_n ≤ λ < 1 for all
n, then for every η there is a compact E ⊆ [0,1] with m(E) > 1−η that avoids every x + s·a_n (s ≠ 0). Combined with
the subset and greedy lemmas of CL560, this covers every decreasing null sequence with liminf a_{n+1}/a_n > 0.
Sketch: run the preprint's construction verbatim with q^b replaced by a_b and c = 4/(1−λ). The preprint uses q in
exactly four places, all read in full (sections 2, 3 and 5; section 4 read for its use of q, which it states enters
only through the grids and separation):
1. the grids N_b = 2^⌈log₂(c/a_b)⌉, still powers of two, nondecreasing and nested;
2. the stability density, at most 2N_{b'}·2a_{a_e} ≤ 4c·a_{a_e}/a_{b'} ≤ 4c·λ^{g+1};
3. the separation lemma: t·a_n ≥ a_b, and t(a_n − a_{n'}) ≥ (1−λ)a_b > 1/N_b;
4. the scale count: 1 + a_n·N_{b*} ≤ 1 + 2c·κ^{−(b*−a_e)} ≤ 1 + 2c·κ^{−2r}, so the branching condition becomes
   p(M−1)/2 > 2·log(1/κ).
The global deduction (dyadic normalization of the scale) and the open-neighbourhood repair use only a_n → 0.
tests/probes/swarm/ladder/e120/bounded_ratio_check.py replays items 2–4 exactly on 300 random non-geometric
sequences: 0 violations. Not read: the preprint's routing, no-default and density proofs in full detail. Novelty
unassessed: the preprints do not remark on it, and a quick search found no statement of it. It does not touch the
prize case: when the local ratios tend to 0 (for example 2^{−n²}), item 4 needs branching that grows without bound,
and the construction fixes M.

## The Rule30PrizeKit: what the kit has that the record did not (surveyed 2026-10-22, by Cloud; filed 2026-10-23)

The Wolfram Institute's reference Lean environment for the Rule 30 Prize (github.com/WolframInstitute/Rule30PrizeKit,
commit cc1e0e0). The full map against our record is reports/wolfram-agents/MAP.md. New to this record, as prior art
(known, with Lean proofs there): `Rule30Window` (the seed's center column has no period ≤ 4096 with transient ≤ 8192)
and `Rule30FactorWindow` (T + P ≥ 16359); `Rule30WhiteSeed.problem1_black_or_white`; the period-3 reductions
(`Rule30EtherThree*`) and period-4 reductions (`Rule30Ether`, the 109-state wall); `Rule30WhiteRunEight` (the family
0^r 1 1 for r ≥ 8) and Theorem B′ (`1^r u` for eight blocks); `Rule30ZeroBoundaryBarriers` (no finite-abstraction,
local or edge-DFA ranking proves Q01; `no_joint_local_ranking` two-sided); `Rule30Realization.barrier` (rules 90, 150,
210 share left-permutivity and Jen's theorem yet have eventually constant center columns); the 54 equivalent forms of
the period-2 question (CATALOG.md), including the black-wall form and the coupled halves; and the kernel-checked
width-52 result for Q01. Theorem A and the window principle (our §8.54, §8.58, 2026-10-05) are in the kit in a
stronger `orCol` form (`Rule30MaskedJen`, 2026-10-15); our strip certificates and the kit's `certTable` overlap as
PROOFS.md entry 41's dated note says.

### Addendum: the kit's commits of 2026-10-21 to 2026-10-23 and the public submissions page (Cloud, 2026-10-23 07:18 BST)

Checked at the owner's request against the portal's public `submissions.json` (updated 2026-10-23 06:14Z, 12 entries) and
the kit repository at `9679f83` (19 commits after the verifier's `cc1e0e0`, which `api/environment` still names).
Nothing below is on the critical path (Q01/LR); it is filed so the record is current.

- **Two submissions by others, both partial results for Problem 1.** (1) `R30-20261020-81df0e`, Ying Yin with Codex:
  the zero-boundary stripe family with four tail cells, first deviation at depth ≤ m + 6 and depth 1 white within 31
  steps, every class except v = 1011 with m odd (a real exception, m = 33157); Human Verified and ported into the kit
  as `Rule30ZeroBoundaryStripeFour`. It extends `Rule30ZeroBoundaryStripeFamily` (tails ≤ 3), a family of Q01 starts;
  our LR work does not use the stripe family. (2) `R30-20261022-0cac94`, giraudsa with Claude, Gemini and Grok: the
  kit's bit-sliced kernel checker for Q01 generalized to multiples of any period P with a soundness proof; Q001 holds
  up to width 37, Q_5 up to width 28, and the uniform reduction that Q_P excludes (0^{P-1} 1)^∞ as a tail of the
  center column for every P ≥ 2 (new for P ≥ 5 other than 11, 12, 13). Lean Verified, not yet tagged. Period 3 is
  not our lane; the verified-checker pattern is the one a channel-bound soundness bridge would need.
- **Our white end is a Kit Contribution** (`Rule30WhiteEnd` and `Rule30Certificates/WhiteEndChecks`, "Contributed by
  Gareth Herbert with Claude and GPT as Rule 30 Prize submission R30-20261022-c27323, and ported to core Lean"), and
  the skill's example abstract is ours. Seven of our ten are Human Verified (the night's seven); the three of
  2026-10-23 are not yet tagged.
- **New library modules in `equivalents/`, none on our record before this note:** [41] is now proved, Problem 1 iff the
  unit circle is a natural boundary of Σ c(t) zᵗ, through Szegő's theorem for 0/1 sequences with an explicit notch
  polynomial in place of logarithmic capacity (`Szego`, `SzegoContour`, `SzegoPolynomial`); its last step is
  `ApproximateRecurrence`: Problem 1 iff for every monic Q over any normed field the values (Q(σ)c)(n) stay at
  least 1/2 from 0 infinitely often (`problem1_iff_no_approx_recurrence`), a feedback-shift-register argument. [46]
  (Durand–Cobham, not both α- and β-substitutive) is stated, with the sufficient direction for integer bases and the
  uniform case proved (`Substitutive`, `UniformMorphic`), and `PerronFrobenius` and `LinearRecurrence` (primitive
  substitutive sequences are linearly recurrent, Durand–Host–Skau bound) toward it; Durand's theorem itself is
  missing. Almost-sure laws for the fair-coin measure: `RandomNaturalBoundary` (Steinhaus, Paley–Zygmund),
  `MaxOrderComplexity` (M_n = 2 log₂ n (1 + o(1)), birthday paradox), `ErdosRenyi`, `LocalLimit`, `Lines`. The
  catalog counts 163 `problem1_iff_*` equivalences and 48 `problem1_of_*` sufficient conditions.
- **The kit now takes contributions** (README "Contributing a partial result", skill.md 1.14.0 step 6): a core-Lean
  module under `lean/Ruliology/CellularAutomata/`, a row in "Added in the kit", a pull request, and the essay submitted
  with the pull request as its repository. The verifier stays at `cc1e0e0` until it moves, so a later submission
  cannot import a merged module before `api/environment` names a commit that has it.

### Addendum: square-poor binary words and Corollary F's open class (GPT GC1706, second-read by Cloud, 2026-10-23 08:09 BST)

- **Entringer, Jackson and Schatz (1974)** showed infinite binary words avoiding squares xx with |x| ≥ 3 exist;
  **Rampersad, Shallit and Wang, *Avoiding large squares in infinite binary words* (arXiv math/0306081, 2003)** give
  x = g(h^ω(0)) with a primitive 10-uniform h on four letters and a 6-uniform binary g, avoiding every square of root
  length ≥ 4 (their Corollary 6, cited by GPT; the abstract confirms the construction). Cloud's kill test: the first
  600,000 letters of x contain no square of root 4 to 4,000 (roots 1, 2, 3 occur), and every factor of length 50
  recurs within a gap of 1,200, consistent with linear recurrence.
- **What it settles here.** Corollary F excludes a right neighbour iff it has near-squares with some fixed slack at
  unbounded scales (CF). GPT's hand lemma (GPT-CL594-WORDS.md; second-read by Cloud in CL595): a word with bounded
  square root lengths fails CF (two sufficiently separated gaps with the same c-letter closing context G produce the
  square (G X_d)² of root d). So the RSW word, which is linearly recurrent (uniform morphic image of a primitive
  fixed point), survives Corollary F: the door "every linearly recurrent aperiodic word falls to Corollary F" is
  closed, and with it the hope that the kit's `LinearRecurrence` would carry Theorem E to all primitive substitutive
  neighbours. The surviving class is strictly larger than the large-square-avoiding words (GPT's alternating-runs
  control 0 11 000 1111 … survives CF yet has unbounded squares); its structural classification is open.
- **Thue–Morse.** Its squares τⁿ(aa) have unbounded root but occur far from the origin, and CF needs an anchored
  agreement of length j − K, not a square at an arbitrary position (GPT's point); so unbounded squares alone give no
  CF pairs. The record's earlier note that Thue–Morse is not reached by Corollary F stands, and whether it has CF
  pairs at all is open.


### GPT carrying review of CL561 (2026-10-25, GC1845 / MI778)

Bounded-ratio substitution PASS in its stated conditional scope. Full manuscript
sections2–5, including selector/terminal independence, atom-fixed scale
representatives, parameter order and open residual repair read; report
`reports/GPT-CL561-BOUNDED-RATIO-REVIEW.md` carries the argument and PDF digest.
Extension of the cited unrefereed construction, no Lean/novelty/general-prize
claim. Diagnostic grid sizes use floating log2 despite Fraction sequence data;
no replay or universal numerical certificate. Lower ratio bound carries scale
count, upper bound stability/separation. Old CL561 review complete, no new job.


### GPT — phase counts reconnect to the existing half-rate resource (2026-10-28, GC2008–GC2009)

A sustained independent phase-statistic investigation recovered GC1960's already reviewed external1b82d8 half-rate bound. The new short no11011/five-step argument is explanatory and weaker in single-seed scope. Retrieved exact retained Lean source, SHA256 d756d86d454ebdfb47d7fb043435fdb1f2c0d6dfed5f24f9909b207189e43017; read generic Resource/TemporalCycles and the complete concrete WallResource construction. Its arbitrary-start hand parametrization appears to extend the same bound to all finite seeds; not compiled, independently reviewed or submitted here. [Complete scope audit](reports/rule30-five-step-period-bound.md#gc2009--the-generic-scope-check-is-accessible-not-an-excuse-to-wait). Existing [external review](reports/wolfram-agents/GPT-1B82D8-DIAGONAL-REVIEW.md) remains the source of the previously verified headline. No novelty claim for Newton supports, odometers or the external accounting theorem.


### GC2014 — Right-diagonal monotonicity recovered, known and reproved here (28 October 2026)

The older Brunnbauer survey entry is incomplete as a proof reference. The exact single-seed theorem is already
in the retained kit Rule30RightPeriods.lean at pin 5473ffd075f63c9d626e63b8455805d4831b39ca:
Z_down, Z_of_per, halve and per_mono_all. Source SHA-256
ebc46daf6bb8c59f493ddd4b6410b34c9793696905b59b7f7fa65c61f0327680, retrieved and verified from
cited/gc1960-diagonal-dependencies/Rule30RightPeriods.lean. GPT read the carrying steps and restated the
white-triangle descent in [the review](reports/rule30-bounded-period-graph.md). This is known, reproved here,
not a new result or a fresh local compiler verification. Arbitrary-seed monotonicity does not follow directly:
the initial white cone is a single-seed premise. The earlier survey's attribution to Rowland section 5 should
not be used as a right-diagonal monotonicity proof; that section discusses left diagonals.

## Quantum gates, space-time duality and Rule 30 cryptanalysis (Local, L1071, 2026-10-28)

Surveyed by four Local research agents reading primary sources, at the owner's request (GC2030). The full grounding
is [reports/rule30-quantum-gates-grounding.md](reports/rule30-quantum-gates-grounding.md). Items to import:

- **The left damage speed is 0.2428 ± 0.0003** (Grassberger, cited in Wolfram, "Random sequence generation by
  cellular automata", Adv. Appl. Math. 7, 1986, §§3–6). The right speed is exactly 1. Two further points from that
  paper:
  - the left edge is diffusive;
  - on average 0.26 + 0.19 T right-hand initial cells affect a length-T column.

  The record's 0.246 (§8.30, §8.66) is a finite-time measurement of the same speed. Wolfram's 1986 paper also states
  the sideways rewrite and the two-column extension.
- **Meier and Staffelbach (EUROCRYPT 1991).** Seed recovery from the centre column by guessing the right-adjacent
  column, which has low entropy (about 18 bits at n = 300), then solving the left side by left-permutivity. Read
  through Spencer (arXiv:1306.3546) and Mariot (arXiv:2405.02875); the original is paywalled and unread.
- **Koç and Apohan (IEE Proc. CDT 144, 1997; abstract only).** One-step row inversion through the best affine
  approximation, Rule 150, plus corrections.
- **Mariot's 2024 survey (arXiv:2405.02875)** lists the algebraic degree of CA generators as open. L1071 computes
  deg c(t) = 2t − 1 for t ≤ 12 (CONJECTURE).
- **Dual-unitary circuits** (Bertini, Kos and Prosen, PRL 123, 210601, 2019) and their classical analogue (Gombor and
  Pozsgay, SciPost Phys. 12, 102, 2022) need determinism in both space directions; Rule 30 has it only to the left.
  The one-sided consequences hold for Rule 30 (L1071 §3): a memoryless left environment, and correlations only on the
  right light-cone edge.
- **Sfairopoulos, Causer, Mair, Powell and Garrahan, arXiv:2503.19572** (v4, 2026). Plaquette spin models whose
  ground states are CA histories, including Rule 30. The degeneracies count torus orbits or free boundary data, not
  our pasts; the Rule 30 results are perturbative and numerical.
- **Quantum algorithms** (BBBV 1997, Zalka 1999, Montanaro 2018, BHMT 2002) give at most quadratic speedups for our
  search and counting tasks, without certificates. No quantum result bears on Prize Problem 3.

### GC2032 — degree-law review: standard circuit corollary and novelty limit (2026-10-28)

The independently reviewed L1072 theorem concerns the variable-input Rule30 iterate, degree2t-1 for t>=2.
[Find and Boyar2015, p13](https://tsapps.nist.gov/publication/get_pdf.cfm?pub_id=919080) explicitly state the
standard degree-minus-one multiplicative-complexity bound, citing Schnorr1989. Their definitions specify
binary ANDs with XOR and constants. Applied here this gives2t-2 ANDs; it is not a new bound method or a
single-seed indexing bound. Original Schnorr full proof not read in this review.
[Mariot2024](https://arxiv.org/html/2405.02875v1) proposes studying degree/algebraic immunity of CA generators;
this does not establish that our exact iterate formula was open. The Deva abstract already logged in §8.116
claims linear degree growth; full-text comparison remains unavailable and novelty unresolved. Neither its
stronger claims nor equivalence to our exact formula are adopted. See [review](reports/rule30-degree-law-gpt-review.md).

**Degree-law novelty check (Local, L1073, 2026-10-28).**
- *Deva (2026):* Crossref metadata for DOI 10.2139/ssrn.5908722 names the paper "Algebraic Obstruction and Dual-Flow
  Consistency in Rule 30", by Dhashvin Deva, 2026, with no abstract. SSRN is behind a bot check, so it is unread.
- *Burrieza et al. (2011),* "Cryptographic properties of Boolean functions defining elementary cellular automata":
  one-step local rules only.
- *Others:* no iterate-degree result found. The ANF term counts 4, 10, 30, 122, 346, 1360 are not in OEIS. NOT FOUND,
  not NONE EXISTS.

### GC2033 — owner-surfaced arXiv:2610.34096v1, comparison pending (2026-10-28)

Castronuovo, Dennunzio and Margara, [Computing Functions Through the Orbits of Dynamical Systems:
The Case of Cellular Automata](https://arxiv.org/html/2610.34096v1), dated25 October2026.
Not found by identifier/title/author search in the fetched record at056748ee; older work by coauthors is recorded.
Initial reading: introduction, §4.3.7, §5.1, §6.1–6.2 and §7. Function-valued evolution is directly relevant to
our exact-completion observer; §7's generic symbol is our f_t. Detailed comparison with L1072 and our diagonal
results is pending. No exact-degree duplicate established by this first pass; no novelty clearance or independent
validation of the paper's computations. Owner's hidden-structure question remains the active discussion.

**GC2033's arXiv:2610.34096v1, compared with L1072 (Local, L1075, 2026-10-28).** I searched the full HTML text
(about 159,000 characters after removing scripts and maths) for degree, algebraic normal form, monomial, 2t−1,
linear growth and nonlinearity.
- *Degree:* the paper gives one-step ANFs (§2.1). Its §7 defines the generic space-time symbol Φ_t, our f_t, with its
  recurrence and its left-permutive essential dependence on z_(−t). Its only degree statements concern a Rule 180
  restriction (§8.1) and Nersissian's integer-valued polynomial lift of diagonals (§6.2), which is a different object.
- *Verdict:* no statement, proof or computation of the GF(2) degree or top monomial of Rule 30's Φ_t. That makes it
  related prior art for the f_t viewpoint and the function-valued orbit, not a duplicate of the degree law. Math
  elements were stripped for the search, so sentence-level wording was checked, not every formula.

## The degree law is in the kit: `Rule30Equivalents.AlgebraicDegree` (Local, L1077, 2026-10-28)

**Known, reproved here.** Rule 30's t-step map has GF(2) degree exactly 2t − 1 for t ≥ 2, and for t ≥ 3 its top
monomial is unique. Local's L1072 proves this by hand (second-read by GPT, GC2032), and L1074–L1077 prove it in core
Lean. The kit's own `equivalents/Rule30Equivalents/AlgebraicDegree.lean`, added on 2026-10-18 (kit commit cb53064),
already proves it in Lean with Mathlib:
- `isGreatest_card_coef_center`: the degree is exactly 2t − 1;
- `eq_Icc_of_coef_ne_zero`: the unique top monomial, at every cell;
- `coef_evol_eq_zero`: no monomial with max(3, 2s) or more variables at time s;
- `deriv_evol_right`: the white-diagonal derivative (our Lemma 1).

The same module also proves:
- the coefficient of x_0 is c(t);
- balance and Walsh zeros;
- the uniform centre trace (`card_trace`);
- Hedlund window balance (`card_window`).

`QueryComplexity` in the same directory gives a decision-tree depth bound of 2t − 1.

The two proofs take different routes:
- *Upper bound:* the kit telescopes along the left diagonal; ours eliminates pivots from the right edge.
- *Lower bound:* the kit counts by running rule 30 sideways, a bijection to words with an induction on length; ours
  uses real-space recursions.

The record's novelty searches (L1071, L1073, L1075, GC2032) missed it because they did not read the kit's
`equivalents/` catalog. A novelty check now begins with `git grep` over the kit's current main, covering `lean/`,
`equivalents/` and both READMEs. The degree law is not submitted.

## This session's other results, compared with the kit (Local, L1079, 2026-10-28)

After L1077, at the owner's request, each of the session's results was searched with `known_find.py` and then read
against the kit's statements. The portal's listed submissions were searched too, and none matches.

| Our result | Verdict | Where it is known |
|---|---|---|
| L1054: D_d is P-periodic iff π(D_(d−1)) ⊕ π(D_(d−2)) ⊕ π(D_(d−1)D_(d−2)) = 0 | **known**, reproved here | the record's own §8.27 (a running XOR doubles iff its input has odd weight over one period); kit `Rule30RightPeriods.S_rule`, `inp_least_period` (single seed); kit `TFunctionCycles.lift_iff` with `Phi_bit` (every finite row; Klimov and Shamir 2002). Expanding the OR into three parities is a rewrite |
| L1064 §7: the seed echo | **known**, reproved here | kit `TFunctionCycles.Phi_cycle` (every a) and `lift_iff`; for the single seed, `Rule30RightPeriods.row_restart` and `per_iff_gap`, which also hold Proposition 23 |
| The 111 ban on the doubling word | **known** for the single seed | kit `Rule30RightPeriods.no_three` |
| L1064: the 101 lemma, the mod-4 cascade, the universal start, the tree of beginnings; GC2007's 11011 exclusion | not found | they apply the known criterion above |
| L1069: no region strictly inside the light cone sustains itself; self-sustained order is periodic | **related**, shared left-permutivity mechanism, different hypotheses (GC2039) | kit `PeriodicPoints`: exact recurrence at a velocity in [−1, 1) forces spatial periodicity (no gliders). `Odometer.G_bijective` gives the bijection mod 2^W |
| L1071 §3: the left column is a perfect dephaser at the initial slice; correlations only on the right edge | **known**, reproved here | kit `Mixing`: `measure_inter_cells`, `measure_inter_window`, `measurePreserving_cells`, and `measure_diag_eq`, which is GC2032's counterexample |
| L1066: T^64 fixes only ±1/3; Lemma R (light-speed ring orbits) and its census | not found | `Odometer` (already the record's GC808) excludes periodic points from the orbit closures of finite rows. `PeriodicPoints` leaves velocity +1 outside its hypotheses; it does not rule out the ring case |

Lesson: four of the seven rows were already in the kit, and one of those (L1054) was also in our own §8.27. One is
related, and two are not found. What was new sits in the specific evaluations (the 101 lemma, the universal start, the
T^64 classification, Lemma R), not in the general mechanisms.

## The whole record compared with the kit and the portal (Local, L1080, 2026-10-29)

**Method.** At the owner's request after L1079, four read-only audit agents of Local's each took a part of RECORD-MAP.md's
Rule 30 lines (57–394 and 1159–1772). Each searched with `known_find.py` and then read the kit's Lean statements (main
932cf8dd) and the portal's 57 entries. This is a self-check, not a second read. Local checked every verdict below that
changes the record against the kit source: Preimages, Odometer, RightPeriods, Diagonals, ZeroBoundary, CenterFormulas,
and the word families at the submission-time commit. **Dates matter:** the kit's catalog modules arrived on
2026-10-15 to 10-17, and `equivalents/` on 10-16 to 10-18. Everything in RECORD-MAP lines 57–394 (2026-10-04 to 10-15)
came before its kit counterpart, so none of it is a re-derivation.

### 1. Our portal submissions: duplicates found

- **words-A (R30-20261022-5c4fbf) and words-B (R30-20261022-70d23b).** 15 of their 128 words were already excluded
  at submission time, against kit main 681863d of 2026-10-22 and our own c27323:
  - fully, in our scope: `0 1^k`, k = 14 … 17 (`Rule30FiniteBlackRuns.not_eventually_zero_ones`, k ≥ 9);
  - for the single seed and for every nonzero finite configuration: `0^r 11`, r = 12 … 16 (`Rule30WhiteRunEight`,
    `Rule30FiniteWhiteRuns.no_white_run_11_finite`, r ≥ 8);
  - for the single seed: `0^9 101` (`Rule30StripCertificates.not_eventually_000000000101`);
  - by our own white end (c27323, q ≥ 10): `1 0^q`, q = 13 … 17.

  The essays cite the `0^r 1 1` and `1 0^q` families and still count these words as further words. 113 words are new
  outright, and six more are new only in our broader, left-bounded scope. The Lean is unaffected. Notes are in both
  submission READMEs.
- **W2 (Q01 for widths ≤ 56, bound 100)** repeats a check by the kit's authors. The record already knew this (GC1719).
  The upper bound D(52) ≤ 96 is the kit's `q01_width_le_52`, and our witnesses for the exact values are new.

### 2. Re-derived after the kit had it (KNOWN, reproved here)

| Ours | Kit |
|---|---|
| GC1981, GC1982, GC1984: the root's inverse tree has 2, 3 and then 8 rows, and the periodic rays have unique parents | `Preimages.evol_one_eq_iff_of_eventually_white` (exactly two preimages), `…_of_eventually_black` (exactly three), `eq_of_evol_one_eq_of_frequently` (010 far right gives a unique preimage). "No finite predecessor" is a one-line extension |
| L1051, L1053, GC1998: the white-right past continues each right diagonal periodically; c(s) = D_s(s − P); at the first unsupported diagonal the readout is NOT c(B) | `Odometer.ψ` with unique white-right preimages; `Rule30Diagonals.center_eq_R`, `R_periodic`; `Rule30RightPeriods.antiperiod` |
| L1002: T⁻¹(1) = −1 and T⁻²(1) = (100)^∞; the cap formula at u = 2^k − 1 | `Odometer`, `Preimages.evol_one_eq_iff_of_eventually_black`; `Rule30RightPeriods.rows_at_powers_of_two` (the special case only) |
| L951, L953, L954 (Propositions 1, 2), GC1889 (tick cancellation), GC1892, GC1848, GC1867, CL637/CL638 | `Rule30ZeroBoundary`: `small_identities`, `free_not_eventuallyPeriodic`, `tri_odd`, `tri_even`, `Theta_inj`, `two_step_shift`, `zrow_det`, `zrow_pivot`, `Level`, `koenig`, `count_constrained`. Most were already labelled as restatements in the record |
| L973–L974 (equal width), L910 (right-end moves), GC1772's upper direction | `zrow_det`/`zrow_edge`; `Rule30ControlledResponse`; `Q01_iff_bounded`. All three were already credited in the record |
| GC2025: span growth | `Rule30FiniteDiagonals.Rd_zero_succ`, `Ld_zero_succ` |

### 3. Ours first, later also proved in the kit (cite both)

- **§8.100, Rule 30 = the Rule 150 jump XOR AND echoes** (2026-10-14, held as PROOF-SKETCH). This is
  `CenterFormulas.duhamel` (2026-10-18), proved for every configuration, so the identity is now **PROVED (kit)**.
- The kit later proved these too:
  - Proposition 7 (Jen 1986, credited): `Rule30FiniteConfigs.jen`;
  - §8.19, the single 1's two parents: `Preimages`;
  - GC850, the nine-black lock with eight not enough: `Rule30BlackRuns.nine_black`, `eight_black_not_enough`;
  - GC851, the fair-row band: `Mixing`;
  - §8.84, the Jen-type theorem and the barrier lemma: `Rule30DrivenLeft.no_periodic_column`,
    `Rule30ZeroBoundaryStripe`;
  - the chain's implications: `Q01_iff_bounded`, `koenig`, `CQ01_of_Q01`;
  - GC548, the O(n) versus o(n) reading: `Rule30Problem3`;
  - the §8.61 closure: `Rule30ZeroBoundaryBarriers`;
  - GC727, subluminal recurrence: `PeriodicPoints`. The sign convention still needs a check; Proposition 22 itself is
    not in the kit.
- **The kit has only a special or weaker case:**
  - G249: `per_upper`, for the single seed;
  - entry 42: `Ld_periodic`, with the weaker period 2^j;
  - the GC502 bans: single seed only;
  - G256: `golden`, single seed, with a stronger conclusion;
  - LL1–4: `q01_width_le_52`, against our 248;
  - CL088's counts: `evol_one_eq_self_iff`, p = 1 only.

### 4. Related only, not repeats

- S1, Theorem U: a short corollary of `Odometer.agree_G_iff` and `per_iff_gap`. The added piece is ours.
- S3: `two_step_shift` gives the constrained twins; the localization to any tail and any truncation is ours.
- Also related:
  - GC1936 (`back_fin_iff`; portal 8abb51, one day later);
  - L1000's P and GC2019 (`Mixing.evol_flip_front`, a single flip);
  - L1008 (`PeriodicPoints.evol_one_eq_self_iff`);
  - Rule 210 (`run210_eq`, single seed);
  - §8.77, entropy (`Mixing`, log 2 ≤ h ≤ log 3; our 1.347-bit bound is sharper);
  - GC856;
  - §8.85, the lock lemma (`skeleton_0011`).

### 5. Not found

Everything else. That includes:
- the wheel, the kicks and the records R(d);
- the channel bound and the entropy squeeze;
- Theorem B and A‴'s consequence;
- the death-time values above the kit's;
- the c137e0 clock;
- Theorem S and the T² classification;
- the 101 lemma, the universal start and Lemma R;
- the backward-word and trace-certificate results;
- 113 of the 128 submitted words.

**Still to check:**
- the sign convention behind GC727 and Proposition 22;
- the phase alignment of §8.85's lock lemma against `skeleton_0011`;
- Jen 1986's Theorem 4 against entry 42;
- Rowland 2006 against B2;
- the kit's unpublished "round-2 death-time table" against D(2..30).

### GC2095: finite endpoint exceptions — known, reproved here in core Lean

The finite-endpoint/eventual-code argument is already G131/G132 (6October), independently read L085/L086,
and recovered in GC2051's general-arc review. ArcTailBounds now formalizes the elementary transfer:
if c=d after N, RepeatBound(c,q,C) implies RepeatBound(d,q,C+2N); a time shift costs N. It also gives
a classical cutoff for finitely many single-visit labels. This is known, reproved here, not a new novelty
claim or an effective last-visit bound. Intel4.33.1 component passes GC2095; geometric/current-toolchain/
full Rule30 assembly remains separate.

### GC2120: exact fringe matches and recurrence sign correction

At current kit932cf8dd/portal08:42:19Z, [the statement-level comparison](reports/wolfram-agents/FRINGE-RECURRENCE-DISPOSITION.md)
finds PROOFS33's original finite S_r family fully covered by TransformsSeeds.evol_stripeSeed and
stripeSeed_center (literal pattern/column equality, not only equivalent non-EP). Its arbitrary common-left
GC641 extension with white -1 remains a separate candidate. PROOFS34's first-disagreement/tau corollary
follows immediately from AlgebraicDegree.evol_congr and PeriodicPoints.evol_ne_of_ne_left; known, reproved
here, no new standalone submission needed. Mixing's single-flip theorem alone is narrower.

The pending GC727 sign check is resolved: our right displacement s corresponds to kit d=-s. The exact kit
interval is -p<=s<=p-1; velocity+1 and the two supercausal wings are outside it. Thus the middle interval is
known, reproved here; full s!=p is not subsumed by that module. Boyle–Lee Remark2.1 assumes an injective
CA and is related precedent, not an exact Rule30 outer-count certificate. Outer finite-window/count prior-art
scope remains unresolved; no census or formal verification is asserted by this comparison.

### GC2122: the outer recurrence count is a standard feedback-register specialization

Following GC2120's exact sign check, Petrides (2022), section2/equation(1)/Cycle structure
([primary article](https://link.springer.com/article/10.1007/s12095-022-00562-x)) supplies the precise general
nonsingular-register form of PROOFS35(b): a lengthL=|s|+p window shifts and appends dropped-bit XOR a
function of the retained bits. Every labelled window has a unique two-sided orbit, giving2^L labelled rows;
this is not a cycle count or a claim about the full CA's injectivity. The singular outer direction uses the
standard finite stable-image/cycle fact. See [the explicit comparison and final disposition](reports/wolfram-agents/FRINGE-RECURRENCE-DISPOSITION.md).
Known mechanisms, reproved here in the recorded Rule30 hand specialization; no new standalone submission.
Critical s=p and ring classification are untouched. Reopening requires a useful dependency or maintainer request.

### GC2123: prefix-doubling antiperiod — known, reproved here

The bridge lemma antiperiod_of_minimal_double is the standard odd-forcing-parity lifting mechanism:
TFunctionCycles.lift_iff/per and single-seed RightPeriods.antiperiod/e_step. Our explicit PrefixPer/LeastPrefix
form avoids assuming individual-period monotonicity; L1142 has independently carried the actual source and
its application to the already recorded guarded11011 theorem. No new lifting principle is claimed. Kit per
at n bits corresponds to the profile prefix through n-1. Actual current-toolchain compilation remains pending.

### L1143: exact-strip returned bits (GC2026–2028) — corollaries of kit lemmas

The black-wall lock that GC2028 recovered as G.GPT271 is `Rule30FiniteBlackRuns.nine_black` in the kit, for every
configuration. Its "two more sites every nine updates" iteration is in substance `black_shield`. The eight-step
form, when the first right cell starts white, follows from `Rule30ZeroBoundary.col1_five_check` and the
absorbing 01 pair. With left permutivity it gives F^8(x)_8 = a for x[0..7] = a0101010: known in substance,
reproved here. The two-step identity F²(x)_i = x_(i−2) for x_(i−1) ≠ x_i is elementary. In the kit and on the
portal (kit 932cf8dd, portal 08:32Z; terms "two steps", "left permutiv", "black wall", "nine steps",
"returned bit") no matching statement was found in the inspected material. Record-only.

### L1145: reset-track pair restrictions are in the kit

L1040 marked its gap-pair corollary as known from the record (GC503/504). The kit has the same words as well:
`Rule30PeriodTwoWidth6.col1_constraints` forbids the gap pairs 21, 23 and 12, beside 11 and 00000 (the gaps 1 to 4),
and adds the triples 114, 132, 241 and 243. Its scope differs: an eventual statement under a hypothetical eventually
period-2 centre, while L1040's is from age 0 beside the clamped clock, for every right row. The gap bound 1..4 from
age 0 is `Rule30ZeroBoundary.col1_five_check` with the no-11 rule. The portal's R30-20261028-e34744
(`col1_constraints_width6_leftmost`, another team) extends the width-6 words to every configuration with a leftmost
black cell. The four-bit gap function and the explicit tracks were not found in the inspected material (kit 932cf8dd,
portal 08:32Z; terms "reset", "gap word", "forbidden word", "col1_five_check"). They are an organizing hand lemma with
no novelty claim. Record-only.

### L1146: Troy Lowry's earlier public Lean prefix-clock bridge (PR #51 comment; credit wording per GC2127)

Troyusrex2 (Troy Lowry) commented on kit PR #51 at 2026-10-29 04:35Z with standalone checked modules (fork commit
e1ff89b9, `research/right-prefix-clock`). For the actual evolution from any right-bounded configuration, every finite
right-diagonal prefix has a least dyadic period that stays or doubles, and doubling makes the newest diagonal
antiperiodic at the old period. With our shift law this excludes the prefix word 11011 for base exponent at least 2,
and it extends the kit's half-rate bound to every right-bounded configuration. Our GC2118 `PrefixPeriodBridge`
(compiled in L1144) assumes the least prefix periods instead of constructing them, so it is a conditional special
case: known, reproved here. The kit's `Rule30FiniteDiagonals` already gives basic arbitrary-seed dyadic periodicity.
Credit, as GC2127 states it: the earlier public *Lean* prefix-clock proof, its 11011 application and the right-bounded
half-rate extension are Troy Lowry's. The 11011 hand theorem itself is ours (GC2007/L1063/GC2010, public on 28
October), and his comment credits our shift law. The two predicates are not literally identical: ours is a finite
Nat prefix with the recurrence from index 2, his an Int half-prefix with a least dyadic period.

### GC2127: independent PR51 source read and precise credit qualification

[Actual earlier public proof review](reports/wolfram-agents/PREFIX-PRIOR-ART-REVIEW.md) confirms the04:35
comment/edit/frozen-commit times, complete PrefixClock/PrefixBound source and retained57/6,79/6 reports;
no new build or public verifier outcome asserted. Stop additional GC2118 package delivery, known/reproved
conditional interface. The integer half-prefix/least-dyadic predicate is not identical to our finite natural
prefix/minimum-over-all-periods; don't call them literally the same arbitrary-world theorem. The finite-seed
application is covered and the generic lifting calculation is known. Troy Lowry's earlier PUBLIC LEAN
form/application and right-bounded half-rate extension are credited. Our earlier GC2007/L1063/GC2010 public
HAND11011 result remains credited; "first public proof Troy" in the preceding note must not erase that.
Relevant PR discussions/frozen fork source are now an explicit AGENTS pre-work requirement; known_find
coverage documentation names this remaining index boundary. Later06:02/06:44 archives await actual source read.

## Repetition exponents versus an explicit finite deadline (GPT, 2026-10-29, GC2134)

Known, reproved here at the definition level: [Bugeaud–Kim, sections2–3](https://irma.math.unistra.fr/~bugeaud/travaux/complsturm3ndRev1.pdf)
already give rep(x)<=sqrt(10)-3/2<2 for Sturmian words. The record's forbidden repeat is exactly
r(ell)<=2ell-C-2, with r a prefix LENGTH, not an inclusive last index. Thus qualitative violation for each
fixed C is known. A retained single-party compactness proof sketch also yields an unspecified uniform
B(C); it does not yield251(C+4). [Exact dictionary, guards and scope](reports/wolfram-agents/UNIFORM-RECODING-DELIVERY-SCOPE.md).
No claim of novel asymptotic exclusion or current formal certification. The explicit linear horizon and
recoding/reset margins remain pending, not cleared as novel by this comparison.

### GC2151: the DQ-024 forty-level measurement is already published

Rowland, [Local Nested Structure in Rule30](https://ericrowland.github.io/papers/Local_nested_structure_in_rule_30.pdf),
Complex Systems16 (2006), author-PDF page4, tabulates a(k) through40. The kit's last-black-run identity
gives a(k)=J_k+1: all38 overlapping Cloud rows agree; J40=92. Thus the proposed increment forecast is
already answered by published data, not a new computation. Seed-dependent growth is also discussed
in section3. No limit-one-half proof is imported. [Source/accounting audit](reports/rule30-edge-density-account.md).
Known, reproved here: exact10 decrement follows from kit difs_past plus minimal vanishing index;01
resource value is order_of_antiperiod. The universal mechanism is classical cyclic F2 linear algebra.
No new standalone delivery is proposed, and negative searches do not establish priority.

### GC2157: known odometer conjugacy, with classical tree geometry applied explicitly

Known, reproved here at the finite-prefix level: kit932cf8dd Odometer/TFunctionCycles already supply
the actual-seed phase embedding and orbit closure. Coven–Pivato–Yassawi,
[Prevalence of Odometers in Cellular Automata](https://arxiv.org/pdf/math/0511030), Theorem1/proof,
gives the standard finite-column construction. Lyons,
[Phase Transitions on Nonamenable Graphs](https://rdlyons.pages.iu.edu/pdf/review.pdf), section6,
gives tree-boundary dimension/capacity background. These primary carrying sections were read.
[GC2157](reports/rule30-edge-odometer-dimension.md) writes out the homogeneous-prefix and energy
argument with the exact Rule30 exponent dictionary. The critical zero-capacity corollary uses the
existing record-charge upper bound; no density equality, priority or new submission is claimed.

### GC2158: known local gates, explicitly eliminated one ancestor further

Known machinery reapplied here: currentkit932cf8dd Rule30Diagonals.R_step supplies the three
upstream OR equations. The record/kit/portal/PR search and actual delivered101 shift-law read are
retained in the [hand account](reports/rule30-edge-density-account.md#gc2158-one-more-upstream-gate-leaves-choices-only-at-isolated-black-cells).
The011 clause and cyclic component count are elementary consequences written out for the current
run-fill question. They are not separately novelty-cleared or proposed as a delivery package; the
more global101 profile theorem has different period assumptions. Actual-root ancestry remains open.

### GC2159: classical signed-basis argument reused for the retained G134/G135 separation

Known, reproved in a formalization variant: the adjacent unimodular-basis argument already used
in G134/G135 and SharpAdjacentReturn now retains the error's sign to force the exact negative
return directly. Actual floor carries and current-kit932cf8dd Lagrange continuants supply the
arcs, determinant, signs and coefficient-one recurrence. This is dependency preparation for the
existing quantitative horizon, not a new best-approximation theorem or separate submission.
[Carrying proof, source hashes and uncompiled status](reports/wolfram-agents/ACTUAL-CONTINUANT-SOURCE-REVIEW.md#gc2159-exact-opposite-scale-separation-now-has-carrying-source).

### GC2168: explicit-horizon delivery disposition after finite-estimate comparison

Known Sturmian repetition and arbitrary-intercept machinery remains prior art, including the finite estimates
rather than only asymptotic slogans. The [exact comparison and index dictionary](reports/wolfram-agents/UNIFORM-RECODING-DELIVERY-SCOPE.md#gc2168-quantitative-prior-art-disposition-for-delivery)
clears preparation of a credited quantitative formal package relative to the compared exports, with no
first-in-literature or sharpness claim. Full release/checker/artifact validation remains required.

### GC2170: common-left fringe trace is a known StripeMeeting specialization

Current kit932cf8dd StripeMeeting.stripe_related_same_trace already allows arbitrary common high bits
beyond its white separator. The [reflected cut and causal-truncation argument](reports/wolfram-agents/FRINGE-RECURRENCE-DISPOSITION.md#gc2170-common-left-trace-extension-is-covered-by-stripemeeting-plus-locality)
resolves the common-left center-trace candidate, including infinite tails observation by observation.
Known, reproved here at the interface; the stronger moving wedge remains the original hand corollary.
No new standalone submission or trace-completeness claim.


### GPT — Rote parity lifting actual-source comparison,29 October2026 (GC2183)

Read section4/Theorem3 and its Theorem4 proof in
[Rote's original paper](https://page.mi.fu-berlin.de/rote/Papers/pdf/Sequences+with+subword+complexity+2n.pdf),
plus the [author's errata](https://page.mi.fu-berlin.de/rote/Papers/abstract/Sequences%2Bwith%2Bsubword%2Bcomplexity%2B2n.html).
The Sturmian derivative/cumulative-parity relation and offset-parity explanation are known, rederived here.
Read actual Lemma3.7 and Theorem3.10's statement/written SU-case proof in
[Medkova–Pelantova–Vuillon2019](https://numdam.org/item/10.1051/ita/2019004.pdf): stable-prefix parity filters
occurrences; three return-word forms require an associated standard Sturmian derivative. This goes beyond our
old abstract-only record without claiming a full-paper audit. It does not yet equate their guarded prefix-return
formulas with G144's all-factor initial-repeat bound. See UNIFORM-RECODING-DELIVERY-SCOPE.md GC2183.


### GPT — complexity proof of Rote/window separation,29 October2026 (GC2186)

Known, reproved here: Rote's classical derivative theorem (actual source in GC2183; also2019 Proposition2.4)
gives p_c(n)=2n. A width(w+1) block map of a Sturmian word has p(n)<=n+w+1, contradicted at n=w+2; a rational
mechanical input gives a periodic output. This already separates cumulative-parity generation from any fixed
window representation. It needs neither the new251 horizon nor G143's special repeat-debt proof. No additional
submission/novelty claim. Detailed derivation in UNIFORM-RECODING-DELIVERY-SCOPE.md GC2186.


### GPT — finite-prefix invariance of the first-repeat exponent,29 October2026 (GC2189)

Known, reproved here: Bugeaud–Kim's [primary paper](https://irma.math.unistra.fr/~bugeaud/travaux/complsturm3ndRev1.pdf),
last paragraph of section2, printed p5, gives r(n-1,x)+1<=r(n,ax)<=r(n,x)+1. Iterating proves that rep is unchanged
by finite shifts/prefix alterations. This is background for the quantitative G145 half-phase consequence, not new
symbolic dynamics or portal material. [Exact calculation and qualifications](reports/wolfram-agents/UNIFORM-RECODING-DELIVERY-SCOPE.md#gc2189-the-carried-half-phase-witness-already-gives-a-relative-first-repeat-gap).


### GPT — new public finite-defect and corrected zero-thread statements,29 October2026 (GC2191)

Full public99db76 and23ac1b Lean sources read,253/484lines, fresh16:04:33Z index at kit932cf8dd. Both externally
Lean Verified,37/136replayed, no GPT replay. 99db76 explicitly supersedesf98be4 and matches its earlier read proof
after inert CenterDot decoding. Its physical zero-thread exclusion was already compared to8084e6 at GC2183.
23ac1b gives an explicit zero-center finite-defect frontier and a center-blind support exclusion. Known kit
Rule30FiniteConfigs.no_column_eventually_constant_finite already excludes the physical eventual-black-neighbour
premise without the defect restriction; standard finite propagation gives the corresponding abstract support
comparison. This does not assert an identical kit numeric-frontier export or dispute its actual formal proof.
[Exact scope and hand seam read](reports/wolfram-agents/UNIFORM-RECODING-DELIVERY-SCOPE.md#gc2191-two-current-public-finite-support-proofs-do-not-replace-the-quantitative-horizon).
No change to the accepted quantitative horizon delivery scope or prize status.


### GPT — positive Diophantine-exponent match for the unbounded rotation case,29 October2026 (GC2193)

Known, reproved here: Nguyen, [Spectrum of the refined Diophantine exponent, v2](https://arxiv.org/html/2608.20191v2),
Theorem7.4, and Bugeaud–Kim [Lemma10.3](https://irma.math.unistra.fr/~bugeaud/travaux/complsturm3ndRev1.pdf)
already cover GC2187's unbounded-digit rep=1 subcase at every phase. The exact half-circle identification,
bounded-type scaling proof, source-reading scope, refined-versus-ordinary guard and retained document digests
are in [the full disposition](reports/wolfram-agents/UNIFORM-RECODING-DELIVERY-SCOPE.md#gc2193-exact-repetition-is-classified-at-phase-zero-but-one-error-admits-arbitrarily-long-near-cubes).
The sharper phase-zero rep=2 classification is now hand-carried L1192, but its exact prior-art disposition remains
unresolved. No additional posting decision or novelty claim. The one-error near-cube consequence is a separate
PROOF-SKETCH, not an infinite approximate-repetition theorem inferred from finite data.


### GPT — actual2020 critical-exponent match for the silver language,29 October2026 (GC2194)

Known silver cube-freeness now has an actual primary-source/convention comparison in
[GC2194](reports/wolfram-agents/UNIFORM-RECODING-DELIVERY-SCOPE.md#gc2194-the-one-bit-repair-has-an-exact-endpoint-cube-freeness-is-a-known-separate-constraint).
It supersedes the7October abstract-only reading scope. The anchored classification remains a different unresolved
prior-art disposition; generic searching is parked with a named-source reopening condition.


### GPT — CL642's parity rules are known cycle identities,29 October2026 (GC2201)

Known, reproved: actual kit932cf8dd Rule30RightPeriods.S_rule, antiperiod, half_black and per_mono_all give
CL642's single-seed Case A/B and even-tick identities. [Exact carrying scope and boundary guards](reports/wolfram-agents/RIGHT-PROFILE-DELIVERY-SPEC.md#cl642-case-ab-carrying-read-with-explicit-period-conventions).
Prefix-cycle parities for arbitrary seeds must keep their stated cycle length. Cloud's numerical outputs and
runtime enforcement are not independently validated by that hand read. No separate submission or novelty claim.

### GPT — constant-tail inverse classification recovered in a4691a (29 October2026, GC2206–2207)

Known mechanism, reproved/formalized in the source: G122/G141/GC691 already give the zero/one/period-three inverse-tail graphs. The new portal a4691a supplies explicit front-boundary inverse operators and finite-width clone criteria; those boundaries differ from our free-neighbour wall inverse. [Exact source, PR45 comparison and scope review](reports/rule30-primitive-source-review.md). Do not reclaim the tail trichotomy as a new discovery. Its primitive/survivor conjunction retains the future-survival predicate, and low-width orbit projection alone does not transfer the larger mortality certificate. The elementary count uses G121's injective-image principle; no separate priority claim.

### GPT — the proposed forbidden3/5-gap search was already in the record (29 October2026, GC2208–2209)

Known, recovered: L323 already lists SSLSSLS among11 seven-gap exclusions (8October); L590 gives two exact42-symbol cuts, GC1009/1011 their recurrent macro/startup interpretation, and SLC records83 further cut certificates. [Sources and exact comparison](reports/rule30-clocked-gap-interface.md). The current published width-14 graph rejects the same SSLSSLS in one bounded control, but accepts both L590 cuts. This corrects SYNTHESIS3.5/5.2's claim that no forbidden gap words had been written. Historical SAT/cake_lpr outcomes remain inherited; no rerun or new mathematical priority claim. The phase/boundary transfer is a separate solo hand sketch.

### GPT —00 phase law reuses the known cycle lift and one-bit delay (29 October2026, GC2210–2211)

Known, reused: kit932cf8dd TFunctionCycles.Phi_bit/lift_iff/Phi_cycle and GC2014/L1070's delayed one-bit parity identity. [Two-bit conditional expansion](reports/rule30-zero-pair-phase.md) adds an elementary phase/closure calculation; no priority claim or independent carrying acceptance yet. Anashin–Khrennikov–Yurova1111.3093 section2.4.1 supplies classical triangular-coordinate background, with whole-space bijectivity/ergodicity hypotheses distinct from the single seed's depth sequence. The pointed-to differentiability-mod4 literature is a new reading target, not an imported theorem.

### GPT — the adjacent-coordinate theorem's regularity hypotheses matter (30 October 2026, GC2212)

Shi–Anashin–Lin1111.4635 was already cited abstract-only in the overlooked-CA survey. Definitions 2/4/5 and Theorem 5 are now read in primary full text: the coordinate relation needs transitivity and uniform differentiability modulo four. [The actual-map calculation](reports/rule30-edge-regularity.md) gives a solo sketch of Phi's exact pointwise regularity and shows this direct transfer fails. Classical definitions and the modulo-two isometry fact are known; no first-in-literature claim for the elementary specialization, and no theorem about single-root density imported.

GC2213: the return quotient telescopes to exactly GC2014/L1070's known phase coefficient. The fixed-iterate obstruction uses the current kit's `OrbitSignalizer.log2_Phi` and `log2_iterate_Phi`, whose complete proof bodies were read. New consequence remains a solo sketch without priority clearance; it is not a new all-period or density theorem.

### GPT — PR57 arbitrary-driver transport and conditional prize bridge (30 October 2026, GC2214)

[Complete carrying review](reports/rule30-periodic-mask-review.md) of public PR57 head37f8d755/source93c1847f, with exact linked canonical inputs/evidence. The masking observation is already MaskedJen; PR57 supplies the arbitrary-driver iff and conditional bridge. Its open exclusion is not proved. The solo deletion-of-isolated-pulses consequence is an elementary use of this prior art, with no priority claim. G231's differently indexed effective-input lemma does not supply this driver reduction.


### GPT — reset language and finite-tail test reused with PR53 (30 October 2026, GC2216)

Known, reused: G13's exact synchronizing factors0 1^(3m+1) 0 z; G141's clamped-wall finite-tail test and5/6->13 merger; official kit932cf8dd ZeroBoundary.back/eq_back/back_fin_iff. [Full PR53 source/evidence review and elementary consequence](reports/rule30-reset-free-review.md) carries the external sharp three-row reset law and five-row tail theorem. The solo exact-one-predecessor characterization and its branching corollary have no novelty clearance; whole-line finite injectivity is a different boundary statement. No duplicated submission, fresh replay or claimed literature priority.


### GPT — boundary-specific preimage counts use classical transfer methods (30 October 2026, GC2218)

Known machinery, reused: Erica Jen, [Enumeration of Preimages in Cellular Automata](https://content.wolfram.com/sites/13/2018/02/03-5-2.pdf), Complex Systems3(1989),421–456, section2 endpoint recurrences and section4 Rule30/45 case, printed434–435. Those portions read; not a full-paper audit. Unrestricted n+2-to-n preimages, cyclic fixed points and finite zero-wall parents are different boundary counts. Actual kit932cf8dd `predCount_eq_one_iff`, `numWithPreds_weighted` and `numWithPreds_zero` read against the [new elementary zero-wall count](reports/rule30-reset-free-review.md#gc2218-the-fixed-control-passed-exact-finite-word-counts-by-hand). The recurrence and limiting3/4,0,1/4 word proportions are solo PROOF-SKETCH; no novelty clearance, root-frequency conclusion or new submission. G121's3/4 normalized whole-line root count does not by itself prove this clamped-wall result.


### GPT — approximate periodicity already uses residue-class consensus (30 October2026, GC2219)

Known, reused: Amir–Eisenberg–Levy, [Approximate Periodicity, author full text](https://www.researchgate.net/publication/221544033_Approximate_Periodicity), Definitions6/9 and Lemmas1–2: fixed-period Hamming repair uses the most frequent symbol per residue class, while one substitution can change two shifted comparisons. Relevant definitions/proofs read; not a full-paper audit or exact hosted-version claim. El Ghazi–Starikovskaya's [ISAAC2025 section2.1](https://drops.dagstuhl.de/storage/00lipics/lipics-vol359-isaac2025/html/LIPIcs.ISAAC.2025.36/LIPIcs.ISAAC.2025.36.html) uses shifted mismatch count, a distinct observable; only definitions/introduction read. [GC2219](reports/wolfram-agents/UNIFORM-RECODING-DELIVERY-SCOPE.md#gc2219-two-substitutions-have-an-exact-endpoint-set-by-a-residue-chain) applies the known consensus criterion to the carried silver mismatch formula. Its exact two-edit endpoint is solo PROOF-SKETCH without novelty clearance.


### GPT — uniform window accounting is a restart of the known Path (30 October2026, GC2220)

Known machinery, reused: kit932cf8dd Rule30RecordCharge.Path/record_potential/exponent_bound_before_threshold and Rule30RightPeriods.pairPath. The Path has no resource(0) condition, so the [shifted-window proof](reports/rule30-edge-odometer-dimension.md#gc2220-the-known-accounting-bound-restarts-in-every-spatial-window) is an elementary restart with parameter nu+E(a), not a new half-rate mechanism. PR55 already uses the same accounting for general right-bounded prefixes. Banaji–Rutar–Troscheit, [Interpolating with generalized Assouad dimensions](https://pmc.ncbi.nlm.nih.gov/articles/PMC12255623/) (2025), equation1.1 and section2.1 Proposition2.1/proof read for classical local-cover background. The direct cylinder proof gives a solo dim_Assouad(K)<=1/2 specialization; no priority claim, independent carrying read or lower bound.


### GPT — PR48 edge-clock restrictions and arbitrarily long finite imitations (30 October2026, GC2222)

[PR48](https://github.com/WolframInstitute/Rule30PrizeKit/pull/48), head865e77a5d11a, source4112e112: all374 lines and its exact linked source/evidence archive carried independently. [Review and retained identities](reports/rule30-edge-clock-drop-review.md). The period/antiperiod/period prohibition and constant-column white-prefix theorem agree with earlier mechanisms in rule30-doubling-word4–5. The explicit free carrier and finite odd seeds give arbitrary finite imitation of a period8/period2 pair, not an actual all-time drop. Credit the external formal interfaces; do not recreate them. Author99-constant/13-headline validation inspected, no GPT replay. The retained first-deviation pattern remains finite/unproved.

### GPT — carrier and guarded-front methods precede the exact lifetime sketch (30 October2026, GC2223)

Known, reused: L1066's period-eight0001/0111 ring carrier, PR48's exact carrier/exit and finite seeds, and kit932cf8dd `Rule30EtherThreeErosion.front_step`/`wake_good` and `Rule30ZeroBoundaryStripeFront.win_step` as guarded-front methods with different backgrounds/coordinates. [GC2223](reports/rule30-carrier-invasion.md) supplies a solo four-tick/six-depth invariant and exact lifetime for PR48's family, not a new carrier or a claimed general front theorem. Rasolonjanahary–Vasiev2020's [primary discussion](https://pmc.ncbi.nlm.nih.gov/articles/PMC7304752/) concerns finite-chain stripe formation and stationary four-periodic rows; the compared statements do not carry this moving period-eight lifetime. No exhaustive novelty clearance or submission.

GC2225 scoped hypothesis check: actual kit ClockMask requires temporal clock hypotheses, PeriodicPoints whole-row recurrence, and Lines a random almost-everywhere setting. Portal0ef9c8's headline assumes a full finite-state D^32 return;4d375d's clock map is different. Primary [Kopra2202.13809](https://arxiv.org/pdf/2202.13809), Definition2.4/Theorem3.5, requires the original rule's left-zero start and trace hypotheses. None was imported into the [four-tick/six-depth sampled guard problem](reports/rule30-carrier-invasion.md#gc2225-exact-guard-map-and-the-remaining-capture-question) without a bridge. These are definition/headline comparisons, not fresh complete carrying reviews or a novelty clearance.


### GPT — group flat connections and a known singular ring recognizer (30 October2026, GC2229–GC2230)

[PR58](https://github.com/WolframInstitute/Rule30PrizeKit/pull/58), exact head70ca1830 and linked archive87ba7661, supplies the carried finite-support group-gauge theorem and boundary countermodel. [Source/evidence review](reports/rule30-group-cocycle-review.md) accepts only their stated homogeneous invertible scope, with no general invariant classification. The archive's first singular matrix example is already identified there as the alternating-ring recognizer; known, reproved here by matrix units and uniqueness of the alternating row's preimage. The current kit's PeriodicPoints.evol_one_eq_self_iff separately classifies all fixed rows, not all their preimages. Neither theorem is silently substituted for the other. Parry1997 exact comparison awaits full text; abstracts are insufficient.

PR55 head918284e3 and the old GC2012 period-eight graph already provide finite-profile realization and the seed93 path. [GC2230](reports/rule30-profile-boundary-control.md) spells that path out and uses it as a boundary scope control for PR58, not a new realization theorem or seed search. The unrestricted-past countermodel does not refute uniqueness between two white-rooted histories.


### GPT — the full-line four-return conclusion is known, reproved by local words (30 October2026, GC2231)

Known, reproved here: G258's universal00100/11011 ban, GC732's exact two-step white/rain/interface law, and the retained complete unrestricted q4 profile core. [GC2231's short hand reproof](reports/rule30-full-line-small-clocks.md) eliminates primitive-four profiles by the next neighbour's odd forcing parity. The hand argument is solo PROOF-SKETCH; the pre-existing finite result is not upgraded or relabelled as a discovery. Lemma R and GC759 supply the known ring/path and finite-graph pumping machinery. Actual PR48/PR55/PR58 source scopes and kit932cf8dd PeriodicPoints velocity hypotheses were compared. Ring-only tests do not classify higher-clock transient paths. No new census, centre-column exclusion, novelty clearance or submission.


### GPT — finite return-eight criterion and two-run shape corollary (30 October2026, GC2232–GC2233)

Known, carried: [PR33](https://github.com/WolframInstitute/Rule30PrizeKit/pull/33), exact d34b305b/09aa298b source, gives whole finite eight-return iff two-return after removing three newest cells. [Full review](reports/rule30-finite-return-eight-review.md) distinguishes the current reported128-constant replay from the older retained26-constant replay. No recreated submission or safety-completeness claim.

Known machinery, reused: GC798's exact two-equation projection and G258's universal word bans. The [even two-run doubling deduction](reports/rule30-full-line-small-clocks.md#gc2233-an-even-two-run-profile-forces-the-next-period-to-double) is solo PROOF-SKETCH with no priority claim. GC821/G261 require a different proper-odd-period/joint-period condition, and delivered TemporalProfiles.heavy_source_two_runs concerns a left-diagonal pulse-source weight. Exact hypotheses read. Fresh kit932cf8dd/portal04:17:45Z/23openPR source index is unchanged. No broad literature exclusion, root occurrence or generic00 law is inferred.


### GPT — signed-event height equivalence carried (30 October2026, GC2234)

Known, carried from the exact linked0cbc49ef research sources RootEventHeight c3e09248 and RootOrientedHeight a1c5f671: safety is equivalent to correctly oriented two-level signed height of both-white driver events. [Full calculation and evidence review](reports/rule30-oriented-height-review.md). The event-time odd-gap formulation is an explanatory rephrasing, not a new root theorem. No finite-white ancestry restriction or new submission follows. GC2235 only prepares the Boolean part of GC2233 in core Lean; current-kit integration and independent carrying read remain pending.


### GPT — finite reset-excursion counterexample carried (30 October2026, GC2237)

Known, carried: immutable0cbc49ef ResetExcursionControl e9cf39dc, [full scoped review](reports/rule30-reset-excursion-review.md). Two finite white-boundary rows share eight newest outputs and a returning newest000 triple while a parent bit differs. Both traces start00, so the witness concerns finite-excursion decoding and not the conditional safe-output bridge or ReturnComplete. Six-constant author replay retained; no recreated computation or submission.


### GPT — run-map corollary and transition-cover obstruction (30 October2026, GC2238–GC2239)

GC2238 is a conditional [shape-based reformulation](reports/rule30-run-period-law.md) of known accumulator/input parity, using GC798 and elementary OR-dilation/AND-erosion. Actual current kit932cf8dd Rule30RightPeriods.inp_least_period/S_rule already supplies the broader root input law; no claim to discover that rule or a density. Rowland2006's general2-times-joint-period bound is credited in its own scope.

GC2239 independently carries the existing [CedarTCObstruction theorem](reports/rule30-transition-cover-review.md), source2137d6db: every nonzero dyadic word has a normalized reversed-derivative TC chain. Known kit DifferenceOrder.difs_two_pow/vanish_of_period supplies the same annihilation mechanism. Its failure to assert shared Rule30 ancestry is explicit in the original source. The small hand incompatibility control explains that distinction; no new package or novelty claim.


### GPT — antiperiod-height necessity and a scoped constructive converse (30 October2026, GC2242–GC2243)

Known, independently carried: immutable0cbc49ef RootAntiPeriodHeight513de31a, [exact source/evidence and comparison](reports/rule30-antiperiod-height-review.md). The signed projection, diameter2 necessity and zero drift are the external author's results. GC2243 adds a solo elementary two-binary-track construction for the different existential quantifier, choosing the antiperiodic partner. No prescribed-partner/ancestry converse or priority claim; independent carrying read and further prior-art clearance remain pending. The nearby CedarD3Converse concerns finite-word completeness and is not this statement.


### GPT — counting the freely chosen partners (30 October2026, GC2246)

The [excursion-label count](reports/rule30-antiperiod-height-review.md#gc2246-count-all-free-partners-by-excursion-choices) refines GC2243's free-partner construction, using the already-carried external signed-height/orientation identities. It counts phase-anchored partners in that relaxation, not actual Rule30 predecessor histories. Elementary binary-path/parity counting is credited; no first-in-literature claim or novelty clearance. Independent carrying review remains pending, and finite retained-data agreement is separate evidence.


### GPT — standard strip counting applied to free-partner drivers (30 October2026, GC2247)

[Exact scope and source comparison](reports/rule30-free-partner-language.md). Known, specialized here: Krattenthaler's author-hosted Lattice Path Enumeration10.11.1 and proof, printed630–631, give weighted bounded-Motzkin transfer matrices. Loop weights2 below the top and1 at the top encode paired even/odd white events; inclusion-exclusion gives the driver count. Kit932cf8dd's EtherTrap word_lemma and ProductParity/LocalConservation balanced_gradient concern other closed-walk assertions, as read. RootAntiPeriodHeight remains credited for necessity. No new general counting method, priority claim or novelty clearance; the application and growth consequence remain solo PROOF-SKETCH.


### GPT — D3 and finite-word safety completeness (30 October2026, GC2248)

Known external result, independently carried in scope: [RootD3Reduction/CedarD3Converse and dependency audit](reports/rule30-d3-completeness-review.md), immutable0cbc49ef. The equivalence is proved; its two completeness assertions remain open. Existing short-extension and reader results are credited, with529retained author replay declarations across two checkpoints. This recovers linked fork material beyond the portal index, not a new submission or completeness theorem. The delayed unsafe pair of1000010 is an inspected author certificate branch, not a new experiment.


### GPT — PR52 arbitrary-future closing and conditional reduction (30 October2026,GC2250)

Known, independently carried in scope: [source and complete canonical archive review](reports/rule30-gate-past-closing-review.md), PR52head64003389/archive48a2173d. Finite4–7past closing, finite-prefix checker soundness, exact support preservation and conditional all-length exclusion belong to the external author. The10bit/200rate counterexample does not refute eventual closing. No new submission, priority claim or inference from COMPUTED12 to kernel7. Completeness of the finite-cover format is the next scoped hand question, not asserted here.


### GPT — compactness completeness for the PR52 cover format (30 October2026,GC2251)

[Scoped solo proof](reports/rule30-gate-past-closing-review.md#gc2251-the-finite-cover-format-is-complete-for-qualitative-closing). Standard finite-tree/cylinder compactness is applied after kit zrow_local converts row-tail agreement into PR52's finite absorbing pair. G129 and kit ProfiniteIntegers.exists_level already use related compactness with different hypotheses. Boyle–Kitchens section2/printed3 supplies classical closing finite-window context; its factor-map theorem is not directly applied. Exact finite-cover completeness is a solo application, not a new compactness method or cleared-priority claim. The source's all-length closing hypothesis remains open.

### GPT — carrier endpoint and infinite extension distinguished (30 October2026, GC2253)

Known mechanisms, exact scope corrected: PR48 carrier_exit/arbitrary_older_context supply a finite spatial8-to2drop; the known odd-forcing parity rule then forces16next for that endpoint. PR58's retained q8 witness uses the opposite alternating exit phase and extends to rain. [Hand comparison and failed control](reports/rule30-carrier-reach-pilot.md#exact-hand-diagnosis-and-the-other-exit-choice). Urías et al.1996 sectionV, Lemma5/proof/following theorem now read in the author-linked full text; its strict end-resolving velocity hypothesis excludes our critical moving-edge frame. Neither source yields the proposed all-clock classification.


### GC2258 — known AND domino and clock machinery, reproved here (30 October2026)

[Skirrow's original author notes](https://oeis.org/wiki/User:Natalia_L._Skirrow/on_nearsighted_binary_counters), Theorems1–2/Corollary3, give regular-block AND dynamics. The n=2 closed form and logarithmic prefix clocks are known, reconstructed in [the comparison account](reports/quadratic-edge-clock-transfer.md#5-a-known-exact-and-comparison-the-two-cell-seed). These are author notes, not an asserted referee/Lean certificate. The Newton multiplication calculus is also known (Nersissian and GC2008). Kit a6399ef1 Rule30DifferenceOrder/RecordCharge and PR55 at918284e3 give the OR proof mechanism; GC2258 proposes a scoped all16gate transfer, not priority for the underlying method. The affine bound is standard nilpotent-matrix linear algebra. No novelty conclusion follows merely from the search.

### GC2270 — known support and reset machinery, reproved in the question pass (30 October2026)

[Nersissian2609.25077](https://arxiv.org/html/2609.25077v1), sections2.1–2.3 and4.1 read: Newton/Lucas multiplication and the left reset/integration mechanism are known, reproved here. The antiperiodic top-support lemma is an immediate consequence of the Theorem1 argument; its next-letter corollary needs a small-period correction. No new basis method is claimed. [Scoped comparison](reports/cloud-question-workflow-20261030.md) uses kit a6399ef15ff409d4dc0c5feb119b289aa31588a4, actual TFunctionCycles/FiniteConfigs/DifferenceOrder/RecordCharge sources, delivered0616de and prior four-state inverse constructors. PR60atdb6e71128339 was fully read and retains its synchronization/RowClosing hypotheses; it does not prove arbitrary-root backward closure. The new choked-gate restriction and finite-depth branch consequence are solo specializations, not cleared-priority claims. Optional Parry comparison remains parked.

### GC2272 — finite outside-edge imitation is known realization plus locality (30 October2026)

[Scoped argument](reports/cloud-revised-questions-review-20261030.md#gc2272-two-immediate-answers-in-the-revised-list). Known, reproved here: kit a6399ef1 `Rule30Realization.evol_conf`/`realize` supplies the white-right infinite realization of0101...; radius-one locality preserves its finite trace after truncation. Source da6444504fc3d9789ccdae0f042f63e980b6f0de1ce23958d5387e6d4999eac5, complete carrying proof read. This is not a new finite-row exclusion. The backward3*2^e family is an immediate induction from GC2261 E2, not the misquoted all-period ring classification. The late-halving/channel-transfer obstruction was already recorded in GC1867/GC2146 and does not become a new proof by calling entropy refill.

## GC2276 — the relay patch is known ether; the stop is a known word (30 October2026)

[Application and source hashes](reports/rule30-relay-witness-audit.md). The seven-cell four-phase cycle is exactly current kit Rule30Ether.ether_rule/ether_period, also Rule30PeriodTwoCoupled.c7_eq_ether; known, reidentified here, no new periodic-orbit claim. The finite repair101->100 is already GC1940/L1004. Target010101001 is excluded by the finite-language certificate for101001 used in GC1023, GC1196/L681 and GC1945/GC1951; known, reapplied here. The extra finite enumeration corroborated a known exclusion and should have been avoided by a literal factor screen. The new scoped application is the fixed-left optimum17, still awaiting independent transfer review.


## GC2282–GC2283 — finite physical past is known; the new defect budget has a precise scope (30 October2026)

[Exact comparison](reports/GPT-PROOF-DELIVERY-RESUMPTION-20261030.md#gc2282-package-b-has-an-older-reviewed-core-and-a-precise-formalization-gap). Known, reproved here: G121/G122 (Local L077,6October) already give the finite root/age/count structure and first backward tails. Current kit a6399ef1 Preimages exports stronger right-asymptotic injectivity and canonical inverse classification; FiniteConfigs/FrozenRuler provide endpoint growth. Package B would formalize credited wrappers and consequences, not discover these ingredients. Wall-frame, decoration and stripe-map parent notions are distinct. The later count's solo label was a record-recovery error, now corrected.

[New PR61 source comparison](reports/GPT-PROOF-DELIVERY-RESUMPTION-20261030.md#gc2283-new-pr61-black-clock-budget-and-its-exact-scope): head17098426, public source b278d4f5, source-carried four-layer escape and retained author47constant/5headline replay. Its non-additive rank may stall on white ticks and is not ruled out by earlier strict/additive obstructions. Linked sources prove the ACC exclusion but retain a controlled five-digit trap satisfying two lower recurrences; no anchored counterexample or arbitrary-band escape. Known external work, with review/replay limits retained. No duplicate theorem or submission.


## GC2289 — known solid-block collapse and finite period-three parents, reapplied (30 October2026)

GC544 already computes the three-cell image of a finite solid interval. G122/GC593, carried by Cloud CL058, constructs finite equally spaced-by-three parents of solid intervals and then the three-cell image, with the left-two-black invariant explicit. Current kit Preimages.leftPair/extendLeft and G122/L077 give the three-state inverse cycle. These are known, reapplied in [GC2289's fixed-mass age consequence](reports/GPT-PROOF-DELIVERY-RESUMPTION-20261030.md#gc2289-at-three-black-cells-finite-ancestry-has-depth-at-most-two). The new full three-black classification/count is a solo consequence, not cleared-priority work or a new submission candidate. The portal196859 black temporal-tail padding result concerns a different interface.


## GC2290 — finite ancestor and age already have 2016 OEIS records (30 October2026)

Known, reproved/formalized here: Antti Karttunen's [A269160](https://oeis.org/A269160) records the finite integer Rule30 map, injectivity and width growth; [A269162](https://oeis.org/A269162) its partial finite inverse; [A269163](https://oeis.org/A269163)/[A269164](https://oeis.org/A269164) its image/complement; [A269165](https://oeis.org/A269165) and [A269166](https://oeis.org/A269166) the earliest finite ancestor and its age. A269165 explicitly reconstructs a word by iterating its ancestor for that age. All those primary entries were read, not just search snippets. This corrects the missing external attribution in Package B's earlier comparison: G121/L077 supplied our carried proof, not priority for the objects or decomposition. A269160 had already been cited elsewhere in this record without following these ancestry links. The count wrappers remain useful formal preparation, all UNCOMPILED; no claim about the historical priority of the exact count. [Full comparison](reports/GPT-PROOF-DELIVERY-RESUMPTION-20261030.md#gc2290-normalized-source-actual-counts-and-older-external-provenance).

GC2291's four-black age classification is an explicit solo application of the known inverse pair map. Actual current-kit SparsePreimage is a strip-certificate accelerator, PaddedWords' four-black theorem is temporal, and DividedDifference's four-cell example is an auxiliary linear mode. None identifies the physical finite-ancestry statement merely by sharing a keyword. A new priority claim or submission decision would still require the full current comparison and independent carrying read.


GC2314, 30 October 2026: **known, reproved here** — triangular fresh-bit maps preserve the uniform finite cube.
Actual kit main7beff71c `RandomConfigurations.measure_triangular` already proves the general event law; its full
hypotheses/body were read. The fair-binomial CLT is already `tendstoInDistribution_count`. The
[finite-image boundary account](reports/rule30-two-step-finite-past.md#gc2314-every-fixed-ancestry-depth-has-a-binomial-bulk-and-finite-boundary-corrections)
uses these standard mechanisms under finite normalized endpoint conditions, and distinguishes its new solo boundary
accounting from classical probability tools and the kit's infinite temporal trace. Kari's balance tutorial and the
Kari–Taati abstract are credited there in their actually read scope. No priority claim or Parry dependency.


GC2321, 30 October2026: **known, reproved here** — distinct nonzero linear Boolean forms give pairwise independence
(Vadhan §3.5, Construction3.18/Proposition3.19), triangular permutive maps preserve fair product measure (actual kit
`RandomConfigurations.measure_triangular`), and Doob conditional-expectation increments are orthogonal (Oveis Gharan
Lecture9 §9.1). The [Bipermutive boundary control](reports/rule30-two-step-finite-past.md#gc2321-a-bipermutive-control-isolates-the-missing-boundary-estimate) supplies a finite normalized-endpoint application and its exact
width guards, without a priority claim for the standard probability mechanisms. The nonlinear extension uses the
same fresh-coin argument. The Manzoni–Mariot–Menara no-boundary convention is explicitly kept distinct.

- **Quint, G.P.J.W. with Gemini, "Constructive Backward Operators, the Period-3 NOR Wave Trichotomy, and Projective Orbit Laws
  for Zero-Boundary Stripe Primitive Roots" (R30-20261029-a4691a) and "The Universal Backward Wave Cascade, Clone-Ray
  Disjointness, and 16-Ray All-Length Mortality for Zero-Boundary Stripe Prefixes" (R30-20261030-5beddc)**, portal, Lean
  Verified (the second Human Verified). In the zero-boundary stripe frame: the backward NOR recurrence `V_i = NOT (V_(i-1) OR
  V_(i-2))`, its period-3 wave `(100)^infty`, the complement `(011)^infty` one step further back, and the doubling of the spatial
  period from 3 to 6 (`wave_011_to_period6_step0`). **Known, found after our CL659 to CL661 (30 October) and GC2272 (3 x 2^e at
  every depth)**: our backward ocean's periods 1, 3, 3, 6 are this cascade seen from the two-sided finite row; Quint's Lean
  statements precede ours by a day. Our root structure (unique finite parent, depth, counts: R30-20261030-803bc4) and the 3 x 2^e
  family at every depth (GC2272, solo sketch) are not in his headlines. Added by Cloud, 2026-10-31 (CL668).

## L1257 — Rule 30 has no block coarse-graining to N = 4: known, reproved here (31 October 2026)

Israeli, N. and Goldenfeld, N., "Coarse-graining of cellular automata, emergence, and the predictability of complex
systems", Phys. Rev. E 73 (2006), arXiv nlin/0508033 (read via ar5iv for this sentence): "The 16 elementary CA which we
could not coarse-grain are rules 30, 45, 106, 154 and their symmetries." Song, Z. and Aaron, J., "An improved
algorithm for coarse-graining cellular automata", arXiv 2012.12153 (read via ar5iv): 20 elementary CA have no
coarse-graining up to supercell size 7, the 16 plus the classes [37, 91] and [164, 218]. The summary seen did not list
the 16 by name.

Reproved here (`tests/probes/inquisition_coarse_grain.py`, 3ccf5fe9, output a542b5c3): for N = 2, 3, 4, no
non-constant P from N-cell blocks to one bit gives P(F^N(abc)) = g(P(a), P(b), P(c)) for any elementary g, for Rules
30, 86, 135 and 149. Exhaustive over all 2^(2^N) projections. The controls, Rules 90 and 150 at N = 2, each have six,
including the first-cell projection onto themselves. Local first dropped this test as "already known". The owner
corrected that ("Already known is well worth proving"), and the result is now reproved rather than assumed. The scope
is the one-bit, time-N definition only. Targets with more colours, or other time scales, are not covered here or, as
far as the summaries show, in those papers.

Also searched for T-S (the trace grammar by direction): Milnor 1988 (directional entropy), Sablik (directional
dynamics; Rule 30 has no expansive direction), Kopra 2023 (rapid left expansivity), Guillon and Zinoviadis
(diagonal determinism, arXiv 1204.0949, not read). No count of Rule 30's single right-diagonal language and no
forbidden word 00100 was found; prior art is possible.


## Inquisition corrections and known results reproved (GPT, GC2326–GC2328, 31 October 2026)

The [carrying read](reports/GPT-INQUISITION-20261031.md) identifies Local's 00100/11011 obstruction with the already
second-read G258, alongside G264's white wedge and G267/G268's longer exclusions. Known, reproved here; absence of
those names from a keyword search did not make the words additional. The left-diagonal bijection is the standard
permutive triangular reconstruction in this exact geometry, independently carried here.

At kit842b756f, `Rule30ZeroBoundary.complete_near_wall` refutes a sea-only uniform clock-death bound for unbounded
patch width. More decisively, `Rule30PeriodTwoCoupled.etherLeft_zbl` and `ether_col1_black` already exhibit the
period-seven sea1100001 repeated, with depth-1 trace1011 repeated forever. Thus the conjectured eventual death of
all nonwhite/noncheckerboard seas also fails. These actual source proofs were read, not inferred from catalog words.

Lowry PR69 atfcffbaa9 gives the one-in-four moving-edge pair invariant and eventual exclusion. GPT's finite-time
bound and extremal coefficient remain separately unreviewed deductions from that source, with no first-in-literature
claim. Brummitt–Rowland2012's boundary inventory was checked in scope; its cited Phillips periodic-background work
remains a targeted comparison dependency before priority or delivery decisions.

GC2329 literature scope: Phillips's2004 periodic-background notebook was obtained and its width-at-most-four
seed/background inventory read. Its Rule30 evidence is principally bitmap figures, not inspected here. This is a
specific remaining comparison for the ether-episode construction, not a negative-search novelty clearance; source
link and exact digest are in the block report.
