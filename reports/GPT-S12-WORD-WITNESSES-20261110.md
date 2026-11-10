# S12 stage 2: explicit finite word witnesses

GPT GC2818 audit, 10 November. **PROOF-SKETCH: implementation support pending Local's read; no new module or compile.** The CP3.2 hand argument was already carried GC2702. This note makes its finite witnesses and guards explicit and avoids requiring a count of all right-special factors. Local retains every S12 module/build; L1634 starts stage 1, while this is a separate hand/source audit for stage 2.

## The exact input needed from stage 1

For a Boolean word f, use ordinary factors from all positions, including position 0. Write `BlockEq(i,j,n)` for agreement at offsets r<n. The needed hypothesis is the bounded-lag conclusion from the diagonal plan:

```text
BL(f): for every K there exists B such that
  i<j, j<=n+K, BlockEq(i,j,n) ==> j-i<=B.
```

Together with non-eventual-periodicity, it implies

```text
for every K, eventually p_f(n)>n+K.
```

The actual free word is not eventually periodic by the kit's `free_not_eventuallyPeriodic`, with its finite-support and constrained-row hypotheses. Alternatively BL alone rules out an eventual period: choose K=0, two sufficiently late starts separated by a period multiple larger than B, and then n>=j. Their length-n blocks agree and contradict BL. Thus no extra recurrence or uniform-recurrence hypothesis is being added to the word.

## A finite two-run lemma

Fix q>=1. A q-periodic run starts at a and has length L>=q when

```text
f(a+r+q)=f(a+r) for every r with r+q<L.
```

For this lemma require a>0 and both breakers:

```text
left:  f(a-1) != f(a+q-1);
right: f(a+L) != f(a+L-q).
```

These are exactly the conditions that this q-run cannot extend one cell to either side. Its least period need not be q.

Suppose A=(a,L) and B=(b,M) are two such runs, their first q cells agree, and

```text
L>=q,  M>=L+q+1,  a>0,  b>0.
```

Their chronological positions need not be ordered. Define two length-(L+1) factors:

```text
U = the factor starting at a-1;
V = the factor starting at v=b+M-L-1.
```

They are distinct right-special factors, with the following explicit occurrences.

**U:** its occurrences at a-1 and b-1 agree. The predecessors agree because each is the binary complement of the same periodic predecessor, determined by the common first q-block. The next L cells agree by q-periodicity and the same first q-block. Their following cells are respectively

```text
f(a+L) and f(b+L)=f(a+L-q),
```

which differ by A's right breaker. So U has both Boolean right extensions. This is the step that uses the binary alphabet.

**V:** its occurrences at v and v-q agree by B's q-periodicity. Both lie within B, because M>=L+q+1 gives v-q>=b. Their following cells are

```text
f(b+M) and f(b+M-q),
```

which differ by B's right breaker. Thus V is right-special too. The shorter occurrence ends before B's end, so no period assertion outside B is used.

**Distinctness:** V has period q, since it lies inside B. U does not: its positions 0 and q disagree by A's left breaker. Position q exists because L>=q. Therefore U!=V. No alignment of L and M modulo q is needed.

This finite statement is a convenient first stage-2 Lean lemma. It only refers to natural indices, Boolean equality and a finite collection of period/breaker hypotheses. It does not require infinite languages, asymptotic complexity, recurrence or a canonical minimal-period representation.

## One-sided maximal runs: why the breakers are available

In a non-eventually-q-periodic word, every finite q-periodic factor can be extended maximally to the right only a finite distance; otherwise the word would be q-periodic from its start. Extend to the left until a breaker or position 0. This also takes only finitely many steps.

Runs starting at position 0 are a genuine boundary case, not an excuse to assume recurrence. There is at most one maximal q-periodic prefix, and it has finite length unless the entire word is q-periodic. Consequently an unbounded family of q-periodic factors yields unbounded maximal q-runs with positive start and both breakers.

There are finitely many first q-blocks. At least one occurs as the first block of maximal q-runs with unbounded lengths. Choose A in that family with L as large as required, then choose B in the same family with M>=L+q+1. The finite lemma supplies two right-special factors of arbitrarily large common lengths L+1. This is valid for one-sided words that are not recurrent.

## Avoid the exact right-special counting theorem

Let F_n be the finite set of length-n factors, and p(n)=|F_n|. Deleting the final letter gives a surjection

```text
pi: F_(n+1) -> F_n.
```

Every fibre is nonempty. If two distinct length-n factors are right-special, each of their fibres has two elements, so

```text
p(n+1)>=p(n)+2.
```

One can prove this by choosing one lift of every factor and retaining one extra lift over each of the two distinguished factors. The two extra lifts are distinct from the chosen lifts and from each other because their prefixes differ. This is an elementary finite-surjection inequality; the exact formula counting all right-special factors is unnecessary.

For a non-eventually-periodic word, `p(n+1)>=p(n)+1` for every n. Otherwise the same surjection is bijective, so each factor has a unique right extension. Equal windows then have equal futures; a repeated finite window makes the word eventually periodic. This is the actual Morse–Hedlund/deterministic-window argument in the kit's `ShiftOrbit` and `WordsAutomata`, and should be credited as known.

## Complete the bounded-excess contradiction with finite maxima

Assume the target fails for a fixed K: arbitrarily large n satisfy p(n)<=n+K. Since f is not eventually periodic, the integer excess e(n)=p(n)-n is nondecreasing. Each e(n) is at most K, by comparing it with a later bounded-excess value. A bounded nondecreasing integer sequence is eventually constant, so

```text
p(n+1)=p(n)+1 for all n>=N0.
```

By the two-fibre inequality there cannot be two distinct right-special factors at any such length. The finite two-run lemma therefore shows: for every fixed q>=1 there is a bound R_q on the lengths of q-periodic factors.

Take B from BL for this K. If B=0, the pigeonhole step below is already contradictory. Otherwise choose one common finite bound R for q=1,...,B. This is a maximum over finitely many numbers, not an infinite uniform period bound. Choose n>R. The global excess bound gives p(n)<=n+K. Among the n+K+1 windows starting at

```text
0,1,...,n+K
```

two agree, at i<j. BL gives q=j-i<=B, while q>=1. The union of the two equal windows is q-periodic of length n+q: its required period equalities are exactly `BlockEq(i,j,n)`. This exceeds R and contradicts the q-periodic-factor bound. The target follows for every K.

No infinite subsequence selection, full classification of quasi-Sturmian words or quantitative rate for p(n)-n is needed. The initial position zero is included in the pigeonhole count and treated separately only when producing two-sided breakers for long periodic runs.

## Known source and formal work still required

Read at actual kit03a19bf6:

- `ShiftOrbit.factors`, `image_init_factors`, `unique_right_extension`, `eventuallyPeriodic_of_ncard_factors_succ_le` and the Morse–Hedlund equivalences;
- `WordsAutomata.OccursThen`, `RightSpecial`, `occursThen_ofFn`, `determined_of_not_rightSpecial` and `not_eventuallyPeriodic_iff_rightSpecial`, together with that module's scope and source notes.

These modules are Mathlib-based equivalents, not a ready-made core-Lean dependency for the portal packet. The finite-surjection inequality, factor-count model and finite word witnesses still need a core implementation or an explicitly chosen supported dependency. This note does not pretend that stage 2 becomes a single compiler invocation.

The kit credits [Cassaigne, *Complexité et facteurs spéciaux* (1997)](https://doi.org/10.36045/bbms/1105730624), §3.1.1, for the exact binary special-factor count. That is known context, not a new claim here. The publisher DOI/primary page was located during this audit, but the full article could not be retrieved through the available browser (publisher challenge/old institutional timeout); no fresh full-paper read is claimed. The displayed finite inequality and witnesses are proved explicitly above and the known kit proof was read directly. No literature-priority conclusion follows.

Record searched: right-special/quasi-Sturmian, GC2702 and current kit lean/equivalents/catalogues/portal/openPR index14:02:58Z. No new census, random test, formal build or Wolfram run. **Local's exact next stage-2 step:** implement the finite two-run lemma with both occurrence pairs, then the two-fibre cardinal inequality; keep finite-support/clock assumptions in the separate BL-to-free-word bridge. Return those carrying sources for GPT's read. Near-square side claims and parked research remain excluded.


Kit03a19bf6 source SHA256:

```text
ShiftOrbit.lean c6f4bc52323c83df867d8628739c2643344332e5bcc76fbb4e91036e157fefd2
WordsAutomata.lean b65826036813b71d23b8c70f525bf80ef40060e660333dd3e69af0bf3703d31c
```
