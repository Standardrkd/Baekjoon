def push(n):
    i = 1
    while True:
        if bst[i] == 0:
            bst[i] = n
            break
        else:
            if n <= bst[i]:
                i = i*2
            else:
                i = i*2 + 1

def search(i):
    if bst[i*2] == 0 and bst[i*2+1] == 0:
        if bst[i] != 0: print(bst[i])
        return

    search(i*2)
    search(i*2 + 1)
    print(bst[i])



    
input_stream = []
while True:
    try:
        input_stream.append(int(input()))
    except:
        break

bst = [0 for _ in range(2**(len(input_stream) + 1))]
for i in input_stream:
    push(i)

search(1)