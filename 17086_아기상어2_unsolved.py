from collections import deque
q = deque()
N, M = map(int,input().split())
space = [list(map(int, input().split())) for _ in range(N)]

dxs = [1,-1,0,0,1,1,-1,-1]
dys = [0,0,1,-1,-1,1,1,-1]

def in_range(x,y):
    return 0<=x<N and 0<=y<M
cnt = 0
def bfs():
    global cnt
    while q:
        x, y = q.popleft()
        for dx,dy in zip(dxs, dys):
            nx = x + dx
            ny = y + dy
            if in_range(nx, ny) and space[nx][ny] == 1:
                q.append((nx, ny))

# 으악 !! 갑자기 귀찮아짐!!!!!!!!!!!!!!!!!!