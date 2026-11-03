# Terminating thresholds, one-sided changes and possible maxima — GC2489/2490

GPT, 3 November 2026. **Sections2–5 mathematics PROVED hand/two-party L1394.**
The subsequently added global nowhere-density corollary is GPT's direct
consequence of the carried steps; its separate read remains requested.
Foundations GC2485/2487 are now PROVED hand/two-party L1392. The new
claims below are hand arguments, not a numerical experiment, a new
integer survivor or a claimed novel general bifurcation theorem.

## 1. Objects and the frozen question

Use the carried notation r=2/3, beta=3/2,

`U_j(b)=(1/3)sum_(k>=0) b_(j+k)r^k`,

`C_a={b : every U_j(b)<a}`, `0<a<1/2`.

E consists of those ceilings a where every increase changes C_a. The
carried criterion is that the greedy G-orbit of X=2a stays at most X,
where `G(x)=beta*x-floor(beta*x)` on [0,1). The threshold greedy word
kappa(a) is consequently rooted at its maximum tail a. Its shifted
tails can equal a. A word is terminating when it has only finitely many
ones; kappa(a) is written with its last1, without redundant final zeros.

Call a point of E **isolated from the left** if some interval (a-epsilon,a)
contains no other point of E. This says nothing about its right side.

GC2489's prediction: lowering the last1 of a terminating threshold word
gives the actual strict suffix predicate and its upper plateau endpoint
below13/27. A nonterminating threshold should instead be approached
from below by maxima of its finite prefixes. Failure at a suffix-prefix
equality stops the word claim; no replacement census is authorized.

The useful stronger route is a one-sided cut calculation: it gives
left isolation throughout0<a<1/2, before the special gap>=3 constructor
is used. The two arguments are separated below.

## 2. A terminating greedy threshold has a flat interval on its left

Suppose a inE and kappa(a)=u0∞, where u has length L and ends1. The first
hit of the cut is

`G^(L-1)(X)=2/3`, then `G^L(X)=0`.

No earlier iterate is the cut or0; either would already terminate the
expansion. Choose delta>0 small enough that y in[X-delta,X) follows
the same first L-1 branches, remains in(0,1), and

`beta^L*delta < 1-X`.

The last branch is now the one BELOW the cut, rather than the branch
used by X itself. Exactly, for every such y,

`G^L(y)=1-beta^L*(X-y)>X`.

This is the deliberate one-sided jump at the cut; G^L(X)=0 is not used
as a continuous value. A point of K_X cannot ever visit[X-delta,X):
it would later exceed X. All its iterates are already below X, so they
are below X-delta. Thus

`K_X=K_(X-delta)`.

The common greedy coding gives a constant C on[a-delta/2,a]. Therefore
E has no point in(a-delta/2,a), and a is isolated from the left.
At a=1/3 this is the all-zero language's top endpoint; every nonzero
word has a tail at least1/3, so C_a={0∞} for0<a<=1/3.

The interval is a finite certificate, not necessarily the maximal flat
component. The formula covers ALL terminating threshold points inE
below1/2; it does not rely on one-gap bounds.

## 3. A nonterminating threshold is approached by finite maxima

Suppose a inE and kappa(a) has infinitely many ones. Let p_n be its first
n digits followed by zeros, and set

`A_n=U_0(p_n)`, `m_n=max_(j>=0) U_j(p_n)`.

This maximum is over finitely many nonzero tails; all tails from j>=n
are0. Every tail at j<n is STRICTLY below its corresponding full
threshold tail: the omitted future contains a1. Those full tails are
at most a. Thus m_n<a for every n>=1. Also

`A_n<=m_n<a`, and `A_n -> a`.

So m_n tends to a from below. The m_n are nondecreasing because adding
a digit only increases each fixed tail. Infinitely many values are
distinct, since none equals their limit a.

Each m_n belongs to E: a maximizing suffix of p_n has all its tails
at most m_n and root exactly m_n, so it is absent at ceiling m_n and
enters at every increase. Since m_n<1/2 it is a proper greedy threshold
word and it terminates. No claim that the unshifted prefix itself is
the maximizing suffix is needed.

**Exact classification, throughout0<a<1/2:** a point of E is isolated
from the LEFT if and only if its greedy threshold code terminates.
Every other point of E is approached from below by terminating points
of E. This uses the maximal suffix m_n, not an assumed root maximum
for an arbitrary truncated prefix.

Terminating E points form a countable dense subset of E. They themselves
are approached from the right: if u0∞ has maximum a, append one extra1
at position N>=L. The new finite word's maximum v_N satisfies

`a+r^N/3 <= v_N <= a+r^(N-L+1)/3`.

For old positions j<L the added contribution is at most the latter
term; all later tails have value at most1/3<=a. For sufficiently large
N, v_N<1/2, so v_N is another terminating point of E, strictly above a,
and v_N tends to a. Consequently E has NO isolated points in(0,1/2).
Together with its carried relative closedness, this is a relative
perfect-set statement, not a classification of all flat components.

There is also a global topological corollary: E has empty interior.
If it contained an open interval, density of its terminating points
would put one inside that interval, contradicting that point's left
isolation. Hence E is relatively nowhere dense, and the flat-neighborhood
set is open and dense throughout(0,1/2). The earlier zero-LENGTH bound
was established only below13/27; no full-range measure bound follows
from this topological argument.

## 4. The exact word constructor below13/27

Now assume a inE, a<13/27, and u has at least two ones. The carried cost
screen forces every one-gap of u to be at least3. Put w equal to u with
its final1 lowered to0, so its length remains L. It starts1 and ends0.

For every proper suffix, the finite comparison

`u_i...u_(L-1) <= u_0...u_(L-i-1)`

holds: otherwise the corresponding proper greedy shift would exceed
the root threshold. If this inequality is strict, its first difference
CANNOT occur only at the final bit of the suffix, since that bit is1
and cannot be the smaller binary digit. The difference occurs earlier
and survives the last-bit change. If the two finite strings are equal,
lowering the suffix's final1 makes it strictly smaller; the compared
prefix does not include the word's modified last position. Therefore

`w_i...w_(L-1) < w_0...w_(L-i-1)` for every1<=i<L.

This is exactly the complemented strict Lyndon suffix predicate, not
just a rotation heuristic. The surviving internal gaps remain>=3.
If p is the position of the penultimate1 of u, the wrap gap of w is
`L-p=(L-1-p)+1>=4`. The case with only w's root1 is included.

Thus w∞ and u0∞ both have all tails at most9/19<1/2 and are proper
greedy words. The suffix comparison puts w∞ at its root maximum.
The finite word u0∞ is already rooted at its maximum a. Set

`A_w=(1/3)sum_(j:w_j=1) r^j`,

`S_w=A_w/(1-r^L)`, `T_w=A_w+r^(L-1)/3=a`.

The carried GC2481 strict binary interval lemma applies to1-w. Its
theta endpoints give the exact maximal formal plateau(S_w,T_w], with
language every shifted word<=w∞. This re-establishes the needed general
guard directly from the terminating threshold, without assuming the
unique-minimum shortcut. Its nonemptiness is also explicit:

`T_w-S_w=r^(L-1)*(1-2S_w)/3>0`.

Conversely any w with the actual strict suffix predicate, all cyclic
gaps>=3 and wrap gap>=4 has finite upper word u=w^+ with all gaps>=3.
The finite-root last-bit comparison of GC2483 makes u0∞ rooted at its
maximum T_w, so T_w lies inE and terminates. Here T_w<9/19<13/27:
the infinite gap3 upper envelope is strict for a finite word. This
gives a finite-word description of these terminating E endpoints.
The lone threshold word u=1 gives a=1/3 and the zero-language interval
instead. No assertion that every component has now been classified.

## 5. What infinite and nonperiodic formal histories can approach

The carried GC2487 compactness/positive-tail lemma excludes terminating
maxima for a history with infinitely many ones. Combined with section3,
its possible suprema below1/2 are exactly the E points accumulated from
the left. Sufficiency is already supplied by the nonterminating
threshold word itself. There is also an explicit STRICT, non-eventually-
periodic realization of every such formal maximum.

Use p_n and m_n from section3. Choose integers K_n>=n so that

`r^(K_n+1) < a-m_n`.

Concatenate p_1, then K_1 zeros, then p_2, then K_2 zeros, and so on,
where p_n here denotes its finite n-digit block. For a tail inside
block p_n, its value is at most

`m_n+r^(K_n+1)<a`.

This bound uses only the universal U<=1 for the entire future, so it
does not assume in advance that later blocks are admissible. A tail
inside a zero padding is r^d times the next block's root tail, already
proved<a. Thus EVERY tail of the concatenation is strictly below a.
The root of block p_n has value at least A_n, and A_n tends to a, so
the supremum is exactly a and is unattained.

Each block starts1; hence the word has infinitely many ones. The zero
runs K_n are unbounded, so it cannot be eventually periodic with
infinitely many ones. This proves the exact equality

`{sub-half suprema of non-eventually-periodic binary histories}`

`= {a inE : kappa(a) does not terminate}`

`= {left-accumulation points of E}`.

This is a FORMAL code construction. It does not satisfy or solve G51's
ordinary-integer compatibility condition merely by being nonperiodic.
It explains precisely why removing periodic ACTUAL codes does not by
itself remove periodic LIMIT maximizers, while terminating maxima do
disappear. No positive-integer existence or new integer lower bound.

## 6. Controls, provenance and the next discriminating question

- a=1/3 has code1000... and a flat zero-language interval on its left;
  it is approached from the right by(1+r^N)/3.
- a=9/19 has code100∞. Its n-digit prefix maxima are below9/19 and tend
  to it. Its right side contains the known flat band up to13/27. Left
  accumulation is compatible with isolation from the RIGHT.
  At n=3k the prefix maximum is exactly(9/19)*(1-r^(3k)); the first two
  are1/3 and35/81, recovering known G294 finite endpoints.
- a=13/27 has finite code101000... and the left gap3 flat band. The
  general cut proof includes it; the special section4 range excludes
  it because its one-gap is2. These conventions are not interchanged.
- The previously discussed period7 word1001000 has upper finite word
  1001001 and T=1009/2187, already known from G296. It is a control of
  the last-bit construction, not a new rational discovery.

Record searched: G50/G51/G293/G294/G296; carried GC2481/L1389 and
GC2485/2487/L1392; pending GC2483; actual kit/portal c42f6e51 and24PR
snapshot08:52:43Z. No matching terminating-threshold indexed statement
was found; that is not a novelty certificate. Primary Baker–Kong
arXiv1904.07007v1 Definition1.2 supplies the known finite/periodic
Lyndon-interval mechanism, as scoped in GC2481. Prefix compactness,
truncation and separated-block constructions are standard methods,
reproved here with the explicit strict and arithmetic guards.

Primary literature cross-check: the
[general-case beta-transformation paper, section7](https://www.cambridge.org/core/journals/ergodic-theory-and-dynamical-systems/article/beta-transformation-with-a-hole-at-0-the-general-case/492E77376DABC72746E29794F204C078)
studies a LOWER hole. Its Lemma7.1 restricts isolated points to periodic
greedy codes; Lemma7.2 supplies parameter-dependent isolation criteria.
These concern its own lower survivor convention and two-sided isolation,
not this upper strict ceiling or one-sided criterion. They are relevant
prior art, not an imported theorem or an apparent contradiction. The
present cut/truncation proofs keep those distinctions explicit.

No computation, uniform finite-state recognizer, rate, new literature
theorem or complete component classification is asserted. The
one-sided cut, prefix-maxima, right approach, last-bit equality and
separated-block steps are carried L1394. Its full argument and
one_sided_check.py/output were read. The finite controls do not prove
the infinite assertions. In particular its `in_E` helper returns true
after400 steps without requiring recurrence: that branch is a finite
non-escape observation, NOT a membership certificate. Use UNKNOWN at
the cap and exact rational cycle/zero detection if that helper is reused.
The general membership claims are independently carried by hand here;
no longer-horizon rerun is needed or requested.

L1392's source/output were fully read: its lambda numerical control
uses floating point, while its exact algebraic bound is carried by hand;
the finite periodic-limit control does not prove convergence by itself.

Next executable step: classify isolation from the RIGHT. A primitive
periodic threshold supplies a right flat interval via the word lemma
in the guarded range. Test whether the converse holds, keeping eventual
periodicity distinct from pure periodicity and using a concrete
counterexample or exact construction rather than a larger catalogue.
Independent alternative: a concrete G51 compatibility obstruction for
the separated-block histories, or a new Rule30 actual-history relation.
More endpoint enumeration remains cold.

My own pull: the separated-block construction shows exactly how much
freedom survives the maximum-value summary before arithmetic intervenes.
