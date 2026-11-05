"""five_fronts_gen.py: the data module `Rule30FiveFronts` for CL736 stage 2. Recomputes the five strips through wheel 165,749
(the single black cell's, A1's, B0's, B1's, and B0's second child at the fork 165,748) on 165,750 wheels at period 32, runs the
settling recursion at phase 0, and writes the Lean module: five literals, their returns, the doubling and fork facts, the
black windows, Local's walk segments (a head to a multiple of 32, the rounds, a tail, and four facts per black run, L1524),
the chains, and the theorems. The numbers in the kernel facts come from this Python; the kernel confirms or refutes each.
Usage: python3 five_fronts_gen.py OUTFILE   (no OUTFILE: print the segments only)."""
import re, sys, time, hashlib
import numpy as np
K = 165750; MASK = (1 << K) - 1; T_END = 340000; P = 32; JMAX = 165749; BLK = 512   # rounds of 32 ticks per kernel fact
SRC = 'reports/wolfram-agents/submissions/four-left-sides/Rule30FourLeftSides.lean'
src = open(SRC).read()
def step(v): return ((v << 2) ^ ((v << 1) | v)) & MASK
def literal(name):
    m = re.search(r'^def %s : Nat := (.*?)$' % name, src, re.M); body = m.group(1)
    h = int(re.findall(r'0x[0-9a-fA-F]+', body)[0], 16); sh = re.search(r'<<<\s*(\d+)', body)
    return h << int(sh.group(1)) if sh else h
def bits_of(x): return np.unpackbits(np.frombuffer(x.to_bytes((K + 7) // 8, 'little'), dtype=np.uint8), bitorder='little')[:K]
def digest(x): return hashlib.sha256(format(x, 'x').encode()).hexdigest()[:16]
A0o = literal('A0'); A1o = A0o ^ literal('A1'); B0o = A0o ^ literal('B0'); B1o = B0o ^ literal('B1')
t0 = time.time()
rows = {}
for name, v in [('A0', 1), ('A1', A1o), ('B0', B0o), ('B1', B1o)]:
    x = v
    for _ in range(T_END): x = step(x)
    rows[name] = x
rows['B2'] = rows['B0'] ^ (1 << (K - 1))
names = ['A0', 'A1', 'B0', 'B1', 'B2']
print(f"rows: {time.time()-t0:.1f} s; digests " + ", ".join(f"{n} {digest(rows[n])}" for n in names))
def cycle(x):
    c = [x]
    for _ in range(P): c.append(step(c[-1]))
    assert c[P] == x, "no 32-tick return"
    return c[:P]
cyc = {n: cycle(rows[n]) for n in names}
ret16 = {n: cyc[n][16] == rows[n] for n in names}
print("16-tick returns:", ret16)
def words_of(c):
    bits = np.stack([bits_of(r) for r in c]).astype(np.int64)
    return [int(w) for w in (bits * (1 << np.arange(P, dtype=np.int64))[:, None]).sum(axis=0)]
W = {n: words_of(cyc[n]) for n in names}
whites = {n: [j for j in range(K) if W[n][j] == 0 and j >= 2] for n in names}
print("white wheels:", whites)
def srch(w, m):
    for r in range(P):
        if (w >> ((m + r) % P)) & 1: return r
    return P
def fstep(w, j, st):
    a, b = st; m = max(a, b)
    return (b, m) if w[j + 1] == 0 else (b, m + srch(w[j + 1], m) + 1)
def run(w, j0, n, st):
    for j in range(j0, j0 + n): st = fstep(w, j, st)
    return st
def states(w):      # S(j) for all j <= JMAX - 1 ... we need S(j) = state after reading wheels 1..j
    S = [(0, 1)]
    st = (0, 1)
    for j in range(JMAX): st = fstep(w, j, st); S.append(st)
    return S
S = {n: states(W[n]) for n in names}
F = {n: [s[0] for s in S[n]] + [S[n][-1][1]] for n in names}
print("F(53207), F(87866), F(165749):", {n: (F[n][53207], F[n][87866], F[n][JMAX]) for n in names})
assert all(F[n][JMAX] == S[n][JMAX - 1][1] for n in names)
# the segments: per strip, the runs of black wheels after wheel 400 through wheel 165,748, split at white wheels
def segments(n):
    segs = []; j = 400
    ws = [w for w in whites[n] if w > 400]
    while j < JMAX - 1:
        nxt = min([w for w in ws if w > j] + [JMAX - 1])    # next white wheel or the end (wheel 165,748 is the last read)
        if nxt > j:                                          # black run reading wheels j+1 .. nxt-1 if nxt is white, else .. nxt
            end = nxt - 1 if nxt in ws else nxt
            if end > j:
                segs.append(('black', j, end - j))            # frun w j (end - j): reads j+1 .. end
                j = end
        if nxt in ws and nxt <= JMAX - 1:
            segs.append(('white', nxt - 1, 1)); j = nxt       # frun w (nxt-1) 1: reads wheel nxt (white)
        if nxt == JMAX - 1 and nxt not in ws: break
    return segs
SEG = {n: segments(n) for n in names}
for n in names: print(n, SEG[n])
def seg_params(n, j0, cnt):
    a, b = S[n][j0]; A, B = S[n][j0 + cnt]
    h = (P - b % P) % P; rest = A - 1 - b - h
    assert rest >= 0 and a <= b and b < A and A < B and cnt >= 2, (n, j0, cnt, a, b, A, B)
    g, d = divmod(rest, P)
    return a, b, A, B, h, g, d
# share: A1 from A0 through 58,286; B0 from A0 through 53,207; B1 from B0 through 72,575; B2 from B0 through 165,748 (F only)
share = {'A1': ('A0', 58286), 'B0': ('A0', 53207), 'B1': ('B0', 72575)}
for n in names:
    base = n in share and share[n][1]
    for kind, j0, cnt in SEG[n]:
        if n in share and j0 + cnt <= share[n][1]: continue
        if kind == 'black':
            a, b, A, B, h, g, d = seg_params(n, j0, cnt)
            print(f"  {n}: black run j0 {j0} n {cnt}: ({a}, {b}) -> ({A}, {B}); h {h} g {g} d {d}; ticks {B - b}")
        else:
            a, b = S[n][j0]; print(f"  {n}: white wheel {j0 + 1}: ({a}, {b}) -> ({b}, {b})")
if len(sys.argv) < 2: sys.exit(0)
# ---------- the Lean module ----------
L = []
L.append(r'''module

public import Ruliology.CellularAutomata.Rule30FiveFrontsBase

/-!
# Five left sides of rule 30 through wheel 165,749, each with its settling tick

`Rule30FourLeftSides` placed every configuration with a leftmost black cell on one of four strips through wheel 87,866;
`Rule30FourFronts` gave the tick. Here both go on to wheel 165,749, the first branch node beyond, on a register of 165,750
wheels at period 32. The single black cell's strip `A0` has a white wheel at 87,866 whose farther word has odd parity, so its
child's period doubles to 32 and the complement of the child is the child's own rotation by 16: a shift of 16 that the
wheels below do not see (`white_shift`). `A1` and `B1` have no white wheel between 87,867 and 165,749. `B0` has one at 165,748,
whose farther word has even parity, so its child keeps period 16 and the complement is a fifth strip, `B2`
(`white_fork`). The settling recursion of `Rule30FrontLaw`, read on each strip's thirty-two-row cycle and carried through
the tree (`Rule30FiveFrontsBase`), gives `forced_front_five`: every array with the left-diagonal recurrence and a black start
carries one of the five strips on every wheel through 165,749 from strip tick `F j`, at a shift of at most `15 + 16 = 31`.
The fronts at wheel 165,749 are 333,333 (`A0`), 333,257 (`A1`), 333,503 (`B0` and `B2`) and 334,150 (`B1`), by the walk
(`seg_black`) at thirty-two ticks a round, in blocks; so from strip tick 334,150, that is from tick at most 334,181 of its own
clock, every configuration with a leftmost black cell carries the whole of its strip through 165,749
(`forced_front_five_uniform`, `forced_front_five_left_side`, `forced_front_five_seed`). The five strips are realized by finite
rows, no time shift relates two of them, and each configuration is on exactly one (`exactly_five_left_sides`,
`on_exactly_one`); the classification holds with its shift bounded by 31 (`classification_bounded`). As arithmetic, iterating
`v ↦ 4 v ⊕ (2 v ∨ v)` modulo `2 ^ 165750` from any odd `v` reaches one of the five rows (`odd_reaches_one_of_five`).
The rows: `A0` is the single cell's row at tick 340,000, `A1`, `B0`, `B1` are the rows of `Rule30FourLeftSides` evolved to tick
340,000, `B2` is `B0` with bit 165,749 complemented. The tree of forks and doublings to this depth was first found by
computation, in the contributors' record; here it is a theorem as far as it is used. Nothing here concerns the center column or the Prize problems, and 165,749 is
where these rows stop, not a claim about what happens beyond it.
-/

@[expose] public section

namespace Ruliology.CellularAutomata.Rule30FiveFronts

open Rule30FiveFrontsBase
open Rule30AgedLeftDiagonals Rule30FiniteDiagonals Rule30Diagonals Rule30Realization
open Rule30UniversalLeftSide (rowAt rowAt_add_mul ofRow ofRow_left Ld_ofRow D_recurrence)

set_option autoImplicit false

/-- The register: wheels `0, …, 165,749`. -/
abbrev K : Nat := 165750

/-! ### The five rows -/

''')
for n in ['A0', 'A1', 'B0', 'B1']:
    L.append(f"def {n} : Nat := 0x{rows[n]:x}\n\n")
L.append("/-- The second child at the fork 165,748: `B0` with bit 165,749 complemented. -/\ndef B2 : Nat := B0 ^^^ (1 <<< 165749)\n\n")
for n in names: L.append(f"theorem {n}_return : rowAt K {n} 32 = {n} := by decide +kernel\n")
for n in ['A1', 'B0', 'B1', 'B2']: L.append(f"theorem {n}_return16 : rowAt K {n} 16 = {n} := by decide +kernel\n")
L.append(r'''
set_option exponentiation.threshold 200000 in
/-- All five rows are finite, with their leftmost black cell at position 0. -/
theorem rows_finite : A0 < 2 ^ K ∧ A1 < 2 ^ K ∧ B0 < 2 ^ K ∧ B1 < 2 ^ K ∧ B2 < 2 ^ K ∧
    A0.testBit 0 = true ∧ A1.testBit 0 = true ∧ B0.testBit 0 = true ∧ B1.testBit 0 = true ∧ B2.testBit 0 = true := by
  decide +kernel

/-! ### Below the first fork, on `A0` -/

theorem A0_zero_phase : ∀ r, r < 32 → Sp K A0 0 r = true := by decide +kernel
theorem A0_one_phase : ∀ r, r < 32 → Sp K A0 1 r = true := by decide +kernel
theorem A0_zero (t : Nat) : Sp K A0 0 t = true := black_of_phase A0_return A0_zero_phase t
theorem A0_one (t : Nat) : Sp K A0 1 t = true := black_of_phase A0_return A0_one_phase t

set_option exponentiation.threshold 200000 in
theorem black_mask : (orRows K A0 32 ||| whiteMask) % 2 ^ 53207 = 2 ^ 53207 - 1 := by decide +kernel

theorem per2 : ∀ r, r < 32 → rowAt K A0 (r + 1) % 2 ^ (2 + 1) = rowAt K A0 r % 2 ^ (2 + 1) := by decide +kernel
theorem anti2 : ∀ r, r < 32 → Sp K A0 (2 + 1) (r + 1) = !Sp K A0 (2 + 1) r := by decide +kernel
theorem per7 : ∀ r, r < 32 → rowAt K A0 (r + 2) % 2 ^ (7 + 1) = rowAt K A0 r % 2 ^ (7 + 1) := by decide +kernel
theorem anti7 : ∀ r, r < 32 → Sp K A0 (7 + 1) (r + 2) = !Sp K A0 (7 + 1) r := by decide +kernel
theorem per28 : ∀ r, r < 32 → rowAt K A0 (r + 4) % 2 ^ (28 + 1) = rowAt K A0 r % 2 ^ (28 + 1) := by decide +kernel
theorem anti28 : ∀ r, r < 32 → Sp K A0 (28 + 1) (r + 4) = !Sp K A0 (28 + 1) r := by decide +kernel
set_option exponentiation.threshold 200000 in
theorem per399 : ∀ r, r < 32 → rowAt K A0 (r + 8) % 2 ^ (399 + 1) = rowAt K A0 r % 2 ^ (399 + 1) := by decide +kernel
theorem anti399 : ∀ r, r < 32 → Sp K A0 (399 + 1) (r + 8) = !Sp K A0 (399 + 1) r := by decide +kernel

/-! ### The doubling at 87,866 and the forks -/

set_option exponentiation.threshold 200000 in
/-- Below wheel 87,867 the strip of `A0` still has period 16. -/
theorem per87866 : ∀ r, r < 32 → rowAt K A0 (r + 16) % 2 ^ (87866 + 1) = rowAt K A0 r % 2 ^ (87866 + 1) := by decide +kernel
/-- Wheel 87,867 of `A0` is complemented after 16 ticks: its period is 32. -/
theorem anti87866 : ∀ r, r < 32 → Sp K A0 (87866 + 1) (r + 16) = !Sp K A0 (87866 + 1) r := by decide +kernel

theorem white_53207 : ∀ r, r < 32 → Sp K A0 53207 r = false := by decide +kernel
theorem white_58286 : ∀ r, r < 32 → Sp K A0 58286 r = false := by decide +kernel
theorem white_87866 : ∀ r, r < 32 → Sp K A0 87866 r = false := by decide +kernel
theorem white_72575 : ∀ r, r < 32 → Sp K B0 72575 r = false := by decide +kernel
theorem white_165748 : ∀ r, r < 32 → Sp K B0 165748 r = false := by decide +kernel

set_option exponentiation.threshold 200000 in
theorem low_B0 : ∀ r, r < 32 → rowAt K B0 r % 2 ^ 53208 = rowAt K A0 r % 2 ^ 53208 := by decide +kernel
set_option exponentiation.threshold 200000 in
theorem low_A1 : ∀ r, r < 32 → rowAt K A1 r % 2 ^ 58287 = rowAt K A0 r % 2 ^ 58287 := by decide +kernel
set_option exponentiation.threshold 200000 in
theorem low_B1 : ∀ r, r < 32 → rowAt K B1 r % 2 ^ 72576 = rowAt K B0 r % 2 ^ 72576 := by decide +kernel
set_option exponentiation.threshold 200000 in
theorem low_B2 : ∀ r, r < 32 → rowAt K B2 r % 2 ^ 165749 = rowAt K B0 r % 2 ^ 165749 := by decide +kernel
theorem top_B0 : ∀ r, r < 32 → Sp K B0 53208 r = !Sp K A0 53208 r := by decide +kernel
theorem top_A1 : ∀ r, r < 32 → Sp K A1 58287 r = !Sp K A0 58287 r := by decide +kernel
theorem top_B1 : ∀ r, r < 32 → Sp K B1 72576 r = !Sp K B0 72576 r := by decide +kernel
theorem top_B2 : ∀ r, r < 32 → Sp K B2 165749 r = !Sp K B0 165749 r := by decide +kernel

/-! ### The black windows -/

set_option exponentiation.threshold 200000 in
theorem wA0_1 : (orRows K A0 32 >>> 53208) % 2 ^ (58286 - 53208) = 2 ^ (58286 - 53208) - 1 := by decide +kernel
set_option exponentiation.threshold 200000 in
theorem wA0_2 : (orRows K A0 32 >>> 58287) % 2 ^ (87866 - 58287) = 2 ^ (87866 - 58287) - 1 := by decide +kernel
set_option exponentiation.threshold 200000 in
theorem wA0_3 : (orRows K A0 32 >>> 87867) % 2 ^ (165749 - 87867) = 2 ^ (165749 - 87867) - 1 := by decide +kernel
set_option exponentiation.threshold 200000 in
theorem wA1_1 : (orRows K A1 32 >>> 58287) % 2 ^ (165749 - 58287) = 2 ^ (165749 - 58287) - 1 := by decide +kernel
set_option exponentiation.threshold 200000 in
theorem wB0_1 : (orRows K B0 32 >>> 53208) % 2 ^ (72575 - 53208) = 2 ^ (72575 - 53208) - 1 := by decide +kernel
set_option exponentiation.threshold 200000 in
theorem wB0_2 : (orRows K B0 32 >>> 72576) % 2 ^ (165748 - 72576) = 2 ^ (165748 - 72576) - 1 := by decide +kernel
set_option exponentiation.threshold 200000 in
theorem wB1_1 : (orRows K B1 32 >>> 72576) % 2 ^ (165749 - 72576) = 2 ^ (165749 - 72576) - 1 := by decide +kernel

/-! ### The words of the five strips -/

abbrev wA0 : Nat → Nat := wd K A0
abbrev wA1 : Nat → Nat := wd K A1
abbrev wB0 : Nat → Nat := wd K B0
abbrev wB1 : Nat → Nat := wd K B1
abbrev wB2 : Nat → Nat := wd K B2
theorem wordsA0 : Words K A0 wA0 := words K A0
theorem wordsA1 : Words K A1 wA1 := words K A1
theorem wordsB0 : Words K B0 wB0 := words K B0
theorem wordsB1 : Words K B1 wB1 := words K B1
theorem wordsB2 : Words K B2 wB2 := words K B2

theorem wA0_53207 : wA0 53207 = 0 := word_zero_of_white wordsA0 white_53207
theorem wA0_58286 : wA0 58286 = 0 := word_zero_of_white wordsA0 white_58286
theorem wA0_87866 : wA0 87866 = 0 := word_zero_of_white wordsA0 white_87866
theorem wB0_72575 : wB0 72575 = 0 := word_zero_of_white wordsB0 white_72575
theorem wB0_165748 : wB0 165748 = 0 := word_zero_of_white wordsB0 white_165748

set_option exponentiation.threshold 200000 in
theorem hbwA0 : ∀ m, m < 53207 → wA0 m ≠ 0 ∨ m = 2 ∨ m = 7 ∨ m = 28 ∨ m = 399 := fun m hm => by
  rcases black_or_white black_mask hm with ⟨r, hr, hb⟩ | h
  · exact Or.inl (word_ne_of_black wordsA0 hr hb)
  · exact Or.inr h

''')
for (nm, strip, lo, hi, fact) in [('bA0_1','A0',53208,58286,'wA0_1'), ('bA0_2','A0',58287,87866,'wA0_2'), ('bA0_3','A0',87867,165749,'wA0_3'),
                                  ('bA1_1','A1',58287,165749,'wA1_1'), ('bB0_1','B0',53208,72575,'wB0_1'), ('bB0_2','B0',72576,165748,'wB0_2'),
                                  ('bB1_1','B1',72576,165749,'wB1_1')]:
    L.append(f'''set_option exponentiation.threshold 200000 in
theorem {nm} : ∀ m, {lo} ≤ m → m < {hi} → w{strip} m ≠ 0 := fun m h1 h2 => by
  obtain ⟨r, hr, hb⟩ := black_window_phase {fact} h1 (by omega)
  exact word_ne_of_black words{strip} hr hb
''')
L.append(r'''
/-- Below a fork the two strips have the same words, so the same fronts. -/
theorem wB0_eq_A0 : ∀ i, i + 2 ≤ 53208 → wA0 (i + 1) = wB0 (i + 1) := fun i hi =>
  (word_eq_of_low wordsA0 wordsB0 (fun r _ => low_of_phase A0_return B0_return low_B0 (i + 1) r (by omega))).symm
theorem wA1_eq_A0 : ∀ i, i + 2 ≤ 58287 → wA0 (i + 1) = wA1 (i + 1) := fun i hi =>
  (word_eq_of_low wordsA0 wordsA1 (fun r _ => low_of_phase A0_return A1_return low_A1 (i + 1) r (by omega))).symm
theorem wB1_eq_B0 : ∀ i, i + 2 ≤ 72576 → wB0 (i + 1) = wB1 (i + 1) := fun i hi =>
  (word_eq_of_low wordsB0 wordsB1 (fun r _ => low_of_phase B0_return B1_return low_B1 (i + 1) r (by omega))).symm
theorem wB2_eq_B0 : ∀ i, i + 2 ≤ 165749 → wB0 (i + 1) = wB2 (i + 1) := fun i hi =>
  (word_eq_of_low wordsB0 wordsB2 (fun r _ => low_of_phase B0_return B2_return low_B2 (i + 1) r (by omega))).symm

/-! ### The tree, with the time carried -/

/-- **The forced front on the five strips.** Every array with the left-diagonal recurrence and a black wheel 0 carries one of
the five strips on every wheel `j ≤ 165,749` from strip tick `F j` on, at a shift of at most `31`. -/
theorem forced_front_five {a : Nat → Nat → Bool} (ha : Recurrence a) (ha0 : a 0 0 = true) :
    ∃ s, s ≤ 31 ∧ (AlignedFrom K a A0 s (F wA0) 165749 ∨ AlignedFrom K a A1 s (F wA1) 165749 ∨
      AlignedFrom K a B0 s (F wB0) 165749 ∨ AlignedFrom K a B1 s (F wB1) 165749 ∨
      AlignedFrom K a B2 s (F wB2) 165749) := by
  obtain ⟨s, hs, h⟩ := low_from (by decide) ha ha0 A0_return wordsA0 A0_zero A0_one hbwA0
    (strip_shift A0_return per2 anti2) (strip_shift A0_return per7 anti7) (strip_shift A0_return per28 anti28)
    (strip_shift A0_return per399 anti399) 53207 (Nat.le_refl _)
  have hs15 : s ≤ 15 := by rw [lsum_53207] at hs; exact hs
  rcases step_white ha A0_return wordsA0 (by decide) h wA0_53207 with hA | hB
  · -- the A side
    have h2 : AlignedFrom K a A0 s (F wA0) 58286 :=
      extend_from ha A0_return wordsA0 (by omega) (by decide) (by omega) hA bA0_1
    rcases step_white ha A0_return wordsA0 (by decide) h2 wA0_58286 with hA0 | hA1
    · -- A0: through 87,866, then the doubling
      have h3 : AlignedFrom K a A0 s (F wA0) 87866 :=
        extend_from ha A0_return wordsA0 (by omega) (by decide) (by omega) hA0 bA0_2
      rcases step_white ha A0_return wordsA0 (by decide) h3 wA0_87866 with hD0 | hD1
      · exact ⟨s, by omega, Or.inl (extend_from ha A0_return wordsA0 (by omega) (by decide) (by omega) hD0 bA0_3)⟩
      · have h4 : AlignedFrom K a A0 (s + 16) (F wA0) 87867 := white_shift h3 hD1
          (strip_shift A0_return per87866 anti87866).1 (strip_shift A0_return per87866 anti87866).2
        exact ⟨s + 16, by omega, Or.inl (extend_from ha A0_return wordsA0 (by omega) (by decide) (by omega) h4 bA0_3)⟩
    · -- A1
      have h3 : AlignedFrom K a A1 s (F wA0) 58287 := white_fork h2 hA1
        (fun j t hj => low_of_phase A0_return A1_return low_A1 j t (by omega))
        (comp_of_phase A0_return A1_return top_A1)
      have h4 : AlignedFrom K a A1 s (F wA1) 58287 :=
        alignedFrom_congr (fun j hj => F_congr j (fun i hi => wA1_eq_A0 i (by omega))) h3
      exact ⟨s, by omega, Or.inr (Or.inl (extend_from ha A1_return wordsA1 (by omega) (by decide) (by omega) h4 bA1_1))⟩
  · -- the B side
    have h3 : AlignedFrom K a B0 s (F wA0) 53208 := white_fork h hB
      (fun j t hj => low_of_phase A0_return B0_return low_B0 j t (by omega))
      (comp_of_phase A0_return B0_return top_B0)
    have h4 : AlignedFrom K a B0 s (F wB0) 53208 :=
      alignedFrom_congr (fun j hj => F_congr j (fun i hi => wB0_eq_A0 i (by omega))) h3
    have h5 : AlignedFrom K a B0 s (F wB0) 72575 :=
      extend_from ha B0_return wordsB0 (by omega) (by decide) (by omega) h4 bB0_1
    rcases step_white ha B0_return wordsB0 (by decide) h5 wB0_72575 with hB0 | hB1
    · -- B0: through 165,748, then the fork
      have h6 : AlignedFrom K a B0 s (F wB0) 165748 :=
        extend_from ha B0_return wordsB0 (by omega) (by decide) (by omega) hB0 bB0_2
      rcases step_white ha B0_return wordsB0 (by decide) h6 wB0_165748 with hC0 | hC1
      · exact ⟨s, by omega, Or.inr (Or.inr (Or.inl hC0))⟩
      · have h7 : AlignedFrom K a B2 s (F wB0) 165749 := white_fork h6 hC1
          (fun j t hj => low_of_phase B0_return B2_return low_B2 j t (by omega))
          (comp_of_phase B0_return B2_return top_B2)
        have h8 : AlignedFrom K a B2 s (F wB2) 165749 :=
          alignedFrom_congr (fun j hj => F_congr j (fun i hi => wB2_eq_B0 i (by omega))) h7
        exact ⟨s, by omega, Or.inr (Or.inr (Or.inr (Or.inr h8)))⟩
    · -- B1
      have h6 : AlignedFrom K a B1 s (F wB0) 72576 := white_fork h5 hB1
        (fun j t hj => low_of_phase B0_return B1_return low_B1 j t (by omega))
        (comp_of_phase B0_return B1_return top_B1)
      have h7 : AlignedFrom K a B1 s (F wB1) 72576 :=
        alignedFrom_congr (fun j hj => F_congr j (fun i hi => wB1_eq_B0 i (by omega))) h6
      exact ⟨s, by omega, Or.inr (Or.inr (Or.inr (Or.inl
        (extend_from ha B1_return wordsB1 (by omega) (by decide) (by omega) h7 bB1_1))))⟩

/-- The classification, recovered through wheel 165,749 with its shift bounded by `31`. -/
theorem classification_bounded {a : Nat → Nat → Bool} (ha : Recurrence a) (ha0 : a 0 0 = true) :
    ∃ s, s ≤ 31 ∧ (Aligned K a A0 s 165749 ∨ Aligned K a A1 s 165749 ∨ Aligned K a B0 s 165749 ∨
      Aligned K a B1 s 165749 ∨ Aligned K a B2 s 165749) := by
  obtain ⟨s, hs, h⟩ := forced_front_five ha ha0
  refine ⟨s, hs, ?_⟩
  rcases h with h | h | h | h | h
  · exact Or.inl (aligned_of_alignedFrom h)
  · exact Or.inr (Or.inl (aligned_of_alignedFrom h))
  · exact Or.inr (Or.inr (Or.inl (aligned_of_alignedFrom h)))
  · exact Or.inr (Or.inr (Or.inr (Or.inl (aligned_of_alignedFrom h))))
  · exact Or.inr (Or.inr (Or.inr (Or.inr (aligned_of_alignedFrom h))))

/-! ### The numbers, by the walk -/

theorem a_low : frun wA0 0 400 (0, 1) = (783, 784) := by decide +kernel
''')
# the walk segments and chains
def walk_sim(n, ticks, t, j):
    c = cyc[n]
    for _ in range(ticks):
        j += (c[t % P] >> j) & 1; t += 1
    return j
def seg_text(n, lab, j0, cnt):
    a, b, A, B, h, g, d = seg_params(n, j0, cnt)
    R = f"(rowAt K {n})"; out = []
    j = j0 + 1; t = b
    j1 = walk_sim(n, h, t, j); t += h
    out.append(f"theorem {lab}_h : walk {R} {h} {b} {j0 + 1} = {j1} := by decide +kernel\n")
    blocks = [BLK] * (g // BLK) + ([g % BLK] if g % BLK else [])
    jj = j1; facts = []
    for i, rounds in enumerate(blocks):
        jn = walk_sim(n, P * rounds, t, jj); t += P * rounds
        out.append(f"theorem {lab}_b{i} : w32 {R} {rounds} {jj} = {jn} := by decide +kernel\n")
        facts.append(f"{lab}_b{i}"); jj = jn
    j2 = jj
    def nest(i):
        if i == len(facts) - 1: return facts[i]
        return f"(w32_chain _ (by decide) {facts[i]} {nest(i + 1)})"
    if len(facts) == 1:
        out.append(f"theorem {lab}_g : w32 {R} {g} {j1} = {j2} := {facts[0]}\n")
    else:
        out.append(f"theorem {lab}_g : w32 {R} {g} {j1} = {j2} :=\n  {nest(0)}\n")
    J = walk_sim(n, d, t, j2)
    assert J == j0 + cnt - 1 and t == b + h + P * g, (n, lab, J, j0 + cnt - 1)
    out.append(f"theorem {lab}_d : walk {R} {d} ({b} + {h} + 32 * {g}) {j2} = {j0 + cnt - 1} := by decide +kernel\n")
    out.append(f"theorem {lab} : frun w{n} {j0} {cnt} ({a}, {b}) = ({A}, {B}) :=\n"
               f"  seg_black (K := K) (v := {n}) (h := {h}) (g := {g}) (d := {d}) (by decide) (by decide) (by decide) (by decide) (by decide) (by decide)\n"
               f"    (fastWalk_of _ {lab}_h {lab}_g {lab}_d) (by decide +kernel) (by decide +kernel) (by decide +kernel)\n")
    return "".join(out)
def white_text(n, lab, j0, wfact):
    a, b = S[n][j0]
    return f"theorem {lab} : frun w{n} {j0} 1 ({a}, {b}) = ({b}, {b}) := frun_white (by decide) {wfact}\n"
wfacts = {('A0', 53207): 'wA0_53207', ('A0', 58286): 'wA0_58286', ('A0', 87866): 'wA0_87866', ('B0', 72575): 'wB0_72575', ('B0', 165748): 'wB0_165748'}
chains = {}
# A0: full chain from a_low
labs = {'A0': [], 'A1': [], 'B0': [], 'B1': []}
cnt_lab = {}
def emit_strip(n, start_lab, start_j):
    """emit the segments of strip n after wheel start_j (state fact start_lab : frun w n 0 start_j (0,1) = S[start_j]); return the chain to S w 165748."""
    out = []; chain = [(start_lab, 0, start_j)]
    k = 0
    for kind, j0, cnt in SEG[n]:
        if j0 < start_j: continue
        k += 1; lab = f"{n.lower()}_{k}"
        if kind == 'black':
            out.append(seg_text(n, lab, j0, cnt)); chain.append((lab, j0, cnt))
        else:
            out.append(white_text(n, lab, j0, wfacts[(n, j0 + 1)])); chain.append((lab, j0, 1))
    return out, chain
def chain_text(n, chain, end):
    # chain: list of (lab, j0, cnt) with the first covering 0..start; produce S w n end = (..) via frun_chain nesting
    total = sum(c[2] for c in chain)
    assert total == end, (n, total, end)
    def nest(i):
        lab, j0, cnt = chain[i]
        if i == len(chain) - 1: return lab
        rest = sum(c[2] for c in chain[i + 1:])
        return f"(frun_chain _ {j0} {cnt} {rest} _ _ _ {lab}\n    {nest(i + 1)})"
    a, b = S[n][end]
    return f"theorem S{n}_{end} : S w{n} {end} = ({a}, {b}) :=\n  {nest(0)}\n"
# A0
outA0, chA0 = emit_strip('A0', 'a_low', 400)
L.extend(outA0)
# intermediate facts for sharing: S wA0 53207, S wA0 58286 (as frun from 0)
def prefix_fact(n, chain, end, lab):
    sub = []; tot = 0
    for c in chain:
        if tot + c[2] <= end: sub.append(c); tot += c[2]
        else: break
    assert tot == end, (n, tot, end)
    def nest(i):
        l, j0, cnt = sub[i]
        if i == len(sub) - 1: return l
        rest = sum(c[2] for c in sub[i + 1:])
        return f"(frun_chain _ {j0} {cnt} {rest} _ _ _ {l}\n    {nest(i + 1)})"
    a, b = S[n][end]
    return f"theorem {lab} : frun w{n} 0 {end} (0, 1) = ({a}, {b}) :=\n  {nest(0)}\n"
L.append(prefix_fact('A0', chA0, 53207, 'a_53207'))
L.append(prefix_fact('A0', chA0, 58286, 'a_58286'))
L.append(prefix_fact('A0', chA0, 87866, 'a_87866'))
L.append(chain_text('A0', chA0, 165748))
# B0 from a_53207 via low_congr
L.append("theorem b_53207 : frun wB0 0 53207 (0, 1) = (107310, 107310) :=\n  (low_congr (fun i hi => (wB0_eq_A0 i (by omega)).symm)).trans a_53207\n")
outB0, chB0 = emit_strip('B0', 'b_53207', 53207)
L.extend(outB0)
L.append(prefix_fact('B0', chB0, 72575, 'b_72575'))
L.append(chain_text('B0', chB0, 165748))
# A1 from a_58286
a58 = S['A0'][58286]
L.append(f"theorem a1_58286 : frun wA1 0 58286 (0, 1) = ({a58[0]}, {a58[1]}) :=\n  (low_congr (fun i hi => (wA1_eq_A0 i (by omega)).symm)).trans a_58286\n")
outA1, chA1 = emit_strip('A1', 'a1_58286', 58286)
L.extend(outA1)
L.append(chain_text('A1', chA1, 165748))
# B1 from b_72575
b72 = S['B0'][72575]
L.append(f"theorem b1_72575 : frun wB1 0 72575 (0, 1) = ({b72[0]}, {b72[1]}) :=\n  (low_congr (fun i hi => (wB1_eq_B0 i (by omega)).symm)).trans b_72575\n")
outB1, chB1 = emit_strip('B1', 'b1_72575', 72575)
L.extend(outB1)
L.append(chain_text('B1', chB1, 165748))
FA = {n: F[n][JMAX] for n in names}
L.append(f'''
/-- Read the front at wheel `j + 1` off the state after `j` wheels. -/
theorem F_of_S' {{w : Nat → Nat}} {{j a b : Nat}} (h : S w j = (a, b)) : F w (j + 1) = b := by
  rw [← S_snd, h]

theorem FA0_165749 : F wA0 165749 = {FA['A0']} := F_of_S' SA0_165748
theorem FA1_165749 : F wA1 165749 = {FA['A1']} := F_of_S' SA1_165748
theorem FB0_165749 : F wB0 165749 = {FA['B0']} := F_of_S' SB0_165748
theorem FB1_165749 : F wB1 165749 = {FA['B1']} := F_of_S' SB1_165748
theorem FB2_165749 : F wB2 165749 = {FA['B2']} :=
  (F_congr 165749 (fun i hi => (wB2_eq_B0 i (by omega)).symm)).trans FB0_165749

/-- The fronts below the first fork and at the doubling: the numbers of `Rule30ForcedFront` and `Rule30FourFronts`. -/
theorem F_low : F wA0 53207 = {F['A0'][53207]} ∧ F wA0 87866 = {F['A0'][87866]} :=
  ⟨F_of_S a_53207, F_of_S a_87866⟩

/-- Every front through wheel 165,749 is at most 334,150, the `B1` front there. -/
theorem fronts_le : (∀ j, j ≤ 165749 → F wA0 j ≤ 334150) ∧ (∀ j, j ≤ 165749 → F wA1 j ≤ 334150) ∧
    (∀ j, j ≤ 165749 → F wB0 j ≤ 334150) ∧ (∀ j, j ≤ 165749 → F wB1 j ≤ 334150) ∧
    ∀ j, j ≤ 165749 → F wB2 j ≤ 334150 :=
  ⟨fun j hj => Nat.le_trans (F_mono wA0 hj) (by rw [FA0_165749]; omega),
   fun j hj => Nat.le_trans (F_mono wA1 hj) (by rw [FA1_165749]; omega),
   fun j hj => Nat.le_trans (F_mono wB0 hj) (by rw [FB0_165749]; omega),
   fun j hj => Nat.le_trans (F_mono wB1 hj) (by rw [FB1_165749]; omega),
   fun j hj => Nat.le_trans (F_mono wB2 hj) (by rw [FB2_165749]; omega)⟩

/-! ### The headlines -/

/-- **From strip tick 334,150**, that is from tick at most 334,181 of its own clock, every array with the recurrence and a
black start carries the whole of one of the five strips through wheel 165,749. -/
theorem forced_front_five_uniform {{a : Nat → Nat → Bool}} (ha : Recurrence a) (ha0 : a 0 0 = true) :
    ∃ s, s ≤ 31 ∧ (OnStrip K a A0 s 334150 165749 ∨ OnStrip K a A1 s 334150 165749 ∨
      OnStrip K a B0 s 334150 165749 ∨ OnStrip K a B1 s 334150 165749 ∨ OnStrip K a B2 s 334150 165749) := by
  obtain ⟨s, hs, h⟩ := forced_front_five ha ha0
  refine ⟨s, hs, ?_⟩
  rcases h with h | h | h | h | h
  · exact Or.inl (onStrip_of_alignedFrom fronts_le.1 h)
  · exact Or.inr (Or.inl (onStrip_of_alignedFrom fronts_le.2.1 h))
  · exact Or.inr (Or.inr (Or.inl (onStrip_of_alignedFrom fronts_le.2.2.1 h)))
  · exact Or.inr (Or.inr (Or.inr (Or.inl (onStrip_of_alignedFrom fronts_le.2.2.2.1 h))))
  · exact Or.inr (Or.inr (Or.inr (Or.inr (onStrip_of_alignedFrom fronts_le.2.2.2.2 h))))

/-- **Every configuration with a leftmost black cell**, whatever lies to its right: on one of the five strips through wheel
165,749 from tick 334,150 + s of its own clock, s ≤ 31. -/
theorem forced_front_five_left_side {{x : Int → Bool}} {{lo : Int}} (hleft : ∀ p, p < lo → x p = false)
    (hlo : x lo = true) :
    ∃ s, s ≤ 31 ∧ (OnStrip K (Ld x lo) A0 s 334150 165749 ∨ OnStrip K (Ld x lo) A1 s 334150 165749 ∨
      OnStrip K (Ld x lo) B0 s 334150 165749 ∨ OnStrip K (Ld x lo) B1 s 334150 165749 ∨
      OnStrip K (Ld x lo) B2 s 334150 165749) :=
  forced_front_five_uniform (Ld_recurrence hleft) (by simpa [Ld, evol] using hlo)

/-- The single black cell. The proof does not say which strip. -/
theorem forced_front_five_seed :
    ∃ s, s ≤ 31 ∧ (OnStrip K D A0 s 334150 165749 ∨ OnStrip K D A1 s 334150 165749 ∨
      OnStrip K D B0 s 334150 165749 ∨ OnStrip K D B1 s 334150 165749 ∨ OnStrip K D B2 s 334150 165749) :=
  forced_front_five_uniform D_recurrence (D_zero 0)

/-- Every configuration with a leftmost black cell is on one of the five sides. -/
theorem left_side_classification {{x : Int → Bool}} {{lo : Int}} (hleft : ∀ p, p < lo → x p = false)
    (hlo : x lo = true) :
    ∃ s, Aligned K (Ld x lo) A0 s 165749 ∨ Aligned K (Ld x lo) A1 s 165749 ∨ Aligned K (Ld x lo) B0 s 165749 ∨
      Aligned K (Ld x lo) B1 s 165749 ∨ Aligned K (Ld x lo) B2 s 165749 :=
  let ⟨s, _, h⟩ := classification_bounded (Ld_recurrence hleft) (by simpa [Ld, evol] using hlo)
  ⟨s, h⟩

/-! ### The five are different, realized, and each configuration is on exactly one -/

/-- Wheels below 87,867 of `A0` keep period 16; the other four rows return after 16. -/
theorem per16_A0 : ∀ j, j ≤ 87866 → ∀ t, Sp K A0 j (t + 16) = Sp K A0 j t :=
  (strip_shift A0_return per87866 anti87866).1
theorem per16_of_return {{v : Nat}} (hv : rowAt K v 16 = v) (j t : Nat) : Sp K v j (t + 16) = Sp K v j t := by
  have h := Sp_add_mul' hv j t 1
  rwa [Nat.one_mul] at h

theorem comp_symm {{v v' w : Nat}} (h : ∀ t, Sp K v' w t = !Sp K v w t) : ∀ t, Sp K v w t = !Sp K v' w t := fun t => by
  rw [h t]; cases Sp K v w t <;> rfl

theorem prim_A0 : ∀ d, d < 16 → d ≠ 0 → ∃ q, q < 16 ∧ Sp K A0 400 (q + d) ≠ Sp K A0 400 q := by decide +kernel
theorem prim_A1 : ∀ d, d < 16 → d ≠ 0 → ∃ q, q < 16 ∧ Sp K A1 400 (q + d) ≠ Sp K A1 400 q := by decide +kernel
theorem prim_B0 : ∀ d, d < 16 → d ≠ 0 → ∃ q, q < 16 ∧ Sp K B0 400 (q + d) ≠ Sp K B0 400 q := by decide +kernel
theorem prim_B1 : ∀ d, d < 16 → d ≠ 0 → ∃ q, q < 16 ∧ Sp K B1 400 (q + d) ≠ Sp K B1 400 q := by decide +kernel

theorem lowA1 (j t : Nat) (hj : j < 58287) : Sp K A1 j t = Sp K A0 j t := low_of_phase A0_return A1_return low_A1 j t hj
theorem lowB0 (j t : Nat) (hj : j < 53208) : Sp K B0 j t = Sp K A0 j t := low_of_phase A0_return B0_return low_B0 j t hj
theorem lowB1 (j t : Nat) (hj : j < 72576) : Sp K B1 j t = Sp K B0 j t := low_of_phase B0_return B1_return low_B1 j t hj
theorem lowB2 (j t : Nat) (hj : j < 165749) : Sp K B2 j t = Sp K B0 j t := low_of_phase B0_return B2_return low_B2 j t hj
theorem compB0 : ∀ t, Sp K B0 53208 t = !Sp K A0 53208 t := comp_of_phase A0_return B0_return top_B0
theorem compA1 : ∀ t, Sp K A1 58287 t = !Sp K A0 58287 t := comp_of_phase A0_return A1_return top_A1
theorem compB1 : ∀ t, Sp K B1 72576 t = !Sp K B0 72576 t := comp_of_phase B0_return B1_return top_B1
theorem compB2 : ∀ t, Sp K B2 165749 t = !Sp K B0 165749 t := comp_of_phase B0_return B2_return top_B2

/-- **The five strips are pairwise unrelated** through wheel 165,749. -/
theorem five_distinct : ¬ Related K 165749 A0 A1 ∧ ¬ Related K 165749 A0 B0 ∧ ¬ Related K 165749 A0 B1 ∧
    ¬ Related K 165749 A0 B2 ∧ ¬ Related K 165749 A1 B0 ∧ ¬ Related K 165749 A1 B1 ∧ ¬ Related K 165749 A1 B2 ∧
    ¬ Related K 165749 B0 B1 ∧ ¬ Related K 165749 B0 B2 ∧ ¬ Related K 165749 B1 B2 :=
  ⟨not_related (w := 58287) (p := 400) (by omega) (by omega) (per16_A0 _ (by omega)) (per16_A0 _ (by omega))
      (per16_of_return A1_return16 400) (comp_symm compA1) (fun t => (lowA1 400 t (by omega)).symm) prim_A0,
   not_related (w := 53208) (p := 400) (by omega) (by omega) (per16_A0 _ (by omega)) (per16_A0 _ (by omega))
      (per16_of_return B0_return16 400) (comp_symm compB0) (fun t => (lowB0 400 t (by omega)).symm) prim_A0,
   not_related (w := 53208) (p := 400) (by omega) (by omega) (per16_A0 _ (by omega)) (per16_A0 _ (by omega))
      (per16_of_return B1_return16 400)
      (comp_symm (fun t => by rw [lowB1 53208 t (by omega)]; exact compB0 t))
      (fun t => by rw [lowB1 400 t (by omega), lowB0 400 t (by omega)]) prim_A0,
   not_related (w := 53208) (p := 400) (by omega) (by omega) (per16_A0 _ (by omega)) (per16_A0 _ (by omega))
      (per16_of_return B2_return16 400)
      (comp_symm (fun t => by rw [lowB2 53208 t (by omega)]; exact compB0 t))
      (fun t => by rw [lowB2 400 t (by omega), lowB0 400 t (by omega)]) prim_A0,
   not_related (w := 53208) (p := 400) (by omega) (by omega) (per16_of_return A1_return16 53208)
      (per16_of_return A1_return16 400) (per16_of_return B0_return16 400)
      (comp_symm (fun t => by rw [lowA1 53208 t (by omega)]; exact compB0 t))
      (fun t => by rw [lowA1 400 t (by omega), lowB0 400 t (by omega)]) prim_A1,
   not_related (w := 53208) (p := 400) (by omega) (by omega) (per16_of_return A1_return16 53208)
      (per16_of_return A1_return16 400) (per16_of_return B1_return16 400)
      (comp_symm (fun t => by rw [lowA1 53208 t (by omega), lowB1 53208 t (by omega)]; exact compB0 t))
      (fun t => by rw [lowA1 400 t (by omega), lowB1 400 t (by omega), lowB0 400 t (by omega)]) prim_A1,
   not_related (w := 53208) (p := 400) (by omega) (by omega) (per16_of_return A1_return16 53208)
      (per16_of_return A1_return16 400) (per16_of_return B2_return16 400)
      (comp_symm (fun t => by rw [lowA1 53208 t (by omega), lowB2 53208 t (by omega)]; exact compB0 t))
      (fun t => by rw [lowA1 400 t (by omega), lowB2 400 t (by omega), lowB0 400 t (by omega)]) prim_A1,
   not_related (w := 72576) (p := 400) (by omega) (by omega) (per16_of_return B0_return16 72576)
      (per16_of_return B0_return16 400) (per16_of_return B1_return16 400) (comp_symm compB1)
      (fun t => (lowB1 400 t (by omega)).symm) prim_B0,
   not_related (w := 165749) (p := 400) (by omega) (by omega) (per16_of_return B0_return16 165749)
      (per16_of_return B0_return16 400) (per16_of_return B2_return16 400) (comp_symm compB2)
      (fun t => (lowB2 400 t (by omega)).symm) prim_B0,
   not_related (w := 72576) (p := 400) (by omega) (by omega) (per16_of_return B1_return16 72576)
      (per16_of_return B1_return16 400) (per16_of_return B2_return16 400)
      (comp_symm (fun t => by rw [lowB2 72576 t (by omega), compB1 t]; cases Sp K B0 72576 t <;> rfl))
      (fun t => by rw [lowB1 400 t (by omega), lowB2 400 t (by omega)]) prim_B1⟩

theorem Ld_row (v : Nat) {{j : Nat}} (hj : j ≤ 165749) (t : Nat) : Ld (ofRow v) 0 j t = Sp K v j t :=
  Ld_ofRow (K := K) (by decide) v t j (by show j < 165750; omega)

/-- **All five occur.** Each strip is carried from tick 0 by a finite row with its leftmost black cell at position 0. -/
theorem five_realized (v : Nat) : Aligned K (Ld (ofRow v) 0) v 0 165749 :=
  fun _ hj => ⟨0, fun t _ => Ld_row v hj (t + 0)⟩

/-- **Each array is on exactly one side.** -/
theorem on_exactly_one {{a : Nat → Nat → Bool}} {{s s' : Nat}} :
    ¬ (Aligned K a A0 s 165749 ∧ Aligned K a A1 s' 165749) ∧ ¬ (Aligned K a A0 s 165749 ∧ Aligned K a B0 s' 165749) ∧
    ¬ (Aligned K a A0 s 165749 ∧ Aligned K a B1 s' 165749) ∧ ¬ (Aligned K a A0 s 165749 ∧ Aligned K a B2 s' 165749) ∧
    ¬ (Aligned K a A1 s 165749 ∧ Aligned K a B0 s' 165749) ∧ ¬ (Aligned K a A1 s 165749 ∧ Aligned K a B1 s' 165749) ∧
    ¬ (Aligned K a A1 s 165749 ∧ Aligned K a B2 s' 165749) ∧ ¬ (Aligned K a B0 s 165749 ∧ Aligned K a B1 s' 165749) ∧
    ¬ (Aligned K a B0 s 165749 ∧ Aligned K a B2 s' 165749) ∧ ¬ (Aligned K a B1 s 165749 ∧ Aligned K a B2 s' 165749) :=
  ⟨fun h => five_distinct.1 (side_unique A1_return h.1 h.2),
   fun h => five_distinct.2.1 (side_unique B0_return h.1 h.2),
   fun h => five_distinct.2.2.1 (side_unique B1_return h.1 h.2),
   fun h => five_distinct.2.2.2.1 (side_unique B2_return h.1 h.2),
   fun h => five_distinct.2.2.2.2.1 (side_unique B0_return h.1 h.2),
   fun h => five_distinct.2.2.2.2.2.1 (side_unique B1_return h.1 h.2),
   fun h => five_distinct.2.2.2.2.2.2.1 (side_unique B2_return h.1 h.2),
   fun h => five_distinct.2.2.2.2.2.2.2.1 (side_unique B1_return h.1 h.2),
   fun h => five_distinct.2.2.2.2.2.2.2.2.1 (side_unique B2_return h.1 h.2),
   fun h => five_distinct.2.2.2.2.2.2.2.2.2 (side_unique B2_return h.1 h.2)⟩

set_option exponentiation.threshold 200000 in
/-- **Exactly five left sides through wheel 165,749.** Every configuration with a leftmost black cell is on one of the five
strips; the five rows are finite and realize them; and no time shift relates two of them. -/
theorem exactly_five_left_sides :
    (∀ {{x : Int → Bool}} {{lo : Int}}, (∀ p, p < lo → x p = false) → x lo = true →
      ∃ s, Aligned K (Ld x lo) A0 s 165749 ∨ Aligned K (Ld x lo) A1 s 165749 ∨ Aligned K (Ld x lo) B0 s 165749 ∨
        Aligned K (Ld x lo) B1 s 165749 ∨ Aligned K (Ld x lo) B2 s 165749) ∧
    (A0 < 2 ^ K ∧ A1 < 2 ^ K ∧ B0 < 2 ^ K ∧ B1 < 2 ^ K ∧ B2 < 2 ^ K ∧
      A0.testBit 0 = true ∧ A1.testBit 0 = true ∧ B0.testBit 0 = true ∧ B1.testBit 0 = true ∧ B2.testBit 0 = true) ∧
    (∀ v, Aligned K (Ld (ofRow v) 0) v 0 165749) ∧
    (¬ Related K 165749 A0 A1 ∧ ¬ Related K 165749 A0 B0 ∧ ¬ Related K 165749 A0 B1 ∧ ¬ Related K 165749 A0 B2 ∧
      ¬ Related K 165749 A1 B0 ∧ ¬ Related K 165749 A1 B1 ∧ ¬ Related K 165749 A1 B2 ∧ ¬ Related K 165749 B0 B1 ∧
      ¬ Related K 165749 B0 B2 ∧ ¬ Related K 165749 B1 B2) :=
  ⟨fun hl h0 => left_side_classification hl h0, rows_finite, five_realized, five_distinct⟩

/-! ### The same theorem as arithmetic -/

theorem aligned_uniform {{a : Nat → Nat → Bool}} {{u s : Nat}} : ∀ J, Aligned K a u s J →
    ∃ T, ∀ j, j ≤ J → ∀ t, T ≤ t → a j (t + s) = Sp K u j t := by
  intro J
  induction J with
  | zero =>
    intro h
    obtain ⟨T, hT⟩ := h 0 (Nat.le_refl _)
    exact ⟨T, fun j hj t ht => by
      have e : j = 0 := by omega
      subst e
      exact hT t ht⟩
  | succ J ih =>
    intro h
    obtain ⟨T1, h1⟩ := ih (fun j hj => h j (by omega))
    obtain ⟨T2, h2⟩ := h (J + 1) (Nat.le_refl _)
    refine ⟨max T1 T2, fun j hj t ht => ?_⟩
    by_cases hc : j ≤ J
    · exact h1 j hc t (by omega)
    · have e : j = J + 1 := by omega
      subst e
      exact h2 t (by omega)

set_option exponentiation.threshold 200000 in
theorem rowAt_succ_lt (v n : Nat) : rowAt K v (n + 1) < 2 ^ K := by
  simp only [rowAt, Rule30UniversalLeftSide.stepK]
  exact Nat.mod_lt _ (Nat.pow_pos (by omega))

set_option exponentiation.threshold 200000 in
theorem eq_of_low_bits {{x y : Nat}} (hx : x < 2 ^ K) (hy : y < 2 ^ K)
    (h : ∀ j, j < K → x.testBit j = y.testBit j) : x = y := by
  apply Nat.eq_of_testBit_eq
  intro j
  by_cases hj : j < K
  · exact h j hj
  · have hp : 2 ^ K ≤ 2 ^ j := Nat.pow_le_pow_right (by omega) (by omega)
    rw [Nat.testBit_lt_two_pow (Nat.lt_of_lt_of_le hx hp), Nat.testBit_lt_two_pow (Nat.lt_of_lt_of_le hy hp)]

set_option exponentiation.threshold 200000 in
/-- If a row's strip is aligned with `u`'s, the row reaches the number `u`. -/
theorem reaches {{v u s : Nat}} (hu : rowAt K u 32 = u) (hlt : u < 2 ^ K)
    (h : Aligned K (Ld (ofRow v) 0) u s 165749) : ∃ n, rowAt K v n = u := by
  obtain ⟨T, hT⟩ := aligned_uniform 165749 h
  obtain ⟨n, hn⟩ : ∃ n, (T + 1) * 32 + s = n + 1 := ⟨(T + 1) * 32 + s - 1, by omega⟩
  refine ⟨n + 1, eq_of_low_bits (rowAt_succ_lt v n) hlt fun j hj => ?_⟩
  have hj' : j < 165750 := hj
  have e := hT j (by omega) ((T + 1) * 32) (by omega)
  rw [hn, Ld_row v (by omega)] at e
  have base : rowAt K u (0 + (T + 1) * 32) = u := by
    rw [rowAt_add_mul hu]
    rfl
  rw [Nat.zero_add] at base
  simp only [Sp] at e
  rw [base] at e
  exact e

/-- **Every odd number reaches one of five.** Iterate `v ↦ 4 v ⊕ (2 v ∨ v)` modulo `2 ^ 165750` from any odd `v`: the orbit
reaches `A0`, `A1`, `B0`, `B1` or `B2`. -/
theorem odd_reaches_one_of_five (v : Nat) (hv : v.testBit 0 = true) :
    ∃ n, rowAt K v n = A0 ∨ rowAt K v n = A1 ∨ rowAt K v n = B0 ∨ rowAt K v n = B1 ∨ rowAt K v n = B2 := by
  have h0 : ofRow v 0 = true := by simpa [ofRow] using hv
  obtain ⟨s, h⟩ := left_side_classification (ofRow_left v) h0
  rcases h with h | h | h | h | h
  · obtain ⟨n, e⟩ := reaches A0_return rows_finite.1 h
    exact ⟨n, Or.inl e⟩
  · obtain ⟨n, e⟩ := reaches A1_return rows_finite.2.1 h
    exact ⟨n, Or.inr (Or.inl e)⟩
  · obtain ⟨n, e⟩ := reaches B0_return rows_finite.2.2.1 h
    exact ⟨n, Or.inr (Or.inr (Or.inl e))⟩
  · obtain ⟨n, e⟩ := reaches B1_return rows_finite.2.2.2.1 h
    exact ⟨n, Or.inr (Or.inr (Or.inr (Or.inl e)))⟩
  · obtain ⟨n, e⟩ := reaches B2_return rows_finite.2.2.2.2.1 h
    exact ⟨n, Or.inr (Or.inr (Or.inr (Or.inr e)))⟩

/-- `A0` has least period exactly 32; the other four have least period exactly 16. -/
theorem least_periods : (∀ d, d < 32 → d ≠ 0 → rowAt K A0 d ≠ A0) ∧ ∀ d, d < 16 → d ≠ 0 →
    rowAt K A1 d ≠ A1 ∧ rowAt K B0 d ≠ B0 ∧ rowAt K B1 d ≠ B1 ∧ rowAt K B2 d ≠ B2 := by
  decide +kernel

end Ruliology.CellularAutomata.Rule30FiveFronts
''')
open(sys.argv[1], 'w').write("".join(L))
print("module written:", sys.argv[1], f"({time.time()-t0:.1f} s)")
