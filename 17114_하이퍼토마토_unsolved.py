# 이런 미친 문제. 시간초과 어떻게 하냐!!!!!!!

from collections import deque
import sys

input = iter(open(0).read().splitlines()).__next__

queue = deque()
queue2 = deque()
cnt = 0
m, n, o, p, q, r, s, t, u, v, w = map(int, input().split())
Box = [[[[[[[[[[list(map(int, input().split())) for a in range(n)] for b in range(o)] for c in range(p)] for d in range(q)] for e in range(r)] for f in range(s)] for g in range(t)] for h in range(u)] for i in range(v)] for j in range(w)]

dws = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-1,1]
dvs = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-1,1,0,0]
dus = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-1,1,0,0,0,0]
dts = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,-1,1,0,0,0,0,0,0]
dss = [0,0,0,0,0,0,0,0,0,0,0,0,-1,1,0,0,0,0,0,0,0,0]
drs = [0,0,0,0,0,0,0,0,0,0,-1,1,0,0,0,0,0,0,0,0,0,0]
dqs = [0,0,0,0,0,0,0,0,-1,1,0,0,0,0,0,0,0,0,0,0,0,0]
dps = [0,0,0,0,0,0,-1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
dos = [0,0,0,0,-1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
dns = [0,0,-1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
dms = [-1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0] # 변화량





def in_range(a,b,c,d,e,f,g,h,i,j,k):
    return 0<=a<w and 0<=b<v and 0<=c<u and 0<=d<t and 0<=e<s and 0<=f<r and 0<=g<q and 0<=h<p and 0<=i<o and 0<=j<n and 0<=k<m

def bfs():
    global add_tomato
    while queue:
        a, b, c, d, e, f, g, h, i, j, k = queue.popleft()
        for da, db, dc, dd, de, df, dg, dh, di, dj, dk in zip(dws, dvs, dus, dts, dss, drs, dqs, dps, dos, dns, dms):
            na = a+da
            nb = b+db
            nc = c+dc
            nd = d+dd
            ne = e+de
            nf = f+df
            ng = g+dg
            nh = h+dh
            ni = i+di
            nj = j+dj
            nk = k+dk

            if in_range(na,nb,nc,nd,ne,nf,ng,nh,ni,nj,nk) and Box[na][nb][nc][nd][ne][nf][ng][nh][ni][nj][nk] == 0:
                Box[na][nb][nc][nd][ne][nf][ng][nh][ni][nj][nk] = 1
                queue2.append((na,nb,nc,nd,ne,nf,ng,nh,ni,nj,nk))
                add_tomato += 1

first_tomato = 0
add_tomato = 0
void = 0
for a in range(w):
    for b in range(v):
        for c in range(u):
            for d in range(t):
                for e in range(s):
                    for f in range(r):
                        for g in range(q):
                            for h in range(p):
                                for i in range(o):
                                    for j in range(n):
                                        for k in range(m):
                                            if Box[a][b][c][d][e][f][g][h][i][j][k] == 1:
                                                queue2.append((a,b,c,d,e,f,g,h,i,j,k))
                                                first_tomato += 1
                                            elif Box[a][b][c][d][e][f][g][h][i][j][k] == -1:
                                                void += 1

while queue2:
    queue = queue2
    queue2 = deque()
    bfs()
    cnt += 1


if void + first_tomato + add_tomato == m*n*o*p*q*r*s*t*u*v*w:
    print(cnt-1)
else:
    print(-1) 