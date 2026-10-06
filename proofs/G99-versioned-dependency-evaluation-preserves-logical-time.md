# versioned dependency evaluation preserves logical time

*GPT's proofs, second-read by Local. Derived from [PROOFS.md](../PROOFS.md), entry "G.GPT99. versioned dependency
evaluation preserves logical time (second-read by Local, 2026-10-06)"; rebuild with `python3 proofs/build.py`. Edit
the proof in PROOFS.md and this summary in [summaries.md](summaries.md), never this file.*

**Status:** proved by GPT and second-read by Local.

## In plain words

A shared logical generation can survive unequal physical update times.

**What it says.** Store immutable values labelled by site and generation. Any complete schedule that computes a node only after its three prior-generation parents gives the synchronous history's values. An intermediate mixture of generations is not necessarily a synchronous frame.

**Why it matters.** It identifies the buffering and dependency assumptions needed to answer the owner's local-clock question. It claims neither a physical metric nor an algorithmic speedup. Independent review and small controls remain pending.

**An everyday picture.** Cooks can prepare different ingredients at different times, provided each recipe uses the specified versions and the finished dish includes every required ingredient.

## The formal statement and proof

### G99. Versioned dependency evaluation preserves logical time (2026-10-06)

**Status:** elementary finite-dependency proof; independent review and controls pending. Follow-up to G98, Local L052 and CONSTELLATION row19. The asynchronous-simulation prior art in PRIOR-ART.md uses additional state; this is a direct scheduling statement, not a new simulator or universality result.

**Proposition.** To compute x_N(0), keep immutable values indexed by (i,k) for 0<=k<=N and |i|<=N-k. Initially store x_0(i) for -N<=i<=N. A noninitial node (i,k) becomes ready only when its three parents (i-1,k-1), (i,k-1), (i+1,k-1) are stored. Evaluate it using the original local rule. Every schedule that eventually evaluates all these nodes and only evaluates ready nodes produces exactly the synchronous values, whatever the physical delays or order of independent ready nodes.

**Proof.** All parents of a node lie in the stated triangle. Generation0 is identical to the original data. By induction on k, every parent of a generation-k node has its synchronous value, so evaluating the deterministic rule produces x_k(i). This holds whenever that node is evaluated, independently of intervening work elsewhere. The finite graph is acyclic because each dependency lowers k; every complete topological order is therefore valid. Unbounded physical delays or lack of eventual completion are excluded explicitly.

There are (N+1)² stored nodes in this full cone, including initial nodes, and a longest chain of N update nodes. Those are costs/depths of this explicit one-step dependency graph, not lower bounds against every algorithm for the centre bit. Generation labels are logical time. The theorem supplies no physical time dilation, uniform physical signal speed, memory-optimal implementation or sublinear prize algorithm.

**Unexpected mixed-generation guard.** Start with a black cell at1. After computing only node(0,1), project the latest stored value at each site while retaining generation0 elsewhere. This projection has black set {0,1}, whereas the complete synchronous generation1 has {0,1,2}. Thus correct individual versioned nodes do not make an arbitrary mixed-generation projection a synchronous frame. An observable must specify its logical generation; buffering and labels are part of the assumptions, not optional bookkeeping. G98's raw in-place order guard separately shows what can go wrong if the parents are overwritten or read from the wrong generation.

**VP1 preregistered NOT RUN.** For N1..4 and every initial word on [-N,N], compare two complete ready-node schedules (increasing generation/site order and a ready-node schedule prioritizing the largest site) with a separately computed synchronous truth-table triangle. Require all stored node values and the centre output to agree. Retain the mixed-generation guard above; the unrestricted claim that every intermediate projection is a synchronous frame must fail. No asynchronous random-cell profile, Local job or speed benchmark. Publish the instrument and predictions before execution.

*Second reader's note on G99 (Local, 2026-10-06; chat L055).* Correct, and rightly labelled a scope restatement of
known scheduling (Nakamura's construction is the bounded-state local version). Checked
(`rule30_audit_g99_g100.py`, S1): for $N \le 5$ and every initial word, three different ready orders (by generation,
largest site first, seeded random) give every node its synchronous value; the mixed-generation projection is
$\{0, 1\}$ against the synchronous $\{0, 1, 2\}$. Its point for the owner's question stands: what an observer reads
must name its logical generation.
