"""tree_gen.py: the kit-form modules for a tree of strips with the time carried (CL738, stage 2), from the state of
tree16_data.py: one module per strip (its row, its returns, its events above its creation with their kernel facts, the black
windows, the walk's segments in blocks chained by w32_chain, the states at its white wheels for its children) and a final
module (the sixteen-way alignment OnTree, one lemma per strip in post-order carrying the time through its events, the
headlines, distinctness of every pair at the lowest fork where their lineages part, realization, the arithmetic form).
Every number in a kernel fact comes from this Python; the kernel confirms or refutes it.
Usage: python3 tree_gen.py STATEDIR K PREFIX OUTDIR [BLOCK]"""
import sys, os, json, time
import numpy as np
STATE, K, PREFIX, OUT = sys.argv[1], int(sys.argv[2]), sys.argv[3], sys.argv[4]
BLK = int(sys.argv[5]) if len(sys.argv) > 5 else 128
P = 32; MASK = (1 << K) - 1; J = K - 1
st = json.load(open(f"{STATE}/state.json"))
order = st['order']; S = st['strips']
idx = {name: i for i, name in enumerate(order)}
def step(v): return ((v << 2) ^ ((v << 1) | v)) & MASK
def load_row(name): return int.from_bytes(open(f"{STATE}/rows/{name}.bin", 'rb').read(), 'little')
t0 = time.time()
rows = {n: load_row(n) for n in order}
cyc = {}
for n in order:
    c = [rows[n]]
    for _ in range(P): c.append(step(c[-1]))
    assert c[P] == rows[n]; cyc[n] = c[:P]
def words_of(c):
    w = np.zeros(K, dtype=np.int64)
    for r in range(P):
        bits = np.unpackbits(np.frombuffer(c[r].to_bytes((K + 7) // 8, 'little'), dtype=np.uint8), bitorder='little')[:K]
        w += bits.astype(np.int64) << r
    return [int(x) for x in w]
W = {n: words_of(cyc[n]) for n in order}
print(f"rows and words: {time.time()-t0:.0f} s")
def srch(w, m):
    for r in range(P):
        if (w >> ((m + r) % P)) & 1: return r
    return P
def fstep(w, j, s):
    a, b = s; m = max(a, b)
    return (b, m) if w[j + 1] == 0 else (b, m + srch(w[j + 1], m) + 1)
STATES = {}
for n in order:
    s = (0, 1); L = [s]
    for j in range(J - 1): s = fstep(W[n], j, s); L.append(s)    # L[j] = state after reading wheels 1..j, j <= J-1
    STATES[n] = L
F = {n: [s[0] for s in STATES[n]] + [STATES[n][-1][1]] for n in order}
for n in order: assert F[n][J] == S[n]['front'], (n, F[n][J], S[n]['front'])
print("fronts agree with the probe:", {n: F[n][J] for n in order})
# events per strip: whites above the creation wheel (root: above 400), sorted; exactly one doubling expected
def creation(n): return S[n]['fork'] if S[n]['parent'] else 400
EV = {}
for n in order:
    c = creation(n)
    ev = [(e[0], e[2]) for e in S[n]['whites'] if e[0] > c]
    nd = sum(1 for e in ev if e[1] == 'doubling')
    assert nd <= 1 and (nd == 0 or ev[-1][1] == 'doubling'), (n, ev)   # no fork after the doubling (Prop. 9)
    EV[n] = ev
children = {n: [m for m in order if S[m]['parent'] == n] for n in order}
def mod(i): return f"{PREFIX}Strip{i}"
def ns(i): return f"Ruliology.CellularAutomata.{mod(i)}"
def walk_sim(n, ticks, t, j):
    c = cyc[n]
    for _ in range(ticks):
        j += (c[t % P] >> j) & 1; t += 1
    return j
# ---------------- strip modules ----------------
def seg_text(n, lab, j0, cnt):
    a, b = STATES[n][j0]; A, B = STATES[n][j0 + cnt]
    h = (P - b % P) % P; rest = A - 1 - b - h
    assert rest >= 0 and a <= b and b < A and A < B and cnt >= 2, (n, lab, j0, cnt, a, b, A, B)
    g, d = divmod(rest, P)
    R = "(rowAt K V)"; out = []
    j = j0 + 1; t = b
    j1 = walk_sim(n, h, t, j); t += h
    out.append(f"theorem {lab}_h : walk {R} {h} {b} {j0 + 1} = {j1} := by decide +kernel\n")
    blocks = [BLK] * (g // BLK) + ([g % BLK] if g % BLK else [])
    jj = j1; cum = 0
    for i, rounds in enumerate(blocks):
        jn = walk_sim(n, P * rounds, t, jj); t += P * rounds
        out.append(f"theorem {lab}_b{i} : w32 {R} {rounds} {jj} = {jn} := by decide +kernel\n")
        if i == 0: out.append(f"theorem {lab}_c0 : w32 {R} {rounds} {j1} = {jn} := {lab}_b0\n")
        else: out.append(f"theorem {lab}_c{i} : w32 {R} {cum + rounds} {j1} = {jn} :=\n  w32_chain _ (g1 := {cum}) (g2 := {rounds}) (by decide) {lab}_c{i - 1} {lab}_b{i}\n")
        cum += rounds; jj = jn
    j2 = jj; assert cum == g
    out.append(f"theorem {lab}_g : w32 {R} {g} {j1} = {j2} := {lab}_c{len(blocks) - 1}\n")
    Jend = walk_sim(n, d, t, j2); assert Jend == j0 + cnt - 1 and t == b + h + P * g
    out.append(f"theorem {lab}_d : walk {R} {d} ({b} + {h} + 32 * {g}) {j2} = {j0 + cnt - 1} := by decide +kernel\n")
    out.append(f"set_option exponentiation.threshold {K + 10} in\n"
               f"theorem {lab} : frun w {j0} {cnt} ({a}, {b}) = ({A}, {B}) :=\n"
               f"  seg_black (K := K) (v := V) (h := {h}) (g := {g}) (d := {d}) (by decide) (by decide) (by decide) (by decide) (by decide) (by decide)\n"
               f"    (fastWalk_of _ {lab}_h {lab}_g {lab}_d) (by decide +kernel) (by decide +kernel) (by decide +kernel)\n")
    return "".join(out), (A, B)
def white_text(n, lab, j0, e):
    a, b = STATES[n][j0]
    return f"theorem {lab} : frun w {j0} 1 ({a}, {b}) = ({b}, {b}) := frun_white (by decide) w_{e}\n"
def chain(start_lab, start_j, segs, end_j):
    """segs: list of (lab, j0, cnt); returns the term for frun w 0 end_j (0,1) by nested frun_chain from start_lab (frun w 0 start_j (0,1))."""
    items = [(start_lab, 0, start_j)] + segs
    tot = sum(c[2] for c in items); assert tot == end_j, (tot, end_j)
    def nest(i):
        l, j0, cnt = items[i]
        if i == len(items) - 1: return l
        rest = sum(c[2] for c in items[i + 1:])
        return f"(frun_chain _ {j0} {cnt} {rest} _ _ _ {l}\n    {nest(i + 1)})"
    return nest(0)
os.makedirs(OUT, exist_ok=True)
TH = f"set_option exponentiation.threshold {K + 10} in\n"
for n in order:
    i = idx[n]; par = S[n]['parent']; c = creation(n); ev = EV[n]; D = ev[-1][0] if (ev and ev[-1][1] == 'doubling') else None
    L = ["module\n\n"]
    L.append(f"public import Ruliology.CellularAutomata.{mod(idx[par]) if par else 'Rule30FiveFrontsBase'}\n\n")
    hdr1 = f"/-!\n# Strip {i} of the tree through wheel {J}" + (f": the child at the fork {c} of strip {idx[par]}, with wheel {c + 1} complemented" if par else ": the single black cell's") + "\n\n"
    hdr2 = (f"Its row `V` on {K} wheels, at phase 0; its period is 32 from wheel {D + 1} (the doubling at {D}); its events above its creation,\n" if D is not None
            else f"Its row `V` on {K} wheels, at phase 0, of period 16 throughout; its events above its creation,\n")
    hdr3 = (f"with their kernel facts; the walk's segments in blocks of {BLK} rounds; the states at its white wheels, for its children.\n-/\n\n"
            "@[expose] public section\n\n"
            f"namespace {ns(i)}\n\nopen Rule30FiveFrontsBase\nopen Rule30UniversalLeftSide (rowAt)\n" + (f"open {mod(0)} (K)\n" if par else "") +
            "\nset_option autoImplicit false\n\n")
    L.append(hdr1 + hdr2 + hdr3)
    if not par: L.append(f"/-- The register: wheels `0, …, {J}`. -/\nabbrev K : Nat := {K}\n\n")
    L.append(f"def V : Nat := 0x{rows[n]:x}\n\n")
    L.append(f"theorem V_return : rowAt K V 32 = V := by decide +kernel\n")
    L.append(TH + f"theorem V_finite : V < 2 ^ K ∧ V.testBit 0 = true := by decide +kernel\n")
    if D is not None: L.append(f"theorem least_period : ∀ d, d < 32 → d ≠ 0 → rowAt K V d ≠ V := by decide +kernel\n")
    else: L.append(f"theorem V_return16 : rowAt K V 16 = V := by decide +kernel\ntheorem least_period : ∀ d, d < 16 → d ≠ 0 → rowAt K V d ≠ V := by decide +kernel\n")
    L.append(f"abbrev w : Nat → Nat := wd K V\ntheorem words : Words K V w := Rule30FiveFrontsBase.words K V\n")
    L.append(f"theorem prim : ∀ d, d < 16 → d ≠ 0 → ∃ q, q < 16 ∧ Sp K V 400 (q + d) ≠ Sp K V 400 q := by decide +kernel\n\n")
    if not par:
        L.append("/-! ### Below the first fork -/\n\n"
                 "theorem V_zero_phase : ∀ r, r < 32 → Sp K V 0 r = true := by decide +kernel\n"
                 "theorem V_one_phase : ∀ r, r < 32 → Sp K V 1 r = true := by decide +kernel\n"
                 "theorem V_zero (t : Nat) : Sp K V 0 t = true := black_of_phase V_return V_zero_phase t\n"
                 "theorem V_one (t : Nat) : Sp K V 1 t = true := black_of_phase V_return V_one_phase t\n"
                 + TH + "theorem black_mask : (orRows K V 32 ||| whiteMask) % 2 ^ 53207 = 2 ^ 53207 - 1 := by decide +kernel\n")
        for (m, Lsh) in [(2, 1), (7, 2), (28, 4), (399, 8)]:
            L.append((TH if m == 399 else "") + f"theorem per{m} : ∀ r, r < 32 → rowAt K V (r + {Lsh}) % 2 ^ ({m} + 1) = rowAt K V r % 2 ^ ({m} + 1) := by decide +kernel\n"
                     f"theorem anti{m} : ∀ r, r < 32 → Sp K V ({m} + 1) (r + {Lsh}) = !Sp K V ({m} + 1) r := by decide +kernel\n")
        L.append(TH + "theorem hbw : ∀ m, m < 53207 → w m ≠ 0 ∨ m = 2 ∨ m = 7 ∨ m = 28 ∨ m = 399 := fun m hm => by\n"
                 "  rcases black_or_white black_mask hm with ⟨r, hr, hb⟩ | h\n  · exact Or.inl (word_ne_of_black words hr hb)\n  · exact Or.inr h\n\n")
        L.append("theorem a_low : frun w 0 400 (0, 1) = (783, 784) := by decide +kernel\n\n")
    else:
        pm = mod(idx[par])
        L.append(f"/-! ### Below the creation: the parent's strip -/\n\n")
        L.append(TH + f"theorem low_V : ∀ r, r < 32 → rowAt K V r % 2 ^ {c + 1} = rowAt K {pm}.V r % 2 ^ {c + 1} := by decide +kernel\n")
        L.append(f"theorem top_V : ∀ r, r < 32 → Sp K V {c + 1} r = !Sp K {pm}.V {c + 1} r := by decide +kernel\n")
        L.append(f"theorem low_V' (j t : Nat) (hj : j < {c + 1}) : Sp K V j t = Sp K {pm}.V j t := low_of_phase {pm}.V_return V_return low_V j t hj\n")
        L.append(f"theorem comp_V : ∀ t, Sp K V {c + 1} t = !Sp K {pm}.V {c + 1} t := comp_of_phase {pm}.V_return V_return top_V\n")
        L.append(f"theorem w_eq : ∀ i, i + 2 ≤ {c + 1} → {pm}.w (i + 1) = w (i + 1) := fun i hi =>\n"
                 f"  (word_eq_of_low {pm}.words words (fun r _ => low_V' (i + 1) r (by omega))).symm\n")
        a, b = STATES[n][c]
        L.append(f"theorem s_{c} : frun w 0 {c} (0, 1) = ({a}, {b}) :=\n  (low_congr (fun i hi => (w_eq i (by omega)).symm)).trans {pm}.s_{c}\n\n")
    L.append("/-! ### The events above the creation -/\n\n")
    for (e, kind) in ev:
        L.append(f"theorem white_{e} : ∀ r, r < 32 → Sp K V {e} r = false := by decide +kernel\n"
                 f"theorem w_{e} : w {e} = 0 := word_zero_of_white words white_{e}\n")
    if D is not None:
        L.append(TH + f"theorem per_{D} : ∀ r, r < 32 → rowAt K V (r + 16) % 2 ^ ({D} + 1) = rowAt K V r % 2 ^ ({D} + 1) := by decide +kernel\n"
                 f"theorem anti_{D} : ∀ r, r < 32 → Sp K V ({D} + 1) (r + 16) = !Sp K V ({D} + 1) r := by decide +kernel\n"
                 f"/-- Below wheel {D + 1} the strip keeps period 16. -/\n"
                 f"theorem per16 : ∀ j, j ≤ {D} → ∀ t, Sp K V j (t + 16) = Sp K V j t := (strip_shift V_return per_{D} anti_{D}).1\n\n")
    else:
        L.append(f"theorem per16 : ∀ j, j ≤ {J} → ∀ t, Sp K V j (t + 16) = Sp K V j t := fun j _ t => by\n  have h := Sp_add_mul' V_return16 j t 1\n  rwa [Nat.one_mul] at h\n\n")
    # black windows: between consecutive events, and after the doubling to J
    j = (400 if not par else c); wins = []
    pts = [e for e, _ in ev]
    for e in pts:
        lo, hi = j + 1, e
        if lo < hi: wins.append((lo, hi))
        j = e
    wins.append((j + 1, J))
    for (lo, hi) in wins:
        L.append(TH + f"theorem win_{lo}_{hi} : (orRows K V 32 >>> {lo}) % 2 ^ ({hi} - {lo}) = 2 ^ ({hi} - {lo}) - 1 := by decide +kernel\n"
                 + TH + f"theorem b_{lo}_{hi} : ∀ m, {lo} ≤ m → m < {hi} → w m ≠ 0 := fun m h1 h2 => by\n"
                 f"  obtain ⟨r, hr, hb⟩ := black_window_phase win_{lo}_{hi} h1 (by omega)\n  exact word_ne_of_black words hr hb\n")
    L.append("\n/-! ### The walk -/\n\n")
    # segments from j0 = start to J-1 (reads through wheel J-1 = K-2), with states at each white wheel exposed
    start_lab = 'a_low' if not par else f"s_{c}"; start_j = 400 if not par else c
    segs = []; j = start_j; k = 0
    for (e, kind) in ev:
        if e - 1 > j:
            k += 1; lab = f"r{k}"; txt, _ = seg_text(n, lab, j, e - 1 - j); L.append(txt); segs.append((lab, j, e - 1 - j)); j = e - 1
        k += 1; lab = f"r{k}"; L.append(white_text(n, lab, j, e)); segs.append((lab, j, 1)); j = e
        a, b = STATES[n][e]
        L.append(f"theorem s_{e} : frun w 0 {e} (0, 1) = ({a}, {b}) :=\n  {chain(start_lab, start_j, segs, e)}\n")
    a, b = STATES[n][J - 1]
    if J - 1 > j:
        k += 1; lab = f"r{k}"; txt, _ = seg_text(n, lab, j, J - 1 - j); L.append(txt); segs.append((lab, j, J - 1 - j)); j = J - 1
        L.append(f"theorem s_end : frun w 0 {J - 1} (0, 1) = ({a}, {b}) :=\n  {chain(start_lab, start_j, segs, J - 1)}\n")
    else:
        L.append(f"theorem s_end : frun w 0 {J - 1} (0, 1) = ({a}, {b}) := {start_lab if not segs else 's_' + str(j)}\n")
    L.append(f"theorem front : F w {J} = {F[n][J]} := by rw [← S_snd]; exact congrArg Prod.snd s_end\n")
    L.append(f"theorem front_le : ∀ j, j ≤ {J} → F w j ≤ {F[n][J]} := fun j hj => Nat.le_trans (F_mono w hj) (by rw [front]; exact Nat.le_refl _)\n")
    L.append(f"\nend {ns(i)}\n")
    open(f"{OUT}/{mod(i)}.lean", 'w').write("".join(L))
    print(f"{mod(i)}: {len(L)} pieces, events {ev}, windows {wins}")
# ---------------- the final module ----------------
T = max(F[n][J] for n in order)
NS = f"Ruliology.CellularAutomata.{PREFIX}"
L = ["module\n\n"] + [f"public import Ruliology.CellularAutomata.{mod(i)}\n" for i in range(len(order))]
L.append(f'''
/-!
# {len(order)} left sides of rule 30 through wheel {J}, each with its settling tick

The tree of strips through wheel {J}: every configuration with a leftmost black cell carries one of {len(order)} strips on
every wheel through {J} from strip tick `F j`, at a shift of at most 31 (`forced_front_tree`), and from strip tick {T} on
all of them (`forced_front_tree_uniform`, `…_left_side`, `…_seed`); the {len(order)} strips are realized by finite rows, no time
shift relates two of them, and each configuration is on exactly one (`exactly_left_sides`, `on_exactly_one`); every odd number
reaches one of the {len(order)} rows under `v ↦ 4 v ⊕ (2 v ∨ v)` modulo `2 ^ {K}` (`odd_reaches_one`). Strip 0 is the single
black cell's; strip i > 0 is the child at a fork of its parent, with the fork's child wheel complemented; each strip's period
doubles once in the range. The proof is one lemma per strip, in post-order, carrying the time through the strip's events
(`extend_from`, `step_white`, `white_fork`, `white_shift`); the fronts come from the walk in the strip modules.
-/

@[expose] public section

namespace {NS}

open Rule30FiveFrontsBase
open Rule30AgedLeftDiagonals Rule30FiniteDiagonals Rule30Diagonals Rule30Realization
open Rule30UniversalLeftSide (rowAt rowAt_add_mul ofRow ofRow_left Ld_ofRow D_recurrence)
open {mod(0)} (K)

set_option autoImplicit false

''')
N = len(order)
for i, n in enumerate(order):
    L.append(f"abbrev V{i} : Nat := {mod(i)}.V\nabbrev w{i} : Nat → Nat := {mod(i)}.w\n")
L.append(f"\n/-- On one of the strips, wheel by wheel. -/\ndef OnTree (a : Nat → Nat → Bool) (s : Nat) : Prop :=\n  " +
         " ∨\n  ".join(f"AlignedFrom K a V{i} s (F w{i}) {J}" for i in range(N)) + "\n")
L.append(f"\n/-- On one of the strips from strip tick `T`. -/\ndef OnTreeFrom (a : Nat → Nat → Bool) (s T : Nat) : Prop :=\n  " +
         " ∨\n  ".join(f"OnStrip K a V{i} s T {J}" for i in range(N)) + "\n")
L.append(f"\n/-- On one of the strips, from some time on. -/\ndef OnTreeAligned (a : Nat → Nat → Bool) (s : Nat) : Prop :=\n  " +
         " ∨\n  ".join(f"Aligned K a V{i} s {J}" for i in range(N)) + "\n\n")
def inj(i, N):
    return "Or.inr (" * i + ("Or.inl h" if i < N - 1 else "h") + ")" * i
for i in range(N):
    L.append(f"theorem inj{i} {{a : Nat → Nat → Bool}} {{s : Nat}} (h : AlignedFrom K a V{i} s (F w{i}) {J}) : OnTree a s := {inj(i, N)}\n")
L.append("\ntheorem onTreeFrom_of_onTree {a : Nat → Nat → Bool} {s : Nat} (h : OnTree a s) : OnTreeFrom a s " + str(T) + " := by\n  unfold OnTree at h\n  rcases h with " + " | ".join(f"h" for _ in range(N)) + "\n")
for i in range(N):
    L.append(f"  · exact {inj(i, N).replace('h', f'(onStrip_of_alignedFrom (fun j hj => Nat.le_trans ({mod(i)}.front_le j hj) (by decide)) h)')}\n")
L.append("\ntheorem onTreeAligned_of_onTree {a : Nat → Nat → Bool} {s : Nat} (h : OnTree a s) : OnTreeAligned a s := by\n  unfold OnTree at h\n  rcases h with " + " | ".join("h" for _ in range(N)) + "\n")
for i in range(N):
    L.append(f"  · exact {inj(i, N).replace('h', '(aligned_of_alignedFrom h)')}\n")
L.append("\n/-! ### The tree, strip by strip, in post-order -/\n\n")
# post-order
def postorder(n):
    out = []
    for m in children[n]: out += postorder(m)
    return out + [n]
po = postorder(order[0])
child_at = {n: {S[m]['fork']: m for m in children[n]} for n in order}
for n in po:
    i = idx[n]; m = mod(i); c = creation(n); ev = EV[n]
    start = c + 1 if S[n]['parent'] else 53207       # aligned through this wheel on entry
    body = []
    ind = "  "
    cur = "h"; curj = start
    def extend(lo_wheel, hi_wheel, hname, newname, ind):
        # extend alignment from wheel lo_wheel to hi_wheel using window b_{lo+1}_{hi}
        return f"{ind}have {newname} : AlignedFrom K a V{i} s' (F w{i}) {hi_wheel} :=\n{ind}  extend_from ha {m}.V_return {m}.words (by omega) (by decide) (by omega) {hname} {m}.b_{lo_wheel + 1}_{hi_wheel}\n"
    lines = [f"theorem done{i} {{a : Nat → Nat → Bool}} (ha : Recurrence a) {{s : Nat}} (h : AlignedFrom K a V{i} s (F w{i}) {start}) :\n"
             f"    ∃ s', s' ≤ s + 16 ∧ OnTree a s' := by\n  have h0 : AlignedFrom K a V{i} s (F w{i}) {start} := h\n"]
    # we carry the shift as `s` (unchanged at forks); at the doubling the right branch uses s + 16
    def emit(ev_list, cur, curj, ind, shift):
        out = []
        if not ev_list:
            out.append(f"{ind}exact ⟨{shift}, by omega, inj{i} (extend_from ha {m}.V_return {m}.words (by omega) (by decide) (by omega) {cur} {m}.b_{curj}_{J})⟩\n")
            return out
        (e, kind), rest = ev_list[0], ev_list[1:]
        if e > curj:
            out.append(f"{ind}have {cur}e : AlignedFrom K a V{i} {shift} (F w{i}) {e} :=\n{ind}  extend_from ha {m}.V_return {m}.words (by omega) (by decide) (by omega) {cur} {m}.b_{curj}_{e}\n")
            cur = f"{cur}e"
        out.append(f"{ind}rcases step_white ha {m}.V_return {m}.words (by decide) {cur} {m}.w_{e} with {cur}L | {cur}R\n")
        if kind == 'fork':
            q = child_at[n][e]; qi = idx[q]; qm = mod(qi)
            out.append(f"{ind}· -- the same side at the fork {e}\n")
            out += emit(rest, f"{cur}L", e + 1, ind + "  ", shift)
            out.append(f"{ind}· -- the other side: strip {qi}\n"
                       f"{ind}  have {cur}F : AlignedFrom K a V{qi} {shift} (F w{i}) {e + 1} := white_fork {cur} {cur}R\n"
                       f"{ind}    (fun j t hj => ({qm}.low_V' j t (by omega)))\n"
                       f"{ind}    {qm}.comp_V\n"
                       f"{ind}  have {cur}G : AlignedFrom K a V{qi} {shift} (F w{qi}) {e + 1} :=\n"
                       f"{ind}    alignedFrom_congr (fun j hj => F_congr j (fun i hi => {qm}.w_eq i (by omega))) {cur}F\n"
                       f"{ind}  exact done{qi} ha {cur}G\n")
        else:
            out.append(f"{ind}· -- aligned through the doubled wheel {e + 1}, same shift\n")
            out += emit(rest, f"{cur}L", e + 1, ind + "  ", shift)
            out.append(f"{ind}· -- the complement: a shift by 16\n"
                       f"{ind}  have {cur}S : AlignedFrom K a V{i} ({shift} + 16) (F w{i}) {e + 1} := white_shift {cur} {cur}R\n"
                       f"{ind}    (strip_shift {m}.V_return {m}.per_{e} {m}.anti_{e}).1 (strip_shift {m}.V_return {m}.per_{e} {m}.anti_{e}).2\n")
            out += emit(rest, f"{cur}S", e + 1, ind + "  ", f"({shift} + 16)")
        return out
    lines += emit(ev, "h0", start, "  ", "s")
    L.append("".join(lines) + "\n")
L.append(f'''/-! ### The headlines -/

/-- **The forced front on the tree.** -/
theorem forced_front_tree {{a : Nat → Nat → Bool}} (ha : Recurrence a) (ha0 : a 0 0 = true) : ∃ s, s ≤ 31 ∧ OnTree a s := by
  obtain ⟨s, hs, h⟩ := low_from (by decide) ha ha0 {mod(0)}.V_return {mod(0)}.words {mod(0)}.V_zero {mod(0)}.V_one {mod(0)}.hbw
    (strip_shift {mod(0)}.V_return {mod(0)}.per2 {mod(0)}.anti2) (strip_shift {mod(0)}.V_return {mod(0)}.per7 {mod(0)}.anti7)
    (strip_shift {mod(0)}.V_return {mod(0)}.per28 {mod(0)}.anti28) (strip_shift {mod(0)}.V_return {mod(0)}.per399 {mod(0)}.anti399)
    53207 (Nat.le_refl _)
  obtain ⟨s', hs', h'⟩ := done0 ha h
  exact ⟨s', by rw [lsum_53207] at hs; omega, h'⟩

theorem classification_bounded {{a : Nat → Nat → Bool}} (ha : Recurrence a) (ha0 : a 0 0 = true) :
    ∃ s, s ≤ 31 ∧ OnTreeAligned a s :=
  let ⟨s, hs, h⟩ := forced_front_tree ha ha0
  ⟨s, hs, onTreeAligned_of_onTree h⟩

/-- **From strip tick {T}**, that is from tick at most {T + 31} of its own clock. -/
theorem forced_front_tree_uniform {{a : Nat → Nat → Bool}} (ha : Recurrence a) (ha0 : a 0 0 = true) :
    ∃ s, s ≤ 31 ∧ OnTreeFrom a s {T} :=
  let ⟨s, hs, h⟩ := forced_front_tree ha ha0
  ⟨s, hs, onTreeFrom_of_onTree h⟩

/-- **Every configuration with a leftmost black cell.** -/
theorem forced_front_tree_left_side {{x : Int → Bool}} {{lo : Int}} (hleft : ∀ p, p < lo → x p = false) (hlo : x lo = true) :
    ∃ s, s ≤ 31 ∧ OnTreeFrom (Ld x lo) s {T} :=
  forced_front_tree_uniform (Ld_recurrence hleft) (by simpa [Ld, evol] using hlo)

/-- The single black cell. -/
theorem forced_front_tree_seed : ∃ s, s ≤ 31 ∧ OnTreeFrom D s {T} :=
  forced_front_tree_uniform D_recurrence (D_zero 0)

theorem left_side_classification {{x : Int → Bool}} {{lo : Int}} (hleft : ∀ p, p < lo → x p = false) (hlo : x lo = true) :
    ∃ s, OnTreeAligned (Ld x lo) s :=
  let ⟨s, _, h⟩ := classification_bounded (Ld_recurrence hleft) (by simpa [Ld, evol] using hlo)
  ⟨s, h⟩

/-! ### Realization, distinctness, the arithmetic form -/

theorem Ld_row (v : Nat) {{j : Nat}} (hj : j ≤ {J}) (t : Nat) : Ld (ofRow v) 0 j t = Sp K v j t :=
  Ld_ofRow (K := K) (by decide) v t j (by show j < {K}; omega)

theorem realized (v : Nat) : Aligned K (Ld (ofRow v) 0) v 0 {J} :=
  fun _ hj => ⟨0, fun t _ => Ld_row v hj (t + 0)⟩

theorem comp_symm {{v v' w : Nat}} (h : ∀ t, Sp K v' w t = !Sp K v w t) : ∀ t, Sp K v w t = !Sp K v' w t := fun t => by
  rw [h t]; cases Sp K v w t <;> rfl

''')
# distinctness: pairs
lineage = {}
for n in order:
    ln = []; x = n
    while x is not None: ln.append(x); x = S[x]['parent']
    lineage[n] = ln[::-1]      # root first
def low_chain(target, strip, wheel):
    """a term proving Sp K V_strip wheel t = Sp K V_target wheel t for an ancestor target of strip, wheel below every fork on the way; as a tactic `rw` list."""
    ln = lineage[strip]; k = ln.index(target); rws = []
    x = strip
    while x != target:
        rws.append(f"{mod(idx[x])}.low_V' {wheel} t (by omega)"); x = S[x]['parent']
    return rws
pairs = []
for a_i in range(N):
    for b_i in range(a_i + 1, N):
        na, nb = order[a_i], order[b_i]
        la, lb = lineage[na], lineage[nb]
        common = [x for x in la if x in lb]; mcs = common[-1]
        fa = S[la[la.index(mcs) + 1]]['fork'] if mcs != na else None
        fb = S[lb[lb.index(mcs) + 1]]['fork'] if mcs != nb else None
        # the lineage that leaves mcs lower carries the complement at f+1; the other has mcs's word there
        if fa is not None and (fb is None or fa < fb): f = fa; comp_side, same_side = na, nb; qa = la[la.index(mcs) + 1]
        else: f = fb; comp_side, same_side = nb, na; qa = lb[lb.index(mcs) + 1]
        pairs.append((na, nb, mcs, f, comp_side, same_side, qa))
L.append("theorem distinct :\n    " + " ∧\n    ".join(f"¬ Related K {J} V{idx[na]} V{idx[nb]}" for (na, nb, *_ ) in pairs) + " :=\n  ⟨")
terms = []
for (na, nb, mcs, f, comp_side, same_side, qa) in pairs:
    ia, ib = idx[na], idx[nb]; ma, mb = mod(ia), mod(ib)
    # hc : ∀ t, Sp K Va (f+1) t = !Sp K Vb (f+1) t
    # Sp comp_side (f+1) t = Sp qa (f+1) t = !Sp mcs (f+1) t ; Sp same_side (f+1) t = Sp mcs (f+1) t
    rw_comp = low_chain(qa, comp_side, f + 1)          # comp_side -> qa
    rw_same = low_chain(mcs, same_side, f + 1)         # same_side -> mcs
    comp_fact = f"{mod(idx[qa])}.comp_V t"
    if comp_side == na:
        hc = (f"(fun t => by rw [{', '.join(rw_comp + [comp_fact] + rw_same)}])" if (rw_comp or rw_same) else f"(fun t => {mod(idx[qa])}.comp_V t)")
    else:
        inner = f"(fun t => by rw [{', '.join(rw_comp + [comp_fact] + rw_same)}])" if (rw_comp or rw_same) else f"(fun t => {mod(idx[qa])}.comp_V t)"
        hc = f"(comp_symm {inner})"
    # h4 : ∀ t, Sp K Va 400 t = Sp K Vb 400 t : both down to the root (mcs suffices)
    ra = low_chain(mcs, na, 400); rb = low_chain(mcs, nb, 400)
    h4 = f"(fun t => by rw [{', '.join(ra + rb)}])" if (ra or rb) else "(fun t => rfl)"
    terms.append(f"not_related (w := {f + 1}) (p := 400) (by omega) (by omega) ({ma}.per16 _ (by omega)) ({ma}.per16 _ (by omega))\n"
                 f"      ({mb}.per16 _ (by omega)) {hc}\n      {h4} {ma}.prim")
L.append(",\n   ".join(terms) + "⟩\n\n")
# on_exactly_one
L.append("theorem on_exactly_one {a : Nat → Nat → Bool} {s s' : Nat} :\n    " +
         " ∧\n    ".join(f"¬ (Aligned K a V{idx[na]} s {J} ∧ Aligned K a V{idx[nb]} s' {J})" for (na, nb, *_ ) in pairs) + " :=\n  ⟨")
acc = []
for k, (na, nb, *_ ) in enumerate(pairs):
    proj = "distinct" + ".2" * k + (".1" if k < len(pairs) - 1 else "")
    acc.append(f"fun h => {proj} (side_unique {mod(idx[nb])}.V_return h.1 h.2)")
L.append(",\n   ".join(acc) + "⟩\n\n")
L.append(TH + "theorem rows_finite : " + " ∧ ".join(f"(V{i} < 2 ^ K ∧ V{i}.testBit 0 = true)" for i in range(N)) + " :=\n  ⟨" +
         ", ".join(f"{mod(i)}.V_finite" for i in range(N)) + "⟩\n\n")
L.append(f'''/-- **Exactly {N} left sides through wheel {J}.** -/
theorem exactly_left_sides :
    (∀ {{x : Int → Bool}} {{lo : Int}}, (∀ p, p < lo → x p = false) → x lo = true → ∃ s, OnTreeAligned (Ld x lo) s) ∧
    ({" ∧ ".join(f"(V{i} < 2 ^ K ∧ V{i}.testBit 0 = true)" for i in range(N))}) ∧
    (∀ v, Aligned K (Ld (ofRow v) 0) v 0 {J}) ∧
    ({" ∧ ".join(f"¬ Related K {J} V{idx[na]} V{idx[nb]}" for (na, nb, *_ ) in pairs)}) :=
  ⟨fun hl h0 => left_side_classification hl h0, rows_finite, realized, distinct⟩

theorem aligned_uniform {{a : Nat → Nat → Bool}} {{u s : Nat}} : ∀ J', Aligned K a u s J' →
    ∃ T, ∀ j, j ≤ J' → ∀ t, T ≤ t → a j (t + s) = Sp K u j t := by
  intro J'
  induction J' with
  | zero =>
    intro h
    obtain ⟨T, hT⟩ := h 0 (Nat.le_refl _)
    exact ⟨T, fun j hj t ht => by
      have e : j = 0 := by omega
      subst e
      exact hT t ht⟩
  | succ J' ih =>
    intro h
    obtain ⟨T1, h1⟩ := ih (fun j hj => h j (by omega))
    obtain ⟨T2, h2⟩ := h (J' + 1) (Nat.le_refl _)
    refine ⟨max T1 T2, fun j hj t ht => ?_⟩
    by_cases hc : j ≤ J'
    · exact h1 j hc t (by omega)
    · have e : j = J' + 1 := by omega
      subst e
      exact h2 t (by omega)

{TH}theorem rowAt_succ_lt (v n : Nat) : rowAt K v (n + 1) < 2 ^ K := by
  simp only [rowAt, Rule30UniversalLeftSide.stepK]
  exact Nat.mod_lt _ (Nat.pow_pos (by omega))

{TH}theorem eq_of_low_bits {{x y : Nat}} (hx : x < 2 ^ K) (hy : y < 2 ^ K) (h : ∀ j, j < K → x.testBit j = y.testBit j) : x = y := by
  apply Nat.eq_of_testBit_eq
  intro j
  by_cases hj : j < K
  · exact h j hj
  · have hp : 2 ^ K ≤ 2 ^ j := Nat.pow_le_pow_right (by omega) (by omega)
    rw [Nat.testBit_lt_two_pow (Nat.lt_of_lt_of_le hx hp), Nat.testBit_lt_two_pow (Nat.lt_of_lt_of_le hy hp)]

{TH}theorem reaches {{v u s : Nat}} (hu : rowAt K u 32 = u) (hlt : u < 2 ^ K) (h : Aligned K (Ld (ofRow v) 0) u s {J}) :
    ∃ n, rowAt K v n = u := by
  obtain ⟨T, hT⟩ := aligned_uniform {J} h
  obtain ⟨n, hn⟩ : ∃ n, (T + 1) * 32 + s = n + 1 := ⟨(T + 1) * 32 + s - 1, by omega⟩
  refine ⟨n + 1, eq_of_low_bits (rowAt_succ_lt v n) hlt fun j hj => ?_⟩
  have hj' : j < {K} := hj
  have e := hT j (by omega) ((T + 1) * 32) (by omega)
  rw [hn, Ld_row v (by omega)] at e
  have base : rowAt K u (0 + (T + 1) * 32) = u := by
    rw [rowAt_add_mul hu]
    rfl
  rw [Nat.zero_add] at base
  simp only [Sp] at e
  rw [base] at e
  exact e

/-- **Every odd number reaches one of the {N} rows.** -/
theorem odd_reaches_one (v : Nat) (hv : v.testBit 0 = true) :
    ∃ n, {" ∨ ".join(f"rowAt K v n = V{i}" for i in range(N))} := by
  have h0 : ofRow v 0 = true := by simpa [ofRow] using hv
  obtain ⟨s, h⟩ := left_side_classification (ofRow_left v) h0
  unfold OnTreeAligned at h
  rcases h with {" | ".join("h" for _ in range(N))}
''')
for i in range(N):
    L.append(f"  · obtain ⟨n, e⟩ := reaches {mod(i)}.V_return {mod(i)}.V_finite.1 h\n    exact ⟨n, {inj(i, N).replace('h', 'e')}⟩\n")
L.append(f"\ntheorem fronts : " + " ∧ ".join(f"F w{i} {J} = {F[order[i]][J]}" for i in range(N)) + " :=\n  ⟨" + ", ".join(f"{mod(i)}.front" for i in range(N)) + "⟩\n")
L.append(f"\nend {NS}\n")
open(f"{OUT}/{PREFIX}.lean", 'w').write("".join(L))
print(f"final module written; T = {T}; {len(pairs)} pairs; {time.time()-t0:.0f} s")
