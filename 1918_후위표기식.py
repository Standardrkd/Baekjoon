operators = []
d = {"+" : 1, "-" : 1, "*" : 2, "/" : 2}
L = list(input())

for i in range(len(L)):
    if L[i] == "(":
        operators.append("(")
    elif L[i] == ")":
        o = operators.pop()
        while o != "(":
            print(o,end="")
            o = operators.pop()
    elif L[i] in d.keys():
        while True:
            if len(operators) == 0 or operators[-1] == "(" or d[operators[-1]] < d[L[i]]:
                break
            else:
                print(operators.pop(), end="")
        operators.append(L[i])
    else:
        print(L[i], end="")
while operators:
    print(operators.pop(), end="")
    