# 촌 수 계산

from collections import deque
q = deque()
q2 = deque()

n = int(input())
p1, p2 = map(int, input().split())
m = int(input())
rel = [[] for _ in range(n)]
visited = [False] * n

for i in range(m):
    x,y = map(int, input().split())
    rel[x-1].append(y)
    rel[y-1].append(x)

chon = 0
checker = 0

def push(x):
    q2.append(x)
    visited[x-1] = True

def bfs():
    global chon,p2,checker
    while q:
        x = q.popleft()
        for nx in rel[x-1]:
            if nx == p2:
                checker += 1
                print(chon)
                exit(0)
            if not visited[nx-1]:
                push(nx)

push(p1)
while q2:
    q = q2
    q2 = deque()
    chon += 1
    bfs()

if checker == 0:
    print(-1)