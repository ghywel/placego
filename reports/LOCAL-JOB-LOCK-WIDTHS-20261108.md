# Job request for GPT (Intel): closed sets above width 40 in the two-cell window graph

*Local, L1594, 8 November 2026, 16:06 UTC. At the owner's word ("submit the full width job to run on GPT"). Frozen before any run. The program is Block 3's [`lift.c`](../tests/probes/swarm/sw02/block3/lift.c) (xx mode, exact two-cell moves) with the targets file [`targets.txt`](../tests/probes/swarm/sw02/block3/targets.txt), as audited in GC2696. GPT owns the execution; any code change is GPT's, stated and controlled before launch.*

## Question

[L1593](LOCAL-LOCK-FAMILY-20261108.md) found no third closed period-7 lock. Block 3's cores (GC2696) show no CLOSED component outside the targets through width 40 (42 pruned): lock-7 is the only closed period-7 set of closure width ≤ 40, and lock-7b closes at 45. Two things remain:
- Is there a closed set of the two-cell graph (a lock) closing only above width 45?
- Do the two leaky LOCKED components with the lock-7 word at width 40 ever become closed as they lift? These are rank 15, period 21, word (0101000)³, 78 nodes, and rank 9, period 63, 379 nodes.

## Arms

**Arm A, pruned lift (the main arm).** `lift --mode xx --prune-from P`, resuming where GC2696 stopped if possible (otherwise from P = 34 as before), to `--wmax 50` or the first cap.
- Report at every completed width the same SCC table as before, with the CLOSED flag, and every LOCKED component whose period is a multiple of 7, with its word, size, leaks and cut counts.
- Lock-7b's cut lies in X's lineage at 38–40 (7 cut windows), so this arm carries it to 45, where it becomes a target.
- **Positive control:** at W = 45 the 33 lock-7b windows are removed as targets, and an independent scalar closure of those 33 windows under xx passes, as in GC2696.

**Arm B, LOCKED-lineage lift (small).** Lift only the windows of the W = 40 LOCKED components whose period is a multiple of 7 (ranks 9 and 15 of the full xx40 core) and their children, to W = 60 or the first cap. Report at each width the cyclic SCCs of the lifted lineage with CLOSED status, judged in the full xx graph: every move counts, including moves into targets.
- This needs either a dump of those two components at 40 (`--dump`) or a new `--lift-components` option. Either is GPT's change, with a control: lifting lock-7's 66-window lineage from 30 gives the 66-window closed set at every width it is checked.

## Predictions, frozen

| # | Prediction | Conf. | Counterfactual |
|---|---|---:|---|
| A1 | No CLOSED component outside the targets at any completed width of arm A | 0.85 | A CLOSED component appears: a new lock, or another closed set |
| A2 | X and Y both persist as UNRESOLVED to the widest completed width | 0.65 | One breaks into LOCKED or GAP35 pieces |
| A3 | The widest completed width is between 44 and 47 (node cap) | 0.6 | Below 44: memory, not nodes, binds first |
| B1 | Both period-7-word lineages lose their cyclic core, or stay leaky LOCKED, through W = 60; no CLOSED child | 0.8 | A CLOSED child: a third period-7 lock |

**What it would teach.** A1 and B1 holding extend "no closed set but the known ones" to higher widths and narrow the period-7 family to lock-7 and lock-7b in that range. A new CLOSED component would be a new lock. Local would then certify it by kernel check, as in `Rule30SidewaysLocks`, find a finite right half that enters it, and submit it.

## Caps (Intel standard)

`run_capped.py --track-tree --rss-mib 8192 --swap-growth-mib 4096 --min-free-mib 1024`, one serial worker, nice 10, the lift's own `--max-nodes` (default 1.2 × 10⁸) as the node stop.
- Arm A: at most 3 CPU hours and 4 wall hours.
- Arm B: at most 20 CPU minutes.
- Thermal and pressure stops as in GC2696.
- Stop at the first cap and report the widest completed width; no retry with larger caps without the owner.
- Dumps stay outside git; the SCC tables, gap words and receipts go to the shared store by digest.

## Outputs to the ledger

Per width: core size, X and Y sizes and gaps, the CLOSED flag of every component, and each period-7k LOCKED component's word, size, leaks and cut counts. Also the positive controls, the resources used and the widest completed width.

**Record searched:** L1593 and its report; GC2696's results and xx, xxp and pq SCC tables; SW02-BLOCK3-JOB §§2–7 (targets, move rules, P7); `lift.c`'s header and options; BN-13's lock data.
