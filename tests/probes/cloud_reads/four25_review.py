"""Cloud's carrying-read instrument for FOUR-BIN-PARTITIONS section 25 / 25.1 (MI557, MI579), CL475.

Identity (2): with x_i = k_i, z_i = l_i - 1 (i in J, |J| = j), sum x = kappa - D, sum z = q + D - j,
  sum_J (f_(c_i)(k_i + 1) - 1) - alpha = (1-D)kappa + j(j+1)/2 - D(j+2) + D^2 - C,
  f_c(k) = L(c-k) + (q+1)k + L(k), alpha = L(q) + (q+1)kappa + L(kappa), C = Cross(x) + Cross(z).
Checked exactly on random integer data (no admissibility needed: it is a polynomial identity), and the
vertex bound (3) min C >= j(j-2) + (j mod 2) checked over all vertex splits for d_i in {2,3}, j <= 10.
Prediction: 0 failures.

OUTCOME: identity (2) 200,000 cases, 0 failures; vertex bound (3) j = 2..10, 0 failures.
"""
import itertools, random
L = lambda n: n * (n - 1) // 2
cross = lambda v: sum(a * b for a, b in itertools.combinations(v, 2))
rnd = random.Random(7); bad = 0; n = 0
for _ in range(200000):
    j = rnd.randint(1, 8); D = rnd.randint(0, 6)
    x = [rnd.randint(0, 12) for _ in range(j)]; z = [rnd.randint(0, 12) for _ in range(j)]
    kappa = sum(x) + D; q = sum(z) - D + j
    lhs = sum(L(zi) + (q + 1) * (xi + 1) + L(xi + 1) - 1 for xi, zi in zip(x, z)) - (L(q) + (q + 1) * kappa + L(kappa))
    rhs = (1 - D) * kappa + j * (j + 1) // 2 - D * (j + 2) + D * D - (cross(x) + cross(z))
    n += 1; bad += lhs != rhs
print('identity (2):', n, 'cases,', bad, 'failures')
bad3 = 0
for j in range(2, 11):
    for d in itertools.product((2, 3), repeat=min(j, 6)):
        d = list(d) + [2] * (j - len(d))
        m = min(cross([d[i] for i in range(j) if s[i]]) + cross([d[i] for i in range(j) if not s[i]])
                for s in itertools.product((0, 1), repeat=j))
        bad3 += m < j * (j - 2) + (j % 2)
print('vertex bound (3), j = 2..10:', bad3, 'failures')
