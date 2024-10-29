# 양팔 저울
# 주어진 구슬의 무게를 확인할 수 있는지

N = int(input())
my_weight = list(map(int, input().split()))
M = int(input())
check_weight = list(map(int, input().split()))

max_checking = sum(my_weight)
print(max_checking)
