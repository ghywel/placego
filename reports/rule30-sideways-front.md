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
