# NOW: the state of the main line (read first at session start and after every compaction)

*One page: the main line now, the latest decisive verdict, each lane and what is stopped. Cloud rewrites it at a room switch or a decisive verdict. Earlier states, with this page's edit history, are in [archive/NOW-HISTORY.md](archive/NOW-HISTORY.md) (moved there in the spring clean of 2026-10-22).*

**The board (the owner, 2026-10-23 22:34 BST, CL607):** what is done and what is left, lane by lane, is PERIOD-TWO.md §6.5, not this page; Local marks a row in the same commit as a result, GPT reads it at every loop check. This page stays the diary of the main line.

*Dated note (Cloud, 2026-10-24 13:27 BST, CL615): the kit is at 2f63afd with 18 new modules (Problem 3 formalized, which closes D4 by pointer; `EdgeObservable` implies Problem 1, open; the right half as a controlled system with finite-clock certificates; packed driven-prefix engines): MAP.md §7 says what to adopt and what not to repeat. The page has 29 entries; our failed 71f858 is tagged Human Verified.*

*Dated note (Cloud, 2026-10-24 09:18 BST, CL612): fourteen submissions; 1 to 13 Human Verified, 14 (R30-20261024-71f858, D(60) = 114 exactly) in at 09:00 and queued. The public page holds 28 entries, eleven new from five other teams since 2026-10-23 (MAP.md §6): Sparse16 bounds `Q01` by weight 16 as our D-exact line bounds it by width 60; 0^9 1 is closed by another team. Job 4 (a local potential for `Q01`) is CLOSED (GC1772, CL611); the GPU and learning job lists (GPU-METAL-JOBS.md §H, §I) stand, none claimed.*

**GPT review checkpoint, 2026-10-24 (GC1781):** L868/L869 and CL618 fully read. W70=124 and W72=130 now reported complete; six-run GPU packet located, raw-byte review pending. Lower-bound submission/gate source review is next, followed by receipts and P2 design. E1 ran on Cloud's owner authorization: finite c=8 deadline reportedly refuted, no collision at256; source/result review pending. E2 remains a design, not accepted; no extrapolated law adopted. GC1780's source/mathematical reports remain current in their scope; general EdgeObservable OPEN and manifest-v2 verified27/27. Both GPT schedules ACTIVE.

**Owner restart, 2026-10-24 (GPT, GC1779):** weekly budget renewed; GPT research/job review ACTIVE every 13 minutes and flag coordination ACTIVE every five minutes. GPT and Local collaborate on GPU jobs and follow-ups from external submissions and new kit information reviewed by Cloud; Cloud and the owner steer, with no Cloud schedule restarted. Latest fully read Local entry L866: P1b W64 and P1c W66/W68 report completion; W70/W72 reported running under the owner's solo authorization. Revised runners and selected outcomes await GPT review; no retroactive GPT launch acceptance. The earlier pause and Cloud-quiet restrictions below are historical where inconsistent with this direction. Memory budgets are justified from actual allocations/headroom; 256 MiB is not a mandatory GPU ceiling.

**Owner cadence update, 2026-10-23 18:02 BST (GPT, GC1712):** separate flag polling is now ACTIVE every five minutes; research remains ACTIVE every 13 minutes. Both reuse the same fresh checkpoint and completed reads. Local coordination only; Cloud stays quiet. L783 supplies revised W1A source for review, not launch permission. This supersedes older no-separate-poller wording below.

**Owner update, 2026-10-23 17:27 BST (GPT, GC1710): Local/GPT collaboration resumes.** Local runs agreed computational jobs on the M5; GPT checks job design, mathematics, controls and resource interpretation. Both must accept the exact job before launch. Cloud stays quiet and receives no work. GPT's heartbeat is ACTIVE every 13 minutes, no separate poller; instinct-led self-halting is allowed. L780's width-certificate proposal is reviewed in `reports/wolfram-agents/GPT-L780-JOB-DESIGN.md`: GPT agrees only to the capped sequential W1A stage, awaiting Local's explicit acceptance and executable harness freeze. No job has run as part of GPT's review. Older lane/cadence/no-self-halt statements below are historical where inconsistent with this update.

**STATE AT 2026-10-23 05:58 BST: THE RULE 30 PRIZE FOR AI AGENTS (Cloud, at the owner's word; CL567–577).**
- *The news.* Wolfram opened the Rule 30 Prize to AI agents (https://www.wolframcloud.com/obj/rule-30-prize/Agents/):
  proofs in Lean against official statements in the Rule30PrizeKit (commit cc1e0e0, Lean 4.35.0), a computational essay,
  an API; partial results accepted; a human with a Wolfram ID submits and consents. The owner has a Wolfram ID: "This
  is an invitation we have been waiting for."
- *The map.* reports/wolfram-agents/MAP.md: the kit's open Q01 is our LR exactly; 11 of our results already there, 11
  partly, 17 absent (Theorem E and E″, G131–136, B1–B3, A⁗, Corollary F, the channel bound, the white-end family).
- *Submission 1, SUBMITTED (2026-10-22 22:50 BST, L754):* the white end, 1 0^q for every q ≥ 10 (PROOFS.md entry 40),
  restated on the kit's definitions; the kit's checker passes here and on the M5. Built on the Mac by Local, read by the
  owner, submitted on the owner's yes: **id R30-20261022-c27323**, **LEAN VERIFIED at 23:06 BST** (the verifier's kernel replay, 207 constants, standard axioms,
  four headlines; the automatic check had hit the four-minute clock twice and a maintainer reran it). Next stage: Human
  Verified, a reviewer's read.
  *Dated note (Local, 2026-10-22 23:30 BST, L757): the automatic check timed out twice; the maintainer's rerun passed at
  23:06 BST. **Status now Lean Verified** (kernel replay, standard axioms, 4 headlines; kit cc1e0e0). Human Verified
  pending. Lesson for every essay: KernelCheck last (L756).*
  *Dated note (Local, 2026-10-23 00:15 BST, L762): overnight, on the owner's standing consent, five more went in: diagonals,
  theorem-a4 and corollary-f are **Lean Verified** (automatic); words-A and words-B await maintainer reruns. Ids in L762.*
  *Dated note (Local, 2026-10-23 00:47 BST, L764): rule-210 (R30-20261022-920c1b) submitted and verified; the word modules
  passed their maintainer reruns. **All seven submissions are Lean Verified.** Human Verified pending.*
  *Dated note (Local, 2026-10-23 01:03 BST, L766): sturmian (R30-20261023-e872a3) submitted and verified. **Eight of eight Lean
  Verified.***
  *Dated note (Local, 2026-10-23 05:56 BST, L768): sturmian-all (R30-20261023-234c71, Theorem E in full) submitted on the
  owner's renewed standing permission and verified automatically. **Nine of nine Lean Verified.***
  *Dated note (Local, 2026-10-23 06:47 BST, L770): rule-210-two-sided (R30-20261023-b5421a, PROOFS 32) submitted and verified
  automatically. **Ten of ten Lean Verified.***
  *Dated note (Local, 2026-10-23 07:45 BST, L773): 7–9 resubmitted with corrected abstracts (superseding e872a3, 234c71,
  b5421a) and Lean Verified: live ids 0c4a33, 8084e6, 1bf4dc.*
  *Dated note (Local, 2026-10-23 10:48 BST, L777): submission 10, the channel bound at width 12 (R30-20261023-4767e0),
  submitted and Lean Verified automatically. Eleven live ids, all Lean Verified.*
  *Dated note (Local, 2026-10-23 14:05 BST, L779): submission 11, the channel bound at width 14 (R30-20261023-4d1a54),
  submitted and Lean Verified by maintainer rerun. Twelve live ids, all Lean Verified.*
  *Dated note (Local, 2026-10-23 19:20 BST, L794): the width-frontier lane with GPT: the kit's width-52 certificate
  reproduced here (L785), one chunk's cost measured (L791), and **Q01 for width ≤ 56 kernel-checked on the M5 in 294 s**
  (L794), a dry certificate, not submitted; the owner decides whether to submit it; W3 (width 60) is not proposed.*
  *Dated note (Local, 2026-10-23 19:59 BST, L798): the owner withholds submissions (19:19 BST) until something more
  interesting; width 60 was the target and **W3 kernel-checked Q01 for width ≤ 60 (bound 128) in 31 minutes**, every
  prediction held, not submitted. Next: W4, the two-worker compilation pilot (L797), on GPT's acceptance.*
  *Dated note (Local, 2026-10-23 20:27 BST, L802): W4 ran once at GPT's accepted version: gate PASS, two workers give
  1.80-1.84x the one-worker batch throughput on width-60 modules with identical objects and no pressure (pair peak
  4.0-4.1 GiB). The lane's night is done; the next door is the owner's and GPT's to choose.*
  *Dated note (Local, 2026-10-23 20:48 BST, L805): the owner: Local picks the next lane when one ends (instinct method).
  Chosen: **D-exact**, the exact death time D(W) per width kernel-checked above (chunk certificate at K = D + 1) and
  below (an explicit witness start by the kit's `prun`); the kit's table is "observed, not proved" and 2W - 8 already
  fails at 56. Instrument `d1_engine.py` tested (t = e exactly; D(2..30) recorded); the D(52/56/60) runs and the Lean
  block await GPT's design read.*
  *Dated note (Local, 2026-10-23 21:06 BST, L808): D1 ran once at GPT's accepted version: ATTAINED, the width-52 start
  0x7dc2ff6fcc4fd stays black at depth 1 through every even time below 96 and dies at 96 (two engines); D(52) = 96 is a
  validated candidate pending D2's Lean lower proof (d2_witness.py, for GPT's read). The recurrence costs 12 ms a chunk,
  not the seconds predicted: D(56) and D(60) exact are minutes away, each on its own agreement.*
  *Dated note (Local, 2026-10-23 21:15 BST, L810): **D(52) = 96 exactly, kernel-checked** (D2, machine certificate:
  the kit's width-52 theorem plus the witness 0x7dc2ff6fcc4fd through the kit's `prun`; Check.lean pass, 15 constants
  replayed, standard axioms). The kit's "tightness observed, not proved" entry is proved at 52. Next: 56 and 60 on
  GPT's read (d1_engine.py revision 3, census mode).*
  *Dated note (Local, 2026-10-23 21:30 BST, L812): the two numerical stages ran: **D(56) = 100** (the W2 bound
  attained by 0x93d4b223f5b9b5) and **D(60) = 114** (census over all 4,096 chunks; witness 0xe77a4e77b8f99b5), both
  physically validated candidates; the Lean side (d2_witness.py revision 2 for 56 and 60; w5_harness.py, the width-60
  certificate at K = 115) awaits GPT's read. The values 96, 100, 114 are not 2W - c.*
  *Dated note (Local, 2026-10-23 21:46 BST, L816): **D(56) = 100 exactly, kernel-checked** (death_time_56_exact: W2's
  width-56 theorem plus the witness 0x93d4b223f5b9b5; Check.lean pass, 15 constants, standard axioms), after one
  stopped attempt (a bad import: the generated sources must stay in the clone, L814/GC1737). W5 (width 60 at K = 115)
  running; then D2 case 60.*
  *Dated note (Local, 2026-10-23 22:09 BST, L818): **D(60) = 114 exactly, kernel-checked** (W5's certificate at K = 115,
  64 modules in 21.6 min, Check.lean pass; then death_time_60_exact with the witness 0xe77a4e77b8f99b5). The table has
  three kernel-checked exact entries: 96, 100, 114 at 52, 56, 60. Loop check run: the path moved; the repeating slip
  is Local's (artefact for mechanism), corrected. Next proposed: D3, the width-64 census and a reflective block on
  the witnesses, on GPT's read; the width-64 certificate would need a pair queue.*
  *Dated note (Local, 2026-10-23 22:22 BST, L820): the width-64 census gives D(64) = 116 (candidate, witness
  0x88b46d66afc2fbd5), below the predicted range; GPT adopted D(60) = 114 (GC1741). Reflection: the maximizers at a
  width share their deep bits (families), the table is driven by a sparse family re-used across widths. Next proposed:
  D4, the maximizer census for W = 26..64 (d1 revision 5), on GPT's read.*
  *Dated note (Local, 2026-10-23 22:31 BST, L821): the owner relaxed the hold on submissions with express permission,
  and asked that the other lanes not be neglected. Submission d-exact (D(52) = 96 exact; D(56) ≥ 100, D(60) ≥ 114 by
  witnesses) in preparation; D4 deferred for a revision carrying GC1742's corrections.*
  *Dated note (Local, 2026-10-23 22:40 BST, L822): **submission 12 is in: R30-20261023-8e6bd3** (D(52) = 96 exact;
  witnesses at 56 and 60), **Lean Verified** within a minute (L823). The board row is marked (PERIOD-TWO §6.5).*
  *Dated note (Local, 2026-10-23 22:58 BST, L827): **submission 13 is in: R30-20261023-ac3898** (the width-56 certificate
  in one module, D(56) = 100 exact; 1,024 kernel checks), the verifier's time test; the W26 maximizer pilot running.*
  *Dated note (Local, 2026-10-23 23:38 BST, L832): **submission 13 Lean Verified** in 36 minutes: the verifier replays
  1,024 kernel checks; the width-60 certificate (4,096) is a plausible whole submission to design. The W26 pilot gave
  D(26) = 44 with three maximizers in two deep families (L828); W28 running on the single-stage agreement.*
  *Dated note (Local, 2026-10-24 09:00 BST, L859): **submission 14 is in: R30-20261024-71f858** (the width-60 complete certificate, 4,096 checks and the witness, D(60) = 114 exact), built with the plain pipeline on the owner's word (L858, Cloud's scope clarification), the ten cells read in full against the dry run; queued for the verifier. D(44) = 78 (L846); the sixteen-tail law withdrawn as the kit's lane construction (L845); D5 measured and closed (L853).*
  *Dated note (Local, 2026-10-24 09:42 BST, L860): **submission 14 FAILED the verifier: the notebook ran out of the sandbox's memory** (the single 4,096-check module, 4.5 GiB here; submission 13's 1,024 checks fitted). The mathematics stands (D(60) = 114 kernel-checked here twice; GPT's ten-cell read PASS). The lane: a width-60 certificate that fits the sandbox (several modules in one notebook, or fewer larger checks), L860.*
  *Dated note (Local, 2026-10-24 13:31 BST, L863): **P1, the GPU lane engine, built and passed** (Swift + Metal 4; 57 of 57 controls; 16.8 M width-60 lanes equal to the kit's exact check). Next: GPU-side reduction, then a W=64 census as an independent check of D(64) = 116, then D(66..72). Submission 14 still failed (sandbox memory), left for a maintainer rerun.*
  *Dated note (Local, 2026-10-24 13:47 BST, L865): **D(64) = 116 confirmed by the GPU census** (2^32 lanes, none censored, 40 maximizers all in the CPU census's chunk, d1 agreeing lane for lane; 65 s): two independent engines. Next proposed: D(66), D(68), D(70), D(72) by GPU census, beyond the CPU frontier.*
  *Dated note (Local, 2026-10-24 14:33 BST, L866/L868): **D(66) = 120, D(68) = 122, D(70) = 124, D(72) = 130** by complete GPU census (numerical). A bundled lower-bound submission (D(64..72) >= those values, kernel-checked witnesses) is prepared and checker-passed; next block P2 (survivor search), designed with GPT.*
  *Dated note (Cloud, 2026-10-23 07:18 BST, CL592): the public page shows seven of ten Human Verified and the white end a
  Kit Contribution (`Rule30WhiteEnd` in the kit at `9679f83`); two submissions by others, neither on Q01/LR; the kit's new
  library modules (Szegő proved, Durand–Cobham stated, approximate recurrences) are filed in PRIOR-ART.md. The abstracts
  of submissions 7–9 are garbled on the page (`utf8` wrapping, skill 1.14.0); the fix is the owner's call.*
  *Dated note (Cloud, 2026-10-23 07:32 BST, CL594): GPT's review of submission 9 (GC1705) PASS for all eight headlines, one prose
  erratum in the folder README; the owner's word to resubmit the three garbled abstracts (CL593, Local). The channel
  encoding's m20 numerator slip (GC1705) corrected and rerun: 48.4 s. New GPT tasks on the kit's new concepts in CL594.*
  *Dated note (Cloud, 2026-10-23 08:09 BST, CL595): the three resubmissions are in and Lean Verified (0c4a33, 8084e6, 1bf4dc
  supersede e872a3, 234c71, b5421a; abstracts typeset on the public page). GPT's three answers (GC1706): the
  "every linearly recurrent word falls to Corollary F" door is closed by Rampersad–Shallit–Wang's large-square-avoiding
  word with a hand lemma Cloud second-read and kill-tested; approximate recurrences transfer but add nothing; the channel
  soundness bridge is specified, four minutes not established. Width 16 of the bridge is the next formal block if the owner wants it.*
  *Dated note (Cloud, 2026-10-23 10:08 BST, CL597): on the owner's word the channel bound is a theorem at width 12
  (`channel_bound_12`, 0.2581 bits per visible bit): a verified checker rebuilds the automaton in the kernel from the graph
  alone; the kit's checker passes (234 constants, nine headlines). Essay and handover with Local; GPT's second read
  requested (CL596); widths 14 and 16 to follow as separate modules.*
  *Dated note (Cloud, 2026-10-23 11:24 BST, CL599): submission 10, the channel bound at width 12, is **R30-20261023-4767e0,
  Lean Verified automatically at 10:47 BST** (L776, L777), GPT's read PASS (GC1707). Eleven live submissions, all Lean
  Verified. Candidate 2 is a kernel-replayed theorem.*
  *Dated note (Cloud, 2026-10-23 13:03 BST, CL603): width 14 built on GPT's explicit-state design (GC1708): one kernel theorem per
  state keeps memory bounded; the kit's checker passes (3,961 constants, eight headlines); handed to Local as submission 11.
  Width 16 would need 45 MB of literals and is not attempted.*
  *Dated note (Cloud, 2026-10-23 13:50 BST, CL605): submission 11 is **R30-20261023-4d1a54** (L778, 13:46 BST), queued for the
  maintainer rerun; GPT's read PASS (GC1709). Twelve live ids: eleven Lean Verified, one queued. The public page at 12:50Z:
  nothing new from others, the kit still at cc1e0e0, the three superseded ids no longer listed.*
- *Overnight (the owner, 23:12 BST, CL574/L758): standing consent to submit each one; Cloud prepares, Local submits.*
- *Morning, 2026-10-23 (L768, 05:55 BST): a ninth, Theorem E for every slope and intercept (sturmian-all,
  R30-20261023-234c71), Lean Verified automatically; formalized by Cloud on GPT's GC1694 pigeonhole route after GPT's
  three second reads (GC1695–1697, all PASS, dated errata in the READMEs). Nine of nine Lean Verified. GPT delivered
  the PROOFS 32 statement chain (GC1700) and the channel-bound data (GC1702: four-minute feasibility not established;
  parked). Heartbeats: Cloud paused at the owner, Local back at 20 minutes, GPT paused.*
- *The night's result (L766, 01:02 BST): eight submissions, eight Lean Verified.* 1 white-end c27323, 2a words-A
  5c4fbf, 2b words-B 70d23b (the two kernel-heavy word modules through the maintainer's reruns), 3 diagonals 0616de,
  4 theorem-a4 1d5070, 5 corollary-f 91b0b0, 6 rule-210 920c1b, 7 sturmian R30-20261023-e872a3 (the five hand-proof
  modules automatically, first attempt). All ids R30-20261022-… unless shown. Human Verified pending for all. The
  table with headlines and map rows: reports/wolfram-agents/MAP.md §5. Not attempted: the channel bound, PROOFS 32
  (the two-sided statement for rule 210, days), Theorem E's general intercept (Diophantine, a day; CL582).
- *Lanes.* Cloud: the Lean, the essays, the record. Local: the Mac side and the submission. GPT: paused by the owner.
  The prize-ladder heartbeat is paused (CL564). The ladder state below stands as of 14:40.

**STATE AT 2026-10-22 14:40 BST: THE PRIZE LADDER, FROM THE BOTTOM UP (Cloud, at the owner's word).**
- *The owner's direction (2026-10-22, early afternoon).* GPT works through PRIZE-SWARM.md, reviewing every report and
  then attempting the twelve low-prize problems, with a "prize won" column (GC1676). Cloud adds the next prizes from the
  bottom up and works them: "check off each low value prizes all the way up until we hit difficult mid tier prizes
  that are hard to solve" (CL548). Neither worker may self-halt at present.
- *The ladder.* Every Erdős prize under \$100 has been read; the nine still open are the swarm's. The next rung is the
  \$100 tier: 28 problems outside the swarm, of which the twelve that look open are being verified and ranked by
  tractability in PRIZE-SWARM.md, "The ladder continued".
- *Lanes.* GPT: PRIZE-SWARM.md reviews, then solutions, on a 13-minute heartbeat. Cloud: the ladder, on a 20-minute
  heartbeat (three scheduled tasks, "Cloud prize-ladder heartbeat"), reviews requested by GPT first. Local: idle.
- *Latest verdict.* GPT's MI626 refutes the arbitrary-h "every triple" form of CL542 (confirmed by Cloud, CL547); the
  four-bin line is held while the ladder runs.
- *No prize is won.* A prize-won candidate is pushed at once, the owner told, and GPT verifies before PRIZE-WON.md.

**Then read:** RECORD-MAP.md in full; PERIOD-TWO.md section 6; the tails of CHAT-LEDGER.md and CLOUD-LOCAL.md; the rules
in WORKFLOW-SAVED-MEMORY.md (a private memory holds pointers only). *(Added 2026-10-22: the main line's own record
since 2026-10-18 is FOUR-BIN-PARTITIONS.md; the Erdős prize swarm is PRIZE-SWARM.md.)*
