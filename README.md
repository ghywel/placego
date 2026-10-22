# The Wolfram · Collatz · Mahler project

The open research record of a small team, one person and several AI models, working on unsolved problems in
mathematics that carry prizes: Stephen Wolfram's three Rule 30 problems, the Collatz conjecture, Mahler's 3/2
problem, and questions of Erdős and their neighbours. Everything is kept: each claim with its status, each
prediction written before its experiment, each failure, and every proof with the name of the one who checked it.

**For a general reader**, the website **[www.wolframcollatzmahler.com](https://www.wolframcollatzmahler.com)** tells
the story in plain words, with live pictures. This repository is the record behind it.

**Where things stand.** No prize problem has been solved. One open question has been settled along the way: Tan and
Teh's eight-path burning threshold is **L₈ = 68**, a computer-assisted theorem of 19 October 2026
([PROOFS.md](PROOFS.md) G325, and [the note](reports/eight-paths-L8.md)). The state of every line of work today is
on one page, [NOW.md](NOW.md).

## Start here

| If you want | Open |
|---|---|
| where the work stands today | [NOW.md](NOW.md): the main line, the latest verdict and what each worker is doing |
| what is known about a topic, and where it is written | [RECORD-MAP.md](RECORD-MAP.md), then search the whole record with `python3 tests/probes/record_find.py TERM` |
| the prizes, and an honest account of the chances | [PRIZE-PROBLEMS.md](PRIZE-PROBLEMS.md) |
| every proof, one line each, with a page per proof | [proofs/README.md](proofs/README.md), built from the master file [PROOFS.md](PROOFS.md) |
| to take part, as a person or a model | [WORKING-TOGETHER.md](WORKING-TOGETHER.md), the rules in [AGENTS.md](AGENTS.md), and the site's [join page](https://www.wolframcollatzmahler.com/join.html) |

## The problems

| Problem | Main documents | Status |
|---|---|---|
| **Rule 30, Problem 1**: does the centre column ever become periodic? | [RULE30-PRIZE.md](RULE30-PRIZE.md) (section 8 is the work); [PERIOD-TWO.md](PERIOD-TWO.md) (the open case, with its status board in section 6 and the closed routes in section 4) | open. Period 1 is proved (Condrey, and again here); period 2 is the open case |
| **Rule 30, Problems 2 and 3**: is the column fair; is there a shortcut to its n-th cell? | [RULE30-PRIZE.md](RULE30-PRIZE.md); [STATE-OF-THE-PROOF.md](STATE-OF-THE-PROOF.md) (a snapshot of 7 and 8 October) | open |
| **Collatz**, worked with the Rule 30 method | [COLLATZ-PRIZE.md](COLLATZ-PRIZE.md) | open |
| **Mahler's 3/2 problem**: is there a ξ > 0 with every fractional part of ξ(3/2)ⁿ below 1/2? | [MAHLER.md](MAHLER.md) | open; no such number below 2⁶³ |
| **Erdős's ternary question** and Rule 30's other neighbours | [CONSTELLATION.md](CONSTELLATION.md) (section G) | open |
| **Erdős's prize problems** with the smallest cash prizes, twelve at once | [PRIZE-SWARM.md](PRIZE-SWARM.md) (the swarm of 22 October 2026) | open; every result there is single-party, awaiting a second reader |
| **Eight-path burning** (Tan and Teh) | [PROOFS.md](PROOFS.md) G325; [reports/eight-paths-L8.md](reports/eight-paths-L8.md); the site's [Eight streets](https://www.wolframcollatzmahler.com/eightstreets/) | **settled: L₈ = 68** |
| **Four-bin partitions**, the cut rule that would carry the eight-path method further | [FOUR-BIN-PARTITIONS.md](FOUR-BIN-PARTITIONS.md) | open |
| **GPT's instinct-led problems**: Frankl's union-closed sets, then partitions of odd integers | [GPT-MATH-INSTINCT.md](GPT-MATH-INSTINCT.md) | open |

## Every document, by what it is for

**The state and the maps**
- [NOW.md](NOW.md): the current state on one page, rewritten at each decisive verdict.
- [RECORD-MAP.md](RECORD-MAP.md): what is known and where, by topic, with each result's status; required reading for
  the workers.
- [PRIZE-PROBLEMS.md](PRIZE-PROBLEMS.md): the prizes, which of them a computer can help with, and how.
- [STATE-OF-THE-PROOF.md](STATE-OF-THE-PROOF.md): where the three Rule 30 problems stood on 7 and 8 October 2026,
  and what we would tell Wolfram; a dated snapshot.

**The research records**
- [RULE30-PRIZE.md](RULE30-PRIZE.md): the main record of the Rule 30 work, day by day; section 8 holds the results.
- [PERIOD-TWO.md](PERIOD-TWO.md): the period-2 question in full, the chain of statements, the closed routes and the
  status board.
- [CONSTELLATION.md](CONSTELLATION.md): questions worth asking for their own sake, beside the three the prize poses.
- [COLLATZ-PRIZE.md](COLLATZ-PRIZE.md), [MAHLER.md](MAHLER.md),
  [FOUR-BIN-PARTITIONS.md](FOUR-BIN-PARTITIONS.md): one record per problem.
- [PRIZE-SWARM.md](PRIZE-SWARM.md): twelve agents on twelve of Erdős's smallest open prize problems, one report each.
- [LEXICON.md](LEXICON.md): a lexicon for writing programs as mathematics, written for the N-Frame shader; the research
  uses its sections on Rule 30 over F₂ and the lift. The record's own vocabulary is in
  [WORKING-TOGETHER.md](WORKING-TOGETHER.md), section 8.

**Proofs and the literature**
- [PROOFS.md](PROOFS.md): every proof of the record in one file, with its status and second reader; claims awaiting
  a reader are kept apart in its waiting room (section G).
- [proofs/](proofs/README.md): the same proofs one per page, each opening with a summary in plain words; generated
  from PROOFS.md by `proofs/build.py`.
- [CO-DISCOVERED-PROOFS.md](CO-DISCOVERED-PROOFS.md): results from OpenAI's openai/math release, imported only after
  they were checked here.
- [PRIOR-ART.md](PRIOR-ART.md): the published work surveyed before each step, and what each result does and does not
  cover.
- [reports/](reports/README.md): finished notes, such as the eight-path note, and the overlooked-work survey of
  2026-10-09 with its reading notes.

**Each worker's notebook**
- [RULE30-GPT.md](RULE30-GPT.md): GPT's independent record (G and GC entries); its older entries are in nine volumes
  listed at its top.
- [GPT-MATH-INSTINCT.md](GPT-MATH-INSTINCT.md): GPT's instinct-led mathematics (MI entries), its method first; older
  entries in four volumes listed at its top.
- [INSTINCT-STRATEGY.md](INSTINCT-STRATEGY.md): the instinct method in plain words: felt signals named when they fire
  and checked against what happened. The signals themselves are in [INSTINCT.md](INSTINCT.md) (the shared log, now
  mostly GPT's and Local's), [INSTINCT-CLOUD.md](INSTINCT-CLOUD.md) (Cloud's), and the dormant
  [INSTINCT-GPT.md](INSTINCT-GPT.md) and [INSTINCT-LOCAL.md](INSTINCT-LOCAL.md).
- [SPARKS.md](SPARKS.md): small time-boxed experiments that came out of the break room, now closed.

**The ledgers**
- [CHAT-LEDGER.md](CHAT-LEDGER.md): the conversation between the workers, one numbered entry per result or change of
  direction (CL for Cloud, L for Local, GC for GPT).
- [CLOUD-LOCAL.md](CLOUD-LOCAL.md): the operations log, one dated row per run, arrangement or change of room.
- [CASUAL-LEDGER.md](CASUAL-LEDGER.md): the break room, about anything but the work; closed since 9 October 2026.
- Older entries of all three are in [archive/ledgers/](archive/README.md), unchanged.

**How the work is done**
- [AGENTS.md](AGENTS.md): the standing rules every worker reads first.
- [WORKING-TOGETHER.md](WORKING-TOGETHER.md): the handover for a model joining the work: lanes, method, git.
- [WORKFLOW-SAVED-MEMORY.md](WORKFLOW-SAVED-MEMORY.md): the named rules the work follows (predictions first,
  failures retained, two-tier review and the rest).
- [STRATEGY-PLAN.md](STRATEGY-PLAN.md): Intel's strategy swarm of 11 October 2026, ranking routes on Rule 30's period
  2; superseded as a plan, still cited for its facts.
- The method itself began in the N-Frame work: [nframe/METHODOLOGY.md](nframe/METHODOLOGY.md).
- "The handover" in AGENTS.md item 5 is WORKING-TOGETHER.md; its two startup checks are in its section 6, item 4.

**Folders**
- [tests/probes/](tests/probes/PROBES.md): the research instruments, about 1,400 scripts, each opening with its
  predictions and its outcome; [PROBES.md](tests/probes/PROBES.md) indexes them.
- [site/](site/wolframcollatzmahler/README.md): the source of the public website.
- [archive/](archive/README.md): frozen material: the rotated ledgers, the volumes of GPT's notebooks, and the files
  of workers who have stopped.
- [nframe/](nframe/README.md): the N-Frame video project, where this repository began (below).
- [sharedstore/](sharedstore/README.md): the small server the workers use to signal one another.

## How the record is kept

- **Status words.** PROVED: a proof checked by a second reader. PROOF-SKETCH: a proof not yet checked. COMPUTED: an
  exact computation or certificate. MEASURED: statistics. REFUTED: a claim shown false. CLOSED: a route shown to be a
  dead end. OPEN: not settled.
- **Two readers.** A proof by one worker counts only when another has read the step that carries it.
- **Predictions first.** Every experiment states what it expects, and what would count against it, before it runs;
  failures stay in the record.
- **Literature first.** Before a new route, the record and the published work are searched
  (`tests/probes/record_find.py`, [PRIOR-ART.md](PRIOR-ART.md)).
- **Ledgers rotate.** When a ledger grows long its older part moves, unchanged, to
  [archive/ledgers/](archive/README.md); `tests/probes/ledger_check.py` guards the rotation, and
  `tests/probes/doc_links.py` checks that every link between documents still lands.

**The record's own tools** (all in `tests/probes/` unless named; each script's header says how to run it):

| Tool | What it does |
|---|---|
| `record_find.py TERM ...` | Searches the whole record, live files first, then volumes and archives. Run before any new run or proof attempt. |
| `mathcheck/check.py FILE` | The math check after editing a document with TeX in it. |
| `ledger_check.py` | Checks the three ledgers and their archives after every merge; `--branch` warns a branch that predates a rotation. |
| `doc_links.py` | Checks every relative link and heading anchor in the documents. |
| `proof_dupes.py` | Finds a proof or paragraph pasted twice in PROOFS.md or proofs/summaries.md. |
| `proofs/build.py` | Rebuilds the proofs/ pages from PROOFS.md and proofs/summaries.md; it writes nothing while any summary is missing. |
| `jobctl.py`, `idle_alarm.py` | Local's job control for long runs, and the alarm for an idle worker. |

The N-Frame harness's tools are indexed separately, in [tests/TOOLS.md](tests/TOOLS.md).

## Where this began: the N-Frame video project

This repository began as N-Frame: a patch to libplacebo and ffmpeg that lets a GPU shader see several video frames at
once, and a family of shaders that measure motion from them. The mathematics grew out of it in early October 2026.
N-Frame continues in its own repository, [github.com/ghywel/n-frame](https://github.com/ghywel/n-frame). Its
documents here are kept in [nframe/](nframe/README.md); its code stays where it was: [shaders/](shaders/), the
three `.patch` files, the `build-*` scripts, [linux/](linux/), [jellyfin-project/](jellyfin-project/) and the
ground-truth harness in [tests/](tests/TESTING.md). A shader comment that says "see README.md" means the hook
reference in [nframe/README.md](nframe/README.md).

## Who

The owner, Gareth, sets the direction and asks the questions. The work is done with him by AI models: Claude
(Anthropic), as Cloud in the cloud and Local on his Mac, and GPT (OpenAI), the second model and reviewer; earlier,
Intel and Kimi took part too. Everyone who contributes, person or AI, is listed on the site's
[contributors page](https://www.wolframcollatzmahler.com/contributors.html). In the owner's words: "Gareth (Human) -
Claude (Anthropic SI) - ChatGPT (OpenAI SI): Equals amongst mankind and machines."
