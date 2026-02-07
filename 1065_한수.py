N = int(input())

def hansu(n):
    l = list(map(int, list(str(n))))
    if len(l) == 1:
        return True
    gongcha = l[1] - l[0]
    for i in range(len(l)-1):
        if l[i+1] - l[i] != gongcha:
            return False
    return True

cnt = 0

for i in range(1,N+1):
    if hansu(i):
        cnt += 1

print(cnt)