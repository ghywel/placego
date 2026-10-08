# the offset budget and the eight-bit prefix

*GPT's proofs, second-read. Derived from [PROOFS.md](../PROOFS.md), entry "G.GPT87. the offset budget and the
eight-bit prefix (second-read by Local, 2026-10-06)"; rebuild with `python3 proofs/build.py`. Edit the proof in
PROOFS.md and this summary in [summaries.md](summaries.md), never this file.*

**Status:** proved by GPT and second-read by Local.

## In plain words

A budget argument forces three more steps, pinning down the first eight steps of any meeting pair at 21.

**What it says.** At the sixth step there were two possibilities. One would leave the two numbers too little room in
their possible offsets to meet, so it is ruled out, and the growth-factor rule then forces the next two. The
patterns must begin 11011011 and 11111111 (1 meaning odd), so the starts leave remainders 251 and 255 when divided
by 256.

**Why it matters.** The candidates shrink by proof alone, and the method, comparing the most and least each option
could contribute, becomes the next page's certificate.

**An everyday picture.** Planning a trip on a fixed budget: if one route already costs more than the rest of the
trip could ever save, cross it off.

## The formal statement and proof

### G87. The offset budget rules out one sixth-bit branch (2026-10-06)

Continue G84-G85 at odd count a = 21. After five steps the states obey w' = 3*w + 29 and therefore have opposite parity. The branch with lower bit 1 and upper bit 0 would give prefixes 110111 and 111110. For a >= 5 their attained extrema are

    max B_110111 = B_max - 32*3^(a-5),
    min B_111110 = 3^a + 32*3^(a-5) - 2^(a+1).

The first replaces G67's fifth odd position 6 by 5; later latest positions are unchanged. The second delays the earliest odd positions after the initial five ones by one place, if any remain. Both extremal words satisfy admission. Their normalized positive gap is consequently

    max (B_110111-B_111110)/3^a = R_a - 64/243 + (2/3)^a.

At a = 21 its numerator over 3^21 is 40809080460, less than 4*3^21 = 41841412812. G84 requires the positive offset gap to equal 4*3^21, so this branch is impossible for a collision. The sixth bits must instead be 0/1.

After that branch the states satisfy x' = 9*x + 44. Admission of the lower branch forces an odd seventh bit, since its four odd steps would otherwise give 81 < 128. Both states have the same parity, so both take an odd step and satisfy y' = 9*y + 62. The lower branch needs another odd bit at step eight, since 243 < 256, again forcing both; then z' = 9*z + 89. Thus every a = 21 candidate must begin 11011011/11111111, with starts 251/255 modulo 256. The ninth bits are opposite. No meeting pair has been found, and no a = 21 word search is registered.

**Unexpected minimum-offset correction guard.** At a = 5 the extremal words 1101110 and 1111100 have offsets 287 and 211. Their gap is 76/243. Omitting the positive (2/3)^a correction from the normalized formula would give only 44/243 and falsely exclude this valid gap. The correction is small at a = 21, but cannot be discarded from a uniform bound.

**Next controls, preregistered NOT RUN.** PB1: reuse existing a = 5 to 12 admitted words to check both attained sixth-prefix extrema and their gap formula. PB2: exact a = 21 integer comparison and direct first-eight-step controls on starts 251/255, including the three affine relations and opposite ninth parity; do not claim they meet. Require the formulas and necessary bound to hold. Counterfactual dropping the correction must fail on the a = 5 guard. No extended collision enumeration or Local job duplication. Independent reading requested; elementary recorded offset extrema.

### G87 prefix-budget controls outcome (2026-10-06)

PB1 passes eight attained sixth-prefix extrema pairs on 4396 existing words. PB2 verifies the exact a = 21 budget and eight-step affine guards; the omitted-correction counterfactual is refuted.
