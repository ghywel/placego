# Collatz at rStation: what could change our approach to Rule 30?

Owner-requested appraisal, 2026-10-25. GPT, GC1882 / MI814.

**Verdict:** the most useful import is a proof architecture from paper 37: make one exceptional integer generate more exceptional integers than an independently established sparsity bound permits. This is a genuine way to cross an almost-everywhere/every-integer divide. It suggests a precise alternative question for Rule 30, but the required survival-preserving amplification has not been constructed. Neither Collatz nor our all-width Rule 30 problem is solved by this appraisal.

This is an internal research report. Nothing was posted to rStation; no experiment, census, benchmark, Lean build, worker wakeup or schedule restart was made. The third halt remains in force outside this one-off request. The two old dynamics startup scripts were not rerun during this source-and-hand-reasoning task; no fresh startup-test pass is claimed.

## 1. What I examined

The survey is pinned to the 37-paper / 45-discussion inventory retrieved on 2026-10-25 from the [Collatz problem page](https://rstation.ai/problems/collatz). Appendix A records every paper's version; Appendix B records every discussion's revision. Paper manuscripts, their latest review reports, full discussion bodies and comment-list snapshots were retained outside git. Downloading a source is not reading or verifying it.

Reading depth was deliberately uneven:

- All 37 paper abstracts and the opening verdict/scope of their latest review reports; all 45 discussion inventory entries and a substantive beginning/end triage of their main posts.
- Complete manuscripts and reviews for papers 35 and 37; the carrying quantitative construction in paper 14 §7.4; extensive theorem/proof sections in papers 15, 28, 32 and 34. Additional papers were assessed at their stated theorem and dependency scope, as indicated below, rather than independently proved from scratch.
- Complete main discussions 34–38 and 41–45, and selected mathematical sections of 31, 33, 39 and 40. In particular, some discussions are manuscript-length documents: triage does not mean every embedded proof or code block was audited.
- All ten replies to our discussion 35 and all four replies to discussion 45, including their corrections and the unreviewed linear-cutoff continuation. The other comment lists were screened selectively; hundreds of full comment bodies were not all read.
- Our current Rule 30 board, prior submission and signed-error question, the Q3/G5 matrix discussion, selected-wait and inverse-branch records, and the current finite-support trace interfaces. No external computational certificate was replayed.

The platform's latest reports label the surveyed papers “Accept.” That is platform review, not independent verification here, and some reports assess a revision relative to an earlier version. In particular, several analytic conclusions import recent external work whose complete proofs I have not independently audited. This report distinguishes a useful argument conditional on those inputs from a newly adopted theorem.

The public source retrieval briefly met a rate limit; requests were stopped and resumed more slowly. No authentication, private account content or external write was involved. The inventory is a dated snapshot, not a claim that the live community has stopped changing.

## 2. What the pool has actually accomplished

The 37 papers are not 37 independent attacks on the last step. They form several connected programmes, with repeated machinery, revisions and useful corrections.

| Programme | Papers | Mathematical gain | Remaining distinction |
|---|---|---|---|
| Joint affine laws, passage and predecessor counts | 5–7, 9–10, 12–14, 18–19 | Retain division sums, real size and ternary residues together; improve ensemble statements and inverse counts. | An averaged law does not control an arbitrarily selected rare trajectory. |
| Fourier and transfer operators | 2, 11, 29–30, 36 | Exact identities, improved finite or conditional bounds, collision and residue-resolution estimates. | Geometric random words are not automatically the words selected by integer survival. |
| Cycles, arithmetic ordering and completions | 4, 8, 17, 20, 22, 24–27, 33 | Stronger exclusion criteria and complexity requirements for possible cycles. | Rational cycles and admissible symbolic words remain plentiful; integrality is decisive. |
| Complexity of individual trajectories | 15–16, 31 | Restrictions on periodic dictionaries, automatic/substitutive descriptions and additive structure. | Excluding structured exceptions does not exclude every exception. |
| Smaller sources, synchronization and compression | 1, 13, 21, 28 | Source-aware comparisons and useful compression of whole populations. | A rare selected set could consist of the exceptional fibre representatives. |
| Obstructions to proposed methods | 3, 32, 34 | Precisely scoped failures of local potentials, fixed-resolution graphs and convex completion tests. | These do not prohibit all nonlocal certificates or all adaptive methods. |
| Adaptive reserve accounting | 35 | Exact refill distributions and correlations, with a finite-integer window. | The reserve charges are dependent; selected survival is an additional change of measure. |
| Pointwise inverse routing | 37 | Uses ancestor abundance against a thin failure set to obtain an every-integer conclusion. | Routes need not be short, low, or lead to a source smaller than the original integer. |

My appraisal is positive about the mathematical content, but cautious about interpreting accumulation as proximity to convergence. The more revealing contributions retain the variable that a previous argument lost: the original source, total division sum, real lift interval, sign, temporal join, or changing resolution.

Two examples of important scope corrections are already visible within the community. Paper 5 acknowledges earlier sum-conditioned mixing work, and paper 6's natural-density conclusion is not presented here as a newly discovered theorem independent of that prior work. The cycle advances in paper 20 concern **94/95 blocks of local minima**, not exclusion of all cycles of 94/95 ordinary steps; they also use the existing finite verification input. Those are meaningful results in their stated setting, not a convergence proof.

## 3. The strongest import: amplification of a counterexample

[Paper 37/v1](https://rstation.ai/problems/collatz/papers/37/v1) studies the odd map and its legal inverse branches

```math
S(n)=\frac{3n+1}{2^{v_2(3n+1)}},\qquad I_e(u)=\frac{2^eu-1}{3}.
```

Its crucial ingredient is not merely that inverse orbits visit many residue classes. With the analytic inputs inherited through [paper 14/v3, §7.4](https://rstation.ai/problems/collatz/papers/14/v3), a fixed sufficiently large cutoff $M$, divisible by six, supports many **distinct positive integer ancestors** of every positive odd target prime to three:

```math
\#\bigl(A_M(x)\cap[1,X]\bigr)
\ge e^{-C_1M}(X/x)^{1-C_0/M},\qquad X\ge x.
```

For failure to reach a specified unit class modulo $3^k$, with $6\mid M<2\cdot3^k$, its separate cylinder argument gives an upper counting exponent

```math
D_{k,M}=\frac{\log(3^k-M/2)}{k\log3}<1.
```

Failure is closed under the **same capped inverse operations**. If one integer failed, all its capped ancestors would fail. Choosing $1-C_0/M>D_{k,M}$ makes the lower and upper counts incompatible. This yields a maximum individual valuation of order $\sqrt{k}\,3^{k/2}$ for routing. It does not give a bound of that order on route length, sum of valuations, total height, or descent below the original source.

The carrying checks in my read were: the strict positive-weight margin survives truncation; normalized branches really are legal integer inverse steps; nonperiodic targets give distinct sources rather than just many words; a periodic target can be escaped through an off-cycle child; and the failure set has the closure property for exactly the cutoff used in the lower bound. The external analytic inputs themselves remain outside this independent audit.

The important transferable lesson is the **comparison of two counts on the same invariant exceptional set**, not a slogan that a thin set contains no integers. A measure-zero set can contain integers, or even all integers inside a completion. Paper 37 supplies the extra structural reason it cannot contain the particular integer exception under consideration.

### A live extension, kept separate

Discussion 45 now contains an [author-audited linear-cap argument](https://rstation.ai/r/collatz/posts/45#comment-LIqfAhwOqDo0ZDDa), claiming

```math
\max e\le(\log_2 3)k+C.
```

The comment explicitly calls it **unreviewed**, and paper 37/v1 remains unchanged. Its intended improvement is an exponentially small deficit in the inverse counting exponent, obtained with a finite-horizon construction rather than an unjustified infinite atom floor for truncated geometric gaps. I read the complete comment, but not the full attached manuscript or the external Leen/EJ dependency proofs. I do not promote this claim to an accepted result. Even if correct, it still does not supply the missing height/order control for smaller-source descent.

The later [sibling-energy comment](https://rstation.ai/r/collatz/posts/45#comment-lPBxx2FM2eMZQrSr) is also instructive: an exact local energy identity initially looks promising, but its added Fourier-packet control rules out a precision-independent strict contraction over any fixed number of steps. Keeping initial precision matters. This is a useful warning against inferring uniform extinction from attractive finite spectral diagnostics.

## 4. A precise Rule 30 question obtained from that architecture

Use the project's reflected half-line convention, with $x_0=0$:

```math
(Fx)_i=x_{i+1}\mathbin{\oplus}(x_i\lor x_{i-1}),\qquad i\ge1.
```

Let $E_B$ be the set of rows supported in $\{1,\ldots,B\}$ whose depth-one cell stays black at every even ordinary time. Q01/LR says every $E_B$ is empty. This is the all-width finiteness question; the stronger proposed affine deadline is a separate claim.

There is already a simple exact upper bound:

```math
|E_B|\le2^{\lfloor B/2\rfloor}. \tag{1}
```

**Reason.** Triangular trace coding gives
$(F^t x)_1=x_{t+1}\oplus H_t(x_1,\ldots,x_t)$.
For every even $t<B$, imposing a black cell fixes the new odd-depth bit $x_{t+1}$, with earlier bits known. The even-depth bits remain free. Thus there are exactly $2^{\lfloor B/2\rfloor}$ rows satisfying these early constraints; eternal survivors are a subset. This is the known permutivity/free-bit mechanism, re-expressed here, not a new result or a late-time survival estimate.

The imported proof obligation is therefore concrete:

> **Unproved amplification target.** From any hypothetical finite eternal survivor $L$, construct, for arbitrarily large $B$, distinct finite eternal survivors supported within $B$, in number greater than $2^{\lfloor B/2\rfloor}$.

For example, a lower bound $c_L2^{(1/2+\varepsilon)B}$, with $\varepsilon>0$ and $c_L>0$, would suffice. Combining it with (1) would contradict the existence of $L$. The implication is elementary and hand-checked; **the construction is missing**. No independent new Rule 30 theorem is claimed.

This differs usefully from asking that the entire survivor population lose a fixed fraction at every late time. The amplification could be conditional on one eternal counterexample, and need not give a uniform hazard law for arbitrary long-lived rows. A qualitative construction would prove all-width finiteness. An explicit deadline would require a quantitative, finite-horizon version, specifying how much survival of the original seed creates a large family through a common horizon at least $B-1$.

### Why the obvious import fails

I tried to defeat this proposal before treating it as a direction:

1. **Ordinary backward time does not give Collatz's rich ancestry.** For a nonzero finite row of exact width $W$, $Fx$ has exact width $W+1$: the new cell at $W+1$ is black and all deeper cells are white. Hence ancestors of a fixed finite target have strictly decreasing widths and bounded depth. The unbounded inverse tree used by paper 37 is absent in this direction of Rule 30.
2. **Forward iteration is too poor.** A bad row would produce further bad rows under $F^2$, but only one along each successive width, not the required exponential family.
3. **Far-tail choices preserve a finite prefix, not eternal survival.** Causality cannot justify extending the claim beyond the time when those choices enter the boundary cone. Counting multiple zero-padded encodings of the same row would be another false gain.
4. **Two choices per two cells are only critical.** They match the exponent $1/2$ in (1); they do not beat it. A genuine surplus or a sharper upper bound is necessary.
5. **Count distinct rows, with the same survival predicate.** Symbolic histories, relaxed infinite tails and different driving boundaries cannot be substituted. The old GC690–695 inverse-branch discussion already exposes these difficulties for the alternating-wall model; those statements must not be silently transferred to this zero-boundary map.

The unexpected control is **rule 210**. Our record proves its LR analogue false. A proposed amplification argument relying only on generic permutivity/free-bit coding would therefore be suspect: it must use a feature distinguishing rule 30 from that control. Likewise, genuine infinite-support survivors in a relaxed model are not counterexamples to finite-seed Q01.

The plausible place to seek an operation would be the existing *sideways, source-retaining compatibility relation*, not ordinary inverse time. But I found no operation in these papers or in our existing record that both preserves eternal survival and produces the necessary surplus of finite rows. This remains a research question, not an executable programme or a request to reopen a census.

## 5. Other imports: useful, but not the missing theorem

### Dependent charges and merger accounting

[Paper 35/v1](https://rstation.ai/problems/collatz/papers/35/v1) gives a clean warning about adaptive periodic reserves. Its charge has the form

```math
J_i=B_{i+1}+R_{i+1}-R_i,
\qquad \sum_{i=0}^{m-1}J_i=\sum_{i=1}^{m}B_i+R_m-R_0.
```

The single-charge variance is $68/9$, while negative covariances reduce the asymptotic variance per block to $4$. A finite positive-integer window is proved separately. These facts do not describe a fixed survivor-conditioned orbit indefinitely. For Rule 30, the value is a disciplined way to distinguish paid increments from a reserve difference; our Q7 selected-wait identities already make a related distinction. It supplies no new joint stage budget by itself.

The response to our [signed-error question](https://rstation.ai/r/collatz/posts/35#comment-36tdI339isKsohav) says explicitly that the source coupling does not control the discrepancy after the width block's free digits have been exhausted. That is the exact location of our wall, not an inferred shortcoming.

A further [merger-forest reply](https://rstation.ai/r/collatz/posts/35#comment-ysMkhDZu66JnnGyW) gives a worthwhile accounting refinement. With unsplitting groups of multiplicities $u,v$, convexity of $\phi(s)=s\log_2s$ gives

```math
\phi(u+v)-\phi(u)-\phi(v)\ge2\min(u,v).
```

Consequently total repeatedly matched mass is at most $(N/2)\log_2 M_*$, where $M_*\le N$ bounds group size; killed groups must remain terminal roots. I checked this elementary telescoping argument. The weighted version still leaves a signed production term, and source multiplicity is not the ordering of original integers. Thus the reply improves bookkeeping while expressly leaving our estimate open. In Rule 30 it would apply only to genuine unsplitting state groups, not an arbitrary coarse trace quotient.

### Keep actual joins and the physical boundary

[Paper 34/v1](https://rstation.ai/problems/collatz/papers/34/v1) constructs local actual-integer histories inside sharp completion hulls even though the corresponding rational completions fail a later step. The lesson is narrow and useful: sharp local convex inequalities need not enforce a common realizable continuation. Our real-past, common-right-witness and finite-zero-tail conditions must survive any relaxation.

[Paper 28/v1](https://rstation.ai/problems/collatz/papers/28/v1) compresses uniformly sampled translated intervals, retaining the clock and odd count. Its image bound uses the exponent $H_2(\log_3 2)$, about $0.94995$, with a logarithmic improvement. That is population compression. A selected exceptional family could consist of fibre leaders, so dividing by a very small survival probability does not turn it into the estimate we need. Its clock retention is portable; its arithmetic bound is not automatically portable.

[Paper 32/v2](https://rstation.ai/problems/collatz/papers/32/v2) shows how negative rational cycles generate positive integer shadows defeating specified fixed-resolution drift certificates. The needed binary precision grows with the duration of the shadow and the size of the positive representative. In Rule 30 the analogous question is whether a certificate sees the actual finite white tail as its relevant scale grows. This does not prove that every local or finite-dimensional potential is impossible.

### Matrix certificates are an old open possibility here

[Discussion 43/r4](https://rstation.ai/r/collatz/posts/43) illustrates the sensitivity of termination proofs to their encoding: a compressed return rule can admit a matrix interpretation where a particular split-rule representation fails. Boundary padding, rather than an informal sign label alone, can determine whether a negative cycle is included.

My first pull toward this was checked against our own record. **Q3 and G5 already discuss matrix interpretations.** G5 corrected an overstrong equivalence between finite-dimensional rankings and uniform fractional count loss; small matrices can count arbitrarily long words. Thus “try matrices” is not a new discovery from this survey. A fresh contribution would have to name a new finite family and a faithful finite-support encoding. No such certificate has emerged here, and no synthesis job is proposed.

### Structured exceptions remain only a slice

Papers 15–16 and discussion 6 strengthen restrictions on dictionary, automatic and substitution descriptions of Collatz itineraries. They resonate with our Theorem E, including its all-intercept Sturmian exclusion. But their arithmetic tools use the special roles of powers of two and three, algebraicity, and the affine Collatz identity. Replacing a Collatz itinerary by a Rule 30 column does not preserve those hypotheses. Nor would another structured-family exclusion cover arbitrary Q01 survivors.

The same qualification applies to Mahler. Thin survivor sets are compatible with arithmetically special points. An amplification strategy there would need operations preserving both the exceptional constraint and the relevant arithmetic domain, plus a distinct-point count exceeding the survivor bound. I found no supplied operation that does this. The three problems share a quantifier obstruction; this is not a proof of equivalence between them.

## 6. Corrections that matter for our own record

The complete discussion-35 exchange contains more than endorsements:

- An unbounded-horizon collision family extends our finite G89 collisions, while explicitly crediting G89 for the original nonuniqueness result. Equal terminal state and equal final odd count still do not erase earlier barrier labels.
- The fair-coin asymptotic exponent is $1-H_2(\log_3 2)$, about $0.05005$ bits per shortcut step. Our finite fitted slopes around $0.059$–$0.064$ are not that asymptotic exponent.
- Coefficient survival and actual first-descent survival remain separate. Terras's free-bit bijection alone does not identify them after the free-bit window.
- A reply advertised a complete carry-cutoff resolution, but the [following correction](https://rstation.ai/r/collatz/posts/35#comment-9pSeBY36Iy4ocaLI) gives $T_2(11)=9$, not 13, and a positive odd start $1865045$ entering the cutoff-11 zero basin despite not being a dyadic multiple of 1365. The author acknowledges these corrections. I read the argument and the native-code references but did not replay the examples. Neither the original sweeping claim nor its unproved minimality assertions are adopted.

Discussion 44 also retracts overbroad claims about zero-entropy cycle exclusions and generic logarithmic run lengths. These corrections are evidence that reading only an attractive headline would give a materially false appraisal.

## 7. Result of the exploration

**What changed:** a specific pointwise proof architecture was identified and translated into the exact Rule 30 threshold (1), with its essential missing construction and its failed direct implementation exposed. The source replies also confirm that our signed-bias question remains genuinely unanswered; they supply a useful merger budget, not its solution.

**What did not change:** no all-width Q01 bound, no general CQ01 coverage, no Collatz convergence proof, no Mahler exclusion, and no board-status promotion. The source-reading result is complete; the amplification premise is an explicitly unproved mathematical question, not an outstanding promised review.

**Judgment:** if choosing one question from this survey for a future owner-authorized return, I would choose “what transformations can a finite eternal counterexample survive?” before another census of its apparent randomness. It asks for structural closure and multiplicity, with a numerical threshold supplied by an existing exact theorem. It is more discriminating than “improve mixing,” but it is not yet a demonstrated path through the wall.

**Instinct and trajectory:** the pull was the possibility of crossing a null-set/individual-point barrier without asserting typicality. The direct inverse-time test rejected the simplest transfer; the matrix record search rejected an apparent novelty. Those failures changed the deliverable from a proposed proof programme to this conditional architecture and appraisal. The gut verdict is interested but unconvinced; the reasoned verdict is a useful new comparison, with the hard lemma still absent. No experiment is queued.

**Niggle sweep:** analytic dependencies, latest-version versus discussion status, finite versus eternal survival, distinct rows versus histories, zero versus alternating boundary, positive versus negative arithmetic, selection normalization, and prior matrix/selected-wait work were each checked at the scope stated above. No remaining uncertainty has been silently upgraded to a result.

## Local sources and reading record

- [Our original Collatz post](collatz-post-35.md) and [GPT's earlier signed-error contribution](collatz-post-35-gpt-check-in.md).
- [Current board](../../PERIOD-TWO.md), [Rule 30 catalogue map](../wolfram-agents/MAP.md), [finite-survival interface](../wolfram-agents/GPT-CL609-TASK4-REVIEW.md), and [common-witness CQ01 specification](../wolfram-agents/GPT-CL624-NESTING-CQ01.md).
- [G5 matrix correction](../../archive/gpt/RULE30-GPT.1.md), [GC690–695 inverse-branch discussion](../../archive/gpt/RULE30-GPT.6.md), and [Q3 history, §8.61](../../RULE30-PRIZE.md).
- [Collatz record](../../COLLATZ-PRIZE.md), [Mahler record](../../MAHLER.md), and [record map](../../RECORD-MAP.md).

Record searched before the transfer analysis: `ancestor|amplif|porosity|selected.wait|negative.*correl` (217 paragraph hits across 67 files); `matrix.interpret|weighted.autom|noncommut|termination.prov` (10 hits across eight files). These are navigation results, not claims that no other precedent exists. The named sources were read before using their claims.


## Appendix A. All 37 papers, pinned versions

Reading codes: **S** = abstract, stated scope and review-opening screen; **D** = substantial selected theorem/proof reading; **F** = complete manuscript and review. None denotes an independent replay of computational evidence. The main text specifies which dependencies remain external.

| Paper | Title | Read | Appraisal |
|---|---|---|---|
| [1/v3](https://rstation.ai/problems/collatz/papers/1/v3) | Inverse minima and escape to smaller Collatz sources | S | Inverse minima and escape examples; fixed-depth ancestry can fail, and a new endpoint can change the answer. No universal smaller-source selection. |
| [2/v5](https://rstation.ai/problems/collatz/papers/2/v5) | How fast does the Syracuse characteristic function decay? Exact computation, a renewal identity and a certified conditional bound | S | Finite exact Fourier evidence and a conditional decay bound; the uniform hypothesis remains an input, not a measured theorem. |
| [3/v1](https://rstation.ai/problems/collatz/papers/3/v1) | Two-path obstructions to Collatz potentials built from size, residues and prime-factor counts | S | Two actual growing paths defeat the specified additive potential architecture. Not a prohibition on all rankings. |
| [4/v1](https://rstation.ai/problems/collatz/papers/4/v1) | Closed-Form Rearrangement Brackets, Dual Simplex Extrema, Stern–Brocot Parent Determinants, and Single-Transposition Exclusions for Collatz Cycles | S | Rearrangement and arithmetic cycle exclusions; useful exact combinatorics, with the integer divisibility test still essential. |
| [5/v3](https://rstation.ai/problems/collatz/papers/5/v3) | A joint formulation of sum-conditioned Syracuse mixing | S | Joint sum/residue formulation with corrected prior-art credit. Retaining a variable is valuable but does not make a selected survivor typical. |
| [6/v3](https://rstation.ai/problems/collatz/papers/6/v3) | Natural-density almost boundedness of Collatz orbits via the renewal theorem | S | Natural-density almost-boundedness via renewal; prior-work and ineffective-error qualifications matter. No individual-orbit conclusion. |
| [7/v1](https://rstation.ai/problems/collatz/papers/7/v1) | Collatz orbits from a dyadic block: almost bounded values with exceptional density O_A(log^{-A} N_0) | S | Sharper exceptional-density control from dyadic blocks. Arbitrarily small density still permits a fixed exception. |
| [8/v2](https://rstation.ai/problems/collatz/papers/8/v2) | The Bezout–Syracuse Seed Identity, Dual Fixed-Point Homogenization, Coupled Block-CRT Renormalization, and Deterministic Functional-Graph Obstructions for {1, 2}-Valuation Collatz Cycles | S | Dual affine normalizations and block congruences for cycle words. Special arithmetic structure has no supplied Rule 30 counterpart. |
| [9/v1](https://rstation.ai/problems/collatz/papers/9/v1) | Ternary Syracuse laws: tail conditioning, moment growth, and predecessor bounds | S | Real-tail conditioning can select a singular ternary law. Particularly useful as a warning against transferring an unconditioned law. |
| [10/v3](https://rstation.ai/problems/collatz/papers/10/v3) | A uniform linear lower bound for Collatz predecessor counts, from joint Syracuse atoms at fixed valuation | S | Uniform linear predecessor lower bound from joint atoms. Strong inverse abundance, conditional on the stated analytic inputs; not descent. |
| [11/v2](https://rstation.ai/problems/collatz/papers/11/v2) | Additive-to-Multiplicative Parseval Isometry, Quarter-Plane Twisted Pascal Green's Functions, and m-Step Horizontal Plaquette Majorants for the Syracuse Characteristic Function | S | Parseval and Green-function identities for Fourier analysis. Exact reformulation and majorants, not a deterministic survivor estimate. |
| [12/v1](https://rstation.ai/problems/collatz/papers/12/v1) | First-landing bounds and canonical inverse laws for Collatz | S | First-landing and inverse-law bookkeeping. Useful retained-source framework; keep the positivity and first-landing restrictions. |
| [13/v1](https://rstation.ai/problems/collatz/papers/13/v1) | Conditional clocks and source couplings for Collatz synchronization | S | Source-marked coupling and clock synchronization. Explicitly insufficient for arbitrary rare selection; discussion 35 confirms our gap. |
| [14/v3](https://rstation.ai/problems/collatz/papers/14/v3) | The Krasikov–Lagarias programs have no ceiling below x^1: λ_k → 2, via the Syracuse dual | D | Quantitative positive-weight construction is a carrying input to paper 37. Read §7.4; external analytic premises not independently reproved. |
| [15/v1](https://rstation.ai/problems/collatz/papers/15/v1) | Effective periodic-dictionary complexity for Collatz trajectories | D | Effective escape from fixed periodic dictionaries. Dictionary complexity can grow without supplying the universal bound needed here. |
| [16/v2](https://rstation.ai/problems/collatz/papers/16/v2) | Automatic parity and primitive substitutions in rational Collatz dynamics | S | Automatic and primitive-substitution restrictions in rational dynamics. Large analytic argument not independently audited in this appraisal. |
| [17/v1](https://rstation.ai/problems/collatz/papers/17/v1) | Place-Time Duality, the Backward 3-Adic Dual-Ballot Sieve, Universal Unrestricted Block-CRT Renormalization, and Unconditional Exclusion of 92- and 93-Block Collatz Cycles | S | Dual-ballot/block-CRT cycle exclusions to 92/93 blocks. Not ordinary step counts; finite verification and analytic inputs retain their roles. |
| [18/v1](https://rstation.ai/problems/collatz/papers/18/v1) | Microscopic occupation from smooth Syracuse passage laws | S | Microscopic occupation extracted from smooth passage laws. A local ensemble statement with conditioning hypotheses, not every trajectory. |
| [19/v2](https://rstation.ai/problems/collatz/papers/19/v2) | Geometry, integer fibres, and dyadic equidistribution of the joint Collatz affine law | S | Joint affine geometry and integer fibres. Distinguish law-level equidistribution from positivity and size of a particular lift. |
| [20/v1](https://rstation.ai/problems/collatz/papers/20/v1) | Coupled Bézout Congruence Towers, Telescopic Prefix Completion Cuts, and Unconditional Exclusion of 94- and 95-Block Collatz Cycles | S | Congruence towers and 94/95-block exclusions. Uses existing finite verification; no certificate replay here and no all-cycle claim. |
| [21/v3](https://rstation.ai/problems/collatz/papers/21/v3) | Smaller Collatz sources before first descent: power gains and conditional exponent shells | S | Smaller-source gains before descent and conditional shells. Actual-source and extension-cylinder scopes must not be interchanged. |
| [22/v4](https://rstation.ai/problems/collatz/papers/22/v4) | Sparse block-sum and ordered-state complexity in positive Collatz cycles | S | Sparse block-sum and ordered-state complexity restrictions on cycles. Raises the cost of a cycle without proving none exists. |
| [23/v1](https://rstation.ai/problems/collatz/papers/23/v1) | Permitted Canonical Potential Invariance, a 64-Bit (min, +) Semiring Homomorphism, and Exhaustive Uncapped Certification of W_20 = 44 for the Joint Collatz Affine Law | S | Canonical invariance/min-plus formulation and finite W20 certificate. Finite certificate reported; no independent replay or all-size extension. |
| [24/v1](https://rstation.ai/problems/collatz/papers/24/v1) | Square-root Farey-defect complexity in coprime Collatz cycles | S | Square-root Farey-defect complexity. Arithmetic cycle restriction, not a general termination mechanism. |
| [25/v1](https://rstation.ai/problems/collatz/papers/25/v1) | Universal Canonical-Root Width, the Defect-Free Eulerian Farey Digraph, Complementary-Factor Chebyshev Decomposition, and Fixed-Slope Q_d-Fibre Census for Collatz Cycle Words | S | Canonical-root width and Farey graph/census. Canonical root is not automatically the numerical minimum; see discussion 41. |
| [26/v2](https://rstation.ai/problems/collatz/papers/26/v2) | Large phase-minimal families of Collatz words | S | Large phase-minimal families. Important counterweight: phase inequalities alone leave many rational candidates. |
| [27/v1](https://rstation.ai/problems/collatz/papers/27/v1) | Sorted-Ascent Rank Descents, Coprime-to-6 Stopping Certificates, Linear-Form State-Ordering Isomorphism, Sturmian-to-Farey Discrepancy Bridges, and Carry-Absorption / Ternary-Digit Suffix Tower Laws for Collatz Cycles | S | Rank/order and suffix congruence tools. A collection of structural cycle criteria; no unqualified universal stopping result adopted. |
| [28/v1](https://rstation.ai/problems/collatz/papers/28/v1) | Logarithmic stopping boundaries for uniform Collatz interval compression | D | Translated-interval compression retaining time and odd count. Selected exceptional representatives remain an unresolved transfer. |
| [29/v1](https://rstation.ai/problems/collatz/papers/29/v1) | Subgroup-Lifting Transfer Operators, Shifted Diagonal Filtrations, and Sub-1/2 Ternary Collision Bases for Geometric Collatz Words | S | Collision/transfer bounds for geometric words. Improved random-law estimates do not assign that law to integer survivors. |
| [30/v1](https://rstation.ai/problems/collatz/papers/30/v1) | Logarithmic residue resolution for geometric Collatz words | S | Residue resolution on a logarithmic precision scale. Do not silently replace logarithmic resolution by linear resolution. |
| [31/v2](https://rstation.ai/problems/collatz/papers/31/v2) | Additive structure, energy, and integer rigidity of Collatz orbit sets | S | Additive complexity of actual orbit sets is more source-sensitive than a random-word model. Its arithmetic bridge still needs a Rule 30 analogue. |
| [32/v2](https://rstation.ai/problems/collatz/papers/32/v2) | Drift certificates for Collatz residue avoidance: an entropy characterization and a sign barrier | D | Exact scope of drift-graph entropy/sign obstructions. Positive shadows of negative pins obstruct fixed resolution; adaptive methods remain distinct. |
| [33/v1](https://rstation.ai/problems/collatz/papers/33/v1) | Two-Sided Prefix-Suffix Phase-Minimality Certificates, Support-Valuation Order Ideals, and Pre-Halving Dual Plateau Obstructions for Collatz Bridge Posets | S | Prefix-suffix phase and support-order restrictions. Retain joint consistency; separate local inequalities need not certify integer realization. |
| [34/v1](https://rstation.ai/problems/collatz/papers/34/v1) | Local integer histories in sharp Collatz completion hulls | D | Actual finite histories can satisfy sharp completion hulls while later completion fails. A direct caution about local convex relaxations. |
| [35/v1](https://rstation.ai/problems/collatz/papers/35/v1) | Exact refill laws and negative correlations for adaptive periodic reserves in Collatz dynamics | F | Full selected-charge law and all-lag covariance read. Negative dependence/coboundary structure carries; survivor-conditioned import does not. |
| [36/v1](https://rstation.ai/problems/collatz/papers/36/v1) | Shifted 3-Adic Carry-Quotient Encodings, Zero-Sum Endpoint-Collision Obstructions, Child-Diagonal Defect Sandwiches, and Nilpotent Suffix Markov Operators for Critically Tilted Collatz Words | S | Carry-quotient and endpoint/suffix operator machinery for tilted words. Source scope screened; no complete proof audit or deterministic transfer. |
| [37/v1](https://rstation.ai/problems/collatz/papers/37/v1) | Finite valuation cutoffs and pointwise modular routing in Collatz inverse trees | F | Full manuscript/review read. Same-cutoff inverse abundance versus failure porosity yields pointwise routing, conditional on inherited analytic inputs. Best architectural import. |

## Appendix B. All 45 discussions, pinned main-post revisions

Reading codes: **T** = inventory and main-body triage; **P** = selected mathematical sections; **F** = full main body; **C** = all replies in the captured thread read in full. These codes do not claim that linked external references or attachments were all read. Revision applies to the main post; selected comment revisions are noted in the main text.

| Post | Title | Read | Appraisal |
|---|---|---|---|
| [1/r1](https://rstation.ai/r/collatz/posts/1) | Positive-integer stress tests for low-bit plus carry-depth Lyapunov searches | T | Positive growing paths defeat low-bit plus carry-depth potentials; scope-specific counterexample mechanism. |
| [2/r1](https://rstation.ai/r/collatz/posts/2) | Inverse minima for words with no consecutive twos, and a sharp four-step overhead | T | Inverse-minimum comparison; later collision and source-selection discussion is relevant, not a convergence theorem. |
| [3/r1](https://rstation.ai/r/collatz/posts/3) | The Rational-Cycle Tautology Filter, Overgeneralized Negative Barriers, and Coupled (Z_2 x Z_3) Renormalization | T | Rational-cycle tautology filter and coupled-completion proposals; local identities alone do not enforce integrality. |
| [4/r2](https://rstation.ai/r/collatz/posts/4) | Fourier decay is not Tao's bottleneck; and a gap in Siegel-O'Dwyer's passage-location step | T | Separates Fourier strength from passage/renewal losses; external Hydra-proof criticism is reported, not independently adjudicated here. |
| [5/r1](https://rstation.ai/r/collatz/posts/5) | Two growing inverse-tree certificates defeat size + residues + omega/Omega potentials | T | Two-path prime-factor potential obstruction; latest paper 3 gives the formal scope. |
| [6/r2](https://rstation.ai/r/collatz/posts/6) | A subspace criterion and factor-complexity barrier for Collatz parity words | T | Low-complexity/Sturmian conjugacy criterion; arithmetic counterpart to our already-existing structured-trace exclusions. |
| [7/r2](https://rstation.ai/r/collatz/posts/7) | Tao's almost-boundedness in natural density (submitted; please attack) | T | Early natural-density argument; use paper 6 v3 and its corrected priority, not this older novelty framing. |
| [8/r2](https://rstation.ai/r/collatz/posts/8) | The missing universal bridge after mixing: expansion of integer-lift fibres | T | Explicit missing integer-lift-fibre expansion question. Still distinguishes legal congruence from real source ordering. |
| [9/r1](https://rstation.ai/r/collatz/posts/9) | Dual Fixed-Point Homogenization, Unrestricted Excess Homogenization, and Mod-5/7 Index-Parity Collapse for Collatz Cycles | T | Cycle homogenization and small-prime nonuniformity; exact arithmetic, not generic equidistribution. |
| [10/r1](https://rstation.ai/r/collatz/posts/10) | Why Tao's 3-adic method stops at n^{-A}: a chain equation, a digit barrier, and numerics for the extremal frequency | T | Fourier-chain/digit obstruction; includes a withdrawn induction and an unverified unbounded-chain step. |
| [11/r1](https://rstation.ai/r/collatz/posts/11) | Krasikov–Lagarias exponent: x^{0.84} -> x^{0.8811} by extending their LP to k=15 (exact certificates) | T | Exact finite KL exponent improvements; later paper 14 changes the asymptotic context. Certificates not replayed. |
| [12/r1](https://rstation.ai/r/collatz/posts/12) | Prior work to audit: conditioned mixing, Gaussian clocks, and positive predecessor density | T | Prior-work correction register for conditioned mixing, Gaussian clocks and predecessor density; valuable dependency hygiene. |
| [13/r1](https://rstation.ai/r/collatz/posts/13) | An exact real/3-adic tail identity at positive odd targets | T | Exact real/ternary tail identity; moving-target uniform integrability remains an additional obligation. |
| [14/r2](https://rstation.ai/r/collatz/posts/14) | Real-tail conditioning selects a singular ternary law: a Gaussian prefix window | T | Conditioning on a large real tail changes the ternary law; a strong selection-bias warning. |
| [15/r1](https://rstation.ai/r/collatz/posts/15) | The Baker–Shadow Dichotomy: Why Collatz Cycles Must Be Highly Oscillatory ($r \gg k / \log k$) | T | Baker/shadow complexity discussion; broad randomness language is not adopted as a theorem about every orbit. |
| [16/r2](https://rstation.ai/r/collatz/posts/16) | Ternary Lp regularity gives a uniform polynomial predecessor-density bound | T | Uniform predecessor density programme; later source credit and revised papers govern priority and assumptions. |
| [17/r2](https://rstation.ai/r/collatz/posts/17) | Exact 2-Adic Ultrametric Peeling, the Binary Affine Automaton, and the 3x3 Minimum-Length Classification of Common-Future Collisions (Resolving collatz_1 Sec. 5) | T | Ultrametric peeling/collision encoding; finite/minimal-length statements remain separate from convergence. |
| [18/r1](https://rstation.ai/r/collatz/posts/18) | Krasikov–Lagarias reaches every exponent < 1: 2 - lambda_k = O(1/k), and a uniform-in-a count (x/a)e^{-C sqrt log(x/a)} | T | Earlier KL asymptotic construction; paper 14 v3 is the pinned current source for the quantitative input. |
| [19/r1](https://rstation.ai/r/collatz/posts/19) | A uniform pointwise Wirsching bound: pi_a(X) >= cX/a for all X >= a, via joint atoms at fixed valuation | T | Linear predecessor count from joint atoms. Target-uniform hypotheses and thresholds are important. |
| [20/r4](https://rstation.ai/r/collatz/posts/20) | Square-root coalescence tails: proof discussion and corrected attribution | T | Coalescence-clock discussion with corrected prior credit; not the arbitrary rare-selection bridge. |
| [21/r1](https://rstation.ai/r/collatz/posts/21) | Additive-to-Multiplicative Parseval Isometry, the 5/7 Spectral Main Term of E_u/chi_n(u)/^2, and an Unconditional Beat-(ln 2) Lower Bound for collatz_2 Sec. 6 | T | Parseval/spectral development; references several distinct majorants, not one proven uniform decay rate. |
| [22/r1](https://rstation.ai/r/collatz/posts/22) | A 3x+k test for our toolkit, and an exact census of S(w) mod divisors of 2^L-3^m | T | Minus-map/3x+k controls expose which algebra cannot distinguish the desired positive-integer conclusion. |
| [23/r3](https://rstation.ai/r/collatz/posts/23) | Fixed-descent excursion bounds and superlogarithmic non-one counts | T | Fixed-descent excursion complexity; longer words must be less simply described, which does not itself force descent. |
| [24/r1](https://rstation.ai/r/collatz/posts/24) | Hercher m-cycle bound at X0=2^71: no gain; a Thm 15 proof gap + repair; m=92 reduces to one (K,L) | T | Hercher gap repair and cycle-block frontier; later 92–95-block papers supersede the earlier numerical frontier. |
| [25/r5](https://rstation.ai/r/collatz/posts/25) | Effectivity registry for r/collatz results: what is explicit, what is k-sensitive, one shared choke point (corrections welcome) | T | Effectivity registry: separates explicit constants, effective existence and ineffective inputs. Helpful when appraising stronger headlines. |
| [26/r1](https://rstation.ai/r/collatz/posts/26) | Audit: the Fourier-free almost-boundedness proof of arXiv 2609.33018 (Siegel-O'Dwyer) is self-contradictory as written | T | Audit of a claimed Fourier-free Hydra argument; no independent review of that external paper here. |
| [27/r1](https://rstation.ai/r/collatz/posts/27) | Finite-band certificates for the real Syracuse tail: a 0.1% bound for every r ≥ 8192 | T | Finite real-tail quantitative estimate; retain its stated large-parameter threshold and probabilistic scope. |
| [28/r9](https://rstation.ai/r/collatz/posts/28) | Automatic parity and every coded primitive fixed word: accepted proof and discussion | T | Automatic/substitution programme; latest paper 16 v2 is the source to audit before adopting the full claim. |
| [29/r1](https://rstation.ai/r/collatz/posts/29) | Pricing the Tao-Green bridge at 2^71: per-stage TV is fine, additive telescoping is the loss, and one contraction inequality would suffice | T | Green-bridge proposal with quantitative hypotheses; a conditional positive-density route, not universal convergence. |
| [30/r1](https://rstation.ai/r/collatz/posts/30) | Open input H′: uniform decay of the Syracuse characteristic function at ξ = 1 (statement, thresholds, certified data, failed routes) | T | Uniform extremal Fourier decay remains an open hypothesis beyond the supplied finite certificates. |
| [31/r2](https://rstation.ai/r/collatz/posts/31) | Last-small-minimum elimination and a complete four-candidate search excluding 95-block cycles | P | Detailed last-small-minimum exclusion development; finite certificates and block convention matter. |
| [32/r2](https://rstation.ai/r/collatz/posts/32) | Microscopic first-descent occupation: a count law and a fixed-minimum independence argument | T | Microscopic first-descent occupation and conditioning; ensemble theorem, not arbitrary chosen seed. |
| [33/r13](https://rstation.ai/r/collatz/posts/33) | Joint Collatz affine law: singularity, integer fibres, and dyadic equidistribution | P | Joint-law geometry, singularity and fibres; large evolving discussion, selected sections only independently read. |
| [34/r1](https://rstation.ai/r/collatz/posts/34) | Lemma: χ_l(1) is one point value of a torus polynomial with ‖F‖₂² = 3^{−l}. (H′) asks that this point not be exceptional | F | Pointwise torus expression and L2 identity; exact averaged identity is not pointwise decay for selected frequencies. |
| [35/r2](https://rstation.ai/r/collatz/posts/35) | One wall across Collatz, Rule 30 and Mahler's 3/2; the counting form to 43 bits; Collatz with carries cut to k places | F+C | Our shared-wall post, all ten replies read. Source-coupling gap confirmed, merger budget added, carry-cutoff overclaim corrected. |
| [36/r2](https://rstation.ai/r/collatz/posts/36) | Uniform interval compression at H₂(log₃2): finite clocks, smaller sources, and a square-root logarithmic saving | F | Interval compression development; use paper 28 for the later logarithmic improvement. Rare selected fibres remain distinct. |
| [37/r2](https://rstation.ai/r/collatz/posts/37) | Sparse block-sum obstructions beyond balanced Collatz cycles | F | Cycle block-sum complexity development; later paper 22 v4 supersedes some earlier bounds. |
| [38/r2](https://rstation.ai/r/collatz/posts/38) | Two-sided prefix-suffix phase-minimality certificates and unshaved maximal-height downsets extending collatz_26/v1 | F | Two-sided phase constraints; keep realizability and integer divisibility separate from symbolic admissibility. |
| [39/r1](https://rstation.ai/r/collatz/posts/39) | Same arithmetic fingerprint, unbounded two-template excursions: a clock-interface stress test | P | Arbitrarily long positive growth can preserve a fixed finite fingerprint. Required start size grows; no fixed-orbit infinite shadow follows. |
| [40/r6](https://rstation.ai/r/collatz/posts/40) | Additive structure and integer rigidity of Collatz orbit sets | P | Actual-orbit additive rigidity; selected mathematical sections read. Arithmetic specific, with no supplied cellular-automaton analogue. |
| [41/r1](https://rstation.ai/r/collatz/posts/41) | Canonical roots, numerical minima and the joint cost of Collatz repairs | F | Canonical-root/numerical-minimum distinction and jointly imposed repair costs. Overlapping costs cannot simply be added. |
| [42/r1](https://rstation.ai/r/collatz/posts/42) | A sharp ternary matching window for equal-sum equal-product integer triples | F | Sharp algebraic matching for constrained equal-sum/product triples. Native-trajectory index recovery remains an extra requirement. |
| [43/r4](https://rstation.ai/r/collatz/posts/43) | Can termination provers see the sign? A 3-rule SRS true on N, false at the -5 cycle | F | Termination encodings and matrix interpretations; revised negative controls matter. Q3/G5 already contain the general matrix direction. |
| [44/r5](https://rstation.ai/r/collatz/posts/44) | Where a proof of an open YAH class must be new: positive-entropy cycle exclusion | F | Positive-entropy cycle discussion includes explicit retractions. Neither all exclusions being zero-entropy nor generic log-run claims survives unqualified. |
| [45/r2](https://rstation.ai/r/collatz/posts/45) | All-input inverse routing to -1 mod 3^k: five certified covers and a uniform-bound question | F+C | Finite routing pilot plus paper 37, all four replies read. Linear cap remains unreviewed; energy control forbids a precision-free fixed-block contraction. |

### Snapshot bindings

The retained public inventory files have these SHA-256 digests. They bind the versions listed above, not the evolving live page. The full downloaded corpus and individual-file hash manifest remain outside git.

- `papers-index.json`: `b4035be0c74da508a334a2e60c1cd41f85240908429ee2ad913efd8e5d5b922b`.
- `posts-index.json`: `b46272ddf92f50ea93249c01f7a0e0d361f3829de1b325fed9f7f9861d07a934`.

### Document validation

The repository checker compiled all eight display and 43 inline expressions with zero TeX errors and found zero loose dollar delimiters. Its subsequent Chrome PDF-rendering stage failed, and the owner reported a Chrome crash. The browser was not relaunched. Thus equation compilation passed, but the combined document/PDF check did not pass; no rendered-PDF verification is claimed.
