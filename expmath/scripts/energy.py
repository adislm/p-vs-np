import subprocess, sys, time
import numpy as np

def gen(n):
    p=subprocess.Popen(["geng","-c",str(n)],stdout=subprocess.PIPE,bufsize=1<<20)
    for line in p.stdout: yield line.strip()
    p.wait()

def parse(line,n):
    bits=[]
    for ch in line[1:]:
        b=ch-63
        bits += [(b>>5)&1,(b>>4)&1,(b>>3)&1,(b>>2)&1,(b>>1)&1,b&1]
    A=np.zeros((n,n)); deg=[0]*n; m=0; k=0
    for j in range(1,n):
        for i in range(j):
            if bits[k]: A[i,j]=A[j,i]=1.0; deg[i]+=1; deg[j]+=1; m+=1
            k+=1
    return A,deg,m

if __name__=="__main__":
    n0=int(sys.argv[1]); n1=int(sys.argv[2])
    for n in range(n0,n1+1):
        t0=time.time(); cnt=0; viol=[]; mins=1e9; tight=None; tested=0
        for line in gen(n):
            cnt+=1
            A,deg,m=parse(line,n)
            if m < n+1: continue
            tested+=1
            e=np.linalg.eigvalsh(A)
            sp=float(np.sum(np.square(e[e>0])))
            slack=sp-n
            if slack<mins: mins=slack; tight=line
            if slack < -1e-9:
                viol.append((line.decode(),m,sp)); print("VIOLATION n=%d m=%d s+=%.10f %s"%(n,m,sp,line.decode()),flush=True)
            if cnt%500000==0: print(f"  n={n} scanned {cnt}",flush=True)
        print(f"n={n}: connected={cnt} with m>=n+1 tested={tested} violations={len(viol)} minslack={mins:.6g} tight={tight.decode() if tight else None} time={time.time()-t0:.1f}s",flush=True)
