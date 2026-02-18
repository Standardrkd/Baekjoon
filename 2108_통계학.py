import math, sys
input = sys.stdin.readline
N = int(input())
l = []
d = dict() # 최빈값을 위한 딕셔너리

for i in range(N):
    a = int(input())
    l.append(a)
    if not a in d:
        d[a] = 1
    else:
        d[a] += 1
l.sort()

# 산술평균
sl = sum(l)
if sl > 0: # 파이썬 반올림이 생각처럼 되지 않기 때문에 구현함
    if int(str(float(sl/N)).split('.')[1][0]) >= 5:
        print(math.ceil(sl/N))
    else:
        print(math.floor(sl/N))
else:
    if int(str(float(sl/N)).split('.')[1][0]) >= 5:
        print(math.floor(sl/N))
    else:
        print(math.ceil(sl/N))

# 중앙값
print(l[N//2])

# 최빈값
cnt = 0
mc = 0
mcl = []
for k,v in d.items():
    if v > cnt:
        mc = k
        cnt = v
        mcl = [mc]
    elif v == cnt:
        mcl.append(k)
mcl.sort()
if len(mcl) >= 2:
    print(mcl[1])
else:
    print(mcl[0])

# 범위
print(l[N-1] - l[0])

#dusgbdp qorwnsee
#연휴에 백준ㄷㄷ