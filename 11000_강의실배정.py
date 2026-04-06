import heapq
import sys
input = sys.stdin.readline

N = int(input())
L = []
q = []
for _ in range(N):
    s,e = map(int, input().split())
    L.append((s,e))

L.sort() # 시작 시간 기준 정렬
heapq.heappush(q, L[0])

for i in range(1,N):
    if L[i][0] >= q[0]: # 이번에 추가할 수업의 시작 시간이 q에서 가장 앞에 위치한 수업 끝 시간보다 늦거나 같다면?!
        heapq.heappop(q) # q에서 기존에 있던 수업 끝 시간을 빼고
        heapq.heappush(q, L[i][1]) # 새 수업의 끝 시간을 넣는다.
    else: # 이번에 추가할 수업의 시작시간이 가장 빨리 끝나는 수업보다 이전에 위치한다면? --> 강의실을 하나 더 빌려야겠지?
        heapq.heappush(q, L[i][1]) # 새 수업의 끝 시간을 넣는다.
    
print(len(q)) # q의 길이가 강의실의 개수임 왜냐하면 강의실의 추가 예약의 횟수가 q에 push만 했던 횟수와 같기 때문이지 