N,T=map(int,input().split())
L=list(map(int,input().split()))
y,g=[],[]
for i in range(1,T+1):
    if T%i==0:
        y.append(i)
for n in L:
    if T%n!=0:
        m = 1001
        for i in y:
            if abs(i-n)<m:
                m=abs(i-n)
        g.append(m)
print(sum(g))