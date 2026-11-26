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
