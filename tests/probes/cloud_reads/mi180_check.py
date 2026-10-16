# Cloud's independent implementation of MI180 (B79): the two-chain picture, the full-label construction (N = n-2) and the
# sparse contraction (two halves >= k+2). Each output cycle is checked by its MOVE BAG (p, q, -2d) and folded labels.
import itertools, collections, sys
sys.path.insert(0, '.')
from b77_check import exists_cycle
def cycle_from_chains(n, A, B):
    """A, B disjoint increasing index lists, 0 in A. Returns physical positions in cycle order and the move bag."""
    assert A[0] == 0 and not set(A) & set(B) and A == sorted(A) and B == sorted(B)
    pos = [0] + [2*n - 1 - 2*v for v in B] + [2*u for u in reversed(A) if u > 0]
    M = 2*n; labels = {min(x, M - 1 - x) for x in pos}
    assert all(0 <= x <= M - 1 for x in pos) and len(labels) == len(pos), (n, A, B, pos)
    moves = [pos[(i+1) % len(pos)] - pos[i] for i in range(len(pos))]
    return pos, sorted(moves)
def word_runs(n, p, q, d):
    """full-label word: first run A of length alpha, internal runs d_i-1 for d_i>1 (given order), last run beta."""
    alpha = (2*n - 1 - p) // 2; beta = (2*n - 3 - q) // 2
    assert alpha >= 1 and beta >= 1 and (2*n - 1 - p) % 2 == 0 and (2*n - 3 - q) % 2 == 0
    runs = [alpha] + [x - 1 for x in d if x > 1] + [beta]
    assert sum(runs) == n, (n, p, q, d, runs)
    return runs
def chains_from_runs(runs):
    A, B, i = [], [], 0
    for r, L in enumerate(runs):
        (A if r % 2 == 0 else B).extend(range(i, i + L)); i += L
    return A, B
def full_label(n, p, q, d):
    if p < q: p, q = q, p
    A, B = chains_from_runs(word_runs(n, p, q, list(d)))
    pos, bag = cycle_from_chains(n, A, B)
    assert bag == sorted([p, q] + [-2*x for x in d]), (n, p, q, d, bag)
    return pos
def sparse(n, p, q, d, iD, iE):
    """refine d[iD] into (D-k, k units), order internal runs D-k-1 (B) then E-1 (A) then the rest, delete first k A's of run 3."""
    if p < q: p, q = q, p
    N = len(d); k = n - N - 2; D, E = d[iD], d[iE]; assert k > 0 and iD != iE and min(D, E) >= k + 2
    rest = [d[i] for i in range(N) if i not in (iD, iE)]
    refined = [D - k, E] + rest + [1]*k
    alpha = (2*n - 1 - p) // 2; beta = (2*n - 3 - q) // 2
    runs = [alpha, D - k - 1, E - 1] + [x - 1 for x in rest if x > 1] + [beta]
    assert sum(runs) == n
    A, B = chains_from_runs(runs)
    third = list(range(runs[0] + runs[1], runs[0] + runs[1] + runs[2]))   # the A run of length E-1
    A = [u for u in A if u not in third[:k]]
    pos, bag = cycle_from_chains(n, A, B)
    assert bag == sorted([p, q] + [-2*x for x in d]), (n, p, q, d, bag)
    return pos
# exhaustive tests on small windows
full_cases = sparse_cases = 0; iff_checked = 0
for n in range(3, 11):
    M = 2*n
    for N in range(1, n - 1):
        for d in itertools.combinations_with_replacement(range(1, n), N):
            K = sum(d)
            for p in range(1, 2*K, 2):
                q = 2*K - p
                if q < p: continue
                legal = q <= M - 3 and not (p == q == M - 3)
                if N == n - 2:
                    if n <= 7:
                        truth = exists_cycle(M, p, q, list(d)); assert truth == legal, (M, p, q, d, truth, legal); iff_checked += 1
                    if legal:
                        for perm in set(itertools.permutations(d)): full_label(n, p, q, perm); full_cases += 1
                elif legal:
                    for iD in range(N):
                        for iE in range(N):
                            if iD != iE and min(d[iD], d[iE]) >= n - N - 2 + 2:
                                sparse(n, p, q, list(d), iD, iE); sparse_cases += 1
print("full-label iff vs exhaustive truth on n=3..7 (iff) and n=3..10 (constructions):", iff_checked, "cases agree;", full_cases, "constructions (all internal orders) pass move-bag and labels")
print("sparse contractions on n=3..7 (iff) and n=3..10 (constructions):", sparse_cases, "pass move-bag and labels")
# the hand example and M=28 fixtures
pos = sparse(14, 21, 19, [8, 8, 1, 1, 1, 1], 0, 1); print("hand example positions", pos)
for d, p, q in [([8,8,1,1,1,1],25,15), ([8,8,1,1,1,1],23,17), ([8,8,2,2,2,2],25,23), ([10,10,1,1,1,1],25,23), ([8,9,1,1,1,4],25,23)]:
    sparse(14, p, q, d, 0, 1)
print("M=28 sparse fixtures pass")
