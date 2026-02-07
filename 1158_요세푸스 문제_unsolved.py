# 요세푸스 문제
N, K = map(int, input().split())

Josephus = [i+1 for i in range(N)] # 1,2,3,4 ...
result = []
index = 0
while Josephus:
    result.append(Josephus.pop((index + K-1)%len(Josephus)))
    if len(Josephus) != 0:
        index = (index+K-1)%len(Josephus)
        


print(result)
