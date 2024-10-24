import sys
sys.setrecursionlimit(10**6)
# 재귀 함수 작성이 좀 이상한듯? 그래서 recursionerror 나지 않았을까?

def superDFS(start):
    global surface
    si, sj = start
    checked[si][sj] = 1
    surface += 1
    for di, dj in ((0, 1), (1, 0), (-1, 0), (0, -1)):
        ni, nj = si + di, sj + dj
        if 0 <= ni < N and 0 <= nj < M and not checked[ni][nj] and board[ni][nj] == 1:
            superDFS((ni, nj))




N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
checked = [[0] * M for _ in range(N)]
ans = 0
area = 0
for i in range(N):
    for j in range(M):
        if not checked[i][j] and board[i][j] == 1:
            surface = 0
            superDFS((i, j))
            ans += 1
            area = max(area, surface)

print(ans)
print(area)