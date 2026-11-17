"""rule30_audit_g58.py: Local's check of GPT's G58 (one-parity walls: an explicit empty-left witness for Rule 210) and
its periodic-input addendum, the second reader's companion to an argument audit, independent of GPT's OP controls.
For random odd-time inputs a (periodic and aperiodic, with holes) it evolves the left half from an empty row under
Rule 210's own truth table (not Rule 90), with the wall tau(even) = 0, tau(2m+1) = a_m, and checks: the parity
invariant (no black cell with t + k even), the wall equation tau(t+1) = f(pi, tau, sigma) at every time with
sigma(t) = tau(t+1) xor pi(t), sigma(odd) = 0, and the dyadic filter pi(2n) = xor of a_(n - 2^r) over 2^r <= n. The
Rule 30 counterfactual must fail. (Local, 2026-10-06; PROOFS.md G58 note; chat L033.)

COMMAND:    python3 tests/probes/lexicon/rule30_audit_g58.py      (seconds)
OUTCOME, 2026-10-06: ALL CHECKS PASS (200 inputs, 0 failures; the Rule 30 counterfactual violates 199 times).
"""
import random
random.seed(20261006)
R210 = lambda l, c, r: l ^ r ^ (c & r)
R30 = lambda l, c, r: l ^ (c | r)


def run(a, T, rule):
    K = T + 3
    u = [0] * (K + 1)                     # u[k] = column -k, u[0] = the wall
    tau = lambda t: 0 if t % 2 == 0 else a[(t - 1) // 2]
    u[0] = tau(0)
    bad = 0; pis = []; sig = []
    for t in range(T):
        pi = u[1]; s = tau(t + 1) ^ pi
        pis.append(pi); sig.append(s)
        bad += rule(pi, tau(t), s) != tau(t + 1)                     # the wall's own update
        bad += any(u[k] for k in range(1, K) if (t + k) % 2 == 0)   # parity invariant (left cells)
        new = [0] * (K + 1)
        for k in range(1, K):
            new[k] = rule(u[k + 1], u[k], u[k - 1])                  # l = column -(k+1), r = column -(k-1)
        new[0] = tau(t + 1); u = new
    return bad, pis, sig


fails = 0; n_inputs = 0
for trial in range(200):
    T = 160
    if trial % 2:
        q = random.choice([1, 2, 3, 4, 5, 7]); base = [random.randint(0, 1) for _ in range(q)]
        if not any(base): base[0] = 1
        a = [base[m % q] for m in range(T)]
    else:
        a = [random.randint(0, 1) for _ in range(T)]
    bad, pis, sig = run(a, T, R210)
    fails += bad
    fails += any(sig[t] for t in range(1, T, 2))                       # sigma(odd) = 0
    for n in range(T // 2):
        filt = 0; r = 0
        while 2 ** r <= n: filt ^= a[n - 2 ** r]; r += 1
        fails += pis[2 * n] != filt
    n_inputs += 1
cf_bad, _, _ = run([1] * 160, 160, R30)
print("G58:", n_inputs, "inputs (half periodic with periods 1..7, half random), T = 160: failures", fails,
      "; Rule 30 counterfactual violations", cf_bad, "(must be > 0)")
print("ALL CHECKS PASS" if fails == 0 and cf_bad > 0 else "CHECK FAILED")
