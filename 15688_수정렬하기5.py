import sys
input = sys.stdin.readline
N = int(input())
L = []
for i in range(N):
    L.append(int(input()))
L.sort()
for item in L:
    print(item)