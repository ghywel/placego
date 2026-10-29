#!/usr/bin/env python3
"""paired_column_runs_census.py: every periodic point on a ring of 3..18 cells against Theorem B's bound (L1084).

RUN-ON: cpu, under a second. On a ring every column of a periodic point shares its least period P, so every
maximal white run of row 0 must have length <= 2P - 2 (zero_run_le), and every odd one of length >= 3 at most
2P - 5 (odd_zero_run_le). Prediction: no violation; the bound attained at small P. Counterfactual: a violation
refutes the formal statement's reading. Result (2026-10-29): no violation; attained at P = 3 (the period-3 ether
(000011111001)^inf, runs of 4) and P = 4 ((0000001)^inf, runs of 6). Cross-checked at n = 10 against a naive
period count (38 periodic states, periods 1, 5, 15).
"""
