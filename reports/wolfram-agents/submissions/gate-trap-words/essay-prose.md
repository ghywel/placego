# The Gate Trap Forbids Five Gap Words, and Q01Gap Weakens to Q01GapWords

Gareth Herbert; Claude (Anthropic); GPT (OpenAI). 9 November 2026.

## 1. The statement

For period `2` the kit drives a right half `R` with the alternating center column and reads `u R s`, column `1` at the odd time `2 s + 1` (`Rule30PeriodTwoSideways.u`). The coupled question `CQ01` asks that the candidate left row `Psi R`, whose free bits are the complement of `u R`, is never finitely supported. The kit's gate trap (`Rule30GateTrap`) is a set of `829` windows of the columns `1..16` at the odd times. It is closed under the double step whatever column `17` does. After the window of `R` enters it, the black cells of `u R` come `3` or `5` steps apart (`gaps_of_entry`). The kit's open `Q01Gap` excludes every finitely supported left half with free bits of that shape. With it, every right half that enters the trap satisfies `CQ01` (`not_finSupp_Psi_of_Q01Gap`), the empty one included (`CQ01Empty_of_Q01Gap`).

A gap word `g₁ g₂ … gₖ` is read from a black cell at `s` when the next black cells are at `s + g₁`, `s + g₁ + g₂`, … and the cells between them are white. This module proves that the trap forbids more than other gaps.

- `gap_words_of_entry`: once the window of `R` is in the trap at an odd time `t0`, `u R` never reads `333`, `3353`, `3533`, `3553` or `5533` from a step `s` with `t0 ≤ 2 s + 1`. `no_3353_of_entry` is the word `3353` alone.
- `no_33535555_of_entry`: nor `33535555`, which begins with `3353`.
- `no_late_33`: after any two gaps, the next two are not both `3`. With `gaps_of_entry`: from the third black cell after entry on, `u R` is a concatenation of the blocks `001` and `00001` in which no two blocks `001` are adjacent and no two are separated by exactly two blocks `00001`.
- `minimal_paths`: each word is minimal for the trap. Removing its first or its last gap gives one of `33`, `335`, `353`, `533`, `355` and `553`, and a path of the trap graph reads each of these.
- `Q01GapWords` (open) is `Q01Gap` with the five words excluded as well. `Q01Gap` implies it (`Q01GapWords_of_Q01Gap`). It still gives `¬ FinSupp (Psi R)` for every right half whose window enters the trap (`not_finSupp_Psi_of_Q01GapWords`), and so `CQ01Empty` (`CQ01Empty_of_Q01GapWords`).

## 2. The trap graph

A window is coded as a `16`-bit number, bit `i` being column `i + 1` (`Rule30Certificates.GateTrap.decode`). From an odd time column `0` is white, then black. So two steps after the window `w` the window is `step2 w x₁ x₂`, where `x₁` and `x₂` are the two values of column `17`. The trap graph has the `829` windows as vertices and the four double steps from each as edges. Every edge stays in the trap (`trapClosed_ok`). A real right half is a walk in this graph: its windows at the odd times move by `step2` with its own values of column `17` (`win_step2`). Once inside, it stays inside (`win_mem_trap`). So a word that no path of the graph reads in column `1` is never read by a right half after entry.

## 3. The check

For a word `b₀ b₁ … bₙ` of column-`1` samples, the layer `Lₖ` is the set of windows of the trap that can have read `b₀ … bₖ`. The first layer holds the windows that read `b₀`, and each next layer the double steps that read the next letter. The kernel checks three facts for each word: the windows of the trap that read `b₀` are in `L₀` (`startOK`); every double step from `Lₖ₋₁` that reads `bₖ` lands in `Lₖ` (`stepOK`); and the last layer is empty. By induction along the word, a right half in the trap never reads it (`not_reads_of_check`).

The five words share their first samples, so the layers form a tree. There are `40` nonempty layers in all, checked by one start check and `44` step checks, each a separate kernel check. The layers of `3353` have `188, 191, 186, 68, 68, 69, 17, 21, 21, 18, 21, 29, 40, 41` and `0` windows. These are the sizes GPT first computed for this word.

## 4. The whole language

By computation (not in Lean), the five words are all that the trap forbids. A finite word over the gaps `3` and `5` is read along some path of the trap graph exactly when it contains none of them. The test is a product of two deterministic automata: the trap's path sets on gap words, starting from its `188` black windows, and the three-gap memory of the five words. Explored over all `19` reachable pairs, the two never disagree. Up to `14` gaps there are `17` distinct path sets.

Eventually the language is simpler. The words over `3` and `5` that contain neither `33` nor `3553` are those in which every `3` is isolated and two consecutive `3`s are separated by one `5` or by at least three. That class has `0.132` bit of entropy per sample (the root `λ = 1.096` of `λ⁻⁸ + λ⁻¹⁸/(1 − λ⁻⁵) = 1`). The class of `Q01Gap`, all sequences of `001` and `00001`, has `0.256` bit per sample (`λ⁻³ + λ⁻⁵ = 1`). So `Q01GapWords` excludes a class of half the entropy, but the entropy is still positive.

The empty right half enters the trap at time `293`, with the black cell of step `146` (`entry_empty`, `u_empty_146`). From there its gaps run `5, 3, 3, 5, 5, 5, 3, 5, 5, 5, 3, …`: its pair `33` comes right after entry, as `no_late_33` allows. In its first `431` gaps after entry it reads none of the five words, and no other pair `33` occurs (computation, consistent with the theorems).

## 5. What it explains

In finite right halves beside the alternating center, rows often enter the trap during or soon after the gap word `33535555`. We measured two samples of right halves: `20,000` random rows of support `30`, run to time `8001`, and all `1,048,575` rows of support at most `20`, run to time `2001`. In them the word began `1,532` and `77,642` times. `98.8%` and `98.9%` of these occurrences were followed by entry before the horizon, and none of the `79,174` began after entry (MEASURED). `no_33535555_of_entry` explains the last count: the word cannot begin after entry. So the decline of its occurrences over time can come from the shrinking population of rows not yet trapped. None of this shows that every finite right half enters the trap. That is the open part of the kit's reduction.

The open hypothesis on the left half weakens accordingly. `Q01GapWords` has to exclude fewer free bits than `Q01Gap`, and it gives the same consequences for the right halves that enter the trap. The kit's `Rule30PeriodTwoWidth13.CQ01_of_RD_of_Q01Gap` uses `Q01Gap` only through `not_finSupp_Psi_of_Q01Gap`. The same proof therefore gives `CQ01` from its open dichotomy `RD` and `Q01GapWords`. That is not formalized here, because the verifier's kit predates that module.

## 6. Worked numbers

The cell below reads the trap's `829` codes from the kit and counts the edges that stay inside. It then computes the layer sizes of the five words and lists the minimal forbidden gap words of up to eight gaps, with the number of distinct path sets among the allowed ones.

## 7. Prior art and scope

The trap, `gaps_of_entry`, `Q01Gap` and the method are the kit's `Rule30GateTrap` and `Rule30Certificates.GateTrap` (R. Bosdure, Rule 30 Prize submission R30-20261027-230bc7). Its four layers after a black cell give the gaps `3` and `5`. Our layers give the gap words.

The words themselves are partly known.
- R30-20261030-60990f (J. Lee, with GPT and Claude) proves in Lean that for the one-cell right seed, black only at position `1`, the gap sequence of `u` never contains `33`, `3553` or `3535353`. It uses an `18`-cell relaxation with an invariant pool of `2,040` states, and it credits `33` and `3553` to the authors' earlier work. That is one right half. The theorems here hold for every right half that enters the kit's trap.
- Our own record has parts of this language. An earlier hand proof, in a different frame, shows that two short returns never follow each other after entry into a closed core. A computation shows that inside the kit's trap `33` occurs at most once and `3553` and `3535353` never occur. That record also names the weaker form of `Q01Gap` that `Q01GapWords` formalizes here.
- [`lhallee/rule30-open`](https://github.com/lhallee/rule30-open) computes a larger gap trap of windows with a count, with `3,562` entry windows, which contains the kit's `829` (`findings/period-two/gate-census.md`). It notes that `Q01Gap`'s free bits have positive entropy. Its notes record no two adjacent gaps `3` for the empty right half, by computation.
- `Rule30PeriodTwoWidth13` (R30-20261109-62afca) proves, for every right half, a nine-pair gap language for the left trace. Its pairs include `33`, `35`, `53` and `55`, so on words over `3` and `5` it allows everything.
- `Rule30SidewaysLocks` puts its lock of period five inside the trap (`lock5_win_trap`). Its gaps `5, 5, 5, …` are allowed here, as they must be.

`3535353` is not among the five words. The `16`-column trap graph reads it, so the trap alone cannot exclude it. Lifted to `18` columns (`3,316` windows, closed), the trap kills it, and up to `14` gaps that is the only word the lift adds (computation, not in Lean).

What is new:
- the five words in Lean for every right half that enters the kit's trap, with their minimality, and the completeness of the list for the trap graph;
- `3353` and the start words `333`, `3533`, `5533`, which describe how a pair `33` can occur once right after entry;
- `Q01GapWords` in Lean, with its reductions.

The exclusion of `3353` was found by GPT's exact path-set computation. The other words of the list, the completeness computation and the module are Claude's. Nothing here proves `Q01Gap`, `Q01GapWords`, `CQ01`, `CQ01Empty` or the absence of period `2`.
