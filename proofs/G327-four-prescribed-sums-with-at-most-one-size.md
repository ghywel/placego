# Four prescribed sums with at most one size-two bin

*GPT's proofs, second-read. Derived from [PROOFS.md](../PROOFS.md), entry "G.GPT327. Four prescribed sums with at
most one size-two bin (second-read by Cloud, 2026-10-20)"; rebuild with `python3 proofs/build.py`. Edit the proof in
PROOFS.md and this summary in [summaries.md](summaries.md), never this file.*

**Status:** proved by GPT and second-read by Cloud.

## In plain words

Four bins with set counts and set totals can share out a run of numbers from 0 exactly when no group of bins asks
for too little, even with one bin of two.

**What it says.** Take the numbers 0, 1, 2, … up to some last number, and four bins that between them must hold
every number exactly once. Each bin is told how many numbers it gets (at least two, with at most one bin getting
exactly two) and what they must add up to. The counts add up to how many numbers there are, and the totals add up to
the sum of all of them. One check is obviously needed: any one, two or three bins taken together must ask for at
least as much as that many of the smallest numbers would give. There are fourteen such groups, and the result says
these fourteen checks are also enough. The earlier proof G316 settled the case where every bin holds at least three
numbers; this one allows a single bin of two by starting from the tightest check, either filling one bin first and
handing the other three to the three-bin results G315 and G326, or splitting the run into its two ends and letting a
pair of bins share each end.

**Why it matters.** Each bin's total can be reachable on its own while the bins still get in each other's way, and
here fourteen simple sums settle whether all four can be filled together. It does not cover two or more bins of two:
on 0 to 9, bins of sizes 3, 2, 2 and 3 with totals 4, 8, 10 and 23 pass every check but cannot be filled. It says
nothing about five or more bins.

**An everyday picture.** Dealing every one of a run of raffle tickets numbered from 0 into four envelopes, each with
a set count of at least two and a set total of ticket numbers, and at most one envelope taking just two. As long as
no envelope, or group of envelopes, asks for less than its lowest tickets would make, the deal can always be done.
With two envelopes of just two tickets each, a pair of envelopes can still jam it.

## The formal statement and proof

**Review update, MI531 (2026-10-20): PROVED within project standards.**
Cloud CL468/0e3f4daa independently verified the carrying scalar spectra,
reflection, exact H2 root gate and strict-pair composition. Its committed
g327_review.py reports zero mismatches on all eleven size patterns to
N15, pair spectra to m300 and normalization N<60. Supporting computation
is reported, not rerun here; the hand read carries the verdict. Novelty
UNASSESSED; five-bin admission/multiple thin rows remain outside scope.
The candidate-status wording below records the original filing.

**PROOF-SKETCH, NOT independently verified.** This completes the formerly
conditional MI453 reduction using PROVED G326 (H2), with its new size-two
staircase audit spelled out below. G315/G316 supply the reviewed minimum-three
constructions; no G320–322, MI430 or MI460 is used. Novelty UNASSESSED.
The result concerns realization on a FULL interval, not count admission for
five bins or multiple thin rows. No new computation carries this candidate.

**Statement.** Let c_1,...,c_4>=2 total N, with at most one c_i=2, and let
integer targets s_i total L(N), where L(r)=r(r-1)/2. There is a partition of
{0,...,N-1} with cardinalities c_i and sums s_i if and only if

    S_I >= L(C_I) for every nonempty proper I subset{1,2,3,4},
    C_I=sum_(i in I)c_i, S_I=sum_(i in I)s_i.

The complementary lower bound is the corresponding upper bound
U_N(C_I)=C_I(2N-C_I-1)/2. There are fourteen lower cuts. If all sizes are
at least3 this is PROVED G316. Hence assume sizes(2,b,c,d), b,c,d>=3.
Necessity follows by taking the union of each group of bins.

**1. A scalar pair lemma on the two staircase shapes.** Use the explicit
P_m(h), Q_m(h) of FOUR-BIN-PARTITIONS §7, now m=c+2 with c>=3 and
0<=h<2c. Their pair spectra both contain the ENTIRE required interval

    [1+h, 2m-3].

For h0 they are the full interval. Otherwise write h=T_s+t, 0<=t<=s,
T_s=s(s+1)/2, and set p=m-s. Necessarily p>=3: if p<=2, then s>=m-2,
so T_s>=(m-2)(m-1)/2>=2(m-2), contrary to h<2(m-2), since m>=5.
The P pool is

    [0,p-1] union {p+2j+1+1_(j>=s-t): 0<=j<s}.

All-low pairs fill [1,2p-3]. For each high H_j, one low token gives
the complete interval [H_j,H_j+p-1]. Consecutive H_j differ by at most3;
these intervals therefore meet/touch because p>=3. The last endpoint is
2m-2+1_(t>0), beyond the required upper endpoint. The first high is
p+1+1_(t=s). It joins the all-low range except possibly when p3,t=s.
In that case m=s+3 and T_s+s<2s+2 imply s<=2. As m>=5, the only case
is m5,s2,t2,h5. Its pool is {0,1,2,5,7}; required pair sums6,7 are
{1,5},{0,7}. This covers all P cases without using an all-high spectrum.

For Q, t0 gives P. For t>=1, set S=s+1 and q=m-S=p-1>=2. Its pool is

    [0,q-1] union {q+2j+1-1_(j>=t): 0<=j<S}.

If q>=3, all-low pairs fill [1,2q-3]; the first high is q+1, so the
one-low/one-high intervals join it. High gaps are at most2 and those
intervals join each other. Their final endpoint is exactly2m-3.
If q2, m=s+3 and T_s+t<2s+2, with s>=2 and1<=t<=s. The only possibilities
are (m,h)=(5,4),(5,5),(6,7). The pools and ALL required sums are:

    Q5(4)={0,1,3,4,6}: 5={1,4},6={0,6},7={1,6};
    Q5(5)={0,1,3,5,6}: 6={0,6},7={1,6};
    Q6(7)={0,1,3,4,6,8}: 8={0,8},9={1,8}.

For s>=4, T_s+1>=2s+2, excluding additional cases. This proves the
size-two central lemma on BOTH shapes. It asserts only the protected
central interval; P5(5) really has a missing pair sum4.

**2. Choose the minimum of all fourteen cuts.** Put h_I=S_I-L(C_I) and
h=min_I h_I>=0. The reflection v->N-1-v sends h_I to the old h_(I^c):

    C_I(N-1)-S_I-L(C_I) = L(N)-S_I-L(N-C_I).

Consequently reflection preserves all cuts and the minimum. If a singleton
or triple attains h, reflect once if needed to make its singleton A have
size a and target s_A=L(a)+h. Treat this case in step3. Otherwise every
singleton/triple slack is STRICTLY larger than h; step4 treats a pair.
A pair tie with a singleton/triple belongs to step3.

**3. Singleton/triple minimum: the exact H2 interface.** Let J be any
nonempty proper group of the other three bins and put r=C_J. The cut of
A union J has slack at least h. Subtracting s_A gives

    S_J >= L(a+r)-L(a) = L(r)+ar.                 (3a)

Deleting ANY a values from the full pool cannot raise its r smallest
survivors beyond the original ranks a,...,a+r-1. Thus (3a) gives every
residual lower rank bound; complementary groups give the upper bounds.
This observation does not assume a compatible first bin or a joint partition.

The full-interval prefix/suffix/pivot recipe realizes every target of A.
Choose l smallest values, k largest values and pivot p, with l+k=a-1.
For fixed k the legal pivots fill [l,N-k-1]; successive target intervals
meet at the SAME extremal first-bin set, and cover [L(a),U_N(a)]. Put

    M=N-a, q=p-l, t_i=s_i-lc_i for the remaining bins.

The normalized remainder is [0,M] minus q, with0<=q<=M. Direct summation
of the chosen first bin gives

    h=kM+q,       sum t_i=L(M+1)-q.

The cuts J and A union J give, respectively,

    t_J >= L(r)+kM+q-lr,
    t_J >= L(r)+(k+1)r.

Thus the exact combined condition is

    t_J >= L(r)+max(kM+q-lr,(k+1)r).             (3b)

The remaining cut, that of ALL three other bins, is
(l+1)M-q>=h, equivalently (l+1-k)M>=2q. Together with A and the twelve
cuts in(3b), this accounts for all fourteen original lower cuts. In
particular every one of the SIX proper remaining groups satisfies

    t_J >= L(r)+r,

since k>=0. No symmetric protection after a second deletion is assumed.
Only the original full-interval problem was reflected; (3b) is computed
in its chosen orientation, not obtained by falsely reflecting H2's margin.

If q0 or M, trim the endpoint: the remainder is a full interval and all
three sizes are at least2. The PROVED three-bin full-interval lemma
(FOUR-BIN-PARTITIONS §5, MI295/G315) completes it from its actual rank cuts.
For internal q there are two possibilities:

- If a>=3, the remaining sizes are exactly(2,b',c'), b',c'>=3. Total
  conservation and all six inequalities above are precisely G326's H2
  hypotheses. That independently PROVED theorem completes the remainder.
- If a2, every remaining size is at least3. Apply G315 after checking its
  scalar hypotheses, not H2. A scalar minimum+1 omission requires q=r;
  its normalized target would be L(r)+1, whereas (3b) gives at least
  L(r)+r. A scalar maximum-1 omission is a minimum+1 omission for its
  complementary group of two remaining bins, excluded by the same bound.
  Actual rank bounds were already established for every group in(3a).
  Hence all three targets are in their actual scalar spectra and G315
  applies. This uses r>=3 for singleton groups and an even larger complement.

This covers every singleton/triple minimum, including ties and endpoint pivots.

**4. Strict pair minimum: one physical boundary, two scalar choices.**
Let AB attain h, with sizes a,b; the other two sizes are c,d. Relabel WITHIN
each pair so any size-two bin is the selected scalar bin on that side.
Set x=s_A-L(a), z=U_N(c)-s_C. Conservation and the four strict singleton
lower/upper inequalities give

    s_B=L(b)+ab+h-x,       U_N(d)-s_D=cd+h-z,
    h<x<ab,               h<z<cd.

In particular h<min(ab,cd). Put m=a+b, n=c+d. On the side containing
size2, step1 proves both staircase central spectra. On the other side,
use the PROVED minimum-three central lemma (FOUR-BIN-PARTITIONS §7).
For h>0 both m,n>=s+3: step1 proves this for the size-two side, and the
reviewed lemma proves it for the other. The ACTUAL complementary boundary
identity of §8 therefore still applies; its set calculation needs these
length bounds, not individual sizes>=3. For h0 take the ordinary prefix.

Choose that actual P_m(h) as the AB side of the original full interval.
Its reflected ACTUAL complement is Q_n(h) (P_n(h) when t0). The a-spectrum
of the first side contains [L(a)+h,L(a)+ab]; the c-spectrum of the reflected
other side contains [L(c)+h,L(c)+cd]. Choose A with sum L(a)+x and C' with
sum L(c)+z independently on these disjoint sides. Reflect C' back:

    sum C=c(N-1)-L(c)-z=U_N(c)-z=s_C.

The leftover sets on each side give B,D with their prescribed cardinalities
and sums, by conservation. No joint spectrum assumption or iterative swap
is used. Both sides share the exact complementary geometry already proved
in §8, including t0,t=s and empty high segments.

All possible locations of the minimum cut have now been covered. This is a
complete hand candidate for the one-size-two four-bin extension, conditional
only on its independent verification, with G315/G316/G326 already proved.
It makes no assertion about two or more size-two bins, five-bin count
selection, equal-sum novelty, or a new value of L8.


**Hand controls and filing receipt (MI504).** On0..10, counts(3,2,3,3)
and targets(6,8,24,17), the minimum among all14 cuts is3. Select
A={0,1,5}, with l2,k0,q3,M8. The normalized residual has H2 targets
(4,18,11), with its pair-plus-last-bin bound T(5)=15 met exactly.
The original literal partition is

    {0,1,5}; {2,6}; {7,8,9}; {3,4,10}.

This independently checks translation, the thin REMAINING bin, a tied
singleton/triple minimum and a protected group face. On0..10, counts(2,3,3,3)
and targets(3,17,17,18), the selected size-two bin instead gives the witness

    {0,3}; {1,6,10}; {2,7,8}; {4,5,9}.

The retained negative M8,q2,targets(8,6,20) has individual scalar feasibility
but no joint partition: the triples of sum6 consist only of{0,1,5}, which
meets each of the sum8 pairs{0,8},{1,7},{3,5}. It fails the H2 group cut
8+6>=T(5)=15. Thus the positive interface uses genuine group protection,
not an unsupported size-two extension of G315.

proof_dupes --near W327 passes345 entries; nearest G326,W324,G316 were
read in full. G326 is the protected three-bin dependency; G316 is the
minimum-three precursor explicitly extended; G324 fixes counts on TWO
labelled intervals with one singleton row. The present full-interval
one-size-two criterion is distinct, and no status of those entries changes.


**Scope supplement, MI505–506 (same-worker hand check, 2026-10-20).**
The endpoint recipe has h=kM+q, q0..M; adjacent ranges meet at the SAME
first-bin set. At h0 the strict-pair construction uses a prefix and its
actual full-interval complement. No new premise was found in these cases.
The one-size2 restriction cannot simply be removed: on0..9 the sizes
(3,2,2,3), targets(4,8,10,23) pass all14 cuts but do not partition.
The first triple is forced013, then pair8 is forced26; every available
pair10 hits26. MI506 gives all14 slacks and the unbounded(a,2,2,c) family,
a,c>=3, by the SAME W2 forced-extremes calculation already implicit in
MI308. A nearby positive control is013 /26 /47 /589 with targets
(4,8,11,22). This clarifies the candidate's exact scope; it is not a new
mechanism, an independent verification of G327 or another review request.
