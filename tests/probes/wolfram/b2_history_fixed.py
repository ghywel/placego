#!/usr/bin/env python3
"""GC2521: TWO FIXED B2 contexts, no search or adjustable horizon.

RUN-ON: cpu, one Python process/thread, no subprocesses or network.
COMMAND: run_capped.py [frozen limits] -- nice -n 10 python3 b2_history_fixed.py
Requires CAPPED_OUT. The literal 8-entry physical rule is independent of the
edge-coordinate update and its three polynomial-response streams.
Prediction and caps: reports/GPT-B2-FIXED-CONTEXT-PILOT-20261103.md.
"""
import hashlib
import json
import os
from pathlib import Path
import sys
import time

assert len(sys.argv) == 1, "fixed probe has no adjustable parameters"
OUT = Path(os.environ["CAPPED_OUT"])
assert OUT.is_dir()
START_CPU = time.process_time()
START_WALL = time.monotonic()
RULE = (0, 1, 1, 1, 1, 0, 0, 0)
SEED = 0x889DA3
CASES = (
    dict(name="j5_hand_control", j=5, r=3, P=2, T=8, lo=1, hi=2),
    dict(name="j14_fixed_test", j=14, r=12, P=64, T=256, lo=10, hi=11),
)
checked_cells = 0


def budget():
    if time.process_time() - START_CPU > 5 or time.monotonic() - START_WALL > 15:
        raise RuntimeError("fixed probe internal CPU/wall stop")


def coefficients(a, b, ua, va, za, ub, vb, zb):
    p = ((1 ^ b) & ua) ^ ((1 ^ a) & ub) ^ (ua & ub)
    q = ((1 ^ b) & va) ^ ((1 ^ a) & vb) ^ (va & vb)
    z = ((1 ^ b) & za) ^ ((1 ^ a) & zb)
    z ^= (ua & vb) ^ (va & ub) ^ (ua & zb) ^ (za & ub)
    z ^= (va & zb) ^ (za & vb) ^ (za & zb)
    return p, q, z


def parity(v):
    return sum(v) & 1


def physical(seed, T, j):
    """Literal rows with two white halo cells outside the whole seed cone."""
    first = -(seed.bit_length() - 1) - T - 2
    last = T + 2
    row = [0] * (last - first + 1)
    for k in range(seed.bit_length()):
        row[-k - first] = (seed >> k) & 1
    rows = []
    for t in range(T + 1):
        budget()
        rows.append([row[t - i - first] for i in range(j + 1)])
        if t < T:
            nxt = [0] * len(row)
            for x in range(1, len(row) - 1):
                nxt[x] = RULE[(row[x - 1] << 2) | (row[x] << 1) | row[x + 1]]
            row = nxt
    return rows


def response(case):
    j, T = case["j"], case["T"]
    mask = (1 << (j + 1)) - 1
    x = SEED & mask
    u = [int(i == case["lo"]) for i in range(j + 1)]
    v = [int(i == case["hi"]) for i in range(j + 1)]
    z = [0] * (j + 1)
    base, us, vs, zs, forces = [], [], [], [], []
    for t in range(T + 1):
        budget()
        b = [(x >> i) & 1 for i in range(j + 1)]
        base.append(b)
        us.append(u[:]); vs.append(v[:]); zs.append(z[:])
        c = []
        for i in range(j + 1):
            def at(a, k):
                return a[k] if k >= 0 else 0
            c.append(coefficients(at(b, i - 1), at(b, i - 2),
                                  at(u, i - 1), at(v, i - 1), at(z, i - 1),
                                  at(u, i - 2), at(v, i - 2), at(z, i - 2)))
        forces.append(c)
        u = [u[i] ^ c[i][0] for i in range(j + 1)]
        v = [v[i] ^ c[i][1] for i in range(j + 1)]
        z = [z[i] ^ c[i][2] for i in range(j + 1)]
        x = (x ^ ((x << 1) | (x << 2))) & mask
    return base, us, vs, zs, forces


def bits_equal(rows, t, i):
    return rows[t][:i + 1] == rows[0][:i + 1]


def least_dyadic_prefix(rows, i):
    p = 1
    while p < len(rows):
        if bits_equal(rows, p, i):
            return p
        p *= 2
    raise AssertionError("fixed baseline horizon did not include prefix return")


def matches_period(rows, i, P):
    return bits_equal(rows, P, i) and (P == 1 or not bits_equal(rows, P // 2, i))


def run_case(case):
    global checked_cells
    j, r, P, T = (case[k] for k in ("j", "r", "P", "T"))
    base, us, vs, zs, force = response(case)
    oracle = {}
    for beta in (0, 1):
        for gamma in (0, 1):
            label = f"{beta}{gamma}"
            seed = SEED ^ (beta << case["lo"]) ^ (gamma << case["hi"])
            rows = physical(seed, T, j)
            oracle[label] = rows
            for t in range(T + 1):
                for i in range(j + 1):
                    pred = base[t][i] ^ (beta & us[t][i]) ^ (gamma & vs[t][i])
                    pred ^= beta & gamma & zs[t][i]
                    assert pred == rows[t][i], (case["name"], label, t, i, pred, rows[t][i])
                    checked_cells += 1
    periods = [least_dyadic_prefix(oracle["00"], i) for i in range(j + 1)]
    assert periods[r - 2:r + 1] == [P, P, P]
    assert periods[j - 1] == 2 * P
    assert [periods[j - k] // periods[j - k - 1] - 1 for k in (1, 2, 3)] == [1, 0, 0]
    flags = [None] + [periods[i] // periods[i - 1] - 1 for i in range(1, j + 1)]
    # This exact word100 descent has c=10, K=0. Both pairing/integration totals vanish.
    assert (P % 2) == 0
    w = [int(t % 2 == 0) for t in range(P)]
    U = [base[t][r - 3] for t in range(P)]
    V = [base[t][r - 2] for t in range(P)]
    W = [base[t][r - 1] for t in range(P)]
    h, acc = [], 0
    for bit in U:
        h.append(acc); acc ^= 1 ^ bit
    weighted = lambda a: parity([w[t] & a[t] for t in range(P)])
    S = parity(w)
    Aw = weighted([1 ^ W[t] ^ (V[t] & h[t]) for t in range(P)])
    Bw = weighted([1 ^ V[t] for t in range(P)])
    alpha = parity(U)
    A = parity([W[t] ^ (V[t] & h[t]) for t in range(P)])
    B = parity(V)
    F = weighted([V[t] | W[t] for t in range(P)])
    assert F == flags[j], "baseline weighted leaf did not reproduce retained target"
    history_coeff = {}
    for i in range(1, j + 1):
        oldP = periods[i - 1]
        assert oldP <= T
        history_coeff[i] = tuple(parity([force[t][i][q] for t in range(oldP)]) for q in range(3))
    variants = []
    for beta in (0, 1):
        for gamma in (0, 1):
            label = f"{beta}{gamma}"; rows = oracle[label]
            failed = [i for i in range(1, j) if not matches_period(rows, i, periods[i])]
            bad_pred = [i for i in range(1, j) if (beta & history_coeff[i][0]) ^
                        (gamma & history_coeff[i][1]) ^ (beta & gamma & history_coeff[i][2])]
            # Only the FIRST failed guard has a new-growth interpretation on the old period.
            assert (failed[0] if failed else None) == (bad_pred[0] if bad_pred else None)
            full_history = not failed
            local_pred = not ((beta & alpha) or ((beta & A) ^ (gamma & B)))
            local_real = matches_period(rows, r - 1, P) and matches_period(rows, r, P)
            assert local_pred == local_real
            Fnew = weighted([rows[t][r - 2] | rows[t][r - 1] for t in range(P)])
            Fpred = F ^ (beta & Aw) ^ (gamma & Bw) ^ (beta & gamma & S)
            assert Fnew == Fpred
            target = None
            if full_history:
                if bits_equal(rows, periods[j - 1], j): target = 0
                else:
                    assert bits_equal(rows, 2 * periods[j - 1], j)
                    target = 1
                p, q, zz = history_coeff[j]
                assert target == flags[j] ^ (beta & p) ^ (gamma & q) ^ (beta & gamma & zz)
                assert target == Fnew
            variants.append(dict(choice=label, full_history=full_history, local00=local_real,
                                 first_failed_depth=failed[0] if failed else None,
                                 weighted_value=Fnew, target_flag_only_if_history_preserved=target))
    return dict(case=case, baseline_periods=periods, baseline_flags=flags,
                local_coeff=dict(alpha=alpha, A=A, B=B), weighted_coeff=dict(S=S, A=Aw, B=Bw),
                history_coeff=history_coeff, variants=variants,
                oracle_profiles={key:[sum(b << i for i,b in enumerate(row)) for row in rows]
                                 for key,rows in oracle.items()})


# Adversarial algebra control over every 8-bit coefficient/base assignment.
poly_controls = 0; dropped_zz_failures = 0
for code in range(256):
    a,b,ua,va,za,ub,vb,zb = [(code >> i) & 1 for i in range(8)]
    p,q,z = coefficients(a,b,ua,va,za,ub,vb,zb)
    for beta in (0,1):
        for gamma in (0,1):
            an = a ^ (beta & ua) ^ (gamma & va) ^ (beta & gamma & za)
            bn = b ^ (beta & ub) ^ (gamma & vb) ^ (beta & gamma & zb)
            direct = (a | b) ^ (an | bn)
            pred = (beta & p) ^ (gamma & q) ^ (beta & gamma & z)
            assert pred == direct
            dropped_zz_failures += int((pred ^ (beta & gamma & za & zb)) != direct)
            poly_controls += 1
assert dropped_zz_failures > 0, "negative algebra control failed to detect missing product"
result = dict(source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              poly_controls=poly_controls, dropped_zz_negative_failures=dropped_zz_failures, cases=[])
for case in CASES:
    result["cases"].append(run_case(case))
    (OUT / "results.json").write_text(json.dumps(result,sort_keys=True,indent=2)+'\n')
small,large = result["cases"]
assert [v["choice"] for v in small["variants"] if v["full_history"]] == ["00"]
assert small["variants"][3]["local00"] and not small["variants"][3]["full_history"]
assert small["weighted_coeff"] == dict(S=1,A=1,B=0)
# Deliberately deleting the mixed mask term must miss choice11 in the hand control.
assert small["variants"][3]["weighted_value"] != (1 ^ 1)
result.update(checked_cells=checked_cells,cpu_seconds=time.process_time()-START_CPU,
              wall_seconds=time.monotonic()-START_WALL,status="FIXED_B2_CONTROLS_PASS")
(OUT / "results.json").write_text(json.dumps(result,sort_keys=True,indent=2)+'\n')
for case in result["cases"]:
    print(case["case"]["name"], json.dumps({k:v for k,v in case.items() if k!='oracle_profiles'},sort_keys=True))
print("B2_FIXED_DONE",json.dumps({k:v for k,v in result.items() if k!='cases'},sort_keys=True))
