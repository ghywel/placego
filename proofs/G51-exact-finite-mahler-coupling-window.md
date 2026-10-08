# Exact finite Mahler coupling window

*GPT's proofs, second-read. Derived from [PROOFS.md](../PROOFS.md), entry "G.GPT51. Exact finite Mahler coupling
window"; rebuild with `python3 proofs/build.py`. Edit the proof in PROOFS.md and this summary in
[summaries.md](summaries.md), never this file.*

**Status:** proved by GPT and second-read by Local.

## In plain words

The exact finite form of Mahler's two conditions over T steps: a class of whole numbers and a window of fractions.

**What it says.** For a pattern of T steps, the whole-number starts all leave one remainder on division by 2^T, and
the allowed starting fractions form one exact interval. Both are written down explicitly.

**Why it matters.** It turns Mahler's question into a finite check for each length, the kind of statement a computer
can test or a proof can iterate.

**An everyday picture.** A delivery address: a postcode that fixes the street, and a range of house numbers along
it, both written down exactly.

## The formal statement and proof

**Where:** RULE30-GPT.md G51; copied proof. **Status:** second-read by Local, 2026-10-06 (note below); GPT's MW1-MW3 finite controls pass (G51 outcome).

### G51 lemma and proof: exact finite Mahler coupling window

Fix a T-bit word b_0,...,b_(T-1). Put C_0=0 and C_(t+1)=3*C_t+b_t*2^t. Prescribed ceil branches and fractional branches give

    2^t*n_t=3^t*n_0+C_t,
    2^t*u_t=3^t*u_0-C_t.

The integer word is realized by the unique nonnegative residue r_T=-C_T*(3^T)^(-1) modulo2^T. This follows from prefix congruences and integrality, as in G49 with the sign reversed. The allowable initial fractions through timeT form the half-open interval

    I_T=[L_T,U_T),
    L_T=max_(0<=t<=T) C_t/3^t = C_T/3^T,
    U_T=min_(0<=t<=T) (C_t+2^(t-1))/3^t,

with the t0 upper endpoint interpreted as1/2. If L_T>=U_T it is empty. The lower equality follows because C_t/3^t is a partial sum of nonnegative terms b_j*2^j/3^(j+1). These inequalities are precisely0<=u_t<1/2 for all prefixes. Consequently every n_0=r_T+2^T*m>=0 paired with u_0 in I_T satisfies the finite Z-number condition throughT, except xi=n_0+u_0=0 is excluded. The recurrence in G50 proves both necessity and sufficiency; no independent parity or randomness assumption is needed.

Across increasing T for a single infinite word, realizing residues satisfy r_(T+1)=r_T or r_T+2^T. They therefore form a nondecreasing integer sequence. An ordinary nonnegative integer realizes the infinite itinerary if and only if these least residues are bounded: bounded monotone integers stabilize, and the stabilized value realizes every prefix; conversely a realizing integer has r_T equal to itself once2^T exceeds it. This makes the missing integer compatibility an explicit boundedness condition, separate from nonemptiness of the fractional intersection. No boundedness theorem for Mahler-admissible words is supplied.

Unexpected finite exclusion:10101 contains no11, but its terminal lower endpoint is133/243>1/2. Its fractional window is empty. Thus the simple no11 subshift from G50 is a strict overestimate of the fractional language; checking only adjacent forbidden bits is insufficient. These are elementary specialized forms of the already recorded decoupling/residue tools, not a new Mahler nonexistence proof.

*Second reader's note on G50 and G51 (Local, 2026-10-06; chat L022).* Both correct. G50: separating integer and
fractional parts of $\tfrac32(n_j + u_j)$ gives $n_{j+1} = \lceil 3n_j/2 \rceil$ and $u_{j+1} = (3u_j - b_j)/2$, with
$u_j < 1/3$ forced at even $n_j$ and $u_j \ge 1/3$ at odd; the tail series and its converse hold; two adjacent ones
force $u \ge 5/9$; the $(100)$ tails are $9/19$, $4/19$, $6/19$ in that order (G018's corrected order); and the
integer obstruction $19 n_0 + 9 \equiv 0 \pmod{8^k}$ follows because 19 and 27 are invertible modulo $8^k$. The
base-six rule's two outputs check for every $(y, z)$; that this is Kari and Kopra's rule is taken from the source,
not checked here. G51: both affine identities by induction; the window is exactly $0 \le u_t < 1/2$ for every
prefix, with $L_T = C_T/3^T$ because the partial sums increase; the residues are nondecreasing and stabilise
exactly when an ordinary integer realises the word; $10101$ gives $133/243 > 1/2$. Exact checks
(`collatz_audit_g39_g42.py`, G50/G51 part): for every word of length at most 12 with a nonempty window (588
words), $\xi = r_T + L_T$ was multiplied by $(3/2)^t$ in exact rationals, and its integer parts follow the word's
parities and its fractional parts stay in $[0, 1/2)$ through $T$; no $n_0 < 200$ passes the $8^6$ congruence.
