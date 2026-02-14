N, M = map(int, input().split())
L = list(map(int, input().split()))
prefix = []

p = 0
for i in L:
    p += i
    prefix.append(p)


'''
부분 합 중에서 M으로 나누어지는 구간의 개수를 구해라
'''
