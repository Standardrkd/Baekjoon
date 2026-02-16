# 요세푸스 문제
N, K = map(int, input().split())

Josephus = [i+1 for i in range(N)] # 1,2,3,4 ...
result = []
index = K-1

while Josephus:
    result.append(Josephus.pop(index%len(Josephus)))
    if Josephus:
        index = (index + K -1)%(len(Josephus)) # 원소가 하나씩 없어지니까 index더할 때 1도 빼줘야함.
print(result)
