'''
수열 A가 주어졌을 때, 가장 긴 증가하는 부분 수열을 구하는 프로그램을 작성하시오.

예를 들어, 수열 A = {10, 20, 10, 30, 20, 50} 인 경우에 가장 긴 증가하는 부분 수열은 
A = {'10', '20', 10, '30', 20, '50'} 이고, 길이는 4이다.
'''



''' 
N  = int(input())
A = list(map(int,input().split()))
cnt_list = []

for i in range(N):
    cnt = 1
    tmp = A[i]
    for j in range(N-i-1):
        if tmp < A[i+j+1]:
            tmp = A[i+j+1]
            cnt += 1
    cnt_list.append(cnt)

print(max(cnt_list))

일단 첫 인덱스를 기준으로 시작해서 끝까지 검사하여 증가하는 길이를 저장하는 것을 모든 인덱스에 대해 반복
-> 예외 : 1 22 3 4 5 6 7 8 9 10 => 8x -> 9
'''




''''
10 20 10 30 20 50
1  2  1  3  2  4 

4 3 2 1 5
1 1 1 1 2

앞에 있던 최장 길이들의 최대를 더함
'''

N  = int(input())
A = list(map(int,input().split()))
len_list = [0] * N

for i in range(N):
    tmp = 0
    for j in range(i):
        if A[i] > A[j] and tmp < len_list[j]: # 현재의 수보다 작은 수의 길이 중 최대를 찾는다.
            tmp = len_list[j]
    len_list[i] = tmp+1 # 1을 더한 것을 해당 수까지의 최대 길이로 재정의한다.

print(max(len_list))
