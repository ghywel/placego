#!/usr/bin/env python3
"""check_batch.py NAME: validate a finished SW-02 batch from its files, not its manifests: every task's folder, each .jsonl parses,
counts per file, and a digest per task. Writes DATA/state/NAME.json. Also reports a privacy scan of the task's files."""
import glob, hashlib, json, os, re, sys

DATA = os.environ.get("SW02_DATA", os.path.expanduser("~/placego-data/sw02"))
HOME = os.path.expanduser("~")


def main():
    name = sys.argv[1]
    b = json.load(open(os.path.join(DATA, "batches", name + ".json")))
    rows, bad = [], 0
    for t in b["tasks"]:
        d = os.path.join(DATA, "out", t["id"])
        files = sorted(f for f in glob.glob(d + "/*") if os.path.isfile(f))
        h = hashlib.sha256()
        counts, errs = {}, []
        for f in files:
            raw = open(f, "rb").read()
            h.update(os.path.basename(f).encode() + b"\0" + raw)
            if f.endswith(".jsonl"):
                n = 0
                for k, line in enumerate(raw.decode("utf-8", "replace").splitlines()):
                    if not line.strip():
                        continue
                    try:
                        json.loads(line)
                        n += 1
                    except ValueError:
                        errs.append("%s:%d" % (os.path.basename(f), k + 1))
                counts[os.path.basename(f)] = n
            else:
                counts[os.path.basename(f)] = len(raw)
            if HOME.encode() in raw and not f.endswith(".py"):
                errs.append("home path in " + os.path.basename(f))
        ok = bool(files) and not errs
        bad += 0 if ok else 1
        rows.append({"id": t["id"], "ok": ok, "digest": h.hexdigest()[:16], "counts": counts, "errs": errs[:6]})
        print(("ok " if ok else "BAD"), t["id"], counts, errs[:6])
    os.makedirs(os.path.join(DATA, "state"), exist_ok=True)
    json.dump(rows, open(os.path.join(DATA, "state", name + ".json"), "w"), indent=0)
    print(len(rows), "tasks,", bad, "with problems")


if __name__ == "__main__":
    main()
