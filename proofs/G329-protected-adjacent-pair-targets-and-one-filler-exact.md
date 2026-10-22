# Protected adjacent pair targets and one filler: exact failures

*GPT's proofs, second-read. Derived from [PROOFS.md](../PROOFS.md), entry "G.GPT329. Protected adjacent pair targets
and one filler: exact failures (second-read by Cloud, 2026-10-20)"; rebuild with `python3 proofs/build.py`. Edit the
proof in PROOFS.md and this summary in [summaries.md](summaries.md), never this file.*

**Status:** proved by GPT and second-read by Cloud.

## In plain words

Under a safety margin, pairs aiming at totals one apart fit around a missing number except in two listed situations,
both ruled out by a big enough leftover bin.

**What it says.** Take the whole numbers from 0 up to some top value, remove one that is not at either end, and
share out the rest: some pairs of numbers must each add up to one total, some to the next total up, and one more
bin, the filler, takes every leftover number and has a total of its own. Suppose the requested totals add up to the
sum of the numbers, and a safety margin holds: every group of bins, short of all of them, asks for at least 1 + 2 +
... + n, where n is how many numbers it holds. Then the share-out fails in exactly two families of cases, and every
case in them does meet the margin. In the first family the pair totals are as high as the margin allows, in the
second they are one lower, and in each the missing number lies in a window fixed by how many pairs of each kind
there are and the filler's size. So the share-out always succeeds when the filler holds more numbers than there are
pairs, and, if no group sits exactly on its margin, when it holds as many.

**Why it matters.** The list of failures is complete and every case in it meets the margin, so both size rules are
exact: however many pairs of each kind there are, a filler one number smaller can fail under the same conditions. It
says nothing about pair totals further apart or about more than one filler.

**An everyday picture.** Among 0 to 9, the numbers that can pair up to 11 or 12 line up in a single row, 6, 5, 7, 4,
8, 3, 9, 2, where neighbours add to 11 and 12 in turn, so every such pair is a domino covering two neighbouring
squares. Take out 5, which cuts 6 off, and ask for two pairs making 11 and one making 12: the three dominoes must
cover 7, 4, 8, 3, 9, 2 exactly, and the only way, 7+4, 8+3 and 9+2, gives three 11s. A long row leaves squares to
spare for any mix; a row with almost none to spare lets the gap force too many dominoes of one kind.

## The formal statement and proof

**Review update, MI531 (2026-10-20): PROVED within project standards.**
Cloud CL469/64af1b21 independently verified the all-cut equivalence,
deletion lemma, two endpoint budgets and sharp thresholds. Its committed
g329_review.py reports49,797 admitted inputs to M22,1,020 failures
exactly in ranges A/B, zero mismatches. Supporting computation is reported,
not rerun here; the hand read carries the verdict. Adjacent targets and
one filler only; novelty UNASSESSED. Original filing status follows.

**PROOF-SKETCH; complete hand candidate, independent carrying read pending.**
GPT MI527–528. Known matching/reflection ingredients; novelty UNASSESSED.
No G327/G328, other unread partition result, experiment or numerical census
is a premise. The elementary path facts needed below are proved here.

**Statement.** Let r,s,c be positive integers, t=r+s and M=2t+c.
Let 1<=q<=M-1 and P=[0,M] minus{q}. There are r size2 bins targeting
integer u, s size2 bins targeting u+1, and one size-c bin targeting w.
Assume conservation tu+s+w=T_M-q, where T_n=n(n+1)/2. For every
nonempty proper group of bins J assume its total target is at least
T_(C_J), where C_J is its total size. A partition with these targets
fails to exist if and only if one of the following holds:

    A: u=2M-2t,    c<=q<=r;
    B: u=2M-2t-1,  c+r<=q<=t+min(r,c-1).

An empty displayed hole range contributes no failures. Every displayed
case satisfies all the assumed protection inequalities. Consequently
c>=t+1 guarantees completion for all protected inputs, sharply; if all
proper-group inequalities are STRICT, c>=t guarantees it, sharply.
These uniform thresholds hold for each positive r,s, not just one example.

**1. Reduce ALL protection inequalities.** A group of m pair bins,
containing k blue (target u+1) bins, has target mu+k and size2m.
The group of ALL t pair bins gives tu+s>=t(2t+1). Since 0<s<t and
u is integer this implies u>=2t+1. Conversely this lower bound makes
EVERY pair-only lower cut strict: mu+k-T_(2m)>=2m(t-m)+k,
positive for m<t, and equal to at least s>0 for m=t.

Every remaining nonempty proper group contains the filler. By total
conservation its lower bound is equivalent to an upper bound on its
complement, which consists of m pair bins, 1<=m<=t. That upper bound is

    mu+k <= T_M-q-T_(M-2m) = m(2M-2m+1)-q.

For fixed m the largest k is min(m,s), attainable since m<=r+s.
Put A0=2M-u+1 and g_m=m(A0-2m)-min(m,s). All these upper cuts hold
exactly when q<=min_(1<=m<=t) g_m. The successive differences

    g_(m+1)-g_m = A0-4m-2-1_(m<s)

strictly decrease (by4, or by3 at the colour-count boundary). Thus
g_m is discretely concave; its minimum is at m1 or mt. Protection is
therefore EXACTLY equivalent to

    u>=2t+1,
    q<=min(2M-u-2, t(2M-2t+1-u)-s).                        (329.1)

All proper cuts are strict exactly when the second line is strict;
the pair-only lower cuts are already strict. In particular the second
line forces u<=2M-2t. This proves admission, not just two necessary cuts.

**2. The actual adjacent-sum graph is one path plus isolates.** Colour
distinct-token sum-u pairs red and sum-(u+1) pairs blue. Each colour
is a matching. If u is even, put f=u/2; the path's ray ordering is

    f, f+1, f-1, f+2, f-2, ... , first BLUE.

If u is odd, put f=(u+1)/2; the ordering is

    f, f-1, f+1, f-2, f+2, ... , first RED.

In each case consecutive sums alternate u,u+1 as specified. Every
integer occurs once; applying either reflection x->u-x or x->u+1-x
gives exactly its neighbours, except that the fixed-point loop at f
is not an edge. Under(329.1), f lies inside[0,M]. The allowed positions
form an initial path segment, plus isolated later positions, of length

    E=min(u+1,2M-u)                                       (329.2)

EDGES. For even u, even ray positions survive to2f and odd positions
to2(M-f)-1; for odd u these bounds are2(M-f) and2f-1. This proves
(329.2) in both parities. Delete q from its actual position on this
path, or leave the path unchanged when q is isolated.

**3. A deletion from E>=2t+2 edges permits EVERY mixture of t pairs.**
An alternating path of length2k permits all quotas(a,b), a+b<=k:
orient it red-first and take the first a red edges and last b blue
edges. Their nearest indices differ by2(k-a-b)+3>=3. The same
construction on a red-ended length2k+1 path permits all a+b<=k,
and its unique perfect matching adds(k+1,0). The colour-reversed case
is identical. Uniqueness follows by forcing edges successively from
the first endpoint. Empty triangles/choices are allowed at k0.

If q is isolated or an endpoint of the original E-edge path, the
remaining path has triangle capacity at least t. For an internal q,
the two child lengths a,b sum to E-2. Their triangle capacities sum
to floor(a/2)+floor(b/2)>=floor((E-3)/2), hence at least t when
E>=2t+3. For E=2t+2, even child lengths also give capacity t.
If both child lengths are odd, write them2h-1,2k-1, h+k=t+1.
Their majority colours are opposite: their first edge positions differ
by an odd number because the removed vertex has even position.
If the budgets for both full-majority matchings were too small, their
sum t would be at most(h-1)+(k-1)=t-1, impossible. Fully match one
affordable child; the residual quotas have total t-h=k-1, or t-k=h-1,
and fit the other child's entire triangle. This proves the claim.

From(329.1), u+1>=2t+2. Thus every u<=2M-2t-2 has E>=2t+2
and completes. Only the two stated upper endpoints remain.

**4. Upper endpoint u=2M-2t.** Here(329.1) reduces exactly to q<=r:
the two upper-cut bounds are2t-2 and r, and r<=t-1. The filler target
is w=T_c+r-q. The actual path has E=2t, first BLUE, centre f=t+c,
and active tokens c,...,M. If q<c it is isolated and all quotas fit.
Otherwise c<=q<=r<t+c, and its ray position is p=2(f-q), an even
positive integer. At q=c it deletes the far endpoint, leaving an odd
path whose only size-t matching is all blue, incompatible with r>0.

At q>c the two children are odd. A size-t matching must be perfect
on both children: their total remaining vertex count is2t. The right
child is red-majority, with full cost q-c; the left is blue-majority,
with full cost t+c-q. Exact quotas would require r=q-c. But q<=r
and c>=1 contradict that equality. Thus precisely range A fails.

**5. Next endpoint u=2M-2t-1.** Now(329.1) reduces exactly to q<=t+r,
because its bounds are2t-1 and t+r, with r<=t-1. The filler target is
w=T_c+t+r-q. The path has E=2t+1, first RED, centre f=t+c,
active tokens c-1,...,M. An isolated deletion or either endpoint
deletion leaves enough triangle capacity, so completes.

For c<=q<f, the ray position is p=2(f-q)-1. Its left child has even
length and its right child odd length. Together their triangle capacity
is t-1; the right child's unique full matching is red, of cost
h=q-c+1. Hence quota(r,s) is possible exactly when r>=h: necessity
requires the one extra pair, and sufficiency fills the other child's
remaining triangle after taking that full red matching. Failure is
q>=c+r. Intersecting with q<f and q<=t+r gives precisely range B.

For q=f, deletion is at the first endpoint and succeeds. For q>f,
the left odd child instead has full red cost h=q-f; the other child
is even. The admission bound q<=t+r gives h<=r-c<r, so completion
always succeeds. These exhaust all possible q and prove the classification.

**6. Sharp thresholds and literal checks.** Range A needs c<=r<t.
Range B can be nonempty only when c<=t. Thus c>=t+1 eliminates both.
At c=t, its sole possible failure is B with q=t+r, where w=T_c is
tight. Strict protection excludes it, proving the strict guarantee c>=t.
For every positive r,s the choice c=t,u=2M-2t-1,q=t+r is an admitted
ordinary negative, establishing sharpness. For strict sharpness choose
c=t-1,u=2M-2t-1,q=t+r-1. It belongs to B; both upper bounds in(329.1)
strictly exceed q, so EVERY proper protection inequality is strict.
All these holes are internal since t>=2 and M=2t+c.

For r2,s1,t3, the old MI522 negative is M8,c2,q4,u9, targets9/9/10/4;
every proper cut is strict. At c3,M9,q5,u11, targets11/11/12/6 are the
ordinary sharp negative. Nearby c3,M9,q4 has the STRICT positive

    38 /29 /57 /016, targets11/11/12/7.

At c4,M10,q5,u13, the ordinary safe-boundary positive is

    49 /{3,10} /68 /0127, targets13/13/14/10.

Range A also has strict negatives: r3,s1,c2,M10,q2,u12 gives targets
12/12/12/13/4, admitted strictly by(329.1). These are hand sums,
cardinalities and path controls, not evidence replacing the infinite proof.

**Scope and verification.** Adjacent pair targets and ONE filler only.
This is independent of the old conditional full-four-bin parent and
does not solve multiple-filler allocation or arbitrary target gaps.
Known ingredients are rederived; no novelty or project PROVED status.
Independent review should carry the all-cut equivalence, E>=2t+2
deletion lemma, both endpoint colour budgets and threshold sharpness.


**Filing receipt (MI528).** The pre-filing in-memory duplicate controls pass;
nearest W327,W328,G305 were read in full. W327 concerns four arbitrary
full-interval sums with at most one size2 bin. W328 concerns exactly TWO
pair bins, arbitrary gap and c>=3: its adjacent-target subcase overlaps
our r=s=1 slice, which is reproved directly here, not assumed. G305 is
an E32 odd-partition parity-transfer construction. The present arbitrary
positive multiplicities/adjacent targets/exact failure ranges and sharp
filler thresholds are distinct from those statements. No status of any
older candidate changes, and none is a premise. The earlier failed
G329 neighbour lookup is recorded honestly in MI527. Post-filing
proof_dupes --near W329 passes347 entries, with the same three neighbours.
No generated proof page or TeX is edited.
