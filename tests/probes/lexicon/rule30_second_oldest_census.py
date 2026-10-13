#!/usr/bin/env python3
"""rule30_second_oldest_census.py: Local's census of the two odd-class profiles that GPT's GC1181 leaves at the second-oldest
birth age, with the profile controls GPT asked for registered first (CHAT-LEDGER GC1181, L670's offer).

The setting (GC1181): a child of phase p with a white band [d, d + L - 1], L >= 5, d >= 6, whose canonical ancestry
reaches the age a = m = floor((d - p)/2), one below the oldest (excluded by 8.97). Write e = d + p and N = a + p =
floor(e/2); the birth parent is C_(N mod 2)(0^q w) with q = floor(N/2), checkerboard at depths 1 .. N; zero-prefix
promotion forces the child's first sample w0 = 1. The even classes of e are GPT's; the odd classes leave two profiles:
  Q profile, e = 4q + 1, N = 2q, white parent wall: checkerboard through N, white N + 1, Q core from N + 2, of at least
     L + 2a - 1 = L + 4q - 2p - 1 cells;
  P profile, e = 4q + 3, N = 2q + 1, black parent wall: checkerboard through N, black N + 1, white N + 2, P core from
     N + 3, of at least L + 2a - 2 = L + 4q - 2p cells.
The child sits at parent tick a = N - p; its first sample is at parent tick N, its black tests at N + 1, N + 3, ...;
the synthetic zeros are not filtered. GC1181's normal forms: the child row is the left crop at X = N - 3 of the ordinary
seed with black sites {0, -2, -3, -4} (Q) or {0, -1, -4} (P), at T = N - p - 1 ticks, through J = K + p + 1 (Q) or
K + p + 2 (P) for a core of K cells.

Why the classes are finite: a finite seed whose rightmost black cell is at site 0 has V_0(t) = x_t(t) = 1 for every t,
and V_j(t + 1) = V_j(t) XOR (V_(j-1)(t) OR V_(j-2)(t)) (G249/GC755) is a bijection on the prefix (V_1 .. V_k), so the
prefix is purely periodic in t from t = 0. The child row's depths 1 .. W are V_(3-p) .. V_(W+2-p) at T, so the class of
q is T(q) modulo that period, and a window of W child ticks is decided class by class for every q whose core fixes it.

RUN-ON:     cpu, standard library plus the certified cut lists in the RLK scratch; seconds to minutes.
COMMAND:    python3 tests/probes/lexicon/rule30_second_oldest_census.py [WMAX=40]

Record searched (record_find, 2026-10-13 16:57 BST): 'second.oldest|second-oldest' -> 5 hits in 1 file (GC1181 only);
'promot' -> 331 hits in 53 files (the generic word, other objects); 'fingerprint' -> 17 hits in 11 files (other
objects); '10111|11001' -> 761 hits in 184 files (generic bit strings); 'free.prefix|free prefix' -> 2 hits (GC1181 and
an Intel probe). GC1181, GC1177, GC1170 and 8.97 read.

PREDICTIONS (written 2026-10-13 16:59 BST, before any run).
  S1 must hold (GC1181's hand facts): (a) depth N + 1 of C_(N mod 2)(0^floor(N/2) w) is 1 - w0 for even N and w0 for odd
     N (N = 1 .. 12, all w of length 6); (b) the one-step images: the Q row gives checkerboard through N - 1, black N and
     N + 1, then white; the P row gives checkerboard through N - 1, white N, black N + 1, then white; (c) the time shift
     behind promotion: C_p(0u) advanced two ticks is C_p(u) on every shared determined depth (both p, all u of length 6).
  S2 must hold (the normal forms, by direct simulation of the parent row, not the crop): for q = 1 .. 48, both p, cores
     K = 6 .. 16 and 4 random tails, the child row equals the stated seed crop through J and is white at depths d .. J;
     depth 1 is black at parent ticks 0 .. N - 1 and the child's first sample is 1.
  S3 blind (0.5), the census: in both profiles and both phases, with the child phase's certified cut list (mfw44all and
     cuts40 for p = 0; mfw44allp1 and cuts40 for p = 1) and the clock, every class of q is excluded within a window that
     the minimal core (L = 5) fixes, and every small q below that window is excluded on its own window. REFUTED-BY: a
     surviving class or small q; it is then reported with its child word and retained as OPEN.

OUTCOME: (filled in after the run, below this line)
"""
import os, random, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from rule30_extremal_p_corner_read import step, depth1_column, forced_row      # Local's own helpers (L668)

SEEDS = {'Q': (0, -2, -3, -4), 'P': (0, -1, -4)}


def profile(kind, q):
    """(N, parent wall phase, junction cells after the checkerboard, core start)."""
    if kind == 'Q':
        N = 2 * q
        return N, 0, [0], N + 2
    N = 2 * q + 1
    return N, 1, [1, 0], N + 3


def parent_row(kind, q, K, tail):
    N, ph, junction, start = profile(kind, q)
    return [None] + [j % 2 for j in range(1, N + 1)] + junction + [1] * K + list(tail)


def kmin(kind, q, p, L=5):
    return L + 4 * q - 2 * p - (1 if kind == 'Q' else 0)


def jlen(kind, K, p):
    return K + p + (1 if kind == 'Q' else 2)


def child_row(kind, q, p, K, tail):
    N, ph, _, _ = profile(kind, q)
    row = parent_row(kind, q, K, tail)
    for t in range(N - p):
        row = step(row, (t + ph) % 2)
    return row


def verdict(row1, p, W, forb):
    """Child row depths 1 .. W -> (verdict, word) over child ticks 0 .. W - 1, child wall (t + p) mod 2."""
    x = depth1_column([None] + row1[:W] + [0], p, W - 1)
    word = ''
    for t in range(W):
        if (t + p) % 2 == 0:
            word += str(1 ^ x[t])
            bad = [f for f in forb if word.endswith(f)]
            if bad:
                return 'cut ' + bad[0], word
        elif x[t] != 1:
            return 'black failure at child tick %d' % t, word
    return 'OPEN', word


class Seed:
    def __init__(self, sites, T):
        self.O = T + 8
        x = 0
        for s in sites:
            x |= 1 << (self.O + s)
        self.rows = []
        for t in range(T + 1):
            self.rows.append(x)
            x = (x << 1) ^ (x | (x >> 1))

    def V(self, j, t):
        return (self.rows[t] >> (self.O + t - j)) & 1

    def site(self, s, t):
        return (self.rows[t] >> (self.O + s)) & 1


class Edge:
    """The right-edge window only: e_t holds V_0 .. V_kmax at time t, V_j as bit kmax - j (no full rows kept)."""
    def __init__(self, sites, horizon, kmax):
        O, x, self.k, self.e = horizon + 8, 0, kmax, []
        for s in sites:
            x |= 1 << (O + s)
        mask = (1 << (kmax + 1)) - 1
        for t in range(horizon + 1):
            self.e.append((x >> (O + t - kmax)) & mask)
            x = (x << 1) ^ (x | (x >> 1))

    def V(self, j, t):
        return (self.e[t] >> (self.k - j)) & 1

    def period(self, k):
        """Exact least period in t of (V_1 .. V_k): the first return to the t = 0 state (the map is a bijection)."""
        sh, m = self.k - k, (1 << k) - 1
        s0 = (self.e[0] >> sh) & m
        return next((t for t in range(1, len(self.e)) if (self.e[t] >> sh) & m == s0), None)


def s1():
    ok_a = True
    for N in range(1, 13):
        for m in range(64):
            w = [(m >> i) & 1 for i in range(6)]
            row = forced_row([0] * (N // 2) + w, N % 2)
            ok_a &= row[1:N + 1] == [j % 2 for j in range(1, N + 1)]
            ok_a &= row[N + 1] == ((1 - w[0]) if N % 2 == 0 else w[0])
    ok_b = True
    for q in range(1, 20):
        for kind in 'QP':
            N, ph, _, _ = profile(kind, q)
            img = step(parent_row(kind, q, 6, [1] * 4), ph)
            want = [j % 2 for j in range(1, N)] + ([1, 1] if kind == 'Q' else [0, 1]) + [0] * 4
            ok_b &= img[1:N + 6] == want[:N + 5]
    ok_c = True
    for p in (0, 1):
        for m in range(64):
            u = [(m >> i) & 1 for i in range(6)]
            A = forced_row([0] + u, p)
            for t in range(2):
                A = step(A, (t + p) % 2)
            B = forced_row(u, p)
            n = min(len(A), len(B))
            ok_c &= n > 4 and A[1:n] == B[1:n]
    print('S1 (a) first free cell: %s; (b) one-step images: %s; (c) two-tick shift: %s'
          % tuple('HELD' if v else 'FAILED' for v in (ok_a, ok_b, ok_c)))
    return ok_a and ok_b and ok_c


def s2():
    rng = random.Random(1181)
    ok = True
    seeds = {k: Seed(SEEDS[k], 2 * 48 + 4) for k in 'QP'}
    for kind in 'QP':
        for q in range(1, 49):
            N, ph, _, _ = profile(kind, q)
            for p in (0, 1):
                d = 2 * N + 1 - p
                T, X = N - p - 1, N - 3
                for K in range(6, 17):
                    J = jlen(kind, K, p)
                    for _ in range(4):
                        tail = [rng.randrange(2) for _ in range(8)]
                        kid = child_row(kind, q, p, K, tail)
                        ok &= all(kid[j] == seeds[kind].site(X - j, T) for j in range(1, J + 1))
                        ok &= all(kid[j] == 0 for j in range(d, J + 1))
                    x = depth1_column(parent_row(kind, q, K, [0] * 8), ph, N)
                    ok &= all(x[t] == 1 for t in range(N)) and x[N] == 0
    print('S2 normal forms by direct simulation (q <= 48, both p, K = 6..16):', 'HELD' if ok else 'FAILED')
    return ok


def s3(wmax=40):
    import rule30_relaxed_records_k as rlk
    lists = {0: rlk.load_forbidden('44all') + rlk.load_cuts(0, 40),
             1: rlk.load_forbidden('44allp1') + rlk.load_cuts(1, 40)}
    held = True
    for kind in 'QP':
        S = Edge(SEEDS[kind], 1 << 16, wmax + 2)
        for p in (0, 1):
            q0 = 2 if kind == 'Q' else 1                                  # d >= 6
            closed = None
            for W in range(4, wmax + 1):
                Pt = S.period(W + 2)
                if Pt is None:
                    print('S3 %s p=%d W=%d: prefix period beyond 2^16, stop' % (kind, p, W)); break
                Pq = Pt // 2 if Pt % 2 == 0 else Pt
                qa = q0
                while jlen(kind, kmin(kind, qa, p), p) < W:                 # first q whose minimal core fixes W
                    qa += 1
                surv = []
                for q in range(qa, qa + Pq):
                    T = (2 * q + (0 if kind == 'Q' else 1)) - p - 1
                    row1 = [S.V(j + 2 - p, T % Pt) for j in range(1, W + 1)]
                    v, w = verdict(row1, p, W, lists[p])
                    if v == 'OPEN':
                        surv.append((q, w))
                small = []
                for q in range(q0, qa):
                    K = kmin(kind, q, p)
                    Wq = jlen(kind, K, p)
                    kid = child_row(kind, q, p, K, [0] * 8)
                    v, w = verdict(kid[1:], p, Wq, lists[p])
                    if v == 'OPEN':
                        small.append((q, w))
                if not surv and not small:
                    closed = (W, Pq, qa)
                    break
            if closed:
                print('S3 %s profile p=%d: CLOSED at window W=%d (q-period %d; classes from q=%d; small q %d..%d each'
                      ' on its own window)' % (kind, p, closed[0], closed[1], closed[2], q0, closed[2] - 1))
            else:
                held = False
                print('S3 %s profile p=%d: OPEN at W=%d; surviving classes %s; small q %s'
                      % (kind, p, W, surv[:6], small[:6]))
    print('S3', 'HELD' if held else 'REFUTED')
    return held


if __name__ == '__main__':
    wmax = int(sys.argv[1]) if len(sys.argv) > 1 else 40
    s1()
    s2()
    s3(wmax)
