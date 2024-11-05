def check_water(start):
    temp = 0
    si = start[0]
    sj = start[1]
    while True:
        sj += 1
        if sj >= M:
            break
        if arr[si][sj] == 1:
            return temp
        else:
            temp += 1

        visited[si][sj] = 1

    return 0


N, M = map(int, input().split())
info = list(map(int, input().split()))

ans = 0

arr = [[0] * M for _ in range(N)]
visited = [[0] * M for _ in range(N)]

for i in range(M):
    if info[i] != 0:
        for j in range(info[i]):
            arr[N - 1 - j][i] = 1

for i in range(N-1, -1, -1):
    for j in range(M):
        if arr[i][j] == 1 and not visited[i][j]:
            ans += check_water((i, j))
            visited[i][j] = 1

print(ans)

"""
현호야  안뇽
공부 열심히 하고있어??
아니 안쓸래
현호 여자친구ㅡㅡㅡㅡㅡ\
                     \
                      \
                       \
                        \
                         \
                          \
                           \
                            \
                            \/
"""
