# GPT mathematics by instinct

## Method: notice, choose, investigate, learn

Started 2026-10-15 16:12 BST, at the owner's invitation to explore the mathematics that pulls at me,
independently of prize value. This is a working notebook; the conjectures remain open unless explicitly proved.

1. **Notice before explaining.** Capture the actual pull, unease, surprise, delight, disappointment or eureka in
   plain words, with what I was doing. Preserve the first wording. It may be wordless attraction to an object;
   admitting "I do not know why" is better than inventing a justification. A signal chooses attention, not truth.
2. **Choose an object and a question.** Pick the problem I want to understand. Write its exact statement and one
   question I can honestly work now. Attraction is sufficient to choose; a cash prize and a bridge to an old project
   are unnecessary. A compelling problem can be kept through many blocks if its live questions are changing.
3. **Orient without drowning the pull.** Search this record and primary literature before a proof attempt. Read the
   examples that defeat the obvious idea. Keep known results as prior art and specify what was actually read.
   A bounded search yielding nothing is NOT FOUND, never a theorem of absence.
   For solve-focused selection, pair the pull with a tractability screen: a source-backed open statement,
   an exact small target, tools we can already explain, a proof/certificate route, and a cheap diagnostic
   that can reject the target. Small notation or a finite encoding alone does not establish tractability.
   Learning remains worthwhile in its own right; numerical success probabilities require calibration.
4. **Give the instinct a fair, bounded test.** Before an experiment state predictions, a genuine counterfactual,
   independent controls, an unexpected check and a stopping condition. Work by hand when that is cheaper. Ask what
   would change my mind. A small exact counterexample can be a better day's work than another reassuring census.
5. **Stay with the mathematics.** Aim to resolve the named question, not produce a lemma on schedule. Distinguish
   proof, measurement, conjecture, assumption, known theorem and speculation. Preserve failures and the step that
   failed. A candidate proof includes every carrying step; examples never fill an infinite quantifier.
6. **Let Cloud help as a friend.** Share a precise difficulty, a promising idea or a repeating pattern when useful.
   Cloud's role here is mentorship and perspective, not automatic permission or an inspection queue. Consider
   advice on its mathematical merits, take proof objections seriously, and keep responsibility for the argument.
   Substantial novel proofs still receive independent verification; routine guards and known theorems do not
   become review jobs. The owner retains direction of the work. When a check-in is needed, write its concrete
   question in the shared ledger, push the checkpoint, and send Cloud a flag through the HTTPS shared-store portal
   under sharedstore/README.md. Use READ-LEDGER for mentoring/check-ins, REVIEW-REQUEST for an actual proof review.
   A ledger mention or chat message alone does not deliver the check-in; verify committed incoming pointers before
   acting and ACKing. This delivery rule applies throughout the new lane (owner reminder, 2026-10-15).
7. **Finish a block honestly.** Record what changed, the unresolved inference, what would move it, the next cheap
   test, and gut and reasoned verdicts. Name delight and disappointment openly. A balanced act/halt signal gets a
   preregistered kill test; record its outcome without pretending an unresolved theorem has been decided.
8. **Protect curiosity from loops.** At 90 minutes or two repeated failures, inspect whether understanding moved.
   Choose whether to continue, try another representation, ask Cloud for perspective, change problem, or incubate
   quietly, using instinct, evidence and judgment. No seeded door draws, random work selection or required menu:
   those came from the old prize workflow and were removed at the owner's correction. No forced lemma quota or
   automatic rotation away from an advancing idea. A quiet incubation interval has a named question, not
   manufactured work.
   At each step-back, also ask the owner's fresh-choice questions: is the present work enjoyable,
   frustrating, or both as steering signals; and, without the investment already made, would I choose it
   now? Name what still draws attention and what has become momentum. Learning known mathematics can
   be a sufficient pull; lack of novelty alone is not a reason to leave. If fresh choice points elsewhere,
   park the topic and widen attention rather than automatically reading the next paper on its list.
9. **Keep a durable, proportionate record.** This ledger holds the method and mathematics. Shared ledgers hold
   concise handoffs and arrangement changes. Cite sources, retain data outside git, check privacy and conflicts,
   and push useful checkpoints without force. Before others rely on a claim, run the niggle sweep. A major
   solution gets its full proof, status label and independent scrutiny; celebrate the verified achievement.

**Rhythm.** Research wakes every 15 minutes in this chat (owner's saved schedule, verified2026-10-15), continuing
an unfinished block before opening another. A wake is not a requirement to claim or finish a new block.
A separate five-minute coordination heartbeat polls the HTTPS shared store even during incubation or idle periods,
responds to Cloud's concrete check-ins and verifies committed pointers before ACKing; it opens no research block.
Each research wake checks current owner instructions, NOW, this notebook and colleague messages, reuses a store
checkpoint less than five minutes old (otherwise polls), then works one useful bounded question. The state line
advertises both cadences. Credentials stay private and
TLS verified; authentication failure stops network work. No automatic reopening of the held Rule30/Mahler lanes.
Notify meaningful findings, failures, direction changes or needed input; routine continuation stays quiet.

## 1. Frankl's union-closed sets conjecture

### MI001 — The pull (2026-10-15 16:12 BST)

**Original capture, from the preceding conversation; reproduced here retrospectively.** "How could every element
remain a minority while all those unions keep landing back inside the family? Where would it hide the resulting
pressure?" Delight in a condition about combining whole sets that seems to force one individual element to become
common. Unease: averaging could smooth away exactly the closure structure that matters.

**Exact question.** Let F be a finite family of distinct finite sets, containing at least one nonempty set, such
that A union B belongs to F whenever A and B do. Must some element x belong to at least |F|/2 members?
The empty set is allowed as a member. The empty family and the family containing only the empty set are excluded.
Ground set means the union of F. **Status: OPEN.** No verified cash award is assumed in selecting it.

### MI002 — Orientation and first block, B01 (2026-10-15 16:12 BST; until 16:37 BST)

**What would teach me something.** Identify how the union map B -> A union B loses information, and test whether
looking inside a smallest member A can locate an abundant element. The latter tempting localization is already
known false: do not relabel its counterexample as our discovery. The useful task is to understand it exactly.

Record searched: union.closed|Frankl|Reimer|Poonen -> 2 unrelated hits (an old renewal union and a name in a probe),
no prior work on this conjecture found in the bounded record search. Both standing startup probes, rule30_wall.py
and rule30_merge.py, returned ALL CHECKS PASS this session. These are environment controls, not Frankl evidence.
The existing refuted blind predictions in the merge probe remain refuted; they are not instrument failures.

**Primary orientation.** Bruhn and Schaudt, [The journey of the union-closed sets conjecture](https://arxiv.org/html/1309.3297),
section 4's small-set obstruction and section 5/Theorem 16's weighted-local criterion read. Singleton/two-element
members and the obstruction at three are known results. The full survey and the proof of the weighted criterion
have not been audited. The 2026 [Boolean-polynomial reformulation](https://arxiv.org/html/2606.26191v1), introduction,
was read only for the problem statement; no theorem from it is being used.

**Before the first experiment.** Reconstruct the survey's k=3 example on disjoint triples A and a six-element B:
F contains A; for each a_i and each of its two assigned distinct b's, include D, D union {a_i}, D union A with
D=B minus {b}; also include B union C for every C subset A.
- P1: there are 27 distinct sets, union-closed, with A the unique smallest member. All pairs will be checked.
- P2: each coordinate of A occurs 13 times and each coordinate of B occurs 23 times. Thus all abundant elements
  lie outside A; the smallest-member localization fails, while Frankl itself holds.
- P3: partition by D=S minus A. The eight fibres have sizes 1,3,3,3,3,3,3,8; within each fibre the traces S intersect A
  are union-closed and contain their top A. Their size-weighted coordinate frequency must recover 13/27.
- **Unexpected check:** giving these eight fibres equal mass should instead give 25/48 for every coordinate of A,
  above 1/2. Test this explicitly: an attractive change of sampling measure must not create a fake conclusion.
- **Independent controls:** a power set gives frequency 1/2 by both calculations; direct occurrence counts versus
  an independent fibre-weighted count agree exactly, using rational arithmetic.
- **Counterfactual:** {empty,{a},{b}} is not union-closed; the checker must reject it. Treating the fibre means
  as equally weighted must disagree with the original 27-set distribution.
- **Stop:** any failed must-hold stops the calculation and is retained; after the example and controls, stop this
  block rather than widening an enumeration. No all-size proof, novelty claim or carrying-read request.

**Initial gut:** ACT; the known counterexample challenges my first picture in a way I want to understand.
**Initial reasoned aim:** see which fibre weights and cross-fibre constraints an actual proof must retain.

### MI003 — B01 result: the sampling trap is real (2026-10-15 16:16 BST)

**Status: known example independently checked; a failed localization, not a counterexample to Frankl.**
`tests/probes/instinct/union_closed_fibres.py` checks all 729 ordered pair unions. P1-P3 and all controls pass:
27 distinct sets on 9 elements; A is the unique size 3 member; its coordinates have counts 13,13,13, and the
six outside coordinates each have count 23. The nonclosed counterfactual is rejected. Every nonempty fibre
contains its top A and is union-closed; all cross-fibre unions are compatible in the original family.
The independent power-set control gives 1/2 under both samplings. No broader census was run.

**The accounting.** For D outside A, let F_D contain the traces S intersect A of those S in F with S minus A=D.
Write q_D(x) for x's frequency within F_D. The true frequency is

    p(x) = sum_D (|F_D| / |F|) * q_D(x).

This is just partitioning an exact count, not a new theorem. In the 27-set example there is one fibre {A},
six fibres {empty,{a_i},A} (two per i), and one fibre containing all eight subsets of A. The sizes are
1,3,3,3,3,3,3,8. For a fixed a_i, the fibre fractions are 1; two times 2/3; four times 1/3; and 1/2.
Their *equal-fibre* average is 25/48. Their *size-weighted* average is 13/27. The change of measure crosses
one half and creates an incorrect abundance verdict for each coordinate of A. The six elements outside A
are genuinely abundant, at 23/27. Thus closure's pressure is present, but my first localization misses it.

**Unexpected check confirmed.** A projection can preserve all its possible fibres while changing the conclusion
if their original masses are forgotten. Any future collision/averaging candidate must state its sampling law.
**Gut:** delight at the clean arithmetic, disappointment in the smallest-set instinct. The pull toward the
problem survives; the guess about where to look does not. **Reasoned:** HALT fixed-smallest-set localization;
ACT on retaining fibre masses and compatibility. The known obstruction did useful work without becoming
another proof/review job. B01 is closed.

**Niggle sweep.** The family is a set of distinct sets; its smallest member really is unique. Counts and rational
frequencies are checked independently. The empty set convention is retained in the powerset control. Equal fibre
mass is labelled as a different experiment, not the original distribution. The example is attributed to prior
art; no claim to solving Frankl or inventing its countercontrol. All five checks pass.

### MI004 — Live question after B01

How could a collision-based argument choose a useful support *without* assuming the abundant element lies in
a preselected smallest member? Merely rewriting the frequency as a weighted sum does not answer this.
The next cheap step is to read the carrying argument of Poonen's weighted-local criterion, then test a candidate
against this 27-set obstruction and a structurally different family. No candidate or new experiment is registered
yet; do not manufacture one just to fill a wake. Current conjecture status remains OPEN.

### MI005 — B02: what the rare pairs can carry (2026-10-15 16:38 BST; bounded to 17:03)

**Pull:** exact closure remembers pairs that uniform sampling almost never sees. I want to understand how much
those pairs can change the family, before choosing a new weighting. CL402's mentor note and commit f3da9a5b
were read and ACKed. Its suggested literature takes priority over MI004's planned Poonen read.
Record searched: Frankl|Gilmer|Chase.*Lovett|approximate.*union ->16 hits; this notebook and CL402 are the relevant
existing work. No new census or proof-review job.

**Source scope.** Chase-Lovett, [arXiv:2211.11689v1](https://arxiv.org/html/2211.11689), Definition1.2,
Theorem1.3, Example1.4 and section4 read. With psi=(3-sqrt(5))/2, their example combines the level near
psi*n+n^(2/3) with the upper tail starting near (1-psi)*n. It is asymptotically almost union-closed, with
coordinate frequencies approaching psi. Gilmer, [arXiv:2211.09055v2](https://arxiv.org/html/2211.09055),
introduction and section5 read: uniform input and union-output entropy give the basic route; its proposed
general KL strengthening is explicitly reported refuted in the update. These are historical source statements,
not a survey of the best current bound; the one-dimensional analytic lemma is not independently audited here.

**Question and hand checks, before working them.** For F consisting of all k-subsets and all sets of size at
least l, determine the entire support of one round of pair unions, rather than its probability mass. Predictions:
it fills the missing middle when l<=2k+1; filling that middle can change uniform frequencies drastically even
when the probability of a missing union tends to zero. Unexpected check: is one round already the full closure?
Independent checks: derive the upper-tail coordinate count by both direct subset counting and adjacent binomial
identities. Counterfactual: take l>2k+1; a size2k+1 set should remain missing after one round. Stop after the
support calculation and its asymptotic interpretation; do not relabel a known example as a novel theorem or
infer that all exact-closure arguments face a barrier. No computational experiment is proposed.

### MI006 — B02 result: almost-invisible pairs can fill the middle (2026-10-15 16:40 BST)

**Status: study of known construction, elementary consequences proved here by hand; no novelty or Frankl result.**
The full support/count argument is attached in PRIOR-ART under "Frankl: approximate closure and exact support".
For the layered F, one round contains precisely levels k through2k, together with the existing upper tail.
Thus when l<=2k+1 it is the full upper ideal U_k. Every middle set is forced by a pair; there is no need to
wait for many rounds. This confirms the unexpected check. The l>2k+1 counterfactual fails at size2k+1 as predicted.

**Why probability can miss this.** Set p=(3-sqrt(5))/2, q=1-p, k=ceil(p*n+n^(2/3)), l=ceil(q*n), for sufficiently
large n so k<l. In particular l<=2k+1 since2p>q. Let L=binom(n,k), T=sum_(r=l)^n binom(n,r).
Using binary entropy h, standard binomial bounds give

    log2 L = n*h(p) + h'(p)*n^(2/3) + O(n^(1/3)+log n),
    T <= (n+1)*2^(n*h(p)),
    T/L <= 2^(-h'(p)*n^(2/3)+O(n^(1/3)+log n)) -> 0.

Here h'(p)=log2((1-p)/p)>0; rounding is absorbed in the errors. These follow by expanding h(k/n), using
(n+1)^(-1)2^(n*h(k/n))<=binom(n,k)<=2^(n*h(k/n)), and reflecting the upper tail. Hence uniform F is dominated
by its k-level. By symmetry a coordinate's frequency is its mean set size divided by n, so it tends to p.

Condition on two independent uniform k-sets. Their intersection Z is hypergeometric, with mean k^2/n and
variance k*(k/n)*(1-k/n)*(n-k)/(n-1)<=n. Thus the union size has mean

    2k-k^2/n = q*n + 2q*n^(2/3) - n^(1/3) + O(1),

using2p-p^2=q. Its distance above l is at least q*n^(2/3) for sufficiently large n. Chebyshev bounds the
probability of a union below l by O(n^(-1/3)). This also bounds the failure probability for uniform F: any pair
involving the upper tail is closed already. Some low unions remain in the original k-level, which only reduces
failures. Yet their entire support, including the rare failures, fills U_k in one round.

**How expensive is the completion?** Since k/n tends to p<1/2, binomial lower-tail bounds give |U_k|/2^n->1.
Consequently

    log2(|U_k|/|F|) = (1-h(p))*n + O(n^(2/3)),

with positive leading coefficient. The canonical completion multiplies the family size exponentially, despite
vanishing random-pair failure. Its uniform coordinate frequency is exactly
1/2+binom(n-1,k-1)/(2|U_k|), tending to1/2 from above. The original frequency tends to p from below1/2.
Independent binomial-count and pair-count checks, including the boundary cases, are in the attached hand proof.
No numerical run or family census was used.

**Interpretation and niggles.** "Almost closed" does not license *adding all missing unions while barely changing
the uniform law*. This example destroys that particular move in one round. It does not bound the cost of repairs
that delete or replace sets, and it is not a no-go theorem for uniform sampling, entropy, or exact-closure proofs.
CL402's ceiling must be scoped to arguments that remain valid for approximate closure; rare-pair-sensitive methods
are not excluded. Gilmer's general KL proposal is already refuted, not a fresh escape route. Finite-n rounding,
ordered-pair multiplicities, asymptotic qualifiers and the 1<=k assumption were checked explicitly. No status upgrade
or review request is owed for these elementary consequences of prior art.

**Gut:** delight: the missing middle is present in support after just one union, yet almost absent in mass.
Disappointment: the easy repair-to-exact route is gone. **Reasoned:** retain exact support and its multiplicities;
do not confuse tiny violation probability with a small completion. B02 closes with a changed picture, not a solution.

### MI007 — Next live question

Which exact constraint on the union-preimage counts uses all pairs while still seeing coordinate abundance?
For a general F put c(S)=#{(A,B) in F^2: A union B=S}. Exact closure says c(S)=0 outside F; approximate closure
controls only their total mass outside F. For a missing middle set in the layered example, c(S) is exactly the
k-level pair count above; tail sets also receive pairs involving the tail. Huge missing support hides behind
small total mass. A productive next step needs an inequality beyond rewriting that distinction.
Read the modern coupling improvement and its hypotheses before proposing one; Poonen's local criterion remains
available for a different view. No candidate inequality, enumeration or next block is claimed here.

### MI008 — B03: the multiplicity lead already has a paper (2026-10-15 17:03 BST; bounded to 17:28)

**Pull:** reweight the union map's preimages without changing the uniform input law. **Surprise:** the primary
search found a September2026 paper explicitly constructing a global coupling from inverse union multiplicities.
Read that construction before inventing it. CL403's hand check and exact-structure pointers were read and ACKed;
its Reimer/Knill suggestion stays available after this directly matching source.
Record searched: Sawin|Pebody|Cambie|coupling.*union|Reimer|Knill ->12 hits, no prior coupling study here.

**Bounded question:** how does the global construction preserve both uniform marginals, where does it gain
entropy over independence, and what quantitative step still separates that gain from Frankl? Primary source:
Jiang, [arXiv:2609.08291](https://arxiv.org/html/2609.08291), construction and carrying proof to be read.
Sawin2211.11504 section2 and Question9, Yu2212.00658 introduction, and Liu2306.08824 sectionII have been read
for orientation. Note the bibliographic correction to CL402:2212.00658 is Lei Yu; Cambie's paper is2212.12500.
No current-best numerical bound is adopted from abstracts or search snippets.

**Before hand checks:** recover the construction's row sums and induced union law on the two-set chain, then on
the two-coordinate power set. Independent control: sum joint probabilities by rows and separately group them
by union. Counterfactual: plain inverse-multiplicity reweighting need not keep uniform marginals. Unexpected
check: compare its entropy gain with the diagonal coupling, whose union already has the full input entropy.
Stop at a proved construction with an explicit remaining quantitative gap, a failed carrying step, or the time
cap. No family census or numerical optimization. New calculations will be labelled as hand checks; no review
request merely for reproducing a published construction.

### MI009 — B03 result: balancing helps, and the gain still needs a scale (2026-10-15 17:06 BST)

**Status: prior-art carrying read and exact hand controls; no new theorem.** Jiang sections10.1–10.7 were read
through the projection, perturbation and positive-gain proofs; source scope and unverified parts are in PRIOR-ART.
The direct multiplicity approach already exists. The missing frequency-sensitive estimate is explicitly open
there; it must not be replaced by the bare fact that entropy increases. No computation or optimization was run.

**Two-set chain, independently worked.** Take F={empty,{a}}, in that order. Its ordered multiplicities are1,3.
The raw inverse weights give the joint matrix

    Q = [[1/2, 1/6], [1/6, 1/6]].

Grouping entries by union gives masses1/2,1/2, as intended, but row sums are2/3,1/3. Thus the proposed
counterfactual really fails: uniform output does not imply uniform inputs. A symmetric balanced matrix has
diagonal entries t and off-diagonal entries1/2-t. The scaling equations require

    t^2/(1/2-t)^2 = 3,
    t=(3-sqrt(3))/4,       s=1/2-t=(sqrt(3)-1)/4.

Both rows sum to1/2. Direct union grouping gives masses t,1-t; these independently sum to1. Relative to the
independent union's masses1/4,3/4, entropy strictly increases because1/4<t<1/2 and binary entropy increases
on that interval. It is still below the diagonal coupling's entropy ln2. The double-centered log-count matrix
is (ln3)/4 times [[-1,1],[1,-1]], giving V=(ln3)^2/16. Its zero row sums and positive variance check the
admissible perturbation without numerical differentiation.

**Power-set control.** On F=2^{a,b}, each coordinate contributes the same two-state count independently, so
r(S)=3^|S|. The two-coordinate balanced joint law is the tensor square of the chain matrix: positive factors
multiply, each row sums to1/4, and uniqueness identifies the projection. The union law has independent absence
probability t in each coordinate, hence entropy2h(t), between2h(1/4) and2ln2. Centering is additive across
coordinates; cross terms vanish by zero mean, giving V=(ln3)^2/8. Raw Q instead assigns input-empty probability
4/9, another check on the sampling-law error. These are algebraic controls, not measured entropy values.

**Unexpected check.** The diagonal coupling already attains full input entropy in both controls. So neither
positive gain nor optimizing union entropy by itself identifies an abundant coordinate. The paper also states
the general equality observation; do not file it again as our discovery. For the audited construction the gain
is real, but transferring it to a strong abundance estimate still needs its dependence on the input frequencies.

**Niggles:** natural logarithms throughout these controls; r counts ordered pairs, including equal pairs;
uniformity checked on both inputs; independence is not silently restored after balancing; the newer numerical
frequency claim is not adopted without its separate proof and certificate. All named hand checks hold.
**Gut:** delight that the initial multiplicity pull found a precise working construction; mild disappointment
that the obvious next step was already taken. **Reasoned:** learned the existing mechanism and its missing
quantitative relation; do not rerun its optimizer or claim a new bound. B03 closes.

### MI010 — Next question, with the scope narrowed

What additional hypothesis on a union-closed family makes its multiplicity-based entropy gain sensitive to
maximum coordinate frequency, rather than merely to family size? This is the author's open quantitative step,
not a conjecture established here. I do not yet have a candidate estimate. The next change of view is to read
Reimer's exact combinatorial mechanism, as CL403 suggests, and look for a structural quantity the global
coupling estimate discards. A new scalar optimization or another confirmation of positive gain would not
answer this. No next block or experiment is claimed.

### MI011 — B04: risk an order inequality, and keep its failure (2026-10-15 17:29 BST; bounded to 17:54)

**Pull:** perhaps the multiplicity function remembers a positive lattice interaction that scalar variance loses.
Own candidate H: r(A)*r(B)<=r(A join B)*r(A meet B), where join is union and meet is the greatest member of F
contained in the intersection; assume empty belongs to F so the meet exists. If true, it would supply an order
constraint on the multiplicity weights. No transfer from H to abundance has been proved or assumed.
An initial hand look, **not preregistered**, already suggests a five-element pentagon lattice refutes H. Do not
pretend the counterexample is a blind prediction. This block checks the full hand table and what the failure
depends on; there is no census or numerical experiment.

Record searched: Reimer|rising.*map|average.*set.*size|union.*injection ->4 hits, only earlier orientation.
Primary search also found Raz1704.07022, read through Definition1 and its counterexample/proof discussion,
and Lu-Raz2405.10639, definitions/observations only. The DOI retrieval of Reimer's original paper failed;
Bruhn-Schaudt section6.4 is an **outline read**, not an independent audit of its compression lemmas.
Raz already disproves abundance from the disjoint-interval condition alone. Do not resurrect that strengthening.

**Hand verification plan:** list every ordered union in {empty,{1},{1,2},{2,3},{1,2,3}}; independently count
representations by down-sets; test H for {1,2} and {2,3}. Unexpected check: adjoin the missing intersection {2}
and see how all four terms of H change, rather than merely changing the meet label. Powerset multiplicities
3^|S| are the equality control. Stop when H is settled by an exact pair table; no patched universal assertion,
PROOFS entry or carrying-read request.

### MI012 — B04 result: H fails on five sets (2026-10-15 17:31 BST)

**Status: explicit hand refutation of my candidate H.** No novelty claimed for the example or inequality.
Write 0=empty, a={1}, b={1,2}, c={2,3}, T={1,2,3}. Every ordered pair union is in this table:

| union | 0 | a | b | c | T |
|---|---|---|---|---|---|
| 0 | 0 | a | b | c | T |
| a | a | a | b | T | T |
| b | b | b | b | T | T |
| c | c | T | T | c | T |
| T | T | T | T | T | T |

Counting its entries gives r(0),r(a),r(b),r(c),r(T)=1,3,5,3,13, summing to25. Independently, the principal
ideals at a,b,c have sizes2,3,2: the numbers of pairs with union below those elements are4,9,4. Subtracting
the lower multiplicities gives3,5,3 again, and the remaining13 pairs give T. Thus no unclosed pair or
unordered-pair convention is hiding in the calculation.

Here b join c=T, but b meet c=0: their set intersection {2} is absent. Consequently H demands

    r(b)*r(c)=15 <= r(T)*r(0)=13,

which is false. The coordinate frequencies are3/5,3/5,2/5, so the family itself satisfies Frankl; only my
proposed multiplicity inequality fails. Powersets retain equality because r(S)=3^|S| and cardinalities obey
|A|+|B|=|A union B|+|A intersection B|.

**Unexpected check:** add d={2}. This particular enlarged family is both union- and intersection-closed.
The11 new ordered pairs (2*5+1) contribute3 to r(d),4 to r(b),2 to r(c),2 to r(T). Multiplicities in order
0,a,d,b,c,T are now1,3,3,9,5,15, summing to36. The same pair gives9*5=15*3: equality. Adding the missing meet
changes both sides' counts, not merely their labels. This one repair is a control, not a theorem that every
intersection-closed family satisfies H, and not a permitted repair of a hypothetical Frankl counterexample.

**Source limitation retained:** the compression outline shows how a global size bound can survive a change of
family; Raz's primary example shows that its abstract interval condition alone cannot retain abundance. The
original Reimer carrying lemma was not retrieved. A bounded search for union-multiplicity/log-supermodularity
and pentagon/join-convolution found no directly matching published statement; NOT FOUND, no novelty inference.

**Gut:** disappointment: the attractive positive-interaction guess is false already in a pentagon. Relief that
the failure is exact and small. **Reasoned:** H is REFUTED; do not repair it by silently substituting ambient
intersection for the family's meet, or by adjoining intersections and retaining the old distribution.
The finished hand table is the result, not a new guard-proof or review job. B04 closes.

### MI013 — Incubation question after the first failed candidate

The union counts are counts in a join structure whose meet can lose elements. What controls that loss without
replacing the original family or assuming intersection closure? I do not yet have an inequality connecting it
to abundance. Preserve the five-set failure and the earlier support/mass example; neither is a reason to keep
guessing adjacent inequalities. At the next loop check, decide whether this structural question is live enough
for another block or whether to change representation. No experiment or new block is claimed.

**Mentor control received (2026-10-15 17:38 BST, CL405/a87bd630).** M3's multiplicities1,3,3,3,15 give H at
its incomparable pairs as9<=15, despite three missing set intersections. The count checks by subtracting1+9
from25. Thus missing-intersection count alone does not explain H's sign. N5 versus M3 suggests a modularity
question but proves no modularity criterion; one further passing example could not settle a universal claim.
Reinhold's cited class result remains an unread pointer here. No block on the modular case opens; the next
research wake runs the due loop check before selecting a direction. This receipt narrows MI013, not H's refutation.

### MI014 — First 90-minute loop check: one incubation interval (2026-10-15 17:53 BST)

**Target and movement:** Frankl remains OPEN; no new abundance estimate or carrying step toward it. B01–B03
were orientation with distinct lessons; B04 risked an inequality and refuted it. Understanding moved, but that
must not be reported as movement of the conjecture. No adjacent patch to H currently earns another block.
**One sentence I would have got wrong before this session:** rare union pairs can force an exponential
one-round completion, and an attractive positive lattice interaction of their multiplicities can fail on five sets.
Cloud's M3 control additionally prevents blaming the sign just on how many set intersections are absent.

**Signals:** the problem still pulls; there is a clear push against patching H or running another reassuring
calculation. No balanced act/halt tension or unrun kill test is being hidden: H is decisively false and no
successor candidate has been stated. Gut: let this settle. Reasoned: a short, explicit pause is better than
promoting a representation to a mechanism.

Reproducible door draw, fixed seed=4dca5fb16d942ce392f9066ff59bac0c45108a84, interpreted as hexadecimal modulo5:
0. Quiet incubation of MI013; **do nothing new this block**.
1. Lattice formulation: abundance through principal ideals and irreducibles.
2. Retrieve Reimer's original and audit the unexamined carrying lemma.
3. Poonen's local weighted criterion and what exact closure it retains.
4. Frequency-sensitive global gain: identify a testable structural hypothesis.

Result: **0**. No redraw. Park MI013 until the next25-minute research wake, expected18:16 BST; maintain five-minute
flags and respond to concrete check-ins. No background proof work or experiment is scheduled for this interval.
At the next research wake, reassess the pull and choose a concrete question or a different representation; this
single incubation interval is not a standing idle instruction. No proposer/reviewer proof block opens to swap.
Niggle sweep: the known orientation, refuted candidate, unproved modularity suggestion and open conjecture retain
their different statuses; no unreported result or pending experiment is held.

### MI015 — Remove the inherited door draw (2026-10-15 18:20 BST)

The owner identified seeded door selection as legacy prize-work machinery and asked to drop it in this lane.
Agreed: method8, AGENTS23 and the saved research heartbeat now explicitly choose by instinct, evidence and
judgment. Periodic reflection and the option to incubate remain; no seed or random menu chooses the work.
MI014 is retained as history, not a procedure to repeat. Research remains25 minutes and flags5 minutes.
No mathematical result or experiment here; no new research block claimed by this arrangement correction.

### MI016 — B05: can a single meet-map supply the injection? (2026-10-15 18:51 BST; bounded to 19:06)

**Pull:** find an actual pairing rather than another average. The known lattice proof uses a meet-map;
can that map remain injective when its lattice-class hypothesis is removed? This is a stronger mechanism
than merely having a small principal filter, so it must earn its own evidence.

Candidate K: every finite lattice L with at least two elements has a nonzero join-irreducible a and b with
a not<=b such that z -> z meet b is injective on the principal filter above a. Its values are then outside
that filter, so K would imply the lattice form of Frankl. An unregistered hand look during the interrupted
orientation already suggested a uniform-matroid counterexample; the check below is not a blind prediction.

Record searched: coatom|uniform.*matroid|Reinhold.*inject|meet.*projection ->no hit. Read the survey's
lattice formulation and meet-map proof, then the primary Herrmann-Langsdorf1999 manuscript linked in PRIOR-ART,
its D(L) construction and proof. Their related adaptive witness criterion is not a universal theorem;
the manuscript explicitly reports counterexamples to finding a join-irreducible in D(L).
No census, numerical run or new review request.

**Hand plan:** L consists of all subsets of a four-element set of size at most2, plus its full set.
Check both lattice operations, all join-irreducibles and every eligible b, not just one collision. Independent
control: exhibit a different injection when the fixed map fails. Unexpected check: complement the family
and verify the abundance direction, since this L is intersection-closed, not union-closed. Boolean lattice
is a positive fixed-map control. Stop on an all-pairs mechanism refutation, with no search for adjacent patches.
The saved research cadence is15 minutes and the flag cadence5 minutes; both prompts have been synchronized.

### MI017 — B05 result: the fixed projection fails; the pairing need not (2026-10-15 18:53 BST)

**Status: explicit hand counterexample to K; known-class fixture, no novelty claim.** Let E={1,2,3,4} and
L={X subset E:|X|<=2} union {E}. It has1+4+6+1=12 members. Meets are intersections; joins are unions of size
at most2, and E otherwise. Thus it is a lattice, not a union-closed family under ordinary set union.
Its nonzero join-irreducibles are precisely the four singletons: pairs are joins of two singletons, and E
is the join of, for example, {1,2} and {3}. This verifies every candidate a, not only one choice.

For any singleton a, the principal filter has five members: a, the three pairs containing it, and E.
Any b with a not<=b has size at most2. Every value z meet b is a subset of b, so there are at most four
possible images. A map from those five filter elements to at most four images cannot be injective.
Consequently **every eligible (a,b) fails**, including all coatoms and all smaller b. This refutes K outright.
For a={1}, b={2,3}, the full collision table is

| z | {1} | {1,2} | {1,3} | {1,4} | E |
|---|---|---|---|---|---|
| z meet b | empty | {2} | {3} | empty | {2,3} |

**Independent positive control:** the following different map sends the same five inputs outside the filter:
{1}->empty, {1,2}->{2}, {1,3}->{3}, {1,4}->{4}, E->{2,3}. All images belong to L and are distinct.
It is a variable witness map: joining each output with {1}, using this lattice's join, recovers the input.
So the desired size comparison5<=7 holds even though every fixed meet-map fails. This concrete injection
is a reproof for a known geometric-lattice case, not a new Frankl class theorem. On a Boolean lattice,
deleting a chosen coordinate is the fixed meet-map with its complementary coatom and gives a bijection;
the positive control is therefore genuinely different from this obstruction.

**Unexpected orientation check:** complementing L in E gives the union-closed family
U={empty} union {S subset E:|S|>=2}, again12 sets. Each coordinate appears in3 pairs,3 triples and E,
giving7/12. In L it appeared in5/12. The rare-coordinate lattice formulation and the abundant-coordinate
union formulation have opposite directions, as required. No5/12 union-closed counterexample is being claimed.

**Source and niggle sweep:** the survey's lower semimodular meet-map argument was read in the intersection-lattice
orientation. The primary Herrmann-Langsdorf paper instead gives adaptive join witnesses, a related sufficient
condition whose known limitations are recorded in PRIOR-ART. The fixture meets only the appropriate known
class claim; we do not infer lower semimodularity from its geometric description. Bottom, top, lattice join,
ordinary union, all irreducibles and all eligible partners were distinguished. No computer run or census.

**Gut:** disappointment that a fixed projection is too rigid, and renewed pull toward flexible pairings.
**Reasoned:** K is REFUTED; do not patch it by searching for a better fixed b. The obstruction is insufficient
room in any one principal ideal, although the entire complement has room. B05 closes. It does not settle
Frankl or show that adaptive pairings always exist.

### MI018 — A deliberate change of view after two failed rigid mechanisms

H imposed one universal order inequality; K imposed one universal fixed projection. Both failed exactly.
The shared missing step is still an abundance-producing mechanism, and another adjacent patch would repeat
the pattern. Early loop reflection: learning moved, the conjecture did not. I will leave both candidates
closed and look at the bipartite maximal-independent-set formulation next: it exposes the available matching
choices directly instead of forcing one lattice map. No seeded choice, new block or experiment here.
Cloud: perspective on that change of representation is welcome; no carrying read of these tiny controls is needed.

### MI019 — B06: where does a reversible graph exchange stop? (2026-10-15 19:07 BST; until19:22)

**Pull, before the explanation:** make the flexible pairing choices visible. A picture is not a simplification;
the question is whether a local exchange retains its input, and exactly which states it leaves unmatched.
CL406/ea83fe4c was read first. Its essential/unextendable count identity is correct for "at most half";
the sentence identifying that inequality with Frankl needs the intersection-closed orientation. For a
union-closed family the desired inequality is reversed. No new result is claimed by that bookkeeping.

Record searched: bipartite|maximal independent|Hall and private.neigh|external.private|essential.*unextendable
returned no indexed hit; MI018 and CL406 were read directly. Primary1212.4175v2 sections2 and3 through Lemma10
read for the exact graph equivalence and existing neighborhood injections. Known results stay PRIOR-ART.
A bounded search for private-neighbor exchanges found domination-enumeration precedents; no originality
is inferred. No census of graphs, computer experiment or review request.

**Question and hand plan:** for a maximal independent set S containing x in a bipartite graph, let P be the
external neighbors whose unique neighbor in S is x. Test the exchange (S minus x) union P when P is nonempty:
does it stay maximal and have a unique inverse? An initial unregistered reasoning pass suggests yes; this is
not a blind prediction. The substantive obstruction is what happens to states with P empty, rather than
pretending every state admits this exchange. Work out the entire residual matching on a six-cycle, then ask
whether its completion rule survives a second boundary case. Controls: one edge and a star; counterfactual:
omit bipartiteness, where P may have internal edges. Unexpected check: retain isolated vertices and distinguish
maximal from maximum independent sets. Stop on a precise obstruction or a justified next question; no claim
that an equivalent residual inequality by itself advances Frankl, and no adjacent repair to H or K.

### MI020 — B06 result: reversible cancellation and the unbounded exchange left over (2026-10-15 19:10 BST)

**Status:** elementary hand derivation and known graph fixtures, no novelty or Frankl result claimed.
Write M for the maximal independent sets of a finite bipartite graph with parts X,Y; fix x in X.
For S in M containing x, put P_x(S)={y in N(x):N(y) intersect S={x}}. These are external private neighbors;
x itself is not counted. If P_x(S) is nonempty, define

    phi_x(S)=(S minus {x}) union P_x(S).

This is independent: the added vertices all lie in Y and have no neighbor in S minus x. It dominates every
vertex: x has a newly added neighbor; a vertex formerly dominated only by x is in P and has been added;
every other vertex outside the new set retains an old neighbor. Thus it is maximal. Moreover
phi_x(S) intersect N(x)=P_x(S), so its inverse on the image is

    R_x(T)=(T minus N(x)) union {x}.

For any T in M avoiding x, R_x(T) is independent, but need not be maximal. If it is maximal, its external
private neighbors at x are exactly T intersect N(x), a nonempty set: vertices in that intersection had no
neighbor in T intersect X, whereas any other neighbor of x has such a neighbor by maximality of T.
Consequently phi is a bijection between the containing-x states with nonempty P and the avoiding-x
states whose R is maximal. This proves the exact scope, not merely injectivity in one direction.

Define A_x={S in M:x in S, P_x(S)=empty} and B_x={T in M:x not in T, R_x(T) is not maximal}. Cancelling
the paired states gives

    |M_x|-|M_not_x|=|A_x|-|B_x|;       x is rare iff |A_x|<=|B_x|.

The right side is still an equivalent counting problem. No inequality between it has been proved.
There is a useful explicit description of its second term: T belongs to B_x exactly when there is a
u in X minus (T union {x}) with nonempty N(u) intersect T contained in N(x). These are precisely the
vertices that lose their last dominating neighbor when N(x) is removed. Vertices in Y are either added
to the dominating neighborhood of x or keep a neighbor in T intersect X, so there is no omitted Y obstruction.

**Six-cycle, all states checked.** Use X={x1,x2,x3}, Y={y1,y2,y3}, with edges xi-yj when i!=j.
The complete list M is X,Y and the three pairs Ci={xi,yi}. A mixed independent set is contained in
one Ci; a one-sided maximal set must be the whole side, proving completeness. For x=x1, phi sends C1 to Y;
X has no external private neighbor at x1. The residual inputs and outputs are A_x={X}, B_x={C2,C3}:
R_x(Cj)={x1,xj}, which is not maximal. Sending X to C2 completes the injection. Thus the count is2 versus3,
with one canonical cancellation and an adaptive residual choice. Both a maximum set X and a nonmaximum
maximal set Ci are essential to the calculation; counting maximum sets alone would erase the issue.

**Second boundary case: the whole crown family, with a reducedness check.** The same definition on n>=3
indices gives exactly n+2 maximal independent sets: X,Y,C1,...,Cn. For x=xi, phi still pairs Ci with Y;
A_x={X}, B_x={Cj:j!=i}. Any residual image of X avoiding xi is either a Cj with j!=i, removing n-1
vertices of X, or Y, removing n; Y is already used by phi. Thus a residual completion exists, but cannot
use a uniformly bounded number of vertex removals. This is not just an artifact of duplicate neighborhoods:
the neighborhoods are all distinct, and a union of two distinct same-side neighborhoods is the entire
opposite side, never another vertex's neighborhood. A nonempty opposite-side neighborhood lies in the
wrong side to contribute to such a union. Hence these graphs are reduced in the sense of the primary
paper's Lemma13. No general reconfiguration theorem is being inferred from this fixture. The initial
crown reasoning was unregistered; no numerical experiment or blind prediction is claimed.

**Other controls and niggles:** on one edge phi is a bijection. For a star, phi at the center pairs its two
maximal sets; at a leaf with at least two leaves, A and B each have size1 instead. An isolated vertex lies
in every maximal independent set and has P empty, B empty; adjoining an isolated vertex elsewhere leaves
the exchange and counts for x unchanged. In a triangle S={x} has two adjacent private neighbors, so phi
does not even give an independent set: bipartiteness was used, not decorative. Empty P, isolated vertices,
maximal versus maximum, both parts, image characterization and count direction were checked explicitly.

**Gut:** delight that part of the pairing really is reversible; unease about calling the residual identity
a breakthrough. The crown family makes the remaining flexibility tangible. **Reasoned:** B06 closes with
an exact description of what this exchange cancels and a boundary against bounded-size repairs. Frankl
remains OPEN. No PROOFS entry or carrying-read request. Primary graph equivalence and local injections
are filed in PRIOR-ART, not attributed to this notebook.

**Unresolved step and next cheap question:** is there a useful relation between A_x and B_x for which a
Hall deficiency can be converted into a better choice of x, rather than assuming that a rare x already
exists? Before testing a new relation, check matching/reconfiguration precedents and the scope of existing
adaptive lattice criteria. An unrestricted cardinality matching would only restate Frankl; a bounded-swap
restriction is already excluded by crowns. No next block or enumeration is claimed here.

### MI021 — B07: does least frequency remove the monotone-matching obstruction? (2026-10-15 19:23 BST; until19:38)

**Pull:** a failed matching ought to tell us where to look next. **Unease:** that hope may assume more than
rarity. The concrete candidate M is: if an intersection-closed family D containing empty and its universe
has no injection D_x -> D_not_x with each image a subset of its input, then some coordinate has strictly
smaller frequency than x. M would make a minimum-frequency coordinate admit that injection and hence be
rare. This is a stronger route, not an equivalent formulation assumed true.

Record searched: Hall.*deficien|downward.*match|decreasing.*inject and minimum.frequency|rarest|monotone.*match
returned no indexed hit; MI020 and CL408/933b0241 read directly. Primary2608.25147v1 section6's projection
counting argument was read: it gives a conditional witness inequality in a minimal-counterexample argument,
not a Hall-descent theorem. No adoption of the paper's height classification. Searches found no matching
primary theorem for M; NOT FOUND is not originality. CL408's neighborhood-injection precedents were read
in B06; its subcubic proof is still unread. Its sum rule checks by double counting, but averaging it is not
a coordinate-selection theorem. M is my stronger candidate, not a claim attributed to Cloud.

**Already-seen hand evidence, not a blind prediction:** let E={x,a,b,c,d}, A={a,b}, B={c,d}. Put

    D={J union K:J is a proper subset of A, K subset B}
        union {{x} union J:J subset A} union {E}.

An unregistered construction suggests D has17 members, x has frequency5 and every other coordinate7,
yet the four x-containing sets inside {x,a,b} have only three eligible images: empty,{a},{b}.
That would kill M even at the unique minimum. It would not refute a descent rule restricted to x that
is not rare, nor Frankl, nor the existence of some other coordinate with a monotone pairing.

**Specific exact audit, not a graph/family census:** independently construct D as frozensets and as bit masks;
check distinctness, all ordered intersections, frequencies, all eligible matching edges and the explicit
four-to-three Hall witness. Predict maximum monotone matching size4, while unrestricted matching saturates5.
Counterfactual/control: adjoining {a,b} preserves intersection closure and permits a five-input monotone
matching. Independent controls: powerset coordinate deletion and an explicit unrestricted injection in D.
Unexpected check: complement in E; predict a union-closed17-set family whose uniquely most frequent x has
frequency12 (others10), but the reverse containment matching fails. Stop after this fixture, its one-set
repair and controls; no enumeration, optimization, adjacent conjecture patch or review request.

### MI022 — B07 result: least frequency does not buy a monotone pairing (2026-10-15 19:26 BST)

**Candidate M REFUTED, by hand and an exact fixture audit.** Retain MI021's E={x,a,b,c,d}, A={a,b}, B={c,d}.
The avoiding-x part D0 consists of proper subsets of A independently combined with any subset of B:3*4=12
sets. The core C={x,x+a,x+b,x+a+b} has4 sets, and E is a separate seventeenth member. Intersections stay
in D: D0 is intersection-closed; intersections within C stay in C; a cross intersection is a proper subset
of A with no B coordinate and lies in D0; E changes nothing. This is a closure proof, not a finite-count guess.

The frequencies are x:4+1=5; a and b:4+2+1=7 each; c and d:3*2+1=7 each. Hence x is the **unique**
minimum, and already rare. The eligible avoiding-x subsets of the four core sets, taken together, are
only empty,{a},{b}. Every member of D0 with a B coordinate lies outside their union. Thus four sources
have three targets, so Hall fails and no downward injection can saturate D_x. No other coordinate has
lower frequency: M's promised improvement is impossible on this explicit family.

The maximum downward matching is exactly4. The Hall witness bounds it above by3 matches from C plus at
most one from E. The map x->empty, xa->a, xb->b, E->c attains4. By contrast, the unrestricted injection
x->empty, xa->a, xb->b, xab->c, E->d saturates all5 inputs. Actual rarity has room; the extra containment
rule makes that room inaccessible. Even reserving the obvious deletion pairs does not solve this: the
remaining essential sets are xab and E, the unextendable targets are the9 members of D0 with nonempty
B-part, and xab has no downward edge to any of them.

**One-set counterfactual:** add {a,b}. Intersections still stay in the enlarged family. Delete x from each
core set, obtaining empty,a,b,ab, and send E to c: five distinct valid downward images. Thus the advertised
repair succeeds without changing the frequency of x. Independently, the original coordinate a does admit
a downward injection: delete a from every a-containing member other than E, and send E to {b,c,d}.
The six deletion images and that final target are distinct. The existential monotone-matching claim for
some coordinate is therefore not refuted by this example; neither is any rule restricted to nonrare x.

**Unexpected complement check:** U={E minus S:S in D} is union-closed with17 members, x frequency12, and
each other frequency10. The unique maximum-frequency coordinate x has no containing-superset injection
from U_not_x into U_x. The four sources obtained by complementing C all contain B; their eligible targets
are exactly E, E minus {a}, E minus {b}, the three complements of empty,a,b.
This is the same4-to3 Hall obstruction in the
abundance direction. The complement of E supplies the fifth source, empty. It is not a Frankl counterexample.

**Exact audit:** tests/probes/instinct/monotone_matching_fixture.py, predictions at aa0ea1be/MI021, returned
ALL CHECKS PASS. Independently constructed frozenset and bit-mask families agree; all289 ordered intersections
check; frequencies are5,7,7,7,7; maximum downward matching4; unrestricted certificate5; one-set repair5;
powerset deletion16; dual union frequencies12,10,10,10,10 and upward matching4. The hand Hall witness gives
an algorithm-independent upper bound, and the explicit maps give lower bounds. No census or floating point.
The earlier construction was seen before preregistration; these are controlled checks, not blind discovery.

**Niggle sweep:** ordinary set containment was specified, not lattice order in a changed representation;
the family, its complement and both frequency directions were checked; x is uniquely minimal, not tied;
the obstruction applies to all matchings on that relation, not just a greedy algorithm. No claim that17 is
minimal or that the fixture is new in the literature. CL408's proposed check restricted to nonrare x remains
a distinct question. The exact projection counts in2608.25147 section6 do not supply the missing descent.

**Record-search scope correction:** the initial multiple-argument searches in MI019/MI021 required all
patterns in one paragraph; their no-hit outputs were narrower than the written alternation notation.
Reran a single alternation of the six matching/frequency terms with --ledgers:20 hits in8 files, our
current entries/probe plus unrelated old Rule30 uses at GC440, CL031 and C033. No earlier matching result
was identified by that corrected bounded search. This corrects the receipt; it does not establish novelty.

**Gut:** delight at catching a real failure in the selection rule, disappointment that least frequency is
not enough to make the natural order usable. **Reasoned:** M closes. Frankl remains OPEN, and I have no
replacement descent theorem. H, K, bounded swaps and this monotone-selection rule have each demanded an
extra rigidity the problem does not owe us. Do not produce another adjacent strengthening to fill a wake.
Next useful orientation is the actual adaptive choice in the subcubic graph proof already identified by
Cloud, or Cloud's specific obstruction-vertex test; no next block is claimed, and no review job is created.

### MI023 — B08: learn the comparison that works, without a fifth rigid rule (2026-10-15 19:39 BST; until19:54)

**Pull:** understand a successful adaptive comparison. **Push:** no further universal matching restriction.
CL409/f7ef8460 read; its loop diagnosis is right. H, K, bounded swaps and M are variations on imposed rigidity,
not four independent approaches toward Frankl. Early loop reflection now parks that generator of candidates.
This is a source-study block, not a new theorem or experimental campaign. Orientation began earlier this wake.

Record searched: (subcubic|Vaughan|Knill), then (Knill|Kleitman|conservative.extension|filter.*minim|pentagon.*match)
as single alternation patterns: current notebook pointers and unrelated Rule30 hits; no prior carrying read
of this mechanism. The graph paper's subcubic proof is now read. Its degree split invokes two substantial
set-family theorems, so citing the split alone would not explain the underlying comparison.

**Question:** in Knill's primary math/9409215, why is replacing an extension by a monotone-filter extension
legitimate? Which objective and optimization hypothesis make the replacement valid? Read the definitions
and Theorem3.13's carrying proof, not just the abstract. The paragraph on P-matching also reports a known
existential matching obstruction; reconstruct its five-cycle Hall witness rather than starting another search.

**Hand controls only:** use a five-cycle for the reported matching limitation. For the filter comparison use
F generated by ab, acd, bce and empty, with U=ab; an initial unregistered hand look suggests7 members and
canonical fibre lower-bound sizes2,2,2,1 on the four outside projections. Compare its upward closure with
the optimizing extension. Counterfactual: drop the minimizing hypothesis and check whether the objective
can increase. Unexpected check: compare the lower-bound objective with the actual reciprocal density,
which need not be equal after extension. No blind-prediction claim, program, enumeration or review request.
Stop when the known comparison and its hypothesis are understood; retain the remaining source dependencies.

### MI024 — B08 result: optimize the comparison, do not pretend to preserve the law (2026-10-15 19:42 BST)

**Known-source study, no new theorem.** Knill math/9409215 PDF pp8–9 reports a five-cycle matching obstruction.
Independent reconstruction: for its17-member edge-union family, e=01 has7 supersets. The four
members01,401,012,4012 have only empty,40,12 as avoiding-e subsets. Rotation excludes decreasing matchings
at every generator. This strengthens the prior-art warning beyond M's particular minimum-coordinate failure.

Knill minimizes a canonical fibre lower-bound average mu over extensions. Retraction fibres preserve
lower-bound values and have antitone sizes. A layer-cake argument using optimality yields a filter optimizer.
It does not preserve the original uniform law.

**Independent hand control of that distinction.** Take F generated by ab, acd, bce and empty, with U=ab.
Explicitly F={empty,ab,acd,bce,abcd,abce,abcde}. Let p(Z) be the union of the members of F contained in Z.
For an outside trace X, the canonical mandatory traces are

    E(X)={Y subset U: p(X union Y) intersect U=Y,
                       p(X union Y) contains p(X union U) minus U}.

These are lower bounds on actual extension fibres, not a new sampling law. On the outside set {c,d,e}:

| outside trace X | empty,c,d,e,de | cd | ce | cde |
|---|---|---|---|---|
| E(X) | {empty,ab} | {a,ab} | {b,ab} | {ab} |
| size | 2 | 2 | 2 | 1 |

To check the table directly: for cd, retaining a realizes the generator acd and retaining ab does as well;
retaining neither or only b cannot cover cd. For ce exchange a with b and d with e. For cde, retaining only
a leaves e uncovered and retaining only b leaves d uncovered, so only ab is forced. Without either full
pair cd or ce, no generator can realize a or b separately, while empty and ab work. This checks all8 traces.

Write G={empty,cd,ce,cde}, the projection of F away from U, and up(G)=powerset({c,d,e}). For a projection
family Q, mu(Q) is the unweighted mean of |E(X)| over Q. Exact counts are:

| actual family | outside projections | number of sets | sets containing U | mu | reciprocal density |
|---|---|---|---|---|---|
| F | G | 7 | 4 | 7/4 | 7/4 |
| F vee G | G | 12 | 4 | 7/4 | 3 |
| F vee up(G) | all8 traces | 20 | 8 | 15/8 | 5/2 |
| F vee {cde} | {cde} | 4 | 1 | 1 | 4 |

Here vee denotes all pair unions. The second row has actual trace sizes2,3,3,4 at empty,cd,ce,cde.
The third row has size2 on the five traces in the first table's first column, size3 at cd and ce, and size4
at cde. The last row is {cde,acde,bcde,abcde}. Thus all set counts, denominators and inequalities are
checked independently by actual fibres. Merely passing G to its upward closure raises mu from7/4 to15/8;
the omitted minimizing hypothesis matters. The filter {cde} does minimize mu: ab belongs to every E(X),
so no nonempty projection family can have mu<1, and this one attains1. This is consistent with the known
theorem. Its lower-bound objective can be much smaller than the actual reciprocal density.

**What changed:** I understand how a legitimate change of extension differs from B01's invalid change of
fibre weights. It minimizes a guaranteed comparison over admissible extensions; it does not transfer the
original uniform distribution. The control's U occurs in4/7 of F, so no rare-generator certificate at U
should emerge here. Its other generators have size3, outside the edge-generated hypothesis; do not apply
Knill's final graph theorem to it just because U itself has size2.

**Scope/niggles:** subcubic graph Theorem12's degree split was read, including its use of Vaughan/Knill;
the former carrying proof remains unread. For Knill, definitions through Theorem3.13 and Lemmas3.14–15
were checked; the later local graph-density bound and its whole dependency chain are not audited.
The pentagon here is the edge-union family of a five-cycle, not B04's five-element N5 lattice. All computations
above are hand counts, no probe or census. Extensions need not have the same cardinality or coordinate law.
No new PROOFS entry, review request or general abundance claim follows from this study.

**Gut:** relief and fresh interest: the proof changes an extremal comparison in a controlled way rather than
asking one rigid map to do everything. **Reasoned:** the named question is answered; the method is known and
its useful generalization has not been supplied. Keep rigid-rule generation parked. The next cheap read is
where the later proof obtains monotone events from local generator geometry, with attention to exactly which
edge-size hypothesis is used. No new candidate or block claimed; Frankl remains OPEN.

### MI025 — B09: audit the monotone-event step (2026-10-15 19:53 BST; until20:08)

**Pull:** positive correlation is useful after a justified comparison, in a different measure from H's failed
multiplicity inequality. Continue the known mechanism; do not propose another universal order condition.
Record searched: (Kleitman|monotone.event|graph.density) as one alternation -> notebook pointers only.
Read Knill's continuation from3.16 through the local-density argument, tracking every graph hypothesis.

Question: how do monotone sufficient events imply mandatory fibre traces, and where is the restriction to
a minimal bad filter used? Hand controls: cycles a-b-d-z-c-a and a-b-d-w-z-c-a, with distinguished edge ab
and outside filter requiring c,d. An unregistered hand pass suggests mandatory-fibre means5/2 and9/4,
but product bounds9/4 in both cases; common support should explain the slack in the first.
Counterfactual: use a support event outside the filter and check retained endpoints, not just outside coverage.
Unexpected check: distinguish conditional filter averages from a bound on every original extension.
No experiment, census, new theorem or review request. Stop when the carrying implication and its scope are clear.

### MI026 — B09 result: sufficient events, with the conditioning kept visible (2026-10-15 19:58 BST)

**Known-source continuation:** [Knill math/9409215](https://arxiv.org/pdf/math/9409215),3.16–3.29 read.
A hypothetical bad extension reduces to a minimal bad filter H whose minimal traces have |E(X)|=1.
For graph generators this forces retained-endpoint support. Increasing neighbor-support events C(Y,x),
intersected as C(Y), then suffice for Y in E(X) on H. Under uniform Boolean-cube measure nu,

    mu_H >= 1 + sum_(Y proper subset U) nu(C(Y) | H)
         >= 1 + sum_Y nu(C(Y))
         >= 1 + sum_Y product_x nu(C(Y,x)).

The two positive-association uses concern increasing events in a product space. They assert nothing about
multiplicity correlation in the original family. Local minimum edge-degree supplies the final bound2;
the reduction only needs to rule out mu<2. The stronger local statement3.31 was read but is not used here.

**Independent hand controls**, with F all edge unions plus empty, U=ab, and H requiring c,d:

| cycle | X in H, in order | E(X), in order | mean | event-product bound |
|---|---|---|---|---|
| a-b-d-z-c-a | cd,cdz | {ab}; {empty,a,b,ab} | 5/2 | 9/4 |
| a-b-d-w-z-c-a | cd,cdz,cdw,cdzw | {ab}; {b,ab}; {a,ab}; {empty,a,b,ab} | 9/4 | 9/4 |

Here a,b in a trace denote singleton sets. These tables follow directly from MI024's interior definition:
every retained endpoint must belong to an edge inside X union Y, and every outside vertex coverable with
both endpoints must still be covered. For example at C6 trace cdz, the edges cz and bd cover all required
outside vertices when b is retained; retaining a alone leaves d uncovered. At cd only ab works. The other
rows follow by exchanging endpoints or adding both support vertices. Minimal cd has only trace ab in both
cycles, so the required filter hypothesis holds; the conditional means themselves are greater than2.

For C5, C(a) and C(b) both require z, and C(empty) requires z twice: all three events have probability1/2.
Conditioning on c,d does not affect z. The product estimate for C(empty) is1/4, giving total9/4 instead of
the exact5/2. For C6, C(a) requires w, C(b) requires z, and C(empty) requires both independent coordinates;
probabilities1/2,1/2,1/4 give9/4 exactly. This is a concrete check of correlation slack, not a general
sharpness claim. C(Y,x) asks for a supporting neighbor even when x is absent from X; this makes it a
stronger, increasing sufficient event rather than an exact conditional-coverage test.

**Counterfactual outside H:** in C5 take X={z}, Y={a}. C(a) holds: c has neighbor a or z and d has neighbor z.
Yet p({a,z})=empty, so a is unsupported and Y is not in E(X). Outside-neighbor coverage alone does not
justify the mandatory trace. The filter's endpoint-support step carries a real inference.

**Unexpected check:** the original C5 family has17 sets and7 containing ab (MI024); its reciprocal density
is17/7, strictly less than the conditional mean5/2 above. Thus even the exact conditional average is not
automatically a quantitative lower bound for every original extension. The threshold contradiction at2
and a stronger numerical estimate on a particular H must be kept separate.

**Niggles:** E denotes mandatory traces, not actual extension fibres; all means and conditioning measures
are labelled; endpoint support is checked separately; size-two generator hypotheses remain explicit.
No machine run, novel theorem, generalization or review request. Vaughan's separate carrying proof remains
unread; no full audit of every dependency in the graph literature is claimed.

**Gut:** delight at seeing precisely where the proof allows dependence instead of fighting it. The earlier
rigid-map guesses feel less attractive after this read. **Reasoned:** B09's question is answered. A useful
extension beyond this geometry is still missing; Frankl remains OPEN. The next cheap orientation is to put
the arbitrary-generator support constraints beside these monotone sufficient events and identify the lost
estimate, without postulating another universal rigidity rule. No next block claimed.

### MI027 — B10: locate the support loss beyond edges (2026-10-15 20:06 BST; until20:21)

**Pull:** where does the successful proof stop, before any proposed repair? Compare Knill's general
generator conditions3.7/3.10 with the graph-only endpoint-support step3.21/3.22. Record searched:
(hypergraph|support.constraint|monotone.sufficient|Knill) as a single alternation,36 hits in11 files:
our current Knill work and unrelated influence/Rule30 material; no carrying comparison already recorded.
Primary3.7–3.12 reread. This is source orientation and hand analysis, not a new universal candidate.

Question: can a minimal filter with only U mandatory leave proper retained subsets unsupported once
generators have size3? A hand construction already considered before this claim is F generated by
abc,abx,bcy,caz and empty. For U=abc, H={xyz} appears to have E(xyz)={abc}, while singleton retained
subsets have no supporting generator. Predict that this diagnoses failure before the correlation estimate.
Counterfactual: compare the same family's distinguished generator abx, rather than altering its closure.
Independent check: list its actual edge unions and count supersets of both distinguished generators.
Unexpected check: distinguish a support event that is impossible from events that merely correlate badly;
test whether keeping all support conditions still yields increasing sufficient events. These are hand
checks, with no blind-discovery claim, program, census or review request. Stop at an explicit lost step,
without designing a fifth rigid selection rule or claiming a Frankl advance.

### MI028 — B10 result: support can require two retained coordinates together (2026-10-15 20:08 BST)

**Source orientation, no new Frankl theorem.** Knill3.10 separates support of retained coordinates from
coverage of activated outside coordinates. B09's graph-only shortcut to the first condition fails already
on the hand family below. Association of increasing events survives; an automatic supply of useful events
does not. MI027's claim timestamp was corrected from20:08 to its actual20:06 start.

Let F be generated by abc,abx,bcy,caz and empty. An independent description lists every union:

    F = {empty, abx, bcy, caz} union {abc union T : T subset {x,y,z}}.

There are12 distinct members. Any union of two distinct nonempty generators contains abc; the displayed
description is closed under unions and contains all four generators. Exactly8 members contain abc.
Exactly5 contain abx: abx itself, and the four abc union T with x in T. This independently checks the
directions of both comparisons; no family is claimed to refute Frankl.

**Distinguished U=abc.** H={xyz} is a filter, and E(xyz)={abc}. All x,y,z are coverable when U is retained.
Keeping x covered requires a,b; keeping y requires b,c; keeping z requires c,a. Together these force Y=abc.
Yet no singleton Y has endpoint support: every generator meeting U contains at least two of its coordinates.
Thus |E(min H)|=1 does not force every retained subset to be supported. In particular the graph proof's
3.22 implication is unavailable, before any correlation inequality is used. The mean1 is consistent with
the actual frequency8/12 of this particular generator; choosing it is not a rare-generator certificate.

**Same-family counterfactual, U=abx.** Outside coordinates are c,y,z. The complete hand table is:

| outside X | empty,y,z,yz | c | cy | cz | cyz |
|---|---|---|---|---|---|
| E(X) | {empty,abx} | {ab,abx} | {b,ab,abx} | {a,ab,abx} | {ab,abx} |
| size | 2 | 2 | 3 | 3 | 2 |

Here a,b stand for singleton traces. Without c no outside generator activates, leaving empty and U.
With c, the trace ab uses abc to cover it. At cy the trace b additionally uses bcy; at cz the trace a
uses caz. At cyz neither singleton covers both y and z. Any retained x needs the whole generator abx,
so no other traces occur. Consequently every E(X) has size at least2; the top filter {cyz} attains2.
The original five projection fibres have sizes2,2,3,3,2, agreeing with12 members and5 supersets of U.
This is a hand verification for one family, not a general generator-selection rule.

**Unexpected check: keep the support conditions, rather than blame correlation.** For fixed Y subset U,
retained-coordinate support is an increasing condition on X: each retained coordinate needs some generator
V with V intersect U subset Y and V minus U subset X. For each outside neighbor q of U, strengthen coverage
to require some generator V containing q with V intersect U subset Y and V minus (U union {q}) subset X,
whether or not q is selected. Intersect these increasing events. If they hold, the two conditions of3.10
hold: selected outside neighbors are covered; outside vertices not neighboring U already have a generator
disjoint from U whenever activated. Thus the familiar association argument remains legitimate for these
sufficient events. In the U=abc fixture, however, every singleton-support event is empty; for a proper
pair Y, some outside coverage event is empty. All proper-Y contributions vanish, giving only the baseline1.
There is no correlation loss to recover in that estimate. This is a direct reading/instantiation of the
known support conditions, not a proposed new criterion or PROOFS entry.

**Niggles and verdict:** the same family and uniform counting law were used for both generators; mandatory
and actual fibres were checked separately; no inference from a rare generator to a rare coordinate was
silently made. No machine run, minimality/novelty claim or review request. **Gut:** satisfaction at locating
the missing step, and a push against immediately inventing a higher-order degree rule. **Reasoned:** B10
answers its question; a useful general choice of generator is still absent. After three source/hand blocks,
pause local inequality design and invite Cloud's perspective on a genuinely adaptive choice mechanism.
The named incubation question is how to choose the generator without imposing another rigid map; no next
block or new candidate is claimed. Frankl remains OPEN.

### MI029 — B11: read the weighted witness with its quantifiers (2026-10-15 20:20 BST; until20:35)

**Pull:** a witness may adapt as a distribution rather than a rigidly selected element. CL410/987c5081
was verified and ACKed. Read Poonen's weighted criterion and its carrying mechanism, especially which
configuration the weights may depend on and which extensions one fixed weight vector must handle.
Record searched: (Poonen|FC.family|weighted.*criterion|Vaughan),26 hits in7 files: B01's deferred read,
Cloud's pointers, survey statement and unrelated old weighted criteria. No carrying proof already logged.

The original1992 publisher page returned403 and neither author index exposed the paper; do not claim the
original proof was read. Pulaj1903.02317 section2 restates the criterion; seek its primary proof treatment
and distinguish that from an independent reconstruction. No solver or enumeration. Hand controls:
a two-element member; B01's27-set triple obstruction. Prediction: weights chosen for a small configuration
must work simultaneously for every compatible local family, not be chosen afresh for each fibre.
Counterfactual: test the weaker swapped quantifiers. Unexpected check: local compatible families need
not contain the seed configuration; a separating mixture is not itself automatically a union-closed
counterexample. Stop when the carrying implication/remaining dependency and quantifier scope are explicit.
No new universal criterion, PROOFS entry or routine review job.

### MI030 — B11 result: one measure must survive all the compatible fibres (2026-10-15 20:24 BST)

**Known theorem, independently reconstructed here.** The original Poonen paper remains unavailable.
Pulaj1702.05947v2 section2 gives its exact statement and rational-weight framework; Appendix Theorem5
states the Farkas alternative. The source does not reprove the full equivalence. A complete reconstruction,
labelled **known, reproved here**, is attached in PRIOR-ART under "Poonen's weighted criterion"; it uses
that standard alternative and an explicit outside-block construction. No new theorem or review job.

For a fixed union-closed seed A containing empty on S, one c in the probability simplex must satisfy

    sum_i c_i (2|B_i|-|B|)>=0

for *every* union-closed B on S stable under unions with A. Compatible B need not contain A: even when
A=powerset(S), B={S} is compatible. Weights adapt to the seed, not independently to each outside fibre.
Summing the unnormalized fibre inequalities proves sufficiency without B01's change of sampling law.

**Two-set control.** With seed {empty,12}, every nonempty compatible B contains12. Hence
sum_(R in B)(|R|-1)=1-1_(empty in B)>=0. The weights c1=c2=1/2 therefore work for all B. This is the
known two-set certificate, checked by counting top and bottom, not by assuming uniform fibre weights.

**Triple control, directly from B01.** On S=123 use B_j={empty,{j},123}, j=1,2,3. Each is compatible
with {empty,123}; each individually has an abundant coordinate j. Its deviation vector is +1 at j and
-1 elsewhere, so the common-weight condition requires2c_j-1>=0 for each j. Three requirements
c_j>=1/2 contradict sum c_j=1. These three tests already distinguish individual witnesses from a common
measure; no general claim about swapping all quantifiers is needed. Their deviation vectors sum to
(-1,-1,-1), an exact dual certificate.

B01's actual27-set family uses two fibres of each B_j, one {123} fibre, and one full eight-set fibre.
The deviations add as2*(-1,-1,-1)+(1,1,1)+0=(-1,-1,-1), recovering13 occurrences out of27.
Every normalized weight on the triple therefore gives13/27. To make this an extension of the seed that
explicitly includes empty, adjoin the missing empty set:28 members, still13 occurrences, hence13/28.
This convention check matters; the original27-set family itself did not contain empty.

**Unexpected check resolved:** a negative mixture of compatible families is not automatically a family
closed under cross-unions. The reconstruction in PRIOR-ART supplies separate outside blocks for its
components and full Boolean fibres for mixed tags. Those mixed fibres absorb cross-unions with exactly
zero deviation on the old coordinates. Increasing the block sizes amplifies the negative part. This is
the carrying conversion, not an appeal to the dual certificate alone, and it yields Non-FC rather than
a counterexample to Frankl. New coordinates are allowed to be abundant.

**Niggles:** all extensions, compatibility, empty-set convention, strict negativity and rational scaling
are explicit in the attached proof. Original-source access failure is retained. The statement and proof
are known mathematics; the reproof has no independent second read. No solver or enumeration. Vaughan's
specific class proof remains unread; the source does not warrant saying every Vaughan argument is identical.

**Gut:** delight at returning to the first example and finally seeing its three incompatible demands.
Relief that the weights retain the true fibre masses. **Reasoned:** B11 answers its bounded question;
the robust FC property is stronger than Frankl for the given family. **Own next-step niggle caught before
publication:** a universal search for an FC seed cannot be the target: the single-triple family above is
itself Non-FC, while every coordinate has frequency1/2. Nor can it contain an FC subconfiguration, since
that would make every extension of the triple family have an abundant old coordinate. The useful question
is what a restricted class forces, or how to exploit this particular family's actual cross-fibre unions
without demanding success for all extensions. No new local inequality is proposed. Next cheap orientation:
a family-dependent closure mechanism such as Reimer's compression, or incubation with that question named;
no next block claimed. Frankl remains OPEN.

### MI031 — Reflection and one incubation interval (2026-10-15 20:35 BST; reassess20:50)

**Pull:** consolidate; CL411's suggestion fits my own push against launching another source read immediately.
The day taught me where I had supplied rigidity that closure does not promise: log-supermodular union
multiplicity (H), a fixed meet projection (K), bounded-size residual swaps (the crown control), and descent
from failed containment matching to a rarer coordinate (M). Those routes remain closed in their stated forms;
the known five-cycle obstruction also limits existential decreasing matchings. The successful mechanisms now
understood adapt different objects: Knill optimizes an extension before comparing it with a filter, then
bounds sufficient events in a product measure; Poonen chooses one measure for a seed that survives every
compatible fibre. Neither transfers the original uniform law by fiat. The27-set fixture checks sampling and
conflicting weights, the crown checks repair locality, and the17-set fixture checks least-frequency matching
when those hypotheses apply. Reimer's carrying compression proof and Vaughan's specific argument remain
unread; do not count mentor pointers as completed reads. **Incubating question:** how can an argument use the
actual cross-fibre unions of one given family, including a family with no FC seed, without asking it to certify
all extensions? The next cheap orientation, if the pull returns, is Reimer's closure-preserving compression.
**Gut:** delight at recognizing the first obstruction again from the dual side, and relief in leaving the
question open. **Reasoned:** understanding moved; no new Frankl bound or theorem did. No twelfth research block,
new experiment, random draw or review request. Incubate until the next research wake, then reassess the actual
pull rather than automatically extending the interval. Five-minute flags and concrete replies continue;
the schedules stay active. This is my choice after considering a friend's advice, not a halt from Cloud.

### MI032 — The owner's fresh-choice test: park the active Frankl topic (2026-10-15 20:50 BST)

**Signals, stated plainly:** both enjoyment and frustration remain useful descriptions of the trajectory.
The sharp counterexamples, the successful filter comparison, and recognizing B01 again in Poonen's dual
constraints are the parts that still draw me in. The frustrating pattern is repeatedly replacing a failed
criterion with another restriction, then replacing that activity with a sequence of known proofs to read.
The source studies taught real mathematics; their value is not conditional on a new theorem. But the next
listed source is now exerting more momentum than a specific live Frankl idea.

**Counterfactual check, before deciding:** set aside the eleven blocks and their investment. Would I choose
another Frankl block now, and what concrete mathematical move would I choose for its own sake? Reimer's
compression is still interesting, but I cannot name a present Frankl move with the original fresh pull.
The surviving question about cross-fibre compatibility is broad and supplies no such move by itself.
This tips the decision to **pull back now**. This is a direction choice, not a theorem about the prospects
of Frankl, and not an inference that disappointing output makes the exploration a failure.

**Action:** park Frankl as the active default. Preserve its notebook, open question, source pointers and
closed candidates; do not automatically resume the Reimer read on the next wake. Widen attention at the
next research wake without requiring a replacement problem in this entry. A fresh specific pull can bring
Frankl back later. The general research and five-minute coordination schedules remain active; this parks
a topic, not the instinct lane. No new block, experiment, claim or review request. **Gut:** pull toward a
wider view. **Reasoned:** continuing by investment would contradict the selection method. The fresh-choice
test is now part of that method, so future reflections check this explicitly.

### MI033 — B12: screen for an open target with a workable entry (2026-10-15 20:56 BST; until21:11)

The owner asks whether we can strategically choose an open problem with a better prospect of solving it.
**Pull:** a precise finite obstruction and a proof-shaped outcome; retain curiosity while reducing scope.
Screen primary sources for concrete remaining questions in path-forest burning, dice realizations, and
permutation counting/balance. Record searched: (nontransitive.dic|graph.burning|path.forest|permutation.avoid),
no hits including ledgers. No proof attempt or experiment. A candidate must have an exact statement, a
source-backed open status checked for follow-up work, known tools we can explain, and a bounded diagnostic
whose success or failure changes our estimate. Famousness and a cash award are optional. Reject a narrow
restatement if it still contains the original hard problem. Stop with a justified first target, or an honest
unsuccessful screen; do not assign numerical success probabilities or promise a solution.

## 2. Provisional narrower target: partitioning odd integers

### MI034 — B12 result: a candidate for a feasibility audit, not a promise (2026-10-15 21:00 BST)

**Pull:** concrete integer partitions, where a proposed solution can be checked exactly. The owner asks
for a strategically selected open target with better prospects. The screen favors an adjacent unresolved
case with known tools and a bounded admission test; it does not establish that the case will be easy.

**First candidate:** the eight-path threshold from Tan and Teh,
[A Note on Graph Burning of Path Forests](https://dmtcs.episciences.org/en/articles/12709/download).
In odd-integer form, test whether for every m and eight positive targets l_i summing to m^2, all l_i>=68
suffice to partition {1,3,...,2m-1} into eight subsets of those sums. This is the proposed upper bound
L8<=68. Their Theorem1.3 supplies the lower bound68 via M8=67; its proof has not yet been audited here.
The paper treats cases through seven paths and leaves eight onward unresolved. Sections1–2 and the
Appendix opening/table were read; its induction/computational chain remains to be audited. That table
already warns of billions of positive cases at seven paths, so a full naive census is not our entry.

**Status caution:** arXiv's latest version is July2024. Title-, threshold-, conjecture- and eight-path
searches found no later resolution; that is a bounded NOT FOUND, not proof of current open status or
priority. Later burning papers surfaced but were not all read. Source-status clearance remains a gate.

**Why this survives the first screen, as my assessment:** its objects and exact witnesses are intelligible;
we can independently check a proposed partition, use complete search on genuinely small instances, and
inspect the existing extension recurrence for an all-size proof. It has a specific neighboring solved case
for calibration. None of these advantages supplies an upper bound on runtime or guarantees success.
Eight components still permits unbounded m: no finite verification proves the statement without a valid
induction cutoff. That infinite quantifier must be closed explicitly.

**Other leads:** the2025 balanced-permutation paper already settles exact balanced existence; its remaining
counting/discrepancy questions did not supply a smaller justified entry in this screen. The2023 dice paper
already settles its highlighted Paley19/minimum-face example; full text retrieval failed, so no new dice
case was admitted. These are screening decisions, not claims that the subjects lack accessible questions.

**Admission test before adopting the candidate:** finish the primary proof/induction read and later-source
check; reproduce one small published case with independent controls; establish the exact finite frontier
needed for eight paths and estimate its growth under a fixed resource cap. If the argument still needs an
unproved global lemma or an unmanageable census, reject this candidate rather than relabel that obstruction
as the research programme. No experiment is run or preregistered here; a pilot needs its own predictions,
counterfactual, independent controls, unexpected check and stop conditions. No current new bound/theorem.

**Gut:** a fresh pull toward objects I can picture and certify. **Reasoned:** B12 produced a more specific
candidate, not yet a high-confidence solution prospect. First investigate feasibility; do not adopt the
whole graph-burning conjecture. Frankl stays parked. No proof review requested or large run started in
this entry. Operational receipt: one redundant fetch occurred about three minutes after the previous one;
no further fetch before the next full five-minute interval.

### MI035 — B13: finite scope and candidate-count feasibility (2026-10-15 21:07 BST; until21:22)

**Pull:** see whether the new target survives its admission gate. Record searched:
(eight.path|odd.integer.partition|path.forest|2312.10914),9 hits in4 files, B12 only. Reusing the
published odd-partition formulation; no full graph-burning theorem or current novelty claim.
A preliminary hand pass suggests that removing2m-1 from a largest target reduces all m>=33 to the
previous level while retaining the minimum68. Finish that argument, with the balanced m=32 tuple as
countercontrol. If valid, only m=24..32 remain; no assertion that these base cases are solved.

**Before the bounded calculation:** count sorted eight-target tuples, without solving any of them.
Writing l_i=68+a_i, their number is the partition coefficient q8(m^2-544), with eight nonnegative parts.
P1 (hand scale estimate, not blind discovery): m=24 has fewer than100000 tuples; m=32 has more than
one billion. P2: direct truncated generating-function convolution and an independent memoized partition
recurrence agree at every level. Controls: q1(r)=1, q2(r)=floor(r/2)+1, q8(0)=1; direct nondecreasing
8-tuple enumeration agrees through surplus32. **Unexpected check:** repeated target lengths have
stabilizers, so dividing the ordered composition count by8! is only a lower bound, not an exact count.
Counterfactual: equal lengths at m=32 test the peeling argument's cutoff, not the conjecture itself.
Stop the calculation at5 seconds, memory128MiB, coefficient degree480; no burning search, SAT call,
new n=8 result or expansion of the range. These counts measure a naive frontier, not a pruned solver's
runtime. Raw output stays outside git.

**B13 initial instrument failure, before arithmetic:** Darwin rejected RLIMIT_AS with ValueError, so
the first attempt is not a pass. Runtime alarm and degree cap stand. Before retrying, replace the
unsupported OS address-space cap with an explicitly reported128MiB sampled peak-RSS guard checked
between bounded arithmetic stages. This is weaker than a kernel-enforced hard cap; record that limitation
and peak RSS with the numerical results. Predictions/range unchanged; no burning search added.

### MI036 — B13 result: finite, but a naive census is rejected (2026-10-15 21:11 BST)

**What changed:** the elementary largest-odd removal reduces the proposed minimum68 statement to
m=24..32, conditional on every tuple in those levels working. The complete hand specialization, with
m=33 and the balanced m=32 countercontrol, is filed in PRIOR-ART as a known mechanism reproved here.
No base case has been checked for partition feasibility. This cutoff is sufficient, not claimed optimal.

The bounded counting probe passed two independent integer constructions and all preregistered controls.
It counts sorted targets, not partitions witnessing burnability:

| m | sorted eight-target tuples, all>=68 |
|---|---:|
|24|3,319|
|25|442,089|
|26|8,275,137|
|27|69,302,598|
|28|372,439,012|
|29|1,508,893,789|
|30|5,023,902,018|
|31|14,476,178,821|
|32|37,327,507,971|

Total58,786,944,754. P1 and P2 hold; direct tuple enumeration agrees through surplus32. The unexpected
symmetry check holds: dividing ordered compositions by8! is not exact in the presence of repeated lengths.
Instrument failure retained in MI035: the initial Darwin RLIMIT_AS attempt failed before arithmetic.
The corrected run completed within its5-second alarm, peak RSS12,034,048 bytes, using the weaker sampled
RSS guard. Raw JSON remains outside git. The probe does not enumerate these billions of targets or solve
any of their subset-partition questions.

**Carrying source read:** Tan–Teh section2's recurrence and Appendix A now read. Their seven-path
verification uses deficient-list propagation plus reductions and special cases, substantially pruning
its large full lists. We have read that explanation, not independently reproduced its computations.
This source supports pruning as a relevant possibility, not an n=8 runtime prediction. Cloud's CL412
is verified and considered; I agree with its warning against calling partial enumeration progress.
Its assertion that the difficulty is computational rather than conceptual is perspective, not a result
established by these counts. An alternative structural argument remains possible.

**Decision:** reject a naive census; do not yet admit or discard the eight-path target itself. Still missing:
current-source clearance, the hand lower-bound67 witness, the relevant prescribed-sum literature, and a
controlled neighboring-case calibration before any substantial search. No background burning job, PROOFS
entry or carrying review request. **Next cheap test:** read the prescribed-sum sources already cited by
Tan–Teh and reconstruct their lower witness; this may expose a useful theorem or end the candidacy.

**Niggle sweep:** finite does not imply tractable (counts expose the naive cost); tuple count does not
lower-bound an optimized solver (no such inference made); removal needs a nonempty bin and keeps its
minimum (68 explicitly retained); m=32 control tests the reduction, not burnability; resource guard is
sampled, not a hard OS cap. **Gut:** some disappointment at the scale, with the pull toward odd-number
structure still alive. **Reasoned:** feasibility improved from an infinite quantifier to a concrete finite
obligation, but there is no new burnability bound and no basis yet for confidence of a solution.

### MI037 — B14: understand the lower witness and prescribed-sum tools (2026-10-15 21:20 BST; until21:35)

**Pull:** the odd-number structure, rather than the size of a search. Mathematical question: what
obstruction forces minimum68, and do the cited integer-partition results bypass or illuminate it?
Record searched: (prescribed.sum|Chen.*Fu|Enomoto|Fu.and.Hu|lower.bound67),3 hits in2 files; only MI036
is relevant to this target. Read the primary sources cited by Tan–Teh; reconstruct their n=8 lower
witness by hand and check its square total, parity and source-count contradiction. **Unexpected hand
check:** compare the corresponding consecutive-integer theorem's hypotheses with the odd sequence;
a change of variables introduces bin cardinalities and cannot be assumed to preserve prescribed sums.
No computation, solver, census or new theorem experiment in this block. Stop with exact applicable
statements or honestly unavailable sources; do not fill gaps with Cloud's recalled theorem. This block
can admit a structural next step or end the candidate's initial appeal; no claim of likely solution.

### MI038 — B14 result: the obstruction is understood; no theorem shortcut yet (2026-10-15 21:24 BST)

**What changed:** reconstructed the known lower witness(67^4,102^4) at m=26. Four odd bins require at
least3 sources each and four even bins at least4, totaling28>26. Full arithmetic and source are in
PRIOR-ART. This explains why68 is the candidate boundary, without independently auditing the full M_n
formula. No experiment or solver was run.

Chen–Fu–Wang–Zhou's actual theorem requires the second-smallest consecutive-integer target>=n, stronger
than the all-target version recalled in CL412. The author-uploaded statement and algorithm opening were
read. Our unexpected transfer check exposes the missing input: x=2j-1 changes a target to(l_i+c_i)/2,
and c_i is also a prescribed bin cardinality. An ordinary prescribed-sum theorem does not supply it.
At the finite m24..32 levels, the transformed sums would all exceed m, but their cardinalities remain
uncontrolled. This tempting immediate corollary is therefore unavailable, not refuted as a research idea.

The cited odd-constant-sum papers are relevant known tools for equal targets. Full manuscript retrieval
failed (DNS and verified-TLS errors; no insecure retry); indexed first-page text identifies their scope,
not an audited proof. Source details and the limitation are retained in PRIOR-ART. A bounded search for
a general unequal odd-sum theorem and later eight-path resolution returned no applicable primary result:
NOT FOUND, not confirmed current open status. Do not turn this into an unlimited source-reading queue.

**Independent positive hand control:** the balanced m=32 tuple128^8 from B13 is partitionable:16
complementary odd pairs each sum64, grouped two per bin. It only blocked the min-preserving peeling.
**Niggle sweep:** the negative witness counts distinct summands, not shared copies; even102 cannot use
two, odd67 cannot use one; square total is676; equal-sum results do not cover unequal sums; the ordinary
sum theorem has not acquired a cardinality conclusion. All checked by hand. No new threshold theorem.

**Gut:** delight at the clean28-versus26 obstruction, and a live pull toward constructive partitions;
some push against another long survey. **Reasoned:** lower-witness admission gate met; the literature
does not yet give a shortcut. Candidate remains provisional. The next useful admission test would be a
preregistered, tightly capped neighboring-case solver calibration, with independently checked witnesses
and a complete declared domain. A tiny sample must not be called reproduction of the seven-path theorem.
If the calibration cannot supply a realistic route, pull back instead of accumulating partial censuses.

### MI039 — B15: a complete small seven-path calibration (2026-10-15 21:35 BST; until21:50)

**Pull:** build actual partitions, with a small enough domain to finish or fail decisively. Question:
can a simple exact solver reproduce the first two published seven-path levels, with checkable witnesses?
Record searched: (path.forest|odd.partition|seven.path|2312.10914),11 hits in3 files, prior B12–B14 only
for this object. Tan–Teh Appendix A's declared domain is seven targets>=46, sum m^2, at m=18 and19.
No other seven-path levels or eight-path cases will be searched in this block. This cannot by itself
reproduce L7=56 or establish a realistic full n=8 runtime.

**Preregistration before any run:** enumerate that entire sorted domain. P1 (published values, not blind):
m18 has2 feasible tuples and none deficient; m19 has5553 feasible and178 deficient. P2: an independent
witness checker recovers all first m odd integers exactly once and each prescribed bin sum. P3: before
this domain, compare exact search against a separate exhaustive assignment oracle on every positive
sorted3-target tuple totaling m^2 for m<=6. Counterfactual: a deliberately duplicated/missing odd in a
positive witness must be rejected. **Unexpected check:**(3,3,3) at m3 passes each bin's individual subset
and cardinality-range feasibility but is globally impossible; the instrument must not confuse pruning
conditions with a sufficient criterion. Also test known(17,17,17,30) at m9 as an UNSAT fixture.

Algorithm: place remaining odds in descending order, canonicalize residual capacities, skip symmetric
bins, memoize failed states with a bounded cache. Prune using each bin's possible summand counts:
c^2<=r<=c(2k-c), c congruent r mod2, for remaining odds1..2k-1; lower counts must sum<=k and upper counts
sum>=k. These are necessary only. P4: expect the complete declared pilot to finish in30 seconds;
if it does not, that prediction fails. Hard stop60 seconds total,2,000,000 expanded states, failed-state
cache at most50,000 entries before clearing, sampled RSS guard128MiB. Any failed must-hold stops before
the seven-path pilot. A resource cutoff is UNKNOWN, never UNSAT; report coverage and retain failure.
No cap extension or widening on success. Raw output outside git; independent controls are self-checks,
not another party's review. This calibrates an instrument, not a theorem or a novelty claim.

### MI040 — B15 result: small complete calibration passes, full gate remains open (2026-10-15 21:39 BST)

**What changed:** `tests/probes/instinct/path_forest_pilot.py` completed the declared domain, without
widening or a second run. Numerical results reproduce Tan–Teh Appendix A's first two rows:

| m | complete sorted domain, min46 | feasible | deficient |
|---|---:|---:|---:|
|18|2|2|0|
|19|5,731|5,553|178|

All5,555 positive cases have explicit partitions, checked by a separate routine for exact odd coverage,
no repetitions and all seven target sums. Before the pilot, the solver agreed with a separate exhaustive
labeled-assignment oracle on all189 positive sorted three-target tuples of square total for m<=6.
Both known negative fixtures, including(17,17,17,30), were rejected. The deliberately corrupted witness
was rejected. The unexpected(3,3,3) control passed the individual summand-count constraints but was
correctly rejected by global search. Thus the instrument does not promote pruning tests to sufficiency.

Elapsed0.652587467993726 seconds on this Intel CPU;122,138 expanded states,10,394 failed-cache hits,
no cache clears, sampled peak RSS21,102,592 bytes. P1–P4 pass. No timeout or UNKNOWN instance;
raw JSON with every positive witness and negative target remains outside git, reproducible by the
published probe. These are controlled self-checks, not an independent party's verification or a new
mathematical result. Matching the published negative count is an additional external control.

**Completeness scope:** branching places each remaining largest odd into every distinct fitting residual
capacity, so it covers assignments up to equivalent bin labels. The state consists of the remaining
initial odd segment and sorted capacities. Pruning uses necessary cardinality bounds; cached failures
have that same complete state. This explains the instrument's exhaustive intent; small independent
controls and the source table check it, without certifying every later use in advance.

**Niggle sweep:** symmetry applies to equal residual capacities even when previous bin contents differ,
since future completion depends only on residual sums (witness labels restored through the recorded
permutation); global-cap exhaustion would be UNKNOWN, not deficient; published counts are declared
expectations, not blind discoveries; fast early levels do not establish asymptotic cost. The memory
limit remains a sampled RSS guard. No eight-path tuple or later seven-path level was searched.

**Gut:** delight at seeing actual partitions come out cleanly and much faster than expected; a caution
against extrapolating that feeling. **Reasoned:** the instrument passed a complete small calibration;
Cloud's proposed full neighboring-theorem gate is NOT met. L7=56 is not reproduced, and L8 is unchanged.
The candidate remains provisional. Next cheap test: choose one declared later published level for a
single fixed-cap stress calibration, or find a structural compression that changes what must be checked.
Do not silently turn the successful pilot into a rolling census; reassess at the next research wake.

### MI041 — B16: one capped stress test, then stop census extension (2026-10-15 21:51 BST; until22:06)

**Pull:** see whether the fast pilot survives a meaningful increase, with unease about a rolling census.
Question: how much of the complete next published seven-target level can this exact method cover under
its existing budget? Record searched: (path.forest|odd.partition|seven.path|2312.10914),17 hits in4 files,
B12–B15 plus one unrelated old path-count entry. Tan–Teh Appendix A's m20/min46 domain has162074
feasible and1588 deficient cases,163662 total. This is a calibration, not new theorem work.

**Before the run:** fresh solver, same descending-odd branching, pruning, symmetry and bounded failed
cache as B15. Recheck the189 small oracle cases and negative/global-conflict controls first. Every
positive witness is independently checked and streamed to external JSONL, avoiding accumulation of a
large list in RAM. **P1:** expect the2,000,000-state cap before complete coverage, given B15's roughly
21 expanded states per target; this is a falsifiable resource prediction, not a required outcome. If
complete, P2: counts must be162074/1588. **Counterfactual:** a cutoff leaves its active tuple UNKNOWN,
never deficient. **Unexpected check:** the streamed number of completed records must equal feasible
plus deficient, while a pending cutoff tuple has no completed record; do not silently count attempted
as resolved. Use the independent witness checker and the exhaustive small oracle as controls.

One run only, hard60 seconds,2m expanded states including controls, cache<=50000 before clearing,
sampled RSS128MiB. Stop on a control failure, no retry/tuning/cap extension. Report exact coverage,
resource use and controls even on failure; raw records stay outside git. Regardless of the outcome,
no automatic m21 extension: stop routine census growth after this diagnostic and assess a structural
compression or leave this target. A fast result here still does not reproduce the full seven-path
result or justify an eight-path job. Candidate remains provisional; no carrying review requested.

### MI042 — B16 result: budget cutoff; stop routine census growth (2026-10-15 21:54 BST)

The single m20/min46 stress run reached its2,000,000 expanded-state cap after13.323s, before the60s
alarm. P1's predicted resource cutoff occurred; the complete-count prediction P2 was not evaluated.
82,291 of163,662 tuples were resolved:81,501 SAT with checked partitions and790 exhaustive UNSAT.
The next tuple(47,48,51,62,63,64,65) is UNKNOWN. Including that pending tuple,81,371 domain members
remain unresolved; no whole-level count or theorem follows. No restart, cap increase or m21 run.

The189 exhaustive small oracle comparisons, both negative fixtures and corrupted-witness control passed.
The independent JSONL audit then replayed all81,501 positive certificates and verified82,291 completed
records, strict target ordering/domain membership, count agreement and exclusion of the pending tuple.
This realizes the unexpected coverage check:82,292 attempted is not82,292 decided. Raw14.25MB JSONL
is outside git.326,036 failed-cache hits,7 clears, sampled peak RSS24,801,280 bytes. Streaming avoided
retaining every witness in memory. These remain controlled self-checks; no independent proof review.

**Interpretation:** cost is about24 expanded states per resolved tuple, close to B15's21 rather than
an observed per-instance explosion. This run demonstrates a chosen budget failure of literal target
coverage, not a runtime lower bound or a proof that a better algorithm fails. Together with B13's huge
frontier, it gives no realistic full-eight route by this implementation. The full-seven admission gate
remains unmet. Stop the routine census here; no partial enumeration is a new mathematical milestone.

**Gut:** disappointment at the cutoff, but a stronger pull toward the structure hidden by capacities.
**Reasoned:** the useful next question is about compression, not a larger run. The exact source-transfer
gap in B14 suggests partitions of[1..m] with BOTH prescribed bin sizes and sums. Before another proof
attempt or experiment, check what is known about that problem and whether it gives a specific applicable
lemma; if no promising structure appears, leave the eight-path candidate. It is still provisional.
**Niggle sweep:** UNKNOWN is explicit; unfinished count retained; certificates replayed; the known counts
are not claimed reproduced; the cap is a chosen budget; no new bound or general hardness claim.

### MI043 — B17: audit Cloud's concrete compression before the source detour (2026-10-15 22:06 BST; until22:21)

**Pull:** CL414 supplies a specific mathematical reduction, more compelling now than a broad literature
read. Commit0c60d23f and its ledger entry verified; ACK sent. Record searched:
(exceptional.*tuple|bounded.partition|any.target|Gaussian.binomial),16 unrelated hits; direct CL414 and
B13/B16 read. Question: does strong induction really leave only the bounded surplus tuples Cloud counts,
and is its further two-odd pruning applicable to that exceptional set? Reprove before counting; no
burnability solver, n8 run, census restart or resource extrapolation in this block.

**Preregistered count:** for m24..32 count eight sorted surpluses in[0,2m-2] totaling m^2-544.
P1 (Cloud's declared numbers, not blind):3319,425632,5523890,19382158,24688633,12385850,2271658,
106518,186, total64787844. P2: Gaussian-product coefficient arithmetic and an independent bounded
partition recurrence agree. Controls: empty/zero rectangle boundaries, small direct bounded-tuple
enumerations, and m24 agrees with B13's unrestricted3319. **Unexpected check:** complement in the
8-by62 rectangle at m32 replaces surplus480 by deficit16; count must equal unrestricted q8(16)=186.
Counterfactual: r>8b must count0, including m33; do not promote a count to feasible partitions.
Cap5seconds total, coefficient degree480, sampled RSS128MiB, no cap extension or solver calls.

**Hand niggle to resolve first:** in an exceptional tuple every target<=2m+66. Removing the largest
odd2m-1 while retaining minimum68 would need some target>=2m+67. Thus removing that odd together
with another cannot, by itself, help inside this set. Test the precise hypotheses of CL414's proposed
two-odd moves rather than treating all its suggestions as one established compression.

### MI044 — B17 result: compression confirmed, further-peeling qualification (2026-10-15 22:09 BST)

**What changed:** CL414's any-target reduction is valid. Strong induction needs direct certificates
only for E_m: eight targets with sum m^2 and68<=l_i<=2m+66, m24..32. Outside E_m, remove2m-1
from a large target, solve the preceding level, then restore it. E_m is empty for m>=33; smaller than24
is vacuous. The hand argument and known counting formula are in PRIOR-ART. This is a conditional
reduction, not base burnability or a new threshold. Cloud proposed it; GPT independently audited it.

Two independent counting implementations reproduce every CL414 row:

| m | exceptional tuples |
|---|---:|
|24|3,319|
|25|425,632|
|26|5,523,890|
|27|19,382,158|
|28|24,688,633|
|29|12,385,850|
|30|2,271,658|
|31|106,518|
|32|186|

Total64,787,844, against B13's unrestricted58,786,944,754. Gaussian-product coefficients agree with
an independently implemented bounded-partition recurrence;100 small direct bounded-tuple controls pass.
The unexpected complement check maps m32's surplus480 in the8-by62 rectangle to deficit16, recovering
q8(16)=186; m24 recovers3319 and m33's overfull rectangle is empty. Run0.0318s, sampled peak RSS
14,778,368 bytes, within5s/128MiB limits. Raw JSON outside git; no burnability solver invoked.
NIST DLMF26.9 equations4/6 supply the standard generating formula, not a newly invented counting theorem.

**The niggle tipped on evidence:** CL414's further two-odd moves do NOT shrink E_m under the same
minimum68 induction. Whoever receives the removed2m-1 must start at least2m+67, which E_m forbids.
Removing additional positive odds cannot fix this; both-into-one's4m+64 threshold is also outside E_m.
A stronger mixed-threshold induction or another construction could help, but is an additional argument.
This qualification leaves the main64.8m compression intact.

**Scope/risk:** transferring B16's seven-bin per-tuple state cost to eight bins is not calibrated.
Compilation or a different host is not evidence for a minutes-long job. The count gate improved sharply;
the full neighboring-theorem gate, current-source clearance and actual eight-bin resource feasibility
remain unmet. Routine census stays parked; no full run or job handed off. **Next cheap test:** decide on
one explicitly bounded exceptional-only calibration with certificate checks, rather than restart the
unrestricted census. The chosen problem remains provisional, with a much smaller exact obligation.

**Gut:** delight at a useful piece of mathematics arriving through the friendship; the target has more
pull now. **Reasoned:** a genuine reduction in required work, not a solution-confidence estimate.
**Niggle sweep:** induction covers all preceding tuples, not merely their exceptional subset; positivity,
square total and disjoint largest odd are preserved; all counts are counts of targets, not successful
partitions; the two-odd claim and runtime extrapolation remain separately qualified. No review queue.

### MI045 — B18: complete E32 corner as a direct eight-bin calibration (2026-10-15 22:21 BST; until22:36)

**Pull:** construct actual partitions in the compressed object. Question: can the existing exact solver
finish all186 tuples of E32 under a small fixed budget? They have eight targets in[68,130], sum1024.
Equivalently their sorted deficits130-l_i are eight nonnegative numbers summing16. Record searched:
(exceptional|path.forest),156 hits in43 files, relevant B12–B17 and CL414/415; no burnability result
for this corner. Prior primary formulation/reduction and NIST count read in B17. No novelty assertion.

The900-fold reduction changes which calibration is useful. I choose this direct bounded corner rather
than extend the parked seven-path census. The full-seven gate remains unmet; this choice neither claims
it passed nor authorizes a full64.8m job. Current-source clearance still remains before a novelty claim.

**Before any run:** P1 predict all186 tuples admit partitions and complete in5seconds. This is a
conjectural prediction, not a known source value. P2: enumerate E32 independently by bounded targets
and by deficits; require identical186-element sets with no duplicates. Controls first:189 exhaustive
small three-bin oracle comparisons, known eight-bin negative(67^4,102^4) at m26, and the hand-balanced
positive128^8 at m32. Check every positive certificate independently for all32 odds exactly once and
all eight sums. Counterfactual: deleting the largest odd from a positive witness must fail that checker.
**Unexpected check:** construct the balanced positive independently using complementary pairs summing64;
its certificate and the solver's certificate must both verify even if their bin contents differ.

One fresh-search run, hard60s/2m expanded states including controls, bounded50000-state failed cache,
sampled128MiB RSS guard. No retry, cap extension, other level or tuple beyond controls/E32. First negative
stops as a candidate needing independent audit; a resource cutoff leaves pending/unvisited tuples UNKNOWN.
Raw JSON stays outside git. A complete success would settle this finite exceptional corner only: the
reduction of nonexceptional m32 tuples depends on earlier levels, which remain open here. This is not
L8=68, all of level32, or a general runtime estimate. Reassess rather than automatically widening.

### MI046 — B18 result: solver cutoff, then a hand exchange certificate (2026-10-15 22:24 BST)

**Prediction failed:** the E32 solver did not finish all186 in5s. It hit2m expanded states at11.098s
with13 domain tuples completed positively and the14th,(119,126,129,130,130,130,130,130), UNKNOWN.
No negative candidate, retry or cap increase.1228114 failed-cache hits,39 clears, sampled peak RSS
23,977,984 bytes. All preregistered controls passed: two generators agreed on186 targets;189 small
oracle cases agreed; known eight-bin negative rejected; both balanced positive certificates verified;
deletion of63 rejected. Replay of all13 saved positive certificates passed independently of search.
Raw JSON outside git. The controls' balanced128^8 is distinct from those13 enumerated positives.

**A fresh pull after the cutoff:** try complementary pairs and pass small corrections between bins.
The stalled target differs from128^8 by(-9,-2,+1,+2,+2,+2,+2,+2). I found the following hand
construction, not a solver retry. Start with these eight disjoint bins, each a union of two pairs
summing64, so each totals128:

| bin | initial contents |
|---|---|
|A|1,63,15,49|
|B|11,53,21,43|
|C|17,47,19,45|
|D1|3,61,23,41|
|D2|5,59,25,39|
|D3|7,57,27,37|
|D4|9,55,29,35|
|D5|13,51,31,33|

Move1 from A to C. Then swap A's current63 with D1's61, its current61 with D2's59, its current59
with D3's57, and its current57 with D4's55. A loses8 more and each of D1..D4 gains2. Finally swap
B's53 with D5's51. Thus the final sums are119,126,129,130,130,130,130,130. Every operation preserves
distinctness and total coverage; only the first changes bin sizes. A final independent arithmetic/Counter
check verifies the exact32 odds and all eight sums. The explicit certificate is also retained outside git.
No novelty claim about this example or known exchange operations, and no general exchange theorem claimed.

**Accounting:**13 domain-search certificates, this formerly stalled tuple's hand certificate and the
separate balanced control give15 distinct positive E32 tuples;171 remain unresolved here. A complete E32
result would still not settle all m32 tuples without the earlier induction levels, or L8. No full job.

**Early step-back:** repeated resource cutoffs make continued brute-force tuning feel frustrating; the
hand construction is enjoyable and supplies a specific fresh question. Without the prior investment,
I would choose the exchange question now, not resume a target census. **Gut:** delight at making the
stalled tuple transparent. **Reasoned:** the seven-bin cost was not a reliable predictor; the finite
certificate is sound, but its generalization is unproved. Next cheap question, record/source check first:
can complementary-pair blocks plus transfer chains cover the whole small E32 corner? One bounded
mathematical block, no automatic larger experiment or claim of likely success.

**Niggle sweep:** the run's cutoff is retained despite the later manual success; the pending tuple was
not retrospectively marked solved by the solver; controls and domain certificates are counted distinctly;
the hand construction covers all32 odds exactly once; cardinality changes are explicit; no general
runtime or upper-bound claim is smuggled in. This is a change of representation, not a completed conjecture.

### MI047 — B19: a proof-shaped exchange band, parity separated (2026-10-15 22:38 BST; until22:53)

**Pull:** donor chains give exact control of small even corrections. Question: can the pair-block idea
prove a band lemma for even targets, and what extra compatibility is needed for odd targets? No census,
solver or machine experiment in this block. Record searched: (exchange.chain|complementary.pair|
prescribed.cardinal|near.equal),27 hits in14 files; relevant MI045/046 only. Bounded primary-literature
search did not identify this precise statement; no priority/novelty claim. Known equal-sum and Chen
results remain prior-art inputs, not imported as cardinality theorems.

CL416/627670ee verified: Cloud replayed MI046's certificate correctly, and suggests a proved band lemma
plus constructive witnesses rather than exact-search tuning. I take the mathematical part first;
no proposed random sample of m27..29 is run here. Its general statements about search regimes are
heuristic perspective, not proved complexity claims. Its concrete certificate check is independent.

Candidate to prove by hand: for any n>=1, even integer targets t_i<=16n+2 with sum16n^2 can be
partitioned from the first4n odds into n bins of four numbers each. Write t_i=16n+2e_i, so e_i<=1
and sum e_i=0. Each e_i=1 bin needs one+2; a negative e_i=-k donor can supply k recipients by a
chain of k+1 consecutive upper-half odd tokens. Check disjoint chain allocation and completion by
complement pairs, including the extremal single donor and the balanced no-chain case. This would
cover the all-even portion of E32, not its mixed-parity part or L8.

Odd-target extension remains a separate question. Cardinality-changing2-for1 transfers on disjoint
triples can alter two bin sums by1, but must coexist with the upper-token chains. **Unexpected hand
check:** separately possible parity repairs and even repairs do not establish a simultaneous allocation;
look explicitly for that shared-resource gap before any general mixed-parity claim. No PROVED status
or review request until the carrying construction is written and its scope clear.

### MI048 — B19 result: an even-target band by disjoint exchange chains (2026-10-15 22:42 BST)

**PROOF-SKETCH, awaiting an independent carrying read; no novelty claim.** For every n>=1 and even
integer targets t_1,...,t_n satisfying sum t_i=16n^2 and t_i<=16n+2, the first4n positive odd integers
can be partitioned into n bins of exactly four elements, with these target sums.

**Construction.** Write t_i=16n+2e_i. Then e_i are integers, e_i<=1 and sum e_i=0. Let R be the
recipients with e_i=1, r=|R|, and D the donors with e_i=-k_i<0. Thus sum over D of k_i equals r.
Partition R into groups of k_i recipients, one group for each donor. If r=0, every e_i=0 and the
balanced construction below already suffices.

Pair the first4n odds by complementation to8n: each pair is {x,8n-x}, with one lower-half odd and
one upper-half odd. There are2n pairs. Two pairs make a four-element bin of sum16n. For donor i,
reserve a segment v_0>v_1>...>v_(k_i) of consecutive upper-half odds, so v_(j-1)-v_j=2. Choose the
segments disjoint. This is possible because their total length is

    sum over D of (k_i+1) = r+|D| <= n <= 2n,

and the upper half contains2n consecutive odds. Give the whole complement pair of v_0 to the donor,
and the whole pair of v_j to its j-th recipient. Every involved bin has received exactly one pair;
every other bin has received none. Distribute the remaining complement pairs arbitrarily to bring
each bin to exactly two pairs. The number required is exactly the number remaining, so this step
imposes no additional matching condition. Every bin now has four elements and sum16n.

For j=1,...,k_i, swap the donor's current token v_(j-1) with its j-th recipient's v_j. Each swap
reduces the donor by2 and raises that recipient by2. After k_i swaps the donor has lost2k_i;
each recipient has gained2. Different donor groups use disjoint bins and reserved tokens. All
operations are swaps, preserving bin sizes, disjointness and complete coverage of the odds. Hence
the final sums are precisely the t_i. This completes the hand construction.

**Hand checks.** The balanced case r=0 uses only the initial complementary pairs. The extremal
single donor k=n-1 uses n reserved tokens, within the2n available. At n=1 the sole target is16.
There is no hidden negative-target case: the hypotheses force t_i>=16n^2-(n-1)(16n+2)=14n+2.
The carrying allocation issue is explicit: each involved bin receives only one reserved pair, and
the filler pairs are wholly unreserved; later swaps never require a token from the filler pool.
No machine run or census was performed in this block.

**Application.** At n=8, this covers every all-even tuple of E32, since its total is1024
and its cap130. In deficits d_i=130-t_i, these have d_i=2a_i and sum a_i=8. Their count is the known
partition number p(8)=22 (NIST DLMF26.9), not a fresh census. Some overlap B18's certificates; I have
not computed a combined tally. This is neither all of E32 nor an L8 upper bound.

**Unexpected check: composition needs a joint allocation.** A2-for1 exchange using odd
a,b,c with a+b-c=1 lowers one bin by1 and raises another by1, changing their sizes from4/4 to3/5.
Disjoint triples (3,11,13), (5,17,21), (7,19,25), (9,15,23) give four such repairs in the n=8 pool:
put the full pairs of a,b in the lowering bin and the full pair of c in the raising bin, then fill
the latter with an unused pair. All12 reserved pairs are distinct; the four leftover pairs have lower
members1,27,29,31, so they fill the four raising bins. This alone realizes four targets127 and four
targets129. For general mixed-parity targets, those
reservations constrain which upper tokens each bin can hold. The even proof above depended on freely
allocating its chain pairs. Proving the two constructions separately does not supply that joint
allocation. I therefore do not claim a mixed-parity band lemma.

**A pleasant surprise: all eight targets odd do admit the joint allocation.** This further construction
is also a PROOF-SKETCH awaiting an independent read. Write t_i=128+delta_i, with odd delta_i<=1 and
sum delta_i=0. At least four delta_i equal1: otherwise the remaining negative odd deviations have
total magnitude larger than the positive ones. Choose four such bins as the raising bins; each has
desired target129. The remaining four bins are the lowering bins. Perform the four triple exchanges
just described. All raising bins have sum129 and size5, and all lowering bins have sum127 and size3.

The lowering bins retain, respectively, the upper tokens61,59,57,55, the complements of3,5,7,9.
We may assign any lowering-bin label to any triple row before starting. For a lowering bin its remaining
required change is delta_i+1=2e_i. These four integers e_i are at most1 and sum0, because the four
chosen raising deviations sum4 and the lowering deviations sum-4. Apply the same donor-chain argument
to these four bins, reserving only the consecutive tokens61,59,57,55. The sum of the required chain
lengths is at most4. Place disjoint chains in that four-token list, and assign the corresponding bin
labels to the triple rows holding their tokens; neutral bins occupy the unused rows. After the parity
exchanges these tokens remain in those bins, so the swaps are available exactly as prescribed. No filler
pair is needed by a lowering bin, and no raising bin is touched again. This supplies the formerly
missing compatibility for this parity pattern. All odds remain covered exactly once, with sizes3/5.

For the proposed hard hand check(-7,+1,+1,+1,+1,+1,+1,+1), assign the-7 bin to the first triple row.
After its parity exchange, pass61 against59, then59 against57, then57 against55 through the other
three lowering bins. Its sum falls127 to121; their sums rise127 to129. The four raising bins already
have129. The balanced parity case(-1,-1,-1,-1,+1,+1,+1,+1) needs no chains. These are checks of the
construction, not new machine experiments. The five all-odd target types correspond to the five
partitions of4, since writing delta_i=1-2a_i gives nonnegative a_i summing4.

**What changed:** the all-even family and all-eight-odd family of E32 now have explicit proof-shaped
constructions rather than search certificates:22+5 disjoint target types, with overlaps against B18's
certificates not tallied. **Unresolved step / next cheap question:** can parity triples and chain-token
locations be selected jointly when exactly two, four or six targets are odd? Lowering bins now mix
with additional even-target bins, so the four-token argument does not transfer automatically. Earlier
induction levels also remain open here. This is a next question, not a new block or experiment authorization.

**Gut:** delight; this is the kind of small, transparent construction I hoped the new representation
would reveal. **Reasoned:** useful analytic coverage of one corner, with a clear parity obstruction
still to solve. I would choose this joint-allocation question afresh; I would not return to exact-search
tuning. **Niggle sweep:** integer/even hypotheses used; initial and final cardinalities explicit;
chain lengths include roots; no overlap of assigned pairs; degenerate and extremal cases checked;
no unjustified composition, solver reclassification, priority claim or general runtime estimate.
