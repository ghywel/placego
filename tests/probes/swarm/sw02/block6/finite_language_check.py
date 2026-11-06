#!/usr/bin/env python3
"""Fixed PE2.1 finite premises and XP3.1 local-balance controls.

No graph width, word length or sample horizon adapts to an outcome. Conclusions
are finite computations, not a Lean replay or an assertion of right finiteness.
"""
import hashlib
import json
import os
from pathlib import Path

import numpy as np
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import connected_components


WORDS = ['010', '1001', '10001', '01101', '01110', '011110', '0111110', '10110']
DRIVER = (0, 0, 1, 1)


def rulebit(a, b, c, rule):
    return (rule >> ((int(a) << 2) | (int(b) << 1) | int(c))) & 1


def scalar_step(s, r, center, width, rule):
    return sum(rulebit(center if j == 0 else (s >> (j - 1)) & 1,
                       (s >> j) & 1, r if j + 1 == width else (s >> (j + 1)) & 1, rule) << j
               for j in range(width))


def successors(width, rule):
    n = 1 << width
    ids = np.arange(4 * n, dtype=np.int64)
    phase, s = ids // n, ids % n
    left = ((s << 1) | np.asarray(DRIVER, dtype=np.int64)[phase]) & (n - 1)
    ans = []
    for r in (0, 1):
        right = (s >> 1) | (r << (width - 1))
        if rule == 30:
            out = left ^ (s | right)
        elif rule == 90:
            out = left ^ right
        elif rule == 150:
            out = left ^ s ^ right
        else:
            raise ValueError(rule)
        ans.append(((phase + 1) % 4) * n + out)
    return ids, ans


def graph(width, rule=30):
    ids, succ = successors(width, rule)
    n = len(ids)
    G = csr_matrix((np.ones(2 * n, dtype=np.int8),
                    (np.concatenate([ids, ids]), np.concatenate(succ))), shape=(n, n))
    G.sum_duplicates()
    nc, labels = connected_components(G, directed=True, connection='strong')
    sizes = np.bincount(labels, minlength=nc)
    # A phase advances by one modulo four, so there is no single-vertex cycle.
    assert all(np.all(s != ids) for s in succ)
    cyc = sizes[labels] > 1
    internal = [labels == labels[s] for s in succ]
    return ids, succ, labels, sizes, cyc, internal


def spell(width, data, word):
    ids, succ, labels, sizes, cyc, internal = data
    n = 1 << width
    active = (ids < n) & cyc & ((ids & 1) == int(word[0]))
    for g in word[1:]:
        for _ in range(4):
            nxt = np.zeros(len(ids), dtype=bool)
            for s, edge in zip(succ, internal):
                start = np.flatnonzero(active & edge)
                nxt[s[start]] = True
            active = nxt
        active &= (ids & 1) == int(g)
    return int(np.count_nonzero(active))


def balance_controls():
    assert all(rulebit(a, b, c, 30) == (a ^ (b | c))
               for a in (0, 1) for b in (0, 1) for c in (0, 1))
    # Ring evolution is not a bijection: both all-white and all-black map white.
    assert [rulebit(a, a, a, 30) for a in (0, 1)] == [0, 0]
    result = {}
    for radius in (1, 2, 3):
        P = radius + 4
        counts = [0] * (1 << radius)
        for q in range(1 << P):
            row = [(q >> j) & 1 for j in range(P)]
            for _ in range(2):
                row = [rulebit(row[(j - 1) % P], row[j], row[(j + 1) % P], 30)
                       for j in range(P)]
            counts[sum(row[j] << j for j in range(radius))] += 1
        assert counts == [16] * (1 << radius)
        result[str(radius)] = {'ring_length': P, 'each_local_word_preimages': 16}
    return result


def main():
    root = Path(os.environ['CAPPED_OUT']) / 'finite-artifacts'
    root.mkdir()
    control = {}
    for rule in (30, 90, 150):
        ids, succ = successors(3, rule)
        for v in ids:
            p, s = divmod(int(v), 8)
            for r in (0, 1):
                assert int(succ[r][v]) % 8 == scalar_step(s, r, DRIVER[p], 3, rule)
        if rule != 30:
            d = graph(5, rule)
            present = {w: spell(5, d, w) for w in WORDS}
            assert all(present.values())
            control[str(rule)] = present
    result = {'scalar_successor_and_sibling_controls': control,
              'local_balance_controls': balance_controls(), 'widths': {}}
    print(json.dumps({'controls': result}), flush=True)
    for width in (13, 16, 17):
        d = graph(width)
        found = {w: spell(width, d, w) for w in WORDS}
        assert not any(found[w] for w in WORDS[:-1])
        assert bool(found['10110']) == (width < 17)
        sizes = d[3]
        assert {13: 3349, 16: 11372, 17: 16465}[width] in sizes
        r = {'cyclic_component_sizes': sorted((int(s) for s in sizes if s > 1), reverse=True),
             'internal_word_endpoints': found,
             'scc_labels_sha256': hashlib.sha256(d[2].astype('<i4').tobytes()).hexdigest()}
        result['widths'][width] = r
        print(json.dumps({'width': width, 'result': r}), flush=True)
        del d
    (root / 'result.json').write_text(json.dumps(result, indent=2) + '\n')


if __name__ == '__main__':
    main()
