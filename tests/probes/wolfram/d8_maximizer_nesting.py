#!/usr/bin/env python3
"""D8, revision 3 (Local, 2026-10-24, L895; GPT's GC1805: a supervised `stage` taking an exact input manifest of all seven widths
64..76 with their digests, requiring all six steps, under the W1A supervisor with explicit caps; the median labelled as the UPPER median
of the row-best runs). Revision 2 (Local, 2026-10-24, L895; GPT's GC1804: the comparison labelled, the counterfactual narrowed, the coincidence count named
precisely with a multiplicity beside it, a typical-pair measure beside the maximum, input domains validated, an occupied output refused,
an explicit pair cap, literal controls). Revision 1 (L894; Cloud's CL624 item 2, at the owner's word: "read the maximizer structure off
the data already in hand ... are the maximizers' deep prefixes at W + 2 extensions of those at W (nested), or unrelated?"). CPU only, on
the retained census results; no new compute. Prepared while the width-76 census runs; to run when it returns, before any new launch.

Coordinates. A census index f at width W has W/2 bits; bit i is the odd trace bit a(2i+1) (p1_lane_engine.index_of). A start's trace is
physical, so the first W/2 bits of a width-(W+2) index are the trace bits a(1), a(3), ..., a(W-1) in the same coordinates as a width-W
index: the projection j mod 2^(W/2) is exact, not an approximation. The DEEP prefix of length k is the top k of those W/2 bits (the
latest trace bits below time W). The comparison is PROJECTED: the top k bits of j mod 2^(W/2) and of a width-W index are the same
absolute odd trace times W-2k+1, ..., W-1; the new bit a(W+1) is dropped. It is not a comparison of the newest k bits at each width.
The coordinate identity does not preserve the zero tail beyond W, the lifetime or maximizing status: nesting is a finite observation.

For each consecutive pair (W, W+2) with both results present, reported exactly:
  - for k in (4, 8, 12, 16, 20): P_k = { f >> (W/2 - k) : f a width-W maximizer }, Q_k = { (j mod 2^(W/2)) >> (W/2 - k) : j a width-(W+2)
    maximizer }; |P_k|, |Q_k|, |P_k & Q_k|, and whether Q_k is contained in P_k (NESTED at k);
  - the longest run of top bits shared by any width-W maximizer and any projected width-(W+2) maximizer;
  - DISTINCT projected values that are width-W maximizers, and the MULTIPLICITY (width-(W+2) rows whose projection is one);
  - the longest shared top-bit run over all pairs (a maximum, not typical) and the median over width-(W+2) rows of each row's best run;
  - the new top bit a(W+1) of the width-(W+2) maximizers: counts of 0 and 1.
Every result file is read through its census fields only (complete, scope W, zero censored, complete maximizer list); its digest is
recorded. The output is one JSON and a markdown page with the exact maximizer lists.

Predictions (written before any run, L894): Cloud's (CL624, low confidence): NESTED at the top 20 bits for at least four of the five steps
64 to 74. Local's: NOT nested at 20 bits for most steps (at most two of the six steps 64 to 76), with the shared top-bit run usually
under 12. Counterfactual for both, narrowed by GC1804: non-nesting at a step refutes, at that step, only the policy that extensions of the
previous width's maximizing k-bit blocks are all that need searching; it does not kill incremental exact search in general (a method
may keep non-maximizing blocks or use sound bounds). Nesting at the measured steps is neither a pruning certificate nor a law for W78,
and says nothing about late bits alone determining death (D5's within-block spread stands). Cloud's prediction counts five steps
(through 74), Local's six (through 76); both denominators are kept.
Usage: python3 d8_maximizer_nesting.py OUT_DIR W=RESULT.json [W=RESULT.json ...]     (OUT_DIR new or empty; widths even, distinct, in 64..76)
       python3 d8_maximizer_nesting.py --controls                                    (literal controls, GC1804's two adversarial cases)
       python3 d8_maximizer_nesting.py stage OUT_DIR MANIFEST.json   (the supervised run: exactly the seven widths, digests checked,
              all six steps required; W1A caps: stage, step wall and CPU 300 s, group RSS 2 GiB, artifacts 10 MiB, log 10 MiB)
OUTCOME: (to be filled after the run)
"""
import hashlib, json, os, sys

KS = (4, 8, 12, 16, 20)
REQUIRED_WIDTHS = (64, 66, 68, 70, 72, 74, 76)
W1A_SHA256 = '3f9089146c744e4910b3a1bb30ff2a62c102f33ceaf3bfb5b1f6dbf201a73883'
STAGE_S = 300
WIDTHS_ALLOWED = range(64, 77, 2)
PAIR_CAP = 10 ** 6


def load(W, path):
    d = json.load(open(path)); c = d['census']
    assert d.get('complete') is True and d['scope']['W'] == W and c['censored'] == 0 and c['maximizer_list_complete'] is True, path
    mx = sorted(int(i) for i in c['maximizers']); assert len(mx) == c['max_count'] and len(set(mx)) == len(mx)
    assert mx and all(0 <= i < (1 << (W // 2)) for i in mx), 'empty or out-of-range maximizer list'
    return {'W': W, 'D': c['max'], 'maximizers': mx, 'sha256': hashlib.sha256(open(path, 'rb').read()).hexdigest()}


def shared_top(a, b, n):
    x = a ^ b
    return n if x == 0 else n - x.bit_length()


def pair(A, B):
    W, n = A['W'], A['W'] // 2
    assert B['W'] == W + 2
    proj = [j & ((1 << n) - 1) for j in B['maximizers']]
    assert len(A['maximizers']) * len(B['maximizers']) <= PAIR_CAP, 'the pairwise comparison exceeds the cap'
    out = {'W': W, 'W2': W + 2, 'D': A['D'], 'D2': B['D'], 'count': len(A['maximizers']), 'count2': len(B['maximizers']), 'k': {}}
    for k in KS:
        P = {f >> (n - k) for f in A['maximizers']}; Q = {x >> (n - k) for x in proj}
        out['k'][str(k)] = {'P': len(P), 'Q': len(Q), 'common': len(P & Q), 'nested': Q <= P}
    best = sorted(max(shared_top(f, x, n) for f in A['maximizers']) for x in proj)
    out['longest_shared_top_bits_max_over_pairs'] = best[-1]
    out['upper_median_best_shared_top_bits_over_rows'] = best[len(best) // 2]     # the upper middle order statistic of the row-best runs
    Aset = set(A['maximizers'])
    out['distinct_projected_coincidences'] = len(set(proj) & Aset)
    out['rows_projecting_onto_width_W_maximizers'] = sum(1 for x in proj if x in Aset)
    top = [(j >> n) & 1 for j in B['maximizers']]
    out['new_top_bit_counts'] = {'0': top.count(0), '1': top.count(1)}
    return out


def controls():
    n = 32; res = {}
    A = {'W': 64, 'D': 116, 'maximizers': [0]}; B = {'W': 66, 'D': 120, 'maximizers': [0, 1 << n]}
    q = pair(A, B); res['two_rows_one_projection'] = q['distinct_projected_coincidences'] == 1 and q['rows_projecting_onto_width_W_maximizers'] == 2
    B2 = {'W': 66, 'D': 120, 'maximizers': [0, 1 << (n - 1)]}
    q = pair(A, B2); res['max_run_not_typical'] = (q['longest_shared_top_bits_max_over_pairs'] == n and q['upper_median_best_shared_top_bits_over_rows'] == n
                                                  and not any(v['nested'] for v in q['k'].values()))
    B3 = {'W': 66, 'D': 120, 'maximizers': [(1 << (n - 1)) | 5]}
    q = pair(A, B3); res['disjoint_top_bit_not_nested'] = not q['k']['4']['nested'] and q['longest_shared_top_bits_max_over_pairs'] == 0
    B4 = {'W': 66, 'D': 120, 'maximizers': [3, (1 << n) | 7]}
    q = pair(A, B4); res['low_bit_change_still_nested_at_20'] = q['k']['20']['nested'] and q['distinct_projected_coincidences'] == 0
    ok = all(res.values()); print(json.dumps(res, indent=1)); print('D8 CONTROLS', 'PASS' if ok else 'FAIL', len(res)); return ok


def stage(out, manifest_path):
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    import w1a_harness as H
    if hashlib.sha256(open(H.__file__, 'rb').read()).hexdigest() != W1A_SHA256:
        print('REFUSED: W1A is not the pinned bytes'); return 3
    if not os.path.isabs(out) or (os.path.exists(out) and os.listdir(out)):
        print('REFUSED: OUT must be absolute and new or empty'); return 3
    man = json.load(open(manifest_path))
    if sorted(int(w) for w in man) != list(REQUIRED_WIDTHS):
        print('REFUSED: the manifest must name exactly the widths', REQUIRED_WIDTHS); return 3
    for w, e in man.items():
        if hashlib.sha256(open(e['path'], 'rb').read()).hexdigest() != e['sha256']:
            print('REFUSED: width %s input is not the manifest bytes' % w); return 3
    os.makedirs(out, exist_ok=True)
    H.CAPS['stage_s'] = STAGE_S; H.CAPS['rss_stop_bytes'] = 2 << 30; H.CAPS['artifacts_max_bytes'] = 10 << 20; H.CAPS['log_max_bytes'] = 10 << 20
    sup = H.Supervisor(out, out); Rc = sup.receipts
    Rc['d8'] = {'this_sha256': hashlib.sha256(open(os.path.abspath(__file__), 'rb').read()).hexdigest(), 'w1a_sha256': W1A_SHA256,
                'manifest': {w: e['sha256'] for w, e in man.items()}, 'manifest_sha256': hashlib.sha256(open(manifest_path, 'rb').read()).hexdigest(),
                'caps': {'stage_s': STAGE_S, 'step_wall_s': STAGE_S, 'step_cpu_s': STAGE_S, 'group_rss_stop_bytes': 2 << 30, 'artifacts_max_bytes': 10 << 20}}
    sup.save()
    if H.pressure_bad(sup.baseline):
        Rc['stopped'] = 'pressure at launch'; sup.save(); print('STOP: pressure'); return 1
    r = sup.register(H.preflight())
    if r['verdict'] != 'pass':
        Rc['stopped'] = 'preflight'; sup.save(); print('STOP: preflight'); return 1
    rdir = os.path.join(out, 'run')

    def matcher(rc, text):
        try:
            d = json.load(open(os.path.join(rdir, 'd8_nesting.json')))
        except Exception as e:
            return 'FAIL', 'no result: %r' % e
        steps = [(q['W'], q['W2']) for q in d.get('pairs', [])]
        if rc != 0 or steps != [(w, w + 2) for w in REQUIRED_WIDTHS[:-1]]:
            return 'FAIL', 'rc %s steps %s' % (rc, steps)
        return 'pass', 'D8 complete: all six steps 64 to 76'
    cmd = [sys.executable, os.path.abspath(__file__), rdir] + ['%s=%s' % (w, man[w]['path']) for w in sorted(man, key=int)]
    rec = sup.run_step('d8_nesting', cmd, out, STAGE_S, STAGE_S, matcher)
    Rc['complete'] = rec['verdict'] == 'pass'; sup.save()
    print('DONE' if Rc['complete'] else 'STOP', rec['verdict'], rec['reason'], rec.get('match_note'))
    return 0 if Rc['complete'] else 1


if __name__ == '__main__':
    a = sys.argv[1:]
    if a == ['--controls']:
        sys.exit(0 if controls() else 1)
    if len(a) == 3 and a[0] == 'stage':
        sys.exit(stage(a[1], a[2]))
    if len(a) < 3:
        print(__doc__); sys.exit(2)
    out_dir = a[0]
    assert not (os.path.exists(out_dir) and os.listdir(out_dir)), 'the output folder must be new or empty'
    os.makedirs(out_dir, exist_ok=True)
    res = {}
    for spec in a[1:]:
        w, p = spec.split('=', 1); w = int(w)
        assert w in WIDTHS_ALLOWED and w not in res, 'widths must be even, distinct, in 64..76'
        res[w] = load(w, p)
    widths = sorted(res)
    pairs = [pair(res[W], res[W + 2]) for W in widths if W + 2 in res]
    R = {'inputs': {str(W): {'D': res[W]['D'], 'count': len(res[W]['maximizers']), 'sha256': res[W]['sha256']} for W in widths}, 'pairs': pairs}
    json.dump(R, open(os.path.join(out_dir, 'd8_nesting.json'), 'w'), indent=1)
    lines = ['# D8: maximizer nesting across widths (Local, L894)', '', '| W to W+2 | D | ' + ' | '.join('nested at %d (projected)' % k for k in KS) + ' | longest shared top run (max over pairs) | upper median of row-best runs | distinct coincidences / rows | new top bit 0/1 |',
             '|---|---|' + '---|' * len(KS) + '---|---|---|---|']
    for q in pairs:
        lines.append('| %d to %d | %d to %d | %s | %d | %d | %d / %d | %d/%d |' % (q['W'], q['W2'], q['D'], q['D2'],
                     ' | '.join('%s (%d of %d)' % ('yes' if q['k'][str(k)]['nested'] else 'no', q['k'][str(k)]['common'], q['k'][str(k)]['Q']) for k in KS),
                     q['longest_shared_top_bits_max_over_pairs'], q['upper_median_best_shared_top_bits_over_rows'], q['distinct_projected_coincidences'], q['rows_projecting_onto_width_W_maximizers'], q['new_top_bit_counts']['0'], q['new_top_bit_counts']['1']))
    lines += ['', '## The exact maximizer lists (census indices)', '']
    for W in widths:
        lines.append('- W = %d, D = %d, %d maximizers: %s' % (W, res[W]['D'], len(res[W]['maximizers']), ', '.join(str(i) for i in res[W]['maximizers'])))
    open(os.path.join(out_dir, 'd8_nesting.md'), 'w').write('\n'.join(lines) + '\n')
    print(json.dumps([{k: q[k] for k in ('W', 'W2', 'longest_shared_top_bits_max_over_pairs', 'upper_median_best_shared_top_bits_over_rows', 'distinct_projected_coincidences', 'rows_projecting_onto_width_W_maximizers')} | {'nested': {k: q['k'][k]['nested'] for k in q['k']}} for q in pairs]))
