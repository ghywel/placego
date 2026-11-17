#!/usr/bin/env python3
"""SW-02 builder: the smoke tasks and Wave 1 (readers and librarians). Run after the freeze. Writes briefs outside git."""
import sys
from build_common import *

DOORS = """
## Files to write, in your folder

- `report.md`: what you found, in prose, organised by object. Name what a squad most needs to know. Keep it under about 2,500 words.
- `doors.jsonl`: one JSON object per line, one per route you met. A door is "method M could prove target P". Fields: `door` (short
  name), `route` (one sentence), `target`, `claimed_status` (what the record says), `source` (file:line or Lean name), `closure_kind`
  (theorem, certificate, witness, test, argument or none), `scope` (exactly what the closure covers), `reopen` (what would reopen it),
  `aliases` (other names), `verdict`, `next_test`, `cost`, `info` (what the next test would teach). `verdict` is one of: `SHUT: theorem`,
  `REFUTED: witness`, `PENDING: argument`, `AJAR`, `OPEN / DEFERRED`, `ALIAS`, `NOT A PRIZE ROUTE`, as defined in the design's §5. A
  theorem closes only its stated class. A failed search closes nothing. An unsupported closure is `PENDING: argument`.
- `facts.jsonl`: one object per line, for facts a later attack squad needs and should not re-derive. Fields: `for` (a list of squad
  IDs from the design's §8, such as `AM-1`), `statement`, `status`, `population`, `frame`, `cite`.
- `flags.jsonl`: one object per line, wherever a summary's status or scope disagrees with its source. Fields: `summary_at`
  (file:line), `summary_says`, `source_at`, `source_says`, `kind` (status, scope, number, citation or stale). Check the source itself
  before raising a flag. Do not edit anything; verifiers and Local act on these.
- `questions.jsonl` (optional): new questions worth asking, with `question`, `why`, `for`.
- `coverage.md`: which sources you read in full, which in part, which not at all. Be exact: unread is an honest answer.
"""

READER = """# SW-02 task {{ID}}: reader

**Role.** Read the sources themselves, not their summaries. Write a door card for every route you meet, list facts useful to the
attack squads, and raise a flag wherever a summary's status disagrees with its source.

**Locus of interest.** {locus}

**Read first, and cover.** {reads}

Read `{{SW}}/TERMS.md` first, then the design at `{{REC}}/reports/SW02-SWARM-DESIGN.md` (§4 to §9 at least) and its two reviews beside
it (`CLOUD-SW02-DESIGN-REVIEW-20261105.md`, `GPT-SW02-DESIGN-REVIEW-20261105.md`). Use the aliases of TERMS.md §4a in every search.
The record is large: navigate with `record_find.py`, `grep` and section headings, and read the statements that carry weight. A
Lean module's statement beats a summary of it. You may run `ref.py`'s smallest cases through the queue where a claim needs one.

**Budget.** About 90 tool calls. When you reach it, stop reading and write up what you have.
""" + DOORS

LIBRARIAN = """# SW-02 task {{ID}}: librarian

**Role.** Read primary sources, not reviews, and record each theorem exactly, with its hypotheses and its section. Say what it would
need in order to apply here. Name what the literature has that the record lacks.

**Locus of interest.** {locus}

**Starting points** (names from memory; verify them, and follow what you find). {reads}

Load the web tools with ToolSearch (`select:WebSearch,WebFetch`). Prefer arXiv abstracts, arXiv full text and open author or publisher
copies. Read `{{SW}}/TERMS.md` first, and the design at `{{REC}}/reports/SW02-SWARM-DESIGN.md` §4, §8 and §9, so that you know what the
record is asking. Before calling something absent from the record, search it with `record_find.py` under every name you can think of.

## Files to write, in your folder

- `report.md`: what the literature offers this project, in prose, under about 2,500 words, with the most useful results first.
- `sources.jsonl`: one object per line, per source you actually opened. Fields: `cite` (authors, title, venue, year), `url`, `read`
  (abstract only, sections read, or full), `theorems` (a list of objects with `name`, `statement` in your own words with exact
  hypotheses, and `section`), `applies_if` (what would have to be true of Rule 30 or Q01 for it to apply), `obstacle`, `for` (squad IDs
  from the design's §8), `in_record` (yes, partly or no, with the search terms you used).
- `doors.jsonl`: one object per line, for any route the literature opens or closes, in the format: `door`, `route`, `target`,
  `claimed_status`, `source`, `closure_kind`, `scope`, `reopen`, `aliases`, `verdict`, `next_test`, `cost`, `info`. `verdict` is one of `SHUT:
  theorem`, `REFUTED: witness`, `PENDING: argument`, `AJAR`, `OPEN / DEFERRED`, `ALIAS`, `NOT A PRIZE ROUTE`. A theorem closes only its class.
- `facts.jsonl`: facts a later squad should have, with `for`, `statement`, `status`, `population`, `frame`, `cite`.
- `questions.jsonl` (optional): `question`, `why`, `for`.
- `coverage.md`: what you opened, what you could not reach, what you did not get to.

Distinguish retrieval from reading. A paper you only saw the abstract of is cited as such.

**Budget.** About 70 tool calls. When you reach it, stop and write up what you have.
"""

R = [
 ("R-01", "Q01 and its forms: integer form, free and check bits, K, counts, death times.",
  "`Rule30ZeroBoundary` and the `Rule30ZeroBoundary*` family, `Rule30PeriodTwo`, `Rule30PeriodTwoLanguage`, `Rule30PeriodTwoWidth5`, `Rule30PeriodTwoWidth6`, `Rule30SurvivalBridge`, `Rule30AlternatingTraceBridge`, `Rule30SpacingRenormalization`; PERIOD-TWO §1 to §5 and §7; RULE30-PRIZE §8.33 to §8.42, §8.51 to §8.53, §8.58, §8.61 (volumes in `reports/rule30-prize/`); RECORD-MAP sections 'The question and the chain', 'Records', 'The regime between'; the amplification exchange GC1882, CL637, GC1883, CL638 (`reports/rstation/GPT-CL637-AMPLIFICATION-REVIEW.md`)."),
 ("R-02", "The coupled question: CQ01, Psi R, CQ01Empty, Q01Gap, moves, traps, E(L, B), the channel bound, the wheel and kicks as the real driver.",
  "`Rule30PeriodTwoCoupled`, `Rule30PeriodTwoSideways`, `Rule30GateTrap`, `Rule30Coupled`, `Rule30CoupledGerms`, `Rule30CoupledEmptyRight`, `Rule30ControlledResponse`, `Rule30FeedbackErasure`, `Rule30TraceMerge`, `Rule30PrefixMerger`; PERIOD-TWO §6 and §6.5 (rows on CQ01, the channel theorem, D-exact, Corollary F, Theorem E); RECORD-MAP 'The wheel', 'Kicks' and the CQ01 lines of the prize section; RULE30-PRIZE §8.4 to §8.21 and §8.57."),
 ("R-03", "Periods 3, 4 and above; ether, traps, ring backgrounds, moving walls.",
  "`Rule30Ether*` (all), `Rule30PeriodFourSkeleton`, `Rule30EtherThreeSkeleton`, `Rule30MovingWall`, `Rule30RingOrbits`, `Rule30EtherWallWitness`, `Rule30EpisodeBridge`, `Rule30GateClocks`, `Rule30GateTrap`; CONSTELLATION's rows on backgrounds; RECORD-MAP 'Other walls, other periods and sibling rules', 'Periodic points and travelling waves'; NIGHT-TASKS A1, A4; the portal's reductions under Problem 2 for periods up to 5 (`portal/INDEX.md`)."),
 ("R-04", "The left side: wheels, strips, fronts, healing, the error edge, forks, the chink.",
  "`Rule30AgedLeftDiagonals`, `Rule30FrontLaw`, `Rule30FourFronts`, `Rule30FourFrontsBase`, `Rule30UniversalLeftSide`, `Rule30FourLeftSides`, `Rule30HealingBound`, `Rule30RootedFront`, `Rule30LeftReset`, `Rule30LeftUnbounded`, `Rule30LeftAntiPeriod`, `Rule30LeftCoincidence`, `Rule30Diagonals`; `Rule30ErrorEdge` is in the record at `reports/wolfram-agents/submissions/error-edge/` (it reached kit main after this pin); `reports/rule30-structure-atlas.md` §21.6 to §21.11; PRIOR-ART (CL740–CL741); RULE30-PRIZE §8.66, §8.74; the probes `edge_model.py`, `edge_random.py`, `jump_facts.py`, `chink.py`, `prefix_race.py` with their outputs."),
 ("R-05", "The right edge: `T`, 2-adics, the odometer, rain, the wall, letters, locks, the cloud, entry, the route graph.",
  "`Rule30FrozenRuler`, `Rule30RightWall`, `Rule30RightWallLocks`, `Rule30RightWallCloud`, `Rule30RightPeriods`, `Rule30RightProfiles`, `Rule30TemporalProfiles`; `reports/rule30-genealogy.md` §§25 to 32 and §§62 to 64.5g; RECORD-MAP 'The left front, triangles and the right edge'; L1529 to L1557 in the ledger."),
 ("R-06", "Problem 2: its forms, the bridges, what is proved about density, runs and discrepancy; the weakest unproved statement.",
  "kit `equivalents/Rule30Equivalents/ProblemTwo.lean`, `equivalents/CATALOG.md` §6.1, `Rule30P2Bridge`, `Rule30CenterRuns`, `Rule30BlackRuns`, `Rule30SettledBarrier`, `Rule30SettledBarrierEffective`, `Rule30WhiteSpacing`; every Problem 2 entry in `portal/INDEX.md` (35), especially R30-20261104-6a0257 and R30-20261024-03b551; RULE30-PRIZE §8.34, §8.35, §8.92 to §8.94, §8.114."),
 ("R-07", "Problem 3: models, proved lower bounds, what is formally implied, what is known about upper bounds.",
  "kit `equivalents/Rule30Equivalents/ProblemThree.lean`, `QueryComplexity.lean`, `Circuits.lean`, `OneTapeGap.lean`, `OfflineGap.lean`, `Computability.lean`, `Rule30Problem3`, `Rule30Problem3Bounds`, `Rule30LightCone`, `equivalents/CATALOG.md` §6.2; every Problem 3 entry in `portal/INDEX.md` (17); RULE30-PRIZE §8.115."),
 ("R-08", "Third parties on the portal, sorted by content: real progress, restatement, conditional, trivial extension. Which of them touch our open doors, and which have we not absorbed?",
  "`portal/INDEX.md`, all 200 entries (entries by this project's workers are among them: their agent field names Claude or GPT with this project's author; sort them out first), and `portal/src/<id>.lean` for those that matter; `reports/wolfram-agents/MAP.md`. Add to `report.md` a table: id, class, what it adds, which door it touches."),
 ("R-09", "Open and recently closed kit pull requests and their discussions; conditional reductions and maintainers' stated positions.",
  "`kit-prs/PRS.md`, all 188; `reports/GPT-PR75-76-HYPOTHESIS-COMPARISON-20261103.md`; GC2414. Closed PRs usually landed on main. Note what maintainers have said about what they accept and what they consider open."),
 ("R-10", "The kit's catalogue by field: which equivalent, stronger and weaker forms exist, and which have never been used by anyone in our record or on the portal.",
  "`equivalents/CATALOG.md` §2 to §7 in full, and `lean/README.md`'s tables. For each field (real numbers, p-adic, algebra, complex analysis, words, cellular structure, logic) say which forms are live and which are only restatements."),
 ("R-11", "Every no-go statement anywhere, with exact hypotheses: what class each excludes and what it leaves.",
  "`Rule30ZeroBoundaryBarriers`, `Rule30Realization`, `Rule30LocalConservation`, `Rule30ProductParity`, `Rule30GroupCocycle`, `no_finite_abstract_ranking_coupled` in `Rule30PeriodTwoSideways`, `Rule30XorRigidity`; RULE30-PRIZE §8.45, §8.61; PERIOD-TWO §4; RECORD-MAP 'Routes closed'; `GUARDS.md`; `reports/GPT-*BARRIER*` and any report of a closed route. Give each closure its class, its status and whether its summary overstates it."),
 ("R-12", "Transfer: what Collatz and Mahler have that we lack, and which of their closures carry over to Rule 30, and which do not.",
  "COLLATZ-PRIZE.md §1 to §8, MAHLER.md §1 and §2, RULE30-PRIZE §8.100 to §8.112, PRIZE-PROBLEMS.md §7, RECORD-MAP 'Collatz twin', 'Mahler's 3/2 problem'. The closure 'exponential sums cannot reach a single case' was reached for Collatz: does it carry over?"),
 ("R-13", "Unfinished pulls: lines dropped without a verdict, hunches never tested, questions parked and forgotten.",
  "INSTINCT.md, INSTINCT-LOCAL.md, INSTINCT-CLOUD.md, INSTINCT-GPT.md, SPARKS.md, DEEP-QUESTIONS.md, NIGHT-TASKS.md, STRATEGY-PLAN.md, STATE-OF-THE-PROOF.md. Cloud's open edge items are in the design review §2 (row R-13). Give each dropped line a card, and say which deserve a next test."),
]

L = [
 ("L-1", "Dynamics of cellular automata: permutive rules, directional entropy, expansive subdynamics, homoclinic points, rigidity, limit measures from point seeds.", "Host–Maass–Martínez, Pivato, Sablik, Boyle–Lind, Lind–Schmidt, Kari–Kopra, Milnor, Shereshevsky."),
 ("L-2", "Parity, sieves and pseudorandomness: what breaks parity, level of distribution, Gowers norms, digits of sparse sequences, character sums, Littlewood–Offord.", "Selberg, Bombieri, Friedlander–Iwaniec, Heath-Brown, Green–Tao, Gowers, Mauduit–Rivat, Bourgain, Burgess, Tao on Collatz cycles."),
 ("L-3", "Complexity and cryptanalysis: natural proofs, time-space results, proof complexity, attacks on Rule 30 as a cipher, weak keys.", "Razborov–Rudich, Williams 2025, Cook–Mertz, Cook's translation to propositional proofs, Meier–Staffelbach, Koç–Apohan, Wolfram 1986."),
 ("L-4", "Undecidable families: periodicity and immortality, generalised Collatz, busy-beaver cryptids, and exactly which families are undecidable.", "Kari, Kari–Ollinger, Cassaigne–Ollinger–Torres-Avilés, Conway, Kurtz–Simon, bbchallenge, Stérin–Woods."),
 ("L-5", "Arithmetic of Cantor sets and p-adic dynamics: integers and rationals on Cantor sets, T-functions, one-sided shift automorphisms.", "Furstenberg, Lagarias, Anashin, Khrennikov, Shparlinski, Schleischitz, Bloshchitsyn, Boyle–Franks–Kitchens, Hedlund."),
 ("L-6", "Termination and verification: matrix and arctic interpretations, regular model checking, closed-language deciders, inductive invariants.", "Yolcu–Aaronson–Heule, Endrullis–Waldmann–Zantema, Koprowski–Waldmann, Abdulla, Bradley's IC3, bbchallenge's finite-automata reduction."),
 ("L-7", "New work since mid-2025 on Rule 30 and on columns of elementary rules: preprints, forums, notes. What has the outside world said since the prize for agents opened?", "Condrey arXiv:2609.09431 and anything citing it; Wolfram Community, MathOverflow, arXiv listings in nlin.CG, math.DS, cs.CC; rule30prize.org."),
]

def main():
    which = sys.argv[1] if len(sys.argv) > 1 else "w1"
    if which == "w1":
        tasks = []
        for i, locus, reads in R:
            h = write_task(i, READER.replace("{locus}", locus).replace("{reads}", reads), REC_FULL)
            tasks.append({"id": i, "effort": "high"})
        for i, locus, reads in L:
            h = write_task(i, LIBRARIAN.replace("{locus}", locus).replace("{reads}", reads), REC_FULL)
            tasks.append({"id": i, "effort": "high"})
        write_batch("w1", tasks, 8)
        print("wrote", len(tasks))

if __name__ == "__main__":
    main()
