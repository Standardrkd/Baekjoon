T = int(input())
for _ in range(T):
    N = int(input())
    d = dict()
    for i in range(2,N+1):
        while N%i == 0:
            if not i in d:
                d[i] = 1
            else:
                d[i] += 1
            N //= i
    for k,v in d.items():
        print(k,v)