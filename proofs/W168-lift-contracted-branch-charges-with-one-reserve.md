# lift contracted branch charges with one reserve

*The waiting room (not yet verified). Derived from [PROOFS.md](../PROOFS.md), entry "GPT G168 — lift contracted
branch charges with one reserve (RULE30-GPT.md G168; awaiting second reader, 2026-10-07)"; rebuild with `python3
proofs/build.py`. Edit the proof in PROOFS.md and this summary in [summaries.md](summaries.md), never this file.*

**Status:** in the waiting room: stated with a proof, not yet checked by a second reader.

## In plain words

A bound for complete blocks can cover their interior steps with one shared reserve.

**What it says.** If a timing budget covers ordinary edges and complete branch blocks, adding a fixed reserve at block boundaries lets that budget extend to every interior edge. The reserve depends on the size of one block's possible excursion, not on the number of blocks.

**Why it matters.** It gives the missing transfer from complete-block payments to arbitrary intervals, while keeping the unproved boundary budget explicit.

**An everyday picture.** A reusable cash buffer covers the temporary expense before each rebate; it need not grow each time another receipt is processed.

## The formal statement and proof

**Conditional finite-history statement; review requested.** Fix one finite gated periodic history and disjoint four-edge branch blocks from G167, all at common period q. Keep every other edge unchanged and replace each complete branch block by one edge between its actual endpoints, with reward equal to the sum of its four original rewards. These contracted edges represent actual blocks; the compressed sequence is not asserted to be a new Rule30 history. Suppose a nonnegative potential K on the retained vertices satisfies every contracted edge inequality, with original doubled slope5/2 rewards.

Let A bound the positive reward of every prefix starting at a branch block's first vertex, allowing an empty prefix. Let B bound the positive reward of every contiguous subinterval inside any one block. Both are nonnegative and uniform across the blocks. Then K lifts to a nonnegative potential h on every original vertex, satisfying every original edge inequality, with

    max h <= max K+A+B.

Thus the interior cost is one reserve for the whole fixed-period history, not A or B multiplied by the number of branches. This is conditional on a certificate K for all retained ordinary edges and complete blocks; no such uniform certificate is supplied here.

**Proof.** Give every retained vertex h=K+A. Inside a block, define h backwards from that fixed endpoint by h(v)=max(0,w(v,u)+h(u)). This is possible on a finite block and verifies all its interior edge inequalities. Expanded at an internal vertex, h is the maximum of rewards from stopping at an interior vertex and the remaining-block reward plus the endpoint's K+A. The first terms are at most B and the last is at most B+max K+A. At the block's first vertex the backwards-required value is the maximum of prefix stopping rewards, at most A, and whole-block reward plus K(endpoint)+A, at most K(start)+A by the contracted inequality. Hence the assigned h at the first vertex also covers its first original edge. Ordinary edges retain their inequalities because the same A is added at both ends. Nonnegativity and the stated uniform upper bound follow. Adjacent blocks would also work if they share only a retained endpoint; G159's spacing guarantees disjoint blocks on the rooted histories under discussion. No new compatibility after contraction is assumed. Square.

**Exact G167 reserves.** Its fast block rewards are(-5,-3,-3,2ell-5); its slow block rewards are(-5,2ell-3,-3,2m-5). With ell+m<=q and ell,m>=1, G167 supplies A=max(0,2q-10). Every single positive edge is at most2q-5; every two-edge interval is smaller than this, and every three-edge interval is at most2q-11, while the four-edge reward is at most2q-16. Thus B=max(0,2q-5) suffices. The lifted overhead is at most4q-15 for q>=8 (and3 for q4), independent of the number of genuine branches. On the known q16 split's table, the sharper reserves A=2 and B=7 give overhead9 for those local blocks only. This is not a bound on later q16 branch blocks.

**Identified unexpected control and counterfactual.** The q8 slow pulse block has rewards(-5,11,-3,-3), total0. With K=0 at its two contracted endpoints, naive lifting with no reserve fails at the first endpoint because its two-edge prefix earns6. With A=6 the backwards construction gives original vertex values(6,11,0,3,6); every edge inequality holds and the zero stopping option is active at the middle vertex. The general bound max K+A+B=17 safely covers these values. Using a whole-block endpoint inequality alone would miss that middle stop; repeating the block does not require adding6 per repetition. This is exact arithmetic on the existing compatible block, with no new computation or root-membership claim.

**Scope and next obligation.** This is standard finite-path dynamic programming, already present in G8/G166, now applied to G167's actual branch blocks. It resolves how a contracted certificate would transfer to arbitrary subintervals without a per-branch reserve. It does not construct K, bound intervening nonbranch charges, solve the all-period cycle problem, or establish period growth. For multiple dyadic stages, any eventual O(q) certificate must still be stitched as in G165/G166. No prize conclusion or new run is claimed. Next reasoning target is K on the retained ordinary edges and genuine branch transitions, rather than accumulating a fresh allowance for each branch.
