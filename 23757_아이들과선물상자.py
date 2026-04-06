N, M = map(int, input().split())
present = list(map(int, input().split()))
childs = list(map(int, input().split()))
if sum(present) < sum(childs) or max(present) < max(childs):
    print(0)
else:
    print(1)