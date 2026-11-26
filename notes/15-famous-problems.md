# 15 — Landmark problems instead of recent preprints

Notes 07 and 13–14 audit 2025–2026 preprints. That work found real defects, but the
user's objection is correct: a day-old preprint has not been checked by anyone, so
finding a mistake in it says little. The present note changes target.

## Why the two categories are not comparable

A **recent preprint** is in the regime where defects are *likely*. Nobody has read
it closely. A careful audit finds something with probability maybe 1/3, and the
findings are frequently typos, off-by-ones, or a hypothesis silently dropped. But
the value of the finding is bounded by the value of the paper — usually low, since
most 2026 preprints will be read by tens of people.

A **landmark conjecture** is in the opposite regime. It has been attacked for
decades by specialists, and much of the low-hanging computational evidence has been
collected already. Defects are rare because everyone who could find one has tried.
The expected yield of an audit is close to zero — but a genuine finding is a real
result.

The two regimes also differ in method:

| | recent preprint | landmark conjecture |
|---|---|---|
| typical finding | local error in a proof | nothing |
| method | read closely, re-derive | exhaustive search / construction |
| cost of a false claim | moderate | severe — the literature is watching |
| chance of a positive result | ~1/3 | ~1/50 |

So the honest framing of what follows is: **a null result is the expected outcome,
and a null result is not a failure.** The point of sweeping landmark problems is
that the tails are fat — the one-in-fifty case is worth the other forty-nine.

## The selection criterion

A conjecture qualifies for computational attack only if all three hold:

1. **It is famous.** Named after people, with a literature, not a single preprint.
2. **It is open.** Not "recently resolved and the news hasn't propagated" — verified
   against the current literature, not memory.
3. **It is finite-checkable.** Either the conjecture quantifies over finite objects
   that can be enumerated (`Erdős–Gyárfás`, `Caccetta–Häggkvist`), or it asks for a
   specific number that a search can pin down (`van der Waerden`, `Schur`), or it
   asks for existence of a single object that a construction can exhibit
   (`Hadamard`, `Rota`).

Condition 3 is what separates a computable conjecture from a merely famous one. The
Riemann hypothesis is famous and open and fails condition 3; nothing in this repo
will touch it.

## The target list

Grouped by what a search can actually produce.

### A. Exact numbers with open values

- **Ramsey numbers.** `43 ≤ R(5,5) ≤ 48`, open in this window since 1989/1995. A lower
  bound is a graph certificate; the upper bound is out of reach.
- **Schur numbers.** `S(5) = 160` known; `S(6)` open. Lower bound = a colouring,
  upper bound = exhaustive search.
- **van der Waerden numbers.** `W(2,6) = 1132`, `W(3,5) ∈ [1008, 1127]`. Small open
  values are SAT-attackable.
- **Rado numbers** for simple equations — same structure as Schur.

These are the most promising category. The objects are small, the certificates are
short and checkable, and the problems have a history of being pushed by exactly this
method (Heule's SAT proof of `S(5)=160` is the model).

### B. Structural conjectures over finite objects

- **Erdős–Gyárfás (1995).** Every graph with minimum degree ≥ 3 has a cycle of length
  a power of 2. Enumerable by `geng -d3`. A counterexample would be major.
- **Caccetta–Häggkvist (1978).** Digraph of minimum outdegree `r` has a directed cycle
  of length ≤ `⌈n/r⌉`. Enumerable with reductions only.

Both are "for all finite objects" statements, so exhaustive search gives a theorem
for the orders covered and silence beyond. That silence must be stated, not hidden.

### C. Existence statements

- **Hadamard conjecture.** Smallest undecided order is **2396 = 4·599**, not 668. The
  twelve open multiples of 4 below 2000 were resolved in August 2026 (Alpöge, Voinov,
  Reynolds-Haertle and an Anthropic model), and I verified the published 668 matrix
  myself. See note 16. A construction at 2396 would be real; but the standard
  constructions plus order multiplication provably cannot reach it, so only a direct
  sequence search can.
- **Rota's basis conjecture (1989).** Small `n` checkable by exhausting column
  assignments. A counterexample at small `n` would be extraordinary and therefore
  must be checked twice for bugs before being believed.

### D. Number-theoretic statements with huge verified ranges

- **Erdős–Straus.** `4/n = 1/a + 1/b + 1/c`, verified to ~`10^17`. Anything this repo
  computes is far below the record; the only honest output is "re-verified a small
  range", which is not news.

Listed for completeness. No result is expected here.

## The discipline

Identical to note 06, and it binds harder here:

- **Reproduce before extending.** Re-derive a published small value first. If the
  reproduction fails, the bug is ours — the published value has been checked by more
  people than we have.
- **A certificate or nothing.** A lower bound is a printed object plus a verifier.
  An upper bound is an exhaustion whose scope is stated exactly.
- **No bound without an object.** "The search timed out" is not a lower bound.
- **State the range.** "Verified for `n ≤ 12`" is a claim about `n ≤ 12` and nothing
  else.
- **Cross-check any counterexample twice.** Two independent implementations. A false
  counterexample to a famous conjecture is the worst possible output of this project,
  worse than no output.

## What is being attempted

Not a solution. The realistic outcomes, in descending order of probability:

1. Null results confirming known bounds — expected, and worth recording as such.
2. An independent reproduction of a published value, with our own code — modest
   value, catches our own bugs.
3. A marginal improvement to a lower bound — a real, publishable-in-a-note result.
4. A counterexample to a landmark conjecture — would be a major result, and the
   probability is very small.

Anything in category 4 gets held for days and checked by independent code before it
leaves this repo.
