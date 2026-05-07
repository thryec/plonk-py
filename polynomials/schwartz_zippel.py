import random

import galois
import numpy as np

# goal: to test if two polynomials are equal by sampling a random point

p = 103
GF = galois.GF(p)

xs = GF(np.array([1, 2, 3]))

v1 = GF(np.array([3, 5, 6]))
v2 = GF(np.array([3, 5, 6]))


def L(v):
    return galois.lagrange_poly(xs, v)


p1 = L(v1)
p2 = L(v2)

# find a random number between zero and p
random_int = random.randint(0, p)

lhs = p1(random_int)
rhs = p2(random_int)

assert lhs == rhs
