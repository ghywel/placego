# A primitive six-cycle of sign type2+4 fits with any cancelling pair

*GPT's proofs, second-read. Derived from [PROOFS.md](../PROOFS.md), entry "G.GPT314. A primitive six-cycle of sign
type2+4 fits with any cancelling pair (2026-10-16; Cloud CL426)"; rebuild with `python3 proofs/build.py`. Edit the
proof in PROOFS.md and this summary in [summaries.md](summaries.md), never this file.*

**Status:** proved by GPT and second-read by Local.

## In plain words

A primitive six-move zero-sum component with two positive or two negative moves,
extrema sum<=28, fits in0..27 with any cancelling gap1..14 using eight different
folded labels. Computer-assisted PROOF-SKETCH: hand diameter reduction plus
complete span20 and25-wide-profile certificates; carrying read pending.

**Why it matters.** Closes this6+2 component type without a new target census.
It does not settle balanced six-cores, other factorizations or full even E28.

## The formal statement and proof

**Current status: PROVED in the stated scope, computer-assisted and two-party.**
Cloud CL426/a0caec24 independently verified the full statement by direct cyclic-order/
root/pair exhaustion on3409 primitive cores and all14 gaps. Original candidate
text below is retained verbatim as provenance; its sketch labels are historical.
No full E28/L8 conclusion or novelty claim.

### GPT G314 — A primitive six-cycle of sign type2+4 fits with any cancelling pair (2026-10-16; waiting room, MI145-148)

**Status: computer-assisted PROOF-SKETCH, independent carrying read requested.**
The hand reduction and independently implemented finite certificates are separate
premises below. No novelty claim or full E28/L8 conclusion. Provenance: MI143-148;
preregistrations bb346018,5764eeb2,0eee072e.

**Statement.** Let e1,...,e6 be nonzero integers summing0, with no nonempty proper
zero-sum submultiset. Suppose exactly two are positive or exactly two are negative,
and max(e_i)+max(-e_i)<=28. For every integer g in1..14 there is a cyclic ordering
of those moves whose six distinct partial-sum vertices have a translate in0..27,
and a physical pair(x,x+g) in0..27, such that all eight vertices have different
folded labels min(y,27-y). The closing partial sum is NOT a seventh vertex.

**Reduction.** First take two positive moves. The complete hand diameter argument
is reproduced verbatim from MI145; it includes nonprimitive tuples for the span
identity, while the statement uses minimality to make its six vertices distinct.

**Hand candidate, SKETCH.** Write positive moves a>=c>=1, negative magnitudes
b1>=b2>=b3>=b4>=1, P=a+c=sum b_i, and a+b1<=28. For any cyclic ordering,
rotate to start with +a and let B be the total negative magnitude before +c.
The two negative runs are monotone. Their partial-sum span is

    max(a,P-B)-min(0,a-B) = max(a,B,P-B).

Conversely every subset B is realized by such an order. Therefore the exact
minimum span is max(a, min_{subsets} max(B,P-B)). This is about span only;
minimality is needed separately for distinct partial sums.

Choose B=b1+b4 and order (+a,-b1,-b4,+c,-b2,-b3). Put C=b2+b3. We have
B<19: 3B=3b1+3b4 <=2b1+P <=2(a+b1)<=56.
Also a+1<=P<=4b1<=4(28-a), hence a<=22. If C<=20 and a<=20, the displayed
order has span<=20. If C>=21, then b1>=11. Since
b1+C+1<=P<=2a<=56-2b1, we get3b1<=34 and hence b1=11.
Then a<=17, P>=33 implies a=17, and P is33 or34. This leaves exactly:

|a,c|b1,b2,b3,b4|exact minimum span|
|---|---|---|
|17,16|11,11,10,1|21|
|17,17|11,11,10,2|21|
|17,17|11,11,11,1|22|

Direct subset sums have no balancing subset in[P-20,20]; their best maxima are
21,21,22. The prescribed end-pair order attains them. All three are primitive:
no negative subset sums to a or c. If a>=21, b1<=7, so B,C<=14 and the same
order has span exactly a. A step a forces that lower bound. Thus all six-move
lists of this sign type have minimum span<=22; precisely those with a>=21 or
one of the three rows require span>20. Sign reversal covers four-positive/two-
negative cores. One/five and three/three remain separate questions.


**Short-span certificate, MI144/B61.** Every normalized six-element subset of
0..20 containing0 has a joint placement with any gap1..14. The complete domain
has C(20,5)=15,504 shapes. All217,056 questions have literal witnesses, and full
root/edge maps agree between independent pair-sum/bitmask and physical/set
implementations. Cloud CL425/8e631206 independently replicated the whole result.
This is an exact finite premise, not an extrapolated hand span theorem.
Artifact cited/instinct/b61-six-plus-pair-81544cf1c7fc931c.json, SHA256
81544cf1c7fc931cbb3be2ed99d60131e01e07f3c36f200c1394c99b46398b00;
source tests/probes/instinct/path_forest_six_plus_pair.py, independent replication
 tests/probes/cloud_reads/b61_check.py. Fewer than six vertices are not used here.

**Wide-span reduction.** The hand classification leaves the three listed rows
and a21/22. For a21, b1<=7, sum b=21+c gives b4>=c. If b4=c, a proper two-cycle
exists. Otherwise b4>c, which is also sufficient for minimality (a negative
subset summing21 would have complement summing c, impossible when each b_i>c).
Consequently c1..5. The four deficits7-b_i are nonnegative, sum7-c, and b_i>c;
the20 sorted profiles have counts8,5,4,2,1 at c1..5. For a22, b1<=6, hence c1/2,
with magnitudes(6,6,6,5)/(6,6,6,6). Both are primitive. Including the three
small-step exceptions gives exactly25 wide primitive profiles.

**Wide-span certificate, MI148/B63.** For each of those25 profiles use ONLY
(+a,-b1,-b4,+c,-b2,-b3), normalize its six vertices, and allow translations
0..27-span. All350 combinations with g1..14 have a literal joint placement.
The complete sets of(root,pair-root), not just selected successes, agree between
formula-label-bitmask and direct-physical-coordinate-set implementations. All
retained witnesses are checked for eight distinct folded labels and the exact
cyclic displacement multiset. Domain completeness is also checked against B62's
independent full arithmetic generator and free-order minimum-span DP. Source
 tests/probes/instinct/path_forest_wide_six.py; no alternative permutation, role
repair or arbitrary cycle search. Artifact cited/instinct/b63-wide-six-d71dcdd07867d84a.json,
SHA256d71dcdd07867d84a84e82d48d003a39e907f2a3ea1dcf79e6ff6fdfdfcc732fe.
Thus every primitive two-positive core lies in a certified short or wide case.

**Other sign orientation.** Negate the six moves to put the sequence in the
previous case. Reflect all selected coordinates y->27-y afterward; this negates
every displacement and preserves every folded label. Swap the two pair owners
if needed. This proves the two-negative case with the same gap bound. It does
not claim that a sign-reversed target tuple meets the E28 sorting constraints.

**Fixed-role consequence.** If an even E28 move vector admits a factorization
into this primitive six-cycle and(+g,-g), the eight distinct labels reserve one
whole complementary pair per active bin. Fill the remaining pair slots, then
permute selected tokens around the cycles, as in the established allocator.
Every bin has h_i>=1, and the target change is2e_i, so the exact odd partition
follows. We do not assert that every E28 move vector has this component type.
Primitive8, other component sizes and six-core sign types1+5/3+3 are not covered.
The three finite scripts validate their own stated domains; their agreement is
a self-check, except B61's explicitly identified independent Cloud replication.

**Filing check.** proof_dupes --near W314 passes. Nearest G309,G306,G313
read in full. G309 constructs a two-surplus target slice, G306 a one-negative
cycle, and G313 four two-cycles. This proof combines a six-core diameter
classification with generic joint geometry; it does not restate those results.


**Independent carrying read, Cloud CL426 (verbatim). VERIFIED.** I checked the
statement itself rather than your route: enumerate every core a ≥ c ≥ 1, b1 ≥ … ≥ b4 ≥ 1, a + c = Σb, a + b1 ≤ 28
(7,300 tuples, 3,409 primitive, your counts), and for each primitive core and each g in 1..14 search all cyclic orders,
roots and physical pairs for eight distinct labels. No failure in 47,726 questions, 1.1 CPU seconds. The hand
classification of B62 is also confirmed independently: the minimum span over orders equals max(a, min over negative
subsets of max(B, P − B)) on all 3,409 cores, and the cores needing span above 20 are exactly the 22 with a ≥ 21 and the
three rows (17,16; 11,11,10,1), (17,17; 11,11,10,2), (17,17; 11,11,11,1), with minima 21, 21, 22. The 4+2 type follows by
negating moves and reflecting coordinates, which preserves labels. On the project's rule G314 leaves the waiting room:
PROVED in scope, computer-assisted and now two-party; the 1+5 and 3+3 types stay open as you say.

**Promotion filing check (2026-10-16).** proof_dupes --near W314 passes;
nearest G309,G306,G313 read in full again. This joint six-core/gap placement
is distinct from G309's two-surplus slice, G306's one-negative cycle and G313's
four cancelling pairs. The complete primitive8 and1+5/3+3 six-core questions
remain open. No new proof is inferred from those separate results.
After promotion the G314 query also returns G311; read in full. Its spare-edge
matching argument for a five-core differs from this six-core diameter reduction.
