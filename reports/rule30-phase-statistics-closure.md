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
