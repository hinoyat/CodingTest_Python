from collections import deque
from pprint import pprint



def spread_test(start):
    temp_dust = [[0] * C for _ in range(R)]
    que = deque(start)

    while que:
        qi, qj = que.popleft()
        spread = 0
        for di, dj in spread_direction:
            ni, nj = qi + di, qj + dj
            if 0 <= ni < R and 0 <= nj < C:
                if (ni, nj) not in samsung_air_conditioner:
                    temp_dust[ni][nj] += int(my_room[qi][qj]/5)
                    spread += 1
        temp_dust[qi][qj] += my_room[qi][qj] - int(my_room[qi][qj]/5) * spread
    return temp_dust


def air_moving():
    conditioner = 0
    for si, sj in samsung_air_conditioner:
        if conditioner == 0:
            direction = air_move[0]
        else:
            direction = air_move[1]
        conditioner += 1

        ni = si
        nj = sj
        dir = 0
        temp = 0
        d = 0
        while True:
            di = spread_direction[direction[d]][0]
            dj = spread_direction[direction[d]][1]
            if 0 <= ni + di < R and 0 <= nj + dj < C:
                ni, nj = ni + di, nj + dj
                my_room[ni][nj], temp = temp, my_room[ni][nj]
            else:
                d = (d + 1) % 4
            # print(dir)
            # print(ni, nj)
            # pprint(my_room)

            if (ni, nj) == (si, sj):
                break

        my_room[si][sj] = 0






R, C, T = map(int, input().split())
my_room = [list(map(int, input().split())) for _ in range(R)]

# 공기 청정기 찾기
samsung_air_conditioner = []
air_move = ((0, 1, 2, 3), (0, 3, 2, 1))

                    # 우      상       좌       하~~
spread_direction = ((0, 1), (-1, 0), (0, -1), (1, 0))

status = []

for i in range(R):
    for j in range(C):
        if my_room[i][j] == -1:
            samsung_air_conditioner.append((i, j))

first_conditioner = (samsung_air_conditioner[0][0], [samsung_air_conditioner[0][1]])
second_conditioner = (samsung_air_conditioner[1][0], [samsung_air_conditioner[1][1]])

for _ in range(T):
    # 먼지 찾기
    for i in range(R):
        for j in range(C):
            if my_room[i][j] > 0:
                status.append((i, j))

    new_room = (spread_test(status))
    # pprint(new_room)
    my_room = new_room
    air_moving()
    # pprint(my_room)
    status = []
# 정답
ans = 0
for i in range(R):
    ans += sum(my_room[i])
print(ans)
