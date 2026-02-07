# 팰린드롬
from itertools import permutations
T = int(input())

def is_palindrome(list):
    for i in range(len(list)//2):
        if list[i] != list[len(list)-i-1]:
            return False
    return True
    


for _ in range(T):
    N = int(input())
    L = []
    checker = 0
    for i in range(N):
        L.append(list(input()))
    
    for t in permutations(L,2):
        tmp = t[0] + t[1]
        if is_palindrome(tmp):
            for j in tmp:
                print(j, end='')
            print()
            checker += 1
            break
    if checker == 0:
        print(0)
        
