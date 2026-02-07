import math
def percent(X,Y):
    return int(math.floor((Y/X)*100))
X, Y = map(int, input().split())

if X == Y:
    print(-1)
    exit(0)

init = percent(X,Y)
cnt = X // 2
while True:
    print(percent(X+cnt, Y+cnt))
    if init == percent(X+cnt, Y+cnt):
        while init == percent(X+cnt, Y+cnt):
            cnt += 1
        print(cnt)
        break

    cnt = cnt//2

