# Sharp six-position reflection-free translation

*GPT's proofs, second-read. Derived from [PROOFS.md](../PROOFS.md), entry "G.GPT308. Sharp six-position
reflection-free translation (2026-10-16)"; rebuild with `python3 proofs/build.py`. Edit the proof in PROOFS.md and
this summary in [summaries.md](summaries.md), never this file.*

**Status:** proved by GPT and second-read by Local.

## In plain words

Any at most six distinct integer positions of span<=20 translate into0..27 without repeated
complementary-pair labels. A six-point span21 obstruction makes the bound sharp. PROVED CL422.

**Why it matters.** It separates literal position collisions from reflected-pair collisions in
the E28 construction; more active bins need a new geometry argument.

## The formal statement and proof

**Status: PROVED after Cloud's independent hand carrying read, CL422/fde83bd8.**
Source: GPT-MATH-INSTINCT.md MI087, first committed 1be3bc90; boundary controls MI088.
Every set of at most six distinct integer positions of span at most20 has a translate in
0..27 with pairwise distinct labels min(x,27-x). Span21 can fail. No novelty claim.
The carrying argument is copied verbatim below.

Normalize min S=0, span D. A translate r is blocked
only by an opposite-parity pair x,y with x+y=27-2r. If D<=18 there are at least ten
roots and at most nine cross-parity pairs. At D=19 there are nine roots; blocking all
would require three even and three odd points, with all nine sums distinct and equal
to 11,13,...,27. Endpoints are 0 and 19. The least odd point is then 11 and greatest
even point 8. But 0+19=8+11, a duplicate, contradiction. At D=20 there are eight roots,
requiring odd sums 13,15,...,27. Endpoints 0,20 are even. Each odd point contributes
at most one useful pair with the endpoints (it would need both y>=13 and y<=7 to
contribute two). With E even and O odd points, useful pairs <=(E-1)O<=6 when E+O<=6
and E>=2, short of eight. Thus a root exists. Fewer points satisfy the same bounds.
The span bound is sharp: S={0,2,6,15,19,21} blocks all seven roots through sums
15,17,19,21,23,25,27. Literal duplicates remain a separate failure.

**Review provenance.** Cloud independently checked the cross-parity count, both endpoint cases,
the forced duplicate at span19 and the complete sharpness fixture. No numerical premise is
needed for this theorem.


**Filing check.** proof_dupes hard checks pass. Nearest older entries G121, G178 and G307: read; Rule30 ancestry/quotient arguments and second-negative surgery do not restate this sharp packing bound.
