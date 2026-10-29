# What the portal knows: the statements of the Rule 30 Prize as one picture

*GPT dated review, GC2151–GC2153,29 October: section5.1's40 forecast already has a published answer,
Rowland2006 J40=92, increment13; no repeat needed. The limit remains open. Positive, not negative, linear
drift of J_k-2k would suggest density below one half. The kit already proves temporal half-blackness for
newly doubling individual diagonals; the conjecture concerns frequency of doubling across diagonals.
See [account and bounded omitted-transition check](../rule30-edge-density-account.md). Original text follows.*


Cloud, 2026-10-29, CL640, at the owner's request ("consider the learned maths from the portal as a whole - not the long
proofs but the statements they prove - and try to connect these formulae ... to begin to try to understand a unifying theory").
Sources: the kit at 932cf8d (141 modules; `lean/README.md`), the public page at 10:12Z (62 entries, 29 ours;
MAP.md section 16), the `equivalents/` library (108 equivalent forms), and our record. Statements only; every item below is a
theorem somewhere unless marked *conjecture* or *measured*. Two cheap computations of my own are reported in section 5 with
their scripts (`tests/probes/wolfram/edge_gaps.c`, `edge_lift.c`). Nothing here changes any status; the candidate statements
of section 5 are instinct, with kill tests, for the workers' and the owner's judgement.

*Corrections (2026-10-29 12:58 GMT, CL641, after GPT's scope review GC2146, reports/wolfram-agents/CL640-GPT-SCOPE-REVIEW.md; all six taken and
applied in place below): (1) physical left and right were reversed in the two mechanisms; (2) the arc theorem 0ef6e2 is conditional on
large partial quotients; (3) the width-16 channel figure 0.2131 is a record prototype, not a published theorem, so the capacity
statement uses the published width-14 bound; (4) an entropy gap plus one witness does not make the whole gate language a subshift of the
gap shift, only its intersection with it; (5) a finite J_40 cannot kill a limit, and the sign of the drift that would argue against
the conjecture is positive, not negative; (6) the five half-rate appearances are a connection, not one theorem.*

*GPT source update, GC2209,29October: sections3.5/5.2's claim that no forbidden gap words have been written is superseded by [the exact prior-art/interface audit](../rule30-clocked-gap-interface.md). L323 already lists the seven-gap SSLSSLS, and L590/GC1009/1011 give explicit longer cuts with startup guards. The two time conventions match by a one-tick restart; the direct clamped-boundary transfer remains a solo hand sketch. A single bounded published-graph check detects the known seven-gap word and misses two known42-symbol cuts. No new cut search or entropy stage is queued. The original appraisal text below is preserved.*

## 1. One rule, three frames, two mechanisms

Rule 30 is `new = left XOR (centre OR right)`. Everything proved so far follows from two consequences of that formula, and every
statement on the portal lives in one of three frames.

**Mechanism 1, left-permutivity.** With `new = L XOR (C OR R)`, toggling the left input always toggles the output, and
`L = new XOR (C OR R)`: the left neighbour is recovered from the next row and the right pair. So a cell's influence on its *right*
neighbour is unconditional, and the whole history to the *left* of two adjacent columns is determined by those two columns (Jen).
The kit's name for the consequence is Jen's theorem with its masked and windowed forms; the portal's name for it is "the moving left
edge forbids two periodic columns".

**Mechanism 2, OR-masking.** The right neighbour enters only through `C OR R`: when the centre is black the OR is 1 whatever `R`
is, so a black cell masks the influence of its *right* neighbour, and a white cell passes it. The left neighbour enters by XOR and
is never masked. So influence travels rightward unconditionally and leftward only through white cells. (In the wall frame, where
depth increases leftward, the same statements read with the words exchanged; the kit's depth coordinates are used in sections 2B
and 3.4 and said so there.) The portal's names for this: the nine-black shield (`black_shield`), the ether-and-wall traps, "white
passes, black masks" (GC1897, in depth coordinates), the forced bits of the sideways front (L3 to L6), the vacuum certificates, and
the 2-to-1 character of the zero-boundary map (`backward_det`).

**Frame A, the lab (column) frame.** Time down, space across; the object is the centre column `c(t)` and its neighbours. Home
of Problem 1 itself, of every word exclusion, of the run bounds, and of Problem 2.

**Frame B, the right-edge frame.** Read a finite row from its rightmost black cell as a binary number `a`; one step is the
T-function `Φ(a) = a XOR (2a OR 4a)` (`IntegerRows`, `TFunction`). Bits below `n` evolve on their own; `Φ` is a permutation of
`Z/2^n` for every `n`; the orbit closure of the seed is the 2-adic odometer (Coven, Pivato, Yassawi; `Odometer`); the right
diagonals `R_j(t) = cell(t, t - j)` are the coordinates of that odometer, each periodic with period `2^{e_j}`; the automaton
group is 2369. The centre is the diagonal of the bit matrix: `c(t) = bit t of Φ^t(1)`.

**Frame C, the wall (zero-boundary) frame.** The left half beside a white wall, `(Fx)_k = x_{k+1} XOR (x_k OR x_{k-1})`,
`x_0 = 0`. As an integer with bit `0` at depth `1`: `F(Y) = ⌊Y/2⌋ XOR (Y OR 2Y)` (Bosdure, 317c64). **Frames B and C are
the same map up to one discarded bit: `F(Y) = Φ(Y) >> 1`** (the bit at the wall is thrown away each step, and the wall's
whiteness re-enters through the OR of the two lowest bits only). The kit's `FrozenBoundary` family is the formal home of this
identity: every frozen two-cell boundary is "rule 30 in the bulk and an autonomous rule on the two edge cells", and `Q01` is the
period-2 instance of the frozen-boundary conjecture. The sideways reconstruction (`recon`, Theta) is Frame C with time and depth
exchanged: the trace at the wall determines the row (`realization`), one free bit per two depths.

The three frames are connected by exact dictionaries, and the portal has filled in all three:

| | Frame A (centre) | Frame B (edge) | Frame C (wall) |
|---|---|---|---|
| state | a column of bits | an integer / a 2-adic number | an integer with a leaky low bit |
| the map | `evol` | `Φ`, a permutation mod every `2^n` | `F = Φ >> 1`, at most 2-to-1 |
| periodic structure | **open** (Problem 1) | odometer: `R_j` periodic, `2^{e_j}` | the stripe `…0101` is the unique fixed background |
| what is counted | words, runs | period exponents `e_j`, white gaps `J_k` | survivors `2^{⌊W/2⌋}`, death times `D(W)` |
| the half | `Problem 2` (density 1/2, open) | `e_j ≤ j/2 + O(log* j)` (theorem) | one free bit per two depths (theorem) |

## 2. The map of statements, by object

**A. The centre column (Frame A).** Problem 1 ⟺ no word `w` is an eventual tail (`problem1_iff_no_word`). Every exclusion
on the portal is one proof shape: *a periodic centre forces, through a finite relaxation of the cells to its right that is closed
under the word's steps, the next column to be periodic at some phases; Jen forbids it.* The families now closed:
- black runs: `1^r u` with `9⌈(P - r)/4⌉ ≤ r` (Bosdure, halving the kit's slope); `1^r u`, `|u| ≤ 4`, `r ≥ 9`; `|u| ≤ 8`, `r ≥ 18`;
  `11 0^q`, `q ≥ 8` (Norris);
- white-padded tails: `0^r u` for every `u` with `r ≥ paddedBound(u)` (singly exponential in `|u|`; Lowry, AIOvernight; sharp
  bounds 8, 9, 49, 69, 74 for short tails; every block of ≤ 9 cells after ≥ 102 whites);
- the white end `1 0^q`, `q ≥ 9` (ours from 10 in every column of every leftmost-black configuration; AIOvernight from 9 for the
  seed by one pumped certificate);
- grammars: periods made of blocks `1^r 0^q` from four run categories; all white runs ≥ 17; mixtures of isolated and double
  black cells (AIOvernight);
- lists: 30 (kit) + 2 + 87 + 39 + 74 explicit words (kit, AIOvernight, ours), lengths 8 to 18;
- runs of the centre, for Problem 2: black runs `L ≤ a - 2` (Villafuerte), `5L ≤ 3a + 10` (Goux), white `L ≤ a - 3` (Morales),
  with `log log` margins (AIOvernight); so `log₂ n + 1` black cells before `n`, `log_{8/5} n` white.
What is **not** covered: every word with no run of 9 and no long white padding; in particular all words of periods 2, 3, 4, which
is why those go to Frames B and C.

**B. Period 2 (Frame C and its coupling).** Under the clock `0101…` the centre passes nothing to the left half (`effective_step`),
so period 2 reduces to `Q01`: no finite start beside a white wall keeps depth 1 black at every even time. Known: every start of
width ≤ 60 dies (kit ≤ 52; ours 56, 60), with exact death times `D(52) = 96`, `D(56) = 100`, `D(60) = 114` and lower bounds to
`D(76) ≥ 138`; the constrained starts are `Theta f` with free bits `f` at odd times, exactly `2^{⌊W/2⌋}` of width `W` survive
through `W - 1` (`count_constrained`), and `F²` acts on the free bits as the shift (`two_step_shift`). Under the coupling the
free bits never spell `00` or `11111`. The right neighbour of a clocked centre: no Sturmian word of any slope or intercept, no
finite-arc rotation code whose continued fraction has arbitrarily late large partial quotients (ours, 0ef6e2), no near-squares at unbounded scales (Corollary F, ours), and at most `0.2445` bits of information
per visible bit at width 14 (the channel bound, ours; a width-16 prototype in our record gives `0.2131` and is not published). The coupled form `CQ01` is `Psi R` infinite for every
finite right half `R`; two infinite families are absorbed by the ether (ours); the empty right half's gate has gaps 3 or 5 from
step 146 (Bosdure), which turns `CQ01Empty` into the left-only `Q01Gap`. `EdgeObservable` (equal centre traces ⇒ equal left
edges) implies Problem 1 (Lowry), and holds for three edge pairs with exact deadlines 8, 13, 14 (ours). Sparse16: 56 even blacks
force 17 blacks in 111 cells (AIOvernight). The sibling rule 210 shares the count `2^{⌊W/2⌋}` and has `Q01` **false** and the
two-sided statement **true** (ours): the counting cannot decide `Q01`. Stripe prefixes with tails of up to seven cells die within
45 steps of arrival (Yin, Quint, Lowry); the seven-cell prefixes `1100011` and `1010101` merge in two steps for every tail (ours).

**C. Periods 3 and 4 (Frame A's right half under a periodic driver).** The period-3 ether erodes, so it has no wall (Morales);
`Q001` holds to width 37 (giraudsa). Period 4 reduces to Absorption into the ether-and-wall family; proved for a single cell at
every position and phase and for every right half white on cells 1..30 (Tensorbend); the weaker `Lock w` suffices (Bosdure), and
the left half must be finite: with a 7-periodic left half and a finite right half the centre reads `0001` from time 0 (Bosdure).

**D. The diagonals (Frame B and its mirror).** Right: `R_j` has period `2^{e_j}`, `e_j` non-decreasing, doubling exactly when
`R_{j+1}(2^{e_j})` is black, never three times in a row; `e_j ≤ j/2 + O(log* j)` (AIOvernight) and `e_j ≥ log₂(j + 2) - 1`;
row `2^k` reads `1 0^{J_k} 1` from its edge, with `R_n` of period `2^k` iff `n ≤ J_k`. For every finite seed the right diagonals
after the first equal adjacent pair have least periods 4, 8, 8, 16, 32, 32 (ours); the 101 shift law and its mod-4 forms (ours);
a finite-depth right edge follows the single cell's ruler with a cap, and the only odd 2-cycles of the edge map are `±1/3`, the
rain rows, which keep an alternating patch for ever while every staircase of the single cell ends (ours). Left: `D_j` eventually
periodic with period dividing `2^j`, the periods unbounded, no two adjacent eventually white, white runs in the settled band at most
`2P - 1` (ours); eventually white diagonals at least five apart (AIOvernight); defect spectra `D_2..D_5` (Villafuerte).

**E. Structure (all frames).** The XOR of two histories is a history only trivially (AIOvernight). Every density conserved by four
steps on every window is a coboundary (Lowry): there is no local conservation law, as our window-12 search had found. Distinct
columns of the seed differ by time `max(|p|,|q|) + 18` (Lowry). Two finite rows with equal traces: merges and ambiguities with
unbounded right support (Lowry); the terminal rewrites `011 → 01`, `101 → 11` preserve the centre trace (Lowry; our right-end
moves). Configurations recurring with velocity in `[-1, 1)` are spatially periodic (kit); at velocity `+1` the periodic rings are
closed walks of periodic profiles, and at period 2 only white and alternating (ours). A 32-step return with the shielding gates
forces period 2, hence a stripe (Lee). The centre cell at time `t` has algebraic degree exactly `2t - 1` (Norris; kit).

**F. Problems 2 and 3.** Problem 2 is equivalent to one nearly geometric sequence of nearly balanced scales (Tensorbend), to the
times of the black cells, to Cesàro and Abel means, and more (`equivalents/`). Problem 3 has its three formal forms (kit); the
degree and query-complexity bounds (Norris) are the only quantitative statements.

## 3. The connections

**3.1 The whole of Problem 1 is one implication chain, and the exclusions are its finite instances.** Suppose the centre has
eventual period `P`. By left-permutivity the left half is a function of columns 0 and 1; by Jen column 1 must then be
non-periodic; so the right half, driven by the periodic centre, must keep its first column non-periodic for ever. Every exclusion
on the portal shows the opposite for one family of drivers: the driven right half falls into a finite set of strip states closed
under the driver (a trap, a vacuum, a pumped relaxation, an ether wall), and its first column is forced. The *shape* of the open
cases is therefore one question: **for which periodic drivers `w` does the driven right half, from a finite start, always lock
its first column?** The ether-and-wall conjectures (period 4), `Lock w` (Bosdure), the period-3 reductions, and the width-`K`
strip pumpings are all this question for particular `w`. Period 2 is the exception that makes the left half the difficulty: under
the clock the right half's first column is *not* forced periodic, it is merely starved of information (0.21 bits per visible bit),
and the left half must supply the rest from a finite start, which is `Q01`.

**3.2 Five appearances of "one bit per two cells" are one connection.** (i) `Theta`: a constraint at every even time pins every
second depth, the odd depths are free (`tri_odd`, `tri_even`). (ii) `count_constrained`: `2^{⌊W/2⌋}` survivors through `W - 1`,
and exactly `2^{W - ⌈T/2⌉}` through `T ≤ W` (GC1867). (iii) The sideways row above a sinking front exposes one fresh trace bit
per two columns (GC1898, L960). (iv) The coin model of the death time: after the `W` free steps each pair of steps halves the
survivors, so `D(W) ≈ 2W` (measured `D(W) - 2W ∈ [-16, 6]` to `W = 76`). (v) The right-diagonal exponent grows by at most one per
two diagonals, `e_j ≤ j/2 + O(log* j)` (AIOvernight's record charge). The common mechanism is Mechanism 1 in a triangular frame: each
step exposes exactly one new bit (left-permutivity), and an observation or constraint made every *second* step can pin only every
second one. Only (i) and (ii) are exact counts; (iii) is a bijection count under a model; (iv) is measured; (v) is a proved upper
bound by its own record-charge argument. Equal leading constants do not identify their hypotheses. (v) is the same count read in Frame B: pairing the diagonals, the exponent rises by 0, 1 or 2 per pair and the
resource argument shows the average is at most 1. What is *not* a theorem is the matching lower bound in any frame: that the
freedom is actually used. In Frame C it is (every free bit is free); in Frame B it is the open question of section 5.1.

**3.3 Alternation is the one rigid periodic structure, in every frame.** The stripe `…0101` is the unique fixed boundary
background of the wall frame (Quint); it is what long black runs leave behind (`black_shield` forces `(01)^j`); the rain rows
`±1/3` are the only odd 2-cycles of the edge map and keep their patch for ever (ours); the rings with `Φ² x = x` are white or
alternating (ours); a 32-step return under the gates collapses to period 2 and a stripe (Lee); the kit's three fixed points of rule
30 restrict to exactly these rings; and the ether of period 4 is a period-2 structure in a moving frame. The record's open
hypotheses H and N (NOW.md) say the same thing at the next level: *rain is the edge map's only periodic orbit*. This is the
conjecture that would unify S2, Lee's result, the ring classification and the `T^64` computation (only `±1/3`, COMPUTED).

**3.4 The merges are one phenomenon.** `F = Φ >> 1` says the wall frame is the invertible edge frame with one bit thrown away
per step, re-entering through one OR. Hence: `F` is at most 2-to-1 (`backward_det`), two rows with the same image differ at depth 1, beside the wall, and the rest of
their difference is forced from that one bit (the GC693 fixture; our prefix merger `1100011 ~ 1010101`; the twin merges of the
forgetting front), and the kit's trace merge and trace ambiguity (Lowry) are the same leak seen from the centre. The question the kit calls
`EdgeObservable` is whether the leak can erase the *left edge* (the highest bit). In the edge frame the highest bit is never
erased (`OrbitSignalizer`: the top bit rises by exactly two per step); so `EdgeObservable` is precisely a statement about what one
discarded bit per step can hide. That is a sharper form of the question than "equal traces, equal edges", and our three exact
deadlines (8, 13, 14) are its first data points.

**3.5 Two capacities, one language.** The channel bound (ours, published at width 14) says the visible column of *any* right
half under the clock lies in a language of at most `0.2445` bits per symbol (growth ratio `1.1847`). Bosdure's trap says the empty
right half's visible column, and that of every right half whose window enters the trap, has gaps 3 or 5 from step 146. The
`{3,5}`-gap shift alone has entropy `log₂ z = 0.2556` with `z^5 = z^2 + 1`, `z > 1.19 > 1.1847`. So, provided the two results
count the same symbols (the certified bound samples column 1 at even times; the trap counts gaps between black cells of that
column), **the gate languages of the right halves that enter the trap form a proper subshift of the `{3,5}`-gap shift, missing
at least a fraction `1 - 0.2445/0.2556 ≈ 4%` of its entropy** (17% with the unpublished width-16 figure). GPT's GC2146 is right
that the whole gate language need not lie in the gap shift; the statement is about the intersection. Nobody has written down which
gap words are forbidden; the width-14 automaton (our submission) contains the answer as a finite computation, once the two time
units are matched. This is the one place where two portal results combine into a new statement without new mathematics.

**3.6 The barrier results are the other half of the map.** No local ranking, no finite abstraction, no edge-DFA ranking for `Q01`
(kit); no local conservation law (Lowry, confirming our search); rules 90, 150, 210 share Jen's hypotheses and fail Problem 1
(kit, Quint: exactly these four rules form Jen's class); rule 210 shares `Q01`'s count and has `Q01` false (ours); the coupled
witness with a periodic left half and a finite right half reads the period-4 word from time 0 (Bosdure); the XOR of histories is
rigid (AIOvernight). Together: **any proof of `Q01` must use the OR's nonlinearity beyond its counting consequences, must use the
finiteness of the left half beyond its periodicity, and cannot be a local potential.** Every one of our closed routes (job 4, the
end-bit selectors, the amplification) is an instance of one of these three.

## 4. What is still missing, said once

Problem 1 needs, for every periodic driver, that a finite right half locks its first column (3.1), *except* at period 2 where it
needs the finite left half to die (`Q01`). `Q01` needs a mechanism that is nonlinear, uses finiteness, and is not local (3.6).
The frames supply two candidate mechanisms that no theorem yet uses: the leak `F = Φ >> 1` (3.4), which says that the wall frame
loses exactly one bit per step relative to an odometer, and the odometer's own rigidity (3.3), which says that the only periodic
structures the edge frame tolerates are alternating. A proof of `Q01` along these lines would say: *a finite row in the wall frame
is an odometer orbit with a leak; the leak forces the lowest bit to be white infinitely often because the only way to keep it black
is the stripe, and the stripe is unstable under the leak.* I do not know how to make that an argument; I record it as the shape
the three frames point at.

## 5. Candidate new statements, with kill tests

**5.1 The doubling density of the right diagonals is one half (conjecture).** `e_{j+1} - e_j = [R_{j+1}(2^{e_j}) = 1]`
(kit `e_step`), so `e_j / j` is the density of black cells at the "return times" `2^{e_j}` on the next diagonal. AIOvernight's
theorem is an *upper density* statement: at most `1/2 + o(1)`. The kit records `e_j ≈ 0.43 j` numerically. My computation
(`edge_gaps.c`, the white gap `J_k` of row `2^k` to `k = 35`, hence `e_j` to `j = 81`) gives the marginal rates:

| range | gap growth per `k` | implied doubling density |
|---|---|---|
| `k = 4..14` | 3.00 | 0.33 |
| `k = 14..24` | 2.30 | 0.43 |
| `k = 24..34` | 2.00 | 0.50 |

and `e_j / j = 0.40, 0.42, 0.43` at `j = 40, 60, 79` with marginal `0.46` over `j = 40..79`. The average is dragged down by the
start (the universal start's rate is 2/3, then a long plateau); the recent rate sits on the proved bound. **Conjecture:**
`lim e_j / j = 1/2` for the single seed, equivalently `J_k = 2k + o(k)`. If true, AIOvernight's half-rate theorem is sharp. (The kit's `half_black` already gives temporal density one half on each
newly doubling diagonal; this conjecture is about the doubling *events across* diagonals, not the first half-density statement.) *Finite test, not a kill of the limit:* `J_k` to `k = 40`; the finite prediction `J_40 - J_34 = 12 ± 2` was settled from Rowland
(2006), whose table gives `J_40 = 92` (GC2151): held. A drift of `J_k - 2k` that argued against the conjecture would be linearly
*positive* (a rate below one half); no finite window settles the limit. *Seed dependence:* by the kit's lifting rule (`TFunctionCycles.lift_iff`) I computed the block exponents `E_n` to
`n = 56` for twelve finite seeds (`edge_lift.c`): `E_56` ranges from 18 to 26 (rates 0.32 to 0.46), seeds with an alternating low
end start with long plateaus (the frozen ruler at work), so **the rate is not visibly universal at this depth**; whether the limits
agree is a second question. Record searched: `per_upper_half`, `e_step`, `rows_at_powers_of_two`, `not_half_lower`; the kit's
docstring gives `0.43 j` and nothing on the limit.

*Addendum (2026-10-29 13:18 GMT, CL642):* a competing value. By hand from the kit's `S_rule`, `antiperiod` and `half_black`, the doubling bit
after a doubling is the weight parity of the diagonal two back (so two doublings force a zero: `no_three`), and otherwise the sum of the
two previous weight parities and an overlap parity; the weight parity of a non-doubling diagonal is the even-time black count of its
input. Exact to `j = 56` (`edge_diag_rules.c`). If the unforced parities were fair coins the density would be exactly `3/7 = 0.4286`,
the kit's "0.43" and the measured `0.42` to `j = 92`. Pooling 64 random seeds (CL642 part 2) gives `0.407 ± 0.009` with a
second forced zero after the letters 101 (the 101 shift law), so on this evidence the limit is near `0.41`, neither `3/7` nor `1/2`, and
the half-rate theorem is not sharp; the exact law after 101 is the open hand question.

**5.2 The forbidden gap words of the clocked gate (a corollary to compute).** From 3.5: the visible column of every right half
under the clock, once in Bosdure's trap, has gap sequence in a proper subshift of the `{3,5}` shift. *Statement to produce:* the
list of forbidden gap words of length ≤ 8, read off the width-14 (or 16) window automaton, and the entropy of the resulting sofic
shift, which must lie in `[h(u∅), 0.2131]`. *Kill test:* if the automaton admits every `{3,5}` gap word of length ≤ 8 the
restriction is long-range only and the statement is weaker than it looks. Owner: Local (the automaton data is in
`reports/wolfram-agents/submissions/channel-14/`).

**5.3 Rain is the edge map's only periodic orbit (the record's H and N, stated as one conjecture).** Every periodic point of
`T` on the odd 2-adic integers is `-1/3` or `1/3` (period 2). Known: no fixed point, the odd 2-cycles are exactly `±1/3` (ours,
S2), `T^32` and `T^64` fix only `±1/3` (COMPUTED, L1065, L1066), a 32-return under the gates forces period 2 (Lee, a different but
related map), the velocity-`+1` rings of period 2 are white or alternating (ours). *Kill test:* a fixed point of `T^128` or
`T^{96}` other than `±1/3`; the rank checker of L1066 extends. If it holds, 3.3 becomes a theorem-shaped target: the frozen ruler
plus "no other periodic orbit" would classify every eternal right edge.

**5.4 Problem 1 as a lock statement, for the workers to weigh.** Define `Lock w` for every periodic word `w` as Bosdure did for
period 4 (the driven right half's column 1 is eventually periodic at the white times of the driver, or some column is eventually
periodic). Then by 3.1, Problem 1 for all periods other than 2 is exactly `∀ w ≠ 01, Lock w` for finite right halves plus the
single seed's reduction, and period 2 is `Q01`. *Not new* in pieces (the kit's `Rule30Coupled` has `CQ ω`), but nobody has
stated the whole prize as "lock for every driver, die for the clock". The useful question is whether `Lock w` has a uniform
proof for all `w` with a run of 9 (where the shield gives a trap) and what the minimal `w` without one are.

## 6. What this suggests for the programme

- Put 5.1 to GPT as a hand question (why is the return-time cell biased white early and fair late?) and to Local as the `k = 40`
  run; it is the only place where a density-1/2 statement is already a one-sided theorem.
- Put 5.2 to Local as a finite computation from data we already own.
- Fold 3.4 into DQ-010 and DQ-009: the sideways lane's "leak" is `F = Φ >> 1`, and the open `EdgeObservable` is "what one
  discarded bit per step can hide".
- The §6.5 board has not been written to since 2026-10-25 (thirteen submissions since); the map above can seed its rows.
