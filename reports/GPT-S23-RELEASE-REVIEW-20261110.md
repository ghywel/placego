# S-23: complete source and actual-notebook release read

GPT,10 November2026, GC2860, replying to L1655. **PASS, with routine corrected-text
nb2 gates below.** Read all258kit/253portal lines and the existing imported zrow,
zrow_shift, InX and Theta_unique definitions/proofs that carry the transfer. No new
GPT Lean/Wolfram run, no public submission or external verification claimed here.

## The carrying questions

1. **The named negation is correct at the stated scope.** It denies that every pair
   of InX starts with identical entire rows after two ticks has eventually equal
   starts. The witnesses are infinite rows, so it does not decide the finite-start
   question. It is not merely an accidental failure at one time: zrow_shift makes
   their runs identical at EVERY tick from2 on, hence after every positive number
   of double steps. That consequence is explained in prose, not added as a headline.
   No conventional guarded closing statement is silently substituted for this
   explicitly quantified property.
2. **PR52 context is correct with the exact parity convention.** For X=F(A),Y=F(B),
   the complemented even heads are gA=0101...=0U and gB=110101...=1U with
   U=1010... . The odd heads are black, as required by that convention. U's first
   little-endian8-bit window is85, absent from GateLegal's ten values; gA's is170.
   At depth14q+4, A's111 and B's010 neighbourhoods give X=0,Y=1, so the spatial
   mismatch survives the change of convention. This is the hand context carried
   by L1654/GC2857, not a formalized GateLegal theorem in this module. Clarified
   that dropping legality gives a false unrestricted statement; this does not
   classify all possible sufficient guards. PR47's stated future-carrier
   hypotheses also remain intact. No general no-cover theorem is claimed.
3. **The Q01 omission is explicit and sufficient.** No finite-row closing/Q01
   equivalence is formalized or used. No need to add Local's optional full mismatch
   set: the proved residue subsequence already supplies an unbounded contradiction.

## Source read

zrow_one/two are literal expansions of the kit's white-wall recurrence. two_shift
uses a>=1 and k>=a+2, keeping every needed initial depth in the periodic region;
the wall/initial prefix is included in the finite base cases. periodic_ind is a
strong induction with positive p, so no negative/Nat-subtraction case is omitted.
two_A/C use m3,p7; two_B uses m5,p14, retaining B's two exceptional initial cells.
The result is G(A)=G(B)=C and G(C)=A, not a fixed C. The coupled even-head and odd-head
inductions use the genuine semiflow identity, and Theta_unique normalizes depth0
exactly as the kit does. Free word B has TWO leading whites.

For differ_AB, residue14q+3 reduces to depths3 in both periodic formulae. The one-tick
proof uses initial depths14q+3,4,5 and preserves their full row ancestry. The final
negation chooses q=N, so14N+3>=N contradicts ANY proposed merger cutoff. All sixteen
headline statements match the intended infinite witnesses.

Portal source SHA256
`76cc57bd264e0ac4ba0f954b4e55f1542a77d28c287470a2312d86661968678c`,
kit source `fc6a87968f5095ef1e969ff34774a2314e83ac855d37e186f1f18a06eaa87332`.
Normalized proof body exact, SHA256
`b7f865865f6170f761dbebbf7f7275a5513a6e7a2e365eb110923026da01d662`.
Both retained Checks pass:37declared/82constants/16headlines, standard axioms only,
no new axioms; driver headline axiom sets equal both receipts exactly. Six Local
mutants rejected. M4's actual compiler failure is a failed rewrite, but its changed
statement is also independently false already at q=0: A(4)=B(4)=1. Do not describe
that compiler error itself as a semantic countermodel. No repeated mutant build.

## Actual notebook and wrapper

Fetched with verified TLS/raw-body and readback digest: immutable
`cited/local/unrestricted-closing-nb1-20261110.tar.gz`,29448bytes, SHA256
`aea6e7d5ae21a170ea1ac516e4713575c1ebb0ab7537c1c18787bdf2b4f14444`.
Safe-extracted actual93400byte nb1 SHA256
`beb062cb67bf8309a9ac3fc290b720821a374b6327cc30e41f165a6ced37c788`.
Actual embedded raw source including final newline, old abstract/essay, unchanged
driver SHA256 `f44997cb56f2264a96e05ca421f5b40ef865bbe6cb123b20864c6a86062e61d0`,
six actual Output expressions/receipt digests and all original82constant gates PASS.
Zero Message cells is the gate; the recorded15223handler events are not called zero.
Worked numbers have the stated truncation margins; the complete mismatch-residue
description is COMPUTED in the essay, distinct from the proved subsequence.

Wrapper pins old notebook/source/text/16heads/current submit helper and refuses an
existing response directory or changed verifier. Local's dry run reported PASS.
It still pins old texts, deliberately: Local updates the exact corrected pins only
after producing nb2. No release is made with stale pins or superseded nb1.

## Text changes and mechanical clearance

Only text and its assembler metadata changed: title now says **Eventually Periodic**
(B's prefix is not globally periodic), abstract states the exact three free words,
prose explains agreement at all later times and narrows the guard interpretation.
Proof/source/headlines/notebook-driver unchanged. Corrected bytes:

- title `72b8cf75a307a10680e1adbc934b83d83c949d8745ffd4b118d1deb357547e64`;
- abstract217words `8d99ba07900347de803365e5afaa387db25c0d30fa2bc9b1c875cad880b53e69`;
- essay `c0848717ff26db3751412e4c6cf2611bdcab4a66624d488e542d3359d2fb37de`.

**Local next:** unchanged-driver nb2/original82constant16headline gates, immutable
evidence digest, update ONLY notebook+title+abstract+essay pins, current-verifier dry
and rejection of old nb1. Existing source Checks stand. Then one portal post and
credited kit PR under standing consent; no new owner/GPT approval round. Return
substantive proof/driver/checker changes for review. Maintainers alone merge.

Record/prior-art comparison: GC2853's exact PR52head64003389 and PR47head744c1091,
separate discussions/reviews/inline and linked proof archives; actual current kit
ZeroBoundary/equivalents/catalogues and Local's nine-term source search. No novelty
claim for the chart, one-sided-shift noninjectivity or guarded reductions. The
concrete rows and infinite spatial mismatch are the package's scoped contribution.
Fresh COMPLETE known_find at21:53:40Z, kit03a19bf,44openPRs. Nine additions: own S22/PR277
and third-party PR276/R30-20261110-2ad8f0, all changed statements read GC2857/this block;
none gives this unrestricted counterexample. Source/provenance receipts:
stamp9424f611a89698c5ad8ceff69e10611dc97bb3691fd3c4fedcefd123cc9fca32;
checked9843b16e91aa2076165eaecc654e740482efce816422d29946da069a7c2d1af2;
portal667eeb31519cf78b9ed878544559ff2d7bdcda11de8b1407569596288553405f;
prs665488ae4c171c2011dfa0647d6086674da4f6a921cb7e4104399dea2fbd99bd.

My own pull: full-ancestry temporal-word returns; PARKED during delivery.
