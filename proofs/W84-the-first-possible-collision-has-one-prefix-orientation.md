# The first possible collision has one prefix orientation

*The waiting room (not yet verified). Derived from [PROOFS.md](../PROOFS.md), entry "G84. The first possible
collision has one prefix orientation (2026-10-06)"; rebuild with `python3 proofs/build.py`. Edit the proof in
PROOFS.md and this summary in [summaries.md](summaries.md), never this file.*

**Status:** in the waiting room: stated with a proof, not yet checked by a second reader.

## In plain words

At 21 odd steps, the first case G83 leaves open, any meeting of two surviving numbers would have to take one exact
form.

**What it says.** Sort the surviving step patterns by their first three steps: odd-odd-even or odd-odd-odd. GPT
showed that two patterns with the same first three steps cannot meet at a = 21, and that a meeting between the two
kinds is possible only if the offsets differ by exactly 4 times 3^21, so that the two starting numbers differ by
exactly 4. No such pair has been found.

**Why it matters.** It narrows any future search for a meeting at a = 21 to one precise shape, instead of all
patterns. It has not yet had its second reading.

**An everyday picture.** A detective who cannot yet name the culprit, but has proved it must be one of two twins who
arrived four minutes apart.

## The formal statement and proof

G83 leaves a21 as the first odd count not excluded by its exact spacing bound. Without enumerating those words, their first three bits sharply constrain any collision. This is a necessary condition, not existence.

For a>=3, split W_a into prefixes110 and111. Position extrema give

    min B_110=13*3^a/9-2^(a+1),
    max B_111=B_max-4*3^(a-3).

For the first formula, the earliest positions of a word110 are0,1,3,4,...,a. The initial two terms sum to5*3^(a-2); the remaining terms are twice the corresponding all-ones-prefix terms. This sums to the displayed minimum. These earliest positions satisfy admission. For the second, G67's latest positions begin0,1,3; imposing111 replaces only position3 by2, reducing the intercept by4*3^(a-3). The remaining latest positions are unaffected, and the resulting word is admitted. Both bounds are attained within their classes. Thus the signed opposite-prefix difference obeys

    (B_111-B_110)/3^a <= R_a-16/27+(2/3)^a.

At a21, the right-hand side is exactly37365342780/10460353203<4, while4<R_21<8. Equal-terminal words with the same first three bits would realize starts equal modulo8 (the parity-word bijection), hence have a nonzero displacement of magnitude at least8; the global span excludes this. Opposite-prefix words therefore are required. The signed bound excludes B_111>B_110 by4*3^21 or more. Every possible collision must consequently have

    B_110-B_111=4*3^21,
    n_111=n_110+4,
    n_110=3 modulo8, n_111=7 modulo8.

The two parity representatives modulo8 follow directly by evolving one odd start of each class for three steps. G81 realizes any code collision by actual positive starts; the necessity above holds for all realizing lifts. No candidate has been found, and no new a21 search is registered. The reduction narrows any future witness search rather than replaces the missing injectivity proof.

**Unexpected signed-direction guard.** At a3, W_110 consists of1101 with B23, and W_111 of1110 with B19. The reverse signed bound is-4/27, attained by(19-23)/27. It is not an absolute-difference bound: abs(19-23)/27=4/27. Replacing a directional bound by an absolute bound is the counterfactual refuted here. Also a2 has no111 class; the extrema formulas require a>=3.

**Next controls, preregistered NOT RUN.** PF1: reuse a3..12 admitted words to verify both attained prefix extrema and the signed inequality; independently check representatives3/7 modulo8 and the a3 direction guard. PF2: exact integer verification of a21's two interval bounds and signed numerator. Require the stated necessity bounds to hold; do not infer or search for a collision. Report any failure, and record this as a continuation of the existing residue-code lane, not a duplicate of Local's a17 enumeration. Elementary affine/position reasoning from G67/G81/G83, no imported theorem or novelty claim; independent review requested.
