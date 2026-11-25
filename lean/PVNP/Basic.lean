/-
Root definitions for a formal treatment of P versus NP.

Design note
-----------
`PT` (polynomial time) is primitive. No Turing machine is constructed and no
runtime is measured anywhere in this development. A model of polynomial time is
therefore a *bundle of standard facts* about it, recorded as the fields of
`Model`, and every theorem in `PVNP/Results.lean` is conditional on those
fields.

That split is deliberate, and it mirrors the shape of the problem. The
modelling layer is routine but long: a multi-tape machine, a step counter, a
runtime measure, a proof that the measure is bounded by a polynomial. The layer
above it -- a lower bound against *every* polynomial-time machine -- is where
the three barrier theorems (relativisation, natural proofs, algebrisation)
apply. See `notes/`.

What is formalised here is the part that is not in doubt: the implication
structure of the problem, i.e. exactly which reduction-theoretic facts force
which conclusions.
-/

namespace PVNP

/-- Binary strings. -/
abbrev BinStr : Type := List Bool

/-- A language is a predicate on binary strings. -/
abbrev Language : Type := BinStr → Prop

/-- Two-argument Boolean procedures. Deciders and verifiers both live here; a
decider ignores its second argument. -/
abbrev Pred : Type := BinStr → BinStr → Bool

/-- String transducers, the carrier of many-one reductions. -/
abbrev Transducer : Type := BinStr → BinStr

/-- A model of polynomial time.

Every field is a fact a textbook uses without comment, and each is true of the
real notion. None of them is deep; all of them are routine against a concrete
machine model. Formalising them is the unglamorous half of the project. -/
structure Model where
  /-- `PT V` holds when the two-argument procedure `V` runs in polynomial time. -/
  PT : Pred → Prop
  /-- `PTMap f` holds when the transducer `f` runs in polynomial time. -/
  PTMap : Transducer → Prop
  /-- A polynomial-time procedure may ignore its second argument. -/
  pt_ignore : ∀ {V : Pred}, PT V → PT (fun s _ => V s [])
  /-- The identity transducer is polynomial time. -/
  ptMap_id : PTMap id
  /-- Polynomial-time transducers compose. -/
  ptMap_comp : ∀ {f g : Transducer}, PTMap f → PTMap g → PTMap (fun s => g (f s))
  /-- Substituting a polynomial-time transducer into the first argument of a
  polynomial-time procedure preserves polynomial time. -/
  pt_precomp : ∀ {f : Transducer} {V : Pred}, PTMap f → PT V → PT (fun s w => V (f s) w)
  /-- Polynomial time is closed under conjunction of tests. -/
  pt_and : ∀ {V W : Pred}, PT V → PT W → PT (fun s w => V s w && W s w)
  /-- Polynomial time is closed under disjunction of tests. -/
  pt_or : ∀ {V W : Pred}, PT V → PT W → PT (fun s w => V s w || W s w)
  /-- Polynomial time is closed under negation. -/
  pt_not : ∀ {V : Pred}, PT V → PT (fun s w => Bool.not (V s w))
  /-- Deciding a fixed polynomial bound on witness length is polynomial time. -/
  pt_lengthTest : ∀ k : Nat, PT (fun x w => decide (w.length ≤ (x.length + 2) ^ k))

namespace Model

/-- `L ∈ P`: some polynomial-time procedure decides `L`. -/
def MemP (M : Model) (L : Language) : Prop :=
  ∃ V : Pred, M.PT V ∧ ∀ s : BinStr, (V s [] = true ↔ L s)

/-- `L ∈ NP`: membership has a polynomial-time witness relation with
polynomially bounded witnesses. -/
def MemNP (M : Model) (L : Language) : Prop :=
  ∃ (V : Pred) (k : Nat), M.PT V ∧
    ∀ s : BinStr, L s ↔ ∃ w : BinStr, w.length ≤ (s.length + 2) ^ k ∧ V s w = true

/-- coNP: `L` is in coNP when its complement is in NP. -/
def CoNP (M : Model) (L : Language) : Prop := M.MemNP (fun s => ¬ L s)

/-- Polynomial-time many-one reducibility. The growth exponent is recorded
explicitly because the closure of NP under reduction needs it. -/
def Reduces (M : Model) (L L' : Language) : Prop :=
  ∃ (f : Transducer) (c : Nat), 1 ≤ c ∧ M.PTMap f ∧
    (∀ s : BinStr, (f s).length ≤ (s.length + 2) ^ c) ∧
    ∀ s : BinStr, L s ↔ L' (f s)

/-- `L` is NP-hard: every language in NP reduces to it. -/
def NPHard (M : Model) (L : Language) : Prop := ∀ L' : Language, M.MemNP L' → M.Reduces L' L

/-- `L` is NP-complete. -/
def IsNPComplete (M : Model) (L : Language) : Prop := M.MemNP L ∧ M.NPHard L

end Model

end PVNP
