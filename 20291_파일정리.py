import sys
input = sys.stdin.readline

N = int(input())
d = dict()
for _ in range(N):
    ext = input().split('.')[1].strip()

    if ext in d:
        d[ext] += 1
    else:
        d[ext] = 1

srtd = dict(sorted(d.items()))
for k,v in srtd.items():
    print(f"{k} {v}")