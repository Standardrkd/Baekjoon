import sys
from collections import deque
input = sys.stdin.readline
q = deque()
N, M = map(int, input().split())

grid = [input().strip() for _ in range(N)]
dist = [[0]*M for _ in range(N)]

dxs = [-1,1,0,0]
dys = [0,0,-1,1]
dxys = [(-1,0), (1,0), (0,-1), (0,1)]

def bfs():
    while q:
        x, y = q.popleft()
        for dx, dy in dxys:
            nx = x + dx
            ny = y + dy
            if 0<=nx<N and 0<=ny<M and dist[nx][ny] == 0 and grid[nx][ny] != '1':
                q.append((nx,ny))
                dist[nx][ny] = dist[x][y] + 1

                if 3 <= int(grid[nx][ny]) <= 5:
                    print("TAK")
                    print(dist[nx][ny])
                    exit(0)
checker = 0
for i in range(N):
    for j in range(M):
        if grid[i][j] == '2':
            q.append((i,j))
            checker += 1
            break
    if checker == 1:
        break
bfs()
print("NIE")