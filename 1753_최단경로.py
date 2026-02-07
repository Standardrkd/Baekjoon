import heapq
import sys

input = sys.stdin.readline
N ,M = map(int, input().split())
k = int(input())
INF = 1e8
distance = [INF] * (N+1)
graph = [[] for _ in range(N+1)]

for i in range(M):
    u, v, w = map(int, input().split())
    graph[u].append((v,w))

def dijkstra(start):
    q = []
    distance[start] = 0
    heapq.heappush(q, (distance[start], start))

    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue
            
        for i in graph[now]:
            if dist + i[1] < distance[i[0]]:
                distance[i[0]] = dist + i[1]
                heapq.heappush(q, (dist+i[1], i[0]))

dijkstra(k)
for i in range(1,len(distance)):
    if distance[i] == 1e8:
        print("INF")
    else:
        print(distance[i])

        ####????????????????????????????????????????