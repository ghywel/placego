#!/usr/bin/env python3
"""Submission generator for the width-74 death-time lower bound (Local, 2026-10-24, L889; prepared while the GC1795-accepted width-74
census ran, under the owner's next-job-ready rule). NOT for submission until GPT has read the module, the essay and the gate.

The theorems are submission 15's, unchanged: d5_lower_submission.module (its bytes untouched) generates the body for the one witness;
only the module's opening comment is replaced by one written for a single width. The witness is the census maximizer with the smallest
lane index, as at widths 66 to 72; it is re-checked here by the scalar engine and by d1_engine.validate_witness before any text is
written, and the census result is pinned by its digest once known. Nothing about maximality, the number of maximizers or any upper
bound is proved; those are the census's numerical results, stated as such in the essay.

Usage:
  python3 d6_lower74_submission.py pick CENSUS_RESULT.json     print D, the count, the occupied 4,096-blocks and the smallest-lane maximizer
  python3 d6_lower74_submission.py write OUT_DIR CENSUS_RESULT.json [CHECK_JSON]
        write Rule30Submission.lean and essay.md into OUT_DIR (CHECK_JSON, the kit checker's output, fills the replay count in the essay)
"""
import hashlib, json, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import p1_lane_engine as P
import d1_engine as E
import d5_lower_submission as D5

W74_CENSUS_SHA256 = None          # filled from `pick` after the census
WITNESSES = []                    # [(74, D, start)], filled from `pick` after the census
TEMPLATE = os.path.join(HERE, '..', '..', '..', 'reports', 'wolfram-agents', 'submissions', 'd-lower-74', 'essay-template.md')

HEAD = """import Rule30PrizeKit
import Ruliology.CellularAutomata.Rule30ZeroBoundarySmall

/-!
# A death-time lower bound at width 74: an explicit witness from a complete GPU census

**Partial result on the kit's `Q01` (the period-2 question, Problem 1 of the Rule 30 Prize), proved against the kit's own
definitions.** Write `D(W)` for the largest, over zero-boundary starts supported at depths at most `W`, of the first even time at
which the depth-1 cell is white. The kit at the pinned commit cc1e0e0 proves `D(52) <= 96` (`Rule30ZeroBoundaryWidth52`) and has no
statement at any width above 52; submission R30-20261024-b16332 proved `D(64) >= 116` to `D(72) >= 130`. This module proves
`D(74) >= @@D@@`: an explicit start, supported at depths at most 74, is black at depth 1 at every even time below the bound and white
at the bound, by the kit's packed evaluator `prun` and its bridge `run_toFun` (`width74_lower`).

**Where the witness comes from.** A complete numerical census on a GPU of every reconstructed start of width 74 that survives the
even times below 74 (every maximizer lies among them, since the value exceeds 74) found this value to be the maximum, the witness
attaining it. The engine is an exact lane engine in Metal; a batch of 2^24 starts, a sample of further starts, every maximizer and
every chunk holding one were checked against an independent CPU evaluation of the kit's lane check. The census is numerical; this
module proves only the lower bound.

**The argument** is a kernel computation and the kit's own lemmas: `w < 2 ^ W` by `decide`; `toFun w k = false` beyond the width
by the kit's `testBit_ge_of_lt`; the packed orbit `prun w (2 s)` tested at depth 1 for every `s < D / 2` by `decide +kernel`;
`zrow (toFun w) t 1 = (prun w t).testBit 0` by the kit's `run_toFun`.

**Provenance.** The Wolfram · Collatz · Mahler record (github.com/ghywel/placego, CHAT-LEDGER.md L887 to L889, 2026-10-24).
Nothing is claimed for maximality, for the number of maximizers, or for any upper bound.
-/

"""


def pick(path):
    d = json.load(open(path)); c = d['census']
    assert d.get('complete') is True and d['scope']['W'] == 74 and c['censored'] == 0 and c['maximizer_list_complete'] is True
    mx = sorted(int(i) for i in c['maximizers']); i0 = mx[0]; s = P.recon(74, i0)
    listed = {int(w['index']): int(w['start'], 16) for w in c['witnesses']}
    out = {'census_sha256': P.digest(path), 'D': c['max'], 'count': c['max_count'], 'occupied_4096_blocks': len({i >> 12 for i in mx}),
           'index': i0, 'start': hex(s), 'bits': s.bit_length(), 'scalar_death': P.death(s, 4 * 74), 'equals_census_witness_entry': listed.get(i0) == s,
           'census_wall_s': d.get('census_wall_s'), 'gpu_total_s': d.get('gpu_total_s')}
    print(json.dumps(out)); return out


def module(wit):
    text = D5.module(wit)
    i = text.index('set_option Elab.async false')
    out = HEAD.replace('@@D@@', str(wit[0][1])) + text[i:]
    assert '"' not in out and '\\' not in out, 'the module would break the Wolfram string'
    return out


def write(out, census_path, check_path=None):
    assert WITNESSES and W74_CENSUS_SHA256, 'fill WITNESSES and W74_CENSUS_SHA256 from `pick` first'
    assert P.digest(census_path) == W74_CENSUS_SHA256, 'the census result is not the pinned one'
    d = json.load(open(census_path)); c = d['census']
    (W, Dv, s), = WITNESSES
    mx = sorted(int(i) for i in c['maximizers'])
    assert W == 74 and Dv == c['max'] and P.recon(74, mx[0]) == s, 'the witness is not the smallest-lane census maximizer'
    assert 0 < s < (1 << W) and P.death(s, 4 * W) == Dv, 'scalar death'
    ok, why = E.validate_witness(W, Dv, s); assert ok, why
    os.makedirs(out, exist_ok=True)
    src = module(WITNESSES); open(os.path.join(out, 'Rule30Submission.lean'), 'w').write(src)
    consts = 'N' if not check_path else str(json.load(open(check_path))['replay']['constants'])
    ratios = [96 / 52, 100 / 56, 114 / 60, 116 / 64, 120 / 66, 122 / 68, 124 / 70, 130 / 72, Dv / 74]
    fill = {'@@D@@': str(Dv), '@@HEX@@': '%x' % s, '@@BITS@@': str(s.bit_length()), '@@COUNT@@': str(c['max_count']),
            '@@BLOCKS@@': str(len({i >> 12 for i in mx})), '@@GPUMIN@@': str(round(d['gpu_total_s'] / 60)), '@@CONSTANTS@@': consts,
            '@@STEPS@@': str(Dv + 2), '@@DIGITS@@': str(74 + Dv + 10), '@@DM2@@': str(Dv - 2),
            '@@RLO@@': '%.2f' % min(ratios), '@@RHI@@': '%.2f' % max(ratios)}
    tpl = open(TEMPLATE, encoding='utf-8').read()
    for k, v in fill.items(): tpl = tpl.replace(k, v)
    assert tpl.count('@@LEAN_SOURCE@@') == 1 and '@@' not in tpl.replace('@@LEAN_SOURCE@@', ''), 'an unfilled placeholder'
    essay = tpl.replace('@@LEAN_SOURCE@@', src.rstrip('\n') + '\n')
    open(os.path.join(out, 'essay.md'), 'w', encoding='utf-8').write(essay)
    for n in ('Rule30Submission.lean', 'essay.md'):
        print(n, hashlib.sha256(open(os.path.join(out, n), 'rb').read()).hexdigest())


if __name__ == '__main__':
    a = sys.argv[1:]
    if len(a) == 2 and a[0] == 'pick':
        pick(a[1]); sys.exit(0)
    if len(a) in (3, 4) and a[0] == 'write':
        write(a[1], a[2], a[3] if len(a) == 4 else None); sys.exit(0)
    print(__doc__); sys.exit(2)
