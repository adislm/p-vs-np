/-
The structural lemma behind the correction to Theorem 6 of arXiv:2604.23188.

The paper claims that the only words with one `a` and exactly `M(1,n)` abelian
squares are `b^⌈(n−1)/2⌉ a b^⌊(n−1)/2⌋` and its reverse. That is false (see
`notes/12-experimental-search.md`). The reason is a one-line observation:

  a word of the form `b^i a b^j` contains exactly one `a`, and an abelian square
  splits into two halves with the same letter counts. Equal counts summing to one
  would have to be 1/2 each. So no abelian-square factor can contain the `a`.

Everything else in the correction follows from that. This file proves it.
-/

namespace PVNP

/-- Words over a two-letter alphabet: `true` is `b`, `false` is `a`. -/
abbrev Word : Type := List Bool

/-- The number of occurrences of `a`, that is, of `false`. -/
def countA : Word → Nat
  | [] => 0
  | x :: xs => (if x then 0 else 1) + countA xs

/-- A word is an abelian square when it splits into two equal-length halves
carrying the same multiset of letters. Since the halves have equal length, equal
`a`-counts is the same condition as equal multisets. -/
def IsAbelianSquare (v : Word) : Prop :=
  ∃ p : Nat, v.length = 2 * p ∧ countA (v.take p) = countA (v.drop p)

/-- `v` occurs as a contiguous factor of `w`. -/
def IsFactor (v w : Word) : Prop := ∃ s t : Word, w = s ++ v ++ t

theorem countA_append (u v : Word) : countA (u ++ v) = countA u + countA v := by
  induction u with
  | nil => simp [countA]
  | cons x xs ih =>
    simp only [List.cons_append, countA]
    rw [ih]
    omega

/-- The key lemma. A word with exactly one `a` is never an abelian square: the
halves would need equal `a`-counts, and those counts sum to one. -/
theorem not_isAbelianSquare_of_countA_one {v : Word} (h : countA v = 1) :
    ¬ IsAbelianSquare v := by
  rintro ⟨p, _hlen, heq⟩
  have hsplit : v = v.take p ++ v.drop p := (List.take_append_drop p v).symm
  have hsum : countA v = countA (v.take p) + countA (v.drop p) := by
    have hcongr := congrArg countA hsplit
    rwa [countA_append] at hcongr
  rw [heq] at hsum
  omega

theorem countA_le_of_isFactor {v w : Word} (h : IsFactor v w) : countA v ≤ countA w := by
  obtain ⟨s, t, rfl⟩ := h
  rw [countA_append, countA_append]
  omega

theorem countA_replicate_true (n : Nat) : countA (List.replicate n true) = 0 := by
  induction n with
  | zero => rfl
  | succ k ih => simp [List.replicate_succ, countA, ih]

/-- The word `b^i a b^j` has exactly one `a`. -/
theorem countA_bab (i j : Nat) :
    countA (List.replicate i true ++ [false] ++ List.replicate j true) = 1 := by
  simp [countA_append, countA_replicate_true, countA]

/-- **The correction.** Every abelian-square factor of `b^i a b^j` consists
entirely of `b`s. So the abelian squares of such a word are the `b^{2p}`, and
there are `⌊max(i,j)/2⌋` of them — never a block of positions near the centre
only. -/
theorem isAbelianSquare_factor_of_bab_is_all_b {i j : Nat} {v : Word}
    (hfac : IsFactor v (List.replicate i true ++ [false] ++ List.replicate j true))
    (hsq : IsAbelianSquare v) : countA v = 0 := by
  have hle : countA v ≤ 1 := by
    have := countA_le_of_isFactor hfac
    rwa [countA_bab] at this
  rcases Nat.eq_zero_or_pos (countA v) with h0 | hpos
  · exact h0
  · exact absurd hsq (not_isAbelianSquare_of_countA_one (by omega))

end PVNP
