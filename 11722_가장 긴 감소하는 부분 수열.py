N = int(input())
L = list(map(int, input().split()))
dp = [0 for _ in range(N)]
dp[0] = 1
for i in range(1, N):
    longest = 0
    for j in range(i):
        if L[j] > L[i] and longest < dp[j]:
            longest = dp[j]
    dp[i] = longest + 1        
print(max(dp))