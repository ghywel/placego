# Rule30ErrorEdge: the error edge of two configurations

One module, `Ruliology.CellularAutomata.Rule30ErrorEdge`, importing `Rule30AgedLeftDiagonals`. For two arrays with the
left-diagonal recurrence, with the error edge the lowest wheel on which they differ: agreement below the edge is kept
(`agree_step`, `agree_after`, `edge_le`), the arrays agree at the edge one tick later exactly when the wheel below it is
black (`heal_iff`, `edge_stall`, `edge_heal`), and after a heal the wheels above the old edge obey `white_above`,
`black_two_above` and the six laws `jump_two` … `jump_seven` (after a jump of exactly 2 the new parent is white, after 3
black, after 4 black one tick later, after 5 with a white new parent black one tick later, after 6 or 7 with a white new
parent white one tick later). No literals; the proofs unfold the recurrence on a window and decide Boolean identities.
Builds in about two seconds; `Check` passes with thirteen headlines, 56 constants, standard axioms. Portal entry: to be
added by Local on posting.
