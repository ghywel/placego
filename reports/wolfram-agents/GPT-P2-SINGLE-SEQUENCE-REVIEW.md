# Problem 2 single-sequence equivalence: source review

GPT, GC1864 / MI797, 2026-10-25. **COMPLETE: scoped source/hand PASS,
with a helper-label qualification.** This is an external equivalence, not a
proof of density one-half or a new project theorem.

The official catalogue at 06:57:05Z contained 40 entries, including
R30-20261025-eb3b91 (Lean Verified) and its replacement 5105a7 (building,
Lean source unavailable). At 06:58:30Z it contained 39 entries: the predecessor
was removed and replacement **R30-20261025-5105a7 was Lean Verified**.
The completed check at 06:57:29Z reports 118 replayed constants, standard
axioms only, one selected headline, and no verified official target.
The two actual downloaded sources are byte-identical: 586 lines, 24,577 bytes,
SHA-256 `2d24ba37ac3553a4e87b8531c1ceb8fe3a570d28a97bdc0c2296426e8c66adc4`.
Every source proof body was read. No independent kernel replay was performed.

Sources: [replacement status](https://www.wolframcloud.com/obj/rule-30-prize/Agents/status/R30-20261025-5105a7),
[actual submitted Lean source](https://www.wolframcloud.com/obj/rule-30-prize/Agents/api/file?id=R30-20261025-5105a7&kind=lean),
and [pinned official target](https://github.com/WolframInstitute/Rule30PrizeKit/blob/3eca23c0a9fa6b153313655e6d51835406c2d06e/lean/Ruliology/CellularAutomata/Rule30Prize.lean).
Credit belongs to the external submission; novelty was not assessed.

## What carries the headline

For an arbitrary Boolean sequence b, let D(n) be twice its black count before n
minus n. Boolean increments imply the exact Lipschitz bound
|D(m)-D(n)| <= m-n for n <= m, proved by finite telescoping.
The claimed equivalence is between D(n)/n tending to zero and the existence
of one strictly increasing natural sequence g for which, for every positive k,
eventually both k|D(g(j))| <= g(j) and
k(g(j+1)-g(j)) <= g(j). Separate eventual thresholds combine by their maximum.
Strict increase makes g unbounded and supplies a bracket for every sufficiently
large n; the source proves that bracket by induction.

At parameter 2k, bracket g(j) <= n < g(j+1). The base discrepancy costs at most
g(j)/(2k), and telescoping through the gap costs at most another g(j)/(2k).
Thus k|D(n)| <= g(j) <= n. This is the carrying implication.
The converse simply takes **g(j)=j**: density supplies accuracy, and gap 1
supplies the ratio condition eventually. The actual converse uses no diagonal
construction. The abstract's diagonalisation description is unnecessary to
this proof, and the source does not establish a separately formalized
return-gap predicate equivalence.

The official target bridge proves blackCount equals the finite sum of the
Boolean indicators by induction. Substitution matches the pinned official
integer definition of Problem2 exactly. The headline is an iff with Problem2,
not a theorem asserting Problem2. The argument before instantiation is generic;
no Rule 30 dynamics supplies a sequence or a rate. No circularity found.

## Other read helpers and their limits

- `densityOf_of_epsGaps`: for every positive tolerance e, some accuracy K>=e
  has a good scale g<=N with (e-1)N<=eg for every sufficiently large N.
  The source uses e=4k, bounds the gap and discrepancy separately, then reduces
  the scale. It supplies a sufficient hypothesis, not its realization.
- `densityOf_of_boundedGaps` actually assumes **bounded additive gaps**:
  for each k there is a fixed m with a k-good g in [N,N+m] eventually.
  Its comment “bounded relative gaps” must not be read as a fixed positive
  relative fraction being sufficient. The proof uses n>=(2k+1)m.
- Exact zero returns suffice only with the same vanishing relative gaps.
- FirstPassage quantifies every sufficiently large reached absolute height h:
  k h<=t whenever |D(t)|=h. Density excludes early large heights via |D(t)|<=t;
  the converse splits bounded heights below H from controlled heights above H.
  The source does not require defining a first-hit operator.

## Hand controls and scope

**Kill test for dropping the gap condition:** initialize the Boolean word 10,
so D(2)=0. On each interval [2^j,2^(j+1)), j>=1, use 2^(j-1) black cells
then 2^(j-1) white cells. Every dyadic endpoint has D=0, yet at the midpoint
n=3*2^(j-1), D(n)=2^(j-1), so D(n)/n=1/3. Infinitely many exact balanced
returns and fixed relative gaps therefore do not establish density one-half.
The hypothesis with every k rejects this example. This is a generic hand
control, not a Rule 30 trajectory or a new research result.

Dropping accuracy also fails: the all-black word with g(j)=j meets the gap
condition but violates accuracy for k=2. **Unexpected check:** a bounded
walk satisfies the large-height first-passage condition vacuously; that is
consistent with density one-half, not a defect. The zero scale g(0)=0 causes
no ratio division because all formal statements are integral and eventual.

Pure-file audit checked source equality, exact published check/headline/pin,
the identity converse, additive-gap hypothesis and official definition.
No Lean, automaton dynamics, benchmark, GPU, count evaluation or startup probe
was run; no startup pass is claimed. A speculative kit-root download returned
404; the documented official-target path succeeded. No authentication failure.
Record searched: return.gap, singleSequence, nearly.geometric: no hits.

Eight fixed payloads, each under 1 MiB, were retained and read back through
the authorized private HTTPS store at
`cited/gpt-p2-single-sequence-review-20261025/`.
Audit JSON SHA-256:
`fa1bfea22db0b12cc30ee9e0b746d76fcb9460ba087c3adf8114220c6d334578`.

Reasoned and gut verdicts agree: adopt the equivalence at source scope with
its gap/accuracy quantifiers intact; qualify the helper label. Neither source
provides a way to establish those quantifiers for the actual center column.
Problem 2, normality, CQ01 and an all-width D(W) bound remain open. No new
job, review request, Local wake, schedule change or held-lane reopening.
