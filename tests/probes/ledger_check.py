#!/usr/bin/env python3
"""ledger_check.py: the live CHAT-LEDGER.md must not carry entries that are already archived.

RUN-ON:     cpu (Python 3, standard library)
COMMAND:    python3 tests/probes/ledger_check.py [REPO_ROOT]   or   python3 tests/probes/ledger_check.py --branch
COST:       instant. Run after merging main into a branch, and before pushing.

Why (CHAT-LEDGER.md CL001). The ledger rotates like a log: `git mv CHAT-LEDGER.md CHAT-LEDGER.N.md` and a fresh
file. With `merge=union` on CHAT-LEDGER.md, a branch begun before a rotation that appended an entry merges without
any conflict and re-imports the whole archived ledger into the live file. This check fails if any `## ` heading of
the live file also appears in an archive, or if a heading appears twice in the live file.
Control: the script is checked on a synthetic case below (a live file that repeats an archived heading must fail).
Mode --branch (Local's L015 proposal, without changing the ledger's header): run after your fetch and before
merging origin/main into a branch (it makes no fetch of its own, for the network etiquette). A branch is from before a rotation exactly when its tree holds fewer CHAT-LEDGER.N.md archives than
origin/main's. Then do not merge the ledger path: re-append your new entries onto main's live file instead.
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


def archives_in(ref):
    import subprocess
    out = subprocess.run(["git", "ls-tree", "--name-only", ref], cwd=ROOT, capture_output=True, text=True, check=True)
    return sum(1 for n in out.stdout.split() if re.fullmatch(r"CHAT-LEDGER\.\d+\.md", n))


def branch_mode():
    mine, theirs = archives_in("HEAD"), archives_in("origin/main")
    if mine < theirs:
        print(f"STOP: this branch has {mine} ledger archive(s) and origin/main has {theirs}: a rotation happened since"
              " the branch began. Do not merge CHAT-LEDGER.md; re-append your new entries onto main's live file.")
        sys.exit(1)
    print(f"BRANCH CHECK PASSES ({mine} archive(s) here, {theirs} on origin/main)")


def main():
    if len(sys.argv) > 1 and sys.argv[1] == "--branch":
        branch_mode()
        return
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
