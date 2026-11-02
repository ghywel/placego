#!/usr/bin/env python3
"""GC2398: exhaustive clause predicate/sign controls; no SAT or real export."""
import itertools
from guarded_wall_export import clause

count = 0
for j in (2,3):
    D = j+11
    for pattern in (0,1,2):
        t = 7
        k = 19
        cols = [((1 << 1024)-1) if (pattern == 1 or (pattern == 2 and i % 2)) else 0 for i in range(1024)]
        for word in (0,1,128,255):
            lits = clause(1024, cols, k, D, j, t, word)
            for vals in itertools.product((0,1), repeat=j+7):
                actual = dict(zip(range(2,j+9), vals))
                d = {i: actual[i] ^ ((cols[(k-i) % 1024] >> t) & 1) for i in actual}
                forbidden = d[j] == 1 and all(d[i] == 0 for i in range(2,j)) and all(
                    d[j+h] == ((word >> (h-1)) & 1) for h in range(1,9))
                sat = any(actual[(abs(lit)-t-1)//1024] == (lit > 0) for lit in lits)
                assert sat == (not forbidden)
                assert all(abs(lit) <= (D+2)*1024 for lit in lits)
                count += 1
for D,j,word in ((12,2,0),(13,3,0),(13,2,256)):
    try:
        clause(1024,[0]*1024,0,D,j,0,word)
    except ValueError:
        pass
    else:
        raise AssertionError('unsupported boundary/word accepted')
print('PASS:',count,'independent Boolean predicate/sign cases; three invalid guards rejected')
