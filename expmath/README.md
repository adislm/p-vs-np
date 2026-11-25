# expmath

Search programs written during the counterexample hunt recorded in
`notes/12-experimental-search.md`.

**Provenance.** These were written by the search agents, not audited line by line.
They compile, their outputs were spot-checked against known values, and the
results they produced are recorded with their ranges in `notes/12`. They are kept
so a claim can be re-run rather than trusted.

| Script | What it searches |
| --- | --- |
| `scripts/antimagic.py` | Hartsfield–Ringel antimagic labelling, connected labelled graphs |
| `scripts/ryser_latin.py` | Ryser's conjecture, transversals in Latin squares |
| `scripts/ch_diffset.py` | circulant Hadamard matrices via difference sets |
| `scripts/graceful_trees.py` | graceful trees (Ringel–Kotzig), already settled to n ≥ 35 |

Run with `python3 -I scripts/<name>.py`. Several need `networkx`, `sympy` or
`gmpy2`; the imports at the top of each file say which.

Nothing here proves anything. A search that finds no counterexample says where a
counterexample is not, over the range it names, and nothing more.
