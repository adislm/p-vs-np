#!/usr/bin/env python3
"""
Ryser's conjecture (1967): every Latin square of ODD order has a transversal
(n cells, one per row & column, all n symbols distinct). OPEN in general.
Even order can fail: Cayley table of Z_6 (cyclic even) has none (Hall-Paige).

METHOD
 * Transversal existence is invariant under isotopy (independent row/column/
   symbol permutations), which map transversals to transversals.
 * Classical identity: #LatinSquares(n) = R(n) * n! * (n-1)! , R(n)=#reduced.
 * So checking every REDUCED Latin square settles EVERY square of that order.
 * Exhaustive: orders 3 and 5.  Heuristic: random reduced squares, order 7,9.
"""
import sys, random, time
from itertools import permutations

def is_latin(L,n):
    return (all(sorted(r)==list(range(n)) for r in L) and
            all(sorted(L[r][c] for r in range(n))==list(range(n)) for c in range(n)))

def has_transversal(L,n):
    used_col=[False]*n; used_sym=[False]*n
    def rec(r):
        if r==n: return True
        for c in range(n):
            if not used_col[c]:
                s=L[r][c]
                if not used_sym[s]:
                    used_col[c]=used_sym[s]=True
                    if rec(r+1): return True
                    used_col[c]=used_sym[s]=False
        return False
    return rec(0)

def reduced_latin(n):
    """Yield every reduced Latin square (row0 = col0 = 0,1,...,n-1)."""
    L=[[0]*n for _ in range(n)]
    L[0]=list(range(n))
    perms=list(permutations(range(1,n)))   # row r>=1 has p[0]=r fixed
    def rec(r):
        if r==n:
            yield [row[:] for row in L]; return
        for tail in perms:
            p=(r,)+tail
            ok=True
            for c in range(1,n):
                for rr in range(r):
                    if L[rr][c]==p[c]: ok=False;break
                if not ok: break
            if ok:
                L[r][:]=p
                yield from rec(r+1)
    yield from rec(1)

def random_reduced_latin(n, rng):
    L=[[0]*n for _ in range(n)]; L[0]=list(range(n))
    perms=list(permutations(range(1,n)))
    def rec(r):
        if r==n: return True
        ps=perms[:]; rng.shuffle(ps)
        for tail in ps:
            p=(r,)+tail; ok=True
            for c in range(1,n):
                for rr in range(r):
                    if L[rr][c]==p[c]: ok=False;break
                if not ok: break
            if ok:
                L[r][:]=p
                if rec(r+1): return True
        return False
    rec(1); return [row[:] for row in L]

def cyclic_table(n): return [[(i+j)%n for j in range(n)] for i in range(n)]

if __name__=="__main__":
    Z5,Z6=cyclic_table(5),cyclic_table(6)
    assert is_latin(Z5,5) and is_latin(Z6,6)
    a,b=has_transversal(Z5,5),has_transversal(Z6,6)
    print(f"VALIDATION: Z5 transversal={a} (expect True); Z6 transversal={b} (expect False)")
    assert a and not b

    import math
    for n in (3,5):
        t0=time.time(); R=0; noT=0
        for L in reduced_latin(n):
            R+=1
            if not has_transversal(L,n): noT+=1; print("  NO-TRANSVERSAL reduced:",L)
        total=R*math.factorial(n)*math.factorial(n-1)
        print(f"order {n}: EXHAUSTIVE. reduced={R}, all squares={total} "
              f"(=R*n!*(n-1)!); without transversal={noT}; {time.time()-t0:.1f}s")

    rng=random.Random(12345)
    for n,trials in ((7,int(sys.argv[1]) if len(sys.argv)>1 else 500),
                     (9,int(sys.argv[2]) if len(sys.argv)>2 else 20)):
        t0=time.time(); noT=0
        for _ in range(trials):
            L=random_reduced_latin(n,rng)
            assert is_latin(L,n)
            if not has_transversal(L,n): noT+=1
        print(f"order {n}: HEURISTIC. {trials} random reduced Latin squares; "
              f"without transversal={noT}; {time.time()-t0:.1f}s")
