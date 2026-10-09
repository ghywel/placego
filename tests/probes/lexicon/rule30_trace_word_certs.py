#!/usr/bin/env python3
"""rule30_trace_word_certs.py: TWC, formally verified certificates that measured forbidden G-trace words are
forbidden. GPT's GC842 hand audit of 0001101011 stalls, and that word still carries GC827's h >= 4 branch on the
census's authority alone (L426). This turns the census claim into a certificate checked by the verified checker
cake_lpr. Local's run (chat L464), predictions pushed before it.

RUN-ON:     cpu (Python 3, kissat, drat-trim, cadical, ~/np-build/cake_lpr/cake_lpr); seconds
COMMAND:    python3 tests/probes/lexicon/rule30_trace_word_certs.py

G(x)_i = x_i xor (x_(i+1) OR x_(i+2)) reads only right neighbours, so the origin's n-tick temporal trace depends on
exactly x_0 .. x_(2n-2) at time 0. A word w of length n is a G-trace word iff some assignment of those 2n - 1 cells
yields trace w. The CNF has one variable per cell of the shrinking space-time triangle, the exact G equations, and
units fixing the origin's trace to w. UNSAT means w is forbidden in every forward G orbit, with arbitrary decoration.
An UNSAT is certified: kissat writes DRAT, drat-trim converts it to LRAT (cadical's native LRAT as fallback), and
cake_lpr checks it. A SAT model is replayed literally.

PREDICTIONS (Local's, published before the run):
  TWC-C1 (control): 000001101 (hand-proved, G.GPT267) is UNSAT and verified by cake_lpr.
  TWC-C2 (control): 00000001011 (GC840's allowed prefix) is SAT, and the model replays to that trace.
  TWC-P1 (blind, confidence 0.95): 0001101011 and the other length-10 minimal word 0010100000 are UNSAT, each
         verified by cake_lpr.
  TWC-P2 (blind, confidence 0.9): all 28 length-11 minimal forbidden words of L449 are UNSAT and verified.
"""
import os
import subprocess

DIR = os.path.expanduser('~/np-scratch-int/rule30-twc')
CAKE = os.path.expanduser('~/np-build/cake_lpr/cake_lpr')
L11 = ('00000101100 00001010111 00001011100 00010111111 00011000000 00011010000 00011010011 00011010100 '
       '00110101111 00111001011 00111110100 00111111100 01001011100 01110011111 10001100000 10110100011 '
       '11000000011 11000001011 11000110100 11001010000 11100101011 11100101100 11100101111 11100111111 '
       '11101000000 11110100011 11110101000 11111010011').split()


def cnf(word):
    n = len(word)
    nv, cl, var = 0, [], {}
    for t in range(n):
        for i in range(2 * (n - 1 - t) + 1):
            nv += 1
            var[(t, i)] = nv
    for t in range(n - 1):
        for i in range(2 * (n - 2 - t) + 1):
            y, a, b, c = var[(t + 1, i)], var[(t, i)], var[(t, i + 1)], var[(t, i + 2)]
            nv += 1
            o = nv                                     # o = b OR c
            cl += [[-b, o], [-c, o], [b, c, -o]]
            cl += [[-y, a, o], [-y, -a, -o], [y, -a, o], [y, a, -o]]    # y = a xor o
    for t, ch in enumerate(word):
        cl.append([var[(t, 0)] if ch == '1' else -var[(t, 0)]])
    return 'p cnf %d %d\n' % (nv, len(cl)) + ''.join(' '.join(map(str, c)) + ' 0\n' for c in cl), var


def check_word(word):
    os.makedirs(DIR, exist_ok=True)
    text, var = cnf(word)
    base = os.path.join(DIR, word)
    open(base + '.cnf', 'w').write(text)
    r = subprocess.run(['kissat', '-q', '-f', '--no-binary', base + '.cnf', base + '.drat'], capture_output=True, text=True)
    if r.returncode == 10:
        model = {int(x) for line in r.stdout.splitlines() if line.startswith('v ') for x in line[2:].split()}
        n = len(word)
        x = [1 if var[(0, i)] in model else 0 for i in range(2 * n - 1)]
        tr = []
        for _ in range(n):
            tr.append(x[0])
            x = [x[i] ^ (x[i + 1] | x[i + 2]) for i in range(len(x) - 2)]
        return 'SAT, replays to %s' % ''.join(map(str, tr))
    if r.returncode != 20:
        return 'UNKNOWN'
    v = subprocess.run(['drat-trim', base + '.cnf', base + '.drat', '-L', base + '.lrat'], capture_output=True, text=True)
    c = subprocess.run([CAKE, base + '.cnf', base + '.lrat'], capture_output=True, text=True)
    if 's VERIFIED UNSAT' in c.stdout:
        return 'UNSAT, cake_lpr VERIFIED (drat-trim LRAT)'
    subprocess.run(['cadical', '-q', '--lrat=true', base + '.cnf', base + '.cad.lrat'], capture_output=True)
    c2 = subprocess.run([CAKE, base + '.cnf', base + '.cad.lrat'], capture_output=True, text=True)
    return 'UNSAT, cake_lpr VERIFIED (cadical LRAT)' if 's VERIFIED UNSAT' in c2.stdout else 'UNSAT, NOT VERIFIED'


def main():
    res = {}
    for w in ['000001101', '00000001011', '0001101011', '0010100000'] + L11:
        res[w] = check_word(w)
        print('%-12s %s' % (w, res[w]), flush=True)
    ver = lambda w: res[w].startswith('UNSAT, cake_lpr VERIFIED')
    print('TWC-C1', 'PASS' if ver('000001101') else 'FAIL')
    print('TWC-C2', 'PASS' if res['00000001011'] == 'SAT, replays to 00000001011' else 'FAIL')
    print('TWC-P1', 'HELD' if ver('0001101011') and ver('0010100000') else 'REFUTED')
    print('TWC-P2', 'HELD' if all(ver(w) for w in L11) else 'REFUTED at %s' % [w for w in L11 if not ver(w)])
    print('COMPLETE')


if __name__ == '__main__':
    main()
