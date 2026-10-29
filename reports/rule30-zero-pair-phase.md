# Two recent start bits at a zero-doubling pair

GC2210, 29 October 2026. **PROOF-SKETCH, solo GPT.** This is an exact
conditional phase calculation using the known right-diagonal recurrence and
cycle-lifting criterion. It is not a density theorem or a new autonomous model.

## Pull and the cheap objection

GC2200/L1201 show that after110 the next doubling ignores two recent seed bits.
Is the same true after00, or does the two-bit choice have an explicit, different
form? The cheap objection is decisive: changing the older bit may change the
second0 itself. A comparison must first identify which choices keep00.
The useful outcome is a formula for that restriction and for the next flag,
with actual finite-seed interpretation. It would not make the root's fixed
bits into random choices.

Record searched: seed-echo/start-bit/phase-sensitivity and their complement,
initial-bit and overlap equivalents; GC2014/L1070, GC2200/L1201; actual current
kit932cf8dde039b89b1dcbe9636867bb1b2057fef0 lean/equivalents/catalogues and
listed portal/21open-PR source index (complete refresh22:47:13Z).
`TFunctionCycles.Phi_bit`, `lift_iff`, `Phi_cycle`, and the single-seed
`Rule30RightPeriods.S_rule` give the existing recurrence/lifting machinery.
The actual universal-start source3ca86f and PR54 head7a3f1d8dcf5f412041f52000ee5a057872547160
have different finite-start conclusions; no new claim about those statements.
GC2014 already proves the one-diagonal-delayed single-bit effect. The
two-bit affine expansion below is an elementary specialization, not novelty
clearance from a failed keyword search.

Primary background: Anashin–Khrennikov–Yurova,
[*T-functions revisited*, section2.4.1, Theorem2](https://arxiv.org/html/1111.3093v2#S2.SS4.SSS1)
states the classical triangular Boolean-coordinate criteria. Those are
bijectivity/transitivity criteria for entire residue spaces. They do not
assert fairness along the single-seed sequence of spatial depths. The kit
credits Klimov–Shamir and Anashin for its general cycle description; that
mechanism is reused here.

## Statement with the closure condition

Use addition and multiplication in F2. Let an actual finite seed have a right
edge at0, and choose j with common least PREFIX period

    Q_j = Q_(j+1) = Q_(j+2) = H,     H even.

Write a=D_j, b=D_(j+1), c=D_(j+2); thus the two growth flags are00.
All three are H-periodic, and Delta c=a OR b. The preceding full prefix,
through j, is held fixed. Flip the initial bit at depth j+1 by beta and that
at depth j+2 by gamma; hold all other seed bits fixed. Both parameters lie
in{0,1}. Write

    h(t) = SUM_(0<=u<t) (1+a(u)),     h(0)=0,
    alpha = SUM_(0<=t<H) a(t),
    B = SUM_(0<=t<H) b(t),
    A = SUM_(0<=t<H) [c(t)+b(t)h(t)],
    F = SUM_(0<=t<H) [b(t) OR c(t)].

The changed streams, for every time, are exactly

    b_beta(t) = b(t)+beta,
    c_beta,gamma(t) = c(t)+gamma+beta*h(t).

The first0 is always preserved. The second0 is preserved **iff beta*alpha=0**.
For those choices, the next growth flag is

    F_beta,gamma = F + beta*A + gamma*B.

If beta*alpha=1, the changed prefix has history01 instead, with period2H
after c. Its following growth flag, measured over that true2H period, is B.
The H-tick affine expression still gives an H-tick parity in this case, but
it is not the new prefix's next growth flag.

## Proof

The feeder of b does not use its own starting bit, so changing that bit
complements b at all times, without changing its period. Pointwise,

    (a OR (b+beta)) + (a OR b) = beta*(1+a).

Integrating the difference with the specified initial bits gives the formula
for c. Since a is H-periodic and H is even,

    h(t+H)+h(t) = alpha,
    c_beta,gamma(t+H)+c_beta,gamma(t) = beta*alpha.

The older prefix still has least period H. Hence if beta*alpha=0 the full
prefix through c still has least period H; otherwise c is antiperiodic at H
and the least prefix period is2H. This uses prefix periods, and does not
assume monotonicity of individual diagonal periods for arbitrary seeds.

For the next input, expand OR as x+y+xy. At a single time the difference is

    [(b+beta) OR (c+gamma+beta*h)] + [b OR c]
      = beta*(1+c+b*h) + gamma*(1+b) + beta*gamma.

The two beta*h terms cancel because beta squared equals beta. Summing over
the even cycle kills the standalone beta, gamma and beta*gamma terms,
giving F+beta*A+gamma*B. The known lift criterion turns this parity into the
next flag exactly when the changed prefix closes at H.

In the remaining case b_beta repeats after H and c_beta,gamma complements.
Pairing the two H-blocks of the next forcing gives NOT b_beta pointwise.
Its parity over H is B, since H is even and complementing b does not change
its parity. This proves the stated01 continuation.

## What is inherited, and what is not

The gamma coefficient B is precisely the carried GC2014/L1070 single-bit
effect. The beta coefficient includes the response of the intermediate
diagonal, so it is not obtained by complementing b while leaving c unchanged.
It can be written without c, since any H-periodic integral has

    SUM c(t) = SUM_(even t<H) [a(t) OR b(t)].

Thus A depends only on the full a,b profiles and the ordered prefix sum h;
the initial phase of c drops out. These profiles and their cycle length are
inputs, not a bounded-size spatial state. In the110 regime GC2200's stronger
antiperiod assumptions make the corresponding coefficients vanish. That
invariance cannot be transferred to00 without checking A and B.

If alpha=0, all four start choices keep00. An exactly uniform distribution
on those four choices would give a constant next flag when A=B=0 and a
balanced next flag otherwise. If alpha=1 only beta=0 keeps00; its two gamma
choices agree when B=0 and disagree when B=1. These are finite truth-table
counts under a declared choice distribution, not a probability law for the
one-black seed. That seed has its specified initial bits, not fresh coins.

## Hand control: a genuine closure failure at H=2

Take the finite seed with initial black cells0 and-2 (edge code5). Let j=1.
Then a=01, b=10, c=01 over H=2, time0 first; the prefix periods are all2.
Here h=01, alpha=B=1, A=1 and F=0.

With beta=0, gamma=0 gives next flag0, whereas gamma=1 gives flag1. With
beta=1 the second0 becomes1 for either gamma, so these choices must not
remain in a00 comparison. At their actual period4, the following flag is1.
For beta=1,gamma=0 the seed is the one-black seed: the known start has
periods2,2,4,8, matching this branch. This is a four-tick hand check, not an
asymptotic root inference. Dropping the even-H assumption would also be
wrong: the summed beta*gamma term survives for odd H.

## Exact next control, frozen before execution

Use only the retained GC2155 root words14..18 over256ticks, plus the hand
H=2 example. Retained `out.json` SHA256
fcdf3b5b6de5375a30a7f9ece88ab85d05eefcd1fa6c2087615012772fd9a3f0;
metadata `manifest-v2.json` SHA256
c5104e38bcd1b3b0ca9bff597ad50205fd06aa22142327005ca5bb7e8018129b.
The actual-root00 triple is a=D16,b=D17,c=D18. Its source multiplicity127
already implies alpha=0. No longer orbit or new seed sample is proposed.

Prediction P1: the exact phase formulas and closure classification match
independent literal Rule30 evolution for the four specified two-bit
perturbations of that fixed root prefix, and the four H=2 controls.
Counterfactual: retain the first mismatch, stop and repair the hand statement
before considering another computation. Prediction P2, deliberately tested
rather than assumed: the particular root256 triple has A=B=0, so all four
00 continuations agree. A nonzero coefficient refutes this proposed local
invariance, not the affine identity or the root's deterministic evolution.
Unexpected control: the H=2 beta=1 branch is excluded from00 and its next
flag is read over4ticks, not2. Also compare the ordered formula for A with
the even-tick formula eliminating c. No frequencies, random seeds, full
branching tree or phase census beyond these eight fixed cases.

Source [zero_pair_phase_check.py](../tests/probes/wolfram/zero_pair_phase_check.py),
SHA2568e32eb97fc57744a613d98014c81982617e2249628cb4e73c2ee3f9ce1f752b8.
Independent oracle is the literal8-entry Rule30 table on complete physical
rows: four fixed256-tick perturbations and four fixed4-tick controls,1048
row observations total. No search for seeds or least periods, no longer
horizon, no GPU or compiler. Existing input is read by its exact digest.

Intel prelaunch load1.95/2.04/2.08, about5829MiB free+inactive,225.25MiB swap.
One computing process/thread at nice10. One run_capped stage:120CPU/300wall/
768MiB RSS, tree/max3processes,4096MiB launch/3072MiB running free+inactive,
64MiB swap-growth stop,16MiB/file128MiB/stage. Internal wall stop240s.
The CPU limit applies to the sole computing process; supervisor/time overhead
is separately reported, not claimed as a hard aggregate tree CPU limit.
No concurrent heavy job; no reliable thermal reading. Monitor, pressure or
control failure stops the stage, with failure and cleanup receipts retained.
No automatic repair/rerun/widening. Data outsidegit with digests.

## GC2211 completed control and the remaining question

The sole stage ran at freeze3f362a06 on29October23:47:01Z and PASSED.
Both predictions held. All1048 literal physical-row observations agree with
the temporal formulas and the retained baseline words.

| Fixed case | alpha | A | B | F | Four next flags, beta/gamma order00,01,10,11 |
|---|---:|---:|---:|---:|---|
|Root D16,D17,D18; H256|0|0|0|0|0,0,0,0; all keep00|
|Finite edge code5; H2|1|1|1|0|0,1,1,1; last two have history01|

In the root case a,b,c each have128black ticks and b AND h has60, giving
the three zero coefficients explicitly. The four finite edge codes are1,
262145,131073,393217. They are four named perturbations of one retained
prefix, not a seed-frequency sample. In the H2 case codes5 and13 stay00;
codes1 and9 leave it. For code9 the first2-tick parity is0 but the correct
4-tick next flag is1: ignoring the closure guard gives an actual wrong label.

This is a COMPUTED implementation control for the hand PROOF-SKETCH.
It is not an independent carrying read and does not promote the universal
statement to PROVED, compiled or Lean Verified. The root case's phase
invariance is finite evidence, not a theorem that all00 extensions ignore
their recent bits. No all-depth coefficient law has been obtained.

Intel child0.12s wall/0.11s CPU, maximum resident set18227200bytes
(about17.38MiB). Runner0.54s wall/0.094s CPU. Launch5827MiB free+inactive,
225.25MiB swap. Finished before the first monitor sample: sampled maxima
are unavailable, not zero. Child receipt reports zero swaps; normal
completion, no remaining owned process, no retry or widening. Output/time
files total3877bytes. Immutable packet
`cited/gc2210-zero-pair-phase/manifest.json`, SHA256
`d1d78f9d4451a627f076c60475fbc4c96602c5d93ac871acaced88505a2c3e2b`,
retains exact source, results, time and normalized launcher with its original
digest. The earlier input packet remains separately identified above.

The phase calculation is complete at this scope. A further phase census
would not answer why the actual root's ordered coefficient has its value.
Reopen that route only with a root-compatible law for A/B or a recurrence
for a supplied whole component, not additional parity features. The fresh
primary-source pull is different: the T-function literature discusses
adjacent-coordinate relations under uniform differentiability modulo4 and
ergodicity. Before importing any such theorem, check those hypotheses for
Phi(x)=x XOR(2x OR4x) itself. Whole-space ergodicity already fails because
Phi preserves bit0; a restriction or conjugacy would need its own proof.
The first discriminating hand step is its difference quotient for a2^n
perturbation, including carries, followed by comparison with the paper's
exact regularity definition. No new computation is frozen for that step.
