import sys
input = sys.stdin.readline  
N = int(input())
L = []
result = []
for i in range(N):
    L.append(int(input()))
L.sort()

for i in range(N):
    result.append(L[i]*(N-i))
print(max(result))