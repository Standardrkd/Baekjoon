S = input()
L = list()
for i in range(len(S)):
    L.append(S[i:])
L.sort()
for i in L:
    print(i)
