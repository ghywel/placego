#!/usr/bin/env python3
"""gen_trap_words.py (Local, 9 November 2026): writes the Lean module `Rule30GateTrapWords` (the gap words the kit's
gate trap forbids), in the kit's form and in the portal's form, from the kit's 829 trap codes.

Usage: python3 gen_trap_words.py KIT_DIR OUT_DIR
  writes OUT_DIR/Rule30GateTrapWords.lean (kit form) and OUT_DIR/Rule30Submission.lean (portal form)

Data: for each forbidden gap word, the path sets of the trap after each of its samples (as in local_trap_lemma.py);
for each of the six maximal proper factors 33, 335, 353, 533, 355, 553, one path of the trap graph that reads it
(a start window and the values of column 17), the minimality controls. Conventions are the kit's
`Rule30Certificates.GateTrap`: bit i of a code is column i + 1, the double step from an odd time has column 0 white
then black, and x1, x2 are the two values of column 17.
"""
import re
import sys
from pathlib import Path

KIT, OUT = Path(sys.argv[1]), Path(sys.argv[2])
src = (KIT / 'lean/Ruliology/CellularAutomata/Rule30Certificates/GateTrap.lean').read_text()
TRAP = [int(x) for x in re.search(r'def trapCodes : List Nat := \[(.*?)\]', src, re.S).group(1).replace('\n', ' ').split(',')]
assert len(TRAP) == 829
TS = set(TRAP)
M16 = (1 << 16) - 1


def step(s, c, x):
    e = s | (x << 16)
    return (((e << 1) | c) ^ (e | (e >> 1))) & M16


def step2(s, x1, x2):
    return step(step(s, 0, x1), 1, x2)


def bits(gaps):
    b = [1]
    for g in gaps:
        b += [0] * (g - 1) + [1]
    return b


def layers(word):
    S = {w for w in TRAP if (w & 1) == word[0]}
    out = [S]
    for y in word[1:]:
        S = {v for w in S for a in (0, 1) for b in (0, 1) for v in [step2(w, a, b)] if (v & 1) == y}
        out.append(S)
    return out


def path(word):
    """The least start window of the trap, and column-17 values, along which column 1 reads `word` (layered search
    with parent pointers; among the final windows the one reached first from the least start)."""
    parent = [{w: None for w in TRAP if (w & 1) == word[0]}]
    for y in word[1:]:
        nxt = {}
        for w in sorted(parent[-1]):
            for a in (0, 1):
                for b in (0, 1):
                    v = step2(w, a, b)
                    if (v & 1) == y and v not in nxt:
                        nxt[v] = (w, a, b)
        parent.append(nxt)
    if not parent[-1]:
        return None
    v = min(parent[-1])
    xs = []
    for k in range(len(word) - 1, 0, -1):
        w, a, b = parent[k][v]
        xs.append((a, b)); v = w
    return v, xs[::-1]


gl = lambda gw: '[' + ', '.join(map(str, gw)) + ']'
WORDS = [('333', [3, 3, 3]), ('3353', [3, 3, 5, 3]), ('3533', [3, 5, 3, 3]), ('3553', [3, 5, 5, 3]),
         ('5533', [5, 5, 3, 3])]
FACTORS = [('33', [3, 3]), ('335', [3, 3, 5]), ('353', [3, 5, 3]), ('533', [5, 3, 3]), ('355', [3, 5, 5]),
           ('553', [5, 5, 3])]

data = []
checks_l = []
lb = lambda b: 'true' if b else 'false'


def wrap(prefix, items, sep=', ', width=99, indent='    '):
    """Join items after prefix, wrapping lines at width."""
    lines, cur = [], prefix
    for i, it in enumerate(items):
        piece = it + (sep if i < len(items) - 1 else '')
        if len(cur) + len(piece.rstrip()) > width:
            lines.append(cur.rstrip()); cur = indent
        cur += piece
    lines.append(cur.rstrip())
    return '\n'.join(lines)


# the trie of the five words' sample prefixes: one layer per proper prefix, shared between words
trie = {}
for name, gw in WORDS:
    word = bits(gw)
    Ls = layers(word)
    assert not Ls[-1] and all(Ls[:-1])
    for k in range(len(word)):
        key = ''.join(map(str, word[:k + 1]))
        S = frozenset(Ls[k])
        assert trie.setdefault(key, S) == S
full = {''.join(map(str, bits(gw))) for _, gw in WORDS}
lay = lambda key: '[]' if key in full else 'lay' + key
for key in sorted(trie, key=lambda k: (len(k), k)):
    if key in full:
        continue
    c = sorted(trie[key])
    data.append(f'/-- The {len(c)} windows of the trap that can have read the samples `{key}`. -/\n'
                + wrap(f'def lay{key} : List Nat := [', [str(x) for x in c]) + ']')
lines = ['theorem start1 : startOK true lay1 = true := by decide +kernel']
for key in sorted(trie, key=lambda k: (len(k), k)):
    if len(key) >= 2:
        lines.append(f'theorem step{key} : stepOK {lay(key[:-1])} {lb(key[-1] == "1")} {lay(key)} = true := by\n'
                     '  decide +kernel')
checks_l.append('\n'.join(lines))
for name, gw in WORDS:
    word = bits(gw)
    keys = [''.join(map(str, word[:k + 1])) for k in range(len(word))]
    sizes = ', '.join(str(len(trie[k])) for k in keys)
    items = sizes.split(', ')
    items[-1] += '); the last is empty. -/'
    data.append(wrap(f'/-- The layers of the gap word `{name}`, one per sample (', items, indent='') + '\n'
                + wrap(f'def layers{name} : List (List Nat) := [', [lay(k) for k in keys]) + ']')
    lit = '[' + ', '.join(lb(b) for b in word) + ']'
    simps = [f'layers{name}', 'wordCheck', 'readCheck', 'start1'] + [f'step{k}' for k in keys[1:]] + \
        ['List.isEmpty_nil', 'Bool.and_self']
    checks_l.append(f'theorem check{name} : wordCheck (gapWord {gl(gw)}) layers{name} = true := by\n'
                    + wrap(f'  rw [show gapWord {gl(gw)} =\n    [', [lb(b) for b in word], indent='    ')
                    + '] from rfl]\n'
                    + wrap('  simp only [', simps) + ']')
print('trie layers', sum(1 for k in trie if k not in full), 'step lemmas', sum(1 for k in trie if len(k) >= 2))
ctrl = []
for name, gw in FACTORS:
    w0, xs = path(bits(gw))
    # replay the witness
    w = w0
    rd = [w & 1]
    for a, b in xs:
        w = step2(w, a, b); rd.append(w & 1)
        assert w in TS
    assert rd == bits(gw), name
    xl = ', '.join(f'({"true" if a else "false"}, {"true" if b else "false"})' for a, b in xs)
    ctrl.append((name, gw, w0, xl))

checks = '\n\n'.join(checks_l)
paths = '\n'.join(f'def path{n} : Nat × List (Bool × Bool) :=\n' + wrap(f'  ({w0}, [', xl.split(', (') if False else
                  [x if i == 0 else '(' + x for i, x in enumerate(xl.split(', ('))]) + '])' for n, g, w0, xl in ctrl)
minimal = ' ∧\n    '.join(f'trapPath path{n}.1 path{n}.2 (gapWord {gl(g)}) = true' for n, g, w0, xl in ctrl)

BODY = r'''
/-! ## Gap words -/

/-- The samples of a gap word: a black cell, then for each gap `g` the `g - 1` white cells and the
next black cell. So `gapWord [3, 5]` is `1, 0, 0, 1, 0, 0, 0, 0, 1`. -/
def gapWord : List Nat → List Bool
  | [] => [true]
  | g :: gs => true :: (List.replicate (g - 1) false ++ gapWord gs)

/-- `v` reads the word `w` from the step `s`. -/
def Reads (v : Nat → Bool) (s : Nat) (w : List Bool) : Prop :=
  ∀ i, i < w.length → v (s + i) = w.getD i false

theorem reads_take {v : Nat → Bool} {s : Nat} {w : List Bool} (h : Reads v s w) (n : Nat) :
    Reads v s (w.take n) := by
  intro i hi
  rw [List.length_take] at hi
  rw [h i (by omega), List.getD_eq_getElem?_getD, List.getD_eq_getElem?_getD,
    List.getElem?_take_of_lt (by omega)]

theorem reads_drop {v : Nat → Bool} {s : Nat} {w : List Bool} (h : Reads v s w) (k : Nat) :
    Reads v (s + k) (w.drop k) := by
  intro i hi
  rw [List.length_drop] at hi
  rw [Nat.add_assoc, h (k + i) (by omega), List.getD_eq_getElem?_getD, List.getD_eq_getElem?_getD,
    List.getElem?_drop]

/-! ## Windows by their codes -/

theorem seg_testBit_encList : ∀ (w : List Bool), seg (fun i => (encList w).testBit i) w.length = w
  | [] => rfl
  | x :: l => by
    have h0 : (encList (x :: l)).testBit 0 = x := by
      cases x <;> simp [encList] <;> omega
    have h1 : (fun i => (encList (x :: l)).testBit (i + 1)) = (fun i => (encList l).testBit i) := by
      funext i
      rw [Nat.testBit_succ]
      congr 1
      cases x <;> simp [encList] <;> omega
    show (encList (x :: l)).testBit 0 ::
      seg (fun i => (encList (x :: l)).testBit (i + 1)) l.length = x :: l
    rw [h0, h1, seg_testBit_encList l]

theorem decode_encList {w : List Bool} (hw : w.length = 16) : decode (encList w) = w := by
  have := seg_testBit_encList w
  rw [hw] at this
  exact this

/-- A list of codes as a bitmap: bit `n` is set for each code `n` of the list. -/
def maskN : List Nat → Nat
  | [] => 0
  | n :: rest => 2 ^ n ||| maskN rest

theorem maskN_spec : ∀ (L : List Nat) (n : Nat), (maskN L).testBit n = true → n ∈ L
  | [], n, h => by simp [maskN] at h
  | m :: rest, n, h => by
    simp only [maskN, Nat.testBit_or, Bool.or_eq_true] at h
    rcases h with h | h
    · rw [Nat.testBit_two_pow] at h
      have e : m = n := by simpa using h
      subst e
      exact List.mem_cons_self
    · exact List.mem_cons_of_mem _ (maskN_spec rest n h)

/-- A window whose code is set in the bitmap of a list of codes is in the decoded list. -/
theorem mem_of_maskN {LN : List Nat} {w : List Bool} (hw : w.length = 16)
    (h : inM (maskN LN) w = true) : w ∈ LN.map decode :=
  List.mem_map.2 ⟨encList w, maskN_spec LN _ h, decode_encList hw⟩

/-! ## The word check -/

/-- The windows of `trap` that read `b` in column `1` are in the layer `L`. -/
def startOK (b : Bool) (L : List Nat) : Bool :=
  trap.all (fun w => w.headD false != b || inM (maskN L) w)

/-- One layer: every double step from a window of the layer `S`, for all four values of column `17`,
either does not read `b` in column `1` or lands in the layer `L`. -/
def stepOK (S : List Nat) (b : Bool) (L : List Nat) : Bool :=
  (S.map decode).all (allSucc (fun w => w.headD false != b || inM (maskN L) w))

/-- Reading the letters `word` from the windows `S`. For each letter, every double step from a
window of `S`, for all four values of column `17`, either does not read the letter in column `1` or
lands in the next layer; after the last letter the layer is empty. -/
def readCheck : List Nat → List Bool → List (List Nat) → Bool
  | S, [], _ => S.isEmpty
  | S, b :: rest, L :: Ls => stepOK S b L && readCheck L rest Ls
  | _, _ :: _, [] => false

/-- **The word check.** The windows of `trap` that read the first letter of `word` in column `1`
are in the first layer, and `readCheck` holds from there for the other letters and layers. -/
def wordCheck : List Bool → List (List Nat) → Bool
  | b :: rest, L :: Ls => startOK b L && readCheck L rest Ls
  | _, _ => false

section Driven
variable (R : Nat → Bool)

theorem readCheck_spec : ∀ (word : List Bool) (S : List Nat) (Ls : List (List Nat)),
    readCheck S word Ls = true → ∀ t, t % 2 = 1 → win R t ∈ S.map decode →
      ¬ ∀ i, i < word.length → (win R (t + 2 * (i + 1))).headD false = word.getD i false
  | [], S, Ls, h, t, _, hw, _ => by
    simp only [readCheck, List.isEmpty_iff] at h
    subst h
    simp at hw
  | b :: rest, S, L :: Ls, h, t, ht, hw, hr => by
    simp only [readCheck, stepOK, Bool.and_eq_true] at h
    have hP := win_next R h.1 ht hw
    have hb : (win R (t + 2)).headD false = b := by simpa using hr 0 (by simp)
    rw [hb] at hP
    simp only [bne_self_eq_false, Bool.false_or] at hP
    refine readCheck_spec rest _ Ls h.2 (t + 2) (by omega) (mem_of_maskN (win_length R _) hP) ?_
    intro i hi
    have := hr (i + 1) (by simp; omega)
    rw [show t + 2 + 2 * (i + 1) = t + 2 * (i + 1 + 1) by omega]
    simpa using this
  | _ :: _, _, [], h, _, _, _, _ => by simp [readCheck] at h

/-- **A word check excludes its word after entry.** If `wordCheck word layers` holds and the window
of `R` is in `trap` at an odd time `t0`, then `u R` does not read `word` from any step `s` with
`t0 ≤ 2 s + 1`. -/
theorem not_reads_of_check {word : List Bool} {layers : List (List Nat)}
    (hc : wordCheck word layers = true) {t0 : Nat} (h0 : t0 % 2 = 1) (hw : win R t0 ∈ trap)
    (s : Nat) (hs : t0 ≤ 2 * s + 1) : ¬ Reads (Rule30PeriodTwoSideways.u R) s word := by
  intro hr
  have hw0 : win R (2 * s + 1) ∈ trap := by
    have := win_mem_trap R h0 hw ((2 * s + 1 - t0) / 2)
    rwa [show t0 + 2 * ((2 * s + 1 - t0) / 2) = 2 * s + 1 by omega] at this
  cases word with
  | nil => simp [wordCheck] at hc
  | cons b rest =>
    cases layers with
    | nil => simp [wordCheck] at hc
    | cons L Ls =>
      simp only [wordCheck, startOK, Bool.and_eq_true] at hc
      have hb : (win R (2 * s + 1)).headD false = b := by
        have := hr 0 (by simp)
        rw [u_eq_head] at this
        simpa using this
      have hP := List.all_eq_true.1 hc.1 _ hw0
      rw [hb] at hP
      simp only [bne_self_eq_false, Bool.false_or] at hP
      refine readCheck_spec R rest _ Ls hc.2 (2 * s + 1) (by omega)
        (mem_of_maskN (win_length R _) hP) ?_
      intro i hi
      have := hr (i + 1) (by simp; omega)
      rw [u_eq_head] at this
      rw [show 2 * s + 1 + 2 * (i + 1) = 2 * (s + (i + 1)) + 1 by omega]
      simpa using this

end Driven

/-! ## The layers of the five words -/

@DATA@

@CHECKS@

/-! ## The gap words after entry -/

section Words
variable (R : Nat → Bool)

/-- **The trap never shows `3353`.** If the window of `R` is in `trap` at an odd time `t0`, then
`u R` never reads the gap word `3, 3, 5, 3` from a step `s` with `t0 ≤ 2 s + 1`. -/
theorem no_3353_of_entry {t0 : Nat} (h0 : t0 % 2 = 1) (hw : win R t0 ∈ trap) (s : Nat)
    (hs : t0 ≤ 2 * s + 1) : ¬ Reads (Rule30PeriodTwoSideways.u R) s (gapWord [3, 3, 5, 3]) :=
  not_reads_of_check R check3353 h0 hw s hs

/-- **The five gap words.** If the window of `R` is in `trap` at an odd time `t0`, then from every
step `s` with `t0 ≤ 2 s + 1`, `u R` reads none of the gap words `333`, `3353`, `3533`, `3553` and
`5533`. -/
theorem gap_words_of_entry {t0 : Nat} (h0 : t0 % 2 = 1) (hw : win R t0 ∈ trap) (s : Nat)
    (hs : t0 ≤ 2 * s + 1) :
    ¬ Reads (Rule30PeriodTwoSideways.u R) s (gapWord [3, 3, 3]) ∧
      ¬ Reads (Rule30PeriodTwoSideways.u R) s (gapWord [3, 3, 5, 3]) ∧
      ¬ Reads (Rule30PeriodTwoSideways.u R) s (gapWord [3, 5, 3, 3]) ∧
      ¬ Reads (Rule30PeriodTwoSideways.u R) s (gapWord [3, 5, 5, 3]) ∧
      ¬ Reads (Rule30PeriodTwoSideways.u R) s (gapWord [5, 5, 3, 3]) :=
  ⟨not_reads_of_check R check333 h0 hw s hs, not_reads_of_check R check3353 h0 hw s hs,
    not_reads_of_check R check3533 h0 hw s hs, not_reads_of_check R check3553 h0 hw s hs,
    not_reads_of_check R check5533 h0 hw s hs⟩

/-- **No `33535555` after entry**: it begins with `3353`. -/
theorem no_33535555_of_entry {t0 : Nat} (h0 : t0 % 2 = 1) (hw : win R t0 ∈ trap) (s : Nat)
    (hs : t0 ≤ 2 * s + 1) :
    ¬ Reads (Rule30PeriodTwoSideways.u R) s (gapWord [3, 3, 5, 3, 5, 5, 5, 5]) := by
  intro h
  have h' := reads_take h 15
  rw [show (gapWord [3, 3, 5, 3, 5, 5, 5, 5]).take 15 = gapWord [3, 3, 5, 3] by decide] at h'
  exact no_3353_of_entry R h0 hw s hs h'

/-- **Two gaps of `3` in a row only at the start.** If the window of `R` is in `trap` at an odd time
`t0`, then from a step `s` with `t0 ≤ 2 s + 1`, after any two gaps `x` and `y` (each `3` or `5`,
the only gaps of `gaps_of_entry`) the next two gaps are not both `3`. So from the third black cell
after entry on, no two consecutive gaps are both `3`. -/
theorem no_late_33 {t0 : Nat} (h0 : t0 % 2 = 1) (hw : win R t0 ∈ trap) (s : Nat)
    (hs : t0 ≤ 2 * s + 1) (x y : Nat) (hx : x = 3 ∨ x = 5) (hy : y = 3 ∨ y = 5) :
    ¬ Reads (Rule30PeriodTwoSideways.u R) s (gapWord [x, y, 3, 3]) := by
  intro h
  rcases hy with rfl | rfl
  · rcases hx with rfl | rfl
    · have h' := reads_drop h 3
      rw [show (gapWord [3, 3, 3, 3]).drop 3 = gapWord [3, 3, 3] by decide] at h'
      exact not_reads_of_check R check333 h0 hw (s + 3) (by omega) h'
    · have h' := reads_drop h 5
      rw [show (gapWord [5, 3, 3, 3]).drop 5 = gapWord [3, 3, 3] by decide] at h'
      exact not_reads_of_check R check333 h0 hw (s + 5) (by omega) h'
  · rcases hx with rfl | rfl
    · exact not_reads_of_check R check3533 h0 hw s hs h
    · exact not_reads_of_check R check5533 h0 hw s hs h

end Words

/-! ## A weaker form of `Q01Gap` -/

/-- At `s`, the bit sequence `g` is white, or black with the next black cell at distance `3` or
`5` (`GapOK`), and `g` reads none of the five gap words from `s`. -/
def WordsOK (g : Nat → Bool) (s : Nat) : Prop :=
  GapOK g s ∧ ¬ Reads g s (gapWord [3, 3, 3]) ∧ ¬ Reads g s (gapWord [3, 3, 5, 3]) ∧
    ¬ Reads g s (gapWord [3, 5, 3, 3]) ∧ ¬ Reads g s (gapWord [3, 5, 5, 3]) ∧
    ¬ Reads g s (gapWord [5, 5, 3, 3])

/-- **`Q01GapWords`** (**open**): no finitely supported constrained start of the zero-boundary left
half has free bits whose complement, from some step on, has each black cell followed by the next
one at distance `3` or `5` and reads none of the gap words `333`, `3353`, `3533`, `3553`, `5533`. -/
def Q01GapWords : Prop := ∀ L : Nat → Bool, FinSupp L → InX L →
  ¬ ∃ s0, ∀ s, s0 ≤ s → WordsOK (fun s => !zrow L (2 * s + 1) 1) s

/-- **`Q01Gap` implies `Q01GapWords`**: it excludes more free bits. -/
theorem Q01GapWords_of_Q01Gap (h : Q01Gap) : Q01GapWords := fun L hf hX ⟨s0, hs⟩ =>
  h L hf hX ⟨s0, fun s hs' => (hs s hs').1⟩

/-- **`Q01GapWords` gives `CQ01` for every right half whose window enters the trap**, as `Q01Gap`
does in `not_finSupp_Psi_of_Q01Gap`: the candidate left row `Psi R` has infinitely many black
cells. -/
theorem not_finSupp_Psi_of_Q01GapWords (hQ : Q01GapWords) (R : Nat → Bool) {t0 : Nat}
    (h0 : t0 % 2 = 1) (hw : win R t0 ∈ trap) :
    ¬ FinSupp (Rule30PeriodTwoSideways.Psi R) := by
  intro hfin
  refine hQ _ hfin (Rule30PeriodTwoSideways.Psi_inX R) ⟨t0, fun s hs => ?_⟩
  have e : (fun s => !zrow (Rule30PeriodTwoSideways.Psi R) (2 * s + 1) 1) =
      Rule30PeriodTwoSideways.u R := by
    funext s; rw [Rule30PeriodTwoSideways.Psi_free]; simp; rfl
  rw [e]
  exact ⟨gaps_of_entry R h0 hw s (by omega), gap_words_of_entry R h0 hw s (by omega)⟩

/-- **`CQ01Empty` follows from `Q01GapWords`.** -/
theorem CQ01Empty_of_Q01GapWords (hQ : Q01GapWords) : Rule30PeriodTwoSideways.CQ01Empty :=
  not_finSupp_Psi_of_Q01GapWords hQ _ (t0 := 293) (by decide) entry_empty

/-! ## The five words are minimal -/

/-- Along the double steps with the listed values of column `17`, the window `w` reads `word` in
column `1`, starting with its own. -/
def pathReads : List Bool → List (Bool × Bool) → List Bool → Bool
  | w, [], [b] => w.headD false == b
  | w, (x1, x2) :: xs, b :: rest => (w.headD false == b) && pathReads (step2 w x1 x2) xs rest
  | _, _, _ => false

/-- A path of the trap graph that reads `word`: a window of `trap`, coded by `c`, and values of
column `17`. By `trapClosed_ok` every window of the path is in `trap`. -/
def trapPath (c : Nat) (xs : List (Bool × Bool)) (word : List Bool) : Bool :=
  trapCodes.contains c && pathReads (decode c) xs word

@PATHS@

/-- **The five words are minimal for the trap.** Removing the first or the last gap of any of them
gives one of `33`, `335`, `353`, `533`, `355`, `553`, and each of these is read along a path of
the trap graph. So no shorter word explains any of the five, as far as the trap alone can see. -/
theorem minimal_paths :
    @MINIMAL@ := by
  decide +kernel
'''

HEAD_DOC = r'''/-!
# The gap words of the gate trap

`Rule30GateTrap` gives a set `trap` of `829` windows of the columns `1..16` of the right half
driven by the alternating column, read at the odd times and closed under the double step whatever
column `17` does. After the window of a right half `R` enters it, every black cell of `u R` (column
`1` at the time `2 s + 1`) is followed by the next one at distance `3` or `5` (`gaps_of_entry`).
This module shows that the trap forbids more: five gap words never occur after entry.

A gap word `g₁ g₂ … gₖ` is read from a black cell at the step `s` when the next black cells are
at `s + g₁`, `s + g₁ + g₂`, … and the cells between them are white (`gapWord`, `Reads`).

* `gap_words_of_entry`: if the window of `R` is in `trap` at an odd time `t0`, then from every step
  `s` with `t0 ≤ 2 s + 1`, `u R` reads none of the gap words `333`, `3353`, `3533`, `3553` and
  `5533`. `no_3353_of_entry` is the second alone.
* `no_33535555_of_entry`: nor `33535555`, which begins with `3353`.
* `no_late_33`: after any two gaps, the next two gaps are not both `3`. With `gaps_of_entry`, from
  the third black cell after entry on, `u R` is a concatenation of the blocks `001` and `00001` in
  which no two blocks `001` are adjacent and no two are separated by exactly two blocks `00001`.
* `Q01GapWords` (**open**) is the kit's `Q01Gap` with the five words excluded as well: it follows
  from `Q01Gap` (`Q01GapWords_of_Q01Gap`), and it still gives `¬ FinSupp (Psi R)` for every right
  half whose window enters the trap (`not_finSupp_Psi_of_Q01GapWords`), hence `CQ01Empty`
  (`CQ01Empty_of_Q01GapWords`).
* `minimal_paths`: each of the five words is minimal for the trap: removing its first or last gap
  gives a word that a path of the trap graph reads (`33`, `335`, `353`, `533`, `355`, `553`).

The method is the kit's: for each word the windows of the trap that can have read its first `k`
samples are given as data (`layers333`, …), and the kernel checks that the double step, for every
value of column `17`, takes each layer into the next and that the last layer is empty (`wordCheck`,
`not_reads_of_check`). By computation, not in Lean, the five words are all the trap forbids: a word
over the gaps `3` and `5` is read along some path of the trap graph exactly when it contains none of
them. Nothing here decides `CQ01`, `Q01Gap`, `Q01GapWords` or Problem 1.
-/'''

body = BODY.replace('@DATA@', '\n\n'.join(data)).replace('@CHECKS@', checks).replace('@PATHS@', paths) \
    .replace('@MINIMAL@', minimal)

kit = ('module\n\npublic import Ruliology.CellularAutomata.Rule30GateTrap\n\n' + HEAD_DOC + '\n\n@[expose] public section\n\n'
       '-- Sequential elaboration: the kernel checks would otherwise run in parallel and stack their memory.\n'
       'set_option Elab.async false\n\n'
       'namespace Ruliology.CellularAutomata.Rule30GateTrapWords\n\n'
       'open Rule30StripCertificates Rule30GateTrap Rule30ZeroBoundary\n' + body + '\nend Ruliology.CellularAutomata.Rule30GateTrapWords\n')
portal = ('import Ruliology.CellularAutomata.Rule30Prize\nimport Ruliology.CellularAutomata.Rule30GateTrap\n\n' + HEAD_DOC +
          '\n\n-- Sequential elaboration: the kernel checks would otherwise run in parallel and stack their memory.\n'
          'set_option Elab.async false\n\n'
          'namespace Rule30Submission\n\n'
          'open Ruliology.CellularAutomata Rule30StripCertificates Rule30GateTrap Rule30ZeroBoundary\n' + body + '\nend Rule30Submission\n')
for text in (kit, portal):
    assert '"' not in text and '\\' not in text
OUT.mkdir(parents=True, exist_ok=True)
(OUT / 'Rule30GateTrapWords.lean').write_text(kit)
(OUT / 'Rule30Submission.lean').write_text(portal)
print('kit form', len(kit), 'chars; portal form', len(portal), 'chars;', sum(len(layers(bits(g))) - 1 for _, g in WORDS) + 5,
      'layers;', 'paths', [(n, w0, len(xl.split('),'))) for n, g, w0, xl in ctrl])
