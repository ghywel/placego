#!/usr/bin/env python3
"""SW-02 builder: Wave 3. `screen NAME TASK... -- IDS`: a screener over the claims of the listed Wave 2 tasks.
`skeptics NAME`: from DATA/state/selected.jsonl (Local's list after screening), a record and a mathematics skeptic for each selected claim."""
import glob, json, sys
from build_common import *

SC = """# SW-02 task {{ID}}: gate and statement screener

**Role.** Read each claim below with its source report, and classify it. **Locus:** the claims of tasks {tasks}. You are the first adversarial reader. Compare title, quantified statement, proof and intended target; statement fidelity is mandatory: a claim whose proof does not prove its
statement is not a candidate as stated. Read `{{SW}}/TERMS.md` (definitions, aliases, gates), and the design's §5, §6, §8.0 and §11 at `{{REC}}/reports/SW02-SWARM-DESIGN.md`. Each task's report is at `{{DATA}}/out/<task>/report.txt`, its claims at `claims.jsonl`, and its scripts beside them.

For each claim give one class:
- **KNOWN**: the kit, the record, the portal or the literature holds it; cite the matching name, using TERMS.md §4a. A known input from the brief reported as a finding is KNOWN.
- **REFUTED**: give the exact witness or the false step. Test it through the queue where you can.
- **UNJUSTIFIED**: a step is missing; name it.
- **INCONCLUSIVE**: a bounded search with its parameter box and no theorem.
- **OUT OF SCOPE**: not about the problems at hand.
- **CANDIDATE**: valid as far as you can see, and worth a skeptic. A valid narrow lemma with no prize bridge is a candidate.

A theorem gate rejects only by matching its exact hypotheses: name them and the failed step. Gates 4, 6, 8 and 9 are diagnostics and reject nothing. CT-4's bound limits one unsigned estimate; it shuts nothing else. An uncertain case goes to a skeptic. Merge claims that are one statement under two names.

Write `screen.jsonl` in your folder (Bash heredoc), one object per claim: `claim_id` (task id and claim number, as AM-1.2), `title`, `class`, `reason`, `cite_or_witness`, `fidelity` (does the proof prove the statement, and is the title true to it), `gates`, `merge_with`, `rank` (1 to 5, how much a skeptic's time is worth: consequence and novelty), `bridge` (the claimed bridge to a target, or none). Put your overview in the manifest's `report` field. Budget: about 100 tool calls.

## The claims

{claims}
"""

SKR = """# SW-02 task {{ID}}: record skeptic

**Role.** Default unverified. Has this been done, closed or renamed? **Locus:** one claim, below. Search the record at `{{REC}}` under every name in `{{SW}}/TERMS.md` §4a and every name you can derive; the kit at `{{KIT}}` by exact statement; the portal (`{{DATA}}/portal/INDEX.md` and `src/`); the PR snapshot (`{{DATA}}/kit-prs/PRS.md`), including closed PRs and review bodies; and the survey's cards in `{{DATA}}/out/*/doors.jsonl`. Use the web for the literature where the claim's shape suggests a known theorem. A literal miss is not absence: read exact sources. A result is known once its hypotheses and conclusion match.

Write `verdict.json` in your folder (Bash heredoc): `claim_id`, `verdict` (KNOWN, PARTLY KNOWN, CLOSED ROUTE, ALIAS, or NOT FOUND AFTER SEARCH), `matches` (each with name, location, and how hypotheses and conclusion compare), `searched` (the terms and places), `confidence` (0 to 1), `note`. Put your reasoning in the manifest's `report` field. Budget: about 70 tool calls.

## The claim

{claim}

The task's report is at `{{DATA}}/out/{task}/report.txt`.
"""

SKM = """# SW-02 task {{ID}}: mathematics skeptic

**Role.** Default unverified. **Locus:** one claim, below. Find the first false step or the first unproved one, and keep those apart. Check domain, limits, boundary conditions, quantifier order, the frame and the population, and the smallest cases, by computation through the queue. Check whether the proof proves too much: rules 90, 150, 210, the ether, a random word. Read the statement and proof at `{{DATA}}/out/{task}/report.txt`, with `{{SW}}/TERMS.md`, and its cited Lean statements in the kit at `{{KIT}}`. Accept a valid narrow lemma even if no prize follows. If the proof fails but a weaker statement holds, state it and prove it.

Write `verdict.json` in your folder (Bash heredoc): `claim_id`, `verdict` (VALID, VALID WITH REPAIR, UNPROVED, or FALSE), `first_bad_step`, `witness` (for FALSE), `repaired_statement`, `smallest_cases`, `carrying_step` (the one step a second reader should check), `confidence` (0 to 1), `note`. Put your reasoning in the manifest's `report` field. Budget: about 80 tool calls, 120 CPU seconds.

## The claim

{claim}
"""

RS = """# SW-02 task {{ID}}: rescuer

**Role.** A claim died, but a reader judged it interesting. Can a weaker true statement be saved? **Locus:** the claim below, its report at `{{DATA}}/out/{task}/report.txt`, and its verdicts at `{{DATA}}/out/SK-*/` for this claim. State the strongest statement that survives the objections, prove it or say what is missing, and say what it would still teach.

Write `rescue.json` in your folder (Bash heredoc): `claim_id`, `rescued_statement`, `status`, `proof_at`, `what_it_teaches`, `open_step`. Put your work in the manifest's `report` field. Budget: about 80 tool calls, 120 CPU seconds.

## The claim

{claim}
"""


def claims_of(tasks):
    out = []
    for t in tasks:
        p = os.path.join(DATA, "out", t, "claims.jsonl")
        if not os.path.exists(p):
            continue
        n = 0
        for line in open(p, encoding="utf-8"):
            if line.strip():
                n += 1
                try:
                    r = json.loads(line)
                except ValueError:
                    r = {"raw": line.strip()}
                r["claim_id"] = "%s.%d" % (t, n)
                out.append(r)
    return out


def main():
    mode = sys.argv[1]
    if mode == "screen":
        sid, tasks = sys.argv[2], sys.argv[3:]
        cl = claims_of(tasks)
        body = "\n".join(json.dumps(c, ensure_ascii=False) for c in cl)
        write_task(sid, SC.replace("{tasks}", ", ".join(tasks)).replace("{claims}", body), REC_FULL)
        write_batch("w3-" + sid, [{"id": sid, "effort": "high"}], 3)
        print(sid, len(cl), "claims")
    elif mode == "skeptics":
        name = sys.argv[2]
        sel = [json.loads(l) for l in open(os.path.join(DATA, "state", name + ".jsonl"), encoding="utf-8") if l.strip()]
        tasks = []
        for c in sel:
            cid = c["claim_id"]
            task = cid.split(".")[0]
            slug = cid.replace(".", "-")
            cj = json.dumps(c, ensure_ascii=False)
            write_task("SKR-" + slug, SKR.replace("{claim}", cj).replace("{task}", task), REC_FULL)
            write_task("SKM-" + slug, SKM.replace("{claim}", cj).replace("{task}", task), REC_FULL)
            tasks.append({"id": "SKR-" + slug, "effort": "high"})
            m = {"id": "SKM-" + slug, "effort": "xhigh"}
            if c.get("fable"):
                m["model"] = "fable"
            tasks.append(m)
        write_batch(name, tasks, 8)
        print(name, len(tasks))
    elif mode == "rescue":
        name = sys.argv[2]
        sel = [json.loads(l) for l in open(os.path.join(DATA, "state", name + ".jsonl"), encoding="utf-8") if l.strip()]
        tasks = []
        for k, c in enumerate(sel, 1):
            cid = c["claim_id"]
            write_task("RS-%d" % k, RS.replace("{claim}", json.dumps(c, ensure_ascii=False)).replace("{task}", cid.split(".")[0]), REC_FULL)
            tasks.append({"id": "RS-%d" % k, "effort": "xhigh"})
        write_batch(name, tasks, 6)
        print(name, len(tasks))


if __name__ == "__main__":
    main()
