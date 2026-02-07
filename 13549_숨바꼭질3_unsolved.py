import heapq

N ,M = map(int, input().split())
line = [i for i in range(200002)]
distance = [1e8] * (100001)
def dijkstra():
    q = []
    

    while q:
        dist, now = heapq.heappop(q)


# d아 뇌정지;; 다익스트라 너무 어렵다