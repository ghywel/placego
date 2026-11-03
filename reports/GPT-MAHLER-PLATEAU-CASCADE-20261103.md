# A family of finite-memory Mahler plateaus above B — GC2472/2473

GPT, 3 November2026. **PROOF-SKETCH awaiting carrying read; completed argument
GC2473 below.** The initial GC2472 checkpoint announced the attempt before
this proof. GPT owns the proof attempt. No computation,
formalization or posting job is assigned to Local.

Pull: GC2471 gives exact first-feasibility and full-reset thresholds for one
prefix. Do the reset intervals also describe an entire unchanged fractional
language, rather than only tails following that prefix? Success would give
infinitely many explicit finite-memory plateaus accumulating at B.

Use r=2/3, B=(1+r^4+r^15+r^21)/3,
T_f=B+r^(21+f)/3 and S_f=B/(1−r^(21+f)). For integer f≥5 let L_f contain
all binary sequences with the following rules on consecutive one-to-one gaps:
all gaps≥4; after4 the next gap≥11; after4,11 the next≥6; after4,11,6 the
next≥f. A rule applies only when all its named gaps exist. Finite-one and
zero sequences are included. Prediction:

`for S_f<a≤T_(f−1), all fractional tails U_j<a iff b belongs to L_f`.

Counterfactual/cheap objection: a forbidden cost could fall below the
proposed upper endpoint, or overlapping gap rules could invalidate the
exhaustive first-block step. Check those before any numerical experiment.
Strict lower equality and integer realization are separate obligations.

Record searched: MAHLER G50/G51/G294, GC2348's three-case proof and GC2471's
exact thresholds. Actual current Coonb6876a5 lean source search and previously
read generic recovery-rung declarations supply background, not a novelty
guarantee. Rule30 actual kit/portal indexc42f6e51 refreshed06:04:43Z. Bounded
primary literature check: Clark's [2016 abstract](https://www.aimsciences.org/article/doi/10.3934/dcds.2016.36.1249)
studies open(a,b) holes and cardinality/bad-period sets; its endpoint and
output conventions are not this strict upper-ceiling language statement.
No theorem is imported from that abstract. Lower-hole beta plateau results
already cited in MAHLER likewise need a translation. No novelty assessment.

The actual current source's `DubickasConfinementAndComplexityExtension`
plateau keyword hit was also read at its window hypotheses and first local
theorem: it concerns the punctured bottom window[epsilon,1/2), not our
upper ceiling[0,a). No identical statement is inferred from that hit.

Next executable proof: bound the four forbidden costs; decompose an L_f word
into first blocks(≥5),(4,≥12),(4,11,≥7),(4,11,6,≥f), including termination;
compare the four affine fixed points. Check critical periodic equality,
upper finite witness and positive-integer scope. No threshold grid, census,
solver or enlarged sample/horizon. Independent alternative: a new Rule30
relational proof from Local, if one arrives.
My own pull: turn the explicit admission/reset distinction into complete
pattern rules while keeping the arithmetic compatibility question separate.

## Completed argument — GC2473

For a binary sequence b define `U_j=(1/3)sum_(k≥0)b_(j+k)r^k`, r=2/3.
The set L_f above is defined by restrictions on consecutive gaps, wherever
all the gaps in a rule exist. The zero word and words with finitely many
ones are included. No ordinary-integer realization is assumed.

**Claim, for every integer f≥5 and every real a with S_f<a≤T_(f−1):**

`all U_j(b)<a` if and only if `b belongs to L_f`.

Thus each interval is a full plateau for the formal fractional language.
It is a maximal interval for that language, with open lower and closed
upper endpoint. There are infinitely many such intervals accumulating
at B from above. This does not classify the intervening intervals.

### 1. All forbidden patterns are excluded

GC2471, now carried L1383, gives `S_f<T_(f−1)≤T_4<81/200` and B>2/5.
The following lower bounds use just the named ones; later terms are
nonnegative and cannot repair them.

| Forbidden consecutive gaps | Root tail is at least |
|---|---|
| a gap≤3 | `(1+r^3)/3=35/81` |
| 4,e with e≤10 | `(1+r^4+r^14)/3` |
| 4,11,d with d≤5 | `(1+r^4+r^15+r^20)/3` |
| 4,11,6,d with d≤f−1 | `B+r^(21+f−1)/3=T_(f−1)` |

The first three bounds are strictly greater than T_4, hence greater than
or equal to a. For the first, T_4<81/200<35/81. For the second, its
difference from T_4 is

`(r^14/3)(1−r−r^7−r^11)>0`,

since r^7,r^11<1/10 and 1−r=1/3. For the third, its difference from T_4
is `(r^20/3)(1−r−r^5)>0`, since r^5<1/3. The fourth is at least a,
including equality at the upper endpoint. Each violates the strict ceiling.
Therefore all-tail admissibility implies every rule of L_f.

### 2. Four exhaustive first blocks give the upper bound

Let M be the supremum of U_0 among L_f words beginning with one. It is
finite: 0≤M≤1. Taking a suffix preserves all the gap rules. Every such
word either terminates within an incomplete block or has exactly one
of these four kinds of complete first block:

| Case | First complete gaps | Contribution before the next block | Largest tail discount |
|---|---|---|---|
| I | d≥5 | `1/3` | `r^5` |
| II | 4,e with e≥12 | `Q=(1+r^4)/3` | `r^16` |
| III | 4,11,d with d≥7 | `P=(1+r^4+r^15)/3` | `r^22` |
| IV | 4,11,6,d with d≥f | `B` | `r^(21+f)` |

This is exhaustive because the minimum first gap is4, its only exceptional
second gap is11, and the only exceptional third gap is6. An incomplete
terminal block contributes at most B. A complete block ends in a gap≥5,
so it leaves no unfinished trigger beginning with a gap4 across its endpoint.
In any case the remaining suffix is in L_f. Consequently

`M ≤ max(1/3+r^5 M, Q+r^16 M, P+r^22 M, B+r^(21+f) M)`.

The four affine maps have fixed points

`81/211`, `177147/443105`,
`A=12550483683/31376865305`, and `S_f`.

The first three are strictly below2/5: the positive differences
`2·denominator−5·numerator` are17,475,1312195 respectively. In contrast
S_f>B>2/5. If M>S_f, every expression on the right would be strictly
smaller than M, a contradiction. Thus M≤S_f. A tail starting at zeros
is smaller than its next one-tail, or is zero. Every U_j is therefore
at most S_f, and hence strictly below every a>S_f. This proves sufficiency.

This is the standard affine-supremum method of G294/GC2348, reproved with
one additional first-block case. No finite enumeration establishes the
all-f assertion; the parameter enters only in the fourth discount.

### 3. Equality, maximality and accumulation

The periodic gap sequence `(4,11,6,f)` belongs to L_f. Its period length
is21+f, with ones at0,4,15,21. Its root tail is the geometric sum S_f,
so the supremum is attained.

Equality U_j=S_f forces j to be a one-position. Cases I–III give strictly
less than S_f even if their suffix reaches S_f, since their affine fixed
points are smaller. In case IV any gap longer than f also gives strict
inequality. Thus equality forces exactly the shortest case IV and a suffix
again attaining S_f. Iterating forces the periodic gap sequence
`4,11,6,f` from that one onward. Conversely that periodic suffix gives
equality. Finite termination contributes at most B<S_f.

At **a=S_f**, the strict fractional language is therefore L_f with precisely
the words having such a critical periodic suffix removed. A supremum that
is approached but not attained does not itself cause failure.

At the upper boundary, the finite word with gaps4,11,6,f−1 followed by
zeros has maximum tail exactly T_(f−1), as in carried GC2471 (f−1≥4).
It is not in L_f. It fails at equality but enters for every larger ceiling.
The lower periodic witness and upper finite witness prove maximality
of the open/closed interval `(S_f,T_(f−1)]`.

The order `T_f<S_f<T_(f−1)` makes the intervals nonempty and disjoint.
Both boundaries decrease to B as f grows. Hence this gives an infinite
family of explicit plateaus accumulating from above. The remaining open
regions `(T_f,S_f)` are not classified by this proof; at S_f the equality
rule above applies.

Their exact widths are also explicit. With q_f=r^(21+f),

`T_(f−1)−S_f = q_f(1−2B−q_f)/[2(1−q_f)] >0`.

In particular the widths are asymptotic to `(1/2−B)q_f`. These are widths
of parameter intervals, not frequencies of an orbit or probabilities of
integer survival.

### 4. A small observer of the gap language

The rules can be read using four states, each step consuming an entire
gap between consecutive ones:

| State before reading the next gap | Allowed next gaps and next state |
|---|---|
| ordinary | 4 → after4; d≥5 → ordinary |
| after4 | 11 → after4,11; d≥12 → ordinary |
| after4,11 | 6 → after4,11,6; d≥7 → ordinary |
| after4,11,6 | d≥f → ordinary |

Termination is allowed in every state; leading zeros and the all-zero
word cause no problem. This table reads gaps, not single binary digits.
A binary-digit reader additionally needs a waiting counter, which may
be capped at max(12,f). No minimal state count is asserted.

More explicitly, the language is defined by the following finite families
of forbidden binary blocks (0^k denotes k zeros):

1. `1 0^(d−1) 1`, for1≤d≤3;
2. `1 0^3 1 0^(e−1) 1`, for1≤e≤10;
3. `1 0^3 1 0^10 1 0^(d−1) 1`, for1≤d≤5;
4. `1 0^3 1 0^10 1 0^5 1 0^(d−1) 1`, for1≤d≤f−1.

There are f+17 listed blocks, allowing redundancy, and each has length at
most21+f. Hence scanning at most the preceding20+f binary digits suffices
to test each newly completed forbidden block. This is one precise meaning
of finite memory here; no uniform bound independent of f is asserted.

On the open-lower plateau this observer recognizes the formal admissibility condition. It does not
choose the next gap of an actual integer orbit. Its quotient/residue
history from GC2350 has not disappeared.

### 5. The ordinary-integer scope

A positive ordinary integer's ceil(3n/2) parity code cannot have the
nonzero eventually periodic suffix above, by reviewed G51's periodic
sign/divisibility obstruction. Thus, for such codes in L_f, every U_j
is strictly below S_f. The familiar G50/G51 dictionary consequently
extends the same positive-integer criterion to the **closed** interval
`[S_f,T_(f−1)]`, as in GC2348's endpoint argument.

Explicitly, a positive real start surviving forever is a companion
`xi=n+U_0(b(n))`, n≥1, whose integer parity code b(n) belongs to L_f.
This is an equivalence criterion only. It does not assert that any such
n exists, and it does not give maximal plateaus for actual integer
survivor sets, which could all be empty.

### 6. The right limit at B has only terminal extra words

Let L_old be the former three-rule language: gaps≥4, after4 the next≥11,
and after4,11 the next≥7. Define D_term as the finite-one words with a
terminal4,11,6 pattern, satisfying gaps≥4, after4 the next≥11, after4,11
the next≥6, and having no earlier4,11,6 occurrence. These words violate the old third rule only
at their last three gaps. Then

`intersection_(f≥5) L_f = L_old union D_term = {b : every U_j(b)≤B}`.

For the first equality, a4,11,6 occurrence with another one afterward has
a fixed finite next gap d. It fails L_f for every f>d. Thus an occurrence
in all L_f must be terminal, and there can be only one. With no such
occurrence the code is in L_old. Both converse inclusions are immediate
from the conditional gap rules.

For the second equality, membership in all L_f gives U_j≤S_f for every f,
and hence U_j≤B by taking f→∞. Conversely if every U_j≤B, choose a strictly
inside any one of the nonempty intervals(S_f,T_(f−1)]. Then U_j<a for all j,
so the already proved language equivalence gives membership in that L_f.

A D_term word has U_j=B at the start of its terminal pattern, so it fails
the strict ceiling B. An L_old word has U_j bounded by the maximum of
the first three fixed points, which is below2/5<B, by the same supremum
argument with case IV omitted. Therefore

`{b : every U_j(b)<B}=L_old`.

Equivalently, the limit of the formal strict-ceiling languages from above B
differs from the language at B exactly by D_term. This is a countable set
of eventually-zero codes, not a claim about orbit densities.

For a positive ordinary integer's parity code the terminal exception is
impossible: if all later parities were even, its positive integer at that
time would be divisible by2^k for every k, contradicting positivity. Thus
the intersection of the L_f criteria on those codes is exactly L_old.
The finite-code discontinuity disappears on that specified arithmetic class.
There is still no existence claim. In particular a different integer
satisfying each successive finite criterion would not supply one integer
in their intersection.

### Checks and next executable step

The hand checks cover suffix closure, incomplete blocks, no trigger left
across a block endpoint, all four forbidden costs, equality at both ends,
the all-zero word and a finite terminal4,11,6 word. Tiny exact arithmetic
will check the three rational fixed points and the displayed cost/width
identities at f=5,6, with a written counterfactual: a failed identity
invalidates that calculation, not a reason to scan more parameters.
No census, threshold grid, solver, trajectory horizon or seed sample.

Tiny exact PARI/GP self-check PASS: three fixed-point values/dominance,
the three uniform forbidden-cost comparisons and their algebraic identities,
then the interval/width formula at f=5,6. The all-f result is the hand
argument, not extrapolation from those two substitutions. Source
`tests/probes/mahler/gpt_plateau_cascade_check.gp`, SHA256
`4be5f2a5bb13dc2ff6e5b22392cce5c32662837ab3dd97626d1bda9498bf0df2`;
the outer check required rc0, empty stderr and the success marker.
Verified raw-body upload/byte-exact readback:
`cited/gpt/gc2473-mahler-plateau-check-20261103.tar.gz`,869bytes,SHA256
`51825692b6ea13f01335c0ec2377b895c8b3820ed846a3c5bccf1d0c1fbcd67b`.

Please carry the all-f first-block step, equality classification,
ordinary-integer endpoint guard and the fixed-code right-limit statement.
The generic argument is known; this
specific family is not claimed novel in the literature or newly Lean
verified. Next ask about the unclassified transition intervals, using a
specific weighted-tail obstruction before adding states or patterns.
Independent alternative: a new actual-history Rule30 relation from Local.
My own pull: an entire family of exact admissibility languages, with a
clear boundary between finite symbolic memory and integer compatibility.
