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

## arXiv:2505.11403 — a linear factor-complexity conjecture is FALSE

Abdullah and Hamoud, May 2025. **Conjecture 2.8, verbatim**: "The factor
complexity p(k) of W_{A,σ,a₀} is linear. Specifically, for sufficiently large k,
p(k) = (N−1)k + C_N for some constant C_N that depends on N."

**The slope is wrong, and by a lot.** Take N = 3 with σ: 0→01, 1→12, 2→20. Its
fixed point is W(n) = s₂(n) mod 3, where s₂ is the binary digit sum — I checked
the first eight symbols are `01121220`, matching the morphism. Counting distinct
factors of length k in a prefix of length 2¹⁸:

| k | p(k) | p(k)/k | conjectured slope |
| --- | --- | --- | --- |
| 2 | 9 | 4.500 | 2 |
| 8 | 54 | 6.750 | 2 |
| 32 | 234 | 7.313 | 2 |
| 64 | 474 | 7.406 | 2 |
| 128 | 954 | 7.453 | 2 |
| 256 | 1914 | 7.477 | 2 |

**Recomputed here independently** from the digit-sum definition, and the ratio is
climbing steadily toward 7.5 = N(2N−1)/2, with no sign of levelling at 2. The
other audit adds the finer structure — every increment p(k) − p(k−1) for k up to
16400 is 6 or 9, never N−1 — and the same failure at N = 4 (ratio → 14, claimed 3)
and N = 5 (ratio → 22.5, claimed 4).

**A second, smaller defect in the same paper.** The proof of Theorem 2.6 asserts
that every length-3 factor of W has the form xσ(x)σ²(x). That is false: W begins
`01121220`, which contains `112`, while {xσ(x)σ²(x)} = {012, 120, 201}. The
theorem itself survived testing; it is the proof's first step that is unsupported.

## arXiv:2605.26916 — preorder polytopes — CLEAN, one index slip

Athanasiadis and Chapoton, May 2026. Conjectures 4.4, 4.8, 5.3 and 5.4 all held
under exact enumeration — all 4 preorders on 2 elements and all 29 on 3, with
Ehrhart polynomials interpolated exactly, and the paper's worked examples
reproduced (Delannoy numbers 2, 5, 12, 29, 70 and h₅ = (1,9,25,25,9,1)).

**One defect, in a table.** §9.3 tabulates the poset C_n × C₂ minus its minimum
and maximum: "n=1: 4, (1,2,1); n=2: 29, (1,7,13,7,1); n=3: 265". But the count
sequence 1, 4, 29, 265 is L_n = 1, 4, 29, 265 for n = 1, 2, 3, 4 — every row is
indexed one too low, and the n = 1 row (a single point, h = (1)) is missing. The
paper's own generating function corroborates: its x^n coefficient is −L_n with
L₁ = 1, L₂ = 4. An indexing slip in the table, not in the mathematics.

## arXiv:2507.17780 — machine-generated invariants — one conjecture false from n = 9

Davila, Brimkov and Pepper, on ten years of conjectures produced with a machine
collaborator. Four conjectures, enumerated against every connected graph to order
9 (273,192 graphs, with A000088 and A001349 reproduced exactly).

| Conjecture | Verdict |
| --- | --- |
| α ≥ (a+R)/Δ for nontrivial connected G | fails **only at K₂**; all 273,191 graphs with n ≥ 3 pass |
| Z ≤ α+1 for connected Δ ≤ 3, G ≇ K₄ | clean over 358,889 subcubic graphs to n = 14 |
| i ≤ μ* for r-regular G, r > 0 | clean over 590,081 regular graphs |
| μ* ≤ H for nontrivial connected G | **FALSE from n = 9** |

**The K₂ failure is a boundary slip.** Both endpoints have α = a = R = Δ = 1, so
the bound reads 1 ≥ 2. The n ≥ 3 version is separately known.

**The μ* ≤ H failure is real and I checked it here.** The smallest witness is the
friendship graph F₄ — four triangles sharing a centre, nine vertices. Recomputed
from scratch: the degrees are 8 and then eight 2's, so the harmonic index is

    H = 8·(2/10) + 4·(2/4) = 8/5 + 2 = 18/5 = 3.6

and the minimum maximal matching is 4, since every triangle must contribute an
edge or its two rim vertices would leave a matching edge addable. So 4 ≤ 3.6 is
false. Verified by brute force over all edge subsets as well as by the parity
argument.

## arXiv:2507.20298 — eta quotients — three defects

Huber, McLaughlin and Ye. The proved vanishing results were reproduced over
truncations of 6,000–20,000 terms as a control, and all held.

**One defect I checked directly.** The proof of Lemma 2.1 asserts
`(−q;−q)_∞ = f₂³/(f₁f₄)`. Computed here as power series:

    (−q;−q)_∞    = 1, 1, 1, 2, 2, 3, 4, 5, 6, 8, 10, 12, 15, …
    f₂³/(f₁f₄)   = 1, 1, −1, 0, 0, −1, 0, −1, 0, 0, 0, 0, −1, …
    f₂/f₁        = 1, 1, 1, 2, 2, 3, 4, 5, 6, 8, 10, 12, 15, …

so the identity is false and the correct one is `(−q;−q)_∞ = f₂/f₁`. The lemma's
two conclusions remain true; the proof's first step is not.

Two further defects from the other audit: an equation dropping a factor of f₄²
(making it fail at q⁷ and q¹¹), and a table whose "extra zero" exponents are each
one too high.

## arXiv:2511.15877 — fractional triangle decompositions — finite n, not the limit

Mahabaduge and Simkin, November 2026. Two conjectures, both asymptotic as n → ∞.

**The audit found finite cases where the statement fails, and was careful about
what that means.** Conjecture 7.1, read at fixed n, is false at n = 4, 5 and 6:
once the graph process has just become triangle-covered it can be K₄ − e, K₅ − 2e
or K₆ − 2e, and none of those admits a fractional triangle decomposition — edge
12 is forced to carry weight 2. Verified by an exact DP over all orderings.

**But the conjecture is a limit statement, and it is not refuted.** The audit says
so explicitly: "For n = 7–12 both types of K_n − 2e are FTD, so this universal
E−2 obstruction stops. The n → ∞ whp claim is not refuted." That is the right
distinction, and a less careful report would have called this a counterexample.

## Two more clean audits

- **arXiv:2611.22656**, Golomb rulers with real marks — every table reproduced,
  all 126 Singer rulers for prime powers m ≤ 13 verified with exact dual
  certificates, and G_R = G_Z re-proved independently for 2 ≤ n ≤ 10.
- **arXiv:2603.04218**, arrow pattern avoidance — the paper's own sequences in
  Tables 2 and 3 reproduced exactly, and all three parts of Conjecture 7.1
  verified: a_n(123,(12;1→3)) = 2ⁿ−n, a_n(321,(12;1→3)) = F_{2n−1}, and
  a_n(321,(12;1→2)) = M_n, each for every n up to 16.

## What this batch shows

The distribution of outcomes is the useful part. Twenty papers, one small
counterexample and three cosmetic defects — no collapse of any main theorem. Deep
auditing finds real things at a low but nonzero rate, and the findings cluster at
small parameters and in displayed intermediate steps, not in the proofs' substance.

That is worth stating plainly against the temptation to report a swarm as
productive because it produced volume.
