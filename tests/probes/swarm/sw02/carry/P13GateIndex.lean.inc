/- The base clauses are ordered by transition time, column, gate clause, then period column. -/
private def stripBase : List (List Nat) :=
  transitionFormula 13 65 ++ periodFormula 13 65 65

private def gateClauses (i : Nat) : List (List Nat) :=
  let t := i / 378
  let j := i / 6 % 63
  sixClauses (vid 65 t j) (vid 65 t (j + 1)) (vid 65 t (j + 2)) (vid 65 (t + 1) j)

private def selectBase (i : Nat) : List Nat :=
  if i < 4914 then ((gateClauses i)[i % 6]?).getD []
  else
    let j := (i - 4914) / 2
    if (i - 4914) % 2 = 0 then [mkLit (vid 65 13 j) false, mkLit (vid 65 0 j) true]
    else [mkLit (vid 65 13 j) true, mkLit (vid 65 0 j) false]

private theorem selectBase_mem {i : Nat} (hi : i < 5044) : selectBase i ∈ stripBase := by
  apply List.mem_append.mpr
  by_cases ht : i < 4914
  · left
    apply List.mem_flatMap.mpr
    refine ⟨i / 378, List.mem_range.mpr (by omega), ?_⟩
    apply List.mem_flatMap.mpr
    refine ⟨i / 6 % 63, List.mem_range.mpr (by omega), ?_⟩
    change selectBase i ∈ gateClauses i
    rw [selectBase, ite_eq_left ht]
    have hk : i % 6 < (gateClauses i).length := by
      change i % 6 < 6
      omega
    apply List.mem_of_getElem? (i := i % 6)
    rw [getElem?_pos (gateClauses i) (i % 6) hk, Option.getD_some]
  · right
    apply List.mem_flatMap.mpr
    refine ⟨(i - 4914) / 2, List.mem_range.mpr (by omega), ?_⟩
    rw [selectBase, ite_eq_right ht]
    dsimp only
    split <;> simp
