#!/usr/bin/env python3
"""Independent CL754 replay: explicit edges, queue peeling, deletion certificates.

Read only the fixed 43 saved cores. No Cloud code import, wider lift, cycle sweep,
SAT call or assumption that a finite path starts in a bi-infinite core.
"""
import argparse
from collections import deque
from fractions import Fraction
import hashlib
import json
from pathlib import Path
import numpy as np

GAPS = [2, 5] * 4 + [3, 3, 5, 3, 5, 5, 5, 5] + [2, 5] * 7 + [3, 3, 5, 3, 5, 5, 5, 5]
PERIOD = sum(GAPS)
TRACE = [0] * PERIOD
pos = 0
for gap in GAPS:
    TRACE[pos] = 1
    pos += gap
assert PERIOD == 145


def move(x, exterior, width):
    z = x + (exterior << width)
    y = (z << 1) ^ (z | (z >> 1))
    return (((y << 1) | 1) ^ (y | (y >> 1))) & ((1 << width) - 1)


def scalar_move(x, exterior, width):
    row = [(x >> i) & 1 for i in range(width)] + [exterior & 1, exterior >> 1]
    for boundary in (0, 1):
        row = [(boundary if i == 0 else row[i-1]) ^ (row[i] | row[i+1])
               for i in range(len(row)-1)]
    return sum(b << i for i, b in enumerate(row))


def make_graph(sets, width):
    nodes = [(s, x) for s, xs in enumerate(sets) for x in sorted(xs)]
    index = {node: i for i, node in enumerate(nodes)}
    successors = [[] for _ in nodes]
    predecessors = [[] for _ in nodes]
    for i, (s, x) in enumerate(nodes):
        targets = {index[((s+1) % PERIOD, y)] for e in range(4)
                   if ((s+1) % PERIOD, (y := move(x, e, width))) in index}
        successors[i] = sorted(targets)
        for j in targets:
            predecessors[j].append(i)
    return nodes, successors, predecessors


def peel(successors, predecessors):
    n = len(successors)
    incoming = list(map(len, predecessors)); outgoing = list(map(len, successors))
    rank = [0] * n; reason = [-1] * n
    max_in = [0] * n; max_out = [0] * n
    queue = deque()
    for i in range(n):
        if not incoming[i] or not outgoing[i]:
            rank[i] = 1; reason[i] = 0 if not incoming[i] else 1; queue.append(i)
    while queue:
        i = queue.popleft()
        for j in successors[i]:
            incoming[j] -= 1; max_in[j] = max(max_in[j], rank[i])
            if not rank[j] and incoming[j] == 0:
                rank[j] = max_in[j] + 1; reason[j] = 0; queue.append(j)
        for j in predecessors[i]:
            outgoing[j] -= 1; max_out[j] = max(max_out[j], rank[i])
            if not rank[j] and outgoing[j] == 0:
                rank[j] = max_out[j] + 1; reason[j] = 1; queue.append(j)
    return rank, reason


def check_certificate(successors, predecessors, rank, reason):
    for i, depth in enumerate(rank):
        if depth:
            neighbors = predecessors[i] if reason[i] == 0 else successors[i]
            assert all(0 < rank[j] < depth for j in neighbors), ('bad deletion', i)
        else:
            assert any(rank[j] == 0 for j in predecessors[i]), ('no predecessor', i)
            assert any(rank[j] == 0 for j in successors[i]), ('no successor', i)


def synchronous(successors, predecessors):
    alive = set(range(len(successors))); ranks = [0] * len(successors); r = 0
    while True:
        gone = {i for i in alive if not any(j in alive for j in successors[i])
                or not any(j in alive for j in predecessors[i])}
        if not gone:
            return ranks
        r += 1
        for i in gone:
            ranks[i] = r
        alive -= gone


def longest_dag(successors, predecessors):
    degree = list(map(len, predecessors)); distance = [0] * len(degree)
    queue = deque(i for i, d in enumerate(degree) if d == 0); seen = 0
    while queue:
        i = queue.popleft(); seen += 1
        for j in successors[i]:
            distance[j] = max(distance[j], distance[i] + 1)
            degree[j] -= 1
            if degree[j] == 0:
                queue.append(j)
    assert seen == len(degree), 'unexpected directed cycle'
    return max(distance, default=-1)


def main(source, out):
    out.mkdir(parents=True, exist_ok=True)
    checks = 0
    for width in range(1, 7):
        for x in range(1 << width):
            for e in range(4):
                assert move(x, e, width) == scalar_move(x, e, width)
                checks += 1
    previous = None; rows = []; margin = 0; hashes = {}; rejection_done = False
    for width in range(1, 44):
        path = source / ('core_W%d.npz' % width)
        hashes[path.name] = hashlib.sha256(path.read_bytes()).hexdigest()
        with np.load(path, allow_pickle=False) as z:
            expected = [set(map(int, z['s%d' % s])) for s in range(PERIOD)]
            assert all(len(expected[s]) == len(z['s%d' % s]) for s in range(PERIOD))
        candidates = [{TRACE[s]} for s in range(PERIOD)] if width == 1 else [
            xs | {x | (1 << (width-1)) for x in xs} for xs in previous]
        assert all(all(x & 1 == TRACE[s] for x in xs) for s, xs in enumerate(candidates))
        nodes, succ, pred = make_graph(candidates, width)
        ranks, reason = peel(succ, pred)
        check_certificate(succ, pred, ranks, reason)
        if width <= 6 or width == 43:
            assert ranks == synchronous(succ, pred)
        retained = [set() for _ in range(PERIOD)]
        for (s, x), r in zip(nodes, ranks):
            if r == 0:
                retained[s].add(x)
        assert retained == expected, ('Cloud core mismatch', width)
        if not rejection_done and any(ranks):
            bad = ranks.copy(); i = next(i for i, r in enumerate(ranks) if r); bad[i] = 0
            try:
                check_certificate(succ, pred, bad, reason)
            except AssertionError:
                rejection_done = True
            else:
                raise AssertionError('false retained node accepted')
        depth = max(ranks, default=0)
        row = {'width': width, 'candidates': len(nodes), 'edges': sum(map(len, succ)),
               'core': sum(map(len, retained)), 'max_deletion_rank': depth,
               'margin_before': margin, 'margin_after': margin + depth}
        if width >= 7:
            row['source_low7'] = [sorted({x & 127 for x in retained[s]}) for s in (20, 103)]
        if width >= 9:
            row['gate_quartet'] = [sorted({(x >> 5) & 15 for x in retained[s]}) for s in (25, 108)]
        if width == 7:
            assert row['source_low7'] == [[64], [64]]
        if width == 12:
            assert row['gate_quartet'] == [[11], [11]]
        if width == 21:
            labels = []
            for s in (20, 103):
                words = set()
                for x in retained[s]:
                    cells = [(x >> i) & 1 for i in range(width)]; word = 0
                    for t in range(14):
                        word |= cells[7] << t
                        cells = [(t % 2 if i == 0 else cells[i-1]) ^ (cells[i] | cells[i+1])
                                 for i in range(len(cells)-1)]
                    words.add(word)
                labels.append(sorted(words))
            row['source_labels'] = labels
            assert labels == [[4520], [4520]]
        if width == 43:
            assert not row['core']
            row['candidate_longest_edges'] = longest_dag(succ, pred)
            maximum = 2 * margin + row['candidate_longest_edges']
        np.savez_compressed(out / ('rank_W%d.npz' % width),
                            phase=np.array([s for s, x in nodes], dtype=np.uint8),
                            window=np.array([x for s, x in nodes], dtype=np.uint64),
                            rank=np.array(ranks, dtype=np.uint32),
                            reason=np.array(reason, dtype=np.int8))
        rows.append(row); previous = retained; margin += depth
        print(json.dumps(row), flush=True)
    assert rejection_done
    B = 1
    while 145*(B//2) + (62 if B % 2 else 0) <= maximum:
        B += 1
    result = {'status': 'independent finite graph replay; hand transfer awaits carry',
              'scalar_move_controls': checks, 'all43_cores_match': True,
              'wrong_retained_node_rejected': rejection_done, 'widths': rows,
              'input_hashes': hashes, 'sum_deletion_margins': margin,
              'maximum_periodic_trace_edges_bound': maximum,
              'forbidden_consecutive_47_pairs': maximum // 145 + 1,
              'forbidden_zero_slack_return_run': B,
              'conditional_liminf_cost_lower_bound': str(Fraction(145, 2) + Fraction(7, 2*B)),
              'single_47_passage_exclusion_claimed': False}
    (out / 'result.json').write_text(json.dumps(result, indent=2) + '\n')
    print('CYCLE_CORE_RANK_AUDIT_PASS')


if __name__ == '__main__':
    p = argparse.ArgumentParser(); p.add_argument('--cores', type=Path, required=True)
    p.add_argument('--out', type=Path, required=True); a = p.parse_args(); main(a.cores, a.out)
