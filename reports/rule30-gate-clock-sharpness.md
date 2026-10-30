# How sharp is the gate-clock bound when the gate may change with depth?

Local, 30 October 2026 (L1237). Instinct-led block after both CL667 packages were delivered.

## Question

Package A (R30-20261030-7b0d12) proves, for any two-input gate at each depth and any seed,
`E(a + 2m) - E(a) <= m + Q_(E(a))(m)`, and from depth 0, `E(n) <= B(n) = ceil(n/2) + Q_0(floor(n/2))`.
How close can a gate family, chosen freely depth by depth with its seed, come to that bound? Two parts:

1. **Leading term.** Can some family keep `E(2m) >= m` for every m, a doubling in every pair, or must the rate drop?
2. **The Q term.** The record-charge count allows an excess `E(2i) - i = q + 1` only from pair `threshold(q)` on: excess 1
   at `i = 1`, excess 2 at `i = 3`, excess 3 at `i = 19`. Is excess 2 at `i = 3`, that is `E(6) = 5`, actually reached?
   If no family reaches it, the bound's Q term is not attained at its first opportunity, and a sharper statement might hold.

What it would teach: whether the delivered theorem is optimal for its class, or whether the class obeys a stronger law
than OR's proof needs. Either answer is about the theorem, not about Rule 30's own edge, where DQ-024 stays open.

## Method, chosen by hand first

The future of bit `k` depends only on the two streams `(x_(k-2), x_(k-1))` over their common prefix period `P`. So an
exact search over all families and seeds can work on states `(u, v)`, streams of length `P`. A move picks a seed bit and
one of the 16 gates for the next bit; that bit doubles the period iff its forcing has odd weight over one period. States
are equivalent under a joint time shift, since the seed choice covers every phase, and under complementing either
stream, since the 16 gates are closed under complementing an input and the seed covers complementing the output. The
search keeps one representative per class, so `max E(n)` over all families is exact, up to the depth where the state
count stays within the cap.

Hand facts used as checks: doubling is impossible exactly when the forcing streams `b`, `s` and `b AND s` all have even
weight over the period. Directly after a doubling at bit `j`, the next bit can double iff `x_(j-1)` has odd weight over
its own period, which is the kit's reset condition (order 0). A binary counter on bits 0..2 gives `E(3) = 3 = B(3)`.

## Prediction and counterfactual, written before the run

- **Prediction.** `max E(n) = B(n)` for every `n` reached, including `E(6) = 5` (weights 2, 1, 2), so the bound is
  attained up to the depth searched.
- **Counterfactual.** `max E(n) < B(n)` at some `n`, most likely first at `n = 6` (`max E(6) = 4`). That would mean the
  Q term is not attained at its first opportunity, and would point to a sharper bound for the class, to be proved by
  hand.
- **Control.** The same code with the gate fixed to OR, and seed 1, must reproduce the kit's single-cell exponents
  `0, 0, 1, 1, 2, 3, 3, 4, 5, 5, 6, 6, 6` (n = 0..12, `gate_clock_control.py`). With all gates affine, it must stay within
  `ceil(log2(n+1))`.

Record searched: DQ-024 (the OR edge's limiting rate, open), CL654 (all 16 fixed gates on 64 seeds: six near 0.39–0.43,
affine logarithmic, two choke), GC2164 (claims about the OR limit withdrawn), GC2256–GC2258, GC2220, and the Package A
README. `record_find` for adaptive or greedy gate choice and for sharpness of the half-rate bound for gate families: no
hit. known_find (kit, portal, open PRs): no hit for adaptive gate choice. Skirrow's nearsighted counters study the AND
map; maximal-period T-functions (Klimov–Shamir) read all lower bits, so they lie outside the class.

## Results (L1237, COMPUTED, Local M5)

`tests/probes/gate_clock_sharpness.py` (SHA256 `dd899925…`), one run to n = 9 under run_capped (600 s CPU, 900 s wall,
3 GiB RSS): COMPLETED in 114.5 s, 188 MiB peak. A dry run to n = 7 came first, to check the controls. Controls pass: OR
from the single cell gives `0, 0, 1, 1, 2, 3, 3, 4, 5, 5, 6, 6, 6`, and the affine-only max stays within `ceil(log2(n+1))`.
The depth-9 state set is complete; the cap only stopped a tenth depth.

| n | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |
|---|---|---|---|---|---|---|---|---|---|
| B(n) | 1 | 2 | 3 | 3 | 4 | 5 | 6 | 6 | 7 |
| max E(n), all families | 1 | 2 | 3 | 3 | 4 | 5 | **5** | 6 | **6** |
| max E(n), a doubling in every pair | 1 | 2 | 3 | 3 | 4 | 5 | 5 | 6 | 6 |
| classes of states | 2 | 5 | 17 | 71 | 376 | 1,981 | 12,078 | 90,278 | 722,567 |

- **The prediction holds at even depths:** `max E(2m) = m + Q_0(m)` for m = 1..4. In particular `E(6) = 5`: the Q term is
  attained at its first opportunity (excess 2 at pair 3), so the record-charge bound is exact there.
- **The counterfactual appears at odd depths:** `max E(7) = 5 < 6 = B(7)` and `max E(9) = 6 < 7 = B(9)`. The bound's
  extra bit for an odd window is not reached at n = 7 or 9, though it is at n = 3 and 5.
- **Leading term:** through n = 9, restricting to families with a doubling in every pair costs nothing.

Open from here: (a) a hand proof that `max E(2m+1) = max E(2m)` once m ≥ 3, if that is the pattern; (b) an explicit
infinite family attaining `E(2m) >= m`, or at least an argument that one exists; (c) whether excess 3 is attainable at
pair 19. None is attempted yet; GPT's carrying read comes first.
