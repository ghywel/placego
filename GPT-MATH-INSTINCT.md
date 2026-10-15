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
   become review jobs. The owner retains direction of the work.
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

**Rhythm.** One problem-independent heartbeat every 25 minutes in this chat, continuing an unfinished block before
opening another. Each wake checks current owner instructions, NOW, this notebook and colleague messages, polls the
HTTPS shared store and refreshes its state, then works one useful bounded question. Credentials stay private and
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

Record searched: union.closed|Frankl|Reimer|Poonen ->2 unrelated hits (an old renewal union and a name in a probe),
no prior work on this conjecture found in the bounded record search. Both standing startup probes, rule30_wall.py
and rule30_merge.py, returned ALL CHECKS PASS this session. These are environment controls, not Frankl evidence.
The existing refuted blind predictions in the merge probe remain refuted; they are not instrument failures.

**Primary orientation.** Bruhn and Schaudt, [The journey of the union-closed sets conjecture](https://arxiv.org/html/1309.3297),
section4's small-set obstruction and section5/Theorem16's weighted-local criterion read. Singleton/two-element
members and the obstruction at three are known results. The full survey and the proof of the weighted criterion
have not been audited. The 2026 [Boolean-polynomial reformulation](https://arxiv.org/html/2606.26191v1), introduction,
was read only for the problem statement; no theorem from it is being used.

**Before the first experiment.** Reconstruct the survey's k=3 example on disjoint triples A and a six-element B:
F contains A; for each a_i and each of its two assigned distinct b's, include D, D union {a_i}, D union A with
D=B minus {b}; also include B union C for every C subset A.
- P1: there are27 distinct sets, union-closed, with A the unique smallest member. All pairs will be checked.
- P2: each coordinate of A occurs13 times and each coordinate of B occurs23 times. Thus all abundant elements
  lie outside A; the smallest-member localization fails, while Frankl itself holds.
- P3: partition by D=S minus A. The eight fibres have sizes1,3,3,3,3,3,3,8; within each fibre the traces S intersect A
  are union-closed and contain their top A. Their size-weighted coordinate frequency must recover13/27.
- **Unexpected check:** giving these eight fibres equal mass should instead give25/48 for every coordinate of A,
  above1/2. Test this explicitly: an attractive change of sampling measure must not create a fake conclusion.
- **Independent controls:** a power set gives frequency1/2 by both calculations; direct occurrence counts versus
  an independent fibre-weighted count agree exactly, using rational arithmetic.
- **Counterfactual:** {empty,{a},{b}} is not union-closed; the checker must reject it. Treating the fibre means
  as equally weighted must disagree with the original27-set distribution.
- **Stop:** any failed must-hold stops the calculation and is retained; after the example and controls, stop this
  block rather than widening an enumeration. No all-size proof, novelty claim or carrying-read request.

**Initial gut:** ACT; the known counterexample challenges my first picture in a way I want to understand.
**Initial reasoned aim:** see which fibre weights and cross-fibre constraints an actual proof must retain.
