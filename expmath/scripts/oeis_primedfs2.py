import sys
from math import isqrt
def sieve(N):
    s=bytearray([1])*(N+1); s[0:2]=b'\x00\x00'
    for i in range(2,isqrt(N)+1):
        if s[i]: s[i*i::i]=bytearray(len(s[i*i::i]))
    return s
S=sieve(300000)
sys.setrecursionlimit(20000)
def find_path(n):
    O=list(range(1,n+1,2)); E=list(range(2,n+1,2))
    oi={v:i for i,v in enumerate(O)}; ei={v:i for i,v in enumerate(E)}
    adjO=[[e for e in E if S[o*e+1]] for o in O]
    adjE=[[o for o in O if S[o*e+1]] for e in E]
    def deg_e(i): return sum(1 for o in adjE[i])
    def deg_o(i): return sum(1 for e in adjO[i])
    def attempt(start, startOdd):
        # build pattern
        pat=[]; cur=startOdd
        for _ in range(n): pat.append(cur); cur=not cur
        if pat[-1]:  # odd n must end odd; even n pattern OK by construction
            pass
        budget=[3000000]
        def dfs(depth, cur, usedO, usedE):
            budget[0]-=1
            if budget[0]<0: raise TimeoutError
            if depth==n: return True
            if pat[depth]:  # need odd, cur is even
                for o in sorted(adjE[ei[cur]], key=lambda o: sum(1 for e in adjO[oi[o]] if not (usedE>>ei[e])&1)):
                    if not (usedO>>oi[o])&1:
                        if dfs(depth+1,o,usedO|(1<<oi[o]),usedE): return True
            else:
                for e in sorted(adjO[oi[cur]], key=lambda e: sum(1 for o in adjE[ei[e]] if not (usedO>>oi[o])&1)):
                    if not (usedE>>ei[e])&1:
                        if dfs(depth+1,e,usedO,usedE|(1<<ei[e])): return True
            return False
        if startOdd: return dfs(1,start,1<<oi[start],0)
        else: return dfs(1,start,0,1<<ei[start])
    starts=[]
    if n%2==1:
        starts=[(o,True) for o in O]      # must start odd
    else:
        starts=[(o,True) for o in O]+[(e,False) for e in E]
    for s,so in starts:
        try:
            if attempt(s,so): return True
        except TimeoutError:
            return None
    return False
out=[]
for n in range(17,121):
    r=find_path(n)
    out.append((n,r))
    if r is not True:
        print('NONRESULT',n,r); break
else:
    print('paths found for all n in 17..120')
print('count tested',len(out))
