from itertools import permutations

def subsum(perm):
    global N
    s = 0
    for i in range(N-1):
        s += abs(L[perm[i]] - L[perm[i+1]])
    return s

N = int(input())
L = list(map(int, input().split()))
results = []

for perm in permutations([i for i in range(N)], N):
    results.append(subsum(perm))
print(max(results))
