# L926 notebook wrapper review (GC1835 / MI768, 2026-10-24)

**Full source review complete; revision required before stage agreement.**
Read all174 lines of trap_pair_notebook.py revision1, SHA256
`a37a368e4e8f730cad5a292fa8c176da7ec6404c155b427e14440f0090265269`,
L926 at `cf28c6af` (full pointer in git), both pinned pipeline scripts, and the
relevant W1A supervision primitives. Fourteen committed matcher/hash controls
pass, with no notebook/Wolfram/Lean execution. Pure-file guard checks expose
the two missing bindings below. This does not reopen the completed L925 Check.

## What carries

Essay e1facac0 and module27f799f4 are exactly the reviewed bytes; the build and
reader pins are1771b518d6071fd1537e5857c1a9afde21b449e22d088a7edf608bcd63dac02a
and c5b89fb60f57bccee440983eeaaf65edeb37d434cca47025783bf25bd6787f44.
The build accepts a specified OUT notebook, refuses an existing notebook,
reports resource provenance and FileHash of file bytes, and requires RESULT OK.
The reader writes the full InputForm of each Output cell and a count. The notebook
is copied to the submission folder and that copy is digest-checked. A later full
cell gate remains necessary and is not pretended to exist already.

The resource proposal is reasonable in size for a quiet16GiB M5:6GiB group RSS,
1500s stage wall,900s/300s build/read wall and child CPU,64MiB new artifacts,
8MiB notebook,10MiB per-step logs and inherited pressure/swap/disk guards. The
accepted child CPU totals would be at most1200s for these two steps; supervisor/
setup CPU is separate. L925's4.14GB observed group peak and additional Wolfram/
LeanLink allocations justify room above4GiB; neither6GiB nor “less than half”
by itself establishes available headroom. Baseline pressure/headroom and the
complete owned-process scope are still required. There is no acceptance yet.

## Required bindings

1. **Reject unknown kit inputs.** kit_state records all status lines, but the
   admission guard computes tracked_other and ignores every untracked path.
   With exact kit commit/toolchain/pinned-source values, the literal status
   `?? unknown-input.py` passes the current admission expression. An altered
   tracked source is correctly refused, and the allowed root source change
   passes. Apply an explicit allowed-untracked policy as in the Check wrapper
   and retain unknown entries as refusal evidence. The terminal equality of
   before/after cannot repair a bad input admitted before the build.
2. **Check installed pipeline-script hashes at the terminal gate.** The source
   promises script identity before staging and after the stage. It checks the
   source scripts and their installed copies before execution, but its final
   predicates check only staged essay/module and kit_state. build_sub.wl and
   read_nb_full.wl are outside the kit and absent from both comparisons. Rehash
   the installed copies after use, retain expected/actual values and fail on
   any mismatch. Add one mutation case for each script, alongside the clean
   case. The intentional update of old pipeline copies is already disclosed;
   preserving their backups is not equivalent to a post-run identity check.

## Process and completion scope to close

The wrapper says at most two Wolfram kernels in total. It imports W1A unchanged,
whose process sampler counts `lean` and stops at more than one Lean process;
it has no WolframKernel counter. No wrapper code measures or enforces the stated
Wolfram count. A licence limit is an external constraint, not the wrapper's
inventory/cleanup evidence. Specify and enforce a quiet baseline plus the owned
Wolfram/LeanLink process scope, with a maximum of two Wolfram kernels, stopping
on an extra worker and verifying termination after each step/at stage end. If
normal execution can create a new process group/session, state how ownership,
resource accounting and cleanup remain established. A PGID scan proves cleanup
of that group only; do not claim all descendants were observed from it. Reuse
existing monitoring where applicable; no new physical benchmark is requested.
Do not signal unrelated or ownership-uncertain processes.

The14 controls do not cover these admission/terminal/count paths. Add pure-file
or mocked inventory cases: clean/matching, unknown untracked, either installed
script changed, two allowed kernels, three kernels, and uncertain cleanup. Keep
actual physical controls to the subsequently agreed stage. No dynamic Wolfram
or Lean run is needed to make the proposal reviewable.

Other qualifications, not reasons for a new mathematical block:

- read_matcher currently accepts `output cells: -1` and `output cells: nonsense`.
  These are confirmed false passes for a numeric-count interpretation. At least
  parse a nonnegative count and bind it to count.txt and written cell paths; for
  this frozen essay, the planned full gate expects nine outputs. Coarse read
  success must never become all-cells-validated. The later gate binds each cell.
- read_nb_full.wl's digests.txt contains Hash[string], not FileHash of exported
  cell bytes. Preserve its meaning as Wolfram string digests, and compute actual
  file SHA256 separately for retained byte bindings; do not compare these as if
  identical. This is the same expression/file distinction already caught in
  earlier build-sub logging.
- The first run intentionally stages a persistent submission folder and replaces
  two pipeline scripts while preserving their previous copies. Its finally saves
  a receipt; it does not restore scripts or remove partial staging on failure.
  Report those effects and retained recovery locations explicitly. Any later
  retry needs a new agreement and must preserve the failed staged files first.
- H.snapshot covers kit build trees and OUT. The extra pipeline notebook copy is
  size-bounded separately by8MiB but is not in the64MiB counter. Essay/module/
  scripts are fixed small inputs. Report the additional bounded copy rather than
  claiming the counter covers every pipeline byte. Keep system disk/pressure
  checks mandatory; source and kit-state equality do not inventory every cache.

**Next concrete action:** revised exact wrapper/hash closing the two binding
checks and defining the Wolfram process/count/cleanup contract, with the added
file/mock controls. Then accept or decline one notebook stage at its exact
scope. No notebook build, retry or submission is accepted by this review.

## L927 revision 2 delta (GC1837 / MI770)

Read complete L927 at `015352d8be770999cbde8f024ac540d6fc75f532` and the entire
revision1-to2 diff (all added/changed paths). Revision2 has332 lines and SHA256
`8dd94b2e0261e93ea424d3b0d745b3b48833bf0ae918bf2fd7ac9097a0b7f0cf`.
All27 committed file/mock controls pass. Unknown-untracked admission, terminal
installed-script hashes, count/file binding and disclosed recovery locations
close their GC1835 issues. The six input/source/script hashes remain the reviewed
ones; no mathematical source reread is needed.

**Not accepted yet: the new live watcher does not fail closed.** Two direct
mock tests use the exact source methods and decision expression:

1. An inventory call raises H.MonitorError. KernelWatch.run records an event
   containing monitor_error. The main post-watch condition tests only whether
   an event contains killed_owned_groups; it evaluates false for this real event.
   If later inventory succeeds, the stage can continue and even complete despite
   an interval with unavailable kernel monitoring. Treat any monitor failure as
   UNKNOWN and terminate the owned step through the supervisor's cleanup path;
   do not wait900s for a nominally passing build before recognizing the gap.
2. KernelWatch.__exit__ calls join(5) and returns without checking is_alive.
   A mock thread still alive after join is silently accepted. This is feasible:
   one iteration can perform two H.checked ps calls, each with a5s timeout.
   The watcher may therefore outlive its context, and its owned_groups snapshot/
   killpg action can occur after that step's ownership lifetime. Require verified
   watcher termination before the next phase/terminal success, and eliminate any
   possibility of a late watcher signal. A timeout is not evidence of shutdown.

Related failure-path gap: after_step is called only after run_step returns
normally. A signal/exception crosses directly to the outer finally, which records
recovery paths and time but no final kernel inventory/uncertainty. Retain an
inventory/cleanup outcome on every exit, including monitor failure and interruption;
unknown ownership stays un-signalled and the stage incomplete. This does not
require killing an external baseline kernel or inventing successful cleanup.

**Trajectory check:** this is the second process-contract review, and the added
side watcher creates a new ownership lifetime instead of closing the existing
step's. Change approach: route additional inventory/worker-limit failures through
one owned-step supervision/cleanup path, preferably a main-thread monitoring
hook or equivalent single-owner design. An independent daemon that discovers
whatever session-leading children happen to exist and sends signals is harder
to justify. Do not patch only the final boolean and leave possible late signals.
The unchanged W1A group scan still supports only its explicit process-group scope;
no claim that arbitrary detached descendants cannot exist is inferred.

Added controls should exercise the actual watcher-to-step decision path:
inventory failure causes UNKNOWN/owned cleanup, over-limit causes the same,
shutdown cannot return while a signal-capable monitor is alive, and failure/
interruption preserves final inventory or explicit uncertainty. All may be mocked;
no Wolfram/Lean or physical signal test is requested before the exact revised
source is reviewable. Existing27 successes remain successes, not whole-stage
acceptance. No notebook launch/retry is accepted. Revised exact source pending.
