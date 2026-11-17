#!/usr/bin/env python3
"""rule30_cheat_ladder.py: the cheating coin one level up (RULE30-PRIZE.md 8.93), after the owner (2026-10-13): "the
coin appears fair on measure, but is not fair given rule 30 is a logical predictable repeatable pattern - so the very
toss of the entire problem is cheating."

Three parts.
  D  The fairness ladder. Call a periodic word k-fair if every k-block occurs equally often in its cycle. 8.34 noted
     that density 1/2 (1-fair) rules out every odd period and every lopsided block but not 01. Here, at every level:
     a k-fair word's least period is a multiple of 2^k, and at period 2^k the k-fair words are exactly the de Bruijn
     cycles. So every finite level of fairness is passed by some periodic cheat; 01 is the de Bruijn cycle of order 1.
  R  Where cheats come from. On a ring every column is eventually periodic (finite state, pigeonhole). L433 found
     rings with a column reading 01 for ever only at 7, 14 and 21 cells (to 22). Here: their temporal periods, whether
     they are one family, and how many states alternate in column 0 from tick 0 for ever (the plateau, against
     Collatz's exactly one per phase in 8.92).
  K  The pair side at depth (the block's unexpected check): the tick by which the single seed's centre column has shown
     all 2^k k-blocks, against a coin, with two cheaters as controls.

RUN-ON:     cpu (Python 3 standard library; a few minutes, most of it the single seed to 2^19 ticks)
COMMAND:    python3 tests/probes/lexicon/rule30_cheat_ladder.py

Record searched: 'Problem 3' -> 8.34 (P3 implies P1, noted by Wolfram), GC481; 'odd period' -> 8.34 (density rules out
odd periods and lopsided blocks); 'de Bruijn' -> de Bruijn graphs used for counts (8.77, 8.86, G127), no fairness
ladder; 'injective' with 'finite config' -> G121 (Rule 30 is injective on finite configurations); 'column reading 0 1'
-> L433 (ring sizes 7, 14, 21 for q = 1); 'Kolmogorov', 'logical depth' -> no hit.

PREDICTIONS (written 2026-10-13 before the run).
  D1 must hold (proof: each of the 2^k blocks occurs p/2^k times, an integer): over every word of length p <= 16
     whose least period is p, k-fair implies 2^k divides p, for k = 1 .. 4. REFUTED-BY: a k-fair word with 2^k not
     dividing p.
  D2 must hold (de Bruijn; the BEST theorem count 2^(2^(k-1) - k) cycles up to rotation): at p = 2^k the k-fair words
     of least period p number 2, 4, 16, 256 for k = 1, 2, 3, 4, and each contains every k-block exactly once.
  D3 blind: for k = 1, 2, 3 and every p <= 16 divisible by 2^k, some word of least period p is k-fair.
     REFUTED-BY: a multiple of 2^k (<= 16) with no k-fair primitive word.
  R1 must hold (L433): among rings of 3 .. 21 cells, those with a column reading 01 for ever are exactly 7, 14, 21.
  R2 blind: every such cheating cycle has temporal period 4 and is the 7-cell cheat repeated around the ring (one
     family). REFUTED-BY: a cheating cycle at 14 or 21 cells that is not a repetition of a 7-cell cheating state, or a
     temporal period other than 4.
  R3 blind: the plateau (ring states, transients included, whose column 0 alternates from tick 0 for ever, either
     phase) is at most 2 n per cheating ring size n, i.e. tiny against 2^n. REFUTED-BY: a larger count.
  K1 must fail (controls that the instrument can say no): the word 0101... never shows the block 00, so it completes
     k = 1 only; Rule 90's single-seed centre column (1 then white) never shows 01, so it completes k = 1 only.
  K2 blind: the single seed's centre column completes every k = 1 .. 14 within 2^19 ticks, each completion tick within
     a factor of 2 of the mean over 16 coin sequences. REFUTED-BY: a k not completed, or a ratio outside [0.5, 2].

ADDENDUM PREDICTION (written after the first run's R results, before part B ran).
  B1 blind: the basin of the cheating cycles (ring states whose orbit eventually enters one, in any column) is below
     5 percent of all states at n = 14 and n = 21: on rings the cheat is an isolated cycle, not the attractor it is
     for Collatz (every start below 2^16 reaches the cycle 1, 2). REFUTED-BY: 5 percent or more at either size.

OUTCOME (2026-10-13, M5, 23 s; machine output quoted; eight of nine held, B1 refuted):
  D1 HELD, D2 HELD, D3 HELD. Primitive k-fair words for k = 1..4: p = 2 [2, 0, 0, 0]; p = 4 [4, 4, 0, 0]; p = 6
     [18, 0, 0, 0]; p = 8 [64, 32, 16, 0]; p = 12 [900, 396, 0, 0]; p = 16 [12800, 4864, 1280, 256]. At p = 2^k:
     2, 4, 16, 256. Every multiple of 2^k up to 16 has a k-fair primitive word (k = 1, 2, 3).
  R1 HELD: cheating ring sizes [7, 14, 21] (L433 replicated). R2 HELD: 7, 14, 21 cheating (cycle, column) pairs, every
     temporal period 4, every cheating state the 7-cell cheat repeated. R3 HELD: plateau 4 at every size (4 of 128,
     4 of 16384, 4 of 2097152).
  K1 HELD: 0101... completes k = 1 only; Rule 90's centre completes k = 1 only.
  K2 HELD: Rule 30 against the 16-coin mean, k = 1..14: ratios 0.86, 0.74, 0.68, 0.94, 0.76, 1.48, 1.76, 1.00, 0.88,
     0.78, 1.45, 1.17, 0.99, 0.87 (k = 14: tick 143603 against 164283). The column took 18 s to 2^19 ticks.
  B1 FAILED: basin 49 of 128 (n = 7), 1085 of 16384 = 6.6223 percent (n = 14, longest transient 43), 49 of 2097152 =
     0.0023 percent (n = 21). Post hoc, not a prediction (checked by brute force, 80 ticks per state): of the 1085,
     49 are 7-periodic already and 1036 are non-periodic states whose orbit becomes 7-periodic after 1 to 41 ticks,
     which needs x and its shift by 7 to share an image; the 14-cell ring has 813 images with two or more preimages
     (and 813 gardens of Eden). The n = 7 basin (49) was confirmed by a brute-force second implementation.
"""
import random, sys, time

def least_period(w):
    p = len(w)
    for d in range(1, p + 1):
        if p % d == 0 and w == w[d:] + w[:d]:
            return d
    return p

def fair_level(bits, p):
    """Largest k <= 4 such that every k-block occurs equally often in the cyclic word (bits as an int, length p)."""
    best = 0
    for k in range(1, 5):
        if k > p: break
        counts = [0] * (1 << k)
        for i in range(p):
            b = 0
            for j in range(k):
                b = (b << 1) | ((bits >> ((i + j) % p)) & 1)
            counts[b] += 1
        if len(set(counts)) == 1: best = k
        else: break
    return best

def part_D(ok):
    print("D: the fairness ladder over primitive words of length p <= 16")
    d1 = True; at_db = {}; exists = {}
    for p in range(1, 17):
        tally = [0] * 5
        for bits in range(1 << p):
            s = format(bits, f"0{p}b")
            if least_period(s) != p: continue
            F = fair_level(bits, p)
            for k in range(1, F + 1):
                tally[k] += 1
                if p % (1 << k): d1 = False
            for k in range(1, 4):
                if F >= k: exists[(k, p)] = True
        if p in (2, 4, 8, 16):
            at_db[p] = tally[{2: 1, 4: 2, 8: 3, 16: 4}[p]]
        if p in (2, 4, 6, 8, 12, 16):
            print(f"  p={p:2d}: primitive words that are k-fair for k=1..4: {tally[1:]}")
    print("  k-fair words at p = 2^k (k=1..4):", [at_db[p] for p in (2, 4, 8, 16)])
    ok["D1"] = d1
    ok["D2"] = [at_db[p] for p in (2, 4, 8, 16)] == [2, 4, 16, 256]
    missing = [(k, p) for k in (1, 2, 3) for p in range(1 << k, 17, 1 << k) if not exists.get((k, p))]
    print("  multiples of 2^k with no k-fair primitive word:", missing)
    ok["D3"] = not missing

def ring_cycles(n):
    mask = (1 << n) - 1; N = 1 << n
    nxt = [(((s << 1) | (s >> (n - 1))) & mask) ^ (s | (((s >> 1) | (s << (n - 1))) & mask)) for s in range(N)]
    colour = bytearray(N); cycles = []
    for s0 in range(N):
        if colour[s0]: continue
        path, s = [], s0
        while not colour[s]:
            colour[s] = 1; path.append(s); s = nxt[s]
        if colour[s] == 1: cycles.append(path[path.index(s):])
        for q in path: colour[q] = 2
    return nxt, cycles

def rot(s, n, r):
    mask = (1 << n) - 1
    return ((s << r) | (s >> (n - r))) & mask if r else s

def part_R(ok, nmax):
    print(f"\nR: rings of 3 .. {nmax} cells with a column reading 01 for ever")
    sizes = []; r2 = True; r3 = True
    seven = None
    for n in range(3, nmax + 1):
        nxt, cycles = ring_cycles(n)
        cheating = []   # (cycle, column)
        for cyc in cycles:
            if len(cyc) % 2: continue
            for i in range(n):
                col = [(c >> i) & 1 for c in cyc]
                if all(col[t] != col[t + 1] for t in range(len(cyc) - 1)) and col[-1] != col[0]:
                    cheating.append((cyc, i))
        if not cheating: continue
        sizes.append(n)
        periods = sorted({len(c) for c, _ in cheating})
        if n == 7: seven = {s for c, _ in cheating for s in c}
        # one family: every cheating state is the 7-cell cheating state repeated n/7 times, up to rotation
        fam = True
        if seven is not None and n % 7 == 0:
            reps = set()
            for s7 in seven:
                rep = 0
                for j in range(n // 7): rep |= s7 << (7 * j)
                for r in range(n): reps.add(rot(rep, n, r))
            fam = all(s in reps for c, _ in cheating for s in c)
        else:
            fam = n == 7
        # plateau: states whose column 0 alternates from tick 0 for ever (cycle detection along the orbit)
        plateau = 0
        for s0 in range(1 << n):
            s, seen, prev, good = s0, {}, None, True
            t = 0
            while s not in seen:
                seen[s] = t
                c = s & 1
                if prev is not None and c == prev: good = False; break
                prev = c; s = nxt[s]; t += 1
            if good:
                # the closing step back into the cycle must also alternate, and the cycle length must be even
                if (s & 1) == prev: good = False
                if good and (t - seen[s]) % 2: good = False
            plateau += good
        print(f"  n={n:2d}: cheating cycles (column) {len(cheating)}, temporal periods {periods}, one family {fam}, "
              f"plateau {plateau} of {1 << n}")
        r2 &= fam and periods == [4]
        r3 &= plateau <= 2 * n
    print("  ring sizes with a cheating column:", sizes)
    ok["R1"] = sizes == [n for n in (7, 14, 21) if n <= nmax]
    ok["R2"], ok["R3"] = r2, r3

def part_B(ok, sizes):
    print("\nB: the basin of the cheating cycles (states that eventually enter one)")
    b1 = True
    for n in sizes:
        nxt, cycles = ring_cycles(n)
        cheat = set()
        for cyc in cycles:
            if len(cyc) % 2: continue
            for i in range(n):
                col = [(c >> i) & 1 for c in cyc]
                if all(col[t] != col[(t + 1) % len(cyc)] for t in range(len(cyc))):
                    cheat.update(cyc); break
        N = 1 << n; state = bytearray(N)        # 0 unknown, 1 enters a cheating cycle, 2 does not, 3 on the current path
        depth = [0] * N                          # ticks to reach a cheating cycle, for basin states
        for c in cheat: state[c] = 1
        for s0 in range(N):
            if state[s0]: continue
            path, s = [], s0
            while state[s] == 0:
                state[s] = 3; path.append(s); s = nxt[s]
            v = 2 if state[s] == 3 else state[s]   # a 3 means the path closed a new cycle, which cannot be cheating
            d = depth[s]
            for q in reversed(path):
                state[q] = v
                if v == 1: d += 1; depth[q] = d
        longest = max((depth[q] for q in range(N) if state[q] == 1), default=0)
        basin = sum(1 for x in state if x == 1)
        print(f"  n={n:2d}: basin {basin} of {N} ({100 * basin / N:.4f} percent), cycle states {len(cheat)}, "
              f"longest transient into it {longest}")
        if n in (14, 21): b1 &= basin < 0.05 * N
    ok["B1"] = b1

def completion_ticks(bits, kmax):
    """bits: a list of 0/1. For each k, the index of the bit that completes the set of all 2^k k-blocks, or None."""
    out = {}
    for k in range(1, kmax + 1):
        need = 1 << k; seen = bytearray(need); got = 0; v = 0; mask = need - 1; done = None
        for i, b in enumerate(bits):
            v = ((v << 1) | b) & mask
            if i >= k - 1 and not seen[v]:
                seen[v] = 1; got += 1
                if got == need: done = i; break
        out[k] = done
    return out

def centre_column(rule, T):
    S = 1 << (T + 2); col = []
    for t in range(T):
        col.append((S >> (T + 2)) & 1)
        if rule == 30: S = (S << 1) ^ (S | (S >> 1))
        else: S = (S << 1) ^ (S >> 1)
    return col

def part_K(ok, T, kmax):
    print(f"\nK: ticks by which all 2^k k-blocks have appeared (T = {T})")
    t0 = time.time()
    c30 = centre_column(30, T)
    print(f"  single-seed centre column computed in {time.time() - t0:.0f} s")
    k30 = completion_ticks(c30, kmax)
    alt = completion_ticks([t & 1 for t in range(T)], kmax)
    k90 = completion_ticks(centre_column(90, 4096), kmax)
    ok["K1"] = [k for k, v in alt.items() if v is not None] == [1] and [k for k, v in k90.items() if v is not None] == [1]
    print("  controls, k completed: 0101...", [k for k, v in alt.items() if v is not None],
          "| Rule 90 centre", [k for k, v in k90.items() if v is not None])
    rng = random.Random(30)
    coins = [completion_ticks([rng.getrandbits(1) for _ in range(T)], kmax) for _ in range(16)]
    k2 = True
    for k in range(1, kmax + 1):
        vals = [c[k] for c in coins if c[k] is not None]
        mean = sum(vals) / len(vals) if vals else None
        r = (k30[k] / mean) if (k30[k] is not None and mean) else None
        print(f"  k={k:2d}: Rule 30 {k30[k]}, coin mean {mean:.0f} (min {min(vals)}, max {max(vals)}, n={len(vals)}),"
              f" ratio {r:.2f}" if r is not None else f"  k={k:2d}: Rule 30 {k30[k]}, coins {vals}")
        k2 &= r is not None and 0.5 <= r <= 2
    ok["K2"] = k2

def main():
    ok = {}
    part_D(ok)
    part_R(ok, int(sys.argv[1]) if len(sys.argv) > 1 else 21)
    part_K(ok, 1 << 19, 14)
    part_B(ok, (7, 14, 21))
    print("\n" + "  ".join(f"{k} {'HELD' if v else 'FAILED'}" for k, v in ok.items()))
    print("ALL CHECKS PASS" if all(ok.values()) else "SOME CHECKS FAILED")

if __name__ == "__main__":
    main()
