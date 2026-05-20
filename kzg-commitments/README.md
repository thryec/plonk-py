# kzg-commitments

KZG polynomial commitment scheme implemented over BN254 using py_ecc.

The commitment to a polynomial p(x) is a single G1 element representing
[p(tau)] for a secret tau. Opening proofs let a verifier check p(z) = y
for any point z without learning p.

Verification reduces to a single pairing equation:
    e(C - [y]G1, G2) == e(pi, [tau]G2 - [z]G2)

This works because (p(x) - y) is divisible by (x - z) exactly when p(z) = y,
and the pairing lets us check this in the exponent.

## Files
- `kzg.py` — commit, open, verify, and trusted setup

## References
- [Kate-Zaverucha-Goldberg 2010](https://www.iacr.org/archive/asiacrypt2010/6477178/6477178.pdf)
- [Dankrad Feist's writeup](https://dankradfeist.de/ethereum/2020/06/16/kate-polynomial-commitments.html)
