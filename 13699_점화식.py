# def func(n):
#     result = 0
#     if n == 0 or n == 1:
#         return 1
#     for i in range(n):
#         result += func(i)*func(n-i-1)
#     return result
table = [1]

N = int(input())
for i in range(N):
    add = 0
    for j in range(len(table)):
        add += table[j]*table[len(table)-j-1]
    table.append(add)
print(table[N])