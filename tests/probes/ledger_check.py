#!/usr/bin/env python3
"""ledger_check.py: no live ledger may carry entries that are already archived.

RUN-ON:     cpu (Python 3, standard library)
COMMAND:    python3 tests/probes/ledger_check.py [REPO_ROOT]   or   python3 tests/probes/ledger_check.py --branch
COST:       instant. Run after merging main into a branch, and before pushing.

Why (CHAT-LEDGER.md CL001). The ledgers rotate like a log: `git mv LEDGER.md LEDGER.N.md` and a fresh file. With
`merge=union` on the live files, a branch begun before a rotation that appended an entry merges without any
conflict and re-imports the archived text into the live file. This check fails if any entry of a live file also
appears in one of its archives, or if an entry appears twice in the live chat.
Three ledgers, three kinds of entry (extended by Cloud, 2026-10-07, when the owner asked for all three to rotate):
  CHAT-LEDGER.md     entry headings with an ID: "## C001 ...", "## GC143 ...", "## CL001 ...", "## GC549.3 ...";
  CASUAL-LEDGER.md   entry headings with an author: "## <name> — <title> (...)";
  CLOUD-LOCAL.md     dated table rows, in the messages table and the ledger: "| 2026-10-07 21:02 | ...".
Controls: each kind is checked on a synthetic case below (a live file that repeats an archived entry must fail, and
a live file with only new entries must pass).
Mode --branch (Local's L015 proposal): run after your fetch and before merging origin/main into a branch (it makes no
fetch of its own, for the network etiquette). A branch is from before a rotation exactly when its tree holds fewer
archives of some ledger than origin/main's. Then do not merge that ledger's path: re-append your new entries onto
main's live file instead.
"""
import pathlib, re, sys

ROOT = pathlib.Path(__file__).resolve().parents[2]

KINDS = {
    "CHAT-LEDGER": (re.compile(r"^## [A-Z]+\d+(\.\d+)* "), True),  # entry headings (C001, L013, CL001, GC549.3)
    "CASUAL-LEDGER": (re.compile(r"^## \S[^\n]* — "), False),    # "## Local — a title (...)", not the preamble's
    "CLOUD-LOCAL": (re.compile(r"^\| 20\d\d-\d\d-\d\d"), False),  # dated rows of the messages table and the ledger
}


def entries(text, pat):
    return [l.strip() for l in text.split("\n") if pat.match(l)]


def problems(live, archives, pat=KINDS["CHAT-LEDGER"][0], unique=True):
    archived = {h for a in archives for h in entries(a, pat)}
    seen, out = set(), []
    for h in entries(live, pat):
        if h in archived:
            out.append(f"archived entry in the live file: {h[:90]}")
        if unique and h in seen:
            out.append(f"entry repeated in the live file: {h[:90]}")
        seen.add(h)
    return out


def archives_in(ref, base):
    import subprocess
    out = subprocess.run(["git", "ls-tree", "--name-only", ref], cwd=ROOT, capture_output=True, text=True, check=True)
    return sum(1 for n in out.stdout.split() if re.fullmatch(re.escape(base) + r"\.\d+\.md", n))


def branch_mode():
    bad = False
    for base in KINDS:
        mine, theirs = archives_in("HEAD", base), archives_in("origin/main", base)
        if mine < theirs:
            bad = True
            print(f"STOP: this branch has {mine} {base} archive(s) and origin/main has {theirs}: a rotation happened"
                  f" since the branch began. Do not merge {base}.md; re-append your new entries onto main's live file.")
        else:
            print(f"BRANCH CHECK PASSES for {base} ({mine} archive(s) here, {theirs} on origin/main)")
    sys.exit(1 if bad else 0)


def control():
    chat, casual, cl = (KINDS[k][0] for k in ("CHAT-LEDGER", "CASUAL-LEDGER", "CLOUD-LOCAL"))
    assert problems("## C001 x\n", ["## C001 x\n"], chat) and not problems("## L013 y\n", ["## C001 x\n"], chat)
    assert not problems("## Archives, and how to catch up\n", ["## Archives, and how to catch up\n"], chat)
    assert problems("## GC549.3 x\n", ["## GC549.3 x\n"], chat)               # dotted sub-entries count too
    a = "## How it works\n## Local — socks (2026-10-07 06:50 BST)\n"
    assert problems("## Local — socks (2026-10-07 06:50 BST)\n", [a], casual, False)
    assert not problems("## How it works\n## GPT — tea (2026-10-07)\n", [a], casual, False)
    r = "| 2026-10-07 21:02 | Cloud | x | y | z |\n"
    assert problems(r, ["| When | Who |\n" + r], cl, False)
    assert not problems("| When | Who |\n| 2026-10-07 22:10 | Cloud | new | row | |\n", [r], cl, False)


def main():
    if len(sys.argv) > 1 and sys.argv[1] == "--branch":
        branch_mode()
        return
    control()
    root = pathlib.Path(sys.argv[1]) if len(sys.argv) > 1 else ROOT
    found, counts = [], {}
    for base, (pat, unique) in KINDS.items():
        live_path = root / f"{base}.md"
        if not live_path.exists():
            continue
        live = live_path.read_text()
        archives = [p.read_text() for p in sorted(root.glob(f"{base}.*.md"))]
        f = problems(live, archives, pat, unique)
        found += [f"{base}: {p}" for p in f]
        counts[base] = (len(entries(live, pat)), len(archives))
    for p in found[:10]:
        print("FAIL ", p)
    n, a = counts.get("CHAT-LEDGER", (0, 0))
    others = "; ".join(f"{b} {c[0]} live, {c[1]} archive(s)" for b, c in counts.items() if b != "CHAT-LEDGER")
    print(f"{'LEDGER CHECK PASSES' if not found else f'{len(found)} PROBLEM(S): merge the archived copy out'}"
          f" ({n} live headings, {a} archive(s); {others})")
    sys.exit(1 if found else 0)


if __name__ == "__main__":
    main()
