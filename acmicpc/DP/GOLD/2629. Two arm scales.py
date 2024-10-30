# 양팔 저울
# 주어진 구슬의 무게를 확인할 수 있는지

N = int(input())
my_weight = list(map(int, input().split()))
M = int(input())
check_weight = list(map(int, input().split()))

max_weight = 500
max_weight_cnt = 30
max_checking = max_weight * max_weight_cnt

my_dp = [0] * 40001
my_dp[0] = 1

for mine in my_weight:
    can = set()
    for i in range(40001):
        if my_dp[i]:
            if i + mine <= 40001:
                can.add(i + mine)
            if i - mine >= 0:
                can.add(i - mine)
            if mine - i >= 0:
                can.add(mine - i)
    for c in can:
        my_dp[c] = 1

for check in check_weight:
    if my_dp[check]:
        print('Y', end=' ')
    else:
        print('N', end=' ')