# Numbers for the rule 210 essay, computed first (Cloud, 2026-10-23). The kit's ZBL form, depth k = position -k,
# depth 0 the wall, black at even steps (the kit's InX phase). Rule 210 leftward: z(t+1,k+1) = z(t,k+2) xor (not z(t,k+1) and z(t,k)).
def zrows(L, T, D):
    """rows t = 0..T-1 of depths 0..D-1 from start L (a dict or function on depths >= 1); the wall by the clock."""
    row = [1] + [L(k) for k in range(1, D)]
    out = [row]
    for t in range(1, T):
        prev = out[-1]
        new = [1 if t % 2 == 0 else 0] + [0] * (D - 1)
        for k in range(1, D - 1):
            new[k] = prev[k + 1] ^ ((1 - prev[k]) & prev[k - 1])
        new[D - 1] = 0  # beyond the computed width: only valid inside the light cone, which we respect below
        out.append(new)
    return out
T, D = 300, 600
Z = zrows(lambda k: 0, T, D)
# the parity check inside the light cone (depth <= t, where the truncation cannot reach)
bad = [(t, k) for t in range(T) for k in range(0, t + 1) if Z[t][k] == 1 and (t + k) % 2 != 0]
print("black cells with t+k odd, white start, t < 300, k <= t:", len(bad))
print("black cells counted:", sum(Z[t][k] for t in range(T) for k in range(t + 1)))
# column -1 at even steps (must be white), and the derived visible bits at odd steps: sigma(t) = not z(t,1)
print("column -1 at even t < 40:", [Z[t][1] for t in range(0, 40, 2)])
sig = [1 - Z[t][1] for t in range(1, T, 2)]
print("visible bits at odd t = 1, 3, 5, ... (first 64):", ''.join(map(str, sig[:64])))
runs = []
cur, n = sig[0], 0
for b in sig:
    if b == cur: n += 1
    else: runs.append((cur, n)); cur, n = b, 1
runs.append((cur, n))
print("runs:", runs[:12])
# first 12 rows, depths 0..12, as strings (depth increasing to the left, as on the pattern)
for t in range(12):
    print(t, ''.join('#' if Z[t][k] else '.' for k in range(12, -1, -1)), '| wall', Z[t][0])
# how many starts of width <= W keep the clock through time W - 1 (rule 210), W = 1..12
import itertools
for W in range(1, 13):
    cnt = 0
    for bits in itertools.product([0, 1], repeat=W):
        Lw = lambda k, bits=bits: bits[k - 1] if k <= W else 0
        R = zrows(Lw, W, W + W + 2)
        if all(R[t][1] == 0 for t in range(0, W, 2)):
            cnt += 1
    print("W", W, "starts keeping the clock to time W-1:", cnt)
