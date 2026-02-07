# 셀프 넘버 구하기 (생성자가 없는 수)

'''
1 ~ 10000 까지 d함수를 적용시킨 수들은 자연수 리스트에서 제거함
그 리스트가 답임
'''
L = [i for i in range(20000)]

for i in range(1,10000):
    x = i + sum(list(map(int, list(str(i)))))
    L[x] = 0

r = 0
while True:
    if r > 10000:
        break
    if L[r] != 0:
        print(L[r])
    r += 1


