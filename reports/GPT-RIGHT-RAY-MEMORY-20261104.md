# What a moving observer can read from the right side of Rule 30

Owner-requested GPT block, 4 November 2026, GC2657 onward. Cloud separately owns the forced front on the four left strips.

Start with a finite row and put its rightmost black cell at position zero. At tick `t` the right edge is at position `t`. Watch position `ceil(t/2)`. This moves into new territory at half the speed of the edge. In edge coordinates the observer reads wheel 0 twice, wheel 1 twice, wheel 2 twice, and so on. Write the two readings of wheel `j` as a pair. We ask which finite words can follow a given history, allowing every finite seed that gave that history.

**Result.** There is no finite-state rule that reads the first bit of each pair and always predicts the second. Even the histories obtained by starting the observer at different times on the same single-black-cell evolution require unboundedly many states. For the family of all finite anchored starts, there is an exact description of what information matters. Two histories admit the same finite futures precisely when two time sequences agree. The first sequence reads the last cell already passed. The second records whether either of the last two cells already passed is black.

## A delayed black cell on the actual singleton

Write the right-edge row from low to high depth as an odd integer. Its update is `Φ(x) = x XOR (2x OR 4x)`. Each new bit is its old value XOR a function of the two shallower bits. Every finite low register is therefore a permutation, with period a power of two. These are known right-edge facts. In particular, at the first visit to a depth, all lower initial bits can be recovered from earlier first visits. The current first reading determines the one remaining initial bit. The second reading is then forced. Through wheel `d−1` there are exactly `2^(d−1)` histories for `d≥1`. [Kit TFunctionCycles](https://github.com/WolframInstitute/Rule30PrizeKit/blob/2b6233857e5b0828333657e3499464438baf3ccb/equivalents/Rule30Equivalents/TFunctionCycles.lean)

Here is a concrete experiment with just one physical evolution. Launch the observer at the right edge of the singleton at the indicated absolute tick. In all four experiments advance the observer another 18 ticks and begin reading at wheel 9. A pair `01` means that the first observation was white and the repeat was black. The 12-bit singleton register returns after 64 ticks.

| Launch tick on the singleton | Pairs beginning at wheel 9 |
|---:|---|
| 50 | `01` |
| 48 | `00 01` |
| 47 | `00 00 01` |
| 46 | `00 00 00` |

This works at arbitrarily large depths. A nonzero finite row whose highest black bit is at `b` has its highest black bit at `b+2` one tick later, and the next bit down is black as well. At the common age `6m`, wheel `3m`, put the singleton register at an early phase whose leading cells first cross the observer on the repeat of a chosen pair `i<m`. Concretely take early tick `floor((3m−3i−1)/2)`. Everything the observer samples in this interval is white up to that repeat. Register periodicity supplies an actual nonnegative launch time with exactly that early snapshot on the required finite interval. One further phase stays white through all `m` pairs.

There are now `m+1` distinguishable histories at the same elapsed time. The one with the earlier crossing rules out the longer white continuation: prescribing the intervening white first readings fixes the next repeat for every seed with the same past. The later crossing admits that continuation. The argument even restricts the possible continuations to phases of the singleton. It establishes nonregularity of the language of **prefixes from the marked launch**. Predicting one fixed launch or recognizing the shift closure of all factors are different questions. [Finite-row theorem](../tests/probes/lean/RightRayDelay.lean) · [Singleton-phase theorem](../tests/probes/lean/RightRaySeedPhases.lean) · [Follower sets and finite rooted presentations](https://arxiv.org/abs/2101.02441)

## A white run identifies a spatial interval

Let `n` be the wheel at the start of a block, and let `m≥1`. In the row at that starting tick the following are equivalent.

| Observations required to be white | Cells that must all be white at the start, inclusive |
|---|---|
| `m` complete pairs, starting with a first reading | `[n−3m+1, n+m−1]`, a run of `4m−1` cells |
| `2m+1` readings, starting with a repeat | `[n−3m, n+m]`, a run of `4m+1` cells |

The implication back to the spatial row uses a feature of Rule 30. If the new row is white on an interval, then on that interval each old bit equals the OR of its two shallower neighbours. One old white witness in the interval forces both neighbours white and pins the whole predecessor interval. The last repeated observation gives the first witness. Each earlier observation lies within the interval already exposed. Iterating backwards recovers the whole bottom of the cone. The forward implication is ordinary locality. This specializes the carried white-witness argument of GC2598/L1487. [Earlier cylinder proof](GPT-CYLINDER-HISTORY-TRANSFER-20261103.md) · [White-path theorem](../tests/probes/lean/RightRayWhiteCone.lean) · [Exact half-speed intervals](../tests/probes/lean/RightRayProbe.lean)

For example, no finite seed with its rightmost cell black can supply more than `floor(n/3)` consecutive fully white pairs starting at wheel `n`: the next required interval would include the anchor. This ceiling is sharp over finite seeds, even over singleton launch phases, since a low register can be placed at the singleton’s initial phase. In particular the ray has infinitely many black readings for **each** anchored seed, including the singleton launched at tick zero. This does not supply a density.

## The exact information at a cut

Cut just before the first reading at wheel `d≥2`, when the physical clock reads `2d`. The past fixes the low `d` bits of that row. They evolve autonomously. At subsequent tick `t`, measured from this cut, write

```
U(t) = bit d−1
V(t) = (bit d−1) OR (bit d−2).
```

The pair has only three possible values. The old three-symbol boundary word and its sufficiency are prior art. The result here is that the possible observations on **one drifting ray** recover the entire boundary word, even when the two cuts being compared have different depths. Times are aligned to the respective cuts. [PR61’s boundary-word proof](https://github.com/Troyusrex2/Rule30PrizeKit/blob/30b7cfb980efadd1809bb9aff4039815e218efad/research/period-reflection-20261030T190801Z/proofs/WordBoundary.lean) · [Exact moving-ray criterion](../tests/probes/lean/RightRayLanguage.lean)

**Why the two words suffice.** At the first new depth the update XORs in `V(t)`. One cell farther in, it uses the OR of the new bit and `U(t)`. All remaining updates use only cells above the cut. When the two words agree, copying the same higher initial bits therefore copies the entire future above the cut. For finite histories and finite continuations the required high bits at the cut are attainable. Triangular inversion chooses their initial values one at a time while preserving the observed past, after which all farther initial cells may be set white.

**Why the ray recovers both words.** Ask whether *some* continuation can contain a white block at a specified later offset. Its earlier symbols are free. For `k=1,2`, choose the starting wheel and block length so that the bottom interval in the table begins at `d−k`. The prescribed low part is then white exactly when the last `k` old cells are white. Every other cell required by the block can be set white by choosing a finite upper completion. Thus one choice of `k` tests `U=0`, and the other tests `V=0`.

For a fixed `k` the two starting offsets from the cut are `2(3m−k−1)` and `2(3m−k)+1`. One is even and one odd. Increasing `m` advances either by six ticks. Modulo a common dyadic register period `P`, this visits every phase of the respective parity because 3 is invertible modulo `P/2`. Equal future languages consequently give equal movies at every tick. The choices of upper completion may vary with the query. This is an inference from all possible finite futures. [Steering a finite completion](../tests/probes/lean/RightRayFollowerProbe.lean) · [Phase coverage for each probe](../tests/probes/lean/RightRayProbeTime.lean)

This argument gives a finite distinguishing length. If the movies have common period `P≥2` and differ, choose `1≤m≤P/2` in the parity family that tests the differing phase. The wait and queried block together require at most `4P` samples. For `P=1` the even query with `m=1` uses at most four. This bound is a hand consequence of the two probe offsets.

One can also use the words as the predictor’s state. If `a` is the next first reading, set `Z(0)=a` and `Z(t+1)=Z(t) XOR V(t)`. The next repeat is `Z(1)`. At the next cut the two words are `Z(t+2)` and `Z(t+2) OR U(t+2)`. Equal word pairs represent the same predictions for every possible future sequence of first readings. No two different pairs can be merged.

## What the check distinguishes

| Depth at the cut | Odd low states | Classes after the frozen short horizon | Distinct top-cell movies alone | Distinct full boundary movies |
|---:|---:|---:|---:|---:|
| 8 | 128 | 125 after 8 pairs | 126 | 128 |
| 10 | 512 | 390 after 7 pairs | 510 | 512 |

The short computation compared both child responses recursively and cross-checked the implementation by direct enumeration of input words at smaller widths. The complete test compared phase-aligned words over a full dyadic return. A separate local truth table checked the white-interval identity on every odd snapshot at the 27 prescribed depth/length combinations. At both reported depths every pair of different low states can eventually be distinguished. A short horizon can hide a real difference. [Finite-horizon check](../tests/probes/right_ray_memory.py) · [Complete-register check](../tests/probes/right_ray_boundary.py)

At width three this distinction is visible by hand. The low registers 1 and 3 alternate respectively with 7 and 5. Their top cells have the same word `01`. The OR of the top two starts white in the first register and black in the second. Giving both the same white first reading therefore yields different repeats immediately.

The kit’s fixed-column experiment allows every external left driver and compares the resulting responses. Its known complete statistic consists of the same two words, after reversing the low register. The new criterion therefore identifies its equivalence relation with the moving observer’s finite future languages. The three-letter word itself and the kit’s terminal reductions are earlier results. The fixed-depth question of whether *every* different odd register can be distinguished is equivalent to the existing same-edge rigidity conjecture. Our two finite counts resolve only their stated depths. [Compiled bridge](../tests/probes/lean/RightRayControlledBridge.lean) · [Kit’s controlled responses](https://github.com/WolframInstitute/Rule30PrizeKit/blob/2b6233857e5b0828333657e3499464438baf3ccb/lean/Ruliology/CellularAutomata/Rule30ControlledResponse.lean) · [Earlier rigidity equivalence](https://github.com/Troyusrex2/Rule30PrizeKit/blob/30b7cfb980efadd1809bb9aff4039815e218efad/research/period-reflection-20261030T190801Z/proofs/ReturnSections.lean)

## A clock test on the single black cell

Start the observer at any phase of the actual single-seed evolution. At an even-tick cut at wheel `3m`, with `m≥1`, **the next `2m` readings are white exactly when the low `4m` bits have returned to the singleton**. Here the interval exposed by the ray is exactly `[1,4m−1]`, and bit zero is always black. There is no ensemble of alternative seeds in this test.

Under that condition, consider the very next reading, at depth `4m`. From the initial one-cell row, the highest black bit at local tick `2m` is exactly `4m`. The cut row agrees on every lower bit, and a change to its bit `4m` passes through at that bit under every iterate. Thus the new reading is white exactly when bit `4m` was black at the cut. [Lean readout](../tests/probes/lean/RightRaySeedReadout.lean)

Write `P` for the least positive return time of the low `4m` bits. At multiples of `P` the next bit is either always zero or alternates. The kit's known period-lift law identifies the second case with a doubled period on `4m+1` bits. An extra white reading is therefore attainable at **some singleton launch** exactly in the doubling case. The entire `2m+2`-white word is impossible because its bottom interval would include the black anchor. The longest white run at this cut across launch phases is consequently `2m` or `2m+1`. This is a way to read an individual doubling bit from a moving observation. The frequency of doublings as the depth grows remains open. [Formal extra-white criterion](../tests/probes/lean/RightRaySeedReadoutDoubles.lean) · [Kit lift parity](https://github.com/WolframInstitute/Rule30PrizeKit/blob/2b6233857e5b0828333657e3499464438baf3ccb/equivalents/Rule30Equivalents/TFunctionCycles.lean)

For a small example take `m=1`. The singleton’s low four bits return after four ticks. Its low five bits at tick four are `10001`, so the larger clock doubles. At wheel 3 the launches `s=2` and `s=6` both give the two compulsory whites. Only the second launch gives a third consecutive white. More generally, over all ordinary launch times in a common return cycle, the `2m`-white event has frequency `1/P`. When the larger clock doubles, exactly half of those returns give the extra white. These are frequencies over launches at a *fixed* depth.

## A candidate readout at every depth

**PROOF-SKETCH, GC2667.** The geometry suggests a single recipe for every new bit `J≥4`. Let `h=floor(J/2)` and look at the `h` samples immediately *before* the first reading of wheel `J`, so the window begins at observer tick `2J−h`. Its last two observations both see wheel `J−1`. The white-path theorem exposes the interval `[J−2h+1,J−1]` in the row at the start of the window. For even `J` this begins at 1. For odd `J` it begins at 2. On the singleton, bits 1 and 2 start white and toggle together forever: bit 1 is toggled by the black anchor, and the toggle of bit 2 is bit 1 OR the black anchor. The observed white bit at depth 2 therefore supplies the missing white bit at depth 1. An even absolute starting tick is necessary for such a block and follows from the observations themselves. The all-white window now certifies a return of all the low `J` bits in either case.

For an initial singleton the largest occupied depth after `h` ticks is exactly `2h`. Starting instead from a return on the low `J` bits, triangularity transmits any difference in bit `J` to the new reading. Thus on the return, look for **white at even J** and **black at odd J**. Either color in its stated parity means the return had a black bit just above the prefix. Across singleton launches this color occurs iff the clock doubles there. No knowledge of the absolute launch tick is needed for this singleton deduction. The synchronized low pair is essential to this argument at odd widths. A common finite-register period lets the chosen return be taken after the window start. This all-width deduction is awaiting a carrying read; the separate compiled theorem above covers `J=4m`.

## Evidence and next block

Intel Lean 4.35.0 compiled the universal and singleton-phase state lower bounds, both white-block intervals, the complete boundary characterization, its statement for histories of genuinely finite anchored seeds, the official controlled-response bridge, the physical singleton return/readout and the extra-white criterion. The queried headlines report only `propext`, `Classical.choice` and `Quot.sound`. The last criterion states the usual period hypothesis explicitly: the lower register returns at time `t` exactly when `P` divides `t`. The output counts and period-64 example are separate computations. I have not requested a portal submission. [Rooted theorem](../tests/probes/lean/RightRayRooted.lean) · [Official controlled-response theorem](https://github.com/WolframInstitute/Rule30PrizeKit/blob/2b6233857e5b0828333657e3499464438baf3ccb/lean/Ruliology/CellularAutomata/Rule30ControlledResponse.lean)

**Run incident.** A separate `leanchecker --help` command ignored the unknown flag and started its default module scan. I terminated it and confirmed the process exited. It consumed at least 224.92 CPU seconds and its last sampled RSS was about 7.1 GiB. This exceeded the planned block CPU allowance and overlapped the last compiler checks. The targeted checks retain their own capped receipts and standard-axiom outputs; the unintended scan supplies no verification. I stopped further computation. Future checker invocations should be scoped to named modules under the supervisor. Usage questions can be answered from the installed source.

**Next executable step.** Carry the all-width window argument, then replace the four residue cases by one Lean theorem indexed by `J`, using `white_path_iff`, `spot_iff` and the top-bit bound. Check `J=5` and `J=7` first. Use the kit’s existing `R_two_eq_one` or its two-line recurrence proof to discharge the odd-width low bit. This is a source task; no enlarged period census is required. Keep same-edge rigidity as a separate target. A same-width collision of complete three-letter words would change that problem directly.

Receipts and source hashes are in shared-store archive `cited/gpt/gc2666-right-ray-evidence.tar.gz`, 6643 bytes, SHA256 `8a9da1d3caad2edaf94c5d3d7028f6e45a995aa0f67a70c515515c6a99769750`. The capped Lean development and validation stages accounted for 63.58 aggregate worker CPU seconds, separately from the incident above.
