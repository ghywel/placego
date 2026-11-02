# A reset pair can recover an old bit on the next blocked step — GC2395

## Why this example

L1327 independently carries GC2393's two-open reset. Its proposed T47 measurement
of reset frequency and blocked imports belongs to Local. This note does not
duplicate it. It tests the stronger suggestion that frequent pair resets bound
the required history by one interval between resets. That conclusion needs a
guard on the deeper wake, since the reset only concerns the pair.

Record searched: GC2393's explicit map and warning about deeper imports; L1325's
distinction between shallow move reading and deeper state updating; L1327's full
carrying argument and proposed T47. This is a logical countercontrol within the
known Rule30 update, not a new novelty/submission claim or a sampled phase result.

Prediction before the literal check: two actual rows can have the same front,
phase and pair immediately after a two-open reset, then different pairs after
the very next blocked tick. The difference can encode an old pair bit, not just
an unrelated deep input. Counterfactual: if the whole future pair were fixed by
the reset pair alone, these two rows would stay identical in that observable.
Budget: two rows, three updates each; no search, new seed sample or long run.

## Explicit actual histories

Use depth increasing into the row and the usual edge-frame update
`Phi(X)_n = X_n xor (X_(n-1) or X_(n-2))` in the interior. Choose R>=8.
Let the reference row E initially have just one1 at depth R+5 and zeros elsewhere.
Use the same shallow boundary for all rows; it cannot affect the cells displayed
in these three steps. Let E evolve by the same rule.

For u=0 or1, let X initially differ from E exactly at R and R-3, and also at
R-1 when u=1. Thus its deepest mismatch is R, its trailing pair is (u,0),
and D_(R-3)=1 in both histories. These are complete deterministic row histories,
not separately chosen far inputs at successive times.

The background block at R-2 through R+3 is all zero, an instance of dc00zz with
c=d=z=0. Therefore two open moves put both fronts at R+4 and both pairs at (1,0).
The old bit u nevertheless survives in their third trailing bit:

`D_(R+1)(2) = u`.

Here is a direct hand derivation. Since the reference is still zero on these
cells, the perturbed values at time1 satisfy

`X_(R+1)=1, X_R=1 xor u, X_(R-1)=1 xor u`.

Consequently

`X_(R+1)(2)=1 xor ((1 xor u) or (1 xor u))=u`.

At time2, the background at R+2,R+3,R+4,R+5 is 0,0,0,1. The next tick is blocked,
and its advance is +1 for both histories. The two trailing bits at the new
front R+5 are

`(D_(R+4)(3), D_(R+3)(3)) = (0, 1 xor u)`.

Indeed the first is `1 xor (1 or 0)=0`; the second is `1 xor (0 or u)=1 xor u`.
The old pair bit is visible again after just one blocked tick, although it was
absent from both bits of the pair at time2. No row has been modified in mid-run.

Status: **PROOF-SKETCH** pending Local's carrying read; a literal six-update
self-check is supplied in [open_pair_memory_return_check.py](../tests/probes/open_pair_memory_return_check.py).
The reset used in the argument is already PROVED two-party (GC2393/L1327).
The six-update Intel self-check passed: both fronts follow R,R+2,R+4,R+5;
the time2 pairs agree, and the time3 pairs are (0,1) and (0,0).
No sample/horizon search was performed.

## Scope and the constructive way forward

This example does not claim that the displayed background block occurs in
P1024 or480, or that their actual prefixes fail to capture. It refutes the
unqualified inference from the *pair reset theorem alone* to loss of all earlier
information needed by later pairs. A phase-specific theorem could still exclude
this mechanism; that exclusion is a new hypothesis to establish.

Local can continue T47 as a useful finite measurement, but should keep two
quantities separate: number of blocked ticks between resets, and the age of
the data read at those ticks. A short interval does not by itself bound that
age. The concrete route is to retain the overlapping deeper blocks that feed
the next blocked transition, or certify that their relevant incoming dependency
has also reset. A full reset of that required finite block, with a sufficient
cone guard, would justify a finite-memory claim that a pair reset does not.

Next executable step: screen this mechanism against the actual retained phase
tables before any solver query; ask whether their legal reset-to-blocked words
force the incoming third bit, rather than treating it as a fresh arbitrary bit.
This is a question about actual allowed histories, not another generic class
census. Independent alternative: the already carried guarded wall-clause exporter.

My own pull: trace the returning bit through the wake. A bit can be erased from
our chosen two-cell observable while remaining present in the physical row.
