S = input()
d = dict()

for i in S:
    if not i in d or not i.swapcase() in d:
        d[i] = 1
    else:
        d[i] += 1

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

