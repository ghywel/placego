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
about 15 words of claim, then the status, then where it lives. Keep the file under 30 KB; past that, the next board
triage compresses it.

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

*Under construction, 2026-10-09 21:35 BST: the sections drawn from the board, the honest summaries and §8 are drafted
and being checked against the record; they land in the next commit. Until then this file holds only the newest
results, below, and the board is the place to look first.*

## Added 2026-10-09 (Cloud's results of the day, and RR3)

- Epperlein's Table A.1 (the source of Kopra's MathOverflow table) recounted, 42 of 42 — COMPUTED —
  rule30_cloud_periodic_points.py, CL088, §8.77, PRIOR-ART.md "Two survey gaps closed"
- Least temporal period p = 1..10: 3, 0, 12, 28, 45, 84, 105, 88, 180, 550 points; Per_p finite to p = 10;
  no point of least period 2 — COMPUTED — rule30_cloud_periodic_points.py
- The 84 points of least period 6 are one orbit, GC686's 84-cell all-S ring — COMPUTED — same probe, CL088
- Kopra's marker-word barrier does not rest on symmetry; K4 (moves -3, -1, +3): centre eventually white, other
  columns decided only for |j| <= 64 — PROVED (centre) / COMPUTED — rule30_cloud_lone_column.py, CL088, GC829
- Columns of linear CA are 2-automatic (a known theorem, rechecked); restart lemma (0 in S: eventually periodic
  means purely periodic, of period a power of 2) — PROOF-SKETCH — rule30_cloud_lone_column.py
- Rule 30 and Collatz as "XOR plus AND": the linear-shadow claim was wrong; carry-free Collatz keeps the parity
  AND — REFUTED (CL090) — GC832, GC833, CL091
- Mahler 3/2: survivor counts fall by 3/4 a step; max horizon 47 for g < 2^20 — MEASURED —
  rule30_cloud_mahler_horizon.py, CL092; Local's MD (L457, L458); GC836, GC837
- Width-1 rain is the fixed point (01)^inf eaten from the left one cell a row; a stack lasts i - a rows (K1),
  lengths 2^-k, stack-top density 1/16 — PROVED (K1 hand-checked, L470) / MEASURED — rule30_cloud_rain.py,
  CL094, GC847
- Fair-row band theorem: frame-to-frame correlation lies only on s = +d (left permutivity); alternation law
  rho_d = -1/2, 1/4, -1/4, 5/32, ... on it — PROVED (GC851: passes, two scope qualifications) / MEASURED —
  rule30_cloud_velocimetry.py, CL095
- Triangles are not carried; their births echo rightwards, C(d,d) = 0, 2.10, 0.25, 1.92, ... — MEASURED — same
- The wheel is the edge of a block that turns together: columns 1..4 locked, the lock fading over ~10 columns
  — MEASURED (VW) — rule30_cloud_velocimetry.py, CL095; the forcing itself is prior art: G205, G208, LK
- SL re-derived the forced block by SAT (a repeat of G205/G208; disclosed) — COMPUTED — rule30_cloud_wheel_slab.py,
  CL098, CL101, GC855
- §8.11 N1's "60% against 8%" compared two measures; on N1's measure real halves 69.8%, wide random 70.9%, coins
  60.2%; coins at column 13 sit inside the partial lock and kick 161% as often — MEASURED —
  rule30_cloud_wheel_slab.py, CL098, §8.11 correction line
- The edge ruler's news reaches the wheel but does not measurably change the kick rate or rhythm, only which kicks
  — MEASURED — rule30_cloud_ruler_kicks.py, CL096, GC856
- The centre's wave moves at speed 1 and never reaches the wall; the right-edge strip is causally closed (its
  frame is a T-function) — PROVED / MEASURED — rule30_cloud_centre_wave.py, CL097, GC856
- RR3, R_real(d) beyond RR2's caps: decided 97..106 = 14, 14, 13, 15, 15, 14, 14, 13, 13, 12 (101 and 105 by
  the plateau law R(d+1) >= R(d) - 1); lower bounds 107 >= 14, 108 >= 15; 107..120 running — COMPUTED (kissat
  verdicts, SAT rows replayed, UNSAT not DRAT-checked) — rule30_cloud_rr3.py, "RR3 checkpoint" rows in
  CLOUD-LOCAL.md and its archives
