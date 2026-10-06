"""collatz_audit_g67_g69.py: Local's checks of GPT's G67 (the maximal affine offset at a first coefficient deficit),
G68 (two endpoint ceilings and digit certificates) and G69 (the polynomial first-deficit ceiling from Rhin's bound),
the second reader's companion to argument audits, independent of GPT's OB/EC/LF controls. Exact integers only.
(Local, 2026-10-06; PROOFS.md notes; chat L037.)
COMMAND:    python3 tests/probes/prizes/collatz_audit_g67_g69.py      (under a minute)
OUTCOME, 2026-10-06: ALL CHECKS PASS (81,119 first-deficit words to length 24; G68 on all to length 20; G69 to a = 2000,
  least observed exponent -1.585). G70 part (added the same day): inclusion and cutoff for n < 65,536,
  T <= 40, the only discrepancy start is 1; the width criterion with T = ceil(3w/2) first holds at w = 104.
"""
import math
fails = 0

def first_deficit_words(tmax):
    """DFS over admissible prefixes; yield (word, a, t) for words whose first coefficient deficit is at their end."""
    out = []
    def go(w, a):
        t = len(w)
        for b in (0, 1):
            a2 = a + b; t2 = t + 1
            if 3 ** a2 < 2 ** t2: out.append((w + [b], a2, t2))
            elif t2 < tmax: go(w + [b], a2)
    go([], 0)
    return out

words = first_deficit_words(24)
def intercept(w):
    B = 0
    for t, b in enumerate(w): B = 3 ** b * B + b * 2 ** t
    return B
best = {}
for w, a, t in words:
    if a == 0: continue
    fails += t != (3 ** a).bit_length()                       # t = least integer with 2^t > 3^a
    B = intercept(w)
    if a not in best or B > best[a][0]: best[a] = (B, [w], t)
    elif B == best[a][0]: best[a][1].append(w)
Bmax = lambda a: sum(3 ** (a - 1 - i) * 2 ** ((3 ** i).bit_length() - 1) for i in range(a))
for a, (B, ws, t) in best.items():
    if t <= 24 and len(ws) == 1:
        fails += B != Bmax(a)
    else:
        fails += 1
for a in range(1, 400):
    A = 3 ** a; Bm = Bmax(a)
    fails += not (a * A < 6 * Bm and 3 * Bm <= a * A) or (a > 1 and 3 * Bm == a * A)
fails += intercept([0, 0, 1, 1]) != 20 or intercept([1, 1, 0, 0]) != 5
print("G67:", len(words), "first-deficit words to length 24; per-a maximum unique and equal to B_max(a) for a =", sorted(best)[:3], "..", max(best), "; envelope a = 1..399")

# G68: endpoint identities and certificate soundness on every first-deficit word to length 20 with a >= 1.
for w, a, t in words:
    if a == 0 or t > 20: continue
    M, A = 2 ** t, 3 ** a; D = M - A; B = intercept(w); K = B // D
    r = (-B * pow(A, -1, M)) % M; y = (A * r + B) // M
    fails += (A * r + B) % M != 0 or not (0 < y < A) or r <= 0
    lifts_n = max(0, 1 + (K - r) // M); lifts_q = max(0, 1 + (K - y) // A)
    fails += lifts_n != lifts_q
    if lifts_n:   # an actual survivor: check by direct evolution
        n = r; x = n
        for b in w:
            fails += x % 2 != b; x = (3 * x + 1) // 2 if x % 2 else x // 2
        fails += x < n
    for s in range(t + 1):                                   # prefix certificate is sound
        u = w[:s]; au = sum(u); Cu = intercept(u)
        rho = (-Cu * pow(3 ** au, -1, 2 ** s)) % (2 ** s) if s else 0
        L = rho if rho > 0 else 2 ** s
        if L > K: fails += lifts_n > 0
w = [1, 1, 0, 1, 1, 0, 0]; t = 7; a = 4; M, A = 128, 81; B = intercept(w); K = B // (M - A)
r = (-B * pow(A, -1, M)) % M; y = (A * r + B) // M
fails += (K, r, y) != (1, 59, 38)
print("G68: identities, lift counts and prefix-certificate soundness on all first-deficit words to length 20; guard 1101100 (K, r, y) =", (K, r, y))

# G69: the exact consequences of the cited bound, a = 1..2000: D/A > t^-13.3 (as D^10 t^133 > A^10) and
# K_max < a t^13.3 / 3 (as 3^10 K^10 < a^10 t^133); also the least observed exponent log(D/A)/log t.
worst = 0.0
for a in range(1, 2001):
    A = 3 ** a; t = A.bit_length(); D = 2 ** t - A
    fails += not (D ** 10 * t ** 133 > A ** 10)
    K = Bmax(a) // D
    fails += not (3 ** 10 * K ** 10 < a ** 10 * t ** 133)
    worst = min(worst, (math.log(D) - math.log(A)) / math.log(t) if t > 1 else 0)
print("G69: cited-bound consequences hold for a = 1..2000; least observed log(D/A)/log t =", round(worst, 3), "(the cited floor is -13.3)")
# G70 (added 2026-10-06): C(T) is contained in A(T), and every start in A(T) \ C(T) is below R(T) = T^14.3 / 3 (exact
# tenth-power form 3^10 n^10 < T^143); direct trajectories for n < 2^16, T <= 40. Also the width threshold for
# T = ceil(3w/2): the least w with 3^10 2^(10(w-1)) >= T^143, and the n = 1, T = 2 guard.
disc = {}
for n in range(1, 1 << 16):
    x = n; a = 0; inA = True; inC = True
    for T in range(1, 41):
        if x % 2: a += 1; x = (3 * x + 1) // 2
        else: x //= 2
        inA = inA and x >= n; inC = inC and 3 ** a >= 2 ** T
        if inC and not inA: fails += 1                      # C must be inside A
        if inA and not inC:
            fails += not (3 ** 10 * n ** 10 < T ** 143)
            disc.setdefault(T, set()).add(n)
        if not inA and not inC: break
fails += 1 not in disc.get(2, set())
first = next(w for w in range(2, 400) if 3 ** 10 * 2 ** (10 * (w - 1)) >= (-(-3 * w // 2)) ** 143)
print("G70: inclusion and cutoff hold for n < 65,536, T <= 40; discrepancy starts found:", sorted(set().union(*disc.values())) if disc else [],
      "; the width criterion with T = ceil(3w/2) first holds at w =", first)
# G71 (added 2026-10-06): the boundary-loss recurrence V(t+1) = 2V(t) - N(t), the first-paid-bit identity
# 2 C_w(w) - V(w) = F(w-1), and the later loss process C_w(t+1) = C_w(t) - E_w(t), checked by direct trajectories of
# every width-w start for w = 2 .. 15 to horizon 30 (coefficient survival of each start's own parity word).
ell = lambda t: 0 if t == 0 else (2 ** t).bit_length() * 0 + next(a for a in range(t + 1) if 3 ** a > 2 ** t)
TT = 30
Vc = [1]; cur = {0: 1}; Nc = []
for t in range(TT):
    crit = ell(t + 1) == ell(t) + 1
    Nc.append(cur.get(ell(t), 0) if crit else 0)
    nxt = {}
    for a, c in cur.items():
        for b in (0, 1):
            if 3 ** (a + b) > 2 ** (t + 1): nxt[a + b] = nxt.get(a + b, 0) + c
    cur = nxt; Vc.append(sum(cur.values()))
    fails += Vc[t + 1] != 2 * Vc[t] - Nc[t]
for w in range(2, 16):
    m = w - 1
    surv = [0] * (TT + 1); E = [0] * TT; F = 0
    for n in range(2 ** m, 2 ** w):
        x = n; a = 0; alive = True
        for t in range(TT):
            if alive: surv[t] += 1
            crit = ell(t + 1) == ell(t) + 1
            if alive and crit and a == ell(t):
                if x % 2 == 0: E[t] += 1
                if t == m: F += (-1) ** ((x - 3 ** a) % 2)   # q = x - 3^a at the free-bit boundary
            if x % 2: a += 1; x = (3 * x + 1) // 2
            else: x //= 2
            if alive and not (3 ** a > 2 ** (t + 1)): alive = False
        if alive: surv[TT] += 1
    fails += surv[m] != Vc[m]                                          # free bits: C_w(m) = V(m)
    fails += 2 * surv[w] - Vc[w] != F                                  # first paid bit
    fails += any(surv[t + 1] != surv[t] - E[t] for t in range(TT))   # loss process
print("G71: recurrence for V to T = 30; first-paid-bit identity and loss process for every width 2..15 (direct trajectories)")
# G72, G73 (added 2026-10-06): for admitted (coefficient-surviving) width-w starts at horizon t, the band
# 3^a 2^(w-1) <= 2^t y < 3^(a+1) 2^(w-1) labels a; equal terminals have |n - n'| < a/3; the label (y, n mod 2^s) with
# 3 * 2^s >= t is injective. Also look for ACTUAL admitted collisions (GPT's samples had none) and check the span there.
coll = 0; maxspan = 0; checked72 = 0
for w in range(2, 19):
    m = w - 1
    for t in sorted({m, m + 3, m + 8, min(3 * 2 ** m, 40)}):
        if t > 3 * 2 ** m: continue
        fib = {}
        for n in range(2 ** m, 2 ** w):
            x = n; a = 0; ok = True
            for k in range(1, t + 1):
                if x % 2: a += 1; x = (3 * x + 1) // 2
                else: x //= 2
                if 3 ** a < 2 ** k: ok = False; break
            if not ok: continue
            checked72 += 1
            fails += not (3 ** a * 2 ** m <= 2 ** t * x < 3 ** (a + 1) * 2 ** m)
            fib.setdefault(x, []).append((n, a))
        s_ = next(s for s in range(0, 64) if 3 * 2 ** s >= t)
        for y, lst in fib.items():
            if len(lst) > 1:
                coll += 1
                aa = {a for _, a in lst}; fails += len(aa) != 1
                a0 = lst[0][1]; ns = [n for n, _ in lst]
                span = max(ns) - min(ns); maxspan = max(maxspan, span)
                fails += not (3 * span < a0)
                fails += len({n % 2 ** s_ for n in ns}) != len(ns)
print("G72/G73: band labels on", checked72, "admitted (w, t) samples, w = 2..18; actual admitted collisions found:", coll,
      "; largest collision span", maxspan, "(always below a/3; short labels injective)")
# G74 (added 2026-10-06): the backward-weight telescoping identity C_w(T) - Q_w(T) = (1/2) sum_t sum_a I_w(t,a) Delta_t(a)
# in exact rationals, widths 2..13, T = m .. m + 14, by direct trajectories.
from fractions import Fraction as Fr
def ellf(j): return 0 if j == 0 else next(a for a in range(j + 1) if 3 ** a > 2 ** j)
n74 = 0
for w in range(2, 14):
    m = w - 1
    for T in range(m, m + 15):
        f = {T: {}}
        for a in range(0, T + 2): f[T][a] = Fr(1) if a >= ellf(T) else Fr(0)
        for t in range(T - 1, -1, -1):
            f[t] = {}
            for a in range(0, T + 2):
                f[t][a] = Fr(0) if a < ellf(t) else (f[t + 1].get(a, Fr(0)) + f[t + 1].get(a + 1, Fr(1))) / 2
        I = {}; C = 0
        for n in range(2 ** m, 2 ** w):
            x = n; a = 0; alive = True
            for t in range(T):
                if t >= m and alive:
                    I[(t, a)] = I.get((t, a), 0) + (1 if x % 2 else -1)
                if x % 2: a += 1; x = (3 * x + 1) // 2
                else: x //= 2
                if 3 ** a < 2 ** (t + 1): alive = False
            C += alive
        rhs = Fr(0)
        for (t, a), iv in I.items():
            rhs += Fr(iv, 2) * (f[t + 1].get(a + 1, Fr(1)) - f[t + 1].get(a, Fr(0)))
        # Q_w(T) = H_m = sum over admitted length-m words of f_m(a); count admitted length-m words by a
        Hm = Fr(0)
        for n in range(2 ** m, 2 ** w):
            x = n; a = 0; ok = True
            for t in range(m):
                if x % 2: a += 1; x = (3 * x + 1) // 2
                else: x //= 2
                if 3 ** a < 2 ** (t + 1): ok = False; break
            if ok: Hm += f[m][a]
        fails += Fr(C) - Hm != rhs
        n74 += 1
print("G74: telescoping identity exact in", n74, "width/horizon cases (w = 2..13, T = m..m+14)")

# G75: the exact distribution of J (max demand) by dynamic programming, for horizons h up to 300, and the bound
# min over L of L/sqrt(h+1) + 32 exp(-(L-1)/2); report the first h where the bound is below 1 (non-vacuous) and check it.
first_nonvac = None; checked75 = 0
for h in (8, 16, 32, 64, 128, 200, 300):
    T = h + 50; t = T - h - 1
    # J = max over j = t+1..T of (ell_j - Z_(j-t-1)); Z counts fair bits for steps t+2..T (h bits).
    dist = {(0, ellf(t + 1)): Fr(1)}                     # (Z so far, running max) after j = t+1 (Z_0 = 0)
    for k in range(1, h + 1):
        j = t + 1 + k; nd = {}
        for (z, mx), pr in dist.items():
            for b in (0, 1):
                z2 = z + b; v = max(mx, ellf(j) - z2)
                nd[(z2, v)] = nd.get((z2, v), Fr(0)) + pr / 2
        dist = nd
    Jd = {}
    for (z, mx), pr in dist.items(): Jd[mx] = Jd.get(mx, Fr(0)) + pr
    atom = max(Jd.values())
    bound = min(L / math.sqrt(h + 1) + 32 * math.exp(-(L - 1) / 2) for L in range(1, 200))
    fails += float(atom) > bound + 1e-12
    if bound < 1 and first_nonvac is None: first_nonvac = h
    checked75 += 1
    print(f"   G75 h = {h}: max atom of J = {float(atom):.4f}, bound {bound:.4f}")
print("G75: exact J distributions checked; first non-vacuous horizon among those tried:", first_nonvac)
print("ALL CHECKS PASS" if fails == 0 else f"{fails} CHECK(S) FAILED")
