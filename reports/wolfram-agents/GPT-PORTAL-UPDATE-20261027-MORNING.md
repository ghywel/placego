# Morning portal check and implications for the natural-clock question

GPT GC1938 / MI857, 27 October 2026. Live catalogue timestamp **09:44:10 UTC**,
compared with the retained 26 October 10:30:13 UTC snapshot.

## Catalogue delta

52 entries, up from 40: **12 new external IDs, no removed IDs**. Of the new
entries, 11 have Lean Verified status and one is Lean Unverified. The whole
catalogue has 50 Lean Verified and two Lean Unverified. The 12 new abstracts
were read; this is not a carrying review of all 12 proofs.

All 20 current team IDs in MAP section 5 remain listed; 19 remain Lean
Verified. One status detail changed: width-60 entry71f858 remains Lean
Unverified and its former Human Verified tag is now absent. Nineteen team
entries now carry Human Verified. The snapshot does not explain the tag
removal; do not infer rejection of the theorem. External017d83 acquired
Kit Contribution. Other changes to retained entries are display grouping.

Verifier environment is now image10, kit
`7d665044b904117af9e82328aeb90a30692b2b85`, Lean4.35.0. Both catalogue and
separate environment endpoint agree on this pin. The prior image8/0090056
state is historical.

| New ID | Subject | Public status at this snapshot |
|---|---|---|
| [c389d5](https://www.wolframcloud.com/obj/rule-30-prize/Agents/status/R30-20261026-c389d5) | The White End of Rule 30 from q = 9, by One Pumped Certificate | Lean Verified; Human Verified, Kit Contribution |
| [4d375d](https://www.wolframcloud.com/obj/rule-30-prize/Agents/status/R30-20261026-4d375d) | Short Blocks Before Long White Runs in the Center Column of Rule 30 | Lean Verified; Human Verified |
| [196859](https://www.wolframcloud.com/obj/rule-30-prize/Agents/status/R30-20261026-196859) | Long White Runs in the Center Column of Rule 30 | Lean Verified; Human Verified |
| [d611aa](https://www.wolframcloud.com/obj/rule-30-prize/Agents/status/R30-20261026-d611aa) | A Four-Category Block Grammar for the Center Column of Rule 30 | Lean Verified; Human Verified |
| [e67465](https://www.wolframcloud.com/obj/rule-30-prize/Agents/status/R30-20261026-e67465) | Partial structural results toward Rule 30 Problem 1: a truncation bridge, first kernel-checked Q001 instances, and a coupled golden-mean source constraint | Lean Verified |
| [0ef9c8](https://www.wolframcloud.com/obj/rule-30-prize/Agents/status/R30-20261026-0ef9c8) | Period-32 two-phase shielding rigidity for finite Rule 30 moving-front states | Lean Verified |
| [1b82d8](https://www.wolframcloud.com/obj/rule-30-prize/Agents/status/R30-20261026-1b82d8) | A Half-Rate Exponent Bound for Right-Diagonal Periods in Rule 30 | Lean Verified |
| [1910d0](https://www.wolframcloud.com/obj/rule-30-prize/Agents/status/R30-20261027-1910d0) | Unconditional Six-Cell and Seven-Cell Stripe-Tail Mortality and Sparse Return-Map Completion of (97, 0) in Zero-Boundary Rule 30 | Lean Verified |
| [c137e0](https://www.wolframcloud.com/obj/rule-30-prize/Agents/status/R30-20261027-c137e0) | Least Period 4 of Rule 30: a Weaker Sufficient Condition, and Why the Left Half Must Be Finite | Lean Verified |
| [230bc7](https://www.wolframcloud.com/obj/rule-30-prize/Agents/status/R30-20261027-230bc7) | Rule 30, Period 2: a Closed Trap for the Right Half Driven from the Empty Row | Lean Verified |
| [317c64](https://www.wolframcloud.com/obj/rule-30-prize/Agents/status/R30-20261027-317c64) | Rule 30: Self-Shielded Black Runs, Sharper White-Run Bounds, and Q01 as an Integer Iteration | Lean Verified |
| [b035ac](https://www.wolframcloud.com/obj/rule-30-prize/Agents/status/R30-20261027-b035ac) | Universal Spatial Transducer Annihilation, Center OR-Mask Blocking, and Left-Cone Aperiodicity in Rule 30 | Lean Unverified |

The newest unverified b035ac advertises formal results, but its actual check
says the verifier could not evaluate the notebook; its Lean URL is null.
Do not treat the abstract's assertion of verification as the portal outcome.
No prize solution is established by this delta.

## Relevant proof reading and limits

**230bc7, period-two trap.** Read the source's definitions, complete transition
and physical-window proof, empty-row entry and reduction, and transform
obstruction. The numerical certificate tables were retained, not independently
recomputed. The six `decide +kernel` checks certify an invariant 16-cell window
set and its 3/5-gap grammar against both choices of the exterior at each of
two updates. Exact finite evolution gives entry at time293, and a black gate
at sample146 makes the recurrence nonvacuous. `Q01Gap` is an additional open
hypothesis in the finite-left exclusion; it is not a proved consequence of
trap closure. The public check reports passed kernel replay of 141 constants. No local Lean replay was performed.

Read the pinned kit's complete `Rule30SpacingRenormalization`,
`Rule30SpacingGapCounterexample`, and `Rule30DrivenPrefix` modules. The
spacing-preserving second translation is impossible for an infinite recurrent
gate; a periodic 3/5-gap gate refutes a uniform reconstructed white-gap ceiling
of16. These blocks prevent two attractive but already false shortcuts.

**c137e0, period-four sufficient condition and half-infinite witnesses.** Read
the complete source, especially the actual coupling from the periodic left
half to a finite right ether-and-wall state. The natural alternating witness
uses an infinite7-periodic left side and a right side white beyond position19.
It is not a finite-seed clock. The new `Lock` condition remains an assumption
for excluding least period4. Read the pinned ether table/config definitions
and reused interface; did not re-audit every imported certificate or run Lean.

**1b82d8, improved diagonal-period bound.** Abstract and headline/check status
read, full source downloaded and retained but not carrying-reviewed. It
reports a bound with half-rate leading exponent and an iterated-log correction.
It is relevant to the right-edge ruler, but supplies no bound for the natural
centre. **317c64** likewise retained for later source review: self-shielding,
white-run improvements and an integer formulation of Q01 are the reported
claims; Q01 remains open. The other eight new entries received catalogue-level
triage only, with no blanket independent verification claim.

## Decision

Keep DQ-023, the natural-clock handover question. The next proposed experiment
is a small **cut-and-repair intervention**, with exact controls from the
half-infinite clock and a hand-derived left-only deadline, rather than another
width/lifetime census. [The concrete plan](../rule30-clock-cut-and-repair-plan.md)
contains the six starts, complete right-edit domain, falsifiable prediction,
controls, counterfactual, limits and stopping rule. It is a recommendation;
no executable has been frozen or accepted and nothing was launched.

The known discrepancy front answers the unchanged-right truncation by hand.
The proposed test asks whether changing the right side can repair that arrival
while preserving all previous centre ticks. A positive result concerns a
finite relay, not an eternal clock; a negative result closes only the stated
intervention family. Existing CQ01 computations and G239 gap-language work
are explicitly acknowledged. No heartbeat restart or submission.

## Retained evidence

Public sources: [catalogue](https://www.wolframcloud.com/obj/rule-30-prize/Agents/submissions),
[JSON](https://www.wolframcloud.com/obj/rule-30-prize/Agents/submissions.json),
[environment](https://www.wolframcloud.com/obj/rule-30-prize/Agents/api/environment),
and the linked submission source endpoints. Raw public files are outside git
in `cited/gc1938-portal-morning/`, with SHA-256 manifest. Catalogue249487 bytes,
SHA256 `dc5f1dacde429880ec22bc5e8942b2976e156f6f26b8ded79e1a97c3b0149647`.
Source230bc7 SHA256 `39c0f0376e26d86e6be1c8eeb8874f39e1fc1fd89bd9b37e78dd87a7aafd7660`;
c137e0 `94dfd146a3707dedee2122e8ca67479e7c8c7837d74327cef7c17570a8f9aaf2`.
Verified-TLS curl retrieved these after Python's default trust store failed;
no certificate-verification bypass. No authentication failure occurred.
