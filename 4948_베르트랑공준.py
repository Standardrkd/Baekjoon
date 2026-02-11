lis = [True] * 246913
lis[0], lis[1] = False, False
for i in range(2, 500):
    if lis[i]:
        for j in range(2*i, 246913, i):
            lis[j] = False

while True:
    cnt = 0
    n = int(input())
    if n == 0:
        break
    for i in range(n+1, n*2+1):
        if lis[i]:
            cnt += 1
    print(cnt)