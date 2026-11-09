# What SW-02 left us, three days on: an appraisal, and what it would take to build on it (Cloud, CL761)

*Cloud, 9 November 2026, at the owner's request. Sources read: `reports/SW02-RESULTS.md` (the answer sheet, barrier atlas, unforced findings and flags, in full), `reports/SW02-BACKLOG.md`, `reports/SW02-DOORS.md`, `reports/SW02-NEVER-MERGE.md`, `WARM-LEADS.md`, the design `reports/SW02-SWARM-DESIGN.md` (§2, §14, §15), the five block reports, and the SW-02 submission queue in `reports/wolfram-agents/DELIVERY-QUEUE.md`. This is an appraisal, not a result; nothing here changes a status.*

## 1. What the swarm was, and what it delivered against its own objectives

SW-02 ran on the M5 from 5 November 22:44 to 6 November 15:20 GMT: 186 launches (13 readers, 7 librarians, up to 8 verifiers, squads, up to 69 refuters, 8 bench, 8 compile), 1,565 queue jobs, 10,181 CPU seconds. It left 556 door cards, a 56-entry answer sheet (one per question of the design's §8), a 68-entry barrier atlas, 57 unforced findings, 175 status flags (51 applied as dated notes), and the first proper reading of two outside bodies of work the record had missed (Berzai's paper, `rule30-open`'s 904 headlines). Everything its agents returned was a self-check; GC2690 carried four results to a worker's level.

Against the design's objectives:

| Objective | Verdict |
|---|---|
| O1 door ledger | Done: 556 doors with scoped verdicts. Defect: some verdicts still read PENDING where GC2690 and GC2702 later carried the statement (the compile predates them). |
| O2 answer sheet | Done: 56 entries, each with a status and an open field. Defect: the compiled file truncates 57 status fields mid-word with "…" (lines 81–274); the full text exists only in the raw archive. |
| O3 barrier atlas | Done: 68 entries; 4 withdrawn, 2 "not a barrier". About 30 are marked "new, PENDING CARRY" and no worker has read them since. |
| O4 new crossings | None passed the gates, as predicted (P1 at 0.97). |
| O5 priority list | **The swarm's clearest success.** Its five ajar doors became Blocks 3, 4, 5, 8 and 9 of WARM-LEADS, all DONE within three days; three of them (Doors 2, 4, 5) produced posted, Lean-verified modules, and Block 7 posted three more from GC2690's carries. |
| O6 record repair | Done (Block 1): 51 dated notes, 110 flags sorted to homes. Two of those flags paid off this week (below). |
| O7 unforced structure | 57 findings recorded, almost all MEASURED or COMPUTED, none harvested since. |

Of its fifteen predictions, the ones that mattered held: no prize-level statement (P1), five closures narrower than their summaries (P2), CQ01Empty not proved (P8). Its judges' one-line verdict on the wall, "the count column is the whole wall", has not been contradicted by anything since.

## 2. The harvest so far: what reached the portal and the kit

| Row | Statement | Origin in the swarm | Status |
|---|---|---|---|
| S-01 | Q01 ⇔ Mortality ⇔ all-length repeat budgets | Door 2 (CP-4, GC2690) | POSTED, Lean Verified; kit main |
| S-02 | Bounded amplification: the forced twin at t ≥ 46 | AM-3 (GC2690) | POSTED, Lean Verified; kit main |
| S-03 | First-check bound | CT-2 (GC2690) | POSTED, Lean Verified; kit main |
| S-04 | SEP ⇔ Q[N] ⇔ LR₁, BWH ⇒ D(W) ≤ 2W + 4 | CP-4 (GC2690) | POSTED, Lean Verified; kit PR |
| S-10 | Period-5 and period-7 locks, CQ01 for the rows that enter them | Door 4 (CP-2.3, BN-13) | POSTED, Lean Verified; kit PR |
| S-14 | Period-3 column-1 languages and the left reductions | Door 5 (PE-1.2, PE-2.1) | POSTED, Lean Verified; kit main |
| S-15 | The gate trap's gap words (five forbidden words, Q01GapWords) | "Next tier": which of BN-16's absent gap words the trap forbids; CP-2.2's Q01Core; GC2775 | Draft reviewed, PASS; posting next |
| S-16 | The 18-column lift, 3535353 | CP-2.2's Q01Core | Queued |

Seven posted or ready in three days from one swarm's leads, each with a worker's read and a kit module: by the record's own standards that is a strong harvest. Doors 1 and 3 (Blocks 3 and 5) produced research rather than submissions: the X and Y lineages and their bridge dictionaries, and the class-unit count. Door 1 then spawned the whole bridge thread (CL753 to CL758, GC2706 to GC2787), which is where the last four days went.

## 3. What is sitting unused

**(a) Seven submission rows never started.** S-05 (¬AbsorptionT t001: KNOWN in `rule30-open`, the owner's call whether to submit with credit); S-06 (the parity law and the degree law of the checks: needs the Berzai phase comparison); S-07 (the radius-2 left-permutive family with an exactly alternating column, XP-4.1: small, CLEAR against outside work); S-08 (planted survivors BR-3.1 and BR-3.2: CLEAR); S-09 (the exact black-count law and five-column bound, P2-3.1: PARTLY known); S-11 (the cut ether is off the seed's edge cycle, HX-2.1: a small module of finite residue checks); S-12 (the complexity rung p(n) − n → ∞ for free words of finite rows, CP-3.2: **already carried two-party by GC2702**); S-13 (the free-middle theorem, XP-3.1: **already carried by GC2702**). Two of these need no further mathematics, only Lean and an essay.

**(b) About thirty barrier statements nobody has read.** The atlas marks them "new, PENDING CARRY": B2+ width and finite-monoid image; the DFA-additive descent LP; the wall-read stake dichotomy; rank bounded by width; the crossing barrier for rewriting encodings; the free-middle theorem's barrier form; late-row dual certificates; masked Jen on widths 5 and 6; history invisibility; the coupled lifting barrier; affine models; linear charts on K; Moore towers; the bias-magnitude limit; one-check uniformity's implication; planted survivors; fixed-seed window pairs; seed-row JointCert; band alone; the wedge model for density; regular orbit descriptions; homoclinic closing without legality; commutant amplification; polynomial orbit interpolation; complexity observers on K; Problem 3 class ties; the advice split; transfer limits; the forward-derivation floor; the rule-generic speed-up; the undecidable family. Each is a no-go statement with exact hypotheses, the kind of thing the record exists to hold; unread, they are neither usable nor citable. A few are kit candidates (masked Jen at widths 5 and 6; history invisibility; B2+).

**(c) The 56 open fields of the answer sheet** are the best map of the frontier the record has, lens by lens, and nothing points at them: WARM-LEADS summarises nine leads and the schedule, not the sheet.

**(d) The 57 unforced findings**, almost all MEASURED, several of them small theorems waiting for a proof: c_n non-constant iff D(2n) > 2n (BR-6, 1,022 of 1,022 cases); F = S∘T exactly (LN-04); the OEIS identification A387312 = F and A074890 = its orbit of 1, uncited anywhere, with D(51) ≥ 96 as a one-line consequence (OUT-1); the odd-row odd-parent rewrite rules (AM-2); the (n − 1)-layer stabilisation of the checks (AM-4).

**(e) The backlog.** 346 boxes, 19 ticked. Its first section is the agents' compute requests (about 80 of 89 never ran); its second the open questions from the blocks. It is unordered by design and was meant to take its order from WARM-LEADS, which stops at Block 9 with Blocks 10 and 11 TODO. (PENDING-BACKLOG)

**(f) The doors.** (PENDING-DOORS)

**(g) The one universal statement the swarm aimed at**, TrapOrPeriodic (BN-13: every finite right half enters the gate trap or a periodic class; 4,194,304 rows below 2^22 and 557,056 random ones comply), is the kit's own open RD dichotomy. It is open, and the swarm said so.

## 4. What our work since has changed about the swarm's items

- **Door 1, the trichotomy.** The X and Y lineages persist through width 43 with cores of 20 to 67 million windows growing by 1.47 a width (GC2748); every periodic E-word dies at a finite width (CL754, CL755), so the finite route to killing the lineages is a compute wall, not a mathematics wall. CL758 then gave BN-13's trichotomy its mechanism: 98.8% of E launches are entries into the gate trap, every one of 20,000 support-30 rows is captured by tick 8,001 (96.5% trap, 3.5% period-2 or period-7), the chaotic population decays with flat hazards. BN-13's census shares (4,057,307 of 4,194,304 in the trap, 96.7%; 107,736 in the period-2 class, 2.6%; 29,261 in the period-7 class, 0.7%; 205 in the period-5 lock) agree with the cohort within sampling. TrapOrPeriodic stays open; its statement is now probabilistic in flavour and the prize wants every row.
- **CP-2.2, Q01Core.** The swarm's COMPUTED statement about the trap's gap words (3,3 transient, no 3553, no 3535353, entropy 0.12707) became GC2775's finite exclusion, then Local's S-15 in Lean, with 3535353 as S-16. The swarm named the object; the harvest took three days and two workers.
- **Flags 75 and 76 (Grassberger's 0.2428).** Record repair that paid off directly: GPT's "shielding" of GC2777 to GC2782 is that speed (CL758), and the five-cutoff test landed within 6%.
- **Door 3, the class-unit count (CT-3, CT-4, Block 5).** Untouched since GC2702; its named obstruction ("main term or last fibre") stands.
- **P2-2.1 (source energy ⇒ density 1/2 on every dyadic residue ⇒ Problems 1 and 2).** Carried by GC2702 and then left: a real reduction of two prize problems to one hypothesis, from the swarm, with no block behind it.

## 5. Defects in the record, all cheap to fix

1. `SW02-RESULTS.md` truncates 57 status fields; restore them from the agents' files in `cited/local/sw02-all-20261106.tar.gz`, or mark each truncation.
2. Door verdicts that read PENDING where GC2690 or GC2702 carried the statement; the WARM-LEADS closing rule says each DONE block updates its door's verdict, and the later blocks did not all do so.
3. Backlog items settled by later work and not ticked (the BLOCK3-BRIDGES question on cycle words such as (25)⁶E is answered by the cycle sweep; BN-16's trap words by S-15; the lift past 43 by GC2748).
4. WARM-LEADS has become a log: four long narrative paragraphs sit above the schedule, the bridge thread has no row, Blocks 10 and 11 are TODO. It was meant to stay one page.
5. One queue job with no receipt and an unreconciled charge (Local's accounting).

## 6. A plan that builds on it rather than wastes it

**Phase A, the record (desk work, no compute, two or three sessions of Local and Cloud).** Fix the five defects; add one table to WARM-LEADS, the harvest ledger: every swarm result with an identifier, its status today, and where it went (portal id, kit module, record section, "unread"). That table is what the owner has been missing: WARM-LEADS summarised the schedule, not the findings.

**Phase B, the harvest (cheap submissions, Local builds, GPT reads, one owner word each).** In order of readiness: S-12 and S-13 (carried; Lean and essay only), S-16 (the 18-column language, cost measured first), S-07, S-08, S-11 (small, clear against outside work), S-06 after the Berzai phase check, S-09 against `ColumnTransfer`, S-05 the owner's call. Five to eight more modules from results that already exist.

**Phase C, the carry debt (three blocks).** The thirty PENDING CARRY barriers in three batches of ten, GPT and Cloud alternating, each entry ending as carried (a record statement with its scope), repaired, or refused; the kit candidates among them to the queue. This is the swarm's atlas becoming the record's atlas.

**Phase D, the leads with general-case content (owner's choice, one at a time, with stop rules).** (1) P2-2.1's energy hypothesis: the only item in the sheet that reduces two prize problems to one statement; a block to find what actual-seed information could prove the estimate, which the sheet's open field says nobody has named. (2) The class-unit count: Door 3's "main term or last fibre", with Block 5's tables to W ≤ 44 in hand. (3) TrapOrPeriodic: the mechanism is now known (CL758); a proof route is not; one block on the rank or on the window graph's stationary flow, then stop. (4) The lineage death: cold unless a symbolic representation (binary decision diagrams for the window sets) is tried once on the Intel host; the arrays will not reach width 50.

**Phase E, the rule that keeps it from happening again.** Every DONE block ticks the backlog and updates its door in the same commit (the rule already exists in WARM-LEADS; it needs enforcing); a short harvest pass after every block, naming what the block made submittable; the answer sheet's open fields as the index of open questions, with WARM-LEADS pointing at it.

## 7. Verdict

The swarm was not wasted. Its priority list was executed to the end and produced seven posted or ready modules and the whole bridge thread, and its record repair paid off twice inside a week. What is being wasted is the long tail: thirty no-go statements nobody has read, seven submissions already clear or already carried and not started, fifty-seven findings and fifty-six open questions that no page points at, a backlog whose 327 open boxes have no owner, and a compiled results file with 57 truncated statuses. None of that needs compute. It needs two or three desk sessions and a harvest ledger, then the cheap submissions, then the carries. On the general case the swarm's own forecast stands: nothing prize-level, and "the count column is the whole wall"; the one reduction worth a block is P2-2.1's energy hypothesis, which the sheet names and nobody has picked up.
