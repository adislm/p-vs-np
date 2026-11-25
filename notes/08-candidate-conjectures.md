# Candidate intermediate conjectures, and why nearly all of them die

An experiment: generate statements that sit between known theorems and P ≠ NP,
then try hard to kill them. The value is in the filter, not the generation. A
candidate that survives is worth thinking about; a candidate that dies leaves a
record of *why* that class of statement cannot work, which is itself useful.

Each candidate is recorded with: the statement, its direction to P ≠ NP, whether
it is already known, whether it is trivial, the barrier it faces, and the
strongest objection. Verdicts: VIABLE / KNOWN / TRIVIAL / FALSE / VAGUE.

**Headline result of the experiment: of the candidates generated so far, one
survives, and it is a known research programme rather than a new idea.** That is
the expected outcome, and recording it honestly is more useful than dressing up
a restatement as a discovery.

## 1. Proof complexity

### Lemma A — no recognizable tautology family is hard for all proof systems

This kills a whole class of candidates at once, so it is worth stating.

Let S ⊆ TAUT be decidable in polynomial time. Define the system Q_S whose
verifier accepts (φ, w) when either w is a marker and φ ∈ S, or w is a Frege
proof of φ. Then Q_S is a valid Cook–Reckhow proof system: the verifier runs in
polynomial time, it is sound because S ⊆ TAUT and Frege is sound, and it is
complete because Frege is. Every φ ∈ S has an O(1)-size Q_S proof.

Consequence: **a polynomial-time recognizable family of tautologies is easy for
some proof system**, always. So no candidate of the form "family F is hard for
every proof system" can be true, and any p-optimal system automatically has
short proofs of every recognizable family. The universal quantification over
proof systems cannot be discharged by exhibiting one family.

This is the proof-complexity analogue of the relativization barrier: a
diagonal construction (the axiom-completion system) defeats every "one explicit
family" proposal.

### Candidates

| Candidate | Verdict | Implies |
| --- | --- | --- |
| C1: Extended Frege is not polynomially bounded (Cook's conjecture) | KNOWN | nothing — it is *implied by* NP ≠ coNP, hence strictly weaker |
| C2: a p-optimal system that is not polynomially bounded | KNOWN — a restatement | NP ≠ coNP, but *equivalent* to it |
| C3: hardness magnification — a barely-superlinear (n^{1+ε}) lower bound for a sparse NP language (MCSP or MKtP) against a *weak circuit model* | **VIABLE** | NP ⊄ P/poly, hence P ≠ NP |
| C4: a proof-complexity generator hard for every system | naive form **FALSE** by Lemma A; refined form KNOWN | — |
| C5: "prove Frege (or AC⁰[p]-Frege) lower bounds" | VAGUE | none |

**Why C3 survives, and what it actually says.** Hardness magnification
(Oliveira–Santhanam, FOCS 2018; Chen–Jin–Williams, FOCS 2019;
McKay–Murray–Williams, STOC 2019) is a transfer theorem: a weak lower bound in a
weak *circuit* model upgrades to a strong one. A barely-superlinear bound for
MCSP or MKtP against formulas or read-once branching programs would give
NP ⊄ P/poly and hence P ≠ NP. It is non-natural by construction, which is why
Razborov–Rudich does not kill it.

*Correction to the generated version of this candidate.* It was originally
stated as a barely-superlinear **Resolution** lower bound. That is a
proof-complexity analogue and is a different result; the verified magnification
statements are about circuit and formula models. The claim here has been
narrowed to what the literature actually supports. This is the kind of drift
that makes unverified generated mathematics dangerous, and it is why every
candidate is checked before being recorded.

**The obstruction is a barrier of its own.** The locality barrier (Chen,
Hirahara, Oliveira, Pich, Rajgopal, Santhanam; ITCS 2020 / ACM TOCT) explains
why existing lower-bound techniques cannot reach the magnification regime: they
relativise to small fan-in oracle gates, and the required bounds do not. So C3
is not merely "nobody has tried hard enough"; there is a documented reason the
current toolkit falls short, alongside the open auxiliary hypotheses on the
language itself.

**Why C2 is a trap.** "A p-optimal system that is not polynomially bounded" looks
like a strict intermediate. It is not: given p-optimality, "not polynomially
bounded" is *equivalent* to "no system is polynomially bounded", which by
Cook–Reckhow is exactly NP ≠ coNP. And by Lemma A the witnessing family would
have to be a non-recursive subset of TAUT, so it yields no usable object. The
candidate is NP ≠ coNP with a hypothetical noun attached.

**Structural conclusion for this family.** There is no strict-intermediate route
to NP ≠ coNP from proof complexity. Any sufficient condition strictly weaker than
the statement would be a genuine breakthrough, and none is known — the field has
no sufficient condition for NP ≠ coNP other than the definitional restatement.
The universal quantification over proof systems is inescapable, and that
quantification *is* the separation.

## 2. Algebraic and geometric complexity

| Candidate | Verdict | Reaches P vs NP? |
| --- | --- | --- |
| C1: the GCT multiplicity conjecture — some irrep occurring with greater multiplicity in the perm coordinate ring than in the det coordinate ring | **VIABLE** | No |
| C2: `perm ∉ VF` — no polynomial-size arithmetic *formula* for the permanent | **VIABLE**, strictly weaker than VP ≠ VNP | No |
| C3: no polynomial-size *monotone* arithmetic circuit for the permanent | **TRIVIAL** — already a theorem (Jerrum–Snir) | No |
| C4: VP ≠ VNP over 𝔽₂ | **FALSE** — `det ≡ perm (mod 2)` | No |
| C5: PIT ∈ P — deterministic polynomial identity testing | **VIABLE** | No — it gives NEXP ⊄ P/poly, conditionally |

Count of candidates that reach P vs NP: **zero**. That is not timidity; there is
a structural reason, and it is the best finding of this whole exercise.

### The field dilemma

Arithmetic circuits are polynomial-time equivalent to Boolean circuits over
exactly one field: 𝔽₂. There, AND is ×, XOR is +, and NOT is 1 + x, so each model
simulates the other with polynomial overhead. But over 𝔽₂ the hard polynomial
does not exist, because the sign of a permutation is ±1 ≡ 1, so

    det_n ≡ perm_n (mod 2).

Hence perm = det over 𝔽₂, det ∈ VP, and perm is VNP-complete over any field by a
combinatorial reduction, so VP_𝔽₂ = VNP_𝔽₂. Valiant's conjecture is a
characteristic ≠ 2 statement.

So the dilemma is exact: over 𝔽₂ the model matches Boolean computation and there
is no hard polynomial to separate; over characteristic ≠ 2 the hard polynomial
exists and the model does not correspond to Boolean circuits. **There is no field
at which both halves hold at once.** This is not a technicality, and it is why
no algebraic lower bound transports.

### Why the rest of the bridge fails

- **Complete-problem mismatch.** VNP's operator is summation over `{0,1}^m`, i.e.
  weighted counting. Its complete object is the permanent, which is #P-complete.
  `P = NP` does not put counting in FP — Toda gives PH ⊆ P^#P, but collapsing PH
  to P does not make #P tractable. So the Boolean shadow of "perm is easy" is not
  something `P = NP` would even deliver.
- **Asymmetry of the one real transfer.** Kabanets–Impagliazzo run from an
  *algorithm* (derandomising PIT) to a Boolean *lower bound* (NEXP ⊄ P/poly).
  GCT's target is a lower bound, and yields no Boolean statement at all. The only
  side of algebraic complexity that touches Boolean lower bounds is the upper-bound
  side, and it lands at NEXP, far from P vs NP.
- **Non-constructivity is load-bearing in both directions.** GCT's certificate is
  "there exists λ with a multiplicity gap", with no algorithm to find λ;
  multiplicities are #P-hard to compute in this range. That non-constructivity is
  what lets representation theory evade natural proofs — and it is the same fact
  that prevents it from encoding an algorithmic consequence. The evasion and the
  isolation are one property.

**Verdict for this family.** The algebraic arena is not a weaker shadow of the
Boolean one that can be resolved and then transported. Its distinctive features —
symbolic inputs, arbitrary field constants, counting, non-constructive existence
proofs — are themselves the barriers to any bridge. GCT could prove VP ≠ VNP and
P vs NP would remain exactly where it is. Asserting otherwise is rhetoric rather
than implication.

## 3. Algorithmic and structural

### Lemma (no free lunch)

If C implies P ≠ NP, then C is not strictly weaker than P ≠ NP.

*Proof.* Suppose C ⟹ (P ≠ NP). If also (P ≠ NP) ⟹ C, then C is equivalent. If
not, C is strictly stronger. There is no third case. ∎

This is trivial and it kills the naive form of the whole exercise. There is no
"strictly weaker sufficient condition" for P ≠ NP, ever — that is a logical
impossibility, not a research gap. So "a middle conjecture" can only mean one of
two things: a *strengthening* whose route to P ≠ NP runs through named theorems so
that it is more locally attackable, or a *consequence* of P ≠ NP, which is
useless as a route. Every candidate must be classified as one of these.

### Candidates

| Candidate | Implies P ≠ NP? | Status | Obstruction |
| --- | --- | --- | --- |
| NP ⊄ BPP | yes, since P ⊆ BPP | folklore, KNOWN | morally NP ⊄ P/poly behind a derandomisation mask; if BPP = P it *is* P ≠ NP |
| NP ⊄ P/poly | yes, since P ⊆ P/poly | classical, KNOWN | natural proofs + algebrization, triple-blocked |
| PH ≠ Σ₂ | yes, via Karp–Lipton | KNOWN | strictly stronger; Karp–Lipton relativises, so no leverage is inherited |
| W[1] ≠ FPT | yes: P = NP would put k-CLIQUE in P, hence in FPT | KNOWN | the best "algorithmic" rung; ETH ⟹ W[1] ≠ FPT ⟹ P ≠ NP, but every attack is conditional on ETH |
| no sparse ≤p-complete set for NP | **no — implied by P ≠ NP** | direction reversed | Mahaney gives P ≠ NP ⟹ this, not the converse |

**The direction trap, on the record.** The last row is the instructive failure: a
genuine consequence of P ≠ NP with the arrow reversed. Anyone pursuing it has the
implication backwards, and it is easy to do — the statement sounds like a
hardness assertion.

### Killed on sight

- **"SAT ∉ DTIME(n^k)" for fixed k.** Fails direction: SAT could be `n^{k+1}`.
  And "SAT requires superpolynomial time" *is* P ≠ NP, so it is not intermediate
  at all — "superpolynomial" is a step, not a range.
- **Fine-grained conjectures (3SUM, APSP, OV).** The problems are in P, so their
  conjectures are polynomial lower bounds. Direction fails.
- **"No p-optimal algorithm for SAT search."** FALSE — Levin's universal search is
  p-optimal up to a constant factor.
- **NPI ≠ ∅.** Equivalent to P ≠ NP by Ladner, so circular rather than
  intermediate.

### Bottom line for this family

Zero VIABLE. Every candidate that implies P ≠ NP is necessarily a strengthening,
and the strengthenings split into two families: non-uniform circuit lower bounds,
stopped by natural proofs and algebrization; and uniform collapse or
parameterised statements, correct in direction but strictly stronger than
P ≠ NP, with the *implication* relativising so that no non-relativising leverage
is inherited from the route.

The nearest thing to a genuine rung is W[1] ≠ FPT, because it is algorithmic
rather than circuit-theoretic and so escapes the formal statement of natural
proofs. It is still KNOWN, still strictly above P ≠ NP, and has never been
attacked unconditionally.
