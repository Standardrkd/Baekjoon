from collections import deque
import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    C = list(input().strip())
    N = int(input())
    err = False
    if N == 0:
        trash = input()
        L = []
        L_reverse = []
    else:   
        L = list(map(str, input()[1:-2].split(',')))
        L_reverse = deque(reversed(L))
        L = deque(L)
    isReversed = False

    for comm in C:
        if comm == "R":
            isReversed = not isReversed
        else:
            if len(L) == 0:
                err = True
                break
            elif isReversed:
                L_reverse.popleft()
                L.pop()
            else:
                L_reverse.pop()
                L.popleft()
    if err:
        print("error")
        continue
    elif isReversed:
        print('[',end='')
        print(','.join(L_reverse),end='')
        print(']')
    else:
        print('[',end='')
        print(','.join(L),end='')
        print(']') 