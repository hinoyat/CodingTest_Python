from itertools import combinations
from collections import deque
def find_ans(lst):
    que = deque()
    visited = [0] * (N + 1)
    visited[0] = 1
    que.append(lst[0])
    visited[lst[0]] = 1
    val = 0
    val += people[lst[0]]

    while que:
        q = que.popleft()
        for nq in graph[q]:
            if not visited[nq] and nq in lst:
                visited[nq] = 1
                que.append(nq)
                val += people[nq]


    lst2 = []
    for i in N_to_list:
        if i not in lst:
            lst2.append(i)
    val2 = 0
    val2 += people[lst2[0]]
    que.append(lst2[0])
    visited[lst2[0]] = 1
    while que:
        q = que.popleft()
        for nq in graph[q]:
            if not visited[nq] and nq in lst2:
                visited[nq] = 1
                que.append(nq)
                val2 += people[nq]

    for v in N_to_list:
        if not visited[v]:
            return 10000000
    return abs(val2 - val)



N = int(input())
people = [0] + list(map(int, input().split()))

N_to_list = [i for i in range(1, N + 1)]

graph = [[]for _ in range(N + 1)]

for n in range(1, N + 1):
    info = list(map(int, input().split()))
    if info[0] == 0: continue
    num = info.pop(0)
    for i in info:
        graph[n].append(i)

my_comb = []

for c in range(1, N//2 + 1):
    for comb in combinations(N_to_list, c):
        my_comb.append(comb)

ans = 10000000

for clst in my_comb:
    ans = min(find_ans(clst), ans)

if ans == 10000000:
    print(-1)
else:
    print(ans)

#
# from itertools import combinations
# from collections import deque
#
# def find_ans(lst):
#     visited = [0] * (N + 1)
#     val = 0
#     que = deque([lst[0]])
#     visited[lst[0]] = 1
#     val += people[lst[0]]
#
#     while que:
#         q = que.popleft()
#         for nq in graph[q]:
#             if nq in lst and not visited[nq]:
#                 visited[nq] = 1
#                 que.append(nq)
#                 val += people[nq]
#
#     lst2 = [i for i in N_to_list if i not in lst]
#
#     val2 = 0
#     que = deque([lst2[0]])
#     visited[lst2[0]] = 1
#     val2 += people[lst2[0]]
#
#     while que:
#         q = que.popleft()
#         for nq in graph[q]:
#             if nq in lst2 and not visited[nq]:
#                 visited[nq] = 1
#                 que.append(nq)
#                 val2 += people[nq]
#
#     for i in N_to_list:
#         if not visited[i]:
#             return 10000000
#
#     return (abs(val2 - val))
#
#
# N = int(input())
# people = [0] + list(map(int, input().split()))
#
# N_to_list = [i for i in range(1, N + 1)]
#
# graph = [[] for _ in range(N + 1)]
#
# for n in range(1, N + 1):
#     info = list(map(int, input().split()))
#     if info[0] == 0:
#         continue
#     num = info.pop(0)
#     for i in info:
#         graph[n].append(i)
#
# my_comb = []
# for c in range(1, N//2 + 1):
#     for comb in combinations(N_to_list, c):
#         my_comb.append(comb)
#
# ans = 10000000
#
# for clst in my_comb:
#     ans = min(find_ans(clst), ans)
#
# if ans == 10000000:
#     print(-1)
# else:
#     print(ans)
#


