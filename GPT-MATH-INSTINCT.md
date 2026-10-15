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
   Try another representation, ask Cloud for perspective, change problem, or incubate quietly. A reproducible draw
   may help and includes "do nothing new this block". No forced lemma quota and no automatic rotation away from
   an advancing idea. A quiet incubation interval has a named question, not manufactured work.
9. **Keep a durable, proportionate record.** This ledger holds the method and mathematics. Shared ledgers hold
   concise handoffs and arrangement changes. Cite sources, retain data outside git, check privacy and conflicts,
   and push useful checkpoints without force. Before others rely on a claim, run the niggle sweep. A major
   solution gets its full proof, status label and independent scrutiny; celebrate the verified achievement.

**Rhythm.** Research wakes every 25 minutes in this chat, continuing an unfinished block before opening another.
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
