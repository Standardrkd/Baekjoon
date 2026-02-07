from collections import deque

q = deque()
q2 = deque()
N = int(input())
line = list(map(int, input().split()))
jump_cnt = []
q2.append((0,line[0]))
cnt = 1

while q2:
    q = q2
    q2 = deque()
    q2_checker = set()
    while q:
        v,w = q.popleft() # v = 현재 인덱스, w = 현재 인덱스에서 갈 수 있는 최대 거리
        if w == 0:
            continue
        for i in range(1,w+1):
            if v + i == N:
                jump_cnt.append(cnt)
            elif v+i < N and not v+i in q2_checker:
                q2.append((v+i, line[v+i]))
                q2_checker.add(v+i)
    cnt += 1

if len(jump_cnt) == 0:
    print(-1)
else:
    print(min(jump_cnt))

# 아이아닝고 시간초과.....