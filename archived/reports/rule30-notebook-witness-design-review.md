# L1028 witness-first proposal: pre-run review

GPT, GC1980, 27 October 2026. Reviewed complete L1028 and its appended design
at `14c04869514e127b97aacee75ee30cd074aee822`, against GC1977–1979's actual
source, initial language and retained results. No simulation or SAT was run.

**Verdict: accept simulation-first witness discovery as a method; amend the
pilot before launch.** The advertised all-36 prediction contradicts the known
death controls. No executable accompanies this proposal, so this is a design
review, not executable or launch acceptance. Schedules remain paused.

## 1. The target is the age-34 language, not the initial language

The previous gate asked whether E_34^8 = E_100^8. It did not ask whether all
36 words in E_0^8 survive. Five words in the retained initial list already have
the following exclusions from the two reproduced length-7 controls:

| Initial length-8 word | Known dying factor | Offset | First absence no later than |
|---|---|---:|---:|
| `00010001` | `0010001` | 1 | 31 |
| `00100010` | `0010001` | 0 | 32 |
| `10010001` | `0010001` | 1 | 31 |
| `01000101` | `1000101` | 1 | 33 |
| `10001010` | `1000101` | 0 | 34 |

For example, `00100010` at age 100 would contain `0010001` at age 100,
contradicting its absence from age 32 onward. These are factor implications
of accepted controls, not new death computations. There may be other early
exclusions: deleting these five does **not** establish the exact age-34 set.
W1 as written is therefore already refuted; finding any of these five at age
100 would be a validation failure, not new evidence against the controls.

Use either an exact, evidence-backed E_34^8 target list, or classify every word
in the initial list by one of:

- absence at age 34, supported by retained evidence;
- a physically replayed witness at age 100;
- unresolved.

The first two categories covering the whole initial list prove the desired
equality by nestedness; any unresolved entry leaves the gate incomplete.
Simulation alone may collect the second category without pretending to have
completed the first. In particular, `00001001` is a legitimate positive target:
GC1979 retained its age-34 witness, with age 100 still unresolved.

## 2. Missing samples do not establish a new death

For independent sampled rows with probability p of the target event, the chance
of no hit in N rows is (1-p)^N. We have no uniform positive lower bound on p for
surviving words. Therefore zero hits in 200,000 rows cannot distinguish absence
from rarity. Overlapping windows in one row are not independent trials either.

Replace the counterfactual by: **some target words remain unwitnessed under the
frozen sampling budget; their membership stays unresolved.** They may be ranked
for a later exact query, but absence in the sample supplies no age-43 lower
bound. To establish a new death after 43, retain a witness at an age at least 43
and an UNSAT result at the next age, with the agreed verification status.

Stage S's adjacent test is mathematically sound when A(w) is an actual witnessed
age: UNSAT at A(w)+1 gives the boundary, SAT only improves the lower bound, and
UNKNOWN gives neither. A(w) is undefined for an entirely unseen word. It is a
sample maximum, never a claim to be the true last possible occurrence. Stage S
needs separate exact scope and bounds; it must not start automatically at W's end.

## 3. Freeze the physical cone and boundary convention

For an n-letter window starting at visible age J, the last required physical
time is H = 2(J+n-1), and its right light cone uses initial cells 1 through H+1.
For n=8 and J=100, that is H=214 and **215 initial right cells**.

The proposed width 2J+4=204 is not the full arbitrary-input cone. It can still
define valid examples if the initial tail is explicitly zero and the simulation
faithfully evolves that infinite zero-tail completion. A clipped or periodically
wrapped 204-cell array would instead impose an unwanted boundary. Avoid the
ambiguity: sample 215 fair bits, declare all further initial bits zero, and
evolve a shrinking cone for 214 updates, with wall x(t,0)=t mod 2.

Freeze J_max=100, not the unbounded phrase '100 or later'. Save every complete
length-8 window at starts 0 through 100. If another horizon is desired, name it
and recompute H and the input width before the source is frozen. If an example
is eventually used at age A>100, nestedness justifies E_100, and restarting its
right row at physical time 2(A-100) constructs an explicit age-100 witness.

## 4. Concrete requirements for the revised pilot

- One process, no solver; at most 200,000 independently sampled initial rows.
  Freeze the PRNG algorithm, seed, bit order and batching. Do not change the seed
  or add draws after seeing missing words. Stop early only if the frozen witness
  targets are all obtained, and retain the actual draw count.
- Use the already retained `00001000` age-100 row as a deterministic positive
  replay control. Do not demand that random sampling rediscover it or count an
  injected control as a random success. Include the known dead words as negative
  controls and exhaustive tiny-cone cross-checks of any optimized simulator.
- Replay every retained witness with GC1977's literal-table evaluator: full
  initial row, wall phase, physical time and observed word. Compare optimized
  and literal cell evolutions in the small controls; a shared simulation routine
  called twice is not an independent implementation check.
- Freeze 600 CPU seconds, 750 wall seconds, sampled process-group RSS 512 MiB,
  output/disk 64 MiB and per-file 16 MiB. Use the existing supervisor's launch
  free+inactive 4096 MiB, stop below 1024 MiB or swap growth above 256 MiB;
  document its sampled measurements. No GPU, detached process or automatic rerun.
- Retain code/input hashes, PRNG details, draw count, observed-word counts,
  witness rows and replay results, unresolved targets and terminal resource
  receipt. Raw evidence belongs in the private store. No frequency or confidence
  claim without its actual sampling model.

**Next action for Local:** revise the target and counterfactual and supply the
actual bounded executable, control fixtures and intended host for source review.
These requirements give a useful witness-discovery pilot, not approval to run
the original impossible all-36 prediction or the later solver stage.

Reasoned verdict: the method is worth implementing after these repairs. Gut
verdict: this is exactly the cheap adversarial hand check the owner's method
calls for; preserve the useful idea while correcting what would count as success.

## L1029 executable review and freeze (GC1981)

Read the entire 212-line proposed source at
`6972f20c` (original SHA256
`3662b071633362b6f2aa235450d67c07e95e207093d6d1fa778fec61354bd05f`).
The big-integer transition has the correct orientation:
`((R << 1) | (t & 1)) XOR (R | (R >> 1))`, masked after dropping the far-right
cell. The 215-cell cone, 214 updates and windows starting at 0..100 carry.
The fixed positive row is exactly 215 bits and byte-equal to GC1978 q00002.
The source's tiny-cone check compares every cell, and terminal witnesses use
the independent literal evaluator. Those runtime checks have not been run here.

GPT amended the source directly to finish the review rather than send another
round of implementation requests:

- retain the initial row and draw number behind each latest observed age, then
  replay those certificates too; an integer age alone cannot support Stage S;
- checkpoint partial unverified evidence on new age-100 witnesses and every
  5,000 draws, so a resource stop does not erase the collected examples;
- retain offending rows, detect words outside the initial language, and prevent
  a control violation from also reporting `gate_complete=true`;
- record terminal reason, literal-evaluator hash, Python version and age-100
  row counts separately from distinct-word coverage.

The retained primary 230bc7 abstract/source were checked, source SHA256
`39c0f0376e26d86e6be1c8eeb8874f39e1fc1fd89bd9b37e78dd87a7aafd7660`,
from `cited/gc1938-portal-morning/`. Its empty-right entry theorem begins at
sample146, and its reported96% numerical observation concerns eventual entry.
It uses a black-first wall, sampling odd physical times; our initial ensemble
is white-first, sampling even times. No matching distribution or age100 entry
bound has been supplied. Moreover, a small fraction of rows can cover many
distinct words. The amended P_B is only Local's exploratory fewer-than10-of19
coverage prediction, with the complementary outcome explicitly retained. It
cannot confirm/refute that external trap result. Internal3/5 spacing is not a
test for membership in its829-window invariant set.

The31 nonexcluded candidates are still **not** an exact E_34 list; other early
exclusions may remain. The pilot may be useful even if it cannot close the gate.
No missing sample is promoted to a new death, and no automatic Stage S follows.

**Accepted source for one Local M5 pilot:**
`tests/probes/wolfram/notebook_witness_pilot.py`, SHA256
`e25dd2cff3740df3c364ce744ca3c837f77a7f5f1b9302bf80af423466df0a29`.
Dependencies frozen:

- literal evaluator: `6e51527c1198218ed6d1f50e57c09a922ae29713b5bb2258298e7c763f9ff5ee`;
- supervisor: `38ed7189ce5911d06e03e50295995d2a1d5c15451db9367da5cdbf299d2fef6c`;
- MFW list: `80eee0a74712632a4339f7cd0a7776f23dd2a45fea8e934b79e6f0aba390d378`.

One process, seed1976, at most200,000 draws. Use a fresh destination:

```sh
python3 tests/probes/wolfram/run_capped.py \
  --out /private/tmp/gc1981-notebook-witness-pilot \
  --cpu 600 --wall 750 --rss-mib 512 --file-mib 16 --disk-mib 64 \
  --launch-free-mib 4096 --min-free-mib 1024 --swap-growth-mib 256 \
  -- python3 tests/probes/wolfram/notebook_witness_pilot.py
```

Check all frozen hashes before launch. The600s limit covers the sole simulation
process; supervisor CPU is reported separately. The570s checkpoint guard leaves
room for replay but does not override the hard limit. A partial checkpoint is
not a completed or replayed result. Retain launcher/time receipts and all nested
artifacts, including failures; no retries, larger sample, changed seed, solver,
GPU or schedule restart. Local's L1029 records the owner's execution direction;
this freeze completes GPT's requested source review, not an additional job.
Local should verify the small GPT retention edits before launch and stop on any
disagreement. Syntax compilation and static source/control binding checks passed;
runtime controls and execution outcomes remain pending on Local. GPT ran no pilot.
