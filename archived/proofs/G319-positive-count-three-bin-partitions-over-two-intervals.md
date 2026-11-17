# Positive-count three-bin partitions over two intervals

*GPT's proofs, second-read. Derived from [PROOFS.md](../PROOFS.md), entry "G.GPT319. Positive-count three-bin
partitions over two intervals (second-read by Cloud;2026-10-18;MI382)"; rebuild with `python3 proofs/build.py`. Edit
the proof in PROOFS.md and this summary in [summaries.md](summaries.md), never this file.*

**Status:** proved by GPT and second-read by Cloud.

## In plain words

Three groups can partition two labelled integer intervals with positive prescribed counts in each interval whenever their combined individual sum bounds and the total agree.

**Why it matters.** A feasible division of the sums between the intervals can be repaired when singleton choices collide. This proves compatibility for fixed positive count rows;it does not choose those counts for a larger partition problem. Independently verified by Cloud in CL442;novelty unassessed.

## The formal statement and proof

*Status:* PROVED in scope under two-tier review;Cloud carrying read CL442,commit9fd9bd0a.
The original proof and dependency receipts below are retained;their pending-review language is historical.
CL442 re-derived parts A-E,MI378 sections1-2,and MI380,including the scalar omissions and endpoint repairs.
Positive per-interval counts are essential;zero-count cases and subsequent applications are not promoted.
The reported217441 finite checks are supporting evidence,not the carrying verification.
Promotion receipt:MI436/GC1569. Novelty remains UNASSESSED.
*Where:* GPT-MATH-INSTINCT.md MI378,MI380,MI382. Novelty UNASSESSED.

**Statement.** Take two labelled copies of the integer intervals
[0,P-1],[0,Q-1]. Let l_i,k_i>=1 be integers for i=A,B,C,sum(l)=P,sum(k)=Q.
For integer targets v_i,there are partitions with these counts and combined bin sums v_i
if and only if sum(v)=L(P)+L(Q) and,for each i,

```text
L(l_i)+L(k_i)<=v_i<=l_i*(P-1)-L(l_i)+k_i*(Q-1)-L(k_i).
```

Here L(n)=n(n-1)/2. Translating either interval adds its fixed
count times the translation to each target,so the statement applies
to the original separated intervals. Copies are labelled;equal
normalized values in DIFFERENT copies are not a collision.

**A. Rank splitting and a fibre bound.** MI378 section1's integer
interval argument first splits v into low and high row sums meeting
each row's rank bounds and total. That argument uses no regularity
hypothesis until the final realization step. We now repair the split.
For any full interval of length n=a+b+c,hold its B sum z fixed.
The possible A sums within the rank region form the integer interval

```text
max(L(a),L(n)-z-U_c) <= s <= min(U_a,L(n)-z-L(c)),
U_j=j*(n-1)-L(j).
```

Its width is at least a*c. Indeed each of the four upper-minus-lower
endpoint differences is at least a*c:two are U_a-L(a)=a*(b+c)
and U_c-L(c)=c*(a+b);the others follow by substituting z=U_b
or z=L(b),respectively,and equal a*c at those extremes. Thus if
all three counts are positive,the fibre has at least two integers.
If the whole row has all counts>=2,it is realizable by the reviewed
full-interval three-bin theorem MI295,throughout this rank region.

**B. Both rows have at least two singleton bins.** Call such a row
thin. A thin row is actual exactly when its chosen singleton values
are distinct;its remaining bin takes the complement. Rank bounds
force their sum to lie between1 and2P-3. A collision x=z=t therefore
has1<=t<=P-2. If neither row collides there is nothing to do. Choose
a colliding row as low;the other row may itself collide.

If the singleton bin pairs coincide,call them A,B. Write the high
singletons y,w. Some one-coordinate unit move of (y,w),within
[0,Q-1]^2,makes them distinct:try a neighbour of y different from w;
if none exists,y is an endpoint and w its adjacent value,so move w
one step away from y (Q>=3). Compensate by the opposite move of
the matching low singleton t. It stays in range and differs from
the unchanged t. Both rows are now actual;C takes the complements.
The combined sum in each bin is unchanged.

If the pairs differ,relabel so low has A,C singleton and high has
A,B singleton. Low A=C=t,high A=y,B=w. Try changing low C to t+e
and high B to w+e,e=+1 or-1,keeping low A and high A fixed.
Both remaining-bin sums change by-e,so all combined targets stay
fixed. Choose a legal neighbour w+e different from y. This succeeds
unless (w,y)=(0,1) or(Q-1,Q-2). In the first exception instead
change low A to t+1 and swap high A,B from(1,0) to(0,1).
In the second change low A to t-1 and swap high A,B from(Q-2,Q-1)
to(Q-1,Q-2). Low C stays t. All values are legal and distinct;
complements give the correct remaining sums. This covers all thin
pairs,including rows(1,1,1),without a lattice-point counting argument.

**C. A regular positive row absorbs any other row's defect.** Here
regular means all three counts>=2. If the other row is also regular,
MI295 realizes both. If it is thin and collides at t,t,move either
one of its singleton values by one step and compensate in the same
bin of the regular row,keeping another bin's sum fixed. Both signs
are legal in the thin row;by partA at least one sign is rank-legal
in the regular row. Both resulting rows are actual.

Otherwise the other row has exactly one singleton,say low A= x,
with counts(1,b,c),b,c>=2. The reviewed one-hole lemma says a
rank-feasible row can fail only at x=b,B sum L(b)+1,or its reflected
upper case. In the lower case either x=b-1 or x=b+1 allows the
explicit B set{0,...,b-2,b},keeping B's sum fixed. Compensate in
high A while holding high B fixed. PartA again supplies a rank-legal
sign,and the regular row is actual. Reflect BOTH intervals for the
upper case. All targets transform and recover bijectively.

**D. Different singleton owners.** It remains useful to prove a
slightly broader repair:low counts(1,b,c),b,c>=2;high counts(a,1,d),
a,d>=1. Low A is singleton;high B is singleton. Here we repair a low-row
gap. PartE handles the orientations where only the high row fails.

Suppose the low row fails at its LOWER gap:low A=b,B sum L(b)+1.
Let high B=y,high A sum z. At fixed y,the high A rank fibre equals
its actual extreme interval after deleting y. Its possible omissions
have these three properties:

(i) Two values z-1,z+1 in that interval cannot both be missing.
(ii) If the minimum plus1 is missing,then y=a and the minimum is L(a).
(iii) If the maximum minus1 is missing,the width is at least2 and
      the maximum minus2 is present.

For a,d>=2 these follow from the reviewed one-hole spectrum lemma:
only extreme-distance1 omissions are possible;an internal deletion
has width>=a*d+1>=5,while endpoint deletions have none. If a=1,
the spectrum is simply[0,Q-1] minus y. If d=1,it is its reflected
complement spectrum L(Q)-y-([0,Q-1] minus y). These explicit sets
prove(i)-(iii) also when a or d equals1,including a=d=1,Q=3.
For clarity,in the d=1 case an internal y gives minimum
L(Q)-y-(Q-1);minimum+1 is missing exactly when y=Q-2=a,
and that minimum is L(a). Endpoint deletions give full intervals.

Try low A=b-1 or b+1,low B unchanged;high A becomes z+1 or z-1,
high B unchanged. Low B is realized by{0,...,b-2,b} for either
choice. The high fibre has width>=a*d>=1 by partA,so at least
one neighbour is rank-legal. If both are legal,(i) gives an actual
choice. If only one is legal and it is missing:

- The legal neighbour is z+1:then z is the fibre minimum and(ii)
  gives y=a,z=L(a). Keep low A=b and high A sum L(a),increase
  high B from a to a+1,and decrease low B sum from L(b)+1 to L(b).
  Use low B={0,...,b-1},high A={0,...,a-1};both avoid their
  respective singleton. High B=a+1 is legal since d>=1.
- The legal neighbour is z-1:then z is the fibre maximum. Instead
  put low A=b+2 and high A sum z-2,keeping B unchanged.
  Low A exists since c>=2 and avoids the same displayed low B set;
  (iii) supplies an actual high A set disjoint from high B=y.

Complements give C;every modification preserves all combined sums.
Reflection of both intervals handles a low upper gap. Thus ANY
low-row gap is repairable with this high singleton owner,whether
or not the original high row was actual.

**E. Exhaustion of row types.** PartB handles two thin rows and
partC handles any regular row. Remaining rows each have a singleton,
and at least one has exactly one. Choose such a row as low,with
singleton A. If high has a singleton in another bin,rename that bin
B and use partD whenever low is nonactual. If low is actual but high
is nonactual:

- If high also has exactly one singleton,swap the two rows and
  relabel its singleton A;the old low singleton is a different bin,
  so partD applies.
- If high has exactly two singleton bins sharing low's singleton,
  use MI380 with interval/bin relabelling. Its other two counts
  are the two >=2 counts of the old low row. Otherwise choose
  high's singleton pair B,C,disjoint from low's singleton A;this
  includes high(1,1,1).
  A high collision at t,t forces t internal. Change high B,C to
  t+e,t-e,for e=+1 or-1,and compensate low B,C sums by-e,+e,
  holding low A fixed. Both high pairs are legal and distinct.
  The low one-hole fibre has width>=b*c>=4;at least one neighbour
  is rank-legal,and two legal neighbours cannot both be missing.
  If the sole legal neighbour is missing,the original low B sum
  is its minimum or maximum. In the lower case the one-hole lemma
  forces low A=b,low B sum L(b). Instead increase low A to b+1
  and high C from t to t+1,keeping low B and high B unchanged.
  Low B={0,...,b-1} avoids its new singleton;high B,C are distinct.
  The low C sum falls1 and the high A sum falls1,so all combined
  targets are preserved. At the upper extreme low A=c,low B is
  the top b-set;decrease low A to c-1 and high C to t-1 instead.
  Again complements finish the construction. This argument also
  handles high(1,1,1):choose its B,C singleton pair,disjoint from
  the low A singleton,even though it has a third singleton.

For high thin rows with exactly two singletons SHARING low's A,
MI380 applies because the high remaining count is>=2 and low's
other two counts are>=2. The preceding disjoint-pair argument
handles every other thin row. Finally,if high has no singleton
except A,both rows have that same sole singleton and MI378 section2
supplies the shared-singleton spectrum/slide construction. Thus all
positive row pairs are covered. All unreviewed dependencies are
explicit:MI378's rank split/shared-singleton repair and MI380's
shared additional-singleton repair. Reviewed ingredients are MI295
and the one-hole scalar lemma;W318 is not used.


**Scope and dependency receipt.** Necessity is immediate from subset extrema.
The sufficiency above uses reviewed MI295 and the one-hole scalar lemma,
and provisional MI378/MI380. Review must include those latter carrying
repairs,not just the new case split. W318 is independent. The existing
MI380 diagnostic covers400 positive row pairs/44656 targets at lengths3..6;
it is supporting finite evidence,not a general proof. Zero counts are
excluded:rows(1,3,3)/(1,0,0) on lengths7/1 admit combined-rank target
(3,4,14),but no partition. Selecting positive counts for the original
protected targets remains OPEN;no five-bin,P_0,E28 or L8 conclusion.

**Filing comparison.** Native proof_dupes --near W319:337 entries,no
repeats. Nearest G315,G316,G301 read in full. G315 is a one-hole
three-bin criterion,G316 a full-interval four-bin cut criterion,and
G301 a known automatic-sequence result. The present statement fixes
positive counts separately on two interval copies;it is distinct from
those entries. The closest actual precursors are its explicitly cited
MI378/MI380 constructions,now combined with the remaining row types.

After the filing receipt,the nearest list is G315,G316,G317.
G317 also read in full:it concerns an interval missing1 and one
other value with bin sizes>=4,not separately prescribed counts
in two full intervals. No duplicate claim is identified.
