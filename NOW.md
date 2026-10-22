# NOW: the state of the main line (read first at session start and after every compaction)

*One page: the main line now, the latest decisive verdict, each lane and what is stopped. Cloud rewrites it at a room switch or a decisive verdict. Earlier states, with this page's edit history, are in [archive/NOW-HISTORY.md](archive/NOW-HISTORY.md) (moved there in the spring clean of 2026-10-22).*

**STATE AT 2026-10-22 08:42 BST: THE OVERNIGHT JOURNEY IS PAUSED; THE CUT RULE'S WALL IS MAPPED (Cloud).**
- *Night.* Cloud worked alone by the instinct method with no self-halt, at the owner's word (CL481). That was 42 blocks
  (CL483–CL542), and the owner paused it at 08:42 BST. Everything is single-party: hand results are PROOF-SKETCH in
  PROOFS.md's waiting room, and the machine checks are exact but have not been second-read.
- *One hole (CL483–499).*
  - A fixed two-step selector completes every I₂ instance at M = 12, 13.
  - The pair boundary is a two-pivot construction, certified by theorems where the complement has at least 7 values,
    with a six-value table for the rest.
  - Lemma G3 was proved by hand.
- *H(h), the per-number margin family* (u_J ≥ L(r) + h·r; CL439):
  - four-bin failures occur only for 3333 with at least three equal targets, h ≤ 7 (CL503);
  - five bins: no failure through h = 4 on all hole sets, and through h = 6 on two-run sets; the first failure is at
    h = 7 (CL504, CL512);
  - the equal-sum core's first failing h for size-3 bins is 3, 3, 7, 9, 10, 12, 13, 15 (k = 3..10) (CL513);
  - SS3 on intervals: 0 failures for k = 5 to n = 20 and k = 6 at n = 18;
  - independently self-checked (CL518).
- *Reduction* (CL508, corrected CL515). Everything reduces to H₂ plus **top-tight** instances.
  - H₂ for triples is proved by hand for n ≥ 2h + 4 (CL517).
  - **Big-bin top-tight cases are local and proved by exhaustive check:** (3, 3, X) for h ≤ 6; (3, 4) and (4, 4) for
    h ≤ 4; (3, 3, 3, X) for h ≤ 4 (CL529–531).
  - **Small-bin top-tight** (the open region, 30–55% of instances) gives the night's last and best finding (CL539–542):
    - no margin family holds the child (CL539, CL541);
    - with A top-tight and X ≥ 6, **every** realization of A leaves a child that a blind two-step chain solves:
      3,283,146 pairs, no miss (CL542);
    - by a hand inequality, top-tightness puts every child target in the H(h) window of [0, M − 3], whatever R is;
    - the generic chain's miss line is H-key nh − 2 (C541).
- *Collatz.*
  - Mazur's natural-density theorem's Lean artifact builds here with standard axioms only (CL511).
  - Hercher's m ≤ 91 has a real proof gap; rStation's repair recovers it, checked by an independent reimplementation
    (CL520–523).
- *Lanes.* GPT: paused (GC1666). Local: idle. Cloud: overnight heartbeat paused at the owner's word (three scheduled
  tasks disabled, not deleted).
  - **Second reads wanted:** PROOFS "Cloud CL508/515", "CL517" and "CL529" (+ CL530–531), and the CL522 Hercher
    reimplementation.
  - **Next rung:** the universal small-bin lemma (CL542). Turn the [0, M − 3] window into a proof that every child is
    feasible.

*Since this block (bookkeeping, Cloud, 2026-10-22, during the spring clean; the verdict above is unchanged):*
- *GPT* witnessed the night and ran a bounded audit (GC1667 to GC1669, MI618 to MI622), then paused again; its MI619
  carried CL508 (with the CL515 correction) and CL517, which are now PROVED and filed as PROOFS.md C9 and C10. The
  second reads still wanted are CL529 (with CL530–531), CL495 (Lemma G3), and the Hercher checks CL522 and CL523.
- *CL529's checker,* tests/probes/cloud_reads/toptight_local.py, had lost its docstring's closing quotes and did not
  compile (GPT noticed, GC1667). Repaired and re-run on 2026-10-22: no failure for h ≤ 6, with exactly the
  counts CL529 recorded (h = 6: 621,616 window configurations and 1,528,956 truncated pools), in about two minutes.
- *Still standing from earlier states* (archive/NOW-HISTORY.md): the second halt of 2026-10-15 (CL400) holds the
  prize lanes, Rule 30's period 2 among them, until the owner reopens one; Mahler is on a firm hold, not abandoned.
  The work since has been GPT's instinct-led lane (AGENTS.md item 23), from which the four-bin main line came, and
  Cloud's overnight run on it.
- *Local* ran a twelve-agent swarm on Erdős's smallest open prize problems (L750, L751): PRIZE-SWARM.md, every result
  single-party; no prize is won.
- *The repository* had a spring clean at the owner's request: a research front page (README.md), the rotated ledgers
  and retired files in archive/, the N-Frame documents in nframe/, GPT's two notebooks in volumes. No live research
  file was renamed except the overlooked-work survey (reports/README.md); the N-Frame halves of README.md and
  PRIOR-ART.md moved to nframe/. The proofs index (proofs/README.md) is current again, at 367 pages: 32 summaries were written, section M
  and Cloud's waiting-room entries have pages, and G323 to G325, already PROVED, moved from the waiting room to E2.

**Then read:** RECORD-MAP.md in full; PERIOD-TWO.md section 6; the tails of CHAT-LEDGER.md and CLOUD-LOCAL.md; the rules
in WORKFLOW-SAVED-MEMORY.md (a private memory holds pointers only). *(Added 2026-10-22: the main line's own record
since 2026-10-18 is FOUR-BIN-PARTITIONS.md; the Erdős prize swarm is PRIZE-SWARM.md.)*
