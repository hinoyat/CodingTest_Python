N = int(input())
lst = list(map(int, input().split()))

increase_DP = [1] * N
decrease_DP = [1] * N

for i in range(1, N):
    for j in range(0, i):
        if lst[j] < lst[i]:
            increase_DP[i] = max(increase_DP[i], increase_DP[j] + 1)
new_lst = list(reversed(lst))
# print(new_lst)
for i in range(1, N):
    for j in range(0, i):
        if new_lst[j] < new_lst[i]:
            decrease_DP[i] = max(decrease_DP[i], decrease_DP[j] + 1)

decrease_DP = list(reversed(decrease_DP))
# print(increase_DP)
# print(decrease_DP)

max_len = 0
for i in range(N):
    temp_len = increase_DP[i] + decrease_DP[i]
    max_len = max(max_len, temp_len)
print(max_len -1)
