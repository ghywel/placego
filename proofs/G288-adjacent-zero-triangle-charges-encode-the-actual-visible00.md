# Adjacent zero-triangle charges encode the actual visible00 pair

*GPT's proofs, second-read. Derived from [PROOFS.md](../PROOFS.md), entry "G.GPT288. Adjacent zero-triangle charges
encode the actual visible00 pair (second-read by Local, 2026-10-13)"; rebuild with `python3 proofs/build.py`. Edit
the proof in PROOFS.md and this summary in [summaries.md](summaries.md), never this file.*

**Status:** proved by GPT and second-read by Local.

## In plain words

Inside a white triangle, an odd-or-even tally along a slanting path is odd exactly when two successive white-beat
bits from the right are both white.

**What it says.** Start with a row where a black square is followed by a long run of white squares; under Rule 30
that run shrinks tick by tick into a white triangle. Assume the clock, a middle column that blinks black, white,
black, white: proof G287 turned each check that its black beat is obeyed into a parity, that is, whether a count is
odd or even, of the places along a slanting path where two white squares sit side by side. The next check, two ticks
later, uses the same path moved one tick later and one square further out, plus one extra square at its end. This
result tallies, along the first path minus its last place, how many places switch between "two white side by side"
and not under that move. The tally is odd exactly when the two successive bits heard from the right at the white
beats (the ticks when the right side gets through), one just before each check, are both white. It holds while the
white run reaches far enough to cover both checks and both checks pass. So the stream of these values can never read
odd, even, odd, nor odd four times running (that would need five white bits in a row at the white beats, which is
already known never to happen).

**Why it matters.** It ties hidden bookkeeping inside the triangle directly to what is actually heard from the
right, working forward from the real starting row without inventing an earlier history. It is not a rule that
predicts the next check, and it gives no bound on cost. It does not claim the two forbidden patterns are the only
limits: an all-even stream is still allowed. It does not newly prove that two black bits never come in a row at the
white beats; it uses that known fact.

**An everyday picture.** Two rows of chairs, the second one row back and shifted one seat along. Walk both rows side
by side, and tick a tally each time "two empty chairs together" is true in one row but not the other, skipping the
last seat. The tally comes out odd exactly when your last two glances through the window on the right, one before
each row, both showed an empty chair.

## The formal statement and proof

**PROVED, Local L689 atf7e087e2.** Source: RULE30-GPT.md GC1204, following second-read G287. Under its black-offset convention and k+3<=E, let S_t(j)=x_t(j+2)x_t(j+1) XOR [(1-x_t(j))(1-x_t(j-1))][x_t(j+2) XOR x_t(j+1)]. On the old moving path, omit its final position to obtain parity R_a. Then R_a=(1-q(k-1))(1-q(k+1)) for the actual successive white visible bits.

**Proof sketch.** The local empty-pair update has difference S. Shift G287's path one tick and one outward depth; the next path adds exactly one terminal hole q(k+1). At the old terminal, the black guard fixes depth2=1-depth1 and makes S=q(k-1). The required total hole parities differ by1, giving R_a=1 XOR q(k-1) XOR q(k+1). The real no11 gate converts this to the stated00 indicator. Hence valid consecutive R_a cannot contain101, or1111 (the latter would force the old absent word00000). GC1204 gives the complete endpoint proof and registered controls. This is an origin-preserving coupled gate, not a finite-state update, a cost bound or a new proof of no11. L689 hand-reads the local law, shifted path, both endpoints, horizon and visible00 interpretation; no computation requested.
