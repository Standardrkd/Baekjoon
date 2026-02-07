# N과M 10

from itertools import combinations

N, M = map(int, input().split())
L = list(map(int, input().split()))
L.sort()
stream = set()
for i in combinations(L, M):
    stream.add(i)

stream = list(stream)
stream.sort()

for i in stream:
    print(*i)