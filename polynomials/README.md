# polynomials

Polynomial primitives over finite fields — building blocks for KZG and PLONK.

## Concepts

**Lagrange interpolation.** Given n points `(xᵢ, yᵢ)`, exactly one polynomial of degree < n passes through all of them. Constructed as a weighted sum of basis polynomials (each 1 at one input, 0 at the rest). PLONK uses this to encode wire values as a polynomial.

**Schwartz-Zippel lemma.** Two distinct polynomials of degree d agree on at most d points in a field of size p. So evaluating at a random field element gives ≈ d/p chance of false agreement — the soundness argument behind "evaluate at a random challenge."

**Polynomial arithmetic.** Add, multiply, evaluate, divide. Division by `(x − a)` is the workhorse: if `p(a) = b`, then `(p(x) − b) / (x − a)` divides cleanly. KZG opening proofs commit to exactly this quotient.

## Files

- **`lagrange.py`** — `lagrange_poly(xs, ys, GF) → galois.Poly`. Oracles: `scipy.interpolate.lagrange`, `galois.lagrange_poly`.
- **`schwartz_zippel.py`** — vector equality via random polynomial evaluation.
- **`polynomial_ops.py`** — from-scratch arithmetic:
  - `poly_add(p1, p2) → galois.Poly`
  - `poly_mul(p1, p2) → list` (ascending coefficients)
  - `poly_div(p1, p2) → (galois.Poly, galois.Poly)`
  - `poly_eval(p, x) → field element` (Horner's, O(n))

## Field

`galois.GF(17)` for examples. PLONK production uses the BN254 scalar field (~2²⁵⁴); the math is identical.

## References

- [RareSkills: Python Lagrange interpolation](https://rareskills.io/post/python-lagrange-interpolation)
- [RareSkills: Schwartz-Zippel lemma](https://rareskills.io/post/schwartz-zippel-lemma)
- [zkiap session 3](https://zkiap.com/) — math building blocks
- [galois library docs](https://mhostetter.github.io/galois/latest/)
