#!/usr/bin/env python3
"""rule30_words.py: black alone, white alone, and both: the wall form for every word of period up to 4 (lead 1).

RUN-ON:     cpu (pure Python 3, standard library; records.c for the control)
COMMAND:    python3 tests/probes/lexicon/rule30_words.py
COST:       several minutes on one core, under 2 GB.

The owner's lead (2026-10-05): "just as we found studying the left by itself, the right by itself and both yielded
results, considering white by itself is just as important. Black, Both, White."
The wall form (rule30_wall.py, PRIZE-PROBLEMS.md section 8.39), for any centre word w (column 0 = w_t, repeating).
Both halves evolve forward by Rule 30 against the wall, each from its own row 0, and the centre update
x_{t+1}(0) = x_t(-1) XOR (w_t OR x_t(1)) must give w_{t+1}. That splits by the wall's colour at time t:
  - black (w_t = 1): x_t(-1) = NOT w_{t+1}, a condition on the left half alone;
  - white (w_t = 0): x_t(-1) XOR x_t(1) = w_{t+1}, a condition coupling the two halves.
A finite configuration whose column 0 is w from time 0 to T keeps both. Three games, each from a left seed and a right
seed of width s (white beyond), each scored by T, the first time a condition it keeps fails, maximised over seeds:
  T_B(s), black alone (the left seed only; Conjecture LR for w says T_B is finite);
  T_W(s), white alone (both seeds, white conditions only);
  T_BW(s), both (the real problem: column 0 = w for a finite configuration).
Each condition at time t < s fixes the left cell at depth t + 1 (the left edge of its light cone is pure XOR), so the
free data are the left cells at depths whose time carries no kept condition, plus the right seed.
Black alone also has the diagonal form (records.c, generalised): a zero run of the forced left half from depth d,
where column 1 is free at the wall's white times. Its census merges walks as rule30_merge.py does, so it reaches
deeper: R_w(d), and the distinct walks D_w(d).
The coin model. In black alone each black time costs one coin, so the best of n walks survives about
(log2 n + 0.33) / beta cells, beta the black fraction of w. Under the coin model, with no merging:
T_B(s) ~ s / beta, T_W(s) ~ s + s (1 + beta) / (1 - beta), and T_BW(s) <= min(T_B, T_W).

PREDICTIONS, written 2026-10-05 before this script's first run (words 0, 1, 01, 001, 011, 0001, 0011, 0111, and a
random wall of 4096 bits as the chaos step; "two-colour words" are 01 .. 0111):
  WD0 (controls, must hold): (a) for w = 01 the census reproduces records.c's R(d) at every depth from 3 to 33; (b)
      for every word, T_B(s) from the wall equals s + R_w(s + 1) from the census, for each s computed (two
      instruments); (c) T_BW(s) <= min(T_B(s), T_W(s)) wherever all three are computed (inclusion); (d) the known
      answer for w = 1 (Condrey's period 1): the forced left half is vertical stripes, so R_1(d) = d mod 2.
  WD1 (blind; merging everywhere): for every two-colour word and the random wall, the distinct walks grow at a steady
      rate per free bit, lambda between 1.6 and 1.9 at the largest depth reached.
  WD2 (blind; one coin law for every word): for every two-colour word and the random wall, the records follow the
      coin's best over the distinct walks: the mean of R_w(d) - (log2 D_w(d) + 0.33) / beta over depths from 15 up
      lies between -4 and +4.
  WD3 (blind; both binds): at the largest s where all three games are computed, T_BW(s) <= min(T_B(s), T_W(s)) - 2
      for at least 4 of the 6 two-colour words: the two kinds of condition compound.
  WD4 (blind; white alone, the owner's lead): for every word with a white cell, T_W grows linearly, with
      least-squares slope over s within 35% of the merged coin value 1 + 0.82 (1 + beta) / (1 - beta).
  WD5 (blind; both): for every word, the least-squares slope of T_BW over s lies between 1.0 and 2.0.
  WD6 (random-chaos: does periodicity matter?): the random wall obeys WD1 and WD2 like 01, whose black fraction it
      shares, so left rigidity would not need a periodic centre at all.
REFUTED-BY: WD0 failing (the instruments); WD1 to WD6 failing.
"""
import math, pathlib, random, statistics, subprocess, sys, tempfile

HERE = pathlib.Path(__file__).resolve().parent
FAILS = 0
CAP_STATES = 1_500_000


def report(name, ok, detail=""):
    global FAILS
    FAILS += not ok
    print(f"{'PASS' if ok else 'FAIL'}  {name}" + (f"  ({detail})" if detail else ""), flush=True)


def verdict(name, held, detail=""):
    print(f"{'HELD' if held else 'REFUTED'}  prediction {name}" + (f"  ({detail})" if detail else ""), flush=True)


def slope(xs, ys):
    mx, my = statistics.fmean(xs), statistics.fmean(ys)
    return sum((x - mx) * (y - my) for x, y in zip(xs, ys)) / sum((x - mx) ** 2 for x in xs)


# ---- black alone, diagonal form: the forced left half for column 0 = w, column 1 free at white times ----

def diag(P, Q, c, k, W):
    X = (P << 1) | (Q << 2) | (c << 1)
    X = (X & ~1) | W[k % len(W)]
    s = 1
    while s <= k:
        X ^= X << s
        s <<= 1
    return X & ((2 << k) - 1)


def canon(P, Q):
    return P, Q & ~(P >> 1)


def run_from(front, d, W, cap):
    """Merged forced walk from the depth-d frontier; returns the longest zero run (cap if reached)."""
    cur, k, best = dict(front), d, 0
    while cur and k - d < cap:
        nxt = {}
        free = W[(k - 1) % len(W)] == 0
        for (P, Q), m in cur.items():
            A = diag(P, Q, 0, k, W)
            if (A >> k) & 1:
                if free:
                    A = diag(P, Q, 1, k, W)
                else:
                    best = max(best, k - d)
                    continue
            key = canon(A, P)
            nxt[key] = nxt.get(key, 0) + m
        cur, k = nxt, k + 1
    return cap if cur else best


def census(W, dmax):
    """R_w(d) and D_w(d) for d = 2 .. while the frontier stays under CAP_STATES."""
    front, k, R, D = {canon(W[0], 0): 1}, 1, {}, {}
    beta = sum(W) / len(W)
    while k <= dmax and len(front) <= CAP_STATES:
        if k >= 2:
            D[k] = len(front)
            R[k] = run_from(front, k, W, int(6 * k / max(beta, 0.05)) + 60)
        free = W[(k - 1) % len(W)] == 0
        nxt = {}
        for (P, Q), m in front.items():
            for c in ((0, 1) if free else (0,)):
                key = canon(diag(P, Q, c, k, W), P)
                nxt[key] = nxt.get(key, 0) + m
        front, k = nxt, k + 1
    return R, D


# ---- the wall form: three games ----

def left_x1(lrow, t, W, width):
    """x_t(-1) of the left half evolved t steps from row 0 = lrow (bit j - 1 = x_0(-j)) against the wall."""
    r, p, mask = lrow, len(W), (1 << width) - 1
    for u in range(t):
        r = ((r >> 1) ^ (r | ((r << 1) | W[u % p]))) & mask
    return r & 1


def right_col1(rrow, T, W):
    """x_t(1) for t = 0 .. T of the right half from row 0 = rrow (bit i - 1 = x_0(i)) against the wall."""
    out, r, p = [], rrow, len(W)
    for t in range(T + 1):
        out.append(r & 1)
        r = ((r << 1) | W[t % p]) ^ (r | (r >> 1))
    return out


def kept(game, black):
    return (black and game in ("B", "BW")) or ((not black) and game in ("W", "BW"))


def target(W, t, col1):
    p = len(W)
    return 1 - W[(t + 1) % p] if W[t % p] else W[(t + 1) % p] ^ col1[t]


def first_failure(lrow, s, W, game, col1, tmax):
    """Evolve the left seed (white beyond s) and return the first time >= s a kept condition fails (tmax + 1: none)."""
    width = s + tmax + 4
    r, p, mask = lrow, len(W), (1 << width) - 1
    for t in range(tmax + 1):
        if t >= s and kept(game, W[t % p]) and (r & 1) != target(W, t, col1):
            return t
        r = ((r >> 1) ^ (r | ((r << 1) | W[t % p]))) & mask
    return tmax + 1


def game_value(W, s, game, tmax):
    """max over seeds of the first failing time; left cells at depths 1 .. s are forced where a condition is kept."""
    p = len(W)
    best = -1
    rights = [0] if game == "B" else range(1 << s)
    for rr in rights:
        col1 = right_col1(rr, tmax + 1, W) if game != "B" else [0] * (tmax + 2)
        stack = [(0, 0)]                                       # (time t whose depth t + 1 is next, left row so far)
        while stack:
            t, lrow = stack.pop()
            if t == s:
                best = max(best, first_failure(lrow, s, W, game, col1, tmax))
                continue
            if kept(game, W[t % p]):
                x = left_x1(lrow, t, W, t + 2)                 # depth t + 1 is 0 in lrow so far
                stack.append((t + 1, lrow | ((x != target(W, t, col1)) << t)))
            else:
                stack.append((t + 1, lrow))
                stack.append((t + 1, lrow | (1 << t)))
    return best


def free_bits(W, s, game):
    p = len(W)
    return sum(1 for t in range(s) if not kept(game, W[t % p])) + (0 if game == "B" else s)


def main():
    rng = random.Random(4096)
    words = {"0": [0], "1": [1], "01": [0, 1], "001": [0, 0, 1], "011": [0, 1, 1], "0001": [0, 0, 0, 1],
             "0011": [0, 0, 1, 1], "0111": [0, 1, 1, 1], "random": [rng.getrandbits(1) for _ in range(4096)]}
    two = ["01", "001", "011", "0001", "0011", "0111"]
    beta = {n: sum(W) / len(W) for n, W in words.items()}
    cen = {}
    for n in ["1", "01", "001", "011", "0001", "0011", "0111", "random"]:
        R, D = census(words[n], 41)
        cen[n] = (R, D)
        top = max(D)
        print(f"   census {n:6s} (beta {beta[n]:.3f}): to depth {top}, D = {D[top]}; R_w(d) for d = 2 .. {top}: "
              + " ".join(str(R[d]) for d in sorted(R)), flush=True)
    exe = pathlib.Path(tempfile.gettempdir()) / "rule30_words_records"
    subprocess.run(["cc", "-O2", "-fopenmp", "-o", str(exe), str(HERE / "records.c")], check=True)
    ok_a = True
    for d in range(3, 34):
        out = subprocess.run([str(exe), str(d), "0"], check=True, capture_output=True, text=True).stdout
        ok_a &= int(out.split()[2]) == cen["01"][0][d]
    R1 = cen["1"][0]
    ok_d = all(R1[d] == d % 2 for d in R1)

    games = {}
    for n, W in words.items():
        if n == "random":
            continue
        for g in ("B", "W", "BW"):
            if (g == "B" and beta[n] == 0) or (g == "W" and beta[n] == 1):
                continue                                       # no kept condition: never fails
            vals = {}
            for s in range(2, 20):
                if free_bits(W, s, g) > 16:
                    break
                tmax = int(3 * s / max(min(beta[n], 1 - beta[n]), 0.2)) + 30
                vals[s] = game_value(W, s, g, tmax)
            games[(n, g)] = vals
            print(f"   {n:5s} {g:2s}: " + " ".join(f"{s}:{v}" for s, v in vals.items()), flush=True)
    ok_b = all(games[(n, "B")][s] == s + cen[n][0][s + 1] for n in words if (n, "B") in games and n in cen
               for s in games[(n, "B")] if s + 1 in cen[n][0])
    ok_c = all(games[(n, "BW")][s] <= min(games[(n, g)][s] for g in ("B", "W") if (n, g) in games
                                           and s in games[(n, g)])
               for n in words if (n, "BW") in games for s in games[(n, "BW")]
               if all(s in games[(n, g)] for g in ("B", "W") if (n, g) in games))
    report("WD0a the census reproduces records.c's R(d) for 01 at depths 3 .. 33", ok_a)
    report("WD0b the wall's black-alone game equals s + R_w(s + 1) from the census, every word", ok_b)
    report("WD0c both never outlasts either game alone", ok_c)
    report("WD0d w = 1: R_1(d) = d mod 2 (vertical stripes)", ok_d)

    lam, resid = {}, {}
    for n in two + ["random"]:
        R, D = cen[n]
        top = max(D)
        p = len(words[n]) if n != "random" else 8
        nf = sum(1 for k in range(top - p + 1, top + 1) if words[n][(k - 1) % len(words[n])] == 0)
        lam[n] = (D[top] / D[top - p]) ** (1 / max(nf, 1))
        ds = [d for d in R if d >= 15]
        resid[n] = statistics.fmean(R[d] - (math.log2(D[d]) + 0.33) / beta[n] for d in ds)
    print("   lambda per free bit: " + ", ".join(f"{n}: {v:.3f}" for n, v in lam.items()))
    print("   mean residual R - (log2 D + 0.33) / beta: " + ", ".join(f"{n}: {v:+.2f}" for n, v in resid.items()))
    verdict("WD1 lambda between 1.6 and 1.9 for every two-colour word", all(1.6 <= lam[n] <= 1.9 for n in two))
    verdict("WD2 the coin law over distinct walks, mean residual within 4", all(abs(resid[n]) <= 4 for n in two))

    common = {}
    for n in two:
        ss = [s for s in games[(n, "BW")] if all(s in games[(n, g)] for g in ("B", "W"))]
        if ss:
            s = max(ss)
            common[n] = (s, games[(n, "B")][s], games[(n, "W")][s], games[(n, "BW")][s])
    print("   at the largest common s (s, T_B, T_W, T_BW): " + ", ".join(f"{n}: {v}" for n, v in common.items()))
    verdict("WD3 both binds (T_BW <= min - 2) for at least 4 of 6 words",
            sum(1 for v in common.values() if v[3] <= min(v[1], v[2]) - 2) >= 4)
    sl_w, sl_bw = {}, {}
    for n in words:
        if (n, "W") in games and len(games[(n, "W")]) >= 4:
            v = games[(n, "W")]
            ss = [s for s in v if s >= 4]
            sl_w[n] = slope(ss, [v[s] for s in ss])
        if (n, "BW") in games and len(games[(n, "BW")]) >= 4:
            v = games[(n, "BW")]
            ss = [s for s in v if s >= 4]
            sl_bw[n] = slope(ss, [v[s] for s in ss])
    coin_w = {n: 1 + 0.82 * (1 + beta[n]) / (1 - beta[n]) for n in sl_w}
    print("   white-alone slopes (measured / coin): "
          + ", ".join(f"{n}: {sl_w[n]:.2f} / {coin_w[n]:.2f}" for n in sl_w))
    print("   both slopes: " + ", ".join(f"{n}: {v:.2f}" for n, v in sl_bw.items()))
    verdict("WD4 white alone grows linearly, slope within 35% of the coin value",
            all(abs(sl_w[n] / coin_w[n] - 1) <= 0.35 for n in sl_w))
    verdict("WD5 both grows with slope between 1.0 and 2.0 for every word",
            all(1.0 <= v <= 2.0 for v in sl_bw.values()))
    verdict("WD6 the random wall obeys WD1 and WD2", 1.6 <= lam["random"] <= 1.9 and abs(resid["random"]) <= 4,
            f"lambda {lam['random']:.3f}, residual {resid['random']:+.2f}")
    print(f"\n{'ALL CHECKS PASS' if FAILS == 0 else f'{FAILS} FAILURE(S)'}")
    sys.exit(1 if FAILS else 0)


if __name__ == "__main__":
    main()
