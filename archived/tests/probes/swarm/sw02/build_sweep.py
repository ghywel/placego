#!/usr/bin/env python3
"""SW-02: the critic's most useful omission (CR-1): the record skeptics that never ran, grouped into five tasks with rule30-open on the search list. These fit the frozen launch ceiling
(181 of 186 used). The fresh-eyes search is mandatory in the design before any follow-on."""
import json
from build_common import *
from build_w3 import claims_of
G = {"SKG-1": ["FE-1.1", "FE-1.2", "FE-1.3", "FE-2.1", "FE-2.2", "FE-2.3", "FE-3.1", "FE-3.2", "FE-3.3", "FE-4.1", "FE-4.2", "FE-4.3"],
     "SKG-2": ["BR-2.1", "BR-2.2", "XP-3.1", "LN-06.1", "XP-2.1", "P3-3.3"],
     "SKG-3": ["LN-05.1", "LN-05.2", "LN-03.1", "LN-04.1", "LN-07.1", "LN-07.2"],
     "SKG-4": ["LN-09.1", "LN-11.1", "PE-1.2", "PE-2.1", "P2-1.1", "CP-3.2"],
     "SKG-5": ["AM-2.2", "CT-1.2", "HX-2.1", "BR-3.1", "BR-3.2", "LN-12.2", "XP-1.1"]}
T = """# SW-02 task {{ID}}: grouped record skeptic

**Role.** Default unverified: has each claim below been done, closed or renamed? **Locus:** the claims listed, one verdict each. The swarm's critic found that record skeptics never ran on these, and that every record skeptic that did run found prior art. {extra}

Search, under every name in `{{SW}}/TERMS.md` §4a and every name you can derive: the record at `{{REC}}`; the kit at `{{KIT}}` by exact statement; the portal (`{{DATA}}/portal/INDEX.md`, `src/`); the PR snapshot (`{{DATA}}/kit-prs/PRS.md`), including closed PRs and review bodies; the survey's cards in `{{DATA}}/out/*/doors.jsonl`; and two outside sources the earlier skeptics lacked. **First, `lhallee/rule30-open` on GitHub:** read its README, ROADMAP, catalogue of headline theorems and the relevant Lean file names and statements, with WebFetch on github.com and raw.githubusercontent.com pages. Read only: clone nothing, build nothing, run nothing. **Second, N. Berzai's paper** (`nateberzai-svg/rule30-left-edge`, paper/RULE30_PAPER.pdf, §24's table of closed routes) if you can reach it. `{{SW}}/GPT-SW02-CARRY-REVIEW-20261106.md` and `{{SW}}/GPT-SW02-INTERIM-REVIEW-20261106.md` record what GPT has already compared. A literal miss is not absence: a result is known once its hypotheses and conclusion match, and a keyword hit alone is only a candidate.

Write `verdicts.jsonl` in your folder (Bash heredoc), one object per claim: `claim_id`, `verdict` (KNOWN, PARTLY KNOWN, CLOSED ROUTE, ALIAS, or NOT FOUND AFTER SEARCH), `matches` (name, location, how hypotheses and conclusion compare), `searched`, `confidence` (0 to 1), `note`. Put your account in the manifest's `report` field. Budget: about 90 tool calls.

## The claims

{claims}
"""
tasks = []
for k, ids in G.items():
    ts = sorted(set(i.split(".")[0] for i in ids))
    cl = {c["claim_id"]: c for c in claims_of(ts)}
    body = "\n".join(json.dumps({x: cl[i].get(x) for x in ("claim_id", "claim", "statement", "status", "population")}, ensure_ascii=False) for i in ids if i in cl)
    extra = "These are the fresh-eyes claims: the design requires this search before any follow-on work or acceptance. Their authors saw one page and no record, so expect much to be known." if k == "SKG-1" else ""
    write_task(k, T.replace("{extra}", extra).replace("{claims}", body), REC_FULL)
    tasks.append({"id": k, "effort": "high"})
write_batch("w3-skg", tasks, 5)
print(len(tasks))
