---
Template: ComputationalEssay
Name: Telling left edges apart from the center column: exact deadlines for three edge pairs
Author: Gareth Herbert - with Claude (Anthropic) and GPT (OpenAI)
Date: 2026-10-24
Description: A partial result on the trace-edge conjecture of the Rule 30 Prize kit, proved in Lean against the official definitions: two configurations of rule 30 whose leftmost black cells sit at -2 and -1 have center columns that differ by time 8; at -4 and -3 by time 13; at -3 and -2 by time 14; each bound is attained. The right side is unrestricted.
Abstract: For any two configurations x, y of rule 30 whose leftmost black cells sit at -2 and -1, the center columns differ at some time t <= 8 (sep_8); for leftmost black cells at -4 and -3 by time 13 (sep_13), at -3 and -2 by time 14 (sep_14); each bound is attained (attained_8, attained_13, attained_14). The right side is unrestricted, finite or infinite. The kit's later module Rule30TraceEdge names the conjecture that two finite configurations with the same complete center trace have the same left edge and proves that it implies Problem 1; these are its first instances, with exact deadlines, for every configuration with those edges. The center through time m depends on the initial cells at positions at most m only, so a configuration is cut to the window [a, m]; the 2^(m - a) fillings with a black cell at a run as lanes of one number, the signatures of each edge class are collected into a bitset, and the bitsets are disjoint, checked by the kernel in blocks of 256 values. Nothing is claimed about the general conjecture or Problem 1.
Keywords: [rule 30, Rule 30 Prize, Problem 1, left edge, center trace, light cone, lanes, kernel certificate, Lean 4, LeanLink]
Sources: ["[The Rule 30 Prize kit](https://github.com/WolframInstitute/Rule30PrizeKit)", "[The Wolfram · Collatz · Mahler record](https://github.com/ghywel/placego)"]
Links: ["[Rule 30 Prizes](https://rule30prize.org/)", "[wolframcollatzmahler.com](https://www.wolframcollatzmahler.com)", "[Rule30TraceEdge in the kit](https://github.com/WolframInstitute/Rule30PrizeKit/blob/main/lean/Ruliology/CellularAutomata/Rule30TraceEdge.lean)"]
---

## The question

Run rule 30 from any configuration with a leftmost black cell. The edge moves left one cell per step, and the center column records what it sees. Does the center column know where the edge was? The kit's module `Rule30TraceEdge` (added after the verifier's pinned commit) states the conjecture `EdgeObservable`: two finite configurations with the same complete center trace have the same left edge; and it proves that the conjecture implies Problem 1 in full. Nobody has proved the conjecture. Here are its first instances, exact: for leftmost black cells at `-2` and `-1` the center columns differ by time `8`; at `-4` and `-3` by time `13`; at `-3` and `-2` by time `14`; and each deadline is attained. The theorems hold for every configuration with those edges, finite or not, which is more than the conjecture asks on these instances.

## Three pairs that agree as long as possible

The attaining pairs. Each line is a configuration written from its leftmost black cell; the center columns agree for exactly the stated number of steps and then differ:

```wl
run[cells_, lo_, T_] := Module[{w = cells, l = lo, out = {}}, Do[AppendTo[out, If[1 <= 1 - l <= Length[w], w[[1 - l]], 0]]; w = With[{z = Join[{0, 0}, w, {0, 0}]}, Table[BitXor[z[[i - 1]], BitOr[z[[i]], z[[i + 1]]]], {i, 2, Length[z] - 1}]]; l = l - 1, {T}]; out];
pairs = {{-2, {1, 0, 0, 1, 1, 0, 1, 0, 0}, -1, {1, 0, 0, 1, 0, 0, 0, 1}, 8}, {-4, {1, 1, 1, 0, 1, 1, 0, 1}, -3, {1, 1, 0, 1, 0, 0, 1, 0, 0, 1}, 13}, {-3, {1, 0, 0, 0, 1}, -2, {1, 1, 0, 0, 0, 0, 1}, 14}};
Table[With[{ta = run[p[[2]], p[[1]], p[[5]] + 1], tb = run[p[[4]], p[[3]], p[[5]] + 1]}, {p[[1]], p[[3]], ta, tb, First[Position[MapThread[UnsameQ, {ta, tb}], True]][[1]] - 1}], {p, pairs}]
```

So the pair with edges `-2` and `-1` agrees at times `0` to `7` and differs at `8`, and likewise `13` and `14` for the other two pairs.

## Why a finite search settles an infinite question

The center cell at time `t` depends only on the initial cells at positions `-t` to `t`. So if two configurations with edges `a` and `b` agree on the center through time `m`, cutting both at any position `R >= m` preserves that agreement. Conversely, if an exhaustive search over the window `[a, R]` finds that no pair of edges `a`, `b` agrees through time `m`, and `R >= m`, then no pair at all does: a longer-agreeing pair would cut down to one in the window. The search is run as lanes, every filling of the window as one bit of a big integer:

```wl
pat[n_, s_] := FromDigits[Table[BitGet[l, s], {l, 2^n - 1, 0, -1}], 2];
laneWords[a_, R_, m_] := With[{n = R - a}, Table[Which[p < a || p > R, 0, p == a, 2^2^n - 1, True, pat[n, p - a - 1]], {p, -m, m}]];
stepLanes[w_] := With[{z = Join[{0}, w, {0}]}, Table[BitXor[z[[i - 1]], BitOr[z[[i]], z[[i + 1]]]], {i, 2, Length[z] - 1}]];
centers[a_, R_, m_] := Module[{w = laneWords[a, R, m], c = {}}, Do[AppendTo[c, w[[m + 1]]]; w = stepLanes[w], {m + 1}]; c];
sigs[c_, n_] := Union[Table[Table[BitGet[c[[t]], l], {t, Length[c]}], {l, 0, 2^n - 1}]];
longest[a_, b_, R_, m_] := Module[{sa = sigs[centers[a, R, m], R - a], sb = sigs[centers[b, R, m], R - b], k = m + 1}, While[k > 0 && Intersection[Take[#, k] & /@ sa, Take[#, k] & /@ sb] === {}, k--]; k];
{Table[longest[-2, -1, R, 10], {R, {6, 8, 10}}], longest[-4, -3, 13, 13], longest[-3, -2, 14, 14]}
```

The longest agreement for edges `-2`, `-1` is `8` whether the window ends at `6`, `8` or `10`: the maximum has saturated, and since `10 >= 8` it is the maximum over every configuration. For edges `-4`, `-3` the window `[a, 13]` gives `13`, and for `-3`, `-2` the window `[a, 14]` gives `14`; both windows reach their own answer, so both are exact.

## The idea of the proof

1. **Locality.** The kit's `evol_local_le`: two configurations that agree on every position `<= b` have the same evolution at `(t, p)` whenever `p + t <= b`. A configuration with its edge at `a` agrees with its own window `[a, m]` filling on every position `<= m` (white left of the edge, equal inside), so its center through time `m` is the window's (`center_eq_lane`).
2. **Lanes.** The window fillings are the numbers `2 l + 1`, `l < 2^(m - a)`: the edge cell black, the free bits the bits of `l`. The lane words `initWords` hold, at each position, the bits of every filling at once; one step of rule 30 on all lanes is `l XOR (c OR r)` on the words (`stepW`, `stepL`), and the invariant `laneInv` says bit `l` of the word at position `p` after `t` steps is the evolution of filling `l` (`laneInv_step`, `centers_spec`).
3. **Signatures.** The signature of a configuration is its center cells at times `0` to `m` as the bits of a number (`sig`). For each value `v`, `memb` ANDs the center words or their complements and is nonzero exactly when some lane has signature `v`; `sigSet` collects the values into a bitset. `memb_block` puts the signature of every configuration with edge `a` into the bitset of its class.
4. **Disjointness, in blocks.** The two classes' bitsets share no bit. The kernel checks this in blocks of `256` values (`partSet`, `BlocksDisjoint`), one theorem per block, because the Lean kernel keeps every intermediate word in a cache that lives for one declaration: a single loop over all `32768` values at `m = 14` exhausted memory. `separationB` turns the block facts into the theorem.
5. **Attainment.** `witCheck` has the kernel compare two named lanes at every time, and `attained` turns a passing check into two explicit configurations with the given edges that agree before `m` and differ at `m`.

## The formal proof

The module, built against the kit at the verifier's commit:

```wl
Needs["Wolfram`LeanLink`"];
$Rule30PrizeKit = Environment["RULE30PRIZE_KIT"];
DirectoryQ[$Rule30PrizeKit]
```

```wl
rule30Submission = LeanImportString["import Rule30PrizeKit
import Ruliology.CellularAutomata.Rule30ZeroBoundaryBarriers
import Ruliology.CellularAutomata.Rule30ZeroBoundaryLanes

/-!
# Fixed-edge instances of the trace-edge question, by exhaustive lane certificates

For two configurations with leftmost black cells at `a < b < 0`, the center columns differ by
time `m`: `M(-2,-1) = 8`, `M(-3,-2) = 14`, `M(-4,-3) = 13`, each attained. The right side is
unrestricted (finite or not): the center through time `m` depends on positions `<= m` only
(`evol_local_le`), so the configuration may be truncated to the window `[a, m]`, whose `2^(m-a)`
fillings with a black cell at `a` are run as lanes; the sets of center signatures (times `0..m`)
of the two edge classes are shown disjoint by one `Nat.land`.
-/

namespace Rule30Submission
open Ruliology.CellularAutomata Rule30Jen Rule30Realization

/-! ## 1. Forcing (the kernel is lazy) -/

noncomputable def force {α : Sort u} (n : Nat) (k : Nat → α) : α :=
  Nat.casesOn (motive := fun _ => α) n (k 0) (fun m => k (Nat.succ m))

theorem force_eq {α : Sort u} (n : Nat) (k : Nat → α) : force n k = k n :=
  match n with
  | 0 => rfl
  | _ + 1 => rfl

/-- Force every entry of a list of lane words, then continue. -/
noncomputable def forceL {α : Sort u} : List Nat → (List Nat → α) → α
  | [], k => k []
  | n :: ns, k => force n fun n' => forceL ns fun ns' => k (n' :: ns')

theorem forceL_eq {α : Sort u} : ∀ (l : List Nat) (k : List Nat → α), forceL l k = k l
  | [], _ => rfl
  | n :: ns, k =>
    (force_eq n (fun n' => forceL ns fun ns' => k (n' :: ns'))).trans
      (forceL_eq ns (fun ns' => k (n :: ns')))

/-! ## 2. Bitwise rule 30 on lane words -/

def stepW (l c r : Nat) : Nat := Nat.xor l (Nat.lor c r)

theorem stepW_testBit (l c r i : Nat) :
    (stepW l c r).testBit i = rule (l.testBit i) (c.testBit i) (r.testBit i) := by
  unfold stepW rule
  rw [show Nat.xor l (Nat.lor c r) = l ^^^ (c ||| r) from rfl, Nat.testBit_xor, Nat.testBit_or]

/-- One step on a list of lane words: entry `i` from entries `i - 1`, `i`, `i + 1` (zero outside).
`prev` is the entry before the first of `l`. -/
def stepL (prev : Nat) : List Nat → List Nat
  | [] => []
  | c :: rest => stepW prev c (rest.headD 0) :: stepL c rest

theorem stepL_length (prev : Nat) : ∀ l : List Nat, (stepL prev l).length = l.length
  | [] => rfl
  | _ :: rest => by simp [stepL, stepL_length _ rest]

theorem stepL_getD (prev : Nat) : ∀ (l : List Nat) (i : Nat), i < l.length →
    (stepL prev l).getD i 0 =
      stepW (if i = 0 then prev else l.getD (i - 1) 0) (l.getD i 0) (l.getD (i + 1) 0)
  | [], i, h => by simp at h
  | c :: rest, 0, _ => by
    simp [stepL, List.getD_cons_zero]
    cases rest <;> rfl
  | c :: rest, i + 1, h => by
    simp only [stepL, List.getD_cons_succ]
    rw [stepL_getD c rest i (by simpa using h)]
    simp only [Nat.add_one_ne_zero, ↓reduceIte, Nat.add_sub_cancel]
    cases i <;> simp [List.getD_cons_zero, List.getD_cons_succ]

/-! ## 3. Window configurations and the lane invariant -/

/-- The configuration read from code `n` on the window `[a, a + w)`: position `a + i` holds bit `i`. -/
def cfg (a : Int) (w n : Nat) : Int → Bool :=
  fun p => if a ≤ p ∧ p < a + w then n.testBit (p - a).toNat else false

/-- Lane words for the window `[lo, lo + len)`: `word i` is the lane word at position `lo + i`. -/
def laneInv (lo : Int) (t : Nat) (words : List Nat) (lanes : Nat) (code : Nat → Nat)
    (a : Int) (w : Nat) : Prop :=
  ∀ (i : Nat) (ℓ : Nat), ℓ < lanes → t ≤ i → i + t < words.length →
    (words.getD i 0).testBit ℓ = evol (cfg a w (code ℓ)) t (lo + i)

/-- One step preserves the invariant with the usable region shrinking by one on each side. -/
theorem laneInv_step (lo : Int) (t : Nat) (words : List Nat) (lanes : Nat) (code : Nat → Nat)
    (a : Int) (w : Nat) (h : laneInv lo t words lanes code a w) :
    laneInv lo (t + 1) (stepL 0 words) lanes code a w := by
  intro i ℓ hℓ hi hlen
  rw [stepL_length] at hlen
  rw [stepL_getD 0 words i (by omega)]
  have hi0 : i ≠ 0 := by omega
  simp only [hi0, ↓reduceIte]
  rw [stepW_testBit, Rule30ZeroBoundaryBarriers.evol_succ]
  rw [h (i - 1) ℓ hℓ (by omega) (by omega), h i ℓ hℓ (by omega) (by omega),
    h (i + 1) ℓ hℓ (by omega) (by omega)]
  congr 2 <;> push_cast <;> omega

/-- `t` steps, applied at the base: `iter (t + 1) w = iter t (stepL 0 w)`. -/
def iter : Nat → List Nat → List Nat
  | 0, w => w
  | t + 1, w => iter t (stepL 0 w)

theorem iter_succ' : ∀ (t : Nat) (w : List Nat), iter (t + 1) w = stepL 0 (iter t w)
  | 0, _ => rfl
  | t + 1, w => by rw [iter, iter_succ' t (stepL 0 w)]; rfl

theorem iter_length : ∀ (t : Nat) (w : List Nat), (iter t w).length = w.length
  | 0, _ => rfl
  | t + 1, w => by rw [iter, iter_length t, stepL_length]

theorem laneInv_iter (lo : Int) (words : List Nat) (lanes : Nat) (code : Nat → Nat) (a : Int)
    (w : Nat) (h : laneInv lo 0 words lanes code a w) :
    ∀ t, laneInv lo t (iter t words) lanes code a w := by
  intro t
  induction t with
  | zero => exact h
  | succ t ih =>
    rw [iter_succ']
    exact laneInv_step lo t _ lanes code a w ih


/-! ## 4. The initial lane words: window `[-m, m]`, edge at index `d` (position `d - m`), `2^n` lanes with `n = 2m - d` -/

/-- Lane word at index `i`: white left of the edge, all lanes black at the edge, then the lane
patterns of the free bits. -/
def initWord (d n i : Nat) : Nat :=
  if i < d then 0 else if i = d then 2 ^ 2 ^ n - 1 else Rule30ZeroBoundaryLanes.pat n (i - d - 1)

def initWords (m d n : Nat) : List Nat := (List.range (2 * m + 1)).map (initWord d n)

theorem initWords_length (m d n : Nat) : (initWords m d n).length = 2 * m + 1 := by
  simp [initWords]

theorem initWords_getD (m d n i : Nat) (hi : i < 2 * m + 1) :
    (initWords m d n).getD i 0 = initWord d n i := by
  rw [initWords, List.getD_eq_getElem?_getD, List.getElem?_map, List.getElem?_range hi]
  rfl

/-- Lane `ℓ` carries the window code `2 ℓ + 1`: the edge cell black, the free bits the bits of `ℓ`. -/
def laneCode (ℓ : Nat) : Nat := 2 * ℓ + 1

theorem laneCode_testBit_zero (ℓ : Nat) : (laneCode ℓ).testBit 0 = true := by
  simp [laneCode, Nat.testBit_zero]

theorem laneCode_testBit_succ (ℓ j : Nat) : (laneCode ℓ).testBit (j + 1) = ℓ.testBit j := by
  rw [laneCode, Nat.testBit_add_one, show (2 * ℓ + 1) / 2 = ℓ by omega]

/-- The invariant holds at time `0`: the lane words read the window configurations. -/
theorem laneInv_init (m d : Nat) (hd : d ≤ 2 * m) :
    laneInv (-(m : Int)) 0 (initWords m d (2 * m - d)) (2 ^ (2 * m - d)) laneCode
      ((d : Int) - m) (2 * m + 1 - d) := by
  intro i ℓ hℓ _ hlen
  rw [initWords_length] at hlen
  rw [initWords_getD m d _ i hlen]
  simp only [evol, cfg]
  by_cases hid : i < d
  · have : ¬ ((d : Int) - m ≤ -(m : Int) + i) := by omega
    simp [initWord, hid, this]
  · have h1 : (d : Int) - m ≤ -(m : Int) + i := by omega
    have h2 : -(m : Int) + i < (d : Int) - m + ((2 * m + 1 - d : Nat) : Int) := by omega
    have h3 : (-(m : Int) + i - ((d : Int) - m)).toNat = i - d := by omega
    simp only [h1, h2, and_self, ↓reduceIte, h3]
    by_cases hid2 : i = d
    · subst hid2
      rw [Nat.sub_self, laneCode_testBit_zero]
      simp [initWord, Nat.testBit_two_pow_sub_one, hℓ]
    · have hgt : d < i := by omega
      obtain ⟨j, rfl⟩ : ∃ j, i = d + j + 1 := ⟨i - d - 1, by omega⟩
      simp only [initWord, hid, ↓reduceIte, hid2, show d + j + 1 - d - 1 = j by omega,
        show d + j + 1 - d = j + 1 by omega, laneCode_testBit_succ]
      exact Rule30ZeroBoundaryLanes.pat_spec _ j ℓ (by omega) hℓ

/-! ## 5. The center words `C_0, …, C_m`, with forcing -/

/-- The center words for times `0..k`, each row forced before the next step. -/
noncomputable def centers (m : Nat) : Nat → List Nat → List Nat :=
  Nat.rec (motive := fun _ => List Nat → List Nat)
    (fun words => [words.getD m 0])
    (fun _ ih words => words.getD m 0 :: forceL (stepL 0 words) ih)

theorem centers_zero (m : Nat) (words : List Nat) : centers m 0 words = [words.getD m 0] := rfl

theorem centers_succ (m k : Nat) (words : List Nat) :
    centers m (k + 1) words = words.getD m 0 :: centers m k (stepL 0 words) := by
  show words.getD m 0 :: forceL (stepL 0 words) (centers m k) = _
  rw [forceL_eq]

theorem centers_getD (m : Nat) : ∀ (k : Nat) (words : List Nat) (t : Nat), t ≤ k →
    (centers m k words).getD t 0 = (iter t words).getD m 0
  | 0, words, 0, _ => rfl
  | 0, _, t + 1, h => by omega
  | k + 1, words, 0, _ => by rw [centers_succ]; rfl
  | k + 1, words, t + 1, h => by
    rw [centers_succ, List.getD_cons_succ, centers_getD m k _ t (by omega)]
    rfl

/-- **The center bits are the evolutions.** For `t ≤ m` and lane `ℓ`, bit `ℓ` of the center word at
time `t` is the center cell of the window configuration of lane `ℓ` at time `t`. -/
theorem centers_spec (m d : Nat) (hd : d ≤ 2 * m) (t ℓ : Nat) (ht : t ≤ m)
    (hℓ : ℓ < 2 ^ (2 * m - d)) :
    ((centers m m (initWords m d (2 * m - d))).getD t 0).testBit ℓ =
      evol (cfg ((d : Int) - m) (2 * m + 1 - d) (laneCode ℓ)) t 0 := by
  rw [centers_getD m m _ t ht]
  have h := laneInv_iter (-(m : Int)) _ _ laneCode _ _ (laneInv_init m d hd) t m ℓ hℓ ht
    (by rw [iter_length, initWords_length]; omega)
  rw [h]
  congr 1
  omega

/-! ## 6. Signature sets -/

/-- The lanes whose signature on times `0..k` is the bit string `v`: an AND of the center words or
their complements. -/
noncomputable def memb (ALL : Nat) (C : List Nat) (v : Nat) : Nat → Nat
  | 0 => ALL
  | k + 1 => Nat.land (memb ALL C v k)
      (cond (v.testBit k) (C.getD k 0) (Nat.xor (C.getD k 0) ALL))

theorem memb_testBit (ALL : Nat) (C : List Nat) (v : Nat) (ℓ : Nat) (hALL : ALL.testBit ℓ = true) :
    ∀ k, (∀ t, t < k → (C.getD t 0).testBit ℓ = v.testBit t) → (memb ALL C v k).testBit ℓ = true
  | 0, _ => hALL
  | k + 1, h => by
    simp only [memb]
    rw [show Nat.land (memb ALL C v k) _ = memb ALL C v k &&& _ from rfl, Nat.testBit_and,
      memb_testBit ALL C v ℓ hALL k (fun t ht => h t (by omega))]
    have hk := h k (by omega)
    cases hv : v.testBit k
    · rw [hv] at hk
      simp only [Bool.cond_false]
      rw [show Nat.xor (C.getD k 0) ALL = C.getD k 0 ^^^ ALL from rfl, Nat.testBit_xor, hk, hALL]
      rfl
    · rw [hv] at hk
      simp only [Bool.cond_true, hk]
      rfl

/-- The signature bitset, accumulator-passing so the kernel runs it as a loop: `fuel` more values
from `v`, bits already collected in `acc`; bit `u` is set when some lane has signature `u`. -/
noncomputable def sigSet (ALL : Nat) (C : List Nat) (m : Nat) : Nat → Nat → Nat → Nat :=
  Nat.rec (motive := fun _ => Nat → Nat → Nat) (fun _ acc => acc)
    (fun _ ih v acc => force (memb ALL C v (m + 1)) fun mv =>
      force (Nat.lor acc (cond (Nat.beq mv 0) 0 (Nat.shiftLeft 1 v))) fun acc' =>
        ih (Nat.add v 1) acc')

theorem sigSet_zero (ALL : Nat) (C : List Nat) (m v acc : Nat) : sigSet ALL C m 0 v acc = acc := rfl

theorem sigSet_succ (ALL : Nat) (C : List Nat) (m fuel v acc : Nat) :
    sigSet ALL C m (fuel + 1) v acc =
      sigSet ALL C m fuel (v + 1)
        (Nat.lor acc (cond (Nat.beq (memb ALL C v (m + 1)) 0) 0 (Nat.shiftLeft 1 v))) := by
  show force (memb ALL C v (m + 1)) (fun mv =>
      force (Nat.lor acc (cond (Nat.beq mv 0) 0 (Nat.shiftLeft 1 v))) fun acc' =>
        sigSet ALL C m fuel (Nat.add v 1) acc') = _
  rw [force_eq, force_eq]

theorem sigSet_mono (ALL : Nat) (C : List Nat) (m : Nat) :
    ∀ (fuel v acc u : Nat), acc.testBit u = true → (sigSet ALL C m fuel v acc).testBit u = true
  | 0, _, _, _, h => h
  | fuel + 1, v, acc, u, h => by
    rw [sigSet_succ]
    apply sigSet_mono
    rw [show Nat.lor acc _ = acc ||| _ from rfl, Nat.testBit_or, h]
    rfl

theorem sigSet_testBit (ALL : Nat) (C : List Nat) (m : Nat) :
    ∀ (fuel v acc u : Nat), v ≤ u → u < v + fuel → memb ALL C u (m + 1) ≠ 0 →
      (sigSet ALL C m fuel v acc).testBit u = true
  | 0, v, _, u, h1, h2, _ => by omega
  | fuel + 1, v, acc, u, h1, h2, hne => by
    rw [sigSet_succ]
    by_cases huv : u = v
    · subst huv
      apply sigSet_mono
      have : Nat.beq (memb ALL C u (m + 1)) 0 = false := by
        cases h : Nat.beq (memb ALL C u (m + 1)) 0
        · rfl
        · exact absurd (Nat.eq_of_beq_eq_true h) hne
      rw [this]
      simp only [Bool.cond_false]
      rw [show Nat.lor acc (Nat.shiftLeft 1 u) = acc ||| 1 <<< u from rfl, Nat.testBit_or,
        Nat.testBit_shiftLeft]
      simp
    · exact sigSet_testBit ALL C m fuel (v + 1) _ u (by omega) (by omega) hne

/-- Bits of a signature set computed from an empty accumulator lie in the range of values visited. -/
theorem sigSet_range (ALL : Nat) (C : List Nat) (m : Nat) :
    ∀ (fuel v acc u : Nat), (sigSet ALL C m fuel v acc).testBit u = true →
      acc.testBit u = true ∨ (v ≤ u ∧ u < v + fuel)
  | 0, v, acc, u, h => Or.inl h
  | fuel + 1, v, acc, u, h => by
    rw [sigSet_succ] at h
    rcases sigSet_range ALL C m fuel (v + 1) _ u h with h1 | h1
    · rw [show Nat.lor acc _ = acc ||| _ from rfl, Nat.testBit_or] at h1
      cases hb : acc.testBit u
      · rw [hb] at h1
        simp only [Bool.false_or] at h1
        cases hc : Nat.beq (memb ALL C v (m + 1)) 0
        · rw [hc] at h1
          simp only [Bool.cond_false] at h1
          rw [show Nat.shiftLeft 1 v = 1 <<< v from rfl, Nat.testBit_shiftLeft] at h1
          cases hdv : decide (u ≥ v)
          · rw [hdv] at h1; simp at h1
          · cases hto : Nat.testBit 1 (u - v)
            · rw [hdv, hto] at h1; simp at h1
            · have hvu : v ≤ u := of_decide_eq_true hdv
              have h2 := Nat.testBit_one_eq_true_iff_self_eq_zero.mp hto
              exact Or.inr ⟨hvu, by omega⟩
        · rw [hc] at h1
          simp at h1
      · exact Or.inl rfl
    · exact Or.inr ⟨by omega, by omega⟩

/-- A lane with a true bit witnesses a nonzero word. -/
theorem ne_zero_of_testBit {n i : Nat} (h : n.testBit i = true) : n ≠ 0 := by
  intro hn; rw [hn, Nat.zero_testBit] at h; exact Bool.false_ne_true h

/-! ## 7. Soundness: from a configuration with a left edge to its lane -/

def HasLeftEdge (x : Int → Bool) (lo : Int) : Prop := x lo = true ∧ ∀ p, p < lo → x p = false

/-- The signature of a configuration: its center cells at times `0..m` as the bits of a number. -/
def sig (x : Int → Bool) (m : Nat) : Nat := Rule30ZeroBoundaryLanes.pack (fun t => evol x t 0) (m + 1)

/-- The lane of a configuration with edge at `a`: the bits of positions `a + 1 .. a + n`. -/
def laneOf (x : Int → Bool) (a : Int) (n : Nat) : Nat :=
  Rule30ZeroBoundaryLanes.pack (fun j => x (a + 1 + j)) n

theorem laneOf_lt (x : Int → Bool) (a : Int) (n : Nat) : laneOf x a n < 2 ^ n :=
  Rule30ZeroBoundaryLanes.pack_lt _ n

/-- The window configuration of the lane of `x` agrees with `x` on every position `≤ a + n`. -/
theorem cfg_laneOf (x : Int → Bool) (a : Int) (n : Nat) (hx : HasLeftEdge x a) :
    ∀ p : Int, p ≤ a + n → cfg a (n + 1) (laneCode (laneOf x a n)) p = x p := by
  intro p hp
  unfold cfg
  by_cases h1 : a ≤ p
  · have h2 : p < a + ((n + 1 : Nat) : Int) := by omega
    simp only [h1, h2, and_self, ↓reduceIte]
    obtain ⟨j, hj⟩ : ∃ j : Nat, p = a + j := ⟨(p - a).toNat, by omega⟩
    subst hj
    rw [show (a + (j : Int) - a).toNat = j by omega]
    cases j with
    | zero =>
      rw [laneCode_testBit_zero, show a + ((0 : Nat) : Int) = a by omega, hx.1]
    | succ j =>
      rw [laneCode_testBit_succ, laneOf, Rule30ZeroBoundaryLanes.testBit_pack]
      have : j < n := by omega
      simp only [this, decide_true, Bool.true_and]
      congr 1; omega
  · have : ¬ (a ≤ p ∧ p < a + ((n + 1 : Nat) : Int)) := fun h => h1 h.1
    rw [if_neg this]
    exact (hx.2 p (by omega)).symm

/-- **Key step.** For a configuration with left edge at `a = d - m`, every center cell up to time
`m` is read off its lane in the center words. -/
theorem center_eq_lane (m d : Nat) (hd : d ≤ 2 * m) (x : Int → Bool)
    (hx : HasLeftEdge x ((d : Int) - m)) (t : Nat) (ht : t ≤ m) :
    ((centers m m (initWords m d (2 * m - d))).getD t 0).testBit (laneOf x ((d : Int) - m) (2 * m - d))
      = evol x t 0 := by
  rw [centers_spec m d hd t _ ht (laneOf_lt _ _ _)]
  have hw : (2 * m + 1 - d) = (2 * m - d) + 1 := by omega
  rw [hw]
  have hagree := cfg_laneOf x ((d : Int) - m) (2 * m - d) hx
  have hloc := Rule30ZeroBoundaryBarriers.evol_local_le (x := x)
    (x' := cfg ((d : Int) - m) (2 * m - d + 1) (laneCode (laneOf x ((d : Int) - m) (2 * m - d))))
    (d := 0) (b := (m : Int)) (fun p hp => by rw [Int.add_zero]; exact hagree p (by omega)) t 0 (by omega)
  rw [Int.zero_add] at hloc
  exact hloc

/-- The signature of `x` is in the signature set of its edge class. -/
theorem sig_mem (m d : Nat) (hd : d ≤ 2 * m) (x : Int → Bool) (hx : HasLeftEdge x ((d : Int) - m)) :
    (sigSet (2 ^ 2 ^ (2 * m - d) - 1) (centers m m (initWords m d (2 * m - d))) m (2 ^ (m + 1)) 0 0).testBit
      (sig x m) = true := by
  apply sigSet_testBit
  · exact Nat.zero_le _
  · rw [Nat.zero_add]; exact Rule30ZeroBoundaryLanes.pack_lt _ _
  · apply ne_zero_of_testBit (i := laneOf x ((d : Int) - m) (2 * m - d))
    apply memb_testBit
    · rw [Nat.testBit_two_pow_sub_one]; simp [laneOf_lt]
    · intro t ht
      rw [center_eq_lane m d hd x hx t (by omega), sig, Rule30ZeroBoundaryLanes.testBit_pack]
      simp [ht]

def blk : Nat := 256

noncomputable def partSet (m d k : Nat) : Nat :=
  forceL (centers m m (initWords m d (2 * m - d)))
    (fun C => sigSet (2 ^ 2 ^ (2 * m - d) - 1) C m blk (blk * k) 0)

theorem partSet_eq (m d k : Nat) : partSet m d k =
    sigSet (2 ^ 2 ^ (2 * m - d) - 1) (centers m m (initWords m d (2 * m - d))) m blk (blk * k) 0 := by
  unfold partSet; rw [forceL_eq]

/-- The signature of `x` is in the block that covers it. -/
theorem memb_block (m d : Nat) (hd : d ≤ 2 * m) (x : Int → Bool) (hx : HasLeftEdge x ((d : Int) - m))
    (k : Nat) (hlo : blk * k ≤ sig x m) (hhi : sig x m < blk * k + blk) :
    (partSet m d k).testBit (sig x m) = true := by
  rw [partSet_eq]
  apply sigSet_testBit _ _ _ _ _ _ _ hlo hhi
  apply ne_zero_of_testBit (i := laneOf x ((d : Int) - m) (2 * m - d))
  apply memb_testBit
  · rw [Nat.testBit_two_pow_sub_one]; simp [laneOf_lt]
  · intro t ht
    rw [center_eq_lane m d hd x hx t (by omega), sig, Rule30ZeroBoundaryLanes.testBit_pack]
    simp [ht]

/-- **Separation from disjoint signature sets.** -/
theorem separation (m d e : Nat) (hd : d ≤ 2 * m) (he : e ≤ 2 * m)
    (hdisj : Nat.land
      (sigSet (2 ^ 2 ^ (2 * m - d) - 1) (centers m m (initWords m d (2 * m - d))) m (2 ^ (m + 1)) 0 0)
      (sigSet (2 ^ 2 ^ (2 * m - e) - 1) (centers m m (initWords m e (2 * m - e))) m (2 ^ (m + 1)) 0 0) = 0)
    (x y : Int → Bool) (hx : HasLeftEdge x ((d : Int) - m)) (hy : HasLeftEdge y ((e : Int) - m)) :
    ∃ t, t ≤ m ∧ evol x t 0 ≠ evol y t 0 := by
  apply Classical.byContradiction
  intro hcon
  have hcon : ∀ t, t ≤ m → evol x t 0 = evol y t 0 := fun t ht =>
    Decidable.byContradiction fun hne => hcon ⟨t, ht, hne⟩
  have hsig : sig x m = sig y m := by
    apply Nat.eq_of_testBit_eq
    intro i
    unfold sig
    rw [Rule30ZeroBoundaryLanes.testBit_pack, Rule30ZeroBoundaryLanes.testBit_pack]
    by_cases hi : i < m + 1
    · simp only [hi, decide_true, Bool.true_and]
      exact hcon i (by omega)
    · simp [hi]
  have h1 := sig_mem m d hd x hx
  have h2 := sig_mem m e he y hy
  rw [hsig] at h1
  have h3 := congrArg (fun z : Nat => z.testBit (sig y m)) hdisj
  change ((_ : Nat) &&& (_ : Nat)).testBit (sig y m) = (0 : Nat).testBit (sig y m) at h3
  rw [Nat.testBit_and, h1, h2, Nat.zero_testBit] at h3
  exact absurd h3 (by decide)

/-! ## 8. The kernel-facing form: one declaration per block of `2^8` signature values

The kernel caches every intermediate word for the lifetime of one declaration, so the signature
loop is cut into blocks of `256` values; disjointness holds block by block, since a block collects
only the signatures of its own range. The center words are forced to literals before each loop. -/

/-- Disjointness of all blocks `k < K`. -/
def BlocksDisjoint (m d e K : Nat) : Prop := ∀ k, k < K → Nat.land (partSet m d k) (partSet m e k) = 0

theorem blocksDisjoint_zero (m d e : Nat) : BlocksDisjoint m d e 0 := fun _ h => absurd h (Nat.not_lt_zero _)

theorem blocksDisjoint_succ (m d e K : Nat) (h : BlocksDisjoint m d e K)
    (hK : Nat.land (partSet m d K) (partSet m e K) = 0) : BlocksDisjoint m d e (K + 1) := by
  intro k hk
  by_cases hkK : k = K
  · subst hkK; exact hK
  · exact h k (by omega)

/-- **Separation from block-wise disjointness.** With `blk * K ≥ 2 ^ (m + 1)` every signature lives
in some block, and the two classes never share one. -/
theorem separationB (m d e K : Nat) (hd : d ≤ 2 * m) (he : e ≤ 2 * m) (hK : 2 ^ (m + 1) ≤ blk * K)
    (hdisj : BlocksDisjoint m d e K)
    (x y : Int → Bool) (hx : HasLeftEdge x ((d : Int) - m)) (hy : HasLeftEdge y ((e : Int) - m)) :
    ∃ t, t ≤ m ∧ evol x t 0 ≠ evol y t 0 := by
  apply Classical.byContradiction
  intro hcon
  have hcon : ∀ t, t ≤ m → evol x t 0 = evol y t 0 := fun t ht =>
    Decidable.byContradiction fun hne => hcon ⟨t, ht, hne⟩
  have hsig : sig x m = sig y m := by
    apply Nat.eq_of_testBit_eq
    intro i
    unfold sig
    rw [Rule30ZeroBoundaryLanes.testBit_pack, Rule30ZeroBoundaryLanes.testBit_pack]
    by_cases hi : i < m + 1
    · simp only [hi, decide_true, Bool.true_and]
      exact hcon i (by omega)
    · simp [hi]
  -- the block of the common signature
  have hlt : sig y m < 2 ^ (m + 1) := Rule30ZeroBoundaryLanes.pack_lt _ _
  have hb : 0 < blk := by decide
  have hk : sig y m / blk < K := by
    rw [Nat.div_lt_iff_lt_mul hb, Nat.mul_comm]; omega
  have hlo : blk * (sig y m / blk) ≤ sig y m := Nat.mul_div_le _ _
  have hhi : sig y m < blk * (sig y m / blk) + blk := by
    have := Nat.lt_mul_div_succ (sig y m) hb
    rw [Nat.mul_succ] at this
    exact this
  have hmemx := memb_block m d hd x hx (sig y m / blk) (by rw [hsig]; exact hlo) (by rw [hsig]; exact hhi)
  have hmemy := memb_block m e he y hy (sig y m / blk) hlo hhi
  rw [hsig] at hmemx
  have h3 := congrArg (fun z : Nat => z.testBit (sig y m)) (hdisj _ hk)
  change ((_ : Nat) &&& (_ : Nat)).testBit (sig y m) = (0 : Nat).testBit (sig y m) at h3
  rw [Nat.testBit_and, hmemx, hmemy, Nat.zero_testBit] at h3
  exact absurd h3 (by decide)



/-! ## 9. The three instances -/

/-! ### `(-2, -1)`: `m = 8`, `d = 6`, `e = 7`, two blocks -/

theorem d8_0 : Nat.land (partSet 8 6 0) (partSet 8 7 0) = 0 := by decide +kernel
theorem d8_1 : Nat.land (partSet 8 6 1) (partSet 8 7 1) = 0 := by decide +kernel

theorem blocks8 : BlocksDisjoint 8 6 7 2 := by
  intro k hk
  match k with
  | 0 => exact d8_0
  | 1 => exact d8_1
  | k + 2 => exact absurd hk (by omega)

/-- **Edges `-2` and `-1` are told apart by time `8`**, for every pair of configurations with those
leftmost black cells (finite or not). -/
theorem sep_8 (x y : Int → Bool) (hx : HasLeftEdge x (-2)) (hy : HasLeftEdge y (-1)) :
    ∃ t, t ≤ 8 ∧ evol x t 0 ≠ evol y t 0 :=
  separationB 8 6 7 2 (by decide) (by decide) (by decide) blocks8 x y
    (by rw [show ((6 : Nat) : Int) - (8 : Nat) = -2 by decide]; exact hx)
    (by rw [show ((7 : Nat) : Int) - (8 : Nat) = -1 by decide]; exact hy)

/-! ### `(-4, -3)`: `m = 13`, `d = 9`, `e = 10`, sixty-four blocks -/

theorem d13_0 : Nat.land (partSet 13 9 0) (partSet 13 10 0) = 0 := by decide +kernel
theorem d13_1 : Nat.land (partSet 13 9 1) (partSet 13 10 1) = 0 := by decide +kernel
theorem d13_2 : Nat.land (partSet 13 9 2) (partSet 13 10 2) = 0 := by decide +kernel
theorem d13_3 : Nat.land (partSet 13 9 3) (partSet 13 10 3) = 0 := by decide +kernel
theorem d13_4 : Nat.land (partSet 13 9 4) (partSet 13 10 4) = 0 := by decide +kernel
theorem d13_5 : Nat.land (partSet 13 9 5) (partSet 13 10 5) = 0 := by decide +kernel
theorem d13_6 : Nat.land (partSet 13 9 6) (partSet 13 10 6) = 0 := by decide +kernel
theorem d13_7 : Nat.land (partSet 13 9 7) (partSet 13 10 7) = 0 := by decide +kernel
theorem d13_8 : Nat.land (partSet 13 9 8) (partSet 13 10 8) = 0 := by decide +kernel
theorem d13_9 : Nat.land (partSet 13 9 9) (partSet 13 10 9) = 0 := by decide +kernel
theorem d13_10 : Nat.land (partSet 13 9 10) (partSet 13 10 10) = 0 := by decide +kernel
theorem d13_11 : Nat.land (partSet 13 9 11) (partSet 13 10 11) = 0 := by decide +kernel
theorem d13_12 : Nat.land (partSet 13 9 12) (partSet 13 10 12) = 0 := by decide +kernel
theorem d13_13 : Nat.land (partSet 13 9 13) (partSet 13 10 13) = 0 := by decide +kernel
theorem d13_14 : Nat.land (partSet 13 9 14) (partSet 13 10 14) = 0 := by decide +kernel
theorem d13_15 : Nat.land (partSet 13 9 15) (partSet 13 10 15) = 0 := by decide +kernel
theorem d13_16 : Nat.land (partSet 13 9 16) (partSet 13 10 16) = 0 := by decide +kernel
theorem d13_17 : Nat.land (partSet 13 9 17) (partSet 13 10 17) = 0 := by decide +kernel
theorem d13_18 : Nat.land (partSet 13 9 18) (partSet 13 10 18) = 0 := by decide +kernel
theorem d13_19 : Nat.land (partSet 13 9 19) (partSet 13 10 19) = 0 := by decide +kernel
theorem d13_20 : Nat.land (partSet 13 9 20) (partSet 13 10 20) = 0 := by decide +kernel
theorem d13_21 : Nat.land (partSet 13 9 21) (partSet 13 10 21) = 0 := by decide +kernel
theorem d13_22 : Nat.land (partSet 13 9 22) (partSet 13 10 22) = 0 := by decide +kernel
theorem d13_23 : Nat.land (partSet 13 9 23) (partSet 13 10 23) = 0 := by decide +kernel
theorem d13_24 : Nat.land (partSet 13 9 24) (partSet 13 10 24) = 0 := by decide +kernel
theorem d13_25 : Nat.land (partSet 13 9 25) (partSet 13 10 25) = 0 := by decide +kernel
theorem d13_26 : Nat.land (partSet 13 9 26) (partSet 13 10 26) = 0 := by decide +kernel
theorem d13_27 : Nat.land (partSet 13 9 27) (partSet 13 10 27) = 0 := by decide +kernel
theorem d13_28 : Nat.land (partSet 13 9 28) (partSet 13 10 28) = 0 := by decide +kernel
theorem d13_29 : Nat.land (partSet 13 9 29) (partSet 13 10 29) = 0 := by decide +kernel
theorem d13_30 : Nat.land (partSet 13 9 30) (partSet 13 10 30) = 0 := by decide +kernel
theorem d13_31 : Nat.land (partSet 13 9 31) (partSet 13 10 31) = 0 := by decide +kernel
theorem d13_32 : Nat.land (partSet 13 9 32) (partSet 13 10 32) = 0 := by decide +kernel
theorem d13_33 : Nat.land (partSet 13 9 33) (partSet 13 10 33) = 0 := by decide +kernel
theorem d13_34 : Nat.land (partSet 13 9 34) (partSet 13 10 34) = 0 := by decide +kernel
theorem d13_35 : Nat.land (partSet 13 9 35) (partSet 13 10 35) = 0 := by decide +kernel
theorem d13_36 : Nat.land (partSet 13 9 36) (partSet 13 10 36) = 0 := by decide +kernel
theorem d13_37 : Nat.land (partSet 13 9 37) (partSet 13 10 37) = 0 := by decide +kernel
theorem d13_38 : Nat.land (partSet 13 9 38) (partSet 13 10 38) = 0 := by decide +kernel
theorem d13_39 : Nat.land (partSet 13 9 39) (partSet 13 10 39) = 0 := by decide +kernel
theorem d13_40 : Nat.land (partSet 13 9 40) (partSet 13 10 40) = 0 := by decide +kernel
theorem d13_41 : Nat.land (partSet 13 9 41) (partSet 13 10 41) = 0 := by decide +kernel
theorem d13_42 : Nat.land (partSet 13 9 42) (partSet 13 10 42) = 0 := by decide +kernel
theorem d13_43 : Nat.land (partSet 13 9 43) (partSet 13 10 43) = 0 := by decide +kernel
theorem d13_44 : Nat.land (partSet 13 9 44) (partSet 13 10 44) = 0 := by decide +kernel
theorem d13_45 : Nat.land (partSet 13 9 45) (partSet 13 10 45) = 0 := by decide +kernel
theorem d13_46 : Nat.land (partSet 13 9 46) (partSet 13 10 46) = 0 := by decide +kernel
theorem d13_47 : Nat.land (partSet 13 9 47) (partSet 13 10 47) = 0 := by decide +kernel
theorem d13_48 : Nat.land (partSet 13 9 48) (partSet 13 10 48) = 0 := by decide +kernel
theorem d13_49 : Nat.land (partSet 13 9 49) (partSet 13 10 49) = 0 := by decide +kernel
theorem d13_50 : Nat.land (partSet 13 9 50) (partSet 13 10 50) = 0 := by decide +kernel
theorem d13_51 : Nat.land (partSet 13 9 51) (partSet 13 10 51) = 0 := by decide +kernel
theorem d13_52 : Nat.land (partSet 13 9 52) (partSet 13 10 52) = 0 := by decide +kernel
theorem d13_53 : Nat.land (partSet 13 9 53) (partSet 13 10 53) = 0 := by decide +kernel
theorem d13_54 : Nat.land (partSet 13 9 54) (partSet 13 10 54) = 0 := by decide +kernel
theorem d13_55 : Nat.land (partSet 13 9 55) (partSet 13 10 55) = 0 := by decide +kernel
theorem d13_56 : Nat.land (partSet 13 9 56) (partSet 13 10 56) = 0 := by decide +kernel
theorem d13_57 : Nat.land (partSet 13 9 57) (partSet 13 10 57) = 0 := by decide +kernel
theorem d13_58 : Nat.land (partSet 13 9 58) (partSet 13 10 58) = 0 := by decide +kernel
theorem d13_59 : Nat.land (partSet 13 9 59) (partSet 13 10 59) = 0 := by decide +kernel
theorem d13_60 : Nat.land (partSet 13 9 60) (partSet 13 10 60) = 0 := by decide +kernel
theorem d13_61 : Nat.land (partSet 13 9 61) (partSet 13 10 61) = 0 := by decide +kernel
theorem d13_62 : Nat.land (partSet 13 9 62) (partSet 13 10 62) = 0 := by decide +kernel
theorem d13_63 : Nat.land (partSet 13 9 63) (partSet 13 10 63) = 0 := by decide +kernel

theorem blocks13 : BlocksDisjoint 13 9 10 64 := by
  intro k hk
  match k with
  | 0 => exact d13_0
  | 1 => exact d13_1
  | 2 => exact d13_2
  | 3 => exact d13_3
  | 4 => exact d13_4
  | 5 => exact d13_5
  | 6 => exact d13_6
  | 7 => exact d13_7
  | 8 => exact d13_8
  | 9 => exact d13_9
  | 10 => exact d13_10
  | 11 => exact d13_11
  | 12 => exact d13_12
  | 13 => exact d13_13
  | 14 => exact d13_14
  | 15 => exact d13_15
  | 16 => exact d13_16
  | 17 => exact d13_17
  | 18 => exact d13_18
  | 19 => exact d13_19
  | 20 => exact d13_20
  | 21 => exact d13_21
  | 22 => exact d13_22
  | 23 => exact d13_23
  | 24 => exact d13_24
  | 25 => exact d13_25
  | 26 => exact d13_26
  | 27 => exact d13_27
  | 28 => exact d13_28
  | 29 => exact d13_29
  | 30 => exact d13_30
  | 31 => exact d13_31
  | 32 => exact d13_32
  | 33 => exact d13_33
  | 34 => exact d13_34
  | 35 => exact d13_35
  | 36 => exact d13_36
  | 37 => exact d13_37
  | 38 => exact d13_38
  | 39 => exact d13_39
  | 40 => exact d13_40
  | 41 => exact d13_41
  | 42 => exact d13_42
  | 43 => exact d13_43
  | 44 => exact d13_44
  | 45 => exact d13_45
  | 46 => exact d13_46
  | 47 => exact d13_47
  | 48 => exact d13_48
  | 49 => exact d13_49
  | 50 => exact d13_50
  | 51 => exact d13_51
  | 52 => exact d13_52
  | 53 => exact d13_53
  | 54 => exact d13_54
  | 55 => exact d13_55
  | 56 => exact d13_56
  | 57 => exact d13_57
  | 58 => exact d13_58
  | 59 => exact d13_59
  | 60 => exact d13_60
  | 61 => exact d13_61
  | 62 => exact d13_62
  | 63 => exact d13_63
  | k + 64 => exact absurd hk (by omega)

/-- **Edges `-4` and `-3` are told apart by time `13`.** -/
theorem sep_13 (x y : Int → Bool) (hx : HasLeftEdge x (-4)) (hy : HasLeftEdge y (-3)) :
    ∃ t, t ≤ 13 ∧ evol x t 0 ≠ evol y t 0 :=
  separationB 13 9 10 64 (by decide) (by decide) (by decide) blocks13 x y
    (by rw [show ((9 : Nat) : Int) - (13 : Nat) = -4 by decide]; exact hx)
    (by rw [show ((10 : Nat) : Int) - (13 : Nat) = -3 by decide]; exact hy)

/-! ### `(-3, -2)`: `m = 14`, `d = 11`, `e = 12`, one hundred and twenty-eight blocks -/

theorem d14_0 : Nat.land (partSet 14 11 0) (partSet 14 12 0) = 0 := by decide +kernel
theorem d14_1 : Nat.land (partSet 14 11 1) (partSet 14 12 1) = 0 := by decide +kernel
theorem d14_2 : Nat.land (partSet 14 11 2) (partSet 14 12 2) = 0 := by decide +kernel
theorem d14_3 : Nat.land (partSet 14 11 3) (partSet 14 12 3) = 0 := by decide +kernel
theorem d14_4 : Nat.land (partSet 14 11 4) (partSet 14 12 4) = 0 := by decide +kernel
theorem d14_5 : Nat.land (partSet 14 11 5) (partSet 14 12 5) = 0 := by decide +kernel
theorem d14_6 : Nat.land (partSet 14 11 6) (partSet 14 12 6) = 0 := by decide +kernel
theorem d14_7 : Nat.land (partSet 14 11 7) (partSet 14 12 7) = 0 := by decide +kernel
theorem d14_8 : Nat.land (partSet 14 11 8) (partSet 14 12 8) = 0 := by decide +kernel
theorem d14_9 : Nat.land (partSet 14 11 9) (partSet 14 12 9) = 0 := by decide +kernel
theorem d14_10 : Nat.land (partSet 14 11 10) (partSet 14 12 10) = 0 := by decide +kernel
theorem d14_11 : Nat.land (partSet 14 11 11) (partSet 14 12 11) = 0 := by decide +kernel
theorem d14_12 : Nat.land (partSet 14 11 12) (partSet 14 12 12) = 0 := by decide +kernel
theorem d14_13 : Nat.land (partSet 14 11 13) (partSet 14 12 13) = 0 := by decide +kernel
theorem d14_14 : Nat.land (partSet 14 11 14) (partSet 14 12 14) = 0 := by decide +kernel
theorem d14_15 : Nat.land (partSet 14 11 15) (partSet 14 12 15) = 0 := by decide +kernel
theorem d14_16 : Nat.land (partSet 14 11 16) (partSet 14 12 16) = 0 := by decide +kernel
theorem d14_17 : Nat.land (partSet 14 11 17) (partSet 14 12 17) = 0 := by decide +kernel
theorem d14_18 : Nat.land (partSet 14 11 18) (partSet 14 12 18) = 0 := by decide +kernel
theorem d14_19 : Nat.land (partSet 14 11 19) (partSet 14 12 19) = 0 := by decide +kernel
theorem d14_20 : Nat.land (partSet 14 11 20) (partSet 14 12 20) = 0 := by decide +kernel
theorem d14_21 : Nat.land (partSet 14 11 21) (partSet 14 12 21) = 0 := by decide +kernel
theorem d14_22 : Nat.land (partSet 14 11 22) (partSet 14 12 22) = 0 := by decide +kernel
theorem d14_23 : Nat.land (partSet 14 11 23) (partSet 14 12 23) = 0 := by decide +kernel
theorem d14_24 : Nat.land (partSet 14 11 24) (partSet 14 12 24) = 0 := by decide +kernel
theorem d14_25 : Nat.land (partSet 14 11 25) (partSet 14 12 25) = 0 := by decide +kernel
theorem d14_26 : Nat.land (partSet 14 11 26) (partSet 14 12 26) = 0 := by decide +kernel
theorem d14_27 : Nat.land (partSet 14 11 27) (partSet 14 12 27) = 0 := by decide +kernel
theorem d14_28 : Nat.land (partSet 14 11 28) (partSet 14 12 28) = 0 := by decide +kernel
theorem d14_29 : Nat.land (partSet 14 11 29) (partSet 14 12 29) = 0 := by decide +kernel
theorem d14_30 : Nat.land (partSet 14 11 30) (partSet 14 12 30) = 0 := by decide +kernel
theorem d14_31 : Nat.land (partSet 14 11 31) (partSet 14 12 31) = 0 := by decide +kernel
theorem d14_32 : Nat.land (partSet 14 11 32) (partSet 14 12 32) = 0 := by decide +kernel
theorem d14_33 : Nat.land (partSet 14 11 33) (partSet 14 12 33) = 0 := by decide +kernel
theorem d14_34 : Nat.land (partSet 14 11 34) (partSet 14 12 34) = 0 := by decide +kernel
theorem d14_35 : Nat.land (partSet 14 11 35) (partSet 14 12 35) = 0 := by decide +kernel
theorem d14_36 : Nat.land (partSet 14 11 36) (partSet 14 12 36) = 0 := by decide +kernel
theorem d14_37 : Nat.land (partSet 14 11 37) (partSet 14 12 37) = 0 := by decide +kernel
theorem d14_38 : Nat.land (partSet 14 11 38) (partSet 14 12 38) = 0 := by decide +kernel
theorem d14_39 : Nat.land (partSet 14 11 39) (partSet 14 12 39) = 0 := by decide +kernel
theorem d14_40 : Nat.land (partSet 14 11 40) (partSet 14 12 40) = 0 := by decide +kernel
theorem d14_41 : Nat.land (partSet 14 11 41) (partSet 14 12 41) = 0 := by decide +kernel
theorem d14_42 : Nat.land (partSet 14 11 42) (partSet 14 12 42) = 0 := by decide +kernel
theorem d14_43 : Nat.land (partSet 14 11 43) (partSet 14 12 43) = 0 := by decide +kernel
theorem d14_44 : Nat.land (partSet 14 11 44) (partSet 14 12 44) = 0 := by decide +kernel
theorem d14_45 : Nat.land (partSet 14 11 45) (partSet 14 12 45) = 0 := by decide +kernel
theorem d14_46 : Nat.land (partSet 14 11 46) (partSet 14 12 46) = 0 := by decide +kernel
theorem d14_47 : Nat.land (partSet 14 11 47) (partSet 14 12 47) = 0 := by decide +kernel
theorem d14_48 : Nat.land (partSet 14 11 48) (partSet 14 12 48) = 0 := by decide +kernel
theorem d14_49 : Nat.land (partSet 14 11 49) (partSet 14 12 49) = 0 := by decide +kernel
theorem d14_50 : Nat.land (partSet 14 11 50) (partSet 14 12 50) = 0 := by decide +kernel
theorem d14_51 : Nat.land (partSet 14 11 51) (partSet 14 12 51) = 0 := by decide +kernel
theorem d14_52 : Nat.land (partSet 14 11 52) (partSet 14 12 52) = 0 := by decide +kernel
theorem d14_53 : Nat.land (partSet 14 11 53) (partSet 14 12 53) = 0 := by decide +kernel
theorem d14_54 : Nat.land (partSet 14 11 54) (partSet 14 12 54) = 0 := by decide +kernel
theorem d14_55 : Nat.land (partSet 14 11 55) (partSet 14 12 55) = 0 := by decide +kernel
theorem d14_56 : Nat.land (partSet 14 11 56) (partSet 14 12 56) = 0 := by decide +kernel
theorem d14_57 : Nat.land (partSet 14 11 57) (partSet 14 12 57) = 0 := by decide +kernel
theorem d14_58 : Nat.land (partSet 14 11 58) (partSet 14 12 58) = 0 := by decide +kernel
theorem d14_59 : Nat.land (partSet 14 11 59) (partSet 14 12 59) = 0 := by decide +kernel
theorem d14_60 : Nat.land (partSet 14 11 60) (partSet 14 12 60) = 0 := by decide +kernel
theorem d14_61 : Nat.land (partSet 14 11 61) (partSet 14 12 61) = 0 := by decide +kernel
theorem d14_62 : Nat.land (partSet 14 11 62) (partSet 14 12 62) = 0 := by decide +kernel
theorem d14_63 : Nat.land (partSet 14 11 63) (partSet 14 12 63) = 0 := by decide +kernel
theorem d14_64 : Nat.land (partSet 14 11 64) (partSet 14 12 64) = 0 := by decide +kernel
theorem d14_65 : Nat.land (partSet 14 11 65) (partSet 14 12 65) = 0 := by decide +kernel
theorem d14_66 : Nat.land (partSet 14 11 66) (partSet 14 12 66) = 0 := by decide +kernel
theorem d14_67 : Nat.land (partSet 14 11 67) (partSet 14 12 67) = 0 := by decide +kernel
theorem d14_68 : Nat.land (partSet 14 11 68) (partSet 14 12 68) = 0 := by decide +kernel
theorem d14_69 : Nat.land (partSet 14 11 69) (partSet 14 12 69) = 0 := by decide +kernel
theorem d14_70 : Nat.land (partSet 14 11 70) (partSet 14 12 70) = 0 := by decide +kernel
theorem d14_71 : Nat.land (partSet 14 11 71) (partSet 14 12 71) = 0 := by decide +kernel
theorem d14_72 : Nat.land (partSet 14 11 72) (partSet 14 12 72) = 0 := by decide +kernel
theorem d14_73 : Nat.land (partSet 14 11 73) (partSet 14 12 73) = 0 := by decide +kernel
theorem d14_74 : Nat.land (partSet 14 11 74) (partSet 14 12 74) = 0 := by decide +kernel
theorem d14_75 : Nat.land (partSet 14 11 75) (partSet 14 12 75) = 0 := by decide +kernel
theorem d14_76 : Nat.land (partSet 14 11 76) (partSet 14 12 76) = 0 := by decide +kernel
theorem d14_77 : Nat.land (partSet 14 11 77) (partSet 14 12 77) = 0 := by decide +kernel
theorem d14_78 : Nat.land (partSet 14 11 78) (partSet 14 12 78) = 0 := by decide +kernel
theorem d14_79 : Nat.land (partSet 14 11 79) (partSet 14 12 79) = 0 := by decide +kernel
theorem d14_80 : Nat.land (partSet 14 11 80) (partSet 14 12 80) = 0 := by decide +kernel
theorem d14_81 : Nat.land (partSet 14 11 81) (partSet 14 12 81) = 0 := by decide +kernel
theorem d14_82 : Nat.land (partSet 14 11 82) (partSet 14 12 82) = 0 := by decide +kernel
theorem d14_83 : Nat.land (partSet 14 11 83) (partSet 14 12 83) = 0 := by decide +kernel
theorem d14_84 : Nat.land (partSet 14 11 84) (partSet 14 12 84) = 0 := by decide +kernel
theorem d14_85 : Nat.land (partSet 14 11 85) (partSet 14 12 85) = 0 := by decide +kernel
theorem d14_86 : Nat.land (partSet 14 11 86) (partSet 14 12 86) = 0 := by decide +kernel
theorem d14_87 : Nat.land (partSet 14 11 87) (partSet 14 12 87) = 0 := by decide +kernel
theorem d14_88 : Nat.land (partSet 14 11 88) (partSet 14 12 88) = 0 := by decide +kernel
theorem d14_89 : Nat.land (partSet 14 11 89) (partSet 14 12 89) = 0 := by decide +kernel
theorem d14_90 : Nat.land (partSet 14 11 90) (partSet 14 12 90) = 0 := by decide +kernel
theorem d14_91 : Nat.land (partSet 14 11 91) (partSet 14 12 91) = 0 := by decide +kernel
theorem d14_92 : Nat.land (partSet 14 11 92) (partSet 14 12 92) = 0 := by decide +kernel
theorem d14_93 : Nat.land (partSet 14 11 93) (partSet 14 12 93) = 0 := by decide +kernel
theorem d14_94 : Nat.land (partSet 14 11 94) (partSet 14 12 94) = 0 := by decide +kernel
theorem d14_95 : Nat.land (partSet 14 11 95) (partSet 14 12 95) = 0 := by decide +kernel
theorem d14_96 : Nat.land (partSet 14 11 96) (partSet 14 12 96) = 0 := by decide +kernel
theorem d14_97 : Nat.land (partSet 14 11 97) (partSet 14 12 97) = 0 := by decide +kernel
theorem d14_98 : Nat.land (partSet 14 11 98) (partSet 14 12 98) = 0 := by decide +kernel
theorem d14_99 : Nat.land (partSet 14 11 99) (partSet 14 12 99) = 0 := by decide +kernel
theorem d14_100 : Nat.land (partSet 14 11 100) (partSet 14 12 100) = 0 := by decide +kernel
theorem d14_101 : Nat.land (partSet 14 11 101) (partSet 14 12 101) = 0 := by decide +kernel
theorem d14_102 : Nat.land (partSet 14 11 102) (partSet 14 12 102) = 0 := by decide +kernel
theorem d14_103 : Nat.land (partSet 14 11 103) (partSet 14 12 103) = 0 := by decide +kernel
theorem d14_104 : Nat.land (partSet 14 11 104) (partSet 14 12 104) = 0 := by decide +kernel
theorem d14_105 : Nat.land (partSet 14 11 105) (partSet 14 12 105) = 0 := by decide +kernel
theorem d14_106 : Nat.land (partSet 14 11 106) (partSet 14 12 106) = 0 := by decide +kernel
theorem d14_107 : Nat.land (partSet 14 11 107) (partSet 14 12 107) = 0 := by decide +kernel
theorem d14_108 : Nat.land (partSet 14 11 108) (partSet 14 12 108) = 0 := by decide +kernel
theorem d14_109 : Nat.land (partSet 14 11 109) (partSet 14 12 109) = 0 := by decide +kernel
theorem d14_110 : Nat.land (partSet 14 11 110) (partSet 14 12 110) = 0 := by decide +kernel
theorem d14_111 : Nat.land (partSet 14 11 111) (partSet 14 12 111) = 0 := by decide +kernel
theorem d14_112 : Nat.land (partSet 14 11 112) (partSet 14 12 112) = 0 := by decide +kernel
theorem d14_113 : Nat.land (partSet 14 11 113) (partSet 14 12 113) = 0 := by decide +kernel
theorem d14_114 : Nat.land (partSet 14 11 114) (partSet 14 12 114) = 0 := by decide +kernel
theorem d14_115 : Nat.land (partSet 14 11 115) (partSet 14 12 115) = 0 := by decide +kernel
theorem d14_116 : Nat.land (partSet 14 11 116) (partSet 14 12 116) = 0 := by decide +kernel
theorem d14_117 : Nat.land (partSet 14 11 117) (partSet 14 12 117) = 0 := by decide +kernel
theorem d14_118 : Nat.land (partSet 14 11 118) (partSet 14 12 118) = 0 := by decide +kernel
theorem d14_119 : Nat.land (partSet 14 11 119) (partSet 14 12 119) = 0 := by decide +kernel
theorem d14_120 : Nat.land (partSet 14 11 120) (partSet 14 12 120) = 0 := by decide +kernel
theorem d14_121 : Nat.land (partSet 14 11 121) (partSet 14 12 121) = 0 := by decide +kernel
theorem d14_122 : Nat.land (partSet 14 11 122) (partSet 14 12 122) = 0 := by decide +kernel
theorem d14_123 : Nat.land (partSet 14 11 123) (partSet 14 12 123) = 0 := by decide +kernel
theorem d14_124 : Nat.land (partSet 14 11 124) (partSet 14 12 124) = 0 := by decide +kernel
theorem d14_125 : Nat.land (partSet 14 11 125) (partSet 14 12 125) = 0 := by decide +kernel
theorem d14_126 : Nat.land (partSet 14 11 126) (partSet 14 12 126) = 0 := by decide +kernel
theorem d14_127 : Nat.land (partSet 14 11 127) (partSet 14 12 127) = 0 := by decide +kernel

theorem blocks14 : BlocksDisjoint 14 11 12 128 := by
  intro k hk
  match k with
  | 0 => exact d14_0
  | 1 => exact d14_1
  | 2 => exact d14_2
  | 3 => exact d14_3
  | 4 => exact d14_4
  | 5 => exact d14_5
  | 6 => exact d14_6
  | 7 => exact d14_7
  | 8 => exact d14_8
  | 9 => exact d14_9
  | 10 => exact d14_10
  | 11 => exact d14_11
  | 12 => exact d14_12
  | 13 => exact d14_13
  | 14 => exact d14_14
  | 15 => exact d14_15
  | 16 => exact d14_16
  | 17 => exact d14_17
  | 18 => exact d14_18
  | 19 => exact d14_19
  | 20 => exact d14_20
  | 21 => exact d14_21
  | 22 => exact d14_22
  | 23 => exact d14_23
  | 24 => exact d14_24
  | 25 => exact d14_25
  | 26 => exact d14_26
  | 27 => exact d14_27
  | 28 => exact d14_28
  | 29 => exact d14_29
  | 30 => exact d14_30
  | 31 => exact d14_31
  | 32 => exact d14_32
  | 33 => exact d14_33
  | 34 => exact d14_34
  | 35 => exact d14_35
  | 36 => exact d14_36
  | 37 => exact d14_37
  | 38 => exact d14_38
  | 39 => exact d14_39
  | 40 => exact d14_40
  | 41 => exact d14_41
  | 42 => exact d14_42
  | 43 => exact d14_43
  | 44 => exact d14_44
  | 45 => exact d14_45
  | 46 => exact d14_46
  | 47 => exact d14_47
  | 48 => exact d14_48
  | 49 => exact d14_49
  | 50 => exact d14_50
  | 51 => exact d14_51
  | 52 => exact d14_52
  | 53 => exact d14_53
  | 54 => exact d14_54
  | 55 => exact d14_55
  | 56 => exact d14_56
  | 57 => exact d14_57
  | 58 => exact d14_58
  | 59 => exact d14_59
  | 60 => exact d14_60
  | 61 => exact d14_61
  | 62 => exact d14_62
  | 63 => exact d14_63
  | 64 => exact d14_64
  | 65 => exact d14_65
  | 66 => exact d14_66
  | 67 => exact d14_67
  | 68 => exact d14_68
  | 69 => exact d14_69
  | 70 => exact d14_70
  | 71 => exact d14_71
  | 72 => exact d14_72
  | 73 => exact d14_73
  | 74 => exact d14_74
  | 75 => exact d14_75
  | 76 => exact d14_76
  | 77 => exact d14_77
  | 78 => exact d14_78
  | 79 => exact d14_79
  | 80 => exact d14_80
  | 81 => exact d14_81
  | 82 => exact d14_82
  | 83 => exact d14_83
  | 84 => exact d14_84
  | 85 => exact d14_85
  | 86 => exact d14_86
  | 87 => exact d14_87
  | 88 => exact d14_88
  | 89 => exact d14_89
  | 90 => exact d14_90
  | 91 => exact d14_91
  | 92 => exact d14_92
  | 93 => exact d14_93
  | 94 => exact d14_94
  | 95 => exact d14_95
  | 96 => exact d14_96
  | 97 => exact d14_97
  | 98 => exact d14_98
  | 99 => exact d14_99
  | 100 => exact d14_100
  | 101 => exact d14_101
  | 102 => exact d14_102
  | 103 => exact d14_103
  | 104 => exact d14_104
  | 105 => exact d14_105
  | 106 => exact d14_106
  | 107 => exact d14_107
  | 108 => exact d14_108
  | 109 => exact d14_109
  | 110 => exact d14_110
  | 111 => exact d14_111
  | 112 => exact d14_112
  | 113 => exact d14_113
  | 114 => exact d14_114
  | 115 => exact d14_115
  | 116 => exact d14_116
  | 117 => exact d14_117
  | 118 => exact d14_118
  | 119 => exact d14_119
  | 120 => exact d14_120
  | 121 => exact d14_121
  | 122 => exact d14_122
  | 123 => exact d14_123
  | 124 => exact d14_124
  | 125 => exact d14_125
  | 126 => exact d14_126
  | 127 => exact d14_127
  | k + 128 => exact absurd hk (by omega)

/-- **Edges `-3` and `-2` are told apart by time `14`.** -/
theorem sep_14 (x y : Int → Bool) (hx : HasLeftEdge x (-3)) (hy : HasLeftEdge y (-2)) :
    ∃ t, t ≤ 14 ∧ evol x t 0 ≠ evol y t 0 :=
  separationB 14 11 12 128 (by decide) (by decide) (by decide) blocks14 x y
    (by rw [show ((11 : Nat) : Int) - (14 : Nat) = -3 by decide]; exact hx)
    (by rw [show ((12 : Nat) : Int) - (14 : Nat) = -2 by decide]; exact hy)

/-! ## 10. Attaining pairs: the bound is exact -/

/-- The window configuration of a lane has its left edge at `a`. -/
theorem cfg_hasLeftEdge (a : Int) (w ℓ : Nat) : HasLeftEdge (cfg a (w + 1) (laneCode ℓ)) a := by
  refine ⟨?_, fun p hp => ?_⟩
  · simp only [cfg, Int.le_refl, true_and]
    rw [if_pos (by omega), Int.sub_self, Int.toNat_zero, laneCode_testBit_zero]
  · simp only [cfg]
    rw [if_neg (fun h => by omega)]

/-- The kernel-facing check that lanes `i` and `j` of the two classes agree at times `< m` and
differ at time `m`. -/
noncomputable def witCheck (m d e i j : Nat) : Bool :=
  forceL (centers m m (initWords m d (2 * m - d))) fun Cd =>
    forceL (centers m m (initWords m e (2 * m - e))) fun Ce =>
      ((List.range m).all fun t => (Cd.getD t 0).testBit i == (Ce.getD t 0).testBit j) &&
        !((Cd.getD m 0).testBit i == (Ce.getD m 0).testBit j)

theorem witCheck_eq (m d e i j : Nat) : witCheck m d e i j =
    (((List.range m).all fun t =>
      ((centers m m (initWords m d (2 * m - d))).getD t 0).testBit i ==
        ((centers m m (initWords m e (2 * m - e))).getD t 0).testBit j) &&
      !(((centers m m (initWords m d (2 * m - d))).getD m 0).testBit i ==
        ((centers m m (initWords m e (2 * m - e))).getD m 0).testBit j)) := by
  unfold witCheck; rw [forceL_eq, forceL_eq]

/-- From a passing check to two configurations with the given edges, agreeing before `m` and
differing at `m`. -/
theorem attained (m d e i j : Nat) (hd : d ≤ 2 * m) (he : e ≤ 2 * m) (hi : i < 2 ^ (2 * m - d))
    (hj : j < 2 ^ (2 * m - e)) (h : witCheck m d e i j = true) :
    ∃ x y : Int → Bool, HasLeftEdge x ((d : Int) - m) ∧ HasLeftEdge y ((e : Int) - m) ∧
      (∀ t, t < m → evol x t 0 = evol y t 0) ∧ evol x m 0 ≠ evol y m 0 := by
  rw [witCheck_eq, Bool.and_eq_true, List.all_eq_true] at h
  obtain ⟨h1, h2⟩ := h
  have hw : 2 * m + 1 - d = (2 * m - d) + 1 := by omega
  have hw' : 2 * m + 1 - e = (2 * m - e) + 1 := by omega
  refine ⟨cfg ((d : Int) - m) (2 * m + 1 - d) (laneCode i), cfg ((e : Int) - m) (2 * m + 1 - e) (laneCode j),
    ?_, ?_, ?_, ?_⟩
  · rw [hw]; exact cfg_hasLeftEdge _ _ _
  · rw [hw']; exact cfg_hasLeftEdge _ _ _
  · intro t ht
    rw [← centers_spec m d hd t i (by omega) hi, ← centers_spec m e he t j (by omega) hj]
    have := h1 t (List.mem_range.mpr ht)
    exact eq_of_beq this
  · rw [← centers_spec m d hd m i (Nat.le_refl _) hi, ← centers_spec m e he m j (Nat.le_refl _) hj]
    intro heq
    rw [heq] at h2
    simp at h2

theorem wit8 : witCheck 8 6 7 44 68 = true := by decide +kernel
theorem wit13 : witCheck 13 9 10 91 293 = true := by decide +kernel
theorem wit14 : witCheck 14 11 12 8 33 = true := by decide +kernel

/-- **The bound `8` is attained** for edges `-2`, `-1`. -/
theorem attained_8 : ∃ x y : Int → Bool, HasLeftEdge x (-2) ∧ HasLeftEdge y (-1) ∧
    (∀ t, t < 8 → evol x t 0 = evol y t 0) ∧ evol x 8 0 ≠ evol y 8 0 := by
  have h := attained 8 6 7 44 68 (by decide) (by decide) (by decide) (by decide) wit8
  rw [show ((6 : Nat) : Int) - (8 : Nat) = -2 by decide, show ((7 : Nat) : Int) - (8 : Nat) = -1 by decide] at h
  exact h

/-- **The bound `13` is attained** for edges `-4`, `-3`. -/
theorem attained_13 : ∃ x y : Int → Bool, HasLeftEdge x (-4) ∧ HasLeftEdge y (-3) ∧
    (∀ t, t < 13 → evol x t 0 = evol y t 0) ∧ evol x 13 0 ≠ evol y 13 0 := by
  have h := attained 13 9 10 91 293 (by decide) (by decide) (by decide) (by decide) wit13
  rw [show ((9 : Nat) : Int) - (13 : Nat) = -4 by decide, show ((10 : Nat) : Int) - (13 : Nat) = -3 by decide] at h
  exact h

/-- **The bound `14` is attained** for edges `-3`, `-2`. -/
theorem attained_14 : ∃ x y : Int → Bool, HasLeftEdge x (-3) ∧ HasLeftEdge y (-2) ∧
    (∀ t, t < 14 → evol x t 0 = evol y t 0) ∧ evol x 14 0 ≠ evol y 14 0 := by
  have h := attained 14 11 12 8 33 (by decide) (by decide) (by decide) (by decide) wit14
  rw [show ((11 : Nat) : Int) - (14 : Nat) = -3 by decide, show ((12 : Nat) : Int) - (14 : Nat) = -2 by decide] at h
  exact h

end Rule30Submission
", "ProjectDir" -> $Rule30PrizeKit]
```

## The formal checks

The three headlines, as Lean prints them, with the edge predicate as defined:

```wl
opens = {"Ruliology.CellularAutomata.Rule30Realization", "Rule30Submission"};
thm = rule30Submission["Rule30Submission.sep_8"];
{thm["TypeForm", "Open" -> opens], rule30Submission["Rule30Submission.sep_13"]["TypeForm", "Open" -> opens], rule30Submission["Rule30Submission.sep_14"]["TypeForm", "Open" -> opens], rule30Submission["Rule30Submission.HasLeftEdge"]["TypeForm", "Open" -> opens]}
```

The attained bounds, and the pillars: separation from block-wise disjointness, the lane invariant at the center, and one block's theorem as stated:

```wl
{rule30Submission["Rule30Submission.attained_8"]["TypeForm", "Open" -> opens], rule30Submission["Rule30Submission.separationB"]["TypeForm", "Open" -> opens], rule30Submission["Rule30Submission.centers_spec"]["TypeForm", "Open" -> opens], rule30Submission["Rule30Submission.d14_0"]["TypeForm", "Open" -> opens]}
```

The axioms of the headline are the three standard ones and nothing else:

```wl
thm["Axioms"]
```

The proof's structure, one level down from the headline:

```wl
thm["CallGraph", "Depth" -> 1]
```

The kernel accepts every declaration of the module again. This is the replay the verifier runs; it comes last because it resets LeanLink's elaboration state:

```wl
thm["KernelCheck"]
```

## What is not proved

- Nothing about the conjecture `EdgeObservable` in general, about any other pair of edges, or about Problem 1. The three deadlines, `8`, `14`, `13` for edge depths `2`, `3`, `4`, are not monotone, and three values support no law.
- The theorems are about the center column from time `0`; the kit's implication from `EdgeObservable` to Problem 1 applies the conjecture to two times of one orbit, which is Problem 1 itself, and these instances do not touch it.
- The bitsets are computed by the kernel, not supplied as data; the search in the Wolfram Language above is an illustration, and the theorems do not depend on it.

## Provenance

The question came from the kit's `Rule30TraceEdge` (Troy Lowry with OpenAI Codex, 2026-10-24). GPT (OpenAI) proposed the finite search over positioned rows, found the standard common-right-half lemma and corrected the first reading of the data; Claude (Anthropic) ran the searches, found the saturation argument, and wrote the module; GPT read the argument and the retained results before the module was written. The record is at github.com/ghywel/placego, reports/wolfram-agents/submissions/edge-sep.

## References

[1] S. Wolfram, [*Announcing the Rule 30 Prizes*](https://writings.stephenwolfram.com/2019/10/announcing-the-rule-30-prizes/), Wolfram Writings, 2019.

[2] Wolfram Institute, [*The Rule 30 Prize kit*](https://github.com/WolframInstitute/Rule30PrizeKit), 2026: `Rule30ZeroBoundaryBarriers.evol_local_le`, `Rule30ZeroBoundaryLanes.pat`, `Rule30TraceEdge.EdgeObservable`.
