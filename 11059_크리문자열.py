S = list(map(int, list(input())))
size = []
for i in range(2,len(S)+1,2): # 영역
    for j in range(len(S)-i+1):
        tmp = S[j:j+i]
        l1 = tmp[0:i//2]
        l2 = tmp[i//2:i]
        if sum(l1) == sum(l2):
            size.append(i)
if len(size) != 0 : print(max(size))