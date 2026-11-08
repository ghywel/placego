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
