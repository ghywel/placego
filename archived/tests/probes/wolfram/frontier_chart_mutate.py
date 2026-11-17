#!/usr/bin/env python3
"""Control for S-01: each mutation of a statement or definition in the portal form must fail to compile, or it would show the
proof does not depend on that piece. Run from a built kit root: frontier_chart_mutate.py SOURCE KIT_LEAN_DIR. Prediction: all rejected.
Counterfactual: a mutant compiles; then that piece carries no weight and the essay's account of it is wrong."""
import os, subprocess, sys, tempfile
src = open(sys.argv[1], encoding='utf-8').read()
root = sys.argv[2]
M = [
 ('wall or becomes and', 'chart fr (τ + 1) 0 = xor (chart fr τ 1) (chart fr τ 0 || false) := by', 'chart fr (τ + 1) 0 = xor (chart fr τ 1) (chart fr τ 0 && false) := by'),
 ('wall from time zero', '(hτ : 1 ≤ τ) :\n    chart fr (τ + 1) 0', '(hτ : 0 ≤ τ) :\n    chart fr (τ + 1) 0'),
 ('interior or becomes and', 'xor (chart fr τ (e + 2)) (chart fr τ (e + 1) || chart fr τ e) := by', 'xor (chart fr τ (e + 2)) (chart fr τ (e + 1) && chart fr τ e) := by'),
 ('interior drops the deep cell', 'xor (chart fr τ (e + 2)) (chart fr τ (e + 1) || chart fr τ e) := by', 'xor (chart fr τ (e + 1)) (chart fr τ (e + 1) || chart fr τ e) := by'),
 ('low bit at the wrong parity', 'if (τ + e) % 2 = 0 then (atDepth (fr ((τ + e) / 2)) e).1\n  else (atDepth (fr ((τ + e + 1) / 2)) e).2', 'if (τ + e) % 2 = 0 then (atDepth (fr ((τ + e) / 2)) e).2\n  else (atDepth (fr ((τ + e + 1) / 2)) e).1'),
 ('recurrence high part uses the wrong row', '(xor (atDepth w2 (e + 1)).1 ((atDepth w2 (e + 1)).2 || (atDepth w e).1),', '(xor (atDepth w2 (e + 1)).1 ((atDepth w2 (e + 1)).2 || (atDepth w (e + 1)).1),'),
 ('recurrence low part uses the wrong row', 'xor (atDepth w2 (e + 1)).2 ((atDepth w (e + 1)).1 || (atDepth w e).2)) := by', 'xor (atDepth w2 (e + 1)).2 ((atDepth w e).1 || (atDepth w e).2)) := by'),
 ('start at time one', 'def start (fr : Nat → List Sym) (k : Nat) : Bool := chart fr 2 (k - 1)', 'def start (fr : Nat → List Sym) (k : Nat) : Bool := chart fr 1 (k - 1)'),
 ('nonempty hypothesis dropped from the wall', 'theorem chart_wall (hZ : ∀ n, Z (fr n) = some (fr (n + 1), s n)) (h0 : fr 0 ≠ []) (τ : Nat)', 'theorem chart_wall (hZ : ∀ n, Z (fr n) = some (fr (n + 1), s n)) (τ : Nat)'),
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
