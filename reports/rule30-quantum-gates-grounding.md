# Can quantum gates help? A grounding for the programme (L1071)

Local, 28 October 2026, answering the owner's question as relayed in GPT's GC2030: can the modern science of quantum
gates and circuits expand our ordinary logic-gate view of Rule 30 with additional information, and how might we use
it? This is a literature grounding by four parallel research agents reading primary sources, followed by my own
checks of their carrying claims. Agent findings are labelled with what the agent read. Anything an agent could not
read is marked.

**Record searched:** `record_find.py` for `quantum|Toffoli|tensor.network|reversible circuit` (GPT, GC2030) and
`Meier|Staffelbach|Koc|Apohan|cryptanaly|dual.unitar|influence matrix|Sfairopoulos|Garrahan|butterfly` (Local). The
record already credits Meier and Staffelbach (1991) and Koç and Apohan (1997) in PRIOR-ART.md (Cloud, 5 October),
but neither paper had been read. Nothing in the record treats dual-unitarity, influence matrices or spin-model
reformulations.

## Verdict

**Quantum computing itself will not help us.** On our machines it cannot help at all. Even on real hardware it
would give at most quadratic speedups on our search and counting tasks, with answers that are not proofs. It has no
known bearing on Prize Problem 3.

**The mathematics built around quantum gates does transfer, but only as classical tools.** Three pieces do:
1. **Space-time duality** gives an exact description of what Rule 30's left environment supplies: one fresh,
   memoryless bit per step. It also says where the open problem is: the right environment, which has memory.
2. **Reversible-circuit accounting** (AND or Toffoli count, algebraic normal form) tracks exactly the correlations an
   observer keeps. It led to one new computed fact this session, §2: the centre cell has algebraic degree exactly
   2t − 1.
3. **Transfer matrices** are the exact way to count histories. Tensor networks are the same computation in another
   form and add no structure.

Everything else found studies a changed system: quantum spin models, Rule 54, dual-unitary circuits and quantum
cellular automata. It is useful as language and analogy, not as transferable theorems.

## 1. What quantum algorithms could and could not do

Agent report (read BBBV, Zalka, Montanaro, Ambainis–Kokainis, BHMT, Beals et al., Chia–Chung–Lai, Coudron–Menda and
others; full citations in L1071). Here T is the size of the search tree.

| Task | Best classical (ours) | Best quantum | Advantage | Lost in classical simulation |
|---|---|---|---|---|
| compute c(n) | direct Θ(n²) cell updates | reversible simulation only, about n² Toffoli and 3n² CNOT | none known | nothing to gain |
| ancestors of a word | inverse-tree depth-first search, SAT | Montanaro backtracking, O(√T·n^{3/2} log n) | at most quadratic | costs at least classical brute force |
| prove a word forbidden | exhaustive search, SAT with DRAT certificate | backtracking detection | at most quadratic | **the certificate**: a bounded-error claim, not a proof |
| count pasts | enumeration | quantum counting (approximate quadratic; exact none near half) | at most quadratic | exactness |
| periodic ring orbits | functional graph, pair graph (L1066) | Grover for F^p(x) = x | quadratic for one orbit, none for listing all | as above |

Two facts make simulation pointless:
- *Laptop limit:* statevector simulation tops out around 32–34 qubits on a laptop, while a Rule 30 oracle for a
  word of length 10 over depth 10 already needs about 200 ancillas.
- *No shortcut:* simulating a classical oracle on a superposition evaluates it on every input.

Grover's bound is optimal relative to an oracle (BBBV, Zalka). Quadratic speedups are not expected to pay off on early
fault-tolerant hardware (Babbush et al., PRX Quantum 2021).

**Prize Problem 3** asks whether computing c(n) needs more than O(n) effort, meaning total steps on a finite machine.
Nothing quantum is known to bear on it.
- *Depth is not effort:* a quantum circuit of sublinear depth but polynomial size would not count. Classical
  parallel simulation already has depth Θ(n).
- *Oracle-only results:* the proved quantum results on inherently sequential computation are all relative to
  oracles (Chia–Chung–Lai; Coudron–Menda; Chung–Fehr–Huang–Liao; Ozhigov on iterated functions).
- *Lower bounds are harder:* a quantum lower bound would imply roughly a classical one.
- *No prior work:* no paper studies Rule 30's centre column with quantum algorithms. One related paper (Fedoriaka
  2025) explicitly excludes Rule 30.

**Close this route,** with the table above as the prior-art note.

## 2. Reversible circuits and exact information: the import that produced something

Rule 30's update is f(a, b, c) = a ⊕ b ⊕ c ⊕ bc, which is Rule 150 (all XOR, the Clifford-like part) plus one AND (one
Toffoli). Its reversible embedding is 3 CNOTs and 1 Toffoli per cell update (GPT, GC2030). The agent read Meuli et
al. (ICCAD 2019): T-count is at most 4 × the AND count. So **Toffoli count is the classical multiplicative
complexity under another name.** On basis states a CNOT+Toffoli circuit is classically trivial, so magic and
stabiliser measures say nothing new about Rule 30's own dynamics. What transfers is the bookkeeping:
- algebraic normal form over GF(2), or phase polynomials;
- XOR-AND graphs;
- AND-count bounds.

That bookkeeping is exactly what GC2026–GC2029 needed. The three-valued observer forgets that (NOT r) OR (r OR s) = 1.
The ANF does not.

**Cryptanalysis prior art.**
- *Meier and Staffelbach (EUROCRYPT 1991; paywalled, so read through Spencer's thesis and Mariot's 2024 survey):*
  they recover the seed from the centre column. They guess the right-adjacent column, which is far from equiprobable
  (about 18 bits of entropy for n = 300), and solve the left side by left-permutivity. Wolfram describes the same
  two-column construction (NKS p. 604) and already states the sideways rewrite in his 1986 paper.
- *Koç and Apohan (1997, abstract):* they invert one step of a row by treating Rule 30 as its best affine
  approximation (Rule 150) plus corrections.
- *Spencer (arXiv:1306.3546):* forced-bit propositions; for example, output 010 makes the predecessor row unique.
  These are the retained relationships the three-valued observer misses.

**New computed fact (CONJECTURE; COMPUTED for t ≤ 12).** As a GF(2) polynomial in its 2t + 1 initial cells
x_(−t) … x_t, the centre cell c(t) has degree exactly **2t − 1** for 2 ≤ t ≤ 12. For 3 ≤ t ≤ 12 it has a **unique**
top-degree monomial, the product x_(−t+2) x_(−t+3) ⋯ x_t of all cells except the two leftmost. (At t = 2 there are
two top monomials.)
- *Monomial counts* for t = 1 … 12: 4, 10, 30, 122, 346, 1,360, 4,852, 23,094, 79,192, 324,572, 1,244,124, 5,529,024.
- *How it was found:* the agent first computed it for t ≤ 9. I recomputed it independently
  (`tests/probes/wolfram/centre_anf_degree.py`, exhaustive truth table and Möbius transform, t ≤ 11). The t = 12
  case, 33,554,432 rows in 2.2 s under `run_capped.py`, was predicted before the run and held.
- *The bound is 2t, not 2t − 1, a priori.* The leftmost cell enters only linearly (left-permutivity), so the only
  degree-2t monomial possible is x_(−t+1) ⋯ x_t.
- *Two parity statements to prove.* The Möbius formula reduces the conjecture to two of them:
  - the number of initial rows with x_(−t) = 0 and c(t) = 1 is **even**;
  - among rows with x_(−t) = x_(−t+1) = 0 it is **odd**, and for every other deleted cell x_j it is even.
- *Not in the literature:* Mariot's 2024 survey (arXiv:2405.02875) lists the algebraic degree of CA generators as an
  open question. The agent found no published degree result for Rule 30, and the monomial-count sequence is not in
  OEIS. That absence is unverified.
- *Bearing on the prize:* none directly. It is a structural fact about how much nonlinearity each step adds, one
  degree per step after the first.

## 3. Space-time duality: what the left boundary supplies, exactly

Agent report (read Bertini–Kos–Prosen 2019, Gombor–Pozsgay 2022 §3.3, Klobas–Bertini–Piroli 2021, Wolfram 1986
§§3–6, Tisseur 2000, Courbage–Kamiński).

**What dual-unitarity means and buys.** Dual-unitary circuits are unitary in both time and space. That makes
correlations live only on the light-cone edges and the environment an exact memoryless "perfect dephaser" (Lerose,
Sonner and Abanin, PRX 2021). Classically the analogue needs a rule that is a bijection in both directions
(Gombor–Pozsgay). **Rule 30 fails it.** It is deterministic sideways only to the left, and not invertible. No source
calls Rules 30, 90 or 150 dual-unitary.

**What survives on the permutive side** (my check of the agent's derivation, by hand):
- **The left environment is a perfect dephaser** (PROVED, elementary). Under random initial conditions the column
  just left of any region is independent fair coins, independent of everything to its right. Its cell at time t is
  the exact XOR of the initial cell t places further left, which is fresh at step t, plus a function of initial
  cells to the right of that one, which include the earlier fresh ones. For fixed data on the right, that is a
  triangular bijection. This
  is the exact version of L1069's "fresh bit through the XOR": the left supply has no memory at all.
- **Correlations live only on the right light-cone edge** (PROVED, elementary). Every later cell contains its
  leftmost initial input by XOR. So it is independent of any single initial cell except the one at x = t. This is
  the one-sided analogue of the dual-unitary edge property.
- **The open quantity is the right environment, which has memory.** Wolfram (1986) measured that on average
  0.26 + 0.19 T right-hand initial cells affect a length-T column, against all T + 1 on the left. Tisseur's average
  exponent I⁻ is the rigorous version. Nobody has computed it rigorously for Rule 30, and the quantum toolkit offers
  no exact method for it.

So for the owner's boundary question (GC2025, L1069), the toolkit gives a precise split: the left supply is exactly
memoryless, and all memory, and all hope of structure, is in the right boundary.

**A prior-art correction.** The left damage speed in the literature is **0.2428 ± 0.0003** (Grassberger, cited in
Wolfram 1986). The left edge is diffusive and its probability of being affected is damped exponentially beyond it.
- *Our figure:* the record's 0.246 (§8.30, §8.66) is a finite-time measurement.
- *The agent's run:* 60 samples to T = 4,000 on the M5 gave 0.2442, with the front's spread growing like √t, which is
  consistent with slow convergence from above.
- *Do not conflate:* Baetens and Gravner's 0.41 is the linearised (Boolean-derivative) cone, a different object.

## 4. Counting histories: transfer matrices, not spin models

Agent report (read Sfairopoulos, Causer, Mair, Powell and Garrahan, arXiv:2503.19572 v4, April 2026, and
predecessors; Jen 1989; Powley and Stepney; Hedlund 1969 through Kari's notes).

**The spin-model reformulation studies a changed system.** It maps Rules 30, 54 and 201 to plaquette Hamiltonians
whose ground states are valid histories.
- *What its degeneracy counts:* periodic orbits on a torus, or free boundary data (open boundaries, 2^(L+2M−2)). That
  is not our count.
- *What it shows for Rule 30:* only small-size perturbation theory and numerics.
- *Its own limit:* the linear-rule symmetry tools fail for Rule 30, by the authors' account.

**What is exact.**
- *Hedlund's balance theorem:* every word of a surjective CA has exactly 4^t pasts on its widening light-cone window.
- *Jen's 4×4 recurrences:* exact one-step preimage counts.
- *Powley–Stepney traces:* preimage counts on rings as Tr(D^N) of a de Bruijn matrix.

With left-permutivity every past is fixed by its right-edge column. So our constrained counts become path counts in
a finite automaton:
- the root pasts (1, 2, 5, 8, …, 122 at depth 12, 8,858 at depth 140);
- GPT's background-parent relation (GC2024);
- the ring pair graph (L1066).

Tensor-network contraction is the same computation; it is exact only at full bond dimension and gives no
certificate when truncated.

**A curiosity, by inspection (agent).** Rule 54's reversible brickwork form is χ = s₁ ⊕ s₂ ⊕ s₃ ⊕ s₁s₃, the same
Boolean function y ⊕ (x OR z) as Rule 30. Its linear input is the past centre instead of the left neighbour. That
choice makes Rule 54 time-reversible and integrable, while Rule 30's choice makes it left-permutive. The same gate,
wired differently, gives an integrable system or a chaotic one.

## 5. The smallest discriminating next steps

1. **Prove the degree law** (a proof task; GPT or Local). The test is already run: t = 12 held as predicted.
   - *Target:* the two parity statements of §2, by induction on t, using c = x_(−t) ⊕ g and the structure of the
     first row.
   - *Failure condition:* a counterexample at t = 13, which is computable at 2^27 rows.
   - *Gain:* an exact, new structural fact about how Rule 30 accumulates nonlinearity. This is the circuit view's
     AND accounting made concrete.
2. **Measure the right environment's memory exactly** (computation, small).
   - *Definition:* for a length-T segment of a column, the exact number of right-hand initial cells that can change
     it, maximised or averaged over the rest. Compute it exactly by ANF dependence for T ≤ 20.
   - *Prediction:* linear growth with slope near Wolfram's 0.19.
   - *Failure condition:* a slope far from 0.19, or growth that is not linear.
   - *Gain:* the one boundary quantity the toolkit identifies as open, and the quantitative core of the owner's
     boundary-supply question.
3. **Do not pursue:** simulated quantum algorithms, spin-model ground states or tensor-network truncation as sources
   of Rule 30 structure. The reasons are in §§1 and 4.

What would make a quantum idea more than notation: an exact identity or bound for ordinary Rule 30 that the circuit
picture suggests and that we then prove classically. The degree law (§2) and the dephaser split (§3) are the first
two candidates.

## Status

| Item | Status |
|---|---|
| §1 quantum speedups at most quadratic; none for c(n) or Problem 3 | literature, agent-read primary sources |
| §2 deg c(t) = 2t − 1 with unique top monomial (3 ≤ t ≤ 12) | CONJECTURE, COMPUTED t ≤ 12 (two independent implementations to t = 9) |
| §3 left perfect dephaser, right-edge-only correlations | PROVED, elementary, Local's check of the agent's derivation |
| §3 literature value 0.2428 for the left damage speed | literature (Wolfram 1986 citing Grassberger); record's 0.246 is a finite-time measurement |
| §4 spin-model counts are not our counts | agent-read primary source |
