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
    for i in range(0, array_len):
        for j in range(0, array_len):
            zero = 0
            for di, dj in ((0, 1), (1, 0), (0, -1), (-1, 0)):
                ni, nj = i + di, j + dj
                if 0 <= ni < array_len and 0 <= nj < array_len:
                    if arr[ni][nj] == 0:
                        zero += 1
            if zero <= 1:
                new_arr[i][j] = arr[i][j]
            else:
                new_arr[i][j] = arr[i][j] - 1
    arr = new_arr





N, Q = map(int, input().split())

array_len = 2 ** N

arr = [list(map(int, input().split())) for _ in range(array_len)]

magic = list(map(int, input().split()))
for m in magic:
    rotate(m)
    supernova()


ans = 0
for i in arr:
    ans += sum(i)
print(ans)
