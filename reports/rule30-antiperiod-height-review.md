# Antiperiodic drivers: the height obstruction and its free-partner converse

GC2242–GC2243, 30 October2026. The external necessary theorem is independently
carried in scope. The constructive converse and controls are **PROOF-SKETCH,
solo GPT**, pending an independent carrying read. No trajectory search or
external compiler ran in this block.

## GC2242: the exact existing necessary condition

Complete source:
[RootAntiPeriodHeight.lean](https://github.com/Troyusrex2/Rule30PrizeKit/blob/0cbc49ef30888b32760def46ec31f954626192ff/research/agent-experiments/coordinator/20261026-height-and-cylinder/work/root-height/RootAntiPeriodHeight.lean),
SHA256 `513de31a591d3fa7afbeb69e4ac8a3967718a1ba8ced6df39a4ba2039083ed57`.
Its dependency RootEventHeight has the exact c3e09248 source already carried
in GC2234; the retained source/report binding matches again.

Let P>0 be even, b(t+P)=b(t), c(t+P)=NOT c(t), and
d(t+1)=d(t) XOR(b(t) OR c(t)). Safe means that d never has two consecutive
white cells. Write A=NOT b, Z=NOT b AND NOT c, and
H_X(T)=sum over t<T of (-1)^t X(t), with Boolean bits interpreted as integers.
The source proves:

```
H_A(T) = H_Z(T) + H_Z(T+P) - H_Z(P).
Safe(d) implies H_A(P)=0 and |H_A(T)-H_A(S)|<=2 for all S,T.
```

P is a returning period, not necessarily a least period or a power of two.
The hypotheses do not impose the actual recurrence between b and c, nor
finite white ancestry. This is a necessary condition for a specified pair
of drivers and a specified child; no sufficiency is asserted in that source.

The carrying steps are short and exact. Antiperiodicity partitions the
white ticks of b between Z(t) and Z(t+P). Since P is even the two signed
weights have the same sign, giving the first identity, including its prefix
offset. Safe d puts H_Z in the single oriented pair {0,-q(d,0)}, by GC2234.
Every difference of two such heights is in [-1,1], so the sum of the two
shifted differences is in [-2,2]. Finally H_A(3P)=3H_A(P); the bounded
integer difference forces H_A(P)=0. The proof never needs a safety converse
or a count/frequency premise.

Raw evidence:26 replayed constants,12 declared constants, six exact headline
types, all standard propext/Classical.choice/Quot.sound, no new axioms,
required statement import, partial pass. Raw checker JSON equals the report.
Author compiled digest
`745e714a6054c7f9b2703eaf295a205480224cb14a526514ab28b2997b746321`;
official pin5473ffd0 and checkerb882f252 match the other retained height
records. Author compile3.6510182s/total6.0986038s; guard6.1969036s,
1375985664bytes owned RSS,43203649536bytes minimum available, exit0/no stop.
The300s/8GiB RSS/2GiB available guard and0.1s sampling were read. No aggregate
CPU, disk/output, swap or thermal enforcement or raw sample series is
inferred. No GPT replay or live portal status is asserted.

Twelve selected author payloads match the112-entry archive. The adjacent
CedarD3Converse statement was read to disambiguate its name: it equates two
open finite-word completeness statements, not the height converse below.
Its imported certificate chain is not newly accepted here.

Shared-store packet `cited/gc2242-antiperiod-height/review-manifest.json`,
SHA256 `eb83f9ea79ef7e5b388cf15417829a76dab57041e287addf69aac2c1ff5cba01`:
14payloads53261bytes plus manifest,15 verified raw uploads. Selected evidence
review only, not a full112-entry archive audit.

## Two hand controls: sharpness and the quantifier on the partner

Take P=6 and repeat b=010010. Its white indicator A=101101 has prefix heights

```
0,1,1,2,1,1,0.
```

Thus the necessary height diameter is exactly2. Take c=001001110110,
repeated with period12; the second half complements the first. Its joint
white-event word is Z=100100001001. From initial d(0)=1 the child is
d=110110101101, repeating with period12 and with no00. These strings directly
attain the bound. They are arbitrary temporal drivers: b contains cyclic
00100, forbidden by G258 for an actual profile. No rooted realization is
provided.

Keep b fixed but choose c=000000111111. This also is6-antiperiodic and b
still passes the same height test. If d(0)=0, then d(1)=0. If d(0)=1, then
d(2)=d(3)=0. No initial colour is safe for this specified partner. Hence
the height test cannot be sufficient for every given c. The meaningful
remaining question is existence of a suitable freely chosen c.

## GC2243: existence of a free antiperiodic partner is exactly the height test

**Claim, solo PROOF-SKETCH.** Fix any positive even returning period P and
any P-periodic Boolean b. There exists a P-antiperiodic Boolean c and a safe
child d obeying the single displayed recurrence if and only if

```
H_A(P)=0 and max(H_A)-min(H_A)<=2, where A=NOT b.
```

Zero drift and even P make H_A itself P-periodic, by the carried
height_period_add identity. Thus the extrema may be taken over one P-block
including its endpoint. In the forward direction the carried theorem applies. In the reverse direction
the construction also makes d2P-periodic, not necessarily of least period2P.
There is no recurrence requirement between b and c, or older ancestry.

The pull is to regard the bounded integer height as the sum of two binary
paths. The cheap objection is endpoint orientation: after P ticks the two
paths must exchange their endpoint values so they can be concatenated.
That issue is settled explicitly, rather than assumed from a height bound.

### Lift a three-level walk to two binary paths

Let h(t)=H_A(t) for0<=t<=P; h(0)=h(P)=0. Its steps are
h(t+1)-h(t)=(-1)^t A(t). Choose a sign e in {1,-1} and a in {0,1} so that
S(t)=e*h(t)+a always belongs to {0,1,2}:

- If h is nonnegative, choose e=1,a=0.
- If h is nonpositive, choose e=-1,a=0 (either choice handles h identically0).
- Otherwise its minimum and maximum are -1 and1; choose e=1,a=1.

Lift S to two binary paths z,w with z+w=S. At a nonzero step of S change
exactly one of the two bits in that same direction; at a zero step change
neither. Such a move is always possible at levels0,1,2. Start with
(z(0),w(0))=(0,a). We can arrange the final pair to be (a,0):

- For a=0, total S(P)=0 already forces both bits to be0.
- For a=1, h is nonconstant. Ignore zero steps and take the first excursion
  from total1 back to total1. It is1,0,1 or1,2,1. In the first case remove
  the initially occupied bit, then fill the other; in the second fill the
  initially empty bit, then remove the other. Either exchanges the labels.
  On every later excursion use the same bit for the outward and return
  moves, preserving the exchanged labels. Thus the endpoint is (1,0).

An excursion cannot move through level0 or2 to any other level before
returning to1, so this construction covers every finite walk. No fairness,
probability or asymptotic argument is involved.

### Concatenate, then choose the partner

Define K over0..2P by following z for the first P ticks and w for the next
P ticks. The endpoint conditions z(P)=w(0)=a and w(P)=z(0)=0 make K a
well-defined2P-periodic binary path starting at0.

For0<=t<P, let Z(t) mark whether z changes at that tick. Since only one
track changes when A(t)=1, the change of w is marked by A(t)-Z(t). Define
Z(t+P)=A(t)-Z(t), and repeat with period2P. Evenness of P gives

```
K(t+1)-K(t) = e*(-1)^t Z(t),
H_Z(T) = e*K(T), for every nonnegative T.
```

In particular Z<=A and its signed height is always in {0,e}. On the first
half choose c(t)=1-Z(t) wherever b(t)=0, and choose c(t)=0 wherever b(t)=1.
Set c(t+P)=1-c(t), then repeat. At a white tick of b, the second half's joint
white event is1-Z(t)=A(t)-Z(t); at a black tick neither half has a joint
white event. Thus the constructed Z is exactly NOT b AND NOT c.

Start d black for e=1 and white for e=-1. Then -q(d,0)=e. The already
carried oriented-height equivalence GC2234 applies to the recursively
defined child and shows it is safe, since H_Z always lies in {0,e}.

Finally, the number of joint white events in a2P-block equals the number
of white ticks of b in a P-block. Zero signed drift means equal even- and
odd-position white counts, so this number is even. The OR forcing over2P
therefore also has even weight. XOR accumulation gives d(t+2P)=d(t).
This proves existence and the stated returning period, without a least-period
claim.

## Searches, disposition and next discriminating check

Record searched: GC2234's complete oriented equivalence; the exact
RootAntiPeriodHeight source/report above; GC2239's missing shared-profile
compatibility control; current record and known-index queries for the named
height theorem; actual kit lean/equivalents searches for the signed-height
and antiperiod-height expressions. The last complete portal/kit refresh is
04:53:47Z at932cf8dd,23 open PRs. The linked archive explicitly states only
necessity. CedarD3Converse concerns a different finite-word quantifier.
A bounded primary-source web search for the exact antiperiod/signed-height
terms returned no source; that negative search supplies no novelty evidence.
The construction is elementary binary-path lifting; no priority or submission
claim is made.

The distinction this settles is mathematical: for a freely chosen partner,
the projected height information is enough; for a prescribed partner or a
shared Rule30 ancestry, it is not. Do not promote this to finite-white safety
completeness, a root-density bound or an obstruction to an actual00 pair.

Next executable step: write the two-track constructor with its endpoint
exchange explicit, and compare its outputs against independent exhaustive
partner/initial-colour existence at fixed P=2,4,6 only. Predict exact
equivalence with the finite height test. Include nonnegative, nonpositive,
and mixed-sign height paths, the identically-zero path and both P6 controls.
Freeze source, counters and conservative pilot limits before any run; no
larger period or automatic repetition. Independent alternative remains a
scoped source read of RootD3Reduction/CedarD3Converse's actual completeness
interface, not an assumption that either open statement is proved.
