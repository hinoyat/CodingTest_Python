# from collections import deque
from pprint import pprint
# def BFS(start, end):
#     que = deque()
#     visited = set()
#     visited.add(start)
#     que.append((start, 0, []))
#
#     while que:
#         (qi, qj), cnt, path = que.popleft()
#         path = path + [(qi, qj)]
#         # print(path)
#         # print(qi, qj)
#         if (qi, qj) == end:
#             return path
#
#         for di, dj in direction:
#             ni, nj = qi + di, qj + dj
#             if 0 <= ni < N and 0 <= nj < N:
#                 if (ni, nj) not in visited:
#                     now = arr[ni][nj]
#                     if now == 'G' or now == 'Y':
#                         que.append(((ni,nj), cnt, path))
#                         visited.add((ni, nj))
#                     elif now == 'T':
#                         if cnt < M:
#                             que.append(((ni,nj), cnt + 1, path))
#                             visited.add((ni, nj))
#
#     return []
#
#
# direction = ((0, 1), (1, 0), (-1, 0), (0, -1))
# T = int(input())
# for tc in range(1, T + 1):
#     N, M = map(int, input().split())
#     arr = []
#     start_point = []
#     end_point = []
#     for i in range(N):
#         lst = list(input())
#         if not start_point or not end_point:
#             for j in range(N):
#                 if lst[j] == 'X':
#                     start_point = (i, j)
#                 elif lst[j] == 'Y':
#                     end_point = (i, j)
#         arr.append(lst)
#     result = BFS(start_point, end_point)
#
#     dir = (-1, 0)
#
#     print(len(result))
#     print(start_point)
#     print(end_point)
#     print(result)



#
# from collections import deque
#
# def BFS(start, end):
#     que = deque()
#     visited = [[[0] * (M + 1) for _ in range(N)] for _ in range(N)]
#     visited[start[0]][start[1]][0] = 1
#     que.append((start[0], start[1], 0, []))
#     while que:
#         qi, qj, tree, path = que.popleft()
#         if (qi, qj) == end:
#             return visited[qi][qj][tree], path
#
#         for di, dj in direction:
#             ni, nj = qi + di, qj + dj
#             if 0 <= ni < N and 0 <= nj < N:
#                 if arr[ni][nj] != 'T' and visited[ni][nj][tree] == 0:
#                     visited[ni][nj][tree] = visited[qi][qj][tree] + 1
#                     que.append((ni, nj, tree, path + [(ni, nj)]))
#                 elif arr[ni][nj] == 'T' and tree < M:
#                     visited[ni][nj][tree + 1] = visited[qi][qj][tree] + 1
#                     que.append((ni, nj, tree+1, path + [(ni, nj)]))
#     return -1
#
#
# direction = ((0, 1), (1, 0), (-1, 0), (0, -1))
# T = int(input())
# for tc in range(1, T + 1):
#     N, M = map(int, input().split())
#     arr = []
#     start_point = []
#     end_point = []
#     for i in range(N):
#         lst = list(input())
#         if not start_point or not end_point:
#             for j in range(N):
#                 if lst[j] == 'X':
#                     start_point = (i, j)
#                 elif lst[j] == 'Y':
#                     end_point = (i, j)
#         arr.append(lst)
#     way, result = BFS(start_point, end_point)


from collections import deque

# 방향: 상, 우, 하, 좌
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def solution(N, K, field):
    start_x, start_y = None, None
    end_x, end_y = None, None

    # 시작점과 끝점 찾기
    for i in range(N):
        for j in range(N):
            if field[i][j] == 'X':
                start_x, start_y = i, j
            elif field[i][j] == 'Y':
                end_x, end_y = i, j

    # BFS 함수
    def bfs(cut_trees):
        queue = deque([(start_x, start_y, 0, 0, cut_trees)])  # x, y, direction, moves, cut_trees
        visited = set([(start_x, start_y, 0, tuple(cut_trees))])

        while queue:
            x, y, direction, moves, current_cut_trees = queue.popleft()

            if x == end_x and y == end_y:
                return moves

            # 전진
            nx, ny = x + dx[direction], y + dy[direction]
            if 0 <= nx < N and 0 <= ny < N:
                if field[nx][ny] == 'G' or field[nx][ny] == 'Y' or (nx, ny) in current_cut_trees:
                    if (nx, ny, direction, tuple(current_cut_trees)) not in visited:
                        queue.append((nx, ny, direction, moves + 1, current_cut_trees))
                        visited.add((nx, ny, direction, tuple(current_cut_trees)))
                elif field[nx][ny] == 'T' and len(current_cut_trees) < K:
                    new_cut_trees = current_cut_trees + [(nx, ny)]
                    if (nx, ny, direction, tuple(new_cut_trees)) not in visited:
                        queue.append((nx, ny, direction, moves + 1, new_cut_trees))
                        visited.add((nx, ny, direction, tuple(new_cut_trees)))

            # 좌회전
            new_direction = (direction - 1) % 4
            if (x, y, new_direction, tuple(current_cut_trees)) not in visited:
                queue.append((x, y, new_direction, moves + 1, current_cut_trees))
                visited.add((x, y, new_direction, tuple(current_cut_trees)))

            # 우회전
            new_direction = (direction + 1) % 4
            if (x, y, new_direction, tuple(current_cut_trees)) not in visited:
                queue.append((x, y, new_direction, moves + 1, current_cut_trees))
                visited.add((x, y, new_direction, tuple(current_cut_trees)))

        return -1

    return bfs([])


# 테스트 케이스 실행
T = int(input())
for t in range(1, T + 1):
    N, K = map(int, input().split())
    field = [input().strip() for _ in range(N)]
    result = solution(N, K, field)
    print(f"#{t} {result}")