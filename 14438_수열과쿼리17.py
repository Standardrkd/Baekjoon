import sys
input = sys.stdin.readline

N = int(input())
k = 0
size = 0

while 1:
    if 2**k >= N:
        size = 2**(k+1)
        break
    k += 1

leaf_start = 2**k
l = list(map(int, input().split()))
min_segtree = [1e10] * size



for i in range(N):
    min_segtree[leaf_start+i] = l[i]

for i in range(size-1,0,-1):
    if min_segtree[i] < min_segtree[i//2]:
        min_segtree[i//2] = min_segtree[i]

def update(index, value):
    global k
    index = index + leaf_start - 1
    min_segtree[index] = value
    for _ in range(k):
        if index%2 == 0: # 왼쪽 노드
            if min_segtree[index] < min_segtree[index+1]:
                min_segtree[index//2] = min_segtree[index]
                index//=2
            else:
                min_segtree[index//2] = min_segtree[index+1]
                index//=2

        else: # 오른쪽 노드
            if min_segtree[index] < min_segtree[index-1]:
                min_segtree[index//2] = min_segtree[index]
                index//=2
            else:
                min_segtree[index//2] = min_segtree[index-1]
                index//=2

def segmin(s,e):
    r = 1e11
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

M = int(input())
for _ in range(M):
    c, a, b = map(int, input().split())
    if c == 2:
        if a < b:
            print(segmin(a, b))
        else:
            print(segmin(b, a))
    elif c == 1:
        update(a,b)
