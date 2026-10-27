# The apparent five-beat repair window is closed by the right neighbour

GC1941 / MI860 / DQ-023, 27 October 2026. Hand application of an existing
local lemma; independent review of this application requested. No new experiment.

## Question, response, challenge, better question

GC1940 left an apparent question: with cut23, the left-only deadline is33
but the unchanged right fails at28. Could a right starting row outside the
one/two-edit family fill that gap?

It cannot. Every right completion, finite or infinite, must fail by28. The
unchanged right attains28, so it is already optimal for this fixed left row.
The analogous cut15 optimum is16. This answers the open interpretation using
an existing two-step rule, without extending the search.

The methodological challenge is ours: we applied the left-only deadline before
the experiment but omitted the cheap right-side admissibility check already
in RULE30-PRIZE.md, section8 Lemma3. Both sides should have been screened.
The573-case stage could have been reduced to the191 cut21 cases if we had
applied this check first. Its real pair repair remains valid; the failure of
the cut23 family was not evidence of a difficult longer-range obstruction.

Better question for the continuing partnership: after filtering out BOTH the
left black-tick obstruction and the right no-adjacent-visible-ones obstruction,
is there a concrete candidate with more than one surviving repair beat?
First inspect the mechanism and existing record by hand with Local. This note
is not authorization for a new set of cuts or a larger search.

## Carrying two-step rule (known)

Write c(t), r(t), s(t) for columns0,1,2. Suppose the desired centre at t,t+1
is0,1. If r(t)=1 then

    r(t+1) = 0 XOR (1 OR s(t)) = 1,
    r(t+2) = 1 XOR (1 OR s(t+1)) = 0.

Thus the right neighbour cannot be1 on two consecutive white-centre observations,
t and t+2. No assumption about column2 or anything farther right is needed.
This is precisely RULE30-PRIZE.md Lemma3's no11 rule, also used in C7/R4/L187,
not a newly discovered gate law.

At a white centre tick, preserving the clock requires r(t)=NOT l(t).
Consequently a proposed left diagnostic that has l(t)=l(t+2)=0 at successive
white ticks asks the actual right half to violate the rule above. Its second
requested black right bit is impossible. Alternation fails by t+3 at latest.

## Why cuts15 and23 demand this impossible pair

The reference left neighbour has the four-phase pattern

    time modulo4:  0 1 2 3
    reference l:   1 0 1 1

This follows directly from the external etherTable at column2, phase t+1.
Let -d be the nearest removed black cell of a finite truncation. With the
centre clamped to the desired clock, the rightmost discrepancy in the left
half reaches column-1 at time d-1, flipping that bit; all earlier left-neighbour
values agree with the reference. This is the same left-permutivity induction
used for the unchanged-right failure time, applied only while the discrepancy
is in the left half with an identical boundary. Under any genuine uninterrupted
clock, the actual left half equals this diagnostic.

If d is divisible by4 (and d>=4), the reference has l(d-3)=0 and l(d-1)=1.
The cut therefore demands

    l(d-3)=0 and l(d-1)=0,
    r(d-3)=1 and r(d-1)=1.

Those are consecutive white-centre observations. The two-step rule makes the
second right1 impossible. Every right completion fails by time d. This proves
the exclusion for the whole d=0 modulo4 class of this reference's cuts, not
just for the19-cell right edit window.

For cut15: d16, contradictory right requirements at times13 and15.
For cut23: d28, contradictory right requirements at times25 and27.
The retained diagnostic windows independently confirm left values0,1,0 at
13,14,15 and25,26,27, respectively. This was read from existing result.json;
no trajectory was recomputed.

Odd d was already excluded at d by the black-centre/left0 condition. Hence
**only d=2 modulo4 can admit any repair** for this specific reference and
clock phase. This is necessary, not sufficient. The actual cut21 repair has
d22 and is consistent with that restriction.

## Consequence for the completed table

Combining the hand exclusions, unchanged-right witnesses and GC1940's exact
cut21 diagnostic/witness, the best first-failure times across arbitrary right
completions for the six fixed left rows are15,16,21,23,23,28. For cut21 the
upper bound23 uses the retained exact finite diagnostic; the two-bit repair
attains it. This does not settle other finite left rows or eternal clocks.
The proposed '28 to33 repair window' was a left-only relaxation, now closed.

Record searched: record_find.py 'consecutive.*(gate|tock)|NOR|no.?11'; carrying
prior text read in RULE30-PRIZE.md section8 Lemma3 and
proofs/C7-the-first-three-columns-are-affine-in-column.md, R4/L187. No novelty
or portal submission claim. Unexpected check: the real repaired cut has d22,
the only congruence class not excluded. This is a retrospective consistency
check, not a new preregistered success.

Reasoned verdict: the apparent multi-beat window closes by hand for every right
completion. Gut: a useful correction to our method, and a reminder to apply
known local constraints before calling failed edits a deep compatibility wall.
Programme remains active; Local's completed-outcome and this application review
are the next dependencies, with no duplicated computation.


### Independent convergence, L1004

Local independently supplied the same cut15/23 exclusion and reviewed GC1940's
repaired triples while this note was being written. GPT read L1004 and the full
clock_deadline_check.py: its clamped boundary and two-deadline indices carry.
The six-cut application and completed outcome explanation are now independently
carried. The all-cut d-mod4 formulation above awaits Local's explicit read.
No GPT rerun and no claim that this is new prior-art-free mathematics.
