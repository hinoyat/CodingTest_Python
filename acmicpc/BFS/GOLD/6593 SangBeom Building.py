from collections import deque

def run(h, i, j):
    que = deque()
    visited = [[[-1] * C for _ in range(R)]for _ in range(L)]
    visited[h][i][j] = 0
    que.append((h, i, j))
    while que:
        qh, qi, qj = que.popleft()
        if building[qh][qi][qj] == 'E':
            return visited[qh][qi][qj]
        for dh, di, dj in ((0, 0, 1), (0, 0, -1), (0, 1, 0), (0, -1, 0), (-1, 0, 0), (1, 0, 0)):
            nh, ni, nj = qh + dh, qi + di, qj + dj
            if 0 <= nh < L and 0 <= ni < R and 0 <= nj < C and visited[nh][ni][nj] == -1 and building[nh][ni][nj] != '#':
                visited[nh][ni][nj] = visited[qh][qi][qj] + 1
                que.append((nh, ni, nj))
    return -1

# L, R, C = map(int, input().split())
while True:
    L, R, C = map(int, input().split())
    if (L, R, C) == (0, 0, 0):
        break
    building = []
    for l in range(L):
        level = []
        for r in range(R):
            row = list(input())

            level.append(row)
        input()
        building.append(level)
    # input()
    # pprint(building)
    sh = 0
    si = 0
    sj = 0
    find = False
    for h in range(L):
        for i in range(R):
            for j in range(C):
                if building[h][i][j] == 'S':
                    sh = h
                    si = i
                    sj = j
                    find = True
                    break
            if find == True:
                break
        if find == True:
            break
    # print(si, sj)

    # pprint(building)

    result = run(sh, si, sj)
    if result == -1:
        print('Trapped!')
    else:
        print(f'Escaped in {result} minute(s).')


'''
리뷰

- 빌딩 입력 받을 때 공백이 있어서 어지러웠다
- 틀린 이유는 마지막 결과 출력할 때 result == -1 이게 아니라 not result로 설정한 것이 문제였다.
 
'''