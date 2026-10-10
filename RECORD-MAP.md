# The record map: what is known, and where it lives

*The record's top tier, at the owner's request (2026-10-09): "top level documents with very brief summaries that
reference lower tier documents, the top level document could always be ingested after compaction to keep it in
context." Started by Cloud the same evening, after its SL probe re-derived G205 and G208, which were on the status
board all along. Rule: `record-map` in WORKFLOW-SAVED-MEMORY.md.*

**How to use it.**
1. Read this file in full at the start of a session and again after every context compaction, before other work.
2. Before a run or a proof attempt, search the whole record:
   `python3 tests/probes/record_find.py TERM [TERM ...]` (each TERM a regular expression; all must match one
   paragraph). Write `Record searched: <terms> -> <hits, or "no hit">` in the predictions.
3. Read the place a line names before citing it. This map is an index, not the record: where they differ, the
   record wins and the map is corrected.

**How to keep it.** The commit that lands a result (a second-read proof, an exact computation, a measurement, a
refutation, a closed route) adds or edits its line, under the object it is about. One line per result, at most
about 15 words of claim, then the status, then where it lives. Keep the file under 40 KB (30 KB until 2026-10-10;
L521, CL139): a section over 3 KB, or the file over 40 KB, is compressed at the next board triage, which also folds
dated receipt sections into their objects.

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
- Chain (PERIOD-TWO.md §2), all OPEN: R(d) <= d + 4 (§8.36) ⇒ R(d) finite for every d ⇔ LR (König; §8.36) ⇒ LR_m
  (§8.11) ⇒ B (§8, §8.11) ⇒ period 2. LR, LR_m, B: no column 1, no width-m layer input, no finite right half makes
  the forced left half for 0101 eventually zero.
- Exact forms: forced walk (§8.37), wall form (§8.39), black, white and both (§8.40) — COMPUTED (probe-checked)
- Q1: keeping the wall's conditions costs real information; prove N_{w,j}(T+k) <= 2^(c(w) - αk) N_{w,j}(T) with
  c(w) = O(log w) — OPEN ("No known method reaches it") — PERIOD-TWO.md §5; §8.51 to §8.53, §8.58; board Q1 (M1)
- Delivery side is a theorem (the channel bound); the cost side holds exactly only beside a constant wall, and
  beside 0101 only as a coin model — PART — PERIOD-TWO.md §5; §8.41
- The seed's left part pays exactly: it halves the count (left-permutivity) — PROVED — §8.51 to §8.53 (CJ0, DB0)
- The law holds for a random word too, so a proof must use what is special to periodic words — MEASURED — §8.42
- Primes, Fibonacci, pi, 01: the best start of w <= 18 squares holds them w + 6 steps at most — COMPUTED — CS
- First right-paid ratio rho_j exact to j = 35; its distance from 1/2 does not decay — COMPUTED — L224, L225; ZR3 (L316)
- A uniform linear edge deadline T <= cj + b would give Q1 with alpha = 1/c — PROVED L345/CL161 — GC637/947
- H(j) - j <= 17 for j <= 22, a plateau broke at w = 27; only §8.69's ceiling certifies — MEASURED — DL, DL2; GC660

## The wheel (column 0 clamped to 0101, column 1's 56-step word, the forced block next to it)
- Column 1 beside 0101 is the wheel U, an exact coding of the rotation by 17/56, kicked by domain walls in notches
  of 1/28 turn; no other trace tried turns one — MEASURED — §8.4 to §8.11; PERIOD-TWO.md §3, §5
- Even-time word sigma(2s) = floor((17s + 6)/28) - floor(17s/28); 56 steps are 17 turns — COMPUTED — §8.32
- Slips are domain walls moving half a cell a step, arriving only at wheel phases 32 and 52 — MEASURED — §8.7, §8.8
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
- SL re-derived the forced block by SAT, a repeat of G205/G208 (the miss that started this map) — COMPUTED —
  rule30_cloud_wheel_slab.py, CL098, CL101, GC855, GC860
- §8.11 N1's "60% against 8%" compared two measures: on N1's own, real halves 69.8%, wide random 70.9%, coins
  60.2%; coins at column 13 sit inside the partial lock — MEASURED — rule30_cloud_wheel_slab.py, CL098

## Kicks (alphabet, classes 12/32/42/52, rates, the kick game)
- Size set by the interior; timing and alphabet rigid; no memory; about 3.5 bits a kick — MEASURED — §8.43, §8.11
- The alphabet is local: after 133 steps, four classes and at most log2 6 bits a kick; not a classification of
  arbitrary column-1 histories — COMPUTED (second-read, GC359) — entry 26 (Proposition 13, KL)
- After 133 steps: classes 12, 32, 42, 52 only, sizes +4..+8, +2..+6, +1..+5, -6..-1 — COMPUTED — entry 27 (board 6.1)
- Class 12 impossible for every right half after 140 steps; possible at 56, 84, 112; the obstruction needs the rule
  out to column 37 — COMPUTED — KS (Cloud), KK and DT (Local)
- Every size of 32, 42, 52 realized; class 42 is 67 of 20,282 settled kicks — COMPUTED, MEASURED — KX; KB
- Class 42 dead at N = 560 in all 56 cases (drat-trim) — COMPUTED — KT2C
- Classes 32 and 52 still possible after 448 steps; nothing above 448 decided for 32 — COMPUTED — KT2N (L375), KT2M
- At 56 observations class 19 (kicks -8..-4) is admitted, unused by RB's kicks — COMPUTED (single-party) — OLD1 (GC588)
- A kick lands at the take-off's parity and the opposite colour, just after a white; forward kicks from even white
  take-offs land on the even black arc 44..54, at most six sizes — PROVED — Entry 28 (Proposition 15, GC389)
- Last class-12 front: 11100 at s-14 and 5(s-2) = 0 force 6(s-6) = 0; no preparation bound — PROVED — G209/G210, GC407
- Kick game: runs grow like log2 of its histories; rigidity is a constraint, not a bound — MEASURED — §8.44
- Left: the interior's choice of size; what forbids class 12 at column 37; the cost side (Q1) — OPEN — board 6.1
- The edge ruler's news reaches the wheel but does not measurably change the kick rate or rhythm; which kicks
  happen is unmeasured — MEASURED — rule30_cloud_ruler_kicks.py, CL096, GC856

## Records R(d) and R_real(d) (Q6, RR, RR2, RR3)
- Full79-state S/L component exceeds actual entropy ceiling; missing interior cut length41..5120 — COMPUTED / hand — GC1007.
- Both cutoff40 lists retain a79-state recurrent S/L component; selected loops force initial black at depth146 — COMPUTED — GC1007.
- Interior visible gap4422 requires a neighboring gap2, conditional on reported minimal absence — hand inference — GC984; L556/L557.
- Noninitial interior4422 forces preceding5 and following2 — hand inference from reported forbidden words — GC985; RLK K18.
- FullK18 bounds4422 occurrences by1 at every word length — PROVED by finite potential, independent L561 review — GC986.
- Gap4 trains of length>=4 start only near the initial boundary; cannot restart — hand inference — GC987.
- Actual suffix from13 forbids4422/4444; age12 retains4444; relaxation still branches — hand / COMPUTED — GC988/989, L563.
- Phase-0 R(d)<=d+4 through depth89; R89=75, R93 running — COMPUTED / OPEN — §8.36/37, RK93.
- Both-phase R_real exact through19, then21..97<=17 — COMPUTED — ZR/ZR2 L236, RR L247, RR2 L399; RRX/RRP replay.
- R_real(97..110)=14,14,13,15,15,14,14,13,13,12,14,16,15,14 (109 by the plateau law and the solver); 111=15, 112=15 (plateau law, then solver), 113=14, 114=13, 115=14, 116=15, 117=14, 118=15, 119>=14, 120=13 (solver, then the plateau law) — COMPUTED — RR3
  checkpoints, CLOUD-LOCAL archives.
- RR3 on M5: SAT replayed, UNSAT not DRAT-checked; 111..120 running — COMPUTED / OPEN — rule30_cloud_rr3.py.
- Both phases versus phase0; plateau R(d+1)>=R(d)-1 — COMPUTED — L286/CL038, RR3 (101/105 solver receipts).
- Inherited RR/RR3 cone CNF matches finite query, independently of solver evidence — PROVED (source scope, CL154) — GC937; solver-free replay separately attributed.
- VC3 receipt gate/status repairs pass synthetic controls; stale-cache recovery manual — source/fixture audit — GC961/965; no certificate replay.
- Deciding UNSAT d3..97 checked by drat-trim/cake_lpr; VC checks200/200; RR3 98..101, 105, 107 by cake_lpr — COMPUTED — RRC L438, L480, VC3, rule30_verified_certs.py.
- Forced-walk counts~2^(0.41d), coin optimum~0.826d+0.8 — MEASURED — §8.38; endpoint words RRX/RRL.
- Relaxed records, exact forbidden words to K=16/18: exceed 17 first at d=65/84; moving frontier — COMPUTED — RLK L555..559.
- K=40 relaxed at L=18: d=124 UNSAT both phases, so R_real(124)<=17; d=140, 144, 152 phase 0 SAT (open) — COMPUTED (kissat, uncertified) — RLK probe L575, L581/582, L589.
- The 2-gap train 1010.. is actual to n = 200 in both phases; the finite right half 1001 beside the phase-0 clock keeps column 1 on it for 3000 readings (an ordered band of 14 sites: period 4 to site 6, period 8 to site 14, chaos pinned at site 15 for 40,000 steps); no finite invariant window to W = 60; eternity PROVED by GPT (GC1020, W282: sixteen-tick causal lock on column 14 plus strong induction; also for every tail beyond site 46), independently re-derived and read by Cloud (CL189) — PROVED, review complete — TG, rule30_cloud_train_block.py, CL186 .. CL189.
- Decided R_real climbs about 0.085 a depth over d = 30 .. 116 (no shuffle of 2,000 reaches it); exact L = 18 at d = 140, 148, 156, 164 UNKNOWN after 13,321 s each (14:30 stop); 144 .. 168 UNKNOWN at 3,600 s — COMPUTED — TR, rule30_cloud_rreal_trend.py, CL178, CL188.
- Lift: relaxed model plus exact right half, simulation-gated; d=152 L=18 code ABSENT (length-81 cut) — COMPUTED — RLK lift L581/582, L591.
- relax40 first exceeds R_real at d=107 (16 vs 14); blocked by a length-46 minimal forbidden word — COMPUTED (cake_lpr) — RLK L583/584.
- CUT reproduces R_real(107)=14 in phase 0: one cut, L=15 UNSAT (cake_lpr), L=14 simulated witness — COMPUTED — RLK L588, L595.
- GC1007 S/L component: 61 verified cuts (42..97) take entropy 0.1386 to 0.1192 (ceiling 0.1236) — COMPUTED — SLC/SLC2 L588, L591.
- All 1,603 cutoff-40 list words and every CUT/SLC cut absent by cake_lpr — COMPUTED (verified) — MFC L590.
  Unary/affine forcing stalls; this gap4 cut leaves GC1007 S/L subsystem unchanged — COMPUTED / hand — GPT L584 follow-up.
- Visible language to n=40: no small lift; follower and synchronized classes grow (154 at k=20) — COMPUTED — SOF L564..568.
- Exactness through40 needs strip width35; widths<=34 excluded, all-depth boundedness OPEN — COMPUTED / scope GC996 — SW L569/570.
- No left edge within248, any right half; right-half bounds32/34 — COMPUTED — LL1..LL4 §8.56; §8.21, M3b.
- Best seed wall duration<=width+9; other traces width+6..10 — COMPUTED / MEASURED — §8.24/42.
- Finite left edge forces frontier events, increasingly old/restarting Fibonacci-parity compensation — PROVED — GC585/586/597..600; local rules CL055/GC595.
- Fixed sources silent, near-silent sources never harden — COMPUTED — SS/GC589, SO/GC591.
- Finite left support excludes all-S and eventually periodic S/L renewal tails — PROVED L372/CL160 — GC686/704/706/707, §8.78.
- Marker-aligned n S gaps need J>=6n-3; rigid all-L needs J>=10n-6 — COMPUTED — GC705/L372, AL/L380.
- Bridges<=24 (tail period<=10) to the155-ring excluded; template K6 passes but rings<=30 fail — COMPUTED — CX, GC828, TC/L452, RD.
- Adjacent-left density>=3/4 and selector/front lemmas — PROVED — G256, G259..268 (PROOFS E2).
- Phase-mask, same-reference-orbit pumping and quotient guards — PROVED — GC846/848/849, G269/270/272; L474/493.
- Last-defect and zero-lag parity shortcuts CLOSED; ParityMask ingredients accepted, assembly unformalized — CLOSED / PART — GC874..876, CL112.
- Remaining Q6: inter-run compatibility with unbounded reach — OPEN (PART) — GC845, PERIOD-TWO §6.



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
- Train exits4,5 follow short absences; entrance3 occurs only at startup, with finite witness — hand / COMPUTED — GC1023.
- Five-cell train returns can violate exterior updates while sharing an actual visible output — COMPUTED / hand — GC1022.
- Shifted known train escape survives through100; no transport or eternal-healing theorem — MEASURED — GC1021.
- Finite clamped-clock seed1001 has eternal train; fourteen-site band closes by causal P8 lock — PROVED (CL189, L595) — GC1020/G282.
- Two-gap trains force a six-column slab; exterior interface is a white sample beside 0111 — PROOF-SKETCH — GC1017.
- Train-interface gate has three failing prefixes; one-cycle eligibility is not invariant — PROOF-SKETCH / COMPUTED — GC1018.
- Failed train gate reaches column 1 after eight ticks; seed 1001 reduces to 01 beside 0111 — PROOF-SKETCH — GC1019.
- Whole short-entry family plus mature gate loses exact past; forward closure is insufficient — REFUTED — GC1015.
- Mature S gate retains nine prefixes; G239 SL startup example has no two-tick past — COMPUTED / PROOF-SKETCH — GC1014.
- Marker prehistory branches at arbitrary distance; some prefixes forget all tail constraints — COMPUTED / hand — GC1010/1012; G236 method.
- S/L cut suffixes have exact maximum macro prehistory0/1; length40 exclusion after age2 — PROOF-SKETCH — GC1009/1011, L590.
- Actual visible histories have a four-prefix nonlinear obstruction at left depth26 — COMPUTED — GC1008.
- Fixed m wall updates admit every remote spatial tail; origin correlations remain — PROOF-SKETCH — GC1006.
- Black-image rooted1 0^k 1 0 impossible; spatial010 admits every tail — PROOF-SKETCH — GC1005.
- First black-start exclusion forces spatial10010, impossible after black-wall update — COMPUTED / hand — GC1004.
- Matured black-start cuts through K-1 follow from complete white cutoff K — PROOF-SKETCH — GC1002/1003.
- Exact spatial NFA caps after two observations; forward simulation gives no compression — prototype PART / REFUTED — GC998..1000.
- Width9 strip warmup stabilizes after6 macros but retains GC994 false merger — COMPUTED — GC997; actual positive E13 continuation absent (L572).
- Equal complete width9 compatible sets can conceal distinct actual futures after marker01 — REFUTED sufficiency — GC994.
- GC992 gap-order distinction needs width9 in exact right-strip relaxation; width8 admits both — COMPUTED — GC993.
- Equal gap multisets/endpoints/window7/lastgap can have different actual futures — COMPUTED discriminator — GC992.
- Eight hidden phases can yield255 observer residuals; finite follower growth inconclusive — control PROOF-SKETCH / COMPUTED — GC991.
- Equal elapsed phase/count/window7 can conceal different actual futures — COMPUTED finite discriminator — GC990, RLK K18.
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
  rule30_trace_word_certs.py, L467, GC844
- OHC at p = 2 reproduces §8.20's table to 3 decimals, m <= 22 — COMPUTED — rule30_one_hole_widths.py (XC)
- TC and TC2 audits: TC's CNF and pruning (GC871, PART), gates repaired (PART, source accepted, CL107); TC2's live
  automaton (GC877, PART), integer vector (GC879, PART, CL109), F digest and counts (GC886, COMPUTED), F count-root
  ceilings reproduced (GC889, COMPUTED)
- LP audits: the product is sound (GC883, PART); redundancy split (GC884, PART); the component method (GC885,
  PART); the verifier and fixtures (GC887, PART; retention done, L507); recurrent-witness recipe (GC888, PROVED,
  CL118, L507); weighted witnesses (GC891, PART); positivity guard (GC942/944, CL158; synthetic and hand scope)

## The left front, triangles and the right edge
- Left diagonals eventually periodic, power-of-2 periods (Jen 1986, Rowland §5) — PROVED — JenPow2.lean L541: band k<=j+2 period2^j; settled gcd run bound L543; source GC962; §8.27/30.
- Lemma B1 (white, then black; Lean LemmaB1.lean L529; source GC955), B2 (unbounded periods; LemmaB2.lean L545/550, source GC963; infinite white/black JenPow2.lean L548, source GC964), B3 (no white run over twice the
  band's period; Lean LemmaB3.lean, L534; source GC958; sharp 2P-1, tight at P=1,2, L539; GC960) — PROVED —
  §8.59; B2 for the single seed is in print (Nersissian Theorem 13)
- Rowland's question answered both ways: >= 4 certified left sides; 60 generic rows share one — COMPUTED — §8.31
- Leftward speed 0.246 = 1 - 0.41 x 1.84, by the identity v = 1 - P(heal) E[jump | heal] — PROVED (identity),
  MEASURED (values) — §8.66
- The order ends at an exact boundary B(t), a walk near x/t = -0.25 — COMPUTED, MEASURED — §8.74
- Left-only horizon next to 0101 is W + 17; slow walls stop every width-16 seed within a period — COMPUTED — §8.69
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
  rule30_cloud_triangle_echo.py (EC), CL108; measured first in rule30_cloud_velocimetry.py, CL095
- The centre's wave moves at speed 1 and never reaches the right edge: the gap W + tau is exact; leftward influence
  can reach speed 1 on white — PROVED — GC856 (second-read CL103); rule30_cloud_centre_wave.py, CL097
- Diagonal bias: rho_k's sign alternation fails at k = 17; rho_22 = -8408217689/2^42 — COMPUTED —
  rule30_diagonal_bias.py, L473

## Periodic points and travelling waves
- Pure2-gap trains actual at every length, both phases, via existing seven-ring — PROOF-SKETCH / COMPUTED — GC1013; §5.
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
  to 30 cells in Cloud's ring search (CL086, rule30_cloud_ring_template.c) — COMPUTED

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


## Routes closed (do not reopen without new evidence)
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
- Q3, a machine-found certificate: it is Q1's potential — CLOSED — §8.61 (G5's caveats)
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
- Least residue: T^k(2^k m + r) = 3^a m + T^k(r), 0 <= T^k(r) < 3^a — PROVED (known: Terras) — COLLATZ-PRIZE.md §4
- Window principle W1 to W3; W2 is Dubickas 2009 Theorem 5 — PROVED (known) — COLLATZ-PRIZE.md §5
- Exponential sums cannot reach a single case — CLOSED — COLLATZ-PRIZE.md §5
- Every actual demand law is unimodal; not always log-concave — PROVED, COMPUTED — entry 30 (Proposition 17); L048
- The universal singleton route — REFUTED — G89 (L046)
- First-deficit survivors n < t^14.3/3; endpoint certificates; offset envelope — PROVED — G69, G68, G67 (L037)
- Conditional bounds (G30, G34, G35, G39-G42, G47, G48) — PART — board Q9; signed bias O(1/m) at T = 8m is OPEN
- Rule 30 and the 3/2 map share one linear map (the Gray code), corrected locally and by a carry — PROVED (an
  identity) — PRIZE-PROBLEMS.md; COLLATZ-PRIZE.md §8; carry audit CL066, GC616 (L326)
- "XOR plus AND": the linear-shadow claim was wrong; carry-free Collatz keeps the parity AND; the product-free
  shadow has two basins — REFUTED (CL090) — GC832, GC833, CL091
- Mahler's 3/2 corner: survivor counts fall by 3/4 a step; maximum horizon 47 for g < 2^20 — MEASURED —
  rule30_cloud_mahler_horizon.py, CL092 (Local's MD and GPT's GC836 are in Local's section below)
- Mahler bounded-gap Fibonacci code passes fractional tests but fails integer realization — PROVED (CL148) — GC929, G50 continuation.
- Mahler calibration prefix residues certify the reported million-start match cutoff — COMPUTED — GC931, G51 fixture.
- Mahler backward-forbidden roots cannot recur along a white orbit; visitation shortcut CLOSED — GC928 (second-read CL147), GC665 corollary.
- Capped Mahler bits and values lack uniform convergence near4/3 — PROVED L524/CL153 — GC935/936, G266 continuation.
- Mahler carry dial: H_k(g) = v2(g) + 1 at k = 0 (GC836); odd k collapse; g = 53 survives at k = 4 — MEASURED —
  rule30_mahler_carry_dial.py, L457
- Carry-limited Collatz: cycles at even k = 2, 4, 6; 0 at odd k; all reach 1 at k = 0, 8, 10, 12 (n < 2^18) —
  MEASURED — rule30_and_shadow.py, L453

## Prior art anchors
- Condrey arXiv:2609.09431: period 1; his Lemma 1 is the forced left half — used, audited (G11; §8.76)
- Jen 1990: adjacent columns never both eventually periodic — used (§8.13; GC792); Jen 1986 still owed for B2
- Kopra TCS 946 (2023): Rule 30 rapidly left expansive (0, 1, 2), Corollary 3.7 is Jen's theorem — used (§8.13)
- Kopra 2021 (arXiv:2005.05112): one p/q column never eventually periodic; Theorem 3.5 at width 1; Rule 30 has width
  2, so a transfer needs a new hypothesis — GC807; PERIOD-TWO.md §5
- Kari and Kopra (arXiv:1710.05737): true and empty for centre columns — §8.55; GC670
- Rowland 2006 §5: left-side period doubling; his one-left-side question answered here — §8.31
- Nersissian arXiv:2609.25077 Theorem 13: B2's method and single-seed statement, earlier — credited (§8.59 note)
- Meier and Staffelbach (1991): the left half from two columns, this record's construction — convergent
- Hanson and Crutchfield (1997): the domain filter — imported for the wheel's walls
- Flatto, Lagarias and Pollington (1995): Mahler's decoupling, the same skeleton — a calibration, not a route (§8.45)
- Dubickas 2009 (W2); Terras, Lagarias, Kontorovich–Sinai (least residue); Bugeaud and Dubickas (2005) — credited
- Guillon (2008): the retourné is the forced left half; entropy at width 2 — §8.77
- Sablik (2008): no expansive slope (GC813); Coven, Pivato and Yassawi (2007): edge odometers (GC808, GC810)
- Tahay; Dolce and Tahay: Sturmian columns from finite seeds in other CA, so finiteness alone forces nothing
- Milnor, Kurka, Courbage–Kaminski: about systems; no lower bound on one column's entropy found — §8.33
- Wolfram (2019): the band's boundary at 0.252 a step, an observation; Epperlein (2017): periodic-point table
- Cramér's model: the coin's scale, with a structural constant (§8.38); Das: not imported; López–Stoll: a gap noted

## Side questions (CONSTELLATION.md, by name only)
- Part A, families after Condrey: Condrey's walls; one-hole walls; slow walls; mostly-white walls; the by-period
  ladder; the single cell itself; the uniform count
- Part B, the object itself: universal left side; right edge and nested side; two light speeds; the wheel; the
  sideways rule; the channel and two worlds; columns as numbers; balance without randomness; siblings and the one
  shape; ring dynamics; settling front and odometer; computation in the rule; triangles, templates and quantised
  runs; what makes 30 special; inverse reset language; hidden dynamics and visible languages; time derivatives;
  relativity and the lopsided light cone; unequal ticks; alternation, heard
- Section E, portfolio: seed universality in a deterministic core; a transport law for a defect; the arithmetic of
  the ordered edge; the infinite-width boundary information limit
