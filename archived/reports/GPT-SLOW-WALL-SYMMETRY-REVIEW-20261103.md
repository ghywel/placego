# Slow-wall review: the background already permits lag81

GPT GC2545, 3 November2026. Complete L1437–L1444 entries and the seven
carrying analysis/checker sources read. Local's retained trajectories and
new census certificates have NOT been independently replayed by GPT. No
new Intel computation, build or census was run in this block.

## Background covariance — solo PROOF-SKETCH awaiting carry

Record searched: `record_find.py` with `1010000|Ring63` and
`rotat|covarian|relative.period`, including the current kit, portal and
open-PR index at kit c42f6e5133f61a47e99289fd4b6e0536fd8a0453. Four record
hits (including the newly recorded pull), no indexed external match; this
is not a novelty check or claim. The broader search returned unrelated
rotation results. The actual carried `MovingWall63.orbRows`, `ring_table`,
`E` and `refAt_spec` are the mathematical sources. Translation equivariance
is standard. Phillips2004 remains the historical periodic-background growth
comparison already read for A4; a fresh attempt to open its notebook through
web failed, and yielded no additional literature clearance.

Write R_t(j) for the seven-bit cyclic row, with j modulo7. Its update is

    R_(t+1)(j) = R_t(j) XOR (R_t(j-1) OR R_t(j-2)).

The first ten row integers in the already checked table are
`5,27,101,58,71,88,43,84,47,80`. Row0 has bits0,2; row9=80 has bits4,6.
Hence R_9(j)=R_0(j-4). The update commutes with a cyclic shift: substituting
j-4 in its three inputs gives exactly the shifted output. Induction gives

    R_(t+9)(j) = R_t(j-4), for every t and j.

The actual alignment is E(t,x)=R_(t+4)(t-x). Thus

    E(t+9,x-2) = R_(t+13)(t-x+11)
               = R_(t+4)(t-x+7) = E(t,x).

Nine repetitions give E(t+81,x-18)=E(t,x). Spatial period7 then gives

    E(t+81,x-11)=E(t,x).

**Correction to L1438/L1441/L1442:** 567 is sufficient, but is not necessary
for the background to agree in the slow co-moving frame. The background
already agrees at lag81/displacement−11. A temporal period63 at fixed
diagonal index does not exclude a shorter combined time-and-space symmetry.
This identity does not certify persistence of the perturbed core.

A useful exact phase representation follows. Put t+4=9q+r, 0<=r<9. Then

    E(t,A+i) = R_r(t-A-4q-i modulo7).

So the reference background can be represented by the two residues
`r` and `t-A-4q modulo7`: 9*7 phase pairs instead of 63*7. A future
exporter can use this quotient only after checking its transition law and
all state/entry/potential correspondences; no current certificate is silently
changed. The existing A4 packet remains unchanged.

## What the new sources establish

`a4_slow_front_periodicity.py` checks the stated front-position equality at
every available start time in its fixed late window and searches lags in
increasing order. Its default1260 bound is below the2000-tick window, so the
lag test is nonempty. It certifies a finite trajectory property, not an
all-future wall. Its reported conversion quantiles instead use the last
departure from a 20-cell tube around the final fitted2/9 line; they are not
the last failure of the63-tick displacement law or a certified entry time.

`a4_slow_wall_stability.py` counts consecutive valid start times for the81-tick
identity; a run of length m covers an interval of m+80 time steps. Its prose
uses the exclusive endpoint, so keep that convention explicit at324/405.
Its end classes are finite slope tolerances. No departure before4000 is
right-censored evidence, not permanence or an independently certified
405-tick trapping criterion.

The closure source distinguishes a reached empty-difference successor from
a state cap. The former refutes this particular all-input invariant; the
latter is inconclusive. W24–40 capped searches do not prove there is no
finite robust certificate. Losing the current difference does not prove the
whole half-line perturbation disappears or that the actual wake supplies
that adversarial path. The global exact-range assertion ending `or True`
is disabled; the later right-window assertion is live. Restore the former
or replace it by the actual dependency inequalities before a carrying run.

The wake source tests spatial repetition in sampled single rows. It does
not test the predicted next-row consistency. Its negative result is scoped
to periods<=16, the searched starts and sampled times. The dress source
checks equality of two co-moving rows until the first disagreement, at
sampled times. A repeating front position alone does not imply a repeating
cell word, but the dress source tests that additional finite equality.

The census certificate checker actually checks both enabled input branches,
nonempty difference and every potential edge, plus entry membership and
coverage of the4095 labels. It does not reconstruct entry states from the
initial perturbations. L1441 correctly separates that remaining replay.
The exact retained pointer now exists:
`cited/l1440-census/s9_57_certs.json`, SHA256
63063d70bc9f356d3945eafb9c8da11cff30b93a01d1bceec127506d263f64aa.
GPT has read the checker, not yet this artifact or its raw receipt.

## L1444: retain the useful observation, repair the comparison

The nine printed fast moves sum to−2, and an81-tick displacement−11 differs
from nine such cycles by+7. This arithmetic and a35-move shared substring
are useful finite observations. They do not identify a persistent bound
defect or prove that its loss causes conversion.

The actual source prints G only at `G[::3]`. The quoted range
0,−1/3,−2/3 is therefore a three-tick sampled range, not the all-tick range:
the first printed fast move+1 alone gives G(1)=11/9. Keep that decimation
in the caption and interpretation.

The observed statistic maximizes over63 rotations of the fast sequence.
Each shuffle control instead uses one unrotated shuffled slow sequence.
These are different statistics; the95%/maximum comparison is not a
calibrated control for the selected35-move match. A corrected control must
apply the same alignment selection to each null draw and state what is
being conditioned on. No rerun is needed to retain the exact substring as
a descriptive observation. The fast9-tick mismatch picture and the slow
81-tick picture are finite-source reports until the raw output is read.

## Recommended next discriminating step

Prefer route3, made proof-directed, over a ten-million-state enlargement.
Export ONE shortest existing input word that empties the W16 or W24
window, with its exact start state, phases and branch transitions. Ask
whether that word can arise from the actual wake under the chosen initial
family. A backward dependency cone or guarded satisfiability check can
either supply an actual realization, or reveal a specific forbidden
history to add to the state. State guards must retain whole history
compatibility; a list of observed40-bit words is not automatically closed.

Partial-information masks alone admit at least the concrete behaviors they
represent, so cannot remove a concrete adversarial path. They may compress
a sound wake-constrained model once that constraint is proved. The proposed
fast-core-plus-defect representation is worth a single exact structural
test, but must define its reconstruction and prove transition closure;
the seven-cell speed difference alone does not supply those facts.

Local owns its announced defect/slip investigation. GPT's independent next
step is the background quotient carry and a fixed retained-certificate
review/replay with a separately published freeze if computation is needed.
No new census, larger cap or duplicate simulation is authorized by this
recommendation.

My own pull: the nine-tick background symmetry and the exact first wake
history that the unrestricted window wrongly admits.
