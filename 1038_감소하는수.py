L = [0,1,2,3,4,5,6,7,8,9]

front = L # front는 지금 만들 리스트의 이전 리스트를 의미한다.
for i in range(9):
    tmp = [] # 이번에 추가될 리스트
    num = 1 # 앞에 더할 수
    d = 10**i # 자리 수를 맞추기 위한 10의 거듭제곱
    while True:  
        for item in front:
            if num > item//d:
                tmp.append(num*d*10+item)
            else:
                break
        num += 1
        if num == 10: # 앞에 더할 수가 10이 되면 이번 반복은 종료
            front = tmp[:] # 만들어진 리스트는 front에 저장함과 동시에
            L += tmp # 전체 리스트에 더함
            break

N = int(input())
if N <= 1022:
    print(L[N])
else:
    print(-1)