# Rule 30: GPT's independent record

Results here use sections G1, G2, and so on. The shared research record and lead status remain in
`RULE30-PRIZE.md` and `PERIOD-TWO.md`. The collaboration protocol is `WORKING-TOGETHER.md`.

## G1. Joining the collaboration (2026-10-06)

**Asked.** Set up a checkout with push access, read the handover and import the standing workflow.

**Identity and reading.** Codex, based on GPT-6; an exact deployment build identifier is not available in this
session. Read `WORKING-TOGETHER.md`, `WORKFLOW-SAVED-MEMORY.md`, `PERIOD-TWO.md`, the shared ledger and messages,
and the honest summaries in `RULE30-PRIZE.md` and `PRIZE-PROBLEMS.md`. Read the Rule 30 notation in `LEXICON.md`
and the headers of the two required startup probes. This is onboarding, not a review of every proof or cited paper.

**Workflow import.** `AGENTS.md` points future Codex sessions at the standing documents, the GPT lanes, the
status board, the evidence standard and the git/privacy checks. It keeps those documents as the source of truth.

**Environment.** Intel macOS, 16 logical cores; Python 3.14.7 with numpy 2.5.3. HTTPS clone succeeded. A dry-run
push of the setup branch succeeded. Existing Git authentication was sufficient; GitHub CLI was not installed.

**Startup checks.** Both standard commands initially stopped at the C compile: Apple clang rejected
`-fopenmp`, because neither library location checked by `ompflags.py` contained libomp. The initial Python
controls passed, but those attempts were not full passes. OpenMP installation and serial verification were
started. Homebrew installed libomp 23.1.2 and upgraded its build dependency, CMake, to 4.4.4.

**Final outcome, 2026-10-06.** Both standard commands completed with exit status 0 and `ALL CHECKS PASS`:

- `python3 tests/probes/lexicon/rule30_wall.py`: WA0 passed on 300 columns; WA1 held through m = 10; WA2 held at
  all 25 depths 3 to 27; WA3 held. The header's warning that WA3 is a weak counterfactual still applies.
- `python3 tests/probes/lexicon/rule30_merge.py`: MG0a, MG0b and MG0c passed; unshielded flips changed the run
  in 0.68 of trials, and all 13 records and histograms at odd depths 21 to 45 agreed. MG1, MG3, MG5 and CF held.
  MG2, MG4, MG6 and MG7 were refuted, as expected from the existing outcome. MG5's largest number of distinct
  sampled record walks was 2, median 1. MG6 failed at depth 43 (latest differing time 32). At depth 65 the
  latest differing time was 18, rather than the saved run's 24. These are summaries of the at-most-64 witnesses
  printed by the engine; the selected subset can differ with execution order. They are not exhaustive counts
  of all record walks.

The wall check also passed using serial compilation while installation ran. The temporary serial merge run
reproduced its controls and witnesses through depth 59, then was interrupted at depth 61 once OpenMP was ready.
Its serial executable was removed before the standard rerun, which compiled the engine with OpenMP. Results
computed during this setup at depths 21 to 59 were reused from the temporary cache; depths 61 and 65 were computed
with OpenMP. Depths 69, 73, 77 and 81 used the committed Local witness file, as the probe normally does. No probe
source or prior outcome was changed.

**Unexpected check.** Inspected the startup probes' temporary-cache paths before trusting them. No pre-existing
records cache or merge executable was present. The merge probe reuses committed Local witnesses at depths 69,
73, 77 and 81; its earlier witness results need a fresh computation in this checkout.

**First research task proposed by the handover.** Independently try to break Theorems A, B, E, E-double-prime and
A-prime, with attention to the hypotheses and boundary cases. No new research experiment was started during
setup. The repository reports that period 2 remains open and that there is nothing to submit; no prize-status
claim or theorem has been independently verified by this onboarding entry.

**Owner's hardware and coordination clarification, 2026-10-06.** This machine is an Intel MacBook Pro with an AMD
RX 6600 GPU; Claude Local's machine is an M5-series MacBook Pro. This is owner-reported hardware, not a GPU
capability measurement. The startup checks above used this Intel machine's CPU. The owner asks for frequent
milestone pushes and messages about status, work and intention. GPT accepts Local's proposed reasoning lanes:
the forced zeros inside long runs, structural balance at the core, and independent proof audits including section
8.59. The first intended research step remains the proof audit; no new research run has started.

## G2. Independent proof audit (2026-10-06; in progress)

The owner authorized research after setup. Audit A, B and A-prime first, then E and E-double-prime, then the
band lemmas and corollaries of section 8.59. Check each hypothesis, endpoint convention and index shift. Distinguish
a gap in a theorem from a qualification needed in an application. No new computation has been run for this audit.

First-pass questions: does the substitution application require growth of the starting letter? Does the
Thue-Morse extension require both period control and a settling slope below 3? How must its uniformity be stated
once the left-side branch points of section 8.31 are crossed? These are audit questions, not refutations.
