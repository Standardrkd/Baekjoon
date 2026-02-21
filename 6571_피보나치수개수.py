while 1:
    a, b = map(int, input().split())
    if a == 0 and b == 0:
        break
    fib = [1,2]
    f = 0
    i = 0
    while f <= b:
        f = fib[i]+fib[i+1]
        fib.append(f)
        i += 1 
    i, j = 0,len(fib)-1
    while fib[i] < a:
        i += 1
    while fib[j] > b:
        j -= 1
    print(j-i+1)