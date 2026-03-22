N, K = map(int, input().split())
item = ["1인덱스를 쓸 거야"]
for _ in range(N):
    w, v = map(int, input().split())
    item.append(())

dp = [[0] * (K+1) for _ in range(N+1)]

for i in range(1,N):
    for j in range(1,K):
        pass