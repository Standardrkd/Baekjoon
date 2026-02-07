from collections import deque

N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]
grid = [[0]*N for _ in range(N)]
l = [[] for _ in range(N)]
q = deque()
visited = [False for _ in range(N)]

for i in range(N):
    for j in range(N):
        if graph[i][j] == 1:
            l[i].append(j)

def push(x):
    q.append(x)
    visited[x] = True

def bfs(f):
    while q:
        x = q.popleft()
        for nx in l[x]:
            if not visited[nx]:
                if nx == f:
                    return True
                else:
                    push(nx)
    return False

for i in range(N):
    for j in range(N):
        q = deque()
        push(i)
        if bfs(j):
            grid[i][j] = 1
for row in grid:
    print(*row)








# 빨리 해!! ㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋ 벌써 망했다..! ㅠㅠㅜㅜㅠㅜㅠㅜㅠㅜㅠ 나빠 
# 