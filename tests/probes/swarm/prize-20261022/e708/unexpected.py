#!/usr/bin/env python3
"""Unexpected check: is the Erdos-Suranyi closeness condition 2 p1^2 > pl^2 needed for cost 4 at n = 3?
Exhaustive over all interval positions (CRT residues) for pair-products of three primes that VIOLATE it."""
import sys, time
sys.argv = [sys.argv[0], '420']
sys.path.insert(0, '.')
import g708
for P in ([3, 5, 7], [5, 7, 11], [3, 5, 11], [2, 3, 5]):
    A = sorted([P[0]*P[1], P[0]*P[2], P[1]*P[2]])
    t = time.time()
    try:
        v, w, tot = g708.worst_interval(A)
        print('primes %s A=%s 2p1^2>pl^2:%s  worst min|B|=%d over all %d positions  witness=%s  (%.0fs)' %
              (P, A, 2*P[0]**2 > P[2]**2, v, tot, w, time.time() - t), flush=True)
    except TimeoutError:
        print('TIMEOUT on', P, flush=True); break
