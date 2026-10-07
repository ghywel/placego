# Rudin–Shapiro passes the necessary repeat-debt filter

*The waiting room (not yet verified). Derived from [PROOFS.md](../PROOFS.md), entry "G153. Rudin–Shapiro passes the
necessary repeat-debt filter (2026-10-07; computer-assisted candidate)"; rebuild with `python3 proofs/build.py`.
Edit the proof in PROOFS.md and this summary in [summaries.md](summaries.md), never this file.*

**Status:** in the waiting room: stated with a proof, not yet checked by a second reader.

## In plain words

An exact automaton calculation says the Rudin–Shapiro word passes every necessary repeat-debt inequality with allowance zero. A separate graph-product check agrees; review of the encoded predicate and certificate is pending. The result would close that exclusion shortcut for this word, while leaving its forced wall tail unresolved. No finite compatible row has been constructed.

## The formal statement and proof

**Status.** Exact automaton candidate, independent semantic/certificate review pending. RSP preregistration was pushed at dd61eb5 before runs. No finite-left realization or prize claim. The raw universal decision is TRUE and an independently implemented graph-product check agrees, conditional on the compiled repeat predicate's semantics. The standard automatic-sequence logical decision theorem is the prior-art method, not a new technique.

Let r(n) be the parity of overlapping occurrences of11 in the binary representation of n, r(0)=0. Proposed statement: for every a,b>=0 and q>=1, if r(s)=r(s+q) for all a<=s<=b with b>=a, then

    b <= 2*a+q.

Thus Safe(0) and Bounded in the RSP plan hold. This is a necessary-filter pass, not a candidate construction. RSP2 was not run because a verified Safe(0) would already settle Bounded positively.

**Certificate chain.** The four-state output automaton remembers the last binary digit h and the parity e. Reading d updates (h,e) to (d,e XOR h*d); induction on digits proves the definition of r, including leading-zero padding. Pinned Walnut7.1.0 source commit67e69c248d07324b25de1d4a498e877ac504999a compiled the exact RSP predicate

    q>=1 AND b>=a AND FOR ALL s:
        (a<=s AND s<=b) IMPLIES r(s)=r(s+q)

into a deterministic78-state automaton over synchronized most-significant binary digits of (a,b,q). Its exported file SHA256 is1a0f3ac7b9222da522c2077b1dbeccb8098bc9df15a1200af6920a2243f309b6. Review artifacts rsp-repeat-dd61eb5.txt and rsp-product-dd61eb5.json are in the shared scratch; bulk outputs stay outside Git. The formula, driver and replay verifier are in tests/probes/prizes/rudin_shapiro_repeat.py.

The independent checker intersects that exported relation with a separately derived debt comparator. After a digit triple, the signed prefix debt d=b-2a-q updates to 2*d+b_bit-2*a_bit-q_bit. Values at most-1 stay negative under all later digits; values at least3 stay positive. Saturation to the five states -1,0,1,2,3 is therefore exact, with final d>0 accepting. Breadth-first traversal of the product has84 reachable states and no accepting state. Closed reachability proves emptiness for all finite digit strings, not a finite integer horizon. This check does not independently prove the compiled relation's semantics; review of that compiler/encoding remains the explicit dependency. Walnut's separately compiled universal formula also returned TRUE.

**Controls and failures.** RSP0 passes: the supplied generator versus the integer bit-count formula at0..4095 and189 selected64-bit carry-boundary inputs;2040 admissible literal repeats through a,b<=15 and q<=15; constant-zero and alternating Bounded=FALSE controls; and G137's powers-of-two Safe(0)=TRUE control. An expanded4096-tuple replay includes q=0 and reversed ranges and checks three additional leading zeros. The debt comparator matches32768 independent integer comparisons through31. These finite controls check instruments, not the universal theorem. The identified unexpected padding check is supplemented by the initial all-zero-digit self-loop and unbounded finite-graph traversal; no fixed bit width is used.

The first RSP0 run failed because Walnut resolves command filenames inside its command directory; the absolute positional filename was invalid. That failed run is retained, lookup corrected, and RSP0 completed before RSP1. Python's toolchain metadata request also failed its certificate-store check; system curl succeeded without disabling TLS. A checksum-verified portable Java archive and isolated tool/dependency caches were used, with no system-runtime installation. Formula processes had120 CPU-second limits,768MiB Java heap bounds,1GiB sampled-RSS termination checks and an additional180-second wall limit. No limit was approached: successful formulas took about0.42 seconds wall each, with sampled peak RSS below50MiB. Resource samples are not exact peak-memory measurements. No Local computational job was duplicated.

**Scope and next obligation.** After independent review, the ordinary repeat-filter exclusion route is closed for this specific automatic word. Its forced initial tail and full right extension remain unresolved. Passing this necessary inequality is neither finite evidence for support nor a theorem that a compatible finite row exists.
