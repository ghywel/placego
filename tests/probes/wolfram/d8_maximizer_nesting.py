#!/usr/bin/env python3
"""D8, the maximizer-nesting reading (Local, 2026-10-24, L894; Cloud's CL624 item 2, at the owner's word: "read the maximizer structure off
the data already in hand ... are the maximizers' deep prefixes at W + 2 extensions of those at W (nested), or unrelated?"). CPU only, on
the retained census results; no new compute. Prepared while the width-76 census runs; to run when it returns, before any new launch.

Coordinates. A census index f at width W has W/2 bits; bit i is the odd trace bit a(2i+1) (p1_lane_engine.index_of). A start's trace is
physical, so the first W/2 bits of a width-(W+2) index are the trace bits a(1), a(3), ..., a(W-1) in the same coordinates as a width-W
index: the projection j mod 2^(W/2) is exact, not an approximation. The DEEP prefix of length k is the top k of those W/2 bits (the
latest trace bits below time W).

For each consecutive pair (W, W+2) with both results present, reported exactly:
  - for k in (4, 8, 12, 16, 20): P_k = { f >> (W/2 - k) : f a width-W maximizer }, Q_k = { (j mod 2^(W/2)) >> (W/2 - k) : j a width-(W+2)
    maximizer }; |P_k|, |Q_k|, |P_k & Q_k|, and whether Q_k is contained in P_k (NESTED at k);
  - the longest run of top bits shared by any width-W maximizer and any projected width-(W+2) maximizer;
  - how many projected width-(W+2) maximizers are themselves width-W maximizers (exact index coincidence);
  - the new top bit a(W+1) of the width-(W+2) maximizers: counts of 0 and 1.
Every result file is read through its census fields only (complete, scope W, zero censored, complete maximizer list); its digest is
recorded. The output is one JSON and a markdown page with the exact maximizer lists.

Predictions (written before any run, L894): Cloud's (CL624, low confidence): NESTED at the top 20 bits for at least four of the five steps
64 to 74. Local's: NOT nested at 20 bits for most steps (at most two of the six steps 64 to 76), with the shared top-bit run usually
under 12. Counterfactual for both: unrelated prefixes kill any incremental exact search (fixing deep bits from the previous width) and
say so cheaply; nested prefixes would make the previous width's blocks the place to start a pruned search, still not a bound (GC1794).
Usage: python3 d8_maximizer_nesting.py OUT_DIR W=RESULT.json [W=RESULT.json ...]
OUTCOME: (to be filled after the run)
"""
import hashlib, json, os, sys

KS = (4, 8, 12, 16, 20)


def load(W, path):
    d = json.load(open(path)); c = d['census']
    assert d.get('complete') is True and d['scope']['W'] == W and c['censored'] == 0 and c['maximizer_list_complete'] is True, path
    mx = sorted(int(i) for i in c['maximizers']); assert len(mx) == c['max_count'] and len(set(mx)) == len(mx)
    return {'W': W, 'D': c['max'], 'maximizers': mx, 'sha256': hashlib.sha256(open(path, 'rb').read()).hexdigest()}


def shared_top(a, b, n):
    x = a ^ b
    return n if x == 0 else n - x.bit_length()


def pair(A, B):
    W, n = A['W'], A['W'] // 2
    assert B['W'] == W + 2
    proj = [j & ((1 << n) - 1) for j in B['maximizers']]
    out = {'W': W, 'W2': W + 2, 'D': A['D'], 'D2': B['D'], 'count': len(A['maximizers']), 'count2': len(B['maximizers']), 'k': {}}
    for k in KS:
        P = {f >> (n - k) for f in A['maximizers']}; Q = {x >> (n - k) for x in proj}
        out['k'][str(k)] = {'P': len(P), 'Q': len(Q), 'common': len(P & Q), 'nested': Q <= P}
    out['longest_shared_top_bits'] = max(shared_top(f, x, n) for f in A['maximizers'] for x in proj)
    out['projected_that_are_width_W_maximizers'] = len(set(proj) & set(A['maximizers']))
    top = [(j >> n) & 1 for j in B['maximizers']]
    out['new_top_bit_counts'] = {'0': top.count(0), '1': top.count(1)}
    return out


if __name__ == '__main__':
    a = sys.argv[1:]
    if len(a) < 3:
        print(__doc__); sys.exit(2)
    out_dir = a[0]; os.makedirs(out_dir, exist_ok=True)
    res = {}
    for spec in a[1:]:
        w, p = spec.split('=', 1); res[int(w)] = load(int(w), p)
    widths = sorted(res)
    pairs = [pair(res[W], res[W + 2]) for W in widths if W + 2 in res]
    R = {'inputs': {str(W): {'D': res[W]['D'], 'count': len(res[W]['maximizers']), 'sha256': res[W]['sha256']} for W in widths}, 'pairs': pairs}
    json.dump(R, open(os.path.join(out_dir, 'd8_nesting.json'), 'w'), indent=1)
    lines = ['# D8: maximizer nesting across widths (Local, L894)', '', '| W to W+2 | D | ' + ' | '.join('nested at %d' % k for k in KS) + ' | longest shared top bits | coincident | new top bit 0/1 |',
             '|---|---|' + '---|' * len(KS) + '---|---|---|']
    for q in pairs:
        lines.append('| %d to %d | %d to %d | %s | %d | %d | %d/%d |' % (q['W'], q['W2'], q['D'], q['D2'],
                     ' | '.join('%s (%d of %d)' % ('yes' if q['k'][str(k)]['nested'] else 'no', q['k'][str(k)]['common'], q['k'][str(k)]['Q']) for k in KS),
                     q['longest_shared_top_bits'], q['projected_that_are_width_W_maximizers'], q['new_top_bit_counts']['0'], q['new_top_bit_counts']['1']))
    lines += ['', '## The exact maximizer lists (census indices)', '']
    for W in widths:
        lines.append('- W = %d, D = %d, %d maximizers: %s' % (W, res[W]['D'], len(res[W]['maximizers']), ', '.join(str(i) for i in res[W]['maximizers'])))
    open(os.path.join(out_dir, 'd8_nesting.md'), 'w').write('\n'.join(lines) + '\n')
    print(json.dumps([{k: q[k] for k in ('W', 'W2', 'longest_shared_top_bits', 'projected_that_are_width_W_maximizers')} | {'nested': {k: q['k'][k]['nested'] for k in q['k']}} for q in pairs]))
