# Falsification Checklist for Claimed P vs NP Proofs

**Verdicts.** DEAD = refuted by the cited theorem. HEURISTIC = gap flagged, not conclusive. PASS = survives this test only. One DEAD suffices.

## Barrier tests

**A1. Relativization — DEAD.** *Test:* rewrite every machine as oracle-access; if all steps stay valid for an arbitrary oracle O, the argument *relativizes*. *Why valid:* Baker–Gill–Solovay (1975) give oracles A, B with P^A = NP^A and P^B ≠ NP^B. A relativizing proof forces one answer for every oracle, contradicting one of them. *Failure:* pure simulation or diagonalization that never uses a non-relativizable resource; an explicit claim of "model-independence." Ambiguous: HEURISTIC.

**A2. Natural proofs — DEAD (conditional on one-way functions).** *Test:* does the proof define a property Φ of Boolean functions, testable from the 2^n-bit truth table in 2^{O(n)} time (*constructive*), true for a ≥ 2^{-O(n)} fraction of random functions (*large*), and implying superpolynomial circuit size (*useful*)? That is a *natural proof*. *Why valid:* Razborov–Rudich (1997): such Φ would distinguish computable pseudorandom functions from random ones in 2^{O(n)} time, breaking PRFGs. One-way functions yield PRFGs (HILL 1999), so under the standard OWF assumption no natural proof of NP ⊄ P/poly exists. *Failure:* "f is hard if [truth-table statistic] is large; random f has it with probability 1/poly; hence f ∉ P/poly." The barrier is conditional; borderline: HEURISTIC.

**A3. Algebrization — DEAD.** *Test:* allow machines to query the low-degree (multilinear) extension Ã of an arbitrary oracle A; does every step remain valid? *Why valid:* Aaronson–Wigderson (2008) exhibit algebraic-oracle worlds in which P = NP and worlds in which P ≠ NP. An argument valid under algebraic-oracle access ("algebrizing") would force both, so it cannot settle the question. It extends relativization: arithmetization that evades A1 is typically caught here. *Failure:* algebraic or arithmetic steps that never use power unavailable to algebraic-oracle machines.

## Logical and definitional tests

**B1. Uniformity confusion — DEAD.** *Test:* is the object a uniform machine (P) or a circuit family (P/poly)? *Why valid:* P vs NP concerns uniform time. P ⊆ P/poly; P/poly contains undecidable languages and may hardwire answers per length. A P/poly bound implies P ≠ NP, but a bound against size n^c for fixed c does not even contradict NP ⊆ P/poly. And NP ⊆ P/poly gives PH = Σ₂ᵖ (Karp–Lipton 1980), so NP ⊄ P/poly is stronger than P ≠ NP. *Failure:* "SAT needs > n² gates, so SAT ∉ P"; equating polynomial time with polynomial-size circuits; claiming P/poly ⊆ P.

**B2. The one-machine fallacy — DEAD.** *Test:* does the proof analyze one algorithm (or one schematic family) and conclude about the *problem*? *Why valid:* L ∉ P requires that *no* deterministic poly-time machine decides L. An exponential upper bound on one algorithm, or the failure of known algorithms, bounds nothing below. *Failure:* "the best known algorithm is 2^n; all known algorithms are exponential; hence SAT ∉ P."

**B3. Definition drift — DEAD.** *Test:* re-derive P, NP, and "polynomial" from the proof's text. Standard: P = ⋃_k DTIME(n^k); NP = ⋃_k NTIME(n^k) (poly-time verifiable witnesses); n is input *bit-length*; polynomial = O(n^k) for a fixed k. *Why valid:* these are the conjecture's definitions (Cook 1971; Levin 1973); another class is another theorem. *Failure:* time measured in numeric value, not bit-length (pseudo-polynomial); unary encoding; input-dependent exponent; n^{log n} or 2^{√n} called "polynomial"; NP redefined as "not polynomial."

**B4. "Not polynomial, therefore exponential" — DEAD.** *Test:* does the proof infer non-membership in P from a super-polynomial upper bound, or treat {polynomial, exponential} as exhaustive? *Why valid:* the complement of P contains n^{log n}, 2^{√n}, quasi-polynomial, sub-exponential rates. Showing L ∉ P needs ∀k, L ∉ DTIME(n^k) — a lower bound beating *every* polynomial, not an exponential algorithm. The time hierarchy theorem (Hartmanis–Stearns 1965) gives P ⊊ EXP unconditionally but does not reach NP, which may lie strictly between. *Failure:* "our algorithm takes 2^n, which is not polynomial, so the problem is not in P."

**B5. Quantifier scope — DEAD.** *Test:* expand the claim: P ≠ NP is ∃L∈NP such that ∀M ∀k, L ∉ DTIME_M(n^k). Check each ∀: every deterministic machine (not one, not a natural subclass), every constant k (not a fixed exponent), with correct asymptotics (O(n^k); constants absorbed). *Why valid:* this is the literal negation of "∃M ∃k deciding L in O(n^k)." Dropping a ∀ proves a weaker statement. *Failure:* "no machine of schema S solves SAT in n³ time, therefore SAT ∉ P."

**B6. Counting is not a lower bound — DEAD.** *Test:* is hardness inferred from the size of a search space (2^n assignments, 2^{n²} circuits)? *Why valid:* that bounds only brute-force enumeration; a machine may exploit structure. *Failure:* "there are 2^n assignments, so any algorithm must examine exponentially many."

**B7. Self-contradiction and overreach — DEAD.** *Test:* (a) instantiate the central lemma on a known-easy language (2SAT, REACHABILITY, PRIMALITY since AKS 2002); if declared hard, the lemma is false. (b) Run the argument under an oracle O with P^O = NP^O; if it still "separates," it is broken. (c) Check it does not contradict Karp–Lipton or the hierarchy theorem. (d) Check circularity (a hard function posited to build the PRFG used to prove hardness). *Failure:* a criterion satisfied by random or easy functions; a lemma that assumes its conclusion.

## Positive requirements

A genuine P ≠ NP proof must produce:

1. **Target and membership:** an explicit L ∈ NP (e.g., SAT), with proof L ∈ NP.
2. **Machine-independent lower bound:** "every deterministic machine deciding L runs in time ≥ f(n)" with f(n) = ω(n^k) for every k, proved.
3. **An explicit invariant:** a property of languages/functions, defined independently of the proof, that L has and every target-class language lacks.
4. **Named barrier evasion:** the invariant must be non-constructive or non-large (else A2), non-relativizing (A1), and non-algebrizing (A3); the proof must say which and how.
5. **A class containing NP:** bounds against AC⁰, monotone circuits, or fixed-depth classes do not touch P vs NP; a bound against P/poly (⊇ P) does.
6. **Complete lemmas:** each load-bearing step a proved theorem with constants and asymptotics; no "clearly," "it is known," or unproved conjecture.
7. **Model robustness:** model stated (TM/RAM/circuit); conclusion invariant across polynomial-time-equivalent models.

Any missing item is the exact place to attack.

## Worked example

**Claimed proof.** "SAT requires trying all 2^n assignments, since a machine cannot know which one satisfies the formula without checking. No known algorithm beats 2^n. Since 2^n is not a polynomial, SAT ∉ P, hence P ≠ NP. The argument is model-independent and holds for any oracle, since it only counts assignments."

**Application.**
- **B6:** "2^n assignments" bounds enumeration, not computation; structure may be exploited. GAP.
- **B2:** only brute force is analyzed; nothing is said about all machines. DEAD.
- **B4:** non-membership in P is inferred from an exponential upper bound. DEAD.
- **B5:** no ∀ over machines or k; "no known algorithm" is not "no algorithm." DEAD.
- **A1:** the proof claims oracle-independence; BGS supplies an oracle A with P^A = NP^A, under which the argument "proves" a falsehood. DEAD.

Five independent fatal errors, none needing deep mathematics. A repair must satisfy the positive requirements — notably a non-natural, non-relativizing invariant (4) and a bound over all machines (2).
