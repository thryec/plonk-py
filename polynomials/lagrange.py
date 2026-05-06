import galois
import numpy as np
from galois import lagrange_poly
from scipy.interpolate import lagrange

# simple lagrange interpolation of points

x_values = [1, 2, 3, 4]
y_values = [4, 8, 2, 1]

print(lagrange(x_values, y_values))  #  p(x) = 2.5x³ - 20x² + 46.5x - 25

# lagrange using finite field

GF17 = galois.GF(17)  # a class representing the finite field 𝔽₁₇, ie.. integers {0, 1, ..., 16}

xs = GF17(np.array(x_values))
ys = GF17(np.array(y_values))

p = galois.lagrange_poly(xs, ys)  # p(x) =  11x³ + 14x² + 4x + 9

# key takeaway: simple lagrange and lagrange over finite field gives different polynomials
# this is because lagrange's formula uses division, which means 5/2 = 2.5 in set of real numbers,
# and 5/2 = 5·inv(2) = 11 in 𝔽₁₇ (no fractions allowed in 𝔽₁₇)
# so the coefficients differ even though both polynomials pass through the same points
# inv(2) in 𝔽₁₇ is "the element x such that 2 · x ≡ 1 (mod 17)"


if __name__ == "__main__":
    print(xs, ys)
    print(p)

    assert p(1) == GF17(4)
    assert p(2) == GF17(8)
    assert p(3) == GF17(2)
    assert p(4) == GF17(1)
