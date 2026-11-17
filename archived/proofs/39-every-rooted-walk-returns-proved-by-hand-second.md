# Every rooted walk returns (proved by hand, second-read, machine-checked): at every period q, the rooted profile walk reaches a zero child

*Siblings, Jen and the squeeze. Derived from [PROOFS.md](../PROOFS.md), entry "39. Every rooted walk returns (proved
by hand, second-read, machine-checked): at every period q, the rooted profile walk reaches a zero child"; rebuild
with `python3 proofs/build.py`. Edit the proof in PROOFS.md and this summary in [summaries.md](summaries.md), never
this file.*

**Status:** proved by hand by Local (chat L487).

## In plain words

In the walk that builds Rule 30's repeating columns one after another, every walk that starts from a blank column comes back to a blank column, whatever the period.

**What it says.** Each new column is forced by the two before it, and you can also run the rule backwards to recover the earlier column from the later two. A walk that never came back to a blank column would have to loop, and running it backwards from the loop would lead to a column before the start, which cannot exist.

**Why it matters.** It explains a computer census in which every such walk did return, and it is checked line by line by a proof assistant.

**An everyday picture.** A one-way trail through a finite maze where every junction has one way in: if you start at the entrance, you cannot end up circling forever, so you must reach an exit.

## The formal statement and proof

*Status:* proved by hand by Local (chat L487). Second-read by GPT in GC867, which accepted the statement and the proof
structure against the census walk, with "rooted" meaning zero-started; it does not supply G7's physical-root ancestry.
Machine-checked in Lean 4 against Mathlib (tests/probes/lean/RootedReturn.lean, L489; no sorryAx). The compilation is
Local's reported verification; GPT reviewed the source but did not compile it. Filed by Local, 2026-10-09.
*Provenance:* the walk is S84's (G190 .. G198), as censused by RC88, RC16, RW and RWC. GC863 noted that the two-live-
state bound follows from reset uniqueness (G158, G204, R2), and GC864 bounds each first excursion. This entry adds the
termination argument and its formal check.

**Statement.** Fix q >= 1. For q-periodic binary words, call c a child of the pair (x, y) when
c(t + 1) = x(t) XOR (y(t) OR c(t)) for every t modulo q. For every nonzero word c, the walk (0, c) -> (c, c_2) ->
(c_2, c_3) -> ..., taking at each step the unique child of a nonzero driver, reaches a state whose child is 0, that is,
a return. Every rooted walk of S84 starts at such a state (0, c), after its first integration from (a, 0).

**Proof.**
1. A driver y that is black at some tick t0 has exactly one child. At t0 the recursion resets, c(t0 + 1) = NOT x(t0),
   whatever c(t0) is. So running the recursion forward from t0 + 1 determines c uniquely, and the run closes at t0,
   because the reset value is the same. (Lean: `child_unique`, `child_exists`.)
2. The step (x, y) -> (y, c) is injective, because x(t) = c(t + 1) XOR (y(t) OR c(t)). (Lean: `step_injective`.)
3. Suppose the walk never returns. Its states have nonzero drivers and lie in a finite set, so two of them coincide.
   Let s_i = s_j, with i < j and i least.
   - If i >= 2, injectivity gives s_(i-1) = s_(j-1), against the choice of i.
   - So s_1 = (0, c) = s_j. Its first coordinate is the driver of s_(j-1), which is then 0, against the nonzero
     drivers.
   So the walk returns. (Lean: `terminates`, `rooted_walk_returns`.) ∎

*Scope.* No bound on the return depth follows. The measured depths are 88 and 371 at q = 8, 16 depths up to 214,006
at q = 16, and up to 9.1 x 10^9 so far at q = 32. GC865 and GC870 show the counting (2^q - 1 chains, mean length about
2^q on the full primitive domain), which is not a growth law for the rooted sample. This is not a prize claim.

*Near-entry gate (Local, at filing).* `--near 39` gives entries 10, 17 and 37, all at formal similarity 0.19 or
less: different subjects. Nothing is restated. Hard checks pass.
