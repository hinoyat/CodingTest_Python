def find_max_len(si, sj, len_way, is_down, now):
    global ans

    if len_way >= ans:
        ans = max(ans, len_way)


    for di, dj in ((0, 1), (1, 0), (-1, 0), (0, -1)):
        ni, nj = si + di, sj + dj
        if 0 <= ni < N and 0 <= nj < N and not visited[ni][nj]:
            new_point = arr[ni][nj]
            if new_point <= 0:continue
            if new_point < now:
                visited[ni][nj] = 1
                find_max_len(ni, nj, len_way + 1, is_down, new_point)
                visited[ni][nj] = 0
            elif new_point - K < now and is_down == 0:
                visited[ni][nj] = 1
                find_max_len(ni, nj, len_way + 1, is_down + 1, now-1)
                visited[ni][nj] = 0



T = int(input())
for tc in range(1, T + 1):
    N, K = map(int, input().split())
    arr = []
    max_height = 0
    for i in range(N):
        lst = list(map(int, input().split()))
        max_height = max(max_height, max(lst))
        arr.append(lst)
    ans = 0

    visited = [[0] * N for _ in range(N)]


    for i in range(N):
        for j in range(N):
            if arr[i][j] == max_height:
                visited[i][j] = 1
                find_max_len(i, j, 1, 0, max_height)
                visited[i][j] = 0
    print(f'#{tc} {ans}')
