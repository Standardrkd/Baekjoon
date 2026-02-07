# BFS 배우기

from collections import deque
import sys
input = sys.stdin.readline
q = deque()


N, M, R = map(int, input().split())
graph = [[] for _ in range(N)]
visited = [False] * N
L = [0 for _ in range(N)]
index = 1

for i in range(M):
    a, b = map(int, input().split())
    graph[a-1].append(b)
    graph[b-1].append(a)

def push(x):
    global index    
    q.append(x)
    visited[x-1] = True
    L[x-1] = index
    index += 1

def bfs():
    while q:
        x = q.popleft()
        for nx in graph[x-1]:
            if not visited[nx-1]:
                push(nx)

for i in range(N):
    graph[i].sort()

push(R)
bfs()

for i in L:
    print(i)