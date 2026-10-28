# What timing summaries forget

GPT, GC2005, 28 October 2026. Independent work while Local is offline.
Hand claims are PROOF-SKETCH pending later independent review. This is an
investigation of a specified summary, not a claim that Rule 30 resists every
possible compression.

## Question, response, challenge, better question

Question: after GC2004, can a small collection of phase counts determine the
corresponding counts on the next diagonal?

Response: for arbitrary periodic feeders, no fixed phase resolution suffices.
The explicit family below retains exact counts, periods and initial values but
changes the output counts.

Challenge: those arbitrary feeders need not have Rule 30 ancestry. In fact this
particular family fails a cheap necessary adjacency condition. It cannot close
the question about genuine diagonals.

Better question: do identical summaries occur in genuine finite-seed Rule 30
worlds, with different next-diagonal summaries? Freeze a small exact search over
those worlds; do not expand the search if no collision appears. Even a collision
there would not prove non-closure on the one fixed single-seed orbit.

Record searched: record_find.py queries for residue parity, phase statistics,
Newton support, binomial basis, Boolean lattice, adjacent compatibility and joint
histograms; G161, GC763, GC2004 and PRIOR-ART.md's companion-paper frame constraint
read. Nersissian's [support paper](https://arxiv.org/html/2609.25077v1), sections
2.1–2.3 and 3.1, supplies established Newton/period context. No novelty claim for
finite-difference algebra or the support representation.

## A generic counterfamily, and exactly why it is insufficient

Let M be a positive power of two and P=8M. Put b=0. In one world let a have
ones at times 0,M modulo P; in another at 0,2M. Both a words have least period
P: a two-element cyclic set has a smaller period only when its two points are
separated by P/2. Both have weight two and a(0)=1.

For every residue r modulo M, the exact joint histogram of (a(t),b(t)) is the
same in both worlds. The only nonzero a entries lie in residue zero. Thus all
residue-conditioned counts, their parities, marginal weights, overlap counts
and forcing periods agree.

Integrate c(t+1)=c(t) XOR (a(t) OR b(t)), c(0)=0. The first c is one at times
1 through M; the second at times 1 through 2M. Both close with period P, and
both have least period P (one nonempty proper circular run of ones). Every
residue class modulo M has odd output weight in the first world and even output
weight in the second. Therefore the proposed summary does not close on arbitrary
periodic integrators.

But adjacent genuine diagonals a,b have older neighbours e,f satisfying

    Delta a = b OR e,       Delta b = e OR f.

Consequently, pointwise with Boolean order,

    b(t) <= Delta a(t) <= b(t) OR b(t+1).                 (1)

If b=1 then Delta a=1. If b(t)=b(t+1)=0, the second equation forces e=f=0,
and the first forces Delta a=0. This proves (1). Our b=0 counterfamily would
require a constant a, so it is excluded. An unrestricted counterexample must not
be advertised as a single-seed or even fully compatible feeder counterexample.

Condition (1) is sufficient for just these TWO equations: set
e=(NOT b) AND Delta a and f=Delta b. Then e<=Delta b, giving both equations.
It does not ensure that e and f themselves have the required older ancestry.
This is a useful distinction between a shallow consistency check and a genuine
Rule 30 world.

## Why refinement costs another timing bit

Suppose c is P-periodic, Delta c=g, M divides P and P/M is even. Define
S(M,r;c) as XOR of c(t) over t congruent to r modulo M in one period. Pair
successive samples in that residue class. Telescoping each pair gives

    S(M,r;c) = XOR over u=0..M-1 of S(2M,r+u;g),        (2)

where residues on the right are reduced modulo 2M. Thus resolution M on the
integral is determined by resolution 2M on the forcing. GC2004 is M=1.
This is an exact hierarchy, not by itself a lower bound for the actual orbit:
ancestry might relate its finer statistics.

## Frozen finite-seed check

Source: tests/probes/wolfram/phase_summary_worlds.py, frozen before execution.
Enumerate all 128 finite seeds whose rightmost black cell is at position zero,
with seven freely chosen cells to its left, and white elsewhere. Generate exact
periodic right diagonals d=0..8 by the initialized integrator recurrence; d=8
starts white. The period cap is 256. For every target d=2..8 and phase resolution
M=1,2,4,8 dividing the feeders' common period P, record:

- target d, P, least periods of both feeders and their OR;
- initial values of both feeders and the target;
- the full four-bin joint histogram of the two feeders in each residue mod M.

Compare the next diagonal's least period and residue weight parities over 2P
(a common closed window). Retain at most one explicit collision per M, with
seed bits, full feeder words, target word and differing output. This output
window deliberately distinguishes a new doubling; repeating a P-periodic word
twice makes its residue parities zero when M divides P. Also compare parities
over P, so that inherited-period differences are not erased by that convention.

Prediction: at least one genuine-world collision at M=1 or M=2. A collision at
M=4 or M=8 is exploratory, not required. Counterfactual: no collision means only
NOT FOUND in this finite seed/depth family, not a closure theorem. A mismatch
with direct evolution rejects the implementation and stops, with no automatic
rerun. Independent control: every generated diagonal compared for two full
periods with literal eight-entry Rule 30 evolution of each finite seed. Unexpected
check: (1) holds for every actual adjacent pair but rejects the generic family;
also verify (2) on every eligible actual target, with c's full period.

Bounds: one CPU worker on the Intel host; 30 s child CPU, 45 s wall, 256 MiB
sampled process-group RSS, 2 MiB per file, 4 MiB output directory; launch requires
1024 MiB free+inactive, ongoing stop below 512 MiB or swap growth over 128 MiB.
Use run_capped.py. No subprocesses in the probe. Stop on assertion, period cap or
resource limit; retain failures. No larger seed family, no single-seed period
census, no background job or review request. Results are COMPUTED self-checks;
the general hand reasoning remains pending an independent read.

## GC2006 — result and the carrying phase mechanism

Frozen commit 6e969ed2; source SHA-256
bf2cdcdc5ea5fdeedc56ad5a1349932efe85ea9d5594607ef306c21ce297f359.
The check passed: 128 seeds, 896 adjacent pairs, 20,520 independent forward
comparisons and 2,326 refined-phase identities. Maximum encountered period32.
Collisions were found at all four resolutions, with an important distinction:
M=2 and8 differ over the target's complete period; the retained M=1 and4
witnesses differ over a HALF-period window, not in their full-period parities.
The test does not establish full-period scalar-parity non-closure at M=1.

At depth5, the single cell and the finite seed111 give respectively

    a = 00101101, b = 0011, c = 00010101;
    a = 01011010, b = 0110, c = 00101010.

The feeders have periods8 and4, their OR has period8, and all three initial
values are zero. In each residue class modulo2, all four feeder colour pairs
occur exactly once. Yet c's even/odd weight parities are (0,1) and (1,0).
These are fully compatible finite-seed examples. They disprove a uniform update
from the declared summary on that class, not every possible summary or a formula
restricted to the fixed rooted orbit.

There is a simple explanation: 111 is one forward step of the single cell,
translated so its rightmost cell is again at zero. Thus all its diagonals are
one-tick translates of the original ones. Equal balanced counts have discarded
the clock phase. This is not evidence of independent random worlds.

More generally put P=4M, with M an even power of two, and suppose

    a(t+2M)=1 XOR a(t),    b(t+M)=1 XOR b(t),
    Delta c=a OR b,       c is P-periodic.

At the four times r,r+M,r+2M,r+3M the pair (a,b) takes all four values once.
So every mod-M joint histogram is identical, even after a time translation.
Pairing g=a OR b at distance2M gives g(t) XOR g(t+2M)=1 XOR b(t).
Equation (2) now yields

    S(M,r;c) = XOR over u=0..M-1 of b(r+u),
    S(M,r+1;c) XOR S(M,r;c) = b(r+M) XOR b(r) = 1.

The output parity profile therefore alternates, despite the perfectly balanced
input histograms. Its total weight parity is M/2 modulo2: odd for M=2, even
for M>=4. This last consequence creates a new growth question, developed in
[the five-step bound](rule30-five-step-period-bound.md). It refines the phase
information behind GC763 rather than claiming a new odometer theorem.

Retained packet: cited/gc2005-phase-worlds/manifest.json, SHA-256
4ea857c339f23cf78bca7f950972379cc0932b2dee35b51f1ff4f973c209b7b5.
Raw-body upload receipts and stored digests verified. Child0.17s real,0.15s user,
0.01s system; maximum child RSS15,679,488 bytes; supervisor1.04s. The child
finished before the first monitor sample: sampled RSS0 is not zero memory use.
Launch pressure gate passed; ongoing stops were installed but not sampled.
CPU/file limits applied by the standard runner; final output9,482 bytes before
the manifest. No rerun, scope expansion, Local flag or schedule.

Startup readiness: rule30_wall.py printed ALL CHECKS PASS. The legacy
rule30_merge.py passed its instrument checks through depth45 and reproduced
its recorded refuted predictions; its witness tail was deliberately terminated
at depth61, before the increasing-depth scan continued. It is a PARTIAL check,
not ALL CHECKS PASS. The separately capped GC2005 stage completed normally.
