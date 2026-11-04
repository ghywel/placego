# For Local: build, check and post the universal-left-side module

1. Kit checkout at main (the module was compiled against 722a0c5). Copy `Rule30UniversalLeftSide.lean` to
   `lean/Ruliology/CellularAutomata/`. Add `public import Ruliology.CellularAutomata.Rule30UniversalLeftSide` to
   `lean/Ruliology.lean` next to `Rule30LeftCoincidence`. Add the row to `lean/README.md` ("Added in the kit"):

   | `Rule30UniversalLeftSide` | 2026-11-04 | Rowland's one left side (2006, §5) below the first fork: for every strip admissible below a cut `J` (base words black, the reset recurrence at every wheel, no even fork: the nearer word has blacks arbitrarily late, or it is white and the farther word has odd parity over a common period of the lower strip) and every configuration with a leftmost black cell, one time shift aligns every wheel below `J` with the strip from some time on; any two such configurations share one left side below `J` up to a shift; the single seed's diagonals are the strip's. The universal strip generated from `1, 1` by the recurrence alone is admissible below `53208` (white words at wheels 2, 7, 28, 399 with farther weights 1, 1, 3, 3; wheel 53,207 has weight 6, the first fork): a finite check of the data, replayed outside Lean. Contributed by Gareth Herbert with Claude (Anthropic) and GPT (OpenAI), after Rowland's argument; the reset lemmas are the kit's and `Rule30LeftCoincidence`'s. | `one_left_side`, `same_left_side`, `seed_left_side`, `Admissible`, `par_shift` |

2. Build and check, as the verifier does:

       lake build Ruliology.CellularAutomata.Rule30UniversalLeftSide
       lake env lean --run Check.lean Ruliology.CellularAutomata.Rule30UniversalLeftSide --claim partial \
         --headline Ruliology.CellularAutomata.Rule30UniversalLeftSide.one_left_side

   Expected: verdict pass, axioms propext and Quot.sound, 58 constants replayed (as on Cloud's Linux check).

3. Portal entry (Kit Contribution): `Rule30Submission.lean` with the module's content under `namespace Rule30Submission`,
   importing `Rule30PrizeKit` and `Ruliology.CellularAutomata.Rule30LeftCoincidence` plus
   `Ruliology.CellularAutomata.Rule30FiniteDiagonals`, as for the synthesis entry (R30-20261103-3cf160); abstract from
   `abstract.txt` (count the words); essay from `essay-prose.md` with the Lean cell; headline `one_left_side`. Record the id
   in the ledger.

4. Kit PR: the module, the import line and the README row; the PR as the submission's repository.

Nothing is posted without the owner's word. GPT's carrying read of the hand proof (PROOFS.md waiting room, CL724) is requested
before posting; the Lean is independent of it.
