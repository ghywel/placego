"""G76 SA1-SA2, preregistered at961ed39.
SA1 MUST HOLD: widths2..10,T=m..24, exact positive/negative budgets,
net agrees with direct count minus coin, triangle exceeds absolute net.
Keep zero-net and empty ensembles; ratios only in stated domains.
SA2 BLIND: some positive-count case has nonzero net and A/abs(D)>2.
CF: every term has final-net sign; MUST FAIL width3,T5.
REFUTED-BY: guard terms(+1/4,-1/4,+1/2), net1/2, triangle1.
OUTCOME 2026-10-06, GPT Intel Python, under1 s:
SA1 PASS180 cases;148 nonzero-net cases have opposite-sign terms;
18 zero-net and57 empty-final cases retained. SA2 HELD: width10,T20,
C13, Pplus2067/512, Pminus2243/512, cancellation2155/88 (~24.49).
Largest A/Q=1033093/95527 at width5,T24. CF REFUTED.
No rate fit, asymptotic bound, or larger count job.
"""
from collections import Counter
from fractions import Fraction
from collatz_gpt_backward_weights import backward, states_at
from collatz_gpt_boundary_loss import coin, direct_count


def main():
    V, _ = coin(24)
    records = []
    zeros, empty = [], []
    opposite = 0
    guard = None
    for w in range(2, 11):
        m = w-1
        rows = states_at(w, 24)
        for T in range(m, 25):
            f = backward(T)
            plus = minus = Fraction(0)
            terms = []
            for t in range(m, T):
                I = Counter()
                for y, a in rows[t]:
                    I[a] += 1 if y % 2 else -1
                for a, imbalance in I.items():
                    g = imbalance*(f[t+1][a+1]-f[t+1][a])/2
                    terms.append(g)
                    plus += max(g, 0)
                    minus += max(-g, 0)
            D, A = plus-minus, plus+minus
            Q = Fraction(2**m*V[T], 2**T)
            C = direct_count(2**m, 2**(m+1), T)
            assert C == len(rows[T]) and D == C-Q and A >= abs(D)
            if not D:
                zeros.append((w, T))
            if not C:
                empty.append((w, T))
            opposite += bool(D and any(g*D < 0 for g in terms))
            records.append((w, T, C, plus, minus, A/Q, D/Q,
                            A/abs(D) if D else None))
            if (w, T) == (3, 5):
                guard = terms
                assert terms == [Fraction(1, 4), Fraction(-1, 4), Fraction(1, 2)]
    candidates = [r for r in records if r[2] and r[7] is not None]
    largest_cancellation = max(candidates, key=lambda r: r[7])
    largest_budget = max(records, key=lambda r: r[5])
    print('SA1 PASS', len(records), 'cases;', opposite, 'nonzero-net cases with opposite-sign terms')
    print('All zero-net cases:', zeros)
    print('All empty-final cases:', empty)
    print('Row fields: w,T,C,Pplus,Pminus,A/Q,D/Q,A/abs(D)')
    print('Largest A/Q:', largest_budget)
    print('Largest cancellation factor with C>0:', largest_cancellation)
    print('SA2', 'HELD' if largest_cancellation[7] > 2 else 'REFUTED',
          ': positive-count cancellation factor exceeds2')
    print('CF REFUTED: width3,T5 terms:', guard)


if __name__ == '__main__':
    main()
