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
- First right-paid ratio rho_j exact to j = 35; its distance from 1/2 does not decay — COMPUTED — L224, L225; ZR3 (L316)
- A uniform linear edge deadline T <= cj + b would give Q1 with alpha = 1/c — PROOF-SKETCH — GC637
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
- R(d) exact at 1..61, 65 and every fourth depth to 89; R(89) = 75; R(d) <= d + 4 throughout — COMPUTED — §8.36,
  §8.37; board 6.2 and M4. R(93) runs — OPEN — RK93
- §8.36's R(d) is the phase-0 record; RR, RR2 and R_real are maxima over both phases — COMPUTED — L286; CL038
- About 2^(0.41 d) distinct forced walks; the best under coin flips gives 0.826 d + 0.8 — MEASURED — §8.38
- R_real(d) over every configuration: exact to d = 19 (4 against 17 at d = 13); after a black cell at depth j at
  most 4, 2, 0, 3, 3, 2 white cells, j = 2..7 — COMPUTED — ZR, ZR2 (L236)
- R_real 7..15 at d = 21..81 (RR, L247); decided to 97, at most 17 (RR2, L399) — COMPUTED — RRX, RRP replay
- Every deciding UNSAT, d = 3..97, has a DRAT proof checked by drat-trim and cake_lpr — COMPUTED — RRC (L438), VC
- R_real(97..106) = 14, 14, 13, 15, 15, 14, 14, 13, 13, 12 (105 by the plateau law R(d+1) >= R(d) - 1; 101 by the
  solver too, 101 L 16 UNSAT); 107 >= 14, 108 >= 16, 109 >= 15; 105, 107..120 running on the M5 (Local) —
  COMPUTED (kissat; SAT replayed, UNSAT not DRAT-checked) — RR3, rule30_cloud_rr3.py, "RR3 checkpoint" rows in
  CLOUD-LOCAL.md and its archives
- A run's end needs the clock's first beats; words 11, 00000, 101001 fit the records to d = 19 — COMPUTED — RRX; RRL
- No counterexample has its left edge within 248 cells, whatever its right half — COMPUTED — §8.56 (LL1 to LL4)
- No right half <= 32 cells works with a left half <= 108; none to 34 cells — COMPUTED — §8.21; board 6.3 and M3b
- Best seed keeps 0101 at most width + 9 steps; words to period 4 and a random word: width + 6..10, growing like a
  log — COMPUTED, MEASURED — §8.24, §8.42
- Q6 ray: a finite left edge forces an edge event at every frontier step; the inside pays its Fibonacci-parity beat
  with ever older, restarting events, never a long streak — PROVED — GC585, GC586, GC597, GC598 to GC600
- Five fixed sources silent at the frontier; near-silent ones never harden — COMPUTED — SS and GC589, SO and GC591
- Edge events obey three local rules — PROVED — CL055 (read in GC595)
- An all-S orbit exists (the 84-ring); finite left support forbids an all-S tail and any eventually periodic S/L
  renewal tail — PROOF-SKETCH (reader not stated) — GC686, GC704, GC706, GC707; §8.78
- n completed marker-aligned S gaps force J >= 6n - 3; a rigid 155-cell all-L ring: n L gaps force J >= 10n - 6 —
  COMPUTED — GC705, L372; AL (L380)
- No non-ring row with G^310 = id left-asymptotic to the 155-ring has bridge <= 24, tail period <= 10 — COMPUTED — CX
- A 0101 centre forces column -1 to long-run density at least 3/4 — PROVED (second-read by Local) — G256
- Selector-parity and front lemmas — PROVED — G.GPT259 .. G.GPT268 (PROOFS.md E2)
- GC828's template passes a K = 6 coupling gate; no ring of up to 30 cells carries it — COMPUTED — TC (L452), RD
- Same-reference-orbit backgrounds at p = 310 excluded by phase pumping — PROVED — GC848 (L474; G.GPT270)
- Left: an inter-run compatibility input with unbounded reach — OPEN — board Q6 (PART); GC845
- VC: every UNSAT behind CX, CXE, ALC, ASF and RRC (d <= 97) checked by cake_lpr, 200/200 — COMPUTED —
  rule30_verified_certs.py, L480
- GC846, GC848, GC849 filed as G.GPT269, 270, 272; G269's ingredients in Lean (ParityMask.lean) — PROVED —
  PROOFS.md E2, L493
- Bridge shortcuts: last-defect parity pullback (GC875) and interior zero-lag overlap parity (GC876) — CLOSED,
  second-read CL112; ParityMask.lean's ingredients match, assembly unformalized (GC874, PART, L493)

## The regime between, finite left halves, supports (Q7)
- Fixed-period spread <=q-1 (G6, PROVED); doubling split fixture second-read (GC922, COMPUTED, CL142); G174 guards clocks.
- Doubling preserves two occupied old lifts' coalescence iff the odd source is a pulse — PROOF-SKETCH — GC923.
- Fair-reset leaf weights are 2^-branch-depth; uniform-leaf/ambient mean transfer invalid — PROVED (CL141) / shortcut CLOSED — GC921; G158.
- Kicks cannot thin out faster than geometrically — PROVED — Theorem A, §8.54
- Every Sturmian column 1 (Theorem E); arc codings for almost every rotation number (E″) — PROVED — §8.57
- Near-squares at unbounded periods: period-doubling, Chacon, double-letter substitutions — PROVED — Corollary F, §8.59
- Thue–Morse and paperfolding, for every left edge up to 15,868 cells — PROVED — Theorem A⁗, §8.59
- Sturmian block codes, one-orbit arc unions, single-character torus codes, slower-than-geometric resets — PROVED
  — G131, G132; G131 to G136 (STATE-OF-THE-PROOF.md §3)
- All excluded classes have zero entropy; a real column 1 has about 0.08 bits per visible bit — MEASURED — §8.20
- Settling reduces to gap 1, a stage budget O(q) at each dyadic period q, and gap 2, period growth R_j to infinity
  — PROVED — G164, G165, G184; a threshold of 17 at slope 5/2 suffices (G186, G187)
- Exact debt identity at mismatch endpoints — PROVED (second-read by Local) — GC652 .. GC702; GC684
- No zero return within eleven steps after doubling (period >= 4); the return-eight graph is acyclic — PROVED —
  G188, G192; every excursion pays an automatic baseline (G203)
- Every zero-started even return at q = 8 and q = 16 is exactly its cycle; the q = 16 even classification is complete —
  COMPUTED — RC88, RC16, RC16X, QX, QX2; GC861
- Period 64 first entered at depth 65,821,413; the rooted period-32 stage passes 2.6 x 10^10 steps — COMPUTED —
  Proposition 9 (TM6), Proposition 10; clock debt <= 60 on sixteen histories to 1,048,576 (RD32, GC325)
- Left: gap 2; Thue–Morse and paperfolding for every left edge; Rudin–Shapiro; q >= 32; odd returns — OPEN —
  board Q7 (PART); the finite-left support question (G129, G140, G141) is part of Q7 (GC155)
- Rooted walks return at every period q (injective step, unique reset) — PROVED (GC867; Lean RootedReturn.lean) —
  entry 39, L489
- Zero-started returns q = 8 at 88, 371; q = 16 at 16 depths (last 214,006), each exactly its cycle — COMPUTED (GC861,
  GC862) — rule30_r88_census.py, rule30_q16_exits.py, L486
- A physical one-parity odd return exists: the single cell's q = 16 end 1010100010100000 (depth 87,867, N_5's
  minimum); its period-32 entry is sharp, wt(f) = 8 = q/4. None of TM6b's 56 exits to period 64 is one-parity —
  COMPUTED — rule30_cloud_sharp_entry.py (SE), CL134; GC915 independently verifies the fixed witness; exclusion REFUTED
- Rooted (physical) tree, period-16 stage: fifteen branch nodes, sixteen histories entering period 32 at 87,867 ..
  894,235; earlier entries N_j = 3, 8, 29, 400 — COMPUTED (second-read) — Proposition 8, entry 21 (TM5, TM5b, TM6)
- Its whole in-tree at fixed q: 4, 14, 98, 3,066, 34,541,082 states (q = 1 .. 16); non-dyadic q repeat their dyadic
  part — COMPUTED, a third replay of Proposition 8 — ZF, CL126 to CL128. RC88's r = 88 source is not physical; 371's is
- q = 32: 15 of 16 sampled zero-started orbits return (4.5e7 .. 9.1e9), one beyond 2e10 — COMPUTED — rule30_rooted_walk.c,
  L488
- Fixed-q zero-started excursions: every admissible one returns, r <= (2^q-1)^2+2 (GC864, PROVED, CL103); first
  excursions biject onto nonzero return words (GC865, PROVED, CL103); the compressed graph is the physical-root tree
  plus nonroot cycles (GC866, PROVED, CL105, CL137) — G273
- Return budgets: complete-source mean live chain <= 2^q (GC869, PROVED, CL106); dyadic strata mean <= 2^q +
  2^(q/2) - 1 (GC870, PROVED, CL131); exact dependent spread (GC872, PROVED, CL129); individual cap saves a factor q
  (GC890, PROVED, CL119); G203 tightens it to m - 5a + 6, fixed-baseline counting CLOSED (GC892, PROVED, CL119) —
  G274 .. G276, W277
- RW instrument: depth caps and initial max-live REFUTED by hand (GC868), repaired (L490, PART, source audit), small
  caps guarded (L491, PROVED, source scope); RootedReturn.lean's statement matches the census walk (GC867, PROVED,
  source scope)
- W278 .. W281, the driver row: boundary-only matching (GC894, PROVED, CL120; shortcut CLOSED); driver-row freedom
  (GC895, PROVED, CL121); the one-bit response interval (GC896, PROVED, CL122, L510); multiple-driver XOR and measure
  guards (GC897, PROVED, L511); same-child fibres (GC899, PROVED, L511); alternating-child fibres recover the
  driver (GC901, PROVED, L512); q = 4 fibre starts are nonphysical (GC903, PROVED, CL126; transfer CLOSED)
- Doubling entries: the fourth child is primitive with weight q/4 .. q/2 (GC904, PROVED, CL127); sharp q/4 forces
  an alternating union and a one-parity source (GC909, PROVED, L514); one-parity odd sources give both sharp entries
  (GC911, PROVED, CL132); mask shortcuts CLOSED (GC912, CL133; GC913, CL134); mixed-parity sources reach q/4 + 1
  (GC914, PROVED, CL135); entry children's three-state language (GC916, PROVED, CL136); the next profile has weight
  3q/4 (GC917, PROVED, L516); physical controls refute a sustained floor (GC918, PROVED, L519/CL138)
- Sharp entry's fourth profile k = 1_(pi+1) + S^-1 f + S^-2 f, weight q/2: sharp weights run q/4, 3q/4, 3q/4, q/2 —
  PROVED (Cloud CL138, second-read L520/GC919; all 556 sharp entries to q = 32 agree) — CL138
- Sharp entries agree through k, then split: l = 1_(pi+1) + S^-3 f + S^-2 f (1 + S^-4 f), weight q/4 + tau, tau the
  twisted-cycle changes of f's half-word — PROOF-SKETCH (Cloud; all sharp entries to q = 32) — CL143, SL2
- Conventions: RC88's zero-started 88/371 reconciled with physical ancestry (GC907, COMPUTED, scope); ZF's chain
  weights and repaired guards (GC908, GC910, PROVED, source scope, CL130)

## Correlations, entropy and traces
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
  CL118, L507); weighted witnesses (GC891, PART)

## The left front, triangles and the right edge
- Left diagonals eventually periodic, power-of-2 periods (known: Jen 1986, Rowland §5) — COMPUTED — §8.27, §8.30
- Lemma B1 (white, then black), B2 (periods unbounded), B3 (no white run over twice the band's period) — PROVED —
  §8.59; B2 for the single seed is in print (Nersissian Theorem 13)
- Rowland's question answered both ways: >= 4 certified left sides; 60 generic rows share one — COMPUTED — §8.31
- Leftward speed 0.246 = 1 - 0.41 x 1.84, by the identity v = 1 - P(heal) E[jump | heal] — PROVED (identity),
  MEASURED (values) — §8.66
- The order ends at an exact boundary B(t), a walk near x/t = -0.25 — COMPUTED, MEASURED — §8.74
- Left-only horizon next to 0101 is W + 17; slow walls stop every width-16 seed within a period — COMPUTED — §8.69
- Every white triangle is exact (shrinks two cells a step); every climb on black reaches the origin in t moves —
  PROVED — §8.18, §8.29
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
- Theorem B: with P-periodic columns 0 and 1, P >= 2, no forced zero run exceeds 2P - 2 — PROVED — §8.54
- Theorem A′, the window principle: a block of two columns recurs at a′ only if its length <= L + a′ — PROVED —
  §8.58; its Collatz twin is Terras's bijection (COLLATZ-PRIZE.md §5)
- Theorem A‴: a repeat of the trace, a white run in the later row, stays a growing distance below A′ — PROVED — §8.59
- Jen 1990 for every eventually zero left half: no eventually periodic column 1 — PROVED — Proposition 7, §8.13
- GPT's audit of A, B, A′, E, E″ and §8.59 — PROVED (first pass) — RULE30-GPT.md G2
- Not found in print (limited search): A and A′ "NOT FOUND; NEAR"; E "NOT FOUND" — PRIOR-ART.md
- Theorem A and its no-two-periodic-columns corollary machine-checked in Lean — PROVED — TheoremA.lean, L501, GC882
- TheoremA.lean matches entry 5 (GC882, PROVED, source scope); its hand time re-basing is formal in WhiteEnd.lean

## Other walls, other periods and sibling rules
- Strip ranks certify eventual phase forcing: two tables bound onset (GC919, PROVED, CL139); one bounds bad visits (GC920, PROVED (CL140)); kernel untested — L515.
- Periods 3 to 6: Theorems A, A′, B, E hold for every period — OPEN (parked) — board Rung 3; §8.42, §8.62
- Black-end walls 0 1^q excluded for finite seeds at q = 7 and every q >= 9 — PROVED — entry 38 (SG L429, GC806
  read in L430, WT L431; method from an external repository, gap GC805); q = 1..6 and 8 OPEN
- Black end: exact records p = 3..8 to 32 free bits, LR holds; white end: the latch lemma, too weak alone —
  COMPUTED, PROVED — board (the two Condrey ends); §G11, G12, G13, G14
- One-hole layers: width 5 forces the hole bit to 0 for odd p >= 11; p = 5, 7, 9 narrow to width 22 without closing
  — COMPUTED — OH, OHC, OHD; GC850 (G.GPT271)
- One-hole walls under random right halves: p = 5 alternates between locks (column 1 period 10, about 1,000 holes,
  kicked at a constant 1.0e-3 a hole) and free stretches; p = 7, 9 keep about 0.36 and 0.56 bits a hole, stationary
  — MEASURED — HE, HE2, HE3, rule30_cloud_hole_entropy.py
- One-hole TRUE language by SAT: exact counts to 17, 15, 14 holes; certified rho <= 1.512835, 1.642221, 1.709537
  (p = 5, 7, 9): below width 22's c_60 roots, but only p = 9's beats width 22's own radius (1.714447; L504); zero
  entropy still OPEN — COMPUTED (CaDiCaL UNSAT, integer Collatz-Wielandt) — TC, rule30_cloud_hole_truecount.py,
  CL114, CL116; GC871, GC877
- Free pairs to the reached length: p = 9 (000, 001), p = 7 (00, 010), p = 5 (10, 111000), but p = 9's pair
  fails at 30 holes (001001001000000001001000000000 unrealised; CaDiCaL and kissat) — REFUTED as free —
  FP, FP2, rule30_cloud_hole_freepairs{,_long}.py, CL114, CL123
- The TRUE 0101 channel to 39 visible bits certifies only 0.1517 bits, not below §8.20's 0.1236; a product with the
  layer automaton is the suggested next step — COMPUTED — TC2, rule30_cloud_channel_truecount.py, CL113
- Kopra's marker-word barrier does not rest on symmetry; K4 (moves -3, -1, +3): centre eventually white, other
  columns decided only for |j| <= 64 — PROVED (centre) / COMPUTED — rule30_cloud_lone_column.py, CL088, GC829
- Columns of linear CA are 2-automatic (a known theorem, rechecked); restart lemma (0 in S: eventually periodic
  means purely periodic, of a power-of-2 period) — PROOF-SKETCH — rule30_cloud_lone_column.py
- Slow walls 0^a 1^b: injection rate log2(a + 1)/(a + b), reset for b >= 3a + 1 — PROVED — G15, G18, G19 (§8.63)
- Rule 210 (Rule 30's velocity): LR false; no finite seed keeps the full 0101 clock; not verbatim for Rule 30 —
  PROVED — §8.65, §8.70; entry 32 (Proposition 19), GC479; entry 29, Entry 31
- Rule 90: no finite configuration has a period-2 column (Lucas); the search sees Rule 60's counterexample —
  PROVED, COMPUTED — Proposition 5; §8.3
- One-sided Jen route + Theorem A excludes, for finite seeds: the white end 1 0^q, q >= 10 (entry 40); the black end
  q >= 14 (L497); 139 more words of period 10 .. 18, none at p <= 9 (entry 41) — PROVED (CL110, CL111, GC880; Lean
  WhiteEnd, JenRoute: L508, L513) — rule30_white_end_jen.py, rule30_word_jen_census.py, L498, L499
- Strip test fails for every primitive word of period 3 .. 6 (radius 9) and every open Condrey case (radius 11) —
  COMPUTED — rule30_rung3_strip.py (RG, WE), rule30_strip_c.c (SGC), L488
- One-hole: closed exactly at p = 8 and p >= 10 (nine black steps lock 01; Lean BlackLock, P8Lock); exact relaxed
  forms p = 9 x^4-2x^3+x-1, p = 7 x^5-x^4-x^3-x^2-x+1 (GC857); beside the true 0 1^4, hole word 10000 never occurs —
  PROVED / COMPUTED — G.GPT271, OH, TB, OHD; L476, L479, L480, L496
- One-hole certified ceilings a hole: width-22 radii p = 3, 4, 5, 6, 7, 9 <= 1.220382, 1.231763, 1.471227, 1.383947,
  1.599414, 1.714447; times TC's F, p = 5, 7, 9 <= 1.461900, 1.590415, 1.697625 — COMPUTED (verified) — LP (ODD ..
  ODD3), L504, L506
- Lean audits: BlackLock (GC873, PROVED, source scope); P8Lock, exact three-word equality needs a prefix
  certificate (GC878, PART); WhiteEnd (GC893, GC898, PROVED, source scope); JenRoute (GC906, PROVED, source scope);
  the white end replayed at width 8 (GC880, PROVED); fourteen WC walls certified (GC881, COMPUTED)
- FP2 audits: the longer-prefix formula is sound and its guards repaired (GC900, GC902, PART; GC905, PROVED, source
  scope; CL123 .. CL125)

## Routes closed (do not reopen without new evidence)
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
