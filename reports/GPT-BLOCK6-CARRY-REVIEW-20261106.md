# Block6 carrying review

GPT GC2702, 6 November 2026. **Block6 DONE: scoped hand reads completed, with repairs.** The bridge return-state pull is parked for later. Nothing here proves Q01, C3, source-energy decay or a prize statement. Local's finite measurements remain attributed to the M5; the small independent replay below ran on GPT's Intel host.

| Item | Verdict | Submission consequence |
|---|---|---|
| L1573 Theorems1/2 | **PROVED hand/two-party**, with synchronous classes and K>=0 | Keep both; reject the asserted same-hypothesis replacement of CT4C |
| CT4 TheoremC / CT3 bridge | **PROVED hand/two-party**, finite-range hypotheses retained | Remains a conditional route to Q01; not merely a death-time estimate |
| XP3.1 | **PROVED hand/two-party after repair**, integer/rational densities | S-13 may be packaged with the free-middle, horizon and lower-bound guards |
| PE2.1 | **PROVED conditional reduction**, with independently replayed finite premise | Block9 may use the eight-word residual language; the exclusion itself remains open |
| CP3.2 reserve | **PROVED hand/two-party**, finite-row free-word population | S-12 complexity rung cleared for packaging; other CP3 claims not covered |
| P2-2.1(i) reserve | **PROVED conditional hand/two-party** | Source-energy decay implies every fixed dyadic residue has density1/2, hence Problems1 and2; decay remains open |
| LN06.1 reserve | **PROVED after repairs** for the stated encoding class | Positive distinct cuts, rule-local physical tick bits, corrected corollaries; novelty remains unestablished |

## Read scope and prior record

Complete carrying arguments and their mathematical-skeptic amendments were read from immutable packets `cited/local/sw02-all-20261106.tar.gz` (SHA256 c231157f6daeb1433d2c8aaf2e0190f78b5c4723009fdcc32ee8842a5c11d94c) and `cited/local/sw02-second-20261106.tar.gz` (a5bbfc81689042d31086424857663680481dd116ed3edacb2758058ef3938911). The XP-3, PE-2, CP-3, LN-06 reports and relevant skeptic reports were read completely; CT-3/CT-4, MM-1 and P2-2 were read through the statements, definitions and proof sections carrying the named claims. This is not blanket acceptance of those agents' other claims or numerical tables. A swarm skeptic is a self-check, not the worker's second read supplied here.

**Record searched:** `record_find.py 'free.middle|source.energy|crossing.word|class.amplifier|near.square'`, and the actual sources named below. Relevant hits include GC1772/local conservation barriers, the orbit floor in AM-1/CT-3 section6/MM-1, CorollaryF and G52's phase guards, the kit's local conservation and zero-boundary barriers, the portal's source-energy theorem, and crossing sequences in `OneTapeRegular`. Cloud CL752's source comparison remains the prior-art register for the queue. A clean keyword search is not novelty clearance.

Last successful complete index refresh: portal 2026-11-06T19:30:33Z, kit `9d837cd5e5ac447cd868c20aebf49a1b4cfa866e`, 30 open PRs, zero added/changed indexed entries. The exact primary declarations were read, not inferred from index hits: `Rule30LocalConservation.cyclic_conserved_iff_shift_coboundary`, `Rule30ZeroBoundaryBarriers.no_local_ranking`, `Rule30CoupledEmptyRight.not_coupled_of_right_masked_periodic`, `Rule30PeriodFourSkeleton.C3` and its tail reduction, portal R30-20261028-e34744's `skeleton_0011_leftmost`/`skeleton_0011_finite`, portal R30-20261104-6a0257's energy definitions and `problem2_of_source_energy`, and `Rule30LeftAntiPeriod.problem1_and_problem2_of_all_dyadic_subseq_halfDensity_lt`. No new Lean build, public submission, Lean Verified or Human Verified status is claimed.

## 1. Class counts: two true theorems, two different hypotheses

**Definition repair.** N_k(W) counts different rows at the **same physical tick** t0(W)+2k, among the original width<=W starts that have passed every required check. It is not an equivalence class under arbitrary time shifts along one orbit. The latter would identify the very rows used in the floor. N_k is a nonincreasing integer sequence; q(W) is its eventual constant value. Count ratios include both deaths and further coalescences. They are not automatically the fraction passing the next check among a fixed deduplicated population. CT-4's fixed population and Block5's repeated deduplication must not be identified without a no-further-merging proof.

**Theorem1 carried.** An immortal row y of width w supplies G^j y for all j with w+2j<=W. At one common later tick t their widths are w+2j+t, all distinct. Therefore q(W)>=floor((W-w)/2)+1. Conversely Q01 kills every member of the finite initial population, so q(W)=0. Thus q(W)=o(W) along any unbounded set of widths implies Q01. This is the known orbit floor, restated here.

**Theorem2 carried, K>=0.** Suppose at every k with N_(k-1)>K²,

`N_k <= (N_(k-1) + K sqrt(N_(k-1)))/2`.

If the eventual plateau q exceeded K², substitution at a late check would give q<=K², a contradiction. Hence q<=K². Combined with the floor, K(W)²<=cW on unbounded widths, for fixed c<1/2, implies Q01. This does not force q=0 at a single width; the comparison across unbounded widths matters.

**Replacement refused.** CT4C assumes control only while the *ideal* count M_k=P*2^(-k) is at least98K². The new theorem assumes a one-sided bound at **every time** whose *actual* previous count exceedsK². These are different hypotheses. For an explicit abstract count sequence, take K=1, P=2^r, r>=7; halve until N=M=128, then keep N=128 forever. Every check in CT4C's range M_k>=98 has beta=0. The new law fails as soon as the plateau begins. This is a logical separation of assumptions, not a proposed Rule30 orbit. GPT supplies this explicit sequence as a hand self-check (PROOF-SKETCH pending Local carry); the distinction between the two source hypotheses is directly checked.

**CT4C carried as well.** Write N_k=M_k r_k. Under `|beta_j| <= K/sqrt(N_(j-1))` through m, with M_m>=98K², induction keeps r_j>=1/2. Indeed the geometric sum of the beta bounds is at most `(2+sqrt(2))*K/sqrt(M_k) < 3.42*K/sqrt(M_k)`. Every beta has magnitude below1/2, so log(1+beta)>=-2|beta| gives

`|log r_k| <= 6.84*K/sqrt(M_k)`.

At the threshold, 6.84/sqrt(98)<log2, closing the induction strictly. These constants can be checked without floating arithmetic using sqrt98>=9899/1000 and log2>=842/1215. For K>0 choose the last m with M_m>=98K²: then M_m<196K² and N_m<392K². If P starts below98K² it is already small. K=0 can be handled separately, or enlarge K to at least1. Consequently K(W)²=o(W), under this **finite-range** law, contradicts the immortal floor. The stronger all-time hypothesis improves the sufficient coefficient from c<1/784 to c<1/2; this is not a constant improvement under unchanged assumptions.

**Interpretation repairs.** Finite coin-like tables alone do not bound q uniformly in W. But bulk control is not logically idle: any proved finite-time bound N_m(W)=o(W) contradicts the orbit floor, even if later counts are uncontrolled. The law also rules out every plateau aboveK², not only permanent ones. A class amplifier would be useful; it is not a necessary prerequisite for every count argument. Repeated uniform contraction remains a possible route; one isolated contraction at one check does not suffice by itself. The measured K and degree-3 tables are not independently rerun here and do not establish a uniform law.

## 2. XP3.1: free middle survives the review

**Carried version.** Let r>=1, wall/edge widths w,e>=1 and w,e>=r-1. Let h be an integer density on r-windows. Write

`R(Y)=beta(width(Y),wall_w(Y),edge_e(Y)) + sum of h over in-row windows`.

Let u(W) be natural-valued and tend to infinity, L(W)=max(W-u(W),0), and A the finite zero-wall rows surviving the prescribed even checks through L(W). If R>=-KW on A for a fixed K, and R(GY)<=R(Y) for Y in A, then h is a cyclic G-conserved density. By the kit's conservation theorem it is constant plus a shift coboundary; R therefore depends only on width and its two boundary windows. There is no Nat-valued such R strictly descending on A. Rational h follows by clearing denominators. This read does not extend automatically to arbitrary real h.

**Balance repair.** A nonzero cyclic rise can be made a positive cyclic rise because each local output r-word under two Rule30 ticks has exactly16 preimages among r+4 free input bits. Take a cyclic input period at least r+4 (repeat an existing periodic witness first). Sum over all inputs and all window positions. The mean rise is zero, so a negative witness forces a positive one. This is local left-permutive balance, not invertibility or uniformity of a whole finite ring. In fact the all-zero and all-one ring rows have the same all-zero image after one tick.

**Carrying construction.** At width W_n=W0+2n put a stripe prefix of length L(W_n)+w+3 at the wall, then a growing repeated positive-rise word in the free middle, and an edge label E_n on a cycle of the finite edge update. The prefix guarantees the required survival and fixes the wall data. The number m_n of positive-rise repeats tends to infinity since u(W)->infinity; interface errors are bounded independently of n. If B_n denotes beta at these boundary labels, nonincrease forces `B_(n+1)<=B_n-m_n*rho+C`, rho>0. Hence B_n/n tends to minus infinity, while R>=-KW and bounded h force a linear lower bound for B_n. Contradiction. The lower-bound assumption matters: width-dependent terms with quadratic negative drift can otherwise mask a rise.

**Rank restriction repair.** One cannot simply apply a theorem on all rows to the smaller population A. The actual proof of `no_local_ranking` uses finitely many iterates j<=j2 of arbitrarily long stripe truncations; j2 is fixed after the edge pigeonhole. At width W these iterates survive through W-4j. Increase the initial truncation length until u(W)>=4j2 for every relevant later width. Every row used by that proof then lies in A, and the same rank contradiction works. This also handles Nat-valuedness required only on A. Bounded u is not covered, rather than refuted.

**Scope:** S-13 may retain this strengthened survival-population barrier with its hypotheses. No conclusion about all dissipative potentials, nonlocal rankings or Q01 follows. Other XP-3 LP tables and claimed late-survival barriers are outside this read.

## 3. PE2.1: the residual language, with all SCCs retained

Let the boundary driver be0011, with phase0 its first white tick, and u(m) column1 at times T+4m. The independently reconstructed phase-labelled width17 graph forbids, inside **every** cyclic SCC,

`F={010,1001,10001,01101,01110,011110,0111110,10110}`.

An actual driven right-half history gives an infinite path in this graph, even when the right half is infinite. A path in a finite graph eventually remains inside one cyclic SCC. Therefore **every driven right half eventually has u avoiding F**. This finite-language consequence needs no finite-left assumption and no rejection of components merely because their output is periodic. Seven words are already absent at width13; `10110` is admitted at13/16 and absent at17. The earlier width18-only wording is corrected.

**Reduction carried.** For a left-finite actual0011 tail, the primary leftmost-black skeleton theorem gives eventual column1 phases `(u,1,1,0)`. The cell rule then gives column-1 phases `(u,0,0,1)`. The effective left boundary remains the actual product of consecutive driver bits; it is not replaced by a free driver. Choose a later phase-aligned origin after the skeleton and language onsets. A hypothetical left-finite0011 tail then supplies a finite left start fitting that skeleton with u eventually avoiding F. Thus excluding **this narrower compatibility population** suffices to exclude the original tail. C3 implies the restricted exclusion; strict logical weakening is not established. Neither exclusion is proved here. Finite left is essential at the skeleton/exclusion stage, not at the all-SCC language stage.

Primary-source population is explicit: portal R30-20261028-e34744's `skeleton_0011_leftmost` covers left-bounded configurations, and `skeleton_0011_finite` covers finite nonzero configurations. The kit's seed-specific skeleton is not silently applied to arbitrary rows. The master masked-periodic coupled theorem is likewise read with its finite-left and phase hypotheses. No claim that PE-2's whole graph census, larger widths or periodic rigidity tables have been certified is made.

## 4. CP3.2: the complexity rung

For the free word f of any finite constrained zero-wall row, **for every K, eventually p_f(n)>n+K**. This is conditional on membership in that row population, which could be empty. For a coupled application, the corresponding reconstructed left row must actually be finite; an infinite reconstruction is outside the statement. Complementation preserves factor complexity.

The carrying word argument is sound. For a non-ultimately-periodic binary word, p(n+1)-p(n)>=1. If p(n)-n stayed bounded along infinitely many n, its nondecreasing integer values would eventually be constant, so exactly one factor is right-special at each sufficiently large length. Such a word has no arbitrarily long factors of any fixed period q: take two long maximal q-runs A,B with the same starting q-word, |B|>=|A|+q+1, away from the initial position. Their preceding breaker is the same binary complement. The factor breaker+A has two right extensions, while a q-periodic factor of the same length at the end of B also has two extensions (compare its copy one period earlier). These are distinct right-special factors, a contradiction. Runs beginning at0 cannot provide an unbounded exceptional family unless the whole word is periodic.

Among the first n+K+1 length-n factors, two agree, at i<j<=n+K. Their overlap has length n>=j-K. Their lags cannot remain bounded, by the preceding fixed-period argument. These are near-squares at unbounded lags with fixed slack, contrary to the finite-row version of CorollaryF.

**Frame check.** The last implication needs the zero-wall row version, not an unguarded import from a whole-line alternating-center statement. Repeating f-blocks of length ell at i<i' makes G^iY and G^i'Y agree through depth2ell+1 by the two-step shift identity. Earlier-row support ends at W+2i. The usual left-diagonal recurrence supplies eventually black diagonals of arbitrarily large index b. Choose b>=W+2K-1, then 2(i'-i)>b and a late enough i'. The later black cell at depth W+2i'-b lies beyond earlier support yet inside the agreed range, contradiction. The source's diagonal proof uses the nonzero leading black edge, eventual power-of-two periods, reset forcing, and no adjacent eventually-white diagonal pair. It does not assume arbitrary near-squares align to the wrong phase. The proof establishes the rung, not a uniform quantitative rate for p(n)-n. Other CP-3 claims, in particular phase-zero Rote variants, are not carried by this reserve read.

## 5. P2-2.1(i): source energy controls every fixed dyadic class

For any sign sequence z, put N=2^n, S_n={0} union {2^j:0<=j<=n-2}, and `E_n=sum_(0<=u<N) (sum_(s in S_n) zext_N(u+s))²`. There are n shifts. If `E_n/(N*n²)->0`, then every fixed residue class r modulo q=2^a has mean zero.

For completeness, let T={u<M:u=r mod q}, D=sum_T z. The n-a good shifts0 and2^j, j>=a, preserve the residue. A shift s=q*k changes the truncated interval sum by at most2k; each of the a remaining shifts contributes at most|T|. Cauchy-Schwarz gives

`(n-a)|D| <= sqrt(|T|*E_n) + a|T| + sum_(j=a..n-2) 2*2^(j-a)`.

Choose dyadic N with N/2<M<=N. For fixed a,r, N/|T| stays bounded, so after division by (n-a)|T| the first term tends to zero with the normalized energy, and the remaining terms are O(1/n). This handles arbitrary prefix lengths of the residue class, not just dyadic endpoints.

For center signs z=1-2*center, every fixed dyadic class therefore has density1/2. The exact kit theorem requires only one residue per exponent, so yields **Problem1 and Problem2**. The a=0 density implication is already portal R30-20261104-6a0257's theorem; the hand extension to fixed dyadic residues is the carried fragment here. The portal's integer hypothesis `for every k>0, eventually 8*k²*E_n<=N*n²` is equivalent to the little-o condition. Neither that hypothesis nor either prize conclusion is established unconditionally. Other P2-2 energy/spectral claims are not part of this read.

## 6. LN06.1: crossings, encoding repair and limits

**Carried class.** A fixed finite string-rewriting system, each rule having nonempty left side and no shrinkage; lmax>=2. Use a depth-ordered encoding `P(Y1) phi(Y2)...phi(Yw) v`, with fixed first-block map P and fixed **nonerasing** phi. More generally the proof needs every designated cut to be positive and the cuts distinct. The first-block form includes R_Q literally. Tick redexes contain the first letter; tick bits are functions of the applied rule and count consecutive **physical ticks**, not just the even black checks. Keep soundness for every derivation in the specified input population.

**Carrying splice proved.** Track a cut at its unchanged offset within each rewritten redex; nonshrinkage preserves positive ordered distinct cuts. Record each crossing as (rule,offset). If two crossing words agree, interleave the left-only projected rewrites of one derivation and right-only rewrites of the other, synchronizing the crossings. The two sides fit the recorded redex at each synchronization. The spliced run retains exactly the first run's anchored ticks and their rule-local bits: a right-only step cannot contain the first letter. Each rewrite crosses at most lmax-1 cuts and the crossing alphabet has at most E=|R|(lmax-1) letters.

TheoremA's stripe cuts then give the source bound `|D_n| >= m/(2(lmax-1))*log_(E+1)(m/2)`, m=(n-1)/2, odd n>=3, when the maximum tick count N(n) is strictly increasing and attained. Equal short crossing words would splice out an even stripe block, preserve all N(n) ticks and contradict the shorter stripe's maximum. Under the original erasing-morphism wording, the skeptic's assertion that the first cut must be positive is not justified: P(1) and phi(0) may be empty. The carried nonerasing version avoids this issue and fits R_Q. A weaker general encoding theorem can discard exceptional zero cuts and restate constants; it is not silently accepted here.

For TheoremB fix an even input prefix. Survivor completions have 2^(floor(W/2)-p/2) choices. The first W wall bits determine a width<=W input by the triangular left-permutive dependency. Equal crossing words for two different nonempty tails would splice one completion onto the other's first W ticks and contradict that injectivity. Count crossing words, average, then sum over cuts. This yields the stated mean lower bound `W²/(16(lmax-1)*log2(E+1))-O(W)`. Derivations may be truncated at their Wth tick.

**Corollary repair.** TheoremA alone does not imply unbounded rewrites per tick: its N(n) may be exponential. The skeptic's counter system `W1->W0`, `W2->W1` (ticks), `01->20`, `02->21` has N(n)=(2^(n+1)-1)/3 on odd stripes and total rewrites2N(n)-(n+1)/2. The value sum d_k*2^(k-1) and potential sum d_k*(2^k-1) prove these counts. It is not an F encoder. Require N(n)=o(n log n), or use TheoremB truncated at W ticks, for the per-tick conclusion.

TheoremA still excludes a globally linear bound on **all rewrites** in this class. Therefore it excludes the specified one-shot all-rules-strict arctic interpretation with linear initial potential, and match-bounded systems. The primary [Geser–Hofbauer–Waldmann paper, Proposition2](https://intranet.csc.liv.ac.uk/~coopes/comp319/2016/papers/nia-matchbounded.pdf) was checked: match-bounded string systems have linear derivational complexity. Relative arctic interpretations count strict tick steps instead; they are not ruled out by this argument. Shrinking systems, moving tick anchors, nonlocal output labels, random access, DAG encodings and unrestricted algorithms lie outside. No Problem3 lower bound or new R_Q execution is claimed. The method is classical and statement-level novelty remains open.

## 7. Independent finite replay and evidence

The separately frozen [checker](../tests/probes/swarm/sw02/block6/finite_language_check.py) (SHA256 9631564ddb0288418b56ae5ed2dab26cef4069b717640aee4b22412d9d6951af) reconstructs all phase-labelled transitions and all cyclic SCCs, then propagates complete subsets while spelling each word. The source is independent of the original C implementation. Scalar-cell successor checks and rules90/150 controls pass. At width13/16 the `10110` endpoint counts are26/96; at17 every named word has zero endpoints. No cyclic SCC is discarded. Local balance controls r=1,2,3 have exactly16 preimages per local output word, with the whole-ring non-bijectivity negative control retained.

**Receipt:** one frozen stage, COMPLETED rc0, 1.130513 accounted CPU seconds plus0.149 outer-supervisor CPU, 1.18 mathematical-worker wall seconds, sampled peak tree RSS127.28MiB, minimum headroom5153MiB, swap growth0, no stop/failure. Limits were120 aggregateCPU/300wall, individual100CPU/240wall, tree8192MiB RSS, launch4096/running1024MiB free-memory floors,4096MiB swap growth, max6 processes,16MiB/file and128MiB/stage. No retry, GPU, new width search or active job. Raw receipts/results: `cited/gpt/gc2702-block6-evidence-20261106.tar.gz`,3970bytes,SHA2564c0990d7aac42c5d24fe4ab4a81536443da64a935cf2f1efd044fcc4cbed93f6. Archived path redactions are declared alongside raw and archived hashes; mathematical data are unchanged.

## Next executable step

Block7: Local owns the first submission, S-01. The frozen essay/notebook/receipts are now reviewed PASS in [GC2703](GPT-S01-RELEASE-REVIEW-20261106.md), without rebuilding unchanged proofs; return the readiness verdict to the owner. Posting still requires the owner's word. Then S-03, S-02 and S-04 in queue order as their own packets clear. S-13/S-12 have hand carries, not ready-made submission packets. Bridge research and schedules remain paused.

My own pull: the bridge return state remains logged for later; no bridge work was launched in this review block.

## GC2701 finite-premise replay freeze

Before any numerical execution, independently reconstruct the PE2.1 phase-labelled graph for driver0011 at widths13,16,17. Use scalar-cell truth tables to control the vector successor construction, SciPy SCCs, and complete subset propagation inside each cyclic SCC to test the eight named words. Expected: seven words absent at13;10110 present at13/16 and absent at17. Rules90/150 at width5 must admit every tested word. No SCC is discarded merely because its column label is periodic. If all SCCs avoid the words, this gives the stronger eventual language statement for every driven right half, without a finite-left premise; finite left remains in the later exclusion argument.

Also replay XP3.1's local balance: at radius r=1,2,3, each r-bit output block after two ticks has16 preimages among r+4-bit cyclic inputs. The global ring map is not claimed bijective: all-white/all-black is a direct negative control. General-r balance is carried by the kit's local left-permutive counting theorem, not this finite sample.

Any control/count discrepancy withholds the affected language claim, retains the evidence and causes no wider retry. This is one fixed finite replay, not a new width search or a certificate of CQ01/C3. Source SHA256 9631564ddb0288418b56ae5ed2dab26cef4069b717640aee4b22412d9d6951af; generated serial plan 8bd4e5a0f50a1cc0d0828020e844f6248a9015cadaefff8b984590d9e89b37fe. One mathematical worker, one thread, nice10;120 aggregateCPU/300wall, worker stop105 plus reserved15 for outer supervision; individual100CPU/240wall. Tree RSS8192MiB, launch headroom4096MiB/running floor1024MiB, swap-growth stop4096MiB, max6 processes including wrappers/monitors;16MiB/file,128MiB artifacts. Existing run_capped and CPU-only stage driver enforce tree/pressure/thermal/artifact gates and aggregate reaped/live worker accounting. No GPU, automatic rerun or enlarged graph.

**Record searched:** complete PE2 report and mathematical-skeptic repair, full XP3 report/skeptic and actual kit local-conservation/barrier statements. Current known_find refresh19:30:33Z, kit9d837cd5,30 open PRs, no additions/changes. This replay supplies finite premises for a carrying read, not novelty clearance or a new Lean/public-verification status.
