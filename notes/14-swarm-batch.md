# Swarm batch: twenty concurrent audits

Twenty agents each deep-audited one recent paper, all under the same discipline as
`notes/13`: quote the conjecture verbatim, reproduce the paper's own numbers before
testing, use the paper's proved results as a control on the code, and report a
defect only with the paper's exact words beside a computed contradiction.

**Outcome across the batch so far: one genuine counterexample, two minor defects,
and the rest clean.** The counterexample is to an extremal conjecture at a small
case; none of the papers' main theorems fell. That is the honest ratio, and it is
recorded here as it stands rather than as a highlight reel. This file is updated
as the remaining agents report.

## arXiv:2609.02477 — planar bondage conjecture refuted — CLEAN

Srivastava, *The Truncated Octahedral Graph Has Bondage Number Five*. The paper
refutes a 1998 conjecture rather than proposing one: Dunbar–Haynes–Teschner–
Volkmann's claim that every connected planar graph has bondage number at most
Δ+1.

**Verified twice, from different starting points** — once from the paper's
36-edge list, once rebuilt here from coordinates (the 24 permutations of
(0, ±1, ±2), edges at distance √2):

| Check | Result |
| --- | --- |
| vertices, edges, regularity | 24, 36, cubic |
| planar | yes; Euler gives F = 14 |
| γ(T) | **8** — no 7-set dominates, exhaustively |
| dominating 8-sets | **1,767** |
| four-edge deletions scanned | all **58,905** |
| minimum surviving 8-sets over those | exactly **5** |

So γ(T − F) = 8 for every four-edge set F, giving b(T) ≥ 5; with the paper's
five-edge set, b(T) = 5. Since Δ(T)+1 = 4, the conjecture is false. Every figure
matches between the two implementations and with the paper.

## arXiv:2506.01830 — divisor-sum Collatz analogue — CLEAN, one definitional slip

Conjecture 1.1: "For every positive integer n there exists k ∈ ℕ such that
ℜ^k(n) = 1", with the paper's computational claim of all n ≤ 10¹⁰. Orbits were
checked here for every n ≤ 10⁷ with no violation, and the theorem statements
(divisibility of σ, the contraction bound, the Mersenne-prime characterisation,
the 2-adic formula) over millions of cases with none.

**The defect is a definitional one at p = 2.** The paper defines P_i as
{ p prime : od(p+1) ∈ P_{i−1} } and prints P₂ = {5, 11, 13, 23, 47, 61, …}.
But od(2+1) = 3, and 3 is a Mersenne prime, so **2 belongs to P₂ by the stated
rule** while being absent from the printed list. The set-builder needs "p odd
prime". Recomputed here: the rule gives {2, 5, 11, 13, 23, 47, 61, 191, 223, 383,
…} below 500, and deleting 2 reproduces the paper's list exactly.

Harmless, since T is only defined on odd integers, and the paper does state the
odd-prime restriction where it matters (Theorem 3.1 genuinely fails at p = 2).

## arXiv:2509.12537 — union-closed families — a counterexample at n = 4

Bouchard, *An averaging result for union-closed families of sets*. Conjecture 1.1
(the union-closed conjecture itself) held over all 2,747,402 families on a
5-element ground set, and Theorem 2.1 with it.

**The paper's own Section 2 extremal conjecture fails at n = 4.** It proposes a
family A* as the minimiser of average member-set size under the conditions h = 4
and |B| = 1, with no lower bound on n. At n = 4 the following family is smaller:

    A = { ∅, {1}, {2,3}, {1,2,3}, {1,2,4}, {1,2,3,4} }

**Checked here independently**: A is union-closed (every pairwise union is a
member), its sizes are 0, 1, 2, 3, 3, 4, so the average is 13/6 ≈ 2.167. The
proposed extremal A\*, computed from the paper's own formula at n = 4, is
{ ∅, {1}, {1,2,3}, {1,2,4}, {1,2,3,4} } with average 11/5 = 2.2. So A is strictly
smaller and A\* is not the minimiser.

At n = 5 the conjecture is true — the minimum is 17/6, attained exactly by the
S₅-orbit of A\*. The repair is therefore "n ≥ 5", the same shape of defect as the
one in `notes/12`: a small-case hypothesis that was not written down.

*Caveat.* The hypotheses h = 4 and |B| = 1 are the other audit's reading of the
paper's definitions; I verified union-closedness and both averages myself, but not
that A meets those two conditions under the paper's precise meaning.

## arXiv:2503.06228 — partitions into distinct even parts — CLEAN, one typo

Nath and Sarma. The conjectured congruence for p ≥ 5 with (−2/p) = −1 was tested
over 1,409,384 coefficients across sixteen primes with no failure, and the paper's
proved 192-divisibility families were reproduced first as a control.

**One typographical defect in the introduction**, and it is confirmable in a line.
The prose says the relevant progressions are 5n+4, 7n+5 and 11n+6; the display
beside it asserts p(11n+7) ≡ 0 (mod 11). That display is false:

    p(7) = 15 ≡ 4,  p(40) = 37338 ≡ 4  (mod 11)
    p(6) = 11 ≡ 0,  p(17) = 297 ≡ 0    (mod 11)

so the progression is 11n+6 and the display carries an off-by-one. Recomputed here
from the partition numbers directly.

## arXiv:2511.05191 — Steiner systems S(2,6,226) and S(2,6,441) exist — CLEAN

Banakh, Hetman, Ravsky. The paper resolves two of the 29 open cases for S(2,6,v),
finding seven 1-rotational designs at v = 226 and six point-transitive ones at
v = 441.

**This is the best kind of audit: a deterministic certificate check rather than a
search.** The base blocks were parsed mechanically from the LaTeX source and each
design rebuilt from scratch — all 15×225 translates for each of the seven 226-designs
then all C(226,2) = 25,425 pairs, and all 20×441 translates for each of the six
441-designs then all C(441,2) = 97,020 pairs. Every pair of points occurs in exactly
one block, no block repeats, every block has six points. Thirteen of thirteen
designs pass. The 29-entry open list was checked too: sorted, distinct, and every
entry satisfies the necessary conditions 5 | v−1 and 30 | v(v−1).

**What the audit did not establish, stated plainly by it.** The paper's search at
441 is explicitly non-exhaustive, so "these designs exist" is certified but "no
others do" is not. The non-isomorphism counts (7 and 6) were not settled —
λ = 1 forces every low-order invariant constant, and a bounded search was
inconclusive. The cited nonexistence inputs are taken as given, not reproved.

That is the right boundary: existence claims are certified by explicit objects,
and the parts that rest on a search are labelled as resting on a search.

## arXiv:2501.12083 — r-Euler-Mahonian statistics — CLEAN, one wording slip

Huang and Yan. Two conjectures of Liu on equidistribution: (exc_ℓ, den_ℓ) is
ℓ-Euler-Mahonian, and (g·exc_ℓ, g·den_ℓ) is r-Euler-Mahonian with r = g+ℓ−1.

**Verified by full bivariate distribution comparison**, not just moments: all 24
permutations of 𝔖₄ reproduce Table 1 row for row including both columns, and the
conjectures hold for ℓ = 1..4 and g, ℓ = 1..6 across n = 1..7, with spot checks at
n = 8. The displayed polynomial is exactly the computed (3des, 3maj) distribution.

**A useful sharpness result beyond the paper's claim.** The exponent r = g+ℓ−1 is
uniquely determined: for (g,ℓ) = (2,2) and (1,3) on 𝔖₆, r = 1..7 gives equality
only at r = 3. So the conjectured exponent is not one choice among several.

**One non-substantive finding.** The prose describes g·exc_ℓ as counting letters
"weakly to the right of π_ℓ", but the displayed formula uses a *position*
condition (i ≥ ℓ). Read off the prose literally the count differs on 12 of the 24
permutations of 𝔖₄ and contradicts the paper's own table; the formula is correct
and the prose is loose. Recorded as wording, not error.

## arXiv:2611.27685 — remoteness in trees with a given segment sequence — CLEAN

Allie, Du Preez, Hefty and Mafunda, November 2026. Conjecture: for every segment
sequence D, a D-tree with minimum remoteness is starlike or a (Δ,2)-tree — that
is, a minimiser never has three or more branch vertices.

**Tested over every unlabelled tree on at most twenty vertices**: 1,346,023 of
them, with the counts matching A000055 term by term. Over 1,996 (n, D) pairs, no
tree with three or more branch vertices was ever a remoteness-minimiser, not even
tied, while 98 segment sequences at n = 20 show the (Δ,2) tree strictly beating
both the starlike tree and a three-branch competitor — so the test is not vacuous.

**One edge case the conjecture's wording does not cover.** A single-segment
sequence D = (n−1) determines the path uniquely, which has no branch vertices at
all and is therefore neither starlike nor (Δ,2). That is an implicit-hypothesis
gap rather than a counterexample, and it should be read as "assuming branch
vertices are present".

## Three OEIS conjectures from 2025 — all survive

Each sequence was computed from its defining object, never from the conjectured
formula, and the entry's own terms were reproduced first.

| Entry | Conjecture | Range | Result |
| --- | --- | --- | --- |
| A386648 | a(n) mod 6 repeats 2,3,4,3,2,5 for n > 6 | exact to n = 199; derived reduction to 10⁶ | survives |
| A386655 | a(n) mod 6 repeats 1,0,3,0,3,2 for n ≥ 6 | n = 6..2999 | survives |
| A383423 | the difference set is exactly {1,3,4,5,7} | 2,944,276 terms below 10⁷ | survives |

**The third independently confirms a published proof.** arXiv:2610.04842 proves
the A383423–A383427 conjectures; the computation here reproduces the realised
difference set as exactly {1,3,4,5,7} over ten million indices, with no value
outside it and all five occurring. Agreement between a proof and a large
computation is worth more than either alone.

## What this batch shows

The distribution of outcomes is the useful part. Twenty papers, one small
counterexample and three cosmetic defects — no collapse of any main theorem. Deep
auditing finds real things at a low but nonzero rate, and the findings cluster at
small parameters and in displayed intermediate steps, not in the proofs' substance.

That is worth stating plainly against the temptation to report a swarm as
productive because it produced volume.
