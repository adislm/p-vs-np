import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import sympy as sp
import mpmath as mp
mp.mp.dps = 60
from spec import parse

def hp(g6, n, verbose=True):
    line = g6.encode() if isinstance(g6,str) else g6
    A0, deg, edges = parse(line, n)
    A = sp.Matrix([[int(A0[i,j]) for j in range(n)] for i in range(n)])
    L = sp.zeros(n,n)
    for i in range(n):
        L[i,i] = deg[i]
        for j in range(n):
            if i!=j: L[i,j] = -A[i,j]
    rank = A.rank()                      # exact integer rank
    eA = list(A.eigenvals().keys())      # algebraic
    # high precision numeric spectra
    Am = mp.matrix(n,n); Lm = mp.matrix(n,n)
    for i in range(n):
        for j in range(n):
            Am[i,j] = int(A[i,j]); Lm[i,j] = int(L[i,j])
    evA = sorted([mp.re(x) for x in mp.eigsy(Am)[0]], reverse=True)
    evL = sorted([mp.re(x) for x in mp.eigsy(Lm)[0]], reverse=True)
    splus = sum(x*x for x in evA if x>0)
    sminus = sum(x*x for x in evA if x<0)
    R = mp.mpf(0)
    for i,j in edges:
        R += 1/mp.sqrt(mp.mpf(deg[i])*mp.mpf(deg[j]))
    l1,l2 = evA[0],evA[1]; mu1,mu2 = evL[0],evL[1]
    m=len(edges)
    checks = {
     'C1 #643  R-(l2+1)': R-(l2+1),
     'C2 #20829 (mu1-2)-l2': (mu1-2)-l2,
     'C3 #501193 rk*l1-2R': rank*l1-2*R,
     'C4 #112951 (R+mu2)-l1': (R+mu2)-l1,
     'C5 #239534 2m-(mu2+rk)': 2*m-(mu2+rank),
     'C6i R^2-(m+1)/2': R*R-mp.mpf(m+1)/2,
     'C6ii mu2^2-(4l2+1)': mu2**2-(4*l2+1),
     'C6iii mu1^2-(4l2+8)': mu1**2-(4*l2+8),
    }
    if verbose:
        print('graph6',g6,'n',n,'m',m,'edges',edges,'deg',deg)
        print('rank(A) exact =',rank)
        print('l1,l2 =',mp.nstr(l1,30),mp.nstr(l2,30))
        print('mu1,mu2 =',mp.nstr(mu1,30),mp.nstr(mu2,30))
        print('R =',mp.nstr(R,30))
        print('s+ =',mp.nstr(splus,30),' s- =',mp.nstr(sminus,30),' s+-n =',mp.nstr(splus-n,20))
        for k,v in checks.items(): print(f'  {k:28s} = {mp.nstr(v,20)}')
        print('violations:', [k for k,v in checks.items() if v < -mp.mpf(10)**-25])
    return checks

if __name__=='__main__':
    hp(sys.argv[1], int(sys.argv[2]))
