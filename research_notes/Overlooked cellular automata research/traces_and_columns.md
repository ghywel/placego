# Traces, columns and vertical dynamics of one-dimensional CA; permutive rules and Rule 30 (under-cited work, 2005-2026)

Scope note for the report writer. Every item was checked against `PRIOR-ART.md` by grepping the author surname and a
title word. Items marked **[IN PRIOR-ART]** were already listed there. They are repeated only where this pass found
something new. **Access** says how much was actually read. "Full text read" means the PDF was downloaded and the
stated theorems were read in the extracted text. It does not mean every proof was audited line by line. Citation
counts come from Semantic Scholar on 2026-10-09; it undercounts, so treat them as rough evidence of under-citation.
DBLP (bot wall), OpenAlex (daily quota used up) and ScienceDirect (403 earlier, per PRIOR-ART) could not be used.

Two search-engine summaries were wrong and were not used. One said "Rule 30 is not permutive"; in fact Rule 30 is
left-permutive. The other credited a T-function paper to "Anashin, Khrennikov and Yurova", but the arXiv page lists
Shi, Anashin and Lin.

**Unexpected check of this work block (identified as such):** I took OEIS A269160's integer formula for Rule 30
and tested it against a direct simulation (script in the session scratchpad; run with `python3 -I`). The test shows
that Rule 30 from a single seed is the orbit of 1 under a 2-adic "T-function". The details are under Key Question
5. No published source making this link was found.

---

## Key Question 1: What is known about trace subshifts of CA (Cervelle, Formenti, Guillon, Gilman, Kůrka, Sablik, Di
Lena, Margara and students), and does any of it decide eventual periodicity of a column for permutive rules?

### Takeaway
The trace-subshift literature from 2007 to 2023 has two parts. The first, by the French-Chilean group around Cervelle,
Formenti and Guillon, characterises which subshifts can be traces and proves undecidability for whole classes. The
second, by the Turku group around Kari, Kopra and Jalonen, connects traces to expansivity and to arithmetic. **No
result decides whether one column of Rule 30 is eventually periodic.** The only single-column theorem found for a
permutive-type class is Kopra's Proposition 2.8 (TCS 2021), for the automata that multiply by p/q. It works because
there one column determines its left neighbour (a "sideways" map of width 1). Rule 30 needs two columns, which is
exactly where Jen's theorem stops.

### Cited Findings

**A. Cervelle, J., Formenti, E. and Guillon, P., "Sofic trace subshift of a cellular automaton"**, CiE 2007, LNCS 4497,
doi:10.1007/978-3-540-73001-9_16; arXiv:math/0703241. Not in PRIOR-ART. Access: full text read (sections 1 to 4 and the
statements of section 5). Semantic Scholar shows 11 citations.
- Definitions: the trace $T_F(x) = (F^j(x)_0)_{j\in\mathbb N}$ is column 0 of the space-time diagram. The trace subshift
  is $\tau(F) = T_F(A^{\mathbb Z})$, "a factor subshift of $(A^{\mathbb Z},F)$". A subshift is *T0* if it includes a
  2-SFT on the same alphabet — [arXiv:math/0703241](https://arxiv.org/pdf/math/0703241)
- Proposition 2: "The trace subshift of a CA is T0." The witness is $\varphi(a) = F({}^\omega a^\omega)_0$, the trace of
  the uniform configurations — [arXiv:math/0703241](https://arxiv.org/pdf/math/0703241)
- Theorem 3: "Any 2-SFT is traceable." Theorem 4: "A T1 subshift is k-traceable for some k." Theorem 5: "Any SFT is T1."
  Theorem 6: "Any T2 subshift is T1", where T2 means sofic and containing an infinite transitive subshift. Theorem 7:
  "Any T3 k-traceable subshift is traceable." Theorem 8: "Any T3+T1, T3 SFT, or T3+T2 subshift is traceable." The
  definition of T3 was not extracted cleanly — [arXiv:math/0703241](https://arxiv.org/pdf/math/0703241)
- Checkability: the proofs are short and constructive, with lemmas in an appendix. The paper concerns which subshifts
  arise as traces. It says nothing about the trace of a particular orbit.

**B. Cervelle, J., Formenti, E. and Guillon, P., "Ultimate traces of cellular automata"**, STACS 2010, LIPIcs 5;
arXiv:1001.0251; Dagstuhl PDF: https://drops.dagstuhl.de/opus/volltexte/2010/2451/pdf/1001.CervelleJulien.2451.pdf . Not
in PRIOR-ART. Access: section 2 statements and Theorem 5.6 with its proof read.
- Theorem 2.3, credited to Guillon and Richard (MFCS 2008): "A traceable subshift cannot be weakly nilpotent without
  being nilpotent." In words: if every column of every orbit eventually becomes 0, then a uniform bound exists —
  [arXiv:1001.0251](https://arxiv.org/pdf/1001.0251)
- Theorem 5.1: "The problem whether a spreading CA F is nilpotent is undecidable." —
  [arXiv:1001.0251](https://arxiv.org/pdf/1001.0251)
- Theorem 5.6 (a Rice theorem for traces): take any property of subshifts that (1) is satisfied by the trace subshift of
  some CA over {0,1} but not by all, and (2) is stable under ultimate coincidence. Then deciding whether $\tau_G$ has
  the property, given a CA G on {0,1}, is undecidable. The authors say this covers "fullness, finiteness, ultimate
  periodicity, soficness, finite type", nilpotency, and properties of the limit system's trace —
  [arXiv:1001.0251](https://arxiv.org/pdf/1001.0251)

**C. Guillon, P. and Richard, G., "Nilpotency and limit sets of cellular automata"**, MFCS 2008, LNCS 5162, 375-386, and
**Salo, V., "On nilpotency and asymptotic nilpotency of cellular automata"**, AUTOMATA & JAC 2012, EPTCS 90;
arXiv:1205.6714. Not in PRIOR-ART. Access: Guillon-Richard only through the citations above. Salo: abstract and
introduction read.
- Salo's abstract: "We prove a conjecture from [Guillon-Richard '08] by showing that cellular automata that eventually
  fix all cells to a fixed symbol 0 are nilpotent on $S^{\mathbb Z^d}$ for all d", and "weak nilpotency implies
  nilpotency in all subshifts and all dimensions" — [arXiv:1205.6714](https://arxiv.org/pdf/1205.6714)

**D. Goles, E., Guillon, P. and Rapaport, I., "Traced communication complexity of cellular automata"**, arXiv:1102.3522.
The arXiv version reads "Preprint submitted to Theoretical Computer Science"; the journal details were not verified. Not
in PRIOR-ART. Access: full text read (statements).
- The problem: "each of two players know half of some finite word, and must be able to tell whether the state of the
  central cell will follow a given evolution, by communicating as little as possible" —
  [arXiv:1102.3522](https://arxiv.org/pdf/1102.3522)
- Proposition 14: "For any bipermutive CA and any word $z\in A^{n+1}$, the multi-round CC of $\hat f_z$ is equal to
  $n\log|A|$." The paper adds: "The expansive elementary CA are exactly the four bipermutive ones (90, 150, 105, 165)."
  Corollary 18: "The CA 18, 26, 146, 154, 218 have a multi-round CC in Ω(n)." —
  [arXiv:1102.3522](https://arxiv.org/pdf/1102.3522)
- Proposition 13 gives a lower bound $nm\log|A|$ for expansive CA with expansivity speeds satisfying
  $m = 1/t^\to + 1/t^\leftarrow - 1 > 0$. The text notes "the same inequalities hold when the CA is permutive on one
  side and expansive on the other one" — [arXiv:1102.3522](https://arxiv.org/pdf/1102.3522)
- Rule 30 is not treated: no "30" appears in the extracted text. The conclusion leaves some rules "rather mysterious" —
  [arXiv:1102.3522](https://arxiv.org/pdf/1102.3522)

**E. Kopra, J., "On the trace subshifts of fractional multiplication automata"**, Theoretical Computer Science 851
(2021) 92-110, doi:10.1016/j.tcs.2020.11.010; arXiv:2005.05112. **[IN PRIOR-ART, abstract only]**. Upgraded here: full
text read for the statements below. Semantic Scholar shows 4 citations.
- **Proposition 2.7** (a sideways CA on traces): "There is a radius-1 CA
  $\Delta_{p/q}:\Xi(\Pi_{p/q,pq})\to\Xi(\Pi_{p/q,pq})$ such that
  $\Delta_{p/q}(\mathrm{Tr}_{i}(x)) = \mathrm{Tr}_{i-1}(x)$ for all x, i." So column i alone determines column i - 1 —
  [arXiv:2005.05112](https://arxiv.org/pdf/2005.05112)
- **Proposition 2.8** (single column, every period): "Let p > q. If x is a configuration that represents a positive real
  number (in particular, if x is a finite configuration different from $0^{\mathbb Z}$), then
  $\mathrm{Tr}_{\Pi_{p/q,pq}}(x)$ is not eventually periodic." The proof is about 15 lines. It assumes the column is
  P-periodic and uses Proposition 2.7 to make every column to its left P-periodic. Since $\mathrm{real}(x_t)$ shrinks, a
  later column becomes 0 on a whole period, hence identically 0. Then $(p/q)^t\,\mathrm{real}(x)$ is bounded, which
  contradicts $\mathrm{real}(x) > 0$. Kopra writes: "The same idea has been used for other cellular automata in [11]",
  where [11] is Jen, Physica D 45 (1990) — [arXiv:2005.05112](https://arxiv.org/pdf/2005.05112)
- Lemma 3.17 is a second single-column aperiodicity proof, for configurations whose rightmost nonzero digit lies in
  $\{np : 1\le n<q\}$. It works by approximating fractional parts:
  $\mathrm{frac}(\mathrm{real}(x_n)) - \mathrm{frac}((p/q)^P\mathrm{real}(x_n)) = O((q/p)^{nP})$ against a lower bound
  of $(pq)^{-(j+P)}$ — [arXiv:2005.05112](https://arxiv.org/pdf/2005.05112)
- Theorems 3.6 and 3.7: the trace is conjugate, via Φ, to a base-p/q numeration subshift $Y_{p/q}$. Theorem 3.15: the
  complexity is $P(n) = pq(p^{n-1}-q^{n-1})/(p-q) + p^n q$. Example 3.16: for 3/2 this is $4\cdot 3^n - 3\cdot 2^n$,
  giving 6, 24, 84, 276, 876. Theorem 3.18: $\Xi_{p/q}\cap\Sigma_p^{\mathbb Z}$ is not sofic. Corollary 3.19:
  $\Xi_{p/q}$ is not sofic, so $\Pi_{p/q,pq}$ is not regular in Kůrka's sense. Theorem 3.21: it is not synchronizing.
  Problem 3.20 asks whether every subshift factor of $\Pi_{p/q,pq}$ is coded —
  [arXiv:2005.05112](https://arxiv.org/pdf/2005.05112)
- The paper cites Jalonen and Kari: "there exists a reversible CA on a full shift which is left expansive ... and has a
  non-sofic trace subshift" — [arXiv:2005.05112](https://arxiv.org/pdf/2005.05112)

**F. Sablik, M., "Directional dynamics for cellular automata: A sensitivity to initial condition approach"**,
Theoretical Computer Science 400 (2008) 1-18 (author PDF:
https://www.math.univ-toulouse.fr/~msablik/article/2008-TCS.pdf). Not in PRIOR-ART. Access: section 5 read.
- Theorem 5.2: let F have neighbourhood [r, s] and let Σ be an infinite transitive subshift. A nonempty set of
  right-expansive directions has the form $]\alpha',+\infty) \subset\, ]-s,+\infty)$. A nonempty set of left-expansive
  directions has the form $(-\infty,\alpha''[\ \subset (-\infty,-r[$. The expansive directions form an interval
  $]\alpha',\alpha''[$ — [Sablik 2008](https://www.math.univ-toulouse.fr/~msablik/article/2008-TCS.pdf)
- Lemma 5.1 characterises one-sided expansivity of slope α by a finite coding condition. Remark 5.1 adds: "$r_T$
  corresponds to the radius of the transverse CA", citing Blanchard and Maass (Israel J. Math. 99, 1997) — [Sablik
  2008](https://www.math.univ-toulouse.fr/~msablik/article/2008-TCS.pdf)
- Rule 30 and permutive rules are not mentioned in the extracted text — [Sablik
  2008](https://www.math.univ-toulouse.fr/~msablik/article/2008-TCS.pdf)

**G. Di Lena, P. and Margara, L., "Computational complexity of dynamical systems: the case of cellular automata"**,
Information and Computation 206 (2008) 1104-1116, doi:10.1016/j.ic.2008.03.012. Not in PRIOR-ART. Access: repository
abstract only, through search. It classifies CA by "the language complexities which rise from the basins of attraction
of subshift attractors" — [Bologna repository record](https://cris.unibo.it/handle/11585/41739)

**Gilman and Kůrka (pre-2005, not read).** Gilman, R. H., "Classes of linear automata", ETDS 7 (1987) 105-118, and
Kůrka, P., "Languages, equicontinuity and attractors in cellular automata", ETDS 17 (1997) 417-433, appear in Sablik's
reference list. Kůrka's column subshifts are **[IN PRIOR-ART]** (cantor.pdf) — [Sablik 2008
references](https://www.math.univ-toulouse.fr/~msablik/article/2008-TCS.pdf)

### Inferences
- **What is decided, by scope:**
  - (i) All trace-subshift properties stable under ultimate coincidence are undecidable *as a class problem* (B). This
    is no barrier to a single instance such as Rule 30.
  - (ii) Width-w traces of rapidly left-expansive CA from left-finite configurations are never eventually periodic:
    Kopra 2023 and Jen, **[IN PRIOR-ART]**. For Rule 30, w = 2.
  - (iii) For $\Pi_{p/q,pq}$ one column is never eventually periodic (E, Proposition 2.8), because the sideways map has
    width 1.
  - Nothing decides one column of Rule 30.
- Rule 30's width-1 trace subshift is the full shift $\{0,1\}^{\mathbb N}$. This is my own standard argument from
  left-permutivity, not from a source. Take any column-0 sequence c and any right half. The columns ≥ 1 are then
  determined. Column −1 is forced by $x_t(-1) = c_{t+1}\oplus(c_t\vee x_t(1))$, and every column further left is forced
  the same way. So trace-subshift information at width 1 is empty for Rule 30. All the content of Prize Problem 1 lies
  in the particular orbit, which matches the team's insight that both the left side's finiteness and the right side's
  genuine evolution must be used.
- How E serves period 2: Proposition 2.8 is a complete, checkable model of a proof of the single-column problem for a
  sibling of Rule 30 in Kopra's class. Its two ingredients map onto the team's two required ingredients. The left side's
  finiteness becomes the shrinking of $\mathrm{real}(x_t)$; the right side's genuine evolution becomes the growth of
  $(p/q)^t$. The step that fails for Rule 30 is the width-1 propagation of periodicity, so a Rule 30 proof needs a
  substitute. One example: show that a period-2 column 0 forces column 1 into a set small enough that Kopra's Lemma 3.2
  or Morse–Hedlund applies.
- D's traced communication complexity formalises "left half and right half must jointly certify a given centre trace".
  For a period-2 target trace $z = (01)^n$, a lower bound on Rule 30's traced CC would quantify how much the right half
  must "know". This is a possible new angle, not yet tried; Rule 30 is not covered there.

### Gaps
- Gilman's 1987/88 papers and Kůrka's 1997 paper were not read (pre-2005, outside the window). Whether Rule 30 is
  "regular" in Kůrka's sense (all column subshifts sofic) was not found. Whether Rule 30's width-2 trace subshift is
  sofic was not found either.
- The full text of Guillon–Richard (MFCS 2008) was not read. Neither was Guillon's thesis (2008).
- I could not determine whether Kopra 2023's Theorem 3.5 explicitly recovers Proposition 2.8 with w = 1. The 2023 paper
  was read in full earlier by the project (PRIOR-ART), not in this pass.
- No work by students of Formenti, Kůrka or Margara on columns of *specific* permutive rules was found.

---

## Key Question 2: Who wrote the TCS (2022) paper "Rapid left expansivity, a commonality between Wolfram's Rule 30 and
powers of p/q" (pii S0304397522007502), what does it prove, and is there a full-text arXiv version?

### Takeaway
The sole author is **Johan Kopra** (University of Turku; PhD 2019 supervised by Jarkko Kari). It is **[IN PRIOR-ART,
read in full there]**. The journal version is Theoretical Computer Science 946 (2023) 113668,
doi:10.1016/j.tcs.2022.12.018, open access through the Turku repository. The arXiv version, under a **different title**,
is arXiv:2202.13809, "A natural class of cellular automata containing fractional multiplication automata, Rule 30, and
others" (v1, 28 Feb 2022, 12 pages). It has about 2 citations, which is strong evidence of under-citation.

### Cited Findings
- Semantic Scholar resolves doi:10.1016/j.tcs.2022.12.018 to "Rapid left expansivity, a commonality between Wolfram's
  Rule 30 and powers of p/q", Theoretical Computer Science, 2022, author Johan Kopra, 2 citations — [Semantic Scholar
  API](https://api.semanticscholar.org/graph/v1/paper/DOI:10.1016/j.tcs.2022.12.018)
- The arXiv abstract defines "rapidly left expansive cellular automata", a class containing "fractional multiplication
  automata, Wolfram's Rule 30, and many others". The definition was "shaped by a proposition of Jen on the aperiodicity
  of columns", which "generalizes to this class", and the paper "also presents results from the theory of distribution
  modulo 1" — [arXiv:2202.13809](https://arxiv.org/abs/2202.13809)
- The open-access full text (TCS version):
  https://www.utupub.fi/bitstream/handle/10024/174540/1-s2.0-S0304397522007502-main.pdf . The project's earlier full
  reading, recorded in PRIOR-ART.md, covers:
  - Def. 3.1: left expansive with dimensions (h, d, w); Rule 30 has (0, 1, 2).
  - Lemma 3.2: eventual p-periodicity of a width-w trace propagates one column to the left.
  - Theorem 3.5: for a rapidly left expansive rule of width w and any configuration whose left half is eventually zero,
    no width-w trace is eventually periodic.
  - Corollary 3.7: Jen's adjacent-columns theorem for every left-zero configuration.
  - Problem 3.10 and page 7: the class contains Rule 90, so it cannot settle the single column.
  - Section 4 (Theorem 4.5, Corollaries 4.6 and 4.9): right halves return exactly to their start only finitely often and
    have infinitely many limit points, generalising Pisot and Dubickas.
  - [Kopra TCS 2023 PDF](https://www.utupub.fi/bitstream/handle/10024/174540/1-s2.0-S0304397522007502-main.pdf)
- Kopra's PhD thesis is "Cellular automata with complicated dynamics" (Turku, 2019; TUCS article dissertation; eISBN
  978-952-12-3891-8). Its abstract covers multiplication automata, a generalised Mahler problem, uncomputability of
  Lyapunov exponents of reversible CA, and diffusive glider CA — [utupub handle
  11111/26292](https://www.utupub.fi/handle/11111/26292); [Math Genealogy](https://mathgenealogy.org/id.php?id=259088)

### Inferences
- Nothing new on the 2023 paper itself; the project already has it. The new and relevant find is its 2021 precursor (Key
  Question 1, item E), whose **Proposition 2.8 settles the single-column question for the p/q automata**. Read together,
  the two papers show exactly where the class argument stops for Rule 30: a sideways determinism of width 2 instead of
  1.

### Gaps
- No arXiv v2 matching the journal version was found. The journal PDF is open access, so this does not matter.

---

## Key Question 3: What has appeared in AUTOMATA proceedings (LNCS, EPTCS, 2008-2025), Journal of Cellular Automata,
Complex Systems, Natural Computing and Fundamenta Informaticae on columns, traces or Rule 30?

### Takeaway
The relevant venue papers are on traces and expansivity (Jalonen–Kari, AUTOMATA 2018 and Fundamenta Informaticae 2020),
on temporally periodic points (Dennunzio–Di Lena–Margara, AUTOMATA 2012 / EPTCS 90 and FI 2013, followed by
Allaoua–Chemlal 2023), and on the inverse problem of which sequences are columns (Marcovici–Stoll–Tahay, AUTOMATA 2018,
and Tahay's thesis). Plain Rule 30 is almost absent from these venues. The only Rule 30 items found are a Complex
Systems paper on a *memory* variant and an undergraduate statistics report. None of them proves anything about Rule 30's
centre column.

### Cited Findings

**H. Jalonen, J. and Kari, J., "On Expansivity and Pseudo-Orbit Tracing Property for Cellular Automata"**, Fundamenta
Informaticae (2020), doi:10.3233/FI-2020-1881. Expanded from AUTOMATA 2018, LNCS 10875 ("On dynamical complexity of
surjective ultimately right-expansive cellular automata"). Not in PRIOR-ART. Access: full preprint read (statements).
Semantic Scholar shows 0 citations.
- Abstract: "ultimately right (or left) expansive surjective cellular automata are chain-transitive". Left-sided POTP
  together with right-sided ultimate expansivity implies POTP, which "reproves some known results, most notably some of
  Nasu's" — [Turku repository PDF](https://www.utupub.fi/bitstreams/dc03c5fd-e559-4ba1-a8da-2ef685e8e0cd/download)
- Theorem 2: "Let $X\subseteq A^{\mathbb Z}$ be a transitive SFT and let (X, F) be a surjective ultimately
  right-expansive cellular automaton with left-POTP. Then F has POTP and $\tau_m(F)$ is a sofic shift for every m. If F
  is memoryless, then $\tau_m(F)$ is an SFT." — [Turku repository
  PDF](https://www.utupub.fi/bitstreams/dc03c5fd-e559-4ba1-a8da-2ef685e8e0cd/download)
- Proposition 11: "There exists a reversible one-sided cellular automaton whose traces are non-sofic." It is explicit: A
  = {0,1,2,3}, $F_{loc}(ab)=\rho_b(a)$ with $\rho_0=\rho_2=(0)(12)(3)$ and $\rho_1=\rho_3=(012)(3)$. Corollary 3 gives a
  reversible CA over a full shift with left-POTP whose trace is non-sofic — [Turku repository
  PDF](https://www.utupub.fi/bitstreams/dc03c5fd-e559-4ba1-a8da-2ef685e8e0cd/download)
- Jalonen's thesis "On some one-sided dynamics of cellular automata" (TUCS Dissertations 255, 2020): right-expansive CA
  are chain-mixing; conjugacy of one-sided CA is undecidable — [utupub
  10024/150371](https://www.utupub.fi/handle/10024/150371)

**I. Dennunzio, A., Di Lena, P. and Margara, L., "Strictly Temporally Periodic Points in Cellular Automata"**, AUTOMATA
& JAC 2012, EPTCS 90, 225-235, doi:10.4204/EPTCS.90.18; arXiv:1208.2770. Not in PRIOR-ART. Access: full text read
(statements). Semantic Scholar shows 4 citations.
- Proposition 3.2: equicontinuous surjective CA have a residual set of STP points. Proposition 3.3: almost
  equicontinuous surjective CA have a dense set. Proposition 3.4: "Let (A^Z, F) be a positively expansive CA. Then
  STP(F) is empty." Proposition 3.5: some sensitive CA has a dense set of STP points. For additive CA the set is dense
  or empty, and empty iff the CA is transitive — [arXiv:1208.2770](https://arxiv.org/pdf/1208.2770)
- FI extension: Dennunzio, Di Lena, Formenti and Margara, "Periodic Orbits and Dynamical Complexity in Cellular
  Automata", Fundamenta Informaticae 126(2-3) (2013) 183-199. For surjective CA, STP points have positive measure iff
  the CA is equicontinuous. Access: abstract only, through search — [HAL
  hal-01312658](https://hal.archives-ouvertes.fr/hal-01312658)
- Allaoua, N. and Chemlal, R. (Bejaia, Algeria), "Strictly periodic points and periodic factors of cellular automata",
  arXiv:2304.03860 (2023). STP points are "dense in the topological support of the measure" for CA with almost
  equicontinuous points. Access: abstract and statement list read — [arXiv:2304.03860](https://arxiv.org/pdf/2304.03860)

**J. Marcovici, I., Stoll, T. and Tahay, P.-A., "Construction of Some Nonautomatic Sequences by Cellular Automata"**,
AUTOMATA 2018, LNCS 10875, 113-126, doi:10.1007/978-3-319-92675-9_9; HAL hal-01824876. Not in PRIOR-ART. Semantic
Scholar shows 2 citations. Read together with **Tahay, P.-A., "Columns in cellular automata and generalized
Rudin–Shapiro sequences"** (PhD, Université de Lorraine, 2020; HAL tel-03184510). Access: thesis abstract, Proposition
2.3.4, Remark 2.3.5 and §2.4 read.
- The characteristic sequence of integer-valued polynomials and the Fibonacci word "can be realised as columns of
  non-linear cellular automata". Through a binary recoding, the thesis gives "explicitly a 3-automatic sequence on a
  binary alphabet, as a column of a cellular automaton with 2 states, that is not eventually periodic. This answers a
  question asked by Rowland et Yassawi." — [Tahay thesis](https://hal.univ-lorraine.fr/tel-03184510/document)
- Remark 2.3.5 (translated): if $u\in B^{\mathbb N}$ appears as a column of a CA on B from a *finite* initial
  configuration, and π: B → A is a letter-to-letter projection, then π(u) appears as a column of a CA on A from a finite
  initial configuration — [Tahay thesis](https://hal.univ-lorraine.fr/tel-03184510/document)
- Open questions in §2.4: k-automatic sequences for k not a prime power; the Tribonacci word; other non-automatic
  morphic words — [Tahay thesis](https://hal.univ-lorraine.fr/tel-03184510/document)
- Dolce and Tahay, "Column Representation of Sturmian Words in Cellular Automata" (DLT 2022, LNCS 13257) is **[IN
  PRIOR-ART, snippet only]**. Nothing new was found beyond "Sturmian word with quadratic slope ... in a chosen column",
  built via continued fractions — [Dolce publication
  list](https://fit.cvut.cz/en/faculty/people/5073-dr-francesco-dolce/publications)

**K. Rule 30 in the venues (low value).**
- Martínez, G. J., Adamatzky, A., Alonso-Sanz, R. and Seck-Tuoh-Mora, J. C., "Complex dynamics emerging in Rule 30 with
  majority memory", Complex Systems 18(3) (2009); arXiv:0902.2203. It builds Rule 30's de Bruijn diagram and studies
  gliders in a *memory-augmented* variant, not plain Rule 30. Access: abstract only, through search —
  [arXiv:0902.2203](https://arxiv.org/pdf/0902.2203)
- Gage, D., Laub, E. and McGarry, B. (faculty adviser K. Smith), "Cellular automata: is Rule 30 random?", 2005 Midwest
  NKS conference (an undergraduate research report). It runs statistical batteries and tabulates cycle structure on
  rings of width 5 to 24. The number of vertices on the maximal cycle trends as about $2^{0.928N-0.1017}$, and
  weaknesses are "isolated to even window sizes". There are no proofs. Access: full text read —
  [PDF](https://homes.luddy.indiana.edu/dgerman/2005midwestNKSconference/dgelbm.pdf)
- A targeted search found no *Journal of Cellular Automata* article on Rule 30 — [search, no
  hit](https://en.wikipedia.org/wiki/Rule_30)

### Inferences
- Jalonen–Kari Theorem 2 is the most usable new tool for the *trace-subshift* side. Mirrored, it reads: if a surjective,
  ultimately left-expansive CA with right-POTP exists, its width-m traces are sofic. If Rule 30 (left-permutive, hence
  left-expansive) satisfied the mirrored hypotheses, its width-2 trace subshift would be sofic. The set of column-1
  words compatible with a given column-0 word would then be recognised by a finite automaton. Whether Rule 30 has
  right-POTP is unknown to me. Even soficity concerns *all* configurations, so the left-finiteness of the single seed
  would still have to be imported separately.
- The STP literature (I) does not apply. Rule 30 is sensitive, being left-permutive, so it has no equicontinuity points,
  and it is not positively expansive. An STP point is in any case a stronger notion (the whole orbit periodic) than one
  eventually periodic column.
- The column-realisation work (J) gives the reverse lesson. Columns of finite-seed nonlinear CA can be eventually
  periodic, automatic or Sturmian by design, so any period-2 argument must use Rule 30's specific rule (its OR). This
  agrees with Kopra's Rule 90 barrier already in PRIOR-ART.

### Gaps
- The EPTCS AUTOMATA volumes other than 90, the Journal of Cellular Automata and Natural Computing were not browsed
  table of contents by table of contents. Search found nothing on Rule 30 columns there; that is a negative search
  result, not proof of absence.
- The volume and page numbers of the FI 2020 Jalonen–Kari paper came only from a search summary ("vol. 171, 2020, pp.
  239–259") and were not verified.

---

## Key Question 4: Are there results on "sideways" or "vertical" dynamics (time and space swapped) that apply to Rule
30?

### Takeaway
Yes, in three separate literatures that do not cite each other:
- the symbolic-dynamics "transverse CA" and directional expansivity (Blanchard–Maass 1997; Sablik 2008;
  Delacourt–Poupet–Sablik–Theyssier 2011);
- Kopra's sideways CA on traces (Proposition 2.7 above);
- the physics "space-time duality" programme (Klobas–Prosen 2020 on Rule 54; Garrahan's group in 2025 on spin models
  built from Rules 30, 54 and 201).

None of them treats Rule 30's sideways map explicitly. Written out, that map has width 2 and is not invertible, which is
where every existing sideways argument breaks.

### Cited Findings
- Kopra's Proposition 2.7: a radius-1 CA $\Delta_{p/q}$ maps the trace of column i to the trace of column i - 1 for the
  p/q automata. "A second implication of Proposition 2.7 is that to understand the dynamics of all trace subshifts ...
  it is sufficient to study the trace subshifts of width 1." — [arXiv:2005.05112](https://arxiv.org/pdf/2005.05112)
- Sablik: the radius $r_T$ of the coding in Lemma 5.1 "corresponds to the radius of the transverse CA (see [2])", where
  [2] is Blanchard and Maass, "Dynamical properties of expansive one-sided cellular automata", Israel J. Math. 99 (1997)
  149-174. One-sided expansive directions form open half-lines (Theorem 5.2) — [Sablik
  2008](https://www.math.univ-toulouse.fr/~msablik/article/2008-TCS.pdf)
- Directional dynamics along curves: Delacourt, Poupet, Sablik and Theyssier, TCS 2011 (arXiv:1001.5470). There is "a
  cellular automaton with an equicontinuous dynamics along a parabola, but which is sensitive along any linear
  direction." Access: abstract only, through search — [arXiv:1001.5470](https://www.arxiv.org/pdf/1001.5470)
- Klobas, K. and Prosen, T., "Space-like dynamics in a reversible cellular automaton", SciPost Phys. Core 2, 010 (2020);
  arXiv:2004.01671. For Rule 54, "the spatial evolution ... is governed by local deterministic maps", making it a
  space-time dual reversible CA. The spatial rule has larger support and acts on a reduced configuration space. Access:
  abstract only — [SciPost](https://scipost.org/SciPostPhysCore.2.2.010)
- Sfairopoulos, K., Causer, L., Mair, J. F., Powell, S. and Garrahan, J. P., "Spin models from nonlinear cellular
  automata", arXiv:2503.19572 (v4, 6 Apr 2026). It builds classical and quantum spin models "defined such that their
  ground states correspond to allowed trajectories of the CA" for rules 30, 54 and 201. The classical models are
  frustrated and "described by local defect variables". Semantic Scholar shows 3 citations. Access: abstract only —
  [arXiv:2503.19572](https://arxiv.org/abs/2503.19572)
- Blanchard and Maass (pre-2005, not read): a search abstract, whose author attribution was not confirmed, says
  permutive expansive one-sided CA are conjugate to one-sided full shifts — [search result: unpaywall
  10.1007/S002240000108](https://unpaywall.org/10.1007%2FS002240000108). Treat this as unverified.

### Inferences
- **Rule 30's sideways map.** This is my own one-line derivation from $x_{t+1}(j)=x_t(j-1)\oplus(x_t(j)\vee x_t(j+1))$,
  not from a source. It reads

```math
c_{j-1}[t] = c_j[t+1]\ \oplus\ \big(c_j[t]\vee c_{j+1}[t]\big),
```

so $\Psi(c_j,c_{j+1}) = (\sigma c_j\oplus(c_j\vee c_{j+1}),\ c_j)$.
  - Ψ is a one-sided (anticipating) radius-1 CA on the *time* axis, over the alphabet $\{0,1\}^2$.
  - It is not invertible: $c_{j+1}$ enters only through the OR.
  - It has width 2, against width 1 for Kopra's $\Delta_{p/q}$.
  - That is the precise sense in which Kopra's Proposition 2.8 argument does not transfer.
  - The period-2 problem becomes: can iterating Ψ leftwards from $(c_0, c_1)$, with $c_0$ eventually $(01)^\infty$, stay
    consistent with the left half being finite? The finiteness of the left half means column −k is 0 up to time k − 1,
    since the left edge moves at speed 1.
- The physics space-time duality literature has the computational technique for building a sideways rule's reduced
  domain (Klobas–Prosen). For Rule 30 that domain would be the width-2 trace subshift, whose soficity is unknown (Key
  Question 3).
- The "local defect variables" of the Garrahan-group spin model may correspond to the project's domain walls and
  particles (PRIOR-ART section "domains and particles"). This is a tentative link from the abstract only.

### Gaps
- The full texts of Blanchard–Maass (1997), Klobas–Prosen and Sfairopoulos et al. were not read. Whether the
  Sfairopoulos et al. classical Rule 30 model's defect variables coincide with Rule 30's left-permutive "forced"
  structure is unknown.
- No paper was found that studies Rule 30's (or any non-bipermutive left-permutive ECA's) transverse/sideways map as a
  dynamical system in its own right.

---

## Key Question 5 (objective e): Links between permutive CA and arithmetic (p-adic expansions, powers of p/q, Mahler's
3/2 problem, Collatz)

### Takeaway
The arithmetic line runs Kari 2012 → Kari–Kopra 2017 → Kopra 2021 → Kopra 2023, all **[IN PRIOR-ART]** except that Kopra
2021's single-column Proposition 2.8 was missed. One new and verifiable link was found, not in any source located: Rule
30 from one cell is the orbit of 1 under the 2-adic **T-function** $T(x)=x\oplus((x\ll1)\vee(x\ll2))$, and the centre
column is the diagonal bit sequence of that orbit. T-function theory (Klimov–Shamir; Anashin) then gives the known
power-of-two periods of Rule 30's right diagonals at once.

### Cited Findings
- OEIS A269160: "Formula for Wolfram's Rule 30 cellular automaton: a(n) = n XOR (2n OR 4n)". "The sequence is
  injective." It links to A110240, the Rule 30 iterates starting from 1 — [OEIS A269160](https://oeis.org/A269160)
- T-functions were introduced by Klimov and Shamir, "A New Class of Invertible Mappings" (2002). They are maps in which
  each output bit depends only on input bits at or below its position, and are used for ciphers and PRNGs — [Wikipedia:
  T-function](https://en.wikipedia.org/wiki/T-function)
- Shi, T., Anashin, V. and Lin, D., "Linear Relation on General Ergodic T-Function", arXiv:1111.4635 (2011): "linear (as
  well as quadratic) relations in a very large class of T-functions". Access: abstract only —
  [arXiv:1111.4635](https://arxiv.org/abs/1111.4635)
- A search for "T-function" together with "rule 30" found no source connecting them — [search, no hit; T-functions
  revisited, arXiv:1111.3093](https://ar5iv.arxiv.org/html/1111.3093)
- The project already holds the Mahler and Collatz automata: Kari (DLT 2012), Kari–Kopra (arXiv:1710.05737),
  Cloney–Goles–Vichniac (Complex Systems 1, 1987), Bruschi (arXiv:nlin/0502061), Akiyama–Frougny–Sakarovitch and
  Flatto–Lagarias–Pollington, all **[IN PRIOR-ART]**. Kopra 2021 adds Lemma 3.17, a column-aperiodicity proof by
  fractional-part approximation (Key Question 1, item E) — [arXiv:2005.05112](https://arxiv.org/pdf/2005.05112)

### Inferences
- **Unexpected check, computed this session (a measurement; the theory part is a standard derivation, not a sourced
  theorem).**
  - With T as above, bit n of $T^n(1)$ equals Rule 30's centre column for all n < 400: exact agreement with a direct
    simulation.
  - The binary length grows by 2 per step, so T is Rule 30 composed with a re-anchoring shift. Bit 0 is always the right
    edge, and the low bits are the right diagonals.
  - Output bit k of T is $x_k \oplus f(x_0,\dots,x_{k-1})$, so T permutes $\mathbb Z/2^k$ for every k. It is therefore a
    1-Lipschitz, measure-preserving bijection of $\mathbb Z_2$.
  - Hence $T^n(1) \bmod 2^k$ is *purely* periodic, and its period at most doubles from k to k + 1, so periods are powers
    of 2.
  - Computed periods of 1 mod $2^k$ for k = 1..12: 1, 2, 2, 4, 8, 8, 16, 32, 32, 64, 64, 64. The doublings at k = 2, 4,
    5, 7, 8, 10 match Rowland's a(n) = 1, 3, 4, 6, 7, 9 (PRIOR-ART) with an index shift of one.
  - T is not ergodic on $\mathbb Z_2$: it is the identity mod 2, and mod 4 its cycles are {0}, {2}, {1, 3}.
- What this could give period 2: it puts the right side's genuine evolution into p-adic dynamics. The right half's
  evolution is an orbit of a measure-preserving 2-adic isometry, and the centre column is that orbit read along a moving
  bit position, n at time n.
  - Anashin's machinery (van der Put / Mahler-series criteria for measure preservation and ergodicity on sub-balls)
    could describe the cycle structure of T on the balls the seed's orbit visits.
  - The left side's finiteness is the statement that $T^n(1)$ is an integer of exactly 2n + 1 bits.
  - A period-2 centre column would be a statement about the bits on the diagonal of a 2-adic orbit. This is tentative;
    it is a reformulation, not a proof route, until someone shows a constraint on diagonal bits.

### Gaps
- No literature was found treating Rule 30 (or its mirror, Rule 86) as a T-function. The identification should be
  second-read by another party before anyone cites it as new. It is probably folklore among OEIS contributors.
- Anashin and Khrennikov's book *Applied Algebraic Dynamics* (2009) and the van der Put criteria were not read here, so
  applicability is unverified.
- Nothing linking Rule 30 itself to Mahler's problem or Collatz beyond Kopra's class (shared rapid left expansivity) was
  found.
