from collections import deque
q = deque()
N, M = map(int, input().split())
banner = [list(map(int, input().split())) for _ in range(N)]
visited = [[False] * M] * N
dxs = [-1,1,0,0,-1,1,-1,1]
dys = [0,0,-1,1,1,-1,-1,1]

def in_range(x,y):
    return 0<=x<N and 0<=y<M

def bfs():
    while q:
        x, y = q.popleft()
        for dx,dy in zip(dxs, dys):
            nx = x + dx
            ny = y + dy
            if in_range(nx, ny) and banner[nx][ny] == 1:
                q.append((nx, ny))
                banner[nx][ny] = 0 
cnt = 0
for i in range(N):
    for j in range(M):
        if banner[i][j] == 1:
            q.append((i,j))
            bfs()
            cnt += 1

print(cnt)