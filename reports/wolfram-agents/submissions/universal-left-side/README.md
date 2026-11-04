# For Local: build, check and post the universal-left-side module

The release module is `Rule30UniversalLeftSide.lean` (Local, L1506–L1507). It proves common-shift agreement through wheel 53,207 and realizes the first two distinct word continuations at wheel 53,208. `cloud-generic-Rule30UniversalLeftSide.lean` is Cloud's independent proof of the
generic theorem (`universal_of_strip` in the same interface, through the kit's `solutions_agree` and `white_shift`), kept as the
second proof; it is not part of the posted files. Texts: `title.txt`, `abstract.txt`, `essay-prose.md`.

1. Local prepared the kit branch on main `722a0c51`. For a fresh checkout, copy `Rule30UniversalLeftSide.lean` to `lean/Ruliology/CellularAutomata/`. Add `public import Ruliology.CellularAutomata.Rule30UniversalLeftSide` to
   `lean/Ruliology.lean` next to `Rule30LeftCoincidence`. Add the row to `lean/README.md` ("Added in the kit"):

   | `Rule30UniversalLeftSide` | 2026-11-04 | Every configuration with a leftmost black cell eventually shares the singleton’s left-diagonal words through zero-based wheel 53,207 up to one common time shift. Wheel 53,207 is white, and the word at 53,206 has even weight 6 over sixteen ticks. At the child wheel 53,208 two finite configurations realize complementary words, and no common shift aligns the whole prefix through that child. Rowland located this first possible fork in §5 (2006). Contributed by Gareth Herbert with Claude (Anthropic) and GPT (OpenAI). | `universal_of_strip`, `universal_left_side`, `one_left_side`, `seed_left_side`, `fork_dichotomy`, `first_fork`, `left_side_not_unique`, `odd_farther_weights`, `even_farther_weight` |

2. From the kit root containing `Check.lean` and `lakefile.toml`, build the module and run the official checker on all nine headlines under the repository's resource limits.

   ```sh
   module=Ruliology.CellularAutomata.Rule30UniversalLeftSide
   lake build "$module" &&
   lake env lean --run Check.lean "$module" --claim partial \
     --headline "$module.universal_of_strip" \
     --headline "$module.universal_left_side" \
     --headline "$module.one_left_side" \
     --headline "$module.seed_left_side" \
     --headline "$module.fork_dichotomy" \
     --headline "$module.first_fork" \
     --headline "$module.left_side_not_unique" \
     --headline "$module.odd_farther_weights" \
     --headline "$module.even_farther_weight"
   ```

   For the portal check, compile the generated `Rule30Submission.lean` on the currently advertised verifier kit (image 17, `722a0c51` at review) in a clean object directory, put its object first on Lean's search path, and use the same checker arguments with `module=Rule30Submission`. GC2654 checked the updated release bytes on current kit main `a91c7273` and verifier image 17 (`722a0c51`). The official checker passed all nine named headlines on both, replaying 193 constants in each standard-mode run. Their combined axioms were `propext`, `Classical.choice` and `Quot.sound`. The full `lake build Ruliology` is a separate integration check. Both M5 attempts stopped at the memory floor (L1508). Record the final revision and actual result if that check completes elsewhere.

3. For the portal entry, `make_portal_form.py` generates `Rule30Submission.lean` from the kit file by converting its header, imports and namespace. Both source forms directly import `Rule30Prize` and `Rule30AgedLeftDiagonals`. Use `title.txt`, `abstract.txt` and the release notebook built from `essay.md`. That essay is generated from the prose and portal source by `tests/probes/wolfram/assemble_universal_left_essay.py`. If a release input changes, regenerate the affected derivatives, update `essay.sha256`, and have Local rerun the notebook gates before posting. The numeric reference `B` is the singleton’s wall-frame row at tick 72,000 **truncated to its low 53,209 bits** by replay. The kernel uses the supplied literal and checks its sixteen-tick return.

4. Local posts on the owner’s word after the final revision's review and checks. For the companion kit PR include the module, aggregate import and README row. Append the actual public portal entry link to `PR-BODY.md` after it is issued, and update the checks paragraph from the final receipts. Record both public links in the ledger.
