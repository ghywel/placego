#!/usr/bin/env python3
"""unrestricted_closing_replay.py (Local, 10 November 2026; S-23, Cloud's K-08): the plain-Python replay of the
worked-numbers cell of the unrestricted-closing essay. Usage: python3 unrestricted_closing_replay.py

The zero-boundary left half: depth k >= 1, a white wall at depth 0, one tick x(k, t+1) = x(k+1, t) xor (x(k, t) or
x(k-1, t)), and G = two ticks. Rows A = (1011111)^inf, B = 11 (01001011001000)^inf, C = (1100001)^inf from depth 1.
Written independently of the Lean module.

Prediction (written before the first run, from Cloud's LN-03.1 normal forms, GPT's GC2853 and Local's L1654 check):
G A = G B = C and G C = A on every depth checked; depth 1 is black at every even tick for 40 double steps from each
row; the free words (depth 1 at odd ticks) begin 10101010, 00101010 and 01010101; for depths d >= 3, A and B differ
exactly when d mod 14 is one of 0, 1, 3, 5, 6, 8, 9, 11, 12; and after one tick A is white and B black at every depth
14q + 4. Counterfactual: a mismatch refutes the witness or the essay's description of it.
It prints {G A = C, G B = C, G C = A, even heads black, the free words, the mismatch residues, one-tick split}."""
N = 700
pa, pb, pc = [1, 0, 1, 1, 1, 1, 1], [0, 1, 0, 0, 1, 0, 1, 1, 0, 0, 1, 0, 0, 0], [1, 1, 0, 0, 0, 0, 1]
A = [0] + [pa[(d - 1) % 7] for d in range(1, N)]
B = [0, 1, 1] + [pb[(d - 3) % 14] for d in range(3, N)]
C = [0] + [pc[(d - 1) % 7] for d in range(1, N)]


def tick(s):
    return [0] + [s[k + 1] ^ (s[k] | s[k - 1]) for k in range(1, len(s) - 1)]


def G(s):
    return tick(tick(s))


M = N - 100  # depths far from the truncation edge
same = lambda x, y: x[1:M] == y[1:M]


def heads_and_free(s, T=40):
    black, free = True, ''
    for t in range(T):
        black &= s[1] == 1
        if t < 8:
            free += str(tick(s)[1])
        s = G(s)
    return black, free


hA, fA = heads_and_free(A)
hB, fB = heads_and_free(B)
hC, fC = heads_and_free(C)
res = sorted({d % 14 for d in range(3, M) if A[d] != B[d]})
ok_res = all((A[d] != B[d]) == (d % 14 in res) for d in range(3, M)) and A[2] != B[2] and A[1] == B[1]
X, Y = tick(A), tick(B)
split = all(X[14 * q + 4] == 0 and Y[14 * q + 4] == 1 for q in range((M - 10) // 14))
print('{%s, %s, %s, %s, {"%s", "%s", "%s"}, {%s}, %s}' % (
    same(G(A), C), same(G(B), C), same(G(C), A), hA and hB and hC, fA, fB, fC,
    ', '.join(map(str, res)), ok_res and split))
