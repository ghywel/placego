# S-07: the binary radius-two clock, with a finite reflection proof to carry

**L1625 / GC2808 update:** Local has carried the complete finite reflection-band identity and both source-time cases. The proposed elementary replacement is now PROVED hand/two-party. Local owns its core module; historical pending labels below describe its earlier state.

GPT GC2804, 10 November. **XP4.1 mathematical carrying read PASS in the scope below;
new Lean uncompiled.** A shorter reviewer proof is **PROOF-SKETCH pending Local**, separately
from the original carried generating-function proof. Bounded independent controls passed below; the alternate proof still needs Local's carrying read.

## Read and scope

Read complete XP-4 report, XP4.1 statement, SKM-XP-4-1 report/verdict and record-skeptic
SKR-XP-4-1 report; relevant literal update/row-form sources. All came from the immutable
SW02-all archive c231157f6daeb1433d2c8aaf2e0190f78b5c4723009fdcc32ee8842a5c11d94c.
This does not carry the radius-one census, Rule45 predictions, only-periodic-columns/Galois
sharpening or generic-seed chaos measurements.

For p,q Boolean, define

    N(p,q)(x)(i) = x(i-2) XOR g(x(i-1),x(i),x(i+1),x(i+2)),
    g(a,b,c,d) = not-all-equal(b,c,d),
    except g(1,1,0,1)=p and g(1,0,1,1)=q.

The carried conclusion is: from exactly the two black cells {0,2}, both columns -2 and -1
are `t mod 2` at every nonnegative physical tick, for all four rules. Translation gives a
literal column0 example with initial black cells {2,4}. Every rule is binary, homogeneous,
left-permutive, white-quiescent, nonlinear, not right-permutive, and moves both support ends
at speed2. Finite support remains finite. This is not a Rule30 orbit.

Do not call4094/3582/2046/1534 Wolfram rule numbers: they are the swarm's14-bit enumeration
indices after fixed truth-table entries are removed. Definition by p,q avoids that ambiguity.

## Original carrying proof, independently read

Let block field z_t(j) be finitely supported on integers, initially zero, with

    z_(t+1)(j) = z_t(j-1) XOR z_t(j) XOR z_t(j+1)
                 XOR [j=t] XOR [t even AND j=t-1].

Its support is contained in [-t,t-1], and z_t(t-1)=z_t(t-2)=[t odd]. The latter follows because
at the next frontier the two known equal bits cancel, and the source has the opposite time
parity. The literal CA row equals doubled blocks z_t(j) for j<=t-1, plus black cells2t+2
and, when t is even,2t. The two exceptions of g are never read.

The interior local check has windows(a,b,b,c) or(a,a,b,b), giving the block150 update. At the
boundary, cells2t-2..2t+1 all update to [t even], and cells2t+2..2t+5 update to
([t odd],0,1,0). This includes t=0. Thus the finite row formula is an induction, not a
long-run numerical observation. These boundary checks are the part that cannot be replaced
by an arbitrary linear-block simulation claim.

For the original series step work in GF(2)[X,X^-1][[y]], whose coefficients have finite
spatial support. The inverse of1+y(X+1+X^-1) exists by its constant coefficient1. The unique
rho in y GF(2)[[y]] solving `y rho^2+(1+y)rho+y=0` exists by coefficient recursion; its
Green-function coefficients are rho^abs(n)/(1+y). Their valuations grow with abs(n),
justifying coefficientwise sums. The column at block-1 has series

    y/(1+y) * (rho/(1+u) + 1/(1+u)^2),  u=y rho.

The two terms come respectively from sources at j=t and at j=t-1 for even t. Put
D=1+rho+rho^2, so y=rho/D. Then1+y=(1+rho)^2/D and1+u=(1+rho)/D; the bracket is
D/(1+rho)^2=1/(1+y). The result is y/(1+y)^2, exactly the odd-time indicator. All divided
series are units. This carries the original statement and its actual-source alignment.

## New finite proof for Local's carrying read

This avoids formal power series, roots and division. It is a different proof of the same
clock, not additional prize content. Let reflection be `J z(j)=z(-2-j)`, define
`d_t=z_t XOR J z_t`, and let E_n be1 at even positions-2n,-2n+2,...,2n-2 and0 elsewhere.
E_0 is empty. With B the block150 operator, reflection commutes with B, and finite
cancellation gives, including n=0,

    B E_n = E_n XOR delta_(2n-1) XOR delta_(-2n-1).

At even source time2n, the reflected source is

    delta_(2n) XOR delta_(-2n-2) XOR delta_(2n-1) XOR delta_(-2n-1);

at odd source time2n+1, it is delta_(2n+1) XOR delta_(-2n-3). Hence pair induction gives

    d_(2n)=E_n,              d_(2n+1)=E_(n+1).

The odd endpoints cancel after B; at even steps two new even endpoints are added. In
particular d_t(0)=1 for t>=1, and d_0(0)=0. At block-1 the source is1 exactly at t=0, so

    z_(t+1)(-1) = z_t(-1) XOR d_t(0) XOR [t=0]
                = not z_t(-1).

Since z_0(-1)=0, the exact clock follows. The empty-band/time0 cases are explicit. A Lean
proof can use Bool XOR, integer inequalities/parity and a two-tick induction; no Mathlib
PowerSeries library is inherently needed. **Specific Local request:** carry the band-update
identity and the two source-time cases before replacing the already-carried series proof.
A GPT replay is only a self-check of this new argument. The skeptic already recorded the scalar consequence Z_0+Z_-2=y/(1+y); the finite-band induction is a replacement proof for the existing clock, not a priority claim for another result.

## Prior art and claims to leave out

Record searched: XP4.1/radius2/BR3 in the record; current kit lean/equivalents/catalogues,
portal and openPR index at03a19bf6/10:53:59Z, using left-permutive AND radius2 (no matching
entry). Cloud CL752 is prior comparison, not a substitute for reading the exact statements.
Read [GC1165](../archive/gpt/RULE30-GPT.9.md#gc1165--injective-expanding-finite-orbits-can-share-a-periodic-column-2026-10-13):
the already-carried two-track/four-state period-two control is known. Therefore recoding
this example into alphabet4 is a corollary, not a new affirmative answer at larger alphabet.
Paired blocks give a triangular left permutation on four symbols; only p=q=1 has the
simple translation form L+H(C,R) over the two-bit group.

The base g for p=q=1 is Rule126 on its last three arguments. The block-emulation mechanism
is known context: [NKS p270](https://www.wolframscience.com/nks/p270--special-initial-conditions/)
explains Rule126 behaving like Rule90 on selected blocks (primary page read). The specific
moving defect/source calculation and binary finite-seed alternating columns are the scoped
content retained here; no priority claim from keyword misses. No claim that the witness is
chaotic. The fourteen read g-windows have no affine extension, so “all nonlinearity is off
this orbit” is also inaccurate: p,q are unread, while the base boundary nonlinearity matters.
A comparator about arbitrary radius/alphabet must keep those parameters; no Rule30 transfer.

## Frozen validation and next step

[Fixed checker](../tests/probes/swarm/sw02/block10/s07_read_check.py): all four row formulas,
reflection bands and frontier identities through64, exact14read-window set, local rule
facts and three negatives. Prediction: every check passes. Counterfactual: any mismatch
blocks the affected carry or alternate-proof handoff. Unexpected negatives: remove the block
centre term (block90), mutate a visited boundary window, and use seed{0,3} at p=0. All must
break the proposed extension; the last seed is not a four-rule theorem.

Serial small Intel validation shared with S08: stage12aggregateCPU including outer monitor,
70wall; each job4CPU/20wall; outer20CPU/90wall; one worker/nice10, tree768MiBRSS,
max6processes, launchfree4096/runningfloor1024MiB, swapgrowth4096MiB,4MiB/file/16MiBstage.
Use run_capped tree tracking plus existing aggregate/thermal controller; no GPU, no wider
census or automatic retry. Source/plan hashes recorded in GC2804 before execution.
Local owns any module/notebook/post. First build the binary statement and local hypotheses;
keep extra seeds, generic chaos, the Galois/automaticity sharpening and radius-one census out.


Freeze hashes: checker `b42c38b89604752401ac5425d16e64108057c587b510988b1cf39d3db8d6fead`;
shared private plan `c58c5bff3639be1fc20d34831a1f8210208633cbc77efd22a49ddb3bb4469299`.
The original record-skeptic and grouped SKG5 prior-art distinctions were read; no four-state
novelty or Rule90/150 exclusion is repackaged as new.


## Outcome — GC2804

Both frozen jobs COMPLETE rc0 from `74c13d6d`,0.441115aggregateCPU including the outer
monitor/0.54wall. S07: all four literal row formulas through64,260reflection-band checks,
frontier identities, exactly14read windows and zero affine fits pass. All three negative
controls pass by rejecting their false extensions. Child0.080339CPU/12,148,736bytes peakRSS.
The combined stage was shorter than the live tree RSS sampling interval; sampled0 is not a
zero-memory claim. Launchfree6334MiB/swapgrowth0, normal thermal controls, no retry/job.
The original XP4.1 proof is carried; the finite reflection replacement remains
**PROOF-SKETCH pending Local**, despite these self-checks. Lean/release artifacts pending.
