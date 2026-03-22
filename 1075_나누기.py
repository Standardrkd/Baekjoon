s = input()
N = s[:len(s) - 2] + "00"
F = int(input())
for i in range(100):
    if (int(N) + i) % F == 0:
        print(str(int(N) + i)[len(s)-2:len(s)])
        break   