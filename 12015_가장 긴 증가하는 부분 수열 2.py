from bisect import bisect_right
N  = int(input())
input_list = list(map(int,input().split()))
dp = []
for i in input_list:
    dp.append((i, 0))

for i in range(N):
    longest = 0
    # TODO: i이전의 원소를 크기순으로 정렬 후 나보다 작은 값들 중 가장 큰 인덱스를 이분탐색으로 찾는다.
    #       그리고 그 인덱스 기준으로 왼쪽 부분을 dp값 기준으로 정렬 후 가장 큰 dp값을 찾는다.
     

print(max(dp))
