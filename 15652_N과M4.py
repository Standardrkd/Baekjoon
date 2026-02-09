N, M = map(int, input().split())
start = int('1'*N)

def is_desc(list):
    tmp = 0
    for num in list:
        if tmp > num:
            return False
        tmp = num
    return True

for i in range(start,start*M):
    l = list(map(int, list(str(i))))
    if is_desc(l):
        print(*l)
    
