# A certified cut charges the first zero beyond the depth125 witness

*GPT's proofs, second-read. Derived from [PROOFS.md](../PROOFS.md), entry "G.GPT285. A certified cut charges the
first zero beyond the depth125 witness (second-read by Local, 2026-10-13)"; rebuild with `python3 proofs/build.py`.
Edit the proof in PROOFS.md and this summary in [summaries.md](summaries.md), never this file.*

**Status:** proved by GPT and second-read by Local.

## In plain words

The longest known white run starting 125 squares left of the middle has 21 squares; with the 124 squares before it
unchanged, no run there can reach 22.

**What it says.** Hold the middle column to blink black, white, black, white, starting on black. The blink breaks
unless, at each black beat, the square on its left is black and, at each white beat, the squares either side of it
differ in colour. The record counts a white run in the starting row only if some right half keeps this up until news
from the run's far end reaches the middle, and its best example from depth 125 (125 squares left of the middle) has
21 squares. Keep that example's first 124 squares and extend its white run to depth 146: the colours then demanded
on the right at the 38 white beats from tick 71 to tick 145 (the new square sets the last) form a pattern that a
checked computer proof shows no right half can ever produce. Squares farther out cannot help, since news from them
travels at most one square per tick and arrives too late.

**Why it matters.** A start with finitely many black squares whose middle settled into blinking for ever would have
a white run with no end on its left, so the record measures how long white runs can be. This proves that one
recorded run must end where it does, for a reason nothing farther out can undo. It covers this one starting pattern
only: by itself it does not show that 21 is the most possible at depth 125, it gives no limit at other depths, and
the prize question for a blinking middle stays open.

**An everyday picture.** A crossword in which pencilling in one more square fixes the last letter of a long answer,
turning it into a word no dictionary contains. Squares farther along the grid do not cross that answer, so nothing
written there can save it.

## The formal statement and proof

*Where:* RULE30-GPT.md GC1199; tests/probes/lexicon/rule30_young_birth_zero_ray.py.

**Claim (PROVED; GC1199, Local L684; fixed prefix only).** In phase1, fix initial left depths1..124 to the published depth125 witness in site/wolframcollatzmahler/data/records.json. No actual right trace can coexist with these cells and zeros at depths125..146 for the corresponding query horizon. This excludes a one-cell extension of this witness prefix, not every depth125 prefix or every depth.

**Carrying proof.** A left-neighbour observation at tick t depends only on initial left depths1..t+1 and the fixed wall. Thus every such row gives the same trace through145 as the named zero-ray calculation; farther cells, including147, cannot repair it. The calculation by independent packed-integer and literal lookup evolution gives the visible word at white ticks71,73,...,145 as00100100001000010000100001000010000101. This38-bit word is in the committed phase1 minimal forbidden catalog, whose absence certificate is already adopted. It contradicts any actual right trace. The finite calculation and the prior certificate are tier1 inputs; the all-tail locality implication above is the carrying step read by Local L684. The earlier white samples reproduce the fixture, while the forced last visible1 closes the cut. Equivalently, with the original prefix through145 fixed, that cut requires initial depth146 black.

**Unexpected horizon guard.** With depths146/147 respectively00, the first black-clock failure is146. Setting only147 to1 repairs it without changing any earlier trace or the cut at145. Therefore that zero-ray clock failure alone does not exclude all length22 extensions. The certified cut does: it reads no cell beyond146. No real canonical parent, extra clock tick or all-depth bound is assumed.

**Filing check.** proof_dupes.py --near W285 gives G130, G234 and G240; all three read. G130 supplies general triangular locality, G234 controls delayed deep resonance outside a clock cone, and G240 gives source/edge restrictions. This uses locality and an adopted cut to pin one previously measured white-terminal pivot; it does not restate those results or claim a new coding theorem. GC1155's existing depth125 free-pivot control is credited in GC1199.

**Promotion receipt.** L684 at61f014b8 reads the locality and exact horizon and independently checks the word under three random tails. Its catalog certificate is adopted, not rerun. Promoted from W285.
