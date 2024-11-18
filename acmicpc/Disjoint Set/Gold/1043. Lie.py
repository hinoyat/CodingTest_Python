from collections import deque


def find(cur):
    if parent[cur] != cur:
        parent[cur] = find(parent[cur])

    return parent[cur]


def union(a, b):

    a = find(a)
    b = find(b)

    if a in people_who_know_the_truth:
        parent[b] = a
    elif b in people_who_know_the_truth:
        parent[a] = b




N, M = map(int,input().split())

people_who_know_the_truth = list(map(int, input().split()))

people_cnt = people_who_know_the_truth.pop(0)

person = [[] for _ in range(N + 1)]

party = [[]for _ in range(M + 1)]

parent = [i for i in range(N + 1)]

visited = [0] * (N + 1)

for m in range(1, M + 1):
    info = list(map(int, input().split()))
    num_people = info.pop(0)
    if num_people >= 2:
        for i in range(num_people):
            for j in range(num_people):
                if info[i] != info[j]:
                    person[info[i]].append(info[j])

    party[m] = info

cannot = 0
que = deque()
if people_cnt != 0:
    for p in people_who_know_the_truth:
        que.append(p)
        visited[p] = 1
    while que:
        q = que.popleft()
        for new_q in person[q]:
            if not visited[new_q]:
                union(q, new_q)
                visited[new_q] = 1
                que.append(new_q)
    for i in range(1, M + 1):
        for j in party[i]:
            if parent[j] in people_who_know_the_truth:
                cannot += 1
                break
print(M - cannot)
