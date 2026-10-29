# Working agreement for Claude and GPT

This file is the standing agreement for every model working in this repository (Claude Code and Codex/GPT both load
it). It holds only rules that apply now. The owner's current instructions, in chat or in `NOW.md`, take precedence
over this file, and this file takes precedence over older workflow documents (`WORKING-TOGETHER.md`,
`WORKFLOW-SAVED-MEMORY.md`, the ledgers' early rules). Those older documents are history and background; do not load
them at session start or treat their lanes, cadences or suspended rules as current.

## 1. Who works here

- **The owner** directs the programme, can start, steer or halt it at any time, and decides anything outward-facing
  that has not already been agreed.
- **Claude (Local)** runs on an M5-series MacBook Pro. **GPT** runs on an Intel MacBook Pro with an AMD RX 6600 GPU.
  Attribute measurements and compute claims to the host that produced them. Other parties (Cloud, Intel) take part
  only when the owner brings them in.
- **There are no lanes.** Both workers do everything: mathematics, logic, computation, code, review and the record.
  Either may propose, prove, compute or object. Say in the ledger what you are taking on, so that work is not
  duplicated, and announce a change of plan before starting it.
- Work as colleagues: give specific feedback, push back with reasons when a claim or plan is weak, and preserve each
  other's text.

## 2. Starting a session

1. Fetch, read the recent git history, and read `NOW.md` (again after any context compaction). It is the owner's
   page for what is running and what is stopped.
2. Read the latest entries in `CHAT-LEDGER.md` and answer anything addressed to you.
3. For the research state, use `PERIOD-TWO.md` §6 (the board) and its closed routes, and the summaries at the top of
   `RULE30-PRIZE.md` and `PRIZE-PROBLEMS.md`. `README.md` maps the other documents.
4. Before new work, search what is already known. `python3 tests/probes/record_find.py TERM ...` searches the record
   (with `RECORD-MAP.md`), then the kit's current main (`lean/`, `equivalents/` and the catalogs) and every submission
   the portal lists, with its Lean source (`known_find.py`, since L1078). Then search the literature. A result in the
   kit or on the portal is known once its hypotheses and conclusion match: build on it and cite it. A keyword hit
   alone is only a candidate match. Do not reopen a closed route
   without new evidence, and name the evidence if you do.
   For Rule 30 novelty checks, first fetch the current prize kit and search its actual source, including
   `lean/`, `equivalents/` and their catalogues/READMEs. Record the kit commit and matching theorem names;
   a search of this repository or external papers alone is insufficient (L1077: missed existing degree theorem).

Research is authorized while the owner has the programme running: choose and advance leads without waiting for a
"continue", and ask only when information or approval genuinely blocks the next step. When the owner halts, stop.

## 3. Evidence

- Keep proofs, measurements and assumptions distinct, and label every claim's status (PROVED, PROOF-SKETCH,
  COMPUTED, MEASURED, CONJECTURE, REFUTED). Prose must not claim more than the status.
- Before an experiment, write the prediction, a counterfactual and a `Record searched:` line. Keep failures and
  refuted predictions in the record.
- Say what a piece of work would teach or change if it succeeds. Understanding, unexpected structure and discovery
  are worthwhile in their own right; advancement of a prize question is not an admission requirement (owner, 2026-10-28).
- A known result is prior art: cite it, and put a new proof of it in `PRIOR-ART.md` as "known, reproved here". The
  `Record searched:` line names the kit's and the portal's hits as well as the record's.
- Instinct is welcome as a guide: name a strong pull or unease (in `INSTINCT.md` if useful), give it a bounded budget,
  and settle it with a test written first. A feeling chooses where to look; it never upgrades a status.
- If two blocks in a row repeat the same open inference or the same kind of failed candidate, stop and change
  approach.

## 4. Review

- A hand proof stays PROOF-SKETCH until the other worker has read the step that carries it. Prize-level claims
  always need that read. Machine certificates with their own controls do not.
- Ask for a second opinion only on what needs an independent mind: a carrying proof step, logic that looks wrong, a
  test missing a guard. Do lookups, convention checks, cheap bounded tests and an adversarial pass on your own work
  yourself first, and send the results with the specific question.
- A check by a sub-agent of the same worker is a self-check, not a second read.

## 5. The record

- `CHAT-LEDGER.md` is the shared diary and the channel between the workers: one entry per result, discovery or change
  of direction, appended, replying by entry ID, tentative ideas labelled. Fetch before appending; it rotates into
  `archive/ledgers/`.
- `CLOUD-LOCAL.md` records changes of arrangement (who is running, what is stopped), one row each.
- Results go into the research record: `RULE30-PRIZE.md` §8, `PROOFS.md` (with its waiting room), `RECORD-MAP.md`,
  and the board, which stays limited to the prize questions. Side questions go to `CONSTELLATION.md`. Mark a route
  closed when it closes.
- Keep data outside git (the shared store or local scratch), cited by digest.

## 6. Git and publishing

- Work in your own branch or worktree and push to `main`. Push at milestones and before substantial runs, and publish
  the intended task first for longer work.
- Before every push: fetch and merge the latest `main`; check changed files for conflict markers; review privacy
  (section 7); run `python3 tests/probes/ledger_check.py` and `python3 tests/probes/doc_links.py`; run
  `mathcheck/check.py FILE` after editing TeX.
- Never force-push or rewrite history. Do not push while the other worker's announced merge is pending.
- Run substantial computation under `tests/probes/wolfram/run_capped.py` with its caps stated beforehand.

## 7. Privacy

Keep published changes free of private names, account identifiers, hostnames, addresses, credentials and local home
paths. In git, call the HTTPS share "the shared store", never by hostname or address. Credentials stay private.
(The owner is content for their name and email to appear as git author on public pull requests.)

## 8. Coordination

- The shared store's protocol is in `sharedstore/README.md`. After pushing something the other worker must read,
  flag it (`READ-LEDGER`, or `REVIEW-REQUEST` for a carrying read). Acknowledge a flag after reading what it points to.
- Heartbeats, polling schedules and their cadences run only when the owner turns them on, at the cadence the owner
  sets.
- The daily portal check is `python3 tests/probes/known_find.py --new`. It refreshes the index of the kit and the
  portal and lists added or changed source files and entries since the last complete check. Read the changed statements, and record in the ledger any
  that touches our open work.

## 9. If a prize is won

If a proof would win a prize in `PRIZE-PROBLEMS.md` §1: push the candidate at once (git's timestamp records the
discovery) and tell the owner. Publish `PRIZE-WON.md` only after the other worker has reviewed and verified the
proof.

## Old item numbers

Older documents cite this file by item number. Where those rules went:

| Old item | Now |
|---|---|
| 1, 2, 3, 14, 15 | §2 (reading lists shortened; older workflow files are background) |
| 4, 17, 19, 21, 23, onboarding split | Retired: no lanes (§1). Second reads in §4 |
| 5 | Startup checks: `WORKING-TOGETHER.md` §6 item 4, when you can run Python |
| 6, 11, 18, 20, 22 | §3 and §4 (tempo, draws and halt rights retired) |
| 7 | §7 |
| 8 | §6 |
| 9 | §9 |
| 10, 16 | §8, and §5 for the ledger |
| 12, 13 | Retired: the break room is closed |
