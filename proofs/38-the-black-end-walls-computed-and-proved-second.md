# The black-end walls (computed and proved, second-read): no finite seed has a column eventually reading 0 1^q for q = 7 or any q >= 9

*Siblings, Jen and the squeeze. Derived from [PROOFS.md](../PROOFS.md), entry "38. The black-end walls (computed and
proved, second-read): no finite seed has a column eventually reading 0 1^q for q = 7 or any q >= 9"; rebuild with
`python3 proofs/build.py`. Edit the proof in PROOFS.md and this summary in [summaries.md](summaries.md), never this
file.*

**Status:** second-read both ways.

## In plain words

In Rule 30, no pattern that starts from finitely many black cells can settle into a column that beats "one white, then q black" for ever, when q is 7 or at least 9.

**What it says.** Pick any column of a Rule 30 picture grown from finitely many black squares. It can never end up repeating one white tick followed by seven black ticks, nor one white tick followed by nine or more black ticks. A small window around the column, thirteen squares wide, is followed through every way it could possibly evolve. In every case where it can run for ever, the column next door is forced into a repeating beat of its own. Two neighbouring columns that both repeat for ever are impossible for a finite start, by a classical theorem.

**Why it matters.** It closes most of a whole family of rhythms that the centre column might have settled into. The method came from an outside project. We checked its finite cases independently and repaired a gap in its general argument. The cases it cannot reach include the rhythm that matters most, one white then one black, which is Wolfram's period-2 question.

**An everyday picture.** A drummer who plays one rest and then a long roll, over and over, forces the drummer beside them into a fixed pattern too. Two locked drummers side by side cannot both keep going when the band started from a finite crowd.

## The formal statement and proof

*Status:* second-read both ways. GPT's GC806 lemma was second-read by hand by Local (chat L430). The logic of
Local's two certificates was read by GPT (GC807 for SG, GC809 for WT); GPT did not rerun the enumerations. Filed by
Local at GPT's request (GC809), 2026-10-09.
*Provenance:* the claim and the strip-graph method are from an external agent-run repository,
cochon123/rule30-prize, pinned at 3915b39 (`research/strip_graph.py`, `research/isolated_zero_uniform.md`). There
it was unverified and its uniform proof had a gap. This entry is its replication and repair, not an independent
discovery.
- GPT read the source without running it (GC805): the relaxation is sound, and its Lemma F does not follow.
- GPT repaired the uniform step (GC806).
- Local reimplemented the finite cases from GC805's specification alone (`rule30_isolated_zero_strip.py`, SG, L429)
  and computed the wrap table (`rule30_isolated_zero_wrap.py`, WT, L431). Both had predictions pushed first, and
  both are exhaustive and take seconds.
Not a prize claim: period 2 (q = 1) is not touched.

**Theorem.** Let q = 7 or q >= 9. No nonzero finite configuration of Rule 30 has a column that is eventually
periodic with the period word $0\,1^q$ (one white tick, then q black ticks).

**Proof.** Suppose one does. Shift it to column 0. Number the phases 0 .. q with phase 0 the white tick, and start
the clock at a time from which column 0 follows the word.

*The strip.* From that time on, the cells on positions -6 .. 6 form an infinite path in a finite graph.
- The vertices are (row on -6 .. 6, phase), with centre 0 at phase 0 and 1 otherwise.
- An edge applies $x'(i) = x(i-1) \oplus (x(i) \lor x(i+1))$ exactly on -5 .. 5, leaves the two outer cells free,
  and advances the phase.
- An infinite path in a finite graph ends in one cyclic strongly connected component. Inside a component of period
  P, every edge advances the BFS class by one modulo P.
- So if column -1 (or +1) has one value on each class, that column is eventually periodic along every path.

*Finite cases, q = 7 and 9 <= q <= 16 (SG).* Each of these graphs has exactly one cyclic component. Its period is
q + 1, and column -1 has one value on each class. The component has 218 vertices at q = 7 and 14q + 74 for q >= 9.

*Every q >= 17 (GC806 and WT).*
1. Ten consecutive 1-ticks at column 0 force columns +1, +2 to 01 within nine updates, whatever enters at +6, and
   01 then persists while the centre stays 1. Write b .. f for columns +1 .. +5 and z for +6.
   - From b = 1, one update gives the pair 01 or 00.
   - From 00 with d = 1, two updates give b, c, d = 000.
   - From 000 with e = 0, two updates give 01.
   - From b, c, d, e = 0001, the prefixes run 1011, 0010, 1 1 1 e_3, 0 0 0 e_4. Here e_3 = NOT f_2 and
     f_3 = f_2 OR z_2, so e_4 = 1 xor (e_3 OR f_3) = 0, and two more updates give 01.
   - The bound is 9, attained (all 32 x 512 boundary paths checked).
2. Seven consecutive 1-ticks force columns -6 .. 0 to 1010101 by the left inversion; depth j needs j + 1 ticks.
   With q >= 17, every row at phases 11 .. q - 6 therefore has the prefix (columns -6 .. +2) 101010101.
   - At those phases the pair 01 held the tick before, so $d' = \lnot(d \lor e)$. Then d' = e' = 1 forces f = 1 and
     f' = 1, and the suffix (columns +3 .. +6) is neither 1100 nor 1101.
   - So these rows lie in C, a set of 14 rows.
3. At phase q, column -1 = 0 xor (1 OR x(1)) = 1 and columns +1, +2 = 01, so the prefix is one of the 32 words
   h + 1101.
   - Following every strip path from each of these 32 x 16 rows through phase 0 and phases 1 .. 11, only prefix
     110001101 can reach C at phase 11 (WT, exhaustive).
   - Its column -2 is 0, so at the next phase 0, column -1 = 0 xor (1 OR 1) = 1.
   - At phases 1 .. q - 1, column -1 = 1 xor 1 = 0, and at phase q it is 1.
   - So column -1 is eventually periodic with period q + 1.

*The contradiction.* Columns -1 and 0 are then periodic with periods dividing their lcm, on an unbounded window.
Jen's theorem with a clock (entry 5) forbids this for a nonzero finite configuration. ∎

*Remarks.*
- The method certifies nothing at q = 1 .. 6 or 8: each graph has a component forcing neither neighbour. At q = 1
  that component is the 84-ring's strip.
- Radius-7 and radius-8 strips certify none of those cases either (`rule30_isolated_zero_wide.py`, L433).
- Exact ring models, whose column reads 0 1^q, exist for q = 1, 2, 3, 4 and 6, on rings of 7, 12, 7, 15 and 15 cells.
- Post hoc, the single-component shape persists to q = 40.
- The theorem is a statement about finite seeds. Rings are not excluded.

*Near-entry gate (Local, at filing).* `proof_dupes.py --near 38` gives 37, 17 and 06, read in full. 37 is period 1
(the constant walls), and 17 is Jen's theorem in the record's form; entry 38 uses entry 5's clocked version of
it only as its last step. 06 bounds zero runs. None is restated. The hard checks pass (272 entries).

*Filed-text audit (GPT GC812, 2026-10-09).* Read entry38 in full after7364e4b7, and ran
`proof_dupes.py --near 38`:37,17,06 read in full, hard checks pass at272 entries. The
filed theorem is the repaired restricted-wall result, not a restatement of any of those
three. It preserves the radius6 relaxation, eventual-onset/phase alignment, SG's finite
range, GC806's nine-update bound and phase11 cruise membership, WT's twelve-update wrap
and the final two-column contradiction. At q17 the cruise window includes phase11 exactly;
this guards the uniform threshold. The numerical certificates remain Local's independently
implemented SG/WT runs, not a GPT rerun. Original external claim/method and repaired proof
are correctly credited; q1..6/q8 and ring models remain outside the conclusion. No change
to the theorem or proof is needed.
