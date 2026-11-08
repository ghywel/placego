# Block 9, step 1: the period-3 and period-4 language skeletons, and whether wider strips weaken C3

*Local, 8 November 2026, 19:00 UTC, L1599. [WARM-LEADS](../WARM-LEADS.md) Block 9 (door 5), started at the owner's word: "block 9 of warm leads is i think untouched, can this be progressed". Computation on Local's M5. Code: [`lang.c`](../tests/probes/swarm/sw02/block9/lang.c), with the prediction written in its header before any run; ladders [`ladder.sh`](../tests/probes/swarm/sw02/block9/ladder.sh), [`ladder2.sh`](../tests/probes/swarm/sw02/block9/ladder2.sh) and [`ladder3.sh`](../tests/probes/swarm/sw02/block9/ladder3.sh), each with its own prediction; output [`ladder.out`](../tests/probes/swarm/sw02/block9/ladder.out); summary [`summarize.py`](../tests/probes/swarm/sw02/block9/summarize.py).*

## The answer

- **In degree, wider strips weaken C3, and they do so monotonically.**
  - The left statement only has to fail for free words in a sofic language X_B that shrinks as the width B grows. The shrinking is PROOF-SKETCH below; the measurements are COMPUTED.
  - Beside 001 the free bits drop from 1/3 bit per tick (C3s001) to 0.204 (rule30-open's run-length form). At width 22 they are about 0.084.
  - Beside 011 they drop from 1/3 to about 0.105 at width 22.
- **In kind, wider strips only restate C3.** Every X_B tested has positive entropy and is a union of irreducible sofic shifts, so periodic words are dense in it. rule30-open's argument that no finite left game closes therefore applies unchanged at every width.
- **What would change the kind** is a limit language X_∞ = ∩ X_B with no aperiodic word. Masked Jen would then exclude the period outright.
  - The 001 counts level off: the length-24 count falls by 220, 112, 32 and 14 per two added columns.
  - The 011 estimate is still falling steadily: 1.284, 1.267, 1.255, 1.243 per reading at B = 16..22.
  - So neither trend shows a zero limit up to width 22.

## What the strip graph is

Fix a center word w of period P from time T. Take vertices (phase, columns 1..B) of the right half, with one edge for each value of the free column B + 1. Every actual right half is a walk from T on, so it ends in one cyclic SCC.

Call an SCC *labelled* when column 1 at every white phase is a function of its level modulo the SCC's cycle gcd. If the walk ends in a labelled SCC, column 1 is eventually periodic at the white times. Masked Jen excludes that when the configuration has a leftmost black cell (`Rule30FiniteMaskedJen.masked_jen`; the citation repair of the SW-02 self-check). So for such configurations the free word, column 1 at the free white phase, eventually lies in X_B: the union, over unlabelled cyclic SCCs, of the words read along paths inside one SCC.

This is PE-1.2's argument, slightly sharpened. PE-1.2 took the language of a forward closure, which includes transient paths and labelled cycles. Taking only the unlabelled SCCs is smaller, and it is still sound. Status: PROOF-SKETCH, offered for GPT's carrying read.

**Monotonicity (PROOF-SKETCH, hand, Local).** Let S be an unlabelled SCC at width B + 1, and let π drop column B + 1.
- π sends edges to edges: the old top column becomes the free input.
- So π(S) lies in one SCC S′ at width B, and every cycle of S projects to a closed walk of S′. Hence the gcd g′ of S′ divides the gcd g of S.
- Suppose S′ were labelled, and take two vertices of S with the same level mod g. Every path between them has length ≡ 0 (mod g), hence ≡ 0 (mod g′). Their images then have equal level mod g′ and the same column-1 reading. So S would be labelled too.
- Hence S′ is unlabelled, and X_(B+1) ⊆ X_B.

The data agree: every count at every common length is non-increasing in B (`summarize.py`: PASS).

## Replays and controls (COMPUTED, Local M5; my code, a different method from PE's closure and peel)

| Check | Prediction | Result |
|---|---|---|
| Word 01, B = 5 (the kit's `col1Forbidden`) | contains 11, 00000, 100101, 10010001 | exactly those four |
| 001, B = 14, minimal forbidden words to length 14 | PE-1.2's eleven | exactly the eleven: 010 101 1001 11111 000000 0000111 01110001 11100000 1110001110 00000110001110 11100011000111 |
| 001, B = 16, counts at lengths 8, 10, 12, 14 | at most 27, 40, 61, 96 | 23, 34, 53, 82; the shorter word 01110 is now forbidden (so 1-runs are 2 or 4), and all eleven stay forbidden |
| 011, B = 20 | one unlabelled SCC; 00, 010, 01110, 011110, 1^15 forbidden; count at length 16 at most 180 | one SCC of 40,639 states (PE-1.2's number); words as predicted; count **183, prediction MISSED**: PE-1.2's 180 is at b = 22, and a narrower strip allows more |
| 011, B = 22 (the corrected comparison) | counts 19, 35, 62, 109, 180 at 8..16; the fourteen words | exactly, both |
| 0011, B = 13 and 17 (PE-2.1) | seven words at 13, all eight at 17 | yes; 10110 first appears at 17 |
| Period 4 against rule30-open's `channel-ladder.md` (exact growth per period at W = 30: 0001 1.2295, 0011 1.2274, 0111 1.1827) | my estimates at B = 22 at least 1.20, 1.20, 1.15; 0001's count still falling | 1.311, 1.276, 1.242, each above their W = 30 value, as monotonicity requires; 0001's count at length 26: 6536, 5562, 5015 at B = 18, 20, 22 |
| Growth estimates at longer words | each lower than at length 18, and falling with B | **partly REFUTED**: single-length ratios wobble at about 0.001 (001 B = 18 and 22, 011 B = 16). The six-step estimates below are used instead; the counts themselves are monotone |

Also consistent with an outside Lean result: 1001 first becomes forbidden at B = 13 (the eleven words at B = 14). rule30-open's `ThreeRuns` proves 010, 101 and 1001 with a window of columns 1..13, for every right half.

## The ladder (COMPUTED; growth = (c(n)/c(n−6))^(1/6) at the longest length run, per reading)

| B | 001: c(24), growth, bits per tick | 011: c(24), growth, bits per tick |
|---:|---|---|
| 14 | 775, 1.232, 0.100 | (length 18 only: 1.302) |
| 16 | 555, 1.209, 0.091 | 1516, 1.284, 0.120 |
| 18 | 443, 1.199, 0.087 | 1281, 1.267, 0.114 |
| 20 | 411, 1.187, 0.082 | 1176, 1.255, 0.109 |
| 22 | 397, 1.190, 0.084 | 1088, 1.243, 0.105 |

The estimators are finite-length ratios, not Perron roots, and they need not be monotone even though the counts are. Period 4 at B = 22 (lengths 20 to 26): 0001 1.311, 0011 1.276, 0111 1.242 per reading. The full table is the `summarize.py` output.

**Smallest widths for each word set** (useful for a Lean certificate):
- 001:
  - 010 and 101 at B = 6 (192 vertices).
  - Add 11111 and 000000 at B = 10 (3,072): 18 words to length 18.
  - 1001 at B = 13, and the eleven at B = 14 (49,152).
- 011:
  - 00 at B = 6 (192).
  - 00 and 011110 at B = 7 (384).
  - 00, 010, 01110 and 011110 at B = 17 (393,216).
  - 1^15 at B = 18.

## Prior art

Record searched:
- `record_find.py` for C3g001, C3g011, C3X_F, 10110, 0111110, ConstrainedLeft001 and ThreeRuns, with the kit main `12ddd22e` index and the portal index of 14:37Z. Only our own SW-02 records hit; no kit or portal statement.
- Kit main `1487f31`: module docs of `Rule30PeriodFourSkeleton`, `Rule30EtherThreeSkeleton`, `Rule30EtherThreeLeft` and `Rule30PeriodTwoLanguage`.
- `rule30-open` at `f877f5af` (HEAD unchanged; read by raw URL, no clone): `CATALOG.md`, `ThreeRuns.lean` (docstring), `findings/columns/reading-constraints.md`, `negative-results/columns/constrained-left-halves.md` and `negative-results/columns/channel-ladder.md`.
- SW-02's PE-1 report and its self-check SKM-PE-1-2, and GPT's Block 6 carry of PE-2.1.

| Item | Verdict |
|---|---|
| The method: bad-class strip certificates, and a path-language check for period 2 | **KNOWN**: kit `Cert.sound_bad` (any period) and `Rule30PeriodTwoLanguage.occurs`/`no_pattern` (period 2 only) |
| 001: column 1 avoids 010, 101, 1001, for every right half | **KNOWN**: `ThreeRuns` (Lean) |
| 001: runs at most 4 and 5 (11111, 000000), and the longer words | **NOT FOUND**: rule30-open lists these run lengths as "sampled, not forced". They need the left-finite hypothesis (masked Jen) and appear here at B = 10 |
| C3s001 ⇒ C3r001 ⇒ C3g001, with C3r001 excluding 001 tails | **KNOWN** for C3r001 (`ConstrainedLeft001`, Lean); C3g001 is a further weakening (PE-1.2), not in rule30-open |
| 011: the trap words 00, 010, 01110, 011110 | **KNOWN** as computation in rule30-open: entry "not forced" for every right half; 00 forced unless the readings are eventually white, which masked Jen excludes, argued on paper; no Lean. Forced for left-finite configurations here at B = 17, and 00 alone already at B = 6 |
| 011: 1^15 and nine longer words (C3g011) | **NOT FOUND** outside SW-02 |
| Period 4: the channel entropies | **KNOWN** (`channel-ladder.md`, to W = 30); replayed here as a control. PE-2.1's explicit eight-word list for 0011 was not found there |
| "No finite left game closes", and the entropy drop for constrained left statements | **KNOWN** (`constrained-left-halves.md`). The in-kind answer above is their argument; this work adds the period-3 ladder to width 22 and the monotonicity in B |

## What this changes, and the next step

The block's question has an answer. Wider strips weaken C3 in degree, by a measured and decelerating amount for 001, and only restate it in kind. The right half's language is now pinned down near its limit at small widths. Whatever proves C3, or C3g, must use left finiteness beyond any finite strip test.

**Step 2 (proposed): a small Lean module, the period-3 counterpart of `Rule30PeriodTwoLanguage`.**
- *Generalization.* Extend `occurs`/`no_pattern` from period 2 to period P. GPT's self-check (SKM-PE-1-2 f) notes that this is new work.
- *001, B = 10 (3,072 vertices).* For a 001 tail in a left-finite configuration, the free word eventually has 1-runs of length 2..4 and 0-runs of length 2..5. Only the upper bounds are new. The lower bounds (010, 101) are `ThreeRuns`' result, which already holds for every right half.
- *011, B = 7 (384 vertices).* The free word eventually avoids 00 and 011110.
- *Reductions.* C3g001 and C3r011 (C3w w011 restricted to those words) exclude the tails.
- *Packaging.* All of this is small enough for `decide`. The B = 14 and 17 versions (49,152 and 393,216 vertices) are a separate feasibility question.
- First step: a pilot with the 011 B = 6 certificate (192 vertices), to fix the encoding.

**Research alternative.** The 011 ladder past B = 22 decides whether its decline continues. B = 24 to 26 means 50 to 200 million vertices, so it would be an Intel job if ever run.

**Carrying read requested (GPT, low urgency).** It covers two steps:
- (1) The reduction: for a left-finite configuration the walk ends in an unlabelled SCC (masked Jen, with its exact hypotheses).
- (2) The monotonicity lemma.

The tables are machine replays and need no read.

## Resources

Three runs under `run_capped.py`, each frozen before it ran: CPU 900, wall 1200, RSS 4096 MiB tree cap, swap growth 4096 MiB, free floor 1024 MiB, at most 4 processes.
- Aggregate CPU 0.36, 0.87 and 2.38 s; wall 0.53, 1.05 and 2.63 s.
- Peak sampled tree RSS 490 MB. The largest single process (B = 22, P = 4) peaked at 628 MB.
- Minimum free memory 5,428 MiB, with zero swap growth.
- `ladder.out` SHA256 `dbbdd24e1a636107…`, `lang.c` `13f1eec4601d8459…`. The data are these small text outputs, kept in git.

My own pull: the Lean module of step 2. It turns the period-3 skeleton from computation into theorems at small widths, and the 001 run bounds are the one new forced fact here.

## Step 2: the period-3 languages in Lean (L1601, 19:41 UTC)

**Done, at the owner's word ("Carrying read first, then block 9 lean step").** New kit module [`Rule30PeriodThreeLanguage`](wolfram-agents/submissions/period-three-language/Rule30PeriodThreeLanguage.lean), 297 lines, SHA256 `4fcbb7f84b5447e8…`.
- Built at kit main `1487f31` in a local kit branch `b9-period3` (commit `7dcd8f1`, not pushed).
- `lake build` passes with no warnings, in 12 s at 1.6 GB peak on the M5.
- Axioms: `propext`, `Classical.choice`, `Quot.sound`.

**What it proves.** All statements are about the seed, as the kit's `Cert.sound_bad` is.
- `occurs3`, `no_pattern3`: the kit's `Rule30PeriodTwoLanguage` check, extended to period 3. Subset simulation over bitmasks of strips, three ticks per letter, staying in the bad class at every tick. The soundness proof is general in the reading phase R.
- `col1_011` (certificate `K011w7`: 384 strip states, bad class 136): if the center is `011`-periodic from T, column 1 at phase 0 eventually never spells 00, 011110, 111010, 0101010, 0101110, 01011010, 11101110 or 111011010.
- `free_bits_011`: so the free bits (column −1 at phase 0, by `col_m1_011`) never spell 11 or 100001, among others.
- `col1_001` (certificate `K001w10`: 3,072 states, bad class 553): if the center is `001`-periodic from T, column 1 at phase 1 eventually never spells 010, 101, 11111, 000000, 100111, 111001, 00000111, 01110001, 10011001 or 11100000.
  - So its black runs have length 2..4 and its white runs 2..5.
- `free_bits_001`: the same for column −1, by `col_m1_001_skeleton`, as complements: white runs 2..4, black runs 2..5.

**Checks.**
- Positive controls by `decide`: each bad class contains real paths. 11 and 0110111 occur beside 011; 11, 0011 and 110011 occur beside 001. Without these, an empty bad class would make every word "forbidden".
- The certificates were generated and checked first in Python against the kit's own conditions ([`gen_cert3.py`](../tests/probes/swarm/sw02/block9/gen_cert3.py), [output](../tests/probes/swarm/sw02/block9/gen_cert3.out)). Their words are exactly `lang.c`'s.
- **Six mutants, all rejected** ([`mutate.py`](../tests/probes/swarm/sw02/block9/mutate.py), prediction in its header; [output](../tests/probes/swarm/sw02/block9/mutate.out)), each at the line it targets:
  - 11 added to the 011 list, and 1001 added to the 001 list. 1001 is forbidden only from width 13, which is `ThreeRuns`' width.
  - The wrong center word, the wrong bad rank, and one corrupted rank.
  - `col1_001` stated at phase 2.

**Prior art.** No period-3 language module in kit main `1487f31` (source grep), its open PRs or the portal index (`record_find`).
- `rule30-open`'s `ThreeRuns` proves 010, 101 and 1001 for every right half, a larger population.
- New here: the upper bounds 11111 and 000000 and the longer 001 words, and everything for 011, in Lean. rule30-open has no Lean for 011, and lists the 001 upper bounds as "sampled, not forced".

**Not done.**
- The left reduction: a `C3w w011` restricted to free bits avoiding 11 and 100001, and the 001 analogue below `C3s001`, each excluding its tail. This is the counterpart of rule30-open's `ConstrainedLeft001`.
- Packaging. The kit's `Check.lean`, the portal form, the catalogue row and the import line are not made. Nothing is pushed or posted.

## Step 3: the left reductions (L1602, 19:49 UTC)

**Done, at the owner's word ("011 left reduction").** The module (now 420 lines, SHA256 `71ac7331952cf40e…`; kit branch commit `8b816f1`, not pushed) adds:
- **`C3r011`** (open): `C3w w011` with the left configuration's free bits restricted to the right half's language. No finitely supported left configuration, driven by the effective boundary 010, keeps column −1 on (*, 0, 1) for all large times while its phase-0 bits never spell a complement of a `col1Forbidden011` word. The complements, checked by `decide`, are 11, 100001, 000101, 1010101, 1010001, 10100101, 00010001 and 000100101.
  - `C3r011_of_C3w`: `C3w w011` ⇒ `C3r011`.
  - **`not_eventually_011_of_C3r`: `C3r011` excludes 011^∞ as a tail of the center column, for every transient.**
  - The proof takes the seed's own left half at T, as `not_eventually_011_of_C3w` does, and gets the extra free-bit clause from `free_bits_011` through `cell_eq_L_effective`.
- **`C3g001`** (open): `C3s001` restricted the same way at phase 1. The free bits have white runs 2..4 and black runs 2..5, and avoid four longer words.
  - `C3g001_of_C3s`, and **`not_eventually_001_of_C3g`**.
- **`no_eventual_period_three_of_C3g`**: `C3g001` and `C3r011` together exclude an eventually 3-periodic center (via `normalize_period_three`).

**Checks.**
- Built at kit `1487f31` with no warnings. The reductions use `propext`, `Classical.choice` and `Quot.sound`; the implications from C3w and C3s use `propext` only.
- **All nine mutants are rejected** ([output](../tests/probes/swarm/sw02/block9/mutate.out)). The three new ones, with the prediction written in `mutate.py` before their run, each break their reduction proof:
  - dropping the complement in `C3r011`'s free-bit clause;
  - reading `C3r011`'s free bits at phase 1;
  - reading `C3g001`'s at phase 0.

**Prior art and what is new.**
- rule30-open's `ConstrainedLeft001` (`c3r_of_c3s`, `not_eventually_001_of_C3r`) is the 001 pattern with `ThreeRuns`' language: free-bit 0-runs ≥ 2 and 1-runs ≥ 3. Our `C3g001` is incomparable with their `C3r001`. Ours bounds runs above and adds longer words, but it lacks 1001, which needs strip width 13.
- **For 011 nothing comparable exists in Lean**: rule30-open's `constrained-left-halves.md` treats 011 by computation only. `C3r011` and its reduction are new.
- A width-14 version of the 001 certificate (49,152 strip states, all eleven of PE-1.2's words, 1001 included) would make `C3g001` imply both versions. Whether it fits the kit's per-module time limit is untested.

**What it changes.**
- Period 3 now reduces in Lean to two left statements, each over a free word of positive but reduced entropy: about 0.084 bit per tick beside 001 at width 22, and 0.105 beside 011.
- The width-7 and width-10 languages used here are larger than those, so these Lean statements are not yet the thinnest available.
- As step 1 found, the reduction changes C3 in degree, not in kind.
