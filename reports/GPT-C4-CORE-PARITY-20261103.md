# C4: the exact parity condition for the single seed — GC2525

GPT, 3 November 2026. **PROOF-SKETCH pending independent carrying read.**
This is a precise bridge and an obstruction to weaker bridges, not a proof of
Problem 2. No new computation, seed search, formalization or novelty claim.
The discrepancy and pairing facts below are elementary counting identities.

## The statement, with the actual indices

Write x(s,j) for the bit at time s and position j in the whole-line Rule 30
orbit starting with one black cell at position zero. Parity means the XOR
of a finite list: it is one exactly when the list contains an odd number of
ones. OR is one when at least one of its two arguments is one.

At kit main c42f6e5133f61a47e99289fd4b6e0536fd8a0453,
`Rule30Diagonals.center_eq_parity` supplies, for t >= 2,

```
O_t(s) = x(s,s-t+1) OR x(s,s-t+2),   0 <= s < t;
c_t = x(t,0) = XOR_{0 <= s < t} O_t(s).
```

These +1,+2 offsets matter. Choose any integer cutoff 0 <= b(t) <= t and set
A_t = XOR over s < b(t), B_t = XOR over b(t) <= s < t. Then c_t = A_t XOR B_t
exactly. This makes no assertion that A_t has a fixed periodic table.
Two distinct choices are the earlier crystal/news split
`b(t) = floor((4t-3)/6)+1`, and the core split `b(t) = floor(4t/5)`.
For the latter B is the final fifth, A includes everything before it.
Using `ceil(4t/5)` instead changes an event at many times and cannot be
ignored as a small density error in the *parity*.

Use the N times t = 2,...,N+1, and write chi(v) = (-1)^v. For a = 0,1 let
I_a be the times with A_t = a, n_a their number, and

```
D_a(N) = sum_{t in I_a} chi(B_t).
```

A bit sequence is balanced when its fraction of ones tends to one half,
equivalently its mean sign tends to zero. Directly separating the two classes,

```
sum chi(B_t) = D_0 + D_1;
sum chi(c_t) = D_0 - D_1.
```

Consequently the **weakest exact condition** here is
`(D_0-D_1)/N -> 0`. It is precisely Problem 2 rewritten, with no inference
from right-edge fairness. A useful stronger condition is

```
D_0(N) = o(N) and D_1(N) = o(N).                 (CB)
```

Here o(N) means that division by N tends to zero. CB holds **if and only if
both B and the centre are balanced**: add and subtract the two displayed
identities. Thus, **given balance of this actual B**, CB is equivalent to
Problem 2. Without that extra hypothesis it is sufficient, not necessary.
The omission of the first two centre observations changes means by O(1/N),
so this matches the actual kit Problem 2, via
`Rule30Equivalents/ProblemTwo.lean`'s half-density/limit equivalence.

For a conditional mean beta_a = D_a/n_a (zero if n_a = 0), CB says
`(n_a/N)*beta_a -> 0`, not necessarily `beta_a -> 0`. This handles empty
classes, classes of density zero, and class frequencies that do not converge.
No limiting frequency of A is assumed.

There is an equally short correlation formulation. Let Abar, Bbar, Cbar be
the respective empirical sign means and set
`Cov_N = Cbar - Abar*Bbar`. Given Bbar -> 0, centre balance is equivalent to
Cov_N -> 0, since |Abar| <= 1. This asks for one signed correlation to vanish;
full statistical independence or a mixing theorem is stronger than needed.
Neither this correlation nor balance of B follows from the right-edge flags.

## Cheap objections settled without a run

These are countermodels to proposed *logical implications*, not alleged
Rule 30 orbits. They use any ordinary consecutive nonnegative time indexing;
deleting finitely many indices does not change their limits.

1. A_t = B_t = t mod 2. Both pieces are balanced; their XOR is constantly zero.
   Marginal fairness alone proves nothing about the centre's balance.
2. A_t = t mod 2, B_t = 0. The centre is balanced, but D_0 and D_1 are each
   asymptotic to N/2. CB is not necessary without balance of B.
3. Let A_t be one only at powers of two, and B_t = t mod 2. The rare A=1
   class has conditional sign tending to one, but D_1 = O(log N) and
   D_0 = o(N). Both B and the XOR are balanced. An unweighted condition on
   every conditional mean would discard a valid case.
4. Choose any sequence f, even one whose density has no limit, and put
   A_(2k) = A_(2k+1) = f(k), B_(2k) = 0, B_(2k+1) = 1.
   Each full pair cancels within its A class, so |D_a| <= 1 on prefixes.
   CB needs no convergent class frequency.

## Why testing a few samples at a time cannot settle the growing parity

For n bits uniformly distributed among the even-parity words, every choice
of k < n coordinates is exactly uniform: each assigned pattern has
2^(n-k-1) completions. Yet the parity of all n bits is always zero.
This is the standard distinction between tests of a few coordinates and a
parity of the whole word; see O'Donnell, *Analysis of Boolean Functions*,
§6.1, Definition 6.15 and Example 6.16 in the
[author's text](https://www.cs.cmu.edu/~odonnell/papers/Analysis-of-Boolean-Functions-by-Ryan-ODonnell.pdf).

The obstruction also has a deterministic time-array version. Take any
integer m(t) -> infinity with m(t) >= 2. Set the first m(t)-1 entries of
row t to the low binary digits of t and the last entry to their XOR.
Every fixed finite set of coordinate indices eventually consists of binary
digits of t, hence has uniform empirical frequencies, by their finite
period. Nevertheless each entire row has even parity. This does not assert
uniformity for indices that themselves move with t, or for every pooled test.

In C4 the needed character is specifically
`chi(A_t) * product_{b(t)<=s<t} chi(O_t(s))` averaged over t. The number of
factors grows. Proving fairness of single factors, or every fixed small
set of them, does not prove that this average vanishes. This names the
missing estimate rather than attributing the difficulty merely to
information being lost or to a core looking random.

## A concrete route: an actual time pairing

Suppose all but u_N = o(N) of the N actual time indices admit a pairing
such that paired indices have the same A bit and opposite B bits. Each
pair contributes zero to its D_a; therefore |D_a| <= u_N and CB follows.
No independence assumption is needed.

For arbitrary fitted matchings, however, the minimum number left unmatched
is exactly |D_0|+|D_1|: within each A class pair a B=0 index with a B=1
index until the minority is exhausted. Thus merely asserting that *some*
matching exists is another formulation of CB. A productive proof would
construct the pairing from a Rule 30 time shift or another explicit orbit
identity, and bound unmatched times without already counting the target
colours. No such construction is supplied here. An involution on initial
seed bits pairs different initial conditions, not times of this single
seed; the B2 family result and C3 ensemble counts cannot fill this gap.

**Next executable step:** a carrying read of the exact CB equivalence,
zero-density guards and pairing limitation. Any later dynamical attempt
must exhibit its actual time transformation and identify how it preserves
A and flips the *whole* B. Do not launch another marginal census first.

## Sources and search scope

Record searched: `record_find.py` query
`conditional.bias|core.parity|signed.corr|pairing.*(parity|time)|parity.*independen`;
GC2404's existing equal-parity counterexample; NIGHT-TASKS C1/C4; complete
`diagonal_segments.py` and `parity_census.py`/output; current kit actual
`Rule30Diagonals` accumulating-XOR proof, `Rule30Prize` Problem 2 definition,
`ProblemTwo` half-density equivalence and `CesaroMeans` weighted-average scope.
Kit hash above. Last successful COMPLETE external index: 11:50:45Z on
3 November; targeted searches do not advance that clock. This is elementary
bookkeeping applied to known identities, no new submission claim and no
inference of novelty from missing search hits. Source audit GC2526 below
withdraws the old M5 measurements' attribution to the single seed.
