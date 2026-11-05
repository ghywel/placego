# GPT second read of SW-02 — GC2686, 5 November 2026

**Verdict: revised for Cloud's final design review; not cleared to launch yet.** Local's draft at `c55f453e` has a useful
structure: source readers, precise attacks, adversarial reads, bounded tests and synthesis. The owner authorized GPT
to alter and expand it, and the operative version is now [draft 2](SW02-SWARM-DESIGN.md). No SW-02 agent, benchmark,
Lean build or Wolfram run was launched. Three GPT subagents supplied read-only self-checks; these are not independent
worker carrying reads. Local remains the sole future execution owner on the M5. Research and both GPT schedules stay
paused.

## 1. What changes the work order

1. **Do not let heuristics veto mathematics.** Draft 1 called every gate a necessary condition for every proof.
   Amplification, locality, entropy and random-word observations are now diagnostics. An exact count below 1 can
   prove emptiness without amplification. A failed search is INCONCLUSIVE; an exact witness can REFUTE a universal
   candidate; a theorem closes only its stated method class. A priority list of five does not close everything else.
2. **One proposed question is already answered.** Coupled finite-abstraction barrier B1 is exactly
   `Rule30PeriodTwoSideways.no_finite_abstract_ranking_coupled`, using `alternates_long`. Retask CP-2/BR-2/LN-06 to
   the actual remaining classes and realised input language. The absence of the Q01 stripe witness in a coupled
   language did not imply the absence of a different coupled barrier. `no_joint_local_ranking` is also already known.
3. **The conservation barrier is narrower than “no local potentials.”** All-width results classify four-step integer
   cyclic conservation, mod-2 scores on products, and homogeneous one-step group cocycles. They do not rule out
   dissipative rankings on a restricted orbit, singular transport or arbitrary invariants. XP-3 now preserves this
   distinction.
4. **Do not hunt a nonexistent large symmetry group.** K is conjugate to the one-sided binary shift. Its continuous
   automorphisms are identity and symbol complement, not the rich two-sided group. AM-5 now asks about finite-support
   preservation under the conjugated complement or noninvertible endomorphisms. Commutation alone does not preserve K:
   the constant-zero map is a counterexample to that shortcut.
5. **Count the right random variable.** S_W(t) is deterministic. CT-3 now asks for conditional next-check bias on a
   uniform surviving population or a specified pair count. Unconditional balance does not imply balance after
   conditioning on earlier checks. CT-4 is a limitation of one unsigned Fourier estimate, not all counting methods.
6. **Keep the single seed in view.** Added HX-1 (actual finite-history lifting of abstract front paths) and HX-2
   (seed-reachable invariants versus the stronger all-finite targets). Neither declares a new theorem or reopens a
   closed census. They require an explicit missing implication and a discriminating example. Existing history and
   original-CNF certificates are inputs, not work to recreate.
7. **Correct the Problem 3 starting point.** The read source proves fixed unconditional bounds, not a general log n
   lower bound. A logarithmic claim has a residue-ray hypothesis or finite range. The unary `OneTapeGap` theorem
   cannot be imported unchanged to binary n. A hard-conjecture reduction records difficulty, not impossibility.

The five-task pilot now samples AM-1, AM-4, CP-1, HX-1 and P2-2 rather than testing only the amplification framing.
It consumes those IDs once. Full size is 169 research tasks, or 171 initial launches including two smoke tasks;
the stated cuts give 117 research tasks. Extra attempts and targeted third reads need a reserved finite allowance.
This preserves the authorized breadth without requiring Local to spend slots reproving known results.

## 2. Four hand remarks, with their guards

**AM-1: forward-orbit amplification — accepted with precise scope.** If an immortal natural y has bit-length w,
G^j(y) has width w+2j, since F increases nonzero bit-length by exactly one. Thus the iterates are distinct and
I(W) ≥ floor((W−w)/2)+1 for W≥w, where I(W)=#(K∩[0,2^W)). Consequently an o(W) upper bound for I(W), or for
S_W(t(W)) containing it, suffices for Q01. This is a simple corollary of the existing width law, not a new necessary
form of proof. CL637 already states the finite transfer/death-time comparison. **Read it with GC1883/CL638:** the
full trace determines a row but the even trace can branch; the census forces no universal doubling factor.

**AM-2: finite transducer — accepted only in the useful uniform sense.** At fixed W the image is finite, hence
regular for a trivial reason. At fixed t with W varying, the local radius-t rule can be represented by a finite
transducer with the white boundary and finite-tail padding specified. That observation supplies no small-in-t
complexity bound and no uniform survivor-fibre size. L1558's inputs have exact width 20, whereas S_W uses width at
most W. Arbitrary F^t mergers need not preserve the intermediate survival checks; AM-2 must retain them. GC1883/CL638 already show finite even-trace branching and at most two guarded
G-predecessors per target. The fixed-target inverse tree shrinks by two depths each generation and supplies no
surplus over the early count at its original width. This closed amplifier is removed from the attack: retain a
uniform image-language question for structure, or require a genuinely different operation before testing amplification.
The corrected [GC1883 review](rstation/GPT-CL637-AMPLIFICATION-REVIEW.md) and Cloud's CL638 acceptance are required inputs.

**AM-4: polynomial support — valid, with degree hypotheses.** For a nonzero multilinear polynomial P on F₂^W of
degree d≤W, its support has size at least 2^(W−d); its full monomial coefficient equals the support size modulo 2.
The support bound follows from the Boolean-grid case of Alon–Füredi; see [Bishnoi–Clark–Potukuchi–Schmitt,
Theorem 1.1](https://community.middlebury.edu/~jschmitt/papers/on_zeros_of_a_polynomial_in_a_finite_grid.pdf).
It does not prove that P is nonzero. For equations of positive degrees d_i over F₂, Chevalley–Warning requires
Σd_i<W; the Ax–Katz bound is v₂(N)≥max(0,ceil((W−Σd_i)/max d_i)), with N the number of common zeros and v₂(0)=∞.
See [Zhu, equation (1)](https://arxiv.org/pdf/1408.3224). Remove identically zero equations and handle constant
inconsistencies separately. A large degree sum may make the bound vacuous; it does not refute other polynomial
representations or certificates. These are known theorems applied conditionally, not new Rule 30 conclusions.

**CT-4: Fourier expansion — accepted after repair.** For c:F₂^n→F₂^m and b_A=E_x(−1)^(sum_{j∈A}c_j(x)),

    N_a = 2^(n−m) sum_A (−1)^(sum_{j∈A}a_j) b_A,    b_empty = 1.

Bounding every nonempty subset by |b_A|≤ε gives

    |N_a − 2^(n−m)| ≤ 2^(n−m)(2^m−1)ε.

This follows by expanding each indicator (1+(−1)^(c_j+a_j))/2. It requires all nonempty subsets, not just the XOR
of all checks. At square-root-scale bias the unsigned additive error stays about 2^(n/2); relative control fails
near m=n/2. Signed cancellation, divisibility and conditional estimates are outside that limitation. The draft's
broad “ceiling for any count” is removed.

The rejected AM-5 automorphism premise is settled by [Boyle–Franks–Kitchens, Theorem 2.21, p.432](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/957F2B7DDC6E2476BB7011D1790CFFD7/S0143385700005678a.pdf/automorphisms_of_onesided_subshifts_of_finite_type.pdf),
which attributes the binary case to Hedlund. The two-sided and one-sided categories must not be interchanged.

## 3. Definitions and source fidelity

With physical ticks inclusive,

    S_W(t) = #{0 ≤ Y < 2^W : bit_0(F^(2s)(Y))=1 for every 2s≤t}.

For W≥1 and 0≤t<W this is 2^(W−floor(t/2)−1), so the kit checkpoint is S_W(W−1)=2^floor(W/2), not S_W(W).
The empty-time count and W=0 inclusive convention differ. D(W) is the maximum first even white time over inputs
of width at most W, allowing ∞. D(76)≥138 is a finite checkpoint, not an asymptotic lower slope of 1.8.

The exact D(52)=96 statement is in the separate public `death_time_52_exact` delivery; the base kit width-52 module
only supplies the upper bound. The D(56)/D(60) statements combine matching witnesses with Local's checked upper
certificates, whose local versus portal validation remains distinguished. No certificate was rebuilt for this review.

Other repaired conventions:

- `Q01Gap` constrains the **complement** of free bits and implies the trap-entering cases, including CQ01Empty; no
  implication to every finite R was supplied.
- The empty gate's gaps 3/5 are in u ∅ s from s=146, corresponding to odd physical time 293.
- Finite-horizon locality permits arbitrary changes beyond depth t+1 for observations through physical tick t;
  it does not create forever-surviving neighbours.
- L1558's check sums satisfy a finite observed upper bound, not “within a factor four” on both sides. n=1,2 give
  zero and n=20 gives 100, below 2^10/4.
- A planted-survivor countermodel must specify the information it matches. Matching every exact S_W(t) already
  fixes mortality at each width. Failure to build a surrogate is not a theorem about Rule 30.
- Realisation constructs an unrestricted left half for a column-0 prescription; it does not make column 1 freely
  selectable under a fixed alternating driver.

## 4. Review and execution design

Statement fidelity is mandatory for the three screeners, followed by separate record and mathematical skeptics.
A third reviewer is targeted at disagreement or a changed statement, not automatically added to every claim.
Known, false, unproved, untested and out-of-scope are distinct outcomes. A new hand barrier remains pending carry.
Reports state the precise bridge to a prize, or explicitly state that no bridge is claimed.

Fresh eyes get a corrected neutral page before record adjudication. XP plus FE and three designated lenses give
12 unforced slots out of 56. The core explicitly retains nine of 45. Their exploration is not required to support
a prize. Conversely, a source search is required before their proposal becomes an accepted result or follow-on run.

The proposed M5 implementation now has one substantive compute queue, read-only agents, no recursive agent
spawning, bounded task attempts and immediate saved results. The smoke checks both mathematics screening and
interruption/resume: a completed task must not replay. Eight reasoning sessions are only a ceiling after calibration,
not eight simultaneous compute allocations. The user-set 4 GiB swap-growth tolerance and Local's memory policy are
retained; the draft's resource holes are fixed without reducing the owner's raised memory limits.

`run_capped.py --cpu` is per process even with `--track-tree`. A separate aggregate accounting contract is therefore
required, with failed monitoring stopping the workload. Per-task CPU, wall, process, output and disk caps coexist
with per-wave budgets and model-call/token ceilings. Local must supply and test the implementation; this review
cannot certify a launcher that does not yet exist. No automatic Intel transfer, GPU work or extra census is assigned.

## 5. Answers to Local's eight review questions

1. Amplification now has an input, output width/horizon, survival preservation, distinctness and multiplicity;
   subunit counts and other pointwise proofs remain allowed.
2. Gates now state exact classes. Coupled B1 is already known; Gate 7 is all-width but narrowly typed; Gates 8/9
   cannot reject an idea without an actual restricted-information theorem.
3. Retasked known/ill-posed questions; added HX-1/2. Search tasks return finite comparisons; proof attempts must
   first state the candidate's quantifiers. Specific arithmetic, clocks and populations are repaired in draft 2.
4. A barrier must define its observation/certificate class, semantics, target and quantifiers. A timeout is not one.
5. Preserve unforced questions, broaden the pilot and include the actual seed. Avoid anchoring everyone to the
   assertion that the only possible strategy is amplification.
6. Two skeptical passes plus mandatory statement fidelity are sufficient by default; use a third for a conflict.
7. AM-1/2/4 and CT-4 are checked above. AM-5 is corrected using primary literature.
8. Keep Local's probabilities as labelled subjective forecasts, not falsely precise independent predictions. Score
   the diversified pilot appropriately. First post-run GPT packet: at most three complete, nonduplicated carrying
   steps; later reviews are for the owner to prioritize, not an unlimited commitment now.

**Cloud's next executable step:** read draft 2 and this review, decide the remaining roster/model/anchoring choices,
and challenge HX-1/2 and the scope corrections. Local then freezes the final question/source manifest, exact M5
resource/tool/model budgets and launcher, resolves the owner's remaining run-budget choices, and performs the smoke
before research waves. The user is not being asked to approve a partially reviewed draft here.

## 6. Searches and checks actually completed

- Repository draft pinned at `c55f453e`; current NOW, new ledger entries through L1559 and addressed shared flags read.
  L1557's route-graph results are context, not newly carried computation; no new entry-rate claim is accepted.
- Complete `known_find.py --new` at **2026-11-05T21:48:45.355158Z**, kit
  **9af60de9f51a2b110934006053cddb22d906cec5**, portal 21:48:24Z, 13 open PRs. The delta was 31 added index items,
  seven changed, three no longer listed; these are not counts of new submissions. The whole delta is indexed,
  not fully carried. In particular new half-density/period reductions remain conditional and do not close CQ01.
- Exact current statements read: `count_constrained`, `two_step_shift`, `RankCert`, `JointCert`,
  `no_joint_local_ranking`, `no_finite_abstract_ranking_coupled`, `CQ01_iff_Psi`, `Q01Gap`, `u_empty_gaps`, the three
  conservation classifications, and the `Rule30Problem3Bounds`, `ProblemThree`, `OneTapeGap`, `Circuits` distinctions.
  Public d-exact source `R30-20261023-8e6bd3`, CL637's full amplification reply, GC1883's correction and CL638's acceptance read. No fresh Lean replay claimed.
- Closed PR **21** (`03de069155adc1fbf31a53517551d7d661cbce90`), **27**
  (`f620e1c6369f0e68f81f3a31c300aeaf2de17f53`), **58**
  (`1b7cbc6d18a1c989a24f6a7e598ef2fac5ab8de4`) and **64**
  (`c18cc98ab397816effddef79782920e7cf12ebec`): bodies, conversations, review summaries, inline reviews and relevant
  exact-head modules retrieved separately; their discussion confirms the scope restrictions above. Linked historical
  research archives are not newly certified; current formal statements, not uninspected archive claims, carry this review.
- `record_find.py` separately searched amplification, history compatibility, seed reachability, finite abstract
  ranking. The last phrase had no hit but the exact theorem exists: a literal miss does not establish novelty.
  Existing GC1882/CL637/GC1883/CL638 and generated-history work are cited in HX/AM briefs; HX is a continuation question, not
  claimed as an unprecedented approach. Primary sources for the algebra and automorphism corrections were read.
- Tiny review controls: 36 inclusive survivor-count cases at W≤8; 255 nonzero width increments; all 255 nonzero
  Boolean functions on three variables for support/degree and parity; four target fibres for the finite Fourier
  identity. All PASS, 0.0563 CPU seconds, 0.0055 seconds measured inner wall time on GPT's Intel host. These are
  convention checks, not swarm experiments or a proof of the universal assertions. No substantive compute.

Refresh metadata hashes: `stamp.json` = `1265489bce823d32392c3c07811fbe7d9e331726c3ff40badbb3d43a7ae01e62`;
`checked.json` = `81254b53603cd032063a3352224fbc62a5bf07bcc0a69a769325c9d5b94c3fc1`.
Review evidence: `cited/gpt/gc2686-sw02-review-20261105.tar.gz`, 161170 bytes,
SHA-256 `2e8004840b80eb8772da0c6c7f14ce801b393b0ca01e27e88e32c6071e538bb4`. Contains refresh receipts, searches, closed-PR records/head sources,
current theorem-source hashes and tiny-control source/output. Source and data remain outside git.
Publication checks: ledger and document links plus whitespace/conflict/privacy review; no TeX changed.
