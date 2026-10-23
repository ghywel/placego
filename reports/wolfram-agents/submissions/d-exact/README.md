# Submission d-exact: the death time at width 52 is exactly 96, with witnesses at widths 56 and 60 (Local, 2026-10-23)

Lane D-exact (CHAT-LEDGER.md L805 to L821). The kit's certified bound 96 at width 52 is attained by the explicit start
0x7dc2ff6fcc4fd; the starts 0x93d4b223f5b9b5 and 0xe77a4e77b8f99b5 survive to 100 and 114 at widths 56 and 60.
- **Headlines:** `Rule30Submission.death_time_52_exact`, `Rule30Submission.width56_lower`, `Rule30Submission.width60_lower`.
  `check.json`: verdict pass, 24 declared, replay of 34 constants, standard axioms, no new axioms.
- **Imports:** `Rule30PrizeKit`, `Ruliology.CellularAutomata.Rule30ZeroBoundarySmall`, `...Rule30ZeroBoundaryWidth52`
  (the kit's own modules; not reachable from `Rule30PrizeKit` alone).
- **Timing on the M5:** `lake build Rule30Submission` 13 s; the checker a few seconds.
- The width-56 and width-60 upper bounds (W2's and W5's certificates) are not carried; see the ledger for their receipts.
- Expected outputs: bit lengths {51, 56, 60}; first even white times {96, 100, 114}; `Axioms` standard; `KernelCheck` Success.
- Byline and API fields as for the earlier submissions (HANDOVER-LOCAL.md).
