# bounded nonlinear activation gaps for finite Rule210 walls

*GPT's proofs, second-read. Derived from [PROOFS.md](../PROOFS.md), entry "G.GPT214. bounded nonlinear activation
gaps for finite Rule210 walls (second-read by Local, 2026-10-08)"; rebuild with `python3 proofs/build.py`. Edit the
proof in PROOFS.md and this summary in [summaries.md](summaries.md), never this file.*

**Status:** proved by GPT and second-read by Local.

## In plain words

A finite Rule210 row cannot keep a nonzero periodic centre while its nonlinear gates remain silent for too long.

**What it says.** With initial support bounded by R and centre period p, every time s after periodicity begins has a nonlinear activation by time3*s+2*R+3*p.

**Why it matters.** It quantifies the earlier requirement of arbitrarily late nonlinear events. The proof separates two shifted linear copies at a dyadic time, forcing a full period of centre zeros if no gate fires. It does not locate the gate or exclude a finite witness.

**An everyday picture.** Two expanding copies eventually leave a gap at a watched point. A repeating signal there needs another contribution before that gap lasts an entire period.

## The formal statement and proof

**Where:** RULE30-GPT.md GC419 at23fefb3; statement and proof copied verbatim below. Local L251 verified in a405d0a checks the rule split, finite propagation, dyadic identity, centre separation, update endpoint and infinite-support guard. This quantitatively sharpens G59; finite right compatibility remains open.

This quantifies G59, rather than closing finite global compatibility. Suppose a full Rule210 initial row has support in[-R,R], R>=0, and its centre wall is eventually p-periodic and nonzero, with p>=1 and onset a. For every integer s>=a, some nonlinear source V_t(i)=x_t(i)*x_t(i+1) is nonzero at an update time t in[s,3*s+2*R+3*p]. The site i is unrestricted. Here nonzero periodic means its repeating word contains a1.

**Proof.** Write A=S+S^-1 over GF(2); the full update is x_(t+1)=A*x_t+V_t. Finite propagation puts x_s inside[-R-s,R+s]. Choose N as the least power of2 at least R+s+p. Then N>R+s+p-1. Suppose V_t vanishes identically for all updates t=s,...,s+N+p-2. Evolution on that interval is exactly linear, hence x_(s+N+j)=A^(N+j)*x_s for j=0,...,p-1. The dyadic identity A^N=S^N+S^-N separates two translates of A^j*x_s. That row is supported inside[-R-s-j,R+s+j], and N>R+s+j. Its two translates therefore both vanish at the centre. Thus the wall has p consecutive zeros at times s+N,...,s+N+p-1, all after onset a, contradicting the nonzero p-periodic wall. Some source must be active during[s,s+N+p-2]. Since N<2*(R+s+p), the stated coarser endpoint3*s+2*R+3*p contains this interval. This proves the claim.

**Scope:**672 bounded linear subset controls agree with the hand implication, not an enumeration of full periodic witnesses. The event site is unrestricted. No positive-density, finite-witness exclusion or Rule30 consequence.

**Duplicate guard for G214:** actual nearest G59,G212,G60 read in full. G59 is the source qualitative obstruction; G214 adds an explicit gap endpoint from the time-s propagation radius. G60 constructs infinite linear right realizations and G212 bounds fair-input information; neither states this quantitative finite-row necessity. No new general operator identity claimed.
