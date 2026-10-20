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

## 11. Unreviewed extension packet: exactly two bins of size two

**Complete parent PROOF-SKETCH, not independently verified.** Consolidated
from GPT-MATH-INSTINCT MI509–514. This section does not change the proved
statuses or scope of Sections1–10. Novelty is unassessed. It adds no new
PROOFS entry or separate review request. The ingredients and the new parent
interfaces must all survive a carrying read before this becomes PROVED.

**Statement under review.** Let N=a+c+4, a,c>=3. Prescribe integer sums
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
| [G327 step1](PROOFS.md) only: both size2 P/Q central spectra, m>=5, h<2(m-2) | Separated size2 bins at strict pair minimum | Unreviewed scalar lemma |
| [G328](PROOFS.md): exact three-entry protected(2,2,c) failure list | Larger singleton child | Unreviewed classification |
| Sections11.2–11.5 below | Root interface, physical size4 switch, exhaustive composition | Unreviewed parent argument |

This is a self-contained PARENT argument relative to those named
ingredients, not a claim that the two unread ingredient proofs have been
replaced. Their full carrying calculations remain in the linked master
entries. The whole G327 four-bin conclusion is NOT used; G328 is independent
of G327. No G320–322, MI430, MI460 or finite census is a premise. Verifying
G327 and G328 alone would not automatically verify the new parent interfaces.
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
