table = [True for _ in range(1000002)]
table[1] = False
for i in range(1,1001):
    if table[i]:
        for j in range(i*2,1000002,i):
            table[j] = False
primes = []
for i in range(1,1000001):
    if table[i]:
        primes.append(i)
N = int(input())
l = list(map(int, input().split()))
a = 1
for i in l:
    a *= i
if not a in primes:
    print("YES")
    print(len(list(set(l))))
    print(*list(set(l)))
else:
    print("NO")

