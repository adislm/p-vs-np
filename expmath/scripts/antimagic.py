#!/usr/bin/env python3
"""
Antimagic labeling conjecture (Hartsfield-Ringel 1990; popularized by Ringel):
  Every connected graph with at least one edge, other than K_2, has an
  *antimagic* labeling: a bijection edge -> {1,...,m} (m = #edges) such that
  the m vertex sums are pairwise distinct.
(Equivalently: the "antimagic graph" conjecture. Open in general; K_2 is the
unique known exception: its single edge gives both endpoints sum 1.)

We exhaustively enumerate ALL connected graphs on n vertices (n small) and
look for a connected graph != K_2 admitting NO antimagic labeling.  Any such
graph would be a counterexample; none is expected.

Exhaustive over: all labeled connected graphs on n <= NMAX.
"""
import sys, time
from itertools import combinations

def antimagic_labeling(n, edges):
    """Return a list L (L[e] = label in 1..m) that is antimagic, or None if
    no antimagic labeling exists.  Fully exhaustive backtracking."""
    m = len(edges)
    if m == 0:
        return []  # single vertex, vacuously antimagic
    inc = [[] for _ in range(n)]
    for ei,(a,b) in enumerate(edges):
        inc[a].append(ei); inc[b].append(ei)
    vsum = [0]*n
    done_deg = [0]*n
    assign = [0]*m
    # order edges to close vertices early: greedy by shared vertices is possible,
    # but any order is correct. Use natural order.
    full = (1<<(m+1)) - 2   # bits 1..m set  (bit0 unused)
    # precompute for each edge index how many incident edges already placed is dynamic.
    counter = [0]
    import sys as _s
    _s.setrecursionlimit(10000)

    def closed_check(just_closed):
        # just_closed: list of vertex indices whose last incident edge placed now
        sums = {}
        for v in just_closed:
            s = vsum[v]
            if s in sums:
                return False
            sums[s]=v
        # also compare against previously-closed vertices
        for v in range(n):
            if done_deg[v]==len(inc[v]) and v not in just_closed:
                s=vsum[v]
                if s in sums:
                    return False
                sums[s]=v
        return True

    def rec(ei, used):
        counter[0]+=1
        if ei==m:
            # all closed automatically; distinctness enforced incrementally
            return True
        a,b = edges[ei]
        for lab in range(1,m+1):
            bit = 1<<lab
            if used & bit: continue
            vsum[a]+=lab; vsum[b]+=lab
            assign[ei]=lab
            done_deg[a]+=1; done_deg[b]+=1
            just=[]
            ok=True
            if done_deg[a]==len(inc[a]): just.append(a)
            if done_deg[b]==len(inc[b]) and b!=a: just.append(b)
            if just:
                ok = closed_check(just)
            if ok and rec(ei+1, used|bit):
                return True
            # undo
            vsum[a]-=lab; vsum[b]-=lab
            done_deg[a]-=1; done_deg[b]-=1
        return False

    if rec(0,0):
        return assign[:]
    return None

def connected(n, edges):
    if n==0: return True
    parent=list(range(n))
    def f(x):
        while parent[x]!=x:
            parent[x]=parent[parent[x]]; x=parent[x]
        return x
    for a,b in edges:
        ra,rb=f(a),f(b)
        if ra!=rb: parent[ra]=rb
    r=f(0)
    return all(f(i)==r for i in range(n))

def gen_connected_graphs(n):
    """Yield edge lists of all (labeled) connected graphs on vertices 0..n-1.
    Simple approach: iterate all edge subsets (2^M) and filter connected.
    M=C(n,2); feasible for n<=7."""
    allpairs=list(combinations(range(n),2))
    M=len(allpairs)
    for mask in range(1<<M):
        edges=[allpairs[i] for i in range(M) if (mask>>i)&1]
        if connected(n,edges):
            yield edges

def verify_antimagic(n, edges, labels):
    m=len(edges)
    assert sorted(labels)==list(range(1,m+1)), "not a bijection to 1..m"
    vsum=[0]*n
    for (a,b),lab in zip(edges,labels):
        vsum[a]+=lab; vsum[b]+=lab
    assert len(set(vsum))==n, f"vertex sums not distinct: {vsum}"
    # confirm edge label -> endpoints
    return vsum

if __name__=="__main__":
    # ---- unit tests on known cases ----
    K2=[(0,1)]
    assert antimagic_labeling(2,K2) is None, "K2 should be non-antimagic"
    P3=[(0,1),(1,2)]
    L=antimagic_labeling(3,P3); assert L is not None and verify_antimagic(3,P3,L)
    C3=[(0,1),(1,2),(2,0)]
    L=antimagic_labeling(3,C3); assert L is not None and verify_antimagic(3,C3,L)
    K3=C3
    Star=[(0,1),(0,2),(0,3)]
    L=antimagic_labeling(4,Star); assert L is not None and verify_antimagic(4,Star,L)
    C4=[(0,1),(1,2),(2,3),(3,0)]
    L=antimagic_labeling(4,C4); assert L is not None and verify_antimagic(4,C4,L)
    print("unit tests passed (K2 non-antimagic; P3,C3,K3,K1,3,C4 antimagic)")

    NMAX=int(sys.argv[1]) if len(sys.argv)>1 else 6
    for n in range(2, NMAX+1):
        t0=time.time(); nconn=0; bad=[]
        for edges in gen_connected_graphs(n):
            nconn+=1
            L=antimagic_labeling(n,edges)
            if L is None:
                bad.append(edges)
        dt=time.time()-t0
        print(f"n={n}: connected graphs checked={nconn}, non-antimagic={len(bad)}, time={dt:.2f}s")
        for e in bad:
            print("   NON-ANTIMAGIC:", e)
