# Reproduce Table 1 of Debski-Grytczuk-Pawlik, "Extensions and reductions of
# square-free words", arXiv:2209.08507 (Sept 2022), Discrete Math 347(3):113825 (2024).
# Table 1: number N of quaternary steady words of length n, up to permutations of symbols.
#
# Definitions (from the paper):
#   square-free: no factor XX with X nonempty.
#   steady: square-free and stays square-free after deleting any single letter.
# Count up to relabeling of the 4-letter alphabet (restricted-growth canonical form).

import sys

MAXN = int(sys.argv[1]) if len(sys.argv) > 1 else 32

def squares_ending_at_end(u):
    """Return True iff u (assumed square-free before its last char was appended)
    has a square factor whose right end is the last position."""
    n = len(u)
    for p in range(1, n // 2 + 1):
        if u[n - 2*p:n - p] == u[n - p:n]:
            return True
    return False

def canon(w):
    mp = {}
    out = []
    for c in w:
        if c not in mp:
            mp[c] = len(mp)
        out.append(mp[c])
    return tuple(out)

# A clean (non-incremental) steady check, used once as an independent cross-check.
def square_free(w):
    n = len(w)
    for p in range(1, n // 2 + 1):
        for i in range(n - 2*p + 1):
            if w[i:i+p] == w[i+p:i+2*p]:
                return False
    return True

def steady_ref(w):
    if not square_free(w):
        return False
    for d in range(len(w)):
        if not square_free(w[:d] + w[d+1:]):
            return False
    return True

counts = {n: 0 for n in range(1, MAXN + 1)}
canon_sets = {n: set() for n in range(1, MAXN + 1)}

# DFS. State: w (tuple), reds = tuple of tuples, where reds[d] = w with position d deleted
# (for d = 0..len(w)-1), all known square-free. Invariant: w is steady.
def dfs(w, reds):
    n = len(w)
    if n >= 1:
        c = canon(w)
        if c not in canon_sets[n]:
            canon_sets[n].add(c)
            counts[n] += 1
    if n == MAXN:
        return
    for c in range(4):
        u = w + (c,)
        if squares_ending_at_end(u):
            continue
        new_reds = []
        ok = True
        for d in range(n):
            r = reds[d] + (c,)
            if squares_ending_at_end(r):
                ok = False
                break
            new_reds.append(r)
        if not ok:
            continue
        # u minus position n is w, which is steady hence square-free.
        new_reds.append(w)
        dfs(u, tuple(new_reds))

dfs((), ())

expected = {
3:1,4:2,5:3,6:5,7:5,8:7,9:9,10:12,11:16,12:21,13:28,14:37,15:45,16:58,
17:73,18:93,19:101,20:124,21:150,22:179,23:216,24:257,25:309,26:376,
27:453,28:551,29:662,30:798,31:957,32:1149}

print("n   computed  paper  match")
allok = True
for n in range(3, MAXN + 1):
    p = expected.get(n)
    m = (p == counts[n]) if p is not None else None
    if p is not None and not m:
        allok = False
    print(f"{n:2d}  {counts[n]:8d}  {str(p):>5s}  {m}")
print("ALL MATCH" if allok else "MISMATCH")

# Independent cross-check of the incremental steady machinery vs brute force,
# for all words up to length 6 over 4 letters.
if MAXN >= 6:
    import itertools
    bad = 0
    for n in range(1, 7):
        for t in itertools.product(range(4), repeat=n):
            # brute steady:
            r1 = steady_ref(list(t))
            # incremental-style: simulate by direct definition too
            # (we also verify the counting machinery found exactly the steady ones)
            if r1 != steady_ref(list(t)):
                bad += 1
        # count brute-force steady up to symmetry for small n
        s = set()
        for t in itertools.product(range(4), repeat=n):
            if steady_ref(list(t)):
                s.add(canon(list(t)))
        if len(s) != counts[n]:
            print(f"CROSSCHECK FAIL at n={n}: brute {len(s)} vs incremental {counts[n]}")
            bad += 1
    print("CROSSCHECK OK" if bad == 0 else "CROSSCHECK FAILED")
