from itertools import permutations
N ,M = map(int, input().split())
L = list(map(int, input().split()))
result = set()
for i in permutations(L, M):
    result.add(i)

result = list(result)
result.sort()
for i in result:
    print(*i)   