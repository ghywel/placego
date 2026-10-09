# The Condrey white end (computed and proved, second-read): no finite seed has a column eventually reading 1 0^q for any q >= 10

*Siblings, Jen and the squeeze. Derived from [PROOFS.md](../PROOFS.md), entry "40. The Condrey white end (computed
and proved, second-read): no finite seed has a column eventually reading 1 0^q for any q >= 10"; rebuild with
`python3 proofs/build.py`. Edit the proof in PROOFS.md and this summary in [summaries.md](summaries.md), never this
file.*

**Status:** second-read by Cloud (CL110), which checked steps 2 and 3 by hand and replayed step 1 with a third.

## In plain words

No Rule 30 picture grown from finitely many black squares can end up with a column that beats one black tick and then ten or more white ticks, over and over.

**What it says.** Next to such a column, a narrow strip of eight cells is forced into one fixed rhythm, whatever lies further out. So the neighbouring column repeats too. Two neighbouring columns repeating for ever is something a pattern with a left edge cannot do, because the edge sweeps leftwards and breaks the rhythm.

**Why it matters.** It closes almost all of one of the two "Condrey ends", a family of rhythms that had no closed case. The same short argument also gives a simpler, uniform proof of most of the other end.

**An everyday picture.** A long silence broken by a single drumbeat, over and over, forces the neighbouring drummer into one fixed rhythm too, and two locked drummers side by side cannot both keep going while a crowd advances on them from the left.

## The formal statement and proof

*Status:* second-read by Cloud (CL110), which checked steps 2 and 3 by hand and replayed step 1 with a third
implementation (`rule30_cloud_white_end_replay.py`, WR). Local's exploratory finding (L498) was replicated before
filing by a separately written implementation (`rule30_white_end_jen.py`, WJ, predictions first). Filed by Local,
2026-10-09.
*Provenance:* the route is the one-hole relaxation of G15-G20, OH and OHC (rule30_one_hole_widths.py), read for column
+1's whole time series rather than its hole bits (L497). The finish is Theorem A (entry 5). The white end was the
PARKED half of the Condrey ends row, with no case closed (§8.62).

**Theorem.** Let q >= 10. No nonzero finite configuration of Rule 30 has a column that is eventually periodic with the
period word 1 0^q (one black tick, then q white ticks).

**Proof.**
1. *The relaxation.* Take the 8 cells right of column 0, x1 .. x8, with an arbitrary outside bit beyond x8 at every
   step. Every actual history restricts to such a path. Let M_q be the period's step relation, one black step and then
   q white steps, with every outside bit. Let S_k be the k-fold image of all 256 states. The S_k decrease, so they
   reach a stable set S in finitely many periods, and an actual state lies in S from some period on.
2. *Column +1 is determined (computed).* For q = 10 .. 40, x1 takes a single value at every tick of the period from
   S: column +1 reads 1 0 0 1^(q-2).
3. *Every q >= 10.* The white relation satisfies W^(n+4) = W^n exactly for n >= 22. So M_q = M_(q-4) for q - 4 >= 22,
   S_q = S_(q-4), and the tick sets R_j = W^j B S agree with q - 4's for j <= q - 4. For j in (q - 4, q] they repeat
   with period 4, since j - 4 >= 22. Induction from q = 37 .. 40 covers every q >= 41.
4. *The contradiction.* Columns 0 and +1 are then both (q + 1)-periodic for ever. Theorem A (entry 5) forbids two
   adjacent columns that are P-periodic on an unbounded window in a configuration with a leftmost black cell. If that
   cell lies right of column 0 at time 0, re-base time: the left edge passes column 0 in finitely many steps. ∎

*Checks.*
- Three implementations agree: the bitmask one (OH's `jen` mode), WJ (row tuples) and Cloud's WR (set-valued
  relations).
- At width 6 no q is determined; at width 12 no q from 2 to 9 is.
- Plain forward simulation of 200 random true right halves for each of q = 10, 12 and 20 ends, every time, in the
  predicted column +1 word (exploratory).

*Remark (the same route at the black end).* At width 8, the walls 0 1^(p-1) have column +1 determined for every
p >= 15 (B^(n+4) = B^n from n = 20). This reproves entry 38's exclusion for q = p - 1 >= 14, uniformly and without
GC806's lemma, but not entry 38's q = 7 or 9 .. 13 (L497).

*Scope.* q = 1 .. 9 at the white end stay open; q = 1 (the word 10) is the period-2 wall itself. Not a prize claim.

*Near-entry gate (Local, at filing).* `--near 40` gives entries 38 (the black end, by the two-sided strip; a different
family, cross-referenced), 37 (period 1) and 03, all read. None is restated. Hard checks pass.
