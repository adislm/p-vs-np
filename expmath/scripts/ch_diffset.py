#!/usr/bin/env python3
"""
Circulant Hadamard search via cyclic difference sets.

Fact (classical): a circulant +/-1 matrix of order n is Hadamard iff its first
row's +1 positions D form a cyclic (n, k, lambda) difference set in Z_n with
n = 4u^2, k = 2u^2 - u (or its complement 2u^2 + u), lambda = u^2 - u.
(A cyclic (v,k,l) difference set: every nonzero residue is d1-d2 for exactly
lambda ordered pairs d1,d2 in D, d1 != d2.)

We search for such D exhaustively by backtracking, WLOG 0 in D.
A found D yields a circulant Hadamard matrix; none for u>1 supports the
circulant Hadamard conjecture (none for n>4).
"""
import sys, time

def find_diffset(v, k, lam, timeout=None):
    """Exhaustive backtracking for a cyclic (v,k,lam) difference set.
    Returns a sorted tuple D, or None if none exists.  Raises TimeoutError
    if timeout (seconds) elapses first."""
    if k == 0:
        return () if lam == 0 else None
    count = [0]*v            # count[s] = ordered pairs (d1,d2) with d1-d2==s
    D = [0]                  # WLOG 0 in D
    t0 = time.time()
    nodes = [0]

    def rec():
        if timeout is not None and time.time()-t0 > timeout:
            raise TimeoutError
        nodes[0]+=1
        if len(D) == k:
            return all(count[s]==lam for s in range(1,v))
        # Lower-bound prune: with r=k-|D| elements still to add, any single
        # difference s can gain at most 2 per new element (pairs {x,x-s},{x,x+s}).
        r = k - len(D)
        for s in range(1, v):
            if count[s] + 2*r < lam:
                return None
        # next element must be > last (canonical increasing order)
        start = D[-1]+1
        # remaining slots after this choice
        need = k - len(D)
        for x in range(start, v):
            # a new element x is <= last possible so that enough room remains
            if v - x < need:      # not enough integers left (incl x) to fill
                break
            # apply: for each existing d, differences x-d and d-x
            ok = True
            added = []
            for d in D:
                s1 = (x-d) % v
                s2 = (d-x) % v
                count[s1]+=1; added.append(s1)
                count[s2]+=1; added.append(s2)
                if count[s1] > lam or count[s2] > lam:
                    ok = False
                    break
            if ok:
                D.append(x)
                r = rec()
                if r is not None:
                    return r
                D.pop()
            # undo
            for s in added:
                count[s]-=1
        return None

    res = rec()
    return (tuple(D) if res else None), nodes[0]

def circulant_matrix_from_D(v, D):
    """row i (0-indexed shift) has +1 at (j) where (j-i) mod v in D."""
    Dset = set(D)
    return [[1 if (j-i) % v in Dset else -1 for j in range(v)] for i in range(v)]

def verify_hadamard(M):
    n = len(M)
    assert all(len(r)==n for r in M)
    for i in range(n):
        for j in range(n):
            dot = sum(M[i][t]*M[j][t] for t in range(n))
            if i==j:
                if dot != n: return False, (i,j,dot)
            else:
                if dot != 0: return False, (i,j,dot)
    return True, None

if __name__ == "__main__":
    umax = int(sys.argv[1]) if len(sys.argv)>1 else 11
    per_u_timeout = float(sys.argv[2]) if len(sys.argv)>2 else 60.0
    print(f"{'u':>4} {'n=4u^2':>8} {'k':>8} {'lam':>6} {'found?':>8} {'nodes':>12}  time")
    for u in range(1, umax+1, 2):     # u odd only
        v = 4*u*u; k = 2*u*u - u; lam = u*u - u
        t0=time.time()
        try:
            res = find_diffset(v,k,lam, timeout=per_u_timeout)
            if res is None:
                D, nodes = None, 0
            else:
                D, nodes = res
            dt=time.time()-t0
            print(f"{u:>4} {v:>8} {k:>8} {lam:>6} {str(D is not None):>8} {nodes:>12}  {dt:8.2f}s")
            if D is not None:
                M = circulant_matrix_from_D(v,D)
                ok,why = verify_hadamard(M)
                print(f"     witness D={D}  Hadamard-verified={ok}  (n={v})")
                if v<=8:
                    for row in M: print("     ",row)
        except TimeoutError:
            dt=time.time()-t0
            print(f"{u:>4} {v:>8} {k:>8} {lam:>6} {'TIMEOUT':>8} {'':>12}  {dt:8.2f}s")
