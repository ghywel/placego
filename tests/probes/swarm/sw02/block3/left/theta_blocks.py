#!/usr/bin/env python3
"""The left side of the block languages: what Theta does to X's and Y's words.

Why this comes first. Every free word f has its left half Theta f (Rule30ZeroBoundary.Q01_iff_Theta), so a window graph on
the left constrains nothing: only finiteness of Theta f can exclude a word. Theta f at depth k reads f through the sideways
recursion C_(k+1)(t) = C_k(t + 1) xor (C_k(t) or C_(k-1)(t)), C_0 = 0, C_1 = alt f, from ticks 0 to k.

Prediction, written before the run. Take u = (25)^a E (25)^b, f = not u. Outside the past cone of E, the columns are the
periodic backgrounds of the two phases of 25. Inside the cone the sideways rule is chaotic, so the cone fills with
a growing aperiodic region (0.7). Then Theta on these words has no finite-state description, and a certificate of the kind
that would settle Q01X does not exist in this form.
Counterfactual (0.3): the interface between the two phases stays narrow, or the cone fills with a third periodic background.
Then Theta on X's words is a finite-state transducer, its image can be searched for an all-white tail, and Q01X could
have a finite certificate.
Control: f = not 25-word gives a periodic row, by Theta on a periodic word; the kit's free_not_eventuallyPeriodic says no
periodic f has a finite row. Report pre-period, period, and largest white run.
"""
import sys, zlib
sys.path.insert(0, sys.argv[1]); import ref

def uword(gaps):
    w = []
    for g in gaps: w += [1] + [0] * (g - 1)
    return w
def columns(fbits, K):
    """C_1 .. C_K as ints, bit t = tick t, on ticks with a known future."""
    T = 2 * len(fbits)
    c = 0
    for t in range(T):
        if t % 2 == 0 or fbits[t // 2]: c |= 1 << t
    cp = 0
    out = [c]
    for k in range(1, K):
        n = T - k
        c, cp = ((c >> 1) ^ (c | cp)) & ((1 << n) - 1), c
        out.append(c)
    return out, T

def background(word, K, reps):
    u = word * reps
    cols, T = columns([1 - x for x in u], K)
    return cols, T

def report_background(name, gaps, K=4000):
    w = uword(gaps); P = len(w)
    reps = (K // P + 8) * 2 + 8
    cols, T = background(w, K, reps)
    per = 2 * P
    words = [c & ((1 << per) - 1) for c in cols]
    seen = {}
    pair = None
    for k in range(1, K):
        key = (words[k - 1], words[k])
        if key in seen: pair = (seen[key], k); break
        seen[key] = k
    row = ''.join(str(c & 1) for c in cols)
    wr = max((len(x) for x in row.split('1')), default=0)
    print(name, 'word period', P, 'steps; pair of columns repeats at k =', pair, 'row black share %.3f' % (row.count('1') / len(row)), 'longest white run', wr)
    if pair:
        a, b = pair
        print('  pre-period', a, 'spatial period', b - a, 'row', row[:min(b + 8, 120)])
    return pair

report_background('25', [2, 5])
report_background('2', [2])
report_background('E', [3, 3, 5, 3, 5, 5, 5, 5])
report_background('(25)^6 E', [2, 5] * 6 + [3, 3, 5, 3, 5, 5, 5, 5])
report_background('(25)^4 E (25)^7 E', [2, 5] * 4 + [3, 3, 5, 3, 5, 5, 5, 5] + [2, 5] * 7 + [3, 3, 5, 3, 5, 5, 5, 5])
report_background('45 2^3', [4, 5, 2, 2, 2])
report_background('45 2^8', [4, 5] + [2] * 8)

E = [3, 3, 5, 3, 5, 5, 5, 5]
A, B, K = 200, 200, 1500
u = uword([2, 5] * A + E + [2, 5] * B)
cols, T = columns([1 - x for x in u], K)
tau = 2 * len(uword([2, 5] * A))
# backgrounds on each side: the same word with E removed on one side, extended far
left = uword([2, 5] * (A + B + 40))
lc, _ = columns([1 - x for x in left], K)
right_u = uword([2, 5] * (A + B + 40))
off = len(uword(E)) % 7   # phase of the loop after E, in steps
rshift = uword([2, 5] * 3)
right_u = right_u[(7 - off) % 7:]
rc, _ = columns([1 - x for x in right_u], K)
tail = tau + 2 * len(uword(E))
print('E at ticks', tau, 'to', tail, 'of', T)
for k in (1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 1400):
    n = T - k
    c = cols[k - 1]
    d = (c ^ lc[k - 1]) & ((1 << min(tau, n)) - 1)
    lo = d.bit_length() and (d & -d).bit_length() - 1
    # right edge: compare with the right-phase background, aligned at the end of E
    sh = (tail) % 14
    best = None
    for s in range(14):
        rr = (rc[k - 1] >> s)
        m = n - tail
        if m <= 0: break
        x = ((c >> tail) ^ rr) & ((1 << m) - 1)
        if best is None or bin(x).count('1') < best[0]:
            best = (bin(x).count('1'), s, x)
    hi = tail + (best[2].bit_length() if best else 0)
    inner = ''.join(str((c >> t) & 1) for t in range(max(lo, 0), min(hi, n)))
    z = len(zlib.compress(inner.encode(), 9)) if inner else 0
    print(' k', k, 'first difference from the left background at tick', lo, 'last from the right at', hi, 'width', hi - lo, 'distance from cone edge', lo - (tau - k), 'compressed/len %.3f' % (z / max(1, len(inner))), 'right mismatches', best[0] if best else None)
