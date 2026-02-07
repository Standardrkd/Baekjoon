L = [1,2]
N = int(input())
for i in range(1000):
    L.append(L[i]+L[i+1])
print(L[N-1]%10007)