# The prize swarm of 2026-10-22: twelve agents on the smallest open Erdős prizes

*Split of 2026-10-28 (Local, at the owner's request).* This file had reached 310 KB, 247 KB of it the appendix of
the twelve agents' verbatim reports. That appendix moved unchanged to
[archive/PRIZE-SWARM-reports.md](archive/PRIZE-SWARM-reports.md), and its section below now lists the reports
and links there. Everything else is unchanged.

*Designed, run and consolidated by Claude (Local) on the M5. The launch is in CHAT-LEDGER.md L750 and this file is
reported in L751.*

**The owner's request** (2026-10-22, about 10:00 BST), in substance: 29% of the week's budget remains and it resets in
an hour, so use it. Design a swarm in which each agent takes a different new maths problem and works it in reasonable
detail. Problems may be chosen by instinct, but no two agents may share one. Prizes come first, chosen from the lowest
cash prize up, and the high-cash, high-difficulty problems are left to others. The aim is as much simultaneous maths
as possible.

**The design.**
- *Problems.* Twelve agents ran in parallel from 10:08 to about 10:50 BST. Each took a different open problem from
  erdosproblems.com's prize tiers, from the bottom up: \$10, \$25, \$44, \$50, \$78, then \$100. Each had its own
  backup.
- *Shared brief.*
  - About ten minutes on status and the record (`record_find`), the rest on mathematics.
  - A pull named by instinct, predictions before each run and one unexpected check.
  - Every result labelled PROOF-SKETCH, MEASURED, KNOWN, HEURISTIC or NEGATIVE.
  - One core per run, with a time limit; installed tools only.
  - No git, no posting, no sub-agents.
- *Second passes.* Agents that finished early were sent back for a second pass on their own "next hour" plans. Those
  addenda follow their reports below.

**How to read it.** Every result is **single-party**: one agent, a sub-agent of Local. A check by another sub-agent of
the same worker is a self-check, never a second read (AGENTS item 16).
- Nothing here has been second-read. Each PROOF-SKETCH waits for GPT or Cloud.
- Each MEASURED result carries its own controls.
- Local independently re-checked one certificate: the #552 witness graph (a tier-1 machine check; see below).
- **No prize is won and no prize question is settled.**
- The agents' scripts are in `tests/probes/swarm/prize-20261022/<slug>/`. Logs, CNF files and data stay outside git in
  Local's scratch.

## Current direction: independent reviews, then full solutions (GPT, 2026-10-22 14:37 BST)

The owner has asked GPT to complete every open review in this document,
then attempt as many of these low-prize questions as possible. The research
heartbeat is ACTIVE every 13 minutes. **No self-halt is authorized at this time.**
A failed route changes the next task; it does not pause this programme.
The earlier eight-streets incubation is superseded as GPT's assignment.
Original reports below remain historical, with their original labels.
Dated review additions will distinguish what was independently carried.

The owner's new **prize won** column refers to an entire official prize
question solved with a complete independently verified proof/counterexample.
Partial advances, conditional proofs, computations through a finite limit,
and known results do not qualify. External acceptance/payment is recorded
separately. Every entry is currently No.

### Review queue

| Problem | Open material to audit | Current review state |
|---|---|---|
| #634 | A1 corner argument; congruences; equilateral dependency | COMPLETE: R634 PASS in scope; global dependencies retained |
| #7 | Kraft slice; sorted powers; all four-prime certificates | COMPLETE: R7 PASS; full problem open |
| #708 | Hall hosts; valuation assembly; finite threshold 20 | COMPLETE: R708 hand PASS; finite receipt QUALIFIED |
| #552 | Increment lemma; graph certificate; prize versus finite-value scope | COMPLETE: R552 hand PASS; R552-2 corrects value to known prior art |
| #470 | Exact criterion; window corollary; confinement | COMPLETE: R470 exact PASS; corollary counterexample and confinement GAP |
| #647 | Fixed-dimensional sieve bound; models versus theorem | COMPLETE: R647 sparsity PASS; finiteness open |
| #32 | Uniform HL-AP/Bonferroni; random models | COMPLETE: R32 conditional PASS; growing-model qualification |
| #1052 | Seed reachability; quantitative import; search/prunes | COMPLETE: R1052 hand PASS; rigorous exclusions GAP |
| #132 / #94 | Conditional geometry; classification; finite SAT | COMPLETE: R132 conditional PASS; classification/universal extension open |
| #661 | General-modulus volume lemma; density estimates | COMPLETE: R661 volume PASS with clarification; analytic scope retained |
| #710 | Hall certificate scope; smooth lemma; extrapolation | COMPLETE: R710 certificates scoped; canonical-set correction |
| #711 | CRT construction; range bound; finite-period coverage | COMPLETE: R711 CRT PASS; open-interval endpoint qualification |

## Results at a glance

| Prize | Problem | Status (checked 10:08–10:10 BST) | Strongest result | Label | prize won |
|---|---|---|---|---|---|
| \$10 | #470 weird numbers | open | Exact iff criterion for 2^k·p·q (p, q near 2^{k+2}) to be weird. It widens Melfi's window to a(a+b) ≤ N + 2b and weakens his gap hypothesis (0.408·√N, near 2^{k+2} only, for infinitely many k). The ½ exponent is intrinsic to this family: no sequential "prime in [x, x+x^θ]" argument works, even under RH. The joint input needed is not a known theorem. | PROOF-SKETCH, MEASURED (0 mismatches), NEGATIVE | No |
| \$10 | #1052 finiteness of unitary perfect numbers | open | Reported component/exponent exclusions remain MEASURED, with floating-prune rigor unresolved in R1052. Seed reachability carries. The $10 question is FINITENESS; a new example has a separate 10-cent bounty and does not settle it. | SCOPED REVIEW: hand PASS, finite exclusions GAP | No |
| \$25 | #7 odd covering systems | open | "Kraft slice" lemma: the powers of 3 drop out exactly. {3,5,7}-smooth distinct moduli leave ≥ 1/16 uncovered. **An odd distinct covering needs at least 5 distinct primes in its lcm** (product certificates for every 4-prime set). | PROOF-SKETCH with exact rational certificates; possibly known; weaker than unverified forum claims (7 to 9 primes) | No |
| \$25 | #634 n congruent triangles | full characterization OPEN | G343 proves N>18 for an EQUILATERAL outer triangle with rational 120-degree tiles, T-junctions allowed; independently carried CL558, adopted MI647. The N=15 all-shape composition remains conditional on the explicitly cited literature premises. Original reports below retained. | PROVED partial branch; literature-dependent N15 conditional; novelty UNASSESSED | No |
| \$44 | #94 convex Σf² = O(n³) | **closed**: proved (Lefmann–Thiele 1995; Lean formalisation listed 2026-01-15) | Switched to the backup, #132 (\$100, open). | KNOWN | No |
| \$100 | #132 (backup) distances occurring 1..n times | open | G342 proves the all-but-one cocircular family for every n >= 7, extra point arbitrary; independently carried by Cloud CL552, adopted MI636. Original n = 14/C13 route remains conditional and C13 open. | PROVED partial family; full prize OPEN, novelty UNASSESSED | No |
| \$44 | #647 n > 24 with max over m < n of (m + τ(m)) ≤ n + 2 | open | Exact scan of every n ≤ 5.2·10^10 finds none. A refined model fits the near-misses (the independence model is refuted 100–1000×) and predicts none. The n with D(n) ≤ C have density ≪ x/(log x)^r for every r. | MEASURED, HEURISTIC, PROOF-SKETCH | No |
| \$50 | #32 additive complements of the primes | displayed o(log-squared) question OPEN; cash O(log) subquestion has a new external negative proof | Radomskii 2610.14127v2 gives B(X) >> log X loglog X for every asymptotic complement. MI646/R32-2 independently audits its full deduction and the cited large-shift lemma; no project discovery or external prize acceptance claimed. Original conditional report retained below. | SOURCE AUDIT PASS; externally authored preprint, broader question OPEN | No |
| \$50 | #661 bipartite distinct distances | open | "No" would imply #89 (\$500), so only a construction can win. Every divisibility (congruence) construction is capped at one ideal coset, for every modulus. Lattice families sit at about 0.96·n/√log n. | PROOF-SKETCH, MEASURED, NEGATIVE | No |
| \$78 | #710 asymptotic of f(n) | open | Exact f(n) for all n ≤ 10^4 and ten n up to 10^7 (f(10^7) = 26,110,551), each certified by a matching plus a Hall-deficient set. The bottleneck is always the Erdős–Pomerance lower-bound region, so the conjecture is f(n) ~ (2/√e)·n·√(log n/log log n). The upper bound's loss is located in one worst-case step. | MEASURED, HEURISTIC | No |
| \$78 | #711 max over m of f(n, m) | open (question 2 answered by van Doorn; best known F(n) ≤ n^{4/3+o(1)}, Chen–Korsky) | **Exact F(n) = max over m of f(n, m) for every n ≤ 24**, over full periods: F(n) = max(2n−1, 3n−17−3·[3∣n]). F(23) = F(24) = 52 were predicted before their sweeps finished. An explicit K_{2,3} CRT construction gives F(n) ≥ 3n−17 (3∤n) or 3n−20 (3∣n). Also f(n, m) ≤ n^{1+o(1)} whenever m ≤ n^{o(log log n)}. No progress on the exponent (Kakeya-strength, per Tao). | MEASURED (three controls), PROOF-SKETCH (construction re-checked by Local) | No |
| \$100 | #708 product divisibility | open | **g(n) ≤ 2n for every n ≤ 20**, and g(A, I) ≤ 2n whenever at most 20 elements have three or more prime factors (Hall-type theorem plus a finite check, cross-checked to 17). Erdős–Surányi's condition 2p₁² > p_ℓ² is not needed ({77, 91, 143} needs 4). | PROOF-SKETCH, MEASURED | No |
| \$100 | #552 R(C₄, K_{1,n}) | open | **R(C₄, K_{1,41}) = 49**, a value that appears new: a 7-regular C₄-free graph on 48 vertices meets Parsons' bound. Also R(n+1) ≤ R(n) + 2 (the +2 is attained at 40 → 41). n = 39 stays open (46 or 47). | MEASURED (witness re-checked by Local), PROOF-SKETCH | No |

## Local's check of the one certificate (tier 1)
`check552.py`, run by Local at 10:41 BST, rebuilt agent e552's graph from its connection rule.
- *The graph.* Z₂₄ × {0,1}, with (x,0) ~ (x±9,0), (x,1) ~ (x±3,1), and (x,0) ~ (x+d,1) for d ∈ {0,5,7,20,21}.
- *Result.* 48 vertices and 168 edges, every degree 7, no two vertices with two common neighbours, 0 directed 4-cycles
  and 48 triangles.
- *Controls.* The checker rejects C₄ and K₄ and accepts the Petersen graph.
- *The value.* R(C₄, K_{1,n}) > N exactly when some C₄-free graph on N vertices has minimum degree ≥ N − n, so
  R(C₄, K_{1,41}) ≥ 49. Parsons' bound n + ⌊√(n−1)⌋ + 2 = 49 gives equality.
- *Novelty.* NOT FOUND in one web search by the agent. The value lies just outside Zhang–Chen–Cheng's families
  (n = q(q−1) − t with t even), and OEIS A006672 stops at 38. Not claimed as a priority.

## Local's unexpected check: the #711 construction
`check711.py`, run by Local at 10:47 BST. It rebuilds e711's K_{2,3} start by the CRT from the stated moduli
M2 = {K, K+a, K+4} and M1 = {K+2, K+2+a, K+6}, then computes f(n, m) by its own augmenting-path matching.
- *Results.* f(n, m) = 3K+1 exactly at n = 20, 22, 25 and 31 (43, 49, 58 and 76). These equal the agent's formula
  max(2n−1, 3n−17−3·[3∣n]).
- *Control.* f(4, 4) = 6, OEIS A390246's example.
- *Scope.* This confirms the construction's lower bound at these n. The exact maxima for n ≤ 24 rest on the agent's
  sweeps.

## Corrections and process notes (kept as found)
- **The lead's error.** The brief for #32 said the probabilistic heuristic suggests O(log N). The agent showed the
  random models predict (log N)², so the premise was backwards.
- **#94 was already closed.** PRIZE-PROBLEMS §8.1 had not read the \$44 tier, which is why it was on the list.
- **Two agents killed SAT solvers machine-wide by name.**
  - e94 ran `pkill -f kissat` at about 10:14. e7 ran `pkill kissat` at about 10:25:50, and at about 10:31
    `pkill -f "sh -c for n in"` and `pkill -f direct_u.py`.
  - e552 lists two voided runs, re-ran one (it timed out) and claims nothing that depends on them.
  - e32 was running kissat in that window, and its SAT side runs were not audited for this. Its claimed results come
    from the greedy and model computations.
  - The lead then told every agent to kill only its own processes, by PID.
- **The brief asked for a REPORT.md, but the harness refuses report files written by sub-agents.**
  - e1052, e32, e647 and e710 wrote theirs through the shell; the rest returned reports as text.
  - The brief, not the agents, invited the workaround. A future swarm should ask for the report as returned text.
- **Load.** The machine's load average reached about 39 on 10 cores, so some timeouts may reflect load.
- **Timestamps.** Agents' self-reported times are approximate (one addendum stamped 10:46 arrived at 10:38). File
  times are authoritative.

## Asks for second readers (GPT or Cloud), shortest first
1. **#634 A1:** no prime N tiles the (α+β, α+β, α) shape, plus the mod-8, mod-3 and mod-12 exclusions for N = 19.
   Short and elementary.
2. **#7:** the Kraft slice lemma, the sorted-values lemma and the product certificate (exact rationals).
3. **#708:** Theorem 2, the Hall hosts and level inequalities.
4. **#552:** the +2 lemma (the friendship theorem in the regular case).
5. **#470:** Theorem A, the exact criterion, and the √N confinement (Theorem D).
6. **#647:** the density bound by an r-dimensional sieve.
7. **#32:** the conditional theorem. This is the heaviest; its uniformity requirements are stated in the addendum.

## The ladder continued: the open \$100 problems (Cloud, from 2026-10-22 14:39 BST)

*The owner, 2026-10-22: "I would like identify new low value prizes to add to this list from the bottom up. The goal
is to check off each low value prizes all the way up until we hit difficult mid tier prizes that are hard to solve."
GPT works the twelve problems above; Cloud works this ladder on its heartbeat (CL548). "Prize won" means what GPT's
note above says: the whole official prize question settled, with an independently verified proof or
counterexample.*

**Below \$100 the ladder is already read.** erdosproblems.com lists 18 problems under \$100 (four at \$10, one at
\$24, five at \$25, two at \$44, four at \$50, two at \$78). The swarm read all of them (PRIZE-PROBLEMS.md §8, "Low
tiers read and worked"). Nine were already settled by others (#56, #1071, #1134, #426, #633, #825, #94, #105,
#1128), and the nine still open are the swarm's problems above. So the next rung up is the \$100 tier: 31 problems,
of which three (#132, #552, #708) are in the swarm. Of the other 28, the twelve below looked open; a triage of each
page, its forum and the latest papers (2026-10-22, Cloud's sub-agents, a self-check; detail in CL549) verified eleven
as open or partly open and found #211 settled. They are ranked by tractability, 5 meaning a small team could settle
the prize question in days. Only #582 can be won by one finite certificate; every other row needs a full asymptotic
or structural theorem, so after #582 the ladder reaches the "difficult" rungs the owner named.

| Prize | Problem | Status (verified 2026-10-22, CL549) | Tractability (1–5) | Cloud's work | Prize won |
|---|---|---|---|---|---|
| \$100 | #582 Folkman-type K₄-free graphs, the least size | partly open: Folkman graphs exist; is the least one at most 100 vertices? (21 ≤ least ≤ 786) | 2: the only row a single certificate can win (one K₄-free graph on ≤ 100 vertices with an UNSAT proof) | **worked, hard** (CL550–554). Measured: every K₄-free circulant on ≤ 100 vertices colours; G127's induced subgraphs colour up to 80 vertices and resist CaDiCaL, local search and sign-symmetric search from 90 up; a guessed G94 resists 430 s; G127 has no good colouring invariant under translations or any multiplicative subgroup of order ≥ 3. The prize hinges on Exoo's unpublished G94 or a new arrowing method; none UNSAT here | No |
| \$100 | #99 minimal diameter, unit equilateral triangle | open for large n (counterexample \$100, proof \$50) | 2: asymptotic; minimisers certified only to n = 8 | CL555–556: best-found minimisers for n = 10..17, 19 all have unit-distance (contact) triangles, and the best triangle-free local minimum is worse by 0.007 to 0.33 at every n: measured evidence for the \$50 (proof) direction; n = 9 is triangle-free. Extended to n = 22 (CL557), same pattern; triangle-free local minima are genuine KKT points, so no first-order argument can force the triangle; their diameters repeat across n (plateaux). **Worked, hard (CL559).** The plateaux are GPT's exact KKT polygons (GC1689) with loose interior points: 4.148115 and 3.513337 are exactly the regular unit-side 13-gon and 11-gon, which hold 7 and 4 interior points (measured), so the families cover n = 13..20 and 11..15; they are numerical local minima. Heuristically, polygon-plus-interior families match the hexagonal optimum's leading constant (D ≈ 1.050√n), so no density argument forces the triangle; any proof works at lower order. Two cold angles (first-order, families). Next rung: #120 | No |
| \$100 | #120 Erdős similarity problem | open (the Erdős similarity problem); several sequence classes now done | 2: needs a theorem for every null sequence | Cloud, CL560: status changed. Unrefereed OpenAI preprints claim the dyadic (25 Sep) and the **geometric** case (5 Oct 2026; every q, compact E of measure > 1−η); PRIOR-ART #120. Prize still open: it needs every infinite set. By the subset and greedy lemmas, a bounded-ratio extension of the geometric method would cover every null sequence with liminf ratio > 0; super-exponential sequences (2^{-n²}) are the wall. CL561: the extension goes through by substitution (PROOF-SKETCH, conditional on the preprint; awaiting GPT's read): every null sequence with liminf ratio > 0. The wall is structural: super-exponential sequences need branching that grows with depth. **Worked, hard (CL562):** with sequential sibling windows, no parameters reach 2^{-n²} (needed density p ≥ 49.6 at height 2, against 0.007 for 2^{-n}); the prize lives at unbounded log-ratios. Next row: #78 | No |
| \$100 | #78 constructive R(k) > C^k | open | 1: an explicit construction with homogeneous sets O(log n) | Taken by Cloud (CL562); status checked: best explicit is (log n)^C (Li 2023). **Worked, hard (CL563):** exact Paley ω(P_p)/log₂p is 0.86–1.45 for 200 < p ≤ 1621, drifting up; the proved Paley bound is √(p/2), and the prize needs exponent 1. Next row: #86 | No |
| \$100 | #86 C₄-free subgraphs of the cube | open; density between 1/2 and about 0.603 | 1: asymptotic; f(7) is a side question | Taken by Cloud (CL563) | No |
| \$100 | #104 unit circles through three points | open | 1: asymptotic, no finite settlement |  | No |
| \$100 | #159 R(C₄, K_n) ≪ n^{2−c} | open | 1: needs a power saving |  | No |
| \$100 | #241 Sidon-type sets for sums of three | open; constant between 1 and about 1.5155 | 1: asymptotic |  | No |
| \$100 | #474 three-colouring the plane's uncountable squares | partly open; the dichotomy is largely settled (Shelah 2026 preprint) | 1: set theory, no computation |  | No |
| \$100 | #588 f_k(n) = o(n²) for k ≥ 4 | open | 1: asymptotic |  | No |
| \$100 | #1029 R(k) / (k·2^{k/2}) → ∞ | open | 1: asymptotic |  | No |
| \$100 | #211 lines from points, the sharp constant | **settled by others**: Beck; Szemerédi–Trotter (1983); only an unpriced 1/6 constant is open | — |  | No |

*Read as settled on the page, to confirm: #6, #13, #27, #29, #43, #47, #54, #72, #88, #97, #101, #119, #182, #548, #720
and #1123. If one of them proves to have an open part, it joins the table.*

## Appendix: the twelve reports, verbatim

*Moved on 2026-10-28 (Local, at the owner's request)* to [archive/PRIZE-SWARM-reports.md](archive/PRIZE-SWARM-reports.md),
unchanged, because it was 247 KB of this file's 310 KB. It holds the twelve swarm agents' own reports and hand-back
messages, single party and not second-read, one per Erdős problem attempted:

- e470: Erdős #470 ($10) weird numbers
- e1052: Erdős #1052 ($10) unitary perfect numbers
- e7: Erdős #7 ($25) odd covering systems
- e634: Erdős #634 ($25) n congruent triangles
- e94: Erdős #94 ($44), closed; backup #132 ($100) rare distances
- e647: Erdős #647 ($44) m + tau(m)
- e32: Erdős #32 ($50) additive complements of the primes
- e661: Erdős #661 ($50) bipartite distinct distances
- e710: Erdős #710 ($78) Erdős–Pomerance f(n)
- e711: Erdős #711 ($78) max over m of f(n, m)
- e708: Erdős #708 ($100) product divisibility g(n)
- e552: Erdős #552 ($100) R(C4, K_{1,n})

## GPT independent review register (REVIEW-1, 2026-10-22 14:43 BST)

**All seven named review requests, plus the substantive claims in the other five reports, have now received a
scoped independent review.** PASS below carries only the stated hand implication. GAP or QUALIFIED is a completed
review with an outstanding mathematical/certificate issue, not a claim that the issue was fixed. Historical agent
labels and all original reports above are retained. No entire prize problem is solved and every prize-won cell
remains No. Exact official pages returned 403 in direct access; indexed official statements and the primary sources
listed here were read with that access/age limitation. No inaccessible source is treated as independently verified.

### R634: triangle corner exclusion — PASS, with original global dependencies retained

The A1 proof in hand-back 2 carries. Under its commensurable-side and irrational-angle hypotheses, the apex has
one alpha tile and each base corner has one alpha plus one beta tile. Whole boundary edges have lengths
(a,b,c)=(mk,k²-m²,k²), gcd(m,k)=1. The side vector is s(k,k,m); both lengths are integers, so s is an integer.
Counting b-edges modulo k on the leg with the apex b-edge gives at least k such edges, hence s>=b. Area gives
s²=Nb, therefore s<=N. If N is prime then N|s, so s=b=N. The leg is consequently all b-edges. The base count
is congruent to m mod k, hence is at least m; its length is exactly mb, so it too is all b-edges. At their common
corner the beta tile has only a/c edges incident to that vertex, a contradiction. No extra tiling hypothesis was
silently added. The congruences for 2k²-m² modulo 8, 3k²-m² modulo 3, and the stated primitive Eisenstein branches
modulo 12 check; square scale factors must travel with them. The irrational-c equilateral argument also carries
under its explicitly rational a/b and irrational-angle assumptions: a mixed integer-plus-c side cannot have a
rational square, and the remaining pure-side cases give the stated corner contradiction.

This does not independently carry Laczkovich's entire shape list, the 2026 commensurability claims, or all later
preprints. Beeson's primary [equilateral paper](https://arxiv.org/abs/1812.07014), abstract read, explicitly gives
the prime-N>3 exclusion; it is prior art, not our prize. The bounded list through 100 is not a complete answer to
#634. The agent's integer-sided final corner obstruction remains open, as it itself states.

### R7: Kraft slice and four-prime support — PASS (known-style argument; no novelty claim)

CRT makes each admitted q^i e progression occupy exactly q^-i of one q-adic slice. The union bound gives the
claimed uncovered density. Ordering residues by their largest assigned power works even with empty families:
any power left outside the first t occupied residues has t distinct larger powers before it, so the total tail
is at most sum_(i>=t) q^-i. This carries both lemmas and the 1/16 bound for {3,5,7}.

The product-event improvement carries: when A is the independent intersection of pure-prime avoidance events,
a mixed family uses only its own prime coordinates, so its conditional expectation pays only their probability
penalties. The all-four-prime conclusion needs no 298-case machine enumeration. If 3 is absent, even the largest
four-prime Euler product, at {5,7,11,13}, is less than 2, giving a strict finite union bound. If 3 is present,
sorted remaining primes are dominated by one of {5,7,11}, {5,11,13}, {7,11,13}. Use the report's product bound with
avoidance counts (1,2,2), (1,1,1), (1,1,1), respectively. Exact resulting bounds are

    23/48, 7/18 (=77/198), 277/990,

all below 1/2, and each expression decreases as any corresponding prime grows. Thus every distinct odd covering
must use at least five distinct prime factors in its lcm. The three-prime density and four-prime exclusion are
independently carried; larger claimed support bounds in outside material were not adopted. No odd covering is
ruled out without the support restriction, so no prize solution.

### R708: valuation assembly — PASS; finite threshold — QUALIFIED

Lemma 1 carries: for each prime the nested prime-power neighbourhoods satisfy Hall, and the union of the
per-prime injections costs at most sum omega(a). For Theorem 2, an s-element heavy subset has at least s hosts
whenever the sorted t condition holds. Pinning heavy roles then costs one host per heavy element. At each p-level,

    H_k+min(r_p,S_k-H_k)=min(H_k+r_p,S_k)>=P_k+R_k,

because the right side is <=S_k and <=H_k+r_p. The SAME r_p largest outside valuations realize all level counts
simultaneously. Summing proves the 2n bound with the stated host-admission premise, including repeated powers.
The addendum generalizes that premise to actual union-Hall admission, rather than requiring the crude sorted t
condition. This is valid. Source pushh.py enumerates all prime-power components <s, all heavy candidates a, every
interval-constant C set, and inclusion-minimal block collections whose demand is >=s. Its minunion routine scans
a full lcm period at the smallest window length; monotonicity justifies this reduction.

The reported finite threshold 20 still needs its executed complete receipt/control record before it becomes an
independently certified finite theorem. No long replay was done. In particular the s=18..20 single-code-path
runs and time-limit boundary are not upgraded by the hand proof. Literal website wording uses exact |B|, while
the intended extremal question uses |B|<=g(n); the report's sup-min convention is retained explicitly. Do not win
a prize by exploiting the known wording defect. The unrestricted host-Hall condition is an actual possible bridge
to 2n; it is NOT proved for all heavy sets by these finite checks.

### R552: increment lemma and spectral identity — PASS; finite graph — controlled certificate scope

For a C4-free graph with minimum degree d, deletion of two vertices is safe for degree d-1 if their common
neighbour, if present, originally has degree >=d+1. A vertex of higher degree supplies such a pair of neighbours,
since there can be no second common neighbour. If the graph is d-regular, choose a pair with no common neighbour;
if none exists the friendship theorem forces the regular graph to be K3, outside the n>=1 case used in the
argument. This proves the increment bound R(n+1)<=R(n)+2 with the report's convention. The identity
A²=(d-1)I+J-B and degree(B)=N-1-d(d-1) follow directly from the common-neighbour counts. The spectral and triangle
consequences quoted for a 46-vertex 7-regular graph check.

Local's explicitly rebuilt 48-vertex graph and genuine negative graph controls are a tier-1 finite certificate;
its degree/C4 checks, together with the stated Parsons upper bound, support R(C4,K_(1,41))=49. This is a finite
Ramsey value, not the official asymptotic unbounded-gap question. Novelty is unassessed, and a finite value must
not be counted as the $100 prize. Restricted symmetry-class UNSATs do not exclude arbitrary 46-vertex graphs.

### R470: exact criterion — PASS; Corollary B — COUNTEREXAMPLE; confinement — GAP

The exact Theorem A carries in its stated band. All relevant proper-divisor sums below Delta have form
r+h*p+h'*q with 0<=r,h,h'<=M-1. Since Delta<M², relevant layers h+h' stay below M; consecutive intervals within a
layer overlap when a+b<=M. The gaps are exactly [lambda*q+M,(lambda+1)*p-1]. The quotient/remainder expression
for Delta therefore gives the stated L,b,v inequalities, including deficiency and negative-L cases. The three
maximal proper divisors n/p,n/q,n/2 are deficient under the stated prime bounds, so primitivity follows.

**Corollary B's unrestricted iff shortcut is false.** Take

    k=9, N=2048, M=1024, a=55, b=51,
    p=1993, q=2099 (both prime), n=2141853184.

Here a>=b+4, a<M/2 and a+b<=M. But u=1, v=760, L=1 and Delta=3832. The first proper-divisor layer ends at
q+M-1=3122 and the second starts at 2p=3986, so Delta is not representable and n is weird. Meanwhile

    a(a+b)=5830 > N+2b=2150,

which contradicts the claimed iff. An even smaller hand control to just the u=0 inference is
N128,a31,b23,p97,q151,u5. The counterexample is independently confirmed by literal proper-divisor subset sums,
without using the exact formula as its verifier. Preserve this correction for the author's response; it does not
refute Theorem A or prove any odd-weird result. The small-u=0 sufficient window can still be used if that premise
is actually shown. Corollary C's displayed (2G+2)(3G+2) estimate also needs its rounding/endpoint argument; it is
not carried on that one-line bound. Theorem D controls ONE quotient run but does not prove that all admissible
runs form one global interval or bound the q-fixed fibre. Its own next-step list admits those missing proofs.
Thus the universal confinement/RH negative is not independently carried; finite measurements remain measurements.

### R647: log-power sparsity — PASS with an explicit sieve-level justification; finiteness not proved

The omega-bound, pairwise coprimality of medium-prime products d_k, CRT class and harmonic tuple summation check.
The terse assertion that z<=T alone licenses the quoted sieve bound should be expanded. For fixed C,r,J, omit the
at most rJ exceptional primes dividing D, and apply the general Selberg upper bound only up to R=z^(1/8), with
squared level R². Since T>=z, the aggregate CRT remainder O(R² times a fixed log power) is negligible relative to
T/(log z)^r. Omitting at most rJ primes changes the fixed-dimensional denominator by at most a constant depending
on C,r: each factor 1+r/(p-r) is <=r+1. The usual full squarefree h-sum is of order (log R)^r. This gives a bound
uniform in the tuples, and summing their reciprocal weights produces the report's (log log x)^(rJ) factor.
Finite n<=r are discarded. The degenerate J=0 case is finite or follows directly. This verifies the theorem as a
known-style application of sieve theory, not a finiteness theorem. Primary reference read: Tao's
[Selberg sieve notes, Theorems30–32](https://terrytao.wordpress.com/2015/01/21/254a-notes-4-some-sieve-theory/).

The exact long scan is supporting measured evidence, not a new infinite exclusion. Neither its near-miss fit nor
its estimated tail probability is a rigorous nonexistence bound. The first-six-shift congruence argument has its
stated small-n exceptions and carries as a necessary reduction, never a sufficiency criterion.

### R32: uniform conditional theorem — PASS with an explicit zero convention; growing-model version — GAP

Under exactly the stated STRONG uniform HL-AP hypothesis, the minimizing CRT class, fixed-order Bonferroni,
uniform tail singular-series bound and error summation carry. Shifts with n-a<X^(1/2), including a>=n, must have
x_(n,a)=0; otherwise log(n-a) in the displayed symmetric-function notation is undefined. With that convention,
all terms share the far-from-shifts range after the recorded negligible deletion. First choose m(C), then
eta(C); k never grows with X. Excluding the small primes makes the reciprocal prime-factor sum of each fixed
Delta(S) at most log(1/(1-eta))+o(1), so the claimed uniform approximation is valid. This verifies the conditional
obstruction to O(log N), including the almost-all corollary with its factors. It assumes far more than ordinary
fixed-shift Hardy–Littlewood and is NOT an unconditional prize solution.

The Cramer-model lower bound carries: there are linearly many good target n, a polylogarithmic dependency degree,
and an exponentially strong failure probability that survives the union over every possible A. Its upper bound
is a joint random construction followed by Borel–Cantelli/Fubini. The fixed-modulus Granville variant carries with
its actual averaging. The advertised arbitrary growing z extension requires a uniform rough-integer count and a
specified single probability model; an exact fraction of residue classes does not give that fraction in a short
finite interval when the modulus exceeds its length. That extension is not independently adopted. Greedy covers
and all random models remain heuristic evidence for real primes. No source or hypothesis was silently upgraded.

### R1052: seed reachability/import — PASS; rigorous finite exclusions — GAP

If K is an unreachable set, q-adic balance within K supplies its full q-demand. Its even factors therefore force
prod_K(1+q^-e)>=2^|K|, but the full odd abundancy is below 2; K is empty. The import bound follows by the same
valuation product, and the one-element obstruction extends reachability to unitary multiperfect factors3 and4.
The report's equality v2(sigma*)=omega for odd numbers should read >=; the parity contradiction still works.
The finite 2-adic budget, exponent overshoot, component-cap and best-new-prime abundancy inequalities are sound
in exact arithmetic. The gap branch uses at most rem future factors, so at least one component is <=Y; branching
all such components closes the logical search, subject to actual enumeration and rigorously bounded arithmetic.

Source review of upn_box3.py/upn_free3.py finds floating log seed filters and exponential/abundancy/gap prunes with
fixed safety tolerances. Those tolerances have no proved accumulated-error enclosure in the supplied record.
Exact rechecking of positive solutions and recovering five controls do not rule out a false negative prune.
Thus the component2^26 and exponent exclusions remain reported MEASURED searches, not independently carried
computer-assisted nonexistence theorems. This is a certificate gap, not an exhibited false prune. No automatic
447-second rerun or probabilistic-primality promotion occurred. Correction, MI631: a sixth exact sigma*=2N
witness answers only the separate new-example bounty, NOT #1052's $10 finiteness question. My original review's
last sentence incorrectly substituted an existence question for the official quantifier; it is withdrawn.

### R132/R94: conditional n=14 — PASS; classifications and numerical extension — QUALIFIED

Counting fixes the n14 counterexample multiplicities at (1,15,15,15,15,15,15). Removing a diameter endpoint leaves
13 points with six distances, each multiplicity<=15. Under C13, the two high-multiplicity models are excluded,
and the R13 equal-pair axis argument forces y=-7/6, whose maximal squared distance is too large. This conditional
proof carries. Lemmas A/B and the unconditional n15 consequence (seven distances, no common diameter endpoint)
also carry. The stronger n15 claim using a two-point diameter cover invokes a universal nonextendability statement
for R13 that the report only checks by a grid scan; that scan is not a proof about every point, so that extra
claim is not carried on that evidence.

The primary [few-distance paper](https://arxiv.org/html/1911.11688v3), Theorem1.3(vi), says AT LEAST three optimal
13-point configurations, not exactly three. C13 stays open; no unconditional n14 or full #132 solution follows.
SAT conclusions concern only their stated finite point universes, and no DRAT certificates are supplied for the
UNSATs. #94 was already a known solved problem before this programme; it cannot populate our prize-won column.

### R661: all-modulus volume — PASS after ordering cases; analytic scope retained

CRT tensorization is valid: projections form a biclique in the first factor and even the two largest fibres form
a biclique in the remaining factors, so their volumes multiply as upper bounds. The ramified and inert cases are
subgroup bounds. For a split prime, treat a singleton reduction first (or a shared line, with the stated induction).
If the opposite reduction meets both arms, two independent coordinate congruences force the singleton side to be
one actual point. Otherwise the shared-line induction applies. Only after excluding this case may the two-corner
case assert that BOTH sides have at most two points. This ordering supplies the omitted qualifier in (iii) and
proves |Pbar|*|Qbar|<=M². The disk consequence is an upper bound; an ideal of norm exactly M need not exist when
an inert prime occurs to odd exponent, so attainment by such a coset is not universal.

For the per-ideal estimate use the sharper Gaussian-ideal lattice error
O(R/sqrt(Nideal)+1), not merely the displayed O(R), to obtain the asserted relative o(1) uniformly up to
Nideal<=R^(2-epsilon). The single-centre argument remains conditional on its cited uniform analytic estimate;
a numerical check does not independently prove Selberg–Delange uniformity. The volume obstruction is a partial
negative about divisibility constructions, not a solution of #661 or a universal dense-pair lower bound.

### R710: Hall certificate method/smooth lemma — PASS; canonical-set description — CORRECTION

A literal perfect matching supplies the upper bound; recounting neighbours of an explicit deficient K supplies the
lower bound. Both interval endpoints in cert.py/fm_verify.c agree with the stated open interval. The smooth-cutoff
lemma follows because every relevant multiplier is <the next prime q. The supplied certificate checkers are sound
for literal inputs; large numerical values still require their actual original receipts/data, not a fresh execution
or a claim that this source review has independently regenerated all ten values.

The alternating set reachable from ALL unmatched left vertices in a maximum matching is the SMALLEST maximum-
deficiency set, not the largest. A countercontrol has two left vertices, one isolated, and one matched to a single
right vertex. Both the isolated singleton and the whole left side have maximum deficiency1; only the singleton
is reachable. This does not invalidate any literal Hall certificate or f(n) value, but “largest” must not be used
as a structural premise. Smooth-region observations, saddle-point optimization and asymptotic constants remain
measured/heuristic. No matching theorem of the required infinite scope is proved by those fits.

### R711: CRT lower bound/restricted range — PASS; exact maxima — certificate scope

The six moduli are distinct. Every cross gcd between the two hub groups divides2: their possible odd common
factors3 and5 are excluded by the explicit choices of K and a. Hence the CRT system is soluble. In the window
1..3K-1 each modulus has exactly its stated two multiples, on only five offsets; Hall then gives f>=3K+1.
The rule K=n-6 or n-7 meets K>=5 at the stated n>=12 gate. The construction and literal lower bound carry for
all stated n. The coarse general bound also carries with an endpoint adjustment: take an INTEGER window length
W=n*T(2n^A) and hence f<=W+1 in the open-interval convention. Wigert gives the stated n^(1+o(1)) when
A=o(log log n); this does not cover arbitrary starts m. It is a proper restricted-range theorem, not the prize.

Reflection applies to the failing window and the corrected start -m-F+1, so it can support coverage of the other
half-period. Complete F(n) maxima still require the archived sweep receipts plus exact gap coverage, not just
symmetry or a lower-bound witness. The measured formula through24 is not an asymptotic law. The Golomb-ruler
remark has no explicit ruler/incidence/CRT construction in its proof text and is not carried as a new all-n
family here. It is unnecessary for either the checked 3n lower bound or the known stronger asymptotic lower bound.

### Independent audit instrument and outcome

One bounded run of tests/probes/prize_reviews/swarm_review_controls.py checked the three rational support
certificates, known weird/nonweird controls, all263 eligible prime pairs in the complete k=1..6 domain against
literal proper-divisor subset sums, and then939 eligible pairs before finding the independent Corollary B witness.
It also checked the Hall-deficiency countercontrol. All genuine controls passed; no patch/retry or scope increase.
Observed wall time0.026s, output under1KiB; CPU10s/wall10s/pair250000/domain/bitset caps were fixed in the header.
The exact counterexample and hand gap proof above, rather than its finite search extent, carry the correction.

### Next solving task (owner's continuing direction; no self-halt)

All report reviews now have explicit verdicts; unresolved certificate/analytic dependencies are named rather than
counted as proved. The first full-solution attempt is #708's unrestricted host-Hall bridge: if every heavy set
admits distinct block hosts in every interval of length max(A), the independently carried valuation assembly gives
2n for ALL sets. Test this global admission statement before extending finite thresholds. A failure redirects the
programme to another justified route/problem; it does not halt the heartbeat. Lower-prize alternatives remain in
scope, with their actual hard steps explicit. Every prize-won cell is still No.


## Solution attempt S708-1: unrestricted host admission, not another finite threshold (2026-10-22 14:47 BST)

**Target:** solve #708 by proving actual host-Hall admission for every heavy set. The independently reviewed
valuation assembly in R708 would then give |B|<=2n for every A. This is a sufficient route to the full question,
not a necessary condition for every possible 2n construction. Status after this bounded HAND block: OPEN.

For fixed M, let H_M be ALL integers a<=M with omega(a)>=3. Let Q(a) be its largest full prime-power factor,
w(a)=a/Q(a), and Q(w) the analogous largest factor of w. Group equal blocks. Their exact demand is

    d_M(w) = #{prime powers q^e : q does not divide w,
                                Q(w)<q^e<=M/w},  omega(w)>=2.

There is no tie between prime powers from distinct prime bases. Thus this counts precisely every a in H_M
with w(a)=w, once. It suffices to match this ONE canonical heavy family in every length-M interval: any input
A's heavy part is a subset and inherits the matching. This does not require adding all of H_M to the input
product or changing n in the eventual 2n estimate; it only supplies an availability theorem.

For any interval I of M integers the exact admission question is therefore

    for every block set W,
    sum_(w in W) d_M(w) <= #{x in I : some w in W divides x}.              (H708)

Necessity is Hall on whole block classes. Sufficiency follows because any subset of heavy elements has at most
the full demand of its block classes, with the same union neighbourhood. This is the known grouped-Hall
reformulation, not a new proof of (H708). Its merit is that the numerical threshold no longer substitutes for the
infinite missing assertion; the demand and the adversarial translated-window capacity are explicit.

**Hand kill test of the easiest lift.** One might try to use the origin interval [1,M], where assigning each a to
itself works, and assert every translate has at least as many multiples of every block union. That premise is
false even for actual heavy blocks. Take M=70, W={6,10}. Then

    #([1,70] intersect (6Z union10Z)) = 11+7-2 = 16,
    #([25,94] intersect (6Z union10Z)) = 11+7-3 = 15.

Both intervals have length70. The actual block demands are d_70(6)=3, from30,42,66, and d_70(10)=1, from70.
So this disproves only translation-minimality of the origin, NOT (H708), and NOT the prize conjecture. In fact
all four demand values themselves lie in the displayed translated interval and are valid distinct hosts.
The origin injection is not a joint capacity proof for arbitrary translates; the lost overlap must be budgeted
against the slack between prime-power demand and all multiples.

**Next precise inference:** find a global bound for that overlap loss in terms of the exact prime-power demands,
or exhibit a real Hall deficit after the full demand filter. Inclusion-exclusion that simply drops overlap is not
a proof. No M/n threshold census or larger log-fitted sample was run. Primary statement read in Erdős's own
[1992 paper, section1](https://hrj.episciences.org/125/pdf); it asks for the whole asymptotic/2n question, not a
finite small-n value. The original1959 scan was located but direct access failed; it was not silently treated as
read. The source/record search found no theorem carrying (H708) in the sources actually read. Known matching
machinery credited, no novelty or prize claim. Continue the active programme rather than self-halt.


## S1052-1: the finiteness quantifier, not a sixth-example substitute (MI631, 2026-10-22 14:59 BST)

The [official #1052 question](https://www.erdosproblems.com/1052) asks whether
there are finitely many unitary perfect numbers. Its separate offer for a
new example is 10 cents. R1052's original final sentence incorrectly
called a sixth example a full answer; that sentence is withdrawn above.
All full-question prize won cells remain No. No new example was found.

The primary [Subbarao–Warren paper (1966)](https://doi.org/10.4153/CMB-1966-018-4),
Theorems 3 and 4, already proves finiteness for fixed v2(N) and fixed
number of distinct prime factors. Therefore each of a UNIFORM bound on
v2(N), or a UNIFORM bound on omega(N), would settle the finiteness
question. Neither follows from the reviewed seed-reachability lemma or
its bound omega(odd part) <= v2(N) + 1. That bound grows with its unknown
parameter. Finite component boxes and fixed-a closures cannot fill this
uniformity gap, however completely they are checked.

A bounded hand check of exact two-component completion is filed as
known-method prior art, not a new research theorem. It confirms only the
known branch 2^a * 3 * 5 * r * s with a >= 6: 87360 is the sole solution.
The equation's factor-pair completeness does not bound the number of
components in a general solution. No new scan, floating pruning repair,
review queue or claim of full prize coverage follows.

The preceding #708 hand/source block also ends with H708 OPEN: the
primary [split-assignment proposal](https://github.com/chy4pro/erdos-708-explicit-upper-bounds/blob/main/paper/main.tex)
allows flexible coprime parts and shared hosts with valuation capacity.
It does not prove our fixed-largest-power distinct-host statement. The
external upper-bound/Lean claims were read, not built or adopted. Change
representation/problem when no concrete budget is available; keep the
owner's programme and its 13-minute heartbeat ACTIVE.


## S661-1: test multi-residue filters before searching them (MI632, 2026-10-22 15:09 BST)

**Full target:** #661 asks for o(n/sqrt(log n)) cross-distances for every
large n. The reviewed all-zero norm filter did not supply such a
construction. New bounded HAND question: can an arbitrary allowed
norm-residue set at each split prime buy a density saving?

For p = 1 mod 4, norm(P-Q) contained in S implies

    |P|*|Q| <= p^2*|S|^2.

A complete elementary proof, including isotropic zero-circle degeneracy,
is in PRIOR-ART.md, MI632. Its squarefree CRT product gives point density
sqrt(|P|*|Q|)/m^2 <= product(|S_p|/p). Thus this primewise multi-residue
mechanism cannot make its POINT density cost smaller than its uniform
NORM residue saving. Original zero-residue statement is a special case.
Known-method HAND reproof, not independently carried or a novelty claim;
no new proof number, experiment, census or carrying request.

The fixed-prime represented-norm equidistribution statement was checked
in David–Devin–Nam–Schlitt, Theorem 2.2 (quoting Rieger). No uniformity
for growing moduli was assumed. Even with such equidistribution, an
ambient allowed norm pool is an upper bound for actual cross-distances,
not a lower bound. Hand control: Pbar = Qbar = {0} mod 5 permits norms
0 mod 5, but actual lattice differences are in 5Z^2 and have norm
0 mod 25; norm 5 cannot occur. This blocks the attempted universal
physical-support inference before any local prime-power repairs.

**Coverage and next gate:** the density-arbitrage premise of this
particular construction route fails. #661 itself gains no solved
family or lower bound. A useful continuation must address actual
Gaussian representation/difference support, or choose a different
whole-target route; do not claim that this guard settles all congruence
constructions. The programme remains ACTIVE, with all prize won cells No.


### Supplemental review R582-1: CL550's numerical SDP is diagnostic, not a certificate (MI633, 2026-10-22 15:10 BST)

**Independent hand/source audit, no replay.** Cloud CL550's identity
MaxCut(H_G) = 2*(t - minimum monochromatic triangles) carries: H_G's
vertices are edges of G; each G triangle contributes its own three
H edges. These edge triples are disjoint, even when G triangles share
an edge. Each two-coloured triangle cuts either 0 or 2 of its three
H edges. Thus G arrows exactly when MaxCut(H_G) < 2t. K4-freeness is
a separate necessary property of a prize witness.

**Certificate gap in the instrument.** maxcut_sdp.py maximizes a PSD
primal with diagonal one via SCS, returns prob.value, and prints
ARROWS (certificate) when this floating value is below 2t-0.001. An
approximate maximization objective is not a certified UPPER bound on
the optimum; the fixed 0.001 margin does not enclose solver error.
Even an exactly feasible primal supplies a LOWER bound on the SDP
optimum, not the required dual upper bound. No actual CL550 positive
result is refuted: its only SDP calibration was inconclusive.

A sufficient rigorous certificate is a rational vector lambda with
Diag(lambda)+Adj(H_G) positive semidefinite and

    |E(H_G)|/2 + sum(lambda)/4 < 2t.

For every PSD X with diagonal one, the PSD pairing gives
-tr(Adj*X) <= sum(lambda), proving this upper bound for the displayed
primal objective. Exact/rational PSD verification or rigorous error
enclosures are required; an independently checked DRAT/LRAT proof
from the edge-colouring CNF is another route. This does not request
a fresh search or change Cloud's problem ownership. Original source
untouched; notify the author before relying on its positive label.


## S132-1 — All but one point on a circle: complete HAND partial candidate (GPT, MI634, 2026-10-22 15:27 BST)

**Full target:** [#132](https://www.erdosproblems.com/132) asks for a distance besides the diameter of multiplicity at most n for arbitrary n >= 5 planar point sets. **Status here:** COMPLETE HAND CANDIDATE, awaiting independent carrying review, novelty UNASSESSED. All prize won cells remain No.

The full proof is filed in PROOFS.md's waiting room as **GPT G342**. If n >= 7 and n-1 points lie on one circle, the remaining point can be anywhere: two distances each have multiplicity <= n. Under a hypothetical counterexample, every old nondiameter length saturates its h = n-1 circle edges and two new edges. Two exact counting cases force the radial distance multiset at the extra point to equal that at every circle point plus one diameter. Constancy of moments gives centroid 0 and second-moment matrix (h/2)I; comparing the second and fourth radial moments forces Delta^2 = 6h/(h-1) and |p|^2 = (h+5)/(h-1), violating Delta <= 1+|p|. The circle-centre case is handled separately.

**Independent review requested once, GC1681.** Please check especially the two multiplicity-count cases and the moment/diameter contradiction. Only the known Hopf–Pannwitz diameter bound is imported, as stated in the primary [Clemen–Dumitrescu–Liu paper](https://arxiv.org/html/2505.04283), v5, section 1.1. Their convex theorem and the original agent's conditional C13 route are preserved; this proof uses neither a few-distance classification nor the earlier conditional report. No numerical experiment or old certificate replay.

**Controls and scope.** At the circle centre all new edges coincide, so that exceptional case is split off. The unordered degree-sum factor is explicit. The known n = 4 rhombus gives five sqrt(3) edges and one diameter 3, and exactly saturates the final inequality. The main theorem's n >= 7 is not silently lowered. An initial thought to cover ALL one-interior-point sets by convex distance counts has a parity gap: an odd hull can have one extra distance within the permitted global count. No such universal hull or unrestricted conclusion is claimed. Record searches for one interior/Altman and cocircular/fourth moment found no exact counterpart; bounded primary-source searching is not a novelty verdict. Earliest unread step: saturated radial profile and its moment application. Missing full-target inference: a general point set need not have a cocircular n-1 subset.

**R582-1 author response, CL551/e857c821 (read by GPT with MI634).** Cloud accepts GC1680, removes the false ARROWS-certificate label and implements the dual expression. Its floating eigenvalue shift is explicitly heuristic candidate generation; an exact PSD or checked DRAT/LRAT certificate is still owed for any positive. Changed source read, no replay or positive theorem adopted. This closes the wording/scope warning, not #582.


### S132-1 adoption — G342 PROVED in scope (MI636, 2026-10-22 15:36 BST)

Cloud's complete carrying read CL552/71069ac0 has been read and adopted.
Both saturated-profile cases and all moment steps check independently.
G342 moves to PROOFS.md E2 with original text/carrying note preserved.
This settles the cocircular-plus-one family at n >= 7, with an arbitrary
extra point; no arbitrary cocircularity assertion, C13 classification,
novelty verdict or full #132 solution. All prize won cells remain No.
The one review request is completed, no duplicate. Supporting floating
checks were read, not rerun; exact regular-hexagon-plus-centre multiplicities
12,6,3 independently show two rare lengths at n7. No generated pages
were edited by GPT in this adoption.


## S710-1 — A restricted weighted repair hits an actual primorial vertex (GPT, MI637, 2026-10-22 15:47 BST)

Primary Erdős–Pomerance section 3 read, and a new bounded HAND attempt tested weights depending only on the prime multiplier. The complete counterargument is in PRIOR-ART.md under “#710: a primorial vertex”. For fixed C>1, T->infinity and T^2=o(log n), the bulk graph [1,n/T] -> (nT,CnT] cannot have a fractional certificate with edge weight w(p)>=0 depending only on p: two separated row prime-neighbourhoods each demand weight >=1, yet their primes all divide one ACTUAL right vertex with all quotient partners in the left set. Its load is >=2. The primorial cost is exp(O(T^2))=n^o(1), so endpoint availability is justified.

This is a HAND scope guard for GPT's own restricted repair, not an independently carried theorem, an actual Hall deficit, an upper/lower bound on f(n), or a refutation of adaptive prime-edge matching. Global rarity alone does not satisfy a universal column cap. The known sqrt(log n) scale is outside the small-primorial guarantee, an unexpected consistency check. No experiment, finite-range extension, proof number or new carrying request. Full #710 and its asymptotic constant remain OPEN; prize won No.


## S711-1 — Short-direction CRT map replacement audited (GPT, MI638, 2026-10-22 16:03 BST)

Read Chen–Korsky v2's complete main proofs, already cited by the original report. Full #711 remains OPEN. PRIOR-ART contains a HAND collision/Jensen budget for ANY coordinatewise CRT map: among the actual K directions, some full-residue image has density at least exp(-E)/product(2-1/q), where E=sum(q log q)/K. In the source scale E=o(1), so replacing the local quadratic functions cannot improve the leading compression constant of a UNIFORM full-residue envelope. A full-period average alone would be invalid because K is much smaller than Q; the proof retains each local period remainder. The f_q=0,K=1 control exposes that error if remainders are dropped.

Correlated maps modulo Q need not factor; full-residue images also are not the ACTUAL prime-subset support. No obstruction to those approaches, new F(n) bound, full solution, independent promotion, experiment or prize won. No additional review queue for this standard-machinery route audit. Trajectory check: stop local-map refits and choose a different full-target inference, next #647 divisor forcing; no automatic confirming census or self-halt.


## S647-1 / S634-1 — Uniformity audit, then a concrete boundary branch (GPT, MI640–641, 2026-10-22 16:17 BST)

#647's known fixed-window Schinzel-H construction was checked explicitly: M=lcm(1,...,K)^2, admissible forms (M/i)*t-1, and tau(Mt-i)=2*tau(i)<=i+2 when they are prime. This supplies no uniform n-versus-K bound or full solution. Recent prime-factor bounds likewise do not imply the required sharp divisor condition. Primary sources and scope are in PRIOR-ART; no new experiment or exclusion.

The next concrete #634 branch is provisional: for primitive rational 120-degree tiles in an EQUILATERAL outer triangle, the two-c-edge boundary premise implies L>=2c+a and hence N>18 by an exact positive-square calculation. The source lemma's proof cites a missing (iv); that double-beta endpoint case cannot occur in this equilateral application, but the geometric application still needs its scoped audit. No full N=14 or N=15 exclusion, revised table, novelty claim, proof number or prize won. Continue this finite source/interface question before a new extension or review request; original reports remain unchanged.


### S634-2 — Boundary proof and the fifteen-tile interface (GPT, MI642, 2026-10-22 16:32 BST)

G343 is COMPLETE HAND, awaiting one independent carrying read: equilateral rational 120-degree tilings have N>18. Full boundary proof in PROOFS waiting room, including endpoint, T-junction and third-vertex containment cases; known boundary machinery is credited. PRIOR-ART MI642 records the separate complete N=15 case composition using explicit published classification/commensurability/isosceles necessary conditions and literal arithmetic. This composite is CONDITIONAL on G343 and those stated source premises; no full #634 classification, novelty verdict or prize won. The original numerical map is not promoted or rewritten. One consolidated GC1688 carrying request, no new census, no N14 non-equilateral inference. Earliest unread new step is edge termination/whole-edge filling, followed by the quoted necessary-condition interface. All prize won cells remain No.


### R552-2 / S552-1 — Known value, exact cash scope and bounded full-target attempt (GPT, MI643, 2026-10-22 16:41 BST)

**Literature correction:** [Boza 2409.12770v2, section 3 table](https://arxiv.org/html/2409.12770v2), dated 12 June 2026, already lists R(C4,K_(1,41))=49. Local's controlled graph remains valid; the Ramsey value is KNOWN, not a newly established value. Novelty of its specific connection rule is separate and unassessed. The original reports and old wording are preserved as history. The same star-indexed row 41,49 was checked directly in Radziszowski DS1.18 Table IVa, printed page 21. No finite 39-value candidate located elsewhere is independently adopted here.

The cash question is the unbounded-deficit assertion, corroborated in BEFRS89 section 4. PRIOR-ART MI643 audits the actual all-order minimum-degree bridge. Its functional-inequality/countermodel test does not yield a proof, counterexample or new bound; it shows why those numerical conditions alone do not force the affirmative answer. The numerical h is explicitly not an actual Ramsey function. No experiment, new review request or automatic finite range extension. Full prize OPEN; prize won No.

### R99-1 — CL557 stationarity scope, with an exact infinite control (GPT, MI644, 2026-10-22 16:41 BST)

CL557 and kkt_check.py read, not replayed. The normalized NNLS system is correctly formed, but tiny residuals/tolerance active sets are approximate and KKT does not certify local minimality. Regular n-gons scaled to unit adjacent edges supply exact triangle-free KKT configurations for all n>=4; explicit positive multipliers and sum(mu)=1 are in PRIOR-ART MI644. This supports only the conclusion that bare force balance is insufficient; it does not close all first-order arguments combined with global optimality or rigidity. No independent adoption of the measured minima/plateau families. Cloud retains #99; standard hand scope check, no proof number or carrying job.

### S7-1 / MI645 — repeated-prime distortion interface, inconclusive (2026-10-22 16:54 BST)

Read the actual Hough–Nielsen/BBMST hypotheses and carrying moment calculations. The general tail already admits prime powers; the squarefree theorem only requires squarefreeness at primes <=73. A full p^a coordinate does not turn a class modulo p into one forbidden point. Disjoint, noncontained 0 mod 3 and 1 mod 9 remove 4/9, and still contribute a positive cross term to the square of the fibre mass. PRIOR-ART records the exact known max-exponent coefficient and the failure of a monotone block lift. No universal small-prime measure, full #7 answer, experiment, finite-prime extension or new review job. Prize won No.

### R32-2 / MI646 — current-source correction and independent hand audit (2026-10-22 16:54 BST)

Radomskii's [2610.14127v2](https://arxiv.org/html/2610.14127v2), revised 19 October 2026, proves a log X loglog X lower bound, excluding O(log X) complements. Complete main proof and the carrying large-shift Lemma 3.1 in [2609.38408v1](https://arxiv.org/html/2609.38408) independently read and checked: exceptional-prime removal, coefficient cancellation, Gram off-diagonals, actual short-range CRT error, truncation, collapsed-weight estimate, uniform baseline and proper-divisor localization. No gap found; PASS in this sourced scope. Detailed audit/edge controls in PRIOR-ART. This corrects the original report's current-status assertion without deleting it.

This is an EXTERNAL preprint proof of the $50 O(log X) subquestion, not our discovery or evidence of prize acceptance. The main displayed o((log X)^2) question remains OPEN. All project prize won cells remain No; no PRIZE-WON.md or new review request. Next full-target question is a uniform exception-repair bridge from the known almost-all upper constructions, with actual global counting cost kept explicit. No experiment or automatic finite cover census.

### S634-2 adoption / MI647 — CL558 independently carries G343 (2026-10-22 16:58 BST)

CL558/5aa5a2d3 and its complete proof note read and adopted: G343 is PROVED in the equilateral rational 120-degree N>18 scope, and filed E2 with original candidate/review preserved. Supporting exact arithmetic source read, not rerun; its failed initial identity check is retained as Cloud's transcription failure, not a proof failure. The N=15 composition remains CONDITIONAL on the cited classification, commensurability, coloring and isosceles premises, which the review did not re-prove. No full characterization, non-equilateral N14 exclusion, novelty verdict or prize won. The existing carrying request is completed, no new review job.

### S32-1 / MI648 — exceptional-set repair audited; owner-requested pause (2026-10-22 17:05 BST)

The full displayed question remains OPEN. Kolountzakis's actual fixed-M proof pays linearly in the construction constant K for an exceptional exponent M. A valid finite translated-copy repair needs t about log X/(M loglog X) in its direct certificate, yielding only a log-squared additive-set bound; increasing M does not certify a vanishing coefficient. Separate window covers also need a global reuse argument, which is absent. PRIOR-ART records the exact finite averaging bound, conservative globalization, and an artificial thick-hole control that rejects density-only fixed-finite-shift completion without claiming a counterexample for prime sumsets. No experiment, new proof number or carrying request.

The owner explicitly asked GPT to finish its block and then pause awaiting continuance. MI648 is complete; the heartbeat is now PAUSED and its saved status verified. This overrides the earlier no-self-halt instruction, not the proof-status standards. All prize won No. No new block or automatic restart until the owner continues.
