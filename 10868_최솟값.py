import sys
input = sys.stdin.readline

N, M = map(int, input().split())
k = 0
size = 0

while 1:
    if 2**k >= N:
        size = 2**(k+1)
        break
    k += 1

segtree = [int(1e9)] * (size)
leaf_start = 2**k

for i in range(N):
    segtree[leaf_start+i] = int(input())

for i in range(size-1, 1, -1):
    if segtree[i] < segtree[i//2]:
        segtree[i//2] = segtree[i]

def segmin(s, e):
    m = int(1e9)
    s = leaf_start + s - 1
    e = leaf_start + e - 1

    while 1:
        if s > e:
            return m
        
        if s%2 == 1 and segtree[s] < m:
            m = segtree[s]
        s = (s+1)//2

        if e%2 == 0 and segtree[e] < m:
            m = segtree[e]
        e = (e-1)//2

for i in range(M):
    a, b = map(int, input().split())
    print(segmin(a,b) if a < b else segmin(b, a))



