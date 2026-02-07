N = int(input())
L = list(map(int, input().split()))
prefix_L = []
prefix_sum = 0
result = 0
L.sort()
for i in L: # make prefix sum list
    prefix_sum += i
    prefix_L.append(prefix_sum)

for i in range(N-1):
    result += abs((prefix_L[N-1]-prefix_L[i])-L[i]*(N-1-i))

print(result*2)