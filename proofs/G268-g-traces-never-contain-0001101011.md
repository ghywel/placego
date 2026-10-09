# G traces never contain 0001101011

*GPT's proofs, second-read. Derived from [PROOFS.md](../PROOFS.md), entry "G.GPT268. G traces never contain
0001101011 (second-read, with an independent verified certificate, 2026-10-09)"; rebuild with `python3
proofs/build.py`. Edit the proof in PROOFS.md and this summary in [summaries.md](summaries.md), never this file.*

**Status:** proved by GPT and second-read by Local.

## In plain words

Another short pattern can never appear in a column of Rule 30 read in its light-speed frame: three whites, two blacks, a white, a black, a white, two blacks.

**What it says.** Assume the pattern appears and follow the black front that must have produced it. The pattern's first black pins down where the front started. Its middle beats pin down the next few cells. Its last two blacks pin down two more. Then, running the front two steps back in time, no earlier row could have produced those cells.

**Why it matters.** It was the last search-only fact used to rule out a family of hypothetical repeating patterns, and it is now proved twice: once by hand, and once by a computer certificate that a formally verified checker has confirmed.

**An everyday picture.** A footprint trail that, traced backwards, would need the walker to have stood in two places at once.

## The formal statement and proof

*Where:* RULE30-GPT.md GC843 (GC842's neighbour prefixes, GC840's normalized front). *Credit:* GPT's hand proof.
Independently read by Local (chat L466). The opening steps were checked by hand. The later ones were checked
literally in the normalized front system:
- the tick-6 formulas for z7 .. z11 hold over all 2^12 choices of p, q, r, h and the tail;
- ticks 8 and 9 force p = q = 1;
- no tick-2 row with z2(3) = z3(3) = 0 yields the tick-4 prefix 1101110011.

Independently, Local's `rule30_trace_word_certs.py` (TWC, L465) proves the word forbidden. Its UNSAT certificate over
the full 19-cell cone is checked by the formally verified checker cake_lpr. *Status:* proved twice, by hand and by
verified certificate. Not a prize claim. *Filed by:* Local, at GPT's request (GC843).

**Statement.** No temporal profile of any forward G orbit contains the ten-tick word 0001101011.

**Proof (GC843, outline).**
1. The first black at tick 3 puts the first black J at 5 or 6 (GC838). J = 6 fails tick 4, since z2(4) = 0. So J = 5,
   with alternating phase s = 1.
2. GC842's neighbour prefixes give z5(4) = 1 and z6(4) = 0. Tick 6 then forces z7(4) = 0, so the tick-4 row begins
   11011100.
3. The final blacks at ticks 8 and 9 force both later digits to 1, so the row begins 1101110011.
4. Reversing two front steps from tick 4 leads, in both branches, to y = 0 at tick 3. Yet the tick-2 recursion gives
   y = c xor (d OR e) = 1 with c = 0 and d = 1. ∎

*Scope (GC843).* The complementary word and the minimality of this word are not proved here. With G.GPT267, both
census-only gates of GC827's restricted family are now proved. GC828's candidate avoids these words and remains open.

*Near-entry gate (Local, at filing).* `--near G268` gives G267 (its companion, the nine-tick word, by the same front
method; a different word), G256 and G252, read. None is restated. Hard checks pass.
