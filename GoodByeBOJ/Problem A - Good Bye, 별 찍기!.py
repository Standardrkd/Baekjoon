N = int(input())
for i in range(N):
    print(" "*(2*N-i-1)+"*"+" "*(i)+" "+" "*(N-i-1)+"*"+" "*(i+1)+" "*(i)+"*"+" "*(N-i-1))
for i in range(N):
    print(" "*(N-i-1)+"*"+" "*(i+N)+" "+" "*(i)+"*"+" "*(N-i)+" "*(N-i-1)+"*"+" "*(i))