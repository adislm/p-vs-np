def sieve(N):
    s=bytearray([1])*(N+1); s[0:2]=b'\x00\x00'
    for i in range(2,int(N**.5)+1):
        if s[i]: s[i*i::i]=bytearray(len(s[i*i::i]))
    return s
S=sieve(4000)
def count(n):
    if n==0: return 1
    adj=[[j for j in range(n) if j!=i and S[(i+1)*(j+1)+1]] for i in range(n)]
    full=(1<<n)-1
    dp=[[0]*n for _ in range(1<<n)]
    for i in range(n): dp[1<<i][i]=1
    for mask in range(1<<n):
        row=dp[mask]
        for v in range(n):
            c=row[v]
            if c:
                for u in adj[v]:
                    if not (mask>>u)&1:
                        dp[mask|(1<<u)][u]+=c
    return sum(dp[full])
pub=[1,1,2,2,8,4,40,40,56,88,1288,1040,18200,17600,158194,173100,2218366]
got=[count(n) for n in range(len(pub))]
print('match 0..16:',got==pub)
print('got:',got)
print('pub:',pub)
