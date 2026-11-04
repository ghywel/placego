import TwoPairsEntrances

/-! Packed GC2673 witnesses for loss of the expected +3 wall position. The
source row is explicitly anchored and alternates above the encoded window.
The finite calculation scans the inverse from its actual left boundary. -/
namespace TwoPairs.WindowExclusions
open Entrances

def retained : List Nat := [1554, 1556, 1557, 1571, 1578, 1580, 1581, 1594, 1596, 1597, 1682, 1684, 1685, 1699, 1706, 1708, 1709, 1722, 1724, 1725, 1890, 1892, 1893, 1899]

/-- The first ten bits are free. Bit 10 repeats bit 9. -/
def word (i : Nat) : Nat := i + 2 * (i &&& 512)

private def options : Array (Nat × Nat) := #[(0, 0), (1, 3), (1, 5), (1, 7), (2, 1), (2, 5), (2, 9), (2, 19), (2, 21), (2, 25), (2, 27), (3, 11), (3, 59), (3, 63), (3, 69), (3, 71), (3, 79), (3, 93), (3, 111), (3, 125), (3, 127)]
private def selectors : Nat := 0x18c620cc4318c6318c631884318c6310c6318c620c44318c628ca5263e3210c627b651189cd0c84318c6318c6318c6318c6318c6318c6318c6318c6318c6318c6318c6318c6318c6318c6318c6318c631884318c6310c6318c6210c6205270188000804318c6318c6318c6318c6318c6318c6318c6318c6310c6318c6218a700b44318c6318c6318c6318c6318c620c84318c6318c631884318c6310c6318c620a44318c6249dcd2c8e910c624a529189060a44318c620b44318c6318c631884318c6310c6318c6249c00280e93a529411276b800582138ca5203dae2cce94a4a494400781cd3a52794a3249dae2350a10c624a5271890a0a4431884318c6310c6318c6249d462a9293a5294a52949d46229273a5294a4e9188000804310c6318c6249c002010a3a529011460a44318c6249c002010a10c624a4e9189460a84318c6318c6318c6318c6318c6318c6318c6318c6318c6318c6318c6318c6318c6318c6318c6318c6318c6318c6318c6318c6318c6318c6318c6318c6318c6318c6318c6318c6318c6318c6318c6318c6318c6318c6318c6318c6318c6318c6318c6318c6318c6318c6318c6318c6318c6318c6318c6318c6318c6318c6318c6318c6318c6318c6318c6318c6318c6318c6318c6318c6318c6318c6318c6318c6318c6318c6318c6318c6318c6318c6318c6318c6318c6318c6318c6318c6318c6318c6318c6318c6318c6318c6318c6318c6318c6318c6318c6318c6318c6318c6318c6318c6318c6318c6318c6318c6318c6318c6318c6318c6318c6318c6318c6318c6318c6318c6318c6318c6318c6318c6318c6318c6318c6318c6318c6318c6318c6318c6318c6318c6318c6318c6318c6318c6318c6318c6318c6318c63

private def witness (i : Nat) : Nat × Nat :=
  options[(selectors >>> (5*i)) &&& 31]!

/-- Extend bit 10 by alternation above the given eleven-bit source word. -/
def source (w low L j : Nat) : Bool :=
  if j < L then low.testBit j else if j < L+10 then w.testBit (j-L)
  else if (j-(L+10)) % 2 = 0 then w.testBit 10 else !(w.testBit 10)

private theorem source_alt (w low L j : Nat) (hj : L+10 ≤ j) :
    source w low L (j+1) = !source w low L j := by
  by_cases a : (j-(L+10)) % 2 = 0
  · simp [source, show ¬j < L by omega, show ¬j+1 < L by omega,
      show ¬j < L+10 by omega, show ¬j+1 < L+10 by omega, a] <;> omega
  · simp [source, show ¬j < L by omega, show ¬j+1 < L by omega,
      show ¬j < L+10 by omega, show ¬j+1 < L+10 by omega, a] <;> omega

def previousN (x : Row) : Nat → Row
  | 0 => x
  | r+1 => previousN (previous x) r

private def scan (w : List Bool) : Nat → List Bool
  | 0 => w
  | r+1 => scan (back false false w) r

private theorem prefix_back (x : Row) (n : Nat) :
    seg (previous x) 0 n = back false false (seg x 0 n) := by
  cases n with
  | zero => rfl
  | succ n =>
    cases n with
    | zero => simp [seg, back, previous]
    | succ n =>
      have h := back_seg (step_previous x) n 2 (by decide)
      simp only [show 2-1=1 by decide, show 2-2=0 by decide, previous] at h
      change x 0 :: xor (x 1) (x 0) :: seg (previous x) 2 n =
        xor (x 0) (false || false) ::
        xor (x 1) (xor (x 0) (false || false) || false) ::
        back (xor (x 1) (xor (x 0) (false || false) || false))
          (xor (x 0) (false || false)) (seg x 2 n)
      simpa only [Bool.or_false, Bool.xor_false, List.cons.injEq, true_and] using
        congrArg (fun tail => x 0 :: xor (x 1) (x 0) :: tail) h

private theorem prefix_scan (x : Row) (n r : Nat) :
    scan (seg x 0 n) r = seg (previousN x r) 0 n := by
  induction r generalizing x with
  | zero => rfl
  | succ r ih =>
    change scan (back false false (seg x 0 n)) r = seg (previousN (previous x) r) 0 n
    rw [← prefix_back, ih]

private def bits (w : Nat) : List Bool := (List.range 11).map (fun j => w.testBit j)

private abbrev Sample (w low L r : Nat) : Prop :=
  let x := source w low L
  let d := L+9+3*r
  let z := scan (seg x 0 (d+2)) r
  1 ≤ r ∧ r ≤ 3 ∧ x 0 = true ∧ seg x L 11 = bits w ∧
  x (L+10) = x (L+9) ∧ z.getD d false ≠ z.getD (d+1) false

private def checkOne (i : Nat) : Bool :=
  let (r, low) := witness i
  if word i ∈ retained then true else decide (Sample (word i) low (2*r+1) r)

set_option maxRecDepth 8192 in
set_option maxHeartbeats 1200000 in
private theorem checked : (List.range 1024).all checkOne = true := by decide +kernel

/-- Every other ten-bit index specifies a physical anchored row with the
given eleven-bit equal-top word, whose actual inverse misses the expected
top after one, two, or three steps. -/
theorem physical_exclusion (i : Fin 1024) (outside : word i.val ∉ retained) :
    ∃ (x : Row) (L r : Nat), 1 ≤ r ∧ r ≤ 3 ∧ x 0 = true ∧
      seg x L 11 = (List.range 11).map (fun j => (word i.val).testBit j) ∧
      Top x (L+9) ∧ ¬Top (previousN x r) (L+9+3*r) := by
  obtain ⟨r, low, hw⟩ : ∃ r low, witness i.val = (r,low) :=
    ⟨(witness i.val).1, (witness i.val).2, rfl⟩
  let L := 2*r+1
  let x := source (word i.val) low L
  let d := L+9+3*r
  have h := List.all_eq_true.mp checked i.val (List.mem_range.mpr i.isLt)
  have sample : Sample (word i.val) low L r := by
    apply of_decide_eq_true
    simpa only [checkOne, hw, if_neg outside, L] using h
  obtain ⟨rlo, rhi, anchor, window, wall, fail⟩ := sample
  refine ⟨x, L, r, rlo, rhi, anchor, window, ⟨wall, source_alt _ _ _⟩, ?_⟩
  change (scan (seg x 0 (d+2)) r).getD d false ≠
    (scan (seg x 0 (d+2)) r).getD (d+1) false at fail
  rw [prefix_scan, seg_getD _ _ 0 d (by omega), seg_getD _ _ 0 (d+1) (by omega)] at fail
  simp only [Nat.zero_add] at fail
  exact fun bad => fail bad.1.symm

#print axioms physical_exclusion
end TwoPairs.WindowExclusions
