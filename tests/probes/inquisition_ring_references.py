#!/usr/bin/env python3
"""inquisition_ring_references.py: how long can depths (k, k+1) behind a black edge follow each small periodic
background? A census of M_ref(k) over the ring cycles of the edge frame (L1261, round 6, T-G).

RUN-ON:     cpu (Python 3 + numpy), minutes
COMMAND:    python3 tests/probes/inquisition_ring_references.py [PMAX=8] [QMAX=32] [KMAX=12]

Edge frame (PR69, kit Rule30FrozenRuler): X_0 = 1, X_1(t+1) = NOT X_1(t), X_j(t+1) = X_j(t) XOR (X_(j-1)(t) OR X_(j-2)(t))
for j >= 2. A periodic background is a two-sided solution R_j(t) of the same recurrence at every integer j that is
periodic in j with period p. Its time evolution is the ring map on Z/p (the kit's Rule30RingOrbits, mirrored), so
backgrounds are the cycles of that map. For every cycle with p <= PMAX and time period q <= QMAX (one representative per
rotation class), and every k <= KMAX, M_ref(k) is the longest initial run of ticks on which (X_k, X_(k+1)) equals
(R_(k+r)(t+s), R_(k+1+r)(t+s)), over all 2^(k+1) prefixes and all p*q alignments (r, s). Every onset is an initial state.
The horizon is H = 3k + 3q + 24; a run reaching H is printed as '>=H' (possibly unbounded).
Control: PR69's one-in-four ether (p = 4, q = 8) must give the proved M(k) = floor(2k/3) + 4 - [k = 0, 2 mod 6].
Predictions P-G1..P-G4: reports/inquisition-20261031.md (round 6), committed before this ran.
"""
import sys
import numpy as np

PMAX = int(sys.argv[1]) if len(sys.argv) > 1 else 12
QMAX = int(sys.argv[2]) if len(sys.argv) > 2 else 72
KMAX = int(sys.argv[3]) if len(sys.argv) > 3 else 12


def ring_step(s, p):
    """One step of R_j(t+1) = R_j(t) XOR (R_(j-1)(t) OR R_(j-2)(t)) on Z/p, state as a tuple."""
    return tuple(s[j] ^ (s[(j - 1) % p] | s[(j - 2) % p]) for j in range(p))


def cycles(p, qmax):
    seen = set()
    out = []
    for n in range(1 << p):
        s = tuple((n >> j) & 1 for j in range(p))
        orbit = [s]
        cur = s
        for _ in range(qmax):
            cur = ring_step(cur, p)
            if cur == s:
                break
            orbit.append(cur)
        else:
            continue
        if cur != s:
            continue
        q = len(orbit)
        # primitive spatial period only, and one representative per rotation class (with time shifts)
        if any(all(s[j] == s[(j + d) % p] for j in range(p)) for d in range(1, p) if p % d == 0):
            continue
        key = min(tuple(orbit[i][(j + d) % p] for j in range(p)) for i in range(q) for d in range(p))
        if key in seen:
            continue
        seen.add(key)
        out.append((p, q, orbit))
    return out


def traces(k, H):
    n = 1 << (k + 1)
    r = np.arange(n, dtype=np.int64)
    X = np.zeros((k + 2, n), dtype=np.uint8)
    X[0] = 1
    for j in range(1, k + 2):
        X[j] = (r >> (j - 1)) & 1
    a = np.empty((H, n), dtype=np.uint8)
    b = np.empty_like(a)
    for t in range(H):
        a[t], b[t] = X[k], X[k + 1]
        Y = X.copy()
        Y[1] = X[1] ^ X[0]
        Y[2:] = X[2:] ^ (X[1:-1] | X[:-2])
        X = Y
    return a, b


def M_ref(k, p, q, orbit, a, b, H):
    best = 0
    for r in range(p):
        for s in range(q):
            alive = np.ones(a.shape[1], dtype=bool)
            run = np.zeros(a.shape[1], dtype=np.int64)
            for t in range(H):
                st = orbit[(t + s) % q]
                alive &= (a[t] == st[(k + r) % p]) & (b[t] == st[(k + 1 + r) % p])
                if not alive.any():
                    break
                run += alive
            best = max(best, int(run.max()))
    return best


def main():
    refs = []
    for p in range(1, PMAX + 1):
        refs += cycles(p, QMAX)
    # PR69's one-in-four ether as a ring cycle: R_j(t) = e(t + 2j), p = 4, q = 8
    E8 = (1, 1, 0, 1, 0, 1, 0, 0)
    eth = [tuple(E8[(t + 2 * j) % 8] for j in range(4)) for t in range(8)]
    assert all(ring_step(eth[t], 4) == eth[(t + 1) % 8] for t in range(8)), "ether is a ring cycle"
    print(f"{len(refs)} ring cycles with p <= {PMAX}, q <= {QMAX} (primitive, one per rotation class)")
    want = [(2 * k) // 3 + 4 - (1 if k % 6 in (0, 2) else 0) for k in range(1, KMAX + 1)]
    rows = [[] for _ in refs]
    for k in range(1, KMAX + 1):
        Hmax = 3 * k + 3 * QMAX + 24
        a, b = traces(k, Hmax)
        for idx, (p, q, orbit) in enumerate(refs):
            H = 3 * k + 3 * q + 24
            m = M_ref(k, p, q, orbit, a[:H], b[:H], H)
            rows[idx].append(f">={H}" if m >= H else str(m))
        print(f"k={k} done", flush=True)
    for idx, (p, q, orbit) in enumerate(refs):
        row = rows[idx]
        is_ether = (p == 4 and q == 8 and any(tuple(orbit[0]) == tuple(eth[i][(j + d) % 4] for j in range(4))
                                              for i in range(8) for d in range(4)))
        tag = "  <- PR69 ether (control)" if is_ether else ""
        if is_ether:
            assert row == [str(x) for x in want], ("control failed", row, want)
        print(f"ref {idx:2d}: p={p} q={q:2d} state0={''.join(map(str, orbit[0]))}  M(1..{KMAX}) = {' '.join(row)}{tag}",
              flush=True)
    print("RING_REFERENCES_DONE")


if __name__ == '__main__':
    main()
