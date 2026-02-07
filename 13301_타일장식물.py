# 타일 장식물

L = [1,1]
N = int(input())
for i in range(80):
    L.append(L[i]+L[i+1])
print(L[N]*2 + L[N-1]*2)