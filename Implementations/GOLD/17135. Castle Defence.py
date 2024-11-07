# def check_enemy():
#     global game_board
#
#     check = 0
#     for g in game_board:
#         check += sum(g)
#
#     if check > 0:
#         return True
#     else:
#         return False
#
#
# def game_loading():
#     global game_board
#     new_game_board = [[0] * M for _ in range(N)]
#
#     for i in range(0, N - 1):
#         for j in range(M):
#             new_game_board[i + 1][j] = game_board[i][j]
#
#     game_board = new_game_board
#
#
# def kill_enemy(D):
#     global game_board
#     attack_point = [0] * M
#     kill_count = 0
#     point = []
#     for p in range(M):
#         max_enemy_len = D + 1
#         excute_point = None
#         for i in range(N - 1, N - 1 - D, -1):
#             for j in range(M - 1, -1, -1):
#                 if len(point) >= 3:
#                     break
#                 if game_board[i][j] == 1 and not attack_point[p]:
#                     enemy_len = abs(N - i) + abs(p - j)
#                     if enemy_len <= D:
#                         if enemy_len == max_enemy_len:
#                             excute_point = (i, j)
#                         elif enemy_len < max_enemy_len:
#                             max_enemy_len = enemy_len
#                             excute_point = (i, j)
#
#             if len(point) >= 3:
#                 break
#         if excute_point:
#             point.append(excute_point)
#         if len(point) >= 3:
#             break
#     print(point)
#     for i, j in point:
#         if game_board[i][j] == 1:
#             game_board[i][j] = 0
#             kill_count += 1
#
#     return kill_count
#
# N, M, D = map(int, input().split())
# game_board = [list(map(int, input().split())) for _ in range(N)]
# ans = 0
# from pprint import pprint
# while True:
#     pprint(game_board)
#     can = check_enemy()
#     if not can:
#         break
#     ans += kill_enemy(D)
#     game_loading()
#
# print(ans)


from copy import deepcopy
from itertools import combinations


def check_enemy():
    global game_board
    check = 0
    for g in game_board:
        check += sum(g)
    return check > 0


def game_loading():
    global game_board
    new_game_board = [[0] * M for _ in range(N)]
    for i in range(0, N - 1):
        for j in range(M):
            new_game_board[i + 1][j] = game_board[i][j]
    game_board = new_game_board


def kill_enemy(archer_positions, D):
    point = []
    for archer_col in archer_positions:
        min_distance = D + 1
        target = None

        # 가장 가까운 적을 찾음 (거리가 같다면 가장 왼쪽)
        for i in range(N - 1, -1, -1):
            for j in range(M):
                if game_board[i][j] == 1:
                    distance = abs(N - i) + abs(archer_col - j)
                    if distance <= D:
                        if distance < min_distance:
                            min_distance = distance
                            target = (i, j)
                        elif distance == min_distance and j < target[1]:
                            target = (i, j)

        if target:
            point.append(target)

    # 중복 제거하고 적을 제거
    kill_count = 0
    for i, j in set(point):
        if game_board[i][j] == 1:
            game_board[i][j] = 0
            kill_count += 1

    return kill_count


N, M, D = map(int, input().split())
original_board = [list(map(int, input().split())) for _ in range(N)]
max_kills = 0

# 가능한 모든 궁수 위치 조합을 생성
archer_combinations = list(combinations(range(M), 3))

# 각 조합에 대해 시뮬레이션 실행
for archers in archer_combinations:
    game_board = deepcopy(original_board)
    total_kills = 0

    while check_enemy():
        total_kills += kill_enemy(archers, D)
        game_loading()

    max_kills = max(max_kills, total_kills)

print(max_kills)