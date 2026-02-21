table = [1,1]
N = int(input())
for i in range(N-2):
    table.append(table[i]+table[i+1])
print(table[N-1])