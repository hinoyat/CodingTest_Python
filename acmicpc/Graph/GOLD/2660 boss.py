# 회장 뽑기
from collections import deque


def supernova(start):
    global min_val
    visited = [-1] * (N + 1)
    que = deque()
    visited[start] = 0
    que.append(i)
    max_val = 0
    while que:
        qpoint = que.popleft()
        for next in Graph[qpoint]:
            if visited[next] == -1:
                visited[next] = visited[qpoint] + 1
                que.append(next)
                max_val = max(max_val, visited[next])

    return max_val




# 입력
N = int(input())
Graph = [[] for _ in range(N + 1)]

while True:
    a, b = map(int, input().split())

    if a < 0 and b < 0:
        break

    Graph[a].append(b)
    Graph[b].append(a)



min_val = 100
candidate = []

for i in range(1, N + 1):
    val = supernova(i)
    if val == min_val:
        candidate.append(i)
    elif val < min_val:
        min_val = val
        candidate.clear()
        candidate.append(i)
candidate.sort()
print(min_val, len(candidate))
print(*candidate)