#!/usr/bin/env python3
"""gen_black_end38.py: write BlackEnd38L.lean, entry 38's black end at q = 7 and 9 .. 13 by literal stages (L552).

RUN-ON:     cpu (Python 3, standard library); seconds
COMMAND:    python3 tests/probes/lean/gen_black_end38.py tests/probes/lean/BlackEnd38base.lean OUT.lean
            then `lake env lean OUT.lean` (about 1.3 MB of literals, so not kept in git; BE_CASES="7" limits the
            cases for a smoke test).

Why. BlackEnd38.lean proves the six cases with one kernel check each (`checkTwo`); those grew to about 12 GB and were
parked (L525). GC951 proposed literal stage masks, one check per edge. This generator mirrors the Lean definitions
`inner`, `succSet`, `img`, `pre`, `word` and `full0` bit for bit, computes every stage, checks every inclusion in
Python first (BE-C1), and emits:
  - per q, literals A_i (the chain from full0, i < m = n0 (q + 1)), C_ph (the fixed point's phases) and G_k,ph
    (k = 1 .. 6 peel stages, G_0 = C);
  - one `decide +kernel` lemma per edge (chain, link, cycle, peel) and per final colConst;
  - the fixed proof section (stage membership, peel membership, the core with Theorem A), then the assembly.
Predictions: CHAT-LEDGER L552 (BE-C1, BE-P1 .. P3).
OUTCOME, 2026-10-10 06:00 BST (M5): BE-C1 PASS; BE-P1, BE-P2 and BE-P3 HELD.
  - C1: every inclusion holds in Python, each fixed point is exact, and the final peeled sets total 218, 200, 214,
    228, 242 and 256 at q = 7, 9 .. 13: SG's component sizes, 218 and 14q + 74, exactly.
  - P1: BlackEnd38L.lean (1,277,984 bytes, sha256 8a07be2115811fc3) compiles. `black_end_two_sided` depends on
    propext, Classical.choice and Quot.sound only; no sorryAx. Two smoke runs at q = 7 came first:
    - a kernel "deep recursion" in `A7 0 = full0 := rfl` (the kernel unfolds full0's 8192-step scan), fixed by the
      edge lemmas' maxRecDepth;
    - the single `cert` term was split into named lemmas to find it.
  - P2: the peak was 1.46 GB (top MEM, 5 s samples), against about 12 GB for the parked one-shot checks.
  - P3: the profiler, at a 10 s threshold, reported no declaration. The whole build took 456 s, of which type
    checking was 437 s.
  - Reproducibility: BlackEnd38base.lean is the shared part (compiles alone in 27 s, 0.8 GB). This generator, run on
    it, writes a file byte-identical to the one that compiled.
"""
import hashlib
import os
import sys

FULL = (1 << 8192) - 1
CASES = [(7, 2), (9, 1), (10, 1), (11, 1), (12, 1), (13, 1)]
K = 6


def inner(r):
    return ((r << 1) ^ (r | (r >> 1))) & 4094


def succ(w, k):
    i = inner(k)
    if ((i >> 6) & 1) != w:
        return ()
    return (i, i | 1, i | 4096, i | 4097)


def members(S):
    out, k = [], 0
    while S:
        if S & 1:
            out.append(k)
        S >>= 1
        k += 1
    return out


def img(S, w):
    acc = 0
    for k in members(S):
        for y in succ(w, k):
            acc |= 1 << y
    return acc


def pre(S, T, w):
    acc = 0
    for k in members(S):
        if any((T >> y) & 1 for y in succ(w, k)):
            acc |= 1 << k
    return acc


def word(q, ph):
    return 0 if ph % (q + 1) == 0 else 1


FULL0 = sum(1 << r for r in range(8192) if not (r >> 6) & 1)


def sub(X, Y):
    return X & Y == X


def col_const(G):
    bits = {(r >> 5) & 1 for r in members(G)}
    return len(bits) <= 1


def stages(q, n0):
    m = n0 * (q + 1)
    A = [FULL0]
    for i in range(m - 1):
        A.append(img(A[i], word(q, i + 1)))
    C = [img(A[m - 1], word(q, m))]
    for ph in range(q):
        C.append(img(C[ph], word(q, ph + 1)))
    G = [C]
    for k in range(K):
        G.append([pre(G[k][ph], G[k][(ph + 1) % (q + 1)], word(q, ph + 1)) for ph in range(q + 1)])
    ok = all(sub(img(A[i], word(q, i + 1)), A[i + 1]) for i in range(m - 1))
    ok &= sub(img(A[m - 1], word(q, m)), C[0])
    ok &= all(sub(img(C[ph], word(q, ph + 1)), C[(ph + 1) % (q + 1)]) for ph in range(q + 1))
    ok &= all(col_const(G[K][ph]) for ph in range(q + 1))
    fixed = img(C[q], word(q, q + 1)) == C[0]
    return m, A, C, G, ok, fixed


def lit(n):
    return '0x%x' % n if n else '0'


def fn_def(name, vals, default='0'):
    lines = ['def %s : ℕ → ℕ' % name]
    for i, v in enumerate(vals):
        lines.append('  | %d => %s' % (i, v if isinstance(v, str) else lit(v)))
    lines.append('  | _ => %s' % default)
    return '\n'.join(lines) + '\n'


def opts():
    return 'set_option maxRecDepth 100000 in\nset_option maxHeartbeats 0 in\n'


def ors(var, n):
    return '(show %s by omega) with %s' % (' ∨ '.join('%s = %d' % (var, j) for j in range(n)),
                                           ' | '.join(['rfl'] * n))


def per_q(q, n0):
    m, A, C, G, ok, fixed = stages(q, n0)
    total = sum(len(members(g)) for g in G[K])
    out = ['\n/-! ## q = %d (n0 = %d, m = %d) -/\n' % (q, n0, m)]
    out.append(fn_def('A%d' % q, ['full0'] + [lit(a) for a in A[1:]]))
    out.append(fn_def('C%d' % q, C))
    for k in range(1, K + 1):
        out.append(fn_def('G%d_%d' % (q, k), G[k]))
    out.append('def G%d : ℕ → ℕ → ℕ\n  | 0, ph => C%d ph\n%s  | _, _ => 0\n' % (
        q, q, ''.join('  | %d, ph => G%d_%d ph\n' % (k, q, k) for k in range(1, K + 1))))
    Q = q + 1
    # edge lemmas, stated exactly as the goals appear after `rcases ... with rfl`
    for i in range(m - 1):
        out.append(opts() + 'lemma ch%d_%d : sub (img (A%d %d) (word %d (%d + 1))) (A%d (%d + 1)) = true := by '
                   'decide +kernel\n' % (q, i, q, i, q, i, q, i))
    out.append(opts() + 'lemma ln%d : sub (img (A%d (%d - 1)) (word %d %d)) (C%d 0) = true := by decide +kernel\n' % (
        q, q, m, q, m, q))
    for ph in range(Q):
        out.append(opts() + 'lemma cy%d_%d : sub (img (C%d %d) (word %d (%d + 1))) (C%d ((%d + 1) %% (%d + 1))) = true '
                   ':= by decide +kernel\n' % (q, ph, q, ph, q, ph, q, ph, q))
    for k in range(K):
        for ph in range(Q):
            out.append(opts() + 'lemma pe%d_%d_%d : sub (pre (G%d %d %d) (G%d %d ((%d + 1) %% (%d + 1))) (word %d (%d + 1))) '
                       '(G%d (%d + 1) %d) = true := by decide +kernel\n' % (
                           q, k, ph, q, k, ph, q, k, ph, q, q, ph, q, k, ph))
    for ph in range(Q):
        out.append(opts() + 'lemma co%d_%d : colConst (G%d %d %d) = true := by decide +kernel\n' % (q, ph, q, K, ph))
    # assembly
    out.append('lemma chain%d : ∀ i, i + 1 < %d → sub (img (A%d i) (word %d (i + 1))) (A%d (i + 1)) = true := by\n'
               '  intro i hi\n  rcases %s\n%s' % (q, m, q, q, q, ors('i', m - 1),
                                                   ''.join('  · exact ch%d_%d\n' % (q, i) for i in range(m - 1))))
    out.append('lemma cycle%d : ∀ ph, ph ≤ %d → sub (img (C%d ph) (word %d (ph + 1))) (C%d ((ph + 1) %% (%d + 1))) = '
               'true := by\n  intro ph hph\n  rcases %s\n%s' % (
                   q, q, q, q, q, q, ors('ph', Q), ''.join('  · exact cy%d_%d\n' % (q, ph) for ph in range(Q))))
    for k in range(K):
        out.append('lemma peel%d_%d : ∀ ph, ph ≤ %d → sub (pre (G%d %d ph) (G%d %d ((ph + 1) %% (%d + 1))) '
                   '(word %d (ph + 1))) (G%d (%d + 1) ph) = true := by\n  intro ph hph\n  rcases %s\n%s' % (
                       q, k, q, q, k, q, k, q, q, q, k, ors('ph', Q),
                       ''.join('  · exact pe%d_%d_%d\n' % (q, k, ph) for ph in range(Q))))
    out.append('lemma peel%d : ∀ k ph, k < %d → ph ≤ %d → sub (pre (G%d k ph) (G%d k ((ph + 1) %% (%d + 1))) '
               '(word %d (ph + 1))) (G%d (k + 1) ph) = true := by\n  intro k ph hk hph\n  rcases %s\n%s' % (
                   q, K, q, q, q, q, q, q, ors('k', K), ''.join('  · exact peel%d_%d ph hph\n' % (q, k) for k in range(K))))
    out.append('lemma col%d : ∀ ph, ph ≤ %d → colConst (G%d %d ph) = true := by\n  intro ph hph\n  rcases %s\n%s' % (
        q, q, q, K, ors('ph', Q), ''.join('  · exact co%d_%d\n' % (q, ph) for ph in range(Q))))
    out.append(opts() + 'lemma a0_%d : A%d 0 = full0 := rfl\n' % (q, q))   # the kernel unfolds full0 (8192 steps)
    out.append('lemma g0_%d : ∀ ph, G%d 0 ph = C%d ph := fun _ => rfl\n' % (q, q, q))
    out.append('lemma edge%d : ∀ i, sub (img (stage %d %d A%d C%d i) (word %d (i + 1))) (stage %d %d A%d C%d (i + 1)) = '
               'true :=\n  hedge_of %d %d A%d C%d (by norm_num) (by norm_num) (by norm_num) chain%d ln%d cycle%d\n' % (
                   q, q, m, q, q, q, q, m, q, q, q, m, q, q, q, q, q))
    out.append('theorem cert%d : Cert %d %d %d A%d C%d G%d :=\n'
               '  ⟨by norm_num, by norm_num, by norm_num, a0_%d, edge%d, g0_%d, peel%d, col%d⟩\n' % (
                   q, q, m, K, q, q, q, q, q, q, q, q))
    return ''.join(out), ok, fixed, total, m


PROOF = r'''
/-! ## Literal stages (GC951): membership along the stages, and the core -/

def sub (X Y : ℕ) : Bool := X &&& Y == X

lemma sub_mem {X Y r : ℕ} (h : sub X Y = true) (hr : X.testBit r = true) : Y.testBit r = true := by
  have h' : X &&& Y = X := by simpa [sub] using h
  have := congrArg (fun z => z.testBit r) h'
  simp only [Nat.testBit_and, hr, Bool.true_and] at this
  exact this

/-- Column c reads 0 1^q periodically from time a, the 0 first. -/
def Reads0 (x0 : ℤ → Bool) (c : ℤ) (q a : ℕ) : Prop :=
  ∀ n i, i ≤ q → ev x0 (a + n * (q + 1) + i) c = decide (i ≠ 0)

lemma word_at (x0 : ℤ → Bool) (c : ℤ) (q a : ℕ) (hr : Reads0 x0 c q a) (i : ℕ) :
    (ev x0 (a + i) c).toNat = word q i := by
  have hsplit : a + i = a + (i / (q + 1)) * (q + 1) + i % (q + 1) := by
    have := Nat.div_add_mod i (q + 1)
    rw [mul_comm] at this; omega
  have hmod : i % (q + 1) ≤ q := Nat.lt_succ_iff.mp (Nat.mod_lt _ (by omega))
  rw [hsplit, hr _ _ hmod]
  unfold word
  by_cases h : i % (q + 1) = 0 <;> simp [h]

/-- The stage at time a + i: the chain A before m, then the cycle C. -/
def stage (q m : ℕ) (A C : ℕ → ℕ) (i : ℕ) : ℕ := if i < m then A i else C (i % (q + 1))

lemma mod_succ (q i : ℕ) (hq : 1 ≤ q) : (i + 1) % (q + 1) = (i % (q + 1) + 1) % (q + 1) := by
  rw [Nat.add_mod i 1, Nat.mod_eq_of_lt (show 1 < q + 1 by omega)]

lemma word_succ (q i : ℕ) (hq : 1 ≤ q) : word q (i + 1) = word q (i % (q + 1) + 1) := by
  unfold word; rw [mod_succ q i hq]

lemma hedge_of (q m : ℕ) (A C : ℕ → ℕ) (hq : 1 ≤ q) (hm : 1 ≤ m) (hmq : m % (q + 1) = 0)
    (hchain : ∀ i, i + 1 < m → sub (img (A i) (word q (i + 1))) (A (i + 1)) = true)
    (hlink : sub (img (A (m - 1)) (word q m)) (C 0) = true)
    (hcyc : ∀ ph, ph ≤ q → sub (img (C ph) (word q (ph + 1))) (C ((ph + 1) % (q + 1))) = true) :
    ∀ i, sub (img (stage q m A C i) (word q (i + 1))) (stage q m A C (i + 1)) = true := by
  intro i
  unfold stage
  by_cases h1 : i + 1 < m
  · rw [if_pos (by omega), if_pos h1]; exact hchain i h1
  · by_cases h2 : i + 1 = m
    · rw [if_pos (by omega), if_neg (by omega), show i = m - 1 by omega, show m - 1 + 1 = m by omega, hmq]
      exact hlink
    · rw [if_neg (by omega), if_neg (by omega), word_succ q i hq, mod_succ q i hq]
      exact hcyc _ (Nat.lt_succ_iff.mp (Nat.mod_lt _ (by omega)))

/-- The literal certificate for one q. -/
def Cert (q m K : ℕ) (A C : ℕ → ℕ) (G : ℕ → ℕ → ℕ) : Prop :=
  1 ≤ q ∧ 1 ≤ m ∧ m % (q + 1) = 0 ∧ A 0 = full0 ∧
  (∀ i, sub (img (stage q m A C i) (word q (i + 1))) (stage q m A C (i + 1)) = true) ∧
  (∀ ph, G 0 ph = C ph) ∧
  (∀ k ph, k < K → ph ≤ q → sub (pre (G k ph) (G k ((ph + 1) % (q + 1))) (word q (ph + 1))) (G (k + 1) ph) = true) ∧
  (∀ ph, ph ≤ q → colConst (G K ph) = true)

lemma stage_mem (x0 : ℤ → Bool) (c : ℤ) (q a m : ℕ) (A C : ℕ → ℕ) (hr : Reads0 x0 c q a) (hm : 1 ≤ m)
    (hA0 : A 0 = full0)
    (hedge : ∀ i, sub (img (stage q m A C i) (word q (i + 1))) (stage q m A C (i + 1)) = true) :
    ∀ i, (stage q m A C i).testBit (win x0 c (a + i)) = true := by
  intro i
  induction i with
  | zero =>
    rw [show stage q m A C 0 = full0 by simp [stage, show 0 < m by omega, hA0]]
    apply full0_mem _ (win_lt x0 c _)
    rw [win_bit x0 c _ 6 (by norm_num), show c - 6 + ((6 : ℕ) : ℤ) = c by push_cast; ring]
    have := hr 0 0 (by omega)
    simpa using this
  | succ i ih =>
    have hs := succ_mem x0 c (a + i)
    rw [show (ev x0 (a + i + 1) c).toNat = word q (i + 1) from word_at x0 c q a hr (i + 1)] at hs
    exact sub_mem (hedge i) (img_mem _ _ _ _ (win_lt x0 c _) ih hs)

lemma peel_mem_lit (x0 : ℤ → Bool) (c : ℤ) (q a m K : ℕ) (A C : ℕ → ℕ) (G : ℕ → ℕ → ℕ)
    (hr : Reads0 x0 c q a) (hcert : Cert q m K A C G) :
    ∀ k, k ≤ K → ∀ i, m ≤ i → (G k (i % (q + 1))).testBit (win x0 c (a + i)) = true := by
  obtain ⟨hq, hm, _, hA0, hedge, hG0, hpeel, _⟩ := hcert
  have hS := stage_mem x0 c q a m A C hr hm hA0 hedge
  intro k
  induction k with
  | zero =>
    intro _ i hi
    have := hS i
    rwa [show stage q m A C i = C (i % (q + 1)) by simp [stage, show ¬ i < m by omega], ← hG0] at this
  | succ k ih =>
    intro hk i hi
    have hph : i % (q + 1) ≤ q := Nat.lt_succ_iff.mp (Nat.mod_lt _ (by omega))
    have h1 := ih (by omega) i hi
    have h2 := ih (by omega) (i + 1) (by omega)
    rw [mod_succ q i hq] at h2
    have hs := succ_mem x0 c (a + i)
    rw [show (ev x0 (a + i + 1) c).toNat = word q (i + 1) from word_at x0 c q a hr (i + 1), word_succ q i hq] at hs
    exact sub_mem (hpeel k _ (by omega) hph) (pre_mem _ _ _ _ _ (win_lt x0 c _) h1 hs h2)

/-- The core: a leftmost black cell at or left of column c - 1. -/
theorem core_lit (q m K : ℕ) (A C : ℕ → ℕ) (G : ℕ → ℕ → ℕ) (hcert : Cert q m K A C G) (x0 : ℤ → Bool) (c : ℤ)
    (L : ℕ) (hc : x0 (c - 1 - L) = true) (hl : ∀ j < c - 1 - L, x0 j = false) (a : ℕ) (hr : Reads0 x0 c q a) :
    False := by
  have P := peel_mem_lit x0 c q a m K A C G hr hcert K le_rfl
  have hcol := hcert.2.2.2.2.2.2.2
  have split : ∀ t, a ≤ t → t = a + ((t - a) / (q + 1)) * (q + 1) + (t - a) % (q + 1) := by
    intro t ht
    have := Nat.div_add_mod (t - a) (q + 1)
    rw [mul_comm] at this; omega
  have hmod : ∀ t, (t - a) % (q + 1) ≤ q := fun t => Nat.lt_succ_iff.mp (Nat.mod_lt _ (by omega))
  apply no_two_periodic x0 (c - 1) L hc hl (q + 1) (a + m) (by omega)
  · intro t ht
    have h1 := P (t - a) (by omega)
    have h2 := P (t - a + (q + 1)) (by omega)
    rw [Nat.add_mod_right] at h2
    have := colConst_spec _ (hcol _ (hmod t)) _ _ (win_lt x0 c _) (win_lt x0 c _) h1 h2
    rw [win_bit x0 c _ 5 (by norm_num), win_bit x0 c _ 5 (by norm_num)] at this
    rw [show c - 6 + ((5 : ℕ) : ℤ) = c - 1 by push_cast; ring] at this
    rw [show a + (t - a + (q + 1)) = t + (q + 1) by omega, show a + (t - a) = t by omega] at this
    exact this
  · intro t ht
    have e1 := split t (by omega)
    have h0 := hr ((t - a) / (q + 1)) ((t - a) % (q + 1)) (hmod t)
    have h1 := hr ((t - a) / (q + 1) + 1) ((t - a) % (q + 1)) (hmod t)
    rw [show c - 1 + 1 = c by ring, e1, show a + (t - a) / (q + 1) * (q + 1) + (t - a) % (q + 1) + (q + 1) =
      a + ((t - a) / (q + 1) + 1) * (q + 1) + (t - a) % (q + 1) by ring, h0, h1]

/-- Any leftmost black cell: re-base time when it lies right of column c - 1. -/
theorem no_black_word_lit (q m K : ℕ) (A C : ℕ → ℕ) (G : ℕ → ℕ → ℕ) (hcert : Cert q m K A C G) (x0 : ℤ → Bool)
    (e : ℤ) (he : x0 e = true) (hl : ∀ j < e, x0 j = false) (c : ℤ) (a : ℕ) (hr : Reads0 x0 c q a) : False := by
  by_cases hec : e ≤ c - 1
  · exact core_lit q m K A C G hcert x0 c (c - 1 - e).toNat
      (by rwa [show c - 1 - ((c - 1 - e).toNat : ℤ) = e by omega])
      (by rw [show c - 1 - ((c - 1 - e).toNat : ℤ) = e by omega]; exact hl) a hr
  · set k : ℕ := (e - (c - 1)).toNat with hk
    have E := edge x0 e he hl k
    have hkc : e - (k : ℤ) = c - 1 := by rw [hk]; omega
    rw [hkc] at E
    apply core_lit q m K A C G hcert (ev x0 k) c 0 (by simpa using E.1) (by simpa using E.2) (a + k * (q + 1) - k)
    intro n i hi
    have : k ≤ k * (q + 1) := Nat.le_mul_of_pos_right k (by omega)
    rw [ev_add, show k + (a + k * (q + 1) - k + n * (q + 1) + i) = a + (n + k) * (q + 1) + i by
      rw [add_mul]; omega]
    exact hr (n + k) i hi
'''

FINAL = r'''
/-- Entry 38's remaining cases: no configuration with a leftmost black cell has a column reading 0 1^q
periodically, for q = 7 and q = 9 .. 13. -/
theorem black_end_two_sided (q : ℕ) (hq : q = 7 ∨ (9 ≤ q ∧ q ≤ 13)) (x0 : ℤ → Bool) (e : ℤ) (he : x0 e = true)
    (hl : ∀ j < e, x0 j = false) (c : ℤ) (a : ℕ) (hr : Reads0 x0 c q a) : False := by
  rcases hq with rfl | ⟨h1, h2⟩
  · exact no_black_word_lit 7 16 6 A7 C7 G7 cert7 x0 e he hl c a hr
  · interval_cases q
    · exact no_black_word_lit 9 10 6 A9 C9 G9 cert9 x0 e he hl c a hr
    · exact no_black_word_lit 10 11 6 A10 C10 G10 cert10 x0 e he hl c a hr
    · exact no_black_word_lit 11 12 6 A11 C11 G11 cert11 x0 e he hl c a hr
    · exact no_black_word_lit 12 13 6 A12 C12 G12 cert12 x0 e he hl c a hr
    · exact no_black_word_lit 13 14 6 A13 C13 G13 cert13 x0 e he hl c a hr

end BlackEnd38

#print axioms BlackEnd38.black_end_two_sided
'''

HEADER = '''import Mathlib

/-!
# Entry 38's remaining black-end cases by literal stages (Local, 2026-10-10; generated by gen_black_end38.py)

PROOFS.md entry 38 excludes the black end 0 1^q at q = 7 and every q >= 9; JenRoute.lean machine-checks q >= 14.
This file checks q = 7 and 9 .. 13 two-sidedly, by the strip of radius 6 of BlackEnd38.lean, with GC951's literal
stages: the chain from all centre-0 rows (A), the fixed point's phases (C) and six peel stages (G) are literals, and
each inclusion between consecutive stages is its own kernel check. The actual strip lies in every stage by induction;
on the last, cell c - 1 is constant at every phase, so Theorem A finishes it, as in BlackEnd38.lean.

How to check: generate with gen_black_end38.py, then `lake env lean`; the `#print axioms` line must list no `sorryAx`.
-/

-- Sequential elaboration: one kernel check at a time. The profiler reports any declaration over 10 s (BE-P3).
set_option Elab.async false
set_option profiler true
set_option profiler.threshold 10000

namespace BlackEnd38
'''


def main():
    # BlackEnd38base.lean holds the shared part (Rule 30, Theorem A, the strip definitions, the membership and window
    # lemmas, colConst_spec), taken from the parked BlackEnd38.lean without its one-shot checks
    base = open(sys.argv[1]).read()
    out_path = sys.argv[2]
    body = base[base.index('namespace BlackEnd38\n\n') + len('namespace BlackEnd38\n\n'):base.rindex('\nend BlackEnd38')]
    parts, report = [], []
    cases = [c for c in CASES if str(c[0]) in os.environ.get('BE_CASES', '7 9 10 11 12 13').split()]
    for q, n0 in cases:
        text, ok, fixed, total, m = per_q(q, n0)
        parts.append(text)
        report.append((q, n0, m, ok, fixed, total))
    final = FINAL if len(cases) == len(CASES) else '\nend BlackEnd38\n\n' + ''.join(
        '#print axioms BlackEnd38.cert%d\n' % q for q, _ in cases)          # a smoke test of a subset (BE_CASES)
    lean = HEADER + '\n' + body + PROOF + ''.join(parts) + final
    open(out_path, 'w').write(lean)
    for q, n0, m, ok, fixed, total in report:
        print('q=%2d n0=%d m=%2d  inclusions %s  fixed point %s  final peeled total %d (record: %d)' % (
            q, n0, m, 'HOLD' if ok else 'FAIL', 'exact' if fixed else 'NOT EXACT', total, 218 if q == 7 else 14 * q + 74))
    c1ok = all(r[3] for r in report) and all(r[5] == (218 if r[0] == 7 else 14 * r[0] + 74) for r in report)
    print('BE-C1', 'PASS' if c1ok else 'FAIL')
    print('wrote %s: %d bytes, sha256 %s' % (out_path, len(lean.encode()), hashlib.sha256(lean.encode()).hexdigest()[:16]))


if __name__ == '__main__':
    main()
