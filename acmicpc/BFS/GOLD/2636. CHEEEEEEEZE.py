from collections import deque

def supernova(start):
    que = deque()
    visited = [[0] * M for _ in range(N)]
    que.append(start)
    visited[start[0]][start[1]] = 1
    deleted = []

    while que:
        qi, qj = que.popleft()
        for di, dj in ((0, 1), (1, 0), (-1, 0), (0, -1)):
            ni, nj = qi + di, qj + dj
            if 0 <= ni < N and 0 <= nj < M and not visited[ni][nj]:
                if cheeze[ni][nj] == 1:
                    deleted.append((ni, nj))
                elif cheeze[ni][nj] == 0:
                    que.append((ni, nj))
                visited[ni][nj] = 1
    for i, j in deleted:
        cheeze[i][j] = 0

def check():
    remain_cheeze = 0
    for i in cheeze:
        remain_cheeze += sum(i)
    return remain_cheeze





N, M = map(int, input().split())
cheeze = [list(map(int, input().split())) for _ in range(N)]

start_point = (0, 0)
ans = 0
time = 0
while True:
    checking = check()
    if checking == 0:
        break

    ans = checking

    supernova(start_point)
    time += 1
print(time)
print(ans)




























