from collections import deque
q = deque()

M, N = map(int, input().split()) # 가로, 세로
grid = [list(input()) for _ in range(N)]
visited = [[False] * M for _ in range(N)]

dxs = [-1,1,0,0]
dys = [0,0,-1,1]

def in_range(x,y):
    return 0<=x<N and 0<=y<M

cnt = 0
def bfs(s):
    global cnt
    while q:
        x,y = q.popleft()
        for dx, dy in zip(dxs, dys):
            nx = x + dx
            ny = y + dy
            if in_range(nx,ny) and grid[nx][ny] == s and not visited[nx][ny]:
                q.append((nx,ny))
                visited[nx][ny] = True
                cnt += 1
    if cnt == 0:
        cnt += 1
W = 0
for i in range(N): # 흰색부터
    for j in range(M):
        if not visited[i][j] and grid[i][j] == "W":
            q.append((i,j))
            cnt = 0
            bfs("W")
            W += cnt**2
B = 0
for i in range(N): # 흰색부터
    for j in range(M):
        if not visited[i][j] and grid[i][j] == "B":
            q.append((i,j))
            cnt = 0
            bfs("B")
            B += cnt**2

print(W, B)
