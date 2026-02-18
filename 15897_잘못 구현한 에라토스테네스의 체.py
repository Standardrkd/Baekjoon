import math
while 1:
    N = int(input())
    cnt = 0
    for i in range(1,N+1):
        cnt += math.ceil((N)/i)
    print(f"{N}일 때 : {cnt}")
