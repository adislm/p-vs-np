#!/usr/bin/env python3
"""Independent verifier for certificates produced by the landmark-problem sweeps.

Every claim in this repo that rests on a finite object gets checked here, by code
written separately from whatever produced the object. Usage:

    verify_cert.py schur     <colouring>        e.g. 0110220220110
    verify_cert.py vdw       <colouring> <k>    progression length k
    verify_cert.py ramsey    <n> <s> <r> <file> edges "u v" per line, 0-indexed

Exit status is 0 when the certificate verifies, 1 otherwise. A malformed
certificate is a failure, not a pass.
"""
import sys


def fail(msg):
    print(f"FAIL: {msg}")
    sys.exit(1)


def ok(msg):
    print(f"OK: {msg}")
    sys.exit(0)


def check_schur(colouring):
    """A colouring of [1,n] is Schur-valid when no monochromatic x + y = z."""
    if not colouring or not all(c.isdigit() for c in colouring):
        fail("schur colouring must be a string of digits")
    col = [int(c) for c in colouring]
    n = len(col)
    for z in range(2, n + 1):
        for x in range(1, z):
            y = z - x
            if x <= n and y >= 1 and col[x - 1] == col[y - 1] == col[z - 1]:
                fail(f"monochromatic {x}+{y}={z} in colour {col[z - 1]}")
    colours = sorted(set(col))
    ok(f"Schur-valid on [1,{n}] with {len(colours)} colours {colours}")


def check_vdw(colouring, k):
    """No monochromatic arithmetic progression of length k."""
    col = [int(c) for c in colouring]
    n = len(col)
    k = int(k)
    if k < 3:
        fail("k must be at least 3")
    for start in range(n):
        for d in range(1, n):
            if start + (k - 1) * d >= n:
                break
            idx = [start + i * d for i in range(k)]
            if len({col[i] for i in idx}) == 1:
                fail(f"monochromatic AP length {k} at {idx} colour {col[idx[0]]}")
    ok(f"no monochromatic AP of length {k} on [1,{n}]")


def check_ramsey(n, s, r, path):
    """Graph on n vertices with no K_s and no independent set of size r."""
    n, s, r = int(n), int(s), int(r)
    adj = [[False] * n for _ in range(n)]
    with open(path) as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            parts = line.split()
            if len(parts) != 2:
                fail(f"bad edge line: {line!r}")
            u, v = int(parts[0]), int(parts[1])
            if not (0 <= u < n and 0 <= v < n) or u == v:
                fail(f"edge out of range or loop: {u} {v}")
            adj[u][v] = adj[v][u] = True

    def has_clique(size):
        from itertools import combinations
        for cand in combinations(range(n), size):
            if all(adj[a][b] for a, b in combinations(cand, 2)):
                return cand
        return None

    def has_indep(size):
        from itertools import combinations
        for cand in combinations(range(n), size):
            if not any(adj[a][b] for a, b in combinations(cand, 2)):
                return cand
        return None

    cl = has_clique(s)
    if cl:
        fail(f"contains K_{s} on {cl}")
    ind = has_indep(r)
    if ind:
        fail(f"contains independent set of size {r} on {ind}")
    edges = sum(1 for u in range(n) for v in range(u + 1, n) if adj[u][v])
    ok(f"{n} vertices, {edges} edges, no K_{s}, no independent {r}-set")


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)
    mode = sys.argv[1]
    if mode == "schur":
        check_schur(sys.argv[2])
    elif mode == "vdw":
        check_vdw(sys.argv[2], sys.argv[3])
    elif mode == "ramsey":
        check_ramsey(sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5])
    else:
        print(__doc__)
        sys.exit(1)


if __name__ == "__main__":
    main()
