from collections import deque

q = deque()
q2 = deque()

F, S, G, U, D = map(int, input().split()) # F : max floor, S : now position, G : startlink

building = [i for i in range(F+1)]

def push(x):
    q2.append(x)
    building[x] = -1

def in_range(x):
    return 1<=x<=F

def bfs():
    global U, D, G, cnt
    while q:
        x = q.popleft()
        if x == G:
            print(cnt)
            exit(0)
        for nx in [x+U, x-D]:
            if in_range(nx) and building[nx] != -1:
                if nx == G:
                    print(cnt + 1)
                    exit(0)
                push(nx)

cnt = 0
push(S)
while q2:
    q = q2
    q2 = deque()
    bfs()
    cnt += 1

print("use the stairs")