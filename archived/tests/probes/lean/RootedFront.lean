module
public import EtherZeroCert.EtherEdgeZero

/-!
# A rooted-front observer: the inserted edge's right tail matters only beyond 87

Local, 3 November 2026 (L1362–L1366); GPT carried the observer's soundness by hand (GC2434). Core Lean, standard axioms.

Let `E` and `H` be rule-30 evolutions of the whole line and `δ = H xor E` their difference. With `E`'s values as
coefficients, `δ` obeys an exact one-cell identity (`dif_succ`, `mis`). The **rooted observer** follows the leftmost
difference `L` of `δ` with a three-valued window of two cells to its right (`St`, `HoldsR`), and *half-line* states
`δ = 0` on `x ≤ m` (`HoldsH`) evolve by A2's recruitment step (`succH`). One tick (`tick`) evaluates the new cells
three-valued (`tv`), branches until the new front is found (`succR`), expands the least half-line state into rooted states
up to a threshold `k`, converts rooted states with `L - 1 ≥ k` back to half-line states, and deduplicates. The thresholds
are untrusted data: soundness holds for every choice (`tick_sound`). The background rows are bit masks (`stepN`,
`rows_spec`), so the kernel runs the check (`check`, `decide +kernel`).

* `check_sound`: a passing check gives agreement `H T x = E T x` for every `x ≤ Q` and every `H` agreeing with `E` at time
  `0` on `x ≤ b`, whatever its right tail.
* `tail87_c0_c1`: for each of A1's 28 entries, cut `b = 87` gives agreement on the entry window at the entry time.
* `edge_pinned_tail87`: A1's `edge_pinned_tail` with `87` in place of `198`. The single flip at `87` shows that `86` does
  not give the entry at `(4, 3)` (computed, T53; not in this file), so `87` is the least common cutoff for these entries.

Prior art: A2's recruitment frontier (the three-valued observer with an unknown right half-line) and its backward
thresholds (GPT, GC2423) are the special case without a rooted front; the ether, the wall states and the trap are the
kit's `Rule30Ether`.
-/
@[expose] public section
namespace Ruliology.CellularAutomata.RootedFront
open Rule30Jen Rule30StripCertificates Rule30Ether Ruliology.CellularAutomata.EtherEdgeZero

/-! ### The mismatch identity -/

/-- One cell's difference after a tick, from its parents' differences `dl dc dr` and the background's centre `c` and
right neighbour `r`. -/
def mis (dl dc dr c r : Bool) : Bool := xor dl (xor (!r && dc) (xor (!c && dr) (dc && dr)))

theorem mis_rule : ∀ h1 h2 h3 e1 e2 e3 : Bool,
    xor (rule h1 h2 h3) (rule e1 e2 e3) = mis (xor h1 e1) (xor h2 e2) (xor h3 e3) e2 e3 := by decide

theorem mis_zero (c r : Bool) : mis false false false c r = false := by cases c <;> cases r <;> rfl

/-- The difference of two whole-line evolutions. -/
def dif (H E : Nat → Int → Bool) (t : Nat) (x : Int) : Bool := xor (H t x) (E t x)

theorem dif_succ {H E : Nat → Int → Bool} (hH : IsR30Z H) (hE : IsR30Z E) (t : Nat) (x : Int) :
    dif H E (t + 1) x = mis (dif H E t (x - 1)) (dif H E t x) (dif H E t (x + 1)) (E t x) (E t (x + 1)) := by
  unfold dif; rw [hH, hE]; exact mis_rule _ _ _ _ _ _

/-! ### Three-valued cells -/

def opts : Option Bool → List Bool
  | none => [false, true]
  | some v => [v]

/-- `tm o v`: the value `v` is consistent with the three-valued `o` (`none` is unknown). -/
def tm : Option Bool → Bool → Bool
  | none, _ => true
  | some v, w => v == w

/-- The three-valued value of `mis` over every completion of the unknown parents. -/
def tv (dl dc dr : Option Bool) (c r : Bool) : Option Bool :=
  let vs := (opts dl).flatMap fun a => (opts dc).flatMap fun b => (opts dr).map fun d => mis a b d c r
  if vs.all (· == true) then some true else if vs.all (· == false) then some false else none

theorem opt_cases (o : Option Bool) : o = none ∨ o = some false ∨ o = some true := by
  cases o with
  | none => exact Or.inl rfl
  | some v => cases v <;> simp

theorem tv_sound (dl dc dr : Option Bool) (c r a b d : Bool) (ha : tm dl a = true) (hb : tm dc b = true)
    (hd : tm dr d = true) : tm (tv dl dc dr c r) (mis a b d c r) = true := by
  rcases opt_cases dl with rfl | rfl | rfl <;> rcases opt_cases dc with rfl | rfl | rfl <;>
    rcases opt_cases dr with rfl | rfl | rfl <;> revert ha hb hd <;> revert a b d c r <;> decide

/-! ### Rooted and half-line states -/

structure St where
  L : Int
  a : Option Bool
  b : Option Bool
deriving DecidableEq

/-- The leftmost difference is at `s.L`, and the next two cells are consistent with `s.a`, `s.b`. -/
def HoldsR (δ : Int → Bool) (s : St) : Prop :=
  (∀ x, x < s.L → δ x = false) ∧ δ s.L = true ∧ tm s.a (δ (s.L + 1)) = true ∧ tm s.b (δ (s.L + 2)) = true

/-- No difference on `x ≤ m`. -/
def HoldsH (δ : Int → Bool) (m : Int) : Prop := ∀ x, x ≤ m → δ x = false

theorem HoldsH.mono {δ : Int → Bool} {m m' : Int} (h : HoldsH δ m) (hm : m' ≤ m) : HoldsH δ m' :=
  fun x hx => h x (by omega)

/-- `δ'` is the next difference over the background row `E`. -/
def StepRel (δ δ' E : Int → Bool) : Prop := ∀ x, δ' x = mis (δ (x - 1)) (δ x) (δ (x + 1)) (E x) (E (x + 1))

/-! ### One rooted state, one tick -/

/-- The successors from the new cells at `L - 1` (exact: `b0`) and `L, L + 1, L + 2` (three-valued: `o1 o2 o3`). -/
def succRaw (L : Int) (b0 : Bool) (o1 o2 o3 : Option Bool) : List St × Option Int :=
  if b0 then ([⟨L - 1, o1, o2⟩], none) else
  let r1 : List St := if o1 = some false then [] else [⟨L, o2, o3⟩]
  if o1 = some true then (r1, none) else
  let r2 : List St := if o2 = some false then [] else [⟨L + 1, o3, none⟩]
  if o2 = some true then (r1 ++ r2, none) else
  let r3 : List St := if o3 = some false then [] else [⟨L + 2, none, none⟩]
  if o3 = some true then (r1 ++ r2 ++ r3, none) else (r1 ++ r2 ++ r3, some (L + 2))

theorem succRaw_sound (L : Int) (b0 : Bool) (o1 o2 o3 : Option Bool) (v1 v2 v3 : Bool)
    (h1 : tm o1 v1 = true) (h2 : tm o2 v2 = true) (h3 : tm o3 v3 = true) :
    (b0 = true → ⟨L - 1, o1, o2⟩ ∈ (succRaw L b0 o1 o2 o3).1) ∧
    (b0 = false → v1 = true → ⟨L, o2, o3⟩ ∈ (succRaw L b0 o1 o2 o3).1) ∧
    (b0 = false → v1 = false → v2 = true → ⟨L + 1, o3, none⟩ ∈ (succRaw L b0 o1 o2 o3).1) ∧
    (b0 = false → v1 = false → v2 = false → v3 = true → ⟨L + 2, none, none⟩ ∈ (succRaw L b0 o1 o2 o3).1) ∧
    (b0 = false → v1 = false → v2 = false → v3 = false → (succRaw L b0 o1 o2 o3).2 = some (L + 2)) := by
  rcases opt_cases o1 with rfl | rfl | rfl <;> rcases opt_cases o2 with rfl | rfl | rfl <;>
    rcases opt_cases o3 with rfl | rfl | rfl <;> cases b0 <;> cases v1 <;> cases v2 <;> cases v3 <;>
    simp_all [succRaw, tm]

/-- The successors of a rooted state over the background row `e`. -/
def succR (e : Int → Bool) (s : St) : List St × Option Int :=
  succRaw s.L (!e (s.L - 1)) (tv (some false) (some true) s.a (e s.L) (e (s.L + 1)))
    (tv (some true) s.a s.b (e (s.L + 1)) (e (s.L + 2))) (tv s.a s.b none (e (s.L + 2)) (e (s.L + 3)))

theorem succR_sound {δ δ' e E : Int → Bool} {s : St} (hs : StepRel δ δ' E) (he : ∀ x, s.L - 1 ≤ x → e x = E x)
    (h : HoldsR δ s) : (∃ s' ∈ (succR e s).1, HoldsR δ' s') ∨ (∃ m, (succR e s).2 = some m ∧ HoldsH δ' m) := by
  obtain ⟨hlt, hL, ha, hb⟩ := h
  have z : ∀ x, x < s.L - 1 → δ' x = false := by
    intro x hx
    rw [hs, hlt _ (by omega), hlt _ (by omega), hlt _ (by omega), mis_zero]
  have d0 : δ' (s.L - 1) = !e (s.L - 1) := by
    rw [hs, hlt _ (by omega), hlt _ (by omega), show s.L - 1 + 1 = s.L by omega, hL, he _ (by omega)]
    cases E (s.L - 1) <;> cases E s.L <;> rfl
  have d1 : tm (tv (some false) (some true) s.a (e s.L) (e (s.L + 1))) (δ' s.L) = true := by
    rw [hs, he _ (by omega), he _ (by omega)]
    exact tv_sound _ _ _ _ _ _ _ _ (by rw [hlt _ (by omega)]; rfl) (by rw [hL]; rfl) ha
  have d2 : tm (tv (some true) s.a s.b (e (s.L + 1)) (e (s.L + 2))) (δ' (s.L + 1)) = true := by
    rw [hs, he _ (by omega), he _ (by omega), show s.L + 1 - 1 = s.L by omega, show s.L + 1 + 1 = s.L + 2 by omega]
    exact tv_sound _ _ _ _ _ _ _ _ (by rw [hL]; rfl) ha hb
  have d3 : tm (tv s.a s.b none (e (s.L + 2)) (e (s.L + 3))) (δ' (s.L + 2)) = true := by
    rw [hs, he _ (by omega), he _ (by omega), show s.L + 2 - 1 = s.L + 1 by omega, show s.L + 2 + 1 = s.L + 3 by omega]
    exact tv_sound _ _ _ _ _ _ _ _ ha hb rfl
  obtain ⟨c0, c1, c2, c3, c4⟩ := succRaw_sound s.L (!e (s.L - 1)) _ _ _ _ _ _ d1 d2 d3
  unfold succR
  cases h0 : δ' (s.L - 1) with
  | true =>
    rw [d0] at h0
    refine Or.inl ⟨_, c0 h0, fun x hx => z x hx, by rw [d0]; exact h0, ?_, ?_⟩
    · rw [show s.L - 1 + 1 = s.L by omega]; exact d1
    · rw [show s.L - 1 + 2 = s.L + 1 by omega]; exact d2
  | false =>
    rw [d0] at h0
    have lt1 : ∀ x, x < s.L → δ' x = false := fun x hx => by
      rcases (by omega : x < s.L - 1 ∨ x = s.L - 1) with h | h
      · exact z x h
      · rw [h, d0, h0]
    cases h1 : δ' s.L with
    | true => exact Or.inl ⟨_, c1 h0 h1, lt1, h1, d2, d3⟩
    | false =>
      have lt2 : ∀ x, x < s.L + 1 → δ' x = false := fun x hx => by
        rcases (by omega : x < s.L ∨ x = s.L) with h | h
        · exact lt1 x h
        · rw [h, h1]
      cases h2 : δ' (s.L + 1) with
      | true =>
        refine Or.inl ⟨_, c2 h0 h1 h2, lt2, h2, ?_, rfl⟩
        rw [show s.L + 1 + 1 = s.L + 2 by omega]; exact d3
      | false =>
        have lt3 : ∀ x, x < s.L + 2 → δ' x = false := fun x hx => by
          rcases (by omega : x < s.L + 1 ∨ x = s.L + 1) with h | h
          · exact lt2 x h
          · rw [h, h2]
        cases h3 : δ' (s.L + 2) with
        | true => exact Or.inl ⟨_, c3 h0 h1 h2 h3, lt3, h3, rfl, rfl⟩
        | false =>
          refine Or.inr ⟨_, c4 h0 h1 h2 h3, fun x hx => ?_⟩
          rcases (by omega : x < s.L + 2 ∨ x = s.L + 2) with h | h
          · exact lt3 x h
          · rw [h, h3]

/-! ### Half-line states -/

/-- A2's recruitment step for a half-line state. -/
def succH (e : Int → Bool) (m : Int) : Int := if e m then m else m - 1

theorem succH_sound {δ δ' e E : Int → Bool} {m : Int} (hs : StepRel δ δ' E) (he : e m = E m) (h : HoldsH δ m) :
    HoldsH δ' (succH e m) := by
  intro x hx
  unfold succH at hx
  rw [hs]
  by_cases hxm : x ≤ m - 1
  · rw [h _ (by omega), h _ (by omega), h _ (by omega), mis_zero]
  · have hm : e m = true := by
      cases hc : e m with
      | true => rfl
      | false => rw [hc] at hx; simp at hx; omega
    rw [hm] at hx; simp at hx
    have hxe : x = m := by omega
    rw [hxe, h _ (by omega), h _ (by omega), ← he, hm]
    cases δ (m + 1) <;> cases E (m + 1) <;> rfl

/-- Rooted states `m + 1, …, m + n` with unknown windows. -/
def expand (m : Int) : Nat → List St
  | 0 => []
  | n + 1 => ⟨m + 1, none, none⟩ :: expand (m + 1) n

theorem expand_sound (δ : Int → Bool) : ∀ (n : Nat) (m : Int), HoldsH δ m →
    (∃ s ∈ expand m n, HoldsR δ s) ∨ HoldsH δ (m + n) := by
  intro n
  induction n with
  | zero => intro m h; right; simpa using h
  | succ n ih =>
    intro m h
    cases hm : δ (m + 1) with
    | true => exact Or.inl ⟨_, List.mem_cons_self .., fun x (hx : x < m + 1) => h x (by omega), hm, rfl, rfl⟩
    | false =>
      have h' : HoldsH δ (m + 1) := fun x hx => by
        rcases (by omega : x ≤ m ∨ x = m + 1) with hx | hx
        · exact h x hx
        · rw [hx, hm]
      rcases ih (m + 1) h' with ⟨s, hs, hR⟩ | hH
      · exact Or.inl ⟨s, List.mem_cons_of_mem _ hs, hR⟩
      · right; refine hH.mono ?_; push_cast; omega

/-- The least element of a list. -/
def minOpt : List Int → Option Int
  | [] => none
  | x :: xs => some (match minOpt xs with | none => x | some y => min x y)

theorem minOpt_le : ∀ (l : List Int) (m : Int), m ∈ l → ∃ m', minOpt l = some m' ∧ m' ≤ m := by
  intro l
  induction l with
  | nil => intro m h; simp at h
  | cons x xs ih =>
    intro m h
    simp only [minOpt]
    rcases List.mem_cons.1 h with rfl | h
    · cases minOpt xs with
      | none => exact ⟨_, rfl, Int.le_refl _⟩
      | some y => exact ⟨_, rfl, Int.min_le_left _ _⟩
    · obtain ⟨m', hm', hle⟩ := ih m h
      rw [hm']
      exact ⟨min x m', rfl, Int.le_trans (Int.min_le_right _ _) hle⟩

/-! ### Deduplication by a bit mask -/

def zig (L : Int) : Nat := if 0 ≤ L then 2 * L.toNat else 2 * (-L).toNat - 1

def code : Option Bool → Nat
  | none => 0
  | some false => 1
  | some true => 2

def key (s : St) : Nat := zig s.L * 9 + 3 * code s.a + code s.b

theorem code_lt (o : Option Bool) : code o < 3 := by rcases opt_cases o with rfl | rfl | rfl <;> decide

theorem code_inj {o o' : Option Bool} (h : code o = code o') : o = o' := by
  rcases opt_cases o with rfl | rfl | rfl <;> rcases opt_cases o' with rfl | rfl | rfl <;> simp_all [code]

theorem zig_inj {L L' : Int} (h : zig L = zig L') : L = L' := by
  unfold zig at h
  split at h <;> split at h <;> omega

theorem key_inj {s s' : St} (h : key s = key s') : s = s' := by
  unfold key at h
  have ha := code_lt s.a; have hb := code_lt s.b; have ha' := code_lt s'.a; have hb' := code_lt s'.b
  have hz : zig s.L = zig s'.L := by omega
  have hca : code s.a = code s'.a := by omega
  have hcb : code s.b = code s'.b := by omega
  cases s; cases s'
  simp only [St.mk.injEq]
  exact ⟨zig_inj hz, code_inj hca, code_inj hcb⟩

def dedupAux : List St → Nat → List St → List St
  | [], _, acc => acc
  | s :: l, seen, acc => if seen.testBit (key s) then dedupAux l seen acc else dedupAux l (seen ||| 2 ^ key s) (s :: acc)

def dedup (l : List St) : List St := dedupAux l 0 []

theorem dedupAux_mem : ∀ (l : List St) (seen : Nat) (acc : List St),
    (∀ j, seen.testBit j = true → ∃ s' ∈ acc, key s' = j) → ∀ s, s ∈ l ∨ s ∈ acc → s ∈ dedupAux l seen acc := by
  intro l
  induction l with
  | nil => intro seen acc _ s hs; simpa [dedupAux] using hs
  | cons x l ih =>
    intro seen acc hinv s hs
    simp only [dedupAux]
    split
    · next hx =>
      obtain ⟨s', hs', hk⟩ := hinv _ hx
      have := key_inj hk
      subst this
      apply ih seen acc hinv
      rcases hs with hs | hs
      · rcases List.mem_cons.1 hs with rfl | hs
        · exact Or.inr hs'
        · exact Or.inl hs
      · exact Or.inr hs
    · apply ih
      · intro j hj
        rw [Nat.testBit_or, Nat.testBit_two_pow] at hj
        rcases Bool.or_eq_true_iff.1 hj with hj | hj
        · obtain ⟨s', hs', hk⟩ := hinv j hj
          exact ⟨s', List.mem_cons_of_mem _ hs', hk⟩
        · exact ⟨x, List.mem_cons_self .., by simpa using hj⟩
      · rcases hs with hs | hs
        · rcases List.mem_cons.1 hs with rfl | hs
          · exact Or.inr (List.mem_cons_self ..)
          · exact Or.inl hs
        · exact Or.inr (List.mem_cons_of_mem _ hs)

theorem dedup_mem {l : List St} {s : St} (h : s ∈ l) : s ∈ dedup l :=
  dedupAux_mem l 0 [] (fun j hj => by simp at hj) s (Or.inl h)

/-! ### A configuration and its tick -/

structure Cfg where
  R : List St
  H : Option Int

def Inv (δ : Int → Bool) (c : Cfg) : Prop := (∃ s ∈ c.R, HoldsR δ s) ∨ (∃ m, c.H = some m ∧ HoldsH δ m)

/-- One tick over the background row `e`, with the untrusted threshold `k` for the next time. -/
def tick (e : Int → Bool) (k : Int) (c : Cfg) : Cfg :=
  let outs := c.R.map (succR e)
  let R1 := outs.flatMap Prod.fst
  let hs := outs.filterMap Prod.snd ++ (c.H.map (succH e)).toList
  let R2 := match minOpt hs with
    | none => R1
    | some m => R1 ++ expand m (k - m).toNat
  let H2 : List Int := match minOpt hs with
    | none => []
    | some m => [m + ((k - m).toNat : Int)]
  let keep := R2.filter (fun s => decide (s.L - 1 < k))
  ⟨dedup keep, minOpt ((R2.filter (fun s => decide (k ≤ s.L - 1))).map (fun s => s.L - 1) ++ H2)⟩

/-- Conversion of rooted states with `L - 1 ≥ k` to half-line states, then deduplication. -/
theorem convert_sound {δ : Int → Bool} {k : Int} (R2 : List St) (H2 : List Int)
    (h : (∃ s ∈ R2, HoldsR δ s) ∨ (∃ m ∈ H2, HoldsH δ m)) :
    Inv δ ⟨dedup (R2.filter (fun s => decide (s.L - 1 < k))),
      minOpt ((R2.filter (fun s => decide (k ≤ s.L - 1))).map (fun s => s.L - 1) ++ H2)⟩ := by
  rcases h with ⟨s, hsR, hR⟩ | ⟨m, hm, hH⟩
  · by_cases hk : s.L - 1 < k
    · exact Or.inl ⟨s, dedup_mem (List.mem_filter.2 ⟨hsR, decide_eq_true hk⟩), hR⟩
    · have hmem : s.L - 1 ∈ (R2.filter (fun s => decide (k ≤ s.L - 1))).map (fun s => s.L - 1) ++ H2 :=
        List.mem_append_left _ (List.mem_map.2 ⟨s, List.mem_filter.2 ⟨hsR, decide_eq_true (by omega)⟩, rfl⟩)
      obtain ⟨m', hm', hle⟩ := minOpt_le _ _ hmem
      have hH1 : HoldsH δ (s.L - 1) := fun x hx => hR.1 x (by omega)
      exact Or.inr ⟨m', hm', hH1.mono hle⟩
  · obtain ⟨m', hm', hle⟩ := minOpt_le ((R2.filter (fun s => decide (k ≤ s.L - 1))).map (fun s => s.L - 1) ++ H2) m
      (List.mem_append_right _ hm)
    exact Or.inr ⟨m', hm', hH.mono hle⟩

theorem tick_sound {δ δ' e E : Int → Bool} {k : Int} {c : Cfg} (hs : StepRel δ δ' E)
    (heR : ∀ s ∈ c.R, ∀ x, s.L - 1 ≤ x → e x = E x) (heH : ∀ m, c.H = some m → e m = E m)
    (h : Inv δ c) : Inv δ' (tick e k c) := by
  -- after the successors: a rooted state of R1 or a half-line state of hs holds
  have step1 : (∃ s ∈ (c.R.map (succR e)).flatMap Prod.fst, HoldsR δ' s) ∨
      (∃ m ∈ (c.R.map (succR e)).filterMap Prod.snd ++ (c.H.map (succH e)).toList, HoldsH δ' m) := by
    rcases h with ⟨s, hsR, hR⟩ | ⟨m, hm, hH⟩
    · rcases succR_sound hs (heR s hsR) hR with ⟨s', hs', hR'⟩ | ⟨m, hm, hH'⟩
      · exact Or.inl ⟨s', List.mem_flatMap.2 ⟨_, List.mem_map.2 ⟨s, hsR, rfl⟩, hs'⟩, hR'⟩
      · exact Or.inr ⟨m, List.mem_append_left _ (List.mem_filterMap.2 ⟨_, List.mem_map.2 ⟨s, hsR, rfl⟩, hm⟩), hH'⟩
    · refine Or.inr ⟨succH e m, List.mem_append_right _ ?_, succH_sound hs (heH m hm) hH⟩
      rw [hm]; simp
  -- after expansion: a rooted state of R2 or the half-line state H2
  have step2 : ∀ (R1 : List St) (hl : List Int), ((∃ s ∈ R1, HoldsR δ' s) ∨ (∃ m ∈ hl, HoldsH δ' m)) →
      (∃ s ∈ (match minOpt hl with | none => R1 | some m => R1 ++ expand m (k - m).toNat), HoldsR δ' s) ∨
      (∃ m ∈ (match minOpt hl with | none => ([] : List Int) | some m => [m + ((k - m).toNat : Int)]), HoldsH δ' m) := by
    intro R1 hl h
    rcases h with ⟨s, hsR, hR⟩ | ⟨m, hm, hH⟩
    · left
      cases minOpt hl with
      | none => exact ⟨s, hsR, hR⟩
      | some m => exact ⟨s, List.mem_append_left _ hsR, hR⟩
    · obtain ⟨m', hm', hle⟩ := minOpt_le hl m hm
      rw [hm']
      rcases expand_sound δ' (k - m').toNat m' (hH.mono hle) with ⟨s, hs, hR⟩ | hH'
      · exact Or.inl ⟨s, List.mem_append_right _ hs, hR⟩
      · exact Or.inr ⟨_, List.mem_singleton_self _, hH'⟩
  exact convert_sound _ _ (step2 _ _ step1)

/-! ### Background rows as bit masks, and the run -/

def stepN (a : Nat) : Nat := (a <<< 1) ^^^ (a ||| (a >>> 1))

theorem stepN_bit (a i : Nat) (hi : 1 ≤ i) :
    (stepN a).testBit i = rule (a.testBit (i - 1)) (a.testBit i) (a.testBit (i + 1)) := by
  unfold stepN
  rw [Nat.testBit_xor, Nat.testBit_or, Nat.testBit_shiftLeft, Nat.testBit_shiftRight]
  simp [show i ≥ 1 from hi, show 1 + i = i + 1 by omega, rule]

/-- Row `t` of `E` as a bit mask: bit `i` is column `lo + i`, valid for `i ≥ t`. -/
theorem rows_spec {E : Nat → Int → Bool} (hE : IsR30Z E) (lo : Int) :
    ∀ (t : Nat) (row : Nat), (∀ i, t ≤ i → row.testBit i = E t (lo + i)) →
      ∀ i, t + 1 ≤ i → (stepN row).testBit i = E (t + 1) (lo + i) := by
  intro t row hrow i hi
  rw [stepN_bit _ _ (by omega), hrow _ (by omega), hrow _ (by omega), hrow _ (by omega), hE]
  rw [show lo + ((i - 1 : Nat) : Int) = lo + (i : Int) - 1 by omega,
    show lo + ((i + 1 : Nat) : Int) = lo + (i : Int) + 1 by omega]

/-- The background row at a column, from its bit mask. -/
def eOf (lo : Int) (row : Nat) (x : Int) : Bool := row.testBit (x - lo).toNat

theorem eOf_spec {lo : Int} {row : Nat} {t : Nat} {f : Int → Bool} (h : ∀ i, t ≤ i → row.testBit i = f (lo + i))
    (x : Int) (hx : lo + t ≤ x) : eOf lo row x = f x := by
  unfold eOf
  rw [h _ (by omega)]
  congr 1; omega

def guard (lo : Int) (t : Nat) (c : Cfg) : Bool :=
  c.R.all (fun s => decide (lo + t ≤ s.L - 1)) && c.H.all (fun m => decide (lo + t ≤ m))

/-- Run `n` ticks from time `t`; `none` if a guard fails. `ks` holds the thresholds for times `t + 1, …`. -/
def run (lo : Int) : Nat → Nat → Nat → List Int → Cfg → Option Cfg
  | 0, _, _, _, c => some c
  | n + 1, t, row, ks, c =>
    if guard lo t c then run lo n (t + 1) (stepN row) ks.tail (tick (eOf lo row) (ks.headD 0) c) else none

theorem run_sound {E H : Nat → Int → Bool} (hE : IsR30Z E) (hH : IsR30Z H) (lo : Int) :
    ∀ (n t row : Nat) (ks : List Int) (c c' : Cfg), (∀ i, t ≤ i → row.testBit i = E t (lo + i)) →
      Inv (dif H E t) c → run lo n t row ks c = some c' → Inv (dif H E (t + n)) c' := by
  intro n
  induction n with
  | zero => intro t row ks c c' _ h hr; simp [run] at hr; subst hr; simpa using h
  | succ n ih =>
    intro t row ks c c' hrow h hr
    simp only [run] at hr
    split at hr
    · next hg =>
      simp only [guard, Bool.and_eq_true, List.all_eq_true, decide_eq_true_eq, Option.all_eq_true] at hg
      have hs : StepRel (dif H E t) (dif H E (t + 1)) (E t) := fun x => dif_succ hH hE t x
      have heR : ∀ s ∈ c.R, ∀ x, s.L - 1 ≤ x → eOf lo row x = E t x :=
        fun s hs x hx => eOf_spec hrow x (by have := hg.1 s hs; omega)
      have heH : ∀ m, c.H = some m → eOf lo row m = E t m :=
        fun m hm => eOf_spec hrow m (hg.2 m hm)
      have := ih (t + 1) (stepN row) ks.tail _ c' (rows_spec hE lo t row hrow)
        (tick_sound hs heR heH h) hr
      rwa [show t + 1 + n = t + (n + 1) by omega] at this
    · simp at hr

def finalOK (Q : Int) (c : Cfg) : Bool := c.R.all (fun s => decide (Q < s.L)) && c.H.all (fun m => decide (Q ≤ m))

theorem final_sound {δ : Int → Bool} {c : Cfg} {Q : Int} (h : Inv δ c) (hf : finalOK Q c = true) :
    ∀ x, x ≤ Q → δ x = false := by
  simp only [finalOK, Bool.and_eq_true, List.all_eq_true, decide_eq_true_eq, Option.all_eq_true] at hf
  intro x hx
  rcases h with ⟨s, hs, hR⟩ | ⟨m, hm, hH⟩
  · exact hR.1 x (by have := hf.1 s hs; omega)
  · exact hH x (by have := hf.2 m hm; omega)

/-- The whole check: cut `b` at time `0`, thresholds `k0 :: ks`, target `Q` at time `T`. -/
def check (lo : Int) (row0 : Nat) (b : Int) (ks : List Int) (T : Nat) (Q : Int) : Bool :=
  match ks with
  | [] => false
  | k0 :: ks' =>
    match run lo T 0 row0 ks' ⟨expand b (k0 - b).toNat, some (b + ((k0 - b).toNat : Int))⟩ with
    | some c => finalOK Q c
    | none => false

theorem check_sound {E H : Nat → Int → Bool} (hE : IsR30Z E) (hH : IsR30Z H) {lo : Int} {row0 : Nat} {b : Int}
    {ks : List Int} {T : Nat} {Q : Int} (hc : check lo row0 b ks T Q = true)
    (h0 : ∀ i, row0.testBit i = E 0 (lo + i)) (hb : ∀ x, x ≤ b → H 0 x = E 0 x) :
    ∀ x, x ≤ Q → H T x = E T x := by
  unfold check at hc
  split at hc
  · simp at hc
  · next k0 ks' =>
    split at hc
    · next c hr =>
      have hinit : HoldsH (dif H E 0) b := fun x hx => by unfold dif; rw [hb x hx]; simp
      have hinv : Inv (dif H E 0) ⟨expand b (k0 - b).toNat, some (b + ((k0 - b).toNat : Int))⟩ := by
        rcases expand_sound _ (k0 - b).toNat b hinit with ⟨s, hs, hR⟩ | hH'
        · exact Or.inl ⟨s, hs, hR⟩
        · exact Or.inr ⟨_, rfl, hH'⟩
      have := run_sound hE hH lo T 0 row0 ks' _ c (fun i _ => h0 i) hinv hr
      rw [Nat.zero_add] at this
      intro x hx
      have hd := final_sound this hc x hx
      unfold dif at hd
      cases hHx : H T x <;> cases hEx : E T x <;> simp_all
    · simp at hc

/-! ### The inserted edge's initial row as a bit mask -/

/-- Little-endian bits to a number. -/
def ofBits : List Bool → Nat
  | [] => 0
  | b :: l => (if b then 1 else 0) + 2 * ofBits l

theorem ofBits_lt : ∀ l : List Bool, ofBits l < 2 ^ l.length := by
  intro l
  induction l with
  | nil => simp [ofBits]
  | cons b l ih => simp only [ofBits, List.length_cons, Nat.pow_succ]; cases b <;> simp <;> omega

/-- The edge's row on `x = -1000 .. 0`; white beyond. -/
def lo0 : Int := -1000

def row0 (c0 c1 : Nat) : Nat := ofBits ((List.range 1001).map fun i : Nat => initRow c0 c1 (lo0 + (i : Int)))

set_option exponentiation.threshold 1100 in
theorem row0_spec (c0 c1 : Nat) (hlow : ∀ i, i < 1001 → (row0 c0 c1).testBit i = initRow c0 c1 (lo0 + i)) :
    ∀ i, (row0 c0 c1).testBit i = G c0 c1 0 (lo0 + i) := by
  intro i
  show _ = initRow c0 c1 (lo0 + i)
  by_cases hi : i < 1001
  · exact hlow i hi
  · have hlt : row0 c0 c1 < 2 ^ i := by
      have h1 := ofBits_lt ((List.range 1001).map fun i : Nat => initRow c0 c1 (lo0 + (i : Int)))
      rw [List.length_map, List.length_range] at h1
      exact Nat.lt_of_lt_of_le h1 (Nat.pow_le_pow_right (by decide) (by omega))
    rw [Nat.testBit_lt_two_pow hlt]
    unfold initRow lo0
    simp only [show ¬ (-1000 + (i : Int) < 0) by omega, show ¬ (-1000 + (i : Int) = 0) by omega, ite_false]


/-! ### A1 with cutoff 87 -/

/-- From a passing entry check, every evolution agreeing with the inserted edge's at the entry time on `x ≤ xB + 13` is
pinned (A1's `pinned_of_check_tail`, with the agreement supplied directly). -/
theorem pinned_of_agree {c0 c1 t1 : Nat} {xB : Int} (h : checkEntry c0 c1 t1 xB = true)
    {H : Nat → Int → Bool} (hH : IsR30Z H) (hag : ∀ x, x ≤ xB + 13 → H t1 x = G c0 c1 t1 x) :
    ∀ t, t1 ≤ t → (∀ x, x ≤ xB → H t x = etherZ c0 x (t + c1)) ∧
      ∃ x, xB < x ∧ x ≤ xB + 13 ∧ H t x ≠ etherZ c0 x (t + c1) := by
  obtain ⟨hk, hE, hW⟩ := entry_spec h
  have hE' : ∀ x, x ≤ xB → H t1 x = etherZ c0 x (t1 + c1) := fun x hx => by
    rw [hag x (by omega)]; exact hE x hx
  have hrow : rowZ H t1 xB 13 = rowZ (G c0 c1) t1 xB 13 :=
    seg_congr _ _ _ (fun i hi => hag _ (by omega))
  have hW' : ((t1 + c1) % 4, rowZ H t1 xB 13) ∈ wallStates := by rw [hrow]; exact hW
  have inv := trap_two_sided hH (c0 : Int) xB c1 t1 hk hE' hW'
  intro t ht
  obtain ⟨hE2, hW2⟩ := inv (t - t1)
  rw [show t1 + (t - t1) = t by omega] at hE2 hW2
  refine ⟨hE2, ?_⟩
  have hne : rowZ H t xB 13 ≠ refStrip ((t + c1) % 4) := by
    have := List.all_eq_true.1 wall_ne_ref_all _ hW2
    simpa using this
  unfold rowZ refStrip at hne
  obtain ⟨i, hi, hfi⟩ := seg_ne_witness 13 _ _ hne
  refine ⟨xB + (i : Int) + 1, by omega, by omega, fun hc => hfi ?_⟩
  rw [hc]
  exact etherZ_eq_ether (by omega) (by omega)

/-! The thresholds `ks` (A2's backward thresholds, GC2423, for the entry window) are untrusted data. -/

def ks_0_0 : List Int := [40, 39, 38, 37, 36, 35, 34, 33, 32, 31, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 19, 19, 19, 19, 18, 18, 18, 17, 16, 15, 15, 14, 13, 13, 12, 12, 11, 11, 11, 10, 10, 10, 9, 9, 8, 7, 7, 6, 6, 6, 6, 6, 5, 4, 3, 3, 2, 2, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, -1, -1, -2, -3, -3, -3, -3, -4, -4, -5, -5, -6]
def ks_0_1 : List Int := [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 9, 8]
def ks_0_2 : List Int := [25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15]
def ks_0_3 : List Int := [106, 105, 104, 103, 102, 101, 100, 99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86, 85, 84, 83, 82, 81, 80, 79, 78, 77, 76, 75, 74, 73, 72, 71, 70, 69, 68, 67, 66, 65, 64, 63, 62, 61, 60, 59, 58, 57, 56, 55, 54, 53, 52, 52, 52, 52, 51, 51, 51, 51, 50, 50, 49, 49, 49, 48, 48, 47, 47, 47, 47, 46, 46, 45, 45, 44, 43, 43, 43, 43, 43, 42, 42, 41, 40, 40, 40, 40, 39, 38, 38, 38, 37, 36, 36, 35, 34, 34, 34, 34, 33, 33, 32, 31, 30, 29, 29, 28, 27, 26, 26, 25, 25, 24, 23, 23, 22, 21, 21, 21, 21, 20, 20, 19, 18, 17, 16, 16, 15, 14, 14, 14, 13, 13, 13, 12, 12, 11, 11, 10, 10, 10, 10, 9, 9, 9, 8, 8, 8, 7, 6, 6, 5, 5, 5, 4, 4, 3, 2, 1, 0, -1, -2, -3, -3, -3, -3, -4, -5, -6, -6, -7, -7, -8, -9, -9, -10, -10, -10, -10, -11, -11, -12, -12, -13]
def ks_1_0 : List Int := [104, 103, 102, 101, 100, 99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86, 85, 84, 83, 82, 81, 80, 79, 78, 77, 76, 75, 74, 73, 72, 71, 70, 69, 68, 67, 66, 65, 64, 63, 62, 61, 60, 59, 58, 57, 56, 55, 54, 53, 52, 51, 51, 51, 51, 50, 50, 50, 50, 49, 49, 48, 48, 48, 47, 47, 46, 46, 46, 46, 45, 45, 44, 44, 43, 42, 42, 42, 42, 42, 41, 41, 40, 39, 39, 39, 39, 38, 37, 37, 37, 36, 35, 35, 34, 33, 33, 33, 33, 32, 32, 31, 30, 29, 28, 28, 27, 26, 25, 25, 24, 24, 23, 22, 22, 21, 20, 20, 20, 20, 19, 19, 18, 17, 16, 15, 15, 14, 13, 13, 13, 12, 12, 12, 11, 11, 10, 10, 9, 9, 9, 9, 8, 8, 8, 7, 7, 7, 6, 5, 5, 4, 4, 4, 3, 3, 2, 1, 0, -1, -2, -3, -4, -4, -4, -4, -5, -6, -7, -7, -8, -8, -9, -10, -10, -11, -11, -11, -11, -12, -12, -13, -13, -14]
def ks_1_1 : List Int := [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 10, 10, 9, 9, 9, 8, 7]
def ks_1_2 : List Int := [23, 22, 21, 20, 19, 18, 17, 16, 15, 14]
def ks_1_3 : List Int := [23, 22, 21, 20, 19, 18, 17, 16, 15, 14]
def ks_2_0 : List Int := [21, 20, 19, 18, 17, 16, 15, 14, 13]
def ks_2_1 : List Int := [18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 9, 9, 9, 8, 8, 8, 7, 6]
def ks_2_2 : List Int := [18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 9, 9, 8, 8, 8, 7, 6]
def ks_2_3 : List Int := [21, 20, 19, 18, 17, 16, 15, 14, 13]
def ks_3_0 : List Int := [19, 18, 17, 16, 15, 14, 13, 12]
def ks_3_1 : List Int := [19, 18, 17, 16, 15, 14, 13, 12]
def ks_3_2 : List Int := [16, 15, 14, 13, 12, 11, 10, 9, 8, 8, 8, 8, 7, 7, 7, 6, 5]
def ks_3_3 : List Int := [19, 18, 17, 16, 15, 14, 13, 12]
def ks_4_0 : List Int := [17, 16, 15, 14, 13, 12, 11]
def ks_4_1 : List Int := [82, 81, 80, 79, 78, 77, 76, 75, 74, 73, 72, 71, 70, 69, 68, 67, 66, 65, 64, 63, 62, 61, 60, 59, 58, 57, 56, 55, 54, 53, 52, 51, 50, 49, 48, 47, 46, 45, 44, 43, 42, 41, 40, 40, 40, 39, 38, 38, 37, 36, 36, 36, 35, 34, 33, 33, 32, 32, 32, 31, 31, 30, 30, 30, 30, 30, 29, 28, 28, 28, 28, 27, 26, 25, 24, 23, 22, 21, 21, 21, 21, 21, 20, 19, 18, 17, 17, 17, 16, 16, 15, 14, 13, 13, 13, 12, 11, 10, 10, 10, 10, 10, 10, 10, 10, 9, 8, 8, 7, 6, 5, 4, 3, 3, 2, 2, 1, 0, 0, 0, -1, -1, -1, -1, -1, -1, -2, -3, -3, -3, -3, -3, -4, -4, -4, -4, -4, -5, -5, -6, -7, -7, -7, -7, -8, -8, -9, -9, -10]
def ks_4_2 : List Int := [17, 16, 15, 14, 13, 12, 11]
def ks_4_3 : List Int := [112, 111, 110, 109, 108, 107, 106, 105, 104, 103, 102, 101, 100, 99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86, 85, 84, 83, 82, 81, 80, 79, 78, 77, 76, 75, 74, 73, 72, 71, 70, 69, 68, 67, 66, 65, 64, 63, 62, 61, 60, 59, 58, 57, 56, 56, 55, 55, 54, 53, 52, 52, 52, 51, 50, 49, 48, 47, 47, 46, 45, 45, 44, 43, 42, 42, 41, 41, 40, 39, 38, 38, 37, 36, 36, 36, 36, 35, 35, 35, 34, 34, 34, 33, 32, 31, 30, 29, 28, 28, 27, 26, 25, 25, 25, 24, 24, 23, 23, 22, 22, 21, 21, 21, 20, 19, 18, 17, 17, 17, 17, 17, 17, 17, 17, 16, 16, 15, 15, 14, 13, 13, 13, 13, 13, 13, 13, 12, 12, 12, 12, 12, 11, 10, 10, 10, 10, 10, 9, 9, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 0, 0, -1, -2, -2, -2, -2, -3, -4, -4, -4, -4, -5, -5, -5, -6, -7, -8, -8, -9, -9, -9, -10, -10, -11, -11, -12, -12, -13, -14, -14, -14, -15, -15, -15, -15, -15, -15, -16, -17, -17, -17, -17, -17, -18, -18, -18, -18, -18, -19, -19, -20, -21, -21, -21, -21, -22, -22, -23, -23, -24]
def ks_5_0 : List Int := [110, 109, 108, 107, 106, 105, 104, 103, 102, 101, 100, 99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86, 85, 84, 83, 82, 81, 80, 79, 78, 77, 76, 75, 74, 73, 72, 71, 70, 69, 68, 67, 66, 65, 64, 63, 62, 61, 60, 59, 58, 57, 56, 55, 55, 54, 54, 53, 52, 51, 51, 51, 50, 49, 48, 47, 46, 46, 45, 44, 44, 43, 42, 41, 41, 40, 40, 39, 38, 37, 37, 36, 35, 35, 35, 35, 34, 34, 34, 33, 33, 33, 32, 31, 30, 29, 28, 27, 27, 26, 25, 24, 24, 24, 23, 23, 22, 22, 21, 21, 20, 20, 20, 19, 18, 17, 16, 16, 16, 16, 16, 16, 16, 16, 15, 15, 14, 14, 13, 12, 12, 12, 12, 12, 12, 12, 11, 11, 11, 11, 11, 10, 9, 9, 9, 9, 9, 8, 8, 8, 7, 6, 5, 4, 3, 2, 1, 0, 0, -1, -1, -2, -3, -3, -3, -3, -4, -5, -5, -5, -5, -6, -6, -6, -7, -8, -9, -9, -10, -10, -10, -11, -11, -12, -12, -13, -13, -14, -15, -15, -15, -16, -16, -16, -16, -16, -16, -17, -18, -18, -18, -18, -18, -19, -19, -19, -19, -19, -20, -20, -21, -22, -22, -22, -22, -23, -23, -24, -24, -25]
def ks_5_1 : List Int := [80, 79, 78, 77, 76, 75, 74, 73, 72, 71, 70, 69, 68, 67, 66, 65, 64, 63, 62, 61, 60, 59, 58, 57, 56, 55, 54, 53, 52, 51, 50, 49, 48, 47, 46, 45, 44, 43, 42, 41, 40, 40, 39, 39, 39, 38, 37, 37, 36, 35, 35, 35, 34, 33, 32, 32, 31, 31, 31, 30, 30, 29, 29, 29, 29, 29, 28, 27, 27, 27, 27, 26, 25, 24, 23, 22, 21, 20, 20, 20, 20, 20, 19, 18, 17, 16, 16, 16, 15, 15, 14, 13, 12, 12, 12, 11, 10, 9, 9, 9, 9, 9, 9, 9, 9, 8, 7, 7, 6, 5, 4, 3, 2, 2, 1, 1, 0, -1, -1, -1, -2, -2, -2, -2, -2, -2, -3, -4, -4, -4, -4, -4, -5, -5, -5, -5, -5, -6, -6, -7, -8, -8, -8, -8, -9, -9, -10, -10, -11]
def ks_5_2 : List Int := [15, 14, 13, 12, 11, 10]
def ks_5_3 : List Int := [15, 14, 13, 12, 11, 10]
def ks_6_0 : List Int := [13, 12, 11, 10, 9]
def ks_6_1 : List Int := [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 9, 9, 9, 9, 9, 8, 8, 7, 6, 5, 4, 4, 3, 2]
def ks_6_2 : List Int := [13, 12, 11, 10, 9]
def ks_6_3 : List Int := [42, 41, 40, 39, 38, 37, 36, 35, 34, 33, 32, 31, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 20, 20, 20, 20, 19, 19, 19, 18, 17, 16, 16, 15, 14, 14, 13, 13, 12, 12, 12, 11, 11, 11, 10, 10, 9, 8, 8, 7, 7, 7, 7, 7, 6, 5, 4, 4, 3, 3, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 0, 0, -1, -2, -2, -2, -2, -3, -3, -4, -4, -5]

theorem tail87_0_0 {H : Nat → Int → Bool} (hH : IsR30Z H) (h0 : ∀ x, x ≤ 87 → H 0 x = initRow 0 0 x) :
    ∀ x, x ≤ (-19) + 13 → H 81 x = G 0 0 81 x :=
  check_sound (G_isR30 0 0) hH (by decide +kernel : check lo0 (row0 0 0) 87 ks_0_0 81 ((-19) + 13) = true)
    (row0_spec 0 0 (by decide +kernel)) h0

theorem tail87_0_1 {H : Nat → Int → Bool} (hH : IsR30Z H) (h0 : ∀ x, x ≤ 87 → H 0 x = initRow 0 1 x) :
    ∀ x, x ≤ (-5) + 13 → H 13 x = G 0 1 13 x :=
  check_sound (G_isR30 0 1) hH (by decide +kernel : check lo0 (row0 0 1) 87 ks_0_1 13 ((-5) + 13) = true)
    (row0_spec 0 1 (by decide +kernel)) h0

theorem tail87_0_2 {H : Nat → Int → Bool} (hH : IsR30Z H) (h0 : ∀ x, x ≤ 87 → H 0 x = initRow 0 2 x) :
    ∀ x, x ≤ 2 + 13 → H 10 x = G 0 2 10 x :=
  check_sound (G_isR30 0 2) hH (by decide +kernel : check lo0 (row0 0 2) 87 ks_0_2 10 (2 + 13) = true)
    (row0_spec 0 2 (by decide +kernel)) h0

theorem tail87_0_3 {H : Nat → Int → Bool} (hH : IsR30Z H) (h0 : ∀ x, x ≤ 87 → H 0 x = initRow 0 3 x) :
    ∀ x, x ≤ (-26) + 13 → H 186 x = G 0 3 186 x :=
  check_sound (G_isR30 0 3) hH (by decide +kernel : check lo0 (row0 0 3) 87 ks_0_3 186 ((-26) + 13) = true)
    (row0_spec 0 3 (by decide +kernel)) h0

theorem tail87_1_0 {H : Nat → Int → Bool} (hH : IsR30Z H) (h0 : ∀ x, x ≤ 87 → H 0 x = initRow 1 0 x) :
    ∀ x, x ≤ (-27) + 13 → H 185 x = G 1 0 185 x :=
  check_sound (G_isR30 1 0) hH (by decide +kernel : check lo0 (row0 1 0) 87 ks_1_0 185 ((-27) + 13) = true)
    (row0_spec 1 0 (by decide +kernel)) h0

theorem tail87_1_1 {H : Nat → Int → Bool} (hH : IsR30Z H) (h0 : ∀ x, x ≤ 87 → H 0 x = initRow 1 1 x) :
    ∀ x, x ≤ (-6) + 13 → H 17 x = G 1 1 17 x :=
  check_sound (G_isR30 1 1) hH (by decide +kernel : check lo0 (row0 1 1) 87 ks_1_1 17 ((-6) + 13) = true)
    (row0_spec 1 1 (by decide +kernel)) h0

theorem tail87_1_2 {H : Nat → Int → Bool} (hH : IsR30Z H) (h0 : ∀ x, x ≤ 87 → H 0 x = initRow 1 2 x) :
    ∀ x, x ≤ 1 + 13 → H 9 x = G 1 2 9 x :=
  check_sound (G_isR30 1 2) hH (by decide +kernel : check lo0 (row0 1 2) 87 ks_1_2 9 (1 + 13) = true)
    (row0_spec 1 2 (by decide +kernel)) h0

theorem tail87_1_3 {H : Nat → Int → Bool} (hH : IsR30Z H) (h0 : ∀ x, x ≤ 87 → H 0 x = initRow 1 3 x) :
    ∀ x, x ≤ 1 + 13 → H 9 x = G 1 3 9 x :=
  check_sound (G_isR30 1 3) hH (by decide +kernel : check lo0 (row0 1 3) 87 ks_1_3 9 (1 + 13) = true)
    (row0_spec 1 3 (by decide +kernel)) h0

theorem tail87_2_0 {H : Nat → Int → Bool} (hH : IsR30Z H) (h0 : ∀ x, x ≤ 87 → H 0 x = initRow 2 0 x) :
    ∀ x, x ≤ 0 + 13 → H 8 x = G 2 0 8 x :=
  check_sound (G_isR30 2 0) hH (by decide +kernel : check lo0 (row0 2 0) 87 ks_2_0 8 (0 + 13) = true)
    (row0_spec 2 0 (by decide +kernel)) h0

theorem tail87_2_1 {H : Nat → Int → Bool} (hH : IsR30Z H) (h0 : ∀ x, x ≤ 87 → H 0 x = initRow 2 1 x) :
    ∀ x, x ≤ (-7) + 13 → H 17 x = G 2 1 17 x :=
  check_sound (G_isR30 2 1) hH (by decide +kernel : check lo0 (row0 2 1) 87 ks_2_1 17 ((-7) + 13) = true)
    (row0_spec 2 1 (by decide +kernel)) h0

theorem tail87_2_2 {H : Nat → Int → Bool} (hH : IsR30Z H) (h0 : ∀ x, x ≤ 87 → H 0 x = initRow 2 2 x) :
    ∀ x, x ≤ (-7) + 13 → H 16 x = G 2 2 16 x :=
  check_sound (G_isR30 2 2) hH (by decide +kernel : check lo0 (row0 2 2) 87 ks_2_2 16 ((-7) + 13) = true)
    (row0_spec 2 2 (by decide +kernel)) h0

theorem tail87_2_3 {H : Nat → Int → Bool} (hH : IsR30Z H) (h0 : ∀ x, x ≤ 87 → H 0 x = initRow 2 3 x) :
    ∀ x, x ≤ 0 + 13 → H 8 x = G 2 3 8 x :=
  check_sound (G_isR30 2 3) hH (by decide +kernel : check lo0 (row0 2 3) 87 ks_2_3 8 (0 + 13) = true)
    (row0_spec 2 3 (by decide +kernel)) h0

theorem tail87_3_0 {H : Nat → Int → Bool} (hH : IsR30Z H) (h0 : ∀ x, x ≤ 87 → H 0 x = initRow 3 0 x) :
    ∀ x, x ≤ (-1) + 13 → H 7 x = G 3 0 7 x :=
  check_sound (G_isR30 3 0) hH (by decide +kernel : check lo0 (row0 3 0) 87 ks_3_0 7 ((-1) + 13) = true)
    (row0_spec 3 0 (by decide +kernel)) h0

theorem tail87_3_1 {H : Nat → Int → Bool} (hH : IsR30Z H) (h0 : ∀ x, x ≤ 87 → H 0 x = initRow 3 1 x) :
    ∀ x, x ≤ (-1) + 13 → H 7 x = G 3 1 7 x :=
  check_sound (G_isR30 3 1) hH (by decide +kernel : check lo0 (row0 3 1) 87 ks_3_1 7 ((-1) + 13) = true)
    (row0_spec 3 1 (by decide +kernel)) h0

theorem tail87_3_2 {H : Nat → Int → Bool} (hH : IsR30Z H) (h0 : ∀ x, x ≤ 87 → H 0 x = initRow 3 2 x) :
    ∀ x, x ≤ (-8) + 13 → H 16 x = G 3 2 16 x :=
  check_sound (G_isR30 3 2) hH (by decide +kernel : check lo0 (row0 3 2) 87 ks_3_2 16 ((-8) + 13) = true)
    (row0_spec 3 2 (by decide +kernel)) h0

theorem tail87_3_3 {H : Nat → Int → Bool} (hH : IsR30Z H) (h0 : ∀ x, x ≤ 87 → H 0 x = initRow 3 3 x) :
    ∀ x, x ≤ (-1) + 13 → H 7 x = G 3 3 7 x :=
  check_sound (G_isR30 3 3) hH (by decide +kernel : check lo0 (row0 3 3) 87 ks_3_3 7 ((-1) + 13) = true)
    (row0_spec 3 3 (by decide +kernel)) h0

theorem tail87_4_0 {H : Nat → Int → Bool} (hH : IsR30Z H) (h0 : ∀ x, x ≤ 87 → H 0 x = initRow 4 0 x) :
    ∀ x, x ≤ (-2) + 13 → H 6 x = G 4 0 6 x :=
  check_sound (G_isR30 4 0) hH (by decide +kernel : check lo0 (row0 4 0) 87 ks_4_0 6 ((-2) + 13) = true)
    (row0_spec 4 0 (by decide +kernel)) h0

theorem tail87_4_1 {H : Nat → Int → Bool} (hH : IsR30Z H) (h0 : ∀ x, x ≤ 87 → H 0 x = initRow 4 1 x) :
    ∀ x, x ≤ (-23) + 13 → H 148 x = G 4 1 148 x :=
  check_sound (G_isR30 4 1) hH (by decide +kernel : check lo0 (row0 4 1) 87 ks_4_1 148 ((-23) + 13) = true)
    (row0_spec 4 1 (by decide +kernel)) h0

theorem tail87_4_2 {H : Nat → Int → Bool} (hH : IsR30Z H) (h0 : ∀ x, x ≤ 87 → H 0 x = initRow 4 2 x) :
    ∀ x, x ≤ (-2) + 13 → H 6 x = G 4 2 6 x :=
  check_sound (G_isR30 4 2) hH (by decide +kernel : check lo0 (row0 4 2) 87 ks_4_2 6 ((-2) + 13) = true)
    (row0_spec 4 2 (by decide +kernel)) h0

theorem tail87_4_3 {H : Nat → Int → Bool} (hH : IsR30Z H) (h0 : ∀ x, x ≤ 87 → H 0 x = initRow 4 3 x) :
    ∀ x, x ≤ (-37) + 13 → H 222 x = G 4 3 222 x :=
  check_sound (G_isR30 4 3) hH (by decide +kernel : check lo0 (row0 4 3) 87 ks_4_3 222 ((-37) + 13) = true)
    (row0_spec 4 3 (by decide +kernel)) h0

theorem tail87_5_0 {H : Nat → Int → Bool} (hH : IsR30Z H) (h0 : ∀ x, x ≤ 87 → H 0 x = initRow 5 0 x) :
    ∀ x, x ≤ (-38) + 13 → H 221 x = G 5 0 221 x :=
  check_sound (G_isR30 5 0) hH (by decide +kernel : check lo0 (row0 5 0) 87 ks_5_0 221 ((-38) + 13) = true)
    (row0_spec 5 0 (by decide +kernel)) h0

theorem tail87_5_1 {H : Nat → Int → Bool} (hH : IsR30Z H) (h0 : ∀ x, x ≤ 87 → H 0 x = initRow 5 1 x) :
    ∀ x, x ≤ (-24) + 13 → H 148 x = G 5 1 148 x :=
  check_sound (G_isR30 5 1) hH (by decide +kernel : check lo0 (row0 5 1) 87 ks_5_1 148 ((-24) + 13) = true)
    (row0_spec 5 1 (by decide +kernel)) h0

theorem tail87_5_2 {H : Nat → Int → Bool} (hH : IsR30Z H) (h0 : ∀ x, x ≤ 87 → H 0 x = initRow 5 2 x) :
    ∀ x, x ≤ (-3) + 13 → H 5 x = G 5 2 5 x :=
  check_sound (G_isR30 5 2) hH (by decide +kernel : check lo0 (row0 5 2) 87 ks_5_2 5 ((-3) + 13) = true)
    (row0_spec 5 2 (by decide +kernel)) h0

theorem tail87_5_3 {H : Nat → Int → Bool} (hH : IsR30Z H) (h0 : ∀ x, x ≤ 87 → H 0 x = initRow 5 3 x) :
    ∀ x, x ≤ (-3) + 13 → H 5 x = G 5 3 5 x :=
  check_sound (G_isR30 5 3) hH (by decide +kernel : check lo0 (row0 5 3) 87 ks_5_3 5 ((-3) + 13) = true)
    (row0_spec 5 3 (by decide +kernel)) h0

theorem tail87_6_0 {H : Nat → Int → Bool} (hH : IsR30Z H) (h0 : ∀ x, x ≤ 87 → H 0 x = initRow 6 0 x) :
    ∀ x, x ≤ (-4) + 13 → H 4 x = G 6 0 4 x :=
  check_sound (G_isR30 6 0) hH (by decide +kernel : check lo0 (row0 6 0) 87 ks_6_0 4 ((-4) + 13) = true)
    (row0_spec 6 0 (by decide +kernel)) h0

theorem tail87_6_1 {H : Nat → Int → Bool} (hH : IsR30Z H) (h0 : ∀ x, x ≤ 87 → H 0 x = initRow 6 1 x) :
    ∀ x, x ≤ (-11) + 13 → H 25 x = G 6 1 25 x :=
  check_sound (G_isR30 6 1) hH (by decide +kernel : check lo0 (row0 6 1) 87 ks_6_1 25 ((-11) + 13) = true)
    (row0_spec 6 1 (by decide +kernel)) h0

theorem tail87_6_2 {H : Nat → Int → Bool} (hH : IsR30Z H) (h0 : ∀ x, x ≤ 87 → H 0 x = initRow 6 2 x) :
    ∀ x, x ≤ (-4) + 13 → H 4 x = G 6 2 4 x :=
  check_sound (G_isR30 6 2) hH (by decide +kernel : check lo0 (row0 6 2) 87 ks_6_2 4 ((-4) + 13) = true)
    (row0_spec 6 2 (by decide +kernel)) h0

theorem tail87_6_3 {H : Nat → Int → Bool} (hH : IsR30Z H) (h0 : ∀ x, x ≤ 87 → H 0 x = initRow 6 3 x) :
    ∀ x, x ≤ (-18) + 13 → H 82 x = G 6 3 82 x :=
  check_sound (G_isR30 6 3) hH (by decide +kernel : check lo0 (row0 6 3) 87 ks_6_3 82 ((-18) + 13) = true)
    (row0_spec 6 3 (by decide +kernel)) h0

/-- **Arbitrary right tails beyond 87.** A1's `edge_pinned_tail` with cutoff `87` in place of `198`: every rule-30
evolution of the whole line whose initial row agrees with the inserted edge's on `x ≤ 87`, whatever it holds beyond, is
pinned in the same 13-cell window from the same time on. -/
theorem edge_pinned_tail87 (c0 c1 : Nat) (h0' : c0 < 7) (h1' : c1 < 4) {H : Nat → Int → Bool} (hH : IsR30Z H)
    (h0 : ∀ x, x ≤ 87 → H 0 x = initRow c0 c1 x) : ∃ xB : Int, ∃ t1 : Nat, ∀ t, t1 ≤ t →
    (∀ x, x ≤ xB → H t x = etherZ c0 x (t + c1)) ∧ ∃ x, xB < x ∧ x ≤ xB + 13 ∧ H t x ≠ etherZ c0 x (t + c1) :=
  match c0, c1, h0', h1' with
  | 0, 0, _, _ => ⟨(-19), 81, pinned_of_agree entry_0_0 hH (tail87_0_0 hH h0)⟩
  | 0, 1, _, _ => ⟨(-5), 13, pinned_of_agree entry_0_1 hH (tail87_0_1 hH h0)⟩
  | 0, 2, _, _ => ⟨2, 10, pinned_of_agree entry_0_2 hH (tail87_0_2 hH h0)⟩
  | 0, 3, _, _ => ⟨(-26), 186, pinned_of_agree entry_0_3 hH (tail87_0_3 hH h0)⟩
  | 1, 0, _, _ => ⟨(-27), 185, pinned_of_agree entry_1_0 hH (tail87_1_0 hH h0)⟩
  | 1, 1, _, _ => ⟨(-6), 17, pinned_of_agree entry_1_1 hH (tail87_1_1 hH h0)⟩
  | 1, 2, _, _ => ⟨1, 9, pinned_of_agree entry_1_2 hH (tail87_1_2 hH h0)⟩
  | 1, 3, _, _ => ⟨1, 9, pinned_of_agree entry_1_3 hH (tail87_1_3 hH h0)⟩
  | 2, 0, _, _ => ⟨0, 8, pinned_of_agree entry_2_0 hH (tail87_2_0 hH h0)⟩
  | 2, 1, _, _ => ⟨(-7), 17, pinned_of_agree entry_2_1 hH (tail87_2_1 hH h0)⟩
  | 2, 2, _, _ => ⟨(-7), 16, pinned_of_agree entry_2_2 hH (tail87_2_2 hH h0)⟩
  | 2, 3, _, _ => ⟨0, 8, pinned_of_agree entry_2_3 hH (tail87_2_3 hH h0)⟩
  | 3, 0, _, _ => ⟨(-1), 7, pinned_of_agree entry_3_0 hH (tail87_3_0 hH h0)⟩
  | 3, 1, _, _ => ⟨(-1), 7, pinned_of_agree entry_3_1 hH (tail87_3_1 hH h0)⟩
  | 3, 2, _, _ => ⟨(-8), 16, pinned_of_agree entry_3_2 hH (tail87_3_2 hH h0)⟩
  | 3, 3, _, _ => ⟨(-1), 7, pinned_of_agree entry_3_3 hH (tail87_3_3 hH h0)⟩
  | 4, 0, _, _ => ⟨(-2), 6, pinned_of_agree entry_4_0 hH (tail87_4_0 hH h0)⟩
  | 4, 1, _, _ => ⟨(-23), 148, pinned_of_agree entry_4_1 hH (tail87_4_1 hH h0)⟩
  | 4, 2, _, _ => ⟨(-2), 6, pinned_of_agree entry_4_2 hH (tail87_4_2 hH h0)⟩
  | 4, 3, _, _ => ⟨(-37), 222, pinned_of_agree entry_4_3 hH (tail87_4_3 hH h0)⟩
  | 5, 0, _, _ => ⟨(-38), 221, pinned_of_agree entry_5_0 hH (tail87_5_0 hH h0)⟩
  | 5, 1, _, _ => ⟨(-24), 148, pinned_of_agree entry_5_1 hH (tail87_5_1 hH h0)⟩
  | 5, 2, _, _ => ⟨(-3), 5, pinned_of_agree entry_5_2 hH (tail87_5_2 hH h0)⟩
  | 5, 3, _, _ => ⟨(-3), 5, pinned_of_agree entry_5_3 hH (tail87_5_3 hH h0)⟩
  | 6, 0, _, _ => ⟨(-4), 4, pinned_of_agree entry_6_0 hH (tail87_6_0 hH h0)⟩
  | 6, 1, _, _ => ⟨(-11), 25, pinned_of_agree entry_6_1 hH (tail87_6_1 hH h0)⟩
  | 6, 2, _, _ => ⟨(-4), 4, pinned_of_agree entry_6_2 hH (tail87_6_2 hH h0)⟩
  | 6, 3, _, _ => ⟨(-18), 82, pinned_of_agree entry_6_3 hH (tail87_6_3 hH h0)⟩
  | c0 + 7, _, h, _ => absurd h (by omega)
  | _, c1 + 4, _, h => absurd h (by omega)

end Ruliology.CellularAutomata.RootedFront
