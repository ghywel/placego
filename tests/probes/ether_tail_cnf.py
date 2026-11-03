#!/usr/bin/env python3
"""GC2431: literal finite-cone CNF and independent retained-model controls.

No solver in this stage. Predict original/protected files fit16MiB and all
controls pass. Exact87-input question, no folding or added wall assumptions.
"""
import hashlib
import importlib.util
import itertools
import json
import os
from pathlib import Path

FILE_LIMIT = 16 << 20


def gate(a, b, c, y):
    # y = a XOR (b OR c). Six exact clauses, no auxiliary variables.
    return ([b, c, -a, y], [b, c, a, -y], [-b, a, y],
            [-b, -a, -y], [-c, a, y], [-c, -a, -y])


def check_clause(clause, bits):
    return any(bool(bits[abs(x)]) == (x > 0) for x in clause)


class Cone:
    def __init__(self, left, right, time, cutoff, initial):
        self.left, self.right, self.time, self.cutoff = left, right, time, cutoff
        assert right-left+1 > 2*time
        self.widths = [right-left+1-2*t for t in range(time+1)]
        self.starts = []
        total = 1
        for n in self.widths:
            self.starts.append(total)
            total += n
        self.nv = total-1
        self.initial = [initial(x) for x in range(left, right+1)]
        self.fixed = [(self.var(0, x), initial(x)) for x in range(left, min(cutoff, right)+1)]
        self.reference = self.scalar_model({})
        self.target = [self.var(time, x) * (1 if not self.reference[self.var(time, x)] else -1)
                       for x in range(left+time, right-time+1)]

    def var(self, t, x):
        i = x-(self.left+t)
        assert 0 <= t <= self.time and 0 <= i < self.widths[t]
        return self.starts[t]+i

    def scalar_model(self, changes):
        # Literal triple evaluation; independent of gate() and its clause signs.
        row = self.initial[:]
        for x, v in changes.items():
            assert self.left <= x <= self.right
            row[x-self.left] = v
        bits = bytearray(self.nv+1)
        for t in range(self.time+1):
            bits[self.starts[t]:self.starts[t]+len(row)] = bytes(row)
            if t < self.time:
                row = [int(a != (b or c)) for a, b, c in zip(row, row[1:], row[2:])]
        return bits

    def packed_control(self, bits):
        n = self.widths[0]
        z = sum(bits[self.starts[0]+i] << i for i in range(n))
        for t in range(self.time+1):
            assert bits[self.starts[t]:self.starts[t]+n] == bytes((z >> i) & 1 for i in range(n))
            if t < self.time:
                z = (((z << 1) ^ (z | (z >> 1))) >> 1) & ((1 << (n-2))-1)
                n -= 2

    def clauses(self, protected=False):
        for t in range(1, self.time+1):
            for x in range(self.left+t, self.right-t+1):
                yield from gate(self.var(t-1, x-1), self.var(t-1, x),
                                self.var(t-1, x+1), self.var(t, x))
        for v, b in self.fixed:
            yield [v if b else -v]
        yield self.target
        if protected:
            assert (self.left, self.right, self.time, self.cutoff) == (-332, 198, 222, 111)
            yield [-self.var(0, 112)]

    def count(self, protected=False):
        return 6*(self.nv-self.widths[0])+len(self.fixed)+1+int(protected)

    def write(self, path, protected=False):
        header = f'p cnf {self.nv} {self.count(protected)}\n'.encode()
        def lines():
            yield header
            for cl in self.clauses(protected):
                yield (' '.join(map(str, cl))+' 0\n').encode()
        # Exact byte preflight before opening a possibly oversize artifact.
        size = sum(len(line) for line in lines())
        assert size < FILE_LIMIT, ('CNF_FILE_LIMIT', size)
        h = hashlib.sha256()
        with path.open('wb') as f:
            for line in lines():
                h.update(line)
                f.write(line)
        assert path.stat().st_size == size
        return {'variables': self.nv, 'clauses': self.count(protected),
                'bytes': size, 'sha256': h.hexdigest()}


def disk_unsatisfied(path, bits):
    # Parse the actual emitted DIMACS, not the generator's in-memory clauses.
    bad, count = [], 0
    with path.open() as f:
        header = next(f).split()
        assert header[:2] == ['p', 'cnf'] and int(header[2]) == len(bits)-1
        for line in f:
            ints = [int(x) for x in line.split()]
            assert ints.pop() == 0 and ints and all(0 < abs(x) < len(bits) for x in ints)
            count += 1
            if not check_clause(ints, bits):
                bad.append(count)
    assert count == int(header[3])
    return bad


def main():
    out = Path(os.environ['CAPPED_OUT'])
    report = {'stage': 'ENCODER_ONLY', 'solver_run': False, 'controls': {}}
    def save():
        (out/'encoder.json').write_text(json.dumps(report, indent=2)+'\n')
    # Exact gate truth table, all16 parent/output assignments.
    accepted = 0
    for a, b, c, y in itertools.product([0, 1], repeat=4):
        actual = all(check_clause(cl, [0, a, b, c, y]) for cl in gate(1, 2, 3, 4))
        expected = y == int(a != (b or c))
        assert actual == expected
        accepted += actual
    assert accepted == 8
    report['controls']['gate_16_cases'] = True
    # Two exact small cones: 010 return is constant,110's preceding cell is not.
    for name, word, expected_models in [('010', [0, 1, 0, 0, 0], 0),
                                        ('110-gap', [0, 1, 1, 0, 0, 0], 2)]:
        left = 3-len(word)
        cone = Cone(left, 2, 2, 0, lambda x: word[x-left])
        path = out/(name+'.cnf')
        cone.write(path)
        models = 0
        for u, v in itertools.product([0, 1], repeat=2):
            bits = cone.scalar_model({1: u, 2: v})
            cone.packed_control(bits)
            bad = disk_unsatisfied(path, bits)
            assert bad in ([], [cone.count()])
            models += not bad
        assert models == expected_models
        report['controls'][name] = {'goal_models_of_four': models}
    p = Path('tests/probes/ether_adaptive_shield.py')
    assert hashlib.sha256(p.read_bytes()).hexdigest() == 'f1fccc493af4fe3538a89b3dcc8d12d7f56f9279b5074afb5b197afa210ee85a'
    spec = importlib.util.spec_from_file_location('base', p)
    base = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(base)
    assert hashlib.sha256(Path('tests/probes/lean/EtherEdgeZero.lean').read_bytes()).hexdigest() == base.ENTRY_HASH
    prior_bytes = Path(os.environ['ONE_FLIP_RESULT']).read_bytes()
    assert hashlib.sha256(prior_bytes).hexdigest() == 'fbaa0329db36166a48536944cad589c5eab049e0052e89670c0fb30a9ea0ba71'
    prior = json.loads(prior_bytes)
    initial = lambda x: base.TABLE[(x+4)%7][3] if x < 0 else int(x == 0)
    cone = Cone(-332, 198, 222, 111, initial)
    assert cone.nv == 68907 and len(cone.fixed) == 444 and len(cone.target) == 87
    original = out/'tail111.cnf'
    protected = out/'tail112.cnf'
    report['original'] = cone.write(original)
    report['protected'] = cone.write(protected, True)
    save()
    for name, changes in [('baseline', {}), ('flip112', {112: 1}), ('flip113', {113: 1})]:
        bits = cone.scalar_model(changes)
        cone.packed_control(bits)
        assert disk_unsatisfied(original, bits) == [cone.count()]
        protected_bad = disk_unsatisfied(protected, bits)
        assert protected_bad == ([cone.count(), cone.count()+1] if name == 'flip112' else [cone.count()])
        wall = [bits[cone.var(222, x)] for x in range(-36, -23)]
        assert wall == prior['results'][0]['reference_wall']
        path = out/(name+'.bits')
        path.write_bytes(bits)
        report['controls'][name] = {'bits_sha256': hashlib.sha256(bits).hexdigest(),
                                  'only_original_goal_fails': True,
                                  'protected_unsatisfied': protected_bad}
        save()
    # Corrupt a constrained gate output: rejection must no longer be just the goal.
    badbits = cone.reference[:]
    badbits[cone.var(1, -331)] ^= 1
    badclauses = disk_unsatisfied(original, badbits)
    assert any(k < cone.count()-len(cone.fixed) for k in badclauses)
    report['controls']['corrupt_gate_rejected'] = True
    report['status'] = 'ENCODER_CONTROLS_PASS'
    save()
    print(json.dumps(report))


if __name__ == '__main__':
    main()
