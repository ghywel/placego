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
- `essay-template.md` + `assemble.py` -> `essay.md` (SHA256 `e1facac0647c0d2ece7d83c9011e83e3960545ad7865b12b7512b7faea004d16`, after GC1832's wording qualifications and GC1830's etherLeft note); `abstract.md` (212 words, SHA256 `d6f34abb0dd1413e3b915ed445351800ab6af082bcc0e7a99a8fd319dcabfb4f`);
  `expected_numbers.py`: independent plain Python for the three illustration cells, whose Wolfram outputs (run once in the Wolfram Engine)
  match it exactly: visible columns `0,1,0,1,...` for both, the row of R31 at time 4 = R495; the rows at the trap entries, columns 1..19,
  both `0000010100000100000`, ether columns 1..6 at phase 12 `000001`; the S-chain from `[1]` and the two roots.
- `check.json`: the kit's `Check.lean` (GC1833-accepted stage, trap_pair_check.py d12487a3, 2026-10-24 23:33 BST): verdict `pass`,
  **66 constants replayed**, 40 declared, the five headlines found, ok and type-matching, on `propext`, `Classical.choice`, `Quot.sound`
  (`not_move_equivalent`: `propext`), no new axioms. Build 17.69 s, checker 4.16 s; sampled group RSS peaks 4,139,581,440 bytes (build) and
  3,912,007,680 (checker), under the 4 GiB stop by about 155 MB; the kit copy restored and verified. Packet: store
  `cited/trap-pair-check-20261024-2333/`.
- Not yet: the notebook (build_sub.wl) and its gate.

## Status
Source PASS (GC1831), essay PASS (GC1832), Check PASS (L925). Next: the notebook and its full-cell gate, for GPT's agreement, then a submission request.
