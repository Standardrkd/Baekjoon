a = 1
b = 2
N = int(input())
for i in range(N-1):
    tmp = b
    b = (a+b)%15746
    a = tmp

print(a)