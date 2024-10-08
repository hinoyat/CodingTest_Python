from collections import deque
direction = {0 : (-1, 0, 'U'), 1 : (0, 1, 'R'), 2 : (1, 0, 'D'), 3 : (0, -1, 'L')}


def find_F(start, end):
    que = deque()
    visited = set()
    d = 0
    path = []
    order = []
    que.append((start, 0, d, tuple(), path, order))
    visited.add((start, d, tuple()))

    while que:
        (qi, qj), move, di, tree, path, order = que.popleft()
        if (qi, qj) == end:
            return move, path, order + ['G']

        ni, nj = qi + direction[di][0], qj + direction[di][1]

        if 0 <= ni < N and 0 <= nj < N and ((ni, nj), di, tree) not in visited:
            if arr[ni][nj] == 'G' or arr[ni][nj] == 'X' or arr[ni][nj] == 'F' or (ni, nj) in tree:
                que.append(((ni, nj), move + 1 , di, tree, path + [(ni, nj)], order + ['A']))
                visited.add(((ni, nj), di, tree))
            else:
                if len(tree) < M:
                    new_tree = tree + ((ni, nj),)
                    que.append(((ni, nj), move + 1 , di, new_tree, path + [(ni, nj)], order + ['F', 'A']))
                    visited.add(((ni, nj), di,  new_tree))
        ldi = (di - 1) % 4
        if ((qi, qj), ldi, tree) not in visited:
            visited.add(((qi, qj), ldi, tree))
            que.append(((qi, qj), move + 1, ldi, tree, path + [(qi, qj)], order + [direction[ldi][2]]))

        rdi = (di + 1) % 4
        if ((qi, qj), rdi, tree) not in visited:
            visited.add(((qi, qj), rdi, tree))
            que.append(((qi, qj), move + 1, rdi, tree, path + [(qi, qj)], order + [direction[rdi][2]]))

    return -1, [], []


def hacking(hint):
    result = 'G '
    for h in hint:
        result += chr((ord(h) - 65 + 9) % 26 + 65)

    return result


def daddys_love(start, end):
    que = deque()
    visited = set()
    d = 0
    path = []
    order = []
    que.append((start, 0, d, tuple(), path, order))
    visited.add((start, d, tuple()))

    while que:
        (qi, qj), move, di, tree, path, order = que.popleft()
        if (qi, qj) == end:
            return move, path, order + ['F']

        ni, nj = qi + direction[di][0], qj + direction[di][1]

        if 0 <= ni < N and 0 <= nj < N and ((ni, nj), di, tree) not in visited:
            if arr[ni][nj] == 'G' or arr[ni][nj] == 'X' or (ni, nj) in tree:
                que.append(((ni, nj), move + 1 , di, tree, path + [(ni, nj)], order + ['A']))
                visited.add(((ni, nj), di, tree))
            else:
                if len(tree) < M:
                    new_tree = tree + ((ni, nj),)
                    que.append(((ni, nj), move + 1 , di, new_tree, path + [(ni, nj)], order + ['F', 'A']))
                    visited.add(((ni, nj), di,  new_tree))
        ldi = (di - 1) % 4
        if ((qi, qj), ldi, tree) not in visited:
            visited.add(((qi, qj), ldi, tree))
            que.append(((qi, qj), move + 1, ldi, tree, path + [(qi, qj)], order + [direction[ldi][2]]))

        rdi = (di + 1) % 4
        if ((qi, qj), rdi, tree) not in visited:
            visited.add(((qi, qj), rdi, tree))
            que.append(((qi, qj), move + 1, rdi, tree, path + [(qi, qj)], order + [direction[rdi][2]]))

    return -1, [], []


N, M = map(int, input().split())
arr = []
start_point = ()
end_point = ()
hacking_point = ()
for i in range(N):
    lst = list(input().split())
    if not start_point or not end_point:
        for j in range(N):
            if lst[j] == 'A':
                start_point = (i, j)
            elif lst[j] == 'X':
                end_point = (i, j)
            elif lst[j] == 'F':
                hacking_point = (i, j)

    arr.append(lst)
# print(end_point)


# print('최적 경로')
# result, path, order = daddys_love(start_point, end_point)
# print(path)
# print(order)

print(hacking('SRKKCVJJRWP'))

# result2, path2, order2 = find_F(start_point, hacking_point)
# print('보급 경로')
# print(path2)
# print(order2)