import itertools, collections
from e28lib import *
def positions(order, q, r):
    first, middle, last = order; A = 16 - q; R = 22 - q
    P = [0, 6, A, R, R + first, 22 - last, 22]
    assert 0 < A < 6 < R < R + first < 22 - last < 22 and len(set(P)) == 7, P
    return [p + r for p in P]
def valid(P):
    if max(P) > 27: return False
    labs = [label(p) for p in P]
    return len(set(labs)) == 7
def rule(a, b, c):
    q = a + b + c
    if q >= 13: return (a, b, c), 0
    if q == 12 and c == 4: return (4, 4, 4), 0
    if q == 12 and c == 5: return (a, b, c), 1
    if q == 11 and a <= 2: return (a, b, c), 1
    if q == 11 and a >= 3:
        rest = sorted([a, b, c]); rest.remove(3)   # one 3 goes last
        return (rest[0], rest[1], 3), 2
    raise ValueError
sub = collections.Counter(); targets = set(); n = 0
for a, b, c in itertools.combinations_with_replacement(range(1, 6), 3):
    q = a + b + c; Z = q - 10
    if not (1 <= Z <= 5): continue
    n += 1; sub[q] += 1
    order, r = rule(a, b, c)
    P = positions(order, q, r)
    assert valid(P), (a, b, c, order, r, P)
    first, middle, last = order
    # bins: 0=+v small at P0, 5=-Z at P1, 1=+u small at P2, 2,3,4 = first,middle,last at P3..P5, 6=-22 at P6, 7 neutral
    cyc = [(0, P[0]), (5, P[1]), (1, P[2]), (2, P[3]), (3, P[4]), (4, P[5]), (6, P[6])]
    t = realize([cyc], {0: 6, 1: 6}, {5: -Z, 2: first, 3: middle, 4: last, 6: -22, 7: 0})
    targets.add(t)
    # controls from MI101
    if q == 11:
        assert not valid(positions((a, b, c), q, 0)), "root0 should fail at q=11"
    if (a, b, c) == (3, 3, 5):
        assert not valid(positions((3, 3, 5), 11, 1)), "sorted root1 should fail for (3,3,5)"
    if (a, b, c) == (4, 4, 4):
        assert all(valid(positions((4, 4, 4), 12, rr)) for rr in range(6)), "all in-pool roots for (4,4,4)"
print("choices", n, "subtotals q11..15", [sub[q] for q in range(11, 16)], "distinct targets", len(targets))
dom = set()
for t in even_e28():
    e = [(x - 112)//2 for x in t[2:]]
    if t[0] == 68 and t[1] == 68 and -22 in e and sum(1 for x in e if x > 0) == 3 and sum(1 for x in e if x == 0) == 1 and max(e) <= 5 and sum(1 for x in e if x < 0) == 2:
        dom.add(t)
print("independent W=22 three-surplus domain", len(dom), "equal:", dom == targets)
