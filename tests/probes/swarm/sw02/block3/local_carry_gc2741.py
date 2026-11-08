#!/usr/bin/env python3
"""Local's carrying read of GC2741 (independent code; GPT's scripts not imported or run).

Prediction, written before the run (8 November 2026): for the three cited roots in the source frame (center black at
even ticks, rows as naturals with bit p - 1 = column p), heads at the odd ticks 5..45 follow the word 253353 (black at
7, 17, 23, 29, 39, 45), and (head3, col8(10), col8(13)) is (0,0,0), (0,0,1), (1,0,1). With seam m = 85 (physical 193),
P = parity of the 7 OR terms z_s(84) | z_s(85), s = 3..9, equals head3 XOR col8(10), and Q = parity of the 8 OR terms
z_s(81) | z_s(82), s = 5..12, equals center5 XOR col8(13) = col8(13). The two P = 0 roots share the P terms 1111101 and
have Q terms 01110111 (Q = 0) and 01110101 (Q = 1). An inverse right-to-left scan of the seam row reproduces every row
and reads event (t, p) at cell j = m - t + p; at the physical seam 193 the live rows before cells 102 and 79 number
102 and 79, so 204 and 158 pair bits.
Counterfactual: any mismatch means an index, phase or datum in GC2741 is off, and the carry stops there."""

ROOTS = [52777231658405, 54421244276371]
def step(x, t): return ((x << 1) | (1 if t % 2 == 0 else 0)) ^ (x | (x >> 1))
def history(x, n):
    out = [x]
    for t in range(n): x = step(x, t); out.append(x)
    return out
def cell(rows, t, p):  # column 0 is the drive
    return (1 if t % 2 == 0 else 0) if p == 0 else (rows[t] >> (p - 1)) & 1
WORD = {}
s, ones = 0, {0}
for ch in '253353': s += int(ch); ones.add(s)
for k in range(s + 1): WORD[3 + 2 * k] = int(k in ones)

# the genuine fixture: seed 2135555 at tick 74 (even, so the drive phase matches), clipped to 46 cells
fx = history(2135555, 74)[-1] & ((1 << 46) - 1)
ROOTS.append(fx)
m = 85
for R in ROOTS:
    rr = history(R, m)
    heads_ok = all(cell(rr, t, 1) == b for t, b in WORD.items() if t != 3)
    h3, w10, b13 = cell(rr, 3, 1), cell(rr, 10, 8), cell(rr, 13, 8)
    z = lambda s_, j: cell(rr, s_, j - m + s_)
    Pt = [z(s_, 84) | z(s_, 85) for s_ in range(3, 10)]
    Qt = [z(s_, 81) | z(s_, 82) for s_ in range(5, 13)]
    P, Q = sum(Pt) % 2, sum(Qt) % 2
    # inverse scan of the seam row: v_s(k) = v_{s+1}(k) xor (v_s(k+1) or v_s(k+2)), v_m(k) = seam cell k + m
    M = rr[m]; W = M.bit_length() + m + 3
    v = {}
    ok_scan = True
    for k in range(W, -m - 1, -1):
        v[(m, k)] = (M >> (k + m - 1)) & 1 if k + m >= 1 else None
        for s_ in range(m - 1, -1, -1):
            if k + s_ < 0: break
            up = v[(s_ + 1, k)] if k + s_ + 1 >= 1 or s_ + 1 == m else None
            a = v.get((s_, k + 1), 0); b = v.get((s_, k + 2), 0)
            val = up ^ (a | b)
            v[(s_, k)] = val
            if val != cell(rr, s_, k + s_): ok_scan = False
    print(f'root {R}: heads 5..45 match {heads_ok}; (head3, col8(10), col8(13)) = ({h3},{w10},{b13}); '
          f'P = {P} = head3 xor col8(10) {P == h3 ^ w10}; Q = {Q} = center5 xor col8(13) {Q == (cell(rr,5,0) ^ b13)}; '
          f'P terms {"".join(map(str,Pt))}; Q terms {"".join(map(str,Qt))}; inverse scan reproduces rows 0..{m-1} {ok_scan}')
# event schedule at the physical seam 193, read j = 193 - t + p
for name, t, p in (('older pulse', 111, 1), ('head113', 113, 1), ('last5 start', 115, 1), ('white input', 118, 8),
                   ('black input', 121, 8), ('E start', 125, 1), ('end of 3353', 153, 1)):
    print(f'{name}: j = {193 - t + p}')
live = lambda jn: sum(1 for s_ in range(0, 193) if (jn - 193) + s_ >= 0)
print('live rows before cell 102:', live(102), '-> pair bits', 2 * live(102), '; before cell 79:', live(79), '-> pair bits', 2 * live(79))
