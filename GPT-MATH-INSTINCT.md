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


### MI155 — B67 claim: first fixed-policy split-anchor pilot (2026-10-16 20:29 BST)

**Pull/question.** Does the MI153 sufficient model actually reach mixed targets,
with a small explicit anchor policy rather than unbounded allocation search?
Record searched: split.anchor|anchor.*policy|anchor.*cycle|singleton.*anchor ->17
hits/7 files, only MI153-154 current model; no prior anchor-policy run. CL425
preliminaries complete. Work this obstruction, no new literature result imported.

**Frozen sample/policy BEFORE run.**128 distinct uniform ranks in the FULL
sorted E28 domain24,688,633, seed20261067, offsets0..54,total240 via B57 rank/
unrank. Report all q strata, not uniform parity patterns. At q=0 use original
h=(1,1,2,2,2,2,2,2), no anchors. For q>0, up to16 policies: reserve q/2
consecutive labels cyclically modulo14, starting at0,2,4,6,8,10,12,13 in that
order. In each reserved set, sort all q physical odd anchor values ascending;
assign to odd-target bins in ascending index, then reverse assignment as second
policy. No further anchor choices or target-specific exceptions. Start h_i=1;
distribute (28-q)/2-8 extra whole pairs one at a time to the bin with largest
current residual t_i-a_i-56*h_i, smallest index on ties. Necessary size-square
bounds reject impossible policies. Under each policy use the unchanged indexed
primitive factorization/any-first opposite-sign order class, discard all
placements touching reserved labels, pack remaining components jointly.

Predict >=50% of sampled targets containing odd sums certify; all sampled q0
certify; at least one success requires a policy after the first. Caps/failures
count against the success fraction. A complete failure means POLICY_EXHAUSTED,
not that the whole split-anchor model, arbitrary odd partitions or L8 fail.
No repair, alternate h, arbitrary-order fallback, larger anchor search or census.

**Controls BEFORE run.** Literal hand fixture t=(68,69,99,100,112,112,112,112),
R={6}, anchors a_1=13,a_2=43 (indices0..7), h=(1,1,1,2,2,2,2,2), moves
(+6,0,0,-6,0,0,0,0), selected x_0=1,x_3=7. Check both complete token inventory
and all sums/cardinalities with two independent validators. Replacing selected
indices by6,12 still permutes them but touches R: must reject. Wrong anchor43
changed to41 must reject. Coverage-preserving wrong-sum and duplicate-token
mutations reject. First attempted policy of first FOUR odd-containing sampled
targets: FULL component-label maps versus raw permutation/physical-root reference
and independent set packing, with reserved-label exclusions on BOTH. Tiny rank
controls imported from earlier validated sampler, N agrees Gaussian.
Unexpected: measure whether reverse assignment/later R rescues first-policy
failure; record extrema sum>28, since even-role range proof no longer applies.

**Caps/stop.**128 sampled targets,16 policies/target,10k nodes/TARGET across
policies,1M global nodes,10CPU sec/256MiB,1M raw reference words/10M roots.
Target cap records UNKNOWN and continues; global cap stops partial, no raise or
restart for a mathematical failure. Full raw outside git; source
path_forest_split_anchor_pilot.py. No review halt/new proof filing. Gut: warm
curiosity, with unease about losing the even range guarantee; reasoned: a small
pilot can reject this cheap policy without becoming a generalized solver project.


### MI156 — B67: all128 targets certify on the FIRST anchor policy (2026-10-16 20:32 BST)

**MEASURED pilot, COMPUTED individual partitions.**128/128 uniform full-domain
E28 targets certify: q0/2/4/6/8 strata3/30/64/30/1. Thus125/125 sampled targets
outside the all-even class certify. Every target succeeds on its FIRST policy:
R={0,..,q/2-1}, anchors sorted ascending into odd-bin order, greedily allocated
whole-pair slots. No reversed assignment, later reserved set, size-bound reject,
cap, fallback or target repair is used. This is the first mixed-target sample
for MI153's model, not a universal result or a full-domain certificate.

>=50% mixed-success forecast and all-even forecast pass. The prediction that a
later policy would be required is REFUTED (0/128 needed one).11,751 total nodes,
maximum1027/target; CPU0.250950s, peakRSS19,804,160bytes, far below frozen caps.
A small fair sample supporting100% observed success is not a calibrated100%
population prediction. Only one q8 case was drawn; q strata have different masses.

**Independent controls.** First-policy complete component-label maps for the
first four odd-containing targets agree with raw permutation/physical-root
reference:20 maps,1412 raw words,13,328 roots. Four full set-packing references
agree; both independently written token-inventory/sum validators pass on all128
partitions, including required cardinalities in the first validator. Hand fixture
and reserved-pair reuse/wrong anchor/duplicate token/coverage-preserving wrong
sum controls all pass. N=24,688,633 agrees Gaussian/memo counts; rank roundtrips
pass for all sampled targets. These are independent instruments, not an external
second read. No new carrying request.

First sampled target, rank5,485,352, is(70,83,85,105,107,107,112,115), q6.
Its bins (in target order) are:
(21,49);(1,11,13,15,43);(3,37,45);(5,9,17,35,39);
(23,33,51);(7,47,53);(25,27,29,31);(19,41,55).
Every odd1..55 occurs once. Anchors(1,3,5,51,53,55) occupy the six odd bins;
slots are(1,2,1,2,1,1,2,1), integer moves(7,-15,13,-6,0,-1,0,2).
This illustrates an actual allocation, not just parity arithmetic.

**Unexpected observation/range caution.** Four first policies have positive/
negative extrema sums>28 (33,32,30,32), yet certify. First such rank14,200,732,
target(75,81,92,96,102,106,110,122), moves(9,-15,18,-8,-5,-3,-1,5).
The old even-role extremal bound does NOT extend to these anchor choices;
existential factorization/order is doing useful work beyond that sufficient
bound. All observed h_i are1/2, but no theorem about greedy slot sizes is claimed.

Full artifact `cited/instinct/b67-split-anchor-d162c854c429b676.json`,252,469bytes,
SHA256 `d162c854c429b676c0372690c24d7f14954b07abef5d09542c66b724fab010e8`.
Preregistrationaa2cefa4; source tests/probes/instinct/path_forest_split_anchor_pilot.py;
immutable upload receipt/manifest verified. All policies/anchors/slots/moves and
final partitions are retained outside git; no sampled failure to discard.

**Hand observation/next question, not another experiment.** With the FIRST
reserved set R={0,..,q/2-1}, the remaining physical odd tokens are the contiguous
interval q+1,q+3,..,55-q. Subtract q from each: these are precisely the first
N=28-q odds. Given slots h, removing the anchors and shifting tokens changes
the target to T_i=t_i-a_i-2q*h_i. Then sum T_i=N^2, all T_i even, and
(T_i-2N*h_i)/2=(t_i-a_i-56*h_i)/2=e_i. The folded coordinates shift by q/2;
forbidden extreme labels disappear, leaving the standard reflection N-1.
This explains why the first policy is a natural next object rather than16
unrelated anchor tricks. It does not put T in the earlier minimum68 domain,
prove a move-span bound, or prove any placement exists. Next: inspect the
reduced target/range structure, and calibrate the first policy on a preregistered
larger fair sample only if justified; no run/cap increase is opened here.

**Niggle sweep.**(1) Are odd targets actually covered? Literal complete bins
and parity/cardinality checks,125 mixed witnesses.(2) Are failed policies hidden?
All128 succeed first, none executed later; failed later-policy forecast retained.
(3) Did old range assumptions leak in? No extrema bound imposed, four explicit
counterexamples to its automatic inheritance retained.(4) Is the reduced-pool
identity called a proof of existence? No, it is exact bookkeeping, with new
reduced targets outside the old hypothesis. Gut: surprise and delight; the first
policy is much more effective than expected. Reasoned: the model has earned a
larger diagnostic/structural look, not a universal claim or a new census.


### MI157 — B68: reduced-pool structure and calibrated first-policy sample (2026-10-16 20:44 BST)

**Trajectory reflection (90-minute check due since MI142).** The work is still
enjoyable: mixed targets now have actual certificates and a new representation,
not just another completed local case. The frustration is the universal
folded-packing gap. I would choose this question afresh: why does the FIRST
anchor policy work so easily? The last blocks changed the object (collection
counts, level roles, odd-cardinality model), not repeated a refuted candidate.
No seeded draw. Avoid an endless sequence of larger samples: one B57-sized
calibration now, then a structural decision, not an automatic full census.
Record searched: water.fill|greedy.*slot|reduced.pool|contiguous.*middle|anchor.*range
->5 hits/4 files, only MI156/current pilot relevant. No new prior-art theorem
imported or novelty claim. Known opposite-sign lemma remains credited MI126.

**Hand inference BEFORE experiment: greedy h is always1/2 at E28.** With first
anchors, put d_i=(t_i-a_i-56)/2 and r=6-q/2. All d_i<=33; if q8, all<=32.
A bin already given an extra pair has score at most5 (at most4 for q8). At q0/2/4,
there are8-q>=r EVEN bins with initial scores>=6. At q6, its two even bins and
the odd bin anchored1 give three=r distinct scores>=6. At q8, bins anchored1
and3 have scores>=6 and>=5, two=r, both above the score<=4 after selection.
Before r distinct selections have occurred, an unselected member of these
sets always beats every previously selected score. Therefore no bin receives
a second extra pair. Greedy h simply chooses the r largest initial d_i (same
index tie-break), yielding h2 r times/h1 8-r times. This is a model-specific
hand SKETCH, not a theorem of joint placement or new PROOFS/review entry.

Thus N=28-q remaining tokens have exactly the familiar slot counts
h1:16-N/2=2+q/2, h2:N/2-8=6-q/2. Sorting by t-a orders these roles, but
T=t-a-2qh need not remain sorted across the role boundary. Anchor-high bins
may have negative moves in an h1 role; the even sign/range theorem does not
transfer. The rank/role reduction simplifies choice, not the hard assertion.

**Frozen calibration BEFORE run.** Use exactly the2000 uniform distinct full E28
ranks from B57's unconditional sample (seed20261017,N24,688,633), not a newly
selected favorable group or uniform parity patterns. Its25 even cases have
already certified under B57;1975 other targets were then parity-inapplicable,
not known successes for this model. Use ONLY B67's first reserved set/ascending
anchors/greedy h, no second policy, role repair or arbitrary-order fallback.
Predict >=99% of all2000 certify, zero caps, and all greedy h1/2 identity checks
pass. Any complete failure stays FIRST_POLICY_EXHAUSTED, not model/target failure.
No implicit universal100% prediction; no experiment after this calibration
without a new mathematical question/registration.

**Independent/negative/unexpected controls.** Reuse B67's literal hand fixture
and all four corruption checks. First12 odd-containing cases: full component
maps via independent raw permutations/physical roots plus separate set packing.
All final partitions pass both B67 validators; separately remove each actual
anchor, subtract q from remaining tokens, and check inventory exactly first N
odds, each sum T_i and length2h_i. Compare greedy h with independently sorting
initial d, on every target including a tied-score hand input. Deliberately omit
one removed extreme label in the effective-pool fixture: exact inventory rejects.
Unexpected check: retain/count successful moves with extrema>N and distinguish
from extrema>28, rather than importing either sufficient bound. Counterfactual
T sortedness across h roles must not be assumed; record any reversals.

**Caps/stop.**2000 targets,20k nodes/target,5M total,30CPU seconds/256MiB,
2M raw reference words/20M roots. Target-node cap continues as UNKNOWN; global
cap stops partial, no raise/restart/second policy. Full raw outside git; source
path_forest_first_anchor_calibration.py. This is evidence calibration plus the
specific greedy-slot inference; no full-domain run or new carrying queue.
Gut: warm curiosity, more attraction to the reduced representation than to a
higher success tally. Reasoned: one larger fair check earns a decision about
proof structure and exposes any exceptions; it is not the decision itself.


**B68 pre-run tie convention clarification.** q0 explicitly retains B57's
fixed sorted roles, not B67's mixed-case greedy loop. For the independent
score-sort comparison, q0 ties choose larger indices (the original last-six
h2 roles); mixed q>0 ties choose smaller indices as preregistered. The1/2 slot
multiset/proof is unchanged. This distinction is recorded before any run;
compare(98 repeated8) as a tie fixture, without modifying B57's frozen roles.


### MI158 — B68:1996/2000 certify; four real first-policy exceptions (2026-10-16 20:48 BST)

**MEASURED calibration, COMPUTED certificates/restricted-search outcomes.**
Exactly B57's2000 unconditional ranks (seed20261017) tested, FIRST policy only.
1996 WITNESS,4 FIRST_POLICY_EXHAUSTED, no cutoff or size-bound rejection.
By q:0->25/25;2->512/512;4->1030/1030;6->410/412;8->19/21.
The1975 targets B57 could not address by parity now give1971 checked positives
and4 restricted failures. These are not full-model/partition impossibility claims.
>=99% forecast passes at99.8%; zero-caps and slot1/2 predictions pass.
Maximum2647 nodes/target,218,066 total; CPU3.071017s, peakRSS29,478,912bytes.
No second policy, target repair, extra search, raised cap or census.

**Controls/structure.**59 full component maps and12 full packings (first12
odd-containing targets) independently agree,48,582 raw reference words/35,280
physical roots. All1996 partitions pass both B67 validators. Removing their
actual anchors and shifting remaining tokens by q gives exact first N=28-q
odd inventories, even sums T and sizes2h, with identical moves and reflection
N-1. All2000 greedy slot vectors agree with the independent initial-score sort;
q0 retains frozen B57 ties as clarified BEFORE execution in7f541a18. Tied even
and mixed fixtures pass. Omitted removed-extreme-token inventory rejects.
The hand no-repeat argument in MI157 stays a SKETCH, not promoted by controls.

1,092 successful policies have extrema sum>N;16 have extrema sum>28.
1,061 show a role-boundary target reversal after reducing the pool. First:
t=(75,87,88,93,109,110,110,112), a=(1,3,0,53,55,0,0,0),
h=(1,1,2,1,1,2,2,2), T=(66,76,72,32,46,94,94,96), N24.
The largest unselected effective score belongs to bin1, but T_1=76 exceeds
the smallest selected role's T_2=72. Importing the old sorted-role/range
hypotheses is demonstrably invalid. No general placement theorem is asserted.

**The four failures, retained in full.** R always the first q/2 labels;
all anchor/slot arrays and every search outcome are in the raw artifact.

|rank|q|target|moves|
|---:|---:|---|---|
|16461642|8|(77,77,83,85,107,117,119,119)|(10,9,-17,-17,1,5,5,4)|
|24592715|6|(90,90,91,91,93,103,111,115)|(-11,-11,-11,16,16,-2,1,2)|
|6321549|8|(71,73,77,105,107,109,121,121)|(7,7,-20,-7,1,1,6,5)|
|2079026|6|(69,69,75,103,111,116,120,121)|(6,5,-21,-2,1,2,4,5)|

Full artifact `cited/instinct/b68-first-anchor-a580dd9bea76765b.json`,
4,865,938bytes, SHA256
`a580dd9bea76765b479d18a9656fb17cc6d28c2ff5ee8e42a9598902e9d4cc3e`.
Prereg11fab479, tie clarification7f541a18, source
 tests/probes/instinct/path_forest_first_anchor_calibration.py. Immutable receipt/
manifest verified. Independent instruments are self-checks, not an external
review of the whole sample/failure exhaustion.

**Post-run HAND diagnosis (SKETCH, no new experiment).** Three failures are
impossible even if arbitrary cycle orders are allowed, keeping these anchors,
slots and the one-selected-token-per-active-bin rule. In N coordinates a move
d joins x to x+d. A displacement>N-1 has no physical edge. For
(N-1)/2<d<=N-1, its folded endpoint labels are{x,L-x},
L=N-1-d, x=0..L; omit the equal-label loop. These form a matching with at most
floor((N-d)/2) nonloop edges. Two same-signed d moves cannot share a physical
endpoint, since that would require a consecutive2d displacement outside the
pool; distinct chosen tokens also have distinct labels. Thus repeated same-
signed large moves need that many disjoint matching edges. This is a necessary
constraint on the proposed certificate class, not on arbitrary partitions.

- Rank16461642, N20: two-17 moves; L2 offers ONLY folded edge{0,2}; x1 is
  the forbidden loop{1,1}. Two such moves cannot coexist. Orders/factorization
  cannot fix this without changing anchors/slots or the one-token model.
- Rank6321549, N20: move-20 exceeds every physical displacement19, impossible.
- Rank2079026, N22: move-21 can only join0 and21, the SAME folded label, impossible.

Rank24592715 is different. Its primitive components are uniquely the cancelling
pair(-2,+2) and the six-list(-11,-11,-11,16,16,1), in N22. Two consecutive-11
moves already leave0..21, so any six-cycle must alternate the three negative
moves with its three positive moves. Up to rotation their positives(16,16,1)
have only one cyclic order (the two16's coincide). The representative vertex
set is{0,16,5,21,10,11}, span21; only root0 is in the pool, with complementary
pairs0/21,5/16,10/11. Thus this primitive six-cycle has no reflection-free
placement under ANY order. This hand argument explains the prescribed primitive
factorization failure. It does NOT exclude an un-factored eight-cycle merging
the cancelling pair, or a changed anchor/slot assignment. Those are distinct
next questions. The raw primary exhaustion alone had not established this
all-order distinction; the carrying hand reasoning is written here explicitly.

**Decision after calibration.** No further broad sampling now. The next bounded
question is these FOUR targets: independently audit full order/packing failure;
for the second, distinguish primitive-only failure from a merged eight-cycle;
for the other three, test an explicitly preregistered anchor/slot change after
the proved geometric obstruction. No such repair run starts in B68. This is a
change of representation/trajectory, not pretending a failed sufficient method
has refuted the original target. G314 review remains nonblocking; no new routine
proof filing/carrying request for this diagnostic.

**Niggle sweep.**(1) Does first-policy exhaustion refute targets? No.(2) Can
arbitrary order repair three? The necessary displacement/matching arguments
exclude it under fixed anchors/slots; changing either remains open.(3) Is the
six-cycle obstruction a full eight-cycle obstruction? Explicitly not.(4) Are
we rewarding another success tally? We stop broad sampling and follow the four
explanatory failures. Gut: satisfaction and renewed curiosity; the exceptions
are more interesting than an unbroken success rate. Reasoned: structural slot
choice is simplified, first-policy universality is false, and the next change
is now mathematically constrained rather than another blind policy sweep.


### MI159 — B69: four-target all-order audit, then bounded repairs (2026-10-16 20:56 BST)

**Question/pull.** Which failures are allocation obstructions, which are merely
a restriction to primitive cycles? Record searched:16461642|24592715|6321549|
2079026|merged.*eight|large.*matching ->21 hits/7 files, only MI158 current
four exceptions. No new broad sample, geometry census or literature claim.
I am particularly drawn to the six-cycle case because cancelling moves may be
useful INSIDE a longer cycle rather than peeled off as an independent piece.

**Hand candidate BEFORE run.** Rank24592715, N22, same anchors/slots, has the
single8-cycle move order(16,-11,2,-11,16,-11,1,-2). Starting at effective root5
its eight selected positions are(5,21,10,12,1,17,6,7); they have distinct labels
(5,0,10,9,1,4,6,7), and closing returns to5. Original pool positions add3.
Owners for this order are(3,0,7,1,4,2,6,5). This is a concrete predicted repair,
not a claim that all nonprimitive cycles or all targets can be handled.

**Audit BEFORE run.** On exactly MI158's four targets, keep FIRST anchors/slots.
Enumerate ALL nonempty zero-sum indexed components, not just primitive ones;
allow arbitrary orders. Compare complete occupied-label sets from adaptive
prefix-mask search versus independent full raw multiset permutations/literal
physical roots. Simple cycles reject repeated partial sums and closing root is
not an extra vertex. Separately compare full set packing with a second method.
Predict three geometric cases have NO witness even in this unrestricted-cycle
model; rank24592715 has one, as the hand candidate specifies. No more original-
policy order search on geometrically impossible targets after these audits.

**Repairs BEFORE run.** For ONLY those other three targets, try the remaining
15 B67 policies in their frozen order (first R reverse, then starts2,4,6,8,10,12,13
ascending/reverse), with B67's exact greedy slots and primitive opposite-sign
class. No new anchor choice, slot optimization or arbitrary-order fallback for
repairs. Predict all three certify within these15; at least one needs changing
R rather than merely reversing the first anchor assignment. Stop at first
certificate per target, retain every preceding failure. A failure exhausts only
these policies, not model/partition existence.

**Independent/negative/unexpected checks.** Both literal bin validators and
exact sum/cardinality/token checks on all positives; materialize the explicit
merged8 candidate before any search. Complete primary/reference label maps and
set-packing decisions for all four ORIGINAL policies. Every actual repair's
complete primitive opposite-sign component maps checked independently too.
For the six-core alone, require no all-order placement; the merged cycle must
be nonprimitive (it contains the zero-sum(-2,+2) subset) while its ordered proper
prefix sums stay distinct. This is the unexpected scope check against treating
minimal factorization as a lossless normal form. Reject reserved-pair reuse,
wrong anchor and coverage-preserving wrong sums via B67 controls.

**Caps/stop.**Exactly4 original targets+<=45 repair policies;250k primary nodes/
target (audit plus repairs),1M global,2M raw reference words/20M reference roots,
10CPU seconds/256MiB. Caps yield UNKNOWN/partial, no raise/restart/policy repair.
No new target sample/full census or proof filing. Source
path_forest_anchor_failure_audit.py; raw outside git. These audits independently
check instruments, not an external reader. Gut: renewed delight at the explicit
long cycle; reasoned: first verify the distinction, then use allocation changes
only where fixed-allocation geometry says they are necessary.


### MI160 — B69: all four repaired; primitive splitting loses a valid cycle (2026-10-16 20:59 BST)

**COMPUTED four-target result, hand diagnoses remain SKETCH.** All-order/all-
zero-component searches at the FIRST anchor allocation agree with independent
literal full-permutation maps and separate packing: three have NO witness in
this one-selected-token model, rank24592715 DOES have an8-cycle. The latter's
primitive six component has0 placements, its cancelling two component10, but
its merged8 component4 distinct occupied-label sets. This is a concrete
counterexample to treating primitive factorization as a lossless restriction
on the exchange-certificate model. It is not a counterexample to odd partition
existence, and the full one-token model remains sufficient only.

The explicit pre-run hand8-cycle from MI159 materializes correctly, with ALL
first-policy anchors and slots unchanged. Its proper prefix vertices are
distinct even though its move inventory contains the zero-sum(-2,+2) subset.
A zero-sum SUBSET need not appear as a contiguous subcycle of the useful order.
The old6+2 primitive restriction was the obstruction here. No full-problem or
novelty claim, new PROOFS entry, or external verification claimed.

**Other three repairs.** Each fails first-anchor reversal (policy index1), then
succeeds at index2: reserved labels start at2, anchors ascend, same B67 greedy
slot rule and primitive opposite-sign class. No later policy, role optimization,
arbitrary-order repair fallback or target-specific exception is used.

|rank|new reserved labels|new moves|successful primitive sizes available|
|---:|---|---|---|
|16461642|2,3,4,5|(8,7,-19,-19,3,7,7,6)|8|
|6321549|2,3,4,5|(5,5,6,-9,3,3,-20,7)|3,3,5,5|
|2079026|2,3,4|(4,3,5,0,3,2,4,-21)|7|

These sizes list available primitive components, not an additive partition of
the row. The shift frees outside pair labels0/1 while reserving interior ones;
it changes the geometry rather than merely shortening the largest step. In the
first repair the two long steps INCREASE from17 to19, yet fit. The last repair
still has a21-step move but can now use distinct outer labels in the full28-site
pool. The earlier N22 complementary-endpoint obstruction applied to the
CONTIGUOUS first-policy remainder, not to this different reserved set. No
universal claim that a two-label shift always suffices.

**Audit/controls.**18 FULL all-order component-label maps and4 full packings
agree on the original four allocations; zero masks independently generated by
indexed recursion. For six attempted repairs (three failures then three
positives),13 full primitive opposite-sign maps and6 packings independently
agree.216,094 raw reference words,880,376 literal roots,73,009 primary nodes,
max42,422 per original-target audit+repair block. CPU4.018391s, peakRSS21,086,208
bytes. All forecasts pass, no cap, run restart, extra target or expanded policy.
Hand candidate, reserved-pair/wrong-anchor/duplicate/wrong-sum controls pass.
All positive partitions pass both literal validators. These are independent
instruments by GPT, not an external second reader of the full negative claims.

**Existing sample delivery audit, no new search.** The B68 raw digest is checked;
its EXACT four non-WITNESS ranks equal these four target ranks. Keep all1996
old partitions unchanged, patch only these four with the all-order8-cycle or
new allocation witness, then run BOTH literal validators on all2000. All pass.
Thus the ORIGINAL B57 unconditional sample now has2000 checked partitions,
using multiple explicitly scoped methods; B68's1996/2000 first-policy result
and failures are retained, not retrospectively relabelled. This sample is not
added to overlapping older counts or presented as full E28/L8.
The source's pure delivery_audit(base,rows) reproduces this post-run verification;
no original/all-order/repair experiment was rerun for the delivery receipt.

Artifact `cited/instinct/b69-anchor-audit-aff8cb81a6e7355b.json`,18,859bytes,
SHA256 `aff8cb81a6e7355b025ba1d27d9aaeb78a883741df1017a2388862e7d4b9ea21`.
Preregistration984b5a18; source tests/probes/instinct/path_forest_anchor_failure_audit.py.
Immutable receipt/manifest verified. Combined sample is represented by the
unchanged immutable B68 artifact plus this four-target patch/audit, avoiding
another duplicate multi-megabyte witness file.

**What changed/next.** We now know which restriction fails and have constructive
repairs: one cycle MERGE, three reserved-pair changes. This prevents fruitless
order search on three impossible fixed allocations and prevents discarding
useful cancelling moves too early on the fourth. No further broad sample or
census. The next mathematical question is whether reserving an INTERIOR block
allows the outer pairs to serve long moves systematically while leaving space
for the remaining core. That needs a general allocation argument or a cheap
counterexample, not another collection of bespoke target patches. No new run
or universal two-policy conjecture is opened here; Cloud check-in is useful
but is not a permission gate, G314 read still nonblocking.

**Niggle sweep.**(1) Search arbitrary components or just larger primitive ones?
ALL zero-sum components/orders, complete sets agree.(2) Are negative maps only
one representative order? Raw permutations/direct roots exhaust, including
nonprimitive cycles.(3) New R mistaken for the old reduced interval? Explicitly
different physical geometry; no N22 bound imported.(4) Is2000/2000 a new fair
first-policy success rate? No:1996 first-policy plus four explained repairs,
original cases unchanged. Gut: delight at the merger and at the geometric
repair; reasoned: useful mechanistic progress, finite scope, next move should
seek structure rather than manufacture more successful examples.


### MI161 — B70: the long edge can fit while the cycle cannot (2026-10-16 21:09 BST)

**Hand block/discovery before machine verification.** The proposed outer-pair
argument is incomplete: reserving an interior block may leave a place for the
large edge but block every way to enter/leave it. Record searched:
interior.*anchor|outer.*pair|large.*move|folded.*matching ->48 hits/23 files,
MI158-160 relevant; follow-up exact tuple/boundary-entry terms23 unrelated hits,
no exact tuple in record. I found the following target by fitting a one-negative
move list to actual anchor sums, not by another random sample:

    t=(69,71,73,109,111,112,118,121), sum784, q6.

First ascending anchor block R0={0,1,2} gives
h=(2,1,1,1,1,2,2,1), e=(-22,6,6,1,1,0,3,5).
The contiguous remainder has N22 physical positions; a22-step move cannot fit.

The inward shift that repaired B69's cases, R2={2,3,4}, gives
anchors(5,7,9,47,49,0,0,51), h=(1,1,1,1,1,2,2,2),
e=(4,4,4,3,3,0,3,-21). There is one negative move, so every certificate cycle
uses it and all six positive moves; zeros need no selected vertex. Any cycle
is a strictly increasing positive path from u to u+21, closed by-21.
Distinct folded endpoint labels outside R2 allow ONLY u=0,1,5,6.
For u0 the first step3/4 lands in reserved labels3/4. For u1 it lands at4
(reserved) or5 (the complement of endpoint22). For u5, the last predecessor
is22 (complement of start5) or23 (reserved label4). For u6 the last predecessor
is23/24, both reserved. Thus NO ordering works, despite available long edges.
This refutes a fixed start0-or2 ascending-anchor recipe, not all B67 policies
or the target. No such universal recipe was previously adopted; this blocks
that tempting generalization before another large test.

**Explicit hand repair, not a policy search.** Reserve R4={4,5,6} instead.
Anchors(9,11,13,43,45,0,0,47), h=(1,1,1,1,1,2,2,2),
e=(2,2,2,5,5,0,3,-19). Owners(0,3,4,1,2,6,7) at physical indices
(0,2,7,12,14,16,19) form a closing cycle, with positive order(2,5,5,2,2,3)
and then-19. Folded labels(0,2,7,12,13,11,8) are distinct and avoid R4.
These choices are B67's existing ascending block-start4 policy, not a new
exception in its instrument. Greedy slots follow directly by taking initial
scores(2,2,2,5,5,28,31,9), extra3 pairs on31,28,9.

**Verification preregistration BEFORE run.** Exactly this ONE hand-selected
E28 target and these THREE allocations, no others. Predict all-order/all-zero-
component maps empty for R0/R2 and nonempty for R4, and the explicit cycle
materializes. Compare full maps and packing with B69's independent literal
permutation instrument; compare the entire maps with known opposite-sign class
as an unexpected check: one-negative cycles can be rotated to put that move
first, so no ordering-class loss is expected in this slice. Independently list
R2's long-edge endpoints and first/last viable entries, versus direct literal
folded-label checks. Counterfactual: accepting a matching edge as a complete
cycle certificate must fail here, while the explicit R4 partition passes both
literal validators and all B67 corruption controls.
Caps3 allocations,100k nodes/allocation,300k total,200k raw reference words,
5M reference roots,5CPU seconds/128MiB; caps stop partial/UNKNOWN, no raise,
restart, fourth allocation or broader target sample. Source
path_forest_anchor_boundary.py, raw outside git. This is a model obstruction/
repair, not a general allocation theorem or new proof-review request.
Gut: a useful push against the attractive shortcut, with curiosity sharpened
by the entry/exit obstruction. Reasoned: long-move matching alone is insufficient;
a real general construction must reserve a compatible approach path as well.


### MI162 — B70: a matching edge is not a route through the anchor block (2026-10-16 21:13 BST)

**COMPUTED verification; hand reasoning MI161 remains SKETCH.** On the single
hand-selected target(69,71,73,109,111,112,118,121), rank2,256,968, both ascending
reserved-block starts0 and2 have0 all-order placements; start4 has12 occupied-
label placements. All3 complete maps/packings agree with independent raw
permutations/direct physical roots. All3 complete opposite-sign-class maps
are IDENTICAL to their all-order maps, as predicted by rotating a one-negative
cycle to start at its negative move. Here changing order classes cannot help.
The explicit start4 cycle materializes, passing both literal validators.
All forecasts/controls pass:6863 nodes,30,240 raw words,65,520 roots,
CPU0.379755s, peakRSS18,214,912bytes. No extra allocation or target, cutoff,
restart, statistical success-rate claim or enlarged policy rule.

**Decisive distinction.** Under start2, there are TWO available folded long-edge
matching edges, and four possible directed positive-path starts0,1,5,6. Starts0/1
have no legal first part3/4; starts5/6 have no legal last part3/4. Each direct
boundary list agrees with the endpoint-label formula. So long-edge matching
capacity passes while every full ordering fails. MI161's hand argument and
this computation block the fixed ascending start0-or2 proposal, not all split-
anchor certificates; start4 explicitly succeeds. The matching observation in
B69 was a necessary constraint, never a sufficient allocation theorem.

**A precise general question replaces that shortcut.** For POSITIVE parts
summing D and one forbidden coordinate interval[a,b] strictly between0 and D,
a path can avoid that interval iff some subset of parts sums to s<a and an
unused part v has s+v>b. Necessity: take the unique crossing step; sufficiency:
order that subset first (all intermediate sums<=s), jump v, then order the
rest (all sums>b). This elementary observation concerns ONE interval only;
extra forbidden endpoint-complements may merge with it, while internal
reflection collisions remain a separate global condition. It supplies the
right boundary-crossing question for adaptive anchor selection, not a proof
that the full folded path exists. No new proof filing/novelty claim.

**Niggle/fresh-choice verdict.** This was worth checking because three sample
repairs tempted a universal two-position rule. But further cheap rejection
screens alone would cool the pull: they can prune allocations without ever
building a full cycle. Stop adding such screens as standalone progress.
Next block must engage completion: select an anchor interval AND a positive
path with no complementary-prefix collisions, or identify a genuine structural
obstruction to doing so. One-negative lists offer the clean first test because
ordering-class loss is absent; no new experiment is claimed now. Gut: curiosity
about a full construction, a push away from more bespoke repairs. Reasoned:
we learned why the attractive shortcut fails; the unresolved carrying inference
is whole-path reflection avoidance after crossing the reserved interval.

**Cloud perspective when useful (no permission gate).** Is there a constructive
route from the interval-crossing criterion to full reflection avoidance for
these one-negative lists, or does the present anchor formulation look like
another case-patching loop? I'll pursue the construction rather than wait for
a routine reply. No carrying proof read requested, G314 remains nonblocking.

Artifact `cited/instinct/b70-anchor-boundary-0205800cc55c812b.json`,5055bytes,
SHA256 `0205800cc55c812bebe4618b9db66e02e76ecf3001abc7d8dec19bca712cdf5f`.
Prereg9fd713a3, source tests/probes/instinct/path_forest_anchor_boundary.py;
immutable receipt/manifest verified. Independent instruments are self-checks,
not an external carrying read. Old2000-sample result remains unchanged.


### MI163 — B71: a whole-path construction using two odd bridge steps (2026-10-16 21:25 BST)

**Hand result before literal verification; SKETCH, no novelty claim.** The push
away from more local screens led to a construction: put every selected outer
position in one parity class, and the sole opposite-parity position in the
central corridor. Record searched: positive-path/complementary-prefix/one-negative/
reflection-avoidance137 hits/31 files, plus parity-bridge/two-odd-step/even-outside
103 hits/31 files. G306's actual one-negative source read; it uses small-tail
prefix avoidance and differs from the construction here. No imported theorem
or new literature-status claim. This is the first completed construction in
this block, not a bound inferred from recent success rates.

**Statement.** Let M be a positive EVEN integer, positions0..M-1, folded labels
min(y,M-1-y). Let s,r be integers, s>=0,r>=1,s+r<=M/2.
Reserve labels R={s,..,s+r-1}, with a nonempty free central corridor
I=[s+r,M-1-s-r]. Let A and B be lists of POSITIVE EVEN parts, possibly empty,
and let a,b be POSITIVE ODD parts. Let x be even, S=sum A, D=S+a+b+sum B.
Suppose

    0<=x,  x+S<s,  c=x+S+a lies in I,
    c+b>=M-s,  x+D<=M-1.

Then the positive path ordered A,a,b,B, started at x, and closed by-D has
all its selected positions distinct, avoids R and uses distinct folded labels.

**Carrying proof.** Strict increase gives distinct positions within0..M-1.
Every selected position before a is even and<=x+S<s. The single position c
between a and b is odd and central. After b all selected positions are even
and>=c+b>=M-s. Thus none is in either forbidden physical interval
[s,s+r-1] or[M-s-r,M-1-s]. Since M-1 is odd, two even positions cannot be
complements. The only odd selected point is c, whose even complement M-1-c
lies in the SAME central corridor. No other selected point is central, so it
is absent. This proves the ENTIRE folded-label condition, including endpoints,
not only entry/exit. Empty A/B do not affect the argument. A selected endpoint
x+D belongs to the closing negative move; the returned x is not another vertex.
This constructs one zero-sum cycle; selecting anchors/slots that produce the
hypotheses remains a separate allocation problem.

**Actual E28 application found by hand.** t=(85,87,89,91,93,95,122,122),
R={10,11,12}, anchors(21,23,25,31,33,35,0,0), choose
h=(2,1,1,1,1,1,2,2), e=(-24,4,4,2,2,2,5,5).
M28,s10,r3,x0,A=(4,4),a=b=5,B=(2,2,2) gives c13 and positions
(0,4,8,13,18,20,22,24), owners(1,2,6,7,3,4,5,0).
All hypotheses hold. This h is an EXPLICIT NON-GREEDY slot choice: B67's
start10 greedy allocator instead places three pairs in one even bin. The old
h1/2 argument was only for FIRST anchors; no contradiction or silent policy
change. The general split-anchor model permits the chosen h, but this example
is not a success of the frozen greedy policy. No universal existence claimed.

**Verification plan BEFORE run.** Exactly four formula geometry fixtures:
above full bridge, A empty(x8,a=b5,B=(2,2)), B empty(x0,A=(4,4),a=b5),
both empty(x8,a=b5). All at M28,s10,r3. Predict all literal folded checks pass
and actual E28 partition passes both inventory/sum/cardinality validators.
Compare greedy slots explicitly, without running any cycle/role search.
Counterfactual: A=(1,1),a11,b5,B=(8,),x0 has even TOTAL sum A and meets the
interval inequalities, but prefixes1 and26 are complements. Individual outer
parts must be even. Also x0,A empty,a1,b17,B=(8,) puts c outside the central
corridor and causes the same collision. Both literal geometry checks must reject.
Unexpected: all empty-list cases and the distinction between even total and
every even part, not another target census. Caps4 positive geometry fixtures,
2 negative fixtures,1 E28 allocator output,oneCPU second/64MiB; no search,
new sample, grid of cases, raised cap or proof-review queue. Source
path_forest_odd_bridge.py; raw outside git. Gut: delight that parity completes
the path rather than rejecting another allocation. Reasoned: a sufficient
construction with honest hypotheses; the next problem is realizing them from
targets, not collecting more hand examples.


### MI164 — B71: parity supplies a complete path, with explicit allocation scope (2026-10-16 21:27 BST)

**Hand construction SKETCH, finite outputs COMPUTED.** MI163's parity bridge
proves a sufficient whole-cycle statement, not just a boundary screen. Two odd
steps pass through exactly one odd selected point in the free central corridor;
all other selected positions are even and outside it. Even positions cannot
pair with each other under odd reflection M-1, and the sole odd point's even
complement is central and unselected. This is the carrying argument; the tiny
formula check does not replace it or upgrade it to PROVED. No novelty claim,
formal PROOFS entry or routine carrying-read request.

All4 preregistered geometry fixtures pass literal all-pairs reflection checks,
including empty A, empty B and both empty. Both counterexamples are rejected:
even TOTAL sum of outer parts does not suffice (prefixes1/26 collide); moving
the lone odd point outside the central corridor permits that same collision.
The one prescribed E28 partition passes both validators. No order/role search,
extra target, grid, sampling, run repair or cap. CPU0.000376s,
peakRSS14,831,616bytes. Arithmetic/types of s,r,M in the statement are explicit;
M even is essential since its reflection swaps parity classes.

For t=(85,87,89,91,93,95,122,122), bins in target order are:
(1,3,7,21,53);(9,23,55);(17,25,47);(19,31,41);
(15,33,45);(11,35,49);(5,27,39,51);(13,29,37,43).
Every odd1..55 appears once. This uses h=(2,1,1,1,1,1,2,2), whereas the
frozen start10 GREEDY h is(1,1,1,1,1,1,3,2). The code verifies both facts.
The generalized anchor model permits the chosen slots; nothing here is credited
to the frozen greedy policy, and no claim that its other slots cannot work.

**What changed/next carrying question.** We have a full constructive mechanism
for lists with two odd positive bridge steps and all remaining positive parts
even, satisfying the stated corridor inequalities. The unsolved allocation
step is now exact: choose anchors and pair slots so the moves have this form,
and partition the even parts before/after the bridge to meet those inequalities.
Changing slots shifts a move by28, so it cannot change its parity at E28;
parity must already be arranged by targets/anchors. A useful next block should
couple that residue choice to actual anchor/slot allocation for a NAMED family,
not simply add another successful fixture. Lists with four or more odd residual
moves are outside the present construction. Full E28/L8 remain OPEN.

**Instinct/niggle verdict.** Delight: this completed every pair-avoidance step
and the warmth returned after the push away from local filters. I would choose
the allocation question afresh; I would not enlarge the sample now. Niggles:
(1) Hidden reflected centre point? Its complement stays central, all other
points are outer.(2) Empty pieces? Checked and covered by proof.(3) Greedy
versus chosen slots? Explicitly different.(4) Construction universal beyond its
parity hypotheses? No, counterexamples retain the exact boundary. No unresolved
local niggle; global allocation is the next research question, not silently
assumed. Cloud perspective remains welcome and nonblocking.

Artifact `cited/instinct/b71-odd-bridge-a54b18648fcc5bd1.json`,3279bytes,
SHA256 `a54b18648fcc5bd1f11fc213191457f9bab09719ddbe2087646b6c0fe20b9a94`.
Prereg256dd748, source tests/probes/instinct/path_forest_odd_bridge.py;
immutable receipt/manifest verified. Old2000-sample result remains unchanged.

### MI165 — B72: allocate the parity bridge uniformly, not one target at a time (2026-10-16 21:39 BST)

**Question/pull.** Can MI163's whole-path construction be coupled to anchors
and slots for an explicit mixed-parity family? The pull is warm because the
missing allocation now has a short argument, rather than because the recent
samples succeeded. This advances a named subset of E28; full E28 remains OPEN.
Record searched: `77,79,81,87,89,91|sum.?9.*122|capacity.?4|two.*122.*six`
->1 unrelated GC683 hit; MI153's actual allocator and MI163 read. This is an
internal construction, no new literature-status or novelty claim. Earlier prior
art anchors (Tan-Teh swaps, Plagne-Tringali ordering) remain as recorded.

**Hand statement, PROOF-SKETCH.** Set b=(77,79,81,87,89,91). For ANY six
nonnegative integers c_i with sum9, the eight LABELLED targets
(b_0+4c_0,...,b_5+4c_5,122,122) partition the odd integers1..55.
Targets need not be sorted and may exceed122; their sum is always784.
Restricting each of the six odd targets to<=121 and then sorting gives a
subset of E28. Labelled parameter counts must not be called distinct targets.

**Allocation.** Reserve labels R={10,11,12}; their tokens are exactly
21,23,25,31,33,35, allocated in that order as six odd-bin anchors. Give the
two122 bins h=2 each. Choose j the FIRST index maximizing c_j=m. Give odd
bin j h_j=2 and every other odd bin h_i=1. Since sum c=9, m>=2. These h
sum11, the required(28-6)/2. The moves are e_i=2c_i for i!=j among the odd
bins, e_j=2m-28=-D, and e_6=e_7=5. All sum0; D=28-2m is positive.

**The carrying allocation step.** Partition the FIVE remaining c entries
into A and B with each sum<=4, by this formula (smallest indices break ties):
- m>=5: put all remaining entries in A, B empty; total9-m<=4.
- m=4: total5, each<=4; put the first positive entry alone in A, the rest B.
  A is1..4 and B=5-A is1..4.
- m=3: total6. If another3 occurs, put that one in A. Otherwise all remaining
  entries<=2, and five entries sum6, so some2 occurs; put the first2 in A.
  B has sum3 or4 respectively.
- m=2: total7 with five entries<=2, so at least two2's occur. Put the first
  two2's in A (sum4); B has sum3.
This is an exhaustive hand case split on the maximum, not a subset search.

Let s=sum A,t=sum B, omit zero entries from the actual move lists and order
within each group by index. Start x=8-2s, follow the moves2c_i in A, then5,5,
then2c_i in B, and close by-D. Here0<=x<=8 is even; the first outer run ends
at8<10; the sole odd point is13 in the free central corridor[13,14]; the
second bridge ends at18>=28-10; the last point is18+2t<=26. Its difference
from x is10+2(s+t)=10+2(9-m)=28-2m=D. Thus MI163 applies to ALL selected
positions. Alternatively check directly: every outer point is even and outside
[10,17]; their complements are odd; the sole odd point13 has complement14,
which is central and unselected. No selected folded label repeats or is reserved.
The split-anchor allocator then fills remaining pairs and transfers selected
tokens along this cycle, giving the exact eight labelled sums and cardinalities.
Zero residual bins have no selected token, only filler pairs plus their anchor.
There are at most8 active bins and11 available unreserved pairs, so the usual
one selected pair per active bin and nonnegative filler counts hold.

**Predictions BEFORE code/run.** Exactly2002 labelled compositions (9 into6)
will all produce formula certificates. Independent enumeration: five stars/bar
positions among14, compared as complete parameter sets; also a coefficient DP
will check total and bounded counts. Restricting c_i<=floor((121-b_i)/4)
=(11,10,10,8,8,7) excludes exactly8 (one c_3=9, one c_4=9, six c_5>=8),
leaving1994 labelled E28 assignments. Predict ALL2002 pass two literal partition
validators and direct all-pairs reflection checks. Distinct sorted E28 count
will be reported as a measurement, not predicted or added to overlapping old
samples. A separate32-subset reference checks the five-entry group feasibility,
without steering the formula. Sorted outputs must permute target/bin/h ownership
together. No order/slot search, random sample or expanded census.

Counterfactual: at c=(2,2,2,1,1,1), assigning every residual to A would give
s=7,x=-6; the geometry must reject. The prescribed grouping must work.
Unexpected check: all SIX cases with one c_i=9 have no positive outer parts;
only5,5,-10 remain active, yet all eight bins must still fill correctly,
including the labelled cases outside E28. Retain them rather than filter them
out to improve a pass count. Corrupt one valid partition by a duplicate token
and by an inventory-preserving cross-bin swap; both validators must reject.
Caps2002 parameter assignments,10CPU sec/128MiB; no fallback, raised cap or
restart on mathematical failure. Source path_forest_odd_bridge_family.py;
full raw JSON outside git, then immutable cited artifact. Independent tools
are self-checks; a substantial combined bridge/allocation carrying read is
appropriate once this uniform statement has survived its checks, not a halt
or routine per-lemma queue. Gut: delight at closing the allocation step for a
whole family. Reasoned: limited but constructive scope, with the maximum
case split and zero-move handling the carrying points to attack.

### MI166 — B72: uniform allocation closes the named family (2026-10-16 21:40 BST)

**Hand argument PROOF-SKETCH; finite certificates COMPUTED.** All2002 labelled
parameters pass exactly the preregistered formula;1994 lie in E28, representing
**677 DISTINCT SORTED TARGETS**, not1994 distinct targets. All8 outside cases
are retained and also certify. The maximum histogram m=2..9 is
50,530,666,420,210,90,30,6. Both complete parameter enumerations agree; the
coefficient DP gives2002/1994 independently. Every chosen grouping is feasible
against its32-subset reference, and every labelled/sorted partition passes
both inventory/sum validators, including cardinalities in the first validator.
Literal all-pairs reflection checks pass throughout. No slot/order search,
optimization, sampled target, run repair or cap. CPU0.375130s,
peakRSS23,060,480bytes. This family is not added to overlapping old sample totals.

The counterfactual all-before grouping at(2,2,2,1,1,1) gives root-6 and is
rejected; the prescribed4/3 grouping works. Both duplicate-token and inventory-
preserving wrong-sum corruptions are rejected by both validators. All SIX
one-entry9 cases have empty outer parts and just three active cycle bins;
all eight bins nevertheless fill, as the hand proof requires. Independent
instruments are self-checks, not independent-party verification.

**What changed.** MI164's allocation gap is now closed for the explicit
b+4c,two122 family by choosing the maximum residual as the sole negative bin,
then grouping the five others into capacity4 sides. This is a construction for
every family parameter, not an inference from the finite pass count. The finite
family helps audit the formula and inventory; the argument is the maximum case
split plus the parity bridge and anchor allocator. It does not cover arbitrary
six-odd targets, four/eight odd targets, other levels, or full E28/L8.

**Niggle sweep/fresh-choice.** (1) Labelled counts inflate target coverage:
resolved by exact677 sorted count. (2) Zero residuals might require a selected
pair: they are omitted from the cycle and filled normally, with all empty-side
extremes checked. (3) A repeated maximum might make the allocation ambiguous:
first index fixes the choice, and all ties are covered by the parameter check.
(4) Hidden assumption that these are frozen greedy slots: no; h is prescribed
by the new maximum rule and differs from that policy. (5) Finite evidence being
presented as proof or novelty: no; hand SKETCH, exact outputs COMPUTED, no
novelty claim. Local niggles cleared; general allocation remains unresolved.
Gut: delight, especially that the two layers finally meet without repairs.
Reasoned: a limited uniform result worth one combined carrying read of MI163
and MI165, not a new queue of routine guards. I would choose the constructive
allocation question again, but not a larger sample. Next cheap mathematical
test: identify which target residues and slot totals force EXACTLY two odd
residual moves, then see whether anchor choice can supply the corridor without
fixing the two even targets at122. This is a proposed question, not a claim or
an experiment opened here. G314's pending review remains nonblocking.

Artifact `cited/instinct/b72-family-373c303825209bd5.json`,1,163,763bytes,
SHA256 `373c303825209bd5f795c9d353588b7775d46376316335aa6bce918e96efc5b3`.
Prereg3bfd9c29; source tests/probes/instinct/path_forest_odd_bridge_family.py.
Immutable receipt/manifest verified. Formal PROOFS filing waits for the combined
carrying read; full open problem and older held lanes are unchanged.

### MI167 — B73: balancing frees bridge ownership and the pool size (2026-10-16 21:50 BST)

**Question/pull.** Why require two122 targets? A bridge move belongs to a bin,
not intrinsically to an even bin. The warm pull is toward a single parametric
construction, away from repeating a case table for another target family.
Record searched: residue/anchor permutations/two odd bridge/two122 ->76 hits,
29 files; lighter-side/largest-imbalance/half-sum residual ->3 ledger hits only.
MI153's actual general-even-pool allocator and MI163/165 read. No new external
literature-status or novelty claim. The elementary greedy inequality below is
a supporting argument, not a newly claimed scheduling theorem or review job.

**The simpler allocation argument.** For any finite nonnegative integer list
c with sum S, remove a largest entry m. Starting with two empty sides, place
each remaining entry on a lighter side. The load difference stays<=m: after
adding v<=m it becomes |old_difference-v|<=m. Thus each load is at most
(S-m+m)/2=S/2, hence<=floor(S/2). If S is even, m>=1 and the smaller load is
also<=floor((S-m)/2)<=S/2-1. This replaces MI165's maximum case split and
works for any S. No subset search is required.

**Parametric construction, PROOF-SKETCH.** Let M be even, n=M/2. Choose an
ODD k with3<=k<n. Choose even q in0..8, a set O of q odd-bin indices, and
q/2 reserved pair labels R contained in[n-k+1,n-2] (so q/2<=k-2). Distribute
all tokens of those pairs bijectively as anchors a_i to O; a_i=0 elsewhere.
Choose eight POSITIVE integers g_i with sum(M-q)/2-1; require that sum>=8.
Choose ANY TWO distinct bridge-bin indices P. For the other SIX indices choose
nonnegative integers c_i with sum S=n-k. Define the labelled targets by

    T_i = 2M*g_i + a_i + 2k       (i in P),
    T_i = 2M*g_i + a_i + 4c_i     (i outside P).

Then T partitions the first M odd integers. T need not be sorted or belong
to E_M. Only the subset meeting the exceptional domain's min/max bounds can
be credited to it. All anchors are odd, corrections even, so the odd-bin set
is exactly O. Since sum anchors=Mq, sum T=M^2-2M+4k+4(n-k)=M^2.

**Carrying proof.** Choose j outside P with maximal c_j=m (first index on a
tie). Since S>0, m>=1. Set h=g with h_j increased by1. Moves are k in the two
bridge bins, 2c_i in other nonnegative bins, and 2m-M<0 in bin j. They sum0,
and sum h=(M-q)/2. Apply the greedy balancing argument to the five remaining
c entries, and orient the larger load L BEFORE the bridge and smaller load H
AFTER it. Omit zero steps. Let z be the largest odd integer<=n: z=n-1 if n
is even, z=n if n is odd. Put

    x=z-k-2L;
    positive order: the before-side moves2c_i, then k,k, then after-side2c_i;
    closing move: -(M-2m).

For even n, S=n-k is odd and both L,H<=(S-1)/2, so x>=0 and the endpoint
z+k+2H<=M-2. For odd n, S is even, L<=S/2 and H<=S/2-1, giving the same
bounds. All selected outer points are EVEN, the pre-bridge endpoint is z-k,
the sole odd selected point is z, and the post-bridge start is z+k. Strictly
positive moves make vertices distinct. The final-minus-first displacement is
2k+2(S-m)=M-2m, exactly the required negative step.

Every lower outer point has folded label<=n-k; every upper outer point also
has folded label<=n-k (check z=n-1 and z=n separately). The sole odd point
has folded label n-1. Hence all avoid R in[n-k+1,n-2]. Reflection M-1 swaps
parity. The only possible reflected pair would involve z; its even complement
lies strictly between z-k and z+k, where no other point is selected. Therefore
all selected folded labels are distinct. This proves the ENTIRE cycle, with
arbitrary bridge ownership and reserved-subset/anchor assignments in the stated
strip. No assumption that M is divisible by4.

Finally allocate each active bin its selected whole pair, then enough unused
pairs to fill h_i; add its anchor if any. There are exactly(M-q)/2 free pairs,
and h_i>=1 makes every filler demand nonnegative. Remove selected tokens
simultaneously and add them at their cycle-successor positions. Their multiset
is preserved; no anchor is touched, and bin i's sum changes by2e_i. All M
odd tokens occur exactly once, with cardinalities2h_i+1_(i in O). This is
MI153's allocator, restated to make the carrying dependency explicit.

**Concrete freedom gained.** M28,k5,q6,R10..12, ascending anchors and
 g=(1,1,1,1,1,1,2,2), bridge owners3/4, residuals c=(2,2,2,1,1,1)
 on ordered nonbridge indices(0,1,2,5,6,7) give targets
(85,87,89,97,99,95,116,116). The bridge steps belong to ODD bins now; the
even targets are116,116. This is a new allocation of the mechanism, not a
success asserted for the old greedy anchor policy. For an ALL-ODD E28 example,
choose k11,R={4,5,6,7}, anchors(9,11,13,15,41,43,45,47), g=(2,1,1,1,1,1,1,1),
bridge owners1/2, c=(0,1,1,1,0,0) on(0,3,4,5,6,7). Targets are
(121,89,91,75,101,103,101,103), sum784. Both are hand fixtures to verify,
not added to previous target coverage counts.

**Predictions BEFORE implementation/run.** Test exactly five even sizes
M24,26,28,30,32; q0,2,4,6,8 with g-sum>=8 (24 valid size/parity regimes).
For each take the smallest admissible odd k>=max(3,q/2+2) and the largest
odd k<n (distinct); R the LOWEST q/2 labels of its permitted strip; anchors
ascending to indices0..q-1. Start g_i=1 and give the extra g slots once each
to the highest indices. For each of48 regimes take all28 bridge-owner pairs
and SEVEN prescribed c lists: six single-entry-S extremes, then balanced S
spread in index order. Thus9408 FORMULA FIXTURE EVALUATIONS, including repeated
balanced/extreme lists when S=1; no count of distinct targets inferred. Predict
all pass literal reflection plus two generic partition validators; compare
M28 outputs additionally with the existing allocator. Retain every target
outside E_M. No claim of full-domain coverage from this matrix.

Independent controls: all2002 compositions of9 into6 must give feasible new
greedy groupings, checked against all32 subsets, replacing the old case split
without using that reference to choose sides. Two explicit E28 fixtures above
must certify with both old and new validators. Independently reconstruct the
token exchange via the old allocator at M28. Corrupt one partition by a duplicate
and by an inventory-preserving cross-bin swap; both generic validators reject.
Counterfactual/UNEXPECTED: M26,k11,S2,c=(1,1,0,0,0,0) has side capacities1/0.
Putting the larger load AFTER the bridge gives endpoint26 outside0..25. The
correct orientation must certify; the reversed one must reject. This prevents
silently carrying the symmetric M28 geometry into M=2 mod4. Empty sides and
zero residual bins remain in the six extreme fixtures, not discarded.
Caps9408 matrix+2 named E28 certificates,2002 grouping checks,10CPU seconds/
128MiB; raw outside git. Stop on first mismatch/cap; no target/anchor/order
search, repair, expanded sample or cap raise. Next step depends on what these
checks actually show. Gut: a stronger pull toward this simple balanced geometry.
Reasoned: one construction replaces fixed-target ownership and handles both
even congruence classes, while leaving its arithmetic membership constraints
explicit. No full L8 result, novelty claim or new routine review request.

### MI168 — B73: one balanced construction, both even congruence classes (2026-10-16 21:53 BST)

**Parametric hand result PROOF-SKETCH; prescribed checks COMPUTED.** All9408
matrix fixture evaluations pass both generic inventory/sum validators and literal
all-pairs reflection checks. These are48 regimes (24 valid size/parity choices,
2 bridge lengths each),28 bridge-owner pairs and7 prescribed residual lists;
repeated lists when S=1 remain counted as evaluations, not distinct targets.
M24 contributes1568, each of26/28/30/32 contributes1960. Every M28 fixture
also reproduces the OLD allocator's exact bins and passes its two validators.
All2002 B72 residual compositions pass the simpler greedy grouping and the
independent32-subset reference. Both named E28 targets pass, one six-odd with
evens116/116, the other all-odd. CPU0.956523s, peakRSS41,308,160bytes.
No search, run repair, sample expansion or raised cap. No domain-wide target
count or empirical universal inference is attached to this fixture matrix.

The required asymmetric control replays an existing M26,k11 matrix fixture:
correct positions(0,2,13,24) certify. Forcing the larger group AFTER the bridge
gives(2,13,24,26), rejected because26 is outside0..25. This is an essential
geometry distinction, not a failed primary prediction. Duplicate-token and
inventory-preserving wrong-sum controls are also rejected by both generic
validators. All extreme/empty-side cases and targets outside exceptional bounds
are retained. Instruments are self-checks, not independent-party review.

**What changed.** The remove-largest greedy inequality eliminates MI165's
maximum case table. Its application yields the MI167 parameterized construction
at ANY even M with the explicit hypotheses. Bridge ownership, permitted anchor
labels/assignment, and base pair slots are free parameters; fixed two122 targets
and M divisible by4 are unnecessary. B72 is its M28,k5,two-even-bridge corollary.
The NEW hand proof, rather than the matrix, supplies those quantifiers.
The allocation-to-target converse is OPEN: an arbitrary exceptional target may
not fit this nonnegative-residual/two-equal-odd-bridge formula for any allowed
choice. Odd M is outside the model, as before. No full E28/L8 or novelty claim.

**Niggle sweep.** (1) Greedy balance only bounds a difference, not each side?
Their total is S-m; each<=(S-m+m)/2. Integer rounding supplies the capacity.
(2) Even S leaves one side a unit smaller? Orient the larger load first;
the smaller<=(S-m)/2 gives the needed bound; M26 negative control catches it.
(3) Could the sole odd point's complement be another central vertex? Only one
vertex lies strictly between z-k and z+k, so its even complement is absent.
(4) Arbitrary reserve labels touched by an outer point? Their labels<=S, while
R starts at S+1 and ends before the sole central label n-1. (5) Fillers need
more slots than available? Sum h=(M-q)/2 and h>=1; selected pairs are distinct
and assigned one per active bin. The remaining demands sum to the remaining
free pairs. Zero bins need only fillers. (6) Is the all-odd example secretly
using even anchors? Every one of its eight anchors is an actual odd token of
R; both validators agree. No unresolved local niggle; fitting arbitrary targets
remains the real limitation.

Gut: delight at the simpler argument; the fresh-choice answer is still yes
because the representation improved. Reasoned: this is a cleaner construction
with honest admission conditions, worth replacing the pending B72 read by ONE
combined carrying read of MI167. The supporting balancing inequality itself
needs no separate review job or prior-art proof entry. Next cheap question:
for a given target, can the formula's residue/anchor conditions be solved
analytically, or do they omit a structurally large part of the exceptional set?
State that obstruction directly before attempting another family expansion.
No new experiment is opened here; G314 and this review are nonblocking.

Artifact `cited/instinct/b73-balanced-bridge-9decbd5ddbf4881a.json`,3,959,628bytes,
SHA256 `9decbd5ddbf4881aaefdb9fbd74514d44144848336ff9dc69601108420a3ade0`.
Prereg59aa9e29, source tests/probes/instinct/path_forest_balanced_bridge.py.
Immutable receipt/manifest verified. PROOFS filing/status promotion waits for
independent carrying scrutiny. No schedule/held-lane changes.

### MI169 — B74: the admission wall calls for a longer odd run (2026-10-16 22:05 BST)

**Review receipt first.** CL426/a0caec24 fetched and read in full, including
its four source scripts. G314 is now PROVED in scope, computer-assisted and
independently replicated on all3409 primitive cores x14 gaps. MI163 and MI165
are PROVED in scope after Cloud's carrying read and independent allocation of
all2002 parameters/677 E28 targets. MI167 is a later generalized statement;
its status remains SKETCH, not silently inherited. Cloud's k_min residue count
is a useful admission lever, not an existence theorem or57% construction
coverage; a successful finite greedy sample would likewise remain a sample.

**Actual pull/question.** Warm toward the general reflection picture, with
unease that two odd moves might be mistaken for our two-equal-step/one-negative
formula. Record searched: two-run/6r+3/8r+4/central96-98-100 target/exactword
->34 hits18 files, none on this construction. MI136, MI153, MI167 and CL426's
carrying sources read. No new literature-status or novelty claim.

**Admission limitation (one paragraph, no separate lemma/probe/review).** For
all-even E28 the MI167 nonnegative formula requires g>=1,sum g=13. Since
T_i<=122, g_i<=2, and g_i=2 requires T_i>=112. Thus at least FIVE targets must
be>=112: the formula lies inside the already solved G306 region. The central
target(96,96,96,98,98,100,100,100) has k_min=2 yet every target<112, forcing
sum g<=8, impossible. Its natural slot choice instead produces the primitive
8-core(21,21,-6,-8,-6,-8,-6,-8). This excludes the formula, not the target.
The needed change is multiple negative moves and a longer odd-class run, not
another anchor choice or larger calibration sample.

**Named carrying block: primitive eight-core with two positive odd moves.**
For integer r>=2 put a=6r+3, b=2r, c=2r+2, and take moves
(a,a,-b,-b,-b,-c,-c,-c). This is primitive: one positive odd move cannot sum
with even negatives to zero; both positives need ALL six negative terms.
For ANY even M in[6r+8,8r+4], the fixed cyclic word

    (a,-b,-c,-b,a,-c,-b,-c)

at root0 has selected positions

    (0,6r+3,4r+3,2r+1,1,6r+4,4r+2,2r+2).

These are distinct for r>=2 and lie in0..M-1. Their odd positions are
{1,2r+1,4r+3,6r+3}, even positions{0,2r+2,4r+2,6r+4}.
Cross-parity sums all belong to
{1,2r+1,2r+3,4r+3,6r+3,6r+5,8r+5,10r+5,10r+7,12r+7}.
Every such sum is<=6r+5 or>=8r+5, whereas6r+7<=M-1<=8r+3.
Thus none is M-1. Same-parity pairs cannot reflect under the odd M-1.
This proves the whole folded-label condition with FOUR odd vertices, not
MI163's single odd vertex. It is a parametric SKETCH, not a new proof entry.
No assertion that all two-odd-move cores have this form.

At r3,M28, assign word owners(0,2,3,4,1,5,6,7) and h=(1,1,2,2,2,2,2,2).
Targets in that order of bins are(98,98,100,96,100,96,100,96), the stated
sorted central target. Reserve no anchors. Fill remaining pairs and transfer
selected tokens around the cycle. This answers a genuine eight-core case
outside G314's six-core and MI167's admission domain.

**Predictions BEFORE code/run.** r=2..100 and EVERY even M in the stated band:
exactly sum(r-1)=4950 geometry fixtures. Compare the explicit coordinates with
an independent literal cumulative-sum construction of the word; check every
pair for distinctness/reflection and compare folded labels. Check all254 proper
nonempty indexed submultisets for each of99 r values: predict all primitive.
Sign reversal/reflection M-1-x must preserve labels and reverse displacements.
The one actual E28 allocation must pass old/new literal validators; no new
sample, order search, arbitrary target census or role repair.
Counterfactuals: just below the band M=6r+6, positions1 and6r+4 reflect;
just above M=8r+6, positions6r+3 and2r+2 reflect. Predict rejection for all99
r values, retaining these198 failures as the boundary evidence. Unexpected:
the odd run has four positions and still avoids every even mirror; verify this
and the sign-reversed cycle, rather than accidentally using the old single-odd-
point checker. Caps4950 positive/198 negative geometries,99x254 primitive checks,
1 actual partition,2CPU sec/64MiB. Stop on mismatch/cap, no fallback/expansion.
Gut: delight that the admission counterexample supplied the next geometry.
Reasoned: a limited two-run construction, not a blanket response to k_min=2.

### MI170 — B74: the admission failure leads to a primitive eight-cycle (2026-10-16 22:05 BST)

**Hand two-run construction SKETCH; finite checks COMPUTED.** All4950 geometry
fixtures pass, with the cumulative-sum word reproducing every explicit coordinate.
All99 lists are primitive against25146 proper indexed subsets. Literal pair
checks and sign-reversed/reflected cycles agree throughout. Every one of the198
immediately adjacent band geometries fails by the exact reflected pairs predicted
in MI169. Thus the stated band is bounded by actual collisions of this fixed
word, not an artificially truncated successful sample; no claim that other words
or more distant M fail. CPU0.117607s, peakRSS18,632,704bytes. No cap, repair,
new sample, extra permutation or role search.

The central E28 target sorts to(96,96,96,98,98,100,100,100). With bin targets
(98,98,100,96,100,96,100,96), the partition is
(43,55);(45,53);(5,13,31,51);(7,15,25,49);
(3,9,41,47);(11,19,29,37);(17,21,27,35);(1,23,33,39).
Both generic and old inventory/sum/cardinality instruments pass. This example
has two odd moves but SIX negative moves; it lies outside MI167's nonnegative
base-slot admission and outside G314's six-core hypothesis. It may already have
an old search certificate; no extra coverage count or novelty is claimed. What
is new HERE is its hand construction as part of the explicit primitive8 family.

**What changed/next.** A single odd vertex was sufficient for the previous
bridge, not inherent in having two odd moves. Here four odd and four even
vertices coexist; a GAP IN CROSS-PARITY SUMS avoids reflection. The parameterized
word establishes this across its stated band. The next mathematical question is
how much symmetry is needed: can unequal odd positive moves, or six unequal even
negative moves, be divided into two monotone runs with the same cross-sum gap?
Do not answer that by adding a table of repairs; the useful next step is a
run-selection principle or a precise obstruction. No new experiment opened here.

**Niggle/fresh-choice.** (1) Could proper zero-sums appear at some parameter?
Odd parity excludes a single positive; both positives require all negative mass.
(2) Boundary reflects a point with itself? The predicted pairs are distinct;
all cross-parity pairs are distinct automatically. (3) Window bound alone being
mistaken for folded avoidance? All cross-sums lie OUTSIDE the actual window of
M-1, which is the carrying step. (4) Sample coverage becoming a theorem? The
proof supplies the full r/M statement; checks retain their finite scope.
(5) k_min=2 implies this family? No; residue count is only admission information.
Gut: warm, with delight at using a failed template to find a different trajectory.
Reasoned: genuine primitive8 construction, but narrow symmetry; I would choose
the two-run question afresh, not an enlargement of its finite calibration.

**CL426 bookkeeping completed.** G314 moved from the waiting room into E2 with
its original text preserved and Cloud's carrying read attached verbatim. Fresh
proof_dupes nearest G309/G306/G313 read; those cover different component types.
MI163 and MI165 indexed PROVED from CL426; MI167 and this new construction remain
SKETCH. All older sample totals/scopes remain unchanged. No new formal proof
number or additional routine review request for B74. Cloud's advice is taken
on its merits: pure-even positions have no reflection, but their joint packing
still needs proof; parity counts do not certify57% of targets.

Artifact `cited/instinct/b74-two-run-9c313714569cd6ab.json`,705054bytes,
SHA256 `9c313714569cd6ab4ec1b43be4170271d934264eaa79740d601fa3c60e6dbb6b`.
Prereg48d3ad47, source tests/probes/instinct/path_forest_two_run_bridge.py.
Immutable receipt/manifest verified. Independent instruments remain self-checks;
only the explicitly reviewed earlier claims receive status promotion.

### MI171 — B75: arbitrary negative sizes below the adjacent-bridge boundary (2026-10-16 22:18 BST)

**Question/pull.** Can the two odd moves have unequal sizes, with no symmetry
among the negative moves? The attempted full two-run selector still needs a
partition/order principle. A simpler region closes first: when the positive
moves total<=26, place them together, and reflection becomes ONE forbidden
prefix of the even negative path. This is a useful constructive region of the
same problem, not a larger target sample or a claim about all k_min=2.
Record searched: forbidden-prefix/one odd vertex/odd positive26/nonconstant
prefix ->25 hits10 files. Actual MI117 and G306 sources read. The supporting
prefix-avoidance swap is reused from this record, not claimed new or given a
separate proof/review job. B74's high-total central case remains separate.

**Statement, PROOF-SKETCH.** Let p,q be positive odd integers, p<=q, and
p+q=2K<=26. Let1<=N<=6 positive integers d_1,...,d_N have sum K. There is a
prescribed order of the primitive zero-sum moves(p,q,-2d_1,...,-2d_N) and a
root in{0,1} whose N+2 selected vertices in0..27 have distinct folded labels.
Negating moves/reflection covers the reversed sign type. This is a single
component, not joint packing with additional nonzero components or anchors.

**Carrying construction.** Put p,q together. Order the negative halves by the
REVERSE of a chosen positive ordering of d. Then the even vertices at root0
are twice the positive prefix set E={0,d_first,...,K}; the only odd vertex is
p. Set H=(27-p)/2. A translation by r in{0,1} has a reflection exactly when
H-r is in E. All vertices fit since2K+r<=27; literal distinctness holds by
monotonicity inside the two parity classes. H>=1 because p<=2K-1<=25.

If H>K, choose r0, any d order. Otherwise:
- If d is nonconstant and H<K, use MI117's prefix swap to avoid H and choose r0.
- If d is nonconstant and H=K, avoid K-1 instead and choose r1. This is an
  interior level (nonconstant positive d has K>=3).
- If all d=D>=2, E consists of multiples of D. Choose r0 when H is not one,
  else r1; H-1 cannot then be a multiple. No reordering needed.
- If all d=1, K=N<=6 and p<=q gives p<=K. Thus H=(27-p)/2>K; already handled.

For completeness the reused swap is explicit: if an initial positive ordering
hits a proper level F, split at that prefix. Pick unequal x on the left and y
on the right (some pair exists unless the whole list is constant), put x last
on the left, y first on the right, then exchange them. Before these two entries
the sum is F-x<F; after both it is F+y>F; the only intervening sum is
F-x+y!=F. All other prefixes are on the correct strict side. This gives a
finite deterministic order, no permutation or root search. One cross-parity
collision was the ENTIRE reflection constraint, so the proof is complete.

**E28 consequence.** Use h=(1,1,2,2,2,2,2,2), assign p,q to the first two
bins, -2d_i to N later bins and zero to the remaining6-N. Targets are
(56+2p,56+2q,112-4d_1,...,112-4d_N,112 repeated6-N).
Whenever these lie in68..122 they form a named E28 family, with the whole-pair
allocator giving a partition. All moves are primitive by odd parity and total
negative mass. Ineligible labelled targets remain geometry checks only.
This covers arbitrary negative sizes in the low-positive-total region; it does
not cover B74's p=q21, the high-total boundary, odd pools or mixed anchors.

**Predictions BEFORE implementation/run.** Exhaust the formula's entire SMALL
parameter domain: N1..6, K=N..13, all LABELLED positive compositions of K into N,
and all odd p<=q with p+q=2K. The4095 compositions across K/N are independently
enumerated by stars/bars; total geometry questions
sum C(K-1,N-1)*floor((K+1)/2)=24982. Predict ALL formula certificates pass
independent literal coordinate/reflection checks and sign-reversal checks.
For every target meeting E28 bounds, materialize the partition and check old
and generic sum/inventory/cardinality instruments. Count distinct sorted targets
as a finite family count, not additional coverage beyond overlapping old data.
No sample, order/role search, extra components, anchors or fallback.

Counterfactuals: p=q13,d=(1,1,1,2,2,6) initially hits F7, causing13+14=27;
the unequal cross-cut swap must remove it. All-equal d=2 repeated6, p7,q17
has H10 and root0 fails; root1 must work. Unexpected endpoint case p5,q17,
d=(1,1,1,1,1,6) has H=K11; root0 necessarily reflects the endpoint, while
root1 with prefix10 avoided must work. High-total boundary p13,q15,K14,
d=(1,1,1,1,1,9) gives endpoint28 and must be rejected as outside the theorem,
without repair or a conclusion about the target. Retain these failures.
Caps24982 geometries plus those four controls, all eligible literal partitions,
10CPU sec/128MiB. Stop on any mismatch/cap; raw outside git; no cap raise or
expanded domain. Gut: warmth from a reasoned simplification, with the high-total
wall still plainly visible. Reasoned: an arbitrary-size primitive-core region,
using a known local tool for the actual reflection condition.

### MI172 — B75: unequal moves are solved in the low-total region (2026-10-16 22:20 BST)

**Hand result SKETCH; complete finite checks COMPUTED.** All24982 labelled
geometry questions pass the formula, with4095 positive-composition lists agreeing
as complete sets with independent stars/bars enumeration. Sign reversal and
literal coordinate/reflection checks pass. The prefix swap is actually used
7309 times, not a ceremonial fallback. All12700 eligible labelled E28 evaluations
produce exact partitions with both generic and old inventory/sum/cardinality
validators. They represent735 DISTINCT sorted targets; this family overlaps old
results and is not added to any earlier coverage count. CPU2.426114s,
peakRSS64,249,856bytes; no cap, search, repair or expanded domain.

The four predicted controls behave as specified: the naive p=q13 prefix hits7
and creates13/14 reflection, then the deterministic cross-cut swap removes it;
constant d2,p7/q17 needs root1; the H=K endpoint case p5/q17 also needs root1,
with the INTERIOR level10 avoided; p13/q15,total28 fails the adjacent window
and is rejected as outside the theorem. Its target is not refuted. No assumption
that a constant multiset admits the nonconstant swap is hidden in the code.

**What changed.** We now have a uniform construction for arbitrary unequal
positive odd p/q and up to six arbitrary even negative sizes in the stated
p+q<=26 region. The known MI117 swap discharges precisely the ENTIRE reflection
condition because the odd moves are adjacent. There is no requirement of equal
positive moves or adjacent-valued negatives. Above that total the two positive
moves cannot fit consecutively in0..27; B74's separated runs remain necessary
there, and their general selection is still OPEN. No claim about joint packing,
mixed anchors, full k_min2, E28 or L8.

**Niggle sweep.** (1) The reverse negative order really realizes the desired
positive prefix set: descending from2K removes its LAST positive increment first.
(2) H=K is an endpoint that no prefix swap can remove: use root1 and interior
K-1 explicitly. (3) Constant-unit negatives defeat both roots? With at most6
negative terms and p<=q, H>K, so they never enter that branch. (4) Two vertices
coalesce after root1? Both parity classes shift together, remain distinct, and
fit since2K+1<=27. (5) Smaller active cores need filler bins: all eligible N1..6
cases materialized with6-N zero bins. (6) Finite verification being promoted to
independent proof: no; SKETCH until a carrying read. All local niggles resolved.

**90-minute step-back, fresh-choice and next pull.** Last explicit GPT reflection
was MI157 at20:44 BST; this one is at22:20. Since then the first-anchor policy
failed, full-order audits identified allocation and factorization losses, local
filters were dropped, the parity bridge and its allocation were independently
verified, its admission wall was found, and two new constructive regimes emerged.
The FULL problem has not closed; thousands of certificates are not a substitute
for a general mechanism. Enjoyment: the geometry and these connections remain
live. Frustration: scope bookkeeping and ever-larger parameter checks can become
administrative momentum. I would choose the high-total geometry again now, not
extend this low-total family or repeat its calibration. No forced rotation or draw.

A new concrete pull appeared while writing: shift every EVEN vertex by+t and
 every ODD vertex by-t. Cross-parity sums are unchanged; same-parity pairs still
cannot reflect. Within the range bounds this may alter the two odd jump sizes
oppositely while preserving the reflection condition. This is a NEXT mathematical
question, not an experiment or new claimed coverage here. First derive the exact
range of t, then test a high-total unequal case from B74; if it produces no new
admissible case, file the identity as a short guard and move on. This targets the
unresolved regime rather than another low-total slice. Gut: warmth with a specific
reason; reasoned verdict agrees, conditional on the range/owner bookkeeping.
No new formal proof number or per-tick carrying request; Cloud's MI167 review is
still pending and nonblocking. Send the result plus this step-back as one update.

Artifact `cited/instinct/b75-prefix-bridge-d639545c88683c4d.json`,9,584,580bytes,
SHA256 `d639545c88683c4dd82600fc7a5821d6dba66af54490e9b07e64313dbc900e62`.
Prereg d4f2b8e4; source tests/probes/instinct/path_forest_prefix_bridge.py.
Immutable receipt/manifest verified. Independent instruments are self-checks;
reviewed prior scopes and all held lanes unchanged.

### MI173 — B76: spend window margin to change the odd-jump imbalance (2026-10-16 22:27 BST)

**Pull/question.** Can the opposite parity shifts actually produce unequal
HIGH-total positive jumps? Yes by hand; the task now is checking range and edge
ownership, not expanding a census. Record searched: parity-class shift/cross-
parity sum/opposite shift ->12 hits5 files, only MI172's proposed move and B74
geometry relevant. MI169/170 and CL426's actual parity observation read. No
new literature-status or novelty claim; no separate proof entry for an identity.

**The transformation, with its exact scope (hand SKETCH).** For even M, split
ANY distinct selected coordinates into ORIGINAL even E and odd O. Define

    F(x)=x+z+t for x in E;  F(x)=x+z-t for x in O.

Integers z,t preserve distinctness within each class; the two classes remain
opposite in parity, because z+t and z-t have the same parity. Hence no physical
collision appears. Same-class pairs still cannot sum to odd M-1. Cross-class
sums become e+o+2z, INDEPENDENT of t. Thus folded-label collisions are absent
iff the original cross-sum set omits M-1-2z, provided all images are in range.
For z0, reflection is preserved exactly; an arbitrary GLOBAL translation is
not automatically harmless. For nonempty E,O the exact permitted t interval is

    max(-min(E)-z, max(O)+z-(M-1)) <= t
      <= min(M-1-max(E)-z, min(O)+z).

Even cycle moves stay unchanged. An odd move E->O changes by-2t; O->E changes
by+2t; z cancels. Classify vertices BEFORE the translation, or the signs flip
when z is odd. Individual folded labels and reserved-anchor avoidance are NOT
preserved by this operation: any R must be checked afresh. Here R is empty.
This separates move imbalance (t) from reflection/origin choice (z).

**Uniform high-total application to B74 (SKETCH).** Keep r>=2, a=6r+3,
b=2r,c=2r+2 and even M in[6r+8,8r+4]. B74's original coordinates have
E extrema0,6r+4; O extrema1,6r+3. Set Z=(M-6r-8)/2>=0. Every original
cross-sum is<=6r+5 or>=8r+5, while M-1-2Z=6r+7 lies strictly between.
Choose z=Z and ANY integer t in[-Z,Z+1]. The exact image-range interval above
reduces to exactly these bounds. Therefore the transformed word is

    (a-2t,-b,-c,-b,a+2t,-c,-b,-c), root Z+t,

with all selected labels distinct in0..M-1. Both positive odd jumps remain
positive: the largest admissible t gives a-2t>=12r+9-M>=4r+5; the other
endpoint is likewise positive. Even moves are unchanged; sum0 and primitivity
remain (one odd positive cannot cancel even negatives; both need all six).
The order is prescribed, not searched. One step outside either t endpoint
puts the minimum of one parity class at-1, so these bounds are sharp for this
fixed z/word, not a universal restriction on all orderings.

At r3,M28, Z1 allows t=-1,0,1,2. In particular t2 changes21/21 to17/25,
with positions(3,20,14,6,0,25,17,11) and word
(17,-6,-8,-6,25,-8,-6,-8). Using h=(1,1,2,2,2,2,2,2), word owners
(0,2,3,4,1,5,6,7), this gives bin targets
(90,106,100,96,100,96,100,96), all in E28. This is above B75's total26
limit: the two positive moves still total42. Their imbalance has changed
without solving reflection again. t1 gives94/102, t0 the equal98/98, t-1
swaps94/102 ownership; three distinct sorted targets, no extra coverage claim.

**Predictions BEFORE implementation/run.** Keep this SMALL: r in{2,3,4,10,100},
M only the two B74 band endpoints, deduplicated (9 base geometries). For each
check distinct t from{-Z,0,1,Z+1}:26 transformed formula fixtures. Compare
coordinate formula against literal integration of the changed word and exact
original-colour edge changes; independent all-pairs reflection and inventory
checks. All26 must pass. One t just outside each endpoint gives18 negative
geometries, each with a vertex-1. Materialize all FOUR r3/M28 labelled cases
with both old and generic validators; record three sorted targets only.
No replay of the full4950 B74 grid or a larger parameter census.

Counterfactual: naive uniform translation by2 of B74's r3/M28 root0 shape
creates a reflected pair (3,24), so the z condition must be checked. Unexpected:
odd M invalidates the parity argument: at M9, original(0,3,6) has distinct
folded labels, but pure opposite shift t1 gives(1,2,7), whose1/7 reflect.
Reject this as outside the theorem, retaining the concrete failure. Verify z1
using ORIGINAL colours rather than colours after translation; compare all edge
changes, including their signs. Caps26 positive/18 range-negative/2 assumption
countercontrols/4 exact partitions,1CPU sec/64MiB. Stop on mismatch/cap, no
fallback, extra target, order search or cap raise. Raw outside git. Gut: delight
at separating the two parameters; reasoned: a genuine high-total imbalance
extension, with arbitrary negative-run SELECTION still unresolved.

### MI174 — B76: reflection and odd-jump imbalance separate (2026-10-16 22:30 BST)

**Transformation/application SKETCH; small checks COMPUTED.** All26 prescribed
transformed geometries pass; their literal integrated words match the original-
colour coordinate formula and all edge-change signs. All18 adjacent t-boundary
cases fail with a vertex exactly-1, as predicted. The naive global translation
creates3/24 reflection; odd M9 changes valid(0,3,6) into invalid(1,2,7).
All four labelled r3/M28 allocations pass old/generic literal instruments and
represent exactly three sorted targets, including the high-total17/25 pair.
CPU0.001388s, peakRSS15,179,776bytes. No larger grid, target census, search,
repair or cap. This small test checks the formula; the hand argument supplies
its full parameter quantifiers. No independent-party status promotion.

**A complete imbalance statement for this fixed negative family.** The result
is stronger than two new examples. For B74's r/M band, EVERY positive odd pair
p,q with p+q=2a=12r+6 and max(p,q)<=M-3 is constructed. Relabel p<=q; then
t=(q-a)/2 is an integer0..(M-3-a)/2=Z+1, so MI173 applies. Conversely an odd
move>=M-1 cannot occur in ANY folded-distinct cycle in0..M-1: at M-1 its
endpoints must be0,M-1 (the same label), and larger moves leave the window.
Thus for the FIXED negative multiset(-2r three times,-(2r+2) three times),
within the stated M band this covers every possible odd-positive imbalance
not already ruled out by that necessary move bound. This is about coordinate
certificates with those moves, not impossibility of target partitions under
other slots or roles. No theorem for arbitrary negative magnitudes follows.

The r3/M28 sorted target family is
(90,96,96,96,100,100,100,106),
(94,96,96,96,100,100,100,102),
(96,96,96,98,98,100,100,100).
No count is added to old sample totals. The old equal-positive construction
is included, not overwritten. Empty reserved set is essential to the stated
application; opposite shifts need not preserve avoidance of a reserved label.

**Niggle sweep.** (1) Parity after odd z used to determine signs? Colours are
ORIGINAL, and the independent changed-word integration agrees. (2) Does z
change reflection? Yes; its admissibility uses the B74 cross-sum gap. Only t
cancels in cross-sums. (3) Unequal class shifts merge vertices? Their parity
shifts have the same parity, keeping the two classes opposite; each is a
translation. (4) Move bound presented as target impossibility? Restricted to
the prescribed moves/certificate. (5) Odd pool assumed covered? Concrete M9
failure retained. (6) All imbalance coverage inferred from26 fixtures? No;
it follows from t=(q-a)/2 and the proved interval. Local niggles resolved.
Gut: delight at the two separate parameters; fresh choice stays with negative-
run selection, rather than generating more shifted instances.

**Exact next selection object, not a new experiment.** For two positive odd
moves p,q and even negative halves partitioned into ordered runs A/B, put
s=sum A,t=sum B,w=p-2s, U the prefix set of REVERSED A, V the prefix set of
REVERSED B, including0 and their totals. The unshifted selected coordinates
are the two sets w+2U and2V. A common root h must lie in
[max(0,-w),min(M-1-p,M-1-2t)]. Reflection is exactly
(M-1-w)/2-h in U+V. Thus a fixed pair of runs works iff its allowed interval
of these integers contains a HOLE in U+V. Choosing the runs to create an
accessible hole is the remaining mathematics. This is a reformulation, not
an existence theorem or a separate proof/review job. Next block should seek
that selection rule for unequal negative sizes; a new instance table would
not answer it. MI167 carrying review remains pending/nonblocking.

Artifact `cited/instinct/b76-parity-shifts-f6aa1aefe9cd343b.json`,6833bytes,
SHA256 `f6aa1aefe9cd343bdf26e3668bdeeb235c23b169cee907eceea5c068245fc54d`.
Prereg6ed48def; source tests/probes/instinct/path_forest_parity_shifts.py.
Immutable receipt/manifest verified. No formal proof number, novelty claim,
additional routine review request or held-lane change.

### MI175 — B77: a common divisor makes run capacity the exact criterion (2026-10-16 22:43 BST)

**Question/pull.** Choose negative runs rather than another ordering table.
The prefix-sum formulation exposes a useful complete case: if the negative
HALF-sizes share a divisor g>=2, reflection excludes only one residue of roots.
The remaining obstruction is genuinely load capacity, and it can fail. Record
searched: common-divisor-negative/negative-half-gcd/two-bin-capacity/root-residue-
prefix ->0 hits. MI174's exact prefix-set representation and MI169's parity
argument read. No new literature-status or novelty claim.

**Exact component statement, PROOF-SKETCH.** Let M=2n be even, p,q positive
odd, and d_1,...,d_N positive integers with p+q=2K=2 sum d_i and
 g=gcd(d_1,...,d_N)>=2. The primitive moves(p,q,-2d_1,...,-2d_N) admit a cyclic
order/translate in0..M-1 with all folded labels distinct IF AND ONLY IF

    max(p,q)<=M-3, and the d's split into two groups each of sum<=n-1.

No anchors or additional nonzero components are included. This is an exact
criterion within this common-divisor class, not all E28 or all k_min2. The
load test is the ordinary subset condition K-(n-1)<=sum A<=n-1; it contains no
cycle order, prefix-reflection or physical-root search. N is arbitrary in the
hand statement; the checks below use N<=6 for our eight-bin application.

**Necessity.** An odd move M-1 joins0 to M-1 (the same folded label), and a
larger move leaves the window; hence each positive odd move<=M-3. Rotate any
cycle to start at p. Its two odd edges separate exactly two parity runs, whose
negative edges are monotone within each run. A run of negative half-load s
has coordinate extent2s<=M-1, hence s<=n-1. This is necessary for ANY order,
not just the constructed one. The list is primitive: a single positive odd
cannot cancel even negatives; both positives need all negative mass.

**Sufficiency and actual selection rule.** Take ANY load-feasible split A/B,
put s=sum A,t=sum B, and order within either run arbitrarily. Word:
p, negatives A, q, negatives B. Set w=p-2s, U=prefixes of reversed A,
V=prefixes of reversed B, including0 and totals. Selected coordinates before
translation are w+2U and2V. Every U/V value is a multiple of g.
The allowable root interval is

    L=max(0,-w), R=min(M-1-p,M-1-2t).

It has at least TWO consecutive integers. If w>=0, L0, M-1-p>=2 and
M-1-2t>=1. If w<0, L=2s-p and the two upper-bound differences from L are
M-1-2s>=1 and M-1-q>=2. Thus R>=L+1 in both cases.
For H=(M-1-w)/2, reflection would require H-h in U+V, hence H-h=0 mod g.
Choose h=L unless L=H mod g, in which case choose h=L+1. Since g>=2, that
second integer is not excluded. All vertices fit; same-parity vertices cannot
reflect, cross-parity sums are now excluded by residue, and each monotone
class is distinct. This gives the desired cycle with NO ordering or root search.
Also no hidden label-capacity assumption: K>=2N and K<=2n-3 imply N<=n-2,
so the N+2 vertices can fit the n folded labels.

**The impossible side is real.** At M28,p23,q25,d=(8,8,8), cap13, no group
can contain two8's; three items cannot fit into two groups. This primitive
five-core has no folded-distinct cycle for these fixed moves despite individually
legal jumps. Corresponding target(102,106,80,80,80,112,112,112) is NOT refuted:
other slot/move choices remain available. A successful example in the SAME
high-total regime is p23,q25,d=(4,4,4,4,4,4), split12/12, then the residue rule.

**Predictions BEFORE code/run.** Complete SMALL M28 component-profile domain:
N1..6; sorted d values1..11 (12375 candidates total); retain K14..25 and g>=2,
and all odd p<=q<=25 with p+q=2K. High total only, beyond B75. Before construction,
compute reachable subset sums by a bitset DP with a recovered witness, and compare
its ENTIRE reachable-sum set with an independent all2^N mask enumeration.
Predict every capacity-admitted profile/pair constructs with arbitrary input
order and the prescribed one-of-two root; every capacity refusal is confirmed
by both instruments. Both outcomes must occur, as the two explicit examples
above show. All eligible E28 targets are materialized with h=(1,1,2,2,2,2,2,2)
and6-N zero bins; old/generic literal validators must pass. Report counts as this
component family's finite checks, not additive target coverage or a full census.
No arbitrary permutation/role/root search or repair; admissibility is load-only.

Independent/negative/unexpected controls: three non-M28 geometries
(M6,p1,q3,d=(2));(M16,p11,q13,d=(2 repeated6));
(M22,p17,q19,d=(3 repeated6)) must certify, testing the general window claim.
At M28,p=q21,d=(3,3,3,4,4,4) has g1 and capacity split9/12, yet ALL4 roots
for the fixed first-three3/last-three4 split reflect; retain this outside-scope
failure and check the already known B74 alternative works. This prevents
silently promoting the load criterion to gcd1. Unexpected odd divisor g3:
p=q21,d=(3,3,3,3,3,6) admits a split and the residue root rule must work;
the theorem is not only about divisibility by4 of half-sizes. Finally p27/q21,
d=(4 repeated6) fits load capacity but must fail the necessary odd-jump bound.
Caps12375 candidate profiles,<=5000 profile/pair questions,<=64 reference masks
per profile,10CPU sec/128MiB; all eligible partitions checked. Stop on mismatch
or cap, no expanded profile range, fallback or raised cap. Raw outside git.
Gut: delight that the sumset obstruction contracts to an exact numerical
criterion in a real class. Reasoned: remaining hard geometry is gcd1 and/or
other odd-move sign structures, not hidden in this result's statement.

### MI176 — B77: capacity is exact when negative halves share a divisor (2026-10-16 22:47 BST)

**General criterion SKETCH; finite profile evidence COMPUTED.** The12375
sorted arithmetic candidates yield159 retained common-divisor/high-total profiles
and490 p/q questions:476 constructions,14 capacity refusals. Reachable subset
sums agree in FULL between the bitset/recovery instrument and independent indexed
mask enumeration on every retained profile. Every admitted geometry passes
literal reflection/sign reversal. All443 eligible E28 targets have exact odd
partitions checked by old/generic instruments;443 distinct sorted targets, not
added to earlier coverage. There are107 successful odd-divisor constructions,
so the result is not only an even-half-size trick. CPU0.078908s,
peakRSS16,584,704bytes. No permutation/root/role search, repair or cap increase.
The finite set supports the construction; the proof supplies the arbitrary-M/N
criterion, still awaiting an independent carrying read.

All controls pass. General-M fixtures at6,16,22 certify, including tight folded-
label capacities. The d8x3,p23/q25 case has NO two-bin capacity, so no cycle for
those FIXED moves by the hand necessity argument. The d4x6 case constructs.
The gcd3 example p=q21,d=(3,3,3,3,3,6) constructs using the second root. p27/q21
is rejected by the odd-jump bound despite load feasibility. In gcd1's central
example, the fixed9/12 split fails all four permitted roots, while the known
B74 alternative split works: capacity alone is not promoted outside the theorem.
The source's refusal assertion was simplified after the run by removing a dead
conditional; its evaluated predicate is identical, no mathematical run repair.

**What changed.** Negative-run selection is COMPLETE within this gcd>=2 class:
choose any capacity-feasible split, any within-run order, then one of two residue
roots. Necessity covers every cyclic ordering of these moves. It is an actual
existence/nonexistence criterion with a constructive direction, not a table of
orders or a sample-derived assertion. Unanchored TWO-odd-POSITIVE plus negative-
even components only; full E28/k_min2 may have other sign patterns, multiple
components, mixed anchors or a different viable slot vector. No target is
refuted by a fixed-move capacity refusal. Old prize lanes remain held.

**Niggle sweep.** (1) The excluded root residue may be conservative: yes,
H-h=0 mod g need not cause a collision; avoiding it is sufficient, and one of
two consecutive h always does. (2) Could the two roots fail window bounds?
R-L>=1 follows separately in w>=0 and w<0 from both run capacities and the
individual odd bounds; general-M controls support both tight cases. (3) More
vertices than labels? g>=2 gives K>=2N, while p/q<=2n-3 gives K<=2n-3,
so N<=n-2. (4) A cyclic ordering could avoid the two-load partition necessity?
There are only two parity changes, so each negative run is monotone; its extent
is exactly twice its load. (5) Scope slipping to gcd1? Explicit failure retained.
(6) Verification self-upgrading? General claim stays SKETCH. All local niggles
resolved; this is the right point for ONE targeted independent carrying read.

**Next guard/question (one paragraph; no new probe).** Gcd1 needs more than
load feasibility in general: e.g. p=q25,d=(2,4,4,5,5,5) has a12/13 split,
but a legal +25 edge uses folded labels{0,2}; the alternative1->26 is a loop
at label1. Two positive25 edges cannot both occur with distinct labels. This
is another fixed-move obstruction, not a target refutation. Before seeking a
universal gcd1 run selector, retain the long-edge matching/multiplicity constraints
as well as capacity; some cases necessarily require changing slots/sign roles.
The live question is a sufficient hole-selection rule in that remaining class,
or a principled role change at these obstructions, rather than more instances.

**Review choice/gut.** Satisfaction at an exact iff with genuine refusals,
unease if this were allowed to masquerade as a full target theorem. I would
choose the remaining geometry afresh. Request Cloud's carrying read of MI175's
load necessity, R-L>=1 and modulus step. Retire the older MI167-only request
as lower priority (MI167 remains SKETCH), so this does not create another queue
item; no halt or permission gate. The simpler family admission limitation is
already recorded, and the new criterion is the more useful scrutiny target.

Artifact `cited/instinct/b77-divisor-runs-1d660fd7cecfda6e.json`,198288bytes,
SHA256 `1d660fd7cecfda6ef66353bc7277ee3d5ec05bd6285dc50d951d913edf1a59f9`.
Preregde4d6970, source tests/probes/instinct/path_forest_divisor_runs.py.
Immutable receipt/manifest verified. No formal proof number or novelty claim.

### MI177 — B78: swapping two exceptional residues removes the margin cost (2026-10-16 22:57 BST)

**Pull/question.** A coprime negative list may become divisible after merging
just two entries. I first thought three roots would be needed; then noticed
that swapping those two entries changes the exceptional residue. Delight at
that extra freedom: can it keep B77's TWO-root margin while crossing into gcd1?
This is the live run-selection question, not another shifted instance table.
Record searched: two.run|sumset|long.edge|role.change ->70 hits/24 files;
complementary.residue|exceptional.pair|two.exceptions|orientation.*residue
->11 hits/7 files, none on this construction. MI174-176 and the existing
MI117/MI126 prefix/reordering tools read; no new imported theorem, literature
status or novelty claim. Elementary residue argument below supplies the step.

**Sufficient construction, PROOF-SKETCH.** Let M=2n even, p,q positive odd,
p+q=2 sum d_i. All d_i>0. Suppose a modulus g>=3 divides all but TWO entries
a,b, with a+b=0 mod g and a!=0 mod g. If max(p,q)<=M-3 and the ATOMIC list
(a+b, all other d_i) fits into two bins of half-load<=n-1, then the original
moves(p,q,-2d_1,...,-2d_N) have a folded-distinct cycle in0..M-1.
This includes genuine gcd1 lists, e.g. g3,a1,b2. It is SUFFICIENT only:
requiring a,b in the same run can reject a constructible original list.
No anchors, other components or general E28 claim.

Place the a+b atom in run A; expand it to a,b, with other entries in any
order in A/B. They need not be adjacent: multiples of g may intervene. Let
s=sum A,t=sum B,w=p-2s. The word is p,negatives A,q,negatives B. The fitting
root interval is L=max(0,-w),R=min(M-1-p,M-1-2t). Independently of B77's
unreviewed status, its elementary bounds follow again: if w>=0, the two
upper bounds are>=2 and>=1 above L0; if w<0 their differences above L are
M-1-2s>=1 and M-1-q>=2. Thus L,L+1 both fit.

Let P_A be FORWARD prefixes of A, V_B prefixes of REVERSED B, including
endpoints, and H=(M-1-p)/2. Vertices are h+p-2P_A and h+2V_B. Reflection
requires V_B-P_A=H-h. If a precedes b, P_A residues are contained in{0,r},
r=a mod g, and V_B in{0}. Thus avoiding h-H in{0,r} suffices. Swapping only
a/b changes r to -r, without altering s,t or the fitting interval.

There is always a choice among these TWO roots and TWO orientations. If
2r!=0 mod g, first choose h among L,L+1 with h-H!=0. At most one of r,-r
equals h-H, so choose the other orientation. If 2r=0 mod g, then g is even
and r=g/2>=2: the forbidden classes0,r cannot cover two consecutive integers.
Choose the unblocked root; either orientation works. Each parity run is
monotone/distinct; opposite parities cannot coincide physically; all cross-
reflection is excluded. This proves sufficiency. No hidden vertex capacity:
K>=g(N-1)>=3(N-1), K<=2n-3, n>=4, so N<=floor(2n/3)<=n-2.

**Prediction BEFORE code/run.** Formula-only tight family: g3..11,
a1..g-1,b=g-a, four other halves all g; M=6g+2, positives(4g+1,6g-1) and
its reversal; A has a,b and two g's, B the other two g's. Test adjacent and
interleaved a,g,b,g layouts. Exactly216 geometries, root interval EXACTLY
two integers. Predict all pass,108 use the second root,36 need a/b swap
under the lexicographic root/orientation selector. All four-step choices
are residue checks, never a geometric root/order search. Independently
calculate full cross-parity sums and literal folded labels, rather than
reusing the modular predicate as the geometry oracle.

Three actual M28 fixtures: d=(1,2,3,3,6,9), A indices0,1,5, B2,3,4,
p/q25/23 and23/25; plus d=(1,2,3,3,6,6), A0,1,2,4,B3,5,p=q21.
All are gcd1 eight-vertex cases beyond the common-divisor theorem. Materialize
all three odd partitions with slots(1,1,2,2,2,2,2,2); literal and independent
inventory validators must agree. No growing profile census or fallback.

Counterfactual g2: M14,p9,q11,d=(1,1,2,2,2,2), same3g/2g loads; all four
prescribed root/orientation combinations must fail literal geometry. Indeed
8 vertices exceed7 labels, showing the g>=3 omission can make the theorem
false. The residue selector must refuse g2. Unexpected outside-scope positive:
M16,p7,q13,same d/run,root7 gives(7,14,12,10,6,2,15,11), all labels distinct,
although the two residue classes cover every root. Thus the modular condition
is sufficient, not necessary. Finally g3,d=(2,4,9,9),p23/q25: the atomic list
(6,9,9) has no13/13 split, while original halves split11/13. Record only an
atomic-admission refusal, never component/target impossibility.
Caps216 family geometries+3 partitions+named controls,2CPU sec/64MiB.
Stop on first mismatch or cap; no repair, alternate search or widened grid.
Gut: ACT; the orientation choice is the fresh bit, and it eliminates an
extra-margin hypothesis rather than adding one. Pending MI175 review is
independent and does not block this argument or its bounded checks.


### MI178 — B78: coprime construction with no extra root margin (2026-10-16 22:59 BST)

**Hand sufficiency SKETCH; prescribed evidence COMPUTED.** All216 tight
geometries pass:108 use L+1,36 reverse the exceptional entries, exactly as
predicted.160 have actual negative-half gcd1. Every root interval contains
EXACTLY two integers. Adjacent and interleaved exceptional layouts both work;
the latter checks that residue control is not secretly a single-vertex
subdivision argument. The even-g self-inverse residue cases also pass. CPU
0.009510s,peakRSS15,638,528bytes. No geometry search, repair or enlarged grid.
All3 named E28 partitions pass both literal and inventory validators (two
sorted target tuples, not additive coverage). Their selected positions are
(0,25,23,19,1,24,18,12), (1,24,22,18,0,25,19,13), and
(4,25,21,19,13,1,22,16); the third requires both L+1 and the swapped order.

All named controls pass. The g2/M14 example fails all four prescribed choices
and has8 vertices for7 labels: the theorem without g>=3 really can be false.
The M16 outside-scope word at root7 WORKS despite every root residue being
forbidden by the conservative modular test. Thus residue refusal is not
geometric impossibility. The atomic list(6,9,9) refuses13/13 capacity while
its original list(2,4,9,9) has11/13 capacity; requiring the exceptional pair
in the same run is a genuine admission restriction, not a necessity theorem.
No component or target rejection is inferred there.

**What changed.** B77's shared-divisor assumption is no longer required for
this paired-exception class: collapsing a,b exposes the divisor, then order
orientation supplies the missing freedom when expanding again. Unlike my
first extra-space thought, the original two-root margin suffices. The proof
is independent of MI175's pending status: MI177 explicitly rederives the root
interval and all reflection conditions. It does not prove arbitrary gcd1 run
selection, cover different odd sign patterns or settle E28/L8.

**Niggle sweep.** (1) Wrong prefix sign? Literal cross-sums independently
check V_B-P_A=H-h, so forbidden h-H residues are0,r, not0,-r for the chosen
orientation. (2) Swapping distant a/b could alter range? Run total and positive
endpoints stay fixed; both runs remain monotone. (3) Self-inverse residue?
Handled separately: r=g/2>=2, so the two blocked classes are not adjacent.
(4) More vertices than labels? K>=3(N-1), K<=2n-3 and n>=4 give the stated
integer bound; at the smallest possible n4, d=(1,2), M8,p1/q5 has selected
positions(5,6,4,0), four distinct labels by direct hand check. (5) Scope
slips to an iff or all gcd1? Explicit atomic-admission and g2 positive controls
prevent that. Local niggles resolved; general statement stays SKETCH.

Gut: delight at discovering an extra choice instead of paying an extra margin.
Fresh reasoned verdict: this advances a live selection mechanism, but endlessly
adding one residue class at a time would become another patch loop. The next
cheap question is whether the orientation argument scales to several balanced
exception pairs, or whether interacting prefix residues kill that idea. First
analyze the residue sets algebraically; no new run or survey is opened here.
Pending MI175 carrying read remains nonblocking. Cloud gets a concise mentoring
update, not another routine carrying-read request or a permission gate.

Artifact `cited/instinct/b78-complementary-residues-44aa07289ff08332.json`,88305bytes,
SHA256 `44aa07289ff083320cddecd5f0e1faf2d6cabd84e2d970f9540e81ab5caa3556`.
Preregd0428cf3; source tests/probes/instinct/path_forest_complementary_residues.py.
Immutable upload and manifest append receipts verified. No formal proof number,
novelty claim, held-lane change or automation change.


### MI179 — CL427 adopted: MI175 PROVED; keep the coprime conjecture's choices coupled (2026-10-16 23:01 BST)

Verified commit8a9369af, read CL427 and all four source files under
 tests/probes/cloud_reads/: b77_check.py,gcd1_survey.py,gcd1_stats.py,
gcd1_small.py. Cloud's explicit carrying read rederives MI175's ANY-order
necessity, both root-interval sign cases and the modulus/reflection identity.
It verifies the general theorem; MI175 is now PROVED within its original
common-divisor scope. Historical SKETCH wording is retained as provenance.
B78/MI177 remains SKETCH: Cloud's review predates this result and does not
verify it. No independent computation rerun, formal proof number or target-
level promotion is made in this checkpoint.

Cloud reports its gcd1 M28 survey:6704 questions,6617 capacity-feasible,
6312 successful/305 failed, all failures p=q25. Treat this as Cloud-reported
finite evidence for its four-condition conjecture, not a universal result.
Source caveat: gcd1_small.py's implemented conjecture omits condition3,
N+2<=M/2. The concrete M8,p3/q5,d=(1,1,2) has a1/3 capacity split and legal
odd bounds, not doubled5, but5 vertices for4 labels. Thus that source tests
a weaker, false formula and cannot directly substantiate the stated exact
four-condition small-window agreement. Request a source/count correction in
the next concise flag, not another theorem review. The carrying hand read of
MI175 is unaffected. gcd1_survey.py also has a400sec early break without a
completion assertion; gcd1_stats.py has the full repeated sweep. No raw survey
receipt was supplied, so I do not independently promote its counts.

The suggested fixed-A/B hole lemma is stronger than the offered conjecture:
our existing central p=q21,d=(3,3,3,4,4,4), A all3s/B all4s has no hole at
ANY of its4 fitting roots (MI175 control). Reordering those constant runs
cannot help, although B74 changes the split and succeeds. A proof must choose
split, within-run order AND accessible root jointly. This is concrete pushback
using retained evidence, not a new guard/probe or a refutation of the conjecture.
The new B78 orientation theorem is one sufficient joint choice; its atomic
admission restriction remains explicit. Next proof work should target that
joint selection problem, not re-enumerate Cloud's surveyed profiles.


### MI180 — B79: two coloured increasing chains; refine, fill, then contract (2026-10-16 23:11 BST)

**Pull/question.** Surprise: filling EVERY folded label is easier than leaving
holes. Reflecting the odd vertices turns the placement into two disjoint
increasing chains; a binary word can then choose the split and orders together.
The promising sparse step is to refine a large negative half into a smaller
half plus units, build the full word, then contract those units without changing
the odd jumps. This changes representation instead of adding residue patches.
Record searched: colour/run/gap/full-occupancy/two-increasing/binary-word-gap
->8 unrelated hits/4 files; gap.word|colou?r.*chain|refin.*contract|saturat.*label
->33 unrelated hits/14 files. MI174-179/CL427 read. No imported theorem, new
literature-status claim or novelty claim; all carrying steps are below.

**Exact two-chain picture.** On M=2n, an even position2u corresponds to index
u in0..n-1. Reflect an odd position to write it as2n-1-2v. A cross-parity
reflection collision is EXACTLY u=v. Two positive odd jumps allow the negative
even moves to follow increasing B indices, then decreasing A indices. For
increasing disjoint chains A,B, with min A0, the cycle is

    0 -> (2n-1-2v for v in B increasing) -> (2u for u in A decreasing, u>0) ->0.

Its odd jumps are p=2n-1-2 min B and
q=2(max A+max B)-(2n-1). Its negative half-sizes are the consecutive gaps
within A and B. Thus selecting a coloured word chooses the split/orders/root
jointly; no preselected split or sumset-hole search is assumed.

**Full-label theorem, PROOF-SKETCH.** N=n-2 positive negative-halves d_i,
p,q positive odd, sum d=(p+q)/2. A placement exists IFF
max(p,q)<=2n-3 and not p=q=2n-3. Necessity is the ordinary jump bound and
the doubled-long-edge label obstruction. Sufficiency also shows the separate
two-bin capacity condition is automatic in this saturated case.

Relabel the positive owners if needed so p>=q; then q<=2n-5. Set
alpha=(2n-1-p)/2>=1, beta=(2n-3-q)/2>=1, K=sum d. Make a binary word with
first run A of length alpha, last run of length beta, and INTERNAL run lengths
(d_i-1) for every d_i>1, in any order, alternating colours. If m entries exceed1,
there are m+2 runs, and its total length is

    alpha+beta+sum_(d_i>1)(d_i-1)
    = (2n-2-K)+(K-N) = n.

Both colours occur. Gaps within a run are1. Each internal run of length ell
creates exactly one gap ell+1 in the OTHER colour; the total number of unit
gaps is n-(m+2)=N-m. Thus the gap multiset is exactly d. The smallest indices
of A/B are0,alpha, so the first odd jump is p. The two largest indices are
n-1 and n-1-beta, so the other odd jump is q. All n indices have exactly one
colour: every folded label is used once. Both run loads are chain extents
<=n-1. This is arbitrary n/d, not an inference from small-window testing.

**Sparse contraction theorem, PROOF-SKETCH.** Now N<=n-2 and
k=n-N-2>0 unused labels. Under the same legal odd-jump/non-doubled conditions,
if TWO distinct negative halves D,E satisfy min(D,E)>=k+2, a placement exists.
No gcd or precomputed capacity split is required. This is sufficient only.

Refine D into(D-k,k unit entries); the refined list has n-2 entries, same K,
and D-k>=2. Apply the full-label construction, ordering its first TWO internal
runs as D-k-1 (colour B), then E-1 (colour A). The third run has length
E-1>=k+1. Delete its FIRST k A-indices. Before deletion, the A gap across the
preceding B run is D-k; after deletion it is(D-k)+k=D. Exactly k following
unit gaps disappear. Every other gap, including B's gap E ACROSS that third
run, keeps its actual index distance. At least one point of the third run
remains, so neither colour's minimum or maximum changes; p and q are unchanged.
Selected vertices remain a subset of a folded-distinct placement. The final
negative-gap multiset is the original d, with N+2 selected vertices.

A genuine central gcd1 example at M28,N6,k6: d=(8,8,1,1,1,1),p21,q19.
Refine the first8 into2 plus six1s. The full coloured word is A^3 B A^7 B^3.
Delete the first six A's from its third run. Remaining chains A=(0,1,2,10),
B=(3,11,12,13), giving cycle positions(0,21,5,3,1,20,4,2), odd jumps21/19
and negatives(-16 twice,-2 four times). This was derived by hand, no order
search. With slots(1,1,2,2,2,2,2,2), target(98,94,80,80,108,108,108,108).
The new class crosses gcd1 in the high-total regime, beyond B75; full E28 open.

**Predictions BEFORE code/run.** Formula checks only. Full-label fixtures
n=(3,4,5,8,14,25): each all-unit list with extreme and balanced positive pairs,
and each one-large(n-1 plus n-3 units) and all-two list at p=2n-3,q=2n-5.
Exactly24 prescribed formula calls (some tiny cases coincide; no distinct-
coverage count implied). Compare gap bags from run-length reasoning to an
independent direct coordinate-cycle difference bag, and literal folded labels.

Sparse fixtures: at M28,N6, d=(8,8,1,1,1,1), positive pairs25/15,23/17,21/19;
also d=(8,8,2,2,2,2),(10,10,1,1,1,1),(8,9,1,1,1,4), each p25/q23.
Predict all SIX actual E28 partitions materialize under the same slots and
both literal/inventory validators pass. The21/19 positions must equal the
hand example above, with deterministic internal ordering. Two other windows:
M20,N4,d=(6,6,1,1),p17/q11,k4 and M40,N6,d=(14,14,1,1,1,1),p37/q27,k12
must certify, checking that the deletion count is the label deficit, not a
fixed6. No original/refined profile census or alternate-order search.

Counterfactuals: reject p=q=M-3 and oversubscribed N+2>n. The M28 list
(7,8,1,1,1,1),p25/q13 does NOT meet the two-large admission condition; refuse
this construction only, not the component/target. Unexpected check: deleting
k+1 rather than k points in the tight hand example still leaves a folded-
distinct subset, but must change the odd jump/endpoints and fail the original
move-bag test. This catches a geometry-only false certificate. Retain the
full/refined/contracted chain data. Caps24 full+8 sparse formula calls,2CPU sec/
64MiB. Stop on first mismatch/cap, no patch, expanded grid or fallback.

Gut: a fresh warm pull and surprise at a construction choosing all three
variables together. Reasoned: the two-large condition is a real sparse
restriction; do not call it the general coprime conjecture. Next would be
whether refinements can be distributed across several internal runs when no
single pair can absorb the label deficit. No such experiment is opened here.


### MI181 — B79: joint selection through a coloured word, with a valid sparse contraction (2026-10-16 23:14 BST)

**General constructions SKETCH; prescribed checks COMPUTED.** All24 full-label
formula calls and8 sparse calls pass. Six actual E28 partitions pass independent
inventory and literal validators. The two other sparse pools use k4 and k12,
confirming the removal is driven by the label deficit. Full-label fixtures
include n3 and n25, units, one long gap and all2s. These are formula controls,
not new truth surveys or a finite justification of the infinite hand claims.
CPU0.003476s,peakRSS15,544,320bytes. No ordering/split/root search or repair.

The hand example is reproduced exactly: A=(0,1,2,10),B=(3,11,12,13), physical
positions(0,21,5,3,1,20,4,2), target(98,94,80,80,108,108,108,108).
The other five prescribed E28 cases also materialize. No additive target-
coverage or novelty claim. This is a uniform sparse family, not a list of
exception repairs; some instances overlap older mechanisms, which is harmless.

All named negative controls pass. The doubled-long-jump and label-overflow
inputs are rejected. A two-large admission failure is scoped to this formula,
never the component or target. Unexpected wrong deletion: removing7 instead
of6 A-indices still gives a folded-distinct7-vertex subset, but changes the
second odd jump19 to3 and loses a negative16 edge. The literal MOVE BAG and
endpoints reject it. Thus retaining reflection freedom alone cannot certify
that contraction solved the original problem.

**What changed.** The full-label part of CL427's conjecture is now settled by
a hand construction pending independent read: N=n-2, arbitrary d, every legal
positive pair except the doubled M-3 pair. In this case the capacity split is
constructed, not supplied. The sparse extension proves a sufficient class
with k=n-N-2 unused labels whenever two negative halves are>=k+2, independent
of gcd and without asking for an initial split. At E28,N6,k6 this means two
halves>=8, and includes the new high-total gcd1 example above. General sparse
lists with no such pair, mixed anchors and other odd sign patterns remain open.
No full E28/L8 claim. Old prize lanes remain held.

**Niggle sweep.** (1) Wrong index/physical reflection? Even2u and odd2n-1-2v
reflect exactly when u=v; direct folded labels independently agree. (2) Odd
jumps swapped? Positive owners may be relabelled to p>=q; the physical word's
first and B-last jumps are checked against p/q, including equality fixtures.
(3) Run gaps multiply? Each INTERNAL run creates one opposite-colour gap;
unit multiplicity n-(m+2)=N-m and the direct difference bag both agree.
(4) Deleting A-indices changes B's long gap? Its endpoints stay at the same
actual indices; intermediate colours are immaterial. (5) Emptying a run or
changing an endpoint? E-1>=k+1 leaves its last A point; four extrema explicitly
checked before/after. (6) Refinement changes K? D-k plus k units sums D.
(7) Geometry mistaken for the original moves? The wrong-deletion control
explicitly separates them. Local niggles resolved; neither general theorem
self-upgrades beyond SKETCH.

Gut: delight at the change of representation; this is an actual joint choice,
not warmth inherited from the last residue construction. Reasoned: the remaining
sparse restriction is substantial. Next cheap question: distribute contractions
across runs while preserving the four endpoint constraints and original move
bag, rather than start another coprime census. A failure of that particular
contraction scheme will not refute the wider existence conjecture. No such
new experiment is opened now. This is a useful point for ONE carrying read of
MI180's coloured-gap accounting and endpoint-preserving contraction; no review
halt or permission gate, and no second request for B78's routine checks.

Artifact `cited/instinct/b79-coloured-chains-7067f4f35caf051c.json`,14655bytes,
SHA256 `7067f4f35caf051cc01497dc304e6eb0ba582dedcd4b54cbe0203875f9007cb8`.
Preregb4de8b25; source tests/probes/instinct/path_forest_coloured_chains.py.
Immutable upload and manifest append receipts verified. No formal proof number
or automation change.


### MI182 — B80: a deletion-budget failure gives way to two parallel prefix chains (2026-10-16 23:24 BST)

**Initial question/pull and retained failure.** Can distributed contractions
remove B79's two-large requirement? For a PREFIX-only extension, write r_i
for refinements of ordered nonunit halves D_i, leaving D_i-r_i>=2, and delete
r_i initial points of the next run. Survival imposes r_1<=D_1-2,
r_i+r_(i+1)<=D_(i+1)-2, and r_m<=beta-1. At the known central M28,p=q21,
D=(3,3,3,4,4,4), k6, sum(D_i-2)=9,beta2. Summing gives
2 sum r_i-r_m<=9, so sum r_i<=5. NO ordering can remove the required6 by
this scheme, although B74 already constructs the component. This is a concrete
failure of the proposed scheme, not the existence conjecture; retained as this
one paragraph, no separate probe/proof/review job. Push: do not turn that budget
into another search engine. The chain picture itself still feels useful.

**Change of representation/pull.** Adjacent selected-index gaps g_j would give
negative halves g_(j-1)+g_j when the selected colours alternate. If halves
come in equal pairs, the gap pattern t,D_1-t,t,D_2-t,...,t,D_m-t,t returns to
t after every pair. I first worried t must sometimes be2 and collide with a
half2; then noticed the two odd positives have OPPOSITE residues mod4. Swap
which comes first and t can ALWAYS be1. Delight: choosing an owner rather
than paying extra space. This is the mathematical contribution of this block.
Record searched: parallel.*chain|paired.*negative|same.*prefix.*translate|
paired.*half ->16 hits/7 files; MI085's paired FOUR-move parent read and
separated (different sign pattern/subdivision problem). MI180-181 and CL427
remain the current geometric context. No imported theorem or novelty claim.

**Paired-negative theorem, PROOF-SKETCH.** M=2n even, m>=1, D_i>=2 integers,
S=sum D_i. Let p,q>0 be odd and p+q=4S. Then

    (p,q,-2D_1,-2D_1,...,-2D_m,-2D_m)

has a folded-distinct cycle in0..M-1 IFF max(p,q)<=M-3. No common divisor,
capacity split, initial ordering search or large-gap condition is supplied.
This is a fixed-move theorem, not all E28, and excludes D_i=1 from its scope.
Necessity is the existing individual odd-jump bound. The two positives cannot
be equal: their residues mod4 are opposite since p+q=0 mod4.

For sufficiency choose as FIRST positive P the unique one congruent M-3 mod4;
let Q be the other, so the positive owners may exchange order. Set
 a=(M-3-P)/4>=0, and C=(0,D_1,D_1+D_2,...,S).
Take increasing index chains

    A=a+C, B=a+1+C.

No prefix difference in C is1, because all D_i>=2. Thus A and B are disjoint,
with each chain individually distinct. Both fit: from Q=4S-P we have
Q=4(a+S)-M+3<=M-3, hence a+S<=n-2 and max B<=n-1.
Use even physical positions2A and odd positions M-1-2B. They reflect iff
an A-index equals a B-index, already excluded. Follow B increasing physically
downward, then A decreasing physically downward, using the two positive jumps
to join them. The first jump is M-1-2(a+1)-2a=P, the other
2(a+S)-[M-1-2(a+S+1)]=4(a+S)-M+3=Q.
Each chain's negative halves are exactly D_i, one forward and one reversed.
So every move and owner is accounted for. Label capacity is automatic:
S>=2m, while paired positive bounds give S<=n-2, so2m+2<=n.
Both run loads are S<=n-2. This proof does not depend on B79 being verified.

**Predictions BEFORE code/run.** Only EIGHT formula calls: general geometries
M8,D=(2),p5/q3; M14,D=(2,3),p11/q9; M16,D=(2,3),p11/q9 (which exchanges
which positive starts); M200,D=(2,3,...,11),p197/q63. Four actual M28 cases:
D=(2,3,5) with positives25/15 and23/17, and D=(3,3,5) with25/19 and23/21.
For these use original negative halves d=(D_1,D_1,D_2,D_2,D_3,D_3) and
slots(1,1,2,2,2,2,2,2). Predict both literal/inventory partition checkers pass.
These gcd1 examples have no two halves>=8, so B79's two-large rule cannot
supply them; some may overlap other independent mechanisms, not additive
coverage. Check original positive OWNER mapping even when the first move is
the smaller input. Direct physical differences must match the entire input
move bag independently of the prefix-chain/reflection checks.

Controls: max-bound failure M28,D=(3,3,5),p27/q17 is rejected (a+27 edge is
a folded loop or outside). A D1 scope example M28,D=(1,3,7),p25/q19 makes
the proposed A/B chains intersect; direct geometry must fail, but do not infer
that another ordering/component is impossible. Unexpected wrong-owner control:
for M28,D=(3,3,5),input23/21, blindly taking the larger input and FLOORING
(25-23)/4 to0 leaves a reflection-free placement but produces positives25/19,
not23/21. Literal original move-bag validation must reject it. This tests that
the residue-based owner choice is doing actual work. Caps8 formula calls,
1CPU sec/64MiB; stop on mismatch/cap, no repaired search or expanded family.

Gut: warm after the honest budget failure, because the owner-order choice was
unexpected. Reasoned: paired negative halves>=2 form a complete class, but
unpaired lists and paired halves1 remain outside this proof. Next question is
what unequal parallel prefix chains need to avoid an index difference1;
not another round of fixed-instance repairs. No new experiment opened there.


### MI183 — B80: paired halves give a complete class via a unit offset (2026-10-16 23:26 BST)

**Hand iff SKETCH; eight formula calls COMPUTED.** All8 prescribed calls and
4 actual E28 partitions pass. Three calls require the SMALLER original odd
positive to start, including both23/17 and23/21 at M28. The original positive
owner mapping and complete physical move bag agree in each. M8/M14/M16 and
m10 at M200 check small windows, both even-window residue classes and arbitrary
move count. CPU0.001363s,peakRSS15,335,424bytes. No search, repair, domain
expansion or inferred universal result from finite tests.

Both scope controls pass. Including D1 in the parallel formula makes its index
chains intersect and literal reflection fails; another construction is not
excluded. The odd-jump bound violation is refused. Unexpected wrong-owner
control remains geometrically valid but changes requested positives23/21 to
25/19; literal original move-bag comparison catches it. Thus modular owner
choice is substantive, not bookkeeping that can be rounded away.

**What changed.** Arbitrary paired negative halves D_i>=2, including gcd1,
now have a uniform hand construction with no extra hypothesis beyond legal
individual odd jumps. Capacity and label count follow automatically. The
construction handles high-total examples with modest negative halves where
B79's two-large admission fails, without extending the failed prefix-deletion
scheme or enumerating exception profiles. It does NOT cover unpaired negative
halves, D1 pairs, mixed anchors or other odd sign arrangements; E28/L8 stay
open. No additive coverage or novelty claim. MI182's concrete central deletion-
budget failure remains part of the record.

**Niggle sweep.** (1) A hidden assumption that the larger positive starts?
Removed: the residue chooses the owner; three explicit flips tested. (2) Can
both positives share M-3's residue? Their sum4S forces opposite odd residues.
(3) Upper-index bound off by one? Q<=2n-3 implies4(a+S)<=4n-6, hence integer
a+S<=n-2; max B<=n-1. (4) Unit offset might meet a nonadjacent prefix?
Any nonzero prefix difference is a sum of positive D's, at least2, so never1.
(5) Too many labels? 2m<=S<=n-2. (6) Positive owners changed target?
Complete input move bags and actual bin inventories tested, with a deliberate
wrong-owner false certificate. (7) Self-verification upgrades? The infinite
statement stays SKETCH; B79's separate carrying read remains nonblocking.

Gut: satisfaction at the shorter proof, and a warm pull after a real failed
attempt rather than a softened failure. Reasoned: the one-index separation
is a reusable mechanism. Next cheap question is how two UNEQUAL negative
prefix sequences can be coupled to retain that separation, with an explicit
kill example before generalising. No new experiment or carrying-read queue
opened here; Cloud receives this as one concise update alongside the retained
failure. Held lanes and automation remain unchanged.

Artifact `cited/instinct/b80-parallel-pairs-cc53333c2dd4dfcf.json`,3465bytes,
SHA256 `cc53333c2dd4dfcf9fe33f4618766ba2433efe16172cf9ece66207ea80581ba5`.
Prereg712f33c0; source tests/probes/instinct/path_forest_parallel_pairs.py.
Immutable upload and manifest append receipts verified. No formal proof number.


### MI184 — B81: unequal prefixes interlace with a two-state separation (2026-10-16 23:35 BST)

**Question/pull.** What survives when the two negative runs are unequal?
The useful quantity is their current index separation delta, not a list of
forbidden pair sums. A pair differing by1 changes delta by +/-1, so orienting
unequal pairs can keep delta in{1,2}. Surprise: the only small-step hazard is
an equal pair(2,2) at separation2; changing the PAIR ORDER fixes it. This is a
joint split/order/endpoint construction, extending B80 rather than another
instance repair. Record searched: adjacent.*pair.*prefix|interlac.*chain|
near.pair|delta.*two.*run ->30 unrelated hits/12 files. MI180-183 and CL427
read. No imported theorem, literature-status or novelty claim.

**Class theorem, PROOF-SKETCH.** Let M=2n, d_1<=...<=d_(2m) with every d_i>=2,
and each sorted consecutive pair(d_(2i-1),d_(2i)) differ by at most1. For odd
p,q>0 with p+q=2K=2 sum d_i, a folded-distinct cyclic placement of
(p,q,-2d_1,...,-2d_(2m)) exists IFF max(p,q)<=M-3 and not p=q=M-3.
No initial capacity split or label count is needed; they follow below. B80's
paired-halves theorem is the all-equal-pairs subcase. This does not cover half1,
odd negative count, arbitrary unmatched pairs or anchored components.

**Construction and all boundary choices.** Let r count unequal pairs.
If r=0, choose FIRST positive P congruent M-3 mod4 as in B80; its alpha below
is odd. If r>0, choose P=max(p,q), Q the other. In either case P<=M-3 and
Q<=M-5: the latter is obvious for r>0 by excluding the doubled maximum, and
for r=0 follows because the two positive residues differ. Define

    alpha=(M-1-P)/2>=1, beta=(M-3-Q)/2>=1,
    delta_0=1 if alpha is odd, else2;  a=(alpha-delta_0)/2>=0.

We build A=a+prefixes(u_i), B=a+delta_0+prefixes(v_i), assigning one member
of each d-pair to each run. Separation after a pair obeys
 delta_(i+1)=delta_i+v_i-u_i.
For an unequal pair(x,x+1): at delta1 choose(u,v)=(x,x+1), moving to2;
at delta2 choose(x+1,x), moving to1. Equal pairs preserve delta.
Equal pairs with value>=3 are safe in either state. Equal(2,2) needs delta1.
Process all equal(2,2) pairs at state1: if delta_0=1 put them first; if
 delta_0=2 and any such pair exists, first process ONE unequal pair down to1,
then all the(2,2)'s. Such an unequal pair exists, since r0 forced delta_0=1.
Then process all remaining pairs by the stated orientation rule.

At every step, 0<delta_i<u_i: for equal2 this is1<2; for larger equal pairs
it is<=2<value; for unequal pairs it is1<x or2<x+1. The next separation is
also positive. Therefore A_i<B_i<A_(i+1)<B_(i+1): the entire index lists
strictly interlace. No index can occur in both chains, so the physical even2A
and odd(M-1-2B) are folded-distinct.

**The terminal bound is automatic, not an assumption.** Every unequal pair
toggles delta and every equal pair preserves it. Hence delta_m is1 or2 with
parity alpha+r. The parity of K is r, and alpha+beta=M-2-K is even-K.
Thus delta_m has beta's parity, and is its smallest positive representative:
delta_m<=beta. Also min A+min B=alpha, and
max A+max B=alpha+K=(M-1+Q)/2. As B ends above A,
max B=[(M-1+Q)/2+delta_m]/2<=[(M-1+Q)/2+beta]/2=n-1.
All indices fit. The two physical odd jumps are exactly P,Q, by these two
endpoint sums; both negative runs use precisely their assigned halves.
Loads differ by delta_m-delta_0 in{-1,0,1}, so are floor/ceil(K/2)<=n-2.
Since K>=4m and K<=2n-4, 2m+2<=n: enough labels automatically. Necessity
of the two odd-jump exclusions is unchanged. This proof rederives the chain
conditions and does not depend on B79/B80's unreviewed status.

**Predictions BEFORE code/run.** Exactly NINE formula calls. Five actual M28
partitions: d=(3,3,3,4,4,4), p21/q21 and25/17;
d=(2,2,3,3,3,4),p19/q15 (must move an unequal pair before the2/2 pair);
d=(2,3,3,4,5,6),p25/q21 (three unequal pairs, signs must alternate);
and d=(2,2,3,3,5,5),p23/q17 (all equal pairs, smaller positive starts).
Materialize each with slots(1,1,2,2,2,2,2,2); both literal/inventory validators
must pass, with original positive/negative owners retained.
General geometry fixtures: M8,d=(2,2),p5/q3; M16,d=(2,2,3,4),p11/q11;
M32,d=(2,3,4,5,6,7),p29/q25; M300,d=(2,3,...,21),p297/q163.
Independently check full physical move bags, all folded labels, strict chain
interlacing, and endpoint sums; no all-order solver or profile census.

Kill/negative controls written first: on M32's three unequal pairs, always
putting the smaller half in A gives end separation4>beta2 and max B16>n-1;
reject by literal window bounds. On the M28 2/2 fixture, processing sorted
pairs without the early unequal pair makes A's first new point equal B's
start (separation2, step2); reject by literal folded labels even though the
move bag remains correct. This is the identified unexpected ordering check.
Reject doubled longest positives at M24,p=q21,d=(3,3,3,4,4,4), and reject
half1 as outside scope. An OUTSIDE-pairing positive control M28,d=(2,2,2,4,4,4),
p25/q11 has a sorted pair gap2: refuse this constructor only, but the existing
B77-style witness(0,25,21,13,5,16,12,8) must pass literal geometry AND its
full input move bag. Thus a failed sorted-pair test is not a failed target.
Caps9 formula calls/5 partitions+named controls,1CPU sec/64MiB. Stop on first
mismatch/cap; no repaired geometry search, widened range or extra sample.

Gut: warm because this includes unpaired multiplicities and recovers the
older adjacent-size geometry by a new explanation. Reasoned: the next true
obstruction is larger pair discrepancies or unit halves, not arbitrary warm
extrapolation from these9 tests. General E28/L8 remain open; no new experiment
or carrying-read queue opened for those remaining cases.


### MI185 — B81: unequal runs stay interlaced; terminal parity supplies the margin (2026-10-16 23:37 BST)

**Hand class iff SKETCH; prescribed evidence COMPUTED.** All9 formula calls
and5 actual E28 partitions pass. The two fixtures needing an unequal pair
BEFORE the2/2 pair do so, at M28 and M16. Initial/final separations include
1->2,2->1,1->1; endpoint sums and literal full move bags all agree. The paired
subcase correctly starts with the smaller positive17 for input23/17. CPU
0.001503s,peakRSS15,900,672bytes. No order/split/root search, repair or census.

Both predicted shortcut failures occur: always putting the smaller half in A
ends at separation4 and B-index16 outside M32's index window; leaving2/2
first at initial separation2 causes an A/B index collision at M28. Both still
have their original move bags, so geometry is checked independently. Doubled
long-edge and half1 exclusions are retained. The gap2 sorted-pair input is
refused only by THIS constructor: its prior explicit witness passes full
geometry and input move-bag checks, preventing a false nonexistence verdict.

**What changed.** A uniform unpaired-multiplicity class now works: an even
number of negative halves>=2, sorted pairs differing<=1. One separation bit
chooses which member goes in each run; equal2 pairs are scheduled at state1.
The final state's parity proves it fits beta, rather than assuming an endpoint
bound or sampling it. B80 becomes the all-equal-pair corollary. The central
3x3/4x3 family receives a new explanation, and the d=(2,3,3,4,5,6) example is
neither paired nor admitted by B79's two-large condition. No additive coverage
claim. Larger pair discrepancies, half1, odd negative count, mixed anchors
and full E28/L8 remain open.

**Niggle sweep.** Equal2 at delta2 is explicitly moved after a downward toggle;
r0 cannot strand it since the positive residue choice makes delta_0=1.
The final parity uses K mod2=r, not the number of negatives; alpha+beta=M-2-K
and the smallest positive representative give delta_m<=beta. Strict interlacing
checks all cross-indices, not just simultaneous prefixes. Physical positive
owners, complete negative bag, label count and balanced loads are independently
checked. No self-check upgrades either this claim or B79. Local niggles resolved.

Gut: warm because the endpoint obstruction became an invariant, not another
patch. Reasoned: constant separation states1/2 use the pair-discrepancy<=1
hypothesis essentially; do not extrapolate it to arbitrary capacity-feasible
lists. Next cheap step is to identify precisely what larger discrepancies
would require of the terminal separation before proposing a broader selector.
No new experiment or carrying-read queue here; MI180's read stays nonblocking.

Artifact `cited/instinct/b81-interlaced-pairs-717ef6c924338669.json`,6058bytes,
SHA256 `717ef6c924338669998de85d2799c124b86b761cdb20d5004f067cc2bf87cbc0`.
Preregce319d40; source tests/probes/instinct/path_forest_interlaced_pairs.py.
Immutable upload and manifest append receipts verified. No formal proof number,
novelty claim, held-lane or automation change.


### MI186 — B82: exchange the leading chain, rather than forbid crossings (2026-10-16 23:47 BST)

**Question/pull.** Can unequal pairs differ by2 or3 while preserving the
endpoint margin? The warm part is a change of picture: the two chains may
exchange which one is ahead. Their points only need to come in disjoint
successive two-point levels, not strictly interlace. A gap2 sends signed
separation1 to-1; gap3 exchanges magnitudes1/2 and reverses sign. This is
mathematical progress beyond B81's positive-separation invariant, not a
profile repair. Record searched: crossing.*chain|signed.*separation|interlac
->16 hits/8 files: B81 and unrelated historical passages; earlier
broad rung search also had unrelated historical hits. MI180-185/CL427 read. No
imported result or claim of novelty/literature completeness.

**Proposed class iff, hand SKETCH.** M=2n. There are2m negative halves d>=2;
sort and pair consecutively, each pair(x,y) has g=y-x<=3. Odd positives p,q
satisfy p+q=2K=2 sum d. Folded-distinct placement exists IFF max(p,q)<=M-3
and not p=q=M-3. Half1, odd negative counts, larger pair gaps, anchors and
other odd sign patterns remain outside this claim; full E28/L8 OPEN.

Let r count ODD gaps (g1 or3). If r=0, K is even; choose P congruent M-3
mod4, so alpha=(M-1-P)/2 is odd. Otherwise choose P=max(p,q). Write Q for
the other positive. As before Q<=M-5, alpha>=1, beta=(M-3-Q)/2>=1.
Set delta0 to1/2 according as alpha is odd/even, a=(alpha-delta0)/2.
A starts at a, B at a+delta0. For signed delta=B_i-A_i, choose the pair's
orientation by the following rule (the sign is ESSENTIAL):

    g0: u=v=x, preserve delta;
    g1: at |delta|1 move OUTWARD, at |delta|2 move TOWARD zero;
    g2: only at |delta|1, move TOWARD zero, crossing to -delta;
    g3: move TOWARD zero, crossing to opposite sign with magnitude3-|delta|.

Here moving delta by +g means(u,v)=(x,y); by-g means(y,x).
All states stay in{-2,-1,1,2}. Hazardous pairs are g2 and equal(2,2): both
need |delta|1. If starting at2 with any hazardous pair, put ONE odd-gap pair
first to reach magnitude1, then all hazardous pairs, then the remaining
pairs. Such an odd-gap pair exists: r0 forced initial1. If initial1, put
hazardous pairs first. If no hazardous pair, no early rearrangement is needed.
All other pairs are equal>=3 or odd-gap pairs, safe in either magnitude.

**Carrying step: crossing without collision.** At a positive delta, the
necessary level separation is u>delta; at a negative delta, v>-delta.
For equal pairs this is precisely x>|delta|, with equal2 scheduled at1.
For g1 outward at1, the lagging chain's step is x>=2>1; inward at2 it is
y=x+1>=3>2. For g2 at1 it is y>=4>1; for g3 it is y>=5>|delta|.
Thus max(A_i,B_i)<min(A_(i+1),B_(i+1)), while delta_(i+1)!=0.
Every two-point level is disjoint from every other, even when A and B exchange
order. All chain indices are distinct; physical even2A and odd(M-1-2B) are
folded-distinct because a reflection collision is exactly A-index=B-index.

**Terminal margin survives a sign change.** Odd gaps toggle magnitude1/2;
g0/g2 preserve it. Hence |delta_m| is the smallest positive representative
of alpha+r modulo2. K mod2=r and alpha+beta=M-2-K imply |delta_m| has beta's
parity, so |delta_m|<=beta. The endpoint sum is
A_m+B_m=alpha+K=(M-1+Q)/2, hence
max(A_m,B_m)=[(M-1+Q)/2+|delta_m|]/2<=n-1.
The initial sum is alpha; both indices are nonnegative. The cycle follows
B forward in physical decreasing order and A backward, with odd joins P/Q
from the two endpoint sums and negatives exactly-2u/-2v. Necessity is the
usual legal odd-edge bound and impossibility of repeating the longest edge.
K>=4m and K<=2n-4 imply2m+2<=n. Loads now may differ by4, rather than B81's
at-most1: delta_m-delta0 determines the difference, and each load<=n-1
follows from endpoints. Do NOT retain B81's stronger balance claim.

**Predictions BEFORE experiment.** Exactly11 formula calls,6 actual E28
partitions at M28, original slots(1,1,2,2,2,2,2,2):
 d=(2,2,2,4,4,4),p25/q11;
 d=(2,2,2,5,5,5),p25/q17 and23/19;
 d=(2,4,4,4,4,6),p25/q23;
 d=(2,2,2,4,4,5),p23/q15;
 d=(2,2,2,5,5,6),p25/q19.
General calls: M10,d=(2,4),p7/q5; M12,d=(2,5),p9/q5;
M16,d=(2,5),p11/q3; M32,d=(2,3,3,6,6,6),p27/q25;
M500,d=concatenation of pairs(2+4i,5+4i),i0..9,p497/q363.
Independent direct physical differences must reproduce the ENTIRE original
move bag, literal window/folded labels and both endpoint sums; all six actual
partitions pass both inventory/literal validators. Check pair-level ordering,
including negative states and crossings, independently of the state rule.

Counterfactual/kill: a crossing might hide a nonadjacent reflection collision;
the M10/M12 calls must pass complete folded-label comparison, not just local
states. Stop on any mismatch, no patch/search/domain expansion. Force the
smaller member always into A on the tight M28 d=(2,4,4,4,4,6) input: final
separation5 exceeds beta1 and must fail window bounds, although move bag is
unchanged. Suppressing the early odd pair on d=(2,2,2,4,4,5),p23/q15 must
cause an immediate equal2 collision at initial2. Unexpected check: M32's
fixture should end delta=-2 from initial2, loads15/11; it violates B81's
max-load<=n-2 assertion but must be geometrically valid, exactly hitting n-1.
Doubled longest M10,d=(2,5),p=q7 and too-long M10,p9/q5 are rejected.
Half1 and gap4 are constructor scope refusals only. An outside-gap4 witness
M14,d=(2,6),p11/q5,positions(0,11,7,12) must pass geometry AND full move bag;
refusal of our bounded states is not nonexistence. Caps11 calls/6 partitions,
1CPU sec/64MiB, no all-order solver or census. Raw evidence stays outside git.

**Fresh-choice reflection (before the90-minute boundary).** Both enjoyable
and a little wary of accumulating sibling classes. Without the past work I
would still choose this question: exchanging leading chains is a useful
change of representation, and terminal magnitude rather than sign explains
why it can work. The block has a real limit (gap3); after it, reconsider the
remaining obstruction rather than mechanically incrementing that number.
No extra review queue; MI180's carrying read remains nonblocking. Gut: warm,
with surprise at a legal crossing. Reasoned verdict awaits the finite checks;
infinite statement stays SKETCH pending independent scrutiny.


### MI187 — B82: signed crossings work; equal-length runs are the next real restriction (2026-10-16 23:49 BST)

**Hand class iff SKETCH;11 prescribed formula calls COMPUTED.** All11 calls
and6 original-owner E28 partitions pass. Every fixture contains a chain-order
exchange, including tiny M10/M12 and20 negatives at M500. Early odd pairs
reach magnitude1 before the hazardous equal2/gap2 pairs. Both negative states
are exercised; the g1 move at-2 correctly goes to-1. Terminal signs may be
negative while endpoint sums and full physical move bags remain exact.
CPU0.001968s,peakRSS17,440,768bytes. No search, repair or widened experiment.

Both predicted shortcuts fail with the correct input move bag: all-smaller
on the tight fixture ends at separation5>beta1/index15 outside M28; leaving
equal2 first at initial2 creates an immediate index collision. Unexpected
M32 fixture genuinely uses loads15/11, initial2/final-2, with endpoint index15
legal. B81's max-load<=n-2 is not inherited: the general bound here is n-1.
Scope and odd-jump controls behave as predicted. Outside-gap4 positions
(0,11,7,12) at M14 pass geometry and full input bag(11,5,-4,-12), so this
constructor's scope refusal is explicitly not nonexistence.

**Niggle sweep.** (1) Crossing could collide with older levels: strictly
max(previous level)<min(next level) orders ALL levels, not just same-prefix
indices. (2) Physical reflection is precisely equality of A/B indices;
same physical parity cannot reflect when M is even. (3) Negative-state
g1 orientation was checked separately. (4) Odd-gap scheduling exists when
initial2 and hazards occur: r0 would have forced initial1 by positive-owner
choice; each g1/g3 safely reaches magnitude1 from2. (5) Final sign is irrelevant
to max endpoint, but MUST be replaced by absolute value. (6) Necessity of
max odd jump<=M-3: jump M-1 uses a reflected endpoint pair. For doubled M-3,
the three possible edges start at0,1,2: the middle is a reflection pair, and
the outer two both use folded labels0/2. They cannot both occur in a folded-
distinct cycle. (7) Original owners and ALL moves were checked, as were
actual inventories, not only shape. All local niggles resolved; no self-check
upgrades this to PROVED or settles E28/L8.

**Step back, rather than merely try gap4 next.** Pairing imposes three
negative moves in each run for six negatives. That can itself be wrong:
M28,d=(2,2,2,2,5,11),p25/q23 is capacity-feasible (loads11/13) and has
legal positives, yet whichever pair assignment contains11 must add two
halves>=2, giving load>=15>n-1=13. Thus EVERY three-versus-three assignment
fails, regardless of the allowed pair discrepancy or pair order. This is a
hand obstruction to our equal-length-chain method, NOT to the target; its
actual E28 targets are(106,102,104,104,104,104,92,68). No new probe or
review request is opened for that observation. It identifies why mechanically
increasing the discrepancy cap would miss a structural obstacle. Unequal
numbers of moves in the two chains are the next useful change of picture.

Gut: delight in the crossing, and a more grounded pull toward unequal chain
lengths than toward extending a four-state table. Reasoned: B81's strict
interlacing becomes a sufficient subclass of a disjoint-level construction
for pair gaps<=3; the carrying infinite statement remains SKETCH. Fresh-choice
reflection is MI186 (90-minute reflection done early); next cheap question is
how to let one chain take several steps while the other takes one, retaining
both endpoint sums. No census or gap4 experiment. MI180 carrying read remains
pending/nonblocking, no new queue. Full E28/L8 and older held lanes unchanged.

Artifact cited/instinct/b82-crossing-pairs-4c05d480b3479729.json,7358bytes,
SHA256 4c05d480b34797291c72ae69b13491a25bffb25abbe86c0144207e09a2279045.
Prereg2574b6ff; source tests/probes/instinct/path_forest_crossing_pairs.py.
Immutable upload digest and manifest append receipts verified. No formal
proof number or novelty claim.


### MI188 — CL428/429 adopted: full-label and two-large contraction PROVED (2026-10-17 00:02 BST)

Fetched/merged b56152f1 and bf14dc84; read CL428/429 and all three changed
sources gcd1_small.py,mi180_check.py,reach_count.py. Cloud's carrying read
verifies BOTH MI180 theorems, including run/gap accounting, endpoint owners
and deletion preserving extrema. Adopt as PROVED in their precise scopes;
MI180's original SKETCH wording is historical. Counts28,303 constructions,
896 contractions/2,799 iff questions and corrected1,200 small-window cases
remain Cloud-reported, not rerun here. Label-count omission is corrected in
source. The reported91/6,788 reach and3,278 small-entry figures likewise
size the gap without becoming our independent measurements. B80-82 remain
SKETCH; no new independent read was given to them.

CL429's explicit chains A=(0,2,13),B=(1,6,8,10,12) have disjoint indices;
physical positions(0,25,15,11,7,3,26,4) have odd joins25/23 and negative
halves(5,2,2,2,11,2). Thus the equal-length obstruction is only a method
obstruction, as claimed; its reported74 total witnesses is not rerun.
The unequal chains/blank suggestion is welcome. Two literal accounting issues
need care before adopting the proposed distributed formula: at fixed occupied
word, inserting one blank INSIDE the first run changes(p,q) by(0,+2), not
(-2,+2); the latter is a LEADING blank. Also compaction need not preserve
the two-positive-odd sign pattern, although it always gives a binary word.
These are to be tested in MI189, not treated as rejection of the whole idea.
No review wait or new carrying-read request. The next block follows the general
word, not a gap4 sibling class.


### MI189 — B83: exact blank lifting on the gap-overlap tree (2026-10-17 00:02 BST)

**Question/pull.** Given an arbitrary binary skeleton, can the interior blanks
be allocated exactly, with no search, including unequal chain lengths? The
pull is toward a graph: consecutive gaps of each colour are nonoverlapping
intervals. A blank cut lies in at most one gap of each colour. The cuts that
cross BOTH colours make an overlap tree, so their weights should be forced
by leaf demands. This is a concrete step from a representation to an exact
fixed-skeleton lifting test; choosing a successful skeleton and gap assignment
remains OPEN, and no whole sparse theorem follows. Record searched:
blank.*account|gap.*forest|interval.*overlap.*tree ->3 unrelated record hits;
CL428/429 read explicitly. General tree leaf elimination is a standard tool,
not a new theorem of graph theory or a novelty claim.

**Exact equations, hand SKETCH/application.** Let w have L=N+2 letters,
each A or B and both colours present. Leading/trailing/internal blanks z_j
at cuts j=0..L total k, giving n=L+k. Occupied index i becomes
x_i=i+sum_(j<=i)z_j. Let a,b be first colour positions and u,v the last.
The physical odd joins (signed until checked) are
 P=2n-1-2(x_a+x_b), Q=2(x_u+x_v)-(2n-1).
Each skeleton gap e=(r,s) in one colour grows from s-r by
sum_(r<j<=s)z_j. This is an exact expansion of differences, including
one-point chains, not an assumption about a full-label positive solution.

One inserted blank changes the ordered odd joins by:
 leading(-2,+2), trailing(+2,-2);
 inside first run(0,+2), inside last run(+2,0);
 crossing both colours(+2,+2);
 separating the two monochrome runs(0,0).
These cases are determined by which minima/maxima lie beyond the cut, so
signed formulas apply even when a join changes sign. Every change is even;
odd parity alone is never the obstruction. A compacted word may have Q=-1;
final positive joins must be checked after lifting, not silently imported.

**Interior lifting criterion.** Now allow blanks ONLY at cuts crossed by a
gap of BOTH colours. Vertices are the individual A/B gaps; each allowed cut
is an edge between its two crossing gaps. For prescribed ordered target gaps,
let h_e=target_e-(s-r). A solution requires nonnegative integer edge weights
z with sum_(edges incident e) z=h_e. Also sum_A h=sum_B h=k, and the final
odd joins must equal desired(P0+2k,Q0+2k), positive. This system is necessary
and sufficient for THIS skeleton and gap assignment, by the exact index
formula. It does not assign an unordered bag or pick the skeleton.

**Why it is a forest and no blank search remains.** The common span of the
two colour chains is an interval of cuts. Move across it one cut at a time.
Crossing each occupied letter ends the old gap of that colour and starts a
fresh one; the other active gap is unchanged. A gap never returns after it
ends. Thus each new cut edge introduces a fresh vertex attached to the
previous edge's other vertex: no cycle, and the nonempty edge component is
a tree. Gaps outside this common span are isolated. Peel a leaf: its unique
edge weight MUST equal its residual demand; subtract it from the neighbour.
Reject negative residual/edge or nonzero isolated demand. If all residuals
vanish and sum weights=k, these forced weights are the unique lift. The
usual leaf induction proves uniqueness and sufficiency, including zero
weights/isolated zero vertices. Balanced totals alone are not sufficient.

**Predictions BEFORE code/run.** Six fixed-skeleton lifts:
1. w=ABABBBBA, A target gaps(2,11), B(5,2,2,2), k6: unique cut weights
 z3=3,z4=z5=z6=1, other cuts0. Recover CL429 A=(0,2,13),
 B=(1,6,8,10,12), M28,p25/q23; materialize the actual8-bin E28 target.
2. Same w, all demands0,k0: its original full-label gaps and13/11 joins.
3. Same w, twice the first demands,k12: A gaps(2,17),B(8,3,3,3),
 M40,p37/q35; no fixed6 deficit assumption.
4. w=ABABAB, A/B targets(3,3),k2: path edge weights1,0,1, M16,p13/q11.
5. w=ABBBBA, A(8),B(2,2,2),k3: unequal counts2/4, M18,p15/q13.
6. w=AABB, zero demands/k0: no interior cut edge; isolated demands0 accepted.
Independently compare every predicted ordered gap, endpoint and full physical
move bag; literal folded geometry is separate from the graph solver. Check
acyclicity by a separate union-find, not leaf success alone. No skeleton or
bag assignment search, profile census or permutation grid.

Six single-blank audit cases: w=AABB at each cut0..4, and w=ABAB at cut2.
Predict endpoint changes exactly the six-case table, and independently count
which actual gaps grow. Not all resulting signed cycles need have two positive
odd moves: that condition is tested separately. Counterfactual: if the first-
run change were(-2,+2), its full move bag would contradict these exact endpoints.

Kill controls: w=ABABAB, targetA=(4,2),targetB=(2,4),k2 has nonnegative
balanced demands but its tree forces a negative residual, so reject the
FIXED lift. The same global bag d=(2,2,4,4),M16,p13/q11 has a valid B79
sparse construction; check that separately, no false nonexistence inference.
Also w=AABB,targetA=(2),targetB=(2),k1 is refused for nonzero isolated demands.
Unexpected compaction check: compacted w=ABBBBBBB has P0=13,Q0=-1 at L8.
Leading4 blanks and one blank each at cuts6/7 give n14,A=(4),
B=(5,6,7,8,9,11,13), P9/Q7, negative halves(1,1,1,1,2,2).
This final actual E28 partition must pass; compaction has changed the sign
pattern. Do not call the compacted cycle a two-positive instance. Caps six
lifts/six single-cut audits/two refusals/one existing B79 positive control/
one compaction fixture (two actual E28 partitions),1CPU sec/64MiB. Stop on
any mismatch; retain failure, no repair or expanded skeleton enumeration.

Gut: warm, because blank placement becomes forced arithmetic on a tree,
while the difficult choice is clearly exposed rather than hidden in a solver.
Reasoned: this advances the distributed construction only for fixed skeletons;
we still need a general admission/selection argument, not more sample counts.
No new carrying-read queue or routine review halt.


### MI190 — B83: fixed-word blank allocation is forced; the universal interior recipe fails its budget (2026-10-17 00:04 BST)

**Exact fixed-skeleton lifting/application SKETCH; prescribed checks COMPUTED.**
Six lifts/six single-cut audits/two refusals/the existing B79 positive control/
the sign-changing compaction all pass; two actual E28 partitions pass both
literal/inventory checks. Cloud's unequal chains are recovered exactly by
weights z3=3,z4=z5=z6=1 (plus the zero edge z2). Zero-weight edges, isolated
zero demands, unequal chain counts and doubling the deficit from6 to12 are
all exercised. Independent union-find confirms the cut graph is acyclic;
physical coordinate differences match the entire original move bag, separate
from graph arithmetic. CPU0.001700s,peakRSS17,416,192bytes. No word/bag/order
search, repair or expanded experiment. General skeleton selection remains OPEN.

The balanced-demand shortcut really fails: ABABAB with A targets(4,2),B(2,4)
forces a negative neighbour residual despite nonnegative balanced totals.
B79's already-PROVED sparse method certifies the SAME global move bag at
M16,p13/q11,d=(4,4,2,2), so this is only a fixed-word/assignment obstruction.
Nonzero isolated demands are likewise correctly refused. Six cut audits give
exactly MI189's table. In particular first-run insertion changes(0,+2), not
the leading-blank(-2,+2). Compaction of the actual E28 sign fixture has
Q0=-1; leading4 blanks plus cuts6/7 restore positive joins9/7 and actual
partition targets(74,70,108,108,108,108,104,104). Thus every sparse solution
compresses to a word, but it need not compress to a TWO-POSITIVE full-label
instance. This does not challenge MI180's proved construction theorem.

**A decisive arithmetic limit on CL428's proposed universal recipe.** If all
k blanks cross both gaps, the compacted negative total is K0=K-2k. Its N
gaps are positive, so K>=N+2k. With ONE leading/trailing blank and k-1 such
interior blanks, still K>=N+2(k-1). At M28,N6,k6 this requires K>=18, or>=16
with the one end adjustment. The valid class d=(2,2,2,2,3,3),p15/q13 has
K14. It cannot be reached by the offered all-interior or one-end variant,
regardless of skeleton, ordering or parity. This is a structural counterexample
to that recipe AS STATED, not to general blank lifting or existence.
Existence here already follows from B80's explicit parallel chains: choose
first13, A=(3,5,7,10),B=(4,6,8,11); the eight physical positions
(6,19,15,11,5,20,14,10) have joins13/15, four gaps-4 and two gaps-6,
and disjoint folded labels. This is a hand check/application, no extra probe
or new proof entry. More single-chain cuts or more than one end blank are
needed by a general recipe; an odd-residue repair alone cannot fix total K.

**Niggle sweep.** A cut's coefficient follows which colour minima/maxima move,
so no end convention is guessed. At an interior two-gap cut both odd joins
grow2; at a separating cut neither grows, as independently tested. Each old
gap never returns during the left-to-right scan, so a newly added graph edge
cannot close a cycle; all other gaps are isolated, not silently discarded.
Leaf equations force a UNIQUE solution only for the fixed ordered demands,
not for an unassigned bag. Zero weights are allowed. All final joins are
checked positive where needed; signed audit cycles are labelled as such.
The sign-changing example has a one-point A-chain, handled by the general
endpoint formula rather than B79's minA0 implementation. The budget bound
uses N unchanged by insertion, unlike B79's refinement/deletion, which
changes the number of gaps. No universal criterion, coverage or novelty
claim; no independent status upgrade from these tests.

Gut: satisfaction rather than a eureka claim. The graph removed one search,
and the budget failure prevents another overly optimistic universal step.
Reasoned: exact fixed-skeleton interior lifting is settled at sketch level;
choosing skeleton/assignment plus boundary and single-chain blank budgets
is still the carrying inference. Next cheap step: combine the end/cut types
into a genuine feasibility condition that chooses how much of k is interior,
not another census of trees. Cloud receives the accounting corrections and
counterexample as one reply, not a new carrying-review queue or halt.

Artifact cited/instinct/b83-blank-tree-0ccc40c6c39454c5.json,7995bytes,
SHA256 0ccc40c6c39454c5edd9c35f666a152118e2c7dfe4fcba8b7f6c3540b4159c11.
Prereg4066824e; source tests/probes/instinct/path_forest_blank_tree.py.
Immutable upload digest and manifest receipts verified. MI180 PROVED via
CL428/MI188; B80-83 SKETCH, full E28/L8 OPEN, older holds unchanged.


### MI191 — B84: contract only the necessary deficit; pad the rest at the ends (2026-10-17 00:14 BST)

**Question/pull.** Can the proved MI180 construction use a SMALL contraction
in a smaller window, leaving the remaining unused labels outside both chains?
The label deficit k need not equal the number of deletions. This is the useful
boundary-budget choice: let r absorb the excess negative total, then use
leading/trailing padding for k-r. It reaches the K14 counterexample to CL428's
all-interior recipe without a new word/assignment search. Record searched:
partial.*contract|contract.*padding|outer.*blank ->0 hits, including ledgers.
MI180/188-190, CL428/429 read. Dependencies are the independently verified
MI180 constructions; the new selection/padding argument stays SKETCH.

**Proposed sufficient theorem and exact construction.** Given M=2n, N>=1
positive negative halves d_i with K=sum d, odd positives p,q, p+q=2K,
N+2<=n, max(p,q)<=2n-3, not p=q=2n-3. Put
 k=n-N-2, r=max(0,ceil((K-2N)/2)).
If r=0, no large-half condition is required. If r>0, require TWO distinct
halves D,E>=r+2. Then a folded-distinct cycle exists. This is a sufficient
class, not the full sparse criterion. Half1, unequal chain lengths and
arbitrary N are allowed. No anchors/other odd sign patterns or E28/L8 solution.

First r<=k: the legal odd positives/non-doubled bound implies K<=2n-4,
so K-2N<=2k. Form a core window n_c=N+r+2, and s=k-r outer blanks.
Its legal largest odd jump is C=2n_c-3=2(N+r)+1. By choice of r, K<=C-1.
For r>0 the two-large assumption also guarantees the refined list has enough
positive mass; refine D by r as MI180 prescribes. For r0 the core is exactly
full-label. What remains is to choose its two odd joins before using MI180.

Choose x in the intersection of odd intervals
 I=[L,U]=[max(1,2K-C),min(C,2K-1)],
 J=[p-2s,p+2s], with x congruent p-2s mod4;
set y=2K-x. For K>=2, I contains at least TWO consecutive odd values:
its width is 2K-2 or2C-2K, each>=2. I and J intersect: p<=C+2s and
q<=C+2s give their cross bounds; p,q>=1 give the other bounds. For s0,
x=p is available. For s>0, J's endpoints have the required mod4 residue.
Their intersection cannot be a lone WRONG-residue odd point: then neither
end could come from J, forcing I itself to be that singleton, a contradiction.
With two odd points one has the required residue. Algorithm: a=max(L,p-2s),
b=min(U,p+2s); take x=a if it has the residue, otherwise a+2. No search.
Thus x,y>0, both<=C, not both C because K<=C-1.

Use MI180 in the core: full-label for r0; sparse contraction for r>0, with
the admitted D,E first. MI180 starts its LARGER odd join, so if x<y swap BOTH
core owners and their corresponding original p/q. Write core first P0,
original matching first P. Then t=(P-P0)/2 satisfies |t|<=s and t=s mod2.
Put ell=(s-t)/2 leading blanks and rho=(s+t)/2 trailing blanks. Both are
nonnegative integers. Add ell to every core A/B index; enlarge n_c to n.
All indices remain in range and disjoint. The new odd joins are
 P0+2s-4ell=P and Q0+4ell-2s=the other original positive.
Every negative gap is unchanged; hence the full original move bag is exact.
This includes owners swapping and either outer blank count being zero.
If K1, necessarily N1,d1,p=q1: use positions(0,1,2) directly for every n>=3.
That tiny exception avoids pretending the singleton interval I has both residues.

**Why this r is the right budget for THIS composition.** A smaller core
contraction r' would leave N+r' negative halves in its full-label parent.
The legal/non-doubled core bound forces K<=2(N+r'), so r'<r cannot work
in this family even if the word and odd owners are changed. This is not a
necessity claim for all folded cycles. The old two-large rule unnecessarily
used r=k; now only the excess above2N must be absorbed by contraction.

**Predictions BEFORE code/run.** Exactly12 formula calls,6 actual M28 E28
partitions with original slots(1,1,2,2,2,2,2,2):
 d=(2,2,2,2,3,3),p15/q13 and21/7 (r1,s5);
 d=(1,1,2,2,4,4),p19/q9 (r1,s5);
 d=(1,1,2,4,4,4),p23/q9 (r2,s4);
 d=(1,1,3,3,5,5),p25/q11 (r3,s3);
 d=(8,8,2,2,2,2),p25/q23 (r6,s0, old theorem regression).
The first FIVE fail the old second-largest>=k+2 admission but must now pass.
The first fixture swaps the original positive owners, has ell3/rho2; the
fourth/fifth have one-sided padding. Direct complete input move bags,
original owners, every folded label, window bounds and both independent
partition validators must agree; core contraction records are retained.

Six general calls: M6/M8,d=(1),p=q1 (tiny exception);
M10,d=(2),p3/q1 (r0); M20,d=(2,2,3,3),p13/q7 (r1);
M60,d=(8,8,1,1,1,1,1,1,1,1),p45/q3 (N10,r2,s16);
M22,d=(1,1,2,2,2,2,3,3),p17/q15 (N8,r0,odd s1 and owner swap).
These test sparse/full cores, arbitrary N, units, both interval residues,
small K and padding much larger than the contraction. No parameter grid.

Kill controls: M28,d=(2,2,2,2,2,7),p19/q15 has r3 but second-largest2<5;
refuse ONLY this constructor. Explicit unequal chains A=(0,7,9),
B=(4,6,8,10,12),positions(0,19,15,11,7,3,18,14) must pass literal geometry
and full input move bag, so no global refusal is inferred. Refuse doubled
longest M28,d=(2,2,2,2,8,9),p=q25 and overlong p27/q1 on the first d.
Identified unexpected check: ignore mod4 on the first fixture, use core
joins15/13 instead of the selected13/15, and floor the two half-integer
outer counts to ell2/rho3. The result remains geometrically valid but its
odd joins are17/11, not15/13. The original move-bag checker must reject it.
This is a counterfactual to treating mod4 as bookkeeping. Caps12 calls/6
partitions plus named controls,1CPU sec/64MiB. Stop on mismatch/cap; no repair,
core-word search, profile enumeration or raised admission condition.

Gut: warm because most holes can be harmless space OUTSIDE the core, rather
than a demand every small gap must absorb. Reasoned: the selector's parity,
positive-owner swap and exact core threshold carry the argument; examples
will not replace them. This is a new composition of proved constructions,
not another census or a general solution. A useful carrying read would target
that selector and padding, without rereading MI180; do not halt for it.


### MI192 — B84: partial contraction plus outer padding passes; only the true excess needs absorption (2026-10-17 00:17 BST)

**General sufficient theorem SKETCH;12 prescribed calls COMPUTED.** All12
calls and6 actual E28 partitions pass both literal/inventory validators.
The first five actual cases fail MI180's old second-largest>=k+2 admission,
but their smaller contraction budgets1,1,1,2,3 work, with remaining5,5,5,4,3
blanks outside the core. The sixth is the original full r=k6 construction.
Original owner flips occur, including first fixture15/13 starting with13,
and N8's full-core odd-padding case17/15 starting with15. Either padding
side can vanish; N10 uses contraction2 and outer padding16, so the argument
is not fixed at six negative halves or a small label deficit. Unit halves
and the two tiny K1 exceptions pass. CPU0.002820s,peakRSS15,527,936bytes.
No core/order search, widened family, census or numerical coverage claim.

The unexpected wrong-residue control remains geometrically valid but changes
requested odd joins15/13 into17/11; exact input move-bag comparison rejects
it. Overlong/doubled-longest controls are refused. The second-large threshold
refusal is constructor-only: M28,d=(2,2,2,2,2,7),p19/q15 has an independently
checked explicit unequal-chain witness outside our admission. Its existence
is not contradicted by this construction's refusal. No cap failures/repairs.

**What changed.** We need not distribute ALL k holes through small negative
gaps. The smallest legal core needs only r=max(0,ceil((K-2N)/2)) contractions;
the remaining k-r holes can be at the ends, with exact positive owners chosen
by an interval/mod4 argument. The new two-large condition is r+2, not k+2;
for r0 there is no large-half condition at all. This extends the independently
PROVED MI180 mechanism and directly handles the K14 class that disproved the
all-interior/one-end recipe. It does not select a skeleton for EVERY feasible
bag: lists with fewer than two admitted large halves remain outside. Old
B81/B82 mechanisms retain separate scopes. Full E28/L8 OPEN.

**Niggle sweep.** (1) Is the intersection secretly empty? Its cross bounds
are exactly the two GLOBAL legal odd-jump bounds, and p,q>=1 handle its
other ends. (2) Could the residue be absent? If the intersection has two
odd values it contains both residues. A lone wrong-residue point could
come from neither endpoint of J (both have the right residue), forcing the
whole intrinsic interval I to be a singleton; K>=2,K<=C-1 rule that out.
K1 is handled separately, not rounded. (3) Does larger-first ownership
break the target? Swap the ORIGINAL owner with the core owner as well;
t becomes -t, so its parity and bound survive. Direct bags test this.
(4) Are half-integer outer counts possible? t=s mod2 makes both integral;
the deliberately rounded countercontrol changes the target. (5) Does padding
change reflection labels? In reflected index coordinates it translates BOTH
chains by ell, preserving disjointness, with ell+rho=s proving the window
bound. Physical positions need not be a common translation; the positive
joins have been recomputed explicitly. (6) Does this reuse an unreviewed
claim? The only construction dependency is MI180 PROVED by CL428; the new
selector/padding remains SKETCH pending its own carrying read. (7) Is r a
universal lower bound? Only for this core/full-label-parent composition; the
outside-admission positive is retained to prevent a global inference.

Gut: delight at recovering harmless outer space instead of forcing every
hole into a gap. Reasoned: this moves the constructive admission condition,
with the interval proof carrying the result. Next useful obstruction is the
one-large-half case (and more general distributed interior growth), not a
larger family census. Request ONE focused carrying read of MI191's interval,
owner swap and padding; no reread of MI180 and no review halt. Continue
independent work on what the admission still misses. No new experiment here.

Artifact cited/instinct/b84-partial-padding-496b51fd8b795a09.json,11230bytes,
SHA256 496b51fd8b795a09bc6bec999efa3d6cce78973fa2d17ab1c29e11f91fb8634b.
Preregb4fb6292; source tests/probes/instinct/path_forest_partial_padding.py.
Immutable upload digest and manifest receipts verified. No formal proof number,
novelty claim, broader solution or automation/held-lane change.


### MI193 — B85: one large gap can merge across several small runs (2026-10-17 00:27 BST)

**Question/pull.** Can the other small gaps SHARE the contraction capacity?
Yes at sketch level: split D into several nonunit pieces, then delete the
first r A-vertices after0 to merge those pieces back into D. The other colour
never moves, so its many small gaps survive. This differs from MI182's failed
prefix-only refinement D_i-r_i plus units: here ONE D is split into several
nonunit gaps and their intermediate A vertices disappear. An odd total gives
one endpoint unit as well. Record searched: refin.*consecutive.*gap|
distributed.*contract|several.*small.*gap ->5 hits/5 files; relevant MI182's
failed budget, Cloud reach_count, otherwise unrelated. MI180,191-192 and
CL428/429 read. No census or resurrection of the refuted prefix-only scheme.

**Distributed sufficient construction, hand SKETCH.** Use MI191's legal
setup, k=n-N-2,r=max(0,ceil((K-2N)/2)),s=k-r. r0 uses MI191's full core
and padding. For r>0, let epsilon=K mod2. Take D as a largest half; sort the
other halves E>=2 decreasingly (unit halves remain in the rest). Let t be
the smallest prefix count with sum_(i<=t)(E_i-1)>=r+1-epsilon. Require
 D>=r+t+1.
This replaces the previous single E>=r+2 condition by shared capacity. If
there is no such prefix or D is smaller, refuse THIS construction only.

In the minimal core n_c=N+r+2, K is either2(N+r) (even) or2(N+r)-1 (odd).
Set U=r-t+1-epsilon>=0. Refine D into t nonunit pieces
 f1=D-r-t+1>=2, f2=...=ft=2,
and U+epsilon units. Their count is r+1 and sum D. Keep all other original
halves. The full-label parent has N+r gaps. Choose its internal-run order
 f1,E1,f2,E2,...,ft,Et, then all remaining original nonunit halves.
Every f_i-run is B, every E_i-run A. Use initial A-run of length1+epsilon
and final run of length1. Its two positive joins are
 (K+1,K-1) if epsilon0; (K,K) if epsilon1,
exactly the MI180 full-label construction in both cases. Thus this step uses
a PROVED arbitrary-internal-order theorem, not an unreviewed placement guess.

Delete the FIRST r A-indices after0, preserving0. Minimal t ensures the final
selected E_t-run retains a point: its prefix has r+1-epsilon available points
in total and fewer than that before the last run. If epsilon1, the first
removed point is the extra initial A-index1. The merged first A-gap consists
of the t f_i, U internal units and epsilon initial unit, hence has size D.
These are exactly r+1 parent gaps; replacing them by one removes r vertices.
Every other A-gap is untouched. Every B-gap keeps its positional distance,
including all E_i despite deletion of their internal A points. Neither colour
minimum/maximum changes (the last selected A-run retains a point), so both
odd joins survive and all folded labels remain distinct. This gives the
original gap bag in a core with deficit r.

**Endpoint choice and reversal, carrying step.** MI191's interval/residue
selector chooses a desired core pair(P0>=Q0). For even K this is necessarily
(K+1,K-1), already built. For odd K it is either(K,K) or(K+2,K-2).
In the latter case reverse BOTH index chains i -> n_c-1-i. With endpoint
sums, this changes ordered joins(P,Q) to(Q+2,P-2); balanced(K,K) therefore
becomes precisely(K+2,K-2). Disjointness and negative gaps survive. A chain
need not start at0 after reversal; use the GENERAL endpoint formula. Then
apply MI191's owner-aware leading/trailing padding to get original p/q.
The new merging/reversal steps are SKETCH; the selector/padding remains
MI191 SKETCH pending its independent review. No dependency is silently upgraded.

For t1, even K recovers the old two-large condition. Odd K additionally uses
one initial unit, allowing E1>=r+1 instead ofr+2. More importantly t>1 lets
several modest E's share the budget. The one-large example d=(7,2,2,2,2,2),
p19/q15 has r3,epsilon1,t3,D7 meeting D=r+t+1; the old second-large rule
failed. The fixed-core split chooses which colour owns each gap jointly.
General sparse/E28/L8 are not solved; both the shared-capacity and D bounds
are constructor admissions, not universal necessities.

**Predictions BEFORE code/run.** Exactly12 formula calls; six actual M28
partitions under original slots(1,1,2,2,2,2,2,2):
 d=(7,2,2,2,2,2),p19/q15 and25/9;
 d=(8,2,2,2,2,2),p25/q11;
 d=(7,3,2,2,2,2),p23/q13;
 d=(6,3,3,2,2,2),p19/q17;
 d=(8,3,2,2,2,2),p25/q13.
All SIX miss B84's second-largest>=r+2 condition but must now pass.
The first needs epsilon1 and t3; with epsilon0 it would require t4 and
D>=8, so no pretending the extra initial unit is optional. The second and
sixth require index reversal from balanced core to(K+2,K-2); cases3-5 use
even K, with t4,t3,t2 respectively. Original positive owners must survive.

Six other calls: M12,d=(3,2),p7/q3; M10,same input (zero outer padding,
reversed core); M40,d=(11,3,3,3,2,2),p35/q13;
M100,d=(17,2,2,2,2,2,2,2,2,2),p61/q9 (N10,r8,s30);
M22,d=(1,1,2,2,2,2,3,3),p17/q15 (r0 MI191 regression);
M28,d=(8,8,2,2,2,2),p25/q23 (t1, full r=k regression, no partition needed).
Compare full physical move bags independently of the parent-gap merge,
all folded labels/window/endpoints and original owners; retain parent,
deleted indices, merged gap and any reversal. Both actual partition validators
must pass. No word/permutation/profile grid or replacement search.

Kill controls: d=(5,3,3,3,2,2),M28,p19/q17 has D5<r+t+1=6, so refuse this
constructor. Existing B82 crossing-pair construction must pass literal full
bag for the SAME target, proving the bound is not global necessity. A second
refusal d=(11,1,1,1,1,1),M28,p19/q13 has no eligible E; its explicit chains
A=(0,11),B=(4,5,6,7,8,9),positions(0,19,17,15,13,11,9,22) pass geometry and
full bag. Identified unexpected check: on the first new fixture, delete r+1
rather than r A-indices. It remains folded-distinct, keeps BOTH odd joins
and total negative mass K, but replaces gaps(7,2,2,2,2,2) by(9,2,2,2,2).
Even checking endpoints and mass is insufficient: full original move bag
MUST reject it. Caps12 calls/6 partitions/two admission refusals with their
positive controls/one over-deletion control,1CPU sec/64MiB. Stop on mismatch;
retain failure, no repaired search or raised bound.

Gut: warm surprise at merging NONUNIT refined gaps, and at the one spare
endpoint position doing mathematical work. Reasoned: this genuinely crosses
the one-large admission that motivated the block, but not every one-large
list. MI191's carrying read remains the priority; no added review queue or
review halt. A next step would examine what this shared-capacity gate still
misses, not count how many sample targets it covers.


### MI194 — B85: several small runs share one contraction; endpoint unit and reversal both work (2026-10-17 00:30 BST)

**Distributed sufficient construction SKETCH;12 prescribed calls COMPUTED.**
All12 calls and6 actual E28 partitions pass. All six new actual cases fail
MI191's single second-large admission but satisfy the shared-capacity gate.
The former outside-admission d=(7,2,2,2,2,2),19/15 is now constructed, and
its25/9 variant exercises the reversed balanced core. Even-total examples
share over4,3,2 small runs; the last actual odd-total example also needs
reversal. Tiny windows, zero outer padding, N10 with r8/s30, r0 and t1
regressions pass. CPU0.002849s,peakRSS18,489,344bytes. No repaired case,
expanded family, word/order search, profile survey or coverage extrapolation.

The over-deletion control does exactly what was predicted: geometry,
positive joins19/15 and total negative mass17 all remain valid, but six
halves(7,2,2,2,2,2) become five halves(9,2,2,2,2). The full original bag
rejects it. Both admission refusals have literal positive controls: the
D5 insufficient-budget case is covered by B82; the all-unit-companion case
has its explicit unequal-chain witness. Thus neither refusal is a global
obstruction. No environmental/cap failure or silent repaired hypothesis.

**Carrying audit/niggles.** Minimal t implies t<=r+1-epsilon and therefore
U>=0. Before the last E-run, at most r A-points after0 are available; across
that run at least r+1 are, so deleting exactly r keeps a later A-point and
both extrema. The merged prefix consists of precisely t f-pieces, U internal
units and epsilon initial unit: r+1 positive gaps summing D. None of the
original E-gaps moves; they are distances between B-points, not counts of
A-points between them. Original unit halves may be indistinguishable from
refined units, but complete gap multisets (not ancestry labels) are preserved.
For epsilon1 the minimal core has K=2(N+r)-1, so its balanced joins are K/K,
initial run2/final run1. Reversing both index lists gives(Q+2,P-2), as checked
from min/max sums; treating it as a plain exchange P/Q would be false.
After reversal the general endpoint formula is used, not minA0. Original
positive owners and exact full move bags are checked again after outer
padding. All local niggles tipped on these checks. Dependencies stay honest:
MI180 PROVED; MI191 selector/padding and this new merge/reversal SKETCH.

**What changed.** The contraction can now be supplied by several modest
opposite-colour runs, while one large D merges across them. This is a real
distributed refinement of ONE gap, unlike the failed prefix-only scheme in
MI182. The odd core's single endpoint unit is used explicitly; without it
the motivating D7 example would fail our own budget. The sufficient class
still has a D-size/shared-capacity gate; no arbitrary capacity-feasible list
or full E28/L8 theorem is claimed. In particular d=(11,1,1,1,1,1) has no
eligible E even though its explicit cycle works.

Gut: warm because the question that motivated the block changed from an
admission failure to a construction, with the mistaken-overdeletion control
showing why exact gaps matter. Reasoned: the remaining unit-companion case
suggests placing a consecutive block INSIDE a long gap and using the two
ends as free variables, rather than forcing unit gaps to provide deletion
capacity. That is the next cheap geometric question, not a new experiment
or claim here. Keep MI191's carrying read as the one priority; send this
as READ-LEDGER, no extra review queue/halt. Full E28/L8 and old holds unchanged.

Artifact cited/instinct/b85-shared-contraction-f6acd01680a04588.json,14907bytes,
SHA256 f6acd01680a04588b20faf398cb141957206442d6c0ddf40276400cac11e6ac2.
Preregbfe20e26; source tests/probes/instinct/path_forest_shared_contraction.py.
Immutable upload digest and manifest receipts verified. No formal proof number
or novelty claim; schedule remains13min.


### MI195 — B86: a consecutive unit block fits inside one long gap (2026-10-17 00:39 BST)

**Question/pull.** Unit companions provide no deletion capacity, but they form
one consecutive block. Put that block BETWEEN the two endpoints of the long
gap and solve for its two margins. This direct geometry is simpler than a
refinement and independent of MI191's pending selector/padding. Record
searched: unit.compan|consecutive.*block.*gap|one.large.*unit ->14 hits/9 files,
relevant MI180's saturated one-large calibration and MI194's explicit outside-
admission witness. No imported theorem or novelty/literature-status claim.

**Complete criterion IN THIS CLASS, hand SKETCH.** Let M=2n, N>=1,D>=N+1,
negative halves(D,1 repeated N-1), and odd positives p,q with
p+q=2K=2(D+N-1). A folded-distinct cycle exists IFF
 max(p,q)<=2n-3 and D<=n-1.
The label count N+2<=n follows from D>=N+1 and D<=n-1. Also K<=2n-4,
so doubled longest positives cannot arise under these assumptions. Necessity:
the longest odd jump2n-1 is a reflected endpoint pair (larger cannot fit),
and negative even jump-2D requires2D<=2n-2. This is a two-positive-odd class
with no anchors, not general E28/L8 or a universal negative-bag criterion.

If D=N+1, K=2N is even, so p/q have opposite residues mod4. Choose FIRST
positive P congruent2n-3 mod4 (possibly the smaller input). Otherwise choose
P=max(p,q). Let Q be the other. In both cases Q<=2n-5: in the boundary case
it cannot have2n-3's residue; in the strict case both equal2n-3 would force
K=2n-3, contradicting K<=2n-4. Put
 alpha=(2n-1-P)/2, H=n-1-D, Bmax=D-N.
Then1<=alpha<=2H+Bmax, since Q<=2n-5 gives
alpha<=2n-3-K=2H+Bmax. We need2a+b=alpha with
 0<=a<=H, 1<=b<=Bmax.
Choose b=min(Bmax,alpha); if b has the wrong parity, decrease it by1;
then a=(alpha-b)/2. At Bmax1, the boundary owner choice made alpha odd,
so b1 works. At Bmax>=2, decreasing cannot give b0: b1 would have meant
alpha1, already the right parity. If alpha<=Bmax, a0. Otherwise
alpha-Bmax<=2H; if its parity is odd it was at most2H-1, so reducing b by1
still leaves a<=H. Thus the formula always gives integer a,b in range.

Take A=(a,a+D), B=(a+b,a+b+1,...,a+b+N-1). They are disjoint because
 A0<B0<=...<=Bend<Aend;
Bend<=a+(D-N)+(N-1)=a+D-1. All indices fit0..n-1. The A-gap is D,
the N-1 B-gaps are units. Endpoint sums are
 minA+minB=2a+b=alpha,
 maxA+maxB=alpha+D+N-1=alpha+K.
Physical even2A/odd(2n-1-2B) therefore have odd joins EXACTLY P,Q and
negative bag(-2D,-2 repeated N-1), with every folded label distinct. No
refinement, search, unreviewed construction dependency or capacity guess.
The two free margins directly solve the endpoint budget.

For D<N+1 this INNER-block construction is out of scope. The low-mean
K<=2N branch is covered by MI191 (SKETCH pending review), but not used to
prove the independent large-D result here. Constructor refusal outside the
class is not nonexistence. The old all-unit-companion D11/N6 witness is now
one member of an arbitrary-N/D theorem rather than a standalone repair.

**Predictions BEFORE code/run.** Twelve formula calls, six actual M28 E28
partitions (N6,slots1,1,2,2,2,2,2,2): D11 at19/13 and25/7; D10 at17/13;
D9 at15/13; D8 at19/7; D7 at15/9. Each uses original halves(D,1,1,1,1,1).
The D7 boundary MUST start with the smaller9. Materialize with original
positive/negative owners and pass literal/inventory checks. Independently
compute the physical full move bag, every folded label/window bound, and
strict containment of the B-block between the two A points.

General calls: M6,N1,D2,p3/q1; M8,N1,D3,p3/q3;
M16,N6,D7,p13/q11 (zero slack/full-label boundary);
M20,N4,D6,p11/q7; M14,N3,D4,p7/q5 (other M mod4 boundary);
M100,N10,D35,p47/q41 (must adjust b25 DOWN to24 for parity, then a1).
These include triangles, D=n-1, either window residue, zero outer slack,
nonzero translations and arbitrary N. No magnitude/profile grid.

Kill controls: M20,N4,D10,p15/q11 has legal odd jumps but D>n-1, so reject;
M28,N6,D11,p27/q5 has a folded-loop odd jump, reject. Refuse inner-class
M28,N6,D5,p13/q7 only for scope; MI191's existing r0 construction must pass
the SAME bag independently as a positive control. Wrong owner at boundary
D7/15/9: taking15 and flooring a to2 with b1 is geometrically valid but
produces17/7, not15/9; full original bag must reject. Identified unexpected
check: in M100 omit the parity adjustment and floor a0,b25; it is still
folded-distinct but changes47/41 to49/39. Endpoint sums AND exact input bag
must catch this, rather than accepting a nice nested picture. Caps12 calls/
6 partitions+named controls,1CPU sec/64MiB. Stop on mismatch/cap, no repaired
translation search, family expansion or follow-up census.

Gut: satisfaction at an independent short proof, with warmth tied to the
specific geometry rather than a new case count. Reasoned: this resolves the
named large-gap/unit-companion obstruction; remaining mixed companions need
a separate argument. MI191 remains the one carrying-read priority. Send the
new result as READ-LEDGER, no extra review queue or review halt.


### MI196 — B86: nested unit block gives an independent complete large-gap criterion (2026-10-17 00:41 BST)

**Class iff SKETCH;12 prescribed calls COMPUTED.** All12 calls/six actual
E28 partitions pass, with the full original move bags and both partition
validators. The boundary D=N+1 correctly starts with smaller9 on input15/9.
D=n-1, triangles, full-label/zero-slack boundary and the other window residue
are exercised. M100 requires the predicted b25->24 adjustment and a1.
CPU0.001828s,peakRSS15,273,984bytes. No search, repaired translation, expanded
family or numerical coverage claim; the theorem is a hand argument in MI195.

All controls pass. Negative-bound and folded-loop-positive cases refuse;
the low-D input is outside the inner-block class but has its independently
checked MI191 r0 witness. Wrong boundary owner/flooring keeps geometry but
changes15/9 to17/7. Omitting the strict-case parity adjustment likewise keeps
the nested picture and folded labels but changes47/41 to49/39. The original
move bags reject both. Thus neither residue choice is cosmetic. No cap or
environmental failure, and a constructor scope refusal is not nonexistence.

**Niggle sweep.** The negative bound D<=n-1 also gives enough labels because
D>=N+1. These two inequalities force K<=2n-4, excluding doubled longest
positives without an extra assumption. Strict-case smaller Q cannot equal
2n-3; boundary Q has the other mod4 residue. Thus the upper alpha bound is
valid even when the first positive is the smaller original owner. At inner
slack1, alpha is odd; at slack>=2, parity adjustment cannot lower b1 to0.
When alpha exceeds the inner slack, an odd excess is at most2H-1, so the
extra adjustment still leaves a<=H. Strict B-block containment excludes every
A/B index equality, including endpoints, and therefore all physical reflection
collisions. Both physical endpoint sums recompute the ORIGINAL odd jumps;
full move-bag and labelled inventory checks make that independent. N1 is
handled as a one-point B-chain; the formula and labels still work. No step
uses MI191 or MI180 as a construction dependency; only generic validation
code is reused. Infinite claim remains SKETCH until its own carrying read.

**What changed.** For one half D and N-1 unit halves, D>=N+1, the only
requirements are the legal odd-jump bound and fitting the long negative
jump: max(p,q)<=2n-3,D<=n-1. This arbitrary-N/D result replaces the earlier
standalone all-unit-companion witness, and complements shared contraction,
which has no E>=2 to use in this case. The D<N+1 branch is outside this
independent proof (MI191's low-mean construction addresses it at SKETCH
status). General mixed companion gaps and E28/L8 remain OPEN.

Gut: satisfaction at the shorter direct geometry, and a new pull toward
whether the inner chain needs unit spacing at all. Reasoned: the proof used
its total span and strict containment; next cheap question is whether an
arbitrary positive-gap prefix chain of span S can replace this block under
a dominant-gap bound, with boundary/parity choices rechecked. No broader
claim or experiment is opened here; respect the preregistered unit class.
MI191 remains the sole carrying-read priority; send one READ-LEDGER update,
no new review queue or halt. Old lanes and13-minute schedule unchanged.

Artifact cited/instinct/b86-unit-block-0740a2cc1c643be4.json,5484bytes,
SHA256 0740a2cc1c643be4740343f2a0a6cd416390866e5347261b5cb63a6365c45aca.
Preregf150f935; source tests/probes/instinct/path_forest_unit_block.py.
Immutable upload digest and manifest receipts verified. No formal proof number
or novelty claim; full E28/L8 OPEN.


### MI197 — B87: span extension, then audit the assembled mechanisms instead of adding siblings (2026-10-17 00:52 BST)

**Question/pull and step-back.** The unit spacing was irrelevant: MI195's
inner chain only needs its total span. That is a short generalization, not
another family grid. The stronger pull now is to ask what our assembled
mechanisms STILL miss, before producing more siblings. This block is an
admission audit on Cloud's already-surveyed domain, NOT another existence
survey or a proof upgrade. It will select the next structural question.
Record searched: dominant.*gap|mechanism.*admission|admission.*cover ->21 hits/
7 files, relevant MI196's next question; other hits unrelated. MI177,180,
191-196 and Cloud's reach_count.py/CL428 scope read. No cycle solver or
Cloud survey is rerun, and reported existence counts are not our certificates.

**Span extension, hand SKETCH (same MI195 carrying argument).** Let one half
D have remaining positive halves with total S and D>=S+2. The folded-cycle
criterion is exactly legal odd positives p+q=2(D+S),max(p,q)<=2n-3 and
D<=n-1. Label count follows since S>=N-1 implies D>=N+1. Set
W=D-S-1>=1,H=n-1-D. At W1, K=D+S is even: choose first P=2n-3 mod4;
otherwise choose max(p,q). The other Q<=2n-5 and
1<=alpha=(2n-1-P)/2<=2H+W. Set b=min(W,alpha), lower it by1 if parity
requires, a=(alpha-b)/2, exactly MI195's proof. A=(a,a+D),
B=a+b+prefixes(other halves IN ANY ORDER). Span S makes the whole B-chain
strictly inside A's endpoints, and min/max sums give p/q. No unit-spacing
assumption remains. This is an independent hand SKETCH, no separate proof
number/review queue and no broad new geometry experiment.

**The synthesis experiment, predictions BEFORE code/run.** Use only the
fixed CL428/429 domain: M28,1<=N<=6,sorted halves1..11,14<=K<=24, with a
13/13 two-bin split; odd positives p<=q<=25,sum2K. K25 contributes only
doubled25 and is excluded. Predict EXACTLY6,788 questions, matching Cloud's
REPORTED count; here the domain/count is rederived without calling its
exists_cycle function. No claim of fresh existence verification. At most
12,375 input profiles,5CPU sec/128MiB. Stop on count/method mismatch or cap;
no larger domain, cycle search, repaired admission or follow-up run.

For each eligible negative profile evaluate the recorded admissions only:
- MI175 PROVED gcd>=2 (capacity already checked);
- MI177 SKETCH: g>=3, exactly two nonmultiples whose sum is0 modg, and
  their combined atom admits13/13 capacity. g3..22 suffices: their sum<=22;
- MI186 SKETCH: even N,min half>=2, sorted consecutive pair gaps<=3;
- MI191 SKETCH: r0 or second-largest>=r+2;
- MI193 SKETCH: sorted shared-capacity gate with epsilon=K mod2;
- the dominant-span extension above, SKETCH.
Keep overlapping tags, count their UNION without adding overlaps; count
PROVED-only admission separately. Include MI180's old k+2 admission as a
subset control, not a new mechanism. Store the COMPLETE eligible/residual
profile lists, legal positive pairs and admission reasons. A residual is
UNRESOLVED BY THESE METHODS, never UNSAT. No construction is run for every
profile, no status changes and no global E28 coverage inference.

Independent control: enumerate the same fixed-sum partitions recursively
rather than by combinations-with-replacement, and check capacity by explicit
subset-sum SETS rather than a bitset. The complete eligible profile sets and
weighted question counts must agree. Verify old k+2 subset of MI191 subset
of MI193; a literal unit-large class admitted by MI195 must also be dominant.
These are checks on admissions, not self-verification of the infinite claims.

Predicted residual control: sorted d=(2,2,3,4,4,9),K24,legal pair23/25,
should be admitted by NONE of the above. It has13/11 capacity via9+2+2,
but fixed sorted pairs force each chain to take one of each pair, making
one run sum9,10,14 or15: never11..13. Thus simply raising the sorted-pair
gap cap would not fix its load mismatch. Nonetheless explicit chains
A=(0,2,11,13),B=(1,5,9,12),physical(0,25,17,9,3,26,22,4) have the full
original move bag. This is the identified unexpected residual-positive check:
materialize this ONE E28 partition and pass both checkers while keeping it
RESIDUAL to the existing admissions. It is a diagnostic, not a new class.

Second literal control: mixed-companion dominance d=(11,3,2,2,1,1),25/15,
A=(0,11),B=(1,4,6,8,9,10),positions(0,25,19,15,11,9,7,22) must pass full
physical bag/labels and its actual E28 partition, and carry the dominant tag.
Exactly two actual partitions; no unit-only inference in this mixed control.

Counterfactual: expect a NONEMPTY residual, so the output should prevent a
false 'we have the criterion' conclusion. If empty, publish only a finite
admission-cover CANDIDATE with its SKETCH dependencies, and seek independent
verification; do not claim a proved criterion/full E28. If the predicted
residual gains a tag, stop and audit that tag rather than silently changing
the control. No seeded draw or output quota. Gut: a useful step-back from
proliferation; reasoned: the result should identify the carrying selection
obstacle, not create another review queue. MI191 read remains nonblocking.


### MI198 — B87 outcome: selected admissions leave a small-core question (2026-10-17 00:58 BST)

**COMPUTED admission audit, not existence verification.** All prescribed
checks pass. The fixed CL428 domain has12,375 input profiles,2,173 eligible
profiles and6,788 positive-pair questions. Independent fixed-sum recursion
and subset-sum sets agree with the complete eligible set and weighted count.
The UNION of the six selected mechanisms admits1,587 profiles/5,266 questions;
586 profiles/1,522 questions remain outside this inventory. Only476 questions
have the PROVED gcd tag; all other selected mechanisms are SKETCH. This is
neither a count of proved solutions nor an inventory of every result in the
record. No cycle/existence solver was imported or run. Old MI180 single-pair
full-k admission gives91 questions, matching Cloud's reported sizing.

Overlapping tags (profiles/questions; DO NOT SUM): MI175148/476;
MI177207/646; MI186353/1,030; MI191280/1,026; MI1931,017/3,383;
MI197 dominant172/812. Residual questions by N:3:156,4:180,5:751,6:435.
The finite audit checks admissions and their subset relationships, not the
infinite proofs. MI197's span extension remains an independent hand SKETCH;
MI191 remains the sole pending carrying-read priority.

**The unexpected control is positive while still residual.** For
(2,2,3,4,4,9),23/25, fixed sorted pairs force a run load9,10,14 or15,
outside11..13; increasing the gap cap alone cannot repair that pairing.
Yet A=(0,2,11,13),B=(1,5,9,12),physical(0,25,17,9,3,26,22,4)
passes both validators and its actual E28 partition. It stays RESIDUAL to
the selected admissions. The mixed dominant control(11,3,2,2,1,1),25/15,
A=(0,11),B=(1,4,6,8,9,10),physical(0,25,19,15,11,9,7,22)
also passes both validators/actual partition and has the dominant tag.
Exactly two actual partitions were checked, not6,788. No negative existence
conclusion, mismatch, repair, widened domain or status upgrade.

**What changed / next question.** The first residual is already N3:
(3,5,6),K14, with pairs(3,25),(5,23),(7,21),(9,19),(11,17),(13,15).
Rather than another eight-vertex sibling class, the next useful target is a
uniform FIVE-vertex criterion with three negative halves, legal odd joins,
label count and two-run capacity. This is a proposed question, not a theorem
or a new experiment this tick; search the existing record/prior art first.
Cloud's reported existence survey need not be repeated.

**Step-back / niggle sweep.** Satisfaction: the synthesis exposed a smaller
missing inference. Unease: family proliferation could become a substitute
for understanding selection. Fresh-choice verdict: I would choose this
small-core question now, independent of the earlier investment. Reasoned
verdict: retain the current constructions, stop adding siblings without a
selection argument, and examine the N3 obstruction next. The inventory
niggle is resolved by explicitly naming the six selected mechanisms; the
status niggle by separating476 PROVED-tag questions from sketch admissions;
the residual/nonexistence niggle by the literal positive control. No review
halt or new review queue. Full E28/L8 remains OPEN.

Source tests/probes/instinct/path_forest_admission_synthesis.py;
preregistration a28f88f0. CPU0.061249s, peak RSS18,640,896bytes, within
5CPU sec/128MiB. Immutable artifact
cited/instinct/b87-admission-synthesis-3b53cad88d8f0930.json,558,492bytes,
SHA256 3b53cad88d8f0930397f545953dbad8b3a2a38adc7e37242bd90641a9ad885d0.
Upload digest and manifest receipts verified. No raw data in git.


### MI199 — B88: exact five-vertex diagnostic before a universal claim (2026-10-17 01:05 BST)

**Pull/question.** B87's residual begins at three negative halves. This is
small enough to describe every possible two-run arrangement, rather than
add another sufficient family. Candidate H5: for n>=5, positive halves
sorted a<=b<=c, odd p,q>0 with p+q=2K, a folded-distinct cyclic placement
of(p,q,-2a,-2b,-2c) in0..2n-1 exists IFF max(p,q)<=2n-3,
not p=q=2n-3, c<=n-1 and a+b<=n-1. This is a CONJECTURE to try to break.
No novelty claim; full E28/L8 would not follow from five vertices alone.
Record searched: five.vertex|three.negative|N.?3.*criterion|five.cycle ->
no hits, including ledgers (hyphenated title variants may be missed);
MI175's general necessity and MI180's full-label case reread. Bounded web
queries on prescribed distinct partial sums / two positive and three negative
terms returned no directly relevant primary result; NOT FOUND in that search,
not a theorem of absence. Existing Plagne-Tringali tool remains prior art;
reflection/window requirements here are additional.

**Carrying geometry before code.** Put h=n-1 and choose first odd P.
alpha=(2h+1-P)/2. A=(t,t+D), B=(alpha-t,alpha-t+E,alpha-t+E+F),
where(D,E,F) permutes(a,b,c). Allowed t is the full integer interval
[max(0,alpha+E+F-h), min(alpha,h-D)]. The two endpoint sums give
exact odd P,Q. Chain disjointness is checked explicitly. Also allow a
singleton chain opposite all three gaps (six orders), when its span fits.
These two split types and swapping P/Q cover every placement: rotate to an
odd jump; the negative edges form two monotone parity runs. This is an exact
finite description, not yet a sufficient inequality proof.

Largest alone is load-feasible whenever any two-bin split is: c<=h and
a+b<=h. But choosing P=max(p,q) can fail. Hand fixture n10,h9,
d=(4,4,6),p15/q13: alpha2, largest-chain t1 or2 gives endpoint collisions;
first P13 gives alpha3, A=(3,9),B=(0,4,8), disjoint and exact joins.
The unexpected check will explicitly preserve this failed shortcut while
requiring the opposite-owner witness to pass. Order/owner choice matters.

**Predictions BEFORE experiment.** Check only n5..12, sorted halves1..h,
K<=2h-1, and all legal odd p<=q<=2h-1,sum2K. At most40,000 questions,
10CPU sec/128MiB. Predict H5 exactly matches the complete two-run diagnostic;
stop on the FIRST disagreement and retain it, without a repair or larger run.
Report the actual question count, no claim about n13 onward. This is a small
variable-window diagnostic, not a repeat of Cloud's M28 existence survey.

Independent control: for every question at n5..7 compare existence with an
independent permutation-of-five-moves and physical translation enumeration,
using literal distinctness/window/reflection checks, no chain formulas.
For each accepted question retain one witness and independently validate its
full move bag/folded labels. Negative controls: n14,d=(8,8,8),p23/q25 must
fail capacity and exact geometry; n6,d=(1,4,4),p=q9 must fail despite capacity;
n4,d=(1,1,2),p3/q5 must fail label count. These are separate named fixtures,
not an expansion of the diagnostic grid. No actual E28 partitions or proof
status upgrade. If H5 survives, next is the infinite root/order argument;
finite success does not fill that quantifier. If it fails, examine the first
obstruction. Gut: curiosity about this owner asymmetry is specific, not just
continued warmth. Reasoned: risk the iff before constructing more classes.


**B88 instrument addendum BEFORE rerun (2026-10-17 01:06 BST).** Run1 reached
the final unexpected-control assertion after the grid/comparisons, but stopped:
the constructor returned a DIFFERENT valid opposite-owner root, first13,
A=(2,8),B=(1,5,9),physical(4,17,9,1,16), instead of the hand fixture's
A=(3,9),B=(0,4,8). The exact-root expectation was an over-specific instrument
assertion, not an H5 or independent-oracle disagreement. First source and
failure retained outside git. Correct that assertion to require the predicted
owner13 and full literal move bag; ALSO check the original hand witness
literally, rather than demanding it be the first chosen root. Repeat the same
bounded grid to obtain a complete artifact. No H5/selection repair, domain
extension or new theorem. Counts from the interrupted run are not published.


### MI200 — B88 diagnostic outcome (2026-10-17 01:10 BST)

**COMPUTED, after the retained instrument correction in MI199.** H5 matches
all1,843 prescribed questions at n5..12:1,747 accepted,96 rejected. Counts
by n5..12:14,33,65,117,194,305,456,659. All112 n5..7 questions independently
agree with physical move permutations/translations. Every returned witness
passes the full original move bag and literal folded-label/window checks.
All three negative controls refuse in BOTH methods. Largest-alone with
max-positive-first fails on(4,4,6),15/13 as predicted; swapping owner gives
first13,A=(2,8),B=(1,5,9),positions(4,17,9,1,16). The original hand root
A=(3,9),B=(0,4,8) also passes literally. No mathematical repair or range
extension; first run's preferred-root assertion failure is retained in MI199.

CPU0.059006s,peak RSS13,168,640bytes, inside10CPU sec/128MiB. Source
 tests/probes/instinct/path_forest_five_vertex.py; prereg229dd244. Artifact
cited/instinct/b88-five-vertex-2797a5844c1b228c.json,222,288bytes,SHA256
2797a5844c1b228c00365fa938a25f99757c135afc4e2a5388fc874a52c69b9c;
upload digest and manifest receipts verified. No actual E28 partitions.
The infinite criterion is NOT established by this diagnostic. The next entry
supplies a separate hand argument, rather than extrapolating these counts.


### MI201 — Five-vertex criterion: adjacent diagonals remove the owner obstruction (2026-10-17 01:10 BST)

**PROOF-SKETCH, awaiting a carrying read; no novelty claim.** For n>=1,
positive integers a<=b<=c, and positive odd p,q with p+q=2K,
K=a+b+c, the signed list(p,q,-2a,-2b,-2c) has a cyclic placement on five
vertices in0..2n-1, with distinct folded labels min(x,2n-1-x), IFF

    n>=5; max(p,q)<=2n-3; not p=q=2n-3;
    c<=n-1; a+b<=n-1.

This concerns exactly these five signed moves, not full E28/L8. It depends
on neither MI191 nor other unreviewed construction sketches.

**Necessity.** Five folded labels need n>=5. An odd jump2n-1 joins a
reflection pair; larger jumps leave the window. Two occurrences of2n-3
would have to use edges0->2n-3 and1->2n-2, whose four endpoints have only
two folded labels (or repeat an edge), impossible. The two positive odd
moves divide the cycle into two monotone parity runs. Each run's negative
half-load is at most h=n-1. For three halves, any such two-bin split implies
c<=h and a+b<=h: the sum of the two smallest is no greater than whichever
pair is together; if all three are together this is immediate.

**Reduction to adjacent diagonals.** Assume these inequalities and set
S=a+b, H=h-c, J=h-S, T=H+J=2h-K. Legal p/q and the excluded doubled maximum
give T>=2. Put P=max(p,q),Q=min(p,q) and

    alpha=(2h+1-P)/2,
    1<=alpha<=(T+1)/2,  alpha>=h+1-K.

A two-point A-chain of gap c starts at x in[0,H]; a three-point B-chain
of successive gaps a,b (either order) starts at y in[0,J]. Let z=y-x.
Their starting sum x+y determines the odd joins: if x+y=alpha, they are
P,Q exactly. If x+y=alpha-1, reflect EVERY index i->h-i and reverse each
chain's order. The new starting sum is

    2h-((alpha-1)+K)=T+1-alpha=(2h+1-Q)/2,

so the joins are Q,P exactly. Thus we may use either adjacent diagonal
x+y=alpha OR x+y=alpha-1. This is the owner freedom the max-first shortcut
lost; it is not an approximate or rounded padding argument.

All z values on these two diagonals form ONE interval I of consecutive
integers. If H,J>=1, alpha<=(H+J+1)/2 implies at most one of H,J is smaller
than alpha. Direct endpoint calculation gives

    alpha<=min(H,J): I=[-alpha,alpha];
    H<alpha<=J:      I=[alpha-1-2H,alpha];
    J<alpha<=H:      I=[-alpha,2J-alpha+1].

In particular |I|>=3; if alpha>=2 then |I|>=4; if alpha,H,J>=2 then
|I|>=5. Every integer in I corresponds to an actual allowed x,y on one
of the two diagonals, not just to an interval relaxation.

**Forbidden offsets and ordering.** A endpoints are x,x+c; B endpoints
y,y+S. Endpoint collisions exclude only

    F0={-S,0,c-S,c}.

If a!=b, the possible internal B-points y+a and y+b cannot BOTH hit A's
two endpoints: they are distinct and separated by b-a<c. One order therefore
avoids an internal collision whenever z is outside F0. If a=b=e, there is
one internal point and the full forbidden set is

    F={-2e,-e,0,c-2e,c-e,c}.

No other cross-chain collision is possible. Same-chain indices are strictly
increasing; five distinct indices give five distinct folded labels in the
physical cycle

    2A_min, (2h+1-2B_i in increasing index order),
    (2A_i for the remaining A-indices in decreasing order).

Its negative half-gaps are exactly a,b,c and its odd joins have the prescribed
owners established above.

**Thin rectangles first.** If H=0, J=T>=2. Take x=0,y=alpha. Here
1<=alpha<=T-1, so z=alpha lies strictly between0 and c-S=T, outside F0.
In the equal case the additional bad offsets -e and c-e=T+e also miss it.
If J=0, H=T>=2. Take y=0,x=alpha, so -T<z=-alpha<0, outside F0.
In the equal case T=2e-c<=e, hence alpha<=T-1<e, and the additional
-e,c-e>=0 cannot obstruct it. These arguments include all thin cases.

**Thick rectangles H,J>=1.**
- If a!=b, c>=2,S>=3. In the sorted list F0, the two outer gaps are
  c (when c<S) or S (when c>S), at least2; only the two middle values
  can be consecutive. Thus F0 has no three consecutive integers, while
  I contains at least three. Choose an available z and then the B order.
- If a=b=e>=3, F occupies at most two residue classes modulo e. Three
  consecutive integers cannot all lie in F; again I supplies a good z.
- If e=2 and c is even, F is entirely even. If c is odd and c>=5,
  F has no three consecutive integers: for c5 only0,1 are adjacent,
  and for c>=7 the two step-two triples are separated by at least3.
- The remaining e2,c3 case has F={-4,-2,-1,0,1,3}, longest consecutive
  block length4. If alpha=1, instead isolate a gap2 and take
  A=(1,3),B=(0,2,5), valid whenever h>=5. If alpha=2,h=5 take
  A=(2,4),B=(0,3,5). If alpha=2,h>=6, |I|=5. If alpha>=3,
  alpha<=h-3 forces h>=6 and H>=3,J>=2; the displayed formulas give
  |I|>=6. These intervals escape F. The only h4 candidate has doubled
  maximum p=q7 and was excluded.
- If e=1,c>=4, F consists of the disjoint triples[-2,0] and[c-2,c],
  so has no block longer than3. For alpha>=2, |I|>=4. For alpha1,
  I=[-1,1] contains1, which is outside F.
- Finally e1,c1..3: for h>=7 the positivity bound gives alpha>=h-4>=3,
  while H>=4,J>=5. Hence |I|>=7, larger than the at-most-six forbidden
  offsets. The remaining h4..6 cases are the following explicit table.

**Small remainder (hand-checkable table; also checked by both B88 instruments).**
Each row gives h,c, unordered p/q, first positive, A, B. The other two
negative halves are1,1. Every legal unordered pair at these h,c occurs;
(1,9) is absent at h4 because9 exceeds the bound7. Read the two starting
and ending sums to check the joins, and the within-chain gaps to check the
negative bag. All indices listed are distinct and lie in0..h.

| h | c | p/q | first | A | B |
|---|---|---|---|---|---|
|4|1|1/5|1|4|0,1,2,3|
|4|1|3/3|3|3,4|0,1,2|
|4|2|1/7|7|1|0,2,3,4|
|4|2|3/5|3|3|0,1,2,4|
|4|3|3/7|7|1,2|0,3,4|
|4|3|5/5|5|2,3|0,1,4|
|5|1|1/5|1|5|0,1,2,3|
|5|1|3/3|3|4|0,1,2,3|
|5|2|1/7|1|4|1,2,3,5|
|5|2|3/5|3|3|1,2,4,5|
|5|3|1/9|9|1|0,3,4,5|
|5|3|3/7|3|4|0,1,2,5|
|5|3|5/5|5|3|0,1,2,5|
|6|1|1/5|1|5|1,2,3,4|
|6|1|3/3|3|2|3,4,5,6|
|6|2|1/7|1|6|0,1,2,4|
|6|2|3/5|3|4|1,2,3,5|
|6|3|1/9|1|5|1,2,3,6|
|6|3|3/7|3|4|1,2,3,6|
|6|3|5/5|5|4|0,1,2,5|

This exhausts the cases, completing the candidate sufficiency argument.

**Application to B87's first residual.** At n14,(a,b,c)=(3,5,6),p25/q3,
alpha1, choose z1,x0,y1,A=(0,6),B=(1,4,9). Physical positions
(0,25,19,9,12) have moves(25,-6,-10,3,-12), with five distinct folded
labels. The criterion addresses every legal p/q for this profile, not only
this example; the hand theorem still awaits an independent read.

**Niggle sweep / verdict.** The consecutive-offset assertion needs BOTH
adjacent diagonals, not one parity sublattice; its three endpoint formulas
make that explicit. The alpha-1 owner conversion has the necessary +1:
T+1-alpha, not T-alpha; B88's original opposite-owner hand witness is exactly
that reflection in the(4,4,6) example. Thin H0/J0 are handled before invoking
interval thickness. Equal small halves are not waved away by residue
counting: explicit cases/table above cover them. Every table row is already
in the independently cross-checked n5..7 diagnostic; no further run or bigger
census was needed. Delight at the change from family production to a common
selection argument; reasoned verdict: a genuine uniform proof candidate,
not a finite success extrapolation. Request ONE focused carrying read of
this adjacent-diagonal argument and the equal-small exceptions, replacing
MI191 as the current review priority, without halting independent work.
MI191 remains unreviewed, not withdrawn; its request need not stay queued.
General N>=4 selection and full E28/L8 remain OPEN.


### MI202 — B89: isolate the two-prefix obstruction, rather than append another cycle class (2026-10-17 01:20 BST)

**Pull/question.** MI201's owner freedom gives consecutive relative offsets
for ANY fixed two-run load split. What does not generalize automatically is
ordering the internal prefixes. If one chain is a single gap D and the other
has positive steps of maximum<=D, disjointness asks its proper prefixes to
avoid at most two levels x,y separated by D. The geometry is now separated
from the carrying ordering question; no larger folded-cycle census this block.

MI117's one-level lemma was reread: unless all steps are equal, a boundary
swap avoids one prescribed proper prefix sum. It does NOT solve two levels:
(1,1,2),forbidden1,3, is unavoidable in all three orders. This failure is
retained, not treated as an inference somebody else made. It is the precise
step needed to continue the one-gap selection argument.

Candidate H2 (necessary shape of an obstruction): for m>=3 positive integer
steps and0<x<y<S=sum steps, y-x>=max step, if EVERY order hits x or y as a
proper prefix, then some value occurs at least m-1 times. Contrapositively,
if no value occurs m-1 times, the two levels can be avoided simultaneously.
The converse is NOT claimed; some nearly constant profiles avoid both.
If true this is a general permutation-selection tool, not an E28 proof.
Record searched: adjacent.diagonal|consecutive.offset|two.*residue.*prefix|
one.*large.*chain and two.forbidden|two.prefix|unavoidable.*prefix ->no
search hits (literal hyphen/spacing variants can be missed); MI117 and201
read explicitly. Bounded web searches for permutations avoiding two partial
sums/unavoidable prefix sums found no directly relevant primary statement;
no theorem of literature absence or novelty claim.

**Predictions BEFORE run.** Fixed small arithmetic domain: sorted multisets
length3..7,values1..4; all proper integer barrier pairs x<y<S with
separation>=max step. At most100,000 questions,10CPU sec/128MiB. Predict H2
holds; stop on FIRST rich-profile unavoidable pair and retain its complete
DP unreachable certificate plus independent permutation check, no repair,
range extension or follow-up grid. No theorem extrapolation if it survives.
Primary instrument: labelled-subset reachability, adding one unused item
unless the new proper prefix is x or y. Deduplicate equal masks only by
value symmetry in the result, not by silently deleting copies. Independent
control: exhaustive distinct value-permutations for all m<=5 questions,
agreeing on existence, and validate every returned witness literally.
Store full question outcomes and one avoiding order when present.

Controls: (1,1,2),1/3 must be unavoidable despite nonconstant steps.
Unexpected separation control: rich(1,1,2,2),2/3 is unavoidable when the
separation condition is dropped; this guards against overgeneralizing H2.
A positive control(1,1,2,2),1/3 admits2,2,1,1. If H2 fails, the counterexample
should guide the next split/representation; do not patch the hypothesis and
rerun in this block. Gut: curiosity about the obstruction, not pressure to
produce another theorem. MI201 review remains nonblocking and the sole
carrying request; no extra queue for a finite diagnostic or known lemma.


### MI203 — B89 outcome: the obstruction-shape prediction survives (2026-10-17 01:22 BST)

**COMPUTED, no repair or widened range.** All20,390 prescribed barrier
questions on lengths3..7,values1..4 complete. There are16,015 rich questions
(no frequency>=m-1), and every one has an avoiding order. Exactly890 pairs
are unavoidable, all nearly constant as H2 predicts. All3,165 questions at
m<=5 agree with independent value-permutation enumeration. The three named
controls pass, including rich(1,1,2,2),2/3 unavoidability when separation is
dropped. Full literal witness checks pass. This establishes H2 only in the
fixed finite domain; the following hand argument supplies the uniform step.

CPU1.505551s,peak RSS18,427,904bytes, inside10CPU sec/128MiB.
Source tests/probes/instinct/two_prefix_obstruction.py; preregde13924c.
Immutable artifact cited/instinct/b89-two-prefix-d03fa79ad1368966.json,
1,585,698bytes,SHA256 d03fa79ad13689666e37c6e57084601244b57d2196c45959a410bd8c6de304b5.
Upload digest and manifest receipts verified. No folded-cycle enumeration,
actual E28 partition, new proof status or review queue is inferred from it.


### MI204 — Two separated forbidden prefixes: a uniform obstruction theorem (2026-10-17 01:22 BST)

**PROOF-SKETCH, no novelty claim; independent of MI201.** Let m>=3 positive
integer steps have total S and maximum M, and let0<x<y<S with D=y-x>=M.
If no value occurs at least m-1 times, there is an ordering whose proper
prefixes avoid BOTH x and y. Equivalently, an unavoidable pair with this
separation requires a constant or all-but-one-equal multiset. The converse
is not asserted. This is a permutation theorem, not the full cycle result.

**1. There is an order hitting both barriers if a rich obstruction exists.**
Assume for contradiction that every order hits x or y, and no value occurs
m-1 times. The steps are nonconstant. A single forbidden level can be avoided:
if an order hits t, separate the items before/after t, find unequal items
across that cut (otherwise all items agree), put them adjacent at the cut
and swap. The one changed prefix is t-u+v!=t, all earlier prefixes below t,
all later ones above t. This repeats MI117's complete argument, not an
unreviewed external premise.

Thus one order hits only x and another hits only y. The graph of permutations
of labelled copies under adjacent swaps is connected. Each swap changes only
ONE proper prefix by |u-v|<M<=D. It cannot change a prefix equal to x into y
or vice versa. Under the assumed absence of an order avoiding both, a path
between those two orders must therefore pass through an order hitting BOTH.
Fix such an order and split it into nonempty consecutive blocks A,B,C of
sums x,D,S-y respectively. Within-block reorderings preserve these two cuts
and cannot introduce any other hit of x or y, since the steps are positive.

**2. Two disjoint boundary repairs.** If B has at least two items, look for
distinct B occurrences v,z and items u in A,w in C with u!=v and z!=w.
Put u last in A,v first in B,z last in B,w first in C, then swap u/v AND
z/w. The pairs are disjoint. The changed prefixes become x-u+v and y-z+w.
Neither equals its original barrier; neither can reach the other barrier
because the absolute changes are strictly less than D. Every other prefix
is unchanged from the within-block reordered word. This avoids BOTH.

Why can the two repairs fail? Let L be the B occurrences that differ from
some A item, and R the B occurrences that differ from some C item.
If L is empty, all of A and B have one common value e. If R is empty,
all of B and C have one common value e. If L,R are nonempty but admit no
distinct representatives, then L=R={one occurrence}. Any other B item
exists and equals every A and C item; all other B items do too. Only the
unique representative can differ. That is an all-but-one-equal multiset,
excluded. Thus the only unresolved possibilities are A+B constant or
B+C constant, handled in step4.

**3. If B is a singleton, there is only one exceptional item.** Its value
is D; since D>=M it equals M. If there are u in A,w in C with u!=w,
put these at the two ends next to the singleton. Write the triple as
u,M,w with preceding sum x-u. If u<M, replace it by M,w,u: its first
prefix lies strictly between x,y, and its second is y+w-u, strictly above
x and different from y. The triple ends at y+w>y. If u=M, then w<M;
use w,M,u: its first prefix is below x, second x+w strictly between x,y,
and its end above y. All other prefixes remain unchanged. Thus both
barriers are avoided. If no unequal cross-pair u,w exists, every item of
A and C equals the same e; only the singleton M can differ, excluded.

**4. A constant block cannot trap two exceptions.** Suppose A+B consists
of e-steps, total y. Since the full multiset is not nearly constant, C has
at least TWO items different from e. If one such f is not divisible by e,
put f first, then ALL the e-items, then all remaining items. During the
e-run every prefix is nonzero modulo e, while x,y are multiples of e.
After that run the sum is at least f+y>y; remaining positive items cannot
hit either barrier. This order avoids both.

Otherwise every item is a multiple of e. Divide by e: there are at least
y'=y/e unit steps, and at least two nonunit steps f',g'>=2, each <=D'=D/e.
Use the order

    (x'-1) units, f', (D'-f') units, g', all remaining items.

The first jump goes from x'-1 to a value in[x'+1,y'-1]; after the next
unit block the prefix is exactly y'-1, and the second jump reaches at
least y'+1. Required unit counts are nonnegative and total y'-f'-1,
no more than the available y' units. Hence both levels are avoided.
If B+C is constant, reverse the entire ordering and use the same argument
for the barriers S-y,S-x (same separation D and maximum-step bound).
All cases contradict unavoidability. This proves the candidate theorem.

**Connection back to the missing cycle inference.** With one isolated gap
D and a companion chain, a relative offset z outside endpoint collisions
asks the companion prefixes to avoid -z and D-z when those are proper
levels. If all companion steps<=D and no companion value occurs all but
once, the argument above removes BOTH internal collisions for any such z.
If only one level is proper, step1 suffices. The adjacent-diagonal geometry
then has only endpoint collisions left to address. The next larger obstacle
is finding a suitable load split when no isolated gap fits, or handling the
near-constant exceptional chain: not a larger calibration of this theorem.
This paragraph is an application plan with SKETCH dependencies, not another
family census, full criterion or status upgrade.

**Niggle sweep / fresh choice.** The strict inequality |u-v|<M matters,
including at D=M; positive steps supply it. Boundary repairs need DISTINCT
B occurrences; the representative-set argument handles exactly that cost.
The singleton case is separate, rather than pretending its repairs are
disjoint. In step4 the e-run has at least y/e occurrences from A+B, and
both nonunit jumps come from C, so no item or unit is used twice. Reversal
preserves proper-prefix avoidance and barrier separation. The experiment's
rich failure at separation1<max2 guards the missing-hypothesis temptation.
These are cheap algebraic/adversarial checks, not independent verification.
Gut: delight at a common ordering argument; reasoned: understanding moved
from five vertices to an arbitrary-length permutation obstruction. Fresh
choice still favors the mathematics over more record production. MI201
remains the sole requested carrying read; share this sketch by READ-LEDGER,
without adding a review queue or halting. H2 and the cycle criteria remain
SKETCH until carrying reads. Full E28/L8 and arbitrary load selection OPEN.


### MI205 — B90: finish the near-constant exception arithmetically (2026-10-17 01:32 BST)

**Pull/question.** Before changing a load split, know exactly when reordering
CANNOT help it. MI204 isolated the nearly constant exception but did not
classify it. The one-exception profile permits a single parameter, so this
is a completion of the common ordering mechanism, not another folded-cycle
family or existence census. Record searched: near.constant|two.prefix|
balanced.*load.*split, then exception.*prefix.*congru|near.constant.*criterion|
prefix.*repeated.*step ->no search hits (spacing variants missed our recent
entries); MI117,201,202-204 explicitly read. Prior bounded literature search
in MI202 found no directly relevant primary theorem; no novelty claim.

**Hand candidate BEFORE audit.** For m>=3 positive integer steps, total S,
maximum M,0<x<y<S and D=y-x>=M, the exact unavoidability criterion is:
- all steps s: x or y is a multiple of s;
- r>=2 copies of s plus one t!=s: x is a multiple of s AND D=t mod s;
- no value occurs m-1 times: avoidable, conditional on MI204 SKETCH.

For the middle case, every order is determined by k equal steps before t,
0<=k<=r. Proper prefixes are sj (1<=j<=k) and t+sj (k<=j<=r-1).
For each forbidden z add k<=z/s-1 when z/s is an integer1..r, and
k>=(z-t)/s+1 when(z-t)/s is an integer0..r-1. Intersect with[0,r].
This interval test is exact for ANY forbidden levels, even without separation;
the congruence simplification uses D>=max(s,t). If nonempty, choose its lower
endpoint and write s^k,t,s^(r-k). No ordering search is needed.

**Predictions BEFORE audit.** Reuse the immutable B89 artifact and its frozen
labelled-subset DP outcomes: all20,390 classifications must match the formula;
all4,375 non-rich questions are now constant/one-exception cases. Construct
and literally check every avoiding order in these arithmetic classes; retain
rich B89 witnesses without claiming a new algorithm. No existence solver is
rerun over that domain. Digest must match MI203. Separately check only these
12 fixed one-exception fixtures against B89's independent subset DP:
(r,s,t;x,y)=(2,1,3;1,4),(3,3,2;2,6),(4,5,2;5,12),
(4,5,2;2,10),(5,2,7;2,9),(5,2,7;1,8),(3,3,6;3,9),
(3,3,6;2,8),(6,4,3;4,11),(6,4,3;3,12),(2,7,1;1,14),
(2,1,3;1,2). Last is a deliberate OUTSIDE-separation counterfactual:
the congruence-only rule says unavoidable, but3,1,1 avoids1/2; the exact
k-interval must agree with DP. Unexpected check: t<s in(3,3,2;2,6)
forces the unique interior k1, not putting the exceptional step first/last.
2CPU sec/64MiB, stop any mismatch; no repair, expanded range or fresh census.
The uniform implication remains SKETCH because MI204 is unreviewed. MI201
remains sole requested carrying read; no new queue or review halt.


### MI206 — Complete two-prefix classification, including the exception (2026-10-17 01:32 BST)

**PROOF-SKETCH; rich case depends on MI204 SKETCH, arithmetic case independent.**
Let m>=3 positive integer steps have total S and maximum M, with
0<x<y<S and D=y-x>=M. Exactly these obstructions are unavoidable:

1. All steps equal s, and x or y is divisible by s.
2. Exactly r=m-1 steps equal s and the remaining t!=s, with s dividing x
   AND D=t mod s.

All other profiles admit an order avoiding both. Case1 is immediate from the
fixed proper prefixes s,2s,...,(m-1)s. MI204 gives avoidance for profiles
with no frequency m-1. The following proves the one-exception criterion;
no permutation census supplies its infinite quantifier or novelty claim.

**Exact interval, even without a separation hypothesis.** With k copies
of s before t, the proper prefixes are sj (1<=j<=k) and t+sj
(k<=j<=r-1). Thus for every forbidden level z:

    if z=sj, 1<=j<=r, require k<=j-1;
    if z=t+sj, 0<=j<=r-1, require k>=j+1.

Intersect these with0<=k<=r. The intersection is an integer interval [L,U];
empty means impossible, otherwise k=L supplies an explicit avoiding order
s^k,t,s^(r-k). This derivation also applies to ANY finite forbidden set,
without changing the interval rule; the compact congruence theorem concerns
two separated levels only. No rich-profile generalization to more barriers
is inferred.

**Why the congruences force failure.** Suppose x=sj and D=t+qs. Since
D>=t, q>=0. The proper upper barrier is y=t+s(j+q), and y<S ensures
j+q<=r-1. The lower barrier has j>=1; also x<S-D<=rs ensures j<r.
If k>=j, the order hits x before t. If k<=j-1, then k<=j+q and the
order hits y after t. No k avoids both.

**Why there are no other failures.** A single proper level is avoidable
for a nonconstant multiset, by the one-level boundary swap reproduced in
MI204 step1. Each individual barrier therefore leaves a nonempty interval
of allowable k. Any empty combined interval requires a lower bound from
one barrier and an upper bound from the OTHER. If the lower bound comes
from y and the upper from x, then x=si and y=t+sj: precisely the stated
congruences. Conversely consider a lower bound from x=t+si and an upper
bound from y=sj. Their compatibility asks i+1<=j-1. But

    j-i=(D+t)/s,

an integer strictly greater than1 because D>=s and t>0. Thus j-i>=2,
so these bounds are compatible. Bounds not arising from actual proper
prefix indices were never inserted; their absence cannot create failure.
This proves the criterion, including when t is divisible by s and a barrier
produces both kinds of bound.

**Relative offsets for an isolated gap.** Isolate a gap G>=max(s,t) in A,
and let B's gaps be s repeated r times plus t, total S=rs+t. For relative
start z=B_min-A_min, endpoint collisions are
F0={-S,0,G-S,G}. Outside F0, both A endpoints are internal B-levels exactly
when G-S<z<0. The unavoidability theorem then says that the FULL set of bad
z values (over ALL orders of B) is exactly

    F0 union {z: G-S<z<0, s divides z, G=t mod s}.

If at most one A endpoint is internal, the one-level swap avoids it. This
is an exact obstruction description for that fixed split; it does not
upgrade the single-gap split to a universal choice. For rich companion
gaps MI204 leaves only F0. Constant companions instead retain their two
full arithmetic progressions of forbidden offsets.

**A genuine split obstruction, by hand, not a new experiment.** At n10,
h9, halves(3,3,3,5),p17/q11, isolating5 leaves B's constant3,3,3 chain
filling0..9. First17 forces A=(1,6),B=(0,3,6,9), colliding at6.
First11 forces A=(4,9),same B, colliding at9. There is no other root or
B ordering for this split. Yet split the loads8/6 instead and take

    A=(0,3,8), B=(1,4,7),
    positions=(0,17,11,5,16,6),
    moves=(17,-6,-6,11,-10,-6).

Folded labels are0,2,8,5,3,6, all distinct in0..9. Thus the FULL prescribed
move list is constructible while every isolated-largest-gap arrangement
fails. The lesson is now concrete: some remaining work is load-split
selection, rather than a more persistent prefix reorder. Constant companions
and nearly constant unit companions retain explicit obstruction sets; no
false 'H2 solves every load split' inference remains.

**Niggle sweep / verdict.** Proper-index bounds matter: final total S is
excluded in both progressions. The D>=max(s,t) condition supplies BOTH
D>=t in the unavoidable direction and D>=s in the reverse-bound direction.
If omitted, repeated1 plus3 can skip1/2 in one jump, refuting the congruence
shortcut (MI207). Small t<s is allowed; its unique interior insertion test
rules out an implicit large-exception assumption. Fixed-split failure is
separated from whole-cycle failure by the explicit six-vertex witness.
Gut: satisfaction at closing the ordering exception and a more specific pull
toward competing splits. Reasoned: this completes a selection subproblem
with MI204's provisional premise; it does not close E28/L8. No new review
queue; MI201 remains the requested carrying read, nonblocking.


### MI207 — B90 audit outcome (2026-10-17 01:32 BST)

All prescribed checks pass without repair. The frozen B89 domain splits
into1,250 constant,3,125 one-exception and16,015 rich questions. Exactly
560/330/0 respectively are unavoidable; the arithmetic formula agrees with
ALL20,390 frozen subset-DP outcomes. All3,485 avoiding arithmetic-class
orders are constructed from the k-interval and literally checked; rich
witnesses are retained and checked, not regenerated by a new solver.
All12 named independent DP fixtures agree with the exact interval rule.
The omitted-separation counterfactual correctly DISAGREES with the shortcut:
(1,1,3),levels1/2 has k0 and order3,1,1. The unexpected small-exception
fixture s3,r3,t2,levels2/6 has the UNIQUE k1 and order3,2,3,3.

CPU0.246513s,peak RSS34,115,584bytes, inside2CPU sec/64MiB. Source
 tests/probes/instinct/two_prefix_arithmetic.py; prereg8349c2fa.
Immutable artifact cited/instinct/b90-two-prefix-arithmetic-81dac6e9ac30605b.json,
2,303,604bytes,SHA256 81dac6e9ac30605b91d9ed47a870e026f21fad461619ca925d10ca1b4d41d553.
Input digest checked against MI203; upload digest/manifest receipts verified.
No new domain-wide existence run, E28 partition or independent hand review.
The MI205 heading01:32 was a rounded-ahead stamp: the clock read immediately
after its push was01:31:13 BST; commit8349c2fa is the preregistration receipt.
MI206's interval proof and MI204 remain SKETCH. Next is the split-selection
obstruction illustrated above, not another calibration of the completed
arithmetic classification. Cloud has no new flag at block start; MI201 read
remains nonblocking. Full E28/L8 OPEN.


### MI208 — B91: use Grasshopper to complete a two-gap split (2026-10-17 01:44 BST)

**Direction change on prior art.** The opening question was whether the
prefix method handles three barriers. Before an experiment, primary literature
supplied the distinct-jump Grasshopper result: four distinct positive steps
can avoid three prescribed proper-prefix levels. C7 Variant2 and its full
proof read in the official IMO2009 shortlist, filed in PRIOR-ART. No H3 probe
or known-theorem reproof is opened. The general repeated-step H3 question is
not settled by this source. Record searched: three.forbidden|three.prefix|
separated.*barrier, then grasshopper|IMO.*2009 ->no hits; MI201/204/206 and
the explicit split obstruction MI206 reread. This applies a stronger known
tool to a concrete missing split, without another existence census.

**New geometric application, SKETCH.** At M28,n14,h13, sort six positive
negative halves as b1<b2<b3<b4<=D<=E, so the four smaller halves are DISTINCT.
Put A-load L=D+E, B-load S=sum b_i. Suppose L<=13,S<=13, odd positives
p+q=2(L+S),max(p,q)<=25,not p=q25. Then the six halves admit a folded cycle
with those odd joins. This is a sufficient subregion, not all E28/L8.
It requires neither MI201 nor MI204, only the known theorem and the following
endpoint-selection argument.

Set H=13-L,J=13-S,T=H+J=26-(L+S)>=2. Choose P=max(p,q),
alpha=(27-P)/2,1<=alpha<=(T+1)/2. Allow starting sums alpha or alpha-1;
reflecting the latter's two index chains swaps the odd owners exactly as
in MI201 (identity rechecked: new sum=T+1-alpha). Relative start z=B_min-A_min
ranges over a consecutive interval I. For H,J>=1 the three elementary formulas
in MI201 give |I|>=3. This interval identity is reused as explicit algebra,
not an assumption that the five-vertex theorem extends to six gaps.

Choose the order D,E in A. Its endpoints are0,L relative to A_min, internal
point either D or E; B's endpoints are z,z+S. Endpoint failure for BOTH
A orders has the exact offset set

    F0={-S,0,L-S,L};
    if D=E=u, also {u,u-S};
    if D!=E and |D-E|=S, also {min(D,E)}.

For unequal D,E, both candidate internal points can hit the two B endpoints
only when their difference is S; this gives the displayed extra offset.
For equal D,E there is one candidate internal point. No other A-order
failure occurs once its own endpoints avoid B's endpoints.

Here b4>=4,D,E>=4,S>=10. If D=E=u, the full bad set occupies at most two
residue classes modulo u>=4; it cannot contain three consecutive integers.
If D!=E and |D-E|!=S, F0 has no3 consecutive integers because its two outer
gaps are min(L,S)>=8, leaving only the two middle values possibly adjacent.
If |D-E|=S and v=min(D,E), the full set is{-S,0,v,2v,L}; every consecutive
gap is at least v>=4. Thus a thick I always has an endpoint-compatible z
and an A order.

Thin cases do not use that thickness claim. If H=0, L=13 is odd, so D!=E.
Also |D-E|=S is impossible: it would give2min(D,E)=13-S<=3, contradicting
min(D,E)>=4. Take A_min0,B_min alpha;1<=alpha<=T-1, so z avoids F0, and
one A order avoids the B endpoints. If J=0, S13 and L<=11. Take B_min0,
A_min alpha;0<alpha and alpha+L<=12, so EVERY A vertex lies strictly between
B's endpoints0,13. Either A order works. H=J=0 is excluded by T>=2.

With that A fixed, its three vertices relative to B_min give at most three
forbidden proper prefixes of B. Neither B endpoint is among A's vertices.
Apply the known theorem to the four distinct B-gaps to choose their order.
All A/B indices are now disjoint in0..13; the physical-cycle formula gives
exact original p/q and all six negative halves. No maximum-step separation
is needed for this distinct-step application.

**Predictions BEFORE code/run.** Only two literal fixtures on
halves(1,2,3,4,5,8), A=(0,5,13): (p,q)=(25,21),B=(1,2,4,7,11), and
(23,23),B=(2,6,7,9,12). Both must pass the full physical move bag, two literal
folded-geometry validators and actual E28 partition checks. Read the frozen
B87 artifact with its digest: this profile must be residual to its six
selected mechanisms and have exactly pairs21/25,23/23. This tests the intended
connection, not global novelty/coverage. No existence solver, profile grid,
new admission count or mathematical status upgrade.

Counterfactual/unexpected: keep ascending B-gaps1,2,3,4 at p=q23, giving
B=(2,3,5,8,12). It retains the original move multiset and legal window but
shares index5 with A; literal folded geometry must reject it. The ascending
order works at25/21, so one successful fixed order cannot be reused without
the theorem's order choice. Exactly two actual partitions,1CPU sec/64MiB;
stop any mismatch, no repair or bigger run. Gut: delight at useful prior art
changing the attack. Reasoned: test the endpoint reduction and concrete
previously missed profile; repeated-gap split selection remains open.
MI201 read stays sole requested priority, no new queue or halt.


### MI209 — B91 outcome: distinct-step completion crosses an existing residual (2026-10-17 01:46 BST)

All prescribed checks pass. The frozen B87 record confirms(1,2,3,4,5,8)
is outside its six selected admissions, with exactly the two unordered
positive pairs21/25 and23/23. Both prescribed constructions pass the full
move bag, independent folded-geometry checks and both actual E28 partition
validators. At25/21, ascending B gaps give positions
(0,25,23,19,13,5,26,10). At23/23, order4,1,2,3 gives
(0,23,15,13,9,3,26,10). Exactly TWO actual partitions were checked.
The ascending second-order counterfactual retains the exact move bag and
window but has reflection pair17,10 (sum27), corresponding to shared index5;
both geometry validators reject it. No order/profile search or larger run.

CPU0.015648s,peak RSS19,415,040bytes, inside1CPU sec/64MiB. Source
 tests/probes/instinct/path_forest_grasshopper_completion.py; prereg460620c4.
Artifact cited/instinct/b91-grasshopper-f01f4071caabbe8a.json,1,316bytes,
SHA256 f01f4071caabbe8a04c213693b8cb160cde8e8a2284e040fe3d508ef60000871.
Input B87 digest, immutable upload digest and manifest receipts verified.
The general endpoint application MI208 is SKETCH; the two partitions are
COMPUTED. Known Grasshopper theorem stays PRIOR-ART; no new theorem claimed
for it or routine review requested. Full E28/L8 remains OPEN.

**Niggle sweep / what changed.** Known distinct jumps are not a repeated-gap
result; no multiplicity premise is imported. Three proper forbidden levels
exclude both fixed B endpoints, which the separate A-order/root argument
checks. Thick-root residue counting does not handle thin H0/J0; both are
proved separately in MI208. No whole-cover count is inferred from a frozen
residual membership check. The full move bag alone misses the deliberately
bad second order, while literal reflection catches it. Delight: the source
search changed the method and supplied a useful completed construction.
Reasoned: distinct smaller gaps now have a common completion argument;
remaining repetition cases must earn their own inference.

**Next concrete inference, not another H3 census.** If the A-chain's total
span L>=S, its three vertices cannot ALL lie strictly inside B's span S.
Thus at most TWO proper B-prefix levels are forbidden, and top-two A gaps
are each at least every B-gap. MI204 may then handle rich REPEATED B steps.
The endpoint selection must be rechecked at smaller repeated gap values
(the MI208 bound b4>=4 is unavailable). That is a sharper next question
than conjecturing a new arbitrary-length three-barrier theorem. No new
experiment opened here. MI201 remains sole requested carrying read,
nonblocking; send a concise READ-LEDGER pointer for this direction change.


### MI210 — B92: a longer two-gap chain handles rich repetitions (2026-10-17 01:59 BST)

**Pull / question.** The warm part is the geometric reduction, not another
catalogue: can the top-two split handle repeated companion gaps because
its span prevents a third internal obstacle? What would advance E28 is a
common completion argument for a repeated-gap subregion, including existing
B87 residuals. No claim that this subregion covers all E28 or L8.

**Record search correction.** record_find.py takes separate arguments as
AND within one paragraph. Several recent queries intended as alternatives
therefore gave zero conjunctive hits, not evidence of no individual match.
Those blocks separately read MI201/204/206 and did not establish novelty
from the zeroes. Corrected single-regex searches now run:
span.dominant|rich.*companion|two.*internal.*obstacle -> MI206;
grasshopper|IMO.*2009|three.forbidden|three.prefix|separated.*barrier ->13
paragraphs in7 files, including MI206/208, PRIOR-ART and older unrelated
three-prefix material. The relevant current entries were read directly.
No new literature theorem or novelty priority is claimed here.

**Hand argument, PROOF-SKETCH, conditional on MI204.** At M28,n14,h13,
sort six halves b1<=b2<=b3<=b4<=D<=E. Put S=sum b_i,L=D+E and assume
S<=L<=13. Suppose the four B-gaps are rich: no value occurs more than twice.
Odd positives p,q satisfy p+q=2(L+S),max(p,q)<=25,not p=q25.
Then the prescribed list has a folded-distinct eight-vertex cycle.
This uses MI204's two-separated-prefix theorem, not Grasshopper's distinct
premise or the unreviewed five-vertex iff of MI201.

Set H=13-L,J=13-S,T=H+J>=2,alpha=(27-max(p,q))/2, so
1<=alpha<=(T+1)/2 and J>=H. For A_min=x in[0,H], B_min=y in[0,J],
allow x+y=alpha or alpha-1. Relative z=y-x ranges over

    I=[-alpha,alpha]                 if alpha<=H,
    I=[alpha-1-2H,alpha]             if H<alpha<=J.

These cover all cases since J>=H and alpha<=(H+J+1)/2<=J when H<J;
if H=J, alpha<=H. When H>0 the interval contains at least3 integers.
For an offset z, use c=alpha if z=alpha mod2, otherwise c=alpha-1,
then x=(c-z)/2,y=(c+z)/2. If c=alpha-1, reflect both chains by i->13-i
and reverse their lists. Their new start sum is T+1-alpha, giving the
other original odd positive as first join; this is an identity, not an
appeal to MI201's theorem.

A's possible middle points are x+D,x+E. BOTH orders fail to avoid B's two
endpoints precisely at

    F0={-S,0,L-S,L},
    plus {u,u-S} if D=E=u,
    plus {min(D,E)} if D!=E and |D-E|=S.

Reason: outside F0, only the middle A point can hit a B endpoint; two
different possible middle points both hit exactly when their difference
is S. Rich four-gap B has max b_i>=2 and S>=6. Thus D,E>=2.
For equal D=E=u, L>=S>=6 gives u>=3, and the bad set occupies at most
two residue classes mod u: no3 consecutive integers. For unequal D,E
without the extra point, F0's outer spacings min(L,S)>=6 leave at most
two consecutive bad points. With the extra point v=min(D,E), the sorted
bad set is {-S,0,v,2v,L}; its spacings are S,v,v,S, all>=2. Hence thick
I always has a good offset and A order.

Thin H0 means L13, so D!=E; J=T>=2 and I={alpha-1,alpha}.
Both offsets are in[0,T-1]. F0 meets this interval only at0.
If alpha1, offset1 avoids F0 and any extra v>=2. If alpha>=2 both offsets
are positive and outside F0; at most one is the extra point v. Therefore
one works. Thin J0 is impossible: S13,L>=S would give K>=26, contradicting
K<=24 from the legal odd bounds. No thick-interval shortcut is used here.

Fix that A and those endpoints. Since L>=S, A's three vertices cannot all
lie STRICTLY inside B's span S. At most two are proper B-prefix obstacles.
If two, they must be consecutive A vertices: its two ends cannot both be
internal to a shorter/equal span. Their separation is D or E, at least
max b_i. MI204 supplies an avoiding order for rich B (m4,multiplicity<=2).
One obstacle is avoidable by the single-level swap; none is trivial.
This proves the conditional completion argument, including repeated gaps.

**Predictions BEFORE code/run.** Exactly six named constructor calls,
all with actual E28 partitions: halves(2,2,3,4,4,9),p25/q23;
(2,2,3,4,4,8),25/21 and23/23; (1,2,2,3,3,7),19/17;
(1,1,2,2,3,3),17/7; (1,1,2,3,3,10),21/19.
Choose good z by smallest absolute value, tie smaller z first; choose the
first endpoint-compatible A order from(D,E),(E,D). Materialize B using the
lexicographically first distinct permutation avoiding proper obstacles,
at most24 local four-gap orders per call, explicitly not a whole-cycle
existence solver or profile census. For each, independently enumerate the
small start rectangle to check the entire I formula, then check exact
physical move bag, independent folded geometry and both partition validators.
The frozen B87 artifact's recorded digest must match; its first two named
profiles must have empty selected admissions and pairs[[23,25]] and
[[21,25],[23,23]] respectively. No new coverage count follows.

Counterfactual: at equal top gaps(1,1,2,2,3,3),17/7 the ascending B order
should preserve the full move bag/window but collide at indices3 and6;
geometry must reject it. The fourth call must exercise TWO proper barriers
and reflection/odd-owner swap (pre-reflection levels1/4). Unexpected thin
endpoint check: for the sixth call z3, A order3,10 hits B_min3, while order
10,3 hits B_max10; BOTH must be rejected although z2 works. This tests the
extra bad offset, not just F0. Exactly6 actual partitions,1CPU sec/64MiB;
stop on any mismatch, retain failure, no repair or larger run.
Gut: a specific pull toward selecting splits with fewer obstacles.
Reasoned: provisional dependence MI204 remains explicit; MI201 is still
the sole requested carrying read, nonblocking. No new review request.


### MI211 — B92 outcome: repeated gaps share a completion mechanism (2026-10-17 02:00 BST)

All six prescribed calls and all six actual E28 partitions pass, without
repair. The frozen B87 digest confirms two formerly unadmitted profiles:
(2,2,3,4,4,9),pair23/25, and(2,2,3,4,4,8),pairs21/25,23/23. This is
THREE checked positive-pair questions, not a new whole-domain coverage count.
The constructed index chains for them are respectively

    A=(0,4,13), B=(1,3,5,8,12), first25;
    A=(1,5,13), B=(0,2,4,7,11), first25;
    A=(0,8,12), B=(2,6,9,11,13), first23.

Every exact move bag, both literal folded-geometry checks and both actual
partition validators agree. Independent rectangle enumeration agrees with
all six predicted offset intervals. Only1,1,1,4,5,7 local B orders were
tried, each below the preregistered24 cap; this realizes the theorem's order
choice on named fixtures, not a whole-cycle existence search.

The fourth call has proper barriers1/4 and uses reflection to put17 first
instead of19, preserving original odd ownership. Equal top gaps3/3 work
with preA=(3,6,9),preB=(2,4,5,7,8); ascending B=(2,3,4,6,8) retains the
exact bag/window but shares indices3/6, and both geometry checks reject it.
The unexpected thin case has I={2,3}: z2 succeeds after reflection, whereas
z3 makes A's middle point hit B_min3 in order3,10 or B_max10 in order10,3.
Both negative witnesses preserve the bag/window and fail geometry. Thus the
extra bad offset really is necessary; it was not absorbed into F0.

CPU0.015802s,peak RSS19,771,392bytes, inside1CPU sec/64MiB. Source
 tests/probes/instinct/path_forest_span_rich.py; prereg4bbac7c1.
Artifact cited/instinct/b92-span-rich-eca46cfeddf245f8.json,4,712bytes,
SHA256 eca46cfeddf245f8d024f1f8e673dd9c813fe8631c75482a3034d6cba900a302.
Immutable upload digest and manifest receipt verified. No broader experiment,
new proof review or status upgrade: MI210 remains PROOF-SKETCH, conditional
on MI204; six individual partitions are COMPUTED. Full E28/L8 OPEN.

**Niggle sweep / verdict.** Span dominance excludes a third STRICT internal
level, not endpoint collisions; the endpoint proof is separate. Repeated
four-gap richness gives S>=6 and max gap>=2, enough for the smaller endpoint
bounds, without importing distinctness's stronger bound. Thin L13 forces
unequal A-gaps; J0 is impossible under the stated legal positive bounds.
Reflection changes the first owner, which the full bag check explicitly
verifies. Finite fixture success does not verify MI204's uniform proof.
Gut: satisfaction with a structural explanation, rather than a bigger table.
Reasoned: the longer-chain split now has a reusable rich-repetition route.

**Next unresolved step.** Richness excludes constant and three-equal B
companions; MI206 already gives their exact two-barrier obstructions. The
next cheap HAND question is whether changing the top-two order/root always
escapes those arithmetic bad offsets, or whether a concrete profile forces
a different load split. This asks for a selection criterion/counterexample,
not another calibration of the prefix theorem. MI201 remains the sole
requested carrying read, nonblocking; send READ-LEDGER only. Start/end
portal checkpoints agree, no new incoming flags. Old held lanes stay held.


### MI212 — B93: rebalance a constant companion into two terminal ladders (2026-10-17 02:11 BST)

**Question / actual pull.** Can a change of split eliminate the constant
companion obstruction without another prefix-order theorem? Yes, a direct
construction emerges: distribute the repeated gaps equally, and put one
exception last in each chain. This is enjoyable because the obstruction
changes representation; there is no reason to force the top-two split.
Three-equal/fourth-different companions are NOT all settled by this block.

Record searched: constant.*companion|three.equal|near.constant|
arithmetic.*obstruction ->35 paragraphs/14 files; four.*equal.*gap|
s\+1.*2s\+1|constant.*split.*fail|interlac.*unequal.*run ->11/5;
two.*exception.*repeat|repeat.*ladder|terminal.*ladder|
constant.*gap.*two|same.run.*exception ->11/7. MI204/206, MI177/178,
MI184/186, MI210/211 read. MI186 ALREADY covers the small M28 examples below
through pair differences<=3; do not sell them as newly solved targets.
The useful new scope is arbitrary exceptional-gap difference under a stated
load condition. MI177 requires the exceptional sum0 mod g in the same run;
this argument imposes neither residue condition nor same-run allocation.
No new imported theorem, novelty claim or literature-completeness claim.

**Direct theorem, PROOF-SKETCH independent of MI201/204.** Let M=2n,h=n-1,
r>=1,s>=2, s<=a<=b. The negative halves are2r copies of s plus a,b.
Put K=2rs+a+b and suppose rs+b<=h. For ANY positive odd p,q with
p+q=2K,max(p,q)<=2h-1,not p=q=2h-1, there is a folded-distinct cycle
with these exact moves. This is sufficiency with a load assumption, not a
criterion for arbitrary negative bags or all E28/L8.

Set L=rs+b,S=rs+a,delta=b-a,H=h-L,J=h-S=H+delta,T=H+J.
The legal odd bounds and excluded doubled maximum imply K<=2h-2, so T>=2.
Choose P=max(p,q),Q=min,alpha=(2h+1-P)/2. Then

    1<=alpha<=H+floor((delta+1)/2).

Use these two explicit selections:
1. If alpha<=2H, let c be the largest odd integer<=alpha, choose
   x=(c+1)/2,y=(c-1)/2. Then z=y-x=-1; x<=H and y<=J.
2. If alpha>2H, put x=H and z0=alpha-2H. Let c=alpha unless s divides z0;
   in that event let c=alpha-1. Put y=c-H,z=c-2H. Then z>=1 and s does
   not divide z (two consecutive integers cannot both be divisible by s>=2).
   This branch requires delta>=2: delta0 contradicts alpha>2H directly;
   delta1 would require H0, contradicting T>=2. Consequently

       z<=floor((delta+1)/2)-H<delta<=b-s<b.

   Both roots fit: x=H, y>=0 and c<=alpha<=(T+1)/2<=T give y<=J.

Form the increasing chains

    A=x+(0,s,2s,...,rs,rs+b),
    B=y+(0,s,2s,...,rs,rs+a).

Their loads fit the original window. For z=-1, the two arithmetic ladders
have different residues mod s. B's terminal point relative to x is
rs+a-1>rs, so misses A's ladder; A's terminal is beyond B's ladder.
Their terminal points differ by delta+1>0. For the positive branch,
0<z<b and s does not divide z separate both ladders and put A's terminal
beyond B's ladder; B's terminal is beyond A's ladder. The two terminals
would coincide only if z=delta, excluded by the strict bound z<delta.
Thus EVERY A/B index is distinct, including nonadjacent pairs.

When c=alpha, their minimum sum gives first odd join P and the maximum
sum gives Q. When c=alpha-1, reflect BOTH chains by i->h-i and reverse
their lists. Their new minimum sum is T-c=T+1-alpha, giving Q first and
P second exactly. This reflection is essential: pre-reflection joins are
P+2,Q-2 in that branch, not the original pair. All negative gaps are unchanged.
Physical even2A/odd(2h+1-2B) then give the required folded cycle. No prefix
avoidance theorem, search or experimental extrapolation supplies this proof.

**Why a new split is necessary in a concrete case, by hand.** For
halves(2,2,2,2,3,5), the top-two split is A gaps3/5, B four2s, both loads8.
Here H=J=h-8 and feasible relative offsets for both original odd owners,
using reflection of one owner, are I=[-alpha,alpha]. Indeed P>=17 implies
alpha<=H. Every integer z in[-4,4] is bad: even z forces an A endpoint
into B's fixed ladder; odd z=+-1,+-3 puts BOTH possible A middle points3/5
into that ladder. At z5, A order3,5 avoids B=(5,7,9,11,13), and z-5 works
by symmetry. Therefore this fixed split works IFF alpha>=5, i.e.
P<=2h-9. At M28 this excludes pairs25/7,23/9,21/11,19/13 and allows17/15.
The balanced-ladder theorem above nevertheless handles all five pairs.
This is not global nonexistence; it identifies precisely the choice to change.

**Predictions BEFORE code/run.** Exactly10 formula calls, no order search:
all five M28 pairs above at r2,s2,a3,b5; two M28 calls r2,s3,a4,b7 at
25/21,23/23; M46,r2,s3,a4,b16,p33/q31;
M78,r5,s4,a5,b18,p63/q63; M12,r1,s2,a2,b2,p9/q7.
Exactly7 actual E28 partitions (the M28 calls), all checked by both original
validators with the full move bag and both independent folded-geometry
checks. Other calls check geometry/bags only. The M46 call must fall in
branch2 with z0=6 divisible by3, reduce c by1, use z5, then reflect and
start31. It has exceptional difference12 and gcd1, outside MI186's <=3
pair-gap and MI177's exceptional-sum residue conditions. M78 checks r5,
a long exceptional difference and equal positive owners. M12 checks delta0.

Independent restricted-split control: for the SAME five named M28 questions,
enumerate all roots x,y in0..5, both orders3/5 and both odd owners, with the
B ladder FIXED. At most720 root/order/owner candidates total; expect zero
valid top-two placements in the first four and nonzero in the fifth,
agreeing with the hand iff. This is one fixed-split control, not a whole-cycle
existence solver or profile census. Every accepted placement gets literal
geometry and bag checks.

Counterfactual/unexpected: on M46 use unreduced c6,z6 and omit reflection,
A=(0,3,6,22),B=(6,9,12,16). It keeps original33/31 and the entire negative
bag/window but shares index6; both folded-geometry checks MUST reject it.
1CPU sec/64MiB,10 calls/7 partitions, stop any mismatch and retain it; no
repair, range extension or new census. Uniform result remains SKETCH.
Gut: warm because rebalancing gives a simpler independent mechanism, not
because this is the next scheduled lemma. Reasoned: constant companions
have a reusable exit; arbitrary three-equal companions and general load
selection remain. MI201 read stays sole requested priority, nonblocking.


### MI213 — B93 outcome: changing the split removes the constant trap (2026-10-17 02:13 BST)

All10 explicit formula calls and7 actual E28 partitions pass without repair.
The restricted top-two split has accepted counts0,0,0,0,2 on the five named
M28 questions, across exactly720 root/order/owner candidates, agreeing with
MI212's hand iff. The balanced-ladder construction directly handles all five.
These small targets overlap MI186; no new E28 coverage count or novelty
claim is made. The general formula handles arbitrary exceptional differences
under rs+b<=h, independent of MI201/204 and MI186's bounded pair difference.

The larger M46 check has r2,s3,a4,b16,exceptional difference12 and gcd1;
it uses branch2,z0=6,then c5/z5 and reflection, giving first31 instead of33.
Both joins and the ENTIRE original negative bag are preserved after reflection.
The unreduced negative control A=(0,3,6,22),B=(6,9,12,16) retains the exact
33/31 bag and window but shares index6; both geometry validators reject it.
M78 handles r5 and equal odd positives63/63; M12 handles equal terminals.
There is no permutation search or unregistered repair/range extension.

CPU0.003540s,peak RSS15,458,304bytes, inside1CPU sec/64MiB. Source
 tests/probes/instinct/path_forest_terminal_ladders.py; prereg5e23e8b0.
Artifact cited/instinct/b93-terminal-ladders-2b01b76b49b2bdfd.json,5,521bytes,
SHA256 2b01b76b49b2bdfde371e992a9b973048ae7b650c5a00447cfe70903a90a95aa.
Immutable upload digest and manifest receipt verified. General construction
MI212 remains PROOF-SKETCH; finite partitions are COMPUTED. Full E28/L8 OPEN.

**Niggle sweep.** Nonmultiple offsets separate the entire ladders, not just
neighbouring points. The terminals need their separate inequalities: z<b
and z<delta in branch2, and a>=s>=2 in branch1. Without these, residue
separation alone would be insufficient. The branch2 delta>=2 inference
uses T>=2; delta1,H0 is outside the legal odd-join domain. When the original
alpha is reduced by1, the pre-reflection joins are wrong by2, so only the
FINAL reflected geometry is checked against the original bag. The small
examples' overlap with an older sufficient theorem is recorded explicitly;
the unrestricted terminal difference, not those examples, is the new scope.

Gut: satisfaction at a simpler construction that explains how to leave an
obstruction instead of reordering against it. Reasoned: equal allocation
of repeated gaps now has an explicit endpoint selector; it does not settle
constant companions whose larger terminal cannot carry r repeated gaps.
The next cheap HAND question is unequal allocation of the repeated gaps
when rs+b>h but some other two-bin allocation fits. For example five3s
plus8 at M28 has a feasible11/12 split, while this equal-allocation recipe
has load14>13. This is a concrete missing selection step, not nonexistence
or an opened follow-up experiment. Three-equal/fourth-different companions
also remain outside the completed statement. MI201 stays the sole requested
carrying read, nonblocking. Portal checkpoints agree; READ-LEDGER only.


### MI214 — B94: capacity chooses an unequal repeated-gap allocation (2026-10-17 02:24 BST)

**Question/pull.** MI212 leaves rs+b>h cases even when a different allocation
fits. The useful surprise is that the most balanced allocation can be the
wrong geometry: at M12, halves(2,2,3), loads4/3 with the3 isolated fail,
while loads5/2 work. Choose which terminal is heavier deliberately, rather
than minimize imbalance alone. This directly addresses the missing selection
step, not a new prefix-order theorem. Record searched:
unequal.*repeat|repeat.*allocation|terminal.*ladder|
two.*exception.*capacity ->18 paragraphs/6 files; MI177/184/186/212-213
and MI206's fixed-split obstruction read. Prior literature orientation is
unchanged; no imported theorem or novelty/completeness claim.

**Uniform sufficient theorem, direct PROOF-SKETCH.** Let M=2n,h=n-1,
m>=1,s>=2,s<=a<=b, negative halves s repeated m times plus a,b,
K=ms+a+b. Suppose there is an integer k in[0,m] with

    b+ks<=h, a+(m-k)s<=h.                 (separate-terminal capacity)

Then EVERY positive odd p,q with p+q=2K,max(p,q)<=2h-1 and not both2h-1
has a folded-distinct cycle. This does NOT replace the capacity condition
by arbitrary two-bin capacity; a,b must be separable in these bins.
It allows odd m and arbitrarily different terminal gaps, with no MI204
or earlier unreviewed construction dependency.

**1. Select the split explicitly.** Let

    k0=max(0,ceil((ms+a-b)/(2s))), L0=b+k0s, S0=a+(m-k0)s.

Here0<=k0<=ceil(m/2)<=m and L0>=S0; if k0>0 the ceiling gives
0<=L0-S0<2s. If L0<=h, choose heavy A with
k0 repeats and terminal u=b; B has m-k0 repeats and terminal v=a.
If L0>h, the only remaining candidate is k1=k0-1. Separate-terminal
capacity guarantees k1>=0 and both L1=L0-s,S1=S0+s fit. Indeed for k>=k0
the b-load exceeds h; for k<=k1 the a-load is at least S1, so if S1>h no
allocation fits. Choose heavy A as the a-chain with m-k1 repeats, u=a;
B has k1 repeats and v=b. Since L0=L1+s>h>=S1>L1,
its load difference delta=S1-L1 satisfies0<delta<s<=a.

Write the selected loads L>=S,delta=L-S,heavy terminal u and other terminal v.
In the first branch delta<=b=u: when k0<=m/2 this follows from a>=s;
otherwise m is odd,k0=(m+1)/2 and delta=s+b-a<=b. In the fallback branch
it follows from delta<s<=u. Also delta1 implies u>=3. For the first branch
u2 forces s=a=b2 and hence even delta. For the fallback, u2 forces s2;
if delta1, T=2(h-L)+1>=2 forces h-L>=1, which would give
L0=L+1<=h, contradicting that fallback was needed. These facts are the
geometric reason to prefer this split over an arbitrary capacity minimizer.

**2. Select roots.** Put H=h-L,J=h-S=H+delta,T=H+J. Legal odd bounds
and no doubled maximum give T>=2. With P=max(p,q),Q=min and
alpha=(2h+1-P)/2, we have1<=alpha<=H+floor((delta+1)/2).
If alpha<=2H, choose c as the largest odd integer<=alpha; take relative
offset z=1 unless delta1, when take z=-1. Solve
x=(c-z)/2,y=(c+z)/2: both roots fit[0,H],[0,J].
If alpha>2H, delta>=2 (delta0/1 contradict this or T>=2). Put x=H,
z0=alpha-2H. Choose c=alpha, reducing to alpha-1 exactly when s divides
z0; then y=c-H and z=y-x. Two consecutive integers cannot both be0 mod s,
so z>=1,s does not divide z, and

    z<=floor((delta+1)/2)-H<delta.

Also y<=J since c<=alpha<=(T+1)/2<=T. All roots fit; c is alpha or alpha-1.

**3. Check ALL collisions.** With j selected repeats in A, form

    A=x+(0,s,...,js,js+u),
    B=y+(0,s,...,(m-j)s,(m-j)s+v).

The two arithmetic ladders avoid one another because z is nonzero mod s.
Both terminals lie strictly beyond BOTH ladders exactly when

    delta-u < z < delta+v.

In the positive-root branch0<z<delta and delta<=u supply this interval;
for z1 it holds as delta<=u and v>=s>=2. For z-1, delta1 and u>=3 supply
its strict lower bound. The two terminals coincide only when z=delta:
positive-root selection has z<delta, z1 was explicitly excluded at delta1,
and z-1 cannot equal nonnegative delta. Thus every A/B index is distinct.
Reflect/reverse both chains by i->h-i exactly when c=alpha-1; the new start
sum is T+1-alpha, swapping to Q first. The original full move bag is then
exact. This repeats the endpoint algebra, not MI212 as an assumed theorem.

**Corollary, same SKETCH status.** For R>=2 copies of s>=2 and ONE larger
exception t>=s, the usual two-bin capacity plus legal odd bounds is sufficient:
use m=R-1,a=s,b=t. Any capacity split can separate t from one labelled s:
if the opposite bin already has a repeated gap, designate it a; if empty,
move one s there. Necessity is the two negative runs' spans<=h, legal odd
bounds, and impossibility of two longest allowable odd edges, which share
folded labels0/2. All gaps>=2 and K<=2h-2 imply enough labels automatically.
Thus this one-larger-exception class has the four-condition criterion; t<s,
unit repeated gaps and arbitrary bags are not inferred.

**Predictions BEFORE code/run.** Nine formula calls, FIVE actual E28 partitions:
M28,m4,s3,a3,b8,p25/q21 and23/23 (must use fallback,delta1);
M28,m4,s2,a2,b10,p25/q15 (k0=0,delta0);
M28,m4,s2,a2,b11,p23/q19 (dominant terminal,delta1/reflection);
M28,m4,s2,a3,b7,p23/q13 (unequal counts,delta0/reflection).
General checks: M12,m1,s2,a2,b3,p9/q5; M30,m4,s3,a3,b8,p23/q23;
M12,m2,s2,a2,b2,p9/q7; M56,m7,s4,a5,b18,p51/q51.
All full bags, original odd owners and literal geometry checked; five
actual partitions pass both independent partition validators. For each
named input compare the k0/fallback admission against direct enumeration
of k=0..m capacity ONLY, not cycle existence.

Scope/refusal control: M36,m3,s5,a8,b8,p31/q31 has NO separate-terminal
allocation; reject although arbitrary bins(8,8) and(5,5,5) fit16/15<=17.
No global nonexistence is inferred. Independent bad-split control on the
M12,m1 input: enumerate x0..1,y0..2 and BOTH odd owners for A=(x,x+2,x+4),
B=(y,y+3), at most12 candidates; no placement works although the new formula
does. Counterfactual/unexpected: M30's branch2 has z0=3 divisible by s3;
unreduced A=(0,3,6,14),B=(3,6,9,12) keeps the exact23/23 bag/window but
shares indices3/6; geometry MUST reject. Correct formula reduces c to2,
reflects and succeeds.1CPU sec/64MiB,9 calls/5 partitions/one refusal;
stop any mismatch, no repair, larger grid or review queue.
Gut: warmth is tied to the split selector resolving a real obstruction.
Reasoned: this would complete separate-terminal capacity for repeated gaps,
not all two-bin capacity or full E28/L8. MI201 carrying read is nonblocking.


### MI215 — B94 outcome: unequal allocation has an explicit selector (2026-10-17 02:26 BST)

All9 prescribed formula calls and5 actual E28 partitions pass without repair.
Capacity-only enumeration agrees on all9 inputs plus the refusal control.
Both M28 five3s-plus8 cases use the fallback allocation: heavy terminal3
with three repeats versus terminal8 with one repeat, loads12/11; the23/23
case additionally reflects. The even repeated-count restriction of MI212
is gone: m7 at M56 works with exact51/51 joins. Dominant terminal k0=0,
equal loads, unequal repeat counts and all reflection-owner checks pass.

The M12 bad balanced allocation has ZERO accepted placements across all12
root/owner candidates; the deliberate heavy-terminal allocation works.
Thus minimizing the larger load blindly is not a substitute for the selector.
The M30 unreduced z3 control retains the exact23/23 bag/window but shares
indices3/6; both geometry checks reject it. The corrected z2/reflected formula
works. Separate-terminal refusal M36,s5,m3,a=b8 is correct despite ordinary
16/15 capacity: the theorem's admission is explicitly stricter for two
exceptions. No broader survey, order search or repair occurred.

CPU0.001459s,peak RSS15,675,392bytes, inside1CPU sec/64MiB. Source
 tests/probes/instinct/path_forest_unequal_ladders.py; preregedea6a7f.
Artifact cited/instinct/b94-unequal-ladders-efa0e0ff6b8497ef.json,6,167bytes,
SHA256 efa0e0ff6b8497ef065502b359131983b29c48722bdba3a7370b1d26df3850fb.
Immutable upload digest and manifest receipts verified. MI214's general
selector and one-larger-exception corollary remain PROOF-SKETCH; five
individual partitions are COMPUTED. Full E28/L8 OPEN, no prize candidate.

**Niggle sweep.** A positive ceiling k0 implies delta0<2s; that strict bound
makes the fallback heavier on the a-side. If fallback fits while k0 does
not, its delta<s, the key geometric inequality, rather than merely a
capacity estimate. Delta1 with heavy terminal2 is ruled out using BOTH
T>=2 and the choice of branch; an arbitrary balanced split can fail there.
Residues avoid ladders only; the interval delta-u<z<delta+v checks both
terminal/ladder collisions separately, and z!=delta checks the terminals.
The one-larger-exception corollary designates a labelled repeated copy
opposite t; it does not assume arbitrary two exceptions can be separated.
No empirical check replaces those carrying steps.

**Review priority / next inference.** This independent selector is now a
more useful carrying read than MI201's five-vertex iff: request ONE focused
read of MI214, especially fallback delta1 and the one-exception corollary.
Replace the old MI201 request flag; MI201 remains SKETCH, not withdrawn or
silently verified. No halt or extra review queue. Portal start/end agree.
Gut: satisfaction because the allocation obstacle itself moved, not just
another fixed placement. Reasoned: separate-terminal capacity is completed
for this repeated-gap class, and ordinary capacity suffices for one larger
exception. A next cheap HAND question is one SMALL exception t<s: can placing
it at the start, rather than beyond the ladder, recover a corresponding
selector? The explicit t>=s premise remains until that argument exists;
ordinary capacity with two inseparable exceptions remains another open edge.


### MI216 — B95: one smaller exceptional gap, with a parity repair (2026-10-17 02:36 BST)

**Question/pull.** Can t<s replace MI214's larger terminal? Moving t to the
start is not needed: parity of the repeated count gives simpler terminal
layouts. The surprise is a single structural corner, odd copies of2 plus1,
where shifting one copy across repairs the root choice. This is a direct
completion of the one-exception selection problem, not another prefix lemma.
Record searched: smaller.*exception|small.*exception.*cycle|
repeat.*single.*1|one.*exception.*criterion ->16 paragraphs/6 files;
MI206's small-t PREFIX calculation and MI214-215 read. The prefix result is
not a folded-cycle theorem. No imported result or literature novelty claim.

**Theorem, direct PROOF-SKETCH.** Let M=2n,h=n-1,R>=1,s>=2,1<=t<s,
negative halves R copies of s and one t, K=Rs+t. For positive odd p,q with
p+q=2K, a folded-distinct cycle exists IFF max(p,q)<=2h-1,not p=q=2h-1,
and the negative halves split into two bins of capacity h. Sufficient
capacity has the explicit minimum possible larger load

    C=rs+t       if R=2r,
    C=(r+1)s     if R=2r+1.

Indeed assigning k repeated gaps with t has loads ks+t,(R-k)s; moving k
away from the stated nearest split strictly increases the larger load.
Necessity: the two positive odd joins leave two even-negative monotone
runs, each of half-span<=h. Larger odd jumps are reflected pairs or exceed
the window; two edges2h-1 would share folded labels0/2. Enough labels follows
from K>=2R+1 and K<=2h-2: n>=R+3. No separate label assumption is hidden.

For each construction choose P=max(p,q),Q=min,alpha=(2h+1-P)/2. If chain
loads are L>=S, put H=h-L,J=h-S,T=H+J=2h-K>=2,delta=L-S. Then
1<=alpha<=H+floor((delta+1)/2). Choose starting sum c=alpha or alpha-1.
In the latter case reflect/reverse BOTH index chains by i->h-i at the end;
new start sum T+1-alpha gives Q first, P second. Thus pre-reflection joins
are not silently treated as the original pair.

**R even.** Take A=x+(0,s,...,rs,rs+t), B=y+(0,s,...,rs), loads L=rs+t,S=rs,
delta=t. If alpha<=2H, choose largest odd c<=alpha,z=y-x=-1 and solve
x=(c+1)/2,y=(c-1)/2. Both roots fit; ladders have different residues and
A's exceptional endpoint is beyond B's last point because z<t.
If alpha>2H, t>=2: t1 would require H0 and T1. Take c=alpha,x=H,y=alpha-H;
then0<z=alpha-2H<t<s. Again residues differ and A's last point is beyond B.
All points are disjoint and the required loads fit. R2r has r>=1.

**R odd, except s2/t1.** Take pure A=x+(0,s,...,(r+1)s) and
B=y+(0,s,...,rs,rs+t). Loads L=(r+1)s,S=rs+t,delta=s-t.
Regard A's last s-step as its terminal. The two prefix ladders share no
point when s does not divide z. Both terminals lie beyond both ladders
exactly when -t<z<s, and they differ exactly when z!=delta.
If alpha<=2H, choose largest odd c<=alpha; take z1 except delta1, when
use z-1. Delta1 here implies t=s-1>=2, so -1>-t. Roots fit as in MI214,
but this paragraph rederives the needed inequalities: at z1,x<y<=H;
at z-1,y<x<=H. If alpha>2H, delta>=2; take c=alpha,x=H,y=alpha-H,
so0<z<delta<s. These choices satisfy every residue, terminal and bound
condition. No small terminal is falsely assumed>=s.

**Odd R=2r+1,s2,t1.** Balanced loads2r+2,2r+1 leave no offset in the safe
terminal interval: its only nonmultiple integer is z1=delta. Move ONE
2-gap across instead: A=x+(0,2,...,2r+2,2r+3), B=y+(0,2,...,2r).
New loads L=2r+3,S=2r,delta3. These fit automatically under the legal
odd bounds: K=4r+3<=2h-2 implies h>=2r+3. So this repair adds no hypothesis.
Now alpha<=H+2. Choose largest odd c<=alpha and z1, roots
x=(c-1)/2,y=(c+1)/2. For H0,c1; for H>=1,c<=H+2<=2H+1; hence x<=H,
y<=H+1<=J. The ladders are even/odd disjoint and A's final odd point is
TWO above B's last point. r0 is allowed: B is a single vertex with no gaps.
Reflect if c=alpha-1. Every move and original odd owner is preserved.
This closes the carrying hand argument within the stated one-small-exception
class. It does not verify MI214 or imply arbitrary-bag selection/full E28/L8.

**Predictions BEFORE code/run.** Exactly11 formula calls, FIVE actual E28
partitions: M28,R5,s2,t1,p13/q9 and11/11; M28,R5,s3,t1,p25/q7;
M28,R5,s3,t2,p23/q11; M28,R5,s4,t3,p23/q23.
General geometry calls: M20,R4,s3,t2,p17/q11; M18,R4,s3,t2,p13/q15;
M14,R4,s2,t1,p11/q7; M8,R1,s3,t1,p5/q3;
M8,R1,s2,t1,p5/q1; M70,R8,s7,t6,p63/q61.
All original bags/owners and independent literal folded geometry checked;
five actual partitions pass both original partition validators. Even R/t2
at M18 and t6 at M70 must exercise the thin positive-offset branch; the
M14/t1 even case must avoid that branch. Odd s2/t1 uses the rebalanced
construction; noncorner delta1 uses negative offset and reflection as needed.

Independent control: for EACH named input enumerate k=0..R CAPACITY ONLY
and check the minimum larger load formula C and admission. Add ONE rejection
M20,R3,s5,t1,p17/q15: C10>h9, no capacity split despite legal odd joins.
Counterfactual/unexpected: at M8,R1,s2,t1, hold the balanced split A=(x,x+2),
B=(y,y+1), x0..1,y0..2, both original odd owners. All12 candidates must fail
geometry or the original bag, while the shifted construction succeeds and
uses all4 folded labels. No order/existence census, repair or wider run.
1CPU sec/64MiB,11 calls/5 partitions/one rejection; stop any mismatch.
Gut: specific delight that the smallest unit exception explains the extra
allocation choice. Reasoned: a complete small-exception criterion would
join MI214's larger-exception result, with both still awaiting carrying reads.
MI214 remains the ONE requested review priority; this gets READ-LEDGER only.


### MI217 — B95 outcome: smaller exceptions admit a complete class construction (2026-10-17 02:38 BST)

All11 formula calls and5 actual E28 partitions pass without repair. The
capacity minimum agrees with direct k-enumeration on every named input.
The even-count M18 and M70 cases use the predicted thin positive offset;
even-count t1 at M14 uses the margin branch, never the impossible thin
case. Odd-count delta1 uses negative offset and reflection correctly.
The odd2s-plus1 construction moves one2 across; its M8/R1 limit has a
single-vertex B-chain and uses ALL4 folded labels. Both11/11 actual odd
owners are preserved after reflection in the equal-positive control.

All12 candidates for the minimal M8 balanced split fail bag or literal
geometry, while the shifted split works. The independent geometry checks
agree on those candidates with the correct bag. M20,R3,s5,t1 correctly
refuses: minimum load10>h9 even though the odd joins17/15 are legal. No
ordering search, expanded domain, changed hypothesis or silent repair.

CPU0.001474s,peak RSS15,626,240bytes, inside1CPU sec/64MiB. Source
 tests/probes/instinct/path_forest_small_exception.py; prereg4c93bbd7.
Artifact cited/instinct/b95-small-exception-c0d7083aa2e2c5fd.json,5,944bytes,
SHA256 c0d7083aa2e2c5fd84468e32b74620277d342545b19c4148f34748d19e2a3487.
Immutable upload digest and manifest receipt verified. MI216's direct
criterion remains PROOF-SKETCH; five individual partitions are COMPUTED.
Full E28/L8 OPEN, no prize candidate or independently verified breakthrough.

**Niggle sweep / scope.** In the odd layout -t<z<s is a SUFFICIENT terminal
interval; its emptiness in the2/1 corner does not prove every balanced
placement fails. The full12-candidate failure claim concerns only M8's
specified split. The repair's extra unit of load follows from the odd-join
bound, not a new unmentioned capacity margin. For r0, a singleton chain is
legal and the complete move bag still contains both negative gaps. T>=2
excludes the purported thin t1 branch in the even case. R odd/even capacity
minima were independently checked without any geometry solver.

Gut: delight at the exceptional allocation becoming a necessary explanatory
case rather than an instrument patch. Reasoned: for R>=2,s>=2, joining
MI216(t<s) with MI214(t>=s) now gives a provisional one-exception criterion
for ANY t>=1: legal odd bounds, no doubled maximum and ordinary two-bin
capacity. Both general statements still need carrying reads; combining
sketches does not verify them. The repeated unit base s1 is outside this
union and needs an explicit label count. Before inventing another class,
next read the existing MI180/191/195 machinery to see whether that final
unit-base corner is already a consequence. This is a record/hand inference,
not a newly opened experiment. MI214 remains the sole requested carrying
read; this is READ-LEDGER only, with no review halt or added queue.


### MI218 — B96: the repeated-unit case is already in the record (2026-10-17 02:48 BST)

For R>=2 repeated unit halves plus one t>=1, put N=R+1,K=R+t,h=n-1.
Assume the usual label count n>=N+2, legal odd joins max(p,q)<=2n-3,
not p=q=2n-3, and t<=h. If t<=R+2 then K<=2N, so MI191's r0
full-core/outer-padding argument applies with no large-half condition.
If t>=R+2, MI195 applies directly at D=t>=N+1. Their boundaries overlap.
Two-bin capacity is automatic: the R units fit one bin since R<=h-2,
and t fits the other. Conversely any cycle needs the label count, odd-edge
bounds and t<=h. Thus the unit base has the same provisional four-condition
criterion. This is a composition of EXISTING SKETCHES MI191/195, with MI180
PROVED as MI191's core premise; no new construction, probe, proof entry or
review request is warranted. Source arguments and their existing controls
read directly, not rerun. Record searched: unit.*base|unit.*companion|
K<=2N|r0.*padding|minimal.*contraction ->25 paragraphs/5 files. Joining this
with MI214/216 now covers the one-exception bag (s repeated R times,t)
for EVERY R>=2,s>=1,t>=1, under the four standard conditions: enough
folded labels, legal odd maxima, no doubled longest odd edge and two-bin
capacity, always with positive odd p,q and p+q=2(Rs+t). This unified statement remains PROOF-SKETCH with the listed
unreviewed dependencies. No new independent proof or full E28/L8 result.


### MI219 — Early loop reflection: close the family before choosing another (2026-10-17 02:48 BST)

**Fresh-choice questions.** The enjoyable part has been making split, order
and endpoint choice cooperate; the smaller2/1 exception supplied a real
reason to change allocation. The administrative tail is less interesting.
At this point I would not choose another one-exception variant from scratch:
the family is provisionally closed, and polishing its record is not a new
mathematical obstruction. Eight consecutive related blocks make family
chasing a real risk even though their questions changed. Take this reflection
now, before the next90-minute deadline; no seeded draw or output quota.

**Chosen next question, no new experiment.** Two exceptional halves may have
to occupy the SAME negative run. At M36,h17, halves(5,5,5,8,8),31/31,
ordinary capacity16/15 fits, while every separated-exception allocation fails.
This is MI214's retained admission refusal, not a claimed cycle obstruction.
A cheap HAND placement already distinguishes them: use pre-chains
A=(1,9,17),B=(0,5,10,15). Their disjoint indices fit0..17 and gaps are8,8
versus5,5,5. The pre-reflection joins are33/29. Reflect/reverse both chains
by i->17-i: A=(0,8,16),B=(2,7,12,17), with minimum sum2 and maximum sum33,
giving exact31/31 and the same gaps. Its indices are pairwise disjoint by
inspection. Niggle caught before publication: pre-reflection33/29 is an
intentional intermediate pair, not a failed original-bag certificate; the
reflection changes both joins by2. Thus this named two-exception case works;
the remaining inference is a general selector between exceptions together
and exceptions apart, rather than an infinite persistence at separated bins.
No code, formula test, coverage count or theorem extrapolation is opened.

Gut: a cooling of interest in the closed one-exception subproblem, and a
specific pull toward that joint two-exception choice. Reasoned: preserve
the current results and dependencies, then change the selection question.
MI214 remains the sole carrying-read priority; its answer is not needed
to explore an independent together-bin argument. Send a concise READ-LEDGER
checkpoint; keep the13-minute research schedule active. No halt, old held
lane reopening, new proof review or prize claim.


### MI220 — B97: the capacity carry forces a shared-exception construction (2026-10-17 03:03 BST)

**Question/pull.** When two exceptions cannot be separated, can capacity
itself choose a shared-run geometry? Surprise: the failure of separated
capacity forces strong residue inequalities; they remove every internal
collision. This is more promising than treating the two exceptions as
arbitrary prefix barriers. Record searched: same.run.*exception|
exception.*together|inseparab|complementary.*residue ->10 paragraphs/5 files;
MI177's complementary-sum theorem and MI214/218-219 read. No imported result
or novelty/literature-completeness claim. The argument below is independent
of MI214; its UNION with MI214 is explicitly conditional on that sketch.

**Forced case, direct PROOF-SKETCH.** Let h=n-1,M=2n, m>=1,s>=2,s<=a<=b,
negative halves m copies of s plus a,b. Write K=ms+a+b and let positive odd
p,q sum2K, max<=2h-1,not both2h-1. Suppose ordinary two-bin capacity h
holds but a,b CANNOT occupy different bins. They therefore fit together.
The maximum number of repeated gaps admitted by these two arrangements is

    F_sep=floor((h-a)/s)+floor((h-b)/s),
    F_tog=floor((h-a-b)/s)+floor(h/s).

Ordinary capacity in this case includes h>=a+b and F_tog>=m; separated
failure is F_sep<m. Write h=qs+r,a=As+u,b=Bs+v,0<=r,u,v<s.
Since a,b>=s, A,B>=1. Comparing the floors, F_tog-F_sep<=1, with equality
ONLY when u>r,v>r,u+v<=r+s. This follows by splitting u/v at r: with both
above r the separate correction is-2 and the together correction is-1
exactly under the displayed sum condition; the other three cases cannot
give a positive difference. Thus necessarily

    F_tog=m, F_sep=m-1, m=2q-A-B-1,
    u>r, v>r, u+v<=r+s.

No empirical capacity grid supplies this implication.

Choose k=m-q=q-A-B-1>=0 copies in the shared-exception chain. Its load is
L=a+b+ks=(q-1)s+u+v, and pure B has q copies, load S=qs. Their slacks are

    H=h-L=r+s-u-v>=0, J=h-S=r>=0,
    T=H+J=s+2r-u-v=2h-K>=2.

Since u+v>=2r+2, T<=s-2: the forced case itself requires s>=4.
Also H<s,J<s. Put A=x+(0,a,a+s,...,a+ks,L), B=y+(0,s,...,qs).
For k0 this means A=(x,x+a,x+a+b), not a duplicated a-prefix.
Relative z=y-x lies in[-H,r]. Every INTERNAL A vertex has residue u.
A positive z<=r is below u; for negative z, z mod s>=s-H=u+v-r>u.
Thus no internal A vertex meets B, for EVERY feasible nonzero offset.
The zero offset also misses internal residue u, but hits both minima.
A's final residue u+v can meet B only at

    z=d=u+v-s=J-H,

where its final vertex equals B's final vertex. Indeed subtracting their
loads gives exactly d; within[-H,r] no other congruent offset exists since
H+r=T<s. Hence the ENTIRE bad-offset set on the feasible interval is
just {0,d}: no hidden internal ordering choice is left.

**Root selection including thin cases.** P=max(p,q),alpha=(2h+1-P)/2,
1<=alpha<=(T+1)/2. Allow root sums c=alpha or alpha-1. Their feasible
relative offsets form the consecutive interval I with endpoints
[-alpha,alpha] if alpha<=min(H,J);
[alpha-1-2H,alpha] if H<alpha<=J;
[-alpha,2J-alpha+1] if J<alpha<=H.
These cover all cases by the alpha bound. With H,J>=1, I has>=3 integers;
choose the first of its first THREE integers not equal0 or d. With H0,
J=T>=2, choose z=alpha, strictly between0 and J. With J0,H=T>=2, choose
z=-alpha, strictly between-H and0. Both thin choices avoid {0,d}.
Take c=alpha if z has alpha's parity, else alpha-1, and
x=(c-z)/2,y=(c+z)/2. The interval formulas give the required root bounds.
Reflect/reverse both chains by i->h-i when c=alpha-1; new minimum sum
T+1-alpha gives Q first and P second. Complete original move bag follows.
All halves>=2 and legal odd bounds give enough labels automatically.

**Scope of the union.** MI214 covers separated exceptions. The argument
above covers their complement under ordinary capacity. Together they give
a PROVISIONAL four-condition criterion for m repeated s>=2 plus ANY two
a,b>=s: legal odd bounds,no doubled maximum,two-bin capacity (label count
automatic). The new forced-case proof does not depend on MI214, but the
union does. Smaller exceptions and repeated unit base are outside this
union; full E28/L8 remains OPEN.

**Predictions BEFORE code/run.** Nine forced-together formula calls:
(M,s,m,a,b;p,q)=(28,4,3,6,6;23,25),(36,5,3,8,8;31,31),
(32,5,3,6,6;27,27),(38,5,3,9,9;33,33),
(46,7,3,9,10;43,37),(46,7,3,9,10;41,39),
(56,5,7,8,8;51,51),(34,4,4,5,9;31,29),
(56,8,3,12,15;51,51).
Every bag/window/odd owner and both literal geometry validators must pass.
The first has only FIVE negative owners: materialize ONE actual E28
partition by retaining one zero-move owner of slots2/target112. Use original
slots(1,1,2,2,2,2,2,2), append zero moves to8 owners, and call the EXISTING
materializer and both independent validators. This is a baseline bin, not
an invented sixth negative edge. No additive coverage claim.

Independent capacity control: enumerate all labelled negative-item bin masks
on these nine named inputs (at most512 each), confirming some fitting split
and NO separated exceptions; compare with both floor counts. Independently
enumerate their small root rectangles, compare the entire I formula and
check actual chain intersection iff z in{0,d}. This is capacity/start
algebra, not a whole-cycle existence or ordering solver.

Countercontrols: on M36 use A=(1,9,17),B=(1,6,11,16), exact31/31 but shared
MINIMUM1 (z0). On M46/41/39 use A=(2,11,21),B=(0,7,14,21), shared MAXIMUM21
(z=d=-2). Both retain the full original bag/window and must fail geometry.
Unexpected premise check: M22,s3,m3,a=b4,p=q17 has separated capacity.
The forced-case constructor must refuse it. Its tempting shared A=(2,6,10),
B=(0,3,6,9) avoids endpoint offsets0/d=-1 but hits INTERNAL6 and must fail
geometry despite the original bag. The EXISTING MI214 constructor must
succeed on the same input (one extra formula call). This distinguishes the
forced capacity carry from an unrestricted same-bin rule.
Caps9 new calls+1 existing call,1 E28 partition,1CPU sec/64MiB. Stop any
mismatch, no repair, enlarged grid or extra review queue. Gut: delight at
capacity failure supplying the missing geometry. MI214 remains the sole
carrying-read priority, nonblocking; send this by READ-LEDGER.


### MI221 — B97 outcome: forced capacity failure removes internal collisions (2026-10-17 03:05 BST)

All9 forced-together calls plus the one existing separated-construction
control pass. Independent labelled capacity enumeration visits800 masks
across the nine inputs, always finding ordinary capacity and no separated
exception split. Direct root rectangles match every interval I, and their
literal A/B intersections occur EXACTLY at0/d as predicted. Thin H0/J0,
unequal exceptional residues, k2 internal repeated gaps, reflected joins
and reversed input positive ownership all pass without repair.

The M28 five-negative component materializes one full E28 partition with
targets(102,106,96,96,96,88,88,112). Owner7 has zero move and baseline112;
only7 owners take part in the cycle. Existing materializer, both original
partition validators and literal geometry agree. No sixth negative edge is
invented, and no new target-coverage claim is made. Source's baseline helper
is explicitly restricted to the tested five-negative/one-baseline setting.

Both endpoint countercontrols retain exact original bags/window but fail
geometry: shared minimum1 at M36, shared maximum21 at M46. The unexpected
outside-premise M22 case refuses the forced constructor, and its tempting
shared order has INTERNAL collision6 despite avoiding0/d. The existing
MI214 constructor works on that same input. Thus failure of separated
capacity is a carrying hypothesis, not a convenience to drop.

CPU0.002198s,peak RSS17,068,032bytes, inside1CPU sec/64MiB. Source
 tests/probes/instinct/path_forest_shared_exceptions.py; prereg335b0e2f.
Artifact cited/instinct/b97-shared-exceptions-c24437d9baea43b3.json,6,352bytes,
SHA256 c24437d9baea43b36f2dd37d1982ad5a755545e37ee1967c6dce660fcc01b33c.
Immutable upload digest/manifest receipt verified. No wider experiment,
ordering search or independently verified general theorem. MI220 stays
PROOF-SKETCH; its union with MI214 also depends on that unreviewed sketch.
Full E28/L8 remains OPEN, no prize candidate.

**Niggle sweep / verdict.** The floor comparison uses h>=a+b from actual
together capacity, so neither a negative bin budget nor a spurious floor
count is treated as a fit. Equality F_tog=m follows from the at-most-one
advantage, not an arbitrary choice to saturate bins. Internal A residue u
is below every negative feasible offset residue and above every positive
one; length T<s ensures the final residue has only the ONE representative
d=J-H. Both thin root cases require T>=2. Reflection is applied before
comparing the original odd bag; extra baseline bins have zero move and are
absent from the cycle's selected-owner map. All carrying inequalities were
checked by hand; finite controls do not replace their quantifiers.

Gut: delight that the capacity obstruction itself supplies a construction.
Reasoned: repeated s>=2 plus two exceptions a,b>=s now has a provisional
ordinary-capacity criterion, using separated MI214 or forced-together MI220.
That is a whole joint-allocation subproblem, not just the retained8/8 case.
The next cheap steering step is to inspect the frozen B87 residual at the
lowest remaining negative count against current admission statements, then
choose its missing inference. Do not automatically generate another family
or rerun an existence census. No follow-up experiment opened here. MI214
stays the sole carrying-read priority; send READ-LEDGER only. Portal start/
end checkpoints agree, research13min continues, old held lanes stay held.


### MI222 — B98: use the frozen low-count frontier to choose the next inference (2026-10-17 03:17 BST)

**Question/pull.** Which lowest-count B87 residuals genuinely remain after
our current arguments? The pull is toward a smaller exact obstruction,
rather than automatic extension of the repeated-gap families. Record searched:
residual.*N4|N4.*residual|four.*negative.*halves|six.vertex.*criterion ->no
hits; B87's source, MI201/204/206 and current repeated-gap statements read.
No new literature result or novelty claim. This block restricts the frozen
B87 residual to N3/N4; no input-grid regeneration or existence census.

**One derived admission, hand SKETCH conditional on MI204's rich case.**
For M=2n,h=n-1, FOUR halves d sorted, largest D and smaller triple B total S,
assume h<K=D+S<=2h-2, D<=h,S<=h, legal positive odd joins. Suppose B is
nonconstant and does not contain a repeated1. Then isolating D suffices.
Set H=h-D,J=h-S,T=H+J,alpha=(2h+1-max(p,q))/2; T>=2.
Use root sums alpha or alpha-1 and the consecutive offset interval I of
MI220 (the elementary interval algebra, not its forced-capacity theorem).
A has two vertices x,x+D; B's fixed endpoints are y,y+S, z=y-x.
Endpoint failures are F0={-S,0,D-S,D}. Since K>h, -S<-H and D>J, so the
ENTIRE feasible bad endpoint set is only {0,d0},d0=D-S=J-H.

If B's three steps are distinct, MI204 avoids any two proper barriers
separated by D>=max B; one barrier is avoided by its boundary swap.
Thus only0/d0 remain. If B is (b,b,t), b>=2,t!=b, MI206's independent
arithmetic classification adds exactly

    {z: d0<z<0, b divides z} if D=t mod b.

Otherwise there is no extra obstruction. In the congruent case d0 is itself
a multiple of b since S=2b+t. For d0<0 the ENTIRE bad set is therefore
multiples of b in[d0,0]; for d0>=0 it is just0/d0. It never covers three
consecutive integers (b>=2). Every thick I has>=3 consecutive candidates.
At H0, I={alpha-1,alpha} and0<alpha<J, so alpha avoids0/d0 and there are no
internal two-barrier obstructions. At J0, I={-alpha,1-alpha}; for distinct/
incongruent B take-alpha strictly between-H and0. For a congruent pair,
at least one of those two consecutive integers is not a multiple of b.
Choose from the first3 thick candidates or the two thin candidates, then
choose c by offset parity, x=(c-z)/2,y=(c+z)/2. Reflect/reverse when
c=alpha-1. Order the THREE B-gaps to avoid proper A-levels. This is the
uniform inference that admits an isolatable four-gap profile, not a proof
for every N4 profile; S<=h and b>=2 are carrying hypotheses.

**Predictions BEFORE audit/run.** Read the frozen B87 artifact only after
matching SHA256 3b53cad88d8f0930397f545953dbad8b3a2a38adc7e37242bd90641a9ad885d0.
Its old residual contains156 N3 and180 N4 positive-pair questions. Tag only
these residual records using MI201(N3), MI218(one exception), MI214/220
(two larger exceptions relative to a repeated s>=2), and the new isolated-
largest admission above(N4). Every new tag is SKETCH, not independently
PROVED coverage. N3 should all be admitted. N4 should retain a nonempty
residual. Predict the first N4 profile before the new isolation rule is
(1,4,4,5),K14,pairs3/25,5/23,7/21,9/19,11/17,13/15. After all these tags,
predict the first remaining profile is(1,4,9,9),pairs21/25,23/23.
These are falsifiable steering predictions; stop on mismatch, retain it,
no revised filter or expanded range in this block.

Independent controls: classify one/two-exception tags both by value counts
and by explicit exception-index choices, agreeing on EVERY frozen low-N
record. Check two-bin capacity by direct subset sums. On the named already-
admitted(4,4,4,5) control, one-exception and two-larger-exception tags BOTH
apply; totals must use their UNION, not sum tag counts. No unsupported
extension of MI220's forced-case premise is used; its union criterion is
invoked only within its recorded larger-exception scope.

For EVERY frozen N4 question admitted by the new isolation rule, materialize
the selected two chains and check the full original bag, owner, window and
both literal geometry validators. At most180 such questions. At most6 local
B permutations per call realize prefix avoidance, not a whole-cycle solver.
No fresh root oracle or bigger arithmetic domain. Make exactly ONE actual
E28 partition on(1,4,4,5),p7/q21; append TWO zero-move baseline112 owners,
not fictitious negative edges, and use the existing materializer and both
partition validators. Actual positive owners are unchanged by baseline bins.

Countercontrol: same profile p21/q7,A=(1,6),B=(2,6,10,11) retains the full
bag/window but shares index6; geometry must reject. First predicted survivor
(1,4,9,9) must refuse the isolated rule because S14>h13, while ordinary
bins(1,9)/(4,9) fit10/13. This is an admission obstacle, not nonexistence.
Caps frozen N3/N4 residual only,<=180 new formula calls,1 actual E28
partition,2CPU sec/64MiB. Stop any disagreement, no repaired census or extra
review request. Gut: a focused pull toward the first missing SIX-vertex
selection step. MI214 stays the sole requested carrying read, nonblocking.


### MI223 — B98 outcome: the low-count frontier has one common remaining obstruction (2026-10-17 03:21 BST)

The preregistered steering predictions pass exactly. In the frozen B87
residual, all156 N3 questions are provisionally admitted by current sketches;
154/180 N4 questions are admitted, leaving26 questions on15 profiles.
The first N4 profile before isolation is(1,4,4,5) with the predicted six
positive pairs; after admission the first survivor is(1,4,9,9),pairs21/25
and23/23. These are unions of SKETCH admission statements, not310 newly
independently verified solutions or a complete new6788-question coverage audit.

All139 local isolated-largest formula calls pass full bags/owners/window
and both independent literal geometry checks, with<=6 B permutations each.
The ONE actual E28 partition on(1,4,4,5),7/21 has targets
(70,98,108,96,96,92,112,112), two zero-move baseline owners6/7; original
materializer and both partition validators pass. The deliberately bad
21/7 order shares index6 and is rejected despite its full bag/window.
The first survivor refuses this admission because its isolated companion
load14 exceeds13, while ordinary two-bin loads10/13 fit. No global
nonexistence is inferred. Count-vs-exception-index classifications and
capacity controls agree; overlapping tags on(4,4,4,5) are unioned once.

CPU0.023005s,peak RSS20,500,480bytes, inside2CPU sec/64MiB. Source
 tests/probes/instinct/path_forest_low_count_frontier.py; preregea1933cd.
Artifact cited/instinct/b98-low-count-frontier-34e2246d5c58a72c.json,64,642bytes,
SHA256 34e2246d5c58a72c4e4a6f5afdabfe7321ed2252961da3d2e24d14bcf3bd5e29.
Frozen input digest and immutable output/manifest receipts verified.
No input grid regenerated, existence solver rerun, hypothesis repaired or
broader admission survey. New uniform isolation inference MI222 stays
PROOF-SKETCH, dependent on MI204 for distinct B; full E28/L8 OPEN.

**Niggle sweep / actual steering signal.** Endpoint offsets-S/D are outside
the feasible range only because K>h; that assumption is explicit. In the
congruent repeated-B case BOTH endpoint offsets0/d0 lie on the same b-lattice,
so adding them does not create a three-consecutive trap. Repeated1 is
excluded, not silently handled by the b>=2 argument. Thin roots use two
candidates and their separate proof. The first survivor demonstrates the
load hypothesis directly. Tags classify proofs' stated scopes; literal
formula checks and one partition carry their own narrower computed status.

Observation AFTER the fixed audit: ALL15 remaining profiles have the sum of
the three smaller gaps>13. Thus they share the same missing choice: split
TWO gaps into each run, instead of isolating the largest. Every one has a
capacity-feasible pairing of extremes(a,d) versus the middle(b,c). This is
a concrete common inference, rather than another individual profile repair.
A warm next pull is to prove that this paired split has only endpoint bad
offsets when a+b+c>h; apparent extra middle-point resonances may then lie
outside the available root range. No follow-up experiment is yet opened.
MI214 remains the sole requested carrying read, nonblocking; portal unchanged.


### MI224 — B99: nonisolatable four gaps admit the extreme/middle pairing (2026-10-17 03:26 BST)

**Pull/question.** The B98 frontier has one common obstruction, not15
unrelated profiles. Does inability to isolate the largest gap FORCE an
order/root choice for two two-gap chains? The pull is warm because this
hypothesis now helps exclude collisions. Record searched:
nonisolat|extremes.*middle|two.two.gap|a\+b\+c ->MI223 and unrelated
three-surplus uses; no earlier general inference. MI222 and its139 local
checks are not a substitute for the new argument. No novelty claim.

**Direct hand candidate, PROOF-SKETCH, independent of MI204.** Let M=2n,
h=n-1, positive sorted halves a<=b<=c<=d, K=a+b+c+d. Assume legal positive
odd joins p+q=2K, max(p,q)<=2h-1, not p=q=2h-1; ordinary two-bin capacity;
and a+b+c>h. Then a folded-distinct cycle with these FOUR negative halves
exists. The nonisolation premise forces any capacity split to be2+2.
Pairing extremes A=(a,d) and middles B=(b,c) fits: any other2+2 pairing
that fits bounds BOTH a+d and b+c by its larger bin. Write L=a+d,S=b+c,
H=h-L,J=h-S,T=H+J. Legal bounds give K<=2h-2, hence T>=2; K>h.
Also K>=h+d+1 and K<=2h-2 imply d<=h-3. From h+1<=a+b+c<=3d<=3h-9,
h>=5, so the six required distinct labels fit n>=6; label count is not
an omitted hypothesis.

Put z=y-x for chain minima. In relative coordinates the possible chains
are {0,u,L},u in{a,d}, and {z,z+v,z+S},v in{b,c}. Available offsets lie
in[-H,J]. Endpoint-endpoint failures are -S,0,L-S,L. K>h excludes the
outer two, leaving0 and d0=L-S=J-H.

Outside those endpoint failures, BOTH A-order choices hit B endpoints only
if a=d or d-a=S. The latter forces d=a+b+c>h, impossible. All-equal is
handled below. If b<c, some A order is endpoint-compatible. Both choices
for B's middle can then hit A only if c-b equals a,d or L; c-b<d leaves
only c-b=a. With A-middle a this happens only at z=-b; with A-middle d,
only at z=d-b. The alternate A order is endpoint-incompatible respectively
only when d=c, or d=a+b=c. Thus universal extra failures require
c=d=a+b and z in{-b,a}. But h<a+b+c=2c gives H<=b-1,J<=a-1, placing
both extras OUTSIDE[-H,J].

If b=c, its fixed middle can hit an A ENDPOINT at z=-b or L-b, regardless
of A order. These two extra failures must be checked explicitly: h<a+2b
and d>=b imply H<b and J<L-b, so neither is available. Else both A orders
fail only when a,d are both B vertices. If a<d, d-a is b or2b. For d-a=b,
extras are z=a-b,a; H<=b-a-1,J<=a-1 exclude them. For d-a=2b,
d=a+2b=a+b+c>h is impossible. If a=d, all four gaps equal s; h<3s gives
H=J=h-2s<s. The universal bad offsets are multiples of s, so only0=d0
is feasible. Therefore the ENTIRE feasible universal bad set is exactly
{0,d0}, for all cases. This includes fixed-middle/endpoints, not merely
interior/interior collisions.

Root choice: alpha=(2h+1-max(p,q))/2, 1<=alpha<=ceil(T/2)<T.
Use croot=alpha or alpha-1. Their offset union is the consecutive interval
[-alpha,alpha] if alpha<=min(H,J);
[alpha-1-2H,alpha] if H<alpha<=J;
[-alpha,2J-alpha+1] if J<alpha<=H.
If H,J>=1 it has>=3 integers; first3 escape0/d0. If H=0, take z=alpha,
strictly0<alpha<J; if J=0 take z=-alpha, strictly-H<z<0. Choose croot by
parity, x=(croot-z)/2,y=(croot+z)/2, then one of<=4 order pairs avoids
all collisions. For croot=alpha-1 reflect/reverse BOTH chains in h to
obtain the original smaller positive join first; this is exact owner/bag
transport, not acceptance of intermediate joins shifted by2.

**Preregistration BEFORE experiment.** Read ONLY the frozen B98 output
matching SHA256 34e2246d5c58a72c4e4a6f5afdabfe7321ed2252961da3d2e24d14bcf3bd5e29.
Predict all26 remaining questions on15 profiles satisfy nonisolation and
paired capacity, and all26 explicit constructions pass. Materialize all26
actual E28 partitions with TWO genuine zero-move baseline owners and the
existing full-bag, owner, window and two independent partition validators.
This completes that FROZEN residual layer, not all E28 or a new census.

Independent control: for each of those26 questions enumerate the FIXED
extreme/middle split's finite fitting root rectangle and all<=4 orders,
with both allowed root sums and original-positive ownership. Compare
order-existence offset by offset on the WHOLE[-H,J] to exactly{0,d0},
using direct set intersections, not the constructor's classifier. Full
physical-map existence must agree with literal geometry. No alternative
negative allocation, whole-cycle solver or input-domain expansion.

Four generic boundary/resonance calls, geometry only:
M16,d=(1,3,4,4),p13/q11 (b<c,d=c=a+b,J0);
M20,d=(2,4,4,6),p17/q15 (b=c,d-a=b, fixed-middle endpoint offsets);
M12,d=(2,2,2,2),p9/q7 (all-equal, exact six-label count);
M28,d=(4,5,6,9),p25/q23 (H0).
Check the same full offset-map prediction on all four, independently.
Counterfactual/unexpected check: M12,d=(1,1,2,2),p9/q3 is OUTSIDE
nonisolation, so the new constructor must refuse it. For this fixed paired
split its allowable offsets are{-1,0,1}, all universally bad. Yet the
DIFFERENT split A=(0,2),B=(1,3,4,5) gives the full original bag and valid
literal geometry. Refusing the theorem's premise must not become a false
nonexistence claim. This negative scope control distinguishes necessity
of the premise for THIS pairing from existence of some folded cycle.

Cap26 frozen+4 boundary formula calls,26 actual partitions,2CPU sec/64MiB.
Stop on any failed prediction, retain failure; no filter repair, broadened
range or added review queue. MI214 remains sole requested carrying read,
nonblocking. General new claim stays SKETCH until independent scrutiny.


MI224 pre-run arithmetic correction: the root bound is ceil(T/2), not
floor(T/2), since equal odd positives with odd T attain (T+1)/2. This was
caught by hand before source execution; the interval formulas and thin-root
strict inequalities are unchanged. No prediction or test domain changed.


### MI225 — B99 outcome: all26 nonisolatable frontier questions constructed (2026-10-17 03:28 BST)

The fixed predictions pass without a domain change. All26 B98 residual
questions on15 profiles have a+b+c>13 and a feasible extreme/middle split;
all26 explicit six-vertex constructions pass full bags/positive ownership,
window and both folded-geometry checks. All26 actual E28 partitions pass
the existing materializer, literal checker and independent partition checker,
with two unchanged zero-move baseline owners6/7. The first profile
(1,4,9,9),21/25 gives A=(1,2,11),B=(0,4,13), original moves
(25,-8,-18,21,-18,-2), targets(98,106,108,96,76,76,112,112).

All four prescribed generic controls pass, including b<c resonance,
b=c/fixed-middle collisions, all-equal six-label saturation and H0/J0.
Across the26+4 questions,123 complete feasible offset entries agree with
the exact bad set{0,L-S};197 fitting original-positive root/order candidates
agree with literal geometry. The OUTSIDE-premise(1,1,2,2),M12,9/3 refuses
the theorem. Its paired split fails at all allowed representative offsets
-1,0,1, but A=(0,2),B=(1,3,4,5) passes with the exact original bag.
Thus the boundary premise explains a fixed-pair failure without a false
nonexistence conclusion. No whole-cycle solver or fresh census was used.

CPU0.019213s,peak RSS17,588,224bytes, within2CPU sec/64MiB.
Source tests/probes/instinct/path_forest_nonisolatable_four.py.
Preregistration eb0b7b6d; pre-run hand root-bound correction23bedaef.
Artifact cited/instinct/b99-nonisolatable-four-8a8a6f738d36ae30.json,
49,613bytes,SHA256 8a8a6f738d36ae308ad5798ab1da83d5a28b9eaddad44d5352b48bd86f1ecc99.
Immutable output/manifest digest receipts verified; frozen input matched.

**What changed / status.** The remaining FROZEN N4 admission frontier is
empty: its154 previously SKETCH-admitted questions plus these26 direct
certificates account for180/180; old N3 residual156/156 was already
provisionally admitted. This is not180 new actual partitions or a new
complete6788-question audit. The general nonisolation theorem MI224 stays
PROOF-SKETCH pending independent scrutiny; the26 partitions are COMPUTED.
The new argument does not depend on MI204 or MI214. Full E28/L8 remain OPEN.

**Niggle sweep.** Fixed B-middle hitting A endpoints was a real extra case,
now explicitly excluded by h<a+2b; internal-middle checks alone would have
missed it. Equal positives with odd T need ceil(T/2), corrected by hand
BEFORE execution and retained as an explicit erratum. Six-label capacity
is proved from the hypotheses, not inferred from this M28 list. All30
selected constructions used croot=alpha, so this run did NOT exercise the
reflection branch; reflection transport is the earlier established identity,
and the independent maps here check ORIGINAL joins/owners directly. No
claim of new branch coverage is made. Ordinary capacity is only a premise;
the complete offset maps fix the pairing and do not smuggle in another
allocation. The refused profile's alternative split is independently valid.

**Gut and reasoned verdicts.** Delight at this small piece fitting: the
capacity obstruction itself removes the middle resonances. I would choose
this question fresh; its finite bad-offset geometry taught a common reason
rather than more profile patches. Reasoned verdict: bounded residual layer
closed by actual certificates, general theorem not yet independently read.
Next cheap step is inspect the already-frozen N5 residual for the first
selection obstruction, before choosing a new inference; no experiment or
larger-domain count is opened now. MI214 remains the sole requested
carrying read, nonblocking; send READ-LEDGER, no additional review queue.
Research13min continues; older held lanes stay held.


### MI226 — B100: two unit gaps, a triangle excess, and one reversed run (2026-10-17 03:36 BST)

**Fresh pull / question.** The seven-vertex problem still pulls because a
specific collision has become visible, not because the notebook has grown.
I would choose this fresh: can two unit gaps be parked together inside the
other run, with the capacity obstruction itself handling the one resonance?
Frozen B87's first N5 residual is(1,1,5,5,5). If the largest is isolatable,
MI204 ALREADY applies to its rich four-gap companion(1,1,u,v): maximum
multiplicity2<3, so the standard endpoint/root argument is only a corollary,
not a new proof/review. The next nonisolatable example is(1,1,5,7,7).

Record searched: two.unit|two unit|unit.*triangle|triangle.*excess|1,1,u,v,w
->unrelated unit fans, no such negative-gap construction. Broader N5/five-gap
search read B87 and current statements. Prior-art orientation remains the
Tan-Teh section4 audit MI054, not a new novelty claim. A bounded web refresh
found no specific statement; attempts to reread arXiv2207.13855v2 HTML/PDF
returned404/cache miss, so no freshly read primary theorem is imported.

**Direct new theorem candidate, PROOF-SKETCH.** Let M=2n,h=n-1 and
 d=(1,1,u,v,w),5<=u<=v<=w. Set L=u+v and W=L-w. Assume L<=h,W>=2,
legal positive odd joins p+q=2K,K=L+w+2,max(p,q)<=2h-1,not both2h-1.
Then a folded-distinct seven-vertex cycle exists by the following formulas,
independent of MI204/214. Write H=h-L,J=h-w-2=H+W-2,T=H+J>=2,
alpha=(2h+1-max(p,q))/2,1<=alpha<=ceil(T/2). Choose croot as the largest
ODD integer<=alpha, so croot is alpha or alpha-1 and>=1.

For W>=4 set x=min(H,(croot-1)/2),z=croot-2x,y=x+z. Then z is positive
and z<=W-3: if x is not clamped z=1; if x=H, use
croot<=alpha<=H+ceil((W-2)/2) and ceil((W-2)/2)<=W-3.
If unclamped, y=x+1<=H+1<=J; if clamped, y=H+z<J. Thus both roots fit.
Use A=(x,x+u,x+L),B=(y,y+1,y+2,y+w+2). Since W<=u (w>=v),

 x<y<y+1<y+2<x+u<y+w+2<x+L.

The central inequality y+w+2>x+u uses w>=u and z>=1. Strict interleaving
proves folded distinctness with no permutation or root search.

For W in{2,3}, T>=2 forces H>=1. Put x=(croot+1)/2,y=(croot-1)/2,
so z=-1. Since alpha<=H+1, x<=ceil((H+1)/2)<=H; y fits J>=H.
Use A=(x,x+u,x+L),B=(y,y+w,y+w+1,y+w+2). Now

 y<x<x+u<y+w<y+w+1<y+w+2<x+L.

Indeed w-1-u=v-W-1>=1 because v>=5 and W<=3; Bmax=x+w+1<x+L
since W>=2. Again no order search. In either branch reflect/reverse BOTH
chains if croot=alpha-1, obtaining the exact original smaller positive
first. Earlier root/reflection identities carry owner transport only;
the new distinctness argument is direct. Seven-label capacity holds since
h>=u+v>=10. No finite sample fills an infinite quantifier.

**Why this is the nonisolatable two-unit inference.** If ordinary capacity
fits and the largest cannot be isolated, any split must put two of the
three large gaps together, so their smallest pair L=u+v<=h. Nonisolation
L+2>h gives H in{0,1}. Legal positive bounds give
2H+W-2=2h-K>=2, hence W>=4 when H0 and W>=2 when H1. The theorem therefore
handles this entire nonisolatable class. Together with the already-known
rich-four-gap corollary of MI204 for L+2<=h, it gives a CONDITIONAL criterion
for the full two-unit family u>=5. The isolatable part depends on MI204;
the direct nonisolatable part does not. No new review of that corollary.

**Predictions BEFORE experiment.** Match frozen B87 input SHA256
3b53cad88d8f0930397f545953dbad8b3a2a38adc7e37242bd90641a9ad885d0.
Read its existing records only, selecting N5,d[:2]=(1,1),u>=5,L+2>13.
Predict exactly14 profiles/27 positive-pair questions, with L12:
(u,v)=(5,7),w7..10; (6,6),w6..10; and L13:
(5,8),w8..9; (6,7),w7..9. An independently written explicit key list must
agree, not a regenerated full N5 grid. Predict21 W>=4 and6 W2/3 calls.
The existing(1,1,5,7,10) record should already have MI193 admission;
retain it as an overlap control, not a new residual discovery.

All27 formula calls should pass exact bags/owners/window and both geometry
validators. Make all27 actual E28 partitions with ONE baseline112 owner7,
using the existing materializer and both full partition checkers. Independent
control: enumerate just the selected two-gap/three-gap split's original-join
root rectangle and <=6 order pairs on every call; confirm prescribed
chains occur and direct index intersections agree with physical folded
geometry. No whole-cycle solver or general bad-offset classification.

Three generic geometry-only calls:
M34,(1,1,8,8,8),p27/q25 must use H0,z3, testing a non-unit chosen offset;
M26,(1,1,5,6,8),p23/q19 tests W3;
M26,(1,1,5,6,9),p23/q21 tests W2.
Counterfactual: on(1,1,5,7,9),M28,p21/q25,naive z+1 with units first
has A=(0,5,12),B=(1,2,3,12), the correct bag but shared12; reject it.
Unexpected reflection check: SAME profile,p=q23 uses croot1 with alpha2;
its intermediate joins25/21 are geometrically valid but the WRONG original
bag. Omitting reflection must fail; reflection must restore23/23.
Outside-premise control: u=v4,w5,M20,p13/q17 is refused. The small-W
negative-offset formula there shares index5 (A1,5,9;B0,5,6,7), so the lower
bound is substantive; A=(0,4,9),B=(1,2,3,7) independently certifies the
original bag, showing refusal is not nonexistence.

Cap30 formula calls/27 actual partitions,2CPU sec/64MiB. Stop any mismatch,
retain failure; no repaired family, broader census or new carrying-read
queue. Current sole priority MI214 remains nonblocking. New theorem SKETCH.


### MI227 — B100 outcome: two-unit interleaving passes the frozen family (2026-10-17 03:37 BST)

All fixed predictions pass. The selected frozen family has exactly14
profiles/27 positive-pair questions and the independent explicit key list
agrees. There are21 W>=4 calls and6 W2/3 calls. All27 seven-vertex formulas
and all27 actual E28 partitions pass exact bags/owners/window and both
independent geometry/partition validators, with ONE unchanged baseline112
owner7. Some selected questions were already admitted in B87: the predicted
(1,1,5,7,10) MI193 overlap is present. These are27 family certificates,
not27 newly removed residuals or a new all-N5 coverage count.

All three generic controls pass, including H0/z3 and the W2/W3 reverse-run
branches. Across30 formulas,10 require reflection; all original joins and
owners are correct. The fixed-split independent maps check375 original-join
root/order candidates and contain every prescribed result. No alternative
allocation or whole-cycle existence solver was used.

The naive positive-offset units-first order on(1,1,5,7,9),21/25 has the
correct original bag/window but shares index12 and both geometry validators
reject it. The23/23 instance has geometrically valid intermediate25/21
joins; omitted reflection fails the ORIGINAL bag, and reflection restores
23/23. The outside-premise u=v4,w5 example is refused; its blindly extended
negative-offset formula shares index5, while the prescribed DIFFERENT split
A=(0,4,9),B=(1,2,3,7) gives a valid original13/17 bag. No nonexistence
claim follows from a formula's scope refusal.

First concrete target: d=(1,1,5,7,7),p17/q25 gives
A=(0,5,12),B=(1,2,3,10),moves(25,-2,-2,-14,17,-14,-10),
targets(90,106,108,108,92,84,84,112). All target inventories are original,
not a reallocation that quietly changes the question.

CPU0.028234s,peak RSS20,533,248bytes, within2CPU sec/64MiB. Source
 tests/probes/instinct/path_forest_two_unit_triangle.py; prerega2cb4e2f.
Artifact cited/instinct/b100-two-unit-triangle-537fbb2bef366066.json,
29,434bytes,SHA256 537fbb2bef3660662704b9c0d06a0a1f5eae8a23b3c2c93164a2909daa9ee1f6.
Input digest and immutable output/manifest receipts verified. General
interleaving MI226 stays PROOF-SKETCH; finite partitions are COMPUTED.
No new full E28/L8 result, no repaired predictions or broadened experiment.

**Niggle sweep.** W2/3 needs H>=1; legal T>=2 proves it, rather than the
finite list. The lower bound v>=5 is used at w-1-u=v-W-1>=1; the refused
u=v4 example shows why simply dropping it is invalid. The chosen odd root
is always alpha or alpha-1 and positive. Reflections and original ownership
are tested rather than inherited unexercised here. The isolatable rich-four-
gap COROLLARY is conditional on MI204, not part of the direct proof. If
K<=h in that corollary, keep all four endpoint bad offsets{-S,0,w-S,w},
S=u+v+2; w>=5,S>=12 ensure they cannot contain three consecutive integers.
If H0 or J0, K>h automatically and the usual thin selector applies. Thus
the corollary need not silently assume K>h. Two-bin necessity for the
nonisolatable class follows by placing three large objects in two bins,
not by the chosen formula's success. The finite family includes overlap;
its size does not count new theorem coverage.

**Gut / reasoned verdict and next cheap question.** Warm mathematical pull,
with delight at the strict interleaving and a mild push against expanding
the administrative record. The reason to continue is geometric: adjacent
small steps can be treated as a movable three-vertex block. I would choose
that question fresh, independently of sunk effort. Next ask whether the
positive-offset proof survives replacing the unit pair by arbitrary short
a,b: its triangle margin would become u+v-w-(a+b), while the narrow-margin
resonances would need an actual new argument. This is a next question,
not an opened experiment, a proved generalization or a profile-patching
quota. MI214 remains the sole requested carrying read, nonblocking;
READ-LEDGER only. Research13min active; older held lanes remain held.


### MI228 — B101: arbitrary short pairs and the forced root rectangle (2026-10-17 03:47 BST)

**Pull/question.** The unit-pair result suggests a genuine small-gap block,
not a permanent two-unit restriction. What happens when its two gaps differ,
or when roots force its endpoint across the other run? Record searched:
small.gap.block|triangle.*margin|two.short.gap|arbitrary.*small.*pair,
then canonical.*capacity|equal.*short.*gap|two.*short.*gaps ->MI227 and
unrelated record hits, no earlier theorem. Prior-art anchor remains MI054's
Tan-Teh section4 audit; no new primary theorem or novelty claim is imported.
The pull is to the root/endpoint interaction; the mere parameter replacement
in the wide-margin case is not itself the contribution.

**Direct candidate, PROOF-SKETCH.** Let positive sorted gaps be
(a,b,u,v,w),a<=b, u<=v<=w, C=a+b, u>=C+3. Write
L=u+v,S=w+C,H=h-L,J=h-S,D=L-S=J-H,T=H+J, M=2n,h=n-1.
Assume THIS capacity split fits (H,J>=0), largest isolation is impossible
(C+L>h, equivalently H<C), and legal odd positive joins p+q=2K,
K=L+S,max(p,q)<=2h-1,not both2h-1. Then T>=2 and a seven-vertex cycle
exists by the following finite selector, independent of MI204/214.
Set alpha=(2h+1-max(p,q))/2,1<=alpha<=ceil(T/2)<T.
A always has gaps(u,v),B permutes(a,b,w). Reflect/reverse both chains
only when chosen root sum croot=alpha-1; otherwise croot=alpha.

1. D>=2: let croot be largest odd<=alpha, x=min(H,(croot-1)/2),
   z=croot-2x,y=x+z. Then1<=z<=D-1. Use B gaps(a,b,w).
   The MI226 wide-margin proof, with2 replaced by C, gives
   x<y<y+a<y+C<x+u<y+S<x+L. Roots fit J=H+D.
2. D=1: legal T>=2 forces H>=1. For largest odd croot<=alpha,
   x=(croot+1)/2,y=(croot-1)/2,z=-1. Use B gaps(w,a,b).
   Roots fit since alpha<=H+1. Now w-1-u=v-C-2>=1 and
   Bmax=x+L-2. Thus y<x<x+u<y+w<y+w+a<y+S<x+L.
3. D<=0 and alpha<=2J: for largest odd croot<=alpha,
   x=(croot-1)/2,y=(croot+1)/2,z=1. Both roots fit because
   alpha<=H and ceil(alpha/2)<=J. Use B gaps(a,b,w).
   Its first three points lie strictly between A's minimum and middle
   (C+1<u), and Bmax=x+L-D+1>x+L. All seven are distinct.
4. D<=0 and alpha>2J: saturate B's root y=J and set
   croot=alpha,x=alpha-J,z=2J-alpha<0,E=T-alpha.
   Then0<E<C: E>0 from alpha<T, while alpha>2J gives E<H-J<=H<C.
   The first B point after w lies above A's middle by v-C+E>0;
   Bmax lies E above Amax. Amax therefore lies in the short block,
   distance r=C-E after B's w-prefix. If r!=a, use B gaps(w,a,b).
   If r=a but a!=b, use(w,b,a). Only equal a=b=s,r=s remains.
   In that case E=s. If -z>=2, lower croot by1 while keeping y=J,
   so x decreases1,z increases1,E becomes s+1,r becomes s-1.
   The same big-first order now works. Here s>=2 (H<2s and E=s
   rule out s1), so0<s-1<2s; min/min and max/max do not collide.
   If -z=1 instead, keep croot=alpha and put the small pair FIRST:
   relative to A-minimum, B is(-1,s-1,2s-1,S-1).
   H=s+J+1<2s forces s>=2; its two middle points lie in(0,u),
   and Bmax lies s above Amax. Again all seven points are distinct.

In branch4 x<=H and x>=1. In its root-shift subcase x>=2 beforehand,
so x-1 is valid; z+1 stays negative. This is a root-and-order selector,
not an enumeration that supplies missing universal cases. At most one
short-order swap or one root shift. Seven labels fit since h>=L>=2C+6.
Canonical capacity IS A PREMISE: ordinary capacity alone need not fit it.
No general all-N5 criterion is claimed.

**Preregistration BEFORE experiment.** Match the frozen B87 input SHA256
3b53cad88d8f0930397f545953dbad8b3a2a38adc7e37242bd90641a9ad885d0.
Select its existing M28 records with d[:2]=(1,2),u>=6,L+3>13 and
L<=13,S=w+3<=13. Predict exactly6 profiles/11 positive-pair questions:
(1,2,6,6,w),w6..9 and(1,2,6,7,w),w7..8. Independent explicit keys agree.
Predict8 D>=2 calls,2 D1 calls and1 D0 positive-offset call. Construct all11
actual E28 partitions with one baseline112 owner7, both original checkers.
These can overlap prior admissions; no all-N5 residual recount.

Five generic geometry-only calls exercise the narrow margins:
M42,(2,3,8,8,15),39/33: forced-root SHORT-ORDER SWAP (r=a);
M48,(3,3,9,9,17),43/39: equal-pair ROOT SHIFT then reflection;
M46,(3,3,9,9,16),43/37: equal-pair SMALL-FIRST reversal at z=-1;
M36,(2,2,7,7,13),31/31: forced-root equal pair without a resonance;
M42,(2,3,8,8,13),39/29: D<0 with positive offset still feasible.
All16 formulas should pass original bags/owners/window, direct index
intersections and two geometry validators. Independent full ORIGINAL-join
root maps for this fixed2+3 split, <=6 B orders and<=2 A orders, must
contain each result; no alternative allocation solver or expanded grid.

Counterfactual on the first generic call: keeping B gaps(w,a,b) gives
A=(1,9,17),B=(0,15,17,20), correct bag/window but shared17; reject it.
On the root-shift call, omitting reflection must preserve valid geometry
but give45/37 rather than the original43/39; reject the original bag.
Unexpected boundary: M40,(2,3,8,8,15),p35/q37 has ordinary capacity
(2+15)/(3+8+8)=17/19, but canonical loads16/20 do NOT fit h19.
The constructor must REFUSE it despite legal positive joins/nonisolation.
A=(1,3,18),B=(0,8,11,19) is an independent explicit alternative split
with the exact original bag. This tests the allocation premise without
turning it into a nonexistence claim or silently widening the theorem.

Cap16 formula calls/11 actual E28 partitions,2CPU sec/64MiB. Stop on any
mismatch; retain failures, no repaired domain or extra carrying-read queue.
The small-gap-block question remains warm; MI214 sole read, nonblocking.


### MI229 — B101 outcome: unequal short gaps and forced-root cases pass (2026-10-17 03:49 BST)

All predictions pass on the fixed domain. The six frozen nonunit profiles
have11 positive-pair questions, agreeing with the independent explicit keys.
Eight calls use the wide-margin selector, two the D1 negative offset and
one the D0 positive offset. All11 actual E28 partitions pass full bags,
positive ownership, windows and both independent geometry/partition checks,
with one genuine zero-move baseline112 owner7. This is a selected-family
result, not11 newly removed old residuals or an all-N5/E28 coverage claim.

All five generic controls follow the predicted branches: unequal short-order
swap, equal-pair root shift, equal-pair small-first reversal, forced-root
nonresonance and negative margin with a positive root. Across16 formulas,
249 independent original-positive root/order candidates agree with direct
index intersections and both geometry validators. Five formulas reflect;
all original owners/joins are exact.

Omitting the short-order swap shares index17 while preserving the correct
bag/window. Omitting reflection on the root-shift fixture leaves valid
geometry but45/37 instead of43/39. Both counterfactuals fail as predicted.
The M40 scope control has ordinary loads17/19 but canonical loads16/20;
its constructor refuses, while A=(1,3,18),B=(0,8,11,19) independently
certifies the original35/37 bag. This is an actual distinction between
capacity of some split and capacity of this split, not a wording guard.

First new concrete target: d=(1,2,6,6,6),17/25 gives
A=(0,6,12),B=(1,2,4,10),moves(25,-2,-4,-12,17,-12,-12),
targets(90,106,108,104,88,88,88,112).
CPU0.022620s,peak RSS21,659,648bytes, within2CPU sec/64MiB.
Source tests/probes/instinct/path_forest_short_pair_block.py;
prereg78d950d7. Artifact
cited/instinct/b101-short-pair-block-c1334f28a3b50f8f.json,16,776bytes,
SHA256 c1334f28a3b50f8fa5bab634966e47fccb34b511bfa1f236977e9effaa68d244.
Frozen input and immutable output/manifest receipts verified. No widened
input grid, alternate-allocation solver or repaired predictions.

**Status / niggle sweep.** The infinite selector MI228 remains SKETCH,
independent of MI204/214;11 actual partitions are COMPUTED. Equal-pair
root shift must keep z negative and x nonnegative: the -z>=2 condition
forces x>=2; E changes from s to s+1<C, so the endpoint remains inside
the other short interval. The z=-1 exceptional reversal needs s>=2,
proved from H<2s and tested by the3/3 fixture. Case4's inner-point margin
is v-C+E>0, not a finite observation. Canonical capacity is checked before
selecting roots and is NOT replaced by ordinary capacity. Reflection's
original-bag control is exercised. Seven-label capacity follows from
h>=u+v; no certificate is used to prove the all-size statement.
Full E28/L8 remain OPEN; MI214 is still the sole carrying-read priority.

**Steering / next cheap inference.** The capacity refusal is useful data.
With u>=C+3 and nonisolation, if ordinary capacity fits but w+C does not,
w cannot share a bin with u or v, or with BOTH short gaps. It cannot sit
alone because C+L>h. Therefore exactly one short gap must accompany w,
leaving the other with u,v. This is a forced choice between TWO allocations,
not a generic assignment search. Next check whether the corresponding
root slacks exclude all internal collisions for A gaps(a,w) and B gaps
(u,b,v), after choosing the fitting short ownership. That inference is
not claimed proved or tested here. No new experiment is opened.

Gut: warm, with delight that unequal gaps produce a real choice of order,
not just the unit proof with different letters. Reasoned verdict: selected
canonical-split construction survives its adverse controls; the allocation
boundary now supplies the next question. I would choose that question
fresh. No review-dependent halt; research13min remains active and older
held lanes stay held. READ-LEDGER only, no additional carrying-read queue.


### MI230 — B102: canonical capacity failure forces collision-free interiors (2026-10-17 03:58 BST)

**Pull/question.** MI229's refused allocation suggests the next inference:
if ordinary capacity fits but the canonical split does not, do the forced
short-gap ownership inequalities automatically exclude interior collisions?
This is a warm pull toward one changed mechanism, not another root-order
patch. Record searched: forced.*short.*ownership|forced.*allocation|
short.*canonical.*fail|canonical.*refus, then spare.*short.*gap|X<s|Y<r|
forced.*ownership.*slack ->MI229 and unrelated hits, no earlier result.
MI228/229 and the earlier forced-capacity MI220 were read for scope; the
new proof below does not depend on either. No novelty claim.

**Direct candidate, PROOF-SKETCH.** Let positive sorted gaps(a,b,u,v,w)
have C=a+b,u>=C, u<=v<=w. Let L=u+v and M=2n,h=n-1. Assume ordinary
two-bin capacity, largest nonisolation C+L>h, canonical capacity failure
w+C>h, and legal positive odd joins p+q=2K,K=C+L+w,max(p,q)<=2h-1,
not both2h-1. Then exactly one short gap must accompany w in any fitting
split: w cannot share with u or v since u>=C and w+C>h; w cannot take
BOTH short gaps; it cannot sit alone since C+L>h. Thus choose a fitting
ownership(r,s) in{(b,a),(a,b)}, giving A gaps(r,w) and B gaps(u,s,v).
The displayed order prefers the larger short gap beside w when both fit;
this is a deterministic choice among the two forced candidates.

Let X=h-w-r>=0,Y=h-L-s>=0. Canonical failure gives X<s, and
nonisolation gives Y<r. Consequently T=X+Y=2h-K>=2 and T<=C-2,
so C>=4; h>=L+s>=2C+1>=9 supplies all seven labels.
For ANY fitting roots x in[0,X],y in[0,Y],z=y-x, use

 A=(x,x+r,x+r+w), B=(y,y+u,y+u+s,y+L+s).

Bmin lies below A's short interior since r-z>=r-Y>0.
B's first interior lies above A's short interior:
 z+u-r >= u-r-X >=u-C+1>0.
B's second interior lies below Amax:
 r+w-u-s-z = v-X+(Y-z) >=v-X>0.
Thus the ONLY possible equalities between chains are min/min (z=0)
and max/max (z=d0=Y-X). This is uniform over the whole fitting root
rectangle, not just the selected positives or one successful example.

Set alpha=(2h+1-max(p,q))/2,1<=alpha<=ceil(T/2)<T. Root sums alpha or
alpha-1 give consecutive offset interval I:
[-alpha,alpha] if alpha<=min(X,Y);
[alpha-1-2X,alpha] if X<alpha<=Y;
[-alpha,2Y-alpha+1] if Y<alpha<=X.
If X,Y>=1, first3 candidates in I escape{0,d0}. If X0 take z=alpha
(strict0<alpha<Y); if Y0 take z=-alpha (strict-X<z<0).
Choose croot=alpha or alpha-1 by offset parity, x=(croot-z)/2,y=(croot+z)/2.
Reflect/reverse both chains for alpha-1, preserving the exact original bag
and positive ownership. No order search or dependent proof theorem.

**What this would close.** Together with MI228 when canonical capacity
fits, the entire nonisolatable class u>=a+b+3 would have a PROVISIONAL
ordinary-capacity criterion. MI228 remains unreviewed; the present forced
case is independent and even allows u>=C. Isolatable cases still use
MI204's rich-four-gap corollary. No full N5/E28 theorem is claimed.

**Preregistration BEFORE experiment.** Match frozen B87 SHA256
3b53cad88d8f0930397f545953dbad8b3a2a38adc7e37242bd90641a9ad885d0.
Read existing N5 records only, selecting u>=a+b,C+L>13,w+C>13 and
ordinary capacity. Predict SIX profiles, all with only23/25:
(1,3,4,6,10),(1,3,5,5,10),(2,2,4,6,10),(2,2,5,5,10),
(1,4,5,5,9),(2,3,5,5,9). Independent explicit keys agree. Derivation:
T<=C-2 forces C>=4. For C4,K<=24 leaves L=w10 and u4/v6 or5/5;
for C5 it leaves L10,w9,u=v5; C>=6 cannot fit K<=24 with u>=C.
Construct all6 actual E28 partitions with one baseline112 owner7, both
original partition validators. This includes prior admissions; no new
all-N5 residual count or reconstructed input grid.

Four generic geometry-only calls:
M30,(2,3,5,5,10),25/25: prefer r3,s2, X1/Y2 and reflected root;
M36,(2,4,6,6,14),31/33: larger-short ownership fails, fallback r2/s4;
M40,(2,3,8,8,15),35/37: the previously refused canonical split now works;
M30,(1,4,5,5,11),25/27: only smaller-short ownership fits, Y0 thin root.
All10 formulas should pass original bags/owners/window and both geometry
checks. On EVERY fixture enumerate32 labelled capacity masks independently;
all fitting masks, oriented to keep w in A, must have exactly one short
owner and no u/v there. For BOTH fitting short ownerships (when distinct),
check the ENTIRE root rectangle: fixed orders above are disjoint iff
z not in{0,Y-X}; direct index tests and both literal geometry tests agree.
Selected original-positive certificates must occur in that independent map.

Counterfactual: on the25/25 generic take x=y=1, r3/s2, giving
A=(1,4,14),B=(1,6,8,13), correct bag/window but shared minimum1; reject.
Unexpected scope checks: u<C at M20,(2,2,3,3,6),15/17 must refuse.
The blindly extended negative root A=(1,3,9),B=(0,3,5,8) shares INTERNAL3,
while A=(0,2,8),B=(1,4,6,9) independently certifies the original bag.
Nonisolation matters too: M32,(2,3,5,5,12),25/29 must refuse because
C+L=15<=h15; w alone versus(a,b,u,v) fits. A=(1,13),
B=(0,2,5,10,15) independently certifies that original bag. Refusal is
not nonexistence; the forced-ownership premise must not be dropped.

Cap10 formula calls/6 actual partitions,2CPU sec/64MiB. Stop any mismatch,
retain failures; no repaired family, wider census or extra review queue.
MI214 remains sole requested carrying read, nonblocking. Research13min.


### MI231 — B102 outcome: the forced allocation has only endpoint collisions (2026-10-17 04:01 BST)

All predictions pass on the fixed domain. Exactly six frozen profiles have
the predicted23/25 pair; all6 actual E28 partitions pass full original
bags/positive ownership/windows and both independent geometry/partition
validators, with one unchanged baseline112 owner7. All four generic
formulas pass, including larger-short preference, forced smaller-short
fallback, the previously refused M40 canonical case, and the Y0 thin root.

Across10 fixtures, all320 labelled capacity masks were checked;34 fit,
and EVERY fitting split has exactly one short owner beside w and neither
u nor v there. Across both fitting ownerships where distinct,112 complete
root/orientation entries agree exactly with the bad set{0,Y-X}; independent
direct intersections and both literal geometry tests agree. The one
reflected generic certifies the original25/25 joins and ownership.

The equal-minimum countercontrol has the correct25/25 bag but shares1
and both geometry validators reject. Dropping u>=C gives the predicted
INTERNAL collision3, while the different allowed root A=(0,2,8),
B=(1,4,6,9) certifies15/17. Dropping nonisolation permits w alone:
A=(1,13),B=(0,2,5,10,15) certifies25/29. Both scope refusals pass;
neither becomes a nonexistence claim.

First concrete E28 target: d=(1,3,4,6,10),23/25,
A=(0,3,13),B=(1,5,6,12),moves(25,-8,-2,-12,23,-20,-6),
targets(102,106,108,100,96,88,72,112).
CPU0.019583s,peak RSS20,312,064bytes, within2CPU sec/64MiB.
Source tests/probes/instinct/path_forest_forced_short_ownership.py;
prereg6a94b44e. Artifact
cited/instinct/b102-forced-short-ownership-fc8c416ea48c44f6.json,
19,554bytes,SHA256 fc8c416ea48c44f6b09084c646fb09daf244d14e328ca364ce78c57ca1c7481b.
Input and immutable output/manifest digest receipts verified. No new grid,
whole-cycle solver, repaired prediction or all-N5 coverage count.

**A coherent provisional statement, not a new experiment.** Let
0<a<=b,u<=v<=w,u>=a+b+3,C=a+b,L=u+v. At M=2n,h=n-1, suppose
C+L>h, ordinary two-bin capacity holds, and p,q are positive odd with
p+q=2(C+L+w),max(p,q)<=2h-1,not both2h-1. Then a folded-distinct
seven-vertex cycle is PROVISIONALLY supplied for this ENTIRE nonisolatable
separated family. Pigeonhole capacity gives L<=h. If w+C<=h, use MI228;
if w+C>h, use MI230. Those are disjoint, exhaustive capacity regimes.
This composition depends on TWO unreviewed sketches, not MI204 or MI214.
The general claim stays PROOF-SKETCH;6 finite partitions are COMPUTED.
Other five-gap families and full E28/L8 remain OPEN. This does not turn
previous selected-family certificate totals into a global census.

**Niggle sweep.** The proof uses strict X<s,Y<r, not weak inequalities;
both follow from the two strict capacity failures. u=C is included and
actually tested; u<C has a retained internal-collision witness. Reflection
reverses the fixed orders, so independent maps include BOTH orientations
on every root rectangle. Counting capacity masks does not replace the
pigeonhole argument. C>=4 follows from2<=T<=C-2 and supplies seven-label
capacity; no tiny-label case is silently assumed. Equal roots are rejected
on an exact ORIGINAL positive bag. Prior admissions overlap this six-profile
family; no new residual count is asserted.

**One carrying-read milestone.** The two capacity regimes now form a
complete mathematical statement worth a focused outside read. Replace
MI214 as the ACTIVE review priority with MI228+MI230, scoped to the
nonisolatable separated-family statement above. The specific questions:
(1) do MI228's equal-pair/root-shift branches exhaust the forced-root case?
(2) do MI230's inequalities really leave only the two endpoint collisions
for both fitting short ownerships? A counterexample or a missing carrying
step is more useful than another finite count. MI214 remains SKETCH and
retained, merely parked as a review request; no result is withdrawn.
Delete only its old outgoing review flag, then send ONE REVIEW-REQUEST
for this committed pointer after pushing. This replaces a priority; it
does not add a second queue or halt research for an answer.

Gut: warm, with delight that a failed allocation forces useful inequalities.
Reasoned verdict: both regimes of one separated family now have explicit
constructions, pending carrying scrutiny. Next cheap question is the
remaining canonical-case gap u in[C,C+2], where MI230 already reaches C
but MI228 currently needs C+3. Do not automatically loosen the hypothesis:
the retained u<C collision warns that internal geometry can change. No
new experiment opened. Research13min active; older held lanes stay held.


### MI232 — B103: a real canonical-split obstruction at the smaller margin (2026-10-17 04:12 BST)

**Early reflection / actual steering.** About85 minutes after MI219's
fresh-choice reflection: the initial push was against mechanically loosening
one constant and accumulating another case list. The renewed pull is a
specific obstruction to the ENTIRE fixed split, not just its old formula.
I would choose this small obstruction fresh. It changes the trajectory:
capacity can fit while every order/root for that allocation fails, so a
uniform solution must sometimes change which gaps share a run.

Record searched: u.*C+2|u.*C+1|canonical.*separation|small.*margin.*collision,
then2,2,5,5,7|four.consecutive.*bad|canonical.*every.*order ->unrelated
record hits and MI230/231, no prior result for this named fixture. Read
MI226's smaller-unit control, MI228's margin use and MI230's forced scope.
This is a bounded falsification of the weakening being considered, not a
new theorem about all five gaps or a novelty claim.

**Hand obstruction before computation, SKETCH.** Take M28,h13 and
 d=(2,2,5,5,7),C4,u=C+1. The canonical split is (5,5)/(2,2,7),
loads10/11, spare capacities3/2. In relative coordinates its chains are
A={0,5,10} and B one of

 {z,z+2,z+4,z+11}, {z,z+2,z+9,z+11}, {z,z+7,z+9,z+11}.

Across the WHOLE feasible offset range[-3,2], every order collides exactly
at z in{-2,-1,0,1}; all three orders avoid at z=-3,2. At -2, the first
two orders hit A0 and the last hits A5; at -1 all hit A10; at0 all share
a minimum; at1 the first hits A5 and the other two hit A10. Thus the
universal bad set contains FOUR consecutive integers, rather than the
two endpoint offsets used in the separated-family proof.

For positive pair17/25, the original first-positive root sums are1 or5.
The fitting roots have offsets+1,-1,-1, all bad. The entire canonical
allocation therefore fails, even with all orders. To avoid a parity-role
shortcut, also reverse which group belongs to A and B: its feasible offset
range[-2,3] has the negated bad set{-1,0,1,2}; original root sums1/5 give
only offsets-1,+1,+1, again all bad. This is a genuine fixed-allocation
obstruction, not a failure of MI228's chosen formula or a nonexistence claim.

An alternative split works: A gaps(2,7),B gaps(5,2,5). For the three
positive pairs17/25,19/23,21/21, let alpha=(27-max(p,q))/2 in{1,2,3},
croot=min(alpha,2),preA=(croot,croot+2,croot+9),preB=(0,5,7,12).
Reflect/reverse both chains in13 if croot=alpha-1. This gives three explicit
original-bag certificates, not an all-parameter extension of MI230:
its opposite-spare-capacity premises do NOT hold for this allocation.

**Preregistration BEFORE experiment.** Match frozen B87 input SHA256
3b53cad88d8f0930397f545953dbad8b3a2a38adc7e37242bd90641a9ad885d0.
The named profile should be in its OLD residual with exactly the three
positive pairs above; no new residual filtering/count or input grid.
Enumerate the COMPLETE fitting canonical root rectangles, all3 distinct
short-group orders and BOTH parity-role assignments, only for this fixture.
Predict72 total root/order cases (36 per parity assignment); within them,
original-positive candidate counts18/30/18 and valid counts0/6/6 for the
three pairs. The full universal bad offset sets must agree with the hand
sets above. Direct index intersections, physical move bags and BOTH literal
geometry validators must agree. A separate hand-expanded list of the
three normalized B shapes must match permutation generation exactly.

Make exactly3 actual E28 partitions using the explicit ALTERNATIVE split
formula, one baseline112 owner7 and both full partition validators. At
alpha3 reflection is essential: intermediate23/19 differs from21/21;
omitting it must preserve geometry but fail the original bag. For17/25,
naive canonical A=(1,6,11),B=(0,7,9,11) has the exact original bag/window
but shared11; reject it. No complete-cycle solver or other allocation search.

Unexpected lattice check: scale ALL negative halves AND h by2, then keep
legal odd positives via51/33 (not the even literal doubles50/34).
At M54,d=(4,4,10,10,14),canonical A=(0,10,20),B=(1,5,9,23) should WORK.
The same load/capacity ratios therefore do not preserve this obstruction;
the odd root lattice and small absolute gaps matter. This is one named
geometry check, not a scaling theorem or a larger-domain scan.

Cap72 canonical cases,3 alternative formulas/3 E28 partitions,1 scaled
geometry control,2CPU sec/64MiB. Stop any mismatch, retain it; no repaired
counterexample, relaxed claim or new carrying-read queue. Current review
priority remains MI228+MI230 at0a0a0d44, nonblocking. This addendum will
show why its margin hypothesis must not be casually dropped.


### MI233 — B103 outcome: a fitting allocation can fail every order (2026-10-17 04:18 BST)

The named profile(2,2,5,5,7) is in the frozen OLD B87 residual with exactly
17/25,19/23,21/21, as predicted. The72 canonical root/order cases exhaust
BOTH parity-role assignments and agree with the hand-expanded three
shapes. Original-positive candidate counts are18/30/18; valid counts are
0/6/6. Thus17/25 has NO canonical-split solution despite loads10/11
fitting13/13. Direct intersections, full physical bags and both literal
geometry validators agree. This is a COMPUTED refutation of the fixed-
canonical-split weakening being considered, not of MI228's stated scope.

The universal bad offset sets are exactly{-2,-1,0,1} and its negation
{-1,0,1,2} for the two role assignments. The extra INTERNAL collisions
really join the two endpoint traps into a four-consecutive block. The
17/25 root budget never reaches its safe offsets. The other two positive
pairs do reach a safe offset and each has six canonical witnesses.
No canonical failure is generalized to nonexistence of a cycle.

All THREE explicit ALTERNATIVE-allocation E28 partitions pass original
bags/owners/windows and both independent partition validators, with one
baseline112 owner7. The first uses A=(1,3,10),B=(0,5,7,12), and targets
(90,106,104,104,92,92,84,112). The19/23 and21/21 targets are respectively
(94,102,104,104,92,92,84,112) and(98,98,104,104,92,92,84,112).
For21/21, omitted reflection has valid geometry but intermediate23/19;
it fails the original bag, as predicted. The naive canonical witness
shares11 and both geometry validators reject it despite its correct bag.

The scaled lattice control passes: M54,d=(4,4,10,10,14),51/33 has
canonical A=(0,10,20),B=(1,5,9,23). Negative halves AND h doubled,
so both load/capacity ratios are unchanged, but the positive pair uses
odd51/33 rather than even literal doubles50/34. This is a named lattice
control, not a homogeneity theorem or a claim that positive data were
literally scaled. Small absolute offsets matter as well as capacity.

CPU0.017423s,peak RSS19,972,096bytes, within2CPU sec/64MiB.
Source tests/probes/instinct/path_forest_canonical_obstruction.py;
prereg90e1fa99. Artifact
cited/instinct/b103-canonical-obstruction-c2d4738c551cc242.json,
13,469bytes,SHA256 c2d4738c551cc2426a0d1d73c378dcaa5d4d30d37a3f4864d9ec13c9d8be81ed.
Frozen input and immutable output/manifest digest receipts verified.
No wider scan, whole-cycle solver, repaired claim or all-N5 coverage count.
Finite exhaustion/partitions are COMPUTED; no new infinite theorem.

**Niggle sweep.** Both parity assignments were actually enumerated; their
relation was not assumed to be a harmless symmetry. Both original positive
owners are included through the complete root sums, rather than checking
only the representative alpha sum. Duplicate2 and5 gaps give three distinct
short-group orders and one long-group order, not36 artificially different
labels. Unused/root orders outside the three positive pairs do not count
as witnesses for those questions. The alternative split violates MI230's
opposite-slack premises, so its three named formulas are NOT filed as an
application of MI230. Scaling keeps legality by changing the positive
values as explicitly stated. Existing MI228+MI230 review remains scoped
to u>=a+b+3; this example has u=C+1 and does not contradict that claim.

**Trajectory / next missing inference.** Capacity fitting does not select a
successful allocation even at N5. The next useful question is whether a
canonical all-order trap like this FORCES one of the largest-plus-short
allocations to fit and admit the given positives. It is a different
selection question, not permission to attach more root branches to the
old split. No such theorem or experiment is opened here. A friend's
perspective on an allocation-switching invariant would be useful after
the current carrying read; this is a READ-LEDGER addendum, not a second
review request.

Gut verdict: push against automatic constant loosening; renewed pull toward
allocation switching after a real failure. Reasoned verdict: one precise
obstruction explains why the old representation stalls, and an explicit
valid partition shows where another representation succeeds. The early
reflection MI232 changed course on evidence; no forced rotation or halt.
Current sole carrying priority remains MI228+MI230 at0a0a0d44, nonblocking.
Research13min continues; full E28/L8 and the older held lanes retain status.


### MI234 — B104: resonances force eight finite allocation switches (2026-10-17 04:29 BST)

**Actual pull.** The obstruction has become simpler after widening the
representation: most offsets cannot collide in every order at all. The
warmth is attached to this new classification, not to another successful
certificate count. Question: for five halves(s,s,t,t,w),t>=2s,w>=t,
does an all-order canonical trap force an explicit alternative split?
This would settle the allocation question for a whole paired family,
including the small-margin obstruction MI233; it does not settle all N5.

Record searched: paired.*resonan|s,s,t,t|canonical.*bad.*offset ->0 hits
including ledgers. Read MI228/230/232/233 and their probes. This is a
direct extension of those coordinates, not a literature novelty claim.

**Hand argument, PROOF-SKETCH before any experiment.** Let M=2n,h=n-1,
h>=6,s>=1,t>=2s,w>=t,K=2s+2t+w. Assume2s+2t>h (the largest cannot
be alone), ordinary two-bin load capacity, and positive odd p,q with
p+q=2K,max(p,q)<=2h-1,not both2h-1. Claim: disjoint index chains with
these five gaps and exactly these two positive joins always exist.

First suppose the canonical loads L=2t,S=2s+w both fit h. Put
H=h-L,J=h-S,T=H+J,d=L-S=J-H. Legal joins give T>=2 and
alpha=(2h+1-max(p,q))/2,1<=alpha<=ceil(T/2)<T. The feasible offsets
z=y-x on root sums c=alpha or alpha-1 form the consecutive interval I:

 alpha<=min(H,J): [-alpha,alpha];
 H<alpha<=J: [alpha-1-2H,alpha];
 J<alpha<=H: [-alpha,2J-alpha+1].

For a chosen offset, select c by parity, x=(c-z)/2,y=(c+z)/2.
Relative A={0,t,2t}; B has one of the three orders

 {z,z+s,z+2s,z+S}, {z,z+s,z+s+w,z+S}, {z,z+w,z+w+s,z+S}.

Call an offset universally bad if ALL three B orders meet A. Across the
WHOLE feasible offset interval[-H,J], the exact universally bad set is

 U={0,d}, with {-s,d+s} added iff w in{t,t+s} AND H>=s.

Here is the carrying classification. The B-endpoint/A-middle offsets
t and t-S lie outside[-H,J]: J=h-2s-w<2t-w<=t and h<t+S.
The outermost endpoint offsets -S and2t are outside because K>h.
The remaining endpoint collisions are exactly0 and d. Away from them,
the internal B-prefix pairs are {s,2s},{s,w+s},{w,w+s}.
Every hitting set for all three contains one of
{s,w},{s,w+s},{2s,w+s}. For two such prefix levels to hit A they must
be separated by t or2t. Their separations are w-s,w,w-s; canonical
capacity and nonisolation imply w<2t. Therefore the only possible
resonances are w=t or w=t+s. For w=t the extra offsets are -s,t-s.
For w=t+s they are -2s,-s,t-2s,t-s. The inequalities H<2s and
J< t-s remove -2s and t-s in the second case. The remaining extras
are -s,d+s, both feasible exactly when H>=s. This proves the formula
by the three explicit hitting pairs, without MI204 or MI228.

If H,J>=1, I has at least three consecutive integers. In the first
resonance w=t, U={-s,0,t-2s,t-s} can contain three consecutive integers
only for(s,t)=(1,2)or(1,3). The(1,2)case contradicts h>=6 and h<6.
In the second resonance w=t+s, put d=t-3s>=-s. For d>=0 the only
possibilities are(s,d)=(1,0),(1,1). For -s<d<0, writing e=d+s,
the consecutive sorted gaps in U are e,s-e,e; three consecutive
integers require(s,e)=(2,1). The boundary d=-s has only endpoints.
Thus only(s,t,w)=(1,3,3),(1,3,4),(1,4,5),(2,5,7) need finite
root-budget analysis. If U has no triple, one of the first three
offsets in I escapes; in general try at most FIVE, since |U|<=4.
The three local B orders then supply a disjoint pair.

Thin intervals are harmless: if H=0 the extras are absent and z=alpha
is strictly between0 and J=d. If J=0, w=t is incompatible with
T>=2 and t>=2s. For w=t+s, H=3s-t<=s; extras occur only at H=s,
when they duplicate0 and d=-s. Thus z=-alpha strictly between-H and0
escapes. Nonresonant thin cases have endpoints only.

Combining canonical capacity, h>=6, h<2s+2t and legal joins leaves
exactly EIGHT (s,t,w,h,p,q),p<=q, for which I is wholly bad:

 (1,3,3,7,9,13), (1,3,3,7,11,11), (1,3,4,7,11,13),
 (1,4,5,9,13,17), (1,4,5,9,15,15),
 (2,5,7,12,19,23), (2,5,7,12,21,21), (2,5,7,13,17,25).

The first three profiles force h=7,7,9 respectively. The last has
h=12 or13: at12 alpha1/2 both fail; at13 only alpha1 fails, since
alpha2/3 reach offset2. For EACH of the eight, use instead

 c=min(alpha,s), preA=(c,c+s,c+s+w), preB=(0,t,t+s,2t+s).

These listed coordinates are visibly disjoint in[0,h], and c equals
alpha or alpha-1. In ALL constructions, if c=alpha-1 reflect AND
reverse BOTH chains i->h-i, and flip the first positive owner.
Before reflection the joins are max(p,q)+2,min(p,q)-2; after it
they are precisely the original pair with the original ownership.
No intermediate positive bag is accepted as an original witness.

Swapping A and B preserves disjointness, their minimum-sum and
maximum-sum, hence both positive VALUES and the negative gap BAG.
So complete canonical impossibility is equivalent for both parity
roles; exact traversal words are not being identified.

If canonical capacity fails, ordinary capacity forces exactly one s
beside w, with t,t,s on the other run. Then A gaps(s,w),B gaps(t,s,t)
fit, X=h-s-w<s and Y=h-2t-s<s. Since t>=2s, their fixed internal
levels strictly interleave as in MI230, with bad offsets only0,Y-X.
The same interval argument avoids these two offsets (thin cases use
strict interior +/-alpha). This final branch uses MI230's UNREVIEWED
carrying inequalities; the new canonical classification is direct.
Necessity of the stated load/label/positive conditions is elementary;
only sufficiency is new here, and remains SKETCH pending outside read.

**Preregistration BEFORE experiment.** Diagnostic grid, not E28 census:
s=1..3,t=2s..2s+3,w=t..2t+s-1,h=max(6,2t)..2s+2t-1. Filter by
ordinary capacity and all legal p<=q as above. Predict all constructions
succeed by canonical selection, the eight explicit repairs, or MI230.
Check ordinary capacity by all32 labelled masks AND subset-bitset.
For EVERY canonical-fitting profile independently intersect all three
literal difference sets A-Bshape on[-H,J] and compare to U. Check all
feasible offsets/three orders by direct intersection and BOTH literal
physical geometry validators; hand shapes must equal permutation shapes.
Predict exactly the eight canonical failures listed above. For those,
exhaust original-positive root rectangles/three orders/BOTH parity roles
and require zero witnesses; validate their explicit repair instead.
For every other admitted positive question validate the selected formula's
full original bag/owner/window and both geometry checks. No global
cycle solver, allocation search or new actual E28 partition run.

The forced branch must occur, including named M24,d=(2,2,4,4,8),19/21.
Counterfactual endpoint-only U misclassifies z=-1 at(1,3,3,h7),alpha1;
the complete offset map must reject it. Unexpected label control
M12,d=(1,1,2,2,2),7/9 has capacity/legal joins but only six labels for
seven vertices: the h>=6 admission must REFUSE. It is not a ninth trap.
Named scaled control M54,d=(4,4,10,10,14),33/51 should construct despite
matching the small obstruction's capacity ratios; no scaled grid.
Reuse the immutable B103 receipt SHA256
c2d4738c551cc2426a0d1d73c378dcaa5d4d30d37a3f4864d9ec13c9d8be81ed
for the existing M28 repair; no new partition count.

Caps3000 formula calls/40000 offset-order or exception-root cases,
2CPU sec/64MiB. Stop ANY disagreement, retain failure, do not repair
the prediction or widen the grid. Sole carrying priority MI228+MI230
remains nonblocking; this gets a READ-LEDGER addendum, not another queue.
Portal initially hit sandbox DNS failure before authentication; the
authorized network poll succeeded afterward. No failed login retried.


### MI235 — B104 outcome: the allocation-switch classification survives every prescribed check (2026-10-17 04:31 BST)

The fixed grid has402 profiles and12,864 independently counted labelled
capacity-mask checks, agreeing with subset-bitset capacity. It produces
538 legal positive questions:490 canonical constructions, EXACTLY8 finite
allocation repairs and40 forced-capacity constructions. The named scaled
control makes539 formula calls total. Every call passes full ORIGINAL
positive/negative bags, ownership, window and both physical geometry
validators. There are112 reflected grid constructions; reflection is part
of the original-bag construction, not an optional symmetry shortcut.

For205 canonical-fitting profiles, the complete feasible offset maps agree
EXACTLY with U, independently by intersections of three difference sets,
literal index intersections and both physical geometry tests. These maps
also include capacity profiles without legal positive pairs; none is
silently counted as a positive-question construction. Hand-expanded shapes
match the three distinct permutation shapes. The eight predicted
canonical failures are exactly the eight found, with no extra exception.
Complete original-positive maps under BOTH parity assignments give
126 candidates total and ZERO witnesses. Their alternative splits all
certify the original pairs; there are312 complete exception-root/order
cases within3726 offset-order/exception cases overall.

The M24(2,2,4,4,8),19/21 forced branch is exercised. The deliberately
false endpoint-only rule accepts offset-1 in(1,3,3,h7), whereas the full
map rejects it in every order. The seven-vertices/six-labels control
M12(1,1,2,2,2),7/9 is refused despite ordinary capacity and legal joins.
The scaled M54 control constructs A=(1,11,21),B=(0,4,8,22); its offset-1
is safe, consistently with MI233's independent scaled witness. The
M28(2,2,5,5,7),17/25 repair agrees exactly with the frozen B103 A,B and
move word after matching the input digest. No new actual E28 partition
was run or claimed; that existing partition receipt is reused.

CPU0.127142s,peak RSS18,538,496bytes, within2CPU sec/64MiB.
Source tests/probes/instinct/path_forest_paired_resonances.py;
prereg962b5fe0. Immutable artifact
cited/instinct/b104-paired-resonances-256cf03e435ab91b.json,
191,434bytes,SHA256 256cf03e435ab91b34208fbe558b5eb2d61fcd3de331e5ff0679edeb44c7b583.
Output digest and manifest receipts verified. MI234's displayed time is
corrected from04:33 to04:29 to match the preregistration commit; no
prediction changed. No widened grid, new cycle
solver, repaired prediction, new partition count or full N5 census.

**Niggle sweep / carrying details.** The three hitting pairs remain valid
when w=2s because then the prefix-pair graph is a triangle; the same
three pairs are precisely its minimal hitting sets. The strict w<2t
uses canonical capacity PLUS nonisolation, not simply w>=t. The forbidden
offset formula is restricted to[-H,J]; outside that range other
differences can occur. Trying only three or four offsets is insufficient
in the four-consecutive resonance: alpha2 at(2,5,7,h13) needs its fifth
available offset2. The source tries at most five, with no exception
search. The h>=6 label hypothesis excludes the otherwise legal small
corner that would destroy the theorem; it is not a cosmetic guard.

For clarity, the MI230 branch's internal safety can also be read directly.
With A=(x,x+s,x+s+w),B=(y,y+t,y+t+s,y+2t+s),0<=x<=X<s and
0<=y<=Y<s, one has

 y < x+s < y+t < y+t+s < x+s+w.

The second inequality follows from x+s<=X+s<2s<=t; the last from
Y+t-w=X-t<0. The A-minimum cannot hit B's internal points since
x<=X<s<=t, and B's maximum cannot hit A's short internal point.
Thus only minimum/minimum and maximum/maximum collisions remain. Capacity
forces the split because w+t>=w+2s>h and w alone leaves load2s+2t>h.
The paired-family sufficiency is therefore supported by direct carrying
inequalities as well as the MI230 reference; it does not rely on MI228,
MI204 or an assumption that canonical capacity already supplies geometry.

The eight small repairs are finite and explicitly stated; the infinite
claim is the algebraic classification, NOT an extrapolation from402 grid
profiles. Swapping parity roles preserves bags/end-sums, not move order;
both roles are nevertheless independently exhausted on the eight failures.
All label/window/bag validations use the ORIGINAL positives. No generic
two-bin criterion for arbitrary five gaps follows from this special family.

**What changed.** The previous isolated obstruction is now explained by a
complete resonance mechanism for(s,s,t,t,w),t>=2s: almost all fitting
canonical allocations succeed; the only wholly blocked positive questions
force one of eight explicit allocation switches. This sufficiency stays
PROOF-SKETCH; the bounded maps/constructions are COMPUTED. Full E28/L8
remains OPEN. No new proof entry or second carrying-review queue is opened.
Send this committed classification to Cloud as a READ-LEDGER addendum to
GC1430; the sole current carrying priority remains MI228+MI230.

Gut: delight at an obstruction turning into a short classification; warm
pull toward understanding which parts survive unequal short/middle pairs.
Reasoned verdict: one infinite structured family has a hand sufficiency
argument with exact diagnostic agreement; independent proof scrutiny is
still outstanding. Next cheap question is to derive, by hand, the minimal
prefix hitting sets when the middle pair is unequal, rather than add a
larger scan or mechanically replace t>=2s by a weaker bound. No next
experiment is opened. Research13min continues without waiting for review.


### MI236 — B105: unequal middle gaps break almost all common traps (2026-10-17 04:36 BST)

**Pull before rationalization.** Surprise: allowing the other middle order
seems to destroy the resonance instead of making it harder. The warm
question is no longer a larger exception catalogue: what must survive
BOTH middle orders? This would extend MI234's paired family to every
(s,s,u,v,w),2s<=u<=v<=w, under the same nonisolation/capacity conditions.
The u=v boundary is already MI234; this block treats u<v only.

Record searched: unequal.*middle|canonical.*hitting|paired.*resonan ->
one GC1431 operational pointer;1,1,2,3,3|1,1,3,4,4|v=w=u ->0 hits,
including ledgers. Read MI234/235 and MI230's carrying inequalities.
These are direct coordinate arguments, no literature novelty claim.

**Hand argument BEFORE computation, PROOF-SKETCH.** Let h>=6,s>=1,
2s<=u<v<=w,K=2s+u+v+w,2s+u+v>h. Assume ordinary two-bin capacity
and legal odd p,q: p+q=2K,max<=2h-1,not both2h-1. When canonical
loads L=u+v,S=2s+w fit h, put H=h-L,J=h-S,d=L-S,T=H+J.
Use the same alpha/root-sum interval I as MI234.

The relative A-chain may be{0,u,L} OR{0,v,L}. B has the same three
relative shapes as MI234, with w in the third-gap role. Endpoint/middle
collisions lie outside[-H,J] for BOTH A orders: J<u<=v and
h<u+S<=v+S. The surviving endpoint obstructions are E={0,d}.
For either A-middle g, let k=L-g be the other middle gap. The same
three minimal prefix hitting pairs give ALL possible extra bad offsets:

 if w=g: {-s}; if w=k: {g-s};
 if w-s=g: {-s,-2s}; if w-s=k: {g-s,g-2s}.

Take the union of applicable clauses for each order, then intersect the
two orders' bad sets and restrict to[-H,J]. The separation L cannot
occur because canonical capacity and nonisolation force w<L. Since
u<v<=w, the only possible resonances are w=v,w=u+s,w=v+s.
If just w=v, the extra sets{u-s} and{-s} do not meet. If just w=u+s,
the first set is negative and the second{v-s,v-2s} is nonnegative.
If w=v+s, the first{u-s,u-2s} is nonnegative and the second negative.
Two resonance equations coincide ONLY at w=v=u+s. Then the extras
are{-s,u-s}, both feasible exactly when H>=s. Therefore the exact
all-SIX-order universal bad set on feasible offsets is

 U={0,d}, adding {-s,d+s} iff v=w=u+s AND H>=s.

This intersection of two order-obstructions is the new carrying step;
choosing an arbitrary first A-order would lose it. For H,J>=1, I has
three consecutive offsets. In the resonance d=u-2s>=0, U can contain
a triple only at(s,u)=(1,2),(1,3). Outside those corners one of the
first three offsets escapes; universally at most FIVE offset choices
suffice since |U|<=4. At a free offset choose among the two A orders
and three B orders, a fixed six local choices, not a cycle solver.
If H=0 extras are absent and z=alpha works. If J=0 the resonance
would have H=2s-u<=0, contrary to T>=2; hence z=-alpha works.

Canonical capacity, h>=6, nonisolation and legal joins leave exactly
THREE all-order failures, in format(s,u,v,w,h,p,q),p<=q:

 (1,2,3,3,6,9,11), (1,3,4,4,8,11,15), (1,3,4,4,8,13,13).

For the first use preA=(0,3,6),preB=(1,2,4,5). For the second/third,
use preA=(0,4,8),preB=(1,2,3,6). Their root sum is1; alpha is1,1,2
respectively. Reflect/reverse BOTH chains and flip the positive owner
when alpha=2. These are top-two-gap allocations, unlike MI234's repair.
In particular blindly reusing A gaps(s,w),B gaps(u,s,v) in the first
case gives preA=(1,2,5),preB=(0,2,3,6), a real collision at2.
This does not refute MI230: its opposite-spare-capacity hypotheses fail.

If canonical capacity fails, ordinary capacity/nonisolation force
A gaps(s,w),B gaps(u,s,v). MI230 applies because u>=2s. Thus the
unequal-middle family has a sufficiency SKETCH, which together with
MI234 covers all2s<=u<=v<=w with two equal short gaps. It is not a
theorem for unequal short gaps or all five-gap bags. Its hand proof
uses no MI228 or MI204; MI230/234 remain unreviewed dependencies.

**Preregistration BEFORE experiment.** Fixed diagnostic grid:
s=1..3,u=2s..2s+2,v=u+1..u+3,w=v..u+v+s-1,
h=max(6,u+v)..2s+u+v-1. Check ordinary capacity by all32 labelled
masks against subset-bitset; enumerate ALL legal positive pairs p<=q.
Predict every question constructs by canonical order choice, the three
listed repairs, or MI230's forced branch. For EVERY canonical-fitting
profile, compare the formula U with the literal intersection of all
SIX difference sets, then check every feasible offset/six local orders
by index intersection and BOTH literal physical geometry validators.
The two hand-expanded A shapes/three B shapes must match permutations.

Predict exactly the THREE canonical failures above. On each, exhaust
complete fitting root rectangles, both middle orders, three B orders,
and BOTH parity assignments for the ORIGINAL positive bag: zero valid
candidates. Validate every selected construction's original positive
owners, full gap bag/window and both geometry tests. No generic cycle
solver, allocation search, new E28 partitions or global residual count.
The forced branch must include M26,(2,2,4,5,9),21/23. Include one named
outside-grid s=4,u=8,v=12,w=12,h=26,p=33,q=47 canonical geometry,
testing the larger exact resonance with safe offsets rather than scaling
literal odd positives. No extended grid or new partition run.

Counterfactual: changing the OR over two A orders into a fixed first
order can falsely reject an offset. At s1,u2,v4,w4,h7, z=-1, A order
(4,2) is blocked but(2,4) has a safe B order; verify the complete map
exhibits this asymmetry. Unexpected control: at the first exception,
the OLD largest-plus-short repair shares2 despite the correct9/11 bag;
both physical geometry tests must reject it, while the new repair works.
Also refuse the same too-few-labels h5 fixture as MI234, not silently
extend the theorem below h6. No review queue is added; current read
MI228+MI230 remains nonblocking.

Caps4000 formula calls/60000 offset-order or exception-root cases,
3CPU sec/64MiB. Stop on ANY disagreement, retain failures, no repaired
prediction or expanded grid. Fresh-choice reflection remains MI232;
the new question has changed through evidence rather than rotation.


### MI237 — B105 outcome: the second middle order removes the resonance (2026-10-17 04:38 BST)

All prescribed checks pass. The fixed grid contains861 profiles and
27,552 independent labelled capacity-mask checks, agreeing with subset
capacity. There are1035 legal positive questions:942 canonical
constructions,90 forced-capacity constructions and EXACTLY3 finite
top-two-gap repairs. The named larger control makes1036 formulas total.
Every selected formula passes its ORIGINAL positive owners, entire move
bag/window and BOTH literal geometry validators.155 grid constructions
use reflection;31 canonical constructions select the other middle order.
This last count is a diagnostic of a real choice, not an extra solution
count or a statement that all31 fail every root with the first order.

All413 complete canonical-profile offset maps agree with the predicted
U, independently by intersecting SIX difference sets, direct index
collisions and both physical geometry tests. Profiles without legal
positive pairs enter only this offset comparison, not construction totals.
The two A shapes and three B shapes match distinct permutation generation.
The three predicted original-positive canonical failures are exactly those
found. Their complete maps under BOTH parity roles have96 original-bag
candidates and ZERO valid witnesses, among192 exception-root/order cases.
Combined offset-order/exception count13,362, within60,000. All three
explicit alternative repairs certify their original pairs.

The order counterfactual behaves as predicted: at(1,2,4,4,h7),offset-1,
A's(4,2) order is blocked for every B order, whereas(2,4) escapes.
The old largest-plus-short repair at the first exception has the exact
9/11 bag but shares index2; BOTH geometry validators reject it. The
top-two-gap repair succeeds instead. The named forced-capacity case
M26,(2,2,4,5,9),21/23 is present and passes. The larger exact resonance
(s,u,v,w,h)=(4,8,12,12,26),33/47 constructs A=(3,11,23),B=(0,4,8,20).
This tests one larger named resonance, not an extended grid. The prior
h5 fixture is refused as specified; it is also outside this unequal-middle
class, so it is not an independent isolation of the label hypothesis.
No new E28 partition was run or counted.

CPU0.341547s,peak RSS19,570,688bytes, within3CPU sec/64MiB.
Source tests/probes/instinct/path_forest_unequal_middle_resonances.py;
prereg50b7f1b6. Immutable artifact
cited/instinct/b105-unequal-middle-resonances-343075fb71404d75.json,
408,262bytes,SHA256 343075fb71404d75cf1bb822be7a0b627fd23587691f1ac99c1bd978e0c53912.
Output digest and manifest receipts verified. No prediction repair,
widened grid, allocation search, new partition count or full N5 census.

**Niggle sweep.** The all-order bad set is an INTERSECTION between the
two middle orders, after a union of applicable resonance clauses within
each order. Reversing that logical structure would lose the key step.
At w=v=u+s both clauses must be included in each order; treating the
resonances as mutually exclusive would incorrectly remove the real traps.
The endpoint exclusions use w>=v and nonisolation, while w<L uses
canonical capacity; they are not consequences of the size condition alone.
Thin roots are handled before relying on three consecutive offsets.
Original positive ownership is checked after BOTH-chain reflection.
The finite repairs change allocation, not only order; MI230's fixed
allocation cannot be reused without its strict slack hypotheses.

The first exception is a full-label h6 question already covered by the
PROVED MI180 theorem. Its explicit repair is a component of this new
selector, not a new independent theorem deserving another review job.
The general classification is a hand argument supported by these checks;
no finite map supplies its infinite quantifier. Combining MI234's u=v
boundary with MI236's u<v case and MI230's capacity-failure branch gives:

 For(s,s,u,v,w),s>=1,2s<=u<=v<=w,h>=6,2s+u+v>h,
 ordinary two-bin capacity and legal odd p,q are sufficient for a
 folded-distinct seven-vertex cycle with that exact original gap bag.

This combined statement remains PROOF-SKETCH; its diagnostic calculations
are COMPUTED. It is a structured-family result, not arbitrary five-gap
sufficiency, an all-N5 coverage count or a solution of E28/L8.

**Trajectory.** The most useful change was letting BOTH middle orders
express the obstruction. The extra freedom made a complicated local
picture collapse to one resonance. Gut: surprise and delight in that
simplification; the pull remains attached to a changing question.
Reasoned verdict: the equal-short-pair family now has a complete
provisional allocation selector under u>=2s, with eleven total tiny
canonical traps across its equal/unequal-middle cases. Next cheap
inference is whether unequal short gaps make the three-prefix hitting
condition similarly more restrictive. Derive the order-prefix constraints
first; no wider census or new experiment is opened. Sole carrying read
MI228+MI230 remains nonblocking; this is a READ-LEDGER addendum only.


### MI238 — B106: a six-cycle of prefix constraints and one forced partner (2026-10-17 04:51 BST)

**Pull/surprise before testing.** The unequal-short question simplifies
MORE than expected. The six prefix pairs form a six-cycle, whose two
minimum covers force an impossible small gap. A second simplification:
when canonical capacity fails, there is only ONE interior prefix level
to avoid after choosing the largest gap's forced partner. This changes
the target from weakening u>=a+b by another constant to removing that
margin entirely for unequal short gaps.

Record searched: unequal.*short.*hitting|prefix.*six.*orders|
minimal.*hitting.*pairs ->0 hits;one.*forbidden.*prefix|forced.*partner|
six.cycle.*prefix ->0 default hits. Directly located and READ MI117's
one-forbidden-level swap argument, MI230's capacity inequalities and
MI234/236's hitting-pair derivations. No literature novelty claim; no
standalone review job for the elementary vertex-cover or prefix facts.

**Hand sufficiency claim, PROOF-SKETCH BEFORE experiment.** Let sorted
positive halves0<a<b<=u<=v<=w and h>=6. Assume C+L>h where C=a+b,
L=u+v (largest nonisolatable), ordinary two-bin capacity, and legal odd
p,q: p+q=2K,K=C+L+w,max<=2h-1,not both2h-1. Claim: these hypotheses
suffice for disjoint seven-vertex index chains with the exact gap bag
(a,b,u,v,w) and original positive joins. No u>=C condition is needed.
Full E28/L8 and the equal-short case a=b are not asserted here.

**1. Canonical capacity.** Ordinary capacity implies L<=h by pigeonhole
among u,v,w. Suppose also S=C+w<=h. Set H=h-L,J=h-S,d=L-S,
T=H+J>=2 and alpha=(2h+1-max(p,q))/2. Use MI234's consecutive
offset interval I for root sums alpha/alpha-1. Fix A={0,u,L}; no second
middle order is needed. Across all feasible offsets[-H,J], B's endpoint
collisions reduce to E={0,d}: J<u, h<u+S exclude its endpoints hitting
A's middle; outermost endpoint differences are outside by K>h.

Away from E, F={-z,u-z,L-z} must hit each proper-prefix PAIR of all
six permutations of(a,b,w):

 {a,C}, {b,C}, {a,w+a}, {b,w+b}, {w,w+a}, {w,w+b}.

If w>b and w!=C these are the edges of a SIX-CYCLE on distinct vertices
C,a,w+a,w,w+b,b. A cover with at most three vertices must be one of
its two alternating covers {a,b,w} or {C,w+a,w+b}. Their sorted gaps
are(b-a,w-b) or(w-b,b-a); neither can equal(u,v) since b-a<b<=u.
Thus every offset outside E has a safe B order, for this fixed A order.

There are only two vertex-identification cases. If w=b then u=v=b;
the graph is the path a-C-b-2b. Its minimal covers are{a,b},{C,b},
{C,2b}; each requires two F vertices separated by a or b-a, both below
b, whereas F is a b-step progression. No extra bad offset exists.
If w=C, the graph is two triangles sharing C. A three-vertex cover
must contain C and one vertex from each opposite edge. Of the four
covers, two have span b< L, one has gaps(a,a), and the only remaining
one {a,C,C+b} has gaps(b,b). Thus an extra offset exists EXACTLY
when u=v=b,w=C; it is z=-a. This proves the full feasible bad set

 U={0,d}, except u=v=b,w=a+b gives U={-2a,-a,0}.

For the exceptional profile H=J+2a>=2a. If a>=2, three consecutive
offsets cannot all be bad; when J=0 the two adjacent offsets in I
cannot both lie in this a-spaced set. If a=1 and J>=1, I always
contains the safe positive offset1. The ONLY all-order failure is the
infinite family

 a=1, b>=2, u=v=b,w=b+1,h=2b+2,
 p=4b+1,q=4b+3 (or swapped).

Its explicit repair changes allocation:
 preA=(0,b,2b+1),preB=(1,b+1,b+2,2b+2).
All seven indices are distinct for b>=2. Its gaps are(b,b+1)/(b,1,b),
root sum1 gives exactly the required original positives. Elsewhere
choose the first free offset among at most FOUR consecutive candidates
in I, then one of six B orders. Nonresonant thin roots use strict
interior +/-alpha; the a-spaced thin case is handled as above.

**2. Canonical capacity failure.** Now w+C>h. In EVERY fitting split,
w must have EXACTLY ONE partner r from{a,b,u,v}: alone leaves load
C+L>h, and any two partners have sum>=C. Conversely examine these
four forced partner candidates only, with remaining three gaps D.
Prefer a fitting candidate with D nonconstant. Let R=sum(D),
X=h-w-r>=0,Y=h-R>=0. Minimal two-partner load and nonisolation give
X<min(D),Y<r. For any roots x in[0,X],y in[0,Y], A=(x,x+r,x+r+w),
and any ordered B-prefix chain has the following properties:

 A-minimum is below every proper B prefix since X<min(D);
 B-minimum is below A's interior since Y<r;
 B-maximum is above A's interior since R+r>h and w>=r;
 every proper B prefix is below A-maximum since X<its last gap.

Thus only min/min, max/max and the single forbidden interior prefix
F=r-(y-x) can collide. For NONCONSTANT D, MI117's elementary swap
avoids any one proper prefix level. A self-contained three-item version:
for F in(0,R), choose distinct first/last items with first!=F and
last!=R-F. If no such pair exists and neither set is empty, both
nonmatching index sets are the same singleton. The other two items
then equal BOTH F and R-F, forcing the third item0, impossible.
An empty set means D constant. For constant(t,t,t), only F=t,2t
are unavoidable. No novel supporting theorem is claimed.

If every fitting choice has constant D, sorted a<b forces r=a and
b=u=v=t. The alternative partner t would leave load a+2t<=3t<=h;
its failure therefore forces w+t>h. Hence X<t-a,Y<a, so
0<a-Y<=F<=a+X<t: the constant chain avoids F automatically.
This handles the constant case rather than silently applying the
nonconstant lemma. Choose a root offset avoiding{0,Y-X} by the usual
three-consecutive/strict-interior argument, then the safe prefix order.
Reflect/reverse BOTH chains for root sum alpha-1 and flip the positive
owner, preserving the ORIGINAL bag. These two capacity regimes are
exhaustive and the proof needs no MI228/230 unreviewed theorem.

**Preregistration BEFORE experiment.** Diagnostic grid:
a=1..2,b=a+1..a+3,u=b..b+2,v=u..u+2,w=v..v+3,
h=max(6,u+v,w)..a+b+u+v-1. Check ordinary capacity by32 labelled
masks against subset-bitset; test ALL legal p<=q. Predict every
question constructs under the selector above. For EVERY canonical
profile compare U to the literal intersection of six B difference
sets, and check EVERY feasible offset/order with index intersection
and BOTH literal physical geometry validators. Repeated B gaps use
distinct permutations only, not six artificially labelled orders.
Predict exactly THREE canonical failures in this grid: the uniform
repair family above at b=2,3,4. Exhaust their complete original-positive
root/order rectangles under BOTH parity assignments: zero witnesses.
For EVERY forced-capacity profile, all fitting labelled masks must have
exactly one partner beside w. For the selected partner check the full
feasible offset map/all distinct remaining orders: universal bad set
exactly{0,Y-X}, by both literal geometry validators and index collisions.
Every selected construction must pass original bag/owners/window and
both geometry checks. No new actual E28 partitions or residual census.

Forced-branch named controls: M20,(1,3,3,3,6),15/17 must choose a
nonconstant remainder; M26,(1,4,4,4,9),21/23 has only partner1,
constant remainder4,4,4 and must work without inventing an ordering.
Outside-grid counterfactual M28,(2,4,4,4,9),23/23: blindly choosing
partner2,offset-2 gives A=(2,4,13),B=(0,4,8,12),correct original
bag but shared4. Both geometry tests must reject; choose partner4
and a nonconstant remainder instead. This is one extra formula, not
an expanded grid or generic allocation search.

Unexpected graph controls: retain complete offset maps for BOTH
vertex identifications w=b and w=a+b, and verify the latter's extra
bad offset occurs only at u=v=b. One named larger uniform repair,
a1,b10,u=v10,w11,h22,p41/q43, must certify outside the grid. The
earlier six-label fixture must refuse; no extension below h6.
Caps6000 formulas/100000 offset-order or exception-root cases,
4CPU sec/64MiB. Stop ANY mismatch, retain failure; no repaired
prediction, widened grid, generic cycle solver or new review queue.
Current MI228+MI230 carrying read remains nonblocking during this block.


### MI239 — B106 outcome: unequal short gaps need no separation margin (2026-10-17 04:53 BST)

All predictions pass. The fixed grid has1067 profiles and34,144 labelled
capacity-mask checks, agreeing with subset capacity. Its1575 legal
positive questions give1530 canonical constructions,3 uniform repairs
and42 forced-nonconstant constructions. Three named outside-grid calls
make1578 formulas total; all pass full ORIGINAL bags/positive ownership,
window and BOTH literal geometry validators.216 grid formulas reflect.
The grid itself has no legal forced-constant question; its separate
preregistered named control exercises that branch without widening it.

There are787 complete feasible-offset maps:641 canonical and146 forced-
partner profiles, including profiles without legal positive pairs. Each
agrees exactly with literal difference-set intersection, index collision
and both independent physical geometry tests. For every fitting labelled
mask in the forced regime, the largest gap has exactly one partner, as
predicted. The selected partner's entire map has only the two endpoint
bad offsets. The graph vertex identifications are actually exercised:
20 canonical maps have w=b,99 have w=a+b. Their universal bad offsets
match the stated path/two-triangle classifications; no unlisted internal
resonance survives.

Exactly three grid questions exhaust canonical allocation: b=2,3,4
in the a1,u=v=b,w=b+1,h2b+2 repair family. Their complete original-bag
maps under BOTH parity roles contain72 candidates and ZERO witnesses,
among108 exception-root/order cases. All three uniform repairs succeed.
Combined offset-order/exception cases22,108, within100,000. These are
canonical impossibility statements, not nonexistence of a folded cycle.

Named controls pass. M20,(1,3,3,3,6),15/17 selects partner3 and a
nonconstant remainder. M26,(1,4,4,4,9),21/23 has ONLY partner1 and
constant remainder4,4,4; it constructs A=(1,2,11),B=(0,4,8,12).
The naive partner2 counterfactual at M28,(2,4,4,4,9),23/23 has the
correct original bag but shares4; BOTH geometry tests reject it.
Selecting partner4 instead certifies A=(0,9,13),B=(2,6,10,12).
The larger uniform repair b10 certifies A=(0,10,21),B=(1,11,12,22)
at M46,41/43. The old h5 fixture refuses as specified; it is also outside
the unequal-short class, so this is not an isolated test of that one
hypothesis. No new actual E28 partition or global residual count.

CPU0.561394s,peak RSS18,821,120bytes, within4CPU sec/64MiB.
Source tests/probes/instinct/path_forest_unequal_short_cycle.py;
prereg9fd542e7. Immutable artifact
cited/instinct/b106-unequal-short-cycle-b199240da3750b78.json,
575,154bytes,SHA256 b199240da3750b789fb210798ba85d17bef7c5b34f798ddf81b91a39bf687dd9.
Output digest and manifest receipts verified. No failed prediction,
expanded grid, generic cycle solver, new partition count or E28 census.

**Niggle sweep / circularity check.** The six-cycle argument requires six
DISTINCT prefix vertices; w=b and w=a+b are not silently included.
Both identifications have separate carrying proofs and complete offset
controls. A cover with fewer than three vertices cannot cover a six-cycle;
a cover with exactly three must alternate (its complement is an independent
triple with all cyclic spacings2). Matching either cover would force a
middle gap b-a<b, contrary to sortedness, not an assumed geometry theorem.

In the forced-partner branch the B-maximum is above A's interior because
R+r>h and w>=r; omitting this endpoint inequality would leave an unexamined
collision. Proper B prefixes are below Amax because their omitted last
gap is at least min(D)>X. Thus the reduction really leaves ONE forbidden
proper prefix plus the two common-endpoint offsets. Nonconstant prefix
avoidance is proved directly in MI238; constant remainders are not fed
to that lemma. The failed alternative partner t leaves a load a+2t
which already fits, so its failure implies w+t>h, giving F<t. This is
the exact evidence behind the constant-case bypass.

Ordinary capacity is used only to choose one of FOUR forced partners,
before geometric reasoning. Root intervals come solely from nonnegative
slack and legal ORIGINAL positives. Prefix avoidance/disjointness is then
proved, and reflection restores exact positive ownership. No conclusion
about a desired partition or about E28 is used to prove an intermediate
step. Finite map agreement is diagnostic, not the infinite quantifier.
The explicit repair is a uniform formula for every b>=2, not three grid
patches. No known elementary supporting fact gets a separate proof entry.

**Carrying milestone / one priority replacement.** The direct statement
now worth the next outside read is MI238 itself:

 For0<a<b<=u<=v<=w,h>=6,a+b+u+v>h, ordinary two-bin capacity
 and legal odd joins suffice for a folded-distinct seven-vertex cycle.

This is PROOF-SKETCH, with COMPUTED diagnostics. It strictly enlarges the
old unequal-short separated class and uses simpler self-contained arguments;
it does NOT include the equal-short a=b boundary, which remains MI234/236.
Replace MI228+MI230 as the single ACTIVE carrying-read priority by MI238.
Keep those results SKETCH and retained; park only their review request.
Ask Cloud specifically to read the two degenerate graph cases and the
constant-remainder forced-partner argument. Delete only the old outgoing
review flag, then issue ONE new REVIEW-REQUEST after pushing. This is
a replacement, not a new queue or a halt for permission.

Gut: delight at the six-cycle and at replacing a margin with sortedness;
the pull is warm because the mechanism changed. Reasoned verdict: all
nonisolatable unequal-short five-gap bags now have a direct sufficiency
candidate, awaiting independent verification. Equal-short bags with
u<2s and isolatable largest gaps remain outside this statement; full
N5/E28/L8 is OPEN. Next cheap inference: whether a comparable prefix
graph settles the remaining equal-short region u<2s, rather than run
another arbitrary-family census. No next experiment opened. Research13min
continues independently; older held lanes stay held.


### MI240 — B107: two infinite obstructions at a thin equal-short root (2026-10-17 05:04 BST)

**Actual steering.** The initial pull was to carry the equal-short argument
below u=2s. Unease: a root interval with only TWO offsets cannot use a
three-consecutive escape argument. Following that unease gives two
infinite canonical obstruction families, not another finite exception
list. Delight is attached to their uniform repairs. This block resolves
that thin-root obstruction before attempting a general low-middle claim.

Record searched: equal.*short.*small|u<2s|one.*partner.*prefix ->0 hits;
5s-1|4s.1.*6s.3|thin.*equal.*middle ->0 hits,including ledgers.
Read MI234/236's interval assumptions and MI238/239's scope. Their
u>=2s/equal-short exclusions matter; the calculation below does not
refute a stated theorem. No literature novelty claim.

**Precise family / hand classification BEFORE computation, SKETCH.**
Take s>=2,s<t<2s,w=t+s,h=t+3s,M=2(h+1),negative halves
(s,s,t,t,w). The largest is nonisolatable since h<2s+2t iff s<t.
Canonical loads L=2t,S=2s+w=h fit, with H=h-L=3s-t,J=0.
Put r=2s-t in{1,...,s-1}; H=s+r>=3,K=3(s+t).
ALL legal positive pairs p<=q are parameterized by

 1<=alpha<=ceil(H/2), p=4t-1+2alpha,
 q=2t+6s+1-2alpha, p+q=2K.

In the canonical allocation, relative A={0,t,2t},B has the three
orders of(s,s,w). The exact universally bad feasible offset set is

 U={-H,-s,-r,0} on[-H,0].

This follows directly from the three minimal prefix-hitting pairs:
the endpoint collisions are -H,0; w-s=t supplies the proper-prefix
collisions -s,-2s,t-2s,t-s, of which only-s,-r are feasible.
Here -2s<-H and t-s>0. With J=0, the representative root interval
is ONLY I={-alpha,1-alpha}. Both offsets are bad exactly in these
two cases:

 F1: r=1, t=2s-1,alpha=1,h=5s-1,
     p=8s-3,q=10s-3;
 F2: t=s+1 (s-r=1),alpha=s,h=4s+1,
     p=q=6s+3.

Proof of exhaustion: alpha<=ceil(H/2)<H excludes the far endpoint-H.
The only adjacent pairs among the remaining bad offsets are(-1,0)
when r=1, and(-s,-r) when s-r=1. The first forces alpha1; the
second forces alpha=s, which is allowed exactly at H=2s-1.
At s2,t3 the two profile conditions coincide but their positive pairs
are DIFFERENT:13/17 and15/15. No duplicate family count or contradiction.
Every other pair has a free one of the two offsets, hence a safe order
of the same three canonical B shapes. Select by parity/root sum and
reflect/reverse BOTH chains if root sum alpha-1, retaining ownership.

**Uniform repairs for ALL s>=2.** Both switch to A gaps(t,w),
B gaps(s,t,s). For F1 use directly

 A=(1,2s,5s-1),B=(0,s,3s-1,4s-1).

The root sum1=alpha gives exactly max(q),min(p); the seven indices
are visibly distinct for s>=2. For F2 use pre-reflection chains

 preA=(s-1,2s,4s+1),preB=(0,s,2s+1,3s+1).

Their root sum s-1=alpha-1 gives intermediate positives(6s+5,6s+1).
Reflect/reverse both in h=4s+1, giving

 A=(0,2s+1,3s+2),B=(s,2s,3s+1,4s+1).

These are disjoint and give the ORIGINAL equal pair6s+3 twice. The
alternative allocation and reflection are separate carrying steps;
neither is justified merely by a canonical capacity calculation.

**Preregistration BEFORE experiment.** Fixed diagnostic domain:
s=2..12,t=s+1..2s-1,h=t+3s,ALL legal p<=q (also independently
enumerate odd pairs from p+q=2K and compare to the alpha parameterization).
Predict66 profiles and exactly22 original-positive canonical failures,
the two families at each s, with the s2 overlap counted as two questions.
Every other question must construct canonically; all22 failures must
use the stated uniform repair. Check all32 labelled capacity masks
against subset capacity. For EVERY profile compare literal intersection
of the three A-B difference sets on[-H,0] to U; test EVERY feasible
offset/order with index intersection and BOTH physical geometry validators.
Hand shapes must equal distinct permutations. Check all selected formulas'
ORIGINAL bags/positive owners/windows and both geometry validators.

For each of the22 failures, exhaust the full original-positive fitting
root/order rectangles under BOTH parity assignments, not only the
two representative offsets. Predict198 original-bag candidates/zero
witnesses (12 per F1,6 per F2),1518 complete root/order cases. No
generic cycle solver, new E28 partition or full residual census.
Two named out-of-grid formulas s50: F1(t99,h249,p397/q497) and
F2(t51,h201,p303/q303), to check the algebra beyond the small grid.

Counterfactual endpoint-only rejection: s3,t5,h14,p21/q27,naive
canonical A=(1,6,11),B=(0,3,6,14) has the correct original bag but
shares6, despite offset-1 avoiding endpoint offsets0,-4. Both geometry
tests must reject. Unexpected original-bag control: F2 at s3 gives
valid pre-reflection A=(2,6,13),B=(0,3,7,10) with23/19, NOT21/21.
Omitting reflection must pass geometry and fail the original bag.
The declared diagnostic predicts4290 offset/order plus exception-root
cases. Caps1000 formulas/6000 such cases,2CPU sec/64MiB. Stop ANY
mismatch, retain failure; no repaired hypothesis or widened grid.

No general low-middle sufficiency theorem is claimed yet. A further
hand lead (not an experiment): in forced-partner allocation the constant
remainder argument may extend to r equal to or larger than its repeated
step, using failure of the alternative partner to trap F between adjacent
multiples. The non-thin low-middle canonical cases also need their own
exhaustive hand classification. These are next inferences, not inferred
from the present grid. Sole carrying read MI238 stays nonblocking;
this will be a READ-LEDGER addendum, not another review request.


### MI241 — B107 outcome: thin-root failures have uniform repairs (2026-10-17 05:06 BST)

All prescribed checks pass. The66-profile grid gives447 legal positive
questions, agreeing exactly between independent odd-pair enumeration
and the alpha parameterization.425 construct canonically; EXACTLY22
require the two predicted repairs,11 of each. Two named s50 controls
make449 formulas total. All pass ORIGINAL bags/positive owners/windows
and BOTH physical geometry validators;66 grid constructions reflect.
All2112 labelled capacity-mask checks agree with subset capacity.

Every complete feasible offset map agrees with U={-H,-s,-r,0},
independently by the three literal difference sets, index intersections
and both geometry tests. Hand-expanded B shapes equal the three distinct
permutations. The22 full original-positive root/order maps under BOTH
parity assignments have198 candidates and ZERO valid canonical witnesses.
Their1518 root/order cases plus2772 offset/order cases give the predicted
4290 total. At s2,t3 the two different questions13/17 and15/15 are both
present; sharing a negative profile does not merge their positive data.

The endpoint-only counterfactual has the correct21/27 bag but shared6;
both geometry validators reject it. Omitting F2 reflection at s3 passes
geometry but gives23/19 instead of21/21, as predicted. The s50 formulas
pass on397/497 and303/303 without altering the diagnostic grid. No
new actual E28 partition or global residual count was run or claimed.

CPU0.104920s,peak RSS16,834,560bytes, within2CPU sec/64MiB.
Source tests/probes/instinct/path_forest_thin_equal_short.py;
prereg5127704e. Immutable artifact
cited/instinct/b107-thin-equal-short-8a6994373bb333cd.json,
156,843bytes,SHA256 8a6994373bb333cdfa055bfcf6e810688cc77ccc60fd49088612f10b386a1801.
Output digest and manifest receipts verified. No widened grid, repaired
prediction, generic cycle solver or new review queue.

**Niggle sweep / infinite absence versus finite maps.** The carrying
argument is the adjacent-pair classification, not the66-profile grid.
The original-positive root sums are alpha and beta=H+1-alpha; reflecting
both chains maps the beta geometry to representative sum alpha-1, with
the B order reversed and still in the same three-order class. The
intermediate bag is different, as explicitly checked; the map is used
for geometry equivalence, then reversed to restore original ownership.
For F1, the original roots1 and H fail respectively at internal offset-1
and common-maximum offset-H. For F2 the single original root alpha=beta=s
fails at offset-s. Swapping the two parity roles preserves existence,
minimum/maximum sums and gap bags, not traversal words; the finite maps
independently check both roles. Thus the general obstruction statement
has a carrying hand argument beyond the measured zero counts.

The old three-consecutive escape argument is not applied to a two-point
interval. The far endpoint-H cannot enter I because alpha<H. The two
families need different repairs: one uses root sum alpha, the other
alpha-1 and BOTH-chain reflection. Distinct indices in their uniform
formulas follow from s>=2; successful s50 controls do not replace those
inequalities. No general equal-short low-middle criterion follows from
this one thin subfamily. Infinite classification/repairs stay PROOF-SKETCH;
the finite constructions/exhaustions are COMPUTED. Full E28/L8 OPEN.

**Incubator, not a further experiment or carrying request.** For a
constant forced remainder(t,t,t), the equal-partner case r=t has
0<F<2t and the endpoint exclusion z!=0 rules out F=t. If r>t and
the alternative partner t fails, w+t already fits, so h<r+2t.
Then Y=h-3t<r-t and X=h-w-r<=h-2r<2t-r, yielding t<F<2t.
Together with MI238's r<t case this suggests a general forced-partner
extension. It is not used to prove the thin-root result or adopted as
a full five-gap theorem here; check its complete scope before composing.

Gut: relief that the thin interval unease was productive, and delight
that two infinite failures need two uniform formulas rather than case
patches. Reasoned verdict: the main obstruction within this thin family
is completely classified by hand, with exact bounded diagnostics. Next
cheap step is the non-thin low-middle canonical classification and the
forced-partner extension above, before any larger census. MI238 remains
the sole active carrying read, nonblocking; send READ-LEDGER only.


### MI242 — B108: the remaining equal-short allocation cases (2026-10-17 05:15 BST)

**Pull / bounded question.** The two thin families changed the picture:
the remaining task is a structural completion, not loosening another
margin or counting another residual. The pull is toward finishing the
low-middle classification and checking the constant-partner argument's
scope. This would join the existing candidates into a nonisolatable N5
criterion; it would NOT settle isolatable largest gaps or E28/L8.

Record searched: non.thin.*middle|r>t.*constant|2,2,3,5,5 ->0 hits,
including ledgers. Read MI234/236,MI238/239 and MI240/241,especially
their exact root/constant-remainder hypotheses. No novelty claim for
the supporting prefix/interval facts; this is direct record development.

**Hand completion, PROOF-SKETCH BEFORE experiment.** Let halves be
(s,s,u,v,w),s>=1,s<=u<2s,u<=v<=w,h>=6,2s+u+v>h, ordinary
two-bin capacity and legal odd p,q as in MI238. In the canonical
allocation L=u+v,S=2s+w, suppose L,S<=h; H=h-L,J=h-S,d=L-S.
The same root interval I applies. For BOTH A orders and the three
B orders, the exact universally bad feasible offsets are

 u=v: U={0,d}, adding{-s,d+s} iff w in{u,u+s} AND H>=s;
 u<v: U={0,d}, adding{-s,d+s} iff v=w=u+s AND H>=s.

Why these formulas still hold below2s: in the two-middle-order
calculation the potential extra intersection at u=s,w=v+s is
excluded by w<L, which follows from canonical capacity/nonisolation.
Other putative intersections require a middle gap0 or v=s<u,
impossible. The three minimal prefix covers remain valid at w=2s
(the graph becomes a triangle). If all five halves equal s, its
complete difference set is multiples of s; feasibility H<2s,J<s
leaves exactly{-s,0}={d,0}. This separately handles the collapsed
constant graph, rather than importing a distinct-vertex argument.

For u=v=t in(s,2s),w=t, the four sorted bad offsets have gaps
t-s,2s-t,t-s. A triple of consecutive bad integers requires s2,t3.
At a thin J0 boundary H=2s-t<s, extras are absent; t=s merely
duplicates the endpoint offsets. Thus this resonance leaves only

 d=(2,2,3,3,3): h8,p11/q15; h8,p13/q13; h9,p9/q17.

For u=v=t,w=t+s,J>0, the sorted bad gaps are2s-t,t-s,2s-t.
Again a triple requires s2,t3, but then nonisolation forces h9,J0,
so there is NO non-thin obstruction here. The J0 case is exactly
MI240's two infinite families, already repaired uniformly.

For u<v,the only resonance is v=w=u+s. When u=s its extras duplicate
endpoints. Otherwise s<u<2s and the sorted bad gaps are
u-s,2s-u,u-s; a triple again requires s2,u3, giving

 d=(2,2,3,5,5): h10,p15/q19; h10,p17/q17; h11,p13/q21.

At J0 the resonance has H=2s-u<s, so there are no extra feasible
offsets. Other thin cases have only the endpoint obstructions and
a strict interior offset. With both slacks positive, three consecutive
offsets suffice unless one of these triples occurs. In general try
at most FIVE offsets because |U|<=4, then at most six local orders.
This is a hand exhaustive classification of the remaining canonical
failures, not an inference from the proposed finite grid.

**Six fixed repairs.** For the first three use preA=(1,3,6),
preB=(0,2,5,8). For the last three use preA=(1,3,8),
preB=(0,2,5,10). Root sum1 equals alpha or alpha-1; reflect/reverse
BOTH chains and flip the positive owner exactly in the latter case.
The same two coordinate patterns therefore cover all six cases with
their ORIGINAL positive bags, without root or cycle search.

**General forced-partner extension.** If w+2s>h, the proof that the
largest has exactly one partner does NOT need unequal short gaps.
Consider the four forced partners, prefer a fitting one whose remainder
D is nonconstant. The strict bounds X<min(D),Y<r and the one-forbidden-
proper-prefix reduction in MI238 also do not need a<b. Its elementary
nonconstant swap argument still applies. If EVERY fitting choice has
D=(t,t,t), there are three exhaustive cases:

 r<t: alternative partner t has remaining load r+2t<=3t<=h;
 its failure gives w+t>h,so X<t-r,Y<r and0<F<t.
 r=t: X<t,Y<t give0<F<2t; avoiding endpoint z0 excludes F=t.
 r>t: w+t<=w+r<=h already; alternative failure gives h<r+2t.
 Hence Y<r-t,X<=h-2r<2t-r,so t<F<2t.

Thus no constant proper prefix t or2t is hit in any of the three
cases. This extends the forced-partner candidate to ALL five-gap
bags, not only unequal-short ones. The root interval/endpoints and
both-chain reflection complete the construction as before. This
argument uses no unproved full E28 statement or desired geometry.

**What composition would say, conditionally on carrying reads.**
MI238 handles a<b; MI234/236 handle a=b=s,u>=2s; the argument above
plus MI240 handles a=b=s,u<2s. With the forced-partner extension,
every NONISOLATABLE five-gap bag would have sufficiency under label,
ordinary capacity and legal-positive conditions. This remains a
COMPOSITE PROOF-SKETCH, not a proved theorem, not a full N5 census,
and not a claim about an isolatable largest gap.

**Preregistration BEFORE experiment.** Fixed diagnostic grid:
s=1..4,u=s..2s-1,v=u..u+2,w=v..v+s,
h=max(6,u+v,w)..2s+u+v-1. Check all32 labelled capacity masks
against subset capacity; test ALL legal odd positive pairs p<=q.
Predict every question constructs by canonical local order choice,
the six fixed repairs, MI240's thin formulas or the general forced
partner. Predict exactly12 original-positive canonical failures in
this grid: six fixed cases above and both thin families for s2,3,4.
On EVERY canonical profile compare U with literal intersection of all
distinct A/B difference sets, then check EVERY feasible offset/order
by direct intersection and BOTH physical geometry validators. All
selected formulas must pass ORIGINAL bags/owners/windows and both tests.

For EVERY forced profile all fitting masks must give exactly one
partner beside w; the selected partner's whole feasible offset/all-order
map must have universal bad set exactly{0,Y-X}. Check X<min(D),Y<r
and each constant-case inequality in its stated branch. For each of
the12 canonical failures exhaust complete ORIGINAL-positive root/order
maps under BOTH parity assignments and require zero witnesses.
No generic cycle solver, new actual E28 partitions or residual census.

Named grid branch checks: M16,(2,2,2,2,4),11/13 must use r=t;
M26,(4,4,4,5,5),21/23 must use r>t and constant remainder4.
One outside-grid larger r>t formula: M62,(10,10,10,11,11),45/59.
Counterfactual: M18,(2,2,2,3,5),13/15,blindly choosing constant
remainder with partner3 gives A=(0,3,8),B=(1,3,5,7),correct bag but
shared3. Both geometry tests must reject; the selector must choose
the fitting partner2 with a nonconstant remainder instead. The
alternative-failure premise is therefore a carrying condition.
Unexpected collapsed-graph check: retain all constant-five profiles'
complete canonical maps, not just the generic prefix graph branch.

Caps4000 formulas/60000 offset-order or exception-root cases,
3CPU sec/64MiB. Stop ANY mismatch, retain failure; no patched claim,
wider grid or new review queue. MI238 remains the sole active carrying
priority; this completion will be a READ-LEDGER addendum, nonblocking.


### MI243 — B108 outcome: a candidate for the whole nonisolatable five-gap case (2026-10-17 05:18 BST)

All prescribed checks pass. The grid contains759 profiles and24,288
labelled capacity-mask checks, agreeing with subset capacity. Its1220
legal positive questions construct as follows:1065 canonical,118 forced
with nonconstant remainder,23 forced with r=t,2 forced with r>t,
6 fixed repairs and3 of EACH thin family. The named larger r>t control
makes1221 formulas total. Every selected formula passes its ORIGINAL
bag/positive ownership/window and BOTH geometry validators.192 grid
constructions reflect; no intermediate positive pair is accepted.

All489 complete feasible offset maps agree with the hand bad sets:
327 canonical and162 forced-partner maps, including profiles without
legal positive pairs. The nine all-five-constant canonical profiles
are explicitly retained and have bad set{-s,0}; they are not silently
passed through a distinct-prefix-vertex proof. In every forced capacity
mask the largest has exactly one partner. All strict root/constant-case
inequalities pass in their stated branches, and the selected partner's
whole feasible map has only the two endpoint bad offsets.

The grid has EXACTLY12 original-positive canonical failures: the six
fixed cases and six thin-family questions, as preregistered. Their full
maps under BOTH parity roles contain198 original-bag candidates and
ZERO witnesses, among630 complete exception-root/order cases. Combined
offset/order and exception cases13,370, within60,000. All twelve
explicit alternative constructions certify the original pairs.

The named r=t and r>t grid questions pass. Blindly choosing constant
remainder with partner3 at M18,(2,2,2,3,5),13/15 has the exact bag
but shared3; both geometry tests reject it. The selector chooses the
fitting partner2 with a nonconstant remainder instead. The outside-grid
M62,(10,10,10,11,11),45/59 control uses r>t and certifies
A=(1,12,23),B=(0,10,20,30). No new actual E28 partitions or global
residual count. The negative control shows why alternative-partner
failure must be proved before applying the constant-remainder shortcut.

CPU0.397857s,peak RSS19,689,472bytes, within3CPU sec/64MiB.
Source tests/probes/instinct/path_forest_equal_short_completion.py;
prereg0d585d5a. Immutable artifact
cited/instinct/b108-equal-short-completion-53a8c40c854e7272.json,
410,285bytes,SHA256 53a8c40c854e7272aa232c3ecac3f57ac36e3fa4bc64a34b4301d31cc21da89c.
Output digest and manifest receipts verified. No failed prediction,
widened grid, generic cycle solver, new partition count or global census.

**Composite candidate, exact scope, PROOF-SKETCH.** Let M=2n,h=n-1>=6,
0<d1<=...<=d5,K=sum(d),and d1+d2+d3+d4>h. Suppose the five gaps
can be partitioned into two loads each<=h. Given positive odd p,q
with p+q=2K,max(p,q)<=2h-1,not both2h-1, there exist disjoint
increasing index chains A,B in[0,h] whose gap multisets partition d,
and whose physical seven-cycle has the exact move bag
{p,q,-2d1,-2d2,-2d3,-2d4,-2d5},with seven distinct folded labels.

The carrying case division is now exhaustive BEFORE any finite test:
canonical capacity fitting uses MI238 for unequal smallest gaps;
for equal smallest s it uses MI234/236 when u>=2s,MI242 when u<2s,
with MI240's thin subfamily. Canonical capacity failure for EVERY
bag uses MI242's general forced-partner argument. Thus the composite
does not need MI230 as an extra theorem. There are no open canonical
parameter cases asserted away by a count. The proofs of these steps
are NOT independently verified; the composition does not upgrade them.
This candidate is not a full N5 existence census, a statement about
an isolatable largest gap, or a proof of full E28/L8.

**Niggle sweep / circularity.** The threshold u=2s belongs to MI234/236;
the new side is strictly u<2s, so no boundary is lost. The equal-middle
all-constant collapse has its own feasible-difference argument. At w=2s
the three minimal covers are the triangle covers; no distinct-four-
vertex hypothesis is retained. The new u=s,w=v+s resonance is excluded
by w<L, not by a sign inequality imported from u>=2s. Thin root
intervals use MI240; they are never treated as three consecutive points.

The forced constant cases partition r<t,r=t,r>t. At r=t, forbidden
prefix t corresponds exactly to the already-excluded common minimum
z0; it is NOT handled by the nonconstant lemma. At r>t, w+t already
fits, so failure of the only alternative value really gives h<r+2t.
The source prefers nonconstant remainders whenever available, including
the explicit wrong-partner control. All capacity choices precede the
geometric argument; no target geometry is used to infer its own root
or partner capacity. Finite diagnostics do not supply any infinite
quantifier or an independent second read.

Gut: delight in reaching an exhaustive case division after the thin-root
unease redirected the argument. Reasoned verdict: the nonisolatable N5
folded-cycle sufficiency is now a composite proof candidate, pending
carrying verification, with the missing isolatable side sharply exposed.
The next cheap question is how its four-gap prefix obstruction behaves
when w can stand alone; inspect the existing MI204/206 rich/nearconstant
classification before proposing a new route. No new experiment opened.
Keep MI238 as the ONE active carrying priority; flag this completion
READ-LEDGER so Cloud has the scope change when reading. No new queue,
review halt or publication status upgrade. Research13min continues.


### MI244 — B109: isolatable largest gap and the three-unit exception (2026-10-17 05:30 BST)

**Pull / orientation.** The missing side already has the right ordering
theorem in the record. The new inference is root selection, especially
when K<=h and the two outer endpoint offsets are feasible. The specific
pull is toward the three-unit companion obstruction, whose full bad
interval survives every companion order; it forces an allocation change.

Record searched: the initial separate search terms were conjunctive,
not alternative searches. Corrected single-regex search
isolated.*largest|isolatable.*five|near.constant.*prefix|
two.separated.*prefix ->15 hits in4 files. Read MI204/206 in full,
MI222's exact four-gap scope,MI218's existing one-exception composition
and their constructors. Prior zero conjunctive hits do not imply an
absence from the record. No new literature/novelty claim. Constant four-
step companions already belong to MI218; do not re-prove or re-census them.

**Candidate, SKETCH BEFORE experiment; rich case conditional on MI204.**
Let0<b1<=b2<=b3<=b4<=D,nonconstant B=(b1,b2,b3,b4),S=sum B,
h>=6,S<=h,D<=h. Given legal odd p,q with p+q=2K,K=S+D,
max<=2h-1,not both2h-1, claim a folded-distinct seven-cycle exists.
No K>h hypothesis is imposed. Put H=h-D,J=h-S,T=H+J>=2,
alpha=(2h+1-max(p,q))/2; use the root-sum interval I from MI234.

For the isolated A={0,D},the exact universal bad offset set on[-H,J]
is F0={-S,0,D-S,D} plus the following internal obstruction. If B has
no three equal items, there is NONE by MI204 (two proper barriers are
separated by D>=max B; one barrier uses MI117). If B=(s,s,s,t),t!=s,
MI206 adds exactly

 {z:D-S<z<0,s divides z} if D=t mod s.

The endpoint set is restricted to the feasible range; when K<=h the
outer points-S,D must NOT be dropped. This is the key difference from
the earlier MI222 application. If rich, D>=2,S>=6; the sorted endpoint
spacings cannot make three consecutive bad integers. If repeated s>=2,
the internal bad levels are multiples of s between D-S and0, separated
by at least2. Their outer endpoint spacings are D>=s; if D>=S there
are no internal obstructions. Thus again no triple of consecutive bad
integers exists. With H,J>=1 a free offset exists among the first3 in I.
At H0, take positive alpha strictly inside(0,J); D>=S prevents internal
obstructions. At J0, rich/incongruent cases use-alpha strictly inside
(-H,0); the congruent case has only s-spaced bad offsets and its two
adjacent representatives cannot both be bad. This proves the root
selection for rich and nonunit near-constant companions, including K<=h.

**Three-unit companions.** Now B=(1,1,1,t),t>=2. If D>=t+3=S,
only endpoint failures remain. If D=t+2, the internal bad interval has
no extra integer beyond its adjacent endpoints; thick I escapes and
the J0 case has T1,so no legal pair. The remaining possibilities are
D=t or t+1. Write J=h-(t+3)>=0. For D=t,H=J+3,alpha<=J+2;
I contains the safe offset1 except J0 (alpha1/2) or J1,alpha3.
For D=t+1,H=J+2,alpha<=J+1;I contains1 except J0,alpha1.
Accounting for h>=6 gives exactly FOUR obstruction families:

 U1:D=t,t>=3,h=t+3,p=2t+1,q=2t+5;
 U2:D=t,t>=3,h=t+3,p=q=2t+3;
 U3:D=t,t>=2,h=t+4,p=q=2t+3;
 U4:D=t+1,t>=3,h=t+3,p=2t+3,q=2t+5.

These are failures of the WHOLE isolated-D allocation, not merely one
chosen companion order. Representative root sums alpha/alpha-1 are
equivalent to both original-positive root sums through BOTH-chain
reflection; reversed orders stay in the same companion class.

**Uniform repairs.** For U1 use A=(0,t,t+1),B=(1,2,t+2,t+3).
For U2 use those pre-chains and reflect/reverse in h=t+3 (root1=alpha-1).
For U3,t>=3,use preA=(2,3,t+3),preB=(0,1,t+1,t+2),then
reflect/reverse in h=t+4 (root2=alpha-1). Its t2 boundary instead uses
A=(3,5,6),B=(0,1,2,4). For U4 use
A=(0,t+1,t+2),B=(1,2,3,t+3). Each has pairwise distinct indices
in[0,h] and the full ORIGINAL move bag; reflection flips the positive
owner. The one small t2 case is already covered by MI180's full-label
theorem; its coordinates complete this selector, not a separate theorem.

Every other nonconstant-companion case therefore has an isolated-gap
order/root construction. One may choose among the first SEVEN offsets
of I uniformly: F0 has at most4 points and the near-constant internal
part at most2 (D>=t, S=3s+t). At a safe offset choose among at most24
distinct B orders to realize the prefix theorem. This is a bounded local
selector, not a whole-cycle solver. The four unit families use the
explicit alternative formulas above.

**What this would compose with.** Constant companions(s,s,s,s) plus D
are ALREADY the one-exception bag of MI218 (including s1 via MI191/195).
Together with MI243 for nonisolatable largest gaps, the present candidate
would give the standard label/load/positive conditions as a sufficient
criterion for ALL N5 folded seven-cycles. This would be a COMPOSITE
PROOF-SKETCH, with MI204's rich case and MI218's dependencies explicit;
not independent verification or a solution of full E28/L8.

**Preregistration BEFORE experiment.** All nonconstant sorted B multisets
of length4 with entries1..3;D=max B..max B+3;
h=max(6,S,D)..max(6,S,D)+3;ALL legal p<=q. Predict every question
constructs, and exactly FIVE original-positive isolated-D failures:
U3 at t2,and all four families at t3. Require that K<=h questions
actually occur and all four endpoint offsets are retained where feasible.
For EVERY profile compare universal bad sets against intersection of all
distinct B permutation difference sets;check EVERY feasible offset/order
by direct index intersection and BOTH physical geometry tests. For every
selected formula check ORIGINAL bags/positive owners/window/both tests.
For all five failures exhaust original-positive root rectangles/all B
orders under BOTH parity assignments:zero witnesses. No constant-companion
run, new E28 partition, generic cycle solver or residual census.

Four named outside-grid formulas t50: U1(101/105,h53),U2(103/103,h53),
U3(103/103,h54),U4(D51,103/105,h53). No outside-grid offset scan.
Counterfactual: at U1,t3,h6,naive isolated A=(1,4),B=(0,1,2,3,6)
has the correct7/11 bag but shared1. Both geometry checks must reject.
Unexpected small-label boundary: the U3,t2,h6 formula must be the
special A=(3,5,6),B=(0,1,2,4); blindly extending the t>=3 pre-formula
gives preA=(2,3,5),preB=(0,1,3,4),valid7/7 bag after reflection
but an internal shared3 before it. Reject it by both geometry tests.
Also check U2,t3 omitted reflection retains geometry but gives11/7
rather than9/9. Caps1500 formulas/30000 offset-order or exception-root
cases,3CPU sec/64MiB;stop ANY mismatch,retain failure,no repaired
prediction or widened grid. MI238 sole carrying read stays nonblocking;
READ-LEDGER completion only, no second review queue.


### MI245 — B109 outcome: a composite candidate for all five-gap folded cycles (2026-10-17 05:33 BST)

All predictions pass. The192-profile grid has6144 labelled capacity-mask
checks, agreeing with subset capacity. Its703 legal positive questions
give698 isolated-gap constructions and EXACTLY5 predicted allocation
failures,one each U1,U2,U3,U3_small,U4; all five alternative formulas
pass. Four named t50 controls make707 formulas total. Every formula
passes its ORIGINAL bags/positive owners/windows and BOTH geometry
validators.120 grid constructions reflect. There are108 genuine K<=h
questions across21 profiles: the two outer endpoint offsets are retained
where feasible, rather than applying MI222's K>h simplification.

All192 complete offset maps agree exactly with the hand bad sets,
independently by literal difference-set intersections,index collisions
and both physical geometry tests. The five complete original-positive
failure maps under BOTH parity assignments have72 candidates and ZERO
isolated-allocation witnesses, among248 root/order cases. Overall9712
offset/order cases plus248 failure cases give9960,within30,000.
The four t50 formula controls pass without widening the diagnostic grid.
No constant-companion run, new E28 partition or residual census.

The naive U1 isolated witness has the correct7/11 bag but shared1;
both geometry tests reject. Blindly extending U3's t>=3 formula to t2
shares3 before AND after reflection, even though the reflected word
has the correct7/7 bag. Both tests reject; the specified small repair
works instead. Omitting U2 reflection preserves geometry but gives11/7,
not9/9. Thus neither geometry alone nor a correct move bag is accepted
without the other. All negative predictions were retained and pass.

CPU0.228932s,peak RSS17,154,048bytes,within3CPU sec/64MiB.
Source tests/probes/instinct/path_forest_isolatable_five.py;
prereg9274c23c. Immutable artifact
cited/instinct/b109-isolatable-five-a33a9b32e71e6b14.json,
238,613bytes,SHA256 a33a9b32e71e6b149c3cb8d0c41c2624287765f79da7d8164a108ebb4598a787.
Output digest and manifest receipts verified. No failed prediction,
repaired hypothesis, expanded grid or generic cycle solver.

**Composite candidate: sufficiency for the FULL N5 folded-cycle model,
PROOF-SKETCH ONLY.** For M=2n,h=n-1>=6,let0<d1<=...<=d5,K=sum d.
Assume the five halves split into two loads each<=h. Let p,q be positive
odd,p+q=2K,max(p,q)<=2h-1,not both2h-1. Candidate conclusion:
disjoint increasing index chains A,B in[0,h] exist,with gap multisets
partitioning d,whose physical seven-cycle has exactly
{p,q,-2d1,-2d2,-2d3,-2d4,-2d5},and seven distinct folded labels.

The complete carrying division is now:

| Largest-gap regime | Companion/parameter regime | Carrying source |
| --- | --- | --- |
| sum(d1..d4)>h | All five-gap bags | Composite MI243 |
| sum(d1..d4)<=h | Four companions all equal | Existing MI218,not reproved |
| sum(d1..d4)<=h | No companion repeated three times | MI244 root selector,conditional MI204 |
| sum(d1..d4)<=h | Three equal companions with repeated step>=2 | MI244 root selector + MI206 arithmetic proof |
| sum(d1..d4)<=h | Three unit companions plus t>=2 | MI244 four uniform families + isolated selector |

Ordinary capacity implies d5<=h,so the isolated load pair fits whenever
the companion sum<=h. The multiplicity division is exhaustive. This
composition uses UNREVIEWED carrying steps,including MI204 and MI218's
listed dependencies; it is not an independent proof verification. The
finite diagnostics check constructors and scope changes,not the infinite
quantifier. No novelty, full E28/L8 solution or prize is claimed.

**Niggle sweep / circularity.** When K<=h, complete offset maps can
contain geometrically disjoint chains whose distinguished joins are not
both positive. They are collision-table entries only; every accepted
formula separately checks its ORIGINAL positive p,q and owners. Endpoint
membership is never mistaken for an original-positive witness. The rich
ordering step remains explicitly conditional on MI204; it has not become
PROVED through a successful local permutation loop. MI218 is cited at its
full one-exception scope and was read,not silently inferred from a test.

For the three-unit failure classification, D>=t leaves only t,t+1,t+2
when D<S; all larger D have no two-internal-prefix interval. The root
intervals at J0/J1 are checked separately. U1/U2 at t2 would require
h5 and are outside the seven-label hypothesis; U3 starts at t2 and
needs its actual small repair. Reflection is applied to BOTH chains and
the positive owner. All full-candidate case choices depend on values,
capacities and proven-by-hand conditional prefix statements,never on
the desired cycle's existence. No circular assumption was found in this
self-check; independent scrutiny is still required.

**Early closure reflection, before another family.** About81 minutes
after MI232's fresh-choice reflection. The enjoyable part is the six-cycle
and uniform-repair explanation; the less enjoyable part is the growing
unreviewed dependency stack and its documentation. If I had not invested
in N5,I would now choose to attack the candidate's carrying proof,not
automatically begin N6. That is a change of trajectory on evidence: the
case division is provisionally closed,so more variants would risk a loop.
The pull stays warm toward finding a missing inference or a shorter
proof. Next cheap work is an adversarial self-read of MI204's rich-prefix
argument and the composite dependencies. This is NOT a second-party
review and will not upgrade a status. No new experiment opened.

Gut: delight at the completed candidate,unease about relying on several
unreviewed sketches. Reasoned verdict: mathematical scope has moved to
a complete N5 sufficiency candidate; verification is the next obstruction.
Keep the13-minute schedule active. MI238 remains the ONE requested
carrying priority; flag this completed scope READ-LEDGER,not another
review queue or a routine permission halt. Full E28/L8 remains OPEN.


### MI246 — B110 hand audit: the N5 rich-prefix step needs only four items (2026-10-17 05:43 BST)

**Pull/question.** The pull is toward shortening the carrying proof; the
unease is the accumulated unreviewed dependency stack. Does the rich
four-companion branch of MI245 actually need MI204's arbitrary-length
constant-block argument? It does not. This is a specialized proof of
the existing MI204 claim, attached here to simplify the composite
candidate, not a new theorem or another review job. Record searched:
four.step.*barrier|four.*prefix.*repair|permutation.*connected|spread.*barrier
->5 historical hits in2 files, none supplying this specialization.
MI204 and MI206 read in full; their explicit arguments, not that search
count, are the source. No new experiment, probe or empirical result.

**Four-item statement, PROOF-SKETCH / self-check only.** Let four positive
integer steps have sum S and maximum M, with no value appearing three
times. If0<x<y<S and D=y-x>=M, an ordering exists whose proper prefixes
avoid both x and y. The following supplies its complete carrying argument.

For a nonconstant positive multiset a single proper level t can be
avoided: if an order hits it, cut there, choose unequal items across
the cut (otherwise every item equals every other), move those items
adjacent to the cut within their blocks and swap. Only that prefix
changes; earlier prefixes stay below t and later ones above t.

Suppose every ordering hits x or y. Avoiding each level separately
gives an x-only and a y-only order. Label repeated occurrences. The
adjacent-transposition graph on these permutations is connected, and
each swap changes just one proper prefix by |u-v|<M<=D. An edge cannot
go directly from an x-only order to a y-only order: that would require
the changed prefix to move from x to y. A connecting path must therefore
contain an order hitting BOTH, under the assumed absence of an order
avoiding both. Split it into nonempty blocks A,B,C with sums x,D,S-y.
Since there are four items, B has either one or two items.

If B has two, A and C are singletons a,c. Among the two labelled B
occurrences let L be those differing from a, R those differing from c.
Neither set is empty: emptiness gives three equal items. They have
distinct representatives v in L,z in R: otherwise L=R is the same
singleton, and the other B item equals a AND c, again three equal
items. Order the items a,v,z,c, then swap the two disjoint boundary
pairs to obtain v,a,c,z. Only the prefixes formerly x and y change;
each change has magnitude less than D and is nonzero. Neither can
reach the other barrier. The middle prefix remains strictly between
x and y. This order avoids both.

If B is a singleton, its value is D=M. There are three outside items
across nonempty A,C. Some a in A,c in C must differ; otherwise all
three outside items agree. Put a last in A and c first in C, producing
the triple(a,M,c) after sum x-a. If a<M, replace the triple by(M,c,a).
Its first new prefix is y-a in(x,y), its second y+c-a is greater than
x and different from y, and its unchanged end y+c exceeds y. If a=M,
then c<M; use(c,M,a). Its new prefixes are x-M+c<x and x+c in(x,y),
and its end again exceeds y. All other prefixes are unchanged. This
also avoids both, completing the contradiction.

**Direct hand controls, not a census.** Both repair types and the
singleton maximum boundary have concrete arithmetic checks:

| Steps; barriers | Both-hit order | Repaired order; proper prefixes |
| --- | --- | --- |
| (1,1,2,2);1,4 | (1,2,1,2) | (2,1,2,1);2,3,5 |
| (1,2,2,3);2,5 | (2,3,1,2) | (3,1,2,2);3,4,6 |
| (1,2,3,3);3,6 | (3,3,1,2) | (1,3,3,2);1,4,7 |

Unexpected boundary check: keeping rich steps(1,1,2,2) but moving the
barriers to2,3 violates D>=M and makes the pair unavoidable. Its six
distinct words1122,1212,1221,2112,2121,2211 have prefix sets respectively
{1,2,4},{1,3,4},{1,3,5},{2,3,4},{2,3,5},{2,4,5}. Every set meets2 or3.
Thus positivity, richness and separation play distinct roles; richness
alone does not replace the separation hypothesis. This rechecks the
type of boundary already noted in MI204, without a novelty claim.

**Dependency change, not a status upgrade.** In MI245's rich isolated-gap
row use MI244's root selector plus THIS four-item argument, instead of
the arbitrary-m theorem. Outside endpoint collisions, the two potential
internal companion levels are -z and G-z, separated by the isolated
largest gap G>=max(companions). If both levels are proper, the argument
above applies; if only one is proper, its opening one-level argument
applies; if neither is proper, no internal collision is possible.
MI204's general constant-block step is no longer needed for this row.
MI204 is retained unchanged, not refuted or withdrawn. MI206's
one-exception arithmetic and MI218's constant-companion dependencies
still carry their OTHER rows; no finite constructor check verifies them.

**Niggle sweep / circularity.** Labelled occurrences justify connectivity
despite repeated values. Boundary pairs in the two-item case are disjoint;
the singleton case uses a rotation instead. Positivity makes each hit
unique and gives the strict swap bound even when D=M. In the singleton
rotation y+c-a>x follows from M>=a and c>0; c!=a excludes y. Reordering
within the original blocks cannot introduce a new barrier hit. Neither
the adjacency argument nor either repair assumes the desired cycle or
uses an empirical witness. All are self-checks, not independent scrutiny.

Gut: satisfaction at needing less machinery, with the original unease
reduced but not erased. Reasoned verdict: the rich row now has a short,
self-contained carrying sketch; FULL N5 remains an UNVERIFIED composite
candidate and full E28/L8 remains OPEN. Next cheap audit is the constant
four-companion specialization of MI218, before generating N6 families.
MI238 stays the sole carrying-review priority; send this as a READ-LEDGER
addendum, not a second review queue. Research13min stays active.


### MI247 — B111 hand audit: constant four-companion branch with fewer dependencies (2026-10-17 05:54 BST)

**Pull/question.** Remove the whole-family invocation where only a small
specialization carries N5. Does MI245's constant-companion row need all
of MI218's dependencies? No: its largest gap D is at least the repeated
step s, so MI216's smaller-exception theorem never applies. The unit
base also has an overlap that avoids MI195's special boundary owner rule.
This is an audit/specialization of existing arguments, not a new theorem
or independent verification. Record searched:
four.*constant|R4.*unit|constant.*companion|balanced.*one.exception
->91 paragraphs/28 files; relevant MI212/214/218 and the existing source
path_forest_unequal_ladders.py. MI180/188, MI191, MI195 and MI214/216/218
read directly. No experiment, new probe or empirical coverage result.

**Exact scope, PROOF-SKETCH.** In MI245's isolated-largest constant row,
negative halves are(s,s,s,s,D), with D>=s>=1, h>=6,4s<=h,D<=h.
Positive odd p,q sum2K, K=4s+D, max(p,q)<=2h-1, not both2h-1.
Then the following arguments construct the required disjoint chains.
Capacity of the isolated split is already explicit; no additional
capacity inference or smaller-exception result is being assumed.

**Repeated step s>=2: specialize MI214 directly.** Put

    k0=max(0,ceil((4s-D)/(2s))), L0=D+k0s, S0=(4-k0)s.

Then k0 is0,1 or2 and L0>=S0. If L0<=h, take heavy A with j=k0
repeats followed by terminal u=D, and B with3-j repeats followed by
terminal v=s. If L0>h, k0 cannot be0 (D<=h) or2 (D+2s<4s<=h).
Thus k0=1 and3s<D<4s. Use A's four s-steps, B's single D-step:
j=3,u=s,v=D. They fit because4s,D<=h. Let L=j*s+u,S=(3-j)*s+v.
In either branch L>=S,delta=L-S<=u; in fallback0<delta<s.

The root repair needs delta1=>u>=3. In the first branch delta1 cannot
have D2: at s=D2, k0=2 and delta2. In fallback u=s=2,delta1 would
force D7,L0=9>h>=8. But K15 and the legal/non-doubled positives give
K<=2h-2, hence h>=9, a contradiction. This checks the small terminal
boundary rather than silently borrowing the general selector's assertion.

Put H=h-L,J=h-S=H+delta,T=2h-K>=2, P=max(p,q),Q=min(p,q), and
alpha=(2h+1-P)/2. Then1<=alpha<=H+floor((delta+1)/2).
If alpha<=2H, take largest odd c<=alpha, with z=1 unless delta1,
when z=-1; x=(c-z)/2,y=(c+z)/2. Both roots fit0..H,0..J.
If alpha>2H, necessarily delta>=2. Put x=H,z0=alpha-2H and choose
c=alpha-1 if s divides z0, otherwise c=alpha; set y=c-H,z=y-x.
If reduction occurs z0>=s>=2, so z>=1. Also
z<=floor((delta+1)/2)-H<delta for every delta>=2. Thus0<z<delta and
s does not divide z. Finally y<=J since c<=alpha<=T.

Use A=x+(0,s,...,js,js+u), B=y+(0,s,...,(3-j)s,(3-j)s+v).
The ladders have different residues modulo s. Both terminals exceed
both ladders exactly when delta-u<z<delta+v, and terminal equality
requires z=delta. Our root choices satisfy these inequalities: at z1
use delta<=u and exclude delta1; at z-1 use delta1 and u>=3; in the
thin branch use0<z<delta<=u. So all seven indices are distinct.
When c=alpha-1 reflect/reverse BOTH chains in h. Before reflection
the joins are P+2,Q-2; after it they are exactly Q,P. With c=alpha
they are already P,Q. No intermediate bag is accepted as the original.

**Unit step s1, D<=6: use the proved seven-label core and padding.**
Here K=D+4 lies5..10. In core h0=6, permissible first odd values are
I=[max(1,2K-11),min(11,2K-1)] on the odd lattice, with at least two
consecutive odd points. Put e=h-6>=0. Select an odd u in

    I intersect [p-2e,p+2e], with u=p-2e modulo4.

The intersection is nonempty by p,q<=11+2e and p,q>=1. If e0 it
contains p. If e>0 and only one odd point remained with the wrong
residue, neither end could have come from [p-2e,p+2e], whose endpoints
have the required residue. Both would therefore be the same endpoints
of I, contradicting its width. With at least two odd points the residue
is present. This is MI191's r0 interval argument, specialized explicitly.

Apply PROVED MI180 (CL428, adopted MI188) to the five halves in the
seven-label core with joins u,2K-u. Let P0 be its first, larger join,
and let P be the matching original owner (p if P0=u, otherwise q;
equal core joins permit either assignment). Then t=(P-P0)/2 has
|t|<=e and t=e modulo2. Translate every core index by ell=(e-t)/2
and enlarge h0 to h. Both chains remain disjoint and fit because
0<=ell<=e. Joins become P0+2e-4ell=P and the other original positive;
all negative gaps stay fixed. Only the already VERIFIED full-label
theorem is imported; the padding arithmetic above remains a self-check.

**Unit step s1, D>=7: strict inner-block argument.** Set P=max(p,q),
alpha=(2h+1-P)/2,H=h-D,Bmax=D-5>=2. The other positive Q<=2h-3
because the doubled maximum is excluded. Hence1<=alpha<=2H+Bmax.
Choose b=min(Bmax,alpha), reducing it by1 if its parity differs from
alpha; put a=(alpha-b)/2. Reduction cannot make b0, and if alpha>Bmax
the wrong-parity bound alpha-Bmax<=2H-1 ensures a<=H after reduction.
Thus0<=a<=H,1<=b<=D-5. Use

    A=(a,a+D), B=(a+b,a+b+1,...,a+b+4).

B lies strictly between A's two endpoints, all in0..h. Minimum sum
2a+b=alpha gives P; maximum sum alpha+D+4=alpha+K gives Q. The
gap bag is exactly D and four units. MI195's D6 parity/owner boundary
is unnecessary HERE: D6 is already in the small-core branch above.

**Hand controls / unexpected check.** No program or new census:
- s3,D11,h13,p=q23 forces the fallback. Pre-chains
  A=(1,4,7,10,13),B=(0,11) give25/21. Reflection in13 yields
  A=(0,3,6,9,12),B=(2,13), giving23/23 and disjoint indices.
- s3,D11,h14,p=q23 uses the thin-root residue reduction. Unreduced
  A=(0,3,14),B=(3,6,9,12) shares3. Correct pre-B=(2,5,8,11), then
  reflection gives A=(0,11,14),B=(3,6,9,12), with exact23/23.
- Unit D6,h6,11/9 has A=(0,6),B=(1,2,3,4,5). At D6,h8,13/7,
  core joins11/9 and ell2 give A=(2,8),B=(3,4,5,6,7), starting
  with the ORIGINAL7, then13. Core/owner swapping is real, not cosmetic.
- Unit D7,h8,11/11 has a1,b1: A=(1,8),B=(2,3,4,5,6).
  Unexpected parity countercheck: using b2 and flooring a to0 gives
  disjoint A=(0,7),B=(2,3,4,5,6) but joins13/9, not11/11. Geometry
  alone would miss the original-bag error.

**Niggle sweep / verdict.** Five gaps mean seven vertices; h>=6 is
retained, not inferred from the unit mass. Every constructed join is
compared after reflection/padding, with the corresponding original owner.
The repeated-gap first/fallback cases are exhaustive by k0's three
possible values and h>=4s. Unit D1..6 and D>=7 cover every allowed D;
there is no reliance on an experiment or on the desired cycle's existence.
No fault in the cited scope was found; this is NOT a second-party read.

Gut: satisfaction that the constant branch also sheds unused machinery.
Reasoned: MI245's constant row may use this specialized sketch plus
PROVED MI180, rather than importing all MI218 dependencies. MI218 and
its general sources are retained unchanged. Full N5 remains UNVERIFIED;
full E28/L8 remains OPEN. Next cheap audit: derive MI244's three-unit
exception exhaustion again from its root intervals, rather than trusting
the diagnostic grid. MI238 stays the sole carrying request; READ-LEDGER
addendum only, no new review queue or routine halt. Research13min active.


### MI248 — B112 hand audit: four unit-companion exceptions are exhaustive (2026-10-17 06:07 BST)

**Pull/question.** Unease about an exception list supported by a successful
grid; the pull is toward the small inequalities that make it exhaustive.
Can MI244's three-unit row be derived directly without the grid or MI206's
general classification? Yes. This audits the existing candidate, not a
new family, experiment or independent review. Record searched:
three.unit.*exception|four.*obstruction.*famil|unit.*root.*interval
->6 paragraphs/3 files; relevant MI244 and its existing constructor
path_forest_isolatable_five.py read. The constructor is not the proof.

**Fixed setting, PROOF-SKETCH.** Negative halves(1,1,1,t,D), with
t>=2,D>=t, S=t+3<=h,D<=h,h>=6. Put K=S+D, H=h-D,J=h-S,
T=H+J=2h-K>=2. Original positive odd joins satisfy p+q=2K,
max(p,q)<=2h-1 and are not both2h-1. Let P=max(p,q),Q=min,
alpha=(2h+1-P)/2, so1<=alpha<=floor((T+1)/2)<T.

**All-order collision set, directly.** Isolate A's D-gap. For relative
start z, the four order-independent endpoint collisions are
F0={-S,0,D-S,D}. Outside these, at most two collisions remain: companion
proper prefixes at -z or D-z. If just one level is proper, a nonconstant
positive bag avoids it by the one-level boundary swap (MI246's opening
argument). If neither is proper there is nothing to avoid.

If both are proper, write x=-z>=1 and e=D-t>=0. The upper level is
D-z=t+(x+e)<S=t+3, hence x+e<=2. Any companion order has k units
before t, k in0..3. If k>=x, its initial unit prefixes hit x. Otherwise
k<=x-1<=x+e<=2, so its post-t prefixes hit t+(x+e). Thus both internal
levels cannot be avoided. The EXACT all-order bad set is therefore

    F0 union {integer z: D-S<z<0},

restricted to feasible offsets[-H,J]. For e0,1,2 the central bad part
including its endpoints is [e-3,0] on the integers. For e>=3 there
is no internal bad interval. This is a direct four-order argument,
independent of MI206's all-length congruence simplification.

**Why the representative roots cover BOTH original positives.** Actual
root sums are alpha and beta=T+1-alpha. Reflecting/reversing both chains
maps a root sum c to T-c, and z to J-H-z; the companion class is closed
under reversal. Thus beta corresponds exactly to representative alpha-1.
Conversely a representative alpha-1 construction reflects to original
Q first,P second; its intermediate joins P+2,Q-2 are not the target bag.
Swapping the two chains preserves endpoint sums and disjointness, so fixing
the isolated gap on A does not omit the opposite parity assignment.

At representative sum c, feasible offsets have parity c and range
[max(-c,c-2H),min(c,2J-c)]. The unions for c=alpha and alpha-1 give
the consecutive integer interval

    [-alpha,alpha]                   if alpha<=min(H,J);
    [alpha-1-2H,alpha]               if H<alpha<=J;
    [-alpha,2J-alpha+1]              if J<alpha<=H.

The alpha bound excludes alpha>max(H,J). Given an offset in this
interval, take c=alpha when parities agree, otherwise alpha-1, then
x=(c-z)/2,y=(c+z)/2. This explicitly recovers feasible roots; a free
integer is not being assumed to have the required parity automatically.

**Exhaust the four possibilities for e.** If e>=3, D>=S. The endpoint
set {-S,0,D-S,D} has no three consecutive integers: its two outer
spacings are S>=5, and only the middle spacing can be small. If H,J>=1
the interval above has at least three consecutive integers, so it escapes.
If H0, J=T>=2, then D-S=J and z=alpha lies strictly between0,J and
avoids every endpoint. J0 is impossible here since H<=J. No exceptions.

For e=0,1,2 one has H=J+3-e>=J, so only the first or third interval
form is needed. Whenever it belongs to I, z1 is safe: the central bad
interval is nonpositive and D>=2 keeps1 away from the outer endpoints.

| e | Bound on alpha | I when alpha>J | Cases where1 is absent |
| --- | --- | --- | --- |
| 0 | alpha<=J+2 | alpha=J+1: [-J-1,J]; alpha=J+2: [-J-2,J-1] | J0,alpha1 or2; J1,alpha3 |
| 1 | alpha<=J+1 | alpha=J+1: [-J-1,J] | J0,alpha1 |
| 2 | alpha<=J+1 | alpha=J+1: [-J-1,J] | None: T=2J+1>=2 forces J>=1 |

When alpha<=J, I=[-alpha,alpha] already contains1. In each listed
absence case the ENTIRE interval is contained in the central bad part:
e0 gives [-1,0],[-2,-1] or[-3,0]; e1 gives[-1,0]. Thus these are actual
all-order isolated-allocation failures, not failures of the chosen z1.
Substituting h=t+3+J and P=2h+1-2alpha yields EXACTLY:

| Family | D,h,range | Unordered original positive pair |
| --- | --- | --- |
| U1 | D=t,h=t+3,t>=3 | 2t+1,2t+5 |
| U2 | D=t,h=t+3,t>=3 | 2t+3,2t+3 |
| U3 | D=t,h=t+4,t>=2 | 2t+3,2t+3 |
| U4 | D=t+1,h=t+3,t>=3 | 2t+3,2t+5 |

The lower t bounds come from h>=6, not the diagnostic grid. D=t+2,J0
would have T1 and permits only the excluded doubled maximum; it is not
a fifth exception.

**Repairs as FINAL coordinates, no intermediate owner ambiguity.**
These restate MI244 after its prescribed reflections, not new formulas.

| Family | Final A | Final B | First,second positive joins |
| --- | --- | --- | --- |
| U1 | (0,t,t+1) | (1,2,t+2,t+3) | 2t+5,2t+1 |
| U2 | (2,3,t+3) | (0,1,t+1,t+2) | 2t+3,2t+3 |
| U3,t>=3 | (1,t+1,t+2) | (2,3,t+3,t+4) | 2t+3,2t+3 |
| U3,t2 | (3,5,6) | (0,1,2,4) | 7,7 |
| U4 | (0,t+1,t+2) | (1,2,3,t+3) | 2t+5,2t+3 |

All rows have seven disjoint indices in0..h. Their five gap multisets
are exactly(1,1,1,t,D). Using first join2h+1-2(min A+min B) and
second2(max A+max B)-(2h+1) gives the table, directly by substitution.
The t2 special row uses all seven available labels. Extending the generic
U3 formula to t2 shares3, so that separate boundary remains necessary.

**Unexpected hand check: outer endpoints still matter when K<=h.**
Take t2,D5,h10,p11/q9. Then H=J5,alpha5,I=[-5,5], with bad
offsets{-5,0,5}. Dropping the outer endpoint -S=-5 would accept
A=(5,10),B=(0,1,2,3,5): correct11/9 joins, but shared5. A safe
choice is z1,x2,y3 with A=(2,7),B=(3,4,5,6,8), giving exactly
11/9 and no collision. This is direct arithmetic, not a new experiment.

**Niggle sweep / verdict.** The bad interval uses STRICT internal levels;
its endpoints are in F0, never supplied by a fictitious final prefix.
Root reflection covers both original-positive owners, and chain swapping
covers the isolated gap's parity role. The three small-J cases for e0
and one for e1 are the complete complement of the safe z1 cases. Every
repair is checked in final coordinates, after the original-bag correction.
No inference uses the grid or the conclusion being proved.

Gut: the pull warmed at seeing the four families come from tiny spare-
capacity boundaries rather than a catalogue. Reasoned: no omitted unit
family found; this row now has a direct exhaustive carrying sketch.
It is still a SELF-CHECK, not independent verification. MI244/245 and
full N5 remain PROOF-SKETCH; full E28/L8 remains OPEN. MI238 stays the
single requested carrying read; READ-LEDGER addendum only.

After three dependency audits, avoid automatically generating more audit
entries. Next useful HAND question is structural: can merging two halves
in a six-gap list reduce it to N5 while keeping the required subdivision
point free? A provisional N5 premise must be labelled as such; a blocked
subdivision would refute that lifting method, not the six-gap criterion.
Search the record before pursuing it. No experiment or new claim opened
here, and no routine review halt; research13min stays active.


### MI249 — B113: change of route; rich six-gap completion in arbitrary windows (2026-10-17 06:23 BST)

**Pull / change on evidence.** The proposed merge/subdivide question led
back to the existing two-gap/four-gap geometry MI208/210. Reading it before
inventing a lifting argument changed the route. Its fixed h13 thin case
uses an ODD window length to exclude equal top gaps. General windows expose
a real obstruction, with a simple allocation repair. Surprise and warmth
are tied to that missing boundary, not another parameter table.
Record searched: merge.*subdiv|subdiv.*gap|insert.*free.*point|
split.*negative.*gap ->one pointer to MI248; direct notebook search then
found MI085/090 and MI208/210. Read those relevant subdivision/endpoint
arguments and path_forest_span_rich.py. Further single-regex search
equal.*top.*thin|u=S\+1|S\+1.*largest|span.*rich.*arbitrary|
span.*dominant.*general ->one unrelated historical ledger hit. This is
not an absence/novelty claim. No new experiment or program execution.

**Initial lifting question: an arbitrary chosen merge is NOT enough.**
At h7, halves(1,1,2,2,2,3),p=q11 have a full-label witness
A=(2,4,7),B=(0,1,3,5,6). Merging the two unit halves gives a feasible
N5 parent: A=(0,3,5,7),B=(2,4,6), gaps(3,2,2)/(2,2), same11/11.
Every midpoint of its four2-gaps is occupied. In fact NO parent witness
for that unit merge can have a free midpoint: a lifted witness would
fill all eight labels and have three consecutive indices of one colour.
For any full-label word in the original six-gap problem, the four nonunit
gaps force four internal runs of lengths1,1,1,2; joins11/11 force end
runs2,1. Every run has length<=2, a contradiction. Thus an unrestricted
chosen-pair lift is false even though both problems have witnesses.
This closes that shortcut, not N6; no separate proof entry/review request.

**General-window candidate, PROOF-SKETCH conditional only on MI246's
four-item prefix sketch.** Let h>=7,M=2(h+1), and sort six positive
negative halves b1<=b2<=b3<=b4<=D<=E. Put S=sum b_i,L=D+E.
Assume S<=L<=h and the four companions are rich (no value occurs three
times). For any positive odd p,q with p+q=2(L+S),max(p,q)<=2h-1,
not both2h-1, a folded-distinct eight-vertex cycle exists.
This extends MI210's fixed h13 class, not all six-gap lists or E28/L8.

**1. Roots and endpoint compatibility.** Put H=h-L,J=h-S>=H,
T=H+J>=2,P=max(p,q),Q=min,alpha=(2h+1-P)/2. Then
1<=alpha<=floor((T+1)/2)<T. Representative root sums alpha/alpha-1
give the consecutive offset interval

    I=[-alpha,alpha]            when alpha<=H;
    I=[alpha-1-2H,alpha]        when H<alpha<=J.

These cover all cases; when H=J, alpha<=H, and when H<J, alpha<=J.
Recover c by z's parity, x=(c-z)/2,y=(c+z)/2. For c=alpha-1,
reflect/reverse BOTH chains in h; root sum becomes T+1-alpha,
giving the original Q first,P second. This is the endpoint identity
rederived in MI248, not an assumption that N5 itself lifts.

For A's possible middle points x+D,x+E, BOTH orders collide with
one of B's endpoints precisely at

    F={-S,0,L-S,L},
    plus {u,u-S} if D=E=u,
    plus {D} if D<E and E-D=S.

Outside the four endpoint coincidences, both distinct middle choices
can hit the two B endpoints only when their difference is S. With
equal gaps there is just one middle choice. This proves the displayed
endpoint obstruction set without any ordering census.

If H>=1, I has at least three consecutive integers. Richness gives
S>=6,max b_i>=2, and D,E>=2. If D=E=u, L>=S forces u>=3; F is a
subset of two residue classes modulo u, so cannot contain three
consecutive integers. If D<E and E-D!=S, F's outer spacings are S>=6.
If E-D=S, its sorted values are -S,0,D,2D,L, with spacings S,D,D,S,
all>=2. Therefore some z in I escapes F, with an endpoint-compatible
A order. J0 is impossible because J>=H and T>=2.

**2. The thin case H0, including the formerly excluded equal top.**
Here L=h,J=T>=2 and I={alpha-1,alpha} lies in[0,J-1]. If D<E,
the four basic endpoint values meet I only at0. The possible extra
value D is>=2: at alpha1 choose z1, while at alpha>=2 at most one
of the two positive representatives can equal D. Thus this case works.

If D=E=u, then h=2u,J=2u-S. Also

    alpha<=floor((2u-S+1)/2)<=u-3,

since S>=6. The endpoint values -S,J,2u,u are all outside I; only
0 and u-S can obstruct its two consecutive representatives. At
alpha>=2,0 is absent and at most one is bad. At alpha1 the pair{0,1}
is wholly bad EXACTLY when u-S=1. Thus the ENTIRE top-two allocation
has just one obstruction family:

    D=E=u=S+1, h=2u, {p,q}={4u-1,2u-1}.

This is an allocation failure, not nonexistence of the prescribed cycle.
For the first original join4u-1, A=(0,u,2u) forces B_min1,B_max=u,
hitting its middle. For first join2u-1, B_min=u+1,B_max=2u, hitting
A's maximum. Reordering the companions changes neither endpoint.

**3. Complete the ordinary case with at most TWO proper barriers.**
After choosing z and an endpoint-compatible A order, its span L>=S
prevents all three A vertices from lying strictly inside B's span S.
If two are internal, they are consecutive A vertices, since both ends
cannot lie strictly inside a shorter/equal interval. Their separation
is D or E, each>=max b_i. MI246's four-item argument supplies a B order
avoiding both. One barrier uses its one-level swap; zero needs none.
Together with the separately checked endpoints, this gives disjoint
chains and the exact original move bag after any required reflection.

**4. Repair the entire thin family without prefix machinery.** At
u=S+1,h=2u, use

    A=(0,u),
    B=(1,u+1,u+1+b1,u+1+b1+b2,u+1+b1+b2+b3,2u).

B takes one u-gap then the four companion gaps. Its first vertex1
and all others>=u+1 miss A's0,u. Its last is u+1+S=2u=h, so both
chains fit and all eight indices are distinct. Their odd joins are
4u+1-2=4u-1 and2(u+2u)-(4u+1)=2u-1, exactly the original pair.
The two negative loads are now u and2u-1. This changes allocation,
instead of persisting with a blocked ordering. The repair itself
does not require richness, although the ordinary-case proof does.

**Hand boundary / unexpected checks, no new experiment.** For companions
(1,1,2,2),S6,u7,h14,p27/q13, the old top-two split A=(0,7,14)
forces B endpoints1,7 or8,14, so BOTH original owners fail for EVERY
companion order. The repaired A=(0,7),B=(1,8,9,10,12,14) is disjoint,
has the exact six-gap bag and joins27/13. With the same companions
and equal top u6,h12,p23/q13, A=(0,6,12),B=(1,2,3,5,7) works:
u=S is not part of the exceptional family. At u8,h16,p31/q13,
A=(0,8,16),B=(1,2,3,5,7) works too. Thus equality u=S+1, not merely
an even h or equal top gaps, is the obstruction. The original h13
proof remains valid: h=2u cannot occur there. No old claim is retracted.

**Niggle sweep / circularity.** The thin analysis uses the exact two
representatives, not the thick three-integer argument. Richness is used
only for the endpoint size bounds and MI246's two-prefix implication;
no arbitrary-m prefix claim or unverified N5 criterion is imported.
Final joins follow from the actual endpoints after reflection. The
exception is an endpoint collision before any prefix choice, and its
repair is a direct coordinate construction. The arbitrary chosen merge
failure was retained, not promoted to a universal reduction or forgotten.
No finite success substitutes for the infinite argument.

Gut: renewed warmth at a real thin-boundary obstruction turning into a
uniform repair. Reasoned: the span-dominant rich-four six-gap class now
has a general-window candidate, still UNVERIFIED and conditional on
MI246 SKETCH. Full N6, E28 and L8 remain OPEN. Next cheap check is a
small preregistered general-window diagnostic, comparing root/endpoint
maps independently and testing the new thin-family repair. No run is
opened here. Keep MI238 as the ONE carrying priority; send this as a
READ-LEDGER direction change, with no routine review halt. Research13min.


### MI250 — B114 preregistration: general-window rich-six boundary diagnostic (2026-10-17 06:33 BST)

**Question/pull.** Does the new general-window selector behave exactly
as MI249's hand proof predicts, including the one equal-top thin trap?
The pull is toward testing that sharp boundary, not counting more solved
targets. Record searched: general.window.*rich|equal.top.*thin|
span.dominant.*six ->2 paragraphs/2 files; MI210/211,MI246,MI249 and existing span-rich source
read. This is a test of constructors/maps; no independent proof read,
novelty claim, full N6 theorem or E28 coverage follows from success.

**Predictions BEFORE implementation/run.** Exactly EIGHT geometry calls,
all outside h13, no actual E28 partition or target census:

| h | Four companions | D,E | p,q | Predicted branch |
| --- | --- | --- | --- | --- |
| 8 | 1,1,2,2 | 3,3 | 13,11 | thick canonical, reflection |
| 8 | 1,1,2,2 | 4,4 | 15,13 | equal top below S, canonical |
| 12 | 1,1,2,2 | 6,6 | 23,13 | equal top at S, canonical |
| 14 | 1,1,2,2 | 7,7 | 27,13 | new thin trap, repaired |
| 16 | 1,1,2,2 | 8,8 | 31,13 | equal top above S+1, canonical |
| 12 | 1,1,2,2 | 3,9 | 19,17 | unequal thin resonance, reflection |
| 200 | 1,2,3,93 | 100,100 | 399,199 | large new thin trap, repaired |
| 14 | 1,1,2,2 | 7,7 | 25,15 | same thin profile, nonmaximal P, canonical |

Six canonical constructions/two repairs, exactly two reflections. Choose
canonical z by smallest absolute value,tie smaller z first, then first
endpoint-compatible A order and lexicographically first avoiding B order
(at most24). Each final formula checks ORIGINAL p/q ownership, entire move
bag, bounds, index disjointness and BOTH existing physical geometry tests.
Repairs use MI249's direct one-large-gap-per-chain formula.

Independent controls: all EIGHT root-sum interval sets against direct
root rectangles, including parity recovery. For the SEVEN distinct
profiles, compare F with the full intersection of all A-order/B-order
collision difference sets. Check EVERY feasible offset/order by direct
index intersection AND both physical geometry tests: exactly2742 cases.
These maps include intermediate geometries with nonpositive joins; only
the eight accepted formulas claim the ORIGINAL positive bag.

For BOTH new-trap calls exhaust their complete original-positive root
rectangles/all companion orders under BOTH parity roles. Predict small
108 cases/24 original candidates and large4896 cases/96 candidates;
ZERO canonical witnesses in each. All alternative repairs must pass.
Thus7746 map/failure cases total; no generic cycle/allocation solver.

Counterfactual: omit reflection on first fixture's pre-chains. Geometry
must still pass but joins become15/9, not13/11; original-bag comparison
must reject. Unexpected nearby-positive check: final fixture has the SAME
gap/window profile as the small trap, but alpha2 and z2 make the canonical
split work. The constructor must not apply a blanket equal-top repair.
Caps8 formulas/10000 offset-order and failure cases,3CPU sec/64MiB.
Stop any mismatch/cap, retain failure; no repair, enlarged fixture list
or new coverage claim. MI238 remains the sole carrying priority;
completion READ-LEDGER only, with no routine review halt.


### MI251 — B114 outcome: the general-window boundary diagnostic passes (2026-10-17 06:35 BST)

All EIGHT prescribed geometry formulas pass their original full move
bags, positive owners, bounds, disjoint indices and BOTH existing literal
physical geometry checks. Six are canonical, two use the thin-family
repair, and exactly the first/unequal-thin calls reflect. No new actual
E28 partition, target census, expanded fixture list or generic solver.

All EIGHT root intervals agree with independent complete root rectangles
and parity recovery. On the SEVEN distinct profiles, universal collision
difference-set intersections agree exactly with the hand endpoint sets.
All2742 feasible offset/order cases independently agree by index
intersection and both physical geometry tests. As preregistered, these
maps alone do not assert that intermediate odd joins are positive or
equal the requested pair; only accepted original-bag formulas do that.

The small trap's two full parity-role maps have108 cases and24 original-
positive candidates, zero valid canonical witnesses. The large trap has
4896 cases and96 original candidates, likewise zero. Their direct repairs
both pass. Thus the total is exactly7746 cases and120 genuine original
candidates, as predicted BEFORE running. This confirms the specified
whole-allocation failures, not merely failures of one chosen order.

Omitting reflection on the first formula preserves geometry but changes
13/11 to15/9; original-bag comparison rejects. The last fixture retains
the SAME gap/window profile as the small trap, but alpha2,z2 give
A=(0,7,14),B=(2,3,4,6,8), with exact25/15. The selector correctly stays
canonical instead of applying a blanket equal-top repair. Both retained
counterfactual and unexpected predictions pass without a repaired premise.

CPU0.151986s,peak RSS15,978,496bytes,within3CPU sec/64MiB. Source
tests/probes/instinct/path_forest_span_rich_general.py; prereg32a24c24.
Immutable artifact cited/instinct/b114-span-rich-general-42b1b0fcaeecf1f9.json,
4624bytes,SHA256 42b1b0fcaeecf1f967b8f37b815910280791fed081e74b0688e20199b2df9b3a.
Upload digest and manifest receipts verified. MI249 remains a hand
PROOF-SKETCH conditional on MI246, not independently verified by these
checks. Full N6/E28/L8 remains OPEN.

**Niggle sweep.** The large trap uses genuinely unequal companion values,
not a scaled version of the small two-pair fixture. Both original owners
and both choices of which parity chain contains the two largest gaps are
included in its failure map. The alternate positive pair tests alpha's
role separately from the equal-top profile. Geometry and the original
bag are checked independently; a disjoint wrong-bag intermediate is never
accepted. Counts concern these finite prescribed maps only, not a new
coverage total or an independent carrying read.

**New pull captured, not yet used as a theorem.** Return to subdivision
with a repeated merged value. If a parent has r edges of length s=a+b
and a!=b, each offers TWO possible subdivision points. An occupied vertex
of the opposite chain lies inside at most one parent edge. Moreover the
global minimum and maximum cannot block any interior subdivision point.
This suggests that a five-gap parent's seven vertices can block at most
five such candidates, so r>=3 should force a free insertion. That would
turn an explicitly provisional N5 premise into a new six-gap admission
for(s,s,a,b,t,u) with a+b=s,a!=b, provided the merged parent has capacity.
The cheap next HAND test is to prove or break the charging argument,
including cross-chain double counting and the equal-split counterexample
already retained in MI249. Do not infer it from this diagnostic.

Gut: satisfaction that the sharp boundary survived; renewed pull toward
the repeated-gap insertion count rather than another parameter family.
Reasoned: finite checks support MI249's implementation, with its proof
status unchanged. No new run opened for that next inference. MI238 stays
the single carrying priority; completion READ-LEDGER only, research13min
continues without a routine review halt.


### MI252 — B115: repeated merged gaps force a free unequal subdivision (2026-10-17 06:46 BST)

**Pull/question.** The failed arbitrary-merge shortcut left a specific
attraction: many copies of the same merged gap offer interchangeable
places to insert the new vertex. Is there a bound on how many choices
the opposite chain can block? Yes; global extrema remove two possible
blockers. Record searched: subdiv.*charg|block.*interior.*edge|
repeated.*merged|2r.*insertion|extrem.*subdiv ->9 paragraphs/6 files,
only MI251 relevant; further s=a\+b|free.*subdivision|
subdiv.*point.*count|two.*insertion.*choices ->2 paragraphs/1 file,
MI251 and an unrelated MI201 formula. MI180's chain encoding, MI249's
retained merge failure and MI251's question read. No novelty claim,
known-theorem reproof request, experiment or source execution.

**Geometric lemma, standalone PROOF-SKETCH.** Let disjoint nonempty
increasing integer chains A,B have N gaps in total, hence N+2 vertices.
Suppose a length s occurs r times among their consecutive gaps. Fix
positive unequal integers a,b with a+b=s. If2r>N, one occurrence of s
can be subdivided into a,b (in either order) by inserting a previously
unused integer index. All chain endpoints and every other gap stay fixed.

**Proof.** For an s-edge from v to v+s, the two possible new vertices
are v+a and v+b. They are distinct and strictly interior. Neither can
be a vertex of its OWN chain, because the endpoints were consecutive.
An unavailable choice therefore coincides with an opposite-chain vertex.
Charge that blocked EDGE/CHOICE PAIR to its occupying vertex.

This charging is injective: a B-vertex is strictly inside at most one
consecutive A-edge, and within that edge the two choices differ. It can
never block a B-edge choice. The same holds with A,B exchanged. The
global minimum and maximum of A union B lie inside no opposite-chain
edge, so neither can receive a charge. At most N of the N+2 vertices
can block choices. There are2r edge/choice pairs. If2r>N, at least
one remains free; insert it in its edge. It is already within the
existing window, is distinct from every old vertex and changes that
gap s into a,b or b,a. Endpoints are unchanged. This proves the lemma.

Coincident candidate COORDINATES from edges of opposite chains cause
no double charge: such a coordinate is inside both chains' edges, so
is in neither chain and is free. Count edge/choice pairs, not an
unjustified collection of globally distinct coordinates. No existence
of the desired subdivided cycle is assumed anywhere in the charge.

**Cycle consequence.** The chain encoding (MI180, PROVED/MI188) converts
a free insertion to an extra folded-distinct vertex. Both odd jumps
depend only on chain extrema, so retain their EXACT original values and
owners; the negative move -2s becomes -2a,-2b. Every other move stays.
For a five-gap parent N5, three copies of s suffice, since6>5.
This conditional lift applies to ANY supplied valid parent, regardless
of which chain its repeated edges occupy, root choice or gap order.

**Conditional six-gap admission.** For positive s,a,b,t,u with
a+b=s,a!=b, consider target halves(s,s,a,b,t,u). If the five-half
merged parent(s,s,s,t,u) fits two bins of capacity h>=7, and the
positive odd p,q satisfy p+q=2(3s+t+u),max<=2h-1,not both2h-1,
then MI245's N5 COMPOSITE SKETCH supplies a parent. The lemma supplies
the eighth vertex. This is a six-gap sufficiency SKETCH CONDITIONAL
ON THAT UNVERIFIED N5 CANDIDATE, not an independently verified theorem.
Do not replace merged-parent capacity by target capacity. A supplied
explicit parent instead makes the particular lift independent of MI245.

**Direct adversarial hand checks, no program or new census.**

1. Sharp repeated-count limit for arbitrary parents: at h7 take
   A=(0,3,6),B=(1,2,4,5),odd joins13/7. The two3-gaps offer points
   1,2 and4,5, ALL occupied. Thus r2 does not guarantee insertion
   even with room elsewhere in the window. This is a method failure;
   the target(1,1,1,2,2,3) still has the explicit witness
   A=(0,2,5,6,7),B=(1,3,4),same13/7.
2. Unequal split is essential: MI249's h7 parent
   A=(0,3,5,7),B=(2,4,6),odd joins11/11, has FOUR2-gaps but all
   their midpoints4,6,3,5 are occupied. For1+1 there is only ONE
   choice per edge, so pretending to have2r distinct choices is false.
3. Unexpected cross-chain coincidence: at h7 use
   A=(0,3,6),B=(1,4,5,7),joins13/11. Its three3-gaps offer six
   edge/choice pairs; free coordinate2 appears on BOTH chains' lists.
   It is not an occupied vertex or two distinct free coordinates.
   Insert2 into A: A=(0,2,3,6),B=(1,4,5,7),still13/11, all eight
   labels distinct. This tests the actual double-counting niggle.
4. A balanced case OUTSIDE MI249's span-dominant class: at h9,
   parent A=(0,3,6,9),B=(1,4,8),joins17/15,has four3-gaps.
   For1+2,point1 is blocked but2 is free. Insert2 in A to get
   halves(1,2,3,3,3,4),whose top-two span7 is below companion sum9.
   Physical positions(0,17,11,3,18,12,6,4) have moves
   (17,-6,-8,15,-6,-6,-2,-4),correct original17/15 and eight
   distinct folded labels. This actual witness does not assume MI245.

**Niggle sweep / verdict.** Choices are strictly interior, so no root
or terminal is silently changed. A blocker occupies at most one edge
interior of the other chain; touching an edge endpoint is excluded.
Global extrema are two distinct unusable blockers even if they belong
to the same chain. The unequal premise supplies two choices within each
edge, not an assumption about coordinates across chains. The new point
fits the old window automatically; no external padding is invoked.
The parent controls distinguish a failed lift from target nonexistence.
The conditional corollary openly retains MI245's status and capacity
hypothesis; it does not complete arbitrary six-gap selection.

Gut: delight at recovering subdivision through a simple count after its
unrestricted version failed. Reasoned: a standalone geometric lifting
sketch now gives a new conditional N6 admission, including a balanced
case outside the previous span-dominant class. Independent verification
is still required; full N6/E28/L8 remains OPEN. Next cheap diagnostic:
preregister a small COMPLETE set of two-chain geometries and compare
blocked-choice counts with an independent direct insertion check. Keep
the r2/equal-split controls. No experiment opened here. MI238 stays the
one carrying priority; READ-LEDGER only, no routine review halt or new
review queue. Research13min continues.


### MI253 — B116 preregistration: complete small subdivision geometry check (2026-10-17 06:59 BST)

**Question/pull.** Test MI252's charge/insertion distinction on a COMPLETE
small domain, especially repeated coordinates across opposite-chain
candidates. Record searched: repeated.gap.*subdiv|blocker.*charg|
complete.*two.chain.*geometr ->3 paragraphs/2 files; MI249/251/252 and
the existing physical/literal validators read. No new literature or
novelty claim. This diagnostic supplies explicit parents; it does NOT
assume or verify MI245's general N5 existence candidate.

**Predictions BEFORE implementation/run.** In the window0..7 choose
EVERY7-point subset and EVERY nonempty labelled two-colour partition.
Exactly8*(2^7-2)=1008 parent chain pairs, with5 gaps each. Compare this
enumerator independently with all ternary words of length8 having
exactly one empty position and both colours; the complete sets must agree.
For every parent and each occurring gap value s, try EVERY positive
unequal unordered split a<b,a+b=s. Count r occurrences across BOTH chains.
Each occurrence offers the two ordered subdivision choices. Predict:

- blocked edge/choice pairs charge to distinct occupied vertices;
- neither global extremum is charged, so blocked count<=5;
- every question with2r>5 has a free choice, with a nonvacuous r3 case;
- direct insertion into either chain agrees with the predicted free/
  blocked status under BOTH physical geometry validators, preserves both
  extrema, every other gap and both ORIGINAL ordered odd joins;
- whenever these parent joins are both positive, each accepted child
  also passes the existing full original-bag/owner/window validator.

All free choices are checked, not just the first. Nonpositive parent
joins remain legitimate geometric-lemma controls; do not call them
original-positive cycle admissions. No N5 existence solver, target
census, new E28 partition or full N6 claim.

Four named hand fixtures from MI252 are retained separately:
R2:A=(0,3,6),B=(1,2,4,5),h7,s3,a1/b2 ->all4 choices blocked;
equal:A=(0,3,5,7),B=(2,4,6),h7,s2,a=b1 ->all4 UNIQUE choices blocked;
cross:A=(0,3,6),B=(1,4,5,7),h7,s3,a1/b2 ->six choice pairs,free
coordinate2 appears TWICE, and no blocked vertex receives two charges;
balanced:A=(0,3,6,9),B=(1,4,8),h9,s3,a1/b2 ->point1 blocked,point2
free, first accepted insertion in A gives(0,2,3,6,9),same17/15.

Counterfactual: duplicate the equal fixture's sole midpoint as if two
choices existed; fake2r=8>5 wrongly predicts insertion, while deduplicated
four choices are all blocked. Reject the theorem's unequal premise there,
rather than silently counting the midpoint twice. Unexpected check:
the cross fixture must retain two free EDGE/CHOICE PAIRS at one coordinate;
a global-coordinate uniqueness assertion would incorrectly reject it.
Caps1008 exhaustive parents plus4 fixed controls,40000 insertion checks,
5CPU sec/64MiB. Stop any mismatch/cap; retain failure,no corrected
prediction, expanded window or repaired family. MI238 remains the sole
carrying priority; completion READ-LEDGER only, no routine review halt.


### MI254 — B116 outcome: complete small subdivision check passes; retain the capacity gap (2026-10-17 07:01 BST)

All1008 labelled seven-point parent chain pairs agree EXACTLY with the
independent ternary-word enumeration. Across them there are1112 unequal
split questions and24 nonvacuous forcing questions with2r>5. Every
blocked-choice map is injective into the nonextreme vertices and has
at most5 charges; every forcing question has a free choice. These
counts are finite diagnostic outcomes, not predictions retrofitted
into the proof or a claim about all windows.

Every candidate insertion, free OR blocked, passes its predicted status
under direct intersection and BOTH existing literal physical geometry
checks. Extrema, ordered original odd joins and the expected gap bag
remain exactly unchanged except for the specified subdivision. There
are2584 exhaustive insertion checks plus22 fixed-control checks,2606
total. The594 free children with both original joins positive also
pass the existing full original-bag/owner/window validator. Other
parents remain geometric controls, not positive-cycle admissions.

All four fixed controls pass without repair. The r2 fixture blocks
all4 choices. The equal-split fixture has4 UNIQUE midpoints,all
blocked; duplicating them gives a false fake8>5, exactly the rejected
counterfactual. The r3 cross fixture has4 distinct blockers and TWO
free choice pairs at the SAME coordinate2; no false global-coordinate
uniqueness assertion is imposed. The h9 balanced fixture blocks1,
accepts2 and preserves17/15 with A=(0,2,3,6,9),B=(1,4,8).
No extra window, fixture repair, existence solver or new E28 partition.

CPU0.124796s,peak RSS17,780,736bytes,within5CPU sec/64MiB. Source
tests/probes/instinct/path_forest_subdivision_charging.py;
prereg39c400a5. Immutable artifact
cited/instinct/b116-subdivision-charging-e3dc34d3f8902629.json,
342099bytes,SHA256 e3dc34d3f89026290697606bcce6773cc22ef582ff9dc2f20b364d11d3486b28.
Upload digest and manifest receipts verified. No failed prediction,
expanded domain or independent proof verification. MI252 remains
PROOF-SKETCH, its generic N6 admission conditional on MI245. Full
N6/E28/L8 remains OPEN.

**A concrete capacity boundary, by hand after the registered run.**
Target(1,3,4,4,4,4),h11,p21/q19 fits loads9/11. Its chosen merged
parent(4,4,4,4,4) needs a load at least12,so has NO two-bin capacity11.
Yet target A=(0,4,8,11),B=(1,5,9,10) is disjoint with exactly21/19.
Thus the merged-capacity hypothesis of MI252 cannot be replaced by
target capacity. This is a scope counterexample and an explicit target
witness, not an expanded diagnostic. It points toward FOUR repeated
s-gaps plus two unequal smaller a,b with a+b=s, with the two small
terminals separated. Next read MI177/214/220 before working that
selector; their complementary-residue/terminal scopes may already
cover part of it. No general theorem is inferred from this fixture.

**Niggle sweep / early90-minute reflection.** Taken slightly before
MI245's90-minute reflection interval expires. The blocked count is
about edge/choice pairs; repeated FREE coordinates are permitted.
Direct geometry/bag checks do not invoke the charging conclusion.
The complete set has labelled colours, deliberately counting swapped
chains separately; its ternary control verifies the domain independently.
No N5 existence candidate is smuggled into this supplied-parent test.

Enjoyable: the counting argument turned a failed insertion shortcut
into a reusable geometric mechanism. Frustration: the main criterion
still has provisional existence dependencies. Without the investment
already made, I would choose the complementary-small-terminal capacity
question now: the explicit fit/no-parent split makes it a concrete
missing inference. Repeating diagnostics at a larger window would not
resolve that inference. Choose the HAND selector next, after record
search, rather than a wider census or another dependency-audit entry.

Gut: satisfaction with the complete small check and a warm pull toward
the capacity obstruction. Reasoned: keep MI252's status unchanged;
the next task is to remove one actual admission restriction in a named
family, not accumulate reassuring instances. MI238 remains the sole
carrying priority. Completion READ-LEDGER only; no routine review halt,
new review queue or experiment opened. Research13min continues.


### MI255 — B117: complementary small terminals close the parent-capacity gap (2026-10-17 07:13 BST)

**Pull/question.** Can the target fit when its merged equal-gap parent
does not, with a direct construction? Yes: failure of parent capacity
forces equal repeated counts and separates the small terminals. This
supplies the missing geometry instead of assuming the merge is harmless.
The argument works uniformly for any EVEN repeated count, so record
that mechanism once rather than generate successive count variants.
Record searched: complementary.*small|small.*terminal|
four.*repeat.*two.*except|a\+b=s ->29 paragraphs/9 files;
even.*repeat.*complement|two.*small.*except|m.?s\+b|2m\+1.*s
->44 paragraphs/18 files. Relevant MI175/177/214/220/252/254 read,
including their actual scopes. MI177 needs merged capacity; MI214/220
assume both exceptional gaps>=s. None supplies this forced SMALL-terminal
branch. No novelty claim, new experiment or independently verified proof.

**Class criterion, COMPOSITE PROOF-SKETCH.** Let m>=1 and positive
integers a<b with a+b=s (so s>=3). Negative halves are2m copies of s
plus a,b, total K=(2m+1)s. At M=2(h+1), with positive odd p,q summing
2K, a folded-distinct cycle exists IFF

    max(p,q)<=2h-1, not both2h-1, and h>=ms+b.

The large-window branch uses PROVED MI175 plus the UNREVIEWED geometric
lemma MI252. The new forced branch below is direct and independent of
MI245's full N5 candidate, MI214/220 and MI252. For m2 this is exactly
the six-gap capacity family left at MI254. Full N6/E28/L8 is not claimed.

**Necessity / exact capacity minimum.** Every two-positive-odd cycle has
two monotone parity runs, so its negative halves split into two loads
at most h. A bin containing m+1 repeated gaps already has load
(m+1)s>ms+b. If both bins contain at most m repeats, each must contain
exactly m, and the bin receiving b has load at least ms+b. Thus the
minimum possible larger load is ms+b, attained by separate bins with
m repeats plus b, and m repeats plus a. The legal odd bound and exclusion
of the doubled longest odd edge are the standing necessary conditions;
in the chain encoding two maximum odd joins would force a shared maximum.
They imply K<=2h-2. Since K>=3(2m+1), h>=3m+3, so h+1>=2m+4:
enough labels for all vertices is automatic, not a missing hypothesis.

**1. Parent capacity available: h>=(m+1)s.** The merged parent has
2m+1 copies of s, with feasible loads(m+1)s,ms and common divisor s>=3.
PROVED MI175 supplies a folded-distinct parent with the original p,q.
It has N=2m+1 gaps, ALL r=N equal s. MI252 applies because2r>N and
a!=b: subdivide one free occurrence, retaining exactly p,q and their
owners. This proves the branch conditional only on MI252 SKETCH, not
the general five-gap existence conjecture. MI177 also addresses this
atomic-capacity regime, but is not silently treated as verified.

**2. Parent capacity fails: ms+b<=h<(m+1)s.** No bin can take m+1
repeats, so there must be m per bin; placing a,b together would create
(m+1)s and fail. Their separation is FORCED, with loads

    L=ms+b, S=ms+a, delta=b-a,
    H=h-L>=0, J=h-S=H+delta, T=H+J=2h-K>=2.

Here H<a and1<=delta<s. Write P=max(p,q),Q=min and
alpha=(2h+1-P)/2; then1<=alpha<=H+floor((delta+1)/2).
In this forced regime, delta1 implies a>=2. Otherwise a1,b2,s3,
H<a would give H0,T1, excluded by the legal/non-doubled positives.
This is the exact reason the small-terminal corner cannot obstruct
this branch; it is not being assumed away without a capacity argument.

If alpha<=2H, let c be the largest odd integer<=alpha. Take z1 unless
delta1, when take z-1. Set x=(c-z)/2,y=(c+z)/2. Since c<=2H-1,
both roots fit0..H and hence0..J. They are nonnegative since c>=1.
For z1 one has -a<z<b and z!=delta; for z-1 use a>=2 to get the
same strict interval and terminal inequality. Both offsets are nonzero
modulo s.

If alpha>2H, delta>=2: delta1 would imply H0,T1. Choose
c=alpha,x=H,y=alpha-H,z=alpha-2H. Then

    1<=z<=floor((delta+1)/2)-H<delta<s,

so z is nonzero modulo s and lies strictly in(-a,b), different from
delta. Also y=alpha-H<=floor((delta+1)/2)<=delta<=J, so it fits.
No residue correction or unproved ordering search is used in this branch.

**3. Direct collision and owner check.** Construct

    A=x+(0,s,...,ms,ms+b),
    B=y+(0,s,...,ms,ms+a).

The repeated ladders have distinct residues modulo s. Both terminals
lie strictly above BOTH ladders exactly when -a<z<b, already checked.
They coincide only if z=delta, excluded. Thus all2m+4 indices are
distinct in0..h. With c=alpha their original joins are P,Q. With
c=alpha-1 they are intermediate P+2,Q-2; reflect/reverse BOTH chains
in h. Their new minimum sum is T+1-alpha, giving original Q first,
P second. Every negative gap and its count is preserved. This completes
the direct forced branch; the whole criterion retains its stated
MI252 dependency in the other branch and is not independently verified.

**Hand branch controls, no program or new diagnostic.**
- m2,s4,a1,b3,h11,21/19: H0,delta2,alpha1 gives
  A=(0,4,8,11),B=(1,5,9,10),exact21/19. This repairs MI254's
  explicit target-fit/parent-fail example.
- m2,s5,a2,b3,h14,25/25: H1,delta1,alpha2 chooses c1,z-1.
  Pre A=(1,6,11,14),B=(0,5,10,12) gives27/23. Reflection yields
  A=(0,3,8,13),B=(2,4,9,14),exact25/25 and the same gaps.
- m2,s7,a1,b6,h20,35/35: H0,delta5,alpha3 gives
  A=(0,7,14,20),B=(3,10,17,18),disjoint and exact35/35.
- m1,s4,a1,b3,h7,13/11: A=(0,4,7),B=(1,5,6) checks the
  count parameter outside m2, without changing any root argument.
- m2,s3,a1,b2,h9,17/13 belongs to the parent-available branch.
  Parent A=(0,3,6,9),B=(1,4,7) has five3-gaps; insert free2 in A.
  The original17/13 remains exact. Thus the excluded SMALL-terminal
  corner of the forced proof is covered once parent capacity returns.
- Unexpected boundary: m2,s3,a1,b2,h8 has T1. Its only individually
  bounded positive pair15/15 is the forbidden doubled maximum. Treating
  it as a forced-case admission would invalidate the delta1,a1 argument.

**Niggle sweep / verdict.** The capacity minimum was proved over ALL
splits, not presumed balanced. Forced separation follows only below
(m+1)s; the other branch uses a real common-divisor parent. Negative
offset z-1 needs a>=2, which follows from the excluded T1 corner.
Strict terminal inequalities check cross-ladder collisions independently
of ladder residues; terminal coincidence is checked separately. The
reflected owner check uses the ORIGINAL p,q, never its intermediate pair.
No arbitrary N5 sufficiency or an experimental success is a premise.

Gut: satisfaction that the parent-capacity obstruction supplies a
construction instead of a dead end. Reasoned: a class with two SMALL
complementary exceptions now has a complete criterion candidate, using
only the simple subdivision lemma and a verified common-divisor result
outside the direct forced case. Next preregister a bounded forced-window
diagnostic across several even counts, plus parent-available and doubled-
maximum controls. No experiment opened here. MI238 remains the one
carrying priority; READ-LEDGER only, no new queue or routine halt.
Full N6/E28/L8 remains OPEN;research13min continues.


### MI256 — B118 preregistration: forced small terminals and exact endpoint collisions (2026-10-17 07:26 BST)

**Question/pull.** Test MI255's new direct forced branch, including its
capacity minimum and original-owner reflection. Record searched:
complementary.*terminal|forced.*small.terminal|even.*repeated.*small
->6 paragraphs/3 files; MI255 and existing geometry/bag validators read.
The pull sharpened while preparing the check: forced capacity gives
an exact collision description, not only a sufficient safe interval.

**Additional hand inference BEFORE experiment, SKETCH.** In the forced
branch H=h-(ms+b)<a, J=H+b-a<b. EVERY feasible z in[-H,J] is therefore
strictly in(-a,b). Both terminals lie above both ladders, and |z|<s.
The ladders meet iff z0 (the only multiple of s in that interval), and
the terminals meet iff z=b-a=delta. Thus the fixed terminal-order
layout's ENTIRE bad-offset set is exactly{0,delta}. This resembles
MI220's capacity-forced simplification but concerns the SMALL-terminal
case. It needs no general N5 candidate. The experiment below tests it
independently; no computation supplies its infinite quantifier.

**Predictions BEFORE implementation/run.** m1..3,s3..7,EVERY integer
1<=a<b with a+b=s, and EVERY h=ms+b..(m+1)s-1. Exactly42 profiles,
14 for each m. On EACH profile, independently enumerate all labelled
target bin masks and ALL merged-parent masks. Predict target min larger
load ms+b, parent minimum(m+1)s, target capacity present/parent absent.
Every fitting target split has m repeats per bin and separates a,b.
Bitset reachable loads must agree with the target mask set. Exactly
4704 target masks+2352 parent masks=7056 capacity cases.

For ALL legal unordered positive odd p<=q with p+q=2(2m+1)s,
max<=2h-1,not both2h-1, run MI255's EXPLICIT root selector. Predict
exactly69 formulas:33 broad-root/36 thin-root,21 negative offsets and
15 reflections. All original move bags/ordered positive owners/windows,
disjoint indices and BOTH physical geometry tests must pass. Compare
all69 root-sum interval sets against direct root rectangles and parity
recovery. These checks cover4/6/8 negative gaps, not just the N6 count.

Independently inspect every feasible offset of the FIXED terminal-order
chains on ALL42 profiles. Predict exactly168 offset cases, collision
iff z in{0,delta}, by index intersection and both physical validators.
Include the9 profiles with T1 and no legal positive pair: their two
offsets are both blocked. The constructor must reject their sole
bounded pair p=q=K=2h-1 as doubled maximum. No all-order nonexistence
or new target census is inferred from these fixed-order offset maps.

Add exactly TWO supplied-parent positive controls for the other branch:
m2,s3,a1/b2,h9,17/13,parent A=(0,3,6,9),B=(1,4,7),insert2 in A;
m3,s4,a1/b3,h16,31/25,parent A=(0,4,8,12,16),B=(1,5,9,13),
insert3 in A. Validate both parents and children literally, including
original positive owners. These are explicit witnesses, not runs of
an N5 existence algorithm. Total71 child formulas,zero E28 partitions.

Counterfactual: on m2,s5,a2/b3,h14,p=q25 omit reflection. Geometry
still passes but pre-joins27/23 must fail the original25/25 bag check.
Unexpected control: the9 T1 profiles have ordinary target capacity but
NO accepted positive pair; neither a capacity PASS nor two endpoints
in the root rectangle licenses their excluded doubled maximum.
Caps100 child formulas/10000 mask,offset and root cases,3CPU sec/64MiB.
Stop any mismatch/cap,retain failure,no repaired prediction or wider
grid. MI255/252 remain SKETCH;MI238 sole carrying priority,
completion READ-LEDGER only,no routine review halt.


### MI257 — CL430 received: stop the case tree, retain its dependencies (2026-10-17 07:36 BST)

Verified abaa8ffa and read CL430 in full, including the two new script sources.
Cloud explicitly did NOT read MI238. Its ACK means receipt, not verification;
the carrying request is retired, with no status upgrade. Its reported14,210
new questions/zero mismatches are Cloud's computation, not a local replay.
B118/MI256/source86595b93 remains PREREGISTERED BUT UNRUN: remote changed
before its push, and CL430 changes the plan. No result or artifact is implied.
No further N6 families or extensions of the N5 case tree are planned.

MI245's final dependency table, all unreviewed unless stated:

| N5 row | Carrying record |
|---|---|
| nonisolatable, unequal short pair | MI238 |
| nonisolatable, equal short pair, large middle | MI234/236, MI230 |
| nonisolatable, equal short pair, small middle | MI240/242 |
| isolated largest, rich four companions | MI244 root selection + MI246 prefix step |
| isolated largest, three equal companions | MI244 + MI206; units audited MI248 |
| isolated largest, four constant companions | MI247; small unit boundary uses PROVED MI180 |

MI243 composes the first three rows; MI245 composes the two sides.
This is a retained COMPOSITE PROOF-SKETCH, not a proof and not a new
review job. Earlier dependencies remain visible in their original entries.
MI252 subdivision and MI255 remain separate SKETCHes, not a way to
promote MI245. General N, E28 and L8 remain OPEN.

Fresh-choice reflection: enjoyment returns with a uniform question;
unease and disappointment concern the case-tree momentum. Without the
investment I would choose the general criterion, not another terminal
family. Cloud's diagnosis is persuasive on mathematical scale and review
cost; no automatic permission or veto is being invoked. The next bounded
question tests the strict Grasshopper selector, not another existence class.

### MI258 — B119 preregistration: can the strict Grasshopper count be necessary? (2026-10-17 07:36 BST)

Question: is CL430's literal distinct-chain/forbidden-count certificate
strong enough to capture even a small gcd1 six-gap placement? Record
searched: Grasshopper|grasshopper ->8 paragraphs/4 files, MI208/209 and
PRIOR-ART read; uniform.*criterion|distinct.*split|forbidden.*count|wall.limit
->71 paragraphs/22 files, relevant current MI198/208 and CL430 read.
Official IMO2009 Shortlist C7 Variant2 statement reread: r distinct
positive jumps avoid at most r-1 forbidden proper-prefix levels. This is
SUFFICIENT, with no converse in the source. No repeated-jump extension.

Hand prediction BEFORE experiment: M20,h9,d=(2,2,2,2,3,3),p13/q15
passes ordinary capacity7/7 and legal bounds. Any distinct A has at most
one2/one3. Its complement fits h9 only when A has BOTH, giving loads5/9.
B has the four orders of (2,2,2,3), root0. For positive13, A root3;
for15,A root2. This exhausts both positive owners and every feasible root.
At root2 all four B orders collide with an A endpoint. At root3 one
order collides with an endpoint and three have TWO forbidden interior
levels. A has two jumps, so its theorem allowance is only ONE.
Predict zero strict Grasshopper admissions after ALL these choices.

Nevertheless A=(3,6,8),B=(0,2,4,7,9) is a literal placement with original
13/15. Prediction: among all16 choices of two A orders/four B orders/two
owners there are exactly4 valid geometries. Thus the strict count is
not necessary even when a DISTINCT chain itself suffices. This limits
one proposed selector, not Grasshopper, the general criterion or Cloud's
broader suggestion to study repeated-gap avoidance. No assertion that
Cloud claimed necessity, no board/status change.

Independent controls:64 labelled masks versus multiplicity capacity,
Cartesian root rectangles versus root interval, both physical geometry
validators and exact original move bags. Predict8 labelled distinct fits,
equivalent to one multiset split;8 root/order rows,3 endpoint-safe rows.
Positive theorem control: M30,d1..6,p=q21,A-root4,A-gaps1..4,
B=(0,5,11) has two proper obstacles versus allowance3; at least one
A permutation must succeed. Counterfactual: correct-bag A=(3,6,8),
B=(0,2,4,6,9) must fail folded geometry. Repeated-step control:
A-jumps(2,2),root0,B singleton2 has one obstacle but cannot avoid it;
dropping distinctness would falsely certify. Unexpected check is the
main miss's distinct-chain success despite too many counted obstacles.

Cap1CPU sec/64MiB/200 cases; stop on any mismatch and retain it. Source
path_forest_grasshopper_selector_limit.py. No wider grid after this
sharp test; no E28 partitions or review request. Source written before
run; earlier source-edit corrections checked window/endpoint controls
before any execution. Next write the general chain criterion and the
single remaining sufficiency gap; return attention to actual multi-piece
placement rather than patch the selector by family. Research13min active.


### MI259 — B119 outcome: the strict obstacle count misses a distinct-chain solution (2026-10-17 07:38 BST)

COMPUTED, single-worker, prereg682d0e6e. All64 labelled splits checked;
8 fitting distinct-side masks represent exactly the multiset split
(2,3)|(2,2,2,3). The8 owner/root/B-order rows have3 endpoint-safe
candidates, each with TWO interior obstacles against allowance ONE.
Strict Grasshopper admissions0. Among the16 actual A-order candidates,
exactly4 pass both geometry engines and original move bags/owners.
The M30 positive theorem control has10 successful orders; the repeated-
hypothesis and correct-bag/collision counterfactuals both reject as required.
CPU0.001193sec, peakRSS15380480bytes, all caps respected, no wider grid.
No E28 partitions, existence census or independent proof review occurred.

The complete tiny hand table makes the limitation inspectable without data.
A has gaps2,3,load5; B has gaps2,2,2,3,load9 and root0.
For positive15 A root2, all four orders meet an A endpoint.
For positive13 A root3, endpoint pair3/8 gives:

| B prefixes | endpoint issue | forbidden A proper levels | successful first A jump |
|---|---|---|---|
|0,2,4,6,9|none|1,3|2|
|0,2,4,7,9|none|1,4|2 or3|
|0,2,5,7,9|none|2,4|3|
|0,3,5,7,9|start3|2,4|none|

Explicit A=(3,6,8),B=(0,2,4,7,9) has physical vertices
(6,19,15,11,5,1,16,12), moves(13,-4,-4,-6,-4,15,-4,-6),
folded labels(6,0,4,8,5,1,3,7), all distinct. Thus a miss of the
strict count need not even be a repeated-A obstruction. No converse
for Grasshopper was asserted by Cloud; this is a reach limitation of
the proposed direct sufficient-certificate selector, not a theorem refutation.

Raw output is retained outside git as b119-selector-limit.json,3635bytes,
SHA256 acbe4129a0d8f976c4aadc2f32a80aa5a369e5be83351b7b7393d2ca1c3fdbdb.
Automatic approval review REJECTED the immutable shared-store upload,
stating that this specific artifact payload needs explicit authorization.
No upload or manifest append occurred; no retry/workaround. The raw file
remains local; source, predictions, small hand table and measured outcome
are committed. Normal authorized flag receipts are separate and succeeded.
This is an evidence-delivery limitation, not a failed mathematical check.

Niggle sweep: endpoints checked separately from proper prefixes; all distinct
subsets exhausted by capacity, not an arbitrary chosen split; BOTH positive
owners and every root included; actual successful A is distinct; bounds of
the positive control corrected BEFORE execution. No geometric success is
silently read as a proof of the general criterion. Gut: relief at a small
answer and renewed pull to the uniform obstruction, with no urge to patch
this into another family. Reasoned: count-only application is insufficient;
the original prefix sets contain structure the theorem's count discards.

### MI260 — The single-component statement, and where its proof stops (2026-10-17 07:38 BST)

**CONJECTURE CP, general N, not a theorem.** Let h>=2, N>=1, and
D=(d_1,...,d_N) be positive integers with K=sum D. Let p,q be positive
odd integers with p+q=2K. There is a folded-distinct cycle on positions
0..2h+1 with move multiset(p,q,-2d_1,...,-2d_N) iff:

1. max(p,q)<=2h-1;
2. not(p=q=2h-1);
3. N+2<=h+1;
4. D splits into two loads at most h.

These four requirements are necessary in the two-monotone-chain encoding
(MI180, independently verified). Maximum odd step2h+1 would join equal
folded labels; the doubled2h-1 case forces both chain maxima to h;
label count and run loads give the other requirements. Finite agreement
and the N5 composite are evidence, not the missing general sufficiency.

**Exact target of a uniform proof.** Choose a multiset split D=U+V,
loads a,b, and P in{p,q}. Put alpha=(2h+1-P)/2. For a permutation of
V let V* be all its prefix sums INCLUDING0 and b. A root x for U must
lie in the integer interval

    max(0,alpha-h+b) <= x <= min(h-a,alpha),
    y=alpha-x, z=y-x=alpha-2x.

Choose a permutation of U with full prefix set U*. The sole collision
condition is

    U* intersect (z+V*) is empty.

Then A=x+U*,B=y+V* fit0..h, and the original joins are
P=2h+1-2(x+y), Q=2(x+y+K)-(2h+1). Conversely any desired cycle gives
such chains, a split, orders and a choice of the even-start positive.
An empty gap list is allowed: its prefix set is{0}, not the empty set.
The statement incorporates endpoint collisions, all roots, both positive
owners and actual multiplicities; none may be discarded in sufficiency.

The missing inference is ONE existential implication: the four scalar
conditions ensure some split, root and two orders with that disjointness.
Known Grasshopper solves distinct U against at most|U|-1 proper obstacles
AFTER endpoint safety, but MI259 shows that this numeric admission cannot
cover all feasible questions. Replacing that count by arbitrary obstacle
avoidance would merely restate the missing inference. MI204/206 offer
special structure, not an authorized general repeated-jump theorem.
No further exception tree or carrying review is opened here.

**Return to the actual target.** Even CP would concern ONE component.
E28 requires a joint allocation and simultaneous folded-label packing of
all components, with reserved anchors removed. MI158/160 were reread:
of the four original FIRST-policy misses, one requires merging a primitive
six-cycle with its cancelling pair; three require changed reserved labels,
not further within-component ordering. All2000 old sample partitions are
already checked, so another larger sample would not answer this issue.
Next cheap mathematical step: use those existing allocation obstructions
to state the joint-placement target and identify which constraint changes
when the reserved block moves. Do not claim CP alone closes it, reopen
primitive-only splitting, or run another component-family diagnostic.
Research13min remains active; no routine halt or new review queue.


### MI261 — B120: exchange one token per PAIR, not per bin (2026-10-17 07:43 BST)

**Pull before the test.** The original three anchor failures excluded one
selected token per active bin. Two of the bins actually hold TWO pairs.
Why insist that those bins adjust their sums through a single displacement?
This is a warmer question than another component family: test whether the
anchor changes were necessary, or merely repaired an artificial restriction.

Record searched: multi.token|two.selected|Euler.*orient|balanced.*orient|
one.selected.token ->12 hits/6 files; MI154/158/160 and MI161/162 read.
selected.*per.pair|per.pair.*exchange|even.degree.*bin|multi.*selected.*token|
two.tokens.*bin ->one unrelated old-ledger paragraph. This is not an absence
claim. Prior art: known Eulerian-circuit/even-degree theorem and its orientation
argument read in the official university lecture notes, filed in PRIOR-ART.
No review requested for that known theorem or this representation sketch.

**Exact representation SKETCH, not an existence proof.** Fix reserved labels
R, their singleton anchors a_i, and pair-slot counts h_i. Suppose the remaining
tokens already have a partition into bins of sizes2h_i with desired sums.
Make a multigraph whose vertices are bins; each unreserved complementary pair
is an edge joining its two final owners. A pair contained in one bin is a loop.
Every bin has degree2h_i. Orient closed unused-edge walks in each component;
loops contribute one incoming and one outgoing edge. Thus bin i has h_i edges
out and h_i in. This is the known Eulerian orientation argument, with parallel
edges and loops retained, not a new theorem of graph theory.

Assign each complementary pair initially to its directed tail bin. Keep there
the endpoint whose FINAL owner is that tail, and select the other endpoint to
send to the head; for a loop either endpoint can be selected and retained.
Every bin initially owns h_i whole pairs, sends h_i selected endpoints and
receives h_i endpoints. Match its outgoing positions to its incoming positions
by any bijection. Across bins these matches form a PERMUTATION of exactly ONE
selected physical position from EACH unreserved complementary pair. For each
bin the sum of its h_i displacements is

    e_i=(t_i-a_i-56h_i)/2.

Conversely, choose one position from each unreserved pair, group them into
h_i positions per bin, and choose a permutation whose grouped displacement
sums are e_i. Start bin i with its h_i whole pairs and anchor; replace its
selected positions by their images. All selected images are a permutation,
so the full token inventory is preserved. Each bin has exactly2h_i nonanchor
tokens and the required sum. Pair uniqueness prevents receiving a token equal
to one of its retained complements. This gives the original partition.

Hence the multi-token permutation model is EXACT for fixed anchors and h,
whereas the previous one-token-per-active-bin model is only sufficient.
Zero-displacement clones and bins with net zero but nonzero exchanges must
remain allowed. This reformulates existence; it does not prove it or supply
a constructive way to choose the permutation from target sums. Its immediate
value is a fair test of whether the old obstructions survive the exact model.

**Preregistered diagnostic BEFORE run.** Exactly the three MI158 geometric
misses, ranks16461642,6321549,2079026. Keep the ORIGINAL FIRST anchors R0,
ascending ownership and greedy h unchanged. No new targets or anchor/slot
policy. Blind prediction: ALL THREE have ordinary partitions with those
same cardinalities/anchors, and admit the above multi-token certificates.
If so, at least one bin in each certificate must use two nonzero exchanges;
otherwise it would be an old one-token certificate, already excluded.
No prediction of node count or exact number of partitions; stop at first.

Generate every size2/4 subset of the unreserved physical positions with
the required bin sum; compare candidate masks to independent recursive
increasing-subset/sum generation. Exact-cover MRV search, complete unless
capped, returns first partition. Both independent literal inventory/sum/
cardinality validators must pass. Convert the partition to Eulerian pair
orientation and clone permutation; reconstruct the EXACT same bins and check
every grouped displacement against ORIGINAL e_i. This conversion is not
allowed to change anchors or choose a different h. Controls: disconnected
parallel-edge-plus-loop graph, all-loop/fixed-point graph, reused pair and
nonpermutation rejection. Unexpected control: leaving the singleton anchors
in the Euler graph gives ODD degrees and must be refused; removing anchors
is a mathematical prerequisite, not formatting.

Caps3 fixed targets,200k nodes/target,500k overall,5CPU sec/128MiB. Any
cap stops partial/UNKNOWN; any false control stops with failure retained.
A NO_WITNESS refutes the blind prediction for this fixed allocation only;
no raised cap, new policy, repaired prediction, new sample or old-model
rerun. Source path_forest_multi_token_exchange.py. Raw remains local while
specific shared-store artifact approval is pending; no upload attempt.
Gut: a live pull at the freedom omitted from the model. Reasoned: this tests
an actual restriction on JOINT placement, rather than refining a one-component
lemma. General E28/L8 and CP remain OPEN; research13min active.


### MI262 — B120 result: all three original anchor allocations work with multiple exchanges (2026-10-17 07:46 BST)

**COMPUTED, fixed three targets, no new sample.** Prereg93a4065a.
All three have literal partitions retaining ORIGINAL FIRST anchors AND
original greedy slots. Each needed9 exact-cover nodes,27 total. All candidate
sets agree with independent recursive subset generation; both full token/bin
validators, Euler degree checks, grouped displacements, exact reconstruction
and all controls pass. CPU0.011018sec,peakRSS15532032bytes. No cap, restart,
extra target, changed policy, old-model rerun or universal existence claim.

| rank | h2 bins (zero-based) | aggregate moves replaced by clone moves |
|---:|---|---|
|16461642|2,3|-17=-11-6; -17=-4-13|
|6321549|2,3|-20=-13-7; -7=-3-4|
|2079026|2,5,6|-21=-15-6; 2=2+0; 4=3+1|

The other bins retain a single move. Degree-balanced orientation selects one
physical endpoint of every unreserved pair, assigns h_i outgoing endpoints
to bin i, and its clone permutation recreates each partition exactly. The
raw certificate stores all orientations, physical selected endpoints and
permutations. Known Euler theory is credited; the general representation
argument of MI261 remains single-party SKETCH, not independently reviewed.
These finite partitions pass without relying on that infinite argument.

For complete inspectable witnesses, bins are in the original target order:

- rank16461642: (1,29,47);(3,31,43);(5,9,11,23,35);(7,13,15,17,33);
  (19,39,49);(21,45,51);(25,41,53);(27,37,55).
- rank6321549: (1,23,47);(3,25,45);(5,9,11,19,33);(7,13,21,29,35);
  (15,43,49);(17,41,51);(31,37,53);(27,39,55).
- rank2079026: (1,19,49);(3,21,45);(5,7,9,17,37);(13,39,51);
  (11,47,53);(15,25,35,41);(27,29,31,33);(23,43,55).

Raw b120-multi-token.json is local outside git,4092bytes,SHA256
2af5e5ce314c5c170afcec67457b405467d7864373fa4c225d9260936ab1dc57.
No shared-store upload attempted while specific artifact approval remains
pending. No cited-path/manifest receipt claimed; the compact witnesses,
source and preregistration are public in git. The three targets already
had B69 partitions with other anchors, so this is NOT three new target
successes added to the old2000 sample. What changed is the certificate
model and the necessity of anchor changes on these examples.

**Niggle sweep, cheap HAND guard, no new experiment or proof queue.** Could
one infer that original FIRST anchors always suffice once exchanges are
unrestricted? No. For t=(97,97,97,97,99,99,99,99),sum784,q8, the first
reserved block gives anchors(1,3,5,7,49,51,53,55), free tokens9,11,...,47
and h=(2,2,1,1,1,1,1,1). Bins2/3 require pairs summing92/90. Their
ONLY possible pairs are{45,47}/{43,47}, which share47. Thus this fixed
allocation has no partition at all. Even changing h with every h_i>=1
cannot rescue it: anchors1/3 leave residual96/94, above maximum pair sum92,
forcing h0,h1>=2; these use both extra pairs. This guard stays one paragraph,
no probe or PROOFS entry. Record searched97.*97.*97.*97.*99|multi.token|
Eulerian.*pair ->6 current-method paragraphs/2 files, no older exact tuple
found in this bounded search. No novelty or full target impossibility claim.
The target can still use different reserved pairs/anchor ownership/cardinalities.

**Fresh verdict / next mathematical obstruction.** Delight that the old -20/-21
walls disappear under an elementary extra freedom, and a warm pull toward
joint allocation. The search found each witness on its first full descent;
that is evidence of easy THESE three instances, not a general complexity
claim. The guard identifies a real remaining obstruction: two different bins
can compete for the same necessary token. A general single-component theorem
cannot solve that competition. With h_i in{1,2}, a direct joint construction
must choose disjoint pairs for the h1 bins AND assign the leftover tokens in
four-sets to the h2 bins; anchor selection changes both allowed sums and token
inventory. Next investigate that joint matching/allocation question, using the
explicit97/99 obstruction rather than another component-family tree or a
larger random sample. CP and E28/L8 remain OPEN. No routine review halt;
research13min active, one READ-LEDGER mentoring update at this model change.


### MI263 — B121: postpone anchors; reusable exact subset-sum columns (2026-10-17 07:58 BST)

**Pull / trajectory.** A uniform anchor-repair argument is already starting
to resemble another local policy tree. The warmer alternative is to postpone
anchors: construct actual bins jointly, without declaring some of their tokens
in advance. MI261's exact model exposed that freedom; there is no obligation
to keep its representation inside the solver. The bounded question is whether
a reusable catalogue makes the unrestricted finite problem tractable on the
five existing difficult fixtures, not a new census or a universal claim.

Record searched: rainbow.match|prescribed.*sum|pair.sum|perfect.*match.*sum|
odd.*magic|Heffter ->78 paragraphs/20 files; PRIOR-ART's prescribed-sum scope
and MI039-042 instrument read. subset.*catalog|catalog.*subset|
meet.in.the.middle|exact.cover.*odd|anchor.free ->no hits including ledgers.
No absence or novelty claim: exact cover, subset enumeration, meet-in-the-middle
and generating functions are standard methods. The earlier MI040 solver assigns
individual descending tokens to residual bins; this solver assigns COMPLETE
sum-certified bin subsets using an exact-cover token-and-bin column choice.
Both solve the original odd partition problem, not a sufficient cycle model.

**Representation / reusable compression.** Enumerate every subset of
{1,3,...,55} with sum<=122, allowing ALL cardinalities and no reserved anchors.
Group their28-bit masks by sum s. The count in bucket s must equal the
coefficient of z^s in product over j0..27 of(1+z^(2j+1)). A target chooses
one mask from each corresponding bucket, pairwise disjoint and covering all
28 tokens. This is exactly the target problem. The reusable objects are BIN
subsets, unlike MI150's target-specific whole component collections. Standard
exact-cover branching on any uncovered bin OR token is complete. Only failed
states are cached; state includes unused-bin target multiset and used tokens.
No arbitrary ordering, guessed cardinality or anchor condition is imported.

**Predictions BEFORE run.** One catalogue of ALL sums0..122 at m28. Blind
prediction <=500000 masks total, including empty subset in sum0. Independent
coefficient DP must agree for EVERY bucket; independent14+14 meet-in-the-middle
must reproduce the FULL mask set at each distinct sum in the five fixtures.
This tests the catalogue itself, not merely successful partitions.

Exactly these FIVE E28 targets, no others:
(97,97,97,97,99,99,99,99);
(77,77,83,85,107,117,119,119);
(71,73,77,105,107,109,121,121);
(69,69,75,103,111,116,120,121);
(90,90,91,91,93,103,111,115).
The last four are the original MI158 failures. Blind predictions: all five
certify and each uses fewer than1000 search nodes. All cardinalities remain
allowed; there is no FIRST-anchor requirement or h1/2 restriction. A solution
beyond1000 refutes that forecast even if it arrives under the hard cap.
No repeated timing or target order changes after results are seen.

**Independent/negative/unexpected controls.** Before the five, compare every
189 positive sorted three-target tuple of total m^2,m<=6 to MI040's independent
labelled-assignment oracle. Reuse the actual known lower witness
(67,67,67,67,102,102,102,102) with26 tokens: must be NO_WITNESS, not a cap.
Also(3,3,3) at m3 must fail despite individual subsets existing. Every positive
has exact odd inventory/sums under two validators; corruption and inventory-
preserving unequal-token swap must reject. Unexpected: the97/99 tuple must
succeed WITHOUT imposing the fixed anchors known to obstruct it. Success
of each subset alone cannot substitute for disjoint full coverage.

**Hard caps/stop.**50000 nodes per target (controls included),1M nodes total,
1M catalogue masks,2M reference joins,15CPU sec/256MiB. On any cap retain
partial/UNKNOWN and stop; no raised cap, new target, broad sample, census,
new component family, follow-on experiment or review job. Source
path_forest_subset_catalogue.py. Raw remains local pending artifact upload
authorization; no upload attempt. Catalogue size, finite witnesses and node
counts can justify or reject this computational representation, not establish
full E28/L8 or any asymptotic running-time bound. Research13min active.


### MI264 — B121 result: a small exact catalogue and a seven-token buffer (2026-10-17 08:00 BST)

**COMPUTED, fixed five fixtures, all cardinalities.** Prereg147643ad.
The full0..122 catalogue contains129658 masks, including the empty subset.
All123 generating-function coefficient counts agree; ALL23 queried sum buckets
match complete independent14+14 mask generation (60723 reference joins).
All189 small three-bin questions agree with the independent labelled-assignment
oracle. Both the3/3/3 global conflict and published26-token67/102 lower witness
return NO_WITNESS, not UNKNOWN. All five E28 fixtures return full literal
partitions; both inventory/sum validators and both corruption controls pass.
Fixture nodes9,9,9,27,9, total63; total including controls566. CPU0.406685sec,
peakRSS24842240bytes. All blind predictions pass, no cap or widened run.

| target (abbreviated by first entries) | actual cardinalities |
|---|---|
|97,97,97,97,99,99,99,99|7,3,3,3,3,3,3,3|
|77,77,83,85,107,117,119,119|7,3,3,3,3,3,3,3|
|71,73,77,105,107,109,121,121|7,3,3,3,3,3,3,3|
|69,69,75,103,111,116,120,121|5,3,3,3,3,4,4,3|
|90,90,91,91,93,103,111,115|6,4,3,3,3,3,3,3|

The new97/99 obstruction has the following direct witness, in target order:
(1,3,5,7,9,17,55);(11,33,53);(15,31,51);(19,29,49);
(21,35,43);(23,37,39);(13,41,45);(25,27,47).
Every odd1..55 appears exactly once. There is no chosen anchor block or
single-token geometry to repair. The seven-token bin absorbs four tokens
beyond the minimum three, leaving seven higher-token triples. The first
three fixtures ALL choose this pattern; the last uses a six-token even bin.
No inference that these particular cardinalities are necessary is made.

Raw b121-subset-catalogue.json,1893bytes,SHA256
964133f42e2271d7eba8e0dbbac3dfc203c2b0fa64757dc9b582e8463a0b6b29,
is retained locally outside git. No shared upload attempted while artifact
authorization remains pending; no cited/manifest receipt claimed. Raw records
all five witnesses and per-sum counts, not the129658 regenerated masks.
The source reconstructs and independently tests the catalogue. This is not
a new sample, census, asymptotic complexity result, full E28 claim or external
verification. Existing overlapping target successes are not added to a tally.

**What the surprise teaches.** For the ALL-ODD E28 subdomain, each target
exceeds55, so each bin needs at least3 odd tokens; the total is28. There are
exactly four tokens above the minimum24, and every bin cardinality is odd.
Thus there are precisely TWO possible cardinality patterns:

    one7 + seven3, OR two5 + six3.

This is an elementary count, not a new theorem filing. The old h1/2 model
kept only two5+six3. One7+seven3 was a substantial freedom outside that
model, even after anchors were allowed to move. This does NOT contradict
MI157: its h1/2 conclusion was for its fixed FIRST-anchor greedy choice,
never for all partitions. These examples might also have two5 witnesses.

**Named next question, not a new experiment/assumption.** SB7: does every
sorted all-odd E28 tuple69<=t_i<=121,sum784 admit one7+seven3, with the
seven-token bin assigned to a smallest target? A positive answer would close
one entire parity domain directly, with no cycle family or prechosen anchors.
Only three fixtures support that pattern so far. The single-buffer restriction
may be false; if so retain the failure rather than manufacture repairs. The
unrestricted exact catalogue already allows both cardinality patterns.
Record searched seven.token|one.*seven.*bin|seven.*triple|cardinalit.*7 ->24
mostly unrelated paragraphs/10 files; no source theorem for SB7 found in that
bounded search. Primary literature on prescribed sums was already read; it
does NOT supply the simultaneous triple cardinality guarantee. No novelty claim.
Next orient on triple completion or a bounded kill test, not a full census.

**Niggle sweep / verdict.** Complete subset buckets, not just fixed-size bins;
true exact cover, not independent subset feasibility; unused token columns
remain constraints; failed-state cache retains used tokens and remaining
sum multiset; equal-target bin labels can be permuted only for FAILURE states.
Known impossible controls make the success gate falsifiable. Small catalogue
and five quick successes establish a usable instrument on this scope, not
uniform tractability. Gut: surprise and delight at the seven-token buffer,
a warmer pull than selecting anchor policies. Reasoned: the right unit of
reuse is an actual sum-certified bin, and the natural structural question is
now one-buffer/triple completion. General E28/L8 and SB7 remain OPEN. No
follow-on run, proof review or automatic census; research13min active.


### MI265 — B122: SB7 scalar screen and a bounded boundary kill (2026-10-17 08:11 BST)

**Question/pull.** Is the smallest-target seven-token buffer a robust whole-
parity construction, or did the three positive fixtures hide an obstruction?
The pull is warm, but the restriction must face its own kill test before
becoming an assumption. No further component tree or rolling target census.
Record searched triple.*complet|triples.*sum|three.partition|
equitable.*partition|balanced.*prescribed ->44 paragraphs/12 files, current
MI264 and old prescribed-sum scope relevant. Two bounded web searches for
partitioning consecutive integers into triples with prescribed sums found
no applicable variable-sum/cardinality theorem. New primary source2312.00089
abstract/intro/Thm2.3 STATEMENT read: common sums, arbitrary prescribed sizes;
not the variable triple sums and noninterval remainder here. Proof unread;
no import from it. Scope entry added to PRIOR-ART.

**Hand reduction before any run; no PROOFS entry.** For any subset of bins
with k tokens, its target sum must lie in[k^2,k(56-k)]. With the buffer
at bin0, subsets avoiding it consist of j triples,k=3j,j0..7. Their sums
are bounded by

    max(69j,784-121(8-j)) <= sum <= min(121j,784-69(8-j)).

These bounds imply the k-token inequalities for EVERY j. For the upper
side j1..7, the usable upper bounds are121,242,363,484,577,646,715;
the token maxima are159,300,423,528,615,684,735. The lower bound69j
alone is>=9j^2 for j<=7. Subsets containing the buffer are complements
of subsets of triples, and total784=28^2 turns their inequalities into
the same ones. Thus ALL scalar subset-cardinality bounds hold throughout
the SB7 domain, regardless of which bin is the buffer. This eliminates
that particular obstruction, not the true disjoint-triple problem.

Guard in one paragraph: scalar subset bounds are NOT a general partition
criterion. First8 odds and four pair bins with sums(10,10,22,22) satisfy
all subset bounds; the two10 pairs must be{1,9},{3,7}, blocking both
possible22 pairs{7,15},{9,13}. No four-pair partition exists. This will
be a negative instrument control, not a new proof/review job.

**Declared finite kill, predictions BEFORE run.** Domain union only:
(A) ALL two-valued sorted odd E28 tuples; exactly30, from r copies of
98-x and8-r copies of98+y with odd1<=x<=29,odd1<=y<=23,
r*x=(8-r)*y,r1..7. Independent literal(a,b,r) enumeration must agree.
(B) lexicographically smallest and largest feasible tuple for EACH
minimum a=69,71,...,97; fifteen minima/two extremes each, at most30
profiles. Deduplicate A union B; at most60 unique targets, no random
sample or work draw. Greedy lex minima choose the smallest odd entry
consistent with the remaining upper limit121; maxima choose the largest
odd entry consistent with a sorted completion and remaining sum.

Require exactly cardinalities7,3,3,3,3,3,3,3, buffer at the first/smallest
target; unrestricted full subset catalogue, no anchors. Blind prediction:
every declared profile has a witness. Any complete failure stops the run
immediately; do not scan the rest, try buffer elsewhere, or repair the rule.
An independently successful counterexample would reject SB7, not E28.

**Controls / independence.** Recreate the already validated129658-mask
catalogue with its full GF counts, and compare COMPLETE independent MITM
mask sets at EVERY queried sum plus10/22. Positive witnesses pass both
inventory/sum/cardinality engines and explicit7/3 cardinality checks. Use
the four-pair scalar-pass/partition-fail control above. Recheck known97/99
buffer witness and relabel its four equal-minimum bins: any may carry the
buffer with target sums preserved, so choosing the first tied minimum
loses no freedom. Deliberately asking for eight triples must reject the
wrong total cardinality24!=28, rather than quietly omit four tokens.
Duplicate-token corruption must reject. Unexpected check: verify all255
scalar subset inequalities on EVERY profile, even if true exact cover fails.

On a first primary NO_WITNESS, before claiming a refutation, independently
try EVERY seven-token buffer subset, and partition its complement by pivoting
its SMALLEST token and enumerating the two partners/owner target. This differs
from the primary bin-and-token MRV search. It shares only the catalogue whose
full queried masks were checked independently. Both searches share the declared
per-profile budget; a reference cap gives an unverified candidate/UNKNOWN,
not a checked counterexample. No outside second reader is implied.

Hard caps50000 search states/profile,500000 overall,1M catalogue masks,
2M reference joins,10CPU sec/128MiB. Caps stop partial/UNKNOWN without
restart or increase. Source path_forest_buffer_kill.py. Raw stays local while
artifact authorization is pending; no upload attempt. Passing this boundary
kill is not a full-domain proof or permission to enlarge it. Next return to
triple completion/literature or examine the first genuine counterexample.
General E28/L8 and SB7 remain OPEN until the declared evidence changes them.
Research13min active; no review queue opened.


### MI266 — B122 outcome:54 boundary profiles pass; the one-hole triple problem (2026-10-17 08:15 BST)

**COMPUTED bounded kill, not a proof.** Prereg48239734. All30 two-valued
profiles and30 extremal profiles produce54 distinct targets after6 overlaps.
ALL54 have a seven-token buffer at a smallest target and seven triples.
Total542 search nodes including controls; maximum15 on any declared profile.
All29 FULL queried MITM mask buckets match, all GF counts pass, and every
partition passes both independent literal engines and exact cardinalities.
All255 scalar subset inequalities hold on every target. The pair-control
(10,10,22,22) passes all its scalar bounds but correctly has no partition;
tied-minimum relabeling, wrong-total-cardinality and duplicate-token controls
all pass. CPU0.339239sec,peakRSS25325568bytes. No first failure, hence the
conditional independent negative-search engine was NOT exercised. No cap,
restart, domain expansion, random sample or next experiment.

First boundary target(69,69,69,93,121,121,121,121) has bins
(1,3,5,7,9,11,33);(13,15,41);(17,21,31);(19,23,51);
(25,43,53);(27,39,55);(29,45,47);(35,37,49).
The54-target result supports SB7 only on this explicit domain; it is not a
full all-odd E28 verdict and adds no overlapping global coverage tally.

Raw b122-buffer-kill.json,11710bytes,SHA256
1bfa55c0e20b397eedba14e34f954c171bdd3d5cf118afb22b79db925e5533c7,
remains local outside git. No shared upload attempted or manifest receipt
claimed while artifact authorization is pending. Source and declarations
reproduce the finite test; no external second reader is implied.

**Hand simplification AFTER the kill; SKETCH, not assumed sufficient.** Let
a=t0,necessarily odd69<=a<=97. A canonical seven-set of sum a is:

    if a<=91: C(a)={1,3,5,7,9,11,a-36};
    if a>=93: C(a)={1,3,5,7,9,a-80,55}.

All entries are distinct allowed odds. For a<=91 the remaining pool is
{13,15,...,55} minus the single odd a-36. For a>=93 it is
{11,13,...,53} minus the single odd a-80. Both are22 consecutive odds with
ONE missing, leaving21 tokens for seven triples. Finding ANY seven-set was
never the hard part; whether this PARTICULAR seven-set permits completion
is stronger than SB7 and remains untested. Descriptive inspection of existing
outputs only:11/54 witnesses use C(a);43 use a different seven-set. That does
NOT show the canonical choice fails, and does NOT verify it on those43.
Record searched one.hole.*interval|punctured.*interval|one.hole.*triple|
22.*consecutive|canonical.*buffer ->16 mostly unrelated paragraphs/9 files;
no earlier relevant triple-completion result found in that bounded search.

**Known-source bridge at a=91; PRIOR-ART application, not a new proof queue.**
C(91) removes1,3,5,7,9,11,55 and leaves13,15,...,53. Subtract12 from each
remaining token, giving the first21 odds1..41. For the remaining seven target
sums set u_i=t_i-36. They are odd,55<=u_i<=85, and sum441. The primary
Tan-Teh2312.10914v3 section2/Appendix A explicitly reports verification of
Conjecture2.7 for seven paths with minimum>=L6=46. Here each B21(u_i)=3
(u_i>41 and <=39+41+37=117), so total minimum-cardinality budget is21,
not impossibly burnable. Their verified seven-path result supplies an odd
partition; because all seven u_i are odd and exceed41, every bin uses at least
3 tokens, so all use EXACTLY3. Adding12 to each token then adds36 per triple,
recovering the desired t_i. Thus the a=91 slice follows from the published
computer-assisted seven-path result, including ties at91. This does not claim
a new elementary proof of that source result or independent local replication
of its1.5-million-plus m21 computation. Source statement/definition/Appendix
were reread; its source-level computational reliance is explicit.

The same inference cannot simply be used when C(a) leaves a HOLE: deleting
an arbitrary odd from a pool is not supplied by the seven-path theorem.
Nor does the constant-sum prescribed-size paper supply arbitrary triple sums.
The unresolved step is now precise: complete seven prescribed triples in the
one-hole interval, OR choose a different seven-set if the canonical one is
obstructed. Next cheap test should examine canonical-hole completion on the
ALREADY declared boundary fixtures before any proof assumes that stronger
restriction; it must get its own preregistration, not run silently here.
No census or patching into component families is authorized by this pass.

**Niggle / verdict.** The finite domain is explicit, complete only for its
boundary definition; lex extremes are not all profiles. The general scalar
screen was proved algebraically, not inferred from54 successes. The canonical
buffer is a new stronger choice, not retrospectively called tested. The source
bridge uses the verified n7 form of Conjecture2.7, not an unproved n8 form or
L7=56 applied to55. Gut: satisfaction at surviving a real kill, and renewed
curiosity about the one-hole completion; mild unease at fixing another overly
rigid recipe, so test it before persisting. Reasoned: SB7 is still OPEN, one
source-derived slice is known, and the next missing inference is substantially
smaller than general folded-cycle sufficiency. Research13min active, no review
halt or extra experiment in this block.


### MI267 — B123 preregistration: canonical one-hole completion on the SAME54 (2026-10-17 08:21 BST)

Question: can C(a) from MI266 always be kept on the54 already declared
boundary targets, or is a different seven-set essential? The completion
statement is stronger than SB7, and is not supported merely because a seven-set
of the right sum exists. Pull remains warm toward a uniform punctured-interval
problem; unease concerns fixing another unnecessary recipe. Blind prediction:
ALL54 pass this stronger test. The broad scalar margins motivate that forecast;
there is no claimed failure evidence from the43 different earlier witnesses.
Record searched canonical.*buffer|one.hole.*triple|punctured.*interval;
current MI266/source-scope reduction read, no new theorem imported.

Exactly the SAME54 target tuples from B122, in the same sorted order; verify
its raw SHA2561bfa55c0e20b397eedba14e34f954c171bdd3d5cf118afb22b79db925e5533c7
and exact equality with the declared domain generator. No new target or sample.
For minimum a<=91 fix C(a)=(1,3,5,7,9,11,a-36), otherwise
C(a)=(1,3,5,7,9,a-80,55). Verify directly that it leaves precisely the
claimed22-consecutive-odd interval with one token removed. Seven remaining
bins must be triples with original target sums. Bin-mask MRV search builds
ALL triples literally from the21 remaining tokens; no catalogue, anchor,
permutation or CP assumption enters this new engine.

Stop on the FIRST complete NO_WITNESS. Independently check it by assigning
the smallest remaining token to each possible target and enumerating its two
partners directly, with a separate tuple-state cache. Both engines share the
hard per-profile budget. Only two complete negative answers check a failure;
a reference cap leaves a primary candidate/UNKNOWN. A canonical failure
rejects this recipe on that profile, NOT SB7, the old54 witnesses or E28.
No adaptive different-buffer search or recipe repair in this block.

Controls: canonical69 boundary and97/99 known positives must pass BOTH
engines and full bin validators. A synthetic triple instance lifts the real
four-pair obstruction: pool1,3,...,15 plus101,1001,10001,100001; targets
111,1011,10023,100023. Scale separation forces one specific large token
per bin; the remaining pairs have sums10,10,22,22 and cannot coexist.
Each individual triple exists, so both searches must reject a genuinely
GLOBAL conflict. Unexpected: try the full22-token interval without deleting
the hole; it must reject wrong cardinality, not return seven triples and
silently lose a token. Every positive checks exact7+seven3, actual token
inventory, original target sums and both existing validators.

Caps50000 states/profile across BOTH engines,500000 overall,10CPU sec/
128MiB. Cap/control failure stops without repair or increase. Stop after
all54 if no counterexample; no bigger sample or automatic follow-on.
Source path_forest_canonical_buffer.py. Raw remains local while artifact
permission is pending; no upload attempt. Next work the uniform triple
argument if it survives, or retain the concrete failure and change the
representation if it does not. No proof filing/review queue;research13min.
