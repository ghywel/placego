#!/usr/bin/env python3
"""SW-02 builder: Wave 2 briefs. Questions come from the design's §8 (struck text removed); known inputs come from DATA/known/<ID>.md,
which Local writes from Wave 1's facts and Cloud's review §2. Attack agents read the pre-design export; the design is withheld."""
import json, re, sys
from build_common import *

DESIGN = os.path.join(HERE, "..", "..", "..", "..", "reports", "SW02-SWARM-DESIGN.md")
FABLE = {"AM-1", "AM-4", "CP-1", "CP-5", "HX-1", "HX-2", "CT-1", "CT-3"}
PILOT = ["AM-1", "AM-4", "CP-1", "HX-1", "P2-2"]

RIGOUR = """
## What a proof-shaped return carries

1. **Statement**, with its quantifiers and its population named. 2. **Dependencies**: kit theorem names at the pin, each with its hypotheses checked, or a primary source with its section.
3. **Proof** in numbered steps, the step that carries the result marked. 4. **Smallest cases**, computed with `ref.py` through the queue. 5. **Proves-too-much check**: what does the same proof say
about rules 90, 150 and 210, about the ether, about a random word? 6. **Status**, and whether the result is known. 7. **Bridge and limits**: the exact implication to the intended target, every
quantifier and limit exchange, what is still missing; fixed or growing width, physical or surrogate input, seed or almost-every input. 8. **Failure artifact**: an exact witness for a refutation, a
parameter box and a reason for an inconclusive search. A missing argument is unjustified. Absence of a found witness is not a theorem. 9. **Verification**: which checks actually ran, with controls.

A barrier must give a mathematical class (observation map, certificate syntax and semantics, ranking range and order, or oracle access), the target and a quantified impossibility, never "all ideas".
An accepted intermediate lemma need not solve any prize. A conditional bridge is useful if its hypothesis is weaker, more testable or more structural than the target, with that comparison explained.
"""

FILES = """
## What to return, and files to write in your folder (use a Bash heredoc for files)

- **Your report goes in the manifest's `report` field, as full text, not in a file** (sub-agent tools refuse report files). Open with the known inputs restated in your own words, then your candidate statement, then the attack and what came of it. A clear negative is a full answer. Write everything needed for a reader who sees nothing else, up to about 4,000 words.
- `claims.jsonl`: at most three headline claims, one JSON object per line. Fields: `claim` (title), `statement` (fully quantified), `population`, `frame`, `status`, `carrying_step`, `proof_at` (section of
  your report), `known_matches` (what you searched, under which names, and what you found), `gates` (which of the theorem-scoped gates in TERMS.md §6 apply and how), `bridge` (the exact implication to a target,
  or "none claimed"), `first_falsifier`, `smallest_cases`, `kill_test`. If you have no claim, write an empty file and say why in your report.
- `requests.jsonl` (optional): tests for Local's queue that exceed your allowance. Fields: `test`, `prediction`, `counterfactual`, `positive_control`, `negative_control`, `cost_estimate`, `script` (a file in your folder), `record_searched`.
- `questions.jsonl` (optional): `question`, `why`.
"""

ATTACK = """# SW-02 task {{ID}}

**Your question.**

{question}

**Known inputs.** What the record already holds on this question. Restate these in your own words at the top of your report, then build on them. You may not report one as a finding: a new proof of one is "known, reproved here".

{known}

**Your materials.** `{{SW}}/TERMS.md` (read it first: definitions, aliases, gates), the record export at `{{REC}}`, the kit at `{{KIT}}`, the portal snapshot, the PR snapshot. You may read primary literature with `WebSearch` and `WebFetch` (load them with ToolSearch, `select:WebSearch,WebFetch`).

## What to do

1. Restate the known inputs, briefly.
2. Write the fully quantified candidate you are testing: population, parameters, input facts, desired conclusion and first falsifier. A survey or classification question may instead return a precise finite comparison table.
3. Attack it. Smallest cases first. Try to falsify your own candidate before you try to prove it.
4. Before calling anything new, search the record, the kit and the portal under every name, and read the exact source. A literal miss is not absence.
5. Stop when you have a result, an obstruction stated exactly, or your budget is used. If you find a better question than the one you were given, answer that too, and say so.

**Budget.** About 120 tool calls and 120 CPU seconds through the queue.
""" + RIGOUR + FILES

LENS = """# SW-02 task {{ID}}: lens

**Role.** Propose one mechanism with grip on one object, from a primary source in your field. Say which theorem-scoped gates apply. Write the smallest discriminating test; a test beyond your allowance goes in `requests.jsonl`.{unforced}

**Your field.** {field}

**Your locus of interest.** {locus}

**Known inputs.** What the record already holds near your locus. Restate these in your own words, then build on them. You may not report one as a finding.

{known}

**Your materials.** `{{SW}}/TERMS.md` (read it first), the record export at `{{REC}}`, the kit at `{{KIT}}`, the portal and PR snapshots, and the web through `WebSearch` and `WebFetch` (load them with ToolSearch, `select:WebSearch,WebFetch`). Read the primary source; do not name a precedent from memory.

## What to do

1. Find the one object in this problem your field can grip, and the theorem or technique that grips it. State that theorem exactly, with hypotheses, from the source.
2. Write the fully quantified statement your mechanism would prove, and where the mechanism would use something specific to Rule 30, to finite support, or to period 2.
3. Try to break it yourself: smallest cases, the sibling rules, the ether, a random word.
4. Search the record under every name before calling it new.

**Budget.** About 100 tool calls and 120 CPU seconds through the queue.
""" + RIGOUR + FILES

FRESH = """# SW-02 task {{ID}}: fresh eyes

Read the one page at `{{SW}}/FRESH.md`. You are reading it as {persona}. It is all you get: do not open any other file in this project, do not search the project's record, and do not look the problem up
on the web. Your value here is that you have not seen the work done on it. Think about the problem as you would if a colleague had put it on your desk.

Say what strikes you: what it resembles, what you would try first, what you would compute, what you would conjecture, where you think the difficulty really is. Prove what you can. You may run small
computations: write a script in `{{OUT}}` and run it with `python3 {{SW}}/q.py --task {{ID}} --cpu 30 --wall 60 -- python3 {{OUT}}/script.py`. Jobs have 120 CPU seconds in total. In a script you may use
`sys.path.insert(0, '{{SW}}'); import ref` for F, G and S, and nothing else from this project. Write only in `{{OUT}}`.

Make no claim of novelty and no claim that an approach cannot work: that is for a later reader. Write `claims.jsonl` in your folder (with a Bash heredoc) with at most three statements you would stand behind, each with
`claim`, `statement`, `status` (proved, computed, conjecture), `proof_at`. Then return the manifest through StructuredOutput: `id`, `outcome`, `files`, `summary` (at most 120 words), `counts`, `unforced`, `not_done`,
`prize_level_claim` (true only if you believe you have answered the page's question; assume first that you are wrong), and `report`: your thoughts as full text, in the order they came. Sub-agent tools refuse report files, so the report goes there.

Budget: about 80 tool calls.
"""

OUT1 = """# SW-02 task {{ID}}: drafter

**Role.** Draft a one-page statement of the integer problem for mathematicians, with a list of possible venues. **Locus:** clarity for an outsider. Nothing leaves the repository; the owner alone decides what happens to this.

Read `{{SW}}/TERMS.md` §4 and `{{SW}}/FRESH.md`, and use the record at `{{REC}}` and the kit at `{{KIT}}` to get every stated fact right, with its status. The page says what the problem is, why it matters (what it implies for
Rule 30's period-2 question, and how it relates to the prize), what is proved, what is computed, what has been tried, in plain mathematical English, with no claims beyond their status. Credit the kit's contributors and Condrey where due.

Write, with Bash heredocs, `page.txt` (the one-page statement) and `venues.txt` (where such a problem could be put before mathematicians, with what each venue expects; read each venue's rules on the web and do not post anything). Put what you left out and why in the manifest's `report` field.
Budget: about 60 tool calls.
"""

PERSONAS = {"FE-1": "a number theorist", "FE-2": "a combinatorialist", "FE-3": "a physicist who works on cellular automata and disordered systems", "FE-4": "a theoretical computer scientist"}


def questions():
    s = open(DESIGN, encoding="utf-8").read()
    w = s[s.index("### Wave 2: squads"):s.index("### Wave 3: refutation")]
    w = re.sub(r"~~.*?~~", "", w, flags=re.S)
    items = {}
    for m in re.finditer(r"(?ms)^- \*\*((?:AM|CT|CP|PE|P2|P3|BR|XP|HX)-\d)[^\n]*?\n?.*?(?=^- \*\*(?:AM|CT|CP|PE|P2|P3|BR|XP|HX)-\d|^#### |\Z)", w):
        txt = m.group(0).strip()[2:]
        # known-input paragraphs in the design are carried by the known file, not the question
        txt = re.split(r"\*\*Known inputs? \(Cloud, draft 3[^*]*\*\*", txt)[0].strip()
        items[m.group(1)] = re.sub(r"\s*\n\s*", " ", txt)
    lens = {a: (b.strip(), c.strip()) for a, b, c in re.findall(r"^\| (LN-\d\d) \| ([^|]+) \| ([^\n]+?) \|$", w, flags=re.M)}
    return items, lens


def known(i):
    p = os.path.join(DATA, "known", i + ".md")
    return open(p, encoding="utf-8").read().strip() if os.path.exists(p) else "(None listed; search the record.)"


def build(ids):
    items, lens = questions()
    tasks = []
    for i in ids:
        if i in items:
            write_task(i, ATTACK.replace("{question}", items[i]).replace("{known}", known(i)), REC_PRE)
            t = {"id": i, "effort": "max" if i in FABLE else "xhigh"}
            if i in FABLE:
                t["model"] = "fable"
        elif i in lens:
            unf = " You need no bridge to a prize: this slot is for what the field can see." if i in ("LN-03", "LN-04", "LN-09") else ""
            write_task(i, LENS.replace("{field}", lens[i][0]).replace("{locus}", lens[i][1]).replace("{known}", known(i)).replace("{unforced}", unf), REC_PRE)
            t = {"id": i, "effort": "xhigh"}
        elif i in PERSONAS:
            write_task_fresh(i, FRESH.replace("{persona}", PERSONAS[i]))
            t = {"id": i, "effort": "xhigh"}
        elif i == "OUT-1":
            write_task(i, OUT1, REC_PRE)
            t = {"id": i, "effort": "high"}
        else:
            raise SystemExit("unknown id " + i)
        tasks.append(t)
    return tasks


def write_task_fresh(i, text):
    os.makedirs(os.path.join(DATA, "tasks"), exist_ok=True)
    os.makedirs(os.path.join(DATA, "out", i), exist_ok=True)
    body = text.replace("{{SW}}", SW).replace("{{OUT}}", os.path.join(DATA, "out", i)).replace("{{ID}}", i)
    open(os.path.join(DATA, "tasks", i + ".md"), "w", encoding="utf-8").write(body)


if __name__ == "__main__":
    name, ids = sys.argv[1], sys.argv[2:]
    b = write_batch(name, build(ids), 8)
    print(name, len(b["tasks"]))
