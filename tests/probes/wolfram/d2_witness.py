#!/usr/bin/env python3
"""D2, revision 1: the kernel-checked LOWER bound of the death time, for GPT's design read. Generates a Lean module
that states, for an explicit witness start r of width W, that the depth-1 cell is black at every even time below U
(by the kit's packed evaluator `prun`, bridged to the physical `zrow` by `run_toFun`), white at U, and composes it
with the kit's certified upper bound into the exactness statement D(W) = U; builds it in a clean clone under the
unchanged W1A supervisor with a negative control and the kit's Check.lean. NOT an agreed job until GPT accepts this
exact file and the generated text's hash; it runs nothing on import; nothing is submitted.

Usage:  python3 d2_witness.py KIT_CLONE OUT_DIR            (W = 52, U = 96, the D1 witness; the only case in revision 1)
        python3 d2_witness.py --print                       (print the two generated Lean files and stop)

If this holds, it changes the kit's death-time table entry D(52) = 96 from "tightness observed, not proved" to a
kernel-checked exact value: the first exact entry (LR row). The witness is D1's (L808): r = 0x7dc2ff6fcc4fd (51 bits,
width <= 52), physically validated by two independent engines here (packed and list-of-bools): black at depth 1 at
every even t < 96, white at 96.

The generated module `Rule30DeathTime52.lean` (untracked in the clone, beside the kit's sources):

    import Ruliology.CellularAutomata.Rule30ZeroBoundarySmall
    import Ruliology.CellularAutomata.Rule30ZeroBoundaryWidth52
    namespace Ruliology.CellularAutomata.Rule30DeathTime52
    open Rule30ZeroBoundary Rule30ZeroBoundarySmall
    def w : Nat := 0x7dc2ff6fcc4fd
    theorem w_lt : w < 2 ^ 52 := by decide                                 -- width
    theorem w_width (k : Nat) (hk : 52 < k) : toFun w k = false            -- toFun is false beyond the width
    theorem w_black : ∀ s, s < 48 → (prun w (2 * s)).testBit 0 = true := by decide +kernel   -- the orbit, 48 even times
    theorem w_white : (prun w 96).testBit 0 = false := by decide +kernel  -- and white at 96 (the physical death)
    theorem zrow_w (t : Nat) : zrow (toFun w) t 1 = (prun w t).testBit 0  -- run_toFun, then toFun at depth 1
    theorem w_survives : ∀ t, t < 96 → t % 2 = 0 → zrow (toFun w) t 1 = true
    theorem w_dies : zrow (toFun w) 96 1 = false
    theorem death_time_52_exact :
        (∀ x : Nat → Bool, (∀ k, 52 < k → x k = false) → ∃ t, t ≤ 96 ∧ t % 2 = 0 ∧ zrow x t 1 = false) ∧
        (∃ x : Nat → Bool, (∀ k, 52 < k → x k = false) ∧ (∀ t, t < 96 → t % 2 = 0 → zrow x t 1 = true)) :=
      ⟨Rule30ZeroBoundaryWidth52.q01_width_le_52, ⟨toFun w, w_width, w_survives⟩⟩

Reading: the first conjunct is the kit's theorem unchanged (every start of width <= 52 has an even white time
<= 96); the second exhibits a start of width <= 52 with no even white time below 96. Together: the least uniform
even death bound at width 52 is exactly 96. Nothing is claimed about other widths. `decide +kernel` evaluates
`prun w (2 s)` for s < 48 (48 separate packed orbits of at most 94 steps on numbers below 2^146: trivial) through
`Nat.decidableBallLT`.

Negative control (`Rule30DeathTime52Neg.lean`, must be rejected as false): the same `w_black` with `s < 49` (which
asks for black at time 96, where the start is white). The matcher accepts only the elaborator's or the kernel's
"proved that the proposition ... is false" form bound to that statement.

Order under the W1A supervisor (caps: stage 30 min, module 180 s wall / 150 s CPU, checker 600 / 540 s, controls
30 / 30 s, RSS stop 6 GiB; one worker; no retry): pins (commit cc1e0e0, toolchain, the seven sources, deps built,
clean tracked tree; the Width52 objects present: W1A rebuilt them in this clone, byte-identical to the kit's);
preflight; the negative (lake env lean, expected rejected); `lake build Ruliology.CellularAutomata.Rule30DeathTime52`
(expected pass, fresh olean); the kit's `Check.lean` on that module with headline `death_time_52_exact`, claim
partial (expected: verdict pass, headline found, type matches, standard axioms, newAxioms [], replay ok). The
generated texts' sha256 are recorded in the receipt and must equal the hashes GPT accepts.

Predictions: the negative rejected in about 1 s; the module compiles in under 10 s (the kernel's work is 48 short
orbits plus `decide` on `w < 2^52`); the checker passes in about 2 s with 5-10 constants replayed. Counterfactuals:
the module fails to elaborate (a wrong lemma name or a `decide` instance missing: fix the text, which changes the
hash, which needs a new acceptance); the kernel rejects `w_black` (then the two Python engines and the kit's `prun`
disagree: a bug somewhere, stop); the checker reports a non-standard axiom (stop).

OUTCOME (MEASURED, run d2-w52-20261023-2112, launched 21:12:40 BST at GC1732's accepted version fa934106…, 8.1 s in all,
complete, no stop; receipt sha256 31afffa7eda672610716b1367bf0fa81e94bdca63cf91376c4e32d42c2c59634, kept on the M5; the
generated sources and the object archived in the run folder, kit-w1a clean again): pins ok (cc1e0e0, clean, the width-52
object 0bdb8beb… equal to the W1A receipt's); preflight pass; the negative (s < 49) rejected in the elaborator form,
"Tactic `decide` proved that the proposition ∀ (s : Nat), s < 49 → (prun w (2 * s)).testBit 0 = true is false", one
error line, 1.6 s; the module built fresh in 2.1 s (0.35 s user; olean 97,032 bytes, sha256 71e9738a…; one deprecation
warning on `if_false`, no error); the kit's Check.lean on Rule30DeathTime52 with headline death_time_52_exact: verdict
pass, headline found, theorem, type matches, axioms propext / Classical.choice / Quot.sound, newAxioms [], replay of 15
constants ok, 2.1 s. Peak RSS 0.4 / 0.66 / 1.37 GiB (negative, module, checker); swap growth 0; pressure 1. So
**D(52) = 96 exactly, kernel-checked**: every start of width <= 52 has an even white time at depth 1 at or before 96
(the kit's theorem), and the start 0x7dc2ff6fcc4fd of width <= 52 has none below 96. Against the predictions: negative
about 1 s (1.6); module under 10 s (2.1); checker about 2 s with 5-10 constants (2.1 s, 15 constants: the module's
own 9 declarations plus the Nat-literal and decidability helpers it uses). Not submitted.
"""
import hashlib, os, re, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

W, U, R = 52, 96, 0x7dc2ff6fcc4fd
UPPER = 'Rule30ZeroBoundaryWidth52.q01_width_le_52'
MOD = 'Rule30DeathTime52'
LIB = 'lean/Ruliology/CellularAutomata'


def module(neg=False):
    half = U // 2 + (1 if neg else 0)
    return f"""import Ruliology.CellularAutomata.Rule30ZeroBoundarySmall
import Ruliology.CellularAutomata.Rule30ZeroBoundaryWidth{W}

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


def m_neg(rc, text):
    stmt = '∀ (s : Nat), s < %d → (prun w (2 * s)).testBit 0 = true' % (U // 2 + 1)
    flat = ' '.join(text.split())
    elab = 'proved that the proposition' in flat and stmt in flat and 'is false' in flat
    kern = '(kernel) application type mismatch' in flat and ('decide (%s) = true' % stmt) in flat
    # Accept only the intended statement's rejection, never a parser/import error or mixed-error run.
    errors = [line for line in text.splitlines() if 'error:' in line or 'error: ' in line]
    ok = rc != 0 and len(errors) == 1 and (elab or kern)
    return ('pass' if ok else 'FAIL', 'rejected-as-false' if ok else 'unexpected (exit %d)' % rc)


def main():
    if sys.argv[1:] == ['--print']:
        print(module()); print('---- negative ----'); print(module(neg=True)); return
    import w1a_harness as H, subprocess, time
    kit = os.path.abspath(sys.argv[1]); out = os.path.abspath(sys.argv[2])
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
    pos, neg = module(), module(neg=True)
    R_['d2'] = {'W': W, 'U': U, 'witness_hex': hex(R), 'upper': UPPER, 'module': MOD, 'this_sha256': H.digest(os.path.abspath(__file__)),
                'files': {pos_rel: hashlib.sha256(pos.encode()).hexdigest(), neg_rel: hashlib.sha256(neg.encode()).hexdigest()}}

    def stop(msg, code=1):
        R_['stopped'] = msg; sup.save(); print('STOP:', msg); sys.exit(code)

    commit = H.checked(['git', '-C', kit, 'rev-parse', 'HEAD']).strip()
    dirty = subprocess.run(['git', '-C', kit, 'status', '--porcelain'], capture_output=True, text=True).stdout.strip()
    toolchain = open(os.path.join(kit, 'lean-toolchain')).read().strip()
    got = {f: H.digest(os.path.join(kit, f)) for f in H.PIN['sources']}
    bad = [f for f, want in H.PIN['sources'].items() if got[f] != want]
    w52 = os.path.join(kit, 'lean/.lake/build/lib/lean/Ruliology/CellularAutomata/Rule30ZeroBoundaryWidth52.olean')
    R_['pins'] = {'commit': commit, 'tracked_tree_dirty': dirty.splitlines(), 'toolchain': toolchain, 'bad_sources': bad,
                  'deps_built': {dd: os.path.exists(os.path.join(kit, dd)) for dd in H.DEPS}, 'width52_olean': os.path.exists(w52),
                  'width52_olean_sha256': H.digest(w52) if os.path.exists(w52) else None}
    sup.save()
    if commit != H.PIN['commit'] or dirty or toolchain != H.PIN['toolchain'] or bad or not all(R_['pins']['deps_built'].values()) or not R_['pins']['width52_olean']:
        stop('pin mismatch: commit %s dirty %r toolchain %s bad %s deps %s width52 %s' % (commit[:8], bool(dirty), toolchain, bad, R_['pins']['deps_built'], R_['pins']['width52_olean']))
    if H.pressure_bad(sup.baseline): stop('pressure at launch')
    r = sup.register(H.preflight())
    if r['verdict'] != 'pass': stop('preflight failed')
    os.makedirs(os.path.join(kit, 'lean', 'd2_controls'), exist_ok=True)
    open(os.path.join(kit, neg_rel), 'w').write(neg); open(os.path.join(kit, pos_rel), 'w').write(pos)
    sup.art_baseline = H.snapshot(kit, out)
    r = sup.run_step('neg_49', ['lake', 'env', 'lean', 'd2_controls/%sNeg.lean' % MOD], os.path.join(kit, 'lean'), H.CAPS['control_wall_s'], H.CAPS['control_cpu_s'], m_neg)
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
