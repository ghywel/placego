# Finite physical past: first source checkpoint

GC2286. GPT owns this source preparation; posting is unassigned. Local remains
the intended owner of static Package A on confirmed return. This follow-on
module packages the reviewed G121/G122/L077 finite-core argument; it does not
claim new mathematics for finite injectivity, endpoint growth or root descent.
The exact [source/prior-art comparison](../../../GPT-PROOF-DELIVERY-RESUMPTION-20261030.md#gc2282-package-b-has-an-older-reviewed-core-and-a-precise-formalization-gap)
records current kit declarations and separates other parent notions.

[Rule30FinitePastDraft.lean](Rule30FinitePastDraft.lean) imports the actual
Rule30Realization evolution through a core-only two-module dependency closure.
It states finite support using explicit black endpoints. It supplies endpoint
uniqueness/growth, right-asymptotic injectivity, finite-iterate injectivity,
ancestor endpoint/depth bounds, the small-width roots, and existence/uniqueness
of the finite root and age. The final theorem includes the depth bound and
uniqueness in one interface. All-white is excluded and separately fixed.

Current status: **UNCOMPILED, no independent source read**. The older hand
argument is carried; this new formal transcription is not. Direct small proofs
repeat current-kit ingredients to avoid importing the Mathlib equivalents
package and its unrelated closure, with explicit credit. The inverse criterion,
normalized finite-word bijection/count and age-distribution corollary are not
in this module. The mixed-driver infinite-tail family is excluded entirely.

## GC2287: one frozen development pilot

Prediction: the source and [small guards](FinitePastGuard.lean) elaborate under
the installed Lean4.33.1, with no sorry axiom. Counterfactual: an elaboration,
source-binding or control failure leaves the module unvalidated and ends this
stage; inspect the exact failure before any separately justified later stage.
No automatic retry, wider budget, download or dependency substitution.

Record searched: GC2282's G121/G122/L077 and actual current-kit sources; the
complete20:00external refresh at kit a6399ef15ff409d4dc0c5feb119b289aa31588a4,
69portal entries and17openPRs; GC2283's new PR61 leaf/guard comparison; Kari's
primary finite-configuration discussion. This is source preparation for known
structure. No renewed novelty decision or repeated keyword loop is needed.

Exact frozen inputs, SHA256:

- Jen: `0700944834df40a026191a7fe4c1ab22114c6509a319afc1d71877e30a22c6bc`.
- Realization: `da6444504fc3d9789ccdae0f042f63e980b6f0de1ce23958d5387e6d4999eac5`.
- Draft: `a46243a1ac7ed1732f6bbce9986c9434152f934c1e3d62ec251dee3e8c0acf3f`.
- Guard: `464868dfd7435abf6f842c92b9144ef3949149e56c9b1724d706a39e0806abf1`.
- [Pilot driver](../../../../tests/probes/wolfram/finite_past_lean_pilot.py):
  `d0a1195ce226db9125d3c65aa0e1c63d040eb6bf72543b0e7a78c79e36594729`.

All four source hashes are checked before the driver compiles unchanged copies
in the fresh capped output directory. Four serial compiler invocations build
Jen, Realization, the draft and the guard. The guard uses literal width-one
and width-two words and the one-step support endpoints, independently of the
abstract root construction; it prints eight selected axiom closures. An
additional negative-control invocation must reject an ill-typed attempt to
use the zero-exclusion theorem as False. This is not the official checker.
Unexpected check: all-white must remain outside the domain despite being a
fixed finite-support row, and width-two must be handled without a width-one
parity assumption. The positive guards and negative-control result must remain
separate in the receipt. Failure before a control leaves it unexecuted.

### Resource envelope and actual host

Intel8physical/16logical,16GiB. One job, one Lean process at a time, at most
2compiler threads, driver nice10 verified. At20:24UTC the approved host-level
preflight reads free+inactive about6185MiB, swap used161.25MiB, load1.60/2.02/2.18,
16available CPUs, speed/scheduler limits100 and no recorded thermal/performance
warning. No competing research compiler was identified. The earlier sandbox
attempt denied sysctl/ps and could not read thermal status; no job was launched
on that attempt. The authorized host-level monitor read succeeded; raw preflight
is retained locally and will accompany the result.

Launch only through `run_capped.py` with **120s per-process CPU backstop,
300s wall,768MiB sampled tree RSS,16MiB/file,128MiB stage disk,4096MiB launch
free+inactive,3072MiB running floor,64MiB swap-growth stop**, tree tracking and
at most4observed processes (time wrapper, driver, sole compiler and transient
monitor helper). Driver uses a separate **110aggregate CPU-second stop** over
its own CPU plus all reaped direct children and the sole live compiler's CPU,
queried every0.25s. It also stops at280wall seconds. The aggregate claim comes
from this live sum, not from inherited per-process limits. Sampled enforcement
has scheduling/measurement latency; the10second margin is not an exact kernel
bound. Outer run_capped/time overhead is reported separately. No native-code
compilation or additional compiler descendants are requested; tree monitoring
and the process cap remain active.

Thermal/performance status is checked before every invocation, every2seconds
during an invocation, and at completion; reduced speed/scheduler capacity,
warning or unavailable/unparseable status stops the stage. CPU monitor failure
also stops it. run_capped handles memory, swap, disk, wall and owned-process
cleanup. Pressure/thermal/monitor failure redirects to light source reasoning,
with no automatic retry or relaxed cap. The stage is scratch-only and uses no
GPU. No output is written into the source repository.

The pilot is development validation on4.33.1 only. Required Lean4.35/current
unchanged-checker replay, independent carrying read, essay, posting and live
portal verification remain distinct, pending stages.
