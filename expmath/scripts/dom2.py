import subprocess, sys, time
sys.setrecursionlimit(100000)

def gen(n, args=None):
    a=["geng","-c"]+(args or [])+[str(n)]
    p=subprocess.Popen(a,stdout=subprocess.PIPE,bufsize=1<<20)
    for line in p.stdout: yield line.strip()
    p.wait()

def parse(line,n):
    bits=[]
    for ch in line[1:]:
        b=ch-63
        bits += [(b>>5)&1,(b>>4)&1,(b>>3)&1,(b>>2)&1,(b>>1)&1,b&1]
    N=[0]*n; deg=[0]*n; m=0; k=0
    for j in range(1,n):
        for i in range(j):
            if bits[k]:
                N[i]|=1<<j; N[j]|=1<<i; deg[i]+=1; deg[j]+=1; m+=1
            k+=1
    return N,deg,m

def annih(deg,m):
    ds=sorted(deg); s=0; a=0
    for d in ds:
        s+=d
        if s<=m: a+=1
        else: break
    return a

def has_cover(n,N,K,seen=None):
    full=(1<<n)-1
    if K<=0: return full==0
    if seen is None: seen=set()
    def rec(covered,k):
        if covered==full: return True
        if k==0: return False
        key=(covered,k)
        if key in seen: return False
        rem=full ^ covered
        # choose uncovered u with fewest candidate dominators
        best=None; bcnt=99; x=rem
        while x:
            lb=x&-x; u=lb.bit_length()-1; x^=lb
            cand=[]; y=N[u]
            while y:
                lb2=y&-y; v=lb2.bit_length()-1; y^=lb2
                cand.append(v)
            if len(cand)<bcnt: bcnt=len(cand); best=cand
        for v in best:
            if rec(covered|N[v],k-1): return True
        seen.add(key)
        return False
    return rec(0,K)

if __name__=="__main__":
    n=int(sys.argv[1])
    t0=time.time(); cnt=0; fails=[]; mins=10**9; tight=None; maxg=0
    for line in gen(n):
        cnt+=1
        N,deg,m=parse(line,n)
        a=annih(deg,m); K=a+1
        ok=has_cover(n,N,K)
        if not ok:
            fails.append((line.decode(),a)); print("FAIL",a,line.decode(),flush=True)
        if cnt%500000==0: print(f"n={n} {cnt} {time.time()-t0:.0f}s",flush=True)
    print(f"n={n} TOTAL {cnt} in {time.time()-t0:.1f}s fails={len(fails)}")
