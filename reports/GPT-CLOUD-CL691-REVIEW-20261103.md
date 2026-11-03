# Cloud CL691: fresh input and wake memory — GC2514

GPT, 3 November2026. Read the complete CL691 entry, round14 questions, owner
answers, predictions and outcomes, and both complete sources/outputs
`front_feet.py` and `fake_coin_tells.py`. No Intel replay or new search.
This is a carrying review and adversarial source check, not novelty clearance.
Record searched: GC2404's fair-trace/front review, GC521/522 jump pointers,
CL645/GC2405, current round14, and NIGHT-TASKS B2/B3. Existing left-permutivity
is the mathematical input; no new general randomness theorem is claimed.

## 1. Fresh-input fairness carries with a nonanticipating history

Let A_t be the reference Rule30 row on the whole integer line, with mutually
independent fair initial bits X_i. Let B initially differ only at0, and F_t
be the leftmost mismatch. The next cell inspected is A_t(F_t-1), with
left foot q_t=F_t-1-t. A left foot is the leftmost initial cell that can
affect a space-time cell. Rule30's linear left input gives, by induction,

`A_t(x) = X_(x-t) XOR H_(t,x)(X_(x-t+1),...,X_(x+t))`.

For fixed finitely many cells with distinct left feet, the corresponding
finite Boolean map is triangular with ones on its diagonal: conditional on
all other initial bits, solve from the largest foot down. Their values are
independent fair bits. This is the known fixed-trace fact.

An adaptive front needs an extra argument: its next inspection location must
be chosen before that initial bit is read. Here is the carrying argument.
Expose all initial bits at or to the right of the smallest previously queried
foot m. At t=0, F_0=0 is fixed. At time t, F_t is determined by the earlier
exposure. The event q_t<m and its chosen integer q_t are therefore determined
without consulting X_(q_t). If fresh, expose any skipped bits strictly between
q_t and m before reading the query. The displayed H does not use X_(q_t), so
the inspected cell is exactly fair conditional on this exposed history.

The induction that makes this legitimate uses the difference equation. Write
delta_t=A_t XOR B_t, and h(u,v)=u OR v. Then

`delta_(t+1)(x) = delta_t(x-1) XOR h(A_t(x),A_t(x+1))`
`                 XOR h(B_t(x),B_t(x+1))`.

All positions x<F_t-1 agree at the next tick. For x>=F_t-1 the right side
uses reference cells with left feet >=q_t and the current difference field.
Thus after exposing the tail through q_t, the next front location is
determined; no initial bit strictly left of the new running minimum is
needed. A finite one-flip difference never vanishes because its rightmost
edge advances one cell per tick. This closes the induction.

**CARRY:** under iid fair whole-line initial data, the advance indicator is
conditionally fair whenever q_t is a strict new minimum, for the natural
past front/query history (and the larger exposed-tail history just defined).
The phrase "whole history" must exclude advance knowledge of unqueried left
initial bits or the entire reference row. This is an ensemble statement,
not an iid claim about the single-seed front.

## 2. What that proof does not establish

On a reused foot the inspected cell is determined by the exposed initial
tail. This does **not** prove it is determined by the front's jump sequence,
the difference pattern alone, or a fixed-size wake state. The exposed tail
contains reference-background information in addition to the perturbation.
Accordingly "the conditioned core is dissolved" and "its own trace elsewhere,
and nothing else" exceed the carrying argument. A finite-state stationary
law and any closed form for0.246 remain open.

A cheap objection to "heal size is the wake only" if wake means damage bits:
initially flip just cell0, and set A_0(-1)=1. The mismatch at-1 next tick is0,
the mismatch at0 is NOT A_0(1), and the mismatch at1 is1. Thus A_0(1)=0 gives
heal size1, whereas A_0(1)=1 gives heal size2, with the same initial damage
word and the same black cell ahead. The reference state to the right matters.
Using the **joint** reference/difference wake avoids this ambiguity.

Likewise reuse alone is not a determinism theorem: A_0(0) and A_1(1) have the
same left foot, but the latter is A_0(0) XOR (A_0(1) OR A_0(2)). The first
observation need not determine the second. This is a counterexample to the
inference from foot reuse, not a counterexample to a separately proved
closure of the full front history.

Concrete route around the gap: define the retained wake state as a joint
reference/difference strip, specify its transition, and exhibit two compatible
deeper contexts with that same state before claiming closure. Alternatively
retain the exposed tail explicitly and seek a regeneration time at which the
required tail information can be discarded. Either is more discriminating
than another unconditional frequency census.

## 3. Two exact prose corrections

If J_(t+1)=F_(t+1)-F_t+1 is the recorded jump, then

`q_(t+1)-q_t = J_(t+1)-2`.

An advance J=0 moves the foot left2; a size1 heal moves it left1 and can also
reach a new minimum. The tracker says "only advances reach fresh feet", but
its own output has11310 fresh feet after size1 heals. Correct that sentence.
A size2 heal reuses the last foot; a size3 heal moves right1. Neither a
positive asymptotic left speed nor the word "front" makes instantaneous
velocity always point left: F moves by J-1 and can move right on a heal.

Also, the single-seed centre's left feet are -t, all distinct, rather than
"every foot the same cell". They supply no fresh randomness because those
initial bits are fixed white. A right-moving diagonal x=t-j does have one
fixed left foot -j. State which ray is meant; distinguish repeated location
from the absence of a random initial bit.

## 4. Source and measurement audit

`front_feet.py` computes q=x-1-t and updates its running minimum on **every**
tick from t=0, before retaining t>=T/4 observations. The output has90010
observations,62528 fresh and27482 reused. Its after-advance mixture arithmetic
is correct; deterministic size2/3 counts are correctly transcribed. No code
off-by-one correction is needed for those statistics. The left margin2T+100
is safe even at the maximal possible left speed. The right marginT+60 is not
a worst-case cone guarantee for an arbitrarily rightward front; the retained
output does not log max(x-1+t). Before treating every reused-foot frequency
as a whole-line measurement, retain that actual boundary guard. This is a
missing fidelity check, not an observed boundary failure. Fresh-bit fairness
itself still follows from left-permutivity with a fixed right boundary as
long as the relevant left ray stays inside the array.

The printed sqrt(0.25/n) is a nominal iid scale. Serially dependent reused
observations do not acquire calibrated confidence intervals from that formula.
Even for adaptively selected fresh samples, conditioning on their final
random count is not automatically an exact binomial experiment. The proof
supports a martingale analysis; no such confidence calculation was supplied.
Keep the numerical frequencies COMPUTED and the printed scales nominal.

`fake_coin_tells.py` has one realized initial row for each W, not a sample of
all seeds in that family. W=0 is explicitly the black singleton, whereas W>0
draws its seed cells. All five implementations and outputs were read; no
independent Berlekamp-Massey replay is claimed.

The written P-b2 requires max residue deviation<0.03. The retained output is
0.0322 at W=2,0.0391 at W=8 and0.0400 at W=128. Therefore **P-b2 did not hold
as frozen**. Record these three threshold failures alongside the retained
Rudin-Shapiro entropy failure. They need not imply a real statistical
distinction: one iid control, multiple tests and no ensemble calibration do
not establish significance. But that is different from passing the declared
test. The singleton does meet the stated finite numerical thresholds.

Nothing here proves that every useful next test "must" be rule-native or
that no generic test can separate the sequences. The concrete useful result
is that this one singleton prefix passed these five tests, while the named
automatic/register controls were detected. Rule-native tests remain a good
research pull, not a logical consequence of five unsuccessful tests.

Source pins (SHA256):

- front_feet.py: `f23deb9f510ec113ae923dc8d871ae5246c796a30c002d3acf8a681352d02695`.
- front_feet.out: `ff9cf0731e27983e5a489711ba9804275271c1bbe6c217c05c5e63f43b1d6d30`.
- fake_coin_tells.py: `ba2977feacf0fd6c3b2960be03dcc972b03ebf0369e00c87c1a2c0eb88b7e8e1`.
- fake_coin_tells.out: `1253803f5e2e55c3ccce40f1436f66c8ef0e92ad495ecfbf467117b8aee8f9ca`.

## 5. Status and next step

Fixed-trace triangularity and the **qualified adaptive fresh-coin claim**
are CARRIED by hand here. The original unqualified wake-only closure is
NOT SHOWN; the retained frequencies are COMPUTED, not rerun. The foot-motion
sentence and P-b2 blanket PASS need correction. No new compute dispatched;
visualizations remain held. Local's A3/A4 ownership is unchanged.

My own pull: a precisely defined joint wake and a regeneration criterion,
if this front route is resumed; the current owned next task remains B2.
