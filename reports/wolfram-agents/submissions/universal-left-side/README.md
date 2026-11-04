# For Local: build, check and post the universal-left-side module

1. Kit checkout at main (the module was compiled against 722a0c5). Copy `Rule30UniversalLeftSide.lean` to
   `lean/Ruliology/CellularAutomata/`. Add `public import Ruliology.CellularAutomata.Rule30UniversalLeftSide` to
   `lean/Ruliology.lean` next to `Rule30LeftCoincidence`. Add the row to `lean/README.md` ("Added in the kit"):

   | `Rule30UniversalLeftSide` | 2026-11-04 | Rowland's one left side (2006, §5) below the first fork: for every array with the left-diagonal recurrence and a black edge, hence every configuration with a leftmost black cell, and every strip admissible through `J` (base words black, the reset recurrence at every wheel, no even fork: the nearer word has blacks arbitrarily late, or some period `L` of the lower strip is an antiperiod of the child; Rowland's odd parity gives the antiperiod), one time shift aligns every wheel through `J` with the strip from some time on; any two such configurations share one left side through `J` up to a shift; the single seed's diagonals are the strip's. The seed's strip is admissible through `53207` (white words at wheels 2, 7, 28, 399 with farther weights 1, 1, 3, 3; wheel 53,207 has weight 6, the first fork): a finite check of the data, replayed outside Lean. Contributed by Gareth Herbert with Claude (Anthropic) and GPT (OpenAI), after Rowland's argument; the reset lemmas are the kit's and `Rule30LeftCoincidence`'s. | `universal_of_strip`, `one_left_side`, `same_left_side`, `seed_left_side`, `antiperiod_of_odd_parity`, `D_recurrence` |

2. Build and check, as the verifier does:

       lake build Ruliology.CellularAutomata.Rule30UniversalLeftSide
       lake env lean --run Check.lean Ruliology.CellularAutomata.Rule30UniversalLeftSide --claim partial \
         --headline Ruliology.CellularAutomata.Rule30UniversalLeftSide.universal_of_strip

   Expected: verdict pass, axioms propext, Classical.choice and Quot.sound, 42 constants replayed (as on Cloud's Linux check,
   kit main 722a0c5). Local's certificate layer (L1502: `B`, the Nat-row bridge to `Ld`, the sixteen-row checks, the instance at
   the full cut, the fork theorem) composes with `universal_of_strip` and `one_left_side` as stated.

3. Portal entry (Kit Contribution): `Rule30Submission.lean` with the module's content under `namespace Rule30Submission`,
   importing `Rule30PrizeKit` and `Ruliology.CellularAutomata.Rule30LeftCoincidence` plus
   `Ruliology.CellularAutomata.Rule30AgedLeftDiagonals`, as for the synthesis entry (R30-20261103-3cf160); abstract from
   `abstract.txt` (count the words); essay from `essay-prose.md` with the Lean cell; headline `universal_of_strip` (or `one_left_side`). Record the id
   in the ledger.

4. Kit PR: the module, the import line and the README row; the PR as the submission's repository.

Nothing is posted without the owner's word. GPT's carrying read of the hand proof (PROOFS.md waiting room, CL724) is requested
before posting; the Lean is independent of it.
