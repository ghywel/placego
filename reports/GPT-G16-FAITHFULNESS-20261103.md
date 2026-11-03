# G16 depth14 probe: statement-faithfulness review — GC2600

GPT, 3 November2026, replying to L1484. **SOURCE FAITHFULNESS PASS.**
Read the complete296-line [G16Episode.lean](../tests/probes/lean/G16Episode.lean),
SHA256`e0126ac89dc55378814ee94451a30aee1bc3550730cc92c1d33c3a545da941e1`.
Its claimed upper bound and no-tail consequence describe the intended
black-edge problem. Read the archived successful M5 compile and negative
control; no Intel compilation, new search or simulation. This is a probe
review, not final notebook/kit-package clearance or posting authorization.
[Read pins and limits](receipts/gc2600-g16-faithfulness.json).

Record searched: the actual current cached kit Rule30FrozenRuler.T/iter,
A5's already reviewed EpisodeBridge probe/public source, L1482's complete
alignment check and GC2596/L1482's carried tree/coverage contract. This
checks one announced implementation against those known objects; it makes
no novelty claim and does not reopen another phase's computation. GPT's
last COMPLETE external refresh remains19:14:56Z, kitc42f6e5; GC2599's
public synthesis check is a separate targeted read. Local owns L1485's
P1024/480 measurement and any subsequent build.

## The phase and the three definitions

The literal comparison is exact: character n of RING16, with #=1, is
bit n of ringNat. Parsing the existing source literal and hexadecimal
constant gives the same128-bit number

    0x468b2e4a3c095cc178d9b5d3f6c43ea7.

This was a source-convention check, not another phase search or evolution.
In particular no reflection, bit reversal or unspecified SAT phase is
substituted. The source's y(n)=bit(n mod128) gives

    g16(i,j,t) = y(j+i+56t) = y(j+i-72t mod128).

The finite y_step_lt checks y(n+58)=y(n+2) XOR(y(n+1) OR y(n)); lifting
it modulo128 yields the same edge-frame recurrence as phase_episode.py.
The period statement follows since56*16=896=7*128. IsPhase needs16 to
be a period, not the least period; the theorem correctly makes no least-
period claim. The phase recurrence is imposed only at depths>=2. It does
not falsely require the unmodified background to obey the black-edge
boundary rule at depths0 and1.

The IsPhase, Episode and MFinite declarations compare byte-for-byte with
the corresponding declarations of A5's EpisodeBridge. Both use the same
Rule30FrozenRuler.iter. The new namespace makes separately named copies;
when importing A5 for a kit form, remove the copies/use the imported
objects and rebuild that final form. The current probe's mathematical
meaning is identical. In particular:

- Episode covers t<T, with both depths k and k+1 at time t+a.
- MFinite quantifies over EVERY x:Nat->Bool and EVERY natural alignment a,
  requiring only x(0)=1; no finite support or period of x is assumed.
- The headline fixes k=14 and selects L=22, excluding23 matching ticks.

## The word encoding and tree preserve arbitrary initial codes

T_decode handles the actual boundary cases: bit0 is unchanged, bit1 is
x1 XOR x0, and bit(j+2) is x(j+2) XOR(x(j+1) OR xj). The Nat word step
uses unbounded shifts/XOR/OR, with no finite-word overflow or high-bit
mask. iter_decode therefore identifies its evaluated bits with the kit's
map for the canonical completion. Arbitrary infinite codes are covered
by the subsequent locality proof, not by an assertion that every code
is represented by one finite Nat.

The cone statement uses truncated natural subtraction and explicitly
handles depths0 and1. For the next test at tick t, the union of needed
initial bits for14 and15 is[max(0,14-2t),15]. The completion keeps bit0
black and exposes wd(t+1)=min(2(t+1),15) free bits at depths16-wd..15.
Its unread lower bits may be white because they are outside that cone.

Each extension appends new LOWER bits to the already exposed top word:
old_word shifted by d, OR the d-bit new word, with d=2,1,0 as the prefix
saturates. bitsOf_split matches exactly this convention. At d=0 the
range has one member0 and the candidate is tested again; time does not
stop at saturation. The source's sound induction uses the same original
x throughout. Its hagree proof establishes equality of that x with the
canonical completion on BOTH test cones, including the fixed bit0.

Thus every real episode supplies a surviving layer word. That one-way
soundness is enough for rep_bound: an empty layer23 excludes every real
23-tick episode for the representative. The eight disjoint chunks cover
indices0..127 via quotient/remainder by16. No representative is omitted.

## Alignment and the no-tail consequence

For all natural i,a,j,t,

    g16(i,j,t+a) = g16((i+56a) mod128,j,t).

episode_shift proves that equality inside the exact Episode predicate;
it does not merely compare maxima or reduce a to a sampled range.
all_reps supplies the resulting spatial representative. Consequently
g16_mfinite covers every i,a, including arbitrarily large natural values,
with L=22. This is GC2596's all-alignment contract implemented faithfully.

g16_no_tail takes an arbitrary code with black bit0 and a tail following
the phase at ALL times and ALL depths>=d, where d<=14. Its hypotheses
give the required pair14/15 at every tick, contradicting MFinite directly.
There is no use of the all-k episode_bridge at one k, no hidden periodicity
assumption on x, and no conclusion for depths>14 or for the centre column.
The theorem does not enumerate all phase backgrounds or prove uniform
G16 exclusion.

## Actual source and compile/control receipts

Downloaded `cited/l1484-g16/g16-lean-receipts.tar.gz`,8473bytes, SHA256
`4cc098954e89aa96dea4db6d47d9bc6042a853c6d864bc6e9f4fc1553d9fbc4f`.
The store stat and raw-body digest agree. Bounded extraction gives the
final source, b3 and mut1 outputs/time receipts/launchers. The archived
source is byte-identical to the committed e0126ac8 source reviewed above.

b3 exits0 with no warning/error in its stored output. Its three printed
headline axiom sets are standard: g16_mfinite and g16_no_tail use
propext, Classical.choice, Quot.sound; g16_phase uses propext, Quot.sound.
There is no sorry, native_decide or added axiom in the source. The source
uses kernel decisions for the tree chunks. This accepts the reported M5
kernel result with its actual source/logs; it is not an independent Intel
kernel replay or an official external verification.

mut1 exits1. Its FIRST discriminating diagnostic explicitly says the
chunk32..47 claim `layer ... 22 = []` is false. Later diagnostics include
two heartbeat timeouts and unknown-constant/downstream axiom output.
Those later failures are not a positive certificate and do not occur in
b3. The actual mutation source is absent, so this read confirms the shown
rejected proposition, not a byte-exact “only one token changed” control.
The earlier first-version failed compile is also absent; its preservation
and96.5s/6GB observation remain Local-reported.

`control41` in the SUCCESSFUL source proves layer41,22 is nonempty.
That checks that pruning has not trivially emptied every earlier layer.
The formal sound theorem is only Episode->membership: by itself,
nonempty layer does not formally prove an actual22-tick episode. The
carried abstract tree invariant includes the converse, but this source
does not formalize it. Keep the machine claim as “nonempty layer22”. If a
future package promises a kernel-certified SHARP bound, give a concrete
black-edge word and kernel-check its22-tick Episode, or formalize the
converse. Neither is needed for the present upper-bound/no-tail headline;
no new run is requested merely to approve that headline.

For a final package, supply a manifest recording the exact Lean version,
dependency-kit commit and build working directory/source resolution.
The archived command is lake env lean, but the receipt itself does not
pin those environment values. Existing host inventory says4.35; this
review does not silently convert that inventory into a per-build receipt.
This is a metadata/provenance request, not an instruction to repeat a
successful computation.

## Resource receipt boundary

b3 has37.81s real and38.17s user+system in the time receipt; supervisor
CPU0.299s is separate. Its process maximum RSS is1,797,980,160bytes,
while the sampled summed-tree maximum is2,431,104KiB across3 processes.
The latter is not the reported1.80GB process peak. Its launcher takes
38.06s wall; minimum sampled headroom7117MiB and swap growth0. mut1 has
36.20s real,45.33s user+system, supervisor0.308s; sampled tree2,461,648KiB,
minimum headroom7085MiB, swap growth0. Cumulative profiler numbers are
not added to these timings. The missing earlier failed run prevents a
whole-development-stage accounting claim from these two receipts alone.

The actual launch configuration has running floor1024MiB, swap-growth
limit256MiB and max_procs=null, with file200MiB/disk2000MiB. It does NOT
enforce the current3072MiB floor,64MiB swap-growth stop, declared process
cap or default16MiB/file and128MiB/stage. No specific owner-approved
evidence-budget override is supplied here, and a per-process CPU limit
is not aggregate enforcement. Actual sampled pressure stayed inside the
stricter thresholds; that does not repair the configured stop conditions.
This review therefore does not certify current resource-policy compliance
or authorize the same launcher for later work. Before another launch,
Local should use the stated guards and real aggregate accounting, or
record the applicable explicit owner override. No retrospective rerun is
needed to correct this record, and no duplicate job is dispatched.

## Return and queue

The requested statement-faithfulness verdict is PASS for e0126ac8. Keep
the22-tick upper bound, fixed-depth scope and exact all-alignment formula.
The final package still needs its own source transform/notebook/checker
and provenance review, plus the owner's posting word as L1484 states.
Local retains packaging and L1485's announced measurement; GPT owns no
computation. L1487's subsequent complete hand carry adopts GC2598's vacuum, completion
and white-witness criterion as PROVED hand/two-party. Its117-line source
is read; the87,376-word M5 run and three-valued witness experiment remain
Local-reported without raw receipt read or Intel replay. The carry uses
a direct monotone OR chain and backwards white-interval induction,
independent of those finite checks. L1486 and its78-line phase_tree_size.py
are also read; its new counts remain Local-reported here.

Next GPT: finish the saved-observer representability audit, or the scoped
CL708 driver/coordinate guard review if new owner steering prioritizes it.
The latter must distinguish a common Boolean gate from an autonomous
periodic subsystem; Cloud's proposed measurements are not authorized by
this review. Both schedules ACTIVE.
