# Counterexample hunting: a record of what survived and what did not

A conjecture that can be tested by finite search is a conjecture that can be
killed. Killing one is a result; failing to kill one over a stated range is also
a result, and both are worth recording precisely.

**Method.** For each target: state the conjecture exactly with its source, write a
small program, verify the program reproduces known terms before testing anything,
search exhaustively over a named range, and report either a printed witness or a
null result with the range. A program that emits a false counterexample is worse
than no program, so every claimed witness is re-run by hand before it is recorded
here.

## 1. OEIS conjectures

Four conjectures attached to OEIS entries, all still standing over the ranges
searched. This section is a record of survival, which is the honest outcome for
conjectures that have already survived some attention.

### A000172 — Franel numbers

`a(n) = Σ_k C(n,k)³`, with the recurrence
`(n+1)² a(n+1) = (7n²+7n+2) a(n) + 8n² a(n−1)`.

**Conjecture** (Detlefs, 2013): a(n) ≡ 2 (mod n³) **iff** n is prime. The forward
direction, prime ⇒ congruence, is proved (Z.-W. Sun). The converse is open.

**Result: survives.** Searched n = 2..200000. Every prime satisfies the
congruence, and no composite does — including the base-2 Fermat pseudoprimes
1093 and 3511 and the base-2 Wieferich prime 16843, which is the sort of n most
likely to break it.

**Independently reproduced** at n ≤ 30000 during the audit of this record, with a
separately written program: zero anomalies.

### A219197

**Conjecture** (Hanna): a(n) is never congruent to 3 mod 4.

**Result: survives** for n = 0..50000, using Kotesovec's exact three-term
recurrence, with the computed terms matched against OEIS before testing.

### A237656 — a prime-counting residue system

`a(n)` is the least m such that {π(k²) : k = 1..m} is a complete residue system
mod n.

**Conjecture** (Z.-W. Sun): a(n) is always positive, and a(n) < 2·p(n+1) − 2 for
n > 0, where p is the nth prime.

**Result: survives** for n = 1..150, with the search cap m ≤ 2000 exceeding every
bound tested. `a(5) = 8 < 24` checked by hand: the residues π(k²) mod 5 for
k = 1..8 are 0, 2, 4, 1, 4, 1, 0, 3, which covers all five classes.

### A307532 — primality of a minimal exponent

**Conjecture**: a(n) is prime for all n ≥ 0, where a(n) is the least
k > 2^(2ⁿ) + 1 with k ≡ 1 (mod 2ⁿ) and 2^(k−1) ≡ 1 (mod (2^(2ⁿ) − 1)·k).

**Result: survives** to n = 12, four terms beyond those listed in OEIS, with
primality by BPSW. The minimal m values found (202, 56, 304, 635) independently
match the m-list in the OEIS remark, which is a useful cross-check that the search
is finding the intended objects and not merely some strong pseudoprime.

**Limit worth stating.** n ≤ 12 is a narrow range, and a primality conjecture
that holds to n = 12 is weak evidence. This one is recorded for completeness, not
as a meaningful test.

## 2. Antimagic conjectures in graph theory

Three open conjectures, all searched over every graph in a range, with a verified
witness produced for every graph where the conjecture predicts one. Method: local
search for a witness, then an exact independent verifier — so "no failure" always
means an explicit certificate was checked, never merely that the search gave up.

### Hartsfield–Ringel edge-antimagic

Every connected G ≠ K₂ admits a bijection f : E(G) → {1,…,m} with pairwise
distinct vertex sums σ(v) = Σ_{e ∋ v} f(e). Source: *Pearls in Graph Theory*
(1990); Gallian's Dynamic Survey DS6. The K₂ exception is genuine — its single
labeling gives both endpoints the same sum.

**Result: no counterexample**, across all 273,193 connected unlabelled graphs on
at most 9 vertices (996 of order ≤7, 11,117 of order 8, 261,080 of order 9). Every
graph received a verified witness.

### Hefetz–Mütze–Schwartz antimagic orientation

Every connected G has an orientation D and a bijection on its arcs with pairwise
distinct in-sums. Source: *J. Graph Theory* 64 (2010), Conjecture 1.1.

**Result: no counterexample** over the same 273,193 graphs, jointly searching
orientations and labelings.

### D-antimagic with D = {1}

A bijection f : V(G) → {1,…,n} with pairwise distinct weights
ω(v) = Σ_{u ∈ N_D(v)} f(u), where N_D(v) is the set of vertices at distance in D.
Conjecture: such an f exists **iff** no two vertices have equal D-neighbourhoods.
Source: Simanjuntak et al., *Symmetry* 13(11):2071 (2021).

**Result: no counterexample** across all 288,266 unlabelled graphs of order at
most 9, connected and disconnected. This is the only entry in this section that
extends a published check rather than reproducing one: the paper's verification
reaches order 8, and this reaches order 9. That is a small increment, not a
resolution, and the claim about the paper's range is taken from its own
description.

The twin-containing cases are not searched — two vertices with equal
D-neighbourhoods necessarily have equal weights, so the conjecture predicts no
labeling and there is nothing to find. The 2,218,478 twin-free connected
9-vertex instances all received verified labelings.

**Checks performed during the audit of this record.** The counts were recomputed
independently and match exactly: 996 + 11,117 + 261,080 = 273,193 connected
graphs on ≤9 vertices, and 274,668 − 261,080 = 13,588 disconnected graphs of
order 9, giving 288,266 in total. The quoted K₉ witness for D = {1} was verified
by hand: on a complete graph the weight is the total label sum minus the vertex's
own label, so labels 6,3,5,4,8,2,7,9,1 give weights 39,42,40,41,37,43,38,36,44,
which are distinct.

## What this section is not

None of these is evidence for the conjectures in any mathematical sense. A
congruence holding to 2·10⁵ is consistent with a counterexample at 2·10⁵ + 1, and
several famous conjectures have died far beyond their first computational check.
The value of the record is the opposite direction: it tells you where a
counterexample, if one exists, does *not* live, and it fixes the exact programs
and ranges so the claim can be re-run rather than trusted.
