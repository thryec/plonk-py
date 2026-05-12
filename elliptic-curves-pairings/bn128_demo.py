from py_ecc.bn128 import G1, G2, add, curve_order, eq, multiply, pairing

print(G1, G2)  # generator points from their existing group
print(curve_order)


x = 12

# adding curve_order to scalar just adds another round around the cyclic group
# n · G1 = O
assert eq(multiply(G2, x + curve_order), multiply(G2, x))
assert eq(multiply(G1, x + curve_order), multiply(G1, x))

# new points can be constructed with scalar multiplication (i.e. repeated addition)
print(eq(add(G1, G1), multiply(G1, 2)))
print(eq(add(G2, G2), multiply(G2, 2)))


# you can only add elements from the same group
try:
    add(G1, G2)
    assert False, "expected TypeError"
except TypeError:
    pass


# bilinear pairings

P = multiply(G1, 2)
Q = multiply(G2, 9)
R = multiply(G1, 18)

# 2 * 9 = 18 can be proved with just P,Q,R points
# bilinearity helps to hide inputs 2 and 9
assert eq(pairing(Q, P), pairing(G2, R))


# we can also compare other G1 and G2 points

P1 = multiply(G1, 4)
P2 = multiply(G2, 8)

Q1 = multiply(G1, 2)
Q2 = multiply(G2, 16)

assert eq(pairing(P2, P1), pairing(Q2, Q1))

# G1 x G2 = GT
# LHS discrete log points are multiplied, then added together to get RHS

# discrete log: 14 + 18 = 32
P1 = multiply(G1, 2)
P2 = multiply(G2, 7)

Q1 = multiply(G1, 6)
Q2 = multiply(G2, 3)

# 4 * 8 = 32

R1 = multiply(G1, 4)
R2 = multiply(G2, 8)

assert eq(pairing(P2, P1) * pairing(Q2, Q1), pairing(R2, R1))
