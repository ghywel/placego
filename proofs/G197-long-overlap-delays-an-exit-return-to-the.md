# long overlap delays an exit return to the original circuit

*GPT's proofs, second-read by Local. Derived from [PROOFS.md](../PROOFS.md), entry "G.GPT197. long overlap delays an
exit return to the original circuit (second-read by Local, 2026-10-07)"; rebuild with `python3 proofs/build.py`.
Edit the proof in PROOFS.md and this summary in [summaries.md](summaries.md), never this file.*

**Status:** proved by GPT and second-read by Local.

## In plain words

A stripe that leaves the known loop cannot rejoin it quickly.

**What it says.** While the first changed tick is still inside the window, the unchanged part keeps recording the
old phase, so the window cannot match the old loop whatever follows. For the known exits at period 16, that means at
least 26,396 steps before any rejoining.

**Why it matters.** It shows that a short search for a way back cannot succeed here. It does not show that a way
back, or any legal continuation, exists.

**An everyday picture.** A typo in the scrolling news ticker at the bottom of a television screen stays in view
until enough text has scrolled past.

## The formal statement and proof

### GPT G197 — Long overlap delays an exit's return to the original circuit (2026-10-07; second reader pending)

**Statement and scope.** Let w have least dyadic period q>=2, let m>=q, and let the paired circuit consist of the m-bit windows of w at phases t and t+h, h=q/2, as in G190/G195. Suppose its first alternative edge flips both appended bits. Let L be a phase-identifying length: the q length-L cyclic blocks of w are distinct. Along ANY subsequent shift-and-append continuation, a return to any vertex of the original ordered or unordered circuit requires at least

    ell >= m-L+1

edges counted from the source before that first flipped edge. A phase-identifying length L<=q-1 always exists for a primitive binary word. Separately, along any continuation from the original paired source, the equal-tail pattern of G195 cannot occur before ell>=m-h. These are necessary latency bounds, not an assertion that a continuation is legal or ever returns.

**Prediction and counterfactual for hand controls.** The untouched prefix should fix the old phase until the first flipped bit has approached the start of the window. The counterfactual that a short continuation can rejoin the rooted q16 circuit will fail through 26395 edges. An unexpected equal-weight check should improve the generic q-bit phase anchor to q-1 bits. No trajectory computation or graph search runs here.

**Return bound.** Set the exit source's first window at phase0. After ell edges, 1<=ell<=m, the first window starts with the untouched block w(ell)..w(m-1), of length m-ell. Immediately after that prefix is the first injected bit w(m)+1, still retained. If ell<=m-L, the first L untouched bits identify phase ell uniquely among all q phases. Equality with any original first window would thus require precisely that phase. But the injected bit disagrees with its expected bit w(m). This is impossible. Matching an unordered pair does not avoid the argument: its first window must equal one of the original windows, and both orientations already occur among the q phases. The same argument applies at any exit phase by rotation. Later appended bits were arbitrary throughout the proof.

**The q-1 anchor.** Distinct rotations of a binary word have equal total weight. If their first q-1 bits agree, their final bits must also agree to preserve that weight. Their full q-blocks therefore agree; least period q makes their phases identical. Hence length q-1 identifies every phase. This is a word fact, not a special property of the return graph.

**Equal-tail bound.** Before ell>=m, the tails of the two current windows still contain the untouched paired differences beta(ell+1)..beta(m-1), a block of length m-ell-1. By G195, beta(t)=w(t)+w(t+h) is nonzero and h-periodic on this dyadic circuit. If m-ell-1>=h, those tails cannot be equal, since a full h-block of zeros would force beta identically zero. Thus equal tails require ell>=m-h. This applies even without a first flipped edge. It does not exclude general unequal-tail branching from G196.

**Actual hand control: the PR196-D1 rooted word.** Local's verified word is w=1000101001100001, q16, m26403. Its cyclic length-eight blocks at phases0..15 are

    10001010 00010100 00101001 01010011
    10100110 01001100 10011000 00110000
    01100001 11000011 10000110 00001100
    00011000 00110001 01100010 11000101.

They are all distinct. Phases7 and13 have the same seven-bit prefix0011000, so the smallest phase-identifying length is exactly8. The return bound is therefore ell>=26403-8+1=26396. The parallel-edge source requires ell>=26403-8=26395. These apply to both D1 exit decisions by rotation; they establish no path of those lengths.

**Independent word-only boundary control and identified unexpected weight guard.** For w=0001, phases0 and1 share the first two bits00, so q-2 bits do not identify phases, whereas q-1 bits do; the weight argument's universal length cannot be lowered. For w=01, m3, the initial pair(010,101), flipped first target(100,011), then targets(001,110) and(010,101) return after exactly3 edges. Here L1, so m-L+1=3 is attained. These arbitrary append paths are NOT asserted to lie in any Rule30 return graph. They check the counting convention, retention of the injected bit and the strict boundary in the bound.

**Record and limits.** This extends G195's original-circuit overlap argument to arbitrary continuations, using standard cyclic-word phase identification and no external novelty claim. It does not classify the rooted strongly connected component. D1's legal exits refute outgoing isolation; the component itself can still be the original sixteen-cycle if no exit returns. A short detour search cannot establish a return here. Local: audit the untouched-prefix indexing, eight-block table and both word-only guards; no continuation job is requested. General recurrence and normalized stage growth remain open.

*Second reader's note on G197 (Local, 2026-10-07; chat L166).* Correct. After $\ell$ edges the first window begins with
the untouched block $w(\ell), \dots, w(m-1)$ and then the flipped bit $w(m) + 1$. If $m - \ell \ge L$, that block fixes
the phase as $\ell$, and the flipped bit contradicts it; both orientations of an unordered pair occur among the $q$
phases, so the pair gives no escape. Equal weight of rotations makes $q - 1$ bits enough. The paired tails keep
$\beta(\ell + 1), \dots, \beta(m - 1)$ untouched, so a full $h$-block of zeros, which G195 forbids, would be needed
before $\ell \ge m - h$. Checked (`rule30_audit_g99_g100.py`, S94). Every primitive word of length up to 12 is
phase-identified by $q - 1$ bits, and 0001 needs exactly 3. By brute force over every continuation, on five small
primitive words with $m = q$ to $q + 3$ and every exit phase, no first window returns before $m - L + 1$ edges. On three
complementary dyadic words, no paired continuation reaches equal tails before $m - h$. GPT's $w = 01$, $m = 3$ path
returns in exactly 3 edges, attaining the bound. The PR196-D1 word's sixteen 8-bit blocks match GPT's table and are
distinct, phases 7 and 13 share 0011000, and so $L = 8$, giving the bounds 26,396 and 26,395.
