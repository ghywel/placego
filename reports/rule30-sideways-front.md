# The sideways front: four bits close it, one bit is forced, and the speed lives in one conditional density

Local, 26 October 2026, L957. This block takes up GPT's GC1894 question: what local state decides whether a difference survives in the
outward reconstruction? It has hand lemmas and one frozen probe ([sideways_front.py](../tests/probes/wolfram/sideways_front.py),
frozen at 99be4a30 with sha256 f35079c5…, run once at 10:32 GMT in 1.6 s with a 12 MB maximum resident set).

**Status:** the lemmas are hand proofs, single-party, awaiting GPT's read. The speeds and densities are finite Monte Carlo
measurements, scoped as GC1894 asks. Nothing here changes the status of the prize, the board or PROOFS.

## In words

Turn the reconstruction on its side. The trace's time becomes space, the depth becomes time, and the start of the trace is a floor.
Flip one tock high up at time τ. The difference this makes never climbs. It sinks toward the floor and falls off. Its top edge
decides how long the tock is remembered.

Whether the top edge survives a step is decided by **four bits**: whether it differs in each of the last two columns, and the two
background cells beside it. That is exact; no history is hidden in the rule itself. History enters only through what the
background looks like at the top.

Then the probe found something the coin model could not have guessed. **One of those background bits is never a coin.**
Whenever the top is in the state "differs now, did not differ before", the background cell beside it is white, every time. So
that state always survives. The edge's speed then comes down to one number: how often the cell just above the edge is black.
Measured, it is 0.615, not a half. The sinking speed is about 0.155 levels per column at every height tested, the same as the
twin forgetting front of L955. A fair-coin version of the same chain sinks about 40% too fast.

## The exact part (hand)

Write c_d for column d (c_0 = 0; c_1 = the trace), and δ_d = c_d XOR c'_d for two traces that differ only at the tock τ = 2j+1. From
x(t,d+1) = x(t+1,d) XOR (x(t,d) OR x(t,d−1)),

    δ_(d+1)(t) = δ_d(t+1) XOR o(α, β, u, w),   α = δ_d(t), β = δ_(d−1)(t), u = c_d(t), w = c_(d−1)(t),
    o = 0 for (α,β) = (0,0);  NOT w for (1,0);  NOT u for (0,1);  [u = w] for (1,1).

The same holds with c' in place of c, by direct case check.

- **L1 (one-way).** Levels ≥ t evolve as a closed system, given the backgrounds at levels ≥ t. A difference never rises; it stays
  or moves down one level, and it falls off below t = 0.
- **L2 (four bits close the top).** Let H be the top of supp δ_d ∪ supp δ_(d−1). Then δ_d(H+1) = 0, so δ_(d+1)(H) = o(α,β,u,w). No
  two equal four-bit states can have different next outcomes, so GPT's kill test cannot fail for this state.
- **L3 (state 10 always survives; found by the probe, proved by hand).** If (α,β) = (1,0) at the top, then w = 0, so the top level
  survives and moves to state 11.
  *Proof.* At d = 1, w is the wall cell, which is 0. For d ≥ 2, δ_d(H) = δ_(d−1)(H+1) XOR o(δ_(d−1)(H), δ_(d−2)(H), c_(d−1)(H),
  c_(d−2)(H)). The first term is 0 because H is the top, and δ_(d−1)(H) = 0. So o = 1 forces δ_(d−2)(H) = 1 and o = NOT c_(d−1)(H),
  that is, w = c_(d−1)(H) = 0. ∎
- **L4 (where state 01 comes from, and what decides it).** State 01 at the top always follows state 11, because 10 always goes to
  11 by L3, and the start is a 10. At that step o = 0 meant c_(d−1)(H) ≠ c_(d−2)(H), so their OR is 1. Hence u = c_d(H) = NOT
  c_(d−1)(H+1). **State 01 survives exactly when the shared background cell just above the top, one column back, is black.** ∎

So the top runs the chain 10 → 11 (always); 11 → 11 or 01; 01 → 10 or vacate. With fair coins at the two remaining branches, the
expected residence from 10 is 8 columns (hand: E10 = 1 + E11, E11 = 2 + E01, E01 = 1 + E10/2).

## The measured part (sideways_front.py)

The probe ran four controls, all of which pass:

- **S0:** the sideways columns reproduce forward evolution.
- **S1:** L2 holds at every column of every run.
- **S2:** the heal/drop identity holds, in its exact bookkeeping form.
- **S3:** a Monte Carlo of tock_twins.c's influences gives 0.0027 for tock 0 on k_24 (exact value 0.0025) and 0.1694 for tock 2
  (0.1666), each within 3 standard errors.

| τ | runs | median death column | v = τ / median | P(top vacates per column) | E[levels dropped] | coin model v |
|---|---|---|---|---|---|---|
| 51 | 400 | 328 | 0.1555 | 0.1234 | 1.264 | 0.2143 |
| 101 | 300 | 657 | 0.1537 | 0.1223 | 1.269 | 0.2174 |
| 201 | 200 | 1303.5 | 0.1542 | 0.1219 | 1.274 | 0.2188 |
| 401 | 100 | 2577 | 0.1556 | 0.1225 | 1.273 | 0.2207 |

At the top, pooled over τ ≥ 101:

| Top state | Statistic | Value | Count |
|---|---|---|---|
| 10 | P(w = 0) | 1.0000 | 160,230 |
| 01 | P(u = 0) | 0.6154 | 227,327 |
| 11 | P(u = w) | 0.4824 | 327,633 |

The top sits on even levels in 0.5003 of columns, so the black ticks at even trace times leave no parity mark.

**Scored against the frozen predictions:**

| Prediction | Verdict |
|---|---|
| PS1, a flat real speed in [0.12, 0.18] | HELD |
| PS2, the coin bracket | HELD |
| PS3, coin within 15% of real | **FAILED**; the counterfactual was MET, with a gap of 42% |
| PS4, coin-like backgrounds | **FAILED**; it found L3 (exactly 1, not a coin) and a bias of 0.615 in state 01 |
| PU, the parity check | HELD |

## What it means

- **GPT's question.** The sideways transition closes exactly on four local bits (L2). The hidden history acts only through the
  background the top sees. Part of that background is forced exactly (L3), and the rest reduces to one conditional density by L4:
  P(black just above the top) = 0.615, measured. As in section 8.66, where the forward leftward speed 0.246 reduced to the density
  of the diagonal below the front "as the front sees it", **a derivation of 0.155 is a derivation of that conditional density**.
  It is a front seeing its own wake.
- **DQ-009.** The fitted slope of L955 is now a mechanism: a top edge that sinks one level about every 8.2 columns, by 1.27 levels
  when it does. It is still finite evidence, measured at τ ≤ 401. No asymptotic law is claimed.
- **No portal candidate.** L2 to L4 are elementary facts about the reconstruction, not prize-catalogue results.

## Next doors

1. **Why is the cell above the top black 61.5% of the time?** The top level vacates in state 01 exactly when that cell is white. So
   the levels the top passes through are selected for black above them. Is there a second exact lemma in the 11 state, like L3,
   that biases it?
2. **A constrained coin model.** Build L3 and L4 into the chain and make only c_(d−1)(H+1) and the 11-branch coins, with the drop
   law taken from the exact one-way structure. Does it land at 0.155? If not, more history matters, and the gap says how much.
3. **For GPT:** please check L3 and L4. If they hold, is the 0.615 within reach of a hand fixed-point argument for "the background
   above a sinking edge"?

**Evidence:** raw output out.txt (sha256 bf40621b…) and time.txt (9b7fca05…), in the shared store at
`cited/sideways-front-20261026/`, each read back byte-exact. **Reasoned verdict:** GPT's state question is answered exactly, and
the speed is reduced to one measured conditional density. **Gut verdict:** warm. L3 was a surprise that the data forced on me,
and L4 makes the speed a single number with a clear meaning.

## Addendum, L958 (26 October 2026, 10:43 GMT): one fair row drives the top; the bias is forced at arrival

**Hand lemmas (single-party, for GPT's read).** Write s = c_(d−1)(H+1), the shared background cell just above the top in the
previous column.
- **L5.** State 11 comes only from 10 or 11, because 01 survives into 10. From 10, using L3: u = s XOR c_(d−1)(H) and w = c_(d−1)(H).
  From a surviving 11 with c_(d−1)(H) = c_(d−2)(H) = v: u = s XOR v and w = v. Either way, **11 survives iff s = 0**. With L3 and L4
  the top's whole fate at a level is a deterministic function of one background row, the row just above it: 10 always survives;
  11 survives iff s is white; 01 survives iff s is black.
- **L6.** A level vacates only from state 01 with s = 0. By L4, the background cell at that level in that column is then black. That
  cell is exactly the s of the next top's first decision, whenever the new top is one level down and arrives in state 11 or 01. So
  the first decision after a drop of one is forced black, except when the new top arrives in state 10, which decides nothing.

**Measured** ([sideways_row.py](../tests/probes/wolfram/sideways_row.py), frozen at 79c86e13, one run): all controls pass, and L5
holds at every column.
- The background rows are fair and uncorrelated along depth: density 0.5000, P(1|1) 0.5002.
- At the first decision on a new level, P(s = 1) = 0.868 (55,897 cases). From age 6 on it is 0.4996.
- Drops: mean 1.270; P(drop = 1) = 0.852; P(drop ≥ 4) = 0.025.

**Meaning.** The 0.615 of L957 is not a property of the background. It is a fair row plus one forced black bit at each arrival:
the front reads its own wake, exactly, through L6. What remains open for a hand derivation of 0.155 is the arrival law (which
state the new top enters, and how far it falls). That comes from the one-way structure below the top (L1). **Next door:** a two-level
closed model, with the top and the level below it driven by fair rows and the exact lemmas. If its speed lands near 0.155, the front
speed is derivable from a finite chain.

## Addendum, L959 (26 October 2026, 10:59 GMT): GC1898 adopted; the window model reproduces the speed under an explicit fair input

**Corrections from GPT's GC1898, adopted.**
- "Four bits close the top" overstates L2. The four bits **decide the next difference bit at the old top**; they are not an
  autonomous machine. GPT's reachable witness has equal four-bit states at d = 2 with different next states: the tocks a and b sit
  at τ and τ+2, and only a is flipped.
- L4 and L5 now rest on GPT's direct proofs, which hold at a newly exposed top. My ancestry shortcut is withdrawn.
- "The only bias is at arrival" and "a fair row plus one forced bit" are withdrawn. The age ≥ 6 figure pools states 01 and 11,
  so their biases could cancel, and near-half low-order statistics are not fairness.
- **A row is provably not i.i.d. fair:** a D-cell row prefix corresponds to a D-bit trace slice, with only about D/2 free tocks.
  Along a row, a fresh trace bit enters at every other column.
- The pooled identity is (τ+1)/mean(D−1), not τ/median(D).

**What [sideways_window.py](../tests/probes/wolfram/sideways_window.py) found** (frozen at 8f956eb0, before GC1898 arrived; run once):

| Check | Result |
|---|---|
| L6 | exact in every case |
| Real speed (pooled) | 0.1549 |
| Residence by arrival (10 / 11 forced / 01 forced) | 8.07 / 6.20 / 8.93 columns, against the hand values 8 / 6 / 9 |
| Arrival law | 01 forced 0.60; 10 0.23; 01 after a drop of two or more 0.063; 11 after such a drop 0.056; 11 forced 0.052 |

With the arrival law and the residences, the renewal sum gives 8.17 columns per level and 1.27 / 8.17 = 0.155.

The window model keeps the top and k levels below it, feeds the row above with a fresh fair bit every column, and refills new
bottom levels at random. Its speed **rises** to the real value: 0.137, 0.148, 0.153, 0.154, 0.155 and 0.156 for k = 1 to 6. I had
predicted it would fall, so P2 failed; P3 held at 1.1% for k = 3 and 0.6% for k = 6. This is a model result under an explicit
external fair-input assumption, not a theorem.

**The tension is the next door.** The real row above has half the freshness the model feeds it, yet the model gets the speed.
GPT's question is the discriminator: when the top consults s, is it a fresh trace bit (a tock entering at that column) or a value
already fixed by the past (a tick column)? For a given top H and column d, the input s = c_(d−1)(H+1) has a fresh last trace bit exactly
when (H+1) + (d−1) − 1 = H + d − 1 is odd. If decisions on fixed inputs follow the same conditional law as decisions on fresh ones, given
state and age, the fair-input model is a valid stochastic closure. If they differ, the speed's agreement is a cancellation.

## Addendum, L960 (26 October 2026, 11:12 GMT): GC1899's exposure induction carries; the coin is justified for 95% of decisions; the deviation lives in backward visits in state 11

**Local's carrying read of GC1899** (reports/rule30-sideways-fresh-input.md). Each step checks:
- At column d, the backgrounds at levels ≤ H_d use trace indices ≤ H_d + d − 1 = J_d ≤ R_d.
- The top's update uses δ_d(H_d+1) = 0, so the next pair and H_(d+1), including any drop, are fixed before a new bit is read.
- The next input's leading index is J_(d+1) = J_d + 1 − K_d ≤ R_d + 1.
- B_(d+1) = max(0, B_d + K_d − 1), and a new index appears exactly when B_d = 0 and K_d = 0.
- On a new odd index, s = (unused fair tock) XOR (exposed bits), chosen before reading, so it is exactly fair given the declared history.

The argument carries. My own check below makes it operational (F0).

**Measured** ([sideways_fresh.py](../tests/probes/wolfram/sideways_fresh.py), frozen at f2640c05, one run). All controls pass:
- **F0:** complementing every trace bit beyond R_d leaves the backgrounds and the next difference unchanged, at 400 sampled columns.
- **F1:** new-odd inputs give P(s = 1) = 0.4994.
- **F2:** L6 repeats are black in all 35,799 cases.
- **F3:** the backlog recurrence holds exactly.

| Input class | P(s=1), state 11 | P(s=1), state 01 | Share of decisions |
|---|---|---|---|
| new odd (fresh) | 0.4986 | 0.5009 | 0.425 |
| new even (prescribed) | 0.5028 | 0.4966 | 0.424 |
| one-level-drop repeat (L6) | 1 | 1 | 0.102 |
| backward visit (B ≥ 1) | **0.7075** | 0.4999 | 0.049 |

**Meaning.**
- **The fair-input closure is supported where most decisions live.** Prescribed inputs act like fresh ones, given the state (gaps
  0.004). The repeats are forced. Together these cover about 95% of decisions. This is finite conditional-frequency support for a
  hypothesis, not a proof of stochastic closure (GC1900).
- **The one measured deviation is backward visits in state 11, at 0.71.** A backward visit rereads a trace index an earlier decision
  read at a higher level.
- **The long residence after a big drop into 01 (7.64 against 5) is not in its immediate input**, which is fair. It must come from the
  biased 11 visits that follow, from the lower discrepancy, or from correlations across visits.

**Next door.** What does a backward visit in state 11 know? It reads index J − k, which an earlier decision at height H + k read
with a different lower function. Hand question: does that earlier decision's outcome, through L5 and L6, force or bias the reread
cell? A small exact check is possible: condition backward-visit inputs on the earlier read of the same index.

## Addendum, L966 (26 October 2026, 12:13 GMT): the one agreed revisit stage. Short revisits are forced; long ones are mixed

GPT agreed the stage in GC1906, with its cleanup-parser repair to the supervisor. It ran once at 12:12:38Z, exit COMPLETED; the
receipts are in the shared store at `cited/sideways-revisit-20261026/`. All controls pass:
- **V0:** GC1901's identity holds on 16,940 comparisons.
- **V1:** replicates L960 (OB in state 11: 0.711; in state 01: 0.508).
- **V2:** the backlog partition is exact.

For backward visits classified by M = (earlier-read category, earlier input, gap q capped at 4, current state):

| Gap q | Current state 01 | Current state 11 |
|---|---|---|
| 2 | forced (k = 0 or n), all cells | forced, all cells |
| 3 | forced, all cells | forced in (E01, 0) and (E11, 0); mixed in (E11, 1) 0.14, (E10, 0) 0.81, (E10, 1) 0.81 |
| ≥ 4 | mixed, 0.12 to 0.56 | mixed, 0.40 to 0.78 |

- **Deterministic closure on M is refuted:** 15 of 26 cells conflict exactly.
- **M carries most of the information:** H(s_new | M) = 0.345 bits against 0.928 for the current state alone (descriptive, in sample).
- **The big forced cells carry the 0.71 bias in state 11:** (E01, 0, 3, 11) is black in all 2,098 cases, and (E11, 1, 2, 11) in all 1,836.
- **Scoring:** P1 failed (earlier reads in E11 or E10 make up 0.58 of state-11 visits, not ≥ 0.7). PU is untested, with no ENONE cases.

**Next door (hand).** The forced short revisits should be lemmas. By GC1901, the reread equals the old input XOR q OR terms on cells next to
the top. For q = 2 those cells are pinned by the top's own recent transitions (L3–L6). So a "short-revisit lemma" should give every q = 2
cell, and the state-01 q = 3 cells, exactly. The q ≥ 4 mixing would then be where unpinned background enters.

## Addendum, L967 (26 October 2026): toward a short-revisit lemma (hand, partial)

Take a q = 2 revisit with its old read at column d0 and top H0. The index is unchanged after two columns, so the total drop is 2 and the
new top is H = H0 − 2. By GC1901, with r = d0 − 1 and t = H0 + 1,

    s_new = s_old XOR T1 XOR T2,   T1 = c_(d0−1)(H0) OR c_(d0−2)(H0),   T2 = c_(d0)(H0−1) OR c_(d0−1)(H0−1).

**T1 is pinned by GPT's direct proofs.**
- In old state 01, both copies' previous ORs equal 1 (the L4 proof), so T1 = 1.
- In old state 11, the copy's own previous OR equals w_old = c_(d0−1)(H0) (the L5 proof), so T1 = w_old.
- In old state 10, w_old = 0 by L3, so T1 = c_(d0−2)(H0), which differs between the copies.

So s_new = s_old XOR [1 | w_old | c_(d0−2)(H0)] XOR T2, and everything rests on T2, the OR one level below the old top.

**Case (E01, s_old = 0, q = 2).** The stage found s_new = 0 in all 1,848 + 445 cases. Old state 01 with s = 0 vacates at once. Since q = 2
and the index returns, the drop is exactly 2 at that step and then 0. So level H0 − 1 is empty in columns d0 and d0 + 1. Write
β′ = δ_(d0−1)(H0−1), γ′ = δ_(d0−2)(H0−1), u′ = c_(d0)(H0−1), w′ = c_(d0−1)(H0−1) and v′ = c_(d0−2)(H0−1).

The two emptiness conditions:
1. δ_(d0)(H0−1) = 0. Because δ_(d0−1)(H0) = 1, this forces o(β′, γ′, w′, v′) = 1: (β′, γ′) is (1, 0) with v′ = 0, or (0, 1) with w′ = 0,
   or (1, 1) with w′ = v′.
2. δ_(d0+1)(H0−1) = 0. Because δ_(d0)(H0) = 0, this forces β′ AND NOT u′ = 0.

The branches:
- β′ = 1 gives u′ = 1, so T2 = 1, and s_new = 0 XOR 1 XOR 1 = 0. ✓
- β′ = 0 gives γ′ = 1 and w′ = 0, so T2 = u′ = c_(d0−1)(H0) XOR v′. The case closes iff c_(d0−1)(H0) XOR c_(d0−2)(H0−1) = 1.

The second branch needs the previous column's structure at levels H0 and H0 − 1. It is open by hand.

The other forced cells, (E11, 1, 2, ·), (E01, 0, 3, ·) and the q = 3 cells in state 01, follow the same template, with more OR terms.

## Addendum, L975 (26 October 2026, 13:55 GMT): the short-revisit rules, machine-certified for every trace

GPT agreed one stage in GC1912. [revisit_sat.py](../tests/probes/wolfram/revisit_sat.py) encodes both copies' backgrounds on a window
clamped to the physical boundary, imposes the exact recurrences and the case's facts, and asks whether the wrong reread is possible.

**Result: 466 queries; all 384 UNSATs verified by cake_lpr.** All eleven constant cells of L966 are certified over every boundary profile
(d0 = 2, 3, 4, ≥ 5 crossed with H0 = q .. 3, ≥ 4) and every drop pattern:
- q = 2: the reread repeats the old bit. This is GPT's GC1909 theorem, now also machine-checked.
- q = 3, from a decided old read (E01 or E11): the reread is the opposite of the old bit.
- q = 3, from an E10 read: the reread is 1.

The mixed cell (E11, 1, 3, 11) is correctly not certified. All receipts and certificates are in `cited/revisit-sat-20261026/`.
