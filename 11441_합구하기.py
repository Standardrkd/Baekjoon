import sys
input = sys.stdin.readline
N = int(input())
L = list(map(int, input().split()))
prefix_list = [0]
prefix = 0

for i in L:
    prefix += i
    prefix_list.append(prefix)

M = int(input())
for i in range(M):
    a, b = map(int, input().split())
    print(prefix_list[b] - prefix_list[a-1] if a < b else prefix_list[a] - prefix_list[b-1])