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
