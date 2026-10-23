"""CL596 independent certificate audit, GPT, 2026-10-23.

If this holds, it checks the concrete width-12 data behind the physical channel
bound; the unbounded quantifier still rests on the separately read Lean proof.
Record searched: check_sound|channel.bridge|channel-12 -> specification, CL596.
Prediction: literal cellwise Rule 30, packed steps, and committed successor IDs
agree; 402 states, 48190 row occurrences; every integer weight inequality holds.
Counterfactuals: swapped labels, a false dead edge and zero source weight must
fail. Independent mechanism: per-cell truth table -> complete subset BFS versus
the frozen Lean data, without importing Cloud's Python generator. Unexpected
check: exact rational powers bound the rounded entropy rate; n=0 counting.
Caps: width exactly 12, 1000 states, 200000 row occurrences, 30 CPU/60 wall
seconds, 512 MiB address space, small JSON output. One run, no patch/retry or
width increase. Stop on any failed assertion or cap. No Lean build is claimed.
Outcome is appended in the review report; source remains unchanged after run.
"""
import ast
import hashlib
import json
import re
import resource
import signal
import time
from pathlib import Path

resource.setrlimit(resource.RLIMIT_CPU, (30, 30))
resource.setrlimit(resource.RLIMIT_AS, (512 * 1024**2, 512 * 1024**2))
signal.alarm(60)
start = time.monotonic()
path = Path('reports/wolfram-agents/submissions/channel-12/Rule30Submission.lean')
raw = path.read_bytes()
src = raw.decode()
graph = ast.literal_eval(re.search(r'def succ12[^\n]*:= (\[.*\])', src)[1])
weights = ast.literal_eval(re.search(r'def weights12[^\n]*:= (\[.*\])', src)[1])
R = int(re.search(r'def R12 : Nat := (\d+)', src)[1])
C = int(re.search(r'def C12 : Nat := (\d+)', src)[1])
D, M, DEAD = 10**9, 12, 1000000
assert len(graph) == len(weights) == 402

def literal(s, left, right):
    cells = [left] + [(s // 2**p) % 2 for p in range(M)] + [right]
    # Wolfram truth table index 4*l+2*c+r, not the packed XOR expression.
    return sum(((30 >> (4*cells[p]+2*cells[p+1]+cells[p+2])) & 1) * 2**p
               for p in range(M))

def packed(s, left, right):
    return (((s << 1) | left) ^ (s | (s >> 1) | (right << (M-1)))) & (2**M-1)

one = {}
for s in range(2**M):
    for left in (0, 1):
        for right in (0, 1):
            v = literal(s, left, right)
            assert v == packed(s, left, right)
            one[s, left, right] = v
images = {s: frozenset(one[one[s, 0, u], 1, v] for u in (0, 1) for v in (0, 1))
          for s in range(2**M)}
root = frozenset(range(2**M))
sets, ids, actual = [root], {root: 0}, []
rows = 0
for S in sets:
    rows += len(S)
    assert len(sets) <= 1000 and rows <= 200000
    pair = []
    for bit in (0, 1):
        T = frozenset(t for s in S if s % 2 == bit for t in images[s])
        if not T:
            pair.append(DEAD)
        else:
            if T not in ids:
                ids[T] = len(sets)
                sets.append(T)
            pair.append(ids[T])
    actual.append(tuple(pair))
assert actual == graph
assert rows == 48190

def closure(g):
    for i, pair in enumerate(g):
        for bit, j in enumerate(pair):
            T = set(t for s in sets[i] if s % 2 == bit for t in images[s])
            if j == DEAD:
                if T: return False
            elif not 0 <= j < len(sets) or not T <= sets[j]: return False
    return True

def weighted(w):
    at = lambda j: w[j] if 0 <= j < len(w) else 0
    return all(w[i] > 0 and D * (at(a) + at(b)) <= R * w[i]
               for i, (a, b) in enumerate(graph))

assert closure(graph) and weighted(weights)
bad = list(graph); bad[0] = tuple(reversed(bad[0]))
assert not closure(bad)
bad = list(graph); bad[0] = (DEAD, bad[0][1])
assert not closure(bad)
badw = list(weights); badw[0] = 0
assert not weighted(badw)
assert min(weights) == 803714697 and weights[0] == 174869380839
assert weights[0] <= C * min(weights) and C == 218
assert 1 <= C  # n=0 includes the empty word.
# Exact logarithm enclosure without a floating transcendental certificate:
# 0.2581 < log2(R/D) < 0.2582.
assert R**10000 > 2**2581 * D**10000
assert R**10000 < 2**2582 * D**10000
print(json.dumps({
    'verdict': 'PASS', 'source_sha256': hashlib.sha256(raw).hexdigest(),
    'states': len(sets), 'row_occurrences': rows, 'dead_edges': sum(j == DEAD for p in graph for j in p),
    'literal_step_comparisons': len(one), 'four_pair_images': 4*rows,
    'weight_rows': len(weights), 'R': R, 'D': D, 'C': C,
    'controls': ['swapped labels rejected', 'false dead edge rejected', 'zero source weight rejected',
                 'n=0 valid', 'exact entropy interval (0.2581,0.2582)'],
    'wall_seconds': round(time.monotonic()-start, 4),
    'maxrss_native': resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
}, sort_keys=True))
