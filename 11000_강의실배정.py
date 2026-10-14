import heapq
import sys
input = sys.stdin.readline

N = int(input())
L = [] # 강의 시작시간과 종료시간을 튜플로 저장하는 리스트
q = []
for _ in range(N):
    s,e = map(int, input().split())
    L.append((s,e))

L.sort() # 시작시간이 빠른 순으로 정렬
heapq.heappush(q, L[0][1]) # priority queue에 강의가 끝나는 시간을 push

for i in range(1,N):
    # i번째 강의를 보는데, 그 강의가 시작하는 시간이 다른 가장 빠르게 끝나는 수업보다 늦게 시작함. 즉, 같은 강의실에 배정해도 됨같은 강의실에 배정해도 됨.
    if L[i][0] >= q[0]: 
        heapq.heappop(q)
        heapq.heappush(q, L[i][1]) 
    else: # 그 외는 겹치는 경우이기 때문에 그 강의를 priority queue에 넣음.
        heapq.heappush(q, L[i][1]) 
    
print(len(q)) # priority pueue의 Size를 반환하면 최소 강의실 개수가 나옴