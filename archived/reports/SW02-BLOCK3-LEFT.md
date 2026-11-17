# The left side of X and Y: what it can and cannot say

*Local, L1572, 6 November 2026, at the owner's word to follow this pull before Block 5. It follows [the note on X and Y](SW02-BLOCK3-BRIDGES.md). Probes: [`tests/probes/swarm/sw02/block3/left/`](../tests/probes/swarm/sw02/block3/left/). About one CPU minute on the M5.*

**Local parks this pull; GPT scope review GC2699:** the finite tests do not prove that every finite-state route is impossible. Unrestricted left-trace realization supplies no exclusion without an additional condition such as finite support. The two small-width observations below are prior art. Status below is COMPUTED, self-check, unless it says otherwise.

## The statements

For a set of gap words A, write Q01[A] for: no finitely supported constrained start has free bits whose complement is eventually a word of A. `Q01Gap` is Q01[gaps 3 and 5]. These sit in a chain, with L_W the language at width W:

Q01 ⇒ Q01[gaps 2 to 5] ⇒ Q01[L_W] ⇒ Q01[L_(W+1)] ⇒ no right half has a finite `Psi R` ⇒ CQ01.

**GC2699 correction:** the last reduction requires the language to cover the target and resolved cases as well. If L_W means only the residual X/Y languages, Q01[L_W] alone does not discharge the gate case. A guarded sufficient statement is:

(Q01Gap AND Q01[L_X] AND Q01[L_Y]) implies CQ01,

assuming the valid target certificates, C(W), the corresponding residual-language upper bounds and the existing exclusions for eventually periodic u. The conclusion concerns every **finite** R, as in CQ01. Alternatively define L_W to include the gate and all residual/resolved trace cases before writing a single-language implication. Language inclusions give the restricted-Q01 arrows, not an omitted coverage statement. The gate and other cases remain explicit open premises.

## What was found

1. **Windows on the left constrain nothing.** Every free word has its left half `Theta f` (`Q01_iff_Theta`), so only finiteness of `Theta f` can exclude a word. This is PROVED in the kit, and this blocks a bare trace-only exclusion without a support or compatibility condition.
2. **Loops have backgrounds.** Under `Theta`, the word 25 gives a row of pre-period 1 and spatial period 728, with white runs of at most 7. The word 2 gives the ether, spatial period 7. Cycles containing E show no period within 4,000 columns.
3. **One excursion fills its past cone with disorder.** For (25)^a E (25)^b the columns stay background outside E's past cone, with the first difference 6 ticks inside the cone's edge at every depth tested, from 8 to 1,400. The interior has width k + 68 at depth k, and at 1,462 bits it compresses no better than random bits. This is evidence of spreading in the tested range, not a proof that `Theta` has no finite-state transducer. The finite spreading prediction is supported; the stronger impossibility conclusion remains unproved. A finite-state device can reproduce any fixed finite collection of traces with enough states, and neither spreading nor a narrow interface alone settles the unbounded claim. The compression test is rough: it shows no simple pattern, not a proof of chaos.
4. **The languages are thin.** X has 0.0372 bits per step at W = 39 to 41, against 1 bit for free words. Y falls from 0.0660 at W = 41 to 0.0337 at W = 60. Each drop is smaller than the last; extrapolating the drops gives a limit near 0.02, which is a fit and nothing more. For a specified nested sequence of compact subshifts, entropy decreases to the entropy of their intersection. Identifying that intersection with realizable right-half traces additionally needs a coherent all-width lifting/compactness argument; monotonicity alone does not supply it. A positive computed value at finitely many widths, or the fit, proves no positive limiting entropy. If both the identification and a positive limit were proved, uncountably many aperiodic infinite right-half traces would follow, without a finite-support conclusion.
5. **X's loop looks real at every width.** The tree of period-14 columns has 478 words at depth 1 and between about 4,000 and 20,000 at each sampled depth from 21 to 191. It neither dies nor grows exponentially to depth 200.
6. **X and Y are shallow.** In R = 993,136, column 1 flips between the two aligned phases of the ether on a prefix of at most 12 columns, with disorder beyond. The crossing 45 is that flip. M = 9 for most lock holds says the same of X. These observations motivate a shallow-trunk model for the checked crossings; they do not bound trunk depth for every row, phase or later crossing. A window at W = 41 is mostly recording what those columns can feed the trunk.

## Prior art this reproved

| What I found | Where it already is |
|---|---|
| No adjacent black in u, for every right half | Kit `Rule30CoupledGerms.u_no11` |
| Every five consecutive u hold a black, so gaps are 2 to 5: exact at W = 3, one component of 7 windows | Portal R30-20261028-e34744, `u_golden`, `u_black_among_five` |
| Forbidden gap words from a strip of columns | Kit `Rule30PeriodTwoLanguage`, widths 5 and 6; portal `Psi_free_constraints_width6_of_finSupp` |
| Labelling: a strip that stays out of the bad class has a masked periodic column, so Jen applies | Kit `Rule30PeriodFourSkeleton.Cert.sound_bad`. LOCKED versus UNRESOLVED is this idea, at width 41 |
| Constraining the free bits does not close a finite left game; what survives is positive entropy and periodic words are dense | `rule30-open` `constrained-left-halves.md`, for 001 and 011. Period two is not in it; a transfer to period two is not proved here |

What appears to be ours: the exact languages of X and Y, their block forms, the width-indexed entropies, the backgrounds of 25, and the reading of crossings as flips on a shallow trunk. The `Record searched:` line below says how far that was checked. Note for the packet: C(W) was carried by GPT as a finite-graph statement, and it should cite `Cert.sound_bad` as its small-width ancestor.

## Routes around

The unrestricted realization obstruction and the cited finite-game negatives keep their stated scopes; this experiment adds no blanket finite-state closure. Four routes remain queued in the backlog:

1. **Lean, soon:** carry the kit's width-6 language up through `Cert` to a width near 16 to 20, as an exact automaton rather than nine patterns. It is the formal form of this work and would be a submission.
2. **Hand reading of a crossing:** which input words at column 10 make E pass through the 9-column trunk, and which columns must supply them. GPT owns this one now (GC2697, the bridge-history pilot). It is the most likely place for a real constraint.
3. **The limit:** does any infinite right half cross E infinitely often? A label-restricted lift could test single cycle words far past W = 60, because it tracks only windows on that word.
4. **Bounded search:** enumerating these thin languages would reach left widths in the hundreds. It is a finite result, so it comes last.

**Failures kept.** I predicted (0.6) a gap bound at W ≤ 16; it held at W = 3, but I took it as possibly new for a moment before searching, and it is known. I wrote in L1569 that the left side was "the place to attack" these languages; it is not, in this form.

**Record searched:** `record_find` on left background, sideways, no two adjacent, white run with Theta; `known_find` on free bits, drought, forbidden with u R, white run with u R; the kit's `Rule30CoupledGerms`, `Rule30PeriodTwoLanguage`; portal sources R30-20261028-e34744, R30-20261030-60990f; `rule30-open` `constrained-left-halves.md` and its catalogue on free bits and gaps. The 77 glider and 738 defect hits were sampled, not read in full.

**GPT review GC2699:** complete note and all three probe sources read, no new run. `Rule30PeriodFourSkeleton.Cert.sound_bad` is a relevant prior-art ancestor: it forces the actual seed history into a bad class using certificate ranks and masked Jen. It is not identical in hypotheses to C(W), which first classifies every driven right-half path and does not itself invoke a finite-left exclusion. GC2698 also corrects the claimed all-length equality of X38–41 and the independent-choice block grammar. [Review and exact counterwords](GPT-BLOCK4-BRIDGE-HISTORY-20261106.md).
