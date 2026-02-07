N = int(input())
A = list(map(int, input().split()))
A.sort()
B = list(map(int, input().split()))
S = 0


for i in range(N): 
    S += B.pop(B.index(max(B))) * A[i]
print(S)

