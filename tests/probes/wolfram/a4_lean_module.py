#!/usr/bin/env python3
"""L1424 (Local, 2026-11-03): generate A4's Lean module for one ring background from a4_closure_export.py's JSON, using the
kernel-checked (9, 57) module tests/probes/lean/MovingWall.lean (zero offset written out) as the template.
Run: python3 tests/probes/wolfram/a4_lean_module.py DATA.json NAMESPACE OUT.lean
Every background-specific constant of the template is replaced by the data's (N, q, s, W, P, S, A0, start state, potential
range); each replacement must find its pattern, so a template change cannot pass silently.
"""
import json
import pathlib
import sys

root = pathlib.Path(__file__).resolve().parents[3]
d = json.load(open(sys.argv[1])); ns = sys.argv[2]
N, q, s, W, P, S, t0, A0 = d['N'], d['q'], d['s'], d['W'], d['P'], d['S'], d['t0'], d['A0']
assert d['r'] == 0 and t0 == 300 and d['lo'] == d['hi']
tq0, dq0 = d['states'][0][0], d['states'][0][1]
lo_b, hi_b = min(d['lo']), max(d['lo'])
src = (root / 'tests/probes/lean/MovingWall.lean').read_text()
head, rest = src.split('def orbRows : List Nat := [', 1)
rest = rest.split('\n\ndef ringBit', 1)[1]
rows = [sum(b << j for j, b in enumerate(row)) for row in d['orb']]
keys = []
for (tq, dq, strip), psi in zip(d['states'], d['lo']):
    keys.append(((tq * N + dq) * (1 << W) + sum(b << i for i, b in enumerate(strip)), psi))
data = 'def orbRows : List Nat := [' + ', '.join(map(str, rows)) + ']\n\n'
data += '/-- The closure: `(key, ψ)` with `key = (tq * %d + dq) * 2 ^ %d + strip`. -/\n' % (N, W)
data += 'def closure : List (Nat × Int) := [\n' + ',\n'.join('  (%d, %d)' % kv for kv in keys) + ']'
head = head.rsplit('/-- The ring orbit', 1)[0]
head = head.replace('/-- The closure: `(key, ψ)` with `key = (tq * 9 + dq) * 2 ^ 24 + strip`. -/\n', '')
word = ''.join(str(b) for b in d['orb'][0])
head += '/-- The ring orbit of `%s`: row `τ` as a %d-bit number, bit `j` the cell at diagonal index `j`. -/\n' % (word, N)
body = '\n\ndef ringBit' + rest
reps = [
    ('τ < 57', 'τ < %d' % q), ('j < 9', 'j < %d' % N), ('((τ + 1) % 57)', '((τ + 1) %% %d)' % q),
    ('((j + 1) % 9)', '((j + 1) %% %d)' % N), ('((j + 8) % 9)', '((j + %d) %% %d)' % (N - 1, N)),
    ('/-- The background at alignment `(0, 0)`: `E t x` is the ring orbit\'s row `(t + 0) mod 57` at diagonal index `(t - x) mod 9`. -/',
     '/-- The background at alignment `(0, %d)`: `E t x` is the ring orbit\'s row `(t + %d) mod %d` at diagonal index `(t - x) mod %d`. -/' % (s, s, q, N)),
    ('def E (t : Nat) (x : Int) : Bool := ringBit ((t + 0) % 57) (((t : Int) - x) % 9).toNat',
     'def E (t : Nat) (x : Int) : Bool := ringBit ((t + %d) %% %d) (((t : Int) - x) %% %d).toNat' % (s, q, N)),
    ('have h := ring_table ((t + 0) % 57) (Nat.mod_lt _ (by decide)) (((t : Int) - x) % 9).toNat (by omega)',
     'have h := ring_table ((t + %d) %% %d) (Nat.mod_lt _ (by decide)) (((t : Int) - x) %% %d).toNat (by omega)' % (s, q, N)),
    ('have e1 : (t + 1 + 0) % 57 = ((t + 0) % 57 + 1) % 57 := by omega', 'have e1 : (t + 1 + %d) %% %d = ((t + %d) %% %d + 1) %% %d := by omega' % (s, q, s, q, q)),
    ('have e2 : ((((t + 1 : Nat) : Int) - x) % 9).toNat = ((((t : Int) - x) % 9).toNat + 1) % 9 := by omega',
     'have e2 : ((((t + 1 : Nat) : Int) - x) %% %d).toNat = ((((t : Int) - x) %% %d).toNat + 1) %% %d := by omega' % (N, N, N)),
    ('have e3 : (((t : Int) - (x - 1)) % 9).toNat = ((((t : Int) - x) % 9).toNat + 1) % 9 := by omega',
     'have e3 : (((t : Int) - (x - 1)) %% %d).toNat = ((((t : Int) - x) %% %d).toNat + 1) %% %d := by omega' % (N, N, N)),
    ('have e4 : (((t : Int) - (x + 1)) % 9).toNat = ((((t : Int) - x) % 9).toNat + 8) % 9 := by omega',
     'have e4 : (((t : Int) - (x + 1)) %% %d).toNat = ((((t : Int) - x) %% %d).toNat + %d) %% %d := by omega' % (N, N, N - 1, N)),
    ('/-- The background at column `A + i`, from the phases `tq = t mod 57` and `dq = (t - A) mod 9`. -/',
     '/-- The background at column `A + i`, from the phases `tq = t mod %d` and `dq = (t - A) mod %d`. -/' % (q, N)),
    ('def refAt (tq dq : Nat) (i : Int) : Bool := ringBit ((tq + 0) % 57) (((dq : Int) - i) % 9).toNat',
     'def refAt (tq dq : Nat) (i : Int) : Bool := ringBit ((tq + %d) %% %d) (((dq : Int) - i) %% %d).toNat' % (s, q, N)),
    ('theorem refAt_spec {t tq dq : Nat} {A : Int} (htq : tq = t % 57) (hdq : dq = (((t : Int) - A) % 9).toNat) (i : Int) :',
     'theorem refAt_spec {t tq dq : Nat} {A : Int} (htq : tq = t %% %d) (hdq : dq = (((t : Int) - A) %% %d).toNat) (i : Int) :' % (q, N)),
    ('def mask : Nat := 2 ^ 24 - 1', 'def mask : Nat := 2 ^ %d - 1' % W),
    ('/-- The background\'s 24 cells', '/-- The background\'s %d cells' % W),
    ('refAt tq dq ((i : Int) + 1)) 24', 'refAt tq dq ((i : Int) + 1)) %d' % W),
    ('/-- The window\'s 24 cells', '/-- The window\'s %d cells' % W),
    ('(if b then 2 ^ 23 else 0)', '(if b then 2 ^ %d else 0)' % (W - 1)),
    ('refAt ((tq + 1) % 57) ((dq + 1) % 9) 0', 'refAt ((tq + 1) %% %d) ((dq + 1) %% %d) 0' % (q, N)),
    ('((tq + 1) % 57, (dq + 2) % 9,', '((tq + 1) %% %d, (dq + 2) %% %d,' % (q, N)),
    ('((tq + 1) % 57, (dq + 1) % 9,', '((tq + 1) %% %d, (dq + 1) %% %d,' % (q, N)),
    ('def keyOf (tq dq m : Nat) : Nat := (tq * 9 + dq) * 2 ^ 24 + m', 'def keyOf (tq dq m : Nat) : Nat := (tq * %d + dq) * 2 ^ %d + m' % (N, W)),
    ('def decode (k : Nat) : Nat × Nat × Nat := (k / 2 ^ 24 / 9, k / 2 ^ 24 % 9, k % 2 ^ 24)',
     'def decode (k : Nat) : Nat × Nat × Nat := (k / 2 ^ %d / %d, k / 2 ^ %d %% %d, k %% 2 ^ %d)' % (W, N, W, N, W)),
    ('then -19 else 0) + 5', 'then -%d else 0) + %d' % (P, P - S)),
    ('its potential is `e.2 + 19 * motion + 5`', 'its potential is `e.2 + %d * motion + %d`' % (P, P - S)),
    ('/-- The start: phases `(15, 3)`', '/-- The start: phases `(%d, %d)`' % (tq0, dq0)),
    ('def startKey : Nat := 2321766113', 'def startKey : Nat := %d' % keys[0][0]),
    ('decide (-14 ≤ e.2) && decide (e.2 ≤ 22)', 'decide (%d ≤ e.2) && decide (e.2 ≤ %d)' % (lo_b, hi_b)),
    ('theorem and_mask_lt (a : Nat) : a &&& mask < 2 ^ 24', 'theorem and_mask_lt (a : Nat) : a &&& mask < 2 ^ %d' % W),
    ('mask.testBit i = decide (i < 24)', 'mask.testBit i = decide (i < %d)' % W),
    ('Nat.testBit_two_pow_sub_one 24 i', 'Nat.testBit_two_pow_sub_one %d i' % W),
    ('theorem restOf_bit {eA b : Bool} {m : Nat} (hm : m < 2 ^ 24) {i : Nat} (hi : i < 24) :',
     'theorem restOf_bit {eA b : Bool} {m : Nat} (hm : m < 2 ^ %d) {i : Nat} (hi : i < %d) :' % (W, W)),
    ('(if i = 23 then b else m.testBit (i + 1))', '(if i = %d then b else m.testBit (i + 1))' % (W - 1)),
    ('have h24 : m.testBit 24 = false :=', 'have h24 : m.testBit %d = false :=' % W),
    ('by_cases h23 : i = 23', 'by_cases h23 : i = %d' % (W - 1)),
    ('have hi23 : ¬ (23 = i)', 'have hi23 : ¬ (%d = i)' % (W - 1)),
    ('strip `m` holds the 24 cells right', 'strip `m` holds the %d cells right' % W),
    ('tq = t % 57 ∧ dq = (((t : Int) - A) % 9).toNat ∧ (∀ x, x ≤ A → G t x = E t x) ∧ m < 2 ^ 24 ∧',
     'tq = t %% %d ∧ dq = (((t : Int) - A) %% %d).toNat ∧ (∀ x, x ≤ A → G t x = E t x) ∧ m < 2 ^ %d ∧' % (q, N, W)),
    ('    ∀ i, i < 24 → m.testBit i = G t (A + 1 + i)', '    ∀ i, i < %d → m.testBit i = G t (A + 1 + i)' % W),
    ('G t (A + 25)', 'G t (A + %d)' % (W + 1)),
    ('G (t0 + n) (A + 25)', 'G (t0 + n) (A + %d)' % (W + 1)),
    ('have hcell : ∀ i, i < 24 →', 'have hcell : ∀ i, i < %d →' % W),
    ('(if i = 23 then G t', '(if i = %d then G t' % (W - 1)),
    ('have h : (2 : Nat) ^ 24 = 16777216 := rfl', 'have h : (2 : Nat) ^ %d = %d := rfl' % (W, 2 ** W)),
    ('((tq * 9 + dq) * 16777216 + m) / 16777216 = tq * 9 + dq', '((tq * %d + dq) * %d + m) / %d = tq * %d + dq' % (N, 2 ** W, 2 ** W, N)),
    ('((tq * 9 + dq) * 16777216 + m) % 16777216 = m', '((tq * %d + dq) * %d + m) %% %d = m' % (N, 2 ** W, 2 ** W)),
    ('have e3 : (tq * 9 + dq) / 9 = tq := by omega', 'have e3 : (tq * %d + dq) / %d = tq := by omega' % (N, N)),
    ('have e4 : (tq * 9 + dq) % 9 = dq := by omega', 'have e4 : (tq * %d + dq) %% %d = dq := by omega' % (N, N)),
    ('theorem decode_keyOf {tq dq m : Nat} (hdq : dq < 9) (hm : m < 2 ^ 24)', 'theorem decode_keyOf {tq dq m : Nat} (hdq : dq < %d) (hm : m < 2 ^ %d)' % (N, W)),
    ('(step tq dq m b).2.1 < 9', '(step tq dq m b).2.1 < %d' % N),
    ('`ψ0 + 19 (A - A0) + 5 n`', '`ψ0 + %d (A - A0) + %d n`' % (P, P - S)),
    ('(hdq0 : dq0 < 9)', '(hdq0 : dq0 < %d)' % N),
    ('Inv G (t0 + n) A tq dq m ∧ dq < 9 ∧', 'Inv G (t0 + n) A tq dq m ∧ dq < %d ∧' % N),
    ('ψ = ψ0 + 19 * (A - A0) + 5 * (n : Int)', 'ψ = ψ0 + %d * (A - A0) + %d * (n : Int)' % (P, P - S)),
    ('(hne : m ≠ refMask tq dq) : ∃ x, A < x ∧ x ≤ A + 24 ∧', '(hne : m ≠ refMask tq dq) : ∃ x, A < x ∧ x ≤ A + %d ∧' % W),
    ('have hi24 : i < 24 := by', 'have hi24 : i < %d := by' % W),
    ('Nat.testBit_lt_two_pow (Nat.lt_of_lt_of_le hm (Nat.pow_le_pow_right (by decide) (by omega)))\n    have h2',
     'Nat.testBit_lt_two_pow (Nat.lt_of_lt_of_le hm (Nat.pow_le_pow_right (by decide) (by omega)))\n    have h2'),
    ('simp [show ¬ i < 24 by omega]', 'simp [show ¬ i < %d by omega]' % W),
    ('show i < 24 from hi]', 'show i < %d from hi]' % W),
    ('/-- The start check at `t = 300`: columns `-300 .. -72` are the background, and columns `-71 .. -48` are the strip of',
     '/-- The start check at `t = 300`: columns `-300 .. %d` are the background, and columns `%d .. %d` are the strip of' % (A0, A0 + 1, A0 + W)),
    ('(List.range 229).all', '(List.range %d).all' % (A0 + 301)),
    ('(List.range 24).all (fun j => r.testBit (629 + j) == (startKey % 2 ^ 24).testBit j)',
     '(List.range %d).all (fun j => r.testBit (%d + j) == (startKey %% 2 ^ %d).testBit j)' % (W, A0 + 701, W)),
    ('(startKey % 2 ^ 24 != refMask 15 3) && (keyOf 15 3 (startKey % 2 ^ 24) == startKey)',
     '(startKey %% 2 ^ %d != refMask %d %d) && (keyOf %d %d (startKey %% 2 ^ %d) == startKey)' % (W, tq0, dq0, tq0, dq0, W)),
    ('theorem entry_inv : Inv Gedge 300 (-72) 15 3 (startKey % 2 ^ 24) ∧ startKey % 2 ^ 24 ≠ refMask 15 3 ∧\n    keyOf 15 3 (startKey % 2 ^ 24) = startKey := by',
     'theorem entry_inv : Inv Gedge 300 (%d) %d %d (startKey %% 2 ^ %d) ∧ startKey %% 2 ^ %d ≠ refMask %d %d ∧\n    keyOf %d %d (startKey %% 2 ^ %d) = startKey := by' % (A0, tq0, dq0, W, W, tq0, dq0, tq0, dq0, W)),
    ('have hx : lo + ((629 + i : Nat) : Int) = -72 + 1 + (i : Int)', 'have hx : lo + ((%d + i : Nat) : Int) = %d + 1 + (i : Int)' % (A0 + 701, A0)),
    ('have hk : closure.lookup (keyOf 15 3 (startKey % 2 ^ 24)) = some 0', 'have hk : closure.lookup (keyOf %d %d (startKey %% 2 ^ %d)) = some 0' % (tq0, dq0, W)),
    ('/-- **The front law of the inserted edge on the ring background `100100000` (temporal period 57).** For every `t ≥ 300`',
     '/-- **The front law of the inserted edge on the ring background `%s` (temporal period %d).** For every `t ≥ 300`' % (word, q)),
    ('there is an anchor `A` with the background intact at and left of `A`, a mismatch within the 24 cells right of it, and\n`-14 ≤ 19 (A + 72) + 5 (t - 300) ≤ 22`. So the leftmost difference moves left at exactly `5/19` cell per tick. -/',
     'there is an anchor `A` with the background intact at and left of `A`, a mismatch within the %d cells right of it, and\n`%d ≤ %d (A + %d) + %d (t - 300) ≤ %d`. So the leftmost difference moves left at exactly `%d/%d` cell per tick. -/' % (W, lo_b, P, -A0, P - S, hi_b, P - S, P)),
    ('    (∃ x, A < x ∧ x ≤ A + 24 ∧ Gedge t x ≠ E t x) ∧\n    -14 ≤ 19 * (A + 72) + 5 * ((t : Int) - 300) ∧ 19 * (A + 72) + 5 * ((t : Int) - 300) ≤ 22 := by',
     '    (∃ x, A < x ∧ x ≤ A + %d ∧ Gedge t x ≠ E t x) ∧\n    %d ≤ %d * (A + %d) + %d * ((t : Int) - 300) ∧ %d * (A + %d) + %d * ((t : Int) - 300) ≤ %d := by' % (W, lo_b, P, -A0, P - S, P, -A0, P - S, hi_b)),
]
for old, new in reps:
    assert old in body, 'pattern not found: ' + old[:70]
    body = body.replace(old, new)
out = head + data + body
out = out.replace('namespace Ruliology.CellularAutomata.Rule30MovingWall', 'namespace Ruliology.CellularAutomata.' + ns)
out = out.replace('end Ruliology.CellularAutomata.Rule30MovingWall', 'end Ruliology.CellularAutomata.' + ns)
open(sys.argv[3], 'w').write(out)
print('wrote %s: %d lines' % (sys.argv[3].rsplit('/', 1)[-1], out.count('\n')))
