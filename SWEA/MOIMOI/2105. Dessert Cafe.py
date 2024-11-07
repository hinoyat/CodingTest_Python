def find_desert(start, i, j, dir, len1, len3, total_len):
    global ans
    if dir == 4 and len1 != len3:
        return

    if dir == 3 and total_len * 2 <= ans:
        return
    if i < 0 or j < 0 or i >=N or j >= N :
        return

    if (i, j) == start and dir == 4:
        ans = max(ans, len(check))
        return

    if arr[i][j] in check:
        return

    check.add(arr[i][j])
    ni, nj = i + direction[dir][0], j + direction[dir][1]
    if dir == 1:
        find_desert(start, ni, nj, dir, len1 + 1, len3, total_len + 1)
        if total_len > 0:
            find_desert(start, ni, nj, dir + 1, len1 + 1, len3, total_len + 1)
    elif dir == 2:

        find_desert(start, ni, nj, dir, len1, len3, total_len + 1)
        if total_len > 0:
            find_desert(start, ni, nj, dir + 1, len1, len3, total_len + 1)
    elif dir == 3:
        find_desert(start, ni, nj, dir, len1, len3 + 1, total_len + 1)
        if total_len > 0:
            find_desert(start, ni, nj, dir + 1, len1, len3 + 1, total_len + 1)
    elif dir == 4:
        find_desert(start, ni, nj, dir, len1, len3, total_len + 1)
    check.remove(arr[i][j])




direction = {
    1 : (1, 1),
    2 : (1, -1),
    3 : (-1, -1),
    4 : (-1, 1)
}

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    ans = -1
    for si in range(N - 1):
        for sj in range(N - 1):
            check = set()
            find_desert((si, sj), si, sj, 1, 0, 0, 1)
    print(f'#{tc} {ans}')