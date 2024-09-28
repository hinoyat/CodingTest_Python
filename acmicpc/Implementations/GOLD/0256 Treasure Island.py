# 보물 섬

'''
1. 일단 육지 체크 하면서 육지 표시 한다
2. 구석탱이를 찾는 법은 상하 좌우 봤을 때 육지인 곳이 1곳 인 땅일까?
'''
from collections import deque

def find_land(si, sj):
    find_info = [[-1] * M for _ in range(N)]
    que = deque()
    find_info[si][sj] = 0
    que.append((si, sj))
    time = 0
    while que:
        qi, qj = que.popleft()
        time = max(time, find_info[qi][qj])
        for di, dj in ((0, 1), (0, -1), (1, 0), (-1, 0)):
            ni, nj = qi + di, qj + dj
            if 0 > ni or 0 > nj or ni >= N or nj >= M or find_info[ni][nj] != - 1 or island_map[ni][nj] == 'W':
                continue
            find_info[ni][nj] = find_info[qi][qj] + 1
            que.append((ni, nj))
    return time


N, M = map(int, input().split())

island_map = [list(input()) for _ in range(N)]

land = []
start_point = []
# 엣지 포인트 찾기
for i in range(N):
    for j in range(M):
        if island_map[i][j] == "W":
            continue
        edge = 0
        for ei, ej in ((i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)):
            if 0 <= ei < N and 0 <= ej < M and island_map[ei][ej] == 'L':
                continue
            edge += 1
        if edge == 3:
            start_point.append((i, j))

result = -1
if not start_point:
    for i in range(N):
        for j in range(M):
            if island_map[i][j] != 'W':
                result = max(result, find_land(i,j))
else:
    for i, j in start_point:
        result = max(result, find_land(i,j))


print(result)