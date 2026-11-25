# Definitions, and where the formalisation stops

## The statement

Let Σ = {0,1}, Σ* the set of finite binary strings, and a **language** a subset
L ⊆ Σ*. Write |x| for length.

**P** is the class of L for which there is a deterministic Turing machine M and
a constant k such that M decides L and M halts within |x|^k + k steps on every
input x.

**NP** is the class of L for which there are a relation R ⊆ Σ* × Σ* and a
constant k such that

- R is decidable in time (|x| + |y|)^k + k, and
- x ∈ L ⟺ ∃y, |y| ≤ |x|^k + k and R(x,y).

y is the *certificate*. Equivalently NP is the class decided by a
nondeterministic machine in polynomial time.

The question is whether P = NP.

## Three equivalent formulations

These are equivalent, and each is useful for a different purpose:

1. **Machine form.** As above.
2. **Verifier form.** P = NP iff every polynomial-time verifiable relation has
   a polynomial-time decision procedure.
3. **Optimal-algorithm form.** P = NP iff some NP-hard language is in P. This
   is the formal content of "one fast SAT solver settles everything", and it is
   what `PVNP/Results.lean` proves as `eq_of_complete_in_P`.

The equivalence of (3) with the others is where Cook–Levin enters: SAT is
NP-complete (Cook 1971, Levin 1973), so an NP-hard language in P gives SAT ∈ P.

## What is formalised in this repository, and what is not

`PVNP/Basic.lean` takes `PT : Pred → Prop` as **primitive**. There is no
machine, no step counter, and no runtime measure. The fields of `Model` are the
facts a textbook uses without comment:

| Field | Content |
| --- | --- |
| `pt_ignore` | a poly-time procedure may ignore its second argument |
| `ptMap_id` | the identity transducer is poly-time |
| `ptMap_comp` | poly-time transducers compose |
| `pt_precomp` | substituting a poly-time transducer into the first argument preserves `PT` |
| `pt_and` | poly-time is closed under conjunction |
| `pt_lengthTest` | deciding `|w| ≤ (|x|+2)^k` is poly-time |

Each of these is true, routine, and uninteresting. Proving them against a real
machine model is the long half of the project and would add no insight into
P vs NP. The reason is worth stating plainly: **the difficulty of P vs NP is
not in the definitions.** Every textbook proof of "P ⊆ NP" or "NP is closed
under ≤p" is three lines. The difficulty is a lower bound quantified over all
machines and all constants, and no amount of modelling work touches that.

So this repository formalises the implication structure and is explicit that
it does not formalise the hard part. `notes/02-barriers.md` explains why the
hard part resists the obvious tools.

## Reductions

`L ≤p L'` (L polynomial-time many-one reduces to L') means there is a
poly-time f with x ∈ L ⟺ f(x) ∈ L'.

`PVNP/Basic.lean` records the growth exponent c with `|f(x)| ≤ (|x|+2)^c`,
`c ≥ 1`. The `+2` is a normalisation: it keeps the base at least 2, so
`(n+2)^c ≥ 2` unconditionally and `x + 2 ≤ x²` for `x ≥ 2`, which is exactly
what makes two polynomial bounds compose into one polynomial bound. The
composition bound `2cd` is proved in `PVNP/Arith.lean`; without it the
statement "NP is closed under ≤p" is not provable from the definitions at all,
because the pulled-back certificate bound would not be polynomial.

## What the Lean file proves

All conditional on `Model`, all without `sorry`:

- `memP_subset_memNP` : P ⊆ NP
- `memP_of_reduces` : P is closed under ≤p
- `memNP_of_reduces` : NP is closed under ≤p
- `reduces_refl`, `reduces_trans` : ≤p is a preorder
- `memNP_subset_memP_of_hard_in_P` : NP-hard ∩ P ≠ ∅ ⟹ NP ⊆ P
- `eq_of_complete_in_P` : NP-complete ∩ P ≠ ∅ ⟹ P = NP
- `exists_separator_of_ne` : P ≠ NP ⟹ ∃L ∈ NP \ P

`PVNP/Audit.lean` prints the axiom dependencies. None is `sorryAx`.
