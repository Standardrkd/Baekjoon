N = int(input())
binary = bin(N)[2:]
result = 0

for i in range(len(binary)-1, -1, -1):
    if binary[i] == '1':
        result += 3**(len(binary)-i-1)

print(result)
