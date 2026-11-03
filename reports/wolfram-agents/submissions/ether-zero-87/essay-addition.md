## Any right tail beyond 87

The cutoff 198 comes from the light cone alone. Masking does better. Let δ be the difference between the evolution H
of any row and the inserted edge's evolution G. With G's own values as coefficients, δ obeys an exact one-cell rule:

$$\delta'(x) = \delta(x-1) \oplus (\lnot r \land \delta(x)) \oplus (\lnot c \land \delta(x+1)) \oplus (\delta(x) \land \delta(x+1)),$$

where c and r are G's centre and right cells. A black right neighbour hides a change in the centre, and a black
centre hides a change on the right.

A **rooted observer** follows the leftmost difference L together with three-valued knowledge (0, 1 or unknown) of the
next two cells. **Half-line states**, "no difference at or left of m", advance by the recruitment step: m stays when
G's cell at m is black and falls by one otherwise. One tick evaluates the new cells over every completion of the
unknowns and branches until the new front is found. Half-line states are expanded into rooted ones up to a threshold,
and rooted states far to the right are retired into half-line ones. The tick is sound for **every** choice of those
thresholds, so the thresholds are untrusted data (`tick_sound`). The background rows are bit masks, and the kernel
runs each alignment's check (`check_sound`, `decide +kernel`).

```lean
theorem edge_pinned_tail87 (c0 c1 : Nat) (h0' : c0 < 7) (h1' : c1 < 4) {H : Nat → Int → Bool} (hH : IsR30Z H)
    (h0 : ∀ x, x ≤ 87 → H 0 x = initRow c0 c1 x) : ∃ xB : Int, ∃ t1 : Nat, ∀ t, t1 ≤ t →
    (∀ x, x ≤ xB → H t x = etherZ c0 x (t + c1)) ∧ ∃ x, xB < x ∧ x ≤ xB + 13 ∧ H t x ≠ etherZ c0 x (t + c1)
```

The cutoff 87 cannot be lowered for these entries. Flipping only the cell at 87 changes the 13-cell window at
alignment (4, 3) at time 222:

```wl
edgeRow[f_Integer] := Table[Which[x < 0, ether[x + 4, 3], x == 0 || x == f, 1, True, 0], {x, -700, 400}];
window[r_] := CellularAutomaton[30, r, {{{222}}, {-36, -24} + 701}];
base = window[edgeRow[-1000]];   (* no extra flip *)
{window[edgeRow[87]] == base, window[edgeRow[88]] == base, window[edgeRow[86]] == base}
```

The comparisons are False, True and True: of these three flips, only the cell at 87 reaches the window (checked on
Wolfram Engine 15.0, and replayed in Python by `tests/probes/exact_tail_bridge.py`'s single-flip scan, T53). This is a statement about the entries used here: a row that agrees
only through 86 may still be pinned through some other entry.
