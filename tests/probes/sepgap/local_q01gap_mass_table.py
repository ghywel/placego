#!/usr/bin/env python3
"""L1675 (Local, 16 November 2026): the exact mass table of the Q01Gap language.

Kit frame (Rule30ZeroCoastBridge, kit main 8b397bde): a seed y is a left row as an integer (bit i = depth i + 1),
F y = (y >> 1) ^ (y | (y << 1)).  SurvivesTo y H: the depth-1 trace at ticks 0..H-1 is white at tick 0, black at odd
ticks, and at even ticks follows the gap clock (ages 0..4; a reset, a white cell, is allowed at age 2 and forced at
age 4: gaps of 3 or 5 free steps).  NoMass M H: no y of popcount <= M survives to H.  SurvivesTo y H reads only bits
0..H-1 of y, so NoMass M H <=> M < mu(H), mu(H) = least popcount of an accepted H-bit prefix.

Method: the anti-diagonal recursion of L1673 (local_q01core_frontier.step_depth) builds the unique prefix of each
trace; phase 1 enumerates every accepted trace to K1 free steps; phase 2 is a depth-first search bounded by popcount.
Predictions K1..K5 are in L1675 (and its first addendum), pushed before this file was run.  Exact integers.
"""
import math
import random
import sys
import time

sys.path.insert(0, __file__.rsplit('/', 1)[0])
import local_q01core_frontier as FR   # noqa: E402   (step_depth, F)

step_depth = FR.step_depth
T0 = time.time()
FAILS = []

# The eight seeds of R30-20261115-fdf6a3 (c37Roots), public data of that submission; the last is its y*.
C37ROOTS = [42813888358306443700074217814, 148978366434744761789452353878, 2654468869608816557330812141910,
            20290708049760378067263390038, 871680261646910262683015020886, 3258683745119620012336052404566,
            793529923180978236193646670102, 343533199256979670105602359638]
YSTAR = 343533199256979670105602359638


def say(*a):
    print(*a)
    sys.stdout.flush()


def check(name, ok, text):
    say('%s %s: %s' % (name, 'PASS' if ok else 'FAIL', text))
    if not ok:
        FAILS.append(name)


def verdict(name, ok, text):
    say('%s %s: %s' % (name, 'HELD' if ok else 'REFUTED', text))


def kit_survive_len(y, limit):
    """The largest H <= limit with SurvivesTo y H: a literal simulation of the kit's acceptor."""
    age = 0
    for t in range(limit):
        b = y & 1
        if t == 0:
            if b:
                return 0
        elif t & 1:
            if not b:
                return t
        else:
            g = 1 - b
            if age == 2:
                age = 0 if g else 3
            elif age == 4:
                if not g:
                    return t
                age = 0
            else:
                if g:
                    return t
                age += 1
        y = FR.F(y)
    return limit


KIDS = {0: ((0, 1),), 1: ((0, 2),), 2: ((1, 0), (0, 3)), 3: ((0, 4),), 4: ((1, 0),)}


def root():
    r0, D1 = step_depth(0, 0, 0, 0)       # tick 0 is white
    assert r0 == 0
    return (0, 0, D1, 0, 1, 0, 0)         # (s, age, D_n, D_(n-1), n, R, popcount)


def prefixes_upto(K):
    """All accepted prefixes: dict H -> set of ints, for H = 2s+1 and 2s+2, s = 1..K."""
    out = {}
    stack = [root()]
    while stack:
        s, age, Dn, Dn1, n, R, pop = stack.pop()
        r1, D1 = step_depth(Dn, Dn1, n, 1)
        for g, age2 in KIDS[age]:
            r2, D2 = step_depth(D1, Dn, n + 1, 1 - g)
            R2 = R | (r1 << n) | (r2 << (n + 1))
            chk, _ = step_depth(D2, D1, n + 2, 1)
            out.setdefault(n + 2, set()).add(R2)
            out.setdefault(n + 3, set()).add(R2 | (chk << (n + 2)))
            if s + 1 < K:
                stack.append((s + 1, age2, D2, D1, n + 2, R2, 0))
    return out


def enumerate_all(K, joint_at):
    """Every accepted trace to K free steps.  Per s: B, popcount histogram at H = 2s+2, least popcounts at both
    parities, least support; joint (support, popcount) counts at the levels in joint_at."""
    B = [0] * (K + 1)
    pops = [[0] * (2 * K + 4) for _ in range(K + 1)]
    mu_odd = [10 ** 9] * (K + 1)
    mu_even = [10 ** 9] * (K + 1)
    minL = [10 ** 9] * (K + 1)
    joint = {s: {} for s in joint_at}
    stack = [root()]
    nodes = 0
    while stack:
        s, age, Dn, Dn1, n, R, pop = stack.pop()
        r1, D1 = step_depth(Dn, Dn1, n, 1)
        base = pop + r1
        s2 = s + 1
        for g, age2 in KIDS[age]:
            nodes += 1
            r2, D2 = step_depth(D1, Dn, n + 1, 1 - g)
            R2 = R | (r1 << n) | (r2 << (n + 1))
            p_odd = base + r2
            chk, _ = step_depth(D2, D1, n + 2, 1)
            p_even = p_odd + chk
            B[s2] += 1
            pops[s2][p_even] += 1
            if p_odd < mu_odd[s2]:
                mu_odd[s2] = p_odd
            if p_even < mu_even[s2]:
                mu_even[s2] = p_even
            L = (n + 3) if chk else R2.bit_length()
            if L < minL[s2]:
                minL[s2] = L
            if s2 in joint:
                j = joint[s2]
                j[(L, p_even)] = j.get((L, p_even), 0) + 1
            if s2 < K:
                stack.append((s2, age2, D2, D1, n + 2, R2, p_odd))
    return B, pops, mu_odd, mu_even, minL, joint, nodes


def mass_dfs(M, K, tstop, keep=64):
    """All accepted prefixes of popcount <= M.  Returns per s the counts and least popcounts at both parities,
    the minimisers at even H (up to `keep`), the node count and whether the time limit stopped it."""
    c_odd = [0] * (K + 2)
    c_even = [0] * (K + 2)
    m_odd = [10 ** 9] * (K + 2)
    m_even = [10 ** 9] * (K + 2)
    arg = [None] * (K + 2)
    stack = [root()]
    nodes = 0
    while stack:
        s, age, Dn, Dn1, n, R, pop = stack.pop()
        r1, D1 = step_depth(Dn, Dn1, n, 1)
        base = pop + r1
        s2 = s + 1
        for g, age2 in KIDS[age]:
            nodes += 1
            r2, D2 = step_depth(D1, Dn, n + 1, 1 - g)
            p_odd = base + r2
            if p_odd > M:
                continue
            c_odd[s2] += 1
            if p_odd < m_odd[s2]:
                m_odd[s2] = p_odd
            chk, _ = step_depth(D2, D1, n + 2, 1)
            p_even = p_odd + chk
            if p_even > M:
                continue
            c_even[s2] += 1
            R2 = R | (r1 << n) | (r2 << (n + 1))
            if p_even < m_even[s2]:
                m_even[s2] = p_even
                arg[s2] = [R2 | (chk << (n + 2))]
            elif p_even == m_even[s2] and len(arg[s2]) < keep:
                arg[s2].append(R2 | (chk << (n + 2)))
            if s2 < K:
                stack.append((s2, age2, D2, D1, n + 2, R2, p_odd))
        if (nodes & 0xFFFF) < 2 and time.time() > tstop:
            return None, nodes
    return (c_odd, c_even, m_odd, m_even, arg), nodes


def horizon(res, K):
    """The least H with no accepted prefix of popcount <= M (None if alive at the depth limit)."""
    c_odd, c_even = res[0], res[1]
    for s in range(1, K + 1):
        if c_odd[s] == 0:
            return 2 * s + 1
        if c_even[s] == 0:
            return 2 * s + 2
    return None


def linfit(xs, ys):
    n = len(xs)
    mx, my = sum(xs) / n, sum(ys) / n
    a = sum((x - mx) * (y - my) for x, y in zip(xs, ys)) / sum((x - mx) ** 2 for x in xs)
    return a, my - a * mx


def main():
    say('L1675 mass-table probe.')
    # ------------------------------------------------------------ controls
    rnd = random.Random(1675)
    ok = True
    for _ in range(300):
        m = rnd.randint(1, 40)
        c = [rnd.randint(0, 1) for _ in range(m)]
        Dn, Dn1, R = 0, 0, 0
        for n in range(m):
            r, D = step_depth(Dn, Dn1, n, c[n])
            R |= r << n
            Dn1, Dn = Dn, D
        y = R
        for t in range(m):
            if (y & 1) != c[t]:
                ok = False
            y = FR.F(y)
    check('C0', ok, 'the anti-diagonal recursion inverts arbitrary columns: 300 random columns of length <= 40')
    pre = prefixes_upto(8)
    ok = True
    for H in range(3, 19):
        brute = set(z for z in range(1 << H) if kit_survive_len(z, H) == H)
        if brute != pre[H]:
            ok = False
    check('C1', ok, 'accepted prefixes = {z < 2^H : SurvivesTo z H} by literal simulation of the kit acceptor, 3 <= H <= 18')
    K1 = 80
    t1 = time.time()
    B, pops, mu_odd, mu_even, minL, joint, nodes1 = enumerate_all(K1, (50, K1))
    say('   phase 1: %d nodes in %.0f s; B at H = 102, 162: %d, %d' % (nodes1, time.time() - t1, B[50], B[K1]))
    ok = True
    for trial in range(40):
        s, age, Dn, Dn1, n, R, pop = root()
        depth = rnd.randint(30, 100)
        while s < depth:
            r1, D1 = step_depth(Dn, Dn1, n, 1)
            g, age2 = rnd.choice(KIDS[age])
            r2, D2 = step_depth(D1, Dn, n + 1, 1 - g)
            R = R | (r1 << n) | (r2 << (n + 1))
            Dn, Dn1, n, s, age = D2, D1, n + 2, s + 1, age2
        if kit_survive_len(R, n) != n:
            ok = False
    check('C2', ok, 'every sampled prefix (30 to 100 free steps) survives to its H when run forward as a finite seed')
    mu = {}
    for s in range(1, K1 + 1):
        mu[2 * s + 1] = mu_odd[s]
        mu[2 * s + 2] = mu_even[s]
    ok = all(7 * mu[H] >= H + 4 for H in mu if H <= 90)
    check('C3', ok, '7 mu(H) >= H + 4 for 3 <= H <= 90 (the kit\'s S_upto_90, on a sublanguage)')

    # ------------------------------------------------------------ K1: the kit's rung
    say('--- K1: the rung of R30-20261115-fdf6a3')
    res38, n38 = mass_dfs(38, 120, time.time() + 120)
    H38 = horizon(res38, 120)
    res37, n37 = mass_dfs(37, 120, time.time() + 120)
    H37 = horizon(res37, 120)
    box = res38[4][50] or []
    same = set(box) == set(C37ROOTS) and res38[1][50] == 8 and res38[3][50] == 38
    lives = [kit_survive_len(z, 400) for z in C37ROOTS]
    say('   mu(102) = %d; prefixes of popcount <= 38 at H = 102: %d; equal to c37Roots as a set: %s'
        % (mu[102], res38[1][50], set(box) == set(C37ROOTS)))
    say('   popcounts of c37Roots: %s; bit lengths: %s' % ([z.bit_count() for z in C37ROOTS], [z.bit_length() for z in C37ROOTS]))
    say('   survival of the eight as finite seeds (largest H with SurvivesTo): %s; y* survives to %d'
        % (lives, kit_survive_len(YSTAR, 400)))
    say('   exact least horizons: NoMass 37 H first holds at H = %s; NoMass 38 H first holds at H = %s' % (H37, H38))
    okK1 = mu[102] == 38 and same and max(lives) < 111 and kit_survive_len(YSTAR, 400) == 110
    verdict('K1', okK1, 'mu(102) = 38, minimisers = c37Roots, none survives to 111, y* survives to 110')

    # ------------------------------------------------------------ phase 1 statistics
    say('--- phase 1: popcount over every accepted trace (even H)')
    say('   H : B(H), mean, variance, mu(H), x1 = mean - sd sqrt(2 ln B), mu - x1, least support, H - support')
    rows = {}
    for s in range(1, K1 + 1):
        H = 2 * s + 2
        tot = B[s]
        mean = sum(p * c for p, c in enumerate(pops[s])) / tot
        var = sum(c * (p - mean) ** 2 for p, c in enumerate(pops[s])) / tot
        x1 = mean - math.sqrt(var * 2 * math.log(tot)) if tot > 1 else mean
        rows[H] = (tot, mean, var, mu_even[s], x1, minL[s])
        if H % 20 == 2 or H == 162:
            say('   %3d : %8d  %7.3f  %7.3f  %3d  %7.3f  %+6.2f  %3d  %2d'
                % (H, tot, mean, var, mu_even[s], x1, mu_even[s] - x1, minL[s], H - minL[s]))
    Hs = [H for H in rows if 80 <= H <= 162]
    rho, c_mean = linfit(Hs, [rows[H][1] for H in Hs])
    sig2, c_var = linfit(Hs, [rows[H][2] for H in Hs])
    eta, c_ln = linfit(Hs, [math.log(rows[H][0]) for H in Hs])
    say('   fits over 80 <= H <= 162: mean = %.4f H %+.3f; variance = %.4f H %+.3f; ln B = %.5f H %+.3f (theory 0.08858)'
        % (rho, c_mean, sig2, c_var, eta, c_ln))
    slope_fm = rho - math.sqrt(2 * sig2 * eta)
    say('   first-moment slope rho - sqrt(2 sigma^2 eta) = %.4f; fair coins with this entropy: 0.293' % slope_fm)
    band = [(H, rows[H][3] - rows[H][4]) for H in rows if 60 <= H <= 162]
    lo, hi = min(d for H, d in band), max(d for H, d in band)
    okK3a = lo >= -2 and hi <= 12
    offs = sorted(d for H, d in band if H >= 120)
    off = offs[len(offs) // 2]
    say('   mu - x1 over 60 <= H <= 162: least %+.2f, largest %+.2f; median over 120 <= H <= 162: %+.2f' % (lo, hi, off))
    # the lower tail at H = 162 against a Gaussian with the same mean and variance
    tot, mean, var = rows[162][0], rows[162][1], rows[162][2]
    sd = math.sqrt(var)
    tail = [(p, c) for p, c in enumerate(pops[K1]) if c][:10]
    say('   lower tail at H = 162 (popcount: count / Gaussian expectation): ' +
        ', '.join('%d: %d/%.1f' % (p, c, tot * math.exp(-(p - mean) ** 2 / (2 * var)) / (sd * math.sqrt(2 * math.pi))) for p, c in tail))

    # ------------------------------------------------------------ K4, K5 at H = 162; the two coordinates
    say('--- the two coordinates at H = 102 and H = 162')
    for s in (50, K1):
        H = 2 * s + 2
        j = joint[s]
        mup = min(p for (L, p) in j)
        mL = min(L for (L, p) in j)
        sup_of_minpop = sorted(L for (L, p) in j if p == mup)
        pop_of_minsup = sorted(p for (L, p) in j if L == mL)
        say('   H = %d: mu = %d, supports of its minimisers %s; least support %d, popcounts of its minimisers %s'
            % (H, mup, sup_of_minpop, mL, pop_of_minsup))
        best = {}
        for (L, p), c in j.items():
            if p < best.get(L, 10 ** 9):
                best[L] = p
        fr, cur = [], 10 ** 9
        for L in sorted(best):
            if best[L] < cur:
                cur = best[L]
                fr.append('%d:%d' % (L, cur))
        say('      frontier (support W : least popcount among prefixes of support <= W): ' + ' '.join(fr))
        if s == K1:
            okK4 = sup_of_minpop[0] >= 154 and pop_of_minsup[0] >= 1.2 * mup
            verdict('K4', okK4, 'at H = 162 every min-popcount prefix has support >= 154 (least %d) and every min-support prefix has '
                    'popcount >= 1.2 mu = %.1f (least %d)' % (sup_of_minpop[0], 1.2 * mup, pop_of_minsup[0]))
            tails = {}
            for (L, p), c in j.items():
                tails[H - L] = tails.get(H - L, 0) + c
            seq = [tails.get(t, 0) for t in range(0, max(tails) + 1)]
            rat = [seq[t + 1] / seq[t] for t in range(0, 5)]
            okK5 = all(abs(x - 0.5) <= 0.03 for x in rat) and 14 <= max(tails) <= 26
            say('      white-tail counts: %s' % seq)
            verdict('K5', okK5, 'white-tail ratios %s (within 0.03 of 1/2), longest white tail %d (predicted 14 to 26)'
                    % (['%.3f' % x for x in rat], max(tails)))

    # ------------------------------------------------------------ phase 2: popcount-bounded searches
    say('--- phase 2: depth-first searches bounded by popcount')
    KL = 260
    done = {}
    last = None
    durs = []
    budget_end = T0 + 330
    for M in (50, 60, 70, 80, 90, 100, 110, 120):
        if len(durs) >= 2:
            growth = max(2.0, durs[-1] / max(durs[-2], 0.05))
            if time.time() + durs[-1] * growth > budget_end:
                say('   M = %d not started: the time guard predicts %.0f s' % (M, durs[-1] * growth))
                break
        t2 = time.time()
        res, nn = mass_dfs(M, KL, T0 + 450)
        if res is None:
            say('   M = %d stopped by the time limit after %d nodes; discarded' % (M, nn))
            break
        durs.append(time.time() - t2)
        HM = horizon(res, KL)
        peak = max(max(res[0]), max(res[1]))
        done[M] = HM
        last = (M, res)
        say('   M = %3d: NoMass M H first holds at H = %s (H/M = %.3f); %d nodes, %.0f s; largest box %d'
            % (M, HM, HM / M if HM else float('nan'), nn, durs[-1], peak))
    Mstar, res = last
    mu2 = {}
    for s in range(1, KL + 1):
        if res[0][s]:
            mu2[2 * s + 1] = res[2][s]
        if res[1][s]:
            mu2[2 * s + 2] = res[3][s]
    agree = all(mu2[H] == mu[H] for H in mu if H in mu2)
    check('C4', agree and all(mu[H] <= Mstar for H in mu), 'the bounded search reproduces phase 1\'s mu(H) at every H <= 162')
    Hmax = max(mu2)
    say('   mu(H) exact to H = %d (M* = %d): ' % (Hmax, Mstar) +
        ', '.join('%d: %d' % (H, mu2[H]) for H in range(20, Hmax + 1, 20)))
    table = {}
    for M in range(1, Mstar + 1):
        hs = [H for H in sorted(mu2) if mu2[H] > M]
        table[M] = hs[0] if hs else done[Mstar]
    say('   mass table M : least H with NoMass M H   ' +
        ', '.join('%d: %s' % (M, table[M]) for M in sorted(set(list(range(10, Mstar + 1, 5)) + [37, 38, Mstar]))))
    ratios = [(M, table[M] / M) for M in range(40, Mstar + 1) if table[M]]
    okK2 = all(2.4 <= r <= 3.3 for M, r in ratios)
    verdict('K2', okK2, 'H_M / M for 40 <= M <= %d ranges from %.3f to %.3f (predicted 2.4 to 3.3)'
            % (Mstar, min(r for M, r in ratios), max(r for M, r in ratios)))
    Hl = [H for H in mu2 if H >= 60 and H % 2 == 0]
    a_ls, b_ls = linfit(Hl, [mu2[H] for H in Hl])
    say('   least-squares line through mu(H), even H >= 60: mu = %.4f H %+.2f; mu(H)/H from %.4f to %.4f; '
        'differential slope from H = 162 to %d: %.4f'
        % (a_ls, b_ls, min(mu2[H] / H for H in Hl), max(mu2[H] / H for H in Hl), max(Hl),
           (mu2[max(Hl)] - mu2[162]) / (max(Hl) - 162) if max(Hl) > 162 else float('nan')))

    def x1fit(H):
        return rho * H + c_mean - math.sqrt(max(sig2 * H + c_var, 0) * 2 * (eta * H + c_ln))
    preds = []
    for M in sorted(done):
        if M < 50 or not done[M]:
            continue
        hp_raw = next(H for H in range(3, 2000) if x1fit(H) > M)
        hp_off = next(H for H in range(3, 2000) if x1fit(H) + off > M)
        preds.append((M, done[M], hp_off, hp_raw))
    say('   M : exact horizon, extrapolated with the in-sample offset, extrapolated raw   ' +
        ', '.join('%d: %d / %d / %d' % p for p in preds))
    beyond = [p for p in preds if p[1] > 162]
    okK3b = bool(beyond) and all(abs(p[2] - p[1]) <= 0.10 * p[1] for p in beyond)
    verdict('K3', okK3a and okK3b, 'in sample, mu - x1 between %+.2f and %+.2f (band -2 to +12): %s; out of sample, horizons beyond 162 within '
            '10%% of the extrapolation: %s' % (lo, hi, okK3a, okK3b))

    # are the deep minimisers champions at every depth?
    sdeep = max(s for s in range(1, KL + 1) if res[1][s])
    Pd = res[4][sdeep][0]
    exc = [(H, (Pd & ((1 << H) - 1)).bit_count() - mu2[H]) for H in range(20, 2 * sdeep + 3, 2) if H in mu2]
    say('   the deepest survivor of popcount <= %d (H = %d, popcount %d, %d such): excess of its H-bit prefix over mu(H): '
        'largest %d (at H = %d), zero at %d of %d even H'
        % (Mstar, 2 * sdeep + 2, Pd.bit_count(), res[1][sdeep], max(e for H, e in exc), max(exc, key=lambda x: x[1])[0],
           sum(1 for H, e in exc if e == 0), len(exc)))
    say('   minimisers per even H (count at mu, capped at 64): ' +
        ', '.join('%d: %d' % (2 * s + 2, len(res[4][s])) for s in range(49, sdeep + 1, 10)))
    bits = ''.join(str((Pd >> i) & 1) for i in range(2 * sdeep + 2))
    say('   that survivor, depth 1 first: %s' % bits)
    say('failures: %s' % (FAILS if FAILS else 'none'))
    say('done in %.0f s' % (time.time() - T0))


if __name__ == '__main__':
    main()
