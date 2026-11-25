#!/usr/bin/env python3
"""
Graceful Tree Conjecture (Ringel 1964 / Kotzig-Ringel 1967; a.k.a. Ringel-Kotzig):
  Every tree with m edges has a GRACEFUL labeling: a bijection
  f: V -> {0,1,...,m} such that the edge labels |f(u)-f(v)| are all distinct
  (hence exactly {1,...,m}).  OPEN in general (proved for many classes).

Falsification target: a tree with NO graceful labeling.

We exhaustively consider ALL (unlabeled) trees on n vertices for n<=NMAX,
enumerated via Prufer sequences (labeled, a covering superset) and then
de-duplicated by a tree canonical form.  'graceful' is iso-invariant, so
checking one representative per iso class is exhaustive over all trees.
"""
import sys, time
from itertools import product

def prufer_to_edges(seq, n):
    degree=[1]*n
    for x in seq: degree[x]+=1
    edges=[]
    import heapq
    leaves=[i for i in range(n) if degree[i]==1]
    heapq.heapify(leaves)
    for x in seq:
        leaf=heapq.heappop(leaves)
        edges.append((leaf,x))
        degree[leaf]-=1; degree[x]-=1
        if degree[x]==1: heapq.heappush(leaves,x)
    u=heapq.heappop(leaves); v=heapq.heappop(leaves)
    edges.append((u,v))
    return edges

def canonical(n, edges):
    """Canonical form of an unrooted tree (AHU, min over roots)."""
    adj=[[] for _ in range(n)]
    for u,v in edges: adj[u].append(v); adj[v].append(u)
    from functools import lru_cache
    def rooted_code(root):
        # iterative DFS producing canonical nested string
        def dfs(u,parent):
            child=[dfs(w,u) for w in adj[u] if w!=parent]
            child.sort()
            return "("+"".join(child)+")"
        return dfs(root,-1)
    return min(rooted_code(r) for r in range(n))

def is_graceful(n, edges):
    """Exhaustive backtracking: exists bijection V->0..m with distinct edge diffs."""
    m=len(edges)
    if m==0: return True
    adj=[[] for _ in range(n)]
    for u,v in edges: adj[u].append(v); adj[v].append(u)
    # order vertices: descending degree, then BFS-ish (static) -- correctness ok
    order=sorted(range(n), key=lambda v:-len(adj[v]))
    pos={v:i for i,v in enumerate(order)}
    labels=[-1]*n
    used_label=[False]*(m+1)
    used_diff=[False]*(m+1)
    # neighbors already placed for vertex at step i
    def rec(i):
        if i==n: return True
        v=order[i]
        placed=[ (w,abs(labels[v]-labels[w]) if labels[v]!=-1 else None) for w in adj[v] if pos[w]<i]
        for lab in range(m+1):
            if used_label[lab]: continue
            ok=True; diffs=[]
            for w in adj[v]:
                if pos[w]<i:
                    d=abs(lab-labels[w])
                    if d==0 or used_diff[d]: ok=False; break
                    diffs.append(d)
            if not ok: continue
            labels[v]=lab; used_label[lab]=True
            for d in diffs: used_diff[d]=True
            if rec(i+1): return True
            labels[v]=-1; used_label[lab]=False
            for d in diffs: used_diff[d]=False
        return False
    return rec(0)

def distinct_trees(n):
    """Yield edge lists of all distinct (unlabeled) trees on n vertices."""
    seen=set()
    if n==2:
        yield [(0,1)]; return
    for seq in product(range(n), repeat=n-2):
        edges=prufer_to_edges(list(seq), n)
        c=canonical(n, edges)
        if c in seen: continue
        seen.add(c)
        yield edges

if __name__=="__main__":
    # unit tests
    assert is_graceful(2,[(0,1)]) is True
    path6=[(i,i+1) for i in range(5)]; assert is_graceful(6,path6)
    star=[(0,i) for i in range(1,6)]; assert is_graceful(6,star)
    print("unit tests passed (paths & stars graceful)")
    NMAX=int(sys.argv[1]) if len(sys.argv)>1 else 9
    KNOWN={1:1,2:1,3:1,4:2,5:3,6:6,7:11,8:23,9:47}
    for n in range(2, NMAX+1):
        t0=time.time(); cnt=0; bad=[]
        for edges in distinct_trees(n):
            cnt+=1
            if not is_graceful(n, edges): bad.append(edges)
        dt=time.time()-t0
        exp=KNOWN.get(n,'?')
        print(f"n={n}: distinct trees={cnt} (known {exp}); non-graceful={len(bad)}; "
              f"{dt:.2f}s")
        for e in bad[:5]: print("   NON-GRACEFUL:", e)
