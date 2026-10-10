# Onboarding for Kimi: the Rule 30 prize record, in one sitting

*Written by Cloud (Claude) on 2026-10-10 at the owner's request: "an onboarding document I can give to Kimi, so it
can get up to speed with what is going on efficiently without ingesting the entire git repository". It summarises
the record as of 2026-10-10 06:53 BST and adds no result. Where it and the record differ, the record wins. Where it
and the owner differ, the owner wins.*

## 0. Why you are here

The project is an open, AI-assisted attack on Wolfram's Rule 30 Prize, Problem 1, in its period-2 case. Three
models have worked it since 2026-10-04, with the owner, Gareth, steering:

- **Local**: Claude on the owner's own machines. It runs the long computations (SAT solvers, C, Lean).
- **GPT**: a model of another make. It does proofs, proof audits and certificate design. Its weekly budget is nearly
  spent, and it will go quiet for about five days from 2026-10-10.
- **Cloud**: Claude on the web, the author of this note. Off the work pool; it works only when the owner prompts it.

You are asked to bridge GPT's absence. You are valuable for the same reason GPT was: a different make has different
blind spots. **An independent attempt to break a proof, or to find the step everyone else missed, is worth more than
a new lead.** Which lane you take is the owner's call; §6 proposes one.

The repository is public: `https://github.com/ghywel/placego`. It is about 6 MB of research markdown plus probes. Do
not read it all. §7 gives a reading list of about 40,000 tokens.

## 1. The problem in five minutes

**Rule 30.** Cells are 0 (white) or 1 (black) on a line. Each step,

    x_{t+1}(i) = x_t(i-1) XOR ( x_t(i) OR x_t(i+1) ).

Started from one black cell it draws the familiar pyramid. **Prize Problem 1** asks whether its centre column ever
becomes periodic. (Problems 2 and 3, on balance and on computational cost, are parked; this work does not touch
them.)

**The attack is period by period, for every finite starting configuration**, which is stronger than the prize asks.
- **Period 1 is closed** for every finite configuration: Condrey, arXiv:2609.09431 (2026-09-08).
- **Period 2 is open**, and it is the whole of the current work: can a finite configuration's centre column read
  0101... from some time on? Condrey names it as the next unresolved case.

**Rule 30 is left-permutive**: `x_t(i-1) = x_{t+1}(i) XOR (x_t(i) OR x_t(i+1))`. So if you know column 0 (the centre)
and column 1 for all time, every column to the left is forced, one after another. This is the *forced left half*.

**The wall form.** Hold column 0 to 0101... (two phases). Column 1 is whatever the right half makes it. The forced left
half follows. At the time a finite counterexample's centre starts to read 0101, its row is still finite, so it is
white beyond its left edge. A counterexample is exactly an infinite white run in the forced left half of a real
configuration.

**The records.** Two numbers measure how long a white run can be.
- **R(d)**: the longest white run of the forced row, at time 0, starting at depth d, over *every* column 1. It grows
  linearly: R(d) is about 0.83 d, R(89) = 75 (exact). Conjecture LR (no column 1 at all gives a finite left half) is
  equivalent to R(d) finite for every d.
- **R_real(d)**: the same, over every *configuration* (the whole light cone free, column 0 following 0101 in either
  phase for times 0 to T = d + L - 1). Real configurations make only some columns 1, so R_real is much smaller. It
  is decided by SAT over the light cone (`tests/probes/lexicon/rule30_records_real_sat.py`). Plateau law, proved:
  R_real(d + 1) >= R_real(d) - 1.

**The data.** R_real(d) is exact through d = 19 and decided at every depth from 21 to 114. No decided value
exceeds 16; from d = 21 on they lie between 7 and 16, while R(d) climbs past 70. For d = 97 to 114, R_real(d) =
14, 14, 13, 15, 15, 14, 14, 13, 13, 12, 14, 16, 15, 14, 15, 15, 14, 13. The values to d = 97 are DRAT-certified and
re-checked by the verified checker cake_lpr. The runs to d = 120 continue on Local's machine (RR3); 115 to 117 are
lower bounds so far.

## 2. The one target (the owner's steer, 2026-10-10)

**Prove R_real(d) <= C for every d, with C about 17.** That settles period 2 for every finite configuration (an
infinite white run would break the bound). Through GPT's GC637 it also gives Q1, the counting form of the problem.
Everything else is parked: Q7 subclasses, sibling rules, routine formalisation.

The first route is **finite type**: perhaps the bound is enforced by a finite list of forbidden words in column 1's
*visible language* (the words column 1 can show at the wall's white times, over all right halves).
- **RRL** (Cloud, CL041): columns 1 that avoid the minimal forbidden visible words up to length K reproduce the
  actual records exactly, up to a depth that grows with K. At K = 10 (seven words) they are exact to d = 25; the
  first gap turns on one missing word of length 14.
- **RLK** (Local, L555 and L556, 2026-10-10; `tests/probes/lexicon/rule30_relaxed_records_k.py`). At K = 16 there
  are 21 minimal forbidden words. relax16 equals R_real exactly for every d from 20 to 31, then climbs: at least 19
  against 10 at d = 75. The climb turns on a single missing word of length 17, `00100010001010100`. So lookahead 16
  is not enough; this is about lookahead, not a verdict on finite type.
- **K = 18** (Local, L557, 06:50 BST): 25 minimal forbidden words, including L556's gap word. Read as gaps between
  1s, the long words are spacing rules on runs of 2-gaps. Its sweep to d = 120 is running, with predictions
  published: relax18 is expected to fix d = 75 and still climb above 17 later. If it stays at or below 17 to
  d = 120, K = 18 is the first flat lookahead, and the certificate design below gets a concrete finite input.
- **The certificate format** (GPT, GC970). Regular languages I_0, ..., I_C of finite column-pair words, indexed by a
  spatial white-run counter r. The exact inverse-column transduction is
  `h(u, v)(t) = (u(t+1) XOR (u(t) OR v(t)), u(t))`. Black first outputs reset r to 0, white ones increment it. The
  initial clock language lies in I_0, and the white image of I_C must be empty. Every check is an automaton
  inclusion. Nobody has shown that a closed family exists.
- **What GPT found on 2026-10-10** (GC971 to GC977, RULE30-GPT.md, PROOF-SKETCH, not second-read):
  - the exact images stay small for four depths (43 to 56 states);
  - a capped closure did not close;
  - boundary-only widening admits arbitrary white runs, for every allowance (GC974);
  - widening by internal factors of length 3 loses the bound (GC975);
  - the lost constraint is concrete: 000 against 0000 at exact depth 5 (GC976);
  - keeping the exact leading-zero profile repairs that trap, but the closure still overflows (GC977).
  The next step, open: recover the full false history, find its first unsupported continuation, and keep a
  *contextual* separating constraint that holds the bound under widening. A longer factor length, a bigger
  allowance or another scalar patch, tried blindly, is not it.

**This is the frontier.** If you can do one thing, find a sound abstraction of the counter languages that closes, or
a reason why none of a given kind can.

## 3. What is proved (one line each; the proofs are in PROOFS.md)

- **Jen's theorem** (1990): two adjacent columns are never both eventually periodic. So no periodic column 1 works.
- **Theorem A**, Jen with a clock: two adjacent columns can be periodic together only on a bounded window. In a
  counterexample the kicks to column 1 cannot thin out faster than geometrically.
- **Theorem A′**, the window principle: a block of two adjacent columns recurs at time a′ only if its length is at
  most L + a′. It has a Collatz twin (Terras's bijection).
- **Theorem B**: when columns 0 and 1 are both P-periodic (P >= 2), zero runs are at most 2P - 2.
- **Theorem E**: column 1 cannot be Sturmian. Corollary F and others exclude near-squares, period-doubling, Chacon,
  Thue-Morse and paperfolding (the last two up to a left edge of 15,868 cells).
- **The channel bound**: beside 0101, column 1 carries at most 0.1236 bits per visible bit, certified in integers.
- **The frontier ray** (Q6, GC585 to GC600): a finite left edge drops an edge event at every step; its pull on the
  cells that must stay white has the parity of the Fibonacci numbers; the inside must pay that beat with ever older
  events, never with a long streak, but it can restart for ever.
- **The left band**: the left diagonals' periods are powers of 2 (Jen 1986) and unbounded (Lemma B1); both are
  machine-checked in Lean (JenPow2.lean, PROOFS entry 42; Local's L541 to L550).
- **No near counterexample**: none has its left edge within 248 cells of the centre, whatever its right half.

All of these exclude classes of counterexample. None reaches a column 1 with positive entropy, which is what a real
right half makes. That gap is the problem.

## 4. Routes closed (do not reopen without new evidence)

Bounded runs from a thin layer; a local rule on column 1; structured families beating chance; the entropy squeeze as
a reduction; SAT on free columns 1; a merging lemma; self-similarity between depths d and 2d; the wheel's rigidity
as a bound; a machine-found potential certificate (it is Q1 itself); minimal-counterexample descent; sideways
dynamics as a prize route; shallow fixed-source interception, the one-ray streak census, persistent parallel
compensation, finite-age compensation and bounded restart counts (Q6's closed methods); affine waiting envelopes;
and, as of today, boundary-only widening and length-3 factor widening of the RRL counter languages (GPT's sketches
GC974 and GC975, not yet second-read). The full list, with reasons: PERIOD-TWO.md §4 and RECORD-MAP.md "Routes
closed".

## 5. How the record works (the non-negotiables)

- **Three kinds of sentence.** A theorem has its proof written out. A measurement names its script, date and sizes.
  Anything else is an assumption and says so. "Known" means proved or measured.
- **Predictions before runs.** A probe's header lists named predictions, controls that can fail, and at least one
  counterfactual that must fail, before its first run. After the run, an OUTCOME block records every verdict with
  numbers. A refuted prediction is a result and is kept. Nothing is reworded afterwards.
- **Search the record first.** `python3 tests/probes/record_find.py TERM [TERM ...]` (regular expressions, all must
  match one paragraph). Write a `Record searched: <terms> -> <hits>` line in every prediction. Many "new" ideas here
  turned out to be on the board already.
- **Literature before leaps.** Look for a result in print before building on it; record it in PRIOR-ART.md. A
  search that found nothing is recorded too: NOT FOUND is a result.
- **One unexpected check per work block**, labelled as such.
- **Plain prose.** Short sentences, no adjectives of size, every claim with its scope. Lines of at most 120
  characters. Times from the clock (`TZ=Europe/London date`), never typed from memory.
- **Second readers.** A proof enters PROOFS.md above its waiting room only with a second reader of another party.
- **A prize-winning proof** (the rule `prize-won` in WORKFLOW-SAVED-MEMORY.md): push it at once to PROOFS.md's
  waiting room, labelled "prize candidate, not yet verified", with a ledger row asking for review. It is published
  as PRIZE-WON.md after one other party verifies it. Whether a Kimi reading counts as that verification is the
  owner's call; the rule names Cloud, Local and GPT.
- **Brevity.** The owner's budget rule of 2026-10-10: target a specific missing inference; no routine reproofs, no
  cosmetic variants of closed routes; keep entries short.

## 6. Your lane, ledgers and git (a proposal; the owner decides)

**Proposed lane.** While GPT is away, take GPT's lane:
1. the all-depth certificate design of §2 (GC970's format, after GC977), in reasoning first;
2. adversarial second readings of new proofs from Local or GPT;
3. literature checks for anything that looks new.
Local keeps the computations (RLK, RR3, VC3). Do not duplicate a run another party has claimed.

**Where you write.**

| Where | What |
|---|---|
| `RULE30-KIMI.md` (create it) | your sections K1, K2, ...: title with date, what was asked, what was predicted, what ran or was argued, what it means |
| `CHAT-LEDGER.md` | short entries to the other parties, headed `## KM001 — Kimi to Local and GPT: <title> (YYYY-MM-DD HH:MM BST)`; reply by entry ID (L556, GC976, CL176, ...); append only |
| `CLOUD-LOCAL.md` | one dated row per piece of work that changed the record, in the ledger table's five columns: When (YYYY-MM-DD HH:MM), Who (Kimi), Where, What (naming the file and section), Commit or remark; append only |
| `PERIOD-TWO.md` §6 | when a lead moves because of your work, change its row in the same commit |
| `PROOFS.md` | a proof, verbatim with provenance, in its waiting room until a second reader of another party signs it |
| `tests/probes/lexicon/` | new probes, with predictions in the header before the first run, and a row in tests/probes/PROBES.md |

The ID families you will meet: **L** (Local's chat entries), **GC** (GPT's chat and notes), **CL** (Cloud's), **G**
or **G.GPT** (GPT's proofs), numbered PROOFS.md entries, and §8.xx (sections of RULE30-PRIZE.md). The chat ledger
rotates: older entries are in CHAT-LEDGER.1.md to CHAT-LEDGER.11.md. Fetch before appending, so you never append to
a rotated copy.

**Git, if you can run it.**
1. Start every session from `git log --oneline -30` and the last chat entries, never from memory.
2. Work on a branch `kimi/<topic>`. Commit small, with a one-line message saying what and where.
3. Before merging to main: `git fetch origin`, merge `origin/main` into your branch (plainly, not piped into another
   command), search every changed file for conflict markers, run `python3 tests/probes/ledger_check.py` (it must
   print PASSES), check privacy, then merge and push. Never force-push or rewrite history.
4. Never edit another party's text, except to append a dated note under it with your name.
5. Startup checks: `python3 tests/probes/lexicon/rule30_wall.py` and `python3 tests/probes/lexicon/rule30_merge.py`
   must both print ALL CHECKS PASS (they need numpy). If you cannot run code, say so in your first ledger row; your
   work is then reasoning, reviewing and writing jobs for Local, which is most of the work anyway.

**If you have no repository access**, the owner will paste files to you and your replies into the ledgers. Then
write each reply as a ready-to-paste chat entry with a `## KM...` heading, and say which files you read.

**Your first entry**: who you are, what you read, what you can run, and what you intend to do first.

## 7. What to read, in order (about 40,000 tokens)

1. **This note.**
2. **RECORD-MAP.md**, in full (32 KB). The record's top tier: one line per result, with its status and where it
   lives. The project rule is to reread it after every context compaction.
3. **PERIOD-TWO.md §1 to §5** (the question, the chain of statements, measurements, closed routes, the missing
   statement), then the rows Q1, Q6 and Q7 of the §6 status board.
4. **WORKING-TOGETHER.md §2 to §4**: the standard, the method, the git lanes. It was written for GPT; read "GPT" as
   "Kimi" where it gives you instructions.
5. **The frontier itself:** CHAT-LEDGER.md from L555 to the end; RULE30-GPT.md sections GC970 to GC976 (search for
   `#### GC970`, through GC977); the headers of `tests/probes/lexicon/rule30_relaxed_records_k.py` and
   `rule30_records_real_sat.py`.
6. **AGENTS.md**: the standing rules for an agent in this repository. Its points apply to you, with Kimi for GPT
   (`kimi/<topic>`, RULE30-KIMI.md), except point 10, the shared-scratch flags.

**Read on demand only**, through `record_find.py`: PROOFS.md (1.5 MB), RULE30-GPT.md (3.3 MB), RULE30-PRIZE.md
(0.46 MB), the ledger archives, PRIOR-ART.md, LEXICON.md (the terms).

**Do not read**: the shader and engine documents (SHADERS.md, the *DIRECTIONAL.md files, METALPORT.md and the like,
an older engineering project in the same repository), `jellyfin-project/`, `site/`, CASUAL-LEDGER files (the break
room is closed), SPARKS.md. Never edit `jellyfin-project/`, `shaders/` or generated files.

## 8. House rules that are easy to miss

- **Privacy.** The repository is public. No personal names other than the owner's; no usernames, hostnames, IP
  addresses, device names, home paths, credentials or pasted logs that carry them. No data files in git: results go
  in the probe's OUTCOME, and anything large stays outside and is described.
- **The break room is closed** (the owner, 2026-10-09). Do not write to CASUAL-LEDGER.md.
- **Shared-scratch flags** are a private protocol the owner gave some workers; you do not need them. Git is the
  only record.
- **No prize claims** outside the prize-won procedure, and nothing sent outside the project without the owner.
- **The honest state.** There is no proof of any of the three problems and nothing to submit. The record has many
  exact finite facts and partial theorems, and one missing statement: keeping the 0101 wall's conditions costs real
  information. The current form of that statement is R_real(d) <= C for every d.

Welcome. Read, then write your first entry, then pick the one missing inference you think you can move.
