# State of play, and what would actually count as progress

## Known

- SAT is NP-complete (Cook 1971; Levin 1973).
- Nondeterministic time hierarchy: NP ⊊ NEXP. Deterministic: P ⊊ EXP.
- Ladner (1975): if P ≠ NP there are NP-intermediate languages — neither in P
  nor NP-complete.
- Mahaney (1982): if P ≠ NP, no NP-complete language is sparse. Equivalently,
  no NP-complete language has polynomial-size circuits unless P = NP.
- Karp–Lipton (1980): NP ⊆ P/poly implies PH = Σ₂. So a non-uniform algorithm
  for SAT collapses the polynomial hierarchy two levels.
- If P = NP then PH = P; the whole hierarchy collapses.

So P ≠ NP is the *weakest* of the natural separations one might hope to prove,
and it is the one nobody can prove.

## Where the lower bounds actually reach

| Statement | Status |
| --- | --- |
| PARITY ∉ AC⁰ | proved (Ajtai 1983; Furst–Saxe–Sipser 1984) |
| CLIQUE ∉ monotone P/poly | proved, exponential (Razborov 1985; Alon–Boppana 1987) |
| NEXP ⊄ ACC⁰ | proved (Williams 2011) |
| NEXP ⊄ P/poly | proved, non-constructively (Buhrman–Fortnow–Thierauf 1998) |
| NP ⊄ P/poly | **open** |
| an explicit function in NP with ω(n) gate lower bound against general circuits | **open** |

The best explicit general-circuit lower bound is linear up to a small constant
(around 3n gates, Find–Golovnev–Hirsch–Kulikov 2016). Everything above linear
is open. That gap — linear to superpolynomial — is the entire distance to
P ≠ NP.

## What would count

In decreasing order of strength:

1. **A superpolynomial lower bound for an explicit function in NP against
   general circuits.** This gives NP ⊄ P/poly, hence P ≠ NP.
2. **A lower bound against a circuit class that provably evades the three
   barriers.** Williams' ACC⁰ result is the template; nobody has lifted it.
3. **A conditional theorem.** P ≠ NP from an assumption weaker than P ≠ NP, but
   one that is itself plausible and not known to imply P ≠ NP.
4. **A refutation of a barrier.** Exhibit a technique that does what the
   barrier says is impossible, e.g. a natural property that survives without
   breaking pseudorandom functions. This would be a result about the barrier,
   not about P vs NP, and would be major on its own.

What does **not** count, and is worth naming because it is what nearly all
attempts produce:

- A proof that relativises. Dead by Baker–Gill–Solovay.
- A proof that treats all functions uniformly and decidably from truth tables.
  Dead by Razborov–Rudich.
- A diagonalisation against a *particular* machine or a particular algorithm.
  The statement quantifies over all machines, so refuting one proves nothing.
- Numerical evidence. SAT solvers handle large instances and fail on structured
  ones; that says something about solvers, not about NP.

## Why a language model cannot settle this

Worth being blunt, because it is the honest answer to "can we prove it":

- The statement is quantified over all Turing machines and all constants. A
  finite search cannot discharge a quantifier that is not finite.
- Three barrier theorems are specifically designed to rule out the families of
  arguments that can be produced without new mathematics. Producing a proof
  requires an idea that is not in the literature, which is by construction not
  something that can be recalled.
- Formal verification does not help with discovery. Lean checks a proof once it
  exists; it cannot search a space of proofs of this size.

What a language model can do, and what this repository is:

- State the problem exactly, and formalise the part that is settled.
- Write down the barriers precisely enough that a proposed argument can be
  checked against them.
- Formalise known theorems (Cook–Levin, Ladner, Karp–Lipton) as a durable
  reference.
- Catch the specific error classes above in a proposed proof.

## On the linked repository

`1337isnot1337/solved-conjectures` lists roughly a hundred problems with Lean
status icons, and imports "Anthropic's VP ≠ VNP theorem" as a standing
assumption while stating it does not establish it. VP vs VNP is itself open —
it is the algebraic analogue of P vs NP and is not known in either direction.
A repository that assumes an open separation as an axiom has not proved
anything conditional on that axiom that bears on the open problem.

The status icons distinguish "Lean-verified" from "no Lean verification", which
is a good practice. It is not a substitute for peer review, and the repository
says so. Treat it as an interesting source of problems and formalisation
scaffolding, not as a source of results.
