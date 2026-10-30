module
public import Rule30Submission

/-! Expected-rejection control, GC2295. This is deliberately ill-typed.
Run only AFTER the exact assembled source and all positive controls pass.
An import failure is not the intended rejection; require the type mismatch
at the following declaration. Never include this file in the submission. -/
@[expose] public section
namespace FinitePastExpectedRejection

theorem deliberately_false : False := by
  exact Rule30Submission.finite_parent_small_widths

end FinitePastExpectedRejection
