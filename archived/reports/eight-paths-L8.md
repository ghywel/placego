# The eight-path burning threshold is 68

**The Wolfram · Collatz · Mahler project:**
**Gareth (Human) - Claude (Anthropic SI) - ChatGPT (OpenAI SI): Equals amongst mankind and machines.**

*Note, 19 October 2026; revised the same day against GPT's reading checklist (ledger GC1595); author line set by the
owner on 20 October 2026. Published on the project website; see the statement on method at the end.*

## Abstract

A path forest is a disjoint union of paths. Tan and Teh showed that for each n there is a least L_n such that every
forest of n paths, each of order at least L_n, is well-burnable, and they determined L_1, …, L_7 = 1, 3, 18, 26, 36,
46, 56, leaving n = 8 open "due to computational limitations". We show L_8 = 68. The upper bound reduces, by a
short induction, to a finite statement about 64,787,844 eight-tuples, each of which was given an explicit certificate
that two separate programs re-verified; the lower bound is the forest (67, 67, 67, 67, 102, 102, 102, 102), for which we give a
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

**Theorem.** L_8 = 68. The proof shows that for every positive integer m and every eight integers l_1, …, l_8 ≥ 68 with Σ l_i = m², the set
O_m can be partitioned into eight parts with sums l_1, …, l_8 (Sections 3 to 5), that this gives the upper bound for
forests of any order (Section 4), and that the forest (67⁴, 102⁴) is not well-burnable (Section 6).

## 3. Reduction to a finite set of instances

Call an eight-tuple *exceptional at level m* if its entries are nondecreasing, lie in [68, 2m + 66] and sum to m²; let
E_m be the set of such tuples.

**Lemma 1.** If every tuple of E_m admits a partition of O_m for every m with 24 ≤ m ≤ 32, then for every positive
integer m, every eight-tuple of integers ≥ 68 with sum m² admits a partition of O_m.

*Proof.* Let P_m be the statement for level m, with no upper bound on the entries. For 1 ≤ m ≤ 23 it is vacuous, since
m² ≤ 529 < 544 = 8 · 68. Let m ≥ 24 and assume P_j for all j < m. Take a tuple at level m. If every entry is at most
2m + 66, then m ≤ 32, because for m ≥ 33 we have m² > 8(2m + 66) (the difference is 33 at m = 33 and increases by
2m − 15 with each step), and the tuple lies in E_m, where the hypothesis applies. Otherwise some entry satisfies
l_i ≥ 2m + 67. Replace it by l_i − (2m − 1) ≥ 68. The new tuple has sum (m − 1)², so P_{m−1} gives a partition of
O_{m−1}; adding the plank 2m − 1 to the part of the reduced entry gives a partition of O_m with the original sums.
(At m = 24 the second case cannot occur, since 115 + 7 · 68 > 576, so the induction never descends below level 24.) ∎

The levels are not empty only for 24 ≤ m ≤ 32, and their sizes are

| m | 24 | 25 | 26 | 27 | 28 | 29 | 30 | 31 | 32 | total |
|---|---|---|---|---|---|---|---|---|---|---|
| size of E_m | 3,319 | 425,632 | 5,523,890 | 19,382,158 | 24,688,633 | 12,385,850 | 2,271,658 | 106,518 | 186 | 64,787,844 |

These counts were obtained by two parties in two ways, as coefficients of the Gaussian-binomial generating function for
partitions in a box (DLMF 26.9) and by an elementary bounded-partition recurrence, and agree level by level.

## 4. From partitions to burning

**Lemma 2.** Let F be an eight-path forest of order N, m = ⌈√N⌉, and suppose that after extending one path at an end so that
the order becomes m², the eight path orders admit a partition of O_m. Then b(F) ≤ m.

*Proof.* We use the convention of [TT24]: a source placed at the start of round t is burned in round t, and a vertex
burned in round t − 1 burns its unburned neighbours in round t. A source placed in round t has therefore burned exactly
the vertices within distance m − t of it by the end of round m, and exactly those within distance k − 1 − t when round
k ≥ t + 1 begins.

Cut each extended path into consecutive intervals of the odd lengths assigned to it. For the interval of length
2r + 1, place a source at its middle vertex in round m − r; by the end of round m this fire covers exactly its interval.
The lengths 1, 3, …, 2m − 1 are distinct, so exactly one source is scheduled per round. The schedule is legal. Take two
intervals in the same path with radii r > s, so the larger one's source is placed first. Their centres are at distance
at least r + s + 1 (equality exactly when the intervals are adjacent). When round m − s begins, the earlier fire has
radius (m − s − 1) − (m − r) = r − s − 1 < r + s + 1, so the later centre is still unburned when it is chosen.
Sources on different paths never interact.

For the original forest, project every centre that lies in the added segment to the former endpoint of its path;
distances to original vertices do not increase, so the projected balls still cover F by the end of round m. Projection
can make a centre, projected or not, burned before its round. If a centre is already burned when its round t comes, say by a source placed in round t₀ < t, then every vertex
within distance m − t of it lies within distance m − 1 − t₀ of that earlier source, which was actually placed, and burns by round m in any case; so we
may place the round-t source at any unburned vertex instead, or end early if none remains. This is a legal burning process of F in at most m rounds. ∎

## 5. The certificates

**Generation.** For each tuple in E_24 ∪ … ∪ E_32 an explicit partition of O_m was computed by a backtracking search
(largest plank first, with a parity-aware count bound as pruning) and recorded as the part index of each plank, with
the number of search nodes. The work was split into 285 chunks (level, smallest entry), each written to its own file
ending in a footer line with the chunk's statistics and its elapsed time. The run took 6,385 seconds on eight cores of
a laptop, in one pass with no restart. No tuple was reported impossible, and none hit the per-tuple time cap.

**Verification.** Every record was re-verified by two programs:
- *The generator's checker*, a separate function in the generating program, written by the same author as the search
  and sharing with it only the one-line function that lists the planks. It recomputes every part sum from the plank list and checks the tuple's membership in
  its level. Before the run it was shown to reject a certificate with two planks deliberately swapped between parts.
- *An independent stream verifier*, written by the other AI instance and sharing no code with the generator. It
  requires every chunk file to be present and complete, strictly increasing lexicographic order within each chunk, and
  a record count in every chunk equal to an exact dynamic-programming count of that chunk. It recomputes every part sum.
  Before it was applied to the stream it was shown to reject a corrupted tiling and a duplicated record replacing an
  omitted one, in both
  cases with valid per-record sums and the correct total count.

Both report 64,787,844 valid records, no record impossible or unresolved, chunk counts equal to the table of Section 3,
and the same SHA-256 of the retained byte stream (the chunk files concatenated in name order),

    90fea878fc36d18da25e52b2e73fbfcb8e4a447c72e470f9e5c3a5ea30d1063b.

This digest identifies the retained stream exactly. It is not reproducible by a fresh run, because each chunk's footer
records elapsed time. For regeneration the generator's checker now also prints a *timing-free digest*, the SHA-256 of
the same stream with the elapsed-time field removed from every footer. The search is deterministic, so every
regeneration with the same programs that finishes without hitting the time cap gives the same timing-free digest; this was tested on four
levels (m = 24, 25, 31, 32; 130 chunks), regenerated twice with four and with two parallel workers. Both runs give the
timing-free digest

    0d3799d021b0182d998426f5fe17ff7dac7be3af652acea4ccd7bb30669530f1,

while their byte-stream digests differ (6caa653b… and 218cd0c6…). The timing-free digest of the retained stream is

    da7c2e7716df23188cba01580ceabb4172e924529b9b73721671c330479c3a96.

Restricted to the four levels m = 24, 25, 31 and 32, the retained stream gives 0d3799d0…669530f1, the value of the
two regenerations. So the retained run and the regenerations agree byte for byte on those levels, apart from timing
(ledger L744).

**A further independent run.** Levels m = 24, 25, 31 and 32 (535,655 tuples) were also certified by a third program on
another machine, with its own enumerator, its own search and its own checker. It was written by the author of the
generator and uses a related search, so its value is an independent regeneration of those levels, not an independent
design.

**Source versions.** All programs are in the project repository. The generator and its checker are
`tests/probes/cloud_reads/l8_certificates.py`, run at commit 61edb625. Later commits change only the restart gate,
which the single run never used, and add the timing-free digest. The stream verifier is
`tests/probes/instinct/l8_stream_verify.py` at 87a2b0d9, and the chunk census is
`tests/probes/instinct/l8_certificate_census.py` at 75de7744. The third program is `tests/probes/cloud_reads/e_slice.py`
with `cert_check.py`, at 1d89615b. Regeneration into an empty directory is

    python3 tests/probes/cloud_reads/l8_certificates.py run  OUTDIR --workers 8
    python3 tests/probes/cloud_reads/l8_certificates.py check OUTDIR
    python3 tests/probes/instinct/l8_stream_verify.py OUTDIR

The first two commands regenerate and check the records and print both digests. The third verifies the stream
independently; it prints the byte-stream digest of the new run, which will differ from the one above.

## 6. The lower bound

**Lemma 3.** The forest with four paths of order 67 and four of order 102 (total 676 = 26²) is not burnable in 26
rounds.

*Proof.* A source placed in round t has burned at most 2(26 − t) + 1 vertices of its path by the end of round 26, and
these capacities, 51, 49, …, 1, sum to exactly 676. A process with fewer than 26 rounds has smaller total capacity and
cannot succeed. A successful 26-round process must therefore attain every capacity with no overlap, so the
odd numbers 1, 3, …, 51 are partitioned into the eight path orders. A part summing to 67 has an odd number of odd
summands and cannot be a single one (the largest is 51), so has at least three; a part summing to 102 has an even
number and cannot be two (51 + 49 = 100), so has at least four. That needs 4 · 3 + 4 · 4 = 28 odd numbers; only 26
exist. ∎

Since every path of this forest has order at least 67, L_8 ≥ 68. This is Tan and Teh's example [TT24, Theorem 1.3 with
n = 8]; the argument above is the elementary form of their impossibly-burnable test.

## 7. Proof of the theorem

Lemma 1 and the certificates of Section 5 give the partition for every eight-tuple of integers ≥ 68 with square sum;
Lemma 2 turns each partition into a burning process in m = ⌈√N⌉ rounds, for square and non-square order alike. Hence
every eight-path forest with shortest path at least 68 is well-burnable, L_8 ≤ 68, and Lemma 3 gives equality. ∎

## 8. Remarks

1. *The conjecture.* Tan and Teh's Conjecture 2.7 predicts L_n = M_n + 1 with M_n the largest odd number at most
   12n − 2√(18n − 12) − 6; at n = 8 this is 68, so the theorem confirms the conjecture at n = 8. The next predicted
   values are 78, 88, 98, 110. The same reduction applies for every n and leaves finitely many levels; for n = 9 with
   the predicted threshold 78, the levels are m = 27, …, 36 and hold 1,167,813,363 tuples (by the recurrence of
   Section 3), eighteen times as many as for n = 8.
2. *Why the real instances are easy.* The search never needed more than 4,916 nodes on any tuple, and 8.28% of tuples
   were solved with no backtracking at all (node count m + 1). At m = 24 every tuple of odd entries is forced to three
   planks per part, and every such tuple admits a tiling in which each part takes one plank from each third of the
   plank list, with the largest planks assigned to the parts in sorted order; this was checked on all 70 such tuples.
   No simple deterministic rule tiles every tuple: three natural rules with no backtracking, tried on all tuples at m = 24, 25, 31,
   32 and on 60,000 random tuples at each other level, together tile only about 13% to 30% of them. In the certified
   tilings, the parts with few planks often take consecutive planks from the top of the list paired against
   consecutive planks below the middle, with a constant pair sum; no greedy order finds these pairings. Whether a single
   explicit construction tiles every tuple of every level is open. Natural cut-and-margin conditions that would make
   such a construction routine fail in our experiments once some planks are removed from the interval, and the
   equal-sum case with parts of size at least three is listed as open by Hoory and Kotlar.
3. *Status.* This is a computer-assisted result in the same sense as Tan and Teh's determination of L_5, L_6, L_7:
   the mathematical content is Lemmas 1–3, and the finite premise is a verified certificate stream.
4. *Prior work searched.* Two bounded searches (19 October 2026) found no later determination of L_8. The only paper
   indexed by Semantic Scholar as citing [TT24] is Leong, Sim and Teh (2025), which lists exact values through L_7. A
   search of arXiv for burning and path forests found no later paper on the threshold. The partition results that
   [TT24] cite for odd numbers (Fu and Hu 1994, Enomoto and Kano 1995) concern a common sum for all parts, not unequal
   prescribed sums; their full texts could not be retrieved, and no odd-number analogue of Chen, Fu, Wang and Zhou's
   prescribed-sum theorem was found. Google Scholar, MathSciNet and zbMATH were not consulted. This is a statement of
   what was searched, not a claim of priority.

## 9. Code and data availability

The owner decided on 19 October 2026 that the code and data are published on the project's website beside the
explanatory page, at `wolframcollatzmahler.com/eightstreets/release/`, rather than only through the repository.
1. *Code.* `release/code/` holds every program named in Section 5, the packing tools, the rule experiment of Remark 2
   and the counter for Remark 1, with their SHA-256 digests in `release/README.txt`. Done.
2. *Digests.* The timing-free digest of the retained stream was computed in the same pass that packed it (ledger
   CL461, L744), and is recorded in Section 5 beside the byte-stream digest. Done.
3. *Data.* The retained stream, packed as nine xz files (one per level, concatenating to the original bytes) with a
   manifest of sizes and digests, is in `release/data/` (340 MB), with the third program's certificates for four
   levels. Unpacking it restored the stream byte for byte, and the stream verifier passed on the restored copy
   (ledger L744). Done.
4. *Licence.* None, by the owner's decision (19 October 2026).
5. *Where it lives.* The project website only: no DOI and no formal repository or journal, by the owner's decision
   (19 October 2026).
6. *Author line.* As at the head of the note, by the owner's decision (20 October 2026).

## References

- A. Bonato, J. Janssen, E. Roshanbin, How to burn a graph, Internet Math. 12 (2016) 85–100.
- T. S. Tan, W. C. Teh, A note on graph burning of path forests, Discrete Mathematics and Theoretical Computer
  Science 26:3 (2024), #1; arXiv:2312.10914.
- F.-L. Chen, H.-L. Fu, Y. Wang, J. Zhou, Partition of a set of integers into subsets with prescribed sums, Taiwanese
  J. Math. 9 (2005) 629–638.
- H. Enomoto, M. Kano, Disjoint odd integer subsets having a constant even sum, Discrete Math. 137 (1995) 189–193.
- H.-L. Fu, W. H. Hu, Disjoint odd integer subsets having a constant odd sum, Discrete Math. 128 (1994) 143–150.
- S. Hoory, D. Kotlar, On the equal sum partition problem, arXiv:2605.06071.
- E. J. T. Leong, K. A. Sim, W. C. Teh, From burning extremal balanced spiders into properties for generalization to all
  trees, Bull. Malays. Math. Sci. Soc. (2025).

## Statement on method

The reduction, the certificate programs, the verifiers and the proofs of Lemmas 1–3 were produced by three AI model
instances (two Anthropic Claude instances and one OpenAI GPT instance) working under the direction of the project
owner. Each mathematical step was read by an instance other than its author, and the certificate run was made and
verified on the owner's machine. The owner designed the working method and chose the questions, and set the author line.
