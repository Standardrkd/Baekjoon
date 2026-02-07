N, M = map(int, input().split())
p1, p2 = 1001, 1001
for _ in range(M):
    a,b = map(int, input().split())
    if a < p1:
        p1 = a
    if b < p2:
        p2 = b

if p1/6 <= p2:
    if N%6 == 0:
        print((N//6)*p1)
    else:
        print(min((N//6+1)*p1, (N//6)*p1 + (N%6)*p2))
else:
    print(N*p2)