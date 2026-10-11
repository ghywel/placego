#!/usr/bin/env python3
"""jobctl.py: pause, resume and prioritise Local's long runs (the owner's request, 2026-10-11 13:55 BST).

RUN-ON:     the machine the jobs run on (macOS or Linux; standard library only)
COMMAND:    python3 tests/probes/jobctl.py list
            python3 tests/probes/jobctl.py add LABEL PID PRIO [--wallclock] "description"
            python3 tests/probes/jobctl.py pause LABEL [--force]  |  resume LABEL  |  rm LABEL
            python3 tests/probes/jobctl.py focus LABEL [--force]   (run it in the background)

Why. A job started yesterday may no longer be aligned with the current investigation, or may be welcome but slow
the important task down. Every long run is registered here with a priority (1 = the current main line, 2 = a
planned lane item, 3 = welcome but not urgent, such as re-certifying older results). `pause` and `resume` stop and
continue a job's whole process tree (the driver and every solver under it) with SIGSTOP and SIGCONT; nothing is
lost, and the job continues where it stopped. `focus LABEL` pauses every registered job of a lower priority (a larger
number), waits until LABEL's root process exits, then resumes exactly the jobs it paused.

The one hazard is a wall-clock limit. kissat's --time is an alarm() on real time and drat-trim's -t is measured
with gettimeofday, so a job with such a limit loses its budget while it is paused (kissat -q -n or -f without --time,
drat-trim -t 400000 and cake_lpr are safe). Register such jobs with --wallclock; pause and focus skip them unless
--force is given, and say so.

The registry is a JSON file beside the run data (JOBS below), outside git.
"""
import json
import os
import signal
import subprocess
import sys
import time

JOBS = os.path.join(os.path.expanduser('~'), 'np-scratch-int', 'jobs.json')


def load():
    try:
        return json.load(open(JOBS))
    except FileNotFoundError:
        return {}


def save(reg):
    tmp = JOBS + '.tmp'
    json.dump(reg, open(tmp, 'w'), indent=1, sort_keys=True)
    os.replace(tmp, JOBS)


def table():
    out = subprocess.run(['ps', '-Ao', 'pid=,ppid=,stat=,etime=,%cpu=,rss=,command='], capture_output=True,
                         text=True).stdout
    rows = {}
    for line in out.splitlines():
        p = line.split(None, 6)
        if len(p) == 7:
            rows[int(p[0])] = dict(ppid=int(p[1]), stat=p[2], etime=p[3], cpu=float(p[4]), rss=int(p[5]), cmd=p[6])
    return rows


def tree(root, rows):
    kids = {}
    for pid, r in rows.items():
        kids.setdefault(r['ppid'], []).append(pid)
    out, todo = [], [root]
    while todo:
        p = todo.pop()
        if p in rows:
            out.append(p)
            todo.extend(kids.get(p, []))
    return out


def signal_tree(label, sig, reg, rows):
    pids = tree(reg[label]['root'], rows)
    order = pids if sig == signal.SIGSTOP else list(reversed(pids))
    for p in order:
        try:
            os.kill(p, sig)
        except ProcessLookupError:
            pass
    return pids


def short(cmd):
    for key in ('records_k.py', 'verified_certs.py', 'cycle_cuts.py', 'kissat', 'drat-trim', 'cake_lpr', 'python3'):
        if key in cmd:
            i = cmd.index(key)
            return cmd[i:i + 70]
    return cmd[-70:]


def cmd_list(reg):
    rows = table()
    for label in sorted(reg, key=lambda k: (reg[k]['prio'], k)):
        j = reg[label]
        pids = tree(j['root'], rows)
        state = 'GONE' if not pids else ('PAUSED' if all('T' in rows[p]['stat'] for p in pids) else 'RUNNING')
        flags = (' wallclock' if j.get('wallclock') else '') + (' paused-by:' + j['paused_by'] if j.get('paused_by') else '')
        print('%-14s prio %d  %-7s root %-6d%s  %s' % (label, j['prio'], state, j['root'], flags, j['desc']))
        busy = [p for p in pids if rows[p]['cpu'] > 1 or 'T' in rows[p]['stat']]
        for p in busy[:4]:
            r = rows[p]
            print('      %-6d %-4s %10s %5.1f%% %6d MB  %s' % (p, r['stat'], r['etime'], r['cpu'], r['rss'] // 1024, short(r['cmd'])))


def main():
    a = sys.argv[1:]
    reg = load()
    force = '--force' in a
    a = [x for x in a if x != '--force']
    if not a or a[0] == 'list':
        cmd_list(reg)
    elif a[0] == 'add':
        wall = '--wallclock' in a
        a = [x for x in a if x != '--wallclock']
        label, pid, prio, desc = a[1], int(a[2]), int(a[3]), ' '.join(a[4:])
        reg[label] = dict(root=pid, prio=prio, wallclock=wall, desc=desc, added=time.strftime('%Y-%m-%d %H:%M'))
        save(reg)
        print('registered', label)
    elif a[0] == 'rm':
        reg.pop(a[1], None)
        save(reg)
    elif a[0] in ('pause', 'resume'):
        label = a[1]
        if a[0] == 'pause' and reg[label].get('wallclock') and not force:
            sys.exit('%s has a wall-clock limit; pausing it spends its budget (use --force)' % label)
        pids = signal_tree(label, signal.SIGSTOP if a[0] == 'pause' else signal.SIGCONT, reg, table())
        if a[0] == 'resume':
            reg[label].pop('paused_by', None)
            save(reg)
        print('%s %s: %d processes' % (a[0], label, len(pids)))
    elif a[0] == 'focus':
        label = a[1]
        mine = reg[label]
        rows = table()
        paused = []
        for other, j in reg.items():
            if other == label or j['prio'] <= mine['prio'] or j.get('paused_by'):
                continue
            if j.get('wallclock') and not force:
                print('focus %s: leaving %s running (wall-clock limit)' % (label, other))
                continue
            if tree(j['root'], rows):
                signal_tree(other, signal.SIGSTOP, reg, rows)
                j['paused_by'] = label
                paused.append(other)
        save(reg)
        print('focus %s: paused %s at %s' % (label, paused, time.strftime('%H:%M')), flush=True)
        while tree(mine['root'], table()):
            time.sleep(30)
        reg = load()
        rows = table()
        for other in paused:
            if other in reg and reg[other].get('paused_by') == label:
                signal_tree(other, signal.SIGCONT, reg, rows)
                reg[other].pop('paused_by', None)
        save(reg)
        print('focus %s: %s ended; resumed %s at %s' % (label, label, paused, time.strftime('%H:%M')), flush=True)
    else:
        sys.exit(__doc__)


if __name__ == '__main__':
    main()
