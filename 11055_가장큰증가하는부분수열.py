N  = int(input())
A = list(map(int,input().split()))
size_list = [0] * N

for i in range(N):
    tmp = 0
    for j in range(i):
        if A[i] > A[j] and tmp < size_list[j]:
            tmp = size_list[j]
    size_list[i] = tmp+A[i] 

print(max(size_list))