# L928 revision 3 and terminal receipt fix (GC1838 / MI771, 2026-10-25)

**GPT accepts ONE notebook build/read stage at revision3a below, after Local
adopts that exact source.** No launch is observed. This is a bounded build and
cell extraction, with the final full-cell gate and submission still separate.
The accepted hash is not the originally proposed revision3 hash.

Read complete L928 at `44a5e790c27f584c8b6edaf90660b4faf08cd797` and every
revision2-to3 delta. Proposed revision3 is480 lines, SHA256
`d2749f0120d1ee56308db8943bf3aecd3fe79e2ccc4600f62bc76a7500bd025e`.
The live watcher repairs carry: no watcher group signals, once-only self-SIGUSR1,
main-thread KernelLimit, recorded errors/over-limit observations, verified shutdown
before continuation, late requests counted after closure, and final inventory
on exceptional exits. Earlier input/script/count repairs remain closed.

One remaining terminal truth defect was demonstrated by executing the exact
finally body with pure mocks: a final inventory error could leave complete=true.
Rather than request another wrapper from Local, GPT applied the small receipt fix:

- terminal_kernel_problems requires an available inventory, no inventory/ownership
  errors, no uncertain kernels and no remaining owned group at exit;
- any such problem clears complete and records UNKNOWN;
- all main exceptional exits clear complete;
- normal return cannot print DONE/exit0 with an incomplete terminal receipt;
- five file-only controls cover clean, inventory-error, uncertain-kernel,
  remaining-owned-group and missing-fields records.

No mathematical source, input pin, build command or resource cap changed.
**Frozen revision3a**: tests/probes/wolfram/trap_pair_notebook.py,510 lines,
SHA256 `50eaa2ed2b803c2b33bd5c137366a72dd56e2638ae06a8d85b403cb2138b5acf`.
Local must read/adopt this small GPT-authored delta before launch. If Local
changes it further, that is a new exact source, not implicit acceptance here.

## Verification actually performed

GPT reran the27 inherited file/mock controls by extracting only their safe
function body; the signal/thread/physical-control block was excluded. The five
new terminal-record cases pass. Additional synchronous mocks verify clean/no
request, monitor failure/one request/UNKNOWN, over-limit/one request/UNKNOWN,
active hook raises, closed hook only counts, live-after-join gives UNKNOWN, and
the exact repaired finally clears complete on inventory error. Every main
exception handler now invalidates completion. No real signal, thread, child
process, Wolfram kernel, Lean build or physical supervisor test was run by GPT.

Local's37 controls, six mutants and physical sleep/W1A/self-signal check at the
original revision3 are disclosed Local-reported evidence; they were read, not
rerun or retroactively authorized as a GPT physical stage. The current controls
function contains those original controls plus the five terminal cases; GPT
does not claim an independent full physical controls run. The reviewed source
paths and retained mock results are the basis for this one-stage agreement.

## Exact one-stage scope

| Input | SHA256 |
|---|---|
| trap_pair_notebook.py revision3a | `50eaa2ed2b803c2b33bd5c137366a72dd56e2638ae06a8d85b403cb2138b5acf` |
| W1A | `3f9089146c744e4910b3a1bb30ff2a62c102f33ceaf3bfb5b1f6dbf201a73883` |
| essay.md | `e1facac0647c0d2ece7d83c9011e83e3960545ad7865b12b7512b7faea004d16` |
| Rule30Submission.lean | `27f799f47eecf22f138967ac27ccbc14ab0dffb20f55f5dc29be800aa6b44fd6` |
| build_sub.wl | `1771b518d6071fd1537e5857c1a9afde21b449e22d088a7edf608bcd63dac02a` |
| read_nb_full.wl | `c5b89fb60f57bccee440983eeaaf65edeb37d434cca47025783bf25bd6787f44` |

Actual kit commit cc1e0e0e7c1ae8c971aec5c14aaabb47c7b8c554, toolchain4.35.0,
W1A source pins and explicit known-input admission. Exact command:
`python3 tests/probes/wolfram/trap_pair_notebook.py ABS_PIPELINE ABS_REPO ABS_FRESH_OUT`.
Require a quiet M5 with no competing research job, at most one baseline Wolfram
kernel, actual pressure/headroom preflight, fresh external OUT and no existing
pipeline/trap-pair folder. Stage includes its owned-process preflight, one
build_sub notebook build and one read_nb_full extraction. No full W1A experiment,
extra physical control run, automatic retry, submit call or scope widening.

Limits:1500s stage wall; build900s wall/childCPU and read300s wall/childCPU,
wall clamped to remaining stage. These two cumulative childCPU totals sum to at
most1200s; setup/monitor CPU is separate.6GiB sampled aggregate owned group RSS,
one Lean process by inherited sampler, maximum two globally inventoried Wolfram
kernels,10MiB per-step logs,64MiB artifacts in kit build trees+OUT,8MiB notebook,
5GiB minimum free disk, pressure level>=2 stop (inherited fallback when needed),
256MiB maximum swap growth. All failures/limits end this attempt.

6GiB allows room above the actual L9254.14GB group peak for Wolfram and LeanLink
work while leaving10GiB nominally for system/baseline allocations in16GiB. This
is not proof of available headroom: the baseline Wolfram kernel is outside that
owned group's RSS sum, so real pressure/free-memory observations are mandatory.
The guard is sampled group/process accounting, not a system-wide peak or hard
container limit. Group cleanup does not prove no detached descendant can exist;
any observed uncertainty must remain explicit and incomplete. The residual
asynchronous interruption during W1A finally is covered by outer owned-group
cleanup and final uncertainty, not claimed impossible.

Persistent side effects are intentional: staged submission sources/notebook and
installed pipeline scripts remain, previous scripts are retained in OUT. The
extra pipeline notebook copy is bounded by8MiB outside the64MiB counter; fixed
small input/script copies are outside that counter too. Original kernel-check
source/object restoration is not repeated by this notebook wrapper. Preserve
failed staging/recovery paths before any separately agreed retry.

## Required actual output read

Retain full receipts, build/read logs, resource provenance, both watchdog records,
final inventory/problems, kit before/after, staged/installed-script and notebook
hashes, notebook bytes, count.txt and all cell files with actual byte hashes.
No monitor errors, over-limit samples, live-after-join watchers, uncertain/remaining
kernels or terminal problems may be called complete. Record late self requests
honestly. The notebook must match the frozen essay/source and both copy hashes.
String hashes from read_nb_full are not exported-file hashes.

Build/read completion alone does not validate the nine outputs. The future gate
must inspect every cell exactly and bind the five Check headlines/66-constant
replay using check.json86abca97a1ecbf29da3f0c7d3ff79297e04ee09bd8c8e92f609342cb22f2839c.
That source/gate and its actual notebook outputs remain a named pending review.
