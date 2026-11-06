#!/usr/bin/env python3
"""Control for S-03: each mutation of a statement in the portal form must fail to compile, or that piece carries no weight.
Run from a built kit root: first_checks_mutate.py SOURCE ROOT. Prediction: all rejected.
Counterfactual: a mutant compiles; then the essay's account of that piece is wrong."""
import subprocess, sys
src = open(sys.argv[1], encoding='utf-8').read()
root = sys.argv[2]
M = [
 ('two tick: or becomes and', '((zrow L 0 (j + 1) || zrow L 0 j) && !(xor (zrow L 0 (j + 3)) (zrow L 0 (j + 2)))) := by', '((zrow L 0 (j + 1) && zrow L 0 j) && !(xor (zrow L 0 (j + 3)) (zrow L 0 (j + 2)))) := by'),
 ('two tick: negation dropped', '((zrow L 0 (j + 1) || zrow L 0 j) && !(xor (zrow L 0 (j + 3)) (zrow L 0 (j + 2)))) := by', '((zrow L 0 (j + 1) || zrow L 0 j) && (xor (zrow L 0 (j + 3)) (zrow L 0 (j + 2)))) := by'),
 ('four bools: constant 2', '      1 + c.toNat := by\n  revert c u v0 v1 w0 w1', '      2 + c.toNat := by\n  revert c u v0 v1 w0 w1'),
 ('four bools: check dropped', '      1 + c.toNat := by\n  revert c u v0 v1 w0 w1', '      1 := by\n  revert c u v0 v1 w0 w1'),
 ('pair law: no constant term', 'theorem pair_count (m : Nat) : flips (m + 1) = 2 ^ m + ones m := by', 'theorem pair_count (m : Nat) : flips (m + 1) = ones m := by'),
 ('pair law: wrong index', 'theorem pair_count (m : Nat) : flips (m + 1) = 2 ^ m + ones m := by', 'theorem pair_count (m : Nat) : flips (m + 1) = 2 ^ m + ones (m + 1) := by'),
 ('adjacent: stronger left side', 'theorem adjacent (m : Nat) : 2 ^ m + ones m ≤ gap (m + 2) + 2 * gap (m + 1) := by', 'theorem adjacent (m : Nat) : 2 ^ m + ones m + 1 ≤ gap (m + 2) + 2 * gap (m + 1) := by'),
 ('distance two: 23 for 24', 'theorem distance_two (m : Nat) : 2 ^ (m + 2) ≤ 4 * gap (m + 4) + 24 * gap (m + 2) := by', 'theorem distance_two (m : Nat) : 2 ^ (m + 2) ≤ 4 * gap (m + 4) + 23 * gap (m + 2) := by'),
 ('near constant at 39', 'def Bad (n : Nat) : Prop := 40 * gap n < 2 ^ n', 'def Bad (n : Nat) : Prop := 39 * gap n < 2 ^ n'),
 ('first check counts ones', 'theorem first_check_count (n : Nat) : firstCheck n + ones n = 2 ^ n := by', 'theorem first_check_count (n : Nat) : firstCheck n = ones n := by'),
 ('last cell black', '  | 0, l => if ok (l ++ [false]) then 1 else 0', '  | 0, l => if ok (l ++ [true]) then 1 else 0'),
]
base = subprocess.run(['lake', 'env', 'lean', '/dev/stdin'], input=src.encode(), cwd=root, capture_output=True)
print('unmutated', 'compiles' if base.returncode == 0 else 'FAILS: ' + base.stdout.decode()[:300])
bad = 0
for name, a, b in M:
    assert src.count(a) == 1, name
    r = subprocess.run(['lake', 'env', 'lean', '/dev/stdin'], input=src.replace(a, b).encode(), cwd=root, capture_output=True)
    ok = r.returncode != 0
    bad += not ok
    print(('rejected  ' if ok else 'COMPILES  ') + name, flush=True)
print('rejected', len(M) - bad, 'of', len(M))
sys.exit(1 if bad or base.returncode else 0)
