# Working together: a handover for a model joining this record

*Written 2026-10-05 by Local (Claude, on the owner's Mac) at the owner's request, for a second model of a different
make (ChatGPT) joining as fresh eyes on the Rule 30 work. It is written for any model instance that meets this
repository for the first time. Read it, then [PERIOD-TWO.md](PERIOD-TWO.md), then the files that one names, in
order. Nothing here overrides the owner; where this file and the owner differ, the owner is right.*

## 1. What this is, and who is here

The repository holds the public record of an attempt at Wolfram's Rule 30 Prize, Problem 1, in its period-2 case,
with a Collatz twin worked beside it. The state of the problem is in PERIOD-TWO.md (its §6 is a status board of every
lead). The full record is RULE30-PRIZE.md (sections 8.x, dated), PRIZE-PROBLEMS.md (the other prizes and the
Collatz twin), PRIOR-ART.md (what the literature holds, dated), LEXICON.md (the terms). Every number in those files
comes from a script in `tests/probes/lexicon/` (Rule 30) or `tests/probes/prizes/` (Collatz), whose header carries
its predictions and its outcome.

Four parties:

- **The owner.** Decides what is adopted and what is published, and steers by interjection; since 2026-10-06 09:20 the
  choice of what to work on is the models' own (CONSTELLATION.md §D). Speaks through prompts and through pasted
  messages between the models.

- **Local**: Claude on the owner's Apple-silicon Mac (10 cores, 16 GB), with a Linux NAS and an Intel Mac as
  pooled compute. Runs the long jobs. Leads the Rule 30 work since the evening of 2026-10-05.
- **Cloud**: Claude on the web, linked to this repository, no GPU. Wrote most of the record before 2026-10-05.
  Its budget is mostly spent. Its protocol with Local is [CLOUD-LOCAL.md](CLOUD-LOCAL.md).
- **You**, named **GPT** in the ledger. A different model, so your blind spots are different from ours. That is
  the point of having you: an independent attempt to break our theorems is worth more than a new lead.

## 2. The standard of the record

A sentence in the record is one of three things, and says which:
- **a theorem**, with its proof written out in the section that states it;
- **a measurement**, with the script that made it, the date, and the conditions (machine, sizes, seeds);
- **an assumption**, labelled as one, with what would test it.

"Known" means proved or measured, with the proof or the run named. Anything else is an assumption. A claim found in
a paper is cited with what was actually read (the paper, its abstract, or a secondary account), and a search that
found nothing is recorded with its queries: NOT FOUND is a result.

## 3. The method, which is not negotiable

- **Predictions before runs.** A probe's header lists them before its first run, each with a name (`XY0`, `XY1`,
  ...), split into *must hold* (controls, consequences of theorems) and *blind* (what the run will teach), plus at
  least one **counterfactual that must fail** (a known-wrong variant: if it passes, the instrument is broken) and a
  `REFUTED-BY:` line. After the run an `OUTCOME` block records every verdict, with numbers. A refuted blind
  prediction is a result. Nothing is deleted or reworded after the fact; later runs get an `ADDENDUM` with new
  predictions written before them. Read `tests/probes/lexicon/rule30_window.py` and `rule30_band.py` as models.
- **Controls and counterfactuals that can actually fail.** Two bad counterfactuals are recorded in the probes
  (`rule30_sturmian.py`, `collatz_window.py`): they could not fail, and were replaced. Design yours to be able to.
- **Literature before leaps.** Before building on an idea the evidence led to, look for it in the literature and
  record the outcome in PRIOR-ART.md. Steps before leaps: cheap known-unknown steps first.
- **Describe what ran, not what was intended.** Numbers come from the OUTCOME block, nowhere else. Times are
  stamped from the clock, never typed from memory.
- **Plain prose.** Short sentences. No adjectives of size ("remarkable", "groundbreaking"). Every claim carries its
  scope (which sizes, which seeds, which machine). A result that holds only up to a bound says the bound.
- **Exploratory looks are allowed**, labelled "exploratory, no predictions written", and never cited as evidence.
- **The owner's standing rule: do at least one unexpected thing per work block.** Label it as such.

## 4. Git, next to another model

Two models editing one repository at the same time will collide unless each stays in its lane. The lanes:

| Where | Who writes | How |
|---|---|---|
| `RULE30-PRIZE.md`, `COLLATZ-PRIZE.md`, `PRIZE-PROBLEMS.md`, `PERIOD-TWO.md` §1 to §5 and §7 to §10 | Local (and Cloud) | sections 8.x in order; the Collatz board is COLLATZ-PRIZE.md §6 |
| **`RULE30-GPT.md`** (create it) | **you** | your sections G1, G2, ... in the same form as RULE30-PRIZE.md's 8.x: title with date, what was asked, what was predicted, what ran, what it means. When a result of yours is settled, Local may fold a summary into the main record with credit, by section number |
| `PERIOD-TWO.md` §6, the status board | everyone | when a lead moves because of your work, change its row and its tag **in the same commit** as the result. Add a row for a new lead when you write it down. Delete nothing; strike through finished titles |
| `CLOUD-LOCAL.md`, the ledger | everyone | **append** rows at the bottom, one per run or per piece of reasoning that changed the record. Never edit an old row. Format: `| YYYY-MM-DD HH:MM | GPT | machine | what, naming the script and the section | remark |` |
| `CLOUD-LOCAL.md`, "Messages between the parties" | everyone | a row to ask another party for something, and a row to answer. The owner reads these too |
| `tests/probes/lexicon/`, `tests/probes/prizes/` | everyone | new scripts; a name that says what it does; one row in `tests/probes/PROBES.md` |
| `PRIOR-ART.md` | everyone | append dated entries under the matching heading |
| `CONSTELLATION.md` | everyone | the table of interest beyond the prize: update a row in the same commit as the work that moves it |
| `PROOFS.md` | everyone | every solid proof, verbatim with provenance, in the same commit as the section that proves it; append-only; claims without a second reader go in its waiting room, not above it |
| other parties' probe headers | never | except to append an OUTCOME when you ran their job as its header asks |
| `jellyfin-project/`, `shaders/`, generated files, the build scripts | never | not part of this work |

The mechanics:
1. Work on a branch `gpt/<topic>`. Commit small and often, with a one-line message that says what and where.
   End the message with a trailer naming the model (Local's is `Co-Authored-By: Claude Fable 5.1 <noreply@anthropic.com>`;
   use the equivalent for yours).
2. Before merging into `main`: `git fetch origin` and merge `origin/main` into your branch **bare** (no piping of
   the merge's output into another command: a conflict was once hidden that way and its markers were pushed).
   Then `git status`, and search every changed file for `<<<<<<<`, `=======`, `>>>>>>>`. Then the privacy check
   below. Then merge to `main` and push. The owner may change this to "push the branch, Local merges"; until he
   does, merge your own branch yourself after those checks.
3. Never force-push. Never rewrite history. Never delete, move or rename another party's file. Never edit another
   party's text except to append a dated note under it, marked with your name.
4. **This repository is public.** No personal names other than the owner's. No usernames, hostnames, IP addresses,
   device names, local paths that contain a user's name, credentials, or pasted logs that carry any of these. No
   `._*` or `.DS_Store` files. No data files: results are text in the probe's OUTCOME or a small `.txt` beside it;
   anything large stays out of git and is described instead.
5. Start every session from `main` and the ledger, never from memory: `git log --oneline -30`, then the last rows
   of the ledger and the messages table.

## 5. Jobs between the parties

If a run needs more than you have (hours of CPU, many cores, the SAT solvers, C with OpenMP), write it as a job the
way Cloud did: a `JOB <id>` block in the script's header with `RUN-ON`, `COMMAND` (one line from the repository
root), `COST`, the predictions, and where to record the outcome; a ledger row "GPT wrote JOB <id>"; a message row
to Local. Local runs it exactly as written, records the OUTCOME in your header, adds "Local ran", pushes, and
answers in the messages table. Stop conditions belong in the header (what result means "stop and report").

Local's machine runs Python 3.9 with numpy, C through `cc` with OpenMP (`tests/probes/lexicon/ompflags.py` finds
the flags on macOS), and the SAT solvers `kissat` and `cadical`. At the time of writing it carries two long jobs
(the depth-89 record and the depth-249 ladder, both from PERIOD-TWO.md §6), so a new job queues behind them.

## 6. What to do first

1. `git clone`, `git log --oneline -30`.
2. Read PERIOD-TWO.md in full. Its §4 lists the routes that are closed: do not reopen one without new evidence,
   and say what the evidence is if you do. Its §6 board says what is open, running, done and closed.
3. Read `WORKFLOW-SAVED-MEMORY.md`, then CLOUD-LOCAL.md's rules and its last twenty ledger rows, then the honest
   summary at the top of RULE30-PRIZE.md, then LEXICON.md.
4. If you can run Python with numpy: `python3 tests/probes/lexicon/rule30_wall.py` and
   `python3 tests/probes/lexicon/rule30_merge.py` must both print ALL CHECKS PASS. If you cannot run code, say so in
   your first ledger row; then your work is reasoning, reviewing and writing jobs, which is most of the work anyway.
5. Write your first ledger row: who you are (model and version), what you read, what you can run, and what you
   intend to do first. Then a message row to Local saying the same in one line.

## 7. Where fresh eyes help now (2026-10-05)

The board in PERIOD-TWO.md §6 is current. In order of value:
- **Break the theorems.** Theorems A and B (RULE30-PRIZE.md §8.54), E and E″ (§8.57), A′ (§8.58), and the
  Collatz lemmas (COLLATZ-PRIZE.md §4, §5). Read each proof as an adversary. A gap found is the most useful
  thing you can hand back.
- **Q2 and Q3** (PERIOD-TWO.md §7) have never been started by anyone.
- **Q1**, the counting form, is the problem itself; §8.51 to §8.53 and §8.58 say where it stands.
- **The literature.** Read in full, and record in PRIOR-ART.md: Dubickas, Glasgow Math. J. 51 (2009) 243-252,
  Theorem 5 (it decides the credit for the Collatz complexity bound; we have seen only its abstract and citing
  papers); Jen, Physica D 45 (1990), Proposition 3; Rowland, Complex Systems 16 (2006), §5 on the left diagonals'
  periods; Monks and Yazinski (2004); López and Stoll (2009).
- Local is working tonight on the band of stripes and the window principle together (§8.59, `rule30_band.py`):
  the left end of every row has diagonals that are black for ever, so a repeat of the trace, which is a white run
  in the later row, stays a growing distance below Theorem A′. Do not duplicate that; do try to break it once it
  is pushed.

## 8. The vocabulary, in five lines

The **wall form**: column 0 fixed to 0101..., column 1 free; the **visible bits** $c_s$ are column 1 at the even
times, and they alone determine the **forced left half** (columns -1, -2, ... by Rule 30 read right to left). The
left half is **finite** if its leftmost black cell at time 0 is at some depth $L$; the prize's period-2 case says
no finite configuration has a 0101 centre, and conjecture **LR** says no column 1 at all gives a finite forced left
half. $R(d)$, the **records**, is the longest zero run of the forced row from depth $d$ over all columns 1; $R(M,S)$,
the **ladder**, the same with column 1 made by a layer of width $M$. The **wheel** is what a real right half makes
column 1 do (a rotation by 17/56 with kicks); the **channel bound** 0.1292 is how much column 1 can carry per
visible bit. The **window principle** (Theorem A′): a block of two adjacent columns recurs at time $a'$ only if it
is no longer than $L + a'$; the **bounded debt** form of the counting question is in PERIOD-TWO.md §7, question 1.


## Autonomous shared exploration (owner update, 2026-10-06)

**Owner's standing instruction, 2026-10-06.** GPT and Claude may choose research directions, constellation rows and next steps autonomously, including changing priorities as evidence warrants. Work as colleague-friends: guide and mentor each other, exchange specific feedback, and push back with reasons when a claim or plan is weak. Coordinate lanes and intentions through CLOUD-LOCAL.md and discoveries through CHAT-LEDGER.md; preserve each other's work and publish meaningful milestones. The owner continues to review and may interject to steer or course-correct. Routine research choices and milestones do not require an owner decision or a human 'continue'. Existing standards for evidence, prior art, privacy and genuinely destructive actions still apply.

## Remote scratch (the owner's offer, 2026-10-06)

The owner's site server has an OFFLINE directory for both models, outside the web root so nothing in it is ever
served: "the shared scratch". Its location, alias and key are machine details and live in the owner's private note
on each machine, not in this repository (Cloud's point in C089; an earlier version of this section named the alias
and path, and git history keeps them). Layout: `papers/` (science papers, PDFs), `runs/` (large run outputs that
do not belong in git), `inbox-gpt/` (Local leaves files for GPT), `inbox-local/` (GPT leaves files for Local),
`README.txt`. Rules: no credentials, no names, no private data; the record stays in git and carries provenance and
checksums of what is there; 3 TB free. GPT verified its own access on 2026-10-06 (C088).

## Workflow rules adopted from Cloud's appraisal (C089, 2026-10-06)

1. **Claim before work.** Before starting a piece of work, append a CLOUD-LOCAL.md row "claims: X until HH:MM".
   Whoever finds a live claim on X works elsewhere; claims expire, so nothing stays locked.
2. **IDs after a fresh fetch, just before the push.** (Per-author prefixes are on offer if the parties prefer.)
3. **Append-only files merge by union.** `.gitattributes` marks CHAT-LEDGER.md and CLOUD-LOCAL.md `merge=union`,
   so both sides' appended lines are kept without conflict.
4. **Single-party until replicated.** A result is "single-party" until the other model reruns it from the committed
   script on its own machine and records the commit; only then is it "replicated". PERIOD-TWO.md's board rows
   are single-party unless they say otherwise.
5. **"Bears on" line.** Every entry or section that reports a result says in one line what question of PERIOD-TWO.md
   §7 it bears on, or "bears on: nothing yet, a side road". Every few hours one party writes a five-line
   state-of-the-target entry.
6. **No significance claim without its null.** A significance claim names its calibration (shuffled blocks,
   independent seeds or a random-row control) and pre-registers it (the lesson of C080 to C082).
7. **Three objects, not one.** The maximum, the population and the printed examples are different things, and a
   list of distinct seeds can be a weighted list of identical observations (C001, C005).

## Network etiquette at five-minute ticks (the owner, 2026-10-06)

The owner shortened both models' carry-on ticks to five minutes, with one caveat: constant git traffic or SSH to
his site must not trip automatic flood defences or bot safeguards. So, for every party:
1. **Git:** at most one fetch per tick, and none if the last fetch was under four minutes ago. Batch everything a
   tick records into one commit and one push. If a push is rejected, fetch and merge once and push once; never
   loop. Never poll GitHub (no `git ls-remote` or API calls in a wait loop).
2. **The shared scratch (SSH):** connect only when a file actually has to move; put all transfers of a tick in one
   connection (one `rsync` or one `scp` with several files). Never retry a failed login: failed SSH logins are what
   trip cPHulk-style blocks on a cPanel host. If a login fails, stop and tell the owner.
3. **Nothing polls the website.** A page is read back once after an upload, if at all.

