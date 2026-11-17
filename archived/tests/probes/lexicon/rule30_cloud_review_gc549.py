#!/usr/bin/env python3
"""rule30_cloud_review_gc549.py: Cloud's independent replay of the finite claims in GPT's GC549 checkpoints 10 to 16.

RUN-ON:     cpu (Python 3 standard library)
COMMAND:    python3 tests/probes/lexicon/rule30_cloud_review_gc549.py
COST:       a few seconds.

GPT's sustained Q6 notebook (RULE30-GPT.md, GC549) asked for a second reading of checkpoint 15's extended algebra.
The hand reading is in the chat (CL040). This script checks the finite statements of checkpoints 10 to 16 in
Cloud's own coding, sharing no code with GPT. Rows are sets of black sites; Rule 30 is x' = l XOR (c OR r). Each
check below is GPT's stated value, so each line is a control that should PASS.
  G10: phase-zero clock 0101.. through time t, centre white at time 0, initial white sites -2 .. -5 (d = 2): over all
       initial bits at -1 and sites 1 .. 8, the distinct admissible right prefixes r_1 .. r_t number 2, 2, 1, 2, 4
       for t = 1 .. 5, and x_0(-1) = 1, r_1 = r_2 = r_3 = 0 are forced.
  G11: with white sites -2 .. -7, the counts through t = 6, 7 are 8 and 3, and time 7 passes exactly when
       r_4 = r_5 = 0 and r_6 OR r_7 = 1.
  G12: with white sites -2 .. -8 no configuration keeps the clock through time 8; the traces of {-1, 6}, {-1, 7},
       {-1, 6, 7} are 010101011, that of {-1, 6, -8} is 010101010, and that of {-1} is 010101001.
  G14: at a white wall time, for every right row and the left half forced by the clock,
       (x_a(-1), x_a(-2), x_a(-3)) = (1 - c_0, c_0, 1 - c_1), with c_s column 1 at a + 2s.
  G15: with the left cells reconstructed by the inverse v_(j+1)(t) = v_j(t+1) XOR (v_j(t) OR v_(j-1)(t)) from the
       clock (v_0) and column 1 (v_(-1)) of actual right rows, at a white time a and B, D, E = c_1, c_2, c_3:
       v_3(a) = 1 - B, v_4(a) = 0, v_5(a) = 1 XOR B XOR D, v_5(a+1) = 1 - B, v_6(a) = D,
       v_6(a+1) = B XOR D XOR E, v_7(a) = 1 XOR D XOR E, v_7(a+1) = (1 - E) OR B, v_8(a) = B E.
       And the controls: right code 0101 gives v_1 .. v_8 at a = 10000001; constant c = 1 has v_4(a) = 1.
  G16: GPT's paired recursion f_(j+1) = g_j XOR (f_j OR f_(j-1)), g_(j+1) = S(f_j) XOR (g_j OR g_(j-1)), with
       (f_0, g_0) = (0, 1) and (f_1, g_1) = (1 - c_0, 1), reproduces v_j at white and black times for j <= 12 on
       every actual right word tried.
Unexpected check (Cloud's, predicted before the run, confidence 0.7): checkpoint 15's no-11 simplification is not
  needed for the G15 identities at depth 4 and 8 only. Concretely, on every right word (the free code, with column 1
  allowed to be any sequence, the inverse recursion run on it), v_4(a) = 0 fails somewhere (GPT's own control says
  so), and v_8(a) = B E also fails somewhere, so both depend on the actual right language.
"""
from itertools import product


def step(black):
    if not black:
        return set()
    lo, hi = min(black) - 1, max(black) + 1
    return {i for i in range(lo, hi + 1) if ((i - 1) in black) ^ ((i in black) or ((i + 1) in black))}


def trace(seed, T):
    row, out = set(seed), []
    for _ in range(T + 1):
        out.append(int(0 in row))
        row = step(row)
    return out


def report(name, ok, detail=""):
    print(name, "PASS" if ok else "FAIL", detail)


def clock_ok(seed, T):
    return trace(seed, T) == [t % 2 for t in range(T + 1)]


def g10_g11_g12():
    counts, forced = {}, True
    rows = []
    for m in range(1 << 9):                         # bit 0: site -1; bits 1..8: sites 1..8
        seed = ({-1} if m & 1 else set()) | {k for k in range(1, 9) if m >> k & 1}
        rows.append((m, seed))
    for t in range(1, 8):
        white = set(range(-2, -6, -1)) if t <= 5 else set(range(-2, -8, -1))   # -2..-5, then -2..-7
        pref = set()
        for m, seed in rows:
            if seed & white:
                continue
            if clock_ok(seed, t):
                pref.add(tuple((m >> k) & 1 for k in range(1, t + 1)))
                if t >= 3:
                    forced &= (m & 1) == 1 and all(not (m >> k & 1) for k in (1, 2, 3))
        counts[t] = len(pref)
    report("G10", [counts[t] for t in range(1, 6)] == [2, 2, 1, 2, 4] and forced, f"counts {counts}")
    ok7 = True
    for m, seed in rows:
        if seed & set(range(-2, -8, -1)) or not clock_ok(seed, 6):
            continue
        r = [(m >> k) & 1 for k in range(0, 9)]
        want = r[4] == 0 and r[5] == 0 and (r[6] or r[7])
        ok7 &= clock_ok(seed, 7) == bool(want)
    report("G11", counts[6] == 8 and counts[7] == 3 and ok7)
    dead = not any(clock_ok(seed, 8) for m, seed in rows if not seed & set(range(-2, -9, -1)))
    traces = ["".join(map(str, trace(s, 8))) for s in ({-1, 6}, {-1, 7}, {-1, 6, 7}, {-1, 6, -8}, {-1})]
    report("G12", dead and traces == ["010101011"] * 3 + ["010101010", "010101001"], str(traces))


def inverse_columns(c1, clock, depth):
    """v[j][t] for j = -1 .. depth from column 1 (v_-1) and the clock (v_0); t ranges as far as defined."""
    v = {-1: list(c1), 0: list(clock)}
    for j in range(0, depth):
        n = min(len(v[j]), len(v[j - 1])) - 1
        v[j + 1] = [v[j][t + 1] ^ (v[j][t] | v[j - 1][t]) for t in range(n)]
    return v


def right_column1(right, T):
    """Column 1 for t = 0 .. T of the right half with the wall clamped to t mod 2 (white at even t)."""
    row, out = set(right), []
    for t in range(T + 1):
        out.append(int(1 in row))
        full = row | ({0} if t % 2 else set())
        row = {i for i in step(full) if i >= 1}
    return out


def g14_g15_g16():
    bad14 = bad15 = bad16 = 0
    T = 20
    clock = [t % 2 for t in range(T + 1)]
    for m in range(1 << 13):
        right = {k + 1 for k in range(13) if m >> k & 1}
        c1 = right_column1(right, T)
        v = inverse_columns(c1, clock, 12)
        A, B, D, E = c1[0], c1[2], c1[4], c1[6]
        bad14 += (v[1][0], v[2][0], v[3][0]) != (1 - A, A, 1 - B)
        want = {(3, 0): 1 - B, (4, 0): 0, (5, 0): 1 ^ B ^ D, (5, 1): 1 - B, (6, 0): D, (6, 1): B ^ D ^ E,
                (7, 0): 1 ^ D ^ E, (7, 1): (1 - E) | B, (8, 0): B & E}
        bad15 += any(v[j][t] != w for (j, t), w in want.items())
        n = len(c1) // 2 + 1                                          # white times 0, 2, .., 2(n - 1)
        Fs = {0: [0] * n, 1: [1 - c1[2 * k] for k in range(n)]}        # f_j at white times
        Gs = {0: [1] * n, 1: [1] * n}                                  # g_j at the following black times
        for jj in range(1, 12):
            Fs[jj + 1] = [Gs[jj][k] ^ (Fs[jj][k] | Fs[jj - 1][k]) for k in range(min(len(Gs[jj]), len(Fs[jj])))]
            Gs[jj + 1] = [Fs[jj][k + 1] ^ (Gs[jj][k] | Gs[jj - 1][k])
                          for k in range(min(len(Fs[jj]) - 1, len(Gs[jj]), len(Gs[jj - 1])))]
        for jj in range(1, 13):
            for k in range(len(Fs.get(jj, []))):
                if 2 * k < len(v.get(jj, [])):
                    bad16 += Fs[jj][k] != v[jj][2 * k]
            for k in range(len(Gs.get(jj, []))):
                if 2 * k + 1 < len(v.get(jj, [])):
                    bad16 += Gs[jj][k] != v[jj][2 * k + 1]
    report("G14", not bad14)
    report("G15", not bad15)
    code = inverse_columns([0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0], [t % 2 for t in range(12)], 8)
    ctrl = "".join(str(code[j][0]) for j in range(1, 9)) == "10000001"
    ones = inverse_columns([1] * 14, [t % 2 for t in range(14)], 8)
    report("G15-controls", ctrl and ones[4][0] == 1)
    report("G16", not bad16)
    # unexpected check: free codes (any column-1 sequence) break v_4(a) = 0 and v_8(a) = B E
    f4 = f8 = False
    for bits in product((0, 1), repeat=12):
        v = inverse_columns(list(bits), [t % 2 for t in range(12)], 8)
        f4 |= v[4][0] != 0
        f8 |= v[8][0] != (bits[2] & bits[6])
    print("unexpected check:", "HELD" if f4 and f8 else "REFUTED", f"(free codes break v_4 = 0: {f4}; "
          f"break v_8 = B E: {f8})")


if __name__ == "__main__":
    g10_g11_g12()
    g14_g15_g16()
