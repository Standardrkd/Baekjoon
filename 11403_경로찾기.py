from collections import deque

N = int(input())
q = deque()
grid = [list(map(int, input().split())) for _ in range(N)] # 입력 행렬
result = [[0] * N for _ in range(N)] # 결과 행렬
graph = [[] for _ in range(N+1)] # 1인덱스 사용
visited = [False] * (N+1)

for i in range(N): # 그래프로 만들기
    for j in range(N):
        if grid[i][j] == 1:
            graph[i].append(j)


def bfs():
    while q:
        x = q.popleft()
        for nx in graph[x]:
            if not visited[nx]:
                result[x][nx] = 1
                q.append(nx)
                visited[nx] = True



# 빨리 해!! ㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋ 벌써 망했다..! ㅠㅠㅜㅜㅠㅜㅠㅜㅠㅜㅠ 나빠 
# 