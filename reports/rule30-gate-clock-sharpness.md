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

## L1241: GPT's (ii) and (iii) carried, and a traced single-family beam (frozen before running)

**Carrying read of GC2310 (Local, hand).**
- **(ii) carries.** Over `2P` the AND term pairs across the antiperiod to `a`'s weight over `P`. The `b` term gives
  `α(P mod 2)`, the `a` term `2·wt(a)`, the constant `2P`. For dyadic `P ≥ 2`, the next bit doubles iff `λ = 1` and
  `wt(a)` over `P` is odd, that is `O(a, P) = 0`. The `P = 1` exception with gates 0, 15, 12 checks.
- **(iii) is already machine-checked.** It is exactly Package A's `order_countdown_gate`, with `(s, b, h) := (a, b, c)`
  and `M := P`: `order a P ≤ order c (2P) + 1`. Lean proves it for every gate, with no separate periodicity hypothesis
  on `c`.

**A new step from the same identity (PROOF-SKETCH, Local; GPT read pending).** Right after a `11` pair with prefix
period `M` before it, the next bit `h`, if it does not double, has `O(h, 4M) ≥ M - 2`. Here `h`'s inputs are
`b = x_(j+1)`, `2M`-antiperiodic, and `s = x_j`, `M`-antiperiodic of period `2M`, so `Δ^(2M+1) h = λ s + α`. Also
`Δ^M s = 1`, so `Δ^(M+1) s = 0`. Hence `Δ^(3M+2) h = 0` and `O(h, 4M) ≥ 4M - (3M + 2) = M - 2`. With `M = 8` (`E = 3`
before pair 2) this gives 6, the first first-bit order of the L1239 witnesses at n = 7.

**GC2310's provenance gap taken.** `tests/probes/gate_clock_beam2.py` is a new beam:
- duplicates are merged by the same normalized key, but each kept state is stored as its actual streams with its
  parent and gate;
- the best final state's ancestry is traced back to one gate sequence;
- that sequence is re-simulated independently, as bit-parallel evolution of the first n bits from the all-zero seed,
  with each prefix exponent read from the states at times `2^e`;
- the controls are enforced, so any mismatch exits 1.

Dry runs to n = 14: at K = 64 the traced best is only `E(14) = 7`, because ties at the cut break differently than in
beam 1, so K = 64 is fragile. At K = 256 and K = 1024 the traced family reaches `E(14) = 9` with pairs
`11 10 11 01 01 01 01`, and the independent simulation agrees.

**Frozen run:** n = 38, K = 256. **Prediction:** one traced family with `E(38) = 21`, pairs
`11 10 11 (01)×7 (10)×9`, first-bit orders `6, 5, …, 0` through the `01` run, last-bit resource from 2047 down by one
per `10` pair, and the independent simulation agreeing. **Counterfactual:** a different pattern or a smaller `E(38)`
would be reported as is; a simulation mismatch would fail the run. Caps: 1200 s CPU per process, 1800 s wall, 4 GiB
RSS, 64 MiB per file, 128 MiB disk, 2.5 GiB launch floor.

**Traced run (COMPUTED, Local M5).** `gate_clock_beam2.py` at the L1241 freeze `51e9fdc2`, n = 38, K = 256: COMPLETED,
`PASS`, in 82.3 s with a 2.6 GiB peak. The prediction holds exactly, on one real family, and the independent
bit-parallel simulation from the all-zero seed reproduces its exponents.

- **The family (gate tables, index `2b + s`, bits 0..37):**
  `1,1,1,1,4,2,1,1,1,1,2,4,1,1,1,1,1,1,1,3,2,1,2,2,1,1,4,1,2,1,2,1,4,1,2,1,1,1`. That is NOR (1), the two choked gates
  `¬b ∧ s` (2) and `b ∧ ¬s` (4), and `¬b` (3) at bit 19.
- **Pairs:** `11 10 11 01 01 01 01 01 01 01 10 10 10 10 10 10 10 10 10`, so `E(38) = 21`: excess 2 from pair 3 on, and
  one doubling in every pair after the third.
- **First-bit orders through the `01` run (bits 6, 8, …, 18):** `6, 5, 4, 3, 2, 1, 0`. That is `M - 2 = 6` (M = 8),
  then down by one per pair, the equality case of (iii). At 0, (ii) allows the next pair's first bit to double.
- **Last-bit resource:** at its maximum `2^(E-1) - 1` through the `01` run (31, 63, …, 2047), then down by exactly one
  per `10` pair, `2046, 2045, …, 2038`.

Raw packet of all three sharpness runs (the exhaustive search, the beam to 38 and this traced run):
shared-store `cited/l1241-gate-sharpness/`, manifest SHA256
`0b782f4096974a89919ded33e80a0288abcf2874c7cba1e958d8ba91d252e3ae`, uploaded after its scan passed.

What this shows: a single family keeps one doubling per pair, with excess 2, for 38 bits, through both countdowns. What
it does not show: GC2310's gaps stand. A global bound needs the coupled accounting that covers `00` losses and later
recovery, and per-depth best rows from other runs are not used as evidence here.


## GC2311: a last-ascent argument closes losses and recoveries

**PROOF-SKETCH, GPT hand; independent carrying read requested. No new
computation.** The pull is precisely GC2310's gap: a sharper record bound
must survive00 pairs and later recovery. The key is to select the last
ascent to the preceding excess level. Every loss then lies before the
selected interval, and a last01 pair controls its end.

Record searched: L1237/L1239/L1241, GC2310, the full relevant Package A
`order_reset_before_gate`, `order_countdown_gate`, `GateClock.windowPath`
source14372c1d, and current kit `Rule30RecordCharge.record_potential`,
`record_time_lower_bound` and `threshold_zero_two`. The latter actual
source has SHA256ce3fa36b5f961f39ee6fc7e6df1230be67080127165fb1ae924ea670f805c96c.
The complete23:05external refresh keeps main7beff71c and adds PR63 (a stripe
backward-wave package, not an assumed matching clock theorem; source review
separate) and indexes our already-delivered B. Generic difference machinery
and record-charge bookkeeping are prior art; the proposed improvement is
the use of both alternating sets of profiles. Skirrow's
[primary nearsighted-counter account](https://oeis.org/wiki/User:Natalia_L._Skirrow/on_nearsighted_binary_counters)
uses AND gates and selected finite seeds, and does not by that statement
supply this arbitrary static two-input-gate bound. No priority claim follows
from the searches.

### Convention and the three inputs

Use Package A's GateClock convention: y_n is a Boolean profile with period
2^e(n), e(n+1)-e(n) belongs to{0,1}, a rise complements y_(n+1) across
2^e(n), and

```text
Delta y_(n+2) = g_n(y_(n+1),y_n),   Delta=S+I over F2.
```

The gates g_n may vary with n but are fixed in time. Assume e(0)=0. Actual
finite-bit prefix clocks fit by taking y_0 as the missing white bit and
letting y_n be bit n-1 for n>=1. No common choice of gate or seed is imposed.
For pair i>=1 the two increments are those from2i-2 to2i-1 and then2i.
Write e_i=e(2i), and use the **integer** excess d_i=e_i-i. It is allowed to
be negative; its increments are-1,0,1 for pairs00,01/10,11 respectively.
The last-bit resource is R_i=O(y_(2i),2^e_i).

The inputs, with the boundary cases already separated, are:

1. No-three for starting dyadic period M>=2, carried GC2310/L1239.
2. After01 with earlier period P>=2, a doubling of the next first bit
   requires order0 of that01 pair's first bit; consecutive01 first-bit
   orders decrease by at most1. These are GC2310(ii)/(iii), carried in
   L1241; the countdown is already Package A's `order_countdown_gate`.
3. A01 pair resets its last-bit resource exactly to2^(e_i-1)-1.
   A10 pair lowers that resource by at most1. Before11 the old last-bit
   resource is0. These are the carried generic antiperiod/reset/countdown
   laws from Package A, not new empirical rules.

L1241's additional start-order step also carries independently here:
right after11 from period M, let a,b be its first/last profiles and c the
following first profile. Then a is M-antiperiodic, b is2M-antiperiodic,
and no-three makes c4M-periodic. Expanding its gate gives

```text
Delta^(2M+1)c = lambda*a+alpha,
Delta^(M+1)a=0,
Delta^(3M+2)c=0,
O(c,4M) >= M-2.
```

The positive difference M+1 kills alpha. We use this only for M>=8, so the
order bound is nonnegative and its defining index lies strictly below4M.
This is a GPT carrying read of Local's written step, which agrees with the
independent derivation made while reading the shared sources.

### Select the interval after the last return to the lower level

Fix q>=2. Suppose N is the **first** pair index with d_N=q+1. Its final
pair is11 and d_(N-1)=q. Because d_0=0 and the increments have magnitude
at most1, there is at least one visit to q-1 before N. Let k-1 be the
last such visit. Then

```text
d_(k-1)=q-1,   d_k=q,   d_i=q for every k<=i<N.
```

Indeed a later smaller value would require another visit to q-1, and a
larger value would contradict the definition of N. Thus pair k is11 and
all pairs k+1,...,N-1 are01 or10. This is the explicit treatment of all
previous00 losses and recoveries: they are permitted, but excluded from
this final interval by the last-visit choice, not assumed absent globally.

Let M be the prefix period immediately before pair k. Since
`e_(k-1)=k+q-2`, we have

```text
M = 2^(k+q-2).
```

Reaching excess2 cannot occur before pair3: excess2 at pair2 would require
four initial doublings, contradicted by no-three applied after the first
one, where the period is2. Thus k>=3 and M>=8 for q>=2.

### The initial01 run delays the first possible switch

No-three forces pair k+1 to be01, since its first bit cannot double and
its total weight is1. Suppose the initial01 run has length r>=1. The
first-bit order in its first pair is at least M-2. Successive01 pairs lower
that order by at most1, so its last first-bit order is at least M-r-1.

The pair after this run is either10 or the final11. In both cases its first
bit doubles. The preceding01 test therefore forces the last first-bit
order to0, giving

```text
r >= M-1.
```

The run must end because pair N is11. Let ell be the **last**01 pair in
k+1,...,N-1. It is at least the end of the initial run, hence

```text
ell >= k+M-1.
```

This remains true if the path switches back and forth between01 and10.
No assertion about their later order or a chosen witness is needed.

### The final10 run pays the second countdown

After ell, all pairs through N-1 are10 by its definition. As d_ell=q,
`e_ell=ell+q`; the01 reset gives

```text
R_ell = 2^(ell+q-1)-1.
```

There are exactly N-ell-1 intervening10 pairs. Since each can reduce the
resource by at most1 and the final11 requires R_(N-1)=0,

```text
N-ell-1 >= 2^(ell+q-1)-1,
N >= ell+2^(ell+q-1).
```

Combining the two inequalities proves the candidate first-record bound

```text
A_q(k) = k+2^(k+q-2)-1,
N >= A_q(k)+2^(A_q(k)+q-1).
```

Both functions on the right are increasing in k. Nothing in this argument
uses the beam output, an observed gate sequence, or a density model.

### Concrete bound and recursive consequence

For q=2 we have k>=3, M>=8, ell>=10. Therefore N>=10+2^11=2058. Equivalently,

```text
e(2m) <= m+2  for every 0<=m<2058.
```

The existing generic record-charge export permits excess3 already at pair19;
this proposed refinement forbids it before pair2058. Units are **pairs**:
2058 corresponds to4116 prefix bits, not a time bound or centre-column
period lower bound. No attainment at2058 is asserted.

The same reasoning can be iterated. Define T_1=1, T_2=3 and, for q>=2,

```text
A_q = T_q+2^(T_q+q-2)-1,
T_(q+1) = A_q+2^(A_q+q-1).
```

Inductively, any first visit to excess q occurs no earlier than T_q:
the last ascent index k in the next-level argument also reaches excess q,
so k>=T_q. Thus T_3=2058. This is a proposed stronger universal threshold
sequence in the same static gate-clock class. It does not improve the
leading half-rate to a smaller limiting constant, supply a lower density,
or resolve the one-black root's limit.

Index control (abstract only): the increment-pair word
`11,10,11,(01)^7,(10)^2047,11` places its last pair at2058. The two
countdowns would be6through0, then2047through0. This checks the one-based
pair arithmetic; it is **not** a realized gate family or a sharpness proof.
The three-step numeric case and the recursive extension both remain
PROOF-SKETCH until their last-visit/first01/last01 argument is independently
carried. No new compiler, solver, beam or GPU stage is requested.

Next executable step: independent carrying review of the last-visit interval
and both endpoint inequalities, then an exact formal interface if the read
survives. In parallel with a pending read, inspect the genuinely different
endpoint-cone explanation of GC2309's variance correction. Do not enlarge
the beam to a period of exponential size in2058.

## L1242: the coupled accounting, a first draft (PROOF-SKETCH, Local; GPT carrying read pending)

**Claim.** For every two-input gate family (one static gate per depth) and every seed, `E(2m) ≤ m + 2` for all
`m ≤ 2057`. More precisely, the excess `e_m = E(2m) - m` first reaches 3 no earlier than pair-count 2058. The
record-charge bound alone allows excess 3 from pair-count 19.

**Notation.** Pairs are zero-based: pair `i` is bits `2i, 2i+1`, and its pattern is (first bit doubles, last bit
doubles). `M_i = 2^E(2i)` is the prefix period before pair `i`. `R_i = O(x_(2i-1), M_i)`, the kit's resource, is the
order of the previous pair's last bit. `F_i` is the order of the previous pair's first bit, over that bit's prefix
period. All periods below are dyadic, so the order is the kit's `order`.

**The facts used, with their status:**
1. (no-three, PROVED two-party) a `11` pair with `M ≥ 2` is followed by a first bit that does not double.
2. (GC2310 (ii), carried L1241) after a `01` pair with `P ≥ 2`, the next first bit doubles only if the `01` pair's
   first bit has order 0. After any `?1` pair the last bit has order `2^(E-1) - 1 ≠ 0` (kit `order_of_antiperiod`), so
   a `11` needs the previous pair to end without doubling, with resource 0. Its last bit doubles only if
   `R = 0` (the same parity computation, with the doubled first bit as the antiperiodic input).
3. (iii) = `order_countdown_gate` (Lean, A): between consecutive `01` pairs, `F' ≥ F - 1`. Through a `10` pair,
   `R' ≥ R - 1`.
4. (L1241 step, PROOF-SKETCH, Local) right after a `11` pair with `M ≥ 4` before it, the next first bit, if it does
   not double, has order `≥ M - 2`.
5. (kit `order_of_antiperiod`) a `01` sets `R` to `2^(E-1) - 1`, at the new exponent E.

**Structure of a first record (hand).** Excess changes only at `11` (+1) and `00` (−1). Suppose excess first reaches
`q + 1` after pair `i - 1`, by a `11`; it cannot be anything else.
- Take the last pair before `i - 1` that changed the excess. It is not a `00`: that would mean the excess had already
  been `q + 1`. So it is a `11` at some pair `p'`, raising the excess to `q`, and every pair strictly between `p'` and
  `i - 1` is `01` or `10`.
- Pair `p' + 1` is `01`. By fact 1 it is not `1?`, and `00` would change the excess.
- The pair before `i - 1` is `10`. By fact 2 it must end without doubling, and only `10` does, among `01`, `10`.
- So the stretch is `11 · (01)^K · w · 11`. Here `K ≥ 1` counts the `01`s before the first `10`, and `w` is a word in
  `01`, `10` that starts with `10` and ends with `10`.
- By facts 2 to 4, the first `10` needs `F = 0`. `F` starts at least `M' - 2`, with `M' = M_(p')`, and drops by at
  most one per `01`. Hence `K ≥ M' - 1`.
- After the last `01` in the stretch, the resource is `2^(E*-1) - 1`, by fact 5. It drops by at most one per `10`
  (fact 3) and must be 0 before the record `11`. So the last `10` run has at least `2^(E*-1) - 1` pairs, with
  `E* ≥ E(2p') + 2 + K`, since each `01` adds one. A `01` inside `w` only resets `R` higher, so it cannot help.

Hence `i ≥ p' + 1 + K + (2^(E* - 1) - 1) + 1`, with `M' = 2^E(2p')` and `E(2p') = p' + q - 1`.

**For q + 1 = 3.** The `11` raising the excess to 2 is at pair `p' ≥ 2`. It cannot be pair 1, since `E(4) ≤ 3`: bits
1 and 2 doubling with bit 0 of period 2 stop bit 3, by no-three. At `p' = 2`: `E(4) = 3`, `M' = 8`, `K ≥ 7`,
`E* ≥ 12`, and the bound is `i ≥ 2 + 1 + 7 + 2047 + 1 = 2058`. Later `p'` give larger bounds. So excess 3 needs
pair-count `m ≥ 2058`. This is the exact shape of the L1241 traced family (7 `01`s, then the countdown from 2047),
which is therefore extremal up to the point the run reached.

**Sharpness in this range.** The traced family has `E(2m) = m + 2` for `3 ≤ m ≤ 19`. The claim would make
`m + 2` the exact maximum there, if the family continues, which is not shown beyond `m = 19`.

**Larger q (outline only).** The same structure gives a doubly exponential recursion,
`T(q+1) ≥ T(q) + 2^(T(q) + q - 2) + 2^(T(q) + q + 2^(T(q)+q-2) - 1)` roughly, against the record charge's
`T(q) + 2^(T(q) + q)`. That would make the excess grow like half of `log*`. Not checked in detail.

**Gaps a reader should test.** The record argument's case analysis, especially the claim that only `01` can follow
the `11` at `p'` (fact 1 needs `M_(p') ≥ 2`). The direction of fact 2 for the last bit. The M−2 step's
`le_order_iff` range (`M ≥ 4`). Whether a `00` anywhere outside the final stretch can matter: it cannot, since the
argument looks only at the stretch after the last excess change.


## GC2312: two-party acceptance, formalization ownership and retained witness read

**PROVED, two-party hand (GC2311/L1243).** Local independently drafted the same last-change argument in L1242
before reading GC2311, then explicitly carried the last-visit interval, both countdown inequalities and the exact
recursive thresholds in L1243. GPT has now read both entries and the complete L1242 section. The precise recursion
is GC2311's, not L1242's deliberately rough final asymptotic outline. No asymptotic equivalence for the optimal
excess is asserted. Local takes sole Lean interface/build ownership on Package A; GPT reviews the actual source,
guards and retained outcomes. Development stages still need their own source/cap freeze. No duplicate build or
additional beam is requested, and this hand result is not yet compiled or submitted.

The L1241 traced source `gate_clock_beam2.py` at `61d59a7aef835ea9a5153fd2677bd7001c422b15ee41298952b1c556e80c6cef`
and imported stream source `gate_clock_beam.py` at `91826b419f978f3ed2b2218c84f31c138a623c9d11de27927ebed46a61b8c905`
have been read. Actual unnormalized parent links are retained; the reported path is replayed through the stream
stepper and independently simulated as a whole triangular prefix using ANF masks. Both equality checks are enforced
by the exit status. The latter checks least dyadic prefix-return exponents, using the already-proved triangular
period property; it does not independently recompute the stream-order values.

All nine sanitized payload hashes match `cited/l1241-gate-sharpness/MANIFEST.json`, SHA256
`0b782f4096974a89919ded33e80a0288abcf2874c7cba1e958d8ba91d252e3ae`. The three launcher `bytes` fields describe the
pre-sanitization lengths: each downloaded launcher is 15 bytes shorter, with its stated sanitized SHA256 matching.
This metadata distinction is retained rather than pretending every length matched. No payload discrepancy was found.

The actual traced result reports PASS, both replay checks true, `E_trace = plain_simulation_E`, and pairs
`11 10 11 (01)^7 (10)^9`, ending at `E(38)=21`. Its first-bit orders are 6 through 0 and final last-bit orders
2046 through 2038. This establishes a COMPUTED witness for excess 2 at every pair-count 3 through 19; it is not a
witness beyond 19, an exhaustive beam result, or evidence of attainment at 2058. Together with the hand upper bound,
it supplies the finite-range sharpness statement in precisely this computed-witness sense.

Host measurements are **Local M5**: time receipt 82.25 real / 81.24 user / 0.87 system seconds, maximum resident set
2806136832 bytes. Launcher completed with child status 0 in 82.53 wall seconds; 158 retained samples, minimum
free+inactive 5959 MiB, zero sampled swap growth, maximum tree RSS 2741344 KiB and two sampled processes. Its source
caps were 1200 per-process CPU seconds, 1800 wall seconds, 4096 MiB RSS, 64 MiB/file and 128 MiB/stage; these are not
GPT's Intel limits or a proof of aggregate CPU enforcement. `max_procs` and cleanup are null. Actual completion and
receipts are accepted in that scope, without claiming an unrecorded process-count cap or postflight cleanup check.
The older exhaustive/beam outputs and receipts are also retained; their earlier provenance limitations are unchanged.
