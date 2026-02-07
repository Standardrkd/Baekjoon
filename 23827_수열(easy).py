result = 0

N = int(input())
L = list(map(int, input().split()))


prefix_sum = 0    
for i in range(N-1):
    prefix_sum += L[N-i-1]
    result += prefix_sum * L[N-i-2]
    result %= 1000000007

print(result)

