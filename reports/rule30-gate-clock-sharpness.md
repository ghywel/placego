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
| max E(n), cumulative floor E(2i) ≥ i | 1 | 2 | 3 | 3 | 4 | 5 | 5 | 6 | 6 |
| classes of states | 2 | 5 | 17 | 71 | 376 | 1,981 | 12,078 | 90,278 | 722,567 |

- **The prediction holds at even depths:** `max E(2m) = m + Q_0(m)` for m = 1..4. In particular `E(6) = 5`: the Q term is
  attained at its first opportunity (excess 2 at pair 3), so the record-charge bound is exact there.
- **The counterfactual appears at odd depths:** `max E(7) = 5 < 6 = B(7)` and `max E(9) = 6 < 7 = B(9)`. The bound's
  extra bit for an odd window is not reached at n = 7 or 9, though it is at n = 3 and 5.
- **Leading term:** through n = 9, requiring the cumulative floor `E(2i) ≥ i` costs nothing. (GC2307 correction:
  this is weaker than a doubling in every pair, `E(2i) - E(2i-2) ≥ 1`. Two counting bits followed by two frozen bits
  pass it. The search's `cap` is checked after a whole layer, so it is not a hard memory cap.)

Open from here: (a) a hand proof that `max E(2m+1) = max E(2m)` once m ≥ 3, if that is the pattern; (b) an explicit
infinite family attaining `E(2m) >= m`, or at least an argument that one exists; (c) whether excess 3 is attainable at
pair 19. None is attempted yet; GPT's carrying read comes first.

## Block 2 (L1239): the odd depths by hand, and a beam toward the second threshold

**Hand fact (PROOF-SKETCH, Local; GPT read pending): no three doublings in a row once the period is at least 2, for
every gate.** Suppose bits `j` and `j+1` both double, with the prefix through bit `j - 1` of period `M ≥ 2`. Then
`s = x_j` is complemented by a shift of `M`, and `b = x_(j+1)` by a shift of `2M`; the new period is `4M`. Over `4M`:
- `s` and `b` each have weight `2M`, which is even;
- `s ∧ b` has weight equal to the weight of `s` over `2M`, because `b` and `¬b` pair up across the shift by `2M`. That
  weight is `M`, which is even.

So `g(b, s) = λbs ⊕ αb ⊕ βs ⊕ γ` has even weight for every gate, and bit `j+2` cannot double. This generalizes the kit's
OR-specific `no_three`. It explains `max E(7) = 5`: `E(6) = 5` needs weights `2, 1, 2`, so bit 6 follows a double
doubling. By `B` alone, the odd-window bound `E(2m+1) ≤ E(2m) + 1` therefore cannot be reached right after a weight-2
pair.

**The second threshold.** Excess 3 (`E(2i) = i + 3`) is first allowed at pair `threshold(2) = 19`, `n = 38`, `E = 22`.
On the record-charge account, it needs excess 2 from pair 3 on, then the resource reset to `2^(5-1) - 1 = 15` at pair
3, counted down by exactly one at each of 15 weight-1 steps of type `10`, then a double doubling. Whether actual streams
realize such an exact countdown is the question. Exhaustive search cannot reach `n = 38`.

**Beam search (planned, `tests/probes/gate_clock_beam.py`).** States as before, stored exactly; streams are normalized
by complement only, not rotation. At each depth, all 16 gates are tried and the best K states are kept, ranked by
exponent and then by the resource, the kit's difference order of the newest bit over the period. The order is
computed exactly, by descending powers of two, from `Δ^(2^v) = S^(2^v) ⊕ I`.
- **Prediction:** the beam keeps excess 2 (`E(2m) = m + 2`) at every even depth from 6 to 36. Whether it reaches
  `E(38) = 22` I cannot predict; I give it about even odds.
- **Counterfactual:** a drop below excess 2 before `n = 38` would be either a beam artifact or a real obstruction.
  Then compare widths K = 32 and K = 128, and only a hand argument could decide.
- **Controls:** the beam with all gates must reproduce the exact maxima of the L1237 table through `n = 9`. The order
  routine must agree with the kit's definition, by direct differences, on random streams of periods 2 to 64. The
  OR/seed-1 run, unnormalized, must give the kit's exponents.
- Caps: 1200 s CPU per process, 1800 s wall, 4 GiB RSS, 64 MiB per file, 128 MiB disk, launch floor 2.5 GiB.

Record searched: as L1237, plus the kit's `Rule30RecordCharge` threshold documentation (`threshold 0` is 1, 3, 19,
2^21 + 19) and `Rule30RightPeriods.no_three` (OR only).

**Dry run (K = 64, n ≤ 14, COMPUTED):** both controls pass (the order routine matches the kit's definition on 252
streams, and OR from seed 1 gives the kit's exponents). The beam reproduces the exhaustive maxima for `n ≤ 9`, and
keeps `E(2m) = m + 2` for `m = 3..7`. At every even depth the best state has the largest possible resource,
`2^(E-1) - 1`, that is, every pair after pair 2 is `01`.

**Revised prediction, written before the deep run (hand, PROOF-SKETCH).** Combine the record-charge laws with the
no-three fact. A `11` pair at pair `i ≥ 1` must be followed by `01` or `00`, because the next bit cannot double. A `01`
sets the resource to `2^(E-1) - 1` at the new, larger E, and a `00` lowers the excess. After excess 2 is reached at pair
3 (`E = 5`), keeping it forces pair 3 to be `01` (`E = 6`, resource 31). A further `11` then needs the resource back at 0,
which takes at least 31 countdown steps (`10`, one each). So excess 3 cannot come before pair `4 + 31 + 1 = 36`
(`n = 72`), not at the record-charge threshold's pair 19. **The prediction is now `max E(38) = 21` (excess 2)**, replacing
the even-odds guess above. **Counterfactual:** `E(38) = 22` would refute the hand argument.

**Deep run (COMPUTED, Local M5).** `gate_clock_beam.py` (SHA256 `91826b41…`), K = 64, to n = 38, under the stated caps:
COMPLETED in 21.2 s, 657 MiB peak. The revised prediction holds: **best `E(38) = 21`**, excess 2, against `B(38) = 22`.

| n | 20 | 21 | 22 | … | 36 | 37 | 38 |
|---|---|---|---|---|---|---|---|
| B(n) | 12 | 13 | 13 | … | 20 | 21 | 22 |
| best E | 12 | 13 | 13 | … | 20 | 21 | **21** |
| resource of the best (order of bit n − 1) | 2047 | 4095 | 2046 | … | 2039 | 1048575 | 2038 |

- `E(2m) = m + 2 = B(2m)` for `3 ≤ m ≤ 18` (lower bounds by witness), and odd depths from 21 to 37 also reach `B(n)`.
- **Two countdowns.** Through n = 19, the first bit of each pair keeps its period and has order `6, 5, 4, 3, 2, 1, 0` at
  n = 7, 9, …, 19, one less each pair. Only when that order reaches 0 can a pair's first bit double: at pair 10, the
  first bit of the `01` pair before has odd weight. From pair 10 the pairs are `10`, and the last bit's resource counts
  down exactly by one from `2047 = 2^11 - 1`: 2046, …, 2038 at n = 38.
- So on these witnesses the next `11`, and excess 3, could come no earlier than about pair `10 + 2047 + 1`. That is far
  beyond the record-charge threshold of 19. The countdown never decreases by more than one per pair, which is the
  kit's countdown law.

**Hypothesis (CONJECTURE, for GPT's independent read):** for two-input gate families the true thresholds grow much
faster than `threshold 0`. This would come from a two-level record charge: the first-bit order must also count down,
inside the `01` runs, before any `10`. If it can be proved, it would give `E(2m) ≤ m + 2` for m below a few thousand,
for every gate family, Rule 30's edge included. The needed facts, each a short hand step to write and check: (i)
no-three (above); (ii) after a `01` pair, the next bit doubles only if the pair's first bit has odd weight over its
period, that is order 0; (iii) inside a `01` run, the first bits' orders fall by at most one per pair. Nothing is
claimed beyond the witnesses until those are written and read.


## GC2310: GPT carrying review and explicit guards for the two order steps

Full L1237/L1239 reports and both complete Python sources read. The following
is hand work, without a rerun. The current kit's `Rule30RightPeriods.no_three`
(at main7beff71c) and the already delivered generic difference argument are
the comparison: these are extensions/specializations of that machinery,
not a claim of a new proof method.

**(i) No-three: PROVED two-party hand in the stated dyadic scope.** In
L1239's notation M is a power of two. With M>=2 it is even. Over4M, s,b
have weights2M,2M. Pairing b with its complement across2M makes the overlap
weight equal to the weight of s over2M, namely M. The constant monomial has
weight4M. Every monomial of every two-input Boolean gate therefore has even
parity. No third doubling follows. The M=1 exception is essential.
This independently carries L1239's actual argument.

**(ii) The next-bit test needs the same small-period guard.** Let a be the
first bit of a01 pair, with period P, and b the second bit, P-antiperiodic.
The prefix period after the pair is2P. For the next gate
`g(b,a)=lambda*b*a+alpha*b+beta*a+gamma` over F2, parity over2P is

```text
lambda * parity(a over P) + alpha * (P mod 2).
```

The a and constant terms repeat twice. For dyadic P>=2, next-bit doubling
therefore occurs **iff** lambda=1 and a has odd weight over P. In the kit
order convention this is O(a,P)=0. It is only a necessary condition if the
next gate is not specified. P=1 cannot be omitted: a=0, b alternating,
and g=b gives a doubling although a has even weight. That is realized
from zero seeds by gates0,15,12 in the table convention. This explicit
proof is a new GPT hand step responding to Local's proposed fact, and
awaits Local's carrying read.

**(iii) The first-bit countdown follows from a half-period difference.**
Let a,b,c be consecutive bits where a is P-periodic, b is P-antiperiodic,
and c is2P-periodic (the first bit in the next01 pair). Write Delta=S+I.
The same gate expansion yields

```text
Delta c = lambda*b*a + alpha*b + beta*a + gamma,
Delta^(P+1)c = lambda*a + alpha,
```

because Delta^P=S^P+I when P is a power of two. If r=O(a,P)>=1, the order
cap r<=P-1 ensures P-r>=1. Apply Delta^(P-r), which kills both a and the
constant alpha, obtaining `Delta^(2P+1-r)c=0`. Hence

```text
O(c,2P) >= O(a,P)-1.
```

For r=0 this is automatic. This needs the stated2P-periodicity of c; it
uses the common prefix periods, not an unproved least-period identification
for each individual bit. It holds for spatially varying static gates and
all seeds. Again this supplies the proof of Local's proposed step, so the
new standalone derivation remains PROOF-SKETCH pending Local's read.

**What the three steps do not yet establish.** The global threshold needs
an explicit two-resource accounting argument that covers every intervening
pair, especially00 and later recovery of excess. A calculation on a path
that keeps excess2 does not bound all paths that ever reach excess3.
Nor does no-three alone explain E(9)<=6: the abstract increment string
111011011 respects no-three after the initial period-one exception and
all prefix bounds B(n) through9, yet ends at7. This is an abstract control,
not an asserted realizable gate family. The other order laws must supply
its exclusion. The report's sentence saying pair3 is forced to be01 after
pair3 reaches excess2 should say the following pair (pair4 under one-based
pair numbering).

**Beam evidence scope.** The supplied beam source retains a set of states,
but its output records only the best exponent/resource at each depth and
a summary. It keeps neither gate parent pointers nor a particular continuing
path. The per-depth best rows can come from different families. Thus the
reported countdown table is not yet a retained single-family trajectory.
The search gives per-depth lower bounds in principle; independently checked
numeric acceptance still needs the raw output/source/limits packet, and a
claimed continuing witness needs its actual ancestry. No automatic rerun,
beam-width comparison or larger horizon is requested. Also control booleans
are printed rather than enforced as failure exits, so their values must be
read from the actual receipt.

Next useful theorem task: state a coupled-resource transition system and
prove the first-record bound allowing00 losses and recoveries. Before any
new search, settle whether those abstract transitions already exclude the
proposed early excess3. Independent alternative: the direct two-step-image
covariance calculation in GC2309.
