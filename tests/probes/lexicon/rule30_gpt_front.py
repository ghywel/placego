#!/usr/bin/env python3
"""Reset-front phase comparison, not a proof of its asymptotic speed.

COMMAND: PYTHONDONTWRITEBYTECODE=1 python3 tests/probes/lexicon/rule30_gpt_front.py
RUN-ON: GPT Intel CPU, one core; standard library, Python 3.10+.
COST: seconds, small memory; reuses the exact G2 prefix construction.
Prior mechanism: Rowland section 5; Local section 8.59. No million-side run.

PREDICTIONS before first run, 2026-10-06:
 SF0 control: certified 53208-word period-16 prefix; original worst final
     bound 107312 and birth-aware worst 107313, matching G2.
 SF1 must hold: at every prefix, phase bounds differ by at most P-1;
     lifted bounds tau_phi+phi are nondecreasing in phi and span at most P.
     One-phase plus P-1 bounds every phase, with or without births.
 SF2 blind: the original front's lifted phases have only one residue modulo
     16 by diagonal 1000, and keep that property through 53207.
 SF3 control: independently scanning each word's bits agrees with the
     precomputed waiting-table front on all 16 phases through diagonal 1024.
 SF4 counterfactual must fail: density 1/2 in every temporal word alone
     implies reset slope at most 3. A prescribed period-16 toy sequence,
     with eight consecutive zeros before each selected reset, has slope 9.
     It must fail the Rule 30 recurrence check: it is not an admissible side.
 SF5 unexpected check, must hold: SF1 also holds for 256 seeded random
     word lists of width 64 at period 7, including identically white words,
     with and without birth clamps. The phase lemma needs no power of two.
REFUTED-BY: any control or SF1/SF5 failure; SF2 having more than one residue
at any tested diagonal >=1000; SF4 failing to reject either false shortcut.
OUTCOME, 2026-10-06 03:03 BST, first run: exit 0, ALL CONTROLS PASS.
 SF0 PASSED: certified period 16; final worst 107312 / birth-aware 107313.
 SF1 PASSED: maximum phase spread 15 in both variants; phase zero 107308
     in both. The generic single-phase bound is therefore 107323.
 SF2 HELD: first persistent singleton lifted residue at diagonal 429;
     singleton through 53207. This is finite evidence only.
 SF3 PASSED: 16 phases x 1024 transitions x both boundary variants.
 SF4 REJECTED: 129 half-black words; time 1152 at 128, slope 9;
     1651 failed Rule 30 recurrence equations confirm inadmissibility.
 SF5 PASSED: 256 period-7 word lists, width 64, both variants.
 No blind failure occurred. No all-branch speed or period-growth theorem.
"""
import random
from rule30_gpt_cycles import bit, certified, classify, rows


def waiting(word, period):
    if not word:
        return [0] * period
    return [1 + next(d for d in range(period) if bit(word, t+d, period))
            for t in range(period)]


def front(words, period, birth=False):
    times = [0] * period
    history = [times[:]]
    for k, word in enumerate(words[:-1]):
        table = waiting(word, period)
        for phi in range(period):
            start = max(times[phi], k if birth else 0)
            times[phi] = start + table[(start+phi) % period]
        history.append(times[:])
    return history


def phase_check(history, period):
    for times in history:
        lifted = [t+phi for phi,t in enumerate(times)]
        if (max(times)-min(times) > period-1 or
                lifted != sorted(lifted) or lifted[-1]-lifted[0] > period):
            return False
    return True


def scalar(words, period, phi, birth=False):
    time = 0
    history = [time]
    for k, word in enumerate(words[:-1]):
        time = max(time, k if birth else 0)
        if word:
            while not ((word >> ((time+phi) % period)) & 1):
                time += 1
            time += 1
        history.append(time)
    return history


def recurrence_errors(words, period):
    errors = 0
    for k in range(2, len(words)):
        for t in range(period):
            a,b,c = [bit(words[j],t,period) for j in (k-2,k-1,k)]
            errors += bit(words[k],t+1,period) != (a ^ (b | c))
    return errors


def main():
    controls, blind = [], []
    def check(name, okay, detail, isblind=False):
        print(('HELD' if isblind and okay else 'REFUTED' if isblind else
               'PASS' if okay else 'FAIL')+' '+name+': '+detail, flush=True)
        (blind if isblind else controls).append(okay)
    words,p,_,branch,_ = classify(53208)
    normal, born = front(words,p), front(words,p,True)
    check('SF0', branch == 53208 and p == 16 and certified(rows(words,p),len(words))
          and max(normal[-1]) == 107312 and max(born[-1]) == 107313,
          'period %d; final original %s; birth %s' % (p,normal[-1],born[-1]))
    check('SF1', phase_check(normal,p) and phase_check(born,p),
          'maximum phase spread original %d, birth %d; phase-zero final %d/%d' %
          (max(max(t)-min(t) for t in normal),max(max(t)-min(t) for t in born),
           normal[-1][0],born[-1][0]))
    sizes = [len({(t+phi)%p for phi,t in enumerate(ts)}) for ts in normal]
    last_multiple = max((k for k,v in enumerate(sizes) if v != 1), default=-1)
    persistent = last_multiple+1 if last_multiple+1 < len(sizes) else None
    check('SF2', max(sizes[1000:]) == 1,
          'residues at 1000 %d; final %d; first persistent singleton %s' %
          (sizes[1000],sizes[-1],persistent),True)
    check('SF3', all(scalar(words[:1025],p,phi,b)==[ts[phi] for ts in h[:1025]]
          for b,h in [(False,normal),(True,born)] for phi in range(p)),
          '16 phases x 1024 transitions x 2 boundary variants')
    # Toy word k: its first black at the chosen path's time plus h.
    h,n = 8,128
    toy = []
    for k in range(n+1):
        start = (k*(h+1)+h) % (2*h)
        toy.append(sum(1 << ((start+j) % (2*h)) for j in range(h)))
    toy_time = front(toy,2*h)[-1][0]
    errors = recurrence_errors(toy,2*h)
    check('SF4 rejected', all(w.bit_count()==h for w in toy) and toy_time==n*(h+1)
          and toy_time>3*n and errors>0,
          'all half-black; phase-zero time %d at %d; Rule 30 errors %d' %
          (toy_time,n,errors))
    rng=random.Random(3006)
    lists=[[rng.randrange(128) for _ in range(64)] for _ in range(256)]
    lists[0]=[0]*64
    check('SF5 unexpected', all(phase_check(front(ws,7,b),7)
          for ws in lists for b in (False,True)),
          '256 word lists, period 7, width 64, both boundary variants')
    print('ALL CONTROLS PASS' if all(controls) else 'CONTROL FAILURE',flush=True)
    return not all(controls) or not all(blind)


if __name__ == '__main__':
    raise SystemExit(main())
