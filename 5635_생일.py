L = list()

for i in range(int(input())):
    name, d, m, y = map(str, input().split())
    L.append((int(y),int(m),int(d),name))

L.sort()
print(L[-1][3])
print(L[0][3])