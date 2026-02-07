from itertools import permutations
N ,M = map(int, input().split())
L = list(map(int, input().split()))
L.sort()

for i in permutations(L, M):
    print(*i)