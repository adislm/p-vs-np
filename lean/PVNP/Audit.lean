/-
Axiom audit. Every theorem below must report no `sorryAx`.

`Classical.em` shows up in `exists_separator_of_ne` only because that statement
is nonconstructive (it is a classical case split), not because anything is
assumed about P or NP.

Run with `lake build`, or `lake env lean PVNP/Audit.lean` for the output.
-/

import PVNP

#print axioms PVNP.Model.memP_subset_memNP
#print axioms PVNP.Model.memP_of_reduces
#print axioms PVNP.Model.memNP_of_reduces
#print axioms PVNP.Model.reduces_refl
#print axioms PVNP.Model.reduces_trans
#print axioms PVNP.Model.memNP_subset_memP_of_hard_in_P
#print axioms PVNP.Model.eq_of_complete_in_P
#print axioms PVNP.Model.exists_separator_of_ne
