# List-version tests for Debski-Grytczuk-Pawlik, arXiv:2209.08507.
#
# Conjecture 1 (paper): for every n and every sequence A_1,...,A_n of alphabets
#   of size 4, there is a steady word W = w_1...w_n with w_i in A_i.
# Grytczuk's analogous (2008) conjecture, restated as still open in the paper:
#   the same with "steady" replaced by "square-free" and lists of size 3.
#
# A word is steady iff it is square-free and deleting any one letter leaves a
# square-free word.  Steadiness and square-freeness are both prefix-closed
# (a prefix of a steady word is steady), so left-to-right backtracking with
# prefix pruning is exhaustive.
#
# Exhaustive over ALL assignments of s-element lists drawn from a fixed
# universe [m].  WLOG the first list is {0,...,s-1}: the property is invariant
# under permutations of the universe, so every assignment is equivalent to one
# with that first list.  (Full enumeration without WLOG is run for small n as a
# check.)

import sys, itertools, time

def square_free(t):
    n = len(t)
    for p in range(1, n // 2 + 1):
        for i in range(n - 2 * p + 1):
            if t[i:i+p] == t[i+p:i+2*p]:
                return False
    return True

def steady_ok(t):
    if not square_free(t):
        return False
    for d in range(len(t)):
        if not square_free(t[:d] + t[d+1:]):
            return False
    return True

def ok_prefix(t, kind):
    return steady_ok(t) if kind == "steady" else square_free(t)

def exists(assign, kind, want_witness=False):
    n = len(assign)
    w = []
    def rec(i):
        if i == n:
            return True
        for c in assign[i]:
            w.append(c)
            if ok_prefix(w, kind) and rec(i + 1):
                return True
            w.pop()
        return False
    r = rec(0)
    return (r, tuple(w)) if want_witness else r

def enumerate_assignments(m, s, n, kind, full=False, limit=None, progress=False):
    """Return (num_checked, first_bad_assignment_or_None, witness_if_all_good)."""
    subsets = list(itertools.combinations(range(m), s))
    if full:
        firsts = subsets
    else:
        firsts = [tuple(range(s))]
    checked = 0
    bad = None
    witness = None
    t0 = time.time()
    for f in firsts:
        for rest in itertools.product(subsets, repeat=n - 1):
            checked += 1
            assign = (f,) + rest
            r, wit = exists(assign, kind, want_witness=True)
            if not r:
                bad = assign
                return checked, bad, None
            if witness is None:
                witness = (assign, wit)
            if limit and checked >= limit:
                return checked, bad, witness
            if progress and checked % 500000 == 0:
                print(f"  ... {checked} assignments, {time.time()-t0:.1f}s")
    return checked, bad, witness

def selftest():
    print("selftest:")
    a = ((0,1,2,3),)*5
    r, w = exists(a, "steady", True)
    print("  steady, all lists [4], n=5:", r, "witness", w, "steady_ok", steady_ok(w))
    print("  square-free, all lists {0}, n=2:", exists(((0,),(0,)), "square-free"), "(expect False)")
    print("  square-free, all lists {0}, n=1:", exists(((0,),), "square-free"), "(expect True)")
    # full vs WLOG agreement on a tiny case
    for kind, m, s, n in [("square-free", 4, 3, 4), ("steady", 4, 4, 4), ("steady", 5, 4, 4)]:
        c1, b1, _ = enumerate_assignments(m, s, n, kind, full=True)
        c2, b2, _ = enumerate_assignments(m, s, n, kind, full=False)
        print(f"  full vs WLOG {kind} m={m} s={s} n={n}: full bad={b1} wlog bad={b2} "
              f"(both None: {b1 is None and b2 is None})")

if __name__ == "__main__":
    mode = sys.argv[1]
    if mode == "selftest":
        selftest()
    elif mode == "run":
        kind = sys.argv[2]; m = int(sys.argv[3]); s = int(sys.argv[4]); n = int(sys.argv[5])
        full = (len(sys.argv) > 6 and sys.argv[6] == "full")
        print(f"run kind={kind} universe={m} listsize={s} n={n} full={full}")
        c, bad, wit = enumerate_assignments(m, s, n, kind, full=full, progress=True)
        print(f"checked {c} assignments")
        if bad is not None:
            print("COUNTEREXAMPLE ASSIGNMENT:", bad)
            print("  (no word of this kind exists with w_i in A_i)")
        else:
            print("NO COUNTEREXAMPLE in this exhaustive range")
            if wit:
                print("  example assignment/witness:", wit[0], "->", wit[1])
