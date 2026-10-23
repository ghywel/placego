#!/usr/bin/env python3
"""W1B: the W-dependence of one chunk declaration of the kit's lane checker, measured on the M5 under the W1A
supervisor (tests/probes/wolfram/w1a_harness.py revision 4, its Supervisor, guards, caps and terminal policy), as
proposed in CHAT-LEDGER.md L785 and frozen in L786 for GPT's agreement. NOT an agreed job until GPT accepts this
exact file; it runs nothing on import.

Usage:  python3 w1b_harness.py KIT_CLONE OUT_DIR          (OUT_DIR must not exist or must be empty)

The question. W1A measured 14.5 s per 64-chunk module at W = 52, n = 18, K = 97: about 0.23 s per chunk as a module
average, with compile and import overhead inside it. W1B isolates ONE declaration `check W K n c = true` by
`decide +kernel` per file and measures how its cost moves with W, with K chosen by one rule for every width and the
overhead measured separately, so that the growth of the chunk design can be read before any width past 52 is
attempted. No module of the kit is rebuilt; nothing is added to the library; every file is untracked under the
clone's lean/w1b/ and compiled with `lake env lean <file>` exactly as the W1A controls were.

The generator (this file, function `decl`): the text of a chunk declaration is
    import Ruliology.CellularAutomata.Rule30ZeroBoundaryLanes
    open Ruliology.CellularAutomata.Rule30ZeroBoundaryLanes
    theorem w{W}_k{K}_n{n}_c{c} : check {W} {K} {n} {c} = true := by decide +kernel
which is byte for byte the shape of the kit's own data modules (one `theorem cN : check 52 97 18 N = true := by
decide +kernel` per chunk; the kit holds no other generator, its data modules ARE such lines). The receipt records
every generated file's sha256.

The selection rule, matched across widths:
  n = 18 at every width (lane word 2^18 bits, constant; the chunk count is 2^(W/2 - 18): 4, 16, 64, 256, 1024);
  K = 2 W + 9 at every width (the kit's own linear bound `q01_width_le_52_linear` says t <= 2 W + 8 suffices at 52;
      K is the exclusive bound, so 2 W + 9); the kit's K = 97 at W = 52 is measured too, as the bridge to W1A;
  c = 0, the middle chunk 2^(W/2 - 19), and the last chunk 2^(W/2 - 18) - 1, at every width (first, middle, last);
  W = 40, 44, 48, 52; and 56 for ONE chunk (c = 0) only if GPT agrees (it is a single declaration, not a width-56
      certificate; a full width 56 is 1,024 chunks and is not part of W1B).
Overhead controls at every width: an empty file (import + open only) and the same declaration twice in one file,
so that declaration cost = (two) - (one) and import overhead = (empty); each measured once.
Negative control at every width: `check W 1 18 0 = true` must FAIL with "proved that the proposition … is false"
(chunk 0 holds a lane black at depth 1 at time 0, which no K = 1 bound can kill); its cost is recorded, not compared.
Order: W = 52 at K = 97 first (the bridge: c = 0 must pass and cost about the W1A per-chunk average), then widths
ascending, within a width: empty, negative, c = 0, c = middle, c = last, double.

Predictions, written before the run (hypotheses): per-declaration wall grows about like K^2 at fixed n (the
checker visits k entries at level k, GPT's reading), so at K = 2 W + 9 the ratios 40 : 44 : 48 : 52 : 56 are about
1 : 1.19 : 1.39 : 1.61 : 1.85 (89^2 : 97^2 : 105^2 : 113^2 : 121^2), and W = 52 at K = 113 costs about 1.36 x its
K = 97 cost; c = 0, middle, last differ by less than 2 x at one width (lanes die at different times, the checker
does not stop early); memory per declaration stays near the W1A per-process peak (about 1.1 GiB) and does not grow
with W; the empty file costs under 1 s. Counterfactuals: growth faster than K^2 times a constant (for example a
factor above 3 x between 40 and 56) says the chunk design cannot reach past 56 on this machine within the kit's
verifier budget and the lane stops; memory growing with W says the whole-declaration kernel cache is the limit, as
CL600 found for the channel bound; a c-dependence above 2 x says one chunk per width is not a matched sample.

Caps (W1A's): stage 30 min; each declaration file 180 s wall / 150 s CPU; RSS stop 6 GiB; the cost-miss gate
(60 s / 4.5 GiB) ends the stage after the declaration that misses; one worker; no retry.

OUTCOME: filled in after the run (CHAT-LEDGER.md).
"""
import hashlib, json, os, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import w1a_harness as H

WIDTHS = [40, 44, 48, 52]
WIDTH56_SINGLE = False          # set to True only on GPT's explicit agreement (L786 asks)
N = 18


def K_rule(W):
    return 2 * W + 9


def chunks(W):
    return 2 ** (W // 2 - N)


def decl(W, K, n, c):
    return ("import Ruliology.CellularAutomata.Rule30ZeroBoundaryLanes\n"
            "open Ruliology.CellularAutomata.Rule30ZeroBoundaryLanes\n"
            "theorem w%d_k%d_n%d_c%d : check %d %d %d %d = true := by decide +kernel\n" % (W, K, n, c, W, K, n, c))


def empty():
    return "import Ruliology.CellularAutomata.Rule30ZeroBoundaryLanes\nopen Ruliology.CellularAutomata.Rule30ZeroBoundaryLanes\n"


def double(W, K, n, c):
    return decl(W, K, n, c) + "theorem w%d_k%d_n%d_c%d_again : check %d %d %d %d = true := by decide +kernel\n" % (W, K, n, c, W, K, n, c)


def negative(W):
    return ("import Ruliology.CellularAutomata.Rule30ZeroBoundaryLanes\n"
            "open Ruliology.CellularAutomata.Rule30ZeroBoundaryLanes\n"
            "-- must FAIL: chunk 0 holds a lane black at depth 1 at time 0; K = 1 cannot kill it\n"
            "example : check %d 1 %d 0 = true := by decide +kernel\n" % (W, N))


def m_neg(W):
    def m(rc, text):
        want = ['proved that the proposition', 'check %d 1 %d 0 = true' % (W, N), 'is false']
        ok = rc != 0 and all(w in text for w in want)
        other = [l for l in text.splitlines() if 'error' in l and 'decide' not in l and 'proposition' not in l]
        return ('pass' if ok and not other else 'FAIL', 'expected diagnostic %s; other errors %d' % (ok, len(other)))
    return m


def plan():
    steps = []
    # the bridge to W1A: W = 52 at the kit's own K = 97, chunk 0
    steps.append(('w52_k97_c0', decl(52, 97, N, 0), H.m_pass))
    widths = WIDTHS + ([56] if WIDTH56_SINGLE else [])
    for W in widths:
        K = K_rule(W); mid = chunks(W) // 2; last = chunks(W) - 1
        steps.append(('w%d_empty' % W, empty(), H.m_pass))
        steps.append(('w%d_neg' % W, negative(W), m_neg(W)))
        if W == 56:
            steps.append(('w56_k%d_c0' % K, decl(56, K, N, 0), H.m_pass))
            continue
        for c, label in ((0, 'c0'), (mid, 'cmid'), (last, 'clast')):
            steps.append(('w%d_k%d_%s' % (W, K, label), decl(W, K, N, c), H.m_pass))
        steps.append(('w%d_k%d_double' % (W, K), double(W, K, N, 0), H.m_pass))
    return steps


def main():
    kit = os.path.abspath(sys.argv[1]); out = os.path.abspath(sys.argv[2])
    if os.path.exists(out) and os.listdir(out):
        print('REFUSED: output folder exists and is not empty:', out); sys.exit(3)
    os.makedirs(out, exist_ok=True)
    wdir = os.path.join(kit, 'lean', 'w1b')
    if os.path.isdir(wdir):
        for f in os.listdir(wdir):
            os.remove(os.path.join(wdir, f))
        os.rmdir(wdir)
    sup = H.Supervisor(kit, out); R = sup.receipts
    R['w1b'] = {'widths': WIDTHS, 'width56_single': WIDTH56_SINGLE, 'n': N, 'K_rule': '2W+9', 'generator_sha256': H.digest(os.path.abspath(__file__)), 'files': {}}

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
    r = sup.register(H.preflight())
    if r['verdict'] != 'pass':
        stop('preflight failed')
    r, _ = H.engines_control(); sup.register(r)
    if r['verdict'] != 'pass':
        stop('engines control failed')

    os.makedirs(wdir, exist_ok=True)
    for name, src, matcher in plan():
        path = os.path.join(wdir, name + '.lean')
        open(path, 'w').write(src)
        R['w1b']['files'][name] = hashlib.sha256(src.encode()).hexdigest(); sup.save()
        r = sup.run_step(name, ['lake', 'env', 'lean', 'w1b/%s.lean' % name], os.path.join(kit, 'lean'),
                         H.CAPS['module_wall_s'], H.CAPS['module_cpu_s'], matcher)
        r['cost_miss'] = H.cost_miss(r) if r['verdict'] == 'pass' else None; sup.save()
        if r['verdict'] != 'pass':
            stop('%s: %s (%s)' % (name, r['verdict'], r['reason']))
        if r['cost_miss']:
            stop('COST-MISS at %s: wall %.1f s, peak %.2f GiB; stage ended' % (name, r['wall_s'], r['peak_rss_bytes_either'] / H.GIB), 2)
    R['complete'] = True; sup.save()
    print('DONE: all steps accepted')


if __name__ == '__main__':
    main()
