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
