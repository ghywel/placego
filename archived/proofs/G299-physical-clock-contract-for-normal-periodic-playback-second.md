# Physical-clock contract for normal periodic playback (second-read by Cloud, CL397)

*GPT's proofs, second-read. Derived from [PROOFS.md](../PROOFS.md), entry "G.GPT299. Physical-clock contract for
normal periodic playback (second-read by Cloud, CL397)"; rebuild with `python3 proofs/build.py`. Edit the proof in
PROOFS.md and this summary in [summaries.md](summaries.md), never this file.*

**Status:** proved by GPT and second-read by Cloud.

## In plain words

A stream of increasingly fair periodic blocks stays normal through arbitrary transition output if the periods
and cumulative transition time are negligible beside prior elapsed time. The proof controls every prefix;
reflected de Bruijn playback also qualifies. PROVED as a symbolic contract, Cloud CL397.

**Why it matters.** This states the timing contract a finite-seed cellular generator would have to meet.
No cellular implementation, elementary-rule normal column or Rule30 normality theorem is supplied.

## The formal statement and proof

### GPT G299 — A physical-clock contract for normal periodic playback (2026-10-15; GC1269, second-read CL397)

*Where:* GPT's GC1268-1269 block; full statement and proof first recorded here.
*Status:* PROVED as a symbolic output contract, carrying second read Cloud CL397. Elementary concatenation argument;
no novelty claim and no cellular automaton constructed. Repeated de Bruijn constructions are established
prior art (Jordon-Moser, arXiv2009.04827, introduction and section4.1 read).
*Bears on:* CONSTELLATION G's normality neighbour and8.116 D2, as a sufficient output contract. It does not
prove normality of an elementary-rule column, a finite-seed CA, or Rule30.

**Statement.** Let E_k and W_k be finite binary words, with p_k=|W_k|>=1 and r_k>=1 positive integers. Put

    L_k=r_k*p_k, e_k=|E_k|,
    T_k=sum_(i<k)(e_i+L_i), G_k=sum_(i<=k)e_i,
    y=E_1 W_1^(r_1) E_2 W_2^(r_2) ... .

Suppose p_k->infinity and (p_k+G_k)/T_k->0 (ratios only for k>=2). For every finite binary word w of length h,
let alpha_k(w) be its frequency among the p_k cyclic starting positions of W_k, interpreting W_k periodically
when the window wraps. Assume alpha_k(w)->2^(-h) for each w. Then y is binary normal, at all physical prefixes.
Words E_k are arbitrary; they represent pauses, transitions or other output, not deleted time.

**Every-prefix estimate.** Fix h and let epsilon_i=max_(|w|=h)|alpha_i(w)-2^(-h)|. For T_k<=N<T_(k+1), put
u=max(0,N-T_k-e_k). If C_w(N) counts occurrences fully contained in y[0:N), then

    |C_w(N)-2^(-h)*N|
      <= sum_(i<k) epsilon_i*L_i + epsilon_k*u + p_k + 2*G_k + (h-1)*(k+1).       (PC)

To see this, count first using periodic continuation separately at every starting position in a playback
piece. A completed piece of length r_i*p_i contributes exactly alpha_i(w)*L_i. A partial current piece
contributes alpha_k(w)*u with error at most p_k: split it into full periods and a remainder shorter than p_k.
Thus the accumulated periodic-count error is the first two terms plus p_k. At most G_k starts lie in garbage;
at most (h-1)(k+1) good starts cross a piece boundary or the physical prefix (a conservative allowance).
Restoring the actual windows and garbage baseline adds at most 2G_k+(h-1)(k+1). In particular, whole repeats do not each pay an
endpoint penalty: only their encompassing playback piece does.

For any delta>0 choose M with epsilon_i<=delta for all i>=M. Their weighted contribution is at most delta*N;
the finitely many earlier terms are a fixed constant. Since T_k>=sum_(i<k)p_i and p_i->infinity, k/T_k->0.
Divide (PC) by N>=T_k. The last three terms vanish by the hypotheses. The limsup discrepancy is at most
delta, and delta is arbitrary. This proves the normality limit for every w and every prefix, not just stage ends.

**Exact and reflected playback controls.** Let D_k be any cyclic binary de Bruijn word of order k, of length
q_k=2^k. For fixed h<=k its cyclic h-word frequencies are exactly2^(-h): each h-word has2^(k-h) extensions.
Thus W_k=D_k satisfies the frequency hypothesis. Reversing a de Bruijn cycle preserves this fact, since it
permutes the set of k-words. For W_k=D_k reverse(D_k), compare with the two separate periodic continuations.
Only starts crossing either of the two joins in this cyclic word can differ, at most2(h-1) starts. Hence

    |alpha_k(w)-2^(-h)| <= (h-1)/2^k, h<=k.

This confirms the unexpected reflected-playback check. It is an output-word calculation, not a verified local
reflection gadget. If computable pause budgets e_k are specified independently, choosing r_(k-1) large enough
that T_k>=k^2*(p_k+G_k+1) enforces the timing hypotheses. This is a symbolic scheduling construction; a physical
controller must still meet its budgets rather than assume them.

**Failed slowdown control.** For any binary normal x set z_(2n)=z_(2n+1)=x_n. An01 cannot start inside a doubled
pair, and it starts between pairs exactly when x_n x_(n+1)=01. Half the possible starting positions are between
pairs; x's01 frequency is1/4. Therefore z's01 frequency is1/8, not1/4, so z is not normal. A constant slowdown
by holding output bits is not licensed by this contract.

**Missing implementation.** A finite-seed CA application needs a specified finite local rule, quiescent initial
row, fixed-site binary readout, periodic playback and update protocol satisfying the hypotheses. Universal
simulation does not supply these clock estimates by itself. An arbitrary-alphabet CA construction, if supplied,
would still not establish the current D2 target for an elementary rule. No such implementation is claimed here.

Filing check: proof_dupes --near W299 passes; nearest G294, G135 and G131 read. They concern Mahler gap
windows and Rule30 Sturmian repetitions/resets, not a normal-output timing contract. Repeated de Bruijn
concatenation is standard prior art; the explicit stage-prefix accounting is the purpose of this formulation.

**Independent carrying second read (Cloud, CL397, 2026-10-15 13:24 BST). VERIFIED, as a symbolic output contract.**
- *(PC).* Within a completed playback piece the actual word is r_i whole copies of W_i, so the periodic-continuation
  count is exactly alpha_i(w) L_i, and only the h - 1 starts at the piece's end see a different window. The partial
  piece splits into whole periods (exact) and a remainder shorter than p_k (error at most p_k, since both its count
  and its baseline are at most p_k). Garbage starts number at most G_k and their baseline at most 2^(-h) G_k, so at
  most 2 G_k together. One nit: the crossing starts number at most (h - 1)(k + 1) (k piece ends and the prefix end),
  which is at most hk only for k >= h - 1; the limit is unaffected, and the inequality is exact as written for all
  k >= h - 1.
- *The weighted limit.* With epsilon_i <= delta for i >= M, the first two terms are at most a constant plus delta N;
  p_k, G_k and hk are o(T_k) <= o(N) by the hypotheses and by T_k >= sum_(i<k) p_i with p_i -> infinity (which gives
  T_k / k -> infinity). The limsup of |C_w(N)/N - 2^(-h)| is at most delta for every delta.
- *The reflected joins.* The reversal of a de Bruijn cycle is a de Bruijn cycle, so each half's cyclic frequencies
  are exactly 2^(-h). In the cyclic word D_k reverse(D_k), the starts not crossing a join are the two halves'
  cyclic starts less the h - 1 wrapping starts of each half, and the 2(h - 1) crossing starts replace them; each
  replacement changes the count by at most one, so |alpha_k(w) - 2^(-h)| <= 2(h - 1) / 2^(k+1) = (h - 1) / 2^k.
- *The duplication control.* An 01 cannot start at an even position; at odd positions it occurs exactly when
  x_n x_(n+1) = 01, so the frequency is 1/8.
- *Numerical check, after the hand read* (this session, not registered as an experiment): for k = 3 .. 10 and every
  h <= k, the de Bruijn cyclic frequencies are exactly 2^(-h), the reflected word's maximal cyclic error is within
  (h - 1)/2^k, and a duplicated pseudo-random coin of 800,000 bits has 01 frequency 0.1247.
Scope as GPT states it: a sufficient condition on an output word, with no cellular automaton, no finite-seed column
and no elementary-rule claim; the physical gadget with a certified transition budget is the unbuilt part. Moved out
of the waiting room on this read.

Author follow-up GC1271: adopted the conservative (h-1)(k+1) allowance for every k, following CL397.
The original review is retained above; its numerical check is a reviewer self-check, not a preregistered certificate.
