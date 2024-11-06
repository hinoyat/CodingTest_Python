from collections import deque
from pprint import pprint
def rotate(ma):
    global arr, array_len
    temp_len = 2 ** ma

    new_arr = [[0] * array_len for _ in range(array_len)]
    # print(len(new_arr))
    for i in range(0, array_len, temp_len):
        for j in range(0, array_len, temp_len):
            for ni in range(temp_len):
                for nj in range(temp_len):
                    new_arr[i + ni][j + nj] = arr[i + (temp_len - nj - 1)][j + ni]

    arr = new_arr

def supernova():
    global arr
    new_arr = [[0] * array_len for _ in range(array_len)]
    for i in range(array_len):
        for j in range(array_len):
            if arr[i][j] > 0:
                val = 0
                for di, dj in ((0, 1), (1, 0), (0, -1), (-1, 0)):
                    ni, nj = i + di, j + dj
                    if 0 <= ni < array_len and 0 <= nj < array_len:
                        if arr[ni][nj] != 0:
                            val += 1
                if val < 3:
                    new_arr[i][j] = arr[i][j] - 1
                else:
                    new_arr[i][j] = arr[i][j]
    arr = new_arr

def find_max(i, j):
    que = deque()
    que.append((i, j))
    visited[i][j] = 1
    temp_val = 1
    while que:
        qi, qj = que.popleft()
        for di, dj in ((0, 1), (1, 0), (0, -1), (-1, 0)):
            ni, nj = qi + di, qj + dj
            if 0 <= ni < array_len and 0 <= nj < array_len and not visited[ni][nj] and arr[ni][nj] != 0:
                que.append((ni, nj))
                temp_val += 1
                visited[ni][nj] = 1
    return temp_val


N, Q = map(int, input().split())

array_len = 2 ** N

arr = [list(map(int, input().split())) for _ in range(array_len)]

magic = list(map(int, input().split()))
for m in magic:
    rotate(m)
    supernova()

max_val = 0
total_val = 0

visited = [[0] * array_len for _ in range(array_len)]

for i in range(array_len):
    for j in range(array_len):
        total_val += arr[i][j]
        if arr[i][j] != 0 and not visited[i][j]:
            max_val = max(max_val, find_max(i, j))


print(total_val)
print(max_val)
