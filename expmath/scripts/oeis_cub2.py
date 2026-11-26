import sys
N=int(sys.argv[1])
def a(n):
    S=3*n*n;c=0;x=1
    while 3*x*x<=S:
        y=x
        while x*y+y*y+x*y<=S:
            num=S-x*y;den=x+y
            if num%den==0 and num//den>=y and x*y+y*(num//den)+x*(num//den)==S: c+=1
            y+=1
        x+=1
    return c
bad=[(n,a(n)) for n in range(1,N+1) if a(n)%2==0]
print('N',N,'even terms:',bad[:5],'count',len(bad))
