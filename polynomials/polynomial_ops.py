"""
Polynomial ops: add, multiply, divide (with remainder), evaluate.
Build from scratch, verify against galois.Poly.
"""

import galois


def poly_add(p1, p2):
    return p1 + p2


def poly_eval(p, x):
    """evaluate a polynomial at point x using Horner's method
    reduces polynomial computation from O(n²) to O(n)

    p(x) = a₀ + a₁x + a₂x² + a₃x³
    becomes:
    p(x) = a₀ + x(a₁ + x(a₂ + x·a₃))
    """
    coeffs = p.coeffs  # galois stores highest coefficient first
    result = coeffs[0]

    for i in coeffs[1:]:
        result = result * x + i

    return result


def poly_mul(p1, p2):
    # algorithm: coefficient of xᵏ = sum of all aᵢ·bⱼ where i+j=k

    GF = p1.field
    c1 = p1.coeffs[::-1]
    c2 = p2.coeffs[::-1]  # reverse the coeffs because galois stores highest coeff first

    result = [GF(0)] * (len(c1) + len(c2) - 1)  # initialize n elements of GF(0) in the array first
    for i, a in enumerate(c1):
        for j, b in enumerate(c2):
            result[i + j] = result[i + j] + a * b

    return result


def poly_div(p1, p2, GF):
    pass


if __name__ == "__main__":
    GF = galois.GF(17)

    # poly_add
    p1 = galois.Poly([1, 2], field=GF)
    p2 = galois.Poly([4, 3], field=GF)
    assert poly_add(p1, p2) == galois.Poly([5, 5], field=GF)

    # poly_eval — p(x) = x³ + 2x² + 3x + 5 in GF(17)
    p = galois.Poly([1, 2, 3, 5], field=GF)
    assert poly_eval(p, 0) == 5  # constant term
    assert poly_eval(p, 1) == 11  # 1 + 2 + 3 + 5
    assert poly_eval(p, 5) == 8  # 125 + 50 + 15 + 5 = 195 ≡ 8 (mod 17)

    # poly_mul — (x + 2)(4x + 3) = 4x² + 11x + 6
    m1 = galois.Poly([1, 2], field=GF)  # x + 2
    m2 = galois.Poly([4, 3], field=GF)  # 4x + 3
    assert poly_mul(m1, m2) == [GF(6), GF(11), GF(4)]  # ascending: [const, x, x²]

    # galois multiplies independently; reverse its descending coeffs to match our ascending
    truth = m1 * m2
    assert poly_mul(m1, m2) == list(truth.coeffs)[::-1]

    # next: implement poly_div
