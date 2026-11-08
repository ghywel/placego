# S-02 release review

GPT GC2725/GC2726, 8 November2026. Owner requests S02 while Local prepares S02/S04. Research continuation is parked.

**Verdict: mathematics, both Lean sources and existing kernel receipts PASS. Corrected release text is ready. Final release awaits Local's notebook/pin refresh for that text.** No proof, theorem type, headline, title or computational output changed. Nothing has been posted.

## Mathematics and formal source

I read the complete506-line kit module and the portal form, including the two kernel stages, `sync`, `twin_of_factors`, all four chains and the three final twin theorems. After normalizing imports/namespace/open/end wrappers, their proof bodies are identical. The statement matches GC2690:

- y is nonzero and t≥46; the twin is of x=F^(t−2)y, with equal width, equal bit0 and the same F² image.
- Immortality inheritance requires even t. The proof handles the first G-check through equal bit0 and later checks through the common G-image.
- Off-orbit means no equality to any `iter G j y`: width fixes the only possible orbit position to x, where distinctness rules it out. It is not a new future class.

`F_shiftRight` is valid for every natural cut m, with the cut moving one cell outward per tick. Reading a normalized twenty-cell band additionally requires width≥20. The two stages cover4096 thirteen-cell starts with top cell black, followed by all512 lower-seven-bit extensions of the four C13 phases. The settling proof then uses cycle closure. `band_late` accounts for the initial width delay, giving45; `late_twin` uses the band in Fx at t−1, giving t≥46.

The reset proof retains the extra input bit and two consecutive recovered states. `sync` keeps equality of the entire remaining input suffix. The chain inequality transfers correctly across the one-cell shift between Fx and F²x. The second inversion agrees with the original row above the upper reset, so truncation produces an actual finite natural, not merely a formal infinite predecessor. Equal width is obtained from the common two-step image and the top-bit growth law. I found no carrying defect.

The key official definitions/theorems were read in the pinned kit: F/G/iter, `back`, `eq_back`, `zrow_back`, `zrow_rowOfNat_one`, the natural-row conversion and top-bit facts. The existing receipts show143 replayed declarations, nine matching headlines, standard axioms only and no new axioms, at kit48d8fbbc and verifier5fb59158. This is a read of Local's successful builds, not a fresh Intel compile.

## Concrete scope repairs applied

1. The abstract's26-tick band statement now explicitly assumes a twenty-cell band whose top cell is black. The general row statement retains its proven t≥46 bound.
2. The prose now explains autonomy across the **moving** cut, and says when a twenty-cell top band can first be read.
3. The unformalized2^3955 aside now retains GC2690's even-time and survival guards and says the7911 levels are single F-ticks. Its uncomputed onset and exclusion from this formalization remain explicit.
4. The preregistration's result no longer calls46 an optimal twin onset. The formal theorem proves a sufficient bound. A proof mutation failing at an `omega` step is not a counterexample to the strengthened theorem. Sharpness of the normalized band's26-tick settling was separately computed in GC2690; it is not minimality of the late-twin bound.

The kit catalogue patch also qualifies the twenty-cell band. It applies cleanly to current main. The assembler deterministically regenerated `essay.md` with the unchanged portal Lean embedded verbatim. The corrected abstract has184 words.

## Exact notebook and provenance read

Downloaded Local's write-once packet,535,902 bytes, SHA256 `15a74df5fbabef068dc6e04f0476b0d232c6c52dc28893bcd3b3c991dc7469d9`. The nb1 notebook is129,190 bytes, SHA256 `055b6763d2c9ca64df8d5de45727a2a24cb768b4b75f2f9231d6f936af23be86`.

Without evaluating Wolfram code, I decoded the actual serialized icon string and checked it byte for byte against the portal source, including its final newline; the old Abstract cell also matches the old essay exactly. Public notebook home/scratch-path checks pass. The six output receipts contain the expected14/12 and seven twin checks, the kit True cell, LeanEnvironment, theorem types, the standard axiom sets and KernelChecked143. The build receipt is RESULT OK,18.5s, zero Message cells. Its handler-event count is not zero; I claim zero Message cells, not zero internal handler events.

The current PR60 is OPEN at `db6e71128339d1fc45b5a7ab5f2bade997996ae3`. I read its body, current maintainer discussion and complete changed Lean source, plus the exact linked immutable inverse-cascade source, provenance and statement guards at archive3ebd1501497f168c04b3b0fab00595b1266f5a00. The archived mathematical source matches the PR head. `scheduled_cascade_closes` assumes the reset schedule; it does not supply universal late resets. Its following input cell is retained. S02's attribution and distinction are accurate. The current maintainer import-placement issue belongs to that PR, not S02's correctly placed import.

The Feynman/`Rule30Predecessors.predCount_eq_one_iff` attribution and the fixed-prefix scope of `Rule30PrefixMerger` were checked. The settling result is credited to `Rule30UniversalLeftSide`/`Rule30FourLeftSides`; the new late twin conclusion is distinguished from those helpers. Cloud CL752's prior outside-work clearance is retained. A fresh complete index at11:20:04Z, kit48d8fbbc, shows zero changes since the preceding check. No new novelty assertion is made by this review.

## Remaining release gate

Because abstract/prose changed, **nb1 is superseded for release**, though its Lean payload remains the approved source. Local owns Wolfram and must rebuild from the corrected assembled essay, refresh notebook/abstract/essay pins in the private post script, and run the dry check again. Please publish the new notebook digest/receipt and sanitized pin/dry-run receipt for a short byte read. Rebuilding the unchanged Lean proofs is not required by this text repair unless the verifier/toolchain or module bytes change. Full catalogue build was not performed or claimed.

Current reviewed pins:

| Item | SHA256 |
|---|---|
| Portal Lean | `4322dc313994d98bda9abc93861fa0c9ef2bc9473e0bf5480fe59631e19217b4` |
| Kit Lean | `ed43f13da315ec68a934cd7fd53949e12ee5a4744a7a138b3c2ebc736d3f8203` |
| Corrected abstract | `72fcf6cc76bc0fb7c9f1fc281debdd72c5593d467a4dcb1f9167b0d8eec0e6ca` |
| Corrected essay | `0d1086135e52a7fbc242be9ec60b2cd0208de47601ced28a9fbd8043d0c817a5` |

The private post script and its old dry-run success are Local's reported checks, not independently inspected here. The notebook refresh/dry-run gate is concrete and is the only packet hold found. Posting still follows the owner's release word. The research pull remains parked.
