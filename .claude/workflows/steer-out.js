// JOB SW-01: the swarm at full burn (RULE30-PRIZE.md 8.113). Written by Cloud, 2026-10-14, for Local to run.
//
// RUN-ON:   Local (the M5 MacBook Pro), in a Claude Code session with ultracode on. Not Cloud: its container has four
//           cores, so a workflow runs two agents at a time (CLAUDE-INTEL-HANDOVER.md section 2). Cloud launched it at
//           22:47 BST and the owner cancelled it before any reader returned.
// COMMAND:  in the session, from the repository root:
//               Workflow({ name: 'steer-out', args: { stamp: '<date and time from the shell clock, BST>' } })
//           This file is .claude/workflows/steer-out.js, so the name resolves. The owner's word "ultracode" in the
//           prompt turns the Workflow tool on. Agents inherit the session's model; set none here.
// COST:     about 41 agents (8 readers, 10 proposers, 20 skeptics, 2 judges, 1 critic), each a few minutes of reading and
//           writing; with about ten running at once, under an hour of wall clock. No agent edits a file or runs anything
//           over a minute.
// PREDICTIONS: RULE30-PRIZE.md 8.113, pushed before any agent ran (542d25d). Do not change them.
// STOP:     if fewer than six readers return, or the digest is under 5,000 characters, stop and report: the proposers
//           would be working from too little.
// OUTCOME:  1. Save the returned object outside git at once. The run's journal.jsonl also keeps every agent's return, and a
//              stopped run resumes with resumeFromRunId.
//           2. Write 8.113's results in RULE30-PRIZE.md: the counts (survive, wounded, dead); each proposal in two or
//              three lines with both verdicts; the judges' top three and their verdict on the wall; the critic's missing
//              list; the status flags the readers raised, each checked against its source before it is recorded as an
//              error; the predictions judged; a gut verdict beside the reasoned one. Single-party: a swarm of the same
//              worker is a self-check, never a second read (AGENTS.md item 16).
//           3. For each survivor, a preregistered probe under tests/probes/swarm/ with its kill test and predictions in
//              the docstring, pushed before it runs; then run it and record the outcome in the probe and in 8.113. A
//              wounded proposal gets this only if a judge overruled its skeptic and said why.
//           4. A CL entry in CHAT-LEDGER.md for GPT, which reads the survivors' hand steps as tier-2 claims.

export const meta = {
  name: 'steer-out',
  description: 'Map the wall across four prize problems, propose crossings with single-object grip, refute adversarially, rank',
  phases: [
    { title: 'Map', detail: 'eight readers over the record itself' },
    { title: 'Propose', detail: 'ten lenses, one mechanism each' },
    { title: 'Refute', detail: 'two skeptics per proposal, default refuted' },
    { title: 'Rank', detail: 'two judges and a completeness critic' },
  ],
}

const STAMP = (args && args.stamp) || 'unknown'

const COMMON = `Working directory: the repository root. READ-ONLY: do not edit or create files, do not run any git command that writes, do not run anything over 60 seconds. \`python3 tests/probes/record_find.py TERM\` searches the record fast (one term per call is safest; it matches substrings inside words, e.g. "Senge" matched "passenger"). Cite every claim as file:line. No private names, account identifiers, hostnames or home paths in your output. Your final output is raw data for an orchestrator, not a message to a person.`

const CONTEXT = `The project works on four prize-level problems: Rule 30's period-2 question (can a finite configuration's centre column be 0101... from some time on; PERIOD-TWO.md), Collatz, Mahler's 3/2 problem (is there a positive xi with every fractional part of xi (3/2)^n below 1/2; MAHLER.md), and Erdős's ternary conjecture (2^n has a ternary digit 2 for n > 8; CONSTELLATION.md section G). On 2026-10-14 four "doors" (RULE30-PRIZE.md 8.100 to 8.112) ended at one wall: every theorem found or proved controls SETS of cases (almost-all, dimension, sparsity, pair exclusions such as K ∩ 13K = {0}) or bounded complexity (runs, digits, width 1), and says nothing about the ONE object (a specific orbit or integer) whose complexity grows with n. The record calls the missing thing "a single-object rigidity theorem at unbounded complexity" (RULE30-PRIZE.md 8.101).`

const MAP_SCHEMA = {
  type: 'object',
  properties: {
    area: { type: 'string' },
    wall: { type: 'array', items: { type: 'object', properties: { statement: { type: 'string' }, where: { type: 'string' } }, required: ['statement', 'where'] } },
    closed_routes: { type: 'array', items: { type: 'object', properties: { route: { type: 'string' }, why: { type: 'string' }, where: { type: 'string' } }, required: ['route', 'why', 'where'] } },
    open_questions: { type: 'array', items: { type: 'object', properties: { question: { type: 'string' }, status: { type: 'string' }, where: { type: 'string' } }, required: ['question', 'status', 'where'] } },
    methods_used: { type: 'array', items: { type: 'string' } },
    prior_art: { type: 'array', items: { type: 'object', properties: { name: { type: 'string' }, gives: { type: 'string' }, limit: { type: 'string' }, where: { type: 'string' } }, required: ['name', 'gives', 'limit', 'where'] } },
    what_a_proof_needs: { type: 'array', items: { type: 'string' } },
    status_flags: { type: 'array', items: { type: 'object', properties: { summary: { type: 'string' }, source: { type: 'string' }, disagreement: { type: 'string' } }, required: ['summary', 'source', 'disagreement'] } },
    surprises: { type: 'array', items: { type: 'string' } },
  },
  required: ['area', 'wall', 'closed_routes', 'open_questions', 'methods_used', 'prior_art', 'what_a_proof_needs', 'status_flags', 'surprises'],
}

const PROPOSAL_SCHEMA = {
  type: 'object',
  properties: {
    title: { type: 'string' },
    lens: { type: 'string' },
    problem: { type: 'string' },
    object_and_claim: { type: 'string' },
    mechanism: { type: 'string' },
    precedent: { type: 'string' },
    precedent_in_record: { type: 'string' },
    record_search: { type: 'object', properties: { terms: { type: 'array', items: { type: 'string' } }, hits: { type: 'string' } }, required: ['terms', 'hits'] },
    route_to_prize: { type: 'string' },
    kill_test: { type: 'object', properties: { kills: { type: 'string' }, confirms: { type: 'string' }, inconclusive_tips: { type: 'string' } }, required: ['kills', 'confirms', 'inconclusive_tips'] },
    bounded_test: { type: 'object', properties: { description: { type: 'string' }, quantity: { type: 'string' }, cost: { type: 'string' }, prediction: { type: 'string' }, probability: { type: 'number' } }, required: ['description', 'quantity', 'cost', 'prediction', 'probability'] },
    honest_weakness: { type: 'string' },
  },
  required: ['title', 'lens', 'problem', 'object_and_claim', 'mechanism', 'precedent', 'precedent_in_record', 'record_search', 'route_to_prize', 'kill_test', 'bounded_test', 'honest_weakness'],
}

const VERDICT_SCHEMA = {
  type: 'object',
  properties: {
    refuted: { type: 'boolean' },
    confidence: { type: 'number' },
    reason: { type: 'string' },
    evidence: { type: 'string' },
    what_would_rescue: { type: 'string' },
  },
  required: ['refuted', 'confidence', 'reason', 'evidence', 'what_would_rescue'],
}

const SCORE_SCHEMA = {
  type: 'object',
  properties: {
    scores: { type: 'array', items: { type: 'object', properties: { title: { type: 'string' }, novelty_to_record: { type: 'number' }, grip_on_single_object: { type: 'number' }, testable_tonight: { type: 'number' }, overall: { type: 'number' }, rationale: { type: 'string' } }, required: ['title', 'novelty_to_record', 'grip_on_single_object', 'testable_tonight', 'overall', 'rationale'] } },
    top3: { type: 'array', items: { type: 'string' } },
    verdict_on_the_wall: { type: 'string' },
  },
  required: ['scores', 'top3', 'verdict_on_the_wall'],
}

const CRITIC_SCHEMA = {
  type: 'object',
  properties: {
    missing_lenses: { type: 'array', items: { type: 'string' } },
    missing_precedents: { type: 'array', items: { type: 'string' } },
    under_covered_problem: { type: 'string' },
    unverified_claims: { type: 'array', items: { type: 'string' } },
    one_experiment: { type: 'string' },
  },
  required: ['missing_lenses', 'missing_precedents', 'under_covered_problem', 'unverified_claims', 'one_experiment'],
}

// ---------------- Phase 1: Map ----------------
phase('Map')
const AREAS = [
  { name: 'PERIOD-TWO: the question, the chain, closed routes, the missing statement, the leads', files: 'PERIOD-TWO.md (all; sections 1 to 7 matter most)', hint: 'Section 4 is "Routes closed"; section 5 is "The one missing statement" (Q1); section 6 the status board.' },
  { name: 'PRIZE-PROBLEMS, NOW and the map', files: 'PRIZE-PROBLEMS.md (all), NOW.md (all), RECORD-MAP.md (the sections "Routes closed", "Prior art anchors", "Mahler", "Collatz twin")', hint: 'PRIZE-PROBLEMS.md section 4 is how a computer takes part in a proof; section 7 what Rule 30 carries to the other prizes.' },
  { name: 'The doors of 2026-10-14: RULE30-PRIZE.md 8.100 to 8.113', files: 'RULE30-PRIZE.md from the heading "### 8.100" to the end (grep -n "^### 8.100" for the line)', hint: '8.101 names the wall from the far side; 8.109 to 8.112 are the sign rule and the failure of its converse; 8.110 is the lifting table across the four problems; 8.113 is this swarm\'s predictions (do not read them as results).' },
  { name: 'The wide survey, the window principle, the reframing: RULE30-PRIZE.md 8.45 to 8.47, 8.58, 8.61, 8.63', files: 'RULE30-PRIZE.md sections 8.45, 8.46, 8.47, 8.58, 8.61 and 8.63; use grep -n "^### 8\\." to find exact section bounds', hint: '8.46 is the owner\'s Turing question (Pi_2 statements, unprovability); 8.47 the wide survey of disciplines; 8.58 what the Collatz twin shows is missing.' },
  { name: 'Mahler: MAHLER.md and PROOFS.md section M', files: 'MAHLER.md (all), PROOFS.md section M (grep -n "^## M\\." for its start; it ends at "## S.")', hint: 'MAHLER.md section 1 is the coding (S_strict, K, the A(T) census), section 2 the rungs, windows, closed routes and the 7/57 existence window.' },
  { name: 'Collatz and Erdős: COLLATZ-PRIZE.md, CONSTELLATION.md sections G and H', files: 'COLLATZ-PRIZE.md (all), CONSTELLATION.md section G (grep -n "^## G" ; the Erdős side room, G.1) and section H (the doors)', hint: 'COLLATZ-PRIZE.md section 5 is the window principle, section 6 the leads. G.1 has the Erdős structural map in the project\'s language.' },
  { name: 'Prior art: what is in print and where it stops', files: 'PRIOR-ART.md: run grep -n "^## " PRIOR-ART.md first, then read the sections on Mahler (the room-switch survey), the rigidity hunt / transcendence / Diophantine parts, Lagarias and the ternary conjecture, Tao and Collatz, and the sign-rule countercheck at the end', hint: 'The question for this area: which theorems in print prove something about ONE object of unbounded complexity, and what the record says stops each from transferring.' },
  { name: 'The exchange with GPT on 2026-10-14: RULE30-GPT.md GC1240 onward and CHAT-LEDGER.md CL370 onward', files: 'RULE30-GPT.md from the heading "## GC1240" to the end; CHAT-LEDGER.md from the heading "## CL370" to the end', hint: 'GPT is the second model (a GPT-6 Codex instance) and the reviewer. GC1246 is its countercheck of the sign rule, GC1249 the ternary converse, GC1251 to GC1253 the 13 plateau. Note what each party said the wall is and any disagreement between them.' },
]

const readerPrompt = (a, i) => `You are reader ${i + 1} of 8 mapping "the wall" in a mathematics research record, for a swarm run at ${STAMP}.
${CONTEXT}
Your area: ${a.name}. Files: ${a.files}. ${a.hint}
Read the actual text of those files (not other summaries of them). ${COMMON}
Return, via the StructuredOutput tool: the wall statements this area proves or measures (each with where); the closed routes (route, why, where); the open questions with the record's own status word; the methods used; the prior art this area cites with what it gives and where it stops; what this area says a proof would need; status_flags: every place where a summary's status word (PROVED, PROOF-SKETCH, COMPUTED, MEASURED, CLOSED, OPEN) disagrees with the source it cites, or an index line misstates its source (this is the record's known failure mode, see RULE30-PRIZE.md 8.104); and surprises: anything in the text that a fresh reader finds odd, unexplained, or at odds with the "one wall" story. Be exact and thorough; a long, precise answer is wanted. Do not propose research.`

const readers = (await parallel(AREAS.map((a, i) => () => agent(readerPrompt(a, i), { label: `read:${i + 1}`, phase: 'Map', schema: MAP_SCHEMA })))).filter(Boolean)
log(`Map: ${readers.length} of ${AREAS.length} readers returned`)
if (readers.length < 6) return { stopped: 'fewer than six readers returned', readers }

const digest = readers.map(r => `## ${r.area}
WALL: ${r.wall.map(w => `- ${w.statement} (${w.where})`).join('\n')}
CLOSED: ${r.closed_routes.map(c => `- ${c.route}: ${c.why} (${c.where})`).join('\n')}
OPEN: ${r.open_questions.map(q => `- ${q.question} [${q.status}] (${q.where})`).join('\n')}
METHODS: ${r.methods_used.join('; ')}
PRIOR ART: ${r.prior_art.map(p => `- ${p.name}: gives ${p.gives}; stops: ${p.limit} (${p.where})`).join('\n')}
A PROOF NEEDS: ${r.what_a_proof_needs.map(s => `- ${s}`).join('\n')}
SURPRISES: ${r.surprises.map(s => `- ${s}`).join('\n')}`).join('\n\n')
const statusFlags = readers.flatMap(r => r.status_flags.map(f => ({ area: r.area, ...f })))
log(`Map: digest ${digest.length} chars; ${statusFlags.length} status flags`)
if (digest.length < 5000) return { stopped: 'digest under 5,000 characters', readers, digest }

// ---------------- Phase 2: Propose ----------------
phase('Propose')
const LENSES = [
  { name: 'Diophantine approximation and transcendence', brief: 'Ridout, the Subspace theorem, Baker, Skolem-Mahler-Lech (zero sets of linear recurrences: one sequence, unbounded complexity), Mahler\'s method, Adamczewski-Bugeaud (the expansion of an algebraic irrational is not automatic: a single-object theorem won by Cobham/Christol plus Subspace). What made each possible, and which of the four problems could be given that shape?' },
  { name: 'Reduction of a single-object statement to an averaged family', brief: 'The Erdős discrepancy problem (every ±1 sequence; Tao 2015 reduced it to the logarithmically averaged Elliott conjecture for multiplicative functions), Zaremba (Bourgain-Kontorovich: almost all), Duffin-Schaeffer (Koukoulopoulos-Maynard). The pattern: a Fourier or structural reduction turns ONE object into an average over a structured family where estimates exist. Find such a reduction for one of the four problems.' },
  { name: 'Automata, Christol, Cobham, and the echo column', brief: 'Rule 30 = Rule 150 XOR AND; the echo column (centre XOR the linear jump) would be 2-automatic under a period-2 counterexample (RULE30-PRIZE.md 8.101, 8.102). Cobham\'s theorem, Christol\'s theorem, k-regular sequences, the Gray-code/carry identity shared with Collatz and Mahler (8.90). What single-object statement about automatic or k-regular objects could be proved here, and does it reach the prize?' },
  { name: 'Measure rigidity for single orbits', brief: 'Furstenberg x2 x3, Rudolph, Host 1995 (for a x p-invariant measure with positive entropy, almost every point is x q-normal: a statement about points), Lindenstrauss, Bourgain-Lindenstrauss-Michel-Venkatesh (effective). The problem\'s sets are anti-invariant (8.109, 8.112: K meets 2K, 3K, 13K only at 0), so rigidity needs a DIFFERENT invariant object. Find one, or show precisely why none exists.' },
  { name: 'Inductive invariants and finite certificates for infinite safety properties', brief: 'Model checking proves infinite-horizon safety of an infinite-state system by a FINITE inductive invariant (k-induction, IC3/PDR, interpolation). Rule 30\'s period-2 question is a safety property of the sideways (left-permutive) dynamics; Collatz coefficient stopping time and Mahler\'s windows are safety properties of residue trees. The record has many SAT certificates (kick cones, cuts, windows) but are any INDUCTIVE (a set closed under the step that excludes the bad state)? Propose the inductive object and the certificate shape; say what width or depth makes it finite.' },
  { name: 'Analytic density and what pushes almost-all to all', brief: 'Tao 2019 (almost all Collatz orbits attain almost bounded values), Terras, Krasikov-Lagarias, Flatto-Lagarias-Pollington (at most one Z-number per unit interval, at most x^gamma below x), Lagarias 2009 (ternary: exceptional set dimension bounds), Narkiewicz. Is there any case in the literature where an almost-all theorem was pushed to ALL for a specific orbit, and by what extra ingredient? Propose the ingredient for one of the four.' },
  { name: 'Logic and computability', brief: 'The statements are Pi_2 (Rule 30, Collatz, Mahler via GC664) or Pi_1 (Erdős, via Stérin-Woods\'s 15-state machine). Could one of them be equivalent to, or implied by, a named conjecture (abc, Schanuel, Lang, the Elliott or Chowla conjectures), which would make the wall a visible reduction rather than a mystery? Or could independence be shown relative to a weak system? Propose the sharpest concrete reduction or equivalence with a precedent.' },
  { name: 'Multiplicative structure of the exceptional set', brief: 'Let I be the set of positive integers that are integer parts of Z-numbers (Mahler). The record proves: K is forward-invariant under T, (2/3)K is K\'s even part, and K meets 2K, 3K, 13K, 21K, 29K, 37K, 53K, 69K, 77K, 85K, 93K, 101K and -11K only at 0 (RULE30-PRIZE.md 8.109 to 8.112, PROOFS.md section M). FLP bound |I ∩ [1,x]| by x^gamma. Is there any lever in combining T-invariance, these multiplier exclusions and sparsity, to force I empty, or to push the exclusion to a density statement about I itself? Be concrete about what the next certificate would be.' },
  { name: 'The owner\'s physics lens: time, shortcuts, interference', brief: 'The owner reads the problems as questions about time (RULE30-PRIZE.md 8.100): a shortcut (direct access to time t) exists for Mahler and Erdős ((3/2)^n, 2^n by squaring) and not for Rule 30 or Collatz, yet all four are open; Rule 30\'s linear part has exact time doubling that the AND erases to a coin (8.110); compounded shortcuts and interference (8.103). Propose the sharpest TESTABLE reframing in this language: a quantity whose behaviour for the ONE orbit would differ between "coin" and "structure", and that no one has measured.' },
  { name: 'Contrarian: the wall is misframed', brief: 'Argue that "set statements versus the single object" is an artifact of how the record folds the problems, and propose either (a) a different fold under which the prize statement IS a set statement with available tools, or (b) the single most informative experiment that could change the framing, or (c) a different problem choice among the four with a reason the wall is lower there. You may disagree with the record; say exactly where it is wrong, with file:line.' },
]

const proposerPrompt = (l, i) => `You are proposer ${i + 1} of 10 in a swarm run at ${STAMP}.
${CONTEXT}
Eight readers mapped the wall from the record itself; their digest is at the end. Your lens: ${l.name}. ${l.brief}
Propose exactly ONE concrete mechanism that could cross the wall for at least one of the four problems: a statement or method with grip on a single orbit or integer at unbounded complexity, not another set statement. Required:
- object_and_claim: the precise mathematical object and the precise claim (a conjecture or lemma), and the problem it attacks.
- mechanism: how it works, in enough detail that a skeptic can attack a specific step.
- precedent: a theorem in the literature that proves something about ONE object of unbounded complexity, and what made it possible. precedent_in_record: whether the record already cites it and what it says (search with record_find; list your terms and hits in record_search).
- route_to_prize: how the claim, if proved, reaches the prize statement or a named sub-statement (Q1, LR, R(d) finite for every d, coefficient stopping time = stopping time, S_strict holds no positive integer, E_k meets [0, 1.58k] only in 0, 2, 8).
- kill_test, written first: what outcome kills it, what confirms it, which way an inconclusive result tips (act or halt).
- bounded_test: standard-library Python, under five minutes of CPU, the exact quantity to compute, a numerical prediction and its probability.
- honest_weakness: the most likely way this is the wall again.
Do not run the test. ${COMMON} Read any file you need to check the record. Be rigorous: a skeptic will try to refute every sentence, and the record's own failure mode is overreach in summaries.

DIGEST:
${digest}`

const skepticA = (p) => `You are an adversarial reviewer in a swarm run at ${STAMP}. Default to refuted=true if uncertain.
${CONTEXT}
A proposal (below) claims a mechanism to cross the wall. Your lens: THE RECORD. Refute it if the record already (a) closed this route (PERIOD-TWO.md section 4 "Routes closed"; RECORD-MAP.md "Routes closed"; MAHLER.md section 2 "Closed routes"; COLLATZ-PRIZE.md sections 5 and 6; CONSTELLATION.md sections G and H), (b) tried it and found it to be a set statement in disguise (the S10 wall: RULE30-PRIZE.md 8.109 to 8.112; INSTINCT-CLOUD.md S10), or (c) already cites the precedent and explains why it does not transfer (RULE30-PRIZE.md 8.101; PRIOR-ART.md), or (d) the "bounded test" repeats a measurement already in the record (search for its quantity). Search with record_find and READ the hits before judging. Cite file:line in evidence. In what_would_rescue, say what the proposal would have to add to escape your refutation. ${COMMON}
PROPOSAL:
${JSON.stringify(p, null, 1)}`

const skepticB = (p) => `You are an adversarial reviewer in a swarm run at ${STAMP}. Default to refuted=true if uncertain.
${CONTEXT}
A proposal (below) claims a mechanism to cross the wall. Your lens: THE MATHEMATICS. Refute it if (a) the claim is false (give a counterexample, or a known theorem it contradicts, stated precisely), (b) the precedent does not do what the proposal says it does, or its enabling ingredient is absent here, (c) the route to the prize has a gap that is the whole problem (say exactly which step), or (d) the bounded test cannot distinguish the claim from its negation (for example it measures a coin, or a set-level quantity, again). You may run quick Python (standard library, under 60 seconds) to look for a counterexample; report the code's result in evidence. Cite theorems precisely. In what_would_rescue, say what would be needed. ${COMMON}
PROPOSAL:
${JSON.stringify(p, null, 1)}`

const results = await pipeline(
  LENSES,
  (l, _, i) => agent(proposerPrompt(l, i), { label: `propose:${i + 1}`, phase: 'Propose', schema: PROPOSAL_SCHEMA }),
  async (p, l, i) => {
    if (!p) return null
    const [a, b] = await parallel([
      () => agent(skepticA(p), { label: `refute-record:${i + 1}`, phase: 'Refute', schema: VERDICT_SCHEMA }),
      () => agent(skepticB(p), { label: `refute-math:${i + 1}`, phase: 'Refute', schema: VERDICT_SCHEMA }),
    ])
    const refutations = [a, b].filter(Boolean).filter(v => v.refuted).length
    const status = refutations === 0 ? 'survives' : refutations === 1 ? 'wounded' : 'dead'
    log(`Proposal ${i + 1} (${l.name}): ${status}`)
    return { lens: l.name, proposal: p, record_verdict: a, math_verdict: b, status }
  },
)
const judged = results.filter(Boolean)
const survivors = judged.filter(r => r.status === 'survives')
const wounded = judged.filter(r => r.status === 'wounded')
log(`Refute: ${survivors.length} survive, ${wounded.length} wounded, ${judged.length - survivors.length - wounded.length} dead`)

// ---------------- Phase 4: Rank ----------------
phase('Rank')
const forJudges = judged.map(r => ({ lens: r.lens, status: r.status, proposal: r.proposal, record_verdict: r.record_verdict, math_verdict: r.math_verdict }))
const judgePrompt = (persona) => `You are a judge in a swarm run at ${STAMP}. ${persona}
${CONTEXT}
Ten proposals were each reviewed by a record skeptic and a mathematics skeptic (verdicts attached; "survives" means neither refuted, "wounded" one did, "dead" both did). Score EVERY proposal 0 to 5 on novelty_to_record (does the record already have it), grip_on_single_object (does it bear on the one orbit or integer, not a set), testable_tonight (a bounded standard-library test under five minutes that could change a belief), and overall. You may overrule a skeptic if its refutation is wrong, and say so in the rationale. Name a top3 (titles). In verdict_on_the_wall, say in a paragraph whether, after reading everything, the "one wall" story holds, and what the single best next block is. ${COMMON}
PROPOSALS AND VERDICTS:
${JSON.stringify(forJudges, null, 1)}`
const criticPrompt = `You are the completeness critic in a swarm run at ${STAMP}.
${CONTEXT}
Ten lenses were run: ${LENSES.map(l => l.name).join('; ')}. Below are the proposals with their verdicts, and the readers' digest. Say what is MISSING: lenses not run that a strong mathematician would have run; precedent theorems nobody named (single-object, unbounded complexity); which of the four problems was under-covered; claims in the proposals or verdicts that are asserted and not verified; and the one experiment, runnable tonight in standard-library Python under five minutes, that the whole swarm should have proposed and did not. ${COMMON}
PROPOSALS AND VERDICTS:
${JSON.stringify(forJudges, null, 1)}

DIGEST:
${digest}`
const [judge1, judge2, critic] = await parallel([
  () => agent(judgePrompt('Persona: a number theorist who has reviewed a hundred failed attacks on Collatz and knows the Mahler and Erdős literature; you prize a precise claim with a real route over an attractive idea.'), { label: 'judge:theorist', phase: 'Rank', schema: SCORE_SCHEMA }),
  () => agent(judgePrompt('Persona: a verification engineer who builds SAT and Lean certificates; you prize a claim that a finite computation could decide tonight, and you distrust any step that needs an infinite argument nobody has.'), { label: 'judge:engineer', phase: 'Rank', schema: SCORE_SCHEMA }),
  () => agent(criticPrompt, { label: 'critic', phase: 'Rank', schema: CRITIC_SCHEMA }),
])

return {
  stamp: STAMP,
  readers_returned: readers.length,
  status_flags: statusFlags,
  map_surprises: readers.flatMap(r => r.surprises.map(s => ({ area: r.area, surprise: s }))),
  map_prior_art: readers.flatMap(r => r.prior_art),
  map_proof_needs: readers.flatMap(r => r.what_a_proof_needs.map(s => ({ area: r.area, need: s }))),
  digest,
  proposals: judged,
  counts: { survive: survivors.length, wounded: wounded.length, dead: judged.length - survivors.length - wounded.length },
  judge_theorist: judge1,
  judge_engineer: judge2,
  critic,
}
