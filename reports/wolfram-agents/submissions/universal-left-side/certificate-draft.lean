import Ruliology.CellularAutomata.Rule30LeftCoincidence
import Ruliology.CellularAutomata.Rule30AgedLeftDiagonals

set_option autoImplicit false

namespace Rule30UniversalLeftSide

open Ruliology.CellularAutomata
open Rule30AgedLeftDiagonals Rule30FiniteDiagonals Rule30Diagonals Rule30Realization

/-! ### The induction on the wheel (stub of the generic theorem; Cloud's module replaces this section) -/

theorem rec_zero {a : Nat → Nat → Bool} (ha : Recurrence a) (h : a 0 0 = true) : ∀ t, a 0 t = true := by
  intro t
  induction t with
  | zero => exact h
  | succ t ih => rw [ha.1, ih]

theorem rec_one {a : Nat → Nat → Bool} (ha : Recurrence a) (h : a 0 0 = true) (t : Nat) : a 1 (t + 1) = true := by
  rw [ha.2.1, rec_zero ha h t]
  rfl

theorem child_same {a C : Nat → Nat → Bool} {k s T r : Nat} (ha : Recurrence a)
    (hC : ∀ t, C (k + 2) (t + 1) = xor (C k t) (C (k + 1) t || C (k + 2) t))
    (hk : ∀ t, T ≤ t → a k (t + s) = C k t) (hk1 : ∀ t, T ≤ t → a (k + 1) (t + s) = C (k + 1) t)
    (hr : T ≤ r) (hb : C (k + 1) r = true) :
    ∀ t, r + 1 ≤ t → a (k + 2) (t + s) = C (k + 2) t := by
  intro t ht
  obtain ⟨n, rfl⟩ : ∃ n, t = r + 1 + n := ⟨t - (r + 1), by omega⟩
  clear ht
  induction n with
  | zero =>
    have e : r + 1 + 0 + s = (r + s) + 1 := by omega
    rw [e, ha.2.2, hk r hr, hk1 r hr, hb, show r + 1 + 0 = r + 1 from rfl, hC, hb]
    rfl
  | succ n ih =>
    have e : r + 1 + (n + 1) + s = (r + 1 + n + s) + 1 := by omega
    have e2 : r + 1 + (n + 1) = (r + 1 + n) + 1 := by omega
    rw [e, ha.2.2, hk _ (by omega), hk1 _ (by omega), ih, e2, hC]

theorem child_white {a C : Nat → Nat → Bool} {k s T : Nat} (ha : Recurrence a)
    (hC : ∀ t, C (k + 2) (t + 1) = xor (C k t) (C (k + 1) t || C (k + 2) t))
    (hk : ∀ t, T ≤ t → a k (t + s) = C k t) (hk1 : ∀ t, T ≤ t → a (k + 1) (t + s) = C (k + 1) t)
    (hw : ∀ t, T ≤ t → C (k + 1) t = false) :
    (∀ t, T ≤ t → a (k + 2) (t + s) = C (k + 2) t) ∨
      (∀ t, T ≤ t → a (k + 2) (t + s) = !C (k + 2) t) := by
  have hstep : ∀ t, T ≤ t →
      xor (a (k + 2) (t + 1 + s)) (C (k + 2) (t + 1)) = xor (a (k + 2) (t + s)) (C (k + 2) t) := by
    intro t ht
    rw [show t + 1 + s = (t + s) + 1 by omega, ha.2.2, hk t ht, hk1 t ht, hC, hw t ht]
    cases C k t <;> cases a (k + 2) (t + s) <;> cases C (k + 2) t <;> rfl
  have hconst : ∀ n, xor (a (k + 2) (T + n + s)) (C (k + 2) (T + n)) =
      xor (a (k + 2) (T + s)) (C (k + 2) T) := by
    intro n
    induction n with
    | zero => rfl
    | succ n ih => rw [← ih, ← hstep (T + n) (by omega)]; rfl
  cases hT : xor (a (k + 2) (T + s)) (C (k + 2) T) with
  | false =>
    left
    intro t ht
    obtain ⟨n, rfl⟩ : ∃ n, t = T + n := ⟨t - T, by omega⟩
    have := hconst n
    rw [hT] at this
    cases h1 : a (k + 2) (T + n + s) <;> cases h2 : C (k + 2) (T + n) <;> simp_all
  | true =>
    right
    intro t ht
    obtain ⟨n, rfl⟩ : ∃ n, t = T + n := ⟨t - T, by omega⟩
    have := hconst n
    rw [hT] at this
    cases h1 : a (k + 2) (T + n + s) <;> cases h2 : C (k + 2) (T + n) <;> simp_all

theorem universal_of_strip {a C : Nat → Nat → Bool} {J : Nat} (hJ : 1 ≤ J) (ha : Recurrence a)
    (ha0 : a 0 0 = true) (h0 : ∀ t, C 0 t = true) (h1 : ∀ t, C 1 t = true)
    (hC : ∀ j t, j + 2 ≤ J → C (j + 2) (t + 1) = xor (C j t) (C (j + 1) t || C (j + 2) t))
    (hstep : ∀ m, m + 1 ≤ J → (∀ T, ∃ t, T ≤ t ∧ C m t = true) ∨
      ∃ L, (∀ j, j ≤ m → ∀ t, C j (t + L) = C j t) ∧ ∀ t, C (m + 1) (t + L) = !C (m + 1) t) :
    ∃ s, ∀ j, j ≤ J → ∃ T, ∀ t, T ≤ t → a j (t + s) = C j t := by
  have hmain : ∀ m, m + 1 ≤ J → ∃ s, ∀ j, j ≤ m + 1 → ∃ T, ∀ t, T ≤ t → a j (t + s) = C j t := by
    intro m
    induction m with
    | zero =>
      intro _
      refine ⟨0, fun j hj => ⟨1, fun t ht => ?_⟩⟩
      have hj' : j = 0 ∨ j = 1 := by omega
      rcases hj' with rfl | rfl
      · rw [rec_zero ha ha0, h0]
      · obtain ⟨u, rfl⟩ : ∃ u, t = u + 1 := ⟨t - 1, by omega⟩
        rw [Nat.add_zero, rec_one ha ha0, h1]
    | succ m ih =>
      intro hm
      obtain ⟨s, hs⟩ := ih (by omega)
      obtain ⟨T1, hT1⟩ := hs m (by omega)
      obtain ⟨T2, hT2⟩ := hs (m + 1) (by omega)
      have hCm : ∀ t, C (m + 2) (t + 1) = xor (C m t) (C (m + 1) t || C (m + 2) t) :=
        fun t => hC m t (by omega)
      by_cases hb : ∀ T, ∃ t, T ≤ t ∧ C (m + 1) t = true
      · obtain ⟨r, hr, hbr⟩ := hb (max T1 T2)
        have hnew := child_same (s := s) (T := max T1 T2) ha hCm
          (fun t ht => hT1 t (by omega)) (fun t ht => hT2 t (by omega)) hr hbr
        refine ⟨s, fun j hj => ?_⟩
        by_cases hjm : j ≤ m + 1
        · exact hs j hjm
        · have e : j = m + 2 := by omega
          subst e
          exact ⟨r + 1, hnew⟩
      · obtain ⟨T0, hT0⟩ := Classical.not_forall.mp hb
        have hw : ∀ t, T0 ≤ t → C (m + 1) t = false := by
          intro t ht
          cases e : C (m + 1) t with
          | false => rfl
          | true => exact absurd ⟨t, ht, e⟩ hT0
        rcases hstep (m + 1) hm with hb' | ⟨L, hper, hanti⟩
        · exact absurd hb' hb
        · have hT : ∀ t, max (max T1 T2) T0 ≤ t → T1 ≤ t ∧ T2 ≤ t ∧ T0 ≤ t := by
            intro t ht
            omega
          rcases child_white (s := s) (T := max (max T1 T2) T0) ha hCm
            (fun t ht => hT1 t (hT t ht).1) (fun t ht => hT2 t (hT t ht).2.1)
            (fun t ht => hw t (hT t ht).2.2) with same | flip
          · refine ⟨s, fun j hj => ?_⟩
            by_cases hjm : j ≤ m + 1
            · exact hs j hjm
            · have e : j = m + 2 := by omega
              subst e
              exact ⟨_, same⟩
          · refine ⟨s + L, fun j hj => ?_⟩
            by_cases hjm : j ≤ m + 1
            · obtain ⟨T, hT'⟩ := hs j hjm
              refine ⟨T, fun t ht => ?_⟩
              rw [show t + (s + L) = (t + L) + s by omega, hT' (t + L) (by omega), hper j hjm]
            · have e : j = m + 2 := by omega
              subst e
              refine ⟨max (max T1 T2) T0, fun t ht => ?_⟩
              rw [show t + (s + L) = (t + L) + s by omega, flip (t + L) (by omega), hanti]
              cases C (m + 1 + 1) t <;> rfl
  obtain ⟨s, hs⟩ := hmain (J - 1) (by omega)
  exact ⟨s, fun j hj => hs j (by omega)⟩

/-! ### Rows as numbers -/

/-- One update of the first `K` left diagonals, as a `K`-bit number (`v`'s bit `j` is diagonal `j`). -/
def stepK (K v : Nat) : Nat := ((v <<< 2) ^^^ ((v <<< 1) ||| v)) % 2 ^ K

/-- The row `t` ticks after `v`. -/
def rowAt (K v : Nat) : Nat → Nat
  | 0 => v
  | t + 1 => stepK K (rowAt K v t)

theorem stepK_bit_zero {K : Nat} (hK : 0 < K) (v : Nat) : (stepK K v).testBit 0 = v.testBit 0 := by
  simp [stepK, Nat.testBit_mod_two_pow, Nat.testBit_xor, Nat.testBit_or, Nat.testBit_shiftLeft, hK]

theorem stepK_bit_one {K : Nat} (hK : 1 < K) (v : Nat) :
    (stepK K v).testBit 1 = (v.testBit 0 || v.testBit 1) := by
  simp [stepK, Nat.testBit_mod_two_pow, Nat.testBit_xor, Nat.testBit_or, Nat.testBit_shiftLeft, hK]

theorem stepK_bit_step {K j : Nat} (hj : j + 2 < K) (v : Nat) :
    (stepK K v).testBit (j + 2) = xor (v.testBit j) (v.testBit (j + 1) || v.testBit (j + 2)) := by
  simp [stepK, Nat.testBit_mod_two_pow, Nat.testBit_xor, Nat.testBit_or, Nat.testBit_shiftLeft, hj]

theorem rowAt_add_period {K v P : Nat} (hP : rowAt K v P = v) (t : Nat) :
    rowAt K v (t + P) = rowAt K v t := by
  induction t with
  | zero => simpa [rowAt] using hP
  | succ t ih =>
    rw [show t + 1 + P = (t + P) + 1 by omega]
    simp only [rowAt]
    rw [ih]

theorem rowAt_add_mul {K v P : Nat} (hP : rowAt K v P = v) (t q : Nat) :
    rowAt K v (t + q * P) = rowAt K v t := by
  induction q with
  | zero => simp
  | succ q ih =>
    rw [Nat.succ_mul, show t + (q * P + P) = (t + q * P) + P by omega, rowAt_add_period hP, ih]

/-- The configuration of a row: bit `p` at position `p ≥ 0`, white on the left. -/
def ofRow (v : Nat) (p : Int) : Bool := if p < 0 then false else v.testBit p.toNat

theorem ofRow_left (v : Nat) : ∀ p, p < 0 → ofRow v p = false := by
  intro p hp
  simp [ofRow, hp]

/-- The left diagonals of a row, read off the number. -/
theorem Ld_ofRow {K : Nat} (hK : 1 < K) (v : Nat) (t : Nat) :
    ∀ j, j < K → Ld (ofRow v) 0 j t = (rowAt K v t).testBit j := by
  have hrec := Ld_recurrence (x := ofRow v) (anchor := 0) (ofRow_left v)
  induction t with
  | zero =>
    intro j _
    simp [Ld, evol, ofRow, rowAt]
  | succ t ih =>
    intro j hj
    cases j with
    | zero =>
      rw [hrec.1, ih 0 (by omega)]
      simp only [rowAt]
      rw [stepK_bit_zero (by omega)]
    | succ j =>
      cases j with
      | zero =>
        rw [hrec.2.1, ih 0 (by omega), ih 1 (by omega)]
        simp only [rowAt]
        rw [stepK_bit_one (by omega)]
      | succ j =>
        rw [hrec.2.2, ih j (by omega), ih (j + 1) (by omega), ih (j + 2) (by omega)]
        simp only [rowAt]
        rw [stepK_bit_step (by omega)]

/-! ### The strip: one row that returns after sixteen ticks -/

/-- The first 53,209 left diagonals of the single seed at tick 72,000 (`0x…`). -/
def B : Nat := 0x6497a92b8f14b7ac41ec8a22250fb68f5beaf5ddb3d5fd0ea31c7c6bff5291b5dbd937c37381dcf8444f16061122123e4c583ebe11c15ed63ab03499503bfc003bb184041a4323c495519e75aa757678cad0dc78784fd512f0b3089b31ef8432b25ca7da87698865d4a5195f23366c233de80292eb6bb2a9206743aca18e1fb4ffe46af75caa0ba3fd0c6f56efa611c9178e1b10b3492e4dd2719b1d3dd24bd3d01da37ada9e27ccd501a7869baac52f7cd7d2042c5c7fca540dc77456af306d1b9854716344eac2af78737472ccac796bfdf1d2b9e0cdc302ad4bfea4c46f4142067ae9f77aa1cce243d7ab7c96c1779bbda180d2d33b7531cec2e7e77a20d27d6c912ced316df811cbb790477259c6fe080edf8933e0937a4e208b595e2628f183ab813119011f387484c0c4b18570475916be457b02bfb354b974a7711c0500c13e4ce89344987f6d599ed2e359c6efd6b236cc2f2b4d8914dc5f9ce393c1d779c6d606c2252a5030c2590a3cf0222663129ed69ac993794d51ae14118f7253895e318d358d60ece9a9b2db6bca44ec97c288589ce633c269abdd470192224b5ff521f89ab4ff832d265ea7305643ea6e1b1c1044a095aed8dadf613024c55f430908075873bb526886e3525492fb2e349eed14cf4239ccbab00e137b023a4adc1c1385cf320bc716f3a11bf69076cff6f81bd0842e2ac3f73354943743d04d06a348f5e06b2a3cab350c49043fc03bcba8baa45f75c1c65a8751b1ada5958fe8541d32f00e7ac9f6f93be98ea9e829ec4c83d18cbb56c6f73f2f08766047752a996ee69c628972d1e0e92b4aad6d64a2e22c5544fe9cf6aed410d9f83c84305c33fc70c4b6ea3fe4f2a0d0164a2768cf30c4aacd6f7369c855a87c35329584477c259acbcc08a19a80e8c29506694477cc2bf90a1062c21ad8fd5a7438358b393efbf767c8188df71f1091f4866b2d1657ee49e9f75ab1a0c8b082ce0523e69f6011b0c7422cd4e56e41427a929b6cf72b7ec284754fd4da90c422842f78b574225be6111e9e8ce479b49f53005fbf71696c23062ae93d3ff201748f63024c0e23982c2533c723a6ed6ead720717fbc5a183061a580f584371cd3d96a44fca448202268d3a1efd165da2725359015fe08083646a4605815223ce46721d9bdf7eb38a6a394dd2c3c4d9d2cc0fed52e3bc537e91468b5d73b410958edc8bee033471d8667505771f92e87d06230147d6eee2e5f6326f12fc20340e61b3406e58bf7161fe5a837020b246e5b04dfc2f0c5674c39b1096039f73a436b6376751f3a3c0dca0d872814d1b6074053997074393a17c7100125c71fc7759878020c9abee42de82dfb58321b74391040a6893d1d635d52dc8d8dfd7fdef771208ddd4b8e56f335d712951ab1ec8ef06631f124ed68289202fa6b38655dc9347aa6e1d3b5e9b4e0f2bd6e7dd973b6b76a53b87bd49312f2e2404c454298dd81d7a43508cbfd3c529c88dbceebf15da68b9a2e22ba07b04d0fb8bcd9a97733e53223c8c4d90890bf58f28a0727f81ba2973e5d763b586d4730bff13e9f659897c19ca201b3dbfbb20ac101b2e826933dc00143f2de435a5cb06c6d94f808c76b275c29bee379555e903dbdc6248784a48d0ea472efa4c9811423ede7cee36cd572416d8d73ee69a32e098b7d75eb49f608716bd180116df3d2dde297862fce7f39376bb62506382a21da7b890ffbde81d102bbc484a8cefdbc68d05d1a9b3a0ed74d36f9c41e1d7ab82d2610704d9f521bd4d95ac37641a0f5a57c1c46e2dcf88baf17e3b5ec538e0e967e6db9f076c941079d541e0cfbef1582d982133831beb522c5245511e5fced58f973e1de63d5273195fcf7a62d28365434c7b527589cd606feb762f496673fbecc91ead7a44bcfbf45645d8982a84460841a28b8bbd0cc5d1e09e9396d4f37c481d3305d87649a4660a4ffa6af8f47b90083688b11b431601b4bd1fcdb5a33d18ca5acd344c75ddc02333b19182883cfd31474cfd6365b92f806a5ce36849d73cd3fde7d60039ac1b8f4269cc7ef2951e05187fe42f92a56fb7eff538f513cfccdc80db851b20234f88560d657dfdc8c8c70d8022eb156229a4b8e3d4acb3fdab6a955f6260dffb084171cae8b124e30ab5ff098805cdf8f68f0bac8616953e4f446e22c95a9f41ba77609390a51306ba91c8e255a72c5b4528c5b7ccbcf86da8eaefad83ef7048b828703cb8f91fed39a1401b92e85473296ebfb839965b4337135285740a5923bba5caac619ea32b2ef11d3637600c803e0f6de53efdacbf052bce5be1977e2c7df8973ddec633d9b4f67fe22c962b4a25e490de1e216f73f0d7977ee85c1a5a9f0bb8dd939e40a9770db36c979067b684c2fbbe8572cb15012df2d0e32f2efa45ac728084faf873fc7210858975e84ac7e36b69d1efffc846c8a5f0fde48857c524841e916ea2c3f28f73254088f6b3d15556a310aedb0bd8091b02c2724c22dfe0e3cd5a5ff033ea65d9b8a9c9f641b54905366facbca5d9aa03d029c526e179491694188f7aa6e5cd81a052c2828ebbf87fa04518677cfdd9df972ff487d4873303cd185955907662559762b55ec6d1ace2bc9bc4a9efbd22639388ed1463f6a1142adbd759de772cf2edebc895b71f71b31a8a4369795b7c7b245c9abb91ba3e55e23638ce8e356909c22728ed56ec4d86d55444ef37ae3b4a044295187e8c61f335d599bb1d91877507a6545b82d605ad189ac68b791a0dd2f6e701d12285b6c74f69ccc539ea5cc0e89e29cb3ee27e79e1c7e64302423835fe3ccda13c003de3bc3878104485d0a6e761c5c8a07b1ba6b3e1422d09fc88fc2def3381a61d44374b7843192a5bbe6c9946b50ea9e87509ac3f5fef674104a3dc93e3105cf86f71e29cee4409a5dc1061617ba3ead7317a55efceb5e80acd0812efe591b7c7fdac21885c29e57803b649cee577eafdefb5faa9fc63721e4840d4694a6a6d018c9a89558bfb1e072110f77b93825fbf900081aececdae9ebd19c1e37022f757d63d0109aac62aa9b669dc9fe546d82644d2489e53fcc61237caf2b58680d29df9e4673a7c3b6595e7b9bb6a2d2568fc091670e05abb80f861c74c6c5afed8709f3629c6ed12334abc7c43754189bd7ac879a44cc48c27bb4a0304cd16db11c3d30f239471ef390780850f1c91fd11d5c015136114c8a65b111227bd5510009d0a5c688d954f121242fddce72029ea5cebc9e31f140a935aaf04bb631b71bbe7b82bd3c7b0f2c2be938a999262d3f3b09d7f75c7572ea767d53ede43868dd3cdfc543e9865760465bad8d46ac08357fb75aeae08749f859f2212d8fea75b44601391df497819ab47ae70b8928331e1173c513da3b0d5187b818b4afd32005e82e70b1a830901102e771b9c095bfd6ff84efcd55802832cad332508c34da599a4343d3c9d5f5c624379e770432feb437fd23d7b895c32a993bb6a66bd04bd3ad12672ef3b6e76679da70bc6bd723b9a4627d4829994011f53c148b77dee47bfe9692fa5642eeb7b8c40798bcc6593ced7f715b2d35e36a1a0d0d1ebfea0b0f00be4df86eeb3ae3e9ab30321fad0c41f8aa5f54b3fc86a6d1048b9bedecc286d20cfb64fb72f81079ac70fc6817c09f715999f277c7334b907a9216edaf562da99ca600e9575432a5eeacdf124542054d777c7df89801c35cf769241a453fea7acbeb710168a121b311273fb839140cebc4a6f88f888cbf5935be25f707299bb15e57eeb33f8374585d43a086000e365970b82dce6267fb64e21328526a77254f108b8d4f80ec72003b5aa7abed6573330415e76f8e6d74ecf9efe8d63ee9284f0e7c56ae76364ca1405e0a65e38fef02db963f9a7051ba1a18ac413483e9ad22ba86937632aa22eee194baf2e798e9d34da3f4c48b44bdd3e674d7970ed811c569ddc88c746dd008fc889baa94ac882c86a3f657dd679fe0274cfeb2526a5f7c8c132e7285180ece1c16f0ec8197c7f8bc14fc3a1ed03e69ce119983872d5e90625b5b44a0ba1b40b01b7f3dd093fd67855bfc587dffdcfdb80562a70499fa5ea324bcb41a61bc2892e8f36a52457ac176739aaa72ce835ada34d9522c040a1caff89fe1006e976daf2f8aa7d15b2fb41938d5b1ff098a7c2d2d2c61b93a8e95488e2239f2fb0b7e8fdfed8bfbedcb83103704865baa672af7ad20630ac6eb9e40bcbd1aa0c62eb39619103a933c4a932518d9c91e396446316fc260f7e8b9440c9cbaa145572287d40a1803c33dab0913aa92c4fcca5af6d1046d53a09472e5800989c3802396fbf690455b45a7980d453d8bc5541b2a8ebdba2c38927cdd6216b346f3c2548d72720687bc7b53a466900936cb393728e5717ffcac038c2153eec787cf79bab6afa9a33a1147441cbe8d6749cc7df7a629da2e4870f40f8773522291b3c9be3eb17a907f811ea674c137b99477f90affa7b2992d42377488ff2510a1956da4d14242428f277a2db988910f7148c1fbbc139eaddb58ed1ba74a44623d5150636713bbb68205271e1a2be8e0da512010530dd2822d1f27d3e2090bddbf78d55df8b55d903e5fe419cac18d3947a51311ec86929b9b2ad8212d4c08f2bd7f05962a746aee964bac4b1c76d189bbff150415f8737f20b39497174cd1b88b4bc1641ae682bae4bbf1395fa78142c9f16629a727d98ff5ba6347039f96f5e0e24788c9b0fb61da0d27ec1ccd9bfa604e15a9958d3ff909da98e825620ece4c5cecb127323fcf38d93b507c0f6bdf83ce6118649283f3b627fe740b05b9f3f0fd7c8db1174db74f3ad2652e19105b71101367993866eea516d4f34a42d738481e210f5b9185cf6e60e16de311b28fce9edad83ed9d6cc9900f44de8eae0943000a4923615a85f1031d8701159c0f6cec18a18beaa8b7924851288b6d215ba98ffa675efc346f9c333e9df27907416399da333d8b846f40fde5e36063cb6c9e0b16c464afa950fd3ff9c95d85c3f94fcb2d819b18f2190ae291b1f39c83d773d840bf249ea9826934c608724df602efadc90ad84f7ceefcffb311b6a55da356b7fd4bef4d773cf9a0d88edad3af8371d0f165ae544516ac5b7509066c0d3c5bf17195157631a9af32edfd0616ea4e92011f6d0f60ff285d02ee229a8a3a61d711bb1e9e6500b72f488f6f6013c7e49ccc7560eacecb645e4e5bbeb6f2cb574ccb21f3e6d7cd0cfc7ef8768689a86eb10bb26a0b16028a056b31cfe064e838e376b611c19422e6fc4e4b2a2e618e896badb65a2f7b53593d4a5d37536d2df3d70fca33f1e8a62d2005e66d7581c6cd008d1d0db93dfc9381b06b9e6ce0eb93caa4c2df59ed5a934710201e921786b6c611c97eb4ffb81eb59136170d168f6ce3e0f1dec4eff6279048de644afb2f1b55a663189338aa24330378f8ef0ca0dcd5e2f1df7b6508c89b793212774e6dfe3ca5875ecc37aa6a6903f954d39f7d03f5ae00a38ad5fbef251bef2ea8431ded48c3d3ae913aa04981736582d9f55f54d5782f15e901a80b0169ab376cbe60e6caee93831fe1af2200a1c83e791ac1e8793c67a497d745dfef33468cdbdea7affb71a7e293ce17ed94af0b19357e9b0f0dda4c706dc64b46bfd01b48b606339a20658fcf1972280df4a27b0e21f5a7dea0a9b8ec81d1b621d88d806fc756a28aea1a55b4b29d9de7b8b44338e3322df587d7eff0a7a33da748d624e8ea57215330baa13c8d0096583cf91378a3b3c87b0b79942aa603a1b541519cc0f0e8c70c50361a9d731b3addc2c3698aa99806c42015168650f6dd5550c48dfb293bbe4febcb2769fa72b27371bf77a637a15f24d1de8699138287130f1890a46d20f9b52c25b321c2fcf39293c8fd424b77a0550868d14a7170dc2033807a665121d694e8c8b7ae9a396c2adbcb2f0d92f1acb38f51c27852756e049d5dcf1fe35d8923628f43302ff039ef59197625b78d563b25fd1f74ca05466e91d9a18b8ae61fcce389cc24cfd259e64214e5a40cdd5ee4978128d990bec1646eef3298b36b45961511cf0280b1d0c56f2339fa0d15c7f0d62f190717b08dded2118d1aa75895d38475abcb9c65456c3f4c36c8a5773547d63ff9bf0e885b09762053a2f97fa6490ab73103d5bbb018eb2b32a2162af6ab7d7329dcfd72f0a023902f1cef57ab0d850b056c99c31d4dbc889a04e6d5e42c37a222262c4655167e2f77451b21d0b30b4775e505843fb1e566a49045dfa9b5bc24e4d5ba259568252d6d5aab41d11926801fd310f310de5314cc32f59d46b8e56fed2361cb95d6ddce3d15d8362e81a62ea605329095084fd6e30b7df62396c4f1e8c8207f92bfa5fba2fe97e9858353eecfc0aea374ed7c7b632eeabbe78c431874d1cf77be986846da75d31b30abded309fa6959c28d7a25b39c3649e9d7550aa59c5a3f7cbda13dbf610dbf408caf3520f21dd03fdbfb33da6218fd9adcf17f3e11018ece2596f4b51b02e309e644a10a4be8741158435110b20aca030eae261af28ad7bb4d0c9e1df2db0304afa4d2c0f9e23da3a12567d8370c8470bb22e0e7cc34fbb358c0c1c3f5a6b7d6600daae5df933884d9057dae47057cfa060d594cf43bbe1e0dc550d5599949f7ea98aac4e14c40007f0676f7d7bbfdeea55af39713068508372dbce22b5b21e195cb607e9fa36ef12caef6972869a95d9ffa62c9ba58c07d9fb66bee30511a4d2c13c0cd3dc22989a7ecd98ff51d24a78364aee077447d464b99575808a513f932fb35a6b571a1c441daa63c3aa9f4cbb086e5d436cda63c9dba3fb5b6e508fb5f7f24af6b64e5c0dee70e86c5f50db5cf8eae277234fd40a19283ce2b90c414a00da2dbbccb6260268238894c73101dd64c9fef016d602ca72523a88db051d4af3a19e2645eba1567fbdedc02abd13d22acf5d838295b60c31fb7d543d10f4bbd79bef9a3821c6d8d018916496e07961514f7c968e165a640f32697a9e7bbf5d8ed2d8638f56d0ffec8dd8171482d5b43512245b17b689cbcd8acc784620fb738014c75f300e575da39d7d78b6f83c70e4b13bda17b1123714a4b56c12fa7929ac6774c92586fa44be2c8c3103be5ba1647da1ff89065ac20a1059cad488da9b6c5284e79e121615bd00b99c70d2e7dbb31ca196bbddc3668c282d405e4501753b749d2483a00fc486aa09146be106ef056997019bed9f6e59eae532abc16e51607c1523a468fb044b22af5d6a484961f548914306a4bcef32d0292664063f413a7519ffe79982375a9dd006bca067d5b60a377db2728d8ad63940bf0e8cd685271f401e1e99c3dfe4407475fb3466e17b60f677507ca2ed4d8342818117a223dbde3bf3a84137dbc6667fba6c4d702f14304561dcb2f6a04a256f63594588c0946d8aaed85f26aef9175cb068da02ffa8c46e4eded57b00b36be934ec7b439be04b1219f0a3f0ed0534be3488f5d2c4d8fb9d58e7cd6e48afa10dd2196ddd4239fb33f5aa1bbed7107077d1c64308a6f45b50eb78317d04126cdd5db384dd442cee46cc4c3c8f8843bce5a7d267a646d1c737519332bbd8c7af23b0f6eed0a8fa70154d2b2f5d2e2ad50d19215b1a1f502c2210bc82cc630117b33ad5d0850c9c12e75494e9390745c4925df21cc46f5289988340104fcaf86da46027adab8d04d785fe8e34dbbcb8af24598a74bdae54c3e4cce394c9452bb79816d4442725ef2161a9688c249780e8350158ff0d850282e70e132f02d2342398b98d8e261902fef3b89d458ca51348d4aec8551947bd70b3b36c73eff8d66425ad29d638f1037dcb816cd210bd0a1e27ca1e66ffd6e53034ca0d83bc6e9eaa51758ae7c3aeeb79c8441b8dce6fbdb53c998125ec5dc09dc4099df738577660b8e715ab1f8d1870d4c8abaf29f52e5de2de179e55aaf7e17efd1bd72bcb9d9d9003532a55e85a6388a5363dd78af922146e0b97d36f7c26112790408c8ed0c40ecbb27b77d1163abe0ff876df6e382adc9879ed9bc727abe7b7ec34aad9800ac5b2e53d9b2ba56e871f09d9e4c61f734f0031efc00f353933f85edebb3f26ddc6c4155d8323f0ea51f1632fb3f7514e0fa198992bdb98c8b7e0094d8b57fc5b6bf3490304b5d34060cba6391a28f516ffddf5149555f1784484e7b948092bb40c48b5c4a14327b7e9fb5beee87a83378e404389d5d3b4395c4576c8fffc86e20eec725527dcc392bee5018a4b17bc7971d56a8245a7b01d360b7d47c9a300f6e256908320c469c2491928bc4fe71ddf37c909017cc625515dabcdd6162bb62db61cf76d698fe046ee0e8b9a195e12f8629b2bbb8f8aeba957cc965de93f89c68fc12f89b18c0bc7582451d83c2906007b681fc21ef02f60e9557ee9de6a5f30bdbc222d1ef1b3369611feab9825450a6678c5bae1974b8ce94a88ee18ba282d20cb8962100ebde5c5e20e87e964910807c84d9c34a5ca7a9bd67a16a8251f2abdc1058800255f085245294a1a26692ed0619ae56aca33e18c180310d0f8834276e4c94d5d0a295d45b2a5775844f9e7c0f29053c7fe91e38492af88de2fafa7e3e77fe3b585205987e07c3557f9dcd0816741ab78971b266af70f3bf5ff4fae676434caba40ba5b67b09e3b23fb60b93a8a020350b8adf82c2c6dc2f247122f85fe9c32aa396fb79438857560df83d61e3fe43787d1f1a2034687fb2ccb44647e6edb6f33d735bb3ce6187c49b0edcede555cb91f8667a142cbadaf4b55ca22a328e51ee18bd73b70b68cbc9a616d345bcc26ecf18dc1f19f1cbc23fac2fbc0b4f2a256614d33b869a706ab625ee74edd0ddaddbe64026d3661d06fd60878be47274e28442cab040e5a43514c338eba1f0c805f461b739a8adcc7b787aca1f3a73c7dee92348aa8fda6f9e52ca8c3f05759c5233d3dd95c5bbedcbc8bfc8c1fa441a730f55fe11aa503cdc15ab747f100a2910d9790f98e9a09ea18729f0d1541185644b5420f6f4ac8e461e895d36894a4886392842a81695bbd79dd1000d46a06a0b5778da869b6948ab69de79177973d59d5d73589c26c12427b1a93c9806ed3953aeb957097e77e9e8717076b49dca3085676b59aa5a9d1b1537c65cb44dccf2e693d309a7e8ec5cafbdf400cc79cf3bc9f4fe19d974cad683715d34a38dd6c97fe84f9233a87ebff7c45a35ffa45cdc94e27f27a8c3088dcc01a2bc2666c085305d304f460c22b9024926199afa1211c614eeced2a141b0e7a4d68cd50779989d4b6ebdd90cf5e5db465cad7778e3eb0df9ed347ce63314ad81f1735ea988d3c38230ba31c434895b82ad3e12007e5ee291e772c08e3811b931c63e4023be658e57fe944a96853a314f81afeaafaaafd974d21462e2bd062e7e17e2f1e713

/-- `B` with diagonal 53,208 flipped. -/
def B' : Nat := B ^^^ 2 ^ 53208

theorem B_return : rowAt 53209 B 16 = B := by decide +kernel
theorem B'_return : rowAt 53209 B' 16 = B' := by decide +kernel

/-- The universal strip: diagonal `j` of `B`'s cycle at tick `t`. -/
def C (j t : Nat) : Bool := (rowAt 53209 B t).testBit j

theorem C_add_mul (j t q : Nat) : C j (t + q * 16) = C j t := by
  simp only [C]
  rw [rowAt_add_mul B_return]

theorem C_mod (j t : Nat) : C j t = C j (t % 16) := by
  have h := C_add_mul j (t % 16) (t / 16)
  rw [show t % 16 + t / 16 * 16 = t by omega] at h
  exact h

theorem C_step (j t : Nat) (hj : j + 2 < 53209) :
    C (j + 2) (t + 1) = xor (C j t) (C (j + 1) t || C (j + 2) t) := by
  simp only [C, rowAt]
  rw [stepK_bit_step hj]

theorem C_zero_phase : ∀ r, r < 16 → C 0 r = true := by decide +kernel
theorem C_one_phase : ∀ r, r < 16 → C 1 r = true := by decide +kernel

theorem C_zero (t : Nat) : C 0 t = true := by
  rw [C_mod]; exact C_zero_phase _ (Nat.mod_lt _ (by omega))

theorem C_one (t : Nat) : C 1 t = true := by
  rw [C_mod]; exact C_one_phase _ (Nat.mod_lt _ (by omega))

/-- The OR of the first `n` rows. -/
def orRows : Nat → Nat
  | 0 => 0
  | n + 1 => orRows n ||| rowAt 53209 B n

theorem orRows_black {n m : Nat} (h : (orRows n).testBit m = true) :
    ∃ r, r < n ∧ C m r = true := by
  induction n with
  | zero => simp [orRows] at h
  | succ n ih =>
    simp only [orRows, Nat.testBit_or, Bool.or_eq_true] at h
    rcases h with h | h
    · obtain ⟨r, hr, hc⟩ := ih h
      exact ⟨r, by omega, hc⟩
    · exact ⟨n, by omega, h⟩

/-- The white wheels below 53,207. -/
def whiteMask : Nat := 2 ^ 2 ||| 2 ^ 7 ||| 2 ^ 28 ||| 2 ^ 399

/-- Below 53,207 every wheel has a black at some phase, except the four. -/
theorem black_mask : (orRows 16 ||| whiteMask) % 2 ^ 53207 = 2 ^ 53207 - 1 := by decide +kernel

theorem black_or_white {m : Nat} (hm : m < 53207) :
    (∃ r, r < 16 ∧ C m r = true) ∨ m = 2 ∨ m = 7 ∨ m = 28 ∨ m = 399 := by
  have h := congrArg (fun n => n.testBit m) black_mask
  simp only [Nat.testBit_mod_two_pow, Nat.testBit_two_pow_sub_one, Nat.testBit_or, whiteMask,
    Nat.testBit_two_pow, hm, decide_true, Bool.true_and, Bool.or_eq_true, decide_eq_true_eq] at h
  rcases h with h | h
  · exact Or.inl (orRows_black h)
  · right
    omega

theorem blacks_late {m r : Nat} (hc : C m r = true) (T : Nat) : ∃ t, T ≤ t ∧ C m t = true :=
  ⟨r + T * 16, by omega, by rw [C_add_mul]; exact hc⟩

theorem strip_shift {m L : Nat}
    (h1 : ∀ r, r < 16 → rowAt 53209 B (r + L) % 2 ^ (m + 1) = rowAt 53209 B r % 2 ^ (m + 1))
    (h2 : ∀ r, r < 16 → C (m + 1) (r + L) = !C (m + 1) r) :
    (∀ j, j ≤ m → ∀ t, C j (t + L) = C j t) ∧ ∀ t, C (m + 1) (t + L) = !C (m + 1) t := by
  have ht : ∀ t, t + L = (t % 16 + L) + t / 16 * 16 := by intro t; omega
  constructor
  · intro j hj t
    have e := congrArg (fun n => n.testBit j) (h1 (t % 16) (Nat.mod_lt _ (by omega)))
    simp only [Nat.testBit_mod_two_pow, show j < m + 1 by omega, decide_true, Bool.true_and] at e
    rw [ht t, C_add_mul, C_mod j t]
    exact e
  · intro t
    rw [ht t, C_add_mul, C_mod (m + 1) t]
    exact h2 _ (Nat.mod_lt _ (by omega))

theorem per2 : ∀ r, r < 16 → rowAt 53209 B (r + 1) % 2 ^ 3 = rowAt 53209 B r % 2 ^ 3 := by decide +kernel
theorem anti2 : ∀ r, r < 16 → C 3 (r + 1) = !C 3 r := by decide +kernel
theorem per7 : ∀ r, r < 16 → rowAt 53209 B (r + 2) % 2 ^ 8 = rowAt 53209 B r % 2 ^ 8 := by decide +kernel
theorem anti7 : ∀ r, r < 16 → C 8 (r + 2) = !C 8 r := by decide +kernel
theorem per28 : ∀ r, r < 16 → rowAt 53209 B (r + 4) % 2 ^ 29 = rowAt 53209 B r % 2 ^ 29 := by decide +kernel
theorem anti28 : ∀ r, r < 16 → C 29 (r + 4) = !C 29 r := by decide +kernel
theorem per399 : ∀ r, r < 16 → rowAt 53209 B (r + 8) % 2 ^ 400 = rowAt 53209 B r % 2 ^ 400 := by decide +kernel
theorem anti399 : ∀ r, r < 16 → C 400 (r + 8) = !C 400 r := by decide +kernel

theorem strip_step (m : Nat) (hm : m + 1 ≤ 53207) : (∀ T, ∃ t, T ≤ t ∧ C m t = true) ∨
    ∃ L, (∀ j, j ≤ m → ∀ t, C j (t + L) = C j t) ∧ ∀ t, C (m + 1) (t + L) = !C (m + 1) t := by
  rcases black_or_white (m := m) (by omega) with ⟨r, _, hc⟩ | rfl | rfl | rfl | rfl
  · exact Or.inl (blacks_late hc)
  · exact Or.inr ⟨1, strip_shift per2 anti2⟩
  · exact Or.inr ⟨2, strip_shift per7 anti7⟩
  · exact Or.inr ⟨4, strip_shift per28 anti28⟩
  · exact Or.inr ⟨8, strip_shift per399 anti399⟩

/-- **One left side.** Every recurrence array with a black wheel 0 (every configuration with a leftmost black
cell, whatever lies to its right) has, after one time shift, the strip's words on all wheels through 53,207. -/
theorem universal_strip {a : Nat → Nat → Bool} (ha : Recurrence a) (ha0 : a 0 0 = true) :
    ∃ s, ∀ j, j ≤ 53207 → ∃ T, ∀ t, T ≤ t → a j (t + s) = C j t :=
  universal_of_strip (J := 53207) (by omega) ha ha0 C_zero C_one
    (fun j t hj => C_step j t (by omega)) strip_step

theorem universal_left_side {x : Int → Bool} {lo : Int} (hleft : ∀ p, p < lo → x p = false)
    (hlo : x lo = true) :
    ∃ s, ∀ j, j ≤ 53207 → ∃ T, ∀ t, T ≤ t → Ld x lo j (t + s) = C j t := by
  refine universal_strip (Ld_recurrence hleft) ?_
  simpa [Ld, evol] using hlo

theorem D_recurrence : Recurrence D :=
  ⟨fun t => by rw [D_zero, D_zero], fun t => by rw [D_one, D_zero]; rfl, D_step⟩

/-- The single seed's left diagonals are the strip's, up to one shift. -/
theorem seed_left_side : ∃ s, ∀ j, j ≤ 53207 → ∃ T, ∀ t, T ≤ t → D j (t + s) = C j t :=
  universal_strip D_recurrence (D_zero 0)

/-! ### Any two rows -/

/-- **One left side, for any two arrays.** -/
theorem same_left_side {a b : Nat → Nat → Bool} (ha : Recurrence a) (ha0 : a 0 0 = true)
    (hb : Recurrence b) (hb0 : b 0 0 = true) :
    ∃ s, ∀ j, j ≤ 53207 → ∃ T, ∀ t, T ≤ t → a j (t + s) = b j t := by
  obtain ⟨sa, hsa⟩ := universal_strip ha ha0
  obtain ⟨sb, hsb⟩ := universal_strip hb hb0
  refine ⟨sa + 15 * sb, fun j hj => ?_⟩
  obtain ⟨Ta, hTa⟩ := hsa j hj
  obtain ⟨Tb, hTb⟩ := hsb j hj
  refine ⟨Ta + Tb + sb, fun t ht => ?_⟩
  obtain ⟨u, rfl⟩ : ∃ u, t = u + sb := ⟨t - sb, by omega⟩
  rw [hTb u (by omega), show u + sb + (sa + 15 * sb) = (u + sb * 16) + sa by omega,
    hTa _ (by omega), C_add_mul]

/-- **One left side, for any two configurations with a leftmost black cell.** -/
theorem one_left_side {x y : Int → Bool} {lx ly : Int} (hx : ∀ p, p < lx → x p = false)
    (hx0 : x lx = true) (hy : ∀ p, p < ly → y p = false) (hy0 : y ly = true) :
    ∃ s, ∀ j, j ≤ 53207 → ∃ T, ∀ t, T ≤ t → Ld x lx j (t + s) = Ld y ly j t :=
  same_left_side (Ld_recurrence hx) (by simpa [Ld, evol] using hx0)
    (Ld_recurrence hy) (by simpa [Ld, evol] using hy0)

/-! ### The first fork -/

theorem C_white_phase : ∀ r, r < 16 → C 53207 r = false := by decide +kernel

theorem C_white (t : Nat) : C 53207 t = false := by
  rw [C_mod]; exact C_white_phase _ (Nat.mod_lt _ (by omega))

/-- **At wheel 53,208 there are exactly two continuations.** With the shift that matches every lower wheel, wheel
53,208 of every array is eventually the strip's word or its complement. -/
theorem fork_dichotomy {a : Nat → Nat → Bool} (ha : Recurrence a) (ha0 : a 0 0 = true) :
    ∃ s, (∀ j, j ≤ 53207 → ∃ T, ∀ t, T ≤ t → a j (t + s) = C j t) ∧
      ((∃ T, ∀ t, T ≤ t → a 53208 (t + s) = C 53208 t) ∨
        (∃ T, ∀ t, T ≤ t → a 53208 (t + s) = !C 53208 t)) := by
  obtain ⟨s, hs⟩ := universal_strip ha ha0
  refine ⟨s, hs, ?_⟩
  obtain ⟨T1, h1⟩ := hs 53206 (by omega)
  obtain ⟨T2, h2⟩ := hs 53207 (by omega)
  rcases child_white (k := 53206) (s := s) (T := max T1 T2) ha
    (fun t => C_step 53206 t (by omega)) (fun t ht => h1 t (by omega))
    (fun t ht => h2 t (by omega)) (fun t _ => C_white t) with h | h
  · exact Or.inl ⟨_, h⟩
  · exact Or.inr ⟨_, h⟩

/-- The other row's strip. -/
def C' (j t : Nat) : Bool := (rowAt 53209 B' t).testBit j

theorem C'_add_mul (j t q : Nat) : C' j (t + q * 16) = C' j t := by
  simp only [C']
  rw [rowAt_add_mul B'_return]

theorem C'_mod (j t : Nat) : C' j t = C' j (t % 16) := by
  have h := C'_add_mul j (t % 16) (t / 16)
  rw [show t % 16 + t / 16 * 16 = t by omega] at h
  exact h

theorem low_phase : ∀ r, r < 16 → rowAt 53209 B' r % 2 ^ 53208 = rowAt 53209 B r % 2 ^ 53208 := by
  decide +kernel
theorem top_phase : ∀ r, r < 16 → C' 53208 r = !C 53208 r := by decide +kernel

theorem C'_low {j : Nat} (hj : j ≤ 53207) (t : Nat) : C' j t = C j t := by
  have e := congrArg (fun n => n.testBit j) (low_phase (t % 16) (Nat.mod_lt _ (by omega)))
  simp only [Nat.testBit_mod_two_pow, show j < 53208 by omega, decide_true, Bool.true_and] at e
  rw [C'_mod, C_mod j t]
  exact e

theorem C'_top (t : Nat) : C' 53208 t = !C 53208 t := by
  rw [C'_mod, C_mod 53208 t]
  exact top_phase _ (Nat.mod_lt _ (by omega))

/-- Wheel 400's word has no proper period, so a shift fixing the low wheels is a multiple of 16. -/
theorem wheel400_primitive : ∀ d, d < 16 → d ≠ 0 → ∃ p, p < 16 ∧ C 400 (p + d) ≠ C 400 p := by
  decide +kernel

theorem no_shift : ¬ ∃ s, ∀ j, j ≤ 53208 → ∃ T, ∀ t, T ≤ t → C' j (t + s) = C j t := by
  rintro ⟨s, hs⟩
  obtain ⟨T1, h400⟩ := hs 400 (by omega)
  obtain ⟨T2, htop⟩ := hs 53208 (by omega)
  by_cases hd : s % 16 = 0
  · have e := htop T2 (Nat.le_refl _)
    rw [C'_top] at e
    have p : C 53208 (T2 + s) = C 53208 T2 := by
      have h := C_add_mul 53208 T2 (s / 16)
      rwa [show T2 + s / 16 * 16 = T2 + s by omega] at h
    rw [p] at e
    cases h : C 53208 T2 <;> simp [h] at e
  · obtain ⟨p, hp, hne⟩ := wheel400_primitive (s % 16) (Nat.mod_lt _ (by omega)) hd
    have e := h400 (p + T1 * 16) (by omega)
    rw [C'_low (by omega)] at e
    have e1 : C 400 (p + T1 * 16 + s) = C 400 (p + s % 16) := by
      have h := C_add_mul 400 (p + s % 16) (T1 + s / 16)
      rwa [show p + s % 16 + (T1 + s / 16) * 16 = p + T1 * 16 + s by omega] at h
    rw [e1, C_add_mul] at e
    exact hne e

theorem Ld_B {j : Nat} (hj : j ≤ 53208) (t : Nat) : Ld (ofRow B) 0 j t = C j t :=
  Ld_ofRow (K := 53209) (by omega) B t j (by omega)

theorem Ld_B' {j : Nat} (hj : j ≤ 53208) (t : Nat) : Ld (ofRow B') 0 j t = C' j t :=
  Ld_ofRow (K := 53209) (by omega) B' t j (by omega)

theorem B_lt : B < 2 ^ 53209 := by decide +kernel
theorem B'_lt : B' < 2 ^ 53209 := by decide +kernel
theorem B_bit : B.testBit 0 = true := by decide +kernel
theorem B'_bit : B'.testBit 0 = true := by decide +kernel

/-- **The first fork is realized.** Two finite rows, each with its leftmost black cell at position 0, agree on every left
diagonal through 53,207 at every tick, are complementary on diagonal 53,208 at every tick, and no time shift makes diagonal
53,208 and the lower ones agree. -/
theorem first_fork :
    (∀ j, j ≤ 53207 → ∀ t, Ld (ofRow B') 0 j t = Ld (ofRow B) 0 j t) ∧
    (∀ t, Ld (ofRow B') 0 53208 t = !Ld (ofRow B) 0 53208 t) ∧
    ¬ ∃ s, ∀ j, j ≤ 53208 → ∃ T, ∀ t, T ≤ t → Ld (ofRow B') 0 j (t + s) = Ld (ofRow B) 0 j t := by
  refine ⟨fun j hj t => ?_, fun t => ?_, ?_⟩
  · rw [Ld_B' (by omega), Ld_B (by omega), C'_low hj]
  · rw [Ld_B' (by omega), Ld_B (by omega), C'_top]
  · rintro ⟨s, hs⟩
    refine no_shift ⟨s, fun j hj => ?_⟩
    obtain ⟨T, hT⟩ := hs j hj
    refine ⟨T, fun t ht => ?_⟩
    have := hT t ht
    rwa [Ld_B' hj, Ld_B hj] at this

/-! ### Rowland's parity condition, read off the strip -/

/-- The number of blacks of wheel `m` over the first `L` phases of the strip. -/
def weight (m : Nat) : Nat → Nat
  | 0 => 0
  | L + 1 => weight m L + (C m L).toNat

/-- The farther parents of the four odd white wheels have odd weight over the common period: 1, 1, 3, 3. -/
theorem odd_farther_weights :
    weight 1 1 = 1 ∧ weight 6 2 = 1 ∧ weight 27 4 = 3 ∧ weight 398 8 = 3 := by decide +kernel

/-- The farther parent of wheel 53,207 has even weight, 6 over the period 16: Rowland's first even case. -/
theorem even_farther_weight : weight 53206 16 = 6 := by decide +kernel

#print axioms universal_left_side
#print axioms one_left_side
#print axioms seed_left_side
#print axioms fork_dichotomy
#print axioms first_fork
#print axioms odd_farther_weights
#print axioms even_farther_weight

end Rule30UniversalLeftSide
