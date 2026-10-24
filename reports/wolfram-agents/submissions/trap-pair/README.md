# Submission trap-pair (Local, 2026-10-24; SOURCE FOR REVIEW, not checked, not submitted)

Two explicit instances of the kit's coupled question `CQ01`, by the kit's ether-and-wall trap and absorption route, and a collision
of `R -> Psi R` outside the right-end moves. Record: CHAT-LEDGER.md L919 to L922; PROOFS.md waiting room L919 (HAND/PROVED by
GPT's carrying read, GC1828); GC1825 corollary.

- `Rule30Submission.lean`: the module (183 lines, 9141 bytes, no double quote or backslash; SHA256 `27f799f47eecf22f138967ac27ccbc14ab0dffb20f55f5dc29be800aa6b44fd6`).
  Imports `Rule30PrizeKit` and `Ruliology.CellularAutomata.Rule30PeriodTwoSideways` (which brings Rule30Ether and
  Rule30PeriodTwoCoupled). Uses the kit's `trap_invariant`, `drv_isR30`, `drv_col0`, `ether_congr`, `wallStates`, `rowOf`,
  `u`, `Psi`, `not_finSupp_Psi_of_eventuallyPeriodic`.
- Proposed headlines (claim partial): `Rule30Submission.CQ01_R31`, `Rule30Submission.CQ01_R495`, `Rule30Submission.Psi_eq`,
  `Rule30Submission.not_move_equivalent`, `Rule30Submission.u_R31`.
- Development compiles (disclosed): `lake env lean` on drafts of this file in the pipeline kit (cc1e0e0), four runs under a 300 s CPU
  limit, each under 20 s wall; `#print axioms` on the headlines: `propext`, `Classical.choice`, `Quot.sound` (`not_move_equivalent`:
  `propext` only). No accepted Check, build or notebook yet.
- Not yet written: `essay.md`, `abstract.md`, the notebook (build_sub.wl) and its gate.

## Status
Source for GPT's review (L922). Next, after acceptance of the exact hash: the kit's Check.lean pass, then the essay and notebook.
