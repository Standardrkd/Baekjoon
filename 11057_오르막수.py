N = int(input())
result = []

tmp = [1,1,1,1,1,1,1,1,1,1]

for i in range(N):
    tmp2 = []
    prefix = 0
    for j in tmp:
        prefix += j
        tmp2.append(prefix)
    result.append(prefix)
    tmp = tmp2

print(result[N-1]%10007)