# Co-discovered proofs: results from openai/math, checked before import

OpenAI's [openai/math](https://github.com/openai/math) release (Apache-2.0; read here at commit `adc7f12` of
2026-10-06) holds 722 preprints in 372 families, written by an unreleased internal model, with a Lean 4 library
for part of them. Its README warns that results without a formalisation "could have issues". This document is the
owner's request of 2026-10-07: bring in "cutting edge formula that may or may not be relevant to our project", as
the formula and what it does, briefly, so that the workers can read it into their context. The owner then set the
gate: "only importing formula that you can peer review and replicate", and the pace: "Import the easy ones now,
chew on the hard ones later."

**The gate.** Nothing here is taken on the release's word. A family is imported only at one of two levels, and its
entry says which:

- **A, proof checked.** Cloud read the whole proof, found it correct, and re-derived every step that can be
  computed with a script written without the release's code.
- **B, finite core replicated.** Cloud's own code reproduces the claim's explicit object, its exceptional cases or
  its small instances; the general proof has not been reviewed. A level-B formula is true where it was checked and
  claimed beyond.

Each entry gives the statement, what it does in a line, how it was checked, and where it might touch our work. The
scripts are in `tests/probes/openai_math/`; their predictions were pushed before they ran (commit `a457f78`).
Where the release says a Lean formalisation exists, the entry says so; Cloud has not compiled the Lean library
(that needs the toolchain and a mathlib build, and is the first of the hard ones).

**Imported so far (2026-10-07): 9 entries from 8 of the 372 families, 6 at level A and 3 at level B.** Batch 1 was
088, 049, 205, 189 and 119; batch 2 is 049b, 186, 175 and 235.

| Family | Result | Level | Script |
|---|---|---|---|
| 088 | A product of simplices beats the simplex for projection-body volume | A | `om088_projection_body.py` |
| 049 | A polynomial whose zero set is flat 3-space but which is not a coordinate | A | `om049_noncoordinate.py` |
| 049b | A degree-5 stable coordinate that is not a coordinate; every fibre flat | A | `om049b_stable_coordinate.py` |
| 186 | Symmetric properties: influence at least $(\log n)^{r/(r-1)}$ times the variance | A | `om186_influence.py` |
| 175 | Discrete convexity: $2^{75}$ unions leave only a $p$-small family | A | `om175_discrete_convexity.py` |
| 235 | Random 3-SAT's hitting time has variance $\Theta(n)$ (upper bound read in full) | A | `om235_sat_variance.py` |
| 205 | An irreducible of $S_n$ whose tensor square holds all, for $n \ne 2, 4, 9$ | B | `om205_tensor_squares.py` |
| 189 | Cycle–clique Ramsey numbers, $R(C_m, K_n) = (m-1)(n-1)+1$ | B | `om189_cycle_clique.py` |
| 119 | No Boolean function tells more about noisy bits than one bit (Courtade, Kumar) | B | `om119_courtade_kumar.py` |

---

## 088. A product of simplices beats the simplex (level A)

*Preprint:* "A product counterexample to the simplex maximum for projection-body volume", 2026-09-24. Lean: the
release lists a formalisation of the dimension-20 counterexample.

**Statement.** The projection body $\Pi K$ of a convex body $K \subset \mathbb{R}^d$ has as support function the
shadow volumes, $h_{\Pi K}(u) = \mathrm{vol}_{d-1}(\mathrm{proj}_{u^\perp} K)$ for unit $u$. For a polytope with
facet areas $s_F$ and outward unit normals $\nu_F$ (Cauchy's formula),

```math
h_{\Pi P}(u) = \tfrac12 \sum_F s_F \, |\langle \nu_F, u \rangle|, \qquad
\Pi P = \sum_F \left[ -\tfrac12 s_F \nu_F, \ \tfrac12 s_F \nu_F \right],
```

a sum of segments (a zonotope). Put $R_d(K) = |\Pi K| / |K|^{d-1}$, which is affine-invariant. Then

```math
\Pi(A \times B) = (|B|\,\Pi A) \times (|A|\,\Pi B), \qquad R_{r+s}(A \times B) = R_r(A)\, R_s(B),
\qquad R_d(T_d) = c_d = \frac{(d+1)\,d^d}{d!}.
```

So for the product of two 10-simplices,

```math
\frac{R_{20}(T_{10} \times T_{10})}{c_{20}} = \frac{121 \binom{20}{10}}{21 \cdot 2^{20}}
= \frac{5588869}{5505024} \approx 1.0152 > 1.
```

Brannen's 1996 conjecture that simplices maximise $R_d$ fails in dimension 20. The general test is

```math
\frac{R_{r+s}(T_r \times T_s)}{c_{r+s}} = \frac{(r+1)(s+1)}{r+s+1} \binom{r+s}{r} \frac{r^r s^s}{(r+s)^{r+s}}.
```

(Feng, Hu, Liu and Xu had counterexamples in every dimension from 9 by another route; this one is exact and
elementary. The preprint also shows the excess grows exponentially with dimension.)

**What it does.** It makes a volume functional multiplicative over products. Any conjectured extremal value that
grows more slowly than multiplicatively is then refuted by a product of its own extremisers.

**How it was checked.** Cloud read the five-page proof: the facet formula, the facets of a product, affine
covariance, the simplex as a cube plus one segment, and the arithmetic. It is correct. The script checks Cauchy's
formula against shadows computed directly as convex hulls, the tetrahedron in $\mathbb{R}^3$ and $T_2 \times T_2$ in
$\mathbb{R}^4$ (largest discrepancy $7 \times 10^{-15}$). It finds the facets of $T_r \times T_s$ by brute force
from the vertices. It computes $|\Pi T_d|$ for $d \le 14$, and every product with $r, s \le 6$, from the general
zonotope volume formula (the sum of $|\det|$ over $d$-subsets of generators) rather than the preprint's argument.
It also checks the final and corollary arithmetic. The first equal split that beats the simplex is $r = s = 10$,
as predicted.

**For us.** Not about Rule 30 or Collatz. It is a clean model of a multiplicativity test: compute one value on a
product, and a conjecture falls.

---

## 049. A flat 3-space that cannot be straightened (level A)

*Preprint:* "An explicit noncoordinate polynomial with affine three-space zero fibre", 2026-09-24. Lean: the
release lists a formalisation for every dimension $n \ge 4$.

**Statement.** In $R = \mathbb{C}[h,u,v,w]$ put

```math
x = u^3 + hv, \quad y = -u^2 + hw, \quad s = 2u^3v + 3u^4w + h(v^2 - 3u^2w^2) + h^2w^3
\quad (\text{so } x^2 + y^3 = hs),
```
```math
p = -2s^2x + 3sy^2 - 3s^3y, \qquad F = h - p - 1 \quad (\text{degree } 17,\ 69 \text{ terms}).
```

Then $R/(F) \cong \mathbb{C}[X,Y,T]$: the zero set of $F$ is a flat 3-space, with coordinates

```math
X = x + s^3, \quad Y = y - s^2, \quad T = \alpha u + \beta(v + uw), \qquad
\alpha = 1 + 2s^2x + 4s^5, \quad \beta = (3s^3 - 3sy)(1 + 2s^2x) - 4s^4y^2,
```

and an explicit polynomial inverse. Yet the gradient of $F$ vanishes at $P = (2, 0, -\tfrac12, \tfrac12)$. A
coordinate (the first component of a polynomial automorphism of $\mathbb{C}^4$) never has a zero gradient, because
the automorphism's Jacobian is invertible everywhere, so $F$ is not one. This is a counterexample to the
Abhyankar–Sathaye embedding conjecture for $\mathbb{C}^3 \subset \mathbb{C}^4$, and, by adding variables, in every
dimension from 4. The case $\mathbb{C}^2 \subset \mathbb{C}^3$ is not addressed. The whole obstruction is one
identity:

```math
X^2 + Y^3 = s\,(1 + F),
```

so the fibre $F = -1$ lies over the cusp $X^2 + Y^3 = 0$ and carries the critical point. The engine is a lifting
lemma: if $x^2 + y^3 = hs$ in a ring $B$ and $h$, $y$ generate the unit ideal, then
$B[U,V,W]/(U^3 + hV - x,\ -U^2 + hW - y,\ S(h,U,V,W) - s) \cong B[T]$.

**What it does.** It certifies that a hypersurface is flat space by writing down coordinates both ways, and shows
it cannot be straightened by one critical point on a different fibre.

**How it was checked.** Cloud read the proof (one lemma, three pages): correct. The script checks, as exact integer
polynomial identities, all ten identities the proof rests on: the cusp relation, the shift, the unit-ideal
certificate $\alpha h + \beta y - 1 = (1 + 2s^2x)(h - 1 - p) - 4s^4(x^2 + y^3 - sh)$, the lemma's substitution and
compatibility, its inverse pair, the ambient identity, and $F(P) = -1$ with $\nabla F(P) = 0$ exactly. The maps
round-trip at 12 random rational points of $\mathbb{C}^3$ and at 300 random points of the zero set over the field
with 1009 elements.
*Unexpected check:* over $\mathbb{F}_p$, $p = 3$ to 13, every fibre $F = c$ has exactly $p^3$ points, the critical
fibre included. Cloud's even-odds guess, written before the run, that the critical fibre would differ was wrong.
Point counting does not see this obstruction.

**For us.** The pattern of a certificate by explicit inverse, then an obstruction from one critical point, is the
kind of finite evidence our proofs aim for. The point counts are a caution for counting arguments such as the
Collatz counting form: two objects can agree on every count mod $p$ and still differ.

---

## 049b. A degree-5 stable coordinate that is not a coordinate (level A)

*Preprint:* "A stable coordinate that is not a coordinate in four variables", 2026-10-05, the second paper of family
049. Lean: the release's family 049 note lists the noncoordinate statement in every dimension from 4, and a companion
on commuting derivations.

**Statement.** In $R = \mathbb{C}[x_1, x_2, x_3, x_4]$ put

```math
Q = x_2^2 - x_4^2 + x_1x_3, \qquad f = x_1 - 2Q\big(Q(x_2 + x_4) + x_1x_4\big)
\quad (\text{degree } 5,\ 16 \text{ terms}).
```

Some automorphism of $R[w]$ sends $f$ to $x_1$, so $f$ is a *stable* coordinate. No automorphism of $R$ does, so it is
not a coordinate. Every fibre $f = c$ is affine 3-space, and no fibre's embedding in $\mathbb{C}^4$ can be
straightened. This disproves the stable coordinate conjecture in four variables (it holds in two and three), and
it is a second, stronger counterexample to Abhyankar–Sathaye, with every fibre flat rather than just one.

**How it works.** Write the same polynomial ring as $A = k[p,s,u,F,J]/(H)$, with $x = s^2 - u^2 + pF$ and
$H = x^2F - (1 + 2sx)J - pJ^2 - u$. A unimodular matrix change keeps $x = -\det M$ and makes $H$ linear in a new
coordinate, so $A \cong R$ with $p \mapsto f$. Since $xy - z(z+1) = p(H + u)$ for $y = s + x(x + u^2)$ and
$z = sx + pJ$, the derivation $\Delta = -p\,\partial/\partial u$ in coordinates $(p, x, y, z, u)$ preserves the
polynomial ring and sends $H$ to $p$. So $\exp(w\Delta)$ turns $H$ into $H + pw$, and one more substitution
eliminates a variable: that is the stable coordinate. For the obstruction, weight $p, s, u, F, J$ by
$-1, 0, 0, 1, 1$. The associated graded ring is $B[\tau, I/\tau]$ over the quadric $B = k[x,y,z,u]/(xy - z(z+1))$,
an affine modification. A coordinate would give a nonzero locally nilpotent derivation of $B$ with an invariant in
$I$. Pulled back to $\mathrm{SL}_2/\text{torus} \times \mathbb{A}^1$, that is $k[a,d,b,c,u]/(ac - bd - 1)$, the
ideal $I$ becomes principal, generated by $v = a^3b + a^2u^2 - d^2$. A second grading isolates
$a^2u^2 - d^2 = (au - d)(au + d)$, forces $a$, $d$ and $u$ to be invariants, and leaves a coefficient of fibre
weight $-2$ in $k[a, d, u]$, where every weight is at least 0.

**What it does.** It is a complete toolkit for showing that an explicit polynomial is not a coordinate. Degenerate
to a graded ring, push a hypothetical derivation down to a quadric, lift it to a line bundle, and find a weight
contradiction.

**How it was checked.** Cloud read the five sections and checked each step by hand, with these points verified
explicitly: the separation of the filtration, the domain property of the graded ring, the passage of the derivation
to the graded ring at negative weights, the chart formulas, the local principalisation at primes containing $a$,
the lifting lemma, and the final weight count. It is correct. The script checks every identity (S1 to S4 and S6
above), then builds the composite automorphism $\theta$ of 5-space from the formulas and tests it and its inverse
at 16 random rational points, with first coordinate equal to $f$. Every fibre has exactly $l^3$ points over
$\mathbb{F}_l$ for $l = 3$ to 11. The nilpotency orders of $\Delta$ on $p, s, u, F, J$ are 1, 3, 2, 5, 3.
*Unexpected check:* the Jacobian determinant of $\theta$, computed exactly with dual numbers, is 1 at every point
tried, as Cloud guessed (about 60% confident) before the run.

**For us.** Of the batch, this is the clearest example of a technique beating a famous conjecture with explicit
algebra. Its "weight contradiction after a degeneration" is a general way to prove that something does not exist.

---

## 205. Universal tensor squares for the symmetric groups (level B)

*Preprints:* "Universal Tensor Squares for Symmetric Groups" and "A Cyclic Polytabloid Proof of Saxl's
Conjecture", 2026-09-24. Lean: the release lists formalisations of both.

**Statement.** The Kronecker coefficient $g(\lambda, \mu, \nu)$, the multiplicity of the irreducible $\nu$ in
$\lambda \otimes \mu$, is

```math
g(\lambda,\mu,\nu) = \sum_{\rho \vdash n} \frac{\chi^\lambda(\rho)\,\chi^\mu(\rho)\,\chi^\nu(\rho)}{z_\rho},
\qquad z_\rho = \prod_i i^{m_i}\, m_i!,
```

where $m_i$ counts the parts of $\rho$ equal to $i$. For every $n \notin \{2, 4, 9\}$ there is $\lambda \vdash n$
with $g(\lambda, \lambda, \nu) > 0$ for every $\nu \vdash n$: one irreducible whose tensor square holds every
irreducible (the tensor square conjecture). Saxl's conjecture, the companion's theorem, is that the staircase
$(m, m-1, \ldots, 1)$ is such a $\lambda$ for $n = m(m+1)/2$. Any such $\lambda$ equals its transpose, since
$g(\lambda, \lambda, 1^n) = 1$ exactly when $\lambda = \lambda'$.

**What it does.** It names one representation that generates all the others in one tensor square.

**How it was checked.** By Cloud's own character tables (the Murnaghan–Nakayama rule) for every $n \le 24$: the
$n$ with no universal $\lambda$ are exactly 2, 4 and 9; the staircase is universal for $m \le 6$; every universal
$\lambda$ is self-conjugate (tested on every $\lambda$ to $n = 12$). Controls: column orthogonality of every table,
and $g(\lambda, \lambda, (n)) = 1$. The general proof (recurrences, pruning, and the release's own search to
$n = 64$) is not reviewed. Examples: 311 at $n = 5$, 321 at $n = 6$, 4111 at $n = 7$, 4321 at $n = 10$.

**For us.** Not related. It is a well-checked formula for Kronecker coefficients, if one is ever needed.

---

## 189. Cycle–clique Ramsey numbers (level B)

*Preprint:* "Cycle–clique Ramsey numbers", 2026-09-25. Lean: the release lists a formalisation of the full range.

**Statement.** For all $m \ge n \ge 3$ except $(3, 3)$,

```math
R(C_m, K_n) = (m-1)(n-1) + 1, \qquad R(C_3, K_3) = 6,
```

the least $N$ such that every red–blue colouring of the complete graph on $N$ vertices has a red $m$-cycle or a
blue $n$-clique (the Erdős–Faudree–Rousseau–Schelp conjecture). The lower bound is $n - 1$ disjoint red cliques
of $m - 1$ vertices, all blue between them.

**What it does.** It gives the exact threshold at which a long red cycle or a large blue clique is forced.

**How it was checked.** Cloud's own SAT encoding (a variable per edge, a clause against every red $m$-cycle and
every blue $n$-set), solved with Glucose through python-sat. At $N - 1$ vertices the solver must find a colouring,
which is re-checked without it; at $N$ it must find none. The construction is checked directly. The plain
encoding settles $(3,3)$ (the pentagon at 5 vertices, none at 6), $(4,3)$, $(5,3)$, $(6,3)$, $(7,3)$ and $(4,4)$
within 20 seconds each. The larger cases ran for many minutes, so a second encoding was added after the first run:
split by the largest red degree $D$ (relabel so that vertex 0 has degree $D$ and neighbours $1, \ldots, D$, and bound
every degree by $D$). Its control is to find a colouring one vertex below the threshold, and it agrees with the plain
encoding on $(7,3)$. It settles $(5,4)$ at 13 vertices and $(6,4)$ at 16 in seconds per degree. So 8 of the 9 cases
agree with the formula and none disagree. $(5,5)$ at 17 vertices is still running at the time of writing; its
first degree, $D = 4$, is the hard one. The general proof is not reviewed.

**For us.** Not related, beyond being an exact extremal threshold settled by a finite search plus a proof.

---

## 119. The most informative Boolean function (Courtade–Kumar, level B)

*Preprint:* "Sharp binary information contraction on the discrete cube", 2026-09-24. Lean: the release lists a
formalisation of the inequality and its equality case.

**Statement.** Let $X$ be uniform on $\{0,1\}^n$ and $Y$ be $X$ with each bit flipped independently with
probability $a$. For every Boolean $f$,

```math
I\big(f(X);\, Y\big) \le 1 - h(a), \qquad h(a) = -a \log_2 a - (1-a) \log_2 (1-a),
```

with equality for a dictator $f(x) = x_i$ or its complement. This was conjectured by Courtade and Kumar in 2014.

**What it does.** It bounds what one yes/no answer about some bits can tell you about a noisy copy of them: no
cleverer function beats copying one bit.

**How it was checked.** Every Boolean function of $n \le 4$ bits (65,536 at $n = 4$) at seven noise levels
$a = 0.01$ to $0.45$. The maximum equals $1 - h(a)$ to within $4 \times 10^{-16}$ and is attained only by the
dictators and their complements, as predicted. *Unexpected check:* the best non-dictator at $n = 4$ is a
near-dictator (a dictator with a few values changed), reaching 97% of the bound at $a = 0.01$ and 83% at
$a = 0.45$. Small cases were checked numerically in the literature before, so this is replication, not news. The
general proof (long and analytic) is not reviewed.

**For us.** The closest of this batch to Rule 30. The centre column is a Boolean function of the initial row; with
the inputs seen through noise, no readout of it carries more than one bit's worth of information about them. That
is a ceiling of the kind our information-growth probes measure against.

---

## 186. Symmetry forces influence: a uniform bound for hypergraph properties (level A)

*Preprint:* "A uniform influence bound for hypergraph properties", 2026-10-05; its companion, "A Sharp Threshold
Bound for Monotone Graph Properties", proves the graph case with explicit constants. Lean: the release lists a
formalisation for the family.

**Statement.** Let $f$ be a Boolean function of the $\binom{n}{r}$ edge bits of an $r$-uniform hypergraph that is
invariant under relabelling the $n$ vertices (a *hypergraph property*; no monotonicity needed). Give each edge
probability $p$, and let $I_p(f) = \sum_e \Pr(\text{flipping } e \text{ changes } f)$. For $r \ge 3$,

```math
\mathrm{Var}_p(f) \le \frac{C_r}{(\log n)^{r/(r-1)}}\, I_p(f) \quad \text{for every } 0 < p < 1, \qquad
p_{1-\varepsilon} - p_\varepsilon \le \frac{2C_r}{(\log n)^{r/(r-1)}} \log\frac{1-\varepsilon}{\varepsilon}
```

for increasing properties. The second inequality is Friedgut and Kalai's 1996 conjecture on threshold widths for
hypergraph properties. The companion proves the graph case,
$p_{1-\varepsilon} - p_\varepsilon \le 2^{19} (\log n)^{-2} \log(1/2\varepsilon)$.

**How it works, in four steps.**
1. *Low degree from small influences.* A two-to-four bound, $\|T_\rho g\|_4 \le \|g\|_2$ with
   $\rho = \sigma/4$ and $\sigma = \sqrt{p(1-p)}$, valid at every bias. If every single influence is at most
   $I/m$, then the Fourier mass of degrees 1 to $k = \sigma \log m / 64$ is at most $m^{-1/4} I$.
2. *Restriction to a random block.* Fix every edge outside a random block $B$ of $m \approx \sqrt n$ vertices. The
   function left over is still symmetric under all permutations of $B$, so every free edge's orbit has at least $m$
   members, and step 1 applies to it.
3. *Capture.* A support of $s \le (k/r)^{r/(r-1)}$ edges has a vertex of degree between 1 and
   $r s^{(r-1)/r} \le k$. With probability at least $m/(2n)$ the block meets the support only there. The two factors
   of $m/n$ cancel, so the low Fourier mass up to that size is at most $2r m^{-1/4} I$.
4. *High degree.* The weighted Parseval identity $\sum_S |S| \hat f(S)^2 = \sigma^2 I_p(f)$ bounds the rest by
   $\sigma^2 I / L$. The bias cancels as $\sigma^{2 - r/(r-1)}$, a positive power, which is why the bound is
   uniform in $p$.

**What it does.** It turns symmetry into a lower bound on total influence. A symmetric Boolean function that is
not nearly constant must be sensitive to many coordinates, by a power of $\log n$ that depends on how big the
symmetry group's orbits are.

**How it was checked.** Cloud read the whole proof: correct. The script checks, by Cloud's own code: the
one-coordinate fourth-moment bound behind step 1, exactly on a grid; the two-to-four bound on random functions of up
to 6 bits (worst ratio 0.9994); the weighted Parseval identity, exactly; the degree lemma on all $2^{20}$ 3-uniform
hypergraphs on 6 vertices; the capture probability by exact counting; and Margulis–Russo, $q'(p) = I_p(f)$, on all
168 monotone functions of 4 bits.
*Unexpected check:* the proof's constant hides a threshold $N_r$ beyond which its four conditions hold. Cloud
computed it: about $n = 9 \times 10^{19}$ for $r = 3$ ($\log N_3 \approx 46$, inside the guessed 40 to 60), giving
an explicit $C_3 \approx 1.4 \times 10^4$; then $C_4 \approx 7.0 \times 10^3$, $C_5 \approx 5.4 \times 10^3$,
$C_6 \approx 4.7 \times 10^3$. The step-1 cutoff $k = \sigma \log m / 64$ is below 1 until $m > e^{128}$. So with
these constants the bound beats the trivial $\mathrm{Var} \le I/4$ only for astronomically large $n$: it is a
qualitative tool, not a numerical one.

Cloud also read the graph companion in full. Its Fourier lemma is the same, and its capture step uses the fact that
an $s$-edge graph has a vertex of degree at most $\sqrt{2s}$. For every graph property, every $p$ and every
$n \ge 2$ it gives $\mathrm{Var}_p(f) \le 2^{17} I_p(f)/(\log n)^2$ and the width bound with $2^{19}$; the
constants are checked in F7 (added after the first run). So $r = 2$ is covered, and Cloud's earlier tentative
reading, that the argument goes through there with bias factor $\sigma^0$, is what the companion does. Even with
explicit constants the width bound is below 1 only once $(\log n)^2 > 2^{19}\log(1/2\varepsilon)$, about
$n > e^{600}$ at $\varepsilon = 1/4$.

**For us.** The nearest tool yet to Rule 30. Our influence probes ask how much one initial cell can change a later
cell. This theorem says symmetry alone forces the total influence up, and the method (restrict to a block, keep its
symmetry, cancel the two $m/n$ factors) is the kind of argument a shift-invariant automaton might allow. The
two-to-four bound at every bias, with its explicit $\rho = \sigma/4$, is usable on its own.

---

## 175. Talagrand's discrete convexity: 2^75 unions suffice (level A)

*Preprint:* "Talagrand's discrete-convexity conjecture", 2026-09-23. Lean: the release lists a formalisation for
the family.

**Statement.** Let $\mu_p$ be the product measure on subsets of $[N]$, each element present with probability $p$.
For a family $\mathcal D$, let $E_k(\mathcal D)$ be the sets contained in no union of $k$ members of $\mathcal D$.
Call a family *$p$-small* if a family $\mathcal G$ with $\sum_{I \in \mathcal G} p^{|I|} \le 1/2$ has a member
inside each of its sets (a union-bound certificate that it has measure at most 1/2). Then, with $k = 2^{75}$, for
every $N$, every $p$ and every family $\mathcal D$, monotone or not,

```math
\mu_p(\mathcal D) \ge 1 - \frac1k \quad \Longrightarrow \quad E_k(\mathcal D) \text{ is } p\text{-small}.
```

This is Talagrand's 2010 conjecture (his Research Problem 13.3.2 in the 2021 book). For a positive selector process
$\phi(S) = \sup_{t \in T} \sum_{i \in S} t_i$ it gives an explicit certificate:
$\{S : \phi(S) \ge k^2\, \mathbb{E}\phi\}$ is $p$-small (Park and Pham proved this by other means).

**How it works.** The key quantities are signed weights,

```math
b(U) = (1-q)^{|U|} \sum_{z \in \{0,1\}^U} (-1)^{\sum z}\, \mathbb{E}\big[f(z, Y)\big], \qquad
\sum_{U} q^{|U|}\, b(U)^2 \le \mu_q(\mathcal F) \le 1,
```

where $f$ is the indicator of $\mathcal F$ and $Y$ is Bernoulli-$q$ off $U$. The weight bound is Parseval in the
biased Fourier basis, since $\hat f(U) = (q/(1-q))^{|U|/2} b(U)$. A signed measure on 32-row arrays, which
vanishes on any column that is all zeros, gives for every exceptional $S \in E_{32}(\mathcal F)$

```math
\sum_{U \subseteq S} (-1)^{|U|}\, b(U)^{32} = 0, \qquad\text{so}\qquad
\sum_{\varnothing \ne U \subseteq S} b(U)^{32} \ge b(\varnothing)^{32} = \mu_q(\mathcal F)^{32} \ge 2^{-32}.
```

Sets with large weight are cheap generators. The rest are binned by size and weight, and an elementary covering
lemma (select subsets of high weighted degree, sample unions of pairs, add the residual tuples) covers every set
that contains too many members of one bin. The bins' sixteenth powers then fall short of $2^{-32}$. That covers
$E_{32}(\mathcal F)$ at density $q/2^{70}$. A coupling of $2^{70}$ dependent rows, each exactly $\mu_p$, whose union
is $\mu_{2^{70}p}$ (or everything), returns the density to $p$.

**What it does.** It turns "a family is very likely" into "a few of its members' unions cover everything except an
explicitly cheap exceptional family", with an explicit constant, for arbitrary families.

**How it was checked.** Cloud read the proof, about 16,000 characters: correct, constants included. The script
checks, with Cloud's own code: the signed identity, exactly, with 2 rows (Li's kernel) and with 32 rows, on 2,217
exceptional pairs of family and set each; the weight bound and $b(\varnothing) = \mu_q$; both couplings' laws,
exactly; and every constant ($6/(2^{64}-1) < 1/4$, $16/(15(2^{256}-1)) < 2^{-32}$, the lemma's
$4h + 13rh + 1 \le 2^{4h}$). Control: off the exceptional sets the signed sum is nonzero for 99% of pairs, so the
identity is not checking nothing. Cloud's loose guess that this share would be at least 90% was right. One change was
made after the first run, and the script says so: half of the random families now avoid some coordinates, because
purely random families gave only 26 exceptional pairs. The preprint's two-union corollary rests on outside results
and is not imported.

**For us.** A clean example of the "signed measure that vanishes on the forbidden configuration" technique. A
pointwise-zero product, expanded, becomes an identity among Fourier-type weights. Rule 30's forbidden patterns might
be attacked the same way.

---

## 235. Random 3-SAT becomes unsatisfiable within a window of width $\Theta(\sqrt n)$ (level A for the upper bound)

*Preprint:* "Linear Variance of the Random 3-SAT Hitting Time", 2026-10-05 (the family also holds the general-$k$
companion, and Carenini's result settling the threshold's existence is credited there). Lean: the release lists a
formalisation for the family.

**Statement.** Add independent uniform proper 3-clauses on $n$ variables, and let $H_n$ be the first index at
which the formula is unsatisfiable. Then

```math
c\,n \le \mathrm{Var}(H_n) \le C\,n, \qquad r_n(\eta) - r_n(1 - \eta) = \Theta_\eta(\sqrt n),
```

where $r_n(\eta)$ is the first clause count at which the formula is satisfiable with probability at most $\eta$.
The upper bound is new (the previous bound was $O(n \log n)$). The lower bound is Wilson's 2002 window theorem,
cited, not reproved.

**How it works.** Let $q_j(S)$ be the probability that $j$ random 2-clauses leave no assignment of a set $S$ alive,
and let $P_d(S) = \sum_{j<d} q_j(S) \le d$. The key inequality is that a potential's drift controls a power of a
killing probability:

```math
\mathbf 1_{S \ne \varnothing}\, q_d(S)^{3/2}
\le d^{1/2}\Big(3\,\mathbb{E}_C\big[P_d(S[C]) - P_d(S)\big] + d\,u^{-3}\Big),
```

which rests on the one-clause comparison $h_2(S)^{3/2} \le 3h_3(S) + u^{-3}$ (only frozen coordinates can kill).
Efron–Stein by omitting one clause bounds the variance by $\sum_i \mathbb{E} D_i^2$, where $D_i$ is the delay. If
the omitted clause is pivotal, flipping any of its three variables must be blocked by its "test" clauses. These are
three independent kill events, worth $p^3$, against a remaining duration of $O(d^{3/2} p^{-3/2})$ from the
potential, and $3 - 3/2 = 3/2$ leaves a bounded square. Collisions (clauses meeting two of the three variables) are
rare enough to average out.

**What it does.** It pins the width of the satisfiability transition to the square root of the number of variables:
not sharper, not wider.

**How it was checked.** Cloud read the whole upper-bound proof, constants included ($K = 7$, the moment bounds, the
tail constant 120 and $2(7/8)^{10} < 1$): correct. The script checks the one-clause comparison exactly for every
$b \le u \le 300$, and the drift inequality exactly on random assignment sets of 3 and 4 variables, by dynamic
programming over surviving sets (control: it reproduces $q_1 = h_2$). It also checks the tail constants.
*Simulation, not proof, and a missed prediction:* $\mathbb{E}H_n/n$ falls toward the threshold from above (4.71,
4.48, 4.33, 4.28 at $n = 20, 40, 80, 160$), as predicted. But $\mathrm{Var}(H_n)/n$ fell from 11.7 to 3.8, a factor
of 3.1, against the prediction that it would stay within a factor of 2. That does not contradict the theorem, whose
upper bound allows a falling ratio, but Wilson's lower bound needs it to level off eventually. A repeat at $n = 160$ gave 3.87; a post-hoc run at
$n = 320$ is in progress. Cloud's loose guess that the ratio would lie between 1 and 30 held.

**For us.** We use SAT solvers. Here the transition from "almost surely satisfiable" to "almost surely not" for
random 3-SAT takes about $\sqrt n$ clauses, which is useful when sizing random-instance controls. The potential
$P_d$ (a bounded, monotone function whose drift pays for a power of a kill probability) is a reusable device.

---

## Not imported yet: the hard ones

Most families are long proofs in analysis, geometry, number theory or topology. They need a full read, and many
have no finite core to replicate. Some that looked finite at first sight, and why they wait:

- **161, Sidorenko's conjecture fails.** The 35-vertex pattern is explicit: the incidence graph of 22 triples on 13
  points, each pair of points in exactly two triples. The host graph exists only in a limit (a large prime $q$ and a
  small $\varepsilon$), so there is nothing finite to evaluate yet.
- **162, Ryser's conjecture fails.** The constructions are for every sufficiently large prime, by probabilistic
  deletion.
- **132, sensitivity versus block sensitivity, and 192, the square-root degree bound.** The functions are explicit,
  but on astronomically many bits; 192's construction has no bound on its size at all.
- **156, Borsuk fails in dimension 9, and 158, the plane is not 5-colourable.** Both are continuous objects (all
  rank-one projectors of $\mathbb{R}^4$; arbitrary colour classes) with topological or analytic proofs.
- **The Lean route.** The release's Lean 4 library (`lean/`) and its ComparatorChallenges state the formalised
  results. Compiling them here needs the Lean toolchain and a mathlib build, which is the next step for every
  family the release says is formalised.

The catalogue itself is `CONTENTS.md` in the release. A family enters this document only through the gate above.
