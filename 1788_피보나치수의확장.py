N = int(input())
fib = [0,1]
for i in range(abs(N)-1):
    fib.append((fib[i] + fib[i+1])%1000000000)

if N < 0:
    print(1 if N%2 == 1 else -1)
    print(fib[-N])
elif N == 0:
    print("0\n0")
else:
    print(1)
    print(fib[N])