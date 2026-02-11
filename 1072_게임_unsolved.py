import math
def percent(X,Y):
    return int(math.floor((Y/X)*100))
X, Y = map(int, input().split())

if X == Y:
    print(-1)
    exit(0)

init = percent(X,Y) # 처음 확률 (소숫점은 버림)
cnt = X // 2
while True:
    # print(percent(X+cnt, Y+cnt))
    if init == percent(X+cnt, Y+cnt): # 종료 조건
        while init == percent(X+cnt, Y+cnt):
            cnt += 1
        print(cnt)
        break

    cnt = cnt//2

# 27133 27002 -> 시간 초과 (X, Y가 같은 경우에만 불가능 한 것이 아님)