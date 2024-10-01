from collections import deque


def moving(si, sj):
    que = deque()
    que.append((si, sj))
    visited[si][sj] = 1
    moved = [(si, sj)]

    population = country[si][sj]

    while que:
        qi, qj = que.popleft()
        for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            ni, nj = qi + di, qj + dj
            if 0<= ni < N and 0 <= nj < N and not visited[ni][nj]:
                if L <= abs(country[qi][qj] - country[ni][nj]) <= R:
                    que.append((ni, nj))
                    visited[ni][nj] = 1
                    moved.append((ni, nj))
                    population += country[ni][nj]

    country_num = len(moved)

    if country_num > 1:
        new_population = int(population/country_num)
        for i, j in moved:
            country[i][j] = new_population
        return True
    else:
        return False



N, L, R = map(int, input().split())

country = [list(map(int, input().split())) for _ in range(N)]



day = 0

while True:
    visited = [[0] * N for _ in range(N)]

    moved = False

    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                result = moving(i, j)
                if result:
                    moved = True

    if moved:
        day += 1
    else:
        break

print(day)