def find_position(stu_num, info):
    temp_i = False
    temp_j = False

    max_favorite_friend = 0
    max_empty_place = 0

    for i in range(N-1, -1, -1):
        for j in range(N-1, -1, -1):
            if arr[i][j] == 0:
                temp_favorite_friend = 0
                temp_empty_place = 0
                for di, dj in direction:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < N and 0 <= nj < N:
                        if arr[ni][nj] in info:
                            temp_favorite_friend += 1
                        elif arr[ni][nj] == 0:
                            temp_empty_place += 1
                if max_favorite_friend == temp_favorite_friend:
                    if temp_empty_place >= max_empty_place:
                        max_empty_place = temp_empty_place
                        temp_i = i
                        temp_j = j
                elif max_favorite_friend < temp_favorite_friend:
                    max_favorite_friend = temp_favorite_friend
                    max_empty_place = temp_empty_place
                    temp_i = i
                    temp_j = j

    arr[temp_i][temp_j] = stu




N = int(input())


arr = [[0] * N for _ in range(N)]

info = [[]for _ in range((N * N) + 1)]

direction = ((0, 1), (1, 0), (-1, 0), (0, -1))

cnt = 0

for _ in range(N*N):
    stu, i1, i2, i3, i4 = map(int, input().split())
    stu_mind = (i1, i2, i3, i4)
    if cnt == 0:
        arr[1][1] = stu
    else:
        find_position(stu, stu_mind)
    info[stu].append(stu_mind)

    cnt += 1

ans = 0

point = {
    0 : 0,
    1 : 1,
    2 : 10,
    3 : 100,
    4 : 1000,
}

for i in range(N - 1, -1, -1):
    for j in range(N - 1, -1, -1):
        my_friend = 0
        cur_stu = arr[i][j]
        for di, dj in direction:
            ni, nj = i + di, j + dj
            if 0 <= ni < N and 0 <= nj < N:
                if arr[ni][nj] in info[cur_stu][0]:
                    my_friend += 1
        ans += point[my_friend]

print(ans)
