from collections import deque

def losing_ice():
    global earth
    new_earth =[[0] * M for _ in range(N)]

    can = 0
    for i in range(N):
        can += sum(earth[i])

    if can == 0:
        return -1

    for i in range(N):
        for j in range(M):
            if earth[i][j] > 0:
                water = 0
                for di, dj in ((0, 1), (1, 0), (-1, 0), (0, -1)):
                    ni, nj = i + di, j + dj
                    if 0 <= ni < N and 0 <= nj < M and earth[ni][nj] == 0:
                        water += 1
                new_val = max(0, earth[i][j] - water)
                new_earth[i][j] = new_val

    earth = new_earth
    return 1


def check():
    que = deque()
    cnt = 0
    visited = [[0] * M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if earth[i][j] != 0 and not visited[i][j]:
                cnt += 1
                que.append((i, j))
                visited[i][j] = 1
                while que:
                    qi, qj = que.popleft()
                    for di, dj in ((0, 1), (1, 0), (-1, 0), (0, -1)):
                        ni, nj = qi + di, qj + dj
                        if 0 <= ni < N and 0 <= nj < M and not visited[ni][nj] and earth[ni][nj] != 0:
                            que.append((ni, nj))
                            visited[ni][nj] = 1
    return cnt




N, M = map(int, input().split())

ans = 0

earth = [list(map(int, input().split())) for _ in range(N)]
# print('이게 뭐야.. 신기하다..')

go = 1
while True:
    cnt = check()
    if cnt >= 2:
        break

    going = losing_ice()
    ans += 1
    if going == -1:
        ans = 0
        break

print(ans)

