import sys
import heapq
input = sys.stdin.readline

def dijkstra(start, end):
    que = []
    path = []
    heapq.heappush(que, (0, start))
    visited = [2100000000] * N
    visited[start] = 0
    parent = [-1] * N
    while que:
        qv, qs = heapq.heappop(que)
        if qs == end:
            break
        for nv, ne in graph[qs]:
            new_v =  qv + nv
            if visited[ne] > new_v:
                parent[ne] = qs
                visited[ne] = new_v
                heapq.heappush(que, (new_v, ne))

    get_path_start = end
    while get_path_start != -1:
        path.append(get_path_start)
        get_path_start = parent[get_path_start]

    path.reverse()

    return visited[end], path


N = int(input())
M = int(input())

graph = [[] for _ in range(N)]

for i in range(M):
    a, b, val = map(int, input().split())
    graph[a - 1].append((val, b - 1))

start, end = map(int, input().split())

result, min_path = dijkstra(start-1, end-1)
for i in range(len(min_path)):
    min_path[i] += 1

print(result)
print(len(min_path))
print(*min_path)