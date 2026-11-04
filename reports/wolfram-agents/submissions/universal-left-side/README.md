# For Local: build, check and post the universal-left-side module

File of record: `certificate-draft.lean` (Local, L1503: the generic induction, the certificate on `B`, the instance through
53,207, the fork theorem, the parity checks). `cloud-generic-Rule30UniversalLeftSide.lean` is Cloud's independent proof of the
generic theorem (`universal_of_strip` in the same interface, through the kit's `solutions_agree` and `white_shift`), kept as the
second proof; it is not part of the posted files. Texts: `title.txt`, `abstract.txt`, `essay-prose.md`.

1. Kit checkout at main (both files compile against 722a0c5). For the kit form, give the draft the module header (`module`, the
   `public import`s, `@[expose] public section`, the namespace `Ruliology.CellularAutomata.Rule30UniversalLeftSide`) and copy it
   to `lean/Ruliology/CellularAutomata/Rule30UniversalLeftSide.lean`. Add `public import Ruliology.CellularAutomata.Rule30UniversalLeftSide` to
   `lean/Ruliology.lean` next to `Rule30LeftCoincidence`. Add the row to `lean/README.md` ("Added in the kit"):

   | `Rule30UniversalLeftSide` | 2026-11-04 | Rowland's one left side (2006, §5) below the first fork: for every array with the left-diagonal recurrence and a black edge, hence every configuration with a leftmost black cell, and every strip admissible through `J` (base words black, the reset recurrence at every wheel, no even fork: the nearer word has blacks arbitrarily late, or some period `L` of the lower strip is an antiperiod of the child; Rowland's odd parity gives the antiperiod), one time shift aligns every wheel through `J` with the strip from some time on; any two such configurations share one left side through `J` up to a shift; the single seed's diagonals are the strip's. With `B`, the seed's row at tick 72,000 on 53,209 bits, as the strip (its 16-tick return kernel-checked), the seed's strip is admissible through `53207` (white words at wheels 2, 7, 28, 399 with farther weights 1, 1, 3, 3; wheel 53,207 has weight 6), so every configuration with a leftmost black cell has the seed's left side through 53,207 up to one time shift (`universal_left_side`); and `B` and `B ⊕ 2^53208` realize the two continuations at 53,208 with no shift relating them (`first_fork`): Rowland's first fork, as he located it. Contributed by Gareth Herbert with Claude (Anthropic) and GPT (OpenAI), after Rowland's argument; the reset lemmas are the kit's and `Rule30LeftCoincidence`'s. | `universal_of_strip`, `universal_left_side`, `one_left_side`, `seed_left_side`, `fork_dichotomy`, `first_fork`, `odd_farther_weights`, `even_farther_weight` |

2. Build and check, as the verifier does:

       lake build Ruliology.CellularAutomata.Rule30UniversalLeftSide
       lake env lean --run Check.lean Ruliology.CellularAutomata.Rule30UniversalLeftSide --claim partial \
         --headline Ruliology.CellularAutomata.Rule30UniversalLeftSide.universal_left_side \
         --headline Ruliology.CellularAutomata.Rule30UniversalLeftSide.first_fork

   Expected: verdict pass, axioms propext, Classical.choice and Quot.sound (propext and Quot.sound for `first_fork`), no new
   axioms; Cloud's Linux check of the draft as `Rule30Submission` is recorded in CL726.

3. Portal entry (Kit Contribution): `Rule30Submission.lean` = the draft without the `Rule30LeftCoincidence` import (the portal's
   verifier kit at c42f6e51 lacks that module, L1503), importing `Ruliology.CellularAutomata.Rule30AgedLeftDiagonals`; abstract
   from `abstract.txt` (count the words); essay from `essay-prose.md` with the Lean cell; headlines `universal_left_side` and
   `first_fork`. Record the id in the ledger.

4. Kit PR: the module, the import line and the README row; the PR as the submission's repository.

Nothing is posted without the owner's word. GPT's carrying read of the hand proof (PROOFS.md waiting room, CL724) is requested
before posting; the Lean is independent of it.
