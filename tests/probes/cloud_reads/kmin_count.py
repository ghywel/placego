# Count sorted E28 targets (t = 68 + y, y in 0..54, sum 240) by residues mod 4 and derive the forced number of odd moves.
# Claim (Cloud): in the split-anchor model a bin's move parity is (t_i - a_i)/2 mod 2 (a_i = 0 for even bins); each reserved
# pair gives one anchor = 1 and one = 3 (mod 4), so k_min = |n1 - n3|/2 + n2 (x anchors = 1 to t = 1 bins leaves q/2 + n1 - 2x odd moves) where n_r = #targets = r (mod 4).
from functools import lru_cache
import collections
@lru_cache(None)
def f(rem, parts, cap, n1, n2, n3):
    if parts == 0: return 1 if rem == 0 and n1 == n2 == n3 == 0 else 0
    if rem < 0 or min(n1, n2, n3) < 0: return 0
    tot = 0
    for v in range(min(cap, rem), -1, -1):
        r = (68 + v) % 4
        tot += f(rem - v, parts - 1, v, n1 - (r == 1), n2 - (r == 2), n3 - (r == 3))
    return tot
K = collections.Counter(); Keven = collections.Counter(); total = 0
for n1 in range(9):
    for n2 in range(9 - n1):
        for n3 in range(9 - n1 - n2):
            c = f(240, 8, 54, n1, n2, n3)
            if c:
                k = abs(n1 - n3)//2 + n2; assert k % 2 == 0; K[k] += c; total += c
                if n1 == n3 == 0: Keven[n2] += c
print("total", total)
print("all E28 by forced odd moves k:", dict(sorted(K.items())))
print("even E28 by k (= #targets = 2 mod 4):", dict(sorted(Keven.items())), "sum", sum(Keven.values()))
