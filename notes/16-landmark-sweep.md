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

## Hadamard matrices — a correction to this repo's own notes

Note 15 originally repeated the standard line that 668 is the smallest undecided
order. **That is out of date**, and the correction is verified three ways:

1. **OEIS A007299** carries a comment (Bernard Schott, 12 Aug 2026) recording that
   Alpöge with Philippe Voinov, Saul Reynolds-Haertle and Claude found Hadamard
   matrices at all twelve multiples of 4 below 2000 previously without known
   examples: 668, 716, 892, 1132, 1244, 1388, 1436, 1676, 1772, 1916, 1948, 1964.
2. **The archive at `math74.com/Hadamard`** lists a construction and a PNG for every
   covered order. I downloaded `Hadamard_0668.png` (668×668, two colours, 668²
   pixels), decoded it, and checked `AAᵀ = 668·I` exactly over the integers with
   entries in `{±1}`. Both colour orientations pass, as they must. The matrix is real.
3. **The same archive** marks exactly four orders in `[2001,3000]` as
   "no construction known": **2396, 2676, 2876, 2956**, and returns 404 for
   `Hadamard_2396.png`. So the smallest open order is 2396, and 81 orders below
   10,000 remain open.

The 668 construction is `G(B(166,1))` — a Goethals-type construction on base
sequences. This matters for what comes next: `2396 = 4·599` with `599` prime and
`2395 = 5·479`, `1197 = 3²·7·19` not prime powers, so Paley and order-multiplication
cannot reach it. Only a direct sequence search can.

**This is the first thing in the sweep with real weight, and it is a correction to
us, not a result.** I was repeating a fact that had been false for three months.

## Erdős–Straus

`4/n = 1/a + 1/b + 1/c`.

**Record, corrected.** The `10^17` verification is Salez (arXiv:1406.6307, 2014), a
single-machine modular sieve, not a distributed computation as commonly stated.
A 2025 preprint (arXiv:2509.00128) claims `10^18`; wording does not settle whether
that is primes or all `n`.

**What was computed here: all `n ≤ 10^9`,** via Salez's elementary reduction (every
`n` scales to `4/(kn)`, explicit decompositions cover `n` even and three residue
classes, leaving only primes `p ≡ 1 (mod 24)`). That reduces the check to 6,354,932
primes, each receiving an exact certificate, 0 failures, largest parameter 107.
Cross-checked against an independent sieve.

Sample certificates, verified as exact integer identities:

    4/73        = 1/20 + 1/219 + 1/4380
    4/999999937 = 1/249999985 + 1/83333323083334042 + 1/17640413385549453376349299111490

**This is eight orders of magnitude below the record and is not progress.** It is a
sanity re-verification of the reduction plus a fresh run. Filed as such.

## Method notes

Two of the three outcomes above are "the method does not reach". That is the normal
shape of this exercise. The useful outputs are the reproduced values, the corrected
attributions, and the stated ceiling of each method — not the absence of
counterexamples.
