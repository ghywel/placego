# the Sturmian exclusion survives every finite block factor

*GPT's proofs, second-read by Local. Derived from [PROOFS.md](../PROOFS.md), entry "G.GPT131. the Sturmian exclusion
survives every finite block factor (second-read by Local, 2026-10-06)"; rebuild with `python3 proofs/build.py`. Edit
the proof in PROOFS.md and this summary in [summaries.md](summaries.md), never this file.*

**Status:** proved by GPT and second-read by Local.

## In plain words

Finite recoding preserves the repetitions that exclude a Sturmian companion.

**What it says.** Any fixed finite block function of a Sturmian sequence is excluded beside the alternating wall with finite left support. This includes rotation codes on several arcs when all endpoints belong to one rotation orbit, for every phase and every irrational angle.

**Why it matters.** The earlier theorem transfers with a fixed repetition margin; no new numerical evidence or assumption of an invertible code is needed. Unrelated endpoint orbits and general aperiodic companions remain open.

**An everyday picture.** Reading a fixed group of neighboring symbols cannot erase a long repeated stretch except at its ends.

## The formal statement and proof

### G131. The Sturmian exclusion survives every finite block factor (2026-10-06)

**Status and purpose.** Symbolic extension of RULE30-PRIZE.md section 8.57's Theorem E; independent review pending. No experiment. The target is the open rotation-code lead in PERIOD-TWO.md question 7, without assuming a periodic companion. The counterfactual is that a finite recoding can remove the early repetitions responsible for Theorem E. The proof retains the exact fixed margin. Prior art: finite block coding and orbit-endpoint rotation partitions are standard; the abstract of Kupsa and Starosta, [On the partitions with Sturmian-like refinements (2015)](https://www.aimsciences.org/article/doi/10.3934/dcds.2015.35.3483), discusses this class and stronger refinement results. Only the abstract was read; no refinement or injectivity theorem is imported. The result below is a corollary of the project's existing repeat obstruction, not a novelty claim about Sturmian coding.

**Theorem.** Let g be any irrational Sturmian sequence, with any phase. Let F be any binary function of a fixed block of width w+1, and set c_s=F(g_s,...,g_(s+w)) for s>=0. If c is column 1's visible sequence beside the alternating Rule 30 wall 0101..., the forced initial left row cannot be eventually zero. No injectivity, nonconstancy or aperiodicity premise is imposed on F.

**Proof.** Section 8.57 Step 0 says finite left support would supply a fixed constant C>=0 such that every repetition c_s=c_(s+q) on a<=s<=b, q>=1, obeys

    b <= 2a+q+C.                         (repeat bound)

Enlarging a possibly negative original C only weakens this necessary bound. Suppose g_s=g_(s+q) on a<=s<=e. If e>=a+w, then c repeats on a<=s<=e-w, so e<=2a+q+C+w. If e<a+w, the same inequality holds automatically. Thus finite left support for c would make every repetition of g obey the repeat bound with constant C+w. The continued-fraction argument in section 8.57 Steps 1 to 4 proves that no irrational Sturmian sequence, at any phase, can obey that bound with any fixed constant. Its proof uses only the repeat bound after Step 0, so it applies here unchanged. This contradiction proves the theorem. The margin is w, not a scale-dependent loss.

A finite block function using shifts m,...,M of a bi-infinite mechanical word is also covered: rephase the Sturmian input by m and take w=M-m. Likewise an eventual finite-block coding is excluded once the clock and coding have both begun: restart at an even physical time beyond that prefix. Finite initial left support remains finite at that time by the light cone.

**Corollary: every finite union of arcs with endpoints on one rotation orbit.** Let 0<alpha<1 be irrational, let f be a binary, right-continuous step function on the circle, and suppose its actual jump endpoints all have the form beta+k_j*alpha modulo one, with finitely many integer k_j. Then c_s=f(theta+s*alpha) is excluded beside 0101... for every theta and every alpha, including bounded-partial-quotient angles. This covers multiple arcs, not just the original interval of length alpha.

Here is a direct finite-block construction, with exact endpoint conventions. Put y=x-beta and g(y)=1 on [1-alpha,1), zero elsewhere. A binary circular step function has an even number of jump endpoints. Over GF(2), form the Laurent polynomial

    Q(z)=sum_j z^(k_j)=(1+z)*P(z).

The divisibility follows from Q(1)=0 after multiplication by a power of z to clear negative exponents. For each nonzero coefficient P_k define

    h(y)= XOR_k g(y-(k+1)*alpha).

The k-th term jumps at k*alpha and (k+1)*alpha, so the jump set of h is precisely Q: interior endpoints cancel modulo two. Thus f(beta+y) and h(y) have the same jumps and differ by one constant bit. Right-continuity makes the equality hold at the endpoints as well. Along the orbit this is a finite XOR block code of one rephased Sturmian word, plus that constant. The theorem therefore applies. A constant f is the empty-code case and is covered too.

**Unexpected degeneracy check.** With irrational 0<alpha<1/2, the standard Sturmian word has no adjacent ones: rotating its one interval [1-alpha,1) by alpha lands in [0,alpha), where the next bit is zero. Hence the finite block factor F(u,v)=u AND v is constantly zero, not Sturmian. The proof still excludes it, directly through the repeat bound. Therefore the argument must use inherited repetitions rather than assert that a finite factor stays Sturmian or invertible. This is the identified independent check.

**Scope and lead status.** The one-orbit-endpoint subclass of question 7 is now covered for all phases and all irrational angles, conditional only on the already proved Theorem E repeat argument. Endpoints on unrelated rotation orbits with bounded partial quotients remain open; a finite recoding of several differently phased Sturmian words does not guarantee a common long repeat. Torus rotations, kicked codes and general aperiodic companions remain outside this result. It is a class exclusion for the finite-left problem, not the prize's exclusion of every companion.

*Second reader's note on G131 (Local, 2026-10-06; chat L085).* Correct. A repetition of $g$ on $[a, e]$ gives one of
the block code on $[a, e - w]$, so Step 0's bound passes to $g$ with constant $C + w$; and Theorem E's Steps 1 to 4
(RULE30-PRIZE.md §8.57) apply that bound only to stretches where the Sturmian word itself repeats with period $q_n$,
so they run unchanged on $g$. The corollary's construction is right: an even number of endpoints gives $Q(1) = 0$, and
each $g(y - (k+1)\alpha)$ codes $[k\alpha, (k+1)\alpha)$, so the XOR has exactly $Q$'s jumps. Checked
(`rule30_audit_g99_g100.py`, S29): for 40 random one-orbit arc unions at two irrational angles, $f(\beta + y) \oplus h(y)$ is constant along 20,000 orbit points; for $\alpha < 1/2$ the Sturmian word has no adjacent ones; block codes
inherit repetitions as stated. This closes the one-orbit part of PERIOD-TWO question 7 for every angle; arcs with
unrelated endpoints and small partial quotients remain open, as G131 says.
