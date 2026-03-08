from collections import deque

N = int(input())

grid = [list(map(int, input().split())) for _ in range(N)]
graph = [[] for _ in range(N)]

for i in range(N): # 그래프로 만들기
    for j in range(N):
        if grid[i][j] == 1:
            graph[i].append(j)








# 빨리 해!! ㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋ 벌써 망했다..! ㅠㅠㅜㅜㅠㅜㅠㅜㅠㅜㅠ 나빠 
# 