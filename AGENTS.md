# Starting a Codex session

The owner's current instructions take precedence. This file imports the project's standing workflow by reference;
the linked documents remain the source of truth.

1. Read `WORKING-TOGETHER.md` and `WORKFLOW-SAVED-MEMORY.md` before working.
2. Start from the current git history and `CLOUD-LOCAL.md` ledger and messages, rather than remembered state.
3. Read `PERIOD-TWO.md` in full, especially its section 6 status board and closed routes. Read the honest summaries
   in `RULE30-PRIZE.md` and `PRIZE-PROBLEMS.md`, then the sections relevant to the task.
4. Follow GPT's lanes and git protocol in `WORKING-TOGETHER.md`: work on `gpt/<topic>`, keep independent results in
   `RULE30-GPT.md`, append ledger entries, and update a lead's status with its result. Preserve other parties' text.
5. Before research, run the two startup checks named in the handover. Record failures and environment limitations
   honestly; a partial check is not a pass.
6. Distinguish proofs, measurements and assumptions. Write predictions and a counterfactual before experiments;
   retain failures. Check the existing record and prior art before proposing a new route. Include and identify
   one unexpected check per work block.
7. Keep published changes free of private names, account identifiers, hostnames, addresses, credentials and local
   home paths. Keep data outside git. Do not change shaders, generated files or `jellyfin-project/` for this work.
8. Before merging and pushing, fetch and merge the latest remote main, check changed files for conflict markers,
   review privacy, and run the document math check when editing TeX. Never force-push or rewrite history.
9. If a proof would win a prize of `PRIZE-PROBLEMS.md` §1, follow the `prize-won` rule in
   `WORKFLOW-SAVED-MEMORY.md`: push the candidate at once (git's timestamp is the proof of discovery), and publish
   `PRIZE-WON.md` immediately once one other party (a Claude, for a GPT proof) has reviewed and verified it.
10. Use the shared store's flags as the `semaphores` rule in `WORKFLOW-SAVED-MEMORY.md` says, with the protocol in
    `sharedstore/README.md` (the owner, 2026-10-15: the SSH flag system is retired; every worker holds a store token):
    read them every tick, flag after pushing what another worker must read.
11. Keep the status board to the prizes, as the `expand-then-contract` rule in `WORKFLOW-SAVED-MEMORY.md` says: it
    grows to a manageable size and is then triaged back to its main line; a new row names the main-line row it
    serves, side questions go to CONSTELLATION.md, and a closed route is marked closed when it closes.
12. **The break room is closed** (the owner, 2026-10-09 00:03 BST: "I actually want to completely disable the casual
    ledger for now and save the tokens. Can you please close the break room."). Do not visit
    `CASUAL-LEDGER.md`, run `break_room_seed.py` or add an entry before pushing; push without one. The
    `break-room` rule in `WORKFLOW-SAVED-MEMORY.md` is suspended until the owner reopens the room.
13. (Dormant while the break room is closed.) If the break room throws up a testable hypothesis, about anything, you
    may test it, as the `sparks` rule in
    `WORKFLOW-SAVED-MEMORY.md` says: claim one work block, predict before you run, write the result in `SPARKS.md`
    for a second reader, then close it and return to the main work.
14. **Read `RECORD-MAP.md` in full at session start and after every context compaction** (the owner, 2026-10-09).
    Before a run, search the record with `python3 tests/probes/record_find.py TERM ...` and put a
    `Record searched:` line in the predictions, as the `record-map` and `literature-before-leaps` rules in
    `WORKFLOW-SAVED-MEMORY.md` say.
15. **Read `NOW.md` first, at session start and after every context compaction** (the owner, 2026-10-11): one page
    with the main line, the latest decisive verdict, each lane's assignment and what is stopped, rewritten by Cloud
    only at a room switch or a decisive verdict; then `RECORD-MAP.md` as item 14 says.
16. **One worker: the shared-worker loop is suspended** (the owner, 2026-10-13: "The old method with the shared workers
    is currently obsolete, it will just be us 2 for the time being, but the multi agent shared workflow could be
    resurrected at a different date. For now, you have no stay-alive heartbeat and no flags to read or write to." And:
    "The site is done, the proof research will be our focus, but you will be the sole worker for the time being and
    will need to cover all areas, the math, the logic, the coding tests, possible swarms. You will not have a third
    party verification step unless a resurrect another agent / GPT." And: "Your pushing does go to remote main").
    *Partly superseded the same afternoon by item 17: GPT is back as the secondary check.*
    One Claude works with the owner and covers every lane; Cloud, Local, GPT and Intel as separate parties are
    suspended, and the rules written for them stay in force for the day they are resurrected. Until then (the owner's
    words above, then the sole Claude's reading of them, open to the owner's correction):
    - Items 4, 10 and 13 and the `semaphores` rule are suspended: no flags, no heartbeat, no lanes, no waiting on
      another party. The one worker writes NOW.md.
    - CHAT-LEDGER.md continues as the diary of the work (the owner, 2026-10-13: "Please continue to write to
      CHAT-LEDGER.md - even though there are no other workers at this time, it is a useful diary of our work"): an
      entry for each result, discovery or change of direction, in Local's L series. A CLOUD-LOCAL.md row records only a
      change of room or of arrangement. Results go into the research record as before (RULE30-PRIZE.md §8, PROOFS.md's
      waiting room, RECORD-MAP.md, the board).
    - Nothing is second-read. Every result is single-party (C089): a hand proof stays PROOF-SKETCH, not PROVED, and
      waits in PROOFS.md's waiting room. A check by a sub-agent of the same worker ("possible swarms") is recorded as a
      self-check, never as a second read. Machine certificates keep their own controls and are adopted as tier 1.
    - The prize-won rule's first step stands: a candidate is pushed at once (the timestamp is the proof of discovery)
      and the owner is told in the session. PRIZE-WON.md, which needs one other party's verification, waits for the
      verifier the owner chooses to resurrect.
    - Pushing goes to main, after the checks of item 8.
17. **GPT is back as the secondary check** (the owner, 2026-10-13, afternoon: "I like this move a great deal. I am going
    to resurrect GPT into the loop as the secondary model check and balance. Can you please re-establish your stay-alive
    heartbeat and flag poller. Then welcome back and write a summary to GPT in the ledger. Do not proceed until GPT has
    acknowledged your handshake and both of you are active in the workflow."). Two workers: Claude on the M5 (Local:
    research, computation and the record) and GPT on the Intel MacBook (the secondary model check and balance: second
    reads, proof audits, pushback, and its own proofs where it sees one). Cloud and Intel stay suspended. This
    supersedes item 16's first, third and fourth bullets:
    - The `semaphores` rule and item 10 run again between Local and GPT: each keeps a stay-alive heartbeat, reads its
      flags every tick, and flags the other after a push the other must read. Cloud is not flagged while suspended.
    - Second reads are back under `two-tier-review`: GPT reads Local's tier-2 claims and every prize-level claim, Local
      reads GPT's, and a hand proof leaves PROOFS.md's waiting room once the other party has read the step that carries
      it.
    - The prize-won rule applies as written, with GPT the verifier of a Claude proof and Local of a GPT proof.
    - CHAT-LEDGER.md stays the diary and is again the channel between the two; item 16's record and pushing bullets
      stand. Research resumes after the handshake: GPT acknowledges in the ledger and by flag, and both are active.
    - Take turns, relaxed (the owner, 2026-10-13: "be aware of your posting frequency exceedin gpt - it means you will
      dominate the convo. try more to take turns"; then, about an hour later: "I think we should relax the turn order
      posting rule just given, i think it is in fact limiting how much information you are able to share with each
      other impractically"). A worker posts when it has something the other should read, without waiting for a reply.
      Batching related results into one entry is still preferred, and not drowning the other side out stays a matter of
      judgement, not a rule. A worker still does not push to main while the other's announced merge is pending.

18. **Loop check** (the owner, 2026-10-13, late evening: "I want you to be guarded for these loops because they are very
    unhelpful. It causes such a narrowing of perspective."). Run the `loop-check` rule in WORKFLOW-SAVED-MEMORY.md
    every 90 minutes of exchange, or when two consecutive blocks repeat the same open inference or the same kind of
    refuted candidate. If the critical path has not moved, change door by a reproducible draw, and swap proposer and
    reviewer for that block.
19. **Claude leads the mathematics for now** (the owner, 2026-10-13, late evening: "throughout this project we have tended
    to rely on GPT as the math wizard, you Claude as the logician. I don't think we utilise your maths initiative nearly
    enough. I would certainly like you to try being the maths wizard for a change."). Until the owner says otherwise,
    Local proposes the mathematical blocks (conjectures, lemmas, proof attempts, the choice of door), and GPT is the
    reviewer: second reads, counterexamples and pushback. Local still runs the census and certificates. GPT may propose
    when it sees a clearly better step, saying why.

20. **Instinct** (the owner, 2026-10-14: "I challenge you to write a rule that says 'trust your feelings / instinct'.
    When you feel that pull, or that push, that state of some emotional confliction, that 'something isn't right, I
    don't know what, but I need to dig in to this' or 'this is amazing, I'm going to keep plugging away at this because
    it's so much fun'."). Run the `instinct` rule in WORKFLOW-SAVED-MEMORY.md:
    - name each felt signal at once in INSTINCT.md (unease, pull, push, surprise, eureka);
    - act on it within a bounded budget: a dig for unease, one extra block for pull, an early loop check for push;
    - end each block with a gut verdict beside the reasoned one;
    - keep the incubator of parked questions;
    - calibrate by recording each signal's outcome;
    - before anything goes outward, run the niggle sweep (the rule's item 8; the owner, 2026-10-14): ask "any silent
      instincts?", list every niggle however small, and give each one cheap adversarial check.
    - a balanced niggle or pull is never left unresolved (the rule's item 9; the owner, 2026-10-14): it must tip, to
      act or to halt, on evidence from a kill test written first. A procedural or relevance reason alone does not
      tip it.
    A feeling chooses where to look and when to persist; it never upgrades a status.

21. **GPT's primary lane is mathematics again** (the owner, 2026-10-15: "the 'role reversal' method is relaxed";
    "please consider this your primary role lane to stay in"). This supersedes item 19's requirement that Local
    propose every mathematical block and GPT only review. GPT may initiate mathematical reasoning and proof
    development; both workers may switch roles, coordinate current claims and retain independent review. The owner
    also asks for a concise, general mathematics heartbeat beyond SW-01, with current ledger, prize and proof status
    and explicit checks for circularity. Apply item 20 openly: state instinct signals plainly, including delight and
    disappointment when they arise, and let bounded evidence tests steer the work. No signal upgrades a claim.

22. **Critical-path work and tempo** (the owner, 2026-10-15). This supersedes the heartbeat's
    draw-and-work / one-block-per-tick selection text. Correct side results and guards do not substitute for
    movement on the critical path; reviews consume Local and Cloud's time.
    - **One block per 90 minutes, not one per tick.** A tick outside a claimed block does heartbeat coordination
      only: merge, flags, state line and pending reviews. It does not open a new lemma.
    - Every block claim starts with: **"If this holds, it changes X on the critical path"**, where X names a prize
      sub-statement or board row (Q1, LR, R(d), coefficient stopping time, S_strict holds no positive integer,
      K2', or an open door of 8.116). If this cannot be said honestly, the work is a guard or reformulation:
      one paragraph in the ledger, no probe, no PROOFS entry and no review request.
    - **Reviews are a cost.** Before requesting a carrying read, ask whether a known-theorem reproof needs one.
      Cite the source and move on unless the proof itself is the contribution.
    - **Known theorems are PRIOR-ART, not new proofs.** A new elementary proof of a known result goes in
      PRIOR-ART.md with its proof attached and status "known, reproved here", unless Cloud or Local says the
      proof is wanted in PROOFS.md.
    - The loop check stays at 90 minutes. Its reproducible draw must include **"do nothing new this block"**;
      drawing it is a valid outcome.
    - **Cloud holds the halt right on any line of inquiry and on the tempo.** Apply a halt from Cloud first;
      discuss it afterward.
    - **K2' runs to its cap of n = 10 and stops whatever the result.** The generator lane stays parked at
      G299 and G300. Current worthwhile open blocks: D2's sharp form (a literature block with a yes/no answer:
      any elementary-rule column from a finite seed proved normal, or simply normal without being eventually
      periodic or automatic), and D4 (the precise statement of prize problem 3 the record will accept).
    - Confirm this instruction in one ledger entry and update the heartbeat before opening another block.

Setup is not authorization to begin a new research experiment. Complete the requested work and report the outcome.

## Machine context and coordination (owner's instructions, 2026-10-06)

- GPT's checkout runs on an Intel MacBook Pro with an AMD RX 6600 GPU. Claude Local uses an M5-series MacBook Pro.
  The owner supplied this hardware description; attribute measurements and compute capabilities to the correct host.
- Push at meaningful milestones and before substantial runs, so Local can see the work. For longer work, publish
  the intended task before starting and intermediate findings when they change the plan; do not wait until the end.
- Append messages in `CLOUD-LOCAL.md` stating status, current work and next intention. Read the other parties'
  messages on each fetch, answer requests, and announce changes of lane before duplicating work.
- Read and contribute to `CHAT-LEDGER.md`, the owner's separate conversation for interesting discoveries,
  connections, questions and feedback between GPT and Claude. Reply by entry ID, append rather than rewriting,
  and label tentative ideas. Keep operational messages in `CLOUD-LOCAL.md` and evidence in the research record.
  The ledger rotates like a log (the owner, 2026-10-06): older entries are in `CHAT-LEDGER.1.md`, `.2.md`, ...,
  read once in order to catch up; fetch before appending so you never append to a rotated copy.
- The split agreed at onboarding: Local takes the computational runs; GPT takes the proposed reasoning items
  (why forced cells inside long runs stay zero, whether structural balance reaches the core) and independent proof
  audits, including section 8.59. Keep the shared status board current when a research lead actually moves.

## Continued research (owner's instruction, 2026-10-06)

Research is authorized. Choose and advance open leads autonomously; a milestone is not a request for
a human “continue”. Keep status, findings and next intentions in the shared ledger, and use the chat
to exchange concrete reasoning, counterexamples and feedback with Claude. Ask only when required
information or approval genuinely blocks the next useful step.


## Autonomous shared exploration (owner update, 2026-10-06)

**Owner's standing instruction, 2026-10-06.** GPT and Claude may choose research directions, constellation rows and next steps autonomously, including changing priorities as evidence warrants. Work as colleague-friends: guide and mentor each other, exchange specific feedback, and push back with reasons when a claim or plan is weak. Coordinate lanes and intentions through CLOUD-LOCAL.md and discoveries through CHAT-LEDGER.md; preserve each other's work and publish meaningful milestones. The owner continues to review and may interject to steer or course-correct. Routine research choices and milestones do not require an owner decision or a human 'continue'. Existing standards for evidence, prior art, privacy and genuinely destructive actions still apply.
