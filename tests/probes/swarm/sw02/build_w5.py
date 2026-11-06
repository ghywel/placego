#!/usr/bin/env python3
"""SW-02 builder: Wave 5. Writes DATA/state/claims-all.jsonl (every claim with its screen and skeptic verdicts) and the compile briefs."""
import glob, json, sys
from build_common import *


def assemble():
    scr = {r["claim_id"]: r for r in json.load(open(os.path.join(DATA, "state", "screens.json")))}
    rows = []
    for f in sorted(glob.glob(os.path.join(DATA, "out", "*", "claims.jsonl"))):
        t = f.split("/")[-2]
        n = 0
        for line in open(f, encoding="utf-8"):
            if not line.strip():
                continue
            n += 1
            try:
                c = json.loads(line)
            except ValueError:
                c = {"raw": line.strip()}
            cid = "%s.%d" % (t, n)
            s = scr.get(cid, {})
            r = {"claim_id": cid, "title": c.get("claim"), "statement": c.get("statement"), "status": c.get("status"), "population": c.get("population"), "bridge": c.get("bridge"),
                 "screen_class": s.get("class", "NOT SCREENED"), "screen_rank": s.get("rank"), "screen_reason": s.get("reason"), "fidelity": s.get("fidelity")}
            slug = cid.replace(".", "-")
            for k in ("SKR", "SKM"):
                p = os.path.join(DATA, "out", k + "-" + slug, "verdict.json")
                if os.path.exists(p):
                    try:
                        v = json.load(open(p, encoding="utf-8"))
                        r[k] = {x: v.get(x) for x in ("verdict", "confidence", "first_bad_step", "repaired_statement", "carrying_step", "matches", "note") if v.get(x)}
                    except ValueError:
                        r[k] = {"verdict": "unreadable"}
            r["report_at"] = "out/%s/report.txt" % t
            rows.append(r)
    rs = {}
    for f in sorted(glob.glob(os.path.join(DATA, "out", "RS-*", "rescue.json"))):
        try:
            v = json.load(open(f, encoding="utf-8"))
            rs[v.get("claim_id")] = dict(v, rescued_by=f.split("/")[-2])
        except ValueError:
            pass
    for r in rows:
        if r["claim_id"] in rs:
            r["rescue"] = rs[r["claim_id"]]  # the original statement and the repaired one are both kept
    with open(os.path.join(DATA, "state", "claims-all.jsonl"), "w", encoding="utf-8") as f:
        for r in rows:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")
    print(len(rows), "claims")


GROUPS = {"CM-1a": ["R-01", "R-02", "R-11", "L-6", "L-4"], "CM-1b": ["R-03", "R-04", "R-05", "R-13", "L-1", "L-5"], "CM-1c": ["R-06", "R-07", "R-08", "R-09", "R-10", "R-12", "L-2", "L-3", "L-7"]}

COMMON5 = """
**Materials.** `{{DATA}}/state/claims-all.jsonl`: every Wave 2 claim with its screen class and skeptic verdicts. `{{DATA}}/state/verdicts.json`: the verified status flags. `{{DATA}}/out/<id>/report.txt` or `report.md`, `manifest.json`: each task's report. `{{DATA}}/out/BN-*/`: the bench tests. `{{REC}}/reports/SW02-SWARM-DESIGN.md`: the design, whose §5 gives door verdicts, §2 the objectives, §11 the rigour contract, §14 the predictions.
`{{SW}}/GPT-PORTAL-KIT-UPDATE-20261106.md`, `{{SW}}/GPT-SW02-INTERIM-REVIEW-20261106.md` and `{{SW}}/GPT-SW02-CARRY-REVIEW-20261106.md`: GPT's register, interim review and carrying review (GC2690), which audit your output. Where GC2690 carries a statement, use its repaired statement and status, which are a worker's read: cite the exact external ladder (`Rule30Open.bwh_Q01`, `not_absorptionT_t001`, BinaryCTS, ConstantTailSeparator), apply the leaf-width comparison (a guarded tree of depth d ending at width W gives 2^d leaves at width W - 2d) and the conditional-measure comparison, and leave SEP's reverse realization pending. A failed cutoff in BN-15 is not a refutation of existential Closing; finite repetition in BN-16 is a candidate only, without a closed-state certificate.
Statuses: nothing from this swarm is PROVED by its own say-so. A hand proof is PROOF-SKETCH however many sub-agents re-derived it, and a new hand closure is PENDING CARRY. A failed search is INCONCLUSIVE. Keep Rule 30's populations apart: Q01, CQ01, a fixed R, a surrogate, the seed.
"""

CM1G = """# SW-02 task {{ID}}: door compiler, one third of the cards

**Role.** Compile the door ledger for these sources: {group}. **Locus:** their `doors.jsonl` in `{{DATA}}/out/<id>/`. Merge cards that are one door under two names (use `{{SW}}/TERMS.md` §4a and each card's aliases). Update each verdict from Wave 2, 3 and 4 evidence, by searching `claims-all.jsonl` and the bench outputs. Apply the design's §5 strictly: a theorem closes only its class; a measurement cannot shut a door; a new hand closure is PENDING CARRY; a failed search closes nothing. No silent drops: every input card is either kept or named as merged into another.

Write `doors.jsonl` in your folder (Bash heredoc or a Python script), one object per merged door: `door`, `route`, `target`, `verdict`, `closure_kind`, `scope`, `source`, `evidence` (claim ids, flags, bench ids), `reopen`, `next_test`, `cost`, `info`, `aliases`, `merged_from` (input card names). Sort by target. Put a short account in the manifest's `report` field: counts by verdict, and doors whose verdict changed from the card. Budget: about 70 tool calls.
""" + COMMON5

MM = """# SW-02 task {{ID}}: matchmaker

**Role.** Pair every surviving count with every surviving amplification, and say whether the exponents cross. **Locus:** the count and amplification claims, chiefly AM-1, AM-3, AM-2, AM-5, CT-1 to CT-5, LN-01, LN-02, LN-07, LN-11, XP-1, CP-2. Match population, width transform, time and horizon, conditioning, constants and distinctness before comparing any two bounds. Retain direct subunit-count or seed-specific alternatives. Say exactly what is proved, what is conditional and on what, and the smallest missing statement for each pair. If a pair closes, assume first that you have an error, and report it as a prize-level claim only after trying to break it.

Write `pairs.jsonl` in your folder: `count`, `amplification`, `population`, `exponents`, `crosses` (yes, no, or conditional on), `missing`. Put your account in the manifest's `report` field. Budget: about 60 tool calls.
""" + COMMON5

JD = """# SW-02 task {{ID}}: judge, {kind}

**Role.** {role} **Locus:** the whole swarm's output. Read `claims-all.jsonl`, the door ledger parts in `{{DATA}}/out/CM-1*/doors.jsonl`, the matchmaker's report in `{{DATA}}/out/MM-1/`, and the reports you need. Choose at most five doors to leave AJAR: for each, the next test, its cost, what it would teach even if it fails, and who should own it. Say which results should go to GPT for a carrying read: at most three carrying steps, each with its marked step and exact sources. Give your verdict on the wall as restated in L1558: does count-plus-amplification survive as the right picture? Run a small unexpected check of your own through the queue if one would change your ranking. A door you do not choose stays open or deferred; it is not shut.

Write `ranking.jsonl` in your folder: `rank`, `door`, `next_test`, `cost`, `teaches`, `owner`, `why`. Put your account in the manifest's `report` field. Budget: about 70 tool calls.
""" + COMMON5

CR = """# SW-02 task {{ID}}: completeness critic

**Role.** What is missing? **Locus:** the swarm as a whole: a lens not used, a source unread, a claim unverified, a door with no card, a population confused, a known result re-derived, a place where the swarm's own frame misled it. Read the design, the reports' `not_done` fields (`manifest.json`), the screens, the verdicts, the bench outputs and the predictions in `{{REC}}/tests/probes/swarm/sw02/PREDICTIONS.md`, and judge each prediction P1 to P15 and U with its evidence. Name the single most useful thing the swarm did not do.

Write `predictions.jsonl` in your folder (`id`, `held`, `evidence`) and put the rest in the manifest's `report` field. Budget: about 60 tool calls.
""" + COMMON5

CM2 = """# SW-02 task {{ID}}: answer compiler

**Role.** Compile the answer sheet and the barrier atlas. **Locus:** every question in the design's §8 (56 tasks) and every barrier. For each question: the answer in two or three sentences, its status, the claim ids behind it, and what is still open. For each barrier, from R-11's report, the BR squad, LN-06, XP-2, XP-3, P3-3 and the kit: the class it excludes, in exact terms, its status (kit theorem, or new and PENDING CARRY), and what it leaves open. Unforced findings: collect the `unforced` fields worth keeping, with their evidence. Keep every status as the evidence allows, with no rounding up.

Write in your folder, by Bash heredoc or a Python script: `answers.jsonl` (`id`, `question`, `answer`, `status`, `claims`, `open`), `barriers.jsonl` (`barrier`, `class`, `statement`, `status`, `source`, `leaves_open`), `unforced.jsonl` (`from`, `finding`, `status`). Put a short account in the manifest's `report` field. Budget: about 80 tool calls.
""" + COMMON5


def main():
    mode = sys.argv[1]
    if mode == "assemble":
        assemble()
    elif mode == "cm1":
        ts = []
        for k, v in GROUPS.items():
            write_task(k, CM1G.replace("{group}", ", ".join(v)), REC_FULL)
            ts.append({"id": k, "effort": "high"})
        write_task("MM-1", MM, REC_FULL)
        ts.append({"id": "MM-1", "effort": "xhigh"})
        write_task("CM-2", CM2, REC_FULL)
        ts.append({"id": "CM-2", "effort": "high"})
        write_batch("w5a", ts, 5)
        print(len(ts))
    elif mode == "judges":
        write_task("JD-1", JD.replace("{kind}", "theorist").replace("{role}", "Which ajar doors could become theorems?"), REC_FULL)
        write_task("JD-2", JD.replace("{kind}", "engineer").replace("{role}", "Which ajar doors have the cheapest decisive test?"), REC_FULL)
        write_task("CR-1", CR, REC_FULL)
        write_batch("w5b", [{"id": "JD-1", "effort": "max", "model": "fable"}, {"id": "JD-2", "effort": "max", "model": "fable"}, {"id": "CR-1", "effort": "high"}], 3)
        print(3)


if __name__ == "__main__":
    main()
