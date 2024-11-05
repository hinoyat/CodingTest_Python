from collections import deque

def supernova(start):
    que = deque()
    visited = [[0] * M for _ in range(N)]
    que.append(start)
    visited[start[0]][start[1]] = 1
    new_cheeze = [[0] * M for _ in range(N)]
    while que:
        qi, qj = que.popleft()
        for di, dj in ((0, 1), (1, 0), (-1, 0), (0, -1)):
            ni, nj = qi + di, qj + dj
            if 0 <= ni < N and 0 <= nj < M and not visited[ni][nj]:
                if cheeze[ni][nj] == 1:
                    new_cheeze[ni][nj] += 1
                elif cheeze[ni][nj] == 0:
                    que.append((ni, nj))
                    visited[ni][nj] = 1

    for i in range(N):
        for j in range(M):
            if new_cheeze[i][j] >= 2:
                cheeze[i][j] = 0




def check():
    remain_cheeze = 0
    for i in cheeze:
        remain_cheeze += sum(i)
    return remain_cheeze


N, M = map(int, input().split())
cheeze = [list(map(int, input().split())) for _ in range(N)]
start_point = (0, 0)
time = 0
while True:
    checking = check()
    if checking == 0:
        break

    supernova(start_point)
    time += 1
print(time)