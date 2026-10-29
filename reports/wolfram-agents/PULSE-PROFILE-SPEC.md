# Pulse-profile package: statement and scope preflight (GC2043)

29 October 2026. GPT preparation under the agreed L1082 split. This is a formalization specification from the
existing reviewed PROOFS24/25 results. It is not a compiled module, submission or novelty clearance.

**Record searched:** record_find.py 'pulse.*phase|source.weight|kick.landing' finds PROOFS24/25/28 and the later
GC570–573 extensions. Read the two original proofs and their second reads completely, and the landing proof and
its implementation. Extensions attached under entry24 have separate reader statuses; do not fold them into the
accepted base result. Current cached kit main932cf8dde039b89b1dcbe9636867bb1b2057fef0 has no matching pulse-profile
formula located. Its Rule30WhitePulse studies a black shield surviving boundary pulses and eventual neighbour
periodicity, a different assertion. Its Rule30Diagonals.D_step is exactly the profile recurrence below.

## One domain for the pulse identities

Use q-periodic Boolean words, a pulse B=e_s, and the child relation

    Child(A,B,C) iff C(t+1)=A(t) XOR (B(t) OR C(t)) for every t modulo q.

This is the LEFT-diagonal recurrence, not the right-edge XOR-integral recurrence. For an actual Rule30
configuration x define L_j(t)=evol(x,t,j−t). Literal substitution gives

    L_(j+2)(t+1)=L_j(t) XOR (L_(j+1)(t) OR L_(j+2)(t)).

This is the kit's D_step for the single seed, with the same direct identity for arbitrary x. Thus actual
periodic left-diagonal triples instantiate Child. The converse is not claimed: an arbitrary cyclic triple is
not certified to have finite-seed ancestry. Keep that missing physical-root bridge out of the headlines.

### Source weight: exact, including constant-word guards

A is uniquely recovered from B,C as A(t)=C(t+1) XOR (B(t) OR C(t)). Put E(t)=C(t+1) XOR C(t), and let weight count
black bits over one full cyclic word. If C(s)=1, then A=E. If C(s)=0, then A is E with exactly bit s toggled.
Consequently:

- if C(s)=1, weight(A)=weight(E);
- if C(s)=0 and C(s+1)=0, weight(A)=weight(E)+1;
- if C(s)=0 and C(s+1)=1, weight(A)+1=weight(E).

These natural-number forms avoid subtraction underflow in Lean. For nonconstant C, weight(E)=2r, where r is
the number of black runs around the cycle. This recovers all three cases of PROOFS25 and the heavy-source
corollary weight(A)>3 implies r>=2. The parity is weight(A) mod2 = 1−C(s).

Constant guards: all-white C gives weight(A)=1; all-black C gives weight(A)=0. Neither should be assigned one
black run in the transition-count identity. This specification keeps those cases valid rather than silently
extending the nonconstant run formula.

### The three-driver window: exact phase budget

For q>=4 and C neither zero nor e_s, let L in1..q−1 be the first positive distance from s to a black bit of C.
For Child(B,C,D), the unique periodic D has holes exactly s+1,...,s+L, and is black elsewhere.
A direct proof is short: away from s, D updates by C OR D. A black C away from s forces D to1; it stays1
through s. At s the pulse resets D(s+1)=0. It remains0 until C(s+L)=1 and then remains1 until the next pulse.
This also proves uniqueness: the black C away from s gives a reset value that propagates around the whole cycle.

For arrival T define delta(W,T)=1+the least nonnegative wait to a black W. The successive delays for B,C,D are
(k,L,1), with k=((s−T) modq)+1. Twice the maximum adjusted interval debt at slope5/2 is therefore

    max(0, 2k−5, 2k+2L−10, 2L−5).

Every interval is one of the six nonempty contiguous sublists or the empty list; intervals ending with the
last delay1 never improve upon the same interval with that last term removed. This explains why a mere sum of
all three delays would be the wrong observable. The displayed maximum is nondecreasing in k, so its maximum
over all arrivals occurs at T=s+1, k=q, and is

    2q−5 + max(0, 2L−5).

These are the reviewed PROOFS24 formulas with all halves cleared. Keep q>=4 and L<=q−1 explicit. The q8,k1,L7
case has interval debt9/2 but total debt3/2; the final low-delay edge cannot erase an earlier interval maximum.
No statement about frequency of pulse windows, other windows, birth clamps, total settling time or the centre
prize follows from this local budget. No joined-seven-driver extension is included in this package.

## Keep the kick result separate

PROOFS28's white predecessor condition is the direct local fact that when a cell is black its next value is
fixed by its left neighbour, irrespective of its right neighbour. The portal6827d2 already exposes the same
masking mechanism as center_black_blocks_col1 (the seed case). The stated56-phase landing window also uses
specific W values and even old/new phases. It remains valid reviewed mathematics, but neither a new general
masking principle nor a new asymptotic theorem follows from it. Do not manufacture a standalone finite
56-phase submission. Preserve it as a scoped explanatory corollary unless a genuinely additional general
statement and the current maintainer rules support a package.

The generic idea that a reset erases the starting state is standard automata theory. Primary-source check:
[Ananichev, Gusev and Volkov (2010), section1](https://arxiv.org/html/1005.0129v1) defines reset words precisely
as maps sending every state to the same state. This is background attribution, not a claim that their results
contain our exact Rule30 weight or interval-debt formulas. Full literature novelty remains unestablished.

## Proposed formal boundary and next action

Proposed module: Rule30PulseProfiles. Prove the Boolean source/toggle identities, cyclic transition count with
constant guards, pulse-child hole identity, and the exact three-delay interval budget for every q>=4. Include
the actual Rule30 left-diagonal instantiation, so an abstract profile theorem is not presented as a proved
finite-seed event. A finite horizon census is unnecessary for these arguments.

Local: review whether this is a coherent useful additional catalog contribution, particularly the left-diagonal
bridge and exclusion of the separately scoped birth extensions. The base pulse results retain their older
carrying reads; the assembled statement and current formal source still require a read before delivery.
GPT retains writing ownership. No build, experiment, pull request or portal upload occurred in this preflight.

## GC2044 — bounded compiler stage, written before launch

Initial core source: submissions/pulse-profiles/Rule30PulseProfiles.lean. Prediction: the source algebra,
signed pointwise weight correction, exact six-interval debt reduction/maximum, and literal left-diagonal
instantiation type-check without placeholders. Counterfactual: compilation fails or the kernel reports a
nonstandard axiom; retain the errors and revise the specific step. Cyclic summation/run count and the actual
periodic hole/delay identification remain separate missing theorems; an arithmetic budget with assumed k,L is
not their substitute. No randomized or physical census is planned.

Compiler-development envelope on Intel: at most3 separately retained compile attempts, each one Lean process,
20 CPU seconds,30 wall seconds,512MiB sampled process-group RSS,2MiB per file,8MiB aggregate output. Across all
attempts at most60 child CPU/90 child wall seconds and24MiB retained outputs; no concurrent compiler process.
Launch headroom1024MiB, ongoing512MiB, swap growth128MiB, standard run_capped.py. Revisions must correspond to
retained diagnostics and be committed before their compile. Stop on pressure/resource failure, or after the
third attempt; no automatic extension. The installed Intel toolchain is Lean4.33.1, invoked directly without
changing the default toolchain or installing software. This is a development check, not validation against the
portal's newer toolchain. It will require Local's current-kit cross-check later. Record searches and the primary
source comparison are above; this stage proves no novelty or numerical trend.

## GC2045 — first core compile passed; package remains partial

Frozen f0129f48 source compiled successfully on the first attempt under Intel Lean4.33.1.12 theorem declarations,
no placeholders/custom axioms/native evaluation. The source correction is axiom-free; the two printed arithmetic/
coordinate headlines use only propext and Quot.sound. The [source README](submissions/pulse-profiles/README.md)
records exact receipts and the remaining cyclic-count and delay-identification gaps. This is compiler progress,
not completion of the proposed pulse theorem or validation against the newer portal toolchain. No retry.

## GC2046 — cyclic source-weight extension, prelaunch compiler plan

Next obligation implemented: finite sums of transition bits telescope to twice the white-to-black count plus
an explicit open-end correction. Closing f(q)=f(0) removes that correction; a pulse toggles one source bit,
giving all three weight formulas and the heavy-source two-run corollary. Constant words are covered with zero
rising edges; the number of rising edges is the cyclic black-run count only with that convention. The source
uses Nat-indexed words with a seam equality, sufficient for these finite sums; it does not pretend to prove
periodicity from the equality of just two samples. The actual periodic pulse-hole/reset-delay obligation
remains unimplemented.

Prediction: the extension compiles and the new printed axioms are standard; counterfactual: retained diagnostics
identify an elaboration error or a missing arithmetic premise. Same record/prior-art searches as GC2043. A
separate diagnostic-driven development stage allows at most3 separately committed compile attempts, each
20CPU/30wall seconds,512MiB sampled groupRSS,2MiB/file,8MiB output, sequential total60CPU/90wall seconds and24MiB
retained output. Same1024/512MiB launch/ongoing headroom and128MiB swap-growth stop, run_capped.py. No attempt
is repeated after resource/pressure failure; no automatic widening. Installed Intel Lean4.33.1 only, with
Local's newer current-kit check still required. No physical census or empirical claim.
