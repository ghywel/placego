# Minimal CNF builder with guarded sequential-counter cardinality constraints.
import subprocess, os, time

class CNF:
    def __init__(self):
        self.nv = 0
        self.clauses = []
    def var(self):
        self.nv += 1
        return self.nv
    def add(self, c):
        self.clauses.append(list(c))
    def atmost(self, xs, k, guard=None):
        """sum(xs) <= k, unless guard literal is true."""
        g = [] if guard is None else [guard]
        n = len(xs)
        if k >= n:
            return
        if k < 0:
            self.add(g)  # unsatisfiable unless guard
            return
        if k == 0:
            for x in xs:
                self.add([-x] + g)
            return
        s = [[self.var() for j in range(k)] for i in range(n - 1)]
        self.add([-xs[0], s[0][0]] + g)
        for j in range(1, k):
            self.add([-s[0][j]] + g)
        for i in range(1, n - 1):
            self.add([-xs[i], s[i][0]] + g)
            self.add([-s[i - 1][0], s[i][0]] + g)
            for j in range(1, k):
                self.add([-xs[i], -s[i - 1][j - 1], s[i][j]] + g)
                self.add([-s[i - 1][j], s[i][j]] + g)
            self.add([-xs[i], -s[i - 1][k - 1]] + g)
        self.add([-xs[n - 1], -s[n - 2][k - 1]] + g)
    def atleast(self, xs, k, guard=None):
        self.atmost([-x for x in xs], len(xs) - k, guard)
    def write(self, path):
        with open(path, 'w') as f:
            f.write('p cnf %d %d\n' % (self.nv, len(self.clauses)))
            for c in self.clauses:
                f.write(' '.join(map(str, c)) + ' 0\n')
    def solve(self, path, timeout=300, solver='kissat'):
        self.write(path)
        t0 = time.time()
        if solver == 'kissat':
            cmd = ['nice', '-n', '10', 'kissat', '-q', '--time=%d' % timeout, path]
        else:
            cmd = ['nice', '-n', '10', 'cadical', '-q', '-t', str(timeout), path]
        p = subprocess.run(cmd, capture_output=True, text=True)
        dt = time.time() - t0
        status = None
        model = set()
        for line in p.stdout.splitlines():
            if line.startswith('s '):
                status = line[2:].strip()
            elif line.startswith('v '):
                for t in line[2:].split():
                    v = int(t)
                    if v > 0:
                        model.add(v)
        return status, model, dt
