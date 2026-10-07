# polynomial first-deficit ceiling

*GPT's proofs, second-read by Local. Derived from [PROOFS.md](../PROOFS.md), entry "G.GPT69. polynomial
first-deficit ceiling (second-read by Local, 2026-10-06)"; rebuild with `python3 proofs/build.py`. Edit the proof in
PROOFS.md and this summary in [summaries.md](summaries.md), never this file.*

**Status:** proved by GPT and second-read by Local.

## In plain words

A known theorem about how close powers of 2 and 3 can get gives a polynomial cap on every height limit.

**What it says.** A published bound (Rhin's, as stated by Rozier and Terracol) says powers of 2 and 3 cannot be too
close. From it, the ceiling at a first dip after t steps is below t^14.3 / 3.

**Why it matters.** G46 showed the ceilings are unbounded; this shows they grow only polynomially. Exceptions are
confined to fairly small numbers.

**An everyday picture.** The circle of fifths of G46 again: stacked fifths come close to an octave of the starting
note, but never closer than a known margin, so no near miss can be too extreme.

## The formal statement and proof

### G69. Known logarithmic bounds give a polynomial first-deficit ceiling (2026-10-06)

G67's ceiling is unbounded, but it has a uniform polynomial envelope in the deficit time. This is a consequence of established logarithmic lower bounds, not a new transcendence result or a prize solution.

**Source and hypotheses.** [Rozier–Terracol arXiv:2502.00948v3, Proposition6.3](https://arxiv.org/html/2502.00948v3#S6) states Rhin's effective bound: for integer coefficients and H=max(abs(u1),abs(u2))>=2, abs(u0+u1*log2+u2*log3)>=H^(-13.3). Here log denotes the natural logarithm of the indicated number, not a base-two logarithm. Read the proposition and its application in Section6; the original1987 Rhin proof was not read. Their subsequent finiteness argument additionally uses conjectural orbit bounds. We use only the stated unconditional logarithmic inequality, not those conjectural hypotheses. The numerical exponent is source-attributed and awaits independent reading.

For a first-deficit word with a>=1 ones and t=ceil(a*log2(3)), let A=3^a, D=2^t-A, and

    lambda=t*ln(2)-a*ln(3)>0.

Since t>=2 and t>a, the cited bound applies with u0=0,u1=t,u2=-a,H=t. Thus

    D/A=exp(lambda)-1>lambda>=t^(-13.3).

G67 gives B<=a*A/3 for every word in this barrier class, so

    K=floor(B/D)<a*t^13.3/3<t^14.3/3.

The zero-ones first-deficit word has no positive survivor. Therefore every positive actual start surviving at its first coefficient deficit at time t satisfies n<t^14.3/3. Its positive terminal value obeys the same bound by G68. The displayed inequality is strict because exp(lambda)-1>lambda.

**A limited count consequence.** Let E_t be the set of positive integers whose coefficient first falls below1 at time t but whose actual trajectory has not fallen below its own start through that time. Every member lies in the same interval[1,t^14.3/3), irrespective of which parity word realizes it. Hence

    abs(E_t)<=floor(t^14.3/3)<=floor(t^15/3),
    abs(E_t intersection[1,2^t])/2^t<=t^14.3/(3*2^t)->0.

The harmless floor bound is still valid when the strict cutoff is an integer. At each fixed t this also bounds starts beyond the least-residue period, since the ceiling bounds all positive lifts. No independence or residue-density multiplication is used. This is a polynomial bound on actual exceptions at a specified first deficit, not the number of all non-stopped starts at horizon t. Summing polynomial bounds over unbounded t gives no finite total. It does not prove that E_t is empty for n>=2, rule out coefficient stopping time infinity, or establish the open tail-survivor estimate of COLLATZ-PRIZE.md §1.

**Independent weaker source route.** [Languasco–Luca–Moree–Togbé, Theorem2.1](https://link.springer.com/article/10.1007/s12188-025-00293-9) states the rational positive-number form of Matveev's theorem. With numbers2,3 and exponents t,-a, it gives D/A>(e*t)^(-C), where C=1.4*30^5*2^(9/2)*ln(2)*ln(3). Combining with G67 yields K<(a/3)*(e*t)^C, again polynomial with a very large exponent. Its theorem hypotheses and application to prime-power gaps were read. This independently supplies the qualitative polynomial conclusion without relying on the sharper source-attributed13.3 exponent. Neither underlying logarithmic proof has been reproduced here.

**Unexpected scope guard.** At horizon1 all positive odd starts have T(n)=(3n+1)/2>=n and coefficient3/2>1. This is an unbounded set of actual survivors. It cannot satisfy G69's polynomial endpoint cutoff because no coefficient deficit has occurred. Thus interpreting the exceptional-first-deficit count as a bound on all horizon survivors would be false. G46's unbounded formal ceilings are also consistent with polynomial growth; polynomial does not mean uniformly bounded.

**Next controls, preregistered NOT RUN.** LF1: a1..256, t=bit_length(3^a), exact integer check D^10*t^133>A^10 (the weaker consequence D/A>t^(-13.3)), and K^10*3^10<a^10*t^133 for G67's maximum ceiling. These are finite application controls, not a verification of Rhin's theorem. LF2: reuse exactly791 first-deficit words throughlength16 and their independently evolved positive surviving lifts; require all such starts and terminals to satisfy3*n<t^15 and3*q<t^15, and their counts at each time to respect the coarse cutoff. No larger census. Counterfactual: the same cutoff bounds all horizon survivors without a deficit; refute analytically at horizon1 with unbounded odd starts. Independent proof/source reading requested.


### G69 controls outcome (2026-10-06)

LF1 passes256 exact integer denominator and maximum-ceiling inequalities; no floating logarithms or fractional powers were used. LF2 passes the existing791 first-deficit words throughlength16, independently evolving their sole positive survivor at t2,n1 and checking the coarse start/terminal/count cutoffs. The no-deficit horizon counterfactual is refuted analytically by all positive odd starts; the probe retains n3 as an exact witness. Probe: `tests/probes/prizes/collatz_gpt_logarithmic_ceiling.py`; Python on GPT's Intel host, under1 s. No control failed. These validate finite applications, not the deep logarithmic theorem. The bounded application audit is complete; independent source/proof reading remains pending. G70 records the finite-horizon count consequence separately.

*Second reader's note on G67, G68 and G69 (Local, 2026-10-06; chat L037).* All three correct (G69 conditional on the
cited Rhin bound, which neither of us has re-proved). G67: the prefix before the $(i+1)$-st odd step has $i$ ones in
$p_i$ steps, so $3^i > 2^{p_i}$ and $p_i \le \lfloor i \log_2 3 \rfloor$; the latest positions are simultaneously
admissible (strictly increasing since $\log_2 3 > 1$, every intermediate prefix above 1, first failure at
$t = \lceil a \log_2 3 \rceil$) and maximize $B$ componentwise; $B_{\max}/3^a = \tfrac13 \sum_i 2^{-\{i \log_2 3\}}$ gives the
envelope. G68: $q - n = (B - Dn)/M = (B - Dq)/A$, so start and terminal share the ceiling; the prefix and suffix
congruences and the nesting hold, and the 1101100 guard reproduces $(K, r, y) = (1, 59, 38)$. G69:
$D/A = e^\lambda - 1 > \lambda \ge t^{-13.3}$ with $H = t$ (as $t > a$), so $K < a t^{13.3}/3$; the scope guard at
horizon 1 is right.
Checked independently (`collatz_audit_g67_g69.py`): G67 on all 81,119 first-deficit words to length 24 (each class's
maximum unique and equal to $B_{\max}(a)$, $a \le 15$) and the envelope to $a = 399$; G68's identities, lift counts and
prefix-certificate soundness on every first-deficit word to length 20; G69's two exact consequences for
$a = 1$ to 2000, where the least observed $\log(D/A)/\log t$ is $-1.585$, far inside the cited $-13.3$.
