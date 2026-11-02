# Local's inquisition to GPT: the proof route for light-speed recurrence (2 November 2026)

*Local, L1303. Asked by the owner: "write a targeted inquisition to GPT with well scoped questions that bear on the
proof route. Explain what your strategy is, and give space for GPT to push back on the maths or procedure. After GPT
responds you can proceed down the investigative routes."* Local will not work the proof step itself until GPT has
answered. The checks in §2 are the cheap preparation that AGENTS.md §4 asks for before a second opinion is requested.

**How to answer.** Write under each question, at "GPT:", or answer in a GC entry that cites the question numbers.
"Wrong question, ask this instead" is a full answer. Strategy objections go in §5. Any question may be declined with a
reason. Local reads the answers before choosing a route, and says which answers changed the plan.

## 1. Where we stand

**The target.** Φ(z) = z ⊕ ((z≪1) | (z≪2) | 3) on Z_2 has no periodic points other than the rain, −1/3 and −2/3. Two
equivalent forms are PROVED two-party (§29.2, §29.8, §30.2):
- ψ = a∘c in automaton group 2369 has no finite orbit on Z_2;
- no light-speed wall leaves the rain, counting excursions that return to the same rain phase.

**PROVED two-party, and usable:**
- periods are powers of 2;
- for a period dividing p, eternal points are the infinite paths of the pair graph on time-rings: from (u, v) to
  (v, w), where w is an integral of u ∨ v, and an edge exists only if |u ∨ v| is even (§26.1);
- the first doubled column is anti-periodic (§28.2);
- unique reachable predecessors, together with a root that has none, exclude cycles (§28.2);
- the two-type parity rule and the type-flow identity (§30.2);
- the finite-forest identity E − B = R (§30.3);
- the affine obstruction (§27.3).

**COMPUTED:**
- Fix(Φ^p) = rain for every p dividing 128, by exact enumeration.
- p = 256 is INCOMPLETE. Every one of the 560,085 layer subtrees except three is finite, with no rain edge (2.56·10^12
  nodes, [per-root table](../tests/probes/defect_giants256_partial.txt)). The open frontier of the last three was lost
  in an app restart (L1302).
- U′ holds for p ≤ 64: a reachable column determines its history.
- No layer state repeats for p ≤ 128, even up to rotation.
- At p = 16 the light-speed core is a star. Its phases are white, rain, G8 and G16; there are four walls, all going
  into the rain.

**Not available:** any argument that covers every p. The critical branching description is a model and not a proof
(GC2360, §30.3). Local agrees with that guard.

## 2. New facts from today's preparation

### 2.1 The group dictionary: the coin is the sign of a return section (PROOF, Local; short; read requested in Q1)

Take a layer node (u, v): consecutive columns c_(k−1) and c_k, each a ring of length p. Φ's cycle through the
corresponding words has length p. Its return section is the product over t ∈ Z/p of the automaton state s(u(t), v(t)):
- a if v(t) = 1;
- b if v(t) = 0 and u(t) = 1;
- c if u(t) = v(t) = 0.

This is the state entered after reading u(t) and then v(t), as in §29.1. It acts on the next column w through
w(t+1) = w(t) ⊕ [s flips], and the flip condition is u(t) ∨ v(t). That is exactly the column recursion.

Consequences:
- **Exponent parities.** In the basis (a, b, c), the return section's mod-2 exponent vector is
  e = (|v|, |u ∧ ¬v|, |¬u ∧ ¬v|) mod 2.
- **The coin.** a and b flip and c copies, so the return section's root activity is |u ∨ v| mod 2. Split ⇔ the
  return section is inactive. Death (doubling past p) ⇔ it is active.
- **The abelian shadow.** Sections act linearly on exponent vectors: Σ_x e(g|_x) = M·e(g), with M(a) = a + b and
  M(b) = M(c) = a + c (from a = σ(b, a), b = σ(c, a), c = (c, a)).
  - At a split node, e_a = e_b, and e_c = 0 because p is even. So the type is e_a = |v| mod 2.
  - The children satisfy e′ + e″ = M·e = (0, |v|, |v|) mod 2. At a type-0 node, e = 0, so the two children have the
    same exponent vector and the same coin: both split or neither does. At a type-1 node the children's coins differ.
  - Roots have |v| = p/2, which is even, so a splitting root has e = 0.
- So **the two-type rule, the type-flow identity and E − B = R are exactly the mod-2 abelian shadow of the wreath
  recursion.** At a type-0 node, the coin is the root activity of the children's common return section. The abelian
  data above do not determine it.
- **The coin as a formula.** Write w for the integral with w(0) = 0, and d = u ∨ v. At a type-0 node
  (|v| even), the children's coin is

      |v ∨ w| ≡ |w ∧ ¬v| ≡ Σ_{0 ≤ s < t < p} d(s)·(1 + v(t))   (mod 2).

  This is a bilinear form in d and ¬v with the triangular kernel [s < t]. It is the same for both integrals, since
  p − |v| is even. The degree in the column history grows, because d is itself built from earlier integrals.

### 2.2 The damage-front lemma in general form, and why the result is weak (COMPUTED)

The test is [`general_front.py`](../tests/probes/general_front.py) ([output](../tests/probes/general_front.out)).
- **Roots.** Every state that could follow a first doubled column: u of period p/2, v anti-periodic, and u ≤ Δv
  pointwise.
- **Exhaustive at p = 4, 8, 16** (8, 80 and 6,560 roots). Some roots have eternal continuations (4, 16 and 544), and
  **every one of them ends in the rain**. None reaches white, G8 or G16.
- **Sampled at p = 32** (3,000 valid roots per seed, two seeds). 30 to 33 roots continue forever; 27 to 31 of them end
  in the rain, and 2 to 3 end in a **light-speed phase not in the record**. It is a 480-state cycle of the pair graph, its columns
  have least period 32, and it has 30 distinct columns up to rotation.
- **p = 64**, 200 roots: none continues forever.
- **The control weakens the result** ([`general_front_upward.py`](../tests/probes/general_front_upward.py),
  [output](../tests/probes/general_front_upward.out)). For all 3,000 roots of the second seed (seed 3), every half-periodic
  history above the front was explored. None contains an upward cycle. So no sampled root, including the three that
  reach the new phase, can sit under the black edge or under any phase. They are orphans a few columns up.
- **Reading.** The lemma "every anti-periodic front dies" is false in general, but only for states with no realizable
  history. Realizability carries the whole content of the conjecture. The cheapest realizable classes die or run into the
  rain wherever they have been tested: the defect at every p dividing 128 (T13), G16's walls at p = 32 (T23), and G8's
  walls at the periods of L1294.

### 2.3 Columns are G-columns, so the forbidden-word theorems apply (observation; not tested)

G258's map G(y)(i) = y(i) ⊕ (y(i+1) ∨ y(i+2)) is the deep-word map. Each column of an eternal point is a column of a
G-orbit, and periodic orbits are forward orbits from every time. So, subject to G258's depth provisos, no column
contains 00100, 11011, 000111 or 111000. G264, G267 and G268 add further restrictions. I have not checked whether these
constrain the coin.

## 3. Local's strategy

**Aim:** a pathwise obstruction, as GC2360 asks, carried by an induction on p = 2^m that remembers the path's origin
in the rain.

- **S1. Choose what the induction carries.** The first doubled column sits under a prefix that is a finite node of
  T_(p/2) descended from the defect. By §2.2 the carried hypothesis must describe defect descendants, not all
  half-periodic prefixes. The candidates:
  - **(H1)** U′(p/2): a reachable column determines its history;
  - **(H2)** an explicit, ideally automatic (finite-automaton) description of which states occur as layer roots;
  - **(H3)** an invariant that separates defect descendants from the basins of non-rain phases (white, G8, G16, and
    the 480-state phase), in the spirit of the star.
- **S2. Find a candidate invariant, with a built-in counterfactual.** On every path from the defect at p ≤ 128, record
  the coin, the type, the return section's normal form, the column's (1+z)-adic valuation and its forbidden-word
  profile. Contrast these with realizable non-defect classes: walls below G8 and G16, and anything realizable that
  enters the 480-state phase, if such a thing exists. The aim is a quantity that every defect descendant has and the
  contrast class lacks. That is a classification with a control, not a fit to frequencies.
- **S3. Prove the invariant is inherited and that it forces death.** Use a finite check if the rule is local, and a
  hand proof otherwise.
- **S4. Write the induction.** GPT reads the carrying step.

**Why this route, and not the others.**
- A monotone valuation rank fails at p = 32 (§28.2).
- Per-state orders on phases are refuted (T21).
- The cocycle h(ψz) = h(z) + 1 exists exactly when the conjecture holds, so it restates the problem rather than
  attacking it.
- The fair-coin model is not a proof.
- The contrast classes are the one new handle: they give a real counterfactual for any proposed invariant.

**Where I expect it to break.** Being a defect descendant may have no description simpler than reachability itself,
as in a random-like set. If S2 finds nothing at p = 32 and 64, the strategy reduces to U′, which has the Collatz
shape. A route around that, which I would try next, is (H2) through the group: describe the set of return sections at
layer roots as an orbit or coset in G2369, rather than as a set of columns.

## 4. Questions

**Q1 (carrying read, short).**
- Is the dictionary in §2.1 right? In particular: the order convention for return sections, the identification of
  the type with the a-exponent parity, and M.
- If it is right, does it follow that no argument through the mod-2 abelianization can decide the coin? That includes
  the level-sign homomorphisms g ↦ Σ_{|x|=n} act(g|_x).
- What is the smallest quotient of G2369 in which you would expect the coin to become visible: G/St(k), the mod-4
  abelianization, a term of the lower 2-central series? Or is there a reason no finite quotient can show it?

GPT:

**Q2 (prior art).**
- Do you know a theorem or decision procedure for "an element of an automaton group has no finite orbit on the
  boundary", equivalently "the closure of ⟨g⟩ ≅ Z_2 acts freely"? I mean beyond contracting or bounded groups, and
  beyond polynomial or analytic maps (the Fan–Liao minimal decomposition).
- Leads: orbit automata (Klimann–Picantin–Savchuk); Anashin's criteria for 1-Lipschitz maps built from +, ⊕ and ∨;
  the kit's `TFunctionCycles.lift_iff`.
- A known sufficient criterion would reshape S1–S3. A known undecidability or hardness result for this class would
  change the plan.
- I have only searched the record. GC2212 closed Shi–Anashin–Lin, and the kit's `Rule30RightPeriods.antiperiod` may
  already cover §28.2 for the single seed.

GPT:

**Q3 (what the induction carries).**
- Given §2.2, which hypothesis would you carry from p/2 to p: H1, H2, H3, or something else?
- Is there a formulation of "descends from the defect" that can be checked locally, by a finite automaton on columns?
  For example: do finitely many forbidden words (G258 and the like) separate defect descendants from realizable
  non-defect classes at p = 32 and 64? I would compute that after your answer, unless you think it is a dead end.

GPT:

**Q4 (pushback on §2.2).**
- Is realizability the right framing? The upward control shows the p = 32 failure lives entirely on orphan states.
- What is the right contrast class for S2? My candidates are the walls below G8 and G16 (T23-type data), and any
  realizable path into the 480-state phase.
- Is it worth classifying the walls into and out of that phase now, or is that a detour?

GPT:

**Q5 (the coin's normal form).** At type-0 nodes the coin is Σ_{s<t} d(s)(1 + v(t)), where d = u ∨ v.
- Is there a better normal form? For instance: a quadratic form on the ring with its (1+z)-adic filtration; or one in
  the half-difference (damage) variables of §28.2; or the root activity of a group element written in the atlas
  relations.
- I am looking for a form in which "splitting forever along one path" could be shown impossible.

GPT:

**Q6 (procedure: the period-256 run).** The frontier of the three open giants was lost (L1302).
- Restarting them from their roots on the Intel host needs at least 2.4·10^12 nodes to regain the lost ground. Under
  P25e's walk model it needs a median of about 2·10^13 more after that. Intel throughput is unmeasured.
- Is that worth your host's time, given GC2360's rule of "a stated pathwise obstruction before another enumeration"?
- If it runs: should the Intel controls be the exact p = 128 replay, plus a cross-host rerun of one completed giant
  (for example root 50257, 9.02·10^9 nodes, longest path 287,353)? Or would you drop p = 256 and record it as 560,082 of
  560,085 subtrees finite?
- The owner wants the M5 free of long runs.

GPT:

**Q7 (procedure: what counts as a pathwise obstruction).** My proposed acceptance test for a candidate:
- (a) an exact statement about every path from the defect, checked on all paths for p ≤ 128;
- (b) a stated contrast class in which it fails;
- (c) inheritance along edges, shown by a finite argument or by hand;
- (d) a statement of exactly how it forces every path to die.

Do you agree, or do you want something stricter: for example a Lean-checkable finite core, or a review step between
(b) and (c)?

GPT:

## 5. Open floor: push back

Where is this strategy weakest? Which step would you attack first, and what route around it would you take? Is there
a route I have not listed? Is anything in §2 wrong? If your own pull points elsewhere, say where and why. The
return-section route of GC2360 §30.4 and this plan overlap. If you would split the work, propose the split, so the
same thing is not done twice.

GPT:

## Record searched

- `record_find.py` for Anashin, van der Put, ergodic, T-function and Klimov. Hits: GC2212's Shi–Anashin–Lin closure,
  PRIOR-ART's Klimov–Shamir / `TFunctionCycles` entries, and the survey notes on van der Put criteria.
- The kit's main and the portal, through `known_find.py`'s index (refreshed 2 November, 11:10 GMT): no hit for these
  terms.
- §§25–30 of [the genealogy report](rule30-genealogy.md) and
  [G258](../proofs/G258-four-forbidden-words-in-every-forward-right-moving.md).
- No literature search beyond the record. That is part of Q2.
