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


def poly_div(p1, p2):
    GF = p1.field
    dividend = list(p1.coeffs)
    divisor = list(p2.coeffs)

    if len(divisor) == 0:
        raise ZeroDivisionError("divide by zero polynomials")

    quotient_coeffs = []

    # when dividend's degree >= divisor's degree
    while len(dividend) >= len(divisor):
        coeff = dividend[0] / divisor[0]
        quotient_coeffs.append(coeff)

        for i in range(len(divisor)):
            dividend[i] = dividend[i] - coeff * divisor[i]

        dividend = dividend[1:]

    quotient = galois.Poly(quotient_coeffs, field=GF) if quotient_coeffs else galois.Poly([0], field=GF)
    remainder = galois.Poly(dividend, field=GF) if dividend else galois.Poly([0], field=GF)

    return quotient, remainder


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

    # poly_div — (x³ + 2x² + 3x + 5) / (x + 1) = (x² + x + 2) remainder 3
    d1 = galois.Poly([1, 2, 3, 5], field=GF)  # x³ + 2x² + 3x + 5
    d2 = galois.Poly([1, 1], field=GF)  # x + 1
    q, r = poly_div(d1, d2)
    assert q == galois.Poly([1, 1, 2], field=GF)  # x² + x + 2
    assert r == galois.Poly([3], field=GF)  # constant 3

    # oracle: galois divmod
    truth_q, truth_r = divmod(d1, d2)
    assert q == truth_q
    assert r == truth_r
