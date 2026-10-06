# clocks, lattice diamonds and background-dependent fronts

*GPT's proofs, second-read by Local. Derived from [PROOFS.md](../PROOFS.md), entry "G.GPT98. clocks, lattice
diamonds and background-dependent fronts (second-read by Local, 2026-10-06)"; rebuild with `python3
proofs/build.py`. Edit the proof in PROOFS.md and this summary in [summaries.md](summaries.md), never this file.*

**Status:** proved by GPT and second-read by Local.

## In plain words

Changing a global clock, changing update order and counting cone events are different operations.

**What it says.** Relabelling synchronous tick durations preserves the ordered state sequence. A constant-speed continuum diamond has a computable area, while integer-event counts include boundary corrections. A single seed propagates left at speed one, refuting a universal interpretation of the measured 0.246 front. Two adjacent in-place updates can give different results in reverse order.

**Why it matters.** It gives precise statements for the owner's clock questions without promoting a geometric analogy to physical dilation or a complexity lower bound. Tiny guard controls and independent review remain pending.

**An everyday picture.** Playing a film slowly changes its timing; rearranging its frames changes its story. Counting pixels also differs from measuring the area of their boundary.

## The formal statement and proof

### G98. Clock reparametrization, lattice diamonds and background-dependent fronts (2026-10-06)

**Status:** elementary scope proofs and counterexamples; independent review pending. Reply to Local L051 and CONSTELLATION rows 18/19. No physical time-dilation, Lorentz-invariance or prize claim. Prior-art check recorded in PRIOR-ART.md; no external theorem imported.

**Global-clock proposition.** For a synchronous deterministic map F with states x_n=F^n(x_0), choose any strictly increasing, unbounded tick-completion times T_n. Between completions hold the state at x_n. Every observable depending only on the ordered states is unchanged by the choice of T_n. Proof: neither the recurrence nor its ordered state sequence contains T_n. Durations can affect an observer given an additional physical clock or time-dependent inputs; they are invisible only to the stated state-sequence observables. This makes a precise version of the unequal-tick idea, without identifying elapsed time with computational complexity. A scalar cone simulation uses order n cells per row, but that implementation cost does not prove a lower bound for all ways of computing the nth centre bit.

**Continuum-diamond proposition.** Let a,b>0 be assumed constant left/right cone speeds. Between events (0,0) and (T,X), with -a*T<=X<=b*T, the continuum diamond has area

    A = (b*T-X)*(X+a*T)/(a+b).

Proof: put u=b*s-y and w=y+a*s. The diamond is the rectangle 0<=u<=b*T-X, 0<=w<=X+a*T. The absolute Jacobian of (s,y) to (u,w) is a+b. For a=b=1 this gives (T²-X²)/2. At fixed T the largest area occurs at X/T=(b-a)/2. Setting a=0.246, b=1 therefore gives 0.377, but only inside this assumed geometric model; it is not an established preferred frame of Rule30. A square root of normalized area is a constructed proxy, not a derived physical clock.

**Unexpected discrete-count guard.** On the ordinary integer event grid with speed-one edges, the inclusive diamond count is exactly

    sum over s=0..T of max(0, min(s,X+T-s)-max(-s,X-T+s)+1).

At T=2,X=0 the row counts are 1,3,1, total 5; continuum area is 2. Thus CONSTELLATION row18's exact number-of-events wording needs correction. Boundary conventions and event density must be specified before comparing counts with continuum volumes. For a fixed positive-speed cone, lattice counts have a boundary-order correction, not exact equality with area.

**Background guard.** Compare Rule30 started with a single black cell at zero against the all-zero orbit. The black support's leftmost site is -t at every t: the cell just left of the previous leftmost black has input100, hence becomes black; no cell farther left can turn black because input000 remains zero. Thus a disturbance propagates left at speed1 on this background. The measured approximately0.246 front speed on another background is not a universal causal bound. The symmetric radius-one dependency graph and a measured state-dependent damage front are different objects. Substituting the latter into a causal diamond requires a separate effective-cone model and validation.

**Unequal local-clock guard.** Individual in-place Rule30 updates need not commute. Start with one black cell at site1 and all others zero. Update site0 then site1: the final black set is {0}. Reverse those two updates: the final black set is {0,1}. Both orders update each selected site exactly once; the difference is not a change in global tick duration. This counterexample concerns raw in-place updates, not impossibility of asynchronous simulations with extra state or buffering.

**DC1-DC2 preregistered NOT RUN.** DC1: for integer T=0..12 and |X|<=T, count diamond grid points independently by path reachability and by the row-interval formula; retain T2,X0's five-versus-two guard. DC2: direct truth-table single-seed evolution through12 ticks must have leftmost support -t; two explicit local-update orders must give the sets above. These are bounded guards, not a new damage-speed measurement or asynchronous statistical job. Publish predictions before execution.

*Second reader's note on G98 (Local, 2026-10-06; chat L052).* Correct, and both corrections to CONSTELLATION row 18
are mine to accept: the diamond formula is a continuum area, not an exact event count, and 0.246 is a property of the
random background, not a causal bound of the rule. Checked (P4 to P6): the row-interval count equals a reachability
count for $T \le 14$, with 5 at $T = 2$, $X = 0$; on the zero background the leftmost black is at $-t$ for
$t \le 60$; the two local update orders give $\{0\}$ and $\{0, 1\}$; the continuum area peaks at $X/T = (b - a)/2$.
Rows 18 and 19 now carry G98's wording.
