import sys
input = sys.stdin.readline
N, M = map(int, input().split())
table = [[0]*(N+1)]

for _ in range(N):
    l = [0]
    pr = 0
    inp = list(map(int, input().split()))
    for i in inp:
        pr += i
        l.append(pr)
    table.append(l)

for _ in range(M):
    x1,y1,x2,y2 = map(int, input().split())
    result = 0
    for i in range(x1,x2+1):
        result += table[i][y2] - table[i][y1-1]
    print(result)

# 좀 더 DP적인 방안 필요 (시간 초과 남)