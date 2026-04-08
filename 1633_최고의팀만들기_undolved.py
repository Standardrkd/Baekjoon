L = []
result = 0
while True:
    try:
        a, b = map(int, input().split())
        L.append((a, b))
    except:
        break
for i in range(30):
    if i%2 == 0: # 백을 정하기
        L.sort()    
        print(L[-1][0])
        result += L.pop()[0]
    else: # 흑을 정하기
        L.sort(key= lambda x : x[1])
        print(L[-1][1])
        result += L.pop()[1]
print(result)