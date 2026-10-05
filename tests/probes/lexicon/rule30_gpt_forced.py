#!/usr/bin/env python3
"""Forced-zero diagnostics: an exact parity identity and conditional survival.

RUN-ON: CPU, Python standard library; four independent depths in four processes.
COMMAND: python3 tests/probes/lexicon/rule30_gpt_forced.py
COST: about minutes, modest memory. C control compiled serially in temporary storage.
READ FIRST: RULE30-PRIZE.md sections 8.2, 8.37, 8.38 and 8.41;
RULE30-GPT.md G3. This is a diagnostic, not a new record search or prize proof.

PREDICTIONS, written before first run, 2026-10-06:
FZ0 (controls, must hold): parity formula agrees with cellwise inverse reconstruction
    for 100 random column-1 words, every depth to 64. The exhaustive depth-21
    forced-walk histogram (all 1024 prefixes) equals freshly compiled records.c.
FZ1 (blind): at depths 65,129,257,513, among 20000 independently sampled uniform
    visible prefixes at each depth (fixed seeds 30000+d), the chance of passing
    each of the first eight forced tests is in [0.35,0.65] when at least 100
    prefixes reached that test. Samples are prefix-weighted, not distinct walks.
FZ2 (counterfactual, must be rejected): the three parity bits alone close the
    zero-forcing dynamics. At even depths 22 and 66 find two realised prefix
    states with the same summary and current forced output 0, but opposite
    outputs at the next forced test after a zero-forced free step. Exhaust all
    2048 prefixes at 22; sample 20000 prefixes at 66 (fixed seed 31066).
CF (must be rejected): removing the AND-overlap parity leaves the output formula
    correct. At least one FZ0 cell must differ without that term.
REFUTED-BY: a control or counterfactual failure invalidates the intended diagnostic;
    FZ1 outside its band refutes that empirical prediction only.
OUTCOME: not yet run.
"""
import concurrent.futures
import collections
import pathlib
import random
import subprocess
import tempfile


def parity(v):
    return v.bit_count() & 1


def summary(p, q):
    return parity(p), parity(q), parity(p & (q << 1))


def predicted(p, q, c, k, overlap=True):
    a, b, z = summary(p, q)
    return (k & 1) ^ a ^ b ^ (z if overlap else 0) ^ (c if k & 1 else 0)


def diag(p, q, c, k):
    v = (p << 1) | (q << 2) | (c << 1)
    v = (v & ~1) | (k & 1)
    shift = 1
    while shift <= k:
        v ^= v << shift
        shift *= 2
    return v & ((2 << k) - 1)


def state(prefix, d):
    p, q = 0, 0
    for k in range(1, d):
        c = (prefix >> ((k - 1) // 2)) & 1 if k & 1 else 0
        p, q = diag(p, q, c, k), p
    return p, q


def zero_step(p, q, k):
    c = predicted(p, q, 0, k) if k & 1 else 0
    v = diag(p, q, c, k)
    return v, p, (v >> k) & 1


def walk(prefix, d, cap=256):
    p, q = state(prefix, d)
    for k in range(d, d + cap):
        p, q, cell = zero_step(p, q, k)
        if cell:
            return k - d
    raise RuntimeError('censored control walk; cannot call cap a finite record')


def controls():
    rng = random.Random(301)
    okay, rejected = True, False
    for _ in range(100):
        sigma = [rng.randrange(2) for _ in range(64)]
        far, right = sigma, [t & 1 for t in range(65)]
        cells = []
        for k in range(1, 65):
            left = [right[t+1] ^ (right[t] | far[t]) for t in range(len(right)-1)]
            cells.append(left[0])
            far, right = right, left
        p, q = 0, 0
        for k in range(1, 65):
            c = sigma[k-1]
            v = diag(p, q, c, k)
            okay &= predicted(p, q, c, k) == cells[k-1] == ((v >> k) & 1)
            rejected |= predicted(p, q, c, k, overlap=False) != cells[k-1]
            p, q = v, p
    here = pathlib.Path(__file__).resolve().parent
    with tempfile.TemporaryDirectory(prefix='rule30-gpt-forced-') as tmp:
        exe = pathlib.Path(tmp) / 'records'
        subprocess.run(['cc', '-O2', '-o', str(exe), str(here / 'records.c')], check=True)
        out = subprocess.check_output([str(exe), '21', '1'], text=True)
    known = {int(f.split()[2]): int(f.split()[3]) for f in out.splitlines() if f.startswith('H ')}
    mine = dict(collections.Counter(walk(prefix, 21) for prefix in range(1024)))
    print('FZ0 histogram', sorted(mine.items()), flush=True)
    print('PASS FZ0' if okay and known == mine else 'FAIL FZ0', flush=True)
    print('PASS CF overlap omission rejected' if rejected else 'FAIL CF', flush=True)
    return okay and known == mine and rejected


def closure(d):
    rng = random.Random(31000 + d)
    prefixes = range(2048) if d == 22 else [rng.getrandbits((d-1+1)//2) for _ in range(20000)]
    seen = {}
    for prefix in prefixes:
        p, q = state(prefix, d)
        key = summary(p, q)
        if predicted(p, q, 0, d):
            continue
        p, q, cell = zero_step(p, q, d)
        assert cell == 0
        p, q, cell = zero_step(p, q, d+1)
        assert cell == 0
        future = predicted(p, q, 0, d+2)
        if key in seen and seen[key][0] != future:
            other = seen[key][1]
            print(f'PASS FZ2 depth {d}: summary {key}; prefixes {other}, {prefix}; next forced outputs {seen[key][0]}, {future}', flush=True)
            return True
        seen.setdefault(key, (future, prefix))
    print(f'FAIL FZ2 depth {d}: no witness in the stipulated population', flush=True)
    return False


def sample(d):
    rng = random.Random(30000+d)
    reached, passed = [0]*8, [0]*8
    for _ in range(20000):
        prefix = rng.getrandbits((d-1)//2)
        p, q = state(prefix, d)
        test = 0
        for k in range(d, d+16):
            p, q, cell = zero_step(p, q, k)
            if not k & 1:
                reached[test] += 1
                passed[test] += not cell
                test += 1
                if cell:
                    break
    okay = all(n < 100 or .35 <= z/n <= .65 for n,z in zip(reached,passed))
    return d, reached, passed, okay


def main():
    okay = controls()
    okay &= closure(22)
    okay &= closure(66)
    with concurrent.futures.ProcessPoolExecutor(max_workers=4) as pool:
        for d,n,z,held in pool.map(sample, [65,129,257,513]):
            print(f'{"HELD" if held else "REFUTED"} FZ1 depth {d}: reached {n}; passed {z}; fractions {[round(a/b,4) for a,b in zip(z,n)]}', flush=True)
    print('ALL CONTROLS PASS' if okay else 'CONTROL FAILURE', flush=True)
    return not okay


if __name__ == '__main__':
    raise SystemExit(main())
