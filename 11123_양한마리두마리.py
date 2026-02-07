# 양 한 마리, 양 두 마리..
from collections import deque
T = int(input())
dxs = [-1,1,0,0]
dys = [0,0,-1,1]

def in_range(x,y):
    return 0<=x<H and 0<=y<W

def bfs():
    global cnt
    checker = 0
    while q:
        x,y = q.popleft()
        checker += 1
        for dx, dy in zip(dxs, dys):
            nx = x + dx
            ny = y + dy
            if in_range(nx, ny) and not visited[nx][ny] and grid[nx][ny] == '#':
                q.append((nx,ny))
                visited[nx][ny] = True
    if checker != 0:
        cnt += 1
    

for _ in range(T):
    q = deque()
    cnt = 0

    H, W = map(int, input().split())
    visited = [[False]*W for _ in range(H)]
    grid = [list(input()) for _ in range(H)]

    for i in range(H):
        for j in range(W):
            if grid[i][j] == '#' and not visited[i][j]:
                q.append((i,j))
                visited[i][j] = True
                bfs()
    print(cnt)


    



