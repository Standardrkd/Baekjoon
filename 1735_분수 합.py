a1, b1 = map(int, input().split())
a2, b2 = map(int, input().split())

a3, b3 = a2*b1+a1*b2, b1*b2

def gcd(a,b):
    if b == 0:
        return a
    return gcd(b,a%b)

g = gcd(a3,b3)
print(a3//g,b3//g)