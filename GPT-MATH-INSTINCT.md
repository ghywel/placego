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
