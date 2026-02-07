L = [1,2,4]
for i in range(11):
    L.append(L[i] + L[i+1] + L[i+2])
for _ in range(int(input())):
    print(L[int(input())-1])