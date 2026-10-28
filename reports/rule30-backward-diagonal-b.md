# B's alternating backward diagonal

GC2016, 28 October 2026. Owner requests the diagonal x=t in B's ancestry and a visualisation comparable to
the white-right A view. This is separate from Local's current 2-adic cycle-lifting block.

Record searched: GC1981–84 complete first three ancestor generations; GC1998/GC2000 white-right selection;
L1046/L1048 exact periodic-tail inverse source; GC2015 vertical obstruction. No recorded all-depth result for
the backward alternating x=t path. No novelty claim.

## Frozen question and bounds

At time -k require U(-k,-k)=1-(k mod 2), starting with the root 1, B's hole 0, and the already observed 1,0.
Enumerate every predecessor right ray by cycles of the four-state period-composite inverse map, extend each
uniquely leftward, then filter at the requested diagonal cell. No clamped finite boundary or greedy branch
choice during the constraint search. Completeness follows from the existing periodic-tail inverse argument:
an infinite backward chain of a map on four states lies on a cycle; those cycles generate all parent rays.

Prediction: a further local obstruction may end the alternating trace; three successful steps give no evidence
of an infinite clock. Counterfactual: survivors through depth 512 establish only a finite compatible prefix,
not an eternal path. Stop at the first empty level, or at 512, 2,000 live branches, 20,000 total generated nodes,
or tail period 4,096. A resource stop is inconclusive.

Independent controls: reproduce counts 1,2,5,8; exact A/B rows; GC2015's vertical obstruction; literal Rule 30
truth-table checks over every generated finite window and at least three periods of its infinite right ray.
The A control must retain a black diagonal x=t throughout its white-right history.

Visual context: retain all rejected choices at the first failure. If failure occurs, continue one explicitly
UNCONSTRAINED B history to depth 512, choosing shortest right-tail period then lexicographic tail/window.
This permits viewing what a genuine past does after alternation fails; it must never be labelled a successful
periodic history. Generate the unique white-right A comparison, depth 512, and 64 common future rows. Display
x=-1600..320. Left-window truncation cannot affect inverse cells to its right; positive-time rows use an
expanded white initial window. Raw data remains outside git.

Single Intel worker under run_capped.py: 60 CPU seconds, 90 wall seconds, 512 MiB sampled process-group RSS,
8 MiB per file, 20 MiB total output; launch free+inactive 1,024 MiB, ongoing 512 MiB, swap growth 128 MiB.
No automatic retry or widening. Source backward_diagonal_b.py and this specification are published first.
