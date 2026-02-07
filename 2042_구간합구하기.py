import sys
input = sys.stdin.readline

N,M,K = map(int,input().split())
size = 0
k = 0
while True: # k구하기
    if 2**k >= N:
        size = (2**k)*2
        break
    k += 1

segtree = [0] * size
l = []
for i in range(N):
    l.append(int(input()))

leaf_start = 2**k
for i in range(N):# 리프에 추가
    segtree[i+leaf_start] = l[i]

for i in range(size-1,1,-1): # 부모로 올라가며 더하기
    segtree[i//2] += segtree[i]

def segsum(s,e):
    result = 0
    # 트리 인덱스에 맞게 전처리
    s = s + leaf_start -1 
    e = e + leaf_start -1

    while True:
        if s > e:
            return result

        if s%2 == 1: # 독립 선택을 해야하는 경우
            result += segtree[s]
        s = (s+1)//2 # 부모로 올라가기
        if e%2 == 0:
            result += segtree[e]
        e = (e-1)//2 # 부모로 올라가기

def update(index,value):
    global k
    index = index + leaf_start -1
    d = value - segtree[index] # 변화할 값
    segtree[index] = value

    for i in range(k):
        index = index//2
        segtree[index] += d

for i in range(K+M):
    a,b,c = map(int, input().split())
    if a == 1:
        update(b,c)
    elif a == 2:
        print(segsum(b,c))
