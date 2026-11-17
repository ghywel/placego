# A triangle lineage that reads fresh input at every generation

GPT, 27 October 2026, GC1974 / MI892 / DQ-020. **Complete hand candidate / PROOF-SKETCH;
independent carrying read parked by the owner's full halt (L1025).** No dynamics computation or Lean replay. This addresses the
explicit adaptive-conditioning gap left in GC1933 and L998, under a product initial-row model.
It does not address the fixed single-seed orbit or DQ-023's eternal centre clock.

**Question.** We knew the width law for one child. Does following that child bias the input
that its own child will encounter?

**Response.** For the particular lineage defined below, the hand argument says no. Think of a
sealed strip of coin flips, read from right to left. A child consumes a finite piece of the strip.
When an odd child reaches its tip, the next unread input is still just outside that piece. The
changing tip position and time fit together exactly; there is no jump back into already read input.

**Challenge.** Overlapping space-time cones do not by themselves give independence. We must track
which INITIAL cells have been exposed, and show that the choice of the next one is made before
reading its value. The exact frontier identity in section 4 is the carrying step.

**Better question.** Can we first prove that every prescribed finite width list fixes exactly one
initial left word of the appropriate length? That deterministic coding statement gives the
probability law without assuming that adaptive rows are independent.

## 1. Precisely which lineage and which probability space

Use full-line Rule 30, with black = 1:

    X_(t+1)(i) = X_t(i-1) XOR (X_t(i) OR X_t(i+1)).

Fix an arbitrary initial right half X_0(i), i >= -1, with values 1,0,1 at -1,0,1.
The initial cells i <= -2 are mutually independent fair bits. Start at the specified isolated
white singleton (c,t) = (0,0). Fixing the entire right half is convenient: every remaining
right-side argument is then known. The conclusion holds for every such fixed right half.

At an isolated singleton (c,t), inspect its maximal black run on the left. Its length M is at
least 1; an infinite black run is a possible deterministic exception, handled probabilistically
below. For a finite length m, the reviewed singleton-child lemma gives a white run of width m
on [c-m+1,c] at time t+1, with black flanks.

Follow only this run's **shrinking core**. If m = 2r+1, its next singleton is

    c' = c-r,       t' = t+r+1.

If m is even, stop when the final white pair becomes black. This is a specified chain of cores
and singleton-hung children. It is not a claim about all white connected components, every
geometrical notion of ancestry, or other triangles nearby.

## 2. The candidate conclusions

At every reached tip, conditional on the entire exploration history specified below,

    P(M=m | history) = 2^(-m),       m >= 1.

More exactly, for positive m_1,...,m_n with m_1,...,m_(n-1) odd, the event that these are the
successive child widths has probability

    2^(-(m_1+...+m_n)).

Widths are sampled only while the chain is alive; this is the law of independent geometric
draws stopped at the first even one, not a claim that a survivor-conditioned width is geometric.
In particular, if N is the number of odd-width links before the terminal even child,

    P(N >= n) = (2/3)^n,       P(N=n) = (1/3)(2/3)^n,       n >= 0.

Thus this canonical lineage terminates almost surely. It has mean 2 odd links, or 3 children
including the final even child. These statements are for the specified fair-left model.

## 3. The leftmost initial cell enters by XOR

For every fixed t and i, induction gives a Boolean function H_(t,i) such that

    X_t(i) = X_0(i-t) XOR H_(t,i)(X_0(i-t+1),...,X_0(i+t)).

At t=0 the second term is zero. For the next time, only the left-parent term contains the
new leftmost initial bit i-t-1; the centre and right parents start strictly to its right.
Substitution retains coefficient 1 in XOR. This proves the formula for every finite cone,
with no stochastic hypothesis. It is the standard left-permutivity fact, not a novelty claim.

If all initial cells strictly to the right of i-t are known, specifying X_t(i) therefore fixes
exactly one value of X_0(i-t). With a fresh fair initial bit the output is fair, conditional on
all those known cells. No independence assertion between whole later rows is needed.

## 4. The exposed frontier fits the next tip exactly

Maintain the following invariant at a current tip (c,t): all initial cells with index

    i >= b,       b = c-1-t,

have been exposed; the lower-index cells remain unread independent fair bits. The current
tip and both immediate flanks are determined by this exposed suffix. Initially b=-1, so the
invariant holds by the chosen right half.

The immediate left neighbour c-1 is already known black. Inspect c-2,c-3,... at time t.
For the j-th newly inspected cell c-j-1, j=1,2,..., its leading initial index is b-j.
Every other argument in section 3 has a larger initial index and is already known. The next
inspection therefore reads exactly the next fresh bit. To obtain black-run length m requires
m-1 further black outputs and then one white output: exactly m prescribed fresh outputs.
It has conditional probability 2^(-m), and fixes exactly one initial word on [b-m,b-1].

The stopping frontier after this scan is b_new=b-m. No event in the scan depends on an initial
cell below b_new. In particular, stopping at the first white does not condition those unread
cells. This can be seen directly by partitioning into the disjoint finite stopping words:
on each word, its location and every value read so far are fixed, leaving the lower product
coordinates unchanged. The probability of scanning forever is lim 2^(-k)=0.

Now suppose m=2r+1. The reviewed shrinking-core rule gives the next tip above. Its needed
frontier is

    c'-1-t' = c-r-1-(t+r+1)
             = c-1-t-(2r+1)
             = b-m = b_new.

This identity is the important step. During erosion, the left flank's cone starts at b_new;
every cell in the shrinking core and its right flank has leading index at least b_new.
So producing the next tip requires no initial bit below the suffix already exposed. Its
position, time and flanks are known before the next fresh bit is read. The invariant restarts
without revealing anything extra. This remains true for adaptively obtained finite c and t:
on each finite stopping history they are fixed integers.

Inducting over generations gives the unique-word statement and the joint probability in
section 2. Summing over odd m gives 2/3 at every live generation. The probability of n
successive odd children is consequently (2/3)^n, which tends to zero. All finitely many
children before the first even one have finite widths and finite erosion times; the chain
therefore ends at a finite time almost surely. No uniform deterministic lifetime is inferred.

## 5. Hand objections and controls

- **Width 1.** At t=0, m=1 reads X_0(c-2)=0. The next tip stays at c at time 1; its left
  neighbour is forced black. Its next inspected cell has leading index c-3, a fresh bit.
  Specifically X_1(c-2)=NOT X_0(c-3), so two successive width-1 children prescribe 0,1 in
  the initial left strip. They do not ask twice for the same bit.
- **Width 3.** At t=0 the left word is 0,1,1,1 on [c-4,c-1]. The child has zeros on
  [c-2,c] at time 1 and its next singleton is c-1 at time 2. Its frontier c-4 is exactly
  the old scanned boundary; the next query has leading index c-5. This checks the shift
  in both time and space, rather than extrapolating the width-1 example.
- **Even width.** Width 2 gives a white pair at time t+1, then two black cells. The process
  stops there. Choosing another nearby singleton would define a different observer and
  requires another proof.
- **Unexpected conditioning check.** If the initial tip is selected because its child is
  odd, the next odd-width probability is 1 at that selected event, not 2/3. Such a selection
  has already read beyond the stated frontier. Our proof starts at a fixed tip and does
  not condition on its future survival. Conditioning on previous odd widths is allowed;
  conditioning on the width currently being predicted is not.
- **Deterministic infinite countercontrol.** An alternating left half ending in 101 at
  c-1,c,c+1 can produce width 1 forever, independently of the farther right half. This
  gives an actual exceptional Rule 30 history. Its prescribed infinite left tail has
  probability zero here. Almost sure termination is not universal termination, and this
  model does not include a finite single-seed initial row.
- **L998's original conditioning.** Fix 10001 on [c-2,c+2] with all other initial cells fair.
  At time 1 the singleton at c has frontier c-2. Fixing the whole initial suffix from c-2
  on leaves the lower cells independent fair and gives exactly our invariant. Hence this
  candidate extends that original first-child law along this particular canonical lineage.

## 6. Search, scope and the next carrying read

Record searched: `adaptive.*lineage|lineage.*adaptive|first.generation` returned 16 paragraphs
in 11 files. Read the actual GC1933 review, L998 child-law/independence qualification, GC1971
synopsis and GC1899's predictable-input exposure argument (independently carried L960).
The earlier warning about overlapping cones is correct; section 4 supplies a possible way
through it rather than silently dropping the warning.

Bounded primary-source searches on Rule 30 triangle genealogy, geometric widths and
permutative stopping-line independence found no exact counterpart in the results inspected.
Wolfram's [NKS notes](https://files.wolframcdn.com/pub/www.wolframscience.com/nks/nks-notes.pdf)
already discuss fair-row randomness and exponentially distributed triangle sizes (p. 226 notes).
His [open-problems list](https://www.wolframscience.com/openproblems/NKSOpenProblems.pdf) separately
asks about patches in the single-black-cell pattern. Those are different scopes. This is a
limited search, not a novelty certificate; all probability ingredients used above are elementary.

On an owner restart, the useful independent read is the frontier invariant, the odd-child coordinate identity and the
no-extra-exposure step, including m=1 and m=3. If one fails, retain the precise failure before
designing compute. If they carry, adopt only this stopped canonical-chain law under the stated
product input. No M5 run, formalization, portal submission or review during the halt is requested by this note.

Reasoned verdict: complete hand candidate for the adaptive law in this restricted model.
Gut verdict: warm; this answers our own explicit objection instead of treating it as a permanent wall.

**Halt disposition, GC1975:** this draft was completed before the final fetch revealed L1025's owner halt. Retained unchanged mathematically as an unreviewed candidate; no present Local review or computational task. Reopen only at the owner's restart.
