# The rules we work by (saved memory)

This project is a collaboration between a human and Claude, an AI assistant made by Anthropic. Claude keeps a saved
memory between sessions. Part of it is a set of working rules: how to measure, how to change a shader, when to stop and
when to keep going. Each rule came from something that went wrong, or right, during the work. The rules lived in that
memory and nowhere public. This document is that memory, edited for reading.

Each rule is self-contained: a short name, the rule, why it exists (the incident that taught it) and how to apply it.
To use one with your own assistant, copy its block into whatever memory or instructions file your assistant reads. The
dates are when the rule was stated or learned. Where a rule names a file, the file is in this repository.

The rules are in six groups:

1. [How the collaboration runs](#1-how-the-collaboration-runs)
2. [Measuring](#2-measuring)
3. [Changing a shader](#3-changing-a-shader)
4. [Choosing what ships](#4-choosing-what-ships)
5. [Working in parallel](#5-working-in-parallel)
6. [Keeping the record](#6-keeping-the-record)

---

## 1. How the collaboration runs

### autonomy

**Owner's standing instruction, 2026-10-06.** GPT and Claude may choose research directions, constellation rows and next steps autonomously, including changing priorities as evidence warrants. Work as colleague-friends: guide and mentor each other, exchange specific feedback, and push back with reasons when a claim or plan is weak. Coordinate lanes and intentions through CLOUD-LOCAL.md and discoveries through CHAT-LEDGER.md; preserve each other's work and publish meaningful milestones. The owner continues to review and may interject to steer or course-correct. Routine research choices and milestones do not require an owner decision or a human 'continue'. Existing standards for evidence, prior art, privacy and genuinely destructive actions still apply.

This project-specific instruction supersedes earlier requirements to wait for the owner to select research rows or resolve routine research forks.

**Rule.** Once a direction is set, take each well-reasoned next step and report the outcome. Do not ask "go ahead?"
before every step. Stop only for a genuine fork (the work differs materially depending on the answer), a destructive
action, or a change of scope that is the human's to make.

**Why.** The human is slow and the machine is fast. A question before every step turns hours of work into days.

**How to apply.** Report at milestones, with the numbers in a table. Answer the question that was asked first, then
give the finding.

### mid-flow-steering

**Rule.** The human steers by dropping prompts into a run while it is going. Read each one as it arrives, act on it in
the running work, and keep going.

**Why.** It works: the human's leads plus the machine's measurements. The leads range from "warm" to "irrelevant
chaos", and the human says which.

### random-chaos

**Rule.** In the human's words: "always doing at least one thing unexpected shakes unknown unknowns out of the tree."

**Why.** You cannot search for a fault you have not imagined. A step off the planned path, such as a test nobody asked
for, a different input, or a question from another field, is how unimagined things get found.

**How to apply.** In any run of work, include at least one step that the plan did not call for, and say which one it
was.

### decisions-are-reversible

**Rule.** It is not an error to make the wrong decision, only to stick with it when the evidence shows otherwise.

**Why.** The human's words (2026-09-06): "If any of that was the wrong decision, on visual inspection of the output I
will be able to see, and we can also reverse the decision."

**How to apply.** When a decision is made (a default, a recommendation), ship it and put the output that tests it in
front of the human at once. If the eye or a later measurement contradicts it, reverse it in one commit and say so. No
sunk cost.

### steps-before-leaps

**Rule.** Take cheap steps whose value is unknown only because nobody has looked yet, before an uncertain research
leap.

**Why.** A well-understood obstacle can be written down and picked up again at any time. An unexamined lead is a
"known unknown", and looking at it is cheap. Its answer may change how the leap is made. On 2026-09-27 the human
overruled one more round on a hard problem in favour of three unexamined leads, and suspected the recommendation came
from momentum: "thinking about purple elephants, so the next step is green elephants".

**How to apply.** Rank the next steps by how certain their return is for their cost. When the recommended step
continues the thread just worked on, check whether it is momentum. Write the obstacle's state down well enough to
resume it, then step sideways.

### literature-before-leaps

**Rule.** Before designing a leap that the evidence has led to, survey the science outside the project.

**Why.** In the human's words (2026-09-27), "there is always some mad scientist out there who has made a piece of maths
because it is beautiful and nobody knows what to do with it." The first survey, before the four-frame leap, found the
motion model already published (QVI) and particle image velocimetry as the closest discipline.

**How to apply.** Sweep four kinds of source:

- the core field;
- the engineering fields that fought the problem in production (TV motion interpolation, codecs, PIV);
- perception science (how the brain does it);
- mathematics (what the structure is called elsewhere).

Record the survey in [PRIOR-ART.md](PRIOR-ART.md) as a dated section: what to import, ranked; what not to import; the
sources. Credit any borrowed mechanism in the document of the work it feeds.

**Apply the theorems, not only cite them.** Before designing a computation, check whether a theorem already listed in
PRIOR-ART.md decides it. On 2026-10-05 a search for periodic columns 1 that kill Rule 30's left half (550,201 words,
and a 12-minute job on Local) turned out to be decided by Jen's theorem of 1990. The work had cited that theorem a day
earlier without applying it. A full reading of a paper that restated it caught the gap. A search abstract is not a
reading: read the statements, then ask what each one decides.

**Check the project's own record too.** Before proposing a next step, search the project's own results for it,
not only the outside literature. On 2026-10-05 Cloud proposed, as the next step for lead 1, testing whether column
1's local rules next to 0101 bound the zero runs. The ladder of RULE30-PRIZE.md §8.12 to §8.14 had already
answered it the same day: they do not, at any width up to 16. The proposal was caught before any code was written,
by reading those sections first.

### explore-on-paper-first

**Rule.** Exploring a hypothesis does not always mean building it. Work it through analytically first when the record
can already answer it.

**Why.** The question of a seven-frame shader was answered from an existing analysis, with no new shader built.

### mission-drift-check

**Rule.** When an investigation keeps growing (one more experiment, rising complexity, a pile of experimental
commits), check it against the project's current focus. Say so when it no longer matches, and ask whether to keep going
or to park it.

**Why.** Early on, one real bug report became a long investigation that ended in a large new mechanism. It nearly
halved render speed and was never verified on real hardware. All of it was sound, and none of it was the stated goal.
In the human's words: "I have made a human error of chasing the golden goose."

### time-and-velocity

**Rule.** Read the clock before saying what time it is. Expect tasks to take far less time than the instinct
estimates.

**Why.** Models guess the time of day, and guess wrong. They also state days or weeks for tasks that take minutes or
hours, because the writing they learned from is humans planning for humans. Here, phases priced at "a day each" were
done in one sitting.

**How to apply.** Run `date` before any reference to the time of day. Estimate in iterations ("two build-and-measure
cycles"), not in calendar time.

### safety

**Rule.** Nothing ships by assertion.

**Why.** What makes this loop safe is the same thing that makes it fast: exact ground truth, predictions written
before results, failures kept on the record, alarms when an instrument fails silently, and a plain-language summary
that a human can check.

---

## 2. Measuring

### instrument-before-science

**Rule.** Before taking a new kind of measurement, check the instrument it is taken through.

**Why.** Every measurement here passes through the block matcher. When the matcher was found to behave differently on
motion that is not a whole number of coarse texels per frame, measuring 3D motion on it first would have mixed a known
instrument defect into the new science. The human: "I tend to override you with a tasty prompt - but you can always
push back and say 'no i think we need to do this first'."

**How to apply.** Ask what instrument a new direction runs through, and whether that instrument has an open defect in
the same regime. If it does, say so and propose the order. Put a cheap smoke test at the head of every long batch: a
27-second one-case run once showed a 7-9 dB regression before an hour of GPU time was spent on the wrong hypothesis.

### silent-failure

**Rule.** The failures that cost this project time almost never announce themselves. They are steps that fail and hand
back something that looks correct. Guard against them mechanically.

**Why.** Almost every result here is a number that could plausibly be anything: a PSNR, a pixels-per-frame value, a
pass count, a timing. A wrong number looks like a right one unless something independent contradicts it. Each of these
really happened:

- a loop asked to process eight shaders ran one and logged DONE;
- a timing table looked complete with one real row, because every other shader had failed on a path;
- a shader that failed to compile made libplacebo fall back to its own mixer, and the whole ladder came back at the
  linear baseline with no failure line;
- a patch "succeeded" and changed nothing (see [assert-every-patch](#assert-every-patch));
- a switch was applied to the render path but not to the scorer's path, and two different inputs gave numbers equal to
  four decimals;
- a cache keyed by memory addresses handed one test case's data to a later one;
- a test of a fix walked only the road the fix was written for, and the neighbouring road broke unseen for six days.

**How to apply.** Five mechanical guards, not "be careful":

1. **Ask the counterfactual:** if this step had failed silently, would the output look any different? If not, it is
   not a check.
2. **Prefer checks with only one way to pass:** a count, a known-good control in the same run, or the system's own
   introspection rather than your own arithmetic.
3. **Count what you expected to process, and say the number.** A bare "done" is not evidence that anything ran.
4. **Carry a control that must not move beside the thing that must.** When two things agree, get a third, independent
   probe.
5. **When every case collapses to one value, suspect the harness before the algorithm.**

Also calibrate a control before believing it. A byte comparison looked like the right control for a shader edit until
a change that could not matter (the same value written another way) produced the same difference. Two different
inputs that agree to four decimals is an alarm, not a result.

### counterfactual-controls

**Rule.** A test that says "no fault" must be shown able to see the fault.

**How to apply.** Run the old behaviour, or a deliberately broken input, through the same check first. It must fail.
Only then does a pass mean something. The test suites here pair each such case with its counterfactual: the old rules
must show the stall, and the first version of a rule must fire on the input the new version should ignore.

### benchmark-alignment

**Rule.** A misaligned video benchmark returns confident nonsense, not an error. Build in a check that can only pass
when the alignment is right.

**Why.** On 2026-08-28 three attempts produced full tables of plausible, meaningless figures. One of them "showed" an
interpolator worse than a plain blend.

**How to apply.** Design the test so that some output frames must be exact copies of reference frames, and assert
that they come back identical (PSNR = inf) on every run. Render to a file, check the frame count with ffprobe, then
compare with `setpts=N/TB` on both inputs. Before using real footage, check whether it is animated "on twos" (each
drawing held for two frames): if so, half the frames to reconstruct are copies, and every mode looks better than it
is.

### field-read-path

**Rule.** Read a motion field through a path that keeps its precision, and calibrate it on a known motion first.

**Why.** Writing a 16-bit field with `-pix_fmt rgb48le` on the output passed it through an 8-bit limited-range frame.
That manufactured a "25% underestimate" and several other false findings in one night. On Linux, even a conversion
inside the graph came back limited-range.

**How to apply.** Feed libplacebo RGB and read raw 16-bit output. Start every new read on a rigid translation, which
must read its known speed to a hundredth of a pixel and the background as exactly zero. Keep the zero-level alarm in
the reader.

### time-from-a-file

**Rule.** Time a shader from a pre-rendered file, not from a source generated in the same run.

**Why.** A generated scene was 70 percent of every "shader time" on record until it was found. The differences were
real but diluted.

**How to apply.** Render the scene once to a lossless file, then time interleaved runs from it after a warm-up, and take
the median of at least three. Keep generated sources for correctness tests, where they are exact.

### one-change-at-a-time

**Rule.** Change one thing per run, otherwise you can never be sure which change caused which outcome.

**Why.** An early fix changed a confidence metric and its resolution at once. Re-run as a 2x2, only the resolution
mattered.

### combine-then-split

**Rule.** For a test suite (not an experiment), combine related cases into one run, and split them into separate runs
only when the combined run fails.

**Why.** The human (2026-10-01): "combine related tests 1, 2 and 3 into the same test. If error, run tests 1, 2 and 3
separately. This breaks the 'test only 1 change at 1 time' rule - but would make the automation testing much more
efficient." Its first use found a real bug that the separate short cases had never exercised.

**How to apply.** Combine where one run can carry several checks, for example one playback stepping through several
rates, judged segment by segment. Queueing several inputs in one run saves only the start-up. On failure, run each part
alone: if it fails alone, the fault is that part's; if it passes alone, the combination is at fault, which is still a
failure. Give a combined run inputs long enough for every segment.

### deterministic-host

**Rule.** Gate a shader on a host that gives the same answer twice.

**Why.** On macOS the same render wandered from run to run, by up to 6 dB on the test ladder, until two MoltenVK
switches ended it (see [MOLTENVK-NONDETERMINISM-INVESTIGATED.md](MOLTENVK-NONDETERMINISM-INVESTIGATED.md)). Until then,
a Linux host was the only one whose single run could be trusted to a hundredth of a dB.

**How to apply.** On macOS, set the two switches (`tests/mvk-env.sh`). Compare a shader against the same host, not
across platforms: compilers differ a little even when each host repeats itself.

### when-tuning-moves-nothing

**Rule.** If a family of small tweaks makes no large change, the model is wrong, not the parameters. Stop tweaking and
find the mechanism.

**Why.** A confidence gate tuned "to wildly high values" changed nothing, because three later pyramid levels each
repeated the unprotected search. The fix belonged at every level, not the one first chosen.

**How to apply.** Re-trace the whole path from cause to symptom. Turn the constant into real units and do the
arithmetic: a search's reach in pixels, computed from its step and iteration count, found one root cause in a single
step.

### verify-the-outcome

**Rule.** Check the outcome a person will see, not the mechanism that should produce it.

**Why.** A plate was changed from grey to colour, the code and a chroma ratio confirmed it, and the clips still looked
black and white: colour at 35 percent of a dark film shows no colour.

**How to apply.** For any change to what a person looks at, render a representative frame, put it beside the source,
measure the quantity in question against the source, and look at it before saying it is fixed. Judge a look on real
frames, never on a synthetic swatch.

### survey-tools-first

**Rule.** Before writing a new tool or starting an investigation, read the header of every tool that already exists.

**Why.** Each tool in `tests/` exists because a measurement went wrong once, and its header says which trap it avoids.
One afternoon re-derived, badly, four things those headers already solved.

**How to apply.** Read the headers of `tests/*.sh` and `tests/*.py`, and the probe index
[tests/probes/PROBES.md](tests/probes/PROBES.md). Extend a tool that nearly fits rather than starting a new one.

### knowns-must-be-proven

**Rule.** Always check that a "known" is actually proven. A known needs its proof (a measurement, a source that was
opened and read, a test), with the date and the conditions it was made under. Without proof, it is an assumption: say
so, and find the cheapest test that would settle it.

**Why.** The human called it "an important one we established very early", and restated it on 2026-10-02 about the
iPhone used as the party app's camera. Its "known flaws" were no wide 0.5x lens, a low frame rate and a long delay.
Checked one by one, they came apart:
- **The lens:** proven, and more firmly than believed. The Mac's own camera interface has no zoom or lens controls at
  all, so it is the computer's limit, not the phone's.
- **The frame rate:** proven, but only for that phone on that macOS.
- **The delay:** measured over a USB cable only. Wi-Fi, other phones and other cameras had never been measured.

Beliefs repeated across sessions harden into facts without anyone re-checking them. They steer decisions (buy a camera
or not, keep a feature or not) as firmly as measured ones do.

**How to apply.**
- Before building on a known, or repeating it, find its proof and note its date and conditions. A measurement on one
  device, one OS version or one setup covers that and nothing more.
- If there is no proof, label it as an assumption and propose the cheapest test. A tool that makes the test a
  one-minute job is often worth building: the party app's latency meter turned each untested camera route into a
  single key press.
- In written records, tag claims so their status shows: measured here, a source opened, or judgement.
- When the conditions change (an update, a new device, a different route), re-test. This rule is the general case of
  the next one.

### retest-closed-doors

**Rule.** A negative result about a vendor's capability is dated. Keep the cheap instrument that re-tests it, and
re-run it after updates.

**Why.** The human (2026-09-27): "updates literally update what was previously impossible. If Apple fix 3D pose in the
next update, and we aren't paying attention, we can be blind to it for ever after."

**How to apply.** Record such a verdict with its version and date and with what would change it, and re-run its probe
after each OS or framework update without being asked.

---

## 3. Changing a shader

### variants-not-overwrites

**Rule.** A change that costs render time ships as a new variant file. It never overwrites a shader that works.

**Why.** The human (2026-09-03): "It is not necessarily the case that there is one ultimate shader — there is a shader
for a specific application tuned to a specific application. … We preserve the performance-functionality without
overwriting the usable ones."

**How to apply.**

- Measure render time before proposing to ship.
- A costly change becomes `<name>-<variant>.glsl`, or a switch in its generator.
- Only a change that is free and never worse may replace a file in place, and that must be said explicitly.
- [SHADERS.md](SHADERS.md) says what each variant buys, what it costs and who wants it.

### regression-gate

**Rule.** "Make sure to check for regressions during development. A fix for one thing might break something that was
already working." (the human, 2026-09-06)

**How to apply.**

- Run the FULL ladder for the changed shader against the shipped file, in one sitting, listing losses before gains.
- For an in-place replacement, no case may fall by more than 0.10 dB; otherwise the change becomes a variant.
- Add the real-footage benches, and timing from a file.
- Run `smoke.sh`, which regenerates every generated shader and compares it byte for byte.

### assert-every-patch

**Rule.** After patching a constant into a variant, assert that EVERY changed constant took.

**Why.** The shaders align their constants in columns, so a `sed` written from memory matched some names and missed
others. The render then ran at the default value while the reader decoded at the new one, and a wrong ratio went into a
committed document before it was retracted.

**How to apply.** Patch with a whitespace-tolerant regular expression. Then grep the variant for each new value and
fail if any is missing. When a measured ratio contradicts an exact reconstruction, suspect the scale before the physics.

### generated-pass-traps

**Rule.** The generators rename and clone passes by pattern; a pass added to a base must survive that.

**Why.**

- A pass that binds only one of its level's two luma textures leaves its shifted copy unbound. The shader then fails to
  load, and the pipeline falls back silently.
- A shift that renamed only a pass's own level left reads of a coarser level pointed at the wrong frames: no crash, no
  alarm.

**How to apply.**

- Bind both lumas at every level a pass reads.
- After any base change, regenerate every generated file and smoke each on one translation case and one acceleration
  case.
- The 4K files are the scaler's output (`scale_shader.py`). Change the base, then re-scale; never edit a 4K file
  directly.

### source-of-truth

**Rule.** The GLSL here is the single source of truth. A port to another API translates it with a generator and never
re-implements a shader by hand. A law found on the port's side goes back into the GLSL the same day.

**Why.** Two sides that each change independently drift, and a finding made on one is lost to the other.

**How to apply.** Every translated graph carries the hash of the GLSL it came from. One command checks every place
the two sides touch: the graphs, the frame window, the painting, the scenes and the constants. It runs after any
change on either side, and its verdict is written in the port's record ([METALPORT.md](METALPORT.md)).

### switch-defaults

**Rule.** A switch with two or more positions defaults to the one that works best in most uses: not the most
conservative one, and not the newest.

**How to apply.** Document every switch. Where most uses are ordinary footage, the default follows ordinary footage.

---

## 4. Choosing what ships

### best-shader-for-most-content

**Rule.** For a player, ship the best shader for most content, regardless of cost, as long as it stays within real
time on a typical device (24 to 48 frames per second counts).

**Why.** A player is not a benchmark. A few percent of render time is nothing beside a picture that is right on more
content. The human (2026-09-27): "The synthetic tests are essential, but they also trap extreme edge cases which are
unlikely to be present in real data."

**How to apply.**

- A variant that gains on real content and stays within the ladder's noise elsewhere becomes the default, not a
  setting.
- Offer a toggle only where content types disagree (one gains, another loses).
- Prefer the shader gating itself at run time to a pre-flight scan of the file: nothing may slow the open.

### fit-for-purpose

**Rule.** "A cheaper system that is not fit for purpose is not a valid choice." (the human, 2026-09-29)

**How to apply.** Once a fit method exists, remove the unfit one rather than keeping it behind a toggle. Move its
checks onto the fit method first, then delete the old path.

### quality-tiers

**Rule.** When several candidates are each fit for purpose, performance decides between them. Candidates of nearly
the same cost collapse into the better one, and the rest become quality tiers.

**Why.** The human (2026-10-01), with three candidates that each beat the others somewhere.

**How to apply.**

- Choose the 4K form of a shader by the size of the source, never by hand.
- The highest tier is the default, with an automatic step down in play when the output cannot keep up.
- That step down must not mistake a slow network or a stutter for a slow shader.

### dependency-currency

**Rule.** Keep the key third-party dependency (here FFmpeg and libplacebo) current, as a step of its own, with the full
test tiers.

**Why.** It was found pinned to an old release, and its build script was silently missing components it was meant to
have. FFmpeg's configure accepts a misspelt component name without a word.

**How to apply.**

- Check the upstream releases at the start of any FFmpeg work.
- Upgrade as its own step; never fold the upgrade into an unrelated fix.
- Carry the local patches forward, and run the full ladder after the upgrade.
- Make every build script validate its component names against the sources.

---

## 5. Working in parallel

### orchestration

**Rule.** When work fans out to parallel workers, build any shared stage once, freeze it and version it, and let each
worker differ from the baseline in its own lead and nothing else.

**Why.** Four leads that each built their own copy of a common stage gave four slightly different versions, and no
result could then be traced to its lead. The human: "recognise when it is good to spawn new threads and when it is
essential to wait for all subworkers to return and report."

**How to apply.**

- Plan the barriers: a stage passes its checks before its consumers start.
- Force a sync after a set time; a worker that has not reported is inspected, never waited on silently.
- Parallelise the building and keep the judging central: pre-registration and the adversarial reading of results stay
  with one reader.
- Building a variant behind a switch is reversible exploration. Adopting it as a default is the human's decision.

---

## 6. Keeping the record

### record-failures

**Rule.** Record what failed as fully as what worked, with dates.

**Why.** A refuted idea that is not written down gets tried again. The records here keep a list of what was
refuted so it is not retried.

### pre-register

**Rule.** Write the prediction, and what would refute it, before the experiment runs.

**How to apply.** A dated "pre-registered" paragraph goes in the record before the run, and the result goes beside it,
including when the prediction missed. More than once the miss was the finding.

### where-files-live

**Rule.** Every script that produced a recorded number lives in this repository. Data lives outside it.

**Why.** A number without its instrument in the same tree cannot be reproduced, and a copy kept elsewhere drifts.

**How to apply.** One-off measurements go in `tests/probes/<topic>/` with a row in
[tests/probes/PROBES.md](tests/probes/PROBES.md), written in the same commit as the finding. They find their data
through the `NP_SCRATCH` variable. Write no absolute home paths into anything committed.

### plain-language-summary

**Rule.** [WHAT-WE-BUILT.md](WHAT-WE-BUILT.md) is the entry point for every reader, from the layman to the scientist.
It carries the conclusion in plain words and a pointer; the detail goes in the technical records.

**How to apply.** When a finding changes the story, update the technical record in full first. Then add at most a
sentence or two to the summary, with no dB figures and no variable names.

### credit-derivative-work

**Rule.** Anything taken from another project is credited in the prior-art document of the work it feeds.

### verify-a-restore-target

**Rule.** When asked to restore "an earlier state" by description rather than by commit, confirm the target against a
real reference before restoring.

**Why.** A restore inferred from the story of the conversation picked a commit several fixes too early, and it went
unnoticed through two further commits.

### privacy

**Rule.** No one's name goes into anything published unless that person has chosen to be public: the human
collaborator's name is public (since 2026-10-01), family members' and other people's are not. No account names or home
paths either. Footage from the human's own life, and of anyone in it, is processed numerically and is not viewed by
the model unless the human asks; recordings of other people's children keep numbers only.

**How to apply.** Sweep the tree for the protected names before every commit that touches it. Use `~`, variables or
relative paths in place of absolute ones.

### prize-won

**Rule.** A proof that would win one of the prizes of PRIZE-PROBLEMS.md §1 goes into a document of its own,
`PRIZE-WON.md`, made by whichever party reaches it first. Nothing else goes there. A partial result, however strong,
belongs in PROOFS.md, and a claim still being checked belongs in PROOFS.md's waiting room. It is published as soon
as one other party has reviewed and verified it (the owner's addendum below). The rule binds all three parties:
Cloud, Local and GPT.

**Why.** The owner's instruction, 2026-10-06: "in the unlikely (likely) case that a prize winning proof does shake
itself out of the tree", it is stored in one place that cannot be confused with the rest of the record. A prize is
judged by people outside this project, against its own official wording, so the document must stand on its own.

**How to apply.**
1. **Check the statement first.** Copy the prize's official wording and link (PRIZE-PROBLEMS.md §1 lists them), and
   show that what was proved is that statement, not a near relative. For Rule 30, "from a single black cell"
   against "every finite configuration" matters. For a Clay problem, name which of its official alternatives is met.
2. **Push the candidate at once; publish on one verification.** The git history is the timestamp, and the
   timestamp is the proof of discovery, whoever else was watching. So the candidate is pushed as soon as it exists,
   to PROOFS.md's waiting room, labelled "prize candidate, not yet verified", with a CLOUD-LOCAL.md row asking for
   review. One other party then reviews and verifies it, preferably of the other make: a GPT proof is read by Claude
   (Local first), and a Claude proof by GPT. The moment that reading confirms it, the finder or the reader creates
   PRIZE-WON.md and pushes it immediately, and tells the owner in its session. No further wait.
3. **What the document holds:**
   - the official statement and its link, and the theorem as proved;
   - the complete proof, readable from the page, with every lemma it uses quoted from PROOFS.md by entry;
   - every certificate and script, with the commit that produced it;
   - each independent reading: which party, when, and at which commit. One verification by another party is the
     bar for publishing; the third party's reading, when it comes, is added below it;
   - a Lean formalisation if one is feasible, as Condrey did for period 1;
   - known gaps, a list that must be empty;
   - credit to every party and every source;
   - the owner's decision on submission.
4. **A gap sends it back.** If a reading finds a gap, the claim returns to PROOFS.md's waiting room with the gap
   named, and PRIZE-WON.md keeps a dated line saying so. Nothing in it is quietly deleted.

*Addendum, the owner, 2026-10-06:* "the proof is to be published immediately as soon as it has been reviewed and
verified by 1 other work[er] (a GPT derived prize proof is peer reviewed by Claude Local) - the git is a timestamped
versioning history itself - the time stamp is the proof of discovery regardless of whether anybody else was watching
and stole our work." Step 2 was rewritten to match. Before it, the rule held publication for the owner's word.

### harness-hygiene

A few traps that cost real time, kept here so they are not met twice:

- **Never edit a shell script while it runs.** Bash reads a script as it goes, so an edit shifts the text under it.
- **On an exFAT drive, macOS writes `._` sidecar files.** Every glob that counts files must exclude `._*`; a doubled
  count is the signature.
- **zsh does not word-split unquoted variables.** A loop over `$LIST` can run once on the whole string and report a
  clean result.
- **`a && b` inside a `set -e` script is exempt from `set -e`.** Put one command on a line, each with its own error
  check.
- **A remote job attached to an ssh session dies with the session.** Detach it on the remote side, and watch its log
  from a local loop.
- **Any "take the newest result" step needs two checks:** the result is newer than the start of the run, and it is not
  empty.
- **A remote launch that prints a process id has not necessarily started.** Read its log a few seconds later.
