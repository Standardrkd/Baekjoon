N, M = map(int, input().split())
grid = [list(input()) for _ in range(N)]
L = 0
R = 0
l = 0

index = 0
for i in range(N):
    cnt = 0
    if "#" in grid[i]:
        L = grid[i].index("#")
        for j in range(M-1,1,-1):
            if grid[i][j] == "#":
                R = j
                break
        index = i
        if R-L+1 == grid[i].count("#"):
            l = R-L+1
        else:
            print("UP")
            exit()
        break

for i in range(index+1,index+l):
    if grid[i][L] != "#":
        print("LEFT")
        exit()
    if grid[i][R] != "#":
        print("RIGHT")
        exit()

print("DOWN")            