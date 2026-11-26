# Bifurcate words, from Debski-Grytczuk-Pawlik, arXiv:2209.08507.
#   square-free: no factor XX (X nonempty).
#   bifurcate over A: square-free W such that for EVERY insertion position
#   i in {0,...,|W|} there is a letter x in A with insert_i(W,x) square-free.
#   single-letter extension: insert one letter at one position.
#
# Conjecture 2 (quaternary): there is an infinite sequence W_1,W_2,... of
#   bifurcate words over 4 letters with W_{i+1} a single-letter extension of W_i.
#   By Koenig (finitely branching) this holds iff chains of every length exist;
#   we compute the longest chain anchored at a single letter, up to length L.
#
# Conjecture 3: there is a complete bifurcate tree over 5 letters.
#   G(W,d) = W is bifurcate and, for every insertion position i, some letter x
#   gives a child insert_i(W,x) that is bifurcate and satisfies G(child,d-1).
#   G(W,0) = W bifurcate.  A complete (infinite) tree from root c exists iff
#   G((c,),d) for all d.  Validate: Theorem 7 says over 4 letters no complete
#   tree has words of length > 6, i.e. max depth from a length-1 root is 5.
#
# All search is exhaustive over labelled words over a fixed alphabet [k].

import sys, time
from functools import lru_cache

sys.setrecursionlimit(1000000)
T0 = time.time()

@lru_cache(maxsize=None)
def square_free(w):
    n = len(w)
    for p in range(1, n // 2 + 1):
        for i in range(n - 2 * p + 1):
            if w[i:i+p] == w[i+p:i+2*p]:
                return False
    return True

def insert(w, i, x):
    return w[:i] + (x,) + w[i:]

def canon(w):
    mp = {}; out = []
    for c in w:
        if c not in mp: mp[c] = len(mp)
        out.append(mp[c])
    return tuple(out)

@lru_cache(maxsize=None)
def bifurcate(w, k):
    if not square_free(w):
        return False
    for i in range(len(w) + 1):
        ok = False
        for x in range(k):
            if square_free(insert(w, i, x)):
                ok = True; break
        if not ok:
            return False
    return True

# ---------------- Conjecture 2: chains ----------------
def chain_analysis(k, L):
    by_len = [set() for _ in range(L + 1)]
    def dfs(w):
        by_len[len(w)].add(w)
        if len(w) == L:
            return
        for c in range(k):
            u = w + (c,)
            if bifurcate(u, k):
                dfs(u)
    for c in range(k):
        dfs((c,))
    depth = {}
    maxd_by_len = {}
    for l in range(1, L + 1):
        for w in by_len[l]:
            if l == 1:
                depth[w] = 1
            else:
                best = 0
                for d in range(l):
                    p = w[:d] + w[d+1:]
                    if p in depth and depth[p] > best:
                        best = depth[p]
                depth[w] = 1 + best if best > 0 else 0
        maxd_by_len[l] = max((depth[w] for w in by_len[l]), default=0)
    print(f"chain analysis k={k}, L={L}")
    print("len  #bifurcate  max_chain_depth")
    for l in range(1, L + 1):
        print(f"{l:3d}  {len(by_len[l]):10d}  {maxd_by_len[l]}")
    # Reconstruct and verify an explicit longest chain.
    l = L
    while l >= 1 and maxd_by_len[l] == 0:
        l -= 1
    if l >= 1:
        target = maxd_by_len[l]
        cand = [w for w in by_len[l] if depth[w] == target]
        w = cand[0]
        chain = [w]
        while len(w) > 1:
            for d in range(len(w)):
                p = w[:d] + w[d+1:]
                if p in depth and depth[p] == depth[w] - 1:
                    chain.append(p); w = p; break
        chain.reverse()
        okv = True
        for a, b in zip(chain, chain[1:]):
            is_ext = any(b[:i] + b[i+1:] == a for i in range(len(b)))
            if not (len(b) == len(a) + 1 and is_ext and bifurcate(a, k) and bifurcate(b, k)):
                okv = False
        print(f"WITNESS chain of {len(chain)} bifurcate words (verified={okv}):")
        print("  " + " -> ".join("".join(map(str, w)) for w in chain))
    return by_len, depth, maxd_by_len

# ---------------- paper cross-checks ----------------
def checkpaper():
    # Debski et al. state: 1231 is steady; 1213 is not steady (reduction 113);
    # 12312 is bifurcate but not steady; and the five square-free one-letter
    # extensions of 1231 over {1,2,3} are 21231,13231,12131,12321,12312.
    def sf(t):
        return square_free(tuple(t))
    def st(t):
        t = tuple(t)
        if not sf(t):
            return False
        return all(sf(t[:d] + t[d+1:]) for d in range(len(t)))
    print("1231 steady:", st([1,2,3,1]), "(paper: True)")
    print("1213 steady:", st([1,2,1,3]), "(paper: False)")
    t = tuple([1,2,1,3])
    print("  reduction of 1213 deleting position 3:", "".join(map(str, t[:2] + t[3:])), "(paper: 113)")
    print("12312 steady:", st([1,2,3,1,2]), "(paper: False)")
    print("12312 bifurcate:", bifurcate((1,2,3,1,2), 3), "(paper: True)")
    exts = set()
    w = (1,2,3,1)
    for i in range(len(w) + 1):
        for x in (1,2,3):
            u = insert(w, i, x)
            if square_free(u):
                exts.add(u)
    printed = sorted("".join(map(str, u)) for u in exts)
    expected = sorted(["21231","13231","12131","12321","12312"])
    print("square-free extensions of 1231 over {1,2,3}:", printed)
    print("  paper list:", expected, " match:", printed == expected)

# ---------------- probe: max word length of any complete tree ----------------
def probe(k, Lmax, dcap):
    words = []
    def dfs(w):
        words.append(w)
        if len(w) == Lmax:
            return
        for c in range(k):
            u = w + (c,)
            if bifurcate(u, k):
                dfs(u)
    if bifurcate((), k):
        dfs(())
    best = -1; bestw = None; bestd = None
    for w in words:
        memo.clear(); calls = 0
        d, status = max_complete_depth(w, k, dcap)
        if len(w) + d > best:
            best = len(w) + d; bestw = w; bestd = d
    print(f"probe k={k} Lmax={Lmax} dcap={dcap}: max word length in a complete tree = {best} "
          f"(root {bestw}, depth {bestd}) over {len(words)} bifurcate roots")
    return best

# ---------------- Conjecture 3: complete trees ----------------
memo = {}
calls = 0
NODE_CAP = 3_000_000
class Cap(Exception): pass

def G(w, k, d):
    global calls
    calls += 1
    if calls > NODE_CAP:
        raise Cap()
    w = canon(w)
    key = (w, d)
    v = memo.get(key)
    if v is not None:
        return v
    if not bifurcate(w, k):
        memo[key] = False
        return False
    if d == 0:
        memo[key] = True
        return True
    r = len(set(w))
    letters = list(range(r)) + ([r] if r < k else [])
    for i in range(len(w) + 1):
        found = False
        for x in letters:
            child = insert(w, i, x)
            if G(child, k, d - 1):
                found = True
                break
        if not found:
            memo[key] = False
            return False
    memo[key] = True
    return True

def max_complete_depth(root, k, dcap):
    d = 0
    while d < dcap:
        try:
            if G(root, k, d + 1):
                d += 1
            else:
                break
        except Cap:
            return d, "CAP"
    return d, ("DCAP" if d == dcap else "FALSE")

def tree_analysis(k, dcap):
    global calls
    print(f"complete-tree analysis k={k}, dcap={dcap}")
    best = -1; bestroot = None
    for c in range(k):
        memo.clear(); calls = 0
        d, status = max_complete_depth((c,), k, dcap)
        print(f"  root {c}: max depth {d}  (status {status}, states {len(memo)}, calls {calls}, "
              f"{time.time()-T0:.1f}s) -> deepest word length {1+d}")
        if d > best:
            best = d; bestroot = c
    print(f"  MAX depth over roots = {best} (root {bestroot}), deepest word length {1+best}")
    return best

if __name__ == "__main__":
    mode = sys.argv[1]
    if mode == "chain":
        k = int(sys.argv[2]); L = int(sys.argv[3])
        chain_analysis(k, L)
    elif mode == "tree":
        k = int(sys.argv[2]); dcap = int(sys.argv[3])
        tree_analysis(k, dcap)
    elif mode == "checkpaper":
        checkpaper()
    elif mode == "probe":
        k = int(sys.argv[2]); Lmax = int(sys.argv[3]); dcap = int(sys.argv[4])
        probe(k, Lmax, dcap)
