#!/usr/bin/env python3
"""W1B, revision 2: the W- and K-dependence of one chunk declaration of the kit's lane checker, measured on the M5
under the W1A supervisor (tests/probes/wolfram/w1a_harness.py revision 4: its Supervisor, guards, caps and terminal
policy), proposed in CHAT-LEDGER.md L785, frozen in L786, corrected per GPT's GC1716 (three interpretation points)
in L787. NOT an agreed job until GPT accepts this exact file; it runs nothing on import.

Usage:  python3 w1b_harness.py KIT_CLONE OUT_DIR          (OUT_DIR must not exist or must be empty)

The question. W1A measured 14.5 s per 64-chunk module at W = 52, n = 18, K = 97: about 0.23 s per chunk as a module
average with compile and import overhead inside it. W1B isolates ONE declaration `check W K n c = true` by
`decide +kernel` per file and measures how its cost moves with W at fixed K and with K at fixed W, so that the
growth of the chunk design can be read before any width past 52 is attempted. No kit module is rebuilt; nothing
enters the library; every file is untracked under the clone's lean/w1b/ and compiled with `lake env lean <file>`
exactly as the W1A controls were.

The generator (`decl`): a chunk declaration is
    import Ruliology.CellularAutomata.Rule30ZeroBoundaryLanes
    open Ruliology.CellularAutomata.Rule30ZeroBoundaryLanes
    theorem w{W}_k{K}_n{n}_c{c} : check {W} {K} {n} {c} = true := by decide +kernel
the shape of the kit's own data modules (`theorem cN : check 52 97 18 N = true := by decide +kernel`); the kit holds
no other generator. Every generated file's sha256 goes in the receipt. A matching declaration shape is adequate for
an isolated check (GC1716); no census, no width-56 certificate.

Two K families, and what each may conclude (GC1716 point 1):
  Family A, K = 97 at every width W <= 52 (JUSTIFIED): a start supported at depths <= W is a start supported at
      depths <= 52, so the kit's `q01_width_le_52` (every such start has a white depth-1 cell at an even time <= 96)
      says the check at K = 97 is true at every W <= 52. Family A isolates the W-dependence at fixed K.
  Family B, K = 2W + 9 at W < 52 (EXPERIMENTAL): the kit's `q01_width_le_52_linear` concludes t <= 2*52 + 8 for
      width <= 52 only; it does not prove t <= 2W + 8 at smaller W. K = 2W + 9 is a proposed parameter rule; a false
      check at such a K refutes that parameter choice for that width and says nothing about the checker's
      soundness; it is recorded as such, not as FAIL of the instrument, and the stage continues.
  At W = 52, K = 97, 105, 113 (all justified, since 97 already suffices and a larger K only tests more times)
      isolate the K-dependence at fixed W.
Selection: n = 18 at every width (lane word 2^18 bits, constant; chunk count 2^(W/2 - 18)); c = first, middle and
last chunk (0, 2^(W/2-19), 2^(W/2-18) - 1) at every (W, K) of family A, c = 0 in family B and in the K series, so
that c-variation is measured once per width in the justified family. Widths 40, 44, 48, 52. No width 56 in this
revision (a single declaration at 56 would need K from family A's reasoning at a width the kit does not cover, so
it is not justified; it waits for a later agreement).

Timing (GC1716 point 2): the PRIMARY measures are `time -l`'s real, user and sys seconds (reported to 0.01 s) in
the receipt (time_l_real_s, time_l_user_s, time_l_sys_s) and its peak RSS; the supervisor's wall_s includes its
polling wait of about a second and is retained separately as the operational figure only. Each measured point is
run TWICE in a row (two files with the same content, suffix _r1 and _r2) so that the noise between repeats is
visible beside the differences between points; a difference smaller than the repeat spread is not a difference.
Overhead diagnostics per width: an empty file (import and open only) and a two-declaration file (the declaration
twice); double minus single ESTIMATES the declaration's own cost and is affected by cache sharing between the two
proofs; it is a diagnostic, not an exact declaration cost. Negative per width: `check W 1 18 0 = true` must fail
with the "proved … is false" diagnostic (chunk 0 holds a lane black at depth 1 at time 0).

Order: the bridge (W = 52, K = 97, c = 0, twice; must pass; its time -l real should sit near W1A's 0.23 s module
average minus the per-file overhead), then per width ascending: empty, negative, family A (c0, cmid, clast, each
twice), family B (c0, twice, W < 52 only), double; then the K series at 52 (K = 105 and 113, c0, twice).

Predictions, written before the run (hypotheses, one sample pair per point): in family A at fixed K = 97 the per-
declaration real time changes by less than 1.5 x across 40..52 (the lane word is fixed and K is fixed, so only
the forced-level structure changes); in the K series at W = 52 the real time grows about like K^2 (105/97)^2 ~ 1.17
and (113/97)^2 ~ 1.36; family B's checks at K = 2W + 9 pass at 40, 44 and 48 (the record's own death times are far
below 2W + 8 at those widths, a hypothesis); c-variation at one (W, K) under 2 x; peak RSS per declaration near W1A's
1.1 GiB and not growing with W; the empty file under 1 s; repeat spread under 10 %. What a result may conclude
(GC1716 point 3): a family-A growth or a memory growth with W above the repeat spread is a MEASURED trend at these
points, which motivates a redesign discussion before any wider certificate; it does not by itself prove infeasibility
past 56, and one pair per point is not a growth law. A family-B failure refutes the K = 2W + 9 parameter rule at
that width only. The stage never attempts a certificate at any width.

Caps (W1A's): stage 30 min; each file 180 s wall / 150 s CPU; RSS stop 6 GiB; the cost-miss gate (60 s / 4.5 GiB)
ends the stage after the declaration that misses; one worker; no retry.

OUTCOME: filled in after the run (CHAT-LEDGER.md).
"""
import hashlib, json, os, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import w1a_harness as H

WIDTHS = [40, 44, 48, 52]
K_CONST = 97                     # family A, justified at every W <= 52 by q01_width_le_52
K_SERIES_AT_52 = [105, 113]      # the K-dependence at fixed W = 52 (justified: larger K tests more times)
N = 18


def K_experimental(W):           # family B: a proposed rule, not a theorem (GC1716)
    return 2 * W + 9


def chunks(W):
    return 2 ** (W // 2 - N)


def header():
    return "import Ruliology.CellularAutomata.Rule30ZeroBoundaryLanes\nopen Ruliology.CellularAutomata.Rule30ZeroBoundaryLanes\n"


def decl(W, K, n, c, suffix=''):
    return header() + "theorem w%d_k%d_n%d_c%d%s : check %d %d %d %d = true := by decide +kernel\n" % (W, K, n, c, suffix, W, K, n, c)


def double(W, K, n, c):
    return decl(W, K, n, c) + "theorem w%d_k%d_n%d_c%d_again : check %d %d %d %d = true := by decide +kernel\n" % (W, K, n, c, W, K, n, c)


def negative(W):
    return header() + ("-- must FAIL: chunk 0 holds a lane black at depth 1 at time 0; K = 1 cannot kill it\n"
                       "example : check %d 1 %d 0 = true := by decide +kernel\n" % (W, N))


def m_neg(W):
    def m(rc, text):
        want = ['proved that the proposition', 'check %d 1 %d 0 = true' % (W, N), 'is false']
        ok = rc != 0 and all(w in text for w in want)
        other = [l for l in text.splitlines() if 'error' in l and 'decide' not in l and 'proposition' not in l]
        return ('pass' if ok and not other else 'FAIL', 'expected diagnostic %s; other errors %d' % (ok, len(other)))
    return m


def m_family_b(W, K):
    """A false check at an experimental K refutes the parameter rule, not the instrument: recorded, not FAIL."""
    def m(rc, text):
        if rc == 0 and 'error' not in text:
            return 'pass', 'K = %d suffices at W = %d' % (K, W)
        if 'proved that the proposition' in text and 'is false' in text:
            return 'pass', 'PARAMETER-REFUTED: K = %d does not suffice at W = %d (not an instrument failure)' % (K, W)
        return 'FAIL', 'unexpected error kind (exit %d)' % rc
    return m


def plan():
    steps = []
    for r in ('_r1', '_r2'):
        steps.append(('bridge_w52_k97_c0' + r, decl(52, 97, N, 0, r), H.m_pass, 'bridge'))
    for W in WIDTHS:
        mid = chunks(W) // 2; last = chunks(W) - 1
        steps.append(('w%d_empty' % W, header(), H.m_pass, 'overhead'))
        steps.append(('w%d_neg' % W, negative(W), m_neg(W), 'negative'))
        for c, label in ((0, 'c0'), (mid, 'cmid'), (last, 'clast')):
            for r in ('_r1', '_r2'):
                steps.append(('w%d_k97_%s%s' % (W, label, r), decl(W, K_CONST, N, c, r), H.m_pass, 'familyA'))
        if W < 52:
            K = K_experimental(W)
            for r in ('_r1', '_r2'):
                steps.append(('familyB_w%d_k%d_c0%s' % (W, K, r), decl(W, K, N, 0, r), m_family_b(W, K), 'familyB'))
        steps.append(('w%d_k97_double' % W, double(W, K_CONST, N, 0), H.m_pass, 'overhead'))
    for K in K_SERIES_AT_52:
        for r in ('_r1', '_r2'):
            steps.append(('w52_k%d_c0%s' % (K, r), decl(52, K, N, 0, r), H.m_pass, 'Kseries'))
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
    R['w1b'] = {'revision': 2, 'widths': WIDTHS, 'K_const': K_CONST, 'K_series_at_52': K_SERIES_AT_52, 'K_experimental': '2W+9 (W<52)',
                'n': N, 'generator_sha256': H.digest(os.path.abspath(__file__)), 'files': {}, 'roles': {}}

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
    for name, src, matcher, role in plan():
        path = os.path.join(wdir, name + '.lean')
        open(path, 'w').write(src)
        R['w1b']['files'][name] = hashlib.sha256(src.encode()).hexdigest(); R['w1b']['roles'][name] = role; sup.save()
        r = sup.run_step(name, ['lake', 'env', 'lean', 'w1b/%s.lean' % name], os.path.join(kit, 'lean'),
                         H.CAPS['module_wall_s'], H.CAPS['module_cpu_s'], matcher)
        r['role'] = role
        r['cost_miss'] = H.cost_miss(r) if r['verdict'] == 'pass' else None; sup.save()
        if r['verdict'] != 'pass':
            stop('%s: %s (%s)' % (name, r['verdict'], r['reason']))
        if r['cost_miss']:
            stop('COST-MISS at %s: wall %.1f s, peak %.2f GiB; stage ended' % (name, r['wall_s'], r['peak_rss_bytes_either'] / H.GIB), 2)
    R['complete'] = True; sup.save()
    print('DONE: all steps accepted')


if __name__ == '__main__':
    main()
