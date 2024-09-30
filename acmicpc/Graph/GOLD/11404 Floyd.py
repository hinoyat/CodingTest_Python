

N = int(input())
M = int(input())

Graph = [[] for _ in range(N + 1)]
for i in range(M):
    a, b, val = map(int, input().split())
    Graph[a].append((val, b))

for  i in range(1, N+1):
    for j in range(1, N + 1):
        pass