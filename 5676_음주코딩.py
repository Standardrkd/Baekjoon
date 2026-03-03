import sys
input = sys.stdin.readline
while 1:
    try:
        N, K = map(int, input().split())

        k = 0
        size = 0
        while 1:
            if 2**k >= N:
                size = 2**(k+1)
                break
            k += 1

        tree = [1] * size
        leaf_start = 2**k
        l = list(map(int, input().split()))

        for i in range(N):
            tree[leaf_start + i] = l[i]

        for i in range(size-1, 0, -1):
            if tree[i] < 0:
                tree[i//2] *= -1
            elif tree[i] == 0:
                tree[i//2] = 0

        def multiple(s,e):
            r = 1
            s = leaf_start + s - 1
            e = leaf_start + e - 1

            while 1:
                if s > e:
                    if r > 0:
                        return '+'
                    elif r < 0:
                        return '-'
                    else:
                        return '0'
                
                if s%2 == 1:
                    if tree[s] < 0:
                        r *= -1
                    elif tree[s] == 0:
                        r *= 0
                s = (s+1)//2

                if e%2 == 0:
                    if tree[e] < 0:
                        r *= -1
                    elif tree[e] == 0:
                        r *= 0
                e = (e-1)//2


        def update(i,v):
            i = leaf_start + i - 1
            tree[i] = v
            for _ in range(k):
                if i%2 == 0:
                    if tree[i]*tree[i+1] < 0:
                        tree[i//2] = -1
                    elif tree[i]*tree[i+1] == 0:
                        tree[i//2] = 0
                    else:
                        tree[i//2] = 1
                else:
                    if tree[i]*tree[i-1] < 0:
                        tree[i//2] = -1
                    elif tree[i]*tree[i-1] == 0:
                        tree[i//2] = 0
                    else:
                        tree[i//2] = 1
                i //= 2

        result = ''

        for _ in range(K):
            c, a,b = input().split()
            a = int(a)
            b = int(b)
            if c == 'C':
                update(a,b)
            elif c == 'P':
                if a < b:
                    result += multiple(a,b)
                else:
                    result += multiple(b,a)
        print(result)
    except:
        break