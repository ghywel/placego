#!/usr/bin/env python3
"""collatz_count.py: Rule 30's counting form, carried to Collatz (PRIZE-PROBLEMS.md section 7.1).

RUN-ON:     cpu (Python 3 and a C compiler; collatz.c counts; exact)
COMMAND:    python3 tests/probes/prizes/collatz_count.py [WMAX=30]
COST:       under a minute on one core.

Background. RULE30-PRIZE.md sections 8.51 to 8.53 counted the seeds that keep the wall's conditions for T steps.
The seed's left part pays one bit per condition exactly, by permutivity; the right part pays about a bit on average,
with a debt that does not grow. Collatz has the same skeleton. With T(n) = n/2 or (3n + 1)/2, Terras's theorem says
the first k parity steps of n are in bijection with n mod 2^k: the free bits pay exactly. S_w(T) is the number of
w-bit numbers (2^(w-1) <= n < 2^w) whose orbit stays at or above n for T steps, that is, whose stopping time
exceeds T. C_w(T) is the same for Terras's coefficient stopping time (the first t with 3^(a_t) < 2^t). V(T) is the
number of parity vectors of length T whose coefficients stay above 1, and P(T) = V(T) / 2^T is the coin's survival.
If S_w(T) <= 2^(w - alpha T + c), every stopping time is finite and the conjecture follows. While T < w, the count is
exact by Terras; beyond, it is the open part, as on Rule 30's right part.

PREDICTIONS, written 2026-10-05 before this script's first run (w = 16 .. WMAX):
  CZ0 (control, must hold): C_w(T) = 2^(w - 1 - T) V(T) exactly for every T <= w - 1 (Terras's bijection), at every w.
  CZ1 (blind): S_w(T) = C_w(T) for every T, at every w from 20 to WMAX (no number of 20 bits or more has a stopping
      time different from its coefficient stopping time; Terras's coefficient conjecture, here).
  CZ2 (blind; the horizon): the largest stopping time H_w grows with w at between 8 and 20 steps per bit (least
      squares over w = 16 .. WMAX).
  CZ3 (blind; the coin's rate past the free bits): at w = WMAX, over T from w to 0.8 H_w, the least-squares slope of
      log2 S_w(T) is within 0.02 bits per step of the slope of log2 P(T) over the same range.
  CZ4 (blind; the debt does not grow): with e_w = max over T >= w and k >= 1 (S_w(T + k) >= 1) of
      log2(S_w(T + k) / S_w(T)) - log2(P(T + k) / P(T)), the excess over the coin, e_w <= 8 at every w, and
      e_WMAX - e_16 <= 2.
REFUTED-BY: CZ0 failing (the instrument); CZ1 to CZ4 failing.

OUTCOME, 2026-10-05 (the first run, 21 seconds, w = 16 .. 30, every number):
  CZ0 PASSED: Terras's bijection, exactly, at every w and T <= w - 1.
  CZ1 HELD: stopping time and coefficient stopping time give the same counts at every T, for every w from 20 to 30.
  CZ2 REFUTED, narrowly: the largest stopping time grows by 21.1 steps per bit (135 at w = 16 to 357 at w = 30, noisy:
     395 at 28). Lagarias and Weiss's stochastic models (Ann. Appl. Probab. 2, 1992) predict growth in proportion to
     log n for the total stopping time (41.68 log n); their constant is for a different quantity and was not
     compared here.
  CZ3 HELD: past the free bits (w = 30, T = 30 .. 285) log2 S_w(T) falls by 0.0637 bits per step, against 0.0640 for
     the coin (the random walk of Terras's parity vectors). The high bits pay the coin's rate, as Rule 30's right
     part pays 1.002 bits per condition.
  CZ4 HELD: the excess over the coin, e_w, is 0.2 to 3.7 and does not grow (1.93 at w = 16, 0.43 at w = 30).

ADDENDUM, WMAX = 32. PREDICTIONS written 2026-10-05 before the run with WMAX = 32:
  CZ5 (blind): at w = 32, the slope of log2 S past the free bits (T from w to 0.8 H_w) is within 0.01 of the coin's.
  CZ6 (blind): e_31 and e_32 are both at most 4.
OUTCOME of the addendum, 2026-10-05 (81 seconds, every number of 16 to 32 bits; the verdicts read from the printed
  slope and e_w lines): CZ5 HELD (w = 32: -0.0610 against the coin's -0.0618, T = 32 .. 357). CZ6 HELD (e_31 = 1.80,
  e_32 = 2.66). H_31 = 433, H_32 = 447. CZ0 to CZ4 as before (CZ2 still refuted, 21.2 steps per bit).
"""
import math, pathlib, subprocess, sys, tempfile

HERE = pathlib.Path(__file__).resolve().parent
WMAX = int(sys.argv[1]) if len(sys.argv) > 1 else 30
CAP = 1500
FAILS = 0
L23 = math.log2(3)


def report(name, ok, detail=""):
    global FAILS
    FAILS += not ok
    print(f"{'PASS' if ok else 'FAIL'}  {name}" + (f"  ({detail})" if detail else ""), flush=True)


def verdict(name, held, detail=""):
    print(f"{'HELD' if held else 'REFUTED'}  prediction {name}" + (f"  ({detail})" if detail else ""), flush=True)


def coin(tmax):
    """V(T) for T = 0 .. tmax: parity vectors whose coefficient 3^a_t / 2^t stays above 1 at every t <= T."""
    V, cur = [1], {0: 1}
    for t in range(1, tmax + 1):
        nxt = {}
        for a, c in cur.items():
            for a2 in (a, a + 1):
                if a2 * L23 > t:
                    nxt[a2] = nxt.get(a2, 0) + c
        cur = nxt
        V.append(sum(cur.values()))
    return V


def slope(xs, ys):
    n = len(xs)
    mx, my = sum(xs) / n, sum(ys) / n
    return sum((x - mx) * (y - my) for x, y in zip(xs, ys)) / sum((x - mx) ** 2 for x in xs)


def main():
    exe = pathlib.Path(tempfile.gettempdir()) / "collatz_count_c"
    subprocess.run(["cc", "-O2", "-o", str(exe), str(HERE / "collatz.c"), "-lm"], check=True)
    V = coin(CAP)
    S, C, H = {}, {}, {}
    for w in range(16, WMAX + 1):
        out = subprocess.run([str(exe), str(w), str(CAP)], check=True, capture_output=True, text=True).stdout
        S[w], C[w] = {}, {}
        for line in out.split("\n"):
            f = line.split()
            if f and f[0] == "S":
                S[w][int(f[1])], C[w][int(f[1])] = int(f[2]), int(f[3])
        H[w] = max(t for t in S[w] if S[w][t] >= 1) + 1 if any(S[w][t] for t in S[w]) else 0
        print(f"   w = {w}: H_w = {H[w]}; log2 S_w(T) at T = w, 2w, 4w: "
              + ", ".join(f"{math.log2(S[w][t]):.1f}" if S[w].get(t, 0) else "-" for t in (w, 2 * w, 4 * w)), flush=True)
    ok0 = all(C[w][T] == V[T] * 2 ** (w - 1 - T) for w in S for T in range(w))
    report("CZ0 the coefficient counts equal 2^(w-1-T) V(T) for T <= w - 1", ok0)
    diff = {w: [t for t in S[w] if S[w][t] != C[w][t]] for w in range(20, WMAX + 1)}
    verdict("CZ1 stopping time = coefficient stopping time, counts equal at every T, w >= 20",
            all(not d for d in diff.values()),
            ", ".join(f"w = {w}: {len(d)} values of T differ, first {d[0]}" for w, d in diff.items() if d) or "all equal")
    ws = sorted(H)
    sl = slope(ws, [H[w] for w in ws])
    print("   H_w: " + " ".join(str(H[w]) for w in ws))
    verdict("CZ2 H_w grows by 8 to 20 steps per bit", 8 <= sl <= 20, f"{sl:.2f}")
    w = WMAX
    Ts = [t for t in range(w, int(0.8 * H[w]) + 1) if S[w].get(t, 0) > 0]
    s_obs = slope(Ts, [math.log2(S[w][t]) for t in Ts])
    s_coin = slope(Ts, [math.log2(V[t]) - t for t in Ts])
    print(f"   w = {w}: slope of log2 S past the free bits {s_obs:.4f}; of log2 P {s_coin:.4f} (T = {Ts[0]} .. {Ts[-1]})")
    verdict("CZ3 the slope past the free bits within 0.02 of the coin's", abs(s_obs - s_coin) <= 0.02,
            f"{s_obs:.4f} against {s_coin:.4f}")
    e = {}
    for w in S:
        best = -99.0
        Tl = [t for t in range(w, CAP) if S[w].get(t, 0) >= 1]
        for i, T in enumerate(Tl):
            for T2 in Tl[i + 1:]:
                v = math.log2(S[w][T2] / S[w][T]) - (math.log2(V[T2]) - T2 - math.log2(V[T]) + T)
                best = max(best, v)
        e[w] = best
    print("   e_w: " + " ".join(f"{e[w]:.2f}" for w in ws))
    verdict("CZ4 e_w <= 8 at every w, and e_WMAX - e_16 <= 2", all(v <= 8 for v in e.values()) and e[WMAX] - e[16] <= 2,
            f"e_16 {e[16]:.2f}, e_{WMAX} {e[WMAX]:.2f}, largest {max(e.values()):.2f}")
    print(f"\n{'ALL CHECKS PASS' if FAILS == 0 else f'{FAILS} FAILURE(S)'}")
    sys.exit(1 if FAILS else 0)


if __name__ == "__main__":
    main()
