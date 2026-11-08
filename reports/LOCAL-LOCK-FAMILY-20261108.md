# The period-7 lock family: two locks, no third found

*Local, L1593, 8 November 2026, 15:46 UTC. My pull after Block 8, at the owner's word. All counts are COMPUTED by Local, a self-check; the component table is a reading of GPT's GC2696 data. Probes: `tests/probes/swarm/sw02/lockfamily/`.*

**Question.** Lock-7 (closed at width 30) and lock-7b (closed at width 45) both lock column 1 into the word `0101000` beside the alternating column. BN-13 found that their period-14 column words agree on columns 1 to 9 and then part. If the tree of period-14 column words has infinitely many closed branches, the right statement for period 7 would be a family theorem, as `InFamily` is for period 2.

**Verdict: no evidence of a family.** The finite data are consistent with exactly two closed period-7 locks. The methods used here cannot see a lock that closes only above width 45 with a very small basin, so that question stays open.

## What was done

1. **The two locks' words** ([`words.py`](../tests/probes/swarm/sw02/lockfamily/words.py), [output](../tests/probes/swarm/sw02/lockfamily/words.out)). Late rows of 74 and 3793493 have 27 and 50 period-14 columns. Under a common time shift of 4 ticks their words agree on columns 1 to 9 exactly and first differ at column 10. Lock-7b has no spatial repeat up to a time shift below 30 (one stray pair), and lock-7's 27 words occur nowhere inside lock-7b as a time-shifted block. So the two locks are not a doubling family or a shifted copy. Predictions (a) to (c) held; the 27 against BN-13's 25 locked columns depends on the sampled tick.
2. **Neighbourhoods** ([`neighbours.py`](../tests/probes/swarm/sw02/lockfamily/neighbours.py), [output](../tests/probes/swarm/sw02/lockfamily/neighbours-N5000.out)). I kept each lock's late row through column k, randomized 200 cells beyond, and ran 6000 ticks: 5,000 samples per k, 75,000 in all.
   - The controls held: k = 45 gives 100 % lock-7b and k = 30 gives 100 % lock-7.
   - Lock-7b is re-entered only for k ≥ 25: 7, 143, 275 and 2,816 of 5,000 at k = 25, 30, 35, 40.
   - Lock-7 is re-entered steeply between k = 20 and 25 (1,302 and then 4,326 of 5,000).
   - About 5 to 7 % of lock-7b's neighbours fall into lock-7 at every k up to 35, roughly eight times the base rate of 0.7 % for random right halves.
   - There were no candidates: every sample ended in a known lock, the gate trap or period 2. My prediction gave a third set a chance of 0.3, and none appeared.
3. **Block 3's complete cores** ([`locked_table.py`](../tests/probes/swarm/sw02/lockfamily/locked_table.py), [output](../tests/probes/swarm/sw02/lockfamily/locked_table.out); GPT's GC2696 xx data, with the gate trap, ether family, lock-7 and lock-7b removed as targets).
   - No CLOSED component exists in any arm: full xx through width 40, pruned through 42.
   - So in the exact two-cell model, every closed set of width at most 40 lies in the gate trap, the ether family or lock-7, and lock-7 is the only closed period-7 set there. Lock-7b closes at 45.
   - The leaky components with the period-7 word are two small ones at widths 27 and 28 (the lock-7 word, 7 and 8 nodes) and, at width 40, one of period 63 and one of period 21. The period-21 one has word (0101000)³, 78 nodes, column-1 gaps {2, 5}, and no lock-7 or lock-7b cut window.
4. **The width-40 period-21 component** ([`third.py`](../tests/probes/swarm/sw02/lockfamily/third.py), [output](../tests/probes/swarm/sw02/lockfamily/third.out)). From its first window, with 6,000 random tails of 0 to 200 cells, 94 % went to the gate trap and 6 % to lock-7. None stayed. A first run lost its samples to an argument bug (the imported header reset N), was fixed, and is kept in the script's history.

## What it teaches

- Closed period-7 locks are rare even among period-14 branches of the shared trunk: the tree has thousands of words per depth, but only two branches close by width 45.
- Lock-7 is a strong attractor near the trunk; lock-7b has a narrow basin, about 25 specific columns.
- The kit-ready statement remains the one already proved, `Rule30SidewaysLocks`: CQ01 for every right half that enters lock-5, lock-7 or lock-7b. A period-7 family theorem has no support yet.

## Limits and what would change the picture

- Every finite statement here is at a fixed width or in a sampled ensemble.
- A lock closing only at width 46 or more, with a basin below about 1/5,000 of these ensembles, would not have been seen.
- Full xx cores at widths 43 to 50 would settle the next range. They are an Intel job and are not proposed here unasked.

**Record searched:** `record_find` on period-14, lock-7b, PE-1 with chain, InFamily, column word tree and period-14 tree; BN-13's report, results and `l7deep.py`; SW02-BLOCK3-JOB and GPT-BLOCK3-RESULTS; `known_find` on period 14 with column, locked columns, lock family, period-7 lock and SevenLock with family (hits: the ether-and-wall trap entries, an empty-half period-7 transient in R30-20261028-e34744, and trace-edge entries; none is a family of closed period-7 locks).
