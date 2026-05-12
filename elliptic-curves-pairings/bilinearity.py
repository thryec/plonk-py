from random import randint

from py_ecc.bn128 import G1, G2, curve_order, eq, multiply, pairing

# bilinearity property:  e(a·G, b·H) = e(G, H)^(a·b)

for i in range(50):
    rand_a = randint(1, curve_order - 1)
    rand_b = randint(1, curve_order - 1)

    aP = multiply(G1, rand_a)
    bQ = multiply(G2, rand_b)

    LHS = pairing(bQ, aP)
    RHS = pairing(G2, G1) ** (rand_a * rand_b)

    assert eq(LHS, RHS)

print("Bilinearity property verified 50 times")
