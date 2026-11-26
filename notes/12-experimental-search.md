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

**Adversarial check.** A separate process was given the counterexample and told to
refute it. It upheld the claim, having confirmed from the source that

- Conjecture 4 carries no `n ≥ 5` or "large n" qualifier;
- "trivial" is defined exactly as above, and `abab` is neither a^{2i} nor b^{2i};
- θ counts all abelian squares, trivial and non-trivial together, and for `abab`
  the count is 1 whether taken over occurrences or distinct factors;
- Table 1's caption reads "Length n words containing two a's and the least
  possible number of distinct abelian squares", and its n = 4 row gives
  `abab, baba`.

The strongest corroboration is internal: the paper's Theorem 7 concerns exactly
the two-a case and its M(2,4) computation agrees that `abab` has one abelian
square, which is the non-trivial square `abab` itself. Three separate routes —
the table, the theorem, and direct enumeration — all certify θ(`abab`) = 1.

**How narrow the defect is.** Exhaustive enumeration of all binary words for
n ≤ 16 — independently re-run during this audit with a separately written
program — shows n = 4 is the *only* failure, with exactly two words failing,
`abab` and `baba`. So the correction is a single missing hypothesis, and the
statement was almost certainly intended as n ≥ 5. That is worth stating plainly:
this is a precise, small, verifiable defect, not a crack in the paper's substance.

**What this is and is not.** It is a genuine defect in an unrefereed preprint,
found by exhaustive search and confirmed by the paper's own data. It is not a deep
result and it does not affect the paper's main theorems. The honest description is
that clause 2 needs the qualifier n ≥ 5.

## A second defect in the same paper: Theorem 6 is false

Auditing the rest of arXiv:2604.23188 after the Conjecture 4 finding turned up a
more serious problem. This one is a **theorem**, not a conjecture.

**Theorem 6, verbatim:** "For positive integers n we have M(1, n) = ⌊n/4⌋. The
only words with one a and exactly M(1, n) abelian squares are
b^{⌈(n−1)/2⌉} a b^{⌊(n−1)/2⌋} and its reverse."

**The value is right; the characterisation is not.** At n = 5, take
`babbb` = b¹ab³, or its reverse `bbbab` = b³ab¹. Each has exactly one `a`, and its
only distinct abelian-square factor is `bb`, so θ = 1 = M(1,5). The claimed words
are `bbabb` = b²ab² and its reverse, and `babbb` is neither.

**The failure has a clean pattern.** It occurs at n = 4, 5, 8, 9, 12, 13 — that
is, for every n ≡ 0 or 1 (mod 4) — and does not occur at n = 6, 7, 10, 11, 14.
At n = 4 the additional minimisers are `abbb` and `bbba`. The value M(1,n) = ⌊n/4⌋
appears to be correct throughout; what fails is the claim that the two symmetric
words are the only minimisers.

**The convention matters and is pinned by the paper itself.** Counting
occurrences rather than distinct factors would give θ(`bbabb`) = 2, since `bb`
occurs twice, contradicting the paper's own M(1,5) = 1. So the paper's tables
force the distinct-factor reading, and under that reading the counterexample is
sound.

**Verification.** Computed independently during this audit with a separately
written enumerator: all binary words at each n, θ by exhaustive factor
enumeration, minimisers compared against the claimed two. The pattern above
reproduces exactly. Two bugs in the first version of that enumerator were found
and fixed before the result was accepted — worth recording, because the first
version appeared to confirm and deny the finding in turn.

### The repair

A refutation is worth less than a correction, so here is the corrected
characterisation. Write a one-`a` word as `b^i a b^(n−1−i)`, so the position `i`
determines the word. Then the minimisers are exactly

    2⌊n/4⌋ − 2 + (n mod 4)  ≤  i  ≤  2⌊n/4⌋ + 1

a block of `4 − (n mod 4)` consecutive positions. Equivalently, the number of
minimisers is `4 − (n mod 4)`: four when n ≡ 0, three when n ≡ 1, two when n ≡ 2,
one when n ≡ 3.

The paper's two words are `i = ⌈(n−1)/2⌉` and `i = ⌊(n−1)/2⌋`, the two central
positions. Those lie inside the block — which is exactly why they are minimisers
and exactly why the claim that they are the *only* ones is false. The theorem is
not off by a correction term; it undercounts a block that always contains the
positions it names.

**This is proved, not merely observed.** The argument is short.

*Lemma.* If w = b^i a b^j with i + j = n − 1, then θ(w) = ⌊max(i,j)/2⌋.

*Proof.* Every factor of w containing the single `a` contains exactly one `a`. An
abelian-square factor uv has halves with equal multisets, hence equal `a`-counts;
those counts sum to the factor's `a`-count, which is 1 — impossible. So no
abelian-square factor contains the `a`. The abelian squares of w are therefore
exactly the factors b^{2p} with 2p ≤ max(i,j): the run of max(i,j) consecutive
`b`s contains each of them, and b^{2p} ≠ b^{2q} for p ≠ q. There are
⌊max(i,j)/2⌋ of them. ∎

*Corollary.* Minimising max(i, n−1−i) over i + j = n − 1 gives ⌈(n−1)/2⌉, so
M(1,n) = ⌊⌈(n−1)/2⌉/2⌋, which is ⌊n/4⌋ by the paper's own identity. The
minimisers are the i with max(i, n−1−i) ∈ {2M, 2M+1} for M = ⌊n/4⌋. Now
max ≤ 2M+1 holds exactly when i ≥ n−2M−2, while max ≥ 2M is automatic: if both
i and n−1−i were at most 2M−1 then n−1 ≤ 4M−2 < 4M ≤ n, a contradiction. So the
minimiser set is the interval [n−2M−2, 2M+1]. Writing n = 4M + r with 0 ≤ r ≤ 3,
its lower end is 2M+r−2, and it contains 2M+1−(2M+r−2)+1 = 4−r positions. ∎

The lemma and the resulting block were also checked by brute force for every n
below 60, with no mismatch — a check on the proof's arithmetic, not a substitute
for it.

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

## 1b. OEIS conjectures, second batch

Three entries added in 2024–2026, so newer and less tested than the first batch.
Each sequence was computed from its defining object or recurrence — never from the
conjectured property — and the published terms were reproduced before any test.

| Entry | Conjecture | Published check | Range reached | Result |
| --- | --- | --- | --- | --- |
| A375785 | every term is odd (integer cuboids with surface 6n²) | 36 terms | n ≤ 2000 | survives |
| A397619 | a(n) > 0 (permutations with p(i)p(i+1)+1 prime) | n ≤ 27 | n ≤ 200 | survives |
| A392666 | T(n,k) ≥ 0 for even n | even n ≤ 400 | even n ≤ 6000 | survives |

**The middle one has an argument attached, not just a search.** For a permutation
of [n], two adjacent odd values would give odd·odd + 1, which is even and exceeds
2 unless both values are 1 — impossible in a permutation, since 1 occurs once.
So no two odd values are adjacent, the ⌈n/2⌉ odd values form an independent set
of the n-vertex path, and every valid permutation must alternate odd and even.
The search then only has to find one alternating arrangement for each n, which it
does for every n ≤ 200. That converts a long computation into a short structural
reduction plus a small search, and it is why this entry survives with more
confidence than a bare enumeration would give.

**A392666 is the largest range extension here** — fifteen times the author's
stated check. The triangle row n = 10 was re-derived independently during this
audit: 1, 104849, 45588716, 925915724, 3563737526, 3563737526, 925915724,
45588716, 104849, 1, matching the published row exactly.

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

## 3b. Number theory, second batch

Three more recent conjectures, again all surviving. Identifiers resolved and one
recurrence independently reproduced during the audit.

| Conjecture | Source | Range | Result |
| --- | --- | --- | --- |
| t(n) ≥ 2 for every n, where t(n) counts "Toda primes" | arXiv:2511.19744 (Nov 2025) | n ≤ 10⁷ | survives; minimum is 2, attained at n = 1, 2, 5, 17, 19, 31, … |
| four Ramanujan-type congruences for overpartitions, mod 7, 17, 19 and 23 | arXiv:2603.08510 (Mar 2026) | every index ≤ 4.1×10⁶ | survives; zero failures |
| if S(q) ≠ ∅ for an odd prime q then some prime p ≡ 1 (mod q) has z(p) | π(q) | arXiv:2604.17847 (Apr 2026) | not finitely falsifiable — see below |

**The Toda count has a structural explanation for surviving.** For prime n ≥ 7 one
can prove t(n) ≥ 2 outright, so any failure would have to be composite; none
occurs to 10⁷.

**The overpartition congruences were checked against three independent
computations.** The sequence p̄ was produced by the paper's identity
Σ p̄(n)qⁿ = 1/φ(−q), giving the recurrence
p̄(n) = 2·Σ_{k=1}^{⌊√n⌋} (−1)^{k+1} p̄(n − k²); by exact generating-function
expansion; and by brute-force enumeration. All three agree. The recurrence was
independently re-implemented during this audit and reproduces the published values
p̄(0..15) = 1, 2, 4, 8, 14, 24, 40, 64, 100, 154, 232, 344, 504, 728, 1040, 1472
exactly. The paper's two *proved* congruences (mod 11 and mod 13) were also
verified, which is the useful control: it shows the machinery finds the
congruences that are known to be there.

**The third is not a falsification test, and the agent said so unprompted.** Every
certificate of S(q) ≠ ∅ that a finite search can build — a prime ℓ ≡ 1 (mod q)
with z(ℓ) | π(q) — *is itself* the witness p the conjecture asks for. A genuine
counterexample would need S(q) to be non-empty only via a covering by several
distinct primes, which no finite computation certifies. What was done instead is
honest and weaker: the paper's Table 1 was reproduced row for row, and its
corroborating count extended from q ≤ 50 000 (669 Sophie Germain primes, 160
satisfying the condition, 23.9%) to q ≤ 10⁶ (7 745 primes, 1 880 satisfying,
24.3%). That is an extension of evidence, not a test.

## 2b. Recent graph theory, exhaustive to ten vertices

Three conjectures from 2025–2026, each checked against **every** connected graph
on at most ten vertices — 11,989,764 graphs, with 11,716,571 of them at n = 10
alone. Generation was exhaustive and unlabelled (nauty `geng`); nothing was
sampled.

**Validation first.** The enumeration reproduces A000088 (all graphs, n ≤ 9) =
1, 2, 4, 11, 34, 156, 1044, 12346, 274668 and A001349 (connected, n ≤ 10) =
1, 1, 1, 2, 6, 21, 112, 853, 11117, 261080, 11716571 exactly. Spectral ranks from
`numpy.eigvalsh` matched exact sympy ranks on 1,500 random 10-vertex graphs, and
the domination routine matched brute force on every connected graph of order ≤ 8.
That is what makes the null results worth recording.

| Conjecture | Source | Result |
| --- | --- | --- |
| connected G with m ≥ n+1 has positive square energy s⁺(G) ≥ n | arXiv:2506.07264, Conj 1.2 | survives; minimum slack 0.698 |
| every connected graph has λ₂ ≤ μ₁ − 2 | arXiv:2611.03879, Conj 2 (#20829) | **FALSE at n = 11** — see below |
| γ_t(G) ≤ a(G) + 1 for connected G with an edge | arXiv:2609.10795 (δ ≥ 2 case proved; δ = 1 open) | survives; sharpness witness found |

**These extend published checks by one order, which is the honest size of the
result.** The authors of the energy conjecture verified n ≤ 9; this reaches
n = 10. The spectral corpus tested n ≤ 9 and explicitly extended only its
Conjectures 1 and 7 to n = 10; this extends #20829. The domination paper settles
δ ≥ 2 and leaves δ = 1, which is what was searched here. None of that is a
resolution; all of it is the first order beyond where the authors stopped.

### Correction: the spectral conjecture is false at n = 11

The row above first read "survives; minimum slack 0.0374". That is correct for
n ≤ 10 and wrong as a summary, and the near-zero slack at n = 10 was the warning.

`AmirMakir/broken-conjectures` reports a counterexample on 11 vertices: two
copies of K₄ − e joined tip to tip by a path with three inner vertices, G(4,3).
**Verified independently here, exactly**, by rebuilding the graph from that
description and computing eigenvalues symbolically with sympy:

- the adjacency spectrum begins 2.675131, 2.641186, 1.539189, …, so
  λ₂ = 2.641186476…;
- the Laplacian characteristic polynomial factors as
  λ(λ−4)²(λ²−7λ+11)(λ²−4λ+2)(λ⁴−9λ³+25λ²−22λ+2), so the largest Laplacian
  eigenvalue is μ₁ = (7+√5)/2 and μ₁ − 2 = (3+√5)/2 = 2.618033988…;
- therefore λ₂ − (μ₁ − 2) = 0.02315… > 0.

So Conjecture 2 of arXiv:2611.03879 is **false**, and n = 11 is where it dies.

This is the correct outcome for an exhaustive search to record, and the lesson is
worth stating: *surviving all graphs on ≤ 10 vertices is not evidence of truth*.
The search was sound and its range was stated; the conclusion drawn from it was
too strong. A minimum slack of 0.037 at the boundary of a finite search is a
signal to extend the range, not to record survival.

**A sharpness witness, checked by hand during this audit.** For the total
domination–annihilation conjecture, take the 9-vertex graph with edges
(0,5), (0,8), (1,6), (1,8), (2,6), (3,7), (3,8), (4,7). Its degree sequence is
1,1,1,2,2,2,2,2,3, so m = 8 and a(G) = 5 (prefix sums are 1,2,3,5,7, then 9 > 8).
The set {0,1,3,6,7,8} is total dominating, so γ_t ≤ 6. For the lower bound: the
leaves 5, 2 and 4 force 0, 6 and 7 into any total dominating set, and each of
those then still needs a neighbour in the set, so |D| ≥ 6. Hence γ_t = 6 = a + 1
and the +1 cannot be removed. Verified independently here, not taken on report.

## 3c. Combinatorics on words

Three open conjectures and one open problem, all from Dębski–Grytczuk–Pawlik,
*Extensions and reductions of square-free words*, arXiv:2209.08507, published in
Discrete Mathematics 347(3):113825 (2024). All null results over exhaustive,
deterministic ranges.

**Table 1 was reproduced in full before anything was tested** — the number of
quaternary steady words of length n up to symbol permutation, for every n from 3
to 32: 1, 2, 3, 5, 5, 7, 9, 12, 16, 21, 28, 37, 45, 58, 73, 93, 101, 124, 150,
179, 216, 257, 309, 376, 453, 551, 662, 798, 957, 1149. The paper's worked
verdicts on individual words also match. This is the check that makes the rest
worth reading.

| Statement | Range | Result |
| --- | --- | --- |
| every sequence of n size-4 lists admits a steady word | all 4-lists from a 5-letter universe, n ≤ 10 (1,953,125 cases); 6-letter universe, n ≤ 7 (11,390,625) | survives |
| there is an infinite chain of quaternary bifurcate words, each a one-letter extension of the last | all bifurcate words over 4 letters, length ≤ 13 | survives — chains exist at every length 1..13 |
| there is a complete bifurcate tree over 5 letters | exact recursive criterion to depth 12 | survives to depth 12; depth 13 unresolved |
| the analogous statement for size-3 lists | all 3-lists from a 4-letter universe, n ≤ 12 (4,194,304); 5-letter universe, n ≤ 8 (10,000,000) | survives |

**The informative datum is a threshold, not a null result.** Under the same
recursive completeness test, complete bifurcate trees over **4** letters die at
depth 4 — consistent with Theorem 7 of the paper, which proves no such tree
exists — while over **5** letters they survive past depth 12. That reproduces
empirically the conjectured minimal alphabet of 5, which the paper proves only
for a different parameter. The control case is what gives the 5-letter result
meaning: the same code fails at 4, so it is not simply never failing.

**The chain witness was verified independently here.** The claimed chain
`3, 23, 123, 0123, 10123, 310123, 1310123, 01310123, 301310123, 1301310123,
31301310123, 231301310123, 1231301310123` was checked for both properties: every
word is square-free, and each is the previous with exactly one letter inserted.
Both hold.

**Caveats stated by the search.** For the list conjecture the universe of symbols
is bounded, so arbitrary alphabets are not excluded. For the tree conjecture,
depth 13 hit a 3,000,000-state cap and is genuinely unresolved rather than
survived.

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
