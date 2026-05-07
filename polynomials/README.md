# polynomials

Polynomial primitives over finite fields, used as building blocks for KZG commitments and PLONK.

## Files
- `lagrange.py` — Lagrange interpolation through (x, y) points
- `schwartz_zippel.py` — vector equality via random polynomial evaluation
- `polynomial_ops.py` — add, multiply, evaluate (Horner), divmod

## References
- RareSkills ZK Book: [Lagrange](https://rareskills.io/post/lagrange-interpolation), [Schwartz-Zippel](https://rareskills.io/post/schwartz-zippel-lemma)