N = int(input())
a = 1
b = 1
for i in range(N-1):
    tmp = b
    b = (a+b)%1000000007
    a = tmp%1000000007
print(a, N-2)