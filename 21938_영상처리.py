from collections import deque
q = deque()
N, M = map(int, input().split())
display = []



for i in range(N):
    tmp = []
    line = deque(map(int, input().split()))
    for j in range(M):
        pixel_mean = 0
        for k in range(3):
            pixel_mean += line.popleft()
        tmp.append(pixel_mean/3)
    display.append(tmp)

T = int(input())
for i in range(N):
    for j in range(M):
        if display[i][j] >= T:
            display[i][j] = 1
        else:
            display[i][j] = 0

dxs = [-1,1,0,0]
dys = [0,0,-1,1]

def in_range(x,y):
    return 0<=x<N and 0<=y<M
cnt = 0
# checker = 0
def bfs():
    # global checker
    # checker = 0
    while q:
        x,y = q.popleft()
        for dx, dy in zip(dxs, dys):
            nx = x + dx
            ny = y + dy
            if in_range(nx,ny) and display[nx][ny] == 1:
                q.append((nx,ny))
                display[nx][ny] = 0
                # checker += 1

for i in range(N):
    for j in range(M):
        if display[i][j]  == 1:
            q.append((i,j))
            cnt += 1
            bfs()

print(cnt)