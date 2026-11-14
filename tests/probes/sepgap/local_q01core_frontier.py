#!/usr/bin/env python3
"""L1673 (Local, 14 November 2026): branch counts and the black frontier of a Q01GapCore survivor.

Zero-boundary left half (kit Rule30ZeroBoundary): z(t+1, d) = z(t, d+1) xor (z(t, d) or z(t, d-1)), z(t, 0) = 0.
Constrained rows: depth 1 black at even ticks; free bits f(s) = z(2s+1, 1); Theta f = the row; g = not f.
Languages on g, anchored at a pulse g(0) = 1:  TwoWordsOK = gaps 3 or 5, no 33, no 3553;
TwoCoreOK = also no 3535353 (Q01TwoCore <-> Q01GapCore, kit main 268488d6).  k free bits fix depths 1..2k+1.

Method: depth n+1 of Theta f from c(n) (depth 1 at tick n): with the anti-diagonals D_n (bit tau = z(tau, n-tau)),
X = (D_n | D_(n-1)) restricted to n bits, row[n+1] = c(n) xor parity(X), D_(n+1) = prefix-xor(row[n+1] | X << 1).
Every admissible word is enumerated depth first.  Predictions and the counting heuristic are in L1673, pushed before
this file existed.  Exact integers throughout.
"""
import math
import random
import sys
import time

T0 = time.time()
FAILS = []


def say(*a):
    print(*a)
    sys.stdout.flush()


def check(name, ok, text):
    say('%s %s: %s' % (name, 'PASS' if ok else 'FAIL', text))
    if not ok:
        FAILS.append(name)


MASK = [(1 << n) - 1 for n in range(2000)]


def pxor(p, m):
    sh = 1
    while sh < m:
        p ^= p << sh
        sh <<= 1
    return p & MASK[m]


def step_depth(Dn, Dn1, n, c):
    """Return (row bit at depth n+1, D_(n+1)) given D_n, D_(n-1) and c = depth-1 value at tick n."""
    X = (Dn | Dn1) & MASK[n]
    r = c ^ (X.bit_count() & 1)
    return r, pxor(r | (X << 1), n + 1)


def theta_prefix(f):
    """Depths 1..2k+1 of Theta f for a list f of k free bits, as an int (bit d-1 = depth d)."""
    Dn, Dn1, n, R = 0, 0, 0, 0
    for s in range(len(f)):
        for c in (1, f[s]):
            r, D = step_depth(Dn, Dn1, n, c)
            R |= r << n
            Dn1, Dn, n = Dn, D, n + 1
    r, _ = step_depth(Dn, Dn1, n, 1)
    return R | (r << n)


def F(y):
    return (y >> 1) ^ (y | (y << 1))


def forward_ok(R, f):
    """The finite row R (zeros beyond its prefix) reproduces depth 1 = alt f at ticks 0..2k."""
    y = R
    k = len(f)
    for t in range(2 * k + 1):
        want = 1 if t % 2 == 0 else f[t // 2]
        if (y & 1) != want:
            return False
        y = F(y)
    return True


FORBID = {'words': ('33', '3553'), 'core': ('33', '3553', '3535353')}


def admissible_words(k, lang):
    """All admissible free-bit words of length k (lists), anchored f(0) = 0, by gap choices."""
    out = []

    def rec(s, d, gs, f):
        if s == k:
            out.append(f[:])
            return
        if s == 0:
            opts = [(1, 1, gs)]
        elif d in (1, 2, 4):
            opts = [(0, d + 1, gs)]
        elif d == 3:
            opts = []
            g3 = gs + '3'
            if not any(g3.endswith(x) for x in FORBID[lang]):
                opts.append((1, 1, g3[-7:]))
            opts.append((0, 4, (gs + '5')[-7:]))
        else:   # d == 5: the committed gap 5 ends here
            opts = [(1, 1, gs)]
        for g, d2, gs2 in opts:
            f.append(1 - g)
            rec(s + 1, d2, gs2, f)
            f.pop()
    rec(0, 0, '', [])
    return out


def enumerate_frontier(K, lang, nodemax, Wgrid):
    """Depth-first over admissible words up to length K. Per k: B, min last black, tail histogram,
    white first checks, N(W, k) for W in Wgrid, and a champion word per support bound."""
    stats = {k: {'B': 0, 'minL': 10 ** 9, 'tails': {}, 'white': 0, 'Lh': {}, 'argmin': None}
             for k in range(1, K + 1)}
    nodes = 0
    # stack: (s, d, gs, Dn, Dn1, n, R, fbits as int, )
    stack = [(0, 0, '', 0, 0, 0, 0, 0)]
    aborted = False
    while stack:
        s, d, gs, Dn, Dn1, n, R, fb = stack.pop()
        if s == 0:
            opts = [(1, 1, gs)]
        elif d in (1, 2, 4):
            opts = [(0, d + 1, gs)]
        elif d == 3:
            opts = []
            g3 = gs + '3'
            if lang == 'all' or not any(g3.endswith(x) for x in FORBID[lang]):
                opts.append((1, 1, g3[-7:]))
            opts.append((0, 4, (gs + '5')[-7:]))
        else:
            opts = [(1, 1, gs)]
        if lang == 'all':
            opts = [(0, 0, ''), (1, 0, '')]
        for g, d2, gs2 in opts:
            nodes += 1
            if nodes > nodemax:
                aborted = True
                break
            fbit = 1 - g if lang != 'all' else g
            r1, D1 = step_depth(Dn, Dn1, n, 1)
            r2, D2 = step_depth(D1, Dn, n + 1, fbit)
            R2 = R | (r1 << n) | (r2 << (n + 1))
            k = s + 1
            chk, _ = step_depth(D2, D1, n + 2, 1)
            P = R2 | (chk << (n + 2))
            L = P.bit_length()
            st = stats[k]
            st['B'] += 1
            if L < st['minL']:
                st['minL'] = L
                st['argmin'] = (fb | (fbit << s), k)
            T = 2 * k + 1 - L
            st['tails'][T] = st['tails'].get(T, 0) + 1
            st['white'] += (chk == 0)
            st['Lh'][L] = st['Lh'].get(L, 0) + 1
            if k < K:
                stack.append((k, d2, gs2, D2, D1, n + 2, R2, fb | (fbit << s)))
        if aborted:
            break
    for k in stats:
        stats[k]['N'] = {W: sum(v for L_, v in stats[k]['Lh'].items() if L_ <= W) for W in Wgrid}
    return stats, nodes, aborted


def main():
    say('L1673 frontier probe.')
    # ---------------- controls
    rnd = random.Random(1673)
    ok = True
    for lang in ('words', 'core'):
        for k in (10, 20, 30):
            W = admissible_words(k, lang)
            for f in rnd.sample(W, min(40, len(W))):
                if not forward_ok(theta_prefix(f), f):
                    ok = False
    for _ in range(200):
        k = rnd.randint(1, 30)
        f = [rnd.randint(0, 1) for _ in range(k)]
        if not forward_ok(theta_prefix(f), f):
            ok = False
    check('C1', ok, 'forward evolution of every sampled prefix reproduces depth 1 = alt f at ticks 0..2k')
    ok = True
    for k in range(8, 26):
        for f in admissible_words(k, 'words'):
            P = theta_prefix(f)
            bit = lambda d: (P >> (d - 1)) & 1
            pat = [1, 1, 0, 0, 0, 1, 1, 1 - f[3], 1, 0, 1, 1, 1, 1, 1, f[3]]
            if [bit(d) for d in range(1, 17)] != pat:
                ok = False
    check('C2', ok, 'Quint\'s 16-depth skeleton (L1..16 = 1100011,!f3,1011111,f3; weight 11) for every TwoWordsOK word, 8 <= k <= 25')
    W16 = admissible_words(16, 'words')
    W24 = admissible_words(24, 'words')
    b = lambda P, d: (P >> (d - 1)) & 1
    ok16 = len(W16) == 5 and all(b(theta_prefix(f), 20) == 0 and b(theta_prefix(f), 21) == 0
                                 and (b(theta_prefix(f), 29) or b(theta_prefix(f), 32))
                                 and sum(b(theta_prefix(f), d) for d in range(1, 33)) >= 18 for f in W16)
    ok24 = len(W24) == 11 and all(b(theta_prefix(f), 46) or b(theta_prefix(f), 47) or b(theta_prefix(f), 48) for f in W24)
    check('C3', ok16 and ok24, 'TwoWordsOK: B(16) = %d (Quint 5), depths 20, 21 white, 29 or 32 black, weight(1..32) >= 18; '
          'B(24) = %d (Quint 11), one of 46, 47, 48 black' % (len(W16), len(W24)))
    # Q01 without language against the sepgap record
    dmax = {}
    for w in range(1, 17):
        best = 0
        for y in range((1 << (w - 1)) | 1, 1 << w, 2):
            t, yy = 0, y
            while yy & 1:
                yy = F(F(yy))
                t += 2
            best = max(best, t)
        dmax[w] = best
    rec = {}
    try:
        for line in open(__file__.rsplit('/', 1)[0] + '/death_pairs.out'):
            if line.startswith('w '):
                w = int(line.split(':')[0][2:])
                D = int(line.split('D max ')[1].split(' ')[0])
                rec[w] = D
    except OSError:
        pass
    agree = all(rec.get(w, dmax[w]) == dmax[w] for w in range(8, 17))
    for w in range(17, 23):
        if w in rec:
            dmax[w] = rec[w]
    statsQ, _, _ = enumerate_frontier(19, 'all', 10 ** 7, [])
    okQ = True
    rows = []
    for k in range(1, 20):
        want = min(w for w in dmax if dmax[w] >= 2 * (k + 1)) if any(dmax[w] >= 2 * (k + 1) for w in dmax) else None
        got = statsQ[k]['minL']
        rows.append('%d:%d/%s' % (k, got, want))
        if want is not None and got != want:
            okQ = False
    say('   Q01, k: min support / record   ' + ' '.join(rows))
    check('C4', okQ and agree, 'Q01 with no language: min support m(k) equals the survival record (own walk to width 16 %s with sepgap; sepgap to 22)'
          % ('agrees' if agree else 'DISAGREES'))

    # ---------------- the two languages
    lam = 2 ** 0.12707
    say('--- frontier, lambda (entropy, L1610) = %.5f' % lam)
    Wgrid = list(range(20, 331, 10))
    for lang, K in (('words', 140), ('core', 160)):
        t1 = time.time()
        st, nodes, ab = enumerate_frontier(K, lang, 3 * 10 ** 7, Wgrid)
        kmax = max(k for k in st if st[k]['B'] > 0)
        if ab:
            kmax -= 1     # last level incomplete
        say('=== %s: %d nodes in %.0f s%s; complete to k = %d' % (lang, nodes, time.time() - t1, ' (node budget hit)' if ab else '', kmax))
        say('   k : B(k), B(k)/B(k-1), m(k), T(k), share with a black cell in the last 3 depths, share of white first checks')
        for k in list(range(8, 33, 4)) + list(range(40, kmax + 1, 10)) + ([kmax] if kmax % 10 else []):
            s_ = st[k]
            ratio = s_['B'] / st[k - 1]['B'] if st[k - 1]['B'] else float('nan')
            near = sum(v for T, v in s_['tails'].items() if T <= 2) / s_['B']
            say('   %3d : %8d  %.4f  %4d  %3d  %.4f  %.4f' % (k, s_['B'], ratio, s_['minL'], 2 * k + 1 - s_['minL'], near, s_['white'] / s_['B']))
        Tk = [(k, 2 * k + 1 - st[k]['minL']) for k in range(1, kmax + 1)]
        firstT = {}
        for k, T in Tk:
            for c in range(1, 30):
                if T >= c and c not in firstT:
                    firstT[c] = k
        say('   first k with T(k) >= c: ' + ', '.join('%d: %d' % (c, firstT[c]) for c in sorted(firstT)))
        say('   tail histogram at k = %d: %s' % (kmax, sorted(st[kmax]['tails'].items())))
        # survival records S(W) and decay of N(W, k)
        S = {}
        for W in Wgrid:
            ks = [k for k in range(1, kmax + 1) if st[k]['N'][W] > 0]
            S[W] = max(ks) if ks else 0
        say('   survival record S(W) (largest k with a row of support <= W surviving): ' +
            ', '.join('%d: %d%s' % (W, S[W], '+' if S[W] == kmax else '') for W in Wgrid if W <= 2 * kmax + 1))
        rat = []
        for W in Wgrid:
            seq = [st[k]['N'][W] for k in range(1, kmax + 1)]
            for k in range(W // 2 + 4, kmax):
                a_, b_ = st[k]['N'][W], st[k + 1]['N'][W]
                if a_ >= 200 and b_ > 0:
                    rat.append(b_ / a_)
        if rat:
            say('   per-step ratio N(W,k+1)/N(W,k) beyond k = W/2 + 4 (counts >= 200): mean %.4f, median %.4f, %d ratios; lambda/4 = %.4f'
                % (sum(rat) / len(rat), sorted(rat)[len(rat) // 2], len(rat), lam / 4))
        if lang == 'core':
            ratios = [st[k]['B'] / st[k - 1]['B'] for k in range(80, kmax + 1)]
            okP2 = all(abs(x - lam) <= 0.002 for x in ratios) if ratios else False
            # the growth ratio oscillates with the gap structure; compare the geometric mean over 30 steps too
            gm = (st[kmax]['B'] / st[kmax - 30]['B']) ** (1 / 30)
            say('P2 %s: B(k)/B(k-1) within 0.002 of %.4f for 80 <= k <= %d (range %.4f to %.4f); 30-step geometric mean %.5f'
                % ('HELD' if okP2 else 'REFUTED', lam, kmax, min(ratios), max(ratios), gm))
            Tmax = 2 * kmax + 1 - st[kmax]['minL']
            okP3 = any(T >= 6 for k, T in Tk if k <= 120) and 0.06 <= Tmax / kmax <= 0.2
            say('P3 %s: T(k) >= 6 by k = 120 (first at %s); T(kmax)/kmax = %d/%d = %.3f (predicted 0.06 to 0.2)'
                % ('HELD' if okP3 else 'REFUTED', firstT.get(6), Tmax, kmax, Tmax / kmax))
            wsh = [st[k]['white'] / st[k]['B'] for k in range(60, kmax + 1)]
            okP4 = all(abs(x - 0.5) <= 0.06 for x in wsh)
            say('P4 %s: white first-check share within 0.06 of 1/2 for 60 <= k <= %d (range %.4f to %.4f)'
                % ('HELD' if okP4 else 'REFUTED', kmax, min(wsh), max(wsh)))
            if rat:
                med = sorted(rat)[len(rat) // 2]
                say('P5 %s: median per-step decay %.4f within 0.05 of lambda/4 = %.4f'
                    % ('HELD' if abs(med - lam / 4) <= 0.05 else 'REFUTED', med, lam / 4))
            a = st[kmax]['argmin']
            if a:
                fb, kk = a
                fw = [(fb >> i) & 1 for i in range(kk)]
                P = theta_prefix(fw)
                say('   champion at k = %d: support %d, free bits %s, row %s' % (kk, P.bit_length(), ''.join(map(str, fw)),
                                                                         ''.join(str((P >> i) & 1) for i in range(P.bit_length()))))
                say('   champion forward check: %s' % forward_ok(P, fw))
    say('failures: %s' % (FAILS if FAILS else 'none'))
    say('done in %.0f s' % (time.time() - T0))


if __name__ == '__main__':
    main()
