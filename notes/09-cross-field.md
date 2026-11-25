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

The expectation was stated in advance: most entries are ANALOGY-ONLY, and a field
that produces nothing for complexity theory is a useful finding rather than a
failed survey.

### Quantum complexity — DEAD, ANALOGY-ONLY, DEAD

| Mechanism | What it proves | Verdict |
| --- | --- | --- |
| Recursive compression and quantum low-degree self-testing (Fitzsimons–Ji–Vidick–Yuen 2019; Natarajan–Wright 2019; Ji–Natarajan–Vidick–Wright–Yuen, *MIP\* = RE*) | MIP\* = RE, hence NEEXP ⊆ MIP\*, the Halting problem reduces to approximating the entangled value, and Connes' embedding conjecture is false | **DEAD** |
| Quantum natural proofs (Arunachalam–Grilo–Gur–Oliveira–Sundaram 2020; a 2026 preprint extending the barrier to quantum state preparation) | a quantum PAC learner with parameters γ²T ≪ 2ⁿ/n for class C implies BQE ⊄ C | **ANALOGY-ONLY** |
| Algebrization (Aaronson–Wigderson 2008) | any proof that survives algebraic-oracle access cannot resolve P vs NP | **DEAD** as a route — and the sharpest formal reason the transfer fails |

**Why MIP\* = RE does not transfer.** It is a theorem about *computability*, not
time. The provers are unbounded and the entanglement is unlimited, so MIP\*
contains undecidable languages and cannot equal or sit inside NP. Its genuine
classical corollary — the refutation of Connes' embedding conjecture — is
operator-algebraic, not computational. The polynomial-time version of the
question is not what was proved.

**Why the quantum lower-bound machinery does not transfer.** The learning-to-
lower-bounds implication lands on BQE, a class whose relation to NP would need
NP ⊆ BQE, i.e. a 2^{O(n)} algorithm for SAT, which ETH denies and which is
certainly not a theorem. The 2026 barrier result constrains proofs about quantum
*states*, a different proof space from Boolean circuit lower bounds; it neither
implies nor refutes anything about NP. Note the 2026 item is a preprint and is
recorded as unverified.

**Why algebrization is the honest answer here.** It is not a bridge but the
barrier that forecloses the bridge. Quantum self-testing extends the same
algebraic toolkit as arithmetisation, and algebrization is precisely the
statement that this toolkit cannot separate the classical classes. The transfer
dies at the mechanism, before the resource mismatch is even reached.

**Other genuine crossovers, none of which is a class separation.** NLTS
(Anshu–Breuckmann–Nirkhe 2022) shows low-energy states of local Hamiltonians need
super-constant depth — about quantum states, with no classical time-class
consequence. Dequantisation (Tang 2018) turns quantum linear-algebra speedups
into classical algorithms: a classical-algorithm outcome, not a class statement.
Unconditional quantum-classical gaps in sampling tasks are separations of *sampling
problems*, not of decision classes.

**Recorded state of the art.** QMA vs NP is open, and QMA(2) still has only
QMA ⊆ QMA(2) ⊆ NEXP. No verified result connects BQP, QMA or QMA(2) to a P vs NP
statement. Saying so is the correct answer rather than a deflationary one.

### Descriptive complexity — ANALOGY-ONLY, with one instructive exception

The organising distinction for this whole field: **a capture theorem is an
equality (Class = Logic); a separation is an inequality (Class₁ ≠ Class₂).** A
characterisation yields a complexity lower bound only when paired with an
*independent* lower bound on the logic's expressive power, and that second
ingredient is where the difficulty and all three barriers actually live.

| Mechanism | What it gives | Verdict |
| --- | --- | --- |
| Fagin 1974; Immerman 1982/1986; Vardi 1982 | NP = ∃SO with no order needed; P = FO(LFP) *on ordered structures* | **ANALOGY-ONLY** |
| Cai–Fürer–Immerman 1992; Grödel–Pakusa 2019; Lichter 2023 | the CFI query is in P and provably not definable in fixed-point logic with counting; rank logic ⊊ P | **ANALOGY-ONLY** — but the most instructive entry |
| Choiceless polynomial time (Blass–Gurevich–Shelah 1999; Lichter–Schweitzer 2024) | CPT sits strictly inside P; whether CPT = P is the live form of "is there a logic capturing P?" | **DEAD** for P vs NP |

**The order asymmetry is real and worth recording.** NP has an order-free
logical characterisation; P has none known, and FO(LFP) without order is provably
weaker than P. Gurevich conjectured that no effectively presented logic captures
P order-free. That asymmetry is the closest thing this field has to a structural
statement about the difficulty, and it is a statement about *definability*, not
about time.

**The instructive exception.** CFI is a theorem of the form "this query is in P
but not definable in this logic", proved by pebble games and linear algebra on
CFI graphs. It is a genuine, unconditional lower bound, obtained by the same
combinatorial toolkit that complexity theory uses — and P vs NP is untouched by
it. That is the clearest demonstration available that logic-expressiveness
inequalities and time-class separations are different currencies. The method
never confronts natural proofs because it makes no claim about circuit size.

**Why CPT does not help.** CPT ⊆ P by construction. CPT = P would be a capture,
i.e. no separation at all; CPT ⊊ P would refute one candidate logic for
capturing P. Either way the complexity question is untouched — the object under
study lives strictly inside P.

**Two items recorded and set aside.** Grohe's identification of graph neural
network expressiveness with FOC² and first-order Weisfeiler–Leman (LICS 2021,
2023) is an exact correspondence for a restricted model — analogy-only here. A
2025 preprint claiming P ≠ NP via computational homology is unrefereed, asserts
rather than demonstrates evasion of the three barriers, and is not counted as a
result.

**Bottom line.** Descriptive complexity explains *why* P is hard to capture —
order, symmetry, counting — but every theorem in the area is an equality or a
logic-level inequality. None becomes a complexity lower bound without an added
machine-level argument, which is exactly what the barriers constrain.

### Topology — one real transfer, into the wrong model

Every candidate here has the shape: a topological invariant I(X) ≥ c, for X built
from f. To become a complexity lower bound it needs a **bridge lemma**:

    circuit C computes f  ⇒  I(Φ(f)) ≤ g(|C|)

with g provably below I on an explicit f. That lemma is where every proposal
lives or dies, and stating it this way makes the failure immediate and local.

| Mechanism | What it gives | Verdict |
| --- | --- | --- |
| Neighbourhood complexes and Borsuk–Ulam (Lovász 1978) | χ(G) ≥ k+2 from (k−1)-connectivity of N(G); settles Kneser | **ANALOGY-ONLY** |
| Borsuk–Ulam for sign-rank (Hatami–Hosseini–Meng, STOC 2023) | a ℤ₂-equivariant bound giving Gap Hamming Distance unbounded-error Ω(log n) with O(1) randomized communication — the strongest possible separation | **TRANSFERABLE, but provably cannot reach P vs NP** |
| Betti numbers of the red-corner complex (Björner–Goresky–MacPherson 2022/2024) | invariants β(f), γ(f) multiplicative under AND/OR; a conjecture would give CC(PARITY) ≥ n²/5 | **ANALOGY-ONLY** |

**Why Kneser does not carry over.** There is no map Φ from circuits to graphs, so
there is no bridge lemma at all. And NP-hardness of χ points the wrong way: it
says computing χ is hard, not that a χ bound refutes small circuits.

**The one genuine transfer, and why it still fails.** Hatami–Hosseini–Meng is a
topology-produced complexity lower bound, unconditional, and it is the strongest
separation of its kind in communication complexity. It transfers — into
communication complexity — and stops there, provably: Set Disjointness lies in P
yet has Ω(n) randomized communication complexity
(Kalyanasundaram–Schnitger 1992), so *no* communication lower bound can imply
P ≠ NP. Any communication bound is consistent with P = NP. The topology exploits
the matrix's ℤ₂ symmetry, and no known encoding transports a language's
Turing-machine complexity into that symmetry.

**Why the Betti-number programme is blocked twice over.** The load-bearing
inequality is a conjecture, not a theorem. Even granting it, the authors state
the invariants "fail to detect exponential complexity" — the advertised
consequences are linear and quadratic, so no superpolynomial bound is in reach.
And γ is extracted from the truth table by linear algebra on a complex with at
most 2ⁿ vertices, so it is constructive in Razborov–Rudich's sense: either γ is
also large on random functions, making it a natural property and blocked
assuming one-way functions, or it is not, and usefulness fails. The programme
establishes neither horn.

**Where topology genuinely returns something.** Three places, none of them P vs
NP. TFNP and PPA (Papadimitriou 1994; Aisenberg–Bonet–Buss 2020 prove 2-D Tucker
and Borsuk–Ulam PPA-complete) concern total search problems — PPA ≠ FP would not
give P ≠ NP. Sign-rank in communication complexity, above. And separations of
constant-size circuit classes via Stone spaces. No topological invariant is known
to yield any statement about P/poly.

### Learning theory — direction is everything, and the popular direction is backwards

Two arrows are routinely conflated. Both are real; neither reaches P vs NP.

    (i)  lower bound  ⇒  learner
    (ii) learner      ⇒  lower bound

| Result | Which arrow | What it lands on | Verdict |
| --- | --- | --- | --- |
| Fortnow–Santhanam, robust simulations (ICALP 2011; JCSS 2017) | neither — improved *simulation* ⇒ separation | NTIME hierarchy, Σ₂ᵖ ⊄ r.o.SIZE(n^k), NEXP ⊄ r.o.ACC⁰ | ANALOGY-ONLY |
| Carmosino–Impagliazzo–Kabanets–Kolmogorov (CCC 2016), sharpened by Pich (2025) | (i) lower bound ⇒ learner | a natural property against C yields a quasipoly learner for C; Pich turns it into an equivalence | ANALOGY-ONLY |
| Fortnow–Klivans (COLT 2006; JCSS 2009) | **(ii) learner ⇒ lower bound** | EXP^NP ⊄ C, or BPEXP ⊄ C for the randomized variant | TRANSFERABLE as technique, ANALOGY-ONLY for P vs NP |

**The error to name.** "Hardness of learning implies circuit lower bounds" is
backwards. Fortnow–Klivans gives learner ⇒ lower bound; contrapositively, no
lower bound ⇒ no efficient learner. Hardness of learning is *explained by* the
existing lower-bound barriers rather than being evidence for them. Getting this
direction wrong is the standard mistake in this area.

**A misattribution corrected.** Fortnow–Santhanam is often cited as a learning
result. It is not: the paper contains no learning algorithm — checked against the
arXiv abstract and the JCSS text. It is a robust-simulation theorem, and its
separations are hierarchy and restricted-circuit statements, which is the regime
Baker–Gill–Solovay shows cannot separate P from NP.

**Why even the good arrow stops short.** Fortnow–Klivans and its descendants all
deliver "X ⊄ C" with X ∈ {EXP^NP, BPEXP, NQP} and C a subclass of P/poly. What a
P vs NP proof needs is **NP ⊄ P/poly**, and there is no bridge from the former to
the latter. The proposed bridge is hardness magnification, whose known
instantiations are conditional and stopped by the locality barrier — see
`notes/08-candidate-conjectures.md`.

**The best unconditional output of this line.** Murray–Williams (STOC 2018)
proves NQP ⊄ ACC∘THR unconditionally from SAT algorithms for ACC∘THR, and
Hirahara (FOCS 2018) shows approximating MCSP is NP-hard under randomized
reductions. These are real, non-relativising lower bounds. They are also lower
bounds for nondeterministic quasi-polytime against a restricted class, which is
one level up and several classes over from where the problem is.

### Communication complexity — the cleanest restricted-model story, and its exact stopping point

| Mechanism | What it gives | Verdict |
| --- | --- | --- |
| Karchmer–Wigderson game (1988/1990) | deterministic communication cost = minimum formula depth; with Spira balancing, depth d gives formula size 2^{Ω(d)} | **ANALOGY-ONLY** |
| Raz–McKenzie lifting (1999) | mon-NC ≠ mon-P, and monotone depth separations | **ANALOGY-ONLY** |
| Query-to-communication lifting, DAG-like (Göös–Pitassi–Watson 2017/2020; Garg–Göös–Kamat–Sokolov 2018; de Rezende et al. FOCS 2020) | proof-size lower bounds, exponential monotone-formula bounds, monotone circuit-vs-formula separations | **DEAD** as a route to P vs NP |

**The precise obstruction, which is often stated imprecisely.** Karchmer–Wigderson
does *not* give circuit size, and it is worth being exact about why. The protocol
is tree-like: each communicated bit splits the residual problem and corresponds
to one formula level. A general circuit is a DAG that reuses subcomputations, and
balancing a size-s circuit yields depth s, not log s. So a KW cost equal to
*circuit* size would require a general circuit-balancing theorem, roughly
P ⊆ NC¹ — itself a major open problem. The mechanism soundly reaches formula
depth and formula size, both restricted models, and stops there.

**Why the monotone results are silent.** Perfect matching lies in P and has
exponential monotone circuit complexity (Razborov 1985; Tardos 1988). Monotone
separations are therefore logically consistent with every general circuit having
polynomial size. DAG-like lifting does reach *size*, but only for monotone and
monotone-real circuits, which is exactly the regime where that counterexample
lives.

**One unrefereed claim, recorded as such.** A 2026 manuscript circulated for
STOC 2027 ("Limits of Lifting") reportedly argues that lifting reductions are
subsumed by Razborov's approximation method, and that every function proved hard
by lifting has a cubic-size non-monotone upper bound. If correct this closes the
route outright. It is unrefereed and is not treated as established here, but it
points the same way as everything else in this section.

**Summary for the field.** No lifting theorem, size or depth, has produced a
superpolynomial non-monotone circuit lower bound. The barriers are neither
confronted nor evaded, because the programme succeeds precisely where those
barriers do not bite.

### Statistical mechanics of random CSPs — rigorous, and rigorous about the wrong thing

Every theorem here concerns a random ensemble (average case) or a planted
distribution. It is either an existence/free-energy result or a lower bound
against a restricted algorithm class. P vs NP is worst case over all poly-time
algorithms, so three gaps open immediately: average-case hardness does not give
worst-case hardness; restricted-model bounds are not general ones; and existence
thresholds say nothing about computation.

The sharpest form of the last point: **P ≠ NP does not imply that random 3-SAT
is hard on average.** Impagliazzo's Heuristica and Pessiland are consistent
worlds, so the average-case hardness of random SAT is logically independent of
the separation. This literature and P vs NP are not measuring the same thing.

| Mechanism | What it gives | Verdict |
| --- | --- | --- |
| Rigorous 1RSB / cavity-method validation (Ding–Sly–Sun, *Annals* 2022, *Acta* 2016; Coja-Oghlan–Panagiotou 2016; Coja-Oghlan–Krzakala–Perkins–Zdeborová 2018) | the satisfiability threshold for large k: α_sat(k) = 2^k ln 2 − (1+ln 2)/2 + o_k(1) | **ANALOGY-ONLY** |
| Overlap Gap Property plus stability (Gamarnik–Sudan 2017; Gamarnik–Jagannath–Wein 2024) | every o(n)-stable polynomial-time algorithm fails on the planted ensemble | **ANALOGY-ONLY** |
| Shattering and freezing (Achlioptas–Coja-Oghlan, FOCS 2008; Achlioptas–Ricci-Tersenghi 2009) | the solution space shatters into exp(Θ(n)) well-separated clusters | **ANALOGY-ONLY** |

**The threshold theorems locate existence, not findability.** α_sat(k) describes
where solutions exist, and says nothing about whether they can be found. The
tempting inference "physics transition = complexity transition" is precisely the
unproven analogy, and it is worth stating that the rigour of these proofs — they
are among the hardest results in the area — is rigour about a question adjacent
to P vs NP rather than about it.

*A correction to the received summary.* The tight rigorous 1RSB results are for
independent sets and NAE-SAT, not MAX-CUT. MAX-CUT's rigorous value is
Dembo–Montanari–Sen (2017), and El Alaoui–Montanari–Sellke (2023) give an
efficient local algorithm attaining it. That is an information-theoretic optimum
which is *computable*, and it is the cleanest available demonstration that a
threshold is not a hardness result.

**The Overlap Gap Property is necessary, not sufficient, and this is now proved.**
OGP combined with o(n)-stability does block a class of algorithms, and that is a
real theorem. But Li–Schramm (COLT 2025) prove OGP for shortest path in G(n,p) and
in complete graphs — a problem that is polynomial-time solvable and even
samplable. So OGP does not certify hardness, and "OGP explains hardness" is false
as a general claim. The bounded-depth corollary of the OGP line *is* a circuit
lower bound, but for a search problem on a random ensemble, and Razborov–Rudich's
largeness condition is exactly what the Li–Schramm counterexample undermines.

**The one argument in this literature that targets a separation.** Feige (STOC
2002, Hypothesis 1): no polynomial-time algorithm refutes most random 3-CNFs at
density Δn while never refuting a satisfiable formula. If that holds, P ≠ NP
follows, because P = NP would give an exact SAT decider and hence such a refuter.
It is the only checkable S ⟹ separation statement here. Note what it is: a
conditional target, and one whose reduction relativises, so it relocates the
difficulty into S rather than evading any barrier. Proving S is at least as hard
as the separation it implies.

## Synthesis: six fields, zero transfers

| Field | Best candidate | Outcome |
| --- | --- | --- |
| Quantum | MIP\* = RE | DEAD — a computability theorem, and it refutes Connes rather than separating classes |
| Descriptive complexity | Fagin / Immerman–Vardi, CFI | ANALOGY-ONLY — a characterisation is an equality, not an inequality |
| Topology | Borsuk–Ulam for sign-rank | TRANSFERABLE into communication complexity, which provably cannot reach P vs NP |
| Learning theory | Fortnow–Klivans | learner ⇒ lower bound is real, but lands on EXP^NP vs a subclass of P/poly |
| Communication complexity | DAG-like lifting | reaches size only for monotone circuits |
| Statistical mechanics | Feige's Hypothesis 1 | the only S ⟹ separation target here, and it is conditional |

**Zero transfers to P vs NP.** Not because the fields are barren —
several produced genuine, hard, unconditional theorems — but because every one of
them lower-bounds a resource that maps onto a *restricted model*, and restricted
models are provably exponentially weaker than the general case. Perfect matching
is in P and has exponential monotone complexity; that single example kills the
whole monotone line as a route.

**The most useful observation in this survey is about the barriers, not the
techniques.** These programmes do not *evade* relativisation, natural proofs or
algebrization. They succeed precisely where those barriers do not apply, because
they are not attempting a non-relativising separation at all. A theorem that has
never confronted a barrier has not slipped past it — it has walked around the
outside of the problem.

**What does export.** One thing, and it is methodological rather than
mathematical: the **bridge lemma**. Any proposed transfer must exhibit

    circuit C computes f  ⇒  I(Φ(f)) ≤ g(|C|)

with g provably below I. Stating this explicitly takes about a minute and settles
most proposals immediately, because the map Φ usually does not exist. That is
worth carrying into any cross-field proposal you meet.
