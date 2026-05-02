# Elliptic curves and pairings

Group operations on BN128 and the bilinear pairing that makes pairing-based polynomial commitment verification possible.

## Files

_(implementation in progress)_

- G1 addition and scalar multiplication
- Pairing computation via `py_ecc.bn128`
- Bilinearity verification: `e(aG, bH) == e(G, H)^{ab}`

## References

- [py_ecc](https://github.com/ethereum/py_pairing)
- [zkiap session 3](https://zkiap.com/) — math building blocks
- [RareSkills ZK Book](https://rareskills.io/zk-book) — elliptic curves and pairings chapters
