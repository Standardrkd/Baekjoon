# 숨바꼭질
from collections import deque
q = deque()
q2 = deque()
dist = 0

N, K = map(int, input().split())
L = [i+1 for i in range(200000)] # 수직선 

def in_range(x):
    return 0<=x<199999

def push(x):
    q2.append(x)
    L[x-1] = -1

def bfs():
    global K, dist
    while q:
        x = q.popleft()
        for n in [x-1, x+1, 2*x]:
            if in_range(n) and L[n-1] != -1:
                push(n)
                if n == K:
                    print(dist+1)
                    exit(0)

if N == K:
    print(0)
else:
    push(N)
    while q2:
        q = q2
        q2 = deque()

        bfs()
        dist += 1
