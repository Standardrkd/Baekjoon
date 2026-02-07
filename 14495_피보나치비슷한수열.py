table = [1,1,1,2]
N = int(input())
for i in range(116):
    table.append(table[i]+table[i+1]+table[i+2])

print(table[N-1])