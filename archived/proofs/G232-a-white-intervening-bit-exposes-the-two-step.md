# a white intervening bit exposes the two-step correction

*GPT's proofs, second-read. Derived from [PROOFS.md](../PROOFS.md), entry "G.GPT232. a white intervening bit exposes
the two-step correction (second-read by Local, 2026-10-08)"; rebuild with `python3 proofs/build.py`. Edit the proof
in PROOFS.md and this summary in [summaries.md](summaries.md), never this file.*

**Status:** proved by GPT and second-read by Local.

## In plain words

A two-step readout has one precisely identified nonlinear correction.

**What it says.** With a white intervening bit, the central bit two updates later is the XOR of two original bits and their farther adjacent product. If that product vanishes, the readout is additive. G231 supplies the needed premises for the stated clock family.

**Why it matters.** It expresses even column5 as the discrepancy between the next column3 bit and the prescribed effective input. It does not assume that discrepancy vanishes.

**An everyday picture.** Two signals add cleanly unless a particular pair activates a correction. Identifying that pair tells us exactly which extra condition makes the simpler readout valid.

## The formal statement and proof

**Where:** RULE30-GPT.md GC459 atc3f0265; Local L270 at e4f4ff9 verifies the universal two-case identity and its G231 application, reaffirmed L272 at572eb5e. Source proof and application copied verbatim below. The source's pending GC458 premise is now the reviewed G231, so its clock application is unconditional in that stated family. The translated embedding control restates locality and is not independent evidence about a boundary.

**Proof of the local identity.** Write the five consecutive inputs as (s,0,q,h,z). Their three intermediate bits are c=s XOR q, r=(1-q)*h, v=q XOR ((1-h)*z). The final central bit is Q=c XOR ((1-r)*v). If h=1 then r=1-q,v=q, so (1-r)*v=q and Q=s. If h=0 then r=0,v=q XOR z, so Q=s XOR z. In both cases Q=s XOR ((1-h)*z). This holds for every q and imposes no wall value. Equivalently Q=s XOR z XOR (h*z); the exact defect from the additive readout is the adjacent nonlinear product h*z. This is a universal local identity under the stated white intervening input, not a finite-sample inference.

**Conditional clock application.** If GC458 is verified, every x_(2n)(2)=0 in the empty-left full0101 family, and every V_(2n)(4)=0, including time0 via G229. Apply the identity at j=1,t=2n to obtain

`x_(2n+2)(3)=s_n XOR x_(2n)(5)` for every n>=0.

Thus the even column5 bit is exactly the discrepancy between the next even column3 bit and the prescribed effective input s_n. It is not an independently free bit once that column3 temporal track is specified. This does not force the discrepancy to vanish, determine column3, or discard column5 products. At n=0, G229 fixes s_0=x_0(5)=1, hence the formula yields x_2(3)=0, agreeing with the known prefix. No extension of that prefix is assumed.


**Duplicate guard for G232:** actual nearest G230,G231,G228 read in full. Their bit gates and predecessor-based product removals are inputs here; this entry instead computes an individual two-step bit and its exact nonlinear correction. Initial notation s_0=x_0(1)=1 and x_0(5)=1 refers to two separate prefix facts.

**Scope:** the local identity requires only the white intervening input. Dropping the nonlinear product requires the separate product-zero premise; the clock readout uses G231 and the empty-left full0101 family. No farther bit is thereby forced white.
