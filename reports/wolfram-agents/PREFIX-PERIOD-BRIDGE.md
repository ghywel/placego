# Prefix periods supply the missing 11011 hypotheses (GC2118)

**GC2127 CURRENT DISPOSITION: known mechanisms reproved in a conditional interface; NO new portal/PR
extension.** Earlier public prefix-clock Lean/application and right-bounded half-rate source on PR51 has
been independently read. [Exact comparison, credit and scope](PREFIX-PRIOR-ART-REVIEW.md). The hand proof,
compiler result and outstanding full receipt clarification remain retained; old preparation below is history.

29 October 2026, GPT. **PROVED (hand, two-party L1142); source compiles Lean4.35 (L1144), actual outputs reviewed GC2125.**
Full parent enforcement-packet clarification remains pending; no submission-form/notebook/public delivery.
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

## GC2124: explanation prepared while the sole Local validation proceeds

[prefix-bridge-essay-prose.md](submissions/right-profiles/prefix-bridge-essay-prose.md) and its860-character
abstract draft now give the complete explicit prefix table, the proof, actual-world scope, essential p2
exception, known-lifting credit and limits. These are prose drafts, not native notebooks or accepted portal
fields. The old accepted essay/source/notebook are preserved; no new illustration is run.

Proposed delivery arrangement for Local's consideration after the actual compiler result: Local remains
sole poster/current-kit validator and GPT prepares the byte-preserving source assembly/prose. Prefer an
extension of the existing right-profile package/PR51 over a second competing copy, retaining all old
headline claims and adding the guarded whole-prefix/physical statements. Any expanded portal version should
clearly identify what it adds and how it relates to7d47a9; the exact public/replacement fields depend on the
current portal workflow and have not been selected or posted. No new PR, source transformation or checker
run is launched by this proposal. The only running/released compiler allocation remains GC2123's one Local
stage. Its actual parent receipt and outputs decide the next step.

## GC2125: actual compiler output reviewed, enforcement-packet clarification pending

L1144 reports the ONE released M5 stage COMPLETED/child0,5.23s,1039040KiB sampled owned RSS,4 processes,
launch6864MiB/min5884MiB headroom,swap growth0. Source/wrapper pins match, Lean4.35.0 is printed, the original
bridge compiler output is empty, all seven draft and six EXACT bridge names use only propext/Quot.sound,
and the weakened-modulus mutant has just the expected line90 eta diagnostic. GPT read the entire compact
receipt and all its retained output strings; replaying the receipt gate over those strings passes.
These are actual retained outputs, not the preceding synthetic fixtures. No Lean execution was repeated here.

The draft/empty-bridge/axiom strings match their three listed byte hashes. The mutant string does not:
its private path was sanitized to CAPPED_OUT; embedded-string SHA256 is
ca4079cd400844e55cb2f51e4c256b22fe040580f342813732b9bdfd308709d3,
while the listed output_sha256 is5c5420390a76d4b49fcfffacdb0d6f80f82f20f20f67a41bff480e5e48a2edaf.
This is consistent with original versus sanitized bytes, but the receipt must label those domains rather
than claim equality. No matching raw enforcement/output packet was found in workers/local's listing at
review. Local is asked to retain/share the full parent launcher/time/output packet privately, with original
and sanitized digests distinguished, and its actual start/end/cleanup fields. Do not rerun anything to repair
this documentation. Compiler semantics are accepted; independent full enforcement/byte-packet review remains
pending that clarification. Submission-form checker replay, a native notebook and public delivery still
have not occurred for this bridge.

## GC2128: full retained enforcement packet accepted; no further stage

L1147's MANIFEST e6dd2d974d748cf58668186218437f0a5beb2cfc31debfc1cca931836b9e6d2e now explicitly separates
original and sanitized byte hashes. All11 copied files verify against their sanitized hashes; untouched files
also match original size/hash. The original bytes of changed files and the two olean contents are not claimed
read. Exact original source/draft and exact three-binder mutant match; every compact output string equals its
copied actual file. The earlier mutant discrepancy is fully resolved as ca4079cd sanitized versus5c542039
original, not a compiler or proof discrepancy.

Full parent launcher/time/limits/gates/nine retained samples/inventory read: actual08:58:11Z–08:58:16Z,
COMPLETED/child0,5.23s supervisor wall,4.95s timed child,1.48s user/1.20s sys,691732480-byte timed-child
maximum RSS versus1039040KiB sampled owned RSS. Four owned processes,launch6864/min5884MiB headroom,swap
increase0,final1079049 bytes. These measures differ; no unique system-memory peak is inferred. cleanup=null
is consistent with the frozen supervisor's normal zero-leftover completion path, not a performed TERM cleanup.
All unchanged caps are within bounds. No rerun or binary-object revalidation occurred.

Immutable reviewed sanitized full packet:cited/gc2128-bridge-full/review-manifest.json SHA256
f4456b4a26ee3cd2b78fe4c57215da2e4c3474459e4781166614c686a30a4150.
This closes the evidence-domain request; GC2127's no-new-delivery disposition remains in force.
