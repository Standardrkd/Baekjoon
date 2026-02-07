import sys, heapq
input = sys.stdin.readline

N = int(input())
M = int(input())
INF = 1e8
graph = [[] for _ in range(N+1)]
distance = [INF] * (N+1)

for _ in range(M): 
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
                heapq.heappush(q, (distance[i[0]], i[0]))

s, a = map(int, input().split())
dijkstra(s)
print(distance[a])

    
