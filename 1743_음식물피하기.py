from collections import deque

N, M, K = map(int, input().split())
grid = [["."] * M for _ in range(N)]
cnt = 0
q = deque()
results = []

dxs = [-1,1,0,0]
dys = [0,0,-1,1]

for i in range(K): # 음식물 떨어뜨리기
    a,b = map(int, input().split())
    grid[a-1][b-1] = "#"

def in_range(x,y):
    return 0<=x<N and 0<=y<M

def bfs():
    global cnt
    while q:
        x,y = q.popleft()
        for dx, dy in zip(dxs, dys):
            nx = x + dx
            ny = y + dy
            if in_range(nx,ny) and grid[nx][ny] == "#":
                q.append((nx,ny))
                grid[nx][ny] = "."
                cnt += 1

for i in range(N):
    for j in range(M):
        if grid[i][j] == "#":
            cnt = 0
            q.append((i,j))
            bfs()
            results.append(cnt)

print(max(results))