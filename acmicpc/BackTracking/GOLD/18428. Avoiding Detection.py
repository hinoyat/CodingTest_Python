def check_student(arr):

    pass

def backtrack(array, wall):
    global ans

    if wall == 3:
        student = check_student(array)
        if not student:
            ans = 'YES'
        return

def first_check(si, sj):
    path = []
    direction = ((0, 1), (1, 0), (0, -1), (-1, 0))
    ni = si
    nj = sj
    temp_p = []
    for d in range(4):
        while True:
            ni, nj = ni + direction[d][0], nj + direction[d][1]
            if 0 <= ni < N and 0 <= nj < N:
                if board[ni][nj] == 'S':
                    path += temp_p
                    temp_p = []
                    ni, nj = si, sj
                    break
                else:
                    temp_p.append((ni, nj))

            else:
                ni = si
                nj = sj
                temp_p = []
                break

    return path


N = int(input())
board = [list(input().split()) for _ in range(N)]

ans = 'NO'

make_wall_point = []
teacher_point = []
for i in range(N):
    for j in range(N):
        if board[i][j] == "T":
            teacher_point.append((i, j))
            temp_path = first_check(i, j)
            make_wall_point += temp_path

