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

## Ramsey numbers — and an error of mine corrected

**Correction.** When setting this sweep up I asserted `R(3,10) = 40` as a proved
value. That is false. The current state is

    40 ≤ R(3,10) ≤ 41,

lower bound Exoo (1989), upper bound Angeltveit, *R(3,10) ≤ 41*, EJC 32(4) P4.30
(2025), arXiv:2401.00392 — improved from 42 via a search over roughly 150 billion
`R(3,8)` graphs. The exact value is open, and `R(3,10) = 40` is equivalent to the
non-existence of a triangle-free 40-vertex graph with independence number ≤ 9.
`R(3,10)` and `R(4,6)` are the two smallest unknown classical Ramsey numbers. This
is the second stale or wrong fact I brought into the sweep, after the Hadamard 668
claim, and both were caught by checking rather than by memory.

**Graphs constructed and independently verified here.** Three critical-graph
witnesses, re-checked with my own code (bitset clique number on the graph and on its
complement), not the agent's verifier:

| witness | `n` | edges | `ω` | `α` | gives |
|---|---|---|---|---|---|
| `g45_24` | 24 | 120 (10-regular, circulant `Z₂₄`, ±{1,2,4,8,9}) | 3 | 4 | `R(4,5) ≥ 25` |
| `g39_35` | 35 | 140 (8-regular, circulant `Z₃₅`, ±{1,7,11,16}) | 2 | 8 | `R(3,9) ≥ 36` |
| `g310_39_sat` | 39 | 167 (degrees 7–9, SAT-built) | 2 | 9 | `R(3,10) ≥ 40` |

`ω < s` and `α < r` in every row, so each is a valid witness. The 24-vertex graph is
Kalbfleisch's (1965); there are 352,366 critical graphs on 24 vertices. The 35-vertex
graph hits the unique critical graph for `R(3,9)`. The 39-vertex witness is not
isomorphic to Exoo's, and there are at least `43 × 10⁶` such graphs — so constructing
one is not a result, only a check that our tools work.

Exact equality needs the cited upper bounds (McKay–Radziszowski 1995, with a HOL4
formalisation; Grinstead–Roberts 1982). **No new Ramsey number is claimed.**

## Lonely runner — and a citation of mine corrected

**Correction.** I attributed the seven-runner case to Baranwal et al. (2024). That
attribution does not survive a search; the seven-runner proof is **Barajas–Serra,
EJC 15 (2008) R48**. The chain in the `N`-runner form: `N ≤ 3` elementary,
`N = 4` Betke–Wills 1972, `N = 5` Cusick–Pomerance 1984, `N = 6` Bohman–Holzman–
Kleitman 2001, `N = 7` Barajas–Serra 2008, `N = 8`–`9` Rosenfeld / Trakulthongchai
(2025), `N = 10` Trakulthongchai (EJC 2026), `N = 11`–`13` Sungkawichai–
Trakulthongchai (arXiv:2604.23906). Claims to `N = 14`–`16` exist but are arXiv or
Zenodo only and not fully audited, so they are not counted as settled here.

**What was computed.** Exact integer arithmetic throughout; for `δ = 1/Q` the safe
set is a finite union of closed intervals whose endpoints are crossings
`‖v_i t‖ = δ`, so testing `t = (mQ ± 1)/(v_i Q)` is exhaustive within a speed box.
Every distinct-speed tuple with speeds `≤ B` was enumerated for `(n,B) = (3,200)`,
`(4,120)`, `(5,80)`, `(6,60)`, `(7,50)`, `(8,50)` — 720,394,896 tuples, zero
violations. Each box constant came out exactly `1/(n+1)`, matching the theorems, and
just above it the search flags exactly the known extremal tuples, which confirms
tightness rather than testing a soft bound.

**This is not progress on the conjecture.** It is a bounded verification, and the
bounds are finite only because finite speed bounds exist (Tao 2018; Malikiosis–
Santos–Schymura 2024) and those bounds are enormous. The `N ≥ 14` status is unsettled
and this run says nothing about it.

## Caccetta–Häggkvist

**Two corrections to my framing.** I wrote that `r = 2` and `r = 3` are open. They are
not. In the form "minimum outdegree `r` forces a directed cycle of length `≤ ⌈n/r⌉`":

- `r = 1` trivial; `r ≥ n/2` trivial; tournaments trivial.
- `r = 2` is Caccetta–Häggkvist (1978) themselves.
- `r = 3` is Hamidoune (1987); `r = 4, 5` are Hoàng–Reed (1987).
- `r ≤ √(n/2)` and `n ≥ 2r² − 3r + 1` is Shen (2000).

What is open is the region `n/3 ≤ r < n/2` — equivalently the cycle-length-`k`
formulation at `k = 3`: minimum outdegree `≥ n/3` forces a triangle. I also wrote the
count of digraphs as `3^{n(n−1)}`, which is wrong twice over: all simple digraphs are
`2^{n(n−1)}`, oriented ones `3^{C(n,2)}`.

**Enumeration.** Sound reductions, each justified rather than assumed: a
counterexample is oriented (a digon is already short); deleting arcs while an
outdegree exceeds `r` leaves a spanning subgraph with every outdegree exactly `r` and
creates no new cycles; so exact-`r` digraphs suffice. DFS over exact-`r`
out-neighbourhoods with a sound pruning rule — close a short cycle and every
completion contains it.

| `r` | `n = 7` (full, unpruned) | `n = 8` | `n = 9` | counterexamples |
|---|---|---|---|---|
| 2 | 170,859,375 | 3.8×10¹⁰ | 1.06×10¹³ (mod relabelling) | 0 |
| 3 | 1.28×10⁹ | 2.25×10¹² | 5.4×10¹⁵ (mod relabelling) | 0 |

The maximum girth came out exactly `⌈n/r⌉` in every case — the search proves `≤` and
the circulant `C_n(1..r)` attains it — so the bound is tight, which is a check on the
implementation and not a new fact.

**Scope.** Full unpruned enumeration for `r = 2, 3` through `n = 7`; sound exhaustive
certification through `n = 9`. The open frontier starts near `n = 18`, `δ⁺ = 6`
(combining `r ≤ 5` with the 0.3465 triangle threshold), so this is nowhere near it.
No counterexample, and none expected.

## Erdős–Gyárfás

Every graph with minimum degree `≥ 3` contains a cycle whose length is a power of 2.

**Published range, with a caveat.** The best figures found are all graphs of order
`≤ 40`, cubic graphs `≤ 48`, bipartite `≤ 66` — but these come from a September 2026
preprint (Ducoffe–Dumitru, arXiv:2609.28594) echoed by MathWorld, and **no
peer-reviewed publication of those bounds could be confirmed**. Earlier computational
lineage is solid: Markström (2004) showed a cubic counterexample needs `≥ 30` vertices
and exhibited the four 24-vertex cubic graphs whose only power-of-2 cycle length is
16; Aldred–Royle ran the cubic census to `n = 34`; Royle–Markström gave `≥ 17` in
general. So even the "published range" for this conjecture is softer than it looks.

**What was verified here: all connected graphs with `δ ≥ 3`, orders `4 ≤ n ≤ 11`.**
Connected is enough — a disconnected `δ ≥ 3` graph has a `δ ≥ 3` component.

| `n` | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 |
|---|---|---|---|---|---|---|---|---|
| graphs | 1 | 3 | 19 | 150 | 2,589 | 84,242 | 5,203,110 | 577,076,528 |

Total 582,366,642 graphs, **0 counterexamples**. Counts match OEIS A007112 exactly,
which is the check that the enumeration is complete; the cycle detector was
cross-checked against an independent implementation on every graph to `n = 8` and on
controls — it correctly rejects `C₃, C₅, C₁₀` and accepts `C₄, C₈, C₁₆, K₄`,
Petersen, `K₃,₃`. The `n = 11` pass took 298 s.

Cubic graphs separately to `n = 20` (matching OEIS A002851), 0 counterexamples — but
this is a strict subset and does **not** extend the `δ ≥ 3` range, since "reduce to
cubic" holds only for regular minimal counterexamples.

**Scope.** Order `n` proves the statement for order `≤ n` and nothing beyond. The
published bound is 40; `n = 12` alone has 113,373,005,661 such graphs, so this run
reaches a small fraction of what is already known. It validates the pipeline and adds
no coverage.

## Ramsey `R(5,5)` — a third stale fact of mine

**Correction.** I gave the range as `43 ≤ R(5,5) ≤ 48`. The upper bound has moved
twice since that number: Angeltveit–McKay improved 49 → 48 (J. Graph Theory 89(1),
2018) and then 48 → **46** (arXiv:2409.15709; J. Graph Theory 112(3):198–208, 2026,
DOI 10.1002/jgt.70029), by linear programming plus a case analysis whose replication
reportedly cost ~50 CPU-years. The standing range is

    43 ≤ R(5,5) ≤ 46.

That is the third fact in this sweep that was simply out of date when I asserted it,
after Hadamard 668 and `R(3,10) = 40`.

**Certificate verified here.** Record 0 of McKay's archive `r55_42some.g6` — 328
explicit `(5,5;42)` graphs, the other 328 being their complements. I decoded the edge
list and checked it with my own bitset clique code, independent of the agent's three
verifiers:

| `n` | edges | degrees | `ω` | `α` |
|---|---|---|---|---|
| 42 | 425 | 19–22 | 4 | 4 |

`ω = 4 < 5` and `α = 4 < 5`, so this is a genuine `(5,5)`-graph on 42 vertices and
`R(5,5) ≥ 43`. The graph has trivial automorphism group.

**Structural work, which is not a bound.** Extending a `(5,5;n)`-graph to `n+1` is
equivalent to choosing a neighbourhood `N(v)` that is `K₄`-free with `V∖N(v)` free of
independent 4-sets; that encoding was validated on controls where the answer is known.
All 328 archive graphs — hence all 656 up to complementation — are non-extendable to
43, with four independent SAT solvers agreeing. **This does not prove `R(5,5) ≤ 43`**,
because other 42-vertex graphs are not excluded.

No circulant `C_N(S)` for `N = 42…48` witnesses the property either. SAT at `n = 43`
(903 variables, 1.93×10⁶ clauses) timed out at 17 min, and timeouts prove nothing.
**The range is unchanged by this work.**

## Method notes

Two of the three outcomes above are "the method does not reach". That is the normal
shape of this exercise. The useful outputs are the reproduced values, the corrected
attributions, and the stated ceiling of each method — not the absence of
counterexamples.
