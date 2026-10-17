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

**Status words.** PROVED: a proof with a second reader. PROOF-SKETCH: a proof not yet second-read. COMPUTED: an
exact computation or certificate. MEASURED: statistics. REFUTED: a claim shown false. CLOSED: a dead route. OPEN,
PART: as on the board.

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
- Rule 30 = Rule 150 jump XOR AND echoes: exact (PROOF-SKETCH identity, COMPUTED to t = 64) §8.100; not local — MEASURED
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
- Method and first problem: GPT-MATH-INSTINCT.md. Frankl union-closed conjecture OPEN; old prize lanes held.
- Known27-set smallest-member obstruction audited; fibre-weight sampling trap exact — COMPUTED MI003; no new theorem.
- Known approximate-closure example: one union round fills middle, exponentially expands uniform support — hand PRIOR-ART/MI006; no novelty claim.
- Inverse-multiplicity coupling already in Jiang2609.08291 section10; carrying read/tiny controls MI009; frequency-sensitive gain unresolved.
- Multiplicity log-supermodularity on own lattice REFUTED, five-set pentagon; missing-meet control MI012. No novelty claim.
- Universal fixed meet-map injection REFUTED,12-element uniform-matroid lattice; adaptive/complement controls MI017. No Frankl result.
- Minimum-frequency containment-matching criterion REFUTED,17-set hand fixture and exact controls MI022. Frankl unaffected.
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
