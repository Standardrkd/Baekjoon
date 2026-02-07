# 쉽게 푸는 문제  1,2,2,3,3,3,4,4,4,4,5.....

L = []

for i in range(500):
    for j in range(i+1):
        L.append(i+1)
a,b = map(int, input().split())
print(L)
print(sum(L[a-1:b]))