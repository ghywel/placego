#!/usr/bin/env python3
"""gen_trap_lift.py (Local, 9 November 2026; S-16): writes the Lean module `Rule30GateTrapLift` (the gap word 3535353
never occurs after entry into the kit's gate trap, through the trap's 18-column lift; and Q01GapCore), in the kit's form
(importing Rule30GateTrapWords) and in the portal's form (carrying S-15's reviewed source verbatim, because the
portal's verifier kit predates it).

Usage: python3 gen_trap_lift.py KIT_DIR S15_PORTAL_SOURCE OUT_DIR

Data: the path sets of 3535353 in the 18-column lift from every black lift window (a window of columns 1..18 at an
odd time whose first 16 columns are a window of the kit's trap; columns 17 and 18 arbitrary), one layer per sample;
one path of the 16-column trap graph that reads 3535353 (so the 16-column trap cannot exclude it); and paths of the
18-column lift reading its two maximal proper factors 353535 and 535353 (so it is minimal for the lift).
Conventions as gen_trap_words.py: bit i of a code is column i + 1; x1, x2 are the exterior column's two values.
"""
import re
import sys
from pathlib import Path

KIT, S15, OUT = Path(sys.argv[1]), Path(sys.argv[2]), Path(sys.argv[3])
src = (KIT / 'lean/Ruliology/CellularAutomata/Rule30Certificates/GateTrap.lean').read_text()
TRAP = [int(x) for x in re.findall(r'\d+', re.search(r'def trapCodes : List Nat := \[(.*?)\]', src, re.S).group(1))]
assert len(TRAP) == 829
TS = set(TRAP)


def step(s, c, x, W):
    e = s | (x << W)
    return (((e << 1) | c) ^ (e | (e >> 1))) & ((1 << W) - 1)


def step2(s, a, b, W):
    return step(step(s, 0, a, W), 1, b, W)


def bits(gaps):
    b = [1]
    for g in gaps:
        b += [0] * (g - 1) + [1]
    return b


LIFT = sorted(t | (h << 16) for t in TRAP for h in range(4))
WORD = [3, 5, 3, 5, 3, 5, 3]
w = bits(WORD)
S = {x for x in LIFT if (x & 1) == w[0]}
layers = [S]
for y in w[1:]:
    S = {v for x in S for a in (0, 1) for b in (0, 1) for v in [step2(x, a, b, 18)] if (v & 1) == y}
    layers.append(S)
assert not layers[-1] and all(layers[:-1]) and len(layers) == len(w)
assert all((v & 0xFFFF) in TS for L in layers for v in L)


def path(start, word, W):
    parent = [{x: None for x in start if (x & 1) == word[0]}]
    for y in word[1:]:
        nxt = {}
        for x in sorted(parent[-1]):
            for a in (0, 1):
                for b in (0, 1):
                    v = step2(x, a, b, W)
                    if (v & 1) == y and v not in nxt:
                        nxt[v] = (x, a, b)
        parent.append(nxt)
    v = min(parent[-1]); xs = []
    for k in range(len(word) - 1, 0, -1):
        x, a, b = parent[k][v]; xs.append((a, b)); v = x
    return v, xs[::-1]


lb = lambda b: 'true' if b else 'false'


def wrap(prefix, items, sep=', ', width=99, indent='    '):
    lines, cur = [], prefix
    for i, it in enumerate(items):
        piece = it + (sep if i < len(items) - 1 else '')
        if len(cur) + len(piece.rstrip()) > width:
            lines.append(cur.rstrip()); cur = indent
        cur += piece
    lines.append(cur.rstrip())
    return '\n'.join(lines)


def pathdef(name, w0, xs):
    items = [f'({lb(a)}, {lb(b)})' for a, b in xs]
    return f'def {name} : Nat × List (Bool × Bool) :=\n' + wrap(f'  ({w0}, [', items) + '])'


CH = 192
data = []
chunks = {}
for k, L in enumerate(layers[:-1]):
    c = sorted(L)
    parts = [c[i:i + CH] for i in range(0, len(c), CH)]
    chunks[k] = len(parts)
    if len(parts) == 1:
        data.append(f'/-- The {len(c)} windows of the 18-column lift that can have read the first {k + 1} samples of\n'
                    f'`3535353`. -/\n' + wrap(f'def lift{k} : List Nat := [', [str(x) for x in c]) + ']')
    else:
        for i, part in enumerate(parts):
            data.append(wrap(f'def lift{k}_{i} : List Nat := [', [str(x) for x in part]) + ']')
        data.append(f'/-- The {len(c)} windows of the 18-column lift that can have read the first {k + 1} samples of\n'
                    f'`3535353`, in {len(parts)} chunks. -/\n' + wrap(f'def lift{k} : List Nat := ', [f'lift{k}_{i}' for i in range(len(parts))], sep=' ++ '))
sizes = ', '.join(str(len(L)) for L in layers)
items = sizes.split(', '); items[-1] += '); the last is empty. -/'
data.append(wrap('/-- The layers of `3535353` in the 18-column lift, one per sample (', items, indent='') + '\n' +
            wrap('def liftLayers : List (List Nat) := [', [f'lift{k}' for k in range(len(layers) - 1)] + ['[]']) + ']')
n = len(layers)
checks = ['theorem liftStart : startOK18 true lift0 = true := by decide +kernel']
for k in range(1, n):
    nxt = f'lift{k}' if k < n - 1 else '[]'
    m = chunks[k - 1]
    if m == 1:
        checks.append(f'theorem liftStep{k} : stepOK18 lift{k - 1} {lb(w[k])} {nxt} = true := by\n  decide +kernel')
    else:
        for i in range(m):
            checks.append(f'theorem liftStep{k}_{i} : stepOK18 lift{k - 1}_{i} {lb(w[k])} {nxt} = true := by\n  decide +kernel')
        checks.append(f'theorem liftStep{k} : stepOK18 lift{k - 1} {lb(w[k])} {nxt} = true := by\n'
                      + wrap(f'  simp only [lift{k - 1}, stepOK18_append, ', [f'liftStep{k}_{i}' for i in range(m)] + ['Bool.and_self']) + ']')
simps = ['liftLayers', 'wordCheck18', 'readCheck18', 'liftStart'] + [f'liftStep{k}' for k in range(1, n)] + \
    ['List.isEmpty_nil', 'Bool.and_self']
checks.append('theorem check3535353 : wordCheck18 (gapWord [3, 5, 3, 5, 3, 5, 3]) liftLayers = true := by\n'
              + wrap('  rw [show gapWord [3, 5, 3, 5, 3, 5, 3] =\n    [', [lb(b) for b in w], indent='    ')
              + '] from rfl]\n' + wrap('  simp only [', simps) + ']')
p16 = path([x for x in TRAP], w, 16)
p18a = path(LIFT, bits([3, 5, 3, 5, 3, 5]), 18)
p18b = path(LIFT, bits([5, 3, 5, 3, 5, 3]), 18)
for (w0, xs), word, W, st in ((p16, w, 16, TRAP), (p18a, bits([3, 5, 3, 5, 3, 5]), 18, LIFT), (p18b, bits([5, 3, 5, 3, 5, 3]), 18, LIFT)):
    x = w0; rd = [x & 1]
    for a, b in xs:
        x = step2(x, a, b, W); rd.append(x & 1)
        assert (x & 0xFFFF) in TS
    assert rd == word
paths = '\n'.join([pathdef('path16_3535353', *p16), pathdef('path18_353535', *p18a), pathdef('path18_535353', *p18b)])

BODY = r'''
/-! ## Windows of eighteen columns -/

section Driven18
variable (R : Nat → Bool)

/-- The window of `R` of the columns `1..18` at time `t`. Its first sixteen cells are `win R t`. -/
def win18 (t : Nat) : List Bool := rowOf (drv altCol R) t 0 18

theorem win18_length (t : Nat) : (win18 R t).length = 18 := length_seg _ _

theorem win18_head (t : Nat) : (win18 R t).headD false = drv altCol R t 1 := rowOf_head _ t 0 17

theorem win18_eq (t : Nat) :
    win18 R t = win R t ++ [drv altCol R t 17, drv altCol R t 18] := by
  unfold win18 win rowOf
  rw [show (18 : Nat) = 16 + 1 + 1 from rfl, seg_succ, seg_succ]
  simp [List.append_assoc]

/-- From an odd time, the 18-column window two steps later is a double step of the window, with the
two values of column `19` as the exterior inputs. -/
theorem win18_step2 (t : Nat) (ht : t % 2 = 1) :
    ∃ x1 x2, win18 R (t + 2) = step2 (win18 R t) x1 x2 := by
  have h1 := rowOf_succ (drv_isR30 altCol R) t 0 18
  have h2 := rowOf_succ (drv_isR30 altCol R) (t + 1) 0 18
  rw [drv_col0] at h1 h2
  have a1 : altCol t = false := by unfold altCol; simp [ht]
  have a2 : altCol (t + 1) = true := by unfold altCol; simp; omega
  rw [a1] at h1
  rw [a2] at h2
  refine ⟨drv altCol R t 19, drv altCol R (t + 1) 19, ?_⟩
  unfold win18 step2
  rw [show t + 2 = t + 1 + 1 by omega, h2, h1]

theorem win18_next {L : List (List Bool)} {P : List Bool → Bool} (hc : L.all (allSucc P) = true)
    {t : Nat} (ht : t % 2 = 1) (hw : win18 R t ∈ L) : P (win18 R (t + 2)) = true := by
  obtain ⟨x1, x2, e⟩ := win18_step2 R t ht
  rw [e]
  exact allSucc_spec (List.all_eq_true.1 hc _ hw) x1 x2

end Driven18

/-- The 18-column window coded by `n`: bit `i` of `n` is column `i + 1`. -/
def decode18 (n : Nat) : List Bool := seg (fun i => n.testBit i) 18

theorem decode18_encList {w : List Bool} (hw : w.length = 18) : decode18 (encList w) = w := by
  have := seg_testBit_encList w
  rw [hw] at this
  exact this

theorem mem18_of_maskN {LN : List Nat} {w : List Bool} (hw : w.length = 18)
    (h : inM (maskN LN) w = true) : w ∈ LN.map decode18 :=
  List.mem_map.2 ⟨encList w, maskN_spec LN _ h, decode18_encList hw⟩

/-! ## The check in the 18-column lift -/

/-- Every 18-column window whose first sixteen cells are a window of `trap` (for all four values of
the columns `17` and `18`) and which reads `b` in column `1` is in the layer `L`. -/
def startOK18 (b : Bool) (L : List Nat) : Bool :=
  trap.all (fun w => [[false, false], [false, true], [true, false], [true, true]].all
    (fun e => (w ++ e).headD false != b || inM (maskN L) (w ++ e)))

/-- One layer of the lift: every double step from a window of `S`, for all four values of column
`19`, either does not read `b` in column `1` or lands in `L`. -/
def stepOK18 (S : List Nat) (b : Bool) (L : List Nat) : Bool :=
  (S.map decode18).all (allSucc (fun w => w.headD false != b || inM (maskN L) w))

theorem stepOK18_append (S1 S2 : List Nat) (b : Bool) (L : List Nat) :
    stepOK18 (S1 ++ S2) b L = (stepOK18 S1 b L && stepOK18 S2 b L) := by
  simp [stepOK18, List.map_append, List.all_append]

def readCheck18 : List Nat → List Bool → List (List Nat) → Bool
  | S, [], _ => S.isEmpty
  | S, b :: rest, L :: Ls => stepOK18 S b L && readCheck18 L rest Ls
  | _, _ :: _, [] => false

/-- **The word check in the lift.** -/
def wordCheck18 : List Bool → List (List Nat) → Bool
  | b :: rest, L :: Ls => startOK18 b L && readCheck18 L rest Ls
  | _, _ => false

section Driven18b
variable (R : Nat → Bool)

theorem readCheck18_spec : ∀ (word : List Bool) (S : List Nat) (Ls : List (List Nat)),
    readCheck18 S word Ls = true → ∀ t, t % 2 = 1 → win18 R t ∈ S.map decode18 →
      ¬ ∀ i, i < word.length → (win18 R (t + 2 * (i + 1))).headD false = word.getD i false
  | [], S, Ls, h, t, _, hw, _ => by
    simp only [readCheck18, List.isEmpty_iff] at h
    subst h
    simp at hw
  | b :: rest, S, L :: Ls, h, t, ht, hw, hr => by
    simp only [readCheck18, stepOK18, Bool.and_eq_true] at h
    have hP := win18_next R h.1 ht hw
    have hb : (win18 R (t + 2)).headD false = b := by simpa using hr 0 (by simp)
    rw [hb] at hP
    simp only [bne_self_eq_false, Bool.false_or] at hP
    refine readCheck18_spec rest _ Ls h.2 (t + 2) (by omega)
      (mem18_of_maskN (win18_length R _) hP) ?_
    intro i hi
    have := hr (i + 1) (by simp; omega)
    rw [show t + 2 + 2 * (i + 1) = t + 2 * (i + 1 + 1) by omega]
    simpa using this
  | _ :: _, _, [], h, _, _, _, _ => by simp [readCheck18] at h

/-- **A lift check excludes its word after entry.** If `wordCheck18 word layers` holds and the
window of `R` is in `trap` at an odd time `t0`, then `u R` does not read `word` from any step `s`
with `t0 ≤ 2 s + 1`. -/
theorem not_reads18_of_check {word : List Bool} {layers : List (List Nat)}
    (hc : wordCheck18 word layers = true) {t0 : Nat} (h0 : t0 % 2 = 1) (hw : win R t0 ∈ trap)
    (s : Nat) (hs : t0 ≤ 2 * s + 1) : ¬ Reads (Rule30PeriodTwoSideways.u R) s word := by
  intro hr
  have hw0 : win R (2 * s + 1) ∈ trap := by
    have := win_mem_trap R h0 hw ((2 * s + 1 - t0) / 2)
    rwa [show t0 + 2 * ((2 * s + 1 - t0) / 2) = 2 * s + 1 by omega] at this
  have hu : ∀ k, Rule30PeriodTwoSideways.u R k = (win18 R (2 * k + 1)).headD false := by
    intro k; rw [win18_head]; rfl
  cases word with
  | nil => simp [wordCheck18] at hc
  | cons b rest =>
    cases layers with
    | nil => simp [wordCheck18] at hc
    | cons L Ls =>
      simp only [wordCheck18, startOK18, Bool.and_eq_true] at hc
      have hb : (win18 R (2 * s + 1)).headD false = b := by
        have := hr 0 (by simp)
        rw [hu] at this
        simpa using this
      have he : [drv altCol R (2 * s + 1) 17, drv altCol R (2 * s + 1) 18] ∈
          [[false, false], [false, true], [true, false], [true, true]] := by
        cases drv altCol R (2 * s + 1) 17 <;> cases drv altCol R (2 * s + 1) 18 <;> simp
      have hP := List.all_eq_true.1 (List.all_eq_true.1 hc.1 _ hw0) _ he
      rw [← win18_eq, hb] at hP
      simp only [bne_self_eq_false, Bool.false_or] at hP
      refine readCheck18_spec R rest _ Ls hc.2 (2 * s + 1) (by omega)
        (mem18_of_maskN (win18_length R _) hP) ?_
      intro i hi
      have := hr (i + 1) (by simp; omega)
      rw [hu] at this
      rw [show 2 * s + 1 + 2 * (i + 1) = 2 * (s + (i + 1)) + 1 by omega]
      simpa using this

end Driven18b

/-! ## The layers of `3535353` -/

@DATA@

@CHECKS@

/-! ## `3535353` after entry -/

/-- **The trap never shows `3535353`.** If the window of `R` is in `trap` at an odd time `t0`, then
`u R` never reads the gap word `3, 5, 3, 5, 3, 5, 3` from a step `s` with `t0 ≤ 2 s + 1`. -/
theorem no_3535353_of_entry (R : Nat → Bool) {t0 : Nat} (h0 : t0 % 2 = 1) (hw : win R t0 ∈ trap)
    (s : Nat) (hs : t0 ≤ 2 * s + 1) :
    ¬ Reads (Rule30PeriodTwoSideways.u R) s (gapWord [3, 5, 3, 5, 3, 5, 3]) :=
  not_reads18_of_check R check3535353 h0 hw s hs

/-! ## Why the lift is needed, and minimality -/

@PATHS@

/-- **The sixteen columns of the trap cannot see it.** A path of the 16-column trap graph reads
`3535353`, so no check on the trap's own windows can exclude it. -/
theorem trap_reads_3535353 :
    trapPath path16_3535353.1 path16_3535353.2 (gapWord [3, 5, 3, 5, 3, 5, 3]) = true := by
  decide +kernel

/-- A path of the 18-column lift that reads `word`: an 18-column window whose first sixteen cells
are a window of `trap`, coded by `c`, and values of column `19`. -/
def liftPath (c : Nat) (xs : List (Bool × Bool)) (word : List Bool) : Bool :=
  trapCodes.contains (c % 65536) && pathReads (decode18 c) xs word

/-- **`3535353` is minimal for the lift.** Removing its first or its last gap gives `535353` or
`353535`, and a path of the 18-column lift reads each. -/
theorem lift_minimal_paths :
    liftPath path18_353535.1 path18_353535.2 (gapWord [3, 5, 3, 5, 3, 5]) = true ∧
      liftPath path18_535353.1 path18_535353.2 (gapWord [5, 3, 5, 3, 5, 3]) = true := by
  decide +kernel

/-! ## A weaker form of `Q01GapWords` -/

/-- At `s`, `g` satisfies `WordsOK` and does not read `3535353`. -/
def CoreOK (g : Nat → Bool) (s : Nat) : Prop :=
  WordsOK g s ∧ ¬ Reads g s (gapWord [3, 5, 3, 5, 3, 5, 3])

/-- **`Q01GapCore`** (**open**): `Q01GapWords` with `3535353` excluded as well. No finitely
supported constrained start of the zero-boundary left half has free bits whose complement, from some
step on, satisfies `CoreOK` at every step. -/
def Q01GapCore : Prop := ∀ L : Nat → Bool, FinSupp L → InX L →
  ¬ ∃ s0, ∀ s, s0 ≤ s → CoreOK (fun s => !zrow L (2 * s + 1) 1) s

/-- **`Q01GapWords` implies `Q01GapCore`**, which has fewer free bits to exclude. -/
theorem Q01GapCore_of_Q01GapWords (h : Q01GapWords) : Q01GapCore := fun L hf hX ⟨s0, hs⟩ =>
  h L hf hX ⟨s0, fun s hs' => (hs s hs').1⟩

/-- **`Q01GapCore` gives `CQ01` for every right half whose window enters the trap.** -/
theorem not_finSupp_Psi_of_Q01GapCore (hQ : Q01GapCore) (R : Nat → Bool) {t0 : Nat}
    (h0 : t0 % 2 = 1) (hw : win R t0 ∈ trap) :
    ¬ FinSupp (Rule30PeriodTwoSideways.Psi R) := by
  intro hfin
  refine hQ _ hfin (Rule30PeriodTwoSideways.Psi_inX R) ⟨t0, fun s hs => ?_⟩
  have e : (fun s => !zrow (Rule30PeriodTwoSideways.Psi R) (2 * s + 1) 1) =
      Rule30PeriodTwoSideways.u R := by
    funext s; rw [Rule30PeriodTwoSideways.Psi_free]; simp; rfl
  rw [e]
  exact ⟨⟨gaps_of_entry R h0 hw s (by omega), gap_words_of_entry R h0 hw s (by omega)⟩,
    no_3535353_of_entry R h0 hw s (by omega)⟩

/-- **`CQ01Empty` follows from `Q01GapCore`.** -/
theorem CQ01Empty_of_Q01GapCore (hQ : Q01GapCore) : Rule30PeriodTwoSideways.CQ01Empty :=
  not_finSupp_Psi_of_Q01GapCore hQ _ (t0 := 293) (by decide) entry_empty
'''

COMMON = r'''These are all that the trap's own graph of sixteen-column windows forbids, and
that graph does read `3535353` (`trap_reads_3535353`). This module looks two columns further: an
18-column window whose first sixteen cells are a window of `trap` stays such a window under the
double step, with column `19` free (`win18_step2`), and in that lift no path reads `3535353`.

* `no_3535353_of_entry`: if the window of `R` is in `trap` at an odd time `t0`, then from every step
  `s` with `t0 ≤ 2 s + 1`, `u R` never reads `3, 5, 3, 5, 3, 5, 3`.
* `lift_minimal_paths`: it is minimal for the lift: `353535` and `535353` are read along explicit
  paths of the lift.
* `Q01GapCore` (**open**) is `Q01GapWords` with `3535353` excluded as well: it follows from
  `Q01GapWords` (`Q01GapCore_of_Q01GapWords`), and it still gives `¬ FinSupp (Psi R)` for every
  right half whose window enters the trap (`not_finSupp_Psi_of_Q01GapCore`), hence `CQ01Empty`
  (`CQ01Empty_of_Q01GapCore`).

The method is that of `Rule30GateTrapWords` (`wordCheck18`, `not_reads18_of_check`): the path sets
of the word in the lift, starting from every black lift window, are given as data, with one kernel
check per sample and per chunk of at most 192 windows. Nothing here decides `CQ01`, `Q01Gap`,
`Q01GapWords`, `Q01GapCore` or Problem 1.'''

HEAD_KIT = r'''/-!
# The gate trap at eighteen columns: `3535353` never occurs after entry

`Rule30GateTrapWords` shows that after the window of a right half `R` enters the gate trap of
`Rule30GateTrap`, `u R` never reads the gap words `333`, `3353`, `3533`, `3553` and `5533`.
''' + COMMON + '\n-/'

HEAD_PORTAL = r'''/-!
# The gate trap at eighteen columns: `3535353` never occurs after entry

The kit module `Rule30GateTrapWords` (Rule 30 Prize submission R30-20261109-897fd1) shows that
after the window of a right half `R` enters the gate trap of `Rule30GateTrap`, `u R` never reads
the gap words `333`, `3353`, `3533`, `3553` and `5533`.
''' + COMMON + r'''

The portal's verifier kit predates `Rule30GateTrapWords`, so this module first repeats that
module's reviewed source verbatim, and then adds the eighteen-column part.
-/'''

body = BODY.replace('@DATA@', '\n\n'.join(data)).replace('@CHECKS@', '\n'.join(checks)).replace('@PATHS@', paths)
kit = ('module\n\npublic import Ruliology.CellularAutomata.Rule30GateTrapWords\n\n' + HEAD_KIT + '\n\n@[expose] public section\n\n'
       '-- Sequential elaboration: the kernel checks would otherwise run in parallel and stack their memory.\n'
       'set_option Elab.async false\n\n'
       'namespace Ruliology.CellularAutomata.Rule30GateTrapLift\n\n'
       'open Rule30StripCertificates Rule30Ether Rule30PeriodTwoCoupled Rule30GateTrap Rule30GateTrapWords\n  Rule30ZeroBoundary\n'
       + body + '\nend Ruliology.CellularAutomata.Rule30GateTrapLift\n')
s15 = S15.read_text()
i = s15.index('-- Sequential elaboration')
j = s15.rindex('end Rule30Submission')

portal = ('import Ruliology.CellularAutomata.Rule30Prize\nimport Ruliology.CellularAutomata.Rule30GateTrap\n\n' + HEAD_PORTAL + '\n\n'
          + s15[i:j].rstrip('\n') + '\n\n/-! # The eighteen-column lift -/\n\nopen Rule30Ether Rule30PeriodTwoCoupled\n' + body + '\nend Rule30Submission\n')
for text in (kit, portal):
    assert '"' not in text and '\\' not in text
OUT.mkdir(parents=True, exist_ok=True)
(OUT / 'Rule30GateTrapLift.lean').write_text(kit)
(OUT / 'Rule30Submission.lean').write_text(portal)
print('layers', [len(L) for L in layers], 'total', sum(len(L) for L in layers), '; kit form', len(kit), 'chars; portal form', len(portal), 'chars')
for name, text in (('kit', kit), ('portal', portal)):
    print(name, 'lines over 100 chars:', [(k + 1, len(l)) for k, l in enumerate(text.split('\n')) if len(l) > 100][:5])
