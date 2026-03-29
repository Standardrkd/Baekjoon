T = int(input())
for _ in range(T):
    N = int(input())
    checker = 0
    for i in range(2,1000000):
        if N%i == 0:
            print("NO")
            checker += 1
            break
    if checker == 0:
        print("YES")