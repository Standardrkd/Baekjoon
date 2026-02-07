N, M = map(int, input().split())
L = list(map(int,input().split()))
prefixL = []
tmp = 0
cnt = 0
for i in range(N):
    tmp += L[i]
    prefixL.append(tmp)

for i in range(N):
    for j in range(N-i):
        if prefixL[N-i-1] - prefixL[j] == M:
            cnt += 1
print(cnt+prefixL.count(M))