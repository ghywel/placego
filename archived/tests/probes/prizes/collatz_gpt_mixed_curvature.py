"""G80 MP1-MP2; preregistered ata4645cf.
MP1 MUST HOLD: existing widths2..10,T=m..24, every interior mixed
block equals backward curvature; retain boundary mixed blocks.
MP2 MUST HOLD: disjoint blocks recover direct count minus coin,
including killed inputs, odd tails, empty ensembles and T=m.
CF: curvature applies to every mixed block; MUST FAIL boundary guard.
REFUTED-BY: width2,T3,t1,a1 actual10 contributes1/2, invalid formula1/4.
OUTCOME 2026-10-06, GPT Intel Python, under1 s:
MP1 PASS2925 interior mixed controls;257 surviving boundary blocks
retained. MP2 PASS180 finals,753 killed block inputs,88 odd tails,
57 empty finals. Guards PASS; CF REFUTED. No frequency/rate estimate.
"""
from fractions import Fraction
from collatz_gpt_backward_weights import backward, states_at
from collatz_gpt_boundary_loss import threshold, coin, direct_count


def steps(q, a, t, length):
    bits, stays = [], True
    for j in range(t+1, t+length+1):
        b = q % 2
        bits.append(b)
        a += b
        q = (3*q+1)//2 if b else q//2
        stays &= 3**a >= 2**j
    return q, a, stays, bits


def change(f, q, a, t, length):
    _, final_a, stays, bits = steps(q, a, t, length)
    literal = (f[t+length][final_a] if stays else 0)-f[t][a]
    return literal, bits, stays


def curvature(f, t, a):
    F = f[t+2]
    return (2*F[a+1]-F[a]-F[a+2])/4


def main():
    interior = boundary = blocks = killed = odd_tails = empty = 0
    V, _ = coin(24)
    for w in range(2, 11):
        m = w-1
        rows = states_at(w, 24)
        for T in range(m, 25):
            f = backward(T)
            for t in range(m, T-1):
                for q, a in rows[t]:
                    literal, bits, stays = change(f, q, a, t, 2)
                    if sum(bits) != 1 or not stays:
                        continue
                    if a >= threshold(t+1):
                        assert literal == curvature(f, t, a)
                        interior += 1
                    else:
                        boundary += 1
            total = Fraction(0)
            t = m
            while t+2 <= T:
                for q, a in rows[t]:
                    literal, bits, stays = change(f, q, a, t, 2)
                    killed += not stays
                    total += curvature(f, t, a) if sum(bits) == 1 and a >= threshold(t+1) else literal
                t += 2
            if t < T:
                for q, a in rows[t]:
                    total += change(f, q, a, t, 1)[0]
                odd_tails += 1
            C = direct_count(2**m, 2**(m+1), T)
            assert total == C-Fraction(2**m*V[T], 2**T)
            empty += not C
            blocks += 1
    q, a, stays, _ = steps(3, 0, 0, 1)
    assert stays and (q, a) == (5, 1)
    f = backward(3)
    literal, bits, stays = change(f, q, a, 1, 2)
    assert stays and bits == [1, 0]
    assert literal == Fraction(1, 2) and curvature(f, 1, a) == Fraction(1, 4)
    q, a, stays, _ = steps(7, 0, 0, 2)
    assert stays and (q, a) == (17, 2)
    f = backward(5)
    assert change(f, q, a, 2, 2)[0] == curvature(f, 2, a) == 0
    print('MP1 PASS', interior, 'interior mixed controls;', boundary, 'surviving boundary mixed blocks retained')
    print('MP2 PASS', blocks, 'finals;', killed, 'killed block inputs,', odd_tails,
          'odd tails,', empty, 'empty finals retained')
    print('Guards PASS: interior0; boundary1/2 versus invalid1/4. CF REFUTED')


if __name__ == '__main__':
    main()
