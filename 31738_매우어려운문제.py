N, M = map(int, input().split())
result = 1
tmp = -23498
if N >= M:
    print(0)
    exit(0)
else:
    for num in range(N,0,-1):
        result = (result*num)%M
print(result)


