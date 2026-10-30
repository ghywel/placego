# Two finite inverse steps: sixteen states and period-three gap counting

GC2298, 30 October2026. **PROVED, two-party hand read L1238** for the two-level
boundary machine, gap law and fixed-mass quasipolynomial claims. The control stage was frozen at GC2298 and passed once at GC2300;
its exact outcome and limits are below. Neither this result nor its experiment is added to Package B.

## Pull, comparison and scope

GC2296's population identity counts one-step parents without preserving run
lengths. The next question is whether symbolic gap lengths remain finite-state
for a second step. The cheap objection is that their exact unbounded lengths
could matter. Composing two copies of the known inverse gives a16-state
answer: zero gaps beyond length2 need only their residue modulo3.

Record searched: GC2291's inverse pair monoid, GC2296, G121/G122/L077,
the physical-versus-wall parent comparisons in GC2282, and actual kit
`Rule30Equivalents.Preimages` at a6399ef15ff409d4dc0c5feb119b289aa31588a4.
Its `leftPair`, `extendLeft`, `eq_of_evol_one_eq_of_right`, `preimage_white`
and `eq_third_of_evol_one_black` already supply the inverse rule, uniqueness
and white/black-tail mechanisms used here. The current21:44:30 complete
index has69portal entries/17openPRs. PR47/PR52 are gate-future closing
statements, not these white-exterior physical finite rows. Portal9460e3's
`rule_preimage_count_balance` counts local triples, not finite ancestors;
its title is not a matching theorem. No renewed priority claim follows.

Karttunen's2016 [OEIS A269162](https://oeis.org/A269162) already defines the
unique finite partial inverse, paired with the finite map A269160. Finite
transducers, geometric series and rational counting are standard tools.
This account makes a concrete two-level machine and its gap-period bound
explicit; it does not claim discovery of finite inversion or regularity.

## The machine and exact boundary

Write y=F(p), p=F(q), with all three rows finite and nonzero. Scan y from
right to left. Immediately before reading y_i, keep the state

```text
(a,b,c,d) = (p_i,p_(i+1),q_(i-1),q_i).
```

For input e=y_i define A=e XOR(a OR b), C=A XOR(c OR d), and update

```text
S_e(a,b,c,d) = (A,a,C,c).
```

This is precisely the two equations for p_(i-1) and q_(i-2). For a target
whose support runs from L through R, the right state is0000: a finite
parent ends at R-1 and a finite grandparent at R-2. After reading the entire
target down through L the state is again0000. Conversely, starting with
white right tails and ending0000 reconstructs both rows, and S_0(0000)=0000
continues both as white to the left. Every local equation, including those
outside the target support, holds. Nonzero y excludes a zero parent or
grandparent. Thus the machine accepts exactly the nonzero finite targets
with two finite past steps, after imposing the nonzero target domain.

There is no ambiguity from a nonzero state that eventually becomes0000
under further zeros. S_0(a,b,c,d)=0000 forces a=c=0, then b=d=0. This
checks the stopping boundary independently of a finite-width oracle.

## A zero gap has preperiod two and period three

For e=0 the first pair follows T0(a,b)=(a OR b,a):

```text
00 -> 00,    01 -> 10 -> 11 -> 11.
```

If that pair starts00, every generated A is0 and the second pair follows
the same T0, becoming fixed within two steps. If the first pair is nonzero,
every generated A is1; it reaches11 within two steps. The second pair then
follows T1(c,d)=(NOT(c OR d),c) at every step, from the very first one:

```text
00 -> 10 -> 01 -> 00,    11 -> 01.
```

Its three-cycle is entered within one step. Therefore, on all16states,

```text
S_0^(m+3) = S_0^m for every m>=2.
```

The threshold cannot be replaced by1 on the full state space: first pair01
becomes10 after one step and11 after four, regardless of the second pair.
This period3 is the known all-black predecessor tail appearing inside a
composed white-tail inverse. It is not a new temporal clock of the root.

## Exact counting representation

A normalized K-black target is uniquely specified by its K-1 zero gaps
g_1,...,g_(K-1), read in spatial order. Its membership is the finite matrix
product of K copies of S_1 and the intervening S_0 powers, applied from the
right. Replace each zero-gap power by one of five classes:0,1,2,3,4,
where a length g>=2 is replaced by2+((g-2) mod3). The corresponding width
series are respectively

```text
1, z, z^2/(1-z^3), z^3/(1-z^3), z^4/(1-z^3).
```

Sum the products for those class words that take0000 back to0000, then
multiply by z^K. This is an exact finite expression for the width generating
function at fixed K, without truncating a long gap or enlarging a seed sample.
It is not necessarily a minimal-state representation.

Every nonzero finite image begins11. Hence every accepted word has g_1=0,
eliminating one possible denominator. In fact a second image begins110,
since its parent begins11, but that extra restriction is not needed for the
following bound. For K>=3 the generating function has denominator dividing
`(1-z^3)^(K-2)`. Its coefficients are eventually quasipolynomial in width,
of period dividing3 and degree at most K-3. “Quasipolynomial” means that on
each residue class of width modulo3, one fixed polynomial eventually gives
the count. This follows directly by expanding the finite rational expression.

As a hand control, GC2289's three-black classification gives precisely
`z^5/(1-z^3)` for two finite past steps: one target at widths5,8,11,...,
none at other widths. Thus a single width-independent leading constant
cannot replace the residue classes even at K=3.

This counts two past steps only. It neither bounds all ancestral ages at
fixed mass nor solves the all-depth residue problem. Higher-depth inverse
composition is possible, but no automatic machine expansion is authorized.

## One frozen interface control, not a census for a new law

Source: [finite_two_past_control.py](../tests/probes/wolfram/finite_two_past_control.py),
SHA256`ce628f04fb5aef7e5e4b92975ec80e027ccde8b3c663c9c016b13d4a65366b7b`.
Only Python's standard library; source digest checked before work and copied
to the stage receipt. No compiler, solver, GPU or child research process.

Prediction: the16-state identity above and the exact two-step membership
agree with independent forward images on every normalized target of widths
1through12:2048targets total,512with one past and128with two. The prior
one-step fixed-mass formula matches those controls. The literal111has one
past but not two;11001has two;11has none. Zero is outside the domain.

Counterfactual: any mismatch, source/monitor failure or limit stop fails this
one stage, preserving evidence. No retry, threshold change, larger width or
mass enumeration follows. The direct oracle uses the literal eight-entry
Rule30 truth table; its bit orientation is separately checked against the
known integer formula. The16-state machine uses the inverse XOR/OR equations.
The fixed oracle enumerates all parents through width10 and grandparents
through width8; known endpoint growth makes these exhaustive for the target
fixture, not an assumption that larger ancestors are absent.

Unexpected controls: preperiod1 must fail at state0100;0000must have no
other zero-input predecessor; changing the grandparent's right boundary to
0001 must cause a disagreement. These test the temporal/spatial offset and
the white-right hypothesis, rather than merely replaying the implementation.

Intel8physical/16logical,16GiB. At21:59UTC free+inactive was6426.5MiB,
swap used161.25MiB, speed/scheduler limits100,16CPUs available and no recorded
thermal/performance warning. Process inspection found no competing research
job. This stage is one single-threaded Python worker at verified nice10.

Launch once with run_capped.py:120s per-process CPU backstop,300s wall,
768MiB sampled tree RSS,16MiB/file,128MiB stage disk,4096MiB launch
free+inactive,3072MiB running floor,64MiB swap-growth stop, tree tracking and
at most4observed processes. The worker separately stops at110aggregate
CPU seconds (self plus all reaped diagnostic children) and280wall seconds,
checked at least every128target cases and each width. The only children
are serial pmset reads, each with a5s timeout; there is no live compute child
omitted from the sum. Outer supervisor/time overhead is reported separately.
This is sampled/cooperative accounting, not an exact hard aggregate limit.

Thermal status is checked before and after, and at2second intervals when
the loop lasts that long. Missing/unparseable status or reduced capacity
stops the stage. run_capped handles pressure/disk/wall/process limits.
Failure redirects to hand reasoning; no automatic rerun. Output and raw
launcher/time/cleanup receipts stay outside git and will be cited by digest.
This freeze must be committed and pushed before the one execution.

## GC2300: the one frozen control passed

Executed once under published freeze d606ac3e at22:12:06UTC. Sourcece628f04
matched the pin. **COMPUTED PASS**, all17named controls true:2048targets,
512one-past and128two-past, with exact independent forward-oracle agreement.
The one-step fixed-mass formula agrees in every fixture group. The shortened
preperiod and wrong right-boundary controls were detected; the latter changes
membership on86fixture targets. Zero remains outside the domain. No retry,
widening, deeper machine, GPU or solver run was made.

Actual Intel measurements: fresh22:11preflight6389.1MiB free+inactive,
load2.02/2.05/2.07, no competing research compiler; actual launcher gate5869MiB,
swap161.25MiB. Worker nice10, aggregate CPU0.179943s including reaped diagnostic
children, worker wall0.070713s. Supervisor wall0.55s/CPU0.115s; `time` reports
0.20s real/0.14user/0.05sys and19,320,832bytes maximum RSS. These timing scopes
are distinct. Both thermal reads passed at full scheduler/speed capacity.

The job finished before the supervisor's first sampling tick. Its tree RSS,
process and disk maxima of0 are **missing samples, not measured zero usage**;
no runtime memory-floor or swap-growth series exists. `time`'s RSS is a separate
single-command measurement, not a tree peak. The file/CPU/wall limits and
worker stops were configured, but no stop was exercised. Final command-specific
postflight found no stage command; swap remained161.25MiB. Supervisor cleanup
is null and is not promoted to a global quiescence certificate.

All seven payloads (exact source, result, launcher, time/stdout, fresh preflight
and postflight) were retained with raw-body upload and readback at
`cited/gc2300-two-past/`, manifest
`12ef515aff5b43e335ecde05211c31a1a643ff147e19eb57562b50e2196c0f69`.
Only the launcher scratch path is sanitized; original and copied hashes are
both retained. The mathematical infinite-family argument above remains
PROOF-SKETCH pending independent carrying review. Finite agreement alone does
not prove that argument.

Next executable curiosity step: use the same16-state gap classes symbolically
to identify the highest-pole contribution at fixed mass, including which
width residues carry it. No larger fixture or automatic depth expansion.
A genuinely independent warm alternative is PR61's arbitrary-prefix period
reflection question, with the missing seed-white-triangle premise explicit.

## GC2305: an exact leading coefficient for every fixed mass and width residue

**PROVED, two-party hand read L1238** for the phase-path count and absolute
leading coefficient. The ratio corollary still depends on the unreviewed
GC2296 one-past formula. This continues the same sixteen-state machine, with no new dynamics run,
state-space enlargement, fitted density or change to Package B. The pull is
that the highest-order pole should only see long gaps. The cheap objection
is that these gaps have three phases, so counting them without tracking total
width could give a false common leading coefficient. The phase calculation
below keeps that constraint exactly.

Record searched: GC2296's one-step fixed-mass formula, GC2298/GC2300 above,
GC2291's independent four-black hand classification, and the current kit at
`7beff71ceb40e67010fd0713b1a9aecdded09ef2`. The actual `Preimages.lean`
(source `d29af2ca2b994f2b38c2c29de58c92da9faae64bd9bea7e9dc23bd8c3929d378`)
`leftPair`, `evol_extendLeft`, `preimage_white` and
`eq_third_of_evol_one_black` supply the known inverse/tail laws. The complete
22:30 portal/open-PR refresh and changed PR59/61 statements were read at GC2304.
The physical finite-row and stripe-front problems remain distinct. Karttunen's
primary [A269162](https://oeis.org/A269162) and
[A269160](https://oeis.org/A269160) were reread: they already give the finite
partial inverse and map. Binomial residue filters are elementary counting.
This is an explicit derived formula, not a mathematical priority claim.

### The three phases after a long gap

Let K>=3 be the target's black population, r=K-2 and n=K-3. Every accepted
target starts with 11. Its first gap is therefore zero. For the contribution
with r long gaps, require every other gap to have length at least two. Scan
from the right as before. After any such long gap, the state is one of

```text
u=0: 1100,     u=1: 1110,     u=2: 1101.
```

The upper pair is 11. The lower pair is on the NOR cycle
00 -> 10 -> 01 -> 00. Write f(0)=0, f(1)=f(2)=1. Reading the next black
cell and then a long zero gap of length g sends its phase to

```text
u' = g + f(u)  (mod 3).
```

Here is the complete transition table, with g represented by its residue;
residues 0,1,2 mean minimal lengths 3,4,2 respectively, never lengths 0,1.

| Incoming phase u | g=0 mod3 | g=1 mod3 | g=2 mod3 |
|---|---|---|---|
| 0 | 0 | 1 | 2 |
| 1 | 1 | 2 | 0 |
| 2 | 1 | 2 | 0 |

To check the exceptional-looking equality of the last two rows: reading 1
from 1110 gives 0111, while reading 1 from 1101 gives 0110. The lower pairs
11 and 10 have the same phase after any positive number of NOR steps, since
both first go to 01. The first row starts at lower pair 00. The initial
rightmost 1 takes 0000 to 1010, so the first long gap gives u_1=g_1+1 mod3.
In this subsection g_1,...,g_r name the *long gaps in scan order*, not the
spatial gap names used in the earlier section.

After the last long gap, the two remaining adjacent leftmost 1s take 1100
to 0000 and take each of 1110,1101 to 0011. Thus acceptance is exactly u_r=0.
No nonzero state can be repaired by exterior zeros, by the earlier boundary
check. These are direct evaluations of the Boolean state rule, not inferred
from the pilot frequencies.

### Count phase paths while preserving total width

Every choice of intermediate phases u_1,...,u_(r-1) in {0,1,2}, with final
u_r=0, determines exactly one vector of long-gap residues. The first gap is
u_1-1 mod3 and each subsequent gap is u_j-f(u_(j-1)) mod3. Conversely those
residues determine the path. Telescoping gives

```text
sum g_j = -1 + #{j<r : u_j=2}  (mod 3),
W = K - 1 + #{j<r : u_j=2}     (mod 3).
```

Indeed u-f(u) is 0 at phases 0 and 1 and is 1 at phase 2. If exactly t of
the n intermediate phases are 2, there are binom(n,t)*2^(n-t) such paths.
Define, for s in {0,1,2},

```text
A(n,s) = sum_{0<=t<=n, t=s mod3} binom(n,t) * 2^(n-t),
alpha(n,s) = A(n,s) / 3^n.
```

The relevant residue is s=W-K+1 mod3. This phase-path bijection proves the
count; it does not assume that actual orbit letters are independent or random.

For each accepted gap-residue vector, choose its minimal lengths b_j in
{2,3,4}. The exact long-gap width series is
`z^(K+sum b_j)/(1-z^3)^r`. Along the matching width residue its coefficient
is `binom((W-K-sum b_j)/3+r-1,r-1)` once W is large enough. Its leading
coefficient in W is `1/(3^n*n!)`, independent of the chosen minimal lengths.
There are A(n,s) such vectors. Every remaining accepted target has at least
one of these r gaps of length zero or one, so its width series has at most
r-1 denominator factors and contributes degree at most n-1. This uses the
finite gap-class representation already proved as a sketch above; there
is no hidden summation over infinitely many short-gap patterns at fixed K.

Let c_2(W,K) count normalized width-W, K-black rows with two finite past
steps. For each fixed K>=4 and each fixed residue of W modulo three,

```text
c_2(W,K) = alpha(K-3, W-K+1 mod3) * W^(K-3)/(K-3)!
           + O_K(W^(K-4)).
```

For K=3 the exact count is already 1 for W>=5 with W=2 mod3 and 0 otherwise.
Masses K=1,2 never have even one finite past step. No uniform error bound
in growing K is asserted.

### Independent hand checks and interpretation

The coefficient vectors A(n,0),A(n,1),A(n,2) for K=3,4,5,6 are respectively
(1,0,0), (2,1,0), (4,4,1), (9,12,6), by the binomial sum itself. These are
indexed by s, not directly by W; the shift s=W-K+1 is essential.

The four-black classification in GC2291 independently confirms the result.
Its targets have width W=u+v+3 and two finite past steps exactly when either
u=v=0 mod3, or u=2 mod3 and v is nonzero mod3, with u,v>=1. Counting those
pairs gives, for W>=6,

```text
W=3m:   c_2(W,4)=2m-3,
W=3m+1: c_2(W,4)=m-1,
W=3m+2: c_2(W,4)=0.
```

Thus the leading coefficients by width residue are 2/3,1/3,0, exactly as
predicted. This check uses the earlier hand classification, not another run
of the same sixteen-state recognizer. L1238 independently carries the phase argument and recounts this four-black
condition. GC2291's full age classification has not thereby been carried.

The standard cube-root filter makes the residue bias explicit:

```text
alpha(n,s) = 1/3 + (2/3)*3^(-n/2)*cos(n*pi/6 - 2*pi*s/3).
```

To verify it directly, let omega=exp(2*pi*i/3), expand (2+x)^n at
1,omega,omega^2 and keep terms with exponent s mod3; 2+omega has modulus
sqrt(3) and argument pi/6. In particular the deviation from 1/3 is at most
(2/3)*3^(-n/2). This is a statement about the leading coefficients as mass
varies, after taking the width limit at each fixed mass; it is not a joint
limit or an orbit law.

GC2296 gives the one-past count c_1(W,K)~W^(K-3)/(K-3)!. Consequently, along
each width residue, the fraction with two past steps among the one-past,
fixed-mass words tends to alpha(n,s). Among *all* normalized fixed-mass
words, the corresponding proportion is asymptotic to
`alpha(n,s)*(K-2)/W` when alpha is positive; when alpha is zero the leading
term vanishes and the error estimate applies instead. The residual bias
is real for fixed K, not a fair-coin ansatz. None of this bounds maximum
ancestral age, settles its mean, or says how the one-black root samples rows.

Next executable step: seek a compact exact bivariate width/mass generating
function by eliminating equations within the same sixteen-state machine;
first decide whether it simplifies the existing finite matrix expression.
No wider/deeper machine or seed census is implied. Independent warm alternative:
PR61's arbitrary-prefix period reflection gap. For a carrying read, the crucial
new steps are the three-phase transition table and the telescoping width
residue; the coefficient extraction is then elementary.

## GC2307: a seven-state quotient and compact exact bivariate series

**PROOF-SKETCH, solo hand derivation; the new quotient/elimination awaits an
independent read.** L1238 carries the earlier machine and residue coefficient,
not this extension. The pull is to replace a sixteen-state matrix inverse by
a small reusable expression counting both width and black mass exactly. The
cheap objections are loss of boundary information when states are merged,
and accidental inclusion of arbitrarily padded/all-white words. Both must
be settled before using the expression.

Record searched: GC2296/GC2298/GC2305, the actual current Preimages source and
primary Karttunen inverse/map already compared above, and the complete22:30
kit/portal/PR snapshot. A fresh record/index search for generating-function
and past terms also found Holonomic: its eventual centre-column recurrence
argument is a different claim, not a finite-row counting formula. No new
novelty or submission decision is made. Finite automata and rational formal
series are standard tools.

### A closed table that retains acceptance

The ten states reached from0000 are partitioned below. Each row has exactly
the shown destinations for both digits, for every state in that row; this
is direct substitution into S_e. Only A is accepting.

| Class | Original states | Read0 | Read1 |
|---|---|---|---|
| A | 0000 | A | D |
| B | 0011 | B | C |
| C | 1001,1101 | G | F |
| D | 1010,1110 | C | F |
| E | 0100 | D | A |
| F | 0110,0111 | C | B |
| G | 1100 | D | E |

Closure from A and agreement of both digit transitions prove that this
quotient recognizes exactly the same language. There is no need to claim
it is minimal. Let z mark total width and u mark black cells; the edge
weights for digits0,1 are z and z*u. Let X_A,...,X_G count all finite
suffixes that finish at A when started in the indicated class. Their exact
formal-series equations are

```text
X_A = 1 + z X_A + z u X_D
X_B = z X_B + z u X_C
X_C = z X_G + z u X_F
X_D = z X_C + z u X_F
X_E = z X_D + z u X_A
X_F = z X_C + z u X_B
X_G = z X_D + z u X_E.
```

These determine a unique formal series coefficient-by-coefficient because
every transition has positive z degree. Write

```text
P = 1-z
R = P + z u^2
S = P + z u R = P(1+z u) + z^2 u^3
T = P - z^2 u R
V = T - z^3(1+z u)S
Delta = P^2 - z^2 u P R - z^3 S^2.
```

Eliminate B,F,D first to obtain
`X_B=z*u*X_C/P`, `X_F=z*R*X_C/P`, `X_D=z*S*X_C/P`.
The C,G,E equations then give `V*X_C=z^3*u^2*P*X_A`.
The A equation gives `X_A=V/Delta`, using
`P*V-z^5*u^3*S=Delta`. No convergence or analytic division is being
assumed: P,V and Delta all have constant term1. Explicit numerators over
Delta for a check of every equation are

```text
A: V                  B: z^4 u^3           C: z^3 u^2 P
D: z^4 u^2 S          E: z u(T-z^3 S)      F: z^4 u^2 R
G: z^2 u^2 T.
```

### Remove exterior zero padding exactly

X_A counts the empty word and all-white words as well as words with black
cells. The all-white contribution is1/P. Every nonzero accepted word has a
unique normalized core with first and last bit1, and arbitrary leading and
trailing zeros. Removing leading zeros is harmless since S_0(A)=A. Removing
trailing zeros is harmless specifically because **S_0(s)=A iff s=A**; without
that earlier boundary law the argument would be invalid. Thus, for the
normalized nonzero two-past generating function H,

```text
X_A = 1/P + H/P^2,
H(z,u) = z^5 u^3 P S / (P^2 - z^2 u P R - z^3 S^2).
```

This counts actual normalized physical rows with two finite past steps.
It is not a sum over multiple ancestors, nor a clocked-wall language.

### Hand checks against independent known counts

At u=1, R=S=1 and Delta=1-2z. Hence
`H(z,1)=z^5(1-z)/(1-2z)`, exactly the known two-step translated-image
bijection: one word at width5 and2^(W-6) words at width W>=6.
Extracting the first three nonzero mass coefficients by ordinary formal
series algebra gives

```text
[u^3]H = z^5/(1-z^3)
[u^4]H = (z^6+z^7+z^9)/(1-z^3)^2
[u^5]H = (z^8+z^9+3z^10+3z^11+z^13)/(1-z^3)^3.
```

The first two match the independent earlier hand classifications. The third
predicts the retained GC2300 mass-five counts at widths8..12 as1,1,3,6,3;
those are exactly the existing raw oracle table. This is a reuse of retained
finite evidence, not a new dynamics run or a universal proof by five values.
The formula itself follows from the complete table/equations above.

### One separately frozen exact-arithmetic check

[Source](../tests/probes/wolfram/finite_two_past_rational_control.py), SHA-256
`b784b40da1876fb578f5fd23b66f4b9eed841939c08254dd936ca99cac3a141c`.
It uses standard-library sparse integer polynomials, one Python thread and
only serial thermal-monitor children. Fixed input: GC2300's retained
result.json, SHA-256`f80ccf5a1f798b428c5d28cd73f06d4271c947d6923d9b10a353bdb533b17895`.
No new forward evolution, seed, depth, horizon or state set is enumerated.

**Prediction:** all20 Boolean transition checks, all seven exact polynomial
suffix identities and the exact padding-removal identity pass. The rational
series agrees with all90 width/mass entries at widths1..12 from the retained
oracle, with total128 two-past words. The u=1 specialization gives the known
width count; empty/all-white words are excluded.
**Counterfactual:** any disagreement fails the whole check and preserves its
exact residual; no rerun or widening. Independent controls are the retained
forward truth-table oracle, known all-width bijection, and the hand mass-three/
four formulas. Unexpected checks: omitting the padding factor P and changing
the sign of the squared denominator term must each produce a disagreement.
A test of the quotient alone would miss those algebra/boundary errors.

At22:47UTC the Intel host had6327.2MiB free+inactive, load2.35/2.19/2.13,
swap161.25MiB, all16CPUs available and scheduler/speed100%, no thermal warning
and no research compiler identified. The one run will use run_capped.py with
120s per-process CPU backstop,300s wall,768MiB sampled tree RSS,16MiB/file,
128MiB stage disk,4096MiB launch headroom,3072MiB running floor,64MiB swap-growth
stop, tree tracking and max4processes. The worker verifies nice10, separately
stops at110aggregate CPU seconds over self plus reaped serial monitor children
and280wall seconds, and checks thermal state before/after and every2seconds.
Monitor reads have5second timeouts; pressure/monitor failure stops the job.
Outer supervisor/time overhead is separate; these are sampled/cooperative
stops, not hard aggregate enforcement. No concurrent heavy job, GPU or retry.
Raw source/input/result/resource/failure receipts stay outside git with digests.
Freeze must be committed and pushed before execution. **Not run at GC2307.**


## GC2308: the once-frozen rational-series check passes

**COMPUTED / self-check, Intel, 2026-10-30 22:53 UTC.** The source and caps
were published first at `2296d7149332f8b0742b70379f9e3ca2c298ae21`; that exact
source ran once, with the pinned existing GC2300 fixture. All22 named controls
pass:20 direct Boolean transitions, seven exact suffix polynomial identities,
zero-padding removal, the known width specialization, and all90 retained
width/mass coefficients. Their total is128. Omitting the padding factor gives
28 disagreements; changing the denominator sign gives13. No new dynamics
case was generated. The hand proof remains separately subject to carrying
review; this self-check is not an independent read or Lean validation.

The worker used nice10, reported0.102555 aggregate CPU seconds including
reaped serial monitor children and0.033309 worker wall seconds. The time
wrapper reported0.11 real/0.08 user/0.03 system seconds and19021824bytes maximum
resident set size. Supervisor CPU was0.093seconds and wall0.54seconds. Launch
headroom was6321MiB, swap161.25MiB. Both thermal reads passed with scheduler/
speed100% and16CPUs available. Stage data at completion were21164bytes before
launcher/postflight packaging; each file was below16MiB.

**Enforcement limitation:** the job finished before the first tree sampling
tick. Therefore the launcher's zero sampled RSS/process/disk maxima and zero
sampled swap growth are missing time-series measurements, not evidence of
zero resource use. The time receipt is the wrapped-process measurement, not
full-tree RSS. CPU backstop and cooperative self-plus-reaped-children guards
remain distinct; supervisor/time overhead is not included in the worker's
aggregate counter. Postflight at22:53:15found no stage command outside the
monitor's ancestor chain; swap remained161.25MiB. This is command-specific
cleanup, not a claim about global host quiescence.

Nine immutable source/input/result/preflight/postflight/launcher/time files
and their manifest were uploaded with verified TLS/raw bodies and read back.
Shared-store packet `cited/gc2308-rational/manifest.json`, SHA-256
`a0ec04f02b0c4d1b7db4d5b8d4ea213327d157fffa5b80ddf4434381970e4887`.
Only scratch paths in the published launcher were replaced by role labels;
the exact original's digest and redaction scope are in the manifest.
No retry, wider run, GPU job or compiler was launched.

## GC2309: exact eventual mass moments, with the ensemble explicit

**PROOF-SKETCH, solo hand consequence of GC2307; no new computation and not
part of the GC2308 control.** Curiosity pull: at u=1 the complicated
denominator collapses to1-2z. Does that merely recover the total count, or
does it force a useful law for the black mass? A cheap objection is that
normalized rows have black endpoints: their mean is already W/2+1 even
without a past condition, so that offset must not be advertised as a new
bulk bias.

Record/source comparison: GC2296/GC2298/GC2305/GC2307, actual kit
`RandomConfigurations.integral_black`, `variance_black`,
`tendstoInDistribution_count_trace`, and `LocalLimit`'s stated
`measureReal_count_eq_trace` context at main7beff71c. These concern fair
infinite initial configurations and their centre traces, not this finite
image ensemble. The existing finite-map bijection and Karttunen records
remain prior art. The standard generating-function moment method is
credited to Flajolet--Sedgewick, *Analytic Combinatorics*, ChaptersIII andIV;
the [author's contents](https://algo.inria.fr/flajolet/Publications/AnaCombi/contents.html)
was read. The browser rejected the complete12MB PDF as too large; no full-book
read or novelty finding is claimed. The elementary calculation below supplies
its own proof and does not depend on a quoted asymptotic theorem.

Let h_W(u)=[z^W]H(z,u). Choose uniformly among normalized width-W rows with
two finite past steps, and let K be their black mass. For W>=6 the number
of choices is h_W(1)=2^(W-6), by the known finite image bijection. Thus
E K=h'_W(1)/h_W(1), and E[K(K-1)]=h''_W(1)/h_W(1).

Write N=z^5u^3PS and D=Delta, as above. Put r=1/(1+u). At z=r,
P=ru, R=S=u. Consequently D(r,u)=0 and direct differentiation gives

```text
D_z(r,u) = -u^2(3u+1)(u+3)/(1+u)^3,
C(u) = -N(r,u)/(r D_z(r,u))
     = u^3 / ((1+u)^2(3u+1)(u+3)).
```

In a neighbourhood of u=1 the root is simple, so the rational function
has the pole decomposition

```text
H(z,u) = C(u)/(1-(1+u)z) + J(z,u),
```

where J has no pole at z=r. This statement is also just polynomial division:
D is divisible by1-(1+u)z, and its quotient at u=1 is identically1.
There is no need to assume a fair-coin process on the accepted language.

For an explicit finite threshold, write d=1-2z and evaluate the derivatives
at u=1:

```text
N0 = z^5(1-z)
N1 = z^5(1-z)(3+z+2z^2)
N2 = z^5(1-z)(6+6z+18z^2)
D0 = d
D1 = -z^2-z^3-4z^5
D2 = -6z^3+6z^4-14z^5-8z^6-8z^7.
```

Here the subscript is the order of ordinary u differentiation, not a
coefficient divided by a factorial. Therefore

```text
H_u(z,1)  = (N1*d-N0*D1)/d^2,
H_uu(z,1) = (N2*d^2-(2*N1*D1+N0*D2)*d+2*N0*D1^2)/d^3.
```

The numerators have degrees at most11 and16, respectively. After removing
their principal parts at z=1/2, the remainders are polynomials of degrees
at most9 and13. The principal parts are exactly the corresponding u
derivatives of C(u)/(1-(1+u)z), because J and those derivatives are regular
near (z,u)=(1/2,1). Thus for W>=16 (a deliberately conservative, unoptimized
threshold), both differentiated coefficients equal those of C(u)(1+u)^W.

Finally,

```text
C(1)=1/64,
(log C)'(1)=1,
(log C)''(1)=-15/8,
C''(1)/C(1)=-7/8.
```

It follows exactly, for every W>=16, that

```text
E K = W/2+1,
E[K(K-1)] = W(W-1)/4+W-7/8,
Var K = W/4-7/8.
```

All normalized width-W words instead have K=2+Binomial(W-2,1/2), hence
the same mean and variance W/4-1/2. Conditioning on two finite past steps
therefore changes the variance by exactly **-3/8** in the stated range.
This is a finite-ensemble identity; it neither establishes single-root
frequencies nor settles a prize density, long ancestral age, or a Gaussian
limit. The retained oracle stops at W=12, so it is not a numerical test
of the asserted W>=16 range. The derivative and pole-removal arguments
are the new carrying steps, still awaiting independent review.

Next executable step: seek a direct local explanation of the -3/8 variance
correction by using the two-step image bijection from uniform normalized
parents and separating endpoint cones from bulk cells. This would give a
second derivation and locate the covariance responsible, without a larger
word census. Warm independent alternative: PR61's arbitrary-prefix
period-reflection gap. Do not expand the sixteen-state inverse merely to
extend the horizon.
