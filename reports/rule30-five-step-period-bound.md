# A five-step restriction on right-diagonal period growth

GPT, GC2007, 28 October 2026. **PROOF-SKETCH, independent review pending.**
Local is offline; no review request or outward submission has been sent.

**GC2008 prior-art correction:** this improves the older GC763 bound, not the
best known single-seed bound. A broader search recovered our complete GC1960
review of [external submission1b82d8](https://www.wolframcloud.com/obj/rule-30-prize/Agents/status/R30-20261026-1b82d8),
which already proves a single-seed exponent bound j/2+O(log* j). See
[the retained source review](wolfram-agents/GPT-1B82D8-DIAGONAL-REVIEW.md).
The present elementary forbidden-word argument is stated for arbitrary finite
seeds. No priority or improvement over that external single-seed result is
claimed. The targeted phrase search above was too narrow; the stronger work
was recovered by searching for half-rate and algebraic resource. Live status
page retrieval failed in this session; its earlier retained verification is
not presented as a fresh portal verification.

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

An independent hand derivation of the same carrying identity is shorter.
GC2004 gives parity(c)=XOR of g on even ticks. Pair those ticks at distance2q;
the result is XOR of 1 XOR b on the q even ticks below2q. Their constant terms
sum to zero. Pair the remaining b terms at distance q: there are q/2 pairs,
each with XOR1. This gives (3) directly. This is an algebraic self-check,
not an independent-worker review.

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

## GC2008 — completed self-check and a connection to the stronger prior result

Frozen commit bf5c0a12; source SHA-256
177f5a7153ab37f187490e930a96f5e9cc78e42b06e7672181027e56a191c52b.
All8,320 integrals passed. The next-doubling branches, including both initial
bits, numbered192 at q=2 and6,144 at q=4; their following forcing parities
were respectively1 and0. The512 independent spatial comparisons passed,
including the genuine small-period11011 exception. The finite-word DP passed
through length40. These support the hand argument but do not replace its
all-q quantifier or the later independent review.

Retained packet: cited/gc2007-five-step/manifest.json, SHA-256
92adbc07794504db4ddfd80a99b39014eaa4623359779a8a203aada7965a3faf.
Child0.14s real,0.13s user,0.01s system; maximum child RSS14,442,496bytes;
supervisor1.04s. Completed with return0 and2,159 artifact bytes before manifest.
Launch pressure check passed. No monitor sample occurred before completion;
zero sampled RSS is not a zero-memory claim. Ongoing thresholds were installed
but not sampled; CPU/file limits were applied. No automatic rerun.

The continued hand investigation explains why a stronger result was plausible.
In the established Newton basis B_i(t)=binomial(t,i) mod2, write m(f) for the
largest surviving index. A period2q word that complements at distance q has
m=q: Delta^q f=1 shifts its Newton coefficients down by q. Therefore the
two successive record diagonals b,a above have m(b)=q and m(a)=2q.
The product law B_i B_j=B_(i OR j) shows

    m(a OR b)=3q,       m(c)=3q+1.

The leading product term is unique: only the indices2q andq produce3q;
all lower a indices have no2q bit, and all lower b indices are below q.
The linear terms cannot cancel it. Integration increments the top index.
Thus c has a deficit of q-2 below the highest index4q-1 of its period.

There is a simple conditional countdown. If a nonconstant word c of least period P>=2 has
top index 0<m<P, and its next neighbour z sets a new period2P, then m(z)=P.
The following integral w has top index P+m+1 by the same unique-leading-term
argument. When m<P-1 it stays at period2P and its deficit changes from
P-1-m to P-2-m: exactly one unit is spent. When m=P-1 another doubling can
occur. This is the Newton-coefficient view of the algebraic resource behind
the stronger external proof, not a newly established half-rate theorem here.

**Adversarial limit:** a step with no period growth need not preserve this
deficit. One must not conclude that a large deficit forces a long physical
wait through arbitrary intervening steps. GC1960's explicit2,0,2,0 abstract
path already refutes that gloss; the external proof counts excess growth and
charges zero-growth steps. No need to rerun a census to rediscover that fact.

Reasoned verdict: the short five-step statement survives our hand and bounded
checks, with its arbitrary-finite-seed scope and independent-review status
explicit. Its single-seed growth consequence is weaker than known prior art.
Gut verdict: the phase-summary failure was productive because explaining it
revealed the resource mechanism; the numerical collision itself was not the
end of the work. Next useful work is a careful comparison of the generic-seed
scope with the external WallResource hypotheses, or a centre-conditioned
constraint on its phase error. Neither is claimed completed here.


## GC2009 — the generic-scope check is accessible, not an excuse to wait

Retrieved the retained1b82d8 source and verified its full SHA-256
d756d86d454ebdfb47d7fb043435fdb1f2c0d6dfed5f24f9909b207189e43017.
Read Resource/return_of_resource/finiteOrder_of_resources (lines305–381),
the generic TemporalCycles cases (383–477), and the complete concrete
WallResource construction (879–1029). No local Lean compilation was performed.

The actual exported construction is indeed WallResource0. But its temporal
lemmas already take an arbitrary start x, and Resource itself is parameterized
by x. The natural hand generalization replaces state(t)=PhiS3^t(0) by
state_x(t)=PhiS3^t(x) throughout source/lowbit/highbit/exp/value. The source
at pair0 remains true; both of the first two state bits toggle independently
of x. At later pairs the same local identity high'=high XOR(low OR source)
holds. Thus the source-period and two pair-antiperiod assertions follow from
the existing generic TemporalCycles lemmas at x; the two one-doubling cases
do too. The polynomial reset/countdown lemmas take arbitrary Boolean streams,
so they impose no zero-start condition. This supplies the three Resource
axioms by the same substitutions. The generic return_of_resource then applies.

For a finite odd edge code R=2x+1, the edge map satisfies
T(2x+1)=2 PhiS3(x)+1, where PhiS3(x)=x XOR(2x OR4x OR3). Consequently
this parametrization would give the SAME half-rate bound for every normalized
finite seed. This is a hand source-level extension of the external argument,
not a new formal export or independently reviewed theorem. No hidden initial
resource assumption is needed: Resource asks for reset-before, reset-after and
countdown; exponent0=0 holds for every start.

**Disposition:** even the generic-scope distinction is unlikely to make the
three-fifths ceiling the strongest available bound. Keep it as a short explicit
forbidden-pattern explanation. The concrete next validation is to parameterize
the retained WallResource construction and compile it against its exact kit,
then seek an independent carrying read when a colleague is available. Do not
submit a weaker bound as a new best result. The original centre-conditioned
phase-error question remains open; changing this scope does not solve it.
