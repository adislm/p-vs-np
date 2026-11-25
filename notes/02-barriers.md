# Why the obvious routes fail: three barrier theorems

Three results say that large classes of proof techniques provably cannot settle
P vs NP. They are the reason a session, a month, or a decade of clever
diagonalisation is not going to work.

## 1. Relativisation (Baker–Gill–Solovay, 1975)

An **oracle** is a language A; a machine M^A may query A at unit cost. P^A and
NP^A are defined as usual with oracle access.

**Theorem.** There exist A and B with

    P^A = NP^A        and        P^B ≠ NP^B.

For A take any PSPACE-complete language: P^A = NP^A = PSPACE. For B, a
diagonalisation constructs a language outside NP^B that sits inside P^B.

**Consequence.** Call a proof technique *relativising* if it stays valid when
every machine is given the same oracle. Since the technique would then prove
P^A = NP^A and P^B ≠ NP^B, and these contradict each other, no relativising
technique can prove either direction of P vs NP.

Almost everything elementary relativises: simulation, padding, hierarchy
theorems, the Cook–Levin proof itself. This is the cheapest barrier to state
and the most frequently violated by amateur attempts.

The standard escape used in practice is to prove a theorem that mentions a
*specific* property of computation, not just its oracle behaviour — which is
what circuit lower bounds and proof complexity do.

## 2. Natural proofs (Razborov–Rudich, 1997)

Let F_n be the set of Boolean functions on n bits, and SIZE_n(s) those
computable by circuits of size s.

A sequence of properties Γ = (Γ_n) with Γ_n ⊆ F_n is **natural** if

- **largeness**: |Γ_n| ≥ 2^{-O(n)} · |F_n|;
- **constructivity**: membership in Γ_n is decidable in time 2^{O(n)} given the
  2^n-bit truth table.

It is **useful against size s** if Γ_n ∩ SIZE_n(s) = ∅ for all large n.

**Theorem.** If a natural property useful against P/poly exists, then no
strong pseudorandom function family exists.

**Consequence.** The combinatorial method — exhibit a property shared by almost
all functions, decidable from the truth table, and absent from the circuit
class — cannot prove NP ⊄ P/poly unless it also breaks the pseudorandom
functions that modern cryptography assumes exist. So a successful natural
proof is either a breakthrough in complexity *or* a break of cryptography; it
cannot be both, because natural proofs are constructive enough to build the
distinguisher.

Note the asymmetry. This barrier bites on lower-bound proofs that go through
*typical* functions. Razborov's monotone circuit lower bound for CLIQUE and the
AC⁰ lower bound for PARITY are not natural in this sense (the PARITY proof is
about a specific function; the monotone proof uses an approximation method that
does not transfer).

## 3. Algebrisation (Aaronson–Wigderson, 2008)

Relativisation allows arbitrary oracles but forbids the proof from using
*arithmetic structure*. Algebrisation extends the model: an **algebraic oracle**
A~ answers queries to a low-degree extension of A over a finite field, which is
what algebraic techniques (polynomial method, interactive proofs, PCP) actually
use.

**Theorem.** There are algebraic oracles A~ and B~ with

    P^A~ = NP^A~        and        P^B~ ≠ NP^B~.

**Consequence.** Any technique that survives the substitution of an algebraic
oracle for a Boolean one — any technique that *algebrises* — cannot settle the
question either. This obstructs the polynomial method, the PCP line of attack,
and most interactive-proof machinery.

Three barriers is not bad luck. Each was constructed by taking the previous
escape hatch and showing that the escape hatch has the same weakness one level
up.

## What is left

Techniques known to evade all three:

- **Circuit lower bounds proved by structural, non-natural means.** The
  monotone circuit method and the approximation method are the models, but
  neither extends past monotone.
- **Geometric complexity theory** (Mulmuley–Sohoni, 2001–). Reformulates
  permanent vs determinant as an orbit-closure problem and attacks it with
  representation theory and algebraic geometry of the general linear group.
  It does not relativise because the objects are not languages with oracles.
  Its programme is decades long and unproven.
- **Proof complexity.** Show that no propositional proof system of a given
  strength proves a statement, which by the correspondence between proof
  systems and algorithms would give a lower bound. Strong barriers here are
  themselves open.
- **Williams' method** (2011). Prove a circuit lower bound for a *nondeterministic*
  class (NEXP ⊄ ACC⁰) by combining a satisfiability algorithm with a
  contradiction from an assumed fast circuit. The hope is to push the class
  upward; the ACC⁰ barrier was broken this way and nothing above it has been.

## A structural remark

"P ≠ NP" is a Π₂ sentence of arithmetic:

    ∀ M ∀ c ∃ x,  M does not decide SAT within |x|^c + c steps.

"P = NP" is Σ₂, witnessed by the existence of a deciding machine.

Both are Σ¹₂. **Shoenfield absoluteness** says Σ¹₂ statements are absolute
between a model of ZFC and its forcing extensions. Therefore **forcing cannot
prove independence of P vs NP**, in either direction, and cannot settle it
either. This rules out the largest tool set used for CH-type independence.
Other routes to independence (arithmetic, large-cardinal) are not ruled out by
this argument, but neither is there any result along them.
