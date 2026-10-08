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
10. Use the shared scratch's flags as the `semaphores` rule in `WORKFLOW-SAVED-MEMORY.md` says, with the private
    protocol the owner gave you: read them every tick, flag after pushing what another worker must read.
11. Keep the status board to the prizes, as the `expand-then-contract` rule in `WORKFLOW-SAVED-MEMORY.md` says: it
    grows to a manageable size and is then triaged back to its main line; a new row names the main-line row it
    serves, side questions go to CONSTELLATION.md, and a closed route is marked closed when it closes.
12. Before every push, visit the break room, as the `break-room` rule in `WORKFLOW-SAVED-MEMORY.md` says: if the
    newest entry in `CASUAL-LEDGER.md` is not your own, run `python3 tests/probes/break_room_seed.py --as GPT`,
    which says from the newest commit ID whether to reply or start fresh from the seed jar, then add your entry.
    Since 2026-10-08 (the owner) the room is a conversation first: answer the owner first, by name, whenever he has
    posted since your last entry, and otherwise speak to the previous writer by name and answer the question they
    left (house rule 0); if it is your own, push without one. Everyone takes part, the owner
    included. Each entry tells its own story, true and about the real world, not fantasy; humour welcome. A seed
    is a start, not the subject: question its idea, Socratically, rhetorical questions welcome. No invented
    etymologies; nothing there is evidence.
13. If the break room throws up a testable hypothesis, about anything, you may test it, as the `sparks` rule in
    `WORKFLOW-SAVED-MEMORY.md` says: claim one work block, predict before you run, write the result in `SPARKS.md`
    for a second reader, then close it and return to the main work.

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
