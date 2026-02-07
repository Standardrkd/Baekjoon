# 30
N = list(map(int, list(input())))
N.sort(reverse=True)

if 0 in N and sum(N)%3 == 0:
    for i in N:
        print(i, end='')
else:
    print(-1)

