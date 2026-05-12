# Elliptic curves and pairings

BN254 group operations and bilinear pairings, used for KZG commitment verification in week 2.

## Concepts

**G1, G2.** Two cyclic subgroups of order `curve_order` on BN254. G1 coordinates live in 𝔽_p; G2 coordinates live in 𝔽_p². EVM exposes `add`/`mul` precompiles for G1 only.

**Two primes.**
- `field_modulus` (p) — modulus for point coordinates
- `curve_order` (n) — modulus for scalars in `multiply(P, scalar)`

Both ~2²⁵⁴ bits, different primes.

**Bilinear pairing.** `e: G1 × G2 → GT` (GT ⊂ 𝔽_p¹²), with:
- `e(a·G, b·H) = e(G, H)^(a·b)`
- `e(G1_gen, G2_gen) ≠ 1`

**KZG connection.** Polynomial commitment is one G1 point. Opening proof for `p(z) = y` is one G1 point. Verification is one pairing equation between the two commitments and the trusted-setup G2 element.

## Files

- **`bn128_demo.py`** — scalar mul, group add, cross-group type errors, basic pairing equality.
- **`bilinearity.py`** — 50 random `(a, b)` pairs, asserts `pairing(b·H, a·G) == pairing(H, G)^(a·b)`.
- **`solidity/`** — Foundry project calling `ecPairing` precompile (0x08) via `staticcall`, with pass/fail tests.

## py_ecc.bn128 API

| Symbol | What it is |
|---|---|
| `G1` | G1 generator `(1, 2)` |
| `G2` | canonical G2 generator |
| `multiply(P, k)` | scalar mul, `k·P` |
| `add(P, Q)` | group addition (same group only) |
| `pairing(Q, P)` | `e(Q, P)` — G2 first arg, returns FQ12 |
| `eq(a, b)` | equality across point types |
| `curve_order` | scalar field modulus |
| `field_modulus` | coordinate field modulus |

## References

- [py_ecc](https://github.com/ethereum/py_pairing)
- [RareSkills: bilinear pairings](https://rareskills.io/zk-book)
- [zkiap session 3](https://zkiap.com/)
- [EIP-197](https://eips.ethereum.org/EIPS/eip-197)
