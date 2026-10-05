#!/usr/bin/env python3
"""rule30_debt.py: the bounded-debt statement at total widths beyond 100 (RULE30-PRIZE.md section 8.53).

RUN-ON:     cpu (Python 3 and a C compiler; forced.c and count_j.c; exact)
COMMAND:    python3 tests/probes/lexicon/rule30_debt.py [BMAX=24] [D=100] [alpha]
COST:       a few minutes on one core.

Background (sections 8.51, 8.52). N_{w,j}(T) counts configurations of hull width w whose column 0, at distance j
from the hull's left end, reads 0101... for T steps. By left-permutivity the seed's left part is then the forced
left half's first j - 1 cells (one way only), and for T >= j + 1 the configuration survives exactly when the forced
left half F of its right part (b = w - j - 1 cells) has F_{-j} = 1 and zeros at depths j + 1 .. T - 1. So the count
past the left part is a count of right parts: N_{w,j}(T) = #{right parts and phases : F_{-j} = 1, and the zero run
after depth j has length L >= T - 1 - j}. This is the instrument of section 8.42 (cut the forced left half), counted
instead of maximised. It needs only 2^(b-1) right parts, so the debt can be measured at depths j to D = 100, total
widths beyond 100. Write N_{b,j}(tau) for the number with L >= tau. Its step ratio N(tau+1)/N(tau) is what the
right part pays at depth j + tau + 1.

PREDICTIONS, written 2026-10-05 before this script's first run (word 0101..., both phases):
  DB0 (control, must hold): forced.c reproduces count_j.c's N_{w,j}(T) exactly, for every w up to 16, every j, and
      every T from j + 1 to 30.
  DB1 (blind): over every b up to BMAX and every j up to D - 20, free steps (ratio >= 0.95, counts >= 256) never
      come more than 3 in a row.
  DB2 (blind; the debt constant): for alpha = 0.5, c_b = max over j <= D - 20, tau and k (with N(tau + k) >= 1) of
      log2(N(tau + k) / N(tau)) + 0.5 k is at most 8 for every b up to BMAX.
  DB3 (blind): the pooled cost per condition, -log2(sum N(tau + 1) / sum N(tau)) over counts >= 256, lies between
      0.9 and 1.3 bits for each b from BMAX - 4 to BMAX.
  DB4 (blind; depth does not help the adversary): for b = BMAX the pooled cost over depths j >= 50 is within 0.2
      bits of the pooled cost over j < 50.
REFUTED-BY: DB0 failing (the instrument); DB1 to DB4 failing.

OUTCOME, 2026-10-05 (the first run, 32 seconds, b = 0 .. 24, depths to 100):
  DB0 PASSED: forced.c reproduces count_j.c exactly. The count past the left part is a count of right parts.
  DB1 REFUTED: free steps come up to 5 in a row (from b = 15 on; 3 at b = 12 .. 14). The longest run is 5 at every b
     from 15 to 24: still bounded, at a larger value than at the shallow depths of section 8.52.
  DB2 HELD: c_b for alpha = 0.5 is at most 5.00 (b = 6, 7), and 4.08 to 4.22 for every b from 9 to 24. It does not
     grow with b, at total widths beyond 100.
  DB3 HELD: the pooled cost is 1.001 to 1.004 bits per condition for every b from 11 to 24 (0.94 at b = 9).
  DB4 HELD: 1.003 bits at depths 50 and beyond, 1.001 before.

MODE alpha. The debt constant at rates nearer the true one, and a random-chaos control.
PREDICTIONS for alpha, written 2026-10-05 after the outcome above and before alpha's first run:
  DA1 (blind): for alpha = 0.9, c_b <= 10 for every b up to BMAX, and c_BMAX - c_12 <= 2.
  DA2 (blind): for alpha = 1.0, c_BMAX - c_12 >= 2 (at the true rate, luck accumulates).
  DA3 (random-chaos): a random word (seed 1940) has c_20 for alpha = 0.9 within 2 of 0101's.
"""
import math, pathlib, subprocess, sys, tempfile

HERE = pathlib.Path(__file__).resolve().parent
BMAX = int(sys.argv[1]) if len(sys.argv) > 1 else 24
D = int(sys.argv[2]) if len(sys.argv) > 2 else 100
FAILS = 0
W01 = "01" * 200


def report(name, ok, detail=""):
    global FAILS
    FAILS += not ok
    print(f"{'PASS' if ok else 'FAIL'}  {name}" + (f"  ({detail})" if detail else ""), flush=True)


def verdict(name, held, detail=""):
    print(f"{'HELD' if held else 'REFUTED'}  prediction {name}" + (f"  ({detail})" if detail else ""), flush=True)


def build(name, src):
    exe = pathlib.Path(tempfile.gettempdir()) / name
    subprocess.run(["cc", "-O2", "-o", str(exe), str(HERE / src)], check=True)
    return exe


def forced(exe, bmin, bmax, depth):
    out = subprocess.run([str(exe), str(bmin), str(bmax), str(depth), W01, "2"], check=True,
                         capture_output=True, text=True).stdout
    H = {}
    for line in out.split("\n"):
        f = line.split()
        if f and f[0] == "H":
            H.setdefault((int(f[1]), int(f[2])), {})[int(f[3])] = int(f[4])
    return H


def tail(hist, depth_left):
    """N(tau) = number with L >= tau, for tau = 0 .. depth_left - 1 (beyond that the runs are censored)."""
    return [sum(c for L, c in hist.items() if L >= tau) for tau in range(depth_left)]


def cvals(H, alphas, bmax):
    c = {a: {} for a in alphas}
    for (b, j), hist in H.items():
        if j > D - 20 or b > bmax:
            continue
        N = tail(hist, D - j)
        for tau in range(len(N)):
            if N[tau] < 1:
                break
            for k in range(1, len(N) - tau):
                if N[tau + k] < 1:
                    break
                r = math.log2(N[tau + k] / N[tau])
                for a in alphas:
                    c[a][b] = max(c[a].get(b, -99.0), r + a * k)
    return c


def alpha_mode():
    import random
    fexe = build("rule30_debt_forced", "forced.c")
    H = forced(fexe, 0, BMAX, D)
    c = cvals(H, (0.5, 0.8, 0.9, 1.0), BMAX)
    for a in (0.5, 0.8, 0.9, 1.0):
        print(f"   alpha {a}: c_b for b = 8 .. {BMAX}: " + " ".join(f"{c[a][b]:.1f}" for b in range(8, BMAX + 1)))
    verdict("DA1 alpha 0.9: c_b <= 10 for every b, and c_BMAX - c_12 <= 2",
            all(v <= 10 for v in c[0.9].values()) and c[0.9][BMAX] - c[0.9][12] <= 2,
            f"largest {max(c[0.9].values()):.2f}; c_BMAX - c_12 = {c[0.9][BMAX] - c[0.9][12]:.2f}")
    verdict("DA2 alpha 1.0: c_BMAX - c_12 >= 2", c[1.0][BMAX] - c[1.0][12] >= 2,
            f"{c[1.0][BMAX] - c[1.0][12]:.2f}")
    rnd = random.Random(1940)
    wr = "".join(rnd.choice("01") for _ in range(400))
    out = subprocess.run([str(fexe), "20", "20", str(D), wr, "1"], check=True, capture_output=True, text=True).stdout
    Hr = {}
    for line in out.split("\n"):
        f = line.split()
        if f and f[0] == "H":
            Hr.setdefault((int(f[1]), int(f[2])), {})[int(f[3])] = int(f[4])
    cr = cvals(Hr, (0.9,), 20)
    verdict("DA3 the random word's c_20 (alpha 0.9) within 2 of 0101's", abs(cr[0.9][20] - c[0.9][20]) <= 2,
            f"{cr[0.9][20]:.2f} against {c[0.9][20]:.2f}")


def main():
    if len(sys.argv) > 3 and sys.argv[3] == "alpha":
        alpha_mode()
        return
    fexe, jexe = build("rule30_debt_forced", "forced.c"), build("rule30_debt_countj", "count_j.c")
    out = subprocess.run([str(jexe), "1", "16", "31", W01, "2"], check=True, capture_output=True, text=True).stdout
    J = {}
    for line in out.split("\n"):
        f = line.split()
        if f and f[0] == "J":
            J[(int(f[1]), int(f[2]), int(f[3]))] = int(f[4])
    H = forced(fexe, 0, 15, 40)
    ok = True
    for w in range(1, 17):
        for j in range(w):
            b = w - j - 1
            hist = H.get((b, j), {})
            for T in range(j + 1, 31):
                mine = sum(c for L, c in hist.items() if L >= T - 1 - j)
                ok &= mine == J.get((w, j, T), 0)
    report("DB0 forced.c reproduces count_j.c for w <= 16, T = j + 1 .. 30", ok)
    H = forced(fexe, 0, BMAX, D)
    longest, cmax, pooled, pooled_lo, pooled_hi = {}, {}, {}, [0, 0], [0, 0]
    for (b, j), hist in sorted(H.items()):
        if j > D - 20:
            continue
        N = tail(hist, D - j)
        run = 0
        for tau in range(len(N) - 1):
            if N[tau] >= 256 and N[tau + 1] / N[tau] >= 0.95:
                run += 1
                longest[b] = max(longest.get(b, 0), run)
            else:
                run = 0
            if N[tau] >= 256:
                pooled.setdefault(b, [0, 0])
                pooled[b][0] += N[tau + 1]
                pooled[b][1] += N[tau]
                if b == BMAX:
                    tgt = pooled_hi if j >= 50 else pooled_lo
                    tgt[0] += N[tau + 1]
                    tgt[1] += N[tau]
            if N[tau] >= 1:
                for k in range(1, len(N) - tau):
                    if N[tau + k] < 1:
                        break
                    cmax[b] = max(cmax.get(b, -99.0), math.log2(N[tau + k] / N[tau]) + 0.5 * k)
    cost = {b: -math.log2(p[0] / p[1]) for b, p in pooled.items() if p[1]}
    print("   longest free run by b: " + ", ".join(f"{b}: {longest.get(b, 0)}" for b in range(BMAX + 1)))
    print("   c_b (alpha 0.5) by b: " + ", ".join(f"{b}: {cmax[b]:.2f}" for b in sorted(cmax)))
    print("   pooled cost per condition by b: " + ", ".join(f"{b}: {cost[b]:.3f}" for b in sorted(cost)))
    verdict("DB1 at most 3 free steps in a row, every b and j", all(v <= 3 for v in longest.values()),
            f"largest {max(longest.values()) if longest else 0}")
    verdict("DB2 c_b <= 8 for every b", all(v <= 8 for v in cmax.values()), f"largest {max(cmax.values()):.2f}")
    verdict("DB3 pooled cost 0.9 to 1.3 bits for b = BMAX - 4 .. BMAX",
            all(0.9 <= cost[b] <= 1.3 for b in range(BMAX - 4, BMAX + 1)),
            ", ".join(f"{b}: {cost[b]:.3f}" for b in range(BMAX - 4, BMAX + 1)))
    lo, hi = -math.log2(pooled_lo[0] / pooled_lo[1]), -math.log2(pooled_hi[0] / pooled_hi[1])
    verdict("DB4 cost at depths >= 50 within 0.2 bits of depths < 50 (b = BMAX)", abs(hi - lo) <= 0.2,
            f"{hi:.3f} against {lo:.3f}")
    print(f"\n{'ALL CHECKS PASS' if FAILS == 0 else f'{FAILS} FAILURE(S)'}")
    sys.exit(1 if FAILS else 0)


if __name__ == "__main__":
    main()
