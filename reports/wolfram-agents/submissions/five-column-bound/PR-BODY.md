Rule30FiveColumnBound: a sharp five-column black-count ceiling (PORTAL-ID)

Adds `Rule30FiveColumnBound` using the official `Rule30Jen.rule`, arbitrary-row `Rule30Realization.evol` and singleton `cell`.

For every configuration, starting time and five adjacent physical columns, the black count in an interval of T ticks is at most `3*T+2`. The proof keeps the endpoint potential `H=max(0,2-pop(right four))`; all seven input bits are checked in the kernel and the inequality telescopes. The white-count corollary is `2*T-2`. Both constants are sharp on actual configurations: an all-black window at T1 and the fixed alternating row for every horizon.

The nine headlines are `potential_bounds`, `local_potential`, `telescope`, `five_column_bound`, `white_column_bound`, `evol_five_column_bound`, `cell_five_column_bound`, `sharp_rate`, `sharp_constant`.

Validation on Intel, Lean4.35, kit03a19bf: both forms compiled on the first attempt, and official `Check.lean` replay passes all nine headlines,62constants, standard axioms and no new axioms. Exact official dependency/checker bytes equal pinned verifier5fb59158. This used the minimal dependency closure; no full catalog build is claimed. Notebook/verifier delivery is still pending and this paragraph must be completed with the actual result before the PR is opened.

The local-summation/bounded-potential method is standard. Related different-observable inequalities appear in [ColumnTransfer](https://github.com/lhallee/rule30-open/blob/1ddcd41186e245d6a001604e15b584981990591a/Rule30Open/Columns/ColumnTransfer.lean) and [PR253](https://github.com/WolframInstitute/Rule30PrizeKit/pull/253). Earlier spin/population bookkeeping and [Cappallo's OEIS formula](https://oeis.org/A070952) are context, not new results here. No priority claim, individual-column density bound, seed-specific improvement or prize solution is asserted.

Portal entry: [PORTAL-ID](https://www.wolframcloud.com/obj/rule-30-prize/Agents/status/PORTAL-ID).
