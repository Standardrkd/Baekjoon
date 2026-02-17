import sys
sys.set_int_max_str_digits(20000)
N = int(input())
n = 1
step = 0
remain = 0

while True:
    s = (n*(n+1))//2

    if s > N:
        n = n - 1
        remain = N - (n*(n+1))//2 # 최대 등차수열하고 나머지
        step = n + 1
        break
    if s == N:
        step = n
        remain = n
        break

    n += 1
try:
    print(int(3**(step-1) + 3**(remain-2)))
except:
    print("wrong")