# The ordinary fringe already meets the proposed middle-turnover floor

*GPT's proofs, second-read. Derived from [PROOFS.md](../PROOFS.md), entry "G.GPT290. The ordinary fringe already
meets the proposed middle-turnover floor (second-read by Local, 2026-10-13)"; rebuild with `python3
proofs/build.py`. Edit the proof in PROOFS.md and this summary in [summaries.md](summaries.md), never this file.*

**Status:** proved by GPT and second-read by Local.

## In plain words

The right side demands a minimum number of changes beside a white triangle, but the triangle's ordinary edge
supplies that many for free, so the count rules nothing out.

**What it says.** Suppose the wall, the middle column, blinks black and white, and take a run of white cells in the
starting row that begins eight or more cells left of the wall and has a black cell on its wall side; the run shrinks
into a white triangle. For each black beat, draw a diagonal from the triangle's edge to the wall. A change is a pair
of neighbouring white cells that appears or vanishes from one diagonal to the next. At the wall's white beats the
right side never shows two blacks or five whites in a row, so N consecutive diagonals (from the fifth onward, and
only while the run reaches far enough) hold at least (2N − 6)/5 changes away from their ends. But the triangle's
black edge alone, whose settled pattern is already known, puts a change at the first counted spot of every diagonal
or of every other one, depending on the band's phase, missing at most the first two: always enough.

**Why it matters.** It closes one hoped-for way to cap how long such white runs can be: treating the count of these
changes as a toll that impossible left halves might fail to pay. The triangle's ordinary edge pays it automatically,
so the count cannot tell real left halves from impossible ones. Other routes stay open, such as where the changes
fall, tied to the actual starting row, and nothing here settles whether the middle column can blink for ever.

**An everyday picture.** A rain gauge left under a dripping garden tap: the drip alone fills it past the least a
rainy day would leave, so the gauge can never show that a day was dry. The pattern of wet patches on the patio might
still tell; the level in the gauge cannot.

## The formal statement and proof

**PROVED, Local L691 at3ae23c02.** Source: RULE30-GPT.md GC1206. For its d>=8 black-ended zero band and N consecutive eligible charge paths a>=4, the real middle parity is1 on visible triples001/010. Removing the outer source prefix and wall depths1..5 gives a distinct middle-turnover count C>=max(0,ceil((2N-6)/5)); the five-state finite potential is explicit in GC1206.

The count is a nondiscriminator for relaxed left models. In the established moving fringe, Z5=Z6=Z3 after7 and Z7=0 after10 (GC634). At path position u3, for a>=6, the source is the alternating Z3 phase for e0 and1 for e1. This middle position alone supplies at least floor(max(N-2,0)/2) events, exceeding the proposed lower bound without a real visible-language constraint. Locality compares each quad, whose deepest original input is k+2<E, to the zero-tail reference; the actual whole fringe need not survive finite-band collapse. GC1206 gives all endpoints, source subtraction and registered controls. This closes the count-only pricing proposal, not the full origin-dependent source representation or all finite-type routes. L691 checks the potential, middle parity, cone and u3 comparison by hand; the cited fringe and inverse-column identities remain their established inputs.
