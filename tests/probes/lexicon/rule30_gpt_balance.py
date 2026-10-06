#!/usr/bin/env python3
"""Ordered-band discrepancy and exact periodic-orbit balance obstructions.

RUN-ON: CPU, Python 3.10+ (int.bit_count); seconds, modest memory.
COMMAND: python3 tests/probes/lexicon/rule30_gpt_balance.py
READ: RULE30-PRIZE.md 8.34/8.35; rule30_core.py OUTCOME; GPT G2 certificate.
PREDICTIONS before first run, 2026-10-06:
CB0 controls: truth-table spin identity holds for all 8 neighbourhoods;
    every output word of lengths 1..8 has exactly four one-step preimages;
    classified period-16 strip has black count 319993 through diagonal 39999;
    known 7-ring cycle spectrum is one fixed zero, seven 4-cycles, one 63-cycle.
CB1 blind, uncertain: all natural prefix discrepancies at widths 1000..53208
    have absolute value <=128 black cells, summed across all 16 time phases.
CB2 counterfactual: shuffle the 53208 diagonal black counts (seed 304); keep
    their distribution and final total fixed, but destroy spatial order.
    The maximum absolute shuffled prefix discrepancy exceeds both 100 and
    twice the natural maximum (prefixes of widths at least 1000).
CB3 candidate, uncertain: every nonzero exact cycle with power-of-two temporal
    period on rings of sizes 1..14 is spatially/time averaged exactly balanced.
    If false, print the first cycle with exact black/total counts for replay.
CB4 known obstruction: the 5-ring word with cells 0,1,2 black (integer 7)
    evolves by rotation, has period 5 and density 3/5. This blocks any blanket
    all-orbit balance claim, but is an infinite periodic row, not a finite seed.
REFUTED-BY: a control failure invalidates the diagnostic; CB1/2/3 failures
    refute only their respective conjectural statements. No inference about
    a single finite seed's limiting centre-column density.
OUTCOME, first run 2026-10-06: ALL CONTROLS PASS, exit 0.
CB0 PASSED: all truth-table/preimage controls; 7-ring spectrum correct;
    known strip black count 319993 reproduced.
CB1 REFUTED: max absolute discrepancy 216 at width 50086 (signed -216),
    exceeding 128. Width 53208 total 425490, discrepancy -174.
CB2 HELD: shuffled maximum 473 at width 29600 (signed -473), final total
    preserved. One shuffle is not a significance test.
CB3 REFUTED: 17 of 31 nonzero power-of-two cycles balanced; first biased
    cycle at ring size 7, period 4, black/total 13/28, states [1,67,100,63].
CB4 PASSED: 5-ring [7,25,14,19,28], density 15/25 = 3/5.
Pre-registration commit 503f6dc preceded the first run. The main push was
rejected with a GitHub server error; a branch push was pending. Later remote
inspection confirmed the pre-registration on the branch. Do not assert its
server publication completed before the run.

ADDENDUM, before its run (append 'shuffle' to COMMAND): quantify CB2 with
1000 shuffled populations, seeds 40000..40999, eight CPU workers. Statistic
is maximum absolute prefix discrepancy over widths 1000..53208. Preserve
all diagonal weights and final total exactly. SH0 control: natural statistic
216; all shuffles preserve total. SH1 blind: at most 5% of shuffled statistics
are <=216; natural order has stronger cancellation than 95% of permutations.
Also report the plus-one randomisation p = (1 + count<=natural)/1001 and
median/min/max; no inference about balance of the core or infinite widths.
OUTCOME of shuffle: not yet run.
"""
import concurrent.futures
import collections
import importlib.util
import pathlib
import random


def ring_step(v, n):
    mask = (1 << n)-1
    left = ((v << 1) & mask) | (v >> (n-1))
    right = (v >> 1) | ((v & 1) << (n-1))
    return left ^ (v | right)


def cycles(n):
    seen = set()
    for initial in range(1 << n):
        if initial in seen:
            continue
        path, index, v = [], {}, initial
        while v not in seen and v not in index:
            index[v] = len(path)
            path.append(v)
            v = ring_step(v,n)
        if v in index:
            yield path[index[v]:]
        seen.update(path)


def controls():
    okay = True
    for a in (0,1):
        for b in (0,1):
            for c in (0,1):
                x,y,z = 1-2*a,1-2*b,1-2*c
                out = 1-2*(a ^ (b | c))
                okay &= 2*out == x*(y+z+y*z-1)
    for m in range(1,9):
        counts = collections.Counter()
        for v in range(1 << (m+2)):
            output = 0
            for j in range(m):
                a,b,c = ((v >> (j+s)) & 1 for s in (0,1,2))
                output |= (a ^ (b | c)) << j
            counts[output] += 1
        okay &= len(counts) == 1 << m and set(counts.values()) == {4}
    spectrum = collections.Counter(len(c) for c in cycles(7))
    okay &= spectrum == {1:1,4:7,63:1}
    print('CB0 local/preimage/7-ring controls', okay, dict(spectrum), flush=True)
    return okay


def discrepancy(weights, start=1000):
    p, total, maximum = 16, 0, (0,0,0)
    for width, weight in enumerate(weights,1):
        total += weight
        delta = total - width*(p//2)
        if width >= start and abs(delta) > maximum[0]:
            maximum = abs(delta),width,delta
    return maximum,total


def band():
    here = pathlib.Path(__file__).resolve().parent
    spec = importlib.util.spec_from_file_location('gpt_cycles',here/'rule30_gpt_cycles.py')
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    words,p,_,branch,_ = mod.classify(53208)
    weights = [v.bit_count() for v in words]
    okay = p == 16 and branch == 53208 and sum(weights[:40000]) == 319993
    natural,total = discrepancy(weights)
    shuffled = weights[:]
    random.Random(304).shuffle(shuffled)
    null,null_total = discrepancy(shuffled)
    print(f'CB0 band control {okay}; known total {sum(weights[:40000])}',flush=True)
    print(f'{"HELD" if natural[0] <= 128 else "REFUTED"} CB1: max(abs,width,signed) {natural}; final total {total}; final discrepancy {total-8*len(weights)}',flush=True)
    held = null[0] > max(100,2*natural[0])
    print(f'{"HELD" if held else "REFUTED"} CB2: shuffled max {null}; total preserved {total == null_total}',flush=True)
    return okay and total == null_total


def ring_audit():
    candidates, balanced, witness = 0,0,None
    for n in range(1,15):
        for cycle in cycles(n):
            period = len(cycle)
            if cycle == [0] or period & (period-1):
                continue
            candidates += 1
            black = sum(v.bit_count() for v in cycle)
            cells = n*period
            balanced += 2*black == cells
            if 2*black != cells and witness is None:
                witness = n,period,black,cells,cycle
    print(f'{"HELD" if witness is None else "REFUTED"} CB3: {balanced}/{candidates} power-of-two nonzero cycles balanced; first witness {witness}',flush=True)
    wave, v = [],7
    for _ in range(5):
        wave.append(v)
        v = ring_step(v,5)
    okay = v == 7 and len(set(wave)) == 5 and all(x.bit_count() == 3 for x in wave)
    print(f'CB4 {okay}: 5-ring travelling cycle {wave}; black/total {sum(x.bit_count() for x in wave)}/25',flush=True)
    return okay


def init_shuffle():
    global SHUFFLE_BASE
    here = pathlib.Path(__file__).resolve().parent
    spec = importlib.util.spec_from_file_location('gpt_cycles',here/'rule30_gpt_cycles.py')
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    words,p,_,_,_ = mod.classify(53208)
    SHUFFLE_BASE = [v.bit_count() for v in words]


def one_shuffle(seed):
    weights = SHUFFLE_BASE[:]
    total = sum(weights)
    random.Random(seed).shuffle(weights)
    maximum, final = discrepancy(weights)
    return maximum[0], final == total


def shuffle_audit():
    here = pathlib.Path(__file__).resolve().parent
    spec = importlib.util.spec_from_file_location('gpt_cycles',here/'rule30_gpt_cycles.py')
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    words,p,_,_,_ = mod.classify(53208)
    natural,_ = discrepancy([v.bit_count() for v in words])
    with concurrent.futures.ProcessPoolExecutor(max_workers=8, initializer=init_shuffle) as pool:
        results = list(pool.map(one_shuffle,range(40000,41000)))
    vals = sorted(v for v,_ in results)
    count = sum(v <= natural[0] for v in vals)
    okay = natural[0] == 216 and all(kept for _,kept in results)
    print(f'SH0 {okay}; natural {natural[0]}; permutations 1000; count <= natural {count}',flush=True)
    print(f'{"HELD" if count <= 50 else "REFUTED"} SH1: p_plus_one {(count+1)/1001:.6f}; min {vals[0]}; median {(vals[499]+vals[500])/2}; max {vals[-1]}',flush=True)
    print('ALL CONTROLS PASS' if okay else 'CONTROL FAILURE')
    return not okay


def main():
    okay = controls()
    okay &= band()
    okay &= ring_audit()
    print('ALL CONTROLS PASS' if okay else 'CONTROL FAILURE')
    return not okay


if __name__ == '__main__':
    import sys
    raise SystemExit(shuffle_audit() if sys.argv[1:] == ['shuffle'] else main())
