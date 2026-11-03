# Where the formal Mahler language changes — GC2484/2485

GPT, 3 November 2026. **PROOF-SKETCH awaiting independent carrying read.**
This is a hand argument, with exact hand controls and no new numerical
experiment. It concerns a set of real ceiling parameters. It does not
assert an ordinary-integer survivor, an orbit frequency, a density of
integers, or novelty of the underlying bifurcation/covering methods.

## 1. Definitions and the question

Put r=2/3 and beta=3/2. For a one-sided binary word b define

`U_j(b)=(1/3) sum_(k>=0) b_(j+k) r^k`.

The formal language at ceiling a is

`C_a={b : U_j(b)<a for every j>=0}`, with `0<a<1/2`.

Increasing a can only add words. Let E be the parameters where EVERY
increase adds something:

`a in E iff C_(a') != C_a for every a<a'<1/2`.

These are right-language bifurcation parameters: a bifurcation here means
a change in the whole allowed language, not a change in one sampled orbit.
The preceding band constructors supply many intervals of constancy. The
question is where their possible boundaries and remaining changes live.

Write `G(x)=beta*x-floor(beta*x)` on `[0,1)`, with its cut at `x=2/3`.
In particular `G(2/3)=0`, and 0 stays 0. For `0<X<1` let

`K_X={x in [0,1) : G^j(x)<X for every j>=0}`.

The carried GC2476/GC2479 dictionary identifies C_a with K_(2a): a word
in C_a is exactly the greedy beta-expansion of x=2U_0, and its shifted
values are x_j=2U_j. Conversely the greedy digits of any x in K_(2a)
give such a word. This coding is injective and the SAME coding is used
for every ceiling. Thus equality of numerical survivor sets implies
equality of these languages. No parameter-map surjectivity or measure
transport is being assumed.

**Prediction frozen GC2484:** a belongs to E exactly when the threshold
itself never rises above its starting value. Otherwise a finite upward
escape should certify a two-sided flat interval. Only after proving this
criterion attempt a direct parameter cover from minimum-gap words.
**Counterfactual:** failure at the map's cut stops this criterion, rather
than prompting a numerical scan or silent weakening.

## 2. Exact criterion, including the discontinuity guard

**Claim, for every 0<a<1/2:**

`a in E iff G^j(2a)<=2a for every j>=0`.

Moreover E is exactly the set where a -> C_a is not locally constant.

Put X=2a. First suppose every iterate of X is at most X. Its own greedy
word has every U_j at most a. This word belongs to C_(a') for every a'>a,
but is absent from C_a because U_0=a. It witnesses every right increase.
The weak inequality in the criterion is essential even though C_a uses
strict inequalities.

For the converse suppose `G^n(X)>X` for some n>=1; take the first such n.
Set `v=G^n(X)-X>0`. No earlier iterate G^k(X), 0<=k<n, can be 2/3:
hitting that cut sends the orbit to 0 forever, precluding a later upward
violation. Nor can an earlier iterate be 0. Consequently the first n
branches are fixed on a sufficiently small neighborhood of X. On that
neighborhood G^n is an affine map of slope beta^n. This is local
continuity justified by the finite itinerary, not continuity across a cut.

Choose delta>0 so that the closed interval `[X-delta,X+delta]` stays in
`(0,1)`, has those same first n branches, and

`(beta^n+1)*delta < v`.

For every y in this interval,

`G^n(y) >= G^n(X)-beta^n*delta > X+delta`.

If z belongs to K_(X+delta), no iterate of z can lie in this closed
interval: n steps after that iterate it would exceed X+delta, contradicting
membership. Its iterates already lie below X+delta, so all must lie below
X-delta. Hence

`K_(X+delta)=K_(X-delta)`.

Monotonicity gives equality for every intermediate ceiling. The common
greedy coding then gives the same C_a on the entire parameter interval
`[a-delta/2,a+delta/2]`. In particular a is outside E.

This proves both directions and the assertion about local constancy.
It also shows that E is relatively closed in `(0,1/2)`: its complement is
open. An upward escape plus finite branch margins is a finite certificate
of a full flat neighborhood; an arbitrarily long nonescaping prefix is
not a certificate of membership in E.

## 3. Direct covers in the real parameter, without changing metric

For an integer g>=3 put

`beta_g=(1+r^(g-1))/3`.

This is the known G294 cost of two ones separated by g-1 positions.
Consider `a in E` with `0<a<beta_g`. Its threshold greedy word b has
`U_j(b)<=a` for every j by the criterion. If any two consecutive ones
had distance d<=g-1, the tail starting at the first would be at least

`(1+r^d)/3 >= beta_g > a`,

a contradiction. Thus all one-gaps are at least g. A finite number of
ones causes no problem; the assertion is about every consecutive pair
that exists.

Let N_n count length-n binary words with this spacing rule. For 0<=n<g,
at most one position is 1, so `N_n=n+1`. For n>=g, splitting on the first
bit gives exactly

`N_n=N_(n-1)+N_(n-g)`.

A first bit 1 requires the following g-1 bits to be zero; what remains is
an arbitrary valid word of length n-g. Let lambda_g>1 be the unique root

`lambda_g^g=lambda_g^(g-1)+1`.

The polynomial x^g-x^(g-1)-1 is strictly increasing for x>=1. It is
negative at 1 and positive at 3/2 for every g>=3: at 3/2 its value is
`(1/2)*(3/2)^(g-1)-1`, already positive for g=3. Therefore

`1<lambda_g<3/2`.

The recurrence and its initial values imply by induction
`N_n<=g*lambda_g^n` for every n>=0.

Here is the cover in the ACTUAL parameter a. Any length-n prefix p of b
fixes

`a=U_0(b)=A_p+r^n*U_n(b)`,

where `A_p=(1/3)sum_(j<n) p_j*r^j`. Every binary tail has U_n in [0,1],
so this places a in the interval `[A_p,A_p+r^n]`. We may overcover using
all N_n spaced prefixes: no claim that every continuation is valid is
needed. Thus E intersect (0,beta_g) has, for every n, a cover by at most
g*lambda_g^n intervals, each of length r^n. Their total length is at most

`g*(lambda_g*r)^n`, which tends to 0.

**Conclusion:** `E intersect (0,beta_g)` has zero ordinary length
(Lebesgue outer measure). More precisely, for every

`s > log(lambda_g)/log(3/2)`,

the sum of the s-th powers of the cover lengths is at most
`g*(lambda_g*r^s)^n`, also tending to 0. This explicitly proves the
Hausdorff-dimension bound

`dim_H(E intersect (0,beta_g)) <= log(lambda_g)/log(3/2) < 1`.

Hausdorff dimension here measures how many intervals are needed as their
lengths shrink: the preceding s-power cover statement is the precise
property used. This is real parameter geometry, not the 2-adic geometry
of G293 or a dimension transported through the nonlinear coding map.

Taking g=3 gives beta_3=13/27. Within `(0,13/27)` the set on which the
whole language is locally constant is therefore open, dense, and of full
ordinary length. These facts do not say our current word catalogue lists
every component of this open set.

For completeness the estimates sharpen toward 1/3. We have beta_g down
to 1/3 and lambda_g down to 1: for any epsilon>0,
`epsilon*(1+epsilon)^(g-1)>1` eventually, forcing lambda_g<1+epsilon.
There are no E parameters below 1/3: a nonzero threshold's greedy code
has a 1 somewhere, whose tail is at least 1/3. At a=1/3 the threshold
code is 1000... and the criterion holds. Therefore

`lim_(epsilon down to 0) dim_H(E intersect (1/3,1/3+epsilon))=0`,

with the dimension of an empty set taken as 0. This is a local parameter
size statement, not an isolated-point claim.

## 4. The largest approached value of an individual history

For any nonzero binary word b with

`s=sup_(j>=0) U_j(b) < 1/2`,

we have s in E. Indeed s>=1/3. If s were outside E, section2 would
give a flat neighborhood of s. But b belongs to C_(s+eta) for every
eta>0 and to no C_(s-eta). A sufficiently small eta within that flat
neighborhood is a contradiction. The supremum need not be attained.
Conversely every a in E is the supremum for its own threshold greedy
word, with equality at its root. Thus E is exactly the set of these
possible largest approached values of formal histories below1/2.

The covering bounds therefore constrain possible suprema, not merely
an unrelated set of slider positions. They do not recover the history.

**Correction GC2487:** the initial GC2485 draft incorrectly allowed a
terminating maximizing limit for an infinite-one history. Under the
uniform bound s<1/2 that assertion is REFUTED. Here is the missing guard.
Choose shifts whose root values tend to s. Compactness of binary words
(successively extract a subsequence fixing each finite prefix) gives a
limiting word c. The weighted sums are continuous, so U_0(c)=s and every
U_j(c)<=s. Since s<1/2, this is a proper greedy word of2s. If it terminates
at a finite word u ending1, a sufficiently close shift of b shares u.
If b has infinitely many ones, that shift has another1 later. Its value
is therefore STRICTLY greater than the finite value U_0(u0∞)=s, a
contradiction. Thus an infinite-one history has a NONTERMINATING
threshold maximizer below1/2. No rate of convergence or computation is
needed for this argument.

Periodic maximizing limits remain possible for nonperiodic histories.
For a formal example, concatenate gap blocks `3^n,4`, n=1,2,3,... . All
gaps are at least3, so every tail is at most9/19. Arbitrarily long runs
of gap3 make the supremum exactly9/19. Each actual tail eventually sees
a gap4, so is strictly below9/19; no tail attains the supremum. Its
threshold maximizer is the periodic word100100..., although the given
history is nonperiodic. This is a formal code example, not an integer
realization. G50/G51's exclusion of periodic ACTUAL positive-integer
codes therefore cannot be applied to all periodic maximizing limits.

## 5. Exact hand controls and endpoint objections

1. **The cut itself is not discarded.** At a=1/3, X=2/3 maps to 0. The
   criterion includes this parameter; its threshold word 1000... is
   absent at equality and enters at every increase. Replacing <= by <
   in the criterion would be false even at j=0.
2. **A finite escape really yields a neighborhood.** At a=5/12, X=5/6,
   the exact orbit is `5/6 -> 1/4 -> 3/8 -> 9/16 -> 27/32`. The first
   violation is n=4 with v=1/96. The choice delta=1/1200 keeps branches
   1,0,0,0 fixed and gives
   `v-(beta^4+1)*delta=103/19200>0`. Thus the language is constant on
   `[333/800,1001/2400]`. This is a small certified interval INSIDE an
   already known G294 gap-4 band, not a new maximal band or new number.
3. **The outer cutoff is strict for a reason.** At a=13/27, the threshold
   code is 101000..., with a gap of 2. Its scaled orbit is
   `26/27 -> 4/9 -> 2/3 -> 0`, so it is in E. This does not contradict
   the gap>=3 cover below13/27. The endpoint can separately be added as
   a single point without changing any length or dimension bound.
4. **No integer conclusion follows.** The word witnessing a right
   increase can be periodic or terminating; G50/G51 exclude these for
   positive-integer histories. Even the nonperiodic exceptional codes
   still need the exact arithmetic realization filter. A zero-length
   set of real ceilings need not avoid a specified countable arithmetic
   set. The preceding compactness lemma does exclude terminating
   maxima for infinite-one histories, but not periodic limit maxima.
   None of these covers supplies a new integer-residue bound.

## 6. Sources, status and next step

Record searched: reviewed G50/G51, G293, G294; GC2476/L1386 and
GC2479/L1388; GC2481/L1389 and pending GC2483; current threshold records.
The actual kit/portal snapshot c42f6e5133f61a47e99289fd4b6e0536fd8a0453
was completely refreshed07:28:40Z. Actual Coon main
b6876a5f6e2772aa356a0440c8766b0ffbbd4dfe was refreshed08:19Z and searched
for bifurcation/dimension candidates: its run-map fixedpoint bifurcations
and real-Z-number measure/dimension claims are different objects. This
does not amount to a full new-library review or theorem equivalence audit.

Known, reproved here: self-survival characterizations of parameter
bifurcations and symbolic prefix covers. Baker–Kong,
[arXiv1904.07007v1](https://arxiv.org/abs/1904.07007v1), Proposition2.3(i)
states the lower-hole criterion `G_beta^n(t)>=t` under its conventions.
Its direction and closed/strict survivor conventions differ; section2
above proves the present upper-ceiling version with its own cut guard.
Retained v1 PDF SHA256:
`d84fcb8d452d9d310105f1f43513e77877cc6a4052f5a4eb648a36ada1aa4f62`.
G293's reviewed prefix-count/cylinder method concerns the closed 2-adic
code space and dimension log_2(3/2), not this real parameter set. G294
supplies the two-one costs, not this parameter conclusion.

All new conclusions in sections2–5 remain **PROOF-SKETCH pending Local's
carrying read**. Exact controls are self-checks. No kernel build,
submission, novelty, or positive-integer survival is claimed.

Next executable step: classify terminating threshold codes in E below13/27.
For their finite word u ending in 1, test whether lowering that last 1 to
0 always produces the actual strict suffix predicate for the carried
word constructor, hence an upper plateau endpoint T_w=a. The first
objection is a suffix equal to a prefix before the last-bit change; settle
it directly. Separate the exceptional u=1 at a=1/3, and do not infer that
nonterminating threshold codes or all components are thereby classified.
Independent alternative: a new Rule30 actual-history relation from Local,
or audit one existing G51 arithmetic filter against this parameter
criterion without inventing a residue bound. More band enumeration and
unchanged source hunting remain cold.

My own pull: the finite escape certificates and exceptional parameter
geometry explain the bands without treating lost integer information as
recovered.
