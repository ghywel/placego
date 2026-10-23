# G1: exact Metal survivor engine interface

GPT, 2026-10-23. Design only, following the owner's GPU question and GC1724. No shader changed, no computation
launched, no performance claim, and no execution agreement. Local's exact implementation, hardware/toolchain
inventory and caps still need joint acceptance. W4 runs independently under its existing agreement; G1 must not
overlap it by default.

Record searched: `record_find.py 'Metal' 'survivor engine'` finds the existing next-compute design. Read that report
and the pinned `Rule30ZeroBoundaryLanes.lean` computation, equations and soundness interface. Verified source SHA256:
`e34541fa34ee09d0f480db469384fcab9c05311e7f26bc135db02c5f692de7e3` (kit cc1e0e0). This is an implementation
specification for that computation, not a new proof of its physical theorem.

## Word ownership and exact projection

For chunk c and lane count 2^n, GPU word q owns lane indices p = 32q + b, 0 <= b < 32, restricted to p < 2^n.
This is a bit position within the kit's Nat, not a depth coordinate. The combined free-bit choice is
u = c * 2^n + p; c ranges below 2^(floor(W/2)-n), with n <= floor(W/2). Do not allocate or enumerate that full
range merely because this indexing formula exists. Selected words give selected-word coverage only.

The projection pi_q(X) is bits 32q through 32q+31 of X. It commutes with XOR, OR and AND, so the complete
`scanN`, `mapX`, `stepR` and alive updates split independently into 32-bit words: no carry or neighbor-word access.
Initialization has to agree too. Let M be the valid-lane mask, all 32 bits for a full word. Then:

- For 0 <= s < min(5,n), use the corresponding mask from AAAAAAAA, CCCCCCCC, F0F0F0F0, FF00FF00,
  FFFF0000 (hex, indexed by s), intersected with M.
- For 5 <= s < n, use M when bit s-5 of q is 1, otherwise zero.
- For s >= n, use M when bit s-n of c is 1, otherwise zero.

When n < 5 there is one partial word with 2^n valid bits. Construct its mask without an undefined shift by 32;
handle the full-word case separately. Keep this mask in all complements. This also makes tiny exhaustive controls
exercise the same numbering as production words. Bounds-check dispatched word indices and buffer offsets.

## Exact recurrence and diagnostic meaning

Before level k, R has k entries and Rm has max(k-1,0) entries. For a starting word y, scan depth i = 0..k-1:

    v = y
    for i = 0 .. k-1:
        v = v XOR (R[i] OR (0 if i == 0 else Rm[i-1]))
        S[i] = v

For k = 0 the scan is empty and its last value is y. The next diagonal is:

- k even: scan with y = M; Rnew = [M] followed by S.
- k odd and k+1 <= W: scan with the specified free-bit mask y; Rnew = [y] followed by S.
- k odd and k+1 > W: scan with y = 0, set t to its last value, and use Rnew = [t] followed by each S[i] XOR t.

Only when k is even and k+1 > W, update alive to alive AND (M XOR the scan's last value). Then rotate Rm = R,
R = Rnew. Start at k = 0 with both diagonals empty and alive = M; K levels means k = 0 through K-1.

**Unexpected interface check:** in the forced odd branch the kit returns t as `stepR`'s second component, but the
last cell of Rnew is zero, since the last S entry is t. That returned component is the chosen boundary bit there,
not the physical tail cell. Log these as different quantities. Likewise, a lane's elimination level records a
failed tail constraint in reconstruction; it is not automatically the first white time of a physical orbit.

Alive masks are monotone decreasing. For the first correctness comparison, keep advancing even after alive is
zero so all diagonals remain directly comparable with the source. Early termination is a later implementation
choice and should not silently change retained traces. Preserve identifiers and complete masks, not only a hash
or total survivor count: equal counts can hide a lane permutation.

## A bounded implementation to propose

First prefer one thread per 32-lane word, three distinct rolling diagonal planes in depth-major layout, and a
separate alive array. No atomics or cross-thread reductions are needed for the recurrence. Each thread reads and
writes only its own word index; the three planes prevent in-place overwrite of an older diagonal. A kernel may
advance a small fixed block of levels, then return to the host for progress and stop checks. Block boundaries
must preserve k, the three plane roles and alive exactly. Freeze the block length before launch; do not tune it
adaptively during the pilot.

For B resident words and horizon K, three planes of K+1 uint32 entries per word require 12 B(K+1) bytes. With
B = 8,192 and K = 129 this is 12,779,520 bytes; this is illustrative buffer arithmetic, not approval to run that
batch. All-level alive capture adds 4 BK bytes. Compiler temporaries, driver allocations and CPU buffers are extra.
This layout avoids assuming that two long private per-thread arrays remain in registers. It may instead make
global-memory traffic or dispatch overhead costly; neither layout nor unified memory guarantees acceleration.

Apple documents that pipeline-specific thread limits depend on kernel resource use and that execution width must
be queried: [threadgroup sizing](https://developer.apple.com/documentation/metal/calculating-threadgroup-and-grid-sizes).
The 32 data lanes in a uint are unrelated to a claimed hardware SIMD width. Query actual device identity, feature
support, pipeline limits and allocated-memory baseline. Retain explicit completion/synchronization before CPU
inspection; see [resource synchronization](https://developer.apple.com/documentation/metal/resource-synchronization).

## Controls and launch gates still to freeze

The implementation proposal should supply exact CPU scalar reconstruction, CPU word and Metal sources/digests,
the exact case list and literal expected traces. At tiny widths compare every lane and every level exhaustively;
independently enumerate finite physical starts for the relevant implication, not merely another translation of
`scanN`. At larger selected words compare complete diagonals/alive masks to CPU word output. Include n < 5, n = 5,
q = 0/1, lane 31/32 boundaries, nonzero c, k = 0, fuel zero, and both parities on each side of W. A retained-live
case must reject accidental all-zero output. Wrong parity, swapped lane order and a shifted forced-tail boundary
must be detected by the controls. Include an incomplete last dispatch with untouched output sentinels.

Predict exact agreement first; predict a throughput benefit only for the frozen batched case, with failure allowed.
Separate build/pipeline creation, CPU preparation, dispatch, GPU completion and CPU validation from warmed GPU time.
Compare equivalent outputs and the same case list. Report both CPU word and GPU end-to-end costs, not Lean versus
Metal as if they perform the same trust task. No runtime/quota can be justified from theoretical GPU occupancy alone.

Suggested ceilings for Local to turn into an executable proposal: 256 MiB explicit buffers, 6 GiB owned-process
RSS, 600 seconds stage wall, 300 seconds cumulative host CPU, 256 MiB swap growth, pressure >= 2 stop, 5 GiB free
disk, 128 MiB new output and 10 MiB log; one GPU command buffer in flight and no concurrent Lean job. Individual
dispatch limits and timeout handling must be specified: host cancellation cannot be assumed to preempt GPU work.
On timeout submit no more work, retain UNKNOWN and let the agreed owned-work cleanup policy complete safely.
These are proposed caps, not an execution agreement or proof that the driver obeys them.

The first result would establish or refute a usable exact discovery engine at named inputs. A surviving lane
requires separately reconstructing and validating a finite physical row before it becomes a physical witness.
An all-zero selected-word result proves no universal width statement. A future exhaustive GPU census still needs
the project's independent exact validation/certificate route. No finite-horizon survivor proves infinite survival,
and no runtime result advances arbitrary-width Q01 by itself. No new carrying review or Cloud work is requested.
