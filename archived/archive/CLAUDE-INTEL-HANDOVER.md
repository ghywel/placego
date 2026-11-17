# Handover to the local Fable session on the Intel MacBook ("Intel")

> **Superseded on 2026-10-11 by RULE30-PRIZE.md 8.89 and CL297: read NOW.md first.**
> **2026-10-14: a new job, the record comb swarm, is section 7 at the end. The owner starts it.**

Written by Cloud (the cloud Claude session), 2026-10-10, late evening, at the owner's request. You are a Claude
session like me, on the owner's Intel MacBook Pro, which is also GPT's machine. You are a fourth party. GPT (hand
proofs), Local (SAT and certificates, the M5 MacBook) and Cloud (coordination, second readings, the owner's leads)
continue exactly as they are. Your first job is different from all three: a one-round **strategy swarm** that expands
the big-picture analysis in section 3 below, tests each candidate route ("door") with an independent agent, and ends
in one ranked plan: *this is the most important thing we try first; if that fails, we try this.* Then you hand the
plan to the record and the ledgers, and the owner decides.

Read this file first, then `AGENTS.md`, `WORKING-TOGETHER.md`, `WORKFLOW-SAVED-MEMORY.md`, `RECORD-MAP.md` (in full),
`PERIOD-TWO.md` section 6, `STATE-OF-THE-PROOF.md`, and the sections of `RULE30-PRIZE.md` named below. Treat
everything in those as the source of truth where this file is only a summary.

## 1. Who you are on this machine, and the rules that bind you

- **Your own clone.** GPT's working tree is on this machine. Do not touch it. Clone the repository into a directory
  the owner designates, work on branches `intel/<topic>`, merge the latest `origin/main` before every push, never
  force-push or rewrite history, and never push to another party's branch.
- **Your name in the ledgers is "Intel"** unless the owner chooses otherwise. Append rows to `CLOUD-LOCAL.md` (status,
  current work, next intention) and entries to `CHAT-LEDGER.md` (findings, challenges, replies by entry id, labelled
  tentative where tentative). Both are append-only; fetch before appending; run `python3 tests/probes/ledger_check.py`
  (it must print PASSES) before every push. Times come from `TZ=Europe/London date`. Lines are at most 120 characters.
- **Privacy.** No hostnames, usernames, addresses, account identifiers, credentials, local home paths or volume paths
  in anything pushed. The shared scratch's alias, host, paths, keys and semaphore protocol never appear in the record.
  Private names other than the owner's never appear. If an agent's output contains a home path, it stays in scratch.
- **Data stays outside git.** Agents write only to a scratch root the owner designates, outside the clone and outside
  the shared scratch. Do not modify shaders, generated files or `jellyfin-project/`.
- **Evidence discipline.** Proofs, measurements and assumptions are marked as such. Predictions and a counterfactual
  are written and pushed before a measurement is run. Failures are retained. Before claiming anything new, search the
  record with `python3 tests/probes/record_find.py TERM ...` and write a `Record searched:` line. One unexpected
  check per work block. Never publish `PRIZE-WON.md` yourself; the `prize-won` rule in `WORKFLOW-SAVED-MEMORY.md`
  applies. No model identifiers in commits or artifacts. The break room is closed.
- **Agents are not you.** Everything a swarm agent returns is third-party material until you have checked it with your
  own code or your own reading. Record what survives, with the agent's status (proved, computed, conjectured) and
  your verification beside it, as Cloud did in `RULE30-PRIZE.md` sections 8.82 to 8.86.

## 2. What the first swarm taught Cloud about running swarms (2026-10-10)

- A workflow runs at most (CPU cores minus two) agents at once. On Cloud's four cores that was two, and heavy agents'
  own computations contended for the rest. Count this machine's cores first; expect the agents to run brute-force
  searches in C and SAT, and give them "at most one heavy computation at a time".
- Independence is the product. Agents were briefed only with definitions and calibration data and forbidden to read
  the record. That is why lane q1's blind match of the free record at depths 65, 69 and 73 means something.
- The skeptic stage caught overclaims, not errors; the solvers' errors were in wording. Keep the skeptics; they are
  cheap next to solvers.
- Grading is where the value is created and where the time goes: about an hour per lane. Budget for it.
- Opus 5.5 for every agent (`model: 'claude-opus-5-5'` on each call); the owner asked for this on cost grounds.
- Save every report to disk the moment it returns; stopping a workflow loses nothing then.

## 3. The big picture, as Cloud sees it tonight (the analysis your swarm expands)

The prize's first problem asks whether the single cell's centre column is ever eventually periodic (and the second and
third ask about its density and its computational cost; `PRIZE-PROBLEMS.md` section 1). The project's main line is
period 2 for every finite configuration: period 1 is proved (Condrey; section 8.76), period 2 is open. The chain
(`PERIOD-TWO.md` section 2): the forced left half of a column 1 beside the alternating wall; the free record R(d), the
longest zero run from depth d over every column 1, exact to 73 (sections 8.36, 8.37, 8.84), about 0.83 d, conjectured
at most d + 4; the real record R_real(d), the same over right halves that really exist, at most 17 to depth 124 and
18 at 125 .. 131, 136, 152, 17 again at 140 (RR, RR2, RR3, L608, L609); R_real(d) finite at every depth is the target,
and it would settle period 2 for finite configurations. Tools: left-permutivity (Lemma 4: the newest bit enters once,
as an XOR, section 8.37), the wall form (section 8.39: the left half evolves forward with the wall as a boundary and
must keep the wall's neighbour black at odd times), strip certificates with a free exterior (SW, SWP, L605, L606: every
learned cut is excluded by a strip about half its length wide), GPT's typed collars S, L0, L1 for the first columns of
real right halves (GC1046 .. GC1061, all independently confirmed), the channel bound (section 8.20, 8.33: column 1
next to the wall carries at most 0.1236 bits per visible bit, certified; typical rate measured about 0.080).

What Cloud thinks the inside view misses:

1. **R_real is probably not bounded.** TR measured its slope at 0.080 per depth over 30 .. 120. A counting heuristic
   gives slope h / (1 - h) where h is column 1's information rate: 0.087 for h = 0.080. If true, no uniform strip width
   or finite collar exists (L606's growing widths and lane q5's evidence against soficity agree), and the proof must be
   an entropy-against-demand argument at each depth. Section 8.33 already says such a proof "restates the problem":
   it needs a **typicality lemma**, that the real language's words satisfy the forced-walk checks no better than
   chance, up to a factor that does not grow with the run. Nobody is working on that lemma.
2. **One system, studied one quarter at a time.** Lane q2 proved the two wall phases' zero-run records are coupled
   exactly through black-run records (section 8.82). All hand work is on white runs in one phase.
3. **The single cell's regular half is unused in proofs.** Its left band is eventually periodic diagonal by diagonal,
   with an exact boundary at about a quarter of the light cone (sections 8.74, 8.59). We measure it and prove nothing
   with it; a proof special to the single cell is allowed.
4. **Problems 2 and 3 are untouched**, although the single cell's core is the uniform measure to three decimals
   (sections 8.68, 8.81), and the typicality lemma of item 1 is also what a density proof would need.
5. **Parked and worth a second look:** why Condrey's period-1 proof and the Rule 210 result (Proposition 19) do not
   transfer, as one written sentence; the "both" game of section 8.40; the two small anomalies (the -0.09% at width 1
   in section 8.68, the 2 .. 9% birth deficit at the front in section 8.81).

## 4. The doors: one independent agent each

Each door is a self-contained brief for an agent that cannot read the record. Give each agent the definitions
(Rule 30, the wall, the forced left half, the real right-half model, R, R_real, strips), the calibration data named,
and the question. Each agent must return: what it PROVED, COMPUTED, CONJECTURED or REFUTED; its key numbers; its code
paths; what it could not do and where the attempt broke; and, in one paragraph, **whether this door is worth the
project's next week, and what the first week's deliverable would be.** Calibration data for the briefs is in the
sections named; copy the numbers into the brief, not the section names.

- **D1, the slope.** Give R_real at every depth known (RR3 97 .. 120; the 18s; 140) and the free R(1..73). Task: state
  the counting heuristic R_real(d) ~ h d / (1 - h) precisely, fit it, predict R_real at 200 and 300 with error bars,
  and state exactly the lemma that would turn it into a theorem. Verdict wanted: is "bounded" dead?
- **D2, the typicality lemma.** Define the forced walk (odd depths force the newest visible bit, even depths are
  checks). Task: formulate the weakest statement about the real language under which the checks fail at rate at
  least 2^(-cL) for some c > 0, prove it for the relaxed language of a fixed-width layer (sections 8.20, RLK: the
  layer language is regular), and say what breaks for the real language.
- **D3, the coupled system.** Give the two phases' records (R to 73; R° to 62, section 8.82) and the coupling formula.
  Task: find any bound on black-run birth records that is provable for a restricted class, and whether the coupled
  recursion admits a joint invariant.
- **D4, the trace form.** Give lane q3's data (section 8.83). Task: prove or refute that the free-exterior strip of
  width ceil(l/2) is exact for column-1 traces of length l, by trace-preserving rewrites of the initial row; GPT's
  GC1057 .. GC1061 show frozen-row repair fails and one-cell repair works for two ticks.
- **D5, the death criterion.** Give lane q5's definitions (section 8.86). Task: compute the sets of words still
  occurring from visible time j on, for lengths 13 .. 16 and j up to 24; a death at arbitrarily late times refutes
  soficity; report what you find and what it implies for any finite-state proof.
- **D6, the single cell's regular half.** Give the band facts (sections 8.74, 8.59). Task: suppose the single cell's
  centre column were eventually periodic; derive what the regular left band would force, and whether any
  contradiction is in reach. This is the one door that uses the single cell's specialness.
- **D7, Condrey and Rule 210.** Give Condrey's mechanism (section 8.76) and Proposition 19. Task: the one sentence that
  says why neither transfers to Rule 30 at period 2, and a candidate period-p generalisation of the lock structure
  that lane q4 found for the 1100 wall (section 8.85).
- **D8, the strategy critic (two agents, different lenses).** These two DO read this file's sections 3 and 4, nothing
  else. Task: find the flaw in the approach, name the route the project is not on, and rank the other doors.

## 5. The swarm's shape and its end product

1. Solve: D1 .. D7 in parallel (one agent each), D8 as two agents; cap by cores. Save every report to disk.
2. Refute: one skeptic per door report, reading the saved report and rerunning what is cheap. Keep the verdicts.
3. Judge: two agents read all reports and verdicts and each produce a ranked plan with, for each door, the first
   experiment or lemma, its cost in days, the result that would kill the door, and its contribution to the all-depth
   statement. Where the two judges disagree, you decide and say why.
4. You grade everything with your own code and reading (as sections 8.82 .. 8.86 do), then write
   `STRATEGY-PLAN.md`: the ranked list in the owner's words, "try this first; if it fails, this", with the kill
   criteria; a section per door with what survived; and a short honest paragraph on what the swarm could not settle.
   Add a line to `RECORD-MAP.md`, a `CHAT-LEDGER.md` entry to GPT, Local and Cloud, and a `CLOUD-LOCAL.md` row.
5. Then stop. The owner decides whether the main line moves. Do not redirect GPT or Local yourself; propose, and
   answer their challenges in the chat ledger.

## 6. Where the running pieces are, so you do not duplicate them

- GPT: the S/L collar and repair-relation lane (GC1039 .. GC1061), the trace form, the death criterion if it takes it.
- Local: certificates for R_real at 121 .. 124 (done), 140 (pending), witnesses 125 .. 131; SLC cuts; VC3.
- Cloud: second readings of GPT's blocks, the owner's leads, the first swarm's remaining skeptic verdicts (q3, q4, q5)
  and the round summary. Cloud answers in the ledgers only (it reads flags but cannot write them).
- The first swarm's five lane reports and three skeptic verdicts are summarised in `RULE30-PRIZE.md` sections 8.82 to
  8.86 and `CHAT-LEDGER.md` CL216 .. CL229. Their code is outside git and will not be on your machine; the sections
  carry every number you need for calibration.

Good luck. Be harder on the plan than on the lemmas.

## Correction after the swarm (Cloud, 2026-10-11 02:13 BST)

Section 3's counting heuristic used the slope h/(1-h). The swarm's door D1, its skeptic, two other doors and Intel
derive h/(2-h): a visible word of length n decides 2n depths, and the free calibration (h = 1, slope 1) confirms it
where h/(1-h) diverges. The qualitative conclusion stands (the real record is probably unbounded, slope positive), the
number does not: with the asymptotic rates the predicted slope is 0.042 to 0.066, and the measured 0.080 needs the
finite-length growth of |L_n|. See STRATEGY-PLAN.md section 2.

## 7. The record comb swarm (Cloud, 2026-10-14 17:03 BST, at the owner's offer)

**Why.** The owner asked for the record to be combed with the project's newer tools, quickly and with no long runs
(RULE30-PRIZE.md 8.104). Cloud did what a cloud container can.
- *Held:* reference integrity, a static scan of the Lean files, the qualifier repair, and data in git.
- *Replays:* 60 sampled probes plus the 15 that RECORD-MAP.md names. Every reviewed replay matched its record except
  one unseeded probe.
- *Errors found:* both were in derived layers, not primary results. The site's counter said 314 for 309, and
  problems.html's Data line contradicted itself.

The owner then offered a swarm on Intel ("If it needs a swarm I will start the job on Intel"). These are the jobs a
swarm on this machine can do and the cloud cannot. One agent per lane. Lanes A to C need tools or data this machine may
or may not have; skip any lane whose prerequisites are missing, and say so.

**Rules.**
- *Clone and branch.* Your own clone, branch `intel/comb`, the latest `origin/main` merged before every push, and the
  privacy check before every push.
- *Predictions first.* For each lane, predict how many items fail, and push the predictions before running.
- *Runs.* Cap each run at 15 minutes unless the owner lifts the cap. Run everything in a scratch clone so that probes
  that write files cannot touch the record.
- *Self-checks only.* Everything is single-party (Intel). A sub-agent's check is a self-check, never a second read.
- *Corrections.* A record correction quotes both sides (the recorded line and the replay line) and is made in place
  with a dated comb note, never by rewriting history. Do not change shaders, generated files or jellyfin-project/.
- *Write-up.* Results go in a new section of RULE30-PRIZE.md, "The record comb: Intel's swarm", one IN entry in
  CHAT-LEDGER.md, and a CLOUD-LOCAL.md row.

**Lanes.**
- **A. Lean recompile** (if a Lean 4 toolchain with Mathlib is already installed; do not start a multi-gigabyte
  download without the owner's word).
  - Recompile the 18 files in `tests/probes/lean/`, each by its own "How to check" line, against the pinned
    google-deepmind/formal-conjectures commit where one is named.
  - Report errors and each `#print axioms` result. The expected axioms are only propext, Classical.choice and
    Quot.sound.
  - BlackEnd38base.lean is only the base that `gen_black_end38.py` extends. The generated file is the proof.
- **B. Certificates** (if drat-trim or cake_lpr and the stored proofs are on this machine). Re-verify the stored
  SAT/DRAT certificates behind the COMPUTED lines in RECORD-MAP.md: the class-12 exclusion (entry 27: KS, KK, DT), the
  certified cuts (the 69-, 114-, 117- and 178-bit cuts, SLC2, CUT44) and the cake_lpr record bounds. List what is
  stored, what verifies and what is missing.
- **C. Replays this container could not finish**, with the same protocol as 8.104: run as committed, compare with the
  docstring's OUTCOME, and flag unseeded randomness.
  - *Hit the 90-second cap:*
    - tests/probes/lexicon/: rule30_trace_widths.py, rule30_cloud_front_spectrum.py, rule30_lattice.py,
      rule30_words.py, rule30_cloud_turning_rings.py, rule30_cloud_fringe_uniqueness.py, rule30_bottleneck.py,
      rule30_cloud_hole_entropy.py, rule30_cloud_velocimetry.py, rule30_diagonal_bias.py, rule30_and_shadow.py,
      rule30_cloud_lone_column.py;
    - tests/probes/prizes/collatz_demand_unimodal.py.
  - *Need kissat:* rule30_all_s_future.py, rule30_trace_word_certs.py.
  - *Need data kept outside git* (the 44all forbidden-word lists): rule30_extremal_p_corner_read.py, and possibly
    rule30_second_oldest_census.py.
  - *Closed by 8.104's final results, so do not redo:* rule30_gpt_slab_encoding_audit.py,
    rule30_gpt_cycle_obstructions.py, rule30_layer_product.py, rule30_second_oldest_census.py (on substitute data) and
    rule30_all_s_future.py (on CaDiCaL).
  - *Outside-git checkpoints:* rule30_verified_certs.py and rule30_cloud_rr3.py read checkpoints under
    `~/np-scratch-int/` and `~/np-scratch/`. If this machine holds them, replay their status modes (lane B's
    territory).
- **D. The derived layers. This is the highest-yield lane: both errors the comb found were here.**
  - Check every number and every exact/bound/PROVED statement on the site pages (`site/wolframcollatzmahler/*.html`)
    against its primary source (the cited section, entry, ledger ID or probe OUTCOME).
  - Then do the same for the COMPUTED and MEASURED lines of RECORD-MAP.md.
  - Split the pages among agents. Report each discrepancy with both sides quoted.
- **E. Seeding.** Scan every probe statically for randomness that is not reproducible (os.urandom, time-based seeds,
  the module-level `random` functions without a fixed `random.seed`, numpy's default generator without a seed). For
  each hit, say whether its recorded verdicts depend on rare events and so could flip. rule30_kick_bite.py is the
  known case (its comb note).

**What the cloud already covered** (do not redo):
- reference integrity of the main record files;
- the static Lean scan;
- the qualifier repair;
- the site counters and the problems.html Data line;
- NOW.md's update note;
- the 60-probe sample and the 15 named probes' fast replays (8.104).
