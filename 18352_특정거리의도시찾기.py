# 특정 거리의 도시 찾기
import sys
input = sys.stdin.readline
from collections import deque
q = deque()
q2 = deque()


N, M, K, X = map(int, input().split())
visited = [False] * N
rel = [list() for _ in range(N)]

for i in range(M):
    x,y = map(int, input().split())
    rel[x-1].append(y)

def bfs():
    global cnt
    while q:
        x = q.popleft()
        for nx in rel[x-1]:
            if not visited[nx-1]:
                q2.append(nx)
                visited[nx-1] = True

q2.append(X)
visited[X-1] = True
for i in range(K):
    q = q2
    q2 = deque()
    bfs()

if len(q2) != 0:
    q2 = sorted(q2)
    for i in q2:
        print(i)
else:
    print(-1)


