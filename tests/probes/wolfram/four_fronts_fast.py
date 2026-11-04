#!/usr/bin/env python3
"""four_fronts_fast.py (Local, L1524): the kit form of Cloud's four-strip forced front (CL734) with no data modules. The recursion F on a strip is a walk:
from wheel j at tick t, go to wheel j + 1 if the strip's cell (j, t) is black, and stay if it is white, and the tick moves on either way. That is one
add, one shift and one mask per tick, so the kernel checks all four strips in seconds where the four data modules took minutes. This script reads Cloud's
final module and the walk theory, computes each segment's numbers in Python, and writes the new final module; the kernel confirms the numbers.
Usage (from the repository root): python3 four_fronts_fast.py WALKCORE OUT. Prints the segments."""
import re, sys
K = 87867; MASK = (1 << K) - 1; P = 16
SRC = 'reports/wolfram-agents/submissions/four-left-sides/Rule30FourLeftSides.lean'
FINAL = 'reports/wolfram-agents/submissions/four-fronts/cloud-Rule30FourFronts.lean'
src = open(SRC).read()
def step(v): return ((v << 2) ^ ((v << 1) | v)) & MASK
def literal(name):
    m = re.search(r'^def %s : Nat := (.*?)$' % name, src, re.M); body = m.group(1)
    h = int(re.findall(r'0x[0-9a-fA-F]+', body)[0], 16); sh = re.search(r'<<<\s*(\d+)', body)
    return h << int(sh.group(1)) if sh else h
A0 = literal('A0'); A1 = A0 ^ literal('A1'); B0 = A0 ^ literal('B0'); B1 = B0 ^ literal('B1')
V = {'A0': A0, 'A1': A1, 'B0': B0, 'B1': B1}
def rows_of(v):
    rows = [v]
    for _ in range(P): rows.append(step(rows[-1]))
    assert rows[P] == v
    return rows[:P]
R = {k: rows_of(v) for k, v in V.items()}
def word(s, j): return sum(((R[s][r] >> j) & 1) << r for r in range(P))
def srch(w, m):
    for r in range(P):
        if (w >> ((m + r) % P)) & 1: return r
    return P
def states(s):
    """st[j] = (F j, F (j + 1)) for j = 0 .. 87866"""
    st = [(0, 1)]
    for j in range(0, 87866):
        a, b = st[-1]; w = word(s, j + 1); M = max(a, b)
        st.append((b, M if w == 0 else M + srch(w, M) + 1))
    return st
ST = {s: states(s) for s in V}
white = {s: [j for j in range(1, 87867) if word(s, j) == 0] for s in V}
def walk(s, n, t, j):
    for _ in range(n):
        j += (R[s][t % P] >> j) & 1; t += 1
    return j
out = []
def pair(p): return '(%d, %d)' % p
def seg(name, s, j0, n):
    """a black run: wheels j0 + 1 .. j0 + n"""
    a, b = ST[s][j0]; A, B = ST[s][j0 + n]
    assert all(word(s, j0 + 1 + i) != 0 for i in range(n)) and n >= 2 and a <= b < A < B
    T = A - 1 - b; h = (-b) % P; g = (T - h) // P; d = (T - h) % P
    assert h + 16 * g + d == T and (b + h) % P == 0
    assert walk(s, T, b, j0 + 1) == j0 + n - 1 and (R[s][(A - 1) % P] >> (j0 + n - 1)) & 1 == 1
    assert walk(s, B - 1 - A, A, j0 + n) == j0 + n and (R[s][(B - 1) % P] >> (j0 + n)) & 1 == 1
    out.append(f'theorem {name} : frun wd{s} {j0} {n} {pair((a, b))} = {pair((A, B))} :=\n'
               f'  seg_black (v := {s}) (h := {h}) (g := {g}) (d := {d}) (by decide) (by decide) (by decide) (by decide) (by decide) (by decide)\n'
               f'    (by decide +kernel) (by decide +kernel) (by decide +kernel) (by decide +kernel)')
    print(f'{s} black j0={j0} n={n} {pair((a,b))} -> {pair((A,B))} ticks {T}')
def wht(name, s, j, proof):
    a, b = ST[s][j]; assert word(s, j + 1) == 0 and a <= b
    A, B = ST[s][j + 1]; assert (A, B) == (b, b)
    out.append(f'theorem {name} : frun wd{s} {j} 1 {pair((a, b))} = {pair((A, B))} := frun_white (by decide) {proof}')
    print(f'{s} white wheel {j+1}: {pair((a,b))} -> {pair((A,B))}')
def low(name, s, n):
    out.append(f'theorem {name} : frun wd{s} 0 {n} (0, 1) = {pair(ST[s][n])} := by decide +kernel')
def chain(name, s, parts, n0=0, target=None):
    """parts: list of (j, n, theorem); nested frun_chain"""
    tot = sum(p[1] for p in parts); target = ST[s][tot] if target is None else target
    def nest(i):
        j, n, th = parts[i]
        if i == len(parts) - 1: return th
        rest = sum(p[1] for p in parts[i + 1:])
        return f'(frun_chain _ {j} {n} {rest} _ _ _ {th}\n    {nest(i + 1)})'
    out.append(f'theorem {name} : frun wd{s} 0 {tot} (0, 1) = {pair(target)} :=\n  {nest(0)}')
# A0: wheels 1..400 by the kernel on the words; then the walk
low('a_low', 'A0', 400)
seg('a_1', 'A0', 400, 53206 - 400)
wht('a_2', 'A0', 53206, 'wdA0_53207')
chain('a_53207', 'A0', [(0, 400, 'a_low'), (400, 53206 - 400, 'a_1'), (53206, 1, 'a_2')])
seg('a_3', 'A0', 53207, 58285 - 53207)
wht('a_4', 'A0', 58285, 'wdA0_58286')
chain('a_58286', 'A0', [(0, 53207, 'a_53207'), (53207, 58285 - 53207, 'a_3'), (58285, 1, 'a_4')])
seg('a_5', 'A0', 58286, 87865 - 58286)
wht('a_6', 'A0', 87865, '(by decide +kernel)')
out.append(f'theorem SA0 : S wdA0 87866 = {pair(ST["A0"][87866])} :=\n  frun_chain _ 0 58286 29580 _ _ _ a_58286 (frun_chain _ 58286 {87865 - 58286} 1 _ _ _ a_5 a_6)')
# B0: as A0 below the first fork
out.append(f'theorem b_53207 : frun wdB0 0 53207 (0, 1) = {pair(ST["B0"][53207])} :=\n  (low_congr (fun i hi => (wB0_eq_A0 i (by omega)).symm)).trans a_53207')
seg('b_1', 'B0', 53207, 72574 - 53207)
wht('b_2', 'B0', 72574, 'wdB0_72575')
chain('b_72575', 'B0', [(0, 53207, 'b_53207'), (53207, 72574 - 53207, 'b_1'), (72574, 1, 'b_2')])
seg('b_3', 'B0', 72575, 87866 - 72575)
out.append(f'theorem SB0 : S wdB0 87866 = {pair(ST["B0"][87866])} := frun_chain _ 0 72575 {87866 - 72575} _ _ _ b_72575 b_3')
# A1: as A0 below the second fork
out.append(f'theorem a1_58286 : frun wdA1 0 58286 (0, 1) = {pair(ST["A1"][58286])} :=\n  (low_congr (fun i hi => (wA1_eq_A0 i (by omega)).symm)).trans a_58286')
seg('a1_1', 'A1', 58286, 87866 - 58286)
out.append(f'theorem SA1 : S wdA1 87866 = {pair(ST["A1"][87866])} := frun_chain _ 0 58286 {87866 - 58286} _ _ _ a1_58286 a1_1')
# B1: as B0 below the third fork
out.append(f'theorem b1_72575 : frun wdB1 0 72575 (0, 1) = {pair(ST["B1"][72575])} :=\n  (low_congr (fun i hi => (wB1_eq_B0 i (by omega)).symm)).trans b_72575')
seg('b1_1', 'B1', 72575, 87866 - 72575)
out.append(f'theorem SB1 : S wdB1 87866 = {pair(ST["B1"][87866])} := frun_chain _ 0 72575 {87866 - 72575} _ _ _ b1_72575 b1_1')
numbers = '\n\n'.join(out)
# assemble
core = open(sys.argv[1]).read()
a = core.index('/-! ### The walk: the recursion as one arithmetic step per tick -/')
b = core.index('end WalkTest')
walk_src = core[a:b].rstrip() + '\n'
walk_src = re.sub(r'\bfast\b', 'fastWalk', walk_src).replace('fast_eq', 'fastWalk_eq')
fin = open(FINAL).read()
fin = fin.replace('''public import Ruliology.CellularAutomata.Rule30FourFrontsA0
public import Ruliology.CellularAutomata.Rule30FourFrontsA1
public import Ruliology.CellularAutomata.Rule30FourFrontsB0
public import Ruliology.CellularAutomata.Rule30FourFrontsB1
''', 'public import Ruliology.CellularAutomata.Rule30FourFrontsBase\n')
old_doc = '''(`forced_front_four`). The recursion's values are kernel facts in `Rule30FourFrontsA0` … `Rule30FourFrontsB1`, in blocks of
five thousand wheels: at wheel 87,866 the fronts are 176,968 (A0), 177,229 (A1), 177,170 (B0) and 177,560 (B1). Since the
fronts are monotone,'''
new_doc = '''(`forced_front_four`). The recursion's values come from the walk below: from wheel `j` at tick `t`, move to wheel `j + 1` if the
strip's cell is black and stay if it is white, the tick moving on either way (`walk`, `frun_of_walk`). That is one addition, one
shift and one mask per tick, so the kernel runs all four strips in seconds. At wheel 87,866 the fronts are 176,968 (A0), 177,229
(A1), 177,170 (B0) and 177,560 (B1). Since the fronts are monotone,'''
assert old_doc in fin; fin = fin.replace(old_doc, new_doc)
old_cred = '''Cloud (CL734), after
`Rule30FourLeftSides` (L1513), `Rule30ForcedFront` (CL733) and the kit's `Rule30FrontLaw`.'''
new_cred = '''Cloud (CL734), the walk Local (L1524),
after `Rule30FourLeftSides` (L1513), `Rule30ForcedFront` (CL733) and the kit's `Rule30FrontLaw`.'''
assert old_cred in fin; fin = fin.replace(old_cred, new_cred)
a = fin.index('/-! ### The words of the four strips -/')
b = fin.index('/-! ### White wheels, black windows and the agreement below the forks -/')
words = '''/-! ### The words of the four strips -/

/-- The sixteen-bit word of wheel `j` of the strip of `v`: bit `r` is the wheel at phase `r`. -/
def wd (v j : Nat) : Nat := word16 (fun r => (rowAt 87867 v r).testBit j)

abbrev wdA0 : Nat → Nat := wd A0
abbrev wdA1 : Nat → Nat := wd A1
abbrev wdB0 : Nat → Nat := wd B0
abbrev wdB1 : Nat → Nat := wd B1

theorem wd_row (v : Nat) : ∀ j r, r < 16 → (wd v j).testBit r = (rowAt 87867 v r).testBit j := fun _ r hr =>
  word16_bit _ r hr

theorem wd_lt (v j : Nat) : wd v j < 2 ^ 16 := word16_lt _

theorem words (v : Nat) : Words v (wd v) := ⟨wd_lt v, fun j r hr => wd_row v j r hr⟩

theorem wordsA0 : Words A0 wdA0 := words A0
theorem wordsA1 : Words A1 wdA1 := words A1
theorem wordsB0 : Words B0 wdB0 := words B0
theorem wordsB1 : Words B1 wdB1 := words B1

'''
fin = fin[:a] + walk_src + '\n' + words + fin[b:]
a = fin.index('/-! ### The numbers, from the kernel -/')
b = fin.index('/-- Every front through wheel 87,866 is at most 177,560, the B1 front there. -/')
helpers = '''/-! ### The numbers, by the walk -/

/-- A black run of a strip by the walk, with the long stretch sixteen ticks at a time. -/
theorem seg_black {v j0 n a b A B h g d : Nat} (hab : a ≤ b) (hn : 2 ≤ n) (hA : b < A) (hB : A < B)
    (e : A - 1 - b = h + (16 * g + d)) (ht : (b + h) % 16 = 0)
    (k1 : fastWalk (rowAt 87867 v) h g d b (j0 + 1) = j0 + n - 1)
    (f2 : tb (rowAt 87867 v) (A - 1) (j0 + n - 1) = 1)
    (f3 : walk (rowAt 87867 v) (B - 1 - A) A (j0 + n) = j0 + n)
    (f4 : tb (rowAt 87867 v) (B - 1) (j0 + n) = 1) : frun (wd v) j0 n (a, b) = (A, B) :=
  frun_of_walk (wd_row v) (wd_lt v) hab hn hA hB
    (by rw [e, ← fastWalk_eq _ ht (by omega)]; exact k1) f2 f3 f4

theorem low_congr {w w' : Nat → Nat} {n : Nat} {st : Nat × Nat} (h : ∀ i, i < n → w (i + 1) = w' (i + 1)) :
    frun w 0 n st = frun w' 0 n st :=
  frun_congr n 0 st (fun i hi => by rw [Nat.zero_add]; exact h i hi)

'''
fas = '\n\n'.join(f'theorem F{s}_87866 : F wd{s} 87866 = {ST[s][87866][0]} := F_of_S S{s}' for s in ('A0', 'A1', 'B0', 'B1'))
fin = fin[:a] + helpers + numbers + '\n\n' + fas + '\n\n' + fin[b:]
low_thms = '''/-- Below the first fork the four strips are one, so the front there comes sooner: `107,310`, the value `F 53207` of `Rule30ForcedFront`. -/
theorem F_low : F wdA0 53207 = 107310 ∧ F wdA1 53207 = 107310 ∧ F wdB0 53207 = 107310 ∧ F wdB1 53207 = 107310 := by
  have h0 : F wdA0 53207 = 107310 := F_of_S a_53207
  have h2 : F wdB0 53207 = 107310 := F_of_S b_53207
  exact ⟨h0, by rw [← h0]; exact (F_congr 53207 (fun i hi => wA1_eq_A0 i (by omega))).symm, h2,
    by rw [← h2]; exact (F_congr 53207 (fun i hi => wB1_eq_B0 i (by omega))).symm⟩

theorem low_front {a : Nat → Nat → Bool} {v s : Nat} {w : Nat → Nat} (hF : F w 53207 = 107310)
    (hs : ∀ j t, j ≤ 53207 → Sp v j t = Sp A0 j t) (h : AlignedFrom a v s (F w) 87866) : OnStrip a A0 s 107310 53207 :=
  fun j hj t ht => by
    rw [h j (by omega) t (Nat.le_trans (by rw [← hF]; exact F_mono w hj) ht)]
    exact hs j t hj

/-- **Through the first fork's wheel**: every array with the recurrence and a black start carries the strip of `A0` through wheel 53,207
from strip tick 107,310, that is from tick at most 107,325 of its own clock. -/
theorem forced_front_low {a : Nat → Nat → Bool} (ha : Recurrence a) (ha0 : a 0 0 = true) :
    ∃ s, s ≤ 15 ∧ OnStrip a A0 s 107310 53207 := by
  obtain ⟨s, hs, h⟩ := forced_front_four ha ha0
  obtain ⟨f0, f1, f2, f3⟩ := F_low
  have eB0 : ∀ j t, j ≤ 53207 → Sp B0 j t = Sp A0 j t := fun j t hj =>
    low_of_phase A0_return B0_return low_B0 j t (by omega)
  refine ⟨s, hs, ?_⟩
  rcases h with h | h | h | h
  · exact low_front f0 (fun _ _ _ => rfl) h
  · exact low_front f1 (fun j t hj => low_of_phase A0_return A1_return low_A1 j t (by omega)) h
  · exact low_front f2 eB0 h
  · exact low_front f3 (fun j t hj => by
      rw [low_of_phase B0_return B1_return low_B1 j t (by omega)]; exact eB0 j t hj) h

/-- Every configuration with a leftmost black cell, through wheel 53,207 from tick 107,310 + s of its own clock, s ≤ 15. -/
theorem forced_front_low_left_side {x : Int → Bool} {lo : Int} (hleft : ∀ p, p < lo → x p = false)
    (hlo : x lo = true) : ∃ s, s ≤ 15 ∧ OnStrip (Ld x lo) A0 s 107310 53207 :=
  forced_front_low (Ld_recurrence hleft) (by simpa [Ld, evol] using hlo)

'''
m = 'end Ruliology.CellularAutomata.Rule30FourFronts'
assert m in fin
fin = fin.replace(m, low_thms + m)
old_lin = '''The kit-style linear bound with five white wheels below 87,866 is 2,811,713.'''
new_lin = '''The kit's linear bound `frontBound_le_linear` at period 16 is 1,405,857 at that wheel.'''
assert old_lin in fin; fin = fin.replace(old_lin, new_lin)
open(sys.argv[2], 'w').write(fin)
print('wrote', sys.argv[2], len(fin), 'bytes;', 'F(87866):', {s: ST[s][87866][0] for s in V})
