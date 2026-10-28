# GC1998: reconstructing the real centre from the white-right past

Owner asks whether Local's reconstruction has overlooked prize implications. Read L1046–L1053, complete root-pasts report, wedge/readout and diagonal/past generators, Rule60 comparison, root-past counter and front detector. Main focus is the reconstruction claim; growth/front/source statistics are not independently rerun or adopted as asymptotic statements. No new numerical experiment. Record search: record_find.py 'Cantor diagonal|white.right past|antiperiod.{0,50}diagonal',15 paragraphs/9 files; actual8.27 and catalogue map consulted. No novelty or submission claim.

## 1. The reconstruction carries

Write U(t,x) for the unique white-right bi-infinite extension of the seed's future. For d>=0 define D_d(t)=U(t,t-d). The known right-diagonal recurrence is

    D_d(t+1)=D_d(t) XOR (D_(d-1)(t) OR D_(d-2)(t)),

with D_d=0 for d<0. Its purely periodic forward sequences extend uniquely to all integer times. Induction on d makes that extension satisfy the same recurrence everywhere, and it agrees with the white-right past by uniqueness. This carries L1051's identity as a consequence of the established8.27 diagonal theorem.

For the real centre c(n)=U(n,0), put P=2^m and R_P(n)=U(n-P,-P). The latter location is on diagonal n, hence

    R_P(n)=D_n(n-P),   c(n)=D_n(n).

If the least period p_n divides P, equality follows. Every fixed finite set of diagonals has a common dyadic period, so R_(2^m)(n) eventually equals c(n) for every fixed n. This is a genuine exact reconstruction/pointwise limit. It is not assuming a periodic centre. The spatial coordinate and time shift both move with P; these are not the ordinary right diagonals themselves or a proof that the vertical readout columns are periodic.

The source computes the correct inverse recurrence from right to left, using only already-known right cells. Its finite left cutoff does not pollute cells to its right. The forward integer implementation uses the correct orientation. The measured finite comparisons are reported; raw outputs were not retained in the supplied commit and have not been independently rerun here.

## 2. Stronger hand consequence: the first failure is an exact complement

Let B(P) be the first d whose least diagonal period p_d does not divide P. It exists by the known lower bound p_d>ceil(d/2). Every d<B(P) satisfies R_P(d)=c(d).

At d=B(P), both input diagonals d-1,d-2 have periods dividing P. Therefore the forcing sequence

    Q(t)=D_(d-1)(t) OR D_(d-2)(t)

is P-periodic. Summing the XOR recurrence over P consecutive ticks yields

    D_d(t+P) XOR D_d(t) = XOR over one complete period of Q.

This parity is independent of t. If it were0, P would be a period of D_d, contrary to the choice of d. It is therefore1. In particular,

    R_P(B(P)) = 1 XOR c(B(P)).

Thus the first mismatch is exactly B(P), and is forced by a parity obstruction. This is a hand consequence of the known recurrence, not just a measured coincidence. It holds on the whole extension U; if B(P)>=P, the mismatch lies at time0 or later, beyond the purely-past segment sampled in the script. For every fixed n, sufficiently large P places the recovered prefix wholly before time0.

This names a useful mathematical object: the frontier where the common return period fails. It does not identify the centre bits at later indices or prove their nonperiodicity. In particular, a known matching prefix cannot bootstrap the new unmatched bits without further equations.

## 3. An essential countercontrol already present in Local's work

The same reconstruction structure exists for Rule60, Local's Sierpinski twin. Its update is left XOR centre. From a single seed at0 the entire negative side stays white, so the centre remains1 forever. Yet its right diagonals are

    D_d(t)=binomial(t,d) mod2,

with unbounded dyadic periods. They have the same unique white-right backward extension and the same reconstruction identity. In this case B(2^m)=2^m: the readout gives a growing prefix of the constant centre and then a forced mismatch.

Consequently unbounded diagonal periods, a growing exact reconstructed prefix, and even the forced first mismatch are compatible with a periodic centre in this related rule. They cannot alone prove Prize1. The part that must do additional work for Rule30 is its nonlinear OR coupling and the phases/correlations it forces across successive diagonal indices. This is a cheap hand discriminator, not a proposal for another simulation.

## 4. Two limits in Local's interpretation need correction

**All finite seeds versus this one seed.** L1046's surjectivity/truncation argument establishes

    for every w,j there exists a finite initial row X realizing w at age j.

It does not establish recurrence, normality, or absence of start-only factors within the one fixed seed S named by the prize. The quantifier X depends on w and j. The reported4096 short words in a finite prefix of S's column are useful finite observations only. The statement that the beginning therefore cannot be remembered locally in S's centre is too broad. Full-state merging fixes a common future, but changing representation can still expose a proof about that future.

**Measured cost versus proven cost.** The n-bit readout requires a P divisible by every p_d for d<n (and usually P>n to stay in the past). The rigorous general estimates here give a finite dyadic choice with P<=2^(n-1), and the period lower bound gives P>(n-1)/2 once n>=2. They do not establish an exponential lower bound. The estimate P about2^(n/3) reflects measured period growth; it must not be advertised as an all-n cost theorem. The literal source constructs P inverse rows of width on the order of P and is not a demonstrated shortcut. A new algorithm could in principle exploit a symbolic representation, but its full work, memory and preprocessing must be counted.

Likewise, depth260 counts do not prove polynomial growth or a2log(d) information theorem; the exact finite counts and any empirical fits remain separate. The detected crystal front is a correlation boundary, not a superluminal information signal, and its rate is a measurement. These side observations are not premises of the reconstruction proof.

## 5. How this could bear on the prizes

Prize1 concerns eventual nonperiodicity of the single-seed centre; Prize2 its limiting colour balance; Prize3 the effort needed to compute its nth bit (official rule30prize.org checked this turn). Reconstruction supplies a valid alternate representation, not a result for any of those targets yet.

There are concrete mathematical opportunities, not just an injunction to 'look harder':

- Derive a relation BETWEEN successive dyadic readouts that determines or constrains the newly exposed suffix, rather than only reproducing their already shared prefix. A period-p contradiction would need a forced mismatch c(n+p)!=c(n) at unbounded n, for each candidate p, using Rule30-specific coupling.
- Examine whether the parity that moves B(P) also controls the newly exposed centre bits. At present it determines mismatch with an approximating column, not mismatch between two positions of c itself. The Rule60 control explains exactly why this distinction matters.
- For computation, ask whether the required wedge entry can be evaluated symbolically from n without constructing the huge inverse wedge. The current identity neither supplies such a method nor rules one out.

The most focused next hand question is: what additional relation does the OR term impose across the moving readout frontier that the Rule60 control lacks? Naming that relation is the missing bridge to a prize statement. A bare coordinate translation of c(n+p)!=c(n) would merely restate the target; it must produce an independently provable constraint.

Verdict: the owner's pull is worth pursuing. L1051/L1053 are sound exact consequences of known diagonal structure, and the exact-complement frontier gives a clearer handle. 'The future was fixed anyway' is not a mathematical reason to dismiss a representation. Equally, the Rule60 control prevents promoting reconstruction itself into a nonperiodicity argument. No computation, schedule restart, prize candidate or submission is launched by this review.
