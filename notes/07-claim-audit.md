# Auditing claimed resolutions of P vs NP

The field receives a steady stream of claimed proofs. Most are wrong, and the
useful contribution is not another rebuttal essay but a precise record of
*where* each one fails, checked independently rather than taken on trust. Each
audit below was verified by hand against the source artifact before being
written down.

Method: `notes/06-falsification-checklist.md`. The checklist's decisive tests
were applied in order; a claim that fails an early test is not examined further.

## Case 1 — Zenodo 23757254, "Exact Analytic Resolution of the P versus NP Conjecture"

**Claim.** An unconditional proof that P ≠ NP, via Riemannian Ricci curvature:
polynomial-time computation corresponds to bounded-curvature geodesics on circuit
varieties, while the 3-SAT solution manifold has curvature bounded above by
−κ·2^(c₀n), forcing circuit size 2^Ω(n).

**Finding, verified directly.** The published PDF contains no mathematics.
Checked independently: 20 pages, 27,556 characters of extracted text, **zero**
mathematical operator characters (`=`, `≠`, `≤`, `∈`, `∀`, `∃`, `⊆`, …), and no
mathematics font in the embedded resources. Every displayed equation is a blank
line. The title as printed terminates at "…AND PROOF OF", with the `P ≠ NP`
dropped.

Reproduce:

    curl -sL -o zen.pdf "https://zenodo.org/records/23757254/files/SHAHEEN-TR-2026-F15.pdf?download=1"
    python3 -I -c "import pypdf,re; r=pypdf.PdfReader('zen.pdf'); \
      t=''.join(p.extract_text() or '' for p in r.pages); \
      print(len(r.pages), len(t), len(re.findall(r'[=⇒≠⊆⊂∈∀∃∑∫≤≥√∂]', t)))"

**The prose outline fails independently of the artifact.** Three problems, any
of which is fatal:

- A Boolean circuit is a piecewise-constant map on finite strings. It is not a
  Riemannian submersion, and `{0,1}` is zero-dimensional, so O'Neill's formula
  has no horizontal curvature to compare. Category error, not a gap.
- Gauss–Codazzi is applied in the reverse direction: a bounded second
  fundamental form inside a positively curved ambient space bounds submanifold
  curvature from *above*, which contradicts the claimed embedding rather than
  the circuit.
- Theorem 4.1 is average-case (uniform random 3-CNF at threshold); Theorem 5.2 is
  worst-case. At threshold roughly half of all instances are unsatisfiable, so
  their solution set is empty — no manifold, no clusters, no curvature to
  obstruct.

**Verdict: INVALID.** The artifact states no mathematics, and the outline
contains a category error and a reversed inequality before any barrier is
reached.

## Case 2 — github.com/yimeng2026/PFE, Sylva "computational entropy"

**Claim.** `P ≠ NP ⟺ ΔH > 0`, where H(C) is a supremum of Kolmogorov
complexities over a class and ΔH is a gap between NP ∖ P and P, advertised as
"Lean 4 verified, 8257/8257, 0 sorry."

**Finding 1 — the quantity is identically zero, so the equivalence is vacuous.**
K(L) is the length of the shortest machine deciding L. For every n, each
singleton `{s}` with `|s| = n` lies in P, and any machine deciding `{s}` must
encode s, so `K({s}) ≥ n − O(log n)` by counting: only `2^c` machines have
description length at most c, but there are `2^n` singletons of length n.
Therefore `sup_{L ∈ P} K(L) = ∞`, while `inf_{L ∈ NP∖P} K(L)` is finite. The raw
gap is −∞, and the definition clamps at 0, so **ΔH = 0 unconditionally**. The
equivalence then collapses to `¬(P ≠ NP)`.

**Finding 2 — the Lean genuinely contains `sorry`.** Verified directly against
`sylva-release/src/Complexity.lean` at commit on `main`: `sorry` appears at
lines 228, 276 and 338, while `sylva_entropy_equivalence` is stated at line 286.
`sorry` compiles silently, which is why "8257/8257 compiled" can be literally
true and mean nothing, and why "0 sorry" is false.

Reproduce:

    curl -sL -o c.lean "https://raw.githubusercontent.com/yimeng2026/PFE/main/sylva-release/src/Complexity.lean"
    grep -n "sorry\|admit" c.lean

**Finding 3 — definitional drift.** The release file's `ClassP` is TM-based while
the paper's is circuit-based, a uniform/non-uniform slide. The repository's own
audit flags this.

**Verdict: INVALID.**

## What the two cases have in common

Neither fails because of a subtle mathematical error at the frontier. Both fail
before a barrier is even reached — one at the point of stating any mathematics
at all, the other at the first definition. That is the characteristic shape of
the genre: the failure is usually visible on inspection, and the expensive part
is not refuting the claim but noticing which sentence to look at.

The two most common proximate causes, both present here:

1. **Definitional collapse.** A quantity is defined in a way that makes the
   central claim vacuously true or trivially false. The Kolmogorov-entropy gap
   is the clean example: `sup` over P is infinite, so the gap is zero and the
   theorem says nothing.
2. **Category mismatch.** An object from one theory (a circuit) is treated as an
   object from another (a Riemannian submanifold, or a uniform machine when a
   circuit family is meant). The argument then proves a statement about the
   wrong objects.

Both are caught by B3 (definition drift) and B1 (uniformity confusion) in the
checklist, which are checks that cost minutes, not months.

## Case 3 — the arXiv stream, 2023–2026

Every identifier below was resolved against the arXiv API and returned the
title given, so the list is real rather than reconstructed. None of these is a
resolution of P vs NP.

| Title | Authors, year | ID | One-line claim | Failure mode |
| --- | --- | --- | --- | --- |
| SAT Requires Exhaustive Search | Xu, Zhou, 2023/2025 | 2302.09512 | constructed CSP/SAT instances require brute force | **proves something false** — contradicted by Williams' 2011 algorithm; a published Comment by Allender–Williams records this |
| P=NP | Deng, 2024 | 2405.08051 | an SDP decides 3-colouring of degree-4 graphs | **proves something false** — conflates subgraphs with induced subgraphs; see arXiv:2507.09018 |
| The Linear Correlation of P and NP | Zheng, Wang, 2023 | 2303.03958 | matrix linear dependence gives P ≠ NP | **relativizes** — pure linear algebra, valid under any oracle |
| The Radical Solution and Computational Complexity | Zheng, Wang, 2024 | 2405.15790 | Galois non-solvability of the quintic gives P ≠ NP | **relativizes** — equates "no radical formula" with "no polynomial algorithm" |
| Graph-Based Deterministic Polynomial Framework for NP Problems | Lee, 2025 | 2508.13166 | edge-sharing graph verifier gives constructive P = NP | **one machine only** — a single unverified algorithm, with the trimming step asserted |
| A Quantale-Weakness Route to P ≠ NP | Goertzel, 2025 | 2510.08814 | evidence normalisation and gauge rank give P ≠ NP | **unverifiable** — the samplable family and the mixing/locking lemmas are never constructed |
| Toward P vs NP: An Observer-Theoretic Separation | Edwards, 2025 | 2512.11820 | "N-Frame"/SPDP rank gives P ≠ NP in ZFC | **non-standard definitions** — bespoke observer model; the author states verification is future work |
| Constructive solvability and the P versus NP problem | Hole, 2024 | 2406.16843 | resolves the problem under a constructive interpretation | **non-standard definitions** — redefines "constructible theory", denies NP ⊆ EXPTIME for a homemade family |

**What the failures share.** Each breaks at the same joint: the move from "this
construction or encoding fails" to "no algorithm exists". The algebraic
arguments are oracle-invariant, so Baker–Gill–Solovay kills them outright. The
machine-based arguments refute at most their own program, or assert a lower
bound that a known algorithm violates. The definitional arguments rename the
problem. Not one supplies a circuit lower bound, so the natural-proofs barrier
is never engaged — it is bypassed by asserting a uniform separation directly.
Xu–Zhou additionally exhibits uniformity confusion: a uniform lower bound
contradicted by a non-uniform algorithm.

**Two facts worth keeping.** Exactly one of these reached a peer-reviewed venue
(Xu–Zhou, *Frontiers of Computer Science* 2025), and it is wrong, with a formal
rebuttal on record. And **no** claimed P vs NP resolution has a complete Lean or
Coq formalisation: the attempts either contain `sorry` or rest on unjustified
axioms. The only complete machine-checked complexity results are formalisations
of Cook–Levin (Coq, ITP 2021; Isabelle/AFP 2023), and Mathlib still has no NP
class. That last point is the honest baseline for this repository too — the Lean
here formalises the implication structure, not the classes themselves.
