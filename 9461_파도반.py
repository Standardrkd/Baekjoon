L = [1,1,1]

for i in range(100):
    L.append(L[i] + L[i+1])

for i in range(int(input())):
    print(L[int(input())-1])