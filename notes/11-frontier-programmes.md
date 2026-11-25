# Frontier programmes: what each one can and cannot deliver

Three lines of work that are active, serious, and often described in terms that
promise more than they deliver. Each section ends with a verdict on whether the
programme is a route to P vs NP or something orthogonal to it.

## 1. Bounded arithmetic and the metamathematics of circuit lower bounds

**Verdict: ORTHOGONAL.** This is metamathematics — which weak theories can
formalise which lower-bound arguments. It neither proves nor refutes P ≠ NP, and
unprovability in a weak theory says nothing about truth.

### What is actually proved

**Failures to prove even upper bounds.** PV₁ does not prove P ⊆ SIZE[n^k] for any
k; S¹₂ does not prove NP ⊆ i.o.SIZE[n^k]; T¹₂ does not prove
P^NP ⊆ i.o.SIZE[n^k]. These are not lower bounds — they are failures to
establish *upper* bounds, and the reason is witnessing: a proof of a circuit upper
bound would yield explicit efficient circuits, which is itself a breakthrough.

**Unconditional unprovability of strong average-case separations.** APC₁, and
each Tⁱ_PV, cannot prove Πᵢ-SIZE[poly] versus Σᵢ-SIZE[2^{n^Ω(1)}] separations; in
particular APC₁ cannot prove the Π₃/Σ₃ separation (Li–Oliveira, STOC 2023).

**A conditional separation of theories.** PV₁ ⊊ APC₁ follows from subexponentially
secure indistinguishability obfuscation together with coNP ⊄ AM
(Ilango–Li–Williams, STOC 2023).

**Conditional collapse statements.** PV₁ ⊢ P = NP iff PV₁ ⊢ NP = coNP, and if PV
proved NP ⊆ P/poly then PV proves PH collapses to the Boolean hierarchy, with
analogous Karp–Lipton collapses for S¹₂ and S²₂ (Cook–Krajíček 2007).

**Open.** Whether PV₁ is consistent with P ≠ NP — equivalently PV₁ ⊬ P = NP —
which would follow from superpolynomial Extended Frege lower bounds.

### Razborov's theorem, stated so it cannot be misread

Razborov (1995) proved, by interpolation for "split" bounded theories: assuming
strong pseudorandom generators exist, S²₂(α) cannot refute the statement that α
encodes a circuit of size n^{log* n} for SATISFIABILITY. For S¹₂(α) the same holds
under generators secure against small-depth circuits; for a theory strong enough
to prove exponential lower bounds for constant-depth circuits, the result is
unconditional.

"Cannot refute" means the theory does not prove the lower bound, and is therefore
*consistent with* SAT having small circuits. It is not a claim that P ≠ NP is
unprovable, and the difference is not pedantic — it is the difference between a
statement about circuits and a statement about what mathematics can know.

### No independence result exists

There is no unconditional independence of P vs NP from ZFC, PA, or any bounded
theory. Every unprovability theorem above is about a circuit-bound statement in a
weak theory, or is conditional on cryptographic or complexity assumptions. And
independence from S¹₂ would not bear on truth: S¹₂ is weak enough that true
statements routinely escape it. Even independence from ZFC would not settle
truth.

### What does transfer

One thing, and it is negative guidance rather than mathematics: these results say
a feasible proof of P ≠ NP cannot be too constructive in the ways they exclude. A
proof that produced explicit circuits from a hypothetical collapse would be
witnessable and hence formalisable in a weak theory, so any successful argument
must avoid that shape. That tells you what a proof cannot be. It does not tell
you what it is, and it is methodology rather than progress on the problem.

Razborov's positive companion results — parity/AC⁰ and clique/monotone bounds
provable in PV at doubly-logarithmic parameters — confirm that the known
techniques are formalisable. Validation, not progress.

### Frontier, 2024–2026

Li–Oliveira is the high-water mark: unconditional unprovability in APC₁ and the
Tⁱ_PV. Ilango–Li–Williams separated PV₁ from APC₁; Ren–Wang–Zhong (ECCC TR25-191)
re-derive that separation from "demi-bits" generators. Pich–Santhanam (ECCC
TR23-199) connect Extended Frege lower bounds to P ≠ NP via self-provability of
upper bounds. Oliveira's SIGACT News survey (2025) frames the area. The live open
problems are S¹₂ ⊬ P ⊆ SIZE[n^k], T¹₂ ⊬ NP ⊆ SIZE[n^k], consistency of PV₁ with
P ≠ NP, and strictness of Buss's hierarchy.

## 2. Meta-complexity

**Verdict: EQUIVALENT as a route.** Real theorems, real equivalences, no bypass.
Every proven bridge is an equivalence with a circuit, average-case or
cryptographic hardness assumption, and the headline NP-hardness result of 2025 is
itself *derived from* circuit lower bounds.

### MCSP

Input: the truth table of f : {0,1}ⁿ → {0,1} (length N = 2ⁿ) together with s; does
f have a circuit of size at most s? It is in NP — guess the circuit and verify.

NP-hardness is known only in restricted or relaxed forms: DNF-MCSP (Masek 1979),
OR-AND-MOD under deterministic many-one reductions (Hirahara–Oliveira–Santhanam
2018), partial MCSP\* under randomized polynomial-time reductions with GapMCSP\*
NP-complete (Hirahara 2022), and full MCSP at constant factor only under
deterministic quasi-polynomial nonadaptive reductions from cryptographic *plus
circuit-lower-bound* assumptions (Hirahara–Ilango 2025). There is no unconditional
polynomial-time NP-hardness for full MCSP.

Conversely MCSP has non-trivial algorithms — non-uniform SIZE(2^{0.8N+o(N)})
(Hirahara–Ilango–Williams; Mazor–Pass, 2024), which refutes perebor
non-uniformly — and restricted-model lower bounds (N^{2−o(1)} formula size, 2017;
N^{3−o(1)}, 2019).

### The equivalences, with direction

| Statement | Direction |
| --- | --- |
| DistPH ⊆ AvgP | ⟺ GapMINKT^PH ∈ P (Hirahara 2020) |
| KT is hard on average | ⟺ NC⁰ one-way functions exist (Ren–Santhanam 2021) |
| Kt is hard on average | ⟺ one-way functions exist (Ren–Santhanam 2021) |
| GapMCSP at factor 2^{(1−ε)n} ∈ BPP | ⟺ its average-case version is easy (Hirahara 2018) |
| MCSP ∈ P | ⇒ a natural property against P/poly exists (Kabanets–Cai 2000) |

These are biconditionals in the strong cases. That is what EQUIVALENT means here:
meta-complexity does not reduce the difficulty, it relocates it into a different
vocabulary.

### The one genuine intermediate, and why it still does not help

`MCSP ∉ P` is concrete, and it implies P ≠ NP because MCSP ∈ NP. It is *not*
known to be equivalent: P ≠ NP does not imply MCSP ∉ P. So it is a legitimate
strengthening of exactly the kind `notes/08` says is the only possible kind.

But it is already implied by the existence of one-way functions. Kabanets–Cai
gives MCSP ∈ P ⇒ a natural property against P/poly; Razborov–Rudich turns a
natural property useful against P/poly into a break of pseudorandom functions.
Contrapositive: one-way functions ⇒ no such property ⇒ MCSP ∉ P ⇒ P ≠ NP.

So the chain cryptography ⇒ P ≠ NP is real and clean — and it is the *same*
conclusion as the direct argument in `notes/05`: if P = NP then FNP ⊆ FP by
search-to-decision, so no function is one-way. Meta-complexity gives a second
route to a fact already known, not a new lever.

### Barrier status

Relativisation is evaded by construction: the key reductions are non-black-box,
hence non-relativising. But MCSP-specific oracle-independence results block the
black-box routes and force cryptographic assumptions in their place.

Natural proofs is not evaded — the programme is entangled with it. `MCSP ∈ P`
would *be* a natural property, which is exactly why one-way functions imply
`MCSP ∉ P`. The programme assumes cryptographic hardness rather than defeating
the barrier.

And the hardness of proving hardness bites: Razborov's unprovability results and
the Krajíček–Razborov Extended Frege conjecture say the needed lower bounds are
themselves hard or unprovable in the relevant theories.

### 2024–2026

Hirahara–Ilango (FOCS 2025) is the strongest result: constant-factor MCSP is
NP-hard under deterministic quasi-polynomial-time nonadaptive reductions. Read the
hypotheses — they include coNP ∉ ioNSIZE(2^{n^ε}) and P^NP/poly requiring
Ω(2ⁿ/n) circuits. **The circuit lower bounds are assumptions of the theorem, not
conclusions.** Ilango's random-oracle reductions from hypergraph vertex cover to
MCSP (SICOMP 2026) and Huang–Ilango–Ren's approximation hardness for MOCSP
(SICOMP 2025) sit in the same frame. The notable counter-current is the 2024
upper bound, which shows MCSP is easier than brute force.

## 3. The algorithmic method

**Verdict: DEAD for P vs NP, ANALOGY-ONLY for TC⁰ and NC¹.** This is the only
technique that has produced a genuine non-relativising, non-naturalising lower
bound, and it is worth understanding exactly why it cannot reach the problem.

### The engine

Williams: if C-SAT on n-input, n^k-size circuits runs in O(2ⁿ/n^c) for every k,
then NEXP ⊄ C.

Assume NEXP ⊆ C, hence NEXP ⊆ P/poly. The **easy witness lemma**
(Impagliazzo–Kabanets–Wigderson 2002) then says every NEXP verifier's
yes-instances have witnesses that are truth tables of polynomial-size circuits.
Take Succinct-3SAT: an instance D on n inputs whose truth table is a 2ⁿ-bit 3CNF.
If satisfiable, some small W satisfies it. Guess W; then "tt(W) satisfies tt(D)"
is a C-circuit of polynomial size on n inputs. The fast solver decides it in
2ⁿ/n^ω(1), contradicting the nondeterministic time hierarchy, which places some
L ∈ NTIME(2ⁿ) outside NTIME(2ⁿ/n^ω(1)).

Three things make NEXP essential: witnesses are exponentially long, so
compressing them is substantive; NEXP ⊆ C supplies the easy witness lemma's
hypothesis; and the contradiction is placed at the 2ⁿ hierarchy scale.

### Why ACC⁰ worked and nothing above it does

| Class | Status | Obstruction |
| --- | --- | --- |
| ACC⁰ | **NEXP ⊄ ACC⁰** (Williams 2011) | low-degree polynomial representations over finite rings, made algorithmic |
| TC⁰ | open | MAJORITY has approximate polynomial degree Ω(n), so nothing compresses and the engine dies |
| NC¹ | believed unreachable | 2ⁿ/n^ω(1) formula-SAT would refute SETH, so the missing algorithm is believed *false*, not merely missing |
| P/poly | open | CircuitSAT in 2ⁿ/n^ω(1) is unknown |

ACC⁰ was tractable because Razborov–Smolensky and Beigel–Tarui give it low-degree
representations over finite rings — MOD₂ is parity, so ACC⁰ contains AC⁰[⊕] — and
William's contribution was to *algorithmise* that representation via multipoint
evaluation, getting a 2^(n^δ) divisor that beats any polynomial. TC⁰ has no such
representation; MAJORITY's approximate degree is linear.

### The decisive point

**The method's hypothesis is implied by P = NP.** If P = NP then CircuitSAT is in
polynomial time, hence certainly in 2ⁿ/n^ω(1), and the theorem applies — yielding
NEXP ⊄ P/poly, which is true unconditionally anyway. So the method is consistent
with both worlds and cannot be the thing that distinguishes them. It is
*downstream* of P = NP rather than a route to it.

Put concretely: even a full 2ⁿ/n^ω(1) CircuitSAT algorithm yields only
NEXP ⊄ P/poly — one exponential above NP. Getting NP ⊄ P/poly from this template
would require CircuitSAT ∈ P, which is P = NP itself.

### What actually bounds the method

- **Scale.** Murray–Williams (2018) extended the easy witness lemma to NP and NQP,
  giving NQP ⊄ ACC⁰∘THR at quasipolynomial scale. It stops at NQP: NP witnesses
  are only polynomially long, the easy-witness circuit has O(log n) inputs, brute
  force is polynomial, and there is no hierarchy there to contradict.
- **Relativisation.** Vyas–Williams (2023) give an oracle where CAPP ∈ P but
  EXP^NP has polynomial-size circuits; Chen–Hu–Ren (ITCS 2026) derive new
  algebrisation barriers from Missing-String communication.
- **Locality.** Chen–Hirahara–Oliveira–Pich–Rajgopal–Santhanam (2022) show local
  arguments also hold for small-fan-in oracle circuits, so they cannot certify
  strong general bounds. Pich (2024) localises the approximation method.
- **The frontier moved elsewhere.** Recent progress came from range avoidance and
  iterative win–win rather than the SAT-algorithm method: S₂E/1 ⊄ SIZE[2ⁿ/n]
  (Chen–Hirahara–Ren; Li, STOC 2024), AMEXP ∩ coAMEXP (Chen–Li–Liang 2025),
  E^{prMA}/1 (Ren–Williams 2026). None of these is the engine above, and none
  reaches NEXP.

### What this programme did deliver

NEXP ⊄ ACC⁰, and size strengthenings of it. That is a real result, it was the
first lower bound against a class containing AC⁰[⊕], and it remains the only
proof that the barriers can be beaten at all — for a class far above NP and far
below P/poly. It is the existence proof for the method, not a step toward the
theorem.
