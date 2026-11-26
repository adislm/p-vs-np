# P vs NP: definitions, barriers, and a Lean formalisation of what is settled

P vs NP is open. This repository does not settle it, and no part of it claims
to. What it contains is the part that can be done properly in one sitting: a
precise statement of the problem, a machine-checked development of the
implication structure, and a write-up of the three barrier theorems that rule
out the obvious lines of attack.

## Status

| Claim | Status |
| --- | --- |
| P ⊆ NP | proved in Lean, conditional on `Model` |
| P closed under ≤p | proved in Lean, conditional on `Model` |
| NP closed under ≤p | proved in Lean, conditional on `Model` |
| ≤p is a preorder | proved in Lean |
| NP-hard ∩ P ≠ ∅ ⟹ P = NP | proved in Lean |
| P closed under complement, ∪, ∩ | proved in Lean |
| P = NP ⟹ NP = coNP | proved in Lean |
| NP ≠ coNP ⟹ P ≠ NP | proved in Lean |
| P ≠ NP | **open** |

The `Model` parameter is a bundle of standard facts about polynomial time.
`PVNP/Basic.lean` takes `PT` as primitive; there is no machine model and no
runtime measure. `notes/01-definitions.md` explains why that is the right
split, and `notes/01-definitions.md` plus the file comments state exactly what
is assumed.

## Build

Requires a Lean 4 toolchain (elan). From a checkout:

```
cd lean
lake build
```

Axiom audit — every theorem should report only `propext`, `Quot.sound`, or
`Classical.choice`; any `sorryAx` would mean a hole:

```
cd lean
lake env lean PVNP/Audit.lean
```

Current output:

```
'PVNP.Model.memP_subset_memNP' depends on axioms: [propext]
'PVNP.Model.memP_of_reduces' depends on axioms: [propext]
'PVNP.Model.memNP_of_reduces' depends on axioms: [propext, Quot.sound]
'PVNP.Model.reduces_refl' depends on axioms: [propext, Quot.sound]
'PVNP.Model.reduces_trans' depends on axioms: [propext, Quot.sound]
'PVNP.Model.memNP_subset_memP_of_hard_in_P' depends on axioms: [propext]
'PVNP.Model.eq_of_complete_in_P' depends on axioms: [propext]
'PVNP.Model.exists_separator_of_ne' depends on axioms: [propext, Classical.choice, Quot.sound]
'PVNP.Model.memP_congr' does not depend on any axioms
'PVNP.Model.memP_compl' depends on axioms: [propext]
'PVNP.Model.memP_inter' depends on axioms: [propext]
'PVNP.Model.memP_union' depends on axioms: [propext]
'PVNP.Model.np_eq_conp_of_P_eq_NP' depends on axioms: [propext, Classical.choice, Quot.sound]
'PVNP.Model.ne_of_conp_ne' depends on axioms: [propext, Classical.choice, Quot.sound]
```

## Layout

```
notes/
  01-definitions.md      P, NP, reductions; what the formalisation covers
  02-barriers.md         relativisation, natural proofs, algebrisation
  03-state-of-play.md    known lower bounds, what would count, why an LLM cannot settle it
  05-conjecture-implications.md  which conjectures would settle P vs NP, and which only look like they would
  06-falsification-checklist.md  how to test a claimed proof, with the barrier statements
  07-claim-audit.md      three claimed resolutions checked against the source artifacts
  08-candidate-conjectures.md  an experiment: generate middle conjectures, try to kill them
  09-cross-field.md      the transfer filter, and six adjacent fields under survey
  10-2026-record.md      verified snapshot of what moved in 2026
  11-frontier-programmes.md  bounded arithmetic, meta-complexity, the algorithmic method
  12-experimental-search.md  counterexample hunts: one falsification, the rest survived
  13-deep-audits.md      line-by-line audits of recent papers
  14-swarm-batch.md      twenty concurrent audits, updated as they report
lean/
  PVNP/Basic.lean        languages, PolyTime, MemP, MemNP, Reduces, NP-hard/complete
  PVNP/Arith.lean        the length arithmetic behind closure of NP under reduction
  PVNP/Results.lean      the theorems
  PVNP/Audit.lean        axiom audit
```

## The short version of the state of play

- SAT is NP-complete, so P = NP iff SAT ∈ P.
- Any proof of P = NP must be a lower bound against every polynomial-time
  machine. Any proof of P ≠ NP must produce a polynomial-time algorithm for an
  NP-hard language.
- Relativisation (Baker–Gill–Solovay 1975), natural proofs (Razborov–Rudich
  1997), and algebrisation (Aaronson–Wigderson 2008) each rule out a large
  family of techniques, and each was built by attacking the escape from the
  previous one.
- The best explicit general-circuit lower bound is linear in the input size.
  P ≠ NP needs superpolynomial. The gap between the two is the problem.
- The *algebraic* analogue, VP vs VNP, was claimed settled on 2026-11-23
  (Anthropic, Lean-formalised, no human referee, and explicitly not a result
  about P vs NP). See `notes/03-state-of-play.md`.

See `notes/` for statements and proof sketches.
