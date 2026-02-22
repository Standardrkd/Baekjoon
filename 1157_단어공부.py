S = input()
d = dict()

for i in S:
    if i in d or i.swapcase() in d:
        if 65 <= ord(i) <= 90:
            d[i] += 1
        else:
            d[i.swapcase()] += 1
    else:
        if 65 <= ord(i) <= 90:
            d[i] = 1
        else:
            d[i.swapcase()] = 1


most = ""
cnt = 0
p = False

for k,v in d.items():
    if v > cnt:
        most = k
        cnt = v
        p = True
    elif v == cnt:
        p = False

if p:
    print(most)
else:
    print("?")
