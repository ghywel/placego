#!/usr/bin/env python3
"""When can the Hall condition of Theorem 2 (Q-split) fail?  For heavy a (omega>=3) let Q(a) = largest prime power
exactly dividing a, w_a = a/Q(a), t_a = floor(M/w_a).  The condition fails iff for some i there are >= i heavy
a <= M with t_a < i.  Such a has all prime-power factors < i and a <= M < i*w_a.  For each i compute the maximum
over M of #{a in S_i : a <= M < i*w_a} (interval stabbing).  First i where max >= i is i0; then Theorem 2 gives
g(A,I) <= 2n for every A with fewer than i0 heavy elements, in particular g(n) <= 2n for n < i0."""
import sys, time
T0 = time.time(); TL = 300

def primes_upto(n):
    return [p for p in range(2, n + 1) if all(p % q for q in range(2, int(p ** .5) + 1))]

def run(i):
    ps = primes_upto(i - 1)
    opts = []
    for p in ps:
        pw, q = [], p
        while q < i:
            pw.append(q); q *= p
        opts.append(pw)
    events = []
    cnt = 0
    def dfs(k, a, Q, w_parts, om):
        nonlocal cnt
        if time.time() - T0 > TL:
            raise TimeoutError
        if k == len(ps):
            if om >= 3:
                w = a // Q
                lo, hi = a, i * w - 1
                if lo <= hi:
                    events.append((lo, 1)); events.append((hi + 1, -1)); cnt += 1
            return
        dfs(k + 1, a, Q, w_parts, om)
        for q in opts[k]:
            dfs(k + 1, a * q, max(Q, q), w_parts, om + 1)
    dfs(0, 1, 1, None, 0)
    events.sort()
    best, cur, bestM = 0, 0, None
    for x, d in events:
        cur += d
        if cur > best:
            best, bestM = cur, x
    return best, bestM, cnt

try:
    for i in range(6, 200):
        best, M, cnt = run(i)
        flag = 'VIOLATION POSSIBLE' if best >= i else 'ok'
        print('i=%3d  |S_i intervals|=%8d  max stab=%4d at M=%s  %s  t=%.0fs' % (i, cnt, best, M, flag, time.time() - T0), flush=True)
        if best >= i:
            break
except TimeoutError:
    print('TIMEOUT at i=%d' % i, flush=True)
