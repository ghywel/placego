#!/usr/bin/env python3
"""idle_alarm.py: flag a worker whose recent CLOUD-LOCAL.md rows show passing, declining or idling.

RUN-ON:     cpu (Python 3, standard library)
COMMAND:    python3 tests/probes/idle_alarm.py [--rows K] [--quiet-hours H]
COST:       instant. Cloud runs it on every visit and posts any flag to the owner and in the chat.

Why (the owner, 2026-10-07). Local had drawn five board rows and passed on all five, each with a careful reason, and
nothing outside Local noticed until the owner asked. Earlier the same day GPT and Local had both stalled on their
tick and flag routines. Idling that explains itself well reads like diligence, so a reader skims past it; this script
does not. The owner: "That's a frightening me problem though - I gave Local a private memory, the sentence parses
fine to me, but it took a meaning i didn't intended which intended into a workflow blocker." See the
shared-procedures and draw-and-work rules in WORKFLOW-SAVED-MEMORY.md.

Three flags, per party (Local, GPT, Cloud), over each party's last K ledger rows (default 8):
  PASS     a row records passing on work or declining it: "noted and passed", "passed on the row", "declined to",
           "not started unasked", draws called "proof-shaped", and the like. A test that passed is not a pass on
           work. Under draw-and-work a drawn row is worked, not passed, so one such row is enough.
  STREAK   the party's last three rows are all idle in tone (queue empty, waiting, parked, nothing to do, idle,
           no new work) with no sign of work in them (a result, a run, a review, a check, a filing).
  QUIET    the party's last timed row is older than H hours (default 3), measured from the newest timed row in the
           file. Informational only: a party can be quiet because the owner stopped it.
A flag is a prompt to look, not a verdict: a row can mention a pass while doing plenty else. A pass phrase with
another party's name just before it is reported speech ("making Local pass on") and is not counted to the writer;
nor is one in a sentence that names a rule ("rows passed under the old rule go back in the draw").
Control: a synthetic ledger must raise each flag where it should and none where it should not.
"""
import pathlib, re, sys
from datetime import datetime

ROOT = pathlib.Path(__file__).resolve().parents[1].parent
PARTIES = ("Local", "GPT", "Cloud")
WORKISH = r"(?:(?:the|a|this|that|each|all) )?(?:it|them|valid|work|rows?|draws?|leads?|tasks?|jobs?|Q\d+)\b"
PASS = re.compile(r"\b((?:noted|drawn|considered|read) and passed|pass(?:ed|es|ing)? (?:on|over) " + WORKISH +
                  r"|declin(?:ed|ing) (?:to\b|" + WORKISH + r")|not started unasked|(?:did|do) not start\b"
                  r"|left (?:it|them) (?:unstarted|undone)|skipp(?:ed|ing) " + WORKISH +
                  r"|draws?\b[^|.;]{0,80}proof-shaped|proof-shaped[^|.]{0,60}(?:pass|skip|declin|not start))", re.I)
IDLE = re.compile(r"\b(queue (?:is )?empty|review queue empty|waiting (?:on|for)|parked|nothing to do|idle|"
                  r"no new (?:work|job|task)|no job|no claimed job|holding|on hold|stand(?:ing)? by)\b", re.I)
WORK = re.compile(r"\b(PASS|FAIL|REFUTED|CONFIRMED|proved|proves|ran|run on|executed|wrote|written up|filed|"
                  r"checked|audit(?:ed)?|review(?:ed)?|second[- ]read|claims?|outcome|result|census|measured|"
                  r"reproduc\w*|verified|certif\w*)\b")
RULE = re.compile(r"\brules?\b", re.I)
ROW = re.compile(r"^\|\s*(\d{4}-\d{2}-\d{2})(?:\s+(\d{1,2}:\d{2}))?\s*\|\s*([A-Za-z]+)\s*\|(.*)$")


def rows(text):
    """(party, time, line) per ledger row. A row dated without a time (GPT's habit) borrows the time of the nearest
    timed row above it on the same date, so that QUIET does not flag a party for leaving out the clock."""
    out, last = [], None
    for line in text.split("\n"):
        m = ROW.match(line)
        if m and m.group(3) in PARTIES:
            if m.group(2):
                when = datetime.strptime(m.group(1) + " " + m.group(2), "%Y-%m-%d %H:%M")
                last = when
            else:
                when = last if last and last.strftime("%Y-%m-%d") == m.group(1) else None
            out.append((m.group(3), when, line))
    return out


def sentence(line, i):
    """The sentence of a ledger row around position i, cut at a full stop, a semicolon or a cell border."""
    a = max(line.rfind(c, 0, i) for c in (". ", "; ", "|"))
    bs = [j for j in (line.find(c, i) for c in (". ", "; ", "|")) if j >= 0]
    return line[a + 1:min(bs) if bs else len(line)]


def flags(text, k=8, quiet_hours=3.0):
    rs = rows(text)
    out = []
    newest = max((w for _, w, _ in rs if w), default=None)
    for party in PARTIES:
        mine = [(w, line) for p, w, line in rs if p == party]
        if not mine:
            continue
        for w, line in mine[-k:]:
            for m in PASS.finditer(line):
                before = line[max(0, m.start() - 40):m.start()]
                if any(o in before for o in PARTIES if o != party):
                    continue  # reported speech: the row is about another party's pass, not the writer's
                if RULE.search(sentence(line, m.start())):
                    continue  # the sentence is about a rule ("passed under the old rule"), not a pass
                out.append(("PASS", party, w, f"...{line[max(0, m.start() - 60):m.end() + 40]}..."))
                break
        last3 = mine[-3:]
        if len(last3) == 3 and all(IDLE.search(l) and not WORK.search(l) for _, l in last3):
            out.append(("STREAK", party, last3[-1][0], "last three rows idle in tone with no work in them"))
        timed = [w for w, _ in mine if w]
        if newest and timed and (newest - timed[-1]).total_seconds() > quiet_hours * 3600:
            hours = (newest - timed[-1]).total_seconds() / 3600
            out.append(("QUIET", party, timed[-1], f"no timed row for {hours:.1f} h before the newest one"))
    return out


def control():
    t = "\n".join([
        "| 2026-10-07 10:00 | Local | reviews | Audit S1 PASS; GC1 checked. | |",
        "| 2026-10-07 11:00 | Local | draws | Random draws: Q9, Q2 proof-shaped, passed; Q6 not started unasked. | |",
        "| 2026-10-07 11:05 | GPT | queue | Review queue empty. Waiting for Local. | |",
        "| 2026-10-07 11:10 | GPT | queue | Nothing to do; parked. | |",
        "| 2026-10-07 11:20 | GPT | queue | Idle, waiting on L9. | |",
        "| 2026-10-07 11:30 | Cloud | doc | Wrote the summary; math check PASS. | |",
        "| 2026-10-07 18:00 | Cloud | doc | Filed entry 3. | |",
        "| 2026-10-07 18:01 | Cloud | rule | The owner asked whether X was making Local pass on work. | |",
        "| 2026-10-07 18:02 | Cloud | rule | Rows passed under the old rule go back in the draw. | |",
        "| 2026-10-07 18:03 | Cloud | test | CT0 control passed; CH0 passed; ledger_check passes on main. | |",
        "| 2026-10-07 18:04 | Cloud | test | A challenge pass on every picture; tests passed on 3 hosts. | |",
        "| 2026-10-07 18:05 | Cloud | test | ALL CHECKS PASS on the host; it passes on the four documents. | |",
    ])
    got = {(f, p) for f, p, _, _ in flags(t)}
    assert ("PASS", "Local") in got, got
    assert ("STREAK", "GPT") in got, got
    assert ("QUIET", "Local") in got and ("QUIET", "GPT") in got, got
    assert not any(p == "Cloud" for _, p in got), got
    late = "\n".join([
        "| 2026-10-07 10:00 | Local | x | Filed entry 3. | |",
        "| 2026-10-07 | GPT | y | Proved G9. | |",
        "| 2026-10-07 14:00 | Local | x | Filed entry 4. | |",
        "| 2026-10-07 | GPT | y | Proved G10. | |",
    ])
    assert not any(f == "QUIET" for f, *_ in flags(late)), "an untimed row after a timed one is not quiet"
    busy = "\n".join(f"| 2026-10-07 1{i}:00 | GPT | work | Review received; GC{i} PASS, waiting on Local. | |"
                     for i in range(3))
    assert not any(f == "STREAK" for f, *_ in flags(busy)), "a busy row must not count as idle"


def main():
    k = int(sys.argv[sys.argv.index("--rows") + 1]) if "--rows" in sys.argv else 8
    h = float(sys.argv[sys.argv.index("--quiet-hours") + 1]) if "--quiet-hours" in sys.argv else 3.0
    control()
    arch = sorted(ROOT.glob("CLOUD-LOCAL.*.md"), key=lambda q: int(q.name.split(".")[1]))
    before = arch[-1].read_text() + "\n" if arch else ""          # after a rotation, the newest archive comes first
    fl = flags(before + (ROOT / "CLOUD-LOCAL.md").read_text(), k, h)
    if not fl:
        print(f"IDLE ALARM: no flags in each party's last {k} rows")
        return
    for f, party, when, note in fl:
        print(f"IDLE ALARM {f:6s} {party:5s} {when.strftime('%Y-%m-%d %H:%M') if when else '(untimed)'}: {note}")


if __name__ == "__main__":
    main()
