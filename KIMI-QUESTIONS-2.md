# Rule 30 beside an alternating wall: the forced left half

Self-contained, as before. Mark every assertion **proved**, **computed** or **conjectured**; give computations in a
form that can be rerun; state every case. Answer in order: A0 first (a calibration with a known answer), then A. B is
optional.

## The rule and the wall

Cells take the values 0 and 1. Rule 30: x_{t+1}(i) = x_t(i-1) XOR ( x_t(i) OR x_t(i+1) ), sites i in Z, times t >= 0.

Suppose column 0 is an alternating **wall**: x_t(0) = t mod 2 for all t >= 0. Write the update of column 0 itself as
x_{t+1}(0) = x_t(-1) XOR ( x_t(0) OR x_t(1) ). Solving it for x_t(-1):

- at odd t, x_t(0) = 1 and so x_t(-1) = x_{t+1}(0) XOR 1 = 1, whatever x_t(1) is;
- at even t, x_t(0) = 0 and so x_t(-1) = 1 XOR x_t(1).

So column -1 is determined by column 1 at even times only. Call v_k = x_{2k}(1) the **visible sequence**; column -1 is
1 at odd times and 1 - v_k at time 2k. The same solving step applies to every column: for i <= 0,

    x_t(i-1) = x_{t+1}(i) XOR ( x_t(i) OR x_t(i+1) ).

Hence columns 0 and -1 determine column -2, those determine column -3, and so on: the whole left half x_t(i), i <= -1,
is a function of the visible sequence v. Call it the **forced left half** of v. This is the **free model**: v is any
binary sequence; nothing is assumed about the right half, so realizability by Rule 30 to the right plays no part.

## A0 — calibration (answer known to us)

Replace the alternating wall by the constant white wall x_t(0) = 0 for all t. Then x_t(-1) = x_t(1) for every t and the
left half is again determined by column 1 (now at all times). Show that some column-1 sequence makes the forced left
half **eventually zero at time 0**: there is d with x_0(i) = 0 for every i <= -d. Give the sequence explicitly and
prove the claim.

## A — the record of the alternating wall

Define, for the alternating wall, R(d) = the largest L such that some visible sequence v makes x_0(-d) = x_0(-d-1) =
.. = x_0(-d-L+1) = 0 (a run of L zeros in the time-0 row starting at depth d). Since x_0(-k) depends only on
v_0 .. v_k (the cell at depth k needs column -1 up to time k), R(d) is a well-defined maximum if it is finite.

Known to us by exhaustive computation (each value is exact): R(d) for d = 1 .. 61, 65, 69, 73, 77, 81, 85, 89; among
them R(9) = 9, R(13) = 17, R(16) = 16, R(33) = 33, R(41) = 37, R(49) = 39, R(56) = 42, R(59) = 51, R(61) = 49,
R(65) = 57, R(89) = 75. At every computed depth R(d) <= d + 4, with equality at d = 2 and d = 13 only; the fit is
R(d) ~ 0.826 d + 0.8. A counting heuristic reproduces the fit: inside a run, every other cell can be kept at zero by
choosing the newest visible bit, and each of the other cells is a fair coin, so about half a bit of v is spent per cell
of run. Trivially R(d + 1) >= R(d) - 1.

**Question.** Prove that R(d) is finite for every d, with an explicit bound (the conjecture is R(d) <= d + 4; any bound
f(d) finite at every depth is the result), or construct a visible sequence whose forced left half is eventually zero
at time 0, which would show R(d) infinite for some d.

Why it matters, in these terms only: if R(d) is finite for every d, then by compactness no configuration that is zero
on all of i <= -d can keep the alternating wall for ever, for any d. A0 shows the statement fails for a constant wall,
so a proof must use the alternation; the alternation is also why column -1 is pinned to 1 at odd times, which is where
the "half a bit per cell" comes from. If you cannot settle it, give the strongest partial result you can prove with
proof: a bound f(d) for all d however weak, or a proof of the half-bit statement (every other cell of a run is forced
and the rest are free), or an exact description of the visible sequences that achieve R(d).

## B — optional, the period-4 wall 1100

Now let column 0 follow 1100 repeating: x_t(0) = 1 if t mod 4 is 0 or 1, else 0 (or any rotation of it). Here the
right half matters, so consider all configurations: define R'(d) = the largest L such that some configuration on all of
Z keeps that wall for t = 0 .. d + L - 1 with x_0(-d) = .. = x_0(-d-L+1) = 0. Computed exactly (SAT over the light
cone, maximum over the four rotations), R'(d) for d = 3 .. 22 is
7, 6, 5, 6, 6, 5, 4, 6, 5, 5, 6, 7, 6, 5, 6, 7, 11, 10, 9, 8.
For comparison the alternating wall's analogous values at d = 20, 21, 22 are 16, 15, 14.

**Question.** Is R'(d) finite for every d? Equivalently, is there a configuration, zero on all of i <= -d for some d,
whose column 0 follows 1100 repeating (any rotation) for all t >= 0? The two kinds of wall tick available here, the
white stretch 00 (during which x_{t+1}(1) = x_t(1) OR x_t(2), monotone) and the black stretch 11 (during which
x_{t+1}(1) = NOT( x_t(1) OR x_t(2) )), are the locks that settle the constant walls; say whether they settle this one.

## How to answer

- A0, then A; B only if time remains.
- Mark every assertion **proved**, **computed** or **conjectured**; prove every lemma you use or say you assume it.
- Give computations in a rerunnable form.
