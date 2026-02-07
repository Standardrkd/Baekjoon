N, K = map(int, input().split())
L = list(map(int, input().split()))
sum_list = []
part_sum = sum(L[:K])
sum_list.append(part_sum)
for i in range(N-K):
    sum_list.append(part_sum-L[i]+L[i+K])
    part_sum = part_sum-L[i]+L[i+K]
print(max(sum_list))