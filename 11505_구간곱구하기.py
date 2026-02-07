import sys
input = sys.stdin.readline
mod = 1000000007
N,M,K = map(int,input().split())
size = 0
k = 0
while True: # k구하기
    if 2**k >= N:
        size = (2**k)*2
        break
    k += 1

segtree = [1] * size
l = []
for i in range(N):
    l.append(int(input()))

leaf_start = 2**k
for i in range(N):# 리프에 추가
    segtree[i+leaf_start] = l[i]

for i in range(size-1,1,-1): # 부모로 올라가며 곱하기
    segtree[i//2] = (segtree[i//2] * segtree[i]) % mod

def segmultiple(s,e):
    result = 1
    # 트리 인덱스에 맞게 전처리
    s = s + leaf_start -1 
    e = e + leaf_start -1

    while True:
        if s > e:
            return result%mod

        if s%2 == 1: # 독립 선택을 해야하는 경우
            result = (result*segtree[s])
        s = (s+1)//2 # 부모로 올라가기
        if e%2 == 0:
            result = (result*segtree[e])
        e = (e-1)//2 # 부모로 올라가기

def update(index,value):
    global k
    # tmp = segtree[index] # 바뀌기 전 값
    index = index + leaf_start -1
    segtree[index] = value

    for i in range(k+1):
        if index%2 == 0: # left
            segtree[index//2] = (segtree[index] * segtree[index+1]) % mod
            index = index//2
        else: # right
            segtree[index//2] = (segtree[index] * segtree[index-1]) % mod
            index = index//2
        # 나머지 계산을 할 정도로 커지면 저장된 값이 나중에 계산될 때 정확한 결과가 안 나올 수도 있음


for i in range(K+M):
    a,b,c = map(int, input().split())
    if a == 1:
        update(b,c)
    elif a == 2:
        print(segmultiple(b,c))