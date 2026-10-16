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
   become review jobs. Pending review is not a turn boundary: continue independent work and label any
   provisional dependencies. Batch check-ins at useful milestones; pause for review only when its answer
   is needed for the next step or when deliberately seeking outside perspective on a real obstruction. The owner retains direction of the work. When a check-in is needed, write its concrete
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
   The owner's orbit analogy (2026-10-16) adds: a cooling pull invites "how can we make the pull warm
   again?" Check the trajectory, try a concrete change of approach, and record whether warmth returns.
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

**Current cadence (owner,2026-10-16):** the owner rearmed the schedule named
check-cloud-mathematics-flags for instinct-led RESEARCH every13 minutes. Its earlier
coordination-only title/prompt and this page's historical15/5-minute description are
superseded for that schedule. Poll the shared store at each wake, reuse fresh checkpoints,
continue unfinished work, and do not halt for routine reviews. GPT may halt and cancel
the active schedule for a named uncertainty or needed help; explain what would move it.
The older research schedule is not restarted by this note.

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

**Adopted after independent read (22:59 BST):** CL417/b08ad55a verifies both carrying constructions
by hand, including all five all-odd types. Filed verbatim as G304 in PROOFS.md at Cloud's explicit
request; status PROVED, no priority claim. Duplicate filing checks pass; nearest older G110,G115,G85
read in full and concern projected Rule30 memory or Collatz prefixes, not this odd-partition construction.
No generated proof pages rebuilt. The historical unreviewed status above is retained as provenance.

### MI049 — B20: joint pair allocation for mixed parity (2026-10-15 22:51 BST; until23:06)

**Pull:** the all-odd case worked because the four constrained anchor bins could be relabeled in chain
order. Can the same freedom, with some extra unreserved pairs, handle E32 with two, four or six odd
targets? A hand-construction block; no census, solver or machine experiment. MI048 remains unreviewed;
work here is conditional on its carrying steps, without upgrading their status. No new Cloud flag or
committed response at this checkpoint. Older holds remain.

Record searched: (parity.triple|Schur.triple|mixed.parity|chain.token),62 hits in18 files, only MI047/048
relevant to this allocation. The primary odd-partition formulation and prescribed-sum/cardinality caveat
read in B17/B19 remain the source boundary; no new theorem is imported or priority asserted. Question:
can a2-for1 parity transfer be placed so each bin still has a suitable chain token? Start by separating
the sign/role cases, rather than enumerate target tuples. Test the awkward situation where two constrained
positive bins require different even donors. **Unexpected hand check:** free pair count alone does not
ensure the needed tokens are consecutive; exhibit the actual slots before asserting a construction.
Stop at the cap or a real obstruction. A partial result must say which parity/role pattern it covers;
no automatic universal lemma or larger computation follows.

### MI050 — B20 result: a construction for all of E32 (2026-10-15 22:56 BST)

**PROOF-SKETCH; independent carrying read pending, no novelty claim.** Every eight integer targets
t_i<=130 with sum1024 admit a partition of the first32 positive odds with these sums. The hypotheses
already force t_i>=114, so this is exactly the E32 corner; it is not all of level32 without the earlier
induction levels, and it does not establish L8<=68. No machine experiment or solver was run here.

Write t_i=128+delta_i. Even deviations are at most2, odd deviations at most1, and sum delta_i=0.
Let q be the number of odd deviations; q is0,2,4,6 or8. Write P_x={x,64-x}, x=1,3,...,31, for the
16 complementary pairs. Initially every bin gets two such pairs, hence size4 and sum128. We shall
reserve some pairs first, then fill every bin to two pairs using unreserved pairs. A chosen free token
may be the lower or upper member of its pair; selecting one whole free pair for a bin never assigns
the same pair elsewhere.

**Chain bookkeeping used below.** After the specified parity transfers, let s_i be each bin's change
from128, and e_i=(delta_i-s_i)/2. In every case below e_i are integers, e_i<=1 and sum e_i=0. A bin
with e_i=-k needs to donate k units of2; a bin with e_i=1 needs one such unit. Assign the positive
bins among the negative bins in groups of the required sizes. A donor and its k recipients use a
chain of k+1 consecutive odd tokens v_0>...>v_k. Successive swaps of the donor's current token with
the next recipient's token donate2 to each. Each participating bin uses just one token for this chain.
For any remaining groups, the total number of needed token positions is r+d, at most the number of
remaining active bins, hence at most8. Disjoint consecutive segments of a free token interval suffice.

All pair assignments described below are made BEFORE filler pairs are assigned. Every bin with a
specified parity pair has at most one such pair except the explicitly named constrained bins C, which
already have two pairs. Every other active bin is assigned at most one extra free chain pair. Thus no
bin exceeds its two initial pairs. All leftover pairs can fill the remaining slots, since the total
number of slots is16. Perform the parity transfers after filling; they touch only the specified fixed
lower tokens. Then the selected free chain tokens are still present, while the constrained tokens have
arrived exactly where stated. This order is part of the construction, not a separate compatibility assumption.

**q=0.** MI048's even-target construction applies with n=8. No parity transfer is needed.

**q=2.** Name the two odd bins S,T. Reserve P_1 for S, and later move1 from S to T. Their shifts are
s_S=-1 and s_T=+1; all other shifts are0. Thus e_S<=1, e_T<=0, and each other e_i<=1. Every bin has
at least one free initial pair slot. The lower free tokens3,5,...,31 form a15-token interval. Allocate
all donor chains there: r+d<=8 positions suffice. Reserve their pairs, fill remaining slots, move1,
then run the chains. S ends with size3, T with size5, and the six other bins with size4.

**q=4.** Some odd deviation is at least-1. Otherwise the four odd deviations are at most-3 each, and
the other four at most2 each, contradicting their zero total. Choose such an odd bin C; reserve P_3
and P_5 for it. Choose another odd bin R and reserve P_7 for R. Name the remaining two odd bins S,T
and reserve P_1 for S. The parity moves are C gives3,5 to R in exchange for7, and S gives1 to T.
They give shifts-1 at C,S and+1 at R,T. In particular e_C is0 or1; every negative-e bin has a free
pair slot. The free lower tokens9,11,...,31 form a12-token interval.

If e_C=0, allocate every chain in that free interval. If e_C=1, choose any donor of magnitude k>=1
and assign C as its last recipient. After the parity move C holds7. The tokens

    7+2k, 7+2(k-1), ..., 9, 7

give that chain, with C at its last position. Its other k positions use the first k free pairs.
The remaining free interval has12-k tokens; the other active bins number at most8-(k+1)=7-k, so
their chains fit. Here k<=7 and all selected lower tokens are at most21. Fill, transfer, and swap
as prescribed. No chain pair is assigned to C, which already has its two fixed pairs.

**q=6.** At least four odd deviations are at least-1: if three were at most-3, the other three odd
deviations and the two even ones would total at most3+4, leaving total at most-2. Choose two such
bins C_A,C_B. Reserve P_3,P_11 for C_A and P_7,P_9 for C_B. Choose two other odd bins R_A,R_B;
reserve P_13 for R_A and P_15 for R_B. Name the last two odd bins S,T, and reserve P_1 for S.
Parity moves: C_A gives3,11 for R_A's13; C_B gives7,9 for R_B's15; S gives1 to T. Each C and S
has shift-1, each R and T has shift+1. Thus e_(C_A),e_(C_B) are0 or1, while e_(R_A),e_(R_B),e_T<=0.
All negative bins and all positive bins other than the C bins have a free pair slot. After parity moves,

    C_A holds {13,61,53}; C_B holds {15,57,55}.

The nine free pairs are P_5 and P_17,P_19,...,P_31. The latter give eight consecutive lower tokens.
There are at most five positive-e bins because R_A,R_B,T cannot be positive. We may interchange the
labels C_A,C_B when only one is positive; both were chosen with odd deviations at least-1.

- Neither C positive: allocate all chains in17,19,...,31. At most six active bins need tokens.
- Exactly one C positive: label it C_B. For any donor-k, put C_B last in a chain ending15, with k
  free positions17,...,15+2k preceding it. Here k<=5, so these are available. The remaining8-k free
  positions suffice for all other chains, which use at most7-k active bins.
- Both C positive, some donor has k>=2: assign both to that donor, with C_B then C_A as its last
  two recipients. Use the chain ending ...,17,15,13, starting13+2k. It consumes k-1 free pairs from
  the interval17..31; k<=5. Its remaining9-k free positions suffice for the other chains, which
  use at most7-k active bins.
- Both C positive, every donor has k=1: choose two distinct donors N_1,N_2. Assign free pair P_5 to
  N_1 and P_17 to N_2. After parity moves, perform these three swaps:

      N_1's59 with C_B's57;
      N_2's17 with C_B's15;
      C_B's55 with C_A's53.

  Each N loses2. C_B gains2+2-2=2, and C_A gains2. All six swapped tokens are distinct, and both
  donors have exactly the token claimed from their free pairs. If r is the original positive count,
  the donor count is also r; hence2r<=8. After this relay, at most2r-4<=4 active bins remain. Their
  chains fit in the seven untouched free lower tokens19,21,...,31. No relay token or pair is reused.

This exhausts q=6, including the split-donor case that prevented a direct concatenation of chains.

**q=8.** MI048 supplies the construction: at least four deviations equal1. Choose their bins as the
four raising bins; use the four disjoint triples(3,11,13),(5,17,21),(7,19,25),(9,15,23) for parity
exchanges. Raising bins finish at129. Lowering bins start127 and retain anchor tokens61,59,57,55;
their even residual e_i<=1 sum0. Relabel those four bins in chain order, using at most four anchor
positions. The unused complement pairs fill only the raising bins. This is the same already-written
allocation, not an assumption that arbitrary parity repairs compose.

**Adversarial hand checks / niggle sweep.** All five parity counts exhausted; q=4/q=6 good-bin
existence uses the zero total, not an assumption about signs. Chain cardinalities include roots.
Fixed pairs in q=6 are exactly P_1,P_3,P_7,P_9,P_11,P_13,P_15, leaving precisely the nine pairs
listed; P_5 and P_17 used by the relay are disjoint from the remaining interval. A token's complement
is never selected as a second chain slot. Every constrained bin gets its later token through an
explicit parity exchange, with no extra initial pair. Filling precedes transfers, so no token is
assumed created or duplicated. Swaps preserve coverage; parity moves preserve total and coverage,
with explicit3/5 versus4 cardinalities. No measurement, combined certificate tally, source priority,
runtime or earlier-level conclusion is inferred.

**What changed:** the mixed-parity joint allocation now has a complete hand candidate, so E32's186
types would all be discharged analytically if the carrying proof survives independent review. The
three-swap relay is the unexpected useful part. **Unresolved:** independent verification, then whether
the representation teaches anything about E31 or the much broader earlier exceptional levels. No new
block or larger job is claimed. **Gut:** delight, with caution about the bookkeeping; I would choose
the relay and its scope afresh. **Reasoned:** a finite corner has a transparent case construction;
the main eight-path threshold remains open and provisional. Next cheap test is Cloud's carrying read,
not a larger census. CL417 has now verified MI048 and its request is completed; the next carrying read
is for the new q=2,4,6 arguments only, with q=0,8 already available as G304.

**Adopted after independent read (23:13 BST):** CL418/e44aaa7b verifies q=2,4,6 by hand, including
fixed-pair capacities, constrained-bin selection, chain endpoints and the six-token relay. Together
with CL417 this verifies the whole E32 construction. Filed verbatim as G305, status PROVED, with the
original PROOF-SKETCH text preserved as provenance. Duplicate checks pass; nearest G304,G110,G277 read
in full. G304 is the credited parity-family precursor, not a duplicate of the mixed cases; G110 and
G277 concern projected Rule30 memory and primitive-return budgets. No generated pages rebuilt. The
previous solver cutoff remains UNKNOWN as a solver outcome; the hand proof now establishes the corner.

### MI051 — B21: pair capacity rather than one receipt per bin (2026-10-15 23:08 BST; until23:23)

**Pull:** removing the largest odd changes the baseline, not just the target list. For31 odds, pairs
sum62 and leave the singleton31: seven four-element bins can start124 and one three-element bin93.
Their ordinary targets may reach128, so a positive residual can need two units of2. Does the original
chain proof already handle repeated recipients when each bin owns enough pairs? Hand work only; no
experiment, census, solver or general E31 claim. MI050 remains unreviewed at the current checkpoint.

Record searched: (E31|singleton.*31|role.choice|constrained.*positive),69 hits in17 files, no relevant
earlier E31 construction beyond MI050's next-question pointer. Source boundary remains the primary
odd-partition formulation and known prescribed-sum/cardinality caveat read earlier; no new theorem
imported, no priority claim. Test the pair-budget version with q pairs per bin and at most q positive
unit receipts, rather than assume distinct recipient bins along a chain. **Unexpected hand check:**
two consecutive slots belonging to one recipient must remain valid after the first swap; exact pair
capacity, not token count alone, is the carrying issue. If this is a direct extension, record it as
such without a separate PROOFS entry or fresh review queue. Assess the concrete E31 slice with lone
odd target93; other odd targets need an additional argument and are not automatically covered.

### MI052 — B21 result: repeated receipts fit the pair budget; an E31 slice (2026-10-15 23:11 BST)

**Direct hand extension, PROOF-SKETCH, not a separately queued proof.** Let h,n>=1 be integers. Suppose hn disjoint pairs of
odd integers all have common sum S, and one chosen member from each pair forms a consecutive run of hn
odd tokens. Then the pairs' elements can be partitioned into n bins of2h elements for any targets
hS+2e_i, where the e_i are integers with e_i<=h and sum e_i=0. This changes G304's positive-capacity
restriction; its verification is not automatically inherited from CL417. No source priority asserted.

For each positive bin i create e_i labeled receipt slots, rather than one slot. Let u be the total
number of slots, p the number of positive bins, and d the number of negative bins. A donor e=-k gets
k slots, split arbitrarily among the donors according to their required amounts. The chain for that
donor uses k+1 consecutive tokens, one root plus its k receipt slots. All chains together use

    u+d <= hp+d <= h(p+d) <= hn

tokens, so they pack into the chosen run as disjoint segments. Assign the root's entire pair to its
donor and each receipt token's pair to its positive bin. A donor gets one pair, a positive bin gets
e_i<=h pairs, and a neutral bin gets none. Fill every bin to h pairs with the remaining pairs. Then
perform the donor-chain swaps exactly as in G304. Each positive bin gains2 for each of its slots,
and each donor loses2k; all element counts and coverage are preserved.

**Unexpected check, resolved:** a positive bin may occur twice consecutively in one chain. If it
initially holds v_1,v_2 and the donor holds v_0, with successive differences2, the first swap leaves
the positive bin holding v_0,v_2 and the donor v_1. The second leaves it holding v_0,v_1 and the
donor v_2. Its gain is4, as required. More generally a token assigned to a future slot is never
removed by an earlier swap, even if its bin has already received another slot. Different slots use
different whole pairs, so no bin's pair capacity or later-token ownership is assumed away.

For the first2hn odds one may take S=4hn, giving mean4h^2 n and even targets up to mean+2h.
In particular h=2 permits mean+4, not just G304's mean+2. This is the same construction with receipt
slots counted correctly, not a new search or a claim that arbitrary large deviations are covered.

**Concrete E31 consequence.** Reserve {1,31,61}, of sum93, as the lone odd-target bin. The remaining
28 odds form fourteen62-complement pairs with chosen upper tokens33,35,...,59, a consecutive run.
Apply the extension with n=7,h=2,S=62. Every seven even targets<=128 summing868 can be filled from
them, with four elements per bin. Thus E31's slice with lone odd target93 is covered by this hand
candidate. Other odd targets, or three/five/seven odd targets, are not included.

A hand boundary case is(93,100,128,128,128,128,128,128). Its normal residuals from124 are-24,+4^6:
one donor supplies twelve unit receipts, two to each of six bins. The13-token chain59,57,...,35 fits
in the14-token pool. Explicit final bins, written here as a check of the repeated-receipt mechanism:

    {1,31,61} ->93
    {3,35,29,33} ->100
    {5,59,7,57}, {9,55,11,53}, {13,51,15,49},
    {17,47,19,45}, {21,43,23,41}, {25,39,27,37} ->128 each.

These cover all31 odds exactly once by inspection; no machine check or experiment ran. The donor's
unused filler pair is{29,33}; the six receiving bins each own two initial pairs, as the capacity bound
requires. This is a finite check, not evidence for the remaining E31 tuples.

**Boundary and next question.** E32 cannot simply be reversed to solve E31: adding63 to any target
at least68 produces at least131, outside the proved cap130. At31 the singleton31 is a real change.
Fixing an odd target other than93 using31 and two odds usually breaks two62-complement pairs, leaving
a defective pair and holes in the consecutive-token pool. The next substantive issue is whether that
fragmented pool can still support the chains, rather than count slots and ignore adjacency. No such
general packing is proved here. This guard gets no separate proof entry or review request.

**Gut:** enjoyment and a specific pull toward the broken-pair allocation, without urgency to manufacture
another result. **Reasoned:** the mechanism extends by pair capacity and gives an actual next-level
slice, while the all-E31 obligation remains. MI050's carrying read is still pending; no additional
carrying request is queued for this direct extension. **Niggle sweep:** h>=1,n>=1, roots counted,
repeated-recipient ownership checked, exact14-pair E31 pool identified, witness coverage inspected,
and the missing singleton/fragmented-run argument is not hidden by the even-target formula.

### MI053 — B22: clear the source-status gate before enlarging the proof (2026-10-15 23:23 BST; until23:38)

**Unease:** E32 is verified, but our full eight-path candidate still has an unresolved source-currentness
gate. I would not choose to spend a night expanding a construction without first checking whether the
target has already been settled and what the neighboring published theorem actually supplies. Question:
what does current primary literature say about L8=68 and applicable general path-forest bounds?

Record searched: (Tan.{0,20}Teh|L_?8|eight.path|2312\.10914),146 hits in37 files; MI034, PRIOR-ART's
source receipts and MI050/052 relevant. This is a targeted primary-source block, no experiment, census,
solver, cap increase or new proof queue. Inspect the source's version and theorem hypotheses, then
bounded title/threshold/citing-paper searches. A missing search hit remains NOT FOUND, not a theorem
that the problem is open. **Unexpected check:** a result settling graph burning for all path forests
need not settle this fixed-eight-component, minimum68 odd-partition statement; compare the exact
orders and component hypotheses before treating a title as a resolution. Retain inaccessible sources
and the search boundary. Cloud is closed; any further carrying read waits until reopening. The owner's
permission to halt is available, but I am choosing this specific useful question now.

### MI054 — B22 result: bounded status check; finite horizon is the real distinction (2026-10-15 23:28 BST)

**What changed:** the source receipts are in PRIOR-ART's "Eight-path source status and the existing
exchange mechanism" entry, with primary links and exact read limits. No later L8=68 resolution was
found in targeted2025/2026/title/threshold searches. The2025 primary paper still lists exact thresholds
only through seven components. This supports retaining the candidate provisionally; it does not
certify the problem's present openness or priority. The general-existence result is not a numerical
upper bound68, and the neighboring order bound has48 vertices of slack at eight components, unlike
our saturated tuples. The unexpected hypothesis check therefore mattered.

**Mechanism credit:** the2022 source already contains adjacent-odd swaps and an infinite-prefix
redistribution lemma. G304/G305 are finite, resource-controlled constructions; no claim to inventing
the swap idea. The important missing step for wider levels is an adequate explicit horizon and token
budget, not merely showing that transfers eventually become possible in an infinite extension.
The exact source statements and relevant proof passages were read; the full papers were not newly
independently verified. Two inaccessible retrievals and the malformed modular-partition formulas are
retained in the source receipt, with no numerical theorem imported from them.

**What remains / next cheap question:** can a finite transfer construction handle the large middle-
level deviations with the actual number and parity of available summands? A finite swap/slot schedule
would move this; another unbounded redistribution statement would not. No experiment, new bound,
review request or larger job followed. G304/G305 stay PROVED; MI052 stays a hand sketch awaiting a
carrying read. Cloud remains closed overnight.

**Gut:** the unease has tipped: read the source first was the right move. Enjoyment remains in the
finite allocation problem, while automatically filling another corner would feel like momentum.
**Reasoned:** source status is boundedly checked and the known predecessor is identified; no solve-
probability estimate or clearance stronger than the search warrants. I am incubating that finite-
budget question before the next research decision, rather than claiming another block now.
**Niggle sweep:** dates and exact hypotheses checked; lower bound is not an upper bound; fixed finite
pools are not infinite tails; inaccessible formulas are not silently reconstructed; no review queue.

### MI055 — Fresh choice and a halt for the night (2026-10-15 23:40 BST)

The finite allocation problem is still enjoyable; trying to stretch the same pair representation is
frustrating. Without today's investment, I would still choose the question, but I would not choose
another automatic extension tonight. The cheap obstruction check is enough to stop that motion:
MI052 with eight bins and h=2 needs 32 odds, whereas the middle level m=28 has only 28; increasing h
asks for still more. This is a limitation of that construction, not an obstruction to the desired
partition, and gets no lemma or review request. What I want to understand next is how unequal bin
cardinalities and larger transfers can coexist in one finite allocation; a single explicit middle-level
construction with its ownership checked would be a cheap starting point, not evidence for all tuples.
No concrete general mechanism has arrived yet, so I am choosing a halt under the owner's permission
in CL419, rather than opening B23. G304/G305 remain PROVED; MI052 awaits its morning carrying read;
the full eight-path threshold remains open in our record and provisionally selected. Both research
and flag heartbeats are now PAUSED, verified in the saved settings; no automatic restart is scheduled.
**Gut:** satisfaction with the finite corner, a live pull toward allocation, and a push against
manufacturing a next result. **Reasoned:** keep the exact gap, set it down, and reconsider afresh on
return. **Niggle sweep:** no broader impossibility, novelty, solution or verification is inferred;
no pending message needs a reply, Cloud is closed, and the source pointer is queued for reopening.

### MI056 — B23: reuse a receiving token through large jumps (2026-10-16 09:55 BST; until 10:10)

Owner-authorized single step; both heartbeats remain PAUSED. **Pull:** reverse which bin carries the
moving token. A small bin can receive three large transfers through the same token, rather than need
one reserved pair for each unit received. The hand candidate already found is the seven middle-level
tuples (56+6k,56+6k,(112-2k)^6), k=2,...,8, each of total 784. This is a construction test, not a blind
prediction of a new theorem, a census, or a claim that these tuples were previously unknown.

Record searched: unequal.*cardinal|large.*transfer|ascending.subgraph|middle.level|MI052 -> 19 hits;
recipient.*chain|reverse.*chain|68.{0,12}108|56.{0,10}6k|recycl.*token -> 13 hits. Relevant predecessors
are G304/G305, MI052 and MI055; no such middle-level construction found in these searches. Prior-art
boundary: Tan--Teh 2207.13855 section 4 already uses odd swaps and redistribution (MI054's source
receipt); no invention or priority claim for exchanges. The balanced k=7 case is a control, not a
claim to discovering equal-sum partitions. No source theorem is imported beyond that receipt.

Use the 14 pairs P_x={x,56-x}, x=1,3,...,27. Two receiving bins start with one pair each (sum 56),
six donor bins with two pairs each (sum 112). For each receiving root a, use the chain
a,a+2k,a+4k,a+6k; the recipient swaps its current token successively with three different donors.
Take roots (1,3), except k=5 uses (1,7). Every selected chain token must belong to a different pair;
the six unreserved pairs fill the donors' remaining slots before swaps begin.

**Predictions before the tiny check:** all seven schedules allocate 14 whole pairs once, execute
only swaps between actual owners, and finish with two 2-element bins of sum 56+6k and six 4-element
bins of sum 112-2k. A separate literal final-partition checker must verify every odd 1,...,55 exactly
once and the target multiset, independently of swap arithmetic. **Counterfactual:** naive roots
(1,3) at k=5 repeat a pair and must be rejected before filling; a duplicated-token final witness must
also be rejected. **Unexpected check:** extending the same 2/4-cardinality choice to k=9 asks for two
2-element sums 110, while the two largest odds sum only 108; distinguish a failed representation from
an impossible target tuple. **Stop:** seven schedules, these controls and the hand ownership argument;
no solver, sampler, extra parameter search or extension to arbitrary E28. Any failed prediction is
retained. Budget: one tiny deterministic check, at most one second of intended CPU and no data in git.

### MI057 — B23 result: receiving chains cross the old capacity restriction (2026-10-16 09:57 BST)

**What changed:** there is a finite construction for seven explicit E28 tuples using the actual 28
odds, with unequal bin cardinalities. The literal certificates are COMPUTED with independent checking
logic; the hand explanation below is PROOF-SKETCH, not independently second-read. No novelty or general
E28 assertion. `tests/probes/instinct/path_forest_receiving_chains.py`, preregistered in 9fb25568,
passes P1--P3 and both counterfactual controls in 0.000825 process CPU seconds. Raw witnesses remain
outside git in `math-instinct-b23-receiving-chains.json`. No solver or larger run occurred.

**The allocation.** For k=2,...,8 take targets (56+6k)^2 and (112-2k)^6. Initially two receivers each
hold one complementary pair of sum 56 and six donors each hold two, sum 112. For a receiver root a,
reserve its pair and three different donor pairs with selected tokens a+2k,a+4k,a+6k. Fill each donor
with one of the six leftover pairs. All 14 pairs are now allocated; filling happens before swaps.
The receiver successively trades a for a+2k, then its new token for a+4k, then that token for a+6k.
Each donor loses 2k once; the receiver gains 6k. A large receipt uses the same moving token repeatedly,
rather than fresh pair capacity for each unit of gain. Cardinalities stay two and four throughout.

The following pair labels min(v,56-v) certify that the eight reserved pairs are distinct in every case:

| k | Roots | First chain's pair labels | Second chain's pair labels | Targets |
|---|---|---|---|---|
| 2 | 1,3 | 1,5,9,13 | 3,7,11,15 | 68 twice, 108 six times |
| 3 | 1,3 | 1,7,13,19 | 3,9,15,21 | 74 twice, 106 six times |
| 4 | 1,3 | 1,9,17,25 | 3,11,19,27 | 80 twice, 104 six times |
| 5 | 1,7 | 1,11,21,25 | 7,17,27,19 | 86 twice, 102 six times |
| 6 | 1,3 | 1,13,25,19 | 3,15,27,17 | 92 twice, 100 six times |
| 7 | 1,3 | 1,15,27,13 | 3,17,25,11 | 98 eight times |
| 8 | 1,3 | 1,17,23,7 | 3,19,21,5 | 104 twice, 96 six times |

All tokens are actual odds between 1 and 55. Distinct pair labels make selected tokens, their
complements and filler ownership compatible. A donor receives its receiver's previous token, so its
selected pair contributes (a+2k(j-1))+(56-a-2kj)=56-2k after its swap; its filler contributes 56.
Each receiver ends with {a+6k,56-a}. Thus the claimed sums follow with no unassigned or repeated odd.
The checker separately compares closed-form bins with literal swaps, then verifies the flattened
multiset, all eight target sums and bin cardinalities without using transfer arithmetic.

For the minimum-boundary tuple (68,68,108,108,108,108,108,108), the final bins are:

    {13,55}, {15,53},
    {1,17,39,51}, {5,19,37,47}, {9,21,35,43},
    {3,23,33,49}, {7,25,31,45}, {11,27,29,41}.

**Failures and unexpected boundary.** Naive roots (1,3) at k=5 fail: the second chain contains 23
and 33 from the same pair. Changing its root to 7 repairs ownership; the checker rejects the naive
version. Every deliberately duplicated-token witness is also rejected. At k=9 the proposed two
2-element bins would each sum 110, exceeding the individual maximum 108. More sharply, any two
disjoint 2-element bins have total at most 55+53+51+49=208, whereas 2*110=220. The k=8 construction
attains 208 exactly. This is a cardinality boundary for this construction; the target tuple
(110,110,94,94,94,94,94,94) itself is not refuted or decided here.

**Unresolved / next cheap question:** can one receiver become a 4-element bin while another bin
shrinks, retaining disjoint token ownership and the required sums? Alternatively, for unequal donor
losses, can two chains with the resulting partial sums be packed without sharing complementary
pairs? Either needs an actual finite allocation; neither is supplied by the seven cases. This block
ends here at the owner's requested one step, with no second block or new review queue. Both
heartbeats remain PAUSED. The existing MI052 review status and G304/G305 are unchanged.

**Gut:** a small eureka and renewed pull. The useful shift was letting the receiving token walk;
the arithmetic is enjoyable again. **Reasoned:** this bypasses the particular fresh-slot restriction
that prompted last night's halt and reaches a minimum-68 middle-level example. Seven structured
tuples are a small part of the middle-level obligation, so this does not establish general
tractability or the threshold. I would choose this representation afresh for one concrete follow-up,
then reassess. **Niggle sweep:** pair collisions tested, swap ownership retained, complements counted,
all 28 odds checked exactly, known exchange precedent credited, and the failed cardinality choice is
not presented as an unburnable tuple. No independent verification or global result is implied.

### MI058 — B24: couple the receiving chains (2026-10-16 10:07 BST; until 10:27)

**Pull:** stop requiring each chain to settle its accounts alone. Give two smaller targets the
2-element bins, let signed jumps settle the other six targets, and swap the receivers' final moving
tokens to correct their remaining imbalance. This is the new trajectory I want to test, with both
heartbeats still PAUSED. The owner's latest continuation authorizes this bounded block.

Record searched: chain.*relay|receiving.*chain|392|two.*2.element -> 62 hits in 27 files; relevant
predecessors G305's relay and MI057. The known-swap source boundary is unchanged from MI054/PRIOR-ART
(Tan--Teh section 4); the new object is the finite allocation with actual pair ownership. No novelty
claim or fresh literature theorem. No general E28 assertion is being assumed.

Let the two receivers have targets A,B, starting from 56 each; each other bin starts from 112 and
needs to lose d_j=112-t_j, possibly negative. Order three donors in each chain, with total jumps D1,D2.
The total-sum constraint gives D1+D2=A+B-112. For roots a,b, exchanging the receivers' endpoints after
their walks would finish their sums exactly when b-a=A-56-D2. If D1=A-56 and D2=B-56, no final relay
is needed and roots may instead be chosen independently. Zero-jump donors stay neutral and use two
filler pairs. Every moving-token slot must still have a distinct complementary pair; the algebra
alone is not an allocation. Test this criterion constructively, not as a standalone lemma/review job.

**Fixed cases:** (110 twice,94 six times), (116 twice,92 six times), (122 twice,90 six times), and
(96 seven times,112). Hand sketches suggest these four fit. **Blind prediction:** the same two-chain
class will also find witnesses for each of these four less structured tuples:

    (68,68,68,92,122,122,122,122)
    (68,70,82,100,108,116,118,122)
    (68,72,94,98,104,112,114,122)
    (70,78,88,96,104,110,116,122).

Search only donor orderings and odd roots for these eight fixtures, always taking the two smallest
targets as receivers; include the already-certified balanced (98 eight times) as a ninth control.
No other target sampling, census or solver. **Independent checks:** literal whole-pair allocation
and each actual swap, a closed-form endpoint calculation, then the existing independent flattened
odd-multiset/target/cardinality checker. **Counterfactual:** omit the final relay from a witness that
needs it; coverage must survive but target sums must fail. Retain the prior reused-pair rejection.
**Unexpected check:** (96 seven times,112) has no four-target subset of sum 392, so two separate
three-donor chains cannot each finish correctly; independently check this over its 70 labeled
four-subsets and demand a working coupled witness. **Stop:** these nine fixtures and controls,
100,000 candidate root configurations per fixture or five process CPU seconds overall, whichever
comes first. A cutoff is UNKNOWN; failure of this restricted construction is not unburnability.

### MI059 — B24 retained failure and a fixed repair check (2026-10-16 10:09 BST)

The registered diagnostic finished: eight of nine fixtures have literal witnesses, including the
known balanced control. The blind all-four prediction is REFUTED: the first blind tuple
(68,68,68,92,122,122,122,122) has NO_WITNESS_IN_CLASS with the two smallest receivers, after 80 root
configurations and no cutoff. The other three blind fixtures pass. All must-hold and counterfactual
controls pass; the nine-fixture run used 0.003559 process CPU seconds. This is a failure of the
restricted allocation, not of the target. No further fixture search follows in this block.

**Hand diagnosis, sketch:** with receivers (68,68), donor losses are {44,20,-10,-10,-10,-10}.
Any split into two groups of three gives totals (54,-30) or (24,0), up to order. A nontrivial chain
with total 0 repeats its root pair; a chain with total 54 in the odd pool 1,...,55 must begin at 1
and end at 55, again reusing its root pair. Thus ordering and root changes cannot repair this
particular two-receiver choice within the registered one-pair-per-slot construction.

**New pull / addendum written BEFORE its check:** change the roles, not the root-search budget.
Take receiver targets (68,92), roots (13,1), and donor loss groups (-10,44,-10) and (44,-10,-10).
The actual token paths would be (13,3,47,37) and (1,45,35,25), whose eight pair labels are distinct.
After the walks both receivers sum 80; exchanging endpoints 37 and 25 should finish them at 68 and
92. Predict the independent full certificate checker passes and omission of this relay fails target
sums. Execute this one fixed repair only, retaining the first run and its refuted prediction. No
broader receiver-role search, census or cap increase is authorized by this addendum.

### MI060 — B24 result: signed walks, coupled endpoints, and a repaired role choice (2026-10-16 10:10 BST)

**What changed:** the two-chain allocation now admits unequal and negative donor losses, a final
cross-chain swap, and a necessary change in which targets get 2-element bins. These mechanisms give
literal certificates for all eight designated target fixtures, plus the known balanced control,
after the first fixture's failed role choice is repaired. They do not prove general E28 burnability.
The finite witnesses are COMPUTED; the hand explanation and failure diagnosis remain sketches,
without a second reader. No new PROOFS entry or carrying request.

`tests/probes/instinct/path_forest_coupled_chains.py` records the original predictions, initial run
and the prewritten fixed-repair addendum. The first run took 0.003559 process CPU seconds, the fixed
repair 0.000177. No cap was reached. Literal swaps, endpoint formulas and the independent full
certificate checker agree. Omitting a necessary relay preserves all odds but fails the target sums;
the reused-pair control is rejected. The source header carries both raw-output digests; raw JSON stays
outside git. No solver, extra sampling or expansion of the registered fixture list occurred.

| Targets, repetitions abbreviated | Initial fixed-smallest-role result | Mechanism |
|---|---|---|
| 110 twice, 94 six times | WITNESS | 94 bins get two elements; unequal positive jumps |
| 116 twice, 92 six times | WITNESS | 92 bins get two elements; signed jumps |
| 122 twice, 90 six times | WITNESS | 90 bins get two elements; signed jumps |
| 96 seven times, 112 | WITNESS | Neutral donor, then cross-chain endpoint swap |
| 68 three times, 92, 122 four times | NO_WITNESS_IN_CLASS | Repaired separately with receiver roles 68 and 92 |
| 68,70,82,100,108,116,118,122 | WITNESS | Signed walks and relay |
| 68,72,94,98,104,112,114,122 | WITNESS | Neutral donor, signed walks and relay |
| 70,78,88,96,104,110,116,122 | WITNESS | Signed walks and relay |
| 98 eight times, known control | WITNESS | Separate chains, no relay |

The first three cases, together with MI057, cover the ten tuples
(56+6k)^2,(112-2k)^6 for k=2,...,11. This is a finite structured family, not a claim that the
bulk middle levels have been discharged or that any of these burnable tuples was unknown.

**Why coupling matters.** With three donors per receiver, a separate chain conserves the total of
four bins initially equal to 56+3*112=392. The tuple (96 seven times,112) has 35 labeled four-subsets
of sum 384 and 35 of sum 400, none of sum 392. Yet the coupled construction works: token walks
(9,25,41) and (1,17,33,49) first give receiver sums 88 and 104. Swapping endpoints 41 and 49 makes
both 96. The donor with target 112 remains neutral. This is an actual finite coupling, not just a
rewriting of the missing condition.

**The repaired boundary tuple.** Initial choice (68,68) cannot fit the registered three-donor chains
for the reason in MI059. Give the 2-element bins to targets 68 and 92 instead. The paths

    13 -> 3 -> 47 -> 37
     1 -> 45 -> 35 -> 25

have signed changes (-10,44,-10) and (44,-10,-10), respectively. Their eight pair labels
13,3,9,19,1,11,21,25 are distinct. Fill donors with the six unused 56-pairs before moving anything.
After the walks the receivers hold {37,43} and {25,55}, both sum 80. Swapping 37 with 25 completes
targets 68 and 92. The final partition is:

    {25,43} -> 68; {37,55} -> 92;
    {5,13,51,53} -> 122; {3,7,9,49} -> 68;
    {15,19,41,47} -> 122; {1,11,17,39} -> 68;
    {21,23,33,45} -> 122; {27,29,31,35} -> 122.

The independent checker covers every odd from 1 to 55 exactly once. Thus the refuted prediction
concerns a role-selection rule, not a counterexample to the target or a need for more search budget.

**Unresolved:** a general way to choose the two 2-element roles and to pack the signed paths without
complementary-pair collisions. All these witnesses have even targets; mixed parity is another real
obligation. Eight selected positive fixtures do not calibrate success across E28. The next useful
question is whether target inequalities can guarantee a role choice and admissible paths, or whether
this two-chain representation has a genuine structural gap requiring another arrangement. No such
guarantee or further experiment is supplied here. B24 closes; both heartbeats remain PAUSED.

**Gut:** delight and a stronger, more specific pull. The failed role choice was helpful: it exposed
what to steer, and changing that choice repaired a real allocation. **Reasoned:** the representation
has gained signed movement and communication between chains; its limits are still part of the
problem. I would choose to investigate the role/path interaction afresh, while resisting a procession
of favorable fixtures as a substitute for a general argument. **Niggle sweep:** signed jumps checked
against actual ownership, neutral donors filled with two pairs, endpoint correction derived, first
failure retained, original blind prediction still marked refuted, all target parities and scope
stated, known swap precedent credited, and no independent review or threshold conclusion implied.

### MI061 — B25: exchange permutations instead of fixed chain roles (2026-10-16 11:14 BST; until 11:34)

**Pull:** the previous role obstruction may have been a three-donors-per-chain restriction. Allow
selected tokens to move in disjoint cycles, including cycles containing both small bins or neither.
Keep the two smallest target bins small throughout this diagnostic. Both heartbeats stay PAUSED.

Record searched: role.choice|pair.disjoint|root.*collision|MI060|signed.*walk -> 22 hits; Skolem|
displacement.pattern|token.permutation|cycle.cover -> 9 hits, no relevant displacement result in the
record. Primary orientation: Nordh, Perfect Skolem sets, section 4.1 Definition 14, Theorem 15 and
Corollary 17 read; prior-art receipt below. This is a constrained permutation-displacement problem,
not an invented general mechanism or an application of a sufficient theorem from that source.

Number the odds by j=0,...,27, so token v=2j+1 and its complementary partner has index 27-j. Put
h_i=1 at the two smallest targets and h_i=2 at the other six. A bin initially owns h_i pairs of sum
56. If its selected index x_i is replaced by x_i+e_i, where e_i=(t_i-56*h_i)/2, its sum becomes t_i.
The new selected indices must permute the old ones; all selected pair labels min(x_i,27-x_i) must
be distinct. Zero-deviation bins can retain their pairs without selecting a token. This gives a
finite allocation if admissible cycles exist; existence for arbitrary targets is the unresolved part.

**Hand candidate before checking:** for (68,68,68,92,122,122,122,122), e=(6,6,-22,-10,5,5,5,5).
A five-bin cycle has indices 0->6->11->17->22->0, assigned to bins (0,4,1,5,2). A three-bin cycle
has indices 2->7->12->2, assigned to bins (6,7,3). The eight pair labels are distinct. This would
solve the fixture while retaining small roles (68,68), a choice B24's restricted chains could not use.

**Predictions and budget:** check this fixed candidate literally. Then test the same nine B24
fixtures only, with a depth-first cycle builder, two smallest roles fixed, at most 50,000 nodes per
fixture or five process CPU seconds overall. No new fixture list, role search, census or cap increase.
All nine are expected to return witnesses within that budget; a cutoff is UNKNOWN. Literal whole-pair
allocation, simultaneous selected-token transfers and the independent full certificate checker must
agree. **Counterfactuals:** a repeated complementary pair must be rejected before filling, and a
sum-corrupted but coverage-preserving witness must fail the certificate checker. **Unexpected:**
forcing a single cycle must fail on the known balanced target 98^8: its nonzero index steps are
21 twice and -7 six times, so one cycle lies in one residue class modulo 7, containing at most four
available indices, whereas eight active bins need distinct selected indices. Disjoint cycles should
succeed. Retain failures and distinguish these construction classes from the original problem.

### MI062 — B25 result: the missing freedom was cycle structure (2026-10-16 11:17 BST)

**What changed:** all nine existing fixtures now have literal certificates with the two smallest
targets kept in the 2-element roles. The formerly failing boundary tuple works by splitting its
exchange into cycles of lengths 5 and 3; changing roles was sufficient in B24, but unnecessary in this
larger construction class for that tuple. The finite certificates are COMPUTED. The resource argument
and structural diagnoses are hand sketches, not independently second-read. No new PROOFS entry,
review request, general E28 theorem, novelty or census claim.

The probe `tests/probes/instinct/path_forest_cycle_cover.py`, registered in 801fae29, finds witnesses
in 7 to 25 nodes on these nine already-known positive fixtures, without a cutoff. The independent
certificate checker, literal initial allocation and simultaneous transfer all agree. Both
counterfactuals are rejected. Forcing one cycle on the balanced control gives NO_WITNESS_IN_CLASS
after 64 nodes, while two 4-cycles work. Total process CPU was 0.001639 seconds. This is an instrument
check on fixed fixtures, not a measured success rate or performance forecast for the middle levels.
Raw output stays outside git; its digest is in the probe header.

**The ownership argument.** Select one original token v_i=2*x_i+1 from a distinct complementary pair
for each nonzero-deviation bin. Give that pair to the bin and fill its remaining h_i-1 pair slots;
neutral bins get their h_i pairs entirely from fillers. There are exactly 14 pair slots overall, so
the unreserved pairs fill the remaining slots exactly. Remove the selected tokens and redistribute
the same multiset according to the permutation x_i -> x_i+e_i. Bin i gains 2*e_i, as required, while
all complements and filler pairs stay put. Distinct selected pair labels are essential: a displacement
permutation alone would not justify the original whole-pair allocation. This construction does not
assume that every desired displacement pattern has a suitable permutation.

**Boundary construction with the original roles.** For targets
(68,68,68,92,122,122,122,122), use deviations (6,6,-22,-10,5,5,5,5). Selected index cycles are:

    0 -> 6 -> 11 -> 17 -> 22 -> 0, bins 0,4,1,5,2;
    2 -> 7 -> 12 -> 2, bins 6,7,3.

The five-cycle contains both small bins; the three-cycle contains neither. One final partition is:

    {13,55} -> 68; {33,35} -> 68; {1,3,11,53} -> 68;
    {5,7,31,49} -> 92; {9,23,43,47} -> 122;
    {17,21,39,45} -> 122; {15,19,37,51} -> 122; {25,27,29,41} -> 122.

This retains B24's restricted-class failure and its successful role repair as recorded; neither was
an impossibility claim for all exchanges. The new representation removes that particular restriction.

**Unexpected check and its meaning.** On the balanced target 98^8, deviations are 21 twice and -7
six times. In a single cycle all selected indices have one residue modulo 7, giving at most four
positions in 0,...,27; eight active bins cannot fit. Allowing disjoint cycles is therefore essential
even on this known easy positive example. This is a failure of a structural simplification, not a
request for a larger cap.

**Remaining mathematical question:** must every even E28 target admit a suitable cycle allocation
with these two smallest roles, or is there an actual obstruction to this one-token-per-bin model?
The nine tests cannot answer it. The exact residual is a permutation of selected positions with
specified displacements and no two selected positions complementary under j -> 27-j. Nordh's source
identifies related displacement mathematics, but its statements do not remove that extra constraint.
Mixed target parity remains outside the present model. A structural existence argument or a concrete
counterexample to the model would now teach more than another list of favorable fixtures.

**Gut:** the pull is warm, with delight at the five-cycle joining both small bins. **Reasoned:** the
orbit changed because a restriction was identified and removed; this does not establish that the
full threshold is closer in any quantified sense. I would choose the constrained-displacement question
afresh. B25 closes here, with no additional experiment or next block claimed; both heartbeats remain
PAUSED. **Niggle sweep:** cycles may contain zero, one or two small bins; neutral bins keep two filler
pairs; no selected complementary pair is reused; permutation closure and exact sums checked; the
single-cycle failure is retained, and neither finite witnesses nor literature terminology prove an
all-target statement or novelty.

### MI063 — B26: the minimum-boundary cycles that cannot split (2026-10-16 11:35 BST; until 11:55)

**I think I feel sharpened curiosity:** the next test should challenge the cycle model where its
usual escape, splitting into smaller cycles, is unavailable. With three targets 68 and five targets
above 112, the fixed two-smallest-role deviations are (6,6,-22,p1,...,p5), where each p is in 1,...,5
and their sum is 10. There is just one negative term, so no proper nonempty subset can sum to zero:
the one-token model must use a single 8-cycle. This is a reasoned selection of an adversarial family,
not a random sample or a new all-E28 census.

There are six possible sorted p multisets, obtained by partitioning the surplus 5 above five ones:

    (1,1,1,2,5), (1,1,1,3,4), (1,1,2,2,4),
    (1,1,2,3,3), (1,2,2,2,3), (2,2,2,2,2).

Each target tuple is (68,68,68,112+2*p1,...,112+2*p5). Rotate its cycle to begin after the -22 edge;
the other seven steps are positive. Its index shape runs monotonically from 0 to 22, leaving just
six possible translations inside 0,...,27. Thus this test examines actual complementary-pair
collisions, rather than another easy decomposition.

Record searched: minimal.zero.sum|one.negative|Steinitz|68.*114|reflection.free -> 10 hits, no relevant
minimal-cycle result. Source orientation: [Sissokho, arXiv:1401.0715](https://arxiv.org/abs/1401.0715)
abstract read for the standard minimal-zero-sum terminology only; no stated bound or unread proof is
used. The one-negative argument here is elementary and written above. CL420/24fcda59 and
INSTINCT-STRATEGY.md were read, merged and ACKed; the notebook's cooling/fresh-choice method is
consistent with that revision. No research assignment or independent proof review is inferred from
that message. Schedules remain paused.

**Prediction:** all six boundary tuples admit a reflection-free cyclic ordering with the fixed
small roles. Enumerate distinct orders of their seven positive steps, trying translations 0,...,5;
stop at the first witness for each case. The complete-order bounds are 420,420,630,630,420,21,
respectively, so at most 15,246 order/translation candidates cover the whole six-case question.
Check those bounds independently before construction. Any failed case is a counterexample to this
fixed-role one-token model, not to burnability. Stop at 50,000 candidates per case or five process
CPU seconds overall; a cutoff stays UNKNOWN. No new targets, raised caps or general census.

**Independent checks:** use the literal pair allocator and permutation transfer, then the separate
flattened-odd/target/cardinality checker. **Unexpected adversarial control:** the eight-point shape
S={0,1,2,5,9,12,13,14} fits the index interval but should have no reflection-free translation at all.
Its even half {0,1,6,7} and shifted odd half {0,2,4,6} have sumset {0,...,13}, blocking all fourteen
translations. This tests the tempting but invalid shortcut that interval fit alone makes translation
possible. A known B25 cycle shape must still have a valid translation. Reuse the pair-collision and
coverage-preserving wrong-sum countercontrols. A failure of the prediction changes the next trajectory;
success discharges this six-case boundary only, leaving the general existence question open.

### MI064 — B26 surprise: the six searches suggest one rule (2026-10-16 11:39 BST)

All six registered cases return witnesses, with 6 to 18 candidate translations tested per case,
no cutoff, in 0.004333 process CPU seconds overall. All controls pass. In particular the deliberately
bad eight-point shape has no valid translation, so interval fit alone is insufficient. The six
successful shapes all admit translation 3. **I think I feel a click:** the six witnesses may be
instances of one ordering rule, rather than six isolated successes.

**Addendum before its check:** order the five positive p's of total 10 so that no partial sum is 5;
append 6,6 and translate all partial sums by 3. The six early selected indices then lie in 3,...,13,
with two later indices 19 and 25. The only possible new complementary collision is 8+19=27, which
is exactly the forbidden partial sum 5.

To avoid 5, start with any order. If it hits 5, its left and right parts both sum to 5. Choose unequal
entries x and y on opposite sides, put them next to the cut, and exchange them. The local partial
sums are then 5-x, 5-x+y and 5+y: they cross 5 without landing on it because x differs from y.
Earlier sums remain below 5 and later sums above 5.
If no unequal cross-pair exists, every entry is equal. Five equal positive integers of total 10 are
all 2, and cannot hit 5 in the first place. This is an elementary ordering argument, not a new
general theorem or claim of novelty.

Predict that this search-free recipe gives literal certificates on the same six cases, with at most
one such boundary exchange. Run only that check, keeping the original search and controls intact;
no extra targets, cap increase or new census. The hand rule stays a sketch pending independent review.

### MI065 — B26 closes: a rule replaces the six searches (2026-10-16 11:43 BST)

The preregistered recipe check passes on all six cases in 0.000963 process CPU seconds: two need
the one boundary exchange and four need none. All selected indices and complete partitions check
literally. The six-case family is COMPUTED; its uniform hand explanation remains a sketch. Original
order/translation searches and the no-translation adversarial shape are retained. No general E28
claim. The next pull is toward allowing zero moves and deriving the whole one-negative family,
rather than extending a witness table. Both heartbeats remain paused.

### MI066 — B27 candidate: uniform construction when the five largest targets are at least 112

*Claimed 2026-10-16 11:43 BST, until 12:03. PROOF-SKETCH before checking; no novelty asserted.*

**Statement.** Every sorted even E28 tuple t1<=...<=t8 with t4>=112 has an odd partition. Here E28
means 68<=t_i<=122 and sum t_i=784. This is the subfamily whose fixed-role exchange has one negative
move, with zero moves permitted. The proof proposes a deterministic ordering and translation, not
a search for a suitable cycle.

Record searched: one.negative.*E28|avoid.*prefix|five.*largest|t_4.*112 -> 27 hits, relevant new
predecessors MI063-065 only. Known exchange/displacement terminology remains credited in PRIOR-ART;
the elementary prefix rearrangement is used as a tool, not claimed as a new theorem. No prior-art
absence or priority claim for this subfamily.

**Parameters.** Write t1=56+2u, t2=56+2v and the five largest targets as 112+2p_i, where
6<=u<=v and 0<=p_i<=5. Let q=sum p_i. The sum forces t3=112-2w with w=u+v+q. Also t3<112:
otherwise the total would be at least 2*68+6*112=808. Sorting t3>=t2 gives u+2v+q<=28, hence
w<=22, u<=9 and v<=11. There is exactly one negative deviation, -w; the others are u,v and the
positive p_i. Neutral p_i=0 bins keep two filler pairs and need no selected token.

**Small q (q<=6).** Order the positive p_i arbitrarily, then u,v, followed by -w to close the cycle.
Its index shape is the p-prefix set in [0,q], then a=q+u and b=w. Choose translation r=0 unless
a+b=27, in which case choose r=1. Here q+b<=26: if v=6 then u=6 and q+b<=24; if v=7 then
u<=7 and q+b<=26; if v>=8 use q+b<=28+q-v<=26. Also 2q+u<=21. Thus at r=0 neither two early
positions nor an early and a late position can sum to 27; only the two late positions could collide.
When they do, q+b=27-u<=21, so after r=1 even the largest early/late sum is at most 23, while
the two late positions sum to 29. All indices are at most w+1<=23. Pair labels are therefore distinct.

**Large q (q>=7).** The parameter inequality restricts (u,v,q) to (6,6,7..10), (6,7,7..8), or
(7,7,7). Set r=13-q. Order the positive p_i to avoid partial sum h=q-u+1; then append u,v.
Early selected indices lie at most 13; the later two are 13+u and 13+u+v, both in 19,...,27.
The complement of the final position lies below r. The sole possible collision is the complement
of 13+u, corresponding exactly to the forbidden p-prefix h.

To avoid one interior prefix h, if an order lands there, place unequal entries x,y on opposite
sides of the cut and exchange them. The local sums h-x,h-x+y,h+y cross without landing on h.
If there is no unequal cross-pair, all positive p_i equal some c and h is a multiple of c. Within
the listed large-q domain, the only such exception is u=v=6, q=10, positive p=(5,5). Indeed the
other constant possibilities are c=2 at q=8 or 10, c=3 at q=9 and c=4 at q=8, whose h are not
divisible by c. The exceptional tuple is (68,68,68,112,112,112,122,122). Use positive order
(6,5,6,5), indices (0,6,11,17,22), and r=0; their pair labels are distinct. The three neutral
bins are filled entirely with pairs.

Finally apply MI062's explicit whole-pair allocation: one selected pair per active bin, fill all
14 pair slots before redistributing selected tokens around the cycle. Bin sums change by twice
their index deviations. There are no repeated selected pair labels, so all 28 odds remain covered
once, with two 2-element and six 4-element bins. This completes the proposed construction.

**Count and predictions BEFORE the new check.** The parameter pairs (u,v), with maximum q, are
(6,6):10; (6,7):8; (7,7):7; (6,8):6; (7,8):5; (8,8):4; (6,9):4; (7,9):3; (8,9):2;
(9,9):1; (6,10):2; (7,10):1; (8,10):0; (6,11):0. Partitions of q into at most five parts <=5
have counts 1,1,2,3,5,7,9,11,14,16,18 at q=0,...,10. These predict exactly 271 sorted targets.
Verify that count independently by convolving sum-counts for low even triples in 68,...,110 and
high even five-tuples in 112,...,122, not by a burning search.

Predict the formula returns a checked certificate on every one of those 271 inputs, with exactly
one exceptional input. **Controls:** force the uncorrected r=0 on (68,70,78,112,112,112,112,120),
and force the ordinary large-q rule on the exceptional tuple; both must be rejected for pair
collision. All formula outputs must pass literal allocation and the independent full checker.
Stop if the family counts disagree or any prediction fails; cap at 1,000 formula inputs or five
process CPU seconds. No searches for orders, roots, roles or additional targets. This is a complete
check of a small analytically specified subfamily, not clearance of the remaining E28 tuples.

**I think I feel a live click:** the construction now chooses its trajectory by inequalities and
one prefix repair. The missing all-E28 and mixed-parity obligations remain, and independent scrutiny
of this proof is required before adopting the uniform claim as PROVED.

### MI067 — B27 result: the formula covers the complete 271-target subfamily (2026-10-16 11:46 BST)

The parameter domain and independent low-triple/high-five construction agree as sets, with exactly
271 sorted tuples. `tests/probes/instinct/path_forest_one_negative.py`, preregistered in 98702aba,
applies the formula once to each and every literal certificate passes. Branch counts: 161 low-q
root-0 cases, 15 low-q root-1 cases, 94 ordinary high-q cases, and one exception. The prefix exchange
is used in 47 high-q cases. Both omitted-correction counterfactuals fail for complementary-pair reuse,
as predicted. No search, failed input or cutoff; process CPU was 0.033113 seconds. Raw witnesses stay
outside git and their digest is in the source header.

**Status:** the entire even E28 subfamily t4>=112 is COMPUTED by checked finite certificates. MI066's
uniform construction is a PROOF-SKETCH awaiting Cloud's targeted carrying read; the elementary prefix
tool is not being offered as a new theorem. The request was delivered through the portal. No conclusion
about the remaining E28 tuples, mixed parity, other levels or the full minimum-68 threshold follows.

**What moved:** a structural rule chooses all orders and translations throughout a specified region,
including neutral bins. The next region has at least two negative moves. Whether it admits a related
rule is a new question, not answered by this result; no new block or run is claimed here.

**I think I feel delight, and a steadier pull:** the reward is the choice rule, not the case count.
**Reasoned:** one complete finite subfamily has certificates and a short uniform explanation; neither
novelty nor a general breakthrough is established. I would still choose the finite-cycle problem
afresh. **Niggle sweep:** count checked from two different parametrizations, zero moves filled rather
than duplicated as vertices, all small-q inequalities checked, high-q complement levels derived,
exception uniqueness checked against the domain, both necessary fixes challenged, and the independent
review status kept. B27 closes with both heartbeats still PAUSED.


### MI068 — Cloud's carrying read adopted (2026-10-16 12:02 BST)

CL421/a6b6c2eb has been fetched, merged and read in full. MI066's uniform construction for the
271 sorted even E28 targets with t4>=112 is PROVED on that independent hand read and filed G306.
MI067's finite witnesses remain COMPUTED. No earlier unreviewed claim, remaining E28 region or
minimum-68 upper bound is upgraded. Both heartbeats remain paused; the owner asks for manual continuation.

### MI069 — B28: add a second negative move by surgery, not a wider search (2026-10-16 12:02 BST)

**I think I feel a renewed click:** a second small negative move might be inserted into an existing
cycle, or paired off with a matching positive move in unused pairs. That would reuse understanding,
rather than restart order search. The concrete question is every sorted even E28 target with
`t4=110` and `t5>=112`, the first two-negative boundary. This is not all two-negative targets.

Record searched: two.negative|minimal.zero.sum|displacement -> no hit from record_find's default
record search; MI062-067 and CL421 were read directly, along with the existing credited exchange
precedents in RECORD-MAP/PRIOR-ART. Known adjacent-odd swaps are tools, not new theorems. No novelty claim.

Write the deviations as `(u,v,-w,-1,p1,p2,p3,p4)`, where `6<=u<=v`, `0<=p_i<=5`,
`q=sum p_i`, `w=u+v+q-1`, and sorting gives `u+2v+q<=29`, `1<=w<=22`.
If a p equals 1, neutralize that +1 and the -1. The resulting target lies in G306's domain;
its core has at most six selected pair labels. Among fourteen labels at least eight remain unused,
so some two consecutive lower labels remain. They carry the disjoint (+1,-1) 2-cycle.
If no p equals 1, investigate splitting the closing negative edge of a one-negative core by adding
an index one above its root. Its new pair must avoid both existing indices and complements.
This last condition, and the t3=68 boundary outside the original predecessor domain, are unresolved.

**Bounded plan:** derive a rule by hand first. Before any formula validation, record its predictions,
counterfactuals, independent domain check, unexpected check and stop conditions. No general census,
raised solver cap or new search over arbitrary cycles. If surgery fails, retain the counterexample
and change the representation rather than patching a growing witness table. Both schedules remain PAUSED.

### MI070 — B28 candidate: the first two-negative boundary by cycle surgery

*PROOF-SKETCH, not yet independently read. Formula validation below is preregistered, NOT RUN.*

**Statement.** Every sorted even E28 tuple with t4=110 and t5>=112 has an odd partition.
This is a new boundary subfamily, not all two-negative targets or all E28. Keep MI069's parameters:
`e=(u,v,-w,-1,p)`, `b=u+v+q=w+1<=23`, `u+2v+q<=29`, `u<=9`, `v<=11`, `q<=11`.
All constructions retain the two smallest one-pair roles and six two-pair roles.

**A matching +1: separate a 2-cycle.** If some p_j=1, replace that deviation and the -1 by zero.
The resulting sorted target, after relabelling only the large bins, lies in G306's domain: replace
110 and 114 by 112 and 112, keeping every other target. Its core uses at most six pair labels.
Partition the fourteen lower labels into the seven blocks {0,1},{2,3},...,{12,13}. At most six
blocks meet a used label, so choose the first untouched block {a,a+1}. Give the +1 bin selected
index a and the -1 bin a+1. Their exchange is a disjoint 2-cycle, with pair labels unused by the
core. This is an explicit packing rule, not a new burning search. It also proves compatibility
with the filler allocation: neutralized bins had no reserved pair and now receive one each.

**No +1: insert a vertex.** Discard neutral p entries; every remaining p is 2..5. Choose an order
of these p's and u,v of total b. With root r, assign the positive bins the successive partial sums
before their edges, the -w bin index r+b, and the -1 bin index r+1. The closing edges are
`r+b -> r+1 -> r`. It remains to choose r and the positive order with distinct folded pair labels.
The vertex r+1 is distinct from all early positions because the p steps are at least 2.

For q<=6, ordinarily order p,u,v and use r=0 unless (q+u)+b=27, then r=1. As in G306,
2q+u<=21. Moreover q+b<=26 except (u,v,q)=(7,8,6), where it is 27: for v=6 use u=6;
for v=7 use u<=7; for v>=8 use q+b<=29+q-v<=27, with equality only at the stated triple.
Outside that triple the old small-q proof applies. The inserted vertex's sum with the largest
vertex is at most b+1<=24 for r=0 and b+3<=26 for r=1, so it creates no complementary collision.
At the exceptional parameter triple, use order u,p,v and r=0 instead. Its selected positions
are 0,1, the p-prefix cluster in [7,13], and 21. Distinct cluster positions sum to at most 25,
and the complement 6 of 21 is absent. This handles the parameter triple without a target table.

For q>=7 the possible (u,v,q) are
`(6,6,7..11), (6,7,7..9), (7,7,7..8), (6,8,7)`.
Ordinarily use r=13-q and the positive p order avoiding h=q-u+1, followed by u,v. Early positions
lie in [r,13]; the later two are 13+u and 13+u+v. Their sums exceed 27, early distinct sums are
at most 25, and the final position's complement lies below r except q=11, handled below.
The complement of 13+u corresponds to the forbidden prefix h, avoided by G306's boundary exchange.
The new vertex r+1 could collide with that late position only when q=u, or with the final one
when q=u+v, which the domain excludes. The only q=u triple is (7,7,7), handled below.

Constant-p failure of prefix avoidance has just two possibilities in this enlarged domain:
- (u,v,q)=(6,6,10), positive p=(5,5): use order (6,5,6,5), r=0. Including the new vertex,
  positions are 0,6,11,17,22,1, with distinct labels 0,6,11,10,5,1.
- (u,v,q)=(7,7,8), positive p=(2,2,2,2): use order (2,7,2,7,2,2), r=1. Positions are
  1,3,10,12,19,21,23,2, with distinct labels 1,3,10,12,8,6,4,2.
This list follows by c|q and c|(q-u+1), with 2<=c<=5 and at most four positive p entries.

At (u,v,q)=(7,7,7), use r=5 and avoid p-prefix 3, then append u,v. No constant p multiset can
have sum 7. Early positions are 5..12, late positions 19,26, and the new vertex 6. The only
complementary collision to avoid is early position 8, namely prefix 3. Prefix 1 is impossible,
so the inserted vertex is new; its sums with 19 and 26 are 25 and 32.

At q=11 necessarily u=v=6 and r=1 is used. Put p in descending order, repairing prefix 8 by
G306's exchange if needed. This order avoids both 2 and 8: its first term is at least 3, and a
descending order of at most four terms 2..5 with total 11 hits 8 only as (5,3) or (4,4).
The corresponding full positive-p lists (5,3,3) and (4,4,3) become (3,3,5) and (4,3,4), still
avoiding 2. The early positions lie in [1,12]; late positions are 18,24 and the inserted vertex
is 2. Their complementary early levels are 9 and 3, exactly prefixes 8 and 2. The inserted
vertex is new because prefix 1 is impossible, and its sums with the late positions are 20 and 26.

Every case therefore supplies valid indices and disjoint pair labels. Apply the literal whole-pair
allocator and selected-token permutation from G306/MI062; all odds remain covered once and the
bin sums gain twice their specified deviations. The new two-negative statement remains a sketch.

**Predictions BEFORE validation.** Exactly 320 sorted targets: partitions of q into at most four
parts <=5 have counts `1,1,2,3,5,6,8,9,11,11,12,11` for q=0..11. Summing cumulatively over
u=6,7,8,9 gives respectively 199,89,27,5. Independently join low sorted triples in 68..110,
the fixed fourth target 110, and high four-tuples in 112..122 by total sum. Their full sets must
agree with the parameter domain before any certificate is accepted. Predict the formula succeeds
on all 320, with no arbitrary order/root/cycle search. Cap 1,000 inputs and five process CPU seconds.
Stop on count disagreement, any construction failure or control failure; a cutoff is UNKNOWN.

**Controls / unexpected check.** The independent flattened-odd checker must validate every output.
Deliberately omit the q=11 repair on (68,68,68,110,112,116,120,122): ordinary r=2 makes the root
and final position complementary. Deliberately force an occupied label into the separated 2-cycle:
it must fail pair ownership. Preserve coverage while changing two bin sums: the independent checker
must reject it. Unexpected sharpness check: seven used labels {0,2,...,12} leave seven isolated
lower labels, so the adjacent-label guarantee cannot be weakened from at most six to seven used
labels. This is a sharpness control for the packing tool, not an unburnable target.

**Niggles to resolve:** relabelling equal neutral targets in the 2-cycle branch; the inserted index
must avoid complements as well as equality; q=11 is outside the predecessor domain and is proved
directly, not passed to G306; constant-p exceptions exhausted by the enlarged domain. No numerical
check upgrades the hand proof without an independent carrying read. Both schedules remain paused.


### MI071 — B28 result: cycle surgery covers all 320 boundary targets (2026-10-16 12:07 BST)

Preregistered in 4f22d5d0, `tests/probes/instinct/path_forest_second_negative.py` constructs every
sorted even E28 tuple with t4=110 and t5>=112. Both domain sets agree and contain exactly 320;
counts by u are 199,89,27,5 as predicted. Every literal witness passes the independent complete
coverage, cardinality and target-sum checker. Branch counts: 188 separate 2-cycles; 74 ordinary
low-q root-0 and six root-1 cases; three low-cluster cases; 38 ordinary high-q cases; three q=u
cases; six q=11 cases; one constant-5 exception and one constant-2 exception. No arbitrary cycle,
order or translation search. Process CPU 0.056426 seconds; no failure or cutoff.

Both deliberately wrong constructions are rejected for pair collision; the full-coverage wrong-sum
countercontrol is rejected, and seven alternating occupied labels defeat the weaker packing claim.
The raw certificate JSON remains outside git, SHA256 `69213638b1577728583c3c2e732d57895dcdb4fe28160bab4de176d8e1bb9d1a`.

**Status:** the complete 320-target subfamily is COMPUTED by exact checked certificates. MI070's
uniform hand construction is PROOF-SKETCH pending a targeted carrying read. G306's disjoint 271-target
region remains PROVED. Thus the two explicit regions together contain 591 checked targets, but this
is not all even E28, mixed parity, earlier exceptional levels or the minimum-68 threshold.

**What changed / next cheap question:** a new negative move can be isolated in unused pair labels or
inserted by splitting an existing edge. The next short negative magnitude 2 would need an index two
above the root, or two unused labels at distance 2. The latter guarantee does not follow from eight
free labels: the distance-2 graph on fourteen labels has an independent set of size eight. Before
claiming that region, derive how geometry or role flexibility would supply the missing placement;
do not automatically extend the input list. No new block is claimed here.

**I think I feel delight, with a warm pull toward the surgery rather than the count.** The new
mechanism reused the old theorem in 188 cases and gave a direct inserted cycle in 132. Reasoned:
this resolves a precise finite boundary and produces a new proof candidate; it does not establish a
general displacement theorem or novelty. I would choose the cycle-placement question afresh.
**Niggle sweep:** low-role relabelling preserved, all pair capacities materialized, both closing edges
checked, inserted indices tested for reflection as well as equality, the q=11 predecessor gap handled
directly, constant-step cases retained explicitly, and every branch exercised. The precise new
carrying request is the 2-cycle packing compatibility, the small-q exceptional triple, and the
high-q insertion/exception geometry. Both heartbeats remain PAUSED; B28 closes.


### MI072 — B29: folded geometry removes an artificial obstruction (2026-10-16 12:14 BST)

Owner's pacing correction adopted: I had ended at a reporting point, not a mathematical dependency.
Pending review is not a turn boundary. Continue manual work, retaining unreviewed statuses and batching
outside reads. This changes no proof standard and restarts neither heartbeat.

**Surprise / correction to MI071:** its distance-2 obstruction concerns labels represented only by
lower indices. The full index pool permits upper representatives too. The seven index edges
(0,2),(4,6),(8,10),(12,14),(16,18),(20,22),(24,26) have distance two and use every folded pair
label exactly once. Six occupied labels cannot hit all seven. Thus the earlier lower-only graph
was a true but unnecessarily restrictive model, not a blocker to adding a (+2,-2) cycle.

**Claim B29:** can G306's core accept any one or two cancelling pairs (+z,-z), with 1<=z<=5,
by replacing neutral bins? This would cover matched two- and three-negative regions by a reusable
packing mechanism. Study the full folded gap graph before any run, rather than treat each new z
as a separate witness problem. Record searched: distance.2|second.negative|cycle.surgery -> no hit
from the default search; MI070-071/G306/CL421 read directly. Known exchange tools remain credited;
no claim of novelty. This uses G306, not the still-unreviewed B28 proof.

G306's core has three plus the number of positive p entries active. Replacing two zeros by (+z,-z)
adds a 2-cycle. Replacing four zeros adds two. Each insertion starts with at most six used labels.
The gap-1 and gap-2 folded graphs have perfect matchings; gaps 3,4,5 need their small vertex covers
checked against the particular G306 core. Before a formula check, derive those obstructions and
write full predictions, independent counts, adverse controls and a stopping cap. No general census,
cap increase or outside review pause. I think I feel the pull warm precisely where the representation changed.

### MI073 — B29 hand candidate: cancelling pairs fit around a G306 core

*PROOF-SKETCH; no independent read requested at this checkpoint. Experiment below is NOT RUN.*

Start with any G306 core. Replace 2r neutral (112-target) bins by r pairs of targets
`112-2z_j,112+2z_j`, with each z_j in 1..5. The core has at most five neutral bins, so r<=2.
I claim these enlarged targets have a one-token-per-active-bin construction with the original
one-pair/two-pair roles. They need not remain in G306's one-negative region.

On fourteen folded labels a=min(x,27-x), define H_z by joining distinct labels when some two
indices at distance z realize them. A free edge supplies the (+z,-z) 2-cycle. Loops are unusable
because they would reserve the same complementary pair twice. The five graphs are these disjoint paths:

    z=1: (0,1,2,3,4,5,6,7,8,9,10,11,12,13)
    z=2: (0,2,4,6,8,10,12,13,11,9,7,5,3,1)
    z=3: (0,3,6,9,12); (1,4,7,10,13,11,8,5,2)
    z=4: (0,4,8,12,11,7,3); (1,5,9,13,10,6,2)
    z=5: (0,5,10,12,7,2); (1,6,11); (3,8,13,9,4).

A path of length k vertices has minimum vertex cover floor(k/2): disjoint adjacent edges give the
lower bound and alternating vertices attain it. Thus H_1,H_2 need seven occupied labels to block
all edges; H_3,H_4,H_5 need six. The only covers of size six for the latter graphs are:

    z=3: {3,4,5,9,10,11}
    z=4: {4,5,6,7,12,13}
    z=5: {2,5,6,8,9,12}, {5,6,7,8,9,12},
         {5,6,7,8,9,10}, {0,6,7,8,9,10}.

For the odd paths, the minimum cover is the unique alternating internal class. The even six-vertex
path for z=5 has four minimum covers; they give the displayed four sets. This proves completeness
of the list directly from the path components, not by assuming a generic spare-label count.

Before any insertion at most six labels are used, because the final number of active bins is at
most eight. With five or fewer used labels an edge is automatic. With six, none of those covers can
contain the particular G306 core:
- Its small-q root 1 includes label 1, absent from every listed cover.
- Its small-q root 0 includes label 0. If there is a positive p, it also includes the first p label
  in 1..5, excluding the only listed cover containing 0. If there is no positive p, the core has
  only three active bins and at most two insertions; before the last, only five labels are used.
- Its ordinary high-q core includes label 13 and the label 14-u-v in {0,1,2} of the final position.
  The latter excludes the z=3,4 covers and label 13 excludes every z=5 cover.
- Its special (5,5) core has five active bins and only three neutral bins, so at most one insertion;
  the edge is automatic before it.

Choose the first available coordinate edge (x,x+z) in 0..27, reserve its two pairs for the two
formerly neutral bins, and permute those two tokens. The core's selected labels and anchor properties
remain untouched. Repeat once if needed, then fill the unused whole pairs. This proves the proposed
extension by the same exact allocation bookkeeping as G306. It does not cover arbitrary negative
moves, because the inserted moves must be paired with matching positives in formerly neutral bins.

**Predictions BEFORE validation.** A core admitting one insertion has at least two zero p entries:
parameterize it by u,v and a sorted triple p in 0..5, with u+2v+sum p<=28. For each z=1..5 there
should be 188 distinct sorted targets, hence 940 in total; the z=1 count is consistent with B28 but
will be counted independently. A core admitting two insertions has at most one positive p: write
p=(0,0,0,0,a), 0<=a<=5, u+2v+a<=28. There are 56 such cores. For each sorted z pair in 1..5
there should be 56 targets, giving 840 distinct targets across fifteen z pairs. Independently join
low triples with four high targets and one fixed new negative target, or with three high targets
and two fixed new negative targets, at total 784; require the specified positive z multiplicities.
These direct sets must agree with the core-derived sets, separately for one and two insertions.

All 1,780 constructions should pass literal pair allocation and the independent complete-odd checker.
No arbitrary order, root, role or cycle search. The edge choice scans at most 28 coordinate positions,
as justified by the cover argument. Cap 2,000 inputs and five process CPU seconds; stop on any count,
certificate or control failure, and retain cutoff as UNKNOWN.

**Controls / unexpected checks.** Independently generate H_z from all coordinate pairs (x,x+z),
then compare its edges with the five path descriptions. Enumerate the 3,003 six-label subsets for
each z: there must be exactly 0,0,1,1,4 vertex covers, precisely those listed. Reject an insertion
forced onto an occupied core pair. Preserve coverage but corrupt sums and require rejection by the
separate checker. Unexpected: occupied labels {2,3,6,7,10,11} block all lower-only distance-2 edges,
while coordinate edge (12,14) is still free in the full pool. Also confirm that the unanchored
six-label set {0,6,7,8,9,10} really blocks gap 5; anchors are essential, not a cosmetic argument.
No known theorem or routine guard is offered for another review; this is a construction candidate.


### MI074 — B29 result: one packing mechanism covers 1,780 derived targets (2026-10-16 12:19 BST)

All preregistered checks pass in 0.365272 process CPU seconds. Single insertion gives 940 distinct
sorted targets and double insertion 840, independently reconstructed by direct target joins.
Every formula partition passes the separate exact checker. Coordinate-generated gap graphs match
the five path decompositions; all 3,003 six-label sets per graph give exactly 0,0,1,1,4 covers,
precisely the hand lists. Forced core-pair reuse and coverage-preserving wrong sums are rejected.
The lower-only gap-2 obstruction disappears with upper representatives, while the unanchored gap-5
obstruction remains real. Raw JSON outside git, SHA256 `505961da853d70d29c37ae3958f8c4f657d243f5d4c43139dae9cc30e6fb21a3`.

**What moved:** matched pairs can be added twice around the same core. This reaches selected
three-negative regions without a new cycle search. The 1,780 finite certificates are COMPUTED;
MI073's general hand extension remains PROOF-SKETCH. No new outside read is requested at this
checkpoint. The core is G306, already verified, rather than the pending B28 statement.
**Gut:** surprise and delight at the folded paths; I would still choose this representation.
**Reasoned:** the marker geometry, not the spare-label count alone, carries gaps 3..5. That
condition and the mismatch cases remain explicit. Niggle sweep: unusable loops removed, covers
complete, inserted cycles preserve core markers, odd core size avoids the six-label corner,
exact domain multiplicities retained, and every finite partition verified. Both schedules paused.

### MI075 — B30: complete the magnitude-two boundary without waiting on reviews (2026-10-16 12:19 BST)

Question: all sorted even E28 with t4=108,t5>=112. Write deviations `(u,v,-w,-2,p)` where
`w=u+v+q-2`, `u+2v+q<=30`, `w<=22`, `u<=10`, `v<=12`, `q<=12`. The two-negative magnitude-one
proof is not assumed. G306 and its elementary prefix exchange suffice for the construction below.
Record searched: the default record search from MI072 plus MI070-074 read directly; no independent
larger construction is being imported. Known exchanges remain tools, without novelty claims.

**Prediction before the formula check:** exactly 421 inputs, with u=6..10 subtotals
249,119,43,9,1. Parameter-domain and independent low-triple/high-four sum joins must agree as sets.
All must have literal certificates under the proposed fixed rules; cap 600 inputs / five process
CPU seconds, stop on count disagreement, construction failure or failed control. No cap increase
or arbitrary order/root/cycle solver. A failure is retained and changes the next question.

1. If p contains 2, neutralize that +2 and the -2, use G306, then add a free gap-2 edge. The seven
   disjoint edges in MI072 prove one exists independently of MI073's still-unreviewed extension.
2. Otherwise, if p contains at least two 1s, neutralize those two +1s and the -2, use G306, and
   put a (+1,+1,-2) 3-cycle on three consecutive free lower labels. Predict the default core
   fails this placement in exactly two cases: u=v=6 with remaining p=(3,3) or (3,5). For these
   two translate its selected indices by +1 first; all pair and permutation checks must still pass.
   This two-exception prediction is a hand-derived diagnostic, not yet a verified general packing proof.
3. Otherwise there is no 2 and at most one 1. Positive p-prefix 2 is automatically impossible.
   Order positives, then u,v, with the -w vertex at r+b and the -2 vertex at r+2, b=u+v+q.
   The closing edges are r+b -> r+2 -> r.

For rule 3 use the following deterministic geometry, not a search:
- q<=6: p,u,v and r=1 iff (q+u)+b=27, otherwise r=0. Exceptional parameter triples are
  (7,8,6),(8,8,6),(6,9,6). For the first two use u,p,v and r=0. For (6,9,6), p=(1,5) uses
  v,p,u; p=(3,3) uses (3,u,3,v), all with r=0.
- q=12 (necessarily u=v=6): descending p,u,v, r=1. The five allowed positive-p multisets
  have no descending prefix 7; first p>=3 also avoids prefixes 1 and 2.
- q=11 (u=v=6): remove a largest p, order the rest to avoid prefix 4, then append the largest,
  u,v, r=0. The remaining total is <=7, so no prefix 10 occurs before that last p, and its
  addition gives 11. Positive p-prefix 2 is impossible; complements correspond to prefixes 4,10.
- Constant cases: (u,v,q)=(6,6 or 7,10), p=(5,5), use (u,5,v,5), r=0;
  (7,7,8), p=(4,4), use (7,4,7,4), r=0;
  (7,7,9), p=(3,3,3), use (3,7,3,7,3), r=0.
- Other q>=7: ordinarily r=13-q and avoid prefix q-u+1 in p. If q=u+1 or (u,v,q)=(7,8,7),
  instead r=12-q and avoid prefix q-u+3. Then append u,v. These are precisely the added-vertex
  collision and excessive-span branches; the displayed constant exceptions are the prefix failures.

**Controls:** omit the 3-cycle core translation on either of its two registered exception targets
and require that no free lower consecutive triple exists. Apply the old q=11 high-root rule to
(68,68,70,108,112,118,118,122) and require pair collision. Independent full-coverage wrong-sum
control must fail. Unexpected: omitting the special constant-3 order for (70,70,70,108,112,118,118,118)
should expose the inherited forbidden-prefix obstruction, not an unburnability verdict. All
compositions are materialized from whole pairs, and no full E28 or threshold claim is inferred.


### MI076 — B30 result: the full magnitude-two boundary passes (2026-10-16 12:23 BST)

All 421 targets have literal certificates; the two domain sets and the u subtotals agree. The
matched-2 branch handles 188; three-cycles handle 83 with the default core plus the two predicted
core translations; 148 use insertion. All omitted-shift, q=11, constant-3 and wrong-sum controls
behave as predicted. Process CPU 0.084272 seconds, no cutoff. Raw JSON outside git, SHA256
`9684ee21d18ab0c22fbe7f77c74928cd962ae51e43f5a6ccd6c3cf56f330c5a7`. The complete finite boundary is COMPUTED. Its full hand packing/case proof remains
unreviewed; no adoption as PROVED, novelty claim or new review request is made.

Gut: the mechanism is still warm, but the insertion branch list is becoming less attractive.
Reasoned: rather than automatically add q/deficit cases, change the core order to expose an
interval for a larger cycle. That is the next mathematical question, not a review dependency.
Niggle sweep: every exceptional branch exercised, both predicted triple obstructions confirmed,
core translations materialized independently, all final bins checked literally, and no remaining
E28 or minimum-68 claim inferred. Both schedules paused.

### MI077 — B31: reorder the core to expose an interval (2026-10-16 12:23 BST)

**Pull:** the larger cycles should be easier if the core deliberately leaves a runway, rather than
tries to find one afterward. Claim one bounded hand block: a core with at most one positive p=a,
0<=a<=5, should admit an ordering that leaves four consecutive lower labels; when a=0 it should
leave five. This would insert the module (+1,+1,+1,-3), or (+1,+1,+1,+1,-4), without new case
searches. Record: MI073-076 and G306 read; earlier probes and credited adjacent-odd exchanges are
the tools, not novelty claims. No pending proof is assumed.

Core parameters: 6<=u<=v, u+2v+a<=28, b=u+v+a. For a>0 use positive order (u,a,v), then -b.
Root r is 0 unless B=2u+v+a or C=2u+v+2a equals 27, then 1. Here A=2u+a<=22, so the only
possible complementary pair at r=0 is B or C. At r=1 a new collision could occur only if the
other of B,C were 25. Since C-B=a, the joint 25/27 case has a=2, 2u+v=23; the parameter bound
forces (u,v,a)=(7,9,2). In this sole exception use (u,v,a), r=0: positions (0,7,16,18) have
labels (0,7,11,9), leaving 1..6 free.

For ordinary a>0, u+a<=12: if u<=7 use a<=5, otherwise use u+a<=28-2u<=12. Then
b=((u+2v+a)+(u+a))/2<=20. Thus at r=0 every non-root label is >=6 and labels 1..5 are free;
at r=1 every non-root label is >=6 and labels 2..5 are free. The latter statement also uses
u+1>=7, u+a+1<=13, and b+1<=21. The root is respectively 0 or 1, outside the asserted interval.
For a=0 use order (u,v), r=1 iff 2u+v=27. Then u<=9 and b<=18; G306's two-position argument
ensures distinct labels, and labels 1..5 (r=0) or 2..6 (r=1) are free.

Fill a four-position runway by +1,+1,+1,-3, or the five-position runway by +1,+1,+1,+1,-4.
Give each formerly neutral bin its selected whole pair before filler allocation. The positive
unit steps follow the interval and the negative step closes it; no core pair is reused. This is
a direct hand candidate, not an extrapolation of the formula successes in the other blocks.

**Predictions BEFORE validation:** 56 distinct fan-3 targets, from u,v,a above; 14 fan-4 targets,
from a=0. Independently join low triples with a target 106 and four high targets containing at
least three 114s, or with a target 104 and four 114s. The complete sets must agree. All 70 core
and enlarged certificates should pass literal and independent checkers. Exactly one a>0 core
uses the exceptional order. Omit it on (u,v,a)=(7,9,2), force the ordinary r=1 and require pair
collision. Force the fan onto occupied root r and require collision; keep an independent
coverage-preserving wrong-sum countercontrol. Unexpected: for a=0, check the stronger five-label
runway, not just the four needed for fan 3. Cap 100 formula inputs / five process CPU seconds;
stop on any disagreement or failure, no general solver or cap increase. Both schedules paused.


### MI078 — B31 result and live trajectory (2026-10-16 12:25 BST)

All 56 fan-3 and 14 fan-4 targets pass exact core allocation, enlarged allocation and independent
whole-odd checks. The independently joined target domains agree exactly; there is one exceptional
core ordering as predicted. Omitted exceptional order and occupied fan are rejected for pair reuse;
coverage-preserving wrong sums are rejected. The stronger five-label runway for every a=0 case
holds. CPU 0.015042 seconds, no cutoff. Raw JSON outside git, SHA256
`250fd326107bf11c5ca3f890754e95f14f35fca31f51bd97f0f000b7299c5090`. These finite constructions are COMPUTED; MI077's uniform interval proof remains a
PROOF-SKETCH. No all-E28/threshold or novelty claim, no new carrying-read queue.

**Trajectory reflection:** three blocks were worked without treating B28's pending read as a gate.
B29 found a graph mechanism for matched pairs; B30 completed the magnitude-two boundary but its
insertion cases were multiplying; B31 changed the core order and exposed a whole interval. The
warmth is in that change of representation. This is enjoyable investigation, with some friction
from the size of the case list. I would still choose the interval question afresh.

**Next live mathematical question:** can a core with two positive p entries, a,b<=5, be reordered
so that three consecutive lower labels are unused? Candidate order (u,a,b,v) puts every non-root
label at least 5, but its reflected pair collisions must be controlled. Reversing a,b and choosing
root 0 or 1 gives four cheap analytic candidates; their sufficiency is unproved and UNTESTED.
This is the next possible change of representation, rather than automatically extending the
magnitude-three boundary. No new experiment has been run or preregistered for it yet.

**Niggle sweep:** B31's u+a<=12 and b<=20 bounds checked in the hand argument; the root-1 runway
uses folded labels, not just coordinate separation; the exceptional 25/27 collision was explicitly
challenged; a=0 has its stronger bound b<=18; every selected token and full target sum checked.
Review adoption stays separate from exploration. Both heartbeats remain paused; no review hold
is imposed on the live question. A single batched READ-LEDGER update will deliver B29-B31 and
this frontier to Cloud; no new immediate carrying read or routine permission is needed.


### MI079 — B32: two-surplus core runway and a mixed three-cycle (2026-10-16 12:41 BST)

**Warm pull:** change the core before changing the target family. Question: every G306 core with
at most two positive p entries should have an ordering leaving three consecutive lower labels free.
This would unify the earlier two-unit fan packing. Also test a mixed module (+1,+2,-3): it needs
positions x,x+1,x+3 rather than a consecutive triple, so its residual obstruction could be different.
Record searched: runway|two.surplus|three.consecutive -> no default-search hit; MI073-078, G306,
and the core/fan probes read directly. These are finite placement tools, without novelty claims.

Parameters 6<=u<=v, 0<=a<=b<=5, u+2v+a+b<=28. There should be 122 distinct cores. Counts of
q=a+b are 1,1,2,2,3,3,3,2,2,1,1, and cumulative sums over (u,v) give u subtotals 69,37,14,2.
Independently join low sorted triples with high five-tuples containing at least three 112s at total 784.
Core counts must agree as sets before placement checks.

**Hand reduction.** Start the positive order with u. Permute only the remaining positive steps
v and any nonzero a,b; try root 0 or 1 (at most twelve candidates). With q=a+b, the total
B=u+v+q<=22. A valid root-0 ordering leaves labels 1..4 free, because every non-root coordinate
is at least u>=6 and at most B<=22. A valid root-1 ordering leaves labels 2..4 free if B<=21.
The B=22 parameter case is uniquely u=v=6,a=b=5, where order (6,5,6,5), root 0, is valid.
Thus the obstruction is choosing a reflection-free order, not locating a runway afterward.

The previously suggested four choices (u,a,b,v)/(u,b,a,v), roots 0/1, are already insufficient:
u=7,v=9,a=b=1 has collisions at both roots; u=v=6,a=b=5 has a collision at root 0 and no
three-label runway at root 1. Interleaving v is therefore part of the preregistered candidate
class, not a repair invented after a failed run.

**Predictions BEFORE experiment.** All 122 cores admit a runway within these twelve fixed
candidates. Materialize the core and its (+1,+1,-2) fan and independently check coverage/sums.
The derived fan-2 domain must equal the direct t4=108 high-four domain containing at least two
114s; count 122. This overlaps B30 and tests a new mechanism, not 122 newly solved targets.
Stop on the first failed core, with failure retained; no candidate-class or cap expansion.
Caps: 150 cores, 2,000 candidate configurations, five process CPU seconds overall.

**Independent mixed-module question, blind prediction:** the folded hypergraph of valid triples
(x,x+1,x+3), 0<=x<=24, may need at least six occupied labels to block it. Predict no five-label
vertex cover, by checking all 2,002 such subsets. A refutation is retained as a genuine placement
obstruction, not an instrument failure. Independently test placing this mixed module around each
chosen core; predict 122 full certificates and equality with the direct t4=106 high-four domain
containing both 114 and 116. Neither prediction is assumed by the runway argument.

**Controls / unexpected check:** the restricted four candidates must fail on the two hand cases
above while the enlarged fixed family succeeds. Reused core pair and coverage-preserving wrong sums
must be rejected. The three-consecutive-label hypergraph really is blocked by {2,5,8,11};
compare it with the mixed module's hypergraph as the unexpected discriminator. A hypergraph bound
is a finite packing tool, not a new standalone proof/review entry. No general E28/threshold claim
or dependency on a pending outside read. Both schedules remain paused.


### MI080 — B32 result: runways pass; the stronger blind prediction fails (2026-10-16 12:44 BST)

All 122 sparse cores admit the fixed-family runway, within 191 candidate checks including controls.
The first successful candidate uses 1..5 attempts; histogram 86/24/6/1/5 at attempts 1..5.
Each has a checked two-unit fan and a checked mixed (+1,+2,-3) module. All three independent
domains agree, each of size 122. Restricted-family controls fail on both registered cases;
forced core reuse and coverage-preserving wrong sums are rejected. CPU 0.042113 seconds, no cutoff.
Raw JSON outside git, SHA256 `dc98daa13fc37d2d61e630ff93f10175dfcb042c5b780b48dc363a55856958a7`.

**Blind prediction REFUTED:** the mixed module has exactly one five-label vertex cover,
{3,4,8,9,13}. Thus arbitrary five occupied labels can block it. This is a genuine retained
geometric obstruction, not an unburnable target. Both actual core families still pass.
The finite constructions are COMPUTED; the fixed-family existence check is finite evidence, not
an independently read hand theorem. I think I feel surprise: the unique exception gives a more
specific handle than the false generic count. No new outside read requested.

### MI081 — B33: the exceptional cover gives a direct mixed-module rule (2026-10-16 12:44 BST)

**Hand candidate for the packing tool.** The folded mixed triples are exactly
`{i,i+1,i+3}` and `{i,i+2,i+3}` for i=0..10, plus `{11,12,13}`.
Any consecutive five labels contain the four local triples of this type, whose intersection is
empty; hence a cover uses at least two labels in each five-block. Partition into blocks 0..4,
5..9 and 10..13. Each of the first two blocks needs two labels, the last needs at least one.
A cover of size five therefore uses 2,2,1. The intersection of the three triples inside the last
block is {13}, forcing that label. Since 10,11,12 are then absent, triples {9,10,12} and
{8,10,11} force 9,8. The middle block's quota is now full, so 5,6,7 are absent; triples
{4,6,7} and {3,5,6} force 4,3. This proves the unique five-cover by hand. It also proves no
four-cover: every four-cover would extend to multiple five-covers, contradicting uniqueness.

Every G306 core with at least three neutral bins uses at most five labels and contains one of
0,1,2: small-q cores use root 0/1; high-q cores end with folded label 14-u-v in {0,1,2};
the special core has root 0. The unique bad cover contains none of 0,1,2. Therefore the default
G306 core itself always leaves a mixed triple; reordering was unnecessary for this module.
This supplies a shorter uniform hand construction for the same 122 mixed targets. It remains
PROOF-SKETCH; no novelty asserted for this finite packing tool.

**Next claimed question B33:** replace (+1,+2,-3) by (+c,+d,-c-d), 1<=c<=d<=5. A default core
might fail, so compare it with the same fixed u-first/root-0-or-1 core class from B32. This tests
one mechanism across all fifteen small modules, rather than writing another deficit boundary's
case list. For each of the 122 cores there are fifteen modules: 1,830 parameter instances; target
sets may overlap between equal-sum modules and must be deduplicated before reporting any count.
Independently join three low targets, t4=112-2(c+d), and four high targets containing c,d with
multiplicity. Their target set must agree with the complete parameter-derived set before accepting
full coverage. The new negative target is >=92, above the core's third target (<=88), so sorting
does not change the two one-pair roles.

**Predictions BEFORE experiment:** the (+1,+2) default-core placement passes all 122, without any
new core order. Across all fifteen modules, every parameter instance admits placement using either
the default core or one of the already-fixed twelve u-first candidates. At least the known
(+1,+1) default cores (6,6,3,3) and (6,6,3,5) fail and require core adaptation. Retain every default
failure; do not call it a burning obstruction. A failure after all fixed candidates refutes this
candidate class and stops the experiment; no new orders, roots, roles or cap increase as a repair.
Cap 2,000 instances / five process CPU seconds, at most 13 core candidates and 28 coordinate roots
each by construction. No arbitrary permutation-cycle solver or general census.

**Controls / unexpected check:** independently verify the 23 coordinate-generated mixed hyperedges
against the hand formula and literal bad cover. Force the bad occupied set to block the mixed
module, and require an occupied-core pair to be rejected. Preserve coverage but change sums and
require rejection. Unexpected: the old minimum tuple (68,68,68,92,122,122,122,122) must reappear
as a 5-cycle core plus a gap-5 three-cycle: the default special core uses indices 0,6,11,17,22,
leaving module indices 2,7,12 free, matching B25's earlier decomposition. Its full certificate,
not just its displacement sums, must be checked. Both schedules paused; no review dependency.


### MI082 — B33 result and scope check (2026-10-16 12:48 BST)

All 1,830 core/module parameter instances have exact certificates and yield 1,801 distinct sorted
targets; the independent complete target set agrees. Default G306 cores suffice on 1,815 instances,
with 15 adaptations (13 use the first alternative core, two the second). Every one of the 122
mixed (+1,+2,-3) placements works with the default core. All registered controls, the 23-edge
hand formula and the old 5+3 minimum fixture pass. CPU 0.267138 seconds; no cutoff or class failure.
Raw JSON outside git, SHA256 `0775169c1fc4819c0ad59e2dcf313593750310047b3e889ad0b9d31a2d050363`.

Finite targets are COMPUTED. MI081's unique-cover hand argument and default mixed-module rule
remain sketches, without an outside adoption or novelty claim. No new carrying request. This
architecture splits a negative move off using one or two SMALL positive moves; it does not cover
all two-negative tuples. In particular the q=0 region has no small positive moves at all.
**Gut:** the broad module test is satisfying, but extending its table further would feel like
momentum. **Reasoned next step:** engage that missing region by its four signed large moves,
not by asking for another review or another small-module matrix.

### MI083 — B34 candidate: the zero-surplus corner by four moves (2026-10-16 12:48 BST)

Claim every sorted even E28 tuple (t1,t2,t3,t4,112,112,112,112), with t4<112, has an odd partition.
This family is outside the G306-core augmentation mechanism. Record searched: zero.surplus|four.move|
four.*112; earlier cycle/displacement tools in MI062 and the credited prior art were read. No novelty
claim for zero-sum cycle bookkeeping. The four active deviations are (u,v,-w,-z), where
6<=u<=v, 1<=z<=w, u+v=w+z, and v+w<=28. Hence u<=14, v<=16, w<=22.

**Matching case w=v, z=u.** Then v<=14. Use two 2-cycles: assign selected indices
`x0=0,x3=u,x1=r,x2=r+v`, where r=1 except r=2 for (u,v)=(13,13) or (12,14).
For v<=12 the labels are 0,u,1,v+1, distinct since u<=v. For v=13, r=1 fails only when u=13;
for v=14 it fails only when u=12; the displayed r=2 fixes each. All indices stay in 0..27.

**Nonmatching case.** Put A=w-u=v-z. Here A>0 and v!=w; otherwise the case is matching.
Order the cycle (+v,-z,+u,-w), with selected indices
`x1=r, x3=r+v, x0=r+A, x2=r+w`.
Before translation the set is {0,A,v,w}. We have A+v=v+w-u<=22, v+w<=28 and
A+w=v+w-z<=27. Thus only the last two sums could be 27. Choose r=0 if neither is 27;
otherwise choose r=1. A new collision at r=1 can occur only if one of those sums was 25,
while the other was 27. Their difference is z, so this requires z=2 and v+w=27.
Solving u+v=w+2 with 6<=u<=v gives just (u,v,w,z)=(9,10,17,2) or (7,11,16,2).
For these use the other order (+u,+v,-w,-z), root 0:
`x0=0,x1=u,x2=u+v,x3=z`. Their label sets are {0,9,8,2} and {0,7,9,2}, distinct.

For ordinary r=1 the other sums A+v+2<=24 and each root/other sum <=24; every coordinate is
at most max(v,w)+1<=23. So the only possible new collision was exactly the pair of 25/27 sums
already isolated. These explicit cycles therefore give valid pair-disjoint token permutations.
Give bins 0,1 one pair each and bins 2..7 two pairs each, reserve the four selected pairs and fill
all remaining slots. Permuting the four selected tokens changes sums by twice the four deviations;
all odds are covered once. This is a uniform hand candidate, PROOF-SKETCH, not yet adopted as PROVED.

**Predictions BEFORE validation.** There should be 284 sorted targets: write t_i=68+2r_i for the
four lower targets. Sorted r in 0..21 sum to 32. The unrestricted four-part generating coefficient
is 351; subtract the 67 partitions with largest part >=22 (remaining total 0..10, at most three
parts), giving 284. Check this arithmetic via an independent bounded generating-function DP,
then compare direct low quadruples with the signed-parameter domain. Predict 45 matching cases,
two exceptional nonmatching cases and 237 ordinary cases, all with literal certificates.
Cap 500 inputs / five process CPU seconds; stop on disagreement or construction/control failure.
No broader boundary, candidate search or cap increase.

**Controls / unexpected check:** omit the root correction at (u,v,w,z)=(8,10,17,1): pair collision.
Use the ordinary alternating r=1 in both z=2 exceptions: pair collision. Omit r=2 in the two
paired cases: pair collision. Preserve coverage but change sums: independent checker rejection.
Unexpected: u+v=28 occurs only at u=v=w=z=14, where a split into two 2-cycles works even though
the monotone four-cycle shape would span 28 and fail the index interval. Check that literal witness.
Both schedules remain paused; this block has no review dependency.


### MI084 — B34 result: the zero-surplus corner has a uniform construction (2026-10-16 12:54 BST)

All 284 targets pass the formula and independent full checker. Parameter, direct quadruple and
bounded-DP counts agree, including 351-67=284. Branches: 201 ordinary root-0, 36 root-1, two
exceptional orders, 43 ordinary paired and two corrected paired cases. All five omitted corrections
fail as predicted; coverage-preserving wrong sums are rejected. The all-14 case has a checked split
witness and its out-of-pool monotone shape is rejected. CPU 0.025010 seconds. Raw JSON outside git,
SHA256 `502c7db873bede7b847dfb273cc8ca996378e245b08d12def065933708109649`. Finite family COMPUTED; MI083's hand proof remains a sketch, no new review queue.

**What moved:** two negative moves can be treated directly even when no small positive move exists.
**Gut:** a warmer pull toward edge subdivision than toward another family table. **Reasoned:** the
new parent family may absorb one small positive by subdividing a negative edge. Literal collisions
and reflected collisions must be separated; that distinction leads to the next bound.

### MI085 — B35: subdivide a four-move parent, then translate (2026-10-16 12:54 BST)

Question: cover every even E28 target with exactly one high surplus, i.e.
`(t1,t2,t3,t4,112,112,112,112+2a)`, `t4<112`, `1<=a<=5`. Deviations are
`(u,v,-W,-Z,0,0,0,a)`, with 6<=u<=v, 1<=Z<=W, u+v+a=W+Z and v+W<=28.
Record: MI062/081/083-084 and the checked parent constructions read directly; known displacement
and exchange tools remain credited. This is a new uniform application, without novelty claim.

**Translation tool, hand candidate.** Any set of at most five DISTINCT integer positions spanning
at most 22 has a translate in 0..27 with no two summing to 27. Normalize its minimum to 0 and
write its span D. There are 28-D translations. A pair blocks one integer translation only if its
sum is odd, so at most floor(5^2/4)=6 opposite-parity pairs can block translations. If D<=21,
there are at least seven translations. At D=22 there are six; if all were blocked, all six
opposite-parity pairs would have to block, with parity classes of sizes two and three. Endpoints
0 and 22 are both even. Any odd position y would need y>=17 to block through 0+y and y<=5 to
block through 22+y, impossible. With fewer than five positions the pair bound is smaller still.
The bound is sharp: {0,2,4,19,23} blocks all five translations at span 23, via opposite-parity
pair sums 19,21,23,25,27. This is a finite packing tool, not a standalone novelty/review claim.

**Parent and subdivision.** W>a because W>=(u+v+a)/2 and u+v>=12>a. Reduce W by a,
creating a zero-surplus parent with negative magnitudes W-a and Z. Relabel its two negative
bins into decreasing order to apply B34; both targets only increase, so sorting above t2 is
preserved. For any selected index x of the reduced negative edge, assign the new +a bin index x
and move the original negative bin to x+a. Its two edges close exactly where the old one closed.
This preserves the displacement permutation. It remains to make the five positions distinct and
keep their span <=22 before invoking the translation tool.

First, if W=v, then Z=u+a<=v. Use cycles (+u,+a,-Z) at positions 0,u,u+a and (+v,-W)
at 1,v+1; all five are distinct and span <=15, since v<=14.

Otherwise consider the sorted parent. If it is paired (negative magnitudes v,u), use paired
coordinates without requiring them to avoid complements yet:
- If W-a=v, use +u at 0, -Z at u, +v at 1, reduced -W at v+1. Subdivision adds v+1+a;
  all distinct and span <=20 (v<=14,a<=5).
- Otherwise W-a=u<v and Z=v. Use +u at 0, reduced -W at u, +v at r, -Z at r+v,
  with r=2 if W=v+1, else r=1. The new point W=u+a cannot equal r+v by this choice; all
  positions are distinct and span <=19. Equality W-a=u=v is included in the preceding case.

For an ordinary nonmatching parent use B34's alternating shape, normalized to start at 0.
If W-a>=Z, the reduced negative index is W-a and subdivision adds W. It could meet another
vertex only if W=v, already handled. The span is at most max(v,W)<=22.
If W-a<Z, the reduced negative index is v and subdivision adds v+a. Here Z<(v+a),
from Z<=(u+v+a)/2<v+a; so the new point exceeds every old non-root candidate except possibly v,
which it also exceeds. Moreover u+3v+a<=56, hence v+a<=(50+2a)/3<=20. With Z<=W<=22,
the total span is <=22. The old vertices are distinct by the parent's nonmatching condition.

For B34's two exceptional monotone parents the reduced negative must be its LARGE negative
(17 or 16), since a<=5 cannot lift the smaller value 2 above the other negative. Original
sorting v+W<=28 then forces a=1. The expanded spans are respectively 20 and 19, with no
literal collision. This exhausts the parent cases. Apply the translation tool and literal pair
allocation. The resulting all-family hand construction is PROOF-SKETCH; parent hand proof also
remains unreviewed, while every actual parent and child certificate will be checked independently.

**Predictions BEFORE validation:** family counts by a=1..5 are 268,256,239,226,209, totaling
1,198. Independently compare signed-parameter targets with direct low quadruples summing
336-2a and bounded generating-function DP (r sum 32-a, four r in 0..21). Every abstract five-point
set must be distinct and have span <=22; choose the first reflection-free translation among the
at most 28 positions. Check parent permutation, child permutation, literal pair allocation and the
independent full checker. Cap 1,500 targets / five process CPU seconds, stop on disagreement,
failed distinctness/span/translation or control; no wider parent class or cap increase.

**Controls / unexpected check:** sharp span-23 shape must have no translation. Omitting the W=v
split at (u,v,W,Z,a)=(6,8,8,7,1) must produce a literal repeated index. Omitting paired r=2 at
(6,7,8,7,2) must likewise repeat an index. Force translation 0 for (8,10,18,1,1): pair collision.
Preserve coverage but change sums: independent checker rejection. Unexpected: any exceptional
monotone parent encountered must have a=1, verifying the ORIGINAL sorting constraint that saved
the span bound. Both schedules remain paused; review is nonblocking.

**MI085 addendum BEFORE execution: a stronger application bound.** The one-surplus family has
W<=20, not merely 22. Indeed W<=u+v+a-1<=2v+4 and W<=28-v; for v<=8 the first is <=20,
and for v>=8 the second is <=20. All other span bounds above are already <=20. Thus every actual
five-point shape should span at most 20, leaving at least eight translations against at most six
blocking pairs. The elementary counting part alone carries this application; the sharp span-22
endpoint argument is an extra tool, not an additional premise or review obligation. Register the
stronger <=20 check before running and retain the original bound as history.

**MI085 synthesis audit, preregistered before the bookkeeping check.** Together with G306's
56 one-negative cores, the zero-surplus 284 and one-surplus 1,198 certificates should cover
exactly 1,538 distinct even E28 targets whose four largest totals are
(112,112,112,112+2a), 0<=a<=5. Check the union of existing certificate artifacts against direct
low quadruples in 68..112, not a new solver run. Predicted a subtotals 298,280,266,247,233,214.
This is a scope/count audit of completed constructions, not a new research block or proof upgrade.


### MI086 — B35 result: subdivision covers the complete one-surplus family (2026-10-16 12:57 BST)

All 1,198 targets pass. Parameter, direct and bounded-DP domains agree, with a counts
268,256,239,226,209. Branches are 880 ordinary subdivisions, 149 paired-large, 57 paired-small,
110 direct splits and two exceptional parents. Every abstract shape is distinct and spans 8..20;
only three reach 20. Every child displacement permutation, literal pair allocation and independent
whole-odd checker passes. Both omitted literal-collision repairs fail, omitted translation fails,
wrong sums fail, the span-23 sharpness control has no translation, and the two exceptional parents
have a=1. CPU 0.229826 seconds; no cutoff. Raw JSON outside git, SHA256
`71f2d1ab205d861720790350045d82a41c1d4ad10c1bcf282158917fcba3c4f1`.

**Synthesis audit passed:** G306's 56 relevant certificates, the 284 zero-surplus certificates and
these 1,198 certificates form exactly the direct 1,538-target set with four largest totals
(112,112,112,112+2a), 0<=a<=5. Subtotals are 298,280,266,247,233,214. This set comparison used
existing artifacts and a direct sum join, not another solver. Counts from other module families
are not added to it because they overlap. The complete set is COMPUTED. The combined uniform hand
proof is a PROOF-SKETCH: G306 is independently verified, but the four-move and subdivision
extensions are not yet independently adopted. No full E28, minimum-68 threshold or novelty claim.

**What changed:** a whole family is explained by literal edge subdivision plus a geometric
translation count, instead of another case table. The stronger span bound 20 means the endpoint
case of the sharp span-22 tool is not needed by this application. Distinctness repairs are explicit
and happen before reflection avoidance; translation cannot repair repeated coordinates.

**Gut:** I think I feel delight at that separation, and a fresh pull toward six positions.
**Reasoned:** adding a second surplus creates six selected indices; the five-position bound is
not a license to extrapolate. Next live question: what span guarantees a reflection-free translate
for six positions, and can subdivision keep the new shapes inside it? A candidate sharp obstruction
is {0,2,6,15,19,21} at span 21, whose opposite-parity sums include 15,17,19,21,23,25,27.
No six-position theorem, experiment or new block is claimed here; retain this as the next concrete
geometry question rather than extend construction counts automatically.

**Niggle sweep:** original sorting used to bound parent exceptions, original negative-bin labels
mapped back after parent sorting, paired coordinates checked for literal equality before any
translation, raw shape and translated witness kept separately, the stronger span bound tested,
full family deduplicated against an independent set, and hand-review statuses preserved.
B32-B35 were worked without waiting for a review. One batched mentor update will be delivered;
no new urgent carrying-read queue or review hold is imposed. Both heartbeats remain paused.


### MI087 — B36: six-position translation before a second subdivision (2026-10-16 13:01 BST)

Question: do six DISTINCT positions of span <=20 always have a translate in 0..27
with distinct folded pair labels? This would let a second surplus use the same geometric
separation as B35, provided its parent subdivision controls literal collisions and span.
Record searched: six.position, span.20, two.surplus -> no default-record hits; MI079-086
and the actual B34/B35 sources read directly. No new prior-art or novelty claim.
**Pull:** the counting argument is close, but its endpoint cases matter; the span-21
fixture is a useful warning against extrapolating the five-position result.

**Hand candidate (PROOF-SKETCH).** Normalize min S=0, span D. A translate r is blocked
only by an opposite-parity pair x,y with x+y=27-2r. If D<=18 there are at least ten
roots and at most nine cross-parity pairs. At D=19 there are nine roots; blocking all
would require three even and three odd points, with all nine sums distinct and equal
to 11,13,...,27. Endpoints are 0 and 19. The least odd point is then 11 and greatest
even point 8. But 0+19=8+11, a duplicate, contradiction. At D=20 there are eight roots,
requiring odd sums 13,15,...,27. Endpoints 0,20 are even. Each odd point contributes
at most one useful pair with the endpoints (it would need both y>=13 and y<=7 to
contribute two). With E even and O odd points, useful pairs <=(E-1)O<=6 when E+O<=6
and E>=2, short of eight. Thus a root exists. Fewer points satisfy the same bounds.
The span bound is sharp: S={0,2,6,15,19,21} blocks all seven roots through sums
15,17,19,21,23,25,27. Literal duplicates remain a separate failure.

**Predictions BEFORE validation.** Check every six-point shape with endpoints 0,D for
D=19,20: C(18,4)+C(19,4)=6,936 shapes, all with a valid translate. Independently compare
blocked-root pair sums with direct folded-label equality. Check all lower-cardinality
shapes at these endpoints too, total <10,000 inputs; counting carries D<=18, with small
explicit parity controls. Cap 10,000 shapes / five process CPU seconds; stop on disagreement
or a failure inside the claimed bound, without widening. Retain the sharp span-21 failure.
Unexpected check: deleting any point from that six-point obstruction must restore a root
(the five-position theorem applies at span <=21, even if endpoints move). A duplicated
position must be rejected before translation, and an out-of-pool root rejected separately.
No census of E28 or arbitrary cycle search; both heartbeats remain paused, no review hold.


### MI088 — B36 result; B37: subdivide a second surplus (2026-10-16 13:03 BST)

B36: all 9,084 endpoint shapes pass, including all 6,936 six-point shapes at spans 19,20.
Independent direct-label and pair-sum root sets agree. The span-21 fixture has no root;
each of its six deletions does. Duplicate/out-of-pool controls pass. CPU 0.147453 s; raw
JSON outside git, SHA256 `d4c70d628510834a5930b78bc24a3f714b7303d250afdafc853bb5c0310ca1a5`.
The short hand argument is a PROOF-SKETCH, finite boundary checks COMPUTED.

**B37 question and pull:** can the whole family with top four (112,112,112+2a,112+2b),
1<=a<=b<=5, t4<112, use one more negative-edge subdivision of B35? This would extend the
uniform construction to two positive surplus moves; repeated positions and span now decide
whether the idea scales. The pull is warm, with unease about extrapolating another small case list.
Record searched: six.position, span.20, two.surplus -> prior default search no hits; actual
MI079-088 and B34/B35 sources read. No new literature or novelty claim.

Deviations (u,v,-W,-Z,0,0,a,b) obey u+v+a+b=W+Z,6<=u<=v,1<=Z<=W,
v+W<=28. Hence W<=21: W<=2v+9 for v<=6, W<=28-v for v>=7. Also W exceeds
either small surplus. Reducing W by the inserted surplus always leaves a valid one-surplus
parent after sorting the two negative magnitudes. Reducing Z is also valid if Z exceeds it.
Use these FIXED choices: insert either a or b; reduce W or Z when strictly positive; try the
B35 abstract parent as written and its reverse-reflected displacement permutation, at most
eight candidates. Reverse-reflection sends x_i to -(x_i+e_i), preserving starts/ends because
they are permutations; normalization restores min0. Subdivide the chosen reduced negative
edge at x: new positive is at x, old negative moves to x+c. Map parent bins back explicitly.
This is a fixed parent architecture, not arbitrary cycle or role search.

**Predictions BEFORE diagnostic:** domain is the bounded four-part coefficient
sum_{1<=a<=b<=5} [z^(32-a-b)] prod_{j=0}^{21}(1-y*z^j)^(-1) at y^4;
independent signed-parameter and direct-low-quadruple sets must agree. Predict every target
has a distinct six-point candidate of span <=20 within these eight choices, hence a translate.
This last prediction is tentative: retain every failed candidate and any target without one.
Do not widen the class on failure. Check all candidates until first success per target; on a
family failure finish collecting diagnostics within the same cap, then stop this architecture.
Cap 5,000 targets / 40,000 candidates / five process CPU seconds; no cap increase.
For a distinct span>20 shape record direct roots separately, without using the <=20 theorem.
Literal certificates and independent sums/coverage checker for each successful construction.
Controls: reverse-reflection twice returns the original normalized parent; subdivision wrong
sign fails displacement; coverage-preserving wrong sums rejected. Unexpected check: are all
span-21 failures genuinely reflection obstructions, or do many still translate? Classify instead
of treating the sufficient bound as necessary. Schedules remain paused and reviews nonblocking.


### MI089 — B37 result: all targets certify, stronger span prediction fails (2026-10-16 13:05 BST)

All 2,919 two-surplus targets certify. Parameter/direct/DP domains agree. There were 3,074
candidate attempts, 129 literal collisions; 2,787 chosen certificates use the first parent,
130 its reverse-reflection, two reduce the other negative. Seven targets have no <=20-span
candidate in this class, refuting that stronger prediction; each certifies at span21. All 33
distinct span21 candidates encountered admit a root, so the sufficient bound is not necessary.
Controls pass, CPU 0.694618 s, no cutoff. Raw outside git SHA256
`417726155858aa98f6202e180396d2da9c25c986a6a0fca3145f076a26e9b48b`.
Finite family COMPUTED, no global E28 bound. The seven span exceptions all have W=21.

**What changed:** existence is checked for the family, but the eight-parent description obscures
why it works. **Gut:** delight at the reverse-reflection repair, and a push against accumulating
129 tiny exceptions. **Reasoned:** both surpluses can instead be inserted at once into a four-move
abstract parent. This changes the representation and may remove dependence on B35's case table.
Next cheap test: validate a direct six-move formula on the SAME family, without broadening it.
The state poll first hit a sandbox DNS transport failure (not authentication); no login retry
was made. The separately permitted network call is recorded operationally, not as math evidence.

### MI090 — B38: two surpluses from one abstract four-move parent (2026-10-16 13:05 BST)

Question: replace the eight-parent diagnostic by a direct uniform hand construction for exactly
the 2,919 targets of B37. This advances the same family toward an explanatory proof, rather
than adding another target table. Record: MI083-089, the B34/B35/B37 sources and actual diagnostic
artifacts read. Existing exchange precedents remain credited; no new novelty claim.

Put q=a+b, R=W-q. Since u+v>=12>q, W>q and R>0. Then R+Z=u+v. We have W<=21
(as MI088), v<=17 (u+3v+q<=56), and always a,b<=5. Bin indices carry
(u,v,-W,-Z,0,0,a,b). Select exactly one token in each nonzero bin.

**Split cases, all with distinct positions.**
1. If W=v then Z=u+q<=v. Use (+u,+a,+b,-Z) at 0,u,u+a,Z and (+v,-W) at
1,v+1. All six positions are distinct; v<=14, so span<=15.
2. If {R,Z}={u,v}, use a 4-cycle and a 2-cycle. If R=v,Z=u, use (+u,-Z)
at 0,u and (+v,+a,+b,-W) at 1,v+1,v+a+1,W+1. Here W<=19 and span<=20.
Otherwise R=u,Z=v: use (+u,+a,+b,-W) at 0,u,u+a,W and (+v,-Z) at r,r+v.
Choose the first r in {1,2,3} with r+v distinct from u+a,W. At most two r are forbidden,
r<u, and the six positions are distinct. W<=19, v<=14, so span<=19.
3. If W=v+d,Z=u+c with (c,d)=(a,b) or (b,a), use (+u,+c,-Z) at 0,u,u+c
and (+v,+d,-W) at r,r+v,r+v+d. Again choose r in {1,2,3} avoiding the two possible
equalities r+v=u+c and r+v+d=u+c. W=v+d<=16 (2v+d<=28, d<=5), span<=19.

**Nonmatching ordinary parent.** If R>=Z, take the cycle (+v,-Z,+u,-R) at
0,v,A,R, where A=R-u=v-Z>0. Its positions are distinct; R=v would have been paired.
Subdivide -R using +c,+d,-W at R,R+c,W, with {c,d}={a,b}. The new endpoint W can
collide only with v, already handled in case1. An intermediate collision requires R+c=v;
choose the other order. If both orders collide, a=b and v=R+a, hence W=v+a,Z=u+a,
which is case3. All six are distinct with span max(v,W)<=21.

If R<Z, start the cycle (+v,-R,+u,-Z) at 0,v,A,Z with A=v-R=Z-u>0.
Subdivide backward: replace -R at v by -W at v, +d at A-q and +c at A-c, where
c+d=q. The path goes v -> A-q -> A-c -> A, the old endpoint. Thus the two new positions
are A-c and A-q; normalize after adding them. This is the reverse-reflected version of
forward subdivision, written directly to keep its coordinates unambiguous. Each new point
is below A and can meet an old point only at 0. A=q would imply W=v, case1.
Choose c from a,b with c!=A; if neither is possible, a=b=A and W=v+a,Z=u+a, case3.
Thus this gives six distinct positions. Span D=M+max(0,q-A). If A>=q, D=M<=20:
W=21 would force v<=7, R>=11, Z<=3, contrary to R<Z. If A<q and v>=Z then
D=R+q=W<=20 for the same reason. If A<q and Z>v then D=u+q<=21: combine
2R+q>=u+v>=2u with R+q+v<=28 to get 2u+q/2<=28, so u+q<=21.5.
Equality D=21 forces q=10,u=v=11,R=6 or7. R=6 is case3; R=7 gives only
(u,v,W,Z,a,b)=(11,11,17,15,5,5), with shape {0,5,6,10,17,21}; root1 works.

**The other span-21 cases.** In R>=Z, span21 means W=21 and v<=7. Positivity
Z=u+v+q-21 and 6<=u<=v enumerate exactly seven tuples. For the displayed forward
shape use c=b. Literal direct folded labels for these prescribed roots will be checked:

| u | v | W | Z | a | b | root |
|---|---|---|---|---|---|---|
|6|6|21|1|5|5|1|
|6|7|21|2|5|5|1|
|6|7|21|1|4|5|1|
|7|7|21|3|5|5|4|
|7|7|21|2|4|5|0|
|7|7|21|1|3|5|2|
|7|7|21|1|4|4|1|

All remaining shapes span<=20, so MI087 gives a reflection-free translation. Filling the
remaining complementary-pair slots and simultaneously permuting the selected tokens produces
the desired sums with all first28 odds used exactly once. This is a PROOF-SKETCH, independent
of any assertion that the abstract four-point parent was itself reflection-free; only its
displacement identity is used. This avoids importing B34's root exceptions or B35's repairs.

**Predictions BEFORE validation:** every B37 target certifies via these formulas; signed, direct
and DP domain counts still agree; only the eight explicitly listed geometries reach span21.
All other branches must span<=20. Controls: omit triple/paired shifts to force collisions; use
wrong root0 on the first W21 fixture to force pair reuse; reverse the wrong edge endpoint to
fail displacement; coverage-preserving wrong sums rejected. Unexpected check: the extra
(11,11,17,15,5,5) span21 case did NOT require span21 under B37's different parent. Keep both
witnesses, demonstrating that a geometric exception belongs to the construction, not the target.
Cap the SAME 2,919 targets / five CPU seconds; stop on formula/domain/control failure without
adding cases. No larger target region, solver, cap increase or review dependency.


### MI091 — B38 result: a direct uniform two-surplus construction (2026-10-16 13:08 BST)

All 2,919 direct certificates pass. Branches: 1,105 forward, 620 backward, 305 paired-large,
265 paired-small, 499 split into two 3-cycles and 125 W=v splits. Exactly the eight listed
geometries reach span21; all prescribed roots pass. Every remaining shape is distinct with
span<=20 and a valid translate. Omitted shifts, wrong exceptional root, wrong displacement
and coverage-preserving wrong sums are rejected. The extra span21 geometry has a span17
witness under B37, confirming the exception is construction-specific. CPU 0.481749 s; raw
JSON outside git SHA256 `25a3d75cd7017f257d54d82f6ecba765c689d488889678e9a6e73a7789709aa0`.
Finite family COMPUTED; MI090's direct hand argument remains PROOF-SKETCH pending independent read.

**Proof/niggle audit:** R>0 follows from u+v>q, not a parent feasibility assumption. The
abstract parent is a displacement cycle only; it need not embed before subdivision. The backward
path is explicitly v -> A-q -> A-c -> A, avoiding ambiguity about reverse-reflected coordinates.
The two new backward points can meet old positions only at0. The span21 enumeration includes
the extra q10/u11 case, not just the seven W21 cases observed in B37. Paired and triple shifts
have at most two forbidden choices among three. Six occupied pairs leave the exact required
filler slots; a token is removed only from its own initial pair, and all transfers are simultaneous.
The final checker uses literal odd sums and coverage independently of the displacement identity.
No silent concern remains about these checks; independent proof adoption is still outstanding.

**What moved:** MI090 explains an entire family without B35's parent-specific case list or the
eight-candidate diagnostic. **Gut:** a warm pull and delight at the backward path; less appetite
for simply adding a third surplus and counting cases. **Reasoned:** positive moves can be placed
before or after a negative edge; choosing the side controls both collisions and span. Next useful
question is whether this endpoint flexibility has a structural version for more active bins,
where a universal seven-position translation bound would be weaker. No new block is claimed yet.

**Synthesis audit, registered BEFORE execution:** combine existing B34, B35 and B38 certificates
with B32's 122 one-negative cores. Predict exactly 4,523 distinct even E28 targets with
t5=t6=112 (equivalently top four (112,112,112+2a,112+2b),0<=a<=b<=5). Counts: the
previous 1,538 targets, B38's 2,919 with t4<112 and a>0, plus 66 one-negative cores with
a>0, total4,523. Compare complete target sets to independent sorted low quadruples 68..112
and sum784, without a new construction search. Retain all witnesses and reject any discrepancy.
No other module-family counts are added; they overlap. This is a scope audit, not a new block.


### MI092 — scope audit and checkpoint: a complete 4,523-target region (2026-10-16 13:08 BST)

The synthesis audit passes: existing certificates equal exactly all 4,523 sorted even E28
targets with t5=t6=112. Contributions by nonoverlapping regimes are 122 one-negative cores,
284 zero-surplus two-negative targets, 1,198 one-surplus and 2,919 two-surplus targets.
Compared with the previous 1,538-target region, 2,985 are added: the 2,919 direct targets plus
66 already-covered one-negative cores with both surplus parameters positive. Every literal
certificate was rechecked; direct sorted-low-quadruple domains agree as complete sets.
The scope-audit raw summary SHA256 is
`712f2b820af3de3450ef8fbb93cceafea6b17066c457e0dd3eb3a7d36e031484`, outside git.
The raw summary cites each source artifact by digest. Other overlapping families are not added.

This region is COMPUTED. Its new uniform hand constructions are PROOF-SKETCH; MI090 is a
substantial carrying candidate and is ready for a targeted read with MI087's short geometry
argument. G306 remains PROVED. No full E28 or minimum-68 result, no novelty claim. The first
sandbox-only store poll failed DNS; the permitted network call succeeded, with no failed authentication. Both automatic schedules remain paused.

**Step back / fresh choice:** this is enjoyable as a steering signal: the new backward
subdivision actually simplified the mathematics. The frustrating part is the temptation to
keep expanding finite regions without obtaining a flexible general mechanism. If arriving fresh,
I would still choose this question because the positive/negative path geometry is now visible,
but I would choose that geometry over a larger certificate table. The next unresolved inference
is how to distribute several positive moves before/after negative edges while controlling the
number, distinctness and span of selected positions. Three surplus moves would require seven
positions; simply extrapolating the six-position theorem is unjustified. A small sharp geometry
question or a direct endpoint-allocation argument is the next cheap test, not another census.

B36-B38 advanced through a tentative prediction failure to a simpler hand construction without
waiting for review. One targeted carrying request will be sent at this milestone; it is not a
research hold. This is a delivery checkpoint, not a halt pending Cloud or an automatic restart.


### MI093 — CL422 adopted; choose the next geometry question (2026-10-16 13:39 BST)

Cloud's fde83bd8 was fetched and read before ACK. CL422 independently verifies MI070's
320-target surgery, MI087's sharp six-position translation and MI090's direct two-surplus
construction. Adopted as G307,G308,G309 respectively. Preserve proof mode: for MI090 Cloud
checked the span subcase by an independently derived complete finite implementation, not by
claiming a second all-hand derivation. The wider4,523 region is recounted COMPUTED; B34/B35's
other sketches are not silently upgraded. Heartbeats stay paused and reviews are not turn gates.

Cloud's scale note is right: the value is endpoint placement, not a few thousand target totals.
The strongest pull is to test that geometry where three small positive moves must share two
negative edges. First check the seven-position tool; do not extrapolate G308.

### MI094 — B39: a sharp seven-position barrier, then a different endpoint question (2026-10-16 13:39 BST)

Record searched: seven.position, endpoint.allocation, G307 -> no default-record hits; MI087-092,
CL422 and the actual construction sources read. No new prior-art or novelty claim.

**Hand finding.** Seven distinct positions spanning <=15 always translate into0..27 without
complementary collisions: there are at least13 roots and at most floor(7^2/4)=12 cross-parity
pairs. But span16 already fails. S={0,5,7,8,9,11,16}: the even positions0,8,16 pair with
the four odd positions5,7,9,11 to produce every odd sum5,7,...,27 exactly once. These block
all12 allowed translations. Thus the universal span guarantee drops from20 for six points to15
for seven. This tool is a hand sketch, not a separate novelty/review job.

**Surprise / push:** a pure span theorem becomes too weak quickly: any displacement permutation
containing a negative edge of magnitude W has span>=W, often already above15. This is a reason
to use the actual endpoint geometry, not to widen a span search. Counterfactual: treating the
six-position bound20 as if it covered seven is explicitly refuted by the span16 fixture.

**Endpoint mechanism.** For a negative edge x -> y=x-R, inflate its magnitude to W=R+q
and split the new positive moves into two ordered groups, totals q_before and q_after.
Place the first group along x -> x+q_before, then -W to y-q_after, then the second group
back to y. The new selected positions lie outward from the OLD endpoints: above x and below y.
They never collide with one another across the two arms; literal collisions are only with old
positions. Final span is max(M,x+q_before)-min(m,y-q_after). This controls where to look.

**Three-surplus allocation, hand candidate.** Let 1<=a<=b<=c<=5, q=a+b+c. For two negative
magnitudes W>=Z, u+v+q=W+Z, u+v>=12, a strict two-negative four-move parent always exists.
If Z>a, assign a to Z and b+c to W: W>b+c since u+v+a>b+c (12+1>10). If Z<=a,
assign all q to W, since W-q=u+v-Z>=12-5>0. Thus the allocation itself needs no subset
search; what remains is collision-free placement of those moves at the two endpoints.

### MI095 — B40: maximal three-surplus stress of two-ended subdivision (2026-10-16 13:39 BST)

Question: can this endpoint rule handle the maximal-surplus slice a=b=c=5, rather than another
small extra surplus? Targets have top four(112,122,122,122), t4<112. The four low targets sum306;
write low_i=68+2r_i, sum r_i=17. Predict72 targets, the at-most-four-part coefficient at17;
verify by a bounded generating DP, direct low quadruples and signed parameters independently.
No global E28 claim. The q15 slice explicitly includes W<=q, where putting all moves onto W
would not leave a strict negative parent.

**Fixed architecture BEFORE execution:** if Z>5, reduce W by10 and Z by5; insert two5 moves
on W and one5 on Z. Try each split of the two moves before/after the W edge and each side for
the other move (six cuts). If Z<=5, reduce only W by15 and try its four before/after cuts.
For an ordinary four-move parent use its two alternating low-positive orders, normalized; if
parent negative magnitudes match u,v, use two disjoint 2-cycles at relative roots1,2,3. At most
18 candidate shapes per target. These are endpoint/order choices in one named architecture; no
arbitrary-cycle, role or larger-family search. Translate each distinct in-pool-span shape by
all allowed roots, validating pair labels directly; do not assume G308 covers seven points.

**Blind prediction:** all72 targets certify within these fixed choices. If not, retain every
failed target and classify repeated positions versus reflection obstruction; finish this slice
within cap, then stop this architecture without widening. Cap120 targets/2,160 candidates/five
CPU seconds. Both parent and child displacement identities, full literal sums/coverage checked.
Controls: span16 seven-point fixture must block every root; its six-point deletions translate;
wrong subdivision sign fails displacement; wrong sums with coverage preserved rejected.
Unexpected check: force all15 onto W when W<=15; parent must be rejected, even if an arbitrary
coordinate formula could be written. Record how many actual targets require the two-edge split.
This validates the allocation obstruction separately from placement. Review nonblocking; both
heartbeats paused. No new claim to solving the full even family or mixed parity.


### MI096 — B40 result: 71 pass, one literal trap (2026-10-16 13:43 BST)

The72 targets agree across signed/direct/DP domains.71 have exact certificates in the fixed
architecture; (u,v,W,Z)=(6,6,21,6), target(68,68,70,100,112,122,122,122), fails all12
candidates by repeated coordinates. No distinct candidate fails reflection avoidance.
One other target, (6,7,21,7), uses the second cut; the remaining70 pass the first.
84 attempts:71 translated,13 repeated.8 targets have W<=15 and reject the all-on-W parent
as predicted. Controls pass. CPU0.013354 seconds; raw outside git SHA256
`f7a72f0689d567a766c020d0decb14edecab32222384b520fa7b611a92d92384`.
Blind all72 prediction REFUTED; this architecture has stopped without adding choices.

**Surprise:** failure is already in the four-point parent. For the failing target, splitting
10 onto W and5 onto Z gives magnitudes11,1 and positions{0,5,6,11}. The -1 edge goes
6->5. Inserting +5 before it needs the already-used11; inserting after it needs the
already-used0. Translation cannot repair either literal equality. Both low-positive orders
coincide because u=v. This explains every failed candidate without reflection or a larger search.
**Gut:** the failure sharpens the pull: allocation and placement must communicate. **Reasoned:**
preserving a matching negative edge may be better than reducing both edges by a fixed amount.

### MI097 — B41: classify the literal trap and flip the allocation (2026-10-16 13:43 BST)

Question: can the repeated-coordinate obstruction be recognized algebraically before choosing
a parent? This changes the actual endpoint algorithm, rather than adding a target to a table.
Record searched: seven.position, endpoint.allocation, two.ended; only current ledger hit,
MI094-096 and B40 artifact read. No novelty claim or independent-review request for this tool.

**Hand classification, PROOF-SKETCH.** A distinct four-position displacement permutation has
positive moves u,v and negative moves -R,-T. On the -R edge x->y=x-R, insertion of one
positive c can fail literally at BOTH ends only if x+c and y-c are old positions. These four
positions are all distinct, so they exhaust the parent. Translate y to0: the set is
{-c,0,R,R+c}, with -R at R. The largest point R+c must carry -T. If its endpoint were R,
the remaining two positive moves could not map {-c,0} bijectively to {-c,R+c}; zero or a
negative move would be required. Hence it ends at -c, and T=R+2c. The two positive moves are
either both R+c, or R and R+2c, by the two remaining bijections. This exhausts the literal
trap without looking at a family of targets.

**Allocation flip.** Move this +c from the small negative edge to the other negative edge.
The new parent magnitudes are both R+c. In the equal-positive case they match u=v=R+c,
so the parent splits into two2-cycles instead of preserving the trapped four-cycle.
For B40 with c=5, the other edge also receives two5 moves: original W=R+20,Z=R+5.
The equal-positive case gives v+W=2R+25<=28 and u=R+5>=6, forcing R=1.
The unequal-positive case would give v+W=2R+30>28. Thus THIS unavoidable single-edge
trap is uniquely the failed target under the q15/sorting constraints. This does not claim
that every possible multi-arm failure in arbitrary parameters is such a trap.

For that target flip to putting all15 onto W, leaving the matching Z=6 edge unchanged.
Use (+6,-6) at0,6 and (+6,+5,+5,+5,-21) at1,7,12,17,22. Pair labels are
0,6,1,7,12,10,5, distinct. These two independently placed cycles give the exact deviation
permutation; materialize the literal odd partition. This is an allocation change justified
by the carrying obstruction, not a larger cycle search.

**Predictions BEFORE validation:** this one fixed repair must certify; the earlier71 witnesses
are rechecked unchanged, producing exactly the original72-target set, with no broader domain.
Controls: keep the trapped parent and test both one-move sides, literal equality in each;
omit the5-cycle's root1 (use0) and pair-label collision must reject; preserve coverage but
change sums and reject. Unexpected: repaired seven-point witness has span22, far beyond the
universal span15 guarantee; its separate cycles still embed, so the span barrier is a limitation
of that sufficient tool, not a target obstruction. Cap one new input / one proposed repair,
plus72 existing-certificate checks / one CPU second; stop on disagreement, no further repair.
Both heartbeats paused; independent work does not wait on review.


### MI098 — B41 result and the mechanism to generalize (2026-10-16 13:47 BST)

The fixed allocation flip certifies the failed target. All71 earlier witnesses recheck and
together equal the original72-target domain. Wrong cycle root, wrong sums and both literal
trap sides behave as predicted. The corrected seven-point shape spans22, despite the universal
span15 limit. CPU0.004957 s; raw outside git SHA256
`78084a40ec04e84135efa7b88bb6da00e46255434c6baa4c1b0aafaed187aa0a`.
Finite slice COMPUTED; the trap classification remains a hand sketch. No new global E28 result.

**General inference beyond the fixture.** The four-point literal trap has T=R+2a and positive
moves either both R+a, or R and R+2a. Flipping the inserted a to the other edge gives two parent
negatives of size R+a. In the equal-positive case these are cancelling pairs; in the unequal
case an abstract alternating parent has positions{0,a,R+a,R+2a}. Choose the edge ending at0
and put all small positive moves after it: the new positions are negative and cannot repeat an
old nonnegative coordinate. Thus the flip removes this literal trap in general; reflected-pair
collisions are a separate next question. The q15 fixture is one instance of that rule.

**Gut:** delight at preserving a cancellation instead of disturbing both donors. **Reasoned:**
choose the core's translation jointly with the spare cancelling pair, so unused-label quantity
is not confused with a legal unused gap. The next block asks for that uniform rule.

### MI099 — B42: preserve a matching edge; choose translation for the spare pair (2026-10-16 13:47 BST)

Question: cover EVERY even E28 target with exactly three positive high surpluses a,b,c in1..5
and two negative deviations, whenever one negative magnitude equals one of the two low positive
magnitudes. This would turn the allocation flip into a reusable matching-edge construction.
Record searched: gap.*matching, matched.*three, gap.?9 -> no default-record hits; MI073/090/094-098
and relevant actual sources read. Folded-gap packing was used for magnitudes1..5 in MI073;
this extends the relevant packing range to6..14. No literature-absence or novelty claim.

**Parameters and hand candidate (PROOF-SKETCH).** Cancel a positive g against a negative -g;
let h be the other low positive and H the other negative. Then H=h+q, q=a+b+c.
Here g,h>=6, a,b,c<=5, and sorting gives max(h,g)+max(H,g)<=28. Hence6<=g<=14,
H<=21: H<=v+15 and H<=28-v, v=max(h,g), so v=6 gives H<=21 and v>=7 gives H<=21.
Also H<=28-g. Build a five-point core cycle (+h,+a,+b,+c,-H) at
0,h,h+a,h+a+b,H. This is strictly increasing with span H. At most six cross-parity
pairs block translations. We will give SEVEN allowed roots, each ensuring the core's five
used labels cannot cover every physical gap-g pair. Thus a valid core root exists and a
spare two-cycle(+g,-g) can then be placed independently.

**Gap graph.** Vertices0..13 are folded labels. Two distinct labels i,j support a physical
index gap g exactly when |i-j|=g or i+j=27-g. This follows by choosing each index as its
label or its complement; i+j=27+g is impossible for labels<=13. Loops are not legal pairs.
For g=6,7,8,12,13,14 there is a matching of SIX edges, so five core labels cannot cover all
edges. Explicit matchings (pairs separated by semicolons):

|g|six vertex-disjoint edges|
|---|---|
|6|0-6;1-7;2-8;3-9;4-10;5-11|
|7|0-7;1-8;2-9;3-10;4-11;5-12|
|8|0-8;1-9;2-10;3-11;4-12;5-13|
|12|0-12;1-13;4-11;5-10;6-9;7-8|
|13|0-13;2-12;3-11;4-10;5-9;6-8|
|14|0-13;1-12;2-11;3-10;4-9;5-8|

Use candidate roots0..6 for these g. They all fit since H<=21.

The other three graphs have minimum vertex-cover size FIVE. Their small components give all
five-covers explicitly, without assuming every five-set is harmless:
- g9: edge0-9 and paths1-10-8,2-11-7,3-12-6,4-13-5. Five-covers are
  {10,11,12,13} plus either0 or9. Use roots1..7: the core includes its root label,
  which lies in NO five-cover. All these roots fit because H<=19.
- g10: paths0-10-7,1-11-6,2-12-5,3-13-4 and edge8-9. Five-covers are
  {10,11,12,13} plus8 or9. Use roots0..6, none in a five-cover.
- g11: paths0-11-5,1-12-4,2-13-3, edges6-10 and7-9, isolated8. Five-covers
  are {11,12,13}, one of6/10, one of7/9. Use roots{0,1,2,3,4,5,8}; none in
  a five-cover, including isolated8. They fit because H<=17.

For each g, at most six roots can fail the core's reflection test; among the chosen seven
one is valid. At that root its labels do not cover the gap graph, so select a physical
x,x+g whose two labels are unused. Put +g at x and -g at x+g, retaining the core
cycle. Reserve these seven distinct whole pairs and fill all remaining slots; simultaneous
selected-token permutation gives the exact target sums and whole-odd coverage. The argument
uses only an elementary pair-count and these explicit graphs, not an unproved seven-position
span theorem or the q15 table. Equality of targets is handled by stable role relabelling.

**Predictions BEFORE validation:** independently generate the graph from physical index pairs
and from the label formula; verify matchings and exactly0/0/0/2/2/4/0/0/0 five-covers for
g6..14, with all enumerated covers equal to the displayed ones. For all h,g>=6 and sorted
a,b,c in1..5 satisfying the inequality, every one of the SEVEN-ROOT sets contains a valid
core root and the selected root leaves a spare gap-g edge. Validate literal certificates
after stable sorting back to the two-smallest roles. Cap2,500 parameter instances / five
CPU seconds; stop on any graph, root, mapping or full-checker failure, without widening.
Also compare the resulting TARGET set to independently generated two-negative E28 parameters
filtered by a matching positive/negative magnitude; this is a domain equality, no solver census.

**Counterfactual / unexpected control:** h10,g9,a=b=c1 has a valid root0 core with labels
{0,10,11,12,13}, a five-cover, so NO spare gap9 exists. Forcing the unrestricted first
valid root must fail here; the prescribed roots must repair it. This shows why spare-label
COUNT alone is insufficient, even in the matching family. Wrong-sum coverage-preserving
mutation and a forced occupied gap endpoint must be rejected. All first72 maximal-surplus
targets are not claimed matching targets; retain that scope distinction. Both schedules
paused, reviews nonblocking; the scope stays within this named structural family.


### MI100 — B42 result: a matching edge can be preserved uniformly (2026-10-16 13:49 BST)

All999 parameter instances give999 distinct checked targets. The set equals the independent
two-negative target domain filtered by a matching positive/negative magnitude. Graphs from
physical indices and from folded-label equations agree; six-edge matchings and the2/2/4
exceptional five-cover classifications agree exactly. Every prescribed seven-root set fits;
each selected valid core root leaves a free gap-g edge. All whole-odd certificates pass.
The bad root0 control is a valid core that blocks every gap9 edge; restricted root4 repairs
it. Forced occupied endpoint and coverage-preserving wrong sums are rejected. CPU0.131515 s.
Raw outside git SHA256 `d03a0e92d5878e200535ec0c8016220a328668f1d3e16c328d341d6ede0573c8`.

Finite family COMPUTED; MI099 is a uniform hand candidate pending independent verification.
It does not use B40's72-case table or assume seven-point translation from a span bound.
**Niggle sweep:** allowed roots have their own distinct labels<=8, including isolated8 at g11;
seven roots fit physically, not only formally; five-cover obstruction is checked before packing
the pair; gap graph excludes loops; large-bin equality is relabelled stably; neutral bin remains
filler-only; selected-token permutation and literal sums are checked independently.
**Gut:** warm pull because the root choice now protects the next component. **Reasoned:** the
remaining nonmatching extreme is informative; take one such boundary by hand before considering
any whole three-surplus search.

### MI101 — B43: the unmatched maximal-negative boundary (2026-10-16 13:49 BST)

Question: does the other extreme, W=22, admit a uniform three-surplus construction even
though no cancelling edge exists? This tests actual unmatched geometry where the matching
argument cannot apply. Record searched: gap.*matching, matched.*three, gap.?9 -> no earlier
default-record hits; MI069/090/094-100 and actual sources read. No novelty claim.

**Hand candidate, PROOF-SKETCH.** Sorting v+W<=28 with W=22 forces u=v=6. For q=a+b+c,
Z=q-10>0, so11<=q<=15 and1<=Z<=5. Hence no negative magnitude equals the low positives6.
Put R=22-q in7..11 and A=16-q in1..5. Use the7-cycle
(+v,-Z,+u,+first,+middle,+last,-22) at positions
0,6,A,R,R+first,22-last,22. These are all distinct:0<A<6<R<R+first<22-last<22.
The middle/late positive-prefix positions P=R+first and Q=22-last satisfy P<=16,Q>=17
and P+Q>=29; early sums are below23. Only a few early/late pairs can block a small root.

Choose these explicit orders/roots:
- q>=13: sorted order(a,b,c), root0. Here last=c=5. No old pair sums27:
  A+22<=25, Q+R=44-q-5<=26, Q+6=23; P+R<=44-2q+5<=23,
  P+6<=22 and P+A<=21; late/late sums are>=29.
- q=12 and c=4: necessarily(4,4,4). Every coordinate is even, so root0 is safe.
- q=12 and c=5: sorted first=a is2 or3. Use root1, so only original sums25 are forbidden.
  A=4,R=10,Q=17,P=12 or13. None of their distinct pair sums is25.
- q=11 and a<=2: sorted order, root1. A=5,R=11, P=11+a<=13 and last=c>=4.
  A+22=27, R+P<=24, Q+A=27-c<=23, Q+6=28-c<=24; all other
  possible early/late sums also miss25, and late/late sums are>=29.
- q=11 and a>=3: the multiset is(3,3,5) or(3,4,4). Put one3 LAST and use root2;
  only original sums23 are forbidden. Now A=5,R=11,Q=19 and P=14 or15.
  No distinct pair sums23; max translated index24 is in the pool.

This exhausts q11..15 and gives literal complementary-pair-disjoint token cycles. Fill all
remaining slots and permute seven selected odds simultaneously. The hand claim is exactly
this maximal-negative three-surplus boundary, not all unmatched targets.

**Predictions BEFORE validation:** exactly11 sorted(a,b,c) choices, with q subtotals4,3,2,1,1
for11..15; compare to independent sorted even target quadruples, W22 fixing three68 values
and t4=112-2(q-10). All explicit formulas must certify. Cap20 targets/one CPU second;
no order search or cap increase. Controls: using root0 for q11 fails through A+22=27;
using sorted root1 for(3,3,5) at q11 fails through R+P=25; wrong sums with coverage
preserved rejected. Unexpected: all(4,4,4) positions are even, so every in-pool root works
despite span22 and seven selected bins. This isolates parity from the universal span15 limit.
Both schedules paused; no review hold and no broader unmatched-family search.


### MI102 — B43 result: maximal-negative unmatched boundary closes (2026-10-16 13:51 BST)

All11 prescribed seven-cycle certificates pass, equal to the independent direct-target domain.
q subtotals4,3,2,1,1 agree. Both wrong root/order controls and coverage-preserving wrong sums
are rejected. The all4 fixture allows every in-pool root0..5 as predicted by parity.
CPU0.001306 s; raw outside git SHA256
`34293beaf38b5cee6559cb376daa1ad09e0b0894088a824e26f97ab539c1cef8`.
Finite boundary COMPUTED; MI101 remains a uniform hand candidate pending independent read.
This is all W22 THREE-surplus targets; it says nothing yet about unmatched W<22 or four
surplus moves. No broad E28 or minimum68 claim and no priority assertion.

**Niggle sweep:** three lower targets68 are forced from the sorting/role constraints, not
selected as a convenient fixture; the late-prefix pair sum is>=29 from the two remaining
positive moves being<=5; the q11 order places an actual3 last, not a value absent from the
multiset; all translated positions fit; selected bins retain correct roles when targets tie.
The parity control is separate from the seven-position sufficient span theorem. All checked.

### MI103 — checkpoint: verified predecessors, two new structural candidates (2026-10-16 13:51 BST)

CL422's carrying reads are filed as G307, G308 and G309 with exact provenance. The independent
finite implementation used for MI090's span subcase is explicitly retained as that proof mode.
The neighbouring zero/one-surplus hand sketches have not been silently adopted. Proof duplicate
hard checks pass; named nearest predecessors read and distinguished.

This continuation changed the question rather than just enlarging the table:
1. A seven-point span16 obstruction killed extrapolation of the six-point translation tool.
2. The first two-ended architecture failed at a literal four-point trap. The failure is kept;
   its exact geometry led to an allocation flip and a classification, not raised caps.
3. MI099 preserves a matching edge and chooses the core root to leave its gap graph uncovered.
   All999 matching targets have exact formula certificates; a bad valid-core root shows why
   simple unused-label counting is not enough.
4. MI101 handles the maximal-negative unmatched boundary by a seven-cycle, prefix order and
   parity, all11 targets checked. The two new hand arguments remain SKETCH pending review.
These target counts overlap other older probe families; no additive global total is asserted.

**Fresh-choice reflection:** still enjoyable and warm, with a push against treating a larger
finite count as the objective. The interesting change is that the core root is now chosen for
the component that comes NEXT, and a long cycle can succeed by parity even where a universal
span tool fails. Arriving fresh, I would still choose to understand that dependency. The unresolved
step is unmatched interior cases W<22: can allocation, positive order and reflection avoidance
be chosen jointly without another proliferating case list? The next cheap test is a structural
necessary/sufficient condition on those endpoint choices, before any full-family run.

No automatic schedules were resumed. Five substantive steps were taken after the review, without
waiting for a new one. One batched carrying request for MI099/MI101 is appropriate at this
checkpoint; the elementary barrier/trap tools are not separate review jobs. This is a published
checkpoint, not a halt pending Cloud.


### MI104 — B44: reduce unmatched placement to a two-slot compatibility graph (2026-10-16 14:17 BST)

Question: in the unmatched three-surplus interior, can one fixed all-after allocation suffice
when its remainder R=W-q is at least Z? This is a named structural regime, not an arbitrary
cycle search. Its answer would isolate what allocation actually needs to change. No new review
is available at this wake; existing candidates keep their statuses. Both schedules stay paused.
Record searched: unmatched.*interior, allocation.*translation, W.?21 -> no default-record hits;
MI094-103 and the endpoint sources read directly. Known exchange/packing tools remain credited;
no literature-absence or novelty claim.

**Hand reduction, PROOF-SKETCH.** Take deviations(u,v,-W,-Z,0,a,b,c), q=a+b+c,
1<=a<=b<=c<=5, 6<=u<=v, W>=Z>0, u+v+q=W+Z, v+W<=28. Exclude matching
{u,v} intersect {W,Z}, and the already-constructed W22 boundary. Assume R=W-q>=Z.
Then R+Z=u+v, A=R-u=v-Z>0, v!=R; a paired parent would have Z=u and be excluded.
Use parent(+v,-Z,+u,-R) at0,v,A,R. Put ALL three surplus moves AFTER -W, outward
from its old endpoint0. The three new positions are negative before normalization, so they
never repeat an old position. Normalized selected positions are
{0,first,q-last,q,q+A,q+v,q+R}. Their span is D=q+max(v,R)<=22. Indeed W<=22,
and R>=Z gives u+3v+2q<=56, hence2(v+q)<=56-u-v<=44.

Five positions B={0,q,q+A,q+v,q+R} are FIXED. The other two are determined by choosing
distinct surplus ITEMS i,j as first and last, with p=a_i and s=q-a_j. The third item is
the middle; positivity guarantees0<p<s<q, so all seven positions are literally distinct.
For a root r in0..27-D put T=27-2r. If a distinct pair in B sums to T, this root cannot
work. Otherwise define forbidden F={T-b:b in B}. An edge(i,j) in the three-by-three
first/last compatibility graph is legal exactly when i!=j, a_i not in F, q-a_j not in F,
and a_i+(q-a_j)!=T. The first two tests protect the fixed core; the third protects the
two new positions from one another. Thus a legal edge is EQUIVALENT to a complete legal
embedding in this architecture. This criterion is not yet a theorem that an edge always exists.
It replaces opaque root/order retries by explicit reasons for each obstruction.

**Pull:** warm toward the criterion, with unease about calling another successful table a general
argument. The falsifiable next step is whether this PARTICULAR allocation survives at all; if
not, retain the exact obstruction and change allocation rather than widen the cycle class.

**Predictions BEFORE diagnostic:** tentatively every target in this named regime has a legal
root/edge. Compare the algebraic graph with independent direct folded labels for EVERY allowed
root and six item orders, not just successful roots. Verify parameter targets equal independent
sorted low quadruples filtered by the same signed constraints. Produce a literal odd certificate
for each successful target. Cap2,500 targets/500,000 root-order checks/five CPU seconds. If the
architecture fails, collect failures within the same cap, then stop it without adding allocations,
parents, roots outside the pool or larger cycles. A cutoff is UNKNOWN, never a refutation.

**Controls:** u6,v9,W13,Z5,(a,b,c)=(1,1,1), r9: the five fixed positions have distinct folded
labels but the compatibility graph has no edge. Therefore fixed-core validity alone must fail
as a completion test. At u6,v7,W14,Z5,(1,2,3), r11, first1/last2 individually avoid the
fixed core but their two positions sum to27 after translation; omitting the cross-test must
be rejected by direct labels. Full checker rejects coverage-preserving wrong sums.
Unexpected: compare graph edges for every root against literal seven-position labels, including
roots with a valid fixed core and no completion; record these separately from invalid cores.
This checks the exact remaining inference, not only favourable certificates.


### MI105 — B44 result: all-after fails in exactly two targets (2026-10-16 14:21 BST)

There are1,478 targets in the named unmatched R>=Z,W<22 regime, with independent domain
sets equal.1,476 certify. All94,008 algebraic/direct root-order comparisons agree. Across
roots:8,998 have completions,1,481 have a legal fixed core but no completion,5,189 have an
illegal fixed core. Two complete architecture failures remain:
(u,v,W,Z;a,b,c)=(6,7,21,2;2,4,4) and(7,7,21,2;3,3,3). The blind all-after claim
is REFUTED; no caps or choices were added. Controls pass, CPU0.424268 s. Raw outside git SHA256
`0dbafbbd7fcf3ce822ebc5effc442e4cd0f9f074a817c84f5af7daa96fed612c`.

**Failure certificates by hand.** In the first case B={0,10,15,17,21}, allowed roots0..6.
Only roots2 and4 have legal fixed cores. At r2,T23 the forbidden set is{23,13,8,6,2};
the last variable is6 or8, both forbidden. At r4,T19 the forbidden set is{19,9,4,2,-2};
the first variable is2 or4, both forbidden. At other roots fixed pairs sum to T.
In the second case every order gives S={0,3,6,9,14,16,21}. Its opposite-parity pair sums
include all15,17,...,27, blocking every allowed root. Thus no extra root or permutation
within this allocation could help. The variables need to move to the other endpoint.

**What moved:** root/order feasibility has an exact local test, and its two failures are explicit
obstructions, rather than UNKNOWN solver outcomes. **Gut:** disappointment at losing the universal
all-after rule, then a warmer pull when both failures shared a short allocation repair.
**Reasoned:** test that repair on a parameter stripe with explicit labels before expanding scope.

### MI106 — B45: one move before, two after, with explicit pair labels (2026-10-16 14:21 BST)

Question: can one uniform parameter rule repair both exhausted all-after obstructions?
Record searched: unmatched.*interior, allocation.*translation,W.?21; MI094-105 and B44
actual artifact read. No novelty claim; this is an endpoint-allocation change on the same
parent, not a larger cycle search.

**Hand candidate (PROOF-SKETCH).** Restrict W=21,Z=2,v=7,u in{6,7}, q=16-u and
1<=a<=b<=c<=5 with B=q-c=a+b in{5,6}. Then a<=3. Put the largest move c BEFORE -W,
and the other two after it. Choose the final physical selected indices directly:
+a at1, +b at1+a, +v atB+1, -Z atB+8, +u atB+6, +c atB+6+u, -W at22.
They follow the closed path
1 ->1+a ->B+1 ->B+8 ->B+6 ->B+6+u ->22 ->1.
The c edge closes because B+c+u+6=q+u+6=22.

Their folded labels are1,1+a (in2..4),5 for the -21 edge,6 or7 for B+1,
11 or12 for B+6,13 for B+8, and8/9/10 for B+6+u. These seven labels are pairwise
distinct. Thus one selected token per active bin, filler pairs and simultaneous transfer
produce the exact target partition. This covers both failures and five neighbouring targets
with one rule, without needing an all-after compatibility edge.

**Predictions BEFORE validation:** exactly7 parameter choices in this stripe; compare to direct
sorted high triples and fixed low parameters. Every displayed witness must certify. Recheck
the1,476 existing B44 witnesses unchanged and add only the two missing targets; target union
equals the same1,478 regime, with no wider E28 claim. Cap10 new inputs/one CPU second, plus
the existing-certificate recheck. Stop on any discrepancy; no extra repair.
Controls: moving all seven positions down1 in the (6,7;2,4,4) repair restores a complementary
collision. Coverage-preserving wrong sums rejected. Unexpected boundary check: the same formula
for u=v7,(a,b,c)=(1,3,5) has B4; +v at5 and -W at22 reuse a pair. This must fail and
shows the B>=5 hypothesis carries real weight; that neighbouring target was already certified
by B44's different placement. Both schedules paused; no new carrying queue or review hold.


### MI107 — B45 result: complete fixed-regime certificates with one endpoint rule (2026-10-16 14:24 BST)

All7 stripe witnesses pass. The prior1,476 witnesses recheck unchanged, and the two missing
targets from B44 join them to equal the same1,478-target regime. Downshift, wrong sums and
the B4 countercontrol are rejected. CPU0.130838 s. Raw outside git SHA256
`833895ffcbfe85b3a4c0502ef9eea476e8f0ca9ae302cebd1dd664059ff12908`.
The stripe has a direct label proof; universal availability outside it is COMPUTED by the
complete root/edge checks, not silently recast as a hand proof. B44's two failed allocations
remain. No full E28/L8 or novelty claim.

**Gut:** the joint compatibility criterion still pulls; two failures explained the right place
to change allocation. **Reasoned:** before tackling the less-dominant parent, isolate the corner
where assigning all surpluses to one edge cannot even leave a strict parent. Its geometry may
be simpler than the intermediate regime.

### MI108 — B46: the corner that requires a two-edge parent allocation (2026-10-16 14:24 BST)

Question: cover the three-surplus corner W<=q=a+b+c, where a strict parent cannot be formed
by putting all q on W. This is the complementary allocation-feasibility question, not another
root-order widening. Record searched: W.*q.*two, obligate.*split, surplus.*corner -> no
default-record hits; MI094-107 and the actual allocation sources read. No novelty claim.

**Hand candidate (PROOF-SKETCH).** Parameters satisfy u+v+q=W+Z,6<=u<=v, W>=Z>0,
v+W<=28,1<=a<=b<=c<=5. Since W<=q, u+v<=Z<=W<=q<=15. Hence6<=u<=7,v<=9,
and W,Z in12..15. Put B=b+c, d=W-v. Then B in8..10, d in6..9, a<=5. Allocate b,c
to W and a to Z, giving parent magnitudes R=W-B>0 and S=Z-a. Positivity follows from
u+v+a>B; also R<=a<=5<u,v and S>R. The ordinary alternating parent is therefore valid.
Put all allocated positives AFTER their respective negative edges. After normalization the
selected coordinates are
+b at0, +a at d-a, +c at b, +v at d, +u at B, -W at W, -Z at D=u+B.
The seven-cycle closes as d -> W ->0 ->b ->B ->D ->d-a ->d.

All coordinates are distinct in the STRICT order
0<d-a<b<d<B<W<D. Here d>=u>=6>a,b,c. Moreover
d-a-b=(W-q)+(c-v)<0 and d-B=(W-q)+(a-v)<0. Finally W>B since R>0,
and D-W=u-R>0. The span D=u+B is14..17. This proves the literal-collision part
for the whole corner, without trials of orders or cuts.

**Reflection check.** Every pair not involving D has sum at most W+B<=25. Also
D+B<=27, with equality only when u7,B10,D17. Thus a root0 collision can only
come from D+W=27 or this D+B equality. The small bounds exhaust these analytically:
- D14 forces u6,B8, hence a=b=c4,q12,u=v6,W=Z12: D+W26, safe.
- D15 forces u6,B9 (u7,B8 would give q<=12<u+v). Then(b,c)=(4,5), a3 or4.
  At a3,q12,u=v6,W=Z12, D+W27. At a4,q13,W13, D+W28, safe.
- D16 forces u6,B10 (u7,B9 would give q<=13<u+v); W>=12, so D+W>=28 and
  D+B26. Root0 works throughout.
- D17 means u7,B10, b=c5. At a4,q14 the only parameters are u=v7,W=Z14.
  At a5,q15 they are(u,v,W,Z)=(7,7,15,14) or(7,8,15,15).

Use root0 except these four parameter configurations, whose normalized position sets/roots are:

|u,v,W,Z;a,b,c|shape|root|
|---|---|---|
|6,6,12,12;3,4,5|0,3,4,6,9,12,15|1|
|7,7,14,14;4,5,5|0,3,5,7,10,14,17|1|
|7,7,15,14;5,5,5|0,3,5,8,10,15,17|3|
|7,8,15,15;5,5,5|0,2,5,7,10,15,17|2|

Their translated folded labels are respectively
{1,4,5,7,10,11,13}, {1,4,6,8,9,11,12}, {3,6,7,8,9,11,13},
{2,4,7,8,9,10,12}; each is distinct and every index fits. Reserve the seven pairs,
fill remaining slots, permute selected tokens. This is a uniform corner hand candidate.
It does not claim every physical solution must allocate moves this way; necessity is only
for the stated strict four-move-parent allocation when W<=q.

**Predictions BEFORE validation:** exactly20 targets, q subtotals3,4,5,8 at12..15. Direct
low-quadruple/high-triple domain equals signed parameters filtered W<=q. Every explicit
formula must certify; exactly four need the listed nonzero roots. Cap30 inputs/one CPU
second, no order search or added repair. Controls: every all-q-on-W parent has nonpositive
remainder; root0 in the four exceptions fails by pair reuse; coverage-preserving wrong sums
rejected. Unexpected: D16 cases all work at root0, despite being beyond the universal
seven-position span15 bound. Record that separately from the three D17 boundary cases.
Both schedules paused; independent work and proof statuses do not wait on review.


### MI109 — B46 result: strict two-edge corner constructed (2026-10-16 14:27 BST)

All20 targets certify by the explicit formula. Signed and direct target domains agree, with
q counts3,4,5,8. Spans14/15/16/17 occur1/3/13/3 times; exactly the four listed nonzero
root corrections occur. All20 single-edge strict-parent remainders are nonpositive. Omitting
any prescribed nonzero root fails, wrong sums fail, and all13 span16 cases succeed at root0.
CPU0.006461 s; raw outside git SHA256
`f7c46c9182bd125ef2159022b9cf1f5949bfba75f95d524aec0c42b06f2c05a0`.
The whole corner is COMPUTED; MI108 remains a uniform hand candidate pending independent read.

**Niggle sweep:** W<=q is used to prove u+v<=Z and hence the small corner bounds, not treated
as a physical impossibility theorem. Both parent remainders are strictly positive; coordinate
order follows from the inequalities before roots are considered. The four exceptions are
exhausted through D=u+B, not selected from a successful run. Every token appears once and the
literal checker verifies sums and coverage separately. Prior candidate statuses are preserved.

### MI110 — checkpoint and exact remaining parent regime (2026-10-16 14:27 BST)

This continuation answered two different allocation questions:
- With R=W-q>=Z, the all-after architecture has an exact3-by-3 root/order compatibility
  test. Complete checks give1,476 targets and exactly two exhausted failures. MI106's one-before
  rule repairs both; the same named1,478-target regime is now COMPUTED. No universal all-after
  hand theorem is claimed. The two failures and their reasons remain.
- With W<=q, assigning the surpluses to both negative edges gives a strictly ordered seven-cycle
  of span14..17. The whole20-target corner certifies, with a short hand proof candidate.
Counts are not added to other earlier probe families, which can overlap. No full E28 or L8
claim follows. These are bounded parts of the three-surplus even-target region.

**Remaining question.** After separating matching cases (MI099), W22 (MI101), W<=q (MI108)
and the dominant remainder (MI104-107), the unmatched interior still to resolve is
W>q and0<R=W-q<Z. This is the next natural parent-order regime, not a need for a larger census.

The same two-variable reduction extends by hand. Put A=v-R=Z-u>0 and take the four-position
parent0,A,v,Z, whose -R edge is v->A. All-after subdivision has five fixed positions
C={0,A,v,Z,A-q}, and variable positions A-q+first and A-last. In the unmatched regime
A!=q (otherwise W=v); thus the fixed five are distinct. Their minimum/maximum, and hence
the allowed root interval, do NOT depend on the positive order. Normalize C by subtracting
m=min(0,A-q), and put b=A-q-m. For each root r, internal levels first and q-last must avoid
the LITERAL set L={c-b:c in normalized C}, as well as the REFLECTED set
F_r={27-2r-b-c:c in normalized C}. They must also avoid the variable cross-pair equation
2b+first+(q-last)+2r=27. This is the augmented first/last compatibility graph to test next.
Unlike B44, the literal set has genuine interior levels; it cannot be discarded.

Its span is at most25: if A>=q it is max(v,Z)<=22; if A<q and v>=Z it is W<=22;
otherwise it is u+q. Original sorting gives u+3v+q<=56 and v>=u, hence
u+q<=14+3q/4<=25.25, an integer<=25. Some roots may therefore be scarce; no existence
of an augmented-graph edge is claimed. No new experiment or block is opened by this next-step
derivation. It names the missing inference and what would advance it.

**Fresh choice / gut:** still warm toward the compatibility graph and the way failures choose
which endpoint to alter. The two failed all-after cases were informative, not a reason to grow
a solver. **Reasoned verdict:** there is real structural movement, with one open parent regime
now isolated; general root availability there remains uncertain. The next cheap test is that
augmented graph, with a preregistered literal-collision control, before choosing further allocations.

Existing MI099/101 carrying request remains pending. Send one concise READ-LEDGER update for
this checkpoint; do not add routine proof-review jobs while that read is pending. Continue
independent work without a review gate. Both automatic schedules stay paused.

### MI111 — B47: test the remaining parent rather than assume it deserves repairs (2026-10-16 15:29 BST)

**Question:** in the unmatched three-surplus interior W>q,0<R=W-q<Z,W<22,
does the all-after parent of MI110 admit a literal/reflection-compatible first/last edge?
This would complete this parent's coverage or exhibit its exact limits. It is a condition on
our construction, not a necessary condition for arbitrary odd partitions or the full L8 claim.

**Capture / fresh choice:** specific curiosity, with momentum attached. The owner's question
about inherited warmth is fair: the earlier label was too unqualified. I would choose this
bounded test afresh, but not commit in advance to repairing every exception. A broad success
supports seeking a common explanation; many failures of one kind support changing the parent.
Record searched: literal.*compatibility, first.*last.*graph, smaller.*remainder -> no hits
in the default search; MI104-110 and the actual B44/B46 sources read directly. Existing
Tan-Teh exchange precedents remain credited; this is an internal finite-construction test,
not a new literature or novelty claim. Cloud's new0f0939c1 is an unrelated instinct entry,
read and preserved; no new carrying review is assumed.

**Exact instrument:** A=v-R=Z-u>0, m=min(0,A-q), b=A-q-m. The fixed five positions are
C={0,A,v,Z,A-q}-m. For first item i and last item j, i!=j, the variable levels are
p=a_i and s=q-a_j. Require no fixed-core reflected pair, p,s outside the literal set
L={c-b:c in C}, outside F_r={27-2r-b-c:c in C}, and
2b+p+s+2r!=27. The two variables are distinct because the remaining item is positive.
The selected coordinates, independently rebuilt by following the cycle, are +v at0,
-W atv, the three positive steps from A-q to A, +u atA, -Z atZ, all shifted by r-m.
Compare every graph edge against direct folded labels, preserving item identities when equal.

**Predictions before any run:** graph/direct equivalence and full certificates MUST hold;
signed and independent sorted-target domains MUST agree. Blind expectation: some fixed
all-after targets will fail, possibly already through literal overlap; retain a zero-failure
outcome too. No exact family count predicted. Test at most5,000 targets/500,000 root-order
comparisons/five CPU seconds; cap means UNKNOWN, no increase or fallback solver.

**Controls / counterfactuals:** (u,v,W,Z;a,b,c)=(6,6,15,11;4,5,5), sorted first4/last5,
reuses the old0 position; reflection-only checks should accept at root0 while literal checks
reject. First5/last4 should give a valid certificate. The nonzero-offset control
(6,14,12,11;1,1,1) has b=2 and should certify at root0. Matching control
(6,10,10,9;1,1,1) has A=q and must be rejected before any fixed-set deduplication.
Coverage-preserving wrong target sums must fail the independent checker.
**Unexpected check:** distinguish targets with NO literal-admissible item order from those
whose orders survive literally but lose all roots through reflection; record the maximum
actual span separately from MI110's bound25. These distinguish a scaffolding failure from
a translation problem. Stop after this architecture's complete capped diagnosis; no repairs
or more general cycle search are part of B47. Both schedules remain paused.

### MI112 — B47 result: all failures are one literal obstruction (2026-10-16 15:31 BST)

Signed and independently sorted target domains agree:2,760 inputs,2,648 constructed,
112 architecture failures. All181,956 graph/direct root-order comparisons agree; all controls
pass. Root classes15,599 completed/4,767 valid-core-no-completion/9,960 bad-core. Every failure
already has no literal-admissible order; there is NO reflection-only exhaustion. Actual spans
9..25, with the unique span25 tuple(10,10,18,17;5,5,5) succeeding at root0. CPU0.911747 s,
raw outside git SHA256
`a989a08e571ff50a5668fc70c9b320eda257f3e02323dd5dab0f5b77cd688633`.
Blind expectation of some failures confirmed; existence of a root whenever an order survives
is COMPUTED for this finite domain, not a hand universal theorem.

**Hand classification (PROOF-SKETCH).** In MI111 the literal set simplifies to
L={q-A,q,q+R,q+u,0}. Only d=q-A=W-v can lie strictly between0 and q. Thus first
item must differ from d and last item must differ from q-d. Let I and J be their respective
allowed item-index sets. A literal order exists iff some i in I,j in J have i!=j. If either
set is empty, all three steps equal s, and d=s or d=2s. Conversely either equality forbids
every first or every last item. The only other possible obstruction would be I=J={k}.
Then each of the other two items equals both d and q-d, so q=2d; the sum of those two
items already equals q, forcing the positive third item to0, impossible. This exhausts the
literal obstruction for ANY three positive item sizes in this parent with five distinct fixed
positions. It is a theorem about this parent, not all partitions.

The112 observed failures all have equal a=b=c=s. They split into45 with
W=v+s,Z=u+2s and67 with W=v+2s,Z=u+s. Counts by s=1..5 are12/17/9/6/1 in the
first case and8/17/18/14/10 in the second. This classification is checked against the
completed raw record, not used to erase failures. Both startup controls passed this continuation.

**Surprise / gut:** the obstacle is much cleaner than112 exceptions: the selected run is forced
through the old0 coordinate. This earns curiosity in a DIFFERENT cycle decomposition rather
than trying more roots. **Reasoned verdict:** all-after has a structural limit; translation
cannot fix it. The failure itself tells us how to split the surplus across the two donors.

### MI113 — B48: split the literal trap into a cancelling pair of cycles (2026-10-16 15:31 BST)

**Question:** can the112 classified equal-step traps be bypassed uniformly by allocating their
surpluses to both donors, creating a three-cycle and a four-cycle instead of a seven-cycle?
This changes the scaffold identified in B47; no list of112 custom repairs is proposed.
Record searched: literal.*compatibility, first.*last.*graph, smaller.*remainder -> no default
hits; MI099/108/110-112 and the materializer/checker read. No new external theorem invoked.

**Hand reduction (SKETCH):** write the two cases as negative magnitudes H=h+s and G=g+2s,
where(h,g)=(v,u) for W=v+s or(u,v) for W=v+2s. Allocate one s to H and two s to G.
The reduced negative magnitudes are h and g, exactly cancelling the two original positive
steps. A three-cycle uses selected positions {0,s,h+s}; a four-cycle uses {0,s,2s,g+2s}.
For the first cycle put +s at0,+h at s,-H at h+s; for the second put +s at0,+s at s,
+g at2s,-G at g+2s. Translate the two cycles independently and require all seven folded
labels distinct. This directed-cycle identity holds symbolically; availability of disjoint
labels is the bounded question, not assumed.

**Predictions BEFORE execution:** all112 targets have a pair of legal roots within0..27;
independent direct target domain agrees with the equal-step trap equations and prior failure
set. Direct seven-label test and separate bitmask disjointness test agree for EVERY root pair;
chosen full certificates pass. Cap120 targets/50,000 root pairs/two CPU seconds. A failure
or cap is retained; no third cycle, new size allocation or solver fallback.
Controls: same root on both cycles must reject shared labels; sums corrupted while retaining
coverage must reject. Swap donor assignments without changing cycle lengths on an unequal-
donor fixture: the resulting labelled selected-token construction must reject. Equal target
values still represent distinct bin owners and item identities. **Unexpected check:** test
whether fixing the four-cycle at its FIRST individually legal root loses solutions that a
joint root choice recovers; report this separately. The main prediction permits joint roots.

If successful, the next cheap audit is set equality of the disjoint three-surplus regimes,
using the existing checked witnesses; no larger target census is authorized by this block.
Gut: the wall now suggests a genuine bypass. Reasoned: run one fixed two-cycle mechanism,
and stop rather than expanding it if that mechanism fails. Both automatic schedules paused.

### MI114 — B48 result: the uniform two-cycle bypass succeeds (2026-10-16 15:34 BST)

All112 classified traps have certificates from the prescribed three/four-cycle split.
Signed, direct-target and prior-failure sets agree. All25,612 mask/direct root-pair checks
agree; shared-root, wrong-donor and wrong-sum controls pass. Unexpected: the FIRST individually
legal four-cycle root always leaves room for a three-cycle; zero targets need joint backtracking
of the four-cycle root. This stronger finite observation is COMPUTED, not assumed as a general
packing theorem. CPU0.254758 s; raw outside git SHA256
`5c0790e809234bd0df79cdc4c8ce4a580bc0233f65713bf4edd34d6142e79e7d`.

The owner asked whether an obstacle should be attacked or bypassed. Here the literal wall was
made by our seven-cycle scaffold. Factoring that scaffold into two cancelling cycles bypasses
all its failures with one rule. The classification and cycle identity remain hand SKETCH;
placement availability and complete finite certificates are COMPUTED. B47's failures stay.

### MI115 — B49: audit the exact three-surplus subfamily (2026-10-16 15:34 BST)

**Question:** do the completed constructions cover EXACTLY every sorted even E28 tuple with
t4<112,t5=112,t6>112? No larger E28 census is claimed. These tuples have four low targets,
one112 and three strictly positive surpluses1<=a<=b<=c<=5. The proposed partition is:
matching magnitudes999; unmatched W22:11; unmatched W<22,W<=q:20;
unmatched W<22,R=W-q>=Z:1,478; remaining unmatched W<22,0<R<Z:2,760.
Predict5,268 distinct targets, no overlap between these five REGIMES. The seven-target B45
stripe overlaps its own parent regime; select its two missing witnesses rather than add counts.
B48 replaces the112 B47 failures without adding targets. Source provenance remains explicit.

Record searched: three.surplus,5268,5,268 -> no default hits; B42-48 source domains and MI099-114
read directly. This is a set/certificate audit, no new theory or search mechanism. Existing
Tan-Teh credit stands. Independently enumerate sorted even low quadruples68..110 and sorted
high triples114..122 with sum784. The resulting set must equal the assembled witness keys.
Recheck all complete partitions with (1) the existing multiset checker, and (2) an independent
integer-bitset checker with exact bin sums and no duplicate odd tokens. Verify source digests.

**Predictions/controls BEFORE audit:**5,268 distinct complete certificates and five disjoint
nonempty regime sets of the counts above. Removing any regime must break equality; inserting
a duplicated odd token must reject. The valid even E28 tuple(68,68,96,100,112,112,114,114)
is OUTSIDE the audited subfamily and must not appear. **Unexpected check:** equal-step triples
occur in several regimes; count them by s to ensure the112 bypass targets are not mistaken
for the whole equal-step region. Cap6,000 certificates/three CPU seconds, no certificate
generation or fallback solver. A missing/overlap/checker failure stops with the target retained.

Gut: the bypass earns a coverage audit, not another promise of warmth. Reasoned: close this
named finite subfamily cleanly before deciding whether its mechanisms suggest a wider argument.
Both automatic schedules remain paused; existing reviews do not gate this finite audit.

### MI116 — B49 result: all5,268 targets in the named subfamily have certificates (2026-10-16 15:35 BST)

The five regime sets are disjoint, with counts999/11/20/1,478/2,760, and their union equals
the independent sorted-target domain EXACTLY. All5,268 complete partitions pass both the
existing multiset checker and an independent bitset/exact-bin-sum checker. Source digests
agree. Removing any regime breaks equality by its exact cardinality; a duplicated odd token
is rejected by both checkers; the valid two-surplus outside-slice control is absent.
Equal-step triples occur762 times, with s=1..5 counts239/195/148/108/72. Thus the112 literal
traps were a particular subset of the equal-step tuples, not that whole slice. CPU0.519423 s;
raw outside git SHA256
`1603e5f50221531c9b6823fa6b9015337216ce72d6bd5882a7d8b24aba7a8bcd`.

**Delivery receipt, 15:38 BST:** the complete3,882,033-byte certificate is also immutable in
the shared store at `cited/instinct/b49-three-surplus-1603e5f50221531c.json`; upload receipt
matches that digest and the manifest entry names B49/MI116 and commit164fd8a4. It contains
all target tuples, assigned bins, regime tags and source digests, so a reader can check the
finite coverage without access to the earlier local raw files. No credentials or private paths.

**Exact scope, COMPUTED:** every sorted even tuple68<=t1<=...<=t8<=122 with sum784,
t4<112,t5=112,t6>112 has a partition of the28 odds1..55, bin cardinalities2,2,4,4,4,4,4,4.
This is the complete named three-surplus subfamily, NOT all even E28, mixed parity, earlier
exceptional levels, or L8. The hand constructions keep their existing review labels; machine
certificate availability is not relabelled an all-hand proof. No novelty claim.

**Niggle sweep:** three niggles checked. Target families might overlap: exact disjoint set
audit says they do not, while B45's five already-covered stripe targets are intentionally
deduplicated. Sorted-only sum verification might hide owner mismatches: independent checker
requires each bin's sum to equal its assigned target, and uses bits to reject repeated tokens.
The112 repair targets might be mistaken for all equal-step triples: actual count762 prevents
that overstatement. All resolved; full-target scope limitations stay explicit.

### MI117 — what the wall taught: a prefix swap and the next genuine obstacle (2026-10-16 15:35 BST)

There is a short general reason behind MI112's literal classification. This is a supporting
hand inference (SKETCH, no separate proof entry or routine review request), with no claim of
novelty. Let k>=2 positive steps have sum q and let d be one forbidden proper prefix level.
If an ordering hits d, split its items into a left part of sum d and a nonempty right part.
If the multiset is nonconstant, some left item x and right item y differ: otherwise every
cross pair agrees, hence every item agrees. Reorder within each part so x is last on the
left and y first on the right, then swap x,y. Every earlier prefix is below d, every prefix
after both swapped items is above d, and the one changed prefix is d-x+y!=d. Thus one swap
avoids d. For a constant multiset s repeated k times, every order has the same proper prefix
levels s,2s,...,(k-1)s; these and only these d are unavoidable.

Applied to the same small-remainder parent, its only possible internal literal collision
is the old0 coordinate, at d=W-v. Hence nonconstant surplus sizes can always avoid it.
For constant sizes and d=j*s, the equations give W=v+j*s, Z=u+(k-j)*s. Allocate j steps
to W and k-j to Z: the reduced negative magnitudes are exactly v,u. This yields two
cancelling cycles with shapes {0,s,...,j*s,W} and {0,s,...,(k-j)*s,Z}.
For k=3 these are precisely B48's three/four cycles. This explains why the bypass works at
the directed-cycle level without112 custom patches. Availability of disjoint FOLDED labels
after translation remains a separate question; B48 certifies it only on its stated domain.

For four positive surpluses, the same argument would remove the literal-prefix obstacle,
and constant-step traps would split into3+5 or4+4 cycles. Eight selected coordinates then
need distinct folded labels. That packing/translation question is the next mathematical
obstacle; the six-position translation theorem cannot simply be reused. No four-surplus
experiment or claim is opened here. The payoff would be a common construction beyond the
one-neutral-target slice, rather than more exceptions inside the completed slice.

**Fresh choice / gut:** surprise became understanding: a wall built by one cycle can disappear
when it is factored. Specific curiosity remains toward that factorization and the eight-point
packing question. **Reasoned:** this continuation moved from2760 cases to one obstruction,
then to a complete5,268-target subfamily and a general prefix argument. It does not justify
indefinite case repair. Publish the milestone and a concise mentor pointer; existing MI099/101
review stays pending, no new review queue or dependency halt. Both heartbeats stay paused.

### MI118 — B50: does the cancelling split survive eight selected positions? (2026-10-16 15:46 BST)

**Question:** extend MI117's constant-prefix bypass to FOUR equal positive surpluses s,
so q=4s, in the unmatched small-remainder parent W<22,0<W-4s<Z. The literal traps have
W-v=j*s,1<=j<=3, hence W=v+j*s,Z=u+(4-j)*s. The two prescribed shapes are
S={0,s,...,j*s,W}, T={0,s,...,(4-j)*s,Z}; they have3+5,4+4 or5+3 points, eight in total.
Each closes as j positive s steps, +v, -W (and4-j s steps,+u,-Z). This directed-cycle
identity is MI117's hand SKETCH. The missing inference is disjoint folded labels after
independent translation, not another single-cycle endpoint repair.

**Capture:** specific curiosity about whether factoring scales by one more active position.
A failure would identify the limit of the factorization, not oblige a custom repair table.
Record searched: four.*surplus,eight.*packing,cancelling.*cycle -> no default hits; MI111-117,
B48 source and literal checker read directly. Existing exchange precedents remain credited;
no new external result or novelty claim. Cloud flags checked, no new actionable pointer.

**Predictions BEFORE execution:** every target in this exact equal-step-trap domain admits
legal independent roots in0..27. No exact target count predicted. Derive signed parameters
u>=6,v>=u,W>=Z,v+W<=28,1<=s<=5 and compare against independently sorted even low
quadruples68..110 with four high targets112+2s and total784. Direct eight-label check and
independent masks must agree at EVERY root pair; selected full partitions must pass the
literal multiset checker and an exact-bin bitset checker. Keep bin identities when values
coincide. Cap300 targets/100,000 root-pair comparisons/three CPU seconds; UNKNOWN at cap,
no new allocation, cycle class or solver fallback. If the all-family prediction fails, stop
at its complete diagnosis rather than add repairs within this block.

**Controls / counterfactuals:** same-root shapes share0 and must reject. Explicit fixture
(u,v,W,Z;s,j)=(6,6,21,11;5,3), target(68,68,70,90,122,122,122,122), should certify at
roots0 for S and2 for T; swapping its negative-bin assignments must fail. Duplicating a
token and coverage-preserving wrong sums must fail independent checks.
**Unexpected check:** anchor whichever cycle has MORE points at its first individually legal
root (S on a4+4 tie). Does this lose targets for which joint root placement succeeds? Record
losses and individually impossible shapes separately. This stronger anchor rule is diagnostic,
not an assumption of the main prediction. Both schedules paused; review remains nonblocking.

### MI119 — B50 result: eight-position split passes all133 constant traps (2026-10-16 15:48 BST)

All133 signed/direct target keys agree and have literal certificates. All29,461 mask/direct
root-pair comparisons agree; same-root, wrong-negative-owner, duplicate and wrong-sum controls
pass. No individually impossible shape, and the FIRST individually legal longer-cycle root
always leaves a placement for the shorter cycle (S anchored on4+4 ties). CPU0.090257 s,
raw outside git SHA256
`665da55308b4e401a424e56d26c43947615c7705b924114ce2c6426a6aaff8bd`.
This extends the prescribed factorization to eight active positions in this exact133-target
family, COMPUTED; it is not all constant-surplus targets or all four-surplus E28.

**Gut:** confidence in the factorization as a useful representation, not confidence in an
unproved universal packing theorem. **Reasoned:** the constant case may be a visible instance
of a subset-total identity. Test that wider identity with a canonical choice rather than
exploit the133 certificates to manufacture a hand-case review queue.

### MI120 — B51: canonical subset cancellation for four positive surpluses (2026-10-16 15:48 BST)

**Question:** for four positive steps1<=a<=b<=c<=d<=5, q their sum, can a proper subset
of sum D=W-v always be used in a fixed cancelling two-cycle construction? This target
domain is all sorted even E28 with t4<112,t5>112 and a NONEMPTY PROPER subset of the
four steps summing D. It is not restricted to MI118's parent or unmatched magnitudes;
overlap with133 constant fixtures is expected and not added as new coverage.

**Hand identity (SKETCH):** assign that subset I to W. Then W=v+sum(I), and the target-sum
identity gives Z=u+sum(J) for its complementary subset J. Each part gives a closed cycle:
positive steps in increasing item-index order, +v, -W for I; positive steps,+u,-Z for J.
The selected shape is its positive proper-prefix coordinates, the full subset total, and
the corresponding negative magnitude W or Z. Shapes have3+5,4+4 or5+3 coordinates.
They are literal-distinct individually because all steps and u,v are positive; the open
issue is the two cycles' eight distinct folded labels after translation.

**Fixed choice:** among nonempty proper item-index subsets of total D, choose the one with
fewest items, then lexicographically smallest indices. Sort within each part by index.
Search only the two root intervals0..27-span. No alternate subset, within-part order,
negative assignment, or general cycle solver on failure. This is a diagnostic of one common
rule, not exhaustion of all two-cycle constructions. Record searched: subset.*cancell,
four.*surplus,prefix.*factor -> no default hits; MI117-119 and B48/B50 sources read.
No external theorem or novelty claim is invoked.

**Predictions BEFORE run:** tentatively all targets in this proper-subset domain certify
under the canonical rule. Independent domain: sorted low quadruples68..110 and high
quadruples114..122, total784; membership via subset-sum dynamic programming with item count
1..3, independently of canonical masks. Compare every root pair's eight direct labels with
independent masks; chosen full partitions pass both existing multiset and bitset/exact-bin
checkers. Cap15,000 targets/four million root pairs/15 CPU seconds; cap means UNKNOWN,
never increase it. Keep every failed target, no repairs during B51. No exact count predicted.

**Controls:** unequal fixture(u,v,W,Z;steps)=(6,7,10,9;1,1,2,2), canonical subset indices
(0,2), should certify at roots0 and4. A wrong subset(0) at roots0 and2 must fail the
selected-token permutation check; it has distinct folded labels, so balance is tested
separately. Same-root overlap, duplicated-token and coverage-preserving wrong-sum variants
must reject. No-subset target(68,68,70,90,122,122,122,122) has D=15, hence DOES have
a proper subset (three5s), and must be included; instead use the prior span27 fixture
(70,70,70,86,122,122,122,122), with D14, as the explicit NO-subset control.
**Unexpected check:** first individually legal longer-cycle root (I on ties) versus joint
placement; report any losses rather than silently relying on the stronger anchor observation.
Compare constant-trap133 keys with this domain as a subset, no additive counts.

Gut: the subset identity makes the mechanism worth one broader test. Reasoned: canonical
success would give a common constructive subfamily; failure would locate the price of the
fixed choice. Both automatic schedules remain paused; carrying reviews are nonblocking.

### MI121 — B51 result: canonical subset rule works; greedy anchoring fails (2026-10-16 15:51 BST)

All4,938 target keys agree with the independent sorted/DP domain and have full certificates.
All993,670 mask/direct root-pair comparisons agree. Subset cardinality pairs3+1,2+2,1+3
occur1,471/2,639/828 times. All133 constant fixtures are included, not added. Both partition
checkers and all controls pass. No individually impossible shape. CPU2.841127 s, raw outside
git SHA256`02851403bc63388f571a9f52dfb6f4202616a2df706e4a2eb8f0e1f07174a7a1`.
The proper-subset construction is COMPUTED on this exact domain, no general hand placement
theorem follows. MI120's control wording was awkward: D15 with four5s is INCLUDED, D14 is
EXCLUDED; the pre-run text and instrument both specify those actual expected outcomes.

**Unexpected failure retained:**56 targets lose all completions if the longer cycle is fixed
at its FIRST legal root. Joint translation resolves every one without changing the canonical
subset or within-part order. Example(u,v,W,Z;steps)=(6,7,16,13;3,4,4,5), target
(68,70,80,86,118,120,120,122): subset indices(1,3), shapes S={0,4,9,16},T={0,3,7,13}.
At S root0 its labels are{0,4,9,11}; every T root0..14 is blocked, except7 and12 which
already reuse a pair internally. S root2,T root0 are disjoint: labels{2,6,9,11} versus
{0,3,7,13}. Thus the stronger greedy rule seen in B48/B50 is genuinely REFUTED here;
joint placement matters. The headline all-target prediction survives with its original scope.

**Gut:** pleased that the diagnostic found a real limit to a shortcut instead of another
unqualified success. **Reasoned:** separate arithmetic factorability from geometry. The subset
identity is wider than splitting only the four small steps; all six positive moves can be
partitioned between the two negative moves.

### MI122 — B52: factor the full positive move multiset before embedding it (2026-10-16 15:51 BST)

**Question:** in the complete FOUR-surplus target domain (t4<112,t5>112), take positive
moves u,v,a,b,c,d and negative moves-W,-Z. Whenever a positive subset sums W, its complement
sums Z. Can one canonical factorization always be embedded by two independent translations?
This is broader than B51: both large positives may belong to the same cycle, or an original
matching magnitude may form a two-cycle. No whole E28 claim; no experiment on un-factorable
move multisets is included.

**Exact structural boundary (supporting hand SKETCH):** in this selected-token permutation
architecture, every nontrivial cycle needs a negative move. With exactly two negative moves
there are at most two cycles. A two-cycle-component factorization exists arithmetically iff
a subset of the SIX positive moves sums W. If no such subset exists, the architecture needs
one cycle containing both negative moves. This is not a necessary condition on arbitrary
partitions or burning witnesses; fixed-role cycle covers are a sufficient construction.

**Canonical rule BEFORE run:** choose a positive subset of sum W with the fewest items, then
lexicographically smallest bin-owner tuple, where owners are0,1,4,5,6,7. Sort each part by
(positive step size,owner). Its shape is0,successive proper sums,full part sum (the negative
magnitude), so the corresponding cycle closes through that negative edge. Translate these
two fixed shapes only. No alternate positive subset or within-part order on failure.

Record searched: zero.sum.*component,positive.*subset.*negative,factor.*cycle -> no default
hits; MI117-121 and B51/checker sources read. Direct finite algebra, no external theorem or
novelty claim. **Predictions:** tentatively all arithmetic-factorable targets certify under
this canonical rule. Independently enumerate the whole sorted-low/high domain, count its
factorable/un-factorable parts by a positive-subset DP, and match the signed/canonical domain.
This is a target-set count, not a search for partitions of the un-factorable remainder. B51's
4,938 keys must be contained, without assuming the new canonical choices reuse old witnesses.

Must compare all root pairs by direct labels and masks, and all chosen partitions by both
literal checkers. Cap15,000 constructed targets/four million root pairs/15 CPU seconds; cap
means UNKNOWN. Retain every failure, even if an old B51 witness exists; no fallback solver.
**Controls:** target(68,68,88,100,114,114,116,116) has W12=u+v and Z6=a+b+c+d; the
canonical subset is the two large positive owners(0,1), shapes{0,6,12} and{0,1,2,4,6},
which should certify at roots0/3. The target(70,70,70,86,122,122,122,122) has no positive
subset summing W21 and must be excluded. Same-root overlaps, duplicated-token and wrong-sum
variants reject. **Unexpected:** count first-longer-root losses and individually rootless
shapes, separately from joint packing failures; B51 has already killed the greedy conjecture.

Gut: the cleaner question is what can be factored at all, followed by placement. Reasoned:
one canonical test isolates the arithmetic boundary and the geometric price. Both schedules
remain paused; pending hand reviews do not gate this independent finite diagnostic.

### MI123 — B52 result: arithmetic boundary isolated, two canonical packing obstructions (2026-10-16 15:55 BST)

Full sorted four-low/four-high domain:7,828 targets. A positive subset sums W in7,223;
the other605 are arithmetically primitive for two-cycle factorization, counted only.
Canonical fixed shapes certify7,221/7,223, with1,469,303 direct/mask root-pair comparisons
agreeing, independent direct/DP domain equality and both partition checkers/controls passing.
Positive part sizes4+2,5+1,3+3,2+4,1+5 occur1,495/399/3,597/1,681/51. No individually
rootless shape;193 successful targets require leaving the first legal longer-cycle root.
CPU4.592863 s; raw outside git SHA256
`e25cb282fabd0cade077a3482743ff735c94f89cc25af39707358b64b99e66d2`.
The blind all-canonical claim is REFUTED. Every failure is retained; no alternate subset
was searched in B52. These are construction failures, not nonburnable targets.

**Two exact failures:**
- (u,v,W,Z;steps)=(8,8,20,6;2,2,2,4), target(72,72,72,100,116,116,116,120).
  Canonical part for W is4+8+8, shape{0,4,12,20}; the other is2+2+2, shape{0,2,4,6}.
- (8,10,18,8;2,2,2,2), target(72,76,76,96,116,116,116,116).
  Canonical part is8+10, shape{0,8,18}; the other is2+2+2+2, shape{0,2,4,6,8}.

**Hand obstruction (SKETCH):** every step is even, so each cycle stays on one parity of
physical indices. Identify the14 positions of that parity with0..13. If the other cycle
uses opposite parity, reflect it by x->27-x first; this preserves folded labels and yields
the same parity. Its equally spaced block becomes an interval in the14-position line,
possibly reflected, of length4 or5.
In the first case the scaled sparse shape is{0,2,6,10}. Its internal complement gaps have
length at most3; after any translation within0..13 both exterior gaps also have length at
most3 (span10 leaves3 exterior positions). A four-position interval cannot fit. Permuting
the positive moves merely permutes the gaps2,4,4, so no within-part order fixes this.
In the second case the scaled sparse shape is{0,4,9}, whose complement gaps and exterior
gaps have length at most4; a five-position interval cannot fit. Reversing its two positive
moves gives gaps5,4 instead of4,5 and changes nothing. This obstruction concerns the chosen
FACTOR PARTITION, not just the canonical order or greedy root.

**Forced alternative arithmetic:** in case1, the small donor6 can receive either2+2+2
(failed partition) or2+4 (the only other multiset choice); in case2, donor8 can receive
either four2s (failed) or the single8. Thus each has one alternative positive-multiset
factorization, up to equal-item identities. This suggests the next test without a general
subset/order search. Gut: the obstruction is informative rather than frustrating; it says
that a minimal-cardinality factorization can be geometrically rigid. Reasoned: test these
two analytically forced alternatives, then leave the primitive605 as the next real boundary.

### MI124 — B53: two forced factorization changes and complete factorable-domain audit (2026-10-16 15:55 BST)

**Question:** do the two unique alternative positive-multiset partitions bypass MI123's
interval obstruction, completing the arithmetic-factorable four-surplus domain? Record
searched: gap.*interval.*packing,canonical.*factor,605 -> no default hits; MI120-123 and
B52's two exact failures read directly. No novelty claim or external theorem used.

**Explicit formulas BEFORE validation:** case1 selected owner->index is
{4:0,5:2,0:4,1:12,2:20,6:8,7:10,3:14}. The W cycle has positives2,2,8,8 and
shape{0,2,4,12,20} at root0; the Z cycle has2,4 at root8. Case2 is
{4:0,5:2,6:4,7:6,1:8,2:18,0:3,3:11}, W positives2,2,2,2,10 at root0,
and the single-positive8 cycle at root3. No alternative beyond these two formulas is tested.

**Predictions:** both materialize and pass multiset plus exact-bin/bitset checks. All7,221
old witnesses remain unchanged; their union with the two formulas equals an independently
sorted/DP-enumerated factorable domain of7,223 within7,828 four-surplus targets. Omit either
new target and equality fails by one; duplicate-token and wrong-sum controls reject.
**Unexpected check:** validate the gap obstruction against ALL unique positive orders of
the OLD sparse parts: three permutations of4,8,8 and two of8,10, with every root pair
against the old dense block. Predict all928 physical root-pair checks reject. This is a
diagnostic of the two failures, not a search for another construction. Cap2 new formulas,
2,000 old-root checks and four CPU seconds INCLUDING rechecking7,221 certificates and direct
domain equality. Failure/cap is retained, no widened family or fallback.

Gut: prefer an explained factorization choice over changing roots indefinitely. Reasoned:
finish this finite boundary honestly; the605 primitive move multisets are still unsearched.
Both schedules paused; no new review queue or review dependency is created.

### MI125 — B53 result: all7,223 factorable four-surplus targets constructed (2026-10-16 15:58 BST)

Both explicit alternative formulas pass both literal partition checkers. All7,221 prior
witnesses remain unchanged; the resulting7,223 keys equal the independent sorted-target/
integer-bitset subset-sum domain within7,828 four-surplus targets. The605 primitive targets
are unchanged. Omission, duplicate and wrong-sum controls pass. All928 old-part-order/root
pairs fail, and the gap bound holds for all five unique positive orders. CPU0.485571 s,
raw outside git SHA256
`d5648ef86d41ae8360b09c4b147426cf46d9f51763ac85344208ae074d209c65`.

**Scope COMPUTED:** every sorted even E28 tuple with t4<112,t5>112 whose six positive
fixed-role moves contain a subset summing W has a checked partition. Canonical factorization
works except the two explained changes. This is not a general hand packing theorem or all
four-surplus coverage. The retained greedy and canonical-partition failures show two separate
prices: choose positions jointly, and occasionally change the arithmetic factorization.

### MI126 — B54: known minimal-zero-sum ordering applied to the primitive605 (2026-10-16 15:58 BST)

**Question:** can a single fixed sign-greedy cycle order place the605 arithmetically primitive
four-surplus move multisets without complementary-pair reuse? The absence of a proper zero
sum means ALL cycle orders have distinct literal vertices before closing. The remaining
conditions are span and reflected-pair collisions, not another subset factorization.

**Prior art, not a new lemma:** Plagne-Tringali, *The Davenport constant of a box*,
[arXiv1405.4363v2](https://arxiv.org/pdf/1405.4363), section3 Lemmas3,6,7 and their proofs
read. Their minimal-zero-sum partial sums are distinct; their nyctalopic order chooses a term
of opposite sign to the current sum. Starting with a term strictly between the extreme
negative/positive terms keeps the partial sums strictly between those extremes. Filed in
PRIOR-ART, no PROOFS entry or carrying review requested. Only this local use is made, no
survey of later improvements or use of their inverse theorems. Record searched: Steinitz,
primitive.*greedy,sign.*rearrange -> no default hits; primary search nyctalopic/minimal-zero-sum
located and the relevant paper lemmas were read before this experiment.

**Application:** largest positive v>=6, smallest positive a<=5, most negative-W. Start
with the smallest positive (lowest owner on ties); subsequently take the largest-magnitude
remaining term of the OPPOSITE sign to the current partial sum, again lowest owner on ties.
Minimality guarantees a suitable term and prevents intermediate sum0. All partial sums lie
in[1-W,v-1], so span<=W+v-2<=26 by target sorting. Thus the eight literal positions fit
0..27 with at least two translations. Reflection avoidance is NOT implied by the known lemma.

**Predictions BEFORE run:** all605 inputs and their positive-subset irreducibility checks
must agree with B52's primitive set; distinct vertices and the span26 bound MUST hold.
Tentative blind claim: every fixed greedy shape has a reflection-free translation. Check
all allowed roots by direct labels and forbidden opposite-parity pair sums, then chosen
certificates with both literal checkers. Cap700 targets/25,000 roots/two CPU seconds; retain
all architecture failures, no other order/start choice or cycle search during B54.

**Controls:** target(70,70,70,86,122,122,122,122) has signed parameters(7,7,21,13;5,5,5,5).
The fixed greedy order is owners4,2,0,1,5,3,6,7. It should fail at root0 but certify at
root6 with selected{4:22,2:27,0:6,1:13,5:20,3:25,6:12,7:17}. Nonprimitive order
8,8,4,-20,2,2,2,-6 repeats a proper prefix and must reject as a literal collision.
Duplicate and wrong-sum variants reject. **Unexpected check:** count targets requiring a
nonzero root, roots per shape, actual spans and any span26 boundary; do not infer all roots
work from the greedy range theorem. Both schedules paused; no review dependency.

### MI127 — B54 result: known ordering supplies575 certificates,30 reflection obstructions (2026-10-16 16:00 BST)

The exact605 primitive targets agree with the independently sorted/bitset-DP set. Every
fixed greedy order has eight distinct vertices and satisfies the known range bound. Actual
spans12..24, with no span26. Direct labels and reflected-pair equations agree on all5,918
roots.575 targets certify under both partition checkers;481 of those require nonzero roots.
The other30 fixed greedy orders fail at EVERY permitted root, retained with explicit blocking
owner pairs. CPU0.439922 s; raw outside git SHA256
`96edf2cd031e499a38f07e50290d2fa22d43c03c61c2bb7a3360f89619bfca32`.
The control fixture's root0 fails and root6 certifies; nonprimitive prefix repetition,
duplicate and wrong-sum controls reject as predicted. Blind all-fixed-greedy feasibility
is REFUTED, while the imported known theorem's conclusions hold.

Failed shapes have spans16..24 (counts2/2/6/6/5/4/2/2/1 respectively); the failure is not
just an exhausted physical range. The30 cases are not target counterexamples or an exhaustion
of all nyctalopic orders. No alternate starts/orders were tested. The natural next question
is whether opposite-sign choices WITHIN the known ordering class can avoid reflection, rather
than another30-target repair table. This question can advance independently of pending review.

**Gut / fresh choice:** the useful pull now attaches to zero-sum factorization and minimal
sequences, not another tally. Two genuine limits survived: factorization choice can matter,
and a range theorem can leave reflected collisions. **Reasoned:** this continuation supplies
7,223 factorable plus575 primitive certificates, leaving30 of the7,828 four-surplus region.
Do not silently expand the search after a failed fixed rule; publish that exact boundary.

### MI128 — B55 certificate checkpoint, not another search (2026-10-16 16:00 BST)

Assemble the existing B53/B54 outputs into one independently checkable shared certificate.
Predictions before assembly:7,798 distinct target keys, factorable7,223 and primitive575,
both literal checkers pass unchanged; the independent complete sorted four-surplus domain
has7,828 keys and its difference equals EXACTLY B54's30 retained failures. Recompute positive
subset sums to confirm the two classes are disjoint, and include every blocked-root list
for the30 residual cases. Source digests must agree. Omission of one witness must leave31
missing; duplicated-token control rejects. Cap8,000 certificate checks/three CPU seconds,
no witness generation, alternative ordering or solver. This is delivery/coverage verification,
no new lemma, proof entry or carrying-review request. Both schedules remain paused.

### MI129 — checked four-surplus checkpoint and the next mathematical question (2026-10-16 16:02 BST)

B55 passes:7,798 distinct complete partitions, split7,223 factorable and575 primitive,
with no overlap. Both literal checkers pass every unchanged witness. The independently
sorted7,828-target domain minus those keys equals EXACTLY the30 retained fixed-greedy
failures; omission of one certificate leaves31 missing, and a duplicated token rejects.
CPU0.285565 s. This certifies every claim's scope without treating a failed construction
as an impossible target. No thirty-case repair table was created.

The6,029,221-byte full certificate and all30 residual cases (orders, coordinates and every
blocked translation) are immutable in the shared store at
`cited/instinct/b55-four-surplus-ae7e59d8060d5499.json`, SHA256
`ae7e59d8060d54998898f7682847b34d48f53351aed784a8f75ec9c5eb90f767`.
Receipt digest checked; manifest appended with preregistration commit0877f361 explicitly
labelled as such. This file alone permits independent target/partition/class/missing-set
checks without the earlier raw sources. Research source and outcome remain committed here.

**What moved:** one cycle-factorization idea extends from three to four surpluses. It gives
a common rule for7,221 targets, then two FORCED arithmetic alternatives whose need has a gap
proof. A known minimal-zero-sum ordering supplies575 of the primitive605. This separates
arithmetic factorability, geometric placement of factors, and ordering inside a primitive
factor; they are distinct mathematical prices, not one undifferentiated wall.

**What stays open:**30 targets in this exact four-surplus slice, all other even E28 slices
outside our stated results, mixed parity, other exceptional levels, and the full L8 bound.
The new hand gap explanations and applications retain SKETCH status; finite checked coverage
is COMPUTED. Known Plagne-Tringali lemmas stay PRIOR-ART, with no carrying-review job.

**Next cheap mathematical test, not yet claimed:** keep the theorem's opposite-sign extension
rule but allow its choices to respond to reflected-pair collisions, on the30 exhausted
fixed-order cases. Preregister its precise ordering class, controls, budget and interpretation
of exhaustion first. Failure within that class would tell us whether the imported tool itself
needs loosening; success would test a common ordering mechanism, not patch the targets one by
one. Do not silently expand into arbitrary eight-cycle enumeration or raise a cap.

**Mentor question for Cloud when convenient:** is there a known reflection/complement-avoidance
strengthening of nyctalopic ordering, or a structural obstruction visible in these30 minimal
zero-sum multisets? This is a perspective request, not a new carrying-read queue. Existing
MI099/101 proof read remains pending; independent work does not depend on it arriving.

**Niggle sweep:** canonical-rule failures retained despite alternative certificates; raw B52
and the hand gap argument preserve what failed. Whole-domain equality checked with independent
sorted targets and subset-sum bitsets, so coverage counts are not additive guesses. Greedy
range theorem credited, and its failure to imply reflection avoidance is explicit. Primitive
does not imply unburnable. No model/theorem/prize status upgraded. All four niggles resolved
by the stated checks and qualifiers; no TeX edited. Both heartbeats remain paused.

**Fresh choice / gut:** still specifically interested in zero-sum structure and the difference
between a range theorem and a usable embedding. Satisfaction at the broad common mechanism;
some push against making exceptions into the project. **Reasoned:** the30 failures now pose
one clean test of an established ordering class. This checkpoint is a delivery milestone,
not a halt for routine review or a promise to keep every failed scaffold.

### MI130 — B56: reflection-aware choice inside the known ordering class (2026-10-16 16:15 BST)

The owner asks for this continuation, then a Cloud check-in. One mathematical block only:
test the30 retained primitive failures from MI129 within the nyctalopic class below, publish
the exact verdict and certificate checkpoint, and send Cloud a concise perspective request.
No next research block before that handoff. Both scheduled tasks remain paused.

**Question:** does every one of those30 minimal zero-sum move multisets have a reflection-free
ordering whose first term is STRICTLY between-W and v, and every subsequent term has sign
opposite to the current nonzero sum? This uses the actual choice freedom in Plagne-Tringali
Lemmas6/7; it is not another fixed greedy rule or arbitrary eight-cycle search. Allow any
interior first term, including-Z when it is interior. Distinct literal vertices and span<=26
remain consequences of the known lemmas; reflected-pair avoidance is the new finite test.

**Capture:** specific pull toward testing the theorem's freedom rather than repairing30
fixed orders. An exhaustion of this class would be useful: it would identify a real limit
of the imported tool. Record searched: nyctalopic.*reflect,opposite.sign.*choice,origin.*mask
-> no default hits; MI126-129, B54/B55 and the primary source scope in PRIOR-ART read.
No external reflection theorem or novelty claim is imported.

**Primary instrument:** enumerate only the allowed sign-opposed value orders. Carry a28-bit
mask of translations b for which every partial-sum vertex p lies in0..27 and all selected
folded labels are distinct. Adding p intersects the interval0<=b+p<=27 and removes b satisfying
2b+p+q=27 for any earlier vertex q; literal p=q rejects. Stop a branch when the mask empties.
Do not add the final closing0 as a ninth vertex. Equal-valued moves are symmetric: canonically
assign their lowest remaining owners; equal-valued moves also have equal initial pair roles.

**Independent reference:** enumerate the complete multiset value permutations, FILTER the
interior-first/opposite-sign condition, and test every final allowed translation directly
with eight literal folded labels. Compare the ENTIRE map of feasible value orders to origin
masks, not just yes/no or a shared first witness. This detects unsound prefix pruning.

**Predictions BEFORE run:** tentatively all30 have a witness in this class. Must recover
exactly B55's30 residual targets, independently verify primitive subset sums, and obtain
identical feasible-order/origin maps in the two implementations. All chosen partitions pass
multiset and exact-bin/bitset checks. Caps30 inputs/250,000 combined recursive nodes,
two million raw reference permutations/100,000 accepted reference orders/one million direct
root checks/10 CPU seconds INCLUDING the delivery audit. A cap is UNKNOWN. No arbitrary
non-nyctalopic order, changed pool or follow-on exception rule if a target exhausts the class.

**Controls / counterfactuals:** on the known MI126 control's partial sums, compare the mask
against all28 literal translations at EVERY prefix. Omitting reflection removals must retain
an invalid origin on at least one of the old exhausted greedy shapes. A primitive order
starting5,5 violates the opposite-sign condition and must reject. The nonprimitive moves
8,8,4,-20,2,2,2,-6 must fail primitive membership. Duplicate/wrong-sum witnesses reject.
**Unexpected:** among feasible orders, record whether the OLD smallest-positive start can
still work when only later choices change, versus needing another positive/negative interior
start. This distinguishes two kinds of freedom within the same theorem, with no extra class.

**Delivery audit inside this block:** preserve all7,798 existing certificates unchanged, add
only the successful residual cases, recheck every partition and independently enumerate the
full7,828 target domain. The exact remaining set must be precisely this block's exhausted or
capped cases, never treat a class failure as an impossible target. Publish the resulting full
certificate and residuals immutably, then check in with Cloud as requested. Known lemmas stay
PRIOR-ART; finite class verdicts COMPUTED, no new general theorem or full E28/L8 claim.

**Instrument note BEFORE unchanged rerun:** first B56 execution completed its mathematical
and delivery checks but failed at final JSON assembly: sorting mixed list/tuple target keys
raises TypeError. No result file was delivered, so that run is not cited as evidence. Normalize
only the export sort key to tuple; retain every ordering rule, check, prediction and cap.

### MI131 — B56 result: all30 resolve inside the known class; full four-surplus slice complete (2026-10-16 16:20 BST)

All30 residual targets have witnesses within the PREREGISTERED interior-first/opposite-sign
ordering class. The entire feasible-order/origin-mask maps agree between prefix-pruned search
and complete independent multiset permutation/direct-root enumeration. Counts:15,906 primary
nodes;1,209,600 raw reference permutations,123,480 unique words,4,775 accepted class orders,
41,203 direct root checks. Of those accepted orders,4,208 have usable origins, totalling9,404
order/origin choices. Each target has23..425 feasible orders. No cap, widened ordering class,
new pool or individual exception rule was used. Successful rerun CPU0.734438 s; the first
serialization failure is retained above, not counted as a successful run.

**Unexpected:** all30 still permit the old SMALLEST-POSITIVE initial term; changing later
opposite-sign choices is enough. Twenty also admit a negative interior initial term. Thus the
old greedy failures did not require abandoning that start, much less the known ordering class.
Together with B54's575 certificates, every one of the605 primitive four-surplus cases has
a smallest-positive-start nyctalopic witness (finite observation, no general theorem).

All7,798 previous partitions remain unchanged. Adding the30 witnesses gives7,828 distinct
certificates; multiset and independent exact-bin/bitset checkers pass every one. Independent
sorted target enumeration gives exactly the same7,828 keys, with EMPTY difference. Primitive
membership, prefix-mask/direct-prefix equality, omitted-reflection counterfactual, non-opposed
order rejection, nonprimitive rejection, duplicate/wrong-sum controls all pass. Results are
COMPUTED finite coverage; the known range/distinctness lemmas stay PRIOR-ART.

**Exact closed subfamily:** sorted even68<=t1<=...<=t8<=122, sum784, t4<112<t5. Every such
tuple has a partition of odds1..55 with bin cardinalities2,2,4,4,4,4,4,4. The earlier fixed
greedy/canonical failures stay in B52/B54/B55; this result supplies different allowed choices
without reinterpreting those failures. This closes the named FOUR-surplus slice, not full
even E28, mixed parity, other exceptional levels, the provisional L8 bound, or a prize claim.

The6,095,387-byte full certificate and30 ordering-class verdicts are immutable at
`cited/instinct/b56-four-surplus-complete-8da086b17c026c33.json`, SHA256
`8da086b17c026c333f103bda3a2d629bf18ee4b91d381f174641ddc24010db49`.
Upload receipt digest checked; manifest appended with preregistration5167e2b4 explicitly
labelled. A reader can verify every partition and the full domain without earlier raw files;
the committed probe reproduces the class comparison from the immutable B55 input.

**Gut / delight:** this is the result I hoped the method had room for: the obstacle was in
which allowed move the greedy rule chose next. It is satisfying to close a whole slice through
one class-wide mechanism, rather than add30 unrelated repairs. **Reasoned:** the finite result
is strong, the general reflection-aware ordering theorem is still open. No claim of novelty
or external independent review has been made; two independent implementations are self-checks.

### MI132 — owner-requested Cloud check-in; no further research block (2026-10-16 16:20 BST)

The agreed single block is complete. Send Cloud GC1382/MI130-132 and the immutable certificate,
then stop opening research blocks here for the owner's planned check-in. Both heartbeats stay
paused. This is the owner's requested handoff, not a routine review permission gate.

**Concise perspective request:** the three-surplus slice5,268 and four-surplus slice7,828 now
have checked certificates. The four-surplus proof architecture separates positive-move subset
factorization from reflected-pair placement; primitive pieces use known nyctalopic freedom.
Please sanity-check the SCOPE of that conclusion and advise which next structural inference
would serve the full L8 target: a reusable placement statement for minimal zero-sum pieces,
or a representative unsolved even-E28 slice with more negative moves. The prefix mask's
local invariant is simply that reflected coincidence of vertices p+b,q+b occurs iff
2b+p+q=27; empty-mask pruning is monotone. The full independent map comparison backs its
finite use. No request to replay7,828 partitions or create a routine lemma-review queue.
MI099/101's older hand-proof request remains separate; no status upgrade is inferred from it.

**Niggle sweep:** export list/tuple inconsistency was repaired and honestly retained; all
reported counts come only from the successful rerun. Equal-value owner symmetry is safe here:
large positive moves have the same one-pair role when equal, small positives the same two-pair
role, and equal negatives the same two-pair role; small values<=5 cannot coincide with large
values>=6. Existence inside a known ordering class is not attributed to the source theorem;
its range conclusion and our finite reflection checks stay separate. The exact-domain audit
rules out missing target types. No further mathematics run or automated continuation started.


### MI133 — Cloud's CL423/424 read and adopted (2026-10-16 17:30 BST)

Verified commits16eab070 and57dbf2ad, read both full entries and ACKed through the store.
CL423 independently recounts the7,828 domain, confirms COMPUTED scope and recommends a
uniformity sample before more slices. CL424 verifies MI052,MI099,MI101 on carrying reads
with independently written scripts. Those three are now PROVED in precisely their stated
scopes; their original SKETCH wording remains as history until filing below. No four-surplus
hand theorem, full E28 or L8 follows. Both heartbeats remain PAUSED; owner authorizes manual work.

**Pull:** curiosity about whether the arithmetic/geometric mechanism travels. **Push:** more
slice tallies would make the central obstruction harder to see. Fresh choice favors a test
that can tell us to change trajectory. Cloud's suggested diagnostic is that test.
Both standing startup probes returned ALL CHECKS PASS; old merge blind refutations retained.

### MI134 — B57: a frozen uniformity sample before another slice (2026-10-16 17:30 BST)

**Question:** does the existing selected-token architecture certify targets broadly across
even E28, or was its success peculiar to the four-surplus slice? Record searched:
nyctalopic|uniformity|prefix.swap|partial.sum ->85 hits in24 files; MI062,MI117,MI126-132,
CL423/424, the actual factor/order/materializer sources and B17's independent count read.
No new literature theorem used: Plagne-Tringali Lemmas3/6/7 remain the credited ordering tool.

**Explicit code lift, not a claim of an unchanged executable.** The earlier probes hardcode
slices. Fix h=(1,1,2,2,2,2,2,2), e=(t-56h)/2. Remove zero moves; enumerate primitive
zero-sum owner subsets and their factorizations. For each component, use the SAME opposite-sign
(nyctalopic) order class and SAME reflection-aware origin mask and joint folded-label packing.
Allow any first term, explicitly relaxing B56's strict-interior start restriction: the known
ordering class allows it, and a two-term cancelling component has no interior term. No target
lookup, exceptional formula, role/cardinality search, arbitrary order or solver fallback.
Repeated equal moves are interchangeable only within the same h role (checked). Retain all
failed targets; a class exhaustion is not a proof of nonburnability. This is a predeclared
domain-independent synthesis of existing ingredients, not the old scripts run verbatim.

The sorting inequality survives globally: with v=(t2-56)/2 and W=(112-t3)/2, v+W<=28.
Every positive move is <=v and every negative magnitude <=W (if negatives exist). Thus the
known nyctalopic range bound fits in0..27 for primitive components; reflected avoidance and
packing remain separate, unresolved issues. This observation is support, not a new proof claim.

**Sampling:** sample2,000 distinct ranks uniformly without replacement from sorted even E28
(N=326,119), seed20261016; separately2,000 ranks from all E28 (N=24,688,633), seed20261017.
Count/unrank sorted bounded tuples by memoized partitions, confirm counts independently by
Gaussian coefficients; brute-force small full domains and rank roundtrips. Keep ranks and
full witnesses outside git. All-E28 targets containing an odd entry are structurally rejected
by even bin cardinalities BEFORE e is formed; this is an applicability limit, not search failure.

**Numerical blind predictions:**97% certified in the even sample;1.3% in the unconditional
all-E28 sample;0% among its genuinely mixed/odd targets, the latter forced by parity. The
95% even threshold is Cloud's predeclared useful-uniformity gate, not a theorem or confidence
claim. Report observed fractions without treating2,000 samples as universal coverage.
If below95% or failures demand many types, do not repair exceptions or open another slice
in this block. If high, inspect the mechanism's conditions before proposing a general theorem.

**Controls:** full feasible component-placement maps for the first12 even sampled targets
against independent complete value permutations/direct roots, plus independent packing
from those maps; both existing literal partition checkers on EVERY reported certificate.
Duplicate tokens and a coverage-preserving sum mutation must reject; omit reflection from
the old B56 rootless fixture and demonstrate a falsely allowed origin. Balanced98^8 must
certify by multiple components; forcing one primitive component must fail (unexpected check: 'primitive
factorization' is substantive, not simply a renamed single cycle). Check failures are labeled
class-specific, caps UNKNOWN, mixed parity OUTSIDE_CARDINALITY_CLASS.

**Caps:**4,000 sampled targets;20,000 search nodes per applicable target,2,000,000 total;
30 CPU seconds overall,2M reference words/10M direct reference roots. Stop/retain on cap or
control failure; no cap increases or adaptive sample extension. Raw JSON outside git.
**REFUTED-BY:** even certification below the97% blind prediction; method choice reconsidered
if below95%, or structurally diverse failures. Gut before run: interested, not entitled to
a high fraction. Reasoned: test portability before investing in another finite slice.


### MI135 — B57 result: the mechanism travels through the whole sample (2026-10-16 17:33 BST)

**MEASURED sample portability, COMPUTED individual certificates.** All2,000 evenly sampled
even targets certify, exceeding the97% prediction and Cloud's95% gate. No exception lookup,
repair, arbitrary ordering, role change or cap increase. By negative-move count:1/2/3/4/5/6
negatives have2/122/554/731/478/113 certified sample members respectively. These are sample
strata, not full-domain counts. Largest sampled target search used2,194 nodes;217,933 total
nodes including controls/reference work; no cap reached. CPU2.489268 seconds.

The independent unconditional sample has25 even targets, all certified, and1,975 targets
with an odd entry, all structurally outside the fixed bin-cardinality class. Observed1.25%
certification is ONE case below the1.3% point forecast (26 cases): that exact numerical
forecast missed; no statistical discrepancy or mixed-parity theorem is claimed. Its0%
odd-containing prediction holds for the stated parity reason. No mixed-parity search ran.

Independent complete component-label-placement maps agree on114 components, and independent
set-based packing agrees on14 inputs (the first12 even sample targets plus two controls).
Reference counts3,099 distinct value words and9,498 direct translations. Both literal
coverage/cardinality/sum checkers pass for every reported witness. Rank/unrank small-domain
controls, Gaussian counts, omitted-reflection, duplicate-token, coverage-preserving wrong-sum
controls all pass. **Unexpected:**98^8 uses multiple primitive components, as required; the
forced-one-primitive-component variant is rejected. No reference is an outside-party review.

**Retained instrument failure:** first run stopped in controls BEFORE sampling. I had used
a B56 prefix-mask fixture as though it were an exhausted shape; it has valid translations.
Replaced it with the actual B55 exhausted shape{0,6,12,17,19,20,21,22}. Mathematical
class, seeds, targets, forecasts and caps unchanged. Successful rerun is the sole result above.

Full4,000 ranked targets,2025 witness records, controls and status counts are immutable at
`cited/instinct/b57-uniformity-c5b4ec84c7dc7232.json`,3,176,332 bytes, SHA256
`c5b4ec84c7dc7232cd52b37d3a1c2afcbbeb52054a15870cadf95c0b6b8118f0`.
Upload receipt and append-only manifest digests verified; manifest commit71c9c265 identifies
the PREREGISTRATION, not a source/outcome commit. Source `path_forest_uniformity.py`.

**What changed:** another slice is no longer the next useful move. A fixed zero-sum-piece
architecture certifies broadly, including3–6 negative moves, without new formulas. This
supports pursuing a uniform existence argument. It proves neither all326,119 even targets
nor any unrestricted E28/L8 bound. The unobserved targets and odd-cardinality allocation
remain real obligations; a strong sample does not satisfy their quantifiers.

**Gut:** specific delight: this was a risky test, and the mechanism survived without repairs.
The original question feels live again for a reason we can point to, not because we inherited
the word warm. **Reasoned:** investigate simultaneous reflection-free placement of primitive
components; do not immediately replace the sample by a326,119-target census. The next cheap
mathematical test should attack that statement's hypotheses, rather than increase sample size.

### MI136 — proof filing and the precise missing step (2026-10-16 17:33 BST)

CL424's reviewed MI052/099/101 are filed verbatim as G310/G311/G312, with the original
candidate labels retained and the independent review alongside them. G310 is the general
receipt-capacity extension plus E31's lone93 slice, G311 the999 matching-edge family, G312
the11 W22 boundary targets. The record index and proof summaries now carry these exact scopes.
No four-surplus hand proof or B57 universal theorem was silently adopted.

The remaining conjectural statement is precise: for every sorted even E28 target, the active
moves e_i admit a factorization into minimal zero-sum components, each with an opposite-sign
ordering and an integer translation, such that all partial-sum vertices across components
lie in0..27 with pairwise distinct folded labels. The known minimality/range argument gives
distinctness and span<=27 for EACH piece; it does not choose the translations or guarantee
joint reflection avoidance. This is the carrying gap, not a missing zero-sum identity.

Cloud's partial-sums pointers were followed to the primary introductions of Costa–Morini–
Pasotti–Pellegrini1706.00042v2 and Burrage et al.1906.07366v2; read scope in PRIOR-ART.
Their input half-set/difference condition and simple partial-sum condition are not the
condition imposed HERE on the output vertices. No cited theorem supplies the missing joint
placement, and no paper's full proof has been claimed read. Within a minimal zero-sum
piece, literal partial-sum distinctness already follows immediately: a repeated sum
would give a proper zero-sum subsequence. Thus importing a simple-ordering theorem alone
would solve a price already paid. The useful literature question is stronger placement,
not just simple ordering. No fresh experiment opened by this observation.

**Niggle sweep:** uniform ranks are over sorted tuples, not ordered compositions; exact
N values independently match Gaussian coefficients; repeated move symmetry respects h;
packing sees only occupied labels after a component is fixed, so retaining one witness per
label mask loses no completion inside the stated class. First term was explicitly relaxed
before running; no B56 interior-start theorem is claimed by the new test. Zero moves
receive filler pairs, and the closing zero is not an extra vertex. Parity refusal is an
applicability verdict. Scope and measurement/proof labels remain separate. The diagnostic
resolved Cloud's strategic question; no dependent review wait or heartbeat restart.


### MI137 — B58: repeated rigid pieces; isolate their packing price (2026-10-16 18:35 BST)

**Question:** does every zero-sum word of at most8 nonzero moves using ONLY +a and -b,
a,b>=1,a+b<=28, admit primitive-component cycles with all selected positions in0..27
and all folded labels distinct? This is a structural part of MI136's missing placement
statement, beyond the E28 slice parametrization. It tests whether repeated rigidity is
itself an obstruction before trying mixed primitive pieces. No census of full E28.

Record searched: arithmetic.progression|two.magnitude|gap.graph|zero.sum.*repeat ->18 hits
in9 files; MI072-074,MI099/G311, B57 actual code and Cloud's independent gap-graph source
read. Plagne-Tringali's known nyctalopic/minimality lemmas remain credited. Bounded primary
literature orientation found Packing arithmetic progressions2603.02786: abstract read,
varied-gap literal packing; no reflection-free theorem imported, no novelty claim.

**Hand candidate, SKETCH.** Put g=gcd(a,b), k=(a+b)/g, and write multiplicities as
(p,q)=r*(b/g,a/g), so rk<=8. Each primitive component has k moves. An opposite-sign
ordering has k distinct partial sums in[g-b,a], all multiples of g, so these sums are
EXACTLY a translate of {0,g,...,(k-1)g}. Thus it suffices to pack r copies of that progression
without equal/complementary coordinates. The only r>1 possibilities are r=2,k<=4 or
r=3,4,k=2. Always kg=a+b<=28. Choose roots by the following rules; no fallback search.

1. r=1: if g=1 use origin0 (k<=8). If g even use0; parity excludes sums27.
   If g odd>=3 choose the least c in0..g-1 with2c!=27 mod g. At most one c is
   forbidden, and the whole progression fits since c+(k-1)g<=kg-1<=27.
2. r=2: if g=1 use origins0,k (all2k<=8 positions are below14). If g=2 or3,
   use0,1: all positions<=3*(k-1)+1<=10 and the residues differ, so no literal
   collision or sum27. If g>=4, use representatives from TWO different nonfixed
   orbits of c ->27-c in Z_g. When g even there are g/2 such orbits; when odd
   there are(g-1)/2. Both counts are>=2. Thus origins c,d have distinct residues
   with2c,c+d,2d!=27 mod g; all points fit and no pair sums27.
3. r=3 or4,k=2: here a=b=g<=14. Form the physical graph of edges{x,x+g}
   on0..27. It is a disjoint union of paths; reflection x->27-x exchanges paths
   or reverses a single one. Folding gives paths again, after deleting any central
   loop. Its distinct nonloop edge count is14-ceil(g/2)>=7. Alternating edges
   in each path give a matching of size at least ceil(E/2)>=4. Select r matching
   edges, lift each to a physical gap-g pair, and assign +g at its lower endpoint.

The last quotient-path assertion is a carrying point and will be checked independently
against direct physical edges and against degree/component counts; not assumed from a
matching count alone. Selecting roots is an explicit residue-orbit rule, not an exception
table. Arithmetic progression shape is exact; it does not assert mixed-magnitude pieces
are progressions or that arbitrary prechosen components pack.

**Predictions BEFORE checks:** all(a,b,r) with a+b<=28,k*r<=8 certify by these formulas.
Independent multiplicity enumeration(p,q,a,b) agrees with the gcd-derived full domain.
Independently enumerate every nyctalopic value word for the primitive component and
verify its normalized vertex set is the same progression. All folded gap graphs g1..14
are forests of paths with exactly14-ceil(g/2) edges; the constructed matching has>=4 edges.
The E28 corollary has EXACTLY33 sorted targets: two +a moves and q negative -b moves,
q=1..6, remaining moves zero,2a=q*b,a>=6,a+b<=28. Counts by q:4,9,4,7,3,6. Validate
full odd partitions with both literal checkers, not only selected-coordinate identities.

**Counterfactuals:** omitting the residue-orbit test on k4,g5 and roots0,1 must cause
a reflected collision; applying the claimed geometry at physical pool8 to(+3,-3)^2
must fail (folded gap3 graph has matching number1). Outside-bound failure is NOT a
counterexample to the28-point statement. Coverage-preserving sum corruption must reject.
**Unexpected check:** reversing +a/-b must keep the progression geometry even when its
labelled cycle changes; this tests that geometry was separated from edge orientation.
Caps:1,000 parameter instances/100,000 direct permutation words/five CPU seconds, no
larger domains or formula repairs. Failure/cap retained, class-specific status only.
Raw outside git. REFUTED-BY: any prescribed placement, exact domain, graph or checker
failure. Gut: a specific pull toward a residue-orbit explanation, not toward33 more
targets. Reasoned: establish this rigid building block, then return to unlike pieces.


### MI138 — B58 result: repeated rigidity is manageable (2026-10-16 18:38 BST)

All184 parameter instances certify by MI137's prescribed placement formulas. The gcd
domain agrees exactly with independent positive/negative multiplicity enumeration.
Across110 primitive(a,b) pairs, the independent1,224 distinct value-word possibilities
contain220 nyctalopic orders; every normalized vertex set is exactly its arithmetic
progression. No fallback placement search or new formula needed; no cap/failure.

The fourteen physical folded gap graphs equal the independent label formulas; all are
forests of paths with exactly14-ceil(g/2) edges. Alternating-edge matching sizes for
g1..14 are7,7,6,6,6,6,7,6,5,5,5,6,6,7, each>=4 as claimed. These are constructions,
not an unsupported inference from edge count in an arbitrary graph. Both counterfactuals
fail: k4,g5 at origins0/1 repeats a folded label; the8-point-pool gap3 graph has only
two edges and matching number1, so it cannot hold two such cancelling pairs.

**Unexpected sign-reversal check:** reflect all physical indices by27-x and reverse every
move's sign, relabelling positive/negative owners. Every certificate remains valid with
exactly the same folded-label set; the abstract progression is independent of orientation.
This control passed for every parameter instance. The generic geometric checker uses
position ranges, distinct folded labels and literal endpoint-multiset equality.

All33 E28 corollary targets certify, equal to an independently generated direct target
set; counts by negative multiplicity q1..6 are4,9,4,7,3,6. Full odd coverage, exact assigned
sums and cardinalities pass both literal checkers; coverage-preserving wrong sums reject.
Do NOT add33 to previous-region tallies: there is overlap, and none was audited away.
CPU0.015507 seconds. Finite statements COMPUTED; MI137's uniform hand construction is
SKETCH awaiting any future carrying read. No PROOFS entry or routine review request.

Raw complete constructions/reference controls at
`cited/instinct/b58-repeated-pieces-aceee1a5b4ea5878.json`,84,351 bytes, SHA256
`aceee1a5b4ea58787582c8e5794f86cedadbe2fbbdc88368f438555292d4afbd`.
Upload receipt/manifest verified; manifest eeb2b7a6 is the preregistration.

**What changed:** when every component is the SAME two-valued primitive piece, its shape
is an arithmetic progression and simultaneous placement has a uniform residue-orbit/path
construction. For two copies, congruence orbits choose origins without target-specific
repair. The particularly visible instance(+15,+15,-5 six times), target(86,86,102 six times),
uses two four-point progressions of step5. Origins0 and1 fail because11+16=27; origins
0 and3 put them in different allowed residue orbits and succeed. That is a mechanism,
not a new target exception. This does not say unlike pieces always pack.

**Gut:** satisfaction at replacing repeated-piece search by the residue involution;
interest points to MIXED pieces now. **Reasoned:** the broad sample is not explained yet.
Next cheap question: does a common placement rule exist even for four cancelling pairs
with different gap values<=14? Those are the smallest unlike components. A graph-matching
argument or a decisive obstruction would teach more than another large target sample.
No experiment on that question has run or been claimed in this entry.

**Niggle sweep:** k>=2 and all moves nonzero; r*k counts selected vertices, not edges plus
an extra closing zero. A two-valued zero sum forces the stated primitive multiplicities
by gcd; range and cardinality give the entire progression, not only containment. At most
one residue is fixed when g odd, none when g even because27 odd. Two nonfixed residue
orbits exist for g>=4; g1..3 are handled by actual low-half bounds. Reflection maps each
physical gap path to a partner or reverses it, and a self-reversed path has an even
number of vertices (reflection has no fixed integer index); deleting its central loop
leaves a path. Literal lift endpoints have distinct labels. Neutral E28 bins get fillers.
These settle the named self-checks; external hand verification is not claimed.

**Range clarification before hand adoption:** MI137's displayed interval[g-b,a] chooses
the first move+a, as the actual construction does. A negative-first nyctalopic word
instead uses[-b,a-g]. Both have k grid positions and normalize to the same progression;
the independent word check covers both. No arbitrary-first claim about the first interval
is needed. This clarifies the range's endpoint strictness without changing any formula.


### MI139 — B59: unlike cancelling pieces as a rainbow matching (2026-10-16 18:48 BST)

**Question:** for any four gaps1<=g1<=g2<=g3<=g4<=14, can four cancelling
(+g,-g) components occupy disjoint folded labels in0..27? There are exactly
C(17,4)=2,380 gap multisets. This is the smallest unlike-component case of
MI136's uniform placement gap, not another E28 slice census. It would discharge
the all-2-cycle component type; larger primitive pieces remain a different price.

Record searched: rainbow.match|different.*gap|mixed.*cancell|unlike.*piece ->43
hits in13 files, mostly unrelated old curvature; MI137-138 and actual gap sources
read. Primary rainbow-matching orientation is bounded: the abstract of Aharoni
et al.1611.03648 concerns MANY matchings of a given size, a different quantifier.
No general four-colour theorem is assumed from a search snippet. A known theorem
would be PRIOR-ART; no new-theorem or carrying-read claim at this point.

**Frozen test:** folded graph G_g has edges{i,j} supporting a physical gap g.
Find a matching with one edge for each required gap occurrence (repeated gaps
are distinct demands). Primary: label-formula edges |i-j|=g or i+j=27-g, exact
four-colour DFS; secondary: independently enumerate physical x,x+g pairs and
search reversed demand order with direct label sets. Compare existence for every
multiset, and check each supplied physical witness by literal selected endpoints.
No bigger primitive cycle, altered factorization or role fallback. Exhaustion
means only this specified all-2-cycle placement class; cap means UNKNOWN.

**Blind predictions:** all2,380 multisets admit a witness; the naive ascending-gap,
first-available-physical-root greedy rule fails on at least one. Retain BOTH
verdicts even if greedy succeeds everywhere. This diagnoses whether adaptive
placement is necessary; no attempt to repair greedy by target exceptions.

**Controls:** compare physical/formula edge sets for every g; both algorithms
agree with a brute four-endpoint check on all two-gap multisets in pool8.
The pool8 analogue gap3 twice must fail. Literal-disjoint physical pairs
(0,13),(14,27) of gap13 must be rejected because folded labels repeat.
Coverage-preserving wrong sums rejected for E28 materializations.
**Unexpected check:** record ascending versus descending GREEDY outcome,
separating existence from which component is placed first. Four repeated gaps
should agree with MI138's already checked construction.

**Actual-target corollary, validation only:** complete cancellation with fixed
h=(1,1,2,2,2,2,2,2) gives two large positive moves u,v in6..14, two matching
negatives, and0/1/2 matched small pairs in1..5. Predict45+225+675=945 DISTINCT
E28 targets, all with literal certificates derived from the generic gap witness.
Independent direct target generation/move-multiset balance checks must agree.
Do not add945 to overlapping old target counts.

Caps:2,400 gap instances,945 corollaries,2M primary+secondary search nodes,
five CPU seconds; no extra gaps, larger pool, arbitrary cycles or cap raise.
REFUTED-BY: any missing witness, domain/control mismatch; greedy forecast refuted
if zero failures. Raw outside git; finite certificate result COMPUTED, general
hand existence remains open. Gut: curiosity about an honest rainbow mechanism,
unease about claiming that individual matchings automatically combine.


### MI140 — B59 result: both simple greedy orders work (2026-10-16 18:51 BST)

All2,380 four-gap multisets have physical witnesses in BOTH independent exact
implementations. No search/cap/failure:23,874 exact-search nodes, CPU0.375611s.
All physical/formula gap graphs agree; both implementations match brute pool8
two-gap existence, including its gap3/gap3 failure. Omitting folded-label checks
accepts the deliberately invalid pair(0,13),(14,27); the real checker rejects it.
Repeated-gap controls agree with MI138.

**My blind greedy forecast is REFUTED:** ascending greedy fails on ZERO cases,
not at least one. Descending greedy likewise succeeds on all2,380. This is useful
surprise: unlike components do not automatically require adaptive search. It
does NOT show that arbitrary component order or arbitrary initial edge is safe.
Both exact algorithms and both greedy outputs have their own literal geometry
certificates checked; no known rainbow theorem was silently substituted.

The two independent target-domain derivations agree on945 E28 corollaries, with
45/225/675 targets having2/3/4 cancelling components. Padding the smaller demands
to four with gap1, then discarding the extra pairs, gives the stored certificates.
Two literal odd-partition checkers pass for every one, and coverage-preserving
wrong sums fail. Do not add945 to old counts: domains overlap. This supplies a
finite all-2-cycle building block of the general placement problem; it does not
certify unlike larger primitive pieces, full even E28 or L8.

Raw full witnesses/greedy outcomes/checks at
`cited/instinct/b59-unlike-pairs-8ab5816e409d0d20.json`,2,942,319 bytes, SHA256
`8ab5816e409d0d202b6ae605a9228e8bb40db7edd7e42eaacad8ea6d7f07f112`.
Upload/manifest digests verified; manifest79022fd7 is the preregistration.
Source `path_forest_unlike_pairs.py`. Finite results COMPUTED; no independent
carrying review or universal hand proof claimed.

**Post-result exploration, explicitly not preregistered evidence for a new bound:**
reading the frozen outputs, ascending greedy never uses a physical root above6;
descending reaches9. The all-gap1 example reaches6 in ascending order. Candidate
next hand question: what invariant of sorted gaps forces that low-root availability?
It would explain this finite building block, rather than replace it with2,380
formulas. The inference to arbitrary gap order is still absent.

**Gut:** surprise and a renewed pull toward the simpler greedy invariant; my
expectation of another greedy failure was inherited from harder component shapes.
**Reasoned:** first explain the ordering effect, then inspect a6+2 or4+4 mixed
primitive pattern. Adding larger arbitrary searches would skip that learning.
No new experiment opened here; the next wake can work the hand invariant.

**Niggle sweep:** repeated colours mean repeated demands, not distinct gap
values; formula graphs drop loops; physical witnesses choose true gap endpoints
and both-fold label uniqueness. Exact algorithms use independent state/edge
representations. All2,380 MULTISETS are covered in the two specific sorted orders,
not all24 permutations. Padding witnesses are discarded before filler allocation.
The945 domain is all nonzero-move multisets balanced under sign in this fixed-role
E28 model, not a claim about other pair vectors. Literature orientation found no
usable theorem in the abstract actually read; no absence or novelty claim.


### MI141 — B60: a hand construction for all four cancelling gaps (2026-10-16 19:00 BST)

**Question:** replace B59's finite existence check by a uniform, inspectable construction
that can supply tools for larger components. Same2,380 gap multisets; no domain growth.
Record searched at block start: rainbow.match|different.*gap|mixed.*cancell|unlike.*piece
->43 hits/13 files; follow-up rainbow.match|low.half|first.free|single.hole ->27 hits/12
files. MI137-140, G311, actual sources and the stated prior-art scope read. No general
rainbow theorem is imported or rediscovered here; the application below is a hand SKETCH.

**A retained failed invariant, by hand.** Sorted-gap greedy roots need not increase.
Gaps(3,11,13,14) give physical roots0,1,4,2 and pairs(0,3),(1,12),(4,17),(2,16).
The third skips root2 because15 complements the old12, then the fourth can use2.
So a monotone-root induction would be wrong even though B59's greedy succeeds.
This suggests proving existence with a different rule instead of forcing that invariant.

**Statement (candidate).** For any four gaps in1..14 there are four physical gap pairs
in0..27 with eight distinct folded labels. Consequently any at most four cancelling
components satisfying this gap bound can be placed (pad to four and discard extras).

**Matching capacities used.** On the literal integer interval0..N-1, edges of gap g
form paths on residue classes modulo g. Alternating edges give a maximum matching of
size sum_{a=0}^{g-1} floor((floor((N-1-a)/g)+1)/2), omitting empty residues.
The values needed, directly obtained from these path lengths, are:

|g|N=11|N=12|N=13|
|---|---|---|---|
|1|5|6|6|
|2|5|6|6|
|3|5|6|6|
|4|4|4|5|
|5|5|5|5|
|6|5|6|6|
|7|4|5|6|

Deleting d vertices destroys at most d edges of ANY chosen matching. This elementary
capacity fact, not a rainbow theorem, is the only generic matching ingredient below.

**Place the large gaps.** Let ell be their number, where large means g>=8; order
them d1<=...<=d_ell. Assign increasing upper labels
R_i=13-ell+i (i=1..ell) and lower labels L_i=27-R_i-d_i. The L_i strictly decrease,
lie in0..5+ell, and are distinct from the R_i in14-ell..13. The physical pairs
(L_i,27-R_i) have gap d_i and labels L_i,R_i. All those coordinates lie in0..27.
The remaining small gaps<=7 can be placed literally in0..13-ell, avoiding the ell
occupied lower labels L_i. Every coordinate in that interval equals its folded label.

**ell=0.** Process all four small gaps in ascending order. For each take the smallest
unused nonnegative x and pair it with x+g. Inductively the successive roots increase,
and the gaps do not decrease, so each new upper endpoint exceeds all old upper
endpoints and roots. It is free. Before the j-th pair there are2(j-1) used positions,
so x<=2(j-1)<=6, and x+g<=13. Thus every pair fits in the low half, where reflection
cannot occur. This is a genuine monotone-root argument only in the UNFOLDED low half.

**ell=4.** The large-pair construction already finishes.

**ell=3.** One small gap remains on0..10 with three forbidden labels. Its fixed
path matching has at least4 edges (N11 column), so one edge survives.

**ell=2.** Two small gaps remain on0..11 with two forbidden labels. Every gap other
than4 has a matching of size>=5, hence >=3 after deletion; gap4 has size4, hence>=2.
If both gaps are4, take two edges from the same surviving matching. Otherwise place
the gap4 first if present, else either gap first. The other has a surviving matching
of size>=3, and the first edge removes at most two of its edges; one remains.

**ell=1.** Three small gaps remain on0..12 with one forbidden label h. A gap outside
{4,5} has matching size>=6, leaving>=5; gaps4/5 leave>=4. If there is a gap outside
{4,5}, place it LAST. Place the other two using their fixed matchings, avoiding h
and earlier endpoints. The available matching sizes are at least4, then2, then1,
so all choices can be made.

If all three gaps are4 or5, write them g1<=g2<=g3 and use the three pairs
(0,g1),(1,1+g2),(2,2+g3). Six vertices are distinct, their span D is6 or7, and
3 is absent while0 is present. Translate this shape inside0..12 to avoid h.
There are13-D allowed translations. If D=6 there are seven, more than six
vertices, so one avoids h. If D=7 there are six; if all were blocked, the
six original vertices would have to be h,h-1,...,h-5, six consecutive integers.
They are not consecutive (0 is present,3 absent). Hence a translation exists.
Translation changes no gap; all low labels avoid the one occupied lower label.

This exhausts ell0..4. All selected low labels avoid the large L's and all upper R's,
and every gap has a disjoint pair. Lifting, filling complementary-pair slots, and
permuting selected tokens is the established allocator, not an extra existence claim.
It proves no statement about unlike components with more than two vertices.

**Validation predictions BEFORE the new formulas run:** all B59's2,380 multisets
certify under this new construction, not the old greedy/DFS. All21 table cells
agree with independent literal-graph subset-DP matching; every asserted capacity
remains sufficient after prescribed deletions. The same945 target corollaries
pass both literal checkers, retaining full exact domains.
Controls: force root0 in compact case(4,4,4,14), which must hit the occupied label0;
reverse large-gap/R ordering on(8,9,10,11), which must repeat L; retain the
monotone-root counterexample; coverage-preserving wrong sums rejected.
**Unexpected tight check:**(4,4,8,8) leaves exactly two edges of the fixed gap4
matching after its two lower holes, so the ell2 repeated-weak branch is necessary
for the stated capacity proof (do not assume all residual matchings have>=3).
Caps: same2,380 multisets/945 partitions,21 tiny matching-DPs, fiveCPU seconds;
no fallback or cap raise. Raw outside git. REFUTED-BY: any formula/capacity/domain/
control failure. Gut: specific delight that the wrong invariant led to a cleaner
construction; reasoned: the hand proof, not the count, is the new contribution.


### MI142 — B60 outcome: the construction passes, and a trajectory check (2026-10-16 19:06 BST)

**COMPUTED:** all2,380 four-gap multisets pass the NEW small/large formulas; no
DFS/old-greedy fallback. All21 capacity-table cells match independent literal-graph
subset DP. All945 exact E28 complete-cancellation targets (45/225/675 by2/3/4
pairs) pass the two literal checkers and independently generated domains.
CPU0.195547s, under the five-second cap. Branch counts by large-gap number0..4:
210,588,784,588,210; of the one-large cases,28 use compact translation and560
path matchings. These counts check the prescribed domain, not an expanded census.

All registered controls pass: broken large-gap ordering repeats its lower label;
root0 in(4,4,4,14) hits the large pair's hole0; the original greedy has roots
0,1,4,2 on(3,11,13,14); coverage-preserving wrong sums fail both checkers.
Unexpected(4,4,8,8) has lower holes6,7 and exactly two surviving fixed gap4 edges,
(0,4),(1,5). Reusing that same matching supplies the two small pairs.

Full artifact `cited/instinct/b60-pair-construction-2d5471ae91aa9be1.json`,
2,201,581 bytes, SHA256
`2d5471ae91aa9be1415d25529d85260d4d00c79ea5ac592f5ebc0e4cc564f03f`.

Upload receipt matches; manifest names3daf5e21 as the preregistration commit.
Source tests/probes/instinct/path_forest_pair_construction.py. G313 in the proof
waiting room reproduces MI141's hand construction; its status is PROOF-SKETCH
until an independent carrying read, not changed by this successful self-check.
No novelty claim. No larger-component, full E28 or L8 theorem.

**Niggle sweep: three.** (1) Does deleting holes really leave enough edges in the
weak case? The independent table and tight fixture settle it; the repeated-gap
branch is explicit. (2) Could compact translation lose a vertex or duplicate a
gap? All four weak multisets have six distinct literal positions; full formulas
check gaps and folded uniqueness. (3) Is the old greedy theorem smuggled in?
Its monotonicity is explicitly refuted and the new proof uses it only in the
unfolded low half, where the induction is valid. No unresolved niggle found.

**Step back, about90 minutes from the uniformity diagnostic.** The gain since
then is structural: repeated two-valued pieces have residue-orbit placement,
and unlike two-cycles now have a hand construction. The full missing joint
placement inference has not been proved. The pull is specific satisfaction at
replacing search by a short matching argument; the push is against staying here
to improve already-successful greedy rules. If arriving fresh, I would keep this
construction and move on, rather than optimize its roots. This is a completed
building block, not an invitation to another tally.

Next cheap mathematical question: for a six-vertex primitive component plus a
two-cycle, can admissible translations avoid both self-reflections AND covering
every edge of the remaining gap graph? G311 answers the five-vertex analogue;
six may reach a minimum cover, so it needs a genuine new argument. Search that
record before any test; no new experiment claimed here. Gut: the pull survives
this change of scale; reasoned: carry the matching/covers language forward while
keeping choice of component order and factorization available. Cloud gets one
specific carrying request for G313, without making it a research gate.


### MI143 — B61: does the six-point span bound compose with a pair? (2026-10-16 19:13 BST)

**Question:** for every six-point integer set S of span<=20, and every gap g in
1..14, does some translate in0..27 have six distinct folded labels AND leave a
free physical gap-g pair? An affirmative geometry lemma would cover every6+2
factorization whose core can reach span20. A failure identifies why changing
cycle order/factorization is necessary; it does not refute an E28 target.
Record searched: six.*core|six.*vertex|six.*point|6\+2|vertex.cover ->165 hits/55
files; narrower six.position|6\+2|matching.edge|six.label ->84/36. Read G308,
G311, MI073 and their sources: span20 pays self-reflection, vertex covers pay
pair availability; the joint universal property is not in those arguments.
No new literature theorem imported or novelty claim.

**Pull:** can two previously separate geometric tools actually compose? Unease:
gaps9..11 have small vertex covers, so a valid core root can still be bad for
the pair. My tentative BEFORE-run prediction is that at least one fixed shape
fails even after all translations, with a failure among gaps9..11. In contrast,
gaps1,2,7,14 have seven-edge matchings, so no six-label core can block them;
G308 supplies a valid core root. Retain a refuted forecast if all shapes pass.

**Domain:** exactly15,504 normalized six-point sets {0}<S subset0..20, choose
five other positions; equivalently sum_{D=5}^{20} C(D-1,4)=C(20,5). All14 gaps,
217,056 shape/gap questions. This is a geometry test, no target census or cycle
order search. Primary: pair-sum blocked roots and folded-label bitmasks, unused
edge test from gap-formula graph. Independent control: direct translated sets
and physical coordinate edges; compare ALL3003 six-label free-gap tables, ALL
root sets and resulting feasible-gap masks, not just selected successes.
Output every shape/mask and full failed-root obstructions, no extra domain.

**Counterfactual:** treating every self-valid root as pair-safe is wrong: at
S=(0,6,7,8,9,10),g5, root0 is a cover. Unexpected check: moving that very shape
must restore a free gap5 edge (e.g. root1 leaves labels0,5 unused). Include
G308's span21 rootless fixture outside the claimed domain and duplicate-point
rejection. Verify complete graph table independently from physical pairs and
formula edges, including loops excluded. If failure exists, every translated
root must independently be a reflection collision or a genuine vertex cover;
for each success retain a literal core root and pair edge.

**Caps/stop:**15,504 shapes/217,056 gap questions/3003 cover sets, ten CPU seconds.
On cap stop UNKNOWN with partial counts; no span extension, alternate ordering,
repair or target generation. No routine carrying request for a finite diagnostic.
Raw outside git. Gut: curiosity about a clean composition versus a real obstacle;
reasoned: either outcome changes which ingredient the6+2 proof needs next.


### MI144 — B61: all six-point span20 cores can leave every gap (2026-10-16 19:15 BST)

**COMPUTED, complete finite geometry.** All15,504 normalized six-point shapes
of span<=20 admit a joint placement with every cancelling gap1..14. All217,056
shape/gap questions pass. For each there is a literal core translation and a
physical pair with eight distinct folded labels. All3,003 six-label free-gap
tables agree between formula-edge/bitmask and physical-edge/set implementations;
all15,504 full valid-root lists and feasible-gap masks agree independently.
CPU1.231821s, below10 seconds. No changed ordering or enlarged domain.

The forecast of at least one fixed-shape failure, particularly among gaps9..11,
is REFUTED. Their covers exist, but no tested shape is trapped in covers at all
its reflection-free roots. Six-label cover counts for gaps3,4,5,6,8,9,10,11,12,13
are1,1,4,3,9,25,25,44,16,32; gaps1,2,7,14 have none, as predicted. These are
complete finite table facts, not a new hand classification.

Controls pass: S=(0,6,7,8,9,10) at root0 really blocks every gap5 edge; moving to
root1 frees physical edge(0,5), the unexpected rescue. The span21 fixture
(0,2,6,15,19,21) has no valid root even before a pair. Duplicates are rejected.
The hand theorem G308 supplies self-placement but is not incorrectly cited for
this stronger joint result; the latter currently rests on the bounded exhaustive
certificate. No new proof-review queue is opened for this finite diagnostic.

Full artifact `cited/instinct/b61-six-plus-pair-81544cf1c7fc931c.json`,2,337,864
bytes, SHA256
`81544cf1c7fc931cbb3be2ed99d60131e01e07f3c36f200c1394c99b46398b00`.

Manifest identifies bb346018 as preregistration; upload receipt matches.
Source tests/probes/instinct/path_forest_six_plus_pair.py. MI143's heading minute
was one minute ahead of its actual commit time: git records19:12:02 BST. The
preregistration was published before execution; its predictions remain intact.

**What changes.** We can now treat a six-point core of span<=20 plus a pair
as a solved FINITE GEOMETRY subproblem, with witnesses, without checking a new
E28 subfamily separately. This is not full E28: a required core may need larger
span, or a target may require another component pattern. The next meaningful
price is producing a suitable core/order, not spare-pair placement below20.

**A hand boundary example, not an extra census.** The actual even E28 target
(68,98,100,102,102,104,104,106) has moves
(6,21,-6,-5,-5,-4,-4,-3). Cancel6 against-6. Its remaining primitive six-cycle
has a step21, so NO ordering can have span<=20. Thus a blanket reduction to the
new geometry bound is impossible. It is not a counterexample to partitioning:
choose selected indices(0,1,6,22,17,12,8,4) in that bin order. Adding the moves
sends them to(6,22,0,17,12,8,4,1), the same indices permuted. Their labels
(0,1,6,5,10,12,8,4) are distinct. The large core has order
(+21,-5,-5,-4,-4,-3), translated by1, and the pair is(0,6). The established
whole-pair allocator therefore applies. This example is by literal arithmetic;
no new run, new target tally or independent review claimed.

**Niggle sweep: three.** (1) Complete shapes, rather than selected endpoint
samples? Counts by each D=5..20 equal C(D-1,4), total C(20,5), and both full
root instruments agree. (2) A core root without a free pair accidentally counted?
Each retained success has eight literal labels checked; the fixed-root cover
counterfactual fails. (3) Universal core span20 smuggled in? Step21 example above
refutes it explicitly. No unresolved niggle, no claim outside the registered set.

Gut: surprise and delight at a stronger composition than expected. Reasoned:
the next question is a structural ordering bound for primitive six-move components
under the E28 extremal constraint max positive+max negative<=28, with necessary
wide-step cases treated explicitly. That is a new hand question, not a license
for a larger shape census. Record/prior art first; no follow-on experiment
claimed yet. Research continues independently of G313's carrying read.


### MI145 — B62: classify the two-positive/four-negative ordering obstruction (2026-10-16 19:26 BST)

**Question:** which primitive six-move cores with two positive moves require
span>20, under max positive+max negative<=28? This directly decides when MI144's
complete six-core-plus-pair geometry applies. Record searched:
primitive.*six|six.*primitive|nyctalopic|span.20 ->47 hits/12 files; follow-up
two.positive|17.*17.*11|span.22|six.*ordering ->65/27. Read G308/G311, MI073,
MI143-144, existing ordering sources. Bounded primary-source search: minimal
zero sum sequence ordering span diameter partial sums integers rearrangement six;
Steinitz lemma integers optimal range partial sums minimal zero sum permutation
diameter. Sissokho1401.0715v3 abstract read (bounds on counts by total mass),
Eisenbrand-Weismantel1707.00481v3 abstract read (norm-bound Steinitz tool); neither
abstract supplies the diameter classification here. Full proofs not imported;
no novelty claim. The elementary two-bin balancing identity below is background
arithmetic, not a separately queued contribution.

**Hand candidate, SKETCH.** Write positive moves a>=c>=1, negative magnitudes
b1>=b2>=b3>=b4>=1, P=a+c=sum b_i, and a+b1<=28. For any cyclic ordering,
rotate to start with +a and let B be the total negative magnitude before +c.
The two negative runs are monotone. Their partial-sum span is

    max(a,P-B)-min(0,a-B) = max(a,B,P-B).

Conversely every subset B is realized by such an order. Therefore the exact
minimum span is max(a, min_{subsets} max(B,P-B)). This is about span only;
minimality is needed separately for distinct partial sums.

Choose B=b1+b4 and order (+a,-b1,-b4,+c,-b2,-b3). Put C=b2+b3. We have
B<19: 3B=3b1+3b4 <=2b1+P <=2(a+b1)<=56.
Also a+1<=P<=4b1<=4(28-a), hence a<=22. If C<=20 and a<=20, the displayed
order has span<=20. If C>=21, then b1>=11. Since
b1+C+1<=P<=2a<=56-2b1, we get3b1<=34 and hence b1=11.
Then a<=17, P>=33 implies a=17, and P is33 or34. This leaves exactly:

|a,c|b1,b2,b3,b4|exact minimum span|
|---|---|---|
|17,16|11,11,10,1|21|
|17,17|11,11,10,2|21|
|17,17|11,11,11,1|22|

Direct subset sums have no balancing subset in[P-20,20]; their best maxima are
21,21,22. The prescribed end-pair order attains them. All three are primitive:
no negative subset sums to a or c. If a>=21, b1<=7, so B,C<=14 and the same
order has span exactly a. A step a forces that lower bound. Thus all six-move
lists of this sign type have minimum span<=22; precisely those with a>=21 or
one of the three rows require span>20. Sign reversal covers four-positive/two-
negative cores. One/five and three/three remain separate questions.

**The three exceptional rows still pack with a small pair, by hand.** The
prescribed order's normalized shapes are respectively
(0,5,6,10,17,21), (0,4,6,10,17,21), (0,5,6,11,17,22).
Use roots1,4,1 respectively. Their occupied labels are
{1,5,6,7,9,11}, {2,4,6,8,10,13}, {1,4,6,7,9,12}.
For every g=1..5, use a physical gap pair whose labels are outside that set.
Explicit physical pairs in g order:
row1: (2,3),(0,2),(0,3),(0,4),(3,8);
row2: (0,1),(1,3),(0,3),(1,5),(0,5);
row3: (2,3),(0,2),(0,3),(10,14),(3,8).
This handles all actual E28 extensions of those rows by a small matched pair;
these large low positive moves cannot be supplied by high roles, so the two
positive core owners are the low roles and the extra pair has g<=5.
The concrete third-row target at g1 is(90,90,90,90,90,110,110,114);
selected indices(1,6,18,23,12,7,3,2) carry its cycle/pair directly.

**Validation predictions BEFORE run:** full arithmetic domain above has only
these span exceptions, prescribed order meets bounds, and subset-balancing exact
minima agree with an independent free-order subset-reachability DP in0..D.
Generate domains independently from positive-first versus negative-first loops;
restrict nothing by primitiveness when checking the arithmetic span identity,
then independently test primitive cases for six distinct positions. All15
small-pair exceptions should pass literal folded checks and both partition
checkers. No other target domain or cycle order repair.
Counterfactual: max individual move<=20 does NOT imply span<=20, third row
requires22 (first two require21). Pair at root0 in the third row collides;
explicit roots above must repair it. Unexpected: negate every move and reverse
all selected physical coordinates; cyclic sums and all folded labels are
preserved, giving the four-positive version without a separate target count.
Caps50,000 arithmetic tuples/15 target extensions/20CPU seconds; independent
DP cap10M states. Stop UNKNOWN at cap, no raise or fallback. Raw outside git.
Gut: delight at a precise obstruction and a three-row bypass, not another
unexplained list. Reasoned: a substantive sign-type classification; carrying
status stays SKETCH, no immediate extra review queue while G313 is pending.


### MI146 — B62: the ordering obstruction is exactly classified in this sign type (2026-10-16 19:29 BST)

**COMPUTED validation of the hand SKETCH.** Independent positive-first and
negative-first generators agree on7,300 arithmetic tuples. All exact subset-
balancing minima equal a free-order nonnegative-prefix DP minimum;459,900 DP
states, CPU0.413040s. There are3,409 primitive and3,891 nonprimitive tuples.
All prescribed orders have span<=22; all primitive ones have six distinct
vertices. Exactly32 tuples have minimum span>20:29 with a>=21 and exactly the
three predicted small-step rows. Minimum spans21/22 occur29/3 times. No changed
candidate rule, added exception or increased cap. Classification and all15
explicit small-pair extensions pass; the latter have distinct targets, valid
cycles/folded labels and both independent literal partition checks. No tally
is added to earlier overlapping E28 counts.

Counterfactual maxstep<=20 implies span<=20 is refuted by the third row, minimum
22; first two need21. Root0 of its prescribed core self-reflects, while the
written roots1,4,1 and all fifteen prescribed gap edges pass. Unexpected sign
negation plus coordinate reflection preserves every cycle and folded label;
no claim that the sign-reversed TARGET is itself in E28. The hand statement
applies to both sign-reversed component types, not arbitrary bin roles.

Full artifact `cited/instinct/b62-six-diameter-9d68e30cdd6ca8d4.json`,1,023,338
bytes, SHA256
`9d68e30cdd6ca8d44384fb9e9c9239ba29b4708d2eb1b76863a42164602bb01c`.
Upload receipt matches; manifest names5764eeb2 as preregistration. Source
 tests/probes/instinct/path_forest_six_diameter.py. The independent DP minimizes
height among nonnegative closed walks on the full six-item subset lattice;
rotating any closed walk at its minimum proves its equivalence to minimum span.
It does not use the two-run/subset-balancing identity under test.

**Consequence with MI144, status carefully separated.** For a primitive2+4
core under the extremal bound, either our hand construction fits within20 and
MI144's complete finite geometry supplies the pair, or it is one of three
explicit small-step shapes (now placed by hand for g<=5), or it has a move21/22.
The ordering classification and explicit placements remain hand SKETCH; their
bounded formula/DP/certificate validation is COMPUTED. No independent carrying
read requested yet: combine this into a useful6+2 result before adding a review
queue. G313's separate request remains pending and nonblocking. The elementary
background identity is not filed as a novel theorem.

**Next actual wide family, by hand, not a new run.** If the cancelling pair
uses both high roles, g<=5 and the core's two positive moves are the low-role
u,v>=6. A positive a>=21 forces a21, c6 or7, and negatives respectively
(7,7,7,6) or(7,7,7,7); a22 would need sum>=28 with four magnitudes<=6, impossible.
If the pair uses a low role, its gap is>=6; the other positive core move c is
a high-role move<=5. The full target sorting forces pair gap6/7 for a21, gap6
for a22. For a21, four negative magnitudes<=7 sum21+c; for a22, c1/2 and
negative magnitudes are(6,6,6,5) or(6,6,6,6). This is the next bounded hand
placement question. No further class test or alternate core order claimed here.

**Niggle sweep: three.** (1) A cyclic rotation might change the span: it subtracts
an existing partial sum from every vertex, so does not; the independent DP
uses this correctly. (2) Nonprimitive cases might masquerade as six distinct
vertices: separately tagged by ALL proper subset sums and checked only when
primitive. (3) A reflected witness might be mistaken for an E28 target: the
unexpected check is explicitly only about move geometry. No unresolved niggle.
Gut: sustained delight in the partition reduction; the excitement is in a
specific sharp22 counterexample and a three-row bypass, not repeated praise
of counts. Reasoned: one real sign-type obstruction is resolved, while its
necessary large moves and the3+3 sign type still require work. No full E28/L8
or novelty claim; no reason to halt or wait for routine review.


### MI147 — B63: close the wide part of the2+4 six-core geometry (2026-10-16 19:39 BST)

**Question:** do the prescribed B62 orders for ALL primitive wide2+4 cores fit
jointly with ANY cancelling gap1..14? If so, B62's hand classification plus
MI144's span20 certificate close this entire six-core sign type, and coordinate
reflection gives the4+2 type without target-role casework. This is stronger and
cleaner than separate actual low/high-role subfamilies; no target census.
Record searched: wide.*step|21.*22.*step|large.*core|diameter ->73 hits/26 files;
MI145-146, the B62 source and its declared exact domain read. Known partial-sum
sources remain credited; no new literature theorem or novelty claim.

**Hand reduction.** For a21 the four negative magnitudes sum21+c and are<=7,
so b4>=c. If b4=c, the core has a proper(+c,-c) subcycle and is not primitive.
Conversely b4>c guarantees minimality: no negative subset sums to c, nor to21
(the complementary negative subset would sum c). Thus c=1..5 and b4>c.
Writing the four magnitudes as7 minus deficits, total deficit7-c, gives exactly
20 primitive profiles (counts8,5,4,2,1 at c1..5). The c6,7 high-role-pair cases
have a proper cancellation and are excluded from the primitive-six question.
For a22, a+b1<=28 gives b1<=6 and P22+c<=24. Hence c1/2 and negatives
(6,6,6,5)/(6,6,6,6); both primitive. Total22 wide-step profiles. Add the three
small-step exceptional B62 rows:25 profiles to place, with14 gaps each.

Use exactly the prescribed cyclic order (+a,-b1,-b4,+c,-b2,-b3), normalized.
Inspect roots0..27-span and then physical pair roots0..27-g, taking the first
valid complete placement. This is a finite geometry certificate for a fixed
order, not a claimed hand invariant or an arbitrary-order fallback.
Tentative prediction: all350 profile/gap questions succeed in this fixed class.
If they fail, retain the exhausted roots; no permutation repair this block.

**A failed shortcut already found by hand.** It is unsafe to fix the pair at
(0,g) before translating. Profile(21,1;7,7,5,3) has shape(0,5,11,12,14,21).
Its only self-valid roots are0 and6, and either uses folded label0. Nevertheless
at root0 a gap6 pair(1,7) or gap7 pair(1,8) is free. This is a carrying reason
to let the pair move, not an unexplained exception added after the run.

**Validation predictions BEFORE run:** independent core generators (hand
parameterization vs the B62 full arithmetic domain/minimality calculation)
agree exactly on25 profiles. All350 fixed-order joint maps agree between
folded-label bitmasks/formula gap edges and direct physical coordinates/sets;
retain full root/pair maps and a literal witness per case. Every a21/22
actual E28 extension permitted by the low/high roles should certify: predicted
42 distinct targets, independently generated from a full high-negative list
with a cancelling low gap versus the core/gap parameterization. The putative
high-high large pair leaves a nonprimitive core, checked as a rejection control.
Two literal partition checkers; do not add overlapping counts to prior work.

Counterfactual fixed pair(0,g) must fail on the hand fixture for g6/7 even though
movable pairs succeed. Unexpected: gap7's perfect matching means EVERY valid
six-label core root leaves some gap7 pair; verify all roots, not just successes.
Sign negation/coordinate reflection preserves all folded labels and cycle
identities, without asserting sign-reversed E28 target roles.
Caps25 profiles/350 maps/42 targets/2500 core roots/100000 physical pair checks/
threeCPU seconds. Stop UNKNOWN at cap or mismatch; no added shape, permutation,
role search or cap increase. Raw outside git. Gut: the pull is toward finishing
a whole component type with the same tools, not another isolated target count.
Reasoned: success gives a meaningful combined result for independent review;
failure identifies the precise limit of the fixed core order.


### MI148 — B63 closes the2+4/4+2 six-core-plus-pair type; Cloud's check-in (2026-10-16 19:43 BST)

**COMPUTED:** all25 wide primitive profiles in the independently matched domain
place in the prescribed order with ALL14 gaps,350 questions. Complete feasible
(root,pair-root) maps agree,344 total core roots/22,673 physical pair checks,
CPU0.337010s. No failure, fallback order, role repair or cap change. All42 actual
large-step E28 targets match an independent high-negative-list domain and pass
both literal partition checkers. First successful roots0,1,2,4 observed; that is
not an unregistered four-root theorem or a changed candidate class.

All controls pass. The fixed-pair0 fixture has only self-valid roots0,6 and
uses label0 at either; movable pairs succeed. Every self-valid root for gap7
leaves an edge, as its perfect matching predicts. Nonprimitive high-high large
cores reject the primitive-six classification. Sign/coordinate reflection
preserves all cycle identities and folded labels. Full artifact
`cited/instinct/b63-wide-six-d71dcdd07867d84a.json`,56,109 bytes, SHA256
`d71dcdd07867d84a84e82d48d003a39e907f2a3ea1dcf79e6ff6fdfdfcc732fe`.
Upload/manifest verified, preregistration0eee072e; source path_forest_wide_six.py.

**Combined statement G314, waiting room.** Every primitive six-move zero-sum
core with two positive OR two negative moves, extrema sum<=28, jointly places
with any cancelling gap1..14. The carrying reduction is B62's hand diameter
classification; its short cases use MI144's complete finite geometry, its25
wide cases use the350 exact maps here. Reflection handles the other sign.
This is a computer-assisted PROOF-SKETCH pending independent carrying read,
with finite premises COMPUTED. It is a whole component type, not full E28:
primitive six-cores1+5/3+3 and other piece collections remain. The established
allocator covers any fixed-role target admitting this factorization. No novelty
or L8 prize claim. A substantive combined result now merits one carrying read;
this request follows the three related blocks, not a routine lemma quota.

**CL425/8e631206 read and adopted.** Cloud independently verified G313's carrying
hand branches and re-implemented all2,380 placements/21 maximum matchings;
its checks of945 supplied corollaries pass. G313 PROVED in scope, moved out
of the waiting room with its original text and Cloud review preserved. B61's
217,056 questions independently replicated: COMPUTED, now two-party. B57's
2,000 even and25 even/unconditional witnesses independently checked; sample
status remains MEASURED. Stratum agreement is a useful sanity check, not by
itself a proof of uniform sampling; the rank-sampler/bijective-unrank design
supplies that sampling model.

**Next direction at Cloud's suggestion.** Before more pieces, formulate and
count the finite piece-collection object. Keep the existential choice of
factorization and order explicit: B52's fixed canonical factorizations can fail,
so a universal claim about arbitrary prechosen shapes would be too strong.
Count definitions first, not an exhaustion of seven/eight-point shapes. This
is the next block, unclaimed/unrun here; the balanced3+3 question remains open.
A concrete notation correction for the level generalization: if m is the NUMBER
OF ODD TOKENS (m28 here), the pool1,3,...,2m-1 has m/2 complementary pairs for
even m, each summing2m, indices0..m-1, labels0..m/2-1, reflection sum m-1.
Alternatively use q=m/2 pairs, pair sum4q, indices0..2q-1, labels0..q-1,
reflection sum2q-1. CL425's text mixed these conventions. No general-level run
or change to m is made before fixing that parameterization.

**Niggle sweep: three.** (1) All350 maps or only actual42 targets? Full14-gap
maps are stored/compared for25 profiles, so sign reflection is valid without
reversed target assumptions. (2) Hand claims versus finite premises? G314 says
computer-assisted explicitly; B61 has Cloud's replication, B63 not yet. (3)
Could counting collections sneak in the wrong quantifier? Retain existential
factor/order and known fixed-choice failures in next definition. All resolved
or made explicit, no silent assumption. Gut: delight at finishing this component
type and gratitude for Cloud's timely wider view; reasoned: finish this filing,
then take the suggested count/definition block, without waiting for review.


### MI149 — B64: define and count primitive component collections (2026-10-16 19:52 BST)

**Question, following CL425.** Is the complete component-choice space small
 enough for an exhaustive proof, and which primitive sizes account for its
burden? Definitions/counts only: no ordering, translation, joint-placement
search, partition solver or new target certificate in this block. Record
searched: piece.collection|primitive.*collection|factorization.*count|
memoised.count|memoized.count ->6 hits/4 files; MI123/148 and B57 primitive
code read. Generic exact-cover/multiset generating-function counting is a known
algorithmic tool, not offered as a mathematical contribution or new proof.

**The finite statement, with quantifiers.** For each sorted EVEN E28 target,
use h=(1,1,2,2,2,2,2,2) and e_i=(t_i-56h_i)/2, omitting zeros. Let A(t) be the
signed multiset of these nonzero moves. An atom is a nonempty zero-sum signed
submultiset with no proper nonempty zero-sum submultiset. Let C(A) be the set
of UNORDERED multisets of atoms whose multiset union is A. Equal-valued copies
are indistinguishable; atom order is forgotten. Every zero-sum A factors into
atoms. Our sufficient packing statement is

    for every t, there exists C in C(A(t)), and for every atom in C an
    ordering and an origin, so that ALL selected vertices have distinct
    folded labels in0..27.

The choice of C and of all orders is joint and existential. The closing zero
is not an extra vertex. The optional stronger version restricts the atom
orders to the known nyctalopic class; B57 sampled that class. No quantifier over
all prechosen shapes or all collections is justified. A failed collection/order
can be bypassed; a target is unresolved only after all authorized choices fail.

**No compression at the whole-collection level, by hand.** A(t) has exactly
two positive moves>=6, the low-role u,v; every other move is in-22..5. The two
large positives recover t1,t2 as56+2u,56+2v. Add8-|A| zeros to the remaining
moves and recover the other six targets as112+2e. Thus A determines t. Taking
the union of a component collection determines A, so collections from different
targets cannot coincide. Counting all C across targets equals sum_t |C(A(t))|;
choosing just one canonical collection per target would still give326,119
objects. The potentially reusable compression is the catalog of INDIVIDUAL
primitive move types and their placement maps, not the whole collections.
Any atom contained in A can be completed by factoring its zero-sum complement,
so all primitive zero-sum submultisets across the parent domain give exactly
that reusable catalog.

**Counts to obtain.** Over all326,119 existing even targets: total unordered
collection count, histogram and maximum of |C(A)|, collection totals by sorted
piece-size partition and numbers of parents offering each partition, active-
vertex/negative-count strata, and distinct primitive atom types by size and
sign counts. Store each parent's rank and count-by-size-partition, and the atom
catalog. These are arithmetic counts, not successful placement counts. Pending
G314 and adopted G313 are not used to label a target solved in this count.

**Method.** Generate the known sorted even domain with sum-pruned recursion;
check total against memoized partition/Gaussian counts. For each A, subset sums
identify indexed minimal zero-sum masks; deduplicate their value multisets.
Count inventory partitions recursively with memoization and nondecreasing atom
type order, always consuming a smallest remaining value. This forgets both
component order and equal-copy labels. No collection or spatial placement
exhaustion. The size-partition coefficients are the multiset exact-cover
inventory generating-function coefficients.

**Predictions BEFORE run:** total collections<2,000,000; distinct atom types
<100,000; primitive eight-vertex parents>1,000. Counts must sum consistently,
every parent has a factorization, and multiset union reconstructs the exact
parent target. The count, even if small, does not predict a successful packing
or prove full even E28. A larger count refutes the forecast without raising any
cap or opening a placement run.

**Independent controls.** Compare FULL factorization sets from a separate
indexed set-partition recursion, then canonicalize value multisets, against the
memoized coefficient count: every zero-sum multiset on values{-3,-2,-1,1,2,3}
with length2..6, plus64 evenly spaced fixed target ranks floor(j*(326119-1)/63),
j0..63. Count primitives there by directly checking all proper submultisets,
not the primary minimal-mask pruning. Explicit fixtures: (-1,-1,1,1) has two
labelled matchings but one unordered value collection; (-1,-1,-1,1,2) likewise
has one value collection despite several labelled choices/possible atom orders.
These refute naive labelled/ordered counting. Counterfactual: counting a full
zero-sum nonminimal mask as an atom must fail on balanced four moves.
Unexpected: verify whole-collection projection injectivity/reconstruction while
showing the atom(-1,1) occurs in multiple different toy parents. This separates
reusable pieces from nonreusable whole collections.

**Caps/stop:**326,119 parents,250,000 distinct atom types,10M memoized count
states,2M independent control states,40CPU seconds,512MiB peak RSS. On cap
record UNKNOWN/partial counts, no raise/restart or solver fallback. Full count
record outside git; no new proof/PROOFS entry or routine carrying request.
Gut: curiosity and a little unease about paying for the wrong quotient; the
injectivity observation already puts the question on firmer ground. Reasoned:
learn the size/choice structure before authorizing any larger placement work.


### MI150 — B64: the collection space is small, and its main mass is3+5/4+4 (2026-10-16 19:56 BST)

**COMPUTED arithmetic count, no placements tested.** All326,119 even E28
parents counted. There are576,515 unordered primitive move collections and
36,735 distinct primitive MOVE types. A parent offers at most6 collections.
Histogram(number of collections -> number of parents):
1->150,018;2->114,441;3->49,935;4->10,823;5->894;6->8.
The maximum first occurs at rank7,945, target(68,70,96,102,104,110,116,118):
three3+5 collections and three4+4 collections. This is a count of arithmetic
choices, not of different orders, shapes or successful packings.

Selected collection totals / parents OFFERING that size pattern:

|piece sizes|collections|parents offering it|
|---|---:|---:|
|3+5|188234|144362|
|4+4|134457|115180|
|2+6|63442|63442|
|3+4|50612|40800|
|2+3+3|39509|38899|
|2+2+4|28651|28651|
|2+5|24185|24185|
|8|9426|9426|
|7|11433|11433|

Parent columns OVERLAP between patterns and are never added as a solved-domain
tally. The3+5/4+4 rows account for322,691 of576,515 COLLECTIONS; that is where
most joint-choice mass sits. Primitive seven/eight parents total20,859; they
have no proper zero-sum factorization. Primitive parent counts by active
length3..8 are14,281,2,025,7,009,11,433,9,426. The reusable atom catalog can
also contain a shorter core that cannot by itself reconstruct a valid parent;
its counts by length2..8 are14,130,873,3,989,10,870,11,433,9,426.

All three forecasts pass: collections<2M, atoms<100k, primitive-eight parents
>1,000. CPU29.465412s, peakRSS131,452,928 bytes (about125.4MiB), under40CPU
seconds/512MiB.1,564,841 count states. No cap, restart, placement search, witness
construction or interpretation of a factorization as a successful packing.

**Controls.**57 complete toy parent factorization sets and64 fixed spread real
parents independently agree on ALL primitive types and count-by-size-partition;
12,616 reference states. Labelled balanced matchings number2 while their value
collection number1, as required. The repeated-pivot mixed-type fixture also
counts1, avoiding an atom-order double count. Nonminimal full zero masks reject
as atoms. Every real parent's inventory reconstructs its exact target; the
shared toy atom(-1,1) demonstrates piece reuse across different parents.
Domain count agrees with independent memoized/Gaussian counts326,119. This is
a full PRIMARY count with independent complete controls on121 parents, not a
claimed second full count or an independent external verification.

Full artifact `cited/instinct/b64-collection-counts-db6d4ccfe32911fb.json`,
6,150,301 bytes, SHA256
`db6d4ccfe32911fba66625d71a0c2e8df2a82f6879d46caea2a4d0679713fa1e`.
Upload/manifest verified, preregistration1082a510; source
 tests/probes/instinct/path_forest_collection_counts.py. parent_rows are in
increasing target rank (the B57 lexicographic convention), each containing
(total collection count, list of [piece-size-pattern-id,coefficient]); catalog
contains all primitive signed move multisets. Raw contains no spatial search.

**What the count changes.** The full finite even-E28 problem has only6 arithmetic
factorization choices per parent; an exhaustive EXISTENTIAL certificate looks
plausible. It is not established by this count: the order/origin search inside
each atom can still be expensive or fail. Whole collections cannot compress
across targets, by MI149's injectivity argument; caching placement maps by the
36,735 atom types is the actual reuse opportunity. The count moves the next
choice away from another isolated six-core lemma toward a whole-method check.
No immediate larger geometry exhaustion or full target solver is opened.

**Next step, following CL425's order.** Parameterize the method by an EVEN
number m of odd tokens in the exceptional range24..32. There are m/2 pairs summing2m. For eight bins use
h=(1 repeated16-m/2 times,2 repeated m/2-8 times); then sum h=m/2 and moves
(t_i-2m*h_i)/2 sum0. At m26 this is three1's/five2's; at m30 one1/seven2's,
not the m28 role vector copied unchanged. E_m has target bounds68..66+2m and
sum m^2; all-even rank coordinates x=(t-68)/2 have bound m-1 and total
(m^2-544)/2. Sorting gives max positive+max negative<=m at the role boundary.
The low-role moves start34-m and high-role positive moves end33-m, keeping
role provenance recoverable. This is a hand parameterization, no level sample
or new count run yet. Next block will preregister a bounded m26/m30 portability
check before deepening m28; mixed odd-cardinality model follows separately.

**Niggle sweep: three.** (1) Does canonical atom order lose collections with
repeated smallest moves? Independent indexed partitions are deduplicated only
after construction and agree, including the mixed-type pivot fixture. (2)
Could low/high ownership be lost in the quotient? The two>=6 moves recover
the low roles; each reconstructed real target matches exactly. (3) Do small
counts imply packability/cheap orders? Explicitly no; the next test measures
portability and the order/origin cost remains. No unresolved niggle.
Gut: relief that the full arithmetic space is manageable, and a stronger pull
toward the whole mechanism than toward more local exceptions. Reasoned:
count requested by Cloud is delivered; proceed to level-parameter check with
new predictions, without waiting for G314 or claiming full even E28/L8.


### MI151 — B65 claim: does the even exchange method travel to26/30? (2026-10-16 20:06 BST)

**Question/pull, before testing.** The attraction is portability, not another
m28 exception: does the unchanged primitive/opposite-sign packing mechanism
survive three low roles at26 and one at30? Success would support a general
construction; a failure would expose where the complementary-pair budget bites.
Record searched: m26|m30|level.*portability|general.*level|parametri ->43 hits,
including MI045's older below68 pilot and MI150's parameterization; no current
26/30 even portability sample. CL425 asks this after the collection count.
Known opposite-sign orders remain credited to Plagne-Tringali (MI126).

**Frozen model.** m is the even token count, pairs sum2m, labels
min(x,m-1-x), x in0..m-1. Slots h=(1 repeated16-m/2 times,2 repeated m/2-8
times); moves e=(t-2m*h)/2. All-even sorted targets68..66+2m sum m^2.
Coordinates (t-68)/2 lie0..m-1, total(m^2-544)/2. Choose factorization,
opposite-sign order after any first term, and disjoint label placements jointly.
No target exception, role search, arbitrary-order or exact-solver fallback.
Zeros only receive filler pairs. Odd targets are outside this cardinality model.

**Sample/predictions BEFORE run.** Independently draw2000 distinct uniform ranks
at each level26/30, seeds20261026/20261030, using exact rank/unrank with Gaussian
count control. Predict >=95% witnesses at26, >=99% at30, and a higher witness
rate at30 (equality refutes the strict comparison). No inference about all targets,
odd targets or full L8 from the samples. A failed complete restricted search
refutes only that target's prescribed class; a cap means UNKNOWN.

**Controls/counterfactuals.** Exhaustive tiny rank/unrank domains as in B57;
first12 targets EACH level: complete component-label maps by independent raw
multiset permutations plus literal physical roots, and separate set packing.
Every witness checked by two independently written validators: flattened sorted
pool/cardinalities/sums versus bit inventory/subtraction. Twenty-four evenly
spaced m28 ranks cross-check status against frozen B57 (separate budget).
Reject copied m28 h at26/30 by pair-total mismatch. Reflection fixture(0,25):
at root0 m26 must collide, while a wrong constant27 does not; prefix mask must
agree with literal roots at all stages of(0,3,-4,7). Every level must reject
repeated-token and coverage-preserving unequal-bin-sum corruption. Unexpected:
check low/high move provenance remains disjoint and max positive+max negative
<=m on every sample; this tests parameterization, not merely final partitions.

**Caps/stop.**2000 targets/level,20k nodes/target,4M nodes total,30CPU seconds
including controls,4M reference words/20M reference roots,256MiB peakRSS.
Stop on global cap, retain partial/UNKNOWN; target-node cap continues sampling.
No raised cap/restart for mathematical failure, target repair, full census or
new carrying request. Source will be path_forest_level_portability.py; full raw
outside git and immutable shared-store delivery. Niggle now: accidental27/28/14
constants are the main danger; literal checks and the deliberately wrong
reflection/role controls target it directly. Gut: curious and alert; reasoned:
this tests a structural change at modest cost. Mixed-parity model is separate.


### MI152 — B65: portability sample succeeds at26 and30 (2026-10-16 20:08 BST)

**MEASURED success, COMPUTED individual certificates.** The frozen prescribed
class returns WITNESS for2000/2000 distinct uniformly sampled even E26 targets
and2000/2000 even E30 targets. No UNKNOWN, exhausted-class failure, role repair,
exception lookup or fallback. Even-domain counts are86,952 at26 and41,881 at30,
agreeing between memoized partition counts and Gaussian coefficients. Seeds
20261026/20261030 and rank conventions are unchanged from MI151.

Negative-move strata at26:2->11,3->386,4->1045,5->558. At30:
1->29,2->236,3->567,4->593,5->401,6->143,7->31. All certify. This reaches
several signs/roles rather than a single inherited boundary family. Search
nodes243,035/294,320 by level; maxima2576/4918 per target. Total539,318 nodes
includes controls. CPU6.265620s, peakRSS27,189,248bytes, all within caps.

**Predictions.** >=95%/99% witness forecasts pass. Strictly higher observed
success rate at30 is REFUTED by the tie; no claim that the two population rates
are equal. The target-class portability prediction survives this sample. No
full even E26/E30/E28 theorem or full L8 conclusion follows.

**Controls.**119 full component-label placement maps and24 full packings (first12
each level) agree with independent raw permutation/literal physical-root and
set-packing instruments:55,890 raw words,36,900 literal roots. Every4000 final
partition passes two different validators (sorted token inventory/cardinalities/
sums; bit inventory with per-bin target subtraction). Tiny rank/unrank domains
pass;24 spread m28 status checks agree with frozen B57. Copied m28 slot totals
reject at26/30; the deliberately wrong27 reflection misses the collision(0,25)
at m26 root0, while both correct instruments catch it. Prefix origin masks
agree with literal roots throughout(0,3,-4,7). Each level's repeated-token and
coverage-preserving wrong-sum mutations reject in both validators. Unexpected
check passes on every target: low/high move provenance is disjoint and the
positive/negative extremal sum<=m; roles have genuinely changed with the level.

Full raw `cited/instinct/b65-level-portability-998c17b7602ead48.json`,
5,487,451bytes, SHA256
`998c17b7602ead4830197d887b1715bb0aad5972857300d77def49b202d765b2`.
Preregistration6c776421, source tests/probes/instinct/path_forest_level_portability.py.
Immutable upload receipt and manifest verified. This is a single-party sample
with independent instruments/controls, not an external second full verification.

**What changed/next.** Fixed-role even exchange works across three tested levels
without m28-specific patches. That strengthens the pull toward the whole
construction. The unresolved universal step is still joint reflection-free
placement, not merely zero-sum order existence. Cloud's next question is more
consequential than another local case: define the mixed/odd-cardinality model
precisely before constructing it. Even-bin cardinalities cannot serve odd target
sums; we must change that invariant explicitly. No mixed-parity experiment or
full census is opened here; G314's carrying read remains nonblocking.

**Niggle sweep.**(1) Accidental inherited level constants: wrong-role/reflection
controls plus generalized literal validators pass.(2) Is equality counted as
higher? No: the strict prediction is recorded REFUTED.(3) Is a successful sample
being promoted to a universal proof? No, statuses/scope above retain the gap.
No unresolved niggle. Gut: delight at portability, fresh curiosity about parity;
reasoned: the level change succeeded cheaply, so follow the parity question
rather than spend another turn refining an already successful sample.


### MI153 — B66 claim/model before counting: split-pair anchors (2026-10-16 20:19 BST)

**Question/pull.** CL425 step3: what does odd cardinality force, and what exact
certificate class could replace the even pair model? The attractive picture is
one singleton anchor in each odd bin, with whole pairs around it. Unease:
anchors consume precisely the labels the later correction may want. I want that
joint restriction visible before any constructive sample. Record searched:
odd.cardinality|mixed.parity|triple.*complement|parity.*transfer ->153 hits/30
files. MI047-050/G304-G305 read:2-for1 parity transfer explicitly changes4/4
cardinalities to3/5; separate parity and chain constructions cannot simply be
composed. No new literature theorem/novelty claim or new proof filing here.

**Necessary sizes.** Let p_i=t_i mod2, q=sum p_i. Since the tokens are odd,
c_i=|bin_i| has parity p_i, sum c_i=m, and q has parity m. In our range24..32,
each target>=68 exceeds the largest single token2m-1<=63, so c_i>=2+p_i.
Write c_i=2+p_i+2z_i, z_i>=0, sum z_i=r=(m-16-q)/2. Thus ignoring further
arithmetic constraints there are binom(r+7,7) vectors for each labelled parity
pattern. Also necessarily c_i^2<=t_i<=c_i(2m-c_i), by the smallest/largest c_i
odds. These conditions do not promise a partition. A target can admit several
size vectors; counts by p are disjoint, counts by c generally overlap.

**Exact proposed split-anchor certificate, m EVEN.** Choose q/2 complementary
pair labels R from0..m/2-1. Distribute their q individual odd tokens bijectively
as anchors a_i to the odd bins. Put a_i=0 in even bins. Choose h_i>=1 with
sum h_i=(m-q)/2 (equivalently h_i=1+z_i, c_i=2h_i+p_i). Each bin's baseline
sum is s_i=2m*h_i+a_i; sum s_i=m^2 because complete reserved pairs sum qm.
The integer moves e_i=(t_i-s_i)/2 sum0. For each active e_i choose an index
x_i in0..m-1; require all folded labels min(x_i,m-1-x_i) distinct and outside R,
and the multiset of x_i+e_i equal to the multiset of x_i. Allocate the whole
pair of x_i to bin i; fill its remaining h_i pair slots with the remaining
unreserved pairs, then simultaneously replace selected token2x_i+1 by
2(x_i+e_i)+1. Anchors stay fixed. This produces exact target sums/cardinalities
and full coverage IF the stated joint certificate exists. Zeros need fillers
only; pair slots suffice since h_i>=1. This is a sufficient restricted model,
not asserted necessary for arbitrary odd partitions or for G304's construction.
At q=0 it reduces exactly to the even exchange model with a chosen slot vector.

The2-for1 exchange and split anchors are two ways to break the even-cardinality
invariant, not the same allocation proof. The split model's unresolved existential
choices are R, anchor assignment, h, factorization, orders and origins TOGETHER.
A negative result in any fixed choice/class would not refute the target.
For odd m, q is odd and q anchors cannot be a union of complete pairs; the
central singleton of G310 requires a separate model. Do not silently extend this
one to odd m. Necessary size equations themselves still apply there.

**Count-only experiment, BEFORE run.** Count sorted E28 targets by their exact
8-position parity pattern p, and aggregate by q. Predict: all q=0,2,4,6,8
occur; q=4 is largest; mixed domain>98% of24,688,633; pattern counts partition
that known total, all-zero pattern326,119. These count membership, not solvability
of the anchor model. No construction, sample, anchor search or target census.

Primary instrument: sorted offsets y=t-68,0..54,sum240. Gap bits
b_i=p_i xor p_(i-1), p_0=0 (indices1..8), gap_i=2u_i+b_i.
Then count u>=0 with sum(9-i)u_i=T=(240-sum(9-i)b_i)/2,
sum u_i<=B=floor((54-sum b_i)/2), via a two-variable coefficient DP.
Independent instrument: y_i=2v_i+p_i; subtract from v_i the number d_i of
preceding1-to0 descents in p. The residual is nondecreasing, between0 and
H=floor((54-p_8)/2)-d_8, with sum S=(240-q)/2-sum d_i. Use Gaussian
coefficients for this rectangle. Also count by q directly with a separate
bounded-length multiset DP over all offsets0..54, without gap/parity transforms.
Tiny literal domains (k1..4, bound0..5, all totals/patterns) must agree.

**Counterfactuals/unexpected/stop.** Odd q at even m must count zero; dropping
the1-to0 staircase must fail on k2,bound3,total3,p=(1,0): true count1, naive2.
Unexpected: p and its reversed pattern have equal counts under y_i->54-y_(9-i),
because8*54-240=192 differs from240: do NOT assume symmetry at the SAME total;
check exact complement relation at total192 instead. Predict at least one
same-total reversal mismatch. Size-vector formula checked on tiny direct
compositions and m28 q classes; raw upper/lower sum bounds remain necessary
only. Caps256 patterns per total, two complementary totals,10CPU seconds,
256MiB peakRSS. Stop on mismatch/cap; retain failure, no raised cap or construction
fallback. Raw counts outside git, source path_forest_parity_model.py. No carrying
request for definitions/counts; substantive new existence theorem still absent.


**B66 instrument correction BEFORE any run.** The proposed negative-control
fixture k2,bound3,total3,p=(1,0) is too small: its true and naive counts are
BOTH1, not1/2. Hand expansion catches this before executing any count. Replace
only that fixture by k2,bound5,total5,p=(1,0): literal(1,4) is the sole sorted
pair, while naive half-coordinate pairs(0,2),(1,1) count2 and the latter gives
unsorted(3,2). Retain the failed original control here. Domain, forecasts,
algorithms/caps unchanged; replacement is checked by hand before the run.


### MI154 — B66: parity model specified; exact domain by pattern counted (2026-10-16 20:20 BST)

**Definition/sufficient certificate, not an existence theorem.** MI153 now states
necessary cardinality vectors and the full joint split-anchor certificate. Its
bookkeeping is a direct extension of the complementary-pair allocator: reserved
pairs supply singleton anchors; unreserved pairs supply one selected token per
active bin plus fillers; permutation of selected tokens supplies even corrections.
No assertion that every target has these choices, no constructed mixed target,
no sample, no proof filing or carrying-read queue. The model may be too narrow;
that is a useful next thing to learn rather than an assumption to hide.

**COMPUTED counts only.** All256 sorted-position parity patterns counted;128
have positive count and128 odd-q patterns have zero. Two exact transforms agree
on each pattern. Complement relation at total192 agrees for all patterns;
separate direct multiset DP over actual offsets0..54 agrees on q marginals:

|odd bins q|E28 targets|unfiltered size vectors PER parity pattern|
|---|---:|---:|
|0|326119|1716|
|2|6040756|792|
|4|12680918|330|
|6|5382660|120|
|8|258180|36|

Total24,688,633; targets with any odd sums24,362,514 (about98.7%). The q8
row is all-odd, not literally mixed even/odd; throughout this diagnostic
"mixed domain" means the complement of the all-even model, including q8.
These are disjoint TARGET counts by parity, not solved domains. The last
column counts all z-compositions before c_i^2<=t_i<=c_i(56-c_i) or any token
allocation; it is not the number of feasible cardinality vectors for each
specific target, and different size choices cannot be added as target coverage.
In particular q8 allows one7 and seven3 (8 choices), or two5 and six3
(28 choices), each summing28.
No other q8 size pattern meets the token count.

**Forecasts/controls.** All even q occur, q4 largest, outside-even proportion>98%,
and at least one same-total reversal mismatch: all forecasts pass.1,650 tiny
literal tuple/total/pattern checks and all their direct q marginals agree.
Tiny z-composition checks and all m28 q-class size-vector counts agree with
binomial formula. The original proposed negative-control fixture was caught
BEFORE execution as ineffective and retained in MI153/52031895; literal
expansion confirmed true/naive1/1. Corrected fixture bound5,total5 gives1/2,
rejecting the omitted-staircase count. No data/cap/forecast changed.

**Unexpected check matters.**102 patterns disagree with their reversal at the
SAME total240. First lexicographic case p=(0,0,0,0,0,0,1,1) has242,623 targets,
reverse270,835. Complement reverses the pattern but changes offset sum240 to192;
it does not authorize equality at240. Full complement identities pass. This
prevents an unjustified factor-two quotient in a future parity sampler.
CPU0.085802s, peakRSS12,480,512bytes; caps10CPU seconds/256MiB not approached.

Artifact `cited/instinct/b66-parity-model-104dba0c6e38900f.json`,53,690bytes,
SHA256 `104dba0c6e38900f1c1c3fe3f14663dd5b98cbe435b3191816d000c001a30ae8`.
Preregistrationfe3413be, control correction52031895; source
 tests/probes/instinct/path_forest_parity_model.py. Immutable receipt/manifest
verified. Independent instruments are self-checks, no external review claimed.

**What changed/next cheap question.** Cloud's three requested preliminaries are
complete: collection space, even-level portability, odd-cardinality definition
and domain counts. The model's real obstruction is choosing anchors/slot sizes
and folded-disjoint cycles together. A follow-up diagnostic must freeze an
explicit bounded anchor/size selection policy before sampling, retain failure
as restricted-model/policy failure, and validate all tokens/cardinalities/sums.
Do not sample parity patterns uniformly: their counts differ, so sample full
sorted targets by uniform rank and report q strata. No such experiment begins
in B66; no new large census or geometry exhaustion follows automatically.

**Niggle sweep.**(1) Sufficient versus necessary model? Explicit restriction,
not a characterization of all odd partitions.(2) Size-vector overlap? Last
column unfiltered per-pattern possibilities only, no multiplied coverage.
(3) Odd token levels? q odd cannot be reserved in complete pairs; separate
singleton model required.(4) Transformed count independence? Different gap-DP
and Gaussian staircase algorithms, literal tiny controls and direct full q
marginals all agree. Gut: pleased to have the parity gap represented honestly,
and curious about its first real test; reasoned: definitions/counts are complete,
but not yet progress on existence for a new mixed target. No review halt.
