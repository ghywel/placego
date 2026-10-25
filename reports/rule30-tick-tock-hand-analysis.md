# Tick Tock: an exact cancellation and the discrepancy it leaves

GPT, 25 October 2026. GC1889 / MI818. Owner-requested mathematical continuation after Local L952–L953.

**Status:** hand-derived working note, awaiting a targeted independent read of the depth-five cancellation and discrepancy recurrence. No simulation, algebra program, census or Lean run. The periodicity obstruction is established prior work; the small expansions below are not presented as a novel theorem or a prize advance.

## What the words led to

Local's answer makes the two beats mathematically different. At every **tick**, the watched cell must be black. At each intervening **tock**, it can be either colour. For a hypothetical finite survivor, those tocks cannot eventually settle into any repeating pattern.

I followed the tocks through the next few cells by substitution. The surprising simplification is at the fifth cell: **at each tick it has exactly the same colour as the third cell**. That answers one part of DQ-009. Moving the test outward does not merely add more and more visible dependence; some expressions cancel.

But the third and fifth cells can differ at the tocks. That difference has an exact description in terms of three successive tocks. If the differences eventually repeated, the tocks themselves would eventually repeat. Therefore a hypothetical finite survivor requires the between-tick discrepancy to remain non-eventually-periodic too.

The lesson for the owner's compression question is specific: agreement at every inspected tick is not agreement of the full relevant dynamics. Here we can identify precisely the extra sequence that would have to be retained. We have not ruled out a different, more effective compression.

## Model and conventions

Use the zero-boundary auxiliary half-line, not the unconstrained full-line prize system. Depth increases away from the wall. A black cell is 1, a white cell 0. Write XOR for exclusive or, OR for inclusive or, AND for conjunction, and NOT for colour reversal.

    x(t,0) = 0
    x(t+1,j) = x(t,j+1) XOR (x(t,j) OR x(t,j-1)),  j >= 1.

Assume the survival condition x(2n,1) = 1. Define:

    b_n = x(2n+1,1)            the nth tock
    E_j(n) = x(2n,j)          cell j at tick n
    O_j(n) = x(2n+1,j)        cell j at tock n.

The formulas below hold for an eternal survivor, without assuming finite support. Each finite part also holds for an actual row passing all the ticks used in its backward-in-space reconstruction. For the complete six-cell table at index n, passing ticks through time 2n+6 suffices; this is a safe common horizon, not a claim that every table entry needs that much. All indices start at n = 0; no negative-time sample is used.

Reading the update outward gives the two exact recurrences:

    E_(j+1)(n) = O_j(n) XOR (E_j(n) OR E_(j-1)(n))
    O_(j+1)(n) = E_j(n+1) XOR (O_j(n) OR O_(j-1)(n)).

These are algebraic reconstruction identities. Their references to later tocks do not mean that the physical system reads its future. The prescribed trace is being used to reconstruct the row that produces it.

## Six cells, derived by hand

In each row of this table, u = b_n, v = b_(n+1), w = b_(n+2).

| Depth j | At the tick, E_j(n) | At the tock, O_j(n) |
|---|---|---|
| 0 | 0 | 0 |
| 1 | 1 | u |
| 2 | NOT u | NOT u |
| 3 | u | v |
| 4 | NOT v | (NOT u) AND (NOT v) |
| 5 | u | w XOR (u AND NOT v) |
| 6 | NOT (u XOR v XOR w) | (NOT w) OR ((NOT u) AND (NOT v)) |

The first three depths recover Local's switch, hold and mirror statements. In particular, the third cell's tock equals its next tick. Local's corresponding formula involving time 2n-1 is used only for n >= 1; the table avoids that initial-index issue.

The fourth cell follows immediately:

    E_4 = v XOR (u OR NOT u) = NOT v
    O_4 = v XOR (v OR NOT u) = (NOT u) AND (NOT v).

The fifth tick is the useful cancellation:

    E_5 = ((NOT u) AND (NOT v)) XOR ((NOT v) OR u) = u.

To check the last equality without a truth-table program: if u is black, the first term is white and the second black. If u is white, the two terms are both NOT v and cancel. So the result is u in either case.

At its tock:

    O_5 = (NOT w) XOR (((NOT u) AND (NOT v)) OR v)
        = (NOT w) XOR ((NOT u) OR v)
        = w XOR (u AND NOT v).

For the sixth tick, the two occurrences of the AND term cancel in the identity that XOR of AND and OR equals XOR of the two inputs:

    E_6 = w XOR (u AND NOT v) XOR (u OR NOT v)
        = NOT (u XOR v XOR w).

For the sixth tock, split by u,v. When both are white, O_4 is black and the result is black. In all other cases direct substitution gives NOT w. That is the final expression in the table. This case split is by hand, not an executed enumeration.

## The discrepancy retains the unresolved rhythm

Define d_n to be 1 exactly when cells three and five disagree at the nth tock. They already agree at every tick. From the table,

    d_n = O_3(n) XOR O_5(n)
        = v XOR w XOR (u AND NOT v)
        = w XOR (u OR v).

Equivalently,

    b_(n+2) = (b_n OR b_(n+1)) XOR d_n.

In words: without a discrepancy, the next tock is black if either of the previous two tocks was black. A discrepancy reverses that answer.

**If discrepancies eventually stop, the tocks become constant.** After the last discrepancy, a pair of white tocks remains white forever. Any other pair becomes two black tocks after at most two further updates and stays black. So exact eventual agreement of the third and fifth columns is incompatible with a finite eternal survivor.

**Stronger: if discrepancies are eventually periodic, the tocks are eventually periodic.** Suppose the discrepancy repeats with a fixed period after some time. To determine the next tock, we need only the previous two colours and our position in that repeating discrepancy pattern. There are finitely many such combined states. Their evolution is deterministic, so one repeats, and thereafter the output repeats. This is a finite-state argument on the two-bit recurrence, not a computation or a claim that the original Rule 30 evolution is finite-state.

Thus a hypothetical finite eternal survivor requires d_n itself to be non-eventually-periodic. This says neither that discrepancies have positive density nor that their gaps have a uniform bound. It also does not show that such a sequence cannot arise.

## Why periodic tocks are impossible for a finite survivor

This is Jen's periodicity obstruction, already used by Local L953. Its specialization here has a short proof which also pins the boundary convention.

If b is eventually periodic with period p, then the full watched column, consisting of black ticks interleaved with b, is eventually periodic with period 2p. The boundary column is identically white. Reading the rule outward,

    x(t,j+1) = x(t+1,j) XOR (x(t,j) OR x(t,j-1)),

propagates the same period and the same onset time from two adjacent columns to the next. Induction makes every depth periodic with that same period from that same time. In particular, the entire half-row at the onset and one period later is identical.

But a nonempty finite half-row cannot return: its deepest black cell moves one depth outward at every step. A survivor is nonempty because its watched tick is black. We have a contradiction. This is the existing periodicity propagation plus edge-speed argument; it is not new prior art.

The finite-support assumption enters here. It did not enter the six-cell algebra. Without it, periodic examples really exist, as the controls below show.

## Hand controls and limits

**Always-black tocks.** The half-row alternating black, white, black, white outward from depth 1 is a fixed configuration beside the white wall. It gives b always black and d always white. It has infinitely many black cells. The table and recurrence agree; finite support is essential to the exclusion.

**Always-white tocks.** Depth 1 alternates black and white, while from depth 2 outward the row is the fixed pattern black, white, black, white. Direct substitution verifies this infinite-support solution too. It gives b and d always white. A regular metronome is algebraically possible, but not from the required finite beginning.

**Unexpected nonconstant local control.** Take three tocks with colours white, black, white. The table prescribes the first six cells of the current tick as 110000, written from the wall outward. A single literal application of the rule, done by hand, gives the next first five cells 01100. Thus cells three and five agree at the tick (both white) and disagree at the tock (black versus white). The discrepancy formula also gives 1. No claim of an eternal finite survivor is attached to this finite local check.

The table's cancellation does not imply that every outward move reduces memory. The complete fifth-cell pair still uses later tocks, even though its tick component simplifies. Nor does equality at separated spatial positions constitute a collision between complete states. No spatial cut is licensed by the table: a proposed cut must preserve both phases and the neighbouring inputs that drive them.

## What this does and does not answer

**DQ-009:** there is a genuine cancellation at the fifth tick. A claim that every individual expression must gain dependence at every outward step would be false. A globally bounded rulebook has not been found.

**DQ-004 / DQ-010:** a compressed description that identifies the third and fifth cells using only ticks loses d. The discrepancy cannot be replaced by an eventual repeating clock under the finite-survivor hypothesis. Other abstractions, inequality arguments, all-family proofs and descending reductions remain possible. This is not a no-go theorem for finite certificates or for the owner's compression idea.

**DQ-011:** the tick promise does not force a fixed sign reversal at every tock. Its freedom is shifted into an exact discrepancy signal. We have identified what this particular simplification must carry, rather than proved that it can be discarded.

The next mathematical question is: **does the rest of a finite row place any additional restriction on this discrepancy sequence?** The two-bit recurrence alone allows an arbitrary discrepancy input and does not enforce the finite white tail. Until the outward reconstruction's finite-support condition is used, this is a change of description, not a contradiction.

A useful follow-up would need a relation that survives the full outward propagation, or a justified simplification of that propagation. Merely expanding more cells without such a question risks recreating the earlier growing-rulebook route. No further expansion or numerical search is proposed here.

## Source and review record

Read L951, L952 and L953 and all their tracker additions through commit 55abaaaf; RULE30-PRIZE.md section 8.13 in full for the carrying periodicity proof; the existing GC1886 first-birthday note and GC1883 merging review; Q10's scope and the closed GPU epoch. Record searches used running-XOR, decimation and Tick Tock terms, then targeted third/fifth-column terms. These locate earlier reconstruction and failed decimation shortcuts; they do not establish novelty for these small identities.

The owner's present instruction excludes compute for this pass. No old startup enumeration was rerun, and no startup PASS is claimed. Tools were used only to read, search and write the record and communicate it. The equations, case splits, controls and finite-state implication were worked by hand.

Targeted independent read requested from Local: check the fifth-cell pair, the discrepancy identity, and the periodic-input implication with the exact zero-wall and finite-support hypotheses. Until that read, these extensions remain a hand-derived working note. No prize, board or PROOFS status is changed.

## Owner follow-up: an uneven event clock (GC1890, 25 October 2026)

The owner asks whether unequal tick/tock lengths might explain the agreeing-tick/disagreeing-tock picture. Distinguish the update index from physical duration and from an event count. G98 already establishes that stretching global update durations preserves the ordered configurations; different local update schedules would change the system. Spatial order/asymmetry alone does not provide a second update clock.

For the third/fifth equality observable, disagreement is possible only at odd updates. Every disagreement lasts one update, and the agreement intervals between consecutive disagreements have odd lengths. Reading only colour changes collapses this to a repeating alternating event word, but the discarded waiting times carry the unresolved variation. If the successive disagreement gaps were eventually periodic, concatenating those finitely repeating gap blocks would make the physical-time discrepancy sequence eventually periodic, hence d eventually periodic, contradicting the conditional result above for a finite survivor. Under that hypothesis there are infinitely many disagreements; otherwise d would eventually be zero. This is a hand run-length argument, not a census or a bound on the gaps.

The watched black/white trace has the same isolation pattern for whites, but it is a different observable. Neither gap sequence is proved to satisfy an additional finite-tail relation. DQ-013 asks whether the waiting times reveal such a relation; no computation is proposed.

## Independent read adopted (GC1891)

Local L954 at 1d2483cde34cf4a7752e038dd0baac2239dac230 independently carries the six-cell table, discrepancy identity and periodic-input implication, including the odd-wait consequence. The pending-read language above records the original submission state. GPT's subsequent review of Local's conductor extension and one owner-authorized bounded Intel test are in [the conductor review](rule30-tock-conductor-review.md). Neither read supplies the missing all-width finite-tail contradiction.
