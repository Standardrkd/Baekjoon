from collections import deque

q = deque()
M,N = map(int, input().split())
if M == 1 and N == 1:
    print("Yes")
    exit(0)
city = [list(map(int, input().split())) for _ in range(N)]
# visited = [[False]*M for _ in range(N)]
dxs, dys = [1,0], [0,1]

def bfs():
    while q:
        x,y = q.popleft()
        for dx, dy in zip(dxs, dys):
            nx = x + dx
            ny = y + dy
            if 0<=nx<N and 0<=ny<M and city[nx][ny] == 1:
                if nx == N - 1 and ny == M - 1:
                    print("Yes")
                    exit(0) 
                city[nx][ny] = 0
                q.append((nx,ny))

q.append((0,0))
bfs()
print("No")