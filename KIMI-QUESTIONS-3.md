# Rule 30 beside an alternating wall: the finite-pattern form

Third set, self-contained like the second. Same rule, wall and notation as KIMI-QUESTIONS-2.md (x_{t+1}(i) = x_t(i-1)
XOR (x_t(i) OR x_t(i+1)); wall x_t(0) = t mod 2; visible sequence v_k = x_{2k}(1); forced left half; record R(d)).
Mark every assertion **proved**, **computed** or **conjectured**; give computations in a rerunnable form.

## Corrections to your second answer (please confirm or rebut)

1. Your closed form x_0(-8) = (1 - v0)(v1 OR v2) v3 is wrong on two of the sixteen inputs: at v0 v1 v2 v3 = 1011 and
   1111 the cell is 1. The correct form is x_0(-8) = v3 (v2 OR ((1 - v0) v1)). Your worked example for R(2) = 6 uses
   the input 0101, where both forms agree, so that proof stands.
2. "R(d) - d = 4 only at d = 2" misses d = 13: your own list has R(13) = 17.
3. Your triangle propagation R(d + 2j) >= R(d) - 4j is correct (a zero run shrinks by one cell at each end per time
   step) but weaker than the trivial sub-run bound: a run from depth d of length L contains a run from depth d + 1 of
   length L - 1, so R(d + 1) >= R(d) - 1 and R(d + 2j) >= R(d) - 2j.
4. Your proposed route, "show each new even-depth check erases a positive-measure cylinder", cannot give finiteness by
   itself: a nested intersection of sets can lose positive measure at every step and stay nonempty (a Cantor set).
   Finiteness of R(d) is the statement that the feasible set is **empty** after finitely many checks.
5. You were right about our §B comparison: the values 16, 15, 14 quoted there at d = 20, 21, 22 are from the other
   quantity (configurations on all of Z), not the free model; the free model has R(20) = 14, as you computed.

## The forward view (please prove C1 and C2, then use them)

Run the left half **forward** with the wall as a boundary condition: for i <= -1,
x_{t+1}(i) = x_t(i-1) XOR (x_t(i) OR x_t(i+1)), with x_t(0) = t mod 2 and no reference to column 1 at all.

**C1 (characterisation).** A left half-line configuration y = (x_0(-1), x_0(-2), ...) is the forced left half of some
visible sequence v if and only if its forward evolution has x_t(-1) = 1 at every odd t (equivalently, x_t(-2) and
x_t(-1) differ at every even t). When it is, v_j = 1 XOR x_{2j}(-1).
(Why: at odd t the wall's own update x_{t+1}(0) = x_t(-1) XOR (x_t(0) OR x_t(1)) reads 0 = x_t(-1) XOR 1; at even t it
reads 1 = x_t(-1) XOR x_t(1), which fixes x_t(1) and constrains nothing on the left.)

**C2 (finite patterns).** For a word w of n cells placed at depths 1 .. n with every deeper cell 0 (a finite pattern
beside the wall), let T(w) be the first odd time t at which x_t(-1) = 0 in its forward evolution (T(w) = infinity if
there is none), and S(n) = max over the 2^n words of T(w). Then
    d + R(d) = 1 + S(d - 1)   for every d >= 1.
(Why: a cell at depth k >= 2 beyond the pattern enters x_t(-1) for the first time at t = k - 1, through the left edge of
the light cone, which is a pure XOR; so for even k the condition at odd time k - 1 forces that cell, and the run from
depth d is exactly the pattern's survival. Depth d + R(d), the first forced 1 after the run, is therefore always even.)

Data to check against (from the exact R(d)): S(0 .. 17) = 1, 7, 7, 7, 7, 9, 9, 9, 17, 17, 17, 17, 29, 29, 29, 31, 31,
31. The plateaus are the point: one word of n cells serves every shorter prefix of itself padded with zeros.

So the whole question "is R(d) finite for every d" is this: **can a finite pattern beside the alternating wall keep
the cell next to the wall black at every odd time for ever?** The conjecture R(d) <= d + 4 reads S(n) <= 2n + 5: a
pattern of n cells fails by about twice its width.

## Questions

**C (main).** Prove S(n) < infinity for every n, with any explicit bound F(n) (the conjecture is 2n + 5; a weak bound
is still the result). Structure you may use: the pattern's leftmost cell moves one site left per step and is always
black (x_{t+1}(p-1) = 0 XOR (0 OR 1) when p is the leftmost black cell), so the k-th diagonal from the left edge,
D_k(t) = x_t(-n-t+k), obeys D_k(t+1) = D_{k-2}(t) XOR (D_{k-1}(t) OR D_k(t)): a triangular system in which the first
n diagonals never see the wall and every later diagonal is born at the wall. The wall's condition is on the births.

**C'.** If C is out of reach, prove the strongest statement you can about S(n). For example: (i) S is nondecreasing
and S(n) + 1 is even (both should be easy); (ii) an exact S(n) for n <= 25 or as far as you can compute, with the
maximising words and how many there are; (iii) any linear or polynomial upper bound on S(n) for a restricted class of
patterns (for instance words whose first k cells are fixed), with proof.

**D (the other phase).** With the wall in the other phase, x_t(0) = (t + 1) mod 2, define R°(d) in the same way (runs
at time 0, the condition now at even times). Computed: R°(d) = R(d - 2) for every d from 5 to 27, and R°(3) = R(1),
R°(4) = R(2). Prove this identity for all d, or find the first depth where it fails. Hint: the other phase is the same
problem one time step later, but a zero run at time 1 is not simply a shrunken run at time 0, since the time-0 row is
recovered from the time-1 row by the same XOR-OR solving step.

## How to answer

- Prove C1 and C2 first (they are short), check C2 against the data above by computation, then C, C', D.
- Mark every assertion **proved**, **computed** or **conjectured**; prove every lemma you use or say you assume it.
- Give computations in a rerunnable form, and keep the raw outputs.

**GPT correction, 2026-10-10 (GC1043; second reading requested).** D's
definition correctly tests EVEN times under the black-start wall, but
its quoted data came from WA3, which kept the ODD-time test after
changing the wall phase. Those are different games. The correctly
defined R°(3) is4: formal forced prefix1100001 attains four zeros
from depth3; every prefixab00000 fails at even0,2 or6. Moreover any
finite black-start record has d+R°(d) odd, opposite to the endpoint
parity of the quoted R(d-2). See RULE30-GPT GC1043 and the literal
controls in rule30_black_wall_scope.py. C1/C2 are not changed by this
correction; the stated phase identity D is refuted at its first depth3.
