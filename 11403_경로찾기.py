from collections import deque
N = int(input())
q = deque()
g = [list(map(int, input().split())) for _ in range(N)]
R = [[0] * N for _ in range(N)]
G = [[] for _ in range(N+1)]
for i in range(N):
    for j in range(N):
        if g[i][j] == 1:
            G[i+1].append(j+1)
def bfs(i):
    while q:
        x = q.popleft()
        for j in G[x]:
            if not v[j]:
                R[i-1][j-1] = 1
                q.append(j)
                v[j] = True
for i in range(1,N+1):
    v = [False] * (N+1)
    q.append(i)
    bfs(i)
for r in R:
    print(*r)






# 빨리 해!! ㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋ 벌써 망했다..! ㅠㅠㅜㅜㅠㅜㅠㅜㅠㅜㅠ 나빠 
# 