/-
What follows from the definitions in `PVNP/Basic.lean`.

All of it is genuinely proved, and none of it decides the question. The
structure of the file is the structure of the problem: every route to P = NP
goes through a polynomial-time algorithm for an NP-hard language, and the
barrier theorems of `notes/02-barriers.md` explain why no route to P ≠ NP
survives.

The last theorem, `collapse_of_complete_in_P`, is the formal content of the
standard slogan "one algorithm for SAT settles the question". Everything it
depends on is a hypothesis about a *specific* language being in P, which is why
it proves nothing on its own.
-/

import PVNP.Basic
import PVNP.Arith

namespace PVNP
namespace Model

/-- P is contained in NP. A polynomial-time decider *is* a polynomial-time
verifier that ignores its certificate. -/
theorem memP_subset_memNP (M : Model) {L : Language} (h : M.MemP L) : M.MemNP L := by
  obtain ⟨V, hPT, hdec⟩ := h
  refine ⟨fun s _ => V s [], 0, M.pt_ignore hPT, ?_⟩
  intro s
  rw [← hdec s]
  constructor
  · intro hs; exact ⟨[], by simp, hs⟩
  · rintro ⟨w, _, hV⟩; exact hV

/-- P is closed under polynomial-time many-one reduction. -/
theorem memP_of_reduces (M : Model) {L L' : Language}
    (hred : M.Reduces L L') (hP : M.MemP L') : M.MemP L := by
  obtain ⟨f, c, hc, hf, hlen, hiff⟩ := hred
  obtain ⟨V, hPT, hdec⟩ := hP
  refine ⟨fun s w => V (f s) w, M.pt_precomp hf hPT, ?_⟩
  intro s
  rw [hiff s]
  exact hdec (f s)

/-- NP is closed under polynomial-time many-one reduction. This is what makes
NP-hardness a meaningful notion: hardness transfers upward along reductions,
and membership transfers downward. The certificate length is filtered to the
pulled-back bound, which is where `PVNP/Arith.lean` is used. -/
theorem memNP_of_reduces (M : Model) {L L' : Language}
    (hred : M.Reduces L L') (hNP : M.MemNP L') : M.MemNP L := by
  obtain ⟨f, c, hc, hf, hlen, hiff⟩ := hred
  obtain ⟨V, k, hPT, hcorr⟩ := hNP
  refine ⟨fun s w => V (f s) w && decide (w.length ≤ ((f s).length + 2) ^ k),
    2 * c * k, M.pt_precomp hf (M.pt_and hPT (M.pt_lengthTest k)), ?_⟩
  intro s
  rw [hiff s]
  have hs : (f s).length + 2 ≤ (s.length + 2) ^ c + 2 := by
    have := hlen s
    omega
  have hbound : ((f s).length + 2) ^ k ≤ (s.length + 2) ^ (2 * c * k) := by
    calc
      ((f s).length + 2) ^ k ≤ ((s.length + 2) ^ c + 2) ^ k :=
        Nat.pow_le_pow_left hs k
      _ ≤ ((s.length + 2) ^ (2 * c)) ^ k :=
        Nat.pow_le_pow_left (pow_add_two_add_two_le hc) k
      _ = (s.length + 2) ^ (2 * c * k) :=
        (Nat.pow_mul (s.length + 2) (2 * c) k).symm
  constructor
  · intro hL
    obtain ⟨w, hw, hV⟩ := (hcorr (f s)).1 hL
    have hW : (V (f s) w && decide (w.length ≤ ((f s).length + 2) ^ k)) = true := by
      simp only [hV, Bool.true_and, decide_eq_true_eq]
      exact hw
    exact ⟨w, Nat.le_trans hw hbound, hW⟩
  · rintro ⟨w, hw, hV⟩
    have hsplit : V (f s) w = true ∧ w.length ≤ ((f s).length + 2) ^ k := by
      simpa only [Bool.and_eq_true, decide_eq_true_eq] using hV
    exact (hcorr (f s)).2 ⟨w, hsplit.2, hsplit.1⟩

/-- Reducibility is reflexive. -/
theorem reduces_refl (M : Model) (L : Language) : M.Reduces L L := by
  refine ⟨id, 1, by omega, M.ptMap_id, ?_, fun s => Iff.rfl⟩
  intro s
  simp

/-- Reducibility is transitive. -/
theorem reduces_trans (M : Model) {L₁ L₂ L₃ : Language}
    (h₁ : M.Reduces L₁ L₂) (h₂ : M.Reduces L₂ L₃) : M.Reduces L₁ L₃ := by
  obtain ⟨f, c, hc, hf, hflen, hfiff⟩ := h₁
  obtain ⟨g, d, hd, hg, hglen, hgiff⟩ := h₂
  refine ⟨fun s => g (f s), 2 * c * d, ?_, M.ptMap_comp hf hg, ?_, ?_⟩
  · have : 0 < 2 * c * d :=
      Nat.mul_pos (Nat.mul_pos (by omega) (by omega)) (by omega)
    omega
  · intro s
    have hs : (f s).length + 2 ≤ (s.length + 2) ^ c + 2 := by
      have := hflen s
      omega
    calc
      (g (f s)).length ≤ ((f s).length + 2) ^ d := hglen (f s)
      _ ≤ ((s.length + 2) ^ c + 2) ^ d := Nat.pow_le_pow_left hs d
      _ ≤ ((s.length + 2) ^ (2 * c)) ^ d :=
        Nat.pow_le_pow_left (pow_add_two_add_two_le hc) d
      _ = (s.length + 2) ^ (2 * c * d) :=
        (Nat.pow_mul (s.length + 2) (2 * c) d).symm
  · intro s
    rw [hfiff s, hgiff (f s)]

/-- An NP-hard language in P puts all of NP in P. -/
theorem memNP_subset_memP_of_hard_in_P (M : Model) {L₀ : Language}
    (hhard : M.NPHard L₀) (hP : M.MemP L₀) :
    ∀ {L : Language}, M.MemNP L → M.MemP L :=
  fun hNP => M.memP_of_reduces (hhard _ hNP) hP

/-- A polynomial-time algorithm for an NP-complete language collapses the two
classes. -/
theorem eq_of_complete_in_P (M : Model) {L₀ : Language}
    (hc : M.IsNPComplete L₀) (hP : M.MemP L₀) :
    ∀ L : Language, M.MemP L ↔ M.MemNP L :=
  fun _ => ⟨M.memP_subset_memNP,
    fun hNP => M.memNP_subset_memP_of_hard_in_P hc.2 hP hNP⟩

/-- If the classes differ, some language in NP is outside P. -/
theorem exists_separator_of_ne (M : Model)
    (h : ¬ ∀ L : Language, M.MemP L ↔ M.MemNP L) :
    ∃ L : Language, M.MemNP L ∧ ¬ M.MemP L := by
  by_cases hex : ∃ L : Language, M.MemNP L ∧ ¬ M.MemP L
  · exact hex
  · exfalso
    apply h
    intro L
    exact ⟨M.memP_subset_memNP, fun hNP =>
      match Classical.em (M.MemP L) with
      | Or.inl hP => hP
      | Or.inr hP => absurd ⟨L, hNP, hP⟩ hex⟩

/-- `MemP` respects logical equivalence of languages. -/
theorem memP_congr (M : Model) {L₁ L₂ : Language}
    (h : ∀ s : BinStr, L₁ s ↔ L₂ s) (hP : M.MemP L₁) : M.MemP L₂ := by
  obtain ⟨V, hPT, hdec⟩ := hP
  exact ⟨V, hPT, fun s => (hdec s).trans (h s)⟩

/-- P is closed under complement. -/
theorem memP_compl (M : Model) {L : Language} (h : M.MemP L) :
    M.MemP (fun s => ¬ L s) := by
  obtain ⟨V, hPT, hdec⟩ := h
  refine ⟨fun s w => Bool.not (V s w), M.pt_not hPT, ?_⟩
  intro s
  rw [not_eq_true_iff, hdec s]

/-- P is closed under intersection. -/
theorem memP_inter (M : Model) {L₁ L₂ : Language}
    (h₁ : M.MemP L₁) (h₂ : M.MemP L₂) : M.MemP (fun s => L₁ s ∧ L₂ s) := by
  obtain ⟨V₁, hP₁, hd₁⟩ := h₁
  obtain ⟨V₂, hP₂, hd₂⟩ := h₂
  refine ⟨fun s w => V₁ s w && V₂ s w, M.pt_and hP₁ hP₂, ?_⟩
  intro s
  rw [Bool.and_eq_true]
  exact ⟨fun ⟨a, b⟩ => ⟨(hd₁ s).1 a, (hd₂ s).1 b⟩,
    fun ⟨a, b⟩ => ⟨(hd₁ s).2 a, (hd₂ s).2 b⟩⟩

/-- P is closed under union. -/
theorem memP_union (M : Model) {L₁ L₂ : Language}
    (h₁ : M.MemP L₁) (h₂ : M.MemP L₂) : M.MemP (fun s => L₁ s ∨ L₂ s) := by
  obtain ⟨V₁, hP₁, hd₁⟩ := h₁
  obtain ⟨V₂, hP₂, hd₂⟩ := h₂
  refine ⟨fun s w => V₁ s w || V₂ s w, M.pt_or hP₁ hP₂, ?_⟩
  intro s
  rw [Bool.or_eq_true]
  exact ⟨fun h => h.elim (fun a => Or.inl ((hd₁ s).1 a)) (fun b => Or.inr ((hd₂ s).1 b)),
    fun h => h.elim (fun a => Or.inl ((hd₁ s).2 a)) (fun b => Or.inr ((hd₂ s).2 b))⟩

/-- If P = NP then NP is closed under complement, i.e. NP = coNP. -/
theorem np_eq_conp_of_P_eq_NP (M : Model)
    (h : ∀ L : Language, M.MemP L ↔ M.MemNP L) (L : Language) :
    M.MemNP (fun s => ¬ L s) ↔ M.MemNP L := by
  constructor
  · intro hc
    have hP : M.MemP (fun s => ¬ L s) := (h _).2 hc
    have hP' : M.MemP (fun s => ¬ ¬ L s) := M.memP_compl hP
    exact (h L).1 (M.memP_congr
      (fun s => ⟨fun hnn => Classical.byContradiction hnn, fun hs hnn => hnn hs⟩) hP')
  · intro hNP
    exact (h _).1 (M.memP_compl ((h L).2 hNP))

/-- The contrapositive, which is the usable form: a proof that NP ≠ coNP would
settle P ≠ NP. -/
theorem ne_of_conp_ne (M : Model)
    (h : ¬ ∀ L : Language, M.MemNP L ↔ M.MemNP (fun s => ¬ L s)) :
    ¬ ∀ L : Language, M.MemP L ↔ M.MemNP L := by
  intro hP
  exact h fun L => (M.np_eq_conp_of_P_eq_NP hP L).symm

end Model
end PVNP
