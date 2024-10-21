'''
4 5
Z1--4
23..|
....|
....M

4 4
Z4..
2+-4
.|.|
.2-M
'''


from collections import deque
# 끊어진 곳
def find_point(start):

    que = deque()
    visited = [[0] * C for _ in range(R)]
    for si, sj in start:
        que.append((si,sj))
        visited[si][sj] = 1
    while que:
        qi, qj = que.popleft()
        now = gas_map[qi][qj]
        if now == '.':
            return (qi, qj)

        for di, dj in moving_gas[now]:
            ni, nj = qi + di, qj + dj
            if 0 <= ni < R and 0 <= nj < C:
                if not visited[ni][nj]:
                    que.append((ni, nj))
                    visited[ni][nj] = 1



def gas_move(start):
    que = deque()
    visited = [[0] * C for _ in range(R)]
    check_normal = set()
    for si, sj in start:
        que.append((si,sj))
        visited[si][sj] = 1
    while que:
        qi, qj = que.popleft()
        now = gas_map[qi][qj]
        if '.' in check_normal:
            return False
        for di, dj in moving_gas[now]:
            ni, nj = qi + di, qj + dj
            if 0 <= ni < R and 0 <= nj < C:
                if gas_map[ni][nj] in ('Z', 'M'):
                    visited[ni][nj] = 1
                    check_normal.add(gas_map[ni][nj])

                elif gas_map[ni][nj] != '.':
                    if (-di, -dj) in moving_gas[gas_map[ni][nj]]:
                        if not visited[ni][nj]:
                            que.append((ni, nj))
                            visited[ni][nj] = 1
                            check_normal.add(gas_map[ni][nj])
                    else:
                        return False
                else:
                    if not visited[ni][nj]:
                        que.append((ni, nj))
                        visited[ni][nj] = 1
                        check_normal.add(gas_map[ni][nj])
            else:
                return False


    for i in range(R):
        for j in range(C):
            if gas_map[i][j] != '.' and visited[i][j]==0:
                return False
    return True




# 행의 수, 열=의; 수
R, C = map(int,input().split())

moving_gas = {
    '|' : ((1, 0), (-1, 0)),
    '-' : ((0, 1), (0, -1)),
    '+' : ((0, 1), (1, 0), (-1, 0), (0, -1)),
    '1' : ((0, 1), (1, 0)),
    '2' : ((-1, 0), (0, 1)),
    '3' : ((-1, 0), (0, -1)),
    '4' : ((0, -1), (1, 0)),
    'M' : ((0, 0),),
    'Z' : ((0, 0),),
}
# 맵 입력 1 X 1 크기의 맵도 존재 가능, 최대 25 X 25

from pprint import pprint
gas_map = [list(input()) for _ in range(R)]

# 연결 할 지점 찾기
# 방법 1 시작에서 가고 끝에서 가고 가스가 새는 부분 있으면 거기에 하나씩 넣어보기
M = []
Z = []
russia = ()
croatia = ()
for i in range(R):
    for j in range(C):
        if gas_map[i][j] == 'M':
            russia = (i, j)
            for di, dj in ((0, 1), (1, 0), (0, -1), (-1, 0)):
                ni, nj = i + di, j + dj
                if 0 <= ni < R and 0 <= nj < C:
                    if gas_map[ni][nj] in moving_gas:
                        if (-di, -dj) in moving_gas[gas_map[ni][nj]]:
                            M.append((ni, nj))
        elif gas_map[i][j] == 'Z':
            croatia = (i, j)
            for di, dj in ((0, 1), (1, 0), (0, -1), (-1, 0)):
                ni, nj = i + di, j + dj
                if 0 <= ni < R and 0 <= nj < C:
                    if gas_map[ni][nj] in moving_gas:
                        if (-di, -dj) in moving_gas[gas_map[ni][nj]]:
                            Z.append((ni, nj))
    if M and Z:
        break

break_point = find_point(M)
ans = ''

for pipe in moving_gas:
    gas_map[break_point[0]][break_point[1]] = pipe

    result = gas_move(M + Z)
    if result:
        ans = pipe
        break

ai = break_point[0]
aj = break_point[1]
ai += 1
aj += 1

print(ai, aj, ans)
