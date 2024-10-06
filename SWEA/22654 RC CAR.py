from collections import deque

direction = {0 : (-1, 0), 1 : (0, 1), 2 : (1, 0), 3 : (0, -1)}

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = []
    sti = 0
    stj = 0
    end_point = ()
    for i in range(N):
        lst = list(input())
        for j in range(N):
            if lst[j] == 'X':
                sti = i
                stj = j
            elif lst[j] == 'Y':
                end_point = (i, j)
        arr.append(lst)

    game_cnt = int(input())
    game = deque()
    for _ in range(game_cnt):
        game.append(input().split())

    result = []
    for _ in range(game_cnt):
        num, order = game.popleft()
        si, sj = sti, stj
        di = 0
        for o in order:
            if o == 'R':
                di = (di + 1) % 4
            if o == 'L':
                di = (di + -1) % 4
            if o == 'A':
                ni, nj = si + direction[di][0], sj + direction[di][1]
                if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] != 'T':
                    si, sj = ni, nj

        if arr[si][sj] == 'Y':
            result.append(1)
        else:
            result.append(0)

    print(f'#{tc}', end=' ')
    print(*result)




