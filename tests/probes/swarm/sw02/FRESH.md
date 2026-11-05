# A question about an iteration on the natural numbers

Write bitwise operations on natural numbers in the usual way, with `>>` and `<<` the shifts, and define

    F(Y) = (Y >> 1) XOR (Y OR (Y << 1)),        G(Y) = F(F(Y)).

**Question.** Does every natural number reach an even number under some iterate of G?

This is open. F is one step of the elementary cellular automaton Rule 30 on the bit positions 0, 1, 2, ..., with a cell below
bit 0 that is white for ever.

**Definitions.** t counts applications of F. For W ≥ 1, S_W(t) is the number of Y with 0 ≤ Y < 2^W such that bit 0 of
F^(2s)(Y) is 1 for every s with 2s ≤ t. D(W) is the largest, over 0 ≤ Y < 2^W, of the first even t at which bit 0 of F^t(Y) is 0.

**Verified facts** (a machine-checked proof, or a computation, as labelled).
- F adds exactly one to the bit-length of a nonzero Y. Proved.
- For 0 ≤ t < W, S_W(t) = 2^(W − floor(t/2) − 1). Proved.
- D(1..14) = 2, 6, 6, 6, 8, 10, 12, 12, 18, 18, 30, 30, 30, 32. Computed.
- D(52) = 96, D(56) = 100, D(60) = 114. Machine-checked. D(76) ≥ 138, machine-checked lower bound.
- Every Y up to width 60 reaches an even number. Machine-checked.

Exhaustive computation on small cases is available to you through the queue described in your task.
