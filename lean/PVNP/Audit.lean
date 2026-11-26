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
#print axioms PVNP.Model.memP_congr
#print axioms PVNP.Model.memP_compl
#print axioms PVNP.Model.memP_inter
#print axioms PVNP.Model.memP_union
#print axioms PVNP.Model.np_eq_conp_of_P_eq_NP
#print axioms PVNP.Model.ne_of_conp_ne
#print axioms PVNP.Model.ne_of_np_not_subset
#print axioms PVNP.Model.subset_of_P_eq_NP

-- abelian squares (correction to arXiv:2604.23188)
#print axioms PVNP.countA_append
#print axioms PVNP.not_isAbelianSquare_of_countA_one
#print axioms PVNP.countA_bab
#print axioms PVNP.isAbelianSquare_factor_of_bab_is_all_b
