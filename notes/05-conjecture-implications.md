# Which conjectures would settle P vs NP, and which only look like they would

P vs NP has no shortage of neighbouring open problems. The useful question is
not "what else is open" but "which of those, if settled, would settle this
one" — and in which direction. Chains of the form

    C₁ ⟹ C₂ ⟹ … ⟹ P ≠ NP

are how progress actually accumulates, provided every arrow is discharged. An
arrow is discharged by an eight-line proof or by a named theorem; anything else
is a wish.

## Conventions

| Status | Meaning |
| --- | --- |
| **PROVEN** | the implication is a theorem |
| **OPEN** | the implication is itself conjectured |
| **FALSE** | this direction fails; the argument is given |
| **UNREVIEWED** | rests on a claim with no human referee |

An arrow with no justification is not recorded. A vaguely-remembered
attribution is recorded without a name rather than with a wrong one.

## 1. Algebraic complexity and proof complexity

VP and VNP are non-uniform families of polynomials computed by arithmetic
circuits, not Boolean complexity classes. The distinction is load-bearing
throughout this section, and it is the reason the 2026 result — whatever its
eventual status — is not a step toward P vs NP.

| From | To | Status | Justification |
| --- | --- | --- | --- |
| `det_n` has a polynomial-size arithmetic circuit | — | **PROVEN** | Berkowitz (1984): division-free determinant in polynomially many operations, in fact NC². |
| every VNP family reduces to `perm` | — | **PROVEN** | Valiant (1979): VNP is the class of p-definable families; `perm_n = Σ_σ Π_i x_{i,σ(i)}` is p-definable and universal under p-projections. |
| `perm ∉ VP` | `VP ≠ VNP` | **PROVEN** (equivalence) | (⇒) `perm ∈ VNP`, so it witnesses the separation. (⇐) VP is closed under p-projections, so `perm ∈ VP` would put all of VNP inside VP. |
| `perm ≤_p det` | `VP = VNP` | **PROVEN** | `det ∈ VP`, and VP is closed under p-projections, so `perm ∈ VP`, and every VNP family reduces to `perm`. The converse is **not known**: `VP = VNP` would give `perm ∈ VP`, i.e. small *circuits* for `perm`, which is weaker than being a projection of `det`. |
| padded `perm` is outside the `GL_{m²}`-orbit closure of `det_m` | `VP ≠ VNP` | **PROVEN** (premise OPEN) | A p-projection of `det_m` lies in that orbit closure, so separating the closures gives `perm ≰_p det`, hence `VP ≠ VNP` by the previous row. Mulmuley–Sohoni (2001). The separation is the GCT target and is open. |
| `perm ∈ FP` on Boolean inputs | `P = NP` | **PROVEN** | `perm` of a 0/1 matrix counts perfect matchings and is #P-complete (Valiant), so `perm ∈ FP` gives `#P ⊆ FP`; Toda (1991) gives `PH ⊆ P^{#P}`, hence `PH = P`. |
| `VP ≠ VNP` | `P ≠ NP` | **OPEN** — no implication in either direction | Different models entirely: arithmetic circuits over a field versus uniform Boolean machines. A Boolean algorithm gives no arithmetic circuits, and an arithmetic lower bound gives no uniform Boolean lower bound. The only proven transfer runs through #P (previous row), not through VP. |
| 2026 claim: `perm` (char ≠ 2) and the Hamiltonian-cycle polynomial need `> m^{c(log m)^{1/3}}` gates over every field, hence `VP ⊊ VNP` | `VP ≠ VNP` | **UNREVIEWED** | Superpolynomial, so if correct it gives `perm ∉ VP` and hence `VP ≠ VNP`. But: Lean-formalised with no human referee, formal-statement fidelity unaudited, no independent reproduction (`github.com/anthropics/formal-math`). Not treated as established here, and per the previous row it would not touch P vs NP even if it were. |
| `NP = coNP` | some propositional proof system is polynomially bounded | **PROVEN** (equivalence) | Cook–Reckhow (1979). (⇐) guess the short proof, verify in poly time, so TAUT ∈ NP = coNP. (⇒) the NP-witness for `φ ∈ TAUT` *is* a proof, and its verifier is the proof system. |
| `P = NP` | some propositional proof system is polynomially bounded | **PROVEN** | `P = NP` gives `NP = coNP`, then Cook–Reckhow. Contrapositive: a superpolynomial lower bound holding for *every* proof system gives `NP ≠ coNP` and hence `P ≠ NP`. |
| pigeonhole formulas `PHP_n` | every Resolution refutation has size `2^{Ω(n)}` | **PROVEN** | Haken (1985). A lower bound for one weak system, and it does not separate NP from coNP — a weak system can fail to be polynomially bounded even if `NP = coNP`. |
| occurrence obstructions separate padded `perm` from the `det` orbit closure | `VP ≠ VNP` | **FALSE** | Bürgisser–Ikenmeyer–Panova (2016): the relevant representation multiplicities are nonzero in the standard setting, so occurrence obstructions cannot do it. Multiplicity obstructions are not ruled out. |

**Reading of this section.** The only route here whose target is genuinely
Boolean is the Cook–Reckhow chain: a superpolynomial lower bound for every
propositional proof system gives `NP ≠ coNP`, hence `P ≠ NP`. Everything within
reach today — Resolution, and weak systems generally — is far too weak to give
that, because a weak system can fail to be polynomially bounded for reasons that
have nothing to do with `NP ≠ coNP`. Reaching P vs NP this way needs bounds for
Frege or Extended Frege, and there are none.

The GCT programme is the barrier-evading route to `VP ≠ VNP`, not to `P ≠ NP`.
Its 2016 setback (occurrence obstructions excluded) pushed it onto multiplicity
obstructions and Kronecker-coefficient positivity, which is hard algebraic
combinatorics with no known technique.

**The central negative result, stated plainly: `VP ≠ VNP` implies nothing known
about P vs NP.** Both directions of the bridge are open. Anyone who tells you
the algebraic separation is progress on P vs NP is conflating two models.

## 2. Structural and logical

Here Σ₀ = P and Σₖ₊₁ = NP^{Σₖ}; a set is *sparse* when it has at most
n^{O(1)} strings of length at most n. Every row is textbook or a labelled
open/failing direction.

| From | To | Status | Justification |
| --- | --- | --- | --- |
| P = NP | NP = coNP | **PROVEN** — formalised | `PVNP.Model.np_eq_conp_of_P_eq_NP`. P is closed under complement (`memP_compl`), so `L ∈ NP ⇔ L ∈ P ⇔ L̄ ∈ P ⇔ L̄ ∈ NP`. |
| NP ≠ coNP | P ≠ NP | **PROVEN** — formalised | `PVNP.Model.ne_of_conp_ne`, the contrapositive of the row above. This is the usable direction: proving NP ≠ coNP settles the question. |
| SAT ∈ P | P = NP | **PROVEN** | SAT is NP-complete (Cook 1971; Levin 1973). Compose the reduction with the decider; P is closed under ≤p (`memP_of_reduces`). The general form is `eq_of_complete_in_P`. |
| P = NP | PH = P | **PROVEN** | Σ₁ = NP = P, and a deterministic machine simulates an oracle call to P in polynomial time, so NP^P = NP; induction gives every Σₖ = P. |
| P ≠ NP | some L ∈ NP∖P is not NP-complete | **PROVEN** (conditional) | Ladner (1975), by diagonalisation against all poly-time deciders and all poly-time reductions. The implication is a theorem; its antecedent is open, so no unconditional intermediate set follows. |
| some sparse set is ≤p-complete for NP | P = NP | **PROVEN** | Mahaney (1982). SAT ≤p S with S sparse lets a left-set search over S decide SAT in polynomial time. Stated for many-one reductions; the Turing-reduction version yields only a collapse of PH, not P = NP. |
| NP ⊆ P/poly | PH = Σ₂ᵖ | **PROVEN** | Karp–Lipton (1980). For L ∈ Π₂, the inner NP predicate has small circuits by hypothesis; self-reducibility turns a circuit for it into one that *finds* the witness, placing L in Σ₂. Hence Π₂ ⊆ Σ₂ and PH = Σ₂. |
| coNP ⊆ NP | NP = coNP | **PROVEN** | If L ∈ NP then L̄ ∈ coNP ⊆ NP, so L = (L̄)̄ ∈ coNP. Symmetrically for NP ⊆ coNP. |
| NP = coNP | PH = NP | **PROVEN** | Standard collapse. If L ∈ Σ₂ via ∃y∀z R, then ∀z R is in coNP = NP, say ∃w S, so L = ∃y∃w S is in NP. Inductively PH = Σ₁. It stops at NP; it does not descend to P. |
| NP = coNP | P = NP | **OPEN** | The converse of the first row. No proof known, and the row above shows why no collapse argument reaches it: NP = coNP collapses PH only to NP, one level above P. |
| NP ⊆ P/poly | P = NP | **OPEN**, expected false | P/poly is non-uniform, so a circuit family for SAT need not yield a uniform algorithm. Karp–Lipton is the strongest known consequence. It is not refutable either, since that requires NP ⊄ P/poly, which is open. |
| L is NP-hard | L is NP-complete | **FALSE** | Completeness is hardness plus membership. Take L NEXP-complete: L is NP-hard since NP ⊆ NEXP, but L ∉ NP, because L ∈ NP with NP closed under ≤p would give NEXP ⊆ NP, contradicting NP ⊊ NEXP by the nondeterministic time hierarchy. |

**Reading of this section.** Row 2 is the highest-leverage target in the whole
map: the implication is already a theorem, so proving its hypothesis settles
P ≠ NP outright, and NP vs coNP separates the two certificate types at the
*same* resource level, which is why it is more tractable than P vs NP itself.

Row 11 is a dead end and worth naming as one. Karp–Lipton is the strongest
consequence the non-uniform hypothesis yields — a collapse, not an algorithm —
and the uniformity gap is precisely the obstruction. The productive non-uniform
programme is the contrapositive, NP ⊄ P/poly, attacked by non-naturalising
lower bounds.

Rows 5 and 6 are not proof routes but constraints. They characterise every
P ≠ NP world, so a claimed proof that makes all NP sets complete, or exhibits a
sparse complete set, is refuted by them without further argument.

## 3. Fine-grained complexity

Reading convention: `A ⟹ B` means B is a consequence of A, so A is at least as
strong. This is not material implication — for a true B, material implication
would be vacuous and every row would hold trivially.

Every conjecture here is either a statement about a problem already in P, or a
bound on the exponent of an NP problem. That split is the whole map: only the
second kind can reach P vs NP, and only downward.

Let `s_k = inf { c : k-SAT ∈ DTIME(2^{cn}) }`, so `s_k ≤ s_{k+1}` and
`s_∞ = lim_k s_k` exists. ETH is `s_∞ > 0`; SETH is `s_∞ = 1`.

| From | To | Status | Justification |
| --- | --- | --- | --- |
| SETH | ETH | **PROVEN** | A k-CNF is a (k+1)-CNF, so `s_k ≤ s_{k+1}`; `s_∞ = 1` gives `s_∞ > 0`. Impagliazzo–Paturi (2001). |
| ETH | P ≠ NP | **PROVEN**, strict | ETH: 3-SAT needs `2^{εn}`. By sparsification (Impagliazzo–Paturi–Zane 2001) the input length is `Θ(n)`, so a polynomial algorithm would run in `2^{O(log n)} = 2^{o(n)}`, contradiction. Strict: `P ≠ NP` permits 3-SAT in `2^{n^{0.9}}`, which ETH forbids. |
| SETH | P ≠ NP | **PROVEN**, strict | Transitive through the two rows above. |
| P ≠ NP | ETH | **OPEN**, believed false | `P ≠ NP` bounds only polynomial time and is consistent with 3-SAT in `2^{n^{0.9}}`. Any derivation must extract `2^{Ω(n)}` bounds from a polynomial separation, hence be non-relativising (Baker–Gill–Solovay). No such technique exists. |
| ETH | SETH | **OPEN**, believed false | ETH gives `lim s_k > 0`; SETH demands the limit be 1. Nothing known drives the limit to 1. This is the one genuine strictness gap in the family. |
| SETH | OV conjecture | **PROVEN** | Williams (2005). A formula with n variables and m clauses gives sets `A, B ⊆ {0,1}^m` of size `2^{n/2}`, with coordinate j recording whether clause j is left unsatisfied; satisfiability is equivalent to some pair being orthogonal. An `n^{2-ε}` OV algorithm would then solve SAT in `2^{(1-δ)n}`. |
| SETH | edit distance needs `n^{2-o(1)}` | **PROVEN** | Backurs–Indyk (2015): an `O(n^{2-δ})` edit-distance algorithm yields a `2^{(1-ε)N}` SAT algorithm. Same conclusion for LCS and DTW (Bringmann–Künnemann; Abboud–Backurs–Vassilevska Williams, 2015). |
| OV conjecture | P ≠ NP | **OPEN** — no implication either way | OV is in `DTIME(n²d) ⊆ P`, so the conjecture is a lower bound *inside* P. `P = NP` yields no subquadratic OV algorithm. |
| 3SUM conjecture | P ≠ NP | **OPEN** — no implication either way | 3SUM is in P, so "3SUM is NP-hard" would give `NP ⊆ P` — the only route collapses the classes in the opposite direction. `P = NP` yields no subquadratic 3SUM algorithm. |
| APSP conjecture | P ≠ NP | **OPEN** — no implication either way | APSP is in P by Floyd–Warshall; NP-hardness of APSP would likewise give `P = NP`. Orthogonal to P vs NP. |
| 3SUM conjecture | Gajentaan–Overmars 3SUM-hard problems need `n^{2-o(1)}` | **PROVEN** (conditional) | Gajentaan–Overmars (1995) give linear-time reductions from 3SUM to the geometric problems; the reductions are unconditional, the lower bound is conditional on the conjecture. |

**The direction trap.** `SETH ⟹ OV` together with `SETH ⟹ P ≠ NP` does *not*
give `OV ⟹ P ≠ NP`. A consequent does not inherit the strength of its
antecedent. This is why the table cannot be read as a hardness hierarchy
leading toward P vs NP: every arrow that reaches P vs NP passes through ETH or
SETH, and the P-time bases (OV, 3SUM, APSP) sit *beside* that chain, not on it.
A stronger hypothesis giving a weaker one says nothing about the weaker one's
own consequences.

**On `strict`.** Proving `B ⇏ A` needs a model where A holds and B fails, which
complexity theory essentially never supplies for these statements. "Strict"
here means "A ⟹ B, and B ⟹ A is neither known nor expected", justified
structurally — not a formal independence result.

## 4. Randomness and derandomisation

Status is that of the *implication*, not of its premise or conclusion. Several
rows are theorems with an open premise, which is exactly what makes them
useful.

| From | To | Status | Justification |
| --- | --- | --- | --- |
| L ∈ BPP | L ∈ Σ₂ᵖ ∩ Π₂ᵖ | **PROVEN** | Sipser (1983); Lautemann (1983). With error `2⁻ᵐ` on m bits, polynomially many shifts of the accepting set cover `{0,1}^m` when `x ∈ L` and cannot when `x ∉ L`; "∃ shifts ∀z: some shift accepts" is Σ₂. BPP is closed under complement, giving Π₂. |
| L ∈ BPP | L ∈ P/poly | **PROVEN** | Adleman (1978). With error `2^{-(n+1)}` some random string is correct on all length-n inputs simultaneously; hardwire it. Non-uniform only — this is not a derandomisation and yields no algorithm. |
| E ⊄ SIZE(2^{εn}) | BPP = P | **PROVEN** (implication) | Impagliazzo–Wigderson (1997), with Nisan–Wigderson (1994) and hard-core sets. A hard function in E is average-case hard by the hard-core lemma; the NW generator gives a poly-time PRG with `O(log n)` seed; enumerate seeds, take a majority. The premise is open and far beyond any proven lower bound. |
| a poly-time PRG with `O(log n)` seed fooling poly-size circuits | some exponential-time function is hard for poly-size circuits | **PROVEN** (implication) | Yao (1982); Nisan–Wigderson (1994). Efficient derandomisation is equivalent, up to parameters, to a circuit lower bound, and cannot be free. |
| PIT ∈ NSUBEXP | NEXP ⊄ P/poly | **PROVEN** (implication) | Kabanets–Impagliazzo (2004). Derandomising one concrete problem is already at least as hard as a major unconditional lower bound. |
| nontrivial deterministic CircuitSAT for C-circuits | NEXP ⊄ C[poly] | **PROVEN** (implication) | Williams (2011), the algorithmic method. For C = ACC⁰ this gives NEXP ⊄ ACC⁰, the first bound against a class containing AC⁰[⊕]. The direction is algorithm ⇒ lower bound, the reverse of IW. |
| P = NP | BPP = P | **PROVEN** | Sipser–Lautemann gives BPP ⊆ Σ₂, and P = NP forces Σ₂ = P. So randomness cannot help in the P = NP world. |
| BPP = P | P = NP | **OPEN**, expected false | Uniform derandomisation says nothing about nondeterminism. The expected world is `P ≠ NP ∧ BPP = P`. |
| P ≠ NP | BPP ≠ P | **OPEN** | The expected world has NP hard and randomness useless at the same time, so `P ≠ NP` carries no information here. |
| a one-way function exists | a poly-time PRG with linear seed, secure against poly-size circuits | **PROVEN** | Håstad–Impagliazzo–Levin–Luby (1999); Blum–Micali (1984); Goldwasser–Micali (1984). Caveat: seed length `Ω(n)`, so the seed space cannot be enumerated — one-way functions do **not** give BPP = P. |
| a one-way function exists | P ≠ NP | **PROVEN** | If P = NP then FNP ⊆ FP by search-to-decision, so every poly-time function is invertible, contradicting one-wayness. |
| trapdoor OWFs exist (public-key crypto) | OWFs exist | **PROVEN** | Definitional in Impagliazzo's five worlds (1995). |

**Reading of this section.** Two things here are load-bearing.

The reverse direction rows — PRG ⇒ lower bound, PIT ⇒ NEXP ⊄ P/poly, CircuitSAT
⇒ lower bound — are the cleanest structural facts in the map, because they are
proven and they delimit what can be free. "Prove BPP = P without new lower
bounds" is therefore not a plausible programme.

The bottleneck is the IW premise, `E ⊄ SIZE(2^{εn})`, and it is blocked from
below by natural proofs: the IW generator is a pseudorandom object, so any
*natural* property certifying the needed lower bound would also break the PRG.
Promising technology must be non-natural, which again points at Williams-style
algorithmic bounds or algebraic methods.

**A correction worth recording.** The claim "P = NP settles BPP" is *true*, not
a tempting error: BPP ⊆ Σ₂ by Sipser–Lautemann, and P = NP collapses Σ₂ to P.
The tempting errors in this area lie the other way — `BPP = P ⟹ P = NP` (open,
expected false) and the dual `P = NP ⟹ BPP ≠ P` (equivalent to P ≠ NP, hence
open). None of the interesting statements in this family is provably false;
refuting any would itself need P ≠ NP.

## 5. Non-uniform circuit complexity

The open items in this family are the *antecedents*, not the arrows. What the
table records is which arrows are theorems and which are dead routes — two of
which are inferences people make.

| From | To | Status | Justification |
| --- | --- | --- | --- |
| NP ⊆ P/poly | PH = Σ₂ᵖ | **PROVEN** | Karp–Lipton (1980), proved in §2. The argument relativises, so this arrow is not the step that escapes the relativisation barrier. |
| PH is infinite | NP ⊄ P/poly | **PROVEN** | Contrapositive of Karp–Lipton: `PH ≠ Σ₂ ⟹ NP ⊄ P/poly`. |
| PH is infinite | P ≠ NP | **PROVEN** | Previous row with `P ⊆ P/poly`; equivalently `P = NP ⟹ PH = P`. Relativises. |
| NP ⊄ P/poly | P ≠ NP | **PROVEN** | `P ⊆ P/poly`, so `NP ⊄ P/poly` forces `NP ≠ P`. Pure inclusion; relativises. |
| NEXP ⊆ P/poly | contradiction | **PROVEN** | Buhrman–Fortnow–Thierauf (1998). The proof is explicitly non-relativising. This separates at NEXP and says nothing about NP. |
| NEXP ⊆ ACC⁰ | contradiction | **PROVEN** | Williams (2011, JACM 2014). |
| NEXP ⊄ ACC⁰ | P ≠ NP | **FALSE** | `ACC⁰ ⊆ TC⁰ ⊆ NC¹ ⊆ P/poly`, so a bound against ACC⁰ carries no P/poly content unless the classes coincide; more decisively, hardness at NEXP does not descend to NP. The antecedent is a theorem while the consequent is open, so the arrow cannot itself be one. |
| NEXP ⊄ P/poly | NP ⊄ P/poly | **FALSE** | `NP ⊆ NEXP`; a lower bound for the superset does not transfer to a subset — NP could have polynomial-size circuits while some NEXP language does not. Again the antecedent is proved and the consequent open. |

**The frontier is NEXP versus EXP.** `NEXP ⊄ P/poly` is proved; `EXP ⊄ P/poly`,
`E ⊄ P/poly` and `NP ⊄ P/poly` are all open. The BFT argument uses
exponential-length witnesses and diagonalisation, and does not descend a level.
For scale: `NP ⊆ P/poly` would give `NEXP = MA` (Impagliazzo–Kabanets–Wigderson
2002) — a collapse, not a separation.

**`NP ⊄ P/poly` is the sharpest sufficient target in the whole map.** One
statement about one class, known one exponential up, and proving it settles
P ≠ NP outright. It is sufficient but not necessary: P ≠ NP can hold with
NP ⊆ P/poly, in which case Karp–Lipton collapses PH instead. So it is stronger
than the question it would settle, and the NP-versus-NEXP gap is the distance.

**`PH` infinite is not an independent shortcut.** Karp–Lipton converts it into
`NP ⊄ P/poly`, and Karp–Lipton relativises; the active ingredient is still the
non-relativising circuit separation.

## Synthesis

Strip the five sections to their arrows and a shape appears.

**Four proven arrows reach P ≠ NP.** Each is a theorem whose antecedent is open:

| Antecedent | Arrow | Reachable how |
| --- | --- | --- |
| NP ≠ coNP | proven | formalised in this repository |
| NP ⊄ P/poly | proven | proven one exponential up (NEXP) |
| ETH (or SETH) | proven | proven only for restricted models |
| PH infinite | proven | reduces to `NP ⊄ P/poly` via Karp–Lipton |

Everything else on the map is either a proven *dead end* — Karp–Lipton cannot
give an algorithm, VP ≠ VNP cannot reach Boolean classes, the fine-grained bases
live inside P, efficient derandomisation is equivalent to a lower bound — or an
inference that looks valid and is not (`NEXP ⊄ ACC⁰ ⟹ P ≠ NP`,
`NEXP ⊄ P/poly ⟹ NP ⊄ P/poly`, `SETH ⟹ OV ⟹ P ≠ NP`).

**Why the map has this shape.** The arrows that reach P ≠ NP all run through
circuit lower bounds or proof complexity. The arrows that are easy to prove —
Karp–Lipton, the collapses, the fine-grained reductions — relativise, and
relativising arguments cannot separate P from NP (Baker–Gill–Solovay). The one
non-relativising technique that has produced a genuine bound, Williams'
algorithmic method, reaches ACC⁰ and not NC¹. The one non-naturalising
programme with a concrete target, GCT, reaches VP ≠ VNP and not NP ⊄ P/poly.

So the open links are not scattered. They cluster at a single statement:
**a superpolynomial circuit lower bound for an explicit function in NP**. Every
route in this document either reaches that statement or dies before it.

**What this means for "getting closer".** Progress here is not measured in
proximity, because there is no metric. It is measured in which links get
discharged. The four antecedents above are where a discharge would land, and
of them `NP ≠ coNP` and `NP ⊄ P/poly` are the two whose arrows are already
theorems — nothing further needs proving once the antecedent falls.

That is the honest content of a conjecture-to-conjecture map: not a path to the
answer, but a precise statement of which of four doors is worth pushing, and a
list of the doors that only look like doors.
