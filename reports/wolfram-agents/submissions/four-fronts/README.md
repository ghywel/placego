# The forced front on the four strips

**Status (L1525, 4 November 2026): waiting for GPT's read, then the owner's word. Nothing posted.** Cloud's review passed (CL735), and its four suggestions for the prose are in. Release notebook sha256 `d2eeeea8148eef7288c917a980f6c0484e49dcba7ee2f8ffb3c8b975b825917d`, 401,305 bytes, built on verifier image 17 (kit `722a0c51`), receipts `cited/l1525-four-fronts/nb3-receipts.tar.gz` (8,070 bytes, 442480f516174d46…). The earlier notebook of L1524 (`ab4479f8…`) is superseded.

**What changed from CL734.** Cloud's six modules (below) build and pass `Check`, but they do not fit where they have to go: the kit takes certificate data "in one module per family that builds in under a minute and 4 GB", and the verifier builds one module within four minutes for notebook, build and replay together. The release form keeps Cloud's theorems and replaces the four data modules with a walk (`frun_of_walk`), which reads the recursion off one addition, one shift and one mask per tick.

| Form | File | sha256 | Build (M5) | `Check` |
|---|---|---|---|---|
| Kit, generic | [`Rule30FourFrontsBase.lean`](Rule30FourFrontsBase.lean) | `eb2dd2f57df49c57…` | 1 s | |
| Kit, walk and theorems | [`Rule30FourFronts.lean`](Rule30FourFronts.lean) | `8a84db032d90ba16…` | 7 s, 2.1 GB | pass, kit main 96b4f2a, 256 constants, 11 headlines |
| Portal | [`Rule30Submission.lean`](Rule30Submission.lean) | `134d62fba8e16f30…` | 7 s, 2.4 GB | pass, kit 722a0c51, 681 constants, 11 headlines |

Texts: [`title.txt`](title.txt) (`90f8471f…`), [`abstract.txt`](abstract.txt) (237 words, `e58364e0…`), [`essay-prose.md`](essay-prose.md) (`d4ed8685…`), `essay.md` (`4727ca34…`). Generators: [`four_fronts_fast.py`](../../../../tests/probes/wolfram/four_fronts_fast.py) with [`FourFrontsWalkCore.lean`](../../../../tests/probes/lean/FourFrontsWalkCore.lean), [`four_fronts_portal.py`](../../../../tests/probes/wolfram/four_fronts_portal.py), [`assemble_four_fronts_essay.py`](../../../../tests/probes/wolfram/assemble_four_fronts_essay.py). Driver: [`four_fronts_notebook.wl`](../../../../tests/probes/wolfram/four_fronts_notebook.wl). Kit PR text: [`PR-BODY.md`](PR-BODY.md).

Headlines: `forced_front_four`, `forced_front_four_uniform`, `forced_front_four_left_side`, `forced_front_four_seed`, `classification_bounded`, `forced_front_low`, `forced_front_low_left_side`, `FA0_87866`, `FA1_87866`, `FB0_87866`, `FB1_87866`. `forced_front_low` is new: it gives the 53,207 statement of CL733 part C, so the entry covers both versions and `Rule30ForcedFront` is not needed.

Local alone posts, on the owner's word; any change to the Lean, essay or abstract moves the pins and needs a new notebook.

## Questions for GPT (one read before posting, at the owner's request)

The Lean is machine-checked at two kit commits and Cloud read the walk step by step (CL735), so this read is of the text against the Lean. GPT may change the texts and the Lean's comments, with reasons in the ledger, and Local rebuilds the notebook on any change.

1. **Section 1 against the Lean.** Do the theorem text and "from tick 177,575 of its own clock at the latest" say what `forced_front_four_left_side`, `OnStrip` and `Ld` say? The shift is applied to the configuration's own clock and `s ≤ 15`.
2. **Below the first fork.** Is "the strip there is `A0`" right for `forced_front_low_left_side`, whichever of the four strips the configuration is on?
3. **Sections 2 to 4 against the definitions.** Does the prose match `fstep`, `srch` and `F`? In section 4, the replacement of the maximum by a running tick rests on `F_mono`. Is anything claimed for the walk that `run_arrival`, `arrival_unique`, `walk_black` and `frun_of_walk` do not give?
4. **Section 6.** The bound `1 + 16 j` is stated for the recursion on a strip, by the sixteen-tick wait, and is not a Lean theorem here. It is offered as the form of `frontBound_le_linear`, not as that lemma. Is that wording safe? The two growth rates are labelled as computed.
5. **Scope.** Title and abstract against the Lean: "is on its strip", "by tick 177,575", and the closing sentence about the cut.
6. **Prior art.** Searched with `known_find.py` at kit 96b4f2a, on frontBound, settling time, transient, onset of periodicity. Candidates read: `Rule30FrontLaw`, R30-20261103-1c93e6, R30-20261103-050b68, R30-20261027-e324b6, all credited in section 7. Does anything already give an explicit settling tick for every configuration with a leftmost black cell?
7. **Kit PR.** Does [`PR-BODY.md`](PR-BODY.md) meet the catalog's rule on certificate data? The rule names "every configuration with a leftmost black cell" as a family; the module builds in 7 s at 2.1 GB.

---

## CL734 as Cloud delivered it (Cloud, 4 November 2026)

**Claim (PROVED, Lean 4.35.0 kernel on Cloud's Linux host; Local's build of record to follow).** Every configuration with a
leftmost black cell is on one of the four strips of `Rule30FourLeftSides` (A0, A1, B0, B1) on every wheel through 87,866
from tick 177,560 + s of its own clock, where s ≤ 15 is its phase: `forced_front_four_left_side`. Behind it,
`forced_front_four` gives the time wheel by wheel (the phase-0 settling recursion F_v of the kit's `Rule30FrontLaw` on the
strip's sixteen rows), `forced_front_four_uniform` the single tick 177,560 = max_v F_v(87,866), `forced_front_four_seed` the
single black cell, and `classification_bounded` the classification of L1513 with its shift bounded by 15. The fronts at
wheel 87,866: A0 176,968, A1 177,229, B0 177,170, B1 177,560 (`FA0_87866` … `FB1_87866`). The kit-style linear bound with
five white wheels is 2,811,713. [Corrected in CL735: the forks do not double the period, and at period 16 the bound is 1,405,857.]

**Modules** (kit form, on kit main 8cf1bd4, all under `Ruliology.CellularAutomata`; the two generic ones are here as
`cloud-*.lean`, the four kernel modules are data and live in the shared store under `cited/four-fronts/`, write-once):

| Module | sha256 | Role |
|---|---|---|
| `Rule30FourFrontsBase` | 9f0476c5… | the recursion as a state machine over a word function; L1513's moves with the time carried (`step_black`, `step_white`, `white_shift`, `white_fork`, `extend_from`, `low_from`); `F_congr` |
| `Rule30FourFrontsA0` | e0375fe7… | A0's sixteen rows as literals, each checked against `rowAt 87867 A0 r`; the words; 18 block equations by `decide +kernel` |
| `Rule30FourFrontsA1` | a6cbf079… | the same for A1 |
| `Rule30FourFrontsB0` | 41675ce0… | the same for B0 |
| `Rule30FourFrontsB1` | 9e8b812d… | the same for B1 |
| `Rule30FourFronts` | cb0b060b… | the words are the strips', the chains of blocks, the tree, the headlines |

The four kernel modules are regenerated byte-identically from the record's four-left-sides module by
`python3 tests/probes/wolfram/four_fronts_gen.py OUTDIR` (13.7 s), which also prints the 72 block pairs the kernel confirms.

**Build and check recipe** (a 16 GB host). Kit main 8cf1bd4 with the six modules in `lean/Ruliology/CellularAutomata/` and
their six `public import` lines after `Rule30FourLeftSides`'s in `lean/Ruliology.lean`. `lake build` the base module, then
the four kernel modules one at a time with `LEAN_NUM_THREADS=1` (Cloud's host: 317–356 s and 5.8–6.3 GB each), then the
final module (1.3 s). `lake env lean --run Check.lean Ruliology.CellularAutomata.Rule30FourFronts --claim partial --headline
Ruliology.CellularAutomata.Rule30FourFronts.<name>`: pass, found, 70 constants, on all nine names above. Axioms: propext,
Classical.choice, Quot.sound on the headlines; no `sorry`, no `native_decide`.

**Posting.** Nothing posted. Local, on the owner's word: one entry of the forced front (this and the 53,207 version of
CL733 part C, `Rule30ForcedFront`), and the kit PR importing `Rule30FourLeftSides`, as L1518 proposes. Byline: Gareth
Herbert; Claude (Anthropic); GPT (OpenAI). Credits: the kit's `Rule30FrontLaw` (@AIOvernight) and R30-20261103-1c93e6 for the
recursion and the linear bound; `Rule30UniversalLeftSide` and `Rule30FourLeftSides` for the moves and the strips.
