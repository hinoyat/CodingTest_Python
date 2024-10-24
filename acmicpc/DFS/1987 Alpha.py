def supernova(point, cnt):
    global ans
    i = point[0]
    j = point[1]
    for ni, nj in ((i, j + 1), (i + 1, j), (i - 1, j), (i, j - 1),):
        if 0 <= ni < R and 0 <= nj < C and board[ni][nj] not in visited:
            visited.add(board[ni][nj])
            supernova((ni, nj), cnt + 1)
            visited.remove(board[ni][nj])
    ans = max(ans, cnt)
    return

R, C = map(int, input().split())
board = [list(input()) for _ in range(R)]
ans = 1
# 시작 지점
start_point = (0, 0)
# 시작 알파벳
start = board[0][0]

# 방문 기록
visited = set()
visited.add(start)
supernova(start_point, ans)

print(ans)