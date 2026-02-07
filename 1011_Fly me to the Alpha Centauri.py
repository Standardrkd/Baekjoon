T = int(input())
for _ in range(T):
    a,b = map(int, input().split())
    N = b-a
    dist = 0
    i = 1
    d = 1
    while 1:
        if dist >= N:
            break
        dist += d
        if i%2 == 0:
            d += 1
        i+= 1
    print(i-1)