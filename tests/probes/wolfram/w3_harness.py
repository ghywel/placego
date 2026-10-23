#!/usr/bin/env python3
"""W3, revision 1: a width-60 zero-boundary chunk certificate, built and kernel-checked on the M5 only (the owner,
2026-10-23 19:2x BST: "width 60 seems a reasonable target"; submissions withheld for now), under the W1A supervisor
(tests/probes/wolfram/w1a_harness.py revision 4) with the W2 generator (tests/probes/wolfram/w2_harness.py, whose
width-52 regeneration equals the kit's own modules). NOT an agreed job until GPT accepts this exact file; it runs
nothing on import; nothing is submitted.

Usage:  python3 w3_harness.py KIT_CLONE OUT_DIR          (OUT_DIR must not exist or must be empty)

What is built: W = 60, n = 18, 2^(30 - 18) = 4,096 chunks `check 60 K 18 c = true` by `decide +kernel`, in 256
namespaces `Rule30ZeroBoundaryWidth60.C<j>` of 16 (each with `range` as the balanced append tree), 64 modules
`Rule30Certificates/ZeroBoundaryWidth60Chunks<m>.lean` of 64 chunks, and the wrapper with
`all_chunks : ChunksOK 60 K 18 0 4096`, `q01_width_le_60` (t ≤ K - 1) and `not_inX_of_width_le_60`, the kit's shape.

K, stated honestly. No theorem gives a bound at width 60: the kit's `q01_width_le_52_linear` is a theorem at 52
only, and the kit author's private check reached 56 (bound 100). The record's observed death times are D(52) = 96
and D(56) ≤ 100, i.e. about 2W - 8 to 2W - 12. W3 uses K = 2W + 9 = 129, the experimental rule of W1B (which held
for chunk 0 at 40, 44 and 48 and is about 20 levels above the observed death times), as a PROPOSED bound: a complete
successful collection of kernel checks plus the sound assembly establishes `t ≤ 128` for every start of width ≤ 60
(GC1719/GC1721: no prior K theorem is required). If the kernel rejects some chunk's check at K = 129, that chunk is
recorded as PARAMETER-REFUTED-provisional with its exact statement and log, the stage stops, and nothing is retried
or re-run at a larger K without a new agreement: a rejected proof term does not prove the bound exceeds 128.

Order, stopping at the first unaccepted step, no retry: pins (commit, toolchain, the seven pinned sources, deps,
clean tracked tree, fresh output folder, no pressure); the generator control (W = 52 regeneration equals the kit);
preflight; engines; the controls under lean/w3_controls/ (`check 60 1 18 0 = true` rejected as false; the coverage
negative with `ChunksOK 60 129 18 0 4095` failing at the range type; `check 60 129 18 0 = true` proved alone: the
first cost sample, and the first test of K at this width); then the 64 modules in order with the COST-MISS gate
after each; the wrapper; the kit's Check.lean on the wrapper (headline q01_width_le_60).

Predictions, written before the run (W1B's K² law and W2's module figures projected): per chunk about
0.22 s × (129/101)² ≈ 0.36 s of user time, so about 23 s user and 29 s wall per 64-chunk module (sys about a fifth);
64 modules about 31 minutes; peak RSS about 1.3-1.4 GiB per module (memory follows K: 0.91 → 1.01 → 1.11 GiB at
K = 97, 105, 113, about 12.5 MiB per level); the wrapper a few seconds (256 ranges); the checker a few seconds; all
4,096 checks true at K = 129. Counterfactuals: a chunk rejected at K = 129 (provisional; stop); a module above
60 s or 4.5 GiB (COST-MISS; the K² projection fails at 60); per-chunk user time above 0.6 s (the projection is off by
more than the W1B repeat spread allows); memory above 2 GiB per module.

Caps: STAGE 60 MINUTES (a change from W1A's 30, needed by the 64-module count; everything else unchanged): module
180 s wall / 150 s CPU; checker 600 / 540 s; controls 30 / 30 s; RSS stop 6 GiB; cost-miss gate 60 s / 4.5 GiB; one
worker; no retry; no parallelism; no GPU; no submission.

OUTCOME: filled in after the run (CHAT-LEDGER.md).
"""
import hashlib, os, re, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import w1a_harness as H
import w2_harness as G
from w1b_harness import rejected_as_false

W, K, N = 60, 129, 18
CHUNKS = 2 ** (W // 2 - N)                       # 4096
MODULES = CHUNKS // (G.PER_NS * G.NS_PER_MODULE)  # 64
STAGE_S = 60 * 60
LIB = G.LIB


def m_module(rc, text):
    if rc == 0 and 'error' not in text:
        return 'pass', 'built'
    mm = re.search(r'check %d %d %d (\d+) = true' % (W, K, N), text)
    if mm and rejected_as_false(text, 'check %d %d %d %s = true' % (W, K, N, mm.group(1))):
        return 'FAIL', 'PARAMETER-REFUTED-provisional: chunk %s rejected as false at K = %d (not a proof of the negation)' % (mm.group(1), K)
    return 'FAIL', 'build error (exit %d)' % rc


CONTROLS = {
    'neg_k1.lean': "import Ruliology.CellularAutomata.Rule30ZeroBoundaryLanes\nopen Ruliology.CellularAutomata.Rule30ZeroBoundaryLanes\nexample : check 60 1 18 0 = true := by decide +kernel\n",
    'cov_neg.lean': ("import Ruliology.CellularAutomata.Rule30ZeroBoundaryLanes\nopen Ruliology.CellularAutomata.Rule30ZeroBoundaryLanes\n"
                     "theorem cov_neg (h : ChunksOK 60 129 18 0 4095) (x : Nat → Bool) (hx : ∀ k, 60 < k → x k = false) :\n"
                     "    ∃ t, t < 129 ∧ t % 2 = 0 ∧ Ruliology.CellularAutomata.Rule30ZeroBoundary.zrow x t 1 = false :=\n"
                     "  q01_of_chunks 60 129 18 (by decide) h x hx\n"),
    'pos_one.lean': "import Ruliology.CellularAutomata.Rule30ZeroBoundaryLanes\nopen Ruliology.CellularAutomata.Rule30ZeroBoundaryLanes\ntheorem one : check 60 129 18 0 = true := by decide +kernel\n",
}


def m_neg_k1(rc, text):
    return ('pass' if rc != 0 and rejected_as_false(text, 'check 60 1 18 0 = true') else 'FAIL', 'rejected-as-false')


def m_cov_neg(rc, text):
    want = ['type mismatch', 'ChunksOK 60 129 18 0 4095', 'ChunksOK 60 129 18 0 (2 ^ (60 / 2 - 18))']
    return ('pass' if rc != 0 and all(w in text for w in want) else 'FAIL', 'range diagnostic')


def m_pos_one(rc, text):
    if rc == 0 and 'error' not in text:
        return 'pass', 'K = %d suffices for chunk 0' % K
    if rejected_as_false(text, 'check %d %d %d 0 = true' % (W, K, N)):
        return 'FAIL', 'PARAMETER-REFUTED-provisional: chunk 0 rejected as false at K = %d' % K
    return 'FAIL', 'unexpected error kind (exit %d)' % rc


def main():
    H.CAPS['stage_s'] = STAGE_S
    kit = os.path.abspath(sys.argv[1]); out = os.path.abspath(sys.argv[2])
    if os.path.exists(out) and os.listdir(out):
        print('REFUSED: output folder exists and is not empty:', out); sys.exit(3)
    os.makedirs(out, exist_ok=True)
    gen_paths = ['%s/Rule30Certificates/ZeroBoundaryWidth60Chunks%d.lean' % (LIB, m) for m in range(MODULES)] + ['%s/Rule30ZeroBoundaryWidth60.lean' % LIB]
    for rel in gen_paths + ['lean/w3_controls']:
        p = os.path.join(kit, rel)
        if os.path.isdir(p):
            for f in os.listdir(p): os.remove(os.path.join(p, f))
            os.rmdir(p)
        elif os.path.exists(p):
            os.remove(p)
    for m in range(MODULES):
        for ext in ('.olean', '.ilean', '.trace', '.olean.hash', '.ilean.hash'):
            for rel in ('lean/.lake/build/lib/lean/Ruliology/CellularAutomata/Rule30Certificates/ZeroBoundaryWidth60Chunks%d' % m,
                        'lean/.lake/build/lib/lean/Ruliology/CellularAutomata/Rule30ZeroBoundaryWidth60'):
                p = os.path.join(kit, rel + ext)
                if os.path.exists(p): os.remove(p)
    sup = H.Supervisor(kit, out); R = sup.receipts
    R['w3'] = {'W': W, 'K': K, 'n': N, 'chunks': CHUNKS, 'modules': MODULES, 'stage_s': STAGE_S, 'K_status': 'proposed (2W+9); established only by a complete successful check',
               'generator_sha256': H.digest(G.__file__), 'this_sha256': H.digest(os.path.abspath(__file__)), 'files': {}}

    def stop(msg, code=1):
        R['stopped'] = msg; sup.save(); print('STOP:', msg); sys.exit(code)

    commit = H.checked(['git', '-C', kit, 'rev-parse', 'HEAD']).strip()
    dirty = H.subprocess.run(['git', '-C', kit, 'status', '--porcelain'], capture_output=True, text=True).stdout.strip()
    got = {f: H.digest(os.path.join(kit, f)) for f in H.PIN['sources']}
    bad = [f for f, want in H.PIN['sources'].items() if got[f] != want]
    R['pins'] = {'commit': commit, 'tracked_tree_dirty': dirty.splitlines(), 'sources': got, 'bad_sources': bad,
                 'deps_built': {d: os.path.exists(os.path.join(kit, d)) for d in H.DEPS}}
    sup.save()
    if commit != H.PIN['commit'] or dirty or bad or not all(R['pins']['deps_built'].values()):
        stop('pin mismatch: commit %s dirty %r bad %s deps %s' % (commit[:8], bool(dirty), bad, R['pins']['deps_built']))
    if H.pressure_bad(sup.baseline):
        stop('serious memory pressure at launch')
    ok, detail = G.generator_control(kit); R['generator_control'] = {'ok': ok, 'detail': detail}; sup.save()
    if not ok:
        stop('generator control failed: %s' % detail)
    r = sup.register(H.preflight())
    if r['verdict'] != 'pass':
        stop('preflight failed')
    r, _ = H.engines_control(); sup.register(r)
    if r['verdict'] != 'pass':
        stop('engines control failed')

    cdir = os.path.join(kit, 'lean', 'w3_controls'); os.makedirs(cdir, exist_ok=True)
    for nm, src in CONTROLS.items():
        open(os.path.join(cdir, nm), 'w').write(src); R['w3']['files']['w3_controls/' + nm] = hashlib.sha256(src.encode()).hexdigest()
    sup.save()
    for nm, matcher in (('neg_k1', m_neg_k1), ('cov_neg', m_cov_neg), ('pos_one', m_pos_one)):
        r = sup.run_step(nm, ['lake', 'env', 'lean', 'w3_controls/%s.lean' % nm], os.path.join(kit, 'lean'), H.CAPS['control_wall_s'], H.CAPS['control_cpu_s'], matcher)
        if r['verdict'] != 'pass':
            stop('control %s: %s (%s) %s' % (nm, r['verdict'], r['reason'], r.get('match_note', '')))

    for m in range(MODULES):
        src = G.chunk_module(W, K, N, m); p = os.path.join(kit, gen_paths[m])
        open(p, 'w').write(src); R['w3']['files'][gen_paths[m]] = hashlib.sha256(src.encode()).hexdigest()
    src = G.wrapper(W, K, N, MODULES, MODULES * G.NS_PER_MODULE, K - 1); open(os.path.join(kit, gen_paths[-1]), 'w').write(src)
    R['w3']['files'][gen_paths[-1]] = hashlib.sha256(src.encode()).hexdigest()
    untracked = H.subprocess.run(['git', '-C', kit, 'status', '--porcelain'], capture_output=True, text=True).stdout.strip().splitlines()
    R['w3']['untracked_after_generation'] = untracked; sup.save()
    allowed = set(gen_paths) | {'lean/w3_controls/'}
    extra = [u for u in untracked if not (u.startswith('?? ') and u[3:] in allowed)]
    if extra:
        stop('unexpected tracked-tree changes after generation: %s' % extra)
    sup.art_baseline = H.snapshot(kit, out)

    for m in range(MODULES):
        mod = 'Ruliology.CellularAutomata.Rule30Certificates.ZeroBoundaryWidth60Chunks%d' % m
        olean = os.path.join(kit, 'lean/.lake/build/lib/lean/Ruliology/CellularAutomata/Rule30Certificates/ZeroBoundaryWidth60Chunks%d.olean' % m)
        r = sup.run_step('build_Chunks%d' % m, ['lake', 'build', mod], kit, H.CAPS['module_wall_s'], H.CAPS['module_cpu_s'], m_module)
        exists = os.path.exists(olean)
        r['olean'] = {'exists_after': exists, 'bytes': os.path.getsize(olean) if exists else None, 'sha256': H.digest(olean) if exists else None}
        r['cost_miss'] = H.cost_miss(r) if r['verdict'] == 'pass' else None; sup.save()
        if r['verdict'] != 'pass' or not exists:
            stop('module %d: %s (%s) %s' % (m, r['verdict'], r['reason'], r.get('match_note', '')))
        if r['cost_miss']:
            stop('COST-MISS after module %d: wall %.1f s, peak %.2f GiB; stage ended' % (m, r['wall_s'], r['peak_rss_bytes_either'] / H.GIB), 2)
    r = sup.run_step('build_wrapper', ['lake', 'build', 'Ruliology.CellularAutomata.Rule30ZeroBoundaryWidth60'], kit, H.CAPS['module_wall_s'], H.CAPS['module_cpu_s'], H.m_pass)
    if r['verdict'] != 'pass':
        stop('wrapper: %s (%s)' % (r['verdict'], r['reason']))
    headline = 'Ruliology.CellularAutomata.Rule30ZeroBoundaryWidth60.q01_width_le_60'
    H.HEADLINE = headline
    r = sup.run_step('checker', ['lake', 'env', 'lean', '--run', 'Check.lean', 'Ruliology.CellularAutomata.Rule30ZeroBoundaryWidth60', '--claim', 'partial', '--headline', headline],
                     kit, H.CAPS['checker_wall_s'], H.CAPS['checker_cpu_s'], H.m_checker)
    if r['verdict'] != 'pass':
        stop('checker: %s (%s) %s' % (r['verdict'], r['reason'], r.get('match_note', '')))
    R['complete'] = True; sup.save()
    print('DONE: width-60 certificate built and checked here (not submitted)')


if __name__ == '__main__':
    main()
