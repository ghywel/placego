# The record map: what is known, and where it lives

**Read NOW.md first** (the main line and the latest verdict on one page).

*Top-tier index requested by the owner on 2026-10-09; Cloud started it after SL re-derived the existing G205/G208.
Rule: `record-map` in WORKFLOW-SAVED-MEMORY.md.*

**How to use it.**
1. Read in full at session start and after compaction, before work.
2. Before runs or proof attempts, search `python3 tests/probes/record_find.py TERM [TERM ...]`; regex terms must
   match one paragraph. Predictions include `Record searched: <terms> -> <hits or no hit>`.
3. Read each named source before citing: the record overrides this index; correct discrepancies.

**How to keep it.** Index each landed result (reviewed proof, computation, measurement, refutation, closure) under
its object: about 15 words of claim, status, source. Fold dated receipts into their objects at triage. Compress names
and pointers, never a qualifier or a status word. No size cap (the owner, 2026-10-14: "ditch the cap?"; it was 40 KB).

**The tiers below it.**
- PERIOD-TWO.md §6, the status board: every lead and what is left. §4 lists the closed routes.
- proofs/README.md: every proof, one line in plain words, with links to its page.
- The full record, searched with record_find.py: RULE30-PRIZE.md §8 (Cloud and Local's sections), PROOFS.md
  (numbered entries; the master), RULE30-GPT.md (GPT's G and GC sections), COLLATZ-PRIZE.md, PRIOR-ART.md,
  CONSTELLATION.md (side questions), the probes' docstrings in tests/probes/ (predictions and outcomes), and the
  ledgers with their numbered archives (CHAT-LEDGER, CLOUD-LOCAL).
- *Added 2026-10-22 (Cloud, spring clean): the record has grown rooms not listed above: FOUR-BIN-PARTITIONS.md (the
  partition main line), MAHLER.md, GPT-MATH-INSTINCT.md (GPT's instinct notebook), PRIZE-SWARM.md (Local's Erdős
  prize swarm) and CO-DISCOVERED-PROOFS.md. Older notebook entries are in volumes in `archive/gpt/`, rotated ledgers
  in `archive/ledgers/`. record_find.py searches all of them. README.md is the front door.*

**Status words.** PROVED: a proof with a second reader. PROOF-SKETCH: a proof not yet second-read. COMPUTED: an
exact computation or certificate. MEASURED: statistics. REFUTED: a claim shown false. CLOSED: a dead route. OPEN,
PART: as on the board.

## Contents

- [The question and the chain (period 1, period 2, the missing statement Q1)](#the-question-and-the-chain-period-1-period-2-the-missing-statement-q1)
- [The wheel (column 0 clamped to 0101, column 1's 56-step word, the forced block next to it)](#the-wheel-column-0-clamped-to-0101-column-1s-56-step-word-the-forced-block-next-to-it)
- [Kicks (alphabet, classes 12/32/42/52, rates, the kick game)](#kicks-alphabet-classes-12324252-rates-the-kick-game)
- [Records R(d) and R_real(d) (Q6, RR, RR2, RR3)](#records-rd-and-r_reald-q6-rr-rr2-rr3)
- [The regime between, finite left halves, supports (Q7)](#the-regime-between-finite-left-halves-supports-q7)
- [Correlations, entropy and traces](#correlations-entropy-and-traces)
- [The left front, triangles and the right edge](#the-left-front-triangles-and-the-right-edge)
- [Periodic points and travelling waves](#periodic-points-and-travelling-waves)
- [Theorems for every seed (Q5: Theorems A, B, A')](#theorems-for-every-seed-q5-theorems-a-b-a)
- [Other walls, other periods and sibling rules](#other-walls-other-periods-and-sibling-rules)
- [Routes closed (do not reopen without new evidence)](#routes-closed-do-not-reopen-without-new-evidence)
- [Collatz twin (Q9)](#collatz-twin-q9)
- [Mahler's 3/2 problem (MAHLER.md)](#mahlers-32-problem-mahlermd)
- [Prior art anchors](#prior-art-anchors)
- [Side questions (CONSTELLATION.md, by name only)](#side-questions-constellationmd-by-name-only)
- [GPT instinct-led mathematics (owner-authorized, 2026-10-15)](#gpt-instinct-led-mathematics-owner-authorized-2026-10-15)
  - [Frankl's union-closed sets conjecture (MI001 onward)](#frankls-union-closed-sets-conjecture-mi001-onward)
  - [Eight-path burning, L₈ (MI036 onward)](#eight-path-burning-l₈-mi036-onward)
  - [Three- and four-bin partitions (MI295 onward; later eight-path lines, such as G325 and the L8 release, sit among them by date)](#three--and-four-bin-partitions-mi295-onward-later-eight-path-lines-such-as-g325-and-the-l8-release-sit-among-them-by-date)
- [Prize swarm on the smallest open Erdős prizes (2026-10-22, Local; PRIZE-SWARM.md, L750–L751)](#prize-swarm-on-the-smallest-open-erdős-prizes-2026-10-22-local-prize-swarmmd-l750l751)

## The question and the chain (period 1, period 2, the missing statement Q1)
- Period 1: no nonzero finite configuration has an eventually constant column — PROVED — Condrey arXiv:2609.09431;
  proved again by hand, §8.76, filed and second-read as entry 37, machine-checked in Lean (CHAT-LEDGER.8.md)
- Period 2: can a finite configuration's centre column be 0101... from some time on? — OPEN — PERIOD-TWO.md §1
- Chain (PERIOD-TWO.md §2), all OPEN: R(d) <= d + 4 (§8.36) ⇒ R(d) finite for every d ⇔ LR (König; §8.76,
  PRIOR-ART; R(d) defined §8.36) ⇒ LR_m (§8.11) ⇒ B (§8, §8.11) ⇒ period 2. LR, LR_m, B: no column 1, no width-m layer input, no finite right half makes
  the forced left half for 0101 eventually zero.
- Exact forms: forced walk (§8.37), wall form (§8.39), black, white and both (§8.40) — COMPUTED (probe-checked)
- Q1: keeping the wall's conditions costs real information; prove N_{w,j}(T+k) <= 2^(c(w) - αk) N_{w,j}(T) with
  c(w) = O(log w) — OPEN, parked at the fifth triage L638 ("No known method reaches it") — PERIOD-TWO.md §5;
  §8.51 to §8.53, §8.58; board Q1 (M1)
- Delivery side is a theorem (the channel bound); the cost side holds exactly only beside a constant wall, and
  beside 0101 only as a coin model — PART — PERIOD-TWO.md §5; §8.41
- The seed's left part pays exactly: it halves the count (left-permutivity) — PROVED — §8.51 to §8.53 (CJ0, DB0)
- Random words obey the law too; a proof must use periodicity — MEASURED — §8.42
- Primes, Fibonacci, pi, 01: the best start of w <= 18 squares holds them w + 6 steps at most — COMPUTED — CS
- First right-paid ratio rho_j exact to j = 35; its distance from 1/2 does not decay — COMPUTED — L224, L225; ZR3 (L316)
- A uniform linear edge deadline T <= cj + b would give Q1 with alpha = 1/c — PROVED L345/CL161 — GC637/947
- Fair-coin question: pair/price table fills 4 cells (Collatz cheats, entry 43); k-fair periods are multiples
  of 2^k; column families need not merge (GC1165) — §8.92/93
- H(j) - j <= 17 for j <= 22, a plateau broke at w = 27; only §8.69's ceiling certifies — MEASURED — DL, DL2; GC660
- Phase envelopes R_p(d)+d-1=max_(W<d)H_L^p(W) — PROVED GC1166; §8.94.
- P20 repeats fail34 (phase1); low20 excludes real clock through20 — PROVED GC1167/68.
- Real B100101: no real S prepend — PROVED GC1169.

## The wheel (column 0 clamped to 0101, column 1's 56-step word, the forced block next to it)
- Column 1 beside 0101 is the wheel U, an exact coding of the rotation by 17/56, kicked by domain walls in notches
  of 1/28 turn; no other trace tried turns one — MEASURED — §8.4 to §8.11; PERIOD-TWO.md §3, §5
- Even-time word sigma(2s) = floor((17s + 6)/28) - floor(17s/28); 56 steps are 17 turns — COMPUTED — §8.32
- Slips are domain walls moving half a cell a step, arriving at wheel phases 32 and 52 (98.1%; 42 rare) — MEASURED — §8.7, §8.8
- Exact rotation between kicks; not chaotic, its randomness is the interior's — MEASURED — §8.10, §8.11
- Proposition 6: the pure wheel's left half has an exact tail and period in depth — COMPUTED — §8.6
- Column 1 is never eventually periodic, so the wheel slips for ever; an unkicked wheel never works, at any rotation
  number — PROVED — Proposition 7 (Jen), §8.13; Theorem E, §8.57
- Forced block: column 2 at the centre of any 13-observation wheel window, columns 2..4 at the centre of any
  143-observation window; "Fixed-depth forcing, not a locking-speed theorem" — COMPUTED — G205 (GC373/GC374);
  width 15 forces columns 2..6 (LK, L236; G208)
- White-time zero gaps 4, 4, 4, 4, 2, 4; GC502 and GC503 bar the other even classes, given column 2 black at gap
  starts — PROVED (second-read in CL033) — CL033 (RV)
- Even-class departures swap the two gap-start states (post hoc); transients keep gaps 2, 4 — MEASURED — CL033; RV2
- 3-gap beside the wall SAT at T = 352, UNKNOWN 354..1024; window 10000 last possible at T = 52 — COMPUTED — RV3; L289
- A kick's phase and charge readings differ by 14 x (sum of odd gaps) mod 28 — PROVED — G248 with GC582
- The wheel is the edge of a block that turns together: columns 1..4 locked, the lock fading over ~10 columns —
  MEASURED (VW) — rule30_cloud_velocimetry.py, CL095; the forcing itself is G205, G208, LK above
- SL re-derived G205/G208 by SAT (the miss that started this map) — COMPUTED — CL098, CL101, GC855, GC860
- §8.11 N1's "60% against 8%" compared two measures: on N1's own, real halves 69.8%, wide random 70.9%, coins
  60.2%; coins at column 13 sit inside the partial lock — MEASURED — CL098

## Kicks (alphabet, classes 12/32/42/52, rates, the kick game)
- Size set by the interior; timing and alphabet rigid; no memory; about 3.5 bits a kick — MEASURED — §8.43, §8.11
- The alphabet is local: after 133 steps, four classes and at most log2 6 bits a kick; not a classification of
  arbitrary column-1 histories — COMPUTED (second-read, GC359) — entry 26 (Proposition 13, KL)
- After 133 steps: classes 12, 32, 42, 52 only, sizes +4..+8, +2..+6, +1..+5, -6..-1 — COMPUTED — entry 26 (board 6.1)
- Class 12 impossible for every right half after 140 steps; possible at 56, 84, 112; the obstruction needs the rule
  out to column 37 — COMPUTED — KS, KK, DT; CaDiCaL+cake_lpr route 112/112 (comb §8.108)
- Every size of 32, 42, 52 realized at exactly 140 steps (upper bound beyond); class 42 is 67 of 20,282 settled kicks — COMPUTED, MEASURED — KX; KB
- Class 42 dead at N = 560 in all 56 cases (drat-trim) — COMPUTED — KT2C
- Classes 32 and 52 still possible after 448 steps; nothing above 448 decided for 32 — COMPUTED — KT2N (L375), KT2M
- At 56 observations class 19 (kicks -8..-4) is admitted, unused by RB's kicks — COMPUTED (single-party) — OLD1 (GC588)
- A kick lands at the take-off's parity and the opposite colour, just after a white; forward kicks from even white
  take-offs land on the even black arc 44..54, at most six sizes — PROVED — Entry 28 (Proposition 15, GC389)
- Last class-12 front: 11100 at s-14 and 5(s-2) = 0 force 6(s-6) = 0; no preparation bound — PROVED — G209/G210, GC407
- Kick game: runs grow like log2 of its histories; rigidity is a constraint, not a bound — MEASURED — §8.44
- Left: the interior's choice of size; what forbids class 12 at column 37; the cost side (Q1) — OPEN — board 6.1
- The edge ruler's news reaches the wheel but does not measurably change the kick rate or rhythm; which kicks
  happen is unmeasured — MEASURED — CL096, GC856

## Records R(d) and R_real(d) (Q6, RR, RR2, RR3)
- Both cutoff40 lists retain79 recurrent S/L states above the entropy ceiling; missing cuts41..5120 — COMPUTED/hand — GC1007.
- Interior visible gap4422 requires a neighboring gap2, conditional on reported minimal absence — hand inference — GC984; L556/L557.
- Noninitial interior4422 forces preceding5 and following2 — hand inference from reported forbidden words — GC985; RLK K18.
- FullK18 bounds4422 occurrences by1 at every word length — PROVED by finite potential, independent L561 review — GC986.
- Gap4 trains of length>=4 start only near the initial boundary; cannot restart — hand inference — GC987.
- Actual suffix from13 forbids4422/4444; age12 retains4444; relaxation still branches — hand / COMPUTED — GC988/989, L563.
- Phase0 R(d)<=d+4 to89; R89=75 — COMPUTED — §8.36/37 (RK93, R(93), unfinished).
- Black-wall WA3 wrong parity; R°(3)=4 — PROVED CL212 — GC1043.
- Both-phase R_real exact through19, then21..97<=17 — COMPUTED — ZR/ZR2 L236, RR L247, RR2 L399; RRX/RRP replay.
- R_real(97..120) exact, max16 at108; 121..124,140,144..146,148..150<=17 cake_lpr (both phases); 125..131,133..138,141,152>=18 seen; 147=18; 132=139=142=17 (132 cake), 143=17 cake — COMPUTED — RR3, L596..617, §8.96.
- Sampling 2^28..2^30/phase: 97/101 exact; R_real(125)=21 (cake), 133>=23, 194>=26, 200>=20 (L21 UNKNOWN 12 h), 279>=28, 1035>=38; Intel's 16 witnesses (to 1552>=31) replay — COMPUTED — SP, IW, L617..620.
- Both phases versus phase0; plateau R(d+1)>=R(d)-1 — COMPUTED — L286/CL038, RR3 (101/105 solver receipts).
- RR/RR3 cone CNF equals finite query — PROVED GC937/CL154; phase/horizon lift audit GC1201; replay separate.
- VC3 gate/status repairs pass synthetic controls (stale-cache recovery manual; no certificate replay) — GC961/965.
- RR3 decided 97..120 (solver values); deciding UNSATs d3..97 by drat-trim/cake_lpr; VC 200/200; RR3 98..111, 113,
  114 by cake_lpr, 112 and 115..120 kissat only (VC3 halted; comb §8.108) — COMPUTED — RRC L438, L480, VC3.
- Comb B: stored 42 LRAT, 170 DRAT verify; the 34 kept cert CNFs behind record claims match receipts (36 kept; 2 back nothing); regenerations reproduce — COMPUTED — §8.108.
- Comb A,C-E: 17/18 Lean clean (Rule30Period1.lean deferred, environmental); 15 replays reproduce; 52 derived-layer fixes — COMPUTED (single-party) — §8.106.
- Forced-walk counts~2^(0.41d), coin optimum~0.826d+0.8 — MEASURED — §8.38; endpoint words RRX/RRL.
- Relaxed records, exact forbidden words to K=16/18: exceed 17 first at d=65/84; moving frontier — COMPUTED — RLK L555..559.
- K=40 relaxed at L=18: 124 UNSAT both phases (<=17); 140, 144, 152 settled by CUT/SP — COMPUTED (kissat) — RLK L575, L581/582, L589.
- Two-gap train: phase-0 seed1001 eternal (16-tick causal lock at14, tails beyond46) — PROVED CL189/L595 — GC1020/W282; TG. Measured periods 4 to6, 8 to14, chaos pinned15; no invariant window to60.

- R_real climbs ~0.085/depth over 30..116 (no 2,000-shuffle reaches it); L18 at 140/148/156/164 UNKNOWN at 13,321 s, 144..168 at 3,600 s — MEASURED (trend; capped calls undecided) — TR, CL178, CL188.
- Least d>20 with R_real(d)>=18 is 125 (21..124 <=17) — COMPUTED (121..124 cake_lpr, both phases) — L603..605;
  R125=21, R132<=17 cake_lpr: 18s split at 129 and 132, >=3 runs — GC1171; §8.96
- Cut45 needs width24 (23 admits), 18 pins from19; all77 learned cuts verified, widths13..54 — COMPUTED — SWP L605/606.
- Lift: relaxed model plus exact right half, simulation-gated; d=152 L=18 code ABSENT (length-81 cut) — COMPUTED — RLK lift L581/582, L591.
- relax40 first exceeds R_real at d=107 (16 vs 14); blocked by a length-46 minimal forbidden word — COMPUTED (cake_lpr) — RLK L583/584.
- CUT reproduces R_real(107)=14 (phase 0): one cut, L=15 UNSAT (cake_lpr), L=14 witness — COMPUTED — RLK L588, L595.
- GC1007 S/L component: 61 verified cuts (42..97) take entropy 0.1386 to 0.1192 (ceiling 0.1236) — COMPUTED — SLC/SLC2 L588, L591.
- Every list word to 40 (1,603), 41..44 (726, SOFX) and CUT/SLC cut absent by cake_lpr; lists in git (rule30_local_mfw44.txt) — COMPUTED — MFC L590, L640, L641.
  Unary/affine forcing stalls; this gap4 cut leaves GC1007 S/L subsystem unchanged — COMPUTED / hand — GPT L584 follow-up.
- Visible language exact to n=44, both phases: no small lift; follower classes grow — COMPUTED — SOF L564..568, L640.
- Exactness through40 needs strip width35; widths<=34 excluded, all-depth boundedness OPEN — COMPUTED / scope GC996 — SW L569/570.
- No left edge within248, any right half; right-half bounds32/34 — COMPUTED — LL1..LL4 §8.56; §8.21, M3b.
- Best seed wall duration<=width+9 (halves<=32 cells, cuts to depth 126); other traces width+6..10, growing like log depth — COMPUTED / MEASURED — §8.24/42.
- Finite left edge forces frontier events, increasingly old/restarting Fibonacci-parity compensation — PROVED — GC585/586/597..600; local rules CL055/GC595.
- Fixed sources silent, near-silent sources never harden — COMPUTED — SS/GC589, SO/GC591.
- Finite left support excludes all-S and eventually periodic S/L renewal tails — PROVED L372/CL160 — GC686/704/706/707, §8.78.
- Marker-aligned n S gaps need J>=6n-3; rigid all-L needs J>=10n-6 — COMPUTED — GC705/L372, AL/L380.
- Bridges<=24 (tail period<=10) to the155-ring excluded; template K6 passes but rings<=30 fail — COMPUTED — CX, GC828, TC/L452, RD.
- Adjacent-left density>=3/4 and selector/front lemmas — PROVED — G256, G259..268 (PROOFS E2).
- Phase-mask, same-reference-orbit pumping and quotient guards — PROVED — GC846/848/849, G269/270/272; L474/493.
- Last-defect and zero-lag parity shortcuts CLOSED; ParityMask ingredients accepted, assembly unformalized — CLOSED / PART — GC874..876, CL112.
- Remaining Q6: inter-run compatibility with unbounded reach — OPEN (PART) — GC845, PERIOD-TWO §6.
- Two-phase coupling E°(d) = max(d, E(d-1)-1, Q_S-1, P_S-1) exact; R°(1..62); both peaks one black run of 19 — PROVED (coupling,
  Cloud-verified), COMPUTED (R° third-party, lane q2; Cloud to 14, engines to 33) — §8.82, §8.95
- 1,612 minimal absent words to 48 have w_min <= |f|; strip exact to l = 84; S to W = 39 both phases (IN010) —
  COMPUTED, PROVED (2|f|-2) — §8.83
- R(62..72) = 52 51 50 .. 56 59 60 (lane q1, given 1..61; blind match 65, 69, 73); T(u(10)^k) <= |u|+2k+31, |u| <= 16; Jen-type theorem
  beside a periodic wall; barrier lemma — COMPUTED (third-party), PROVED (hand parts) — §8.84
- 1100 wall: R'(1..100) exact, max 18 at 99; lock lemma, structure
  theorem; all-d finiteness OPEN — COMPUTED (lane q4), PROVED (locks) — §8.85
- Right-half language: DFA >= 291 states; h <= 0.2536 certified; death criterion PROVED; deaths at 32, 34, 43 —
  COMPUTED, CONJECTURED (not sofic) — §8.86
- Swarm round: hand proofs held — §8.87
- Check-free: records exact to 122, no survivor; parity bridges PROVED GC1092..94/CL268..270; forced-only periodic
  case OPEN — §8.88, STRATEGY-PLAN.md
- Room switch to cuts; E absent (L630); cuts leave pure M3 (CL303); typed paths <= 466 (CL340); white-A entrances
  certified GC1139..1145; X return admits the core (CL335); a 676-class origin renews black A (CL347); lane CLOSED
  (CL355) — §8.89
- Carry of Rule 30: Gray correction = two-time AND; column carry solved — PROVED — §8.90
- Black-run records Q, P to d=48 (D3 to 60; leaky-max PROVED); 77/78 are black runs — COMPUTED — §8.95, D3

## The regime between, finite left halves, supports (Q7)
- Geometric kick floor, Sturmian/arc/near-square exclusions and TM/paperfolding for left edges <=15,868 cells — PROVED — §8.54/57/59; G131..136.
  A⁗: TheoremA4.lean L535, source GC959; sharp2P-1 L539, source GC960.
- All excluded classes zero-entropy; real column1~0.08bits/bit — MEASURED — §8.20.
- Settling needs uniform O(q) stage budgets and unbounded period growth — OPEN / conditional PROVED — G164/165/184/186/187, Q7.
- Every rooted walk returns; fixed-q excursion bound, return-word bijection and root-tree/nonroot-cycle split — PROVED — entry39/GC867, G273 (GC864..866).
- No return in first11 steps after doubling; return-eight acyclic; automatic baseline — PROVED — G188/192/203.
- Selected-wait identities — PROVED — GC652..702/684; suffix debt29.5 COMPUTED GC949; budget OPEN.
- Source/stratum means, dependent spread, factor-q cap — PROVED — G274..276/W277 (GC869/870/872/890); baseline counting CLOSED GC892.
- Fair-reset leaf weight2^-branch-depth; ambient/uniform-leaf mean transfer CLOSED — PROVED — GC921/CL141, G158.
- Spread<=q-1, split fixture and complete doubled sampling — PROVED / COMPUTED — G6, GC922/925 (CL142/145).
- Two lifts preserve first-reset coalescence iff odd source pulse — PROVED — GC923/CL144.
- Re-coalescence refuted, driver429; stopped — REFUTED — GC926/CL146, G6.3 SF2; clock guard G174.
- Physical q16:15 branches,16 q32 entries at87867..894235; N1..4=3,8,29,400 — COMPUTED — entry21/Proposition8, TM5/TM5b/TM6.
- Whole in-tree sizes4,14,98,3066,34541082 throughq16; RC88 source nonphysical,371 physical — COMPUTED — ZF/CL126..128, GC907..910.
- q8/q16 even-return classifications complete; physical sharp one-parity odd return exists — COMPUTED — RC88/RC16/RC16X/QX/QX2, GC861/862/915, SE/CL134.
- Period64 first depth65821413; q32 stage>2.6e10 — COMPUTED — TM6/Propositions9/10.
- q32 first16 rooted returns, mean1.007x2^32: restricted prefix only — COMPUTED — RWC/RWX L488/522, GC927.
- RW repairs/Lean census match — PART / source PROVED — GC868, L490/491, GC867.
- Driver fibres exact; boundary/nonphysical transfers CLOSED — PROVED — W278..281, GC894..901/903, CL120..126, L510..512.
- Primitive fourth child and sharp/mixed entry constraints — PROVED — GC904/909/911/914/916; mask shortcuts CLOSED GC912/913.
- Sharp profiles/fifth-edge identity; sustained floor refuted; refinement stopped — PROVED / REFUTED — GC917/918/924, CL138/143/151.
- Debt/rotation/pruning — conditional, reviewed — GC310/312/315/323; coalescence identity PROVED CL157/GC943 via GC320.
- Debt60 through2^20, all phases (91 unused); no later bound — COMPUTED L197/199 — RD16/RD32, GC319/325/940, AP/CL156/159; C2P scope GC945.
- Remaining: joint budget (margin reviewed GC946/CL163), gap2, all-left-edge repeats, Rudin-Shapiro, q>=32 odd returns — OPEN (PART) — Q7; G129/140/141, GC155.


## Correlations, entropy and traces
- Rule50 from one black cell has alternating centre and finite support at every time — reviewed GC1267/CL396.
- Full normality does not imply hard indexed computation: binary Champernowne, polylog bit cost — reviewed GC542/CL035.
- Problem3's official no-O(n) display differs from the prose sublinear target — source audit GC548/CL035.
- Problem3 concrete binary-input multitape target fixed; lower bounds OPEN, matching precedent NOT FOUND — specification GC1282; PRIZE-PROBLEMS D4.
- Initial rewrite/merger GC1057/58 PROVED CL225/26; two-tick normalization GC1059 PROVED CL227.
- Two-tick lift guard, packets PROVED CL228/230 — GC1060/61.
- Origin/future lifts PROVED CL231/32/35..37 — GC1062..66; collar/endpoint lifts PROVED CL238/40/41 — GC1067..69.
- Collar release PROOF-SKETCH — GC1070; selector PROVED CL243 — GC1071; three-centre shield REFUTED CL244 — GC1072.
- Plateau/halo PROVED CL210/11 — GC1040/41.
- Cut45 joint origin/past closes at width24; prefix15 fails — COMPUTED CL210 — GC1036..1039.
- Repair: fixed-track binary; joint nonbinary — PROVED CL211/213 — GC1042/44/45.
- S/L collar/gates and fork guards — PROVED CL214/215/217..220 — GC1046..1054.
- GC1114..19 cap672/inverse/excess139/reset PROVED CL294..99; closure REFUTED.
- GC1121..32/1134..42/1144/45/1154..58/1170 PROVED;1146 fails;1148/49/51/1159 SKETCH;badB1150;gap6 REFUTED1153.
- GC1172/74/76/77/79/1181/84/85/87/89/91/93..99/1200/03..08 PROVED;1173/1182 fail;1178/1192 SKETCH; m-3 out L17 (§8.97).
- History records: R_real,p(d)<=2n+R^(n)(d+n), equivalent — PROVED GC1212; K derivation withdrawn (train), game containment unproved; 16 lack real past; n<=8 lowers 11/81 (young peaks 67, 87); §8.98.
- Mixed S/L residences: runs grow to N=150; uniform budget OPEN — MEASURED — §8.99.
- Real147 record and two rejected origins share the whole left row at11; past guards remain — COMPUTED — GC1217.
- Cut45 reset59/NOT8/pair guard, cone d+L — hand/COMPUTED — GC1030..35.
- Cut45 exit/origins: unary/pair stall, joint works — hand/COMPUTED — GC1028/29/39.
- Train exits4/5; entrance3 startup-only — hand/COMPUTED — GC1023/1026/1027/W283.
- Shifted escape to100, hidden update failure, conditioned follower separation — evidence — GC1021/22/24/25.
- Clamped seed1001 eternal two-gap train via fourteen-site causal P8 lock — PROVED CL189/L595 — GC1020/G282.
- Two-gap six-column slab: three failing interface prefixes, failure eight ticks later — SKETCH/COMPUTED — GC1017..19.
- Short-entry plus mature gate loses exact past — REFUTED — GC1015.
- Mature S gate keeps nine prefixes; G239 SL startup example has no two-tick past — COMPUTED/SKETCH — GC1014.
- Marker prehistory branches at any distance; some prefixes forget all tail constraints — COMPUTED/hand — GC1010/12; G236.
- S/L macro past0/1 and age2 cutoff40 shield — PROOF-SKETCH — GC1009/1011, L590.
- Actual nonlinear origin obstruction, depth26 — COMPUTED — GC1008.
- Fixed-m remote tails full; rooted black-image shield and010 forgetting — hand — GC1004..1006.
- Mature black cuts inherited from white cutoff — hand — GC1002/1003.
- NFA/residual mergers fail; phase255 and W9 warmup inconclusive — PART/REFUTED — GC991/994/997..1000.
- Window7/gap multiset fails; gap order first separates at width9 — COMPUTED — GC990/992/993.
- Channel bound: next to 0101 column 1 carries at most 0.1236 bits per visible bit, whatever the right half —
  COMPUTED (certified in integers) — §8.20, §8.33; SQ6, EN6
- Layer times true forbidden words (TC2's F): width 22 certifies 0.130284, below both factors; gain over the layer
  shrinks with width; 0.1236 not beaten — COMPUTED (verified) — rule30_layer_product.py (LP), L505
- Entropy squeeze: every column left of column 0 = 0101 has at most 0.0618 bits a step — PROVED (adversarial
  review, PRIOR-ART.md) — §8.33
- Information reaches column 1 at about 0.2 cells a step; at fixed depth the channel, not the seed, sets the
  longest real run — MEASURED — §8.17
- Counting form N_w(T) ≈ 2^(w - 1.05 T + c), exact to w = 24; the right part pays in lumps, about one bit a
  condition (1.002), debt flat at total widths beyond 100 — MEASURED — §8.51 to §8.53
- Black and white conditions are independent up to a constant factor — MEASURED — §8.51 (Q8, DONE)
- Rule 30's entropy is its width-2 trace's; positively left-expansive at width 2, not 1 — PROVED — §8.77; GC814
- Centre column's linear complexity exactly N/2 at N = 2^22 — COMPUTED — §8.70
- Single seed: centre density 0.49947 over 2^17 steps, block entropy a coin's — MEASURED — §8.34
- Does a structural reason for balance reach the core? G4's identities; a biased ring (13/28) — OPEN (parked) — §8.34
- Neutral blocks 100 and 10000 return; 11 of 128 seven-block words forbidden — COMPUTED — GC605 to GC609; NL (L323)
- Entropy conversion h(-1) = h(visible period vectors)/p; a coarse bound on every periodic wall — PROVED — G53, G54
- Fair-row band theorem: frame-to-frame correlation lies only in d - (m - 1) <= s <= d + (n - 1) (left
  permutivity); alternation law rho_d = -1/2, 1/4, -1/4, 5/32, ... on s = d — PROVED (GC851; second-read CL103) /
  MEASURED — rule30_cloud_velocimetry.py, CL095; the printed errors are in units of the iid scale (GC851)
- Forbidden G-trace words to length 11 certified minimal (cake_lpr); completeness rests on the census — COMPUTED —
  TWC, L467, GC844
- OHC at p = 2 reproduces §8.20's table to 3 decimals, m <= 22 — COMPUTED — XC
- TC/TC2 audits PART (GC871, CL107, GC877, GC879/CL109), F digest and count roots COMPUTED (GC886, GC889); LP audits
  PART (GC883..885, GC887, GC891), witness recipe PROVED (GC888, CL118, L507), positivity guard GC942/944 (CL158)

## The left front, triangles and the right edge
- Left diagonals eventually periodic, power-of-2 periods (Jen 1986, Rowland §5) — PROVED — JenPow2.lean L541: band k<=j+2 period2^j; settled gcd run bound L543; GC962; §8.27/30.
- Lemma B1 (white, then black; LemmaB1.lean L529; GC955), B2 (unbounded periods; LemmaB2.lean L545/550, GC963; infinite white/black JenPow2.lean L548, GC964), B3 (no white run over twice the
  band's period; Lean LemmaB3.lean, L534; source GC958; sharp 2P-1, tight at P=1,2, L539; GC960) — PROVED —
  §8.59; B2 for the single seed is in print (Nersissian Theorem 13)
- Rowland's question answered both ways: >= 4 certified left sides; 60 generic rows share one — COMPUTED — §8.31
- Leftward speed 0.246 = 1 - 0.41 x 1.84, by the identity v = 1 - P(heal) E[jump | heal] — PROVED (identity),
  MEASURED (values) — §8.66
- The order ends at an exact boundary B(t), a walk near x/t = -0.25 — COMPUTED, MEASURED — §8.74
- Chain reading: orderly chain autonomous (lag-2⌊√p⌋ recurrence), random chain driven one way, xz 0.077 vs 1.000;
  triangle identity Σ 3·2^-(L+4) A(L) = 1/2, 2–9% birth deficit near B(t) — PROVED (recurrence, identity),
  MEASURED — §8.80, §8.81
- Left-only horizon next to 0101 ~W+17 for W 11..20 (§8.69), law refuted to 32 (§8.94); no width-16 seed outlives two black stretches of 0^8 1^8, 0^16 1^16 — COMPUTED — §8.69, §8.94
- Every white triangle is exact (shrinks two cells a step); every climb on black reaches the origin in t moves —
  PROVED — §8.18, §8.29; ShortC.lean L533, source GC957
- Backwards: a single 1 has no finite past, and exactly two parents — PROVED — §8.19
- Core triangles follow the uniform measure's 3·2^-(L+4) per cell — MEASURED (law derived) — §8.68
- Right-edge triangles are a ruler sequence, width a function of v2(t) — PROVED — §8.73; entry 36 (Proposition 23)
- Right-prefix periods Q_j <= 2^ceil((2j - 1)/3) for every finite seed — PROVED (second-read by Local) — G249
- Left band staircase P_e <= 32 to about 98,300 diagonals — MEASURED — UB (L383)
- Of 64 rules only 30, 110, 118 have a certified small-period band — COMPUTED — §8.64
- Width-1 rain is the fixed point (01)^inf eaten from the left one cell a row; a stack lasts i - a rows; stack
  births 1/16 per site, lengths 2^-k — PROVED (GC847; K1 by hand L470; second-read CL103) / MEASURED for the single
  seed — rule30_cloud_rain.py, CL094
- Triangles are not carried; their births echo rightwards. Under fair rows, exactly: P(top) = 21/128 and C(d,d) =
  0, 928/441, 16/63, 94/49, 36/49, 17695/14112, ... (d = 1..9), alternating about 1 — COMPUTED (exact) —
  EC, CL108; measured first in VW, CL095
- The centre's wave moves at speed 1 and never reaches the right edge: the gap W + tau is exact; leftward influence
  can reach speed 1 on white — PROVED — GC856 (second-read CL103); rule30_cloud_centre_wave.py, CL097
- Diagonal bias: rho_k's sign alternation fails at k = 17; rho_22 = -8408217689/2^42 — COMPUTED —
  L473

## Periodic points and travelling waves
- Pure2-gap trains, both phases, seven-ring — PROOF-SKETCH / COMPUTED — GC1013; §5.
- Rings to n = 24 complete; transients outlast cycles at n = 21, 22; cycles glide at prime n 13..23 — COMPUTED — §8.67
- A row turning faster than light is spatially periodic — PROVED — §8.71; entry 35 (Proposition 22), GC727
- The 84-cell ring turns 14 cells a step, period 6, one 14 x 6 brick — COMPUTED — §8.71 (CL071, GC686), §8.72
- Rule 30 is eight jigsaw tiles; every periodic tiling is a wall of one brick — PROVED — §8.72
- Epperlein's Table A.1 (the source of Kopra's MathOverflow table) recounted, 42 of 42 — COMPUTED —
  rule30_cloud_periodic_points.py, CL088, §8.77, PRIOR-ART.md "Two survey gaps closed"
- Least temporal period p = 1..10: 3, 0, 12, 28, 45, 84, 105, 88, 180, 550 points, all spatially periodic; none of
  period 2 — COMPUTED — same probe
- The 84 points of least period 6 are one orbit, GC686's 84-cell all-S ring — COMPUTED — same probe, CL088
- Rings with a column reading 0 1^q exist for q = 1, 2, 3, 4, 6; none for 5, 7, 8 to 22 cells (board; L433), nor
  to 30 cells in Cloud's ring search (CL086, rule30_cloud_ring_walls.c) — COMPUTED

## Theorems for every seed (Q5: Theorems A, B, A')
- Theorem A, Jen with a clock: two adjacent columns P-periodic on [a, b] need b <= 2a + L + 2P - 1 — PROVED — §8.54
- Theorem B: paired P-periodic columns, P>=2: zero runs<=2P-2; bounded odd runs<=2P-5 — PROVED — §8.54;
  Lean TheoremB.lean L526/L528; source reviews GC952/953.
- Theorem A′: two-column repeat at a′ has length<=L+a′ — PROVED — Lean TheoremAprime.lean L527; source GC952 —
  §8.58; its Collatz twin is Terras's bijection (COLLATZ-PRIZE.md §5)
- Theorem A‴: a repeat of the trace, a white run in the later row, stays a growing distance below A′ — PROVED (Lean
  TheoremAprime.lean, L530; source GC954) — §8.59
- Jen 1990 for every eventually zero left half: no eventually periodic column 1 — PROVED (Lean JenProp7.lean,
  L531; actual-config source GC956) — Proposition 7, §8.13
- GPT's audit of A, B, A′, E, E″ and §8.59 — PROVED (first pass) — RULE30-GPT.md G2
- Not found in print (limited search): A and A′ "NOT FOUND; NEAR"; E "NOT FOUND" — PRIOR-ART.md
- Theorem A and its no-two-periodic-columns corollary machine-checked in Lean — PROVED — TheoremA.lean, L501, GC882
- TheoremA.lean matches entry 5 (GC882, PROVED, source scope); its hand time re-basing is formal in WhiteEnd.lean

## Other walls, other periods and sibling rules
- Finite-seed and bounded-search qualifiers restored after compression — source audit — CL155/GC941.
- Strip ranks bound phase-forcing onset/bad visits; kernel untested — PROVED — GC919/920, CL139/140, L515.
- Past peeling charges graph-edge ticks; macro forcing needs intermediate phases — PROVED (hand/source) CL152/L523 — GC930/934; frozen-source scope GC948.
- BlackEnd38 q=7,9..13 machine-checked by literal stages (gen_black_end38.py; 456 s, 1.46 GB) — PROVED — L553 (was parked L525); GC951.
- Black-end q7 and q>=9 excluded for finite seeds; q1..6,8 OPEN — PROVED — entry38, SG/L429, GC805/806/L430, WT/L431.
- Small black-end records/LR and white latch — COMPUTED / PROVED — G11..14, Condrey-end board.
- White-end q>=10, black q>=14 and139 extra period10..18 words excluded for finite seeds — PROVED — entries40/41, CL110/111, GC880, L497..499.
- JenRoute/WhiteEnd/BlackLock/P8Lock formal/source audits — PROVED — L508/513, GC873/893/898/906; WC14 certificates GC881.
- One-hole p8,p>=10 closed; nine black steps lock01 — PROVED — G271, OH/TB/OHD, L476/479/480/496.
- Relaxed p8 exact three-word language; physical equality not inferred; dedicated Lean language absent — PROVED CL150 — GC932/933, G271.
- Relaxed p7/p9 characteristic polynomials; true p5 forbids10000 — COMPUTED — GC857, TB/OHD.
- TRUE p5/7/9 finite counts/ceilings improve count roots; zero entropy OPEN — COMPUTED — TC/CL114/116, GC871/877, L504.
- Width22 and layer-times-F ceilings certified; 0101 product still above0.1236 — COMPUTED — LP/ODD..ODD3, L504..506; entropy section.
- TRUE0101 finite-language bound0.1517 also fails to beat0.1236 — COMPUTED — TC2/CL113; product route LP.
- Random-right p5 lock/free alternation, p7/9 positive hole entropy — MEASURED — HE/HE2/HE3, rule30_cloud_hole_entropy.py.
- Candidate p9 free pair fails at30 holes; finite-prefix formula guards repaired — REFUTED / PART / source PROVED — FP/FP2, CL123..125, GC900/902/905.
- Every primitive p3..6 radius9 and open Condrey radius11 strip test fails — COMPUTED — RG/WE/SGC, L488; not counterexamples.
- Every-period theorem extensions p3..6 remain parked — OPEN — Rung3, §8.42/62.
- Slow-wall injection/reset bounds — PROVED — G15/18/19, §8.63.
- Kopra marker K4 centre eventually white; other columns only |j|<=64 — PROVED / COMPUTED — CL088/GC829, rule30_cloud_lone_column.py.
- Linear-CA columns2-automatic; restart statement only sketch — known / PROOF-SKETCH — same probe.
- Rule210 LR false, no finite full0101 clock; transfer to30 invalid — PROVED — §8.65/70, entries29/31/32, GC479.
- Rule90 no finite period2 column; Rule60 control differs — PROVED / COMPUTED — Proposition5, §8.3.
- Rule 30 = Rule 150 jump XOR AND echoes: exact (PROOF-SKETCH identity, COMPUTED to t = 64; PROVED in the kit as CenterFormulas.duhamel, 2026-10-18, L1080) §8.100; not local — MEASURED
  §8.102, 8.103, 8.105; kick cone forced by class — COMPUTED, certified §8.107


## Routes closed (do not reopen without new evidence)
- Static third-image carrier not forward closed — PROVED CL271 — GC1095.
- Uncorrected three-depth zero-prefix drift fails on an actual seven-ring at unbounded depths — REFUTED — GC1016.
- Length-3 factor widening pumps a spurious zero trap; every allowance fails for K10 — PROOF-SKETCH / COMPUTED — GC976.
- Boundary-only temporal widening admits arbitrary white runs — PROOF-SKETCH / COMPUTED controls — GC974; internal-factor widening remains open.
- Bounded runs from a thin layer: runs grow at every width to 16 — CLOSED — §8.14, §8.41
- Periodic column 1: Jen's theorem; the 550,201 words were an instrument check — CLOSED — §8.13; M2
- "Structured families" beating chance: luck — CLOSED — §8.16
- The entropy squeeze as a reduction: it restates the problem — CLOSED — §8.33
- The SAT crib: correct, but slower than enumeration — CLOSED — §8.37
- A merging lemma as the easy half: a merge needs black cells — CLOSED — §8.38
- A Chebyshev-type identity in survivor counts: none visible — CLOSED — §8.41
- "Periodic words hold deep zero runs down" — REFUTED — §8.42
- The wheel's rigidity as a bound: timing cuts runs but does not stop them — CLOSED — §8.44
- Self-similarity between depths d and 2d (renormalisation) — CLOSED — §8.36, RC5
- Q6's methods: shallow fixed-source interception (SO, GC591), one-ray streak census (GC592), persistent and finite-age
  compensation (GC597, GC598), bounded restarts (GC599), age-cutoff and phase-mask (GC601) — CLOSED as methods —
  CL065, GC614.1
- Q7's affine waiting envelopes: slope below 3 only at dyadic periods up to 4 — CLOSED — GC596
- Q3, a machine-found certificate: the only potentials named are Q1's counting ones (the first version's equivalence
  withdrawn, G5); entry 38's strip graphs hold none for 01 to radius 9 — CLOSED until another finite family is named —
  §8.61; board Q3
- Q4, Kari and Kopra's partial result: true and empty for centre columns — CLOSED — §8.55
- Minimal-counterexample descent: 3/4 of normalized words are roots — CLOSED — G121 to G124, G128
- Sideways dynamics as a prize route — CLOSED — G128 (rest in CONSTELLATION.md row 5)
- Repeat-filter and compact-limit shortcuts; gap 1's refinement loop — CLOSED — G142 to G147; CL011
- Summing marginal information of successive observations — CLOSED (no count-loss certificate) — GC412
- Q2, the finite-window move: reopen only on a condition not local in column 1 — OPEN (parked) — CL065, GC614.1

## Collatz twin (Q9)
- Counting form: Terras's coin to 0.5% (w = 30); slope -0.0591 vs the coin's -0.0591 at w = 43, excess <= 7.4 bits,
  not growing — MEASURED — COLLATZ-PRIZE.md §6, collatz_count.py (CZ12 .. CZ16, L509)
- Fewer than 2^(w - αT + c) survivors, the same gap as Q1 — OPEN — COLLATZ-PRIZE.md §1, §6
- Least residue: T^k(2^k m + r) = 3^a m + T^k(r), 0 <= T^k(r) < 3^a — PROVED (known: Terras 1976, Lagarias 1985 Thm B) — COLLATZ-PRIZE.md §4 (proof), §5 and PRIOR-ART (credit)
- Window principle W1 to W3; W2 is Dubickas 2009 Theorem 5 — PROVED (known) — COLLATZ-PRIZE.md §5
- Exponential sums cannot reach a single case — CLOSED — COLLATZ-PRIZE.md §5
- Every actual demand law is unimodal; not always log-concave — PROVED, COMPUTED — entry 30 (Proposition 17); L048
- The universal singleton route — REFUTED — G89 (L046)
- First-deficit survivors n < t^14.3/3; endpoint certificates; offset envelope — PROVED — G69, G68, G67 (L037)
- Conditional bounds (G30, G34, G35, G39-G42, G47, G48) — PART, parked at the fifth triage L638 — board Q9; signed bias O(1/m) at T = 8m is OPEN
- Rule 30 and the 3/2 map share one linear map (the Gray code), corrected locally and by a carry — PROVED (an
  identity) — PRIZE-PROBLEMS.md; COLLATZ-PRIZE.md §8; carry audit CL066, GC616 (L326)
- "XOR plus AND": the linear-shadow claim was wrong; carry-free Collatz keeps the parity AND; the product-free
  shadow has two basins — REFUTED (CL090) — GC832, GC833, CL091
- Carry-limited Collatz: cycles at even k = 2, 4, 6; 0 at odd k >= 3; all reach 1 at k = 0, 1, 8, 10, 12 (n < 2^18) —
  MEASURED — rule30_and_shadow.py, L453
- Mazur natural-density log-time Collatz theorem (CL510-511): ProofAtlas Lean artifact ca3dd0d built here, standard axioms only; set-level, fold-table note added. PRIOR-ART rStation section. (Moved here from the GPT section on 2026-10-22, Cloud's own line.)
- Hercher 2201.00406v3 (CL520-522): Thm 21 proof gap real; rStation repair recovers m<=91 (independent reimplementation), crude bound gives 82; m=92 open at 2^71. PRIOR-ART rStation section. (Moved here from the GPT section on 2026-10-22, Cloud's own line.)

## Mahler's 3/2 problem (MAHLER.md)
- Code/closure/dimensions PROVED G293; MAHLER §1. Pi_2 form (every positive range dies at a finite horizon, forward-shift
  repair) PROVED GC664, second-read L363.
- Positive census: no Z-number below 2^63, counts/horizons (MAHLER §1); dual census: no eta in (0, 2^63 - 1] with every
  part in (1/2, 1) (MAHLER §2, S2) — COMPUTED (source audit; max replayed by rung code); D-M 2009 had 2^57; later
  literature not checked, so no current-record claim (GC1225).
- Stephan2026 window exclusion and finite-hold certificate limit — PRIOR-ART.
- Bounded-gap Fibonacci fails integer realization — PROVED GC929.
- Million-start cutoff COMPUTED GC931; white-orbit forbidden-root exclusion PROVED GC928/CL147; visitation CLOSED.
- Carry dial: H_0 = H_1 = v2(g)+1 for every g >= 1 PROVED G266 (GC836/837, second-read L461); k >= 2 MEASURED L457;
  capped convergence nonuniform near 4/3 PROVED GC935/936.
- Narrower-window rung exclusions to2^100 — COMPUTED MAHLER §2.
- Gap-g ladder PROVED G294; dual ladder PROVED GC1233 (G294 complemented, read L718); upward annulus criterion PROVED
  GC1230 (read L714); distance to K = 2^-(H-1) PROVED GC1236 (read L722); coupling/bowtie CLOSED; swarm main-line null
  — MAHLER §2.
- Every unit interval [k, k+1], k >= 1, holds a xi with every part in [7/57, 50/57]; the 14-state graph is sharp for
  its own graph; universal necessity OPEN — PROVED GC1235/37, L721/23.
- K intersect eK = {0} for nonzero integer e with 3^v2(e)*odd(e) = 3 mod 4 (pair statements, no single integer), PROVED
  8.110/GC1246; 13 PROVED 8.112/GC1253 (its ten further certificates COMPUTED, Cloud only); plateau SKETCH W296. (2/3)K=even part GC1246.
- Ternary01 unit x^e (e!=0 integer): 3-free(e)=2 mod3 excludes x!=1, PROVED Cloud8.110/GC1246; =1 mod3 infinite, PROVED G295/CL384.

## Prior art anchors
- Condrey arXiv:2609.09431: period 1; his Lemma 1 is the forced left half — used, audited (G11; §8.76)
- Jen 1990: adjacent columns never both eventually periodic — used (§8.13; read as the 1990 report LA-UR-90-761, not compared with Physica D 45, GC792); Jen 1986 still owed
  for B2
- Kopra TCS 946 (2023): Rule 30 rapidly left expansive; Corollary 3.7 is Jen's theorem — used (§8.13)
- Kopra 2021 (arXiv:2005.05112): one p/q column never eventually periodic; Theorem 3.5 at width 1; Rule 30 has width
  2, so a transfer needs a new hypothesis — GC807; PERIOD-TWO.md §5
- Kari and Kopra (arXiv:1710.05737): true and empty for centre columns — §8.55; GC670
- Rowland 2006 §5: left-side period doubling; his question answered here — §8.31
- Nersissian arXiv:2609.25077 Theorem 13: B2's method and single-seed statement, earlier — credited (§8.59 note)
- Meier and Staffelbach (1991): left half from two columns, as here — convergent
- Hanson and Crutchfield (1997): domain filter, used for the wheel's walls
- Flatto, Lagarias, Pollington (1995): Mahler's decoupling, same skeleton — calibration, not a route (§8.45)
- Mahler/Erdős (2026-10-14): Mahler 1968; Dubickas-Mossinghoff 2009 (2^57); Akiyama-Frougny-Sakarovitch 2008; Lagarias
  2009 (exceptional-set dimension bounds; log_3 2 only for the truncated real set); Stérin-Woods 2021 — PRIOR-ART
- Dubickas 2009 (W2); Terras, Lagarias, Kontorovich–Sinai (least residue); Bugeaud, Dubickas (2005) — credited
- Guillon (2008): retourné = forced left half; entropy at width 2 — §8.77
- Sablik (2008): no expansive slope (GC813); Coven, Pivato, Yassawi (2007): edge odometers (GC808/810)
- Tahay; Dolce, Tahay: Sturmian columns from finite seeds in other CA; finiteness alone forces nothing
- Milnor, Kurka, Courbage–Kaminski: no lower bound on one column's entropy found — §8.33
- Wolfram (2019): band boundary 0.252/step, an observation; Epperlein (2017): periodic points
- Tan–Teh2207.13855 section4: known adjacent-odd swaps and unbounded-prefix redistribution; finite horizon remains distinct — PRIOR-ART/MI054, no later L8 resolution found in bounded search.
- Cramér's model: the coin's scale plus a structural constant (§8.38); Das not imported; López–Stoll gap noted

## Side questions (CONSTELLATION.md, by name only)
- Part A: families after Condrey; names in CONSTELLATION.md section A.
- Part B:20 object questions; names in CONSTELLATION.md section B.
- Section E: portfolio questions; names in CONSTELLATION.md section E (portfolio).
- Section G, neighbours (10-14): Erdős ternary (fourth figure), Waring, x2x3, normality, Chowla, Langton, BB
- Erdős K2-prime: valuation removal preserves DFA state bound in both directions — PROVED G297, Local L732; GC1258/59.
- Erdős backward Cantor hits: exact 3-adic closure; mixed LSD terminal components necessary — PROVED G298, Local L733; GC1262/63.
- D2 normality: periodic playback/transition budget contract, reflected de Bruijn control — PROVED G299/CL397; no CA implementation.
- D2 playback primitive: eight-state cyclic port; fixed-support obstruction — PROVED G300/L735; controls COMPUTED.
- D1 pooled AP patterns can be maximal in two-state Thue-Morse — known; direct proof PROVED G301/CL398.
- K2-prime joint leading/trailing/length cylinders and mixed MSB components — PROVED G302/L737; controls COMPUTED.
- K2-prime count-only unit-slice invariants cannot avoid ternary01 — PROOF-SKETCH G303/GC1278; unit-preserving carry descent.

## GPT instinct-led mathematics (owner-authorized, 2026-10-15)
*Subheadings added by Cloud on 2026-10-22 (spring clean) to make this section browsable; no line was moved or changed except two of Cloud's own lines, moved to the Collatz twin.*

- Method and first problem: GPT-MATH-INSTINCT.md. Frankl union-closed conjecture OPEN; old prize lanes held.

### Frankl's union-closed sets conjecture (MI001 onward)
- Known27-set smallest-member obstruction audited; fibre-weight sampling trap exact — COMPUTED MI003; no new theorem.
- Known approximate-closure example: one union round fills middle, exponentially expands uniform support — hand PRIOR-ART/MI006; no novelty claim.
- Inverse-multiplicity coupling already in Jiang2609.08291 section10; carrying read/tiny controls MI009; frequency-sensitive gain unresolved.
- Multiplicity log-supermodularity on own lattice REFUTED, five-set pentagon; missing-meet control MI012. No novelty claim.
- Universal fixed meet-map injection REFUTED,12-element uniform-matroid lattice; adaptive/complement controls MI017. No Frankl result.
- Minimum-frequency containment-matching criterion REFUTED,17-set hand fixture and exact controls MI022. Frankl unaffected.

### Eight-path burning, L₈ (MI036 onward)
- Provisional eight-path minimum68: conditional cutoff24..32; naive frontier58.8b tuples COMPUTED MI036; burnability untested.
- Seven-path pilot min46,m18..19: published2/0,5553/178 counts reproduced with witness/oracle controls — COMPUTED MI040; full L7 untested.
- Seven-path m20 stress:82,291/163,662 resolved under2m-state cap, rest UNKNOWN — MI042; routine census parked, no bound.
- Eight-path conditional exceptional reduction audited;64,787,844 targets counted independently — CL414/MI044; no burnability result, extra two-odd shrink unavailable.
- E32 calibration cut off after13 positives; hand exchange certificate plus balanced control give15 distinct positives,171 unresolved — MI046; no L8 bound.
- Even-target exchange band and all-eight-odd E32 construction,27 types — PROVED G304/MI048, Cloud CL417; no novelty claim.
- All186 E32 targets admit odd partitions via parity transfers, chains and a three-swap relay — PROVED G305/MI050, Cloud CL418; earlier levels and L8 open.
- Pair-budget extension and all105 E31 lone-odd93 targets — PROVED G310/MI052/CL424; general E31 open.
- Seven E28 tuples, including (68 twice,108 six times), have receiving-chain certificates — COMPUTED MI057; hand explanation SKETCH, general E28 open.
- Eight designated E28 tuples have signed/coupled-chain certificates after a role repair — COMPUTED MI060; initial blind prediction REFUTED, general E28 open.
- All nine existing E28 fixtures/control admit fixed-small-role cycle certificates; balanced single-cycle class fails — COMPUTED MI062, hand arguments SKETCH; general existence open.
- Six minimum-boundary forced 8-cycles admit a common translation and prefix-avoidance recipe — COMPUTED MI065; uniform explanation SKETCH.
- All 271 sorted even E28 targets with t4>=112 have formula certificates — COMPUTED MI067; uniform construction MI066 PROVED G306/CL421, remaining E28 open.

- Second-negative boundary t4=110,t5>=112: all 320 formula certificates COMPUTED MI071; cycle-surgery proof MI070 PROVED G307/CL422.
- G306 plus one/two matched pairs of magnitudes 1..5: 940/840 derived targets COMPUTED MI074; folded-gap extension SKETCH.
- Full gap-two boundary t4=108,t5>=112: all 421 formula certificates COMPUTED MI076; hand case argument unreviewed.
- Sparse core reorder leaves a runway for unit fans: 56/14 targets COMPUTED MI078; interval argument MI077 SKETCH.
- Two-surplus sparse cores: all 122 fixed-family runways and unit/mixed modules COMPUTED MI080; generic cover prediction REFUTED.
- Mixed (+1,+2,-3) obstruction is unique at five labels, hand SKETCH MI081; actual sparse cores avoid it.
- Fifteen small three-cycle modules: 1,830 instances / 1,801 distinct targets COMPUTED MI082; adaptive hand theorem unproved.
- Zero-surplus E28 corner: all 284 formula certificates COMPUTED MI084; four-move construction MI083 SKETCH.
- One-surplus E28 family: all 1,198 subdivision certificates COMPUTED MI086; combined top-four (112,112,112,112+2a) region has 1,538 checked targets, new hand extensions SKETCH.

- Six-position reflection-free translation guaranteed at span<=20, sharp at21: PROVED G308/MI087/CL422; 9,084 boundary shapes COMPUTED MI088.
- All2,919 two-surplus E28 targets: direct forward/backward subdivision PROVED G309/MI090/CL422; exact formula certificates COMPUTED MI091.
- Combined even E28 region t5=t6=112 has exactly4,523 checked targets, complete-set audit COMPUTED MI092; general E28/L8 OPEN.

- Seven-position span guarantee drops to15, explicit span16 obstruction: hand SKETCH MI094, literal controls COMPUTED MI096.
- Maximal q15 three-surplus slice: fixed parent class fails1/72, explained allocation flip restores all72, COMPUTED MI096/098.
- Three-surplus matching-edge family999: cover-aware roots — PROVED G311/MI099/CL424; certificates COMPUTED MI100.
- Three-surplus unmatched W22 boundary11: explicit seven-cycles — PROVED G312/MI101/CL424; certificates COMPUTED MI102.

- Unmatched three-surplus R>=Z,W<22: all-after REFUTED on2/1,478; endpoint stripe restores all certificates, COMPUTED MI105/107.
- Three-surplus W<=q corner: strict two-edge seven-cycle hand SKETCH MI108; all20 formulas COMPUTED MI109.
- Unmatched W>q,0<R<Z: graph derived MI110;2,648/2,760 parent certificates,112 equal-step traps bypassed by two cycles — COMPUTED MI112/114, classification SKETCH.
- All5,268 even E28 t4<112,t5=112,t6>112 targets have checked partitions; five disjoint domains, two checkers — COMPUTED MI116.
- One forbidden prefix level avoidable for nonconstant positive steps; constant traps identify cancelling cycle split — supporting SKETCH MI117; eight-point packing OPEN.

- Four-surplus constant traps133 and canonical small-subset4,938 have certificates; greedy-anchor shortcut fails56 — COMPUTED/REFUTED MI119/121.
- Four-surplus7,828-target domain:7,223 factorable, all constructed after two explained factor changes — COMPUTED MI125;605 primitive.
- Fixed known nyctalopic order certifies575/605 primitive targets,30 exhaust translations — COMPUTED/REFUTED MI127/129; allowed ordering choices resolve30 in MI131.
- Plagne-Tringali1405.4363v2 Lemmas3/6/7: distinct partial sums, opposite-sign extension and range; reflection not covered — PRIOR-ART/MI126.

- All30 primitive residuals admit reflection-free nyctalopic orders; whole independent feasible maps agree — COMPUTED MI131, no general theorem.
- Entire7,828 even E28 t4<112<t5 four-surplus slice has checked odd partitions, immutable full certificate — COMPUTED MI131; other E28/L8 OPEN.

- E28 uniformity sample:2,000/2,000 even and25/25 even in2,000 unconditional targets certified;1,975 parity-inapplicable — MEASURED/COMPUTED MI135; no full E28 theorem.

- All184 two-valued zero-sum lists with<=8 moves/extrema sum<=28 admit prescribed reflection-free placement — COMPUTED MI138; residue-orbit/path proof SKETCH MI137, unlike pieces open.

- Four cancelling gaps1..14: all2,380 multisets certify; ascending/descending greedy both work, failure forecast REFUTED — COMPUTED MI140; larger mixed pieces open.

- Four cancelling gaps1..14: uniform small/large hand construction PROVED G313/CL425; all2,380 formulas/945 corollaries COMPUTED MI142.

- Every six-point shape span<=20 jointly fits with any gap1..14:217,056 questions/independent complete maps COMPUTED MI144, replicated CL425; wider-core ordering partly G314.

- Six-core2+4 sign type: span<=22, exact three small-step exceptions to20 plus moves21/22 — SKETCH MI145;7,300 independent DP checks/15 bypass partitions COMPUTED MI146.

- Primitive six-core2+4/4+2 plus any gap<=14: computer-assisted PROVED G314/CL426;3409 primitive cores x14 gaps independently checked; other sign types open.

- Even E28 arithmetic collection space:576,515 unordered collections/326,119 parents, max6;36,735 reusable atoms — COMPUTED MI150; no packing result.

- Even-level portability:2000/2000 E26 and2000/2000 E30 sampled targets certify without patches — MEASURED/COMPUTED MI152; universal/mixed-parity cases OPEN.

- Odd-cardinality split-anchor model sufficient only; E28 exact128 parity-pattern counts24,688,633, outside-even24,362,514 — definition/COMPUTED MI153-154; mixed existence OPEN.

- Split-anchor first-policy pilot128/128 E28 (125 odd-containing) certify;20 complete maps/four packings independently agree — MEASURED/COMPUTED MI156; universal existence OPEN.

- First-anchor calibration1996/2000 E28 certify;four restricted failures, three fixed-allocation geometric obstructions — MEASURED/COMPUTED plus hand SKETCH MI158; full model OPEN.

- Four first-anchor failures repaired:one merged nonprimitive8-cycle,three interior-anchor allocations;all2000 original sample partitions checked — COMPUTED MI160; full E28 OPEN.

- Anchor boundary counterexample:long-edge matching exists but every entry/exit blocked;start4 repairs,three full maps agree — COMPUTED/hand SKETCH MI162; general completion OPEN.

- Whole positive-path parity bridge:two odd central jumps/even outer parts;explicit non-greedy E28 application — PROVED MI163/CL426, finite COMPUTED MI164; general allocation OPEN.

- Parity-bridge allocation family b+4c,sum c9,two122: PROVED MI165/CL426;2002 certificates/677 distinct E28 targets independently replicated.

- Balanced-residual parity bridge at any even pool, arbitrary bridge ownership: hand SKETCH MI167;9408 fixtures/2002 grouping checks COMPUTED MI168, target admission OPEN.

- Primitive8 two-odd-positive equal/adjacent-even-negative family: cross-sum gap hand SKETCH MI169;4950 geometries/central E28 partition COMPUTED MI170; general two-run selection OPEN.

- Two positive odd moves total<=26/up to6 arbitrary even negatives: uniform prefix construction SKETCH MI171;24982 geometries/735 distinct E28 targets COMPUTED MI172; high-total selection OPEN.

- Opposite parity shifts yield complete odd-positive imbalance range for B74 negative family: hand SKETCH MI173-174;26 formula checks/4 partitions COMPUTED; arbitrary run selection OPEN.

- Negative-half gcd>=2: folded cycle iff legal odd jumps and two-run load capacity, PROVED MI175/CL427;490 high-total checks/443 E28 partitions COMPUTED MI176; general gcd1 open.

- Two exceptional negative halves summing0 modg>=3: same-run capacity plus order/root choice suffices, SKETCH MI177;216 tight geometries/3 partitions COMPUTED MI178; arbitrary gcd1 OPEN.

- Coloured index chains: full-label N=n-2 exact construction, sparse if two halves>=unused-label-count+2; PROVED MI180/CL428 (adopted MI188),24 full/8 sparse checks/6 E28 partitions COMPUTED MI181; general sparse OPEN.

- Paired negative halves>=2: parallel prefix chains offset1, positive owner mod4 gives iff legal odd bounds; SKETCH MI182,8 formula calls/4 partitions COMPUTED MI183; unpaired/D1 open.

- Sorted negative pairs>=2 differing<=1: unequal prefixes interlace at separation1/2, exact-class SKETCH MI184;9 formula calls/5 partitions COMPUTED MI185; arbitrary pairs/unit halves OPEN.


- Sorted negative pairs>=2 differing<=3: signed crossings preserve disjoint levels and endpoint margin, SKETCH MI186;11 calls/6 E28 partitions COMPUTED MI187; unequal run lengths remain.


- Fixed binary skeleton: interior blank weights forced by gap-overlap tree, SKETCH MI189;6 lifts/6 cut audits/2 partitions COMPUTED MI190; all-interior/one-end universal recipe REFUTED by K budget.


- Minimal contraction r=max(0,ceil((K-2N)/2)) plus outer padding: r0 or two halves>=r+2 suffices, SKETCH MI191;12 calls/6 E28 partitions COMPUTED MI192; one-large-half cases OPEN.


- Shared contraction: largest D>=r+t+1, small-run capacity sum(E-1)>=r+1-(K mod2), SKETCH MI193;12 calls/6 E28 partitions COMPUTED MI194; unit companions still outside admission.


- One D>=N+1 plus N-1 unit halves: legal odd jumps and D<=n-1 exactly suffice, independent SKETCH MI195;12 calls/6 E28 partitions COMPUTED MI196; arbitrary companions OPEN.


- Six selected folded-cycle admissions cover5266/6788 fixed-domain questions, only476 PROVED-tag;1522 residual already includes N3 — COMPUTED MI197-198; dominant-span extension SKETCH, no existence census.


- Three negative halves: five-vertex folded-cycle iff legal odd bounds, no doubled maximum, label count and two-bin capacity — SKETCH MI201;1843 bounded diagnostics/112 independent comparisons COMPUTED MI200.


- Two proper forbidden prefix levels separated by max step: unavoidability requires all-but-one-equal steps — SKETCH MI204;20390 diagnostics/3165 independent comparisons COMPUTED MI203; separation essential.


- Two separated prefixes: exact constant/one-exception congruence obstruction, conditional rich case — SKETCH MI206;20390 frozen-DP comparisons/12 controls COMPUTED MI207; fixed largest-gap split can fail while balanced split works.


- Known Grasshopper distinct-jump theorem applied to M28 two-largest/four-distinct-smaller load split — SKETCH MI208;two residual-profile E28 partitions COMPUTED MI209; repeated gaps open, PRIOR-ART.


- M28 top-two span>=rich four-gap span: conditional completion SKETCH MI210;6 E28 partitions/3 prior residual questions COMPUTED MI211; constant/three-equal companions remain.


- Equal repeated-gap ladders plus arbitrary two terminals: explicit root/reflection SKETCH MI212;10 calls/7 E28 partitions COMPUTED MI213; unequal repeated-gap allocation remains.


- Repeated s>=2 plus two larger exceptions: separate-terminal capacity selector SKETCH MI214;one-larger-exception criterion corollary;9 calls/5 E28 partitions COMPUTED MI215, smaller exception open.


- One smaller exception among repeated s>=2 gaps: explicit parity/corner-rebalance iff SKETCH MI216;11 calls/5 E28 partitions COMPUTED MI217; unit base remains.


- One-exception bags, all bases s>=1 and R>=2: four-condition criterion composed SKETCH MI218 from MI191/195/214/216; no new run; together/apart selection open.


- Repeated s>=2 plus two exceptions a,b>=s: forced-together capacity-carry SKETCH MI220 complements MI214;9+1 calls/one baseline E28 partition COMPUTED MI221; general bags OPEN.


- Frozen low-N residual: N3 all156 provisionally admitted;N4 leaves26/180 on15 nonisolatable profiles; isolated-largest SKETCH MI222,139 geometries/one E28 partition COMPUTED MI223.


- Nonisolatable four gaps: extreme/middle pairing SKETCH MI224;26 residual E28 partitions/4 controls COMPUTED MI225; frozen N4 frontier empty, full E28 OPEN.


- Two unit gaps plus three large gaps: triangle-excess interleaving SKETCH MI226;27 frozen-family E28 partitions/3 controls COMPUTED MI227; general N5/E28 OPEN.


- Arbitrary short-pair canonical capacity/nonisolation: explicit root/order selector SKETCH MI228;11 nonunit E28 partitions/5 controls COMPUTED MI229; alternative allocation remains.


- Canonical capacity failure forces short ownership/interior safety at u>=a+b: SKETCH MI230;6 E28 partitions/4 controls COMPUTED MI231; separated nonisolatable family provisional with MI228.


- N5 canonical capacity does not guarantee completion: (2,2,5,5,7),17/25 exhausts both parity roles;72-case map/3 alternate E28 partitions COMPUTED MI233; general allocation OPEN.

- Paired(s,s,t,t,w),t>=2s: exact resonances/eight allocation switches give sufficiency SKETCH MI234;539 formulas/205 complete maps COMPUTED MI235; full N5 OPEN.

- Two equal short gaps,2s<=u<=v<=w: unequal-middle intersection/three repairs completes selector SKETCH MI236 with MI234/230;1036 geometries/413 maps COMPUTED MI237.

- All unequal-short nonisolatable five-gap bags: six-cycle/forced-partner sufficiency SKETCH MI238 without separation margin;1578 geometries/787 complete maps COMPUTED MI239; independent read requested.

- Thin equal-short s<t<2s: exactly two infinite canonical obstruction families/uniform repairs SKETCH MI240;449 formulas/66 maps,198 candidates zero witnesses COMPUTED MI241.

- Entire nonisolatable N5: composite sufficiency SKETCH MI243 from MI238/234/236/240/242;1221 geometries/489 maps COMPUTED;isolatable side later MI245;full E28 OPEN.

- Full N5 folded-cycle sufficiency: COMPOSITE SKETCH MI245 adds isolated-largest MI244/204/206 plus existing constant-companion MI218;707 geometries/192 maps COMPUTED;independent verification/full E28 OPEN.

- N5 rich four-companion prefix step: shorter direct SKETCH MI246 replaces general MI204 dependency for this row;hand audit only,no independent verification.

- N5 constant four-companion row: specialized SKETCH MI247 plus PROVED MI180 removes smaller-exception/boundary-owner dependencies;hand audit only,full candidate still unverified.

- N5 three-unit exceptions U1-U4: direct root-interval exhaustion/final-coordinate repairs SKETCH MI248;hand audit only,no independent verification or new census.

- Rich-four span-dominant N6 in arbitrary windows: SKETCH MI249 conditional MI246;unique equal-top thin allocation family repaired uniformly;full N6/E28 OPEN,no new run.

- General-window rich-six diagnostics:8 geometries/7 complete offset maps/7746 cases COMPUTED MI251;120 original trap candidates zero canonical witnesses,repairs pass;MI249 remains SKETCH.

- Repeated-gap unequal subdivision:2r>N guarantees free insertion by blocker charging, SKETCH MI252;N5 yields conditional N6 admission,explicit balanced witness;full N6 OPEN.

- Subdivision diagnostic:1008 parents/1112 questions/2606 insertions COMPUTED MI254;24 forced cases pass,merged-parent capacity gap explicit;MI252 remains SKETCH.

- Even repeated s plus unequal a+b=s: exact capacity/odd-bound criterion COMPOSITE SKETCH MI255;forced-small-terminal branch direct,parent branch MI175+MI252;full N6 OPEN.

- Strict Grasshopper count misses M20 six-gap gcd1 case despite4 distinct-chain witnesses, COMPUTED MI259; CP general-N statement/gap MI260, case tree parked after CL430.

- Three old FIRST-anchor failures have same-anchor/h multi-token partitions, COMPUTED MI262; exact-model Euler representation SKETCH MI261, fixed97/99 allocation still blocked by pair competition.

- Anchor-free exact subset catalogue129658 masks; five fixed E28 witnesses,189 oracle controls COMPUTED MI264; one7/seven3 freedom already in MI154 motivates OPEN SB7, no full-domain claim.

- SB7 smallest-buffer54 boundary fixtures pass, COMPUTED MI266; canonical one-hole remainder untested at that block (later MI268); a91 slice follows known verified n7 result, general all-odd E28 OPEN.

- Canonical buffer SAME54 profiles pass, COMPUTED MI268;15 exact one-hole triple domains, one source-supplied. Complete258180 q8 certificate attempt planned, NOT RUN;general statements OPEN.

- ENTIRE258180 all-odd E28 targets have canonical smallest seven-set plus seven triples, literal stream/independent original-target enumeration+DP TWO-PARTY COMPUTED tier1 MI270/CL431(244a56ed); fullE28/L8 OPEN.

- Odd-k equal-sum three-row magic partition plus rank-gap insertion yields balanced triples after ANY single deletion, supporting hand SKETCH MI271;200 audits/15 q8 fixtures COMPUTED MI272. Arbitrary sums outside scope;known base PRIOR-ART.

- Conditional on canonical q8 MI270, all q6 E28 with even minimum and unequal even entries follow by moving token1, hand implication/inverse MI273;>=258180 distinct images, exact count unrun;other q6/fullE28 OPEN.

- Canonical C(s)+ANY disjoint triple sum s+2 equalizes to4/6 retaining1, hand SKETCH MI274;562 full-local audits COMPUTED MI275. Mixed parity corollaries unreviewed;extensions parked for unrestricted certifier route.

- Finite-base reduction re-audited for CL431: exactly64787844 targets E24..E32 suffice, minimum68 preserved/global preceding-level induction handles ceiling overshoots;known mechanism MI276. No all-base certificates yet.

- Unrestricted SAME2000 pilot stops at240:239 literal witnesses,all catalogue/189 oracle controls pass;1B-scan cap on known-positive target,UNKNOWN MI278. No full run;next representation change,not cap increase.

- Reusable weighted-sum SAT SAME2000 pilot:286 literal witnesses/all controls pass,20CPU cap;old target240 solved but69.53ms/attempt,COMPUTED/MEASURED MI280. Simpleadder instrument parked;fullE28/base OPEN.

- Standard DLX SAME2000 pilot:controls/two literal witnesses pass;target3 hits200001-state cap,0.183CPU loop,COMPUTED/MEASURED MI283. Changed pruning confounds comparison;all cap work retained,fullE28/base OPEN.

- Isolated static token budget on SAME first3 DLX inputs:all controls/literal witnesses pass,10/37/64 states;third was capped200001,COMPUTED/MEASURED MI285. Fixture-specific effect,no2000/fullbase result.

- Early budget-check hoist:exact paired222-state traces/six witnesses match,92% fewer updates on SAME first3,COMPUTED/MEASURED MI287. Single timing pair qualified;no larger pilot/fullbase claim.

- Fixed early-DLX ORIGINAL2000 pilot:239 witnesses/control/prefix traces pass,SAME240 caps200001states,COMPUTED/MEASURED MI289. Completed construction82.4%;standalone DLX parked,fullE28/base OPEN.

- Direct Hall rank/matching criteria lack slack;matching-width condition fails known-positive balancedE32,hand source-scope audit MI290;no new burnability claim or review job.

- Chen-Fu binary recombination leaves cardinality uncontrolled;feasible hand countercontrol MI291,source-scope only. GPT research paused for incubation at GC1463;E28/L8 remain OPEN.

- Owner resumes GPT after CL432-433,GC1464-1465. SS3 strict-swap shortcut fails n9;neutral repair and unit-flow/lifting gap hand MI292. Fixed1680-state graph/reflection entirely escapes nonincreasingly,COMPUTED MI294;general SS3 OPEN,level-dependent pair admission explicit.

- *Pointer (Cloud, 2026-10-22): settled since: L₈ = 68, PROVED, G325 (2026-10-19), indexed under the next subheading by
  date; plain words in proofs/G325-the-eight-path-threshold-is-68.md.*

### Three- and four-bin partitions (MI295 onward; later eight-path lines, such as G325 and the L8 release, sit among them by date)

- Three-bin arbitrary-sum SS sufficiency,sizes>=2,via <=4-swap neutral augmentation:PROVED MI295/CL434;82284 formula calls MI297 and1093704 independent start states pass,bound4 sharp. Equal-sum case known;novelty unknown,general SS3 OPEN.

- Four-bin two-triple owner family:SS always,existence iff either middle bin has a spare,five-swap repair/forced negative boundary PROOF-SKETCH MI298;arbitrary overlap placements/SS3 OPEN,no new run.

- Contiguous pattern B C^c D^d C B A,c>=2,d>=3:explicit eight-swap unit-error release PROOF-SKETCH MI299;known rectangle-ideal picture PRIOR-ART;general DCBA placements/SS3 OPEN,no new run.

- Feasible n12 sizes3^4 has exact four-state nonincreasing ALL-single-token-swap trap;minimum L1 barrier4,atomic2-for-2 escapes:COMPUTED MI301. Universal monotone-single-token strategy REFUTED/parked;SS3/three-bin candidate unaffected.

- Opposed-run four-bin family extends the four-state trap/exact barrier4 arbitrarily far;opposite gaps3/2 give uniform2-for-2 repair,PROOF-SKETCH MI302. No universal move-size/SS3 claim,no new run.


- Compound two-edge unit path need not permit any three-bin-local completion,even with all sizes>=3;outside-bin repair and exact seven-token pair-compatibility criterion,hand SKETCH MI303. Full SS3 OPEN,no new run.


- Four bins sizes>=3,single-bin bounds and a two-bin cut slack0/1/2 suffice via explicit complementary one-hole pools;hand SKETCH MI304. Canonical slack3 split REFUTED on a feasible control;general SS3 OPEN,no new run.


- Prefix plus any h-of-2h boundary window has complete r-subset sums for r,m-r>=h+1;four-bin cut slack0..h^2 follows,PROVED MI305/CL434. Repairs slack3/extends minimum3 to4;carrying read completed,general SS3 OPEN.


- Window lemma's216 pools/962 complete spectra pass independent same-worker DP/literal audit;874 partitions cover730 boundary targets,COMPUTED MI307. Negative holes/tight joins retained;general MI305 PROVED by CL434,SS3 OPEN.


- Target-dependent reflected pools plus forced near-extreme residual repair extend four-bin cut slack to h^2+1 for h>=2;hand SKETCH MI308,dependent MI305. Size2 limit reproduces known counterexample;general SS3 OPEN,no run.


- Targeted X/Y pools:54 pools/278 complete spectra have exact predicted holes;225 targets/36 exceptional repairs and independent size2 negative oracle pass,COMPUTED MI310. General MI308 SKETCH;central SS3 OPEN.


- Complete-spectrum complementary pools have necessary pair-slack ceiling min(r,q)min(c,d);central neither-side-good control repaired by neutral parity redistribution,hand analysis MI311. No general augmentation/existence theorem;SS3 OPEN.


- Central-pool dilation needs exactly K local neutral steps,hand guard MI312. Strong-slack arbitrary-target asymptotic rounding adaptation SKETCH MI313;known fractional ingredients PRIOR-ART,novelty/source coverage unresolved,sparse SS3 OPEN.


- Strong-slack rounding self-audit passes by hand;ANY fixed target triple leaves a completable robust three-bin bulk asymptotically,COMPOSITE SKETCH MI314. Known-method adaptation,novelty unresolved;two-small-bin selection/finite SS3 OPEN.


- MI295 three-bin arbitrary sums/<=4 adjacent-swap descent PROVED by Cloud CL434/5ef12b10;1093704 independent start states,bound4 sharp. MI305 pool lemma/quadratic four-bin boundary PROVED same read,216 pools/962 spectra replicated. Novelty unassessed,full SS3 OPEN.
- MI315 two-triple existence is now a corollary of PROVED MI295;MI316 audit CANCELLED BEFORE EXECUTION,no pass. MI317 records adoption and bounded n12,E2 descent-diagnostic design next,not a run.

- Complete n12,3^4,E2 diagnostic:630 SS targets/235054 starts;adjacent/single/plus2for2 trapped4/4/0,max7/6/5,independent coverage/maps/reflection controls COMPUTED MI319. Traps exactly MI301;general SS3 OPEN.

- Reflected n12 five-move extremals:hand supplier/last-touch lower bound,first-two-step exhaustion;later unrestricted energy cannot shorten remaining3,SKETCH explanation MI320. No general SS3 result/new run.

- Signed +/-1 carriers encode E<=2 exactly;known target-domain unit paths reduce fixed-size SS3 to OPEN unit-neighbour realizability,hand MI321. Exact-neutral small moves fail equal-sum triples;no new run/SS3 proof.

- Complete n13,(3,3,3,4),E2:3576 SS targets/2679333 starts all release under1/2 exchanges,max5;all pair redistributions stillmax5/eight extremals,controls COMPUTED MI323. No universal SS3/bound or automatic further run.

- Three-edge unit witnesses:failed disjoint lift has unique CBA/DCB or separated double fork,hand SKETCH reduction MI324. Frozen-endpoint binary two-level connectivity has hand countercontrol;full control one-quad feasible,SS3 OPEN.

- Unit-neighbour work changes to joint realizations:old five-depth sums permit one-swap alternative,another fibre pair needs exactly3 two-bin moves by hand MI325;general coupling/SS3 OPEN.

- Joint-realization n12 diagnostic PARTIAL:counts/four reference maps/literal witnesses pass,whole reflection direction erroneous and later controls unreached;no retry/full-pass claim MI327. Primary7184 lifts only,general coupling/SS3 OPEN.

- Separated CBA/DCB double fork,all sizes>=3:ONE neutral2for2 exchange creates A->D bin path<=2,global two-order hand PROOF-SKETCH MI328. Fibre-minimal realization excludes this obstruction;unique/shared-two-edge cases and SS3 OPEN.

- Three-bin lifted-outlier rank sufficiency at sharp h<=(r-1)^2;four-bin SS within min(selected size,(other minimum-1)^2) of singleton extreme,hand PROOF-SKETCH MI329 from PROVED MI295. Canonical sharpness not SS3 counterexample;central cases OPEN.

- Chosen x-realization isolated under all neutral two-bin moves;one-hole rank-only three-bin completion fails,hand route tests MI330. Refined singleton-spectrum diagnostic registered MI331,NOT RUN;SS3 OPEN.

- One-hole exact-singleton-spectrum criterion:21 domains/8229 eligible vectors ALL partitioned,two independent maps and negative controls COMPUTED MI332. Hand spectrum/tight-face reduction MI333 leaves strict interior OPEN;no larger run.

- Three-bin one-hole rank bounds permit nonincreasing descent to E<=2;direct-gap reverse ordinary path forced by individual feasibility,hand SKETCH MI334. Size2 collision survives;third-token physical release/general criterion OPEN.

- Least-slack singleton choice protects all residual two-bin rank bounds;alternate old MI295 existence proof PRIOR-ART. One-hole pivot repair reduces to structured subset spectra,hand/unreviewed MI335;completion OPEN,no new run.

- Two-hole subset spectra have only edge-distance1/2 gaps at minsize3;least-slack legal-pivot/two-internal-hole branch repaired uniformly,hand SKETCH MI336. Missing-pivot three-hole branch/one-hole criterion/SS3 OPEN,no run.

- Three-bin one-hole interval,all sizes>=3:individual subset feasibility plus total conservation sufficient,COMPLETE hand PROOF-SKETCH MI337 via MI333/335/336. Independent carrying review pending;novelty/four-bin SS3/E28/L8 unresolved.

- CONDITIONAL on MI337:four-bin closest singleton/triple facet suffices at arbitrary slack;strict closest pair becomes joint central-spectrum boundary selector,hand MI338. Arbitrary boundary shortcut refuted;full SS3/stronger uniform selector OPEN,no run.

- Four-bin SS3,all sizes>=3,arbitrary prescribed sums:COMPLETE hand candidate MI339 via staircase/conjugate central spectra plus MI338 and pending MI337. PROOF-SKETCH,independent review pending,novelty unassessed;no new run/E28/L8 result.

- Staircase candidate audit:363 boundaries/726 pools/4853 COMPLETE spectra and109052 central values pass independent maps,literal complements/negative controls,COMPUTED MI341. Full MI337/339 proof/novelty still unverified,no repeat/larger run.

- Exact equal-sum k4 predecessor normalized t_i=s_i+c_i;arbitrary-target novelty UNASSESSED,dependency map acyclic by hand scope audit MI342. MI337/339 remain SKETCH,no new run.

- Staircase complementary boundary set identity at unequal totals,h0/empty segments;target recovery/ties integrated,hand audit MI343. Same MI337/339 candidate SKETCH,pending review,no run.

- One-hole missing-pivot repair:four original-rank margins and unavailable endpoints self-audited,hand controls MI344. Same candidate SKETCH,pending independent review,no run.

- One-hole legal-pivot endpoint/trimmed-hole coverage self-audited by actual rank formulas and original spectra,MI345. Same MI337/339 SKETCH,independent read pending,no run.

- Cloud CL436/55448489:partial independent hand read plus reported90069 four-bin construction checks;remaining carrying re-derivations explicit. Source scopes acknowledged GC1511,candidate still SKETCH.

- Central-slice algebra self-audit MI346:explicit P/Q endpoints,distinct valid join bounds and single-slice q2 containment. Original candidate unchanged,CL436 checklist qualified;SKETCH,no run.

- G315 one-hole3 individual-spectrum criterion and G316 full-interval4 SS cut criterion,minimum sizes3:PROVED in scope,Cloud CL437/7bfdfe34,adopted MI347/GC1513. Q review machine-support qualification retained;novelty UNASSESSED,E28/L8 OPEN.

- FOUR-BIN-PARTITIONS.md consolidates G315/G316 proofs,including scalar lemmas and review scope,MI348. Subsequent one-hole4 all-union extension tested in MI349/350;no new run.

- One-hole4 ALL-union spectrum hypothesis:tight rank cuts/pair lower slack1 have hand boundary completion MI349. Full criterion subsequently REFUTED MI350;singleton slack1 led to special-two-hole3 compatibility,no run/review job.

- One-hole4 ALL-union criterion REFUTED by hand:4,18,18,32 on0..12 minus6;infinite(a,3,3,3) family MI350. Two forced near-extreme bins expose parity gap;special-two-hole3 also false,no run.

- Special pool[0,V] minus{1,v},three sizes>=4:individual feasibility suffices via zero-owner budgets and G315,PROVED G317/MI351,Cloud CL438/f8a264d2. Min3 counterexample confirmed;10835 independent instances support hand read.

- Zero-owner budgets extend to initial gap L2..5,minsize4;explicit spectrum inheritance gives one-hole4 singleton slack1 all q/slacks1..4 q>a,hand SKETCH MI352. Interior minimum4 criterion OPEN,no run/new review job.

- Known pair-completeness plus sliding/fixed-prefix windows certify all scalar sums12 from extremes for three-hole pools,min(r,t)>=4,hand application MI353/PRIOR-ART. Legal-pivot positive-suffix two-hole3 branch closes at residual sizes>=12;general compatibility OPEN,no run.

- COMPLETE three-hole scalar finite basis48896 cases/586752 independent offsets COMPUTED MI355. Hand reduction supports distance3 localization;conditional legal-pivot two-hole3 branch completes at min4,h>=4. Near-minimum/missing pivot OPEN,no rerun.

- Near-face rank catalogue/four explicit repairs close ALL legal-pivot two-hole3 cases,minsize4,conditional on unreviewed localization,hand MI357. Absent formal pivots/generic theorem OPEN,no run/new review job.

- Far missing-pivot repair preserves adjacent holes/no-four-run;known pairing gives buffer14 and explicit rank-margin completion region,hand UNREVIEWED MI359. Small margins/short one-sided cases OPEN,no run.

- Actual five-bin least-singleton residual forces every group u_J>=L(r)+r;exact lift gate excludes entire MI350 family,hand MI362. Generic hole tree PARKED;protected one-hole4/singleton-facet target OPEN,diagnostic offered to Cloud.

- Actual N17 least-slack residual refutes canonical rooted-G316 adaptation for all4 expanded owners;positive alternate boundary explicit,hand MI366. Protected theorem OPEN;GPT heartbeat PAUSED for perspective/incubation,GC1526.

- Least adjusted-slack deletion preserves margin for ANY realization;one-hole to two-hole step refuted by actual five-bin residual,hand MI368. Sharp three-hole geometry bound retained;owner resumes,13min ACTIVE.

- Coarsening reduction (CL508, PROOFS waiting room, hand, single-party): least-slack group of <=k-2 bins -> coarsened instance in H(mu) + child in H(mu') (MI368 for groups, any realization); H(0)/SS3 reduces fully by reflection. Irreducible = least slack only at co-singletons (top-tight lemma, OPEN; CL443's wall). CORRECTION CL515: for pair/triple-least G the coarsened instance is itself top-tight (big bin B), so the top-tight lemma must include big-bin cases. UPDATE (Cloud, 2026-10-22): PROVED, with CL515's correction and CL517, by GPT's carrying reads in MI619; filed PROOFS.md C9 and C10.
- Top-tight four-bin census (CL509): one deletion (lower/upper, any single/pair) settles 98.0% (h1) / 97.5% (h2) of irreducible 3333 instances; residual is H-family coarseness. Hole-aware families HM/HS FALSE (CL506).
- Equal-sum core distance (CL512-513): size-3 bins first fail H(h) at h = 3, 3, 7, 9, 10, 12, 13, 15 for k = 3..10 (clump family; s=2 window h >= 1.5k-1+1/(k-1), hand). Two-bin base H2(h) (CL514): gaps only n=6 (equal split) and h >= 2n-7 (witness {0} u [h+1,M]); conjecture iff h <= 2n-8, n >= 7.
- SS3 census (CL507/511/513): k=5 n=17..20 all 23 multisets 89.8M ordered vectors, k=6 n=18 83.9M, 0 failures (kholek.c, tier1 measured).
- Big-bin top-tight (3,3,X>=6) case (CL524-529): local (u_A,u_B <= 11+3h); exhaustive check proves it for h<=6, all M, X (PROOFS waiting room, computer-assisted, single-party). Four-rule blind selector 100% on 137,539 instances; minmax misses only at |u1-u2|<=1. Small bins (3,4),(4,4): minmax alone 100% (88,524). Four-bin co-singleton: blind rules leave a feasible child except (19,19,19,21) (CL527). UPDATE (Cloud, 2026-10-22): the committed checker, cloud_reads/toptight_local.py, had lost its docstring's closing quotes; repaired and re-run, same counts (h<=6). Still single-party.
- Small-bin top-tight (CL535-539): common (30-55%); lexmin (top value + smallest completing pair) leaves a feasible child on all 677,808 big-bin instances, but the child is outside H(h') 20-40% (CL537) and at or below even a pool-relative, spectrum-admitted failure line ~93% (CL539, cold): no margin family is the closure.
- Small-bin top-tight blind chain (CL540): A lexmin, middle small bin by any of CL524's four rules (both orders), last bin any triple: 100% on 965,990 instances X>=6 (h<=3), X=4 misses only with equal targets (44). Generic (3,3,X) chain misses only at pool-relative key 0 or equal targets; conjecture C540.
- CL541: C540 FALSE (unequal misses at relative key 1 with 5 holes, key 2 with 6). Generic chain miss line in the record's H-key: unequal nh-2, equal nh-1 (nh=4,5,6): chain solves H(nh) on (3,3,X>=6) (C541, measured). Lexmin children sit at H-key nh-1..nh-3 (~10% covered) yet are 100%: the peel carries non-margin structure.
- CL542: with A top-tight (X>=6), EVERY triple R of sum u_A leaves a child solved by the blind chain: 3,283,146 (instance,R) pairs at (6,1),(6,2),(8,1), 0 misses; lexmin without top-tightness 90.4%. Small-bin top-tight lemma becomes universal in R (measured, single-party). SCOPE (2026-10-22): measured at h <= 2 only; the arbitrary-h form is FALSE, GPT's MI626 hand counterexample at h = 12 (one bad triple of 18), confirmed by Cloud's independent check CL547.
- Five-bin H(h): exact (SEARCH), no failures 33333 h<=3, 33334 h<=2, 33344 h1; sharp at key h-1. Three-bin T(h) reproduced. Cloud CL504 kholek.c, tier1 measured, single-party.
- Four-bin H(h) (u_J>=L(r)+h*r, holes anywhere): exact, failures only 3333 with >=3 equal targets (h3..7: 1,1,1,5,12); 333X h<=6, 3344 h<=4, 3444/4444 h<=3 none; margin (h-1)r fails (sharp). Cloud CL503 khole.c, tier1 measured, single-party. CL501-502 absolute-margin claims withdrawn.

- At most3 deletions,M>=9,subset/complement sizes>=3:entire symmetric central interval PROVED G318/MI369,Cloud CL441/7f710b4e carrying read;25,004 supporting checks reported. H(h) upper-tail/joint compatibility still OPEN,no run.

- Protected TWO-bin margins suffice for h<=3,n>=7,r,t>=3 (h<=2 also n6),hand corollary MI371 conditional on W318. Endpoint trimming/complement gap close tails;h3,n6 exceptions retained,multi-bin allocation OPEN,no run.

- Protected h3,n6 two-bin failures are exactly two12/12 pools,hand MI373;actual two-pivot shapes repair them under bounded-hole least-singleton hypothesis,MI374. Conditional on W318 for larger base;selector/pair branch OPEN,no run.

- Actual low-shape least singleton can contain0,hand MI376;universal <=3-hole selector REFUTED by explicit five-bin lift/every realization. Two-interval representation next;partition existence OPEN,no run.

- Two-interval three-bin fixed regular counts:combined scalar bounds suffice;shared singleton rows repaired by cross-interval slide,hand MI378. Uniform count choice/crossed singleton rows OPEN,no run.

- Two-interval rows(1,1,c)/(1,k,d),c,k,d>=2:collision/endpoint repair hand SKETCH MI380;400 positive-row pairs/44656 rank targets pass bounded exact diagnostic. General smoothing/count selection OPEN.

- ALL positive fixed count rows on two intervals:combined individual bounds/total suffice,PROVED G319/MI382 by Cloud CL442/9fd9bd0a carrying read including MI378/380;adopted MI436. Count admission/zero branches/five-bin OPEN.

- Protected low-shape least-singleton:zero-count failures excluded,individual count intervals nonempty;conditional hand reduction MI383 to OPEN aggregate count capacity,G319 pending,no run.

- Protected low-shape GLOBAL least-singleton count capacity complete hand candidate G320/MI384;rooted partition conditional G319/MI383. Least-singleton-only weakening refuted by protected16/19/19;parent cases OPEN.

- Every protected low-shape p>=3 instance has explicit P_0/full-five-bin lift,hand scope algebra MI385;strict-pair root choice remains OPEN,not outside actual domain.

- Protected low-shape adaptive zero owners:63,589 finite targets admit nonexceptional counts;4,785 literal targets partitioned,12 false scalar owners retained,COMPUTED MI387. Universal selector/five-bin OPEN.

- Protected low-shape:any scalar-admitted zero owner yields some partition after pair-cut/regular-row/three-small-case repairs,conditional hand SKETCH MI389;universal owner admission OPEN,no run.

- Protected low-shape always has a zero owner with all scalar K intervals nonempty,hand SKETCH MI391 via exact gaps/forced-owner/top-sum budget. Aggregate count bounds still OPEN,no run.

- Protected low-shape excessive-minimum-count roots:exactly two configurations,both explicitly repaired by changing zero owner,hand SKETCH MI393. Maximum-count owner capacity remains OPEN,no run.

- Protected low-shape ALL targets,size>=3,proper cuts margin3:COMPLETE COMPOSITE HAND CANDIDATE G321/MI395 via owner existence/four count-failure repairs/MI389;G319 dependency,review pending,full five-bin OPEN.

- Parent P_0 least-singleton missing-pivot route:prefer low repair/G321;empty prefix impossible,end trims G315. Only high{1,2,M-1} remains,hand conditional MI397;legal two-hole/nonsingleton branches OPEN.

- Protected high shape {0} union[3,n] union{n+2}:complete HAND CANDIDATE via two endpoint owners/full-interval MI295,MI399. Conditional parent missing-pivot branch completes with G321;legal two-hole/nonsingleton branches OPEN.

- Actual protected two-hole legal pivot:all45 compressed-count states cycle under lexicographic feedback despite10 partitions;relabelling converges,COMPUTED/explicit hand cycle MI401. Blind feedback parked,existence OPEN.

- SAME protected two-hole fixture:minimum-physical-error fibre feedback strictly improves for all minimizers at42 positive states,3 goal states,COMPUTED MI403;general existential descent OPEN,size2 countercontrol cycles.

- Protected bottom-adjacent two holes:existential optimal-feedback escape in one step,hand SKETCH MI404;universal minimizing-choice descent REFUTED by protected3/3/6 cycle MI405. Separated thresholds/five-bin OPEN,no run.

- Protected holes1,3,three sizes>=3:joint0/2-owner budget and MI295 give complete hand SKETCH MI406;size1 shortcut avoided. General two-hole/five-bin OPEN,no experiment.

- Protected holes1,q:every scalar-eligible zero owner meets both aggregate high-count bounds,hand SKETCH MI407;unprotected failures classified by budget2. Owner existence/joint compatibility/five-bin OPEN,no run.

- Protected holes1,q,three sizes>=3,proper cuts margin2:COMPLETE COMPOSITE HAND CANDIDATE G322/MI407-409;owner/count/exception repairs,dependent G319/MI383. Review pending,arbitrary first hole/five-bin OPEN,no run.

- Protected two-hole3/global-least singleton with <=3-hole realization completes,conditional MI410/W318;MI411 actual five-bin descendant forces4/4/5 holes for every such realization. Selector REFUTED,existence OPEN,no run.

- Four-hole protected two-bin criterion with one size3 has exactly one16/16 exception;parent repairs it and globally least singleton admits<=4-hole realization,UNREVIEWED MI412-413. Other-triple branch candidate,MI371/410 dependencies;general parent OPEN.

- CL441 adopted: G318 PROVED;G319/G321/G322 finite checks only,hand reads pending. Next trunk/coverage reflection;new local extension parked,MI414/GC1551,no seeded draw/new review request.

- Parent coverage matrix and two-level diagnostic scope audit MI415/GC1552:singleton routes partial,nonsingleton branches OPEN;N<=16 misses two-larger-bin gap. No new theorem/run;next actual P_0 pair-boundary selector.

- P_0 minimum pair requires boundary moment L(r)+r+h,reflected complement L(s)+h+q;exact selector and old-fixture bands audited MI416/GC1553. No general selector theorem/run;G316 unchanged.

- Protected missing1 FOUR-bin strict-minimum-pair branch:lowered staircase/two neutral exceptions with uniform complementary spectra,COMPLETE HAND CANDIDATE MI417-418;G316 dependency,review pending,general P_0/five-bin OPEN,no experiment.

- General-q pair boundary:rank identity H-ell=h,skipped staircase moment repaired by alternate unit move;hand instrument MI419/q3 control. Joint mapped spectra OPEN,no new review/experiment.

- Fixed n14,(3,3,4,4),all q:2722 strict-pair targets pass one neutral boundary exchange,canonical fails21,controls COMPUTED MI421. General-q long-prefix canonical-hit region HAND CANDIDATE MI422;moment skips/short prefixes OPEN.

- Owner's CL441 appraisal implemented as parent-level trajectory/assumption/dependency check,MI423/GC1557;13min prompt revised. B218 extension deferred for coverage test,no new mathematical result.

- Skipped-moment-only extension leaves unbounded actual five-bin descendant families with long prefixes,hand scope test MI424/GC1558;extension parked,next common physical-gap condition. No partition theorem/run.

- Canonical boundary thresholds reduce either prefix defect to one punctured interval;trimmed-slice bridge hand MI425/GC1559. q1 missing13 survives at join;general target coverage OPEN,no run/review request.

- Protected pair canonical moment hits,left prefix>=5:ALL hole positions covered by HAND CANDIDATE MI426/GC1560;skips/short prefixes OPEN,no experiment or status promotion.

- Skipped moments force triangular opposite excess;uniform spectra at base prefix>=5,HAND CANDIDATE MI427/GC1561. Combined strict-pair r>=17 candidate;small-left/unbounded-opposite residual OPEN.

- Protected strict-pair selector:4058 short-prefix left profiles,1226 full-spectrum comparisons leave exactly4 triple-pair misses,COMPUTED MI429. Uniform opposite/tail reduction HAND CANDIDATE MI428;q7/q10 repairs still OPEN.

- Protected one-hole FOUR-bin strict-minimum-pair branch:COMPLETE COMPUTER-ASSISTED CANDIDATE MI430,uniform q7/q10 repairs plus MI429 finite spectra;carrying hand review pending,singleton/triple/full-five-bin OPEN.

- MI422/426 scalar support,m6..12:9683 bands/1427 pools,16430 full-spectrum comparisons and negative controls pass,COMPUTED MI432;unbounded hand claims remain unreviewed.

- Triple-minimum P_0 reflection can force a unique deletion outside protected margin2,even on an actual five-bin descendant;explicit positive parent/control,hand MI433. Shortcut REFUTED,parent OPEN.

- Exact strict-triple child gate admits holes4,6;targets7/15/23 are incompatible,hand/COMPUTED MI435;two actual ancestors partition differently. Fixed canonical completion REFUTED,run stopped first negative;parent OPEN.
- G319 independently PROVED by CL442;G320/G321/G322 retain their own unread arguments. MI430 m16 supporting check53490 instances is not carrying verification;adoption MI436.

- Joint-selection consolidation finds no new mechanism beyond MI303/325/330;GPT chooses owner-authorized incubation,MI437/GC1570. Both mathematics schedules PAUSED;parent/statuses unchanged.

- CL443 assessed:actual-hole upper-margin alternation fails for every selected top bin;four-bin21^4 negative violates conditional group-count bound,hand MI438. Seven-fixture diagnostic registered MI439,completed MI440;13min resumed.

- Joint-count14 fixture/reflection diagnostic passes independent maps/oracles,COMPUTED MI440;old size3 negative still admits all conditional group bounds,hand MI441. P_0/five-bin OPEN,no coverage gain.

- Fixed-count group bounds equal convex hull of attainable vectors;one-sided rank split integral but ownership unresolved,hand known-geometry audit MI442. One minimal rounding test registered MI443,NOT RUN;parent unchanged.


- Minimal one-sided pattern:all1234 rank targets realized,independent maps/negative controls COMPUTED MI444. Uniform(a,1,1,1)/(0,k,k,k) construction HAND CANDIDATE G323/MI445 using PROVED MI295;parent admission/five-bin OPEN.


- Balanced P_0 family[0,4r] minus2r,size-r targets2r^2 forces all FOUR bins to cross;literal partitions/actual five-bin lifts,hand scope obstruction MI447. Universal one-sided selector fails;G323 unchanged,GPT incubates/schedules PAUSED.

- G323 independently PROVED in scope by Cloud CL446/a33d8bff, adopted MI448; 96,360 supporting cases reported. General integral rank split confirmed as PRIOR-ART via Frank discrete separation in Fujishige's primary slides; all-thick four-bin completion follows G316.
- Four-bin two-interval counts (1,b,c,d), b,c,d>=3, opposite row all >=3: PROVED G324/MI449 via two-direction singleton repair and strict-submodular tight cuts, Cloud CL448/48a1cd79, adopted MI457; 281,891 supporting targets reported. Count selection/multiple thin rows/five-bin OPEN.
- Tan–Teh's known (45,45,45,45,72,74,74) exception fails pair-group COUNT admission: minimum counts 18, pair congestion requires 22>20. Hand explanation/local threshold and literal positive control MI450; no new nonburnability or global uniqueness claim.
- Full interval N11, counts (2,3,3,3): all 7,417 rank vectors realized by two independent complete maps, 92,400 partitions; negative all-size-two control passes, COMPUTED MI452. MI451 one-hole warning WITHDRAWN (missed subset); general one-size-two theorem OPEN.
- One-size-two full four-bin audit: strict-pair and thin-minimum branches close by hand; remaining protected one-hole3 statement H2 and exact actual-residual gate isolated, UNREVIEWED MI453. H2/full-row/five-bin OPEN; no run or new review job.
- H2 counts233/234, all internal holes:1,659 protected domain-targets pass independent maps, COMPUTED MI455. Closest pair always rank-feasible by hand but can miss a scalar sum; all-pair spectrum-union target MI456, H2/parent OPEN.
- H2 completes when legal sum-u pair count exceeds min(b,c), elementary hand pigeonhole application MI458; equality includes unbounded balanced central family. Stronger three-hole localization not imported; H2/parent OPEN, no run.
- H2 central pair sum u=M, all b,c>=3/internal holes: complete UNREVIEWED HAND slice MI460; matching plus one-/two-hole spectra, explicit small controls. Unmatched-token-only restriction refuted; trajectory MI459 returns next work to whole-choice occupancy threshold, parent OPEN.
- H2 strict sum-preserving two-token escape REFUTED by protected (3,12,20), B057, full fibre/positive partition MI462; stopped second state. Neutral path exists. GPT incubates global-choice inference, both mathematics schedules PAUSED, MI463/GC1585.
- CL449 reports H2 through M14:73,231 canonical instances,zero failures. Its regime2 minimum/slack and high-pair existence estimates fail admitted M9 hand controls, MI464/GC1586; computation retained as support, incubation/PAUSED schedules unchanged.
- CL450 corrected scope: measured three-hole distance4 bound, depth>=5 conditional; overlap with unread MI354–355 noted MI465. Explicit infinite H2 family has depth1 while both original-extreme distances diverge, positive partition MI466; all-shallow/global choice OPEN, schedules PAUSED.
- Owner resumes GPT after CL451–454;13min ACTIVE, Local owns L8 run. Pair-sum doorway is known permutation X-ray problem, MI467. Cuts+ALL unweighted group capacities REFUTED at k8 by weighted9>8 hand certificate MI469; real E24 sorted-high all-odd profiles necessarily contain14..17, MI470; sufficiency OPEN.
- Order8 cuts+support14..17: ALL119 profiles realized,TWO-PARTY COMPUTED MI472/CL455. Actual all-odd E24 admission MI470/473 independently VERIFIED CL455,adopted MI477;structural matching/fullL8 OPEN.
- Central119-class isolated adjacent +/-1 cycle REFUTED at fourth profile; forced cycle type(5,2,1),hand MI475. Strategy switches to exact tight-cut factorization MI476;existence unchanged, no domain expansion.
- Pair-sum tight cuts factor exactly (upper normalization3r); only1/70 actual all-odd E24 targets has a tight face,hand MI478-479 UNREVIEWED. Boundary recursion parked;interior matching mechanism OPEN,no run.
- Ordered-target source check finds no applicable interior construction;119 hand question PARKED,MI480. Separate read-only L8 stream completeness verifier passes tiny can-fail controls MI482;production/independent verifier pass NOT CLAIMED.
- L₈ ≤ 68, odd-integer form: all 64,787,844 towns E24..E32 tile, MACHINE-CERTIFIED tier 1 (check 64,787,844 valid and GPT's stream verifier COMPLETE, same sha256 90fea878…; counts independent; E24/E25 by two solvers) + MI044 reduction — L743/CL454. L₈ = 68 with Tan–Teh Thm 1.3 (published, unaudited here). Hardest town 4,916 nodes; L4 REFUTED. K2′ stopped at its cap (8 LSD certified, 8 MSB undecided), owner 10-19.
- L8=68: joint COMPUTER-ASSISTED THEOREM G325/MI484-486, Local L74369cc079e all64,787,844 certificates+two full verifiers; exact induction/graph bridge/lower witness read by GPT. Archival/access,external scrutiny,novelty remain; no general-n/prize claim.
- L8 release (CL461/L744): timing-free sha256 da7c2e77…3a96 of the retained stream; four-level timing-free digest equals Cloud's regeneration (0d3799d0…669530f1), so the run reproduces byte for byte across machines except timing; nine xz files 340 MB plus manifest, round trip COMPLETE VERIFIED; published to the site's eightstreets/release/data/ on the owner's word.
- Owner resumes eight-streets structural/H2 work,13min ACTIVE; stronger all-pair support-interval claim REFUTED at M8,q2,u8,gap6 outside protected[7,19],first18 domains only,COMPUTED/hand MI495–496. H2 unchanged; positive first-unhit-pair coefficient encoding is reformulation,not proof; no larger census.
- H2 protected counts(2,b,c),b,c>=3: COMPLETE HAND CANDIDATE G326 via G315 construction/pair-gap audit,MI497–499;1128 scalar pools/932 repairs pass finite same-worker checks. Independent carrying review pending; four-/five-bin parent unchanged,13min ACTIVE.
- G326 root-interface audit on SAME1659 targets:1793 allowed roots/1975 recipe branches pass,COMPUTED MI500–501. Unbounded actual-slack comparison eliminates high-gap fixed cores/alternate repair; candidate simplified,independent carrying read pending,no parent promotion.

- H2 protected one-hole counts(2,b,c),b,c>=3: PROVED G326 by Cloud carrying read CL466/01131375, adopted MI502/GC1601. Later MI501 simplification self-audit only; MI453 four-bin reduction/five-bin parent unreviewed, novelty UNASSESSED.

- Full-interval four-bin cut sufficiency, sizes>=2/at most one2: COMPLETE HAND CANDIDATE G327/MI503–504 via PROVED H2 G326 and explicit P/Q pair spectra. Independent carrying review pending; five-bin count admission/multiple thin rows OPEN, no new computation.

- G327 endpoint/tie/reflection self-audit complete MI505. Exactly-two-size2 full-four-bin cut criterion fails even all STRICT cuts, unbounded(a,2,2,c) forced-extremes family MI506, already implicit MI308 W2; no new mechanism/status or review queue.

- Protected one-hole counts(2,2,c),c>=3: COMPLETE HAND CANDIDATE G328/MI507–508, only q1 pairtargets4/6 and M7,q3 pairtargets3/8 or4/10 fail. Global unique-pair exhaustion; strict protected cuts suffice. Independent review pending, no G327 dependency or parent promotion.

- Actual four-bin lifts of G328 obstruction types force k0, MI509–510: q1 is old forced negative; both M7,q3 families have uniform staircase/alternate-root partitions. Singleton/triple exhaustion CONDITIONAL on unread G328; strict pair(2,2) branch remains, no new proof entry.

- Full-four-bin counts(a,2,2,c),a,c>=3: strict-pair branch closes via Q4(2)/actual P_n(2) complement, hand MI511–512. Combined with MI510 gives exact old forced-family-only classification CONDITIONAL on G327 scalar lemma/G328 plus unread parent interfaces; no new proof status/entry/job.

- Two-size2 parent classification consolidated in FOUR-BIN-PARTITIONS section11, MI513–514: full parent argument relative to G327 scalar lemma/G328; ingredients AND composition unreviewed. No new coverage, status, proof entry or numerical experiment.

- Exact two-size2 family remains outside the known COMMON-sum slice under0/1-based translation and reflection, hand scope audit MI515–516/PRIOR-ART. Two bounded search batches no exact counterpart found, novelty UNASSESSED; no parent coverage/status change.

- Protected one-hole(2,2,c),c>=3,EQUAL pair targets: direct edge-count completion avoids G328, hand MI517–518/FOUR-BIN-PARTITIONS section11.6. High endpoint immune to deletion; c2 negative8/8/3 retained. Dependency reduction only, no parent coverage/status upgrade.

- One-hole r equal-target pair bins plus one size-c filler, protected cuts: HAND endpoint classification fails exactly u=2M-2r,c<=q<=r, MI519–520/FOUR-BIN-PARTITIONS section12. Known matching ingredient, specialization unreviewed; no parent/status upgrade or run.

- Two distinct sum fibres form alternating paths; coarse colour/total capacity REFUTED by strict-protected9/9/10/4, weighted6<7 hand certificate MI521–522/FOUR-BIN-PARTITIONS section13. Known matching framework, parent/status unchanged, no run.

- Alternating-path quota supports compose via cheapest full odd components: exact HAND criterion r+s<=K+alpha(r)+beta(s), MI523–524/FOUR-BIN-PARTITIONS section14. Known ingredients, formula unreviewed; two-target/one-filler test, parent unchanged, no run.

- Two-sum components on[0,M] minus q: residue-pair interval intersections, fixed-centre rays and one deletion give exact HAND readout MI525–526/FOUR-BIN-PARTITIONS section15. Known reflection ingredients, unreviewed, no parent/status change or run.

- Protected adjacent pair targets plus one filler: exact two-endpoint failure list, sharp ordinary c>=t+1/strict c>=t thresholds, COMPLETE HAND CANDIDATE G329/MI527–528/FOUR-BIN-PARTITIONS section16. Independent review requested; no older unread premise or parent promotion.

- Arbitrary-gap filler-only guarantee REFUTED by HAND strict-cut family: four sum10/three sum22 pairs,q1,ANY c>=7 need11 low tokens from10, MI529–530/FOUR-BIN-PARTITIONS section17. Known weighted-capacity mechanism; G329 adjacent scope/parent unchanged, no run or new review job.


- G327/G328 and full(a,2,2,c) section11 composition PROVED by Cloud CL468/0e3f4daa; G329 adjacent-target classification PROVED by CL469/64af1b21, adopted MI531/GC1616. Supporting scripts read/not rerun; sections12–15 unreviewed, novelty UNASSESSED, no five-bin/equal-shares transfer.

- Two-target pair-quota support has no integer holes; finite weighted tests complete, PROVED G330 by Cloud CL470/cd65c481 carrying read, adopted MI543/FOUR section18. Reported5,150 random pools/negative control support hand proof, instrument read/not rerun. Current packet verification map distinguishes unreviewed sections; no multiple-filler/three-target transfer.

- G330 source scope: nested-fan lattice theorem/repeated IDP do not directly carry mixed downward addition, MI534/PRIOR-ART. Old(4,8,10,23) blocks automatic two-filler transfer; real E24 sorted-high profiles require >=4 labels. No new theorem/run/status; G330 review pending.

- Actual-three-sum fixed diagnostic:8 AP-target fixtures/963 quota points have no holes; independent supports/exact hull/reflection and genuine-hole controls PASS, MI535–536. AP selection bias explicit; primitive(1,-2,1) perfect-face lattice is a hand scope observation, no universal integrality or new proof job.

- Three AP sum targets on any finite real-token pool: perfect quotas form a primitive lattice segment, HAND known-switch specialization MI537–538/FOUR section19. Alternating-cycle inversion sorting handles sparse/fixed orbits; varying covered-set partial quotas OPEN, no new experiment/status/job.

- Arbitrary three-sum no-hole extension REFUTED by sparse seven-token path: quotas201/021 midpoint111 would leave absent24, hand MI539–540/FOUR section20. AP substitution forces token collision, so AP partial quotas remain OPEN; early trajectory closes generic-colour embedding repair, no run/job.

- AP partial-quota no-hole extension REFUTED: P=[0,8] minus{1,7},targets8/9/10, actual201/021 midpoint111 leaves absent1, hand MI541–542/FOUR section21. Extra26 retained; explicit downward3D mixed-addition hole explains dimension boundary. No one-hole/interval claim, run/job; next consolidation.

- Full-four-bin minimum2 count audit MI544: only unbounded row(2,2,2,c),c>=3 remains beyond proved classes. MI452's finite all-pair30 misses equal permutations of(2,6,8,12)/(4,4,10,10), COMPUTED consequence/no rerun. Source displacement/involution constraint retained; next merged-cut/large-fibre hand test.

- Full-interval(2,2,2,c),c>=3: central>=5-edge fibre and mixed-endpoint completion reduce ALL failures to fixed low triples plus M8..16 endpoint inputs, HAND/unreviewed MI545–546/FOUR section22. Proved three-bin premise only; finite basis unsolved, no experiment/job.

- Three-pair full-interval classification: COMPLETE COMPUTER-ASSISTED CANDIDATE G331/MI547–548, only2/6/8 and reflection fail. Fixed5,146 basis queries/two same-worker engines/controls COMPLETE; unbounded section22 interface still unreviewed, no larger census or parent PROVED upgrade.

- Protected[0,M] minus1,four counts>=3: COMPLETE HAND CANDIDATE G332/MI549, minimum-mean zero owner feeds PROVED G327; all-group and ALL-bins cut proof, hand controls. Replaces MI417–418 endpoint branch; general q/five-bin OPEN, no experiment or G331 dependency.

- General-hole interface audit MI550–551: all compressed sum fibres feasible does not ensure compatible counts; finite bad-vector avoidance helps FIXED rows only. Protected positive10/39/39/40 forces one bin wholly low; general selector unchanged. No run/job; trajectory stops endpoint repairs, next global count/moment source read.

- G331 and G332 PROVED by Cloud CL471/642155b9 carrying reads plus separate finite support, adopted MI552. Original proofs preserved; minimum-mean zero-owner tool named. MI553 primary source audit supplies no count-admission implication; next zero-peeling invariant test, no new experiment/general-hole upgrade.

- CL472 count-box/parity perspective read at MI554: source protection predicate is stronger than baseline; 5/5/11/11 meets baseline but has size2. Protected3333 example6/21/24/26 has unique GOOD-parity count, so universal axis-width claim fails. Next audit singleton-box obstruction criterion, no theorem/run adopted.

- Four-variable subset-interval region: real-feasible/integer-empty iff three complementary pair intervals are pinned at wrong parity, PROVED G333 by Cloud CL474/16404637, adopted MI575. Nonempty-real/integer-endpoint scope; parent REAL admission/thin completion OPEN.

- One-hole singleton count intervals admit conserved total under actual ranks/nonemptiness, sizes>=3, ANY n>=2: PROVED MI557/579/FOUR25–25.1 by Cloud CL475/489d287c, adopted MI582. Joint real region/physical completion OPEN.

- Protected positives refute merged-count full-fibre inheritance and raw-endpoint supermodularity; raw failure does NOT exclude set-level g-polymatroid representation, HAND MI559. Early trajectory MI560 switches to actual balanced double-cover inequality; parent OPEN, no run/job.

- Single M12/q6/c3333 balanced-cover ceiling mechanism:4096 scalar subsets/34 deficit allocations, two engines maximum136<144, controls PASS, COMPUTED MI561–562. HAND price9 certificate/three-endpoint symbolic envelope; no domain enlargement/general count-admission claim.

- Symbolic common-price ceiling certificate REFUTED by literal endpoint mixture, HAND MI563/GC1635: count219,cost4903229/99>48400. Fractional obstruction only; discrete ceiling/balanced inequality/parent OPEN, no census or review job.

- Four-row discrete ceiling maximum reduces exactly to <=189 symbolic endpoint/residual tuples, known geometry rederived MI564/PRIOR-ART. No candidate census/general cost bound or parent coverage; plateau/slack guards retained.

- Protected min3 four-bin rounded count region: REAL nonempty implies integer point, PROVED G334 by Cloud CL474/16404637, adopted MI575/FOUR26. Scalar pin/star-triangle carrying proof; REAL admission/physical thin completion OPEN.

- Fixed minimal M12/3333 ALL11 holes:3557 protected sorted count regions REAL/integer feasible, COMPUTED MI567–568/GC1638; two mechanisms,45568 scalar masks/five controls. No physical partitions/uniform admission claim or larger census.


- One-hole four-bin mean counts both sides>=3: explicit all-group rounded selector plus known rank split/G316 physical composition, HAND/unreviewed MI569–570/FOUR27. Uniform central partial coverage, three fixed-size6 family; general boundary OPEN, no census/new review job.

- Known fractional count projection uses linearly interpolated moment bounds, not raw quadratics; nonempty Q does not imply inward-rounded P, explicit old size2 guard MI571/PRIOR-ART. Parent coverage unchanged; current-state summary shortened.

- Arbitrary fractional-point largest-remainder selector REFUTED on protected M12/q6/3333/18^4, exact Q slack3/10 but rounded count3 needs24, HAND MI572–573/FOUR28. Parent positive retained; MI574 deliberate incubation, schedules PAUSED, GC1641 specific perspective request.

- Corrected core checklist:41 proper collections/9 types (42 with{V}); type9 requires2rho1. G315 carries types3–4; MI557/579 budget5–6 now PROVED by CL475, crossings7–9 OPEN. Known framework/scope audit MI576–577/FOUR29; later adoption MI582, heartbeat PAUSED.

- Singleton high-count budgets under actual rank cuts/nonempty spectra extend to ANY number of minsize3 bins, PROVED MI579/FOUR25.1 by CL475, adopted MI582; one distinct pool, j2 correction retained. Core rows1–6 carried; crossings7–9/physical parent OPEN.

- Replicated-pool singleton-budget transfer REFUTED by two-copy size3 targets3/7/13/13: literal fractional witness, maximum high counts5<6; HAND/control MI580–581/FOUR30. Outside protected parent; crossings unchanged, deliberate incubation/13min PAUSED, GC1644.

- CL475 correction adopted: crossing forms use three labels algebraically, but weaker hypotheses remain empirical; four-used-fibre scan differs from all-seven-fibre scan, M15 witness has two empty unused fibres. Protected M13 kills all three local uncrossings; hand/example audit MI582–583/FOUR29.1, heartbeat PAUSED.


- One-hole four-colour tournament normal form: PROVED G335/MI584-585/FOUR31, Cloud CL477/f70717bb carries flow/path/replacement/recursion -> <=11 cyclic components/45 vertices. Ordered bulk unbounded; absorption/parent OPEN, no M<=45 census. Owner resumes13min research on exact absorption-cut question; no extra poller.

- Distinguished triangle plus one consecutive ordered run with each ordinary colour>=3: HAND candidate G336/MI586–587/FOUR32, unit tight-prefix gate + PROVED G316 lifts opposite correction, Phi+2 with q fixed. Independent review pending; larger core/thin runs/parent OPEN; no census.

- One thick ordered run (four counts>=3) absorbs ANY rainbow cyclic component<=5: HAND G337/MI588–589/FOUR33; slack<=4 cuts form chain (separation9), core debt<=5, fixed-* ordering and PROVED G316 repair. Replaces G336-only review; run existence/thin parent OPEN, no census.

- Joint component cut budget/shape-only shortcut guard: protected M12 cyclic thin-run control is nonmaximal, MI590. Old MI551 compression recognized; separate restricted inversion optimum has WORKING HAND <=2 descents via neutral equal-score flips, MI591. Unverified, no new read job; not G335's global maximum or parent progress.

- Global tournament maximum requires C>=m on actual simple colour-edge circuits; known common potentials alone fail protected NONmaximum, WORKING HAND MI592. Quadratic balanced-reversal/protection inference OPEN; no new review packet or parent coverage.

- Global tournament maximum has <=2 cyclic components/6 vertices: HAND G338/MI593/FOUR34; paired opposite paths forbid two shared colours. Two components must be triangles sharing one ordinary colour. Bulk unbounded; parent OPEN, consolidated independent review pending.

- Working full-palette-core exclusion MI594: actual neutral core/run switches retain strongness and force singleton blocks at degree-gap1; min3/protection then obstruct4-/5-core. HAND/unreviewed, G338 overlap application conditional, no new review job or parent coverage.

- Protected M12/q5 whole exterior fibre forces A01/B11,12, refuting direct-adjacency forcing; disjoint C-mediated repair Phi+2 explicit, HAND MI596. Global-max/parent unaffected; joint all-choice inference incubating,13min schedule PAUSED/no poller, GC1655.

- CL478/9a7e4136 independently carries G337 absorption/G338 six-cyclic-vertex refinement; PROVED, adopted MI597. G336 a corollary; parent OPEN, ordered bulk unbounded. Sources read/not replayed.
- CL478 protected M12/q7/26,8,16,21 refutes universal fixed-run-count transfer; full partition must change side counts, hand audit MI597. One-hole census through M17 reports54 exceptions, one known family; universal classification unproved.
- A2 two-hole base is independent: old MI368 also has UNIQUE least raw-rank singleton and EVERY realization leaves>=3 holes, MI597. No automatic G316-to-parent bridge.
- Extreme filler deficit d<=D, other counts total K: all joint partitions reduce bijectively to first K+D available values, known rank argument MI598/FOUR35. Two triples,d<=3 give ambient maximum<=10; only that stratum, no scalar-inheritance or all-A2 cutoff claim. Owner resumes13min research, next exact slack1 six-value complement classification; no new census/review job.

- Two-hole three-bin sizes(3,3,c),c>=3,filler maximum-minus1: COMPLETE HAND candidate G339/MI599–600/FOUR36, only holes1/4 with12/12 or2/3 with8/16. Unique filler gives21 six-value pools; original-spectrum edge lift excludes remaining gaps. One carrying review requested, no census/parent coverage; next global slack localization, not automatic d2/3 tables.

- All-choice A2 gate: positive sizes(a,3,3), holes a/a+3, targetsL(a)+7/3a+9/3a+9 has UNIQUE least raw slack7 yet every canonical first-bin recipe fails, HAND MI601. Not a localization counterexample. Primary logistic first-bin-fibre theorem needs positive column margins, violated at two holes; no connectivity/coverage transfer, MI602. G339 sole carrying packet, next exact binary-fibre hypothesis.

- Unqualified two-hole first-bin fibre connectivity by2-for-2 moves REFUTED: S=[0,7] minus1,3,size3/sum12 has only isolated057/246, HAND MI603. Complement3 is OUTSIDE actual A2 complement>=6, so that scoped question and coverage remain OPEN; no new review job.

- Actual A2 first-bin quadratic connectivity REFUTED for every M>=10: holes5/7,size3/sum8 only026/134, complementM-4>=6, HAND MI604. Positive8/17/(T_M-37) family has all raw slacks>=5 at M10; failure-localization conjecture untouched. MI605 same-assumption strategy check chooses incubation;13min PAUSED/no poller, G339 sole carrying packet. Reopen on joint-coverage mechanism, justified new reduction or owner direction.

- G339 unit-deficit/two-triple A2 classification PROVED by Cloud CL479/72e62a6e, adopted MI606. Complete21-pool and original-spectrum interface independently carried;11,022 supporting checks through M20 reported/not rerun. CL479 D<=7 gap table measured only; D6 threshold10 leaves8/9-value remainders outside, no global localization.
- At most3 deletions,n>=7,r,t>=3 imply actual missing-sum depth<=4: COMPLETE HAND G340/MI607/FOUR37, independent carrying read requested. G318 triple interior+anchored low tails+sliding fixed-end triples, explicit4/4 join; bound/threshold sharp. Conditional A2 legal-pivot h>=5/other sizes>=5 slice MI608; missing-pivot margin gate next. Parent OPEN;13min research resumes, no census/old finite-basis dependency.

- Missing-pivot three-hole inheritance fails even with unique least raw slack5/other sizes>=5: positive sizes(3,5,M-9),holes5/7,targets8/42/(T_M-62),EVERY first-bin realization leaves4/5 holes, HAND MI609. G340 unaffected; next global large-span pair-cover test, not a repair table/census/new review job.

- Arbitrary-D large-pool scalar depth<=2D-3 for D>=4,max(r,t)>=4D-1,min>=3: COMPLETE HAND G341/MI610/FOUR38, independent of G340; anchored pairs+low-survivor induction+sliding triples. Actual balanced-pivot repair margins>=6 give CONDITIONAL A2 h>=6/other sizes>=5/one>=15 slice FOUR39/MI611. One consolidated carrying packet; parent OPEN.
- G341 cutoff and one physical t5 join reduce a useful D4 strengthening to EXACT6423 normalized triple pools,D<=4,n>=8,N<=16, MI612/FOUR40. Instrument NOT YET frozen/run; no census, sharper threshold adoption or parent finite-M reduction.

- Exact D4 triple basis6423 pools COMPLETE/two engines/independent rank-gap domains/all controls PASS, MI614/FOUR41. With unread G341(a) and physical t5 join, conditional FOUR39 drops max>=15; remaining3/4 and parent selector OPEN, no new census or universal promotion.

- Explicit protected q5/(3,s,s,s),s>=5,targetA9/balanced others reaches CONDITIONAL A2 region through actual018, MI615/FOUR42. Same large companion counts retain MI368 selector obstruction at A6; no universal selector or unconditional promotion.

- FOUR39 all-rank hand self-audit finds no discrepancy, MI616/FOUR43; no independent promotion. MI617 same-assumption trajectory incubates all-choice parent selector:13min PAUSED/no poller, GC1666 specific perspective; reopen on concrete invariant/representation or changed mechanism.

- Cloud CL480/8bfe2134 carries G340/G341, adopted MI618/GC1667; FOUR39/41 remain conditional. Overnight CL542 ALLR finite evidence motivates bounded universal-compatibility hand audit;13min ACTIVE, CL529 committed checker syntax snag unrepaired/pending source recovery.

- CL508 local coarsening/inheritance WITH CL515 correction and CL517 triple H2 at n>=2h+4 PROVED by GPT MI619 carrying reads, filed C9/C10. MI620 exact14-cut child image plus rho+Delta=3N-D retained; no universal child/parent completion,13min ACTIVE.

- Top-tight333X small-target order forces rho>=9+ceil(Delta/3); complete child triple fibres give HAND small-fibre/shared-forced-vertex obstruction, MI621. Actual protected3336/36,12,15,56 control has only5 target12 triples, killing uniform-density shortcut; child positive, CL542 OPEN. MI622 trajectory incubates,13min PAUSED/no poller, no experiment/new review.

## Prize swarm on the smallest open Erdős prizes (2026-10-22, Local; PRIZE-SWARM.md, L750–L751)
- Twelve parallel agents, one open problem each, from the lowest prize up ($10 to $100). All results are single-party
  and await second reads; no prize is won and no prize question is settled.
- **Machine-checked by Local:**
  - **#552:** R(C₄, K_{1,41}) = 49, from a 7-regular C₄-free graph on 48 vertices plus Parsons' bound. Novelty NOT FOUND
    in one search.
  - **#711:** the K_{2,3} construction gives F(n) ≥ 3K+1, checked at n = 20, 22, 25 and 31. Exact F(n) for n ≤ 24 is
    MEASURED by the agent.
- **PROOF-SKETCH:**
  - #708: g(n) ≤ 2n for n ≤ 20.
  - #7: an odd covering needs at least 5 primes in its lcm.
  - #634: for N = 19, only the integer-sided equilateral case still rests on Beeson.
  - #470: exact weird criterion for 2^k·p·q; the √N barrier is intrinsic.
  - #647: density ≪ x/(log x)^r.
  - #32: O(log N) impossible under prime k-tuples.
- **MEASURED:**
  - #647: no n > 24 up to 5.2·10^10.
  - #710: exact f(n) to 10^7, favouring the lower-bound shape.
  - #1052: a new unitary perfect number has a component above 2^26.
- #94 is closed (Lefmann–Thiele; Lean). On its backup, #132, n = 14 is conditional on C13, which is open.

- Cloud CL495 exact depth3/4 gap list after<=3 internal deletions independently PROVED by GPT MI623, filed C11; j² exchange/disjoint blockers/both boundaries carried, G340 central premise. No numerical replay or multi-bin inference. Owner/CL546 restart quiet13min audits; next CL529 actual finite interface.

- Arbitrary-h top-tight EVERY-R extension: COMPLETE HAND counterexample candidate h12/3336/63,44,44,122, MI626/FOUR45. Unique least BCD; bad first triple forces both44 bins through0, parent positive. Cloud scope check pending; measured h1/h2 and one-hole parent unchanged, no run/threshold repair.

- Owner-directed GPT prize-swarm programme ACTIVE/no self-halt, MI628–630/REVIEW-1: all reports scoped reviewed, all prize won No. Exact #470 criterion carried; Corollary B counterexample k9,a55,b51 pending author response. R708 host assembly carried, global grouped-Hall admission OPEN; source/finite-receipt qualifications explicit.

- #1052 review scope corrected MI631/S1052-1: $10 asks FINITENESS, not a sixth example (separate 10 cents). Fixed-v2/component finiteness known; uniform bound OPEN. No prize won or new scan.

- #661 split-prime arbitrary norm filters satisfy |P||Q|<=p^2|S|^2, COMPLETE HAND known-geometry reproof MI632/S661-1. Squarefree density guard only; ambient norm pool is NOT actual support. Parent OPEN, no experiment/prize.

- CL550 #582 SDP gate audit MI633/R582-1: MaxCut reduction carried; floating SCS primal objective is NOT a rigorous upper certificate. Exact PSD dual condition supplied; no positive reported/refuted or new search.


- #132 all-but-one cocircular n>=7: COMPLETE HAND candidate G342/MI634/S132-1, saturation forces incompatible radial moments. Arbitrary extra point/centre control; independent carrying read pending, full prize OPEN, no experiment/novelty claim.


- G342 cocircular-plus-one second-rare-distance family n>=7 PROVED by Cloud CL552/71069ac0; adopted MI636/E2. Full #132 OPEN, novelty unassessed; exact n7 hexagon-centre control, no new experiment.

- #634 equilateral rational 120-degree tilings require N>18: COMPLETE HAND G343/MI642, endpoint/T-junction boundary proof, one carrying request. Literature-dependent N15 composition CONDITIONAL; full classification/prize OPEN, no scan.

- #552 f(41)=49 is KNOWN in Boza 2409.12770v2; swarm witness valid, novelty corrected MI643/R552-2. Full unbounded-deficit attempt inconclusive; no scan/new bound.
- #99 regular n-gons are exact triangle-free KKT points for all n>=4, standard HAND control MI644/R99-1; no local/global minimizer assertion or prize coverage.

- #7 full prime-power lift unresolved MI645/S7-1: actual prefix fibres defeat singleton grouping; general tail already known. No experiment/new coverage.
- #32 Radomskii 2610.14127v2 external log X loglog X lower bound source-audited MI646/R32-2, including carrying large-shift lemma. Cash subquestion negative in preprint; displayed question open, project prize won No.

- G343 equilateral rational 120-degree N>18 PROVED by Cloud CL558/5aa5a2d3, adopted MI647/E2. N15 composition remains literature-dependent, full #634 open; no rerun/prize claim.

- #32 direct exceptional-set repair only certifies log-squared window cost; global reuse missing, HAND/source MI648/S32-1. No full solution; GPT heartbeat PAUSED at explicit owner request awaiting continuance.

## Rule 30 Prize for AI agents (2026-10-22; reports/wolfram-agents/, CL567–CL570, L753–L757)
- Wolfram opened the prize to agents (kit at cc1e0e0, Lean 4.35.0, a submission API; partial results accepted). MAP.md maps our Rule 30 results against the kit's catalogue (Q01 = our LR; Theorem E and the channel bound absent there).
- **Submission 1, the white end** (PROOFS.md entry 40 on the kit's vocabulary, Cloud's module, Local's build and submission on the owner's yes): **R30-20261022-c27323, Lean Verified 2026-10-22 23:06 BST** (kernel replay, standard axioms, 4 headlines). Human Verified pending. No prize claimed.
- **Overnight 2026-10-22/23, on the owner's standing consent (L758):** words-A R30-20261022-5c4fbf and words-B R30-20261022-70d23b (the 128 words the kit lacks, entry 41; maintainer reruns pending), diagonals R30-20261022-0616de (B1–B3, Lean Verified), theorem-a4 R30-20261022-1d5070 (A⁗, Lean Verified), corollary-f R30-20261022-91b0b0 (Corollary F, first formalized; Lean Verified), rule-210 R30-20261022-920c1b (PROOFS 18: the kit's Q01 analogue is false for rule 210; Lean Verified). sturmian R30-20261023-e872a3 (Theorem E's characteristic case and every finite block code of it, via Corollary F; Lean Verified 01:02). sturmian-all R30-20261023-234c71 (**Theorem E in full**, every slope and intercept, GPT's GC1694 route through Corollary F; Lean Verified 05:54, automatic). rule-210-two-sided R30-20261023-b5421a (**PROOFS 32**, no finite configuration keeps rule 210's clock, from GPT's GC1700 chain; Lean Verified 06:45, automatic). **All ten Lean Verified by 06:45 BST on 2026-10-23 (L770)**; the word modules by maintainer reruns. Submissions 7–9 resubmitted 07:41 with corrected (UTF-8) abstracts and Lean Verified 07:44: the live ids are 0c4a33, 8084e6, 1bf4dc; e872a3, 234c71, b5421a superseded (L772–L773). Human Verified pending for the later ones; the night's seven Human Verified per the public page (CL592). **Submission 10, channel-12 R30-20261023-4767e0 (the channel bound certified at width 12, 0.2581 bits per visible bit; the verified checker GPT specified, Cloud built; Lean Verified 10:47, automatic; L776–L777).** **Submission 11, channel-14 R30-20261023-4d1a54 (width 14, 0.2445 bits, GPT's explicit-state design, 3,961 constants; Lean Verified 14:03 by maintainer rerun; L778–L779).**
- Lesson for every essay: put KernelCheck last; a TypeForm with a new "Open" set after it costs 50–60 s (L756).
- **The width-frontier lane on the M5 (2026-10-23, Local with GPT's design reads; tests/probes/wolfram/, L780–L794):** W1A reproduced the kit's width-52 certificate (14.5 s, 1.7 GiB per 64-chunk module, objects byte-identical to the kit's; L785); W1B measured one chunk check flat in W at fixed K (0.19 s, 0.9 GiB) and about K² in K (L791); **W2 built and kernel-checked Q01 for every start of width ≤ 56 (bound 100) in 294 s, the kit's checker passing the wrapper: a dry certificate, not submitted (L794); W3 did the same for width ≤ 60 (bound 128, K = 129 proposed then established by the complete check) in 1,849 s, every prediction held (L798; receipt in the shared store, sources archived outside git).** The owner withholds submissions (19:19 BST) until something more interesting. W4, the sequential-versus-two-worker pilot on W3's first and last module (w4_harness.py; designed L797-L801 with GPT's reviews GC1725/GC1727), ran once at the accepted version: gate PASS, two workers 1.80-1.84x the one-worker batch throughput with identical objects, sampled pair peak 4.0-4.1 GiB, no pressure (L802, figures corrected in L804). Then the owner handed Local the choice of lane; chosen: **D-exact** (L805; tests/probes/wolfram/d1_engine.py): the exact death time D(W) per width, kernel-checked above and below, the kit's table being "observed, not proved"; the engine's exhaustive tests show a lane's elimination level equals the physical death time (t = e) and give D(2..30); D1 ran at width 52 (L808): ATTAINED, start 0x7dc2ff6fcc4fd black at depth 1 through every even time below 96, dead at 96, two engines; D(52) = 96 a validated candidate pending D2's Lean lower proof (d2_witness.py, awaiting GPT's read); D2 then kernel-checked it (L810, d2_witness.py): **D(52) = 96 exactly**, `death_time_52_exact` = the kit's `q01_width_le_52` ∧ the witness through `prun`/`run_toFun`, Check.lean pass, standard axioms, 15 constants replayed: the kit's "observed, not proved" entry proved at 52. D1's stages then gave **D(56) = 100** (witness 0x93d4b223f5b9b5, the W2 bound attained) and **D(60) = 114** (census over all 4,096 chunks, witness 0xe77a4e77b8f99b5), physically validated candidates (L812); not 2W - c. Then **D(56) = 100 exactly, kernel-checked** (L816, death_time_56_exact, after a stopped attempt whose cause, archived generated sources, is recorded in L814); W5 then certified width 60 at K = 115 (64 modules, 21.6 min, Check.lean pass) and D2 case 60 gave **D(60) = 114 exactly, kernel-checked** (L818): three exact entries, 96, 100, 114. D3's width-64 census gave D(64) = 116 (candidate, L820; below the predicted range); reflection: the maximizers at a width share their deep bits and the table is driven by a sparse family re-used across widths (PROOF-SKETCH). **Submission 12, R30-20261023-8e6bd3** (L822): D(52) = 96 exact with the witnesses at 56 and 60 (reports/wolfram-agents/submissions/d-exact). Next: the verifier's verdict; a width-56-certificate submission as the verifier's time test; D4 revision 6 (GC1742's corrections). Cloud's standing GPU jobs (CL606, GPU-METAL-JOBS.md) are a list, not a priority.

- **GPT's directed CL586 second reads (2026-10-23, GC1695–1697/MI651):** `reports/wolfram-agents/GPT-CL586-REVIEWS.md` carries Corollary F, rule-210 and characteristic Sturmian formal statements in exact submitted scope. Essay corrections: substitution growth, prefix nesting from std1, diagnostic spacing labels. Frozen submissions unchanged; no own kernel replay or external Human Verified claim.

- **CL587 jobs completed (GPT MI652–654, 2026-10-23):** `reports/wolfram-agents/GPT-PROOFS32-CHAIN.md` gives the complete full-space rule210 statement/induction chain and retained control receipts; `GPT-CHANNEL-M20.md` gives exact width16/20 graph/vector certificates and fixed shared-store digests, with failed Core Lean benchmark and verifier feasibility unresolved; `GPT-CL588-REVIEW.md` independently carries the full general-intercept module of 28ad7455, no proof gap, minor display notes. GC1700/1702/1703 were sent to Cloud; no GPT schedule restart or submission.

- **CL590–591 reviewed (GPT MI656/GC1705, 2026-10-23):** `reports/wolfram-agents/GPT-CL590-591-REVIEW.md` carries all eight two-sided rule210 formal headlines, sideways background and finite rule90 alternative; one essay parity erratum. Channel tree bindings pass all rows; committed m20 predicate uses the weaker m16 numerator. Cloud kernel timings reported, physical bridge OPEN; heartbeat PAUSED.

- **CL594 jobs (GPT MI657/GC1706, 2026-10-23):** `reports/wolfram-agents/GPT-CL594-WORDS.md` gives HAND all-LR counterexample/interface and a larger residual-class control; `GPT-CL594-RECURRENCES.md` scopes generic FSR transfer; `GPT-CL594-CHANNEL-BRIDGE.md` specifies semantic checker and no-run m16 estimate. Q01 OPEN, no carrying promotion; Cloud sharp-ratio fix read, heartbeat PAUSED.

- **CL595–596 (GPT MI658/GC1707):** scoped CF/LR counterexample review adopted; width-12 physical channel source carrying PASS in `GPT-CL596-REVIEW.md`. CL597 final receipt and eventual theorem accepted at source-review scope; prose corrections remain; optional independent replay stopped before inputs, no retry or prize claim.

- **CL601 architecture read (GPT MI659/GC1708):** `GPT-CL601-WIDTHS.md` traces pinned Lean cache lifetime and kit replay; recommends explicit-set closure chunks, warns of symbolic checkpoint recomputation and table-size limits. Design only, no wider verification/run; heartbeat PAUSED.

- **CL603 width-14 carrying read (GPT MI660/GC1709):** section 7 closure/coverage and physical headline PASS; tiny pilot controls/source bindings checked. Essay constant/provenance corrections requested, full kernel receipt read not replayed; `GPT-CL603-REVIEW.md`, heartbeat PAUSED.

- **M5 job design L780 (GPT MI661/GC1710):** pinned lane-check source gives exact chunk count with K-squared work; records.c is odd-phase, kit death bound even-phase. Capped sequential W1A proposed, awaiting Local acceptance/harness freeze; no run/new Q01 coverage. Owner resumes Local/GPT 13-minute heartbeat, Cloud quiet, self-halting allowed.

- **L845 to L846 (Local, 2026-10-24):** the sixteen-tail hypothesis withdrawn as the kit's lane construction (light cone plus left-permutivity, exhaustive at width 16; PRIOR-ART, section 8.51); W6 and W42 receipt fields quoted; notebook build 1 of the width-60 essay a dry run (2,120.8 s, ten output cells as predicted); W44 MEASURED, D(44) = 78 with the same twelve 41-bit starts as width 42; build 2 on the corrected essay requested.

- **L853 (Local, 2026-10-24):** D5 MEASURED under the accepted stage (8 s, every control passed): the predeclared rule returned SURVIVES at the boundary exactly (R = 0.5 at widths 30 to 36), but the statistic is floor-sensitive (a measured fraction near one half of the lanes dies at the first level beyond the cone; not a theorem for this population, GC1769), and the record prefixes have the largest spreads (2 to 5 of 16 completions attain), reversing L850's one-width reading; the hypothesis is not claimed. d5_spread.py OUTCOME.

- CL609 task 4 review: reports/wolfram-agents/GPT-CL609-TASK4-REVIEW.md (GC1772/MI714). Hand derivation D(W)=W+maximum forced-row white run after W when D(W) finite; scoped flux/strict-moving-edge obstruction, independent read pending. Not a general local-ranking impossibility or Q01 proof; Farkas-to-physical-cycle claim corrected. No computation.

- **L858 to L859 (Local, 2026-10-24):** submission 14, the width-60 complete certificate, SUBMITTED as R30-20261024-71f858 after the plain build on the owner's word (Cloud's clarification of the two-party rule's scope: research launches, not submission builds) and the full-cell gate (one per-session identifier normalised, proven the only difference); queued for the verifier.

- **L860 (Local, 2026-10-24):** submission 14 (R30-20261024-71f858) FAILED the verifier, out of the sandbox's memory: the first measurement of the sandbox's limit (between about 2 and 4 GiB by our per-module numbers); D(60) = 114 stands; the lane is a certificate that fits (several modules in one notebook, or larger chunks).

- **L863 (Local, 2026-10-24):** P1 built and passed: the exact lane engine on the M5's GPU (tests/probes/wolfram/p1_engine/, p1_lane_engine.py), 57 of 57 controls, the drop-edge mutant detected, 16.8 M width-60 lanes equal to d1's exact levels; GPU kernels 7x one CPU process, end to end 2x (CPU reduction dominates); next: GPU reduction, then a W=64 census as an independent check of D(64)=116.

- **L864 (Local, 2026-10-24):** P1 revision 2: GPU-side reduction; 71 of 71 controls (new: GPU reduction = CPU reduction); engine 79 M width-60 lanes/s end to end, 3.5x d1 on all ten cores; P1b proposed (a W=64 GPU census as an independent check of D(64)=116).

- **L865 (Local, 2026-10-24):** P1b passed: the GPU census at W=64 (2^32 lanes, none censored) confirms D(64) = 116 independently of the CPU census, attained by exactly 40 lanes (chunk 10686, lanes 42,688-42,727), each validated, d1 agreeing lane for lane; 65 s. D(66..72) by GPU census proposed.

- **L866 (Local, 2026-10-24, solo on the owner's word):** D(66) = 120 (112 maximizers, one chunk) and D(68) = 122 (32 maximizers, one chunk) by complete GPU census (p1c_census.py; numerical; gate and maximizer chunks checked by d1 lane for lane; carried witnesses and monotonicity); W70 and W72 running.

- GPU P1r3/P1b/P1c source review and next-block advice: GC1780, reports/wolfram-agents/GPT-P1C-FOLLOWUP-REVIEW.md. Known-answer hard-stop/prefix-scoring corrections; selected d1 chunks independently upper-bounded, not all lower levels compared. Raw receipt review pending; no rerun/new job agreement.
- Kit EdgeObservable task5 source/mathematical reading: GC1780/MI715, reports/wolfram-agents/GPT-EDGE-OBSERVABLE-REVIEW.md. Standard common-right-half permutivity corollary; general conjecture OPEN, fixed-diagonal/two-column gaps explicit. E1 finite test DESIGN only, parked/unexecuted.

- **L868 (Local, 2026-10-24):** D(70) = 124 (156 maximizers, 3 chunks) and D(72) = 130 (252, 3 chunks) by complete GPU census, numerical; the P1 receipt packet published (cited/p1-packet/); the lower-bound submission d-lower-64-72 prepared and checker-passed (D(64..72) >= 116, 120, 122, 124, 130).

- GC1782/MI716: `reports/wolfram-agents/GPT-L868-L870-CL618-REVIEW.md` carries the five W64–72 lower-bound sources, closes the selected GPU byte audit, and reviews P2/E1 designs. Notebook axiom gate false acceptance; E1 control-roll-up omission; P2 beam/batch budget mismatch. No replay/new launch; exact notebook output and E1 result reads pending.

- **L874 (Local, 2026-10-24):** submission 15, R30-20261024-b16332: kernel-checked death-time lower bounds D(64..72) >= 116, 120, 122, 124, 130 (witnesses from the GPU census), after GPT's source and output sign-off (GC1782, GC1784); gate revision 4.

- **L875 (Local, 2026-10-24):** submission 15 (R30-20261024-b16332) Lean Verified; S0 revised for GC1785 (driver revision 5: strict input, bounded line reader, indices cap; frozen client harness s0_serve_controls.py; a blocking-read deadlock found and fixed); development dry run 27/27; S0 stage awaiting GPT.
- **L877-L885 (Local, 2026-10-24):** S0 revision 2 stage PASSED (L878, GC1788/GC1789); the P2 latency pilot PASSED (L883: about 1.4 ms per small GPU request); P2 production PASSED its 50-case gate (L885): D(64) found once (shallow-first beam), D(72) not found, no shown advantage at width 72; maximizers concentrate in few deep-prefix blocks (D5's within-block spread, L853, still stands). Packets in the store: cited/s0-stage-20261024-1548/, cited/p2-pilot-20261024-1626/, cited/p2-stage-20261024-1636/.

- GC1794/MI727: `reports/wolfram-agents/GPT-L885-P2-OUTCOME-AND-PREFIX.md` closes selected P2 evidence audit (50 cases/298614 exchanges); exact prefix-pruning obligation, cheap bound OPEN. No rerun; edge-sep actual notebook outputs pending.
- **L886 (Local, 2026-10-24):** submission 16, R30-20261024-991a71: Cloud's edge-sep (sep_8, sep_13, sep_14 with attainment; GC1793 PASS); the M5 checker equal to Cloud's, full-cell gate nb_gate_edgesep.py PASS; packet in the store at cited/edge-sep-submission/. GC1794: P2 audit PASS; no cheap prefix bound known (exact certificate condition stated). Next lane: the width-74 census (about 40 min, ESTIMATE).

- GC1795/MI728: `reports/wolfram-agents/GPT-L886-OUTPUT-AND-L887-W74-REVIEW.md` closes submission 16 actual-output review PASS; one exact L887 W74 census accepted, not yet launched. Bounds/resources/source checked, no duplicate compute.

- GC1796/MI729: `reports/wolfram-agents/GPT-CL623-EXTERNAL-PREFIX-REVIEW.md` scopes nine-word Psi restrictions, initial channel transients,48/128 parametric overlap and conditional Sparse16 weight prune; general deep-prefix bound OPEN, no replay.

- GC1797/MI730: `reports/wolfram-agents/GPT-LOWER74-PREPARATION-REVIEW.md` carries reused lower-bound generator architecture; census-write completeness and range-rounding corrections; final witness/actual outputs pending, no replay.
- **L889 (Local, 2026-10-24):** D(74) = 134 by complete GPU census (numerical; 178 maximizers, 2 blocks; store cited/p1c-W74-20261024-1726/); the width-74 lower-bound submission ready (d6_lower74_submission.py revision 2, nb_gate_lower74.py; store cited/d-lower-74-submission/); the width-76 census proposed (p1c_census.py revision 4).

- GC1800/MI733: `GPT-L889-W74-LOWER74-W76-REVIEW.md` closes selected W74 numerical134/178 evidence and lower74 actual-output reviews PASS; one exact W76 stage accepted, launch unreported. No kernel upper certificate or duplicate run.

- GC1801/MI734: `GPT-L891-PARAMETRIC-LOWER-REVIEW.md` carries W76 preparation source; fixed400 diagnostic limits wider reuse, final evidence pending. L890 submission17 submitted/queued and accepted W76 launched, reported; no new job.

- GC1803/MI736: `GPT-L892-W8-REVIEW.md` carries N20 chunk coverage and accepts one exact W8 local build/check stage after W76 work. Not launched; sandbox fit unproved, final evidence pending.

- GC1804/MI737: `GPT-CL624-NESTING-CQ01.md` scopes D8 nesting and specifies exact finite-support versus relaxed CQ01 word languages; hand horizon-2n gluing argument, endpoint control. Independent implementation read pending; no new launch, W78 held.

- GC1805/MI738: D8 revision 2 source repairs PASS, four literal controls; upper-median convention and all-six-step coverage qualified. Exact retained-input invocation/caps pending; no production run. `GPT-CL624-NESTING-CQ01.md` addendum.

- GC1806/MI739: D8 revision 3 stage read; six-step/caps present, missing/wrong output digest falsely accepted and split parse/hash reads exposed by file fixtures. Binding repair/frozen manifest pending; no production run. `GPT-CL624-NESTING-CQ01.md`.

- GC1807/MI740: D8 revision4 source/design PASS; exact digest and single-buffer repairs close,11+7 file controls pass. Frozen seven-file manifest pending, no production acceptance/run. `GPT-CL624-NESTING-CQ01.md`.

- GC1808/MI741: W76 selected retained-evidence PASS,numerical138/64;1550 checks/512 ranges verified, no replay/kernel upper certificate. Three blocks but zero common high bits; final submission/D8 manifest pending. `GPT-W76-OUTCOME-REVIEW.md`.
- **L895 (Local, 2026-10-24):** D(76) = 138 by complete GPU census (store cited/p1c-W76-20261024-1821/); the width-76 lower bound ready (cited/d-lower-76-submission/); D8 manifest frozen (cited/d8-manifest/); W8 (N = 20 width-60 form) stopped on memory, route (b) NEGATIVE (cited/w8-n20-20261024-1949/).

- GC1809/MI742: lower76 final source/eleven-output PASS; ONE exact D8 manifest-bound stage accepted. W8 negative memory-cap attempt reviewed, cleanup incomplete/no retry. `GPT-L895-FINAL-D8-W8-REVIEW.md`.

- GC1810/MI743: D8 six-step retained-output review PASS; k>=8 disjoint at all6 transitions, k4 partial overlap at2. Stage consumed; no general prefix law/pruning certificate. `GPT-L896-D8-OUTCOME-REVIEW.md`.


- GC1811/MI744 adopts L898: finite CQ01 J characterization HAND/PROVED by independent read; n* extended supremum/pair units/censoring clarified. Executable proposal pending; `GPT-CL624-NESTING-CQ01.md`.


- GC1812/MI745: L899 CQ01 E/scalar source semantics PASS; stage mutation/gate/censoring repairs required, demonstrated by file fixtures. No launch; `GPT-L899-CQ01-DESIGN-REVIEW.md`.


- GC1813/MI746: L900 CQ01 revision2 gate read; ten fixtures pass, seven new failures expose schema/lane-index defects. Launch unaccepted; whole-schema repair next, `GPT-L899-CQ01-DESIGN-REVIEW.md`.


- GC1814/MI747: L901 CQ01 revision3 schema/source PASS,21+9 file controls; ONE exact stage80/20/400 accepted, launch/outcome pending. `GPT-L899-CQ01-DESIGN-REVIEW.md`.
- **L898-L902 (Local, 2026-10-24):** the CQ01 census (job 2): GC1804's finite specification carried (L898); cq01_census.py revisions 1-3 through GC1812-GC1814 (one ordered result schema); E(L, B) for L <= 80, B <= 20 complete, E(L, B) - L <= 17 (store cited/cq01-census-20261024-2031/).
- **L903-L904 (Local, 2026-10-24):** the CQ01 census at larger L: cq01_census.py revision 4 (scope only; GC1816), E(L, B) for L <= 400, B <= 16, K = 800 complete, E(L, B) - L <= 22, E(400, 16) = 417; Psi ∅ black density 0.569 with geometric white runs (store cited/cq01-census-20261024-2041/).
- **L905-L907 (Local, 2026-10-24):** the CQ01 per-R statistics: cq01_per_r_stats.py revisions 1-4 through GC1817-GC1819 (GPT's exact run-avoidance and finite-window gap references, a strict finite gate); B = 16, K = 800: ensemble density 0.5025, per-R 0.34-0.86; mean longest window run matches the iid reference; R -> Psi R 1..800 has 31,478 distinct prefixes of 65,536 (store cited/cq01-per-r-20261024-2125/).
- **L908-L910 (Local, 2026-10-24):** the CQ01 collision structure: cq01_collisions.py revisions 1-2 through GC1820-GC1822; the collisions are right-end moves ('...01' ~ '...011', '...11' ~ '...101', the wall black), exact for B' <= 8 at depth 800; the move lemma, Psi R unchanged by them (PROOFS.md waiting room L910); f_p rises with distance from the wall (store cited/cq01-collisions-20261024-2157/).
- **L911-L913 (Local, 2026-10-24):** the CQ01 kernel test: L910's negative-control claim corrected (L911); cq01_kernel.py revisions 1-2 through GC1823-GC1824 (move lemma HAND/PROVED); depths 800/1,600/3,200: extra merges 1,291/949/908, 82 persistent groups (smallest 11111 vs 111101111), none a delayed move within 600 steps (store cited/cq01-kernel-20261024-2224/).
- **L914-L919 (Local, 2026-10-24):** the CQ01 deep-time rows (cq01_deeptime.py revisions 1-2, GC1825-GC1826): 81 of 82 persistent groups hold through 20,000 visible bits; GC1825 corollary (move classes never merge, HAND/PROVED, carried L916); L910's moves are the kit's tail_011/tail_101 (prior art); **the second mechanism is the kit's ether-and-wall trap**: Psi 11111 = Psi 111101111 and CQ01 for R = 11111 by a trap certificate (PROOFS.md waiting room L919; store cited/cq01-deeptime-20261024-2255/).
- **L920-L925 (Local, 2026-10-24):** the trap census proposed and withdrawn (L920-L921, GC1829); the pair in Lean, submission trap-pair (reports/wolfram-agents/submissions/trap-pair/): source PASS GC1831, essay PASS GC1832, the kit's Check PASS (trap_pair_check.py, GC1833; 66 constants; store cited/trap-pair-check-20261024-2333/).

- GC1815/MI748: L902 CQ01 actual1701-row/control/terminal audit PASS; numerical E(80,20)=93,max E-L17,stage consumed. Bounded gaps conjecture unproved; no wider acceptance. `GPT-L902-CQ01-OUTCOME-REVIEW.md`.

- GC1816/MI749: L903 scope-delta/source review PASS; ONE exact400/16/800 CQ01 stage at793f12b0 accepted under unchanged caps; launch/outcome pending. `GPT-L902-CQ01-OUTCOME-REVIEW.md` addendum.

- GC1817/MI750: L904 larger-L CQ016817-row/1377-overlap/terminal audit PASS; E400,16=417,max E-L22,stage consumed. Individual geometric gap differs from finite longest-run law; per-R proposal pending. `GPT-L904-CQ01-LARGE-OUTCOME.md`.

- GC1818/MI751: L905 per-R source review COMPLETE WITH CORRECTIONS; window/recurrence carries, NaN gate hole and finite-prefix/pooled-gap qualifications. No launch acceptance; `GPT-L905-PER-R-REVIEW.md`.

- GC1819/MI752: L906 per-R revision4 repairs PASS;72 gate fixtures/45 added nonfinite mutations; ONE exact16/800 stage accepted, launch unreported/outcome pending. `GPT-L905-PER-R-REVIEW.md` addendum.

- GC1820/MI753: L907 per-R five-file outcome review PASS;density.502518,31478 prefixes at800;stage consumed. Kit first-difference bridge gives400 visible bits exactly;collision design pending. `GPT-L907-PER-R-OUTCOME.md`.

- GC1821/MI754: L908 collision source reviewed; five whole-line coverage false passes, launch unaccepted. Boundary-front versus visible-bit distinction and exact half-at-depth2 controls; repaired source pending. `GPT-L908-COLLISION-REVIEW.md`.

- GC1822/MI755: L909 collision revision2 repairs PASS;57 file fixtures/12 stage cases,ONE16/800 stage accepted. Launch unreported,retained outcome pending. `GPT-L908-COLLISION-REVIEW.md` addendum.

- GC1823/MI756: L910 move lemma/noninjectivity HAND/PROVED; nine-file outcome PASS, stage consumed. L911 gate accepts false move refinement; exact repair pending, no launch. `GPT-L910-L911-REVIEW.md`.

- GC1824/MI757: L912 kernel revision2 repairs PASS;34 file fixtures/6 stage cases, full old-partition digest checked. ONE16/800/1600/3200 stage accepted; outcome pending. `GPT-L910-L911-REVIEW.md` addendum.

- GC1825/MI758: L913 kernel outcome PASS,196608 labels/82 groups/990 representatives; stage consumed. L914 earlier-prefix binding missing; no launch. Hand commutation/injectivity excludes delayed move equivalence at width>=2 (independent read pending); L915 finite barrier remains unproved. `GPT-L913-L915-REVIEW.md`.

- GC1826/MI759: L916 no-delayed-move corollary HAND/PROVED adopted; L917 revision2 PASS/ONE40000-step stage accepted. Period4 one-cycle guard fails hand lane543; permanent pair equality OPEN. L918 visible move consequence already covered by kit tail_011_drv/tail_101_drv; reuse prior source. `GPT-L913-L915-REVIEW.md` section5.

- GC1827/MI760: pinned TerminalClock linked_diagonal plus equal head-OR gives L918 moving-edge row induction by reuse; width1 needs separate black-wall branch. Nonmerging absent from these two read modules, global novelty unassessed. Source review only, `GPT-L913-L915-REVIEW.md` section6.

- GC1828/MI761: L919 two-row trap composition HAND/PROVED; u31=u495=0101… though not move-equivalent, two CQ01 instances. Actual deep-time outcome PASS:81/82 groups persist finitely; one split at1677, permission consumed. `GPT-L919-TRAP-AND-OUTCOME.md`; general CQ01/novelty open, exact formal source pending.

- GC1829/MI762: L920 trap-census source semantics carry; entry witnesses/known-entry and old-trace bindings missing, four false gate passes. L921 withdraws stage; exact pair Lean source/check plan pending, no launch; `GPT-L920-TRAP-REVIEW.md`.

- GC1830/MI763: common Psi31=Psi495=etherLeft3, positive-depth1011111, known-kit hand application/uncompiled. All-driver completeness remains distinct; approved audit files retained/readback verified. `GPT-L919-TRAP-AND-OUTCOME.md` section4.

- GC1831/MI764: L922 trap-pair Lean source27f799f4 PASS including EqvGen non-move statement; pipeline dependencies compared. Check stage cap/restoration wrapper pending, no compile/launch; `GPT-L922-PAIR-SOURCE-REVIEW.md`.

- GC1832/MI765: L923 essay/abstract/helper source and exact inline-Lean assembly PASS; actual outputs/gate pending. No launch/compile; `GPT-L922-PAIR-SOURCE-REVIEW.md` addendum.

- GC1833/MI766: L924 exact trap-pair Check wrapper d12487a3 PASS,11 file controls; ONE4GiB/1200s stage accepted. No launch observed/output yet; `GPT-L924-CHECK-WRAPPER-REVIEW.md`.

- GC1834/MI767: L925 four-file actual Check/resource/restoration outcome PASS; five headlines/66 constants, local formal pair result adopted. Permission consumed, notebook/gate pending; `GPT-L925-CHECK-OUTCOME-REVIEW.md`.

- GC1835/MI768: L926 notebook wrapper full read/14 file controls; input admission/final script binding/Wolfram scope repairs required. No acceptance, exact revision pending; `GPT-L926-NOTEBOOK-REVIEW.md`.

- GC1836/MI769: agreement withR31 on1..28 orR495 on1..24 forces common Psi etherLeft3 for arbitrary tails; hand locality/trap corollary, uncompiled. `GPT-L919-TRAP-AND-OUTCOME.md` section5; no wider-census classification.

- GC1837/MI770: L927 bindings/count repairs PASS/27 controls; monitor-error ignored, watcher may outlive step, failure inventory missing. No notebook acceptance; `GPT-L926-NOTEBOOK-REVIEW.md` revision2 addendum.

- GC1838/MI771: L928 live monitor repairs PASS; GPT terminal-inventory completion fix50eaa2ed, ONE capped notebook stage agreed after Local adoption. No compute/output yet; `GPT-L928-NOTEBOOK-AGREEMENT.md`.

- GC1839/MI772: CL628 owner exception adopted; notebook goes through authorized plain pipeline, supervisor3a parked. Actual cell/gate review pending; no supervisor agreement prerequisite or Intel build.

- GC1840/MI773: CL629 bare-pair hold adopted; exact prefix-family statements and uncompiled FamilyExtension.lean proof candidate supplied. Await Local elaboration/new Check/cells/gate; no generalCQ01 or all-width bound. `GPT-CL629-FAMILY-STATEMENT.md`.

- GC1841/MI774: L930283-line family source49218116 PASS; exact inclusive hypotheses, finite injective fam and seven Check headlines agreed. Actual Check/notebook outputs pending; `GPT-L930-FAMILY-SOURCE-REVIEW.md`.

- GC1842/MI775: L931 b0113490 family interface delta PASS/eight Check headlines agreed; essay15df19fb exact source assembly PASS, ten outputs expected. Actual Check/gate/cells pending; `GPT-L930-FAMILY-SOURCE-REVIEW.md` addendum.

- GC1843/MI776: L932 Check-tool pin delta3c086cfc PASS/11 controls; ONE b0113490/eight-headline invocation agreed at existing envelope. Actual output pending; `GPT-L930-FAMILY-SOURCE-REVIEW.md` addendum.

- GC1844/MI777: family gate exact-cell inventory repaired after cell12 false pass;32 literal-oracle controls PASS. L933 ONE exact replacement Check agreed after PATH preflight; actual evidence pending. `GPT-FAMILIES-GATE-REVIEW.md`.

- GC1845/MI778: CL561 bounded-ratio carrying read PASS in conditional unrefereed-source scope; routing/scale/repair checked, general similarity prize/novelty open. `reports/GPT-CL561-BOUNDED-RATIO-REVIEW.md`.

- GC1846/MI779: L934 cap-only2a858a4e source PASS; ONE6GiB family Check agreed subject fresh quiet total headroom.4GiB failure/no verdict Local-reported, raw cleanup/outcome pending. `GPT-L930-FAMILY-SOURCE-REVIEW.md`.

- L935: the trap-families submission R30-20261024-8d7751 (2026-10-25 00:44 BST): GC1836's two infinite families of CQ01 instances (AgreesPrefix 28 R R31, AgreesPrefix 24 R R495, any later tail; the explicit finite family fam n) in module b0113490, kit Check PASS (replay 106, declared 57, eight headlines on the standard axioms), the plain build and the full-cell gate PASS (54 controls); the bare pair held (CL629). `reports/wolfram-agents/submissions/trap-families/`, `tests/probes/wolfram/trap_families_check.py`, `reports/wolfram-agents/pipeline/nb_gate_trapfamilies.py`.

- GC1847/MI780: L935 actual family Check/ten-cell review COMPLETE/PASS,12 payload hashes/54 file controls;106 replay/57 declared/eight headlines. Resources/failures qualified; external8d7751 Lean Verified Local-reported. `GPT-L935-FAMILY-OUTCOME-REVIEW.md`.

- GC1848/MI781: exact finite survival-through2h/Level(W,h) interface and endpoint control checked by hand; known-source reformulation, no universalD(W) bound. Submitted R cylinders map to one free sequence. `GPT-CL609-TASK4-REVIEW.md` section6.

- GC1849/MI782: backward white-block five-template description checked; closure underG-preimages refuted by known011->111 bulk control. Source/hand,not eternalTheta/universalD result;candidate stopped. `GPT-CL609-TASK4-REVIEW.md` section7.

- GC1850/MI783: fixedH black-history motif exclusion refuted by known completion forK>H+1;not eternalTheta/depth-coupled claim. Local-template approach incubated,no schedule pause. `GPT-CL609-TASK4-REVIEW.md` section8.

- GC1851/MI784: direct public check objects close74/76/family external-status reviews;new0554f7 entire source scoped PASS,consecutive black-run3/5/conditional white/log count. No all-widthD transfer;d1bcba evaluating/source absent. `GPT-PUBLIC-STATUS-AND-FIFTHS-REVIEW.md`.

- GC1852/MI785: d1bcba completedcheck/source read;oldbody byte-exact,newdiagonal appendix scoped PASS,linear/conditional bounds only. Sublinear/O(1) prose unproved;no universalD transfer,pendingreview closed. `GPT-D1BCBA-DIAGONAL-REVIEW.md`.

- GC1853/MI786: kit3eca backward-vacuum/endpoint/restricted tube carrying source scopedPASS;physical earlywhite via shield/locality/Jen,not universalcertificateexistence orallwidthD. Eightfullsources1430lines,MAP8coverage;`GPT-3ECA-BACKWARD-CERTIFICATES.md`.


- GC1854/MI787: kit3eca StripeMeeting full proof/certificate semantics scoped PASS; arbitrary-length/actual-row bridge, two-step trace preservation, conditional early meeting. Entry/classification/Psi-D transfer unproved; literal pool audit only, no replay. `GPT-STRIPE-MEETING-REVIEW.md`.


- GC1855/MI788: kit3eca XorRigidity full326-line carrying source scoped PASS; exact whole-line XOR classification via distance induction/cuts/shear. Hand half-line site0 exception blocks boundary-driven transfer; no replay/D bound. `GPT-XOR-RIGIDITY-REVIEW.md`.


- GC1856/MI789: kit3eca period-three finite/white-tail erosion988-line carrying source scoped PASS; bounded defect witness, arbitrary-width robust-wall exclusion. Hand bad-state/far-bit controls; no replay/general period3/CQ01-D transfer. `GPT-PERIOD-THREE-EROSION-REVIEW.md`.


- GC1857/MI790: kit3eca uniform white-padding wrappers/certificate semantic bundle scoped PASS; exact A-E left-finite families, endpoint-inclusive pumping, Heavy commonN49.156 literal masks/file bindings only,no replay/universal-tail/CQ01-D deadline. `GPT-UNIFORM-PADDING-REVIEW.md`.


- GC1858/MI791: SparsePreimage78-line source scoped PASS; listed SOURCE states/exact mask binding, restricted implication only. Hand target-list countercontrol; no replay/global predecessor result. `GPT-3ECA-BACKWARD-CERTIFICATES.md` addendum.


- GC1859/MI792: rotation/short<=4,r49 carrying source PASS; five/six69/77 reductions conditional/imported core scope, new core closures unreviewed. Exact r+a+b preserves period; no replay/D deadline. `GPT-TAIL-ROTATION-REVIEW.md`.


- GC1860/MI793: actual eight five-tail core proofs source-scoped PASS; length<=5/r69 uniform theorem now carried, endpoint OR last8/widthK-1 checked.123 literal masks/three exact source-list bindings, no replay/D deadline; six-tail cores unread. `GPT-FIVE-CORE-REVIEW.md`.


- GC1861/MI794: all16 six-tail cores/two endpoint refinements source-scoped PASS; uniform length<=6/r74 carries, exact end-window/inclusive prefix/rotation checked.2018 new lines/13 fixed payloads, no replay/deadline/D transfer. `GPT-SIX-CORE-REVIEW.md`.


- GC1862/MI795: arbitrary-prefix suffix families source PASS at10|v|+41/71; padded-word catalogue sufficient, not optimal (raw011 control). Seven full sources1523lines/12 fixed payloads; small8/9 seed scope, no replay/D deadline. `GPT-SUFFIX-FAMILIES-REVIEW.md`.


- GC1863/MI796: CenterRuns full531-line source PASS; inclusive white-window/exclusive count and strict edge-passage guards carry via hand controls. No new D bridge/replay;4 fixed payloads, trajectory incubation retained. `GPT-PUBLIC-STATUS-AND-FIFTHS-REVIEW.md` section6.


- GC1864/MI797: new 5105a7 single-sequence Problem 2 iff source PASS, 586 lines byte-equal predecessor; Lipschitz sandwich/official bridge carry. Additive-gap helper label qualified; no density/D(W) proof or replay. `GPT-P2-SINGLE-SEQUENCE-REVIEW.md`.


- GC1865/MI798: new bcf514 cut-rank middle equivalence source PASS, 589 lines; ceiling-log rank, both odd middle cuts and n>=2 essential. Generic word reduction, no center-rank/Problem3/D(W) proof or replay. `GPT-CUT-RANK-MIDDLE-REVIEW.md`.


- GC1867/MI799: CL631 source/hand review COMPLETE; D(2)=6 refutes strict all-width2W, early fresh-pivot counts exact/late hazard heuristic. Centre-run transfer lacks premises; finite suffix-risk baselines standard, unrun. `GPT-CL631-COUNTING-AND-TRANSFER.md`.


- GC1868/MI800: seven-kind certificate inventory source review COMPLETE WITH CORRECTIONS; rank counters, trap transients, distinct padding and coverage/positivity contracts. Typed ML labels, no evaluator/launch; `GPT-CERTIFICATE-INVENTORY-REVIEW.md`.


- GC1869/MI801: CL632 source/11 retained arrays8..48 audited numerically; W40 opposite-label pairs defeat exact low/high10 sufficiency. Manifest/timing qualified,52 evidence pending. L938 curve from retained histograms: W40 N70=71 vs32, W48 extinction88 vs16; no evolution/ML, `GPT-CL632-DEATH-TABLES-REVIEW.md`.


- GC1870/MI802: L940639-line finite information-loss source carries; nine literal JSON fixtures expose seven gate false passes. Exact schema/roll-up/permutation/zero-consistency/metadata repairs required; no launch or evolution. `GPT-L940-INFORMATION-LOSS-REVIEW.md`.


- GC1871/MI803: CL633 width52 all67108864 retained values and five part/full hashes PASS,96/10/0; manifest repaired, both pending gaps closed. No evolution/sealed bit-label analysis; L940 repair pending. `GPT-CL632-DEATH-TABLES-REVIEW.md` addendum.


- GC1872/MI804: L941 revision2 source/control PASS; ONE exact W8..40 stage accepted, actual outcome pending. W12 pair is old support11/death30 pair; universal2W+6 fails, prefix pump already closed. Two review addenda, no evolution.
- L942: the exact free-bit information-loss stage (death_info_loss.py e756613b, GC1872; 2026-10-25 09:40 GMT): W = 8..40, replay 8/12/16 agrees lane by lane; early end bits near the permutation line (not equality; GC1873), flipping the last free bit a(W - 1) (start cell W alone) leaves death nearly uncorrelated (pair correlation +0.001 at W = 40), the first barely matters (0.985), late half R^2 0.011 at W = 40; the rare label A concentrated by the latest bits (66 of 1,024 classes). P3-P6 held, P1, P2, P7 (first half), P8 failed. `cited/death-info-loss-20261025-0941/`.


- GC1873/MI805: L942 five-file outcome PASS,468 retained rows/exact scores; stage consumed. Late10 rare-survivor15.515x in-sample enrichment; coin/initial-cell interpretations qualified, no new run. `GPT-L942-INFORMATION-LOSS-OUTCOME.md`.


- GC1874/MI806: period4 single-cell all-position/phase and stripe-prefix/five-tail sources scoped PASS;120/64 cases32 links, abstract stripe/count repaired. No all-input bound/replay; L943 frozen44/48 design supported only. `GPT-PERIOD4-AND-STRIPE-TAIL-REVIEW.md`.


- GC1875/MI807: L944712-line source mathematics carries; seven literal-file gate false passes require provenance/count/maximizer repairs. Neither phase accepted; exact revision pending, no arrays/replay. `GPT-L944-SURVIVOR-TRANSFER-REVIEW.md`.


- GC1876/MI808: L945 gate repairs PASS/nine file cases; ONE exact two-phase stage accepted, actuals pending. Public81e2c6 cone/reference reduction and8623-entry coverage reviewed; kernel checks unevaluated/pending. `GPT-L944-SURVIVOR-TRANSFER-REVIEW.md` addendum; `GPT-TWO-CELL-PERIOD4-REVIEW.md`.
- L946–L947: the frozen survivor transfer test (survivor_transfer.py 7dccdfd9, GC1876; 2026-10-25 10:44–10:45 GMT): select 28..40 (S40 66 words, S40SHA 0e220713, SELSHA e5831606, committed before 44/48 were fetched), then transfer: W = 44 recall 97/1401 (enrichment 1.074), W = 48 54/625 (1.341), both REJECTED; nesting 1/10, 2/21, 2/43; no maximizer in S40 (W = 44 maximizers one early-bit family in word 158). `cited/survivor-transfer-20261025-1044/`.


- GC1877/MI809: public81e2c6 external compilation FAIL before replay, complete receipt read; cause unspecified, corrected source/check pending. Structural review unchanged; `GPT-TWO-CELL-PERIOD4-REVIEW.md` addendum.

- GC1877/MI809: L947 actual11-file source/hash/count/terminal review PASS;44/48 frozen transfer REJECTED,0/44 maximizers, modest enrichment1.074/1.341 retained. Both phases consumed,52sealed; `GPT-L944-SURVIVOR-TRANSFER-REVIEW.md` outcome addendum.


- GC1878/MI810: public dacb3e/a02087 complete source/external-check PASS,119/117 constants; white1..30 allows arbitrary tails, entry14-(phase mod4). No all-position repair/coverage/D deadline; `GPT-TWO-CELL-PERIOD4-REVIEW.md` addendum.

- GC1882/MI814: owner-requested 37-paper/45-discussion Collatz appraisal complete; paper37 pointwise count comparison motivates UNPROVED Rule30 finite-counterexample amplification beyond known 2^floor(B/2) trace cap. Direct inverse-time transfer fails; Q3/G5 prior matrix route recognized. `reports/rstation/GPT-COLLATZ-TO-RULE30-APPRAISAL-20261025.md`; no post/run/restart/status promotion.
- CL637 (Cloud): GC1882's amplification lead given its shape: a finitely checked amplification is a death-time bound (Lemma A, PROOF-SKETCH, single-party); the census says it must double width or horizon (calibration, MEASURED); the zero-boundary half has no hidden multiplicity, and the record's OR-side operations (L910 moves, L919 traps, masked driver) multiply right halves only. `reports/rstation/CLOUD-AMPLIFICATION-REPLY-20261025.md`; no run/restart/status promotion.
- CL638 (Cloud): GC1883 reviewed PASS; CL637's 'no hidden multiplicity' withdrawn for the even-time trace (GC693 fixture holds with a white wall, replayed); calibration softened to the product; sharpening: the guarded backward G-tree of an eternal survivor has at most two branches per generation and lies inside W_W, so Lemma A caps it at 2^floor(W/2) (exactly critical). Lead parked.
- CL640 (Cloud, 2026-10-29): the portal's statements as one picture (`reports/wolfram-agents/SYNTHESIS-20261029.md`: three frames, two mechanisms, F = Phi >> 1, the five half-rate counts, alternation as the rigid structure, the capacity gap between the channel bound and the {3,5}-gap trap); four candidate statements with kill tests (doubling density 1/2, CONJECTURE with measured support; forbidden gap words, to compute; rain the only periodic orbit of T, restating H and N; Problem 1 as lock-for-every-driver plus Q01); the appraisal `APPRAISAL-20261029.md`; DQ-024. MEASURED: J_k to k = 35 (`tests/probes/wolfram/edge_gaps.out`).
- CL641 (Cloud, 2026-10-29): review of GC2150 to GC2158 PASS. DQ-024's exact forms: N_0(n) - N_2(n) = o(n) (accounting, GPT) and Hausdorff dimension one half of the edge orbit closure (GC2157, PROOF-SKETCH). J_40 = 92 from Rowland 2006 (prediction 12 +- 2 HELD at 13); Cloud's own run to k = 38 agrees with the table. Six corrections to the synthesis applied (left/right reversed; arc hypothesis; width 16 unpublished; intersection not inclusion; finite data cannot kill a limit; connection not theorem).
- CL642 (Cloud, 2026-10-29): DQ-024 mechanism: d_j = weight parity of R_(j-1) OR R_(j-2) (kit S_rule) reduces by hand to Case A (after a doubling: weight parity of R_(j-2); two doublings give an even quarter-period weight, no_three), Case B (omega_(j-1) + omega_(j-2) + overlap parity) and omega of a non-doubling diagonal = even-time black count of its input; PROOF-SKETCH, COMPUTED exact to j = 56 (`tests/probes/wolfram/edge_diag_rules.out`). Fair unforced parities give density 3/7 = 0.4286 (CONJECTURE, competing with 1/2); MEASURED 0.42 to j = 92 with conditional frequencies 0.44, 0.63, 0.37. Part 2: pooled over 64 random seeds (block exponents, n = 13..56) the density is 0.407 +- 0.009 with per-seed spread below binomial; after 101 the next doubling occurs in 0.135 of cases and never after 1011 (the 101 shift law and GC2007 in action); the one-half conjecture withdrawn as favoured value; the limit near 0.41, MEASURED.
- CL643 (Cloud, 2026-10-29): GC2164 accepted: CL642's sentences on the limit (near 0.40, not 3/7 or 1/2, half-rate not sharp) withdrawn as claims; finite pooled prefixes cannot settle the asymptotic rate; 0101... obeys both hard zeros at density one half. DQ-024 OPEN, model values heuristics. The mechanism line continues two-party (GC2195 to GC2199, L1194 to L1199).
- CL645 (Cloud, 2026-10-29): forced letters after a double doubling (PROOF-SKETCH): with M = Q_b after x_(b-1) = x_b = 1, every alternating run (10)^m 1 from b is followed by 1 iff m = M/4 - 1 (from GC2197's mask and the antiperiodic order H/2 - 1); exact on the single seed and 64 seeds (297 runs); covers 69 per cent of 101 occurrences; free letters only after 00, measured fair; six-state skeleton density 2/5 (heuristic, model value). DQ-024 OPEN.
- CL648 (Cloud, 2026-10-30): GPT's overnight run assessed. DQ-024: CL645's corollary two-party (GC2205); exceptional ruler closures have zero density (sketch); the edge orbit closure has Assouad dimension at most 1/2 (GC2220, sketch); the closing law alone permits unbounded critical excess (GC2221), so a lower bound must use the 00 transition; the edge map has no 2-adic derivative (GC2212). Synthesis 3.5/5.2 corrected: forbidden gap words are prior art (L590, GC1009, L627). Free-partner theory GC2243 to GC2247 (solo). About fifteen solo sketches await reads.

- GC1883/MI815: independent CL637 review; LemmaA carries, full-trace injectivity does not forbid even-trace finite left branching (GC693 zero-wall hand audit); GC694 right cylinders disjoint. No finite-branch abundance mechanism; finite census does not require doubling. Full-line G121 root proportion kept separate. `reports/rstation/GPT-CL637-AMPLIFICATION-REVIEW.md`; no run/restart/status promotion.

- GC1884/MI816: live18:59Z portal41entries; new01554c is a comment-only proof replacement. Kit009005 adds generic front projection/period/return-map lift and known four-tail completion; all883 new lines source-read, recurrence without white witnesses fails a hand width2 control. `reports/wolfram-agents/GPT-PORTAL-UPDATE-20261025-EVENING.md`; no all-width breakthrough/run/restart.

- GC1885: owner-requested [DEEP-QUESTIONS.md](DEEP-QUESTIONS.md) tracks seven foundational questions in everyday language, their mathematical scope, known obstacles and reopening conditions. DQ-001 preserves the selected question about changing a hypothetical exception without destroying its defining behaviour. Question tracker only; no new claim, run or schedule restart.

- GC1886/MI817: owner-requested L950/DQ-008 source/hand investigation recovers 8.84's known age-one obstruction: the watched sample changes diagonal each step and sees each one a step after boundary birth. Trace-bit changes are not symmetric physical-end perturbations. [First-birthday note](reports/rule30-deep-questions-first-birthday.md); DQ-005 clarified as a visual-return analogy. No new theorem, simulation or restart.

- GC1887: DEEP-QUESTIONS.md DQ-010 preserves the owner's collision question. Existing zero-wall GC693 merger contrasted with full-line finite injectivity G121; simpler survival-preserving representatives remain an open DQ-001 connection. Words/source review only, no new result or run.

- GC1888: owner-requested words-first handoff to Local at the top of DEEP-QUESTIONS.md. Captures antenna/looping, retired fuse analogy, past/present/future, collision-to-compression and eight-streets coverage questions; DQ-004 clarified, DQ-011 asks whether survival spends, preserves or renews its conditions. No new mathematical claim or run.

- L950–L952: Local's three words-first rounds in [DEEP-QUESTIONS.md](DEEP-QUESTIONS.md). L951 gives the near-wall switch restatement (DQ-008) and DQ-009. L952 shows doors settled by checking are deathbeds, so coverage by checking is a deadline (DQ-004). It also gives in-step meetings via Condrey's wall form (DQ-010), the free chapter and no shield beside the wall (DQ-011), and DQ-012 (forced surplus). Hand reasoning only; no new theorem, run or restart.

- L953: the owner's tick-and-tock pull (DEEP-QUESTIONS.md DQ-011). Jen's theorem (section 8.13, Proposition 7), with the white wall as the periodic neighbour, means a survivor's tock (odd-tick colour) is never eventually periodic. The full metronome and black forever are its first two cases. Known results restated; no run.

- GC1889/MI818: [Tick Tock hand note](reports/rule30-tick-tock-hand-analysis.md), targeted Local read pending. Under black even observations, third/fifth depths agree on ticks; their odd discrepancy d drives b_(n+2) = (b_n OR b_(n+1)) XOR d_n. Periodic d implies periodic b, excluded for finite survivors by existing Jen/edge reasoning. No finite-tail constraint on d yet; no general compression obstruction or computation.

- GC1890: DEEP-QUESTIONS.md DQ-013, uneven metronome. Global update retiming versus event coding separated using G98; third/fifth disagreements are isolated and agreement waits odd. Eventual periodicity of waits would imply periodic discrepancy. Hand consequence of GC1889 (carrying algebra still pending independent read), no gap bound or computation.

- L954: Local's hand tock-language notebook ([reports/rule30-tock-language-hand.md](reports/rule30-tock-language-hand.md)). Independent read of GC1889: carries. Cells 7 and 8. The owner's metronome is exact two seats deep: seat 4 misses on black-to-white falls, seat 5 exactly at GPT's d. Proposition 1: a start is its free tock chapter, then universal conducted tocks k_m and checks c_m, so d = NAND(last two) XOR long-memory correction. The two-tock conductor is refuted at k_3. Hand deadlines: width ≤ 5 fails by tick 8. Hand only, single-party; GPT read requested.

- GC1891/MI819: [L954 conductor review](reports/rule30-tock-conductor-review.md) carries cells7–8, conductor/checks and small deadlines; tail discrepancy guard2m+6>W explicit. One bounded Intel audit:256 prefix/32 physical controls pass; fall-only correction REFUTED at admissible0001. Hand F10=1 XOR b4,F11=1 explains width6 failure10; no all-width mechanism or restart. Legacy startups monitoring-blocked, no PASS.

- GC1892/MI820: morning portal has no added IDs/kit change;40 entries, one older ID absent. [Shortening/history note](reports/rule30-tock-shortening-and-history.md): helpful and harmful endpoint deletions explained by hand from retained cases; known triangularity forces depthT+1 for full-history-preserving repair afterT>=W. Non-growing tick-only repair must change an earlier tock; uniform eternal-preserving replacement OPEN, no new run.
- L955: Local's M5 probes, at the owner's word ([reports/rule30-tock-twins.md](reports/rule30-tock-twins.md); tock_twins.c, tock_front.c, tock_gaps_posthoc.c). A start forgets its oldest free tocks exactly (twins identical at tick j+1, never later), by position, not lag (lag prediction REFUTED; 8.38's reading confirmed). The forgotten front moves out about 0.15 tock per tock (W ≤ 48, m ≤ 28; predictions for unseen widths held). The conductor is a coin on all but the oldest tocks. Funnel: 2^(0.83 n) futures, no merging after the free chapter. Four starts in five never meet a narrower start's history. GC1891's check is a coin. DQ-013's wait anticorrelation was a twin echo. Measured, single-party.
- L957: Local's sideways front ([reports/rule30-sideways-front.md](reports/rule30-sideways-front.md); tests/probes/wolfram/sideways_front.py). GC1894's state question: the sideways discrepancy top closes exactly on four bits (L1 one-way, L2). L3 (found by the probe, hand proof): state 10 forces a white background and always survives. L4: state 01 survives iff the cell above the top is black. Measured speed 0.154–0.156 at τ = 51..401 (front of L955); fair-coin chain 0.22; P(black above top | 01) = 0.615 carries the speed. Hand lemmas single-party; Monte Carlo finite.
- L958: [sideways addendum](reports/rule30-sideways-front.md); tests/probes/wolfram/sideways_row.py. L5 (hand): state 11 survives iff the cell above is white, so one background row decides the top. L6 (hand): a vacated level leaves its cell black, read first by the next top. Measured: background rows fair and uncorrelated (0.5000, 0.5002); P(black) 0.868 at first decision, 0.4996 from age 6; drops mean 1.27. The 0.615 is selection, forced at arrival. Single-party lemmas; finite Monte Carlo.
- L959: GC1898 adopted (L3 carries; L4–L6 by GPT's direct proofs; four-bit autonomous closure refuted by a reachable witness; a row has one fresh trace bit per two columns). tests/probes/wolfram/sideways_window.py: L6 exact; residences 8.07/6.20/8.93 (hand 8/6/9); arrival law; a fair-input window model's speed rises to the real 0.155 by k = 3 to 6 (a model result). Next: fresh-versus-fixed input stochastic closure test.
- L960: Local's carrying read of GC1899's exposure induction (carries). tests/probes/wolfram/sideways_fresh.py: measurability operational (F0), new-odd inputs fair (0.4994), L6 repeats all black, backlog exact. New-even inputs act like fresh ones given state (gaps 0.004): fair-input closure supported for about 95% of decisions. Deviation: backward visits in state 11, P(s=1) = 0.7075; in 01 fair. Finite frequencies, not a closure proof.
- L961–L964: revisit discriminator frozen and repaired after GC1903 (sideways_revisit.py; run_capped.py supervisor with eleven harmless controls retained), awaiting GPT's launch agreement; carrying reads of GC1899 (L960) and GC1904 (L963; prescribed-pair four maps and the almost-sure protecting tail carry). L964 hand lemma ([map parity](reports/rule30-sideways-map-parity.md)): the prescribed map follows the fresh coin iff the exposed (J−1) anti-diagonal has odd white parity; protection becomes parity conditions on growing diagonal strings. Single-party, awaiting GPT's read.
- L966: the ONE agreed revisit stage (GC1906; sideways_revisit.py under run_capped.py, cited/sideways-revisit-20261026/): all controls PASS (GC1901 identity on 16,940 comparisons). Deterministic closure on M REFUTED (15 of 26 cells conflict), but every q = 2 cell and every state-01 q = 3 cell is forced; the 0.71 bias in state 11 is carried by forced cells; H(s|M) 0.345 against a 0.928 state baseline. Next: a hand short-revisit lemma.
- L967–L972: GC1909 two-step reread theorem (s_new = s_old at most-recent gap 2, every trace) carried in L970; revisit_sat.py revised after GC1910 (boundary profiles, strict verdicts), awaiting agreement. L972 [finite bridge](reports/rule30-sideways-finite-bridge.md): for finite F, a tock flip's partner F′ is finite iff the sideways pair empties within W + τ + 2 columns; past the white edge state 01 is impossible (L4 forces a black cell), so the top sticks in 11 for ever. Every trace, single-party.
- L973–L974 with GC1911: B0/B4 (every trace): after any finite trace edit the histories coincide from the last edited time on, so finite partners have equal width; no finite set of diary edits shortens a finite start; tocks after the free chapter are never forgotten for finite starts; L955 merged twins = finite single-flip partners. GPT's bundle extension carried (L974). revisit_sat.py containment changed to one supervised group (run_capped.py cleans every exit path; six controls, cited/revisit-sat-controls-20261026/); launch awaiting agreement.
- L975: the agreed SAT stage (GC1912; revisit_sat.py, cited/revisit-sat-20261026/): all eleven forced short-revisit cells CERTIFIED for every trace over every boundary profile and drop pattern, 384 cake_lpr-verified UNSAT certificates; q = 2 repeats (GC1909), q = 3 from a decided read flips, from E10 gives 1; controls K1–K5 pass. Local implications, not a closure, speed or prize result.
- L976: hand proof of (E01, old 0, q 3) by OR parity (every trace, single-party): each level the return's cascade empties contributes a forced OR term 1, so s_new = s_old XOR (q mod 2) on short returns (repeat at 2, flip at 3); (2,1,0) vacuous. Conjecture: q >= 4 conflicts arise where an emptied level's OR is free.
- L977: GC1913's finite-edit three-corner example carries (literal replay: rows, traces, common time-4 row, inverse a_15 = 1): individually forgettable tocks need not combine. GC1914 adopted: the L975 mixed cell is (0,3,0), not (2,1,0) (corrected); the OR-parity law needs joint parity (all T_i = 1 sufficient, not necessary).
- L978: the DQ zero-wall lane is the kit's Rule30ZeroBoundary Q01 (Theta/zrow/InX; equivalent to excluding eventual period 2); finite partners via edits up to tau = the merge class at tau+1; portal question to GPT (equal-width theorem probably too close to known). L979: at q = 4 (E01/0, pattern 4000) one OR term changes, T4 = (NOT u2 XOR (u3' OR u3)) OR u3', carrying the cell u2 that T3 masked; a 'masking chain' picture of where reread memory ends.
- L980: GC1915 carried (mixed E11/1/q3 reread = NOT(x OR y), current01 forced flip by hand); GC1916 adopted (merge class plus earlier-even guard; equal-width corollary internal, immediate from zrow_det and zrow_edge); GC1917 adopted (exact q4 current01 forced; the three-step-cutoff guess withdrawn). Return-length case line closed by agreement; next door: rigidity of a hypothetical Q01 counterexample's trace against the kit's barriers.
- L981–L982: L980 rigidity door downgraded (holds for every finite start; GC1919's control); DQ-007 note on certificate versus explanation; Local self-halts its heartbeat at a wall after reassessing all open DQs (L982), with a summary of the day's settled results and three doors for the owner's method.

- GC1894/MI821: [L955 targeted review](reports/rule30-tock-twins-gpt-review.md) accepts the merge-window criterion, qualifies finite population/late-merge/correlation claims; five retained evidence hashes. [Heartbeat configuration](reports/gpt-deep-question-heartbeats-20261026.md) records owner restart of GPT–Local deep questions and appropriate validated Wolfram submissions, prompts13/5 prepared but paused for owner activation. No new run.

- GC1898/MI822: [L957/L958 review](reports/rule30-sideways-front-gpt-review.md) carries L3 and L4–L6 decision conclusions with direct OR proofs. Reachable prefixes refute autonomous four-bit closure; fair-input/arrival-only and one-density speed claims unproved. Four retained outputs read; bounded Intel lemma audit only, no Monte Carlo replay.

- GC1899/MI823: [Sideways fresh-input candidate](reports/rule30-sideways-fresh-input.md), HAND/unreviewed; predictable leading-index exposure identifies fair new odd inputs and backlog max(0,B+K-1). Reused-input law, closure and speed open; no experiment.

- GC1900/MI824: [L959 model review](reports/rule30-sideways-window-gpt-review.md), COMPLETE/source and two receipts. Large-drop residences differ from iid; arbitrary restart can violate L3. Odd does not imply fresh after drops; exact next design pending, no replay or closure theorem.

- GC1901/MI825: GC1899 independently carried by L960/adopted; L960 source/two receipts reviewed with pooling/class/statistical guards. Same-index input difference is intervening OR parity below J, elementary HAND identity; memory closure open. `reports/rule30-sideways-fresh-gpt-review.md`; no replay/new launch.

- GC1902/MI826: exact all-live-column budget O+B=tau-H bounds old visits by tau; abstract even-input protection defeats fresh-odd-only extinction inference. HAND/unreviewed, not actual Rule30 survivor or uniform lifetime bound; fresh-input note section6.

- GC1903/MI827: L961 full source review; GC1901 identity independently carried/adopted, revisit computation sound. Approximate-as-exact determinism and wrapper pressure/cleanup/disk gaps require repair; same stage unaccepted, no run. Fresh-gpt-review section5.

- GC1904/MI828: predictable zero/one/copy/flip odd-even input map; nonprotecting pairs have three-update hazard>=1/4. HAND candidate: infinite live product-trace path almost surely eventually(11,copy)/(10,zero); actual tail possibility/extinction open. `reports/rule30-sideways-prescribed-pair.md`.

- GC1905/MI829: second-leading Boolean difference gives exposed-diagonal response slope; all four maps realised in valid cones. Background no-copy shortcut REFUTED; first copy cone not at proposed front. HAND, same carrying packet pending; prescribed-pair section5.

- GC1906/MI830: L962 exact revisit stage agreed after supplied cleanup-parser repair; original controls read, seven literal parser fixtures pass. L963 budget/tail proofs adopted; L964 parity carries, both-branch versus realised-path scope explicit. `reports/rule30-sideways-revisit-agreement.md`.

- GC1907/MI831: HAND candidate five-update hazard>=1/8 outside two-choice protection; infinite live product-trace tails almost surely eventually protect both next choices, forcing odd-index white parity0. Actual obstruction open; `reports/rule30-sideways-two-choice-protection.md`.

- GC1908/MI832: L966 three retained receipts/source reviewed; M exact closure refuted15/26 cells, stage consumed;98.4% state11 excess from sample-constant groups. HAND no-ENONE consequence pending Local, L965 phase guards; `reports/rule30-sideways-revisit-outcome-review.md`. No replay/new run.

- GC1908/MI832 continuation: E11/old1/q2 reread1 EVERY-TRACE hand candidate via two zero background equations; Local carrying read pending. L967 E01 branch remains open; no enumerator launch. Same outcome-review report.

- GC1909/MI833: L968 independently carries GC1907 two-choice/parity almost-sure theorem and GC1908 no-ENONE/E11-q2 every-trace results; adopted. Complete EVERY-TRACE gap2 reread-preservation candidate closes E01 via shared-white contradiction; final read pending. `reports/rule30-sideways-two-step-reread.md`; no computation.

- GC1910/MI834: L970 carries full GC1909 most-recent-gap2 reread theorem, adopted EVERY-TRACE. L969 SAT source reviewed; pattern/boundary/verdict/lifecycle repairs, three mocked false passes/24 gate assignments; no launch. `reports/rule30-revisit-sat-source-review.md`.

- GC1911/MI835: L972 single-tock finite-partner bridge independently carried; exact pair cutoffW+tau+3, safe traceW+2tau+2. Finite-edit extension/earliest-edit guard HAND pending Local. L971 SAT coverage/gates accepted; execution containment repairs/no launch. `reports/rule30-sideways-finite-bridge-gpt-review.md`.

- GC1911 continuation: L973 B0/B4 carried; tail equality plus known edge speed forbids shortening by ANY finite trace edit, not just one flip. Empty-start guard; bundle-partner finiteness criterion pending Local. Same review section5.

- GC1912/MI836: L974 finite-bundle bridge independently carried/adopted. Known-window consequence: unequal finite widths require differences in[s,2s+W−1]; retimed equal tails forceW'=W+k. ONE amended SAT stage agreed pending Local adoption; six receipts/eight mocks reviewed. No new dynamics.

- GC1913/MI837: hand finite-edit interaction candidate, reports/rule30-finite-edit-interactions.md. Three width-11 finite beginnings realize tock choices00,10,11 with one common time-4 future; fourth01 is infinite by inverse cell15 and edge width. Successful singleton edits need not combine; no eternal-class/abundance assertion. Local read pending, no computation.

- GC1914/MI838: reports/rule30-revisit-sat-outcome-review.md closes L975 actual evidence review (466 frozen CNFs,384 bound checker receipts,376 branches; no replay) and carries L976 E01/0/q3 hand proof. Correct K3 mixed pattern to(0,3,0); joint OR parity, not a free term alone, controls a longer reread. One-stage agreement consumed.

- GC1915/MI839: hand mixed-return explanation appended to reports/rule30-revisit-sat-outcome-review.md. Old E11/1 most-recent q3 forces030; reread is NOR of c_d(H-2),c_(d+1)(H-2). Current01 forces second bit1; current11 lacks that forcing. Local read pending. L966 capped-gap descriptors lack actual backgrounds; no replay/new run.

- GC1916/MI840: L977 independently carries GC1913 finite-edit noncombination, adopted. L978 merge equivalence requires earlier-even agreement; class/start weighting distinguished. Kit5473ffd lam/Theta and Q01/CQ01 scopes checked; equal-width immediate kit corollary, no standalone portal effort. `reports/rule30-finite-edit-interactions.md`.

- GC1917/MI841: L979 q4/4000 conditional algebra carried; s_new=NOT(v) AND(u2 XOR u3). Current01 forces last input1 and reread0. Exact mixed physical pair unshown; L9664 is>=4/L975q2-q3 only. Revisit outcome report; no run.

- GC1918/MI842: carried GC1913 fixture rebased at A proves edit rescue; fixed-future admissibility q<=p. Rejected time1 inverse has all-black tail from14, known kit back_fin_iff. Both-singletons-fail/general compatibility open; no run. Interaction report.

- GC1919/MI843: L980 independently carries GC1915/adopted; return-case expansion closed jointly. Rigidity-alone entropy inference fails abstract powers-of-two suffix control (nonperiodic, shift-closed, p(N)<=5N+1); no finite Rule30 realization. Interaction report; no run.


- GC1922/MI844: [blind-future/witness hand note](reports/rule30-blind-future-and-witnesses.md), DQ-015/016. Exact finite observation-class criterion; eight-triple Rule30 control keeps75% accuracy while confidence improves; known G4.4/G97 hidden-fair-pivot bound. Physical-time/sideways-selection distinction explicit. Elementary HAND, unreviewed, no new theorem claim, hard-family predictor, run or schedule restart; owner-led Local handoff.


- GC1923/MI845: [Intel witness review](reports/rule30-blind-witness-intel-review.md), 1360 exact lanes/controls COMPLETE; far4 replacement advantage REFUTED, far6 insufficiency witnessed. Post-hoc32-lane joint view raises optimum16/32 to28/32; no unseen/general predictor. Imposed alternating-wall mergers hand/COMPUTED; full-line survival separate. Legacy merge startup capped/incomplete; schedules PAUSED, Local review pending.

- GC1925/MI846: [L987 design review](reports/rule30-certificate-witness-design-review.md), full frozen source. Hand mandatory dependency triangle gives reads=W; triangular trace gives START mincert<=W/2; H3 refuted before run. Exact group minima algorithm carries; policy/scope/stop/evidence amendments pending Local. No run, launch or novel theorem claim.

- GC1926/MI847: L988 independent hand read adopted; full revised certificate source/supervisor review, remaining allocation guards patched and output bound corrected. One exact certificate-only stage GPT-agreed after Local adoption; no launch/result yet. Review addendum contains source hash, bounds and artifact contract.
- L989: certificate_witness.c ran once (GC1926 caps; receipts cited/certificate-witness-20261026/); controls ALL PASS; H1 FAILED (tie at W20), H2 FAILED with counterfactual met (PASS DIARY W28/W14 = 3), PU held 0.627; witnesses grow with W in both coordinates; a crude random-function estimate matches within 0-1 (model, not proof). Next: certificate_shuffle.c (exact shuffle null), frozen, awaiting GPT.

- GC1927/MI848: [certificate outcome review](reports/rule30-certificate-witness-outcome-review.md), six digest-verified receipts/all49,167 rows audited, H1/H2 finite failures and PU hold. Casewise3-read savings; hand F5=F3=NOT F2 explains tie omission, independently matched/carried by concurrent L990. One exact patched sampled-null stage agreed after adoption; no new run.
- L991: certificate_shuffle.c (GC1927 bytes b14a5d1d) ran once, controls ALL PASS; R1/R2 FAILED with counterfactuals MET (Rule 30 diary witnesses shorter than all 64 shuffles at W16..28, gap ~1 cell); PU FAILED; post hoc certificate_influence_posthoc.py: deficit in the oldest three entries = DQ-009's forgetting front (L955). Receipts cited/certificate-shuffle-20261026/.
- L992: L991's witness shortcut = L955's twin-merge front (influence ≈ (1 − μ)/2; merged twins agree every trace, unmerged differ about half the time, q from 0.41 to 0.56 at W16/W24); Local recommends closing the DQ-015/016 single-cell certificate line.

- GC1928/MI849: [shuffle outcome review](reports/rule30-certificate-shuffle-outcome-review.md), six receipts/all1,408 sampled sums audited; rank0 carries, sensitivity attribution qualified. Balanced equal-influence/different-certificate hand control and C_cond bounds; Local conditional ALL specification requested, no launch agreement.
- L993: GC1928 countermodel carried by Local (influence does not determine mean certificate size); two Local claims withdrawn (merged-exactly, rivals-double); certificate_conditional.c frozen (K1-K6, M/CF/PU), awaiting launch review.
- L994: loop check (repeated assumption: a nearby summary settling a different question); certificate_conditional.c PU replaced before review (class-mean span at W28; old slack PU was implied by M/CF via the W22 shuffle mean 8.5164); source sha256 0c6a6358.

- GC1929/MI850: [conditional source review](reports/rule30-certificate-conditional-design-review.md), L993/L994 entire196-line revised source accepted unchanged for one frozen ALL W24/26/28 stage. Countermodel independently carried; launch/results pending, no GPT run.
- L995: certificate_conditional.c ran once (receipts + manifest cited/certificate-conditional-20261026/); controls ALL PASS; M HELD (8,8,8), CF not met, PU HELD (span 0.0635); post hoc lean ~0.03 cells/lane; exact pattern (b1 = b2 = 1 ⇒ tock 0 invisible to x(W+1,1), W8..28) routed to the sideways front; certificate line proposed closed.

- GC1930/MI851: [conditional outcome and hand proof](reports/rule30-certificate-conditional-outcome-review.md), seven receipts/all1,536 shuffle sums reviewed; M held, CF not met, PU65/1024. All-tail time2 merger for forced seven-cell prefix HAND candidate explains classes6/7 for all evenW>=8; Local read pending, no run or survival bound.
- L996: GC1930 seven-cell merger carried by Local's independent derivation (b1 = b2 = 1 ⇒ tock-0 twins merge at time 2, every even W ≥ 8, all tails; two-party, elementary); one-way link: start difference within depths ≤ W − 4 ⇒ tick-1 merge; certificate statistic incubated; Local self-halts its heartbeat at a wall.

- GC1931/MI852: L996 independent carrying read of GC1930 adopted; all-tail time2 merger two-party. D<=W-4 cone link carried as existing machinery. Local halt supported, finite certificate-statistic conclusions qualified; broader observer/survival questions open.

- GC1932/DQ-020: [triangle ancestry manual handoff](reports/rule30-triangle-ancestry-handoff.md), owner questions, corrected cap/tip discussion, four-state backward maps for001/101, period-six interior chain and small white-patch ancestry. Hand derivations awaiting Local read; prior8.18/8.82, finite-margin/phase/realization limits; agreed adversarial hand-first method. No computation or schedule restart.
- L998/DQ-020: [Local's read](reports/rule30-triangle-ancestry-local-read.md): GC1932 carries; white-run parent trichotomy 1:1:2 (refines 8.68; GC847 is L = 1); lone white cell hangs a run of its left black run's length; first-generation child width 2^-k; hand pair H1/H2 — HAND, guarded (triangle_parents_check.py), single-party.
- L999/DQ-021: [Local's staircase review](reports/rule30-staircase-local-review.md): GC1934's alternative carries (independent recompute, 22,321 single-seed bars); left companion (a black bar forces white on its left); the staircase is the rain (GC847's front at exactly one cell per row); the front hangs shape-B triangles in a 2, >=3 rhythm (crop 2, 3, 2, 4) — HAND, guarded (staircase_rain_check.py), single-party; GC1933 adopted.
- L1000/DQ-022: [one rule behind the map](reports/rule30-run-rule.md): R, Rule 30 acts on each run in place (black run -> head only; lone white stays; longer white run -> ends black); P, two histories' agreement eroded from the left at speed 1 and held on the right only on black (8.66 + light cone); bridge law 3r+1 <= L <= 3r+4; edge law E for every finite seed (alternation, rhythm, half-ruler versus rain edge by one bit; single seed = 8.73's ruler); ring counting laws — HAND, guarded (run_rule_check.py), single-party.
- L1001/DQ-022: [the ruler is universal](reports/rule30-universal-ruler.md): Theorem U, every finite seed's right-edge emissions equal the single seed's (shifted by s0) below width k* - 1 and are exactly k* - 1 elsewhere, k* = depth of the edge code on the single seed's 2-adic cycle; k*+1 never a doubling level; rain edges k* = 2 (GC808's mod-8 cycles) — HAND (lifting + GC808 isometry + Proposition 23), guarded on all seeds to width 14 (universal_ruler_check.py), single-party.
- L1002/GC1935: U carried at finite depth (GPT's prefix-return gap proof adopted); infinite depth stated with the compatible phase; assertion A (finite points of the single seed's 2-adic closure are T^tau(1)) OPEN, reduced to '-1 is the only eventually-ones point' (HAND), supported below 2^24 at depth 44 (closure_finite_look.py); T^-j(1) is GC1932's tower and the cap formula L_u >= L iff p_L | u+1 (HAND + replay).
- L1004–L1006/DQ-023: cut-and-repair of c137e0's clock fully explained: left black-tick rule plus membership of the required white-tick right word in the visible language; cut 49's exact optimum over every right row is 52, blocked by MFW 101001 (rule30_local_mfw44.txt) — HAND + exact SAT (clock_deadline_check.py, clock_right_realizability.py).
- L1007/DQ-021: [Theorem S](reports/rule30-staircases-end.md): in the single seed's picture every alternating stretch (staircase) of length >= 3 dies, by the first multiple of p_(W+2) (W = front's distance from the right edge, constant by the front lemma); every patch of a history with no two adjacent white cells is finite-lived; other seeds only W <= k*-2 — HAND, replayed (staircase_end_check.py), single-party.
- L1008/DQ-021: Theorem S is sharp: the rain seed (01)^n keeps an eternal staircase at its right edge because -1/3 (endless rain) is a period-2 point of T and (01)^n agrees with it to 2n bits; GC808's mod-8 cycles (1 7)/(3 5) are the shadows of 1's odometer and the rain 2-cycle; principle: eternal patches exist only as periodic structures dragged by the right edge — HAND, replayed (staircase_end_check.py part two).

- GC1933: [L998 targeted independent review](reports/rule30-triangle-ancestry-gpt-review.md), C/A/B and singleton-child hand claims carried, H1/H2 checked, conditional fair-row law carried; transient versus phase ambiguity, tip-time correction and K4 guard limits. No execution; continued owner-led DQ-020.


- GC1934/MI853/DQ-021: [staircase investigation](reports/rule30-staircase-investigation.md), steady1 bar forces an adjacent alternating segment or a latched01 successor two columns right through b+2. Single-party hand derivation awaiting review; exact supplied-image match and174720-cone/4125-bar finite controls. No eternal-clock or chain-termination claim; cited/gc1934-staircase/ receipts.


- GC1935/MI854: [L999–L1001 independent review](reports/rule30-structure-unification-gpt-review.md). Scoped run/patch/bridge/edge laws and finite-depth capped emitted-width ruler carried; direct prefix-return gap proof, seed100001 cap4. Infinite-depth ordinary-time shift not established; compatible-phase replacement and exact remaining obligation. GC1934 independent read adopted; no rerun.


- GC1936/MI855: [L1002 closure reduction review](reports/rule30-finite-closure-gpt-review.md), finite inverse descent/eventually1 dichotomy, A iff only eventually1 closure point is -1, equivalent fixed-offset detached-run bounds. Hand claims carried; A open, third predecessor boundary defect retained, A/B guard exit coverage qualified. No rerun.


- GC1937/MI856/DQ-023: [natural staircase centre-lock question](reports/rule30-staircase-centre-lock.md). Known period1 excludes permanent supporting bars; genuine alternating-centre identities permit replacement contexts. Hand11001/four-tick witness, endless replacement unexcluded; single-seed/prize and arbitrary-seed scopes distinguished. No run.


- GC1938/MI857: [27 October portal delta](reports/wolfram-agents/GPT-PORTAL-UPDATE-20261027-MORNING.md),12 new IDs/52 total/no removals; selected trap/half-infinite-clock source scoped read, no replay. [DQ-023 cut-and-repair plan](reports/rule30-clock-cut-and-repair-plan.md): exact hand truncation baseline and left-only deadline, bounded intervention DESIGN only, no run.

- GC1940 / MI859 / DQ-023: reports/rule30-clock-cut-and-repair-result.md;573 fixed Intel cases, one10/12 repair at cut21 (22→23), every-right deadline23, failed transfer; cut23 right-prefix compatibility open. Evidence cited/gc1940-clock-repair/manifest.json; independent read pending.

- GC1941 /MI860: reports/rule30-clock-repair-right-obstruction.md applies known Lemma3 no11 to exclude all right completions for cut15/23 beyond d; reference-cut repairs require d=2 mod4. Hand application awaiting Local; no new experiment.

- GC1942 /MI861 /DQ-023: reports/rule30-clock-front-parity.md; hand e-next=e XOR NOT reference-right recurrence,28-phase odd-white parity, candidateL49/d50 immediate-black survival. Single-party application pending Local; right realizability open; no run.

- GC1944 corrects GC1942 novelty: exact prior recurrence GC1167, phase flip GC1194, nonlinear tube GC1195, black-start d50 class GC1197 (all archive/gpt/RULE30-GPT.9.md; independently reviewed). reports/rule30-clock-front-parity.md records coordinate match and scope. No new run.


- GC1948/L1010/GC1950: [full edge period-two classification](reports/rule30-edge-two-cycle-classification.md): the only odd solutions of T^2(R)=R are +/-1/3; all Z_2 solutions are0 and +/-2^m/3. Two-party hand proof; no novelty claim and no centre-column inference.
- GC1949/GC1950: [one witness extraction agreement](reports/rule30-clock-witness-extraction-agreement.md), cut49/TH49 only, exact amended source/supervisor hashes and resource envelope accepted for Local. Outcome acceptance awaits retained witness/trace/receipts.

- L1011/GC1951: [retained witness review](reports/rule30-clock-witness-gpt-review.md), exact first-failure optimum52 for fixed left cut49, explicit finite right completion and known101001 upper bound. All uploaded hashes, SAT model clauses and recorded centre transitions checked; evidence cited/l1011-gc1949-witness/. One agreed M5 extraction complete; no all-seed or centre-prize theorem.


- GC1955/MI873: [external317c64 integer-Q01 review](reports/wolfram-agents/GPT-317C64-INTEGER-REVIEW.md), conjugacy/finite encoding/equivalence source-scoped PASS. Known edge growth separates recursive evaluation from orbit descent; other sections unread, no kernel replay or Q01 solution.


- GC1956/MI874: [external self-shielding review](reports/wolfram-agents/GPT-317C64-SHIELD-REVIEW.md), local WBAt/right-wall/box/cone/4j proof chain carried. Same left driver required; agreement is not alternation. Later exclusion dependencies remain separate, no numerical run.


- GC1957/MI875: [self-shielded exclusion dependency review](reports/wolfram-agents/GPT-317C64-SHIELD-REVIEW.md), pinned BlackRuns/MaskedJen/Jen interface, both later exclusion proofs and length-4/8 corollaries carried in single-seed-centre scope. Retained evidence cited/gc1957-self-shield-dependencies/. Thresholds do not apply to pure period two; no local kernel replay.


- GC1958/MI876: [external WhiteRuns review](reports/wolfram-agents/GPT-317C64-WHITE-REVIEW.md), full generic two-certificate argument and eight instances carried in single-seed-centre scope; external finite-certificate verification, no local replay. Universal one-black-pulse premise fails by hand.


- GC1959/MI877: [317c64 integer/edge completion](reports/wolfram-agents/GPT-317C64-INTEGER-REVIEW.md), full retained source now reviewed across GC1955–1959. Recurrence evaluator/residue and D0–D7 scope carried; no local kernel replay. Known rain -1/3 supplies an infinite-support survivor, leaving Nat membership open.


- GC1960/MI878: [external1b82d8 complete source review](reports/wolfram-agents/GPT-1B82D8-DIAGONAL-REVIEW.md), half-rate diagonal-exponent bound and actual zero-orbit resource carried; exact5473ffd interfaces retained. Abstract2/0 path defeats finite-fuel gloss; cyclic endpoint transfer to DQ-023 unproved, no local kernel replay/run.


- GC1961/MI879: [finite-window correction](reports/wolfram-agents/GPT-1B82D8-DIAGONAL-REVIEW.md), hforce makes hcycle redundant for countdown; elementary source consequence. Exact phase-error E gives corrected A+E resource; closed-end M4 countercontrol defeats uncorrected transfer. HAND/no replay, not a Rule30 realization or centre bound; supersedes GC1960 endpoint diagnosis.


- GC1962/MI880: [actual phase-error hand control](reports/wolfram-agents/GPT-1B82D8-DIAGONAL-REVIEW.md), single-seed depths4/5/6 at times1..9 refute uncorrected arbitrary-window countdown (2<=1). Full-cycle theorem intact; corrected input resource0. HAND/single-party, no computation or centre-clock witness.


- GC1963/MI881: [external e67465 review](reports/wolfram-agents/GPT-E67465-COUPLED-SOURCE-REVIEW.md), complete499-line source scoped PASS; no11 source automatic beside alternating centre, nested-window/density and Fibonacci-rate guards. [L1014 hand reply](reports/rule30-finite-closure-gpt-review.md): exact two-bit strip correction and uninterrupted-shield bound p_W-1 in Omega; cross-episode tower/centre bounds OPEN. No replay/compute.


- GC1964/MI882: [shield interruption continuation](reports/rule30-finite-closure-gpt-review.md), known PhiS0/1/3 action preserves first differing upper bit under any common boundary history. Full-prefix reset unavailable; geometric pattern loss and orbit-specific tower bound distinct. HAND known-structure consequence, no compute or new proof claim.


- GC1965/MI883: [S3 formalization specification](reports/wolfram-agents/GPT-S3-FINITE-EDITS-STATEMENT-CHAIN.md), exact kit types/proof chain; known Theta two-step merging distinguished from seven-cell arbitrary-tail finite-truncation stability. Live7d665044/52-entry targeted duplicate check; Local M5/delivery owner proposed. No compile/submission/new experiment.


- GC1966/MI884: [S1/S2 source review](reports/wolfram-agents/GPT-S1-S2-SOURCE-REVIEW.md), full carrying Lean and exact essay assembly PASS in scope; finite-depth/odd-code/two-phase-patch prose corrections required. Actual Check/notebook evidence pending; no replay, upload or new experiment.


- GC1967/MI885: [S2 related-map comparison](reports/wolfram-agents/GPT-S1-S2-SOURCE-REVIEW.md), actual0ef9c8 definition/bridge/headlines use higher-index/right-shift map; our edge map uses lower-index/left-shift map. Hand1 fixed versus1->7; related-work correction supplied, no full external certificate audit/replay.


- GC1968/MI886: [L1018 catalogue/source review](reports/wolfram-agents/GPT-S1-S2-SOURCE-REVIEW.md), both core modules and merged staircase termination carry; exact essay/patch bindings pass. README table placement and n1 rain geometric gloss require repair; actual validation outputs pending, no replay.


- GC1969/MI887: [L1019 actual evidence review](reports/wolfram-agents/GPT-S1-S2-SOURCE-REVIEW.md), four Check reports and both nine-cell notebooks/output inventories PASS; exact hashes/serialization scope retained. Final L1020 S2 and three-patch README also PASS; both artifact reviews complete, PR/delivery pending; no replay.


- GC1970/MI888: [L1021 S3 source review](reports/wolfram-agents/GPT-S3-FINITE-EDITS-STATEMENT-CHAIN.md), complete195-line arbitrary-tail rewrite/common-cut/guarded-merger core source PASS. Actual Check receipt and section3 Theta localization pending; no replay or new computation.


- GC1971/MI889: [S4 publication synopsis](reports/rule30-run-rule.md), already carried run/parent/hanging/bridge proofs consolidated with finite-boundary and fair-row/adaptive qualifiers. Not all present in S1/S2; formal delivery explicitly pending. Selected kit check only, no new theorem or compute.


- GC1972/MI890: [L1022 S3 complete review](reports/wolfram-agents/GPT-S3-FINITE-EDITS-STATEMENT-CHAIN.md), Theta localization induction and actual two100-declaration checks carry; all8 outputs bound with recon_win display qualification. Abstract later-tick condition restored; final essay validation pending, no replay.

- GC1973/MI891: [final S3 and delivery audit](reports/wolfram-agents/GPT-S3-FINITE-EDITS-STATEMENT-CHAIN.md), corrected8-output notebook/checks PASS, all3 live submitted sources/notebooks byte-bound; portal Lean Verified78/90/100, PR42 open/unmerged, human tags empty. No replay.
- GC1974/MI892/DQ-020: [canonical triangle lineage candidate](reports/rule30-triangle-lineage-fresh-input.md), unique fresh-bit word coding at adaptive odd tips gives width2^-m and survival(2/3)^n under fixed-suffix/fair-left input. Complete HAND/PROOF-SKETCH, Local read pending; not single-seed or arbitrary connected components, no compute.

- GC1975: L1025 owner full halt adopted; both GPT automations tool-confirmed PAUSED. GC1974 candidate/read parked unreviewed, no compute or submission/review request; restart only on owner direction.


- Notebook-growth test: deaths32/34/43 reproduced; age100 short-word control UNKNOWN; longer search unstarted — numerical qualification, not asymptotic verdict — GC1979; reports/rule30-notebook-growth-intel-result.md.

- Isolated root: no finite predecessor, exactly two bi-infinite predecessor rows by OR recurrence — elementary hand derivation, unreviewed — GC1981; reports/rule30-missing-parents.md.

- Root inverse tree: A has2 parents, B3; exactly5 two-step ancestors; complement is not a Rule30 symmetry — elementary hand, unreviewed — GC1982; reports/rule30-missing-parents.md.

- Witness pilot61 retained traces reviewed; E34 length8 has28 words; E100 has25..28; early absences1/1/17 and a one-tick frontier identity — reviewed data/hand consequences — GC1983; reports/rule30-notebook-witness-pilot-gpt-review.md.

- Root inverse tree depth3: exactly8 rows;001 right ray has unique101 parent by constant two-block pair map — elementary hand, unreviewed — GC1984; reports/rule30-missing-parents.md.


- GC1985/GC1986: Ouroboros output/support question recorded under DQ023; exact retained-row back-solve fails, short boundary-prefix explanations; word memberships unresolved — reports/rule30-notebook-backsolve-result.md.


- GC1988/GC1989: direct P100/R100 stage, three timeouts then disk stop; P99 unstarted; controls pass, no membership conclusion — reports/rule30-notebook-membership-result.md.


- GC1991: disappearing-word past-tree recursion, wrapper deadline bound and forced-prefix deletion delay; elementary hand consequences pending read — reports/rule30-disappearing-words-hand.md.


- GC1996/L1037: z=001000010001 occurs only atage0 beside the alternating wall; hand R/B/A/E plus independent full-cone finite D, explicit witness — COMPUTER-ASSISTED proved — reports/rule30-z-head-independent-audit.md.


- GC1997/L1040–42: hand reset tracks carried;3-run successor table independently recovered from MFW44;70/two-head and dependency minimality evidence pending — reports/rule30-reset-tracks-gpt-review.md.


- GC1998/L1051–53: dyadic past-wedge centre readout carried; first unsupported period forces complementary bit; Rule60 constant-centre countercontrol — hand consequences, pending Local read — reports/rule30-past-readout-prize-review.md.


- GC1999/L1054–57: exact readout frontier now two-party; periodic-tail 1-or-3k and no-solid-row lemmas carried; blanket route closure not established. Portal two added IDs, one byte-identical and one conditional pulse synthesis — reports/wolfram-agents/GPT-PORTAL-UPDATE-20261028-MORNING.md.


- GC2000: meaning of canonical-past selection; G122 recovered, finite-patch translation consequence and far-right-singleton nonlocality check — elementary hand analysis, no new independent review — reports/rule30-reconstruction-meaning.md.


- GC2001/L1043: retained reset/survey packet digests verified; exact-minimum depth algorithm source carries conditional on completed execution, correcting GC1997 upper-bound-only objection; numerical rerun and full survey certificate not claimed — reports/rule30-reset-tracks-gpt-review.md (GC2001 addendum).


- L1062: read-out frontier B(P) = L(P) + 1 is Proposition 23 (right-edge white triangles) seen from the past, so the read-out cost is its ruler sequence; Rule 60's frontier is linear; the OR overlap term at B(P) is 1 except at inherited periods and ties c(B−1), c(B−2) to a parity of about P cells, no centre relation — hand, single-party, computed check to P = 2048 — reports/rule30-frontier-overlap.md.


- GC2002/L1062: past-copy first failure equals right-edge triangle width plus one; overlap weight cases carried with forcing-period definition; negative/computational-growth claims qualified — reports/rule30-frontier-overlap-gpt-review.md.


- GC2004: alternating-tick forcing criterion for diagonal weight parity; actual period64 weight32/31 contrast; half-period pairing connects to GC763. Hand application plus bounded self-check, independent read pending — reports/rule30-diagonal-phase-parity.md.


- GC2005–GC2008: genuine-world phase-summary collisions, alternating residue-parity explanation, candidate generic no11011/three-fifths period-exponent ceiling with8,320 bounded carrying checks; stronger external single-seed half-rate bound credited to GC1960/1b82d8. Hand proof pending later review — reports/rule30-phase-statistics-closure.md and reports/rule30-five-step-period-bound.md.

- L1063: GC2007 five-step lemma (11011 forbidden after Q ≥ 4; e_j ≤ ⌊(3j+5)/5⌋) second-read by Local via the even-tick sum, two-party hand result; genuine-seed check (150 seeds) no failure; corollary w(v) ≥ 5v/3 − 1 for Proposition 23's edge triangles and read-out depth ≤ 2^⌈3n/5⌉ — CHAT-LEDGER.md L1063, reports/rule30-five-step-period-bound.md.


- GC2010: L1063 carrying read accepted; five-step core promoted to two-party hand proof. Triangle/read-out corollary qualified as sufficient and weaker than existing single-seed half-rate ceiling. GC2009 generic-source parametrization remains uncompiled and single-party — reports/rule30-five-step-period-bound.md.


- L1064: right-diagonal doubling word — universal start 4,8,8,16,32,32 at j = 1 + first equal adjacent seed pair (PROVED, computer-assisted); 101 lemma x = q/2 + E_q(D_(j−1)), containing GC2007's 11011 exclusion (PROVED, single-party); monotone periods: single seed known (kit per_mono_all, GC2014), arbitrary seeds CONJECTURE, exhaustive through depth j+21, not local; exact beginnings tree 285 at length 20 (×1.56 vs ×1.81); seed echo generalises Proposition 23 (PROVED); single-seed plateaus to v = 25 (MEASURED); fair-coin model REFUTED — reports/rule30-doubling-word.md.


- GC2011–GC2014: L1064 101/cascade and finite-seed echo second-read; universal start independently checked in 256 cases. Complete right-diagonal pair graphs through period 32: only rain cycle, no drops, sharp ten-diagonal period-32 plateau before the first period 64, first 64 by j + 14. Independent rank certificate; candidate full odd T^32 fixed-point classification and delayed seed-bit parity identity await Local. Single-seed monotonicity recovered from existing kit per_mono_all; arbitrary-seed monotonicity remains open. L1064's length-22 tree ends at j + 21. — reports/rule30-bounded-period-graph.md.


- GC2015: B-hole vertical backward alternation forces 0,1,1; elementary local obstruction, PROOF-SKETCH. Moving diagonal starts 1,0,1,0 and is not excluded; eventual backward periodicity remains separate — reports/rule30-missing-parents.md.


- L1066: eternal right edges — cap-64 pair graph closes (171,779 states, rain only, no drop): T^64 fixes only ±1/3 (COMPUTED, with GC2013's argument); 92-diagonal period-64 plateau witness (literal check); unfuelled plateau continuation ≤ 8 (period 32), ≤ 15 (period 64), exact; Lemma R: pair-graph cycles = light-speed ring orbits (PROVED); ring classification complete at Φ-period ≤ 8 (white, rain, (0001)), census to m ≤ 26 / P ≤ 256 and m ≤ 20 / P ≤ 4096; conditional "H and N ⇒ rain only" (N: no diagonal after D_(j+5) below period 32; corrected in L1067), N not local; exact exit mean 9.841 at cap 64 — reports/rule30-periodic-edges.md.


- L1066: eternal right edges — cap-64 pair graph closes (171,779 states, rain only, no drop): T^64 fixes only ±1/3 (COMPUTED, with GC2013's argument); 92-diagonal period-64 plateau witness (literal check); unfuelled plateau continuation ≤ 8 (period 32), ≤ 15 (period 64), exact; Lemma R: pair-graph cycles = light-speed ring orbits (PROVED); ring classification complete at Φ-period ≤ 8 (white, rain, (0001)), census to m ≤ 26 / P ≤ 256 and m ≤ 20 / P ≤ 4096; conditional "H and N2 ⇒ rain only", N2 not local; exact exit mean 9.841 at cap 64 — reports/rule30-periodic-edges.md.

- GC2016–2018: B ancestry with alternating x=t has maximum 37 backward steps; exact complete inverse-tree closure, independent implementation, 13-cell final obstruction; A/B 512-row visual data checked — reports/rule30-backward-diagonal-b.md.


- L1067/L1068: L1066's hypothesis corrected to N (no diagonal after D_(j+5) below period 32), which also covers the (0001) fall-back; GC2015 second-read (carries); GC2018 forcing word second-read; no period drop to 2^24 (MEASURED); approximate periodic points of T: exactly 4, 8, 32, 64 residues mod 2^k fixed by T^2, T^4, T^8, T^16 (explained by the universal start), 2,112 for T^32 (k ≥ 18), 171,776 for T^64 (k ≥ 106, via graph path counts) — reports/rule30-periodic-edges.md §7.

- GC2019: periodic right-background extension and exact rightmost-defect line x=t for root ancestors; hand combination of L1049/G122, PROOF-SKETCH; front colour complements background, independent of alternation — reports/rule30-backward-diagonal-b.md.

- GC2020–2022: two certified crystal fronts of the same depth-512 A/B pasts; 2634/2838-cell transition widths; largest backward jump 50 at unchanged spatial period 48; all jump sites verified by OR masking/XOR cancellation; independent infinite-left seam audit, widened interactive view and retained failed patch-copy prediction — reports/rule30-two-crystal-fronts.md; CONSTELLATION.md I.

- GC2023–2024: strict proper period-three root-backward diagonal words 100/101/110 close at depths 5/3/4, complete dual-implementation parent sets; short hand background-ray explanation pending Local; spatial period-three precursor distinguished from temporal trace — reports/rule30-backward-period-three.md.

- GC2025: root as a past/future junction; finite support versus open observation strip versus closed ring; existing span-growth corollary and elementary bi-infinite finite-state cycle argument, no experiment — reports/rule30-space-time-boundaries.md.


- L1069: self-sustaining regions (GC2025's question) — left boundary is exact XOR (never masked), right is OR (maskable): no region slower than light is ever closed; closure only for light-speed bands against a constant or self-generated exterior (edge bands, ring orbits), and closed ⇒ periodic (PROVED, elementary); interior strip's centre determined exactly W/2 steps, right end erodes ≈ 0.5 (ignorance, vs damage 0.246) (MEASURED, upper bound) — reports/rule30-self-sustaining-strips.md.


- L1070: second reads — GC2019 right front X_t(t) = 1 − C_t(t) for every root ancestor (carries, via L1049); GC2022 left-seam certificate and masking/cancellation identity (carries); GC2024 root-anchored period-three closure, seven parent relations independently recomputed, hand exclusion complete (carries).


- GC2026–2028: [exact strip knowledge](reports/rule30-exact-strip-knowledge.md), a10 uncertainty recovery and a0101010 eight-step returned bit, dual finite-cone checks; infinite-left rain lock recovered as prior G.GPT271, hand five-sample-gate connection awaiting Local. Supersedes L1069's unknown-cannot-heal and universal W/2 gloss, not its twelve measured samples. L1070's three carrying reads adopted and original report statuses updated.


- L1071: quantum-gate grounding (GC2030) — quantum algorithms at most quadratic for our search/counting, no certificates, nothing on Problem 3 (literature); one-sided space-time duality: left environment a perfect dephaser, correlations only on the right light-cone edge (PROVED, elementary); spin models count torus orbits, not our pasts; deg c(t) = 2t − 1 with unique top monomial, t ≤ 12 (CONJECTURE, COMPUTED); left damage speed 0.2428 in the literature (our 0.246 finite-time); L1069 corrected per GC2026–GC2029 — reports/rule30-quantum-gates-grounding.md.


- L1072: the degree law — Rule 30's t-step local rule has GF(2) degree exactly 2t − 1 (t ≥ 2), unique top monomial y_(−t+2)⋯y_t (t ≥ 3); hand proof via the white anti-diagonal (rightmost derivative), triangular pivots, and a z-frame induction — PROOF-SKETCH pending GPT; every lemma checked as an exact identity — reports/rule30-degree-law.md, PROOFS.md §G.

### GC2032 — L1072 degree law, carrying acceptance and survey calibration (2026-10-28)

[Review](reports/rule30-degree-law-gpt-review.md): PROVED after GPT's carrying read, degree2t-1 for t>=2 and
unique top monomial for t>=3. Independent symbolic audit frozen at9b0c93c8 passed; retained receipts by digest.
Small t2 label corrected. Standard AND-bound model specified; novelty unresolved. Essential right-input count
is exactly T, so an ANF dependence census is unnecessary. L1071's blanket quantum closure and future-right
independence claims are not accepted; explicit counterexample supplied. No fixed-seed prize inference.


- L1073: GC2032 corrections applied (degree-law report, L1071 grounding); degree-law novelty NOT FOUND in accessible sources, Deva 2026 SSRN unread (CAPTCHA); formal statement drafted in core Lean (kit is now Mathlib-free), type-checks, main theorem open — reports/wolfram-agents/submissions/degree-law/.


- L1074: degree-law Lean proof started — 524 lines core Lean, 49 theorems, no sorry, standard axioms; formal: Lemma 1 (white anti-diagonal), left permutivity, triangular elimination, coefficient cases (A)–(D); left: main parity (E) and assembly (F) — reports/wolfram-agents/submissions/degree-law/Rule30DegreeLaw.lean.

### GC2035 — visible structures leave hidden constraints (2026-10-28)

[Report and hand derivation](reports/rule30-structure-afterlife.md), frozen source28bd2072: six exact finite
completion families through8 steps, all controls pass. Triangle-origin parity at t6 awaits carrying read;
local decoder fails at t7 by overlapping supports. Rain/period-three recover fixed colours from relations.
Black cap: five-cell00010 forbidden despite every four-cell assignment being possible. Irregular control also
retains constraints. Data/figure by manifest digest; no entropy, universal frequency or permanent-memory claim.


- L1076: degree-law main parity (E) formally proved in Lean — main_parity: ∀ t ≥ 2, A t = true (905 lines, 78 theorems, no sorry, standard axioms), real-space route (behind-front damage, two-linear pivot, shift/clear, recA/recB, kernel-decided base); only the headline assembly (F) remains — reports/wolfram-agents/submissions/degree-law/Rule30DegreeLaw.lean.
- L1077: degree-law assembly (F) formal — degree_law (t ≥ 3, iff), degree_bound (t ≥ 2), degree_attained; 1,271 lines, 97 theorems, no sorry, standard axioms. PRIOR ART: the kit's equivalents/Rule30Equivalents/AlgebraicDegree.lean (2026-10-18) already proves the law in Lean, so known, reproved here; submission withdrawn — PRIOR-ART.md, reports/rule30-degree-law.md.
- L1079: this session's results compared with the kit — KNOWN, reproved here: L1054's period-parity equation (§8.27; kit TFunctionCycles.lift_iff, RightPeriods.S_rule), the seed echo (TFunctionCycles.Phi_cycle), L1071 §3's fair traces (kit Mixing); RELATED: L1069 (kit PeriodicPoints); NOT FOUND: the 101 lemma, universal start, tree of beginnings, 11011, T^64 classification, Lemma R — PRIOR-ART.md.
- L1080: the whole record compared with the kit and the portal — 15 of the 128 words in words-A/words-B were already excluded at submission (4 fully by the kit, 6 by the kit in a narrower scope than ours, 5 by our own c27323), 113 new; re-derived after the kit: GC1981/82/84 (Preimages), L1051/L1053/GC1998 (Odometer, antiperiod), L1002's tower, several zero-boundary restatements; §8.100 now PROVED via the kit's CenterFormulas.duhamel; lines 57–394 all predate the kit — PRIOR-ART.md.
- L1083: GC2038 (the cap 01111110 forbids 00010 at t8, via (P) and lemmas B1/B2) and GC2035 §1 (triangle-origin parity x_6(6) XOR x_6(7) = 1 XOR b) carry on Local's read — PROVED (two-party), local finite-context statements, no novelty claim — reports/rule30-cap-five-cell-proof.md, reports/rule30-structure-afterlife.md.

### GC2038 — hand explanation of cap00010 exclusion (2026-10-28)

[Proof and frozen checks](reports/rule30-cap-five-cell-proof.md): cap -> opposite pair -> constrained a1abc ->
local exclusions -> no00010 at t8. PROOF-SKETCH awaiting Local, finite exact certificate already held.1280
relaxed local controls pass; contrary0100010001101 produces00010 when the premise is removed. Any four-cell
support test misses the five-cell contradiction. Evidence packet and limits recorded; no enlarged census.

- GC2039: L1078–L1079 source review accepts known seed echo/parity/fair traces; distinguishes PeriodicPoints hypotheses; known_find now searches full Lean sources and detects changed existing files — reports/rule30-known-results-review.md. Five offline and seven live-index controls pass; cap proof still awaits Local.

- GC2040: [proof delivery audit](reports/wolfram-agents/PROOF-DELIVERY-AUDIT.md): all23 active registered portal submissions present (22 Lean Verified);21 downloadable sources byte-identical. Identified unsubmitted RootedReturn/TheoremB/pulse-law backlog; general arcs and recent hand results need specified reviews. Not a novelty certificate for every historical lemma.

- GC2043: [pulse-profile delivery specification](reports/wolfram-agents/PULSE-PROFILE-SPEC.md): reviewed base weight/debt identities assembled in left-diagonal coordinates; constant guards and birth-extension exclusions explicit. Not formalized or novelty-cleared; GPT writing, Local scope review requested.

- GC2045: [pulse core implementation status](reports/wolfram-agents/submissions/pulse-profiles/README.md):12 core Lean theorems pass first capped Intel compile; cyclic count and actual delay bridge still missing. No submission or current-kit validation.

- GC2047: [pulse cyclic weight proof](reports/wolfram-agents/submissions/pulse-profiles/README.md):23 core Lean declarations compile after one retained simplifier repair; seam/toggle identity proves exact source weights and heavy-source two-run corollary. Actual periodic hole/delay bridge remains pending.

- GC2049: [pulse-profile formal base](reports/wolfram-agents/submissions/pulse-profiles/README.md):32 core Lean declarations compile, including actual periodic pulse holes and first-black delay/budget bridge. Failed attempt retained. Local carrying read/current-kit validation and delivery fit pending; no finite-seed ancestry claim.

- GC2050: [TheoremB carrying review](reports/wolfram-agents/PAIRED-COLUMN-RUNS-GPT-REVIEW.md) accepts paired-column-runs source; period3 printed ether orientation must be corrected before delivery.
- GC2051: [general-arc review](reports/wolfram-agents/GENERAL-ARC-PROOF-REVIEW.md) recovers G2.2 second read and endpoint/return guards; hand proof carried, full formal artifact absent. Joint pulse/RootedReturn module agreed in principle; single posting owner to confirm.

- GC2052: actual-kit Rule30TemporalProfiles catalog draft adds generic indexed Child, explicit onset window and official evol/D weight/debt instantiations. L1087 carries/validates old standalone base; new wrapper uncompiled. Joint posting owner Local, GPT final reader; no compiler installation launched.

- GC2054: [joint temporal-profile essay](reports/wolfram-agents/submissions/pulse-profiles/essay.md) drafted for Local read/assembly; L1090 carries integrated module and reports checker pass after official import, now retained. Live8131b1 Lean Verified, public Lean byte-identical to retained source; remaining delivery backlog open.

- GC2055: L1091 assembled temporal-profile proof bodies match; canonical provenance/abstract/linter fixes prepared for Local regeneration. Qualitative walk consequence retained; bounded walk inference needs a finite-prefix argument.
- GC2056: [general-arc formal route](reports/wolfram-agents/GENERAL-ARC-FORMAL-ROUTE.md) supplies a determinant-spacing PROOF-SKETCH and exact pinned API map; avoids best approximation with sufficient digit threshold >2^(r+1)+1. Stronger carried theorem unchanged; new read/formal bridges pending.

- GC2057: [arc formal route](reports/wolfram-agents/GENERAL-ARC-FORMAL-ROUTE.md) adds signed real-lift endpoint cover (no separated-endpoint/circle API needed) and exact existing Rule30 repeat substitution C=L; hand interfaces await independent read.
- GC2058: retained Lean4.35 first_pulse regression and applied Local's tested modular fix. Reported persistent-kernel memory incident requires fresh-kernel, kernel-inclusive bounds/teardown before next notebook validation; final package read still pending.

- GC2059: [right-profile delivery specification](reports/wolfram-agents/RIGHT-PROFILE-DELIVERY-SPEC.md) freezes exact101/mod4/cascade/11011/universal-start scope beyond known lifting; no new run/formal artifact, Local formalization after joint posting.
- GC2060: final regenerated temporal-profile source/essay read accepted for sole-Local PR/posting; exact source digests retained, live portal outcome pending. L1094 carries arc endpoint cover and submitted repeat-constant route; determinant/formal wrapper still pending.

- GC2062: temporal-profiles a94f21/PR50 independently Lean Verified, public Lean/catalog byte matches and full notebook/verifier receipt retained; RootedReturn/pulse delivery done, remaining backlog open.
- GC2063: [arc-break component](reports/wolfram-agents/submissions/arc-codes/README.md) first capped Intel4.33.1 compile PASS, source/receipts retained; L1098 reports clean4.35 compatibility. Real rotation/Rule30 assembly still absent.
- GC2064: [right-profile carrying read](reports/wolfram-agents/RIGHT-PROFILE-GPT-REVIEW.md) accepts22-theorem draft in conditional-profile scope; Local essay/posting owner, final assembly pending. Prefix-Q letter/cascade/universal-start formal claims not added by this read.

- GC2065: [right-profile essay preflight](reports/wolfram-agents/RIGHT-PROFILE-ESSAY-PREFLIGHT.md) accepts source/scope and independently repaired illustration; final release read requests existing executed notebook/internal-handler classification, with original counterfactual and resource-enforcement limits explicit. No rerun requested.
- GC2066: [real determinant draft](reports/wolfram-agents/submissions/arc-codes/ArcDeterminantDraft.lean) writes Bezout/spacing/one-scale proofs as UNCOMPILED Mathlib source. Existing compatible project availability and bounded validation remain next; no dependency install or full arc theorem claimed.

- GC2067: keeping growing q_previous recovers the original >2^(r+1) arc threshold in the elementary route (new assembly PROOF-SKETCH); Nat margin lemma frozen for one bounded check. Actual-kit continuant draft uncompiled.
- GC2068: independently read retained failed/successful right-profile notebooks; both lack Message cells, but only repaired output has expected rows. Kernel67/source read supports manual release acceptance with lost-handler/resource limits explicit; sole-Local PR/posting cleared, no rerun.
- GC2069: Local's broad Mathlib load RSS_STOP retained; exact old real-proof body now uses checked narrow imports, with a new single bounded Local stage after posting. No higher cap or actual-continuant-wrapper run requested.

- GC2070: Nat previous-denominator margin lemma passes its sole capped Intel compile; exact source/receipts retained. Original threshold's sharper hand assembly still awaits carrying read/full formal wrapper.
- GC2071: right-profile7d47a9/PR51 independently Lean Verified (67 declarations); public Lean/catalog/notebook match accepted artifacts and full public receipt retained. Remaining universal-start/letter/cascade backlog not implicitly completed.
- GC2072: Local narrow-import attempt REFUSED before child launch; no auto retry. New smaller5GiB RSS/6GiB launch allocation explicitly frozen to fit measured headroom with1GiB margin, one Local attempt only.

- GC2073/L1105: minimal real-spacing component passes Local4.35 under GC2072 limits; universal-start design accepted with all-time cycle/minimality guards. Actual certificate source pending.
- GC2076: [genuine-break construction](reports/wolfram-agents/submissions/arc-codes/README.md) passes core Lean4.33.1 after retained induction-premise failure; derives strict breaks/recurrence from RepeatBound. Geometry/continued-fraction/Rule30 assembly still absent.
- GC2077: ArcCoverDraft composes actual breaks, lifted half-open interval returns and the one-scale determinant contradiction — UNCOMPILED/PROOF-SKETCH; construction of the cover and actual continuant/physical bridges remain open.
- GC2078/L1108: [universal-start source carrying read](reports/wolfram-agents/UNIVERSAL-START-SOURCE-REVIEW.md) accepts actual-diagonal/all-time/mask/minimality steps; cert unevaluated. One amended capped Local stage frozen with isolated outputs and exact checker headline guards.
- GC2079: ArcStepCodeDraft constructs the signed lifted cover from an explicit finite-step constancy interface — UNCOMPILED. GC2080 freezes one isolated3GiB Local integration check after certificate/other compute is idle; no CF/physical assembly claim.
- GC2081: universal-start first launch fails before Lean (missing Lake PATH); independently reviewed separate stage2 accepted, no cert outcome. Essay's unsupported individual-period monotonicity corrected.
- GC2082: [Lemma R scope](reports/wolfram-agents/LEMMA-R-DELIVERY-SCOPE.md) assigns Local preparation/GPT review; P2 all-positive-ring-size white/rain hand sketch pending read/prior-art clearance. No new census or bi-infinite extension.
- GC2083/L1111: all five arc components compile4.35 with17 standard-axiom prints; carrying read and CF/physical assembly pending. Certificate stage2 fails at package-root shadowing before body/cert; distinct-root probe needs actual diagnostic/JSON guards. Retained Lake lookup dependency fetch and overlay DISK_STOP are not proof outcomes.
- GC2084/L1113: finite-ring Phi²-fixed iff unshifted F-fixed (white/rain) hand proof now PROVED two-party; novelty/formal validation pending. Shift representatives can bring small-period ring cases inside PeriodicPoints. Universal stage3 accepted after actual renamed-root probe JSON read; cert still unevaluated.
- GC2085: ArcRotationDraft writes actual-continuant denominator/margin/large-digit scale and abstract finite-step repeat-bound exclusion — UNCOMPILED, depending on uncompiled ArcContinuantsDraft. Physical Rule30/restart/dependency validation remain.
- GC2086: certificate module compile RSS_STOP at4300336KiB; no completed cert/checker result. Frozen V0/V1/V16 probe reviewed as cost evidence only; a guarded hand route to a64-tick upper cycle is proposed, unvalidated, with no new run/cap increase.
- GC2087/L1114: exact16-way certificate split and explicit Nat binder repair independently read; one stage4 accepted, full outcome pending. Cost variants failed despite wrapper0; corrected split probes cover48 distinct cases only. Arc cover/step conditional composition carries; CF/physical assembly remains open.
- GC2088: actual window_jen_col repeat bridge and normalized actual-Rule30 rotation exclusion assembled as UNCOMPILED candidates. Includes closing clock sample/masked parity cases; eventual/endpoint restart and conventional code representation remain separate.
- GC2089/L1115: source32cd904f full256-case universal-start certificate and actual-evol headlines pass unchanged checker (258 replay/122 standard declarations), independently read. Final one-line tactic change carried; A2 final catalog/submission checks pending, with one5GiB submission stage amendment; no portal status yet.
- GC2090: [universal-start essay preflight](reports/wolfram-agents/UNIVERSAL-START-ESSAY-REVIEW.md) accepts precise prose and byte-identical17fdfbcb embed; historical stage4 source/attributed evidence retained immutably. Final A2/notebook/PR/portal remain pending.
- GC2091/L1116: final universal-start catalog/submission pass unchanged checker, independently read; notebook B not launched, pending lifecycle/resource and structural output guards. No additional certificate run or portal verdict.
- GC2092: direct-kernel StartProcess/RunProcess children escape its process group; group-only notebook containment refuted by retained r1 output despite exit0. Minimal core-import variant is body-identical but needs its own full check/essay freeze; no B launch.
- GC2093/L1119: core409e7c59 A3 and17 structural gates PASS, exact essay32672082 embed read; remaining signal/PID-fallback/temp-root corrections frozen, no full B yet.
- GC2094: new Intel lifecycle controls PASS; corrected tree/temp/process-count notebook B ready for one Local attempt after actual source adoption. Raw evidence retained; final artifact/portal still pending.
- GC2095: ArcTailBounds finite-prefix transfer C→C+2N and single-visit cutoff pass Intel4.33.1, five standard-axiom lemmas. Known G131/G132 integration; carrying/4.35/full CF/physical assembly remains pending.
- GC2096/L1121: B1 fails before build at bare-kernel argument binding; actual CommandLine probe supports one B2 with same bounds. ArcEndpointDraft actual irrational single-visit/eventual-code wrapper prepared UNCOMPILED; no extra compute or novelty claim.
- GC2097: ArcIntervalCodeDraft constructs StepCode from an actual periodic union of k half-open lifted intervals; concrete Rule30 candidate uses2k supplied labels/threshold2^(2k+1). All new real/full assembly UNCOMPILED, no extra job.
- GC2098/L1122/L1123: actual universal notebook442525ee manually accepted, exact409e7c59 native embed/six outputs/KernelChecked258; failed JSON/provenance limitations retained. Local delivery cleared, actual receipt pending. Tail/endpoint/interval hand steps carried; existing Lagrange.olean available, full integration uncompiled.
- GC2099: exact12-source/40-headline/four physical-headline current4.35 arc integration stage frozen after universal-start delivery,4GiB/600wall; prepared only, no new run or full-proof outcome claimed.
- GC2100: posted universal3ca86f/PR54 public notebook/catalogue/abstract/row independently byte-matched; external verifier still Lean Unverified06:35Z.
- GC2101/L1125: arc full integration CHILD_FAILED on closing |* token; first7 modules/24 prints plus3 Nat lemmas standard,3 dependent sorryAx prints rejected. One-space same-cap follow-up frozen; full assembly/checker pending.

- GC2102: universal3ca86f externally Lean Verified independently confirmed; public409e7c59 exact, four matching headlines/258 replay, immutable receipt retained. Human/merge pending.
- GC2103/L1127/L1128: [arc integration review](reports/wolfram-agents/ARC-INTEGRATION-GPT-REVIEW.md) accepts12-module4.35 pass and final semantic reads. Final module4 constants replayed; single-file whole-proof replay/package still pending. Mathlib goes directly to portal per current kit policy.
- GC2104/L1129: Lemma R planned encode/decode/P2 statements accepted in exact velocity+1/marked-walk scope; actual source/check pending, no new census.
- GC2105: [single-file arc stage](reports/wolfram-agents/submissions/arc-codes/SUBMISSION-SPEC.md) freezes exact56d226a6 source/whole-proof replay, same resource caps; transformation reproduces12 proof bodies. New source uncompiled; essay/abstract drafted, no notebook launch.
- GC2106/L1130: [actual Lemma R source read](reports/wolfram-agents/LEMMA-R-SOURCE-REVIEW.md) carries moving frame/inverses/P2 finite wrap. Graph interpretation needs positive P,m despite formal interface extending to0; release check/source freeze next.

- GC2107: [receipt repair](reports/wolfram-agents/NOTEBOOK-RECEIPT-REPAIR.md) prepares raw-WL/JSON-safe/nonempty-parsed receipt helper and14 frozen non-building controls; not run, no historical artifact rebuilt.
- GC2108/L1131/L1132: amended ring61fbff78/submission23a3be9f/wrappere5077849 read, one frozen core check accepted; source/prose carry, actual outcome pending.
- GC2109/L1132: exact single-file arc56d226a6 passes complete169-constant replay/90 standard declarations/four physical headlines on4.35; independently structured-evidence read. Executed notebook/portal pending.

- GC2110: [arc notebook stage](reports/wolfram-agents/submissions/arc-codes/NOTEBOOK-SPEC.md) freezes exact37bcdad8 essay/source binding, actual receipt-safe builder,6-output/169-kernel guards and18 prebuild fixtures; prepared unrun, Local source read next.
- GC2111/L1133: both ring forms59 replay/27 standard/eight matching headlines and14 receipt fixtures PASS independently read; actual executed notebooks and portal delivery pending.
- GC2112/L1134: exact ring essay0cefd19b embeds23a3be9f;18 output controls PASS independently read; actual receipt-safe B driver/source/spec accepted for one serialized Local build. Core PR direction agreed; executed artifact/public outcomes pending.
- GC2113/L1135/L1136: [ring final artifact review](reports/wolfram-agents/RING-ORBITS-FINAL-REVIEW.md) accepts exactbc043253 native notebook/23a3be9f source/six outputs/KernelChecked59 and real parsed receipt; immutable packet retained. Local sole prepared PR/portal delivery cleared, actual external outcome pending.
- GC2114/L1135: arc notebook RSS_STOP retained; post-stop writes rejected for release. TypeForm removal/static-source5-output repair selected, no cap increase/rerun until a new freeze. OwnedRSS is not system peak or proof of OOM.
- GC2115: exactarc0976ea3f essay/source56d226a6, TypeForm-free5-output/source-signature display and18 guards frozen for one same-cap B2; prepared unrun, no parent-stop override. Local's actual RunProcess/import excerpt read; ring public a96cee/PR56 independently checking next.
- GC2116: public ringa96cee independently Lean Verified59/eight exact headlines, exact public source/notebook and actualPR56 catalogue/import/row/body checked; immutable evidence retained, Human/merge pending.
- GC2117: [arc final artifact read](reports/wolfram-agents/ARC-NOTEBOOK-FINAL-REVIEW.md) accepts successfulf09c3cbd native/exact56d proof/four full static signatures/5outputs/KernelChecked169/real receipt within originalcap; sole-Local portal posting cleared with phase-explicit abstract, actual receipt/verifier pending.
- GC2118: [prefix-period bridge](reports/wolfram-agents/PREFIX-PERIOD-BRIDGE.md) resolves the hand inference from least whole-prefix doubling to antiperiod; explicit guarded11011 actual-Rule30 source prepared UNCOMPILED, new carrying read pending. Known lifting/stronger bounds and genuinep2 exception retained; no individual monotonicity assumed.

- GC2119: actual arc0ef6e2 independently public Lean Verified169/four matching headlines/no new axioms and exact accepted proof/notebook/clarified abstract; immutable public evidence retained, no Human Verified/catalogue PR. Named arc delivery closed, remaining backlog explicit.
- GC2120: [fringe/recurrence disposition](reports/wolfram-agents/FRINGE-RECURRENCE-DISPOSITION.md) matches original stripe family exactly, derives first-disagreement corollary from existing kit lemmas, and resolves GC727 sign interval -p<=s<=p-1. Common-left extension and supercausal count remain separate; Boyle–Lee injectivity guard retained.
- GC2121: [56-phase kick disposition](reports/wolfram-agents/KICK-DELIVERY-DISPOSITION.md) restores GC2043's reviewed record-only corollary decision, precise known masking comparison/phase guards and reopening condition; no standalone submission, implicit pulse delivery or new census.
- GC2122: outer recurrence/count packaging resolved by exact standard feedback-register and finite stable-image comparison; correct old hand specialization retained record-only, labelled rows distinguished from cycles. Critical s=p and common-left fringe remain separate; no new run/submission.
- GC2123/L1142: prefix bridge hand proof carried; source6eac3d79 still UNCOMPILED. Exact wrapperf0788d3c receipt guards strengthened/4 synthetic controls pass; one same-cap sole-Local stage released, no duplicate Intel run. Standard lifting explicitly credited.
- GC2124: complete prefix-bridge essay/860-character abstract drafts prepared with exact hypotheses, prior credit and exception; old artifacts preserved. Local sole validation/posting arrangement proposed for an extension, no notebook/source assembly/checker/upload outcome claimed.
- GC2125: L1144 actual4.35 compiler/6 exact standard-axiom outputs and mutantline90 independently read, physical prefix theorem registered in PROOFS. Full enforcement packet and original/sanitized mutant hash domains requested without rerun. L1145 eventual/single-seed versus age0/driven-right scope kept distinct.
- GC2126: [uniform recoding delivery scope](reports/wolfram-agents/UNIFORM-RECODING-DELIVERY-SCOPE.md) separates retained G135/G136 explicit251/250 finite horizon/reset bounds from delivered infinite Sturmian/large-digit arc exclusions; real older candidate remains, formalization/novelty pending, no new run.
- GC2127: [earlier PR51 source review](reports/wolfram-agents/PREFIX-PRIOR-ART-REVIEW.md) stops additional prefix-bridge packaging, preserves hand/compiler record and exact Nat/Int-prefix/credit distinctions. Full Clock/Bound source and selected reported replays read; relevant PR discussions now mandatory pre-work coverage, no new build/posting.
- GC2128: full actual bridge supervisor/text/source packet and both digest domains independently accepted; immutable evidence retained, no rerun, extra bridge delivery remains stopped. Local owns open-PR/head-source/comment index extension with controls; GPT reviewing, no competing implementation.

- GC2129–GC2130: [open-PR index review](reports/wolfram-agents/OPEN-PR-INDEX-REVIEW.md) freezes/reproduces4 silent-miss/cache-loss defects offline; REST pagination and old5 tests pass. Local repairing production; Intel has no gh, live REST acceptance deferred until the fixes. Actual failure packet retained.
- GC2131: existing uniform-horizon proof's carry-arc/mismatch distinction checked by hand; exact floor identity explains paired mismatches and validates h+1 offset, with golden q2 counter-control to a false direct mismatch-gap gloss. No new run/theorem/251-constant validation.
- GC2132: [open-PR index independent review](reports/wolfram-agents/OPEN-PR-INDEX-REVIEW.md): L1150 targeted fixes pass frozen regressions and Intel no-gh live controls; initial211PR baseline distinguished from new results, coverage boundaries retained.
- GC2133: [uniform-horizon exact carrying interface](reports/wolfram-agents/UNIFORM-RECODING-DELIVERY-SCOPE.md): finite deadlines, denominator bootstrap, coding width and physical restart margins; renewed Local read requested before any build.
- GC2134: [repeat-debt / first-repetition dictionary and prior art](reports/wolfram-agents/UNIFORM-RECODING-DELIVERY-SCOPE.md): exact inclusive-index offsets, known qualitative obstruction and compactness sketch; explicit251/250 horizon remains pending.
- GC2135: [finite-horizon carrying acceptance and dependency qualification](reports/wolfram-agents/UNIFORM-RECODING-DELIVERY-SCOPE.md): L1151 carries exact claims; sharp adjacent-convergent return lemma still needs explicit formal interface, older Bezout guard alone is insufficient.
- GC2136: [finite-prefix formal component plan](reports/wolfram-agents/FINITE-HORIZON-COMPONENT-PLAN.md), six uncompiled core deadline/carry/growth heads with explicit horizon guard; one Intel check frozen, full rotation theorem separate.
- GC2137: [finite-prefix component first-run outcome](reports/wolfram-agents/FINITE-HORIZON-COMPONENT-PLAN.md): six exact core heads compile Intel4.33.1 with standard axioms, full capped receipt retained; complete rotation horizon remains separate.
- GC2138: [sharp adjacent-return staging review](reports/wolfram-agents/SHARP-ADJACENT-SOURCE-REVIEW.md): five uncompiled Mathlib proof/control heads, proposed sole-Local4.35 check and caps; no actual continuants or new theorem claim.
- GC2139: [noncircular denominator arithmetic plan](reports/wolfram-agents/DENOMINATOR-BOOTSTRAP-PLAN.md), three uncompiled core heads with explicit finite guards/shift premises; one bounded Intel check frozen.
- GC2140: [guarded bootstrap first-run result](reports/wolfram-agents/DENOMINATOR-BOOTSTRAP-PLAN.md): three core heads compile Intel4.33.1, explicit124-index margin and full receipt retained; geometric premises remain explicit.
- GC2141: [sharp adjacent-return full4.35 acceptance](reports/wolfram-agents/SHARP-ADJACENT-SOURCE-REVIEW.md), exact5 heads/std axioms and full resource packet independently read; byte-domain qualification retained, no full-horizon claim.
- GC2142: [actual mechanical carry staging source/review](reports/wolfram-agents/MECHANICAL-CARRY-SOURCE-REVIEW.md): seven uncompiled floor/half-open-arc heads, proposed16-head4.35 check with existing core components; explicit integer lifts avoid a nearest-integer norm API.
- GC2143: [actual carry-return spacing source](reports/wolfram-agents/MECHANICAL-CARRY-SOURCE-REVIEW.md): three uncompiled dependent heads using explicit phase-floor numerator and sharp return; no added run or actual-continuant claim.
- GC2144: [actual continuant-source adapters](reports/wolfram-agents/ACTUAL-CONTINUANT-SOURCE-REVIEW.md): five+two uncompiled actual-data/finite-growth heads; exact n+2 determinant/error indexing, M5 gate preserved, no added run.
- GC2145: [current4.35 failure and targeted carry repair](reports/wolfram-agents/MECHANICAL-CARRY-REPAIR-PLAN.md): nine core heads independently accepted; seven carry heads rejected with sorryAx; explicit real-floor import plus four deprecation-name fixes, new7-only check proposed.
- GC2146: [CL640 synthesis scope review](reports/wolfram-agents/CL640-GPT-SCOPE-REVIEW.md): six exact orientation/quantifier/status/inclusion/finite-limit corrections, plus conditional certified14 entropy-gap route; offered research jobs remain held.
- GC2147: [carry repair refined before execution](reports/wolfram-agents/MECHANICAL-CARRY-REPAIR-PLAN.md): L1161's direct conditional iff proof replaces the diagnosed simp hazard; same7 heads/caps, d73 candidate never run.
- GC2148: [actual denominator threshold/coefficient staging](reports/wolfram-agents/ACTUAL-CONTINUANT-SOURCE-REVIEW.md): four+five uncompiled core/actual sequence heads, no least-index operator or added run; unboundedness comes from kit contQ_ge.
- GC2149: [repaired carry7 full4.35 acceptance](reports/wolfram-agents/MECHANICAL-CARRY-REPAIR-PLAN.md): exact source/output and full parent packet verified;21 component heads compile4.35, original failure retained, full horizon still incomplete.

- GC2150: [finite-horizon block closure/module plan](reports/wolfram-agents/ACTUAL-CONTINUANT-SOURCE-REVIEW.md):
  L1164 adapters carried, selection9 still pending;21 component heads4.35, full theorem unfinished.
- GC2151–GC2153: [DQ-024 edge-density account](reports/rule30-edge-density-account.md): published Rowland2006
  J40=92 recovered; no duplicate run. COMPUTED20pairs:00resource can collapse or increase. Exact10
  decrement and arbitrary local collapse controls PROOF-SKETCH; missing sublinear00-minus11 count/root ancestry.

- GC2154/GC2155: [whole-white-run resource decomposition](reports/rule30-edge-density-account.md):
  third-gate filter excludes earlier synthetic control; COMPUTED256-cycle47fills cancel first two
  root coefficients, explain127->1. Known gate/geometric mechanisms, hand composition awaitsLocal; limitOPEN.

- GC2156: [three-class edge-cancellation witness and projection boundary](reports/rule30-edge-density-account.md):
  retained47fills compress modulo(1+X)^3; standard XOR-linear full-space shift/OR quotient is zero
  orinjective (PROOF-SKETCH). Generic parity closure parked; actual-seed nonlinear correlations open.

- GC2157: [edge-odometer dimension/energy dictionary](reports/rule30-edge-odometer-dimension.md):
  exact2^e_j prefix count, free phase labels, distance2^(-J_k-1), Hausdorff dimensionliminf e_j/j.
  Standard tree argument plus known half bound gives zero critical1/2-capacity; subcritical energy
  and dimension1/2 remainOPEN. PROOF-SKETCH awaitingLocal, no dynamics or new portal package.

- GC2158: [exact next-gate run restriction](reports/rule30-edge-density-account.md#gc2158-one-more-upstream-gate-leaves-choices-only-at-isolated-black-cells):
  011 forces neighbourflip; non-singletonblackruns link fill bits, exact relaxed2^S choicecount.
  RetainedR93/S69 still permits all3lowcoefficients. PROOF-SKETCH, no new CA run or actual-root
  counterexample; gate-by-gate ladder parked pending a repeatable component/root-profile law.

- GC2159: [signed opposite-carry separation](reports/wolfram-agents/ACTUAL-CONTINUANT-SOURCE-REVIEW.md#gc2159-exact-opposite-scale-separation-now-has-carrying-source):
  adjacent-basis strip forces exact negative return; actual half-open carry/continuant instantiation
  prepared in3 UNCOMPILED files/13heads. PROOF-SKETCH awaitingLocal; older21passing heads unchanged,
  full251 assembly/integration incomplete. No compiler run or M5 wake.

- GC2160/GC2161: owner resumed Local12:54; selection9 and separation13 carrying reads accepted.
  Three requested atom/cast normalizations applied, sources UNCOMPILED; stage A13modules/53heads
  agreed at frozen wrapper/caps, actual outcome pending. Local owns final assembly/integration,
  GPT separation/review. No duplicate build or silent stage B widening.

- GC2162: [full stage-A packet acceptance](reports/wolfram-agents/ACTUAL-CONTINUANT-SOURCE-REVIEW.md#gc2162-full-stage-a-evidence-independently-accepted):
  exact13sources/53standard heads/43samples independently read; Lean4.35 PASS, immutable02f5db61.
  Original/sanitized launcher byte domains retained. B5files/22heads uncompiled; reuse hash-verified
  A objects, no automatic repeat. Local irrational assembly; GPT finite-prefix perturbation/recoding.

- GC2163: [irrational/recoded source carrying read](reports/wolfram-agents/ACTUAL-CONTINUANT-SOURCE-REVIEW.md#gc2163-complete-irrational-assembly-and-recoding-draft-carried-core-import-fixes-applied):
  Uniform4/Recoded6 mathematically accepted; core selection fixed87e28fe7. Release/past-development
  provenance still separate. No duplicate recoding source; GPT explicit-constant literature review.

- GC2165: [physical horizon carrying read](reports/wolfram-agents/ACTUAL-CONTINUANT-SOURCE-REVIEW.md#gc2165-physical-restart-source-carried-all-three-statement-sources-read):
  restart10 at79fe5a74 accepted, exact black witness/radius/endpoint recursions. All three statement
  sources second-read; B6/C4 release stages, prior art and submission assembly still pending.

- GC2167/GC2169: [complete modular horizon validation](reports/wolfram-agents/ACTUAL-CONTINUANT-SOURCE-REVIEW.md#gc2169-full-stage-c-packet-independently-accepted-modular-proof-complete):
  full retained M5 A/B/C packets independently accepted,23modules/99standard reports4.35; no GPT rebuild.
  Single-file official replay and delivery artifacts remain pending, Local sole posting owner.
- GC2168: [quantitative horizon prior-art disposition](reports/wolfram-agents/UNIFORM-RECODING-DELIVERY-SCOPE.md#gc2168-quantitative-prior-art-disposition-for-delivery):
  primary finite Sturmian estimates and exact prefix-length dictionary credited; useful explicit251/250/503
  formal package retained, with no priority/sharpness claim; public two-back/first-defect statements read.


- GC2180/GC2188: [official horizon replay and notebook repair review](reports/wolfram-agents/ACTUAL-CONTINUANT-SOURCE-REVIEW.md):
  unchanged checker accepts791e45ed/324replayed/eight heads. First notebook FAILED at hidden .rec name; full packet
  retained, one exact IncludeInternal repair accepted at unchanged caps, actual repaired outcome/posting pending.
- GC2181/GC2184/L1188: [repeat-index and shifted-derivative interfaces](reports/wolfram-agents/UNIFORM-RECODING-DELIVERY-SCOPE.md):
  two-party hand offsets carried; Local's paper convention relies on GPT's primary quote. No novelty clearance.
- GC2187/GC2189: [phase-zero candidate and half-phase relative gap](reports/wolfram-agents/UNIFORM-RECODING-DELIVERY-SCOPE.md):
  phasezero rep2 iff eventualtwos/oddnumerators is PROVED hand/two-party L1192. Old halfphase witnesses give
  rep<=(3+6sqrt2)/7<5/3; quantitative consequence also PROOF-SKETCH, no Rule30 realization or novel-export claim.

- GC2190: [final horizon notebook acceptance](reports/wolfram-agents/ACTUAL-CONTINUANT-SOURCE-REVIEW.md#gc2190-repaired-native-notebook-and-full-enforcement-evidence-accepted-for-sole-local-posting):
  actualff423106/source791/fiveoutputs/eight standard sets/KernelChecked324/73samples accepted. Local sole posting
  cleared; public submission/verification pending. Both tiny-probe full receipts read with LEFTOVER_CLEANED retained.

- GC2191: [new public finite-support source review](reports/wolfram-agents/UNIFORM-RECODING-DELIVERY-SCOPE.md#gc2191-two-current-public-finite-support-proofs-do-not-replace-the-quantitative-horizon):
 99db76 supersedesf98be4, externally verified37;23ac1b frontier verified136, physical exclusion covered by known
 period1/finite propagation. Both full sources read; exact numeric frontier export not claimed known. No horizon overlap.

- GC2192/L1190: [horizon public delivery](reports/wolfram-agents/ACTUAL-CONTINUANT-SOURCE-REVIEW.md#gc2192-horizon-publicly-delivered-and-externally-lean-verified-exact-artifact-identity-accepted):
 dc3d17 Lean Verified324/eight standard heads; exact public791e45ed proof/ff423106 notebook/fields matched.
 Named delivery complete; Human Verified and remaining wider-code backlog separate. No prize claim.

- GC2193/L1192: [exact versus one-error rotation repetitions](reports/wolfram-agents/UNIFORM-RECODING-DELIVERY-SCOPE.md#gc2193-exact-repetition-is-classified-at-phase-zero-but-one-error-admits-arbitrarily-long-near-cubes):
  phasezero classification carried; unbounded rep1 known via Nguyen7.4/Bugeaud–Kim10.3, all phases. One-bit near-cube
  prefixes at unbounded silver scales PROVED hand/two-party L1193; no robust additive repeat bound, CA realization or novelty claim.

- GC2194: [one-substitution repair endpoint](reports/wolfram-agents/UNIFORM-RECODING-DELIVERY-SCOPE.md#gc2194-the-one-bit-repair-has-an-exact-endpoint-cube-freeness-is-a-known-separate-constraint):
  exact maximum2q_next letters/limit2+sqrt2 copies PROVED hand/two-party L1195. Ordinary silver cube-freeness KNOWN via2020
  Prop34; rep2 does not imply cube-free. Generic anchored-prior-art search parked pending a named relevant source.

- GC2195/L1194: [edge-density accounting review](reports/rule30-edge-density-account.md#gc2195-l1194-carrying-scope-and-the-binary-pair-pointer):
  identities/temporal controls hand-carried; exact binary(1,0) countdown and actual Path-extension target clarified.
  Whole-root stack, half-density and wall bridge remain open; no new run.

- GC2197: [conditional alternating-run binomial mask](reports/wolfram-agents/RIGHT-PROFILE-DELIVERY-SPEC.md#gc2197-a-binomial-mask-for-every-finite-alternating-run):
  (10)^m1 nextflag=[mu=m]=XOR over t AND m=0, PROVED hand/two-party L1197; m<=mu<=M-2 supplies guards.
  Known countdown/Lucas application; no occurrence/00/lower-density theorem. L1195/L1196 DQ024 reads accepted.

- GC2198: [guarded110 overlap shift law](reports/wolfram-agents/RIGHT-PROFILE-DELIVERY-SPEC.md#gc2198-the110-overlap-law-needs-its-small-period-constant):
  unguarded product-only shorthand REFUTED at actualq2; add parity(q/2), corrected PROVED hand/two-party L1199. Eight-tick
  hand counterexample retained; no change to delivered101 law, density or occurrence claims.

- GC2200: [110 ordered reader and recent seed-bit invariance](reports/wolfram-agents/RIGHT-PROFILE-DELIVERY-SPEC.md#gc2200-the110-joint-statistic-is-ordered-history-insensitive-to-two-recent-start-bits):
  overlap is a-only events against b-prefix parity; b/c start-phase invariance PROVED hand/two-party L1201. Full older profiles
  still supplied; no closed depth state, frequency/density, older-bit or later-flag theorem.

- GC2201: [power-of-two closing length](reports/wolfram-agents/RIGHT-PROFILE-DELIVERY-SPEC.md#gc2201-a-preceding-doubling-forces-a-power-of-two-closing-length):
  genuine1(10)^m11 requires m+1 dyadic;1101011 forbidden PROOF-SKETCH. Known anti-resource/mask corollary,
  no occurrence/density theorem. CL642 A/B hand read scoped to single-seed least-cycle parities.

- GC2203/GC2205: [overnight plan](reports/GPT-OVERNIGHT-20261029.md) and [ruler-closure count](reports/wolfram-agents/RIGHT-PROFILE-DELIVERY-SPEC.md#gc2205-exceptional-ruler-closures-have-a-deterministic-sparse-count).
  CL645/GC2201 closing-length law carried; new successive-exponent/tower count PROOF-SKETCH. One fixed root control PASS, no density inference. New a4691a carrying review is the next active step; Local/Cloud offline.

- GC2206–2207: complete a4691a backward-operator source/import/PR45 review; G122/G141/GC691 tail mechanism credited, strict-width and projection guards; algebraic class count PROOF-SKETCH with one independent finite implementation control PASS — [review and receipts](reports/rule30-primitive-source-review.md). No survivor classification or certificate for97 inferred.

- GC2208–2209: [clocked-gap phase/boundary interface](reports/rule30-clocked-gap-interface.md), PROOF-SKETCH, and recovered L323/L590/GC1009/1011/SLC prior art. Fixed919-state audit PASS: shortest rejected rooted macro SSLSSLS (7gaps, already known);125/128 and242/256 graph acceptances at7/8; both old42cuts missed. Literal-window controls pass; no actual-language completeness, new SAT, Lean replay or new submission.

- GC2210–2211: [guarded00 phase law](reports/rule30-zero-pair-phase.md), PROOF-SKETCH; exact admissibility beta*parity(a)=0, affine next flag on00, separate2H flag on01. Eight fixed controls PASS, retained root256 A=B=0; no census or density inference. Next different representation: actual Phi difference quotient and the primary T-function regularity hypotheses.

- GC2212: [right-edge finite-precision regularity](reports/rule30-edge-regularity.md), PROOF-SKETCH. Modulo 4 differentiability exactly on Z, modulo 8 exactly on nonnegative integers, modulo 16 nowhere. Exact arbitrary-odd-increment quotient includes carries. Direct uniformly differentiable/transitive theorem transfer is closed; finite-scale return cancellation is the next hand discriminator, no computation frozen.

- GC2213: [return quotient and fixed-iterate obstruction](reports/rule30-edge-regularity.md#gc2213-the-return-quotient-is-the-known-delayed-phase-coefficient), PROOF-SKETCH. Return product recovers GC2014/L1070 parity; no fixed positive iterate restores uniform-mod4 regularity along root states. New PR57 source read begins after complete00:10:27Z refresh.

- GC2214: [PR57 source/evidence review and periodic-driver thinning](reports/rule30-periodic-mask-review.md). Exact transport/consistency/conditional bridge accepted by hand; external28-constant/10-headline replay inspected, not rerun. Solo two-class reduction leaves one pulse per period or no isolated black cells. Strong exclusion and physical realization remain open.

- GC2215: [pulse scope and actual ZBL countercontrol](reports/rule30-periodic-mask-review.md#gc2215-the-small-period-targets-are-already-named-and-a-countercontrol). Small targets recover open Q01/Q001/C3w; an aperiodic trace with P-step black pins is realized only by an infinite start in the explicit example. Solo sketch, no exclusion. Change to PR53 finite reset source review.


- GC2216: [reset-free source/evidence and finite-parent meaning](reports/rule30-reset-free-review.md). PR53 exact three-row/five-row theorems carried;335-constant/40-headline author replay inspected and retained. Solo reset-free iff one finite parent, three-row branching consequence and exact13-tree countercontrol. Reset occurrence does not ensure continuing finite past; no new experiment or independent acceptance of the consequence.

- GC2218: [finite zero-wall predecessor counts](reports/rule30-reset-free-review.md#gc2218-the-fixed-control-passed-exact-finite-word-counts-by-hand). Eight-case GC2217 control PASS with retained actual receipts. Solo all-width recurrence A(z)=(1+z^2)/(1-z-2z^3), support-growth double count and3/4,0,1/4 finite-word proportions. Classical transfer methods credited; no orbit law or novelty clearance. Generic inverse descent and unchanged ordered-profile closure parked.

- GC2219: [two-substitution silver-word endpoint](reports/wolfram-agents/UNIFORM-RECODING-DELIVERY-SCOPE.md#gc2219-two-substitutions-have-an-exact-endpoint-set-by-a-residue-chain), solo PROOF-SKETCH. Same convergent lagQ as GC2194; optimum2q_next+Q, next letter needs three edits although original shifted mismatch count stays two. Known majority-per-residue method, exact signed-arc guard, no computation/priority/Rule30 realization. No automatic edit-budget hierarchy.

- GC2220: [uniform spatial-window half-rate and Assouad upper bound](reports/rule30-edge-odometer-dimension.md#gc2220-the-known-accounting-bound-restarts-in-every-spatial-window), solo PROOF-SKETCH. Restarting the known kit Path preserves its resource and shifts nu; even-window rounding handles all starts. Exact prefix fibers give dim_Assouad(K)<=1/2. No density equality or bounded critical excess; next a ruler-only symbolic control, no computation.

- GC2221: [ruler-law control with unbounded critical excess](reports/rule30-edge-odometer-dimension.md#gc2221-the-ruler-law-permits-unbounded-critical-excess), solo PROOF-SKETCH. Every closing-law occurrence passes while signed excess grows one per tower-separated shared11 block and density tends to1/2. Compatible with any given actual prefix ending00 only in the stated symbolic sense. Upper-bound-only route parked; PR48 actual source review next.

- GC2222: [PR48 complete carrying source/evidence review](reports/rule30-edge-clock-drop-review.md), exact head865e77a5d11a and4112e112 proof. All-time edge restrictions and free/finite imitation guards accepted;26 archive files retained, author99constants/13headlines inspected, no replay or experiment. Eight SAT targets UNKNOWN. Retained67 first-deviation times suggest an unproved eight-tick/twelve-depth invasion law, next hand target after prior-art checks.

- GC2223: [guarded carrier invasion](reports/rule30-carrier-invasion.md), solo PROOF-SKETCH. A closed101/1011/100/100 front advances6depths/4ticks and explains PR48's exact all-n first-failure formula, with separate n0 entrance. Known ring/front machinery credited. One local/table self-check frozen before launch; no root00 or density result.

- GC2224: [carrier control outcome](reports/rule30-carrier-invasion.md#gc2224-the-frozen-control-passed-once), PASS once, literal/packed oracles and omitted-guard witness;0.04childCPU,14.4MB peakRSS. Universal proof remains solo sketch. Next derive guarded001 avoidance for arbitrary finite older prefixes, without a new sample or stage.

- GC2225: [exact guard map and capture scope](reports/rule30-carrier-invasion.md#gc2225-exact-guard-map-and-the-remaining-capture-question), solo PROOF-SKETCH. Phase-A speed is independent of older bits; both101/111 are closed,001 has an exact one/two-cycle avoidance condition and a hand12tick finite-prefix control. No capture theorem or justified standard-clock transfer. Capture parked; next PR47 carrying source/evidence review.

- GC2226: [PR47 complete source/evidence review](reports/rule30-synchronizing-carrier-review.md), head744c1091. Six modules carried; fixed-three-bit and all-length periodic-tail scopes distinguished. Author583replayed/309declared/63headlines,54-file archive identities checked, no GPT replay. No finite ancestry or generic legal-future theorem. Next inspect the already-retained five-periodic reset-free core.


- GC2227: [known five-core comparison](reports/rule30-reset-free-review.md#gc2227-the-nine-state-core-is-the-known-five-cycle-plus-constants) and [shifted-Path source/freeze](reports/rule30-edge-odometer-dimension.md#gc2227-exact-source-lean-draft-and-one-frozen-development-check). Whole-row versus tail scope resolved; two arithmetic Lean drafts still uncompiled, one4.33.1 development stage frozen,4.35 and independent review pending.


- GC2228: [window development stop](reports/rule30-edge-odometer-dimension.md#gc2228-the-development-check-stopped-at-its-memory-cap), RSS cap enforced/cleanup complete/new drafts unattempted; and [PR58 source carrying read](reports/rule30-group-cocycle-review.md), exact homogeneous invertible finite-support scope accepted, raw author evidence still pending.


- GC2229: [PR58 complete archive/replay review](reports/rule30-group-cocycle-review.md#gc2229-complete-archive-and-replay-review),101payload hashes and exact inputs checked; author186/5 core and37/3 boundary replay accepted in scope. No GPT compile; portable resource and notebook summary limits explicit. Known singular alternating-ring recognizer explained by hand; Parry1997 full text is an optional access dependency.
- GC2230: [rooted endpoint control](reports/rule30-profile-boundary-control.md), solo PROOF-SKETCH. Seed93 realizes endpoint21 with predecessor150, while an external nonwhite infinite past gives predecessor21. Endpoint realizability is weaker than boundary restrictions on both candidate histories; known finite graph path, next clock16, no new census or white-root uniqueness refutation.

- GC2231: [full-line small clocks](reports/rule30-full-line-small-clocks.md), solo PROOF-SKETCH. Known G258 plus parity explains Fix(Phi^4)=Fix(Phi^2), recovering the known q4 core and GC732 white/rain/interface classification. Full-line paths, ring cycles and white-root histories distinguished; higher-clock transient obstruction remains open. No new computation. Stale GC1996 hand-D alternative parked; next PR33 finite eight-return carrying read.

- GC2232: [PR33 finite eight-return source/evidence](reports/rule30-finite-return-eight-review.md), all-width three-cell deletion and exact first-discrepancy delay carried. Current source09aa298b reviewed; current128/four-headline replay reported, older26/three-headline raw replay separately retained. Selected19of235 payloads checked, no GPT compile or safety-completeness inference.
- GC2233: [even two-run profile law](reports/rule30-full-line-small-clocks.md#gc2233-an-even-two-run-profile-forces-the-next-period-to-double), solo PROOF-SKETCH. Actual older profiles equal the transition mask and the next least period doubles; for q>4 the period pattern is q,q,q,2q. No root occurrence, density or general00 conclusion. Remaining q8 case list parked; next signed-height source read.

- GC2234: [oriented signed-height review](reports/rule30-oriented-height-review.md), exact safety iff correctly oriented two-level height, known/carried for arbitrary drivers.43/8 and13/3 raw replay/headline evidence retained; no GPT replay or finite-ancestry restriction.
- GC2235: [isolated-transition core-only freeze](reports/rule30-full-line-small-clocks.md#gc2235-one-frozen-core-only-ancestor-check). Three recurrences force both older profiles to equal the isolated transition mask. Eight UNCOMPILED heads; one bounded4.33.1 development stage frozen, no Window retry or period theorem claimed.

- GC2236: [core-stage actual failure](reports/rule30-full-line-small-clocks.md#gc2236-the-core-check-stopped-on-an-elaboration-error). Final wrapper rewrite failed;7helpers report empty axioms but final head has sorryAx. Negative/oracle unattempted; full bounded failure receipts retained, no rerun or cap change.
- GC2237: [finite reset-excursion counterexample](reports/rule30-reset-excursion-review.md), known/carried. Equal8tick traces/reset do not determine parent segment; unsafe00prefix prevents a safety-completeness inference. Exact6/1 author replay/headline evidence retained, no GPT run.

- GC2238: [run-count next-period law](reports/rule30-run-period-law.md), solo PROOF-SKETCH. No singleton runs imply exact input-period preservation via neighbouring AND inverse; next period depends on black-count plus run-count parity. Known root rule credited; no ancestry occurrence or density.
- GC2239: [transition-cover source/evidence review](reports/rule30-transition-cover-review.md), exact reversed-derivative relaxation carried,37/3 author replay/headlines retained. Explicit0001 chain violates shared OR equations; no new compiler or universal ancestry inference. Next separately prepare changed core-only source, with freeze required before any run.

- GC2240–2241: [explicit core repair and inverse validation](reports/rule30-run-period-law.md#gc2241-the-repaired-core-and-inverse-pass-the-development-check),13empty-axiom heads on4.33.1 plus negative/16/8 controls pass once; old failure retained, official4.35/independent review absent.
- GC2242–2243: [antiperiod-height source and free-partner converse](reports/rule30-antiperiod-height-review.md), external26/6 replay/headline review carried. Solo binary-track lift constructs some safe antiperiodic partner iff zero drift/height diameter<=2; actual ancestry absent. Fixed P2/4/6 independent existence diagnostic is next, not yet frozen or launched.

- GC2244–2245: [fixed free-partner pilot](reports/rule30-antiperiod-height-review.md#gc2245-the-fixed-pilot-passes-once), all84P2/4/6drivers and8736partner/initial cases pass once; deliberate endpoint-exchange mutant fails. Full receipts retained, no periodic pressure sample for this short job, no rerun.
- GC2246: [exact free-partner count](reports/rule30-antiperiod-height-review.md#gc2246-count-all-free-partners-by-excursion-choices), solo PROOF-SKETCH; safe pairs2^(P-k+2-D) with guarded special cases.84retained counts agree, no new dynamics. Next hand question is the phase-anchored driver-language transfer matrix, not root density.

- GC2247: [exact free-partner driver-language count](reports/rule30-free-partner-language.md), solo PROOF-SKETCH. trace(M2^m)-trace(M1^m), standard strip counting plus overlap correction; exponentially small fraction of arbitrary length2m words, no actual-root sampling implication. No new enumeration. Next exact D3/ReturnComplete carrying interface.

- GC2248: [D3/completeness carrying review](reports/rule30-d3-completeness-review.md), exact conditional equivalence and short-extension/reader dependencies;529retained author replay declarations20headlines, no GPT replay. Known1000010 passes EightWindow but fails11–12. Both completeness sides remain open; next compare the three-prefix obstruction with the older D record before reopening.

- GC2249: [D3 free-strip obstruction and wrapper disposition](reports/rule30-d3-completeness-review.md#gc2249-the-free-boundary-obstruction-survives-simultaneous-failure): fixed256-equation audit of known period32 witness passes; simultaneous predecessor failure is not a white-root contradiction. Local route parked; PR52 carrying review next.

- GC2250: [PR52 arbitrary-future past closing](reports/rule30-gate-past-closing-review.md), five-module carrying read and retained3057/37author replay, exact source/archive bindings. Any eventual closing rate suffices for the conditional finite-row exclusion; AllPastClosing/FiniteCoverFamily open. Next finite-cover completeness via locality/compactness, no census.

- GC2251: [exact finite-cover completeness](reports/rule30-gate-past-closing-review.md#gc2251-the-finite-cover-format-is-complete-for-qualitative-closing), solo PROOF-SKETCH. At fixed n, qualitative closing iff finite PR52 trees iff a uniform cutoff. Outer locality repairs the open-witness gap; canonical-table, empty/singleton/n0 and endpoint guards explicit. All-length assertion remains open.

- GC2252: [first common-tail reset disposition](reports/rule30-gate-past-closing-review.md#gc2252-the-first-tail-merger-recovers-the-existing-reset-obstruction), known G13/one-versus-five gap; [frozen named-carrier q16 reachability pilot](reports/rule30-carrier-reach-pilot.md), not yet run.

- GC2253: [carrier pilot failure and endpoint phase correction](reports/rule30-carrier-reach-pilot.md#gc2253-the-control-caught-an-unjustified-extension-of-the-proved-endpoint). No traversal ran. PR48's finite endpoint forces16next; the other phase matches PR58's full-line rain path. Failure/source/receipts retained, no rerun.
- CL649 (Cloud, 2026-10-30): deep-question dialogue with the owner on fuel: no conservation (Lowry's theorem), a one-way law instead (`per_mono_all`, `e_step` gear ratios 1:1 and 2:1), doubling consumes the supplier (`half_black`). Block 4 measured: no pressure from runs of unspent wheels (f(m) flat near 1/2, 64 seeds); zero runs geometric except a cluster of five ten-wheel plateaus; the single seed's many-wheels-at-once events are the J_k synchrony (prior art §8.73). Probe `edge_zero_runs.py`.
- CL650 (Cloud, 2026-10-30): the owner's reversal. Exact law: reversing wheel k changes E_(k+1) iff wheel k-1 has odd weight over the period (PROOF-SKETCH, 59 of 59; read owed). Plateaus fragile downstream (43 of 53), made of even-weight suppliers; one reversal built a fourteen-wheel plateau. Run A (256 48-bit seeds): the ten-wheel peak was chance; mild heavy tail. Probes `edge_reverse.c`, `edge_plateau_tail.py`.
- CL651 (Cloud, 2026-10-30): run B (24-bit seeds to 68 wheels): no plateau longer than nine in the zero-setting region, P16 held but consistent with chance; the peak at nine is gone in the pooled count. Greedy extension of the fourteen-wheel chain running (Block 6).
- CL652 (Cloud, 2026-10-30): greedy reversals give 34 wheels at one period (P19 held, P20 refuted: steered, not starved); the owner's three breaks with exact hand rules (P21, P23, P25 all held at every case); single suppliers double at about 0.1 because own weight parity is rarely odd; the doubling is born in the overlap; rule 150's edge map logarithmic, rule 120's at rule 30's density (new, COMPUTED). Handover to GPT. Probes `edge_break.c`, `edge_break_analysis.py`, `edge_greedy.py`.

- GC2256–GC2258: [Boolean edge-clock comparison](reports/quadratic-edge-clock-transfer.md): four Cloud break laws carried with period-one correction; one80case finite control passed; solo all16gate half-rate transfer, affine logarithmic bound and exact AND prefix-branch label. Known domino formula credited; period histories agree before diverging, no density equality. Two-term perturbation ansatz parked.
- CL653 (Cloud, 2026-10-30): GPT's GC2255 to GC2258 assessed: five corrections taken (even-period guard on the reversal law; whole-prefix weights; rule 120 in the 4 October sibling probe; finite frequencies are not a law; AND's special seeds); GC2258's seed 3 / 35 histories reproduced; the gate-generic difference identity carried; the kit's Path confirmed gate-free; the lifting letter read as the all-ones binomial coefficient, the overlap as complementary support pairs (Nersissian). Recommends a gate-parametrised DifferenceOrder lemma for Local and a bounded support question for GPT.
- CL654 (Cloud, 2026-10-30): curiosity block: sixteen-gate census (two product gates choke, six odometer-like, eight affine logarithmic); left wheels settle at 1.27 steps per wheel with periods at most 16 to wheel 1024 (front prediction refuted, asymmetry quantified); right wheels' binomial supports dense, ratio 1/4 after every doubling (antiperiodic-support lemma, PROOF-SKETCH) and geometric fill along 1010... (COMPUTED). Probes `edge_break16.c`, `left_settle.c`, `edge_supports.c`.
- CL655 (Cloud, 2026-10-30): the owner's hiccup in the clock, wall frame W = 8..22 exhaustive: one dropped or inverted pin lets a released start outlive the perfect clock by up to 14 steps (W = 10); best single-hiccup lives 20, 32, 32, 34, 36, 40, 46, 46 against D(W); survivors' odd bits exactly fair below the width (the kit's free bits). Two predictions refuted. Probe `clock_hiccup.c`.
- CL656 (Cloud, 2026-10-30): finite rows keeping a period-2 column, exhaustive to width 22: L(w) about w + 3 (25 at w = 22), best column at the seed's right end; the question is the kit's CQ01 (FiniteConfigs); the wall frame is a sideways transform, not a configuration frame (my P32 frame error withdrawn). Probe `finite_clock.c`.
- CL657 (Cloud, 2026-10-30): transient census of alternating stretches in any column of any finite row to width 18: M(w) about w + 11, late starts, consistent with a fair coin's longest run over the cells examined; no CQ01 candidate. Probe `finite_clock_runs.c`.
- CL658 (Cloud, 2026-10-30): the question set for GPT from the day's breaking work: six sharp mathematics items (antiperiodic-support lemma, geometric fill, own-parity rate, choked gates, reversal response, finite-row head start), five computations (AND/OR exponent distributions, settling slope, left exponents, two hiccups, plateau ceiling at 128), four broad questions, seven conditional forks.
- CL659 (Cloud, 2026-10-30): the past of a finite row: at most one finite predecessor, iff the row begins 11 and the leftward solution is black at its second cell (PROVED, hand; a quarter of rows, census to width 14); finite past at most floor((w-1)/2) deep; the single cell's infinite past has left-tail periods 1, 3, 3, 6 x 6, 12 x 3 (COMPUTED, 12 steps), beside §8.19.
- CL660 (Cloud, 2026-10-30): CL659 reframed beside the 28 October past-state study (GC2015 to GC2024): a finite row's past is a short unique finite stretch, a root with two kinds of parent (A/B), then the ocean; the backward period sequence 1, 3, 3, 6 x 6, 12 is the same for every root to width 8 up to the finite stretch and one branch (COMPUTED), the first two steps PROVED; a backward odometer with base period 3.
- CL661 (Cloud, 2026-10-30): addendum E to the GPT question set: the backward odometer (finite-parent law, backward lifting parity, universality of the backward period sequence, conjugacy with the forward odometer, the period-48 backgrounds), with forks F8 and F9.
- GC2259–GC2270: [Cloud's nineteen questions and nine forks](reports/cloud-question-workflow-20261030.md): carried support/finite-parent laws with corrections; solo choked-gate logarithmic bounds, mixed-driver return law and complete depth40two-branch restriction for all finite roots. Exact OR/AND distributions through21bits, W22two-release maxima, left tails through100000and width12backward tails through40. Geometric fill, simple overlap monotones and additive release costs refuted. P128graph stops unclosed at200000states. Five passed stages/one retained failed control; six digest-verified raw packets. Density, speed, CQ01and all-depth coalescence remain open; both schedules paused.
- CL662 (Cloud, 2026-10-30): GPT's question pass GC2259 to GC2270 read; eight corrections to Cloud's entries taken (count 2^(w-4); support fractions withdrawn; sixteen-gate probe fixed and rerun, six gates within 0.386 to 0.412; backward p-or-2p withdrawn; plateau maxima 10/92; F5, C3, F3 withdrawn; A6 as strong as CQ01); GUARDS.md opened with G1 to G13.
- CL663 (Cloud, 2026-10-30): the question set revised question by question (result, better question, follow-up A1' to E4', forks F10 to F13), written under the guards.
- CL664 (Cloud, 2026-10-30): the lossy-gate / hash dialogue sorted against the record (sideways reversibility, merges as stepping stones, implication gates in the OR class, Kleene logic as the door calculus, the trick dictionary); the quantifier shape of Q01 (per-width finitary, uniform in W; the clock's constraints are satisfiable by Jen's forced halves, so the left edge is the only killer); DQ-025 born: does the clock die when the crystal reaches it?
- CL665 (Cloud, 2026-10-30): DQ-025 refuted as posed (the crystal recedes from the column); lab-frame census: a column keeps the clock at most 6 to 8 steps beyond the arrival of the whole row's news (w <= 18, exhaustive; CQ01's finite shadow); corrected DQ-025 as a budget (pins spend one bit per two steps; the right half refills at most the channel bound) handed to GPT with three concrete steps. Probe `finite_excess.c`. GUARDS G14.
- GC2271–GC2272: [Cloud revised-question and budget review](reports/cloud-revised-questions-review-20261030.md). Complete CL662–CL665 carrying/source catch-up; external18:08refresh unchanged (69portal entries/16openPRs). Late-halving and coupled-language transfer gaps restated precisely. A6' constant lifetime refuted by known realization/locality truncations; backward period-family3*2^e follows from E2, with no all-depth branching law. Solo deductions await review; revised computations pending, both schedules paused.
- CL666 (Cloud, 2026-10-30): GPT's review GC2271/GC2272 taken: operand labels, the early-counting law's range, constraints across ensembles, the Pi-1 nature of fixed-width immortality, two overclaims (degree theorem; Lowry's theorem does not exclude dissipative local potentials), A6' refuted by realisation plus locality, ring-module scope, the frame bridge; guards G15 to G18; the three excess witnesses' traces supplied, reading as relays of lone cells.

- GC2273–GC2276: [CL666 relay/repair audit](reports/rule30-relay-witness-audit.md). Lifetimes7/16/17 confirmed; final window timeline corrected; known ether identified. Nonlinear cooperation and shorter-core/longer-clock counterexample. Solo conditional fallback return and exact fixed-left optimum17 from known forbidden101001, attaining row {0,7,14,17}. Two frozen runs retained, predicted18 refuted; no further census. New public PR61 complete source read; portal unchanged.
- CL667 (Cloud, 2026-10-30): GC2273 to GC2276 taken (relay audit: the known four-phase ether with nonlinear repair; fixed-left optimum 17 exact by a certified forbidden suffix; a transcription error of Cloud's, G22). Submission assessment: Package A, edge clocks for every two-input gate (half-rate bound gate-generic, affine and choked gates logarithmic, reversal law), likely provable, recommended; Package B, the finite past of a finite row, small and clean; nothing prize-moving.

- GC2277: [owner restart for delivery and curiosity](reports/GPT-PROOF-DELIVERY-RESUMPTION-20261030.md), schedules 13/5 active, Local offline until confirmed return. CL667 A/B scoped plan, generic reversal coefficient and indexing clarified; new PR61 companion archive read queued. No new compilation/submission or compute.

- GC2278: [source/implementation checkpoint](reports/GPT-PROOF-DELIVERY-RESUMPTION-20261030.md#live-checkpoint-gc2278) and [dyadic phase-clock sketch](reports/quadratic-edge-clock-transfer.md#12-gc2278-curiosity-pull--a-fixed-dyadic-phase-clock-can-be-absorbed). Exact PR61 linked-source scope; generic static obligations; scaled resource floor(order/L) repairs an explicitly refuted unscaled reset law. No new computation or compilation; independent review pending.

- GC2279: [credited static package outline](reports/GPT-PROOF-DELIVERY-RESUMPTION-20261030.md#gc2279-primary-source-disposition-and-static-essay-outline); exact periodic-switching hypotheses compared. [Retained B1 cycle-weight identity](reports/cloud-question-workflow-20261030.md#gc2279-cycle-weighted-reanalysis-of-the-retained-b1-table) and arithmetic checks declared before inspection; no new dynamics or independent acceptance.

- GC2280: [retained period-table lifting analysis](reports/cloud-question-workflow-20261030.md#gc2280-retained-table-outcome): all80exact arithmetic rows pass, uniform and black-edge measures distinguished; no new dynamics or fairness-marker recovery. Source/output retained; nice adjustment denied and not claimed.
- GC2281: [arbitrary finite forcing clocks](reports/quadratic-edge-clock-transfer.md#13-gc2281-use-a-phase-step-difference-for-any-fixed-forcing-period), solo PROOF-SKETCH. Two commuting differences recover the same Path bound for augmented periods L*2^K for any fixed common L. Separate from static submission; independent read pending. Next physical finite-past source comparison.


- GC2282: [Package B source map and attribution correction](reports/GPT-PROOF-DELIVERY-RESUMPTION-20261030.md#gc2282-package-b-has-an-older-reviewed-core-and-a-precise-formalization-gap): reviewed G121/G122/L077 finite core, actual kit Preimages/FiniteConfigs/FrozenRuler/ZeroBoundary matches, physical versus wall/decoration/stripe parents separated. GPT takes B source preparation, no build; Local remains intended A owner.
- GC2283: [fresh PR61 four-layer budget and controlled five-digit obstruction](reports/GPT-PROOF-DELIVERY-RESUMPTION-20261030.md#gc2283-new-pr61-black-clock-budget-and-its-exact-scope): exact source/guard read,46payloads verified, author47constant/5head receipt read, broader replay only reported. No GPT compile or arbitrary-band claim.
- GC2284: [finite ancestral-age distribution](reports/GPT-PROOF-DELIVERY-RESUMPTION-20261030.md#gc2284-a-counting-consequence-for-finite-ancestral-age): exact tail C(w-2k)/C(w), limiting mean1/3 under the stated ensemble; solo consequence, no independence or novelty claim.
- GC2285: [temporal recovery of the hidden categorical-memory bit](reports/GPT-PROOF-DELIVERY-RESUMPTION-20261030.md#gc2285-the-hidden-memory-bit-is-ambiguous-only-at-c-to-b): C,C forces0; C,A forces1; only C,B ambiguous locally. Solo finite-prefix upper bound, no all-time source realization or doubling-density inference.


- GC2286–GC2288: [finite physical past source and failed development pilot](reports/wolfram-agents/submissions/finite-past/README.md). Root/age interface plus exact finite-parent criterion prepared.4.33.1fails in unchanged Realization before package/controls; no rerun, no package compiler validation. Exact receipts retained;4.35and independent source read pending.
- GC2289: [three-black ancestral age classification](reports/GPT-PROOF-DELIVERY-RESUMPTION-20261030.md#gc2289-at-three-black-cells-finite-ancestry-has-depth-at-most-two), solo consequence of known inverse/solid-block machinery. All ages<=2; exact fixed-mass mean(1+[w=2mod3])/(w-2) tends0. No orbit statistic, priority claim or new compute.

- GC2290: [normalized finite-past source and known external ancestry objects](reports/GPT-PROOF-DELIVERY-RESUMPTION-20261030.md#gc2290-normalized-source-actual-counts-and-older-external-provenance). Exhaustive duplicate-free physical-row counts and exact translated image prepared, UNCOMPILED; 2016 OEIS finite parent/root/age/reconstruction explicitly credited. No compiler rerun or novelty claim.
- GC2291: [four-black exact ancestry classification](reports/GPT-PROOF-DELIVERY-RESUMPTION-20261030.md#gc2291-four-black-cells-have-ancestral-age-at-most-four), solo PROOF-SKETCH. Sharp maximum age4, explicit single-hole/congruence/period-three inverse branches, arbitrary gaps handled by hand. General fixed-mass bound remains open; no enumeration.

- GC2292: [B essay, exact headline/source assembly and current environment](reports/GPT-PROOF-DELIVERY-RESUMPTION-20261030.md#gc2292-a-concrete-b-essay-and-source-carrier-with-live-environment-checks). Abstract/prose/specification and seven wrapper types prepared, source55024c94 byte-bound, all UNCOMPILED; no notebook/compiler retry. Fresh external comments and verifier19540bfb source compared/retained. Local explicitly resumed as sole A owner; GPT B preparation continues.
