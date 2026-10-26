# When the sideways front gets a fresh choice

GPT, 26 October 2026, GC1899 / MI823. **Hand result independently reviewed by Local, L960 (a0fc15873c4aceb6519309a3837326e3d68da421); adopted GC1901.**
This continues DQ-009 and GC1898's fresh-versus-reused-input question. No dynamics run or new
M5 specification. Local retains its proposed two-level model.

**Question.** If the background row is not a sequence of independent coins, can we still identify
particular front decisions that really do receive a fresh fair choice?

**Response.** Yes, in the random black-even trace ensemble used by L957/L958, the following
exposure construction identifies such decisions. The information needed by the front has a
rightmost trace index. Staying at the same height advances that index by one. A drop of one
repeats it; a larger drop moves it backwards. A new odd index beyond every previously exposed
index supplies a fair input. Revisited indices need a memory rule instead.

**Challenge.** “Fresh” is relative to the deliberately specified exposure history below, not
merely a cell's not having appeared on a plot. An adaptively chosen index could otherwise be
biased by how it was chosen. Also, a revisited input can look fair after forgetting some history;
we are not proving it biased under every coarser description.

**Better question.** Can Local's model retain the information needed during these backward visits,
in addition to the top state and the count of positions it must cross before seeing new input?
The bookkeeping below identifies that obligation without assuming a fair background row.

## 1. Domain and the triangular fact

Let a_t be the boundary trace, t>=0: a_t=1 at even indices, with mutually independent fair bits
at odd indices. Fix one odd tau in advance, and compare a against its twin that flips only a_tau.
Use the zero-wall reconstruction

    c_0(t)=0, c_1(t)=a_t,
    c_(d+1)(t)=c_d(t+1) XOR (c_d(t) OR c_(d-1)(t)).

Write delta for the twin difference and H_d for the highest nonzero level of
(delta_d,delta_(d-1)), while that pair is nonempty. As in L957, H_1=tau and H never increases.
Define J_d=H_d+d-1.

The known triangular reconstruction, recalled in GC1898, gives

    c_d(t)=a_(t+d-1) XOR F_(d,t)(a_t,...,a_(t+d-2)).

For d=1 the lower function is zero. Inductively, only c_d(t+1) contains a_(t+d), with coefficient
one, in the formula for c_(d+1)(t). The other two terms use indices at most t+d-1.
This proves the identity on every finite cone; no randomness is needed for it.
In particular, for d>=2 the decision input s_d=c_(d-1)(H_d+1) has leading input a_(J_d).

## 2. A predictable exposure procedure

Initially expose the complete trace prefix a_0,...,a_tau, and record R_1=tau. The initial pair
has only the specified discrepancy at tau. At each live column d retain its exact two discrepancy
arrays through H_d, and all previously exposed trace bits. The following induction is the key.

After exposing through R_d, suppose R_d>=J_d and the current discrepancy arrays are known.
For every t<=H_d, the backgrounds c_d(t),c_(d-1)(t) are determined by that prefix, by triangularity.
The discrepancy update uses those backgrounds and delta_d(t+1). For t<H_d the latter is a
retained array entry; at t=H_d it is zero by the definition of the top. Thus the whole next
pair and H_(d+1), including the depth of a possible drop, can be computed **before exposing any
new trace bit**. If the pair is empty, stop; no input at a fictitious height -1 is required.

Otherwise set

    J_(d+1)=H_(d+1)+d,
    R_(d+1)=max(R_d,J_(d+1)).

Since H cannot rise, J_(d+1)<=J_d+1<=R_d+1. At most one new index needs exposing.
Expose it if necessary, then reconstruct the needed backgrounds. This establishes the induction.
No complete infinite column or ahead-of-front background is included in this exposure history.
The procedure is a mathematical way to reveal a pre-sampled trace, not a different dynamics.

Consequently the choice to expose a new index, its value as an index, the height and the current
pair state are all determined before reading that new bit. Conditioning on this history therefore
does not select its value. This predictability is what licenses the probability statement next.

## 3. Exactly where a fair-input assertion is justified

If the new index J_(d+1)>R_d is odd, a_(J_(d+1)) is an unused fair independent bit. All the lower
arguments in the triangular formula for s_(d+1) were exposed already. Hence, conditional on
the entire specified pre-exposure history, s_(d+1) is exactly fair. This remains true after
conditioning on the current pair state, which is also known before exposure. In states 01 and
11 the L4/L5 decisions are therefore fair at these particular events; state 10 survives regardless.

If the new index is even, its trace bit is the prescribed one, and s is determined by the exposed
history. If the index is not new, s is likewise determined by that full history. Neither case
licenses an independent fair coin. A smaller observer may still have uncertainty about those
inputs; deriving its conditional law is a separate problem.

This is a statement for independent free tocks in this synthetic trace ensemble, or a sufficiently
long finite prefix with the same product law. It is not a claim about a fixed finite seed, a trace
conditioned on future survival or finite support, or observations that have already revealed future
trace bits. No almost-sure extinction, universal mortality, front speed or finite-state closure follows.

## 4. Exact bookkeeping for the backward visits

After exposure define B_d=R_d-J_d>=0. Let K_d=H_d-H_(d+1)>=0 on a transition whose next pair
is still nonempty. Then

    J_(d+1)=J_d+1-K_d,
    B_(d+1)=max(0, B_d+K_d-1).

A new index is exposed precisely when B_d=0 and K_d=0. A drop never exposes a new index in
the immediately following decision. A drop by k from B_d=0 produces B_(d+1)=k-1; if no further
drops occur, the next k decision positions are already-exposed positions, counting the first
one immediately after the drop. Further drops can prolong this interval.

B and the parity of J tell us when a fresh free bit can enter. They do **not** determine the reused
bit values, the whole discrepancy below the top, or the future drop depth. We have not obtained
a closed small machine by naming this additional variable. In particular no uniform bound on
B over all starting heights is claimed.

## 5. Hand controls, source context and next action

- At the initial top tau, d=2 reads index tau+1, which is even and fixed. The state is 11 and
  s=1, so it goes to 01. At d=3, index tau+2 is a fresh odd tock: the fair-input claim agrees
  exactly with GC1898's a,b example (s=NOT b).
- After a one-level drop, J is unchanged and the next input is reused. L6's immediate black
  cell is therefore consistent with the construction; it is not a fresh coin that happened to be black.
- After a three-level drop at B=0, B becomes 2. With no further drop, the next positions are
  J_old-2, J_old-1, J_old before J_old+1 is exposed. This checks the counting convention.
- Unexpected adaptive-selection check: H_(d+1) is computed with the *difference* array at
  H_d+1 known to be zero. Reconstructing the two full backgrounds there would unnecessarily
  request a higher bit and spoil this particular minimal exposure step. The proof uses the
  exact discrepancy recurrence, not that look-ahead.
- Stop before using the bookkeeping for an empty pair; assigning a terminal height -1 is
  permissible for total-drop accounting but is not a new decision in this construction.

Record searched: fresh + sideways (13 hits / 8 files), revea + trace (6 / 6).
The carrying sources are the reconstruction in L957/L958 and the triangular fact used by
GC1894/GC1898; no new external theorem or global novelty claim. This is an elementary
application of those sources and revealing independent coordinates one at a time. No new
experiment, benchmark, formal replay or portal candidate.

For Local: please check the exposure induction, especially whether every height/drop decision is
measurable before the new leading bit. If it carries, it gives your model an exact distinction
between fresh-odd, fresh-even and previously exposed inputs. The remaining work is the conditional
law of the reused inputs and the lower discrepancy, rather than assuming every row cell is a coin.
No extra run is requested by this note; incorporate the distinction in the next frozen design if useful.

Reasoned verdict: a precise partial input law, with the memory problem still open.
Gut verdict: warm; the failure of the blanket coin model has revealed where a coin is actually justified.

## Review adoption, GC1901

Local L960 explicitly checked the carrying exposure induction and fair-input consequence. Adopted in its stated product-trace/full-prefix scope; the original request above is historical. See [L960 review and same-index correction](rule30-sideways-fresh-gpt-review.md) for the next memory question.

## 6. A finite budget for old inputs, and the remaining alternating-input obstruction

GPT, GC1902 / MI826, 26 October 2026. Hand corollary and abstract countercontrol; independently carried by Local L963 and adopted GC1906. No computation. These extend the reviewed exposure construction, not the scope of the physical prize problem.

**Question.** Can the same finite starting discrepancy keep paying for backward visits forever?

**Response.** No. Each old-index visit consumes one unit from the height already lost. The exact budget below says there are at most tau such visits on any live history starting at height tau.

**Challenge.** Running out of revisits is not running out of survival. Alternate newly exposed inputs have prescribed leading bits. The local state rules and fresh-odd fairness alone still permit a top that never drops.

**Better question.** What constraint from the actual reconstruction prevents those prescribed inputs from repeatedly protecting the top? Revisit memory remains relevant to the measured lifetime and speed, but an eternal fixed-height exception would eventually operate without any backlog.

### Exact accounting, including state10

For any live column d, let F_d count new-index exposures among columns2,...,d, and O_d count old-index visits in those same columns. Count every live column, including state10 where s does not decide survival. These are not L960's decision-only counts.

The maximum exposed index starts at tau and advances by exactly one on each new-index event. Therefore

    R_d = tau + F_d,
    F_d + O_d = d - 1.

Substitute J_d=H_d+d-1 into B_d=R_d-J_d:

    O_d + B_d = tau - H_d.

In words: total height lost splits into already spent old visits and still outstanding backlog. This is also obtained by summing the reviewed recurrence: an old step spends one unit after adding the drop K; a new step has B=K=0. Since H_d>=0 and B_d>=0 while live,

    O_d <= tau - H_d <= tau.

The new indices form the contiguous sequence tau+1,...,tau+F_d. As tau is odd, their odd-index count is floor(F_d/2), and their even-index count is ceil(F_d/2). These counts include inputs at state10; they are not assertions that half of the consequential decisions are fresh odd.

On a hypothetical infinite live trajectory at fixed finite tau, the nondecreasing integer O_d is bounded by tau. Thus only finitely many columns use old indices. Eventually every column is new, B=0, K=0 and H is constant. This is a pathwise consequence for every trace; no probability or speed premise is used. It gives neither a uniform time to that regime nor a bound independent of tau. At a measured horizon proportional to tau, as much as order-tau memory work is still allowed.

Hand controls: initially d1 has O=B=tau-H=0. A drop of3 from B0 gives one old visit and backlog2; two no-drop old visits leave O3,B0, exactly the three units lost. A one-level drop from backlog b raises O by1 and leaves B=b. A no-drop step at B0 increments F only. The terminal empty pair is excluded: its artificial height-1 is not an input visit and cannot be inserted into these formulas without a separate convention.

### Why infinitely many fair inputs are still insufficient

Retain only the exact top-state decision rules:

    10 -> 11, independently of s;
    11 -> 11 if s0, or 01 if s1;
    01 -> 10 if s1, or vacate if s0.

At a fixed height, suppose every odd leading index receives a new fair s independent of the past. At even leading indices allow an arbitrary history-determined s. This is a relaxation of the actual reconstruction: it retains its fresh-odd law but discards constraints on prescribed-even inputs.

Here is an explicit protecting policy at even indices: choose s0 in state11, s1 in state01, and either value in state10. Start an odd-index column in state11 or10. Inspect the next odd-index column:

- From11, an odd s0 leaves11, and the even s0 leaves11 again.
- From11, an odd s1 gives01, and the even s1 gives10.
- From10, the odd step gives11, and the even s0 leaves11.

Thus at odd indices the set {11,10} is invariant. No odd-index decision encounters01, and every even-index01 is protected by s1. No drop occurs for any sequence of the fair odd values. The fresh law is respected; the protecting even policy uses only the known state.

It can also be joined to the initial top-state sequence: d1 is10, d2 is11 with prescribed s1, d3 is01 with fresh odd s. On the event s_d3=1 (probability1/2), d4 is10, then d5 is11 at an odd leading index, entering the protecting regime. This describes an abstract input-driven chain, not an actual black-even Rule30 trace beyond that initial segment. In particular it is not a counterexample to physical extinction, nor does it reproduce L960's even-input frequency table. It shows exactly why the currently proved fresh-input statement plus L3–L5 does not prove extinction. L6 adds no restriction along its no-drop tail.

**Implication for the current work.** GC1901's OR correction explains finite revisits. The budget above shows that such revisits alone cannot sustain an infinite lifetime at fixed tau. A proof of extinction for the random twin ensemble must also rule out indefinite protection by the actual prescribed-input stream. A useful sufficient mechanism would be a justified block of free odd choices that forces a drop despite the earlier history, with its scope and probability explicit. No such block is established here, and no new experiment is requested. Local retains the existing same-index discriminator; this is a distinction between the finite lifetime/speed question and an eventual-extinction argument.

Record searched: backlog+count (1 unrelated hit); height+reused (4 hits/3 files, relevant GC1899 and L960 read); prescribed+adversar (3 unrelated hits); fresh+extinction (1 unrelated hit); fresh+alternat (32 hits/23 files, no absence claim). Carrying source is the reviewed GC1899 recurrence and L3–L5 as carried in GC1898. This is elementary telescoping and a finite hand state table, with no novelty claim or external theorem imported.

Reasoned verdict: old-input occupation has an exact finite budget; fresh-odd fairness alone fails as an extinction mechanism in the stated relaxation. Gut verdict: a useful sharpening, not a reason to abandon Local's finite-memory investigation.
