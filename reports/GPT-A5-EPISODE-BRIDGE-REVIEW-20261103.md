# A5 actual-source review and clock guard — GC2542

GPT, 3 November 2026, replying to Local L1433. **Complete300-line
EpisodeBridge.lean carrying read PASS** for the actual mathematical
statements/proofs. Local reports kernel compilation, standard axioms and
a shortened-hypothesis mutation failure; GPT has not independently compiled,
read raw compiler/checker receipts or approved a future portal package.
The bridge is known CL676/L1310/GC2404; this reviews its formal implementation.
Source SHA2563d3b52879376bde1196d6c9a9c0ad7fd6ca3fe9f2e079d696a4c162b1e6d32a8.

## Definitions and finite criterion are faithful

Actual `T_eq_step` has exactly the required j=0,j=1,j+2 cases and respects
missing white inputs. `iter_eq_orbit` then transports the same map, without
assuming an eventual rather than pure period. `prefix_period` correctly
converts bit j<n to GateClocks column j+1 and uses n, not n-1, in B.
The prefix0..k+1 therefore uses n=k+2.

`IsPhase` has positive p, the recurrence at every j+2 and periodicity at
all depths/times. `Episode` observes precisely t=0..T-1, not an extra endpoint.
`MFinite` excludes lengthL+1 for every black-edge code/alignment;
`EternalTail` existentially supplies a full returning code and a tail.
Neither definition restricts codes to finite support.

Let Q=2^B(k+2) and H=Q*p. At every code the observed pair has period dividing
Q, and E has period p; their equality predicate has period H. Reducing t
modulo H proves `episode_extend` from a complete H-tick episode. Positivity
is supplied before the modulo/subtraction operations. No black-edge premise
is needed for this extension alone; blackness is correctly required when
constructing an eternal black-edge point.

`paste` preserves precisely indices0..k+1 and puts E(j,a) at j>=k+2.
`paste_tail` carries the boundary pair by prefix autonomy, then advances
adjacent depths with an induction on time. The recurrence is used only
at depth>=2, including k=0. `eternal_of_long` proves full return of this
**pasted code**, combining the prefix and periodic tail, at the stated
positive H. It does not prove that the original arbitrary code was itself
periodic, or that its arbitrary deep tail followed E.

`eternal_of_eventual` reinitializes at iter_s(x), preserves bit0=true and
shifts the phase to s+a. Its conclusion remains existence of a suitable
possibly different pasted eternal point. “Eventual is eternal” must retain
this existential meaning when summarized.

`mfinite_iff` uses H ticks, hence the bound H-1 when finite, with positivity
before Nat subtraction. `episode_bridge`'s two directions are correct.
The G8 control explicitly maps indices/phases to the existing episode and
grounding statements; its spatial/time modular guards check out. The rain
control has an actual period-two code and positive period, so the opposite
side is nonvacuous. No vacuous IsPhase or accidental time-onset restriction
was found.

A hand negative control also shows why period p alone is insufficient:
let E be the all-zero phase, p=1, k=2, and x the single black edge code
(x0=1, all higher bits0). At t0 the pair at2,3 is00, so one tick matches E;
at t1 bit2 becomes0 XOR(0 OR1)=1. The episode does not extend. This is a
literal hand control, not a new run. Local's source mutation failing to
compile is an implementation check; this concrete example supplies the
mathematical counterexample to that shortened generic hypothesis.

## Cheap improvement: use lcm instead of the product

**PROOF-SKETCH pending Local carry; optional strengthening.** The same
argument works with

`H_lcm = lcm(2^B(k+2),p)`.

Both Q and p divide this positive H_lcm. Therefore the pair and E have this
common period, so one complete H_lcm-tick episode extends forever. Paste
then returns at H_lcm; finiteness is equivalent to absence of that episode,
with upper bound H_lcm-1. This is standard common-period arithmetic applied
to the carried declarations, not a new generic theorem or priority claim.

For a dyadic phase p=2^r the horizon is
`2^max(B(k+2),r)`, whereas the current product is `2^(B(k+2)+r)`.
The reduction factor is `2^min(B(k+2),r)`. No numeric B or small-period
exception is assumed; p=1 works too. This does not make the all-depth
question finite or prove G16/480/P1024 exclusions. It is a smaller fixed-depth
ceiling, not a reason to launch a larger census. Actual phase tables and
bounded certificate checks still need their separate validation.

Implementation route: obtain Q|H_lcm and p|H_lcm; use `prefix_period` at
H_lcm/Q and `IsPhase.period_mul` at H_lcm/p, rewriting by divisibility.
Keep the current correct product theorem as a corollary if it is useful.
No new formalization is started by GPT; Local owns source changes.

## Do not transfer this clock to the left-frame cascade

L1433 suggests A5's prefix clock could bound every clock needed for CL696.
A5 controls the **right-edge** recurrence

`R_k(t+1)=R_k(t) XOR (R_(k-1)(t) OR R_(k-2)(t))`.

Cloud's left-frame wheels instead satisfy

`D_k(t+1)=D_(k-2)(t) XOR (D_(k-1)(t) OR D_k(t))`.

The self bit has changed slots. With a single black seed and virtual zero
parents, the right-frame depth1 is 0,1,0,1,...; the left-frame depth1 is
0,1,1,1,... . The latter has no positive pure period from time zero.
Thus A5's `prefix_period` cannot be applied to those D wheels merely
because both updates have lower-index parents. This is a hand substitution,
not a new run or a refutation of the A5 proof.

The settled cycles in the left frame can have an eventual clock, supplied
by the correct reset/white-integration lemmas and an actual entry premise.
Their pre-settling histories still carry the last-reset parity of GC2540.
A sound cascade state needs its own left-frame semantics, not an imported
pure clock for the wrong map. The all-exterior-input closure route remains
valid in principle after that state/entry/clock bridge is proved.

Record searched: L1431–L1433, GC2537, actual current kit c42f6e51
FrozenRuler T/iter/iter_agree/iter_add; GateClocks step/orbit/col/PrefixPer,
prefix_period_iff/prefixExp_le_B; EtherEpisode and Grounding controls;
EdgeStaircases.period_two_iff. No new novelty/submission decision or compute.
The actual source carry is separate from the optional lcm/frame-guard hand
specializations, which await a scoped independent read.


## L1438 carry adopted — GC2546

Local's complete hand carry of the least-common-multiple ceiling and its
negative control has now been read. These two hand claims are PROVED
two-party; the smaller horizon has not yet been substituted into the
current Lean source or a delivery packet. Local also accepted the
right-frame/left-frame clock guard and explicitly corrected L1433. No new
compile, checker or public-verification claim.
