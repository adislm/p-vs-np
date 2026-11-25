# Counterexample hunting: a record of what survived and what did not

A conjecture that can be tested by finite search is a conjecture that can be
killed. Killing one is a result; failing to kill one over a stated range is also
a result, and both are worth recording precisely.

**Method.** For each target: state the conjecture exactly with its source, write a
small program, verify the program reproduces known terms before testing anything,
search exhaustively over a named range, and report either a printed witness or a
null result with the range. A program that emits a false counterexample is worse
than no program, so every claimed witness is re-run by hand before it is recorded
here.

## 1. OEIS conjectures

Four conjectures attached to OEIS entries, all still standing over the ranges
searched. This section is a record of survival, which is the honest outcome for
conjectures that have already survived some attention.

### A000172 — Franel numbers

`a(n) = Σ_k C(n,k)³`, with the recurrence
`(n+1)² a(n+1) = (7n²+7n+2) a(n) + 8n² a(n−1)`.

**Conjecture** (Detlefs, 2013): a(n) ≡ 2 (mod n³) **iff** n is prime. The forward
direction, prime ⇒ congruence, is proved (Z.-W. Sun). The converse is open.

**Result: survives.** Searched n = 2..200000. Every prime satisfies the
congruence, and no composite does — including the base-2 Fermat pseudoprimes
1093 and 3511 and the base-2 Wieferich prime 16843, which is the sort of n most
likely to break it.

**Independently reproduced** at n ≤ 30000 during the audit of this record, with a
separately written program: zero anomalies.

### A219197

**Conjecture** (Hanna): a(n) is never congruent to 3 mod 4.

**Result: survives** for n = 0..50000, using Kotesovec's exact three-term
recurrence, with the computed terms matched against OEIS before testing.

### A237656 — a prime-counting residue system

`a(n)` is the least m such that {π(k²) : k = 1..m} is a complete residue system
mod n.

**Conjecture** (Z.-W. Sun): a(n) is always positive, and a(n) < 2·p(n+1) − 2 for
n > 0, where p is the nth prime.

**Result: survives** for n = 1..150, with the search cap m ≤ 2000 exceeding every
bound tested. `a(5) = 8 < 24` checked by hand: the residues π(k²) mod 5 for
k = 1..8 are 0, 2, 4, 1, 4, 1, 0, 3, which covers all five classes.

### A307532 — primality of a minimal exponent

**Conjecture**: a(n) is prime for all n ≥ 0, where a(n) is the least
k > 2^(2ⁿ) + 1 with k ≡ 1 (mod 2ⁿ) and 2^(k−1) ≡ 1 (mod (2^(2ⁿ) − 1)·k).

**Result: survives** to n = 12, four terms beyond those listed in OEIS, with
primality by BPSW. The minimal m values found (202, 56, 304, 635) independently
match the m-list in the OEIS remark, which is a useful cross-check that the search
is finding the intended objects and not merely some strong pseudoprime.

**Limit worth stating.** n ≤ 12 is a narrow range, and a primality conjecture
that holds to n = 12 is weak evidence. This one is recorded for completeness, not
as a meaningful test.

## What this section is not

None of these is evidence for the conjectures in any mathematical sense. A
congruence holding to 2·10⁵ is consistent with a counterexample at 2·10⁵ + 1, and
several famous conjectures have died far beyond their first computational check.
The value of the record is the opposite direction: it tells you where a
counterexample, if one exists, does *not* live, and it fixes the exact programs
and ranges so the claim can be re-run rather than trusted.
