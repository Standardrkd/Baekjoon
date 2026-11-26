import sys
input = sys.stdin.readline
while 1:
    N = int(input())
    if N == 0:
        break
    L = []
    for _ in range(N):
        L.append(int(input()))
    dp = [0 for _ in range(N)]
    dp[0] = L[0]
    for i in range(1, N):
        dp[i] = max(dp[i-1]+L[i], L[i])
    print(max(dp))
