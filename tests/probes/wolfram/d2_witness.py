#!/usr/bin/env python3
"""D2, revision 3: the kernel-checked LOWER bound of the death time at a width, composed with the certified upper
bound into the exactness statement D(W) = U, for GPT's design read. Revision 1 (fa934106…, the executed version) was
the single case W = 52; revision 2 is the same generator and harness parametrised over a frozen table of cases (W, U,
the witness r from D1's receipts, the upper theorem and the module that carries it), with the case chosen on the
command line; the generated Lean text for case 52 is unchanged (its hash is asserted in the tests below). NOT an
agreed job until GPT accepts this exact file and the generated texts' hashes for the case run; it runs nothing on
import; nothing is submitted.

Revision 3 repairs only the width-56 source handoff after L814: restore and hash-check W2's seventeen
generated sources and allow exactly those untracked paths. The generated Lean and every execution cap are unchanged.
A stopped run is retained; this revision requires explicit mutual acceptance before one renewed launch.

Usage:  python3 d2_witness.py W KIT_CLONE OUT_DIR       (W in the CASES table)
        python3 d2_witness.py --print W                  (print the two generated Lean files for case W and stop)
        python3 d2_witness.py --test                     (the case-52 texts' hashes equal revision 1's; exits nonzero otherwise)

If this holds, it changes the kit's death-time table from "tightness observed, not proved" to kernel-checked exact at
each width in the table (LR row). Cases:
  52: U = 96, witness 0x7dc2ff6fcc4fd (D1, L808), upper `Rule30ZeroBoundaryWidth52.q01_width_le_52` (the kit);
      DONE (L810, d2-w52-20261023-2112): death_time_52_exact kernel-checked.
  56: U = 100, witness 0x93d4b223f5b9b5 (D1 stage 1, L812; 56 bits; both physical engines: dies at 100), upper
      `Rule30ZeroBoundaryWidth56.q01_width_le_56` (W2's certificate, L794; its object is present in kit-w1a, 83,360
      bytes, sha256 6110e485…, where W2 built it; its module imports the sixteen Width56 chunk modules also built
      there). Run in kit-w1a.
  60: U = 114, witness 0xe77a4e77b8f99b5 (D1 stage 2's census, L812; 60 bits; both engines: dies at 114), upper
      `Rule30ZeroBoundaryWidth60.q01_width_le_60` WITH BOUND 114, which exists only after W5 (w5_harness.py, K = 115)
      has built it in kit-w4-a; the harness asserts the upper module's statement carries `t ≤ 114` before building
      (it reads the generated wrapper source in the clone and requires the literal). Run in kit-w4-a after W5.

The generated module for case W (`Rule30DeathTime{W}.lean`, untracked in the clone, beside the kit's sources) is
revision 1's text with W, U and r substituted: `w := r`; `w_lt : w < 2 ^ W` by decide; `w_width` beyond the width by
the kit's `testBit_ge_of_lt`; `w_black : ∀ s, s < U/2 → (prun w (2 s)).testBit 0 = true` and `w_white : (prun w U).testBit
0 = false` by `decide +kernel`; `zrow_w` by the kit's `run_toFun`; `w_survives`, `w_dies`; and
`death_time_W_exact : (∀ x of width ≤ W, ∃ t ≤ U even with zrow x t 1 = false) ∧ (∃ x of width ≤ W, ∀ t < U even,
zrow x t 1 = true) := ⟨upper, ⟨toFun w, w_width, w_survives⟩⟩`. The negative asks for black at U (`s < U/2 + 1`) and
must be rejected as false (GPT's narrow matcher of revision 1, unchanged: the whole statement bound, both rejection
forms, exactly one error diagnostic, fail closed).

Order under the W1A supervisor (unchanged caps: stage 30 min, module 180/150 s, checker 600/540 s, controls 30/30 s,
RSS stop 6 GiB; one worker; no retry): pins (commit, toolchain, the seven sources, deps built, clean tracked tree;
the upper module's object present, its sha256 recorded; for 60, the bound literal 114 in the wrapper source);
preflight; the negative; `lake build` of the module (fresh olean); the kit's Check.lean with headline
`death_time_W_exact`, claim partial. Predictions per case: negative about 2 s; module under 10 s (56: 50 orbits of at
most 98 steps; 60: 57 orbits of at most 112 steps); checker about 2 s, standard axioms, newAxioms [], replay about 15
constants. Counterfactuals as revision 1's: an elaboration error (fix changes the hash, new acceptance); the kernel
rejecting `w_black` (an instrument discrepancy: stop); a non-standard axiom (stop); for 60, the bound literal absent
(stop before building).

OUTCOME (case 52, revision 1, MEASURED, run d2-w52-20261023-2112, 8.1 s): negative rejected in the elaborator form,
module built fresh (olean 97,032 bytes, sha256 71e9738a…), Check.lean pass with standard axioms, newAxioms [], 15
constants replayed; D(52) = 96 exactly, kernel-checked (L810).
OUTCOME (case 56, revision 3, MEASURED, run d2-w56b-20261023-2145, 6.0 s, after the first attempt d2-w56-20261023-2138
stopped at the module build with "bad import" because W2's generated sources had been archived out of the clone,
L814; GPT's revision 3 pins and allows the seventeen restored sources, GC1737): pins ok with the seventeen sources
hash-equal to W2's manifest and the upper object 6110e485…; negative (s < 51) rejected in the elaborator form, one
error line; the module built fresh with no dependency rebuild (olean sha256 ac86d545…, 0.35 s user); Check.lean on
Rule30DeathTime56 with headline death_time_56_exact: pass, standard axioms, newAxioms [], 15 constants replayed.
D(56) = 100 exactly, kernel-checked (L816). Case 60: filled in after the agreed run.
"""
import hashlib, os, re, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

CASES = {
    52: {'U': 96, 'r': 0x7dc2ff6fcc4fd, 'upper_module': 'Rule30ZeroBoundaryWidth52', 'upper': 'Rule30ZeroBoundaryWidth52.q01_width_le_52'},
    56: {'U': 100, 'r': 0x93d4b223f5b9b5, 'upper_module': 'Rule30ZeroBoundaryWidth56', 'upper': 'Rule30ZeroBoundaryWidth56.q01_width_le_56'},
    60: {'U': 114, 'r': 0xe77a4e77b8f99b5, 'upper_module': 'Rule30ZeroBoundaryWidth60', 'upper': 'Rule30ZeroBoundaryWidth60.q01_width_le_60'},
}
REV1_HASHES = {'pos': 'b241924a15528afa33b8f57d23043304054244d6d56c0a142cbbd63d50f130a6', 'neg': '60eff42442e6915698ab77614180f7dd749d853006f7409fe7bf48c25fc2730d'}
LIB = 'lean/Ruliology/CellularAutomata'

# Exact retained W2 source manifest, independently read at GC1722 and GC1737.
W56_SOURCES = {
    'lean/Ruliology/CellularAutomata/Rule30Certificates/ZeroBoundaryWidth56Chunks0.lean': '14e64224e17b9ea6f3191be4c41ed9c96e6d6dfc10eb858773be2aa2dfb552f9',
    'lean/Ruliology/CellularAutomata/Rule30Certificates/ZeroBoundaryWidth56Chunks1.lean': '364532fa21eac6b4fb051a6bdc21e2af0c5baf1a847d61e8f687fa0d4a6981be',
    'lean/Ruliology/CellularAutomata/Rule30Certificates/ZeroBoundaryWidth56Chunks2.lean': '52562eb96e4bf994b5d8b77bb5598e4201017ad1e06d0762c2798526b0f9b258',
    'lean/Ruliology/CellularAutomata/Rule30Certificates/ZeroBoundaryWidth56Chunks3.lean': 'e1393cd564397c608f76dbc559e83d44a8349d138c91249025ad880931ba9fb9',
    'lean/Ruliology/CellularAutomata/Rule30Certificates/ZeroBoundaryWidth56Chunks4.lean': '4ce88b462061557d824e452d9706b925382363679562ddd154f23bb7d5270af5',
    'lean/Ruliology/CellularAutomata/Rule30Certificates/ZeroBoundaryWidth56Chunks5.lean': '8cbeba98408a0cdfe24793bd7f38a9b36d51e7c3010144837b72e5bdb8f29606',
    'lean/Ruliology/CellularAutomata/Rule30Certificates/ZeroBoundaryWidth56Chunks6.lean': 'b04f32985e2f1b36da7bf5816e3429237b9e9778937bf04fe7af74e43e8196a5',
    'lean/Ruliology/CellularAutomata/Rule30Certificates/ZeroBoundaryWidth56Chunks7.lean': '58e4aab66ccff56db926d18cf208b0e0d48e6058891684fcc76331896f89fc15',
    'lean/Ruliology/CellularAutomata/Rule30Certificates/ZeroBoundaryWidth56Chunks8.lean': '10e646cb359f0310d0ce130e45d8ab6413d5339d009268adfe81a6413486b11f',
    'lean/Ruliology/CellularAutomata/Rule30Certificates/ZeroBoundaryWidth56Chunks9.lean': '33f0ab0ff3ade67393b541f31c8fd049b233f7b15549201aa3beff644549271c',
    'lean/Ruliology/CellularAutomata/Rule30Certificates/ZeroBoundaryWidth56Chunks10.lean': '9f6371683e444d61df36e69efc9da83dc9dba3b34f69c45d3021ff7086a8a996',
    'lean/Ruliology/CellularAutomata/Rule30Certificates/ZeroBoundaryWidth56Chunks11.lean': 'f9ce0a54590e93b78142e5e216e6f0527e6ae0e18027f15562630a3c6a5f1396',
    'lean/Ruliology/CellularAutomata/Rule30Certificates/ZeroBoundaryWidth56Chunks12.lean': 'fa6c1ccc0d9d61405d1cb16cfe67d5b8ec28ed2a5436fe0c039e35f41619941f',
    'lean/Ruliology/CellularAutomata/Rule30Certificates/ZeroBoundaryWidth56Chunks13.lean': 'bbd63716d194447f6b209b00b9c33e64caa8b819c2f601db78c475de5e3fcae2',
    'lean/Ruliology/CellularAutomata/Rule30Certificates/ZeroBoundaryWidth56Chunks14.lean': '5936cb532c7352639ba3c3dc2a8577cb5a129365dd820bd366b64f4c04a06353',
    'lean/Ruliology/CellularAutomata/Rule30Certificates/ZeroBoundaryWidth56Chunks15.lean': '67a4d37ae757ecd4390b493f8260d36932345328db9f39a2bf8ae2033d5b15e1',
    'lean/Ruliology/CellularAutomata/Rule30ZeroBoundaryWidth56.lean': '90bafedde1ebd998a57da1eb186ffaa2b62dc94f0893306ee90f7d6db6587108',
}


def module(W, neg=False):
    c = CASES[W]; U, R, UPPER = c['U'], c['r'], c['upper']; MOD = 'Rule30DeathTime%d' % W
    half = U // 2 + (1 if neg else 0)
    return f"""import Ruliology.CellularAutomata.Rule30ZeroBoundarySmall
import Ruliology.CellularAutomata.{c['upper_module']}

/-! The death time at width `{W}` is exactly `{U}`: the kit's certified upper bound `{UPPER}` is attained by the
explicit start `w` (bits are depths `1 .. {W}`), whose depth-1 cell is black at every even time below `{U}` and white
at `{U}`, by the kit's packed evaluator `prun` and its bridge `run_toFun`. Generated by tests/probes/wolfram/d2_witness.py. -/

namespace Ruliology.CellularAutomata
namespace {MOD}{'Neg' if neg else ''}

open Rule30ZeroBoundary Rule30ZeroBoundarySmall

def w : Nat := {hex(R)}

theorem w_lt : w < 2 ^ {W} := by decide

theorem w_width (k : Nat) (hk : {W} < k) : toFun w k = false := by
  unfold toFun
  have h1 : k ≠ 0 := by omega
  simp only [h1, if_false]
  exact testBit_ge_of_lt w_lt (by omega)

/-- Black at depth 1 at every even time below `{U}`: {half} packed orbits, kernel-evaluated. -/
theorem w_black : ∀ s, s < {half} → (prun w (2 * s)).testBit 0 = true := by decide +kernel

theorem w_white : (prun w {U}).testBit 0 = false := by decide +kernel

theorem zrow_w (t : Nat) : zrow (toFun w) t 1 = (prun w t).testBit 0 := by
  rw [run_toFun]; rfl

theorem w_survives : ∀ t, t < {U} → t % 2 = 0 → zrow (toFun w) t 1 = true := by
  intro t ht he
  rw [zrow_w]
  obtain ⟨s, rfl⟩ : ∃ s, t = 2 * s := ⟨t / 2, by omega⟩
  exact w_black s (by omega)

theorem w_dies : zrow (toFun w) {U} 1 = false := by
  rw [zrow_w]; exact w_white

/-- **The death time at width `{W}` is exactly `{U}`.** -/
theorem death_time_{W}_exact :
    (∀ x : Nat → Bool, (∀ k, {W} < k → x k = false) → ∃ t, t ≤ {U} ∧ t % 2 = 0 ∧ zrow x t 1 = false) ∧
    (∃ x : Nat → Bool, (∀ k, {W} < k → x k = false) ∧ (∀ t, t < {U} → t % 2 = 0 → zrow x t 1 = true)) :=
  ⟨{UPPER}, ⟨toFun w, w_width, w_survives⟩⟩

end {MOD}{'Neg' if neg else ''}
end Ruliology.CellularAutomata
"""


def make_m_neg(U):
    def m_neg(rc, text):
        stmt = '∀ (s : Nat), s < %d → (prun w (2 * s)).testBit 0 = true' % (U // 2 + 1)
        flat = ' '.join(text.split())
        elab = 'proved that the proposition' in flat and stmt in flat and 'is false' in flat
        kern = '(kernel) application type mismatch' in flat and ('decide (%s) = true' % stmt) in flat
        # Accept only the intended statement's rejection, never a parser/import error or mixed-error run.
        errors = [line for line in text.splitlines() if 'error:' in line or 'error: ' in line]
        ok = rc != 0 and len(errors) == 1 and (elab or kern)
        return ('pass' if ok else 'FAIL', 'rejected-as-false' if ok else 'unexpected (exit %d)' % rc)
    return m_neg


def sha(text):
    return hashlib.sha256(text.encode()).hexdigest()


def test():
    ok = sha(module(52)) == REV1_HASHES['pos'] and sha(module(52, neg=True)) == REV1_HASHES['neg']
    print('case-52 texts equal revision 1:', ok)
    for W in CASES:
        print('case', W, 'pos', sha(module(W))[:16], 'neg', sha(module(W, neg=True))[:16])
    sys.exit(0 if ok else 1)


def main():
    if sys.argv[1:2] == ['--test']:
        test(); return
    if sys.argv[1:2] == ['--print']:
        W = int(sys.argv[2]); print(module(W)); print('---- negative ----'); print(module(W, neg=True)); return
    import w1a_harness as H, subprocess, time
    W = int(sys.argv[1]); c = CASES[W]; U = c['U']; MOD = 'Rule30DeathTime%d' % W
    kit = os.path.abspath(sys.argv[2]); out = os.path.abspath(sys.argv[3])
    if os.path.exists(out) and os.listdir(out):
        print('REFUSED: output folder exists and is not empty:', out); sys.exit(3)
    os.makedirs(out, exist_ok=True)
    pos_rel = '%s/%s.lean' % (LIB, MOD); neg_rel = 'lean/d2_controls/%sNeg.lean' % MOD
    for rel in (pos_rel, neg_rel):
        p = os.path.join(kit, rel)
        if os.path.exists(p): os.remove(p)
    d = os.path.join(kit, 'lean', 'd2_controls')
    if os.path.isdir(d) and not os.listdir(d): os.rmdir(d)
    for ext in ('.olean', '.ilean', '.trace', '.olean.hash', '.ilean.hash'):
        p = os.path.join(kit, 'lean/.lake/build/lib/lean/Ruliology/CellularAutomata/%s%s' % (MOD, ext))
        if os.path.exists(p): os.remove(p)
    sup = H.Supervisor(kit, out); R_ = sup.receipts
    pos, neg = module(W), module(W, neg=True)
    R_['d2'] = {'W': W, 'U': U, 'witness_hex': hex(c['r']), 'upper': c['upper'], 'module': MOD, 'this_sha256': H.digest(os.path.abspath(__file__)),
                'files': {pos_rel: sha(pos), neg_rel: sha(neg)}}

    def stop(msg, code=1):
        R_['stopped'] = msg; sup.save(); print('STOP:', msg); sys.exit(code)

    commit = H.checked(['git', '-C', kit, 'rev-parse', 'HEAD']).strip()
    dirty = subprocess.run(['git', '-C', kit, 'status', '--porcelain'], capture_output=True, text=True).stdout.strip()
    toolchain = open(os.path.join(kit, 'lean-toolchain')).read().strip()
    got = {f: H.digest(os.path.join(kit, f)) for f in H.PIN['sources']}
    bad = [f for f, want in H.PIN['sources'].items() if got[f] != want]
    upo = os.path.join(kit, 'lean/.lake/build/lib/lean/Ruliology/CellularAutomata/%s.olean' % c['upper_module'])
    R_['pins'] = {'commit': commit, 'tracked_tree_dirty': dirty.splitlines(), 'toolchain': toolchain, 'bad_sources': bad,
                  'deps_built': {dd: os.path.exists(os.path.join(kit, dd)) for dd in H.DEPS}, 'upper_olean': os.path.exists(upo),
                  'upper_olean_sha256': H.digest(upo) if os.path.exists(upo) else None, 'upper_olean_bytes': os.path.getsize(upo) if os.path.exists(upo) else None}
    if W == 60:
        src = os.path.join(kit, '%s/%s.lean' % (LIB, c['upper_module']))
        txt = open(src).read() if os.path.exists(src) else ''
        R_['pins']['upper_source_present'] = bool(txt); R_['pins']['upper_bound_literal_114'] = ('t ≤ 114' in txt) and ('q01_of_chunks 60 115 18' in txt)
        R_['pins']['upper_source_sha256'] = sha(txt) if txt else None
    sup.save()
    if commit != H.PIN['commit'] or toolchain != H.PIN['toolchain'] or bad or not all(R_['pins']['deps_built'].values()) or not R_['pins']['upper_olean']:
        stop('pin mismatch: commit %s toolchain %s bad %s deps %s upper %s' % (commit[:8], toolchain, bad, R_['pins']['deps_built'], R_['pins']['upper_olean']))
    allowed_dirty = set()
    if W == 56:
        source_hashes = {rel: H.digest(os.path.join(kit, rel)) if os.path.isfile(os.path.join(kit, rel)) else None
                         for rel in W56_SOURCES}
        R_['pins']['upper_source_hashes'] = source_hashes
        sup.save()
        if source_hashes != W56_SOURCES:
            stop('width-56 source handoff does not match retained W2 manifest')
        if R_['pins']['upper_olean_sha256'] != '6110e48543eaab8ab975692b2689a9a9f5e439618ca17d819350bd336b8bf1a3':
            stop('width-56 upper object does not match retained W2 object')
        allowed_dirty = {'?? ' + rel for rel in W56_SOURCES}
    if W == 60:
        if not R_['pins'].get('upper_bound_literal_114'): stop('the width-60 upper module with bound 114 is not present (W5 first)')
        allowed_dirty = {'?? %s/%s.lean' % (LIB, c['upper_module'])} | {'?? %s/Rule30Certificates/ZeroBoundaryWidth60Chunks%d.lean' % (LIB, m) for m in range(64)}
    extra = [l for l in dirty.splitlines() if l not in allowed_dirty]
    if extra: stop('tracked tree not clean: %s' % extra[:3])
    if H.pressure_bad(sup.baseline): stop('pressure at launch')
    r = sup.register(H.preflight())
    if r['verdict'] != 'pass': stop('preflight failed')
    os.makedirs(os.path.join(kit, 'lean', 'd2_controls'), exist_ok=True)
    open(os.path.join(kit, neg_rel), 'w').write(neg); open(os.path.join(kit, pos_rel), 'w').write(pos)
    sup.art_baseline = H.snapshot(kit, out)
    r = sup.run_step('neg_%d' % (U // 2 + 1), ['lake', 'env', 'lean', 'd2_controls/%sNeg.lean' % MOD], os.path.join(kit, 'lean'), H.CAPS['control_wall_s'], H.CAPS['control_cpu_s'], make_m_neg(U))
    if r['verdict'] != 'pass': stop('negative control: %s (%s) %s' % (r['verdict'], r['reason'], r.get('match_note')))
    olean = os.path.join(kit, 'lean/.lake/build/lib/lean/Ruliology/CellularAutomata/%s.olean' % MOD)
    r = sup.run_step('build_%s' % MOD, ['lake', 'build', 'Ruliology.CellularAutomata.%s' % MOD], kit, H.CAPS['module_wall_s'], H.CAPS['module_cpu_s'], H.m_pass)
    r['olean'] = {'exists_after': os.path.exists(olean), 'sha256': H.digest(olean) if os.path.exists(olean) else None}
    sup.save()
    if r['verdict'] != 'pass' or not r['olean']['exists_after']: stop('module: %s (%s)' % (r['verdict'], r['reason']))
    headline = 'Ruliology.CellularAutomata.%s.death_time_%d_exact' % (MOD, W); H.HEADLINE = headline
    r = sup.run_step('checker', ['lake', 'env', 'lean', '--run', 'Check.lean', 'Ruliology.CellularAutomata.%s' % MOD, '--claim', 'partial', '--headline', headline],
                     kit, H.CAPS['checker_wall_s'], H.CAPS['checker_cpu_s'], H.m_checker)
    if r['verdict'] != 'pass': stop('checker: %s (%s) %s' % (r['verdict'], r['reason'], r.get('match_note')))
    R_['complete'] = True; R_['finished'] = time.strftime('%Y-%m-%dT%H:%M:%S'); sup.save()
    print('DONE: death_time_%d_exact kernel-checked here (not submitted)' % W)


if __name__ == '__main__':
    main()
