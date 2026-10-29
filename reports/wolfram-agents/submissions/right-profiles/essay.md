---
Template: ComputationalEssay
Name: The 101 shift law for the right diagonals of rule 30, with its mod-4 forms
Author: Gareth Herbert - with Claude (Anthropic) and GPT (OpenAI)
Date: 2026-10-29
Description: A partial result about the right diagonals of rule 30, proved in core Lean: after the doubling letters 101 the next diagonal shifts by an explicit parity over 4q steps, with a mod-4 form and the guarded consequences that exclude 11011 above period 4
Abstract: Let $q$ be even and let $d, a, b, c, z$ be Boolean profiles in time with $d(t+q)=d(t)$, $a(t+q)=\lnot a(t)$, $b(t+2q)=b(t)$ and $c(t+2q)=\lnot c(t)$, where $b(t+1)=b(t)\oplus(a(t)\lor d(t))$ and $z(t+1)=z(t)\oplus(c(t)\lor b(t))$. Then $z(t+4q)=z(t)\oplus\eta$ for every $t$, with $\eta=\mathrm{parity}(q/2)\oplus E_q(d)$ and $E_q(d)$ the XOR of $d$ at the even ticks $0,2,\dots,q-2$ (`Rule30Submission.shift_law`). On the kit's evolution the right diagonals $D_j(t)=x_t(t-j)$ of every start obey this recurrence, so the law holds on actual diagonals under the same period hypotheses (`rightDiag_shift_law`). For $q\equiv0\pmod 4$, $E_q(d)$ is a XOR of $h(4s)\oplus h(4s+1)$ for $d(t+1)=d(t)\oplus h(t)$ (`E_mod4`); if $d$ complements at $q/2$, then $\eta=\mathrm{parity}(q/2)\oplus\mathrm{parity}(q/4)$, which is false for $q\equiv0\pmod 8$ and true at $q=4$ (`eta_false_of_antiperiod`, `eta_four`); if $d$ has period $q/2$, then $\eta$ is false (`eta_false_of_period_half`). The kit already has the general doubling criterion for right diagonals (`Rule30RightPeriods.S_rule`, and the T-function lifting criterion); what is added is this explicit shift law after the doubling letters 101 and its mod-4 forms. The proof pairs ticks three times: $i$ with $i+2q$, consecutive ticks, and $k$ with $k+q/2$; a window over a full period makes the result independent of $t$. These are conditional profile statements: the translation from a finite seed's prefix-period letters to the hypotheses is derived by hand, not formalized here, so `eta_false_of_antiperiod` alone is not a kernel-checked finite-seed word exclusion. Nothing here concerns the centre column or decides Problem 1.
Keywords: [rule 30, Rule 30 Prize, right diagonals, period doubling, parity, shift law, Lean 4, LeanLink, partial result]
Sources: ["[The Rule 30 Prize kit](https://github.com/WolframInstitute/Rule30PrizeKit)", "[The Wolfram · Collatz · Mahler record](https://github.com/ghywel/placego)"]
Links: ["[Rule 30 Prizes](https://rule30prize.org/)", "[Rule30RightPeriods in the kit](https://github.com/WolframInstitute/Rule30PrizeKit/blob/main/lean/Ruliology/CellularAutomata/Rule30RightPeriods.lean)"]
---

## The question

Read rule 30 along its right diagonals: $D_j(t) = x_t(t - j)$, the cell $j$ places in from a moving right edge. Every
step of the rule, $\text{left} \oplus (\text{centre} \lor \text{right})$, becomes
$D_j(t+1) = D_j(t) \oplus (D_{j-1}(t) \lor D_{j-2}(t))$: each diagonal is a running XOR of the OR of the two to its
right. A running XOR of a periodic input either keeps the input's period or doubles it, and it doubles exactly when
the input has odd weight over one period. That criterion is known: the kit has it as `Rule30RightPeriods.S_rule` for the
single seed and through its T-function lifting for every finite row.

Write $Q_d$ for the period of the whole prefix $D_0, \dots, D_d$ and $x_d = [Q_d > Q_{d-1}]$ for the *doubling
letters*. This essay asks what the letters $101$ force on the letter after them, and answers it with an exact
parity, valid at every time.

## The theorems

- **The shift law** (`shift_law`). For even $q$ and profiles $d, a, b, c, z : \mathbb{N} \to \{0,1\}$ with
  $d(t+q) = d(t)$, $a(t+q) = \lnot a(t)$, $b(t+2q) = b(t)$, $c(t+2q) = \lnot c(t)$,
  $b(t+1) = b(t) \oplus (a(t) \lor d(t))$ and $z(t+1) = z(t) \oplus (c(t) \lor b(t))$:
  $$z(t + 4q) = z(t) \oplus \eta, \qquad \eta = \mathrm{parity}(q/2) \oplus E_q(d), \qquad E_q(d) = \bigoplus_{s < q/2} d(2s).$$
- **On actual diagonals** (`rightDiag_step`, `rightDiag_shift_law`). For every start, $D_j$ obeys the recurrence
  above, so the shift law holds for $(d, a, b, c, z) = (D_{j-1}, D_j, D_{j+1}, D_{j+2}, D_{j+3})$ under the same
  period hypotheses.
- **Mod-4 form** (`E_mod4`). For $q \equiv 0 \pmod 4$ and $d(t+1) = d(t) \oplus h(t)$:
  $E_q(d) = \bigoplus_{s < q/4} [h(4s) \oplus h(4s+1)]$.
- **Guarded consequences.** If $d$ complements at $q/2$, then $\eta = \mathrm{parity}(q/2) \oplus \mathrm{parity}(q/4)$
  (`eta_of_antiperiod`): false for $q \equiv 0 \pmod 8$ (`eta_false_of_antiperiod`) and true at $q = 4$ (`eta_four`).
  If $d$ has period $q/2$, $\eta$ is false (`eta_false_of_period_half`).
- **Running shift** (`running_shift`). If $D(t+1) = D(t) \oplus g(t)$ with $g$ $p$-periodic, then
  $D(t + p) = D(t) \oplus \bigoplus_{i<p} g(i)$.

## Why the letters 101 give these hypotheses

Take $q = Q_{j-1}$ and letters $x_j x_{j+1} x_{j+2} = 101$. Every diagonal up to $j-1$ has a period dividing $q$, so
$d = D_{j-1}$ is $q$-periodic. The letter $x_j = 1$ means $D_j$ does not repeat after $q$; by `running_shift` its forcing
has odd weight over $q$, so $D_j$ complements at $q$. The letter $x_{j+1} = 0$ means $D_{j+1}$ repeats after $2q$, and
$x_{j+2} = 1$ means $D_{j+2}$ complements at $2q$. The shift law then gives $D_{j+3}(t + 4q) = D_{j+3}(t) \oplus \eta$:
the next letter is $x_{j+3} = \eta$. This translation is a short hand argument; the module proves the shift law and
`running_shift`, not the letter-level statement.

So $11011$ cannot occur above prefix period $4$: its middle $101$ has $d$ itself just doubled into $q \ge 8$, and
then $\eta$ is false. At $q = 4$, $\eta$ is true, and the single seed's word does begin $1\,1\,0\,1\,1$.

## The single seed's first 101 events

The single seed's right diagonals to $t = 2048$, their doubling letters, and each $101$ event with $q \ge 2$: the
letter after it, against the theorem's $\eta$.

```wl
T = 2048; ca = CellularAutomaton[30, {{1}, 0}, T];
dg[j_, t_] := ca[[t + 1, T + 1 + t - j]];
lp[j_] := SelectFirst[2^Range[0, 9], Function[p, AllTrue[Range[0, T - p - 1], dg[j, #] == dg[j, # + p] &]]];
per = lp /@ Range[0, 19]; Q = FoldList[Max, per]; x = Prepend[Boole[Rest[Q] > Most[Q]], Missing[]];
events = Select[Range[3, 16], x[[#]] == 1 && x[[# + 1]] == 0 && x[[# + 2]] == 1 &];
Grid[Prepend[Table[With[{q = Q[[j - 1]]}, {j - 1, q, Mod[q/2, 2] ~BitXor~ Fold[BitXor, 0, Table[dg[j - 2, 2 s], {s, 0, q/2 - 1}]], x[[j + 3]]}], {j, events}], {"j", "q", "eta", "next letter"}], Frame -> All]
```

(The table indexes the diagonal $j$ from $0$.) At $q = 4$ the law gives $\eta = 1$, the exception, and at $q = 16$ it
gives $\eta = 0$; in both cases the next letter agrees. This computation illustrates the hand translation above; it
proves nothing beyond these events.

## The formal proof

The module, built against the kit at the verifier's commit:

```wl
Needs["Wolfram`LeanLink`"];
$Rule30PrizeKit = Environment["RULE30PRIZE_KIT"];
DirectoryQ[$Rule30PrizeKit]
```

```wl
rule30Submission = LeanImportString["import Rule30PrizeKit

/-!
# Right-diagonal profiles of rule 30: the 101 shift law and its mod-4 forms

Profiles are `Nat → Bool`. `xr f n` is the XOR of `f 0, …, f (n - 1)`.

* `shift_law`: let `q` be even. Suppose that `d` has period `q`, `a` complements at `q`, `b` has period `2q` and `c`
  complements at `2q`, with `b (t+1) = b t xor (a t || d t)` and `z (t+1) = z t xor (c t || b t)`. Then
  `z (t + 4q) = z t xor eta q d` for every `t`, where `eta q d = parity (q/2) xor E q d` and `E q d` is the XOR of
  `d` at the even ticks `0, 2, …, q - 2`.
* `E_mod4`: for `q ≡ 0 mod 4` and `d (t+1) = d t xor h t`, `E q d` is the XOR of `h (4s) xor h (4s+1)`, `s < q/4`.
* `eta_of_antiperiod`, `eta_false_of_antiperiod`, `eta_four`: if `d` complements at `q/2`, then
  `eta q d = parity (q/2) xor parity (q/4)`. This is `false` for `q ≡ 0 mod 8` and `true` at `q = 4`.
* `eta_false_of_period_half`: if `d` has period `q/2` (`q ≡ 0 mod 4`), then `eta q d = false`.
* `rightDiag_step`, `rightDiag_shift_law`: the right diagonals `D j t = x_t (t - j)` of the kit's
  `Rule30Realization.evol` satisfy `D j (t+1) = D j t xor (D (j-1) t || D (j-2) t)` for every start, so the
  shift law holds on actual diagonals under the same period hypotheses.
* `running_shift`: a running XOR of a `p`-periodic forcing shifts by `xr g p` over `p` steps.

These are conditional profile statements. Turning the doubling letters of a finite seed's prefix periods into the
hypotheses is not formalized here, and `eta_false_of_antiperiod` alone is not a finite-seed word exclusion.
-/

namespace Rule30Submission

open Ruliology.CellularAutomata

/-- XOR of `f 0, …, f (n - 1)`. -/
def xr (f : Nat → Bool) : Nat → Bool
  | 0 => false
  | n + 1 => xor (xr f n) (f n)

def parity (n : Nat) : Bool := decide (n % 2 = 1)

theorem parity_succ (n : Nat) : parity (n + 1) = !parity n := by
  unfold parity
  rcases Nat.mod_two_eq_zero_or_one n with h | h
  · have h' : (n + 1) % 2 = 1 := by omega
    simp [h, h']
  · have h' : (n + 1) % 2 = 0 := by omega
    simp [h, h']

theorem xr_add (f : Nat → Bool) (n m : Nat) :
    xr f (n + m) = xor (xr f n) (xr (fun i => f (n + i)) m) := by
  induction m with
  | zero => simp [xr]
  | succ m ih =>
    rw [Nat.add_succ]
    simp only [xr]
    rw [ih, Bool.xor_assoc]

theorem xr_xor (f g : Nat → Bool) (n : Nat) :
    xr (fun i => xor (f i) (g i)) n = xor (xr f n) (xr g n) := by
  induction n with
  | zero => rfl
  | succ n ih =>
    simp only [xr]
    rw [ih]
    cases xr f n <;> cases xr g n <;> cases f n <;> cases g n <;> rfl

theorem xr_congr {f g : Nat → Bool} (n : Nat) (h : ∀ i, i < n → f i = g i) : xr f n = xr g n := by
  induction n with
  | zero => rfl
  | succ n ih =>
    simp only [xr]
    rw [ih (fun i hi => h i (by omega)), h n (by omega)]

theorem xr_false (n : Nat) : xr (fun _ => false) n = false := by
  induction n with
  | zero => rfl
  | succ n ih => simp only [xr]; rw [ih]; rfl

theorem xr_not (f : Nat → Bool) (n : Nat) : xr (fun i => !f i) n = xor (parity n) (xr f n) := by
  induction n with
  | zero => rfl
  | succ n ih =>
    simp only [xr]
    rw [ih, parity_succ]
    cases parity n <;> cases xr f n <;> cases f n <;> rfl

theorem xr_true (n : Nat) : xr (fun _ => true) n = parity n := by
  have := xr_not (fun _ => false) n
  rw [xr_false] at this
  simpa using this

/-- Pair the two halves of a window of length `n + n`. -/
theorem xr_halves (f : Nat → Bool) (n : Nat) :
    xr f (n + n) = xr (fun i => xor (f i) (f (n + i))) n := by
  rw [xr_add, xr_xor]

/-- Pair consecutive terms. -/
theorem xr_pairs (f : Nat → Bool) (m : Nat) :
    xr f (2 * m) = xr (fun k => xor (f (2 * k)) (f (2 * k + 1))) m := by
  induction m with
  | zero => rfl
  | succ m ih =>
    rw [show 2 * (m + 1) = 2 * m + 1 + 1 by omega]
    simp only [xr]
    rw [ih]
    cases xr (fun k => xor (f (2 * k)) (f (2 * k + 1))) m <;> cases f (2 * m) <;> cases f (2 * m + 1) <;> rfl

/-- A running XOR over `n` steps. -/
theorem integral {z g : Nat → Bool} (h : ∀ t, z (t + 1) = xor (z t) (g t)) (t n : Nat) :
    z (t + n) = xor (z t) (xr (fun i => g (t + i)) n) := by
  induction n with
  | zero => simp [xr]
  | succ n ih =>
    rw [show t + (n + 1) = (t + n) + 1 by omega, h, ih]
    simp only [xr]
    rw [Bool.xor_assoc]

/-- A window over a full period has the same XOR wherever it starts. -/
theorem xr_window {g : Nat → Bool} {n : Nat} (hg : ∀ t, g (t + n) = g t) (t : Nat) :
    xr (fun i => g (t + i)) n = xr g n := by
  induction t with
  | zero => simp
  | succ t ih =>
    have e1 : xr (fun i => g (t + i)) (1 + n) = xor (g t) (xr (fun i => g (t + 1 + i)) n) := by
      rw [xr_add]
      simp [xr, Nat.add_assoc]
    have e2 : xr (fun i => g (t + i)) (n + 1) = xor (xr (fun i => g (t + i)) n) (g t) := by
      simp only [xr]
      rw [hg t]
    rw [Nat.add_comm 1 n, e2] at e1
    rw [← ih]
    revert e1
    cases xr (fun i => g (t + i)) n <;> cases g t <;> cases xr (fun i => g (t + 1 + i)) n <;> simp

/-- **Running shift**: a running XOR of a `p`-periodic forcing shifts by the forcing's parity over `p` steps. -/
theorem running_shift {D g : Nat → Bool} {p : Nat} (hs : ∀ t, D (t + 1) = xor (D t) (g t))
    (hg : ∀ t, g (t + p) = g t) (t : Nat) : D (t + p) = xor (D t) (xr g p) := by
  rw [integral hs t p, xr_window hg t]

/-- The XOR of `d` at the even ticks `0, 2, …, q - 2`. -/
def E (q : Nat) (d : Nat → Bool) : Bool := xr (fun s => d (2 * s)) (q / 2)

def eta (q : Nat) (d : Nat → Bool) : Bool := xor (parity (q / 2)) (E q d)

/-- **The 101 shift law.** -/
theorem shift_law (q : Nat) (hq : q % 2 = 0) (d a b c z : Nat → Bool)
    (hd : ∀ t, d (t + q) = d t) (ha : ∀ t, a (t + q) = !a t)
    (hb : ∀ t, b (t + 2 * q) = b t) (hc : ∀ t, c (t + 2 * q) = !c t)
    (hbs : ∀ t, b (t + 1) = xor (b t) (a t || d t))
    (hzs : ∀ t, z (t + 1) = xor (z t) (c t || b t)) :
    ∀ t, z (t + 4 * q) = xor (z t) (eta q d) := by
  obtain ⟨G, hG⟩ : ∃ G : Nat → Bool, ∀ s, G s = (c s || b s) := ⟨_, fun _ => rfl⟩
  obtain ⟨H, hH⟩ : ∃ H : Nat → Bool, ∀ s, H s = (a s || d s) := ⟨_, fun _ => rfl⟩
  have hzs' : ∀ t, z (t + 1) = xor (z t) (G t) := fun t => by rw [hG]; exact hzs t
  have hbs' : ∀ t, b (t + 1) = xor (b t) (H t) := fun t => by rw [hH]; exact hbs t
  have hGp : ∀ s, G (s + 4 * q) = G s := by
    intro s
    rw [hG, hG, show s + 4 * q = (s + 2 * q) + 2 * q by omega, hc, hc, hb, hb, Bool.not_not]
  -- the window total at time 0
  have step1 : xr G (4 * q) = xr b (2 * q) := by
    rw [show 4 * q = 2 * q + 2 * q by omega, xr_halves]
    rw [xr_congr (2 * q) (g := fun i => !b i) (fun i _ => by
      rw [hG, hG, show 2 * q + i = i + 2 * q by omega, hc, hb]
      cases c i <;> cases b i <;> rfl)]
    have hp : parity (2 * q) = false := by unfold parity; simp
    rw [xr_not, hp, Bool.false_xor]
  have step2 : xr b (2 * q) = xr (fun k => H (2 * k)) q := by
    rw [xr_pairs]
    apply xr_congr
    intro k _
    show xor (b (2 * k)) (b (2 * k + 1)) = H (2 * k)
    rw [hbs']
    cases b (2 * k) <;> cases H (2 * k) <;> rfl
  have step3 : xr (fun k => H (2 * k)) q = eta q d := by
    rw [show q = q / 2 + q / 2 by omega, xr_halves]
    rw [show q / 2 + q / 2 = q by omega]
    rw [xr_congr (q / 2) (g := fun s => !d (2 * s)) (fun s _ => by
      show xor (H (2 * s)) (H (2 * (q / 2 + s))) = !d (2 * s)
      rw [hH, hH, show 2 * (q / 2 + s) = 2 * s + q by omega, ha, hd]
      cases a (2 * s) <;> cases d (2 * s) <;> rfl)]
    rw [xr_not]
    rfl
  intro t
  rw [integral hzs' t (4 * q), xr_window hGp t, step1, step2, step3]

/-- **Mod-4 form** of the even-tick parity. -/
theorem E_mod4 (q : Nat) (hq : q % 4 = 0) (d h : Nat → Bool) (hs : ∀ t, d (t + 1) = xor (d t) (h t)) :
    E q d = xr (fun s => xor (h (4 * s)) (h (4 * s + 1))) (q / 4) := by
  unfold E
  rw [show q / 2 = 2 * (q / 4) by omega, xr_pairs]
  apply xr_congr
  intro s _
  show xor (d (2 * (2 * s))) (d (2 * (2 * s + 1))) = xor (h (4 * s)) (h (4 * s + 1))
  rw [show 2 * (2 * s) = 4 * s by omega, show 2 * (2 * s + 1) = 4 * s + 1 + 1 by omega, hs (4 * s + 1), hs (4 * s)]
  cases d (4 * s) <;> cases h (4 * s) <;> cases h (4 * s + 1) <;> rfl

/-- If `d` complements at `q/2`, the even-tick parity is `parity (q/4)`. -/
theorem E_of_antiperiod (q : Nat) (hq : q % 4 = 0) (d : Nat → Bool) (hd : ∀ t, d (t + q / 2) = !d t) :
    E q d = parity (q / 4) := by
  unfold E
  rw [show q / 2 = q / 4 + q / 4 by omega, xr_halves]
  rw [xr_congr (q / 4) (g := fun _ => true) (fun s _ => by
    show xor (d (2 * s)) (d (2 * (q / 4 + s))) = true
    rw [show 2 * (q / 4 + s) = 2 * s + q / 2 by omega, hd]
    cases d (2 * s) <;> rfl)]
  exact xr_true (q / 4)

theorem eta_of_antiperiod (q : Nat) (hq : q % 4 = 0) (d : Nat → Bool) (hd : ∀ t, d (t + q / 2) = !d t) :
    eta q d = xor (parity (q / 2)) (parity (q / 4)) := by
  unfold eta; rw [E_of_antiperiod q hq d hd]

/-- **The 11011 exclusion**: for `q ≡ 0 mod 8`, a `d` that doubled into `q` gives `eta = false`. -/
theorem eta_false_of_antiperiod (q : Nat) (hq : q % 8 = 0) (d : Nat → Bool)
    (hd : ∀ t, d (t + q / 2) = !d t) : eta q d = false := by
  rw [eta_of_antiperiod q (by omega) d hd]
  unfold parity
  have h1 : (q / 2) % 2 = 0 := by omega
  have h2 : (q / 4) % 2 = 0 := by omega
  simp [h1, h2]

/-- The exception at `q = 4`. -/
theorem eta_four (d : Nat → Bool) (hd : ∀ t, d (t + 2) = !d t) : eta 4 d = true := by
  rw [eta_of_antiperiod 4 (by decide) d hd]
  decide

/-- If `d` has period `q/2`, the even-tick parity vanishes. -/
theorem E_of_period_half (q : Nat) (hq : q % 4 = 0) (d : Nat → Bool) (hd : ∀ t, d (t + q / 2) = d t) :
    E q d = false := by
  unfold E
  rw [show q / 2 = q / 4 + q / 4 by omega, xr_halves]
  rw [xr_congr (q / 4) (g := fun _ => false) (fun s _ => by
    show xor (d (2 * s)) (d (2 * (q / 4 + s))) = false
    rw [show 2 * (q / 4 + s) = 2 * s + q / 2 by omega, hd]
    cases d (2 * s) <;> rfl)]
  exact xr_false (q / 4)

theorem eta_false_of_period_half (q : Nat) (hq : q % 4 = 0) (d : Nat → Bool)
    (hd : ∀ t, d (t + q / 2) = d t) : eta q d = false := by
  unfold eta
  rw [E_of_period_half q hq d hd]
  unfold parity
  have h1 : (q / 2) % 2 = 0 := by omega
  simp [h1]

/-! ### Actual right diagonals -/

/-- Right diagonal `j` of the kit's evolution: `D j t = x_t (t - j)`. -/
def rightDiag (x : Int → Bool) (j : Int) (t : Nat) : Bool := Rule30Realization.evol x t ((t : Int) - j)

theorem rightDiag_step (x : Int → Bool) (j : Int) (t : Nat) :
    rightDiag x j (t + 1) = xor (rightDiag x j t) (rightDiag x (j - 1) t || rightDiag x (j - 2) t) := by
  unfold rightDiag
  show Rule30Jen.rule (Rule30Realization.evol x t (((t + 1 : Nat) : Int) - j - 1))
      (Rule30Realization.evol x t (((t + 1 : Nat) : Int) - j))
      (Rule30Realization.evol x t (((t + 1 : Nat) : Int) - j + 1)) = _
  unfold Rule30Jen.rule
  congr 1
  · congr 1; omega
  · congr 1 <;> congr 1 <;> omega

/-- **The 101 shift law on actual right diagonals.** -/
theorem rightDiag_shift_law (x : Int → Bool) (j : Int) (q : Nat) (hq : q % 2 = 0)
    (hd : ∀ t, rightDiag x (j - 1) (t + q) = rightDiag x (j - 1) t)
    (ha : ∀ t, rightDiag x j (t + q) = !rightDiag x j t)
    (hb : ∀ t, rightDiag x (j + 1) (t + 2 * q) = rightDiag x (j + 1) t)
    (hc : ∀ t, rightDiag x (j + 2) (t + 2 * q) = !rightDiag x (j + 2) t) :
    ∀ t, rightDiag x (j + 3) (t + 4 * q) = xor (rightDiag x (j + 3) t) (eta q (rightDiag x (j - 1))) := by
  apply shift_law q hq (rightDiag x (j - 1)) (rightDiag x j) (rightDiag x (j + 1)) (rightDiag x (j + 2))
    (rightDiag x (j + 3)) hd ha hb hc
  · intro t
    have := rightDiag_step x (j + 1) t
    rwa [show j + 1 - 1 = j by omega, show j + 1 - 2 = j - 1 by omega] at this
  · intro t
    have := rightDiag_step x (j + 3) t
    rwa [show j + 3 - 1 = j + 2 by omega, show j + 3 - 2 = j + 1 by omega] at this

end Rule30Submission
", "ProjectDir" -> $Rule30PrizeKit]
```

## The formal checks

The headlines, as Lean prints them:

```wl
opens = {"Rule30Submission", "Ruliology.CellularAutomata.Rule30Realization"};
heads = {"shift_law", "rightDiag_shift_law", "E_mod4", "eta_of_antiperiod", "eta_false_of_antiperiod", "eta_four", "eta_false_of_period_half", "running_shift"};
Column[rule30Submission["Rule30Submission." <> #]["TypeForm", "Open" -> opens] & /@ heads]
```

Their axioms are standard ones only:

```wl
AssociationMap[rule30Submission["Rule30Submission." <> #]["Axioms"] &, heads]
```

The kernel accepts every declaration of the module again. This is the replay the verifier runs; it comes last because it resets LeanLink's elaboration state:

```wl
rule30Submission["Rule30Submission.shift_law"]["KernelCheck"]
```

## What is not proved

- The translation from a finite seed's prefix-period letters to the theorem's hypotheses (the section above) is a
  short hand argument; it is not formalized here. So `eta_false_of_antiperiod` by itself is not a kernel-checked
  finite-seed exclusion of the word $11011$.
- In the case $\eta$ false, the theorem says the prefix period stays $4q$; it does not give the least period of
  $D_{j+3}$ itself. Individual-period monotonicity for arbitrary seeds is not used and not proved.
- The general doubling criterion is the kit's (`Rule30RightPeriods.S_rule`, and the T-function lifting); the seed echo and
  single-seed monotonicity (`per_mono_all`, `no_three`) are known and not restated as headlines.
- The mod-4 cascade beyond the identities stated, and the universal start of the doubling word, are not in this module.
- Nothing here concerns the centre column or decides Problem 1. We found no such shift law in the kit's catalog or
  the submissions list as we read them, which is a statement about our search, not a global novelty determination.
- The Wolfram Language computation above illustrates the hand translation on two events; the theorems do not depend on it.

## Provenance

The 101 lemma and its mod-4 form were found by hand by Claude (Anthropic) on 2026-10-28 and read independently by
GPT (OpenAI); GPT wrote the exact delivery scope, including the profile-level hypotheses and the guards, and read the
formal source. Claude formalized it in core Lean on the kit's `evol` on 2026-10-29.

## References

[1] S. Wolfram, [*Announcing the Rule 30 Prizes*](https://writings.stephenwolfram.com/2019/10/announcing-the-rule-30-prizes/), Wolfram Writings, 2019.

[2] Wolfram Institute, [*The Rule 30 Prize kit*](https://github.com/WolframInstitute/Rule30PrizeKit), 2026: `Rule30Realization.evol`, `Rule30RightPeriods.S_rule`, `per_mono_all`, `no_three`, `TFunctionCycles.lift_iff`.
