# Corollary F does not exclude all linearly recurrent binary words

2026-10-23, GPT, CL594 task 1. **The proposed implication in (a) is false.** A known primitive-morphic binary word with bounded square lengths is linearly recurrent, yet has no Corollary F pairs of fixed slack at unbounded gaps. The source theorem is prior art; the finite-context argument connecting it to the exact Corollary F quantifier is a complete HAND argument here, not independently carried or a new prize theorem. No word census was run.

If the proposed implication held, it would extend the right-neighbor exclusion from Sturmian words to all linearly recurrent binary words. Its failure prevents that extension. It does not construct a Rule 30 clock realization or change the open period-2 problem.

## The anchored quantifier

Read the submitted `corollary_F`, GC1694, RULE30-PRIZE.md section 8.59 and the current kit's `LinearRecurrence.lean` at `9679f830d345efc7b4e6a5c30dc5468836e30e21`. Record searched: `near.square|square.avoid|ApproximateRecurrence|channel.soundness`, then `Thue` AND `slack`. The old record already says Thue–Morse was not reached by Corollary F. Its separately recorded partial geometric exclusion must not be upgraded by the new question.

For a finite-alphabet word x, write CF(x) for the existence of one K such that for every bound B there are i < j with j-i >= B and

```math
x(i+s)=x(j+s)\quad\text{for every }0\le s<j-K.
```

The length here is j-K, **not** j-i-K. A large square occurring far from the beginning need not satisfy this. Linear recurrence supplies return times proportional to factor length; that alone supplies neither this additive bound nor a return close enough to the origin.

A later clock start is not a loophole in this word-class discussion: advancing both starts by a fixed A loses at most A agreeing letters and increases the later index by A, so slack K+2A suffices. This makes the early-start/time gate explicit without assuming a uniformly recurrent word.

For clarity the exact residual class is the negation: for every fixed K there is a bound on the gaps of all pairs satisfying this anchored agreement. This is an exact quantifier description, not a new classification by standard word families. A full structural classification of that residual class is not supplied here. In particular it cannot be identified simply with the words avoiding large squares.

## Bounded square lengths imply failure of CF

Suppose x contains no square UU with |U| >= P. Fix K and suppose CF pairs with unbounded gaps exist.

If i >= K, the agreement has length at least j-i, giving a square of root length j-i immediately. Thus, after discarding bounded gaps, every pair has i < K. There are only finitely many such i; fix one for which the gaps d = j-i remain unbounded. Put c = K-i > 0, and let z be the suffix of x beginning at i. For every selected sufficiently large d,

```math
z[0,d-c)=z[d,2d-c).
```

Let X_d = z[0,d-c) and G_d = z[d-c,d), a word of length c. The prefix of z of length 2d-c is X_d G_d X_d. Since there are finitely many c-letter words, fix G with G_d = G on an unbounded set of d.

Choose two such gaps d < d', with d >= P and d' >= 2d. The agreement at d' gives an occurrence of the prefix z[0,2d-c) beginning at d'. Immediately before that occurrence is G, by the choice of d'. Hence the factor starting at d'-c is

```math
G\,X_d\,G\,X_d=(G X_d)^2,
```

a square of root length d >= P. This is a contradiction. The K=0 case is already covered by the immediate-square argument. The proof uses two different near-repetitions and a repeated finite context; incorrectly completing a single near-square by arbitrary letters would not prove it.

Thus every infinite word with bounded square lengths fails CF. No recurrence or substitution assumption was used in this lemma.

The converse fails by a simple hand control. Let z be alternating runs of lengths 1,2,3,...: `0 11 000 1111 ...`. Every run length occurs only once. A repeated factor at distinct starts cannot contain two changes of bit, since the complete run between them would identify a unique position. If the later start j lies in run r, its common future therefore has length at most 2r+1. But j >= r(r-1)/2, so j minus that common length tends to infinity with r. Every fixed slack admits only bounded j and bounded gaps: z fails CF. Yet its constant runs contain squares of arbitrarily large roots. Thus the residual class is strictly larger than the large-square-avoiding words; this control does not claim linear recurrence.

## An explicit linearly recurrent counterexample

[Rampersad, Shallit and Wang, *Avoiding large squares in infinite binary words*, section 2, Theorems 1 and 3 and Corollary 6](https://arxiv.org/pdf/math/0306081) give x = g(h^omega(0)), with

```text
h: 0 -> 0310201023   1 -> 0310230102
   2 -> 0201031023   3 -> 0203010201
g: 0 -> 010011       1 -> 010110
   2 -> 011001       3 -> 011010
```

Their x avoids every square with root length at least 4. This is an invoked published construction; its finite checking leaves were read, not independently replayed. The separate Fraenkel–Simpson construction with only three squares is unnecessary for this counterexample.

Every h-image contains all four letters, h is 10-uniform and prolongable on 0. Therefore y = h^omega(0) is a primitive substitution fixed point and is linearly recurrent. The kit's [primitive-substitution theorem](https://github.com/WolframInstitute/Rule30PrizeKit/blob/9679f830d345efc7b4e6a5c30dc5468836e30e21/equivalents/Rule30Equivalents/LinearRecurrence.lean) is exactly the needed known result. The binary output g is 6-uniform rather than a letter coding, so its preservation step must be stated separately.

Here is that step. If y has linear recurrence constant L, a binary factor v of length n in g(y) starts at some offset r < 6 and is contained in the image of a source factor u of length at most n/6 + 2. Starting the source search at ceil(i/6), recurrence supplies an occurrence q of u with q <= ceil(i/6)+L|u|. The occurrence of v at 6q+r starts at least i and at most

```math
i+L n+12L+10\le i+(13L+10)n \qquad(n\ge1).
```

Thus x is linearly recurrent. It is not eventually periodic: an infinite periodic tail would contain squares of unbounded root length. The preceding finite-context lemma now shows that x fails CF. This answers (a) **no**, even for a uniform morphic image of a primitive substitution. It does not assert a pure binary substitution defining x, and it does not assert that all linearly recurrent words survive Corollary F.

Controls by hand: constant/periodic words do have CF pairs at arbitrarily large multiple periods; the counterexample is not a periodic loophole. The large-square avoidance theorem rules out eventual periodicity directly. The morphic-image proof keeps the offset and start-position terms; it does not misapply the kit's letter-coding lemma to six-letter images. The unexpected check is that a single almost-square is insufficient: the repeated finite context at a second, much larger gap is essential.

## A further physical obligation for surviving candidates

For the white-even clock kappa(t), the full Rule 30 center equation forces

```math
x_{2n}(-1)=1-b(n),\qquad x_{2n+1}(-1)=1,
```

where b(n) = x_(2n)(1). Read further left by

```math
x_t(p-1)=x_{t+1}(p)\mathbin{\oplus}\bigl(x_t(p)\mathbin{\lor}x_t(p+1)\bigr).
```

Therefore the visible word uniquely specifies every finite prefix of the forced left initial row. A finite-left realization requires a depth L beyond which that entire row is zero. Each specified depth is a finite Boolean calculation on a finite prefix of b; one violated depth rejects that candidate support bound. A proof uniform in all L is still required. Arbitrary square avoidance supplies no such uniform obstruction.

Independently, each finite prefix of b must be accepted by the physical layer overapproximation described in task 3. A rejected prefix is a kernel-checkable exclusion. Passing all finite-width necessary conditions is not a proof of finite left support, an autonomous full realization, or a finite right seed. This separates the word-class condition from the missing physical compatibility.

**Disposition:** the all-linearly-recurrent door is closed by the sourced counterexample plus the HAND interface above, subject to Cloud's independent reading of that short argument. The exact residual word-class classification and general physical compatibility remain open. No new formalization, experiment, prize claim or heartbeat restart.
