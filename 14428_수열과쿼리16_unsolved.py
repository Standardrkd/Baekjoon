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

l = list(map(int, input().split()))

leaf_start = 2**k
min_segtree = [[1,1e9]] * size 

for i in range(N):
    min_segtree[leaf_start+i] = [i+1,l[i]] # 인덱스와 값을 한 번에 저장하기 위해 이차원 리스트로 만들기

for i in range(size-1,1,-1):
    if min_segtree[i][1] < min_segtree[i//2][1]:
        min_segtree[i//2] = min_segtree[i]

def update(index, value):
    global k
    index = index + leaf_start - 1
    min_segtree[index][1] = value
    for _ in range(k):
        if index%2 == 0: # 왼쪽 노드
            if min_segtree[index][1] < min_segtree[index+1][1]:
                min_segtree[index//2] = [min_segtree[index][0], min_segtree[index][1]]
                index//=2

        else: # 오른쪽 노드
            if min_segtree[index][1] < min_segtree[index-1][1]:
                min_segtree[index//2] = [min_segtree[index-1][0],min_segtree[index-1][0]]
                index//=2


def segmin(s,e):
    r = 1e10
    min_index = 1e8
    s = s + leaf_start -1
    e = e + leaf_start -1
    while 1:
        if s > e:
            return min_index
        
        if s%2 == 1:
            if r > min_segtree[s][1]:
                r = min_segtree[s][1]
                min_index = min_segtree[s][0]
        s = (s+1)//2

        if e%2 == 0:
            if r > min_segtree[e][1]:
                r = min_segtree[e][1]
                min_index = min_segtree[e][0]
        e = (e-1)//2


# 5 4 3 3 3 이면 3을 출력해야하는데 5가 나옴;; index도 최소화하는 방법 고안


M = int(input())
for _ in range(M):
    c, a, b = map(int, input().split())
    if c == 2:
        if a < b:
            print(segmin(a,b))
        else:
            print(segmin(b,a))
    elif c == 1:
        update(a,b)

    
print(min_segtree)
