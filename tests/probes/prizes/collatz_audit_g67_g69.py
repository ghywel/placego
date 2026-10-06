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
print("ALL CHECKS PASS" if fails == 0 else f"{fails} CHECK(S) FAILED")
