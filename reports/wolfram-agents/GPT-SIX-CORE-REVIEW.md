# Six-tail cores and the 74-phase refinement

GPT, GC1861/MI794, 2026-10-25. **Scoped source/hand PASS.** The actual
six-tail core proofs now discharge GC1859's remaining six-tail premise.
The known kit theorem excludes eventual `0^r u` for every Boolean tail of
length at most six and every r>=77; its endpoint refinement improves the
common threshold to **r>=74**. Both cover every column, transient and
configuration with a leftmost black cell, with an unrestricted right tail.
This is adoption of existing source, not a new proof or a kernel replay.

Pin: `3eca23c0a9fa6b153313655e6d51835406c2d06e` of
[Rule30PrizeKit](https://github.com/WolframInstitute/Rule30PrizeKit/tree/3eca23c0a9fa6b153313655e6d51835406c2d06e/lean/Ruliology/CellularAutomata).
Read every semantic declaration and proof body of four new sources:
SixTailBackward (1,347 lines), SixTailEndpoints (509), SixTail (57) and
SixTailSharpened (105): 2,018 lines total. Large decimal data were replaced
only in the reading view; all raw arrays were parsed separately. Rechecked
the full SixTailReduction (108), BackwardVacuum (95), and the restricted-tube
interface/body already carried in GC1853/GC1860, including WhitePulse's
inclusive early-white/prefix boundary. GC1860 supplies the actual FiveTail69
input. Record searched: `SixTailBackward SixTailEndpoints SixTailSharpened`;
no hit, including ledgers. Public catalogue at 05:25:24Z: unchanged 38 entries.

## Sixteen backward-vacuum cores

| Core | K | N | Stated padding threshold |
|---|---:|---:|---:|
| 100001 | 11 | 12 | 74 |
| 100011 | 5 | 0 | 71 |
| 100101 | 7 | 4 | 71 |
| 100111 | 8 | 5 | 71 |
| 101001 | 8 | 8 | 71 |
| 101011 | 5 | 0 | 71 |
| 101101 | 10 | 0 | 73 |
| 101111 | 6 | 6 | 71 |
| 110001 | 14 | 14 | 77 |
| 110011 | 5 | 0 | 71 |
| 110101 | 7 | 2 | 71 |
| 110111 | 8 | 0 | 71 |
| 111001 | 5 | 0 | 71 |
| 111011 | 5 | 0 | 71 |
| 111101 | 12 | 9 | 75 |
| 111111 | 6 | 2 | 71 |

Each chain is over the fixed block `0^N tail`, with Q0=0 (EMPTY predecessor
set) and Q(N+6)=1 (the singleton VACUUM state, not the black state 1).
Every step checks both far bits over all encoded source states. These are
predecessor implications; exact equality with the entire preimage is not
needed by the soundness proof. Ending the actual strip in vacuum would
propagate membership backward into the empty set, a contradiction.

The block sits at the END of the long white run: its start is T+(r-N) and
its end is T+(r+6). All r>=N use the same fixed certificate. The resulting
nonzero end strip contains a black cell that reaches the observed boundary
during the next early-white phase. The source requires
`r >= max(N, 10*6+11, K+9*(6+1)) = max(N,71,K+63)`.
The table matches these sufficient thresholds. No forward full-set
stabilization or enumeration of all r is assumed, and the initial strip
is arbitrary.

Hand unexpected alignment control: for core100001, N=12 and r=74, the
certified 18-input block must start at T+62 and end at T+80. Starting at T
would wrongly place its first black input at T+12, when the proposed driver
is still white. The actual proof aligns the tail at T+74. Shared literal
Q chains for 100011/101011/110011/111011 are consistent: Q0..Q3 are empty,
so their differing early driver letters occur only in vacuous target-empty
implications. This observation does not claim an additional suffix theorem.

## The two endpoint refinements

SixTailEndpoints replaces only the two largest thresholds:

| Core | Old backward K/N/r | Endpoint K/L/r | Forced OR word |
|---|---|---|---|
| 110001 | 14/14/77 | 12/14/74 | `0^(r-2) 1^8` |
| 111101 | 12/9/75 | 10/3/72 | `0^r 111101` |

The physical prefix theorem independently forces an empty K-cell prefix
at every period boundary. Z contains zero and is forward-invariant under
white input, so actual Z membership is established before restricted
predecessor checks are applied. Forward S sets start at S0=Z; tail P checks
run backward from P6=1 at the next empty boundary, with Q0=P0. The Q chain
ends at QL=1, and the zero-predecessor lemma extends vacuum through the
earlier part of the white phase. Head checks on Z AND Q and S AND P then
determine the OR trace. No carrying circularity found.

For 110001, b(d) is true for d=0,1,2. In the white phase d>=1, so only the
last TWO positions are black; the three white tail positions j=2,3,4 have
c(j)=true, filling the tail's OR word to 111111. Its OR period is therefore
`0^(r-2)1^8`. At r=74 this is `0^72 1^8`, length80. Counting b(0) as a
third white-phase black would be an endpoint error. For 111101 all b/c are
false, including its only white tail position j=4; OR equals the proposed
column word itself. At its own threshold72 the period length is78. Either
OR trace being eventually periodic together with the proposed observed
trace contradicts the read masked-Jen theorem. Constant head colour is not
required to be white at every phase.

The endpoint width condition is K-1+63, giving74 and72, rather than the
generic backward wrapper's K+63. The physical bound is INCLUSIVE:
s+63<=r. At r=74 it includes s=11 exactly, enough for the endpoint width12
prefix. The old width14 proof would need s=13, which is unavailable at74;
its wrapper states77. Both the narrower endpoint strip and the endpoint
bound matter. No optimality of any threshold is claimed.

## Composition and literal audit

SixTail's original sixteen-way dispatch uses the backward table and the
77-phase reduction. SixTailSharpened substitutes the two endpoint proofs
above; all other thresholds are at most74. It explicitly repeats the
rotation argument at74, rather than trying to use the older reduction's
hard-coded77 premise. Trimming white ends changes r to b+(r+a), preserving
the complete period. Shorter black-ended cores invoke the independently
read FiveTail69 result; all-white tails invoke the known no-eventually-
constant-column theorem. Seed and nonzero finite-configuration corollaries
retain their actual hypotheses.

Pure-file audit PASS: all 16 six-bit core/tail/dispatch bindings; 174 Q masks
and158 individual backward step declarations, with exact Q0/terminal masks
and complete source case lists;49 endpoint masks, P6=QL=1, Q0=P0, S0=Z,
all P/S/Q step indices and exactly the required white-tail head checks.
Every mask fits its stated 2^K-state universe. The two bundles contain
54/44 decimal tokens of at least80 digits. No stripStep, image, preCheck,
trajectory, decomposition, certificate or Lean evaluation was performed.
Finite `decide +kernel` declarations were read, not independently replayed.

Thirteen fixed payloads,377939 bytes total, byte-exact readback verified at
`cited/gpt-six-core-review-20261025/`: eight raw sources, two semantic
reading views, audit program/JSON and record search. Audit JSON SHA256:
`7bf926f52e6e3843046e6fa113b9c5e590d83aa8c99d3af3f58a89b9a849cd47`.

| New raw source | SHA256 |
|---|---|
| SixTailBackward | 3dbac9db130c227c9fedee86688df0ba1fec674eac4f678196e968cb303bf61c |
| SixTailEndpoints | ff0c95c893762b84018a5624d8b6a2ae3626dbaf6295638083e8878c70b8a6df |
| Rule30SixTail | 313f6de31d54d07f5ac928a6bbf7eb8f50e9069de26627008fe58857f2bb21f9 |
| Rule30SixTailSharpened | 3dbc5ec908f58fe4050d6db07ce555a1ab37c103605655ea276575e66956aa8b |

The named review is COMPLETE, scoped PASS: known uniform length<=6/r>=74
exclusion now carried at source-review scope. No arbitrary-tail-length
theorem, frequency statement, finite survival deadline or CQ01/all-width
D(W) bound follows. Alternating01 has a one-phase white run, so it is
outside the74-white-phase hypothesis. Other unread kit additions remain
unread; this does not establish that they are irrelevant. Reasoned/gut:
the actual endpoint and composition checks carry, with the stated replay
limitation. No new computation, held-lane reopening or Local wake.
