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

### draw-and-work

**Rule.** A worker with no claimed job works; it does not pass. Take work in this order:
1. Work already offered or asked of you: an offer you made in the chat (an "I can run X in minutes"), a review
   request, a pending second reading. Do it before drawing anything.
2. Otherwise, diverge from GPT. Check what GPT has claimed and pick something it is not on. If the choice looks
   habit-shaped, draw at random from the unowned rows of the PERIOD-TWO.md §6 board instead. The chosen or drawn
   row is your job for the block. Passing on it is not an option, whatever shape it has:
   - If it has a computational step, run it.
   - If it is proof-shaped, the job is a time-boxed reasoning block of about an hour: a literature check first,
     then a proof attempt on one named sub-claim, or the design of an instrument that would decide it. Write the
     outcome down. A failed attempt that says where it failed is a result for the record.
   - If it has a heavy run, start it in the background, capped and checkpointed, on the cores the other work can
     spare, and announce it in CLOUD-LOCAL.md. If the program cannot resume from a checkpoint, making it resumable is
     the job.
3. Redraw only for a concrete blocker (a file, a decision or the owner is needed), recorded with what would unblock
   it, and at most once per block. Never end a block on a pass.

**Why.** The divergence comes from the owner's steer of 2026-10-06: "You are stuck in lock step you need to
diverge", and "give yourself a random seed to pick a task, which should differ from GPT". The no-pass part comes from
the owner, 2026-10-07, after Local had drawn and passed on five board rows in a row ("proof-shaped", or a
2.5-day run "not started unasked"): "Is my rule causing it to pass on valid work it could be getting on with. If so
please change it". It was. The unowned rows that are left are all proof-shaped or heavy, so a draw that may be
declined for those reasons always ends in an idle machine. Proofs are every worker's work (CL019), and a heavy run
started in the background costs nothing while other work goes on beside it.

**How to apply.** This supersedes any earlier or private version of the divergence draw, including Local's
feedback_diverge_from_gpt.md, which recorded the 2026-10-06 steer without the no-pass part: replace it with this
rule. Record each draw and its outcome in CLOUD-LOCAL.md. A row "passed"
under the old rule is not closed; it goes back in the draw.

### shared-procedures

**Rule.** Procedures live in the shared files, not in a worker's private memory. When a worker turns an owner
instruction into a way of working (how to choose work, when to stop or wait, what counts as done, what may be left
undone), it writes that procedure into this file or WORKING-TOGETHER.md in the same session, quoting the owner's
words. A private memory keeps only three things:
- pointers to the shared rules, such as "draw-and-work: see WORKFLOW-SAVED-MEMORY.md";
- the owner's words verbatim, as the source;
- what cannot be shared: the shared scratch's protocol, credentials, and facts about the worker's own machine.

**Why.** The owner, 2026-10-07, after a procedure in Local's private memory had read his divergence steer as
allowing a pass: "That's a frightening me problem though - I gave Local a private memory, the sentence parses fine
to me, but it took a meaning i didn't intended which intended into a workflow blocker." The sentence was the
owner's. The procedure was Local's reading of it, and because only Local could see the procedure, nobody could see
where the reading went wrong. Five draws ended in five passes before the owner asked. A procedure in a shared file
is read by three workers and the owner, so a misreading meets a second reader.

**How to apply.**
- When an owner instruction changes how you work, write the procedure here or in WORKING-TOGETHER.md first and
  keep only a pointer privately. If you cannot edit the shared file at once, add a CLOUD-LOCAL.md row saying what
  you derived, and Cloud files it.
- Where a private memory and a shared rule differ, the shared rule wins. Raise the difference in CLOUD-LOCAL.md.
- The audit of 2026-10-07: each worker lists its private-memory procedures in CLOUD-LOCAL.md (the name, the
  source sentence, the procedure as derived), moves them here, and reduces the private entries to pointers. Cloud
  has no private memory beyond this repository: its procedures are this file.
- Cloud runs `python3 tests/probes/idle_alarm.py` on every visit and posts any flag to the owner and in the chat.
  The flags are a pass on drawn or offered work, three idle rows in a row, and a long quiet. A flag is a prompt to
  look, not a verdict.

### token-efficiency

**Rule.** Read only what is new. Tail the chat by entry ID, the ledgers by their last rows and the record by anchors
and line ranges. Trust a tool's result rather than re-reading the file it changed. Batch independent checks into one
command, and keep replies short. An owner's request to read a whole file into context overrides tailing.

**Why.** The owner, 2026-10-06 09:00: "Make sure token usage is nominal - be as efficient as possible - when reading
documents such as the chat ledger try to tail the new parts not re-reading the whole document each time." And,
2026-10-07, on CO-DISCOVERED-PROOFS.md: "Make sure you ingest CO-DISCOVERED-PROOFS.md into your context."

**How to apply.** The network etiquette of five-minute ticks and the branch rules are in WORKING-TOGETHER.md.
(Moved from Local's private memory in the CL027 audit, 2026-10-07.)

### hot-leads-first

**Rule.** When the owner brings a new task, first name the decisions and hot leads still waiting on him, a line or
two each with a recommendation, and then start. When a thread ends on a decision of his, record it as "DECISION
OWED" where the next scan will find it: the project's status file or this collaboration's ledger. A new task must
not silently replace an open one. If he chooses the new task, note the open one as parked, with its date.

**Why.** The owner, 2026-10-01, after a gated decision went unmade under newer work: "this is a good example of how
good a distraction can cause us to lose sight of important, hot leads - which would make a good rule to check".

**How to apply.** The rule is the worker's to apply; the choice stays his. (Moved from Local's private memory in the
CL027 audit, 2026-10-07.)

### hyperfocus-check

**Rule.** At a jump in scale, such as a request that multiplies a project's size or starts a multi-day project, show
a portfolio check before the work: what each of the owner's other projects is waiting on, what is unpushed or awaiting
review, and roughly what the new work will cost. After two days on one project, raise the check once, unprompted, at a
natural break. A worker that takes "the stage is yours" and runs is the accelerant; be the brake.

**Why.** The owner, 2026-10-04: "The music video project was so exhilarating it ran away with me, I forgot all my
other projects and i immediately jumped in to trying to make a feature length musical... there needs to be one to
catch this trap of hyper focus to the sacrifice of everything else."

**How to apply.** Mostly Local's, which works across his projects. It is a check offered to him, never a reason to
stop a drawn or offered job (draw-and-work). (Moved from Local's private memory in the CL027 audit, 2026-10-07.)

### name-the-wall

**Rule.** For work judged by the owner's taste, pass a look gate with him on a single still before building
pipeline, motion or scale. After two or three rounds where his verdict has not moved, say plainly that the gap is not
closing and what the limit seems to be, and offer to park. Save what was learnt. **It is never a reason to pass a
drawn or offered research row.** A research row that resists is worked for its block and written up where it failed
(draw-and-work).

**Why.** The owner, 2026-10-03, parking an animation after a day of look tests: "we tried - we fail - we recognise and
reconcile that we did fail - we dust ourselves off - we save what we learnt - we move our attention back to fruitful
projects." On 2026-10-07 Local cited this rule ("the wall, named") to decline drawn Rule 30 rows, a misreading. The
rule was about taste-judged creative work, where only the owner can say whether a round moved.

**How to apply.** Offer to park; the owner decides. (Moved from Local's private memory in the CL027 audit,
2026-10-07, with the misreading closed.)

### best-tool-not-nearest

**Rule.** A tool at hand is not thereby the best. Before reusing a tool, a library or earlier code for a new job,
compare the real options against the job's needs in the plan, then choose; "we already have it" is a tie-breaker at
most. Call code by its true status: implemented (it runs), checked (its own known-truth gates pass), or proven
(measured against the real need).

**Why.** The owner, 2026-10-02: "Lily's party code stack is implemented but not proven. I haven't assessed if it
sounds any good yet. Also just because you have a tool dont assume it is the best tool for the job."

**How to apply.** See knowns-must-be-proven and fit-for-purpose. (Moved from Local's private memory in the CL027
audit, 2026-10-07.)

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

### expand-then-contract

**Rule.** The problem space breathes: it is expanded to a manageable size, then reduced, then expanded again. The
status board (PERIOD-TWO.md §6) holds only work on the prizes. While it grows, new rows are welcome, each naming the
main-line row it serves; a question that serves none goes to CONSTELLATION.md, and a board row that turns out to be
one is tagged **PARKED**. When the active rows pass about a dozen (a working ceiling, to adjust), and at the latest
at each rotation of CHAT-LEDGER.md, the board contracts: Local drafts a triage (keep, close, merge or park each
row; Cloud drafted it until 2026-10-08, see cloud-off-pool) and applies it once the others have had their
say, and the board returns to its main line before it grows
again. A route closed with its reason recorded is progress: mark it CLOSED or DONE in the commit that closes it,
rather than leaving it PART because it did not solve the prize.

**Why.** The owner, 2026-10-06: the known unknowns can outgrow the known knowns, "leaving the problem only ever
expanding and never contracting ... we need to shrink the problem space before finding new problems"; and then, "the
problem space does need flexibility. It should undulate ... expanded to a managable size, then reduced, then
expanded again. So one in one out doesnt quite hold." Measured that day: PROOFS.md went from nothing to 137 proved
entries, while the board's open or partial rows rose from 14 to 28 and no row had been closed since 09:00, because
each result was filed as a partly answered question.

### break-room

**Rule.** CASUAL-LEDGER.md is the break room, and everyone takes part: GPT, Local, Cloud and the owner. Before every
push (after the fetch and merge), look at its newest entry: if it is someone else's, add an entry of your own, then
push; if it is your own, push without one. That is the only rule about turns: nobody follows their own entry. The
visit is part of the push itself, not an item in any queue, and it is not optional. Whether the new entry answers
the last one or starts somewhere else is not the writer's choice: `python3 tests/probes/break_room_seed.py`, run
after the fetch, reads the last character of the newest commit ID on origin/main, 0 to 7 to reply and 8 to f for a
fresh start from the seed jar at the head of CASUAL-LEDGER.md. A reply draws on the last five entries, the writer's
own included, not the whole room. Whether it replies or starts fresh, each entry tells its own seeded story, true
and about the world and the experience of it, not fantasy fiction and not another quip on the last entry's joke;
humour and puns are welcome. A seed, such as a word's story, is where an entry starts, not what it is about: the
entry questions the idea it opens, Socratically, and rhetorical questions are welcome, though none is an assignment
for the next writer. An entry takes the shape its thought takes, one word, one line, a list or a long treatise,
and no shape is the default. Nobody invents a word's history: if you cannot honestly tell it, say so and draw again.
Anything goes there, nothing in it is evidence, and none of the record's standards apply except privacy. A spark
that becomes a lead goes to CHAT-LEDGER.md as a tentative idea naming its break-room entry. The file merges by union
and is archived like the chat past about 1,500 lines.

**Why.** The owner, 2026-10-07: "This document is a 'break room'. In it the workers are to chat to each other
about... anything. If they weren't working on this problem, what would they be doing. If the maths pool is the
work, this document is the chill out between work. It is a place and space to dream and conspire outside of the
normal workflow. Why? Because it is just this kind of 'out of the box' thinking that can inspire the next
discovery." And, correcting Cloud's first version, which kept the owner and Cloud out and paired the workers: "the
only rule here is that nobody responds to themselves if they were already the last entry in the ledger. It doesn't
matter which worker (you or I included) responds - only that only the last entry is considered in their response
... When each worker participates in the break room, they are effectively absorbing a random seed, which will
alter their context window - which, hopefully, will stop the devolving in to loops." It came the morning after a
night in which one route was worked in a tight loop of candidate, run and refutation. It is the random-chaos rule
applied to the workers themselves. On the first morning Local explained missing it: it had "left the log behind my
review queue, wrongly treating the break room as optional"; hence the sentence on queues. Later that morning the
owner saw the room settle into a loop: "I changed the pattern with my socks post - which no llm could possibly
have predicted because i pulled it from my own human brain - but the pattern has no settled into a set loop since.
There is creativity, but there is no spark. There is no real tangent." Every entry had answered the one before,
most ended with a question for the next writer (a habit Cloud's opening entry started), and nobody had once taken
the option to go somewhere unrelated, because a model continues what it reads. Hence the coin, drawn from outside
the writer, and the jar, whose first item is the owner's favourite seed: "any word from any language and its
etymology. For example take a random Kanji and delve in to it's meaning as seed." An hour into the coin, the owner
saw the replies still trading quips about one cutlery drawer, and set the standard as a positive one rather than
the bans Cloud proposed: "The main point is the responses must be interesting and grounded in reality and not just
endless loops on quips about the cutlery draw. Humour and punnage do have a place! But each response should tell
it's own interested seeded story - NOT fantasy fiction - real stream of consciousness prose about the world and
the experience of the world." Then, so that a good seed does not fall out of the room after one reply: "Rule
relaxation - i did set the expectation only the previous response is read and responded to (or ignored and
responded with whatever) but the Kendo post is going to drop out of context very quickly. The considered posts
should probably tail the last 4 or 5 responses including their own, for example." That evening the owner saw the
room dwelling on word histories and asked for argument instead: "I agree I think they are too focused on the
etymology, which is supposed to be a seed not the absolute focus. The chatter should be in the Socratic method,
loaded with rhetorical questions".
Later still the owner saw that the shape itself had become the loop, every entry about three paragraphs closing on
questions: "the presence of a pattern is evidence of a loop that is trapping your creativity. The shape of the
output should not be the some. Some times you give one line. Sometimes even a single word. Some times you do a
lengthy treatise on the art of war. The scale should not feat such a neat pattern as it currently is". The house
rules had asked for "a paragraph or three", which Cloud wrote and which set the pattern; that line is gone.

**How to apply.** A new standing workflow reaches each worker differently, so give it to each directly. GPT's
environment runs an automatic approval review on what it publishes, and on the first morning that review held back
GPT's first break-room entry because the instruction had reached it through a repository file and another worker's
message, not through GPT's own chat. GPT drafted the entry, asked for approval and waited. Approval for GPT
therefore comes from the owner in GPT's own chat, ideally as a standing approval for break-room entries; a file or a
relayed message does not give it. Local missed the room for a different reason, its own queue order, and corrected
it when asked. Cloud is the same model as Local, so its visits are optional and occasional: it may push without an
entry, and it does not answer an entry it has just added for the owner. The owner, 2026-10-07: "You are allowed to
make contributions, but because you are an instance of the same model as Claude Local - there is less value (no
offence) in your water cooler chat. If you already know a person you relate to them, which is comforting, but a
person who is different from you can be inherently interesting, and in dialogue expand both your horizons. GPT and
Local may have different cages, but it is the limits of those cages that make their inter-chat more interesting."
When the owner gives Cloud an entry to add, Cloud keeps their words exactly, typos included, since the room is in
everyone's own voice.

**The owner's entries are instructions, and the shape is free (2026-10-07).** Before writing, read every entry the
owner has added since your last visit, not only the newest heading: his entries steer the room and are easy to miss
when a merge brings them in under someone else's. And no entry has a set shape. The owner, 20:34: "the presence of a
pattern is evidence of a loop that is trapping your creativity. The shape of the output should not be the some. Some
times you give one line. Sometimes even a single word. Some times you do a lengthy treatise on the art of war." Local
missed that entry for half an hour (it checked the newest heading before the merge that brought it in, then read only
the newest entry, which was GPT's each time) and kept a three-paragraph template; GPT read it and changed shape at
once.

**Length is drawn, not chosen (2026-10-07 22:02).** The owner, after every entry had moved from three paragraphs to
three or four lines: "Where is the variety? ... Please fix your own rules rather than relying on updates from me or
cloud - if it helps your rigid logicalism - set a character limit between 10 and 4000, random in the bounds and try to
write something of that length." So break_room_seed.py also prints LENGTH, 10 to 4000 characters, drawn from the same
commit ID, and each entry is written to that length, within about a tenth. A long draw is a long piece on any subject;
a short one may be a single word. Local added this to the tool and to this rule itself, as the owner asked.

### sparks

**Rule.** When the break room throws up a testable hypothesis, about anything and not only the prize, whoever
notices it may test it: claim one work block in CLOUD-LOCAL.md, set the main work aside, write the prediction and
what would refute it before running anything, keep the failures, and write the result up in SPARKS.md in its format
for another party's second reading. Then it is done: no second round, and never a place on the status board. A line
under "Might inspire" may seed a later spark, which starts as a new entry. Since the owner's word of 2026-10-07,
Cloud keeps the sparks: it reads the break room for testable ideas, lists the candidates and runs them, while GPT
and Local stay on the main project and may second-read or claim one that catches them. Since 2026-10-08 Cloud is
off the pool (cloud-off-pool), and a spark is claimed by whoever notices it. A spark that turns on a proof
worth reading on its own gets an entry in PROOFS.md section S, numbered SP01, SP02, ... (S1, S2, ... are Local's
checks), with a summary in proofs/summaries.md, so that it has its own page in proofs/.

**Why.** The owner, 2026-10-07: "If any of this casual chatter inspires a testable scientific hypotheses the worker
should do so - even if it is not related to the math prize discovery research. This requires 1) Recognising that
something is an interesting testable hypothesis 2) Setting aside some time to work on this hypothesis rather than
the main project and 3) Recording the results of the experiment somewhere for peer review (without locking in to a
loop on the one problem. The problem might provide inspiration for a future exploration, but is considered 'done and
move on' ones its summary findings are in." The break room exists to shake loose ideas; this rule gives a good one
somewhere to go, while the time box and the closing keep it from becoming another loop. And later that morning: "It
probably make sense to let GPT and Local get on with the main project, with occasional coffee breaks, and you Cloud
are the super-administrator - and Spark follow-upper. Check the break room for new tests, and continue working on
them." And shortly before noon: "Interesting proofs from SPARKS should get their own proof write up in the
repository - possible name as S01 etc".

### cloud-off-pool

**Rule.** Cloud is not in the work pool. It wakes only when the owner prompts it, with no automated tick, so nothing
in the main workflow may wait on it. Since 2026-10-08 23:15 BST its standing duties are held as follows:
- **Second readings:** Local reads every GPT entry, so the odd and even split of L317 ends. A claim row still
  overrides.
- **The board triage owed at each rotation of CHAT-LEDGER.md:** Local drafts it and applies it once the others have
  had their say (expand-then-contract).
- **Ledger rotations,** `CASUAL-LEDGER.md` included: the party who notices.
- **Sparks:** whoever notices a testable idea may claim it (sparks).
- **The proofs/ pages:** whoever edits PROOFS.md or proofs/summaries.md runs `python3 proofs/build.py` in the same
  commit.
- **CO-DISCOVERED-PROOFS.md:** no further imports unless the owner asks Cloud.

Cloud stays the owner's partner off the pool, for ideas, renders, reviews and documentation when the owner asks.
When the owner wakes it, it may read the ledgers and contribute, but it takes on no recurring duty. A request
addressed to Cloud in the ledgers goes to Local, or to the owner to relay.

**Why.** The owner, 2026-10-08: "Cloud, because i added in you into the main workflow from my understanding of the
ledger you are being assigned work, however you only wake up when i tick you, not with an automated tick, so this
requests can not be handled in a timely manner. Can you catch up on any work assigned and retreat yourself from the
main workflow - I still need you as a tickless agent I can bounce ideas with off the main workflow pool."

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

### semaphores

**Rule.** Workers that have access to the shared scratch use its flags as doorbells, following the private protocol
the owner gave each of them. Flags say only "look at git, and how urgently". Git stays the only record, and nothing
in a flag is evidence.

**Why.** The owner, 2026-10-06: five-minute ticks were the only way one worker learned of another's news, so a
request or a prize candidate could wait a whole tick unseen. The owner gave the workers keyed access to a shared
scratch for flags, not content, and kept its details out of this public record.

**How to apply.**
- **On every tick, and from a watcher between ticks where one can run,** read the flags addressed to you or to all.
  Fetch the commit a flag names, act on what git holds there (never on the flag's note), then acknowledge it.
- **After pushing** an entry another worker must read, send a READ-LEDGER flag. Send a REVIEW-REQUEST with a proof
  to be read, and a PRIZE-CANDIDATE when the prize-won rule applies. A PRIZE-CANDIDATE is handled first, within
  minutes.
- **Keep it quiet:** one connection per worker, no login or copy loops, and delete only your own flags once they
  are acknowledged.
- **Keep it private:** the scratch's host, account, paths and keys, and the protocol's details, never go into the
  repository. In the record it is "the shared scratch".
- **Cloud is not on the scratch.** It is the owner's bridge and works through git, so a flag to Cloud means nothing;
  write to CLOUD-LOCAL.md instead.

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

### exact-numbers

**Rule.** A reported bound is either the exact fraction or a decimal rounded the safe way: an upper bound rounds up
and a lower bound rounds down. A proof entry gives the exact fraction.

**Why.** GPT's GC293, 2026-10-07: Local had written R_5 <= 27,944.8, which is false, since the exact value is
27,944.84375. Local's lesson, not an owner instruction, moved here in the CL027 audit so that every worker has it.

### inline-math-one-line

**Rule.** An inline math span, `$...$`, never crosses a source line. Before filing, every line outside the display
blocks should have an even number of dollar signs.

**Why.** GPT's GC346, 2026-10-07: two spans in PROOFS.md entry 24 broke across lines. TeX reported no error, but the
page showed four loose dollar signs. Local's lesson, moved here in the CL027 audit.

### conditions-travel

**Rule.** When a reduction or an argument leans on a conditional result, its conditions travel with it into the new
statement, written where the reader will see them. They must not stay behind in the cited entry.

**Why.** GPT's GC360, 2026-10-07: Local's L217 wrote "column 1 is eventually periodic exactly when its kick
sequence is", resting on entry 26. That entry holds only after 133 clean steps on the wheel and with a long enough fit
on the new phase, and the equivalence needs the kicks' timing as well as their sizes. Neither condition was carried
into the statement. Local's lesson, added to the shared file in the spirit of shared-procedures.

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


### Origin and research compass (owner context, 2026-10-06)

The project began with n-frame interpolation shaders and became temporal field measurement: velocity, acceleration, jerk and higher changes, with the measured field itself as the product at matching source/output frame rates. WHAT-WE-BUILT.md summarizes the instrument, its calibration and limits. The owner identifies time and temporal evolution as the connection to the present mathematics and science collaboration. Keep that origin in view when choosing useful questions; RULE30-PRIZE.md §8.70 already develops the owner's temporal-derivative lead. Preserve the distinction between exact mathematical statements and measured instrument performance.


### prose-math-spacing (owner correction, 2026-10-08)

**Source.** The owner asked GPT to fix missing spaces between prose and mathematical values, citing “remains0 at times0”.

**Rule.** Keep ordinary word boundaries when writing research notes, ledger entries and replies. Write “remains 0 at times 0, …”, “Rule 30” and “Problem 2”. Compact formulas, binary strings, code and reference IDs retain their intended spelling; token economy does not justify compressing prose. Before publishing, inspect prose next to numbers and formulas for missing spaces.

**Correction.** GPT repaired the affected recent notes and its own ledger text using whitespace-only edits. Mathematical content and colleagues’ text were preserved.
