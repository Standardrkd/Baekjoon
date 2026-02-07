from collections import deque

q = deque()
q2 = deque()
A, B = map(int, input().split())

visited = set()

def push(x):
    q2.append(x)
    visited.add(x)

dist = 0
def bfs():
    while q:
        x = q.popleft()
        for nx in [int(str(x)+'1'), x*2]:
            if not nx in visited and nx <= B:
                if nx == B:
                    print(dist + 2)
                    exit(0)
                push(nx)
    if int(str(x)+'1') > B and x*2 > B:
        print(-1)
        exit(0)

push(A)
while  q2:
    q = q2
    q2 = deque()
    bfs()
    dist += 1