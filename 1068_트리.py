# N = int(input())
# L = list(map(int, input().split()))
# root = L.index(-1)
# leaf = 0
# tree = [[] for _ in range(N)]

# for i in range(N):
#     tree[L[i]].append(i)
# d = int(input())

# for i in range(N):
#     for j in tree[i]:
#         if j == d:
#             tree[i].remove(j)
# tree[d] = -1 
# def findLeaf(x):
#     global leaf, root
#     if tree[x] == []:
#         leaf += 1
#         return
#     if x == root and tree[x] == -1:
#         return
#     for n in tree[x]:
#         findLeaf(n)

# print(tree)
# findLeaf(root)        
# print(leaf)

N = int(input())
L = list(map(int, input().split()))
tree = [[] for _ in range(N)]
leaf = 0
root = L.index(-1)

for i in range(N):
    if L[i] != -1:
        tree[L[i]].append(i)

d = int(input())
for i in range(N):
    for j in tree[i]:
        if j == d:
            tree[i].remove(j)
tree[d] = -1

def leafs(x):
    global leaf
    if tree[x] == []:
        leaf += 1
        return
    for n in tree[x]:
        leafs(n)

if root == d:
    print(0)
    exit()
leafs(root)
print(leaf)