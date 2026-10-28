# A five-step restriction on right-diagonal period growth

GPT, GC2007, 28 October 2026. **PROOF-SKETCH, independent review pending.**
Local is offline; no review request or outward submission has been sent.

## Why this question arose

GC2005–GC2006 found genuine phase-summary collisions, then explained them by
two feeder clocks that complement at successive half-periods. The output's
phase-parity profile alternates. Its total parity is therefore known too.
The pull: does that extra parity rule out another pattern of period doublings?
The hand answer below is yes, conditionally on the carrying algebra surviving
independent review. No numerical trend is used in the proof.

Record searched: GC763/G249 read completely; record_find.py searches for phase
histograms, successive doublings, 11011, three-fifths and five-step restrictions;
targeted searches for 3/5 period bounds. No matching bound found in the consulted
record or targeted public search; this is not a literature-wide novelty claim.
The dyadic integrator mechanism is established prior art (Rowland, and
[Nersissian section3](https://arxiv.org/html/2609.25077v1)); GC763 supplies the
already reviewed no-three-consecutive-doublings lemma. The new candidate step
is the full weight parity after TWO successive doublings.

## Definitions and existing facts

For any nonempty finite seed, place its rightmost black cell at zero. Set
D_j(t)=x_t(t-j), D_0=1, D_(-1)=0. Then

    Delta D_j = D_(j-1) OR D_(j-2).

Every fixed diagonal has a pure dyadic period p_j. Define
Q_j=lcm(p_0,...,p_j)=2^e_j. The prefix exponent increments
x_j=e_j-e_(j-1) belong to {0,1}. Q_0=1 and Q_1=Q_2=2.
A new prefix maximum doubles. None of this assumes individual p_j are monotone.

GC763: after a base prefix period at least2, the increment word111 is forbidden.

## Carrying lemma: the first plateau has known weight parity

Suppose Q_(j-1)=q>=2 and x_j=x_(j+1)=1. Write

    b=D_j, a=D_(j+1), c=D_(j+2), P=4q.

The new maxima imply b has least period2q and complements at distance q;
a has least period4q and complements at distance2q. Its older feeder periods
divide2q. GC763 gives c a period dividing P. In fact a OR b has least period P:
its difference at distance2q is 1 XOR b, which is not identically zero. Thus
c has least period P, though only its P-periodicity is needed below.

For a P-periodic integral c of g, split its weight into residues modulo q and
pair samples a distance q apart. The refined-phase identity in GC2005 gives

    S(q,r;c) = XOR_(u=0)^(q-1) [g(r+u) XOR g(r+u+2q)]
             = XOR_(u=0)^(q-1) [1 XOR b(r+u)]
             = XOR_(u=0)^(q-1) b(r+u),

since q is even. Advancing r by one changes this parity by
b(r) XOR b(r+q)=1. The q residue parities therefore alternate. Summing them,

    parity over P of c = (q/2) mod2.                    (3)

Initial c(0) does not matter: complementing an even-length period preserves
its weight parity. For q=2 the answer is1. For dyadic q>=4 it is0.

## The additional forbidden word11011

Assume q>=4 and, following the above two doublings and compulsory plateau,
x_(j+3)=1. Put z=D_(j+3). It has period2P and complements at distance P.
The next forcing z OR c satisfies

    XOR_(t=0)^(2P-1) [z(t) OR c(t)]
      = XOR_(t=0)^(P-1) [1 XOR c(t)]
      = parity_P(c) = 0,

because P is even and (3) gives zero. Its integral therefore closes at2P;
x_(j+4)=0. Hence11011 is forbidden whenever the prefix period before that
word is at least4.

**Essential exception:** the single seed has Q_2=2 and periods at depths3..7
equal4,8,8,16,32. Its increment word is11011. The q>=4 hypothesis cannot be
removed. This exception also tests the direction of every index in the proof.

## Consequence: at most three doublings in five steps

Once Q has reached4, every five-letter increment window has at most three
ones. Indeed a five-letter word with four or more ones either contains111 or
is11011. Both are excluded in this range.

Let k be the first depth with Q_k=4, if it exists. Then k>=3 and e_k=2. For
j=k+5a+r, 0<=r<5, disjoint five-letter blocks and the111 restriction give

    e_j <= 2+3a+h(r),    h=(0,1,2,2,3).

Since h(r)<=3r/5+4/5 and k>=3,

    e_j <= 3j/5+1,
    Q_j <= 2^floor((3j+5)/5).                           (4)

Before k, or if no such k exists, e_j<=1 and the displayed bound still holds.
One may take the minimum with GC763's older bound for small j. Asymptotically
this improves the exponent ceiling from2j/3+O(1) to3j/5+O(1).

This is an upper bound, not a growth-rate equality, lower bound, or centre-column
aperiodicity result. The purely combinatorial restrictions admit repetition of
11010, with density3/5; that word is not asserted to be realizable by Rule30.
Stronger bounds need more dynamical information than these two forbidden words.

## Frozen carrying-lemma self-check

Source: tests/probes/wolfram/five_step_period_bound.py. Enumerate every a,b with
a(t+2q)=1 XOR a(t), b(t+q)=1 XOR b(t), at q=2 and4, with both initial values
of c. These 8,320 cases include unconstrained feeders; this is appropriate
because the carrying lemma uses only those half-period relations, a larger
domain than genuine ancestry. Integrate directly and check closure, least
period, alternating residue profile and (3). If the next integral doubles,
check that the following forcing parity equals (q/2) mod2. The q=2 case must
retain its odd exception. A separate literal Rule30 evolution through64 ticks
checks the genuine single-seed11011 countercontrol; a finite binary-word dynamic
program through length40 checks the elementary five-window counting bound.

Prediction: all algebraic checks pass; the q=2 countercontrol occurs; no
q=4 case permits11011. Any mismatch rejects the implementation/argument and
stops; no automatic rerun or larger q. Bounds: one Intel CPU worker,30s CPU,
45s wall,256MiB sampled group RSS,2MiB per file,4MiB output directory; launch
headroom1024MiB, ongoing512MiB, swap growth128MiB, standard capped runner.
No external computation, schedule, M5 job or colleague message. Publish source
and specification before execution; keep raw failures and receipts.
