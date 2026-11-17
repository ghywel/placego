#!/usr/bin/env python3
"""SW-02 builder: Wave 1 verifiers. Sorts every raised flag by file and splits them into at most eight batches."""
import glob, json, sys
from build_common import *

V = """# SW-02 task {{ID}}: verifier

**Role.** Check each flag below against its source, as SW-01's verifiers did, and return one verdict per flag: CONFIRMED (the summary is wrong as flagged), PARTIAL (a real disagreement of smaller scope, or a stale statement) or
NOT AN ERROR (the summary and the source agree, or the flag misread them). **Locus:** this batch of flags. Only Local edits the record.

Read the summary at `summary_at` and the source at `source_at` yourself, in the record at `{{REC}}` or the kit at `{{KIT}}`. Do not trust the flag's paraphrase. Use the aliases in `{{SW}}/TERMS.md` §4a. For a real error, write the smallest correct
wording, in the style of the line it replaces. Budget: about 80 tool calls; a flag you could not settle is reported as UNSETTLED with the reason.

Write `verdicts.jsonl` in your folder, one object per flag: `flag` (the number below), `verdict`, `summary_at`, `source_at`, `why`, `correction` (exact replacement text for the summary, or empty), `severity` (material or cosmetic).

## The flags

{flags}
"""

def main():
    rows = []
    for f in sorted(glob.glob(os.path.join(DATA, "out", "*", "flags.jsonl"))):
        who = os.path.basename(os.path.dirname(f))
        for line in open(f, encoding="utf-8"):
            if line.strip():
                try:
                    r = json.loads(line)
                    r["from"] = who
                    rows.append(r)
                except ValueError:
                    pass
    rows.sort(key=lambda r: str(r.get("summary_at", "")))
    for n, r in enumerate(rows, 1):
        r["flag"] = n
    json.dump(rows, open(os.path.join(DATA, "state", "flags.json"), "w"), indent=0, ensure_ascii=False)
    k = min(8, max(1, (len(rows) + 19) // 20))
    per = (len(rows) + k - 1) // k
    tasks = []
    for i in range(k):
        part = rows[i * per:(i + 1) * per]
        tid = "V-%d" % (i + 1)
        body = "\n".join(json.dumps(r, ensure_ascii=False) for r in part)
        write_task(tid, V.replace("{flags}", body), REC_FULL)
        tasks.append({"id": tid, "effort": "medium"})
    write_batch("w1v", tasks, 8)
    print(len(rows), "flags in", k, "batches")

if __name__ == "__main__":
    main()
