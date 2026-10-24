#!/usr/bin/env python3
"""Submission generator for the width-74 death-time lower bound, revision 2 (Local, 2026-10-24, L889; revision 1 at c171c3cd, reviewed in
GPT's GC1797: one shared census validator for both paths, including the supervisor receipt; the ratio range rounded outward; the header
separates scalar re-simulation from the CPU chunk checks). Prepared while the GC1795-accepted width-74 census ran, under the owner's
next-job-ready rule. NOT for submission until GPT has read the module, the essay and the gate.

The theorems are submission 15's, unchanged: d5_lower_submission.module (its bytes untouched) generates the body for the one witness;
only the module's opening comment is replaced by one written for a single width. The witness is the census maximizer with the smallest
lane index, as at widths 66 to 72; it is re-checked here by the scalar engine and by d1_engine.validate_witness before any text is
written, and the census result is pinned by its digest once known. Nothing about maximality, the number of maximizers or any upper
bound is proved; those are the census's numerical results, stated as such in the essay.

Usage:
  python3 d6_lower74_submission.py pick STAGE_DIR     print D, the count, the occupied 4,096-blocks and the smallest-lane maximizer
  python3 d6_lower74_submission.py write OUT_DIR STAGE_DIR [CHECK_JSON]
        STAGE_DIR is the census stage's output folder (receipts.json and run/p1c_result.json); both paths validate it in full.
        write Rule30Submission.lean and essay.md into OUT_DIR (CHECK_JSON, the kit checker's output, fills the replay count in the essay)
"""
import hashlib, json, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import p1_lane_engine as P
import d1_engine as E
import d5_lower_submission as D5

W74_CENSUS_SHA256 = 'cb4fef782cd56de742292f6357ded296530230c372130705bef4b402e0ccc31b'   # from `pick` (L889)
WITNESSES = [(74, 134, 0x2736c92c34042aaaaab)]   # from `pick` (L889): the smallest-lane census maximizer, index 45192617984
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
attaining it. The engine is an exact lane engine in Metal; a batch of 2^24 starts and every chunk holding a maximizer were checked
against an independent CPU evaluation of the kit's lane check, and samples of further starts and every maximizer were re-simulated by
a scalar evaluator. The census is numerical; this module proves only the lower bound.

**The argument** is a kernel computation and the kit's own lemmas: `w < 2 ^ W` by `decide`; `toFun w k = false` beyond the width
by the kit's `testBit_ge_of_lt`; the packed orbit `prun w (2 s)` tested at depth 1 for every `s < D / 2` by `decide +kernel`;
`zrow (toFun w) t 1 = (prun w t).testBit 0` by the kit's `run_toFun`.

**Provenance.** The Wolfram · Collatz · Mahler record (github.com/ghywel/placego, CHAT-LEDGER.md L887 to L889, 2026-10-24).
Nothing is claimed for maximality, for the number of maximizers, or for any upper bound.
-/

"""


def validate(stage_dir):
    """The shared validator (GC1797): the supervisor's receipt and the census result, in full. Returns (result dict, path, smallest-lane
    maximizer index and its start). Raises AssertionError naming the first failed condition."""
    rp = os.path.join(stage_dir, 'receipts.json'); path = os.path.join(stage_dir, 'run', 'p1c_result.json')
    rc = json.load(open(rp)); d = json.load(open(path)); c = d['census']; sc = d['scope']; n = 1 << 37
    steps = [x for x in rc.get('steps', []) if x.get('step') != 'preflight']
    assert rc.get('complete') is True and len(steps) == 1 and steps[0].get('verdict') == 'pass' and steps[0].get('final_problems') == [], 'the stage receipt is not one clean pass'
    assert d.get('complete') is True and all(v.get('pass') is True for v in d['checks'].values()), 'the result is not complete with every check passed'
    assert sc.get('W') == 74 and sc.get('T') == 296 and sc.get('lanes') == n and c.get('lanes') == n, 'scope, horizon or coverage'
    assert c.get('censored') == 0 and c.get('maximizer_list_complete') is True, 'censoring or an incomplete maximizer list'
    mx = sorted(int(i) for i in c['maximizers'])
    assert mx and len(set(mx)) == len(mx) and all(0 <= i < n for i in mx) and c.get('max_count') == len(mx), 'the maximizer list'
    assert c['max'] % 2 == 0 and c['max'] > 74, 'D must be even and above the width for the domain reduction'
    i0 = mx[0]; s = P.recon(74, i0)
    listed = {int(w['index']): int(w['start'], 16) for w in c['witnesses']}
    assert listed.get(i0) == s, 'the selected witness is not the retained, validated census witness entry'
    return d, path, i0, s


def pick(stage_dir):
    d, path, i0, s = validate(stage_dir); c = d['census']; mx = sorted(int(i) for i in c['maximizers'])
    out = {'census_sha256': P.digest(path), 'D': c['max'], 'count': c['max_count'], 'occupied_4096_blocks': len({i >> 12 for i in mx}),
           'index': i0, 'start': hex(s), 'bits': s.bit_length(), 'scalar_death': P.death(s, 4 * 74),
           'census_wall_s': d.get('census_wall_s'), 'gpu_total_s': d.get('gpu_total_s')}
    print(json.dumps(out)); return out


def module(wit):
    text = D5.module(wit)
    i = text.index('set_option Elab.async false')
    out = HEAD.replace('@@D@@', str(wit[0][1])) + text[i:]
    assert '"' not in out and '\\' not in out, 'the module would break the Wolfram string'
    return out


def write(out, stage_dir, check_path=None):
    assert WITNESSES and W74_CENSUS_SHA256, 'fill WITNESSES and W74_CENSUS_SHA256 from `pick` first'
    d, census_path, i0, s0 = validate(stage_dir); c = d['census']
    assert P.digest(census_path) == W74_CENSUS_SHA256, 'the census result is not the pinned one'
    (W, Dv, s), = WITNESSES
    mx = sorted(int(i) for i in c['maximizers'])
    assert W == 74 and Dv == c['max'] and s == s0, 'the witness is not the smallest-lane census maximizer'
    assert 0 < s < (1 << W) and P.death(s, 4 * W) == Dv, 'scalar death'
    ok, why = E.validate_witness(W, Dv, s); assert ok, why
    os.makedirs(out, exist_ok=True)
    src = module(WITNESSES); open(os.path.join(out, 'Rule30Submission.lean'), 'w').write(src)
    consts = 'N' if not check_path else str(json.load(open(check_path))['replay']['constants'])
    from fractions import Fraction
    ratios = [Fraction(a, b) for a, b in ((96, 52), (100, 56), (114, 60), (116, 64), (120, 66), (122, 68), (124, 70), (130, 72), (Dv, 74))]
    import math
    lo, hi = min(ratios), max(ratios)
    rlo = Fraction(math.floor(lo * 100), 100); rhi = Fraction(math.ceil(hi * 100), 100)   # floor and ceiling at two decimals, exactly (GC1797)
    assert rlo <= lo and hi <= rhi
    fill = {'@@D@@': str(Dv), '@@HEX@@': '%x' % s, '@@BITS@@': str(s.bit_length()), '@@COUNT@@': str(c['max_count']),
            '@@BLOCKS@@': str(len({i >> 12 for i in mx})), '@@GPUMIN@@': str(round(d['gpu_total_s'] / 60)), '@@CONSTANTS@@': consts,
            '@@STEPS@@': str(Dv + 2), '@@DIGITS@@': str(74 + Dv + 10), '@@DM2@@': str(Dv - 2),
            '@@RLO@@': '%d.%02d' % divmod(int(rlo * 100), 100), '@@RHI@@': '%d.%02d' % divmod(int(rhi * 100), 100)}
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
