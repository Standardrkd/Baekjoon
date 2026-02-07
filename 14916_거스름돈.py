N = int(input())
a = 100000000
b = 100000000
table = ["index_out_of_range", -1, 1, -1, 2, 1]
for i in range(6,100001):
    if table[i-2] != -1:
        a = table[i-2] + 1
    if table[i-5] != -1:
        b = table[i-5] + 1
    if a == 0 and b == 0:
        table.append(-1)
    else:
        table.append(min(a,b))
    a = 100000000
    b = 100000000

print(table[N])
    
