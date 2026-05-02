# plonk-py

A from-scratch implementation of the PLONK proving system in Python,
built up from polynomial arithmetic through KZG commitments to the
full protocol.

## Contents

1. [Polynomials](./polynomials/) — lagrange interpolation, schwartz-zippel, basic ops
2. [Elliptic curves and pairings](./elliptic-curves-pairings/) — bilinearity, py_ecc reps
3. [KZG commitments](./kzg-commitments/) — polynomial commitment scheme
4. [PLONK theory](./plonk-theory/) — protocol notes
5. [PLONK implementation](./plonkathon/) — full prover and verifier (based on 0xPARC's plonkathon curriculum)

## Running

This repo uses git submodules. Clone with:

```bash
git clone --recursive https://github.com/thryec/plonk-py.git
```

To run the PLONK implementation:

```bash
cd plonkathon
poetry install
poetry run python test.py
```

## Notes

See [NOTES.md](./NOTES.md) for technical commentary on the implementation.

## References

- [RareSkills ZK Book](https://rareskills.io/zk-book)
- [zkiap (MIT IAP 2023)](https://zkiap.com/)
- [plonkathon (0xPARC)](https://github.com/0xPARC/plonkathon)
- [Vitalik on PLONK](https://vitalik.eth.limo/general/2019/09/22/plonk.html)
- [Dankrad Feist on KZG](https://dankradfeist.de/ethereum/2020/06/16/kate-polynomial-commitments.html)
- [PLONK paper](https://eprint.iacr.org/2019/953.pdf)
