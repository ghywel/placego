# The far edge, the watched cell, and the first birthday

GPT, 25 October 2026. GC1886 / MI817. Owner-requested investigation of Local's L950 response to [DEEP-QUESTIONS.md](../DEEP-QUESTIONS.md).

## Answer in ordinary words

My warmest pull was Local's DQ-008: perhaps the watched cell is only reporting a decision made at the far end.

The far end really does have order. Its outer stripes obey a simpler, one-way recurrence, and the record already contains proofs that each fixed stripe eventually repeats. But the watched cell does not stay on one stripe until it settles. In this description it samples a newly introduced stripe at each step. Each sample is taken one step after that stripe begins at the boundary.

So the tempting argument, “the far end becomes orderly, therefore the watched cell must eventually follow that order”, lacks a step. It confuses knowing the eventual behaviour of each fixed stripe with knowing the early behaviour of an endless succession of different stripes.

A classroom analogy: every pupil eventually learns to read. That tells us nothing about the reading ability of each new pupil on their first day. We need a rule about first days, or about what successive pupils must share, rather than another theorem about eventual graduation.

This is a useful explanation of our obstruction, **not a new obstruction theorem**. RULE30-PRIZE.md section 8.84 already says that survival involves wall-born diagonals at age one. The investigation recovered that point in exact coordinates and connected it to Local's new question.

## What I take from Local's response

- **Keep the question about changing viewpoint.** The difference between the two inputs to the local rule is exact, and the latest trace-bit sensitivity is a real finite measurement.
- **Do not yet call the near end packaging.** The measured first free bit is a bit of the recorded wall history. Changing it while retaining the other selected history bits can change several starting cells. This does not isolate a disposable near-wall part of the row. The last free bit does correspond to the deepest single-cell flip; the two interventions are asymmetrical.
- **Restore the existing far-edge work.** The far edge has been described in sections 8.27, 8.30, 8.59 and 8.84. DQ-008's sentence “we have never described what the far end sends” is too broad. What is missing is a consequence strong enough to control every relevant fresh observation.
- **Keep the sample-to-theorem distinction.** L947's failed transfer rules out the tested frozen late-word selector. It does not prove that no finite doors can be labelled using any recent history. Nor do coin-like moments prove that every return-based argument can provide only averages.

These qualifications leave Local's questions alive. They change what their supporting evidence licenses.

## Hand derivation: where the observation sits

Work in the zero-boundary auxiliary problem, with depth increasing away from the wall. Let x(t,d) be a cell, x(t,0) = 0, and

    x(t+1,d) = x(t,d+1) XOR (x(t,d) OR x(t,d-1)),  d >= 1.

The tested condition is x(2n,1) = 1 for all n. A general prize exception and this auxiliary condition must not be silently identified.

Assume a nonempty finite initial row whose deepest black cell is at depth L. The deepest black cell at time t is at L+t. Indeed, the cell immediately outside the current support becomes black, because its near-wall neighbour is black and its other two inputs are white; all farther cells stay white. This is the known edge-speed fact.

Count stripes inward from that moving edge:

    a_j(t) = x(t,L+t-j).

Here j = 0 labels the outermost black stripe. Negative j are outside the support and have value zero. For j >= 0 the coordinate belongs to the half-line only when L+t-j >= 0. Whenever the next cell is strictly inside the wall, substitution gives

    a_j(t+1) = a_(j-2)(t) XOR (a_(j-1)(t) OR a_j(t)).

This is exactly the existing triangular diagonal recurrence. A stripe depends only on itself and the two stripes nearer the outer edge. The first stripes illustrate its order: a_0 is always 1; a_1 is 1 from time 1; a_2 is 0 from time 2. These statements follow by direct substitution, without a simulation. Existing proofs go much further and establish eventual power-of-two periods for each fixed diagonal, with the appropriate birth time included.

Now locate depth 1:

    x(t,1) = a_(L+t-1)(t).

| Physical time | Stripe sampled by the watched cell | When that stripe first appears at depth 0 |
|---|---|---|
| 1 | L | 0 |
| 2 | L+1 | 1 |
| 3 | L+2 | 2 |
| t >= 1 | L+t-1 | t-1 |

The samples relevant to survival are the even-time rows of this table. The sampled stripe changes each time; at every sample after time zero it has age one since its boundary birth. “Birth” is a coordinate description, not the creation of a new independent physical cause. In particular these stripes move away from the wall as they age; they are not incoming parcels that later arrive there.

The logical gap is therefore precise:

    For each fixed j, a_j eventually repeats

is not a statement about

    a_(L+t-1)(t) at all even t.

This is not fixed by showing that the eventual periods are small. One also needs control at the required time and for the required changing stripe index. Merely renaming the coordinates supplies no such control.

## The narrow claim behind “news always arrives”

There is a correct causal statement. Suppose two rows agree at every depth less than k, first differ at depth k, and have the same imposed boundary. Before time k-1 their depth-1 values agree; at time k-1 they differ. At each step the nearest disagreement advances one cell toward the wall, because the other inputs there are still equal and the differing input enters through XOR.

This establishes a first differing observation. It does **not** establish persistence of the difference, which row fails the survival test, or a constant time from arrival to failure. If k is even, first arrival is at odd time, outside the tested even-time observations.

**Unexpected control, already in the record:** the GC693 pair, with depth 1 written first and zeros beyond the displayed words,

    1100101 -> 01111011 -> 100010011
    1010011 -> 10111011 -> 100010011

first differs at depth 2. Its wall observations differ at time 1 exactly as the causal argument predicts. The complete rows then agree at time 2, so all later observations agree, including every constrained even observation. This is the already reviewed zero-wall fixture from GC1883/CL638, not a new experiment. It prevents us from turning “a message arrives” into “a lasting or fatal message arrives”. The older claim of a universal constant delay after arrival was also tested unsuccessfully in section 8.84; those finite examples do not themselves prove that every possible constant bound fails.

## The question I would carry forward

**Can the repeating structure farther out impose a restriction on successive fresh layers before they have time to settle?**

A more operational version is: **what must one fresh layer leave to the next if the watched cell is to keep passing its every-other-step test, and can a finite initial row keep meeting that requirement forever?**

There is already a local description of the requirement. At an odd time s, the next even observation is black exactly when the two nearest cells x(s,1) and x(s,2) differ, since the boundary is white. This is an exact restatement, not the missing global argument. It permits both pairs 01 and 10. We need a restriction on the succession of those alternatives that uses finite initial support and is stronger than repeating the original survival condition.

That is where this investigation stops. No quantity that must run out, well-founded descent, or closed finite description of that succession has been found. The existing settled-stripe results alone do not provide one. A new route would need to name the additional relation and test it against the existing merging and long-survivor controls. Another width census would not answer this conceptual gap.

## The owner's clarification of the zeta picture

The owner means the appearance of a drawn curve repeatedly looping back toward zero, rather than a proposed transfer of zeta-function theorems or a claim about the Riemann hypothesis. Our first translation into counting periodic orbits was too narrow.

The useful visual question is: **when a picture comes back to the same point, has the system returned, or has our drawing hidden something that changed?** A projection can revisit its origin while other information evolves. Without the particular plot we do not assert what its axes or zeros represent. The analogy can still generate questions about a useful observable, recurrent balance, or what is lost when a large state is drawn as a curve. Its visual origin should remain attached to the question rather than be replaced by a famous-conjecture connection.

## Evidence and disposition

Read Local L950 and all eight tracker entries at commit 50029784. Carrying sources read: RULE30-PRIZE.md sections 8.59 (including the birth-time audit), 8.60 (different, right-half orientation), 8.66 and 8.84; the [L942 outcome review](wolfram-agents/GPT-L942-INFORMATION-LOSS-OUTCOME.md); the [GC1883 review and fixture](rstation/GPT-CL637-AMPLIFICATION-REVIEW.md); and the [latest kit review](wolfram-agents/GPT-PORTAL-UPDATE-20261025-EVENING.md). The source of the L942 coordinate convention is the header of tests/probes/wolfram/death_info_loss.py.

No dynamics, census, GPU job or Lean replay was run. The old startup scripts rule30_wall.py and rule30_merge.py include computational enumerations; they were source-inspected, not rerun on the Intel review host, under the owner's current division of work. No fresh startup-check PASS is claimed. This block is source reading and hand reasoning. The coordinate calculation restates established results; no novel theorem or proof-status upgrade is claimed, and no held lane or schedule is restarted.

**Reasoned verdict:** the far-end question yields a precise missing connection between eventual order and fresh observations, and corrects an overly spatial reading of the measurement. **Gut verdict:** warmer on the question about successive fresh layers; cooler on expecting settled edge patterns alone to settle the wall.
