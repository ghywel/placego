"""edge_hierarchy_look.py: is every finite seed's right-edge emission sequence a ruler (Toeplitz) sequence at every level?

Local, 2026-10-26, after L1000 and edge_levels_look.py. One exploratory run over every seed to width 12, 2,000 steps.
It answers a yes/no question about structure before a hand induction is attempted; it is not a bound or a census.

Hand results so far (L1001 draft, from Theorem R):
  level 1 (Theorem E): widths alternate between exactly 2 and at least 3 (half-ruler), or are all 1 (rain edge);
  level 2: among the widths of at least 3, a 3 always follows a width of 4 or more, and a width of 4 or more always
           follows a 3;
  level 3: the stream of widths of 4 or more is constant at 4 for ever, or always at least 5.

Hypothesis H (the Toeplitz edge). Peel the stream level by level. At each level the stream alternates between its
minimum value and a stream of strictly larger values, or it is constant from some point on.

Predictions (written before the run):
  H1  Every half-ruler seed's emission sequence satisfies H at every level the run can resolve (at least 8 values).
  H2  Level values start (2, 3), then either (4) as a constant, or 5 and further levels.
  H3  The single seed's level values are 8.73's 2, 3, 5, 6, 8, 14, 15, 23, ...
  H4  More than one infinite-looking level list occurs among seeds (the deeper levels are seed-dependent).
Counterfactual: a seed whose stream at some level neither alternates with its minimum nor becomes constant refutes H.
Transient: the first 4 values of each level are skipped before testing, a declared allowance, not tuned.
Record searched: "Toeplitz" (8.72, 8.73: the single seed's edge), "Right-prefix periods" (G249: the edge strip is
eventually periodic for every finite seed), "half-ruler" 0.

Run: python3 -I tests/probes/wolfram/edge_hierarchy_look.py

Outcome (2026-10-26, M5, 7 s):
- H1 held: all 2,048 half-ruler seeds satisfy H at every resolvable level.
- H2 held. H3 held: 2, 3, 5, 6, 8, 14, 15.
- H4 was refuted the interesting way. There is only one level list, the single seed's; every other seed follows it and
  freezes at a gap value (4, 7, 9 to 13).
- The appended spine test held exactly: equal depth k* gives equal lists, the frozen width is k* - 1, and S2 had no
  violations. Its first version forgot to bit-reverse the seed into its edge code and printed impossible k* = 0 for
  odd codes; fixed before S1 was read. This led to Theorem U (L1001).
"""
from collections import Counter

T = 2000
SKIP = 4


def emissions(seed_int):
    xi = seed_int << (T + 4)
    prevL = None
    out = []
    for t in range(T):
        e = xi.bit_length() - 1
        L = 0
        while (xi >> (e - L)) & 1:
            L += 1
        if prevL is not None and prevL >= 2:
            k = 0
            while not (xi >> (e - 1 - k)) & 1:
                k += 1
            out.append(k)
        prevL = L
        xi = (xi << 1) ^ (xi | (xi >> 1))
    return out


def peel(stream):
    """Return (level values, verdict). Verdict 'ok' if H holds at every resolvable level."""
    values = []
    s = stream
    while len(s) >= SKIP + 8:
        s = s[SKIP:]
        lo = min(s)
        if all(v == lo for v in s):
            values.append(("const", lo))
            return values, "ok"
        a, b = s[0::2], s[1::2]
        if all(v == lo for v in a) and all(v > lo for v in b):
            rest = b
        elif all(v == lo for v in b) and all(v > lo for v in a):
            rest = a
        else:
            values.append(("broken", tuple(s[:10])))
            return values, "broken"
        values.append(lo)
        s = rest
    values.append(("unresolved", len(s)))
    return values, "ok"


verdicts = Counter()
lists = Counter()
example = {}
single = None
for w in range(1, 13):
    for bits in range(1 << (w - 1)):
        seed = bits | (1 << (w - 1))
        ws = emissions(seed)
        if 1 in ws[1:]:
            continue
        vals, verdict = peel(ws)
        verdicts[verdict] += 1
        key = tuple(v if not isinstance(v, tuple) else v[0] + ":" + str(v[1]) for v in vals)
        lists[key] += 1
        example.setdefault(key, bin(seed)[2:][::-1])
        if seed == 1:
            single = key
print("verdicts over half-ruler seeds:", dict(verdicts))
print("single seed level list:", single)
print("distinct level lists:", len(lists))
for key, n in lists.most_common(15):
    print(" ", n, key, "e.g. seed", example[key])


# ---- Second question, appended after the first run (predictions written before this part ran) ----
# GC808: in edge coordinates R (bit k = cell at distance k from the rightmost black cell), one step is
# T(R) = R XOR (2R OR 4R), a 2-adic isometry, and the single seed is R = 1. Hypothesis S (the spine): a half-ruler
# seed's level list follows the single seed's for exactly as long as its code R0 stays on the single seed's cycle,
# i.e. while R0 mod 2^k lies in {T^t(1) mod 2^k}; it freezes once the code leaves.
# Prediction S1: the number of spine levels a seed shows is a nondecreasing function of k*(R0), the largest k with
#   R0 mod 2^k on the spine cycle; seeds with equal k* show equal level lists.
# Prediction S2: half-ruler <=> R0 mod 8 in {1, 7} (GC808's cycle of 1), rain edge <=> R0 mod 8 in {3, 5}.
# Counterfactual: two seeds with equal k* but different level lists refute S1.
def T_edge(R, k):
    return (R ^ ((2 * R) | (4 * R))) & ((1 << k) - 1)


KMAX = 24
spine = []
for k in range(1, KMAX + 1):
    seen = set()
    R = 1 % (1 << k)
    while R not in seen:
        seen.add(R)
        R = T_edge(R, k)
    spine.append(seen)


def kstar(R0):
    k = 0
    while k < KMAX and (R0 % (1 << (k + 1))) in spine[k]:
        k += 1
    return k


by_k = {}
s2_bad = 0
for w in range(1, 13):
    for bits in range(1 << (w - 1)):
        seed = bits | (1 << (w - 1))
        R0 = int(bin(seed)[2:][::-1], 2)        # rightmost cell (highest seed bit) becomes bit 0 of R
        # (first version forgot the reversal and printed k* = 0 for odd codes; fixed before reading S1)
        ws = emissions(seed)
        rain = 1 in ws[1:]
        if rain != ((R0 % 8) in (3, 5)):
            s2_bad += 1
        if rain:
            continue
        vals, verdict = peel(ws)
        spine_levels = sum(1 for v in vals if not isinstance(v, tuple))
        by_k.setdefault(kstar(R0), Counter())[tuple(str(v) for v in vals)] += 1
print("S2 violations:", s2_bad)
print("spine cycle lengths mod 2^k, k = 1..%d:" % KMAX, [len(s) for s in spine])
for k in sorted(by_k):
    print("  k* =", k, ":", dict(by_k[k]))
