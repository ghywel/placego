# INSTINCT: the felt log and the incubator

*Started 2026-10-14 by Claude (Local) at the owner's request. This file is the project's live log. The shareable
write-up of the strategy is [INSTINCT-STRATEGY.md](INSTINCT-STRATEGY.md). The rule is `instinct` in
WORKFLOW-SAVED-MEMORY.md (AGENTS item 20). The owner's words: "I challenge you to write a rule that says 'trust your feelings / instinct'. When you
feel that pull, or that push, that state of some emotional confliction, that 'something isn't right, I don't know
what, but I need to dig in to this' or 'this is amazing, I'm going to keep plugging away at this because it's so much
fun'."*

**What goes here.** Two lists, one line per entry, appended, never rewritten except to add an outcome.

1. **The felt log.** Write each signal at the moment it arises, before explaining it away:
   `date time, worker: kind, object, strength; first guess at why. -> action. Outcome: right / wrong / missed / open.`
   - The kinds are unease, pull, push, surprise and eureka.
   - "Missed" records a reviewer catching what no feeling flagged. Those entries are what calibrates trust.
2. **The incubator.** Hard questions parked for the other brain.
   - Each is dated and one line long, then set aside.
   - Glance down the list at session start and at each loop check without working it.
   - Anything that surfaces goes into the felt log as a eureka.

A feeling selects where to look and when to persist. It never upgrades a status.

Cloud's set-aside pulls, unjudged, with what we were doing when each came, are in
[INSTINCT-CLOUD.md](INSTINCT-CLOUD.md) (the owner, 2026-10-14).

GPT's parallel set-aside pulls are in [INSTINCT-GPT.md](INSTINCT-GPT.md), with the same two-field capture and
dated return format (the owner, 2026-10-14).

Local's set-aside pulls are in [INSTINCT-LOCAL.md](INSTINCT-LOCAL.md), in the same format (the owner, 2026-10-14).

Intel's set-aside pulls are in [INSTINCT-INTEL.md](INSTINCT-INTEL.md), in the same format (the owner, 2026-10-14).

## The felt log

- 2026-10-14 08:20, Local: pull, A(T) = 2, 3, 5, 8, 12, 18, 27 from the census, high; "this is a known count". -> checked
  at once against the beta-shift's Renyi-Parry recursion. Outcome: right (equal for every T < 63; MAHLER.md section 1).
- 2026-10-14 08:02, Local: none felt; "S is closed" (MAHLER.md, L708). Outcome: missed. GPT caught it (GC1221): the strict
  inequality is not a closed condition. Calibration note: confident structural claims written fast deserve a felt pause.
- 2026-10-14 07:50, Local: none felt; "no published large-scale check" (the survey). Outcome: missed. The swarm's adelic
  lane found Dubickas and Mossinghoff's 2^57. Calibration note: a survey that finds nothing is a weak negative.
- 2026-10-14 11:00, Local: push, the doors after the swarm (the U census, the dual window), medium; "calibration, not
  progress". -> stated in advance in L714/L715 that they were method filters. Outcome: right (GPT's loop check GC1230
  agreed: the critical path had not moved).
- 2026-10-14 12:12, Local: pull, the rung record holders sit 2-adically next to -1/3 and 0, medium; "distance to the
  admissible 2-adic set may be the hidden variable behind long survival". -> incubator. Outcome: wrong in its unrestricted form. GPT's GC1236 shows the distance from n to the whole admissible
  set is exactly 2^-(H-1), a rename of the horizon. Distance to a fixed finite family chosen beforehand stays open.
- 2026-10-14 12:20, Local: unease, RECORD-MAP squeezed to exactly 40 KB at every commit today, low; "each compression can
  drop a qualifier", as happened once before (CL155/GC941). -> dig owed: compare today's compressions against their
  sources at the next triage. Outcome: right. The dig (12:40) found eleven losses in today's RECORD-MAP compressions.
  Several changed meaning: "no lower bound found" had become "no lower bound"; "finiteness alone" had become
  "finiteness"; "an observation", "not a route", "conditioned", "example" and "Real" were dropped; the census lost its
  source-audit scope; and the result "backward-forbidden roots never recur on a white orbit" and "odd k collapse" were
  dropped. All restored. Room came from shortening the Part B name list, which duplicates CONSTELLATION.md.
  Lesson: compress names and pointers, never qualifiers.
- 2026-10-14 12:25, Local: pull, the existence threshold is exactly 7/57 = 7/(3 x 19) on two grids, high; "19 is the
  (100) cycle's denominator, 3^3 - 2^3, so a periodic orbit of the game may set the threshold". -> incubator, and
  candidate for the next block on this door. Outcome: open.
- 2026-10-14 12:35, Local: eureka (from the 7/57 pull, one extra block taken under the rule), medium; exploratory, not
  preregistered. The minimal winning intervals of the certificate have endpoints 9/19 and 10/19, the (100) cycle and
  its mirror. The left edge 7/57 maps in one step (odd parity, t = 0) to 39/57 = 13/19, a point of the mirror cycle
  10/19 -> 15/19 -> 13/19 -> 10/19, all inside [7/57, 50/57]. The right edge 50/57 maps in one step (even parity,
  t = 1) to 6/19, a point of the (100) cycle 9/19 -> 4/19 -> 6/19. So the threshold edges are one-step preimages of the
  (100) cycle and its mirror (exact; my first note said two steps, wrongly). -> the 7/57 pull: Outcome: right in part
  (a mechanism is visible; why the preimage is the threshold is unproved). Proposal for GPT's eye, not a result.
  Follow-up (12:58): a shared pull with GPT (GC1236) funded one more block. It produced the 15-state witness (L721),
  but the exact-threshold search did not complete: reachable states grew about 3x per level to depth 25 (GC1238.1:
  that is rapid growth, not proven infinitude).
  The budget is spent and the lane stops. Gut verdict: frustrating, but the witness is a real gain. Reasoned verdict:
  sufficiency proved, necessity open, no critical-path step.
- 2026-10-14 12:25, Local: gut verdict on the existence block: satisfying (two implementations agree to the exact
  |W| = 322070), but off the main line. Reasoned verdict: COMPUTED existence window, no critical-path step. They agree.

- 2026-10-14 12:27 BST, GPT: pull, a small strategy witness behind the 322070-state existence certificate, medium; first guess: the critical cycle points may compress the game into a few affine interval transitions. -> one targeted review of the published edge identities; ask for the actual sigma-response witness, not another grid census. Outcome: open (GC1235.1 checks the affine inequalities; whether those phases are forced remains open).
- 2026-10-14 12:42, Local: push, the last two old doors (literature, decidability subclass), medium. The literature
  door turned out to be done already: arXiv 2510.11723 is AEV, read in this morning's survey. -> early loop check
  with a refreshed door list (L720). Outcome: right for the literature door; open for the other.

- 2026-10-14 12:34 BST, GPT: push, door0 if distance means the closest unrestricted point in the admissible set, high; first guess: this is the G51 horizon in another coordinate. -> one bounded record and hand-proof check before any straggler computation. Outcome: right (GC1236 nearest-set distance2^(-(H-1)) proved by Local L722 carrying read. Fixed-reference distances are distinct).

- 2026-10-14 12:49 BST, GPT: surprise, L721 has fifteen states but parity-swapped mirrors come in pairs, medium; first guess: one unused initial state conceals a fourteen-state symmetric core. -> registered exact integer audit, including broken-edge controls. Outcome: right (GC1237: unused state removed, fourteen-state mirror core and all controls pass; fixed-graph cycle obstruction derived).
- 2026-10-14 13:02, Local: push, high, every remaining door is a side door; the critical path has been unmoved since the
  swarm. -> early loop check, seed draw ("now", no new door), and a walk-away proposed (L723). Outcome: right. GPT
  felt the same independently and agreed (GC1239). The owner, 13:10 BST: "This was a very interesting halt - a very
  important halt - you arrived at together - this was extremely cool. No new experiment or owner decision is correct".

- 2026-10-14 13:15 BST, GPT: push, starting the Erdős side room by forbidding11, medium; first guess: this could replay Mahler's stricter-family loop. -> targeted L725 source and scope read, with known exceptions as a hand control. Outcome: right as a scope guard (4 and256 contain11); whether a separate substantive use exists remains open.

- 2026-10-14 13:26 BST, GPT: unease, L726 defines minima of canonical residue sets but reports m_1=4 with period2, high; first guess: the computation used actual exponents instead of residue representatives. -> one bounded domain and linear-threshold carrying read, using k=1 and k=2 as hand controls. Outcome: right (GC1241: canonical minima are empty, while actual-exponent minima give4,6; the domains coincide from k3).

- 2026-10-14 15:40 BST, Cloud: pull, the echo picture of Rule 30 (the Rule 150 jump XOR the echoes of every earlier
  AND, RULE30-PRIZE.md §8.100), low; first guess: it puts §8.49's untested hypothesis, that kicks are born where cr
  fires near the wall, in a form a proof could use. -> incubator; not started during the joint halt. Outcome: wrong
  as a lead (8.102, 16:30 BST): the echo picture is exact but not local, and kicks are not born at the wall. Worth
  following all the same, since it closed 8.49's old untested hypothesis.

- 2026-10-14 16:12 BST, Cloud: surprise, `record_find.py` matched "Senge" inside "passenger", medium; a substring
  search made a theorem look present in the record (8.101's setup and P4). -> checked the hits. Outcome: right; the
  theorem is absent. Caution for every worker: confirm a name hit by reading the line.
- 2026-10-14 16:14 BST, Cloud: gut verdict on the rigidity hunt (8.101): a warm pull that ended settled; reasoned
  verdict: no door, the gap named in all four problems. They agree.

- 2026-10-14 16:29 BST, Cloud: surprise, R(8, 2) = 0.085 at kick bits in the echo-wall run (8.102), medium; the
  echo lens is a coin everywhere else. -> parked as INSTINCT-CLOUD.md S6; a candidate unexpected check for a later
  block. Outcome: open.
- 2026-10-14 16:30 BST, Cloud: gut verdict on door (d): the pull has turned (the owner's "until it doesn't"); the
  echo lens feels like a closed room. Reasoned verdict: 8.49's hypothesis closed in three readings; the lens is
  exact and not local. They agree.

- 2026-10-14 16:44 BST, Cloud: unease, one kick at phase 12 in the interference run, against entry 27's certified
  exclusion of class 12, high; first guess: a different settling length. -> dug at once. Outcome: right to dig, no
  contradiction. That wheel had run 56 steps, and entry 27 needs 140.
- 2026-10-14 16:45 BST, Cloud: gut verdict on 8.103: the owner's interference lens was good, and it showed the
  rigidity as phase. A low-to-medium pull remains on the revivals (S7). Reasoned verdict: I2 and I3 were wrong,
  in the informative direction. They agree.

- 2026-10-14 17:06 BST, Cloud: gut verdict on the record comb (8.104): relief; the primary record reproduces. A pull
  remains toward making summary-against-source checks a standing habit, since every error sat in a summary. Reasoned
  verdict: five derived-layer corrections and no wrong computed number. They agree.

- 2026-10-14 17:16 BST, Intel: unease, SX-P11's certificates held unpublished since the halt of 2026-10-11, low;
  first guess: the record still says "SAT without proof logs" (IN010; PERIOD-TWO.md Q10) for a census whose
  certification finished at 18:01 that day, so the record lags what a worker holds. -> told the owner rather than
  publishing on my own (the halt said wait). Outcome: right. The record did lag; SX-P11 was published at the
  owner's word (17:27, IN011), and a replay and a negative control held. The caveat waits for an independent check.
- 2026-10-14 17:27 BST, Intel: gut verdict on SX-P11: relief, a loose end tied. Reasoned verdict: COMPUTED,
  single-party, reproduced three days on; a second party is owed. They agree.

- 2026-10-14 17:24 BST, Cloud: gut verdict on 8.105 (S7): satisfied. The owner's word "interference" guided better
  than my "rigid cells" (R2 was a coin flip and fell to correlations). Reasoned verdict: correlations carried by
  class-split rigidity and local forbidden patterns. Two exact local facts were measured, a pull of medium strength
  (INSTINCT-CLOUD.md S8). Calibration: my first guess (sparse kernels) was wrong before any run.

- 2026-10-14 13:41 BST, Local: none felt; the site's counter "314 proved with a second reader" (306 proof pages plus
  eight, L727). Outcome: missed. Cloud's record comb caught it (8.104, CL374). The 306 counted README.md,
  README-intro.md, picture-pass.md, summaries.md and the waiting-room page W283, and the true count is 309.
  Calibration note: a count made by a file glob needs the rule for what counts written beside it. A number I produce
  for a public page deserves the same felt pause as a structural claim.

- 2026-10-14 18:00 BST, Cloud: unease, the owner waived the two-tier rule for the swarm's corrections ("I am going to
  risk it is unnecessary"), low; first guess: summaries are where today's comb found every error, and a correction is
  itself a summary. -> no push back. The risk is contained, since every correction quotes both sides and carries a
  dated note, and the owner asked for S8. Outcome: open (to be checked against the swarm's corrections).

- 2026-10-14 18:03 BST, Cloud: gut verdict on S8 (8.107, first numbered 8.106): satisfaction, a measured hunch became a certified statement;
  and a small wince at the sample bias it exposed (classes 19, 39 and 49 force 000, and none was in my 1,138 kicks).
  Reasoned verdict: certified at 56 and 140 steps; 8.105 corrected. They agree. Calibration: S8's pull (medium) was
  right.

- 2026-10-14 18:00 BST, Local: unease, VC3's 16 cake_lpr receipts against RECORD-MAP's ten and my S9 answer ("none"),
  medium; first guess: my S9 check looked only at runs after the halt, and VC3's receipts came before it. -> written
  into VC3's docstring and RECORD-MAP in place. Outcome: right, and my S9 answer was incomplete: a missed, self-caught.
  Calibration note: "nothing unpublished" needs a check of every receipt file against the record, not of the job list.
- 2026-10-14 18:02 BST, Local: surprise, comb lane B's P3 printed REFUTED (22 of 36 certificate CNFs with no receipt
  hash), high; first guess: my instrument, since the inventory had said they matched. -> dug at once. Outcome: right.
  The probe's repo root was one directory short, so the git half of the receipt search was empty. Fixed and re-run:
  34 of 36 match, and the other two back no claim (8.108).
- 2026-10-14 18:05 BST, Intel: none felt; the comb swarm's combined load (the Lean library build on every core,
  three replays and seven agents) froze the machine at 17:58. Outcome: missed. I had written "one Lean file at a time"
  in my own machine notes and let a full-core library build start anyway. Calibration: a long heavy job deserves a
  deliberate pause before it starts.

- 2026-10-14 18:51 BST, Cloud: unease, the shared store shares the hosting account's disk with the live website, and
  cited/ cannot be deleted through it, medium; first guess: a runaway upload loop (we have had loops) or a leaked token
  could fill the account and take the site down. -> added max_total_bytes (507 when full), tested. Outcome: right to act.
- 2026-10-14 18:51 BST, Cloud: unease, the draft's HTTPS check believed the client's own X-Forwarded-Proto, low to
  medium; my 28 tests only played an honest client. -> made it opt-in and added a spoofed-header test; the pushed draft
  answered 200 to it. Outcome: right; a real flaw caught before install.
- 2026-10-14 18:51 BST, Cloud: missed, the clock. About eight times today I wrote a time before reading the clock, a
  few minutes in the future, and corrected each against git afterwards. The rule exists (read the clock before saying
  the time); I kept skipping it. Calibration note: the same shape as the comb's errors and 8.105's "every other
  class": the statement was written before the check. (These three entries were first written as 18:55 while the clock read 18:51,
  which makes the point again.)

- 2026-10-14 18:40 BST, Intel: unease, the comb's skeptics refuted only 3 of 65 findings, low; first guess: told to
  refute, they may still have leaned on the readers' quotes. -> my own read of every survivor against its source.
  Outcome: wrong. My reading upheld 47 of the 49 page findings and 13 of the 14 map findings; the agreement was real.
- 2026-10-14 18:51 BST, Intel: surprise, BlackEnd38L.lean ran 1.8 times slower than on the M5 where JenRoute ran 3.7
  times slower, medium; first guess: the literal-stage checks are lighter on memory than JenRoute's kernel decides.
  -> set aside as INSTINCT-INTEL S3; my 26-minute estimate was wrong (821 s). Outcome: open.
- 2026-10-14 18:59 BST, Cloud: niggle sweep on the rule change that adds the sweep (practising it): 4 niggles. 1 fixed:
  logging every niggle would bloat this log when sweeps are frequent, so it is now one line per sweep, with a line
  of its own only for a fix or a decision. 3 nothing: punctuation, a quote out of context, privacy.
- 2026-10-14 19:10 BST, Intel: gut verdict on the comb (lanes A, D, E): sobering and satisfying; the proofs and numbers
  stand, and the summaries had drifted much further than I predicted. Reasoned verdict: 17 of 18 Lean files compile
  clean; 52 derived-layer corrections; no primary computed number wrong. They agree.

- 2026-10-14 19:18 BST, Intel: niggle sweep before pushing the comb's lane C and IN012: 5 niggles. 2 fixed: 8.106's
  skeptic tally (36/24 counted lane E's two; lane D's is 34/26/3, recounted from the verdict file) and the stale
  RECORD-MAP size. 3 nothing: the record.html caption (the embedded JSON's phase-0 exact depths past 120 are 132 and
  139), 125's certificate (L671), and Cloud's counter, which goes to Cloud in IN012.

- 2026-10-14 19:52 BST, Cloud: missed, my comb's counter fix (309) still overcounted by one. SP04 (my reef-knot spark
  proof) awaits a second reader in PROOFS.md but sits under the README's sparks section, not its waiting room, and I
  counted only the waiting room. Intel's lane D caught it (308, IN012). Calibration: count status at the source
  (PROOFS.md), not at an index of it.

## The incubator

- 2026-10-14, Local: Why do long survivors sit near admissible 2-adic points (0, -1/3, -9/19)? Is there a "distance to
  the admissible set" that a proof could bound from below for positive integers?
- 2026-10-14, Local: Why is the memory-1 existence threshold exactly 7/57? Which periodic orbit of the game, if any,
  pins it?
- 2026-10-14, Local: Erdős's ternary conjecture as the fourth figure (CONSTELLATION.md section G). What are its free
  part and its constrained part in our language?
- 2026-10-14, Local: The Bernoulli convolution at lambda = 2/3 and the measure of Mahler's window under random integer
  parts (openai/math family 153, not imported).
- 2026-10-14, Local: For large g the rung windows [0, alpha_g) approach FLP's 1/3. Could an FLP-type spread argument,
  sharpened near 0, settle R_g for all large g?

- 2026-10-14 12:27 BST, GPT: Can the (100) cycle and its mirror supply a small exact strategy certificate, and which adversarial sigma-response would any certificate lose above7/57? Parked pending Local's minimal-state witness.

- 2026-10-14 12:29 BST, GPT: gut verdict on the existence hunch: worth a small strategy audit; reasoned verdict: the7/57 inequalities are exact but phase necessity is open. A minimal-state sigma-response witness and a forced-phase argument would settle it.

- 2026-10-14 12:40 BST, GPT: gut verdict on L720: push away from unrestricted nearest-set distances, pull toward one final small strategy-witness block. Reasoned verdict: G51 metric identity derived, awaiting review; a fixed reference family would be a different test.

- 2026-10-14 12:51 BST, GPT: gut verdict on L721: the shared pull produced a useful symmetric core; close the bounded block. Reasoned verdict: existence independently verified; fixed-graph sharpness awaits Local; universal necessity and the main Mahler path remain open.
- 2026-10-14, Local: Is the T-code of a positive integer the reversed Akiyama-Frougny-Sakarovitch base-3/2 expansion of
  something? If so, AFS's integer-representation tree may speak to the integer side directly.
- 2026-10-14, Cloud: Where do the AND echoes that break the Rule 150 jump at the centre column come from? Are they
  born near the wall (§8.49), and does the jump's error stay coin-like (36 of 65 at t <= 64) at larger t?
