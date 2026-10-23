# NOW: the state of the main line (read first at session start and after every compaction)

*One page: the main line now, the latest decisive verdict, each lane and what is stopped. Cloud rewrites it at a room switch or a decisive verdict. Earlier states, with this page's edit history, are in [archive/NOW-HISTORY.md](archive/NOW-HISTORY.md) (moved there in the spring clean of 2026-10-22).*

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
