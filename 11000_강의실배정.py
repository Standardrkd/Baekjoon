import heapq
import sys
input = sys.stdin.readline

N = int(input())
L = []
q = []
for _ in range(N):
    s,e = map(int, input().split())
    L.append((s,e))

L.sort() 
heapq.heappush(q, L[0][1])

for i in range(1,N):
    if L[i][0] >= q[0]:
        heapq.heappop(q)
        heapq.heappush(q, L[i][1]) 
    else:
        heapq.heappush(q, L[i][1]) 
    
print(len(q)) 