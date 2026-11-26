# WA
import sys
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    N = int(input())
    tasks = []
    flag = True
    for i in range(N):
        tasks.append(tuple(map(int, input().split())))
    tasks.sort(key=lambda x:x[3])
    deadline = tasks[-1][3]
    a, b, c, p = 0,0,0,0
    for ai, bi, ci, pi in tasks:
        need = max(ai-a + bi-b + ci-c, 0)
        if need < pi:
            p += need + 1 # 훈련비용 + 해결비용(1)
            a = max(a, ai)
            b = max(b, bi)
            c = max(c, ci)
        else:
            flag = False
            break
        if p >= deadline:
            flag = False
            break
            
    if flag:
        print("YES")
    else:
        print("NO")
    