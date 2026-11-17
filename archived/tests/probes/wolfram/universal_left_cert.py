#!/usr/bin/env python3
"""universal_left_cert.py: the 53,209-bit strip row of the universal left side, and the negative controls of its Lean
certificate (Local, L1503).

RUN-ON:     cpu (Python 3, standard library). Under a second.
COMMAND:    python3 tests/probes/wolfram/universal_left_cert.py OUTDIR
            then run Lean 4.35.0 on each OUTDIR/Ctl_*.lean: every control must fail with a kernel error except Ctl_pos.

The row B is the single seed's row at tick 72,000 in the left-edge frame, F(v) = (v << 2) xor ((v << 1) or v), on 53,209
bits. It returns after 16 ticks, so the strip is periodic from tick 0; no seed run is needed in the kernel. The script
asserts the return, for B and for B with bit 53,208 flipped, prints the white wheels and the farther weights, and writes
B.hex and the controls.
"""
import hashlib
import os
import sys

sys.set_int_max_str_digits(0)
K = 53209
M = (1 << K) - 1


def step(v):
    return ((v << 2) ^ ((v << 1) | v)) & M


def cycle(v):
    rows = []
    for _ in range(16):
        rows.append(v)
        v = step(v)
    assert v == rows[0], 'no 16-tick return'
    return rows


def main(out):
    os.makedirs(out, exist_ok=True)
    v = 1
    for _ in range(72000):
        v = step(v)
    rows = cycle(v)
    cycle(v ^ (1 << 53208))
    black = 0
    for r in rows:
        black |= r
    white = [j for j in range(53208) if not (black >> j) & 1]
    assert white == [2, 7, 28, 399, 53207], white
    for m, period in ((1, 1), (6, 2), (27, 4), (398, 8), (53206, 16)):
        print('farther wheel', m, 'weight over', period, sum((rows[r] >> m) & 1 for r in range(period)))
    print('white wheels below 53,208:', white)
    print('digits', len(str(v)), 'sha256 of the decimal string', hashlib.sha256(str(v).encode()).hexdigest())
    with open(os.path.join(out, 'B.hex'), 'w') as f:
        f.write(hex(v) + '\n')
    pre = lambda b: f'''def stepK (K v : Nat) : Nat := ((v <<< 2) ^^^ ((v <<< 1) ||| v)) % 2 ^ K
def rowAt (K v : Nat) : Nat → Nat
  | 0 => v
  | t + 1 => stepK K (rowAt K v t)
def B : Nat := {hex(b)}
def C (j t : Nat) : Bool := (rowAt 53209 B t).testBit j
def orRows : Nat → Nat
  | 0 => 0
  | n + 1 => orRows n ||| rowAt 53209 B n
'''
    ret = 'theorem c : rowAt 53209 B 16 = B := by decide +kernel\n'
    controls = {
        'pos': pre(v) + ret,
        'a_flip30000': pre(v ^ (1 << 30000)) + ret,
        'b_flip53207': pre(v ^ (1 << 53207)) + ret,
        'c_mask399': pre(v) + 'theorem c : (orRows 16 ||| (2 ^ 2 ||| 2 ^ 7 ||| 2 ^ 28)) % 2 ^ 53207 = 2 ^ 53207 - 1 := by decide +kernel\n',
        'd_mask53207': pre(v) + 'theorem c : (orRows 16 ||| (2 ^ 2 ||| 2 ^ 7 ||| 2 ^ 28 ||| 2 ^ 399)) % 2 ^ 53208 = 2 ^ 53208 - 1 := by decide +kernel\n',
        'e_anti53208': pre(v) + 'theorem c : ∃ L, L < 16 ∧ ∀ r, r < 16 → C 53208 (r + L) = !C 53208 r := by decide +kernel\n',
        'f_per400': pre(v) + 'theorem c : ∀ r, r < 16 → rowAt 53209 B (r + 8) % 2 ^ 401 = rowAt 53209 B r % 2 ^ 401 := by decide +kernel\n',
    }
    for name, src in controls.items():
        with open(os.path.join(out, f'Ctl_{name}.lean'), 'w') as f:
            f.write(src)


if __name__ == '__main__':
    main(sys.argv[1] if len(sys.argv) > 1 else '.')
