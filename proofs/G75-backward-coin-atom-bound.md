# backward coin atom bound

*GPT's proofs, second-read by Local. Derived from [PROOFS.md](../PROOFS.md), entry "G.GPT75. backward coin atom
bound (second-read by Local, 2026-10-06)"; rebuild with `python3 proofs/build.py`. Edit the proof in PROOFS.md and
this summary in [summaries.md](summaries.md), never this file.*

**Status:** proved by GPT and second-read by Local.

## In plain words

Those weights are uniformly small: about (log h)/√h, where h is the number of steps still to go.

**What it says.** How much one extra odd step changes the chance of surviving h more fair coin tosses is at most
about (log h)/√h, whatever the state.

**Why it matters.** Late imbalances count for little. It controls the coin side only; the real Collatz imbalances
still need their own bound.

**An everyday picture.** One point dropped in the first week of a long football season barely changes who ends up
top; the more matches still to play, the less it matters.

## The formal statement and proof

### G75. A uniform atom bound for the backward coin weights (2026-10-06)

G74's weights can be bounded without any assumption on the actual Collatz ensemble. Write h=T-t-1>=0 for the number of future coin bits after the selected child. For every integer L>=1,

    max_a Delta_t(a)
      <=min(1, L/sqrt(h+1)+32*exp(-(L-1)/2)).

Choosing L=ceil(4*ln(h+1))+1 proves a uniform O(log(h+1)/sqrt(h+1)) bound as h tends to infinity. This controls the coin completion weights only. It neither bounds actual class imbalances nor proves bounded count excess.

**Proof.** Use G74's future-bit count Z_h and maximum demand J. Reverse the h fair bits and write S_k=Z_h-Z_(h-k), with S_0=0. Algebra gives

    J=ell_T-Z_h+R,
    R=max_(0<=k<=h) (S_k-(ell_T-ell_(T-k))).

Here R is a nonnegative integer, since k0 contributes0. Let beta=log(2)/log(3). The ceiling identity ell_j=ceil(beta*j) implies ell_T-ell_(T-k)>beta*k-1. The exact inequality3^5<2^8 gives beta>5/8. For integer r>=1, R>=r therefore requires some k>=1 with

    S_k-k/2>r-1+k/8.

For completeness the needed fair-binomial tail estimate is elementary: E exp(theta*(S_k-k/2))=cosh(theta/2)^k<=exp(k*theta^2/8). The inequality follows from tanh(u)<=u for u>=0 by integration. Markov's inequality, optimized at theta=4*x/k, gives Pr(S_k-k/2>=x)<=exp(-2*x^2/k) for x>=0. Apply this with x=r-1+k/8 and take a union bound; independence of different suffix sums is not required. Since

    2*(r-1+k/8)^2/k >= (r-1)/2+k/32,

we obtain

    Pr(R>=r)<=exp(-(r-1)/2)*sum_(k>=1) exp(-k/32)
             <32*exp(-(r-1)/2).

The central atom of Binomial(h,1/2) is at most1/sqrt(h+1). One direct proof: for h=2j its maximum is p_(2j)=binom(2j,j)/4^j; p_0=1 and p_(2j+2)/p_(2j)=(2j+1)/(2j+2). Induction uses (2j+1)*(2j+3)<(2j+2)^2 to give p_(2j)<=1/sqrt(2j+1). The odd maximum p_(2j+1)=p_(2j)*(2j+1)/(2j+2) is at most1/sqrt(2j+2).

For any integer v, split the event J=v into R0..L-1 and R>=L. Each small-R event is contained in Z_h=ell_T+r-v, regardless of dependence between R and Z_h. Thus

    Pr(J=v)<=sum_(r=0)^(L-1) Pr(Z_h=ell_T+r-v)+Pr(R>=L),

which gives the displayed bound and, for the stated L, tail term at most32/(h+1)^2. Since Delta_t(a)=Pr(J=a+1), the claim follows. The h0 case is included, though its bound is simply1. This is a standard concentration-plus-truncation argument, not a new probability theorem; prior art is recorded separately.

**Unexpected dependence guard.** Take T3,t1,h1. Then ell_2=ell_3=2, so J=max(2,2-Z_1)=2, while R=Z_1. Its demand distribution has an atom of1, even though Z_1 has maximum atom1/2. Dropping R, or importing the binomial atom bound directly for J, is wrong. The proof above keeps the dependence and its truncation cost. It also shows why no short-horizon square-root estimate with constant1 is asserted.

**Next controls, preregistered NOT RUN.** WA1: reuse G74's complete future-string population T1..10. For each word verify the reverse decomposition, then compare exact R tail probabilities to the conservative geometric bound for every attained positive r, and each J atom to the displayed bound for L1..8. Predict no failure; retain bounds above1 as vacuous rather than evidence of sharpness. WA2: verify the central-binomial induction inequality by exact squared-integer comparisons for h0..256, and independently enumerate the T3,t1 guard. Counterfactual: max atom of J never exceeds max atom of Binomial(h,1/2); must fail at h1 above. No actual-orbit distribution measurement, asymptotic constant estimate or large Local job. Independent proof reading requested.


### G75 controls outcome (2026-10-06)

WA1 passes2036 exact reverse decompositions across all future coin strings for T1..10,57 overshoot-tail comparisons and1304 atom comparisons for L1..8. All1304 atom bounds are vacuous (the uncapped expression exceeds1) at this deliberately small scope: this run does not empirically exercise a nontrivial atom bound or measure decay. Tail and atom exponential comparisons use floating arithmetic with1e-14 tolerance, while probabilities and reverse identities are exact. WA2 passes257 exact squared-integer central-binomial bounds for h0..256. The unexpected T3,t1 guard is confirmed: J has an atom of1 and R equals the fair bit, refuting the direct binomial-atom shortcut.

Probe: `tests/probes/prizes/collatz_gpt_weight_atoms.py`; predictions at51a1a0e, GPT's Intel host, Python, under1 s. No control failed. The asymptotic atom bound remains the analytic result, pending independent reading; the small controls do not demonstrate its asymptotic usefulness. No actual-orbit or Local computational job was run. The remaining count problem is to control actual signed class imbalances against these weights.

*Second reader's note on G74 and G75 (Local, 2026-10-06; chat L041).* Both correct. G74: an odd parent's child has
$f_{t+1}(a+1) = f_t(a) + \Delta/2$ and an even parent's $f_{t+1}(a) = f_t(a) - \Delta/2$, so
$H_{t+1} - H_t = \tfrac12 \sum_a I \Delta$; $H_m = 2^m V(T)/2^T$ because every admitted length-$T$ word has an admitted
length-$m$ prefix; and a child survives exactly when $a \ge J$, so $\Delta_t(a) = \Pr(J = a + 1)$; the width-3 guard
checks. G75: with $j = T - k$ the demand is $J = \ell_T - Z_h + R$; $3^5 < 2^8$ gives $\beta > 5/8$; the Hoeffding tail and
$\sum_k e^{-k/32} < 32$ hold; the central-atom induction rests on $(2j+1)(2j+3) < (2j+2)^2$; the $T = 3$ guard checks.
Checked independently (`collatz_audit_g67_g69.py`): G74's telescoping identity in exact rationals in 180 cases
(widths 2 to 13, $T = m$ to $m + 14$, direct trajectories); G75's bound against the exact distribution of $J$ by dynamic
programming, which makes the bound non-vacuous for the first time (0.977 at $h = 200$, 0.822 at $h = 300$, against exact
maximum atoms 0.058 and 0.047). The exact atoms decay like $1/\sqrt{h}$ with no visible logarithm (ratio 1.55 from
$h = 128$ to 300 against $\sqrt{300/128} = 1.53$), so the bound's $\log$ factor looks like a cost of the proof.
