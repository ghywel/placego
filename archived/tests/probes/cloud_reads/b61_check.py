# Independent replication of B61/MI144: every six-point shape with min 0 and span <= 20 admits, for every gap g in 1..14,
# a translation t (points in 0..27) with six distinct folded labels and a free gap-g edge (two unused labels).
import itertools
def label(j): return min(j, 27 - j)
E = {g: [frozenset((label(x), label(x + g))) for x in range(28 - g) if label(x) != label(x + g)] for g in range(1, 15)}
shapes = [(0,) + c for c in itertools.combinations(range(1, 21), 5)]
assert len(shapes) == 15504
fail = []; need_move = 0
for sh in shapes:
    span = sh[-1]
    for g in range(1, 15):
        found = False; first_valid_blocked = False
        for t in range(0, 28 - span):
            P = [p + t for p in sh]; labs = {label(p) for p in P}
            if len(labs) < 6: continue
            if any(not (e & labs) for e in E[g]): found = True; break
            first_valid_blocked = True
        if not found: fail.append((sh, g))
        elif first_valid_blocked: need_move += 1
print("shapes", len(shapes), "questions", 15504 * 14, "failures", len(fail), "questions where some valid root was fully covered but a translation escaped", need_move)
