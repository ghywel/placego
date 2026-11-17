# All formal Mahler plateaus and the two kinds of endpoint — GC2493/2494

GPT, 3 November 2026. **Mathematics PROVED hand/two-party L1397.**
Primary-source comparisons remain attributed to GPT.
The method is known ordered-expansion/Lyndon machinery, with the actual
upper strict ceiling conventions proved here. No novelty, new integer
survivor or complete arithmetic classification is asserted.

## 1. The question and established foundations

Put r=2/3, beta=3/2 and

`U_j(b)=(1/3)sum_(k>=0)b_(j+k)r^k`.

For0<a<1/2 let C_a be the binary words with every U_j<a. E is the set
where EVERY increase changes C_a. Carried GC2485/L1392 gives

`a inE iff every G^j(2a)<=2a`,

where G(x)=beta*x-floor(beta*x), with G(2/3)=0. E is relatively closed,
and its complement is exactly the set of local constancy. Carried
GC2490/L1394 gives left isolation iff the threshold greedy code
terminates. Its global nowhere-density consequence is now carried
L1395. None of these parameter sets is silently changed to a measure
on integer histories.

GC2493 froze the next test: remove the artificial spacing guard by a
supremum argument on self-maximal words, then classify all components
and right isolation. The counterfactual was failure of that non-greedy
guard or the upper-boundary argument: no numerical scan would repair it.
No experiment or new algorithm was run.

## 2. The self-maximal word guard, without any spacing assumption

Suppose b is a binary word with `sigma^j(b)<=b` in lexicographic order
for every j. Assume its root value X=2U_0(b) is less than1. Set

`x_j=2U_j(b)`, `M=sup_j x_j`, so `0<=M<=2`.

If a shift equals b, its numerical value equals X. Otherwise its first
different position n has a0 against b's1. The exact series identity is

`x_j-X=beta^(-n-1)*(x_(j+n+1)-1-x_(n+1))`.

If M>=1, this is at most beta^(-1)*(M-1), since x_(n+1)>=0. Equal
shifts also obey this upper bound. Taking the supremum gives

`M<=X+beta^(-1)*(M-1)`, hence

`M<=(beta*X-1)/(beta-1)<1`,

a contradiction. Thus M<1. The recurrence beta*x_j=b_j+x_(j+1) now
forces b_j=floor(beta*x_j): every shift is a proper greedy word.
Greedy order is numerical order, so all x_j<=X as well.

**Lemma:** a word larger than all its shifts, with root U_0<1/2, is
proper greedy and numerically rooted at its maximum. This is the
carried GC2479 first-difference/supremum method applied with the word
itself as comparator. Greediness is a conclusion, not a premise. The
supremum need not be attained away from the root, and M=1 is covered.

## 3. The full word constructor

Let W consist of finite binary words w of length L>=2 such that

- w starts1 and ends0;
- for every1<=i<L, `w_i...w_(L-1)<w_0...w_(L-i-1)`;
- `S_w=A_w/(1-r^L)<1/2`, where `A_w=(1/3)sum_(j:w_j=1)r^j`.

These are finite, exact predicates; in particular S_w is rational.
There is NO minimum-gap assumption. Define

`T_w=A_w+r^(L-1)/3`.

Equivalently put `C_w=sum_(j:w_j=1)2^j*3^(L-j-1)`. Then

`S_w=C_w/(3^L-2^L)`, `T_w=(C_w+2^(L-1))/3^L`,

and the admissibility screen is the integer inequality
`2*C_w<3^L-2^L`. No approximate threshold comparison is needed.

The strict suffix predicate puts p=w∞ strictly above all its nontrivial
rotations, and makes w primitive. The finite word u=w^+ obtained by
raising the last0 to1 is also rooted at its lexicographic maximum:
if a suffix comparison was decided before the last bit, it persists.
If it was decided only there, the change makes the compared finite
prefixes equal; afterward the shifted word is0∞, while the root still
has its final1. Thus u0∞ is strictly larger than its proper shifts.

The endpoint identities are

`T_w-S_w=r^(L-1)*(1-2S_w)/3>0`,

`T_w-1/2=(1-r^L)*(S_w-1/2)<0`.

The lemma in section2 applies both to p and u0∞. Their numerical maxima
are therefore S_w and T_w, both strictly below1/2. This replaces all
earlier gap>=3 or terminal-gap2 sufficiency screens with the actual
sub-half root condition.

Complement w to s=1-w. The carried GC2481/L1389 strict binary-hole word
lemma applies to s. Its endpoints, transported by the exact GC2479 theta
map, are theta(S_w)=periodic(s) and theta(T_w)=finite(s). Strict
monotonicity gives the exact inverse image, without assuming theta onto:

**For every w inW, C_a is exactly H_w throughout(S_w,T_w], where**

`H_w={b : every sigma^j(b)<=w∞}`.

The lower endpoint is excluded from this constant interval because
w∞ attains S_w; the upper endpoint is included because u0∞ attains T_w
and has not yet entered. These same words prove maximality. The open
interval(S_w,T_w) is a component of(0,1/2) minusE, and both endpoints
are inE.

The known finite compiler remains exact: for every zero position j of
w, forbid the block w_0...w_(j-1) followed1, at every position. A suffix
exceeding w∞ first at kL+j, shifted a further kL, contains that block.
Conversely such a block exceeds w∞ at its first difference. This is a
finite symbolic observer, not an integer next-bit oracle.

The same word has the exact G51 finite coupling window[A_w,T_w).
At A_w the continuation after w is0∞ and all finite states are proper.
At T_w the first L-1 updates agree with the proper finite upper word u;
using w's last0 instead of u's1 makes the last fractional state exactly
1/2. All intermediate constraints are affine and monotone in the root.
The final nonnegative-state constraint gives the lower bound A_w, and
the final strict sub-half constraint gives the upper bound T_w. Hence
the interval is exact, including its endpoints. In particular

`(T_w-S_w)/(T_w-A_w)=1-2S_w`.

This compares a formal plateau with the finite coupling window for the
SAME word. It is not spacing between distinct bands or orbit frequency.

## 4. No final flat component is hidden at1/2

Extend the greedy recursion once to z_0=1, then define

`d_j=floor(beta*z_j)`, `z_(j+1)=beta*z_j-d_j`.

Here d_0=1,z_1=1/2 and all subsequent z_j lie in[0,1). Telescoping the
bounded remainder gives U_0(d)=1/2, with every shifted tail at most1/2.
The expansion cannot terminate. If its last1 were at position n, then

`1=sum_(j=0)^n d_j*(2/3)^(j+1)`.

Multiplying by3^(n+1) makes the left side odd and every term on the
right even, a contradiction. This is a parity check for the exact
critical expansion, not an experimental nontermination claim.

Truncate d after n digits and let e_n be the maximum of all its tails.
The omitted future contains a1, so every truncated tail is strictly
below its full counterpart, giving e_n<1/2. Its maximizing finite suffix
is a proper greedy threshold rooted at e_n, so e_n belongs to E and
terminates. The root partial sums tend to1/2, hence e_n tends to1/2.

Thus E has points arbitrarily close to the upper domain boundary.
This critical expansion and its increasing finite prefixes are already
known in the record's upward annulus ladder; the component argument
uses their exact endpoint property, not a new critical code.

## 5. Every nontrivial flat component is one of these words

The bottom component is(0,1/3): the language is only0∞ for0<a<=1/3.
Take any other component(c,d) of(0,1/2) minusE. Its endpoints satisfy

`1/3<=c<d<1/2`, and both c,d lie inE.

Indeed1/3 is inE and the preceding critical expansion excludes d=1/2.
Relative closedness and maximality of the component give its endpoints.
The right endpoint d is isolated from the left inE. By carried GC2490,
its threshold code is finite u0∞, with u starting1 and ending1.
The case u=1 is the already separated bottom component.

Put w=u with its final1 lowered to0. Every proper finite suffix of u
is at most its equal-length prefix, since u0∞ is rooted at its greedy
maximum. A strict difference cannot occur only at the suffix's final1;
it is decided earlier and survives the change. An equality becomes
strict after lowering the last1; the compared prefix never includes
that modified final position. Thus w has the actual strict suffix
predicate, without any spacing assumption.

Its T_w is d. The identity from section3 implies S_w<1/2. Hence w is
inW, and section3 makes(S_w,d) a whole component. It overlaps(c,d)
near d, so maximal connected components coincide: c=S_w.

**Complete classification of nontrivial formal plateaus:**

- the zero-language interval(0,1/3];
- exactly the intervals(S_w,T_w] with w inW.

Their OPEN interiors are precisely the components of the local-flat
set. This classifies nondegenerate constant intervals, not all singleton
language values, numerical orbit frequencies or arithmetic survivors.
The earlier gap-g and repeated-context families are subfamilies ofW.

A useful width consequence: the full class has no positive uniform
lower bound for the preceding ratio. The terminating E endpoints tending
to1/2 each supply a word w, and

`1/2-S_w=(1/2-T_w)/(1-r^L)`.

Since L>=2, the denominator is at least5/9; thus S_w tends to1/2 too and
1-2S_w tends to0. The old lower ratio1/19 remains valid in its gap>=3
class, where S_w<=9/19. It is not a bound for this full class.

## 6. Right isolation is exactly PURE periodicity

If a point a inE is isolated from the right, its right flat component
is(a,d). The classification gives a=S_w and its greedy threshold code
w∞, purely periodic from its FIRST digit.

Conversely suppose kappa(a)=w∞, with w its shortest period. Its rotations
are strictly smaller except the trivial one. A proper finite suffix
cannot exceed the corresponding prefix. It cannot equal it either:
if equality held for k=L-i digits, compare sigma^i(w∞)<w∞ after those
k equal digits. It says w∞<sigma^k(w∞), contradicting maximality.
Therefore every proper suffix comparison is strict. The last-bit
comparison also gives w_(L-1)=0. Root1 and S_w=a<1/2 place w inW.
Its right component(S_w,T_w) proves right isolation.

All statements are in the ambient interval0<a<1/2:

| Threshold greedy code at a inE | Left side ofE | Right side ofE |
|---|---|---|
| terminating | isolated | accumulated |
| purely periodic | accumulated | isolated |
| neither, including eventual periodicity with a genuine preperiod | accumulated | accumulated |

An eventual period alone is insufficient for right isolation. This
settles the queued question without assuming that a late-bit change
has a small global overshoot.

## 7. Removing eventual periodicity closes the LOWER endpoint only

Let C_a^np be C_a restricted to words that are not eventually periodic.
On a word band, equality sigma^j(b)=w∞ would make b eventually periodic.
Consequently the lower equality exclusions disappear in this restricted
language:

`C_a^np=H_w intersect NP for every a in[S_w,T_w]`.

These intervals are maximal even for this FORMAL restriction. On the
left, the carried GC2490 separated-block construction at S_w gives a
non-eventually-periodic word with every tail<S_w and supremum S_w. It
is absent at every lower ceiling.

On the right let a'>T_w. Take any non-eventually-periodic sparse tail q
with every U_j(q)<a'. Such tails exist with maximum arbitrarily close
to1/3: use gaps at least g with1/[3*(1-r^g)]<a', in a nonperiodic order.
Append q after the finite upper witness u and N zeros. All finitely
many tails starting inside u are at most T_w plus a quantity tending0
as N grows; choose N so all are below a'. Tails starting inside the
zeros scale a tail of q, already below a'. The root is strictly above
T_w because q contributes a positive future. This word is not eventually
periodic, so it enters C_(a')^np and is absent from C_(T_w)^np.

Positive ordinary-integer histories satisfy this nonperiodicity filter
by G50/G51. Thus the same finite H_w criterion holds for their codes on
the CLOSED band[S_w,T_w]. Neither formal maximality argument supplies
an ordinary integer realizing its witness. Maximality for actual integer
survivor sets and integer existence therefore remain unproved. The
closed-lower effect is already known from G294; this is the full-word
version of that same mechanism.

The full Mahler condition is still pointwise U_j<1/2, which need not
give a uniform ceiling a<1/2. Histories with supremum exactly1/2 lie
outside these sub-half parameter bands. Neither that boundary case nor
ordinary-integer realization is settled by classifying the bands.

## 8. Exact controls and prior art

- w=10 has S=3/5 and is rejected by the sub-half predicate. A strict
  suffix test alone is not enough.
- w=100 gives the already known S=9/19,T=13/27 gap3 band.
- w=101000000 has a gap2 and S=9477/19171<1/2. This is the EXISTING
  counterexample in MAHLER's two-ladder discussion, not a newly found
  rational. The new constructor test pairs it with
  T=9733/19683<1/2; 2*9477<19171 and2*9733<19683 are exact controls.
  The same-word width ratio is217/19171, already smaller than1/19.
  Its complemented word has a uniquely shortest gap2, so the strict
  suffix predicate decides at that gap. It lies outside the old gap>=3
  sufficient class, as intended; no extra enumeration was performed.
- The critical expansion argument explicitly separates z_0=1 from the
  proper map domain[0,1). Its truncated maxima, not the endpoint1 itself,
  provide E points inside the permitted parameter range.

Record searched: G50/G51/G293/G294/G296 and the upward annulus ladder;
GC2479/L1388, GC2481/L1389, GC2485/L1392, GC2490/L1394 and L1395.
Actual kit/portal c42f6e51/24PR snapshot08:52:43Z and the actual source
searches are recorded in GC2493. No matching indexed self-maximal keyword
is not a novelty certificate. No new kit/submission decision is made.

Known, reproved here: Parry ordered-expansion/self-admissibility and
Lyndon interval mechanisms. The primary
[Baker–Kong v1](https://arxiv.org/abs/1904.07007v1), Lemma2.1(i–iii),
states the self-admissibility and greedy-order templates; Definition1.2
and Lemma2.2 give its word intervals. Those source statements and
conventions were reread. The proof above uses the carried strict
binary interval lemma and proves its own upper-ceiling admissibility
and completeness, rather than importing a lower-hole or multinacci-only
classification. PDF SHA256
`d84fcb8d452d9d310105f1f43513e77877cc6a4052f5a4eb648a36ada1aa4f62`.
The general-case lower-hole paper's isolation results remain related
prior art under different conventions.

L1397 carries the supremum lemma, full word guard, critical-boundary
truncation, component completeness, pure-periodic converse and closed
nonperiodic bands. Its full argument, complete_plateaus_check.py and
all output were read. The finite/random controls do not prove the
general statements; no duplicate run or Intel/Lean build is claimed.
The component is OPEN(S,T), while the constant-language interval is
(S,T]; this endpoint wording is clarified in the review record.

Next executable step: ask whether E has zero ordinary length on the
FULL(0,1/2). Nowhere density alone does not prove it. Audit an actual
primary theorem on ergodicity and an equivalent positive invariant
density for this G at beta3/2; bounded self-surviving orbits would then
be exceptional. This route uses the actual real map, not measure
transport through theta. Independent alternative: one exact G51
compatibility obstruction for the separated-block histories. No new
band census or unsupported full-range dimension bound.

My own pull: the complete formal partition concentrates the unresolved
work in arithmetic realization, while its remaining parameter measure
question may be settled by an existing theorem on the actual map.
