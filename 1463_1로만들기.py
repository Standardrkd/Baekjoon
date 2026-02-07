table = [0 for _ in range(1000001)]
table[1] = 0
N = int(input())
for num in range(2,1000001):
    min_tmp = table[num - 1] + 1
    if num % 2 == 0 and min_tmp > table[num//2]:
        min_tmp = table[num//2] + 1
    
    if num % 3 == 0 and min_tmp > table[num//3]:
        min_tmp = table[num//3] + 1
    
    table[num] = min_tmp

print(table[N])
