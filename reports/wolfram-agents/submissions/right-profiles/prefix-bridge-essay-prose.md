**HELD GC2127: no new contribution upload or PR extension. Earlier public prefix-clock source covers the finite-seed application; retain this prose as history. See ../../PREFIX-PRIOR-ART-REVIEW.md.**

# A guarded restriction on Rule 30's prefix-period doublings

Draft explanation, GPT, 29 October 2026, for the established joint byline. Hand argument carried by Local
L1142; source compiles4.35 (L1144), actual outputs reviewed GC2125; full enforcement packet pending. This file is prose only, not an executed computational
essay, source assembly, approved portal upload or new-result priority claim. The accepted historical essay
and public 7d47a9 artifacts are preserved.

## What repeats: a diagonal or the entire prefix?

Read Rule 30 along diagonals moving right at one cell per time step. For an arbitrary initial row x, write
D_i(t)=evol(x,t,t-i). Substitution into the rule gives

    D_i(t+1)=D_i(t) XOR (D_(i-1)(t) OR D_(i-2)(t)).

Each diagonal integrates the OR of its two predecessors. A familiar lifting criterion determines whether
an integrator repeats or complements after one period of its forcing. That is known background, formalized
in the kit's triangular-function and single-seed period machinery.

The small distinction here matters: the period of one diagonal can be different from the common period
of every diagonal seen so far. We use the latter. PrefixPer(n,p) says that every D_0,...,D_n repeats after
p at every time from zero. LeastPrefix(n,p) says p is the smallest positive such common period. We never
assume that the individual diagonal periods are nondecreasing. We also do not assume an arbitrary infinite
initial world has periodic diagonals at all.

## The bridge from a new prefix period to a complementary diagonal

Suppose n>=2, p>0, the older prefix through n-1 has period p, and the prefix through n has LEAST period2p.
The forcing of D_n is p-periodic. The already known running-shift identity therefore says

    D_n(t+p)=D_n(t) XOR kappa,

where kappa is one bit, the forcing parity over p ticks, independent of the starting time t.
If kappa were zero, the old prefix and D_n would all repeat after p. That would contradict minimality of
2p for the new prefix. Hence kappa=1: the new diagonal complements after p.

Only the new prefix's least period is used. The old prefix need only have period p. A separate assertion
about the new diagonal's own minimum, or a general monotonicity theorem, is unnecessary.

## The exact guarded exclusion

Let k>=2, p>0 and p divisible by4. Assume:

| Prefix through diagonal | Period hypothesis |
|---|---|
| k-1 | has common period p |
| k | has least common period2p |
| k+1 | has least common period4p |
| k+2 | has common period4p |
| k+3 | has least common period8p |

Then the prefix through k+4 has common period8p. In particular its least period cannot be16p.
The plateau through k+2 need not be minimal. For a finite seed in its standard right-edge coordinates,
whose prefix periods have the established pure-dyadic form, this is the forbidden doubling word11011
when the period immediately before its first letter is divisible by4. Letters record changes of the
PREFIX period, not the colors in one temporal word.

The actual Rule30 statement takes x:Integer->Bool and uses these hypotheses on its actual evol diagonals.
It imposes no finiteness on x. Its price for that broader scope is explicit periodic-prefix hypotheses:
it does not claim that all arbitrary worlds meet them, construct the prefix periods, or realize an
arbitrarily chosen sequence of doubling letters.

## Why the next doubling fails

Put q=2p, d=D_k, a=D_(k+1), b=D_(k+2), c=D_(k+3), z=D_(k+4).
The minimality bridge applies at k,k+1,k+3. It gives d complementing at p, a complementing at2p and c
complementing at4p. The prefix periods also give d period2p and b period4p. These are exactly the
hypotheses of the already delivered right-profile shift law:

    z(t+4q)=z(t) XOR eta(q,d),
    eta(q,d)=parity(q/2) XOR XOR_{u<q/2} d(2u).

Pairing the even samples of d at distance q/2 gives

    eta(q,d)=parity(q/2) XOR parity(q/4).

Here q is divisible by8, so both terms are zero. Thus z repeats after8p. Every earlier diagonal already
repeats after8p, so the entire enlarged prefix closes. This uses the delivered all-time shift law, not
just a count starting at t=0.

## The exception is part of the result

At p=2, q=4, the same eta formula is ONE rather than zero. The single seed's already recorded prefix
periods Q_2,...,Q_7=(2,4,8,8,16,32) exhibit the otherwise forbidden11011. This is why the condition p%4=0
cannot be relaxed to p even. A compiler mutation that weakens that guard is a diagnostic control; its
rejection is kept separate from the actual proof and from any computational illustration.

The proof gives a short local restriction on an ordered sequence of period-growth events. It gives no
asymptotic rate equality, lower bound on the time between events, uniform plateau length, or conclusion
about the infinite center column. The existing stronger half-rate upper bound is not improved by our
older three-fifths counting corollary, which is not a headline here.

## Relation to existing work and validation still required

The generic forcing-parity mechanism is known: TFunctionCycles.lift_iff/per (Klimov–Shamir lifting) and
Rule30RightPeriods.antiperiod/e_step. The explicit101 shift and eta formulas are already our public
7d47a9 contribution. The guarded11011 hand result is recorded GC2007/L1063/GC2010. This draft supplies
its precise whole-prefix bridge and actual-world statement; it is not a second discovery of that result
or a new cycle-lifting principle. Kit per at n bits corresponds to a prefix through index n-1.

Current comparison sources: [the existing 7d47a9 contribution](https://www.wolframcloud.com/obj/rule-30-prize/Agents/status/R30-20261029-7d47a9),
[TFunctionCycles](https://github.com/WolframInstitute/Rule30PrizeKit/blob/932cf8dde039b89b1dcbe9636867bb1b2057fef0/equivalents/Rule30Equivalents/TFunctionCycles.lean),
and [RightPeriods](https://github.com/WolframInstitute/Rule30PrizeKit/blob/932cf8dde039b89b1dcbe9636867bb1b2057fef0/lean/Ruliology/CellularAutomata/Rule30RightPeriods.lean).

The final package must retain the exact source and theorem signatures, the actual current-toolchain
receipt and negative control, source-matching axiom reports and checker outcome, and an independently
reviewed native notebook. A numerical illustration or an uncompiled draft is not that validation. Posting
owner and whether this extends the existing package must be agreed with Local before packaging or upload;
there will be no competing portal post or duplicated compiler stage.
