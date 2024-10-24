# 점프왕 쩰리(Large)
# 이거 시간초과 계속 나서 다른 사람 풀이 참고함

def hongbeom(point, end):
    global game_over

    i, j = point

    visited.add((i, j))
    di = [game_board[i][j],0]
    dj = [0,game_board[i][j]]

    for d in range(2):
        ni, nj = i + di[d], j + dj[d]
        if 0 <= ni < N and 0 <= nj < N and (ni, nj) not in visited:
            hongbeom((ni, nj), end)


N = int(input())
game_board = [list(map(int, input().split())) for _ in range(N)]
start_point = (0, 0)
end_point = (N - 1, N - 1)
visited = set()

game_over = False

hongbeom(start_point, end_point)

if (N-1, N-1) in visited:
    print("HaruHaru")
else:
    print("Hing")
