#!/usr/bin/env python3
"""Width-parametric lower-bound submission generator (Local, 2026-10-24, L891; prepared while the GC1800-accepted width-76 census ran,
under the owner's next-job-ready rule). d6_lower74_submission.py revision 2 (GC1797, GC1799) generalized from W = 74 to any even width W
with a complete p1c census result; the first intended use is W = 76. NOT for submission until GPT has read the source and the outputs.

Unchanged from d6: the theorem body is submission 15's (d5_lower_submission.module, bytes untouched) for the one witness, under a
one-width header; one shared validator for both paths (the stage receipt one clean pass; the result complete with every check passed;
scope W, horizon 4W and coverage 2^(W/2); zero censored; a complete, unique, in-range maximizer list matching its count; an even D above
W; the selected witness equal to the retained, validated census witness entry); the witness the smallest-lane maximizer; the census
result pinned by digest once known; the ratio range floored and ceiled exactly.

Revision 2 (GC1801): the witness cell's horizon is the frozen D, not a fixed 400; PROVENANCE is frozen with the result, not
named in advance; every check runs before either file is written. New in revision 1: W is a parameter; the prior table and the prior submissions are named in PRIOR and PRIOR_SUBMISSIONS; the essay comes from the
width-parametric template submissions/d-lower-template/essay-template.md.

Usage:
  python3 d7_lower_submission.py pick W STAGE_DIR
  python3 d7_lower_submission.py write W OUT_DIR STAGE_DIR [CHECK_JSON]
"""
import hashlib, json, math, os, sys
from fractions import Fraction

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import p1_lane_engine as P
import d1_engine as E
import d5_lower_submission as D5

CENSUS_SHA256 = 'a6cae0c0424b1bd593fb0af36dfea18c26dbae3a77083f96d6b24e8436c73d8b'   # from `pick` (L895), the width-76 census result
WITNESSES = [(76, 138, 0x5bf46e334109c62aaab)]   # from `pick` (L895): the smallest-lane census maximizer, index 81680756224
PRIOR = [(52, 96), (56, 100), (60, 114), (64, 116), (66, 120), (68, 122), (70, 124), (72, 130), (74, 134)]   # the table below W
PRIOR_SUBMISSIONS = 'submissions R30-20261024-b16332 and R30-20261024-a129c3 proved `D(64) >= 116` to `D(74) >= 134`'
PROVENANCE = 'L889 to L895'      # the carrying ledger entries (proposal L889, launch L890, generator L891, result L895), frozen with the result (GC1801)
TEMPLATE = os.path.join(HERE, '..', '..', '..', 'reports', 'wolfram-agents', 'submissions', 'd-lower-template', 'essay-template.md')

HEAD = """import Rule30PrizeKit
import Ruliology.CellularAutomata.Rule30ZeroBoundarySmall

/-!
# A death-time lower bound at width @@W@@: an explicit witness from a complete GPU census

**Partial result on the kit's `Q01` (the period-2 question, Problem 1 of the Rule 30 Prize), proved against the kit's own
definitions.** Write `D(W)` for the largest, over zero-boundary starts supported at depths at most `W`, of the first even time at
which the depth-1 cell is white. The kit at the pinned commit cc1e0e0 proves `D(52) <= 96` (`Rule30ZeroBoundaryWidth52`) and has no
statement at any width above 52; @@PRIORSUBS@@. This module proves
`D(@@W@@) >= @@D@@`: an explicit start, supported at depths at most @@W@@, is black at depth 1 at every even time below the bound and white
at the bound, by the kit's packed evaluator `prun` and its bridge `run_toFun` (`width@@W@@_lower`).

**Where the witness comes from.** A complete numerical census on a GPU of every reconstructed start of width @@W@@ that survives the
even times below @@W@@ (every maximizer lies among them, since the value exceeds @@W@@) found this value to be the maximum, the witness
attaining it. The engine is an exact lane engine in Metal; a batch of 2^24 starts and every chunk holding a maximizer were checked
against an independent CPU evaluation of the kit's lane check, and samples of further starts and every maximizer were re-simulated by
a scalar evaluator. The census is numerical; this module proves only the lower bound.

**The argument** is a kernel computation and the kit's own lemmas: `w < 2 ^ W` by `decide`; `toFun w k = false` beyond the width
by the kit's `testBit_ge_of_lt`; the packed orbit `prun w (2 s)` tested at depth 1 for every `s < D / 2` by `decide +kernel`;
`zrow (toFun w) t 1 = (prun w t).testBit 0` by the kit's `run_toFun`.

**Provenance.** The Wolfram · Collatz · Mahler record (github.com/ghywel/placego, CHAT-LEDGER.md @@PROV@@, 2026-10-24).
Nothing is claimed for maximality, for the number of maximizers, or for any upper bound.
-/

"""


def validate(W, stage_dir):
    rp = os.path.join(stage_dir, 'receipts.json'); path = os.path.join(stage_dir, 'run', 'p1c_result.json')
    rc = json.load(open(rp)); d = json.load(open(path)); c = d['census']; sc = d['scope']; n = 1 << (W // 2)
    steps = [x for x in rc.get('steps', []) if x.get('step') != 'preflight']
    assert W % 2 == 0 and W > 74, 'W must be an even width above the prior table'
    assert rc.get('complete') is True and len(steps) == 1 and steps[0].get('verdict') == 'pass' and steps[0].get('final_problems') == [], 'the stage receipt is not one clean pass'
    assert d.get('complete') is True and all(v.get('pass') is True for v in d['checks'].values()), 'the result is not complete with every check passed'
    assert sc.get('W') == W and sc.get('T') == 4 * W and sc.get('lanes') == n and c.get('lanes') == n, 'scope, horizon or coverage'
    assert c.get('censored') == 0 and c.get('maximizer_list_complete') is True, 'censoring or an incomplete maximizer list'
    mx = sorted(int(i) for i in c['maximizers'])
    assert mx and len(set(mx)) == len(mx) and all(0 <= i < n for i in mx) and c.get('max_count') == len(mx), 'the maximizer list'
    assert c['max'] % 2 == 0 and c['max'] > W, 'D must be even and above the width for the domain reduction'
    i0 = mx[0]; s = P.recon(W, i0)
    listed = {int(w['index']): int(w['start'], 16) for w in c['witnesses']}
    assert listed.get(i0) == s, 'the selected witness is not the retained, validated census witness entry'
    return d, path, i0, s


def pick(W, stage_dir):
    d, path, i0, s = validate(W, stage_dir); c = d['census']; mx = sorted(int(i) for i in c['maximizers'])
    out = {'census_sha256': P.digest(path), 'W': W, 'D': c['max'], 'count': c['max_count'], 'occupied_4096_blocks': len({i >> 12 for i in mx}),
           'index': i0, 'start': hex(s), 'bits': s.bit_length(), 'scalar_death': P.death(s, 4 * W),
           'census_wall_s': d.get('census_wall_s'), 'gpu_total_s': d.get('gpu_total_s'), 'prev': (d.get('prev') or {}).get('W'),
           'prev_witnesses': (d.get('prev') or {}).get('witnesses')}
    print(json.dumps(out)); return out


def module(wit):
    (W, Dv, s), = wit
    assert PROVENANCE, 'freeze PROVENANCE with the actual ledger entries first'
    text = D5.module(wit)
    i = text.index('set_option Elab.async false')
    head = HEAD.replace('@@W@@', str(W)).replace('@@D@@', str(Dv)).replace('@@PRIORSUBS@@', PRIOR_SUBMISSIONS).replace('@@PROV@@', PROVENANCE)
    assert '@@' not in head
    out = head + text[i:]
    assert '"' not in out and '\\' not in out, 'the module would break the Wolfram string'
    return out


def lanes_text(k):
    v = 1 << k
    return '`2^%d` (%.1f billion)' % (k, v / 1e9)


def write(W, out, stage_dir, check_path=None):
    assert WITNESSES and CENSUS_SHA256, 'fill WITNESSES and CENSUS_SHA256 from `pick` first'
    d, census_path, i0, s0 = validate(W, stage_dir); c = d['census']
    assert P.digest(census_path) == CENSUS_SHA256, 'the census result is not the pinned one'
    (Ww, Dv, s), = WITNESSES
    mx = sorted(int(i) for i in c['maximizers'])
    assert Ww == W and Dv == c['max'] and s == s0, 'the witness is not the smallest-lane census maximizer'
    assert 0 < s < (1 << W) and P.death(s, 4 * W) == Dv, 'scalar death'
    ok, why = E.validate_witness(W, Dv, s); assert ok, why
    prev = d.get('prev') or {}
    assert prev.get('W') == W - 2, 'the census must have carried the previous width (--prev)'
    src = module(WITNESSES)                # every check above runs before either file is written (GC1801)
    consts = 'N' if not check_path else str(json.load(open(check_path))['replay']['constants'])
    table = PRIOR + [(W, Dv)]
    ratios = [Fraction(b, a) for a, b in table]
    lo, hi = min(ratios), max(ratios)
    rlo = Fraction(math.floor(lo * 100), 100); rhi = Fraction(math.ceil(hi * 100), 100)
    assert rlo <= lo and hi <= rhi
    fill = {'@@W@@': str(W), '@@D@@': str(Dv), '@@HEX@@': '%x' % s, '@@COUNT@@': str(c['max_count']), '@@BLOCKS@@': str(len({i >> 12 for i in mx})),
            '@@GPUMIN@@': str(round(d['gpu_total_s'] / 60)), '@@CONSTANTS@@': consts, '@@STEPS@@': str(Dv + 2), '@@DIGITS@@': str(W + Dv + 10),
            '@@HALF@@': str(W // 2), '@@LANESTXT@@': lanes_text(W // 2), '@@CHUNKEXP@@': str(W // 2 - 18), '@@PREVW@@': str(prev.get('W')),
            '@@PREVCOUNT@@': str(prev.get('witnesses')), '@@PREVMAX@@': str(prev.get('max')), '@@TABLE@@': ', '.join(str(b) for _, b in table),
            '@@PRIORSUBS@@': PRIOR_SUBMISSIONS, '@@PROV@@': PROVENANCE,
            '@@RLO@@': '%d.%02d' % divmod(int(rlo * 100), 100), '@@RHI@@': '%d.%02d' % divmod(int(rhi * 100), 100)}
    tpl = open(TEMPLATE, encoding='utf-8').read()
    for k, v in fill.items(): tpl = tpl.replace(k, v)
    assert tpl.count('@@LEAN_SOURCE@@') == 1 and '@@' not in tpl.replace('@@LEAN_SOURCE@@', ''), 'an unfilled placeholder'
    essay = tpl.replace('@@LEAN_SOURCE@@', src.rstrip('\n') + '\n')
    os.makedirs(out, exist_ok=True)
    open(os.path.join(out, 'Rule30Submission.lean'), 'w').write(src)
    open(os.path.join(out, 'essay.md'), 'w', encoding='utf-8').write(essay)
    for n in ('Rule30Submission.lean', 'essay.md'):
        print(n, hashlib.sha256(open(os.path.join(out, n), 'rb').read()).hexdigest())


if __name__ == '__main__':
    a = sys.argv[1:]
    if len(a) == 3 and a[0] == 'pick':
        pick(int(a[1]), a[2]); sys.exit(0)
    if len(a) in (4, 5) and a[0] == 'write':
        write(int(a[1]), a[2], a[3], a[4] if len(a) == 5 else None); sys.exit(0)
    print(__doc__); sys.exit(2)
