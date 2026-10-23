#!/usr/bin/env python3
"""W2, revision 1: a width-56 zero-boundary chunk certificate, built and kernel-checked on the M5 only, as a dry
certificate and a cost receipt, under the W1A supervisor (tests/probes/wolfram/w1a_harness.py revision 4: its
Supervisor, guards, caps and terminal policy). Proposed in L791, specified here for GPT's agreement (GC1719: a
complete collection of kernel checks plus sound assembly would itself establish the bound; no prior proof of K is
required). NOT an agreed job until GPT accepts this exact file; it runs nothing on import; nothing is submitted.

Usage:  python3 w2_harness.py KIT_CLONE OUT_DIR          (OUT_DIR must not exist or must be empty)

What is built. The kit's width-52 certificate is 256 chunk checks `check 52 97 18 c = true` by `decide +kernel`,
grouped 16 to a namespace `Rule30ZeroBoundaryWidth52.C<j>` with `range : ChunksOK 52 97 18 (16 j) 16` as a balanced
`chunksOK_append` tree of `chunksOK_one`, four namespaces to a module, and a wrapper whose `all_chunks` appends the
sixteen ranges and feeds `q01_of_chunks`. W2 generates the same shape at W = 56, n = 18, K = 101 (the bound 100
the kit author reports for their own W <= 56 check, exclusive; 2^(28 - 18) = 1,024 chunks): 64 namespaces
`Rule30ZeroBoundaryWidth56.C<j>` of 16 chunks, 16 modules `Rule30Certificates/ZeroBoundaryWidth56Chunks<m>.lean`
of 64 chunks (four namespaces each), and a wrapper `Rule30ZeroBoundaryWidth56.lean` with
  theorem all_chunks : ChunksOK 56 101 18 0 1024   (a balanced append tree of the 64 ranges)
  theorem q01_width_le_56 (x) (hx : ∀ k, 56 < k → x k = false) : ∃ t, t ≤ 100 ∧ t % 2 = 0 ∧ zrow x t 1 = false
  theorem not_inX_of_width_le_56 … ¬ InX x
exactly as the kit's width-52 wrapper does. The generator is this file (`chunk_module`, `wrapper`); its output at
W = 52, K = 97 must reproduce the kit's own theorem and range lines (checked before anything runs, as a control on
the generator). Every generated file's sha256 is in the receipt. The files are written as UNTRACKED files inside the
clone's library tree (lean/Ruliology/CellularAutomata/…), the only way `lake build` and the kit's Check.lean can see
them; the pin gate therefore requires the tracked tree clean AND the untracked set to be exactly the generated files.

Order, stopping at the first unaccepted step, no retry:
  0. pins (commit, toolchain, the seven pinned sources, deps built, clean tracked tree, fresh output folder, no
     pressure); generator control (W = 52 regeneration equals the kit's lines); preflight; engines control;
  1. controls (untracked files under lean/w2_controls/, `lake env lean`): the negative `check 56 1 18 0 = true` must
     be rejected as false (either form, GC1718's scope); the coverage negative `q01_of_chunks 56 101 18 _ (h :
     ChunksOK 56 101 18 0 1023)` must fail at the range type; the positive `check 56 101 18 0 = true` by
     `decide +kernel` must compile (one chunk, the first cost sample at this K and width);
  2. the sixteen chunk modules, `lake build <module>`, in order 0..15 (fresh compilation evidenced); after each, the
     COST-MISS gate (60 s / 4.5 GiB) ends the stage; a module that FAILS because the kernel rejects some chunk's
     check as false is recorded as PARAMETER-REFUTED-provisional for that chunk (the exact statement read from the
     log; GC1718: a rejected proof term is not a proof of the negation) and the stage stops; any other failure is
     FAIL and stops;
  3. the wrapper, `lake build`;
  4. the kit's Check.lean on the wrapper, headline q01_width_le_56, claim partial: its JSON must say verdict pass,
     the headline found and ok, axioms within the standard three, newAxioms empty, replay ok (the replay covers the
     wrapper's own constants; the 1,024 chunk checks are kernel-checked at compilation, step 2).
No width beyond 56, no submission, no parallelism, no GPU.

Predictions, written before the run (W1B's measurements projected one step): each 64-chunk module about
64 x 0.19 x (101/97)^2 ≈ 13 s of CPU plus overhead, 14-18 s wall, peak RSS about 1.0-1.2 GiB (memory follows K);
sixteen modules about 4-5 minutes; the wrapper about a second; the checker a few seconds; all 1,024 checks true
(the kit author's report); total stage under 8 minutes. Counterfactuals: a chunk rejected as false at K = 101
(provisional parameter failure: a rejected proof term alone does not prove that the physical bound exceeds 100 on
that chunk, GC1721; the generator or the lane encoding would be the first suspect, since the kit author reports
100 suffices); a module above
60 s or 4.5 GiB (COST-MISS; the projection fails at 56); memory above 2 GiB per module (the per-declaration memory
does not add across a module, which this stage tests as a side result).

Caps (W1A's): stage 30 min; module 180 s wall / 150 s CPU; checker 600 / 540 s; controls 30 / 30 s; RSS stop 6 GiB;
cost-miss gate 60 s / 4.5 GiB; one worker; no retry.

OUTCOME (W2 launch 1, 2026-10-23 19:09-19:14 BST, M5, this file at sha256 491edf3d… when it ran, GPT's acceptance
GC1721, Local's L793; receipts in width/w2-20261023-1909/ and the store at workers/local/w2-20261023-1909/;
CHAT-LEDGER.md L794). Complete, every step accepted, 294 s; no final problems, no cost miss; pressure level 1 and
swap unchanged throughout. Pins equal; the generator control (W = 52 regeneration equals the kit's four modules
and wrapper lines) passed; preflight and engines passed; neg_k1 rejected as false (kernel form), cov_neg failed at
the range type, pos_one proved (0.34 s user, 0.95 GiB). The sixteen width-56 chunk modules, each 64 checks
`check 56 101 18 c = true` by `decide +kernel`, compiled fresh in 17.1-18.0 s real, 14.0-14.2 s user, 3.5-3.7 s sys,
peak RSS 1.07-1.13 GiB per lean process (sampled group 1.67-1.77 GiB), one lean process each; 14.1 s of user time
per 64 chunks is 0.22 s per chunk at K = 101. The wrapper 1.0 s; the kit's Check.lean on it 1.5 s: verdict pass,
headline q01_width_le_56 found and ok on propext, Classical.choice, Quot.sound, newAxioms [], replay ok (the
wrapper's own constants; the 1,024 chunk checks were kernel-checked at compilation). So `Q01` holds for every start
of width <= 56 with a white depth-1 cell at an even time <= 100, kernel-checked on this machine: a dry certificate
in the kit's own shape, consistent with the kit author's unpublished W <= 56 check (bound 100, about 345 s on their
machine), not submitted. Predictions: 14-18 s and 1.0-1.2 GiB per module (held: 17.7 s, 1.1 GiB), 4-5 minutes for
the sixteen (held: 4.7), the stage under 8 minutes (held: 4.9), all checks true (held). Per-chunk cost 0.22 s at
K = 101 against W1B's 0.19 s at K = 97 x (101/97)^2 = 0.21 s: the module average carries the per-file overhead
amortized over 64 chunks.
"""
import hashlib, json, os, re, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import w1a_harness as H

W, K, N = 56, 101, 18
CHUNKS = 2 ** (W // 2 - N)          # 1024
PER_NS, NS_PER_MODULE = 16, 4
MODULES = CHUNKS // (PER_NS * NS_PER_MODULE)   # 16
LIB = 'lean/Ruliology/CellularAutomata'
NAME52 = 'Rule30ZeroBoundaryWidth52'


def name(W):
    return 'Rule30ZeroBoundaryWidth%d' % W


def append_tree(items, lo_of, size_of):
    """A balanced chunksOK_append tree over contiguous items (each a Lean term string)."""
    if len(items) == 1:
        return items[0]
    h = len(items) // 2
    return '(chunksOK_append %s %s)' % (append_tree(items[:h], lo_of, size_of), append_tree(items[h:], lo_of, size_of))


def chunk_module(W, K, n, m, per_ns=PER_NS, ns_per_module=NS_PER_MODULE):
    """Module m: namespaces C<j> for j in [m*ns_per_module, (m+1)*ns_per_module), per_ns chunks each."""
    lines = ['import Ruliology.CellularAutomata.Rule30ZeroBoundaryLanes', '',
             '/-! `Q01` at width `%d`: chunk checks of module `%d` (generated by tests/probes/wolfram/w2_harness.py). -/' % (W, m), '',
             'namespace Ruliology.CellularAutomata.%s' % name(W), '', 'open Rule30ZeroBoundaryLanes', '']
    for j in range(m * ns_per_module, (m + 1) * ns_per_module):
        lo = j * per_ns
        lines += ['namespace C%d' % j, '']
        for c in range(lo, lo + per_ns):
            lines.append('theorem c%d : check %d %d %d %d = true := by decide +kernel' % (c, W, K, n, c))
        lines += ['', 'theorem range : ChunksOK %d %d %d %d %d :=' % (W, K, n, lo, per_ns),
                  '  ' + append_tree(['(chunksOK_one c%d)' % c for c in range(lo, lo + per_ns)], None, None), '',
                  'end C%d' % j, '']
    lines += ['end Ruliology.CellularAutomata.%s' % name(W), '']
    return '\n'.join(lines)


def wrapper(W, K, n, n_modules, n_ns, bound):
    lines = ['import Ruliology.CellularAutomata.Rule30Certificates.ZeroBoundaryWidth%dChunks%d' % (W, m) for m in range(n_modules)]
    lines += ['', '/-! `Q01` for every start of width at most `%d` (kernel-checked; generated by tests/probes/wolfram/w2_harness.py). -/' % W, '',
              'namespace Ruliology.CellularAutomata', 'namespace %s' % name(W), '', 'open Rule30ZeroBoundaryLanes Rule30ZeroBoundary', '',
              'theorem all_chunks : ChunksOK %d %d %d 0 %d :=' % (W, K, n, n_ns * PER_NS),
              '  ' + append_tree(['C%d.range' % j for j in range(n_ns)], None, None), '',
              'theorem q01_width_le_%d (x : Nat → Bool) (hx : ∀ k, %d < k → x k = false) :' % (W, W),
              '    ∃ t, t ≤ %d ∧ t %% 2 = 0 ∧ zrow x t 1 = false := by' % bound,
              '  obtain ⟨t, ht, he, hz⟩ := q01_of_chunks %d %d %d (by decide) all_chunks x hx' % (W, K, n),
              '  exact ⟨t, by omega, he, hz⟩', '',
              'theorem not_inX_of_width_le_%d (x : Nat → Bool) (hx : ∀ k, %d < k → x k = false) : ¬ InX x := by' % (W, W),
              '  intro hX', '  obtain ⟨t, _, he, hz⟩ := q01_width_le_%d x hx' % W,
              '  have := hX (t / 2)', '  rw [show 2 * (t / 2) = t by omega, hz] at this', '  exact absurd this (by decide)', '',
              'end %s' % name(W), 'end Ruliology.CellularAutomata', '']
    return '\n'.join(lines)


def theorem_lines(text):
    return [l.strip() for l in text.splitlines() if l.strip().startswith(('theorem ', '(chunksOK_append', 'namespace C', 'end C'))]


def generator_control(kit):
    """The generator at W = 52, K = 97 must reproduce the kit's own theorem, range and namespace lines, module by module."""
    ok = True; detail = {}
    for m in range(4):
        mine = theorem_lines(chunk_module(52, 97, 18, m))
        theirs = theorem_lines(open(os.path.join(kit, LIB, 'Rule30Certificates/ZeroBoundaryWidth52Chunks%d.lean' % m)).read())
        detail['Chunks%d' % m] = (mine == theirs, len(mine), len(theirs))
        ok = ok and mine == theirs
    mine = [l for l in theorem_lines(wrapper(52, 97, 18, 4, 16, 96)) if 'all_chunks' in l or 'chunksOK_append' in l]
    theirs = [l for l in theorem_lines(open(os.path.join(kit, LIB, 'Rule30ZeroBoundaryWidth52.lean')).read()) if 'all_chunks' in l or 'chunksOK_append' in l]
    detail['wrapper_all_chunks'] = (mine == theirs, len(mine), len(theirs))
    return ok and mine == theirs, detail


def m_module(rc, text):
    """pass on a clean build; PARAMETER-REFUTED-provisional when the kernel rejected a chunk's check as false."""
    if rc == 0 and 'error' not in text:
        return 'pass', 'built'
    mm = re.search(r'check %d %d %d (\d+) = true' % (W, K, N), text)
    from w1b_harness import rejected_as_false
    if mm and rejected_as_false(text, 'check %d %d %d %s = true' % (W, K, N, mm.group(1))):
        return 'FAIL', 'PARAMETER-REFUTED-provisional: chunk %s rejected as false at K = %d (not a proof of the negation)' % (mm.group(1), K)
    return 'FAIL', 'build error (exit %d)' % rc


CONTROLS = {
    'neg_k1.lean': "import Ruliology.CellularAutomata.Rule30ZeroBoundaryLanes\nopen Ruliology.CellularAutomata.Rule30ZeroBoundaryLanes\nexample : check 56 1 18 0 = true := by decide +kernel\n",
    'cov_neg.lean': ("import Ruliology.CellularAutomata.Rule30ZeroBoundaryLanes\nopen Ruliology.CellularAutomata.Rule30ZeroBoundaryLanes\n"
                     "theorem cov_neg (h : ChunksOK 56 101 18 0 1023) (x : Nat → Bool) (hx : ∀ k, 56 < k → x k = false) :\n"
                     "    ∃ t, t < 101 ∧ t % 2 = 0 ∧ Ruliology.CellularAutomata.Rule30ZeroBoundary.zrow x t 1 = false :=\n"
                     "  q01_of_chunks 56 101 18 (by decide) h x hx\n"),
    'pos_one.lean': "import Ruliology.CellularAutomata.Rule30ZeroBoundaryLanes\nopen Ruliology.CellularAutomata.Rule30ZeroBoundaryLanes\ntheorem one : check 56 101 18 0 = true := by decide +kernel\n",
}


def m_neg_k1(rc, text):
    from w1b_harness import rejected_as_false
    return ('pass' if rc != 0 and rejected_as_false(text, 'check 56 1 18 0 = true') else 'FAIL', 'rejected-as-false')


def m_cov_neg(rc, text):
    want = ['type mismatch', 'ChunksOK 56 101 18 0 1023', 'ChunksOK 56 101 18 0 (2 ^ (56 / 2 - 18))']
    return ('pass' if rc != 0 and all(w in text for w in want) else 'FAIL', 'range diagnostic')


def main():
    kit = os.path.abspath(sys.argv[1]); out = os.path.abspath(sys.argv[2])
    if os.path.exists(out) and os.listdir(out):
        print('REFUSED: output folder exists and is not empty:', out); sys.exit(3)
    os.makedirs(out, exist_ok=True)
    gen_paths = ['%s/Rule30Certificates/ZeroBoundaryWidth56Chunks%d.lean' % (LIB, m) for m in range(MODULES)] + ['%s/Rule30ZeroBoundaryWidth56.lean' % LIB]
    for rel in gen_paths + ['lean/w2_controls']:
        p = os.path.join(kit, rel)
        if os.path.isdir(p):
            for f in os.listdir(p): os.remove(os.path.join(p, f))
            os.rmdir(p)
        elif os.path.exists(p):
            os.remove(p)
    for m in range(MODULES):
        for ext in ('.olean', '.ilean', '.trace', '.olean.hash', '.ilean.hash'):
            for rel in ('lean/.lake/build/lib/lean/Ruliology/CellularAutomata/Rule30Certificates/ZeroBoundaryWidth56Chunks%d' % m,
                        'lean/.lake/build/lib/lean/Ruliology/CellularAutomata/Rule30ZeroBoundaryWidth56'):
                p = os.path.join(kit, rel + ext)
                if os.path.exists(p): os.remove(p)
    sup = H.Supervisor(kit, out); R = sup.receipts
    R['w2'] = {'W': W, 'K': K, 'n': N, 'chunks': CHUNKS, 'modules': MODULES, 'generator_sha256': H.digest(os.path.abspath(__file__)), 'files': {}}

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
    ok, detail = generator_control(kit); R['generator_control'] = {'ok': ok, 'detail': detail}; sup.save()
    if not ok:
        stop('generator control failed: the W = 52 regeneration differs from the kit: %s' % detail)
    r = sup.register(H.preflight())
    if r['verdict'] != 'pass':
        stop('preflight failed')
    r, _ = H.engines_control(); sup.register(r)
    if r['verdict'] != 'pass':
        stop('engines control failed')

    cdir = os.path.join(kit, 'lean', 'w2_controls'); os.makedirs(cdir, exist_ok=True)
    for nm, src in CONTROLS.items():
        open(os.path.join(cdir, nm), 'w').write(src); R['w2']['files']['w2_controls/' + nm] = hashlib.sha256(src.encode()).hexdigest()
    sup.save()
    for nm, matcher in (('neg_k1', m_neg_k1), ('cov_neg', m_cov_neg), ('pos_one', H.m_pass)):
        r = sup.run_step(nm, ['lake', 'env', 'lean', 'w2_controls/%s.lean' % nm], os.path.join(kit, 'lean'), H.CAPS['control_wall_s'], H.CAPS['control_cpu_s'], matcher)
        if r['verdict'] != 'pass':
            stop('control %s: %s (%s)' % (nm, r['verdict'], r['reason']))

    # generate the modules and the wrapper (untracked, inside the library tree), record their digests
    for m in range(MODULES):
        src = chunk_module(W, K, N, m); p = os.path.join(kit, gen_paths[m])
        open(p, 'w').write(src); R['w2']['files'][gen_paths[m]] = hashlib.sha256(src.encode()).hexdigest()
    src = wrapper(W, K, N, MODULES, MODULES * NS_PER_MODULE, K - 1); open(os.path.join(kit, gen_paths[-1]), 'w').write(src)
    R['w2']['files'][gen_paths[-1]] = hashlib.sha256(src.encode()).hexdigest()
    untracked = H.subprocess.run(['git', '-C', kit, 'status', '--porcelain'], capture_output=True, text=True).stdout.strip().splitlines()
    R['w2']['untracked_after_generation'] = untracked; sup.save()
    allowed = set(gen_paths) | {'lean/w2_controls/'}
    extra = [u for u in untracked if not (u.startswith('?? ') and u[3:] in allowed)]
    if extra:
        stop('unexpected tracked-tree changes after generation: %s' % extra)
    sup.art_baseline = H.snapshot(kit, out)

    for m in range(MODULES):
        mod = 'Ruliology.CellularAutomata.Rule30Certificates.ZeroBoundaryWidth56Chunks%d' % m
        olean = os.path.join(kit, 'lean/.lake/build/lib/lean/Ruliology/CellularAutomata/Rule30Certificates/ZeroBoundaryWidth56Chunks%d.olean' % m)
        r = sup.run_step('build_Chunks%d' % m, ['lake', 'build', mod], kit, H.CAPS['module_wall_s'], H.CAPS['module_cpu_s'], m_module)
        exists = os.path.exists(olean)
        r['olean'] = {'exists_after': exists, 'bytes': os.path.getsize(olean) if exists else None, 'sha256': H.digest(olean) if exists else None}
        r['cost_miss'] = H.cost_miss(r) if r['verdict'] == 'pass' else None; sup.save()
        if r['verdict'] != 'pass' or not exists:
            stop('module %d: %s (%s) %s' % (m, r['verdict'], r['reason'], r.get('match_note', '')))
        if r['cost_miss']:
            stop('COST-MISS after module %d: wall %.1f s, peak %.2f GiB; stage ended' % (m, r['wall_s'], r['peak_rss_bytes_either'] / H.GIB), 2)
    r = sup.run_step('build_wrapper', ['lake', 'build', 'Ruliology.CellularAutomata.Rule30ZeroBoundaryWidth56'], kit, H.CAPS['module_wall_s'], H.CAPS['module_cpu_s'], H.m_pass)
    if r['verdict'] != 'pass':
        stop('wrapper: %s (%s)' % (r['verdict'], r['reason']))
    headline = 'Ruliology.CellularAutomata.Rule30ZeroBoundaryWidth56.q01_width_le_56'
    H.HEADLINE = headline
    r = sup.run_step('checker', ['lake', 'env', 'lean', '--run', 'Check.lean', 'Ruliology.CellularAutomata.Rule30ZeroBoundaryWidth56', '--claim', 'partial', '--headline', headline],
                     kit, H.CAPS['checker_wall_s'], H.CAPS['checker_cpu_s'], H.m_checker)
    if r['verdict'] != 'pass':
        stop('checker: %s (%s) %s' % (r['verdict'], r['reason'], r.get('match_note', '')))
    R['complete'] = True; sup.save()
    print('DONE: width-56 certificate built and checked here (not submitted)')


if __name__ == '__main__':
    main()
