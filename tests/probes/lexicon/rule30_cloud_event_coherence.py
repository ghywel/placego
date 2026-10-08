#!/usr/bin/env python3
"""rule30_cloud_event_coherence.py: EC, why Rule 30's edge events draw sharper lines than random ones (row Q6)

RUN-ON:     cpu (Python 3 standard library)
COMMAND:    python3 tests/probes/lexicon/rule30_cloud_event_coherence.py [TRIALS=400] [SEED=8080]
COST:       under a minute.

The owner's observation on the Sieve (2026-10-08): in Rule 30 mode and in random-photons mode the triangles are both
well defined, but Rule 30's dots sit on a straight "edge line" while random photons straddle it, some dots to the
left and some to the right. The Sieve draws time across and depth down, with the edge event
    E_k(t) = y_(k-2)(t) AND NOT y_(k-1)(t),   y_m = column(-m) of the wall form (column 0 the clock, y_(-1) column 1),
as a dot at depth k. Random photons keep depth 1 and draw the deeper events as independent coins at Rule 30's rate.
Three exact local rules (Cloud, by hand; each uses only Rule 30's update at positions <= 0, which the wall form's
sideways definition guarantees):
  (A) straight down: E_k(t) = 1 forces y_(k-1)(t) = 0, so E_(k+1)(t) = y_(k-1)(t) AND ... = 0.
  (B) down-left: if E_(k+1)(t-1) = 1 then y_(k-1)(t-1) = 1 and y_k(t-1) = 0, so the update at -(k-1) gives
      y_(k-1)(t) = 0 XOR (1 OR y_(k-2)(t-1)) = 1, and E_k(t) = 0. A black cell with a white left neighbour stays black.
  (C) along the row: if E_k(t) = 1 then y_(k-2)(t+1) = 0 XOR (1 OR .) = 1 and y_(k-1)(t+1) = y_k(t) XOR 1, so
      E_k(t+1) = y_k(t). An event continues along its row exactly when the cell under it is black. A row of n events
      is therefore n - 1 dots on black cells closed by one dot on a white cell.
  (D) down-right is GPT's GC592 (G240, awaiting reading): r + 1 events along that diagonal need one black and then
      2r + 1 white cells outward in the starting row. One more event costs two more white cells.
Under a fair-coin row these give continuation rates 0, 0, 1/2 and 1/4 against random photons' constant rate. Rules
A and B are the two edge directions of every red set R(k, t) (its vertical edge i = 0 and its slanted edge
i = k - j), so neither edge of a red set ever holds two adjacent events: at most ceil(k / 2) of its k cells.
That strengthens CL054's proved half ("no edge of a red set is ever full").
Disclosure: this probe follows a post-hoc measurement on 40 right halves (row 0.52, down-right 0.24, straight down
and down-left 0.00, random photons 0.25 in every direction) and one ASCII picture of a wheel-locked half. The
predictions below are for a fresh sample (a different seed and ten times as many halves) and for statistics not yet
measured.
Controls (should PASS):
  EC-C1: rules A, B and C hold at every cell of every Rule 30 half; D's r = 1 case (four cells 1000) holds both ways.
  EC-C2: the same counters find violations of A and B in random-photons mode, so they can fail.
PREDICTIONS (Cloud's, pushed before the first run; 400 halves, K = 120, T = 240, W0 = 24, depths 2 .. K):
  EC-P1: the row continuation rate lies in [0.48, 0.56]. Confidence 0.8.
  EC-P2: the down-right continuation rate lies in [0.21, 0.27]. Confidence 0.8.
  EC-P3: random photons' continuation rate is within 0.02 of their event rate in all four directions. Confidence 0.9.
UNEXPECTED CHECK (not yet measured): two rows down, P(E_(k+2)(t) | E_k(t)) is above 0.30, so event rows stack on
  alternate depths, as the one ASCII picture suggests. Under a fair coin it would be 1/4: the cells are disjoint.
  Confidence 0.55.
Counterfactual: if two rows down is near 1/4, the stacked look of the ASCII picture is the wheel lock or the eye, and
  the sharpness the owner sees comes from rules A to C alone.

OUTCOME, 2026-10-08 (by 20:47 BST; seed 8080, 400 halves, 4 s): EC-C1 and EC-C2 PASS. Rules A, B and C and GC592's
  r = 1 case hold at every cell; random photons break A and B 569,337 and 569,449 times, so the counters can fail.
  Event rates: Rule 30 0.2592, random photons 0.2593. Continuation, Rule 30 | random photons: row 0.5375 | 0.2596,
  down-right 0.2418 | 0.2590, straight down 0 | 0.2592, down-left 0 | 0.2592, two down 0.2897 | 0.2595. EC-P1,
  EC-P2 and EC-P3 HELD. The unexpected check was REFUTED: two rows down is 0.29, above a coin's 1/4 and random
  photons' 0.26, but not above 0.30. So the stacking is weak, and the counterfactual mostly holds: the sharp lines
  come from rules A to C.
  Not predicted: row runs of events are close to geometric (P(longer | at least n) = 0.52 to 0.62 for n = 1 .. 6),
  then fall off a cliff after length 8 (0.063). Post-hoc, the cliff is not the wheel lock: it appears both in the 32
  halves that sit on the wheel for t = 100 .. 211 and in the other 368. Runs of length 8 or more concentrate at
  depths 3, 34, 65 and 96 (7097, 2355, 1239, 480). Depth 3 is explained by the record's identity E3 = 1 - c (G240,
  CL048): E_3(t) is NOT column 1 at the even time at or after t (checked at every cell, post-hoc), so a row run at
  depth 3 is twice a white run of column 1's even-time samples. The longest such run in this sample is 4, hence 8.
  The spacing 31 between the other depths is unexplained.
"""
import random
import sys

TRIALS = int(sys.argv[1]) if len(sys.argv) > 1 else 400
SEED = int(sys.argv[2]) if len(sys.argv) > 2 else 8080
K, T, W0 = 120, 240, 24
DIRS = {"row (0, +1)": (0, 1), "down-right (+1, +1)": (1, 1), "straight down (+1, 0)": (1, 0),
        "down-left (+1, -1)": (1, -1), "two down (+2, 0)": (2, 0)}


def column1(rng):
    """Column 1 for t = 0 .. T + 1 of a random right half of W0 cells (the last black) next to the 0101 wall."""
    n = W0 + T + 8
    cur, nxt = [0] * n, [0] * n
    for i in range(1, W0 + 1):
        cur[i] = rng.getrandbits(1)
    cur[W0] = 1
    out = []
    for t in range(T + 2):
        out.append(cur[1])
        cur[0] = t % 2
        for j in range(1, min(W0 + t + 2, n - 2) + 1):
            nxt[j] = cur[j - 1] ^ (cur[j] | cur[j + 1])
        nxt[0] = (t + 1) % 2
        cur, nxt = nxt, cur
    return sum(b << t for t, b in enumerate(out))


def half(c1, rng=None, rate=None):
    """Columns y_m as bitsets (bit t = time t) and events E_k; with rng, events below depth 1 are coins."""
    y = {-1: c1, 0: sum((t % 2) << t for t in range(T + 2))}
    n = {-1: T + 2, 0: T + 2}
    E = {}
    for k in range(1, K + 1):
        n[k] = T - k + 1
        mask = (1 << n[k]) - 1
        if rng is not None and k > 1:
            e = sum(1 << s for s in range(n[k]) if rng.random() < rate)
        else:
            e = y[k - 2] & ~y[k - 1] & mask
        E[k] = e
        a = y[k - 1]
        y[k] = ((a >> 1) ^ a ^ e) & mask
    return y, n, E


def pairs(E, n, dk, dt):
    """(events whose neighbour (k + dk, t + dt) is defined, of which the neighbour is also an event)."""
    have = both = 0
    for k in range(2, K + 1 - dk):
        m = n[k + dk]
        lo, hi = max(0, -dt), min(n[k], m - dt)       # t with 0 <= t < n_k and 0 <= t + dt < n_(k + dk)
        if hi <= lo:
            continue
        mask = ((1 << hi) - 1) & ~((1 << lo) - 1)
        nb = E[k + dk] >> dt if dt >= 0 else E[k + dk] << -dt
        have += bin(E[k] & mask).count("1")
        both += bin(E[k] & nb & mask).count("1")
    return have, both


def main():
    rng = random.Random(SEED)
    halves = [column1(rng) for _ in range(TRIALS)]
    c1_ok = True
    stats = {"r30": {d: [0, 0] for d in DIRS}, "rand": {d: [0, 0] for d in DIRS}}
    ev = {"r30": [0, 0], "rand": [0, 0]}
    runs = {}
    viol = {"A": 0, "B": 0}
    rate = None
    for mode in ("r30", "rand"):
        prng = random.Random(SEED + 1)
        for c1 in halves:
            y, n, E = half(c1) if mode == "r30" else half(c1, prng, rate)
            for k in range(2, K + 1):
                ev[mode][0] += bin(E[k]).count("1")
                ev[mode][1] += n[k]
            for d, (dk, dt) in DIRS.items():
                h, b = pairs(E, n, dk, dt)
                stats[mode][d][0] += h
                stats[mode][d][1] += b
            if mode == "rand":
                viol["A"] += pairs(E, n, 1, 0)[1]
                viol["B"] += pairs(E, n, 1, -1)[1]
                continue
            for k in range(2, K):
                m1 = (1 << (n[k] - 1)) - 1                  # times t with t + 1 defined at depth k
                c1_ok &= (E[k] & E[k + 1]) == 0                                                         # A
                c1_ok &= (E[k] & m1 & ((E[k] >> 1) ^ y[k])) == 0                                        # C
                c1_ok &= (E[k + 1] & (E[k] >> 1)) == 0                                                  # B
                m4 = (1 << (n[k + 1] - 1)) - 1                                                           # D, r = 1
                two = E[k] & (E[k + 1] >> 1) & m4
                want = y[k - 2] & ~y[k - 1] & ~y[k] & ~y[k + 1] & m4
                c1_ok &= two == want
            for k in range(2, K + 1):
                for r in bin(E[k])[2:].split("0"):
                    if r:
                        runs[len(r)] = runs.get(len(r), 0) + 1
        if mode == "r30":
            rate = ev["r30"][0] / ev["r30"][1]
    print("EC-C1", "PASS" if c1_ok else "FAIL", f"({TRIALS} right halves, depths 2 .. {K})")
    print("EC-C2", "PASS" if viol["A"] and viol["B"] else "FAIL",
          f"(random photons: {viol['A']} straight-down and {viol['B']} down-left adjacent pairs)")
    rr = ev["rand"][0] / ev["rand"][1]
    print(f"event rate: Rule 30 {rate:.4f}, random photons {rr:.4f}")
    print("continuation P(neighbour is an event | event), Rule 30 | random photons:")
    cont = {}
    for d in DIRS:
        a = stats["r30"][d][1] / stats["r30"][d][0]
        b = stats["rand"][d][1] / stats["rand"][d][0]
        cont[d] = (a, b)
        print(f"  {d:<22} {a:.4f} | {b:.4f}   ({stats['r30'][d][0]} and {stats['rand'][d][0]} events)")
    tot = sum(runs.values())
    print("Rule 30 row runs of events: length, count, P(longer | at least this long)")
    for L in range(1, 11):
        ge = sum(c for k, c in runs.items() if k >= L)
        gt = ge - runs.get(L, 0)
        print(f"  {L:2d}: {runs.get(L, 0):7d}  {gt / ge if ge else float('nan'):.3f}")
    print(f"  ({tot} runs, longest {max(runs)})")
    p1 = 0.48 <= cont["row (0, +1)"][0] <= 0.56
    p2 = 0.21 <= cont["down-right (+1, +1)"][0] <= 0.27
    p3 = all(abs(cont[d][1] - rr) <= 0.02 for d in list(DIRS)[:4])
    print("EC-P1", "HELD" if p1 else "REFUTED")
    print("EC-P2", "HELD" if p2 else "REFUTED")
    print("EC-P3", "HELD" if p3 else "REFUTED")
    print("unexpected check", "HELD" if cont["two down (+2, 0)"][0] > 0.30 else "REFUTED")


if __name__ == "__main__":
    main()
