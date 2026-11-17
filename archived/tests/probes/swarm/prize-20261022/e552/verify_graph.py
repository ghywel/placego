# Independent check of a graph file "v: nbrs": symmetric, loopless, C4-free (A^2 off-diagonal <= 1), min degree.
import sys
import numpy as np
fn = sys.argv[1]
rows = [l.split(':') for l in open(fn) if l.strip()]
N = len(rows)
A = np.zeros((N, N), dtype=np.int64)
for r in rows:
    v = int(r[0])
    for u in r[1].split():
        A[v, int(u)] = 1
assert (A == A.T).all(), 'not symmetric'
assert np.trace(A) == 0, 'loops'
A2 = A @ A
off = A2 - np.diag(np.diag(A2))
deg = A.sum(1)
print(fn, 'N=%d' % N, 'max common nbrs=%d' % off.max(), 'C4-free=%s' % (off.max() <= 1), 'mindeg=%d maxdeg=%d' % (deg.min(), deg.max()),
      'degree counts', {int(d): int((deg == d).sum()) for d in sorted(set(deg))}, 'edges=%d' % (A.sum() // 2),
      'triangles=%d' % (np.trace(A @ A @ A) // 6))
