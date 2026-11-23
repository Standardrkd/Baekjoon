N, M = map(int, input().split())
mat = []
target = []
count = 0
for i in range(N):
    l = list(map(int, list(input())))
    mat.append(l)

for i in range(N):
    l = list(map(int, list(input())))
    target.append(l)

for i in range(N-2):
    for j in range(M-2):
        if mat[i][j] != target[i][j]:
            mat[i][j] = 0 if mat[i][j] == 1 else 1
            mat[i][j+1] = 0 if mat[i][j+1] == 1 else 1
            mat[i][j+2] = 0 if mat[i][j+2] == 1 else 1
            mat[i+1][j] = 0 if mat[i+1][j] == 1 else 1
            mat[i+1][j+1] = 0 if mat[i+1][j+1] == 1 else 1
            mat[i+1][j+2] = 0 if mat[i+1][j+2] == 1 else 1
            mat[i+2][j] = 0 if mat[i+2][j] == 1 else 1
            mat[i+2][j+1] = 0 if mat[i+2][j+1] == 1 else 1
            mat[i+2][j+2] = 0 if mat[i+2][j+2] == 1 else 1
            count += 1

for i in range(N):
    for j in range(M):
        if mat[i][j] != target[i][j]:
            print(-1)
            exit(0)
print(count)
