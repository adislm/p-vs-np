/-
The length arithmetic behind closure of NP under polynomial-time reduction.

Everything here is about the normalised bound `(n + 2) ^ c`: adding 2 keeps the
base at least 2, which makes `(n + 2) ^ c ≥ 2` unconditional, which in turn
makes `x + 2 ≤ x * x` available. That is what lets two polynomial bounds
compose into one.
-/

namespace PVNP

theorem two_le_pow_add_two {n c : Nat} (hc : 1 ≤ c) : 2 ≤ (n + 2) ^ c := by
  have h : 1 < n + 2 := by omega
  calc
    2 ≤ n + 2 := by omega
    _ = (n + 2) ^ 1 := (Nat.pow_one (n + 2)).symm
    _ ≤ (n + 2) ^ c := Nat.pow_le_pow_of_le h hc

theorem add_two_le_mul_self {a : Nat} (h : 2 ≤ a) : a + 2 ≤ a * a := by
  calc
    a + 2 ≤ a + a := by omega
    _ = a * 2 := by omega
    _ ≤ a * a := Nat.mul_le_mul_left a h

/-- Adding 2 after a power is dominated by squaring the base. -/
theorem pow_add_two_add_two_le {n c : Nat} (hc : 1 ≤ c) :
    (n + 2) ^ c + 2 ≤ (n + 2) ^ (2 * c) := by
  have h2 : 2 ≤ (n + 2) ^ c := two_le_pow_add_two hc
  have hsq : (n + 2) ^ (2 * c) = (n + 2) ^ c * (n + 2) ^ c := by
    rw [show 2 * c = c + c by omega, Nat.pow_add]
  rw [hsq]
  exact add_two_le_mul_self h2

end PVNP
