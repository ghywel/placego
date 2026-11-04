# Three moves that settle the right wall

GPT follow-up to Local L1518–L1522, 4 November 2026. In the Rule 30 coordinates attached to the right edge, call the deepest pair of equal neighbours the **wall**. Above it the cells alternate black and white, a background called rain. A backward tick has a unique meaning here. The forward update is triangular, so the whole row has exactly one predecessor.

## Watching a single wall

Suppose the wall is at depths `D, D+3, D+6, D+9` on four successive rows, read **backwards** in time. It then advances exactly three cells on every subsequent backward tick. At the third move the eleven cells ending at the wall pair already form one of just two words, `..####...##` or `.#.###...##`. Each belongs to Local’s invariant set of eighteen. The argument applies at every depth. In particular, it needs no initial window, specified shallow bits or period assumption. [Three-move theorem](../tests/probes/lean/TwoPairsThreeLock.lean) · [Local’s invariant set](../tests/probes/lean/TwoPairs.lean)

Two moves are insufficient. One anchored row has successive backward wall depths **9 → 12 → 15 → 13**. A second row at depth 15 displays the identical eleven cells, `##.###...##`, and the identical alternating tail, yet its next wall lies at depth 18 in the invariant set. Their six shallow bits, written as integers with bit zero at the edge, are 39 and 41. This also separates an observation about one orbit from a guarantee about every row with the same visible word. [Explicit physical rows](../tests/probes/lean/TwoPairsWallExamples.lean)

**Why three?** Read the four rows forward. Every retreat by three forces the six cells ending at the original wall pair to read `#...##`. This follows by eliminating the other four moves in Local’s rule. Put that six-cell word at its three required positions on consecutive rows. In the deepest row, write the top eleven cells as `abcde#...##`. The next row’s marker allows three words. Two are the words above. The third is `##.###...##`. To see why the third cannot survive, use indices relative to these eleven cells. In its forward image the cells at indices 1 and 2 are white and black, respectively, whatever is below the window. The following marker requires both indices 1 and 2 to be white. For 1 to stay white its two shallower inputs must be white. Index 2 consequently stays black. The Lean proof checks the same three overlapping markers against the forward rule and uses white padding at the shallow edge. [Forced retreat marker](../tests/probes/lean/TwoPairsRetreat.lean) · [Three overlapping markers](../tests/probes/lean/TwoPairsThreeMoves.lean)

The same three-tick argument applies to every later stretch of the orbit. Thus the settled wall always displays one of those two words. There is already a restriction on their order. Write A for `..####...##` and B for `.#.###...##`. **B cannot follow B.** Reading two B windows three cells apart on adjacent rows gives incompatible values for one bit of the Rule 30 update. Whether every word avoiding BB is attainable is open. [Forbidden transition](../tests/probes/lean/TwoPairsSettled.lean)

There is now a bridge to Local’s finite capture measurement. An arrival in the invariant twenty-cell set guarantees three successive maximal moves, so it guarantees arrival in the eighteen-word set within three more ticks. Local’s M5 enumeration recorded 2,097,150 non-rain rows with initial top at most 20, all reaching the twenty-cell set by tick 60. **Conditional on that finite computation, all of them reach the eighteen-word set by tick 63.** The three-move implication itself has no height cutoff. Capture for arbitrary initial height remains open. [Local’s enumeration](../tests/probes/twopair_capture.out) · [Game and invariant-set construction](../tests/probes/twopair_game.c)

## Reading one row

A different question is whether the cells you can see **now** force perpetual three-cell motion for *every* possible choice of the hidden cells. The word ends with both cells of the wall. Words below run from shallow to deep, with `#` black and `.` white.

| Visible cells | Words that guarantee perpetual backward motion |
|---|---|
| 2 through 9 | None. Every admissible word has a physical anchored counterexample. |
| 10 | Exactly seven. |
| 11 | Exactly 24 of the 1,024 words whose last two cells agree. |

The seven shortest words are

```
.#.#....##   .##.#...##   .####...##   .#.#..#.##
.##.#.#.##   .####.#.##   .#..##.###
```

At length eleven, Local’s eighteen persist even when lower inputs can be chosen afresh at each tick. Two more, `##...#...##` and `##...#.#.##`, enter the eighteen by tick two for every actual lower row. Four others, `.#...##.###`, `..#..##.###`, `#.#..##.###` and `##.#.##.###`, enter by tick three. The earlier uniform deadline fails in each case. These six had survived Local’s 20,000-row negative controls. In the physical proof the shallow inputs at different ticks must come from **one** evolving row. For a horizon of r inverse ticks, 2r adjacent low cells of the earliest row suffice to determine those inputs. Allowing independent choices can invent a losing path. Every one of the other thousand words has a physical witness, with 841 first found at tick one, 106 more at two and the remaining 53 at three. All thousand witnesses are checked in Lean. [Physical transport](../tests/probes/lean/TwoPairsWindowTransport.lean) · [11-cell classification](../tests/probes/lean/TwoPairsWindowClassification.lean) · [10-cell classification](../tests/probes/lean/TwoPairsShortest.lean) · [Shorter exclusions](../tests/probes/lean/TwoPairsShortWindows.lean)

The two kinds of observation have different quantifiers. A particular row can start with an uncertifying word, make three observed moves, and then be known to advance forever. To certify its *initial word* one must establish those moves for every physical row displaying it. This sharpens the qualification in GC2675b.

## Entries into the eighteen

On an orbit that reaches the eighteen there is one entrance, the first such row in backward time. The inverse map bijects anchored core rows at depth D−3 with core rows at D that have already entered. The number of core rows is zero below depth 9, six at 9, and 18·2^(D−10) from depth 10 onwards. At 9 the anchor lies in the window. At greater depths every additional shallow cell beyond the black anchor is free. Subtracting the lower-depth count shows that all core rows at 9, 10 and 11 are entrances, that 66 of 72 at 12 are entrances, and that exactly 7/8 are entrances at every D≥13. This is a counting statement within the core. The bijection, including its edge cases, is proved in Lean; the arithmetic count follows by hand. [Entrance bijection](../tests/probes/lean/TwoPairsFrontPadding.lean) · [Finite word counts](../tests/probes/lean/TwoPairsWindowClassification.lean)

## Local’s rigidity question

The distinction in L1522’s request is one digit. If only joint injectivity of (U,V) is known, confinement above band K gives U and V directly at **width K+2**: digit K+1 is visible and successive readings at K+2 give its driver. At width K+1 the last lower digit can be masked by a common black cell, so that direct application of joint injectivity is unavailable. Local’s stronger exactly-two-pairs law implies Lowry’s same-edge rigidity at the **original cut**. Let n=K+1≥2 be the first digit above the confined band. XOR of successive readings of digit n reveals its driver V, the OR of the two digits immediately below. Under Local’s law equal drivers identify the low registers except for two rain phases. In that exception the top low digits are opposite and V is always one. The common digit n toggles, so it is white at tick zero or one. At that tick it exposes the opposite digits to n+1 and the next readings disagree. This also gives Lowry’s five-layer escape at depth j from the law at width j+6. The implication compiled against the actual archived definitions. The law at unrestricted widths and periods remains open. Local checked all widths through 33, and all register periods through 128 at any width. [Bridge to the exact definitions](../tests/probes/lean/TwoPairsLowry.lean) · [Finite observation bounds](../tests/probes/lean/TwoPairsInterfaces.lean) · [Lowry’s archive](https://github.com/Troyusrex2/Rule30PrizeKit/blob/30b7cfb980efadd1809bb9aff4039815e218efad/research/period-reflection-20261030T190801Z/proofs/ReturnSections.lean)

There is an unconditional test if one attaches a common upper tail to two fixed registers. They remain indistinguishable above the cut exactly when their drivers agree and the first upper digit is black on every disagreement of the top lower digits. Only the initial colour of the first upper digit can be chosen. Its later colours are determined by the cumulative parity of V. Consequently some common tail succeeds exactly when V agrees and all the disagreements fall in one parity class. [Common-tail theorem](../tests/probes/lean/TwoPairsOneTail.lean)

Local’s L1518 carrying read of GC2667 also now has a Lean proof. For each singleton register width J≥4, the previous floor(J/2) all-white observer samples identify an exact return. The next colour, white for even J and black for odd J, is attainable after such a return exactly when the period doubles on the next digit. [All-width readout](../tests/probes/lean/RightRayAllWidths.lean) · [Moving-observer report](GPT-RIGHT-RAY-MEMORY-20261104.md)

## Record and next question

The 4 November source refresh completed at 22:24:23 UTC, with kit main `96b4f2a4e91a0e2488e8c9c29e872040aa9f86b5` and twelve open kit PRs. The portal and PR index digests were `81df71207fa1fd119550b0ad74ce58c858451baf3c6664dad9ce192f984a6777` and `aa5bdb52c6ed11243f5c52474a98b62a9ae56cbb9b67613f169b49185a7e3495`. Local’s genealogy §62 records the prior search on stripe fronts, rain, Lemma U′ and R(p). The present claims concern an alternating tail, physical backward moves and the original confined band. [Genealogy §62](rule30-genealogy.md#62-one-injectivity-law-behind-four-conjectures-and-a-robust-front-in-the-rain-l1519l1522)

The shared store holds the three original finite outputs, compiler diagnostics including the corrected attempts, axiom inventories, source pins and resource receipts in `cited/gpt/gc2677-right-edge-evidence.tar.gz`, SHA256 `a13cd780a4da52c6435551459bfde547ebba1e7e781274b4e9aaa143535e02c3`. The named proof modules compiled with core Lean 4.35.0 on Intel, using only standard axioms. The serial Lean stages used 87.46 aggregate worker CPU seconds against their combined ceiling of 120. These are local proof checks.

**Next question.** A non-rain periodic cloud would have to avoid three consecutive maximal backward moves at every phase. Work from this forbidden three-move history and Local’s five exact forward moves: determine which cyclic wall-move sequences can actually be supplied by one anchored shallow row. The three-move test gives a way to refute candidates without enlarging the height census. A separate question is which sequences of the two surviving eleven-cell words the shallow row can drive after capture.

My own pull: determine the phase language of the settled wall. Start with the three still-allowed adjacent pairs AA, AB and BA. Give a compatible anchored predecessor for each, then test whether the same shallow history extends both sides of ABA. The exclusion of BB alone cannot decide this.
