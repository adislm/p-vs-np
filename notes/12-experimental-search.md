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

## A falsified conjecture — arXiv:2604.23188, Conjecture 4

This is the one positive result of the exercise: a conjecture stated in April 2026
that is false as written, with a one-word counterexample.

**Source.** Fazekas, Mammoliti, Mercaş and Simpson, *Binary Words Containing Few
Abelian Squares*, arXiv:2604.23188v1 (25 April 2026).

**The conjecture, verbatim** from the paper:

> **Conjecture 4.** A binary word of length n contains at least ⌊n/4⌋ abelian
> squares and if it contains exactly ⌊n/4⌋ abelian squares then all the abelian
> squares are trivial.

where an abelian square is a factor uv with u and v having the same letter counts,
and — the paper's own definition — an abelian square of the form a^{2i} or b^{2i}
is **trivial**.

**Counterexample.** w = `abab`, with n = 4 and ⌊n/4⌋ = 1.

- The factor `abab` equals (ab)(ab), and `ab` and `ab` have equal letter counts, so
  it is an abelian square. Its half contains both letters, so it is **not**
  trivial.
- Every even-length factor of `abab` is one of: length 2 — `ab`, `ba`, `ab`; none
  is an abelian square, since a length-2 abelian square would need its two single
  letters to be equal; length 4 — `abab` only.
- Hence θ(`abab`) = 1 = ⌊n/4⌋, the antecedent of the second clause holds, and the
  conclusion "all the abelian squares are trivial" fails.

The count is 1 whether θ is read as occurrences or as distinct factors, so the
counterexample does not depend on that ambiguity.

**The paper contradicts itself.** Its own table of minimum values lists

    n   Number   Words achieving this
    4   1        abab, baba

so `abab` and `baba` are the paper's own minimisers at n = 4, and they are exactly
the words that break clause 2. The likely intent was n ≥ 5; for 5 ≤ n ≤ 46 no
word with θ = ⌊n/4⌋ has a non-trivial abelian square.

**Verification performed.** The conjecture statement and the definition of
"trivial" were extracted from the paper's HTML full text, not from a summary. All
arXiv identifiers in this document were resolved against the arXiv API. The
witness was checked clause by clause by hand.

**What this is and is not.** It is a genuine defect in an unrefereed preprint,
found by exhaustive search and confirmed by the paper's own data. It is not a deep
result and it does not affect the paper's main theorems. The honest description is
that clause 2 needs the qualifier n ≥ 5.

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

## 3. Number theory: three under-tested conjectures

All three survived. Each program reproduces the OEIS terms before searching, and
the π computation was cross-checked against an independent implementation.

| Conjecture | Source | Range | Result |
| --- | --- | --- | --- |
| (least prime > n²) − n² ≤ 1 + φ(n), a strengthening of Oppermann | OEIS A053000, Luo 2023 | n ≤ 10⁷ | survives; equality only at n = 12, 18, 42 |
| no prefix of the decimal expansion of π is a perfect square | OEIS A011545, Haken 1977 | n ≤ 10⁶ digits | survives |
| a(n) > 0 for all n > 1, where a(n) counts k < n with equal prime counts in consecutive length-n intervals | OEIS A238281, Sun 2014 | n ≤ 20 000 | survives; extends the tabulated n ≤ 5000 |

**The Luo case is the most one-sided.** The largest value of the gap found was
541, at n = 4 292 936, where 540 consecutive composites follow n². The bound
1 + φ(n) at that n is 1 995 841, a slack of roughly two million. The conjecture
holds with enormous room throughout the range, which makes it survivable by a
wide margin and correspondingly hard to falsify.

**The Haken case** is a striking statement — no prefix of π's decimal expansion is
a perfect square — and it held to a million digits. A necessary-condition filter
on quadratic residues reduced a million exact square tests to 352 candidates, with
a positive control confirming that no genuine square could be filtered out.

**One limit worth stating.** The A238281 result extends a tabulated range rather
than opening new ground, and the extension is by a factor of four.

## 4. Combinatorial designs: re-verifications, not new ground

Recorded for completeness and explicitly *not* as results.

- **Antimagic labelling (Hartsfield–Ringel).** All 1,893,731 connected *labelled*
  graphs on 2 to 7 vertices were searched by exhaustive backtracking; the only
  non-antimagic graph is K₂, the conjectured exception. This is an independent
  re-derivation by a different route from the unlabelled search in §2, and the two
  agree.
- **Ryser's conjecture** (every odd-order Latin square has a transversal).
  Exhaustive for n = 3 and n = 5 using the fact that transversal existence is
  isotopy-invariant; randomised for n = 7 and n = 9. The literature already covers
  n ≤ 9, so this is a re-verification.
- **Circulant Hadamard matrices.** The difference-set search recovered the order-4
  case and timed out at order 36. Logan–Mossinghoff settle the question to
  n ≤ 4·10³⁰, so nothing here is open at any computable range.

The value in this section is the negative kind: it confirms that the search
apparatus agrees with known results, which is what makes the null results in §1–3
worth recording at all.

## What this section is not

None of these is evidence for the conjectures in any mathematical sense. A
congruence holding to 2·10⁵ is consistent with a counterexample at 2·10⁵ + 1, and
several famous conjectures have died far beyond their first computational check.
The value of the record is the opposite direction: it tells you where a
counterexample, if one exists, does *not* live, and it fixes the exact programs
and ranges so the claim can be re-run rather than trusted.
