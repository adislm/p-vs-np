# Cross-field transfer: the filter, and what six adjacent fields offered

Cross-field transfer is a real heuristic. Two of the most important
developments in this area came from outside it, and one of the barriers did too:

- **Geometric complexity theory** imported algebraic geometry, representation
  theory and plethysm from pure mathematics (Mulmuley–Sohoni 2001).
- **Lifting theorems** imported communication complexity into query and
  proof complexity (Raz–McKenzie 1999; Göös–Pitassi–Watson 2018).
- **Natural proofs** imported cryptographic pseudorandomness and turned it into
  a barrier (Razborov–Rudich 1997).

So looking sideways is not a fantasy. But the failure mode is equally consistent,
and it is worth naming before anything else: **an analogy that never becomes a
statement**. The transfer looks fertile, produces pages of prose, and yields no
mathematical object that can be checked or attacked.

## The filter

Every proposed transfer must answer five questions. A claim that cannot answer
the first three is labelled ANALOGY-ONLY and is not a candidate.

1. **Name the technique precisely.** Not the field, not the vibe — the actual
   lemma or method, stated well enough that a specialist recognises it.
2. **Name the target statement S, and fix the direction.** Either S implies a
   separation, or a separation implies S. Both are useful; they are not
   interchangeable, and confusing them is the single most common error in this
   genre. In particular, a statement *implied by* P ≠ NP is not a route to it.
3. **Which barrier does the argument face?** If the argument relativises it
   cannot separate the classes (Baker–Gill–Solovay). If it defines a property
   that is large and constructively testable it dies to natural proofs
   (Razborov–Rudich). If it survives substitution of an algebraic oracle it dies
   to algebrization (Aaronson–Wigderson). A transfer that has not been checked
   against all three has not been evaluated.
4. **Average case or worst case?** P vs NP is a worst-case statement. A technique
   that controls typical instances controls nothing about the worst case, and
   physics-flavoured work in particular is almost always about typical instances.
5. **Restricted model or full class?** A lower bound for bounded depth, bounded
   query, monotone, or algebraic models is a theorem about a restricted class.
   Restricted-model results have never reached P vs NP, and saying so plainly is
   part of the job.

## The six fields under survey

| Field | The specific question put to it |
| --- | --- |
| Statistical mechanics of random CSPs | does the replica/cavity picture, or the Overlap Gap Property, yield a worst-case statement rather than a typical-case one? |
| Communication complexity | Karchmer–Wigderson gives depth from communication. What exactly blocks the step to size? |
| Learning theory | the "learning algorithms imply circuit lower bounds" line. Which direction is proved in each result? |
| Descriptive complexity | characterisations of P and NP by logics. Is a characterisation ever a separation? |
| Topology | Lovász–Kneser, Borsuk–Ulam, discrete Morse. Has a topological invariant ever produced a complexity lower bound? |
| Quantum complexity | BQP, QMA, MIP\* = RE. What bridge would be needed to reach classical P vs NP, and does it exist? |

## Results

Filled in as the surveys report. The verdict vocabulary is
TRANSFERABLE / ANALOGY-ONLY / DEAD, and the expectation — stated in advance so
the outcome cannot be dressed up afterwards — is that most entries are
ANALOGY-ONLY. A field that produces nothing for complexity theory is a useful
finding, not a failed survey.
