# independent count of sorted E28 targets by number of odd entries q (offsets y in 0..54, sum 240, sorted 8-tuples)
from functools import lru_cache
import collections
@lru_cache(None)
def f(rem, parts, cap, q):
    """sorted tuples of `parts` offsets each <= cap, sum rem, with exactly q odd offsets (offset odd <=> target odd)"""
    if parts == 0: return 1 if rem == 0 and q == 0 else 0
    if rem < 0 or q < 0: return 0
    total = 0
    for v in range(min(cap, rem), -1, -1):
        total += f(rem - v, parts - 1, v, q - (v % 2))
    return total
print({q: f(240, 8, 54, q) for q in range(0, 9)})
