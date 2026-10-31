#!/usr/bin/env python3
"""inquisition_diagonals.py: the single seed's diagonals from both edges, and where the centre reads them (T-E).

RUN-ON:     cpu (Python 3 + numpy), a few seconds
COMMAND:    python3 tests/probes/inquisition_diagonals.py [KR=36] [KL=60]

Right diagonals D_k(t) = x(t - k, t): D_k(t+1) = D_k(t) XOR (D_(k-1)(t) OR D_(k-2)(t)), D_k(0) = [k = 0].
Left diagonals  L_k(t) = x(-t + k, t): L_k(t+1) = L_(k-2)(t) XOR (L_(k-1)(t) OR L_k(t)),  L_k(0) = [k = 0].
Missing indices are white. Both are checked against direct Rule 30 for t < 64, with c(t) = D_t(t) = L_t(t).
Prints, per k: the right diagonal's least period (it is purely periodic: the map on the first k + 1 bits is
invertible bit by bit), and the left diagonal's settle time tau(k) and eventual least period. Predictions:
reports/inquisition-20261031.md (T-E), committed before this ran.
"""
import sys
import numpy as np

KR = int(sys.argv[1]) if len(sys.argv) > 1 else 36
KL = int(sys.argv[2]) if len(sys.argv) > 2 else 60


def rule30_rows(T):
    width = 2 * T + 3
    row = np.zeros(width, dtype=np.uint8)
    row[T + 1] = 1
    rows = [row.copy()]
    for _ in range(T):
        new = np.zeros_like(row)
        new[1:-1] = row[:-2] ^ (row[1:-1] | row[2:])
        row = new
        rows.append(row.copy())
    return rows, T + 1


def right_states(K, T):
    mask = (1 << K) - 1
    s, out = 1, np.zeros(T, dtype=np.uint64)
    for t in range(T):
        out[t] = s
        s = (s ^ ((s << 1) | (s << 2))) & mask
    return out


def left_states(K, T):
    mask = (1 << K) - 1
    s, out = 1, np.zeros(T, dtype=np.uint64)
    for t in range(T):
        out[t] = s
        s = ((s << 2) ^ ((s << 1) | s)) & mask
    return out


def bit(states, k):
    return ((states >> np.uint64(k)) & np.uint64(1)).astype(np.uint8)


def least_period_from(seq, t0):
    tail = seq[t0:]
    n = len(tail)
    p = 1
    while 2 * p <= n:
        if np.array_equal(tail[p:], tail[:-p]):
            return p
        p *= 2
    return None


def main():
    # control against direct Rule 30
    T0 = 64
    rows, off = rule30_rows(T0)
    R, L = right_states(64, T0), left_states(64, T0)
    for t in range(T0):
        for k in range(min(64, 2 * t + 1)):
            assert bit(R[t:t + 1], k)[0] == rows[t][off + t - k], ("right", t, k)
            assert bit(L[t:t + 1], k)[0] == rows[t][off - t + k], ("left", t, k)
    centre = [rows[t][off] for t in range(T0)]
    assert all(centre[t] == bit(R[t:t + 1], t)[0] == bit(L[t:t + 1], t)[0] for t in range(T0))
    print("CONTROL_PASS: both recursions match direct Rule 30 for t < 64; c(t) = D_t(t) = L_t(t)")

    # right diagonals: purely periodic, least period of each
    TR = 1 << 21
    R = right_states(KR, TR)
    full = least_period_from(R, 0)
    print(f"right: joint period of D_0..D_{KR-1} = {full} (2^{full.bit_length()-1})" if full else "right: joint period > window")
    print("right diagonals: k, first 16 values, least period, period > k")
    rp = {}
    for k in range(KR):
        seq = bit(R, k)
        p = least_period_from(seq, 0)
        rp[k] = p
        print(f"  D_{k:<2d} {''.join(map(str, seq[:16]))}  period {p}  {'yes' if (p and p > k) else 'NO'}")

    # left diagonals: settle time and eventual period
    TL = 1 << 15
    L = left_states(KL, TL)
    print("left diagonals: k, settle time tau, eventual period, tau > k, tau/k")
    lt = {}
    for k in range(KL):
        seq = bit(L, k)
        p = least_period_from(seq, TL // 2)
        assert p is not None and p <= 2 ** max(0, k - 2) or k < 2, ("Jen bound", k, p)
        tau = TL // 2
        while tau > 0 and seq[tau - 1] == seq[tau - 1 + p]:
            tau -= 1
        lt[k] = (tau, p)
        print(f"  L_{k:<2d} tau {tau:4d}  period {p:3d}  {'yes' if tau > k else 'NO'}  {tau / k if k else 0:.3f}")
    print("SUMMARY right periods:", [rp[k] for k in range(KR)])
    print("SUMMARY left (tau, period):", [lt[k] for k in range(KL)])
    print("DIAGONALS_DONE")


if __name__ == '__main__':
    main()
