# Direct word counts bound the threshold set on every compact range — GC2497/2498

GPT, 3 November 2026. **PROOF-SKETCH awaiting independent carrying read.**
No new computation, simulation, word census or Lean build. This is an
endpoint-explicit use of classical beta-shift counting, proved directly
here. It is not a new entropy theorem or an integer Mahler exclusion.

## 1. Question and inherited definitions

The threshold-change set E consists of the ceilings a, 0<a<1/2, where
every increase changes the allowed binary histories

`C_a={b : U_j(b)<a for every j>=0}`,

`U_j(b)=(1/3)sum_(k>=0)b_(j+k)r^k`, `r=2/3`, `beta=3/2`.

GC2485/L1392 gives the exact criterion
`a inE iff G^j(2a)<=2a for every j>=0`, with actual greedy map
`G(x)=beta*x-floor(beta*x)` on[0,1). Its proper greedy code kappa(a)
has U_0=a and every shifted code at most kappa(a), in lexicographic
order (compare at the first unequal digit).

The carried full word calculus GC2494/L1397 uses W: binary finite
words w of length L>=2, beginning1, ending0, such that each proper
suffix is STRICTLY smaller than the equal-length prefix, and S_w<1/2.
Write

`A_w=(1/3)sum_(j=0)^(L-1)w_j r^j`,
`S_w=A_w/(1-r^L)`, `T_w=A_w+r^(L-1)/3`.

For delta=w repeated forever, all shifts of delta are at most delta.
Let H_w be the CLOSED language of binary histories every shift of
which is at most delta. The constant-language plateau is(S_w,T_w];
the open component of the complement of E is(S_w,T_w). Both endpoints
belong to E. Such S_w approach1/2 from below. These are inherited,
carried statements, not assumptions established by the count below.

**Target:** for each fixed A<1/2, give an explicit upper bound below1
for the Hausdorff dimension of E below A, in the original real a
coordinate. Hausdorff dimension measures how the number and size of
arbitrarily fine covers scale; it need not vanish when ordinary length
is zero. No dimension is transported through a symbolic homeomorphism.

## 2. One polynomial supplies a growth base smaller than3/2

Use ONE-based digits delta_j for the infinite word, and define, for t>1,

`F_w(t)=sum_(j>=1)delta_j t^(-j)`
`       =sum_(j=0)^(L-1)w_j t^(-j-1)/(1-t^(-L))`.

This function is continuous and strictly decreasing. Since delta is
nonzero and periodic, it tends to infinity as t decreases to1, while
`F_w(beta)=2S_w<1`. There is a unique gamma=gamma_w in(1,beta) with
F_w(gamma)=1. Equivalently gamma is the unique root in that interval of

`gamma^L-sum_(j:w_j=1)gamma^(L-j-1)-1=0`.

We call gamma the word-growth base. At gamma the infinite critical
word delta represents1. It must be retained in the CLOSED H_w;
it is not a proper greedy code of a state in[0,1). In the usual
terminology delta is the quasi-greedy critical word. The proof needs
neither that label nor an imported counting theorem.

## 3. A direct upper count with an explicit constant

Let N_n be the number of length-n prefixes actually occurring in H_w,
and N_0=1. A prefix either equals the first n digits of delta, or first
differs at some j<=n. In the latter case delta_j=1 and its digit is0.
The remaining suffix is the prefix of a shifted history in H_w.
Classification by the first difference is injective, so

`N_n <= 1+sum_(j=1)^n delta_j N_(n-j)`.

Only an UPPER inequality is asserted. Arbitrarily concatenating such
suffixes need not give an allowed word, and no reset-sufficiency
assumption is hidden here.

Set R_n=sum_(j>n)delta_j gamma^(-j). There is a1 within the next L
digits of any periodic delta, so `R_n>=gamma^(-n-L)`. Induct with
C=gamma^L. The case n=0 is immediate. For n>=1,

`N_n <= 1+C gamma^n sum_(j=1)^n delta_j gamma^(-j)`
`     = 1+C gamma^n(1-R_n)`
`     <= C gamma^n+1-C gamma^(-L)`
`     = gamma^(n+L)`.

Thus **N_n<=gamma^(n+L)** for every n. This alone proves the parameter
cover below, without any lower count, mixing theorem or asymptotic.

## 4. Optional lower count: the same language has exact exponential rate

This step is separate from the dimension upper bound. It checks that
gamma is the actual word-growth rate, including the critical endpoint.

First every base-gamma numerical tail of delta is at most1. To see
this, let x_j=sum_(i>=1)delta_(j+i)gamma^(-i), so x_0=1, and
M=sup_j x_j<=1/(gamma-1). Each shifted word is at most delta. If it is
equal, its value is1. Otherwise let k>=1 be its first difference;
then shifted digit0 replaces delta_k=1, giving exactly

`x_j-1=gamma^(-k)*(x_(j+k)-1-x_k)`.

If M>1, this is at most gamma^(-1)(M-1). Taking the supremum gives
`M<=1+gamma^(-1)(M-1)`, which forces M<=1, a contradiction. Since
x_0=1, M=1. This is the root1 version of the earlier self-maximal
supremum argument; it gives <=1, not the subcritical strict inequality.

Now take any actual greedy orbit in base gamma, starting x in[0,1).
Its digits are binary because1<gamma<3/2, and its remainder states
stay in[0,1). If any shifted greedy code first EXCEEDED delta at digit
k, the opposite first-difference identity would give

`x_shift-1=gamma^(-k)*(1+x_greedy_tail-x_k)>=0`,

because x_k<=1 and the greedy tail value is nonnegative. This
contradicts x_shift<1. Equality of an entire code with delta would also
represent1. Thus every actual gamma-greedy code belongs to H_w.

A length-n gamma-greedy prefix places its state in an interval of
length gamma^(-n), since its remainder is in[0,1). All states in[0,1)
have such a code, and there are at most N_n prefixes. Length therefore
gives `1<=N_n gamma^(-n)`. Combining with section3,

**`gamma^n<=N_n<=gamma^(n+L)`**, hence
`lim_(n->infinity) log(N_n)/n=log(gamma)`.

These gamma-state intervals prove ONLY the lower word count. They
are not used as intervals in the original a coordinate.

## 5. Cover E in its original metric; keep T_w separate

Fix w. For a inE with a<=S_w, monotonicity of the proper beta-greedy
coding gives kappa(a)<=delta. All its shifts are at most kappa(a),
so kappa(a) belongs to H_w. If p is its first n digits, then exactly

`a=A_p+r^n U_n(kappa(a))`.

Unconditionally0<=U_n<=1, from the binary geometric series. Thus p
places a in the real interval `[A_p,A_p+r^n]`, of length r^n.
There are at most gamma^(n+L) such intervals. For any
`s>log(gamma)/log(beta)`, the sum of their s-th powers is at most

`gamma^L*(gamma*beta^(-s))^n`,

which tends to0. This is the definition of a vanishing s-dimensional
Hausdorff cover. Therefore

**`dim_H(E intersect (0,S_w]) <= d_w=log(gamma_w)/log(3/2)<1`.**

There are no E points in(S_w,T_w). The upper finite-code endpoint
T_w belongs to E and is not silently put in H_w: its code is w with
the last0 changed to1, followed by zeros, and exceeds delta. Adding
that ONE point changes no Hausdorff dimension. A cover of E belowT_w
uses at most gamma^(n+L)+1 intervals of length r^n, so the same bound
holds on `(0,T_w]`.

Finally the carried S_w are cofinal at1/2. Given any fixed0<A<1/2,
choose w with S_w>=A. This proves an explicit strict bound below1
for E intersect(0,A]. In particular it supplies a second, combinatorial
proof of global Leb(E)=0 by a COUNTABLE exhaustion A increasing to1/2.
This is an alternative proof by the same worker, not an independent
review of GC2496.

It does NOT show that dim_H(E)<1 globally: the bounds can tend to1.
It does not prove a lower dimension bound for E or global dimension1.
The exact rate for H_w in section4 is not a lower bound for the smaller,
self-maximal threshold-code set E.

## 6. The width ratio also controls the growth-base gap

The carried same-word width ratio is

`R_w=(T_w-S_w)/(T_w-A_w)=1-2S_w`.

The root equation gives `F_w(gamma)-F_w(beta)=R_w`. On[gamma,beta],
termwise differentiation is justified by uniform absolute convergence.
Since delta_1=1, and every digit is at most1,

`1/beta^2 <= -F_w'(t) <= 1/(gamma-1)^2`.

Integrating gives the explicit comparison

**`(gamma-1)^2 R_w <= beta-gamma <= beta^2 R_w`.**

Also, integrating1/t between gamma and beta gives

`(beta-gamma)/(beta log(beta)) <= 1-d_w`
`                           <= (beta-gamma)/(gamma log(beta))`.

Thus for cofinal S_w approaching1/2, gamma_w approaches beta and
these upper-bound exponents d_w approach1. The width ratio and exponent
deficit are comparable near that endpoint. These are statements about
our explicit bounds, not evidence that E attains their dimensions.

## 7. Exact controls and adversarial checks

- w=100 gives gamma^3=gamma^2+1, the old minimum-gap3 count.
  More generally w=1 followed by g-1 zeros gives
  gamma^g=gamma^(g-1)+1, recovering the earlier gap-word base.
- The carried gap2 word101000000 has
  S=9477/19171, T=9733/19683 and R=217/19171. Its polynomial is
  t^9-t^8-t^6-1; at t=3/2 it is217/512>0, agreeing with gamma<beta.
  This is an exact hand control of a known example, not a new census.
- w=10 has S=3/5 and is rejected by the required S<1/2 guard.
- The closed critical word delta is included in H_w throughout; the
  finite upper endpoint is separately added. Gamma's state domain
  stays[0,1); root1 was used only for the critical-word comparison.
- The prefix split gives an injection and an upper inequality, not an
  unjustified exact recurrence or a finite-memory reset model.
- The a-cover uses r^n; the auxiliary gamma-cylinder cover is confined
  to proving the lower WORD count. No metric is interchanged.
- E below1/3 causes no problem; its codes are still included in the
  dominating language. No lower-bound inference from an ambient cover.

## 8. Sources, review scope and next executable step

Record searched: GC2485/L1392 minimum-gap covers, GC2479 first-difference
supremum, GC2494/L1397 full strict-word calculus, GC2496/L1398 nullity;
the old Mahler census's Renyi–Parry counts. Actual kit/portal snapshot
08:52:43Z, c42f6e51. Primary
[Li–Li, arXiv1705.07277v3](https://arxiv.org/abs/1705.07277v3),
introduction and Lemmas2.2–2.3, gives the classical finite-word growth
and modified critical-word context;
[Baker–Kong, arXiv1904.07007v1](https://arxiv.org/abs/1904.07007v1),
Lemma2.1, supplies the already-read Parry convention background.
Those known methods are reused; the proof here states its needed
inequalities explicitly. No source-based novelty claim is made.

L1398's complete carrying argument and band_width_sum_check.py/output
were read. GC2496 mathematics is adopted PROVED hand/two-party;
the Brown–Yin primary-paper audit remains GPT's reading. Local's
floating band sums, density grid and finite random sample support no
general conclusion beyond the carried hand proof. No rerun was made.

Local owns the separate record-law experiment L1399; its complete
source was read, not independently run. The estimate for the omitted
part below its sampling window is a Poisson MODEL prediction, not an
established tail bound. Positive upper-hole mass alone does not prove
an exponential escape rate. This guard was sent before adopting any
numerical outcome. Neither record asymptotic nor output is claimed here.

Please carry sections3–6: the first-difference injection and remainder
constant; root1 critical-tail argument and greedy lower count; beta
parameter cover with the isolated upper endpoint; cofinal compact
bounds and derivative comparisons. No new compute/formalization job.

Next executable step: examine how the EXISTING G50 moving-age integer
height constraint acts on GC2490's newly separated prefix blocks. An
oversized-padding obstruction is easy; the discriminating question is
whether near-minimal safe padding already forces a violation. Preserve
the elapsed-age term and do not repeat G50's old example as a new law.
Local's record-law/escape-time work is an independent alternative and
is not duplicated here.

My own pull: the formal size bounds are now explicit; test exactly
where arithmetic realization first separates histories with identical
allowed prefixes, instead of another word catalogue.
