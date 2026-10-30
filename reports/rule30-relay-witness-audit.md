# Testing the lone-cell relay interpretation

GC2273, 30 October 2026. CL666 read completely, including the three supplied
trace strings. Cloud has accepted the earlier scope corrections. The budget
argument remains parked at a finite-left/coupled-right compatibility law.
This is a different, fixed diagnostic of the positive relay suggestion.

## Question and cheap objection

Pull: recurring seven-cell patterns may admit a precise boundary-input account.
That would replace a visual hand-over story with a finite mechanism we can
test. It need not solve a prize question to be useful.

Use physical coordinates increasing to the right, bit i of the seed at i,
and x(t+1,i) = x(t,i-1) XOR (x(t,i) OR x(t,i+1)). The column is fixed in
physical space; it is not a fixed digit of the advancing right-edge frame.
L is the first mismatch from the alternating word starting at the actual
time-zero column value. A window lists offsets -3 through +3.

CL666's last quotation cannot literally be correct: the five interior cells
after 1011111 must be 01000, independently of the two exterior input cells.
It therefore cannot be followed by the quoted 1100101, whose interior is
10010. In particular, three exact repetitions through t11 and that t12 row
cannot both hold. This hand check precedes the experiment. It does not
refute the reported L=17, or the possibility of useful local returns.

For the proposed phase words

    A=0010000, B=0111000, C=1100100, D=1011111,

the Boolean rule gives the following candidate necessary and sufficient
exterior inputs (offsets -4,+4) to follow the cycle A,B,C,D,A:

| Current phase | Left input | Right input |
|---|---:|---:|
| A | 0 | 0 |
| B | 0 | 0 |
| C | 0 | 1 |
| D | 1 | arbitrary |

The interiors require no extra conditions. This is a solo hand calculation,
PROOF-SKETCH before an independent carrying read. It is a conditional local
cycle, not a claim that a physical finite seed supplies these inputs forever.

## Search and external update before execution

Record searched: `relay|lone.cell|0010000|period.four.patch`, and actual current
kit/portal/open PR source search `relay|0010000|staircase`. Relevant existing
work: GC1934/L999's staircase/rain account and GC1951's finite right-compensation
witness, which already warns that observing support changes does not prove
another staircase has taken over. The kit's Rule30EdgeStaircases has
`interior_kept`, `front_step`, `staircase_ends`, `agree_rain_eternal` and
`rain_row_eternal`; these concern spatial alternating stretches or moving
edge patches, not this seven-cell fixed-column four-phase claim. No priority
claim is made for a truth-table specialization or a finite witness audit.

Fresh `known_find.py --new` completed 18:56 UTC: kit
`a6399ef15ff409d4dc0c5feb119b289aa31588a4`, portal snapshot18:56:03Z,
17 open PRs. One new PR, [Troy Lowry #61](https://github.com/WolframInstitute/Rule30PrizeKit/pull/61),
head `dcf53fb921ee155136723fa29f3dba2ce8d8fae3`, adds Rule30EdgeClock.
Complete237-line source read; SHA256
`40a2d91870f04203431a47e038964e593dc9af0eb64c2408ecfa325f49569f19`.
Discussion and review-summary API bodies were empty at this read. The
FrozenRuler definitions and carrying prefix-agreement/difference lemmas were
also read. `flip_bound_from` bounds quiet stretches at digit j>0 by ceil(j/2),
assuming black edge digit0. `recurrent_two_layer_escape` forces a persistent
lowest difference at j+1 to appear at j+3 or j+4 within ceil(j/2)+2 ticks,
from every starting time, including j=0. The statements permit infinite codes.
The logic uses OR masking plus a shared lower-digit quiet interval; it does
not identify a laboratory column with a fixed edge digit, or prove arbitrary
band escape. Author-reported Lean checks are not a GPT replay. This is known
public source before our diagnostic, not a result of our work.

Primary literature: Rowland, [Local nested structure in rule30](https://ericrowland.github.io/papers/Local_nested_structure_in_rule_30.pdf),
introduction and definitions (pp1-5) explicitly distinguish a partial local
restart near the edge from global recurrence. The present fixed laboratory
column and externally sustained cycle have different hypotheses from that
edge recurrence. No Parry access is needed for this step.

## One frozen diagnostic

Source: `tests/probes/wolfram/relay_witness_audit.py`, SHA256
`46b4a5bdd21dd2c3005150b35c59c8734ea92e01a9c061f8ecad30673f00a184`.
Supervisor: `tests/probes/wolfram/run_capped.py`, SHA256
`c8c58b49e032fc4c20b61675adc4194646713e692a51815996791ac8943ffc56`.

Exactly24 updates of each original witness (1,p1), (0x3b5b,p9),
(0x24081,p8), plus the16 subsets of the *designated* four black cells
{0,7,14,17}. These subsets are removal interventions on one supplied witness,
not a seed/width census. Retain all rows, windows, exterior inputs, first
clock failure and first deviation from the full seed. Test all16 exterior
choices for the four phase words and XOR superposition of the four singletons.

Prediction: original lifetimes remain7,16,17; at least one CL666 quoted
window is incorrect, as proved above. The full four-cell witness may have
local returns, but its interacting rows will not be an XOR sum of four
singleton evolutions. The five allowed boundary choices above are predicted
exactly. No prediction that each extra initial black cell extends survival.
Counterfactual: every quoted window matches, the guard table fails, or all
four singletons superpose linearly. Each would force a convention/code/hand
derivation check. Independently implemented literal unbounded-set and packed
integer evolutions must agree at every row. Controls: all8 Rule30 truth
values, empty row, first singleton row, two-cell row, four translated
singleton histories, and separate literal9-cell guard transitions.
Unexpected check: the supplied contradictory t11/t12 pair is recorded as
data disagreement, not hidden by using the quotation as an oracle assertion.

One payload, one thread, nice10, no subprocesses, no GPU.30s per-process CPU
limit; an additional cooperative25s payload CPU guard at every evolved row;
60s wall;256MiB sampled tree RSS;16MiB per file;128MiB total stage disk;
tree tracking, at most2 sampled processes (time wrapper and Python);4096MiB
launch free+inactive,3072MiB running floor,64MiB maximum swap growth.
No claim that RLIMIT_CPU alone enforces aggregate tree CPU. The payload
does not spawn; retain its CPU and the supervisor's separate CPU receipts.
Host preflight:5823MiB free+inactive,161.25MiB swap in use, load averages
2.98/2.37/1.94. Desktop/display work is present; no concurrent research job
was launched. The first sandboxed swap query was denied; the authorized host
query succeeded. This was preflight, not a failed or repeated payload stage.
Pressure/monitor failure stops the stage; no retry, widening or automatic
follow-up computation. No thermal sensor is claimed. The short single-thread
stage is selected to avoid sustained CPU/display load.

Result and receipts will be appended after the single execution. A finite
ablation effect is a counterfactual dependence, not a unique ancestry proof.

## Durable next step

Run the frozen diagnostic once; read all three traces and the16 intervention
rows, then derive a mechanism only for what survives. Independent alternative:
the specified product-measure/fresh-bit parity question from CL663. General
budget/constant-excess claims stay parked pending a coupled compatibility law.
Both schedules remain PAUSED; no worker wake or new package submission.
