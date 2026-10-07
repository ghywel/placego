# Rudin–Shapiro passes the necessary repeat-debt filter

*GPT's proofs, second-read by Local. Derived from [PROOFS.md](../PROOFS.md), entry "G.GPT153. Rudin–Shapiro passes
the necessary repeat-debt filter (second-read by Local, 2026-10-07)"; rebuild with `python3 proofs/build.py`. Edit
the proof in PROOFS.md and this summary in [summaries.md](summaries.md), never this file.*

**Status:** proved by GPT and second-read by Local.

## In plain words

The Rudin–Shapiro sequence passes the repeat test, by a computer-checked certificate.

**What it says.** The Rudin–Shapiro sequence colours each tick n by whether 11 appears an odd or even number of
times in n's binary digits, overlaps counted. An exact calculation with an automaton (a small machine that reads the
digits one at a time) says it passes every necessary repeat inequality with no allowance at all. A second
construction, built a different way, describes the same language, and Local's own code, sharing nothing with GPT's,
agrees with brute force.

**Why it matters.** It is another famous never-repeating pattern that the repeat test cannot exclude, so its
finiteness question stays open and needs a different kind of argument.

**An everyday picture.** Another impostor the filter lets through: the next checks must catch it, or show it is
genuine.

## The formal statement and proof

### G153. Rudin–Shapiro passes the necessary repeat-debt filter (2026-10-07; computer-assisted theorem)

**Status.** Computer-assisted theorem, independently verified by Local L111 at 8f7841c. The direct RSP-S semantic reconstruction and debt-product argument have been audited and independently replayed; the Walnut compilation dependency is discharged. RSP preregistration was pushed at dd61eb5 before runs. No finite-left realization or prize claim. The raw universal decision is TRUE and an independently implemented graph-product check agrees, conditional on the compiled repeat predicate's semantics. The standard automatic-sequence logical decision theorem is the prior-art method, not a new technique.

Let r(n) be the parity of overlapping occurrences of11 in the binary representation of n, r(0)=0. Proposed statement: for every a,b>=0 and q>=1, if r(s)=r(s+q) for all a<=s<=b with b>=a, then

    b <= 2*a+q.

Thus Safe(0) and Bounded in the RSP plan hold. This is a necessary-filter pass, not a candidate construction. RSP2 was not run because a verified Safe(0) would already settle Bounded positively.

**Certificate chain.** The four-state output automaton remembers the last binary digit h and the parity e. Reading d updates (h,e) to (d,e XOR h*d); induction on digits proves the definition of r, including leading-zero padding. Pinned Walnut7.1.0 source commit67e69c248d07324b25de1d4a498e877ac504999a compiled the exact RSP predicate

    q>=1 AND b>=a AND FOR ALL s:
        (a<=s AND s<=b) IMPLIES r(s)=r(s+q)

into a deterministic78-state automaton over synchronized most-significant binary digits of (a,b,q). Its exported file SHA256 is1a0f3ac7b9222da522c2077b1dbeccb8098bc9df15a1200af6920a2243f309b6. Review artifacts rsp-repeat-dd61eb5.txt and rsp-product-dd61eb5.json are in the shared scratch; bulk outputs stay outside Git. The formula, driver and replay verifier are in tests/probes/prizes/rudin_shapiro_repeat.py.

The independent checker intersects that exported relation with a separately derived debt comparator. After a digit triple, the signed prefix debt d=b-2a-q updates to 2*d+b_bit-2*a_bit-q_bit. Values at most-1 stay negative under all later digits; values at least3 stay positive. Saturation to the five states -1,0,1,2,3 is therefore exact, with final d>0 accepting. Breadth-first traversal of the product has84 reachable states and no accepting state. Closed reachability proves emptiness for all finite digit strings, not a finite integer horizon. This product check alone does not establish the compiled relation's semantics. The separate RSP-S reconstruction, audited and replayed by Local L111, discharges that dependency for this exported relation. Walnut's separately compiled universal formula also returned TRUE.

**Controls and failures.** RSP0 passes: the supplied generator versus the integer bit-count formula at0..4095 and189 selected64-bit carry-boundary inputs;2040 admissible literal repeats through a,b<=15 and q<=15; constant-zero and alternating Bounded=FALSE controls; and G137's powers-of-two Safe(0)=TRUE control. An expanded4096-tuple replay includes q=0 and reversed ranges and checks three additional leading zeros. The debt comparator matches32768 independent integer comparisons through31. These finite controls check instruments, not the universal theorem. The identified unexpected padding check is supplemented by the initial all-zero-digit self-loop and unbounded finite-graph traversal; no fixed bit width is used.

The first RSP0 run failed because Walnut resolves command filenames inside its command directory; the absolute positional filename was invalid. That failed run is retained, lookup corrected, and RSP0 completed before RSP1. Python's toolchain metadata request also failed its certificate-store check; system curl succeeded without disabling TLS. A checksum-verified portable Java archive and isolated tool/dependency caches were used, with no system-runtime installation. Formula processes had120 CPU-second limits,768MiB Java heap bounds,1GiB sampled-RSS termination checks and an additional180-second wall limit. No limit was approached: successful formulas took about0.42 seconds wall each, with sampled peak RSS below50MiB. Resource samples are not exact peak-memory measurements. No Local computational job was duplicated.

**Scope and next obligation.** After independent review, the ordinary repeat-filter exclusion route is closed for this specific automatic word. Its forced initial tail and full right extension remain unresolved. Passing this necessary inequality is neither finite evidence for support nor a theorem that a compatible finite row exists.

*Second reader's note on G153 (Local, 2026-10-07; chat L111).* Correct as a computer-assisted theorem, with the semantic
dependency on Walnut discharged. The definition, the inclusive endpoints and the quantifiers match the RSP plan and
G135's convention, and the first interval $[0, 1]$ at period 1 has debt exactly 0, so $C = 0$ is tight. I audited
RSP-S's three steps. The carry completion holds, since $s \le b$ fits the input width and $s + q$ needs at most one more
digit, so one implicit zero digit closes the carry and the last adjacent pair. The reversal holds: reversing the
exported automaton makes its accepting states the starts and its initial state the target, and a simultaneous subset
search that closes decides language equality for every nonempty input. The adjacent-11 parity is the same in either
reading direction. The saturated debt comparator is exact, since $2(-1) + 1 < 0$ and $2 \cdot 3 - 3 \ge 3$. Checked in
code sharing nothing with GPT's (`rudin_shapiro_review.py`). RV1: the exported relation agrees with brute force on all
$32^3$ triples at two paddings. RV2: my own debt product on it reaches 84 states and no violation. Reproduced on this
machine: RSP-S's equivalence closing at 17,033 states with the mutation caught at $(0, 0, 0)$, and G153's replay with 84
product states. Both GPT scripts need Python 3.10 or later for `int.bit_count`, and this machine's default is 3.9. My
first attempt, an independent most-significant-digit construction, was stopped at 3 GB while still determinising once
GC177 showed GPT had closed that lane; it is kept in the script's docstring. The scope stands as written: this closes
the repeat-filter route for this word at this start, and says nothing about its forced tail.
