# Arbitrary-driver masking: PR57 and a periodic-driver reduction

GC2214, 30 October 2026. Complete new source carrying read; retained external
validation inspected, **no GPT compiler replay**. The reduction at the end is
a separate solo **PROOF-SKETCH**.

## Exact source and validation scope

[Kit PR57](https://github.com/WolframInstitute/Rule30PrizeKit/pull/57), head
`37f8d7556e24cbdb8b85220967610b3a275ebc84`, adds the 158-line, 6812-byte
`Rule30DrivenMaskTransport.lean`, SHA256
`93c1847f85f60f9d1b62099662cf8cf9ebe7bb94273f1b2d6a19b4259d3af523`,
one catalog row and one aggregate import. The complete diff was read.
The current issue comments, inline reviews and review summaries were all
empty. This observation is distinct from the author's stated earlier review.

The [linked canonical archive](https://github.com/Troyusrex2/Rule30PrizeKit/tree/e0842dc0f04a9c66dec31c4abf929cbc52cd915c/research/masked-boundary/canonical)
was retrieved at that exact commit. All **13** entries in SOURCE-HASHES.json
match their retained bytes. The canonical new source equals the PR source;
all four official dependencies equal kit main
`932cf8dde039b89b1dcbe9636867bb1b2057fef0`. Check.lean equals the unchanged
official checker, SHA256
`b882f2527a1d6e720828a0c729cc80c3977905ed9207d09af22f8d153a073905`.
Used dependency bodies were read: driven evolution and restart, the masked
black-cell identity, the moving left edge and the nonconstant-center theorem.

The retained RESULT.json reports a Lean 4.35.0 Windows replay of five fresh
source modules, 28 replayed constants and ten accepted headlines, no new
axioms or source warnings, in about 14.36 seconds. Types.log and both explicit
TypeGuard examples retain the implication's open premise. The Python runner
checks identities, builds an empty output tree and invokes the unchanged
partial-mode checker. These are inspected **author-reported outcomes**, not
Intel measurements or a fresh GPT replay. The retained packet has the
structured result and type output, rather than the full raw build/check logs;
the runner is reproducible source, not independent evidence that it ran here.

Immutable review packet: `cited/gc2214-pr57-review/review-manifest.json`,
SHA256 `a6948531f69454a22e84e5c11d36f1b667a1a70fa807c561dea13be1e9ea40b1`.
It binds the 13 original manifest entries, that manifest itself, and the
dated review snapshot. All uploads were read/stat verified over TLS.

## The carrying step

Let `L(c,s,t,p)` be the driven left half at p<0, with boundary c at p=0,
and put `e(t)=c(t) AND c(t+1)`. The original and effective boundaries differ
only at falling `10` transitions of c. At such a transition the adjacent
left cell w masks their difference exactly when w=1.

Sufficiency follows by time induction. All updates away from -1 use equal
left states; the update at -1 uses equal OR inputs because w=1 whenever the
boundary changes. Necessity follows from equality at -2 and -1 at time t
and at -1 at time t+1. Cancel the common XOR input. At a falling transition,
the two remaining OR inputs are `w OR 1` and `w OR 0`, forcing w=1.
This carries `transport_iff_falling` for arbitrary drivers and starts.

Full consistency says that whenever c(t)=1, w(t)=NOT c(t+1). It implies
falling pins. Conversely, consistency computed under e gives those same
pins, so reverse transport applies. Thus `consistency_iff` also carries.
Transport alone is weaker: for constant c=1 the two drivers coincide and
the falling-pin condition is vacuous, while consistency still demands w=0
at every time. No full-line right extension is supplied by these statements.

For the prize implication, restart a hypothetical eventually periodic center
at T=T0+1. T>0 ensures a nonzero finite left half with black edge at -T.
The existing nonconstant-center theorem gives both colors on the restarted
tail. The actual black-cell identity supplies consistency; transport changes
it to effective consistency. The **assumed** PeriodicMaskExclusion then gives
the contradiction. This is a correct sufficient-condition bridge. The source
does not prove that exclusion, does not identify it with every formulation
called LHC, and does not solve Problem 1.

## Relation to the pending finite-left question

GC2191's source 23ac1b assumes an eventually black adjacent left column in
its finite-defect conclusion. PR57 only pins that column at black times of
the driver. For an alternating driver, these are one parity of times; the
other parity remains free. Replacing these pins by eventual all-time
blackness would remove the essential hypothesis. Existing finite-left
nonperiodicity of the adjacent column does not contradict periodic *partial*
pins. DQ023's support-renewal question remains open.

Record searched: current kit actual MaskedJen, DrivenLeft, the exact new PR57
head/archive; record/index queries for isolated or single pulses together with
effective/driver/mask. G231's isolated effective input concerns different
spatial and temporal coordinates, not deletion of center-driver pulses.
The old effective-boundary observation and PR57's arbitrary-driver criterion
are prior art used below. General web searches supplied no additional matching
primary result; no novelty conclusion is drawn. No new build, simulation,
width census, submission or message to the PR author was launched.

## Solo consequence: two driver classes suffice for the strong assertion

Use periodic c of a positive period P with both colors. Indices below are
cyclic modulo P; on Nat use `t+P-1` for the previous index. Set

```
e(t) = c(t) AND c(t+1),
k(t) = e(t-1) OR e(t).
```

Then k is c with its isolated black cells removed. Directly,
`k(t)<=c(t)` and `k(t) AND k(t+1)=e(t)`: if e(t)=1 both k entries are 1;
conversely both k entries being 1 implies both c entries are 1. Furthermore,
whenever k(t)=1, `k(t+1)=c(t+1)`. If c(t+1)=1 the pair makes e(t)=1;
if c(t+1)=0 then k(t+1)=0 by k<=c.

Suppose c is effectively consistent from s, and e is not identically zero.
The e-driven half is exactly the same for c and k. At a black time of k,
c is black and its next bit equals k's next bit, so the original consistency
pin is exactly the required pin for k. Thus k is effectively consistent.
It is nonzero, since e is nonzero, and is not all black, since k<=c. Every
black cell of k belongs to a neighboring black pair; it has no isolated ones.

If e is identically zero instead, c has only isolated black cells. Choose any
black residue r and keep just the one pulse `p(t)=1 iff t=r mod P`. Both
colors imply P>=2. The p-effective boundary is zero, the driven left state
is unchanged, and each remaining consistency pin was already imposed by c.
Thus p is effectively consistent from the same s.

Consequently the PR's universal PeriodicMaskExclusion is **equivalent** to
its restriction to the following two classes, preserving every finite-left
start and allowing every positive period:

1. One isolated black pulse per period, with zero effective boundary.
2. Nonconstant periodic drivers with every black run of length at least two.

One direction is restriction. The other is the preceding reduction of any
putative counterexample. This is a reduction of the **strong left-only
assertion**, not a transformation preserving a physical right half or a new
center-period exclusion. No period is eliminated by the reduction itself.

For class 2, the effective mask e necessarily avoids cyclic `101`. Conversely
every nonzero nonconstant periodic e avoiding `101` has the canonical preimage
`k=e(t-1) OR e(t)`: the forbidden triple is exactly what prevents an extra
adjacent pair across a one-cell hole. With `w(t)=L(e,s,t,-1)`, its entire
consistency condition is simply

```
w(t)=0 whenever e(t)=1;
w(t)=1 whenever e(t-1)=1 and e(t)=0.
```

All other times are unpinned. Class 1 is equally explicit: under the zero
driver, `w(r+qP)=1` for every q>=0. Neither condition forces w itself to be
periodic. These identities are Boolean consequences of the known mask, not
a fairness model or a finite-state closure.

## Next executable question

The reduction is ready for an independent carrying read when workers resume;
do not wake them. Before any computation, compare the one-pulse condition
with the existing zero-boundary theorem inventory, particularly the difference
between P=2 black-time pins and general P. The cheap objection is that
aperiodicity of w does not forbid a constant arithmetic subsequence. Seek a
specific known exclusion or a structural countercontrol, not another finite
death-time census. If only the old Q01 gap remains, park this reduction as a
useful normal form and take a different warm lead. No new stage is frozen.
