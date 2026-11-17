#!/usr/bin/env python3
"""GC915: independent fixed witness audit of Cloud SE/CL134 at 2b55b6cb.

Record searched: one-parity/1010100010100000 + physical/87867 ->30 hits in6 files.
Predictions registered before execution, 2026-10-10 01:30 BST:
 P1: a=1010100010100000 has least period 16, odd weight 5, one-parity support;
     literal B reaches zero after87867 steps at cap 16.
 P2 (unexpected): its repeated cap 32 lift absorbs after the SAME87867 steps.
 P3: both cap 32 integrations yield entry weight 8 and satisfy every local equation.
 C1: physical q 4 source1010 absorbs after8 steps.
 C0 counterfactual: odd source parity implies physical ancestry must FAIL;
     source10001000 has a nonabsorbing B cycle (transient 29, cycle 28).
 REFUTED-BY: wrong period, count, zero detection, closure or control values.
No imports of SE/ZF, no whole-tree or TM6b certificate replay. Arrays of literal
binary cells and cyclic local equations provide an independent implementation.
OUTCOME, 2026-10-10 01:30 BST: P1/P2/P3/C1/C0 ALL PASS.
 Least period 16, weight 5, all odd ticks white; absorption 87867 at both caps.
 Both entry weights8; every literal local compatibility equation passes.
 Physical q4 absorption8; source17 transient 29/cycle 28. Fixed-witness replication
 only: not the whole SE tree classification, its rarity count or TM6b parsing.
"""


def backward(x, y):
    n = len(x)
    return tuple(y[(t + 1) % n] ^ (x[t] | y[t]) for t in range(n)), x


def absorb(a, cap):
    st = (a, (0,) * len(a))
    for step in range(cap + 1):
        if not any(st[0]) and not any(st[1]):
            return step
        st = backward(*st)
    return None


def cycle(a):
    st = (a, (0,) * len(a))
    seen = {}
    for step in range(201):
        if st in seen:
            return seen[st], step - seen[st]
        seen[st] = step
        st = backward(*st)
    return None


def children(x, y):
    out = []
    for start in (0, 1):
        z = [start]
        for t in range(len(x) - 1):
            z.append(x[t] ^ (y[t] | z[t]))
        if x[-1] ^ (y[-1] | z[-1]) == start:
            out.append(tuple(z))
    return out


def compatible(x, y, z):
    return all(z[(t + 1) % len(x)] == (x[t] ^ (y[t] | z[t])) for t in range(len(x)))


def main():
    a = tuple(map(int, '1010100010100000'))
    period = next(k for k in (1, 2, 4, 8, 16) if all(a[t] == a[(t+k) % 16] for t in range(16)))
    n16, n32 = absorb(a, 88000), absorb(a+a, 88000)
    p1 = period == 16 and sum(a) == 5 and not any(a[1::2]) and n16 == 87867
    p2 = n32 == n16 == 87867
    weights, valid = [], True
    zero = (0,) * 32
    cs = children(a+a, zero)
    valid &= len(cs) == 2
    for c in cs:
        ones = children(zero, c)
        valid &= ones == [(1,) * 32]
        e, = children(c, ones[0])
        f, = children(ones[0], e)
        valid &= compatible(a+a, zero, c) and compatible(zero, c, ones[0])
        valid &= compatible(c, ones[0], e) and compatible(ones[0], e, f)
        weights.append(sum(f))
    p3 = valid and weights == [8, 8]
    c1 = absorb(tuple(map(int, '1010')), 10) == 8
    ctl = cycle(tuple(map(int, '10001000')))
    c0 = ctl == (29, 28)
    print('P1', p1, 'period', period, 'weight', sum(a), 'depth16', n16)
    print('P2 unexpected', p2, 'depth32', n32)
    print('P3', p3, 'entry weights', weights, 'local compatibility', valid)
    print('C1', c1, 'C0', c0, 'nonphysical cycle', ctl)
    assert p1 and p2 and p3 and c1 and c0
    print('ALL CHECKS PASS')


if __name__ == '__main__':
    main()
