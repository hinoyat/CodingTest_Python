
'''
# 위상정렬 안 쓰고 하려고 발버둥
T = int(input())
for _ in range(T):

    N = int(input())

    last_ranking = list(map(int, input().split()))
    last_graph = [0] * (N + 1)
    rank_point = N - 1
    for i in last_ranking:
        last_graph[i] = rank_point
        rank_point -= 1

    changed_cnt = int(input())
    change_info = []
    for _ in range(changed_cnt):
        hi, lo = map(int, input().split())
        change_info.append((hi, lo))
    # print(last_graph)

    while change_info:
        h, l = change_info.pop()
        if last_graph[h] < last_graph[l]:
            last_graph[h] += 1
            last_graph[l] -= 1
        else:
            last_graph[h] -= 1
            last_graph[l] += 1


    # print(last_graph)
    can = True
    check_normal = set()
    new_ranking = []
    # print(last_graph)

    for i in range(1, N + 1):
        new_ranking.append((last_graph[i], i))
        if last_graph[i] < 0:
            can = False
        if last_graph[i] in check_normal:
            can = False
        if last_graph[i] >= N:
            can = False

        check_normal.add(last_graph[i])

    new_ranking.sort(reverse=True)
    re = 0
    for i in range(N):
        re += i
    # print(last_graph)
    if sum(last_graph) != re:
        can = False
    # print(re)
    # print(last_graph)

    final_graph = [team for point, team in new_ranking]
    # print(final_graph)
    if can == True:
        print(*final_graph)
    elif can == False:
        print('IMPOSSIBLE')
    else:
        print()
'''

# from collections import defaultdict, deque
#
#
# def solve():
#     n = int(input())
#     last_year = list(map(int, input().split()))
#
#     graph = defaultdict(set)
#     indegree = defaultdict(int)
#
#     for i in range(n):
#         for j in range(i + 1, n):
#             graph[last_year[i]].add(last_year[j])
#             indegree[last_year[j]] += 1
#
#     m = int(input())
#     for _ in range(m):
#         a, b = map(int, input().split())
#         if b in graph[a]:
#             graph[a].remove(b)
#             graph[b].add(a)
#             indegree[b] -= 1
#             indegree[a] += 1
#         else:
#             graph[b].remove(a)
#             graph[a].add(b)
#             indegree[a] -= 1
#             indegree[b] += 1
#
#     # 위상 정렬
#     q = deque()
#     for i in range(1, n + 1):
#         if indegree[i] == 0:
#             q.append(i)
#
#     result = []
#     uncertain = False
#
#     while q:
#         if len(q) > 1:
#             uncertain = True
#
#         cur = q.popleft()
#         result.append(cur)
#
#         for next_node in list(graph[cur]):
#             indegree[next_node] -= 1
#             if indegree[next_node] == 0:
#                 q.append(next_node)
#
#     if len(result) != n:
#         print("IMPOSSIBLE")
#     else:
#         print(*result)
#
#
# T = int(input())
# for _ in range(T):
#     solve()


# 위상정렬 안 쓰고 하려고 발버둥
T = int(input())
for _ in range(T):

    N = int(input())

    last_ranking = list(map(int, input().split()))
    last_graph = [0] * (N + 1)
    rank_point = N - 1
    for i in last_ranking:
        last_graph[i] = rank_point
        rank_point -= 1

    changed_cnt = int(input())
    change_info = []
    for _ in range(changed_cnt):
        hi, lo = map(int, input().split())
        change_info.append((hi, lo))
    # print(last_graph)

    while change_info:
        h, l = change_info.pop()
        if last_graph[h] < last_graph[l]:
            last_graph[h] += 1
            last_graph[l] -= 1
        else:
            last_graph[h] -= 1
            last_graph[l] += 1


    # print(last_graph)
    can = True
    check_normal = set()
    new_ranking = []
    # print(last_graph)

    for i in range(1, N + 1):
        new_ranking.append((last_graph[i], i))
        if last_graph[i] < 0:
            can = False
        if last_graph[i] in check_normal:
            can = False
        if last_graph[i] >= N:
            can = False

        check_normal.add(last_graph[i])

    new_ranking.sort()
    # print(new_ranking)
    for i in range(N):
        if new_ranking[i][0] != i:
            can = False
            break
    # print(last_graph)
    # print(re)
    # print(last_graph)

    final_graph = [team for point, team in new_ranking]
    # print(final_graph)
    if can == True:
        print(*final_graph)
    elif can == False:
        print('IMPOSSIBLE')
    else:
        print()