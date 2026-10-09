# Older and adjacent-field tools (about 1984 to 2015) bearing on an eventually periodic column of Rule 30

Scope: under-cited results on directional dynamics and entropy, Lyapunov exponents, permutive and expansive CA, columns
of linear CA and automaticity, and 2-adic analogues, each checked against PRIOR-ART.md first. Rule 30 throughout is
x'(i) = x(i-1) XOR (x(i) OR x(i+1)): neighbourhood [-1, 1], permutive in the left variable only, nonlinear.

Reading levels: **[FULL]** full text read (by text extraction); **[PART]** named sections read; **[ABS]** abstract
only; **[SEC]** secondary account (search summary, slides or a citing paper); **[BIB]** bibliographic record only.
**[OWN]** is this survey's own derivation, checked by a short Python computation (not committed). OWN items are not
literature and appear only under Inferences.

Already in PRIOR-ART.md (re-listed only where something new was found): Milnor 1988 (Example 6.2), Shereshevsky
1992 (paper and thesis), Tisseur 2000 (abstract only until now), Courbage and Kaminski 2006 (Lyapunov exponents),
Kurka (column subshifts), Kopra 2023 and arXiv:2005.05112, Kari and Kopra, Jen 1986 and 1990, Rowland 2006, Rowland
and Yassawi (arXiv:1209.6008), FLP 1995, Mahler, Allouche and Shallit (Rudin-Shapiro, the book), Boyle and Lee 2006,
Pivato (bipermutative measure rigidity). Not in PRIOR-ART.md (grep on surname and a title word): Sablik, Coven,
Coven-Pivato-Yassawi, Blanchard-Maass, Bressaud, Litow, Dumas, Christol, Berthe, Boyle-Lind, Anashin, Klimov,
D'Amico-Manzini-Margara, Park, Akin. PRIOR-ART.md has "Lind" only as Lind and Marcus.

**Ranked short list of finds** (detail in the sections below):
1. **Coven, Pivato and Yassawi 2007** (odometers). Applied to Rule 30 in the frame that moves with its right edge,
   it gives: the single seed's orbit closure is conjugate to the 2-adic odometer. This is a rigid arithmetic
   structure theorem for Rule 30's chaotic side. It has not been applied to Rule 30 in the record.
2. **Sablik 2008** (directional dynamics). For a left-permutive CA, the vertical lies in the open cone of
   left-expansive slopes. Together with the fact that Rule 30 is not right-closing (checked here), Rule 30 has *no*
   right-expansive and no expansive slope at all. This is the dynamical-systems name for "the column codes the left
   side but not the right".
3. **The 2-adic form [OWN]**. Rule 30 is a T-function (1-Lipschitz map) on the 2-adic integers in either edge frame.
   In the right-edge frame it is an invertible T-function, computed by a 3-state Mealy automaton. The centre column
   is the diagonal bit t of f^t(1). This opens Anashin's p-adic ergodic theory and the automaton-group toolbox. No
   source stating it was found.
4. **Coven 1980 and Blanchard-Maass 1996**. Rule 30 in its one-sided frame is the complement of the "Coven map" for
   the periodic word 00, just outside Coven's aperiodic hypothesis. That makes Coven's family the nearest calibrated
   siblings.
5. **Litow-Dumas 1993 and Allouche-von Haeseler-Peitgen-Skordev 1996**: the linear case's proof skeleton
   (algebraic series, Christol). It is calibrated here against Rule 30 by the measured odometer depth (about log2 k
   for Rule 90 against about 0.4 k for Rule 30).

## Which results say something about the entropy or expansivity of Rule 30 along the vertical direction (a column), and
do any give a positive lower bound on a column's complexity for finite configurations?

### Takeaway
Along the vertical, Rule 30 is left-expansive, but it has no right-expansive and no expansive direction (Sablik's
cone theorem, plus Rule 30 failing to be right-closing). Its vertical (system) entropy is positive, between log 2 and
2 log 2. No result found gives a positive lower bound for one column of a finite configuration. None can come from
system-level entropy or expansivity alone, because Rule 90 has the maximal vertical entropy and yet its single-seed
centre column is eventually 0.

### Cited Findings
#### Sablik, M., "Directional dynamics for cellular automata: A sensitivity to initial condition approach", Theoret.
Comput. Sci. 400 (2008) 1-18 [PART: sections 1 to 5 read by text extraction; minus signs were lost in the extraction]
- **Definitions.** The tube of slope alpha is D^alpha(x, eps, K) = {y : d(sigma^{floor(n alpha)} F^n(x),
  sigma^{floor(n alpha)} F^n(y)) < eps for all n in K}, with K = N, or K = Z for bijective F. F is "(K, Sigma)-expansive
  of slope alpha" if D^alpha(x, eps, K) = {x} for all x. Expansivity is split into right- and left-expansivity, which
  separate configurations that differ on [0, +inf) or on (-inf, 0] respectively. Expansive means both. —
  [Sablik 2008, author copy](https://www.math.univ-toulouse.fr/~msablik/article/2008-TCS.pdf)
- **Example 3.4 ("Open cone of expansive directions"):** for neighbourhood U = [r, s], "If (A^Z, F) is
  left-permutative, then Bl_N(A^Z, F) = (-inf, -r[. If ... right-permutative, then Br_N(A^Z, F) = ]-s, +inf). Thus, if
  ... bipermutative, then B_N(A^Z, F) = ]-s, -r[." The signs were reconstructed from the garbled extraction. They are
  consistent with Example 3.2 (the shift sigma^alpha has its unique equicontinuous direction at -alpha) and with
  bipermutative Rule 90 being positively expansive at slope 0. — [Sablik
  2008](https://www.math.univ-toulouse.fr/~msablik/article/2008-TCS.pdf)
- **Theorem 5.2:** for an infinite transitive subshift Sigma, the right-expansive set is an interval ]alpha', +inf)
  inside ]-s, +inf), the left-expansive set is an interval (-inf, alpha'') inside (-inf, -r[, and the expansive set is
  ]alpha', alpha''[ inside ]-s, -r[. — [Sablik 2008](https://www.math.univ-toulouse.fr/~msablik/article/2008-TCS.pdf)
- **Remark 5.2:** if Br_N is nonempty then F is right-closing on Sigma. If Bl_N is nonempty then F is left-closing.
  — [Sablik 2008](https://www.math.univ-toulouse.fr/~msablik/article/2008-TCS.pdf)
- Sablik credits the directional idea to Boyle and Lind for Z^d actions, and says the work "most connected" to the
  expansive directions is Nasu's. He leaves open whether the bounds of the cone can be irrational. — [Sablik 2008,
  section 5](https://www.math.univ-toulouse.fr/~msablik/article/2008-TCS.pdf)
- **Corollary 4.4** (the opposite pole): if a CA has a unique N-equicontinuous direction alpha, then
  (sigma^{floor(alpha n)} F^n) is ultimately periodic. Corollary 4.5: N-equicontinuity of a given slope is undecidable.
  — [Sablik 2008](https://www.math.univ-toulouse.fr/~msablik/article/2008-TCS.pdf)
- **Applies to Rule 30:** Rule 30 has r = -1, so Bl_N(Rule 30) contains (-inf, 1), and the vertical alpha = 0 is
  inside the left-expansive cone. That is the directional form of Kopra's left expansivity with dimensions (0, 1, 2),
  which is already in the record. Access: free author PDF. Under-citation evidence: Sablik is absent from
  PRIOR-ART.md. Citation counts were not retrieved.

#### Tisseur, P., "Cellular automata and Lyapunov exponents", Nonlinearity 13 (2000) 1547 (already in PRIOR-ART.md by
abstract; now [FULL] read of the arXiv version)
- It restates Shereshevsky's inequality h_mu(F) <= h_mu(sigma)(lambda+_mu + lambda-_mu). **Theorem 5.1:** for
  sigma-ergodic, F-invariant mu, h_mu(F) <= h_mu(sigma)(I+_mu + I-_mu), with average Lyapunov exponents I+- <=
  lambda+-. **Proposition 5.3:** for any onto CA, h_top(F) <= (lambda+_{mu_u} + lambda-_{mu_u}) log #A.
  **Proposition 5.2:** if F has equicontinuous points, I+- = 0 and h_mu(F) = 0. —
  [arXiv:math/0312136](https://arxiv.org/abs/math/0312136)
- Section 6.1 covers Coven's aperiodic CA (see the next question). **Internal inconsistency, flagged:** the text says
  "Coven proves that the topological entropy of this type of CA is log(2)", and later, for the example with B = 10,
  "From [3] h_top(F) = 2 log(2)". One of these is wrong, or they refer to different maps. —
  [arXiv:math/0312136](https://arxiv.org/abs/math/0312136)

#### Courbage, M. and Kaminski, B., "On the directional entropy of Z^2-actions generated by cellular automata", Studia
Math. 153 (2002) 285-295, doi:10.4064/sm153-3-5 [ABS]
- Abstract: for any CA Z^2-action, the directional entropy h_v, v = (x, y), "is bounded above by max(|z_l|, |z_r|) log
  #A if z_l z_r >= 0 and by |z_r - z_l| in the opposite case, where z_l = x + ly, z_r = x + ry". It continues: "in
  the class of permutative CA-actions the bounds are attained if the measure considered is uniform Bernoulli". — [IMPAN
  abstract
  page](https://impan.pl/en/publishing-house/journals-and-series/studia-mathematica/all/153/3/90935/on-the-directional-entropy-of-bbb-z-2-actions-generated-by-cellular-automata)
- **Applied to Rule 30 at the vertical** v = (0, 1): z_l = -1 and z_r = 1, so the bound is |z_r - z_l| = 2 (log #A is
  missing from the printed second case; presumably 2 log 2). The abstract does not say whether "permutative" means
  bipermutative. The Z^2-action needs invertibility or a natural extension, and Rule 30 is not invertible. Their
  natural-extension technique is mentioned by Akin, per the search summary of
  [arXiv:0802.0953](https://arxiv.org/abs/0802.0953).

#### Other entropy items
- Wolfram, NKS note on entropies: "For rule 30, h_mu tx < 1.155, and there is some evidence that its true value may
  actually be 1" (a spacetime measure entropy, not the topological entropy of the map). — [NKS p. 960
  note](https://wolframscience.com/nksonline/page-960b/)
- D'Amico, Manzini and Margara, "On computing the entropy of cellular automata", TCS 290 (2003) 1629-1646 [ABS via
  search]: a closed formula for linear CA over Z_m and an algorithm for positively expansive CA. Rule 30 is neither. —
  [UniUPO record](https://research.uniupo.it/it/publications/on-computing-the-entropy-of-cellular-automata/)
- Hurd, Kari and Culik, "Topological entropy of cellular automata is uncomputable", ETDS [title only, from search
  results]. —
  [Cambridge](https://www.cambridge.org/core/journals/ergodic-theory-and-dynamical-systems/article/abs/topological-entropy-of-cellular-automata-is-uncomputable/875C89765D6DD8EE17262F298DD8CAB2)
- Bressaud, X. and Tisseur, P., "On a zero speed sensitive cellular automaton", Nonlinearity 20 (2007) 1-19 [ABS]: a
  sensitive CA whose perturbations spread at asymptotically zero speed for almost all configurations, under an
  unusual but natural invariant measure. Zero speed implies zero measure entropy. —
  [arXiv:1206.5924](https://arxiv.org/abs/1206.5924)
- Gage, Laub and McGarry, "Cellular automata: is Rule 30 random?" (2005, Midwest NKS conference) [ABS]: statistical
  tests only, with weaknesses at even window sizes. Not relevant to periodicity. —
  [PDF](https://legacy.cs.indiana.edu/~dgerman/2005midwestNKSconference/dgelbm.pdf)

### Inferences
- **[OWN] Rule 30 is left-closing but not right-closing, so it has no right-expansive slope.** A pair-graph search on
  Rule 30's de Bruijn graph found two distinct left-asymptotic configurations with the same image (right-closing
  fails). It found none for right-asymptotic pairs (left-closing holds, as left-permutivity implies). Unexpected
  check, consistent with this: 0^inf has exactly two preimages (0^inf and 1^inf), while 1^inf has three (the shifts of
  (001)^inf). So the preimage count is not constant, and Rule 30 is not open (Hedlund's characterisation of open
  maps, cited from memory). By Sablik's Remark 5.2, Br_N(Rule 30) is empty, so B_N(Rule 30) is empty: **no slope is
  expansive, and the vertical is one-sidedly expansive only.** Any period-2 proof must get the right side's
  genuineness from somewhere other than expansivity. That matches the project's two-ingredient insight.
- **[OWN] Vertical entropy is positive.** Under the uniform Bernoulli measure the single column (F^t(x)_0)_t of Rule
  30 is i.i.d. fair. F^t(x)_0 depends on x_{[-t, t]} and is permutive in x_{-t}, and no earlier column value depends
  on x_{-t}, so each new value is a fair coin given the past. Hence h_mu(F) >= log 2 and h_top(F) >= log 2.
  Tisseur's Proposition 5.3 with radius 1 gives h_top <= 2 log 2. So Rule 30's vertical directional entropy lies in
  [log 2, 2 log 2]. If Rule 30's leftward Lyapunov exponent is below 1, Tisseur's bound puts h_mu below the
  Courbage-Kaminski value of 2 log 2. That suggests their attainment statement concerns bipermutative rules.
- **No transfer to one finite orbit.** Rule 90 is bipermutative, so it is expansive at slope 0 (Sablik Example 3.4).
  If its vertical entropy attains the Courbage-Kaminski bound, as their sharpness statement suggests, its vertical
  entropy is the maximum. Yet its single-seed centre column is C(2m, m) mod 2 = 1, 0, 0, ... (Lucas and Kummer,
  standard). So expansivity and directional entropy say nothing about a single finite configuration's column. This
  sharpens the record's existing remark (PRIOR-ART.md, column-entropy survey) that these are system quantities.
- Bressaud-Tisseur calibrates the other way: sensitivity alone gives no entropy. Rule 30's positive vertical entropy
  comes from permutivity (the i.i.d. argument), not from chaos in general.

### Gaps
- No value of Rule 30's topological entropy, or of its leftward Lyapunov exponent, was found. Only NKS's bound on a
  spacetime entropy was found.
- The Courbage-Kaminski full text was not read, so "permutative" (one-sided or both) in their sharpness claim is
  unverified.
- Kurka's ETDS 1997 classification (equicontinuous, almost equicontinuous, sensitive, expansive; via
  [arXiv:1001.5471](https://arxiv.org/abs/1001.5471)) was not found applied explicitly to ECA 30 (search only). —
  [Kurka 1997,
  Cambridge](https://www.cambridge.org/core/journals/ergodic-theory-and-dynamical-systems/article/languages-equicontinuity-and-attractors-in-cellular-automata/6ECF8483F6929A38EC4055BEE121E3F3)
- **No source gives a positive lower bound on the complexity of a column of any finite Rule 30 configuration**, as
  the record already found. Citation counts (Google Scholar) were not retrieved for any item, so under-citation
  evidence here is only absence from PRIOR-ART.md and from the Rule 30 papers read.

## Are there theorems that a column of a left-permutive CA from a finite configuration cannot be eventually periodic
under extra hypotheses, which could be strengthened?

### Takeaway
Beyond Jen 1990 and Kopra 2023 (in the record), no further non-periodicity theorem was found. The strongest
under-cited structural theorem is Coven, Pivato and Yassawi 2007. For left-permutive, no-memory CA, an orbit with a
fixed right tail has an odometer orbit closure. Applied to Rule 30 in the frame of its right edge, the single seed's
orbit closure is the 2-adic odometer. Jen and Kopra use left finiteness; Coven-Pivato-Yassawi use right finiteness.
They are the two halves the project's insight says a proof needs, each proved separately. Coven's 1980 aperiodic
family is Rule 30's nearest one-sided relative, with Rule 30 at the excluded periodic word.

### Cited Findings
#### Coven, E. M., Pivato, M. and Yassawi, R., "Prevalence of odometers in cellular automata", Proc. AMS 135 (2007)
815-821, doi:10.1090/S0002-9939-06-08754-5, arXiv:math/0511030 [PART: definitions and Theorems 1, 4 to 6 via ar5iv; the
AMS page returned 403]
- **Class.** Left permutive means phi(., t1, ..., tr) is a permutation of the alphabet. No memory means the rule is
  phi(t0, ..., tr), the window x_i ... x_{i+r}. Positive anticipation means r > 0. —
  [ar5iv](https://ar5iv.arxiv.org/html/math/0511030)
- **Abstract:** for each such CA that is not one-to-one, there is a dense set of points x (a dense G_delta in a
  suitable subspace) whose orbit closure is topologically conjugate to an odometer. —
  [arXiv:math/0511030](https://arxiv.org/abs/math/0511030); [publication record](https://oro.open.ac.uk/67101)
- **Theorem 1 (mechanism):** if the orbit {Phi^n(x)} is infinite and the right tail (x1, x2, ...) is fixed by the
  induced right-tail map Phi_R, then Phi on the orbit closure is conjugate to an odometer. The proof builds the
  successive periods s1, s2, ... of longer and longer tails, which exist by left permutivity. It shows that
  Phi^n(x) -> (base-S expansion of n) is uniformly continuous with uniformly continuous inverse. —
  [ar5iv](https://ar5iv.arxiv.org/html/math/0511030)
- **Theorem 4:** over Z/(p), with local rule t0 + theta(t1, ..., tr) and theta nonzero, all the periods equal p:
  the p-adic odometer. Theorem 5 treats Z/(p^m) (periods are powers of p). Theorem 6 treats a t0 + theta (a
  (q, p, p, ...)-adic odometer). — [ar5iv](https://ar5iv.arxiv.org/html/math/0511030)
- The paper's only worked example is a 3-letter rule. Rule 30 is not mentioned. Access: free arXiv. Under-citation
  evidence: absent from PRIOR-ART.md and from the Rule 30 papers read.

#### Coven, E. M., "Topological entropy of block maps", Proc. AMS 78 (1980) 590-594 [ABS via search] and Blanchard, F.
and Maass, A., "Dynamical behaviour of Coven's aperiodic cellular automata", TCS 163 (1996) 291-302 [BIB; content via
Tisseur]
- Coven: for the block map x0 + prod(x_i + b_i) (mod 2), with k >= 2 and the k-block aperiodic, h = log 2. —
  [AMS](https://www.ams.org/proc/1980-078-04/S0002-9939-1980-0556638-1/)
- Tisseur's restatement: f(x0, ..., xr) = x0 + 1 if x1...xr = b1...br, else x0. The word B must be aperiodic (no
  period p with 0 < p < r). "Blanchard and Maass show that all these CA have equicontinuous points." For B = 10, 000
  is a blocking word, the uniform-measure entropy is 0, and lambda- = 2. — [arXiv:math/0312136, section
  6.1](https://arxiv.org/abs/math/0312136);
  [Blanchard-Maass record](https://ftp.math.utah.edu/pub/tex/bib/idx/tcs1995/163/1/291-302.html)

#### Already in the record (nothing new found)
- Jen 1990, Proposition 3 (no two adjacent columns eventually periodic) and Kopra 2023, Theorem 3.5 (no width-w trace
  eventually periodic for rapidly left expansive rules with a left half eventually zero). Searches found no later
  strengthening for a single column.

#### The 2-adic framework (adjacent field)
- Anashin's criteria, via Anashin, Khrennikov and Yurova [SEC]. A 1-Lipschitz map f on Z_p preserves the measure iff
  f mod p^k is bijective for every k, and is ergodic iff f mod p^k is a single cycle for every k. Bijective
  T-functions are exactly the measure-preserving isometries of Z_2. — [arXiv:1111.3093](https://arxiv.org/abs/1111.3093)

### Inferences
- **[OWN, checked over 400 steps] Rule 30 is a T-function on the 2-adic integers.**
  - *Left-edge frame.* Let bit k of S_t be cell (-t + k) at time t. Then S_{t+1} = 4S XOR (2S OR S), a
    *non-invertible* T-function: bit k depends on bits <= k. Left-finite configurations are exactly the 2-adic
    integers, and finite ones are the natural numbers.
  - *Right-edge frame.* Let bit k of R_t be cell (t - k). Then R_{t+1} = R XOR (2R OR 4R), an *invertible* T-function,
    that is, a measure-preserving isometry of Z_2. It models configurations that are finite on the right.
  - *The centre column.* c_t = bit t of S_t = bit t of R_t, from S_0 = R_0 = 1. It is the diagonal of a 2-adic orbit.
    Column n >= 0 is bit (t - n) of R_t.
  - *What carries the hypotheses.* Left-permutivity is exactly the invertibility of the right-edge map. In the
    left-edge frame, finiteness of the right side is the statement S_0 in N. The record's counter-models, those with
    an infinite left half or a ring background, are not finite configurations, so they correspond to no natural-number
    seed in either frame.
- **[OWN] Coven-Pivato-Yassawi apply to Rule 30.** Let F' = F o sigma, so F'(x)_i = x_i XOR (x_{i+1} OR x_{i+2}). It
  is left-permutive with no memory and anticipation 2, of the form t0 + theta with theta = OR nonzero, and the tail
  0^inf is fixed. F'^n(x)_i = F^n(x)_{i+n}, which is the right-edge frame above. The single seed has right tail 0^inf
  and an infinite orbit, so by Theorems 1 and 4 its F'-orbit closure is conjugate to (Z_2, +1). This is my
  application of their theorem to definitions quoted from the arXiv version; the journal text was not read.
  Concretely, there is a continuous Psi from Z_2 to the orbit closure with Psi(n) = F'^n(seed). The cells t-k..t at
  time t depend only on t mod 2^{m(k)}, and c_t = Psi(t)_{-t}. The same Rule 30 single seed has a *certified*
  eventually periodic left band (RULE30-PRIZE.md section 8.64, a different edge). CPY is the theorem for the chaotic
  right edge.
- **[OWN, measured] The odometer depth.** log2 of the period of the width-k right-edge window, k = 1..40, is: Rule 30:
  0 1 1 2 3 3 4 5 5 6 6 6 6 6 6 7 8 8 8 8 8 8 8 8 9 10 10 11 11 12 12 12 12 12 13 13 14 15 15 16 (about 0.4 k). Rule
  90 (R XOR 4R): 0 0 1 1 2 2 2 2 3 ... 5 (about log2 k). Every window is purely periodic with a power-of-2 period, as
  CPY predict. These are measurements, not an asymptotic claim.
- **[OWN, checked on 20,000 random 64-bit inputs] A 3-state Mealy automaton.** The right-edge map is the state A of
  A = (A, C), B = (A, C)sigma, C = (B, C)sigma over {0, 1}: the sections on inputs 0 and 1, and sigma flips the
  current bit. The theory of self-similar (automaton) groups (sections of A^t, orbit structure on the binary tree, and
  the published classification of 3-state, 2-letter automaton groups) is therefore available. Searched once; no
  source on a Rule 30 automaton group was found. The map is measure-preserving but not ergodic: bit 0 is invariant,
  and on odd inputs bits 1 and 2 both flip every step, so the period mod 8 is 2, not 4.
- **[OWN algebra] Coven's family.** x1 OR x2 = 1 + [x1 x2 = 00] (mod 2), so Rule 30 in its one-sided frame, x0 XOR
  (x1 OR x2), is the bitwise complement of the Coven map with the *periodic* word B = 00. That word is excluded by
  Coven's hypothesis. The Coven automata with aperiodic B (entropy log 2 per Coven, with blocking words per
  Blanchard-Maass) are therefore the nearest calibrated one-sided relatives. If their columns from finite seeds can be
  decided, that would show which hypothesis (aperiodic word against periodic word plus complement) carries Rule 30's
  difficulty. This was not tested.
- **Strengthening route (tentative).** Jen and Kopra extract non-periodicity from left finiteness by a backward
  (permutive) induction. CPY extract an odometer from right finiteness. A single statement that uses both, "a point of
  the 2-adic odometer of the right edge whose left half is also finite cannot have a 2-periodic diagonal", is exactly
  the prize, restated. The restatement is not progress by itself. Its value is that p-adic tools (van der Put and
  Mahler expansions, cycle structure mod 2^k) apply to the right side.

### Gaps
- The CPY journal text was not read, nor were the Coven 1980 and Blanchard-Maass 1996 full texts.
- The literature search for "Rule 30" with "T-function", "2-adic", "Mealy automaton" or "automaton group" found
  nothing. Absence after one search is weak evidence.
- Whether Rule 30's one-sided frame F' has equicontinuous points (as Coven's maps do) was not determined.
- Klimov and Shamir's T-function papers were not opened. The general claim that every cycle of an invertible
  T-function mod 2^n has power-of-2 length was not found stated in a source. Here it is a consequence of CPY Theorem
  4 for this map, and the measured periods agree.

## Which results on columns of linear or additive CA (where periodicity questions are decided) have proofs whose
structure might carry over to the nonlinear Rule 30?

### Takeaway
The decided linear cases rest on superposition. Litow and Dumas (1993) show that columns of additive CA over F_q
from finite configurations are algebraic power series, hence p-automatic by Christol's theorem. Rowland and Yassawi
(2015, in the record) prove the converse. Allouche, von Haeseler, Peitgen and Skordev (1996) treat the whole
space-time double sequence. None of this algebra exists for Rule 30. The structure that does carry over is the
odometer: in the right-edge frame both Rule 90 and Rule 30 are 2-adic odometer orbits, and they differ in how many
2-adic digits of t a window of depth k needs.

### Cited Findings
- **Litow, B. and Dumas, Ph., "Additive cellular automata and algebraic series"**, TCS 119(2) (1993) 345-354 [BIB;
  statement via slides]. Each column of a linear CA over F_q, started from an initial condition with finitely many
  nonzero entries, is p-automatic. — [Utah TCS
  bibliography](https://ftp.math.utah.edu/pub/tex/bib/idx/tcs1990/119/2/345_354.html);
  statement in [Yassawi's lecture
  notes](https://moore.pims.math.ca/sites/default/files/lecture-notes/YassawiR-%20Automata.pdf).
  Proof strategy per Rowland's slides: Christol's theorem and a theorem of Furstenberg on formal power series. —
  [Rowland, Fields slides](https://gfs.fields.utoronto.ca/programs/scientific/12-13/words/slides/Rowland.pdf).
  Access: paywalled (Elsevier). Absent from PRIOR-ART.md, which cites the converse only.
- **Rowland, E. and Yassawi, R., "A characterization of p-automatic sequences as columns of linear cellular
  automata"** (already in the record): the converse, every p-automatic sequence is a column of a linear CA. —
  [arXiv:1209.6008](https://arxiv.org/abs/1209.6008)
- **Allouche, J.-P., von Haeseler, F., Peitgen, H.-O. and Skordev, G., "Linear cellular automata, finite automata and
  Pascal's triangle"**, Discrete Appl. Math. 66 (1996) 1-22 [ABS via the preprint page]: automaticity of the double
  sequences produced by linear CA, with a complete solution for binomial coefficients and Lucas numbers and partial
  results in general. Von Haeseler's list gives the title variant "... matrix substitutions, and Pascal's triangle". —
  [preprint](https://webusers.imj-prg.fr/~jean-paul.allouche/ahps96.pdf). Follow-up in TCS 188(1) (1997) 195-209
  [BIB]. — [Utah record](https://ftp.math.utah.edu/pub/tex/bib/idx/tcs1995/188/1/195-209.html)
- **Allouche, J.-P. and Berthe, V., "Triangle de Pascal, complexite et automates"**, Bull. Belg. Math. Soc. (1997) [BIB
  via search]. — [EMIS PDF](https://emis.univie.ac.at/journals/BBMS/Bulletin/bul971/allouche.pdf)
- **Berthe, V., "Complexite et automates cellulaires lineaires"**, RAIRO ITA 34(5) (2000) 403-423 [BIB; the abstract
  was not on the page]. — [Numdam](https://numdam.org/item/ITA_2000__34_5_403_0/)
- **Jen, E., "Linear cellular automata and recurring sequences in finite fields"**, Comm. Math. Phys. 119(1) (1988)
  13-28 [BIB only; abstract not retrieved]. — [MaRDI author page](https://portal.mardi4nfdi.de/wiki/Erica_Jen);
  citation in [arXiv:1909.06915](https://arxiv.org/abs/1909.06915)
- **Akin, H., "The topological directional entropy of Z^2-actions generated by linear cellular automata"** [title and
  search summary]. — [arXiv:0802.0953](https://arxiv.org/abs/0802.0953)
- CPY Theorems 4 to 6 (previous section) are the algebraic families (t0 + theta, Z/p^m, a t0 + theta) where the
  odometer is explicit. — [ar5iv](https://ar5iv.arxiv.org/html/math/0511030)

### Inferences
- The linear proof needs the space-time generating function to be rational in two variables, so that a column is a
  diagonal-type extraction and Furstenberg's theorem makes it algebraic. Christol's theorem then makes it automatic.
  Both steps use superposition over F_p. Rule 30's OR is x + y + xy over F_2, and the xy term destroys the rational
  generating function. This is the same barrier as "Kopra's barrier" in the record (Rule 90 is in Kopra's class), seen
  from the algebraic side.
- **What carries over [OWN, measured].** The odometer frame is shared. For Rule 90 the depth-k window needs about
  log2 k binary digits of t, the slow growth that goes with automatic columns. For Rule 30 it needs about 0.4 k digits
  (k <= 40). A tentative reading: Rule 30's column is "an automaton reading a linearly growing number of digits of
  t", which no finite automaton can do. That fits the conjecture that the column is not automatic, but it is not a
  proof: periodicity needs only one bit per time, and the window carries far more.
- A concrete test the record can run cheaply: for the right-edge odometer, compute the coordinate functions g_k
  (cell t-k as a function of t mod 2^{m(k)}) for k up to about 40, and ask whether the g_k have the self-similar
  (2-kernel) structure that Rule 90's have. A finite 2-kernel would contradict the measured growth. A structured but
  infinite kernel would be a new invariant of the right side.

### Gaps
- The full texts of Litow-Dumas, Allouche et al. 1996, Berthe 2000 and Jen 1988 were not read, so their exact theorem
  numbering and hypotheses (finite configurations; F_q against Z_m) are as given in secondary sources.
- Martin, Odlyzko and Wolfram (1984, algebraic properties of additive CA) and Guan and He (1986) were not checked in
  this survey.
- No nonlinear analogue of Christol or Litow-Dumas (for example for quadratic rules over F_2) was found. The search
  did not target it directly.

## What did Milnor, Sablik or Boyle-Lind prove about the directional entropy of permutive CA at the vertical direction,
and is it zero or positive for Rule 30?

### Takeaway
At the vertical, directional entropy is the entropy of the map itself. For Rule 30 it is positive: at least log 2
(the i.i.d.-column argument above) and at most 2 log 2 (Tisseur's Proposition 5.3; the Courbage-Kaminski bound).
Milnor gives the geometry (the causal cone; in the record). Boyle and Lind's phase-transition results live on
expansive components of a Z^2 action. Sablik's Z x N version shows that Rule 30 has no expansive direction, only a
left-expansive cone that contains the vertical. None of these speaks to one finite configuration.

### Cited Findings
- **Milnor, J., "On the entropy geometry of cellular automata"**, Complex Systems 2 (1988), already in the record
  (Example 6.2, the additional causal cone of a left-permutive map). Nothing new was read.
- **Milnor, J., "Directional entropies of cellular automaton-maps"**, in *Disordered Systems and Biological
  Organization* (1986) [BIB]: the original definition of the directional entropy function. Not read. —
  [Springer record](https://www.springerprofessional.de/directional-entropies-of-cellular-automaton-maps/14967716)
- **Park, K. K., "Continuity of directional entropy"**, Osaka J. Math. 31 (1994) [SEC]. Directional entropy in a
  rational direction is an integral, and the function is upper semicontinuous. Park writes that it was "not yet clear
  if the directional entropy is in fact continuous even in the case of cellular automata". —
  [Osaka repository PDF](https://ir.library.osaka-u.ac.jp/repo/ouka/all/11918/ojm31_03_07.pdf)
- **Boyle, M. and Lind, D., "Expansive subdynamics"**, Trans. AMS 349(1) (1997) 55-102 [ABS via search summary]. For
  a Z^d action on an infinite compact metric space, expansive k-dimensional subspaces form an open set. Nonexpansive
  subspaces exist in every dimension up to d - 1. Properties such as Milnor's directional entropies are constant, or
  vary nicely, within an expansive component and change abruptly between components ("phase transitions"). —
  [abstract index](https://acnpsearch.tweb-dev.unibo.it/singlejournalindex/3323825); cited by Sablik as the origin
  of directional expansivity — [Sablik 2008](https://www.math.univ-toulouse.fr/~msablik/article/2008-TCS.pdf)
- **Sablik 2008** and **Courbage-Kaminski 2002**: see the first question (Example 3.4, Theorem 5.2; the bound 2 at
  the vertical).
- **Lind, D. A., "Applications of ergodic theory and sofic systems to cellular automata"**, Physica D 10 (1984) 36-44
  (the Los Alamos 1983 proceedings) [BIB]. Not read. — [proceedings
  contents](https://www-users.york.ac.uk/~ss44/books/pages/l/DouglasALind.htm);
  cited in [arXiv:1301.3790](https://arxiv.org/abs/1301.3790)

### Inferences
- **Positive for Rule 30.** The vertical directional entropy is between log 2 and 2 log 2, both topologically and
  for the uniform measure ([OWN] lower bound; Tisseur's upper bound). It is not zero.
- Boyle-Lind's theory needs a Z^2 action, and Rule 30 is not invertible (0^inf has two preimages). In Sablik's
  Z x N version Rule 30 has no expansive component, so the "constant on expansive components" results have nothing to
  act on. The vertical sits strictly inside the left-expansive cone (-inf, 1), whose boundary slope 1 is the
  right-edge frame where the CPY odometer lives (tentative: whether slope 1 is a phase transition for Rule 30's
  directional entropy was not determined).
- **[OWN, tentative] The right-finite points.** On the configurations finite on the right, the right-edge dynamics is
  an isometry of Z_2 (zero entropy on that invariant set). That set is null for the Bernoulli measure, so this says
  nothing about the measure-theoretic directional entropy at slope 1. It does make the single seed's world at the
  right edge zero-entropy and rigid, as CPY's odometer says, while the vertical column through the same orbit is the
  open question.

### Gaps
- Milnor 1986, Smillie's directional-entropy work, the Boyle-Lind full text, Nasu's textile systems (Memoirs AMS
  1995) and Boyle-Maass on expansive one-sided CA were not read. Whether any of them computes a directional entropy
  function for a one-sided permutive rule like Rule 30 is unknown.
- No published value of Rule 30's directional entropy at any slope was found, except NKS's spacetime entropy bound.
