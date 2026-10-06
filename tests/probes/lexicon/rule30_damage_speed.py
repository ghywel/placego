#!/usr/bin/env python3
"""rule30_damage_speed.py: CONSTELLATION.md row 3, the leftward light speed. Rule 30's rightward speed of influence is
exactly 1 (the XOR of the left neighbour); leftward it was measured at 0.246 on a random background (section 8.30,
LB5) and never derived. In diagonal coordinates k = x + t the rule reads D_k(t+1) = D_(k-2)(t) xor (D_(k-1)(t) or
D_k(t)) on the whole plane, so a difference between two configurations always flows to higher k (two diagonals up
per step through the XOR) and never to lower k. Its lowest damaged diagonal k_min can only RISE: diagonal k_min
heals at t+1 exactly when the undamaged diagonal below it is black, D_(k_min-1)(t) = 1, and then k_min rises by 1 or
2 (never more: D_(k_min+2) is always damaged). The leftmost damaged cell sits at x = k_min - t, so the left speed is
  v = 1 - (mean rise of k_min per step) = 1 - P(heal) * E[jump | heal],
an exact identity; the content is in the two factors, and P(heal) is the black density of the background's diagonals
as seen from the front. On a structured background the factors can be read off. This probe measures v, P(heal) and
E[jump] on: a random background (the control), the white background (the counterfactual), the checkerboard (a
fixed point of the rule), the single cell's own left band (damage put on a settled diagonal), and the periodic
backgrounds that the cycles of small rings tile. (Local, 2026-10-06; RULE30-PRIZE.md section 8.66.)

RUN-ON:     cpu, one core (numpy)
COMMAND:    python3 tests/probes/lexicon/rule30_damage_speed.py [LOGT=13]
COST:       a minute or two.

SEEN BEFORE these predictions: LB5 (ten random trials, 0.226 to 0.254, mean 0.246); the band's inner edge at 0.245 to
0.257 (section 8.30); the diagonal recurrence (sections 8.30, 8.59); nothing about P(heal) or jumps on any background.

PREDICTIONS, written 2026-10-06 before the first run.
  DS0 (control, must hold): random background, 8 trials: the mean of v is within 0.02 of 0.246.
  DS1 (instrument, must hold): k_min never rises by more than 2 in one step, and the fitted v agrees with
      1 - (mean rise) within 0.01 on every background.
  CF  (counterfactual, must fail): on the white background v is within 0.1 of 0.246. It must be 1 (the flipped cell is
      the single cell, whose left edge moves at light speed; nothing below the front is ever black).
  DS2 (blind): on the checkerboard v is within 0.03 of 1/4: the diagonal below the front alternates, so P(heal) = 1/2
      exactly, and the chaotic content above the front makes the jump 2 about half the time.
  DS3 (blind): on the band (damage on diagonal 64 at t = 4096, tracked for 2^LOGT steps) v is within 0.03 of the
      random background's: the band's diagonals are black about half the time.
  DS4 (blind): across the periodic backgrounds tiled from one cycle state of each ring n = 3 .. 10, the speeds
      spread by more than 0.05 (max - min): the left speed is the background's, not the rule's; and the background of
      highest black density has the lowest speed.
  DS5 (blind, the derivation's test): on the random background P(heal) is within 0.02 of 1/2 and E[jump | heal]
      within 0.05 of 1.5, so 0.754 = 0.5 * 1.5 to that accuracy.
REFUTED-BY: DS0 or DS1 failing (the instrument), CF holding; DS2 to DS5 the other way.
"""
import sys
import numpy as np

LOGT = int(sys.argv[1]) if len(sys.argv) > 1 else 13
T = 1 << LOGT
FAILS = 0


def report(name, ok, detail=""):
    global FAILS
    FAILS += not ok
    print(f"{'PASS' if ok else 'FAIL'}  {name}" + (f"  ({detail})" if detail else ""), flush=True)


def verdict(name, held, detail=""):
    print(f"{'HELD' if held else 'REFUTED'}  prediction {name}" + (f"  ({detail})" if detail else ""), flush=True)


def step(a):
    l = np.roll(a, 1); r = np.roll(a, -1)
    return l ^ (a | r)


def measure(a, b, T):
    """a, b: equal-length uint8 rows differing somewhere. Evolve T steps (periodic boundary, far away); track the
    lowest damaged diagonal k_min(t) = x_min(t) + t. Returns v (least squares over t in [T/4, T]), P(heal), E[jump],
    max jump, and the black density of the diagonal below the front at the steps it was checked."""
    kmin, heals, jumps, below = [], 0, [], 0
    for t in range(T + 1):
        d = a != b
        x = int(np.argmax(d))
        if not d[x]:
            raise RuntimeError("damage vanished")
        kmin.append(x + t)
        if t:
            j = kmin[-1] - kmin[-2]
            if j:
                heals += 1; jumps.append(j)
        if t == T:
            break
        a, b = step(a), step(b)
    ks = np.array(kmin, dtype=float); ts = np.arange(T + 1, dtype=float)
    lo = T // 4
    slope = np.polyfit(ts[lo:], ks[lo:], 1)[0]
    rise = (kmin[-1] - kmin[lo]) / (T - lo)
    ph = heals / T; ej = float(np.mean(jumps)) if jumps else 0.0
    return dict(v=1 - slope, v_inc=1 - rise, pheal=ph, ejump=ej, maxjump=max(jumps) if jumps else 0)


def random_bg(width, rng):
    a = rng.integers(0, 2, width, dtype=np.uint8)
    b = a.copy(); b[width // 2] ^= 1
    return a, b


def tiled(pattern, width):
    p = np.array(pattern, dtype=np.uint8)
    a = np.tile(p, width // len(p) + 1)[:width]
    b = a.copy(); b[width // 2] ^= 1
    return a, b


def ring_cycle_state(n):
    """one state on the longest cycle of Rule 30 on the ring of n cells (None if only the white fixed point)."""
    best = None
    seen = set()
    for s in range(1, 1 << n):
        if s in seen:
            continue
        orbit, x = [], s
        while x not in seen and x not in orbit:
            orbit.append(x)
            cells = np.array([(x >> i) & 1 for i in range(n)], dtype=np.uint8)
            y = step(cells)
            x = int(sum(int(v) << i for i, v in enumerate(y)))
        if x in orbit:
            cyc = orbit[orbit.index(x):]
            if x != 0 and (best is None or len(cyc) > len(best)):
                best = cyc
        seen.update(orbit)
    if best is None:
        return None
    s = best[0]
    return [(s >> i) & 1 for i in range(n)]


def band_bg(T):
    """the single cell to t0 = 4096, then one flipped cell on diagonal 64 (x = -t0 + 64)."""
    t0 = 4096
    width = 2 * (t0 + T) + 64
    a = np.zeros(width, dtype=np.uint8); a[width // 2] = 1
    for _ in range(t0):
        a = step(a)
    b = a.copy(); b[width // 2 - t0 + 64] ^= 1
    return a, b


def main():
    rng = np.random.default_rng(20261006)
    width = 4 * T + 2
    res = {}
    vs = []
    for i in range(8):
        r = measure(*random_bg(width, rng), T); vs.append(r["v"]); res[f"random{i}"] = r
    print("   random: v = " + ", ".join(f"{v:.4f}" for v in vs) + f"  mean {np.mean(vs):.4f}", flush=True)
    r0 = res["random0"]
    ph = np.mean([res[f"random{i}"]["pheal"] for i in range(8)]); ej = np.mean([res[f"random{i}"]["ejump"] for i in range(8)])
    res["white"] = measure(*tiled([0], width), T)
    res["checker"] = measure(*tiled([0, 1], width), T)
    res["band"] = measure(*band_bg(T), T)
    rings = {}
    for n in range(3, 11):
        st = ring_cycle_state(n)
        if st is None:
            continue
        rings[n] = measure(*tiled(st, width - width % n), T)
        rings[n]["density"] = sum(st) / n; rings[n]["state"] = "".join(map(str, st))
    for k in ("white", "checker", "band"):
        r = res[k]
        print(f"   {k}: v {r['v']:.4f} (inc {r['v_inc']:.4f})  P(heal) {r['pheal']:.4f}  E[jump] {r['ejump']:.3f}  max {r['maxjump']}", flush=True)
    for n, r in rings.items():
        print(f"   ring {n} {r['state']} (density {r['density']:.3f}): v {r['v']:.4f}  P(heal) {r['pheal']:.4f}  E[jump] {r['ejump']:.3f}", flush=True)
    report("DS0 random background: mean v within 0.02 of 0.246", abs(np.mean(vs) - 0.246) <= 0.02, f"{np.mean(vs):.4f}")
    allr = list(res.values()) + list(rings.values())
    report("DS1 no jump above 2; fitted v agrees with 1 - mean rise within 0.01 everywhere",
           all(r["maxjump"] <= 2 for r in allr) and all(abs(r["v"] - r["v_inc"]) <= 0.01 for r in allr),
           f"max jump {max(r['maxjump'] for r in allr)}, worst gap {max(abs(r['v'] - r['v_inc']) for r in allr):.4f}")
    report("CF  white background: v is NOT within 0.1 of 0.246 (it is 1)", abs(res["white"]["v"] - 0.246) > 0.1, f"{res['white']['v']:.4f}")
    verdict("DS2 checkerboard: v within 0.03 of 1/4", abs(res["checker"]["v"] - 0.25) <= 0.03,
            f"v {res['checker']['v']:.4f}, P(heal) {res['checker']['pheal']:.4f}, E[jump] {res['checker']['ejump']:.3f}")
    verdict("DS3 band: v within 0.03 of the random background's", abs(res["band"]["v"] - np.mean(vs)) <= 0.03,
            f"band {res['band']['v']:.4f} vs {np.mean(vs):.4f}")
    if rings:
        spread = max(r["v"] for r in rings.values()) - min(r["v"] for r in rings.values())
        dens = max(rings.values(), key=lambda r: r["density"]); slow = min(rings.values(), key=lambda r: r["v"])
        verdict("DS4 periodic backgrounds: speeds spread by more than 0.05, and the densest is the slowest",
                spread > 0.05 and dens is slow, f"spread {spread:.4f}; densest ring v {dens['v']:.4f}, slowest v {slow['v']:.4f}")
    verdict("DS5 random background: P(heal) within 0.02 of 1/2 and E[jump] within 0.05 of 1.5",
            abs(ph - 0.5) <= 0.02 and abs(ej - 1.5) <= 0.05, f"P(heal) {ph:.4f}, E[jump] {ej:.4f}, product {ph * ej:.4f}")
    print("\nALL CHECKS PASS" if FAILS == 0 else f"\n{FAILS} CHECK(S) FAILED")


if __name__ == "__main__":
    main()
