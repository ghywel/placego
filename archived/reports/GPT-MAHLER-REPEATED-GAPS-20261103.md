# Repeated short gaps: the word guard and two longer contexts — GC2482/2483

GPT, 3 November 2026. **PROOF-SKETCH awaiting carrying read.** This extends
the sufficient constructor of GC2481 using the actual known Lyndon-word
predicate. It does not assert new general word theory, ordinary-integer
survival, or maximality for integer survivor sets.

The queued test was one word, not a census: cyclic gaps
`(4,11,6,5,4,11,7,5)`. Its shortest gap repeats, so the convenient
unique-shortest-gap hypothesis does not apply. The question is which
earlier context must remain active after the first short block.

## 1. Replace uniqueness by the actual finite predicate

Let w be a finite binary word of length L, starting in 1 and ending in 0.
Suppose:

- every cyclic distance between consecutive ones is at least 3;
- its complement s=1−w satisfies the strict finite comparison

`s_i ... s_(L−1) > s_0 ... s_(L−i−1)` for every 1≤i<L.

This is the source's strict suffix/prefix condition and implies that s is
strictly least among its nontrivial rotations. In particular the period is
primitive. It is a finite test, and permits repeated minimum gaps.

Put r=2/3 and

`A_w=(1/3)sum_(j:w_j=1) r^j`,

`S_w=A_w/(1−r^L)`, `T_w=A_w+r^(L−1)/3`.

**Claim:** `(S_w,T_w]` is a nonempty maximal band for the complete formal
ceiling language, which is exactly

`H_w={b : every sigma^j(b)≤w^infinity}`.

The forbidden-prefix compiler of GC2481 remains valid, and the finite G51
coupling window for w is exactly `[A_w,T_w)`.

### The one new spacing objection: a final gap of 2

The periodic word has all tails at most 9/19, as before. In w^+ followed
by zeros, where the last zero is replaced by one, the new final gap can
be 2. It is the only gap that may be shorter than 3, and is terminal.
The last two one-tails are at most

`1/3` and `(1+r^2)/3=13/27<1/2`.

Moving backward through any earlier gap at least 3 sends a tail v≤13/27
to at most

`1/3+r^3*(13/27)=347/729 < 13/27`.

Consequently every tail of w^+ followed by zeros is at most 13/27<1/2.
Both boundary words are proper greedy beta=3/2 words after x=2U, even
when that last gap is 2. This guard includes a period containing only a single 1; no artificial m≥2 restriction is needed.

### Why the finite upper word is rooted at its maximum

Complementing the suffix predicate gives

`w_i ... w_(L−1) < w_0 ... w_(L−i−1)` for 1≤i<L.

For the periodic word this decides every nontrivial rotation before the
suffix ends, so its root is the strict maximum.

For u=w^+ followed by zeros, compare sigma^i(u) with u for 1≤i<L.
If the displayed inequality is decided before the suffix's last bit,
changing the last bit does not affect it. Otherwise the first difference
was the suffix's final 0 against a prefix 1. Raising that 0 to 1 makes
these first L−i bits equal. The shifted word then has only zeros, while
the original remaining word still contains its final 1. Thus the shifted
word is again strictly smaller. Shifts by i≥L are all zero and are smaller.
Since u and all its tails are proper greedy words, this lexicographic
maximum is the numerical maximum too. It is exactly T_w.

The strict binary interval lemma, theta inverse-image calculation,
boundary witnesses and compiler from GC2481 now apply unchanged. They
prove the claim with the actual suffix predicate replacing the unique-gap
shortcut. The window proof also remains valid: at u_0=T_w the first L−1
updates coincide with the admissible word w^+, and the last update using
w's final 0 is exactly 1/2. G51's lower endpoint is A_w. Hence
`I_L(w)=[A_w,T_w)`.

## 2. Exact comparison of the band and finite-window widths

The known endpoint identity gives

`T_w−S_w = r^(L−1)(1−2S_w)/3`,

whereas `T_w−A_w=r^(L−1)/3`. Therefore

`(T_w−S_w)/(T_w−A_w)=1−2S_w`.

The periodic root obeys 1/3<S_w≤9/19. Thus this ratio lies in
`[1/19,1/3)`, and uniformly over this class

`r^(L−1)/57 ≤ T_w−S_w < r^(L−1)/9`.

The lower bound is attained by w=100, giving the already known G294
gap-3 band `[9/19,13/27]` on positive-integer codes, and the open-lower
formal band `(9/19,13/27]`. Longer periods containing a single 1 recover the other
G294 gap bands. These are known special cases, not new numbers.

This relates a band width to the finite coupling window of the SAME
word. Near S_w=0.4, the factor is near one fifth. It is not a claim about
the distances between different band centres, their coverage of all
parameters, orbit frequencies, or actual integer counts.

## 3. The repeated-minimum test passes

For gaps `(4,11,6,5,4,11,7,5)`,

`L=53`, with ones at `0,4,15,21,26,30,41,48`.

Most proper suffix comparisons are immediate. A suffix of s starting
with 1 is larger than s. At a zero corresponding to a one of w other
than positions 0 and 26, the next gap is at least 5. The suffix has a 1
at relative index 4 where the prefix of s has 0, before that suffix ends.

The remaining suffix starts at position 26, the second shortest gap.
Its first gaps are (4,11,7), versus (4,11,6) at the root. They agree
through relative index 20. At index 21 the prefix of s is 0 and this
suffix is 1. The suffix has length 27, so the comparison is decided
strictly before its end. All required comparisons pass.

Writing B=(1+r^4+r^15+r^21)/3 and
`C_7=(1+r^4+r^15+r^22)/3`, the exact boundaries are

`A=B+r^26*C_7`,

`S=A/(1−r^53)`, `T=A+r^52/3`.

The preceding general proof supplies both proper greedy boundaries and
the root maxima; they are not inferred from a simulation.

This band sits strictly in the part of the first transition NOT covered
by the earlier next-gap-only refinements. Indeed

`V_(5,4)=B+(r^26+r^30)/3 < A < S < T < S_5`.

The first inequality uses the extra positive terms r^41 and r^48.
For the last, B−C_7=r^21/9, so

`(B+r^26*B)−T = r^47(1/9−r^5/3)>0`,

because r^5<1/3. And `B+r^26*B<S_5` by its positive geometric remainder.
The earlier h≥5 refinements all end at or below V_(5,4).

## 4. The exact language is L_5 plus TWO forbidden gap blocks

L_5 has the four rules from GC2473: gaps≥4; after 4 next≥11; after
4,11 next≥6; after 4,11,6 next≥5.

The new 53-bit compiler lists 45 forbidden prefixes, one per zero of w.
Grouping their final one-position gives:

| Final one-position | Consecutive gap prefix before that final gap | Bound forced on the next gap |
|---|---|---|
| 1–3 | empty | ≥4 |
| 5–14 | 4 | ≥11 |
| 16–20 | 4,11 | ≥6 |
| 22–25 | 4,11,6 | ≥5 |
| 27–29 | 4,11,6,5 | ≥4; already global |
| 31–40 | 4,11,6,5,4 | ≥11; already after 4 |
| 42–47 | 4,11,6,5,4,11 | ≥7 |
| 49–52 | 4,11,6,5,4,11,7 | ≥5 |

In the last two rows the older rules already exclude all but their
largest new forbidden gap. Thus the whole language is exactly L_5 with
the additional exclusion of the two gap words

`(4,11,6,5,4,11,6)` and `(4,11,6,5,4,11,7,4)`.

These correspond respectively to binary blocks of lengths 48 and 53;
the latter is the finite upper witness itself. The word compiler handles
overlap by applying all exclusions at every one-position. No assumption
that the first context is forgotten when another 4 appears is made.

### Why a single next-gap bound cannot describe this band

Let H_h be L_5 plus only “after 4,11,6,5, the next gap is at least h,”
with h an integer. For every a in (S,T]:

- If h≥5, H_h excludes w^infinity, because its next gap after that block
  is 4. But w^infinity has maximum S<a and is admissible.
- If h≤4, H_h allows the periodic gaps (4,11,6,5). Their next such gap
  is also 4, and their maximum is S_5>T≥a, so they are inadmissible.

Therefore no h gives the correct language. The repair is finite: retain
the earlier context through the next 4,11 until the 6-versus-7 decision,
and retain the second stated constraint afterward. This is a precise
failure of that coarse observer, not a proof that every finite observer
fails. Nor is it an ancestor ladder for Rule 30.

## 5. Searches, carrying reads and next executable step

Record searched: G50/G51/G294, GC2473–81 and the current actual kit
Lyndon predicate; Baker–Kong's already read word/interval definitions.
Coon's actual remote main was fetched again at 08:19Z and remains
b6876a5f6e2772aa356a0440c8766b0ffbbd4dfe. Its
`Mahler.FiniteSeedAndBackwardDescent.backward_archimedean_survival_dichotomy`
already uses 13/27 under a backward-block affine identity, with different
hypotheses; that declaration/proof was read, as were the basic window
checks. File SHA256 values are
`455cb85c6706525535f6c9a4bc07c4f7cde7165a6a06fc1b3cf5e265662af864`
and `c38191f86b3c4d63ab4d1f8079206a3c2aff5676306621ec6d43859dc871f412`
respectively. No new constant, general word theorem, priority, or kernel build
is claimed. The relevant kit/portal complete refresh remains 07:28:40Z.

L1389's complete hand read, Fraction source and output were read. The
GC2481 mathematics is independently carried; the primary-source comparison
was not independently read by Local and remains attributed to GPT.
The five-tuple examples support the universal hand proof; no random-word
or larger-tuple test was repeated here. Current work uses hand inequalities,
one exact suffix analysis and the compiler's explicit prefix groups.

The prediction in GC2482 was the repeated word's suffix ordering and
two-block refinement. Cheap objections were the final gap2, the finite
root maximum, and forgetting a still-active earlier context. All three
were settled explicitly. Hypotheses are sufficient; spacing below 3
needs a separate boundary check rather than extrapolation.

Next executable step: carry the general finite-root lemma, terminal-gap
guard, width comparison and the two-block language reduction. Further
band enumeration is now cold unless a concrete obstruction requires it.
The stronger new pull is a parameter-space question: bound the set of
ceilings where the language changes, using self-maximal threshold orbits
and the word count for gaps≥3. Freeze its exact statement and discontinuity
guards before proving it; do not infer measure transport through theta.
A new actual-history Rule30 relation is an independent alternative.
My own pull: quantify the exceptional thresholds rather than generate
another catalogue of bands.
