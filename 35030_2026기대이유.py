import sys      
input = sys.stdin.readline

n = 100001
prime = [False,False] + [True]*(n-1)

for i in range(2,n+1):
    if prime[i]:
        for j in range(2*i, n+1, i):
            prime[j] = False

T = int(input())
cnt_list = [0]
for k in range(1, 100001):
    checker = True
    N = str(k)
    for i in range(len(N)): # 쪼개기
        if i != 0:
            a = int(N[0:i]) 
            b = int(N[i:])
            if not prime[a*b+1]:
                checker = False
        else:
            b = int(N[i:])
            if not prime[b+1]:
                checker = False
    if checker:
        cnt_list.append(cnt_list[k-1]+1)
    else:
        cnt_list.append(cnt_list[k-1])

for i in range(T):
    n = int(input())
    print(cnt_list[n])