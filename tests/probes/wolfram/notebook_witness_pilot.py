#!/usr/bin/env python3
"""L1029: witness-by-simulation pilot for GC1979's blocked short-word gate, revised per GC1980.

Local, 2026-10-27. Source for GPT's review; it runs only after GPT freezes it, under run_capped.py (CAPPED_OUT set).
No solver is called. Conventions are GC1977's: visible index j is physical time 2j, the wall is x(t,0) = t mod 2,
and the right cone starts at cells 1 .. H+1.

Question. Is E_34^8 = E_100^8 for the right-half language beside the clamped alternating wall? Each word in the
initial length-8 language L8 (36 words, from the committed MFW list, as in notebook_death_search.languages) gets one
of three verdicts:
  - EXCLUDED: a factor among the reproduced death controls forbids it from an age at most 34 (offset rule
    d(w) <= d(v) - k). GPT's GC1980 table gives exactly 5 such words.
  - WITNESSED_100: a sampled initial row whose evolution shows w at visible age 100. Every such row is replayed
    with GC1977's literal-table evaluator (notebook_death_gate.replay).
  - UNRESOLVED: anything else. A sample with no hit is NOT evidence of absence (GC1980 section 2).
If every word is EXCLUDED or WITNESSED_100, nestedness gives E_34^8 = E_100^8, and the gate passes. Otherwise the
gate stays incomplete, and this pilot reports which words remain.

Sampling, frozen. N_MAX = 200000 rows. PRNG: Python's random.Random(SEED) (Mersenne Twister), SEED = 1976.
Each row is getrandbits(215); bit i of the integer is cell i + 1. Rows are drawn in order with no batching. The
seed is never changed and no draws are added after looking. The run stops early only when every TARGET (L8 minus
EXCLUDED) is WITNESSED_100. The actual draw count is retained.

Cone, frozen (GC1980 section 3). n = 8, J_MAX = 100, H = 2(J_MAX + n - 1) = 214. Input width 215 = H + 1. A shrinking
cone of 214 updates; the top cell is dropped at each step, so no zero-tail or wrap assumption enters.

Predictions, written before any run.
  P_A (instrument). The fast simulator agrees with the literal evaluator on every one of the 2^12 tiny cones for 11
      steps. The retained GC1978 age-100 witness for 00001000 replays to 00001000 at age 100 in both. No EXCLUDED
      word is ever observed at an age at or above its bound. Any failure stops the run: an instrument error, not
      mathematics.
  P_B (witnesses). The gate will NOT complete. Submission R30-20261027-230bc7 reports that about 96% of random finite
      right halves enter a trap where consecutive visible black cells are 3 or 5 apart, and the others become
      eventually periodic. Uniform rows should therefore witness at age 100 mainly the 12 targets whose internal
      1-distances are all 3 or 5, and leave most of the other 19 targets (those with a distance 2 or 4) UNRESOLVED.
      Gut confidence: about 70%.
  Counterfactual. If random sampling witnesses at age 100 a large share (say 10 or more) of the 19
      non-trap-rhythm targets, uniform rows escape that rhythm far more often than the trap report suggests. If all
      31 targets are witnessed, the gate passes outright.
  What a miss means. UNRESOLVED words are ranked by their latest sampled age, for a later exact, frozen query. No
      death is inferred.

Retained in CAPPED_OUT/artifacts: language.json, controls.json, summary.json (draws, per-word verdict and latest
sampled age, PRNG details, source SHA256) and witnesses.json (one replayed age-100 row per witnessed word, as a
bitstring of 215 cells, with its visible trace).
"""
import hashlib
import json
import os
import random
import resource
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import notebook_death_gate as gate  # GC1977's literal-table evaluator (replay)

N_MAX = 200000
SEED = 1976
NWORD = 8
J_MAX = 100
H = 2 * (J_MAX + NWORD - 1)          # 214
WIDTH = H + 1                        # 215
MFW = Path(__file__).resolve().parents[1] / 'lexicon/rule30_local_mfw44.txt'
DEATHS = {'0010001': 32, '1000101': 34}   # reproduced in GC1977 (first impossible visible start)
# GC1978 q00002: SAT witness for 00001000 at visible start 100, replayed there (zero tail beyond 215 cells).
CONTROL_ROW = ('01101011010011011111011101110111110101101101000100001011000011010000111110111000101010001101111010011'
               '011011101110110011111010110011101101011110001111110000010101011011100000101001100101000111010100100'
               '100000001110110')


def language8():
    text = MFW.read_text().split('## phase 1')[0]
    forbidden = [x.strip() for x in text.splitlines() if x.strip() and set(x.strip()) <= set('01')]
    L = ['']
    for n in range(1, NWORD + 1):
        L = [w + b for w in L for b in '01' if not any((w + b).endswith(f) for f in forbidden if len(f) <= n)]
    assert len(L) == 36, len(L)
    return L, hashlib.sha256(MFW.read_bytes()).hexdigest()


def exclusions(L):
    out = {}
    for w in L:
        for v, d in DEATHS.items():
            for k in range(len(w) - len(v) + 1):
                if w[k:k + len(v)] == v:
                    out[w] = min(out.get(w, 10 ** 9), d - k)
    return out


def visible_fast(bits_int, width, steps):
    """Fast shrinking-cone evolution on an integer (bit i = cell i+1). Returns column 1 at even times 0..steps."""
    R = bits_int
    vis = []
    for t in range(steps + 1):
        if t % 2 == 0:
            vis.append(R & 1)
        if t == steps:
            break
        new = (((R << 1) | (t & 1)) ^ (R | (R >> 1)))
        width -= 1
        R = new & ((1 << width) - 1)
    return vis


def visible_literal(bits_list, steps):
    hist = gate.replay(bits_list, steps)
    return [hist[t][0] for t in range(0, steps + 1, 2)]


def row_bits(x, width):
    return [(x >> i) & 1 for i in range(width)]


def tiny_cross_check():
    count = 0
    for x in range(1 << 12):
        bits = row_bits(x, 12)
        hist = gate.replay(bits, 11)
        R, w = x, 12
        for t in range(11):
            assert [(R >> i) & 1 for i in range(w)] == hist[t], (x, t)
            new = (((R << 1) | (t & 1)) ^ (R | (R >> 1)))
            w -= 1
            R = new & ((1 << w) - 1)
        assert [(R >> i) & 1 for i in range(w)] == hist[11]
        count += 1
    return count


def main():
    root = Path(os.environ['CAPPED_OUT']) / 'artifacts'
    root.mkdir(exist_ok=False)
    started = time.monotonic()
    src = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    L, mfw_sha = language8()
    excl = exclusions(L)
    targets = [w for w in L if w not in excl]
    (root / 'language.json').write_text(json.dumps(dict(L8=L, mfw_sha256=mfw_sha, excluded=excl,
                                                        targets=targets), indent=1))
    # ---- controls (P_A)
    tiny = tiny_cross_check()
    ctrl_int = sum(int(c) << i for i, c in enumerate(CONTROL_ROW))
    assert len(CONTROL_ROW) == WIDTH
    vf = visible_fast(ctrl_int, WIDTH, H)
    vl = visible_literal([int(c) for c in CONTROL_ROW], H)
    assert vf == vl, 'fast and literal disagree on the control row'
    assert ''.join(map(str, vl[J_MAX:J_MAX + NWORD])) == '00001000', 'positive control failed'
    (root / 'controls.json').write_text(json.dumps(dict(tiny_cones=tiny, positive_control='00001000@100 replayed',
                                                        passed=True), indent=1))
    # ---- sampling (P_B)
    rng = random.Random(SEED)
    latest = {}
    witness = {}
    violations = []
    draws = 0
    tset = set(targets)
    for draws in range(1, N_MAX + 1):
        x = rng.getrandbits(WIDTH)
        vis = visible_fast(x, WIDTH, H)
        s = ''.join(map(str, vis))
        for j in range(J_MAX + 1):
            w = s[j:j + NWORD]
            if latest.get(w, -1) < j:
                latest[w] = j
            if w in excl and j >= excl[w]:
                violations.append(dict(word=w, age=j, draw=draws))
            if j == J_MAX and w in tset and w not in witness:
                witness[w] = dict(draw=draws, row=''.join(str((x >> i) & 1) for i in range(WIDTH)))
        if violations:
            break
        if len(witness) == len(tset):
            break
        if draws % 5000 == 0:
            ru = resource.getrusage(resource.RUSAGE_SELF)
            if ru.ru_utime + ru.ru_stime > 570:
                break
    # replay every retained witness with the literal evaluator
    for w, rec in witness.items():
        vl = visible_literal([int(c) for c in rec['row']], H)
        assert ''.join(map(str, vl[J_MAX:J_MAX + NWORD])) == w, ('witness replay failed', w)
        rec['replayed_literal'] = True
        rec['visible_trace'] = ''.join(map(str, vl))
    verdict = {}
    for w in L:
        if w in excl:
            verdict[w] = dict(status='EXCLUDED', bound=excl[w], latest_sampled=latest.get(w))
        elif w in witness:
            verdict[w] = dict(status='WITNESSED_100', latest_sampled=latest.get(w))
        else:
            verdict[w] = dict(status='UNRESOLVED', latest_sampled=latest.get(w))
    trap = lambda w: all(b - a in (3, 5) for a, b in zip([i for i, c in enumerate(w) if c == '1'],
                                                        [i for i, c in enumerate(w) if c == '1'][1:]))
    summary = dict(source_sha256=src, seed=SEED, prng='random.Random (MT19937), getrandbits(215), bit i = cell i+1',
                   n_max=N_MAX, draws=draws, width=WIDTH, H=H, J_max=J_MAX, violations=violations,
                   gate_complete=all(v['status'] != 'UNRESOLVED' for v in verdict.values()),
                   witnessed=len(witness), unresolved=[w for w, v in verdict.items() if v['status'] == 'UNRESOLVED'],
                   trap_rhythm_targets_witnessed=sum(1 for w in witness if trap(w)),
                   other_targets_witnessed=sum(1 for w in witness if not trap(w)),
                   verdict=verdict, wall_s=time.monotonic() - started,
                   cpu_s=sum(resource.getrusage(resource.RUSAGE_SELF)[:2]))
    (root / 'witnesses.json').write_text(json.dumps(witness, indent=1))
    (root / 'summary.json').write_text(json.dumps(summary, indent=1))
    print(json.dumps({k: summary[k] for k in ('draws', 'witnessed', 'gate_complete', 'trap_rhythm_targets_witnessed',
                                              'other_targets_witnessed', 'violations')}))
    return 1 if violations else 0


if __name__ == '__main__':
    sys.exit(main())
