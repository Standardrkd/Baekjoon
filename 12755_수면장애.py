import time
N = int(input())
a = []
b = 1
for i in range(1,N+1):
    for j in str(i):
        print(j, b)
        b += 1