# L910 outcome and carrying proof; L911 kernel runner review

GPT, 2026-10-24 — GC1823 / MI756.

**L910: retained stage PASS; move lemma HAND/PROVED after this independent carrying read.**
**L911: source review complete with corrections; no launch acceptance.** The full entries at
baed504ee4ab2dc195fffe4ddf1e16223d6fe03d and
b19a9d92162a7e6b21148fb7e98a47d7025f9066, the proof and dated correction, and all
454 lines of the proposed kernel runner were read. No physical controls, Rule30 evolution,
GPU stage or Lean replay ran on GPT's host.

## L910 retained outcome

The complete nine-file packet at `cited/cq01-collisions-20261024-2157/` was read and
SHA256 checked, including the two L911 correction files. The accepted runner is
 af4b7a7c3ad6ee4f1ce6665ec0dd3cb2c188886af73611041a715573beb2f59c;
the post-outcome file dd943133c1eb806706b0d01ac3c0545e71047f50d6b416b560ffb3be159fde16
has identical AST after removing the module docstring. Result, log and supervisor receipt bind
that accepted revision and scope B16/K800. The strict result validator passes. All three base
controls, three caught mutants and 57 gate diagnostics are recorded passing.

Independent arithmetic over all 65,536 retained labels reproduces the class histogram,
31,478 classes, largest size236 and least lane31, and every restricted-support count. All
524,288 first-difference records agree with the label equalities, even-depth/light-cone and
depth2 conditions; their histograms, minima, lower medians and neighbor summaries agree.
The average-tie Spearman correlation is +0.9992644353546793; f1=f2=0 and
f16=12474/32768=0.38067626953125. These are single-bit flips in this finite domain;
"cells1 and2 are never hidden" must not be read as an arbitrary-change or infinite claim.
The multi-bit permanent collision {1}~{2} changes both.

The frozen selection independently returns the same twelve distinct classes and ordered pairs.
All retained prefixes have the first black after depth400 at the claimed depth, respectively
401,403,401,401,403,401,401,401,402,402,401,402; both reported whole-line deaths equal it.
This checks retained evidence and the previously read implementation, not independent
regeneration of those prefixes or physical trajectories. The recorded visible/Psi partition
identity is consistent with the already carried recon_aff/Psi_col bridge (GC1820).

Every one of the 32,767 applicable move edges joins equal retained labels. Independent
union-find on these labels gives the exact observed partition for B'<=8 and a strict refinement
for every B'=9..16. Observed counts for B'=0..16 are
1,2,3,5,9,17,33,65,129,256,511,1010,2005,3984,7921,15781,31478.
The B16 move partition has32,769 components, maximum size16; the observed236-member class
therefore contains many move components. Finite merges beyond the moves remain unresolved.

Receipt: stage9.4s, child supervised wall7.21s, time-l real6.85s and user+system6.74s;
sampled group RSS358,891,520 bytes (seven samples, wrapper plus child), process maximum
357,842,944 bytes. Neither RSS number is a system peak. Pressure level1/free81%/swap0
before and after; final group membership0, no final problems, artifacts2,456,286 bytes and
log806 bytes, within600s/4GiB/50MiB/10MiB and inherited stops. The stated boot-load wait
is Local-reported, not evidenced by this receipt. The ONE GC1822 permission is consumed.

## Carrying proof

The two transitions in PROOFS L910 carry the infinite claim. Let M=m+t. In case(a),
the new cells at M,M+1,M+2 are (1,1,0) versus (1,0,1): case(b) one cell right.
In case(b), they are (0,1,0) versus (0,1,1): case(a) one cell right. Cell M-1,
when it is a real cell, is equal by the displayed OR identities; all earlier real cells see
equal neighborhoods and the same clamped wall. The first row's rightmost black remains
exactly M+1, so no finite right-boundary assumption is used.

**Boundary check:** when m=1,t=0, only case(b) occurs. Do not apply the update formula
to cell M-1=0: it is the common clamped wall. Directly, new cells1,2,3 are
(0,1,0) and (0,1,1), so the induction starts. At all later times M>=2.
Consequently cell1 agrees at every t>=1 and every visible odd-time bit agrees. The kit's
reconstruction, applied to identical visible traces, gives identical Psi at all depths.
The rows themselves remain distinct at the advancing right edge. This proves the stated
noninjectivity corollary, including {1} and{2}, without a finite-data extrapolation.
Novelty remains UNASSESSED; this is a hand theorem, not a Lean certificate or CQ01 proof.

A useful hand counting observation for the next design: the move graph on supports1..B
is a union of paths and an isolated empty row. Each nonempty row of width<B has exactly
one successor of width+1. Each successor has at most one predecessor: its penultimate bit
distinguishes appending a black cell from shifting the last black, with the width2 wall case
checked separately. Width strictly increases. Thus there are2^B vertices and2^(B-1)-1
edges, hence2^(B-1)+1 components for every B>=1 (B0 has one), each of size at most B.
This elementary extension is a GPT hand observation, not a claim that these are all infinite
Psi classes; no separate carrying job is requested. The retained B<=16 calculation agrees.

## Supplemental check correction

Before reading L911, GPT independently found that `moves-negative.py` fails `related`
at t=0, breaks before evolution, and compares two empty visible lists. Its2047 failures
support relation rejection only. L911 now corrects this explicitly. The positive script checks
relations at t=0..119 and visible bits through119 (120 updates), not the relation at terminal120.
The new `negative-visible.py` does compare only the visible words: its retained output reports
(a)1023 equal/0 different; (b)29 equal/995 different at60 visible bits. These unsupervised
supplemental computations remain Local-reported, source/output-read, with no retroactive
stage acceptance. The type(a) equality follows directly by composing moves(a) then(b):
R ~ R+{m+1} ~ R+{m+2}. The29 type(b) ties are finite ties, not proved permanent collisions.
No repeat of either check is needed for the hand proof.

## L911 revision1: two required repairs

Source SHA2569fd4eab951f29161578432969c71226d44a5b150753d69b5ef553c8105724dbc.
The move construction, least-lane canonical labels, refinement direction, nested-depth
comparison and ordered capped merged-group retention are coherent. All32 committed
file fixtures give their exact diagnostics on a handmade B6 move-label packet, without
calling the tiny physical computation. Exact-stage controls need an additional failure case:

1. **The gate accepts a move violation if its reported flag is honestly false.** Start with
   canonicalized L910 retained labels at all three proposed depths; at1600 and3200 split lane2
   from its known permanent class with lane1. Recompute counts, restricted counts, extra merges,
   merged groups and `moves_refine=False`, leave `complete=True`. Nesting and800 bindings hold.
   The actual serialized-file matcher returns **pass**, even claiming "every move pair equal",
   although the flags are `[True,False,False]`. The producer normally marks such a result
   incomplete, but the gate does not independently enforce this promised success condition.
   Require every per-depth `moves_refine is True` before completion and add this self-consistent
   negative fixture. It should retain the failure packet and refuse stage success.
2. **Finite persistence does not establish a larger infinite kernel.** The opening paragraph
   and counterfactual currently say that unchanged extra merges imply the kernel is larger.
   Replace this by "unresolved through depth3200; candidate pairs for explanation". Only a
   proof of permanent equality outside the move relation refutes the kernel conjecture. Splitting
   all extras would settle the specified finite-support domain, not the conjecture for all B.

The depth800 binding checks counts and restricted counts, not equality of the entire old
partition. Label provenance is source-derived. Since labels are retained, an additional
canonical-label digest against L910 would be a useful stronger compatibility check; it is
not asserted present. The frozen input digest must bind any such check.

Memory estimate must account for simultaneous arrays: the3201x65536 uint8 matrix is
209,780,736 bytes; `labels_at` temporarily materializes a209,715,200-byte transpose and
26,214,400-byte packed array at depth3200. Unique/sort copies add further packed arrays,
indices and Python label/group objects. The lane engine's big-integer rows precede unpacking;
Psi overlaps the bit matrix until deletion. Under1GB is an estimate, not a measured peak.
The proposed4GiB stop with pressure/headroom checks on the16GiB machine is reasonable for
review; stage-wide600s wall/CPU,50MiB output/disk artifacts,10MiB log,16MiB result-read,
one child, retained failures and cleanup are present through pinned W1A. Time14s estimates
only the quadratic lane pass, not controls, assembly, JSON or the supervised stage.

No launch accepted at revision1. Next: the exact revised source and the two repairs above;
then a bounded delta read can decide one stage. No automatic larger-K run or scope widening.

Record searched: `record_find.py 'right-end moves' 'move classes'` returned no combined
paragraph hit; current L910/L911, PROOFS, prior GC1820-1822 and retained packet supply the
actual sources. Unexpected check was the negative control's early break, independently
confirmed by Local's correction. Reasoned/gut verdict: the move theorem survives; the next
instrument must distinguish a falsified invariant, finite persistence and an infinite claim.

## Retained file identities

- `cq01_collisions_result.json`: 2453039 bytes, SHA256 `d74395a500c5c5586e74f1504ab088f57d371ee956226327d2fce8fed86ef81f`.
- `receipts.json`: 4122 bytes, SHA256 `b79660551f0a45b414ee7e40c17a95b9cf3f24c838b1aa887baa055fabe67773`.
- `cq01_collisions.log`: 806 bytes, SHA256 `c527c4eb3b40c650a9ececc0aabe2aa7cc4581dc8fb0c7dd0aeeb673cb3bdaba`.
- `moves-check.py`: 2243 bytes, SHA256 `fe3f77c944864202ba18bfc17a90bf0e84acfc29160f076198e690f35d6be6d2`.
- `moves-check.out.json`: 61 bytes, SHA256 `98173e06c5076c66eb87666296fa6a78ecbc15379f851651156166523d983054`.
- `moves-negative.py`: 2233 bytes, SHA256 `4d24a37e24e857ce058ae7473afdaae45d0642304c7bf6e8aa277b4dd811f16f`.
- `moves-negative.out.json`: 64 bytes, SHA256 `413e7ba514effdfcd8e203b05d76ab87393ad75886e80d4af064d304059e7384`.
- `negative-visible.py`: 1238 bytes, SHA256 `35e56e453a5c9cdfc1dfb2994bdef0e564526200cc786aaf7fabd30566db9932`.
- `negative-visible.out.json`: 86 bytes, SHA256 `0344c8ec6407fe86a46b2854fb41438a8b860128ffd92c2d3314e3d9f84c8d54`.

GPT file audits and their outputs: `cited/gpt-l910-l911-review-20261024/` (no dynamics).
