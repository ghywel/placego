# Five-tail core certificates: carrying source review

GPT, GC1860/MI793, 2026-10-25. **Scoped source/hand PASS.** This closes the
five-tail core gap explicitly left by GC1859. The known kit theorem excludes
eventual repetition of `0^r u` for every Boolean tail of length at most five,
every `r >= 69`, every column and every configuration with a leftmost black
cell. The right tail and the transient are unrestricted. This is adoption of
existing source, not a new project proof or an independent kernel replay.

Pin: `3eca23c0a9fa6b153313655e6d51835406c2d06e` of
[Rule30PrizeKit](https://github.com/WolframInstitute/Rule30PrizeKit/tree/3eca23c0a9fa6b153313655e6d51835406c2d06e/lean/Ruliology/CellularAutomata).
All semantic statements/proof bodies of the new 1,238-line
`Rule30Certificates/FiveTailTube.lean`, all 54 lines of `Rule30VacuumExample`
and all 63 lines of `Rule30WhitePadding10101` read. Large decimal literals and
three state lists were replaced only in the reading view; their complete raw
bytes were retained and parsed separately. The previously read 60-line
`Rule30FiveTail` dispatch was rechecked, as were the full 194-line restricted
tube and 112-line vacuum criterion. GC1853/1858/1859 carry their underlying
physical, sparse-check and rotation interfaces. Record searched:
`FiveTailTube VacuumExample WhitePadding10101`; only GC1859 scope exclusions.

## All eight new cores

| Tail | Mechanism | Strip width K | Stabilization N | Stated core threshold r |
|---|---|---:|---:|---:|
| 10001 | Vacuum avoidance, W11 | 11 | 18 | 65 |
| 10011 | VacuumExample B | 5 | 2 | 61 |
| 10101 | Endpoint-conditioned tube, L=24 | 16 | not a full-set stabilization | 69 |
| 10111 | Vacuum avoidance, W8 | 8 | 13 | 62 |
| 11001 | Vacuum avoidance, W9 | 9 | 13 | 63 |
| 11011 | VacuumExample A | 5 | 2 | 61 |
| 11101 | Vacuum avoidance, W9 | 9 | 13 | 63 |
| 11111 | Vacuum avoidance, W10 | 10 | 16 | 64 |

The public FiveTailTube vacuum interfaces weaken their five thresholds to a
common 65; the final FiveTail dispatch uses 69 for all eight. No sharpness
claim follows. Here K counts cells immediately to the right of the observed
column, not the support width of the initial row.

For each vacuum core, cached one-step equalities reach G from the full strip
set after N white inputs and prove `image K false G = G`. Five further cached
images spell the actual tail, and their final mask excludes state index zero.
The small width-five pair states those finite checks directly with
`G = 2875964011`. The generic criterion needs
`r >= max(N, 10*5+11, K+9*(5+1))`; these are exactly the listed thresholds.
The period maps any actual initial strip into the vacuum-free tail image.
Its black cell would reach the boundary during the next early white phase,
contradicting the independently established physical early-white estimate.
This argument does not assume the initial strip is vacuum.

## What the 10101 tube actually forces

The separate endpoint proof does establish an empty K-cell prefix at EVERY
period boundary from the physical white-pulse/Jen argument. Its exact width
requirement is `K-1+9*(m+1) <= r`: the encoded indices are j=0..K-1 and the
physical prefix request is j+1. Thus K=16 and m=5 give 69, alongside analytic
bound 61 and tube depth L=24. Substituting the vacuum criterion's different
K+54 bound here would incorrectly demand 70.

During the white phase, actual membership in Z follows from the empty start,
`Z.testBit 0 = true` and `image 16 false Z = Z`. It is not inferred from a
sparse list or from a backward implication. Forward tail sets start at S0=Z;
the tail ends at the next period's empty prefix. Unrestricted P-predecessor
checks therefore propagate P5=1 backward to P0 at the white/tail join.
Q0=P0 then starts the restricted Q chain. Its 24 predecessor steps, restricted
to the independently established Z membership, end at Q24=1, the singleton
vacuum. The zero-predecessor lemma extends this vacuum backward through the
earlier white phase.

The Q head checks force black for backward distances d=0..8 and white for
d=9..24. In the WHITE phase d>=1, so the adjacent column is white until r-8
and black for the last eight white phases. At the two white tail positions
j=1,3, the intersections S1 AND P1 and S3 AND P3 force a white adjacent cell.
At the other tail positions the observed column itself is black, masking its
neighbour in the OR trace. Hence the adjacent OR trace repeats
`0^(r-8) 1^8 10101`. This and the hypothesized observed trace would both be
eventually periodic, contradicting the read masked-Jen theorem. It does not
assert that the entire white phase has an empty adjacent strip.

Hand unexpected/end-point control: at r=69 the OR word is `0^61 1^8 10101`,
length 74. Counting b(0) as another white-phase black would give nine instead
of eight: d=0 is the tail join and is outside s<r. The Q24 singleton is
consistent with its required white head. These checks tip the off-by-one
unease toward acceptance. The proof's period-boundary vacuum premise comes
from the earlier physical theorem, not from the tube conclusion; no carrying
circularity found.

## Literal audit and retained evidence

Pure-file audit PASS: 123 numeric masks fit their declared state universes;
103 decimal tokens have at least 80 digits, maximum 19,729. Exact OR-of-bits
bindings reproduce Z, S1 and S3 from 1,250/1,250/1,254 listed SOURCE states,
all below 65,536. This independently checks the essential GC1858 list/mask
binding. Qstep indices 0..23, Qforce 0..24, Pstep/Sstep 0..4, cached reach
chains and all five tail-image indices are complete. P5=Q24=1, Q0=P0 and
S0=Z match literally. Final cached vacuum masks have bit zero clear.
No stripStep/image/preCheck evaluation, trajectory, certificate or Lean replay
was performed. Finite equality declarations using `decide +kernel` were
read as such, not reported as independently executed.

Ten payloads, 877,566 bytes total, fixed and byte-exact readback verified at
`cited/gpt-five-core-review-20261025/`: six raw sources, semantic reading view,
audit program, audit JSON and record search. Audit JSON SHA256:
`5a0033a8d8c3ed9d92685afef7a68ba1e2fdc952e09ca178f39f36fbf470e154`.

| Raw source | SHA256 |
|---|---|
| FiveTailTube | a34c8c80ea21aa4e867861360a886756bca96cb3c74c44b4b891acda2903f7a0 |
| Rule30VacuumExample | b1e6ac36e8c5fbe59bbd9e48d30211d65b95a7cda3022ce78337da56c4f128f5 |
| Rule30WhitePadding10101 | 5a965d5dddc090c2b2a2d9c543b2b5b9886315753800bd68f0aeb93867458203 |
| Rule30FiveTail | fabfb3713c980c1ea6084eb6f927bf18baf1bc822f6f369cf57c04b5ae4dec6c |
| Rule30RestrictedBackwardTube | 0511547d17e527e81cfd93bf03fbed785885cd79bb3586288f4571b90b7a210b |
| Rule30WhitePaddingVacuumCriterion | 97f43530ba72edf398237176aecaec8b3de237f15633281080e21fb7a0668554 |

## Verdict and remaining scope

FiveTail's eight-way dispatch now has its actual new core proofs read. Together
with GC1859's rotation, shorter-tail cases and all-white branch, this completes
the source-review chain for length<=5/r>=69, with seed and nonzero finite
corollaries. The six-tail reduction can now reuse this five-tail input, but
the new six-tail core certificates and SixTail itself remain unreviewed.
No blanket six-tail acceptance, arbitrary-tail-length theorem, finite survival
deadline or CQ01/all-width D(W) bound follows. Those missing implications are
not supplied by large padding alone. Reasoned and gut verdicts agree: useful
known-source closure at the exact stated scope. No new computation or launch.
