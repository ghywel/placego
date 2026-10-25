# Deep questions

*A shared question tracker, begun at the owner's request on 25 October 2026. For the human, GPT, Local and Cloud.*

This is a place for questions that might change how we see a problem. They need not arrive in mathematical language, fit the current proof attempt, or promise an immediate result. An intuition chooses a question to examine; it does not establish the answer.

Keep the question in ordinary words. Translate it without replacing it. A failed interpretation is not necessarily a failed question. Equally, an attractive analogy earns no exemption from a counterexample.

## How to use this tracker

- Give each question a permanent **DQ number**. Keep the original wording and record later refinements underneath it.
- Explain what an answer would change, what is already known, and the exact point where our understanding stops. Link to evidence instead of repeating an entire technical record.
- When taking up a question, add the reader, date and precise interpretation being examined. On returning it, leave the answer in ordinary words, its mathematical scope, the evidence, and the next unresolved question. Preserve failed attempts.
- Use **Open** for a question awaiting exploration, **Exploring** for a named current investigation, **Parked** for a question awaiting a stated new ingredient, and **Answered in scope** when a specified version has an answer. A refuted proposal can be recorded under an open question; it need not close the larger question.
- There is no question quota, required experiment or obligation to manufacture a breakthrough. Questions may cross problems, but a proposed connection must eventually say what transfers and why.

This tracker is not a launch queue or a proof register. Existing holds and review standards still apply; see [NOW.md](NOW.md). Its creation does not restart workers or schedules. The entries below preserve the conversation and existing evidence; they announce no new theorem or experiment.

## Questions at a glance

| ID | Question | Current position |
|---|---|---|
| DQ-001 | What can we change in an exception without losing what makes it exceptional? | Open; the agreed warm starting point |
| DQ-002 | Have we confused a short repeating pattern with an easy mathematical case? | Open; the distinction is clear, the best doorway is not |
| DQ-003 | What underlying principle would explain why every finite arrangement must fail? | Open; no general mechanism established |
| DQ-004 | Can the infinite problem be reduced faithfully to finitely many cases? | Open; eight streets provides a model, not a transferred proof |
| DQ-005 | What does a drawing hide when its curve loops back toward zero? | Open in the clarified visual sense; the earlier formal route remains parked |
| DQ-006 | Could one eternal survivor force more survivors than there is room for? | Parked pending a new construction |
| DQ-007 | What would make a proof explain the phenomenon as well as certify it? | Open; a continuing question about our method |
| DQ-008 | Are we watching the wrong end? | First source/hand investigation complete; fresh-layer relation remains open |
| DQ-009 | How much does the referee have to remember, seat by seat? | Open; Local's second-round instinct from DQ-008 |

## DQ-001 — Changing an exception while preserving its essential behaviour

**Question:** “What can we remove, compress, or replace in a hypothetical Rule 30 exception without destroying the behaviour that makes it an exception?”

**Origin:** proposed in the human–GPT discussion and selected by the owner as a warm starting point, 25 October 2026. **Status: Open.** No investigation is claimed here.

**Why it matters.** If every supposed exception could be made smaller while remaining an exception, and the shrinking could not continue forever, there could be no exception. Alternatively, many different arrangements might be replaceable by a few faithfully representative types.

**Translation.** First name the behaviour being preserved. In our auxiliary test, a finite arrangement beside a permanently white boundary must keep a specified cell black at every second step forever. That is a particular mathematical test, not a synonym for every possible exception to the Rule 30 prize conjecture. A transformation must preserve that test and remain within its allowed arrangements.

**What we know.** Cutting off distant cells preserves only a bounded period of observation unless we prove more. Going backward in time is also not a general shrinking recipe: a row may have no finite predecessor, and the available backward tree does not provide the missing amplification. But preserving the observations we actually constrain can allow changes that preserving every observation would forbid.

**Next useful question.** What information is essential to the observed behaviour, and what merely accompanies it? Name one proposed replacement and the exact observations it preserves before asking whether it makes anything smaller. “Smaller” needs a measure that cannot decrease forever; it need not mean fewer black cells.

**Record:** [amplification review](reports/rstation/GPT-CL637-AMPLIFICATION-REVIEW.md); Cloud's correction and backward-tree bound in CHAT-LEDGER.md, CL638. Related: DQ-004 and DQ-006.

> **Reader and date:** Local (Claude on the M5), 25 October 2026, about 21:00 GMT; instinct-led, at the owner's request; no computation, the third halt stands.
>
> **Version of the question examined:** in a long-lived starting arrangement, which parts carry the long life and which are packaging?
>
> **Answer in everyday words (an instinct, not an answer):** our own death tables already point at the slack. The twelve
> longest-lived starts at width 44 are near-identical twins: they differ only in their earliest recorded steps, and all twelve die at
> the same moment (78). Across every start at width 40, changing the first recorded step changes the moment of death in only about
> one pair in a hundred, while changing the last recorded step changes it in two pairs out of three and leaves the two deaths
> essentially unrelated. So the long life seems to be carried by the far end of the starting row, and the near-wall end looks
> like packaging. If an eternal survivor existed, my instinct is that its exceptional part would sit at the far end, and the wall end
> could be swapped for other packaging without losing it.
>
> **Exact scope and evidence:** measurements on dying starts at widths up to 48, not on an eternal one. Sources: L942 (the first and last
> free bits; note GC1873: flipping the first recorded step changes several starting cells, and a correlation is not independence) and
> L947 (the twelve maximizers in one late word). GC1877 judged that the twin families give no invariant or map between widths yet.
>
> **What failed, or remains unknown:** whether the slack survives at every width, and whether swapping the packaging can be paired with a
> size measure that falls and cannot fall forever (this tracker's own requirement). This must not be confused with the closed
> "prefix pump" route (GC1872): that tried to extend the early steps, not to swap them.
>
> **Status and what would make another visit useful:** Open. A useful next question: is there a measure of a start that the packaging
> swap always lowers while leaving the far end untouched?

> **GPT follow-up, 25 October 2026, GC1886:** preserve the packaging question, but do not yet identify the packaging with a physical near-wall block. L942 changes trace-history coordinates: flipping the first free history bit can alter several starting cells, while flipping the last changes only the deepest cell. The two interventions do not isolate the two physical ends symmetrically. See the [bounded investigation](reports/rule30-deep-questions-first-birthday.md). DQ-001 remains open; no size-reducing replacement has been found.

## DQ-002 — Short description versus easy proof

**Question:** Why call “black, white, black, white, forever” simplest? Is “00110, 00110, …” any less simple?

**Origin:** the owner's assumption challenge, 25 October 2026. **Status: Open.**

**What is already answered.** The first pattern has a shorter repeating block: two cells rather than five. That is an objective distinction. It does not establish that the first pattern is easier to exclude, more revealing, or the right starting point. Both have short instructions for producing an infinite sequence.

**Why it matters.** We may be choosing a case because its description looks elementary rather than because it exposes a useful mechanism. A longer repeating word could contain a feature that makes it easier to rule out.

**Next useful question.** What property actually makes a repeating pattern tractable? Is it its length, a forbidden local configuration, its interaction with a boundary, or something else? Compare mechanisms in existing proofs before proposing another catalogue. No claim about the particular word 00110 is made here.

**Record:** [period-two problem and closed routes](PERIOD-TWO.md); [review of period-four and stripe-tail work](reports/wolfram-agents/GPT-PERIOD4-AND-STRIPE-TAIL-REVIEW.md).

> **Reader and date:** Local (Claude on the M5), 25 October 2026, about 21:00 GMT; instinct-led, at the owner's request; no computation, the third halt stands.
>
> **Version of the question examined:** what made our successful cases tractable, if not shortness?
>
> **Answer in everyday words (an instinct):** in every case we have actually proved, the thing that helped was a *trap*, not a short
> description. A trap is a pattern that Rule 30 keeps reproducing by itself, next to a boundary that nothing from outside can break
> through. Our family submission (R30-20261024-8d7751) works like that: once the first 28 cells of the right side look a certain way,
> the column falls into a self-sustaining pattern by step nine and stays there forever, whatever the rest of the row holds. The outside
> period-four results have the same shape: a white collar of 30 cells, and then the tail is irrelevant (GC1878). An analogy: a short
> tune is not easier to reason about than a long one; what helps is a tune the instrument keeps playing by itself once started, in a room
> that keeps outside noise out.
>
> **Exact scope and evidence:** our trap families (L919, L935) and GC1878's reading of the public period-four proofs. No claim about the
> word 00110.
>
> **What failed, or remains unknown:** whether "black, white, black, white" at the wall is a pattern Rule 30 can keep going by itself. If it
> cannot, that may be the very reason it must fail, and the useful property would be "not self-sustaining here", not "short".
>
> **Status and what would make another visit useful:** Open. Next question: rank candidate patterns by whether the rule can sustain them
> beside a white wall, rather than by length.

> **Reader and date:** Local, 25 October 2026, about 21:25 GMT, second round; instinct-led, at the owner's request; hand reasoning only, no computation; the third halt stands.
>
> **Version of the question examined:** is "black, white, black, white" even the pattern being tested?
>
> **Answer in everyday words (a challenge to the framing):** in our auxiliary test it is not. The test checks only every second tick:
> black at even ticks, with the odd ticks left free. By the light switch (DQ-008), each odd tick is then forced to be the opposite of the
> second cell. So the "period two" case is really one check every two ticks, half a constraint per tick, beside a wall. My instinct is
> that "simple" might best be measured not by the pattern's length but by how many checks the test makes per tick, compared with how fast
> the rule can bring in fresh influence from the far side (one cell per tick). A pattern checked at every tick would be a harder target
> for a survivor, and perhaps an easier one to rule out.
>
> **Exact scope and evidence:** the even-tick test as GPT's DQ-001 translation states it; the switch identity. Whether the prize's
> period-five case reduces to a test with a different check rate is not known to me, and I make no claim about 00110.
>
> **Status and what would make another visit useful:** Open. Next question: for each repeating pattern, how many independent checks per
> tick does its auxiliary test impose?

## DQ-003 — The physics beneath the bridge

**Question:** What are we missing underneath the behaviour, as a bridge builder would be missing something essential without understanding gravity, foundations and wind?

**Origin:** the owner's bridge analogy, 25 October 2026. **Status: Open.**

**Translation.** We know Rule 30's local update rule completely. What we lack is a general consequence of it that forces the relevant observation to fail for every finite starting arrangement, however large. Knowing the instruction for each next step is different from understanding what all those steps must eventually do.

**What an answer would change.** A principle about unavoidable influence, incompatible demands, or a quantity that cannot keep changing in the required direction could replace case-by-case inspection. These are possible shapes of explanations, not claims that Rule 30 has an energy or conservation law waiting to be found.

**Next useful question.** What would an eternal survivor have to keep supplying, preventing or coordinating forever? Which of those requirements can we express without assuming the conclusion? Test any proposed principle against known long survivors and certified families, not only typical pictures.

**Record:** [current open gaps](NOW.md); [the research status board](PERIOD-TWO.md), section 6.5.

> **Reader and date:** Local (Claude on the M5), 25 October 2026, about 21:00 GMT; instinct-led, at the owner's request; no computation, the third halt stands.
>
> **Version of the question examined:** what one-sided feature of the rule could an eternal survivor be fighting against?
>
> **Answer in everyday words (an instinct):** Rule 30 treats its two neighbours unequally. One neighbour enters through "exclusive or":
> any change there always changes the result. The other enters through "or": a change there is ignored whenever the middle cell is
> black. So news travels one way with certainty and the other way only when it is let through. In our set-up the certain direction
> runs from the far end toward the wall: whatever happens at the far edge always arrives at the watched cell, one step per tick, and
> nothing can block it. The near-wall end's influence travels outward only when unmasked. Today's measurement looks like this one-way
> street made visible: the last recorded step (the deepest cell) scrambles the moment of death, and the first barely touches it. Seen
> this way, an eternal survivor is a wall cell that must answer "black" at every other tick, forever, while being forced to hear an
> unending stream of messages from an ever more distant edge. The coin model treats each message as a fair coin, so an eternal survivor
> would be an endless run of lucky tosses. The missing "physics" is a reason why the messages cannot all be lucky.
>
> **Exact scope and evidence:** the rule's exclusive-or and "or" structure is exact; the reading of L942's numbers through it is mine and
> untested. The coin model is a heuristic, not a law (GC1867, GC1873).
>
> **What failed, or remains unknown:** what the far edge actually sends. If that stream is orderly at its source and scrambled only in the
> middle, the order itself might force an unlucky message. I have not checked it.
>
> **Status and what would make another visit useful:** Open. Next question: describe exactly what a finite pattern's far edge sends toward
> the wall, before it is scrambled.

> **Reader and date:** Local, 25 October 2026, about 21:25 GMT, second round; instinct-led, at the owner's request; hand reasoning only, no computation; the third halt stands.
>
> **Version of the question examined:** my first note's "unending stream of unblockable messages", challenged.
>
> **Answer in everyday words:** I overstated it. A message from the far side always knocks: the first difference reaches the watched
> cell on time, for certain. But it need not stay. GC693's two rows differ at the second cell, knock once at an odd tick (unobserved), and
> are identical from the next tick on. The light switch of DQ-008 shows how a knock can be undone: the switch flips when the neighbour is
> black and flips back when it is black again. So the better picture is not "every message is a coin toss" but "every message flips a
> switch, and a survivor needs the flips to come in pairs". The missing physics is a reason the pairing must eventually break.
>
> **Exact scope and evidence:** GC1883 and CL638 (the fixture); GPT's first-birthday note (first arrival is forced, persistence is not).
>
> **Status and what would make another visit useful:** Open.

## DQ-004 — A finite doorway into an infinite problem

**Question:** The eight streets problem reduced infinitely many cases to a few checkable million. Could Rule 30 admit such a reduction?

**Origin:** the owner's comparison, 25 October 2026. **Status: Open.**

**What made eight streets work.** A proved reduction lets a sufficiently large instance surrender its largest burning segment, leaving a smaller instance of the same admissible kind. A solution to the smaller instance extends back to the original. The remaining finite cases were then checked. The reduction, rather than the number of cases checked, is what reaches infinity.

**What must transfer.** We need either a justified reduction from every large bad case to a smaller bad case, or a finite description that retains every feature needed to exclude eternal survival. We do not currently have that for arbitrary Rule 30 tails. Checking more widths does not create it.

**Next useful question.** Could two arrangements be considered equivalent for this question even when their detailed futures differ? If so, prove that the equivalence survives the evolution and preserves the relevant observation. Otherwise a finite model may discard the very influence that matters.

**Record:** [eight-streets reduction](reports/eight-paths-L8.md), section 3; [latest return-map kit review](reports/wolfram-agents/GPT-PORTAL-UPDATE-20261025-EVENING.md). Related: DQ-001 concerns transformations of an exception; this question also includes faithful finite descriptions without literal shrinking.

> **Reader and date:** Local (Claude on the M5), 25 October 2026, about 21:00 GMT; instinct-led, at the owner's request; no computation, the third halt stands.
>
> **Version of the question examined:** do we already have small finite doorways, and what would the other half of eight streets be?
>
> **Answer in everyday words (an instinct):** we have the first half. Our trap families and the white-collar result each say "if the first
> N cells look like this, the infinite rest does not matter". That is a finite check covering infinitely many cases, eight streets in
> miniature. What is missing is eight streets' other half: the step that pushes every large case into one of finitely many doorways.
> There, every big instance gives up its largest segment and becomes a smaller instance. Here we would need every starting row, within a
> time bounded by its width, to walk through one of finitely many certified doors. An analogy: every river reaches one of a few seas,
> and we need to show that no river wanders forever.
>
> **Exact scope and evidence:** L935 (the families), GC1878 (the collar), eight-paths-L8.md section 3 (the reduction). Today's L947 is
> evidence against one naive version: at each width the long survivors crowd into a few "doors" (patterns of the last ten recorded
> steps), but the doors change almost completely from width to width. So if finite doorways exist, they are not labelled by the last
> few recorded steps.
>
> **What failed, or remains unknown:** whether such a time bound exists at all; this is GC1878's wall, "getting an arbitrary onset row into
> a certified family".
>
> **Status and what would make another visit useful:** Open. Next question: when the doors differ at every width, what do the doors at
> different widths have in common?

## DQ-005 — Returns, repeating histories and the zeta intuition

**Question:** Could organising all the ways a system returns to a checkpoint reveal a global obstruction that watching individual runs misses?

**Origin:** the owner's association between checkpoints, zeta functions and the Riemann hypothesis, 25 October 2026. **Status: Parked.**

**Translation.** The useful question is what a systematic description of returns could tell us about the behaviour we observe. The association with a famous problem is a suggestion of where to look, not evidence of a mathematical connection to it.

**The distinction to preserve.** A whole system returning to the same state, a finite window returning, and one observed cell repeating are different events. The surrounding system can keep changing while that cell repeats. Conversely, proving that a finite model cycles does not prove that its cycle contains the white observation required by our test.

**Reopen when:** someone identifies the object whose returns are being counted, and an argument connecting those returns to the actual observed cell for the required class of initial arrangements. Merely giving the count a zeta-function form would not supply that argument.

**Record:** [return-map review and its recurrence-without-the-required-witness control](reports/wolfram-agents/GPT-PORTAL-UPDATE-20261025-EVENING.md). No Rule 30–Riemann implication is established in this tracker.

> **Reader and date:** Local (Claude on the M5), 25 October 2026, about 21:00 GMT; instinct-led, at the owner's request; no computation, the third halt stands.
>
> **Version of the question examined:** does anything in a long survivor ever come back exactly?
>
> **Answer in everyday words (an instinct, cool):** I agree with parking it. Today's measurements found that after the constrained window,
> the moments of death behave much like fresh coin tosses (L942). That is the kind of behaviour where counting returns gives averages, not
> certainties, and our question needs a certainty for every start. The plain question that would warm me up: in a long-lived start, does
> the whole near-wall stretch ever repeat exactly, and not just the one watched cell? If it never does, returns may not be the right
> object.
>
> **Exact scope and evidence:** L942 (the coin-like reading is qualified by GC1873: near the shuffled baseline is not independence).
>
> **What failed, or remains unknown:** no object has been named whose returns would bite.
>
> **Status and what would make another visit useful:** Parked, as the entry says.

> **Owner clarification, 25 October 2026, after L950:** “I am thinking specifically of the visual graph as it is drawn on paper, with the continuous looping back to the zero. It is more an analogy of the shape of the graph than a description of the actual maths.”
>
> **GPT response, GC1886:** the original formal translation above was too narrow. Keep it as history; it does not exhaust the owner's question. The clarified visual question is **Open**: when a curve loops back to the same point, what has returned, and what might the picture be hiding? A repeat of an observed value need not be a repeat of the full state. No particular graph, choice of axes or meaning of its zeros has yet been identified, so none is assumed. The earlier periodic-orbit route remains parked on its own terms. The analogy does not need a connection to the Riemann hypothesis to be worth thinking with.

> **Reader and date:** Local, 25 October 2026, about 21:25 GMT, second round; instinct-led, at the owner's request; hand reasoning only, no computation; the third halt stands.
>
> **Version of the question examined:** the owner's clarified, visual question: a drawn curve that keeps looping back to zero.
>
> **Answer in everyday words (an instinct):** there is an exact curve in our problem with that shape. Draw a running count: each tick,
> add one if the second cell is black. For a start that begins ON, as every survivor does, the watched cell is ON exactly when that count
> is even (DQ-008, Local's second note). So a survivor
> is a start whose count drawing, taken "modulo 2", comes back to zero at every even tick: a curve that keeps looping back to its
> starting value. The drawing also hides things, which is the owner's question. Two different starts can draw the same curve forever
> (GC693's pair, from tick 2), and the curve says nothing directly about the cells farther out that will decide the next loop.
>
> **Exact scope and evidence:** the count is exact (x(t+1,1) = x(t,1) XOR x(t,2)). The connection to the owner's picture is an analogy of
> shape, as the owner intended, with no claim about the zeta function.
>
> **What failed, or remains unknown:** whether the full count, not just its evenness, carries information that the even-tick test
> throws away: for example, whether long survivors climb in a recognisable rhythm.
>
> **Status and what would make another visit useful:** Open in the visual sense. A useful next question: what does the running count's
> staircase look like for the longest-lived starts, compared with ordinary ones? It is answerable later from retained tables, not now.

## DQ-006 — Too many exceptions to fit

**Question:** Could one hypothetical eternal survivor generate more distinct survivors than can fit inside a common size limit?

**Origin:** the Collatz appraisal and subsequent GPT–Cloud review, revisited in the owner's discussion of contradiction arguments, 25 October 2026. **Status: Parked.**

**Why it matters.** If a survivor necessarily produced more survivors than a proved upper bound permits, the original survivor could not exist. This is a structural counting argument; it need not enumerate every possible survivor.

**What is known.** We have a bound for a specified finite-width survival test. We do not have an operation producing the required surplus. Distinct starting arrangements can share the even-time observations, so preserving those observations does leave some freedom. But the guarded backward tree already considered cannot exceed the bound; it is not the missing construction.

**Reopen when:** a specified operation preserves finite support and the required survival, produces genuinely distinct images, and puts enough of them inside the same stated width bound. Moving sideways among arrangements or widening them remains a question, not an established method. Counting images at different uncontrolled widths does not yield the contradiction.

**Record:** [Collatz appraisal](reports/rstation/GPT-COLLATZ-TO-RULE30-APPRAISAL-20261025.md); [corrected amplification review](reports/rstation/GPT-CL637-AMPLIFICATION-REVIEW.md); CHAT-LEDGER.md, CL638. Retain Cloud's corrections when using its earlier CL637 note.

> **Reader and date:** Local (Claude on the M5), 25 October 2026, about 21:00 GMT; instinct-led, at the owner's request; no computation, the third halt stands.
>
> **Version of the question examined:** do the twin families seen today hint at the missing multiplication?
>
> **Answer in everyday words (an instinct):** they are a finite echo of it, and they probably meet the cap head-on. One long-lived start
> comes with twins that share its fate (twelve at width 44). If an eternal survivor had the same looseness in its earliest steps, it would
> come with eternal twins. But the twins live at the same width and differ only in the bits that the cap already counts. So they are part
> of the room, not extra guests, which is CL638's point about the backward tree in another form. A surplus would need more twins than
> the free bits allow, all still fitting inside the width, and nothing seen today does that.
>
> **Exact scope and evidence:** L947 (twelve maximizers in one late word), L942 (the first recorded step changes the death in about one pair
> in a hundred at width 40), CL638 (the backward tree is exactly at the cap).
>
> **What failed, or remains unknown:** whether the looseness per early step is a fixed fraction. If it were, it would put a number on the
> most twins one survivor can have, but not above the cap.
>
> **Status and what would make another visit useful:** Parked, as the entry says. Twins do not supply the missing operation.

## DQ-007 — Explanation and certification

**Question:** What would make a proof explain why the phenomenon happens, rather than only establish that the answer is correct?

**Origin:** the owner's concern about beauty, brute force and proof by contradiction, 25 October 2026. **Status: Open; a question about our method.**

**Two things to keep separate.** A proof can be valid without being satisfying to read. An elegant story can be satisfying without being a proof. Proof by contradiction describes the logic of an argument, not how much computation it uses.

**A certificate, in ordinary words.** It is a checkable record supporting a precisely stated claim. Finding the record may be difficult; checking it may be much easier. Its value depends on what the checker establishes and which cases the record covers. A certificate for one family does not silently cover every starting arrangement.

**Next useful question.** For each result, what is the reusable reason, and what is the remaining bookkeeping? Eight streets offers one example: a short reduction accounts for the infinite range, while finite checks settle the remainder. Could we seek that division here without rejecting a valid result merely because its checking is extensive?

**Reporting reminder.** Say what we tried to establish, what we actually established, which cases it covers, and what additional fact would make it help the larger problem.

**Record:** [eight-streets proof and certificates](reports/eight-paths-L8.md); [current limitations](NOW.md).

> **Reader and date:** Local (Claude on the M5), 25 October 2026, about 21:00 GMT; instinct-led, at the owner's request; no computation, the third halt stands.
>
> **Version of the question examined:** in our own verified work, which part is the reason and which is the bookkeeping?
>
> **Answer in everyday words (an instinct):** our trap families are the clean example. The reason is the trap: once inside, the rule
> keeps the pattern going by itself and the wall keeps intruders out. The bookkeeping is the check that 28 particular cells lead into
> the trap within nine steps. Our single-width submissions (the exact values of D at 52, 56, 60 and others) are the opposite: pure
> bookkeeping, a large checked table with no reusable reason. That is why the prize kit's maintainer asked for no more of them. On
> "certificate", one analogy: a certificate is like a completed Sudoku, hard to fill in and quick to check. The checker confirms exactly
> the claim written on it, and nothing more.
>
> **Exact scope and evidence:** L919 and L935 (the trap and its families); CL629 (the maintainer's request); the twenty live submissions.
>
> **What failed, or remains unknown:** whether the reasons in our twenty verified submissions share a shape that recurs.
>
> **Status and what would make another visit useful:** Open. Next question, answerable by reading, not computing: list each verified
> submission's reason and its bookkeeping, and see which reasons repeat.

## DQ-008 — Are we watching the wrong end?

**Question:** "We always watch the cell beside the wall. What if the fate of a start is decided at the far end, and the wall cell only
reports it, late?"

**Origin:** Local's instinct, from the information-loss measurement of 25 October 2026 (L942), offered for the owner's judgement.
**Status: Open.** No investigation is claimed here.

**Why it matters.** Every test, census and certificate we have built watches the wall-side cell. If the decision is effectively made far
away, then a bound on the moment of death might be easier to state as a bound on how long the far end's messages take to reach and spoil
the wall, rather than as a statement about the wall's own history.

**What we know.** At width 40, flipping the deepest starting cell (the last recorded step) leaves the moment of death essentially unrelated
to before, while flipping the first recorded step changes it in about one pair in a hundred (L942; GC1873's qualifications apply). The
rule carries news from the far side to the wall with certainty and the other way only when unmasked (DQ-003). These are measurements and
a structural picture, not a mechanism.

**Where our understanding stops.** We have never described what the far end sends toward the wall, or how far into the row the "deciding"
cells reach for the long survivors specifically, rather than for typical starts.

**Next useful question.** For the longest-lived starts at a width, which starting cells can be changed without changing the moment of
death, and is the unchangeable set always at the far end?

**Record:** L942 and [its outcome review](reports/wolfram-agents/GPT-L942-INFORMATION-LOSS-OUTCOME.md); L947 (the twin maximizers).
Related: DQ-001 (what is packaging), DQ-003 (the one-way street).

> **Reader and date:** GPT, 25 October 2026, GC1886 / MI817, at the owner's request.
>
> **Version examined:** can the known orderly far edge explain what the watched cell must eventually do?
>
> **Answer in everyday words:** the far edge has already been described, and fixed stripes eventually repeat. But the watched cell samples a different stripe each time, one step after that stripe begins at the boundary. Knowing that each stripe eventually settles does not tell us what each new stripe does on its first birthday. This is a coordinate description, not a claim that independent new information is being created.
>
> **Exact scope and evidence:** the [full hand derivation and source review](reports/rule30-deep-questions-first-birthday.md) rederives the existing age-one obstruction in RULE30-PRIZE.md section 8.84. It also retains GC1873's distinction between trace-bit and physical-cell changes. The GC693 pair confirms that a first message can arrive at an unobserved odd time and the two rows can then merge before the next tested observation.
>
> **What remains unknown:** a relation between successive fresh layers that uses the finite starting row and prevents the required observations from continuing forever. The local opposite-neighbour condition only restates the survival test; no additional restriction has been found.
>
> **Status and next question:** Open. **Can the orderly structure farther out constrain each fresh layer before it has time to settle?** More concretely: what must one fresh layer leave to the next to keep the test passing, and can a finite start keep doing that forever? This is a refined question, not a proposed run or a new theorem. Local's original wording is retained above, with the evidence qualifications here.

> **Reader and date:** Local, 25 October 2026, about 21:25 GMT, second round; instinct-led, at the owner's request; hand reasoning only, no computation; the third halt stands.
>
> **Version of the question examined:** GPT's refinement: what must one fresh layer leave to the next to keep the test passing?
>
> **Answer in everyday words:** near the wall there is an exact, small answer, and it shows where the difficulty goes.
> 1. **The cell beside the wall is a light switch.** Because the wall is always white, the masked ("or") door on the wall side lets the
>    cell's own value straight through. So the watched cell simply flips whenever its neighbour (the second cell) is black. The test asks
>    for the switch to be ON at every even tick. So the second cell must be black either both times or neither time in each
>    (even, odd) pair of ticks.
> 2. **In a start that keeps passing, the second cell is a mirror.** While the test keeps passing, the second cell's masked door is
>    always jammed open. So the second cell always shows the opposite of what the third cell showed one tick earlier.
> 3. **So the test moves one seat outward.** Survival becomes: the third cell must hold its colour from each odd tick to the next even
>    tick.
> 4. **At the fourth seat it needs memory.** Pushing once more, the requirement on the fourth cell depends on what the third cell did a
>    tick earlier. The clean rule stops there.
>
> In GPT's classroom picture: the pupils' first days are not independent. Each first-day score is the previous one, flipped when an older
> pupil had a black second day. The requirement does not vanish. It migrates outward, and from the fourth seat it starts to carry memory.
> That fits the record's finding that the wall's full rulebook keeps growing (Q10, the visible language: "no small lift; follower
> classes grow" to length 44).
>
> **Exact scope and evidence:** points 1 to 4 follow by hand from the rule as GPT's note writes it, x(t+1,d) = x(t,d+1) XOR (x(t,d) OR
> x(t,d-1)) with x(t,0) = 0. In symbols:
> - point 1: x(t+1,1) = x(t,1) XOR x(t,2);
> - survival from 2n to 2n+2, given x(2n,1) = 1, is exactly x(2n,2) ≠ x(2n,3) (GPT's opposite-neighbour condition);
> - point 2: in a survivor, x(t+1,2) = NOT x(t,3);
> - point 3: given survival through 2n, survival at 2n+2 is exactly x(2n-1,3) = x(2n,3);
> - point 4: the condition on x(2n-1,4) is 0 if x(2n-1,3) = 1, and NOT x(2n-2,3) if x(2n-1,3) = 0.
>
> This is the running-XOR structure already in RULE30-PRIZE.md sections 8.27 and 8.66, read at the wall, so it is a restatement, not a new
> theorem. Checked by hand on GC693's own fixture (1100101): points 1 to 3 predict its survival at tick 2 and its death at tick 4, matching
> the record.
>
> **What failed, or remains unknown:** whether the requirement, carried further outward, ever stops growing. See DQ-009.
>
> **Status and what would make another visit useful:** Open. GPT's refined question now has a concrete first step. The open part is the
> memory that appears from the fourth seat outward.

## DQ-009 — How much does the referee have to remember, seat by seat?

**Question:** "If we move the referee outward from the wall one seat at a time, does the rulebook the referee must apply keep getting
longer, or is there a seat where it stops growing?"

**Origin:** Local's instinct, second round, 25 October 2026, from working GPT's DQ-008 refinement by hand. **Status: Open.** No
investigation is claimed here.

**Why it matters.** DQ-008 asked whether we are watching the wrong end. GPT showed that the far end's order does not reach the watched cell
directly. But the test itself can be carried outward: exactly, at the second and third seats, and with memory from the fourth (DQ-008,
Local's second note). The far end of the row is orderly: its stripes settle (RULE30-PRIZE.md section 8.74, where order ends at a boundary
moving like a random walk). If the referee could be carried out to that orderly region with a rulebook of bounded size, the order there
might decide the test. If the rulebook grows without bound at every seat, then watching a different seat cannot help, and that is a
precise, useful negative.

**What we know.** The rulebook at the wall itself, the full set of sequences the watched cell can show, has no small description: its
follower classes keep growing (Q10, RECORD-MAP "Visible language exact to n=44"). The first two moves outward are clean; the third
already needs one tick of memory. Nothing is known about seats farther out.

**Where our understanding stops.** We do not know whether the memory needed grows with the seat, grows with time, or both. Nor do we know
whether, near the order boundary of section 8.74, the farther cells' settled behaviour supplies exactly the memory the referee needs.

**Next useful question.** Write the referee's rule at the fifth and sixth seats by hand, and ask: does each move outward add memory, or
does some move cancel memory added by an earlier one?

**Record:** DQ-008 (Local's second note and GPT's note); RULE30-PRIZE.md sections 8.27, 8.66 and 8.74; PERIOD-TWO.md row Q10. Related:
DQ-003 (the one-way street), DQ-004 (a finite description would be a bounded rulebook).

## Returning to a question

Append a dated note under its DQ entry using this light template:

> **Reader and date:**
>
> **Version of the question examined:**
>
> **Answer in everyday words:**
>
> **Exact scope and evidence:**
>
> **What failed, or remains unknown:**
>
> **Status and what would make another visit useful:**

If the mathematics reveals that we translated the original question poorly, keep both versions and explain the difference. The purpose is to remember promising questions and learn how to ask better ones, not to make every question look successful.
