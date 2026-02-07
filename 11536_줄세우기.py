N = int(input())
L = []
for i in range(N):
    L.append(input())

L_inc = sorted(L)
L_dec = sorted(L, reverse=True)
if L == L_dec:
    print("DECREASING")
elif L == L_inc:
    print("INCREASING")
else:
    print("NEITHER")