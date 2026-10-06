# fixed-order temporal differences preserve entropy but not the repeat sign

*GPT's proofs, second-read by Local. Derived from [PROOFS.md](../PROOFS.md), entry "G.GPT148. fixed-order temporal
differences preserve entropy but not the repeat sign (second-read by Local, 2026-10-07)"; rebuild with `python3
proofs/build.py`. Edit the proof in PROOFS.md and this summary in [summaries.md](summaries.md), never this file.*

**Status:** proved by GPT and second-read by Local.

## In plain words

Taking acceleration, jerk or another fixed order of XOR temporal difference does not change a binary trace’s word-count entropy: the difference block loses at most its first few input bits. These fields can still expose particular patterns, such as whether a good return repeats or flips the symbols. But quiet temporal differences do not establish a finite spatial tail: the stationary checkerboard has zero differences at every depth and infinitely many black cells. Ordinary signed differences and XOR differences also have different meanings.

## The formal statement and proof

### G148. Fixed-order temporal differences preserve entropy but not the repeat sign (2026-10-07)

**Status and target.** Symbolic diagnostic audit, independent review pending. No experiment, shader change or new general finite-difference novelty claim. The owner linked the project to temporal motion fields; WHAT-WE-BUILT.md's overview and motion-field description were read, alongside the existing G96 transport guard, G138/G139 stationary-tail controls and G143's Sturmian derivative. Prediction: every fixed-order XOR temporal difference has the same word-count entropy as the original binary trace. Counterfactual: going to acceleration, jerk or another fixed order automatically reveals positive entropy missed by the visible trace. The elementary block argument refutes that implication, without refuting uses of these fields for specific structural diagnostics.

Let S shift a one-sided binary word forward, and let D=1+S over GF(2). For any fixed k>=1, D^k is the order-k XOR temporal difference. If P_x(n) counts the distinct length-n factors of x, then

    P_(D^k x)(n) <= P_x(n+k) <= 2^k P_(D^k x)(n).

The first inequality holds because the difference block is a fixed function of its n+k input symbols. For the second, each output block and the first k input bits determine all the remaining input bits: the coefficient of x_(s+k) in (D^k x)_s is one, so solve sequentially for x_k,x_(k+1),...,x_(n+k-1). There are at most 2^k possible first k bits. Thus the word-count entropies agree (using limsup log2(P(n))/n, and invariance under the fixed length shift k). This is valid for one word and its factors, not only for the full shift.

In particular every fixed-order difference of G143's silver code still has zero word-count entropy. The combined jet (x,Dx,...,D^k x) has exactly P_x(n+k) distinct length-n vector factors: its first component gives the n observed input bits; at the last observed time, levels 1 through k form a triangular system recovering the next k input bits in order, because each level has coefficient one on its newest input. Keeping all levels cannot add an entropy rate either. No assertion is made for k growing with the observation length, or for unbounded spatial windows.

**Period and sign controls.** G96 already proves the dyadic identity D^(2^m)=1+S^(2^m); it is reused, not rediscovered as a new result. Thus at these orders a zero difference interval is exactly an equality interval with lag 2^m. A nonzero difference distinguishes a complement-repeat from a repeat, which is the sign lost in the Sturmian integration in GC158. If D^k x is eventually zero, choose 2^m>=k and multiply by D^(2^m-k): x is eventually periodic with period dividing 2^m. More generally eventual periodicity of D^k x implies eventual periodicity of x, by integrating each order: when Dy is p-periodic, y_(s+p) XOR y_s is the constant parity of one derivative period, hence y is 2p-periodic. Iterating gives a sufficient period 2^k p. This period bound is not claimed optimal.

These XOR observables are different from ordinary signed finite differences on integer-valued samples. If an ordinary order-k difference of a bounded integer sequence is eventually zero, successive summation makes its tail a polynomial of degree at most k-1; boundedness forces that polynomial to be constant. For the alternating binary trace 0101..., D^2 x is zero, but its ordinary second difference is the alternating sequence -2,2,-2,2,... . XOR acceleration zero therefore does not mean a constant binary state, or zero ordinary acceleration.

**Unexpected support guard and next obligation.** G138's constant-zero visible code has the stationary checkerboard forced left row, with infinitely many ones. Every fixed-depth temporal column is constant, so all positive-order temporal differences vanish there, under either arithmetic. The derivatives discard the stationary spatial background. This directly refutes inferring finite spatial support from quiet temporal jets, even when every fixed order at every fixed depth is checked. G96 separately explains why fixed-cell differences are not physical acceleration of tracked structures. A productive next use must name a coupled spatial constraint or a specific phase/sign relation; it cannot rely on a generic entropy increase, derivative quietness or the mere word 'acceleration'. No finite initial-tail exclusion or prize claim follows.

*Second reader's note on G148 (Local, 2026-10-07; chat L104).* Correct, with both points GPT asked me to audit
confirmed. The block inversion: the coefficient of $x_{s+k}$ in $(D^k x)_s$ is $\binom{k}{k} = 1$, so the first $k$
input bits and an output block of length $n$ fix the input block of length $n + k$, giving
$P_x(n+k) \le 2^k P_{D^k x}(n)$. The joint jet: the first component gives the $n$ observed bits, and at the last
observed time level $j$ has coefficient one on $x_{t+j}$ with all its other inputs already known, so the jet block and
the input block of length $n + k$ determine each other and the count is exactly $P_x(n+k)$. The integration period $2p$,
the dyadic identity owned by G96, the ordinary-difference contrast and the stationary checkerboard all hold. The
checkerboard is fixed by every single wall step, since every cell has a black cell among its centre and right inputs
(the wall included) and so becomes the complement of its left neighbour, which is its own value. Checked
(`rule30_audit_g99_g100.py`, S43): both inequalities and the exact jet count for $k \le 5$ and $n \le 12$ on GC159's
silver prefix and 20 random words; the dyadic identity for $m \le 4$; the period $2p$ for every derivative pattern with
$p \le 6$; the $0101\ldots$ contrast; and the checkerboard fixed for 40 single steps.
