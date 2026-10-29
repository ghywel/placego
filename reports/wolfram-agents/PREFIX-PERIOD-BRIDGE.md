# Prefix periods supply the missing 11011 hypotheses (GC2118)

29 October 2026, GPT. **PROVED (hand, two-party L1142) for the explicit bridge; prepared Lean source UNCOMPILED.**
The original five-step hand theorem was independently carried in L1063/GC2010. This note makes its
prefix-period interface precise, rather than claiming a second discovery of that theorem. Local has the
reset/exact-information triage (L1140); GPT takes this separate remaining letter-Q bridge. No run, notebook,
portal upload or independent second read of this new source is claimed.

The pull is a small gap in our delivered right-profile package: it assumes complementary profiles, whereas
the hand result starts with letters recording growth of the whole prefix. Can we connect them without
silently assuming monotonicity of individual diagonal periods? Yes: minimality of the *prefix* is enough.
The useful outcome is an actual-Rule-30 corollary with explicit prefix-period hypotheses, not a stronger
asymptotic bound or an ancestry/occurrence claim.

## What was already known and examined

Record searched: record_find.py `11011` + `prefix period`; complete
[the five-step hand report](../rule30-five-step-period-bound.md),
[the delivery specification](RIGHT-PROFILE-DELIVERY-SPEC.md), and the actual delivered
[RightProfilesDraft source](submissions/right-profiles/RightProfilesDraft.lean), especially
`running_shift`, `shift_law`, `eta_false_of_antiperiod`, `rightDiag_step`, and `rightDiag_shift_law`.
The public 7d47a9 source explicitly says its finite-seed letter bridge is not formalized.

Fresh complete known_find --new: portal updated 08:32:26Z, public kit main
932cf8dde039b89b1dcbe9636867bb1b2057fef0. Its only additions since 07:48 were our ring entry/source,
already independently examined GC2116. Actual kit `equivalents/Rule30Equivalents/TFunctionCycles.lean`
`per`, `per_eq_two_pow`, `lift_iff`, `Phi_bit`, `Phi_cycle` provide known triangular cycle lifting.
`lean/Ruliology/CellularAutomata/Rule30RightPeriods.lean` `no_three`, `S_rule`, `inp_least_period`,
`per_mono_all` concern the single seed. We do not transport its individual-period monotonicity to an
arbitrary seed. Literal temporal-word 11011 hits have different objects from doubling letters.

Primary-source comparison: [Nersissian, 2609.25077v1](https://arxiv.org/html/2609.25077v1), section 3.2,
Theorem 8 and its proof use prefix maxima and doubling without assuming individual monotonicity; these are
background, not our novelty. The paper's section 4 reset criterion uses the other oriented recurrence and
is not substituted for this XOR integrator. Its text has no literal 11011 match. This targeted comparison
and the kit/portal searches do not prove absence from all prior literature. The already known half-rate
single-seed bound is stronger than our old three-fifths bound; no best-bound claim is made.

## The bridge, by hand

For profiles D_i(t), let PrefixPer(n,p) mean that every i <= n repeats after p at every t >= 0.
Let LeastPrefix(n,p) mean p > 0, PrefixPer(n,p), and p <= r for every positive common prefix period r.
This definition does not presume the existence of such a p for an arbitrary world.

Assume the triangular recurrence

    D_n(t+1) = D_n(t) XOR [D_(n-1)(t) OR D_(n-2)(t)],  n >= 2.

Suppose p > 0, PrefixPer(n-1,p), and LeastPrefix(n,2p). The forcing is p-periodic, so the existing
running_shift gives a single bit kappa, independent of t, with

    D_n(t+p) = D_n(t) XOR kappa.

If kappa=0, the old prefix and new diagonal both have period p. Thus the entire new prefix has period p,
contradicting its minimum 2p > p. Therefore kappa=1: D_n complements after p. We did not need the old
prefix's period p to be minimal, a divisibility theorem for periods, or any assertion about the new bit's
own least period. This is the whole carrying step.

## Explicit 1101 closure and the forbidden fifth doubling

Let k >= 2, p > 0, and p divisible by 4. It suffices to assume these five facts:

| Prefix through index | Required fact |
|---|---|
| k-1 | has common period p |
| k | least common period 2p |
| k+1 | least common period 4p |
| k+2 | has common period 4p |
| k+3 | least common period 8p |

The plateau assumption need not be minimal. Put q=2p and

    d=D_k, a=D_(k+1), b=D_(k+2), c=D_(k+3), z=D_(k+4).

The bridge gives d(t+p)=NOT d(t), a(t+2p)=NOT a(t), and c(t+4p)=NOT c(t).
The prefix hypotheses give period 2p for d and period 4p for b. These are exactly the previously checked
shift-law hypotheses. Because q is divisible by 8, the checked eta_false_of_antiperiod gives eta(q,d)=0.
Consequently z(t+8p)=z(t). The old prefix through k+3 already has period 8p, so appending z closes the
entire prefix through k+4 at 8p. Its least period cannot be 16p.

Thus an actual least-prefix pattern p,2p,4p,4p,8p,16p is impossible under these guards. For a normalized
finite seed with its known pure dyadic prefix periods, this is precisely the guarded 11011 exclusion.
The explicit theorem is broader in initial-world scope but conditional on the listed periods; it neither
constructs them nor proves occurrence of a profile or letter sequence. It has no center-column conclusion.

**Counter-control already in the record:** p=2 cannot be admitted. The single seed has prefix periods
Q_2,...,Q_7=(2,4,8,8,16,32), a genuine 11011. Here q=4 gives eta=1 instead of 0. This retained exact
example is enough to reject removal of the modulus guard; no new census is needed. Our proof never
excludes that case. A further cheap objection is an individual period drop: nothing in the argument forbids
one, because every closure/contradiction uses the whole prefix.

## Prepared source and next gate

[PrefixPeriodBridge.lean](submissions/right-profiles/PrefixPeriodBridge.lean), SHA256
6eac3d793e56b0b37d94065d173592e71cab25dd5763369b6df0d1e390c4e2bd (6429 bytes), contains
PrefixPer/LeastPrefix, prefix_append, antiperiod_of_minimal_double, prefix_1101_closes, no_11011,
and actual_no_11011. The physical wrapper unfolds D_i(t)=evol(x,t,t-i), with the Nat/Int subtraction guard
n>=2 proved explicitly. Import RightProfilesDraft is a staging dependency, not a claim that the current
public kit already contains that module. The source has not been elaborated, and no compiler/kernel
acceptance is inferred from the old profile package.

Local's requested carrying read: does minimality of the *whole prefix*, as used above, suffice at every
application, and do the five rows/index shifts produce exactly the existing q=2p shift law? Please compare
the actual source and the p=2 counter-control. After that read, agree a single small current-toolchain
validation with exact inputs and resource caps frozen first. No test, scope widening or submission is
requested by this note alone. The all-depth cascade, generic-seed resource parametrization, kick/fringe
candidates and reset triage remain separate unfinished obligations.

The delivery block has made concrete progress (ring independently public-verified, arc artifact released,
this exact bridge prepared); there is no repeated failed mathematical candidate to justify a census or
an automatic rerun. The next step is a short independent proof/source read, not another empirical trend.


GC2123: Local L1142 has now read the actual source, all minimality/index/eta applications and the cast guard;
the hand step is accepted. GPT in turn accepts Local's single-stage compiler plan with the receipt guards
strengthened in the right-profile RUN-SPEC. Local is sole runner after reading/adopting wrapperf0788d3c.
The source hash remains6eac3d79; its creation-time comment about the pending read is historical. No compiler
result is claimed before the actual receipt. The known lifting step is also recorded in PRIOR-ART as known,
reproved here; the additional object is the explicit whole-prefix/physical11011 formulation.
