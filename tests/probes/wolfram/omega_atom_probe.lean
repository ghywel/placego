/-! L1166 probe (Local): does core `omega` identify `q (n+1+1)` with `q (n+2)`? Prediction: the first example FAILS
(its two applications are different atoms) and the second, with the `show` fix, PASSES. Core Lean only. -/
example (q : Nat → Nat) (n : Nat) (h : q (n+2) = q n + 1) : q n ≤ q (n+1+1) := by omega
example (q : Nat → Nat) (n : Nat) (h : q (n+2) = q n + 1) : q n ≤ q (n+1+1) := by show q n ≤ q (n+2); omega
