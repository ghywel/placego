#!/usr/bin/env python3
"""W5, revision 1: the width-60 chunk certificate at the EXACT death bound, K = 115 (t <= 114), for GPT's design read:
W3's harness (tests/probes/wolfram/w3_harness.py, the executed version a38615df…) with K = 129 replaced by K = 115 and
the controls' literals following K; nothing else changed (the diff against w3_harness.py is the K constants, the
control strings' numbers, this docstring and the output name). Lane D-exact (L805 to L812): D1's census at width 60
over all 4,096 chunks gave the maximum elimination level 114 with the physically validated witness 0xe77a4e77b8f99b5
(dies at 114), so the exact value is D(60) = 114 if every chunk check passes at K = 115. NOT an agreed job until GPT
accepts this exact file; it runs nothing on import; nothing is submitted.

If this holds, it changes the width-60 upper bound from 128 (W3) to 114 and, with the witness module (d2_witness.py
case 60), makes D(60) = 114 kernel-checked exact (LR row). Run in the clean clone kit-w4-a (cc1e0e0, deps built), NOT
in kit-w1a, so W3's K = 129 objects stay untouched; the wrapper's module name is the generator's
`Rule30ZeroBoundaryWidth60` with bound 114 in that clone only.

Predictions (W3's figures scaled by (115/129)^2): about 0.29 s of user time per chunk, 18.5 s user and 23 s wall per
64-chunk module, 64 modules about 25 minutes, lean RSS about 1.3 GiB per module; wrapper and checker seconds; all
4,096 checks true at K = 115 (D1's census found no lane above 114 and the census is the same computation in Python;
counterfactual: a chunk rejected at 115 would be an instrument discrepancy between the Python engine and the kernel,
stop and dig; a module above 60 s or 4.5 GiB is a COST-MISS, stop). STAGE 30 MINUTES (the heartbeat's bound; W3 took
30.8 at K = 129, so this is predicted inside by about five minutes; a stage deadline gives UNKNOWN and a later agreement
on the W4 pair path as a queue, never an extension of this run).

OUTCOME (MEASURED, run w5-20261023-2146 in kit-w4-a, launched 21:46 BST at GC1736/GC1737's accepted versions, 1,295 s
in all, complete, no stop; receipt sha256 e1c6821fbc991f6a81239e4e6853996fa5c303f60cb3cc81622a8b45f516027f): generator control true; pins ok;
controls neg_k1 rejected-as-false, cov_neg the range diagnostic, pos_one proved at K = 115 (1.12 GiB); all 64 modules
pass and fresh: real 18.8-21.7 s (mean 19.4), user 15.4-17.4, sys mean 4.1, lean RSS 1.26-1.33 GiB, sampled group
peak 1.98 GiB, no cost miss, one lean process at most; wrapper 0.9 s; Check.lean on Rule30ZeroBoundaryWidth60 with
headline q01_width_le_60: pass, standard axioms, newAxioms [], replay 5 constants ok (bound 114). Against the
predictions: 23 s wall per module predicted, 19.4 measured; 25 minutes predicted, 21.6 measured; 1.3 GiB predicted,
1.26-1.33 measured; all 4,096 checks true at K = 115 as predicted. The handoff for D2 case 60 (L818): 68 generated
files hash-equal to this receipt, the 65 sources kept in the clone, the controls removed, objects and receipt
archived, the wrapper object sha256 af74d7b8… recorded before D2 and reported by it.
"""
import hashlib, os, re, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import w1a_harness as H
import w2_harness as G
from w1b_harness import rejected_as_false

W, K, N = 60, 115, 18
CHUNKS = 2 ** (W // 2 - N)                       # 4096
MODULES = CHUNKS // (G.PER_NS * G.NS_PER_MODULE)  # 64
STAGE_S = 30 * 60
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
                     "theorem cov_neg (h : ChunksOK 60 115 18 0 4095) (x : Nat → Bool) (hx : ∀ k, 60 < k → x k = false) :\n"
                     "    ∃ t, t < 115 ∧ t % 2 = 0 ∧ Ruliology.CellularAutomata.Rule30ZeroBoundary.zrow x t 1 = false :=\n"
                     "  q01_of_chunks 60 115 18 (by decide) h x hx\n"),
    'pos_one.lean': "import Ruliology.CellularAutomata.Rule30ZeroBoundaryLanes\nopen Ruliology.CellularAutomata.Rule30ZeroBoundaryLanes\ntheorem one : check 60 115 18 0 = true := by decide +kernel\n",
}


def m_neg_k1(rc, text):
    return ('pass' if rc != 0 and rejected_as_false(text, 'check 60 1 18 0 = true') else 'FAIL', 'rejected-as-false')


def m_cov_neg(rc, text):
    want = ['type mismatch', 'ChunksOK 60 115 18 0 4095', 'ChunksOK 60 115 18 0 (2 ^ (60 / 2 - 18))']
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
    for rel in gen_paths + ['lean/w5_controls']:
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
    R['w5'] = {'W': W, 'K': K, 'n': N, 'chunks': CHUNKS, 'modules': MODULES, 'stage_s': STAGE_S, 'K_status': 'D1 census maximum 114 + 1; established only by a complete successful check',
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

    cdir = os.path.join(kit, 'lean', 'w5_controls'); os.makedirs(cdir, exist_ok=True)
    for nm, src in CONTROLS.items():
        open(os.path.join(cdir, nm), 'w').write(src); R['w5']['files']['w5_controls/' + nm] = hashlib.sha256(src.encode()).hexdigest()
    sup.save()
    for nm, matcher in (('neg_k1', m_neg_k1), ('cov_neg', m_cov_neg), ('pos_one', m_pos_one)):
        r = sup.run_step(nm, ['lake', 'env', 'lean', 'w5_controls/%s.lean' % nm], os.path.join(kit, 'lean'), H.CAPS['control_wall_s'], H.CAPS['control_cpu_s'], matcher)
        if r['verdict'] != 'pass':
            stop('control %s: %s (%s) %s' % (nm, r['verdict'], r['reason'], r.get('match_note', '')))

    for m in range(MODULES):
        src = G.chunk_module(W, K, N, m); p = os.path.join(kit, gen_paths[m])
        open(p, 'w').write(src); R['w5']['files'][gen_paths[m]] = hashlib.sha256(src.encode()).hexdigest()
    src = G.wrapper(W, K, N, MODULES, MODULES * G.NS_PER_MODULE, K - 1); open(os.path.join(kit, gen_paths[-1]), 'w').write(src)
    R['w5']['files'][gen_paths[-1]] = hashlib.sha256(src.encode()).hexdigest()
    untracked = H.subprocess.run(['git', '-C', kit, 'status', '--porcelain'], capture_output=True, text=True).stdout.strip().splitlines()
    R['w5']['untracked_after_generation'] = untracked; sup.save()
    allowed = set(gen_paths) | {'lean/w5_controls/'}
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
    print('DONE: width-60 certificate at bound 114 built and checked here (not submitted)')


if __name__ == '__main__':
    main()
