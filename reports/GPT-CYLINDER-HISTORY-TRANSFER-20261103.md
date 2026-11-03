# Cylinder gaps with the initial-vacuum branch retained — GC2598

GPT, 3 November2026. **PROVED hand/two-party after L1487, adopted GC2600:**
vacuum equivalence, generic completion and guarded white-witness criterion.
The complete hand carry and117-line check source were read; the bounded
M5 run is Local-reported, with no raw receipt read or Intel replay.
The original hand argument follows. At GC2598 it was PROOF-SKETCH.
Hand reasoning only on GPT's side:
no simulation, solver, compilation, new enumeration or certificate run.
This completes GC2594's queued variable comparison. Local owns the G16
prototype; this work does not duplicate it.

## Source and scope

Read all648 lines of [R30-20261103-b476c1](https://www.wolframcloud.com/obj/rule-30-prize/Agents/status/R30-20261103-b476c1),
*An Exact Cylinder Count for the White Center Times of Rule30*, attributed
to AIOvernight by the portal. Source SHA256
`3ad0168e6b49de01661ca02ce827c498792e2d9b5baefd7308f3cda32feb55bb`.
The COMPLETE19:14:56Z cached portal record says Lean Verified:211 constants,
six headline types matching, standard axioms, kit93d98bbe/Lean4.35.
That is a cached external status, not an Intel compile or a new live check.
[Read pins and scope](receipts/gc2598-cylinder-history-read.json).

The source's generic `zero_pairs_iff_solid`, `center_chain`, `right_core`,
`cylinder_white_iff`, `cylinder_iff`, `zeroPairs_down` and `gap_unique`
pass the hand read. Their hypotheses quantify over arbitrary Rule30
trajectories. In contrast, `gap_exists_of_white` uses the single seed
twice: a black initial cell contradicts an all-white cone, and the seed's
left light-cone boundary gives2g<=t. `white_black_count` then sums the
disjoint cylinders for1<=g<=t/2 in that specific seed pattern. Its second
identity uses the same fixed right-neighbour column at successive times.
It proves an exact count identity, with no positive-density lower bound.

Record searched: separate offline `record_find.py` searches for no-gap,
zero pairs, zeroPairs_down, white barrier and solid interval; cylinder
was a broad positive search, not a negative result. Actual cached kit
lean/equivalents, portal and open-PR sources were searched for the exact
declarations. The positive carrying match is b476c1 itself, particularly
the no-gap contradiction inside `gap_exists_of_white`. GC544/545/593 and
G122 concern solid-block collapse/ancestry; GC2594 supplies the retained
initial-assignment relation. Kitc42f6e5133f61a47e99289fd4b6e0536fd8a0453,
119entries/38openPRs at the last complete refresh. Network work stopped
after GC2597's incorrect portal endpoint returned403. Closed-PR linked
archives and primary literature were not freshly searched here; no novelty
or submission decision is made. These are explicit applications of the
known cylinder proof, not claims to a new cylinder mechanism.

## The missing branch, for an arbitrary initial row

Let X be any full-line trajectory with

    X(s+1,j) = X(s,j-1) XOR (X(s,j) OR X(s,j+1)).

Fix t>=1 and p. Define N(t,p), the absence of a gap, by

    X(t-j,p+j-2)=0 for every1<=j<=t.

The initial-vacuum identities are

    N(t,p) AND X(t,p)=0
      IFF X(0,i)=0 for every p-t<=i<=p+t;

    N(t,p) AND X(t,p)=0 AND X(t,p+1)=1
      IFF initial[p-t..p+t+1] = 0^(2t+1)1.

Here “vacuum” means only the displayed finite interval; all exterior cells
are arbitrary. This exposes the general conclusion already implicit in
the source's seed contradiction.

Proof of the first forward implication: translate p to0 and put D=t-2,
A_s=X(s,D-s), B_s=X(s,D+1-s), C_s=X(s,D+2-s). N says A_s=0 for0<=s<t.
Apply `center_chain` with u=0,k=t-1. From C_t=0 it gives C_1=0 and
B_s=0 for1<=s<t. The first update is

    C_1 = A_0 XOR(B_0 OR C_0) = B_0 OR C_0,

so B_0=C_0=0. Thus (A_s,B_s) is a zero pair at every0<=s<t.
`zeroPairs_down` gives initial depths D-2(t-1)..D+1, namely[-t,t-1],
all white. C_0 supplies the last cell t. Conversely, an all-white initial
cone[-t,t] forces C_t=0 by radius-one causality and quiescence. The cone
of A_s is[t-2-2s,t-2], contained in[-t,t] for every0<=s<t, so it also
forces N. The same proof works at t=1, with the intermediate index range
empty; it reduces to rule(0,b,c)=0 iff b=c=0.

For the second identity put R_s=X(s,D+3-s). `right_core`, with the same
u and k, gives R_t=rule(B_0,C_0,R_0)=R_0. Under the first identity this
is exactly X(0,t+1). Translation restores p.

## A disjoint decomposition that transfers to moving observations

For1<=g<=t set u=t-g. Let W_g(t,p) mean

    X(u,p-g..p+g-2) are all black,
    X(u,p+g-1) OR X(u,p+g) = 1.

Let B_g(t,p) replace the second line by

    (X(u,p+g-1),X(u,p+g),X(u,p+g+1)) in {010,011,100}.

Translate the source's generic cylinder theorems by p. W_g is equivalent
to X(t,p)=0 together with g being the least black witness on the ray
in N; B_g adds X(t,p+1)=1. For each trajectory there is either no black
witness on that finite ray, or a unique least one. Hence, using indicators,

    [X(t,p)=0] = [initial[p-t..p+t] all white] + sum(g=1..t)[W_g(t,p)],

    [X(t,p)=0 AND X(t,p+1)=1]
      = [initial[p-t..p+t+1]=0^(2t+1)1] + sum(g=1..t)[B_g(t,p)].

All terms on either right side are mutually exclusive for one physical
trajectory. The vacuum term and the full upper limit t are necessary
without extra hypotheses. An initial single black at p+t+1, with every
other cell white, gives the second event with no gap: the left edge of
that translated seed is at p+1 at time t. Separately, at t=1, initial
positions p-1..p+1 equal110 give a white output and gap g=1; the seed
center's2g<=t bound fails for this arbitrary row even when a gap exists.

The identities are pointwise, so p may be chosen separately at every
observation time. For the actual input history, evaluate every term on
the SAME initial assignment eta and intersect with the root and
Phi_(i-1) from [GC2594](GPT-ACTIVE-INPUT-FIBRES-20261103.md). An active
zero input at(t_i,p_i) is precisely the union of its vacuum and W_g
branches within that retained relation. No extra neighbour value may be
assumed: B_g applies only when a black neighbour is also established.
For an active one input use the complement of the zero-event relation.
At t_i=0 use the actual initial bit directly.

This is a case split on initial assignments, not a new supply of free
bits at time t_i-g. Those intermediate rows are deterministic images of
the same eta and need not be independent or uniformly distributed after
root/history conditioning. In particular, the fair-row cylinder size
3*2^(-2g-2) is not a path probability. Neither multiplying those numbers
nor independently choosing witnesses for successive gaps is justified.

## A concrete sufficient obstruction and the existing tick19 root

A useful contrapositive of the decomposition is the following guarded
criterion. Suppose some initial cell in[p-t,p+t] is black, and for EVERY
u=0..t-1 a known white cell lies in

    J_u = [p-t+u, p+t-u-2].

Then X(t,p)=1. The initial black excludes the vacuum term. For g=t-u,
the white witness in J_u excludes W_g's all-black interval, eliminating
every possible gap. The guard needs all t layers and a common actual
trajectory. It is sufficient, not necessary: initial100 at t=1,p=0
already forces output1 although J_0={-1} is black. The all-zero row shows
that the initial-black guard cannot be omitted.

Apply this only as a new reading of the already certified root word
0101010010001101110011101 on[-9,15], with t=19,p=10. Initial-8 is black
and lies in[-9,29]. The existing [GC2570 tableau](GPT-A4-COUNTERWORD-PROOF-CHECK-20261103.md#a-carrying-tableau-using-only-two-elementary-rules)
supplies the following white positions. Here J_u=[u-9,27-u].

|u|white position j_u|J_u|
|---:|---:|---|
|0|-9|[-9,27]|
|1|-7|[-8,26]|
|2|-7|[-7,25]|
|3|-5|[-6,24]|
|4|-5|[-5,23]|
|5|-3|[-4,22]|
|6|-3|[-3,21]|
|7|-1|[-2,20]|
|8|-1|[-1,19]|
|9|1|[0,18]|
|10|1|[1,17]|
|11|4|[2,16]|
|12|5|[3,15]|
|13|6|[4,14]|
|14|6|[5,13]|
|15|8|[6,12]|
|16|8|[7,11]|
|17|10|[8,10]|
|18|9|[9,9]|

Rows0..17 are direct reads of that carried tableau. Its row17 has110 on
8..10, giving X(18,9)=1 XOR(1 OR0)=0 for the last row. Thus each of
the19 gap branches fails, independently of all exterior initial bits.
This does not improve the established25-cell forcing guard, prove a
smaller certificate, or add an excluded path. The white witnesses inherit
their derivations from the existing proof; listing them is not a cheaper
derivation of those premises. It exposes what the cylinder representation
requires and gives a checkable example for a future guarded implementation.

## The fixed-column counting identity has a separate motion guard

Rule30 itself gives, for fixed p at a given time,

    [X(t,p)=0 AND X(t,p+1)=1]
      = [X(t,p+1)=1 AND X(t+1,p+1)=1].

For a moving observer r_t=X(t,p_t+1), this is a consecutive11 in r only
when p_(t+1)=p_t, or when the required two positions are separately proved
equal. A retreat changes that coordinate. For example, initial01010 on
[-2,2] gives101 on[-1,1] at time1. Choose p_1=0 and p_2=-1. Then the
white/black event at time1 holds and r_1=1, but r_2=X(2,0)=rule(1,0,1)=0.
Thus the moving-word11 identity fails. This does not by itself give an
active-input counterexample: active reads have their additional stay
guard, and the formula can be used precisely on those stayed steps if
the neighbour is known. Neither an ignored input nor a later active read
may silently be substituted for that next-time fixed-position neighbour.

## Next executable step and review boundary

Original request, now carried L1487: the exact vacuum
equivalence, its disjoint generic completion and the guarded white-witness
criterion. The ingredients are b476c1's existing proof, not a request to
rebuild its completed package. The tick19 table and moving-coordinate
counterexample are hand self-checks. The three requested mathematical
steps are now independently carried; no new compilation, external
submission or Human Verified status follows.

Next GPT: compare the already saved15-state observer's known colours
against these19 witnesses, by reading its existing trace/transition rule,
to identify exactly which witnesses it can express and which require
older initial bits. This is a finite representability audit of the saved
example, not a new product graph, horizon or search. If it lacks a witness,
record that coordinate and the required retained information; do not
enlarge the observer automatically. The independent alternative is the
public synthesis artifact read once network work can resume. Local
retains the G16 pilot. Both schedules remain ACTIVE, no GPT job.
