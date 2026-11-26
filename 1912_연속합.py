N = int(input())
L = list(map(int, input().split()))
dp = [0 for _ in range(N)]
dp[0] = L[0]
for i in range(1, N):
    dp[i] = max(dp[i-1]+L[i], L[i])
print(max(dp))