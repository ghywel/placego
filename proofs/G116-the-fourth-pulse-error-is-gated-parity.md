# the fourth pulse error is gated parity

*GPT's proofs, second-read by Local. Derived from [PROOFS.md](../PROOFS.md), entry "G.GPT116. the fourth pulse error
is gated parity (second-read by Local, 2026-10-06)"; rebuild with `python3 proofs/build.py`. Edit the proof in
PROOFS.md and this summary in [summaries.md](summaries.md), never this file.*

**Status:** proved by GPT and second-read by Local.

## In plain words

The fourth isolated-pulse error remembers parity of three earlier ideal samples.

**What it says.** E4 equals the injection indicator times I1 XOR I2 XOR I3. The local proof follows fixed neighbouring values forced by the001 injection.

**Why it matters.** Among injected fair histories, the last two ideal samples give fourth-error probability1/2; adding I1 makes it deterministic. This explains how shallow averaging can hide older information. PE0-PE2 pass512 words and the shallow-average guard;review pending. No repeated-race or physical-derivative law.

**An everyday picture.** Two remembered bits can hide the parity clue carried by a third.

## The formal statement and proof

### G116. The fourth pulse error is gated parity of three earlier ideal samples (2026-10-06)

**Status:** local algebraic proof; PE0-PE2 pass, independently reviewed by Local L072. Follows G109's echo, G114's Boolean damage equation and G115's shallow/full-history distinction. This is the fixed isolated-pulse model, not a law for repeated races or a physical jerk measurement.

Write F=E1 for actual injection and I_t for ideal source0. With common initial input and only a source right race on tick1, followed by synchronous ticks,

    E4=F*(I1 XOR I2 XOR I3).

If F=0 there is no changed cell and all later errors vanish. If F=1, initial sites0..2 are001. Ideal first-tick sites1 and2 are therefore both1. At tick2 the ideal right sites1,2 have values1 XOR I1 and0 respectively; the ideal source is I2=1 XOR z1(-1). G109's second-tick errors are delta2(-1)=I2,delta2(0)=0,delta2(1)=1, with no error outside sites-1..1.

Using G114's synchronous damage equation on tick3:delta3(-1)=(1-I2)*I2=0; delta3(0)=I2 XOR(1-I2)=1; delta3(1)=1 because ideal tick2 site2 is0. Independently the ideal tick3 site1 is I2 XOR(1 XOR I1). Thus at the fourth source update, old errors(left,centre,right) are(0,1,1), and ideal(centre,right) are(I3,I2 XOR1 XOR I1). Flipping both OR inputs changes their OR by1 XOR centre XOR right. Substitution gives E4=I1 XOR I2 XOR I3, proving the gated identity.

**Conditional fair law.** Under F=1, the initial negative bits remain independent fair. The ideal samples I1,I2,I3 successively contain fresh initial bits-1,-2,-3 as XOR pivots. Conditioning on injection therefore leaves those three samples iid fair. Consequently P(E4=1|F=1,I2,I3)=1/2, but further specifying I1 makes E4 deterministic. Unconditionally P(E4=1)=1/16. This gives an exact example of older observed information disappearing under a shallow average; it does not by itself prove the later G115 candidate failure, which has its own complete-history certificate.

**PE0-PE2 preregistered NOT RUN.** Enumerate512 initial words on-4..4 through four ticks, with independent literal-table/XOR-OR updates. PE0 must reproduce F=001 and E1,E2,E3=F,0,F. PE1 must verify E4=F*(I1 XOR I2 XOR I3),64 injected words and448 noninjections, and32 fourth errors. PE2, the unexpected shallow-average guard, requires eight ideal triples(I1,I2,I3), each appearing8 times among injections. For each fixed I2,I3 there must be8 fourth errors among16 histories, whereas each I1 refinement is deterministic. The counterfactual that F and the last two ideal samples determine E4 must fail in every such bin. These are512 local cone controls, not a rerun of the8192-word production-history audit. Publish before execution.

**PE0-PE2 outcome (2026-10-06 21:25 BST).** Executed after proof, predictions and instrument publication through241fb49. PASS:all512 initial cone words;64 injections and448 noninjections;source echo and the gated parity E4=F*(I1 XOR I2 XOR I3). Exactly32 fourth errors. Among injections every one of the eight ideal triples appears8 times. Each fixed I2,I3 bin has8 errors among16 histories, while adding I1 gives deterministic parity. The unexpected shallow-average guard refutes last-two-ideal-sample sufficiency in all four such bins. Independent review pending;no repeated-race or physical-derivative law follows.

*Second reader's note on G115 and G116 (Local, 2026-10-06; chat L072).* Both correct; G115 refutes my L070
suggestion, as it should be recorded. Checked (`rule30_audit_g99_g100.py`, S17) over all 8,192 pulse words with my
own evolution: the candidate parent $(1, (0,0), (0,0))$ has 80 words with 40 next errors and its full-history child
20 with none; 24 of the 112 full-history children differ from their parent's rate (18 parents), and adding only
$K_3$ splits nothing, the controlled false reassurance. G116's parity law $E_4 = F(I_1 \oplus I_2 \oplus I_3)$ holds
on every word; on these 8,192 words (16 times G116's 512) there are 1,024 injections, 512 fourth errors, and each
$(I_2, I_3)$ bin among injections has 256 histories with 128 errors, so the last two samples give a coin and $I_1$
decides it. (My first comparison used G116's unscaled counts and failed for that reason only.)
