import subprocess, math, sys, time
import numpy as np
EPS = 1e-6

def gen(n):
    p = subprocess.Popen(["geng","-c",str(n)], stdout=subprocess.PIPE, bufsize=1<<20)
    for line in p.stdout:
        yield line.strip()
    p.wait()

def parse(line, n):
    bits = []
    for ch in line[1:]:
        b = ch - 63
        bits += [(b>>5)&1,(b>>4)&1,(b>>3)&1,(b>>2)&1,(b>>1)&1,b&1]
    A = np.zeros((n,n), dtype=np.float64)
    deg = [0]*n
    edges = []
    k = 0
    for j in range(1,n):
        for i in range(j):
            if bits[k]:
                A[i,j] = A[j,i] = 1.0
                deg[i] += 1; deg[j] += 1
                edges.append((i,j))
            k += 1
    return A, deg, edges

def check(line, n):
    A, deg, edges = parse(line, n)
    m = len(edges)
    R = 0.0
    for i,j in edges:
        R += 1.0/math.sqrt(deg[i]*deg[j])
    eA = np.linalg.eigvalsh(A)
    L = -A.copy()
    for i in range(n):
        L[i,i] = deg[i]
    eL = np.linalg.eigvalsh(L)
    l1 = eA[-1]; l2 = eA[-2]
    mu1 = eL[-1]; mu2 = eL[-2]
    rk = int(np.count_nonzero(np.abs(eA) > 1e-7))
    out = {}
    out['C1'] = R - (l2 + 1.0)                 # #643 R >= l2+1
    out['C2'] = (mu1 - 2.0) - l2               # #20829 l2 <= mu1-2
    out['C3'] = rk*l1 - 2.0*R                  # #501193 2R <= rk*l1
    out['C4'] = (R + mu2) - l1                 # #112951 l1 <= R+mu2
    out['C5'] = 2.0*m - (mu2 + rk)             # #239534
    out['C6i'] = R*R - (m+1)/2.0
    out['C6ii'] = mu2*mu2 - (4.0*l2 + 1.0)
    out['C6iii'] = mu1*mu1 - (4.0*l2 + 8.0)
    out['C6iv1'] = R - (2.0/3.0*math.sqrt(m) + 1.0/3.0)
    out['C6iv2'] = R - (1.5*math.sqrt(rk) + 1.0 - 1.5*math.sqrt(2.0))
    return out

if __name__ == "__main__":
    n = int(sys.argv[1])
    t0 = time.time(); cnt = 0
    mins = {}; violations = {}; tight = {}
    for line in gen(n):
        cnt += 1
        d = check(line, n)
        for k,v in d.items():
            if k not in mins or v < mins[k]:
                mins[k] = v; tight[k] = line
            if v < -EPS:
                violations[k] = violations.get(k,0)+1
                print("VIOLATION", k, v, line.decode(), flush=True)
        if cnt % 200000 == 0:
            print(f"n={n} {cnt} graphs {time.time()-t0:.0f}s", flush=True)
    print(f"n={n} TOTAL {cnt} graphs in {time.time()-t0:.1f}s")
    for k in sorted(mins):
        print(f"  {k}: min slack {mins[k]:.6g}  tightest {tight[k].decode()}")
    print("violations:", violations)
