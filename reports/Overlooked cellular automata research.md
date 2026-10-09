# Overlooked proofs pinpoint what period two lacks

The most valuable overlooked work is a complete theorem by Johan Kopra, first in his 2019 Turku doctoral thesis and then
in a sole-author 2021 *Theoretical Computer Science* paper with about four citations. It says that for the automata that
multiply by $p/q$, a **single column from a finite configuration is never eventually periodic**, and the proof takes
about fifteen lines. That is the period-2 question settled for Rule 30's nearest arithmetic siblings. The proof uses
exactly the project's two ingredients: the finite left side enters as a positive real number that keeps shrinking, and
the genuine dynamics enter as a width-one sideways map that pushes periodicity leftwards. PRIOR-ART.md lists the paper
at abstract level only, so it missed this proposition. Reading it shows precisely what Rule 30 lacks: its sideways map
has width two and is not invertible. The second find is unverified but would matter most if it holds. An independent,
agent-run GitHub repository, cochon123/rule30-prize, claims finite certificates that exclude every eventual centre
period of the form $0\,1^q$ for $q = 7$ and all $q \ge 9$, by the same Jen–Kopra mechanism, and it leaves period 2
($q = 1$) open. Its family is the project's own parked black-end walls, so it needs an audit before anyone uses it.
Doctoral theses by Pierre Guillon (2008) and Pierre-Adrien Tahay (2020) are absent from the record. Guillon's gives a
standard citation for the forced left half, and Tahay's gives a library of counter-models showing that finiteness alone
forces nothing. Mathieu Sablik's directional-dynamics theorem, combined with the survey's check that Rule 30 is not
right-closing, shows that the right side's genuineness cannot come from expansivity. The survey's own unpublished
derivation recasts Rule 30's right edge as the orbit of a 2-adic isometry (an odometer); it is a reformulation, not
progress, and needs a second reader. Nothing found proves period 2 or contradicts the record. "Overlooked" here means
absent from the record and barely cited. The evidence shows language, venue and discipline silos, not a measured bias
against students or independent researchers.

## Twelve finds rank above the noise, and only one is a finished proof

Four survey passes produced the material. The first covered independent Rule 30 work since the 2019 prizes. The second
covered adjacent-field tools from 1984 to 2015. The third covered theses from 1995 to 2026, and the fourth the
trace-and-column literature from 2005 to 2026. Each pass grepped PRIOR-ART.md for every author and a title word, and
each recorded how much of a source it actually read. Citation APIs were mostly blocked: Semantic Scholar returned HTTP
429 and OpenAlex's free quota was used up. So under-citation rests mainly on two things: absence from the project's
record, and the few counts that could be retrieved. Kopra's 2023 *Theoretical Computer Science* paper on Rule 30's
class, for example, has about two citations ([Semantic
Scholar](https://api.semanticscholar.org/graph/v1/paper/DOI:10.1016/j.tcs.2022.12.018)). The survey's Semantic Scholar
lookups of 9 October 2026 gave his 2021 paper about four, and the other trace papers between 0 and 11. The preprint
literature is thin. An exact-phrase arXiv search for "rule 30" in abstracts returns 15 entries in all, and almost every
one since 2019 is already in the record ([arXiv API
query](https://export.arxiv.org/api/query?search_query=abs:%22rule%2030%22&max_results=200&sortBy=submittedDate&sortOrder=descending)).
The diamonds are in theses, conference proceedings, GitHub and forum answers.

The ranking weighs three things together: what a work proves, how far a reader can check it, and how concretely it bears
on the period-2 programme. That programme rests on the record's insight that any proof must use both the finite left
side and the genuine Rule 30 evolution of the right side. "Class" in the table follows the three categories asked for:
**verified** (a published theorem whose proof the surveyors read, or a computation they re-ran), **derivation** (the
survey team's own unpublished working, marked OWN in the notes), and **unverified** (a claim by others that nobody here
has checked).

| Rank | Work | Authors' standing | Class | What it proves or claims | Checkable? | Use for period 2 | In PRIOR-ART.md? |
|---|---|---|---|---|---|---|---|
| 1 | Kopra, TCS 851 (2021), Props 2.7–2.8 and Lemma 3.17; thesis, Turku 2019, Props 3.3.4–3.3.5 | Doctoral student, then early-career sole author | Verified | One column of the $p/q$ automata is never eventually periodic from a finite configuration | High: an elementary 15-line proof, read in both versions | A template that uses both ingredients; it names the width-1 step Rule 30 lacks | Paper at abstract level only; thesis absent |
| 2 | cochon123/rule30-prize (2026) | Independent, agent-run | Unverified (the constant-tail part was checked by hand) | Eventual periods $0\,1^q$ excluded for $q=7$ and $q\ge 9$; period-2 onsets killed to width 28 | Low to medium: the scripts are public but were not run, and their scope is unstated | Same mechanism as the record's Proposition 7; covers the parked black-end walls; $q=1$ left open | Absent |
| 3 | Guillon, doctoral thesis, Paris-Est 2008 (in French) | Doctoral student | Verified | A width-$r$ trace reconstructs one side exactly when the rule is positively expansive on that side; entropy equals trace entropy | High; one convention unresolved | Standard citation for the forced left half; gives an entropy computation | Absent ("Ultimate traces" listed at abstract level) |
| 4 | Tahay, doctoral thesis, Lorraine 2020; Dolce–Tahay, DLT 2022; Marcovici–Stoll–Tahay, AUTOMATA 2018 | Doctoral student and small group | Verified | The Fibonacci word, quadratic-slope Sturmian words and binary 3-automatic aperiodic words occur as columns of quiescent CA from finite seeds | High (one proposition is only sketched) | Guard: finiteness plus quiescence forces nothing | Dolce–Tahay "snippet only"; thesis absent |
| 5 | Sablik, TCS 400 (2008), from his 2006 thesis | Then doctoral | Verified theorem plus survey derivation | Left-permutive rules have a half-line of left-expansive slopes; a right-expansive slope requires right-closing | Medium (signs reconstructed from the text extraction) | Rule 30 has no right-expansive slope, so ingredient 2 cannot come from expansivity | Absent |
| 6 | Coven–Pivato–Yassawi, PAMS 135 (2007) | Established, outside the Rule 30 literature | Verified theorem; the application to Rule 30 is a derivation | Left-permutive, memoryless CA with a fixed right tail have odometer orbit closures | Medium; the application was checked numerically | A rigid model of the genuine right-edge evolution | Absent |
| 7 | Kopra, MathOverflow answer 429509 (2022) | Forum answer | Partly verified | No Rule 30 configuration has minimal temporal period 2 | Medium: a ring count reproduces periods 1 to 4 | Consistency anchor | Absent |
| 8 | Jalonen–Kari, Fundamenta Informaticae (2020) | Doctoral student and advisor | Verified | Surjective, ultimately right-expansive CA with left pseudo-orbit tracing (POTP) have sofic traces | High, but whether the mirrored hypothesis holds for Rule 30 is unknown | Could give a finite automaton for the compatible column 1s | Absent |
| 9 | Goles–Guillon–Rapaport, traced communication complexity (arXiv:1102.3522) | Small group | Verified | Exact traced communication complexity for bipermutive CA; Ω(n) for five elementary CA | High; Rule 30 untreated | Would measure what the right half must "know" to hold 0101 | Absent |
| 10 | Math SE 4497595 and 4832480 (2022–23) | Independent users | Measurement | A single cell in a 0101 background fills part of its right side, at a ratio near 1.6241 | Medium; the constant is unexplained | A free measurement of the period-2 domain | Absent |
| 11 | DeepMind formal-conjectures `Rule30.lean`; a lemma in qizwiz/rule30-ski-research; a `decide` proof from The Last Math Competition | Large lab and independents | Formal | Canonical Lean statements of Problems 1 and 2; one left-permutivity lemma proved | High (checked by the Lean kernel) | Target for Lean versions of the record's lemmas | Absent |
| 12 | Litow–Dumas (1993); Coven (1980) and Blanchard–Maass (1996) | Older work by small groups | Verified (secondary sources only) | Columns of linear CA are algebraic, hence automatic; Coven's aperiodic family | Low (full texts unread) | Calibration: where superposition and aperiodic words enter | Absent (the converse, Rowland–Yassawi, is listed) |

cochon123 ranks second despite low verifiability because, if sound, it is the only find that would move a status row.
Coven–Pivato–Yassawi ranks below the theses because, applied to Rule 30, it repackages Jen's known right-diagonal
periods rather than adding a constraint (section 3). Below the table sit items with no period-2 bearing. Natal and
Al-saadi prove an $O(n^2/\log n)$ simulation bound that matters only as a Problem 3 baseline
([arXiv:2409.07065](https://arxiv.org/abs/2409.07065)). Hotanen's 2024 Turku thesis proves an entropy lower bound for
permutive rules over groups ([Hotanen
thesis](https://www.utupub.fi/bitstreams/94811642-f220-4598-8922-c94ddaff3ddc/download)). The Sfairopoulos–Garrahan spin
models built from Rules 30, 54 and 201 were read in abstract only
([arXiv:2503.19572](https://arxiv.org/abs/2503.19572)).

## Verified results: Kopra's width-one proof is the template, and Rule 30 breaks it at one step

**Kopra's Proposition 2.8** reads: "Let p > q. If x is a configuration that represents a positive real number (in
particular, if x is a finite configuration different from $0^{\mathbb Z}$), then $\mathrm{Tr}_{\Pi_{p/q,pq}}(x)$ is not
eventually periodic" ([Kopra 2021](https://arxiv.org/pdf/2005.05112)). The proof runs in four steps. Assume the column
is P-periodic. Proposition 2.7 gives a radius-1 cellular automaton on traces that maps column $i$ to column $i-1$, so
every column to the left is P-periodic. Since real($x_t$) = real($x$)/$q^{2t}$, a far-left column is eventually zero for
a whole period, hence identically zero. That bounds $(p/q)^t\,\mathrm{real}(x)$, which contradicts real($x$) > 0. The
thesis gives the same proof as Propositions 3.3.4 and 3.3.5, and two survey passes read it independently, one in each
version ([Kopra thesis](https://www.utupub.fi/bitstreams/f229bc81-1590-4a47-9047-cc8113366378/download)). Kopra places
it in Jen's lineage himself: "The same idea has been used for other cellular automata in [Jen, Physica D 45 (1990)]".
His thesis also records that in 2019 "it still seems to be an open problem whether TrW30(x) (the trace of width 1) can
be eventually periodic for some finite x ≠ 0Z", and it asks, as Problem 3.1.13, "Is W30 regular?" Each of the project's
ingredients has a counterpart in this proof. **Left-finiteness is the positive, shrinking real value**, a monotone size
functional that a periodic trace forces to vanish. **Genuine dynamics is the width-1 sideways map**, together with the
growth of $(p/q)^t$. Lemma 3.17 gives a second single-column proof by a different route, Diophantine approximation of
fractional parts. That route sits next to the record's Mahler framing in PERIOD-TWO.md §5.

**The step that fails for Rule 30 is the sideways width.** Reading Rule 30 from right to left gives
$c_{j-1}[t] = c_j[t+1] \oplus (c_j[t] \lor c_{j+1}[t])$, the formula in the record's Proposition 7. The survey writes it
as a map Ψ on pairs of columns. Ψ is a radius-1 cellular automaton on the time axis over the alphabet $\{0,1\}^2$, and
it is not invertible, because $c_{j+1}$ enters only through the OR. For the $p/q$ automata one column determines its
left neighbour. Rule 30 needs two, and that is exactly why Jen's theorem stops at adjacent pairs and why Proposition 7
needs column 1 to be periodic. The template therefore says what a period-2 proof must supply in place of the missing
width-1 step. One option is to show that 0101 forces column 1 into a set small enough for Kopra's Lemma 3.2 or
Morse–Hedlund. The other is to find a size functional that shrinks under Ψ the way real($x_t$) shrinks under
$\sigma^{-1}\circ\Pi$. The second option is the "size argument, like Chebyshev's" that PERIOD-TWO.md §5 expects. Kopra's
real($x_t$) is the one worked example of such a functional in Rule 30's class. One gap is open: nobody checked whether
Kopra's 2023 Theorem 3.5, at width $w = 1$, already contains Proposition 2.8. If it does, the new content is the
explicit proof and Lemma 3.17, not the statement.

**Guillon's thesis supplies the published general form of the record's pair map** ([Guillon
thesis](https://theses.hal.science/tel-00432058/document)). Its "retourné" (Proposition 4.6.8) turns the space-time
diagram a quarter-turn. A CA admits a one-sided retourné on its width-$r$ trace subshift exactly when it is positively
expansive of width $r$ on that side; in the thesis's words, one can "reconstruire tout le diagramme à partir du tracé de
largeur r" (rebuild the whole diagram from the width-$r$ trace). Fait 4.6.6 makes strongly left-permutive rules
positively left-expansive. Proposition 4.8.5 says such a rule's entropy equals the entropy of its width-$r$ trace. That
means the record's column-pair counts (§8.2) would measure Rule 30's topological entropy, for which no published value
was found. One caution: read naively with $r = 1$, Remark 4.6.9 would make Rule 30's width-1 trace (a full shift)
conjugate to its width-2 trace, which looks false. The radius and width convention must be checked first. Corollary
4.7.19 and Example 4.7.20 serve as a scope guard. Asymptotic periodicity is decided at the level of whole trace
subshifts, and preperiods need not be uniform there. That matches the record's finding that no constant bound governs
period-2 onsets, but it says nothing about one orbit.

**Sablik's cone theorem names the asymmetry the record already lives with.** By Example 3.4, a left-permutive rule with
neighbourhood $[r, s]$ has the open half-line $(-\infty, -r)$ of left-expansive slopes. Remark 5.2 says a nonempty set
of right-expansive slopes forces the rule to be right-closing ([Sablik
2008](https://www.math.univ-toulouse.fr/~msablik/article/2008-TCS.pdf)). The vertical therefore lies inside Rule 30's
left-expansive cone; this is the directional form of Kopra's dimensions (0, 1, 2). Add the survey's check that Rule 30
is not right-closing (section 3), and **Rule 30 has no right-expansive slope and no expansive slope at all**. In
dynamical-systems language this is the record's sentence "the column codes the left side but not the right". It also
forecloses one source for the second ingredient: the right side's genuineness cannot come from expansivity.

**Tahay's counter-models prove that finiteness alone forces nothing.** The thesis studies the sequences that occur as a
column of a 0-quiescent CA started from a finite configuration ([Tahay
thesis](https://hal.univ-lorraine.fr/tel-03184510/document)). It proves that the Fibonacci word and indicators of
integer-valued polynomials are such columns. Its binary recoding (Proposition 2.3.4) makes every binary 3-automatic
sequence, such as the indicator of $\{3^n\}$, a column of a 2-state CA, which answers a question of Rowland and Yassawi.
Dolce and Tahay add every Sturmian word of quadratic slope ([Dolce–Tahay](https://hal.science/hal-04066361/document)).
The constructions use only the columns to the right of column 0. Together they show that no argument of the form "finite
seed plus quiescent binary CA implies growing column complexity" can work. They also cite cleanly against PRIOR-ART.md's
"Theorem E (Sturmian columns excluded): NOT FOUND" row: Sturmian exclusion is false for CA in general, so the ingredient
that matters is Rule 30's own rule. The theses pass proposed a follow-up test: can a left-permutive CA realise an
eventually period-2 column from a finite seed? Cross-checking against the record shows that question is already answered
for three siblings. The record finds a counterexample in Rule 60 (§8.3), proves there is none in Rule 90 by Lucas'
theorem (Proposition 5), and proves there is none in Rule 210 (Proposition 19). The part still open is whether a
nonlinear member of Kopra's class other than Rule 30 admits one.

Four smaller verified items complete the picture. Jalonen and Kari prove that a surjective, ultimately right-expansive
CA with left pseudo-orbit tracing on a transitive subshift of finite type has a sofic width-$m$ trace for every $m$.
They also give an explicit reversible one-sided CA whose traces are not sofic
([Jalonen–Kari](https://www.utupub.fi/bitstreams/dc03c5fd-e559-4ba1-a8da-2ef685e8e0cd/download)). Mirrored, the theorem
would make Rule 30's width-2 trace sofic if Rule 30 had right pseudo-orbit tracing. That is unknown, and it bears on
Kopra's "Is W30 regular?". Goles, Guillon and Rapaport define the traced communication complexity of a centre-cell
evolution and compute it exactly for bipermutive rules, but they never treat Rule 30
([arXiv:1102.3522](https://arxiv.org/pdf/1102.3522)). A lower bound for the target trace $(01)^n$ would quantify how
much the right half must know. Cervelle, Formenti and Guillon's Rice theorem for traces makes every property stable
under ultimate coincidence undecidable as a class problem, which is no barrier to a single instance
([arXiv:1001.0251](https://arxiv.org/pdf/1001.0251)). Finally, Kopra's MathOverflow answer cites a table of preperiodic
points: for Rule 30 with preperiod 0 and periods 1 to 6 the counts are "3,0,12,28,45,84 and in particular there does not
exist a configuration with minimal period 2" ([MathOverflow
429509](https://api.stackexchange.com/2.3/questions/429509/answers?site=mathoverflow&filter=withbody)). A ring count
written for the notes reproduced 3, 0, 12, 28 for periods 1 to 4 over spatial periods up to 24. The source thesis behind
the table returned HTTP 403 and remains unidentified. The fact is a consistency anchor only: an eventually 0101 centre
cannot sit in a globally 2-periodic space-time, which Jen's theorem already implies for the neighbouring columns.

## Unpublished derivations recast the right side as a rigid 2-adic odometer

The survey team's own derivations are not literature. Short scripts checked them, the scripts were not committed, and no
second party has read them. Two passes arrived independently at the same identity. In the frame that moves with the
right edge, put bit $k$ of an integer $R_t$ at cell $t-k$. Then $R_{t+1} = R_t \oplus (2R_t \lor 4R_t)$, and the centre
column is bit $t$ of $R_t$, starting from $R_0 = 1$. That is the iteration of OEIS A269160's integer formula
$a(n) = n \text{ XOR } (2n \text{ OR } 4n)$ ([OEIS A269160](https://oeis.org/A269160)). Output bit $k$ is
$x_k \oplus f(x_0,\dots,x_{k-1})$, so the map is an invertible T-function, a measure-preserving isometry of the 2-adic
integers $\mathbb Z_2$. Every window is therefore purely periodic, with a period that is a power of two. **Unexpected
check of this synthesis:** the two passes printed identical periods of 1 mod $2^k$, namely 1, 2, 2, 4, 8, 8, 16, 32, 32,
64, 64, 64 for $k = 1$ to 12. Re-running the identity here confirmed it for every $t < 400$ and extended the table to
64, 64, 64, 128 at $k = 13$ to 16. The doublings match Rowland's right-diagonal indices with an index shift of one.

**Coven, Pivato and Yassawi's theorem turns this into an odometer.** Their Theorem 1 covers a left-permutive rule with
no memory. If an orbit is infinite and its right tail is fixed by the induced tail map, the orbit closure is conjugate
to an odometer. Their Theorem 4 makes the periods all equal to $p$ for local rules $t_0 + \theta(t_1,\dots,t_r)$ over
$\mathbb Z/p$ ([arXiv:math/0511030](https://arxiv.org/abs/math/0511030)). Rule 30 composed with a shift is
$x_i \oplus (x_{i+1} \lor x_{i+2})$, of exactly that form with θ = OR. The single seed's right tail $0^\infty$ is fixed
and its orbit is infinite, so by the survey's application the orbit closure is conjugate to the 2-adic odometer
$(\mathbb Z_2, +1)$. A further check, on 20,000 random 64-bit inputs, found that a 3-state Mealy automaton computes the
map. That opens the toolbox of automaton groups, though one search found no source on a Rule 30 automaton group. The map
is not ergodic: bit 0 is invariant, and mod 4 the cycles are {0}, {2} and {1, 3}. Each hypothesis has its place in this
frame. Left-permutivity is the invertibility of the right-edge map. The finite left side is the statement that $R_t$ is
an integer of exactly $2t+1$ bits. The record's counter-models, with infinite left halves or ring backgrounds,
correspond to no natural-number seed.

**The limit is that the odometer repackages what Jen and Rowland already proved.** Its windows are Jen's right
diagonals, whose power-of-two periods are known, and their rigidity is diluted exactly where the centre column lives.
The surveyors measured the period of the width-$k$ right-edge window. For Rule 30 its log2 grows like $0.4k$ (16 at
$k = 40$); for Rule 90 it grows like log2 $k$ (5 at $k = 40$). This report draws a tentative inference from those
numbers. A window of depth $k$ has repeated by time $t$ only if $2^{0.4k} < t$, that is, for $k$ below about 2.5 log2
$t$. The centre cell at time $t$ sits at depth $t$, inside the first period of its own window, so the odometer's
periodicity never acts on it. This fits the record's finding, in the entropy-squeeze review, that right-finiteness alone
cannot help. The 2-adic frame turns the second ingredient into p-adic dynamics. Anashin's van der Put criteria and the
cycle structure mod $2^k$ then apply to it. It does not supply a constraint on diagonal bits, and only such a constraint
would be progress.

The other derivations are smaller and also unpublished. A pair-graph search on Rule 30's de Bruijn graph found two
distinct left-asymptotic configurations with the same image and no right-asymptotic pair. So Rule 30 is left-closing but
**not right-closing**, which is the input to the Sablik conclusion above. A separate check fits: $0^\infty$ has two
preimages ($0^\infty$, $1^\infty$) and $1^\infty$ has three (the shifts of $(001)^\infty$), so by Hedlund's
characterisation of open maps (cited from memory in the notes) Rule 30 is not open. Under the uniform Bernoulli measure,
each new value of a single column is a fair coin given the past, because $F^t(x)_0$ is permutive in $x_{-t}$. Rule 30's
vertical entropy therefore lies between log 2 and 2 log 2, the upper bound from Tisseur's Proposition 5.3
([arXiv:math/0312136](https://arxiv.org/abs/math/0312136)). Rule 90 is bipermutative, hence expansive at the vertical
with positive entropy, yet its single-seed centre column is eventually 0. So system-level entropy and expansivity say
nothing about one finite orbit, which sharpens the record's existing remark. Rule 30's width-1 trace subshift is the
full shift, so a width-1 trace-subshift argument has nothing to work with, and all of Problem 1 lives in the particular
orbit. Finally, since $x_1 \lor x_2 = 1 \oplus [x_1x_2 = 00]$, Rule 30 in its one-sided frame is the complement of
Coven's map for the *periodic* word 00 ([Coven 1980](https://www.ams.org/proc/1980-078-04/S0002-9939-1980-0556638-1/)).
Coven's hypothesis excludes exactly that word, which makes his aperiodic family Rule 30's nearest calibrated one-sided
relatives. That comparison is untested.

## Unverified claims: one repository deserves an audit, and the full-solution claims do not

**cochon123/rule30-prize is the one independent project with substantive, auditable period claims.** Its README says
agents did the work, with a coordinating agent checking the arguments; nobody outside appears to have reviewed it
([repository](https://github.com/cochon123/rule30-prize)). Of its claims, one was checked by hand. A centre that is
eventually 1 forces column −1 to be eventually 0. A centre that is eventually 0 forces columns −1 and 1 to be equal and
column 1 to be non-decreasing, hence eventually constant. Either way two adjacent columns are eventually constant, which
contradicts Kopra's Corollary 3.7. So **period 1 follows in a few lines from Jen and Kopra**, for every nonzero
configuration with an eventually zero left half
([nonperiodicity.md](https://raw.githubusercontent.com/cochon123/rule30-prize/main/nonperiodicity.md)). The record
already holds both halves of that argument, Jen's theorem (Proposition 7, in Kopra's general form) and the monotone
latch beside a white wall, so this is a shortcut to write down, not a new result. The repository's period-2 local
relations also check out by hand. One relation appears to carry a label slip, in the repository or in the note's
transcription: what is written as $l_{t+1} = r_t \lor e_t$ should read $r_{t+1} = r_t \lor e_t$ at even $t$. With that
fixed, a zero of column −1 at an even time forces ones at the neighbouring even times. That is the record's own G240
no-11 premise, behind G256's three-quarters density bound, found independently. The onset kills, "every onset width
T=1..28", with "no uniform-in-T bound", confirm Condrey's $H(2,w) \ge w$ and the record's finding that no constant bound
governs period 2. They are confirmation, not a new lever
([research/LOG.md](https://raw.githubusercontent.com/cochon123/rule30-prize/main/research/LOG.md)).

**The isolated-zero family is the claim to audit.** The log states that "for q=7 and every q>=9, the radius-6 strip has
a unique recurrent component whose left neighbor is periodic, so Jen/Kopra exclude that eventual center". A 14-state
gadget handles $q \ge 17$, finite graphs handle $9 \le q \le 16$, the certificate script is "checked through q=40", and
"Period 9 (q=8) is a genuine exception"
([research/LOG.md](https://raw.githubusercontent.com/cochon123/rule30-prize/main/research/LOG.md)). Its open set is
$q \in \{1,\dots,6, 8\}$, the eventual periods 2 to 7 and 9 of this form. Cross-checking against the record shows that
this family **is the record's black-end wall $0\,1^{p-1}$ with $p = q+1$**, in the parked "two Condrey ends" row of
PERIOD-TWO.md §6. There the record holds exact records for $p = 3$ to 8, to 32 free bits, and finds that LR holds, which
is finite evidence only. If sound, the $q = 7$ certificate would settle the $p = 8$ wall, where the record has only
finite evidence, and $q \ge 9$ would close the family from period 10 on. The exceptions would then mark where "force
column −1 periodic, then apply Jen" stops working. That boundary is the period-2 obstruction seen from the black end.
The red flags are concrete. The certificates do not state whether the strip is a sound relaxation over all inputs or a
model of the single seed. Elsewhere the log warns that strip survivors are not claimed to extend to the single-seed
space-time. The scripts were not run here, and more than 700 pull requests were not inspected. A "16-state tail machine"
excludes the trace for an "eventually-zero Fibonacci u". It is conditional on an eventually zero right neighbour, which
Proposition 7 already excludes if that neighbour is column 1, and the meaning of "Fibonacci u" was not determined. Even
the most favourable reading leaves $q = 1$ untouched, so nothing here is prize-level.

Other independent work is smaller. wryan2986/rule30-lab labels one result "partial-proof", an "explicitly scoped
all-one-tail exclusion" in Lean 4. It reviews the Jen–Kopra width-two theorem "informally but [it] is not formalized in
Lean", and it says plainly that "no depth-independent state bound has been proved"
([repository](https://github.com/wryan2986/rule30-lab)). In qizwiz/rule30-ski-research, `left_boundary_full_sensitive`
(a cone-level form of left-permutivity) is proved without `sorry`. The same file leaves `all_cells_essential` as
`sorry`, and its `prize3_from_sensitivity` is vacuous: `omega` closes `n + 1 ≤ 2*n + 1` without using the hypothesis
([ConeStructure.lean](https://raw.githubusercontent.com/qizwiz/rule30-ski-research/master/lean_proofs/ConeStructure.lean)).
Dibujaron/rule30 is a harness that has agents prove Lean lemmas; its README says solving the prize questions "is not
expected" ([repository](https://github.com/Dibujaron/rule30)). The most usable formal asset comes from a large lab.
Google DeepMind's formal-conjectures states Problems 1 and 2 against fixed definitions, `centerColumn t = state t 0`,
with the left neighbour at `i-1`
([Rule30.lean](https://raw.githubusercontent.com/google-deepmind/formal-conjectures/main/FormalConjectures/Other/Rule30.lean)).
The Last Math Competition's conjecture 1243 was malformed and was disproved by `decide` on the square "11"
([conjecture](https://raw.githubusercontent.com/The-Last-Math-Competition/The-Last-Math-Competition/main/conjectures/00000001243.md)).
That proof does show `decide` evaluating Rule 30 prefixes inside the Lean kernel. On data, Xiangdong Wen's billion-bit
centre column in the Wolfram Data Repository is still the public record, and no independent re-verification by hash was
found ([billion
bits](https://datarepository.wolframcloud.com/resources/A-Billion-Bits-of-the-Center-Column-of-the-Rule-30-Cellular-Automaton)).
cochon123's linear-complexity profile sits near N/2 at 100 to 20,000 bits, as a random sequence's would, and excludes
periods 1 to 4,096 only for onsets at or before 95,902
([REPORT.md](https://raw.githubusercontent.com/cochon123/rule30-prize/main/REPORT.md)). For period 2, finite prefixes
rule out only early onsets, and the open case is a late one.

Two forum threads from independent users hold free measurements and open questions. Math SE user Trevor started a single
cell on a 0101 background, saw it "only expand to fill a portion of its right side", and conjectured a golden-ratio
limit. A follow-up found the ratio heading higher: "The 999000th computed value was 1.62414531", with no explanation and
no answer ([Math SE 4497595 and
4832480](https://api.stackexchange.com/2.3/questions/4497595;4832480?site=math&filter=withbody)). The same user asked
for an asymmetric rule with finitely many, but at least one, eventually periodic columns from an aperiodic start. That
is Kopra's page-7 barrier posed as a question, and its one answer is unread ([Math SE
4141181](https://api.stackexchange.com/2.3/questions/4141181?site=math&filter=withbody)).

The full-solution claims offer nothing to check. lba-brauer/rule30-symbolic-fsm marks all three prize questions "✅" from
"Gaussian statistics and Bernoulli analysis" of finite runs
([repository](https://github.com/lba-brauer/rule30-symbolic-fsm)). Das's 2022 preprint, already in the record, rests on
a heuristic "randomness count" ([arXiv:2207.13237](https://arxiv.org/abs/2207.13237)). The Wolfram Community thread
holds a medland post that gives no formula, a Nersissian prize submission with no confirmation, and Gallimore's year of
unpublished work ([thread](https://community.wolfram.com/groups/-/m/t/1802242)). Nersissian's Binomial–Lucas document
claims row theorems whose sections 6.2 to 9 are headings only, and it cites a placeholder "arXiv:submit/7289701"
([Wolfram Cloud](https://www.wolframcloud.com/obj/b04b6551-fecf-465d-b02d-63d95abd751c)). Wiles's "O(1)" cells inside
white triangles are fixed by local windows and say nothing about the cost of computing cell n
([blog](https://jameswiles.com/blog/Conditional-Patterns-in-Rule-30-and-Their-Implications-on-Computational-Reducibility.html)).
Two "workshop paper" drafts in a GitHub issue tracker, which disagree with each other, fit a preimage-growth constant
near 1.56 ([issue 153](https://github.com/deepseek-launch-community/XuanJi-ISA/issues/153)). Condrey's repository still
returns 404. Michael Brunnbauer's 2019 lemma, that right-diagonal periods never decrease, has now been read
([thread](https://community.wolfram.com/groups/-/m/t/1802242)). PRIOR-ART.md lists it as an empty search term, and its
content is subsumed by Jen's $2^\alpha$ right-diagonal periods and Rowland §5.

The notes mark what the record already holds, and none of it needs re-listing. That covers Condrey; Nersissian's two
arXiv papers; Kopra 2023 and arXiv:2202.13809, read in full; Kari–Kopra; Rowland 2006; Jen; Powley's thesis; Das;
Chan-López–Martín-Ruiz; Spencer's thesis; Meier–Staffelbach; Mariot's later survey; Shereshevsky; Tisseur 2000; Milnor
1988; Courbage–Kaminski; Kůrka; Rowland–Yassawi; Mahler and FLP; Boyle–Lee; Patto1155/rule30-foundry;
fabianxvogt/rule30; the woahwhattheheck issues; and openai/math. Two entries need upgrading rather than adding: Kopra's
arXiv:2005.05112, from abstract to full read with Propositions 2.7 and 2.8 and Lemma 3.17, and Dolce–Tahay, from
"snippet only" to full read.

## Seven next steps, by lane

The steps follow the owner's split: Local runs computations, GPT does reasoning and proof audits, and Cloud keeps the
record. Each step states what it decides and what to predict before it runs. None needs a new status-board row. Step 1
serves the parked "two Condrey ends" row, steps 2 and 4 serve Q1, and the side questions in step 7 belong in
CONSTELLATION.md.

| # | Step | Lane | What it decides | Prediction and counterfactual to register |
|---|---|---|---|---|
| 1 | Audit cochon123's `isolated_zero_uniform.md`, and rerun `isolated_zero_uniform.py` to $q = 40$; set the $q = 7$ certificate beside the record's exact black-end records for $p = 8$; then compare the radius-6 strip's recurrent components at $q = 1$ with the wheel | GPT audit; Local rerun | Whether an infinite family of eventual periods is excluded for every finite configuration, for the single seed only, or not at all | If the strip is a sound relaxation, every certificate for $q \ge 9$ reproduces and $q = 7$ agrees with "LR holds" at $p = 8$. A strip survivor at some $q \ge 9$, or an unsound boundary model, refutes the claim |
| 2 | Write Kopra's Proposition 2.8 into PERIOD-TWO.md §5 beside Proposition 7, map its two ingredients, and state the width-1 substitute as a named target; check whether Kopra 2023 Theorem 3.5 at $w = 1$ already contains it | GPT reasoning | Whether the record's "size argument" has a worked model, and what exactly it must replace | Expect Theorem 3.5 at $w=1$ to contain the statement but not Lemma 3.17's Diophantine route |
| 3 | Second-read the survey's derivations before anyone cites them: the T-function identity, the Coven–Pivato–Yassawi application, the not-right-closing pair graph, and the vertical-entropy bounds; file the ones that survive in PROOFS.md as reformulations with no novelty claim | Cloud or GPT | Whether the Sablik conclusion and the odometer frame can be cited | Expect all four to survive; the right-closing direction convention is the likeliest failure |
| 4 | Resolve Guillon's width convention against the §8.2 column-pair counts: do they grow like $2^n$ or faster? If Proposition 4.8.5 applies at width 2, they estimate Rule 30's topological entropy | Local (cheap) | Whether Guillon's thesis gives Rule 30's entropy, for which no published value was found | Expect growth faster than $2^n$, which would make the convention $r = 2$ and refute the naive reading of Remark 4.6.9 |
| 5 | Upgrade PRIOR-ART.md: add every row of the ranked table with its access level; upgrade Kopra 2021 and Dolce–Tahay; fill in Brunnbauer's content; cite Tahay in the Theorem E row; add Kopra's MathOverflow table | Cloud | Prevents the next survey re-finding these | None needed (record keeping) |
| 6 | State one record lemma (Proposition 7 or Theorem B) against DeepMind's `Rule30.lean` definitions; check a small finite certificate with `decide`; reuse qizwiz's lemma where it fits | Any, low priority | Whether the record's proofs can join the community's canonical target | Expect `decide` to handle prefixes of a few dozen steps but not depth-89 records |
| 7 | Side questions for CONSTELLATION.md: the Math SE 1.6241 constant against the record's 0.21 cells per step beside a clamped 0101; the unread answer to Math SE 4141181; a 2-kernel test of the odometer's coordinate functions; Coven's aperiodic family; the traced communication complexity of $(01)^n$; right pseudo-orbit tracing for Rule 30 | Parked | Each is a well-posed side question, not main-line work | Register each prediction when a row is opened |

## Conclusion

The literature already contains single-column, period-excluding proofs that use both ingredients, and each one works
only where Rule 30's period 2 does not reach. Kopra's needs width-1 sideways determinism. Jen's, Condrey's and the
Mahler-type arguments need the constrained side to be finite. cochon123's claim, if sound, needs a long black run to
force column −1 periodic. The 0101 wall defeats all three: Rule 30's sideways map has width two, column 1 beside the
wall has positive entropy, and the black run has length one. That is a sharper statement than "nobody has solved it". It
supports the record's bet on a counting or size argument, and it supplies the only worked example of the functional such
an argument needs: Kopra's shrinking real($x_t$), which has to vanish under a periodic trace. The odometer frame
explains, as a tentative reading of the survey's measurements, why the right side's rigidity cannot be borrowed
directly: it binds only within about 2.5 log2 $t$ cells of the right edge, far from the centre.

On who gets passed over, the evidence points to silos more than status. The best finds sat in doctoral theses (two in
French), in conference proceedings, and in a journal paper with about four citations. Two of the most useful structural
tools, Coven–Pivato–Yassawi and Sablik, come from established researchers who never mentioned Rule 30. The newest layer
is agent-run GitHub repositories, which now produce substantive, auditable certificates that nobody reviews, so the
project's second-reading discipline can supply that review. The best place to mine next is Guillon's thesis
bibliography, which links the French trace school, Di Lena's Bologna work on regular CA and Moothathu's Hyderabad
thesis. The next most valuable step is the audit in step 1, the only check here that could move a status row.
