import sys

input = sys.stdin.readline

def find(check):
    if check != parent[check]:
        parent[check] = find(parent[check])

    return parent[check]

def union(a, b):

    a = find(a)
    b = find(b)

    if a > b:
        parent[a] = b
    else:
        parent[b] = a

N, M = map(int, input().split())

parent = [i for i in range(N)]

turn = 0
result = False

for turn in range(1, M + 1):
    a, b = map(int, input().split())

    if find(a) == find(b):
        result = True
        break
    else:
        union(a, b)

if result:
    print(turn)
else:
    print(0)