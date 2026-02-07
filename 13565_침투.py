# 침투
import sys
sys.setrecursionlimit(1000000)


N, M = map(int, input().split())

dxs = [-1,1,0,0]
dys = [0,0,-1,1]
visited = [[False] * M for _ in range(N)]
grid = [list(input()) for _ in range(N)]

def in_range(x,y):
    return 0<=x<N and 0<=y<M

def dfs(x,y):
    for dx, dy in zip(dxs, dys):
        nx = x + dx
        ny = y + dy
        if in_range(nx, ny) and not visited[nx][ny] and grid[nx][ny] == '0':
            if nx == N-1:
                print("YES")
                exit(0)
            visited[nx][ny] = True
            dfs(nx,ny)


for i in range(M):
    if grid[0][i] == '0':
        dfs(0,i)

print("NO")