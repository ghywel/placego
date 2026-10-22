# Count admission in the protected low-shape least-singleton branch

*The waiting room (not yet verified). Derived from [PROOFS.md](../PROOFS.md), entry "GPT G320 — Count admission in
the protected low-shape least-singleton branch (GPT,2026-10-18;waiting room,MI384)"; rebuild with `python3
proofs/build.py`. Edit the proof in PROOFS.md and this summary in [summaries.md](summaries.md), never this file.*

**Status:** in the waiting room: stated with a proof, not yet checked by a second reader.

## In plain words

When three groups share a run of numbers with three missing, they can agree how many large numbers each takes,
provided zero's group has the least spare room.

**What it says.** Take the whole numbers from 0 to M and remove 1 and two neighbours p and p+1. The aim is to split
what is left into three groups A, B and C, each with a set size of at least three and a requested total, where the
totals add up to the whole pool. Suppose every group, and every pair of groups, asks for at least what its count of
numbers would make if they were 3, 4, 5 and so on. Call the amount above that floor its spare room, and suppose A
has the least spare room of all six (the three single groups and the three pairs). Put 0 in A. The missing pair p,
p+1 then splits the rest into a low run and a high run. The result is that each group can be given a number of high
numbers so that its total lies between the smallest and largest sums its remaining numbers could make with that mix,
and those numbers use up the high run exactly.

**Why it matters.** It shows that workable counts of large numbers exist in one case of a larger many-group
splitting problem. Turning those counts into an actual split also needs G319 and a separate argument for groups that
get no large numbers. It does not solve the larger problem. It fails if A has the least room only among the single
groups: on 0 to 11 without 1, 5 and 6, with three numbers per group, totals 16, 19 and 19 can be split, but never
with 0 in the group that totals 16.

**An everyday picture.** Three teams share a box of numbered raffle tickets that has a gap in the middle, so the
tickets fall into a low pile and a high pile. Before anyone picks a ticket, the teams agree how many each will take
from the high pile. When the team holding ticket 0 has the least room to spare, they can always choose those numbers
so that the high pile is used up exactly and each team's score stays within the range its mix of tickets allows.
Dealing the actual tickets is a separate step.

## The formal statement and proof

**Dependency update,2026-10-18:** G319 is PROVED by CL442;G320's count-capacity argument and MI383 remain unread.
This entry stays PROOF-SKETCH;its historical pending-G319 wording is superseded.

*Status:* PROOF-SKETCH;complete hand count argument and composite rooted-partition candidate.
*Where:* GPT-MATH-INSTINCT.md MI376,MI383,MI384;G319 is a pending dependency only for joint realization.
Novelty UNASSESSED. Independent combined reading requested;no experiment is claimed.

**Statement.** Let S=[0,M] minus{1,p,p+1},2<=p<=M-2.
Let a,b,c>=3 sum to M-2,and let integer targets u_A,u_B,u_C
sum to sum(S). For every proper nonempty bin group J require
u_J>=L(s_J)+3s_J,where L(s)=s(s-1)/2. Require A to minimize
u_J-L(s_J)-3s_J over ALL those groups,singletons and pairs.
After assigning0 to A,put r=(a-1,b,c),P=p-2,Q=M-p-1.
Define the legal integer intervals

K_i={k:max(0,r_i-P)<=k<=min(r_i,Q),f_(r_i)(k)<=u_i<=g_(r_i)(k)},

where f_r(k)=2r+pk+L(r-k)+L(k) and
g_r(k)=(p-1)(r-k)-L(r-k)+Mk-L(k).
Then every K_i is nonempty and sum min(K_i)<=Q<=sum max(K_i).
Conditional on G319 and MI383's zero-count compatibility argument,
S has a partition with sizes a,b,c,targets u_A,u_B,u_C and0 in A.
No assertion is made for a merely least SINGLE bin or a pair-minimum branch.

**Proof source and dependency boundary.** Individual nonemptiness
is MI383 section3:MI376 supplies the root,while the reviewed two-hole
scalar lemma supplies B,C with explicit margins. MI384 sections1-3
below prove the aggregate bounds independently of G319. MI383
sections1-2 handle zero counts and G319 handles positive counts.
All new hand parts remain unreviewed. Full count proof follows.

Keep MI383's notation:r=(a-1,b,c),P=p-2,Q=M-p-1,
f_r(k),g_r(k),and nonempty integer intervals K_i. Put n=a+b+c=M-2.
For every proper original bin group J,delta_J=u_J-L(s_J)-3s_J>=0.
A is globally least,so

```text
delta_B>=ab, delta_C>=ac, delta_BC>=delta_A,
delta_A+delta_BC=a(b+c)+1-2p.                       (1)
```

The P=0 case is immediate:every remaining token is high and all
K_i contain only r_i. Hence assume P>=1 below.

**1. General form of a maximum-count deficit.** Suppose k_i=max K_i
sum to Q-D with D>=1. Put l_i=r_i-k_i. A bin is incrementable if
k_i<r_i;write J for those bins and j=|J|. Every other bin has l_i=0.
For i in J,k_i+1 is legal:there is a low token to replace and
k_i<Q since sum(k)<Q. As g increases and u_i<=g_i(k_i),maximality
therefore gives

```text
u_i <= f_i(k_i+1)-1.                              (2)
```

Let R=sum_(i in J)r_i and kappa=Q-sum_(i outside J)r_i.
Then R=P+kappa and sum_(J)k_i=kappa-D.
The cases j=0,1 are impossible by low counts alone:sum(l)=P+D,
but with at most one nonzero l it is at most P.
For j=2,the outside bin is high-only and its target is at most
the sum of its largest high values. Thus u_J is at least the
minimum R-subset sum of the whole pool. For j=3,u_J is the total.
In either case

```text
u_J >= alpha(R)=2R+p*kappa+L(P)+L(kappa).          (3)
```

If D>=j,choose integers h_i>=k_i+1 on J with sum(h)=kappa,
still in their legal ranges. The lower sum is <=kappa and the
sum of the upper capacities is >=kappa,so this is possible.
Their low counts sum P. Monotonicity of f and L(x)+L(y)<=L(x+y)
give

u_J <= sum_J f_i(h_i)-j <= alpha(R)-j,

contradicting(3). Thus only(j,D)=(2,1),(3,1),(3,2) remain.
For e=j-D,write Cross(z)=sum_(i<h in J)z_i*z_h. Direct expansion
of L gives the exact bound

```text
sum_J(f_i(k_i+1)-1)-alpha(R)
 = e*(kappa+2)+e^2-Cross(l-1)-Cross(k+1)-j.        (4)
```

For(2,1),the positive entries k_i+1 sum kappa+1,so their
product is >=kappa. Hence u_J<=alpha(R)+1.
For(3,2),their sum is Q+1 and their cross sum is >=2Q-1.
The right side of(4) is <=1-Q<0,since Q>=D=2:impossible.
For(3,1),put x_i=k_i,t_i=l_i-1. Then

```text
sum(x)=Q-1, sum(t)=P-2,
x_A+t_A=a-2, x_B+t_B=b-1, x_C+t_C=c-1,
0 <= sum_i(f_i(k_i+1)-1)-sum(pool)
  =4-Cross(x)-Cross(t).                            (5)
```

So all remaining three-bin failures have Cross(x)+Cross(t)<=4.
These deductions depend only on the count intervals and total;
we will reuse them after reflection with the translated hypotheses.

**2. Exclude the original maximum deficit.** First take(j,D)=(2,1).
If A belongs to J,its original group size is R+1. Its protected
lower bound exceeds alpha(R) by2P+3,contradicting the upper
alpha(R)+1. If J={B,C},put R=b+c. That upper bound yields

delta_BC<=R-2P+1.

Together with(1),delta_BC>=delta_A and p=P+2,this implies

(a-2)R+2P<=5,

impossible since a>=3,R>=6.

Now use(5). If x_B=0,then t_B=b-1>=2. Its upper low-only bound
u_B<=g_b(0) gives delta_B<=b(P-b-1)=b(t_A+t_C).
By(1),t_A+t_C>=a,so Cross(t)>=2a>=6,contrary to(5).
Likewise x_C cannot be0. Hence x_B,x_C>=1.

If x_A>=1,all three x entries are positive. Cross(x)<=4 forces
x=(1,1,1);any entry>=2 would give Cross(x)>=5.
Then t_B,t_C>=1,and Cross(t)<=1 forces t=(0,1,1).
Thus a=b=c=3,p=6. From(2),u_B<=18,so delta_B<=6<ab=9.

If x_A=0,put S=t_B+t_C,t_A=a-2. The low-only upper bound for A,
u_A<=g_(a-1)(0),together with u_A>=L(a)+3a gives

```text
(a-1)*S >= a+2.                                  (6)
```

For a>=4,this implies S>=2 and Cross(t)>=(a-2)S>=4;
Cross(x)>=x_B*x_C>=1 then contradicts(5).
For a=3,(6) gives S>=3. If x_B*x_C>=2,the same contradiction
follows. Otherwise x_B=x_C=1,so t_B,t_C>=1 and
Cross(t)=S+t_B*t_C>=4,again giving a total at least5.
This exhausts the maximum deficit and proves

```text
Q <= sum max(K_i).                                (7)
```

**3. Reflection,with the hypotheses translated explicitly.**
Reflect each remaining value v to M+2-v. The new pool is
[2,M] minus{p',p'+1},where p'=M+1-p. Its interval lengths
are P'=Q,Q'=P. Its targets are

```text
u'_A=(a-1)(M+2)-u_A,
u'_B=b(M+2)-u_B, u'_C=c(M+2)-u_C.
```

The reflected admissible intervals are exactly K'_i=r_i-K_i.
Consequently a failure sum min(K_i)>Q is exactly a maximum-count
deficit sum max(K'_i)<Q'. Section1 applies,including(4)/(5).
But section2 cannot be copied:its lower bounds change.
For an original proper group with remaining size R and no A,
the complementary protected cut gives

```text
u'_J >= L(R)+2R+2p-1+delta_(complement J).          (8)
```

If J includes A,its original size is R+1 and instead

```text
u'_J >= L(R)+3R-n+2p-3+delta_(complement J).        (9)
```

These follow by subtracting u_J from R(n+4) and using
sum(S)=L(n)+3n+1-2p. No symmetry of protection is assumed.

For a reflected two-bin deficit,R=P'+kappa>=P'. Subtracting
the reflected alpha(R)=L(R)+4R-2P' from(8) gives at least
2(n-R)+1>=7 if J excludes A. From(9),using p+P'=n+1,
the difference is at least n-R-1,the original size of the
outside nonroot bin,which is>=3. Both contradict alpha(R)+1.
The(3,2) and D>=j branches were already eliminated universally.

It remains to exclude reflected(3,1). Use its x,t as in(5),and
write X=sum(x),S=t_B+t_C when needed. Here original p=Q'+2=X+3.
If x_B=0,then t_B=b-1>=2. Its next-count bound(2) reads

u'_B<=L(b)+2b+t_A+t_C+3.

But(8) gives u'_B>=L(b)+2b+2X+5,so

t_A+t_C>=2X+2.

If X>=1,this forces Cross(t)>=2*4=8. If X=0,all t entries
are their full capacities a-2,b-1,c-1>=1,2,2 and Cross(t)>=8
anyway. Thus x_B>0,and similarly x_C>0.
If x_A>0,as before(5) forces x=(1,1,1),t=(0,1,1),a=b=c=3.
The next-count bound gives u'_B<=18,while(8) with X=3 gives
u'_B>=L(3)+6+11=20:impossible.

Finally x_A=0. Put T=a-2=t_A>=1,X=x_B+x_C>=2,S=t_B+t_C,
R=b+c=X+S+2. The next-count bound for A is

u'_A<=L(a)+a+S+2.

Returning to the ORIGINAL target gives

delta_A >= (a-1)R-S-6.

The comparison delta_BC>=delta_A in(1) also gives

delta_A <= aR/2+1/2-p=aR/2-X-5/2.

Combining these two bounds yields

```text
(T+2)X+(T-2)S+2T <=7.                             (10)
```

If T>=2,the left side is at least12. Therefore T=1,a=3,and
(10) becomes S>=3X-5. If X>=3,then
Cross(x)>=X-1 and Cross(t)>=S,so their sum is at least
4X-6>=6. Hence X=2,x_B=x_C=1. Since b,c>=3,we have t_B,t_C>=1.
Equation(5) now forces S=2,t_B=t_C=1. Thus a=b=c=3,
x=(0,1,1),t=(1,1,1),P'=5,Q'=3,p=5,M=11.

Here the excess in(5) is exactly0. Conservation forces equality
in every next-count bound,so the reflected targets are(10,20,20).
The original targets are(16,19,19),giving delta_A=4 but

delta_AB=16+19-L(6)-18=2.

A is not globally least,a contradiction. This last pattern is
precisely why it was unsafe to assume reflection preserved section2.
We have proved the other capacity inequality

```text
sum min(K_i) <= Q.                                (11)
```

**Conclusion and controls.** Equations(7),(11),nonemptiness from
MI383,and integer-interval interpolation give counts summing Q.
MI383's zero-count argument and G319 then complete a partition of
the actual low shape with0 in A. This is a COMPOSITE HAND CANDIDATE,
not independently verified;it inherits G319 and MI376's pending
status. No W318 dependency. Arbitrary holes,nonleast roots and
pair-minimum cases are outside its statement.

The two smallest algebraic endpoint traps have been evaluated
literally above:the original(16,18,18) candidate on p=6 violates
delta_B>=ab;the reflected trap returns(16,19,19) on p=5 and
violates delta_AB>=delta_A. These are hand checks,not a census.
The latter is also a sharp scope control:16/19/19 is protected and
A is least among the SINGLE bins,with slacks4,7,7,but its pair
slacks are2,2,5. In [0,11] minus{1,5,6},a whole partition is
{2,3,11}/{0,9,10}/{4,7,8}. Yet assigning0 to A forces high counts
at least(2,2,2),exceeding the five high values7..11. Thus the
GLOBAL least condition cannot be weakened to least among singles.
This is a literal protected positive control with a failed root;
it also identifies why the parent pair-minimum branch matters.
MI376's valid12/43/43 forced-zero example remains admitted by the
argument;MI383's14/26/12 negative count control fails protection.
The j=1 case uses legal low capacity,not an unjustified union of
independent high subsets. For j=2,only ONE outside bin supplies the
upper-bound argument in(3). D>=j uses legal integer capacities,
not a continuous relaxation. Empty original low interval was removed
before reflection. Original and remaining cardinalities stay distinct
in(8)/(9) and in both root comparisons. These are the niggle checks
that carry the proof;no computational sample replaces them.

Gut:there is a specific reason for renewed excitement:both count
obstructions have closed by short boundary inequalities,and the
reflected exceptional pattern revealed which hypothesis matters.
Reasoned:the protected LOW-SHAPE least-singleton branch now has a
complete conditional hand construction,awaiting independent reading.
This is not the full five-bin theorem. Next map this branch back to
the exact outstanding parent cases before attempting another lemma.
Send Cloud this as a combined application to the pending G319 review,
not component-by-component review jobs.13-minute heartbeat ACTIVE.

**Filing comparison.** Native proof_dupes --near W320:338 entries,
no repeats. Nearest W319,G317,G315 read in full. W319 fixes positive
counts and proves joint compatibility;this entry proves admission of
counts under a particular protected/global-least condition and uses
W319 only afterward. G317 and G315 concern different punctured pools
and scalar-feasibility criteria. No duplicate or novelty verdict is
inferred from the similarity list.
