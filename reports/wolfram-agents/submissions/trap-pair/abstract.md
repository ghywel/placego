For the finite right halves $R_{31}$ (black cells $1..5$) and $R_{495}$ (black cells $1..4$ and $6..9$; it is the row of $R_{31}$ at time $4$), the sideways row $\Psi R$ of the kit's `Rule30PeriodTwoSideways` has infinitely many black cells (`Rule30Submission.CQ01_R31`, `CQ01_R495`): two explicit instances of the coupled question `CQ01`, whose general form excludes eventual period 2 and whose milestone for the empty right half is open. Moreover $\Psi R_{31} = \Psi R_{495}$ (`Psi_eq`), and the two are not joined by the right-end moves (`not_move_equivalent`).

Both driven right halves enter the kit's ether-and-wall trap: the alternating column is the column $B_4$ of the kit's $7 \times 4$ ether, and at time $9$ (resp. $5$) columns $1..6$ carry the ether and columns $7..19$ are one of the kit's $109$ wall states, decided by the kernel. The kit's `trap_invariant` keeps the ether for ever, so the visible column is the parity of the step (`u_R31`), and the kit's absorption route `not_finSupp_Psi_of_eventuallyPeriodic` applies.

The right-end moves are the inverse of the kit's terminal rewrites $011 \to 01$, $101 \to 11$; on cells read from the last black cell they have a computable chain root, invariant under moves, and the two roots differ.

Nothing is claimed about `CQ01` in general, the empty right half, or Problem 1.
