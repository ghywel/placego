# The first possible collision has one prefix orientation

*The waiting room (not yet verified). Derived from [PROOFS.md](../PROOFS.md), entry "G84. The first possible
collision has one prefix orientation (2026-10-06)"; rebuild with `python3 proofs/build.py`. Edit the proof in
PROOFS.md and this summary in [summaries.md](summaries.md), never this file.*

**Status:** in the waiting room: stated with a proof, not yet checked by a second reader.

## In plain words

At 21 odd steps, any meeting allowed by these conditions must have one precise orientation.

**What it says.** For two starts satisfying the prefix growth-factor condition and meeting with 21 odd steps each, the smaller starts odd-odd-even and the larger starts odd-odd-odd. The starts differ by exactly four. The reverse orientation is excluded by bounds on the two kinds of offsets. No meeting pair has been found.

**Why it matters.** It narrows the first count left open by W83 without another large search. These are necessary conditions, not an existence claim. Independent review remains pending.

**An everyday picture.** A detective narrows a possible pair to two adjacent seats with a specific left-to-right order, but has not found anyone occupying both.

## The formal statement and proof

G83 leaves a = 21 as the first odd count not excluded by its exact spacing bound. Without enumerating those words, their first three bits sharply constrain any collision. This is a necessary condition, not existence.

For a>=3, split W_a into prefixes110 and111. Position extrema give

    min B_110=13*3^a/9-2^(a+1),
    max B_111=B_max-4*3^(a-3).

For the first formula, the earliest positions of a word 110 are0,1,3,4,...,a. The initial two terms sum to5*3^(a-2); the remaining terms are twice the corresponding all-ones-prefix terms. This sums to the displayed minimum. These earliest positions satisfy admission. For the second, G67's latest positions begin0,1,3; imposing111 replaces only position3 by 2, reducing the intercept by 4*3^(a-3). The remaining latest positions are unaffected, and the resulting word is admitted. Both bounds are attained within their classes. Thus the signed opposite-prefix difference obeys

    (B_111-B_110)/3^a <= R_a-16/27+(2/3)^a.

At a = 21, the right-hand side is exactly37365342780/10460353203<4, while4<R_21<8. Equal-terminal words with the same first three bits would realize starts equal modulo 8 (the parity-word bijection), hence have a nonzero displacement of magnitude at least8; the global span excludes this. Opposite-prefix words therefore are required. The signed bound excludes B_111>B_110 by 4*3^21 or more. Every possible collision must consequently have

    B_110-B_111=4*3^21,
    n_111=n_110+4,
    n_110=3 modulo 8, n_111=7 modulo 8.

The two parity representatives modulo 8 follow directly by evolving one odd start of each class for three steps. G81 realizes any code collision by actual positive starts; the necessity above holds for all realizing lifts. No candidate has been found, and no new a = 21 search is registered. The reduction narrows any future witness search rather than replaces the missing injectivity proof.

**Unexpected signed-direction guard.** At a = 3, W_110 consists of1101 with B23, and W_111 of1110 with B19. The reverse signed bound is-4/27, attained by(19-23)/27. It is not an absolute-difference bound: abs(19-23)/27=4/27. Replacing a directional bound by an absolute bound is the counterfactual refuted here. Also a = 2 has no111 class; the extrema formulas require a>=3.

**Next controls, preregistered NOT RUN.** PF1: reuse a = 3 to 12 admitted words to verify both attained prefix extrema and the signed inequality; independently check representatives3/7 modulo 8 and the a = 3 direction guard. PF2: exact integer verification of a = 21's two interval bounds and signed numerator. Require the stated necessity bounds to hold; do not infer or search for a collision. Report any failure, and record this as a continuation of the existing residue-code lane, not a duplicate of Local's a = 17 enumeration. Elementary affine/position reasoning from G67/G81/G83, no imported theorem or novelty claim; independent review requested.


### G84 prefix controls outcome (2026-10-06)

PF1 passes 10 attained-prefix-extrema pairs on 4401 existing admitted words at a = 3 to 12. Representatives3/7 modulo 8 and the signed-direction counterfactual check. PF2 verifies exactly4<R_21<8 and the reverse-direction bound12455114260/3486784401<4 (the reduced form of the stated fraction). No control failed; no a = 21 word or actual-start search occurred. Probe: `tests/probes/prizes/collatz_gpt_prefix_orientation.py`; predictions at4c2e796, GPT Intel Python, under1 s. Necessity only, with independent proof review pending.
