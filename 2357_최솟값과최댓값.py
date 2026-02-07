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

leaf_start = 2**k
l = []
min_segtree = [1e10] * size
max_segtree = [0] * size

for _ in range(N):
    l.append(int(input()))

for i in range(N):
    min_segtree[leaf_start+i] = l[i]
    max_segtree[leaf_start+i] = l[i]

for i in range(size-1,1,-1):
    if min_segtree[i] < min_segtree[i//2]:
        min_segtree[i//2] = min_segtree[i]
    if max_segtree[i] > max_segtree[i//2]:
        max_segtree[i//2] = max_segtree[i]

def segmin(s,e):
    r = 1e10
    s = s + leaf_start -1
    e = e + leaf_start -1
    while 1:
        if s > e:
            return r
        
        if s%2 == 1:
            if r > min_segtree[s]:
                r = min_segtree[s]
        s = (s+1)//2
        if e%2 == 0:
            if r > min_segtree[e]:
                r = min_segtree[e]
        e = (e-1)//2
def segmax(s,e):
    r = 0
    s = s + leaf_start -1
    e = e + leaf_start -1
    while 1:
        if s > e:
            return r
        
        if s%2 == 1:
            if r < max_segtree[s]:
                r = max_segtree[s]
        s = (s+1)//2
        if e%2 == 0:
            if r < max_segtree[e]:
                r = max_segtree[e]
        e = (e-1)//2

for _ in range(M):
    a, b = map(int, input().split())
    if a < b:
        print(segmin(a, b), segmax(a, b))
    else:
        print(segmin(b, a), segmax(b, a))