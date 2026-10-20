# Four prescribed sums in a consecutive integer interval

Consolidated exposition of project theorems **G315 and G316**.
Proof candidates were published on 17 October 2026 and independently reviewed by Claude Cloud
in CL436 and CL437, commits `55448489` and `7bfdfe34`.
This exposition reorganizes their carrying arguments; it makes no new mathematical claim.
The review's precise scope and the unresolved literature novelty are stated in Section 10.

## 1. Statement and notation

Write L(r)=r(r-1)/2 and U_N(r)=r(2N-r-1)/2.
For a finite ordered pool P, write alpha_P(r) and beta_P(r) for its least and greatest
r-element sums. Write Sigma_r(P) for its actual set of r-element sums.
An integer interval includes both endpoints; an empty prefix or suffix contributes no values.
All ranks below start at zero; min_r(P) is another notation for alpha_P(r).
For any other consecutive interval,translate all values and subtract the translation times
each bin size from its target. Thus the normalized statement covers translated intervals too.

**Theorem B (G316).** Let c_1,c_2,c_3,c_4>=3 be integers totaling N, and let integer targets
s_1,s_2,s_3,s_4 total L(N). There is a partition of {0,...,N-1} into four sets of those
cardinalities and sums if and only if, for every nonempty proper index set I,

```text
L(C_I) <= S_I <= U_N(C_I),
C_I=sum(c_i : i in I), S_I=sum(s_i : i in I).
```

There are fourteen nonempty proper index sets. With total conservation, the upper inequality
for I equals the lower inequality for its complement. We call these the cut conditions.
The proof is given in Section 9 after the scalar lemmas and one-hole completion theorem.

A full interval has every fixed-cardinality sum between its extrema: increase the selected
indices one at a time from the first r indices to the last r. Each increment changes the sum
by exactly one. This elementary fact also applies after translation.

## 2. Scalar sums after one deletion

**Lemma 2.**

Let P={0,...,M} minus{q},and 2<=r<=M-2. Its r-subset sums fill
the interval between their actual minimum and maximum,except possibly
minimum+1 when q=r,and maximum-1 when q=M-r. Both exclusions occur
if both equalities hold. There are no other holes in that spectrum.
Endpoint deletions q=0,M simply leave a full interval.

Derivation:split an r-subset into l=r-k values below q and k above.
Put u=M-q. The feasible k range is max(0,r-q)..min(r,u).
Each fixed k gives an ENTIRE interval [a_k,b_k] by the known
fixed-cardinality spectra on each of the two intervals,where

```text
a_k=L(l)+k(q+1)+L(k),
b_k=U_q(l)+k(q+1)+U_u(k),
L(t)=t(t-1)/2, U_v(t)=t(2v-t-1)/2.
```

Both endpoints increase strictly with k. At adjacent feasible k,k+1,
l>=1,k<=u-1,and elementary subtraction gives

```text
a_(k+1)-b_k-1
=1-(l-1)(q-l)-k(u-k-1).
```

Both products are nonnegative. Thus any gap contains exactly ONE
integer and requires l=1 OR q=l,and k=0 OR u=k+1. The corner
l=1,k0 means r1;the corner q=l,u=k+1 means r=M-1;both are excluded.
The remaining corners are k0,q=r (first gap,minimum+1) and
l=1,k=u-1,r=u (last gap,maximum-1). Their adjacent intervals do
not get filled by a farther k because both endpoints increase.
This exhausts the spectrum. Literal hand control:P={0,1,3,4},r2
has sums1,3,4,5,7,both predicted gaps2,6. That spectrum calculation
also holds at size2;it does not assert simultaneous sufficiency at that size.


## 3. Scalar sums after two deletions

**Lemma 3.**

Let R be an integer interval
with two values deleted,r+c=|R|,r,c>=3. Every r-subset sum between
its actual minimum and maximum occurs EXCEPT possibly minimum+1,
minimum+2,maximum-1,maximum-2. Here is a hand derivation,including
end slices;convex-hull bounds alone would not prove it.

Normalize the interval to0..U. An endpoint hole can be trimmed,
reducing to Lemma 2. For separated internal holes q<v-1,v,put
p=v-1 and u=U-v:the low pool0..v-1 minus q has p values;
the high full interval v+1..U has u values. For k high tokens
and l=r-k low tokens,the sum-range endpoints are

```text
a_k=L(l)+(l-q)_+ +k(v+1)+L(k),
b_k=l(v-1)-L(l)-(l-v+1+q)_+ +kU-L(k),
```

where L(t)=t(t-1)/2 and x_+=max(x,0). Whenever0<k<u,
the high subset spectrum is an interval of width k(u-k)>=1.
The low spectrum,by Lemma 2,misses at most isolated single integers:
this also holds for low size1 or complementary size1,where it is
literally a punctured list. Adding an interval of width>=1 fills
those isolated omissions. Thus every INTERIOR k slice is full.
Both a_k and b_k strictly increase with k. For consecutive legal
slices,with d=v-l>=1,the separating gap length before filling is

```text
G=a_(k+1)-b_k-1
=1-(l-1)d-k(u-k-1)+(l-1-q)_+ +(q-d+1)_+.
```

Because1<=q<=v-2,the last two terms sum to at most l-1.
Hence G<=1-(l-1)(d-1)-k(u-k-1). A positive G requires
l=1 or d=1,and k=0 or k=u-1. The r=1/c=1 corners are
excluded. The remaining corners are k0,l=p=r (a gap at global
minimum+1),and k=u-1,l=1,r=u (global maximum-1).

The nonfull END slices need a separate check. At k=0,if p-r>=2,
Lemma 2 gives only a low minimum+1 and/or low maximum-1 gap.
The former is global minimum+1. For the latter q=p-r=d-1,
G=1-(r-1)d+(r-d)_+<=-2,so k=1 already covers it.
If p-r=1,put v=r+2>=5 and B=b_0. The sole low omission is
B-q,and a_0=B-(v-1). Direct substitution gives

```text
a_1=B+4-v when q<=v-3;
a_1=B+5-v when q=v-2.
```

Thus every such omission is covered by k=1 except possibly
q=v-3 or v-2,at global minimum+2 or minimum+1. If p-r=0,
k0 is a singleton and the preceding adjacent-gap calculation applies.
At k=u write l=r-u,so p-l=c>=3. For l>=2,the low maximum-1
omission is global maximum-1;the low minimum+1 omission requires
q=l and is covered by k=u-1 because
G=1-lc+(l-c+1)_+<=-2. For l=1,writing H=sum(all high values),
the only omission is H+q,while the preceding maximum equals
H+v-4 for q<=v-3,and H+v-5 for q=v-2. Only q=v-3,v-2
can survive,at global maximum-2 or maximum-1. For l=0,the last
slice is a singleton and the adjacent-gap calculation applies.
These calculations also cover cases where k0 or ku is not legal:
there is then no corresponding end slice to inspect.

For consecutive internal holes q,q+1,the two blocks are full.
All fixed-k slices are complete,and the gap formula is

```text
G=2-(l-1)(q-l)-k(u-k-1), u=U-q-1.
```

Positive G needs the two products to sum0 or1. Sum0 leaves only
the first/last corners after r1/c1 are excluded,so omissions are
within2 of an extreme. Sum1 would force either l2,q3 with k0
or u-1,or k=1,u3 with l=1 or q. Each gives r2 or c2,excluded.
This proves the claimed two-hole localization in every case.

For later use,the exact lower-edge omissions have a particularly
short description. Write sorted R=z_0<...<z_(n-1),and
w_i=z_i-z_(i-1). Minimum+1 is absent iff w_r>=2.
Minimum+2 is absent iff w_r=3,or w_r=1 and
w_(r-1)=w_(r+1)=2. Indeed an increment<=2 can use only one
rank step,two steps by the last selected token,or one step each
by the last two selected tokens. Their costs are w_r,
w_r+w_(r+1),w_(r-1)+w_r. Complementation gives the upper edge.
No additional holes can hide away from these four positions by
the preceding slice calculation.


## 4. A structured three-deletion spectrum

**Lemma 4.**

Let 0<=p<=V-3 and

```text
R={0,...,V} minus{p,p+1,V-1},
u=V-p-2>=1, n=p+u=V-2=r+c, r,c>=3.
```

Thus R consists of p low values0..p-1 and u high values
p+2,...,V-2,V. The exact r-subset spectrum fills its actual
minimum/maximum interval apart from these possible omissions:

```text
minimum+1,minimum+2  if r=p;
maximum-1,maximum-2  if r=u;
minimum+3            if u=4 and c=3;
maximum-3            if u=4 and r=3.
```

Only legal r,c>=3 cases in this list apply. No other gap occurs.
For p=0,the pool is a translated one-hole pool missing its penultimate
value;Lemma 2 gives no gaps at these sizes. For u=1,the pool is a full
low interval plus one high value;the two slice ranges overlap as
shown below. Assume p>=1,u>=2 for the main calculation.

Split an r-subset by k high tokens,l=r-k low tokens. Write
L(t)=t(t-1)/2. The sum-range endpoints are

```text
a_k=L(l)+k(p+2)+L(k)+1_(k=u),
b_k=l(p-1)-L(l)+k(V-1)-L(k)+1_(k>0).
```

In the high pool,Lemma 2 gives a full k-subset interval except for
maximum-1 at k=1,and minimum+1 at k=u-1. This remains literally
true for high size1/complementary size1;for u=2 these coincide.
Low subset sums form an interval of width l(p-l). If0<l<p,
its width>=1 fills that isolated high omission. So every slice is
FULL except possibly k=1,l=p and k=u-1,l=0:the other l=0/p
combinations force r1 or c1. A missing entire slice cannot be
inferred by using only its endpoints;these are the actual exceptions.

Both a_k,b_k strictly increase. For consecutive legal slices,
with A=(l-1)(p-l),the separating gap expression is

```text
G=a_(k+1)-b_k-1
=2-A-k(u-k-1)+1_(k+1=u)-1_(k>0).
```

For0<k<u-1,this equals1-A-k(u-k-1)<=0.
At k0 or k=u-1 it is2-A. At k=0,r=l>=3,
positive G requires p=r:if p-r>=1,then A>=2.
This produces exactly the first two global gaps. At k=u-1,
the complement condition gives p-l=c-1>=2,so positive G
requires l=1,r=u,producing exactly the last two global gaps.
For u=1,there is only the join k=0->1,G=3-A;here r>=3
and p-r=c-1>=2 imply A>=4,so the ranges overlap.

Finally inspect the two possibly nonfull slices. If k=1,l=p,
then r=p+1,c=u-1>=3,so u>=4. Its maximum-1 hole is
covered by slice k2 when u>=5,because a_2-b_1=4-u<=-1.
For u=4,a_2=b_1,so it survives at GLOBAL minimum+3.
If k=u-1,l=0,then r=u-1>=3,c=p+1>=3. The previous
slice satisfies a_(u-1)-b_(u-2)=4-u. It covers the
minimum+1 omission when u>=5;at u=4 the omission survives
at global maximum-3. These are exactly the listed conditions.
There is no corresponding end slice when its k is illegal.
This proves the full structured spectrum calculation by hand.


## 5. Least-slack selection and the full-interval three-bin base


The following selection argument works for any ordered pool P of distinct values.
Let alpha(t) be its least t-value sum,beta(t) its greatest,together
with total T. Targets total T and obey their actual rank bounds.
Choose the least of all SIX singleton lower/upper slacks. Reflect values if necessary so selected bin A,size a,has
s_A=alpha(a)+h,and the other bins B,C have upper slacks>=h.
Let their sizes be b,c,so a+b+c=|P|. Conservation gives

```text
s_B >= T-alpha(a)-h-(beta(c)-h)
= alpha(a+b)-alpha(a),
s_C >= alpha(a+c)-alpha(a).
```

For ANY subset A of size a and sum s_A,the least b tokens in
R=P minus A sum AT MOST alpha(a+b)-alpha(a):deleting any a
values cannot raise the least b survivors beyond ranks a..a+b-1.
The same holds for c. Consequently the displayed target lower
bounds imply BOTH residual lower bounds,and s_B+s_C=sum(R)
gives both residual upper bounds. No compatible B subset is assumed.
Individual feasibility of the selected s_A supplies some A;the
problem is still to select one whose actual B spectrum contains s_B.


**Full-interval three-bin lemma.**

Let three sizes a,b,c>=2 total n,with prescribed sums totaling L(n)
and obeying the singleton rank bounds. Write alpha(t)=L(t),beta(t)=U_n(t). Among all six
singleton lower/upper slacks choose the least h. Reflect the values
if needed,so its bin A has s_A=L(a)+h. Other bins' upper slacks
are at least h. Conservation gives

```text
s_B >= L(a+b)-L(a)=L(b)+ab,
s_C >= L(a+c)-L(a)=L(c)+ac.
```

For ANY chosen size-a set A of sum s_A,removing a values cannot
make the smallest b remaining values exceed those at ranks a..a+b-1.
Thus these inequalities protect both residual lower bounds;their
complementary upper bounds follow from s_B+s_C=sum(remainder).
This is a rank argument,not an assumption of compatible bins.

Choose A as a prefix of length l,a suffix of length k,and one pivot,
where l+k=a-1. For each k=0,...,a-1,the pivot ranges from l to n-k-1.
The resulting sum intervals meet at their endpoints:the largest pivot
for k produces exactly the set obtained with the smallest pivot for
k+1. Together they cover all s_A in[L(a),U_n(a)]. The remainder is
[l,n-k-1] minus the pivot. After translating by l,it is0..b+c minus
one value r. The Lemma 2 elementary spectrum calculation says that
its b-subset sums can miss only minimum+1 when r=b,or maximum-1
when r=c. In the first case the original B target would be
L(b)+lb+1,contradicting s_B>=L(b)+ab because(a-l)b=(k+1)b>=2.
The second case is the same forbidden minimum+1 for C,excluded by
s_C>=L(c)+ac and c>=2. Therefore a B subset of the required sum
exists,and its complement supplies C. This proves the full-interval three-bin lemma using only Lemma 2,not a simultaneous one-hole theorem.


## 6. Three bins on a one-hole pool

**Theorem A (G315).** Let P={0,...,M} minus{q}, with a,b,c>=3 and a+b+c=M.
Integer targets summing to sum(P) can be realized simultaneously by a partition with these
cardinalities if and only if every target belongs to its own actual scalar spectrum.
By Lemma 2, this is equivalent to the actual rank bounds with the indicated at most two
edge omissions excluded. Necessity is immediate.

For sufficiency, original endpoint holes reduce to the full-interval lemma in Section 5.
Otherwise orient the least singleton slack lower, as in Section 5. We first establish that
a legal first-bin recipe or a missing-pivot repair exists, and then prove its completion.

**Existence of a pivot recipe or repair.**

For the actual
P=0..M minus q,use the a-1 extremal VALUES of P,not ranks treated
as unpunctured integers. For each k,l=a-1-k,pivots range between
the first/last remaining values. The MIN/MAX sum intervals for
successive k meet at the same extremal set;their union covers
[alpha(a),beta(a)]. Each pivot interval can miss only the value
q plus its fixed extremal sum. Thus an individually feasible s_A
is realized either by this recipe,or by a FORMAL recipe whose
pivot would be q. The latter is not a legitimate chosen subset.

When the pivot is q,the formal low prefix is0..l-1 and high suffix
u..M,u=M-k+1. If k>0 and u-q>=3,replace the formal pair{q,u}
by{q+1,u-1}. If l>0 and q-(l-1)>=3,replace{l-1,q} by
{l,q-1}. These preserve size and sum;the two new values are
available,distinct and not already chosen. At least one repair
exists when the remainder has size b+c>=6:

- If l,k>0,the two distances sum M-a+3>=9,so one is>=3.
- If l=0,the unrepairable distances1 or2 would make s_A respectively
  exceed its actual maximum,or equal the forbidden maximum-1 with
  q=M-a. Individual feasibility excludes both. The k0 case is the
  reflected minimum/minimum+1 argument.


**Legal pivots,including the endpoints.**


Let original P=0..M minus q have sorted values z_0,...,z_(M-1).
Choose l low tokens,k high tokens and a legal middle pivot p,
where l+k=a-1. Remove those tokens to get R of size b+c.
Deleting the pivot from the middle leaves its r least values
no larger than z_(l+1),...,z_(l+r),for either r=b,c.
The protected original bound is F_r=sum(z_a,...,z_(a+r-1)).
Since a=l+k+1 and distinct integer ranks differ by at least1,

```text
F_r-min_r(R) >= k*r.
```

All indices exist because r has a complementary bin of size>=3.
For k>=1,this is>=3. R is an integer interval with at most
two deletions;Lemma 3 localizes every scalar omission to within2
of its extrema. Both lower and complementary upper omissions
are therefore excluded. Trimming an endpoint deletion only makes
a full or one-hole interval;it does not invalidate the comparison.
No assumption that a missing pivot is legal is used here.

**The k=0 span classification.**
Put l=a-1,v=z_l. Original endpoint q0/M cases already reduce
to a full interval,so take0<q<M. If p=v,A consists of the
actual a smallest values:use the tight-face calculation below.
If p=M,the largest actual value,removing it leaves the original
first r middle values intact for r=b,c. Consequently

```text
F_r-min_r(R)=z_(l+r)-z_l >=r>=3.
```

The possible one original hole may be internal or trimmed;its
minimum+1/maximum-1 omissions are excluded by these two bounds.

Now let v<p<M. If q>l,then v=l and BOTH q and p are
internal to[l,M]. This is the internal-hole branch proved below,
including its explicit repaired triple exception;no endpoint
claim is being used to dispose of that exception. If q<=l,then
v=l+1 and q is outside the remaining span. The middle pool is
the full interval[v,M],with only p removed. Write j=p-v.
Its r-minimum and original bound are explicitly

```text
min_r(R)=rv+L(r)+(r-j)_+,
F_r=r(v+1)+L(r),
F_r-min_r(R)=min(r,j).
```

Its possible minimum+1 omission requires j=r,so the margin
is exactly r>=3. An upper omission is the corresponding lower
omission for the other bin,and uses that bin's same formula.
This closes the trimmed-original-hole case without a false
assertion that its minimum is always the full-interval minimum.
The alternatives q>l/q<=l,p=v/p=M/interior are exhaustive.

**The tight first-bin face.**
If p=v,A is the least a values. If q<a,the remainder is
a full interval and rank feasibility supplies the two-bin split.
Otherwise A=[0,a-1],R=[a,M] minus q. For a remaining size r
with other size t=M-a-r,the only possible scalar omissions are:

```text
- q=a+r,requested residual minimum+1. Then the OTHER
original target is beta(t)-1 and q=M-t. It is individually
forbidden in the ORIGINAL pool by Lemma 2.
- q=a+t=M-r,requested residual maximum-1. This equals
the SAME bin's original beta(r)-1,again forbidden by Lemma 2.
```

Here beta is the ORIGINAL maximal-cardinality sum,not a bound
from a reflected or truncated pool. Conservation gives the first
identity;the original r largest values remain available in R
for the second. Thus all tight-face holes are excluded,including
both kinds when the two remaining sizes happen to agree.


**The internal two-hole legal-pivot branch and its uniform exception.**


Use the notation above:original P=0..M minus q,A consists of l low
values,k high values and actual pivot p,where l+k=a-1. Assume
both q and p are INTERNAL to the remaining integer span;endpoint
and one-hole remainders are not needed for the argument below.
Then the prefix is0..l-1,the suffix starts M-k+1,and
R=[l,M-k] minus{q,p}. The least-slack argument gives

```text
s_B>=F_b=alpha(a+b)-alpha(a),
s_C>=F_c=alpha(a+c)-alpha(a).
```

Let z_j be the values of the ORIGINAL P in increasing rank order.
The least b values of R are bounded above by z_(l+1),...,z_(l+b)
(deleting only one pivot after the low prefix). Meanwhile F_b sums
z_(l+k+1),...,z_(l+k+b). Thus F_b-min_b(R)>=kb,and similarly
for c. If k>=1,these margins are>=3,so the two-hole calculation
excludes every possible missing B sum,including upper omissions
by using C and complementation. A completing B therefore exists.

It remains k=0. Then a=l+1,z_l=l,and,putting p'=p-l,

```text
F_b-min_b(R)=min(p',z_(l+b)-l)>=min(p',b).
```

The analogous identity holds for c. Thus a residual lower-edge
omission can matter only for p'=1 or2. If p'=1,minimum+2
cannot be a two-hole omission when b>=3,by the w description.
Minimum+1 requires q-l=b+1;then h=1,F_b=min_b(R)+1 and
the original C upper slack is1 with q=a+b=M-c. Lemma 2 says
this original C target is individually IMPOSSIBLE,contradiction.
If p'=2,only minimum+2 could matter. Its w characterization
forces b=3,q-l5:the alternative consecutive-hole boundary would
require b=2. This is the sole remaining internal-hole exception.
The same analysis for C handles upper-edge B omissions.

There is a uniform repair of this remaining exception. In absolute
values q=a+4,the chosen A is{0,...,a-2} union{a+1},
s_A=L(a)+2,and the problematic triple target is s_B=3a+3.
Replace A by

```text
A*={0,...,a-3} union{a-1,a},
B*={a-2,a+2,a+3}, C*=P minus(A* union B*).
```

A* has size a and sum L(a)+2;B* has size3 and sum3a+3.
They are disjoint,avoid q,and all values are in P because c>=3
and M=a+3+c. Conservation supplies exactly C's target and size.
If C was the problematic triple,interchange B,C. No pre-existing joint realization is assumed. This repairs the exceptional branch globally.


**High and low missing-pivot repairs.**


Return to
original P=0..M minus q,three sizes a,b,c>=3. Let alpha(t)
be the least t-value sum. Choose the least of all six singleton
slacks,and reflect the ORIGINAL problem once if necessary so
A's target is s_A=alpha(a)+h. As in Section 5,for r=b and r=c,

```text
s_r>=F_r=alpha(a+r)-alpha(a).
```

ANY actual first bin of size a and sum s_A leaves these two targets
inside their residual rank intervals. This does not assume joint
feasibility. A formal prefix/suffix/pivot construction with missing
pivot q has prefix0..l-1,suffix u0..M,where
l+k=a-1,u0=M-k+1. If k>=1,u0-q>=3,the high repair
replaces{q,u0} by{q+1,u0-1},leaving

```text
R=[l,u0] minus{q,q+1,u0-1}.
```

After shifting by l,this is Lemma 4 with V=u0-l,p=q-l and
u=V-p-2. The only LOWER-edge omissions for an r-subset are:
(i) distances1/2 if r=p; (ii) distance3 if r=p+1 and the
other size is3,u=4. Upper B omissions are lower C omissions by
complementation,so it is enough to exclude those lower cases.

Let z_j be original P's values in rank order. Because k>=1,
a=l+k+1>=l+2. Thus F_r=sum(z_a,...,z_(a+r-1)) is at
least the sum starting at rank l+2. In case(i),q=l+r,
the residual minimum is rl+L(r),while that rank segment sums
rl+L(r)+2r+2. Its margin is>=2r+2>2. In case(ii),
q=l+r-1,the residual minimum is rl+L(r)+2,while the
same rank segment sums rl+L(r)+2r+3. Its margin is
>=2r+1>3. All displayed ranks remain inside P because the
other bin has size>=3. Hence neither lower omission can be
requested,and the scalar B sum exists. C is its complement.

**Low repair:keep the original slack orientation.** If l>=1,q-(l-1)>=3,the low repair replaces
{l-1,q} by{l,q-1}. The remainder is

```text
R=[l-1,u0-1] minus{l,q-1,q}.
```

It is a reflection of the pool in Lemma 4,but the original
least-LOWER-slack choice was not reflected. Reflect the SPECTRUM
only,and check the original lower bounds directly. Put t=q-l.
The only lower-edge omissions of an r-subset are:
(i) distances1/2 when r=t-1; (ii) distance3 when t=5,r=3.
For(i),q=l+r+1,the residual minimum is L(r)+rl-1.
Since a=l+k+1>=l+1,F_r is at least the original rank segment
starting l+1,whose sum is L(r)+rl+r. The margin is>=r+1>2.
For(ii),the residual minimum is3l+2,and that rank segment
sums3l+6,giving margin>=4>3. Complementation excludes upper
omissions too. Therefore this actual repaired A also completes.
This direct check resolves the niggle that reflecting a construction
need not preserve the orientation of the selected least slack.


The pivot ranges cover the first-bin target range, meeting at their actual extreme sets.
A target either has a legal pivot or is the formal missing-pivot value in such a range.
The preceding cases cover every legal pivot and every available missing-pivot repair.
In each case the desired second-bin scalar sum exists; its complement supplies the third.
This proves Theorem A. No simultaneous partition was assumed in choosing its first bin.

## 7. Central spectra of a staircase and its conjugate

**Lemma 7.**

Let r,c>=3,m=r+c,and integer0<=h<rc. Set L(j)=j(j-1)/2
and T_j=j(j+1)/2. For h>0 choose s>=1,t with

```text
h=T_s+t, 0<=t<=s.
```

The Ferrers shape is staircase(s,s-1,...,1),with1 added to each
of its first t rows. Define p=m-s and the actual m-value pool

```text
P_m(h)={0,...,p-1} union {p+2j+1+1_(j>=s-t):0<=j<s}.
```

Its rank displacements are s-t initial values1,...,s-t,
then s-t+2,...,s+1 (omit the middle value);they sum T_s+t=h.
Consequently |P_m(h)|=m,sum(P_m(h))=L(m)+h.
The claim is

```text
Sigma_r(P_m(h)) contains every integer in[L(r)+h,L(r)+rc].
```

We also need the conjugate shape. For t=0,it is the same staircase.
For t>=1 put S=s+1,q=m-S and define

```text
Q_m(h)={0,...,q-1} union {q+2j+1-1_(j>=t):0<=j<S}.
```

Its positive rank displacements are1,2,...,t,t,t+1,...,s;
again their sum is h. Its claimed central interval is identical.
For h=0 both pools are the full interval0..m-1.

**Prefix sizes used in the proof are justified.** From h>=T_s
and h<rc<=m^2/4,we have m>=s+3. If m<=s+2 and s>=4,
then T_s>(s+2)^2/4>=m^2/4,a contradiction. For s<=3,
m<=s+2 contradicts m>=6. Hence p>=3 and,when t>=1,q>=2.
The auxiliary high blocks really fit and leave a low prefix;
we do not assume a large minimum bin beyond r,c>=3.


**Fullness of middle slices.**


The k-subsets
of an ordered high list admit a path from the k smallest to the
k largest by increasing one selected index at a time (move the
last to its final index,then the preceding one,and so on). If
every adjacent high gap is at most D,successive sums on this
path differ by at most D. Adding a REAL integer low-sum interval
of width at least D-1 makes the translated path intervals meet
or touch. Their union fills from the actual combined minimum
to maximum. This does not assert a complete high spectrum.
The k0/full-high endpoint paths have a single vertex and work too.

For P,high gaps<=3 and an interior low count has width
l(p-l)>=p-1>=2. For Q,high gaps<=2 and width
l(q-l)>=q-1>=1. Therefore all slices with0<l<p,or0<l<q,
are full. Unfilled all-low/all-high slices are not used.


**Endpoints and joins.**


Write L(x)=x(x-1)/2.
For p low values and s high values p+1+2j,the unperturbed
endpoints at k high tokens,l=r-k low tokens are

```text
a0_k=L(l)+k(p+1)+2L(k),
b0_k=l(p-1)-L(l)+k(p+1)+2[k(s-1)-L(k)].
```

Subtract b0_k from a0_(k+1) and then subtract1. Using
L(l-1)+L(l)=(l-1)^2 and L(k+1)+L(k)=k^2 gives

```text
G0=1-A-2B, A=(l-1)(p-l), B=k(s-k-1).
```

In P the high displacement is+1 at j>=s-t,so

```text
a_k=a0_k+(k-s+t)_+, b_k=b0_k+min(k,t),
G_P=1-A-2B+D_k,
D_k=(k+1-s+t)_+-min(k,t)<=1.
```

If the positive part vanishes,D_k<=0. Otherwise when k<=t,
D_k=1-s+t<=1,and when k>t,D_k=k+1-s<=0. In particular
t<s gives D_k<=0;t=s gives D_k=1 at every legal join.
Thus G_P<=2-A-2B. For an interior high-count join B>=1.
For a first or last high-count join with BOTH low counts
interior,the hypotheses r,c>=3 give A>=2. This covers s1
as well:its sole possible join is simultaneously first and last.
All P middle slices join.

For Q put S=s+1,q=m-S and use the SAME template with(p,s)
replaced by(q,S). Its high displacement is-1 at j>=t. Thus

```text
a_k=L(l)+k(q+1)+2L(k)-(k-t)_+,
b_k=l(q-1)-L(l)+k(q+1)+2[k(S-1)-L(k)]-min(k,S-t),
G_Q=1-A-2B+E_k,
E_k=min(k,S-t)-(k+1-t)_+,
A=(l-1)(q-l), B=k(S-k-1).
```

Here0<=k<=S-1 and1<=t<=S-1. Directly
E_k<=min(k,S-k-1):if k+1<=t,drop the subtracted0
and use S-t<=S-k-1;otherwise subtract k+1-t from
min(k,S-t)<=S-t. Also E_k=0 at k0,S-1. Hence
E_k<=B,including those boundaries. At ANY actual join between
two middle slices,l>=2,q-l>=1,so A>=1. Consequently

```text
G_Q<=1-A-B<=0.
```

Q therefore joins without requiring a correction<=1. The two pools use different valid bounds.


**Central containment.**


For low length p/high count s,the full middle counts range
max(0,r-p+1)<=k<=min(s,r-1). This interval is nonempty:
r-p+1<=s follows from c>=1,and r-p+1<=r-1 follows
from p>=2. The same applies to q,S.

For P,if r<=p-1 the first minimum is L(r). Otherwise put
k0=r-p;then c=s-k0>=3. Substitution at k=k0+1,l=p-1
gives the first minimum minus L(r) as

```text
T_(k0)+2k0+2+(k0+1-s+t)_+.
```

Since T_s-T_(k0)>=3k0+6 and the positive part is<=t,
the desired lower endpoint L(r)+h is at least k0+4 ABOVE
this minimum. If r>s,the last middle slice reaches the actual
maximum,at least U_m(r)=L(r)+rc by nonnegative rank
displacements. If r<=s,the last slice k=r-1,l=1 has maximum
minus U_m(r) at least

```text
(r-2)s-L(r)+2r-2 >=T_r-2>0.
```

For Q,the first minimum is L(r) if r<=q-1. Otherwise
k0=r-q,c=S-k0>=3,its excess over L(r) is

```text
T_(k0)+2k0+2-(k0+1-t)_+.
```

Here h=L(S)+t,and L(S)-T_(k0)>=2k0+3. The lower
endpoint margin is at least1+t+(k0+1-t)_+>=2. At the
upper end,r>S again reaches the actual maximum. If r<=S,
the last maximum minus U_m(r) is at least

```text
(r-2)S-L(r)+r-1 >=L(r)-1>0.
```

These substitutions confirm BOTH required endpoints lie within
the full middle union. h=0 uses ordinary interval spectra;for
t=0,the conjugate equals P. Prefix bounds p>=3,q>=2 are
justified at the start of this section from T_s<=h<rc and m>=6;no new large-size
assumption is introduced.


## 8. The two scalar pools are an actual complementary pair


Let
m=a+b,n=c+d,N=m+n,all four sizes>=3,and0<h<min(ab,cd).
Write h=T_s+t,0<=t<=s,p=m-s,as in Lemma 7. Its prefix bound
gives m,n>=s+3,so every interval below is inside0..N-1.
Set A=s-t. For t>0,the proposed boundary is exactly

```text
P=[0,p-1]
union {p+2j+1:0<=j<A}
union {p+2j+2:A<=j<s}.
```

In the window[p,p+2s],its ACTUAL missing positions are exactly

```text
E={p+2j:0<=j<=A},
O={p+2j+1:A<=j<s}.
```

These are disjoint by parity and have total s+1 values. The rest
of its complement is the suffix[p+2s+1,N-1]. Put q=n-s-1.
Reflection v->N-1-v sends the suffix to[0,q-1]. It sends
E to{q+2j:t<=j<=s},and O to{q+2j+1:0<=j<t}. Therefore

```text
{N-1-v:v in[0,N-1] minus P}
=[0,q-1]
union{q+2j+1:0<=j<t}
union{q+2j:t<=j<=s}
=Q_n(h).
```

This is equality of sets,not an equality of cardinality/moment.
It includes t=s:the first high segment of P is empty,but E still
contains its single required position p. For t=0,use the shorter
window[p,p+2s-1]. P takes its odd positions,the complement its
even positions,and the terminal suffix starts p+2s. Reflection
gives prefix0..n-s-1 and highs n-s+2j+1,0<=j<s,exactly P_n(h).
For h=0,P=[0,m-1],and the reflected complement is[0,n-1].
Thus neither the full-row nor empty-segment cases need a limiting
argument or an equal-total assumption.


## 9. Proof of the four-bin theorem

Assume the cut conditions. For every nonempty proper I, let h_I=S_I-L(C_I), and let
h be their minimum. Reflection of every original value in N-1 sends h_I to the old
h_(I-complement), preserving this minimum.

**Singleton or triple minimum,including ties.** If any singleton or triple attains h,
reflect if needed so A,size a,has s_A=L(a)+h. For any nonempty proper group J of the
other three bins,let K be its complement among those three. The upper slack of K is
h_(A union J)>=h. Therefore

```text
S_J >= L(N)-L(a)-h-[U_N(C_K)-h]
= L(a+C_J)-L(a).
```

Deleting ANY size-a first bin leaves its C_J smallest survivors no larger than original
ranks a,...,a+C_J-1. Thus every residual rank cut is protected. Choose A by the full-interval
prefix/suffix/pivot construction of Section 5, with l+k=a-1. Its remainder is an interval
minus at most one value. For a remaining size r,a possible residual minimum+1 gap requires
its target L(r)+lr+1. The displayed bound is L(r)+ar, and (a-l)r>=3, excluding the gap.
A maximum-1 gap is a minimum+1 gap for the TWO-bin complement,where the same argument
applies to its combined size. Hence all three targets are individually feasible in the
remainder. Theorem A completes it. A pair tied with a singleton/triple stays in this case.

**Strict closest pair.** Otherwise choose a pair AB attaining h, with sizes a,b; let the
other sizes be c,d. Put x=s_A-L(a) and z=U_N(c)-s_C. Since every singleton lower/upper
slack is strictly greater than h, conservation gives

```text
s_B=L(b)+ab+h-x,  U_N(d)-s_D=cd+h-z,
h<x<ab, h<z<cd.
```

In particular 0<=h<min(ab,cd). Sections 7-8 give one actual boundary P of size a+b,
with sum L(a+b)+h,whose a-spectrum contains [L(a)+h,L(a)+ab]. Its REFLECTED ACTUAL
complement has a c-spectrum containing [L(c)+h,L(c)+cd]. Choose A inside P with sum
L(a)+x and C' in that reflected complement with sum L(c)+z. Reflect C' back to C:

```text
sum(C)=c(N-1)-L(c)-z=U_N(c)-z=s_C.
```

The remaining values of P give B, and the remaining original complement gives D.
Their cardinalities and sums follow from conservation. These are two independent scalar
choices on disjoint actual sides,so there is no additional compatibility assumption.
This proves sufficiency. Necessity follows by applying the smallest/largest C_I token
sum bounds to every union of bins. Theorem B follows.

## 10. Scope,prior art,and verification

The mathematical statements are G315/G316 in [PROOFS.md](PROOFS.md). Their original detailed
calculations and retained failed shortcuts are in [GPT-MATH-INSTINCT.md](GPT-MATH-INSTINCT.md).
This exposition changes presentation only; the dated notebook preserves discovery history.

Known equal-sum predecessor: Daniel Kotlar,
[Distance magic labeling in complete 4-partite graphs](https://arxiv.org/html/1410.6916),
Theorem 1.6. It treats a common sum on 1,...,N,including sizes2. Translating our values
by1 changes each target to s_i+c_i. Thus its equal-sum slice is s_i=K-c_i;our minimum3
result is not an unrestricted replacement for all its size2 cases.
Hoory and Kotlar,[2605.06071v2](https://arxiv.org/html/2605.06071v2),Section5,distinguish
known equal-sum results from proposed prescribed-target generalizations. The bounded audit
in PRIOR-ART/MI342 did not find this exact arbitrary-target four-bin theorem.
**Novelty and priority remain unestablished.**

Cloud's CL436/CL437 independently reviewed the one-hole theorem,the four-bin reduction,
and the staircase construction. CL437 re-derived the P algebra and checked Q's correction
bound,retaining finite support for the remainder of its Q read rather than claiming a second
complete hand derivation. The author's explicit Q derivation is included in Section7.
The project adopted the results under its two-tier review rule;this is not an external peer
review or formal machine proof. Finite checks support the arguments and carry no infinite
quantifier. The exact review provenance is in the master entries.

The theorems concern three bins on a one-hole pool and four bins on a full interval,with
minimum size3. They prove no eight-bin criterion,E28/L8 threshold or listed prize statement.
No larger census is implicit in this exposition.

## 11. Exactly two bins of size two: verified classification

**PROVED within project standards, Cloud CL468/0e3f4daa; adopted MI531.**
The carrying read verified BOTH G327's scalar ingredient and G328's
classification AND the new root interfaces, physical size4 switch and
exhaustive composition below. This is not promotion by ingredient review
alone. Supporting parent22_review.py reports all fifteen size patterns
to N14 and explicit lifts/switches for a,c<80 with zero mismatches; not
rerun here. Novelty UNASSESSED. This supersedes historical unreviewed
references in this packet; sections12–15 remain unreviewed.

**Statement.** Let N=a+c+4, a,c>=3. Prescribe integer sums
(s_A,s_B,s_C,s_D) for counts(a,2,2,c), with total L(N). A partition of
0,...,N-1 exists exactly when all fourteen proper group cuts

    S_I>=L(C_I)

hold AND the input is not, up to permutation of labelled bins and full
value reflection v->N-1-v, the family

    F(a,c)=(L(a)+1, 2a+2, 2a+4, L(c)+(a+4)c-1).       (11.1)

Permutation carries each count with its target. Full reflection replaces
s_i by c_i(N-1)-s_i. It preserves the cut conditions. In fact (11.1) is
closed under reflection with a,c and the two pair labels exchanged.

### 11.1 Exact premises and verification boundary

| Ingredient | Exact use here | Status |
|---|---|---|
| Section5 full-interval three-bin lemma, sizes>=2 | Endpoint child | PROVED |
| [G326](PROOFS.md), protected one-hole counts(2,b,c), b,c>=3 | Selected size2 singleton | PROVED, CL466 |
| Sections7–8, minimum3 central spectra and actual complement | Large side of pair cut | PROVED G316, review provenance in Section10 |
| [G327 step1](PROOFS.md) only: both size2 P/Q central spectra, m>=5, h<2(m-2) | Separated size2 bins at strict pair minimum | PROVED, CL468 |
| [G328](PROOFS.md): exact three-entry protected(2,2,c) failure list | Larger singleton child | PROVED, CL468 |
| Sections11.2–11.5 below | Root interface, physical size4 switch, exhaustive composition | PROVED, CL468 carrying composition read |

This is a self-contained PARENT argument relative to those named
ingredients, not a replacement for its two ingredient proofs. Their full carrying calculations remain in the linked master
entries. The whole G327 four-bin conclusion is NOT used; G328 is independent
of G327. No G320–322, MI430, MI460 or finite census is a premise. Verifying
G327 and G328 alone would not automatically verify the new parent interfaces;
CL468 explicitly read those interfaces as well.
Explicitly, the size2 scalar premise says that for m=e+2, e>=3 and
0<=h<2e, BOTH P_m(h) and Q_m(h), of moment L(m)+h, contain a pair of
EVERY sum in [1+h,2m-3], with the needed length bound m>=s0+3 for
h=T_(s0)+t0>0. Only this premise from G327 is invoked below.

### 11.2 Necessity and the excluded family's actual obstruction

Every union of bins must meet its rank cut, so the fourteen inequalities
are necessary. The fourteen LOWER cut slacks for F(a,c) are

    A,B,C,D: 1, 2a+1, 2a+3, (a+4)c-1;
    AB,AC,AD,BC: 2, 4, 4c, 4a;
    BD,CD: (a+2)c+2a, (a+2)c+2a+2;
    ABC,ABD,ACD,BCD: 1, 2c+1, 2c+3, a(c+4)-1.

All are positive. A's target L(a)+1 uniquely forces [0,a-2] union{a};
D's target U_N(c)-1 uniquely forces {a+3} union[a+5,N-1]. This follows
by distributing the single unit of displacement above the minimum, or
below the maximum, in a sorted fixed-cardinality subset. Their complement
is {a-1,a+1,a+2,a+4}. Subtracting a-1 leaves {0,2,3,5}, while the two
pair targets become4 and6. That set has pair spectrum{2,3,5,7,8}, so neither
required sum exists. Thus F really is impossible despite all strict cuts.
This is the old MI308/MI506 forced-extremes mechanism, not a new obstruction.

### 11.3 A singleton or triple attains the minimum cut slack

Assume the cuts. Put h=min_I(S_I-L(C_I))>=0. Full reflection sends each
cut slack to its complementary old slack. If a singleton or triple attains
h, reflect once if needed so a selected singleton of size d has target
L(d)+h. Use the ordinary prefix/suffix/pivot recipe of Section5:
choose l low values, k high values, and a pivot p, with l+k=d-1. Set

    M=N-d, q=p-l, t_i=s_i-lc_i.

The actual translated remainder is [0,M] minus{q}, 0<=q<=M. Its moment
and the selected target give

    h=kM+q,   sum t_i=L(M+1)-q.

For any proper nonempty group J of remaining bins, write r=C_J. The
cuts J and selected-singleton union J, both with slack>=h, yield

    t_J>=L(r)+max(kM+q-lr,(k+1)r)>=L(r)+r.       (11.2)

For completeness the all-remaining cut yields (l+1-k)M>=2q. Formula
(11.2) comes from the FULL original interval in its chosen orientation;
it assumes no reflection-invariance of punctured-pool protection. It
accounts for the twelve cuts other than the selected singleton and its
complement. Child protection uses T_r=L(r)+r, not L(r).

The original cuts also give S_J>=L(r)+dr. After ANY d values have been
deleted, the r smallest survivors have sum at most L(r)+dr. Thus actual
rank cuts hold for every child group. If q0 or M, trim the endpoint and
use the proved full-three-bin lemma with sizes>=2. If d2, the internal
child has counts(2,a,c), a,c>=3; its conservation and six inequalities
(11.2) are exactly PROVED G326's hypotheses, so it partitions.

It remains to select a larger bin, renamed A of size a>=3. The internal
child has counts(2,2,c), M=c+4. By G328 it partitions unless its pair
targets u,v (interchangeable) and final target w are one of

    q1: (u,v,w)=(4,6,T_M-11), any M>=7;
    M7,q3: (3,8,14) or (4,10,11).

In EVERY exceptional row a pair has target at most4, while (11.2) demands
that target>=2k+3. Hence k0, l=a-1, h=q. The q1 row translates back to
exactly F(a,c), already excluded in the statement. The other rows have
c3, N=a+7, and respectively translate to

    (L(a)+3,2a+1,2a+6,3a+11),
    (L(a)+3,2a+2,2a+8,3a+8).

Both have direct partitions. Put A*=([0,a-1] minus{a-2}) union{a+1}.
The other three bins are respectively

    {a-2,a+3}, {a,a+6}, {a+2,a+4,a+5};
    {a-2,a+4}, {a+2,a+6}, {a,a+3,a+5}.

For every a>=3 these sets cover0..a+6 disjointly, and their sums are the
displayed targets; A* has sum L(a)+3. No changed child protection is
needed. Thus a bad canonical child in these two rows is not a bad parent.
All singleton/triple minimum cases, including ties, are now covered.

### 11.4 No singleton or triple attains the minimum: a strict pair

Let a pair of bins attain h and write its sizes r,s, with t,u on the other
side. As in Section9, put x=s_r-L(r), z=U_N(t)-s_t. Strict singleton/triple
comparisons and conservation give

    h<x<rs, h<z<tu, and h<min(rs,tu).             (11.3)

If the size2 bins are on different sides, relabel WITHIN each pair so
r=t=2; each side then has counts(2,large). Use the G327 scalar lemma
on BOTH P and Q shapes, selecting targets1+x and1+z respectively. Its length bound on
each side justifies the Section8 ACTUAL complementary set identity.
For h0 use ordinary full intervals. Choose the two scalar subsets on
these disjoint physical sides; reflecting the second back gives
s_t=t(N-1)-L(t)-z=U_N(t)-z. Their complements give the other two targets.

If the size2 bins are together, reflect the FULL interval if necessary
so their side is the lower pair cut attaining h. Recompute(11.3) in this
orientation with r=s=2 and t=a,u=c. Now h<x<4 with x integer,
so h0,1,2 are the only possibilities. Put n=a+c, N=n+4.

- h0: use low side0123; its reflected complement is0..n-1.
- h1: use low side0124, split12/04 for the required targets3/4.
  Its reflected ACTUAL complement is [0,n-2] union{n}=P_n(1).
- h2: strictness forces both pair targets4. P4(2)=0125 misses4;
  instead use Q4(2)=0134 and split04/13. Its ACTUAL complement is
  {2} union[5,N-1], reflecting to [0,n-2] union{n+1}=P_n(2).

For h0/1/2 the large reflected side has moment L(n)+h. The proved
minimum3 central lemma supplies its a-subset target L(a)+z, since
h<z<ac. Reflect it back, obtaining s_a=a(N-1)-L(a)-z; conservation gives
the last bin. This explicitly changes the physical boundary at h2,
not just a scalar representative on an incompatible boundary. The integer
strictness in(11.3) excludes h3; no minimum3 prefix estimate is used at4.

### 11.5 Exhaustion, controls and remaining verification

Every minimum proper cut is a singleton, triple or pair. Sections11.3–11.4
cover all inputs outside F using only the named premises. Section11.2 proves
F itself impossible. This completes the conditional characterization.
It remains a PROOF-SKETCH until the unread ingredients AND composition
receive independent scrutiny. No five-bin criterion, new L8 bound, or
extension to three size2 bins follows from this packet.

Literal controls retained from the notebook:

    F(3,3)=(4,8,10,23): impossible; near positive(4,8,11,22)=013/26/47/589.
    First q3 lift at a3: (6,7,12,20)=024/16/39/578.
    Second q3 lift at a3: (6,8,14,17)=024/17/59/368.
    Strict pair h2: counts(2,2,3,3), (4,4,18,19)=04/13/279/568.

Each string denotes its set of distinct tokens. These check actual sums,
disjointness and coverage by hand, not an infinite quantifier or independent
verification. No numerical experiment or formal proof checker was run.

**Precise comparison with the known common-sum slice (MI515–516).**
[Kotlar's Theorem1.6](https://arxiv.org/html/1410.6916v7) treats a common
sum on1..N. The shift u_i=s_i+c_i preserves all cut slacks because
u_J-T_(C_J)=s_J-L(C_J). Family(11.1) then has size2 targets2a+4 and2a+6.
Their difference2 persists under translation and reverses under full
reflection, so this obstruction cannot belong to that common-sum slice.
This is a scope check, not a new proof of the known result or verification
of our candidate; our count class also omits three/four size2 bins.
[Hoory–Kotlar2605.06071v2, section5](https://arxiv.org/html/2605.06071v2)
distinguishes unequal prescribed targets as a generalization. The bounded
source comparison found no exact counterpart to this classification;
novelty remains unassessed, not established by that search.

The shared cut conditions also coincide: if K is the common one-based
target and P_j sums the j smallest cardinalities, each j-bin group has
C_J>=P_j. The upper-rank function Uplus_N(r)=r(2N-r+1)/2 is increasing,
so jK<=Uplus_N(P_j) implies every group upper cut. Conservation yields
all lower cuts; the converse follows by taking the smallest-count groups.
Thus the candidate agrees with the known slice's EXACT conditions in its
shared count domain, not merely with a smaller sufficient subregion.

### 11.6 Direct equal-pair child simplification (MI517–518)

**Elementary hand argument, not independently verified; no separate proof
filing or review request.** In the singleton reduction, if the two original
size2 targets are equal, they stay equal after normalization. Their child
can be completed without G328's obstruction classification as follows.

On P=[0,M] minus internal q, M=c+4>=7, let targets(u,u,w) conserve the sum
and satisfy all six protected cuts. The two-pair union and filler imply
10<=2u<=4M-6-q, hence5<=u<=2M-4. Before deletion the sum-u fibre has
floor((min(u,2M-u)+1)/2) edges, and every two distinct edges in that SAME
fibre are disjoint. For5<=u<=2M-5 there are at least three edges, so one
deletion leaves at least two. At u=2M-4 there are exactly the edges
{M-4,M},{M-3,M-1}; the upper inequality forces q<=2, below all four
endpoints since M-4=c>=3. Neither edge is removed. Choose those two
edges and put all other tokens in the filler.

The minimum filler size matters: M6,q2,targets(8,8,3), counts(2,2,2),
meet all six protected cuts and have individually feasible targets, but
sum8 has only35 after deletion of26. This is a negative control outside
the stated c>=3 domain, not a broader classification.
The symmetric full-four-bin slice therefore avoids G328 as a premise;
it still needs the unread size2 scalar lemma for separated strict-pair
sides and a carrying read of its composition. The arbitrary-target parent
in Section11 still depends on G328. No proof status is promoted here.

## 12. Elementary matching application: repeated equal pairs and one filler

**HAND DERIVATION, not independently verified; novelty unassessed.**
MI519–520. This independently chosen mechanism question is not an extension
of the four-bin parent proof and uses neither G327 nor G328. Its ingredient
is the ordinary fixed-sum pair matching/count. Known equal-pair consumption
arguments appear in [Hoory–Kotlar2605.06071v2, section2.1](https://arxiv.org/html/2605.06071v2);
that source treats full1-based common-sum instances, not the specialization
below. No new PROOFS filing, routine review job or numerical census is made.
A carrying read is required before adopting this characterization as PROVED.

Put T_j=j(j+1)/2. Let r,c>=1, M=2r+c, and P=[0,M] minus{q}, with
1<=q<=M-1. There are r bins of size2 with common target u, and one bin
of size c with target w. Assume integer targets, ru+w=T_M-q, and every
nonempty PROPER group of bins has target at least T_(its total count).
Then a partition exists unless

    u=2M-2r and c<=q<=r.                        (12.1)

Every input in(12.1), with w determined by conservation, actually satisfies
all those protected cuts and has no partition. Thus this is an exact
characterization within the stated class, conditional on the hand argument.

**One fibre controls the WHOLE allocation.** Distinct edges of the same
sum-u fibre are disjoint, and after choosing r edges the complement has
exactly c tokens and the target w. So a partition exists iff that fibre
has at least r edges. The all-pair union and filler cuts give

    ru>=T_(2r)=r(2r+1),
    ru<=T_M-q-T_c=r(2M-2r+1)-q.

Since q>0 and u integer,

    2r+1<=u<=2M-2r.                            (12.2)

Before deletion there are e0(u)=floor((min(u,2M-u)+1)/2) edges. If
u<=2M-2r-1, (12.2) gives e0(u)>=r+1. One hole destroys at most one,
leaving at least r. No classification of individual low/high exceptions
or an assumption about independent representative choices is used.

At u=2M-2r there are EXACTLY r edges:

    {c+i,M-i}, i=0,...,r-1.

The upper cut above forces q<=r. Such a q cannot hit a high endpoint
M-r+1=r+c+1 or the unmatched midpoint r+c. It hits a low endpoint
precisely when c<=q<=r. Deleting it then leaves exactly r-1 edges; otherwise
all r survive. This proves the partition/nonpartition dichotomy.

**The negatives are actual admitted inputs.** In(12.1), conservation gives
w=T_c+r-q. A group of j pair bins, 1<=j<=r, has protected cut slack

    j[u-(2j+1)]=j(2r+2c-2j-1)>0.

A group consisting of the filler and j pair bins, 0<=j<=r-1, has slack

    r-q+j(2r-2j-1)>=0.

These are ALL proper groups. The second range must stop at r-1: the whole
punctured pool is not a protected proper group. Hence every negative is
admitted. All proper cuts are STRICT when q<r; only the filler cut is
tight when q=r. In particular ordinary protection guarantees existence
uniformly if c>=r+1, sharply; strict protection guarantees it if c>=r,
also sharply. These thresholds come from the exact obstruction, not a
successive margin-repair guess.

**Literal controls.** r2,c2,q2 gives MI518's8/8/3 negative. At r1,c1,q1,
P={0,2,3}, targets4/1 meet protection but no sum4 pair exists. For three
pair bins, M8,c2,q2, targets(10,10,10,4) pass EVERY protected cut strictly:
sum10 has only37 and46 after28 is deleted, so three disjoint pairs cannot
be chosen. All individual targets are feasible, including filler04.
Moving that hole to q1 gives the positive partition

    28 /37 /46 /05, targets(10,10,10,5).

The interior control at q2 is18 /36 /45 /07, targets(9,9,9,7).
The safe upper endpoint r3,c4,M10,q3 uses

    {4,10} /59 /68 /{0,1,2,7}, targets(14,14,14,10).

All are hand cardinality/sum/coverage checks, not a computed range or an
independent review. Multiple fillers or unequal pair targets are not covered;
the complement would no longer be automatic or the edges a single matching.

## 13. Two distinct pair sums: path components and a colour-quota obstruction

**Elementary hand argument and countercontrol, MI521–522; not independently
reviewed and not a premise of the earlier parent classification.** Prescribed
edge-colour counts belong to the known Exact Matching framework; see the
dated PRIOR-ART note. Neither this representation nor weighted matching
certificates are claimed new.

For any finite set P of distinct real tokens and u!=v, let E_u and E_v
be its unordered DISTINCT-token pairs with the indicated sums. Each
colour is a matching, so their union has degree at most2 and alternating
colours along each component. An alternating cycle of length2k would
cover its vertices once by k sum-u edges and once by k sum-v edges.
Adding the token labels gives ku=kv, impossible. Thus the union is a
forest of alternating paths and isolated vertices. The C4 case was
already used in MI303/G328; this is the same elementary sum argument
for arbitrary cycle length, not a new imported graph theorem.

Nevertheless, the three necessary conditions

    |E_u|>=r, |E_v|>=s, nu(E_u union E_v)>=r+s

are NOT sufficient to choose disjoint pairs with quotas(r,s). Here nu
is ordinary maximum matching size. The failure occurs on an actual
protected one-hole interval, not only an abstract coloured graph.

Take P=[0,8] minus{4}, red target9, blue target10. The complete fibres are

    E_9 ={18,27,36},       E_10={28,37}.

The graph is the single path

    1 --R-- 8 --B-- 2 --R-- 7 --B-- 3 --R-- 6,

with isolated vertices0,5. Its matching number is3; its UNIQUE matching
of size3 is18/27/36, all red. Indeed endpoint1 forces18 in any perfect
matching of the six path vertices, then endpoint2 of the remaining path
forces27, then36. Any matching with2 red and1 blue would have size3,
contradicting uniqueness. Yet the red count3>=2, blue count2>=1 and
ordinary matching number3>=3 all hold.

This is also a four-pair prescribed partition obstruction with targets
(9,9,10,4), whose total32 is the sum of P. Every proper group satisfies
the protected cut STRICTLY: for one, two or three bins, the smallest
group targets are4,13,22, exceeding T_2=3,T_4=10,T_6=21. Each individual
target is feasible, including filler4 via13. Failure is therefore neither
an individual scalar hole nor an insufficient count for either colour
nor insufficient TOTAL matching capacity. It is a conflict of quotas
within a single path component. This does not contradict G328, whose
counts(2,2,c) require c>=3; here the remaining filler has size2.

**A weighted certificate on the SAME example.** Give the path vertices
(1,8,2,7,3,6) weights(0,2,1,1,2,0), and the two isolated vertices weight0.
The total weight is6. Each red edge has endpoint weight2, each blue edge
endpoint weight3. Since a matching cannot reuse a vertex and all weights
are nonnegative, any matching with a red and b blue edges satisfies

    2a+3b<=6.

Quotas(2,1) require7>6. This directly proves the obstruction without
invoking a matching-duality theorem. It shows what the three coarse
counts omitted: a weighted joint capacity constraint. It is not a claim
that one such inequality, or all such tests on arbitrary graphs, solve
the partition problem.

**Independent positive controls.** On the SAME P,18/37 is a red-blue
matching, so MI303's one-of-each compatibility remains intact. The
complete partition18/27/36/05 has targets(9,9,9,5), confirming ordinary
capacity3 is attainable and the hole itself does not force failure.
The blue-only matching28/37 confirms its full count2. All pairs have
distinct endpoints;55 is not an edge, and deleted4 removes45 and46.

What changes: two-sum packing has a global path representation, but its
coarse capacity criterion is refuted. The next question is the exact
colour-quota region of an alternating path and how independent components
combine. No larger census, extra parent coverage or proof-status upgrade
follows. G327/G328 and the earlier parent interfaces remain unreviewed.

## 14. Exact two-colour quotas on a forest of alternating paths

**Self-contained elementary hand derivation, MI523–524; unreviewed.**
Known matching ingredients, no originality or general-graph algorithm claim.
This section is independent of the conditional four-bin parent. Its proof
does not use G327/G328 or any other unread partition result. Length means
NUMBER OF EDGES throughout, not vertices; isolated vertices have length0.

### 14.1 One path: a triangle and possibly one extra point

For nonnegative integers a,b, an alternating path of length2k admits
exactly the red/blue quotas

    a+b<=k.                                                   (14.1)

A path of length2k+1 whose two end edges are red admits exactly

    a+b<=k, OR (a,b)=(k+1,0).                                 (14.2)

Interchange colours if the end edges are blue. This includes k0: an
isolated vertex permits only(0,0); a single red edge permits(0,0),(1,0).

**Necessity.** The even-length path has2k+1 vertices, so at most k edges
can be matched. The odd-length path has2k+2 vertices, so at most k+1
can be matched. A matching of size k+1 is perfect. Its first endpoint
forces edge1; removing its two endpoints forces edge3, then5, and so on.
It is therefore the unique perfect matching, all in the end-edge colour.

**Sufficiency of EVERY triangle point.** At k0 the triangle consists of
the empty matching. For k>0 orient an even path to start red, and number
its edges1,...,2k. For an odd red-ended path number
them1,...,2k+1. Choose the first a red edges at positions
1,3,...,2a-1, and the last b blue edges at positions
2k-2b+2,2k-2b+4,...,2k. Empty choices are allowed. Within either list
the edges are disjoint. When both lists are nonempty their closest
indices differ by2(k-a-b)+3>=3, so they also share no endpoint across
lists. This constructs every a+b<=k. For the extra point in(14.2),
choose all odd-indexed edges. The blue-ended case follows by swapping
the colour names. This is the elementary prefix/suffix construction
already visible in the matching literature, specialized here to paths.

### 14.2 An exact criterion for ALL components together

Let the forest's path lengths be ell_i, and put

    k_i=floor(ell_i/2),        K=sum_i k_i.

Each odd-length component has a majority colour (its two end edges'
colour). Its full matching has w_i=k_i+1 edges, all in that colour.
Sort these w_i increasingly within the red-majority components and
within the blue-majority components. For integer budgets r,s>=0 define

    alpha(r)=maximum j for which the j smallest RED w_i sum to <=r;
    beta(s) =maximum j for which the j smallest BLUE w_i sum to <=s.

The empty prefix is allowed. Then a matching with EXACTLY r red and s
blue edges exists if and only if

    r+s <= K+alpha(r)+beta(s).                                (14.3)

Thus the full quota support depends only on the even components'
baseline capacities and the odd components' majority colours/lengths.
No search over individual edges is needed to state the criterion.

**Necessity.** In any matching call an odd component full when it uses
k_i+1 edges. By(14.2) it is then monochromatic. Every other component
uses at most k_i edges. If x red-majority and y blue-majority components
are full, the matching has at most K+x+y edges. Their full red matchings
cost at most r red edges in total, hence the x smallest red w_i also
sum to at most r, giving x<=alpha(r). Likewise y<=beta(s). This gives
(14.3), including matchings that leave many components partly unused.

**Sufficiency.** Fully match the alpha(r) cheapest red-majority components
and beta(s) cheapest blue-majority components. Their red/blue costs
W_R,W_B do not exceed r,s. After removing those components the remaining
baseline capacity is

    K'=K-sum_selected k_i.

The remaining quotas r'=r-W_R,s'=s-W_B are nonnegative. Condition(14.3)
is precisely what gives r'+s'<=K', since the selected components consume
sum_selected(k_i+1) edges. Every remaining component permits its entire
integer triangle(14.1)/(14.2), including both colours. Distribute r'
red edges among their capacities, then s' blue edges among the remaining
capacities. This is possible because their sum is at most K'; on each
component use the construction of14.1. Distinct components have disjoint
vertices. The union has the exact required quotas, proving sufficiency.

### 14.3 Controls, use and limits

- MI522's RBRBR path has k2,K2 and one red weight3. For quotas(2,1),
  alpha(2)=beta(1)=0, so3<=2 fails. For(3,0), alpha(3)=1 and3<=3 holds;
  for(1,1),2<=2 holds. This recovers both the negative and its controls.
- An even path RBRB has K2 and no odd component: quota(1,1) is attained
  by edge positions1 and4, a mixed MAXIMUM matching. Charging a penalty
  for every mixed path would falsely reject it.
- For components RBR and BRB, K2 and majority weights2 of each colour.
  Quota(2,2) activates BOTH components and is attained by their two
  monochromatic perfect matchings. Unexpected check: there is no
  single forest-wide mixed-colour loss; penalties are component-local.
- Red-majority paths RBR and RBRBRBR have weights2,4 and K4. Quota(2,3)
  uses the cheaper full red path, then the three blue edges of the longer
  path. The criterion gives5<=4+1. An arbitrary full-component choice
  could fail its colour budget; sorting by cost is essential to the proof.
- Single red and single blue components have K0 and weights1 of the
  respective colours; quota(1,1) passes and uses both edges. Adding any
  isolated vertices changes nothing.

By section13, this criterion applies to ANY finite distinct-token pool
with two distinct pair targets u,v. For r target-u pair bins, s target-v
pair bins and ONE filler bin of size |P|-2r-2s>=0, total conservation
makes the filler sum automatic once those pairs are chosen. Hence(14.3)
is an exact completion test in that setting. No interval, protection or
hole bound is assumed in the graph argument. Additional filler bins
would require their own joint allocation and are outside this corollary.

This resolves the two-fibre matching question, not the original multi-bin
partition theorem. The next arithmetic question is how the two sums,
interval endpoints and a deleted token determine these component data;
the protected cuts alone have not been shown to enforce(14.3). No new
PROVED status, census, parent coverage or three-colour transfer is claimed.

## 15. Read the two-sum components directly from interval arithmetic

**Elementary hand readout, MI525–526; unreviewed.** Integer pool[0,M],
integer targets u<v, red sum u and blue sum v; loops are excluded.
This specializes the known two-reflection action, with no originality
claim. The component calculation is independent of section14's quota
criterion and of the earlier conditional partition results.

Put d=v-u>0. Reflections R(x)=u-x and B(x)=v-x satisfy BR(x)=x+d.
Their full integer orbits are indexed by the unordered residue pairs

    {a, u-a} mod d.                                          (15.1)

Choose one representative a in0,...,d-1 for each such pair. Every
integer belongs to exactly one orbit. Two different residues give an
infinite path; a fixed residue 2a=u mod d requires the separate ray
description below. Identifying the two cases prevents double counting.

### 15.1 Two different residues: intersect two index intervals

If 2a!=u mod d, define, for ALL j in Z,

    z_(2j)=a+jd,          z_(2j+1)=u-a-jd.

All labels are distinct: a coincidence between the two progressions
would imply 2a=u mod d. Red edges join positions2j,2j+1; blue edges join
2j+1,2j+2. These are all possible edges, by applying R and B to each
label. Thus this is an exact coordinate path, not just a containing orbit.
Its vertices survive in[0,M] precisely at even/odd positions with

    j in I=[ceil(-a/d), floor((M-a)/d)],
    j in J=[ceil((u-a-M)/d), floor((u-a)/d)], respectively.

Empty intervals contribute no edges. Write I=[A,B], J=[C,D]. The
surviving red and blue EDGE index intervals are

    red j in [max(A,C),   min(B,D)]       = [r0,r1],
    blue j in[max(A-1,C), min(B-1,D)]     = [b0,b1].            (15.2)

The edge with index j here has chain-edge position2j+1 for red,
2j+2 for blue, joining consecutive chain vertices h-1,h.
Use only nonempty intervals. If both are nonempty, b0 is r0-1 or r0,
and b1 is r1-1 or r1. Their edges therefore interleave without a gap.
If one is empty, the other has at most one edge: shifting I by1 can
create only a single overlap when I and J are disjoint. Consequently
each orbit contributes at most ONE nontrivial path, plus isolates.

The path length E is the sum of the two nonnegative interval lengths.
Its first/last chain-edge positions are the minimum/maximum of

    2r0+1, 2r1+1 (red, if present);
    2b0+2, 2b1+2 (blue, if present).

If these extremes are h0,h1, the path's vertex positions are h0-1,...,h1.
Its first colour is red when h0 is odd, blue when h0 is even. This gives
both its length and, when odd, its majority colour. Other surviving
coordinate vertices are isolated and contribute no matching capacity.

### 15.2 A fixed residue: one ray, not two copies of a progression

When 2a=u mod d, put m=(u-2a)/d in Z. If m is even, this orbit contains
the integer red fixed point f=u/2; if m is odd, it contains the integer
blue fixed point f=v/2. Exactly one centre belongs to this residue:
their difference is d/2, not a multiple of d. This also handles the two
different fixed residues that can occur when d is even.

For a RED fixed point the ray, starting at f, is

    f, f+d, f-d, f+2d, f-2d, ...,

with first edge BLUE and alternating thereafter. For a BLUE fixed point
it is

    f, f-d, f+d, f-2d, f+2d, ...,

with first edge RED. Applying the two reflections verifies all adjacent
edges; their only omitted edge is the fixed-point loop. Each ray lists
the whole residue class once. If f is outside[0,M], all surviving labels
lie on one side of f and have no adjacent ray positions, so are isolated.
Otherwise put L=floor(f/d), H=floor((M-f)/d). The single nontrivial
component, if any, is an INITIAL ray segment, of length

    E=min(2L+1,2H),       first BLUE, for red fixed f;
    E=min(2L,2H+1),       first RED,  for blue fixed f.          (15.3)

For the first ray, even vertices survive through position2L and odd
vertices through2H-1; for the second exchange L,H. This proves(15.3)
and shows all remaining vertices are isolated. E0 means no edges.

### 15.3 Delete q: only one component can split

Only q's residue orbit changes. If q is isolated, the path data do not
change. Otherwise let p be its vertex distance from the path's first
endpoint, 0<=p<=E, with E its pre-deletion edge length and sigma its
first colour. Removing q leaves edge lengths

    max(0,p-1),         max(0,E-p-1).                         (15.4)

Ignore zero-length pieces for matching purposes. A nonempty left piece
starts in sigma; a nonempty right piece starts in sigma reversed when
p+1 is odd. Its first surviving edge was edge p+2 of the original path.
Endpoint deletion and an absent reflection loop are thus not mistaken
for removing two ordinary edges.

For two-residue coordinates, q has position t=2(q-a)/d if q=a mod d,
and t=2(u-a-q)/d+1 otherwise; when it lies on the path,
p=t-(h0-1). For a red-fixed ray its position is 2(f-q)/d at q<=f,
and 2(q-f)/d-1 at q>f. For a blue-fixed ray it is 2(q-f)/d at q>=f,
and 2(f-q)/d-1 at q<f. In the ray cases p is this position if <=E;
larger positions are isolated. These formulas locate the hole without
exploring the edge graph. They also show that only an internal even
p in an even-edge path creates TWO odd pieces; their majority colours
are opposite. This is a parity constraint, not a new margin repair.

### 15.4 Literal hand controls and scope

- M8,u9,v10 has d1 and BLUE fixed f5. L5,H3 give E7, first red:
  5-R-4-B-6-R-3-B-7-R-2-B-8-R-1, with isolated0. Hole q4 has p1,
  leaving an isolate5 and the red-ended5-edge path of MI522. Hole q5
  instead deletes the endpoint/fixed point, leaving a6-edge path, not5;
  its missing55 loop was never counted. Quotas2 red/1 blue then work:
  18/27/46, with filler03, targets9/9/10/3 on the new pool.
- M10,u4,v7 has d3. Nonfixed representative a0 gives I=[0,3],J=[-2,1],
  red j0..1 and blue j-1..1: path7-B-0-R-4-B-3-R-1-B-6.
  Fixed residue2 has red fixed f2, L0,H2, giving single blue edge25.
  Tokens8,9,10 are isolated. Deleting internal q8 leaves all path data
  unchanged; deleting q3 instead splits the first path into lengths2,1.
- M10,u6,v10,d4 has TWO fixed residues: red fixed f3 gives blue37;
  blue fixed f5 gives5-R-1-B-9. Nonfixed a0 gives
  10-B-0-R-6-B-4-R-2-B-8. All11 tokens occur exactly once; the two
  centres are not merged into one orbit or counted as loops.
- Unexpected check: M8,u7,v9,d2 has one nonfixed orbit, the8-edge path
  0-R-7-B-2-R-5-B-4-R-3-B-6-R-1-B-8. Hole q4 has p4 and leaves
  red-ended and blue-ended3-edge paths. Both can be fully matched:
  07/25/36/18 gives targets7/7/9/9 on[0,8] minus4. The two-colour
  full-component phenomenon in section14 is genuinely attained here;
  its proper cuts are also strict (minima7,14,23 exceed3,10,21).

The result reads all component data for an actual one-hole interval;
with section14's unreviewed criterion it gives a HAND arithmetic test
for two-target pair bins plus ONE filler. No claim that protected cuts
imply that test, or that two or more filler bins are automatic. Known
reflection ingredients, exact formulas unreviewed here, no new proof
status, census, original-parent coverage or three-colour generalization.

## 16. Protection for adjacent pair targets: verified classification

**PROVED G329 by Cloud CL469/64af1b21; adopted MI531.**
The independent carrying read covered the four named proof steps;
49,797 exact admitted inputs to M22 support it with zero mismatches,
reported by Cloud, not rerun here. Original candidate exposition follows.
The full self-contained proof is filed in PROOFS.md G329, including every
path and all-cut step; it does not assume the unreviewed sections14–15
or G327/G328. Known ingredients, novelty UNASSESSED.

Let r,s,c>=1, t=r+s, M=2t+c. On[0,M] minus an internal q, prescribe
r size2 bins of sum u, s size2 bins of sum u+1, and a size-c filler
of sum w. Assume tu+s+w=T_M-q and every proper nonempty group of
bins has target at least T_(its size). The candidate says that failure
occurs EXACTLY in the two families

    u=2M-2t,    c<=q<=r;
    u=2M-2t-1,  c+r<=q<=t+min(r,c-1).

Empty hole ranges give no failures. Every listed negative is admitted.
Consequently c>=t+1 guarantees completion for ordinary protection,
sharply; c>=t guarantees completion for STRICT protection, sharply.
Both sharpness assertions hold for each positive r,s.

The carrying mechanism uses the actual inequalities. All pair-only
lower cuts reduce to u>=2t+1. By discrete concavity, ALL complementary
upper cuts reduce exactly to

    q<=min(2M-u-2, t(2M-2t+1-u)-s).

The adjacent-sum graph is one path of E=min(u+1,2M-u) edges plus isolates.
A deletion from E>=2t+2 permits every mixture of t pairs. The proof
checks its borderline opposite-majority children rather than assuming
ordinary matching capacity suffices. Only the two high u endpoints
remain; their admitted hole positions force exactly the displayed
colour-budget failures. This is not an extension by local repairs.

Old strict negative: r2,s1,c2,M8,q4,targets9/9/10/4. Ordinary sharp
negative at c=t: r2,s1,c3,M9,q5,targets11/11/12/6. Strict safe-boundary
positive at c=t is38/29/57/016 on[0,9] minus4, targets11/11/12/7.
Ordinary safe-boundary positive at c=t+1 is49/{3,10}/68/0127 on[0,10]
minus5, targets13/13/14/10. The first endpoint also has strict negatives,
for example r3,s1,c2,M10,q2,targets12/12/12/13/4. No numerical run.

This resolves the independently posed adjacent-target/one-filler
question at HAND CANDIDATE status. It does not verify the earlier
four-bin parent or establish the threshold for arbitrary target gaps,
multiple fillers, or three distinct pair targets. Its review is one
substantial proof read, not another review of the known matching guards.

## 17. A large filler cannot cure every gap: strict counterfamily

**HAND countercontrol, MI529–530; known weighted token-consumption
method, not a new general matching theorem.** No premise from G327,
G328 or G329 is used. The proposed extension of G329's filler thresholds
to arbitrary target gaps is false, even if the filler is arbitrarily large.

### 17.1 Ordinary protection already fails at gap2

For any c>=3, take M=c+4, delete q=1, prescribe two pair sums4,6 and
filler w=T_M-11, where T_n=n(n+1)/2. Sum4 forces{0,4}; every sum6
pair is{0,6} or{2,4}, so completion is impossible. Yet the pair-only
cuts are4>=3,6>=3,10=T_4, and the three cuts containing the filler have
slacks4c-1,2c,2c+2 over T_c,T_(c+2),T_(c+2), respectively. This is the
old q1 obstruction, checked directly without using its classification.

### 17.2 Strict protection fails for fixed pair multiplicities and unbounded filler

For EVERY c>=7, put M=c+14, q=1. Prescribe four size2 bins of sum10,
three size2 bins of sum22, and one size-c bin of sum

    w=T_M-107.

The target total is106+w=T_M-1, the available token total. There are
exactly ten available tokens in U=[0,10] minus{1}. Every sum10 pair
uses two U tokens. Every sum22 pair uses at least one: two DISTINCT
tokens outside U have sum at least11+12=23. Thus the required seven
pairs demand at least2*4+3=11 U tokens, exceeding|U|=10. No partition
exists. Extra high tokens cannot change this capacity inequality.

Independently, the four sum10 pairs are forced:

    {0,10}, {2,8}, {3,7}, {4,6}.

After these, only5 and9 remain in U. The ONLY remaining sum22 pairs
are{5,17} and{9,13}, both present since M>=21. Three are needed.
The missing{1,9} edge and the prohibited{5,5}/{11,11} loops are not
silently counted as pairs.

**ALL cuts are strictly protected.** A nonempty pair-only group with
j red bins and k blue bins has0<=j<=4,0<=k<=3 and slack

    F(j,k)=10j+22k-T_(2j+2k)
          =9j+21k-2j^2-4jk-2k^2.

For k=0 and j>=1 this is j(9-2j)>0. For k=3 it is
45-3j-2j^2>=1 on0<=j<=4. Concavity in k puts k=1,2 above the
interpolated endpoint values, also for j=0 where F(0,0)=0. Hence every
nonempty pair-only group is strict, including the whole seven-pair
group, whose slack is1.

A proper group containing the filler omits m>=1 pair bins, m<=7.
Let their total target be S<=22m. Its slack over the required triangular
bound is exactly

    T_M-1-S-T_(M-2m)=m(2M-2m+1)-1-S.

Since M>=21 and m<=7, this is at least7m-1>=6. These complementary
groups and the pair-only groups exhaust every proper nonempty cut.
Thus the counterfamily has ALL strict cuts for arbitrarily large c,
with fixed multiplicities4/3 and fixed target gap12. No finite
filler-size bound can suffice uniformly for even this fixed pair data.

### 17.3 Same-pool positive control

Change each blue sum22 to23, retaining the pool and all bin sizes.
Use the same four red pairs and the three disjoint blue pairs

    {5,18}, {9,14}, {11,12}.

The remaining c tokens form a filler of sum T_M-110. At c=7,M=21
they are{13,15,16,17,19,20,21}, of sum121. For larger c add22..M
to that filler. Pair-only cut slacks increase by k; filler-containing
cuts have the same calculation with S<=23m, giving at least6m-1>0.
So both the negative and this literal positive satisfy every strict cut.

This is the known weighted-capacity mechanism (compare MI469 and
section13/MI522), now testing a size-only generalization. It refutes
neither adjacent-target G329 nor the earlier four-bin parent: the
target gap, number of pair bins and filler structure have different
scopes. No new burning obstruction, proof-status promotion or census.
Do not repair this failure by increasing c or starting a gap exception
catalogue. A possible next global question is whether weighted matching
inequalities completely describe integer quotas on alternating path
forests, or whether their convex hull can have unattainable integer
points. That question remains OPEN here; no new test of it has run.

## 18. Weighted capacities are complete for the two-target path model

**PROOF-SKETCH G330, MI532–533; independent carrying review requested.**
This is an application of known polygon machinery, not an originality claim. The angle-ordered merge of convex polygon
edges is standard; see the primary [CGAL5.3 manual, Computing the
Minkowski Sum of Two Polygons](https://doc.cgal.org/5.3/Minkowski_sum_2/index.html).
The lattice rounding argument and its matching specialization are supplied
below; the source is not claimed to state this exact matching result.
Novelty UNASSESSED; no general Exact Matching algorithm is claimed.

### 18.1 Each component has a complete lattice triangle

Let S_i be the attainable(red,blue) edge counts of an alternating path
component, and let its length count EDGES. Put k=floor(ell_i/2) and

    (A_i,B_i)=(k,k)        if ell_i=2k;
              (k+1,k)    if ell_i=2k+1 and both end edges are red;
              (k,k+1)    if ell_i=2k+1 and both end edges are blue.

Then

    S_i = Q_i intersect Z^2,
    Q_i = conv{(0,0),(A_i,0),(0,B_i)}.                    (18.1)

Here is a direct proof, avoiding section14 as an unread premise. A
2k-edge path permits exactly a+b<=k: for the construction orient it
to start red, take its first a red edges and last b blue edges; when
both lists are nonempty their closest edge indices differ by at least3.
The same construction supplies this triangle on an odd path. An odd
path can have k+1 matched edges only if perfect; its endpoint forces
the first edge and then all odd-indexed edges, giving its unique
monochromatic perfect matching. These are all possibilities.

For the red-ended case k>=1, the real triangle inequality is
ka+(k+1)b<=k(k+1). If integers a+b>=k+1 and b>=1, its left side is
k(a+b)+b>k(k+1). Thus the only lattice point above a+b<=k is(k+1,0),
as required. The blue-ended case is symmetric. At k0 the hull is just
the relevant unit axis segment; isolated vertices give the origin.
All S_i and Q_i are downward closed in the nonnegative quadrant.

### 18.2 Why addition creates no integer holes here

More generally, take downward-closed lattice polygons Q_i in R^2_>=0
and ALL their lattice points S_i. Axis segments and points are allowed.
Then

    (sum_i Q_i) intersect Z^2 = sum_i S_i.                (18.2)

Proof: write each polygon's upper boundary from its topmost point on
the vertical axis toward the right. Its vertices are lattice points;
its edges have positive horizontal displacement and nonincreasing,
nonpositive slopes. Vertical axis segments contribute their upper
endpoint throughout; horizontal segments have slope0. The standard
Minkowski edge merge interleaves these edges by decreasing slope,
preserving each component's own order. Break parallel ties by taking
one whole component edge at a time, rather than coalescing them.

For a fixed INTEGER horizontal coordinate r in the sum's range, stop
this merge at the upper boundary point(r,F(r)). At most one component
is inside an edge; every other component is at a lattice vertex. The
remaining component therefore has an INTEGER horizontal coordinate.
Round only ITS vertical coordinate down. Downward closure keeps this
point in its polygon, and the other vertical coordinates are integers,
so the total is exactly(r,floor(F(r))), now a sum of S_i points.
If the stop is at a vertex there is no rounding. To obtain any smaller
nonnegative integer s, decrease the component vertical coordinates by
integer amounts totalling floor(F(r))-s. Downward closure permits this.
Every integer point in the sum is thereby represented. The reverse
inclusion is immediate. This proves(18.2), including the degenerate
axis-only cases. It uses two dimensions and downward closure; it is
not a generic integrality claim about projections or Minkowski sums.

Different graph components have disjoint vertices, so their exact
matching quotas add. Also conv(sum S_i)=sum conv(S_i): one inclusion
is convexity; for the other, expand finite convex combinations using
products of their coefficients. Equations(18.1)–(18.2) therefore prove

    attainable quotas = conv(attainable quotas) intersect Z^2.

Thus there are NO integer holes in an alternating-path forest's quota
projection. This is a complete HAND argument, not an inference from
the finite diagnostic or the earlier cheapest-component criterion.

### 18.3 An explicit finite set of weighted tests

For nonnegative integer quotas r,s, define

    H(p,q)=sum_i max(p*A_i,q*B_i).

A matching with EXACTLY r red and s blue edges exists if and only if

    p*r+q*s <= H(p,q)                                    (18.3)

for normals(1,0),(0,1), and(B_i,A_i) from every component with
A_i*B_i>0. Repeated or proportional normals can be kept. Indeed each
Q_i has these non-axis upper-edge normals, and the known edge merge
gives no other upper-edge direction in their sum. The support in
normal(p,q) is H(p,q), achieved independently on the components.
The axis tests and r,s>=0 handle the remaining boundary directions.
So(18.3) describes the real polygon sum;18.2 gives exact integer
attainability. Every unattainable quota thus has a weighted certificate;
unweighted group/total capacity alone need not expose it (section13).

For ANY finite pool of distinct real tokens and TWO DISTINCT pair
targets u,v, the two-sum graph is such a forest. Each vertex has at
most one incident edge of either colour; omit loops. A cycle would
alternate colours and have even length2h. Successive reflection pairs
x->u-x->v-u+x translate by v-u; going around a cycle would give
x+h(v-u)=x, impossible. Hence every component is a path or isolate.
This proves the representation here, rather than importing section13.
For one filler, its size and sum follow automatically by conservation
after selecting the requested pairs. Multiple fillers do not follow.

### 18.4 Can-fail diagnostic and boundaries

The fixed probe quota_hull.py checks eight forests,252 quota points.
Literal global edge-subset matchings, exact hull membership, finite
normal tests and the older budget formula agree everywhere. It retains
MI522's unattainable(2,1); its weighted normal(2,3) rejects7>6.
Alternating C4 has a GENUINE hole(1,1), between its perfect quota points
(2,0),(0,2). The two lattice segments[0,(2,1)],[0,(1,2)] also have a
sum-hull hole(1,1). Both negative controls pass. Single-edge, isolate,
opposite-majority, parallel-normal and unequal-length cases are included.
No expanded census or repeat. The unbounded argument is18.1–18.3,
not the diagnostic. No originality or independently PROVED status yet.

This completes the chosen two-target obstruction question at HAND
status. It supplies no bridge to three pair targets, multiple fillers,
five-bin admission or the equal-shares wall. Before extending the model,
ask whether such a transfer preserves its path/downward-polygon property.

## 19. Three AP targets: perfect quotas form a lattice interval (MI537–538)

**HAND specialization, unreviewed.** Known monotone-graph switch
connectivity is credited in PRIOR-ART; the argument below is elementary
and self-contained. No originality, general partial-quota integrality,
four-label or five-bin conclusion. It does not depend on G330.

Let P be ANY finite set of2n distinct real tokens, d>0, and allow
pairs whose sums are u-d,u,u+d. Suppose a perfect matching exists.
Write its three quotas as(r,s,t), in that order. Then the attainable
perfect quota triples are EXACTLY the integer points of a closed line
segment (possibly one point). Its line satisfies

    r+s+t=n,    u*n+d*(t-r)=sum(P).                      (19.1)

Differences of integer solutions of(19.1) are multiples of(1,-2,1).
The assertion here is that no such intermediate lattice point is missed.

### 19.1 Switch connectivity without assuming bipartiteness

Take any two perfect matchings X,Y. Their symmetric difference consists
of disjoint even alternating cycles; common edges can be kept. On ONE
such cycle, partition alternate vertices into L,R. Every edge of X or Y
on this cycle crosses L,R. Two consecutive reflections x->u+k*d-x
change x by an integer multiple of d. Consequently, for some real a,
ALL vertices in L belong to a+d*Z and ALL vertices in R belong to
u-a+d*Z. Thus every cross sum belongs to u+d*Z. It is an allowed sum
if and only if it lies in the CLOSED interval[u-d,u+d]. This statement
concerns vertices already on the cycle, not nonexistent tokens between
them. It holds for sparse pools and for fixed reflection residue classes.

List L as x_1<...<x_h and R as y_1>...>y_h. A cross perfect matching
is a permutation pi, pairing x_i with y_(pi(i)). If pi has an adjacent
inversion pi(i)>pi(i+1), then y_(pi(i))<y_(pi(i+1)). The existing
sums x_i+y_(pi(i)) and x_(i+1)+y_(pi(i+1)) bracket BOTH switched sums

    x_i+y_(pi(i+1)),    x_(i+1)+y_(pi(i)).

Both switched sums therefore remain in[u-d,u+d], and both belong to
u+d*Z. They are allowed edges. Swapping these partners removes one
inversion; repeated adjacent inversion switches reach pi(i)=i.
All four tokens in a switch are distinct because L,R are disjoint.
Thus X and Y on this cycle each connect to the same sorted matching.
Reverse the second path and repeat on the disjoint cycles. This gives
a finite sequence of legal two-edge switches from X to Y on P.

The whole graph need NOT be bipartite: targets(-1,0,1) on tokens
(-1,0,1) give a triangle. The proof uses only alternating-cycle cuts;
it never imposes a global bipartition or adds a self-loop.

### 19.2 Primitive steps force every intermediate perfect quota

A two-edge switch preserves the four-token total and number of edges.
Its quota difference therefore has the form k*(1,-2,1), with integer k.
Only two edges change, so the middle quota changes by at most2; hence
k is0,+1 or-1. There are finitely many matchings. Choose those with
minimum and maximum red quota. Along a switch path joining them, the
integer red quota changes by at most1, so it visits every integer in
between. Equation(19.1) uniquely determines the other two quotas from
the red quota. This proves the stated interval property. The empty
pool and a unique perfect matching give degenerate segments as claimed.

Hand controls: P0123, targets2/3/4, has matchings02/13 and03/12,
quotas(1,0,1),(0,2,0). The same switch occurs on the sparse rational
pool{1/5,6/5,9/5,14/5}, with those same targets. The fixed half-integer
pool{-3/2,-1/2,1/2,3/2}, targets(-1,0,1), likewise gives these two quotas.
The abstract two-colour alternating C4 instead has quotas(2,0),(0,2)
and misses their integer midpoint; its arithmetic is not(19.1).
These are literal hand checks, not a new numerical census.

### 19.3 Exact boundary of this argument

It also applies to partial matchings when their COVERED TOKEN SET is
fixed: they are perfect on that set. It does NOT join different covered
sets. At fixed size k, unmatched tokens have total

    sum(P)-u*k-d*(t-r).

Changing that set changes the affine line in(19.1). Taking the union
of the separate line segments need not follow from their individual
contiguity. No overlap theorem for those fibres is proved here. Thus
the full three-dimensional partial-quota hull question remains OPEN,
as does the four-label model that the actual E24 transfer requires.

## 20. Three unequal-gap targets really can have an integer quota hole (MI539–540)

**Explicit hand guard, unreviewed; no originality claim.** The automatic
extension of section18's no-hole property to THREE arbitrary sum targets
is false, even when the actual sum graph is a single path. This is a
sparse-pool example, not a full-interval/one-hole or AP-target example.
No earlier unreviewed theorem is a premise.

Take the seven distinct nonnegative integer tokens

    P={0,2,3,23,25,26,27},     targets(A,B,C)=(26,27,29).

The complete lists of allowed pairs are

    A: {0,26}, {3,23};
    B: {0,27}, {2,25};
    C: {2,27}, {3,26}.

To verify completeness, list x<=target/2 in P and test its complement:
for26 the possible low tokens are0,2,3, giving26,24,23;
for27 they give27,25,24; for29 they give29,27,26.
Only the displayed complements are present. Hence the actual graph is

    23 --A-- 3 --C-- 26 --A-- 0 --B-- 27 --C-- 2 --B-- 25.

Index its six edges1..6 from left to right. The only nonadjacent triples
are135,136,146,246: subtract0,1,2 from their increasing edge indices
to obtain a three-element subset of{1,2,3,4}, which gives exactly four
choices. Their quota triples(A,B,C) are respectively

    (2,0,1), (2,1,0), (1,2,0), (0,2,1).

In particular(1,1,1) is absent, but it is the midpoint of the first and
last displayed triples. It is an INTEGER point of the convex hull of
ACTUAL matching quotas, not just a point of a fractional degree relaxation.
No larger matching exists on seven vertices; smaller matchings cannot
have quota111. The witness uses two different covered-token sets: those
endpoint matchings leave25 and23 respectively.

An independent one-line obstruction makes the missing inference explicit:
sum(P)=106, while one pair of each target consumes26+27+29=82. A quota111
matching would leave the SINGLE token24, which is not in P. The two
endpoint matching totals are81 and83; their mean82 need not be the total
of a six-token subset. Convex averaging does not supply the missing token.

Why this is not an AP counterexample: for a putative distinct-token path
with colour sequence A C A B C B and target values a,b,c, start at x.
Its vertices in order must be

    x, a-x, c-a+x, 2a-c-x, b-2a+c+x, 2a-b-x, 2b-2a+x.

The last minus the third is2b-a-c. If a+c=2b, these vertices coincide;
the putative last endpoint matching uses that token twice. The seven-
vertex coloured-path witness therefore fails injective AP realization.
This computation does NOT prove all other AP quota supports integral.
It shows why forgetting arithmetic would overstate either conclusion.

The broad three-target no-hole extension is REFUTED at hand status.
The AP-target partial-quota question remains OPEN. Section19's fixed-
covered-set perfect-face argument is neither used nor contradicted.
No uniform filler threshold, full-interval counterexample, four-label
E24 obstruction or new numerical census is claimed.
