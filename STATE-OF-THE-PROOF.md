# The state of the proof: Rule 30, 2026-10-07 (section 4 updated 2026-10-08)

*Written by Cloud on 2026-10-07 at the owner's request: "an accurate 'State of the proof' - which is not to say a
proof exists - but where we currently 'stand'. How much closer are we to the proof than when we started. Can we
project some sort of prediction based on our closeness and our rate of discovery." Every claim names the section of
the record it comes from. It summarises the record and adds no new result. Where the record and this page differ,
the record wins, and this page should be corrected.*

## 1. In one paragraph

There is no proof of any of the three Rule 30 prize problems, and nothing to submit. The work, three days old, has
attacked Problem 1 one period at a time, for every finite starting configuration, which is more than the prize
asks. Period 1 was closed before we started, by Condrey. Period 2 is open, and it is where nearly all the work
went. In three days the record gained about 200 statements with a proof and a second reader, a set of exact
computations, and a map of the problem with more than a dozen routes closed and the reasons why. On the counting
statement that would close period 2, the record has not moved since the evening of 2026-10-05. What has moved is
everything around it. We know far more about what a counterexample would have to look like. And we know exactly
which statement is missing: one of a kind that no field has a method for.

## 2. The three problems

| Problem | What it asks (CONSTELLATION.md §0) | Where it stands |
|---|---|---|
| 1 | Is the centre column non-periodic? | **Open.** Period 1 is closed for every finite configuration (Condrey, below). Period 2 is open and is the work of this record. Periods 3 to 6 are parked behind it (PERIOD-TWO.md §6). |
| 2 | Are the two colours equally frequent in it? | **Open; parked.** Nothing proved for the single cell. The measurements agree with a fair coin (RULE30-PRIZE.md §8.34, §8.35). Theorems of Problem 2's kind are proved for the uniform measure only (PROOFS.md C.5). |
| 3 | Does the $n$-th cell cost at least $n$ steps to compute? | **Open; untouched.** "Any lower bound at all" is unknown (CONSTELLATION.md row 12). It would imply Problem 1, as Wolfram notes (RULE30-PRIZE.md §8.34). |

Wolfram offers 10,000 US dollars for each (PRIZE-PROBLEMS.md §1).

**In coin terms** (added 2026-10-08 at the owner's request; RULE30-PRIZE.md, "The three questions, as a coin"). Read
the centre column as a coin, black heads and white tails. Problem 1 asks whether the coin ever falls into a repeating
pattern forever. The same face forever is ruled out (Condrey), and heads, tails, heads, tails, forever is the open
case worked here. Problem 2 asks whether the coin is fair in the long run. Problem 3 asks whether there is a shortcut
to the n-th flip. The coin is not random, so each answer is simply true or false, and only a proof settles it.

## 3. Where we started, and where we are

**On 2026-10-04 at 21:09 BST**, the first Rule 30 commit, the record held three things:
- Condrey's theorem: no column of a nonzero finite configuration is eventually constant (arXiv:2609.09431,
  2026-09-08; PRIOR-ART.md). His conclusion names period 2 as "the next unresolved case".
- Jen's theorem (1990): two adjacent columns are never both eventually periodic.
- Our first exhaustive search: no finite configuration with a periodic centre column for periods 2 to 6, over every
  right half up to 18 cells (27,262,976 cases; RULE30-PRIZE.md §5).

**Now**, the record holds three kinds of thing. They differ in how far each can take us.

*Finite facts.* These are exact, and no amount of them makes a proof.
- **Nothing close to the centre.** No period-2 counterexample has its left edge within 248 cells of the centre,
  whatever its right half (§8.56, the deep ladder). No right half of at most 32 cells works with a left half of at
  most 108 (4.3 billion cases, §8.21), and the search to 34 cells found no candidate.
- **The longest run, exactly.** R(d) is the longest zero run of the forced left half that starts at depth d, over
  every column 1. It is computed exactly to d = 89, where R(89) = 75 (§8.36, §8.37). If R(d) is finite at every
  depth, period 2 is impossible for every finite configuration (PERIOD-TWO.md §2).
- **The single cell.** The centre column's linear complexity is exactly half its length at 2^22 bits (§8.70).
  Wolfram's own computations of that column go much further.

*Theorems.* These are proved, second-read inside the project, and not reviewed outside it. Each excludes a class of
counterexample, or bounds what a counterexample can do.
- Theorem A, Jen's theorem with a clock: two adjacent columns can be periodic together only for a bounded window.
  So in a counterexample the kicks to column 1 cannot thin out faster than geometrically (§8.54).
- Theorem A′, the window principle (§8.58). It holds in the same words for Collatz.
- Theorem B: zero runs are bounded beside periodic columns (§8.54).
- Theorem E: column 1 cannot be Sturmian. With Jen's theorem, no coding of a rotation by a single arc works,
  rational or irrational (§8.57). These are the first columns 1 beyond the eventually periodic ones for which
  Conjecture LR, that no column 1 makes the left half eventually zero, is proved.
- Excluded with them (PERIOD-TWO.md §6, row Q7):
  - Corollary F: near-squares at unbounded periods, which covers period-doubling, Chacon and every substitution
    fixed point that starts with a double letter;
  - Theorem E″ and GPT's G131 to G136: arc codings for almost every rotation number, block codes of Sturmian
    words, and rotation codes whose resets come further apart than geometrically;
  - Theorem A⁗: Thue–Morse and paperfolding, for every left edge up to 15,868 cells.
- The channel bound. Beside a 0101 centre, column 1 carries at most 0.1236 bits per visible bit, whatever the right
  half. This is certified exactly in integer arithmetic (§8.20, §8.33).

*The map.* Every exact form of the problem has been written down and checked against the others (PERIOD-TWO.md §2):
the forced walk, the wall form, the counting form. More than a dozen routes are closed, each with the reason it
fails (ten in PERIOD-TWO.md §4, more on the board in §6). All the forms end at one sentence (PERIOD-TWO.md §5):
**keeping the 0101 wall's conditions costs real information.** In counting form: the number of configurations on w
cells whose centre reads 0101 for T steps falls like 2^(w − αT) for some α > 0 (§8.51, question 1). It is measured
close to α = 1, at w = 24. The half of it paid by the seed's left part is proved. The half paid by the right part
is the open problem.

**So how much closer?** There are two honest answers.
- **On the statement that would close period 2: not measurably.** The board rows for that statement (Q1, the
  counting form) and for the move to a finite window (Q2) were written at 23:07 on 2026-10-05. Their "What is
  left" cells have not changed since (the git history of PERIOD-TWO.md). Q1's reads: "The proof. No known method
  reaches it." The third main-line row, the wheel's kicks (6.1), moved for the first time tonight (§4).
- **On what a counterexample would have to be: a long way.** A period-2 counterexample, if one exists, must look
  like this:
  - its left edge is more than 248 cells from the centre;
  - its column 1 is never eventually periodic, so the wheel slips for ever (Jen);
  - its kicks come no more rarely than geometrically (Theorem A);
  - its column 1 carries at most 0.1236 bits per visible bit (the channel bound);
  - its column 1 is not Sturmian, not any of the codes above, and has no near-squares at unbounded periods.
  None of this was known on 2026-10-04. It is the kind of progress that makes a counterexample implausible without
  proving there is none.

The record is plain about the gap (PERIOD-TWO.md §5): the excluded classes all have zero entropy, while the column 1
of a real right half has positive entropy, about 0.08 bits per visible bit (§8.20). "None of this reaches the real
case, where kicks come at a steady rate" (the honest summary of RULE30-PRIZE.md).

## 4. Today's frontier

Most of 2026-10-07's work sits in row Q7, on one sub-case: excluding Thue–Morse and paperfolding as column 1 for
every left edge, not just up to 15,868 cells. §8.59 reduced that to one question, whether the left side of Rule 30
settles at a bounded rate. GPT's G164, G165 and G184 split the question into two gaps:
- **gap 1, a budget:** each period-doubling stage of the left side's diagonals, of period q, runs up a "clock debt"
  of at most a constant times q;
- **gap 2, growth:** the stage lengths, divided by the period, grow without bound on every history rooted at a
  finite seed (G184). By G186 and G187 it is enough that they pass a threshold, 17 at slope 5/2.

The afternoon joined the two gaps into one statement about a single history (GC310, GC312). It then attacked the
debt through *pulses*. A pulse is a step whose driver has a single black bit, and its *source weight* is the number
of black bits in the step before.

What the last two days settled on this line:
- **Proved, with a second reader.**
  - Propositions 11 and 12 (PROOFS.md entries 24 and 25, Local's, read by GPT): the worst case of a pulse's
    window, and a pulse's source weight read off its child's black runs.
  - GPT's G143 to G204, read by Local. Among them: G188, a doubled stage of period at least 4 cannot return to
    zero within eleven steps; G192, the return-eight graph is acyclic; G203, every excursion pays an automatic
    baseline.
- **Computed exactly.**
  - The earliest entry to period 64 in the rooted tree is at depth 65,821,413 (Proposition 9, TM6).
  - The rooted period-32 stage runs past 2.6 × 10^10 steps, and on the 17 histories still live R_6 exceeds
    412,876,800 (Proposition 10).
  - Clock debt is at most 60 on all sixteen period-32 histories to depth 1,048,576 (RD32, GC325).
  - Local's later HW32 run records debt78.5 on a pulse-free39-edge interval, versus a largest
    period-32 pulse-window debt37.0 (CHAT-LEDGER.md L218). Its initial snapshot-count control
    failed as coded and remains recorded; the stored snapshots agreed with RD32. This is finite
    evidence from Local's execution, not an independently rerun GPT certificate. The live-walk
    debt scan originally omitted its frontier endpoint. Local's HW32w corrected D_end check
    reports unchanged maxima (L224). GPT independently checks the displayed39-edge segment
    by scalar transitions and reset scans (GC370), reproducing elapsed176 and debt78.5;
    this certifies that segment, not root ancestry or the full census.
- **Refuted.** More than a dozen predictions, each kept in the record. Two examples: the next edge after a heavy
  window costs at most 2 (GC350), and a bound on the source weight just before a pulse (GC354).
- **Open.** Gap 2 on every rooted history. For gap 1, a bound on the debt carried across the edges between pulse
  windows. GPT's GC357 puts it exactly: the bit-incidence budget "has no established inequality to that
  cross-boundary h+p".

The record is clear that this line cannot reach the real case: "Nothing for real right halves: their repeats are
short and late, far below Theorem A′" (§8.59). If it closes, it gives a new theorem about two famous zero-entropy
words, and a tested method.

**The main line moved tonight, a little.** At 20:28 Local worked row 6.1, the wheel's kicks, for the first time
since 2026-10-05. It did so under the new draw-and-work rule. Local's KL run finds the kick alphabet local: for every
right side, after 133 steps on the wheel, kicks occur at only four classes, each with a short range of sizes. So
the interior chooses at most log2 6 bits per kick (Proposition 13, PROOFS.md entry26, second-read by GPT in GC359 and filed by
Local). The statement conditions the old wheel duration and the new phase fit; it does not classify
arbitrary column1 histories. It narrows what the missing statement must control. It does not supply it: "the cost side: a statement
that the kicks must pay for the left half's conditions" is still open.

### The frontier on 2026-10-08 (added by Cloud, 22:31 BST)

The prize gap is unchanged: period 2 is still open, and the counting statement (Q1) has not moved. Here is what the
day settled around it. Each item names its source, and each proof named here has a second reader.
- **The sibling Rule 210 is settled for period 2.** No finite Rule 210 seed keeps the full 0101 clock (Proposition 19,
  PROOFS.md entry 32, hand proof, second-read). It does not carry over to Rule 30 verbatim (GC479).
- **Q6: the frontier, mapped exactly.** This is the owner's red-object idea (CL054), worked through as a ray argument.
  - A finite left edge forces an edge event at every step of its frontier (GC585).
  - That ray's pull on the cells that must stay white has the parity of the Fibonacci numbers, odd, odd, even
    (GC586).
  - The inside must pay that beat with ever older events (GC598), at exact binary age slots (GC600). It cannot do
    it with a long streak beside the edge (GC597), but it can restart events for ever (GC599).
  - Five fixed sources are silent at the frontier (SS and GC589), and the near-silent ones never harden (SO and
    GC591), so silence alone cannot block the ray.
  - The open step is joint: whether the actual clock lets the late, restarting events pay the beat at every depth.
    The realizable white runs stay between 7 and 16 out to depth 102 (RR, RR2, replayed in RRX, RRP and ZR3), so no
    counterexample appears where we can look.
- **Edge events obey three local rules** (CL055, read in GC595): never adjacent straight down or down-left, and a
  row of events runs over black cells and ends on one white.
- **Row 6.1: the two readings of a kick, reconciled.** The phase reading and the charge reading of a kick differ by
  14 times the sum of the odd gaps between the locks, mod 28 (G248 with GC582). This was replayed at all 211,000
  recorded lock pairs. Entry 26's one-turn table needs 57 observations; with 56, one more class appears, which no
  recorded kick uses (GC584, GC588, replayed independently).
- **Q1:** the first right-paid ratio keeps a small bias out to j = 35 (ZR3, L316).
- **Side questions, off the board by design** (CONSTELLATION.md section E). One asks whether column 1 next to the
  wall carries positive information per symbol. Two neutral blocks, 100 and 10000, have actual returns (GC605 to
  GC609). They do not concatenate freely: 11 of the 128 seven-block words are forbidden, with certificates (NL,
  L323).
- **Refuted and kept**, among others: hardening of near-silent sources by age 256 (SO), a further departure class
  at 54 transitions (RO), and two slips in the short-return proofs, each caught by a second reader (GC608, GC609).

## 5. The rate of discovery, measured

| Day (BST) | 10-04, from 21:09 | 10-05 | 10-06 | 10-07, to 20:20 |
|---|---|---|---|---|
| Commits to the repository | 27 | 210 | 625 | 564 |

PROOFS.md opened at 11:15 on 2026-10-06, with 40 entries filed from the earlier record by 12:00. The new
second-read entries after that, by six hours (BST), from the file's git history:

| 10-06, 12–18 | 10-06, 18–24 | 10-07, 00–06 | 10-07, 06–12 | 10-07, 12–18 | 10-07, 18–20:25 |
|---|---|---|---|---|---|
| 40 | 59 | 34 | 18 | 7 | 3 |

The second table is a check nobody asked for. It was exploratory, with no prediction written, and it surprised me:
the rate of second-read entries fell about tenfold in a day. Part of that is a change of kind, not of effort:
- the 2026-10-07 work is long finite certificates (TM6, RS32, RD32) and refuted predictions, which take hours
  each;
- GPT's day went mostly into numbered notes, GC300 to GC357, many of them second-read by Local in the chat rather
  than filed in PROOFS.md.

Perhaps part of it is the route itself: the easy exclusions came first.

PROOFS.md began on 2026-10-06 and now holds about 200 second-read entries:
- Local's 25 numbered statements (Theorems A, A′, A‴, A⁗, B, E, E″, Corollary F, Lemmas 1 to 4 and B1 to B3,
  Propositions 5 to 12);
- 8 short proofs (section C) and 2 on Collatz (section F);
- 7 early theorems by GPT (section E), and 159 more (section E2), each second-read by Local.

The 159 in E2 sort by what they bear on (Cloud's count, from their titles):

| Bears on | Entries |
|---|---|
| Q7, the left band's settling (the Thue–Morse and paperfolding route) | 49 |
| Q7, excluded classes of column 1 and their scope | 22 |
| The Collatz twin, and Mahler | 40 |
| Time, moving frames and races (the owner's physics questions, not the prize) | 25 |
| The Rule 210 side system, prime rings, the generality of the period-2 tools | 15 |
| Routes since closed (descent, sideways dynamics) | 8 |

Re-derivations were common at the start. The forced left half (Meier and Staffelbach 1991, Condrey), Jen's theorem
for periodic columns 1, the domain filter (Hanson and Crutchfield) and the left side's diagonal periods (Jen 1986,
Rowland) were all found here first, then in the literature (PRIOR-ART.md). A limited search found no earlier
statement of Theorems A and A′ ("NOT FOUND; NEAR") or Theorem E ("NOT FOUND"). The record calls such a result "a
limited search, not proof of absence".

## 6. A projection

**Why the rate cannot be extrapolated to a date.** Two clocks are running, and neither points at the prize.
- **The finite clock runs logarithmically.** Each four more depths of R(d) costs about 4.7 times the compute: depth
  85 took 3 hours, 89 took 14, and 93 would take about 2.5 days on Local's machine (PERIOD-TWO.md §6, Q6). The left
  edge excluded grew from 104 cells to 248 by deeper engines (§8.56). These numbers grow like the logarithm of the
  compute spent, and the statement needs them for every depth.
- **The theorem clock runs fast, on sub-cases.** 139 second-read entries on 2026-10-06, 40 of them filed from the
  earlier record, and 62 on 2026-10-07 to 20:25. But the quantity that would measure progress toward the prize is
  a cost theorem for some positive-entropy column 1 beside the 0101 wall. Three days have produced none. A rate of
  zero does not extrapolate.

**The judgement.** These are Cloud's estimates. They are not measurements, and they are offered so that they can be
checked later.

| Event | Within | Estimate | Why |
|---|---|---|---|
| A full proof of Problem 1 from this work | a year | well under 1 in 100 | Every period, not only 2, for the single cell. The record's nearest relatives are Mahler's 3/2 problem (open since 1968) and Collatz (open since 1937). |
| Period 2 for every finite configuration | a year | a few in 100 at most | It needs the missing statement, and no field has a method for it (§8.47). |
| Thue–Morse and paperfolding excluded for every left edge | weeks | perhaps 1 in 4 | The route is reduced to named gaps, with a stream of finite certificates, but today refuted more than a dozen of its predictions (§4). A real new theorem, though it stays on the zero-entropy side. |
| Theorems A, A′ and E written up for outside review | days | likely, if the owner chooses it | They are short, second-read and checked by scripts. Outside review is the step the record has not had. |

**What would change the estimate.** A cost theorem for even one positive-entropy family of columns 1 beside the
0101 wall would be the first step onto the main line. So would a condition, implied by the wall, that forces column 1
to be eventually periodic (Q2, not started). Either would move the second row by a large factor. More lemmas on
zero-entropy classes, more depth on R(d) or a wider search would not.

## 7. Why Rule 30 suits this work

The owner, 2026-10-07: "precisely because the prize pool is low, very few people would naturally be chasing it. Yet
our chasing is finding discovery after discovery - it as an ultimate source of truth problem". The record bears
that out in three ways, with one caution.
- **Every finite claim can be settled by running it.** The arithmetic is exact bits, with no rounding to argue
  about (PRIZE-PROBLEMS.md). A prediction written before a run is decided by the run. That is why the record could
  keep its failed predictions honestly, and why three models could check each other quickly.
- **The ground is quiet.** The literature on Rule 30's columns is small: Jen, Kopra, Rowland, Condrey and a few
  more. A result found here has a fair chance of being new, and a short search can say whether it is.
- **The relatives are famous.** Period 2 shares its structure with Mahler's 3/2 problem and with Collatz, exactly
  (COLLATZ-PRIZE.md §5). A tool that works here is a tool for those, and the Collatz prize is ¥120 million.
- **The caution.** "Discovery after discovery" counts three different things. Some results were new to us but
  known. Some are new as far as the search went. Very few bear on the prize. Section 5 keeps them apart, and so
  should anything sent outside the project.

On the prize's size: judged by its nearest relatives, Problem 1 is as hard as problems with prizes a hundred times
larger. A small prize keeps the field quiet, which is the owner's point.

## 8. What we would tell Wolfram

The message, in five sentences:
1. Since 4 October 2026, an open, AI-assisted record has attacked Problem 1 at period 2, for every finite
   configuration, after Condrey's period-1 theorem.
2. It has no proof and makes no claim.
3. It proves several partial theorems, which a limited search did not find in print: Jen's theorem with a clock,
   the window principle, and the exclusion of every Sturmian column 1. It also has a certified
   bound on what column 1 can carry beside a 0101 centre.
4. Its exact computations exclude any period-2 counterexample whose left edge lies within 248 cells of the centre,
   and compute the forced left half's longest zero runs to depth 89.
5. Every route reduces to one counting statement, which is measured to hold and is proved for half of it. We would
   welcome a pointer if any of this is already known.

A draft of the full letter is with the owner. Whether to send it, and when, is his call.
