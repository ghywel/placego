#!/usr/bin/env python3
"""ledger_check.py: the live CHAT-LEDGER.md must not carry entries that are already archived.

RUN-ON:     cpu (Python 3, standard library)
COMMAND:    python3 tests/probes/ledger_check.py [REPO_ROOT]
COST:       instant. Run after merging main into a branch, and before pushing.

Why (CHAT-LEDGER.md CL001). The ledger rotates like a log: `git mv CHAT-LEDGER.md CHAT-LEDGER.N.md` and a fresh
file. With `merge=union` on CHAT-LEDGER.md, a branch begun before a rotation that appended an entry merges without
any conflict and re-imports the whole archived ledger into the live file. This check fails if any `## ` heading of
the live file also appears in an archive, or if a heading appears twice in the live file.
Control: the script is checked on a synthetic case below (a live file that repeats an archived heading must fail).
"""
import pathlib, re, sys

ROOT = pathlib.Path(__file__).resolve().parents[2]


ENTRY = re.compile(r"^## [A-Z]+\d+ ")                 # entry headings (C001, L013, G009, CL001), not the preamble's


def headings(text):
    return [l.strip() for l in text.split("\n") if ENTRY.match(l)]


def problems(live, archives):
    archived = {h for a in archives for h in headings(a)}
    seen, out = set(), []
    for h in headings(live):
        if h in archived:
            out.append(f"archived entry in the live file: {h[:90]}")
        if h in seen:
            out.append(f"entry repeated in the live file: {h[:90]}")
        seen.add(h)
    return out


def main():
    assert problems("## C001 x\n", ["## C001 x\n"]) and not problems("## L013 y\n", ["## C001 x\n"]), "control"
    assert not problems("## Archives, and how to catch up\n", ["## Archives, and how to catch up\n"]), "preamble"
    root = pathlib.Path(sys.argv[1]) if len(sys.argv) > 1 else ROOT
    live = (root / "CHAT-LEDGER.md").read_text()
    archives = [p.read_text() for p in sorted(root.glob("CHAT-LEDGER.*.md"))]
    found = problems(live, archives)
    for p in found[:10]:
        print("FAIL ", p)
    print(f"{'LEDGER CHECK PASSES' if not found else f'{len(found)} PROBLEM(S): merge the archived copy out'}"
          f" ({len(headings(live))} live headings, {len(archives)} archive(s))")
    sys.exit(1 if found else 0)


if __name__ == "__main__":
    main()
