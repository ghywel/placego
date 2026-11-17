#!/usr/bin/env python3
"""Exact bipartite distinct-distance counts for structured lattice families (Erdos #661).

Every family is put on an integer grid (coordinates scaled by s) with an integer quadratic form
  square: N(a,b) = a^2 + b^2        hex: N(a,b) = a^2 - a*b + b^2   (a + b*omega)
P = the n points of lattice L (+ coset shift cP) closest to the origin, Q likewise with shift cQ.
D(P,Q) = number of distinct N(p - q), computed exactly from the support of 1_P * 1_{-Q} (FFT, integer-rounded).
Also prints n*E_{PxQ}[1/r(N(p-q))] where r(m) = number of grid-lattice vectors of the *full* lattice of norm m
(only meaningful for unshifted P=Q families; printed for all as a diagnostic).
Time limit built in: stops starting new sizes after TLIM seconds.
"""
import sys, time, math
import numpy as np
from scipy.signal import fftconvolve

TLIM = 420.0
T0 = time.time()

def pts(form, s, shift, n):
    """n points of (s*Z^2 + shift) closest to 0 in the Euclidean metric of the form; integer coords."""
    R = int(math.sqrt(n) * 1.3 + 5) * s
    a = np.arange(-R, R + 1)
    A, B = np.meshgrid(a, a, indexing='ij')
    A = A.ravel(); B = B.ravel()
    m = ((A - shift[0]) % s == 0) & ((B - shift[1]) % s == 0)
    A = A[m]; B = B[m]
    if form == 'sq':
        N = A * A + B * B
    else:
        N = A * A - A * B + B * B
    ang = np.arctan2(B, A)
    order = np.lexsort((ang, N))
    A = A[order][:n]; B = B[order][:n]
    return A, B

def norm(form, A, B):
    return A * A + B * B if form == 'sq' else A * A - A * B + B * B

def dcount(form, PA, PB, QA, QB):
    lo = min(PA.min(), PB.min(), QA.min(), QB.min())
    hi = max(PA.max(), PB.max(), QA.max(), QB.max())
    W = hi - lo + 1
    gP = np.zeros((W, W)); gP[PA - lo, PB - lo] = 1
    gQ = np.zeros((W, W)); gQ[QA - lo, QB - lo] = 1
    f = fftconvolve(gP, gQ[::-1, ::-1])      # f[z] = #{(p,q): p - q = z}, index offset W-1
    f = np.rint(f).astype(np.int64)
    ia, ib = np.nonzero(f > 0)
    za = ia - (W - 1); zb = ib - (W - 1)
    Nz = norm(form, za, zb)
    vals = np.unique(Nz)
    return len(vals), int((vals == 0).any()), za, zb, f[ia, ib], Nz

FAM = {
    # name: (form, scale, shiftP, shiftQ)
    'sq P=Q':            ('sq', 1, (0, 0), (0, 0)),
    'sq Q=P+(1/2,1/2)':  ('sq', 2, (0, 0), (1, 1)),
    'sq Q=P+(1/2,0)':    ('sq', 2, (0, 0), (1, 0)),
    'hex P=Q':           ('hex', 1, (0, 0), (0, 0)),
    'hex Q=deep hole':   ('hex', 3, (0, 0), (2, 1)),
    'hex Q=edge mid':    ('hex', 2, (0, 0), (1, 0)),
}

def main():
    sizes = [int(x) for x in sys.argv[1:]] or [100, 400, 1600, 6400, 25600]
    print('family | n | D(P,Q) incl.0 | has0 | D*sqrt(ln n)/n | D(PuQ) sym 2n pts | Dsym*sqrt(ln 2n)/(2n)')
    for n in sizes:
        for name, (form, s, cP, cQ) in FAM.items():
            if time.time() - T0 > TLIM:
                print('TIME LIMIT'); return
            PA, PB = pts(form, s, cP, n)
            QA, QB = pts(form, s, cQ, n)
            D, has0, *_ = dcount(form, PA, PB, QA, QB)
            # symmetric count of the union (2n points if disjoint), nonzero distances only
            U = np.unique(np.stack([np.concatenate([PA, QA]), np.concatenate([PB, QB])], axis=1), axis=0)
            UA2 = U[:, 0]; UB2 = U[:, 1]
            Ds, h0s, *_ = dcount(form, UA2, UB2, UA2, UB2)
            Ds -= h0s
            m = len(UA2)
            print(f'{name:18s} | {n:6d} | {D:7d} | {has0} | {D*math.sqrt(math.log(n))/n:.4f} | {Ds:7d} (m={m}) | '
                  f'{Ds*math.sqrt(math.log(m))/m:.4f}', flush=True)

if __name__ == '__main__':
    main()
