from itertools import permutations
import sys
N, M = map(int, input().split())
result = []
for i in permutations(range(1,N+1), M):
    tmp = ""
    for j in i:
        tmp += str(j) + " "
    result.append(tmp)

for s in result:
    sys.stdout.write(s + "\n")
