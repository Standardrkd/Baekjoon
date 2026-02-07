from collections import deque
q = deque()
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
rel = [[] for _ in range(N)]
visited = [False] * N
cnt_list = []

for i in range(M):
    x,y = map(int, input().split())
    rel[y-1].append(x)


def bfs():
    global cnt
    while q:
        x = q.popleft()
        for nx in rel[x-1]:
            if not visited[nx-1]:
                q.append(nx)
                visited[nx-1] = True
                cnt += 1



for i in range(N):
    cnt = 0
    visited = [False] * N
    q = deque()

    q.append(i+1)
    bfs()
    cnt_list.append(cnt)

m = max(cnt_list)
for i in range(N):
    if m == cnt_list[i]:
        print(i+1, end=' ')