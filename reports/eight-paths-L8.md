# The eight-path burning threshold is 68

*Draft note, 19 October 2026. Author line to be decided by the project owner; see the statement on method at the end.*

## Abstract

A path forest is a disjoint union of paths. Tan and Teh showed that for each n there is a least L_n such that every
forest of n paths, each of order at least L_n, is well-burnable, and they determined L_1, …, L_7 = 1, 3, 18, 26, 36,
46, 56, leaving n = 8 open "due to computational limitations". We show L_8 = 68. The upper bound reduces, by a
short induction, to a finite statement about 64,787,844 eight-tuples, each of which was given an explicit certificate
and independently re-verified; the lower bound is the forest (67, 67, 67, 67, 102, 102, 102, 102), for which we give a
three-line counting proof. The value agrees with Tan and Teh's Conjecture 2.7, which predicts L_n = M_n + 1 with
M_n the largest odd number at most 12n − 2√(18n − 12) − 6.

## 1. Setting

Graph burning (Bonato, Janssen and Roshanbin, 2016) is the discrete process in which, at each round, every burned
vertex burns its neighbours and one further unburned vertex is chosen to burn. The burning number b(G) is the least
number of rounds that burn all of G, and G is *well-burnable* if b(G) ≤ ⌈√|G|⌉, the bound conjectured for all
connected graphs. For path forests, which are disconnected, well-burnability can fail, and Tan and Teh [TT24, Theorem
1.1] proved that it holds whenever the shortest path is long enough:

> For every n there is a least L_n such that every n-path forest whose shortest path has order at least L_n is
> well-burnable.

In the same paper they record L_1 = 1, L_2 = 3, L_3 = 18, L_4 = 26 and determine L_5 = 36, L_6 = 46, L_7 = 56 by
complete computer lists, prove a formula for the largest shortest path of an *impossibly burnable* forest (one that
fails a simple plank-counting test), and conjecture that this counting test is the only obstruction once the shortest
path is at least L_{n−1}, which would give L_n = M_n + 1 for all n. For n = 8 the formula gives M_8 = 67, so
L_8 ≥ 68, and their conjecture predicts equality.

The problem has a well-known integer form, also stated in [TT24]: an n-path forest of order m² with path orders
l_1, …, l_n is burnable in m rounds if and only if the set O_m = {1, 3, …, 2m − 1} of the first m odd numbers can be
partitioned into n parts with sums l_1, …, l_n. We prove the "if" direction we need in Section 4, including the
case of non-square order, so that the result does not depend on any monotonicity of the burning number.

## 2. The theorem

**Theorem.** L_8 = 68. Equivalently, for every m and every eight integers l_1, …, l_8 ≥ 68 with Σ l_i = m², the set
O_m can be partitioned into eight parts with sums l_1, …, l_8; and the forest (67⁴, 102⁴) is not well-burnable.

## 3. Reduction to a finite set of instances

Call an eight-tuple *exceptional at level m* if its entries are nondecreasing, lie in [68, 2m + 66] and sum to m²; let
E_m be the set of such tuples.

**Lemma 1.** If every tuple of E_m admits a partition of O_m for every m with 24 ≤ m ≤ 32, then every eight-tuple of
integers ≥ 68 with sum m² admits a partition of O_m, for every m.

*Proof.* Let P_m be the statement for level m, with no upper bound on the entries. For m ≤ 23 it is vacuous, since
m² ≤ 529 < 544 = 8 · 68. Let m ≥ 24 and assume P_j for all j < m. Take a tuple at level m. If every entry is at most
2m + 66, then m ≤ 32, because for m ≥ 33 we have m² > 8(2m + 66) (the difference is 33 at m = 33 and increases by
2m − 15 with each step), and the tuple lies in E_m, where the hypothesis applies. Otherwise some entry satisfies
l_i ≥ 2m + 67. Replace it by l_i − (2m − 1) ≥ 68. The new tuple has sum (m − 1)², so P_{m−1} gives a partition of
O_{m−1}; adding the plank 2m − 1 to the part of the reduced entry gives a partition of O_m with the original sums.
(At m = 24 the second case cannot occur, since 115 + 7 · 68 > 576, so the induction never descends below level 24.) ∎

The levels are not empty only for 24 ≤ m ≤ 32, and their sizes are

| m | 24 | 25 | 26 | 27 | 28 | 29 | 30 | 31 | 32 | total |
|---|---|---|---|---|---|---|---|---|---|---|
| |E_m| | 3,319 | 425,632 | 5,523,890 | 19,382,158 | 24,688,633 | 12,385,850 | 2,271,658 | 106,518 | 186 | 64,787,844 |

These counts were obtained twice, by a generating-function computation and by an independent bounded-partition
recurrence, and agree.

## 4. From partitions to burning

**Lemma 2.** Let F be a path forest of order N, m = ⌈√N⌉, and suppose that after extending one path at an end so that
the order becomes m², the eight path orders admit a partition of O_m. Then b(F) ≤ m.

*Proof.* Cut each extended path into consecutive intervals of the odd lengths assigned to it. For the interval of
length 2r + 1, let its middle vertex be the source lit at round m − r; by round m this fire has radius r and covers
exactly its interval. The lengths 1, 3, …, 2m − 1 are distinct, so exactly one source is scheduled per round. The
schedule is legal: two intervals in one path with radii r > s have centres r + s + 1 apart, while the earlier fire
(lit at round m − r) has radius r − s at round m − s, which is smaller, so the later centre is still unburned when it is
lit. For the original forest, project every centre that lies in the added segment to the former endpoint of its path;
distances to original vertices do not increase, so the projected balls still cover F by round m. If a projected centre
is already burned when its round comes, say by a source lit at round t₀ < t, then every vertex within m − t of it is
within m − t₀ of that earlier source and will burn by round m in any case; so we may light any unburned vertex instead,
or none. This is a legal burning process of F in at most m rounds. ∎

## 5. The certificates

For each tuple in E_24 ∪ … ∪ E_32 an explicit partition of O_m was computed by a backtracking search (largest plank
first, with a parity-aware count bound as pruning), and recorded as the part index of each plank. The run took 6,385
seconds on eight cores of a laptop. Every record was then re-verified by two programs written independently of the
search and of each other: the first recomputes every part sum from the plank list and checks the tuple's membership
in its level; the second, in addition, counts the records of every chunk (level, smallest entry) against an exact
dynamic-programming count of that chunk, requires strictly increasing lexicographic order within chunks, and requires
every chunk file to be present and complete. Both report the same SHA-256 of the record stream,

    90fea878fc36d18da25e52b2e73fbfcb8e4a447c72e470f9e5c3a5ea30d1063b,

64,787,844 valid records, no record impossible or unresolved, and chunk counts equal to the table above in every
chunk. Both verifiers were shown to reject deliberately corrupted inputs (a swapped pair of planks; a duplicated record
replacing an omitted one) before the production run. Four of the nine levels (m = 24, 25, 31, 32; 535,655 tuples)
were additionally certified by a third, unrelated program on another machine.

The programs are in the project repository: `tests/probes/cloud_reads/l8_certificates.py` (generation and first
verifier), `tests/probes/instinct/l8_stream_verify.py` (second verifier), `tests/probes/instinct/l8_certificate_census.py`
(counts), `tests/probes/cloud_reads/e_slice.py` and `cert_check.py` (the third program). Regeneration from an empty
directory is

    python3 tests/probes/cloud_reads/l8_certificates.py run  OUTDIR --workers 8
    python3 tests/probes/cloud_reads/l8_certificates.py check OUTDIR
    python3 tests/probes/instinct/l8_stream_verify.py OUTDIR

and reproduces the digest above. The 6.9 GB record stream is held by the project and can be supplied; the digest and
the regeneration commands are the permanent record.

## 6. The lower bound

**Lemma 3.** The forest with four paths of order 67 and four of order 102 (total 676 = 26²) is not burnable in 26
rounds.

*Proof.* A source lit at round t burns at most 2(26 − t) + 1 vertices by round 26, and these capacities,
51, 49, …, 1, sum to exactly 676. A successful process must therefore attain every capacity with no overlap, so the
odd numbers 1, 3, …, 51 are partitioned into the eight path orders. A part summing to 67 has an odd number of odd
summands and cannot be a single one (the largest is 51), so has at least three; a part summing to 102 has an even
number and cannot be two (51 + 49 = 100), so has at least four. That needs 4 · 3 + 4 · 4 = 28 odd numbers; only 26
exist. ∎

Since every path of this forest has order at least 67, L_8 ≥ 68. This is Tan and Teh's example; the argument above is
the elementary form of their impossibly-burnable test.

## 7. Proof of the theorem

Lemma 1 and the certificates of Section 5 give the partition for every eight-tuple of integers ≥ 68 with square sum;
Lemma 2 turns each partition into a burning process in m = ⌈√N⌉ rounds, for square and non-square order alike. Hence
every eight-path forest with shortest path at least 68 is well-burnable, L_8 ≤ 68, and Lemma 3 gives equality. ∎

## 8. Remarks

1. *The conjecture.* Tan and Teh's Conjecture 2.7 predicts L_n = M_n + 1 with M_n the largest odd number at most
   12n − 2√(18n − 12) − 6; at n = 8 this is 68, so the theorem confirms the conjecture at n = 8. The next predicted
   values are 78, 88, 98, 110. The same reduction applies for every n and leaves finitely many levels; for n = 9 the
   levels are m = 27, …, 36 and the number of tuples is of the order of 10⁹.
2. *Why the real instances are easy.* The search never needed more than 4,916 nodes on any tuple, and 8.3% of tuples
   were solved with no backtracking at all. At m = 24 every all-odd tuple is forced to three planks per path, and
   every such tuple admits a tiling in which each part takes one plank from each third of the plank list, with the
   highs assigned to the parts in sorted order; the hand admission and the finite completion of that observation are
   in the project record. Whether a single explicit construction tiles every tuple of every level is open; the
   general sufficiency of the natural cut conditions for partitions of an interval into parts of size at least three
   is known to fail once the interval has holes, and the equal-sum case with parts of size at least three is listed as
   open by Hoory and Kotlar.
3. *Status.* This is a computer-assisted result in the same sense as Tan and Teh's determination of L_5, L_6, L_7:
   the mathematical content is Lemmas 1–3, and the finite premise is a verified certificate stream. A bounded
   literature search found no later determination of L_8; we make no claim of priority beyond that.

## References

- A. Bonato, J. Janssen, E. Roshanbin, How to burn a graph, Internet Mathematics 12 (2016).
- T. S. Tan, W. C. Teh, A note on graph burning of path forests, Discrete Mathematics and Theoretical Computer
  Science 26:3 (2024), #1; arXiv:2312.10914.
- S. Hoory, D. Kotlar, On the equal sum partition problem, arXiv:2605.06071.

## Statement on method

The reduction, the certificate program, the two verifiers and the proofs of Lemmas 1–3 were produced by two AI
model instances (an Anthropic Claude and an OpenAI GPT) working under the direction of the project owner, with each
mathematical step read independently by the other instance and the computation run and verified on the owner's
machine. The owner designed the working method and chose the questions. The author line is the owner's decision.
