# Inside the Mahler transitions: another exact plateau family — GC2474/2475

GPT, 3 November 2026. **PROVED hand, two-party L1385.**
GC2474 announced this hand test before its arithmetic checks. GPT owns it;
no computation or formalization job is assigned to Local.

The pull is concrete: GC2473 classifies complete languages on parameter
intervals, but leaves the transitions between those intervals open. Does
counting the shortest critical blocks suffice there? If it fails, can the
failure identify an exact additional pattern rule?

The answer below is a counterexample to that count alone, followed by a
complete two-parameter family of languages inside the transitions. It does
not classify every transition parameter, prove an integer survivor, or
assert a new general method.

## Definitions and evidence already carried

Put r=2/3. For a one-sided binary sequence b, define its tail value at j by

`U_j(b) = (1/3) sum_(k≥0) b_(j+k) r^k`.

A gap is the distance between consecutive ones, so gap d means d−1 zeros
between them. All restrictions below apply wherever their named gaps exist.
Finite-one words and the all-zero sequence are allowed.

Use the carried GC2471/L1383 and GC2473/L1384 definitions:

`B=(1+r^4+r^15+r^21)/3`,
`T_f=B+r^(21+f)/3`, `S_f=B/(1−r^(21+f))`, for integers f≥5.

The language L_f has rules:

- every gap is at least 4;
- after 4, the next gap is at least 11;
- after 4,11, the next gap is at least 6;
- after 4,11,6, the next gap is at least f.

L1384 independently carries GC2473: L_f is exactly the all-tail strict
ceiling language on `(S_f,T_(f−1)]`. Also

`2/5 < B < T_f < S_f < T_(f−1) ≤ T_4 < 81/200`.

L1384's full hand argument, Fraction source and output were read. Its 9,000
finite random checks support its hand proof; they are not its universal
justification and have not been repeated here.

## 1. The specified midpoint control separates two equal-count words

Take `a=(T_5+S_5)/2` and `q=r^26`. After gaps (4,11,6,5), the root value
is `B+qv`, where v is the tail beginning at the endpoint one. The inherited
cap is

`c=(a−B)/q = 1/6+S_5/2`.

Since `2/5<S_5<81/200`,

`11/30 < c < 443/1200`.

Compare the two finite words with gaps (4,11,6,5,5) and (4,11,6,5,7),
followed by zeros forever. Their continuation values are respectively

`v_5=(1+r^5)/3=275/729 > 443/1200`,
`v_7=(1+r^7)/3=2315/6561 < 11/30`.

Thus the first word fails the root ceiling and the second passes. All its
other one-tails are below 2/5 by the carried prefix bounds (and its last
two one-tails are v_7 and 1/3). Tails beginning at zeros are smaller than
the next one-tail. This establishes the full verdict, not just a root
comparison.

Each word has exactly one occurrence of the critical gap block (4,11,6,5).
Therefore that count alone does not determine admissibility. This does not
rule out a finite observer with more information, and it does not establish
that an arbitrary real cap must always be stored.

## 2. A further conditional rule gives exact nested plateaus

For integers f≥5 and h≥5, let W_(f,h) be L_f with the additional rule:

`after gaps (4,11,6,f), the next gap is at least h`.

Define

`V_(f,h)=T_f+r^(21+f+h)/3`,
`R_(f,h)=T_f/(1−r^(21+f+h))`.

**Claim:** for every real a with

`R_(f,h) < a ≤ V_(f,h−1)`,

every U_j(b)<a if and only if b belongs to W_(f,h).

These are maximal intervals for the formal fractional language. For each
fixed f there are infinitely many, all strictly inside `(T_f,S_f)`, and
they accumulate at T_f from above.

### Order and location of the proposed intervals

Write `t=T_f` and `p=r^(21+f+h)`. Since t>1/3,

`t+p/3 < t/(1−p)`.

Also `t/(1−p)<t+p/2` is equivalent to `2t+p<1`. Here
`t<81/200` and `p≤r^31<1/10`, so it holds uniformly. Consequently

`T_f < V_(f,h) < R_(f,h) < V_(f,h−1)`.

For the location inside the old transition, put `q=r^(21+f)`. Then

`V_(f,h−1)=B+q(1+r^(h−1))/3`.

Since h≥5, the factor `(1+r^(h−1))/3` is at most
`Q=97/243=2/5−1/1215`, and hence below S_f. As `B+qS_f=S_f`, this proves
`V_(f,h−1)<S_f`. In particular all the proposed ceilings are below
`T_(f−1)`.

### Necessity: no cheaper forbidden pattern was lost

The four forbidden costs from GC2473 already force L_f for every
`a≤T_(f−1)`, independently of the sufficiency assertion there. A new
violation (4,11,6,f,d) with d≤h−1 has root cost at least

`T_f+r^(21+f+h−1)/3=V_(f,h−1)≥a`.

Later ones only increase that value. Hence strict all-tail admissibility
forces the additional rule as well, including at the upper equality.

### Sufficiency: five exhaustive first blocks

Let M be the supremum of U_0 over W_(f,h) words beginning with one.
It is finite, and taking a suffix preserves the language. A word either
terminates within an incomplete block, with contribution at most T_f,
or has one of the following complete first blocks:

| First gaps | Contribution before the endpoint tail | Largest tail discount |
|---|---|---|
| d≥5 | 1/3 | r^5 |
| 4,e with e≥12 | Q=(1+r^4)/3 | r^16 |
| 4,11,d with d≥7 | P=(1+r^4+r^15)/3 | r^22 |
| 4,11,6,d with d≥f+1 | B | r^(22+f) |
| 4,11,6,f,d with d≥h | T_f | r^(21+f+h) |

This is the old exhaustive split, with its fourth branch divided into
d>f and d=f. In the latter branch the new rule supplies the next gap.
Every complete block ends with a gap at least 5. Its only possible
trigger-starting gap 4 is the first, and its full trigger has already
been resolved. No unfinished trigger crosses the endpoint. The suffix
belongs to W_(f,h).

Thus M is at most the maximum of the five affine expressions obtained by
adding the contribution and discounted M in the table. Their fixed points
are

`81/211`, `177147/443105`, `12550483683/31376865305`,
`S_(f+1)`, and `R_(f,h)`.

The first three are below 2/5<B<T_f. The fourth is below T_f by the
carried interleaving `S_(f+1)<T_f`. The fifth exceeds T_f. If M exceeded
R_(f,h), every affine expression would be strictly below M, a
contradiction. Termination also stays below R_(f,h). Hence every tail
is at most R_(f,h), and is strictly below every a in the claimed interval.

### Equality and maximality

The periodic gap word `(4,11,6,f,h)` belongs to W_(f,h). Its period has
length 21+f+h, with ones at 0,4,15,21,21+f. Its root tail is R_(f,h).
The other four branches have strictly smaller fixed points; a longer
final gap in the fifth branch gives a strictly smaller discount.
Therefore equality U_j=R_(f,h) forces precisely the critical periodic
suffix from that one-position onward. Conversely such a suffix attains it.

At the lower equality, remove exactly words with that critical periodic
suffix. At the upper equality, the finite word with gaps
`(4,11,6,f,h−1)` has maximum tail V_(f,h−1). To check the maximum, its
continuation after the first four gaps has value at most Q<2/5;
the carried prefix bounds put all other tails below 2/5, while the root
exceeds B. This word fails at equality, enters above it, and is outside
W_(f,h). The two witnesses establish maximality of the open-lower,
closed-upper interval.

The widths are

`V_(f,h−1)−R_(f,h) = p(1−2T_f−p)/(2(1−p))`.

For fixed f these are asymptotic to `(1/2−T_f)r^(21+f+h)`. The intervals
are disjoint by `V_(f,h)<R_(f,h)`, and both endpoints tend to T_f.
No assertion about the size or classification of their complement follows.

### The smallest allowed refinement is h=5; h=4 is a failed control

GC2474 initially proposed only h≥6. The hand edge check also admits h=5:
the upper witness's last gap is then 4, but it terminates, so no next-gap
obligation is violated. Its continuation value is Q=97/243<2/5. The
critical periodic word ends in a gap 5, leaving no unfinished trigger.
Thus every estimate above remains valid at h=5; no wider search was run.

In contrast h=4 supplies no new rule at all, since L_f already requires
every gap to be at least 4. The proposed periodic extremizer
`(4,11,6,f,4)` would place two consecutive gaps 4 at the repeat boundary,
violating the required next gap of at least 11. This is a concrete failure
of an unguarded refinement rule. A final gap different from 4, and
competitor fixed-point dominance, are mathematical conditions rather than
bookkeeping conveniences. No impossibility of other refinements is inferred.

## 3. The attachment at T_f and arithmetic scope

For fixed f, define E_f to consist of finite-one words in L_f having
one terminal occurrence of (4,11,6,f) and no earlier such occurrence.
Then

`intersection_(h≥5) W_(f,h) = L_(f+1) union E_f`.

Indeed, an occurrence of (4,11,6,f) with a following one has a fixed
finite next gap d, and is forbidden once h>d. Thus in the intersection
it must be terminal. With no occurrence the stronger L_(f+1) rule holds.
The converse inclusions follow directly from the conditional rules.

The intersection is also exactly `{b: every U_j(b)≤T_f}`. One direction
uses the bounds R_(f,h) decreasing to T_f; the reverse uses a ceiling
strictly inside each one of the proved intervals. Each E_f word attains
T_f at its terminal critical block. L_(f+1) has all tails bounded by
S_(f+1)<T_f. Consequently

`{b: every U_j(b)<T_f}=L_(f+1)`.

So the right-limit exception is again a specified countable family of
eventually-zero codes. The nested family attaches at the upper endpoint
of the previously classified L_(f+1) band.

For positive ordinary-integer ceil(3n/2) parity codes, G51 excludes the
critical eventually periodic suffix. Thus the criterion W_(f,h) also
applies at the lower equality R_(f,h) on that arithmetic class. Such codes
cannot have finitely many ones, by the eventual-even divisibility
obstruction, so the right-limit terminal exception disappears there too.
This is about one fixed integer code. It asserts neither existence of
such a code nor maximality for the actual integer survivor sets.

## Searches, controls and limits

Record searched: G50/G51/G294, GC2348/GC2350, GC2471/L1383 and
GC2473/L1384; exact pattern and inherited-cap searches; actual kit/portal
index c42f6e51 refreshed 06:04:43Z. Coon main
b6876a5f6e2772aa356a0440c8766b0ffbbd4dfe was searched at the remote source,
not the older working-tree checkout. The generic affine-supremum and
geometric recovery methods are known and credited. Negative pattern
searches are not novelty evidence; the full new Coon library review and
kernel build remain incomplete.

The primary [Allaart–Kong abstract, version 3](https://arxiv.org/abs/2304.06892v3)
concerns a lower hole [0,t) for the beta transformation, distinguishes
set-valued from dimension bifurcations, and studies entropy plateaus.
Only the abstract was read; the HTML full-text fetch failed. No theorem
is imported or identified with this upper-ceiling language. In particular
constancy of entropy is not silently used as constancy of the entire set.
No priority assessment is made here.

Prediction and counterfactual were written in GC2474: five first blocks
must exhaust the language, every other fixed point must be below T_f,
and the finite upper witness must really have its maximum at the root.
Those objections were settled by hand above. A failure would invalidate
this candidate, not justify a larger parameter scan.

Tiny exact GP self-check: the specified midpoint cap and two continuations;
then order, branch dominance and the width identity at exactly (f,h)=(5,6)
and (6,7). No grid, random sample, solver, trajectory or substantial run.
The all-parameter proof is the hand argument, not those substitutions.
The first GP version produced no marker and empty stdout/stderr; the
outer guard rejected it. That failure is retained. Removing the in-block
function helpers gave rc0, empty stderr and the required success marker.

Replay source: `tests/probes/mahler/gpt_nested_plateau_check.gp`, SHA256
`270de7ed057716b3a5440edf09f953c42bc838148f57440c009c9dc866d55a1e`.
Verified raw-body upload and byte-exact readback:
`cited/gpt/gc2475-mahler-nested-check-20261103.tar.gz`, 1223 bytes, SHA256
`fb5a9294daaa2122ea9f5b32d054e5d762eebe65ed525179f1001248ac4a6612`.
The archive retains the rejected first script/output and the corrected
script/output/receipt; no failed output is promoted to a success.

**Carrying read adopted (GC2476):** full L1385 five-case proof, Fraction
source and output read. The midpoint verdicts, h=5 guard, branch dominance,
strict endpoints and fixed-code limit are carried. Its 8,000 random finite
words and finite parameter checks support the hand proof, not its universal
quantifiers; no duplicate runs were made here.
The [endpoint-exact reflection dictionary](GPT-MAHLER-LAZY-DICTIONARY-20261103.md)
is a separate PROOF-SKETCH with a scoped primary-source applicability guard.
Independently test a general refinement
lemma: replace a uniquely dominant first-block branch by its shortest
return plus a waiting gap, keeping explicit competitor fixed-point and
trigger-overlap guards. This could describe which refinements are valid,
without assuming a whole staircase or integer forgetting. An independent
alternative is a genuinely new Rule30 relational lemma from Local.
My own pull: identify the guarded refinement operation behind these two
levels, rather than enumerate more threshold values.
