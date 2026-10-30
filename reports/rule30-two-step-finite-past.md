# Two finite inverse steps: sixteen states and period-three gap counting

GC2298, 30 October2026. **PROOF-SKETCH**, solo hand argument, independent
carrying read pending. The control stage was frozen at GC2298 and passed once at GC2300;
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
