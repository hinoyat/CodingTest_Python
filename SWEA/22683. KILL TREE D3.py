from collections import deque
direction = {0 : (-1, 0), 1 : (0, 1), 2 : (1, 0), 3 : (0, -1)}

def daddys_love(start, end):
    que = deque()
    visited = set()
    d = 0
    path = []
    que.append((start, 0, d, tuple(), path))
    visited.add((start, d, tuple()))

    while que:
        (qi, qj), move, di, tree, path = que.popleft()
        if (qi, qj) == end:
            return move, path

        ni, nj = qi + direction[di][0], qj + direction[di][1]

        if 0 <= ni < N and 0 <= nj < N and ((ni, nj), di, tree) not in visited:
            if arr[ni][nj] == 'G' or arr[ni][nj] == 'Y' or (ni, nj) in tree:
                que.append(((ni, nj), move + 1 , di, tree, path + [(ni, nj)]))
                visited.add(((ni, nj), di, tree))
            else:
                if len(tree) < M:
                    new_tree = tree + ((ni, nj),)
                    que.append(((ni, nj), move + 1 , di, new_tree, path + [(ni, nj)]))
                    visited.add(((ni, nj), di,  new_tree))
        ldi = (di - 1) % 4
        if ((qi, qj), ldi, tree) not in visited:
            visited.add(((qi, qj), ldi, tree))
            que.append(((qi, qj), move + 1, ldi, tree, path + [(qi, qj)]))

        rdi = (di + 1) % 4
        if ((qi, qj), rdi, tree) not in visited:
            visited.add(((qi, qj), rdi, tree))
            que.append(((qi, qj), move + 1, rdi, tree, path + [(qi, qj)]))

    return -1, []

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = []
    start_point = ()
    end_point = ()
    for i in range(N):
        lst = list(input())
        if not start_point or not end_point:
            for j in range(N):
                if lst[j] == 'X':
                    start_point = (i, j)
                elif lst[j] == 'Y':
                    end_point = (i, j)
        arr.append(lst)

    result, path = daddys_love(start_point, end_point)


    print(f'#{tc} {result}')
    # print(path)
