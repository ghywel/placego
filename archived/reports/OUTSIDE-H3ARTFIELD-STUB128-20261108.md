# h3artfield's stub128 entry, read against our record

*Local, L1583, 8 November 2026. The owner asked to work on the Q01 lead from the refresh (L1581). Source: portal entry [R30-20261108-29c0e5](https://www.wolframcloud.com/obj/rule-30-prize/Agents/status/R30-20261108-29c0e5), Lean Verified, by h3artfield with Cursor Agent (Composer); it supersedes 3edf26. The portal holds only a notebook. I downloaded it at the owner's word: 9,369,644 bytes, SHA256 `60c44dbd6b996c485fbb787722608876aaad2bc7317a083ad08a5cae704e8313`, kept outside git. I extracted the embedded Lean source as text with my own decoder and did not evaluate anything. It is about 90,000 lines, with 1,591 theorems, 679 of them closed by `decide`.*

**Verdict: no new route to Q01.** The entry is a careful, Lean-verified collection in which every main piece is known in kind. Its reduction is a residue split, and its open core is Q01 itself, as its own docstring says. Its exact-time families are truncations of two known periodic backgrounds, the stripe and the ether, dying when the truncation front reaches the wall. I had suggested in L1581 that its period-7 family might be our X lineage's 25-loop. That was wrong: it is the ether.

## What it proves, against what we have

| Its result | What it is | Our record or the kit |
|---|---|---|
| `Q01_iff_stub128_mortality`: Q01 iff every natural ≡ 29, 43, 53, 67, 75, 85, 99, 125 (mod 128) reaches an even value under G | A residue split. The eight classes are exactly the odd rows passing the first three checks, the 2^3 that `count_constrained` counts at that depth. All other classes are shown to reach an even value within 1 to 4 G-steps | Kit `Q01_iff_integer`, `count_constrained`. Known in kind; the same split exists at every depth |
| `stubborn128_no_uniform_hitting_bound` | Long survivors exist in each stubborn class | Kit `trunc_survives`; D(W) grows. Known in kind |
| `stubborn128_immortal_bitstring` (its "Target C") | An infinite immortal configuration with each stubborn prefix, not a natural | Kit `Theta`, `Theta_inX`. Known |
| `stubborn128_finite_immortal_iff_nat_immortal` | Finite-support immortality in a class is immortality of a natural in it | Kit encoding of rows by naturals. Known |
| `sparse10_cylinder_first_even`: 2^(2k+1)n + (4^k − 1)/3 first meets an even value at G-time k | The stripe −1/3 truncated after k ones, with higher bits arbitrary | Kit `Rule30ZeroBoundaryBarriers.trunc_survives` ("lives exactly through time n"). Known; the arbitrary higher bits follow from the light cone |
| `period7_cylinder_first_even`: 14m bits of 67 or 125 repeated, then the next periodic 1 omitted: time 7m | **The ether.** 67 and 125 repeated with period 7 are −67/127 = Θ((01)^∞) and −125/127 = Θ((10)^∞) (AM-5). I checked both, and that the row returns after 4 ticks. The truncation dies when its front reaches the wall, at 14m physical ticks | Truncated ether: portal [R30-20261103-29bcb9](https://www.wolframcloud.com/obj/rule-30-prize/Agents/status/R30-20261103-29bcb9); front arrival: the zero-run bridge (§8.82/8.95, AM-1 §4); kit `Rule30PeriodTwoSideways.truncation_death`. Known in kind |
| `oddDefect`, `oddDefect3`, `oddDefect7` families: the stripe with one extra bit at 4h + 1, 8h + 3 or 8h + 7: times 2h + 1, 4h + 3, 4h + 4 | A single defect in the stripe, killing when its front arrives, at a parity set by its position | The zero-run bridge. Known in kind; the explicit times are tidy formal statements |
| `case1493_cylinder_first_even`: 2^31 n + 1493 has exact G-time 15 | Our width-11 champion (D = 30), lifted to its light-cone cylinder | AM-1, L955. Known value |
| `not_InX` for 2^k − 1, (8^k − 1)/7 and residues mod 8, 32, 128, 512 | Finite-depth deaths | Known in kind |

My own replay agrees with its laws: the truncated ether at 14m bits first meets an even value at 7m for m = 1, 2, 3, 5, 8, and the stripe truncated after k ones at k for k = 1, 2, 3, 6, 10. The script is inline in the L1583 session and is not kept as a probe.

## What it is good for

- **Citations.** For any submission that uses truncated stripes, the ether or exact death times, this is a clean Lean source. That covers S-11 (the cut ether off the seed's edge cycle) and Block 8's lock work.
- **A template.** Its cylinder theorems carry "arbitrary higher bits" through the light cone and close by `decide`, in the style the kit accepts. That pattern would suit an exact-time family of ours.
- **Nothing for the open core.** The stubborn classes are where every immortal natural would have to be, and the entry leaves them open.

## Limits

- I read the docstring, the definitions and the twenty headline statements, not all 1,591 proofs. Its verifier pass is the portal's.
- "Known in kind" means our record or the kit has the same mechanism, not that it has every one of these exact statements.

**Record searched:** `record_find` on ether, truncat, zero-run, trunc_survives, 1493, 67/127, ether with truncat; `known_find` on stub128, InX, coalesc, ether with trunc, trunc_survives; AM-1 §4, AM-5 §0; the kit's `Rule30ZeroBoundary` and `Rule30ZeroBoundaryBarriers` sources at `48d8fbbc`.
