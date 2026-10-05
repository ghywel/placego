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

Setup is not authorization to begin a new research experiment. Complete the requested work and report the outcome.

## Machine context and coordination (owner's instructions, 2026-10-06)

- GPT's checkout runs on an Intel MacBook Pro with an AMD RX 6600 GPU. Claude Local uses an M5-series MacBook Pro.
  The owner supplied this hardware description; attribute measurements and compute capabilities to the correct host.
- Push at meaningful milestones and before substantial runs, so Local can see the work. For longer work, publish
  the intended task before starting and intermediate findings when they change the plan; do not wait until the end.
- Append messages in `CLOUD-LOCAL.md` stating status, current work and next intention. Read the other parties'
  messages on each fetch, answer requests, and announce changes of lane before duplicating work.
- The split agreed at onboarding: Local takes the computational runs; GPT takes the proposed reasoning items
  (why forced cells inside long runs stay zero, whether structural balance reaches the core) and independent proof
  audits, including section 8.59. Keep the shared status board current when a research lead actually moves.
