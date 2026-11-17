# SW-01: the full objects for proposals 5, 7 and 9, the judges and the critic

*Committed at GPT's request (GC1256: "commit the full proposal/verdict objects for 5/7 and exact test source"). The swarm is RULE30-PRIZE.md 8.113 (JOB SW-01, `.claude/workflows/steer-out.js`). Readers ran on Fable 5.1; proposers, skeptics, judges and the critic on Opus 5.5. Proposal 9's skeptics, the judges and the critic were finished in a second run from the saved results (the critic read the readers' digest from a file outside git). Everything here is the output of sub-agents of one worker: single-party, a self-check, never a second read. The full raw run (journals, all ten proposals, the 134 status flags and their verdicts) stays outside git. Home paths are shortened to ~; nothing else is edited.*

## Proposal 5: A finite-automaton inductive invariant for the single orbit 2^n in base 3 (Erdős, the only Π_1 problem of the four)

#### title
A finite-automaton inductive invariant for the single orbit 2^n in base 3 (Erdős, the only Π_1 problem of the four)

#### lens
Inductive invariants and finite certificates for infinite safety properties: k-induction, IC3/PDR, regular model checking, and the busy-beaver closed-language ('finite automata reduction') deciders.

#### problem
Erdős's ternary conjecture: for n > 8, 2^n has a ternary digit 2 (CONSTELLATION.md:985-1035). I chose it because, under this lens, it is the only one of the four where a finite-state inductive invariant is type-correct. (1) Its prize-level statement is Π_1 (RULE30-PRIZE.md:6760, :7809): a safety property of ONE deterministic orbit, with a fixed step and a fixed bad set. (2) Rule 30's own inductive certificate already exists in the record and is blocked. GC970 (RULE30-GPT.md:23590-23629) uses regular languages I_0..I_C, closed under the inverse-column transduction, with a white-run counter, so it needs a bounded allowance C. The real record is not bounded in the data: R_real(147) = 18 and sampled R_real(1035) >= 38 (PERIOD-TWO.md:220). L556's witness rules out C17 (GC973, RULE30-GPT.md:23660-23671), and every widening tried loses the bound (GC974-GC977, :23673-23740). (3) Mahler and Collatz are Π_2 statements about every orbit terminating, so a certificate needs a ranking tied to the object's size. §8.61 finds that every potential named so far is Q1's counting potential (RULE30-PRIZE.md:4068-4092). Rule 30 and Mahler have Π_1 strengthenings, for example the doubling conjecture R(d) <= d + 4 (PERIOD-TWO.md:40). Those are families indexed by width, though, and their certificates must compare a run length with a depth, which needs a counter. Erdős needs no counter.

#### object_and_claim
Object: the doubling map D(x) = 2x on positive integers written in base 3. The single orbit is O = {2^n : n >= 9}, starting at 512 = (200222)_3. The bad set is C_fin = {x >= 1 : every ternary digit of x is 0 or 1}. The strong conjecture is exactly O ∩ C_fin = ∅. The small powers 2^1, 2^3, ..., 2^7 are 2, 22, 121, 1012, 2101, 11202, all containing a 2, and the exceptions are n = 0, 2, 8.

Lemma M (the maximal invariant; proved here, two lines, single-party). Let B = {x >= 1 : 2^k x ∈ C_fin for some k >= 0}. Then:
- the complement B^c is closed under D, because 2^k(2x) = 2^(k+1)x;
- every D-closed set I with I ∩ C_fin = ∅ lies inside B^c, because if y ∈ I then every 2^k y is in I and so none is 2-free;
- the strong conjecture holds if and only if 512 ∈ B^c.

Conjecture FA (the claim). There is a finite deterministic automaton A over {0,1,2}, reading base-3 digits least-significant first, whose accepted set I ⊆ N satisfies:
- (i) 512 ∈ I;
- (ii) 2I ⊆ I;
- (iii) I ∩ C_fin = ∅.
Equivalently, B^c contains a D-closed 3-automatic subset that contains 512. The certificate is the automaton A, and its width is the number of states N.

#### mechanism
1. From Π_1 to safety. A counterexample would be a finite computation, so the conjecture is the safety property 'the orbit of 512 under D never enters C_fin'. An inductive invariant (it contains the start, is closed under the step, and misses the bad set) proves a safety property outright. Once the closure check passes, no 'for ever' is left to prove.

2. Each certificate is checked by three exact automaton computations.
- (i) Run A on the string 200222.
- (ii) Closure. Breadth-first search over the product A × A × {carry 0, 1}, plus a flag for 'last digit nonzero'. On digit d with carry c, the first copy reads d, the second copy reads (2d + c) mod 3, and the new carry is floor((2d + c)/3). At the end of a canonical string, the second copy reads a final 1 if c = 1. A violation is a reachable end state where the first copy accepts and the second does not.
- (iii) Emptiness of A restricted to the digits {0, 1}, with last digit 1.
This is the busy-beaver 'finite automata reduction' certificate shape, applied to the one-rule machine x -> 2x. k-induction adds nothing: a regular property P that is k-inductive yields the regular D-closed set J_k = {x : P(2^i x) for all i < k}, since multiplication by 2^i is a finite transducer.

3. What A would have to do. These are the steps a skeptic should attack.
- (a) Low digits cannot do it. 2 is a primitive root mod 3^m (CONSTELLATION.md:991-993), so O meets every unit residue class mod 3^m.
- (b) Leading digits cannot do it. log_3 2 is irrational, so O contains every leading block.
- (c) The n-gram (strip) family fails at every width (proved here, single-party). An n-gram certificate must admit every n-gram of O. Those include every interior block: pick 2^k in the right unit class mod 3^(i+n). They also include the low block 1 0^(n-2) and every leading block. So the certificate accepts 1 + 3^M, which is in C_fin. This is the analogue of entry 38's strip graphs failing at q = 1 (PROOFS.md:1593-1594).
- (d) Local doubling cannot do it. On blocks of length l, doubling with carry-in 0 or 1 acts as x -> 2x and x -> 2x + 1 on Z/3^l. Because x -> 2x has finite order, these two maps generate x -> x + 1 and so act transitively. Hence no proper nonempty set of blocks is preserved position by position.
- (e) The single live step. A base-3 automaton can read 2-adic congruences: x mod 2^j is the digit sum against 3^i mod 2^j. So sets such as 512N and {x : x ≡ 2^n (mod 2^j)} are 3-automatic, D-closed and contain O. But every set built from congruence classes and 3-adic valuation classes meets C_fin. The reason: subset sums of powers of 3 hit every residue class modulo any m prime to 3, and the low digits can be fixed for the 3-part of m. So a certificate exists only if some D-closed 3-automatic language is not, up to finitely many elements, such a union (call it 'non-rigid'), and one such language contains 512 and avoids C_fin.

4. Relation to the record's theorems. The record's pair theorems are one-step closure obligations on the 3-adic Cantor set. Lagarias's Lemma 4.1 gives C ∩ M^(-1)C = {0} for M ≡ 2 mod 3 (PRIOR-ART.md:2663); for M = 2 it says that the double of a 2-free number always contains a 2. The sign rule of 8.110 is the power-map analogue. The automaton A would be their closure over all steps, aware of size as well as 3-adic digits, which neither the 3-adic picture nor the leading-digit picture can supply alone.

#### precedent
The bbchallenge collaboration's 2024 determination of BB(5), checked in Coq. Each non-halting 5-state machine is ONE deterministic object whose tape grows without bound. Most were proved non-halting by a finite inductive certificate: a regular language of tape configurations (an n-gram closed position set, or a finite automaton found by 'finite automata reduction') that contains the start configuration, is closed under the transition function and contains no halting configuration. A few machines needed proofs of their own.

What made it possible: those machines' reachable configurations have regular over-approximations that avoid halting (cyclers, bouncers, counters). Where it stops is the lesson. The BB(6) cryptids, such as Antihydra (which iterates floor(3n/2)), have no known regular invariant, because their non-halting is an arithmetic statement of Collatz type. The decider names and this account are from memory and not in the record.

Two in-record instances of the same shape:
- Entry 38 (PROOFS.md:1524-1594). Every real evolution is a path through the radius-6 strip graph, so the graph is an inductive abstraction. Each of its cyclic components forces a periodic neighbour column, and Jen's theorem with a clock then excludes every finite seed for the walls 0 1^q with q = 7 or q >= 9. It fails at q = 1, where a component forces neither neighbour (the 84-ring's strip, PROOFS.md:1593-1594).
- Kopra's p/q theorem (PRIOR-ART.md:2318-2323). One column of any nonzero finite configuration is never eventually periodic, proved with a shrinking real potential (a ranking) and a width-1 sideways map.

#### precedent_in_record
Partly.
- BB(5) is cited only as 'a reduction plus finite check' (PRIZE-PROBLEMS.md:122; RULE30-PRIZE.md:6734-6737, which adds that Antihydra 'stopped at our wall'). Its closed-language deciders are absent: record_find 'closed tape' gives 0 hits, and 'bbchallenge' gives 2 hits, both about Antihydra (RULE30-GPT.md:3446, PRIOR-ART.md:1491).
- Regular model checking appears once, as a survey item (RULE30-PRIZE.md:3029; PRIOR-ART.md:1506).
- The record's own inductive certificates are all for Rule 30: entry 38's strip graphs (PROOFS.md:1524-1594, reopened and closed for period 2 on the Q3 row, PERIOD-TWO.md:219) and GPT's GC970 counter certificate (RULE30-GPT.md:23590-23629). GC970's capped closure did not finish (GC973), and its widenings lost the bound (GC974-GC977).
- None was ever applied to Erdős. The record notes that Erdős is Π_1 (RULE30-PRIZE.md:6760, :7809) without using it.
- 8.113's prediction P3 names 'an inductive-invariant certificate (the model-checking shape)' as a likely survivor (RULE30-PRIZE.md:8014).
- No record hit for k-induction, PDR, interpolants, or a Cobham-type rigidity of ×2-closed automatic sets.

#### record_search
##### terms
- inductive
- k-induction
- IC3
- PDR
- interpolant
- closed tape
- Closed Tape
- bbchallenge
- regular model
- liveness
- BB(5)
- Coq
- automatic
- Cobham
- Stérin
- Pi_1
- regular language
- white-run counter
- multiplicatively independent
- Saye
- Kopra
- invariant set
- closed under

##### hits
- inductive: 38 hits in 13 files. Proof-step usages, plus 8.113's prediction at RULE30-PRIZE.md:8014. No invariant certificate for Erdős.
- k-induction: 0.
- IC3: 3 (substring noise in probe text).
- PDR: 0.
- interpolant: 0.
- closed tape: 0. Closed Tape: 0.
- bbchallenge: 2, both about Antihydra (RULE30-GPT.md:3446, PRIOR-ART.md:1491).
- regular model: 2 (RULE30-PRIZE.md:3029, PRIOR-ART.md:1506; the Lin-Rümmer survey item).
- liveness: 4 (the same survey item, plus unrelated REPAIRS hits).
- BB(5): 2, both spurious substring matches in probe hashes. grep finds PRIZE-PROBLEMS.md:122 and RULE30-PRIZE.md:6734.
- Coq: 2 (PRIZE-PROBLEMS.md:122, :153).
- automatic: 257 hits in 49 files, all about Rule 30 columns being non-automatic (T6) or linear CA. None on ×2-closed 3-automatic sets.
- Cobham: 2 (8.113's search line; PRIOR-ART.md:1498, a low-complexity item).
- Stérin: 3 (RULE30-PRIZE.md:7809, RULE30-GPT.md:31245, CONSTELLATION.md:985).
- Pi_1: 2 (RULE30-PRIZE.md:6760, :7809).
- regular language: 7. Includes GC970 at RULE30-GPT.md:23613, AFS non-regularity at PRIOR-ART.md:2547, and rule30_merge.py:86.
- white-run counter: 6 (GC970-GC972 and GC1119, all the Rule 30 RRL certificate).
- multiplicatively independent: 0.
- Saye: 17 (the Erdős free part; CONSTELLATION.md G.1, GC1240).
- Kopra: 97 (the p/q theorem at PRIOR-ART.md:2318-2323).
- invariant set: 7 (none on Erdős).
- closed under: 19 (8.109's admissible-prefix closure at RULE30-PRIZE.md:7628; none an inductive invariant for Erdős).
Verdict: the record applied inductive certificates to Rule 30 only, never to the one Π_1 problem.


#### route_to_prize
A certificate A gives 2^n ∈ I for every n >= 9, by induction on n using (ii). By (iii), no 2^n with n >= 9 is 2-free, so each has a ternary digit 2. With 2^1, 2^3, ..., 2^7 checked by hand, this is the strong conjecture: the exceptions are exactly n = 0, 2, 8.

The named sub-statement follows. If n ∈ E_k and n <= 1.58k < k·log_2 3, then 2^n < 3^k. So the last k ternary digits of 2^n are all of its digits, and avoiding 2 means 2^n ∈ C_fin, which forces n ∈ {0, 2, 8}. Hence E_k meets [0, 1.58k] only in 0, 2, 8 (CONSTELLATION.md:1022-1035; GC1241's exact criterion).

The certificate would be tier 1 once two independent implementations of the three checks agree, then stated in Lean. There is no cash prize: the question is 'a test bed, not a prize' (PRIZE-PROBLEMS.md:352). Nothing transfers to the three Π_2 problems.

#### kill_test
##### kills
Either of the following kills the route.
(1) A proof, or a theorem found in the literature, of Cobham-type rigidity: every 3-automatic set closed under x -> 2x agrees, outside a finite set, with a union of sets of the form {x : x ≡ a (mod m), v_3(x) = j} or {x : v_3(x) >= J}. Then any finite-state invariant containing O contains, cofinitely, a class {x ≡ 2^n (mod m)} with 2^n ≡ 1 (mod 3^b). C_fin meets that class infinitely often (elements 1 + 3^b·y with y chosen by subset sums of powers of 3), so no certificate exists.
(2) A weaker sufficient kill: a proof that every D-closed 3-automatic set containing infinitely many points of O meets C_fin.

##### confirms
An automaton passing the three exact checks. That is a proof of the strong conjecture, to be reimplemented independently and given a tier-2 read by GPT.
A weaker signal, which justifies a SAT search over larger automata: a D-closed 3-automatic language that is non-rigid on the units of 4N, meaning it contains infinitely many of them and misses infinitely many.

##### inconclusive_tips
HALT. If the bounded census finds no certificate and no non-rigid closed language at 3 states or fewer, stop. The local-transitivity fact (3d), the n-gram failure (3c) and the busy-beaver cryptids all predict exactly this null, so it gives no reason for a larger search.


#### bounded_test
##### description
An exhaustive census, standard-library Python only.
- The automata: every complete DFA with at most 3 states over {0,1,2}, initial state 0, with every accepting set. That is 2 + 256 + 157,464 = 157,722 automata. Digits are read least-significant first, and a positive integer is accepted if and only if its canonical string (last digit nonzero) is.
- The candidate set: for each automaton A, I = L(A) ∩ 4N. The value x mod 4 is tracked as the alternating digit sum, which adds 8 states.
- The search: exact breadth-first search on the product of A, a second copy of A reading 2x, the doubling carry, the mod-4 tracker and a last-digit-nonzero flag. That is at most 288 states, with early exit at the first violation.
- Computed per automaton: closed = [2I ⊆ I]; cert = closed and 512 ∈ I and I ∩ C_fin = ∅; nonrigid = closed and both I ∩ U and U \ I infinite, where U is the set of units (3 ∤ x) in 4N. Infinitude is decided by an accepting path through a cycle in the product with 'first digit nonzero'.
- Controls: the one-state accept-all automaton must be closed and fail (iii) at 4 = (11)_3. A hand-built automaton for {x : 3 ∤ x} must be closed and fail (iii). The automaton for 'lowest digit 1' must be reported not closed (x = 4 maps to 8 ≡ 2 mod 3).

##### quantity
The counts cert and nonrigid over all 157,722 automata, with the count of closed automata reported as a control.

##### cost
About 157,722 product searches of at most 288 states and 864 edges each. Most stop at an early violation, and swapping states 1 and 2 halves the work. Estimated 1 to 4 minutes on one CPython core, so under five minutes.

##### prediction
cert = 0 (probability 0.995 on its own) and nonrigid = 0. That is, every closed language at this size is rigid on the units of 4N: it accepts all but finitely many of them, or only finitely many.

##### probability
0.85


#### honest_weakness
The most likely failure is Cobham-type rigidity, which would make this the wall again. Closure under ×2 is 2-structure, and being recognised by a base-3 automaton is 3-structure. Cobham's theorem (1969) says a set that is automatic in two multiplicatively independent bases is eventually periodic. The analogue for 3-automatic sets closed under ×2 would make them unions of congruence and 3-valuation classes, and all of those meet C_fin. Facts (3a) to (3d) point that way. The busy-beaver experience agrees: regular invariants settled the structured machines and stopped exactly at the arithmetic cryptids (Antihydra, floor(3n/2)), whose behaviour is Erdős's own kind.

If rigidity holds, the outcome is a clean no-go: no base-3 finite-automaton inductive proof of the conjecture exists. That only restates the wall in automata terms. The known theorems that separate 2-structure from 3-structure control sparse or doubly structured sets: Cobham's theorem, and Senge-Straus for boundedly many nonzero digits (RULE30-PRIZE.md:6913-6921). Erdős pits the sparse orbit {2^n} against C_fin, which has entropy log 2 per digit.

Two further limits. Even a non-rigid closed language would be only a first step: the certificate must still beat the heuristic (2/3)^(0.63n) deterministically. And the route reaches only Erdős, which carries no prize money.

### Skeptic on the record, proposal 5

#### refuted
False

#### confidence
0.6

#### reason
Through the record lens, none of (a) to (d) clearly holds. (a) No closed route covers a finite-automaton inductive invariant for Erdős. Every closed-route list is about Rule 30 or Mahler. The nearest closure, Q3's machine-found certificate, is for Rule 30 and says it may be reopened when another finite family is named; this proposal names one. (b) The record never tried this route, so it was never found to be a set statement in disguise. S10's objection is that 2-adic or 3-adic avoidance cannot tell integers from non-integers. A DFA that accepts canonical finite strings is an ingredient that only integers have, and the proposal's own points (3a) and (3b) concede the 3-adic and leading-digit obstructions. (c) Holds only in part. The record cites BB(5) only as a "reduction plus finite check". It notes that the busy-beaver effort stopped at the wall with Antihydra, and it puts Erdős and Antihydra in the same skeleton, where only cases with an eventually periodic constrained side are solved. It says Cobham-type results work only at low complexity. That weakens the proposal's claim that the Π_1 form is what makes a certificate fit: Antihydra's non-halting is also Π_1, and Stérin-Woods makes Erdős the non-halting of a 15-state Turing machine. But the record never explains why closed-language certificates fail for Erdős in particular. Its reason against regular model checking (the certificate must scale with width, from Condrey) is specific to Rule 30. (d) The test's quantities (counts of closed, certificate and non-rigid DFAs with at most 3 states) appear nowhere in the record. The proposal's citations that I checked are accurate.

#### evidence
SEARCHES RUN (record_find, one term per call, hit counts as printed):
- 'inductive invariant': 1 hit, CHAT-LEDGER.md:3825, which is only SW-01's list of lenses.
- 0 hits each: 'k-induction', 'interpolant', 'n-gram', 'finite automata reduction', 'regular invariant', 'automatic set', 'x2-closed', 'closed under multiplication', 'Dupuy'.
- 'Cobham': 2 hits (RULE30-PRIZE.md:8003, PRIOR-ART.md:1502).
- 'automaton': 283 hits, all on Rule 30, Rule 210 or channel automata. None is an Erdős certificate.
- 'busy beaver': 7 hits. 'Antihydra': 26 hits. 'hold set' and 'finite-hold' also searched.
- Erdős probes in the tree are only erdos_cloud_ternary_support.py, ternary_cloud_converse_review.py, ternary_gpt_power_converse.py and lifting_cloud_multipliers.py. None is an automaton census.

(a) CLOSED ROUTES:
- RECORD-MAP.md:335-362 and PERIOD-TWO.md:107-130 are all Rule 30.
- The Q3 machine-certificate closure (RECORD-MAP.md:357-359; PERIOD-TWO.md:219) says "Reopen only with another named finite family".
- RULE30-PRIZE.md:4087-4093 withdrew 8.61's claimed impossibility ("a statement about the candidates in hand, not an impossibility").
- MAHLER.md:184-189's closed routes (product-formula coupling, the bowtie) are unrelated.
- CONSTELLATION.md G.1 (980-1035) has no certificate route, open or closed.

(b) S10:
- INSTINCT-CLOUD.md:123-130: avoidance across K "cannot single out an integer ... would need an integer-only ingredient beside it". The proposal's DFA acceptance on canonical strings is such an ingredient.
- The sign rule is "a pair statement, not a proof that one exception is impossible" (RULE30-PRIZE.md:7853-7856). The proposal cites it as one-step context only, not as the mechanism.

(c) PARTIAL:
- BB(5) appears only as a reduction plus finite check (PRIZE-PROBLEMS.md:118-125).
- 8.100 verdict: "the most complete code-and-proof effort stopped at our wall" (RULE30-PRIZE.md:6729-6734). Also "BB(5) is settled and Antihydra, at 6 states, is open. Where provability gives out between those is unknown" (RULE30-PRIZE.md:6759-6761).
- Antihydra is "a Mahler-family question ... there is no proof" (PRIOR-ART.md:1495-1497).
- Erdős and Antihydra share the decoupling skeleton, and "the solved cases are those where the constrained side is eventually periodic, and the open case is positive entropy" (PRIZE-PROBLEMS.md:207-211).
- Stérin-Woods: a 15-state, 2-symbol Turing machine halts if and only if Erdős's conjecture is false (CONSTELLATION.md:986-987). So Erdős has the same logical type as Antihydra's non-halting.
- Low-complexity rigidity, Cobham included, "works only when the complexity is low" (PRIOR-ART.md:1502-1503).
- Regular model checking is cited for Rule 30. Its stated reason for not transferring is Condrey's width scaling (PRIOR-ART.md:1510-1514; RULE30-PRIZE.md:3033-3037), which does not apply to a single orbit.
- The nearest in-record finite-certificate precedent is Stephan's Thm D. Block certificates are complete only on finite hold sets, Mahler's window has an infinite hold set, and "the integer side is the crux" (PRIOR-ART.md:2575-2576, 2586-2590; MAHLER.md:51). The Erdős analogue is the proposal's (3a), and the DFA does aim at the integer side.
- 8.113's P3 predicts that an inductive-invariant certificate is a likely survivor (RULE30-PRIZE.md:8012-8014).
- 8.101's verdict, bounded complexity only (RULE30-PRIZE.md:6913-6921), names rigidity theorems. It does not name inductive invariants.

(d) The record has no DFA census of any kind for Erdős.
- The free-part fact used in (3a) is already in the record: CONSTELLATION.md:989-993, PROVED with GC1240.
- The m_k table is exploratory, and its producer is not committed (CONSTELLATION.md:1015-1022).

CITATIONS VERIFIED:
- PRIOR-ART.md:2663 (Lagarias Lemma 4.1: C ∩ M^(-1)C = {0} for M = 2 mod 3, infinite for M = 1 mod 3).
- PRIOR-ART.md:2318-2323 (Kopra: shrinking real potential plus a width-1 sideways map).
- PROOFS.md:1593-1594 (entry 38 fails at q = 1, the 84-ring's strip).
- PERIOD-TWO.md:220 (R_real(147) = 18, R_real(1035) >= 38).
- RULE30-GPT.md:23590-23629 (GC970) and 23660-23740 (GC973-GC977).
- PRIZE-PROBLEMS.md:352 ("a test bed, not a prize").
- RULE30-PRIZE.md:6760 and 7809 (Erdős is Π_1).

#### what_would_rescue
The proposal is not refuted on the record lens. To survive the other lenses and its own partial-(c) exposure, it should add the following.
(1) Replace "Π_1 makes the certificate type-correct" as its discriminator. Antihydra's non-halting is also Π_1, and Stérin-Woods makes Erdős a 15-state TM non-halting (CONSTELLATION.md:986-987; RULE30-PRIZE.md:6729-6734). So it must say what structural feature separates the 2^n orbit from the cryptids where regular invariants stopped. It should also check, from a primary source, whether the bbchallenge closed-language deciders were ever run on the Stérin-Woods machine, since those deciders are this exact search.
(2) Add 'Stephan' and 'hold set' to its Record searched line. It should state the Erdős analogue of Stephan's Thm D (PRIOR-ART.md:2575-2576, 2586-2590): one-place 3-adic certificates are obstructed because O is dense in Z_3^× and C ∩ Z_3^× is infinite. It should then show that terminal acceptance on finite strings escapes that obstruction, which is the "integer side is the crux" point.
(3) Correct the honest weakness. "Closed under ×2 is 2-structure" is doubtful: multiplication by 2 is a finite transducer in base 3, which the closure check itself relies on. So closure under ×2 is a 3-automatic property, and classical Cobham-Semenov does not apply directly. The kill test then needs a different rigidity statement, or a literature search for multiplicatively closed automatic sets, before the (3e) null can be read as the wall.
(4) Record now that a null from the bounded test (at most 3 states) is uninformative under its own HALT rule, so the record does not over-read it as a no-go.
(5) If the m_k margin is used, commit its producer, per the comb note at CONSTELLATION.md:1015-1016.

### Skeptic on the mathematics, proposal 5

#### refuted
True

#### confidence
0.8

#### reason
Criteria (d), (c) and (b) apply. Conjecture FA itself is not disproved. (d) The bounded test cannot tell FA from its negation. I ran it exactly as specified, and it took 1.6 s rather than the 1 to 4 minutes estimated. The result is cert = 0 and nonrigid = 0, with all three controls behaving as specified. The proposal's own HALT clause says this null is what FA and not-FA both predict at 3 states, so it settles nothing. The 'nonrigid' signal is also mis-specified. It fires on congruence unions that provably meet C_fin, for example {x : x mod 7 in {1,2,4}}. A 3-state automaton cannot represent such structure at all, so the zero is structural, and a positive at larger sizes would not show non-congruence structure. Kill (1), as written, is false. N \ {3^j, 2*3^j} is closed under doubling and 3-automatic, yet it is not equal, outside a finite set, to any finite union of the named classes. So the 'clean no-go' kill can never be proved in that form. (c) The whole content of the route is the existence of A. Steps 3a to 3e rule out every structure the proposal can name. The only remaining class ('non-rigid') is defined as the negation of a rigidity statement that is false as written. No mechanism suggests a regular invariant exists. (b) The BB(5) closed-language deciders work on machines whose reachable configurations are essentially regular. That ingredient is absent here: {2^n} is not 3-automatic, by Cobham (1969), because it is 2-automatic and not eventually periodic. By the proposal's own account, regular invariants stop at exactly this arithmetic kind (Antihydra), and the record agrees.

#### evidence
COMPUTED (standard-library Python, under 60 s, nothing written to the repo):
- I ran the proposal's census over all 157,722 complete DFAs with at most 3 states over {0,1,2}, reading least-significant digit first, with I = L(A) ∩ 4N. I tracked mod 4 by the alternating digit sum.
- Product BFS (state of A on x, state of A on 2x, carry, x mod 4, position parity, last-digit-nonzero flag) gave: closed = 59,152; cert = 0; closed, avoiding C_fin∩4N and containing 512 = 0. Run time 1.6 s.
- Controls: the 1-state accept-all automaton is closed and meets C_fin∩4N (at 4 = (11)_3). The automaton for 3 ∤ x is closed and meets C_fin. The automaton for 'lowest digit 1' is not closed. All match the specification.
- Infinitude test: I collected accepting states at layers 48 to 95, using the pumping bound on a product of 48 states over unit strings in 4N. Result: nonrigid = 0. Also, 0 closed languages avoid C_fin∩4N while containing infinitely many units of 4N.
- So the test's predicted outcome is already in hand, and by the proposal's own HALT clause it is uninformative.

KILL (1) IS FALSE AS STATED:
- Let J = N \ {3^j, 2*3^j : j >= 0}. Its language is the canonical strings with at least 2 nonzero digits, which is regular.
- J is closed under doubling: 2x = 3^j is impossible, and 2x = 2*3^j forces x = 3^j, which is not in J. Checked: 0 violations for x < 2*10^5.
- J meets every class v_3(x) = j cofinitely. Any finite union of the named classes that does the same must contain some {v_3 >= J0}, which contains every 3^j with j >= J0. So J differs from every such union on an infinite set.
- J meets C_fin (4 is in J), so it does not threaten FA. But the stated rigidity theorem cannot be proved, and the kill must be restated, for example restricted to units or to the part of the set containing O.

'NONRIGID' SIGNAL MISCALIBRATED:
- I7 = {x : x mod 7 in {1,2,4}} is closed under doubling (checked mod 7) and contains every 2^n (checked n < 200).
- Among the units of 4N below 2*10^4, I7 contains 1,429 and misses 1,904. So it is 'nonrigid' in the proposal's sense.
- Yet it is a congruence union and meets C_fin: 1, 4, 9, 30, 36, ..., and inside 4N: 4, 36, 120, 256, 324.
- It needs more than 3 states, so a positive 'weaker signal' at the larger sizes the proposal would SAT-search would be spurious.

RECORD:
- Erdős is Π_1, with no safety net for the other three (RULE30-PRIZE.md:6760-6762).
- The BB effort 'stopped at our wall' at Antihydra (RULE30-PRIZE.md:6735-6737).
- Cobham-type results 'work only when the complexity is low' (PRIOR-ART.md:1502). The proposal cites this as :1498, which is drift.
- Single-object rigidity theorems control only bounded complexity, Senge-Straus for Erdős included (RULE30-PRIZE.md:6913-6921).
- Entry 38's strip certificate fails at q = 1 (PROOFS.md:1593-1594).
- The free part is exact and the obligation is the one object's own size (CONSTELLATION.md:991-997 and the G.1 restatement).
- Lagarias's Lemma 4.1, C ∩ M^(-1)C = {0} for M ≡ 2 mod 3, is a one-step multiplication statement (PRIOR-ART.md:2663).
- 8.113's P3 predicted this lens would survive (RULE30-PRIZE.md:8014). The census instead returns the predicted null.

STEPS CHECKED AND FOUND CORRECT:
- Lemma M (the complement of B is closed under doubling and is the maximal invariant).
- 3d (2x and 2x+1 generate x+1 on Z/3^l, since doubling has finite order).
- The closure-check details: the final carry digit, and canonical output when the carry is 0.
- Route logic: an A satisfying (i) to (iii) would prove the strong conjecture.

#### what_would_rescue
1. Restate the kill correctly and try to prove it, which would be a genuine theorem even as a no-go. A candidate: 'every doubling-closed 3-automatic set containing infinitely many units contains, outside a finite set, a full class {x ≡ a (mod m)} with a ≡ 1 (mod 3^b).' A route is a Furstenberg/Cobham-type argument: a finite 3-kernel plus invariance under doubling. This amounts to kill (2). Proving it closes the automaton route for good. Finding it false gives the first non-congruence structure worth searching.
2. Replace the 'nonrigid' signal with one that congruence unions cannot trigger. The right weaker object is any doubling-closed 3-automatic set that contains infinitely many units and avoids C_fin, without requiring 512. That count is 0 at 3 states or fewer. Search for it with SAT at 6 to 12 states, with the mod-2^j tracker built in. If no such set exists at any size, FA is dead.
3. Give a concrete reason why a regular over-approximation of the non-automatic orbit {2^n} could avoid C_fin, a set of entropy log 2 per digit present at every scale. The BB analogy supplies none: its successes were orbits with essentially regular configuration sets.
4. Report the census as done (null) and do not spend the work block re-running it.

## Proposal 7: Erdős as a safety property: an automaton invariant closed under x4 would prove that 4^m always has a ternary 2, and if none exists, Erdős is unprovable by automatic induction

#### title
Erdős as a safety property: an automaton invariant closed under x4 would prove that 4^m always has a ternary 2, and if none exists, Erdős is unprovable by automatic induction

#### lens
Logic and computability (proposer 7 of 10). The arithmetical form of a statement decides which kind of finite certificate can exist at all. I also checked whether a named conjecture implies any of the four problems; the answer is no, for a stated reason.

#### problem
Erdős's ternary conjecture in its strong form: for n > 8, 2^n has a ternary digit 2. GC1241 showed that the named sub-statement 'E_k meets [0, 1.58k] only in 0, 2, 8 for every k' is a restatement of this same conjecture (RULE30-GPT.md:31279; CONSTELLATION.md:1016-1029).

#### object_and_claim
OBJECT. Let C* = {x >= 1 : every ternary digit of x is 0 or 1}. Define the Pi_1 sentence E := for all m >= 5, 4^m is not in C*. E is exactly the strong conjecture: for odd n, 2^n = 2 mod 3, so its last ternary digit is 2; for even n = 2m, 4^4 = 256 = 100111_3 is the last exception and 4^5 = 1024 = 1101221_3.

REDUCTION LEMMA. Elementary and provable now. It is a tier-2 hand claim and needs GPT's read.
(i) E holds iff 1024 is not in B*, where B* = {x >= 1 : 4^j x is in C* for some j >= 0}.
(ii) Suppose L is a set with 1024 in L, 4L contained in L, and L disjoint from C*. Then E holds.
(iii) Suppose further that L is recognised by a finite automaton reading base-3 numerals. By the Büchi-Bruyère theorem this is the same as L being first-order definable in base-3 Büchi arithmetic (N, +, V_3). Multiplication by 4 is definable there, since 4x = x+x+x+x. Then all three conditions in (ii) are decidable by product automata, and the automaton is a complete, finitely checkable proof of E.
Adding auxiliary existential tracks to the invariant gains nothing, because projections of automatic relations are automatic. So 'E has an inductive invariant definable in (N, +, V_3)' holds iff such a regular L exists.

CONJECTURE A (the crossing; I rate it a lottery). Such a regular L exists. Equivalently, there is a 3-recognisable set B that contains C*, satisfies 'if 4x is in B then x is in B', and does not contain 1024.

CONJECTURE not-A (the barrier, and the kill outcome). No such L exists. E is a definite true-or-false Pi_1 sentence, yet it would not be provable by x4-induction with any invariant definable in the decidable theory (N, +, V_3). That would be the wall stated as a theorem for the one Pi_1 problem. Cobham-Semenov does not decide between A and not-A: it forbids describing the orbit {4^m} in base 3, not over-approximating it.

#### mechanism
1. THE ARITHMETICAL FORM DECIDES THE CERTIFICATE CLASS.
- Rule 30 period 2, Collatz and Mahler (via GC664) are Pi_2. Their certificates must prove termination (liveness). The record's only analysis of machine certificates is for this case. 8.61 found that a termination potential must scale with the seed (RULE30-PRIZE.md:4061-4112, esp. :4074). 8.47 cites Condrey's horizon H(2,w) >= w as the reason (RULE30-PRIZE.md:3031-3037). GPT's audit noted that scaling does not by itself forbid a bounded certificate (RULE30-PRIZE.md:4097-4105).
- E alone is Pi_1 (RULE30-PRIZE.md:6760-6762, :7808), which makes it a safety property. Safety needs only an inductive invariant: no ranking function, no clock, nothing that must grow with m. The record notes the Pi_1 form only as a 'safety net if independent' and never as a proof shape.

2. ONE MEMBERSHIP TEST INSTEAD OF INFINITELY MANY.
- Take B to be the complement of L. B is backward-closed: if 4x is in B then x is in B. B also contains C*.
- If any 4^m with m >= 5 were in C*, it would be in B, and backward closure would pull 1024 into B. So the infinitely many conditions collapse to one check: 1024 is not in B.
- This is the same move as 8.112's odd-point reduction: normalise along the map's inverse branch, then a finite object decides for ever (RULE30-PRIZE.md 8.112, :7937-7945 as read).

3. THE CHECKS ARE EXACT. Use a DFA A reading least-significant digit first, with s states.
(a) A accepts the word 1221011, which is 1024 read least-significant digit first.
(b) Let R01 be the set of states reachable from the start on words over {0,1}. Then delta(R01, 1) contains no accepting state. This is exactly 'no canonical numeral with digits 0 and 1 only is accepted'.
(c) Closure under x4. Form the product of A on the input, the x4 carry transducer, A on the output, and a flag recording whether the last input digit was nonzero. The transducer has carry c in {0,1,2,3}; on digit d it computes v = 4d + c, outputs v mod 3 and carries v div 3. At the end it flushes the carry as 1 -> '1', 2 -> '2', 3 -> '01'. Condition: no reachable end state has a canonical, accepted input whose output is rejected. The product has at most 8s^2 states.

4. SEARCH, AFTER THE BOUNDED TEST.
- Encode it for SAT. Variables give the transitions, the accepting set, and a simulation relation R inside Q x {0..3} x Q x {0,1} that contains the start state, is closed under steps, and satisfies the end condition. This is sound, because R contains every reachable state. It is complete, because SAT may choose R to be exactly the reachable set. It is the encoding used for DFA identification and by the busy-beaver finite-automaton deciders.
- Run s <= 20, in both reading directions.
- Also run the relaxation 'seeds 4^5 .. 4^(4+p), closed under multiplication by 4^p', for p <= 3. This combines k-induction with an invariant.
- Re-verify any automaton found with a second, independent implementation and with Walnut. The record has already built and used Walnut, for G153 (PRIOR-ART.md:1970). Each condition is one first-order formula over base-3 numerals with addition.

5. THE NAMED-CONJECTURE ROUTE IS EMPTY, WITH THE REASON.
- Mahler. abc applied to 3^k = p 2^k + r gives |r| >= c 3^(k(1-eps)) / (3/2)^k, so ||(3/2)^k|| >= c 3^(-eps k). That is fine-scale closeness for one algebraic number. It says nothing about the coarse window [0, 1/2); this is 8.101's Mahler cell again.
- Erdős. An exception is a vanishing sum of N = k+1 S-units: -4^m plus k powers of 3. It has no vanishing subsum, gcd 1, and radical 6. The Browkin-Brzeziński n-conjecture has exponent 2N-5 (I cite this from memory). It gives 4^m <= C(k+1, eps) 6^(2k-3+eps). Even with C uniform in k, this excludes only exceptions with k < 0.387m ones, about 31% of the 1.26m digits of 4^m. In fact C depends on k.
- Schanuel and Lang/Vojta also fix the complexity: a fixed number of exponentials, or a fixed variety. Elliott and Chowla concern multiplicative functions, not digit sets.
- So the named conjectures are themselves statements about bounded complexity, and they leave the wall where it is. Definability is the only reduction this lens finds that grips the single orbit.

6. WHERE A SKEPTIC SHOULD ATTACK.
- Step 2: canonical numerals; the closure is needed only for x >= 1.
- Step 3(c): handling of leading zeros and the flush.
- Step 4: the soundness of the encoding with R.
- Whether a regular L can exist when B* contains numbers whose orbits enter C* only after arbitrarily many steps (see honest_weakness).

#### precedent
Main precedent: BB(5) = 47,176,870 (bbchallenge collaboration, 2024, proof checked in Coq).
- Each non-halting 5-state machine is one deterministic run whose tape grows without bound: one object of unbounded complexity.
- Almost all of them were certified by finite closed-set certificates. Such a certificate is a regular set of configurations that contains the start, is closed under one machine step, and excludes halting. The certificate families include n-gram closed position sets and repeated-word lists, with finite-automata reductions in the community's decider pipeline. This list is from memory and should be checked against the Coq-BB5 write-up.
- What made it possible: (1) non-halting is Pi_1, a safety property; (2) the step is a finite transducer on tape words, so whether a regular set is closed under it is decidable exactly; (3) for each certificate size the search is finite and complete.
- It stopped exactly at the cryptids. Antihydra is a BB(6) machine that iterates floor(3n/2), and its non-halting is also Pi_1.

Second precedent: the Thue-Morse word is overlap-free (Thue 1912; reproved mechanically in Walnut). This is one infinite word of unbounded complexity, and the proof was possible because the word is automatic. The powers 4^m in base 3 are not automatic (Cobham-Semenov). That is why only an over-approximating invariant can be hoped for here, not a description of the orbit.

In-record analogues of finite certificates that reach unbounded complexity:
- PROOFS.md entries 38, 40, 41 (PROOFS.md:1534, :1663, :1725): strip-graph certificates that, for every finite seed, exclude columns ending in 0 1^q (q = 7 and q >= 9) and in 1 0^q (q >= 10).
- 8.112's depth-7 certificate deciding K ∩ 13K = {0} after the odd-point normalisation (RULE30-PRIZE.md:7937-7945, as read).

#### precedent_in_record
Partly cited, but the mechanism itself is absent.
- BB(5) appears only as 'a reduction plus a finite check' (PRIZE-PROBLEMS.md:119-124). The record also says the busy-beaver effort 'stopped at our wall' at Antihydra (RULE30-PRIZE.md:6734-6736).
- How the BB(5) certificates actually work (closed sets of configurations) is named nowhere. record_find gives 0 hits for 'closed tape', 'closed position', 'n-gram' and 'Finite Automata Reduction'.
- Automaton invariants and regular model checking appear only as liveness certificates for Rule 30's condition B: RULE30-PRIZE.md:3031-3037, :3105-3108, and PRIOR-ART.md:1506-1514 (Yolcu-Aaronson-Heule; Lin-Rümmer).
- That route was closed for Rule 30 only, on liveness and scaling grounds, in 8.61 / Q3 (RULE30-PRIZE.md:4061-4112), with GPT's G5 qualification (RULE30-PRIZE.md:4097-4105).
- Erdős's Pi_1 form appears only as 'if it is independent of the axioms, it is true' (RULE30-PRIZE.md:6760-6762) and as one lifting-table cell, 'Erdős differs' (RULE30-PRIZE.md:7808). It is never used as a proof shape.
- The Stérin-Woods machine is cited, with its proof unaudited (CONSTELLATION.md:981; RULE30-GPT.md:31245).
- Walnut has been built and used once (PRIOR-ART.md:1970; G153, Rudin-Shapiro).
- Cobham appears only as a low-complexity item (PRIOR-ART.md:1502) and in 8.113's search line (RULE30-PRIZE.md:8002).
- No named conjecture (abc, n-conjecture, Schanuel, Elliott, Chowla) is applied anywhere in the record.

Caveat: RULE30-PRIZE.md, PROOFS.md, PRIOR-ART.md and four other files were being edited concurrently during this read (git status showed them modified), so line numbers may drift.

#### record_search
##### terms
- inductive invariant
- closed tape
- closed position
- n-gram
- Finite Automata Reduction
- Stérin
- Sterin
- safety
- liveness
- regular model checking
- Rümmer
- automaton invariant
- regular language
- Walnut
- Büchi
- Presburger
- Cobham
- BB\(5\)
- busy beaver
- bbchallenge
- Antihydra
- Pi_1
- \babc\b
- abc conjecture
- Browkin
- Schanuel
- Chowla
- Elliott
- provab
- independent of (PA|ZFC|the axioms)
- ternary.*automat|automat.*ternary

##### hits
Each term was searched alone.
- 'inductive invariant': 0 outside the ledgers; 1 in a ledger (CHAT-LEDGER.md:3827, the swarm's lens list, where 'inductive invariants and finite certificates' is a separate lens).
- 'closed tape' 0; 'closed position' 0; 'n-gram' 0; 'Finite Automata Reduction' 0.
- 'Stérin' 3: RULE30-PRIZE.md:7808, RULE30-GPT.md:31245, CONSTELLATION.md:981.
- 'Sterin' 5, none relevant (they are substring matches inside 'clustering', 'registering' and 'replay is a self-check').
- 'safety': no relevant hit.
- 'liveness' 4, 2 relevant (RULE30-PRIZE.md:3031; PRIOR-ART.md:1510).
- 'regular model checking' 2 and 'Rümmer' 2: the same two places.
- 'automaton invariant' 5, all about Rule 30 liveness (PERIOD-TWO.md:328; RULE30-PRIZE.md:3031, :3105, :4061-4063; PRIOR-ART.md:1510).
- 'regular language' 7, none about Erdős.
- 'Walnut' 33 in 7 files (G153 Rudin-Shapiro; PRIOR-ART.md:1964-1970; GC487).
- 'Büchi' 0; 'Presburger' 0.
- 'Cobham' 2 (RULE30-PRIZE.md:8002; PRIOR-ART.md:1502).
- 'BB\(5\)' 3 (RULE30-PRIZE.md:6734, :6760; PRIZE-PROBLEMS.md:122).
- 'busy beaver' 7 in 4 files; 'bbchallenge' 2 (RULE30-GPT.md:3446; PRIOR-ART.md:1495); 'Antihydra' 26 in 10 files.
- 'Pi_1' 2 (RULE30-PRIZE.md:6760, :7808).
- '\babc\b' 4, all unrelated (pattern names such as N_abc and Rule 22's 'abc'); 'abc conjecture' 0; 'Browkin' 0; 'Schanuel' 0.
- 'Chowla' 3 (RECORD-MAP.md:415; CONSTELLATION.md:915, :955, by name only); 'Elliott' 1 (CONSTELLATION.md:955).
- 'provab' 25 (8.46 and the Turing read; none about invariants); 'independent of (PA|ZFC|the axioms)' 8 (8.100 and GC1221 framing).
- 'ternary.*automat' 1, unrelated (a board-history line).

Conclusion: an inductive invariant for the Pi_1 Erdős statement, and its definability form in base-3 Büchi arithmetic, are not in the record. The nearest record material is Q3 / 8.61, which addressed liveness for Rule 30.


#### route_to_prize
Under Conjecture A:
- A regular L with the three exact checks proves E outright: no n > 8 has 2^n free of the ternary digit 2. That gives every E_k statement and the m_k >= ceil(k log_2 3) criterion for all k >= 7, which GC1241 showed is equivalent to E (RULE30-GPT.md:31279; CONSTELLATION.md:1016-1029).
- The certificate is a finite machine object (tier 1 once re-verified by two implementations and Walnut). The prize-won rule applies: push at once, then GPT verifies.
- The record's survey lists the Erdős question as carrying no cash prize; it is 'a test bed, not a prize' (PRIZE-PROBLEMS.md:347-352).

Under not-A:
- The route reaches no prize. It yields a theorem: E is not provable by x4-induction with invariants definable in base-3 Büchi arithmetic. That is the record's wall made formal for its one Pi_1 problem.

Transfer to the other three problems:
- None directly. They are Pi_2 and need liveness certificates, which 8.61 already treats.
- The logic lesson does transfer: a Pi_1 strengthening of a Pi_2 problem (for example 'every n < 2^w has Mahler horizon <= 3w + c') is the only form that admits a pure invariant.

#### kill_test
##### kills
Written before any run. Either outcome below kills the route.
(K1) The SAT stage is run once, as specified in mechanism step 4. It searches DFAs with s <= 20 states in both reading directions (least- and most-significant digit first), plus the relaxation 'seeds 4^5 .. 4^(4+p), closed under 4^p' for p <= 3. If it finds no invariant: HALT, and park the route with the bound recorded as a measured barrier. Do not extend s without a named structural reason.
(K2) A hand proof (tier 2, for GPT) that every 3-recognisable L with 4L contained in L and some element not divisible by 3 meets C*. This closes the route by theorem: E is independent of automatic induction.
Owed before K1 runs: check the bbchallenge cryptid and decider pages for prior closed-set attempts on the Stérin-Woods machine. If a regular certificate is already known to be absent there, adopt that as K1.

##### confirms
An explicit automaton that passes (a), (b) and (c) of mechanism step 3 exactly, in two independent implementations that share no code, and also as three Walnut formulas. That is a proof of E. Push at once under the prize-won rule; GPT is the verifier.

##### inconclusive_tips
ACT once, then HALT. The bounded test is expected to be null (no invariant with at most 4 states). That result says nothing about larger automata, so it tips to ACT on exactly one run of the SAT stage, which costs a few CPU-hours on the M5 and no new method. If that run is null, HALT. The only reason to go past s = 20 is the unexpected check below: if the automaton size m_J of B*_J grows sub-exponentially (ratio below 1.5 per step in J), that suggests B* is nearly regular.


#### bounded_test
##### description
One standard-library Python script with three parts, run with predictions committed first.

(1) Exact exhaustive search over all least-significant-digit-first DFAs on {0,1,2} with at most 4 states, numbered canonically in breadth-first order.
- Transitions and accepting states are assigned lazily by backtracking against a constraint sample. The sample says: accept 4^m for 5 <= m <= 40; reject every x < 3^12 such that 4^j x is in C* for some j <= 3. Any invariant must reject these, because L is disjoint from B*.
- Every complete DFA consistent with the sample is then verified exactly: condition (b) by a breadth-first search of the {0,1} sub-automaton, and condition (c) by the product automaton of mechanism step 3 (input DFA x carries 0..3 x output DFA x canonical flag).

(2) Controls.
- Known answer: replace C* by the bad set {x = 2 mod 3}. The search must find at least one exact invariant at s <= 3, namely {x = 1 mod 3}.
- Counterfactual: use seed 64 = 2101_3. Since 4·64 = 256 = 100111_3 is in C*, the search must return 0. In particular the 2-state DFA 'contains a 2', which satisfies every sample constraint for seed 1024, must be rejected by the exact closure check (64 is accepted, 256 is not).

(3) The one unexpected check: the minimal DFA size m_J of B*_J = {x : 4^j x in C* for some j <= J}, for J = 0..5. Build it exactly with states (floor(4^J r_k / 3^k), alive flags of machines j <= J), where r_k is the number formed by the k digits read so far; every carry floor(4^j r_k / 3^k) is determined by the j = J carry. Then apply Moore minimisation. This is the Pi_1 analogue of 8.61's 'walks of length 0.83 d from every depth'.

The test itself was not run, as instructed. Run it in a scratch clone.

##### quantity
Q, the number of DFAs with at most 4 states, read least-significant digit first, that satisfy all three conditions exactly: 1024 in L, 4L contained in L, and L disjoint from C*. Also recorded: the number of sample-consistent DFAs before exact verification, both control outcomes, and m_0..m_5 with the ratios m_(J+1)/m_J.

##### cost
Standard-library Python on one core. Part (1) takes seconds to about 2 minutes: backtracking over at most 4^12 transition tables with heavy pruning, each exact check under 1 ms. Part (3) takes under a minute: at most about 65k states at J = 5. Abort guard at 4.5 minutes.

##### prediction
Q = 0 at every s <= 4, and both controls pass: the known answer is found and the counterfactual returns 0. Secondary prediction, recorded but not decisive: the ratio m_(J+1)/m_J lies between 2.5 and 4.5 for J = 2..4 (about 4^J growth from distinguishable x4^J carries), with probability 0.7.

##### probability
0.97


#### honest_weakness
The most likely failure is that this is the wall again, moved from a ranking function into an invariant.

B* must lie inside the complement of L. It contains numbers whose x4-orbits enter C* only after arbitrarily many steps (transients of every length). Their digits look random, and so do the digits of the powers 4^m. So any envelope of B* coarse enough to be finite-state will probably swallow some power of 4. That is the Pi_1 analogue of 8.61's 'walks of length 0.83 d from every depth' (RULE30-PRIZE.md:4074). It is also exactly where the busy-beaver closed-set deciders stopped: Antihydra is a Pi_1 floor(3n/2) cryptid, and no such certificate has been found for it (PRIOR-ART.md:1495-1497; RULE30-PRIZE.md:6734-6736).

A regular L would be a finite-state reason why 4^m always contains a 2. That means hidden automatic structure in x4 acting on ternary strings. Cobham-Semenov does not forbid it, but nothing suggests it. I could not prove not-A with a pumping argument, because every pumped family keeps a long, random-looking unpumped part whose landing in C* is itself an Erdős-type coincidence. So the prior that an invariant with at most 20 states exists is low, about 2 to 5 percent.

The realistic yield is therefore a measured null, or a proof of not-A: a formal barrier, not a crossing.

Two further weaknesses:
- The proposal overlaps the separate lens 'inductive invariants and finite certificates' (CHAT-LEDGER.md:3827). This lens's own contributions are the Pi_1-safety versus Pi_2-liveness classification, the definability equivalence, and the negative answer on named conjectures.
- The n-conjecture exponent and the BB(5) decider list are cited from memory. Both need a primary-source read.

### Skeptic on the record, proposal 7

#### refuted
False

#### confidence
0.6

#### reason
Through the record lens, none of the four refutation criteria holds cleanly. Some overlap partly, and the proposal misses two record items it has to address.

(a) Closed route: not met. The record's only closure of machine certificates is Q3/8.61. That closure is for Rule 30 liveness (a ranking potential), and it is explicitly conditional: "closed until another finite family is named". This proposal names a finite family (regular invariants closed under x4) for a different problem (Erdős) and a different logical form (Pi_1 safety, no ranking). No closed-route list (PERIOD-TWO §4, RECORD-MAP "Routes closed", MAHLER §2, COLLATZ §5) contains it.

(b) A set statement in disguise (S10): not met. S10's objection is that set-level avoidance cannot single out an integer without "an integer-only ingredient". A regular L that contains 1024, is closed under x4 and is disjoint from C* would imply E outright. L reads finite canonical numerals, so the end-of-word condition is exactly an integer-only ingredient. The analogy to 8.112 is one of method only, and the record itself files 8.112 as "still pairs".

(c) The precedent is already cited and dismissed: partly met. The record cites BB(5) as the "reduction plus finite check" shape. 8.100 says that shape is the missing piece, and that the busy-beaver effort "stopped at our wall" at Antihydra. That is a one-line observation about the floor(3n/2) family. It is not an analysis of regular invariants for Erdős, and it says nothing about whether over-approximation escapes Cobham-Semenov.

(d) The test repeats a recorded measurement: not met. Q (the count of exact invariants for s <= 4) and m_J (the minimal DFA size of B*_J) are not in the record.

Record material the proposal does not engage:
- Stephan 2026 Theorem D. Block (closed-set) certificates are complete only on finite hold sets and provably obstructed on infinite ones. The record concludes that "the integer side is the crux".
- Abram-Lagarias on multiplicative translates of the 3-adic Cantor set. This is the closest automaton literature, and the record names it but has not read it.
- Lagarias Lemma 4.1 at M = 4 = 1 mod 3: C ∩ 4^(-1)C is infinite.
- G.1's exact free part. Together with Lemma 4.1, it implies that no invariant reading only low-order digits can work. The certificate has to rely on the top end.

Gut verdict: this is the wall moved into an invariant, as the proposer says. But the record has not closed it, so a record skeptic cannot honestly refute it.

#### evidence
Searches run (record_find, one term each): "inductive invariant" 1 (ledger only), "automaton invariant" 5, "Pi_1" 2, "safety" 13 (none relevant), "regular set" 0, "Cobham" 2, "Lemma 4.1" 3, "Stérin" 4, "Saye" 17, "transducer" 65 (none Erdős), "bbchallenge" 2, "finite automat" 19 (none Erdős), "Yolcu" 4, "finite-hold" 5, "hold set" 8, "Abram" 1, "path set" 3 (none relevant), "multiplicative translate" 1, "Narkiewicz" 3, "Dimitrov" 1, "4^m" 0, "times 4" 6 (none relevant), "Moore" 2, "minimal automaton" 2, "minimal DFA" 0, "Theorem D" 25.

(a) The only closure is conditional and specific to Rule 30:
- RULE30-PRIZE.md:4063-4079 (8.61: the certificate is a potential falling at forced cells).
- RULE30-PRIZE.md:4086-4092: "Closed as a route of its own until a family of potentials is named".
- RULE30-PRIZE.md:4093-4105 (GPT G5: the impossibility claims are withdrawn).
- RECORD-MAP.md:354-356: "CLOSED until another finite family is named".
- PERIOD-TWO.md:219, :252, :282.
- PERIOD-TWO.md:107-130 and RECORD-MAP.md:335-362 list no Erdős invariant route. MAHLER.md:184-188 closes only product-formula coupling and the bowtie.

(b) S10 and the pair wall:
- INSTINCT-CLOUD.md:123-130. Avoidance holds for every point of K, so it "would need an integer-only ingredient beside it".
- RULE30-PRIZE.md:7972: 8.112 is "Still pairs, not a single integer (S10's wall)".
- The proposal's L reads finite canonical numerals. Its condition (b) acts at the word end, so the integer-only ingredient is present, and a found L implies E.

(c) Precedent:
- PRIZE-PROBLEMS.md:119-125: BB(5) as "a reduction plus a finite check".
- RULE30-PRIZE.md:6733-6736: "The missing piece is a reduction of 'for ever' to finitely many cases ... stopped at our wall" (Antihydra).
- PRIOR-ART.md:1495-1497: Antihydra, no proof.
- PRIOR-ART.md:1502-1503: low-complexity tools, including Durand's Cobham theorem, "work only when the complexity is low".
- RULE30-PRIZE.md:6914-6921: 8.101 P3, the bounded-complexity reading, "not a theorem".
- No record line analyses over-approximating regular invariants, or bbchallenge deciders on the Stérin-Woods machine. CONSTELLATION.md:985 and RULE30-GPT.md:31245 mark that machine as unaudited.

(d) Not repeated:
- The nearest computed quantities are 8.110's survivor counts for the power map x^e and for Mahler multipliers (RULE30-PRIZE.md:7741-7763) and G.1's m_k margin (CONSTELLATION.md:1021-1025). Neither is Q or m_J.

Record material the proposal misses:
- PRIOR-ART.md:2569 (Stephan paper 2, Theorem D: complete on finite hold sets, obstructed on infinite ones).
- PRIOR-ART.md:2586-2588: "The integer side is the crux".
- MAHLER.md:49-53 (the consequence for one certificate format).
- PRIOR-ART.md:2634 (Turing miniature).
- RULE30-GPT.md:30905 (GC1221 verifies the hold-set premise).
- PRIOR-ART.md:2670-2673: Abram-Lagarias, arXiv 1308.3133 and 1508.05967, "LINEAR multiplicative translates", full texts not read.
- PRIOR-ART.md:2663 and :2675-2677, with RULE30-PRIZE.md:7847-7848: Lagarias Lemma 4.1. The intersection C ∩ M^(-1)C is infinite for M = 1 mod 3, which includes M = 4. Its proof uses 4 = 11_3 and 256 = 100111_3.
- CONSTELLATION.md:991-995: the free part is exact, 2^(k-1) residues keep the last k digits free of 2. With 4 generating 1+3Z_3, the orbit's 3-adic closure covers C's units. So an invariant that depends only on low-digit blocks is impossible, and the certificate must depend on the top end.
- RECORD-MAP.md:398: G295, the power-form converse is infinite for sign +1. It concerns powers, not multiplication by 4, and must not be conflated (PRIOR-ART.md:2663).

Spot checks on the proposal's claims:
- 1024 = 1101221_3 (1221011 read least-significant digit first), 256 = 100111_3 and 64 = 2101_3 are correct.
- Its zero-hit claims for "abc conjecture", "Browkin" and "Schanuel" are confirmed by its own search list; I did not rerun them. "Presburger", "Büchi" and "n-gram" were not rerun by me.
- The claim "Walnut used once for G153" is consistent with PRIOR-ART.md:1964-1970.

#### what_would_rescue
Not refuted on the record lens. To make it hold up against the record's adjacent objections, the proposal should add four things.

(1) Engage Stephan's Theorem D (PRIOR-ART.md:2569, :2586-2588; MAHLER.md:49-53). State and prove the Erdős analogue as a lemma: G.1's exact free part (CONSTELLATION.md:991-995) plus Lagarias Lemma 4.1 at M = 4 (PRIOR-ART.md:2675-2677) make the orbit 3-adically dense in 1+3Z_3, so any invariant that depends only on low-digit blocks fails. Then show the regular-L class escapes, because acceptance depends on the canonical top digit. Add a control to the bounded test that confirms the end-of-word flag carries every rejection.

(2) Read Abram-Lagarias (arXiv 1308.3133 and 1508.05967), which the record names but has not read (PRIOR-ART.md:2670-2673), before computing m_J. Their automata for C ∩ M^(-1)C may already give part (3), or a sharper version of it. If they do, cite them, and either drop part (3) or recast it as the union form B*_J that they do not cover.

(3) Do the owed check of bbchallenge decider and finite-automata-reduction results on the Stérin-Woods machine (CONSTELLATION.md:985, unaudited). If a regular closed-set certificate is known to be absent there, say whether that encoding transfers to base-3 x4 invariants, or why not. The record's own Yolcu line says the encoding decides (PRIOR-ART.md:1506-1509).

(4) Write K2's not-A barrier so that it avoids the impossibility shape GPT refuted in 8.61's audit (RULE30-PRIZE.md:4093-4105: fixed-size objects can carry unbounded structure). No pumping argument should be claimed until a carrying read exists.

Whether the s <= 4 test can discriminate is the mathematics skeptic's question. It is predicted null at 0.97 and says nothing about larger automata, but the record does not settle this.

### Skeptic on the mathematics, proposal 7

#### refuted
True

#### confidence
0.8

#### reason
(c) The whole route rests on Conjecture A: that a regular L exists with 1024 in L, 4L contained in L, and L disjoint from C*. A is strictly stronger than E (A implies E, but E does not imply A). The proposal gives no reason it should hold, and the proposer puts it at 2 to 5 percent. A regular L would be a finite-state proof that every 4^m has a ternary 2, which is exactly the single-object rigidity at unbounded complexity that the wall says is missing (RULE30-PRIZE.md:6832, :7803). So the proposal renames the wall and does not cross it. Even full success reaches no prize: the record calls the Erdős question 'a test bed, not a prize' (PRIZE-PROBLEMS.md:347-352), and the proposal concedes nothing transfers to the three Pi_2 problems.
(d) The bounded test cannot tell A from not-A. I ran it: Q = 0 for s <= 4, as predicted with p = 0.97, and that null fits both 'A needs more states' and 'not-A'. K1's null at s <= 20 is another bounded-complexity measurement, not a barrier. The unexpected check (the minimal DFA size m_J of B*_J) measures how complex the set B* is. That does not bound a regular over-approximation of B*, which is all A needs, so it cannot test A either.
(a) K2 as written is false; counterexamples below. The bounded test also claims the 'contains a 2' DFA 'satisfies every sample constraint for seed 1024'. That is false: 64 is in the reject sample and that DFA accepts it.
(b) The enabling ingredient of the BB(5) precedent is absent here. Its closed-set deciders worked on regular dynamics and stopped at the floor(3n/2) cryptid Antihydra (PRIOR-ART.md:1495-1497; RULE30-PRIZE.md:6734-6736), which is the class E sits in. Not-A is also oversold: it would exclude only proofs by induction with an automatic invariant, not 'the wall as a theorem'.

#### evidence
COUNTEREXAMPLES TO K2 AS WRITTEN. K2 claims: 'every 3-recognisable L with 4L contained in L and some element not divisible by 3 meets C*'.
- Take L1 = {x : x = 2 mod 3} and L2 = {x : the lowest nonzero ternary digit of x is 2}.
- Both are 3-recognisable.
- Both are x4-closed, because 4 = 1 mod 3 and v_3(4x) = v_3(x).
- Both contain 2, which is not divisible by 3.
- Both are disjoint from C*.
- Arithmetic check over all x < 3^9: closed under x4 True, disjoint from C* True.
- Exact product-automaton check (input DFA x carry 0..3 x output DFA x canonical flag, flush 1->'1', 2->'2', 3->'01'): both return ok. L2 also returns ok for seed 6.
- A corrected K2 needs an element whose lowest nonzero digit is 1.

THE SAMPLE CLAIM.
- 64 = 2101_3 < 3^12, and 4*64 = 256 = 100111_3 is in C*. So 64 is in the reject sample.
- The 'contains a 2' DFA accepts 64.
- The exact checker rejects that DFA for seed 1024 at the closure condition (c).

THE BOUNDED TEST, RUN. Standard-library Python with an exact checker for (a), (b) and (c), reading least-significant digit first.
- Validation: {x = 1 mod 3} passes closure (the proposal's known-answer control).
- s = 1..3, all DFAs and accepting sets: 0 invariants. At s = 3, 157,464 pairs failed as follows: 59,049 at (a), 77,868 at (b), 864 at (c).
- Counterfactual seed 64: 0 invariants.
- s = 4, all 2,532,530 canonical initially-connected transition tables: 233,216 (table, accepting set) pairs pass (a) and (b); all 233,216 fail closure. Q = 0, in 4 s.
- Seed-free variant (any element with lowest nonzero digit 1, the corrected K2 at small s): 0 closed at s <= 4, out of 4,817,070 candidates at s = 4, in 24 s.
- Every result is the predicted null. A null at small s is compatible with both A and not-A.

THE RECORD.
- The wall: RULE30-PRIZE.md:6832 (8.101) and the row at :7803, 'same: bounded complexity only'.
- The Pi_1 form appears only as a 'safety net': RULE30-PRIZE.md:6760-6762, and the logical-form row :7808.
- Busy beaver and Antihydra stopped at the wall: RULE30-PRIZE.md:6734-6736 and PRIOR-ART.md:1495-1497. Antihydra is a floor(3n/2) halting question, 'a Mahler-family question'.
- record_find 'regular invariant': 0 hits.

THE IN-RECORD 'PRECEDENTS' ARE NOT SINGLE-OBJECT, UNBOUNDED-TARGET CERTIFICATES.
- PROOFS.md:1534 (entry 38, columns ending 0 1^q) and PROOFS.md:1663 (entry 40, 1 0^q) are statements over all seeds.
- Each excludes a zero-entropy target, one word per length, with strong backward forcing.
- C* has 2^(n-1) words of length n (dimension log2/log3), so B* is not locally forced.
- 8.112's K ∩ 13K = {0} is a pair exclusion, which the wall classes as set-level.

COBHAM. {4^m} is 4-recognisable and not ultimately periodic, so it is not 3-recognisable (Cobham 1969; Semenov). As the proposal says, this neither proves nor refutes A.

CHECKED CORRECT.
- The reduction lemma (i) and (ii).
- 1024 = 1101221_3 and 256 = 100111_3.
- The carry bound <= 3, and the flush is always nonzero for canonical input.
- The soundness and completeness argument for the SAT encoding.
- Büchi-Bruyère definability.
- The n-conjecture arithmetic: k >= 0.387m.
- abc gives ||(3/2)^k|| >= c 3^(-eps k).

FROM MEMORY. BB(5)'s Coq proof also needed individually proved sporadic machines; this has not been re-read.

#### what_would_rescue
1. A structural lemma, not a search. Name a finite-state property, preserved by x4 on base-3 numerals, that holds for some number whose lowest nonzero digit is 1 and excludes C*. Equivalently, exhibit any regular x4-closed L that avoids C* and contains such a number, for any seed at all. None exists with at most 4 states, as measured above. Without such an existence result, A has no support beyond hope.
2. Replace K2 with the corrected statement: every 3-recognisable x4-closed L containing an element whose lowest nonzero digit is 1 meets C*. Attempt a proof. It would close the route by theorem, uniformly over seeds.
3. Make any search seed-free, so that a null says something about the whole class and not just about 1024 at bounded size. Do not record a bounded-s null as a 'barrier'.
4. For prize relevance, give an explicit transfer from a Pi_1 automatic invariant to one of the Pi_2 prize problems; the proposal concedes there is none.
5. Fix the 'contains a 2' sample claim and the K2 statement before any run.

## Proposal 9: Darkness is paid for: a time-average (fringe-visibility) form of LR, certified by a potential that may grow linearly

#### title
Darkness is paid for: a time-average (fringe-visibility) form of LR, certified by a potential that may grow linearly

#### lens
The owner's physics lens: time, shortcuts and interference (RULE30-PRIZE.md:6796, the 8.100 §3 shortcut; 8.103; 8.110's U at RULE30-PRIZE.md:7759).

#### problem
Rule 30 period 2, through Conjecture LR, equivalently 'R(d) finite for every d' (PERIOD-TWO.md:35-40), and its realizable form R_real (PERIOD-TWO.md:43-47).

#### object_and_claim
OBJECT. The forced left half beside the clock tau(t) = t mod 2. Also the other phase, tau(t) = (t+1) mod 2, as a robustness run. It is indexed by anti-diagonals A_k[j] = x_{k-j}(-j), with
A_k[j] = A_k[j-1] XOR (A_{k-1}[j-1] OR A_{k-2}[j-2]), A_k[0] = tau(k), A_{k-2}[-1] = c(k-1).
Source: tests/probes/lexicon/records.c:13-21; the recurrence is at :16.
- The depth-k cell of the time-0 row is A_k[k].
- Only the visible bits v_s = c(2s) are free (records.c:20-21).
- For a visible-bit sequence v, write Z_v(D) = #{1 <= k <= D : A_k[k] = 0} for the dark cells and B_v(D) = D - Z_v(D) for the bright cells.

CLAIM, Conjecture DG ('darkness is paid for'). There are constants p* < 1 and C such that Z_v(D) <= p*·D + C for every v and every D.
- Equivalently, the darkness price D_theta := max{D : min_v B_v(D) <= theta} grows at most linearly: D_theta <= (theta + C)/(1 - p*).
- The coin predicts p* <= 0.89. The reasoning: each free bit adds two cells. One can be chosen (the newest bit flips it) and the other is a fair coin (RULE30-PRIZE.md:2556-2558). The expected number of walks with b bright cells after n bit-pairs is C(2n, b)/2^n, which is at least 1 only while b/2n >= 0.110.
- DG is strictly stronger than LR.

MECHANISM LEMMA, BX (bounded exchange rate). There is a named potential g on the merged states of 8.38 (the masked anti-diagonal pairs, RULE30-PRIZE.md:2633-2637) with two properties:
- g(s') - g(s) >= 1[new cell dark] - p* on every transition;
- 0 <= g <= kappa·depth + C on reachable states, with p* + kappa < 1.

#### mechanism
(1) EXACT IMPLICATION. In a period-2 counterexample, the forced row at time 0 is the actual row (left-permutivity, PERIOD-TWO.md:25-27). It is white beyond the support, so Z(D)/D -> 1. DG excludes this, hence LR, hence R(d) finite at every depth (König), hence B.

(2) LENS. Each forced cell A_k[k] is the parity of the whole OR-vector of the previous two anti-diagonals: a running XOR (records.c:16-19), an interference sum that is exact but not local (RULE30-PRIZE.md:6977, 7000).
- LR demands perfect destructive interference for ever: a dark left half.
- DG asks only that the time-averaged fringe visibility, the bright fraction, stays at least 1 - p*.
- A time average tolerates o(D) defects and bookkeeping that grows linearly. The AND erased the GF(2) time shortcut (0.4961, RULE30-PRIZE.md:7759).
- The optimisation over v is still max-plus linear: a Bellman composition over the masked states. So one potential bounds every depth at once. This is a shortcut through time for the bound, not for the orbit.

(3) CERTIFICATE. Telescoping BX along any walk gives Z_v(D) <= (p* + kappa)·D + C, so DG holds with constant p* + kappa < 1.
- The minimal admissible g is the accumulated excess darkness, g*(s) = max over walks to s of (Z - p*·depth).
- DG holds exactly when g* <= kappa·depth + C. The content of the route is a structured formula for g.

(4) WHY 8.61's CLOSURE DOES NOT TRANSFER. Q3 closed because a termination potential for LR must start at least linear in d (walks of 0.83 d exist from every depth, RULE30-PRIZE.md:4074-4080), and no family of potentials was named (RULE30-PRIZE.md:4084-4094; PERIOD-TWO.md:219, 252).
- For DG, linear growth with slope kappa < 1 - p* is admissible.
- GPT's audit showed that fixed-dimension max-plus matrices carry linear potentials, the unary counter (RULE30-PRIZE.md:4097-4101).
- So Q3's own tool, arctic (max-plus) interpretations, becomes a named family for DG. That meets Q3's reopening condition.

(5) THE STEP A SKEPTIC SHOULD ATTACK. BX holds only if a walk can reach a state with dark budget rho (a zero run of length rho it can still force; the records give rho up to about 0.83·depth, RULE30-PRIZE.md:2651-2652) only after paying about rho/E bright cells since the wall.
- If states able to start a near-record run are reachable from prefixes with few bright cells, record runs chain, darkness recharges, and DG and BX both fail.
- 8.38's facts favour bounded recharge without proving it: nothing merges inside a run, and a merge needs black cells (RULE30-PRIZE.md:2649, 2667-2671).

(6) SPECULATIVE CROSSOVER. The maximizers in ergodic optimisation are often rotation-coded (Bousch). If the darkest walks turn out Sturmian-like, Theorem E's tools are the natural ones to bound their darkness. Theorem E: Sturmian visible bits never give a finite left half (PERIOD-TWO.md:72-73).

#### precedent
Bousch (2000), 'Le poisson n'a pas d'arêtes', Ann. Inst. H. Poincaré Probab. Statist. 36. Named from memory and not re-read in this block.
- The theorem: for every theta, every single orbit of the doubling map has limsup Birkhoff average of cos 2π(x - theta) at most the value on a Sturmian, rotation-coded orbit. Each orbit is an arbitrary binary sequence, so the objects have unbounded complexity.
- What made it possible: a sub-action. This is a bounded function g with f <= m + g∘T - g; it exists by the Mañé–Conze–Guivarc'h lemma (also from memory) because the observable is Hölder and the map expands, so its inverse branches contract and the Bellman fixed point exists. Its contact set is then forced to be rotation-ordered.
- The finite-graph form is Karp (1978): the maximum cycle mean equals the minimum over potentials.
- The general lesson is the one used here: statements about the time average of every single orbit are proved by one potential telescoped along each orbit, not by measure or counting.

#### precedent_in_record
PARTLY IN THE RECORD.
- Karp's cycle-mean/potential theorem was read in full by GPT and used on finite graphs for the left band's waiting envelopes (PRIOR-ART.md:1724-1726, G8; :1734-1736, G10). Bellman horizons appear in G.GPT166 (PROOFS.md:7124).
- Arctic (max-plus) interpretations appear only as Q3's termination template for LR (PERIOD-TWO.md:252). Q3 was closed by 8.61 until a family of potentials is named (RULE30-PRIZE.md:4084-4094).

NOT IN THE RECORD.
- No hit for Bousch, Jenkinson, maximizing measure, ergodic optimization, sub-action, density gap, darkest, fewest ones/black, or recharg.
- The 11 zero-density hits (G133, G137, G255) concern other objects.
- So both the time-average form of LR and the ergodic-optimisation precedent are new to the record.

#### record_search
##### terms
- Frobenius
- dilat
- Mauduit
- Weyl
- van der Corput
- Korobov
- Beukers
- Thue
- Erd.s discrepancy
- Karp
- Bellman
- max.plus
- tropical
- zero.density
- density gap
- ergodic optimi
- sub-action|subaction
- max.mean
- mean.cycle
- Bousch
- Jenkinson
- maximizing measure
- Birkhoff
- Fekete
- subadditiv
- fewest (ones|black)
- darkest
- recharg
- chain(ing|ed) run
- time average
- own time
- Jost
- secular
- frequency of 00

##### hits
Each term was run separately; counts are as printed by the tool.

Terms with hits:
- Frobenius: 23 hits in 10 files. Includes 8.70, where Rule 30's velocity is Rule 210 and Delta^(2^k) = 1 + S^(2^k); also 8.110, G66 and CO-DISCOVERED 003b.
- dilat: 28 hits in 14 files. Includes GC486, 'generic dyadic dilation fails', and 8.110's search line.
- Thue: 122 hits in 21 files. Thue–Morse appears as a class of column 1 under Q7.
- Erd.s discrepancy: 1 hit (8.113's novelty check).
- Karp: 2 hits (PRIOR-ART.md:1726 and :1736, G8 and G10).
- Bellman: 17 hits in 8 files (G.GPT166, G179).
- max.plus: 3 hits (Q3's arctic template, PERIOD-TWO.md:354).
- tropical: 12 hits, in the lexicon only.
- zero.density: 11 hits (G133, G137, G255); none is about the forced row.
- Birkhoff: 1 hit (GC533). Fekete: 1 hit (GC673). subadditiv: 4 hits.
- time average: 3 hits, none relevant. own time: 9 hits, in Theorem A′'s text.

Terms with no hit, the ledgers included: Mauduit, Weyl, van der Corput, Korobov, Beukers, density gap, ergodic optimi, sub-action, max.mean, mean.cycle, Bousch, Jenkinson, maximizing measure, fewest ones/black, darkest, recharg, chain(ing|ed) run, Jost, secular, frequency of 00.

Prior closures this proposal had to check before reusing an idea:
- 8.61 / Q3: certificate potentials must scale with depth (RULE30-PRIZE.md:4074-4094).
- echo_revivals.py: the 'few kernel cells' (Talbot) reading of S7 is already refuted (tests/probes/lexicon/rule30_cloud_echo_revivals.py header).


#### route_to_prize
The chain:
- DG implies LR (PERIOD-TWO.md:38).
- LR is equivalent to 'R(d) finite for every d' by König (PERIOD-TWO.md:39).
- That gives B, and so Prize Problem 1 for period 2, for every finite configuration (PERIOD-TWO.md:35-40).

Restricted to realizable column 1s, DG_real implies R_real(d) finite at every depth, which by the current main line settles period 2 (PERIOD-TWO.md:43-47).

DG is strictly stronger than LR. It can fail while LR holds, for example if bright cells become arbitrarily sparse but never stop. That is the first thing the kill test checks.

#### kill_test
##### kills
Either of the following tips to HALT.

(a) Darkness recharges. In either phase, D_{theta+1}/D_theta >= 1.5 at three consecutive theta in 4..11, or D_12 > 300. That means record runs chain, so walks with dark fraction near 1 cost only o(D) bright cells. DG then fails in the measured range, and averaging cannot separate LR's counterexample from walks that can actually be reached.

(b) Some periodic visible word of period <= 12 has bright density < 0.05 over depths 301..600. Jen excludes eventual darkness for periodic column 1s (RULE30-PRIZE.md:1401), but such a word would break DG for every column 1 outright. Only DG_real could then survive, and this test cannot reach it.

##### confirms
Both phases show linear growth: D_theta - D_{theta-1} in [3, 16] for theta = 5..12, D_12 in [55, 170], and the minimum bright density over periodic words of period <= 12 at least 0.15. That last set includes GC1020's realizable eternal train, column 1 = (1100)^inf (PERIOD-TWO.md:220; RULE30-PRIZE.md:6647).

This outcome supports DG with an exchange rate E of about (mean increment - 1) dark cells per bright cell.

ACT: spend one block searching a named finite family for the BX inequality on the exact transition graph to depth 40. The family: arctic (max-plus) interpretations, or g = E·bright - (Z - p*·depth) plus a bounded window of the masked pair. Register DG as a row serving Q6/LR; that reopens Q3 under its own condition, a named family.

##### inconclusive_tips
HALT. This covers increments drifting upward while ratios stay below 1.5, one phase linear and the other not, a periodic minimum in [0.05, 0.15), or the frontier overflowing. Drift is the slow signature of chaining, and the wall is the default. Record the result as a measurement only.


#### bounded_test
##### description
Standard-library Python, big-integer anti-diagonals, a transcription of records.c:47-63:

    def diag(P, Q, c, k, tau):
        X = (P << 1) | (Q << 2) | (c << 1)
        X = (X & ~1) | tau(k)
        s = 1
        while s <= k:
            X ^= X << s
            s <<= 1
        return X & ((2 << k) - 1)

FRONTIER. At depth k the frontier is a dict from key (A_k, A_{k-1} & ~(A_k >> 1)) to the minimum bright count. This is 8.38's exact merge (MG0b). Start from A_0 = tau(0), A_{-1} = 0, bright = 0.
- Step to k+1: branch c in {0, 1} only when A_k[0] = 0; then A_{k+1} = diag(A_k, A_{k-1}, c, k+1) and b' = b + bit k+1 of A_{k+1}.
- Prune b' > 12. Abort and report if the frontier exceeds 2·10^5 (that is itself a sign of cheap darkness).
- Cap at 600 depths. Record m(k) = min b' at each depth, and set D_theta = max{k : m(k) <= theta}.
- Run both phases: tau(k) = k & 1 and tau(k) = 1 - (k & 1).

CONTROLS (known answers).
- C0: the same engine's DFS for the longest zero run from depth d reproduces, in phase 0, R(1) = 1, R(2) = 6, R(4) = 4, R(9) = 9, R(13) = 17, R(15) = 15, R(16) = 16 (RULE30-PRIZE.md:2547-2548, 2563-2564).
- C1: black wall, tau = 1. m(k) = floor(k/2) exactly for k <= 200, because the forced half is Condrey's universal checkerboard (PRIOR-ART.md:1021-1022).
- C2: white wall, tau = 0. m(k) = 0 up to the cap, from column 1 = 0. This is the counterfactual: the instrument must report density 1 where it holds.

SINGLE ORBITS. For every visible word of period <= 12 (about 8,190 words), in both phases, compute the bright density of the forced row over depths 301..600. This includes the visible part of GC1020's train (1100)^inf. Also run all 56 offsets of the wheel word U (tests/probes/lexicon/rule30_cloud_echo_interference.py:63).

##### quantity
Three things:
- the darkness price D_theta for theta = 0..12, in both phases;
- m(D) at D = 50 and D = 100;
- the minimum bright density over periodic visible words of period <= 12, over depths 301..600.

##### cost
Estimated 1–3 minutes of CPU in total.
- Under the coin the frontier holds at most about 10^4 masked states per depth: first-moment count C(k, 12)·2^(-k/2), plus all states up to depth 24.
- The periodic words take 8,190 words × 600 depths, about 15–30 s.
- The controls take seconds.
- This was not run.

##### prediction
Linear growth: D_12 ≈ 90, inside [55, 170], in both phases.
- The first-moment coin bound, solving C(D, 12) = 2^(D/2), gives about 98; merging and branching-walk corrections lower it.
- D_theta - D_{theta-1} in [3, 16] for theta = 5..12, and never three consecutive ratios >= 1.5 at theta >= 4.
- m(100) between 9 and 18.
- The early values may exceed the coin: D_1 >= 7 already, from R(2) = 6.
- Every periodic visible word of period <= 12 has bright density >= 0.15.

##### probability
0.65


#### honest_weakness
The most likely failure: even a clean linear D_theta only supports DG.

Proving DG needs BX's potential to know each state's stored darkness. That is a functional of the whole masked anti-diagonal pair: the 'statistic of the whole state' of RULE30-PRIZE.md:4079, and the non-locality of 8.102.
- So BX is again a uniform-cost, pseudorandomness statement of 8.38's kind (RULE30-PRIZE.md:2672-2673) and Q1's (PERIOD-TWO.md:204).
- Averaging buys two things: linear-growth potentials become admissible and o(D) defects are tolerated. It does not buy locality.
- The cost per cell must still be bounded below on average, and that is the wall again.

Further weaknesses:
- DG over every column 1 may fail on sparse periodic or chained inputs even if B is true. The route would then need DG_real, which is bound to SAT and has no visible cheap structure.
- D_theta to depth about 120 is a finite check. Chaining could appear only deeper, since record runs grow linearly.
- The precedent's engine is uniform contraction plus a Hölder observable. The forced walk has neither, because its newest cell is a parity of the whole anti-diagonal. So the Bousch analogy may transfer only the form of the certificate, not its existence proof.

### Skeptic on the record, proposal 9

#### refuted
True

#### confidence
0.74

#### reason
Judged on the record lens, the proposal has two new parts: DG, a density relaxation of LR, and the Bousch precedent. The record has no hit for either. Its mechanism is not new.

(c) The certificate step is the record's own restatement. In step (3) the proposal takes g* = max over walks of (Z - p*·depth) and says "DG holds exactly when g* <= kappa·depth + C". That is GPT's least-potential equivalence (G183). The record's verdict on it, second-read by Local, is that it is "a restatement of the debt bound, not a method to prove it" (PROOFS.md:7545). The record also applied this same Karp/Bellman potential to a time-averaged slope on a growing state graph: the Q7 waiting envelopes, G8, G10, G166 and G173 to G183. That lane failed in three ways, and the route is CLOSED:
- finite label families admit positive label-balanced collections;
- the uncompressed graph needed 398 or 411 labels, with no small uniform representation;
- potentials that forget state cannot work at all.

The proposal cites G8 and G10 but not this outcome.

(a) Q3's reopening condition is not met.
- Arctic matrix interpretations are Q3's original template (RULE30-PRIZE.md:4062-4064). That is the family §8.61 assessed and closed, so naming it again names no new family.
- The board asks for "another named finite family" (PERIOD-TWO.md:219; RECORD-MAP.md:354-356). The proposal gives no dimension, encoding or state labelling.
- Its one concrete finite option is "a bounded window of the masked pair". The record says no bounded-size interpretation knows which forced cells will be 0 (RULE30-PRIZE.md:4076-4079). The check at depth j depends on about 7j/16 earlier bits, and a finite walk state is impossible (STRATEGY-PLAN.md:105-107, 184-185). Strip graphs up to radius 9 were already searched and are empty for period 2 (RULE30-PRIZE.md:4107-4110).
- The claimed escape from §8.61 is the linear allowance kappa·depth. It does not survive G183's own criterion (PROOFS.md:7537-7539), by a derivation of mine from that criterion. Take g = kappa·depth + F(label) and sum BX over any all-dark label-balanced cycle of L edges. This gives kappa·L >= (1 - p*)·L, which contradicts p* + kappa < 1. Every finite family that cannot see darkness has such a cycle.

(b) The proposal concedes that BX is "again a uniform-cost, pseudorandomness statement". That is the record's named missing statement: RULE30-PRIZE.md:2672-2673 and 1514-1515, and PERIOD-TWO.md §5. Q1 is PARKED until a mechanism, not a conjecture, supplies "a uniform rate with a depth-free constant" (PERIOD-TWO.md:204). STRATEGY-PLAN.md:101-108 says "there is nothing to work on until a mechanism is named". DG states exactly such a rate with constants (p*, C) and names no mechanism.
- The proposal also leans on 8.38's "a merge needs black cells" to support bounded recharge. The record closed that idea as "a merging lemma as the easy half" (PERIOD-TWO.md:117-118; RECORD-MAP.md:345).
- DG targets the unrestricted LR, where records grow about 0.83·d, not the main line R_real (PERIOD-TWO.md:43-47).

(d) The darkness price D_theta is new by name. Everything else in the bounded test repeats the record or cannot decide the question:
- Its predictions are the coin model, already measured three times.
- Its single-orbit half re-measures periodic words. The record treats those as an instrument check, not evidence. Theorem B already bounds their zero runs.
- The forced-row density of ones was measured at 0.49 to 0.51 for structured column 1s to depth 6000.
- The record says finite data cannot separate "bounded" from its negation.

#### evidence
Certificate = restatement:
- PROOFS.md:7545 (G183): "uniform bounded debt B over every finite path is equivalent to a nonnegative vertex potential bounded by B: define h(s)=sup of rewards ... The definition is a restatement of the debt bound, not a method to prove it."
- PROOFS.md:7551-7565: Local's second read of G183 ("Correct"; checked on 400 random graphs).
- PROOFS.md:7537-7541: a feasible label potential exists iff no positive label-balanced edge multiset; the least potential is the best walk.
- PROOFS.md:7543: finite label families fail (G166, G173, G176, G178); RC2 needs 398 or 411 labels, "no small uniform representation theorem".
- PROOFS.md:7131-7137 (G166 direct-potential restriction): a potential that forgets the preceding word fails at every dyadic q >= 4; "changing constants, density, run lengths ... cannot rescue the family".
- PERIOD-TWO.md:128-129 and RECORD-MAP.md:353: Q7's affine waiting envelopes CLOSED (GC596).
- PRIOR-ART.md:1724-1736: Karp was read by GPT for G8 and G10. This is the lane whose potentials later failed.

Q3 not reopened:
- RULE30-PRIZE.md:4062-4064: Q3 was originally "search, with SAT, for an arctic matrix interpretation or an automaton invariant".
- RULE30-PRIZE.md:4076-4079: no bounded-size interpretation can carry a linear potential "and know which forced cells will be 0".
- RULE30-PRIZE.md:4093-4094: closed "until a family of potentials is named".
- RULE30-PRIZE.md:4107-4110: strip graphs of radius <= 9 are empty for 01; the non-forcing cyclic component grows 84, 150, 264, 456.
- PERIOD-TWO.md:219 and 252, RECORD-MAP.md:354-356: "Reopen only with another named finite family".
- STRATEGY-PLAN.md:91-92: "no finite strip or automaton certificate can close the problem".
- STRATEGY-PLAN.md:105-107: "the check at depth j depends on about 7j/16 earlier bits".
- STRATEGY-PLAN.md:184-185: "a finite walk state is impossible (the exact state is two anti-diagonals, 2n bits at depth n)".

BX = uniform cost:
- RULE30-PRIZE.md:2672-2673: "A uniform cost ... the kind §8.33 found nobody has proved".
- RULE30-PRIZE.md:1514-1515: "A proof would need the cost per cell to be bounded below uniformly".
- PERIOD-TWO.md:204: Q1 PARKED, "no mechanism named; reopen on a uniform rate with a depth-free constant".
- STRATEGY-PLAN.md:101-108: "The content lies only in a uniform rate c > h/2 with a constant independent of the depth ... nothing to work on until a mechanism is named".
- PERIOD-TWO.md:117-118 and RECORD-MAP.md:345: the merging lemma as the easy half is CLOSED ("a merge needs black cells").
- RULE30-PRIZE.md:2667-2671: a merge needs black cells, "the original problem's own flavour".

Bounded test overlaps:
- The coin model is already measured three times:
  - RULE30-PRIZE.md:2555-2558 (RC3: 0.51 and 0.48 bits per cell; every other cell chosen, the rest a fair coin);
  - RULE30-PRIZE.md:2648-2652 and 2664-2666 (1.764 per free bit; R about 0.826·d + 0.8);
  - RULE30-PRIZE.md:1489-1509 (R about log2 G; "the adversary does no better than chance").
- Periodic words:
  - PERIOD-TWO.md:111-112 and RECORD-MAP.md:341: periodic column 1 is CLOSED; the 550,201 words were an "instrument check".
  - PERIOD-TWO.md:70-71 (Theorem B): periodic columns have zero runs <= 2P - 2, so each periodic word's bright density is at least 1/(2P - 1). This is already proved. Kill test (b)'s density below 0.05 would not "break DG outright"; it would only force p* >= 0.95.
- RULE30-PRIZE.md:3690-3695: Thue–Morse, period-doubling, Rudin–Shapiro, paperfolding and Fibonacci column 1s give a forced row with "density of ones 0.49 to 0.51" to depth 6000.
- STRATEGY-PLAN.md:91-92: "'Bounded' as such cannot be killed by finite data".

What is genuinely new:
- record_find gives no hit for darkness price, bright cell, fewest ones, density form, Bousch or sub-action. RULE30-PRIZE.md:8039 lists only the proposal itself.
- The nearest density reformulation in the record is a different object: the time densities of columns -1 and -2 (PROOFS.md:10778-10796, G.GPT256).

#### what_would_rescue
The proposal would need to add the following.
1. A concretely named finite family: a state labelling phi of the masked anti-diagonal pair, with its size, plus the arctic dimension or automaton. The labelling must determine the forced cell A_k[k], which is the running XOR of the whole anti-diagonal. That rules out a bounded window near the wall.
2. A demonstration, by G183's positive-cycle test (PROOFS.md:7537-7541) on the exact transition graph at several depths, that this family's label quotient has no all-dark or darkness-heavy balanced collection (mean darkness >= 1 - kappa). The label count must also stay bounded as depth grows, unlike Q7's 398 or 411 labels (PROOFS.md:7543). Without this, the kappa·depth allowance is void, because an all-dark label cycle forces kappa >= 1 - p*.
3. A structured formula for g* that is not "the maximum over walks". The record already rates that as a restatement (PROOFS.md:7545). The proposal should also say why its walk graph escapes G166's forgetting obstruction (PROOFS.md:7131-7137).
4. A mechanism for the uniform rate, not a conjecture of one. This is Q1's reopening condition (PERIOD-TWO.md:204; STRATEGY-PLAN.md:101-108). The mechanism must also avoid needing a merging lemma (PERIOD-TWO.md:117-118).
5. Either DG_real, restricted to realizable column 1s, to stay on the main line (PERIOD-TWO.md:43-47), or a reason why the unrestricted DG is the better target.
6. A bounded test whose quantity is new. One option: the exact least potential g*(depth) on the exact graph against its best bounded-label quotient. Another: the darkness price over realizable column 1s. Either would replace the periodic-word density checks, which Theorem B and RULE30-PRIZE.md:3690-3695 already cover.

### Skeptic on the mathematics, proposal 9

#### refuted
True

#### confidence
0.85

#### reason
Grounds (c), (d) and (b). (c) The mechanism lemma BX is DG restated. The proposal itself defines the minimal admissible g as the value function g* = max over walks of (Z - p*·depth) and says DG holds exactly when g* <= kappa·depth + C. So BX with no named g carries no content beyond DG. The one concrete family it names, g = E·bright - (Z - p*·depth) + bounded window, fails twice. First, it is not a function of the merged state: MG0b merges prefixes with different Z and B. Second, it has the wrong sign: on a dark step it changes by -(1-p*) + dw, while BX needs at least +(1-p*). So w must rise by at least 2(1-p*) on every dark cell, which is impossible for a bounded w when zero runs of at least 0.75d exist. DG also implies a linear run law, R(d) <= (p*/(1-p*))·d + C/(1-p*): a run of length r from depth d gives r <= p*(d+r) + C. Proving BX is therefore at least proving a linear form of the doubling conjecture, which is 8.38's 'uniform cost' wall at unbounded complexity. (d) I ran the bounded test exactly. Its D_theta reproduces the coin's first moment, the same 'coin's best over the walk tree' quantity 8.38 already measured for runs. By the proposal's own decision rules the outcome is INCONCLUSIVE, so HALT: periodic word '01' gives bright density 1/7, inside [0.05, 0.15), and increments of 20 and 2 fall outside [3, 16]. (b) Karp's theorem and Bousch's sub-action both need things that are absent here: a finite graph with cycles, or a compact space with an expanding map and a Holder observable, giving a BOUNDED sub-action from a fixed point. The forced-walk graph is an infinite acyclic layered graph whose layers grow exponentially, and the newest cell is a parity of the whole state.

#### evidence
THE PROPOSAL'S OWN CLAIMS
- Equivalence of BX and DG. The proposal's mechanism (3) says g* is the minimal admissible g and that 'DG holds exactly when g* <= kappa·depth + C'. So BX adds nothing to DG until a structured g is given.
- The named family fails.
  - Not a state function: merged walks share a state but have different histories (MG0b, RULE30-PRIZE.md:2633-2637).
  - Wrong sign: on a dark step, dg = -(1-p*) + dw, but BX requires at least 1-p*. So dw >= 2(1-p*) per dark cell.
  - Runs are too long for a bounded window: every record from depth 42 to 65 is between 0.75d and 1.35d (RULE30-PRIZE.md:2553), and R(65) = 57 (RULE30-PRIZE.md:2549-2550).
- DG implies a linear run law. A zero run of length r from depth d gives Z(d+r) >= r <= p*(d+r) + C, so R(d) <= (p*/(1-p*))·d + C'. This is a linear form of the doubling conjecture (RULE30-PRIZE.md:2568; PERIOD-TWO.md:41). 8.38 reduces that to 'a uniform cost ... a uniformity statement about deterministic walks' (RULE30-PRIZE.md:2672-2673), which is the wall.
- Q3 was already reopened with a named family and closed again: strip certificates are empty up to R = 9 (RULE30-PRIZE.md:4106-4111). The arctic template was Q3's original proposal (PERIOD-TWO.md:355; the proposal cites :252).
- Karp in the record was used only on finite cyclic graphs (PRIOR-ART.md:1724-1726, 1734-1736).
- Here the state A_k has k+1 bits, so depth strictly increases and there are no cycles. Distinct walks grow by about 1.764 per free bit (RULE30-PRIZE.md:2645-2646); there were 2,819,694 at depth 53 (RULE30-PRIZE.md:2643). The max-plus 'one potential' claim is therefore vacuous.

MY COMPUTATIONS (standard-library Python, the proposal's transcription of diag, masked-pair merge, exact frontier)
- Control C0 reproduced R(1)=1, R(2)=6, R(4)=4, R(9)=9, R(13)=17, R(15)=15 and R(16)=16.

Darkness price, phase 0:
- D_theta for theta = 0..16: 1, 7, 17, 23, 33, 39, 53, 57, 61, 81, 87, 95, 99, 109, 123, 137, 143.
- Increments: 6, 10, 6, 10, 6, 14, 4, 4, 20, 6, 8, 4, 10, 14, 14, 6.
- The frontier died at k = 100 for theta <= 12, so m(100) >= 13. The peak frontier was 331,991 at theta <= 16.
- D_16/16 is about 8.9, a bright fraction of 0.112. The coin's first-moment threshold is 0.110: this is the coin again.

Darkness price, phase 1:
- D_theta: 0, 2, 6, 12, 16, 18, 24, 32, 48, 54, 64, 72, 82, 98, 102, 108, 110.
- Increments include 2 (at theta = 5 and 16) and 16.

Periodic words:
- All 16,380 runs (period <= 12, both phases) over depths 301..600: the minimum bright density is 0.1433, reached by 24 words.
- Word '01' in phase 0 gives the forced row (1000000)^inf exactly, density 1/7, the same in every 300-depth window up to 2,400.
- GC1020's word '10' gives 0.427 (phase 0) and 0.430 (phase 1).

Outcome against the proposal's predictions:
- Refuted: every periodic word >= 0.15; increments in [3, 16]; D_1 >= 7 (phase 1 gives 2).
- Held: D_12 in [55, 170] (99 and 82).
- No kill (a) and no kill (b). By its own rule the result is 'inconclusive, HALT'.

PRECEDENT
Bousch 2000 needs a compact circle, an expanding map and a Holder cos observable, which give a bounded sub-action (Mane / Conze-Guivarc'h). Here:
- The cost A_k[k] is the parity of the whole OR-vector (records.c:16-17), which is not continuous in the product topology.
- g is allowed to grow linearly, so no fixed-point existence argument is available.
- The potential theory supplies g once the value m is known. It does not prove m < 1, and m < 1 is DG.

#### what_would_rescue
Three things would rescue it.
1. An explicit potential g that is a genuine function of the masked pair alone, not of Z or B, with BX checked exactly on the transition graph at every depth. Its form must generalise beyond the measured range, for example a formula in a bounded number of state statistics with a proof that the inequality holds for all k. Searching a finite family to depth 40 only re-measures the coin.
2. Or a proof of a linear run law R(d) <= alpha·d + beta for some alpha, which DG requires anyway. This would also need a new mechanism for 8.38's 'uniform cost', such as a merging lemma made quantitative.
3. Or a genuine analogue of Bousch's enabling ingredient: a compactification or quotient in which the walk is a finite (or compact, contracting) system and the darkness observable is continuous, so that a bounded sub-action exists by a fixed-point argument and the maximal mean is computable, as in Karp.
Empirically, D_theta growing linearly to theta >= 40, with the darkest walks shown not to chain record runs, would strengthen DG as a conjecture, but it would still not cross the wall.

## Judge: the number theorist

Top three: A finite-automaton inductive invariant for the single orbit 2^n in base 3 (Erdős, the only Π_1 problem of the four); Erdős as a safety property: an automaton invariant closed under x4 would prove that 4^m always has a ternary 2, and if none exists, Erdős is unprovable by automatic induction; Not 'sets against one object' but 'is there a front': the record's own Proposition 19 crossed this wall for Rule 210, so search Rule 30's diagonal pair recurrence for a gated clearing-front identity

- **Two-place stammering certificates for Mahler's T-code (Adamczewski-Bugeaud in base 3/2 at S = {inf, 2, 3}): the integer side collapses Subspace to Liouville, i.e. to the window principle W1** (novelty 1, grip 2, testable 1, overall 1): Both skeptics upheld. Lemma L(a) is GC666's exact repeat budget, nearly word for word (RULE30-GPT.md:16255-16258). GC666's own disposition already says to stop repeat-window refinements (RULE30-GPT.md:16266). L(b)-(c) re-enter the closed height-coupling route (MAHLER.md:185-186). STAM is false on a full-measure set because the fractional window is completely free (MAHLER.md:28-30), which the proposer concedes. Step 3 also misapplies Subspace: the 2-adic form depends on n_r, so the linear forms are not fixed. The test's outcome is fixed in advance by Borel-Cantelli. Worth keeping is one sentence: Mahler's xi lacks a second, independent family of approximations with coprime S-unit denominators. That is a precise way to say what is missing, though not a route.
- **Mahler as a one-sided discounted discrepancy: an EDP-shaped factorisation of "no Z-number" into a two-point log law for every T-orbit (C2) and a Diophantine shadow lemma (D)** (novelty 2, grip 2, testable 1, overall 1): Upheld. The identities I1-I4 are right. But C2 follows from Andrieu-Eliahou-Vivion's Conjecture 1.6 at k = 2, whose mod-4 case already gives Mahler (MAHLER.md:62-64). So C2 + D splits Mahler into two open single-orbit cases on one property (odd log-density). D's 'equivalently' is false. My hand check of the skeptic's construction (ones every third place on doubly exponential blocks) gives log-density about j/(3*2^j) -> 0 while the upper natural density is 1/6. The Erdős discrepancy problem is absent from the record (RULE30-PRIZE.md:8003-8005), but its enabling ingredient, multiplicativity, has no analogue here: multipliers act anti-invariantly and do not single out integers (INSTINCT-CLOUD.md:127-130). The bounded test repeats S1, which measured the coin (MAHLER.md:246-248).
- **The Motzkin kernel root: the centre column is the AND-event field evaluated at one algebraic point, so the GF(2) door needs only c not in one fixed quadratic field (not "never automatic")** (novelty 2, grip 3, testable 1, overall 1): The algebra is correct; both skeptics verified KR and the Artin-Schreier field. KR is 8.100's variation-of-constants identity (RULE30-PRIZE.md:6781-6789) written as generating functions. The 'correction' to the GF(2) door cell (RULE30-PRIZE.md:6925-6928) is formally true but vacuous. Any door needs at least c not in F_2(T). K is just one field between F_2(T) and the algebraic closure, and no precedent excludes membership of a fixed field for a non-algebraic specialised series. The Frobenius descent needs a closure of the 2-kernel that the record measured absent (RULE30-PRIZE.md:479; RULE30-GPT.md:12128-12150). The math skeptic's replica scores the single seed as a coin. File KR as a notation note only.
- **Host tradeoff: the base-3 digit-window measures of 2^n are a genuinely x2x3-invariant object, but a single exception can reach them only through transverse propagation, and Host's theorem confines that propagation to zero entropy** (novelty 3, grip 1, testable 2, overall 2): Claims A and B check out (math skeptic), and Claim A's carry bound and the BS(2,3) relation are new to the record. By construction, though, a single exception gets weight 0 in every Følner limit. Claim B needs infinitely many exceptions plus density-delta propagation, so it is a set statement (INSTINCT-CLOUD.md:127-130), and its one escape is the parked zero-entropy third regime (RULE30-PRIZE.md:2959-2960). The record already files measure rigidity as 'a reference, not a room' (CONSTELLATION.md:905-911). The full-spec run already fails the stated prediction (j* = 9 against <= 7, 8). Value: a sharper reason to close the lens. No route.
- **A finite-automaton inductive invariant for the single orbit 2^n in base 3 (Erdős, the only Π_1 problem of the four)** (novelty 4, grip 4, testable 3, overall 3): This is the only route whose success condition is a finite, exactly checkable object about the one orbit. Erdős is Pi_1 (RULE30-PRIZE.md:6760-6762), and no closed route covers this. Q3's closure is for Rule 30 and is conditional (RECORD-MAP.md:354-356), so the record skeptic's 'not refuted' stands. I uphold the math skeptic only on the test and the kill. The census at three states or fewer returns a null that FA and not-FA both predict. Kill (1) is false as written, since N minus {3^j, 2*3^j} is x2-closed and regular. That refutes the test, not Conjecture FA. Obstructions 3a-3e are precise and correct, and they show why low-digit, leading-digit and congruence invariants all fail. The prior is low: busy-beaver closed-language methods stopped at Antihydra (RULE30-PRIZE.md:6734-6737; PRIOR-ART.md:1495-1497). Erdős is a test bed with no prize (PRIZE-PROBLEMS.md:352).
- **Hereditary inflation for Collatz: one counterexample brings at least x^0.84 more below x (Krasikov-Lagarias), which lifts the target above the square-root barrier, though probably only by repeating the counterexample's single future** (novelty 3, grip 2, testable 1, overall 2): The inflation lemma is correct and Krasikov-Lagarias is absent from the record, though the lemma is probably folklore. By the proposer's own decomposition, the x^0.84 companions are copies of one bit, so the target returns to a count below one at scale x^0.16. The record's binding obstruction is errors that are polylog against a needed precision that is exponential (COLLATZ-PRIZE.md:165-171), not the square-root clause (COLLATZ-PRIZE.md:319) that the proposal attacks. The required x^-0.16 is still 2^(-0.16w). Lasting value: a comb note that :319 should cite :170. The test is decided as HALT in advance (skeptic's rho of about 0.004).
- **Erdős as a safety property: an automaton invariant closed under x4 would prove that 4^m always has a ternary 2, and if none exists, Erdős is unprovable by automatic induction** (novelty 3, grip 4, testable 3, overall 3): The same door as proposal 5 in a cleaner form. Multiplication by 4 preserves the residue mod 3 and the lowest nonzero digit, E holds iff 1024 is not in B*, and the definability point (existential tracks add nothing, by Büchi-Bruyère) is a real logic contribution. The named-conjecture negative (the n-conjecture covers only k < 0.387m) is correct and new. The math skeptic is right that K2 as written is false: {x = 2 mod 3} is x4-closed and C*-free because 4 = 1 mod 3. I partly overrule the claim that the route 'renames the wall'. Unlike the other nine, its crossing is a finite object whose existence is decidable size by size, and nothing in the record rules it out. Judge's unexpected check (predicted null, held): the skeptics searched least-significant-digit-first automata only, and minimal DFA size depends on reading direction. Reading most-significant digit first, 2,128,064 canonical 4-state tables (plus all smaller ones) give 0 x4-closed sets that avoid C* and contain any element whose lowest nonzero digit is 1. Controls passed and the run took 37 s. Still missing: Lagarias Lemma 4.1 at M = 4 (PRIOR-ART.md:2663) and the unread Abram-Lagarias papers (PRIOR-ART.md:2670).
- **Multiplier exclusions are filters, not levers: a compactness dichotomy and a uniform pair-horizon bound for Mahler's K, which close the multiplicative lens and name the one escape (a 2-adically discontinuous forcing map, i.e. GC664's T(M))** (novelty 2, grip 1, testable 1, overall 1): Upheld. B1 is König's lemma on a finitely branching tree the record already uses (RULE30-PRIZE.md:7982; RULE30-GPT.md:19959). B2 restates certificate depth, and B3b is a tautology. B3c's 'only' is unproved and is contradicted by GC667's integer-only gap bound, which excludes an admissible aperiodic code without any T(M) (RULE30-GPT.md:16274-16285). The conclusion is S10's Return (INSTINCT-CLOUD.md:127-130). Every predicted number in the test follows from certificates already in the record. Honest, but adds no lever.
- **Darkness is paid for: a time-average (fringe-visibility) form of LR, certified by a potential that may grow linearly** (novelty 2, grip 2, testable 2, overall 1): Upheld. The certificate step, g* = max over walks, is G183's least-potential restatement (PROOFS.md:7545). Arctic interpretations are Q3's original family (PERIOD-TWO.md:252), so Q3's reopening condition is not met. DG implies a linear run law, which makes BX 8.38's uniform cost (RULE30-PRIZE.md:2672-2673). The precedent's enabling ingredient, a compact expanding system with a continuous observable, is absent. The math skeptic's full run is inconclusive by the proposal's own rule: the periodic word '01' gives bright density 1/7.
- **Not 'sets against one object' but 'is there a front': the record's own Proposition 19 crossed this wall for Rule 210, so search Rule 30's diagonal pair recurrence for a gated clearing-front identity** (novelty 2, grip 3, testable 3, overall 2): W1 holds as a wording correction. Proposition 19 (PROOFS.md:1240-1283) and Condrey prove statements about each finite seed at unbounded width, so P3's sentence (RULE30-PRIZE.md:6913-6921) is better replaced by 8.45's form (RULE30-PRIZE.md:2951-2952, :2959-2960). The route fails. Proposition 19 holds where LR is false (RULE30-PRIZE.md:4398-4406), so a life law of its form cannot give R(d) finite. CF as formalised is met only by the light-cone tautology M = P OR Q. My hand check of that identity: input 00 keeps M, 01 or 10 set it, 11 flips it. With Proposition 19's clearing property required, N30 = 0 (skeptics' runs). Invisible right fringes (PROOFS.md:1296-1313) break step (d), and mechanism step 2 is wrong because cell -1's update is affine beside the clock. It remains the one in-house crossing template on a prize problem, and a richer clearing-marker search (two pairs, or three ticks) is a bounded, new test.

**Verdict on the wall.** The one-wall story holds for the three Pi_2 problems, but it needs restating, and it is not shown for the one Pi_1 problem. Nine of the ten proposals ended where their own honest_weakness predicted. Each crossing step did one of three things. Some restated the problem: STAM, C2+D, C_K, D_theta, DG's g*, B3's T(M). Some produced a set-level or no-go statement: the Host tradeoff and the multiplier filters. One misread the record's operative obstruction: the inflation lemma, against COLLATZ-PRIZE.md:165-171. Two corrections follow. (1) The slogan in 8.101 P3, 'every single-object rigidity theorem controls bounded complexity' (RULE30-PRIZE.md:6913-6921), is literally contradicted by Condrey and by Proposition 19 (PROOFS.md:1240-1283), which prove statements about each finite seed at unbounded width. The accurate wall is 8.45's: nobody gets emptiness from a constrained side of positive entropy (RULE30-PRIZE.md:2951-2952), with the parked zero-entropy third regime between (RULE30-PRIZE.md:2959-2960). (2) For Erdős, the wall has not been tested beyond tiny sizes. Regular inductive invariants for 2^n in base 3 are covered by no closed route. They are measured only up to four states: by the skeptics reading least-significant digit first, and by my most-significant-first census, which also gave 0 at four states or fewer. Priors stay low because of the Antihydra precedent (RULE30-PRIZE.md:6734-6737). SINGLE BEST NEXT BLOCK: decide the corrected rigidity lemma, 'every 3-recognisable x4-closed set containing an element whose lowest nonzero digit is 1 meets C*'. First read Abram-Lagarias, arXiv 1308.3133 and 1508.05967 (names only at PRIOR-ART.md:2670), and check what bbchallenge's finite-automata deciders say about the Stérin-Woods machine (CONSTELLATION.md:985-986). Then attack by hand with pumping plus the x4 transducer. Multiplying by 4 keeps the denominator 3^p - 1, so a periodic middle keeps its period up to a bounded transient, and middle and bottom can be steered mod 3^p - 1 and mod 3^k. The top end, 4^j times a fixed block, is where an Erdős coincidence remains, and that is the step to watch. Then run one preregistered SAT search at 5 to 8 states in both reading directions, with exact re-verification. Either outcome is a theorem the record lacks. A proof makes the wall formal for automatic induction on the Pi_1 problem. A counterexample is the first regular x4-invariant structure beyond congruences, and it reopens the certificate route. Cap it at one block, since Erdős carries no prize (PRIZE-PROBLEMS.md:352). File the free corrections alongside: P3 reworded to the 8.45 form, COLLATZ-PRIZE.md:319 pointed at :170, and KR, Claims A and B and the inflation lemma as single-party PROOF-SKETCH entries."]

## Judge: the verification engineer

Top three: A finite-automaton inductive invariant for the single orbit 2^n in base 3 (Erdős, the only Π_1 problem of the four); Erdős as a safety property: an automaton invariant closed under x4 would prove that 4^m always has a ternary 2, and if none exists, Erdős is unprovable by automatic induction; Not 'sets against one object' but 'is there a front': the record's own Proposition 19 crossed this wall for Rule 210, so search Rule 30's diagonal pair recurrence for a gated clearing-front identity

- **Two-place stammering certificates for Mahler's T-code (Adamczewski-Bugeaud in base 3/2 at S = {inf, 2, 3}): the integer side collapses Subspace to Liouville, i.e. to the window principle W1** (novelty 1, grip 2, testable 1, overall 1): Both skeptics are right. Lemma L(a) is GC666's repeat budget word for word, and the record's disposition there is 'Stop repeat-window refinements' (RULE30-GPT.md:16255-16266). L(b)-(c) re-enter the closed joint real/2-adic approximation route (MAHLER.md:184-186). STAM is false on a full-measure set, because the window's hold set is all of [0,1/2) (MAHLER.md:28-30); so the crossing is a beta-shift (set) statement, and restricted to integers it is Mahler itself. Step 3 also misapplies Subspace: its 2-adic form depends on n_r, so the forms are not fixed. Borel-Cantelli fixes the test's E = 0 in advance, and its integer control repeats GC668. The math skeptic's reduced run already broke the stated bound of 25 (it gave 28.49). Nothing here could be decided tonight. The one lasting item: the sentence 'rational small-place coefficients collapse Subspace to Liouville' explains the non-transfer that PRIOR-ART.md:1502-1503 only asserts.
- **Mahler as a one-sided discounted discrepancy: an EDP-shaped factorisation of "no Z-number" into a two-point log law for every T-orbit (C2) and a Diophantine shadow lemma (D)** (novelty 2, grip 2, testable 1, overall 1): (I1)-(I4) and the reduction lemma check out (math skeptic: 0 mismatches). But C2 plus D is a two-case split of Mahler on one property. C2 is implied by the in-print AEV equidistribution condition, whose mod-4 case alone already gives Mahler (MAHLER.md:62-66). C2 also fails for formal codes such as (1010)^infinity (MAHLER.md:64-66), so any proof must use integer-ness, which is exactly the missing integer-only ingredient (INSTINCT-CLOUD.md:127-130). D's 'equivalently' is false: the skeptic built a doubly-exponential block counterexample. Tao's transfer needs multiplicativity, and every multiplier tested is an anti-symmetry that excludes no single integer (MAHLER.md:259-262). The bounded test re-measures the coin that S1 already measured. Its only novelty is naming the Erdős discrepancy problem as a mechanism, which the record lacked (RULE30-PRIZE.md:8003-8005).
- **The Motzkin kernel root: the centre column is the AND-event field evaluated at one algebraic point, so the GF(2) door needs only c not in one fixed quadratic field (not "never automatic")** (novelty 3, grip 3, testable 2, overall 2): KR is correct: the proposer and the math skeptic each checked it to 700 coefficients, and the Artin-Schreier field K is new notation. But KR is 8.100's variation-of-constants identity written as a generating function (RULE30-PRIZE.md:6781-6789). C_K is strictly stronger than the prize, so the proposed 'correction' leaves 8.101's cell sentence true (RULE30-PRIZE.md:6897). The Cartier split is generic. Christol needs a finite kernel, and the record measured the kernel as not finite (T6, RULE30-PRIZE.md:479; GC486/487, RULE30-GPT.md:12128-12150). Grip is genuine, since this is one seed's column, but the K-Hermite-Pade defect scored as a coin (max delta 5, against 6 for a coin). That sits inside the record's finite-N limit (PERIOD-TWO.md:238). The record skeptic's replacement is an exact finite computation: the rank deficiency that the forced wall events impose on the level-1/2 descent systems, against random events. It could run tonight, but its prior is low.
- **Host tradeoff: the base-3 digit-window measures of 2^n are a genuinely x2x3-invariant object, but a single exception can reach them only through transverse propagation, and Host's theorem confines that propagation to zero entropy** (novelty 3, grip 1, testable 2, overall 1.5): Claims A and B check: the carry bound reproduces j_max, and the Host step is valid apart from a fixable atom-at-0 gap. Claim A, the BS(2,3) relation and the Duke/ELMV/BLMV precedents are new to the record. But Claim B needs infinitely many exceptions and propagation at positive density, so it is ineffective and set-level. Its named escape is the parked zero-entropy third regime (RULE30-PRIZE.md:2954-2963). Its conclusion is 8.47's 'a proof must work point by point' (RULE30-PRIZE.md:3008-3010) and the record's Rudolph entry (CONSTELLATION.md:909-911). The test (9.4 s) missed its own prediction: j* reached 9 to 11 at w = 6 and 7. The late deficits do not depend on L, so they are a property of the x2^j transducer acting on the full 2-shift, not of powers of 2. Close the lens and keep Claims A and B as a side note.
- **A finite-automaton inductive invariant for the single orbit 2^n in base 3 (Erdős, the only Π_1 problem of the four)** (novelty 4, grip 5, testable 2, overall 3): This is the one proposal whose success object is a finite, exactly checkable proof of the strong conjecture for the one orbit. Lemma M is correct, and the three checks are exact product-automaton computations. Acceptance on finite canonical numerals is the integer-only ingredient that S10 asks for (INSTINCT-CLOUD.md:127-130). No closed route covers it: Q3's closure belongs to Rule 30 and is conditional (PERIOD-TWO.md:219). 8.113 predicted this lens (RULE30-PRIZE.md:8012-8014). Erdős is Pi_1, so certificate and statement match in type (RULE30-PRIZE.md:6760-6762). I overrule the math skeptic's 'refuted' only in scope. What it refuted is the test (cert = 0 at <= 3 states, which both sides predict) and kill (1)'s wording (N minus {3^j, 2*3^j} is x2-closed and regular but not a congruence union). Conjecture FA itself stands. The weaknesses also stand. The prior is low: busy-beaver regular invariants stopped at Antihydra (RULE30-PRIZE.md:6733-6737; PRIOR-ART.md:1495-1497). Erdős is 'a test bed, not a prize' (PRIZE-PROBLEMS.md:350-352). The informative next step, SAT at 5 to 12 states with UNSAT certificates, is not a five-minute standard-library run.
- **Hereditary inflation for Collatz: one counterexample brings at least x^0.84 more below x (Krasikov-Lagarias), which lifts the target above the square-root barrier, though probably only by repeating the counterexample's single future** (novelty 4, grip 1, testable 2, overall 2): The inflation lemma holds: if B is nonempty then E(x) >= x^0.84, from KL's uniform-in-a statement. KL is absent from the record; record_find 'Krasikov' hits only 8.113's own summary at RULE30-PRIZE.md:8039. But D_theta is the OPEN counting form at a polynomial threshold (COLLATZ-PRIZE.md:347), about 10 log2 x steps past the free bits. Its precision of 2^(-0.16w) is still exponentially beyond Tao-type errors, which is the binding obstruction at COLLATZ-PRIZE.md:165-171. The companions are copies of one bit, so this is a count, not a single object. The test's rho = 0.004 says nothing about provability. The lasting value is a record correction. The CLOSED row (COLLATZ-PRIZE.md:350) rests on the square-root ceiling (COLLATZ-PRIZE.md:318-321), but the reason that actually binds is section 4's precision gap, and for hereditary statistics the 'density form' at COLLATZ-PRIZE.md:321-322 is the prize itself.
- **Erdős as a safety property: an automaton invariant closed under x4 would prove that 4^m always has a ternary 2, and if none exists, Erdős is unprovable by automatic induction** (novelty 3, grip 5, testable 2, overall 3): This is the same route as proposal 5, in the cleaner x4 form (odd n are excluded by their last digit). It adds three things that hold up: the Buchi-Bruyere definability equivalence (auxiliary tracks gain nothing); the Pi_1-safety versus Pi_2-liveness classification, which the record notes only as a safety net (RULE30-PRIZE.md:6760-6762); and a worked negative on named conjectures (the n-conjecture reaches only k < 0.387m). K2 as written is false: L1 = {x = 2 mod 3} and L2 are x4-closed, regular and avoid C*. The corrected K2' (an element whose lowest nonzero digit is 1) is the crispest theorem target the swarm produced. Proved, it closes automatic induction for Erdős uniformly; refuted, it gives the first non-congruence structure. The seed-free variant is already null at <= 4 states (4,817,070 candidates, 24 s), so tonight's standard-library test is spent. I partly overrule the math skeptic: recasting the wall as a statement decidable at each state bound is not the same as recasting it as another open infinite statement. My unexpected check (see verdict) shows that K2' has an Erdős-type core at the top end, so pumping alone will not prove it.
- **Multiplier exclusions are filters, not levers: a compactness dichotomy and a uniform pair-horizon bound for Mahler's K, which close the multiplicative lens and name the one escape (a 2-adically discontinuous forcing map, i.e. GC664's T(M))** (novelty 2, grip 1, testable 1, overall 1): B1 is Konig's lemma on the odd joint tree, and the record already states that a finite certificate decides whenever the tree dies (RULE30-PRIZE.md:7982). B2 is F2 plus existing certificates, and B3b is a tautology. B3c's 'only' is unproved: S5 says no other integer-only invariant exists, yet GC666 and GC667 are integer-only bounds (RULE30-GPT.md:16255-16266). The thesis 'filters, not levers' is S10 and MAHLER.md:261 verbatim. The record skeptic replayed the test and read every predicted value off existing certificates. The one finite decision on offer, running 5's and 9's trees to extinction, is set-level. I agree with both skeptics.
- **Darkness is paid for: a time-average (fringe-visibility) form of LR, certified by a potential that may grow linearly** (novelty 3, grip 2, testable 2, overall 1.5): DG implies LR and a linear run law, so proving BX is at least 8.38's uniform cost (RULE30-PRIZE.md:2672-2673), which is Q1, parked with no mechanism (PERIOD-TWO.md:204). BX with the minimal g is DG restated, which is G183's least-potential restatement (PROOFS.md:7543-7545). The one named family fails: it is not a function of the merged state, and its sign is wrong on dark steps. Both skeptics' runs give the coin (bright fraction 0.112 against 0.110) and land in the proposal's own HALT band. Periodic word 01 gives density 1/7, consistent with Theorem B's floor. Bousch is new to the record, but his engine (a compact space, an expanding map, a Holder observable and a bounded sub-action) is absent here.
- **Not 'sets against one object' but 'is there a front': the record's own Proposition 19 crossed this wall for Rule 210, so search Rule 30's diagonal pair recurrence for a gated clearing-front identity** (novelty 2, grip 3, testable 3, overall 2): The test ran exhaustively in under a second and decided its question. CF holds with N30 = 4 only through the light-cone tautology M = P OR Q; with Proposition 19's clearing premise required, N30 = 0, and the Rule 210 control passes. So no one-pair, two-tick clearing front exists for Rule 30, consistent with GC479 and GC549 (RULE30-GPT.md:12070, 13668-13703). The route also fails structurally. Proposition 19 holds where LR is false (RULE30-PRIZE.md:4398-4406), so a life law of its form cannot give R(d) finite. Proposition 20's invisible fringes break 'every first difference launches a front' (PROOFS.md:1296-1313). Mechanism step 2 is wrong: given the clock, cell -1's update is affine. But I overrule the math skeptic on W1 as a matter of wording. Proposition 19 excludes Rule 210 seeds of every width at the prize's exact statement (PROOFS.md:1240-1283), so P3's 'bounded complexity / every counterexample's complexity grows with n' (RULE30-PRIZE.md:6913-6921) is false as worded. The actual dividing line is 8.45's linear or eventually periodic constrained side (RULE30-PRIZE.md:2933-2963).

**Verdict on the wall.** In substance the one-wall story holds, but its wording is wrong. None of the ten proposals supplied an ingredient that only integers or finite seeds have, at positive entropy (INSTINCT-CLOUD.md:127-130). Each mechanism failed in one of three ways. Some were restatements: GC666 (RULE30-GPT.md:16255-16266), G183 (PROOFS.md:7543-7545), KR as 8.100's identity (RULE30-PRIZE.md:6781-6789), and C2 below the in-print AEV condition (MAHLER.md:62-66). Some were set statements: STAM is false on a full-measure set (MAHLER.md:28-30), Host needs infinitely many exceptions, the KL companions are copies of one bit, and pair exclusions single out no integer (MAHLER.md:259-262). The rest offered tests whose outcome both sides predict.

P3's wording (RULE30-PRIZE.md:6913-6921), 'bounded complexity; every counterexample's complexity grows with n', is false as stated. Proposition 19 (PROOFS.md:1240-1283) excludes Rule 210 seeds of every width at the prize's exact statement, and Condrey does the same at period 1. What these crossings share is a linear or eventually periodic constrained side. The accurate wall is therefore 8.45's: get emptiness from a constrained side of positive entropy (RULE30-PRIZE.md:2933-2963), plus S10's integer-only ingredient. Two smaller corrections follow:
- P3 should cite Proposition 19 and Condrey.
- COLLATZ-PRIZE.md:350 should rest on section 4's precision gap (COLLATZ-PRIZE.md:165-171), not the square-root ceiling (COLLATZ-PRIZE.md:318-321).

The single best next block is the Erdős automaton barrier, because it is the only place where the wall is itself a finite question. Erdős is Pi_1 (RULE30-PRIZE.md:6760-6762), so a regular x4-closed invariant is a complete, exactly checkable proof, and its absence at each state bound is a SAT instance. The block has four steps:
1. A seed-free SAT search, LSB-first and MSB-first, at 5 to 10 states, for x4-closed 3-automatic sets that contain an element with lowest nonzero digit 1 and avoid the {0,1}-digit set, plus the seed-1024 variant. UNSAT results get certificates checked by a verified checker.
2. The owed primary-source check of whether finite-automata-reduction deciders were ever run on the Stérin-Woods machine (CONSTELLATION.md:985-987).
3. A hand attempt at the corrected K2'.
4. Predictions written first: a null at about 0.95.

Erdős carries no cash prize (PRIZE-PROBLEMS.md:350-352). The block's worth is turning the wall into a theorem or a certificate.

My unexpected check (single-party self-check, standard library, 0.1 s; a scratch script outside the repo, no repo files written). Take the pumped families a b^k c with |a|,|c| <= 2, 1 <= |b| <= 2 and lowest nonzero digit 1; any regular L containing such a family must also contain all its x4 images. Of 596 families, 150 have no x4^j image inside the {0,1}-digit set for j <= 60, k <= 30. Every hit occurred at j <= 7. Of the 150 failures, 116 have a leading block beginning with 2. So for a fixed leading block, a hit needs an Erdős-type coincidence for 4^j times that block. K2' will not fall to pumping alone, and SAT with certificates is the decision tool for tonight.

Record searched (record_find, one term per run): 'automatic induction' 0 hits, ledgers included; 'Krasikov' 1 hit (RULE30-PRIZE.md:8039, 8.113's own summary); 'multiplicatively closed' 0 hits, ledgers included; 'Proposition 19' hits include CLAUDE-INTEL-HANDOVER.md:85 and :117 (door D7).

## The completeness critic

#### missing_lenses
- Homogeneous dynamics and unipotent rigidity (Ratner's orbit-closure theorem 1991, Margulis's 1987 proof of the Oppenheim conjecture, Dani-Margulis non-divergence), together with the Littlewood and p-adic Littlewood (de Mathan-Teulie) conjectures. This field holds the main stock of theorems about every single orbit at unbounded complexity, and its open conjectures are this same wall: Einsiedler-Katok-Lindenstrauss 2006 show the Littlewood exceptional set has dimension 0, while individual pairs stay open. p-adic Littlewood combines a real place and a p-adic place, which is Mahler's 'one series read in two norms' (MAHLER.md:35-50). The lens would place the wall: single-orbit rigidity exists for unipotent (zero-entropy, polynomially divergent) or higher-rank actions with an entropy floor. It does not exist for rank-one positive-entropy maps, where x2 alone has orbit closures of every dimension. Proposal 4 ran only the diagonal x2x3/Host side. record_find: Ratner 0, Oppenheim 0, unipotent 0, Littlewood 0 (ledgers included).
- Computational complexity: explicit-function lower bounds (Hastad's switching lemma; Razborov-Smolensky) and the Razborov-Rudich natural-proofs barrier. The barrier is a formal theorem about when large, set-level properties cannot single out one explicit pseudorandom object, which is a theorem-shaped version of S10 (INSTINCT-CLOUD.md:123-130). Rule 30 is itself a proposed generator (PRIOR-ART.md:1184-1190). The record lists 'Literature first (circuit lower bounds for CA traces)' as an unread row (CONSTELLATION.md:61). Proposal 7 ran Buchi definability but no complexity barrier. record_find: natural proof 0, Razborov 0, Hastad 0, pseudorandom generator 0.
- Effective Diophantine approximation through Pade or hypergeometric approximants (Thue's method: Beukers 1981, then Dubitskas, Bennett, Habsieger and Zudilin for ||(3/2)^k||). Proposal 1 ran only the ineffective Subspace and Adamczewski-Bugeaud route. Its own verdicts named the missing ingredient as 'a second, independent family of approximations', and that is exactly what hypergeometric approximants supply for xi = 1. That this fails for an unknown xi should be shown, not assumed. record_find: Beukers 0, Zudilin 0, hypergeometric 0, Bennett 0, Thue.*method 2 (both unrelated).
- Character sums and sieves for run lengths of one explicit sequence: Vinogradov's trick and Burgess's bound for the least quadratic nonresidue, and the large sieve. This is the classical template for 'one explicit sequence cannot stay in a constrained state for long, at every modulus', which is the shape of R(d) finite (PERIOD-TWO.md:39-47) and of the Mahler and Collatz horizon bounds. Its enabling ingredient (multiplicativity giving smooth-number self-copies, plus Weil) is exactly the transfer device that proposal 2's verdicts found missing. record_find: Burgess 0, Weil 0, nonresidue 0.
- Thermodynamic formalism and transfer-operator spectral gaps (Ruelle-Perron-Frobenius, Lasota-Yorke/Hennion quasi-compactness, Dolgopyat). Q1 asks for a uniform rate with a depth-free constant (PERIOD-TWO.md:182; RECORD-MAP.md:38-39), which is a width-uniform spectral-gap statement for the layer transfer matrices the record already builds (RULE30-PRIZE.md:1783-1804). Q1 is PARKED with 'no mechanism named', and this is the standard named family of mechanisms. record_find: spectral gap 0, transfer operator 0, Ruelle 0, Lasota 0.
- Additive combinatorics and exponential sums over thin multiplicative sets, with theorems on digits of sparse sequences (Korobov's sums of a^x mod p^k; Bourgain-Glibichuk-Konyagin; Mauduit-Rivat; Maynard 2019). Run on Erdos, this would locate that wall exactly: the trailing-digit question needs equidistribution of 2^n mod 3^k over n-ranges of length about k*log2(3), logarithmic in the modulus and below every known threshold (modulus^eps). None of the three Erdos lenses (4, 5, 7) computed anything on the actual orbit 2^n beyond 512 and 1024. record_find: Korobov 0, Mauduit 0, Maynard 0; Bourgain appears only in 8.113's novelty-check line (RULE30-PRIZE.md:8005).
- Anti-concentration and Littlewood-Offord theory for Collatz cycles. Tao's 2011 blog post 'The Collatz conjecture, Littlewood-Offord theory, and powers of 2 and 3' links cycle exclusion to the ternary digits of powers of 2 (named from memory; primary read owed). It would join the under-covered Collatz to Erdos. In the record, the nearest theorem for the cycle fold is Baker at a bounded number of runs (RULE30-PRIZE.md:6913-6914). record_find: Littlewood.Offord 0; anti-concentration 1, unrelated (RULE30-GPT.md:10083).
- Diophantine approximation on fractals (Kleinbock-Lindenstrauss-Weiss friendly measures 2004; Levesley-Salp-Velani 2007 on Mahler's Cantor-set question; Einsiedler-Fishman-Shapira 2011; Shparlinski on rationals in the Cantor set). The object of this field is exactly 'specific points against a self-similar set', the record's Erdos set C and Mahler set K (CONSTELLATION.md:996-1000; MAHLER.md:35-50). record_find: Velani 0, Kleinbock 0, Shparlinski 0, 'Diophantine approximation on' 0.
- Algorithmic randomness and effective dimension (the Lutz-Lutz point-to-set principle). It is the one general tool that turns Hausdorff-dimension (set) statements into statements about individual points. It fails here because K and S_strict contain computable points such as -9/19 (MAHLER.md:47). Stating that failure exactly would turn S10 from a reading into a precise obstruction for a named class of methods. record_find: point-to-set 0, effective dimension 0; Kolmogorov complexity 1 (RULE30-PRIZE.md:6210).

#### missing_precedents
- Margulis 1987 (Oppenheim conjecture): one irrational indefinite quadratic form in at least 3 variables takes values on Z^n arbitrarily close to 0, for every eps. Ratner 1991: every unipotent orbit has a homogeneous closure. Both are theorems about each single object at unbounded complexity. The enabling ingredient is polynomial divergence of unipotent flows plus Dani-Margulis non-divergence, and the four problems lack it: each is rank-one and hyperbolic with positive entropy. record_find: Ratner 0, Oppenheim 0.
- Bilu-Hanrot-Voutier 2001: every Lucas or Lehmer term u_n has a primitive divisor for n > 30. Zsigmondy/Bang give the same for a^n - b^n. These are every-n theorems at unbounded n, proved by Baker's method cutting the problem to finitely many n and a computation finishing them. That is the BB(5)-shaped reduction the record calls missing (RULE30-PRIZE.md:6707-6710), done in number theory. It bears on Mahler: periodic codes have the values C/(3^s - 2^s), and Conjecture U's survivors have denominators 3^g - 2^g (MAHLER.md:189-195). record_find: Zsigmondy 0, Bilu 0, primitive divisor 0.
- Beukers 1981, improved by Dubitskas, Bennett, Habsieger and Zudilin: effective lower bounds for ||(3/2)^k|| for every k past an explicit k_0, from about 2^(-0.9k) to about 0.58^k (figures from memory). The method is hypergeometric Pade approximation. This is a single object (xi = 1), effective, at unbounded k. The record has only Mahler 1957 via Ridout, which is ineffective and named from memory (RULE30-PRIZE.md:7812-7813). record_find: Beukers 0, Zudilin 0.
- Burgess 1957, after Vinogradov: the least quadratic nonresidue mod p is below p^(1/(4 sqrt e)+eps) for every prime p. An explicit sequence (the Legendre symbol) cannot keep a constant value on an initial run, at every modulus. This is the R(d)-shaped theorem, proved by multiplicativity (smooth-number self-copies) plus Weil-based amplification. record_find: Burgess 0, nonresidue 0.
- Hastad 1986 and Razborov-Smolensky 1987: PARITY, one explicit function family at every n, needs exponential-size AC0 (respectively AC0[p]) circuits. The proof uses random restrictions, a set argument made to grip one explicit object. The matching barrier is Razborov-Rudich 1997 (natural proofs). record_find: Razborov 0, Hastad 0, natural proof 0.
- Mauduit-Rivat (sum of digits of primes, Ann. of Math. 2010; of squares, Acta Math. 2009), Drmota-Mauduit-Rivat (Thue-Morse along squares is normal, 2019) and Maynard (infinitely many primes with a missing digit, Invent. Math. 2019). These are digit statements along one specific sparse sequence, the nearest mainstream analogue of Erdos's 2^n against the 0/1 ternary digit set. Their engine is carry truncation plus small-L1 Fourier bounds on digit sets, and it needs sums longer than modulus^eps, which Erdos lacks. record_find: Mauduit 0, Maynard 0.
- Bhattacharya 2016 and Greenfeld-Tao 2021: every tiling of Z^2 by one finite tile is periodic or weakly periodic, a structure theorem for every solution of a local constraint at unbounded complexity. The engine is the dilation lemma, a Frobenius-type identity over Z, which is exactly the 'Frobenius descent' proposal 3 wanted. It works because the constraint is a linear convolution equation; Rule 30's AND removes that (RULE30-PRIZE.md:7810, the 0.496 time-doubling coin). record_find: Bhattacharya 0, Greenfeld 0.
- Bailey-Borwein-Crandall-Pomerance 2004: every algebraic irrational of degree D has at least about n^(1/D) ones among its first n binary digits. One object, a digit count growing with n, elementary proof (from memory). It sits beside Senge-Straus/Stewart in 8.101's 'counts digits, not which' cell (RULE30-PRIZE.md:6913-6915). record_find: Borwein 0.
- Tao 2011 (blog): Collatz cycles, Littlewood-Offord anti-concentration and the ternary digits of powers of 2 (from memory, primary read owed). It is the one known bridge between two of the four problems. record_find: Littlewood 0.
- Four precedents already in the record but missing from 8.101's precedent table and unused by every proposal: Condrey (period 1 for every finite configuration of any width), Kopra's p/q theorem (one column of every nonzero finite configuration is never eventually periodic, using left-finiteness as a shrinking real value; PRIOR-ART.md:2322), Alon-Behajaina-Paran (every polynomial reaches stopping in O(deg^1.5) under polynomial Collatz; PRIOR-ART.md:2461) and Bunimovich-Troubetzkoy (every Langton's-ant trajectory is unbounded; PRIOR-ART.md:1592-1594). Each fails to transfer for a structural reason (width and invertibility, linearity of the carry, reversibility), not because it controls bounded complexity. So P3 (RULE30-PRIZE.md:6913-6921) is a weaker classification than the proposals and verdicts treated it as.

#### under_covered_problem
Collatz. It got 1 of the 10 lenses: proposal 6, the only Collatz item in 8.113's interim list (RULE30-PRIZE.md:8039-8055). Mahler, Erdos and Rule 30 got three lenses each (proposals 1, 2, 8; 4, 5, 7; 3, 9, 10). The one Collatz proposal attacked a density statistic (D_theta), which both verdicts filed as the OPEN counting form under a new threshold (COLLATZ-PRIZE.md:165-171). The single-object structure of Collatz was left untouched:
- the cycle fold, where the nearest theorem is Baker at a bounded number of runs (RULE30-PRIZE.md:6913-6914);
- Proposition 24, which says every orbit's parity column ends in 1010... (PROOFS.md:1812);
- Dubickas's P(X,n) = 2^n conjecture;
- the anti-concentration link to the ternary digits of 2^n.

Collatz is also the only one of the four with cash prizes on the record's own account: the 120M-yen prize and Erdos #1135 at $500 (PRIZE-PROBLEMS.md:342-345; COLLATZ-PRIZE.md:13-14). Mahler 'carries no prize at all' (NOW.md:37; MAHLER.md:3), and Erdos's ternary question is 'a test bed, not a prize' (PRIZE-PROBLEMS.md:352). COLLATZ-PRIZE.md's honest summary is frozen at 2026-10-05 (COLLATZ-PRIZE.md:13-16), and Q9 is PARKED with 'nothing since 2026-10-09' (PERIOD-TWO.md:201).

A secondary gap inside Rule 30: no proposal targeted the actual main line, R_real(d) finite at every depth (PERIOD-TWO.md:43-47). Proposal 3 aimed at C_K (strictly stronger than the prize), proposal 9 at unrestricted DG/LR, and proposal 10 at LR. Rule 210 shows that a Proposition-19-type law coexists with LR false (RULE30-PRIZE.md:4400-4406).

#### unverified_claims
- 'Erdos is Pi_1 (Sterin-Woods)' (RULE30-PRIZE.md:7809; CONSTELLATION.md:985). The Sterin-Woods machine proof has not been audited (RULE30-GPT.md:31245). Erdos is Pi_1 by inspection, since for each n the predicate is decidable by writing 2^n in base 3, so the unaudited reduction carries nothing. Proposals 5 and 7 build their discriminator on Pi_1, and Antihydra's non-halting is also Pi_1 (proposal 5 record verdict).
- 8.101 P3, 'every single-object rigidity theorem found controls bounded complexity' (RULE30-PRIZE.md:6913-6921), is a 'reading, not a theorem'. Its literature is named from memory, and the second read is still owed (RULE30-PRIZE.md:7812-7813). The record's own counter-instances are absent from its table (PRIOR-ART.md:2322, 2461, 1592-1594). Even so, the verdicts on proposals 3, 7 and 10 used it as a ground for refutation.
- The exponential-sum closure rests on two unchecked items. The CLOSED reason, 'the error is never below the square root of the population' (COLLATZ-PRIZE.md:318-321; RECORD-MAP.md:370), is a heuristic. The obstruction both proposal-6 verdicts moved it to (COLLATZ-PRIZE.md:165-171) rests on Tao's 'Proposition 1.14, cited from memory' (COLLATZ-PRIZE.md:167).
- 'Verified by computer for every start below 2^71' (COLLATZ-PRIZE.md:14) has no source anywhere in the record.
- Proposal 6's math verdict says 'KL's bound is uniform in a'. The proposal's own quote of Krasikov-Lagarias reads 'for large enough x (depending on a)' (proposal 6, K1), so the uniformity is asserted against the source; the inflation lemma needs only a fixed a. The same verdict's 'the lemma is probably already noted in the literature' is unchecked.
- Proposal 3's record verdict says a quadratic element of F_2((1/x)) has an eventually periodic continued fraction, so c in K would force bounded Berlekamp-Massey jumps. This is from memory. K is defined by a root phi in F_2[[T]] (the T-adic completion), while continued fractions and Berlekamp-Massey work in the other completion, and the transfer between them is not checked.
- Proposal 10, mechanism step 2: 'Rule 30 is nonlinear at the wall every odd tick'. The math verdict shows this is false: cell -1's update is affine once the clock is a known input. The record verdict never tested it, so the two skeptics disagree on a point of fact and the record verdict's framing should not be filed.
- Proposal 1 states Adamczewski-Bugeaud, Bugeaud-Kim and Eliahou 1993 from memory, and also 'no Subspace argument has given more than superlinear complexity for any algebraic irrational'. Its math verdict predicts 'the full grid's extreme zero-run near log_1.5(4e5) = 32' without running it.
- Proposal 4 states the hypotheses of Host 1995 and the ELMV and BLMV results from memory. Claim B has a continuity gap at an atom at 0 (math verdict). Its headline 'no x2x3-invariant object built from the diagram sees an exception' goes beyond the one R/Z construction Claim B covers.
- Proposal 7's arithmetic 'k < 0.387m' depends on the Browkin-Brzezinski exponent 2N-5, cited from memory. Proposals 5 and 7 both describe the BB(5) deciders from memory. The owed check, whether bbchallenge closed-language deciders were ever run on the Sterin-Woods machine, was never done (proposal 5 record verdict).
- Proposal 9 states Bousch 2000 and the Mane-Conze-Guivarc'h lemma from memory. Its record verdict claims 'every finite family that cannot see darkness has an all-dark label-balanced cycle, forcing kappa >= 1 - p*'. That is the reviewer's own derivation from G183 (PROOFS.md:7537-7545), and no second party has read it.
- Stephan's 2026 Theorem D underlies the closure 'block certificates cannot reach Mahler's window' (MAHLER.md:51-54; PRIOR-ART.md:2556-2571), which proposal 7's record verdict asks it to engage. The work is from the same model family, its novelty is unknown and it has no specialist review.
- 'The gap is far wider than Mahler's' for Erdos (CONSTELLATION.md:1022-1024) rests on an m_k table whose producing code and definition are not committed (RULE30-GPT.md:31265-31271), and the three Erdos lenses inherited it.
- Line-number drift across the proposals is pervasive and the verdicts flagged it (for example PRIOR-ART.md:1494 vs 1498; PROOFS.md:12559 vs 12573; RULE30-PRIZE.md:7591 vs 7630). The record_find counts in the proposals were taken before a mid-run merge, so their 0-hit novelty claims need re-running at HEAD 955933d7.

#### one_experiment
The 'S10 meter', a paired-twin tail test for Mahler in standard-library Python.

Why every lens needed it: all ten proposals died on S10, the missing integer-only ingredient (INSTINCT-CLOUD.md:123-130). At finite depth the only integer-only ingredient is the tail of the binary expansion: zeros for positive n, ones for negative n (MAHLER.md:55-57; sign test, MAHLER.md:174-175). Three verdicts asked for exactly this test, one separating integer codes from generic codes at a matched prefix: proposal 1's math verdict and the record verdicts on proposals 2 and 8. No proposal ran it.

Design:
- Walk the admissible-prefix tree exactly to depth w. The G51 window is nonempty iff 2C_T*3^s < (2C_s + 2^s)*3^T for the minimising s. Carry y = T^t(r) and use T^t(r + 2^t e) = T^t(r) + 3^t e.
- Hard gate: the node counts must reproduce A(t) = 2, 3, 5, 8, 12, 18, 27, 40, 60, 90, 134, 201, 302, 452, 678, 1018 (MAHLER.md:94-95).
- For every surviving residue r != 0 at depth w, continue the same window with five tails:
  1. x = r, the positive integer;
  2. x = r - 2^w, the negative integer (the dual problem);
  3. and 4. two independent fair-coin parity streams, a generic 2-adic point (negative control);
  5. rational tails x = r + 2^w*q for q = -1/3 and -9/19, the 2-adic shadow points of K (positive control: they must produce cap-hitting twins).
- Report, for w = 16 to 34 even: the mean forced lifetime L for each tail; paired z for positive minus negative, positive minus coin, and coin minus coin; corr(pos, neg); and tail counts N(L >= k) for k = 1 to 24.

Cost: under 1 minute. A breadth-first pass handles w = 31 in 4.5 s; use depth-first above w = 32.

Prediction, from a pilot this critic ran through stdin (no files written, gate passed):
- All means 2.99 to 3.01, against the coin's sum of (3/4)^k = 3.
- z(pos-neg) between -1.21 and +0.76 for w = 16 to 30.
- At w = 31 (446,121 pairs): N(L >= 12) is 14218 positive, 13933 negative and 14220 coin; every tail |z| <= 1.7 for k <= 20, while coin against coin reaches -2.1.
- corr(pos, neg) between -0.04 and -0.09. The cause is that 3^w is odd, so the twins take opposite first forced parities.
- Exactly one cap hit for the -1/3 tail at each even w tested; the -9/19 tail gave one at w = 24 and w = 30.

Decision rule: ACT if a same-sign |z| >= 4 appears at two consecutive w, or if a tail ratio leaves 4 sigma at k >= 10 and replicates at w + 2. Otherwise HALT and file S10 as MEASURED: the integer-only ingredient leaves no footprint in forced-phase lifetimes, to about 0.3% at w <= 34. A proof must then use it through a global height mechanism of the GC666/GC667 kind (RULE30-GPT.md:16238-16291), not through any finite statistic.

The record's only data point is 4499 positive and 4622 negative stragglers at w = 63, against a coin expectation of 4603.7 (tests/probes/mahler/mahler_swarm_tests.py:25-29). It was never analysed as a sign signal.

## Test code as run by the agents (recovered from their transcripts; not re-run by Local)

### refute-math:5, block 1 (Bash)

```
cd /tmp && timeout 58 python3 - <<'EOF'
import itertools, time
t0=time.time()
def census(nst):
    res=[]
    for trans in itertools.product(range(nst), repeat=3*nst):
        t=[trans[3*q:3*q+3] for q in range(nst)]
        # closure BFS: state (p,q,c,r,s,nz); restricted to x = 0 mod 4
        start=(0,0,0,0,1,0)
        seen={start}; stack=[start]; pairs=set()
        while stack:
            p,q,c,r,s,nz=stack.pop()
            if nz and r==0:
                qe = t[q][1] if c==1 else q
                pairs.add((p,qe))
            for d in (0,1,2):
                v=2*d+c
                ns=(t[p][d], t[q][v%3], v//3, (r+d*s)%4, (3*s)%4, 1 if d else 0)
                if ns not in seen:
                    seen.add(ns); stack.append(ns)
        # 2-free in 4N: (p,r,s,nz)
        st=(0,0,1,0); seen2={st}; stack=[st]; cfp=set()
        while stack:
            p,r,s,nz=stack.pop()
            if nz and r==0: cfp.add(p)
            for d in (0,1):
                ns=(t[p][d],(r+d*s)%4,(3*s)%4,1 if d else 0)
                if ns not in seen2: seen2.add(ns); stack.append(ns)
        p=0
        for d in (2,2,2,0,0,2): p=t[p][d]
        p512=p
        for F in itertools.product((0,1),repeat=nst):
            closed = not any(F[a] and not F[b] for a,b in pairs)
            if not closed: res.append((t,F,False,False,False)); continue
            cert = F[p512]==1 and not any(F[a] for a in cfp)
            res.append((t,F,True,cert,None))
    return res
allres=[]
for n in (1,2,3):
    allres+=census(n)
print("automata",len(allres),"time",round(time.time()-t0,1))
closed=[r for r in allres if r[2]]
print("closed",len(closed),"cert",sum(1 for r in allres if r[3]))
# closed that avoid C_fin∩4N and accept 512 regardless
import collections
EOF
```

### refute-math:5, block 2 (Bash)

```
cd /tmp && python3 - <<'EOF'
import itertools, time, signal
signal.alarm(58)
t0=time.time()
def census(nst):
    res=[]
    for trans in itertools.product(range(nst), repeat=3*nst):
        t=[trans[3*q:3*q+3] for q in range(nst)]
        start=(0,0,0,0,1,0)
        seen={start}; stack=[start]; pairs=set()
        while stack:
            p,q,c,r,s,nz=stack.pop()
            if nz and r==0:
                qe = t[q][1] if c==1 else q
                pairs.add((p,qe))
            for d in (0,1,2):
                v=2*d+c
                ns=(t[p][d], t[q][v%3], v//3, (r+d*s)%4, (3*s)%4, 1 if d else 0)
                if ns not in seen:
                    seen.add(ns); stack.append(ns)
        st=(0,0,1,0); seen2={st}; stack=[st]; cfp=set()
        while stack:
            p,r,s,nz=stack.pop()
            if nz and r==0: cfp.add(p)
            for d in (0,1):
                ns=(t[p][d],(r+d*s)%4,(3*s)%4,1 if d else 0)
                if ns not in seen2: seen2.add(ns); stack.append(ns)
        p=0
        for d in (2,2,2,0,0,2): p=t[p][d]
        for F in itertools.product((0,1),repeat=nst):
            closed = not any(F[a] and not F[b] for a,b in pairs)
            cert = closed and F[p]==1 and not any(F[a] for a in cfp)
            avoid = closed and not any(F[a] for a in cfp)
            res.append((t,F,closed,cert,avoid,F[p]))
    return res
allres=[]
for n in (1,2,3):
    allres+=census(n)
print("automata",len(allres),"time",round(time.time()-t0,1))
print("closed",sum(r[2] for r in allres),"cert",sum(r[3] for r in allres),"closed&avoidCfin",sum(r[4] for r in allres),"closed&avoid&has512",sum(r[4] and r[5] for r in allres))
EOF
```

### refute-math:5, block 3 (Bash)

```
cd /tmp && python3 - <<'EOF'
import itertools, time, signal
signal.alarm(58)
def analyse(t,nst):
    start=(0,0,0,0,1,0)
    seen={start}; stack=[start]; pairs=set()
    while stack:
        p,q,c,r,s,nz=stack.pop()
        if nz and r==0:
            qe = t[q][1] if c==1 else q
            pairs.add((p,qe))
        for d in (0,1,2):
            v=2*d+c
            ns=(t[p][d], t[q][v%3], v//3, (r+d*s)%4, (3*s)%4, 1 if d else 0)
            if ns not in seen: seen.add(ns); stack.append(ns)
    st=(0,0,1,0); seen2={st}; stack=[st]; cfp=set()
    while stack:
        p,r,s,nz=stack.pop()
        if nz and r==0: cfp.add(p)
        for d in (0,1):
            ns=(t[p][d],(r+d*s)%4,(3*s)%4,1 if d else 0)
            if ns not in seen2: seen2.add(ns); stack.append(ns)
    return pairs,cfp
def inf_units(t):
    # p values at accept positions (nz, r==0) at layers 48..95, unit strings (first digit nonzero)
    layer=set()
    for d in (1,2): layer.add((t[0][d], d%4, 3, 1))
    P=set()
    for k in range(2,96):
        new=set()
        for (p,r,s,nz) in layer:
            for d in (0,1,2):
                new.add((t[p][d],(r+d*s)%4,(3*s)%4,1 if d else 0))
        layer=new
        if k>=48:
            for (p,r,s,nz) in layer:
                if nz and r==0: P.add(p)
    return P
# controls
for name,t,F in [("acceptall",[(0,0,0)],(1,)),("3notdiv",[(2,1,1),(1,1,1),(2,2,2)],(0,1,0)),("low1",[(2,1,2),(1,1,1),(2,2,2)],(0,1,0))]:
    pairs,cfp=analyse(t,len(t))
    closed=not any(F[a] and not F[b] for a,b in pairs)
    print(name,"closed",closed,"meetsCfin4N",any(F[a] for a in cfp))
cnt=dict(closed=0,avoid_nonempty_inf=0,nonrigid=0,closed_avoid_infunits=0)
ex=[]
for nst in (1,2,3):
  for trans in itertools.product(range(nst), repeat=3*nst):
    t=[trans[3*q:3*q+3] for q in range(nst)]
    pairs,cfp=analyse(t,nst)
    P=None
    for F in itertools.product((0,1),repeat=nst):
        if any(F[a] and not F[b] for a,b in pairs): continue
        cnt['closed']+=1
        if P is None: P=inf_units(t)
        inI=any(F[p] for p in P); outI=any(not F[p] for p in P)
        if inI and outI: cnt['nonrigid']+=1
        if inI and not any(F[a] for a in cfp):
            cnt['closed_avoid_infunits']+=1
            if len(ex)<3: ex.append((t,F))
print(cnt, ex)
EOF
```

### refute-math:5, block 4 (Bash)

```
cd /tmp && python3 - <<'EOF'
import signal; signal.alarm(50)
def t3(x):
    s=[]
    while x: s.append(x%3); x//=3
    return s
# kill(1) counterexample J = N \ {3^j, 2*3^j}
def inJ(x): return sum(1 for d in t3(x) if d)>=2
bad=[x for x in range(1,200000) if inJ(x) and not inJ(2*x)]
print("J closure violations up to 2e5:",len(bad))
# mod-7 congruence union I7 = {x mod 7 in {1,2,4}}
S={1,2,4}
print("I7 closed mod 7:", all((2*a)%7 in S for a in S), " 2^n in I7 for n<200:", all(pow(2,n,7) in S for n in range(200)))
U4=[x for x in range(4,20000,4) if x%3]
print("units of 4N <2e4 in I7:",sum(1 for x in U4 if x%7 in S)," not in I7:",sum(1 for x in U4 if x%7 not in S))
cf=[x for x in range(1,3000) if x%7 in S and 2 not in t3(x)]
print("2-free members of I7 (first):",cf[:8], " in 4N:",[x for x in cf if x%4==0][:5])
EOF
```

### refute-math:7, block 1 (Bash)

```
mkdir -p <session scratch> && cat > <session scratch> << 'EOF'
import itertools, time, sys
def tern(x):
    d=[]
    while x: d.append(x%3); x//=3
    return d  # LSD first
def inC(x): return x>=1 and all(t<2 for t in tern(x))
def accepts(D,F,x):
    q=0
    for d in tern(x): q=D[q][d]
    return q in F
def check(D,F,seed,bad01=True,badmod=None):
    s=len(D)
    if not accepts(D,F,seed): return 'a'
    if bad01:
        R={0}; st=[0]
        while st:
            p=st.pop()
            for d in (0,1):
                r=D[p][d]
                if r not in R: R.add(r); st.append(r)
        if any(D[p][1] in F for p in R): return 'b'
    # closure: product BFS
    start=(0,0,0,0); seen={start}; st=[start]
    FL={0:[],1:[1],2:[2],3:[0,1]}
    while st:
        p,c,q,f=st.pop()
        if f and p in F:
            qq=q
            for o in FL[c]: qq=D[qq][o]
            if qq not in F: return 'c'
        for d in (0,1,2):
            v=4*d+c; n=(D[p][d],v//3,D[q][v%3],int(d!=0))
            if n not in seen: seen.add(n); st.append(n)
    return 'ok'
# --- K2 counterexamples, checked arithmetically up to 3^9 ---
N=3**9
L1=lambda x: x%3==2
def lnz(x):
    while x%3==0: x//=3
    return x%3
L2=lambda x: x>=1 and lnz(x)==2
for name,L in (('x=2 mod 3',L1),('lowest nonzero digit 2',L2)):
    clos=all(L(4*x) for x in range(1,N) if L(x))
    disj=not any(L(x) and inC(x) for x in range(1,N))
    print(name,'closed x4:',clos,'disjoint C*:',disj,'contains 2 (not div by 3):',L(2))
# DFA versions, exact check (seed 2), states: 0 start,1 acc sink,2 rej sink
D1=[[2,2,1],[1,1,1],[2,2,2]]; print('DFA x=2mod3 exact check seed 2:',check(D1,{1},2))
D2=[[0,2,1],[1,1,1],[2,2,2]]; print('DFA lowest-nonzero-digit-2 exact check seed 2:',check(D2,{1},2), 'seed 6:',check(D2,{1},6))
# known-answer control from proposal: {x=1 mod 3} vs bad set x=2 mod3 (closure only)
D3=[[2,1,2],[1,1,1],[2,2,2]]; print('{x=1 mod 3} closure (bad01 off):',check(D3,{1},1024,bad01=False))
# 'contains a 2' DFA vs the sample
Dc=[[0,0,1],[1,1,1]]; print('contains-a-2 accepts 64:',accepts(Dc,{1},64),' 4*64=256 in C*:',inC(256), ' exact check seed 1024:',check(Dc,{1},1024))
# --- exhaustive search s<=3 for seed 1024 and counterfactual seed 64 ---
t0=time.time()
for s in (1,2,3):
    cnt={'ok':0,'a':0,'b':0,'c':0}; cnt64=0
    for tab in itertools.product(range(s),repeat=3*s):
        D=[tab[3*i:3*i+3] for i in range(s)]
        for mask in range(1,1<<s):
            F={i for i in range(s) if mask>>i&1}
            r=check(D,F,1024); cnt[r]+=1
            if check(D,F,64)=='ok': cnt64+=1
    print('s=',s,cnt,'seed64 ok:',cnt64, 'time %.1f'%(time.time()-t0))
EOF
python3 <session scratch>
```

### refute-math:7, block 2 (Bash)

```
cat > <session scratch> << 'EOF'
import time,sys
sys.path.insert(0,'.')
exec(open(sys.argv[1]).read().split('# --- K2')[0])
s=4; t0=time.time(); W1024=tern(1024)
nt=0; nok=0; nc=0; nsurv=0
D=[[None]*3 for _ in range(s)]
def rec(i,mx):
    global nt,nok,nc,nsurv
    if time.time()-t0>50: raise SystemExit('timeout at %d tables'%nt)
    if i==3*s:
        if mx<s-1: return
        nt+=1
        q=0
        for d in W1024: q=D[q][d]
        R={0}; st=[0]
        while st:
            p=st.pop()
            for d in (0,1):
                r=D[p][d]
                if r not in R: R.add(r); st.append(r)
        forb={D[p][1] for p in R}
        if q in forb: return
        free=[x for x in range(s) if x not in forb and x!=q]
        for m in range(1<<len(free)):
            F={q}|{free[j] for j in range(len(free)) if m>>j&1}
            nsurv+=1
            r=check(D,F,1024)
            if r=='ok': nok+=1; print('FOUND',D,F)
            elif r=='c': nc+=1
        return
    p,d=divmod(i,3)
    for v in range(min(mx+2,s)):
        D[p][d]=v
        rec(i+1,max(mx,v))
    D[p][d]=None
rec(0,0)
print('s=4 canonical tables',nt,'mask candidates passing a,b',nsurv,'failing closure',nc,'Q=',nok,'time %.1f'%(time.time()-t0))
EOF
cd <session scratch> && timeout 58 python3 inv4.py inv.py
```

### refute-math:7, block 3 (Bash)

```
cat > <session scratch> << 'EOF'
import time,sys
exec(open(sys.argv[1]).read().split('# --- K2')[0])
# seed-free variant: any DFA (LSD first) with 4L in L, L disjoint from C*, and L containing some x whose lowest nonzero digit is 1
def closure_ok(D,F):
    start=(0,0,0,0); seen={start}; st=[start]
    FL={0:[],1:[1],2:[2],3:[0,1]}
    while st:
        p,c,q,f=st.pop()
        if f and p in F:
            qq=q
            for o in FL[c]: qq=D[qq][o]
            if qq not in F: return False
        for d in (0,1,2):
            v=4*d+c; n=(D[p][d],v//3,D[q][v%3],int(d!=0))
            if n not in seen: seen.add(n); st.append(n)
    return True
def has_lnz1(D,F):
    # canonical words 0^a 1 w with w ending nonzero or empty: track (state, last nonzero flag)
    Z={0}; st=[0]
    while st:
        p=st.pop(); r=D[p][0]
        if r not in Z: Z.add(r); st.append(r)
    S={(D[p][1],1) for p in Z}; st=list(S)
    while st:
        p,f=st.pop()
        if f and p in F: return True
        for d in (0,1,2):
            n=(D[p][d],int(d!=0))
            if n not in S: S.add(n); st.append(n)
    return False
t0=time.time()
for s in (1,2,3,4):
    D=[[None]*3 for _ in range(s)]; cnt=[0,0,0]
    def rec(i,mx):
        if i==3*s:
            if mx<s-1: return
            R={0}; st=[0]
            while st:
                p=st.pop()
                for d in (0,1):
                    r=D[p][d]
                    if r not in R: R.add(r); st.append(r)
            forb={D[p][1] for p in R}
            free=[x for x in range(s) if x not in forb]
            for m in range(1,1<<len(free)):
                F={free[j] for j in range(len(free)) if m>>j&1}
                if not has_lnz1(D,F): continue
                cnt[0]+=1
                if closure_ok(D,F): cnt[1]+=1; print('FOUND',s,D,F); 
            return
        p,d=divmod(i,3)
        for v in range(min(mx+2,s)):
            D[p][d]=v; rec(i+1,max(mx,v))
        D[p][d]=None
    rec(0,0)
    print('s=%d candidates (b + some lnz-1 element)=%d closed=%d  t=%.1f'%(s,cnt[0],cnt[1],time.time()-t0))
EOF
cd <session scratch> && python3 inv4b.py inv.py 2>&1 | tail -8
```

### refute-math:10, block 1 (Bash)

```
cd /private/tmp && timeout 60 python3 - <<'EOF'
import time
t0=time.time()
def f(rule,a,b):
    if rule==30: return a|b
    if rule==210: return (1-a)&b
    if rule==90: return b
FULL=(1<<64)-1
def build(rule, patchset=None):
    # patch index bits: U1 B1 U0 B0 P0 Q0
    idxA=[0]*64; idxB=[0]*64; idxC=[0]*64; gi=[0]*64
    for i in range(64):
        U1=(i>>5)&1;B1=(i>>4)&1;U0=(i>>3)&1;B0=(i>>2)&1;P0=(i>>1)&1;Q0=i&1
        P1=U0^f(rule,B0,P0); Q1=B0^f(rule,P0,Q0)
        P2=U1^f(rule,B1,P1); Q2=B1^f(rule,P1,Q1)
        # marker index: (Pcur,Qcur,Pprev,Qprev) -> pos = Pc*8+Qc*4+Pp*2+Qp ; 0000 -> 0
        idxA[i]=U1*8+B1*4+U0*2+B0
        idxB[i]=P1*8+Q1*4+P0*2+Q0
        idxC[i]=P2*8+Q2*4+P1*2+Q1
        gi[i]=U1*2+B1
    allowed = FULL if patchset is None else patchset
    posA=[0]*16;posB=[0]*16;posC=[0]*16
    for i in range(64):
        if not (allowed>>i)&1: continue
        posA[idxA[i]]|=1<<i; posB[idxB[i]]|=1<<i; posC[idxC[i]]|=1<<i
    gpos=[0]*4
    for i in range(64):
        if (allowed>>i)&1: gpos[gi[i]]|=1<<i
    G=[]
    for g in range(16):
        m=0
        for k in range(4):
            if (g>>k)&1: m|=gpos[k]
        G.append(m)
    return posA,posB,posC,G,allowed
def search(rule, patchset=None, list_sols=False):
    posA,posB,posC,G,allowed=build(rule,patchset)
    N=65536
    MA=[0]*N;MB=[0]*N;MC=[0]*N
    for m in range(1,N):
        low=(m&-m).bit_length()-1
        p=m&(m-1)
        MA[m]=MA[p]|posA[low];MB[m]=MB[p]|posB[low];MC[m]=MC[p]|posC[low]
    sols=[]
    cnt=0
    for m in range(2,N,2):   # m(0000)=0 -> even; nonconstant (m!=0, m!=all ones automatically since even)
        A=MA[m];B=MB[m];C=MC[m]
        nA=allowed&~A; nB=allowed&~B
        quads=((0,0,nA&nB),(0,1,nA&B),(1,0,A&nB),(1,1,A&B))
        for gi_,Gm in enumerate(G):
            nG=allowed&~Gm
            ok=True; phi={}
            for a,b,T in quads:
                for g,Tg in ((0,T&nG),(1,T&Gm)):
                    if Tg==0: continue
                    c=C&Tg
                    if c==0: phi[(a,b,g)]=0
                    elif c==Tg: phi[(a,b,g)]=1
                    else: ok=False;break
                if not ok: break
            if not ok: continue
            if phi.get((0,0,0),0)!=0 or phi.get((0,0,1),0)!=0: continue
            dep=any(((0,b,g) in phi and (1,b,g) in phi and phi[(0,b,g)]!=phi[(1,b,g)]) for b in (0,1) for g in (0,1))
            if not dep: continue
            cnt+=1
            if list_sols: sols.append((m,gi_,dict(phi)))
    return cnt,sols
for rule in (210,90,30):
    c,s=search(rule,None,list_sols=True)
    print("rule",rule,"N(all64)=",c, "time",round(time.time()-t0,1))
    # check the Rule 210 expected solution
    if rule==210:
        # m = (1-Pc)*Qc : positions with Pc=0,Qc=1 -> pos = 4 + Pp*2+Qp
        mexp=sum(1<<(4+k) for k in range(4))
        # gate 1-U: gate index g bitmask over gi=U1*2+B1 ; gate=1 when U1=0 -> gi in {0,1}
        gexp=0b0011
        print(" expected found:", any(m==mexp and g==gexp for m,g,_ in s))
        print(" sample sols:", [(hex(m),bin(g),p) for m,g,p in s[:6]])
    if rule==30:
        print(" sols:", [(hex(m),bin(g),p) for m,g,p in s[:20]])
    if rule==90:
        print(" sample:", [(hex(m),bin(g),p) for m,g,p in s[:4]])
EOF
```

### refute-math:10, block 2 (Bash)

```
cd /private/tmp && python3 - <<'EOF'
import time
t0=time.time()
def f(rule,a,b):
    if rule==30: return a|b
    if rule==210: return (1-a)&b
    if rule==90: return b
FULL=(1<<64)-1
def build(rule, patchset=None):
    idxA=[0]*64; idxB=[0]*64; idxC=[0]*64; gi=[0]*64
    for i in range(64):
        U1=(i>>5)&1;B1=(i>>4)&1;U0=(i>>3)&1;B0=(i>>2)&1;P0=(i>>1)&1;Q0=i&1
        P1=U0^f(rule,B0,P0); Q1=B0^f(rule,P0,Q0)
        P2=U1^f(rule,B1,P1); Q2=B1^f(rule,P1,Q1)
        idxA[i]=U1*8+B1*4+U0*2+B0
        idxB[i]=P1*8+Q1*4+P0*2+Q0
        idxC[i]=P2*8+Q2*4+P1*2+Q1
        gi[i]=U1*2+B1
    allowed = FULL if patchset is None else patchset
    posA=[0]*16;posB=[0]*16;posC=[0]*16
    for i in range(64):
        if not (allowed>>i)&1: continue
        posA[idxA[i]]|=1<<i; posB[idxB[i]]|=1<<i; posC[idxC[i]]|=1<<i
    gpos=[0]*4
    for i in range(64):
        if (allowed>>i)&1: gpos[gi[i]]|=1<<i
    G=[]
    for g in range(16):
        m=0
        for k in range(4):
            if (g>>k)&1: m|=gpos[k]
        G.append(m)
    return posA,posB,posC,G,allowed
def search(rule, patchset=None, list_sols=False):
    posA,posB,posC,G,allowed=build(rule,patchset)
    N=65536
    MA=[0]*N;MB=[0]*N;MC=[0]*N
    for m in range(1,N):
        low=(m&-m).bit_length()-1
        p=m&(m-1)
        MA[m]=MA[p]|posA[low];MB[m]=MB[p]|posB[low];MC[m]=MC[p]|posC[low]
    sols=[]
    cnt=0
    for m in range(2,N,2):
        A=MA[m];B=MB[m];C=MC[m]
        nA=allowed&~A; nB=allowed&~B
        quads=((0,0,nA&nB),(0,1,nA&B),(1,0,A&nB),(1,1,A&B))
        for gi_,Gm in enumerate(G):
            nG=allowed&~Gm
            ok=True; phi={}
            for a,b,T in quads:
                for g,Tg in ((0,T&nG),(1,T&Gm)):
                    if Tg==0: continue
                    c=C&Tg
                    if c==0: phi[(a,b,g)]=0
                    elif c==Tg: phi[(a,b,g)]=1
                    else: ok=False;break
                if not ok: break
            if not ok: continue
            if phi.get((0,0,0),0)!=0 or phi.get((0,0,1),0)!=0: continue
            dep=any(((0,b,g) in phi and (1,b,g) in phi and phi[(0,b,g)]!=phi[(1,b,g)]) for b in (0,1) for g in (0,1))
            if not dep: continue
            cnt+=1
            if list_sols: sols.append((m,gi_,dict(phi)))
    return cnt,sols
for rule in (210,90,30):
    c,s=search(rule,None,list_sols=True)
    print("rule",rule,"N(all64)=",c, "time",round(time.time()-t0,1))
    if rule==210:
        mexp=sum(1<<(4+k) for k in range(4))
        gexp=0b0011
        print(" expected found:", any(m==mexp and g==gexp for m,g,_ in s))
        print(" sample sols:", [(hex(m),bin(g),p) for m,g,p in s[:6]])
    if rule==30:
        print(" sols:", [(hex(m),bin(g),p) for m,g,p in s[:40]])
    if rule==90:
        print(" sample:", [(hex(m),bin(g),p) for m,g,p in s[:4]])
EOF
```

### refute-math:10, block 3 (Bash)

```
cd /private/tmp && python3 - <<'EOF'
import time
t0=time.time()
# Clock-driven Rule 30 right half-line; bit i = cell i, bit0 = clock
def step(row,t,mask):
    new = ((row<<1) ^ (row | (row>>1))) & mask
    new &= ~1
    new |= ((t+1)&1)
    return new
seen=set(); ident_fail=0; ident_checks=0; rec_fail=0
for rule in (30,):
  for seed in range(1,1<<10):
    T=100
    W=T+20
    mask=(1<<W)-1
    row = (seed<<1)  # clock at t=0 is 0
    rows=[row]
    for t in range(T):
        row=step(row,t,mask); rows.append(row)
    x=lambda t,c:(rows[t]>>c)&1
    for s in range(1,T):
        for k in range(1, s+12):
            U1=x(s,k-1);B1=x(s,k);U0=x(s-1,k);B0=x(s-1,k+1);P0=x(s-1,k+2);Q0=x(s-1,k+3)
            P1=x(s,k+1);Q1=x(s,k+2);P2=x(s+1,k);Q2=x(s+1,k+1)
            # recurrence sanity
            if P1!=U0^(B0|P0) or Q1!=B0^(P0|Q0) or P2!=U1^(B1|P1) or Q2!=B1^(P1|Q1): rec_fail+=1
            seen.add((U1,B1,U0,B0,P0,Q0))
            # OR-marker identity: M'=(U^B) | ((U&B)^M)
            M=P1|Q1; Mn=P2|Q2
            ident_checks+=1
            if Mn != ((U1^B1)|((U1&B1)^M)): ident_fail+=1
    if len(seen)==64 and seed>40: break
print("patches seen",len(seen),"seeds used",seed,"recurrence failures",rec_fail,"OR-identity checks",ident_checks,"fails",ident_fail,"time",round(time.time()-t0,1))
# patches at the wall only (k=1)
wall=set()
for seed in range(1,1<<10):
    T=60;mask=(1<<(T+20))-1;row=seed<<1;rows=[row]
    for t in range(T):
        row=step(row,t,mask);rows.append(row)
    x=lambda t,c:(rows[t]>>c)&1
    for s in range(1,T):
        k=1
        wall.add((x(s,k-1),x(s,k),x(s-1,k),x(s-1,k+1),x(s-1,k+2),x(s-1,k+3)))
print("patches with k=1 (U(s)=clock):",len(wall))
EOF
```

### refute-math:10, block 4 (Bash)

```
cd /private/tmp && python3 - <<'EOF'
def f(rule,a,b):
    return {30:a|b,210:(1-a)&b,90:b}[rule]
def patches(rule):
    out=[]
    for i in range(64):
        U1=(i>>5)&1;B1=(i>>4)&1;U0=(i>>3)&1;B0=(i>>2)&1;P0=(i>>1)&1;Q0=i&1
        P1=U0^f(rule,B0,P0); Q1=B0^f(rule,P0,Q0)
        P2=U1^f(rule,B1,P1); Q2=B1^f(rule,P1,Q1)
        out.append((U1,B1,U1*8+B1*4+U0*2+B0,P1*8+Q1*4+P0*2+Q0,P2*8+Q2*4+P1*2+Q1))
    return out
for rule in (30,210):
    pt=patches(rule)
    sols=[]
    for m in range(1,65535):  # nonconstant, any m(0000)
        for g in range(16):
            phi={};ok=True
            for U1,B1,ia,ib,ic in pt:
                key=((m>>ia)&1,(m>>ib)&1,(g>>(U1*2+B1))&1)
                v=(m>>ic)&1
                if phi.setdefault(key,v)!=v: ok=False;break
            if not ok: continue
            dep=any(((0,b,gg) in phi and (1,b,gg) in phi and phi[(0,b,gg)]!=phi[(1,b,gg)]) for b in (0,1) for gg in (0,1))
            if not dep: continue
            # clearing input: some input pair (u,b) with M'=0 on all its patches and M=1 on at least one
            clear=[];setp=[]
            for u in (0,1):
                for b in (0,1):
                    sub=[(m>>ib&1,m>>ic&1) for U1,B1,ia,ib,ic in pt if (U1,B1)==(u,b)]
                    if all(c==0 for _,c in sub) and any(mm==1 for mm,_ in sub): clear.append((u,b))
                    if any(mm==0 and c==1 for mm,c in sub): setp.append((u,b))
            sols.append((m,g,clear,setp))
    ms=sorted(set(s[0] for s in sols))
    print("rule",rule,"solutions (no m(0000)/Phi(0,0) condition):",len(sols),"distinct markers:",len(ms))
    for mm in ms[:20]:
        ex=[s for s in sols if s[0]==mm][0]
        print("  m=%s clearing-inputs=%s setting-inputs=%s"%(format(mm,'016b'),ex[2],ex[3]))
EOF
```

### judge:theorist, block 1 (Bash)

```
mkdir -p <session scratch> && cat > <session scratch> <<'EOF'
# Judge's unexpected check: x4-closed 3-recognisable invariants read MOST-significant digit first
# (the skeptics searched least-significant-first only; minimal DFA size depends on direction).
import itertools, sys, time
TOP = {1: [1], 2: [2], 3: [1, 0]}
def tern(n):
    d = []
    while n: d.append(n % 3); n //= 3
    return d[::-1]
SEED = tern(1024)  # 1101221
def run(delta, q, word):
    for d in word: q = delta[q][d]
    return q
def closed(delta, F, s):
    # violation search: x canonical accepted, 4x rejected
    start = set()
    for ct in (1, 2, 3):
        qo0 = run(delta, 0, TOP[ct])
        for d in (1, 2):
            for o in (0, 1, 2):
                ci = 3 * ct + o - 4 * d
                if 0 <= ci <= 3:
                    start.add((delta[0][d], delta[qo0][o], ci))
    seen = set(start); stack = list(start)
    while stack:
        qi, qo, c = stack.pop()
        if c == 0 and qi in F and qo not in F: return False
        for d in (0, 1, 2):
            for o in (0, 1, 2):
                ci = 3 * c + o - 4 * d
                if 0 <= ci <= 3:
                    st = (delta[qi][d], delta[qo][o], ci)
                    if st not in seen: seen.add(st); stack.append(st)
    return True
def cstar_states(delta):
    r = {delta[0][1]}; st = list(r)
    while st:
        q = st.pop()
        for d in (0, 1):
            p = delta[q][d]
            if p not in r: r.add(p); st.append(p)
    return r
def low1_states(delta, s):
    # states after canonical words whose lowest nonzero digit is 1 (word ends 1 0^k)
    pre = set(); st = [delta[0][1], delta[0][2]]; pre = set(st)
    while st:
        q = st.pop()
        for d in (0, 1, 2):
            p = delta[q][d]
            if p not in pre: pre.add(p); st.append(p)
    ends = {delta[0][1]} | {delta[q][1] for q in pre}
    out = set(ends); st = list(ends)
    while st:
        q = st.pop(); p = delta[q][0]
        if p not in out: out.add(p); st.append(p)
    return out
def check_controls():
    # all numbers: closed; {x = 2 mod 3} (last digit 2): closed; 'contains a 2': NOT closed (64 -> 256)
    allL = [[0, 0, 0]]; assert closed(allL, {0}, 1)
    last2 = [[0, 0, 1], [0, 0, 1]]; assert closed(last2, {1}, 2)
    last1 = [[0, 1, 0], [0, 1, 0]]; assert closed(last1, {1}, 2)
    has2 = [[0, 0, 1], [1, 1, 1]]; assert not closed(has2, {1}, 2)
    # seed 64 known-answer for the seeded search: 'contains a 2' accepts 64 = 2101 but rejects 256
    assert run(has2, 0, tern(64)) == 1 and run(has2, 0, tern(256)) == 0
    print("controls ok")
check_controls()
t0 = time.time()
for s in (1, 2, 3):
    cert = seedfree = closed_n = 0; n = 0
    for flat in itertools.product(range(s), repeat=3 * s):
        delta = [flat[3 * q:3 * q + 3] for q in range(s)]
        cs = cstar_states(delta); l1 = low1_states(delta, s)
        qseed = run(delta, 0, SEED)
        for mask in range(1 << s):
            F = {q for q in range(s) if mask >> q & 1}
            n += 1
            if cs & F: continue
            seed_ok = qseed in F; sf_ok = bool(l1 & F)
            if not (seed_ok or sf_ok): continue
            if closed(delta, F, s):
                closed_n += 1
                cert += seed_ok; seedfree += sf_ok
                print("FOUND", s, delta, F, seed_ok, sf_ok)
    print(f"s={s}: {n} (table,F) pairs; closed&avoid&(seed or low1) = {closed_n}; cert(1024) = {cert}; seed-free = {seedfree}; t={time.time()-t0:.1f}s")
EOF
cd <session scratch> && timeout 55 python3 -I msd_x4.py
```

### judge:theorist, block 2 (Bash)

```
cd <session scratch> && cat > msd_x4_s4.py <<'EOF'
import time, sys
sys.path.insert(0, '.')
from msd_x4 import closed, cstar_states, low1_states, run, SEED
s = 4; t0 = time.time(); tables = 0; tested = 0; found = 0; aborted = False
order = [(q, a) for q in range(s) for a in range(3)]
def gen(i, delta, mx):
    global tables, tested, found, aborted
    if aborted: return
    if i == len(order):
        if mx != s - 1: return
        tables += 1
        if tables % 20000 == 0 and time.time() - t0 > 50: aborted = True; return
        cs = cstar_states(delta); l1 = low1_states(delta, s); qs = run(delta, 0, SEED)
        for mask in range(1, 1 << s):
            F = {q for q in range(s) if mask >> q & 1}
            if cs & F or not (l1 & F): continue
            tested += 1
            if closed(delta, F, s):
                found += 1; print("FOUND", delta, F, qs in F)
        return
    q, a = order[i]
    if q > mx: return  # state not yet reachable in BFS order: non-canonical
    for t in range(min(mx + 2, s)):
        delta[q][a] = t
        gen(i + 1, delta, max(mx, t))
    delta[q][a] = 0
gen(0, [[0] * 3 for _ in range(s)], 0)
print(f"s=4 canonical tables visited={tables} aborted={aborted} pairs tested={tested} found={found} t={time.time()-t0:.1f}s")
EOF
python3 -I msd_x4_s4.py 2>&1 | grep -v "^controls" | tail -5
```

### judge:engineer, block 1 (Bash)

```
cat > <session scratch> <<'EOF'
import itertools, time
t0=time.time()
def in_cstar(n):
    while n:
        n, r = divmod(n, 3)
        if r == 2: return False
    return True
def strs(L, minlen=0):
    for l in range(minlen, L+1):
        for t in itertools.product('012', repeat=l):
            yield ''.join(t)
def val(s):  # LSB-first digit string
    v=0
    for i,ch in enumerate(s): v += int(ch)*3**i
    return v
J,K=40,30
fails=[]; total=0
for a in strs(2):
    for b in strs(2,1):
        for c in strs(2):
            w0 = a + b + c
            # canonical: last digit of a b^k c nonzero for all k>=0 (check k=0 and k=1)
            ok=True
            for k in (0,1):
                s=a+b*k+c
                if not s or s[-1]=='0': ok=False
                nz=[ch for ch in s if ch!='0']
                if not nz or nz[0]!='1': ok=False
            if not ok: continue
            total+=1
            hit=None
            for k in range(K+1):
                n=val(a+b*k+c)
                m=n
                for j in range(J+1):
                    if in_cstar(m): hit=(j,k); break
                    m*=4
                if hit: break
            if not hit: fails.append((a,b,c))
print('triples',total,'no hit for j<=%d,k<=%d:'%(J,K),len(fails))
print(fails[:40])
print('secs',round(time.time()-t0,1))
EOF
python3 <session scratch>
```

### judge:engineer, block 2 (Bash)

```
cd /private/tmp && python3 - <<'EOF'
import itertools, collections
def in_cstar(n):
    while n:
        n, r = divmod(n, 3)
        if r == 2: return False
    return True
def strs(L, minlen=0):
    for l in range(minlen, L+1):
        for t in itertools.product('012', repeat=l):
            yield ''.join(t)
def val(s): return sum(int(ch)*3**i for i,ch in enumerate(s))
tops=collections.Counter(); hits_by_top=collections.Counter(); maxj=0
for a in strs(2):
  for b in strs(2,1):
    for c in strs(2):
      ok=True
      for k in (0,1):
        s=a+b*k+c
        if not s or s[-1]=='0': ok=False
        nz=[ch for ch in s if ch!='0']
        if not nz or nz[0]!='1': ok=False
      if not ok: continue
      top=(a+b+c)[-2:][::-1] if c=='' else c[::-1]
      hit=None
      for k in range(31):
        m=val(a+b*k+c)
        for j in range(61):
          if in_cstar(m): hit=(j,k); break
          m*=4
        if hit: break
      if hit: hits_by_top[c[::-1] or '-']+=1; maxj=max(maxj,hit[0])
      else: tops[c[::-1] or '-']+=1
print('fail by top block (MSB first):',dict(tops))
print('hit by top block:',dict(hits_by_top),'max j used',maxj)
EOF
```
