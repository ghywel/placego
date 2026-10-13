#!/usr/bin/env python3
"""rule30_birth_deficit_census.py: Local's registered closure attempt for GPT's GC1184 profiles at a fixed birth deficit,
generalising rule30_second_oldest_census.py (L671) to an arbitrary root-dependent gap, with the gap enumerated
explicitly rather than taken from GC1184's symbolic fingerprints.

The setting (GC1184): a child of phase p with a white band [d, d + L - 1] at birth age a, deficit
j = floor((d - p)/2) + 1 - a >= 1, N = a + p, s = d - a + 1, gap length g = s - N = 2j - 1 + ((d + p) mod 2). The
canonical parent has wall phase r = N mod 2, the checkerboard through N, the gap at N + 1 .. s - 1, and either a Q core
(at least L + 2a - 1 black cells from s) or a P birth (black at s - 1, white at s, at least L + 2a - 2 blacks from
s + 1). For j >= 1, a leading 0 in the child's root promotes the band two ticks on into deficit j - 1 with L - 4, so
under the inductive hypothesis that deficit j - 1 is excluded for L - 4 >= L_min(j - 1), the first gap cell is r
(the first-free-cell rule, L671 S1(a)); here L_min(j) = 4j + 1 and d >= 6. Parametrise by (r, g, gap bits, type, p)
and N in the parity class r: then d = 2N + g - p - 1, and the child row is the crop at X = N - 3, T = N - p - 1 of
one ordinary seed per profile, fixed as N grows by 2 (GC1184), through J_Q = K + g + p - 1 or J_P = K + g + p.

RUN-ON:     cpu, standard library plus the certified cut lists in the RLK scratch; seconds to minutes.
COMMAND:    python3 tests/probes/lexicon/rule30_birth_deficit_census.py [J=2] [WMAX=48]

Record searched (record_find, 2026-10-13 17:21 BST): 'third.oldest|third-oldest' -> 5 hits in 2 files (GC1184 and its
probe); 'deficit' -> 325 hits in 58 files (the generic word); 'birth.gap|gap crop' -> 3 hits in 2 files (GC1184 and
its map line). GC1184, GC1183, GC1181 and L671's census read.

PREDICTIONS (written 2026-10-13 17:23 BST, before any run).
  D1 must hold (GC1184's representation, by direct simulation of the parent rows, every gap, not only the leading-1
     ones): for j = 1, 2, 3, both g, both r, every gap assignment and type, N up to 21 in the parity class with
     d >= 6, both p, cores K = 4 .. 12 and 3 random tails: the child row equals the crop of the seed built from the
     one-step image U (V_0 = 1, V_1 = r, V_2 = 1 - r, V_(k+3) = U_(N+k), k < g) through J, and is white at depths
     d .. J; at depth J + 1 it depends on the tail for some case (the index is sharp).
  D2 must hold (the control): at j = 1 with the leading-1 restriction, every profile closes in both phases, as L671
     and GC1181 found (g = 2 the two odd profiles; g = 1 only Q with N odd survives the restriction and must die, as
     it folds into the oldest corner).
  D3 blind (0.4): at j = 2 (third-oldest, L >= 9) all 18 profiles close in both phases within a window W <= 48, each
     class verdict used only where the minimal core (L = 9) fixes the window, smaller N on their own windows.
     REFUTED-BY: a surviving class or N; it is retained and reported with its child word, and the run does not widen.

OUTCOME (2026-10-13 17:24 BST, M5, 13 s; machine output quoted): D1 HELD, D2 HELD, D3 HELD.
  D1: the representation HELD for every gap (j <= 3, both g, both r, all types, N <= 21, K = 4 .. 12, 3 tails), with
     the index sharp somewhere.
  D2: j = 1 ALL CLOSED (8 profile-phase cases): g = 2, r = 0, Q at windows 4/5 and g = 2, r = 1, P at 15/16 (L671's
     two profiles, the same windows), and the two GC1181 hand cases (g = 1, r = 1, Q at 9/10; g = 2, r = 1, Q at 9/10).
  D3: j = 2 ALL CLOSED (36 profile-phase cases, the 18 profiles in both phases); closing windows 4 .. 22, parity-class periods (steps of2 in N) 4 ..
     2048; the longest are g = 4, r = 0, P (gaps 001 and 011) at 21/22.
  Diagnostic after the run (a scratch script, direct simulation of the parent rows with no crop, N <= 120, L = 9 and
     12, 2 random tails, windows min(J, the closing window)): 4,278 cases, none open; the clock excludes 3,112, no11
     1,138 and other certified cuts 28.

ADDENDUM PREDICTIONS (2026-10-13 17:35 BST, before the run): j = 3 as GPT registered it in GC1186, nothing wider.
  Fixed: window cap W <= 48, prefix-period horizon 2^16, L = 13 (the leading-1 threshold at j = 3: a leading 0 gives a
  third-oldest band of length L - 4 >= 9), both phases, d >= 6; neither cutoff is raised. Two speed changes, semantics
  unchanged: the period for W + 2 coordinates is searched among multiples of the period for W + 1, and cuts are
  matched by length-keyed sets.
  E1 must hold (the control): the j = 2 rerun closes all 36 cases with maximum window 22, as in D3.
  E2 must hold (the enumeration): j = 3 has 72 profiles (g = 5: 8 Q + 4 P per r; g = 6: 16 Q + 8 P per r).
  E3 blind (0.4, GPT's GC1186 prediction): every j = 3 case closes within W <= 28. REFUTED-BY: a case closing at
     29 .. 48 (then E3 fails but the case is closed) or a survivor at W = 48 (kept OPEN); a missing prefix period at
     the horizon is UNKNOWN, a computational limit, not a counterexample.
  E4 (the unexpected check, reported, no prediction): the last nonzero right-edge index of each seed, against the
     nominal g + 2.
ADDENDUM OUTCOME (2026-10-13 17:36 BST, M5, under a minute; machine output quoted): E1 HELD, E2 HELD, E3 REFUTED by one
  case, every case CLOSED; E4 below.
  E1: j = 2 ALL CLOSED, 36 cases, maximum window 22 (the speed changes reproduce D3).
  E2: j = 3 has 72 profiles; census j=3 (L >= 13): ALL CLOSED, 144 profile-phase cases, no OPEN, no UNKNOWN.
  E3: windows 4 .. 29; one case needs 29: g = 6, r = 0, gap 00101, P, p = 0 (16384 parity steps; its p = 1 twin closes
     at 27). The next longest: g = 6, r = 1, gap 11011, P at 25/26.
  E4: per phase, the last nonzero index over the 72 profiles is 1 (1 profile per g), 4 (2), 5 (3), 6 (6), 7 (12) and,
     for g = 6 only, 8 (24): half the profiles at each g have full span. Diagnostic after the run (a scratch script):
     every trailing-zero seed is a seed of a shorter gap, either a lower deficit's or, for g = 6, the full-span seed of
     g = 5 at the same deficit (j = 2: 6 of 6 and 3 of 3; j = 3: 24 of 24 and 12 of 12). The last-nonzero-1 seeds are
     seed 11 (the all-black Q gaps, r = 1), closing at 9/10 with period 32, GC1176's own numbers.
"""
import itertools, os, random, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from rule30_extremal_p_corner_read import step, depth1_column       # Local's own helpers (L668)
from rule30_second_oldest_census import Edge, Seed, verdict          # Local's own (L671)


def parent_row(N, gap, typ, K, tail):
    core = [1] * K if typ == 'Q' else [0] + [1] * K
    return [None] + [j % 2 for j in range(1, N + 1)] + list(gap) + core + list(tail)


def profiles(g, r, lead1):
    """Gap assignments (cells N+1 .. N+g-1) and types. P needs depth s-1 black (the last gap cell, or the prefix cell N,
    of value r, when g = 1). With lead1 the first free cell, depth N+1, must equal r: a gap cell, or for g = 1 the cell
    s itself (black for Q, white for P)."""
    out = []
    for bits in itertools.product((0, 1), repeat=g - 1):
        for typ in 'QP':
            prev = bits[-1] if bits else r
            if typ == 'P' and prev != 1:
                continue
            if lead1:
                first = bits[0] if bits else (1 if typ == 'Q' else 0)
                if first != r:
                    continue
            out.append((bits, typ))
    return out


def seed_bits(N, gap, typ):
    """V_0 .. V_(g+2) at time 0 from the one-step image U of the infinite-tail prototype."""
    g = len(gap) + 1
    U = step(parent_row(N, gap, typ, g + 6, []), N % 2)
    r = N % 2
    return [1, r, 1 - r] + [U[N + k] for k in range(g)]


def sites_of(bits):
    return tuple(-i for i, b in enumerate(bits) if b)


def kmin(typ, N, p, L):
    a = N - p
    return L + 2 * a - (1 if typ == 'Q' else 2)


def jlen(typ, K, g, p):
    return K + g + p - (1 if typ == 'Q' else 0)


def child_row(N, gap, typ, p, K, tail):
    row = parent_row(N, gap, typ, K, tail)
    for t in range(N - p):
        row = step(row, (t + N) % 2)
    return row


def d1(jmax=3, nmax=21):
    rng = random.Random(1184)
    ok, sharp = True, False
    for j in range(1, jmax + 1):
        for g in (2 * j - 1, 2 * j):
            for r in (0, 1):
                for bits, typ in profiles(g, r, False):
                    sb = seed_bits(r + 2, bits, typ)                       # the seed is the same for every N in the class
                    S = Seed(sites_of(sb), 2 * nmax + 4)
                    for N in range(r if r else 2, nmax + 1, 2):
                        for p in (0, 1):
                            if N - p < 1 or 2 * N + g - p - 1 < 6:
                                continue
                            ok &= seed_bits(N, bits, typ) == sb
                            d, T, X = 2 * N + g - p - 1, N - p - 1, N - 3
                            for K in range(4, 13):
                                J = jlen(typ, K, g, p)
                                kids = [child_row(N, bits, typ, p, K, [rng.randrange(2) for _ in range(6)])
                                        for _ in range(3)]
                                for kid in kids:
                                    ok &= all(kid[i] == S.site(X - i, T) for i in range(1, J + 1))
                                    ok &= all(kid[i] == 0 for i in range(d, J + 1))
                                if len({kid[J + 1] for kid in kids}) > 1:
                                    sharp = True
    print('D1 representation (j <= %d, every gap, N <= %d, K = 4..12):' % (jmax, nmax), 'HELD' if ok else 'FAILED',
          '| index sharp somewhere:', sharp)
    return ok and sharp


def make_index(forb):
    idx = {}
    for f in forb:
        idx.setdefault(len(f), set()).add(f)
    return sorted(idx.items())


def verdict_fast(row1, p, W, index):
    """verdict() with cuts matched by length-keyed sets: the same first violation, the same word."""
    x = depth1_column([None] + row1[:W] + [0], p, W - 1)
    word = ''
    for t in range(W):
        if (t + p) % 2 == 0:
            word += str(1 ^ x[t])
            for n, ws in index:
                if n <= len(word) and word[-n:] in ws:
                    return 'cut ' + word[-n:], word
        elif x[t] != 1:
            return 'black failure at child tick %d' % t, word
    return 'OPEN', word


def period_from(S, k, base):
    """Least period of (V_1 .. V_k), searched among multiples of the period of a shorter prefix."""
    sh, m = S.k - k, (1 << k) - 1
    s0 = (S.e[0] >> sh) & m
    t = base
    while t < len(S.e):
        if (S.e[t] >> sh) & m == s0:
            return t
        t += base
    return None


def census(j, wmax, lists):
    Lmin = 4 * j + 1
    held, report = True, []
    index = {p: make_index(lists[p]) for p in (0, 1)}
    for g in (2 * j - 1, 2 * j):
        for r in (0, 1):
            for bits, typ in profiles(g, r, True):
                sb = seed_bits(r + 2, bits, typ)
                S = Edge(sites_of(sb), 1 << 16, wmax + 2)
                last = max(i for i, b in enumerate(sb) if b)
                for p in (0, 1):
                    Ns = [N for N in range(r if r else 2, 400, 2) if N - p >= 1 and 2 * N + g - p - 1 >= 6]
                    closed, base, unknown = None, 1, False
                    for W in range(3, wmax + 1):
                        Pt = period_from(S, W + 2, base)
                        if Pt is None:
                            unknown = True
                            break
                        base = Pt
                        Pq = Pt // 2 if Pt % 2 == 0 else Pt
                        big = [N for N in Ns if jlen(typ, kmin(typ, N, p, Lmin), g, p) >= W]
                        n0 = big[0]
                        surv = []
                        for N in range(n0, n0 + 2 * Pq, 2):
                            T = N - p - 1
                            row1 = [S.V(i + 2 - p, T % Pt) for i in range(1, W + 1)]
                            v, w = verdict_fast(row1, p, W, index[p])
                            if v == 'OPEN':
                                surv.append((N, w))
                        small = []
                        for N in [N for N in Ns if N < n0]:
                            K = kmin(typ, N, p, Lmin)
                            kid = child_row(N, bits, typ, p, K, [0] * 8)
                            v, w = verdict_fast(kid[1:], p, jlen(typ, K, g, p), index[p])
                            if v == 'OPEN':
                                small.append((N, w))
                        if not surv and not small:
                            closed = (W, Pq, n0)
                            break
                    tag = 'g=%d r=%d gap=%s %s p=%d last-nonzero %d/%d' % (g, r, ''.join(map(str, bits)) or '-', typ,
                                                                           p, last, g + 2)
                    if closed:
                        report.append('%s: CLOSED at W=%d (N-parity-step period %d, classes from N=%d)' % (tag, *closed))
                    elif unknown:
                        held = False
                        report.append('%s: UNKNOWN at W=%d (prefix period beyond the 2^16 horizon)' % (tag, W))
                    else:
                        held = False
                        report.append('%s: OPEN at W=%d; classes %s; small N %s' % (tag, W, surv[:4], small[:4]))
    return held, report


def main():
    j = int(sys.argv[1]) if len(sys.argv) > 1 else 2
    wmax = int(sys.argv[2]) if len(sys.argv) > 2 else 48
    import rule30_relaxed_records_k as rlk
    lists = {0: rlk.load_forbidden('44all') + rlk.load_cuts(0, 40),
             1: rlk.load_forbidden('44allp1') + rlk.load_cuts(1, 40)}
    if j <= 2:
        d1()
    for jj in (sorted({1, j}) if j <= 2 else [j - 1, j]):
        held, report = census(jj, wmax, lists)
        print('\n'.join(report))
        print('census j=%d (L >= %d): %s, %d profile-phase cases' % (jj, 4 * jj + 1, 'ALL CLOSED' if held else 'SURVIVORS',
                                                                   len(report)))


if __name__ == '__main__':
    main()
