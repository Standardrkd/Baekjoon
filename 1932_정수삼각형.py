N = int(input())
table = [[0] * (i+1) for i in range(N)]
tri = []
for i in range(N):
    tmp = list(map(int, input().split()))
    tri.append(tmp)
table[0][0] = tri[0][0]
for i in range(N-1):
    for j in range(i+1):
        if table[i+1][j] < table[i][j] + tri[i+1][j]:
            table[i+1][j] = table[i][j] + tri[i+1][j]

        if table[i+1][j+1] < table[i][j] + tri[i+1][j+1]:
            table[i+1][j+1] = table[i][j] + tri[i+1][j+1]

print(max(table[N-1]))