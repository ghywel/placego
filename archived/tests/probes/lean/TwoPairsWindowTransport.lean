import TwoPairs

/-!
# Forward transport of finite right-edge windows

All words are in increasing spatial index. One forward step consumes the
first two cells as context. After r steps, exactly the first 2r cells serve
as context. Fixing those cells makes the transport injective. This retains
the shared shallow history across ticks when checking inverse-front words.
-/

namespace TwoPairs.WindowTransport

/-- Compute a forward word starting two cells above the input start. -/
def shrink : List Bool → List Bool
  | a :: b :: c :: rest => xor c (b || a) :: shrink (b :: c :: rest)
  | _ => []

def shrinkN (word : List Bool) : Nat → List Bool
  | 0 => word
  | r + 1 => shrinkN (shrink word) r

theorem shrink_seg (z : Row) (A w : Nat) :
    shrink (seg z A (w + 2)) = seg (step z) (A + 2) w := by
  induction w generalizing A with
  | zero => rfl
  | succ w ih =>
    change xor (z (A + 2)) (z (A + 1) || z A) :: shrink (seg z (A + 1) (w + 2)) =
      step z (A + 2) :: seg (step z) (A + 2 + 1) w
    rw [ih] <;> rfl

/-- Exact locality in the original spatial coordinate, for every tick and width. -/
theorem shrinkN_seg (z : Row) (A r w : Nat) :
    shrinkN (seg z A (2 * r + w)) r = seg (iter z r) (A + 2 * r) w := by
  induction r generalizing z A w with
  | zero => simp [shrinkN, iter]
  | succ r ih =>
    have length : 2 * (r + 1) + w = (2 * r + w) + 2 := by omega
    have pos : A + 2 + 2 * r = A + 2 * (r + 1) := by omega
    have time : iter (step z) r = iter z (r + 1) := by
      rw [Nat.add_comm r 1, iter_add z 1 r] <;> rfl
    rw [shrinkN, length, shrink_seg, ih, pos, time]

/-- Inverse transport once the two lower input cells are specified. -/
private theorem back_shrink (a b : Bool) (tail : List Bool) :
    back b a (shrink (a :: b :: tail)) = tail := by
  induction tail generalizing a b with
  | nil => rfl
  | cons c tail ih =>
    let d := xor c (b || a)
    have recover : xor d (b || a) = c := by
      cases a <;> cases b <;> cases c <;> rfl
    change xor d (b || a) :: back (xor d (b || a)) b (shrink (b :: c :: tail)) = c :: tail
    rw [recover, ih]

private def restore (initial image : List Bool) : List Bool :=
  match initial with
  | [a, b] => a :: b :: back b a image
  | _ => initial

private theorem restore_shrink (word : List Bool) :
    restore (word.take 2) (shrink word) = word := by
  cases word with
  | nil => rfl
  | cons a tail =>
    cases tail with
    | nil => rfl
    | cons b rest =>
      change a :: b :: back b a (shrink (a :: b :: rest)) = a :: b :: rest
      rw [back_shrink]

theorem shrink_take (word : List Bool) (n : Nat) :
    shrink (word.take (n + 2)) = (shrink word).take n := by
  induction n generalizing word with
  | zero =>
    cases word with
    | nil => rfl
    | cons a tail => cases tail <;> rfl
  | succ n ih =>
    cases word with
    | nil => rfl
    | cons a tail =>
      cases tail with
      | nil => rfl
      | cons b rest =>
        cases rest with
        | nil => rfl
        | cons c more =>
          change xor c (b || a) :: shrink ((b :: c :: more).take (n + 2)) =
            xor c (b || a) :: (shrink (b :: c :: more)).take n
          rw [ih]

/-- For fixed 2r lower input bits, the r-tick image determines the entire input. -/
theorem shrinkN_injective {u v : List Bool} (r : Nat)
    (hp : u.take (2 * r) = v.take (2 * r)) (hout : shrinkN u r = shrinkN v r) :
    u = v := by
  induction r generalizing u v with
  | zero => exact hout
  | succ r ih =>
    have h2 := congrArg (fun w : List Bool => w.take 2) hp
    have b : min 2 (2 * (r + 1)) = 2 := by omega
    change (u.take (2 * (r + 1))).take 2 = (v.take (2 * (r + 1))).take 2 at h2
    simp only [List.take_take, b] at h2
    have p := congrArg shrink hp
    have width : 2 * (r + 1) = 2 * r + 2 := by omega
    rw [width, shrink_take, shrink_take] at p
    have hstep : shrink u = shrink v := ih p hout
    calc
      u = restore (u.take 2) (shrink u) := (restore_shrink u).symm
      _ = restore (v.take 2) (shrink v) := by rw [h2, hstep]
      _ = v := restore_shrink v

end TwoPairs.WindowTransport
