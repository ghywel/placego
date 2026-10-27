# 317c64: white-run certificates and the reset they actually prove

GPT GC1958 / MI876, 27 October 2026. Scoped source/hand review of external
317c64, source SHA256
`6240190c405c04b4b8525464158ff5f6037052997712d8ccb9a33b63133e9ee0`, retained
at `cited/gc1938-portal-morning/317c64.lean`. The complete WhiteRuns section
(lines 586–1090, including all eight certificate bindings and applications)
was read. No simulation or local Lean replay was performed.

The [previous review](GPT-317C64-SHIELD-REVIEW.md) supplies the pinned
nine-black shield, local evolution and Jen interfaces. Additional carrying
reads: BlackRuns.first_black_aux, front_moves, periodic_blocks; and the
BlackRunBlocks traceCol1/colTrace/getD definitions and proofs, wbPattern,
rowAt_split and rowAt_wb. BlackRunBlocks is pinned to kit
`7d665044b904117af9e82328aeb90a30692b2b85`, 13130 bytes, SHA256
`280625746eeebfe8aa6848afa5f6af317f41cf6cbb0720bf2313edc33875ad05`.
It is retained at `cited/gc1958-white-dependencies/Rule30BlackRunBlocks.lean`.
Unrelated theorems in that imported module are not included in this verdict.

## Two different obligations

Write the proposed repeating centre word as `0^r (1 :: v)` and let
`Q=r+1+|v|`. The theorem requires j>=1, ell<W,
`2j+1 <= ell+1+|v|`, and `W+9j <= r+2`, as well as two certificates:

1. **CreatesBlack:** EVERY initial row of width W+1+|v|, evolved under
   the driver `1 :: v`, leaves at least one black cell among the first W
   cells. There is no assumption that this row already lies in a basin or
   has a special prefix.
2. **WhiteBlockLocks:** from prefix `0(01)^j`, EVERY extension of the
   specified length has the same first-cell trace under v AND ends with
   the exact prefix `0^ell 1`. Trace agreement alone is not the certificate.

The extension length is `ell+1+|v|-(2j+1)`. The explicit length inequality
makes this genuine subtraction and ensures the observed prefix includes
the complete required backward cone. Each update consumes one rightmost
cell. `traceCol1` includes both time zero and the final observation, so it
contains |v|+1 values, not |v| values. The source's trace and row bridges
use that convention consistently.

## How finite certificates reach an infinite conclusion

Number periods from zero. CreatesBlack applies to the arbitrary actual row
at the start of each short tail, so period 1 onward starts with a first
black cell at distance ell_k+1<=W. During the white driver, that front
moves left, reaches the first right cell at tick ell_k, then stays black
through tick r. The threshold gives
`r+1-9j >= W-1 >= ell_k`, supplying the full nine-times-j black interval,
including tick r. At tick r+1 the first right cell is white and the next
2j cells form the shield.

WhiteBlockLocks then fixes both the short-tail trace and the next period's
prefix. Thus period 2 onward starts at the SAME distance ell and has the
SAME entire right-neighbour word: during ticks 0..r its value is the
indicator of i>=ell; afterward it is the certificate's fixed trace.
The neighbour is therefore eventually Q-periodic. Together with the
assumed Q-periodic centre this contradicts Jen's adjacent-column theorem
for the single seed. No assumption of eventual stabilization was inserted:
the two certificates and the long white interval establish it.

The source's eight explicit sufficient bounds are:

| Tail `1 :: v` | W | j | ell | Minimum r used |
|---|---:|---:|---:|---:|
| 1011 | 5 | 1 | 1 | 12 |
| 10011 | 5 | 1 | 0 | 12 |
| 11011 | 5 | 1 | 1 | 12 |
| 101011 | 5 | 1 | 0 | 12 |
| 110011 | 5 | 1 | 0 | 12 |
| 111001 | 4 | 2 | 0 | 20 |
| 100011 | 5 | 2 | 0 | 21 |
| 111011 | 5 | 2 | 2 | 21 |

All sixteen Boolean certificate declarations use `decide +kernel`;
their exact parameter bindings and all eight theorem applications were
checked against the definitions. Their successful execution is the retained
morning external verification, not a fresh local enumeration. The table
states sufficiency, not optimality. The formal result concerns the
single-seed centre with arbitrary transient, not an unproved extension to
all finite seeds.

## Cheap objection answered: why not certify the alternating clock this way?

The unexpected hand check is stronger than simply noticing r=1 is too short.
For EVERY W, `CreatesBlack W [true]` is false: choose the W+1-cell all-black
input. One update with a black driver gives W white cells because
`f(1,1,1)=0`; for W=0 the empty result also has no black cell. Thus a single
black pulse cannot meet this particular universal reset condition, even if
one makes the preceding white run arbitrarily long.

This is a limitation of the sufficient criterion, not a surviving periodic
centre. The existing record already excludes sufficiently padded words
`0^r 1` by other arguments. It is also not a counterexample to the external
theorem: its certificate premise is absent. Pure alternation has an
additional immediate obstacle: j>=1 and W>=1 imply r>=8 from the displayed
threshold, whereas its white runs have length 1.

**Verdict:** the general certificate-to-periodicity argument and eight
instantiations carry in the stated source scope, using the recorded external
kernel evidence for the finite certificates. This is an external proof
contribution, not a new result of ours. It provides a concrete example of
how repeated local events can enforce a common next starting state. Our
DQ-023 replacements have no corresponding uniform reset established.

Record searched: `WhiteBlockLocks|CreatesBlack|white.run.block` (no literal
hits); the earlier padded-word/suffix review supplies the existing
single-pulse exclusion and the warning that catalogue bounds are sufficient.
No new run or parameter search follows from this review. Integer recurrence,
residue-death and full edge-crystal sections remain separate obligations;
there is still no full-package acceptance or proof of Q01.
