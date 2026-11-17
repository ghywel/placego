"""CL495: exact check of Lemma G3 (PROOFS.md, Cloud CL495) as an IFF at the low end, all k, N <= 18.
Predicted: alpha+3 missing iff D in {k+{0,1,2}, k+{-1,1,3}, k+{-2,2,3}, k+{-1,0,4}}; alpha+4 missing iff
(k = 3 and D = {4,5,6}) or (k = n-3 and D = {k-1,k,k+1}); nothing missing at alpha+5..  Prediction: 0 mismatches.
"""
import itertools
def sig(R, k):
    s = set()
    for c in itertools.combinations(R, k): s.add(sum(c))
    return s
mis = n_cases = 0
for N in range(9, 19):
    for d in range(0, 4):
        for D in itertools.combinations(range(1, N), d):
            R = [x for x in range(N + 1) if x not in D]; n = len(R); Ds = set(D)
            if n < 7: continue
            for k in range(3, n - 2):
                s = sig(R, k); a = min(s); n_cases += 1
                pats = [{k, k+1, k+2}, {k-1, k+1, k+3}, {k-2, k+2, k+3}, {k-1, k, k+4}]
                p3 = Ds in pats
                p4 = (k == 3 and Ds == {4, 5, 6}) or (k == n - 3 and Ds == {k-1, k, k+1})
                if ((a + 3) not in s) != p3 or ((a + 4) not in s) != p4 or (a + 5) not in s:
                    mis += 1
                    if mis <= 5: print('mismatch', N, D, k, 'a+3 missing', (a+3) not in s, 'a+4 missing', (a+4) not in s, 'a+5 missing', (a+5) not in s)
print('cases', n_cases, 'mismatches', mis)
