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
  swarm. -> early loop check, seed draw ("now", no new door), and a walk-away proposed (L723). Outcome: open.

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
