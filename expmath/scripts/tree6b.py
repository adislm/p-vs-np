import subprocess, sys, time, math
import networkx as nx, numpy as np

def gen(n):
    p=subprocess.Popen(["gentreeg",str(n)],stdout=subprocess.PIPE,bufsize=1<<20)
    for line in p.stdout: yield line.strip()
    p.wait()

if __name__=="__main__":
    n0,n1=int(sys.argv[1]),int(sys.argv[2])
    keys=['6i','6ii','6iii','6iv1','6iv2']
    worst={k:(1e9,None) for k in keys}
    for n in range(n0,n1+1):
        t0=time.time(); cnt=0
        for line in gen(n):
            cnt+=1
            G=nx.from_sparse6_bytes(line)
            A=nx.to_numpy_array(G); m=G.number_of_edges()
            deg=np.array([d for _,d in G.degree()],dtype=float)
            eA=np.linalg.eigvalsh(A); L=np.diag(deg)-A; eL=np.linalg.eigvalsh(L)
            l2=eA[-2]; mu1,mu2=eL[-1],eL[-2]
            rk=int(np.count_nonzero(np.abs(eA)>1e-7))
            R=0.0
            for u,v in G.edges():
                R += 1.0/math.sqrt(G.degree(u)*G.degree(v))
            ch={'6i':R*R-(m+1)/2,'6ii':mu2*mu2-(4*l2+1),'6iii':mu1*mu1-(4*l2+8),
                '6iv1':R-(2/3*math.sqrt(m)+1/3),'6iv2':R-(1.5*math.sqrt(rk)+1-1.5*math.sqrt(2))}
            for k,v in ch.items():
                if v<worst[k][0]: worst[k]=(v,(line.decode(),n))
                if v<-1e-9: print('NEG',k,v,line.decode(),'n',n,flush=True)
        print(f'n={n} trees={cnt} time={time.time()-t0:.1f}s',flush=True)
    for k in keys: print(k,'min',worst[k])
