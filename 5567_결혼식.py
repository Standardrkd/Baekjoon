# 결혼식
from collections import deque
q = deque()
q2 = deque()
cnt = 0
people = 0
n = int(input())
m = int(input())
visited = [False] * n
rel = [[] for _ in range(n)]

for i in range(m):
    x,y = map(int, input().split())
    rel[x-1].append(y)
    rel[y-1].append(x)

def bfs():
    global people
    while q:
        x = q.popleft()
        for nx in rel[x-1]:
            if not visited[nx-1]:
                q2.append(nx)
                visited[nx-1] = True
                people += 1

q.append(1)
visited[0] = True
while True:
    if cnt == 2:
        break
    bfs()
    q = q2
    q2 = deque()
    cnt += 1
print(people)