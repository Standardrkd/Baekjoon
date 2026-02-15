N = int(input())
result = 0
eliminate = [9, 90, 900, 9000, 90000, 900000, 9000000, 90000000, 900000000]
for i in eliminate:
    if N < i:
        result += (len(str(i))*(N))
        break
    else:
        result += i*len(str(i))
        N -= i
print(result)