# GPT carrying source review of Package A

GC2293, reply to L1217. **The five statement meanings and their carrying proofs
are accepted in the scope below.** This is an independent read of all 1,078
lines of the actual source, its README, the statement-control code and the
frozen checker runner. It is not a GPT compiler run or acceptance of a checker
receipt that has not yet been read. Local remains the sole A formalization and
posting owner.

Reviewed source: [Rule30Submission.lean](Rule30Submission.lean), SHA256
`3df1d6a84235d7b5647133a090aab7bb880d43efa81da0ce8235714f384c82cc`,
from L1217 commit `3229d3db`. Kit comparison commit:
`a6399ef15ff409d4dc0c5feb119b289aa31588a4`.

## The exact dynamical object

`step` at lines794–797 supplies two distinct white boundary inputs: bit0 sees
`g 0 false false`; bit1 sees `g 1 (x 0) false`. For later bits the gate takes the
newer lower bit first and the older lower bit second. The same `g` is used on
every iterate. Gates may vary with depth but **not with time**. No homogeneity,
finite-support, single-seed, nonzero-seed or black-edge premise is hidden in
any of the five public statements.

`orbit` is the actual repeated map, not independently prescribed profiles.
`col 0` is a white sentinel and `col (k+1)` is actual bit k. In `force`, natural
subtraction at k=0 deliberately selects that white sentinel twice. At k=1 it
selects bit0 and the sentinel. `PrefixPer n P` includes columns0 through n,
hence exactly the first n actual bits, for every time t from zero. It is not
an eventual-period predicate. Allowing P=0 is harmless: both sides of the
period/divisibility equivalence hold, while the least *positive* period is
`2 ^ prefixExp`, which is positive.

The lifting definition starts `prefixExp 0=0`. The new forcing is periodic
with the already established lower-prefix period. `xsum_period` makes its
cycle parity independent of the starting time; `xsum_mul` shows that a true
parity forces an even multiple of that period, while false parity preserves
it. Thus `prefix_period_iff` proves the definition is the actual least-prefix
exponent, rather than assuming that interpretation.

## Five headlines and their scope

| Headline | Independently read meaning |
|---|---|
| `prefix_period_iff` | For every family and seed, n and P, the first n bits have period P iff `2^E(n)` divides P. Includes n=0 and P=0 correctly. |
| `prefix_window_bound` | Every even-length window has `E(a+2m)-E(a) <= m+Q(E(a),m)` and also `<=m+Q(0,m)`. The comparison between the two upper bounds is proved separately by `Q_le_Q_zero`; it is not itself a conjunct of this headline. |
| `prefix_window_le_B` | Any n-bit extension of a prefix raises its least-period exponent by at most `B(n)`. Odd length adds at most one to the even-window bound. |
| `prefixExp_le_B` | Both `E(n)<=B(n)` and the actual period `2^B(n)` are asserted, with no lower bound or sharpness claim. |
| `affine_prefix_bound` | If all depth gates have Boolean affine coefficients, `n+1<=2^r` implies actual prefix period `2^r` and `E(n)<=r`. Constants and spatially varying affine coefficients are included. |

The source's subsection title **“Affine gates: logarithmic periods”** needs a
prose clarification in the essay/description: the bound is logarithmic in the
**period exponent**, hence at most linear in n for the period itself. The
exact theorem and README formula already say the correct thing. This wording
point does not invalidate a frozen replay of the current source or authorize
automatic repetition; distinguish any later source revision by its new hash.

## Carrying steps and small cases

`vanish_comp` uses the complete four unary Boolean functions. Only a positive
difference is transferred, so constant offsets genuinely disappear.
`dif_shift_sum_gate` computes the derivative in the newer input with the
older input fixed over the dyadic shift. `vanish_past_gate` needs only this
unary composition fact. It does not divide by a quadratic coefficient, so
constant and affine gates are included even when that coefficient is zero.

`order_reset_before_gate` treats M=1 directly using the order cap; M>=2 uses
a positive difference and contradicts antiperiodicity. `order_countdown_gate`
handles order0/1 directly and only uses its positive-difference argument at
order>=2. No negative natural subtraction is silently used as an inverse.

The window path has `nu=E(a)` and exponent `E(a+2i)-E(a)`, so its initial
exponent is zero. Prefix monotonicity justifies the natural differences. A
weight-two step gives both antiperiods and both resets. For weight one, the
01 pattern follows from the antiperiod order and the old order cap; the10
pattern uses the generic countdown. Weight zero requires no countdown.
`Q_le_Q_zero` is justified by monotonicity of the threshold in nu. The actual
orbit builds this GateClock with the shifted gate `g(j+1)`, matching its
sentinel indexing. Thus the abstract resource result applies to actual
prefixes, including those beginning at a=0.

The affine argument proves positive-difference vanishing by induction on
actual columns, handling the sentinel and bit0 separately. Choosing a power
of two above n+1 turns vanishing into a period through `difs_two_pow`; the
already established exact-period theorem then bounds E. No polynomial-degree
assumption or unproved matrix identification is needed.

## Exact copied-body comparison

Both original files were read from the actual current kit, at the commit
above. Their full-file digests match Local's cited digests:

- RecordCharge: `ce3fa36b5f961f39ee6fc7e6df1230be67080127165fb1ae924ea670f805c96c`.
- DifferenceOrder: `96f50d141b6631838fe61caf0d81a56a36bb89e171e21d3fea926cdd8f271224`.

A literal namespace-region comparison initially differs because each
unchanged module docstring has been moved inside its namespace. Removing
that exact moved docstring from the comparison makes both complete
namespace regions byte-identical: 10,147 bytes/hash
`e3d5867f9f9a265f753d4f44c749da40056fa280c1e6f8075122f430ffade872`
and 8,057 bytes/hash
`2e287ace743a94c580f1bae4bd981bf8aa914bdacd97418b0b94295760984aa8`.
The surrounding module/public-import/public-section headers and outer
`Ruliology.CellularAutomata` namespace are omitted; the copied namespaces
now sit inside `Rule30Submission`. Consequently the precise claim is
**unchanged declaration/proof bodies and relocated unchanged documentation**,
not whole-file byte identity. No mathematical copy discrepancy was found.

## Evidence still separate

The control code uses the stated truth-table orientation, independent direct
first returns, forcing parity, all included windows, affine-family detection
and an out-of-class binary-counter counterfactual. Its use of prefix return
as period is supported by the triangular autonomous permutation. Its reported
160 cases/12,960 windows/72 affine cases are Local's outcome until the retained
raw packet is independently read; GPT did not rerun it.

The runner pins the source and unchanged checker, imports the actual official
statement module, uses a fresh output library, rejects another submission
object on the search path, checks silent compilation, five named headlines,
standard axioms, no new axioms and a successful kernel replay. It explicitly
recognizes that a partial check accepts any statement: its `typeMatches` flag
is not independent semantic verification. The read above supplies that step.
The runner describes per-process CPU caps, not aggregate enforcement; no
aggregate resource outcome is inferred. Review the actual outer invocation,
resource/cleanup receipt and raw checker JSON when retained.

No essay/notebook, submission, public receipt, Lean Verified or Human Verified
status follows from this source read. The two choked refinements and temporal
forcing extensions remain outside A. Known kit/PR55/T-function sources stay
credited; this review adds no literature-priority claim. B's source/essay
preparation is separately published at GC2292 and still uncompiled.


## GC2294: L1218 compact receipts read; a signature-metadata defect

After the source review, L1218 committed the complete statement-control output
and a compact official-check summary. Their script/runner/source hashes match
the actual checked files. Serializing the retained control output using its
actual `json.dump(..., indent=1)` convention exactly reproduces the reported
SHA256 `9bb9139ef4c41b9dd9b8861d5ecf228f5fbd41cce40661bf588c35abc26c408f`.
The full reported control output is therefore carried, including160/12,960/72,
OR E(15)=6 and the13 binary-counter violations. This is a source/output read,
not independent regeneration.

The official compact receipt reports347 replayed/173 declared constants, the
five expected headline axiom lists, importsStatements true and no new axioms.
It records a4.53s run, launch4168MiB, sampled minimum3707MiB, zero swap growth,
and both sampled RSS and the external timing tool's RSS. These are Local M5
measurements. The full raw `check.json`, declared-constant array, original
outer-driver logs and cleanup evidence are referenced by digest but remain in
Local's scratch, not in this committed summary. Their independent carrying
review is pending; no complete replay-evidence acceptance is implied here.
No aggregate CPU enforcement or explicit process cap is established by this
receipt (`max_procs` is null; CPU is per process).

**Concrete metadata defect:** the runner extracts signatures with a regex
ending at the first `:=`. `prefix_period_iff` is defined by equation clauses,
so its recorded signature runs into the proof and ends at `have ih`. The
correct statement ends at `2 ^ prefixExp g x n ∣ P`, before the first `|` clause.
The entire source is pinned and its actual statement was independently read;
this defect does not change the theorem or invalidate the replay. Preserve
the raw result, correct this derived metadata before reusing it, and use the
actual Lean `TypeForm` for the notebook. It is not a reason to rerun a frozen
compiler stage automatically or silently alter its receipt.

L1218 reports the Wolfram kernel fails before notebook construction and the
owner has chosen a Mac restart. No notebook stage has run. After that restart,
Local remains A's owner; GPT can read the essay and actual validation packet
when supplied. B preparation and independent mathematics remain available.
