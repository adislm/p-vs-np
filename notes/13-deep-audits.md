# Deep audits of recent papers

A shallow test of one conjecture per paper finds nothing. Deep-auditing a single
paper — reproducing every table, checking every displayed identity, testing every
conjecture — found a false theorem in `notes/12`. This file records the same
treatment applied more widely.

**Method.** Resolve the identifier, quote every statement verbatim, reproduce the
paper's own numbers *before* testing anything, treat the paper's proved results as
a control on the checker, then extend the range. A defect is recorded only with
the paper's exact words and a computed contradiction beside them.

## 1. arXiv:2609.37920 — congruences for the Andrews–Uncu function

Baruah, Das, Saikia and Sarma, *Congruences for the Andrews–Uncu partition
function*, September 2026.

**The sequence was pinned first.** With
Σ EO_u(n)qⁿ = f₄²/f₂², the function vanishes at odd n and at even arguments is
`[Q^m] ∏_{i≥1}(1+Q^i)²`, giving 1, 2, 3, 6, 9, 14, 22, 32, 46, … — OEIS A022567.
Computed three ways (product DP, Euler's pentagonal recurrence for p(n), and a C
engine working modulo 320), all agreeing with OEIS. The paper has no numerical
table, only a table of modular forms, so the OEIS match is the available control.

**Every proved congruence passed, with zero failures.** These are the control, and
they are not trivial ones: the modular-2 progressions, the mod-4 self-similarity,
the mod-5 coefficient congruence carrying a factor of 3^{k+1}, the mod-16 and
mod-32 families, and the mod-64 theorem. Instances tested run from 160 000 to
800 000 per statement, up to index 4×10⁶. Reproducing the mod-5 coefficient
congruence matters in particular: it validates the engine on a non-power-of-two
modulus.

**All three conjectures passed.**

| Conjecture | Range reached | Result |
| --- | --- | --- |
| 6.1, mod 16 along 11-adic progressions | k = 0: 165 289 instances; k = 1: 1 365; k = 2: 10 | holds |
| 6.2, mod 64 for every p ≡ 3 (mod 4) | every such p with 3 < p ≤ 107 at k = 0; k = 1 for p = 7, 11, 19, 23, 31, 43, 47, 59 | holds |
| 6.3, mod 64 with coefficient λ_p^k | p = 7 to k ≤ 3; p ≤ 107 to k ≤ 2 | holds |

**One defect, and it is minor.** In the proof of Corollary 5.2 the paper displays

    EO_u(2·7²n + 8) ≡ EO_u(2n)  (mod 16)

which is false at n = 0: EO_u(8) = 9 while EO_u(0) = 1, and 9 ≢ 1 (mod 16). A
factor of 9 from the preceding line was dropped. The corrected statement

    EO_u(98n + 8) ≡ 9·EO_u(2n)  (mod 16)

holds. **Verified here independently**: the sequence was recomputed from
∏(1+Q^i)², giving EO_u(0) = 1 and EO_u(8) = 9, matching OEIS A022567; the printed
form fails at n = 0 and the corrected form passes.

**Why this does not matter for the paper.** Corollary 5.2 itself is true — the
mod-16 vanishing comes from the right-hand side having only q^{7m} terms, which
survives the dropped constant. This is an error in a displayed intermediate step,
not in a result. It is recorded because it is exactly the kind of slip that a
reproduction pass catches and a reading pass does not.

**Verdict:** a clean audit. Three conjectures survive over large ranges, one
cosmetic error in a proof.

## 2. arXiv:2609.31330 — 3-isogeny Selmer groups

Weiss and Zou, September 2026. A clean audit: no defect in any conjecture.

**What was actually verified, and what was not.** The paper's eight tables were
parsed cell by cell. Every deterministic column — mean, SD, MSE, the min/max
percent deviations — reproduces to printed precision, with a maximum relative
error of about 0.5% attributable to rounding of the inputs. More tellingly, every
cross-table sum is exact: Table 2's six blocks sum to Table 1's non-trivial count,
Table 3 sums to Table 5's, and Tables 7 and 8 reproduce Tables 1 and 5 exactly.
That is strong evidence the tables are internally consistent.

What was *not* done, and should be said plainly: the billions of underlying curves
were not regenerated. The raw counts are taken as given; only the arithmetic
relations among them were checked. An error in the curve enumeration itself would
not have been caught.

**The computational definitions were implemented from scratch** and checked
against the paper's own statements: the cubic-residue matrix construction, the
dimension law, the kernel conditions, and the nullity identities. Exhaustive over
6,576 normalized curves, sampled over about 150,000 more.

**Both conjectures held.** The matrix-frequency conjecture converged toward
uniformity as the prime pool grew, with the maximum deviation falling as
predicted; the nullity-distribution conjecture matched the predicted limit law for
every tested parameter. Neither was contradicted.

**Two imprecisions, neither mathematical.** A sentence claims a maximum deviation
of 6×10⁻⁴ where the table gives 2.27×10⁻⁴ for those rows (5.86×10⁻⁴ is the
maximum over all blocks) — a wording slip. And one entry-marginal deviation is
about 16σ under exact iid uniformity, which is a finite-sample effect on the
marginals rather than a failure of the matrix-count uniformity.

## 3. arXiv:2511.21524 — k-path graphs, algebraic connectivity and α-index

de Paula, Justel, Oliveira, Caruba, November 2025. A clean audit that also
extends the authors' own testing range.

**Controls came first and passed**: the enumeration reproduces A000088 for all
graphs and A001349 for connected graphs exactly. The k-path graphs themselves were
generated three independent ways — the paper's algorithmic construction, a
structural predicate run over *all* graphs, and the paper's literal recursive
rule — all agreeing.

**Table reproduction was complete**: 33 of 33 count cells, 260 of 260 numeric
cells in the k = 2 tables, and 378 of 378 α-index cells. Zero mismatches. The
paper's graph6 entries decode to the extremal graphs it claims.

**Both conjectures held, including outside the authors' range.** The paper checks
k ≤ 4 and α ∈ {0.1, …, 0.9}. The audit reaches k = 5, 6, 7 and 8, and α values
down to 0.001 and up to 0.999 — near both endpoints of the interval, which is
where a uniqueness claim is most likely to fail. No violation.

**One expository gap, not a false claim.** The "second maximum" clause of
Conjecture 5.2 is ill-posed when n = k+1, k+2 or k+3, because there the class
L_{k,n} has exactly one element and a second maximum does not exist. Two table
captions also carry wrong ranges. Neither affects the mathematics.

**A methodology note worth keeping.** The agent's own first hand-analysis at n = 5
claimed two 2-path graphs; the program showed the fan and the ribbon are
isomorphic there. The enumeration was right and the hand-check wrong — which is
the rule stated at the top of this file, applied to itself.

## 4. Independent verification of another group's counterexamples

`AmirMakir/broken-conjectures` is doing the same work as this file: agents finding
counterexamples to open conjectures, with exact Python verifiers and Lean proofs.
Its third result is the spectral conjecture that `notes/12` had recorded as
surviving — it is false, and that correction is recorded there. The rest of its
claims were verified here independently, rebuilding each witness rather than
running their code.

### Result 3 — spectral conjecture — CONFIRMED

Recorded in `notes/12`: λ₂ > μ₁ − 2 on the 11-vertex graph G(4,3), verified with
symbolic eigenvalues. The Laplacian characteristic polynomial factors, giving
μ₁ = (7+√5)/2 exactly.

### Result 4 — Hausmann Question 5.4 — CONFIRMED

**Question, verbatim** (arXiv:2611.05178, Hausmann, *Weighted Max Cut in Subcubic
Graphs*, November 2026): "Does every subcubic graph G of odd girth exactly five
admit a partition V(G) = L ∪ R such that L is independent and every component of
G[R] has order at most three?"

**The witness is the Wagner graph** V₈: vertices 0–7, rim edges i ~ i+1 mod 8,
rungs i ~ i+4 for i = 0..3. It is cubic (so subcubic), has 12 edges, and its
**odd girth is 5** while its girth is 4 — the 4-cycles do not disqualify it.

**Exhaustive over all 2⁸ = 256 partitions**, computed here independently:

- 33 have L independent;
- of those, **0** leave every component of G[R] of order at most 3;
- the minimum, over all independent L, of the largest component size is **4**.

So the answer to Question 5.4 is **no**.

*A bug of my own, recorded.* My first check reported odd girth 4 and would have
refuted the witness. The routine was returning the shortest cycle of *any* parity
and calling it the odd girth. Fixing it to consider only odd lengths gives 5, and
the witness stands. The general lesson matches the one in `notes/12`: when a check
disagrees with a claim, suspect the check first, and be specific about what it
actually computed.

### Result 6 — 11-adic congruences — CONFIRMED

**Conjecture 6.1** of Banerjee–Smoot, arXiv:2611.09681 (November 2026), with
P^[1]_a(q) = (−q;q)_∞^a/(q;q)_∞ and P^[2]_a(q) = (−q;q)_∞^a/(q;q)_∞⁵:

> (1) If a ≡ 3, 5, 7 (mod 11), then p^[1]_a(11^α n + δ) ≡ 0 (mod 11^{⌈α/2⌉}),
> where 24δ ≡ 1 − a (mod 11^α).
> (2) If a ≢ 1, 3, 5 (mod 11), then p^[2]_a(11^α n + δ) ≡ 0 (mod 11^{⌈α/2⌉}),
> where 24δ ≡ 5 − a (mod 11^α).

**Both parts fail**, and the congruence-class trap was checked explicitly: 36 ≡ 3
satisfies part (1)'s hypothesis, and 40 ≡ 7 satisfies part (2)'s. With α = 3 the
required modulus is 11² = 121, and 24·54 = 1296 ≡ 1−36 ≡ 5−40 (mod 1331), so
δ = 54 is correct.

**Recomputed here from the product definitions**, in exact integer arithmetic:

    p^[1]_36(54) = 62043410886974649205238011198   divisible by 11, not by 121
    p^[2]_40(54) = 66134580699742235651549220246110  divisible by 11, not by 121

Both have 11-adic valuation 1 where the conjecture requires 2. The digits match
the other group's figures exactly, computed by three different algorithms here.

**This one is genuinely new.** The paper is at v1, no revision, no journal
reference, and the authors prove only the a = 2 case of part (2); the general
conjecture was proposed in the same paper's conclusion. A falsification of a
conjecture proposed four weeks ago, still uncited, is the most valuable thing in
this file.

### Result 2 — random sequential adsorption versus the jammed ensemble — CONFIRMED

**Conjecture 5.2** of Higuita-Diaz, López, Roldán-Correa, arXiv:2611.14718
(v2, 18 November 2026), verbatim:

> For every finite simple graph G with maximum degree Δ(G) ≤ 3, the sequential
> model dominates the static model (N^stat ≤_st N^seq).

Two things about this statement are easy to get wrong and decide the whole
question. "Dominates" is **first-order stochastic dominance over the full
distribution**, not a statement about means. And N^stat is uniform over *all*
maximal independent sets, while N^seq is the size reached by picking a vertex
uniformly among those still available, occupying it, and blocking its neighbours.

**The witness is a 15-vertex tree of maximum degree 3.** Recomputed here exactly
in rational arithmetic, independently of the other group's code:

- maximal independent sets: 55, of sizes 6 (one set), 7 (fifty), 8 (four);
- N^seq: P(6) = 64/3375, P(7) = 7993019/10135125, P(8) = 1949914/10135125;
- N^stat: 1/55, 50/55, 4/55.

The cumulative distributions cross. At k = 6,

    P[N^seq ≤ 6] = 0.018963  >  P[N^stat ≤ 6] = 0.018182

which is exactly the inequality the conjecture forbids. At k = 7 the order
reverses, so neither distribution dominates the other.

**The weaker statement survives, and this matters.** The means are
E[N^seq] = 7.1734 and E[N^stat] = 7.0545, so the sequential model does have the
larger expected jammed set. Only the distributional claim — which is what the
paper actually states — fails. Anyone reading this as "the sequential model is
smaller on average" would draw the wrong conclusion.

**Still open.** Version 2, two weeks before this audit, states Conjecture 5.2 as a
conjecture; no indexed refutation exists. The other group's report also re-ran the
exhaustive check over all 27,525 connected graphs of maximum degree ≤ 3 up to 12
vertices and found no violation, matching the paper's own claimed range — so the
example at 15 vertices is precisely one step beyond where the authors looked.

### Result 1 — distance energy maxima — CONFIRMED under the maximiser reading

**Conjecture 4** of Caporossi–Chasset–Furtula, GERAD G-2009-64 (2009), as
restated by Aouchiche–Hansen (LAA 458, 2014) as Conjecture 8.12: among all graphs
of order n and size m with n ≤ m ≤ (n−2)(n−3)/2, the path–complete graph PK_{n,m}
maximises the distance energy E_D = Σ|µᵢ|, the sum of absolute values of the
distance-matrix eigenvalues.

**Witness:** the 12-vertex, 44-edge graph with graph6 string `K]Nxnsor}^^R`.
Recomputed here from the graph6 string, without using the other group's code:

    E_D(counterexample) = 37.1446819434515
    E_D(PK_{12,44})     = 36.8942393990325
    gap                 = +0.250442544419

The extremal comparison is unambiguous because **PK_{12,44} is unique**: among all
path–complete graphs with 12 vertices and 44 edges, exactly one exists, K₉ together
with a 3-vertex path whose first vertex joins 6 clique vertices. There is no
stronger competitor to appeal to. The constraint holds too: 44 < 45 = (n−2)(n−3)/2.

Independently, the other group enclosed the eigenvalues with exact Sturm sequences
and rational interval arithmetic to a width below 3×10⁻³⁰, so the gap is not a
numerical artefact. My float64 recomputation agrees to twelve digits.

**A necessary caveat about the statement.** Read literally — "Let G be a graph on
n vertices and m ≤ (n−2)(n−3)/2 edges, then G is composed of a path appended to a
clique" — the conjecture is trivially false, since a cycle satisfies the hypothesis
and has no such form. The substantive claim is the maximiser reading, and that is
what the counterexample defeats. Recording this distinction matters: the defect is
in the mathematics, not in an ambiguity of wording.

**Still open as far as we can tell.** No proof or refutation surfaced; the 2014
survey still lists it as Conjecture 8.12. Absence of evidence in a search is not
proof of openness, and that is stated as the limit of this claim.

### Result 5 — five statements from Cazenave's conjecture corpus — CONFIRMED, with a qualification

**The qualification matters and is not pedantic.** These five statements are not
in the paper's body. The identifiers #861166, #1053490, #2632674, #753029 and
#121183 appear nowhere in the PDF of arXiv:2611.03879; they are rows of
`index_conjectures.csv` in the downloadable archive that §8 of the paper points
to, each marked `statut=ouverte` with an empty `contre_exemple` field. So the
correct description is "five statements marked open in the corpus archive", not
"five of the paper's conjectures".

All five are false, with witnesses on 10 to 15 vertices:

| ID | Statement | Witness | Margin |
| --- | --- | --- | --- |
| #861166 | rad ≤ 2(Randic − λ₂) | 10 vertices, 19 edges | +0.0701 |
| #1053490 | λ₂ ≤ Randic − rad/2 | same graph | +0.0351 |
| #2632674 | λ₂ ≤ Randic − √(rad−1) | 12 vertices, 29 edges | +0.0131 |
| #753029 | μ₂ ≤ 1 + 2^{λ₁} | 15-vertex tree | +0.0370 |
| #121183, #123215, #715458 | λ₂ ≤ (log rank)^{R/2} variants | 11-vertex tree | +0.0111 |

**One verified here independently.** For the last family, the 11-vertex tree gives

- characteristic polynomial λ⁷(λ−2)(λ+2)(λ²−6), so λ₂ = 2 **exactly**;
- rank 4 and Randić index R = 4.2101642960, so the right-hand side is
  (ln 4)^{R/2} = 1.9889203416.

Since 2 > 1.98892, the statement fails. All three parenthesised forms of it
coincide, so one witness kills all three.

**The other group's computation is careful about error.** The eigenvalues were
isolated from exact integer characteristic polynomials with interval widths below
10⁻³⁵ and re-checked by exact rational Sylvester-inertia congruence; the
transcendental comparisons carry an explicit additive margin where the numerical
error allowance is smaller by more than seventy orders of magnitude. The
multiplicity question — "second largest with multiplicity" versus "second largest
distinct" — makes no difference on any of the graphs used, since the relevant
eigenvalues are simple.

## 5. arXiv:2611.19635 — box-free colourings — clean audit

Alm and Miller, *Constructive and computational methods for extremal and
near-extremal box colorings*, November 2026. No defect found.

**Every table reproduces.** Table 2's 21 cells of ρ(a,b) all match, and the 14
nonzero entries each have an Appendix-A colouring matrix which recomputes exactly
from the definition; an exact branch-and-bound settled 19 of the 21 cells
exhaustively, with the remaining two following from the paper's convexity bound,
which was re-derived. Table 3's fifteen layer bounds all equal ⌊2·C(a,2)C(b,2)/ρ⌋
exactly. Table 4's thresholds are exact.

**Every certificate checks.** The GitHub constructions for 3×7×126, 4×7×126,
5×5×100, 5×6×75, 6×6×75 and 5×7×50 were downloaded and verified independently:
each is box-free with every layer attaining exactly ρ.

**Both conjectures remain open, with their supporting bounds confirmed**: N(5,7) ≥
50 from a verified certificate, and m(11) ≤ 8 from one with exactly eight boxes.
Neither was refuted by direct search.

**One honest improvement, not an error.** An independent min-conflicts search found
slightly better values than the paper's Table 4 empirical minima (1709 vs 1711,
and so on). That is a stronger construction, not a defect in theirs.
