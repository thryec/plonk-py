"""KZG polynomial commitment scheme.

A toy implementation of Kate-Zaverucha-Goldberg (2010), using py_ecc for
BN254 pairing operations. This is for understanding, not production use —
in particular, the trusted setup here uses a hardcoded tau, which would
defeat the security of a real deployment.

Reference: https://dankradfeist.de/ethereum/2020/06/16/kate-polynomial-commitments.html
"""

import galois
from py_ecc.bn128 import G1, G2, add, curve_order, multiply, pairing

# Use the BN254 scalar field for polynomial coefficients.
GF = galois.GF(curve_order)


def trusted_setup(tau, max_degree):
    """Generate KZG setup parameters"""
    g1_powers = []  # [G1, tau*G1, tau^2*G1, ..., tau^d * G1]
    g2_powers = []  # same in G2

    for i in range(max_degree + 1):
        # multiply G1 by tau^i, use pow syntax for exponentiation
        g1_powers.append(multiply(G1, pow(tau, i, curve_order)))

        # multiply G2 by tau^i
        g2_powers.append(multiply(G2, pow(tau, i, curve_order)))

    return g1_powers, g2_powers


def commit(poly, g1_powers):
    """Commit to a polynomial p(x) = sum(c_i * x^i).
    The commitment is C = [p(tau)] * G1 = sum(c_i * tau^i * G1)
                                       = sum(c_i * g1_powers[i])
    """
    coeffs_asc = poly.coeffs[::-1]  # galois.Poly stores descending; flip to ascending
    commitment = multiply(g1_powers[0], int(coeffs_asc[0]))
    for i in range(1, len(coeffs_asc)):
        term = multiply(g1_powers[i], int(coeffs_asc[i]))
        commitment = add(commitment, term)
    return commitment


def open(poly, z, g1_powers):
    """Produce an opening proof that p(z) = y for a known point z.

    Compute q(x) = (p(x) - y) / (x - z), where y = p(z).

    The proof is the commitment to q(x):
        pi = [q(tau)] * G1

    Returns (y, pi).
    """
    y = poly(z)
    numerator = poly - galois.Poly(y)
    divisor = galois.Poly([1, -z], field=GF)
    quotient = numerator // divisor
    assert numerator % divisor == 0, "division not exact — bug somewhere"

    pi = commit(quotient, g1_powers)
    return y, pi


def verify(commitment, z, y, pi, g2_powers):
    """Verify that the commitment opens to y at point z.

    Check the pairing equation:
        e(C - [y]*G1, G2) == e(pi, [tau]*G2 - [z]*G2)

    """
    # compute LHS pairing
    LHS = pairing(G2, add(commitment, multiply(G1, int(-y))))

    # compute RHS pairing
    RHS = pairing(add(g2_powers[1], multiply(G2, int(-z))), pi)

    return LHS == RHS


if __name__ == "__main__":
    tau = 1234
    max_degree = 4

    # trusted setup
    g1_powers, g2_powers = trusted_setup(tau, max_degree)
    assert len(g1_powers) == max_degree + 1
    assert len(g2_powers) == max_degree + 1
    assert g1_powers[0] == G1
    assert g2_powers[0] == G2
    print("trusted_setup ok")

    # commit
    poly = galois.Poly([4, 3, 2, 1], field=GF)  # descending: 4x^3 + 3x^2 + 2x + 1
    C = commit(poly, g1_powers)
    print(f"commitment: {C}")

    # open
    z = GF(5)
    y, pi = open(poly, z, g1_powers)
    print(f"opening: {y}, {pi}")

    # verify
    assert verify(C, z, y, pi, g2_powers)
    print("commit / open / verify ok")
