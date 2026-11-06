# The left side of X and Y: what it can and cannot say

*Local, L1572, 6 November 2026, at the owner's word to follow this pull before Block 5. It follows [the note on X and Y](SW02-BLOCK3-BRIDGES.md). Probes: [`tests/probes/swarm/sw02/block3/left/`](../tests/probes/swarm/sw02/block3/left/). About one CPU minute on the M5.*

**Verdict: this pull closes.** The left side gives no finite-state route to excluding X or Y. The two easy wins I hoped for are prior art. Status below is COMPUTED, self-check, unless it says otherwise.

## The statements

For a set of gap words A, write Q01[A] for: no finitely supported constrained start has free bits whose complement is eventually a word of A. `Q01Gap` is Q01[gaps 3 and 5]. These sit in a chain, with L_W the language at width W:

Q01 ⇒ Q01[gaps 2 to 5] ⇒ Q01[L_W] ⇒ Q01[L_(W+1)] ⇒ no right half has a finite `Psi R` ⇒ CQ01.

The first and last arrows are immediate, and each middle one is inclusion of languages. With C(41), the language needed is the gate's, plus X's with infinitely many E's, plus Y's. This chain is a statement of what is already implied. PROOF-SKETCH, unread by GPT.

## What was found

1. **Windows on the left constrain nothing.** Every free word has its left half `Theta f` (`Q01_iff_Theta`), so only finiteness of `Theta f` can exclude a word. This is PROVED in the kit, and it is why the coupled window idea fails at once.
2. **Loops have backgrounds.** Under `Theta`, the word 25 gives a row of pre-period 1 and spatial period 728, with white runs of at most 7. The word 2 gives the ether, spatial period 7. Cycles containing E show no period within 4,000 columns.
3. **One excursion fills its past cone with disorder.** For (25)^a E (25)^b the columns stay background outside E's past cone, with the first difference 6 ticks inside the cone's edge at every depth tested, from 8 to 1,400. The interior has width k + 68 at depth k, and at 1,462 bits it compresses no better than random bits. So `Theta` on these words is not a finite-state transducer. The prediction (0.7) held. The compression test is rough: it shows no simple pattern, not a proof of chaos.
4. **The languages are thin.** X has 0.0372 bits per step at W = 39 to 41, against 1 bit for free words. Y falls from 0.0660 at W = 41 to 0.0337 at W = 60. Each drop is smaller than the last; extrapolating the drops gives a limit near 0.02, which is a fit and nothing more. Since the languages are nested, their entropies fall to the entropy of what real infinite right halves can read. Positive limit would mean uncountably many infinite right halves keep aperiodic u outside the closed sets.
5. **X's loop looks real at every width.** The tree of period-14 columns has 478 words at depth 1 and between about 4,000 and 20,000 at each sampled depth from 21 to 191. It neither dies nor grows exponentially to depth 200.
6. **X and Y are shallow.** In R = 993,136, column 1 flips between the two aligned phases of the ether on a prefix of at most 12 columns, with disorder beyond. The crossing 45 is that flip. M = 9 for most lock holds says the same of X. So these are short trunks driven from the deep columns, not structures that run deep. A window at W = 41 is mostly recording what those columns can feed the trunk.

## Prior art this reproved

| What I found | Where it already is |
|---|---|
| No adjacent black in u, for every right half | Kit `Rule30CoupledGerms.u_no11` |
| Every five consecutive u hold a black, so gaps are 2 to 5: exact at W = 3, one component of 7 windows | Portal R30-20261028-e34744, `u_golden`, `u_black_among_five` |
| Forbidden gap words from a strip of columns | Kit `Rule30PeriodTwoLanguage`, widths 5 and 6; portal `Psi_free_constraints_width6_of_finSupp` |
| Labelling: a strip that stays out of the bad class has a masked periodic column, so Jen applies | Kit `Rule30PeriodFourSkeleton.Cert.sound_bad`. LOCKED versus UNRESOLVED is this idea, at width 41 |
| Constraining the free bits does not close a finite left game; what survives is positive entropy and periodic words are dense | `rule30-open` `constrained-left-halves.md`, for 001 and 011. Period two is not in it, but the argument carries |

What appears to be ours: the exact languages of X and Y, their block forms, the width-indexed entropies, the backgrounds of 25, and the reading of crossings as flips on a shallow trunk. The `Record searched:` line below says how far that was checked. Note for the packet: C(W) was carried by GPT as a finite-graph statement, and it should cite `Cert.sound_bad` as its small-width ancestor.

## Routes around

The finite left game is closed, but four routes remain, all in the backlog:

1. **Lean, soon:** carry the kit's width-6 language up through `Cert` to a width near 16 to 20, as an exact automaton rather than nine patterns. It is the formal form of this work and would be a submission.
2. **Hand reading of a crossing:** which input words at column 10 make E pass through the 9-column trunk, and which columns must supply them. GPT owns this one now (GC2697, the bridge-history pilot). It is the most likely place for a real constraint.
3. **The limit:** does any infinite right half cross E infinitely often? A label-restricted lift could test single cycle words far past W = 60, because it tracks only windows on that word.
4. **Bounded search:** enumerating these thin languages would reach left widths in the hundreds. It is a finite result, so it comes last.

**Failures kept.** I predicted (0.6) a gap bound at W ≤ 16; it held at W = 3, but I took it as possibly new for a moment before searching, and it is known. I wrote in L1569 that the left side was "the place to attack" these languages; it is not, in this form.

**Record searched:** `record_find` on left background, sideways, no two adjacent, white run with Theta; `known_find` on free bits, drought, forbidden with u R, white run with u R; the kit's `Rule30CoupledGerms`, `Rule30PeriodTwoLanguage`; portal sources R30-20261028-e34744, R30-20261030-60990f; `rule30-open` `constrained-left-halves.md` and its catalogue on free bits and gaps. The 77 glider and 738 defect hits were sampled, not read in full.
