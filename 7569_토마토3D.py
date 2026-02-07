# 토마토 3D

from collections import deque
q = deque()
q2 = deque()

M, N, H = map(int, input().split())
Box = []

cnt = 0
dxs = [-1,1,0,0,0,0]
dys = [0,0,-1,1,0,0]
dzs = [0,0,0,0,-1,1]

for _ in range(H):
    tmp = [list(map(int, input().split())) for _ in range(N)]
    Box.append(tmp)


def in_range(x,y,z):
    return 0<=x<H and 0<=y<N and 0<=z<M


def bfs():
    while q:
        x,y,z = q.popleft()
        for dx,dy,dz in zip(dxs, dys, dzs):
            nx = x + dx
            ny = y + dy
            nz = z + dz
            if in_range(nx, ny, nz) and Box[nx][ny][nz] == 0:
                Box[nx][ny][nz] = 1
                q2.append((nx, ny, nz))

for i in range(H):
    for j in range(N):
        for k in range(M):
            if Box[i][j][k] == 1:
                q2.append((i,j,k))

while q2:
    q = q2
    q2 = deque()
    bfs()
    cnt += 1

checker = 0
for i in range(H): # 토마토가 다 익을 수 있는지 체크
    for j in range(N):
        for k in range(M):
            if Box[i][j][k] == 0:
                checker += 1

if checker == 0:
    print(cnt-1)
else:
    print(-1)

