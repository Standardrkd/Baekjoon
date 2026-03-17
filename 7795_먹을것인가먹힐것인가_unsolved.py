# T = int(input())

N, M = map(int, input().split())
A = sorted(list(set(map(int, input().split()))))
B = sorted(list(set(map(int, input().split()))))

cnt = 0
L = 0
R = len(A) - 1
for i in range(max(N, M)):
    pass