N = int(input())
M = int(input())

Graph = [[21e8] * (N + 1) for _ in range(N + 1)]

for  i in range(1, N+1):
    for j in range(1, N + 1):
        if i == j:
            Graph[i][j] = 0

for i in range(M):
    a, b, val = map(int, input().split())
    Graph[a][b] = min(val, Graph[a][b])

for k in range(1, N + 1):
    for  i in range(1, N+1):
        for j in range(1, N + 1):
            Graph[i][j] = min(Graph[i][j], Graph[i][k] + Graph[k][j])

for i in range(1, N+1):
    for j in range(1, N + 1):
        if Graph[i][j] == 21e8:
            print('0', end = ' ')
        else:
            print(Graph[i][j], end = ' ')
    print()