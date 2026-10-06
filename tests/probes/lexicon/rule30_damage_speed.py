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

OUTCOME of the first run, 2026-10-06 (LOGT = 13, 70 seconds). DS0 PASSED (random: 0.2547, 0.2434, 0.2482, 0.2166,
  0.2414, 0.2580, 0.2601, 0.2517; mean 0.2468). CF PASSED (white: v = 1). DS1 FAILED on its first half and the header
  above is WRONG where it says "never more": the jump reached 5 on the checkerboard, 7 on the band, 10 on a ring
  background. D_(k+2)(t+1) = D_k(t) xor (D_(k+1) or D_(k+2)) propagates the damage two diagonals up only when the OR is
  the same in both copies; where the damage is dense the OR can differ too and cancel the XOR, so a whole stack of
  damaged diagonals can heal at once. The identity v = 1 - mean rise held everywhere (worst gap 0.0087). The blind
  predictions were all REFUTED, each by a mechanism: DS2, the checkerboard gives v = -0.3877: the damage front moves
  RIGHT; healing (every other step, mean jump 2.5) outruns the leftward flow, so a flipped cell's influence on the
  fixed point recedes to the right and the checkerboard closes behind it. DS3, the band gives v = 1.0000 with 175
  heals, all in the first quarter: the damage climbs from diagonal 64 and LOCKS on one diagonal for ever (the lock
  addendum below says which). DS4, the ring backgrounds spread by 1.39, not 0.05, and the densest (ring 10, 0.700) is
  among the fastest (2/3); the speeds are exact rationals where the jump is exactly 2 and the heal is periodic (ring
  4: 1/2, ring 5: 1/3, ring 10: 2/3, the checkerboard as ring 6: -0.3877 again), and ring 8 (11000001) gives v = 1
  with P(heal) = 0.0006: a white diagonal runs through it and the damage locks above it. DS5, on the random
  background P(heal) = 0.4102, not 1/2, and E[jump] = 1.839, not 1.5; the product 0.7545 is 1 - 0.2455. The front
  sits preferentially above white cells because it heals at black ones, a selection effect, and the jumps are longer
  than 2 for the cancellation reason above. So 0.246 = 1 - 0.410 x 1.839 to the accuracy of the run, and neither
  factor is the background's density: the first is the density of the diagonal below the front AS THE FRONT SEES IT.

LOCK ADDENDUM, written 2026-10-06 before the second run (python3 rule30_damage_speed.py 13 lock). The band's damage
  locked on one diagonal. Healing needs a black cell on the diagonal below the front, and the band has eventually
  WHITE diagonals (2, 7, 28, 399, 87,866: section 8.31). Above an eventually white diagonal w, damage can never heal:
  D_(w+1)(t+1) = D_(w-1)(t) xor D_(w+1)(t) once D_w is white, so a difference on w + 1 is permanent (and constant).
  The 175 heals from diagonal 64 with mean jump 1.92 climb about 336: to 400.
  DL1 (must hold if this is the mechanism): a flip on diagonal 64 at t = 4096 locks on diagonal 400; flips on 10 and
      20 lock on 29; a flip on 3 locks on 8. (Only the preperiods matter: each of those diagonals is white by t = 4096.)
  DL2 (blind): a flip on diagonal 500 at t = 4096, below no eventually white diagonal until 87,866, does not lock
      within 2^13 steps and climbs at a steady rate: v within 0.1 of the random background's 0.25, because the band's
      period-16 diagonals are black about as often as random ones as the front sees them.
  REFUTED-BY: DL1 failing (the mechanism is not the eventually white diagonals); DL2 the other way.
  OUTCOME of the second run, 2026-10-06 (lock; 40 seconds): 64 -> 400 (last rise t = 429) and 10 -> 29 (t = 27) as
  predicted; 3 stays on 3 (it is already above the white diagonal 2: my misapplication, the mechanism's prediction
  was 3); 20 did NOT lock: it passed 29 and 399 and climbed to 6,259 at v = 0.2453. DL1 FAILED on those two; the
  mechanism stands with a correction: the lock is probabilistic, since k_min moves by jumps and a front whose next
  damaged diagonal is above w + 1 when it heals at or below w passes the barrier. DL2 HELD: 500 climbs for the whole
  run at v = 0.2510, the random background's speed.

LOCK-PROBABILITY ADDENDUM, written 2026-10-06 before the third run (python3 rule30_damage_speed.py lockprob). The
  barrier at w + 1 catches the damage only if diagonal w + 1 is damaged when the front heals through w; two of three
  flips were caught. Here: flips on diagonals 3 .. 7 (barrier 8), 8 .. 28 (barrier 29), 30 .. 395 (barrier 400) and
  450 (no barrier until 87,866), at 16 consecutive times from t = 4096, each followed for 2048 steps; "locked" means
  the lowest damaged diagonal did not move in the last 1024 steps and sits at w + 1.
  LP0 (control, must hold): a flip on diagonal 3 is locked on 3 at every phase (it is above the white diagonal 2).
  LP1 (blind): the lock probability at 400, over flips on 30 .. 395 and all phases, is between 0.5 and 0.9.
  LP2 (blind): a flip far below the barrier is caught more often than one just below it, because the damage it
      brings is denser: P(lock at 400 | flip on 30 .. 100) exceeds P(lock at 400 | flip on 350 .. 395) by at least 0.1,
      and the same ordering holds at 29 (flips on 8 .. 15 against 25 .. 28).
  LP3 (blind): every flip that slips past 400 is still climbing at the end, at a speed within 0.05 of 0.25 over
      the last 1024 steps.
  CF  (counterfactual, must fail): flips on 450 lock (the lowest damaged diagonal constant over the last 1024 steps)
      with probability at least 0.5. There is no barrier there; it must be about zero.
  REFUTED-BY: LP0 failing or CF holding (the instrument); LP1 to LP3 the other way. What would change my mind about
  the barriers: a lock probability near 1 (they are nearly absolute) or below 0.3 (they are weak), either of which
  is a fact about how the band's doublings handle information.
  OUTCOME of the third run, 2026-10-06 (lockprob; 75 seconds): LP0, CF PASSED. The lock fractions are EXACT and
  independent of the flip's position: 8/16 at 400 for every flip on 30 .. 395 (LP1 held at its edge, 0.500), 12/16
  locked (at 29 or 400) for every flip on 10 .. 28, 14/16 (at 8, 29 or 400) for every flip on 4 .. 7, 0/16 at 450;
  a flip on 8 is itself locked (8 = 7 + 1), as 3 is. LP2 REFUTED: the damage's density plays no part. LP3 HELD (88
  slipped, 0.209 .. 0.285). Eleven independent 8/16 results are not chance: the lock is decided by the PHASE of the
  band at the flip time, and the fractions 7/8, 6/8, 4/8 at the barriers 8, 29, 400 are fractions of the periods 8,
  8, 16 of the diagonals just above each barrier. The fourth run tests that reading.

PHASE ADDENDUM, written 2026-10-06 before the fourth run (python3 rule30_damage_speed.py lockphase): flips on 4, 6,
  12, 20, 30, 100, 300, 395 at 32 consecutive times from t = 4096 (two periods of 16), recording the end diagonal
  per phase.
  LQ1 (the reading, must hold): for the flips 30, 100, 300, 395 the set of phases (t mod 16) that lock at 400 is one
      set S400 of size 8, the same for all four, and the outcome at t and t + 16 is the same.
  LQ2 (blind): for the flips 12 and 20 the phases that lock at 29 form one set S29 (a union of residues mod 8, 6 of
      the 8), and among the phases that slip past 29 the ones that then lock at 400 are exactly those in S400: the
      barrier decides on the phase alone, not on the history.
  LQ3 (blind): S400 is a single bit of the time: t mod 16 is in S400 iff bit 3 of t is set (or iff it is clear). The
      lock at the period-16 diagonal happens when the flip lands on one half of the odometer's top cycle.
  REFUTED-BY: LQ1 failing (the phase is not the whole story); LQ2, LQ3 the other way.
  OUTCOME of the fourth run, 2026-10-06 (lockphase; 50 seconds). The outcome at t and t + 16 is the same for every
  flip (the lock is a deterministic function of the flip's diagonal and t mod 16), and at EVERY barrier exactly half
  the phases that reach it are caught, whatever came before: at 8 (period 4 above it) 8 of 16, two residues of
  four; at 29 (period 8) 4 of the 8 slippers; at 400 (period 16) 2 of the 4 remaining, and 8 of 16 for every flip
  on 30 .. 395. So 14/16, 12/16, 8/16 are 1 - 1/8, 1 - 1/4, 1 - 1/2: each eventually white diagonal is a fair coin
  for outward damage, tossed on the band's phase. LQ1 FAILED on its first clause: the set of 8 catching phases at
  400 depends on the flip's diagonal (30: 1 3 4 6 7 8 10 13; 100: 1 4 6 7 8 10 11 13; 300 and 395: complementary
  sets), and so does the set at 8 (flips 4 and 6: complementary mod 4), while the set at 29 is the same for the
  flips 12 and 20 (3 4 5 6 mod 8). LQ2 REFUTED (S29 has 8 phases, not 12, and the later barrier does not reuse it);
  LQ3 REFUTED (no single bit). Why exactly half at every barrier is open; the hint is that the diagonal above a
  white one is the running XOR of the one two below (the doubling), so the difference that reaches it is a parity.
"""
import sys
import numpy as np

LOGT = int(next((a for a in sys.argv[1:] if a.isdigit()), 13))
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


def band_flip(diag, T, t0=4096):
    width = 2 * (t0 + T) + 1024
    a = np.zeros(width, dtype=np.uint8); a[width // 2] = 1
    for _ in range(t0):
        a = step(a)
    b = a.copy(); b[width // 2 - t0 + diag] ^= 1
    return a, b, width // 2 - t0


def lock():
    """which diagonal the band's damage locks on, for flips on diagonals 3, 10, 20, 64 and 500 at t = 4096."""
    out = {}
    for diag in (3, 10, 20, 64, 500):
        a, b, off = band_flip(diag, T)
        kmin = []
        for t in range(T + 1):
            d = a != b
            kmin.append(int(np.argmax(d)) + t - off)
            if t < T:
                a, b = step(a), step(b)
        lo = T // 4
        v = 1 - (kmin[-1] - kmin[lo]) / (T - lo)
        last_change = max((t for t in range(1, T + 1) if kmin[t] != kmin[t - 1]), default=0)
        out[diag] = (kmin[-1], v, last_change)
        print(f"   flip on diagonal {diag}: lowest damaged diagonal at the end {kmin[-1]}, last rise at t = {last_change}, v {v:.4f}", flush=True)
    report("DL1 flips on 64 lock on 400, on 10 and 20 lock on 29, on 3 locks on 8",
           out[64][0] == 400 and out[10][0] == 29 and out[20][0] == 29 and out[3][0] == 8)
    verdict("DL2 a flip on 500 does not lock and climbs at v within 0.1 of 0.25",
            out[500][2] > T - T // 8 and abs(out[500][1] - 0.25) <= 0.1, f"v {out[500][1]:.4f}, last rise {out[500][2]}")
    print("\nALL CHECKS PASS" if FAILS == 0 else f"\n{FAILS} CHECK(S) FAILED")


def lockprob(t0=4096, T=2048, phases=16):
    flips = [3, 4, 5, 6, 7, 8, 10, 12, 15, 20, 25, 28, 30, 50, 100, 150, 200, 250, 300, 350, 380, 390, 395, 450]
    barrier = lambda d: 3 if d == 3 else (8 if d <= 7 else (29 if d <= 28 else (400 if d <= 399 else None)))
    width = 2 * (t0 + phases + T) + 1024
    a = np.zeros(width, dtype=np.uint8); a[width // 2] = 1
    for _ in range(t0):
        a = step(a)
    rows = []
    for _ in range(phases):
        rows.append(a.copy()); a = step(a)
    res = {}
    for d in flips:
        locked, speeds, ends = 0, [], []
        for j, r in enumerate(rows):
            off = width // 2 - (t0 + j)
            x, y = r.copy(), r.copy(); y[off + d] ^= 1
            kmin = []
            for s_ in range(T + 1):
                df = x != y
                kmin.append(int(np.argmax(df)) + s_ - off)
                if s_ < T:
                    x, y = step(x), step(y)
            still = kmin[-1] == kmin[T - 1024]
            b = barrier(d)
            if still and (b is None or kmin[-1] == b):
                locked += 1
            elif still:
                locked += 1          # locked somewhere else (reported below)
            if not still:
                speeds.append(1 - (kmin[-1] - kmin[T - 1024]) / 1024)
            ends.append(kmin[-1])
        res[d] = (locked / phases, speeds, ends)
        print(f"   flip on {d:3d} (barrier {barrier(d)}): locked {locked}/{phases}; ends {sorted(set(ends))[:6]}"
              + (f"; climbing at {np.mean(speeds):.3f}" if speeds else ""), flush=True)
    report("LP0 a flip on 3 is locked on 3 at every phase", res[3][0] == 1.0 and set(res[3][2]) == {3})
    p400 = np.mean([res[d][0] for d in flips if 30 <= d <= 395])
    verdict("LP1 lock probability at 400 between 0.5 and 0.9", 0.5 <= p400 <= 0.9, f"{p400:.3f}")
    far = np.mean([res[d][0] for d in (30, 50, 100)]); near = np.mean([res[d][0] for d in (350, 380, 390, 395)])
    far29 = np.mean([res[d][0] for d in (8, 10, 12, 15)]); near29 = np.mean([res[d][0] for d in (25, 28)])
    verdict("LP2 far flips are caught more often than near ones, at 400 and at 29",
            far - near >= 0.1 and far29 > near29, f"400: far {far:.3f} near {near:.3f}; 29: far {far29:.3f} near {near29:.3f}")
    sp = [v for d in flips if 30 <= d <= 395 for v in res[d][1]]
    verdict("LP3 flips that slip past 400 climb at 0.25 within 0.05", bool(sp) and all(abs(v - 0.25) <= 0.05 for v in sp),
            f"{len(sp)} slipped; speeds {min(sp):.3f} .. {max(sp):.3f}" if sp else "none slipped")
    report("CF  flips on 450 do NOT lock with probability >= 0.5", res[450][0] < 0.5, f"{res[450][0]:.3f}")
    print("\nALL CHECKS PASS" if FAILS == 0 else f"\n{FAILS} CHECK(S) FAILED")


def lockphase(t0=4096, T=2048, phases=32):
    flips = [4, 6, 12, 20, 30, 100, 300, 395]
    width = 2 * (t0 + phases + T) + 1024
    a = np.zeros(width, dtype=np.uint8); a[width // 2] = 1
    for _ in range(t0):
        a = step(a)
    rows = []
    for _ in range(phases):
        rows.append(a.copy()); a = step(a)
    ends = {}
    for d in flips:
        ends[d] = []
        for j, r in enumerate(rows):
            off = width // 2 - (t0 + j)
            x, y = r.copy(), r.copy(); y[off + d] ^= 1
            for _ in range(T):
                x, y = step(x), step(y)
            ends[d].append(int(np.argmax(x != y)) + T - off)
        print(f"   flip on {d:3d}: end by phase (t = 4096 + j): " + " ".join(
            ("8" if e == 8 else "29" if e == 29 else "400" if e == 400 else ".") for e in ends[d]), flush=True)
    S400 = [set((t0 + j) % 16 for j, e in enumerate(ends[d]) if e == 400) for d in (30, 100, 300, 395)]
    rep = all(ends[d][j] == ends[d][j + 16] for d in flips for j in range(16))
    report("LQ1 one set S400 of size 8 for the flips 30 .. 395, repeating with period 16",
           all(S == S400[0] for S in S400) and len(S400[0]) == 8 and rep, f"S400 = {sorted(S400[0])}, repeats {rep}")
    S29 = [set((t0 + j) % 16 for j, e in enumerate(ends[d]) if e == 29) for d in (12, 20)]
    slip400 = [set((t0 + j) % 16 for j, e in enumerate(ends[d]) if e == 400) for d in (12, 20)]
    ok2 = S29[0] == S29[1] and len(S29[0]) == 12 and all(s == (set(range(16)) - S29[0]) & S400[0] for s in slip400)
    verdict("LQ2 S29 is one set of 12 residues and the slippers lock at 400 exactly on S400", ok2,
            f"S29 = {sorted(S29[0])} / {sorted(S29[1])}; slippers locked at 400: {sorted(slip400[0])} / {sorted(slip400[1])}")
    bit3 = set(r for r in range(16) if r & 8)
    verdict("LQ3 S400 is bit 3 of t (set or clear)", S400[0] in (bit3, set(range(16)) - bit3), f"S400 = {sorted(S400[0])}")
    print("\nALL CHECKS PASS" if FAILS == 0 else f"\n{FAILS} CHECK(S) FAILED")


def main():
    if "lockphase" in sys.argv[1:]:
        lockphase()
        return
    if "lockprob" in sys.argv[1:]:
        lockprob()
        return
    if "lock" in sys.argv[1:]:
        lock()
        return
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
