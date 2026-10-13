#!/usr/bin/env python3
"""rule30_pair_price.py: the owner's fair-coin question (2026-10-13) and the pair/price table (RULE30-PRIZE.md 8.92).

The owner: the centre column is a fair coin, but a 0101 tail is a coin that cheats, so period 2 contradicts itself.
Two ways the idea could become a proof, and this probe measures each on three systems:
  PAIR   (orbit by orbit): the column has the coin's pair statistics (each of 00, 01, 10, 11 a quarter of the time).
         The weakest pair statement that excludes a 0101 tail, "00 or 11 recurs", is period 2 itself restated.
  PRICE  (count over seeds): holding the alternating word costs bits, so the number of width-w seeds still holding it
         after T steps falls like 2^(w - alpha T + c), and every width-w seed breaks it within about w/alpha steps.
Systems: Rule 30 and Rule 90 on finite seeds (a window of w = 2h+1 cells about the centre column), Rule 30 on rings,
and the Collatz shortcut map T(n) = n/2 or (3n+1)/2 with seeds 1 <= n < 2^w and its parity sequence as the column.

RUN-ON:     cpu (Python 3 standard library; about a minute)
COMMAND:    python3 tests/probes/lexicon/rule30_pair_price.py

PREDICTIONS (written 2026-10-13 before the run; the ring part replicates a scratch run of the same morning).
  P1  must hold (RECORD-MAP L433/CL086): some Rule 30 ring of n <= 16 cells has a column reading 01 for ever; the
      scratch run found n = 7, the single black cell, column 1, row period 4. Controls: the word 0 is found (the
      all-white ring, must fire); the word 011111 (0 1^5) is found on no ring of n <= 16 (record: none to 22).
      REFUTED-BY: no 01 column, or a 011111 column, or no 0 column.
  P2  must hold (left permutivity, 8.51): Rule 30, each phase, N(T) = 2^(w-T) exactly for 1 <= T <= h+1, at
      w = 9, 11, 13, 15, 17 (at time t the cell -t enters the centre by XOR). REFUTED-BY: any mismatch.
  P3  must hold (hand: in Rule 90 the centre at time t is sum_i C(t,(t+i)/2) x_0(i) mod 2 and the cells +-t enter with
      coefficient 1): Rule 90, each phase, the same exact halving for 1 <= T <= h+1. REFUTED-BY: any mismatch.
  P4  blind: Rule 30 after T = h+1 keeps falling at about one bit a step (least-squares slope of log2 N over the range
      N >= 8 between -0.8 and -1.3 bits a step, both phases pooled), and the last survivor dies at T0 <= w + 10.
      REFUTED-BY: a slope outside that band, or a survivor at T = w + 11.
  P5  must hold (hand: at t = 2^m > h only the cells +-t could reach the centre, so x_t(0) = 0; at t = 2^m + 1 only
      +-(2^m - 1) and +-(2^m + 1)): with M the least power of two above h + 1, every Rule 90 seed has broken the
      alternating word by T = M + 2. REFUTED-BY: a survivor at T = M + 2.
  P6  blind: Rule 30, 200 random width-15 seeds, centre column over ticks [1000, 4000): each pooled pair frequency
      within 0.01 of 0.25. REFUTED-BY: one outside.
  P7  blind, from Lucas's theorem (odd binomials thin out): Rule 90 on the same seeds is far from a coin, pooled black
      density below 0.35 over [1000, 4000), and lower over [3000, 4000) than over [1000, 2000). REFUTED-BY: either fails.
  P8  must hold (Terras): Collatz, w = 16 and 20, each phase, N(k) = 2^(w-k) exactly for 1 <= k <= w.
  P9  must hold (a residue class mod 2^k with k >= w holds at most one n < 2^w, and n = 1, 2 alternate for ever):
      N(k) = 1 for every k from w to w + 40, the survivor being n = 1 (phase 1010...) or n = 2 (phase 0101...).
  P10 control: every n < 2^16 reaches 1, so its parity column ends 1010... for ever (00 and 11 never recur).
  C1  check-can-fail control: Rule 110, which is not left-permutive, breaks P2's exact halving somewhere at w = 9 or
      11. REFUTED-BY: exact halving holds for Rule 110 too (the check would then be blind).
  C2  second implementation: the big-integer step agrees with a plain list step on 20 random seeds over 60 ticks for
      Rules 30, 90 and 110.

OUTCOME (2026-10-13, M5, 1.7 s; machine output quoted, ten of twelve held):
  C2 HELD: 0 mismatching runs between the big-integer and list steps (Rules 30, 90, 110).
  P1 HELD: word 0 at n = 3 ('000'); word 01 at n = 7, cycle 4, column 1, start row '1000000' (the single black cell);
     word 011111 on no ring of n <= 16.
  P2 HELD, P3 HELD: exact halving to T = h+1 for Rules 30 and 90 at every w and phase.
  C1 HELD: Rule 110 breaks the exact halving at T = 3 (w = 9: 128/64 against 128/128), so the check can fail.
  P4 FAILED as written. The deadline half held: Rule 30's last survivor dies at T0 = 8, 10, 11, 11, 16 for
     w = 9, 11, 13, 15, 17 (every T0 <= w). The slope half was refuted: least-squares slopes -1.047, -0.743, -0.502,
     -2.845 (w = 11..17; w = 9 has too few points), because after T = h+1 only two to four counts remain above 8 and
     they fall in lumps (w = 17: 256, 141/9, 6/0, then 3 for four ticks, then 0). Post hoc, not a prediction: from
     T = h+1 to death the survivors lose h bits in 3, 4, 4, 3, 7 ticks, at least one bit a tick on average.
  P5 HELD: Rule 90 deadlines 9, 9, 9, 12, 12 against the bound M + 2 = 10, 10, 10, 18, 18; the survivors plateau and
     then die all at once (w = 9 phase 1: 16, 16, 16, 0 at T = 6..9).
  P6 HELD: Rule 30 pairs 00 0.2503, 01 0.2500, 10 0.2500, 11 0.2497; density 0.4997 (thirds 0.4985, 0.5011, 0.4995).
  P7 HELD: Rule 90 pairs 00 0.9968, 01 0.0011, 10 0.0011, 11 0.0009; density 0.0020 (thirds 0.0030, 0.0030, 0.0000).
  P8 FAILED as written, at one point only: phase 0 at k = 1 gives 2^(w-1) - 1 (32767 at w = 16, 524287 at w = 20),
     because the length-1 word 0 is the residue class 0 mod 2, which loses n = 0 from the seed range 1 <= n < 2^w.
     Every other k <= w and all of phase 1 match 2^(w-k) exactly. The prediction was mis-stated; Terras's bijection
     is untouched.
  P9 HELD: N(k) = 1 for k = w .. w+40 in both phases at w = 16 and 20; the surviving starts are n = 1 (1010...) and
     n = 2 (0101...).
  P10 HELD: all 65,535 starts below 2^16 reach 1.
  Addendum (same day, after the run): P5's hand argument is PROOFS.md entry 16, Proposition 5 (RULE30-PRIZE.md 8.3),
  re-derived; the record search had paired 'Rule 90' with 'price' and so missed it. Credit is Proposition 5's.
"""
import math, random, sys

RULES = {
    30: lambda S: (S << 1) ^ (S | (S >> 1)),          # bit b holds cell b - OFF; S << 1 puts cell p-1 at p
    90: lambda S: (S << 1) ^ (S >> 1),
    110: lambda S: ((S | (S >> 1)) & ~((S << 1) & S & (S >> 1))),   # 110 = (q | r) & ~(p & q & r)
}

def list_step(rule, x):
    n = len(x); out = [0] * n
    for i in range(n):
        p = x[i - 1] if i > 0 else 0; q = x[i]; r = x[i + 1] if i + 1 < n else 0
        out[i] = (rule >> (4 * p + 2 * q + r)) & 1
    return out

def check_second_impl(rng):
    bad = 0
    for rule in (30, 90, 110):
        for _ in range(20):
            w, T = 15, 60; OFF = T + w
            seed = [rng.randint(0, 1) for _ in range(w)]
            x = [0] * (T + 1) + seed + [0] * (T + 1)            # cell positions -(T+1+h) .. +(T+1+h)
            S = 0
            for j, b in enumerate(x):
                if b: S |= 1 << j
            mask = (1 << len(x)) - 1
            for t in range(T):
                x = list_step(rule, x); S = RULES[rule](S) & mask
                if any(((S >> j) & 1) != x[j] for j in range(len(x))):
                    bad += 1; break
    return bad

def survivors(rule, w, Tmax):
    """N_phase(T) for T = 0..Tmax: width-w seeds centred on cell 0 whose centre column reads (t + phase) % 2."""
    h = w // 2; OFF = Tmax + h + 2; step = RULES[rule]
    out = {}
    for phase in (0, 1):
        alive = [s << (OFF - h) for s in range(1 << w)]
        counts = [len(alive)]
        for t in range(Tmax):
            want = (t + phase) & 1
            alive = [S for S in alive if ((S >> OFF) & 1) == want]
            counts.append(len(alive))
            alive = [step(S) for S in alive]
            if not alive:
                counts += [0] * (Tmax - t - 1); break
        out[phase] = counts
    return out

def pair_stats(rule, seeds, t0, t1):
    w = len(seeds[0]); h = w // 2; OFF = t1 + h + 2; step = RULES[rule]
    pairs = [0, 0, 0, 0]; dens = {}
    for sd in seeds:
        S = 0
        for j, b in enumerate(sd):
            if b: S |= 1 << (OFF - h + j)
        prev = None
        for t in range(t1):
            c = (S >> OFF) & 1
            if t >= t0:
                if prev is not None: pairs[2 * prev + c] += 1
                lo = (t - t0) * 3 // (t1 - t0)          # thirds of the window
                a, b = dens.get(lo, (0, 0)); dens[lo] = (a + c, b + 1)
            prev = c if t >= t0 else None
            S = step(S)
    tot = sum(pairs)
    allb = sum(a for a, b in dens.values()); alln = sum(b for a, b in dens.values())
    return [p / tot for p in pairs], allb / alln, {k: a / b for k, (a, b) in sorted(dens.items())}

def ring_find(word, nmax):
    p = len(word)
    for n in range(3, nmax + 1):
        mask = (1 << n) - 1; N = 1 << n
        nxt = [(((s << 1) | (s >> (n - 1))) & mask) ^ (s | (((s >> 1) | (s << (n - 1))) & mask)) for s in range(N)]
        colour = bytearray(N)
        for s0 in range(N):
            if colour[s0]: continue
            path, s = [], s0
            while not colour[s]:
                colour[s] = 1; path.append(s); s = nxt[s]
            if colour[s] == 1:
                cyc = path[path.index(s):]
                if len(cyc) % p == 0:
                    for i in range(n):
                        col = [(c >> i) & 1 for c in cyc]
                        for ph in range(p):
                            if all(col[t] == int(word[(t + ph) % p]) for t in range(len(cyc))):
                                return n, len(cyc), i, ''.join(str((cyc[0] >> j) & 1) for j in range(n))
            for q in path: colour[q] = 2
    return None

def collatz_counts(w, kmax):
    out = {}
    for phase in (1, 0):
        alive = [(n, n) for n in range(1, 1 << w)]; counts = [len(alive)]      # (start, current)
        for k in range(kmax):
            want = (k + phase) & 1                     # phase 1: 1,0,1,0...; phase 0: 0,1,0,1...
            alive = [(a, n) for a, n in alive if (n & 1) == want]
            counts.append(len(alive))
            alive = [(a, (3 * n + 1) >> 1 if n & 1 else n >> 1) for a, n in alive]
        out[phase] = (counts, alive)
    return out

def main():
    rng = random.Random(20261013)
    ok = {}
    bad = check_second_impl(rng)
    print("C2 second implementation, mismatching runs:", bad); ok["C2"] = bad == 0

    r0, r01, r5 = ring_find("0", 16), ring_find("01", 16), ring_find("011111", 16)
    print("P1 rings: word 0 ->", r0, "| word 01 ->", r01, "| word 011111 ->", r5)
    ok["P1"] = r0 is not None and r01 is not None and r5 is None

    print("\nsurvivor counts N(T), phase 0 / phase 1 (w = 2h+1 cells; exact halving expected to T = h+1)")
    p2 = p3 = True; c1_broken = False; slopes = []; p4_dead = True; p5 = True
    for rule in (30, 90, 110):
        for w in ((9, 11, 13, 15, 17) if rule != 110 else (9, 11)):
            h = w // 2; Tmax = w + 14
            S = survivors(rule, w, Tmax)
            exact = all(S[ph][T] == 2 ** (w - T) for ph in (0, 1) for T in range(1, h + 2))
            T0 = max(next((T for T in range(Tmax + 1) if S[ph][T] == 0), Tmax + 1) for ph in (0, 1))
            line = " ".join(f"{a}/{b}" for a, b in zip(S[0][:T0 + 1], S[1][:T0 + 1]))
            print(f"  rule {rule:3d} w={w:2d}: exact-to-h+1={exact}  last survivor dies at T0={T0}  N: {line}")
            if rule == 30:
                p2 &= exact
                pts = [(T, math.log2(S[ph][T])) for ph in (0, 1) for T in range(h + 1, Tmax + 1) if S[ph][T] >= 8]
                if len(pts) >= 3:
                    mt = sum(T for T, _ in pts) / len(pts); ml = sum(l for _, l in pts) / len(pts)
                    slope = sum((T - mt) * (l - ml) for T, l in pts) / sum((T - mt) ** 2 for T, _ in pts)
                    slopes.append((w, round(slope, 3)))
                p4_dead &= T0 <= w + 10
            elif rule == 90:
                p3 &= exact
                M = 1
                while M <= h + 1: M *= 2
                p5 &= T0 <= M + 2
                print(f"      P5 bound M + 2 = {M + 2}")
            else:
                c1_broken |= not exact
    print("  Rule 30 slopes of log2 N after h+1 (w, bits/step):", slopes)
    ok["P2"], ok["P3"], ok["P5"], ok["C1"] = p2, p3, p5, c1_broken
    ok["P4"] = p4_dead and all(-1.3 <= s <= -0.8 for _, s in slopes)

    seeds = [[rng.randint(0, 1) for _ in range(15)] for _ in range(200)]
    for s in seeds: s[0] = s[-1] = 1
    for rule in (30, 90):
        pf, d, thirds = pair_stats(rule, seeds, 1000, 4000)
        print(f"\nrule {rule} pairs over [1000,4000), 200 seeds: 00 {pf[0]:.4f} 01 {pf[1]:.4f} 10 {pf[2]:.4f} 11 {pf[3]:.4f}"
              f"  density {d:.4f}  by thirds {', '.join(f'{v:.4f}' for v in thirds.values())}")
        if rule == 30: ok["P6"] = all(abs(x - 0.25) <= 0.01 for x in pf)
        else: ok["P7"] = d < 0.35 and thirds[2] < thirds[0]

    print("\nCollatz shortcut map, N(k) per phase (1 = 1010..., 0 = 0101...)")
    p8 = p9 = True
    for w in (16, 20):
        C = collatz_counts(w, w + 40)
        for ph in (1, 0):
            counts, alive = C[ph]
            ex = all(counts[k] == 2 ** (w - k) for k in range(1, w + 1))
            plateau = all(counts[k] == 1 for k in range(w, w + 41))
            surv = [a for a, n in alive]
            p8 &= ex; p9 &= plateau and surv == ([1] if ph == 1 else [2])
            print(f"  w={w} phase {ph}: exact to k=w {ex}; N(k)=1 for k=w..w+40 {plateau}; "
                  f"N(w-3..w+3) = {counts[w-3:w+4]}; surviving start {surv}")
    ok["P8"], ok["P9"] = p8, p9
    reach = 0
    for n in range(1, 1 << 16):
        m, steps = n, 0
        while m != 1 and steps < 10000:
            m = (3 * m + 1) >> 1 if m & 1 else m >> 1; steps += 1
        reach += (m == 1)
    print(f"\nP10 every n < 2^16 reaches 1: {reach == (1 << 16) - 1} ({reach} of {(1 << 16) - 1})")
    ok["P10"] = reach == (1 << 16) - 1

    print("\n" + "  ".join(f"{k} {'HELD' if v else 'FAILED'}" for k, v in ok.items()))
    print("ALL CHECKS PASS" if all(ok.values()) else "SOME CHECKS FAILED")

if __name__ == "__main__":
    main()
