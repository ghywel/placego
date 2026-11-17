#!/usr/bin/env python3
"""Submission generator (revision 2, GC1782: the census domain, the check scope and the kit pin stated exactly) for the death-time LOWER bounds at widths 64 to 72 (Local, 2026-10-24, L868; GPT's GC1780: "a single
bundled lower-bound submission after the authorized widths finish is worthwhile ... state only the lower bounds actually proved").

For each width W the witness is one maximizer of the GPU census (P1b/P1c, L865-L868): at 64 the CPU census's witness
0x88b46d66afc2fbd5 (lane 42,727 of chunk 10686, found by both engines), at 66..72 the maximizer with the smallest lane index.
The module proves, against the kit's own definitions (Rule30ZeroBoundarySmall: `toFun`, `prun`, `run_toFun`,
`testBit_ge_of_lt`), exactly what submission 12's `width56_lower` proved at its widths: the witness is supported at depths
<= W, its depth-1 cell is black at every even time below D and white at D. Headline per width: `widthW_lower`
(a start supported at depths <= W with no even white time below D). Nothing about maximality, the number of maximizers or
any upper bound is proved here; those are numerical results of the census, stated as such in the essay.

The witnesses are re-checked here before the text is written: the scalar engine's first even white time must equal D, and
d1_engine.validate_witness must pass. Usage: python3 d5_lower_submission.py OUT.lean   (writes the module; prints its digest)
"""
import hashlib, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import p1_lane_engine as P
import d1_engine as E

WITNESSES = [   # (W, D, start): from the census results (L865, L866, L868); re-validated below
    (64, 116, 0x88b46d66afc2fbd5),
    (66, 120, 0x1f2401d1c7d2b42ab),
    (68, 122, 0x46f44349be325d4ab),
    (70, 124, 0x3f6591177592c2aaab),
    (72, 130, 0xd464cc8c0b5f0562ab),
]


def module(wit):
    names = ', '.join('`width%d_lower`' % W for W, _, _ in wit)
    head = f"""import Rule30PrizeKit
import Ruliology.CellularAutomata.Rule30ZeroBoundarySmall

/-!
# Death-time lower bounds at widths {', '.join(str(W) for W, _, _ in wit)}: explicit witnesses from a complete GPU census

**Partial result on the kit's `Q01` (the period-2 question, Problem 1 of the Rule 30 Prize), proved against the kit's own
definitions.** Write `D(W)` for the largest, over zero-boundary starts supported at depths at most `W`, of the first even time at
which the depth-1 cell is white. The kit at the pinned commit cc1e0e0 proves `D(52) <= 96` (`Rule30ZeroBoundaryWidth52`) and has no
statement at any width above 52. This module proves the lower bounds {', '.join('`D(%d) >= %d`' % (W, D) for W, D, _ in wit)}: for each width an explicit start,
supported at depths at most `W`, is black at depth 1 at every even time below the bound and white at the bound, by the kit's
packed evaluator `prun` and its bridge `run_toFun` ({names}).

**Where the witnesses come from.** A complete numerical census on a GPU of every reconstructed start of each width that
survives the even times below `W` (every maximizer lies among them, since the values exceed `W`) found these values to be the
maxima, each witness attaining its width's census maximum. The engine is an exact lane engine in Metal; at each width a batch of
2^24 starts, a sample of further starts, every maximizer and every chunk holding one were checked against an independent CPU
evaluation of the kit's lane check. The census is numerical; this module proves only the lower bounds.

**The argument** is a kernel computation and the kit's own lemmas: `w < 2 ^ W` by `decide`; `toFun w k = false` beyond the width
by the kit's `testBit_ge_of_lt`; the packed orbit `prun w (2 s)` tested at depth 1 for every `s < D / 2` by `decide +kernel`;
`zrow (toFun w) t 1 = (prun w t).testBit 0` by the kit's `run_toFun`.

**Provenance.** The Wolfram · Collatz · Mahler record (github.com/ghywel/placego, CHAT-LEDGER.md L863 to L868, 2026-10-24).
Nothing is claimed for maximality, for the number of maximizers, or for any upper bound.
-/

set_option Elab.async false

namespace Rule30Submission

open Ruliology.CellularAutomata
open Ruliology.CellularAutomata.Rule30ZeroBoundary
open Ruliology.CellularAutomata.Rule30ZeroBoundarySmall

/-- `toFun r` is false beyond the width of `r`. -/
theorem toFun_width {{r W : Nat}} (h : r < 2 ^ W) (k : Nat) (hk : W < k) : toFun r k = false := by
  unfold toFun
  have h1 : k ≠ 0 := by omega
  simp only [h1, ite_false]
  exact testBit_ge_of_lt h (by omega)

/-- The physical depth-1 cell of the start `toFun r` at time `t` is bit `0` of the packed orbit (the kit's `run_toFun`). -/
theorem zrow_packed (r t : Nat) : zrow (toFun r) t 1 = (prun r t).testBit 0 := by
  rw [run_toFun]; rfl

theorem survives_of_black {{r D : Nat}} (hb : ∀ s, s < D / 2 → (prun r (2 * s)).testBit 0 = true) (hD : D % 2 = 0) :
    ∀ t, t < D → t % 2 = 0 → zrow (toFun r) t 1 = true := by
  intro t ht he
  rw [zrow_packed]
  obtain ⟨s, rfl⟩ : ∃ s, t = 2 * s := ⟨t / 2, by omega⟩
  exact hb s (by omega)
"""
    body = []
    for W, D, s in wit:
        body.append(f"""
/-! ## Width {W}: `D({W}) >= {D}` -/

/-- The width-{W} witness ({s.bit_length()} bits; bits are depths 1 .. {W}). -/
def w{W} : Nat := {hex(s)}

theorem w{W}_lt : w{W} < 2 ^ {W} := by decide

/-- Black at depth 1 at every even time below {D}: {D // 2} packed orbits. -/
theorem w{W}_black : ∀ s, s < {D // 2} → (prun w{W} (2 * s)).testBit 0 = true := by decide +kernel

/-- White at {D}: the physical death of `w{W}`. -/
theorem w{W}_white : (prun w{W} {D}).testBit 0 = false := by decide +kernel

theorem w{W}_survives : ∀ t, t < {D} → t % 2 = 0 → zrow (toFun w{W}) t 1 = true :=
  survives_of_black w{W}_black rfl

theorem w{W}_dies : zrow (toFun w{W}) {D} 1 = false := by
  rw [zrow_packed]; exact w{W}_white

/-- **A lower bound at width {W}:** a start supported at depths at most {W} with no even white time below {D}. -/
theorem width{W}_lower :
    ∃ x : Nat → Bool, (∀ k, {W} < k → x k = false) ∧ (∀ t, t < {D} → t % 2 = 0 → zrow x t 1 = true) :=
  ⟨toFun w{W}, toFun_width w{W}_lt, w{W}_survives⟩
""")
    return head + ''.join(body) + "\nend Rule30Submission\n"


if __name__ == '__main__':
    wit = [(W, D, s) for W, D, s in WITNESSES if D is not None and s is not None]
    for W, D, s in wit:
        assert 0 < s < (1 << W), (W, 'support')
        assert P.death(s, 4 * W) == D, (W, 'scalar death', P.death(s, 4 * W))
        ok, why = E.validate_witness(W, D, s)
        assert ok, (W, why)
    text = module(wit)
    open(sys.argv[1], 'w').write(text)
    print('widths', [W for W, _, _ in wit], 'sha256', hashlib.sha256(text.encode()).hexdigest(), 'bytes', len(text.encode()))
