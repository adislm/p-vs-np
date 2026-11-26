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
| `scripts/spec.py`, `scripts/energy.py` | spectral and positive-square-energy conjectures, all connected graphs |
| `scripts/dom2.py` | total domination vs the annihilation bound |
| `scripts/tree6b.py`, `scripts/verify_hp.py` | tree inequalities and witness verification |
| `scripts/oeis_cub2.py` | A375785, integer cuboids with surface 6n² |
| `scripts/oeis_perm.py` | A397619, permutations with prime adjacent products |
| `scripts/oeis_primedfs2.py` | A392666, sign conjecture for a triangle recurrence |
| `scripts/cow_steady_table.py` | steady-word table for arXiv:2209.08507 |
| `scripts/cow_steady_lists.py` | the size-4 list conjecture |
| `scripts/cow_bifurcate.py` | bifurcate chains and complete trees |

Run with `python3 -I scripts/<name>.py`. Several need `networkx`, `sympy` or
`gmpy2`; the imports at the top of each file say which.

Nothing here proves anything. A search that finds no counterexample says where a
counterexample is not, over the range it names, and nothing more.
