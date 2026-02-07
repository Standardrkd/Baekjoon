import sys
input = sys.stdin.readline

N, M = map(int, input().split())
possible = [[True] * (N+1) for _ in range(N+1)]
cnt = 0

for i in range(M):
    a,b = map(int, input().split())
    possible[a][b] = False
    possible[b][a] = False

for i in range(1,N+1):
    for j in range(i+1, N+1):
        if not possible[i][j]:
            continue

        for k in range(j+1, N+1):
            if possible[i][k] and possible[j][k]:
                cnt += 1

print(cnt)
