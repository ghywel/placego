# L925 retained Check outcome (GC1834 / MI767, 2026-10-24)

**COMPLETE / PASS.** The one GC1833 stage ran once at the accepted source and
limits. Its permission is consumed. The kit's local checker replays66 constants
and accepts all five headlines with standard axioms only. This is the local
kernel-check outcome; this packet contains no external submission/verifier status.

Read the complete L925 at `7d8b3f7caa60dbb7c0c9ac70acb87d1b0ffc0709` and the
four retained files at `cited/trap-pair-check-20261024-2333/`. All store stat digests,
download bytes, submitted check.json bytes and checker-log JSON match:

| File | Bytes | SHA256 |
|---|---:|---|
| receipts.json | 13257 | `31ea93f925a0a44fbc96700e7dfa174eba2d44eaf29f96ab49d1566dfd98c3cc` |
| check.json | 4027 | `86abca97a1ecbf29da3f0c7d3ff79297e04ee09bd8c8e92f609342cb22f2839c` |
| checker.log | 5284 | `9592ef552ff75eb3b5800a8bb4a8e7aec3d23bdeca2b66766af19922a1580df3` |
| build_Rule30Submission.log | 219128 | `121fb796544978c9a57c68b9f50f3ca09a64c4cc18cc1b101a64cb9bf6d7f208` |

Initial conservative read guard200kB stopped before downloading the219kB build
log; after inspecting its listed size, the bounded read was raised to300kB,
still below the private client's1MiB response limit. No authentication failure,
physical rerun or proof replay by GPT occurred. All verification here is pure-file
comparison and retained-receipt review.

## Proof and source bindings

Actual module27f799f4, wrapperd12487a3 and W1A3f908914 hashes match the frozen
agreement and current source bytes. The receipt binds actual kit
cc1e0e0e7c1ae8c971aec5c14aaabb47c7b8c554/toolchain4.35.0; source-pin mismatches,
other tracked changes and unknown untracked inputs are empty. Eight dependency
objects have recorded initial digests and the terminal unchanged predicate is
true. As in GC1833, this last fact is the supervisor's byte-comparison result,
not an independently reproduced final set of hashes.

Check JSON has claim partial, importsStatements true, verdict pass, empty
newAxioms/reasons,40 declared entries each standardAxioms true, and replay
{constants:66,ok:true}. Exactly the five frozen headlines are found/ok/typeMatches
true with no problems. CQ01_R31, CQ01_R495, Psi_eq and u_R31 each use
propext/Classical.choice/Quot.sound; not_move_equivalent uses propext alone.
The JSON embedded in checker.log is identical to check.json and the committed
copy. Together with GC1831's full source read, this closes the local formal
composition review. Global CQ01/CQ01Empty/Problem1 remain open.

The build log contains one Built target, Rule30Submission, and91 cached Replayed
status lines. Its935 warning lines concern the existing imports/module syntax
and deprecations; there is no error diagnostic and the build completes
successfully. Cached Lake status replay is distinct from the66-constant kernel
replay in Check. No additional built dependency target appears in the log.

## Resource and restoration outcome

| Metric | Build | Checker |
|---|---:|---:|
| supervised wall seconds | 17.69 | 4.16 |
| time-l cumulative child CPU seconds | 7.66 | 2.88 |
| peak sampled live child CPU seconds | 6.1 | 1.7 |
| sampled aggregate group RSS bytes | 4139581440 | 3912007680 |
| time-l process maximum RSS bytes | 3523706880 | 3615817728 |

The complete receipt spans23.7 seconds. Both steps exit0, complete/pass, have
one Lean process at their observed peaks, zero final group members and no final
problems. Accepted caps and absence of fault injection are verified. All final
predicates hold, including artifact/pressure/swap/disk/source/object/dependency
and deadline checks. Pressure level1, free percentage74 before to69 after,
swap0, more than5GiB disk throughout the retained metrics. Final new artifacts
are1,012,951 bytes, below128MiB.

The4GiB margin above the build's sampled group peak is155,385,856 bytes,
**148.1875MiB** (about155MB). This is a successful narrow-margin attempt, not a
basis for automatic reruns or a system-wide memory peak claim. Cumulative build
CPU is7.66s; L925's6.1s is explicitly the sampled live CPU peak, not total CPU.
Footprint and resident-memory metrics remain separate.

Unexpected file check: receipt log_bytes counts decoded characters, not raw UTF-8
bytes: build205872 characters/219128 bytes, checker5276/5284. Both actual byte
sizes are well below10MiB, so this does not change the result. Future generic
log-cap reporting should label/use bytes consistently; no rerun or source change
is required for this completed stage.

The restoration receipt verifies all six paths: original source and five target
object paths. Preserved source digest is790ecabb598358d903fdcb5d5bbe4017db0fa816f8f924b47ecae3029af654d7.
No physical post-run kit inspection was performed by GPT; these are retained
verified-restoration observations from the M5 wrapper. They do not claim whole-kit
rollback. The terminal receipt is complete true and has all_restored true.

## Next

No retry or wider memory permission. L925's notebook/gate checklist is sensible:
all nine output cells must be bound, including exact illustrations, five types,
CQ01_R31's displayed axioms, graph and KernelCheck66; the final gate also binds
all five accepted Check headlines and whole-module replay through this exact
check.json digest. Exact notebook/gate source and build scope/caps are not yet
supplied, so no notebook build is accepted here. Review that source and its actual
outputs when delivered; prior Lean/essay source reads remain complete.
