def find(check):
    if city[check] != check:
        city[check] = find(city[check])

    return city[check]

def union(a, b):

    a = find(a)
    b = find(b)

    if a > b:
        city[a] = b
    else:
        city[b] = a



N = int(input())
M = int(input())

city = [i for i in range(N)]
Graph = [[] for _ in range(N)]

for i in range(N):
    info = list(map(int, input().split()))
    for j in range(N):
        if info[j] == 1:
            if find(i) != find(j):
                union(i, j)

ans = True
travel = list(map(int, input().split()))
for t in travel:
    if city[t - 1] != city[travel[0] - 1]:
        ans = False
        break
if ans == True:
    print('YES')
else:
    print('NO')