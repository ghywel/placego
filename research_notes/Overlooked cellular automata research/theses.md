# Theses (about 1995-2026) on global properties of one-dimensional CA relevant to Rule 30's Problem 1 (period 2)

Scope and method. I searched the French national portal (theses.fr API) and HAL, the University of Turku repository
(UTUPub), the Universidad de Chile repository, the York thesis page, and the general web. I downloaded and read
targeted parts of six full texts: Kopra 2019, Guillon 2008, Tahay 2020, Hotanen 2024, Mariot 2018 and Powley 2009.
I also read in full Dolce and Tahay 2022, a paper that grew out of the Tahay thesis line, and the parts of Sablik 2008
(a paper from the Sablik thesis) that state its theorems. For every other thesis I saw only the abstract or a
catalogue record, and the entry says so.

Prior-art check (grep of PRIOR-ART.md, 2026-10-09). Already listed: Powley's thesis (GC794), Spencer's DePaul MSc
thesis, Shereshevsky's Warwick PhD thesis, Das (arXiv:2207.13237), Kopra's and Kari-Kopra's papers, "Ultimate traces"
(arXiv:1001.0251, abstract level), and Dolce-Tahay (marked "snippet only"). Not in the file: the Kopra thesis itself,
and the Guillon, Tahay, Sablik, Hotanen, Bernardo, Yasmineh, Tisseur and Cipriano Jara theses.

Citation counts. These could not be obtained. The Semantic Scholar API returned HTTP 429, and the OpenAlex API
reported its shared free budget exhausted. HAL, theses.fr and UTUPub show no counts. "Under-cited" below means only
that the work is absent from this project's record, or (for the French theses) exists only as a French-language
thesis whose results never appeared in the English literature in that form. It is not a measured count.

## Which theses prove results about traces or columns of CA, especially for permutive or expansive rules?

### Takeaway
Two theses carry most of the weight. **Guillon (2008)** builds the general theory of trace (column) subshifts. Its
"retourné" theorem makes "a column pair forces everything to the left" an exact equivalence with one-sided positive
expansivity, and gives entropy = trace entropy. **Kopra (2019)** contains a complete one-page proof that a *width-1*
trace is never eventually periodic from a finite configuration, for the multiplication automata in Rule 30's own
class. That proof shows exactly which ingredient Rule 30 lacks. Sablik's directional dynamics (thesis 2006; paper read)
and Hotanen (2024) add expansive-direction and entropy facts for permutive rules.

### Cited Findings

**1. Kopra, J., "Cellular Automata with Complicated Dynamics", doctoral dissertation, University of Turku (TUCS
Dissertations), 2019.**
- Bibliographic details: ISBN 978-952-12-3891-8, 145 pp., advisor Jarkko Kari.
- Links: [UTUPub record](https://www.utupub.fi/handle/11111/26292);
  [PDF](https://www.utupub.fi/bitstreams/f229bc81-1590-4a47-9047-cc8113366378/download); advisor per [Math
  Genealogy](https://mathgenealogy.org/id.php?id=259088).
- Access: full text downloaded. Chapter 3 read (§§3.1, 3.3, 3.4, 3.7, 3.8), plus Theorem 5.1.2.
- Prior art: the thesis is NOT in PRIOR-ART.md; the derived papers are.

What it proves (quoted or near-quoted from the PDF):
- **Prop 3.3.4 (leftward column CA, width 1).** "There is a radius-1 CA ∆p/q : Ξ(Πp/q,pq) → Ξ(Πp/q,pq) such that
  ∆p/q(TrΠp/q,pq,i(x)) = TrΠp/q,pq,i−1(x)." In words, the width-1 trace at column i determines the trace at column
  i−1 through a sliding block code. The proof gets y[0] modulo q and modulo p separately (Lemma 3.3.3 and the CRT
  step).
  — [Kopra thesis PDF](https://www.utupub.fi/bitstreams/f229bc81-1590-4a47-9047-cc8113366378/download)
- **Prop 3.3.5 (width-1 aperiodicity).** "Let p > q. If x ∈ ΣZpq is a configuration that represents a positive real
  number (in particular, if x is a finite configuration different from 0Z), then TrΠp/q,pq(x) is not eventually
  periodic." The proof is complete and about 15 lines long:
  1. Assume the width-1 trace is periodic from time 0 with period P.
  2. Prop 3.3.4, applied inductively, makes every column of x_t = (σ⁻¹∘Π)^t(x) periodic with the same P.
  3. The real value of x_t is real(x)/q^{2t}, so for large T the first P rows to the left are zero. Periodicity then
     forces y_T = 0^Z, and so y_t = 0 for all t ≥ T.
  4. That bounds (p/q)^t·real(x), a contradiction.
  The thesis states the analogy itself: Jen's proof rests on "digits in the space-time diagram of W30 are determined
  to the left" and on "all finite perturbations in the configuration 0Z must propagate to the left".
  — [Kopra thesis PDF](https://www.utupub.fi/bitstreams/f229bc81-1590-4a47-9047-cc8113366378/download)
- **Theorem 3.1.12 (Jen), as restated.** For finite x ≠ 0^Z, the width-2 trace Tr_{W30,[0,1]}(x) is not eventually
  periodic. In 2019 Kopra wrote: "It still seems to be an open problem whether TrW30(x) (the trace of width 1) can be
  eventually periodic for some finite x ≠ 0Z." **Problem 3.1.13:** "Is W30 regular?" (whether all its trace subshifts
  are sofic). — [Kopra thesis PDF](https://www.utupub.fi/bitstreams/f229bc81-1590-4a47-9047-cc8113366378/download)
- **Lemma 3.4.17.** If x[j] ∈ Q = {np : 1 ≤ n < q} and x[i] = 0 for i > j, then Tr_{p/q}(x) is not eventually
  periodic. **Theorem 3.4.15:** the trace subshift has complexity
  P(n) = pq(p^{n−1} − q^{n−1})(q−1)/(p−q) + p^n·q (for 3/2: 4·3^n − 3·2^n). **Cor 3.4.19:** Ξ_{p/q} is not sofic, so
  Π_{p/q,pq} is not regular. — [Kopra thesis
  PDF](https://www.utupub.fi/bitstreams/f229bc81-1590-4a47-9047-cc8113366378/download)
- **Theorems 3.7.1 and 3.7.2 (maximal vs average left Lyapunov exponent).**
  - λ−(0^Z, Π_{p,pq}) = log_pq p, yet some x has λ−(x) = 1, so λ−(Π_{p,pq}) = 1.
  - The average exponent is I_μ^−(Π_{p,pq}) = log_pq p for the uniform measure μ.
  - Section 3.6 records a cited result: left-permutive CA with memory ≠ 0 are strongly mixing. Problem 3.6.9 asks for
    a natural class of "weak permutive" CA.
  — [Kopra thesis PDF](https://www.utupub.fi/bitstreams/f229bc81-1590-4a47-9047-cc8113366378/download)
- **Theorem 5.1.2 (diffusive glider CA).** For every finite configuration and N, some time t has
  G^t(x)[−N, N] = 0^{2N+1}, with only left-gliders to the left and right-gliders to the right. This is a
  finite-configuration result, but not about Rule 30. — [Kopra thesis
  PDF](https://www.utupub.fi/bitstreams/f229bc81-1590-4a47-9047-cc8113366378/download)
- Checkability: the proofs are elementary and self-contained. No formalisation or code is included.

**2. Guillon, P., "Automates cellulaires : dynamiques, simulations, traces", thèse de doctorat (informatique),
Université Paris-Est, defended 24 November 2008.**
- Bibliographic details: advisors Enrico Formenti and Julien Cervelle; NNT 2008PEST0215; HAL tel-00432058; 171 pp.
  Written in French, with an English summary at the end.
- Links: [HAL PDF](https://theses.hal.science/tel-00432058/document); [theses.fr
  record](https://theses.fr/2008PEST0215).
- Access: full text downloaded. §§4.6 to 4.8 read, Chapter 5 sampled, Chapter 6 statements located.
- Prior art: absent from PRIOR-ART.md. Only the co-authored "Ultimate traces" paper is listed, at abstract level.

What it proves:
- The abstract defines the *tracé* (trace subshift) as "l'ensemble des mots infinis représentant la séquence des
  états successifs pris par la cellule centrale … ou un groupe de cellules centrales". It proves that every property
  of the trace that "peu[t] se voir infiniment tard" is undecidable. — [theses.fr
  record](https://theses.fr/2008PEST0215)
- **Fait 4.6.6.** Strongly left-permutive CA (left-permutive and not left-unidirectional) are positively expansive to
  the left. Strongly bipermutive CA are positively expansive (cited to [8]).
  — [Guillon thesis PDF](https://theses.hal.science/tel-00432058/document)
- **Prop 4.6.8 (the "retourné", a quarter-turn of the space-time diagram).** A CA admits a one-sided right (resp.
  left) *retourné* F* on the width-r trace subshift τ_F^r iff it is positively right (resp. left) expansive of width r.
  Here F* is a CA on the trace sequences with F*∘T = T∘σ. The thesis says one can "reconstruire tout le diagramme à
  partir du tracé de largeur r".
  **Remark 4.6.9.** The retourné is positively expansive of width 1. If F has radius r and is (positively) expansive
  on one side, then τ_F^k is conjugate to τ_F^r for every k ≥ r.
  — [Guillon thesis PDF](https://theses.hal.science/tel-00432058/document)
- **Prop 4.8.5.** A CA positively expansive on the left (or right) with radius r has entropy H(F) = H(τ_F^r). The
  thesis notes that this recovers a cited result: "les permutifs … ont une entropie égale à celle de leur facteur
  canonique". — [Guillon thesis PDF](https://theses.hal.science/tel-00432058/document)
- **Prop 4.7.18 and Cor 4.7.19.** A CA is asymptotically p-periodic iff its width-1 trace subshift is weakly
  p-preperiodic. Example 4.7.20 shows that the preperiod cannot be made uniform.
  **Theorem 4.6.12 (credited to Nasu).** Positively expansive CA on mixing subshifts have τ_F^r essentially a
  one-sided full shift. — [Guillon thesis PDF](https://theses.hal.science/tel-00432058/document)
- Checkability: the proofs are short and written out, in French.

**3. Sablik, M., "Étude de l'action conjointe d'un automate cellulaire et du décalage : une approche topologique et
ergodique", thèse, Université de la Méditerranée (Aix-Marseille 2), 2006.**
- Bibliographic details: NNT 2006AIX22019. Director François Blanchard per theses.fr; Math Genealogy also lists
  Alejandro Maass.
- Access: the thesis is **not online** (theses.fr "accessible: non"). I read the derived paper instead.
- Links: [theses.fr search record](https://theses.fr/2006AIX22019); [Math
  Genealogy](https://mathgenealogy.org/id.php?id=129911).
- **Derived paper:** M. Sablik, "Directional dynamics for cellular automata: A sensitivity to initial condition
  approach", *Theoretical Computer Science* 400 (2008) 1–18, doi:10.1016/j.tcs.2008.02.052. Theorems and examples
  read from the [author PDF](https://www.math.univ-toulouse.fr/~msablik/article/2008-TCS.pdf).
- Prior art: absent from PRIOR-ART.md.

What it proves:
- **Example 3.4.** A left-permutive CA with neighbourhood [r, s] has an open half-line of left-expansive directions,
  ending at a neighbourhood endpoint. Bipermutive CA have an open interval of expansive directions. Caution: the
  minus signs were lost in my text extraction, so check the exact endpoints in the PDF.
- **Theorem 5.2.** The right- and left-expansive direction sets are open half-lines, and the set of expansive
  directions is an open interval.
- **Theorem 6.1** sorts every CA on a weakly-specified subshift into six classes, C1 to C6. In class C2 there is a
  unique rational equicontinuous direction α, and (F^n σ^{⌊αn⌋}) is ultimately periodic.
- Source for all three: [Sablik 2008 PDF](https://www.math.univ-toulouse.fr/~msablik/article/2008-TCS.pdf).

**4. Hotanen, T., "On the topological entropy and Lyapunov exponents of cellular automata: decision problems,
dynamical properties and generalizations", doctoral dissertation, University of Turku, 2024.**
- Bibliographic details: Annales Univ. Turkuensis Ser. A1 No. 722; five included papers I–V (e.g. AUTOMATA 2020,
  "Everywhere Zero Pointwise Lyapunov Exponents for Sensitive Cellular Automata").
- Links: [UTUPub record](https://www.utupub.fi/items/33b01d64-1b8b-48b8-8fb4-efb28a3eaab4);
  [PDF](https://www.utupub.fi/bitstreams/94811642-f220-4598-8922-c94ddaff3ddc/download).
- Access: full text downloaded; introduction and Lemma 5.2.12 read.
- Prior art: absent from PRIOR-ART.md.

What it proves:
- The introduction uses Rule 30 as its running example. It shows Rule 30 is sensitive from left-permutivity alone:
  "if two configurations differ only at index i, their images … will differ at index i + 1".
- **Lemma 5.2.12.** For a CA over a group with G/N ≅ Z that is left- or right-permutive with respect to h ∈ g^k N,
  under the uniform measure, h^N_μ ≥ |k| log|Σ|. This is an entropy lower bound for permutive rules.
- Relevance is low to moderate. It gives entropy and Lyapunov tools, not column periodicity.
- Source: [Hotanen thesis PDF](https://www.utupub.fi/bitstreams/94811642-f220-4598-8922-c94ddaff3ddc/download).

**5. Abstract-only French theses on permutive and ergodic CA (none online).**
- **Bernardo, M., "Nouveaux aspects probabilistes et topologiques de systèmes dynamiques chaotiques, ergodiques et
  intégrables", Paris 7, 2001 (director Tuong Trong Truong).** Part 2 is "limitée à la classe des automates
  cellulaires permutatifs". It shows that directional entropy in irrational directions reduces, "dans les cas
  favorables, au calcul du rayon spectral d'une matrice de transition finie", and otherwise only an interval is given.
  Full text not online. — [theses.fr](https://theses.fr/2001PA077061)
- **Tisseur, P., "Aspects ergodiques des automates cellulaires", Aix-Marseille 2, 1999 (director F. Blanchard).**
  For μ F-invariant and shift-ergodic, it proves that the left and right Lyapunov exponents exist and that
  h_μ(F) ≤ h_μ(σ)(λ⁺ + λ⁻). It introduces smaller "mean" exponents that satisfy the same bound. The derived
  Nonlinearity 2000 paper is already in PRIOR-ART. Abstract only. — [theses.fr](https://theses.fr/1999AIX22006)
- **Yasmineh, S., "Abondance des ondes et propriétés chaotiques des automates cellulaires", Paris 6, 1998 (director
  Maurice Courbage).** A numerical study of travelling waves in 1D CA. For one class of CA, it explains the wavelength
  distribution by roots of polynomials over a finite field. Part 3 treats "chaos spatial", measured by positive
  entropy of stationary structures. Abstract only; I found no derived paper online. —
  [theses.fr](https://theses.fr/1998PA066368)
- **Cipriano Jara, I. U., "Randomización de Medidas de Probabilidad por Autómatas Celulares de Tipo Permutativo No
  Algebraico", undergraduate memoria, Universidad de Chile, 2011.** Advisors: A. Maass, S. Martínez, M. Schraudner.
  It classifies positively expansive non-bipermutive CA and reports that right-permutive automata can have blocking
  words only in direction −1. Only the repository abstract was read. —
  [repository record](https://repositorio.uchile.cl/handle/2250/104316);
  [PDF](https://repositorio.uchile.cl/bitstream/handle/2250/104316/cf-cipriano_ij.pdf?sequence=3&isAllowed=y)

### Inferences
- **Kopra's Prop 3.3.5 is the clearest template for "why period 2 is hard".** Its two ingredients map onto the
  team's key insight:
  - Left-finiteness enters as "real(x) > 0" plus the shrinking real value.
  - The genuine dynamics enter as the width-1 leftward CA ∆ of Prop 3.3.4.
  Rule 30 has the second ingredient only at width 2 (Jen). A single eventually period-2 centre column therefore does
  not, by itself, propagate a period to the left. The missing step is exactly the width-1 version of Prop 3.3.4. The
  proof also shows the most a period-2 attack can borrow: a monotone "size" functional of the finite left side that
  is forced to vanish under a periodic trace.
- **Guillon's retourné is the published general form of the project's pair map / vertical inverse** (G128/G129's H).
  Citing it gives a standard reference for "column pair ⇒ left half".
  - Remark 4.6.9 and Prop 4.8.5 imply that Rule 30's topological entropy equals the entropy of its trace subshift of
    the appropriate width. The project's column-pair counts (§8.2) would then measure Rule 30's entropy.
  - **Caution:** Guillon's radius/width convention must be checked before applying this. Read naively with r = 1, it
    would make Rule 30's width-1 trace (a full shift, since column 0 at time t depends bijectively on x(−t)) conjugate
    to its width-2 trace, which looks false if the pair count grows faster than 2^t. I did not resolve this.
- **Cor 4.7.19 and Sablik's Theorem 6.1 are about all configurations, not one orbit.** They settle global periodicity
  questions, which Rule 30 trivially fails because it is sensitive. They do not settle Problem 1. This is a scope
  guard, not a route.
- **Kopra 3.7.1–3.7.2 shows that maximal and average leftward speeds can differ inside Rule 30's class** (1 vs
  log_pq p). Single-seed measurements of Rule 30's leftward information speed (PRIOR-ART notes no published value)
  should not be read as either the maximal or the average exponent without argument.

### Gaps
- No thesis was found that proves a width-1 column statement for Rule 30 itself, or that treats Problem 1 directly.
- The Sablik, Bernardo, Tisseur and Yasmineh theses are not online; only abstracts or a derived paper were read.
  Bernardo's spectral-radius formula for directional entropy of permutive CA could not be checked.
- Citation counts are missing for every item (the APIs were blocked).
- Whether the trace part of Guillon's thesis was ever fully published in English is unknown. "Sofic trace" (CiE
  2007, [arXiv:math/0703241](https://arxiv.org/abs/math/0703241)) and the Rice theorem on traces
  ([HAL hal-00620284](https://hal.science/hal-00620284)) cover parts of it; the retourné/entropy section may not have
  been published.

## Which theses treat Rule 30 or its equivalence class (rules 30, 86, 135, 149) specifically?

### Takeaway
No thesis found treats Rule 30's columns beyond restating Jen. The Rule 30 content in theses is:
- Kopra's restatement of Jen, plus his open questions (width-1 trace; "Is W30 regular?").
- Powley's ring (periodic-boundary) preimage and transition-graph data.
- Hotanen's sensitivity example.
- Mariot's cryptographic discussion.
- Spencer's MSc (already listed).
Rules 86, 135 and 149 appear in no thesis found.

### Cited Findings
- **Kopra 2019** (above) defines W30, restates Jen's width-2 theorem, flags the width-1 trace as open, and asks
  Problem 3.1.13 "Is W30 regular?". It also records Wolfram's conjecture (NKS p. 725) that W30 with a single 1 is a
  weak universal pattern generator. — [Kopra thesis
  PDF](https://www.utupub.fi/bitstreams/f229bc81-1590-4a47-9047-cc8113366378/download)
- **Powley, E. J., "Global Properties of Cellular Automata", PhD thesis, University of York, October 2009** (230 PDF
  pages; supervisor Susan Stepney per [Math Genealogy](https://mathgenealogy.org/id.php?id=162049)). Already in
  PRIOR-ART (GC794). — [Powley PDF](https://www.cs.york.ac.uk/nature/group/theses/EdPowley.pdf)
  - What it gives on Rule 30: de Bruijn/transfer matrices and preimage counts, e.g. the preimages of the
    configuration 10001101 (Example 4.4).
  - Transition graphs of all ECAs on rings Z_10 and Z_11 (Appendices C and D). Rule 30 is listed as class 3 with
    "max transient 46" and "max transient 55", as printed in the two appendices.
  - It proves nothing about temporal columns or traces of infinite finite-support configurations. That agrees with
    GC794's reading that section 9.3 "does not address a lone temporally periodic column".
- **Mariot, L., "Cellular automata, boolean functions and combinatorial designs", PhD thesis, Université Côte d'Azur,
  2018** (HAL tel-01812051). Rule 30 appears only as Wolfram's stream cipher and its weak
  cryptographic properties; the thesis is about bipermutive CA and Latin squares. No column-periodicity content.
  PRIOR-ART lists only a later Mariot survey. — [HAL PDF](https://theses.hal.science/tel-01812051/document)
- **Hotanen 2024** uses Rule 30 only as an introductory example of left-permutive sensitivity. —
  [Hotanen PDF](https://www.utupub.fi/bitstreams/94811642-f220-4598-8922-c94ddaff3ddc/download)
- **Rowland's PhD (Rutgers 2009), "Experimental Methods Applied to the Computation of Integer Sequences"**: per its
  catalogue abstract it treats the gcd recurrence and pattern-avoiding binary trees, not Rule 30. So the 2006 Rule 30
  paper was not extended there. Abstract only. —
  [RUcore record](https://rucore.libraries.rutgers.edu/rutgers-lib/25893/)
- Already in PRIOR-ART, not re-read: Spencer's MSc thesis (DePaul 2013, arXiv:1306.3546), the Rule 30 forcing rules
  and cryptanalysis; Das, "Rule 30: Solving the Chaos" ([arXiv:2207.13237](https://arxiv.org/abs/2207.13237)), a
  student preprint claiming a solution, recorded as not accepted.

### Inferences
- Kopra's "Is W30 regular?" is a neighbouring open question the team could cite. If some width-k trace subshift of
  Rule 30 were sofic, column-pair languages would be regular, and a period-2 column would face a finite-automaton
  obstruction. Kopra proves non-soficness for the multiplication automata, which suggests the answer for Rule 30 is
  also "no".
- No thesis found treats the 30/86/135/149 class as a class. The reflection and conjugation symmetries are noted only
  in Powley (Example 2.2: conjugate of 30 is 135, plus the reflection).

### Gaps
- No master's or PhD thesis on Rule 30's centre column was found beyond those listed. Searches covered theses.fr,
  HAL, UTUPub, the Universidad de Chile repository and the general web; I did not search ProQuest.
- Works citing Powley's thesis could not be listed. Citation APIs were blocked, and web search returned only Powley
  and Stepney's own JCA 2010 paper (vol. 5, pp. 353–381) as a companion.

## Which theses give results on eventual periodicity of columns from finite configurations, or on the interplay of
left-finiteness and right dynamics?

### Takeaway
**Tahay (2020)** is the find here. It is a whole thesis on columns of CA from finite configurations, and with Dolce
and Tahay (2022) it proves that very structured non-periodic sequences occur as columns of 0-quiescent CA from
finite configurations, even binary ones (by recoding): the Fibonacci word, every quadratic-slope Sturmian word, and
indicators of polynomial values. It is a library of counter-models. Any proof for Rule 30 must use Rule 30's specific
rule, not just "finite seed + quiescent CA". Kopra's Prop 3.3.5 (above) is the matching positive result, where left
finiteness plus genuine dynamics do exclude periodicity at width 1.

### Cited Findings

**6. Tahay, P.-A., "Colonnes dans les automates cellulaires et suites généralisées de Rudin-Shapiro", thèse de
doctorat, Université de Lorraine, defended 17 December 2020.**
- Bibliographic details: advisors Thomas Stoll and Irène Marcovici; NNT 2020LORR0198; HAL tel-03184510; 108 pp.
- Links: [HAL PDF](https://hal.univ-lorraine.fr/tel-03184510/document); [theses.fr](https://theses.fr/2020LORR0198).
- Access: full text downloaded. Chapter 2 read: definitions, Theorems 2.2.1 and 2.3.1, Propositions 2.3.1–2.3.4,
  Example 2.3.3 and §2.4 open questions.
- Prior art: the thesis is NOT in PRIOR-ART.md; Dolce-Tahay is listed as "snippet only".

What it proves:
- **The object studied** is S = {(Φ^n(x)_0)_{n≥0} : Φ a 0-stable CA on A^Z, x ∈ C_0(A) finite}, the set of
  sequences that occur as a column of a quiescent CA started from a finite configuration.
- **Theorem 2.2.1 (Rowland–Yassawi).** A sequence over F_q is p-automatic iff it is a column of a linear CA over F_q
  from a finite configuration.
- **Theorem 2.3.1.** For P ∈ Q[X] of degree ≥ 1 with P(N) ⊂ N, the indicator 1_{P(N)} ∈ S.
- **Props 2.3.2 and 2.3.3.** The indicator of the Fibonacci numbers and **the Fibonacci word are in S**.
- **Prop 2.3.4 (binary recoding).** If F on B^Z (B ⊋ {0,1}) is 0-stable, x is finite, and F^n(x)_0 ∈ {0,1} for all
  n, then the sequence is a column of a *binary* 0-stable CA, of radius (2k−1)(r+1)−1.
  **Example 2.3.3:** every binary 3-automatic sequence (e.g. the indicator of {3^n}) is a column of a 2-state CA
  from a finite configuration. This answers Rowland–Yassawi's third question (p. 80).
- **One-sided constructions.** The constructions use only the right side of column 0: "n'utiliseront que les
  colonnes à droite de celle-ci".
- **Open questions (§2.4):** k-automatic columns when k is not a prime power; the Tribonacci and other k-bonacci
  words.
- Checkability: signal constructions with figures and full proofs; the recoding argument is explicit. No code.
- Source for all of the above: [Tahay thesis PDF](https://hal.univ-lorraine.fr/tel-03184510/document).

**7. Dolce, F. and Tahay, P.-A., "Column Representation of Sturmian Words in Cellular Automata", DLT 2022, LNCS
13257, pp. 127–138, doi:10.1007/978-3-031-05578-2_10.**
- Links: [HAL PDF](https://hal.science/hal-04066361/document).
- Access: full paper read; the theorem is checked against Props 1–4.
- Prior art: listed as "snippet only"; now read in full.
- **Theorem 1:** "A Sturmian word with quadratic slope can be represented as a column in the space-time diagram of a
  one-dimensional cellular automaton." Here "represented" means membership in S: a 0-quiescent CA started from a
  finite configuration.
- The construction runs through the eventually periodic continued fraction of the slope (Props 3–4). Prop 3's proof
  is marked "(Sketch)".
- Section 6 suggests extending it to Arnoux-Rauzy and dendric words. — [Dolce-Tahay
  PDF](https://hal.science/hal-04066361/document)

**8. Related papers by the same group (not read beyond titles and HAL metadata).**
- Marcovici, Stoll and Tahay, "Construction of Some Nonautomatic Sequences by Cellular Automata" (2018), HAL
  [hal-01824876](https://inria.hal.science/hal-01824876/document).
- Tahay, "Characteristic Sequences of the Sets of Sums of Squares as Columns of Cellular Automata" (2023), HAL
  [hal-04504166](https://hal.science/hal-04504166/document).

**Kopra, Prop 3.3.5 and Lemma 3.4.17** (entry 1 above): width-1 non-periodicity from finite or left-supported
configurations, in Rule 30's class.

### Inferences
- **Counter-model library.** Combine Dolce–Tahay Theorem 1 with Tahay Prop 2.3.4 (recoding): there are binary
  0-quiescent CA whose column from a finite configuration is a Sturmian word with factor complexity n + 1, and these
  constructions need only the right half. So no argument of the form "finite configuration + quiescent binary CA ⇒
  column complexity grows" can work.
  This matches the team's observation that counter-models exist when one ingredient is dropped. The ingredient these
  models drop is *Rule 30's particular local rule* (they are large-radius signal machines, presumably not
  left-permutive). It gives a ready citation for PRIOR-ART's "Theorem E (Sturmian columns excluded): NOT FOUND" row:
  Sturmian exclusion is false for CA in general.
- **A sharp test question these sources suggest, untested and tentative:** can a *left-permutive* CA (or one in
  Kopra's rapidly-left-expansive class) realise an eventually period-2 or Sturmian column from a finite
  configuration? Two facts bracket it:
  - Kopra's Prop 3.3.5 says no for the p/q automata at width 1.
  - The Condrey preprint's remark (per earlier search results; [arXiv:2609.09431](https://arxiv.org/abs/2609.09431))
    says left-permutive Rule 90 does admit a zero centre trace.
  The answer would show whether left-permutivity plus finiteness is ever sufficient, and which extra property of
  Rule 30 (the OR latch) must enter.
- **Kopra's proof shape transferred to Rule 30 (inference, untested):** a period-2 column would need a
  "size"-decreasing leftward renormalisation, the analogue of σ⁻¹∘Π shrinking real(x). Rule 30 has no known
  arithmetic interpretation (the Kari–Kopra p/q setting has one). This is a concrete statement of what is missing,
  not a route.

### Gaps
- Not verified: whether any Tahay or Dolce–Tahay construction can be made left-permutive. Neither text discusses
  permutivity.
- The 2018 and 2023 Tahay papers were not read beyond their metadata.
- No thesis was found that treats eventual periodicity of a column as a function of the right half for a fixed finite
  left half, i.e. "left-finiteness vs right dynamics" stated as such.

## What does Powley's thesis prove that is relevant, and which theses does it cite or is it cited by?

### Takeaway
Powley's thesis is about global state spaces on *rings* (periodic boundary): symmetry, preimage counts through
de Bruijn/transfer matrices, and transition graphs. It does not study columns, traces or permutive rules, so for
Problem 1 its use is limited to finite-boundary preimage counting (as GC794 already found). Its bibliography cites one
other thesis (Wuensche's D.Phil). The citing literature could not be retrieved. The theses this assignment actually
needed were reached instead through Guillon's and Kopra's bibliographies.

### Cited Findings
- **Powley 2009** (230 pp.): global state space, symmetry, numbers of preimages, distances between successive states;
  Rule 30's de Bruijn matrices; transition graphs for all ECAs on Z_10 and Z_11. — [Powley
  PDF](https://www.cs.york.ac.uk/nature/group/theses/EdPowley.pdf);
  summary at [York thesis page](https://www-users.york.ac.uk/~ss44/teach/theses/powley.htm)
- PRIOR-ART GC794 already records the targeted reading: §4.3 Theorems 4.6–4.7, §9.2 Theorem 9.5, §9.3, §§7.5–7.6 and
  §§10.3–10.5. It concludes that "section 9.3 compresses a repeated spatial target… it does not address a lone
  temporally periodic column". I found nothing in the text (searched for permutive, Jen, Hedlund, trace) that changes
  this. — [Powley PDF](https://www.cs.york.ac.uk/nature/group/theses/EdPowley.pdf)
- **The one thesis Powley cites:** Wuensche, A., "Attractor basins of discrete networks", D.Phil thesis, University of
  Sussex, 1997 (from Powley's bibliography, [Wue97]; not opened). It concerns basins of attraction on finite rings.
  — [Powley PDF](https://www.cs.york.ac.uk/nature/group/theses/EdPowley.pdf)
- **Theses reached via other bibliographies** (not via Powley).
  - Guillon's bibliography cites:
    - **Moothathu, T. K. S., "Studies in Topological Dynamics with Emphasis on Cellular Automata", PhD, University of
      Hyderabad, 2006** (advisor V. Kannan). Metadata only. — [Stony Brook
      record](https://www.math.stonybrook.edu/2006-moothathu)
    - **Di Lena, P., "Decidable and Computational properties of Cellular Automata", PhD, Università di Bologna,
      December 2006.** The thesis itself was not found online. The derived paper "Decidable properties for regular
      cellular automata" (IFIP TCS 2006) proves regularity undecidable, but nilpotency, equicontinuity and positive
      expansiveness decidable for regular CA (abstract only). — [Guillon thesis
      bibliography](https://theses.hal.science/tel-00432058/document);
      [paper record](https://repositoriosdigitales.mincyt.gob.ar/vufind/Record/SEDICI_aca74153d7d7f87739780a2887314d35)
  - Kopra's bibliography cites Lukkarila's (Turku 2010) and Salo's (Turku 2014) theses, on reversible-CA
    undecidability and on subshifts. These were not examined, as they are off-topic by title. —
    [Kopra thesis PDF](https://www.utupub.fi/bitstreams/f229bc81-1590-4a47-9047-cc8113366378/download)
- **Checked and judged low relevance** (abstracts on theses.fr):
  - Delacourt 2011 (μ-limit sets; [theses.fr](https://theses.fr/2011AIX10131)).
  - Chemlal 2012 (eigenvalues of CA; [theses.fr](https://theses.fr/2012PEST1067)).
  - Lanthier 2020 (filtrations of algebraic CA; [theses.fr](https://theses.fr/2020NORMR034)).
  - Herrera Nuñez 2025 (generic/likely limit sets; [theses.fr](https://theses.fr/2025TLSES071)).
  - Maass 1994 (CA conjugate to SFTs, limit sets; [theses.fr](https://theses.fr/1994AIX22023); just before the date
    range).
  - Martin 2001 and Formenti 1998 (chaos classifications; [theses.fr](https://theses.fr/2001ENSL0177),
    [theses.fr](https://theses.fr/1998ENSL0093)).

### Inferences
- For mining further, Guillon's thesis is a better hub than Powley's. Its bibliography links the French trace school,
  the Bologna decidability work (Di Lena) and the Hyderabad topological-dynamics thesis (Moothathu).
- The Di Lena "regular CA" line connects directly to Kopra's open "Is W30 regular?". If Rule 30 were regular, Di
  Lena's decidability results would apply. Kopra's non-regularity of the p/q automata suggests otherwise for Rule
  30's class (inference, not proof).

### Gaps
- Works citing Powley's thesis are not identified (citation APIs rate-limited; Google Scholar not reachable from this
  environment).
- Moothathu's and Di Lena's theses were not obtained, so I do not know whether they contain trace or column results.
- Wuensche's D.Phil was not opened.
