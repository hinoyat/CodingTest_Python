# 붐버맨

# 초기 폭탄 설치 되어 있습니다~~~   1

# 1초는 일단 암것도 하지 않구요~~~    2

# 다음 1초 폭탄 X 인 칸에 동시에 설치하면 되겠죠~~~~~    3

# 3초 전에 설치된 폭탄이 터지겠죠~~~~~    4

# 3과 4 반복

# 폭탄 설치
# 0인 곳이 있으면 3으로 바꿔주기?
def set_boom():
    for i in range(R):
        for j in range(C):
            if game_board[i][j] == 0:
                game_board[i][j] = 3

# 폭탄 터쳐
def boom():
    new_board = [[0] * C for _ in range(R)]

    for i in range(R):
        for j in range(C):
            if game_board[i][j] >= 1:
                game_board[i][j] -= 1
                if game_board[i][j] == 0:
                    for di, dj in ((1, 0), (-1, 0), (0, -1), (0, 1)):
                        ni, nj = i + di, j + dj
                        if 0<= ni < R and 0 <= nj < C:
                            new_board[ni][nj] = -1

    for i in range(R):
        for j in range(C):
            if new_board[i][j] == -1:
                new_board[i][j] = 0
            else:
                new_board[i][j] = game_board[i][j]

    return new_board


# 초기 폭탄 설치
def start_boom():
    for i in range(R):
        for j in range(C):
            if arr[i][j] == 'O':
                game_board[i][j] = 2
            else:
                game_board[i][j] = 0


import sys
input = sys.stdin.readline

# R은 row C는 col N은 시간
R, C, N = map(int, input().split())

arr = [list(input()) for _ in range(R)]

time = 1
game_board = [[0] * C for _ in range(R)]

# 처리하기 편하게 폭탄 설치하고 시간 1초 늘리고 시작 N은 1부터
start_boom()


for _ in range(N):
    if time == N:
        break

    set_boom()
    time += 1
    if time == N:
        break
    game_board = boom()
    game_board = boom()

    time += 1

for i in range(R):
    for j in range(C):
        if game_board[i][j] == 0:
            print('.', end = '')
        else:
            print('O', end = '')
    print()