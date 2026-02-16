import sys
input = sys.stdin.readline
N = int(input())
xs = []
ys = []
for i in range(N):
    x,y = map(int, input().split())
    xs.append(x)
    ys.append(y)
xs.append(xs[0])
ys.append(ys[0])

a = 0
b = 0
for i in range(N-1):
    a += xs[i] * ys[i+1]
    b += xs[i+1] * ys[i]

print(abs(a-b)/2)

# 오목각형, 볼록각형일 때 다름 ..