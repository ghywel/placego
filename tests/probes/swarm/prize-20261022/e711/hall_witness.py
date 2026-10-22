# Hall witness: for the window (m, m+H) find a max matching; if it is not perfect on {1..n}, print the violating
# set S (left vertices reachable from free ones by alternating paths) and its neighbourhood N(S), |N(S)| < |S|.
import sys
def witness(n, m, H):
    xs = list(range(m + 1, m + H))
    adj = {k: [x for x in xs if x % k == 0] for k in range(1, n + 1)}
    match = {}; mL = {}
    def aug(k, seen):
        for x in adj[k]:
            if x not in seen:
                seen.add(x)
                if x not in match or aug(match[x], seen):
                    match[x] = k; mL[k] = x; return True
        return False
    for k in range(n, 0, -1): aug(k, set())
    free = [k for k in range(1, n + 1) if k not in mL]
    if not free: return None
    S = set(free); stack = list(free); NS = set()
    while stack:
        k = stack.pop()
        for x in adj[k]:
            if x not in NS:
                NS.add(x)
                j = match.get(x)
                if j is not None and j not in S: S.add(j); stack.append(j)
    return sorted(S), sorted(NS)
if __name__ == "__main__":
    n, m, H = map(int, sys.argv[1:4])
    w = witness(n, m, H)
    if w is None: print("perfect matching exists"); sys.exit()
    S, NS = w
    print("n", n, "m", m, "H", H, "|S|", len(S), "|N(S)|", len(NS))
    print("S =", S)
    for x in NS:
        print(" ", x, "offset", x - m, "divisors in S:", [k for k in S if x % k == 0])
