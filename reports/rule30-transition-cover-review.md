# Transition cover admits every nonzero dyadic word

GC2239, 30 October2026. **Known theorem, independent carrying source read
complete in the stated scope.** The added hand explanations and controls
below are solo PROOF-SKETCH. No author program or GPT compiler was run.

The complete source is
[CedarTCObstruction.lean](https://github.com/Troyusrex2/Rule30PrizeKit/blob/0cbc49ef30888b32760def46ec31f954626192ff/research/agent-experiments/coordinator/20261026-height-and-cylinder/work/root-cylinder/CedarTCObstruction.lean),
SHA256 `2137d6db0e2890e59d49f2bf75dc9c32c62271bef354c35e2dbf7f8d91dd83ca`.
The source explicitly disclaims the shared two-predecessor OR recurrence.
That disclaimer is essential, not a caveat to remove by interpretation.

## Exact statement and carrying argument

For Boolean profiles on nonnegative time define Delta b(t)=b(t) XOR b(t+1).
Transition cover TC(a,b) means the two pointwise inclusions

```
a <= Delta b <= a OR S a.
```

If b is nonzero and has a returning period2^k, the theorem gives an m<2^k
and profiles x_i with x_0=1, x_m=b, each2^k-periodic, and
Delta x_(i+1)=x_i, hence TC(x_i,x_(i+1)), for i<m. These are returning
periods, not assertions about least periods. The function x is defined for
all i using natural subtraction, but the derivative/TC conclusions stop
at m. No infinite continuing chain is asserted.

The proof is elementary characteristic-two differencing:

1. Delta^(2^k)b=b XOR S^(2^k)b, by induction and cancellation of the two
   middle terms.
2. The period premise annihilates this derivative.
3. A nonzero profile whose derivative vanishes is the constant1 profile.
   Induction finds a last nonzero derivative Delta^m b=1 with m<2^k.
4. Reverse the derivatives: x_i=Delta^(m-i)b. Each derivative retains the
   returning period. For i<m the next derivative is x_i, and both TC
   inclusions are immediate.

The separate TC(0,0) and TC(0,1) lemmas permit a white prefix at the level
of this relaxation. They do not turn the derivative chain into Rule30.
The import CedarSafetySoundness supplies the ambient proof environment;
its finite-word soundness theorem is not a hidden ancestry premise in this
argument.

## What was projected out

The two actual equations for a newest pair are

```
Delta b = a OR d,       Delta a = d OR e.
```

They imply TC(a,b): a<=Delta b, and d<=Delta a<=a OR S a. Conversely, for
a single TC pair, choose d=Delta b AND NOT a and e=Delta a. The upper TC
bound makes d<=Delta a, giving both displayed equations. Thus TC is exactly
the known two-equation projection GC798, with the omitted profiles chosen
separately for this pair. In a whole chain these separately chosen profiles
need not be the profiles already assigned at the adjacent sites. That
compatibility is the missing information.

A four-tick hand control makes the distinction visible. With strings read
in increasing time and repeated cyclically,

```
b = 0001,  Delta b = 0011,  Delta² b = 0101,
Delta³ b = 1111,  Delta⁴ b = 0000.
```

The normalized chain 1111,0101,0011,0001 meets every adjacent TC condition.
But Delta(0011)=0101, whereas its two assigned predecessors have OR
0101 OR1111=1111. It fails the actual recurrence already at time0. Also
the terminal0001 word contains the cyclic forbidden block00100, so G258
excludes that terminal word as an actual profile even with arbitrary older
ancestors. Transition-cover admission therefore does not certify actual
profile admissibility, let alone finite white ancestry.

More generally, any normalized derivative chain here with m>=2 has
Delta x_1=1, so x_1 alternates. Its next assigned equation would require
Delta x_2=x_1 OR1=1, while its construction gives Delta x_2=x_1. Thus this
particular chain fails the actual recurrence. This does not exclude an
alternative actual ancestry for its terminal word. The control concerns
the construction, not every possible realization of every endpoint.

## Retained validation: author replay, not a new run

Nine selected payloads match the112-entry immutable archive manifest:
the Lean source, replay driver, guard, source map, build/check/report, and
replay log/guard receipt. The raw checker JSON exactly equals the report:

- 37 replayed constants,28 declared constants, three exact headline types;
- derivative_power_two and periodic_annihilation use propext/Quot.sound;
  normalized_tc_chain also uses Classical.choice;
- no new axioms, required statement import true, partial claim, pass.

The compiled digest reported by the author is
`4278ee92a8af1cfacf3c62ed47f3c3d791b053d5f2b0d7ea15590a9cf8a9d643`.
The replay pins official kit `5473ffd075f63c9d626e63b8455805d4831b39ca`
and checker `b882f2527a1d6e720828a0c729cc80c3977905ed9207d09af22f8d153a073905`.
The retained source map binds the earlier imported source/compiled digest;
that is author provenance, not a locally reconstructed binary. The empty
build log and the unchanged checker's deprecation warning are retained.

Author timings: compile0.4397103s, report total1.5764834s; guard wall
1.6352494s, peak owned RSS778190848bytes, minimum available system memory
43694727168bytes, exit0 without a stop. The read guard has300s wall,
8GiB tree RSS and2GiB available-memory thresholds sampled every0.1s.
It does not establish aggregateCPU, disk/output, swap or thermal enforcement,
and no raw sample stream is supplied. These are the author's measurements,
not Intel-host measurements or a new official portal status.

Retained in the shared store:
`cited/gc2239-transition-cover/review-manifest.json`, SHA256
`0d1eb089bf7d836aa8cf453aca5167ab539a7c5479c83e63f7e87ea8967713c0`.
Eleven payloads36578bytes plus manifest,12 verified raw uploads. This is a
selected source/evidence review, not an audit of all112 archive entries.

## Disposition and next use

Record searched: GC798's exact projection, G258's forbidden blocks, the
existing ancestor-ladder obstruction, and the current kit's actual
Rule30DifferenceOrder.difs_two_pow and vanish_of_period. Those last two
already formalize the characteristic-two dyadic annihilation mechanism.
Fresh known_find04:53:47Z completed at kit
`932cf8dde039b89b1dcbe9636867bb1b2057fef0`,23 open PRs, zero index changes.
This review adopts an existing exact obstruction, not a new theorem or a
novelty claim from search silence. No literature priority is requested.

Park transition-cover-only ancestry classification: it accepts every
nonzero dyadic endpoint, including a forbidden actual profile. Reopen only
with an identified shared-profile compatibility law that is not merely
another independent pair projection. Do not add gates or enlarge a seed
search automatically. The true finite-white problem remains open.
