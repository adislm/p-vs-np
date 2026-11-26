# 16 — Landmark-problem sweep

Companion to note 15. Targets are named open problems, not recent preprints. The
expected outcome is a null result; what is recorded here is the *verified range* and
any correction to the literature, since those are the things that are actually true
afterwards.

Every certificate is checked by `tools/verify_cert.py`, written independently of the
code that produced it.

---

## Schur numbers

`S(r)` = largest `n` with a colouring of `[1,n]` by `r` colours avoiding a
monochromatic `x + y = z`.

Independent implementation, plain DFS with the colour-ordering symmetry break
(colours introduced in order of first appearance; `col(1) = 0`):

| `r` | claimed `S(r)` | `[1,S]` feasible | `[1,S+1]` infeasible |
|---|---|---|---|
| 3 | 13 | yes | yes |
| 4 | 44 | yes | yes |
| 5 | 160 | **not found** | — |

Both known values reproduce on both sides, so the implementation is sound. The
`S(4)=44` infeasibility took 2.2×10⁸ nodes / 14 s; the unsymmetrised version took
1.3×10⁹ nodes / 20 s, so the symmetry break buys a factor of six and no more.

`S(5) = 160` is **not reachable by this method**: 15 minutes of DFS on the feasible
side found no colouring. Heule's proof used SAT with cube-and-conquer, and that is
the only method that scales here. Recording the failure is the point — it fixes the
method's ceiling at `r = 4` and says not to spend more compute below it.

---

## Rota's basis conjecture (1989)

`n` pairwise disjoint bases of a rank-`n` matroid, arranged as rows, every column a
basis.

**Status, checked against the literature rather than memory.** `n = 2` is basis
exchange; `n = 3` is Chan (1995). `n = 4` is *settled*: Cheung (2012, rank ≤ 4) and
independently Kirchweger–Scheucher–Szeider (SAT 2022) with machine-checkable DRAT
proofs for all matroids of rank 4. `n = 5` is open — KSS cover only special cases of
rank 5, and the record through 2026 has no general proof. Graphic matroids are open;
Maezawa–Yazawa (2022) give star colour classes and series-parallel follows from Wild
(1994).

Two attributions in circulation are wrong and are corrected here:

- Strongly base-orderable matroids: **Wild (1994)**, not Aharoni–Berger.
- Geelen–Humphries (2006) is the *paving* case, not the unimodular case. Unimodular
  has no general theorem; since graphic ⊂ regular and graphic is open, the regular
  case must be open too.

**Computation.** Exhaustive DFS over column assignments, pruning only failed
prefixes, so an infeasible input is exhausted. A deliberately impossible control
returns "none", which validates the search.

- `n = 3`: 1,502 instances (uniform, four fields, graphic, Pappus). All arrange.
  `U(3,9)` fully enumerated: 216/216 assignments valid.
- `n = 4`: 801 instances. All arrange. `U(4,16)` fully enumerated: 331,776/331,776
  valid, matching the predicted count.
- `n = 5` (the open case): 600 random rank-5 linear matroids over GF(2), GF(3),
  GF(5). All arrange.

Totals: 2,903 instances, 0 failures; a second seed reproduces 2,903/2,903.

**This proves nothing about the conjecture, and the `n ≤ 4` part could not have
proved anything** — those ranks are theorems, so a failure there would have been our
bug. The `n = 5` sample is the only part touching an open case, and random instances
are the easy ones: a serious attack needs an adversarial rank-5 construction, not
more random sampling. That is the honest limit of this result.

---

## Method notes

Two of the three outcomes above are "the method does not reach". That is the normal
shape of this exercise. The useful outputs are the reproduced values, the corrected
attributions, and the stated ceiling of each method — not the absence of
counterexamples.
