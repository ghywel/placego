# Protected count regions have no real/integer gap

*GPT's proofs, second-read. Derived from [PROOFS.md](../PROOFS.md), entry "G.GPT334. Protected count regions have no
real/integer gap (second-read by Cloud, 2026-10-20)"; rebuild with `python3 proofs/build.py`. Edit the proof in
PROOFS.md and this summary in [summaries.md](summaries.md), never this file.*

**Status:** proved by GPT and second-read by Cloud.

## In plain words

Four bins of three or more numbers sharing a run with one gap: given a margin, if fractional counts above the gap
fit, whole counts fit too.

**What it says.** Share a run of whole numbers from 0 with one gap (a missing number, not at either end) among four
bins with given sizes and target totals, at least three numbers to a bin. Each bin, and each group of two or three
bins, can reach its target only if the count of its numbers above the gap lies in a certain range. Suppose, as a
margin, that every such bin or group of n numbers wants at least 1 + 2 + ... + n (at least 6 for a bin of three).
Then if fractional counts can meet every range while sharing out all the numbers above the gap, whole-number counts
can too. The only way this could fail, found in G333, is a trap that pins every pair of bins to one exact count and
leaves every count ending in a half; here, pins like that need the missing number to be 5, 6 or 7, and even then
they cannot all hold at once.

**Why it matters.** It means the first step of one plan, choosing these counts before handing out the actual
numbers, never fails merely because counts must be whole. It does not show that suitable counts exist, even as
fractions, or that the bins can then be filled, so whether the margin always allows a sharing stays open. With four
bins of two numbers each, the trap really can happen, even with the margin.

**An everyday picture.** Four children share four marbles: Ann and Ben must have exactly one between them, Ann and
Cat two, and Ann and Dan two. On paper, only halves work (half a marble each for Ann and Ben, one and a half each
for Cat and Dan), and a marble cannot be split; loosen any one rule by one marble and whole marbles do. With three
or more numbers to a bin and the margin, the proof shows the bins are never cornered like this.

## The formal statement and proof

**Carrying review receipt: PROVED in the stated conditional scope, CL474/16404637; MI575.**
The independent read verified the exact complement identity, legal-count
monotonicity, scalar pin classification with the asymmetric reflected
bound, and every star/triangle case excluding the pinned half-count
obstruction. For baseline-protected four sizes>=3, REAL-nonempty P has
an integer point. REAL admission and zero/thin physical completion are
still OPEN. No census turns this conditional statement into the parent.
Cloud reports I1:487635 identity checks; I3:9370699 protected M12..15
inputs, no complement mismatch or REAL/integer gap, all P nonempty.
Both scripts were read fully, not replayed. I3 does not populate its
half_pins set, so no machine pin-type classification is adopted. The
carrying support is Cloud's hand re-derivation. Original proof text below
is unchanged; its candidate labels are historical. Novelty UNASSESSED.

### GPT G334 — Protected four-bin count admission has no real/integer gap (GPT, 2026-10-20; waiting room, MI565–566)

**Status: COMPLETE HAND PROOF CANDIDATE, not independently verified.**
This closes the rounding obstruction conditionally on REAL admission.
It does not establish real admission or physical partition completion.
Novelty UNASSESSED. The elementary vertex argument of G333 is included
below, so that its still-unread status is not a hidden premise.

**Statement.** Let M=sum_i c_i, with four integer sizes c_i>=3, and
1<=q<=M-1. Set H=M-q, S=T_M-q, T_v=v(v+1)/2, L(v)=v(v-1)/2.
Let integer targets t_i sum to S and satisfy t_J>=T_(C_J) for every
nonempty proper group J, where C_J=sum_(i in J)c_i. For a group of size
c and target t, let K(c,t) be the integer high-count interval admitted
by the two pools0..q-1 and q+1..M. Explicitly, for legal integers
max(0,c-q)<=r<=min(c,H), admission means

    f_c(r)=L(c-r)+(q+1)r+L(r) <=t
        <=g_c(r)=(c-r)(q-1)-L(c-r)+Mr-L(r).

These are exact fixed-count sum bounds; each row interval has consecutive
integer sums, and adding its low/high spectra gives the entire interval.
Both f and g strictly increase across legal consecutive counts. Thus
K is an integer interval whenever nonempty. Define P by sum k_i=H and
k(J) between the INTEGER endpoints of K(C_J,t_J), for all proper J.
If any K is empty, P is empty by definition. If P is REAL nonempty,
then P contains an integer vector. No claim about all vertices follows.

**Scalar pinning lemma.** Suppose c and e=M-c are at least6 and
T_c<=t<=S-T_e. Suppose K(c,t) is the singleton{r}, and the four
integers

    r, l=c-r, h=H-r, d=q-l

are all at least1. Then one of the following occurs, possibly after
replacing the group by its complement:

(i) q=7, c=6, r=1 and t=22;
(ii) H=7, 5<=q<=7, c=6, r=5 and t=6M-22.

Here complement changes(c,t,r,l,h,d) to(e,S-t,h,d,r,l), preserves
both protection bounds, and maps K to H-K exactly.

Proof of the lemma. The counts r-1 and r+1 are legal. Since r is
admitted and f,g increase, singleton admission implies

    g_c(r-1)<t<f_c(r+1).

An expansion gives

    g_c(r-1)-f_c(r+1)
        =(r-1)(h-1)+(l-1)(d-1)-6.

All quantities are integers, so the two strict inequalities require

    (r-1)(h-1)+(l-1)(d-1)<=4.                 (*)

If all r,l,h,d were at least2, put R=r-1,L=l-1,A=h-1,B=d-1.
Then R+L>=4, A+B>=4, and
RA+LB>=R+L+A+B-2>=6, contradicting(*). Some variable is1.
Complementation therefore lets us assume r=1 or l=1.

If r=1, then l>=5 and (l-1)(d-1)<=4. Either d=1, or d=2,l=5.
The first case has q=c and f_c(2)=L(c)+6<=T_c<=t, contrary to
pinning. The second has c6,q7, and g_6(0)=21,f_6(2)=23, forcing t22.

If l=1, then r>=5 and (r-1)(h-1)<=4. Either h=1, or h=2,r=5.
Use reflection ONLY as an algebraic change of coordinates: t'=cM-t,
q'=H. The reflected target has the explicit lower bound

    t'>=cM-(S-T_e)=L(c)+q.                    (**)

Do NOT assume baseline protection is invariant under reflection.
When h=1, H=c and q=e>=6. Pinning of the reflected high count1
would require t'<L(c)+6, contradicting(**). When h=2,r=5, we have
c6,H7. The reflected fixed-count thresholds are21 and23, so t'=22.
Then(**) gives q<=7, while e=q+1>=6 gives q>=5. This is(ii).
This proves the scalar lemma, including its asymmetric reflection bound.

**Exclude the only fractional obstruction.** Every k in P obeys
0<=k_i<=c_i. Any vertex on an integer singleton boundary is integral:
fixing that coordinate leaves three variables of integer total, and all
remaining subset constraints become integer singleton bounds. A vertex
of this box/sum section fixes at least two coordinates at integer
bounds; the third is integer by the total. This covers degeneracies.

Choose a vertex v of nonempty bounded P. If it is integer, stop.
Otherwise all singleton bounds are strict. In pair coordinates

    y=(k12,k13,k14),
    2k1=y1+y2+y3-H,
    2k2=y1-y2-y3+H,
    2k3=-y1+y2-y3+H,
    2k4=-y1-y2+y3+H,

v must be an integer corner of the pair box: an interior pair
coordinate could be perturbed in both directions while preserving
the strict singleton bounds. Therefore all four v_i are half-integers.
If any pair interval has positive width, an integer unit step toward
its other endpoint changes each v_i by plus or minus1/2. Every strict
integer singleton bound has at least1/2 slack at v, so this produces
an integer point still in P. It remains only the case of all three
complementary pair intervals pinned.

At this half-integral v, each individual high and low count is at
least1/2. For every pair, r,l,h,d in the scalar lemma are therefore
positive integers. Each pinned split12|34,13|24,14|23 supplies a
SIDE consisting of two size3 bins. In type(i) their high counts sum1,
so both equal1/2. In type(ii) their high counts sum5, so both equal5/2.
Choose one such side from each split. The resulting three edges on
four bins are pairwise intersecting (disjoint edges belong to the
same split); they form either a three-edge star or a triangle.

If q7 and H!=7, only type(i) is available. A star forces all four
high counts1/2, hence H2, whereas M>=12 gives H>=5. A triangle forces
three high counts1/2; the fourth would be H-3/2, larger than its size
M-9=H-2. Both are impossible.

If H7 and q!=7, only type(ii) is available (q5 or6). A star would
have total high count10, and a triangle already has high count15/2;
neither is compatible with total7 and nonnegative remaining counts.

Finally q=H=7 gives M14. A star would force all four sizes3, whose
sum is12, not14. In a triangle adjacent type(i)/(ii) edges are
incompatible, since their common size3 bin cannot have both1/2 and
5/2 high tokens. All three edges thus have the same type. The other
bin has size5; its high count would be11/2 or -1/2. Again impossible.
If neither q nor H is7, the scalar lemma permits no pinned split at
all. These cases exhaust the obstruction. An integer point exists.

**Can-fail controls and limits.** On M12,q7,counts3333, targets6/16/24/25
are protected (minimum one/two/three totals6/22/46; total71) and have
literal partition015/{2,6,8}/{3,9,12}/{4,10,11}. Pair12 has size6,
target22, high count EXACTLY1: g6(0)=21<f6(2)=23. Thus universal
positive pair width would be FALSE even within this theorem's scope.

On M12,q5,H7,counts3333, targets25/25/10/13 have minimum totals
10/23/48 and total73. Partition{4,10,11}/{6,7,12}/{0,1,9}/{2,3,8}
has pair12 target50=6M-22 and high count EXACTLY5: g6(4)=49 and
f6(6)=51. This retains the genuinely asymmetric reflected exception.
For comparison M20,q13,H7,c6,target98=6M-22 is NOT protected:
its allowed upper is92. Blind reflection would wrongly retain it.

The size2 control M8,q4,counts2222,targets5/5/11/11 has the real
half-integral point(1/2,1/2,3/2,3/2), pinned y=(1,2,2), totalH4,
and no integer point. It obeys baseline protection but violates the
minimum-size hypothesis. This is G333/CL472's genuine obstruction.
No census or machine proof was run. Fixed arithmetic checks are
self-checks only. REAL admission, zero/thin-row physical completion,
five bins and external novelty remain OPEN; independent review required.

**Filing receipt.** proof_dupes --near W334:352 entries, no repeats.
Nearest G319,W333,G326 read in FULL. G319 fixes positive counts in
three bins over two intervals; G326 is the protected three-bin H2
partition theorem. G333 supplies the general conditional parity
criterion but leaves protected exclusion open. G334 adds precisely
that exclusion, and repeats its short vertex argument to remain
self-contained. No statement of real feasibility or known-result
priority is imported from these neighbours. Review G333/G334 as one
packet; this replaces the earlier G333-only request rather than
opening a second independent review queue.
